# Scripts

This directory contains helpful scripts which are used to maintain the secure coding standards. 

NOTE: All bash snippets in this file assume your current directory is the root of the secure coding standards repository.

## Setup

For the python-based scripts, you will need to have the packages listed in `requirements.txt`. 

A good way to do this is via a venv to keep the requirements for these scripts separate from your system or other projects.

```bash
# Use venv to setup a virtual environment. Do this only once
python -m venv venv

# Source the venv into your shell. You must do this each time.
source venv/bin/activate

# Install the required packages. You only need to do this after changes to requirements.txt.
pip install -r scripts/requirements.txt
```

## manage_links.py

The subcommands in this script can be used to manage links found in the standards. For up to date information, check the help:

```bash
python scripts/manage_links.py --help
```

### find-urls

This subcommand finds files which contain at least one of the urls provided via the command line.

### find-urls-from-file

This subcommand finds files which contain at least one of the urls found on the lines of a given file.

### check-links

This subcommand traverses the standards and then uses the python requests library to attempt a HEAD request on the url. It then categorizes the response as `alive`, `redirect`, `dead`, or `error`. 

Intermediate and final results are cached in `./checked_links.json`.

NOTE: Some external websites use bot protection that makes pages return 403 when accessed via requests. Thus, "dead" links with code 403 need to be checked manually in a browser. Also zscaler interferes with some external websites (notably gnu), so it is best to run the script off of zscaler.

### rules-to-recommendations

This subcommand traverses the standards and identifies links from rules to recommendations.

### summary

This subcommand traverses the standards and emits the list of links found on each page. 


## distribute_guideline_table.py

Distribute a related-guidelines table to guideline pages

For example, distributing the MISRA C 2025 alerts among the guidelines: (Note that this leave the Relationship column empty).

``` sh
python3 scripts/distribute_guideline_table.py \
        --link '[MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25)' \
        --source content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md \
        --content-root content/4.sei-cert-c-coding-standard \
        --target-section "Related Guidelines" \
        --target-table-header "Taxonomy"
```

## collect_guideline_table.py

Collect matching cells from Markdown pages into one table on standard output:

For example, to reproduce the complete MISRA C:2025 table from the CERT C guidelines:

``` sh
python3 scripts/collect_guideline_table.py \
    --content-root content/4.sei-cert-c-coding-standard \
    --section 'Related Guidelines' \
    --table-header 'Taxonomy item' \
    --cell-name 'MISRA C:2025' \
    --guideline-header 'CERT Rule' \
    --value-header 'Related Guidelines' \
    'content/4.sei-cert-c-coding-standard/*.rules/**/*.md' \
    'content/4.sei-cert-c-coding-standard/*.recommendations/**/*.md'
```


## Other Files
### codex-session-01a121df-c74d-7c02-ae25-f5d2865b8034.md

Session where Codex created `distribute_guideline_table.py` and `collect_guideline_table.py`
