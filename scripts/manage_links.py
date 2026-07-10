#!/usr/bin/env python3
"""
Extract links from markdown files in content/ and construct a map
between files and all links they contain (both HTML and markdown style).

EXAMPLE:  python3 ./scripts/extract_links.py find-urls /sei-cert-c-coding-standard/recommendations/integers-int/int01-c
  prints all files that reference CERT recommendation INT01-C
"""

import re
import json
import concurrent.futures
from pathlib import Path
from typing import Dict, List
from tqdm import tqdm
import requests


def extract_markdown_links(content: str) -> List[str]:
    """Extract markdown-style links: [text](url).
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


def process_markdown_files(paths: List[str]) -> Dict[str, List[str]]:

    """Process all markdown files in content directory and extract links.

    Args:
        content_dir: Path to the content directory

    Returns:
        Dictionary mapping markdown file paths to lists of links found in them
    """

    # Find all md files associated with the paths
    md_files = []
    for path in map(Path, paths):
        if not path.exists():
            raise ValueError(f"Path does not exist: {path}")

        if path.is_dir():
            # Find all markdown files
            md_files.extend(path.glob('**/*.md'))
        elif path.is_file() and path.suffix == '.md':
            md_files.append(path)
        else:
            raise ValueError(f"Invalid path: {path}")

    # Extract all links for the md files.
    result = {}
    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        links = extract_links(content)

        file_key = str(md_file)
        result[file_key] = links

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
            results[file_path] = list(sorted(matching_urls))

    return results


def check_links_main(link_map: Dict[str, List[str]], output_format: str, checkpoint_file: str = 'checked_links.json'):
    """Check if absolute URLs are alive or dead using parallel requests and tqdm progress bar."""
    url_to_files = {}
    for file_path, links in link_map.items():
        for url in links:
            if url.startswith('http://') or url.startswith('https://'):
                if url not in url_to_files:
                    url_to_files[url] = []
                url_to_files[url].append(file_path)
    
    if not url_to_files:
        print("No absolute URLs found to check.")
        return

    # Load checkpoint
    checked_data = {}
    try:
        with open(checkpoint_file, 'r', encoding='utf-8') as f:
            checked_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        pass

    urls_to_check = [url for url in url_to_files if url not in checked_data]
    
    print(f"Total unique URLs found: {len(url_to_files)}")
    if urls_to_check:
        print(f"Already checked: {len(url_to_files) - len(urls_to_check)}")
        print(f"To check: {len(urls_to_check)}")
    else:
        print("All URLs have already been checked.")

    def worker(url):
        try:
            try:
                response = requests.head(url, timeout=10, allow_redirects=False)
                if response.status_code == 405:
                    response = requests.get(url, timeout=10, allow_redirects=False)
            except requests.RequestException:
                response = requests.get(url, timeout=10, allow_redirects=False)
            
            if 400 <= response.status_code < 600:
                return url, {"status": "dead", "code": response.status_code}
            elif 300 <= response.status_code < 400:
                return url, {"status": "redirect", "code": response.status_code, "dest": response.headers.get('Location')}
            else:
                return url, {"status": "alive", "code": response.status_code}
        except Exception as e:
            return url, {"status": "error", "error": str(e)}

    # Parallel execution
    if urls_to_check:
        i = 0
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = {executor.submit(worker, url): url for url in urls_to_check}
            for future in tqdm(concurrent.futures.as_completed(futures), total=len(urls_to_check), desc="Checking URLs"):
                url, result = future.result()
                checked_data[url] = result
                # Save checkpoint periodically (every 10 URLs or so to reduce I/O, or just every time for safety)
                # For simplicity and safety against interruption, we save every time.
                if i % 100 == 99:
                    with open(checkpoint_file, 'w', encoding='utf-8') as f:
                        json.dump(checked_data, f, indent=2)
                i += 1
                
        with open(checkpoint_file, 'w', encoding='utf-8') as f:
            json.dump(checked_data, f, indent=2)

    if output_format == 'json':
        print(json.dumps(checked_data, indent=4))
    else:
        dead_urls = []
        alive_urls = []
        redirect_urls = []
        error_urls = []

        for url, info in checked_data.items():
            if info["status"] == "dead":
                dead_urls.append((url, info["code"]))
            elif info["status"] == "alive":
                alive_urls.append(url)
            elif info["status"] == "redirect":
                redirect_urls.append((url, info["dest"]))
            elif info["status"] == "error":
                error_urls.append((url, info["error"]))

        print(f"\nSummary:")
        print(f"  Alive: {len(alive_urls)}")
        print(f"  Redirect: {len(redirect_urls)}")
        print(f"  Dead: {len(dead_urls)}")
        print(f"  Errors: {len(error_urls)}")

        if redirect_urls:
            print("\nRedirect URLs:")
            for url, dest in redirect_urls:
                print(f"- {url} (moved to {dest})")
                for file_path in url_to_files.get(url, []):
                    print(f"    - {file_path}")
        
        if dead_urls:
            print("\nDead URLs:")
            for url, code in dead_urls:
                print(f"- {url} (Status: {code})")
                for file_path in url_to_files.get(url, []):
                    print(f"    - {file_path}")
                    
        if error_urls:
            print("\nError URLs (could not connect):")
            for url, err in error_urls:
                print(f"- {url} (Error: {err})")
                for file_path in url_to_files.get(url, []):
                    print(f"    - {file_path}")

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


def print_links_by_file(output_format: str, links: dict[str, list[str]]):
    if output_format == 'json':
        print(json.dumps(links, indent=2))
    else:
        for i, (file_path, matching_urls) in enumerate(sorted(links.items(), key=lambda x: x[0])):
            if i > 0:
                print()
            print(f"- [ ] {file_path}:")
            for url in matching_urls:
                print(f"    - {url}")


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Extract links from markdown files and perform analysis'
    )
    subparsers = parser.add_subparsers(dest='command', help='Subcommands')

    # subcommand: find-urls
    parser_find_urls = subparsers.add_parser('find-urls', help='Find files that reference these URLs')
    parser_find_urls.add_argument('--urls', nargs='+', help='URLs to search for')
    parser_find_urls.add_argument('-o', '--output-format', default='json', choices=['json', 'text'], help="The output format of the result.")
    parser_find_urls.add_argument('paths', nargs='*')

    # subcommand: find-urls-from-file
    parser_find_urls_file = subparsers.add_parser('find-urls-from-file', help='Find files that reference URLs listed in a file')
    parser_find_urls_file.add_argument('--urls-file', help='Path to the file containing URLs')
    parser_find_urls_file.add_argument('-o', '--output-format', choices=['json', 'text'], help="The output format of the result.")
    parser_find_urls_file.add_argument('paths', nargs='*')

    # subcommand: rules-to-recommendations
    parser_rules = subparsers.add_parser('rules-to-recommendations', help='Find all files under rules/ that reference files under recommendations/')
    parser_rules.add_argument('-o', '--output-format', choices=['json', 'text'], help="The output format of the result.")
    parser_rules.add_argument('paths', nargs='*')
    
    # subcommand: check-links
    parser_check_links = subparsers.add_parser('check-links', help='Check if absolute URLs are alive or dead')
    parser_check_links.add_argument('-o', '--output-format', choices=['json', 'text'], help="The output format of the result.")
    parser_check_links.add_argument('paths', nargs='*')

    # subcommand: dump
    parser_dump = subparsers.add_parser('dump', help='Show a dump of links found')
    parser_dump.add_argument('-o', '--output-format', choices=['json', 'text'], help="The output format of the result.")
    parser_dump.add_argument('paths', nargs='*')

    args = parser.parse_args()

    # Load or generate link map
    link_map = process_markdown_files(args.paths if len(args.paths) > 0 else ['./content/'])

    # Perform requested analysis
    if args.command == 'find-urls':
        urls = [url.strip() for url in args.urls]
        print_links_by_file(args.output_format, find_files_with_urls(link_map, urls))
    elif args.command == 'find-urls-from-file':
        with open(args.file_path, 'r', encoding='utf-8') as f:
            urls = [line.strip() for line in f if line.strip()]
        print_links_by_file(args.output_format, find_files_with_urls(link_map, urls))
    elif args.command == 'check-links':
        check_links_main(link_map, args.output_format)
    elif args.command == 'rules-to-recommendations':
        print_links_by_file(args.output_format, find_rules_referencing_recommendations(link_map))
    elif args.command == 'dump':
        print_links_by_file(args.output_format, link_map)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
