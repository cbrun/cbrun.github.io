#!/usr/bin/env python3
"""
Normalize YAML front-matter `tags` to block list style across markdown/html files.

Rules:
- Only touch files with a front matter starting at the first line with `---`.
- If `tags:` is already a block list (with `- item`), leave as is.
- If `tags:` is an inline list (e.g., `tags: [a, b, c]`) or a single scalar (e.g., `tags: a`),
  convert to:
    tags:
      - a
      - b
      - c
- Preserve tag values verbatim (case, spaces, accents), trimming outer quotes and whitespace.

Targets:
- `_posts/`, `_talks/`, `_drafts/`, `about/`, `interview/` (if present).
"""
import os
import re
from typing import List, Tuple


BASES = ["_posts", "_talks", "_drafts", "about", "interview"]


def split_front_matter(text: str) -> Tuple[List[str], List[str], List[str]]:
    lines = text.splitlines()
    if not lines or not lines[0].strip().startswith("---"):
        return [], [], lines
    # find closing '---' line
    end_index = None
    for i in range(1, min(len(lines), 500)):  # sane limit
        if lines[i].strip().startswith("---"):
            end_index = i
            break
    if end_index is None:
        return [], [], lines
    fm = lines[1:end_index]
    body = lines[end_index+1:]
    return lines[:1], fm, body


def parse_inline_list(s: str) -> List[str]:
    # expects content inside [ ... ]
    inner = s.strip()
    if inner.startswith("[") and inner.endswith("]"):
        inner = inner[1:-1]
    parts = [p.strip() for p in inner.split(",")]
    out = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        # strip surrounding quotes if any
        if (p.startswith("\"") and p.endswith("\"")) or (p.startswith("'") and p.endswith("'")):
            p = p[1:-1]
        p = p.strip()
        if p:
            out.append(p)
    return out


def normalize_tags_block(fm_lines: List[str]) -> Tuple[List[str], bool]:
    changed = False
    i = 0
    out: List[str] = []
    while i < len(fm_lines):
        line = fm_lines[i]
        m_inline = re.match(r"^(?P<indent>\s*)tags\s*:\s*\[(?P<inner>.*)\]\s*$", line)
        m_scalar = None
        if not m_inline:
            m_scalar = re.match(r"^(?P<indent>\s*)tags\s*:\s*(?P<value>(?!\[).+?)\s*$", line)
        if m_inline:
            indent = m_inline.group("indent")
            items = parse_inline_list("[" + m_inline.group("inner") + "]")
            out.append(f"{indent}tags:")
            for item in items:
                out.append(f"{indent}  - {item}")
            changed = True
            i += 1
            continue
        elif m_scalar:
            # If next lines start with indented '-' then it's already a block list, keep as-is
            # But here m_scalar captured a scalar on the same line; convert to single-item list.
            indent = m_scalar.group("indent")
            value = m_scalar.group("value").strip()
            # strip quotes
            if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
                value = value[1:-1].strip()
            out.append(f"{indent}tags:")
            if value:
                out.append(f"{indent}  - {value}")
            changed = True
            i += 1
            continue
        else:
            # Detect 'tags:' starting a block; leave untouched
            out.append(line)
            i += 1
    return out, changed


def process_file(path: str) -> bool:
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()
    except Exception:
        return False
    pre, fm, body = split_front_matter(text)
    if not fm:
        return False
    # quick check: if "tags:" not in FM, skip
    if not any(re.match(r"^\s*tags\s*:\s*", l) for l in fm):
        return False
    new_fm, changed = normalize_tags_block(fm)
    if not changed:
        return False
    new_text = "\n".join(pre + new_fm + ["---"] + body) + ("\n" if text.endswith("\n") else "")
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    return True


def main() -> None:
    changed_files = []
    for base in BASES:
        if not os.path.isdir(base):
            continue
        for dirpath, _, filenames in os.walk(base):
            for fn in filenames:
                if not (fn.endswith(".md") or fn.endswith(".html")):
                    continue
                p = os.path.join(dirpath, fn)
                if process_file(p):
                    changed_files.append(p)
    print(f"Normalized tags in {len(changed_files)} files")
    if changed_files:
        for p in changed_files[:50]:
            print(f" - {p}")
        if len(changed_files) > 50:
            print(f" ... and {len(changed_files)-50} more")


if __name__ == "__main__":
    main()
