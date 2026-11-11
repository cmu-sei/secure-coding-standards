#!/usr/bin/env python3
"""
Check "undefined behavior N" links in the CERT C standard against the
CC. Undefined Behavior table.

Guideline pages cite entries of the table with links such as

    [undefined behavior 188](/sei-cert-c-coding-standard/back-matter/cc-undefined-behavior#CC.UndefinedBehavior-ub_188)

and each table row lists the guidelines that cite it in its Guideline
column. This script reports where the two disagree:

  text      the link text names a different number from the anchor it links to
  anchor    the anchor is malformed or names a row the table does not have
  backlink  a page cites row N, but row N's Guideline column does not list the page
  unused    row N's Guideline column lists a page that does not cite row N

The script only reports; it changes nothing. Whether a given finding means
the page cites the wrong row or the row's Guideline column is incomplete
has to be decided case by case.

EXAMPLES:
    python3 scripts/check_ub_links.py
    python3 scripts/check_ub_links.py --kind text --kind anchor
    python3 scripts/check_ub_links.py --tsv > ub-findings.tsv

Exit status: 0 if there are no findings of the selected kinds, 1 otherwise.
"""

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

DEFAULT_ROOT = 'content/4.sei-cert-c-coding-standard'
TITLE_ID = re.compile(r'^# ([A-Z]{3}\d\d-C)\.', re.MULTILINE)
UB_LINK = re.compile(r'\[([^\]]*)\]\([^)\s]*cc-undefined-behavior#([^)\s]*)[^)]*\)')
ANCHOR = re.compile(r'CC\.UndefinedBehavior-ub_(\d+)')
TABLE_ROW = re.compile(r'^\|\s*(\d+)\s*<a id="CC\.UndefinedBehavior-ub_(\d+)"></a>\s*\|(.*)\|\s*$', re.MULTILINE)
GUIDELINE = re.compile(r'\[[^\]]*?([A-Z]{3}\d\d-C)\]')
KINDS = ('text', 'anchor', 'backlink', 'unused')


def read_table(path: Path):
    """Map row number -> set of guideline ids in its last (Guideline) column."""
    rows = {}
    for m in TABLE_ROW.finditer(path.read_text(encoding='utf-8')):
        number = int(m.group(2))
        cells = m.group(3).split('|')
        rows[number] = set(GUIDELINE.findall(cells[-1]))
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__.strip().split('\n\n')[0])
    parser.add_argument('--content-root', default=DEFAULT_ROOT,
                        help=f'CERT C content directory (default: {DEFAULT_ROOT})')
    parser.add_argument('--kind', action='append', choices=KINDS,
                        help='report only these kinds (repeatable; default: all)')
    parser.add_argument('--tsv', action='store_true', help='tab-separated output')
    args = parser.parse_args()
    kinds = set(args.kind or KINDS)

    root = Path(args.content_root)
    if not root.is_dir():
        parser.error(f'{root}: no such directory (run from the repository root or pass --content-root)')
    tables = list(root.rglob('*cc-undefined-behavior.md'))
    if len(tables) != 1:
        sys.exit(f'expected one cc-undefined-behavior.md under {root}, found {len(tables)}')
    table = tables[0]
    rows = read_table(table)

    findings = []          # (kind, guideline, row, detail, file:line)
    cited = defaultdict(set)
    for path in sorted(root.rglob('*.md')):
        if path == table:
            continue
        text = path.read_text(encoding='utf-8')
        title = TITLE_ID.search(text)
        if not title:
            continue
        gid = title.group(1)
        for m in UB_LINK.finditer(text):
            where = f'{path}:{text.count(chr(10), 0, m.start()) + 1}'
            anchor = ANCHOR.fullmatch(m.group(2))
            if not anchor:
                findings.append(('anchor', gid, '-', f'malformed anchor #{m.group(2)}', where))
                continue
            number = int(anchor.group(1))
            cited_before = set(cited[gid])
            cited[gid].add(number)
            numbers_in_text = re.findall(r'\d+', m.group(1))
            if numbers_in_text and str(number) not in numbers_in_text:
                findings.append(('text', gid, number, f'link text "{m.group(1)}"', where))
            if number not in rows:
                findings.append(('anchor', gid, number, 'no such row', where))
            elif gid not in rows[number] and number not in cited_before:
                listed = ', '.join(sorted(rows[number])) or '(empty)'
                findings.append(('backlink', gid, number, f'row lists: {listed}', where))

    for number in sorted(rows):
        for gid in sorted(rows[number]):
            if number not in cited.get(gid, ()):
                pages = ', '.join(map(str, sorted(cited.get(gid, ())))) or '(none)'
                findings.append(('unused', gid, number, f'{gid} cites: {pages}', str(table)))

    findings = [f for f in findings if f[0] in kinds]
    for kind, gid, number, detail, where in findings:
        if args.tsv:
            print(kind, gid, number, detail, where, sep='\t')
        else:
            print(f'{kind:8} {gid:8} UB {str(number):<4} {detail}  ({where})')
    counts = {k: sum(1 for f in findings if f[0] == k) for k in KINDS if k in kinds}
    print(', '.join(f'{v} {k}' for k, v in counts.items()), file=sys.stderr)
    return 1 if findings else 0


if __name__ == '__main__':
    sys.exit(main())
