#!/usr/bin/env python3
"""
List Jekyll posts with succinct Markdown summaries for LLM ingestion.

Outputs one line per post with: path, title, excerpt, and tags rendered as
"#tag #tag2 #tag3". If no excerpt is defined in the front matter, the script
uses the first paragraph of the content (sanitized) and truncates it.

Usage:
  python scripts/list_posts_markdown.py [--root REPO_ROOT] [--posts-dir _posts]
                                       [--include-noindex]

Notes:
  - Parses YAML front matter if PyYAML is available; otherwise uses a
    lightweight fallback parser that handles common patterns (lists, inline
    lists, and multi-line block scalars for excerpt).
  - Scans recursively for .md, .markdown, and .html files inside `_posts`.
  - Skips posts with `noindex: true` by default (use --include-noindex to include).
"""

import argparse
import os
import re
import sys
from typing import Dict, List, Tuple, Optional


def read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.read()


def split_front_matter(text: str) -> Tuple[Optional[str], str]:
    """Return (front_matter_text_or_None, content_text).

    Detects a YAML front matter block delimited by lines containing only '---'
    at the very beginning of the file. If not present, returns (None, text).
    """
    if not text.startswith("---\n") and not text.startswith("---\r\n"):
        return None, text
    # Find the next '---' that ends the front matter
    # Allow for Windows line endings.
    m = re.search(r"^---\s*$", text[4:], flags=re.MULTILINE)
    if not m:
        # Malformed; treat as no front matter
        return None, text
    end_idx = 4 + m.start()
    fm = text[4:end_idx]
    # Content starts after the newline following the closing '---' line
    # Find the end of that line to slice content
    # Position at the start of the closing line
    closing_line_end = text.find("\n", end_idx)
    if closing_line_end == -1:
        content = ""
    else:
        content = text[closing_line_end + 1 :]
    return fm, content


def parse_front_matter(fm_text: str) -> Dict:
    """Parse front matter using PyYAML if available, otherwise a fallback.

    The fallback handles simple key: value pairs, lists (both inline and block),
    and multi-line block scalars for 'excerpt'.
    """
    try:
        import yaml  # type: ignore

        data = yaml.safe_load(fm_text)
        return data or {}
    except Exception:
        return _parse_front_matter_fallback(fm_text)


def _strip_quotes(s: str) -> str:
    s = s.strip()
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        return s[1:-1]
    return s


def _parse_inline_list(val: str) -> List[str]:
    # Expect forms like: [a, b, "c d"]
    inside = val.strip()
    if inside.startswith("[") and inside.endswith("]"):
        inside = inside[1:-1]
        parts = [p.strip() for p in inside.split(",") if p.strip()]
        return [_strip_quotes(p) for p in parts]
    # Fallback: split on spaces
    return [v for v in re.split(r"[,\s]+", val.strip()) if v]


def _parse_front_matter_fallback(fm_text: str) -> Dict:
    data: Dict[str, object] = {}
    current_key: Optional[str] = None
    expecting_block_list = False
    expecting_block_scalar_for: Optional[str] = None
    block_scalar_lines: List[str] = []

    lines = fm_text.splitlines()
    for raw in lines:
        line = raw.rstrip("\r\n")

        # Handle continuation of block scalar (e.g., excerpt: | or >-)
        if expecting_block_scalar_for is not None:
            if line.startswith(" ") or line.startswith("\t"):
                block_scalar_lines.append(line.lstrip())
                continue
            else:
                # Commit previous scalar on dedent
                key = expecting_block_scalar_for
                data[key] = "\n".join(block_scalar_lines).strip()
                expecting_block_scalar_for = None
                block_scalar_lines = []
                # Fall-through to parse the current (non-indented) line

        # Skip empty lines and comments
        if not line or line.strip().startswith("#"):
            continue

        # Block list continuation
        if expecting_block_list and line.lstrip().startswith("- "):
            item = line.lstrip()[2:].strip()
            arr = data.get(current_key or "", [])
            if not isinstance(arr, list):
                arr = []
            if item:
                (arr).append(_strip_quotes(item))
            if current_key:
                data[current_key] = arr
            continue
        else:
            expecting_block_list = False

        # key: value
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            current_key = key

            # Block scalar starts (| or >, with optional modifiers like >-)
            if value in ("|", ">", ">-", "|-", "|+"):
                expecting_block_scalar_for = key
                block_scalar_lines = []
                continue

            if not value:
                # Maybe the next lines are a block list
                expecting_block_list = True
                data[key] = []
                continue

            # Inline list
            if value.startswith("[") and value.endswith("]"):
                data[key] = _parse_inline_list(value)
                continue

            # Scalar
            data[key] = _strip_quotes(value)
            continue

    # Commit any open block scalar at EOF
    if expecting_block_scalar_for is not None:
        data[expecting_block_scalar_for] = "\n".join(block_scalar_lines).strip()

    return data


