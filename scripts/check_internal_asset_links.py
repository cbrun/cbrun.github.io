#!/usr/bin/env python3
"""
Check internal links to assets (images, PDFs, etc.) and flag those not using
the Jekyll `{{ site.url }}` pattern.

Why: Relative links often break in feeds or mirrors; the site prefers absolute
links via `{{ site.url }}`.

What it does
- Scans .md/.markdown (and optionally .html) files under the repo (skips _site/).
- Extracts Markdown links/images and HTML <a>/<img> attributes.
- Detects internal asset links by extension (images, docs, archives, etc.).
- Flags links that are internal assets but do not use `{{ site.url }}`.
- Optional --fix: rewrites common cases to use `{{ site.url }}` safely.

Policy (default)
- Preferred form: `{{ site.url }}/path/to/asset.ext`.
- Flags these styles by default:
  * Hardcoded domain: `https://cedric.brun.io/...`
  * Root-absolute: `/images/...`, `/media/...`, `/talks/...`, etc.
  * Relative: `images/...`, `../images/...` (most fragile)

CLI options let you allow root-absolute and/or hardcoded domain styles.

Usage
  python scripts/check_internal_asset_links.py --root . [--include-html] [--fix]

Exit codes
- 0: No violations found
- 1: Violations found
- 2: Invalid usage or IO error
"""

from __future__ import annotations

import argparse
import os
import re
from pathlib import Path
from typing import Iterator, List, Dict, Tuple


DEFAULT_DOMAIN = "cedric.brun.io"
DEFAULT_SITE_URL_FALLBACK = f"https://{DEFAULT_DOMAIN}"

# Common asset extensions to check
ASSET_EXTS = {
    # images
    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp", ".tif", ".tiff",
    # documents
    ".pdf", ".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx", ".odt", ".odp",
    # archives/binaries
    ".zip", ".tar", ".gz", ".tgz", ".bz2", ".xz", ".7z",
    # media
    ".mp3", ".mp4", ".mov", ".avi", ".mkv", ".webm",
}

# Known site-local asset base dirs (used for safer fixes)
KNOWN_ASSET_DIRS = ("images/", "media/", "talks/", "assets/")


# Simple Markdown/HTML extractors (line-by-line to keep positions)
MD_LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
MD_IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
HTML_HREF_DQ_RE = re.compile(r"<a\s+[^>]*href=\"([^\"]+)\"", re.IGNORECASE)
HTML_HREF_SQ_RE = re.compile(r"<a\s+[^>]*href='([^']+)'", re.IGNORECASE)
HTML_IMG_DQ_RE = re.compile(r"<img\s+[^>]*src=\"([^\"]+)\"", re.IGNORECASE)
HTML_IMG_SQ_RE = re.compile(r"<img\s+[^>]*src='([^']+)'", re.IGNORECASE)
MD_REFDEF_RE = re.compile(r"^\s*\[([^\]]+)\]:\s*(\S+)\s*(?:\"[^\"]*\"|'[^']*')?\s*$")
MD_REFLINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\[([^\]]+)\]")

SITE_URL_VAR_RE = re.compile(r"\{\{\s*site\.url\s*\}\}")


def load_site_url_from_config(repo_root: Path) -> str | None:
    cfg = repo_root / "_config.yml"
    if not cfg.exists():
        return None
    try:
        for line in cfg.read_text(encoding="utf-8", errors="ignore").splitlines():
            m = re.match(r"^\s*url\s*:\s*(\S+)\s*$", line)
            if m:
                return m.group(1).strip('"\'')
    except Exception:
        return None
    return None


def iter_content_files(root: Path, include_html: bool) -> Iterator[Path]:
    exts = {".md", ".markdown"}
    if include_html:
        exts.add(".html")
    skip = {".git", "_site", "node_modules", "venv", ".venv"}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in skip and not d.startswith(".")]
        for fn in filenames:
            p = Path(dirpath) / fn
            if p.suffix.lower() in exts:
                yield p


def strip_code_fences(text: str) -> str:
    return re.sub(r"```[\s\S]*?```", "", text)


