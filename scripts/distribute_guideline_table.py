#!/usr/bin/env python3
"""Distribute rows from one Markdown table to linked pages.

For each source row, this script follows the internal Markdown link in the
first cell and adds a row to a table on that page. The new row replaces the
source row's first cell with a caller-supplied cell and preserves all remaining
source cells.

Run from anywhere in the repository:

    python3 scripts/distribute_guideline_table.py \
        --link '[External standard](...)' \
        --source path/to/table.md \
        --content-root path/to/content \
        --dry-run

The script preflights every source row and destination before writing any
files.  It is safe to rerun: existing rows beginning with the supplied link
are removed before one fresh row is appended.
"""

from __future__ import annotations

import argparse
import os
import re
import stat
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple
from urllib.parse import unquote, urlsplit


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK_RE = re.compile(
    r"^\[(?P<label>(?:\\.|[^\]])+)\]"
    r"\(\s*<?(?P<url>[^\s>)]+)>?(?:\s+['\"][^'\"]*['\"])?\s*\)$"
)
HEADING_RE = re.compile(r"^(?P<marks>#{1,6})\s+(?P<title>.*?)\s*$")
SEPARATOR_CELL_RE = re.compile(r"^:?-{3,}:?$")


class DistributionError(Exception):
    """Raised when input cannot be distributed without ambiguity."""


@dataclass(frozen=True)
class SourceRow:
    label: str
    destination_url: str
    line_number: int
    cells: Tuple[str, ...]

    def destination_cells(self, distributed_link: str) -> Tuple[str, ...]:
        return (distributed_link, *self.cells[1:])


@dataclass(frozen=True)
class MarkdownTable:
    header_index: int
    separator_index: int
    first_data_index: int
    end_index: int
    header_cells: Tuple[str, ...]


@dataclass(frozen=True)
class PlannedChange:
    path: Path
    original: str
    updated: str
    action: str


def parse_markdown_row(line: str) -> Optional[Tuple[str, ...]]:
    """Return trimmed cells from a pipe-delimited Markdown row.

    Pipes escaped with a backslash remain part of the cell content.
    """

    stripped = line.rstrip("\r\n").strip()
    if not (stripped.startswith("|") and stripped.endswith("|")):
        return None

    body = stripped[1:-1]
    cells: List[str] = []
    current: List[str] = []
    backslash_run = 0

    for character in body:
        if character == "|" and backslash_run % 2 == 0:
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(character)

        if character == "\\":
            backslash_run += 1
        else:
            backslash_run = 0

    cells.append("".join(current).strip())
    return tuple(cells)


def is_separator_row(cells: Optional[Tuple[str, ...]]) -> bool:
    return bool(cells) and all(SEPARATOR_CELL_RE.fullmatch(cell) for cell in cells)


def find_markdown_tables(
    lines: Sequence[str], start: int = 0, end: Optional[int] = None
) -> List[MarkdownTable]:
    """Find conventional Markdown tables between two line indexes."""

    if end is None:
        end = len(lines)

    tables: List[MarkdownTable] = []
    index = start
    while index + 1 < end:
        header = parse_markdown_row(lines[index])
        separator = parse_markdown_row(lines[index + 1])
        if header is None or not is_separator_row(separator):
            index += 1
            continue

        if len(header) != len(separator):
            index += 1
            continue

        table_end = index + 2
        while table_end < end and parse_markdown_row(lines[table_end]) is not None:
            table_end += 1

        tables.append(
            MarkdownTable(
                header_index=index,
                separator_index=index + 1,
                first_data_index=index + 2,
                end_index=table_end,
                header_cells=header,
            )
        )
        index = table_end

    return tables


def read_utf8(path: Path) -> str:
    try:
        return path.read_bytes().decode("utf-8")
    except FileNotFoundError as error:
        raise DistributionError(f"File does not exist: {path}") from error
    except UnicodeDecodeError as error:
        raise DistributionError(f"File is not valid UTF-8: {path}") from error


def parse_source_rows(source: Path, table_index: int) -> List[SourceRow]:
    text = read_utf8(source)
    lines = text.splitlines(keepends=True)
    tables = find_markdown_tables(lines)

    if not tables:
        raise DistributionError(f"No Markdown tables found in {source}")
    if table_index > len(tables):
        raise DistributionError(
            f"Requested source table {table_index} in {source}, but only "
            f"{len(tables)} table(s) were found"
        )

    table = tables[table_index - 1]
    rows: List[SourceRow] = []

    for line_index in range(table.first_data_index, table.end_index):
        cells = parse_markdown_row(lines[line_index])
        if cells is None or not cells:
            raise DistributionError(
                f"Malformed source row at {source}:{line_index + 1}"
            )

        match = MARKDOWN_LINK_RE.fullmatch(cells[0])
        if match is None:
            raise DistributionError(
                f"The first cell at {source}:{line_index + 1} is not a "
                "supported Markdown link"
            )

        rows.append(
            SourceRow(
                label=match.group("label"),
                destination_url=match.group("url"),
                line_number=line_index + 1,
                cells=cells,
            )
        )

    if not rows:
        raise DistributionError(f"The source table in {source} has no data rows")

    return rows


