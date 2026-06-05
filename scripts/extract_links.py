#!/usr/bin/env python3
"""
Extract links from markdown files in content/ and construct a map
between files and all links they contain (both HTML and markdown style).

EXAMPLE:  python3 ./scripts/extract_links.py  --find-urls /sei-cert-c-coding-standard/recommendations/integers-int/int01-c
  prints all files that reference CERT recommendation INT01-C
"""

import re
from pathlib import Path
from typing import Dict, List


def extract_markdown_links(content: str) -> List[str]:
    """Extract markdown-style links: [text](url) or [text][ref].

    Handles:
    - [text](url)
    - [text][reference]
    - [text]: url (reference definitions)
    """
    links = []

    # Inline links: [text](url) or [text](<url>)
    inline_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    for match in re.finditer(inline_pattern, content):
        url = match.group(2).strip()
        # Clean up angle brackets if present
        url = url.strip('<>')
        if url:
            links.append(url)

    # Reference links: [text][ref] or [text][] - we only track if there's a ref
    ref_pattern = r'\[([^\]]+)\]\[([^\]]*)\]'
    for match in re.finditer(ref_pattern, content):
        ref = match.group(2).strip()
        # If reference is empty, it's a shortcut reference link - skip
        if ref:
            # We can't get the URL without the reference definition
            # These are typically defined elsewhere and hard to resolve
            # We'll note them but can't extract the URL
            pass

    return links


def extract_html_links(content: str) -> List[str]:
    """Extract HTML-style links: <a href="url"> or <a href='url'>."""
    links = []

    # Anchor tags with href attribute
    # Match both single and double quotes, handle multi-line
    href_pattern = r'<a[^>]*\s+href\s*=\s*["\']([^"\']+)["\'][^>]*>'

    for match in re.finditer(href_pattern, content, re.IGNORECASE):
        url = match.group(1).strip()
        if url:
            links.append(url)

    return links


def extract_links(content: str) -> List[str]:
    """Extract all links from markdown content (both markdown and HTML style)."""
    all_links = []

    # Extract markdown links
    markdown_links = extract_markdown_links(content)
    all_links.extend(markdown_links)

    # Extract HTML links
    html_links = extract_html_links(content)
    all_links.extend(html_links)

    return all_links


def is_relative_url(url: str) -> bool:
    """Check if a URL is relative (starts with / or doesn't have a protocol)."""
    return not (url.startswith('http://') or
                url.startswith('https://') or
                url.startswith('mailto:') or
                url.startswith('tel:') or
                url.startswith('#'))


def extract_file_from_url(url: str, base_path: Path, file_path: Path) -> str:
    """Extract the target markdown file path from a URL.

    Args:
        url: The URL path
        base_path: The content directory base path
        file_path: The current file path

    Returns:
        The resolved file path relative to base_path, or empty string if not a markdown file
    """
    # Remove query parameters and fragments
    url_path = url.split('?')[0].split('#')[0]

    # Skip non-markdown and external links
    if url_path.startswith('http://') or url_path.startswith('https://'):
        return ''
    if url_path.startswith('mailto:') or url_path.startswith('tel:'):
        return ''

    # Handle absolute paths from site root
    if url_path.startswith('/'):
        target = base_path / url_path.lstrip('/')
        if target.suffix == '.md' and target.exists():
            try:
                return str(target.relative_to(base_path))
            except ValueError:
                return ''
        return ''

    # Handle relative paths
    if url_path:
        current_dir = file_path.parent
        target = current_dir / url_path
        # If it's a directory, look for index.md
        if target.is_dir():
            index_file = target / 'index.md'
            if index_file.exists():
                try:
                    return str(index_file.relative_to(base_path))
                except ValueError:
                    return ''
        elif target.suffix == '.md' and target.exists():
            try:
                return str(target.relative_to(base_path))
            except ValueError:
                return ''

    return ''


def process_markdown_files(content_dir: str) -> Dict[str, List[str]]:
    """Process all markdown files in content directory and extract links.

    Args:
        content_dir: Path to the content directory

    Returns:
        Dictionary mapping markdown file paths to lists of links found in them
    """
    content_path = Path(content_dir)
    if not content_path.exists():
        raise ValueError(f"Content directory does not exist: {content_dir}")

    # Find all markdown files
    md_files = list(content_path.glob('**/*.md'))

    result = {}

    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            links = extract_links(content)

            # Store absolute path for the file, relative paths for links
            file_key = str(md_file.relative_to(content_path))
            result[file_key] = links

        except Exception as e:
            print(f"Error processing {md_file}: {e}")

    return result