def parse_links_with_positions(path: Path) -> List[Dict]:
    content = path.read_text(encoding="utf-8", errors="ignore")
    # strip YAML front matter
    if content.startswith("---\n"):
        end = content.find("\n---\n", 4)
        if end != -1:
            content = content[end + 5 :]
    content = strip_code_fences(content)
    lines = content.splitlines()

    # Collect reference definitions for [text][ref]
    ref_defs: dict[str, str] = {}
    for ln in lines:
        m = MD_REFDEF_RE.match(ln)
        if m:
            ref_defs[m.group(1).strip().lower()] = m.group(2).strip()

    results: List[Dict] = []

    def add(url: str, line: int, source: str):
        results.append({"file": str(path), "line": line, "url": url, "source": source})

    for idx, ln in enumerate(lines, start=1):
        for m in MD_IMAGE_RE.finditer(ln):
            add(m.group(1).strip(), idx, "md_image")
        for m in MD_LINK_RE.finditer(ln):
            add(m.group(1).strip(), idx, "md_link")
        for m in HTML_IMG_DQ_RE.finditer(ln):
            add(m.group(1).strip(), idx, "html_img")
        for m in HTML_IMG_SQ_RE.finditer(ln):
            add(m.group(1).strip(), idx, "html_img")
        for m in HTML_HREF_DQ_RE.finditer(ln):
            add(m.group(1).strip(), idx, "html_a")
        for m in HTML_HREF_SQ_RE.finditer(ln):
            add(m.group(1).strip(), idx, "html_a")
        for m in MD_REFLINK_RE.finditer(ln):
            key = m.group(1).strip().lower()
            if key in ref_defs:
                add(ref_defs[key], idx, "md_ref")

    return results


def _normalize_for_ext_check(url: str, site_url: str) -> str:
    # Remove optional title in markdown like (url "title")
    u = url.strip()
    if u.startswith("<") and u.endswith(">"):
        u = u[1:-1].strip()
    u = re.sub(r"\s+(\"[^\"]*\"|'[^']*')\s*$", "", u)
    # Substitute {{ site.url }} before checking extension
    u = SITE_URL_VAR_RE.sub(site_url.rstrip("/"), u)
    # Drop query/fragment
    u = u.split("?", 1)[0].split("#", 1)[0]
    return u


def is_asset_url(url: str, site_url: str) -> bool:
    u = _normalize_for_ext_check(url, site_url).lower()
    return any(u.endswith(ext) for ext in ASSET_EXTS)


def classify_link_style(url_raw: str, site_url: str) -> Tuple[str, str]:
    """Return (style, normalized), where style is one of:
    - uses_site_url
    - hardcoded_domain
    - root_absolute
    - relative
    - external
    - unknown
    Normalized is the URL with whitespace/quotes trimmed.
    """
    url = url_raw.strip()
    # Remove surrounding angle brackets
    if url.startswith("<") and url.endswith(">"):
        url = url[1:-1].strip()
    # Remove optional markdown title
    url = re.sub(r"\s+(\"[^\"]*\"|'[^']*')\s*$", "", url)

    if SITE_URL_VAR_RE.search(url):
        return "uses_site_url", url

    # Protocol-relative
    if url.startswith("//"):
        if DEFAULT_DOMAIN in url.split("/", 3)[2].lower():
            return "hardcoded_domain", url
        return "external", url

    # Absolute
    if re.match(r"^https?://", url, re.IGNORECASE):
        if url.lower().startswith(site_url.lower()):
            return "hardcoded_domain", url
        return "external", url

    if url.startswith("/"):
        return "root_absolute", url

    # Otherwise, looks like a relative path
    return "relative", url


