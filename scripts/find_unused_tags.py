#!/usr/bin/env python3
"""
Detect unused tag pages.

Scans `_posts/` and `_talks/` for tags in front matter, compares their
slugified forms with tag page slugs in `_tag/` (the filename without extension),
and reports any tag pages that are no longer used. Optionally deletes them.

Usage:
  python3 scripts/find_unused_tags.py
  python3 scripts/find_unused_tags.py --delete

Notes:
- Tag usage is detected from front matter `tags:` fields (block or inline list).
- Slugification approximates Jekyll's: ASCII fold, lowercase, non-alnum to '-'.
- Only `_posts/` and `_talks/` are scanned, as requested (not `_drafts/`).
"""

import argparse
import os
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POSTS_DIR = ROOT / "_posts"
TALKS_DIR = ROOT / "_talks"
TAG_DIR = ROOT / "_tag"


def slugify(value: str) -> str:
    # Normalize accents, lowercase
    value = unicodedata.normalize("NFKD", value)
    value = value.encode("ascii", "ignore").decode("ascii")
    value = value.lower()
    # Replace non-alnum with hyphens
    value = re.sub(r"[^a-z0-9]+", "-", value)
    # Collapse and trim hyphens
    value = re.sub(r"-+", "-", value).strip("-")
    return value


def extract_front_matter(text: str) -> str | None:
    # Front matter delimited by --- on first line and next occurrence
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    return text[4:end + 1]  # include trailing newline of front matter block


def parse_tags_from_fm(fm: str) -> list[str]:
    tags: list[str] = []
    # Inline list: tags: [a, b, c]
    m_inline = re.search(r"^tags:\s*\[(.*?)\]\s*$", fm, re.M)
    if m_inline:
        inner = m_inline.group(1).strip()
        for part in re.split(r",", inner):
            t = part.strip().strip("'\"")
            if t:
                tags.append(t)
        return tags
    # Block list:
    m_block = re.search(r"^tags:\s*$", fm, re.M)
    if m_block:
        # Capture subsequent indented - item lines until a non-indented or blank delimiter in YAML
        start = m_block.end()
        lines = fm[start:].splitlines()
        for line in lines:
            if re.match(r"^\s*-\s+", line):
                t = re.sub(r"^\s*-\s+", "", line).strip().strip("'\"")
                if t:
                    tags.append(t)
            else:
                # Stop at first non list item or blank line at same indent
                if line.strip() == "":
                    continue
                break
    return tags


def collect_used_tag_slugs() -> set[str]:
    used: set[str] = set()
    for base in (POSTS_DIR, TALKS_DIR):
        if not base.exists():
            continue
        for p in base.rglob("*"):
            if not p.is_file():
                continue
            if p.suffix.lower() not in {".md", ".markdown", ".html"}:
                continue
            try:
                text = p.read_text(encoding="utf-8")
            except Exception:
                continue
            fm = extract_front_matter(text)
            if not fm:
                continue
            tags = parse_tags_from_fm(fm)
            for t in tags:
                if not t:
                    continue
                used.add(slugify(t))
    return used


def collect_tag_page_slugs() -> dict[str, Path]:
    mapping: dict[str, Path] = {}
    if not TAG_DIR.exists():
        return mapping
    for p in TAG_DIR.glob("*.md"):
        slug = p.stem  # filename without extension is the collection slug
        mapping[slug] = p
    return mapping


def main() -> int:
    parser = argparse.ArgumentParser(description="Detect unused tag pages in _tag/.")
    parser.add_argument("--delete", action="store_true", help="Delete unused tag files instead of only reporting.")
    args = parser.parse_args()

    used_slugs = collect_used_tag_slugs()
    tag_pages = collect_tag_page_slugs()

    unused = sorted([slug for slug in tag_pages.keys() if slug not in used_slugs])

    if not unused:
        print("No unused tag pages found.")
        return 0

    print(f"Found {len(unused)} unused tag page(s):\n")
    for slug in unused:
        path = tag_pages[slug]
        print(f"- {slug} -> {path}")
        try:
            content = path.read_text(encoding="utf-8").strip()
        except Exception as e:
            content = f"<error reading file: {e}>"
        print("  --- file content ---")
        # Indent content for readability
        for line in content.splitlines():
            print("  " + line)
        print("  --------------------\n")

    if args.delete:
        print("--delete specified: Removing unused tag files...\n")
        for slug in unused:
            path = tag_pages[slug]
            try:
                os.remove(path)
                print(f"Deleted {path}")
            except Exception as e:
                print(f"Failed to delete {path}: {e}")
        print("Done.")
    else:
        print("Run with --delete to remove these files.")

    return 0


if __name__ == "__main__":
    sys.exit(main())

