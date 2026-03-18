#!/bin/bash

# Find all 1.index.md files that should be renamed to 01.index.md
find content/ -name "1.index.md" -type f | while read filepath; do
    dir=$(dirname "$filepath")
    # Check if any file in this directory starts with 0
    if ls "$dir" 2>/dev/null | grep -qE '^0[0-9]+'; then
        echo "Renaming: $filepath -> $(dirname "$filepath")/01.index.md"
        mv "$filepath" "$dir/01.index.md"
    fi
done
