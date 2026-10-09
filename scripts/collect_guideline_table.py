#!/usr/bin/env python3
"""Collect matching cells from Markdown pages into one table on stdout.

Each input page is searched for a table containing ``--table-header``. Rows
containing ``--cell-name`` are collected, and the cell under the requested
header is paired with a link back to the input page.

Input arguments may be files, directories, or quoted glob expressions. Glob
expressions support ``**`` recursion.
"""

from __future__ import annotations

import argparse
import glob
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional, Sequence, Tuple
from urllib.parse import quote


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
HEADING_RE = re.compile(r"^(?P<marks>#{1,6})\s+(?P<title>.*?)\s*$")
MARKDOWN_LINK_RE = re.compile(
    r"^\[(?P<label>(?:\\.|[^\]])+)\]"
    r"\(\s*<?(?P<url>[^\s>)]+)>?(?:\s+['\"][^'\"]*['\"])?\s*\)$"
)
SEPARATOR_CELL_RE = re.compile(r"^:?-{3,}:?$")


class CollectionError(Exception):
    """Raised when inputs cannot be collected without ambiguity."""


@dataclass(frozen=True)
class MarkdownTable:
    first_data_index: int
    end_index: int
    header_cells: Tuple[str, ...]


@dataclass(frozen=True)
class CollectedRow:
    guideline_label: str
    guideline_url: str
    value: str
    source_line: int