def find_files_with_urls(link_map: Dict[str, List[str]], urls: List[str]) -> Dict[str, List[str]]:
    """Find all files that reference any of the provided URLs.

    Args:
        link_map: Dictionary mapping file paths to lists of links
        urls: List of URLs to search for

    Returns:
        Dictionary mapping file paths to lists of matching URLs found in them
    """
    results = {}

    for file_path, links in link_map.items():
        matching_urls = [url for url in urls if url in links]
        if matching_urls:
            results[file_path] = matching_urls

    return results


def find_rules_referencing_recommendations(link_map: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Find all files under rules/ that reference files under recommendations/.

    Handles both direct path matching and numbered directory patterns like:
    - 3.rules/ referencing 4.recommendations/
    - rules/ referencing recommendations/
    - Any number prefix for rules or recommendations directories

    Args:
        link_map: Dictionary mapping file paths to lists of links

    Returns:
        Dictionary mapping rule files to lists of recommendation files they reference
    """
    import re

    results = {}

    # Pattern to match numbered rules directories (e.g., 3.rules/, 1.rules/, etc.)
    # Can appear anywhere in the path
    rules_pattern = re.compile(r'(?:^|/)(\d+\.)?rules(?:/|$)')
    # Pattern to match numbered recommendations directories (e.g., 4.recommendations/, 1.recommendations/, etc.)
    # Can appear anywhere in the path
    recommendations_pattern = re.compile(r'(?:^|/)(\d+\.)?recommendations(?:/|$)')

    for file_path, links in link_map.items():
        # Check if this file is under rules/ (numbered or not)
        if rules_pattern.search(file_path):
            # Check if any link points to recommendations/ (numbered or not)
            matching_links = []
            for link in links:
                # Normalize the link for comparison
                link_normalized = link.split('?')[0].split('#')[0]
                # Check for recommendations pattern
                if recommendations_pattern.search(link_normalized):
                    matching_links.append(link)

            if matching_links:
                results[file_path] = matching_links

    return results


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Extract links from markdown files and perform analysis'
    )
    parser.add_argument(
        '--find-urls', '-f',
        nargs='+',
        help='Find files that reference these URLs (comma-separated or space-separated)'
    )
    parser.add_argument(
        '--find-rules-to-recommendations', '-r',
        action='store_true',
        help='Find all files under rules/ that reference files under recommendations/'
    )

    args = parser.parse_args()

    # Load or generate link map
    link_map = process_markdown_files('./content')

    # Perform requested analysis
    if args.find_urls:
        # Parse comma-separated URLs
        urls = []
        for item in args.find_urls:
            urls.append(item.strip())

        results = find_files_with_urls(link_map, urls)

        print(f"\nFiles referencing {len(urls)} URL(s):")
        if results:
            for file_path, matching_urls in sorted(results.items()):
                print(f"  {file_path}:")
                for url in matching_urls:
                    print(f"    - {url}")
        else:
            print("  No files found matching the specified URLs.")

    if args.find_rules_to_recommendations:
        results = find_rules_referencing_recommendations(link_map)

        print(f"\nFiles under rules/ referencing recommendations/:")
        if results:
            print(f"  Found {len(results)} files with recommendations links")

            for file_path, rec_files in sorted(results.items()):
                print(f"  {file_path}:")
                for rec_file in rec_files[:3]:
                    print(f"    - {rec_file}")
        else:
            print("  No files found referencing recommendations.")

    # If no specific query, show summary
    if not args.find_urls and not args.find_rules_to_recommendations:
        print(f"\nProcessed {len(link_map)} markdown files in ./content/")
        total_links = sum(len(links) for links in link_map.values())
        print(f"Found {total_links} total links")

        print("\nOutput:")
        for (file_path, links) in sorted(link_map.items()):
            print(f"  {file_path}: {len(links)} links")
            for link in links:
                print(f"    - {link}")


if __name__ == '__main__':
    main()