def unnumbered_name(name: str) -> str:
    """Remove a leading numeric ordering prefix from a path component."""

    return re.sub(r"^\d+\.", "", name)


def normalize_url_path(url: str, context: str) -> str:
    """Return a normalized site-relative path without query or fragment."""

    parsed = urlsplit(url)
    if parsed.scheme or parsed.netloc or not parsed.path.startswith("/"):
        raise DistributionError(
            f"Expected a site-relative destination URL in {context}, got {url!r}"
        )
    path = unquote(parsed.path)
    return path.rstrip("/") or "/"


def normalize_url_prefix(value: str) -> str:
    path = normalize_url_path(value, "--url-prefix")
    if path == "/":
        return ""
    return path


def route_for_page(content_root: Path, path: Path, url_prefix: str) -> str:
    relative = path.relative_to(content_root)
    components = [unnumbered_name(part) for part in relative.parts[:-1]]
    page_name = unnumbered_name(path.stem)
    if page_name != "index":
        components.append(page_name)

    suffix = "/".join(components)
    if not suffix:
        return url_prefix or "/"
    return f"{url_prefix}/{suffix}" if url_prefix else f"/{suffix}"


def build_page_index(
    content_root: Path, url_prefix: str
) -> Dict[str, List[Path]]:
    """Map site-relative page routes to local Markdown files."""

    if not content_root.is_dir():
        raise DistributionError(f"Content root does not exist: {content_root}")

    index: Dict[str, List[Path]] = {}
    for path in content_root.rglob("*.md"):
        route = route_for_page(content_root, path, url_prefix)
        index.setdefault(route, []).append(path)
    return index


def resolve_destination(
    row: SourceRow, source: Path, page_index: Dict[str, List[Path]]
) -> Path:
    context = f"{source}:{row.line_number}"
    route = normalize_url_path(row.destination_url, context)
    matches = page_index.get(route, [])
    if not matches:
        raise DistributionError(
            f"No local Markdown file found for {row.label!r} at {route} "
            f"({context})"
        )
    if len(matches) > 1:
        formatted_matches = ", ".join(str(path) for path in matches)
        raise DistributionError(
            f"Multiple local files map to {route} ({context}): {formatted_matches}"
        )
    return matches[0]


def find_section_bounds(lines: Sequence[str], title: str, path: Path) -> Tuple[int, int]:
    matches: List[Tuple[int, int]] = []

    for index, line in enumerate(lines):
        match = HEADING_RE.fullmatch(line.rstrip("\r\n"))
        if match is not None and match.group("title").strip() == title:
            matches.append((index, len(match.group("marks"))))

    if len(matches) != 1:
        raise DistributionError(
            f"Expected exactly one '{title}' section in {path}, found {len(matches)}"
        )

    section_start, heading_level = matches[0]
    section_end = len(lines)
    for index in range(section_start + 1, len(lines)):
        match = HEADING_RE.fullmatch(lines[index].rstrip("\r\n"))
        if match is not None and len(match.group("marks")) <= heading_level:
            section_end = index
            break

    return section_start + 1, section_end


def format_markdown_row(cells: Sequence[str], newline: str) -> str:
    return "| " + " | ".join(cells) + " |" + newline


def newline_for(text: str) -> str:
    if "\r\n" in text:
        return "\r\n"
    return "\n"


def plan_destination_update(
    path: Path,
    rows: Sequence[SourceRow],
    distributed_cell: str,
    target_section: str,
    target_table_header: str,
) -> Optional[PlannedChange]:
    original = read_utf8(path)
    lines = original.splitlines(keepends=True)
    section_start, section_end = find_section_bounds(
        lines, target_section, path
    )
    tables = [
        table
        for table in find_markdown_tables(lines, section_start, section_end)
        if table.header_cells and table.header_cells[0] == target_table_header
    ]

    if len(tables) != 1:
        raise DistributionError(
            f"Expected exactly one table beginning with {target_table_header!r} "
            f"in the {target_section!r} section of {path}, found {len(tables)}"
        )

    table = tables[0]
    matching_indexes: List[int] = []

    for line_index, line in enumerate(lines):
        cells = parse_markdown_row(line)
        if cells is not None and cells and cells[0] == distributed_cell:
            matching_indexes.append(line_index)

    newline = newline_for(original)
    desired_lines = [
        format_markdown_row(row.destination_cells(distributed_cell), newline)
        for row in rows
    ]
    matching_index_set = set(matching_indexes)

    if matching_indexes:
        lines = [
            line for line_index, line in enumerate(lines)
            if line_index not in matching_index_set
        ]

    removed_before_insertion = sum(
        line_index < table.end_index for line_index in matching_indexes
    )
    insertion_index = table.end_index - removed_before_insertion
    lines[insertion_index:insertion_index] = desired_lines
    updated = "".join(lines)
    if updated == original:
        return None

    return PlannedChange(
        path=path,
        original=original,
        updated=updated,
        action="updated" if matching_indexes else "inserted",
    )


