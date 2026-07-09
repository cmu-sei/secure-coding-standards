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

### rules-to-recommendations

This subcommand traverses the standards and identifies links from rules to recommendations.

### summary

This subcommand traverses the standards and emits the list of links found on each page. 

