#!/usr/bin/env python3
"""
Make each guideline's "Related Vulnerabilities" search link use the
guideline's own identifier.

Each guideline page has a paragraph like

    Search for vulnerabilities resulting from the violation of this rule on
    the [CERT website](https://www.kb.cert.org/vuls/search/?q=ENV34-C) .

The identifier in `?q=` should be the one in the page's title
(`# ENV34-C. ...`). On some pages it is another guideline's identifier,
usually a former one. This script finds those links and, with --write,
replaces the identifier with the page's own.

Pages whose title does not start with a guideline identifier are skipped
and listed.

EXAMPLES:
    # Report mismatches in the CERT C standard (no changes)
    python3 scripts/fix_related_vulnerabilities.py content/4.sei-cert-c-coding-standard

    # Fix them
    python3 scripts/fix_related_vulnerabilities.py --write content/4.sei-cert-c-coding-standard

    # Whole site
    python3 scripts/fix_related_vulnerabilities.py --write content

Exit status: 0 if every link already matches (or --write fixed them all),
1 if a mismatch remains (useful as a check).
"""

import argparse
import re
import sys
from pathlib import Path

# "# ENV34-C. Do not ..." / "# STR50-CPP. ..." / "# OBJ13-J. ..." / "# DRD10-X. ..."
TITLE_ID = re.compile(r'^# ([A-Z][A-Z0-9]*\d\d-[A-Za-z]+)\.', re.MULTILINE)
SEARCH_Q = re.compile(r'(https?://www\.kb\.cert\.org/vuls/search/?\?q=)([^)\s&"\']*)')


def process(path: Path, write: bool):
    """Return (page_id, [(old, new), ...]) or (None, [found ids]) if the page has no title id."""
    text = path.read_text(encoding='utf-8')
    found = SEARCH_Q.findall(text)
    if not found:
        return None, []
    title = TITLE_ID.search(text)
    if not title:
        return None, [q for _, q in found]
    page_id = title.group(1)
    changes = [(q, page_id) for _, q in found if q != page_id]
    if changes and write:
        new_text = SEARCH_Q.sub(lambda m: m.group(1) + page_id, text)
        path.write_text(new_text, encoding='utf-8')
    return page_id, changes


def main():
    parser = argparse.ArgumentParser(description=__doc__.strip().split('\n\n')[0])
    parser.add_argument('paths', nargs='*', default=['content'],
                        help='files or directories to process (default: content)')
    parser.add_argument('--write', action='store_true',
                        help='rewrite mismatched links (default: report only)')
    args = parser.parse_args()

    files = []
    for p in map(Path, args.paths):
        if not p.exists():
            parser.error(f'{p}: no such file or directory')
        files.extend(sorted(p.rglob('*.md')) if p.is_dir() else [p])

    mismatched = 0
    for f in files:
        page_id, result = process(f, args.write)
        if page_id is None:
            if result:
                print(f'SKIP (no guideline id in title)\t{f}\t{",".join(result)}')
            continue
        for old, new in result:
            mismatched += 1
            print(f'{"FIXED" if args.write else "MISMATCH"}\t{f}\t{old} -> {new}')

    print(f'{mismatched} link(s) {"fixed" if args.write else "mismatched"}', file=sys.stderr)
    return 0 if (args.write or mismatched == 0) else 1


if __name__ == '__main__':
    sys.exit(main())