def build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Check internal asset links style (prefer {{ site.url }})")
    p.add_argument("--root", default=str(Path(__file__).resolve().parents[1]), help="Repository root to scan")
    p.add_argument("--include-html", action="store_true", help="Also scan .html files (legacy posts)")
    p.add_argument("--allow-root-absolute", action="store_true", help="Do not flag /path links as violations")
    p.add_argument("--allow-domain", action="store_true", help="Do not flag hardcoded https://cedric.brun.io links")
    p.add_argument("--no-style", action="store_true", help="Disable style checks; only report missing files")
    p.add_argument("--only-siteurl", action="store_true", help="Only check existence for links using {{ site.url }}")
    p.add_argument("--fix", action="store_true", help="Attempt safe in-place fixes to use {{ site.url }}")
    p.add_argument("--dry-run", action="store_true", help="Show what would change without writing files (with --fix)")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    repo_root = Path(args.root).resolve()
    if not repo_root.exists():
        print(f"Root path does not exist: {repo_root}")
        return 2

    site_url = load_site_url_from_config(repo_root) or DEFAULT_SITE_URL_FALLBACK
    site_url = site_url.rstrip("/")

    violations: List[Dict] = []

    for fp in iter_content_files(repo_root, include_html=args.include_html):
        try:
            links = parse_links_with_positions(fp)
        except Exception as e:
            print(f"Skipping {fp}: {e}")
            continue
        for rec in links:
            url = rec["url"]
            if not is_asset_url(url, site_url):
                continue
            style, norm = classify_link_style(url, site_url)

            if style == "external":
                continue  # ignore external assets

            if style == "uses_site_url":
                continue  # good

            if style == "root_absolute" and args.allow_root_absolute:
                continue

            if style == "hardcoded_domain" and args.allow_domain:
                continue

            if not args.no_style:
                rec2 = dict(rec)
                rec2.update({"style": style, "normalized": norm})
                violations.append(rec2)

    # Compute existence for internal assets
    missing: List[Dict] = []
    for rec in links if False else []:  # placeholder to keep type hints happy in editors
        pass

    def resolve_candidates(url_raw: str, style: str, file_path: Path) -> List[Path]:
        # Normalize like we did for ext check
        urln = _normalize_for_ext_check(url_raw, site_url)
        # Convert to a path relative to repo_root when possible
        cands: List[Path] = []
        if style in ("uses_site_url", "hardcoded_domain"):
            # Strip the site_url prefix
            if urln.lower().startswith(site_url.lower()):
                rel = urln[len(site_url):]
                rel = rel.lstrip("/")
                if rel:
                    cands.append((repo_root / rel))
        elif style == "root_absolute":
            rel = urln.lstrip("/")
            cands.append(replace_unsafe(repo_root / rel))
        elif style == "relative":
            # First relative to the file
            cands.append(replace_unsafe(file_path.parent / urln))
            # Also try relative to repo root for common patterns
            cands.append(replace_unsafe(repo_root / urln.lstrip("/")))
        return [p for p in cands if str(p.resolve()).startswith(str(repo_root))]

    def replace_unsafe(p: Path) -> Path:
        # Identity helper kept for clarity and later constraints if needed
        return p

    # Re-scan to perform existence checks (we want all links again)
    all_missing = []
    for fp in iter_content_files(repo_root, include_html=args.include_html):
        try:
            links2 = parse_links_with_positions(fp)
        except Exception:
            continue
        for rec in links2:
            url = rec["url"]
            if not is_asset_url(url, site_url):
                continue
            style, _norm = classify_link_style(url, site_url)
            if style == "external" or style == "unknown":
                continue
            if args.only_siteurl and style != "uses_site_url":
                continue
            # internal asset -> check existence
            for cand in resolve_candidates(url, style, Path(rec["file"])):
                try:
                    if cand.exists():
                        break
                except Exception:
                    pass
            else:
                all_missing.append(rec)

    if not violations and not all_missing:
        if args.no_style:
            print("No missing internal asset files found.")
        else:
            print("No style violations or missing internal asset files found.")
        return 0

    if violations:
        print(f"Found {len(violations)} internal asset link(s) not using {{ site.url }}:")
        for v in violations:
            loc = f"{v['file']}:{v['line']}"
            print(f"- {loc}  [{v['source']}]  {v['url']}  -> style={v['style']}")

    if all_missing:
        print(f"\nFound {len(all_missing)} internal asset link(s) pointing to missing files:")
        for m in all_missing:
            loc = f"{m['file']}:{m['line']}"
            print(f"- {loc}  [{m['source']}]  {m['url']}")

    if args.fix:
        print("\nApplying fixes (best-effort)...")
        changed_files = 0
        for file_path in sorted({v["file"] for v in violations}):
            path = Path(file_path)
            original = path.read_text(encoding="utf-8", errors="ignore")
            content = original

            # 1) Hardcoded domain -> site.url
            dom_esc = re.escape(site_url)
            content = re.sub(rf"(?<!\w){dom_esc}", "{{ site.url }}", content)
            # Also protocol-relative //cedric.brun.io (ensure not preceded by scheme colon)
            content = re.sub(r"(?i)(?<!:)//" + re.escape(DEFAULT_DOMAIN), "{{ site.url }}", content)

            # 2) Root-absolute for known asset dirs -> site.url
            for base in ("images/", "media/", "talks/", "assets/"):
                content = re.sub(rf"\(\s*/{re.escape(base)}", f"({{ site.url }}/{base}", content)
                content = re.sub(rf"(src|href)=\"/{re.escape(base)}", rf"\1=\"{{ site.url }}/{base}", content)
                content = re.sub(rf"(src|href)='/{re.escape(base)}", rf"\1='{{ site.url }}/{base}", content)

            # 3) Relative paths starting with known asset dirs -> prefix site.url
            for base in KNOWN_ASSET_DIRS:
                content = re.sub(rf"\(\s*{re.escape(base)}", f"({{ site.url }}/{base}", content)
                content = re.sub(rf"(src|href)=\"{re.escape(base)}", rf"\1=\"{{ site.url }}/{base}", content)
                content = re.sub(rf"(src|href)='{re.escape(base)}", rf"\1='{{ site.url }}/{base}", content)

            if content != original:
                changed_files += 1
                if args.dry_run:
                    print(f"Would update: {path}")
                else:
                    path.write_text(content, encoding="utf-8")
                    print(f"Updated: {path}")
        print(f"Fix complete. Files changed: {changed_files}")

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