def plan_changes(
    source: Path,
    content_root: Path,
    url_prefix: str,
    distributed_cell: str,
    source_table_index: int,
    target_section: str,
    target_table_header: str,
) -> Tuple[List[SourceRow], int, List[PlannedChange]]:
    """Validate every row and destination, then return the complete write plan."""

    rows = parse_source_rows(source, source_table_index)
    page_index = build_page_index(content_root, url_prefix)
    rows_by_destination: Dict[Path, List[SourceRow]] = {}

    for row in rows:
        destination = resolve_destination(row, source, page_index)
        rows_by_destination.setdefault(destination, []).append(row)

    changes: List[PlannedChange] = []
    for destination, destination_rows in rows_by_destination.items():
        change = plan_destination_update(
            destination,
            destination_rows,
            distributed_cell,
            target_section,
            target_table_header,
        )
        if change is not None:
            changes.append(change)

    return rows, len(rows_by_destination), changes


def write_atomic(change: PlannedChange) -> None:
    """Atomically replace one file while preserving its permission bits."""

    mode = stat.S_IMODE(change.path.stat().st_mode)
    temporary_name: Optional[str] = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb", prefix=f".{change.path.name}.", dir=change.path.parent,
            delete=False
        ) as temporary:
            temporary_name = temporary.name
            temporary.write(change.updated.encode("utf-8"))
            temporary.flush()
            os.fsync(temporary.fileno())

        os.chmod(temporary_name, mode)
        os.replace(temporary_name, change.path)
        temporary_name = None
    finally:
        if temporary_name is not None:
            try:
                os.unlink(temporary_name)
            except FileNotFoundError:
                pass


def path_argument(value: str) -> Path:
    return Path(value).expanduser().resolve()


def cell_argument(value: str) -> str:
    """Validate a command-line value that will become one Markdown cell."""

    cell = value.strip()
    if not cell:
        raise argparse.ArgumentTypeError("must not be empty")
    if "\n" in cell or "\r" in cell:
        raise argparse.ArgumentTypeError("must not contain a newline")
    if len(parse_markdown_row(f"| {cell} |") or ()) != 1:
        raise argparse.ArgumentTypeError(
            "must not contain an unescaped pipe character"
        )
    return cell


def positive_integer(value: str) -> int:
    try:
        number = int(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError("must be an integer") from error
    if number < 1:
        raise argparse.ArgumentTypeError("must be at least 1")
    return number


def parse_arguments(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Copy rows from one Markdown table into tables on the pages linked "
            "by each source row."
        )
    )
    parser.add_argument(
        "--link",
        required=True,
        type=cell_argument,
        help="Markdown cell to place first in every distributed row",
    )
    parser.add_argument(
        "--source",
        required=True,
        type=path_argument,
        help="Markdown file containing the source table",
    )
    parser.add_argument(
        "--content-root",
        required=True,
        type=path_argument,
        help="root directory containing destination Markdown pages",
    )
    parser.add_argument(
        "--url-prefix",
        type=normalize_url_prefix,
        help=(
            "site-relative URL prefix for the content root; defaults to the "
            "content root directory name without a numeric ordering prefix"
        ),
    )
    parser.add_argument(
        "--source-table-index",
        type=positive_integer,
        default=1,
        help="1-based index of the Markdown table to distribute (default: 1)",
    )
    parser.add_argument(
        "--target-section",
        default="Automated Detection",
        help="destination section heading (default: Automated Detection)",
    )
    parser.add_argument(
        "--target-table-header",
        default="Tool",
        help="first header cell of the destination table (default: Tool)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="validate and report changes without writing files",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="list every file that would be or was changed",
    )
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    arguments = parse_arguments(argv)
    url_prefix = arguments.url_prefix
    if url_prefix is None:
        url_prefix = "/" + unnumbered_name(arguments.content_root.name)

    try:
        rows, destination_count, changes = plan_changes(
            source=arguments.source,
            content_root=arguments.content_root,
            url_prefix=url_prefix,
            distributed_cell=arguments.link,
            source_table_index=arguments.source_table_index,
            target_section=arguments.target_section,
            target_table_header=arguments.target_table_header,
        )
    except (DistributionError, OSError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    inserted = sum(change.action == "inserted" for change in changes)
    updated = sum(change.action == "updated" for change in changes)
    unchanged = destination_count - len(changes)

    if arguments.verbose:
        for change in changes:
            try:
                display_path = change.path.relative_to(REPOSITORY_ROOT)
            except ValueError:
                display_path = change.path
            print(f"{change.action}: {display_path}")

    if arguments.dry_run:
        print(
            f"Dry run: {len(changes)} file(s) would change "
            f"({inserted} inserted, {updated} updated); {unchanged} already current."
        )
        return 0

    try:
        for change in changes:
            write_atomic(change)
    except OSError as error:
        print(f"error while writing {change.path}: {error}", file=sys.stderr)
        return 1

    print(
        f"Processed {len(rows)} source row(s) across {destination_count} "
        f"destination file(s): {inserted} inserted, {updated} updated, "
        f"{unchanged} already current."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
