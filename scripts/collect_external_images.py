#!/usr/bin/env python3
"""
Scan Jekyll posts for external image references, optionally download them
into images/blog/YYYY/slug/ and rewrite the posts to use {{ site.url }} paths.

Default behavior is a dry run that prints a report. Use --apply to actually
download and rewrite. Creates a .bak backup before modifying any post.

Patterns handled:
- Markdown images: ![alt](http(s)://...)
- HTML images: <img src="http(s)://...">
- HTML anchors to images: <a href="http(s)://...{png,jpg,jpeg,gif,webp,svg}"> (often full-size links)

Notes:
- Only external http(s) URLs are considered. Links already pointing to the site
  or local paths are ignored.
- To avoid collisions for services like Blogspot which encode size in a path
  segment (e.g., /s1600/), the size segment is prefixed to the filename.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import sys
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Sequence, Tuple
from urllib.parse import urlparse
from urllib.request import Request, urlopen


MARKDOWN_IMG_RE = re.compile(r"!\[[^\]]*\]\((https?://[^)\s]+)")
HTML_IMG_RE = re.compile(r"<img[^>]+src=[\"\'](https?://[^\"\'>\s]+)")
HTML_A_IMG_RE = re.compile(
    r"<a[^>]+href=[\"\'](https?://[^\"\'>\s]+\.(?:png|jpe?g|gif|webp|svg)(?:\?[^\"\'>\s]*)?)"
)

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}
SITE_URL_PREFIX = "https://cedric.brun.io/"  # used to detect already-internal links


@dataclass
class Occurrence:
    file: str
    url: str
    kind: str  # markdown|img|a_img


def is_external_image_url(url: str) -> bool:
    if not url.startswith("http://") and not url.startswith("https://"):
        return False
    if url.startswith(SITE_URL_PREFIX):
        return False
    return True


def scan_posts(posts_dir: str) -> List[Occurrence]:
    occ: List[Occurrence] = []
    for root, _, files in os.walk(posts_dir):
        for f in files:
            if not f.lower().endswith((".md", ".markdown", ".html")):
                continue
            path = os.path.join(root, f)
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as fh:
                    text = fh.read()
            except Exception:
                continue
            for m in MARKDOWN_IMG_RE.findall(text):
                if is_external_image_url(m):
                    occ.append(Occurrence(path, m, "markdown"))
            for m in HTML_IMG_RE.findall(text):
                if is_external_image_url(m):
                    occ.append(Occurrence(path, m, "img"))
            for m in HTML_A_IMG_RE.findall(text):
                if is_external_image_url(m):
                    occ.append(Occurrence(path, m, "a_img"))
    return occ


def post_year_slug(filename: str) -> Tuple[str, str]:
    """Infer year and slug from a post filename like YYYY-MM-DD-some-name.md.
    Accepts hyphens or underscores for the date separators. Removes trailing _fr.
    """
    base = os.path.basename(filename)
    m = re.match(r"(\d{4})[-_](\d{2})[-_](\d{2})-(.+)\.(?:md|markdown|html)$", base, re.IGNORECASE)
    if not m:
        # Fallback: unknown; put in unknown slug
        return ("unknown", os.path.splitext(base)[0])
    year = m.group(1)
    slug = m.group(4)
    if slug.endswith("_fr"):
        slug = slug[:-3]
    return year, slug


def filename_for_url(url: str) -> str:
    """Derive a filename from URL, prefixed with size segment if present (e.g., s1600_)."""
    p = urlparse(url)
    parts = [s for s in p.path.split("/") if s]
    name = parts[-1] if parts else "image"

    # If the penultimate segment looks like a size indicator (e.g., s1600 or s1600-h), prefix it
    if len(parts) >= 2 and re.match(r"s\d+(?:-[a-z])?", parts[-2] or ""):
        name = f"{parts[-2]}_{name}"

    # Ensure there is an extension; if not, keep as-is (will adjust after download if needed)
    return name


def ensure_unique_path(base_dir: str, filename: str, url: str) -> str:
    """Return a unique file path under base_dir for filename; append short hash if needed."""
    target = os.path.join(base_dir, filename)
    if not os.path.exists(target):
        return target
    stem, ext = os.path.splitext(filename)
    h = hashlib.sha1(url.encode("utf-8")).hexdigest()[:8]
    alt = os.path.join(base_dir, f"{stem}-{h}{ext}")
    if not os.path.exists(alt):
        return alt
    # last resort: numeric suffix
    i = 2
    while True:
        alt2 = os.path.join(base_dir, f"{stem}-{i}{ext}")
        if not os.path.exists(alt2):
            return alt2
        i += 1


def download(url: str, dest_path: str, timeout: int = 20, user_agent: str = "collect-external-images/1.0") -> Tuple[str, Optional[str]]:
    """Download URL to dest_path. Returns (final_path, detected_ext_or_None).
    If no extension and content-type is recognized, rename to add extension.
    """
    req = Request(url, headers={"User-Agent": user_agent})
    with urlopen(req, timeout=timeout) as resp:
        data = resp.read()
        ctype = resp.headers.get("Content-Type", "").split(";")[0].strip().lower()
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "wb") as fh:
        fh.write(data)

    detected_ext = None
    stem, ext = os.path.splitext(dest_path)
    if not ext:
        exts = {
            "image/jpeg": ".jpg",
            "image/png": ".png",
            "image/gif": ".gif",
            "image/webp": ".webp",
            "image/svg+xml": ".svg",
        }
        if ctype in exts:
            new_path = stem + exts[ctype]
            if not os.path.exists(new_path):
                os.rename(dest_path, new_path)
                dest_path = new_path
                detected_ext = exts[ctype]
    return dest_path, detected_ext


def replace_in_file(path: str, replacements: Dict[str, str], backup: bool = True) -> bool:
    with open(path, "r", encoding="utf-8", errors="ignore") as fh:
        text = fh.read()
    new_text = text
    changed = False
    for old, new in replacements.items():
        if old in new_text:
            new_text = new_text.replace(old, new)
            changed = True
    if changed:
        if backup:
            bpath = path + ".bak"
            if not os.path.exists(bpath):
                with open(bpath, "w", encoding="utf-8", errors="ignore") as fh:
                    fh.write(text)
        with open(path, "w", encoding="utf-8", errors="ignore") as fh:
            fh.write(new_text)
    return changed


def group_by_domain(urls: Iterable[str]) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for u in urls:
        try:
            netloc = urlparse(u).netloc
        except Exception:
            continue
        counts[netloc] = counts.get(netloc, 0) + 1
    return dict(sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])))


def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Collect external images and rewrite posts to local paths")
    ap.add_argument("--root", default=".", help="Repository root (default: .)")
    ap.add_argument("--posts-dir", default="_posts", help="Posts directory relative to root")
    ap.add_argument("--target-dir", default="images/blog", help="Base images directory relative to root")
    ap.add_argument("--only-domain", default=None, help="Only process URLs from this domain (optional)")
    ap.add_argument("--apply", action="store_true", help="Apply changes (download + rewrite). Default is dry-run")
    ap.add_argument("--no-backup", action="store_true", help="Do not create .bak backups when rewriting")
    ap.add_argument("--timeout", type=int, default=20, help="HTTP timeout in seconds")
    ap.add_argument("--user-agent", default="collect-external-images/1.0", help="HTTP User-Agent")
    ap.add_argument("--report", action="store_true", help="Print summary report of findings")
    ap.add_argument("--verbose", "-v", action="store_true", help="Verbose logging")
    args = ap.parse_args(argv)

    root = args.root
    posts_dir = os.path.join(root, args.posts_dir)
    target_base = os.path.join(root, args.target_dir)

    occ = scan_posts(posts_dir)
    if args.only_domain:
        occ = [o for o in occ if urlparse(o.url).netloc == args.only_domain]

    if not occ:
        print("No external image references found.")
        return 0

    # Report
    if args.report or not args.apply:
        counts = group_by_domain(o.url for o in occ)
        print("External image references by domain:")
        for dom, n in counts.items():
            print(f"  {dom}: {n}")
        print(f"Total references: {len(occ)} across {len(set(o.file for o in occ))} posts")

    # Build plan per file
    plan: Dict[str, Dict[str, str]] = {}
    for o in occ:
        year, slug = post_year_slug(o.file)
        rel_dir = os.path.join("images", "blog", year, slug)
        abs_dir = os.path.join(root, rel_dir)
        fname = filename_for_url(o.url)
        abs_path = ensure_unique_path(abs_dir, fname, o.url)
        # Compute relative URL path for post content
        rel_path_from_root = os.path.relpath(abs_path, root)
        site_path = "{{ site.url }}/" + rel_path_from_root.replace(os.sep, "/")
        plan.setdefault(o.file, {})[o.url] = site_path

    # Print plan in dry-run
    if not args.apply:
        print("\nDry-run plan (no changes made):")
        for f, repl in sorted(plan.items()):
            print(f"- {f}")
            for old, new in sorted(repl.items()):
                print(f"    {old} -> {new}")
        print("\nRun with --apply to download and rewrite. Use --only-domain to limit scope.")
        return 0

    # Apply: download and rewrite files
    any_changed = False
    for f, repl in sorted(plan.items()):
        # For each URL, download to its target path
        for old, new in sorted(repl.items()):
            # Determine absolute destination path from new site path
            # new looks like: {{ site.url }}/images/blog/YYYY/slug/filename
            rel_after_site = new.split("}}/")[-1]  # crude but effective for our known format
            dest_abs = os.path.join(root, rel_after_site)
            if args.verbose:
                print(f"Downloading {old} -> {dest_abs}")
            try:
                download(old, dest_abs, timeout=args.timeout, user_agent=args.user_agent)
            except Exception as e:
                print(f"ERROR: failed to download {old}: {e}")
                continue
        # Now rewrite the file
        changed = replace_in_file(f, repl, backup=not args.no_backup)
        any_changed = any_changed or changed
        print(f"Rewrote {f}: {'changed' if changed else 'no changes'}")

    if any_changed:
        print("Done. Backups saved as .bak alongside modified files.")
    else:
        print("Done. No changes were necessary.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