def parse_markdown_row(line: str) -> Optional[Tuple[str, ...]]:
    """Return trimmed cells from a pipe-delimited Markdown row."""

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
    if end is None:
        end = len(lines)

    tables: List[MarkdownTable] = []
    index = start
    while index + 1 < end:
        header = parse_markdown_row(lines[index])
        separator = parse_markdown_row(lines[index + 1])
        if (
            header is None
            or not is_separator_row(separator)
            or len(header) != len(separator)
        ):
            index += 1
            continue

        table_end = index + 2
        while table_end < end and parse_markdown_row(lines[table_end]) is not None:
            table_end += 1

        tables.append(
            MarkdownTable(
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
        raise CollectionError(f"File does not exist: {path}") from error
    except UnicodeDecodeError as error:
        raise CollectionError(f"File is not valid UTF-8: {path}") from error


def unnumbered_name(name: str) -> str:
    return re.sub(r"^\d+\.", "", name)


def normalize_url_prefix(value: str) -> str:
    value = value.strip()
    if not value.startswith("/"):
        raise argparse.ArgumentTypeError("must begin with '/'")
    return value.rstrip("/")


def route_for_page(content_root: Path, path: Path, url_prefix: str) -> str:
    try:
        relative = path.relative_to(content_root)
    except ValueError as error:
        raise CollectionError(
            f"Input file is outside --content-root: {path}"
        ) from error

    components = [unnumbered_name(part) for part in relative.parts[:-1]]
    page_name = unnumbered_name(path.stem)
    if page_name != "index":
        components.append(page_name)

    encoded_suffix = "/".join(quote(component) for component in components)
    if not encoded_suffix:
        return url_prefix or "/"
    return f"{url_prefix}/{encoded_suffix}" if url_prefix else f"/{encoded_suffix}"


def page_label(lines: Sequence[str], path: Path) -> str:
    """Use the leading identifier from the first H1, then fall back to the filename."""

    for line in lines:
        match = HEADING_RE.fullmatch(line.rstrip("\r\n"))
        if match is None or len(match.group("marks")) != 1:
            continue
        title = match.group("title").strip()
        if ". " in title:
            return title.split(". ", 1)[0].strip()
        if title:
            return title

    return unnumbered_name(path.stem)


def find_section_bounds(
    lines: Sequence[str], title: Optional[str]
) -> Optional[Tuple[int, int]]:
    if title is None:
        return 0, len(lines)

    matches: List[Tuple[int, int]] = []
    for index, line in enumerate(lines):
        match = HEADING_RE.fullmatch(line.rstrip("\r\n"))
        if match is not None and match.group("title").strip() == title:
            matches.append((index, len(match.group("marks"))))

    if not matches:
        return None
    if len(matches) > 1:
        raise CollectionError(
            f"Found more than one section named {title!r} in one input file"
        )

    section_start, heading_level = matches[0]
    section_end = len(lines)
    for index in range(section_start + 1, len(lines)):
        match = HEADING_RE.fullmatch(lines[index].rstrip("\r\n"))
        if match is not None and len(match.group("marks")) <= heading_level:
            section_end = index
            break
    return section_start + 1, section_end


def visible_cell_name(cell: str) -> str:
    match = MARKDOWN_LINK_RE.fullmatch(cell)
    return match.group("label") if match is not None else cell


def cell_matches(cell: str, requested_name: str) -> bool:
    return cell == requested_name or visible_cell_name(cell) == requested_name


def collect_from_file(
    path: Path,
    content_root: Path,
    url_prefix: str,
    section: Optional[str],
    table_header: str,
    cell_name: str,
) -> List[CollectedRow]:
    text = read_utf8(path)
    lines = text.splitlines(keepends=True)
    bounds = find_section_bounds(lines, section)
    if bounds is None:
        return []

    label = page_label(lines, path)
    url = route_for_page(content_root, path, url_prefix)
    collected: List[CollectedRow] = []

    for table in find_markdown_tables(lines, *bounds):
        matching_columns = [
            index
            for index, header in enumerate(table.header_cells)
            if header == table_header
        ]
        if not matching_columns:
            continue
        if len(matching_columns) > 1:
            raise CollectionError(
                f"Header {table_header!r} occurs more than once in a table in {path}"
            )

        value_column = matching_columns[0]
        for line_index in range(table.first_data_index, table.end_index):
            cells = parse_markdown_row(lines[line_index])
            if cells is None or not any(
                cell_matches(cell, cell_name) for cell in cells
            ):
                continue
            if value_column >= len(cells):
                raise CollectionError(
                    f"Matching row at {path}:{line_index + 1} has no cell under "
                    f"header {table_header!r}"
                )
            collected.append(
                CollectedRow(
                    guideline_label=label,
                    guideline_url=url,
                    value=cells[value_column],
                    source_line=line_index + 1,
                )
            )

    return collected


def expand_inputs(expressions: Iterable[str]) -> List[Path]:
    files = set()

    for expression in expressions:
        path = Path(expression).expanduser()
        if path.is_dir():
            files.update(candidate.resolve() for candidate in path.rglob("*.md"))
            continue
        if path.is_file():
            if path.suffix.lower() != ".md":
                raise CollectionError(f"Expected a Markdown file: {path}")
            files.add(path.resolve())
            continue

        matches = [Path(match) for match in glob.glob(expression, recursive=True)]
        markdown_matches = [
            match.resolve()
            for match in matches
            if match.is_file() and match.suffix.lower() == ".md"
        ]
        if not markdown_matches:
            raise CollectionError(f"Input expression matched no Markdown files: {expression}")
        files.update(markdown_matches)

    return sorted(files)


def escape_table_cell(value: str) -> str:
    """Preserve existing escapes while protecting unescaped table delimiters."""

    return re.sub(r"(?<!\\)\|", r"\\|", value)


def render_table(
    rows: Sequence[CollectedRow], guideline_header: str, value_header: str
) -> str:
    guideline_header = escape_table_cell(guideline_header)
    value_header = escape_table_cell(value_header)
    first_width = max(3, len(guideline_header) + 2)
    second_width = max(3, len(value_header) + 2)
    lines = [
        f"| {guideline_header} | {value_header} |",
        f"|{'-' * first_width}|{'-' * second_width}|",
    ]

    for row in rows:
        guideline = f"[{row.guideline_label}]({row.guideline_url})"
        lines.append(
            f"| {escape_table_cell(guideline)} | {escape_table_cell(row.value)} |"
        )
    return "\n".join(lines) + "\n"


def path_argument(value: str) -> Path:
    return Path(value).expanduser().resolve()


def parse_arguments(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Collect a named cell from Markdown tables across many linked pages "
            "and print one consolidated table."
        )
    )
    parser.add_argument(
        "inputs",
        nargs="+",
        help="Markdown files, directories, or quoted glob expressions",
    )
    parser.add_argument(
        "--content-root",
        required=True,
        type=path_argument,
        help="root directory used to derive links to input pages",
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
        "--section",
        help="only search tables within this Markdown section",
    )
    parser.add_argument(
        "--table-header",
        required=True,
        help="header of the column whose value should be collected",
    )
    parser.add_argument(
        "--cell-name",
        required=True,
        help="exact cell content or visible Markdown-link text identifying rows",
    )
    parser.add_argument(
        "--guideline-header",
        default="Guideline",
        help="first header in the generated table (default: Guideline)",
    )
    parser.add_argument(
        "--value-header",
        help="second generated header (default: value of --table-header)",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="report collection counts to standard error",
    )
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    arguments = parse_arguments(argv)
    url_prefix = arguments.url_prefix
    if url_prefix is None:
        url_prefix = "/" + unnumbered_name(arguments.content_root.name)

    try:
        input_files = expand_inputs(arguments.inputs)
        rows: List[CollectedRow] = []
        for path in input_files:
            rows.extend(
                collect_from_file(
                    path=path,
                    content_root=arguments.content_root,
                    url_prefix=url_prefix,
                    section=arguments.section,
                    table_header=arguments.table_header,
                    cell_name=arguments.cell_name,
                )
            )
    except (CollectionError, OSError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    if not rows:
        print("error: no matching rows found", file=sys.stderr)
        return 1

    rows.sort(
        key=lambda row: (
            row.guideline_label.casefold(),
            row.source_line,
            row.value.casefold(),
        )
    )
    value_header = arguments.value_header or arguments.table_header
    sys.stdout.write(render_table(rows, arguments.guideline_header, value_header))

    if arguments.verbose:
        print(
            f"Collected {len(rows)} row(s) from {len(input_files)} input file(s).",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