def sanitize_and_make_excerpt(content: str, max_chars: int = 300) -> str:
    """Create a short excerpt from content.

    - Remove YAML code fences, HTML tags, and Markdown image/link URLs while keeping text.
    - Use the first paragraph (up to blank line) and truncate to max_chars.
    """
    # Remove front-matter artifacts if any remain
    # Strip code fences
    content = re.sub(r"^```.*?$[\s\S]*?^```\s*$", "\n", content, flags=re.MULTILINE)
    # Remove HTML tags
    content = re.sub(r"<[^>]+>", " ", content)
    # Remove Liquid tags
    content = re.sub(r"\{\%.*?\%\}|\{\{.*?\}\}", " ", content)
    # Replace images ![alt](url) with alt
    content = re.sub(r"!\[([^\]]*)\]\([^\)]*\)", r"\1", content)
    # Replace links [text](url) with text
    content = re.sub(r"\[([^\]]+)\]\([^\)]*\)", r"\1", content)
    # Strip markdown headings/quotes markers from starts of lines
    content = re.sub(r"^\s{0,3}[#>\-\*]+\s+", "", content, flags=re.MULTILINE)
    # Collapse whitespace
    content = re.sub(r"\s+", " ", content).strip()

    # Take first paragraph-like chunk
    # Already collapsed whitespace; just cut to max_chars
    if len(content) > max_chars:
        cut = content[: max_chars + 1]
        # Cut back to last space to avoid splitting words
        if " " in cut:
            cut = cut.rsplit(" ", 1)[0]
        content = cut + "…"
    return content


def ensure_list(value) -> List[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(v).strip() for v in value if str(v).strip()]
    if isinstance(value, str):
        # split on commas or whitespace
        parts = [p.strip() for p in re.split(r"[,\s]+", value) if p.strip()]
        return parts
    return [str(value).strip()]


def format_tags(tags: List[str]) -> str:
    # Deduplicate while keeping order
    seen = set()
    ordered = []
    for t in tags:
        if not t:
            continue
        if t not in seen:
            seen.add(t)
            ordered.append(t)
    return " ".join(f"#{t}" for t in ordered)


def find_posts(posts_dir: str) -> List[str]:
    exts = {".md", ".markdown", ".html"}
    result: List[str] = []
    for root, _dirs, files in os.walk(posts_dir):
        for fn in files:
            if fn.startswith("."):
                continue
            ext = os.path.splitext(fn)[1].lower()
            if ext in exts:
                result.append(os.path.join(root, fn))
    result.sort()
    return result


def process_post(path: str, include_noindex: bool = False) -> Optional[Tuple[str, str, str, str]]:
    """Return tuple (rel_path, title, excerpt, tags_md) or None if skipped."""
    text = read_text(path)
    fm_text, content = split_front_matter(text)
    data: Dict = {}
    if fm_text is not None:
        data = parse_front_matter(fm_text)

    # Skip if noindex: true and not explicitly included
    if (not include_noindex) and str(data.get("noindex")).lower() in ("true", "1", "yes"): 
        return None

    title = str(data.get("title") or "").strip()
    # Build excerpt
    excerpt = str(data.get("excerpt") or "").strip()
    if not excerpt:
        excerpt = sanitize_and_make_excerpt(content)

    tags_list = ensure_list(data.get("tags"))
    tags_md = format_tags(tags_list)

    rel_path = path
    return rel_path, title, excerpt, tags_md


def main() -> int:
    parser = argparse.ArgumentParser(description="List posts in succinct Markdown format")
    parser.add_argument("--root", default=".", help="Repository root (default: .)")
    parser.add_argument("--posts-dir", default="_posts", help="Relative posts directory (default: _posts)")
    parser.add_argument("--max-chars", type=int, default=300, help="Max excerpt length when generated (default: 300)")
    parser.add_argument("--include-noindex", action="store_true", help="Include posts with noindex: true (default: skip)")
    args = parser.parse_args()

    root = os.path.abspath(args.root)
    posts_dir = os.path.join(root, args.posts_dir)
    if not os.path.isdir(posts_dir):
        print(f"Error: posts directory not found: {posts_dir}", file=sys.stderr)
        return 2

    posts = find_posts(posts_dir)
    for p in posts:
        try:
            rel = os.path.relpath(p, root)
            processed = process_post(p, include_noindex=args.include_noindex)
            if processed is None:
                continue
            rel_path, title, excerpt, tags_md = processed
            # Ensure excerpt respects --max-chars when generated
            if not excerpt or excerpt.endswith("…"):
                # already truncated in generator; just ensure hard cap
                pass
            if excerpt and len(excerpt) > args.max_chars:
                excerpt = excerpt[: args.max_chars + 1]
                if " " in excerpt:
                    excerpt = excerpt.rsplit(" ", 1)[0] + "…"

            # One succinct markdown line per post
            # Format: - path — title — excerpt — #tag #tag2
            line_parts = [rel, title, excerpt, tags_md]
            pretty = "\n  ".join([s for s in line_parts if s])
            print(f"- {pretty}")
        except Exception as e:
            print(f"# Error processing {p}: {e}", file=sys.stderr)
            continue

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
