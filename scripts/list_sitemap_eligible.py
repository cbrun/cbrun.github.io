#!/usr/bin/env python3
"""
List sitemap-eligible documents based on the same rules as sitemap.xml:
 - Include: pages, posts, and outputted collections
 - Exclude: items with noindex: true, sitemap: false, or draft: true (for posts/collections)

Outputs a concise report with computed URL (best-effort) and lastmod from git.
Also mirrors the special rule: tag pages are excluded if they have fewer than
3 associated posts (counted from posts' tags).

Usage:
  python scripts/list_sitemap_eligible.py [--root PATH] [--show-excluded]

Notes:
  - Requires PyYAML (`pip install pyyaml`).
  - Last modified time prefers git commit date; falls back to file mtime.
"""
from __future__ import annotations

import argparse
import dataclasses
import datetime as dt
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

try:
    import yaml  # type: ignore
except Exception as e:
    print("This tool requires PyYAML. Install with: pip install pyyaml", file=sys.stderr)
    raise


FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


@dataclasses.dataclass
class Doc:
    kind: str  # 'page' | 'post' | collection label
    path: Path  # repo-relative
    data: Dict
    include: bool
    reason: Optional[str] = None
    loc: Optional[str] = None  # full or site-relative URL
    lastmod: Optional[str] = None  # ISO 8601


def read_yaml_front_matter(p: Path) -> Tuple[Dict, int]:
    text = p.read_text(encoding="utf-8", errors="ignore")
    m = FRONT_MATTER_RE.match(text)
    if not m:
        return {}, 0
    yml = m.group(1)
    try:
        data = yaml.safe_load(yml) or {}
        if not isinstance(data, dict):
            data = {}
    except Exception:
        data = {}
    return data, m.end()


def load_config(root: Path) -> Dict:
    cfg = {}
    cfg_path = root / "_config.yml"
    if cfg_path.exists():
        with cfg_path.open("r", encoding="utf-8") as f:
            cfg = yaml.safe_load(f) or {}
    return cfg


def git_last_modified_iso(root: Path, rel: Path) -> Optional[str]:
    try:
        out = subprocess.check_output(
            [
                "git",
                "-C",
                str(root),
                "log",
                "-1",
                "--format=%cI",
                "--",
                str(rel).replace("\\", "/"),
            ],
            stderr=subprocess.DEVNULL,
        )
        iso = out.decode().strip()
        if iso:
            return iso
    except Exception:
        pass
    try:
        ts = (root / rel).stat().st_mtime
        return dt.datetime.fromtimestamp(ts, tz=dt.timezone.utc).isoformat()
    except Exception:
        return None


def norm_slash(s: str) -> str:
    return s.replace("\\", "/")


def infer_site_url(cfg: Dict) -> str:
    url = cfg.get("url") or ""
    if isinstance(url, str) and url.strip():
        return url.rstrip("/")
    return ""


def in_exclude_list(rel: Path, excludes: List[str]) -> bool:
    rp = norm_slash(str(rel))
    for ex in excludes:
        ex = ex.rstrip("/")
        if not ex:
            continue
        # Exact match or path prefix for directories
        if rp == ex or rp.startswith(ex + "/"):
            return True
    return False


def compute_page_url(root: Path, rel: Path, data: Dict, site_url: str) -> str:
    # Use explicit permalink if present
    permalink = data.get("permalink")
    if isinstance(permalink, str) and permalink.strip():
        url = permalink
    else:
        # Derive from path: about/index.md -> /about/ ; about.md -> /about/
        noext = norm_slash(str(rel.with_suffix("")))
        if noext.endswith("/index"):
            url = "/" + noext[: -len("index")].strip("/") + "/"
        else:
            url = "/" + noext.strip("/") + "/"
    if site_url:
        return site_url + url
    return url


def compute_post_url(rel: Path, data: Dict, site_url: str) -> str:
    # Respect explicit permalink first
    permalink = data.get("permalink")
    if isinstance(permalink, str) and permalink.strip():
        url = permalink
    else:
        # Extract slug from filename: YYYY-MM-DD-my-title.md -> my-title
        slug = rel.stem
        m = re.match(r"^(\d{4}-\d{2}-\d{2})-(.+)$", slug)
        if m:
            slug = m.group(2)
        # Categories can be string or list
        cats = data.get("categories") or data.get("category")
        if isinstance(cats, str):
            cats_list = [c for c in cats.split("/") if c]
        elif isinstance(cats, list):
            cats_list = [str(c) for c in cats]
        else:
            cats_list = []
        prefix = "/" + "/".join([c.strip("/") for c in cats_list if c])
        if prefix != "/":
            url = f"{prefix}/{slug}/"
        else:
            url = f"/{slug}/"
    if site_url:
        return site_url + url
    return url


def compute_collection_doc_url(root: Path, rel: Path, data: Dict, site_url: str) -> str:
    # Collections often set permalinks; otherwise derive from path
    permalink = data.get("permalink")
    if isinstance(permalink, str) and permalink.strip():
        url = permalink
    else:
        noext = norm_slash(str(rel.with_suffix("")))
        if noext.endswith("/index"):
            url = "/" + noext[: -len("index")].strip("/") + "/"
        else:
            url = "/" + noext.strip("/") + "/"
    if site_url:
        return site_url + url
    return url


def collect_docs(root: Path, cfg: Dict, show_excluded: bool) -> Tuple[List[Doc], List[Doc]]:
    out: List[Doc] = []
    excluded: List[Doc] = []
    site_url = infer_site_url(cfg)
    excludes = [norm_slash(e) for e in (cfg.get("exclude") or [])]

    # 1) Pages: scan for .md/.html with front matter outside of underscored dirs
    for p in root.rglob("*"):
        if p.is_dir():
            # Skip underscored directories (Jekyll internals and collections)
            if p.name.startswith("_") or p.name in {".git", "_site", "vendor", "node_modules"}:
                # But allow files under collections and posts to be handled later
                continue
            else:
                continue
        # files only handled here are those not in underscored dirs
    # Re-scan only top-level and non-underscore directories for pages
    candidate_pages: List[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        rel_dir = Path(dirpath).relative_to(root)
        # Skip underscored and known non-page dirs
        parts = rel_dir.parts
        if any(part.startswith("_") for part in parts):
            continue
        if parts and parts[0] in {"assets", "media", "images", "scripts", ".github", ".sass-cache", "audit"}:
            continue
        for fn in filenames:
            if not (fn.endswith(".md") or fn.endswith(".html")):
                continue
            rel = rel_dir / fn
            if in_exclude_list(rel, excludes):
                continue
            if rel.name == "sitemap.xml":
                continue
            candidate_pages.append(rel)

    for rel in candidate_pages:
        data, _ = read_yaml_front_matter(root / rel)
        if not data:
            continue  # not a templated page
        noindex = bool(data.get("noindex"))
        sm_off = data.get("sitemap") is False
        # Exclude asset-like URLs (mirrors sitemap.xml rule)
        url_preview = compute_page_url(root, rel, data, site_url)
        is_assetish = url_preview.endswith(".css") or url_preview.endswith(".js") or url_preview.endswith(".map") or "/assets/" in url_preview
        if noindex or sm_off or is_assetish:
            excluded.append(Doc("page", rel, data, include=False, reason=("noindex" if noindex else "sitemap:false")))
            continue
        doc = Doc("page", rel, data, include=True)
        doc.loc = url_preview
        doc.lastmod = git_last_modified_iso(root, rel)
        out.append(doc)

    # 2) Posts: _posts
    tag_counts: Dict[str, int] = {}
    posts_dir = root / "_posts"
    if posts_dir.exists():
        for p in sorted(posts_dir.glob("*")):
            if not (p.suffix.lower() in {".md", ".markdown", ".html"}):
                continue
            rel = p.relative_to(root)
            if in_exclude_list(rel, excludes):
                continue
            data, _ = read_yaml_front_matter(p)
            if not data:
                continue
            draft = bool(data.get("draft"))
            noindex = bool(data.get("noindex"))
            sm_off = data.get("sitemap") is False
            # Count tag associations regardless of noindex; drafts do not exist in _posts.
            tags = data.get("tags") or []
            if isinstance(tags, str):
                tags_list = [t.strip() for t in tags.split(",") if t.strip()]
            elif isinstance(tags, list):
                tags_list = [str(t) for t in tags]
            else:
                tags_list = []
            for t in tags_list:
                tag_counts[t] = tag_counts.get(t, 0) + 1
            if draft or noindex or sm_off:
                reason = "draft" if draft else ("noindex" if noindex else "sitemap:false")
                excluded.append(Doc("post", rel, data, include=False, reason=reason))
                continue
            doc = Doc("post", rel, data, include=True)
            doc.loc = compute_post_url(rel, data, site_url)
            doc.lastmod = git_last_modified_iso(root, rel)
            out.append(doc)

    # 3) Other collections: from _config.yml
    collections = cfg.get("collections") or {}
    if isinstance(collections, dict):
        for label, cval in collections.items():
            # Skip posts; only outputted collections
            if label == "posts":
                continue
            output = True
            if isinstance(cval, dict):
                output = cval.get("output", True) is True
            if not output:
                continue
            cdir = root / f"_{label}"
            if not cdir.exists():
                continue
            for p in sorted(cdir.rglob("*")):
                if p.is_dir():
                    continue
                if not (p.suffix.lower() in {".md", ".markdown", ".html"}):
                    continue
                rel = p.relative_to(root)
                if in_exclude_list(rel, excludes):
                    continue
                data, _ = read_yaml_front_matter(p)
                if not data:
                    continue
                draft = bool(data.get("draft"))
                noindex = bool(data.get("noindex"))
                sm_off = data.get("sitemap") is False
                # Special rule for 'tag' collection: exclude when fewer than 3 associated posts
                if label == "tag":
                    tag_name = data.get("tag")
                    if isinstance(tag_name, str):
                        n = tag_counts.get(tag_name, 0)
                        if n < 3:
                            excluded.append(Doc(label, rel, data, include=False, reason=f"tag<3 ({n})"))
                            continue
                if draft or noindex or sm_off:
                    reason = "draft" if draft else ("noindex" if noindex else "sitemap:false")
                    excluded.append(Doc(label, rel, data, include=False, reason=reason))
                    continue
                doc = Doc(label, rel, data, include=True)
                doc.loc = compute_collection_doc_url(root, rel, data, site_url)
                doc.lastmod = git_last_modified_iso(root, rel)
                out.append(doc)

    return out, excluded


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=str, default=None, help="Path to site root (defaults to repo root)")
    ap.add_argument("--show-excluded", action="store_true", help="Also list excluded items with reason")
    args = ap.parse_args()

    if args.root:
        root = Path(args.root).resolve()
    else:
        # try git to find toplevel
        root = Path.cwd()
        try:
            tl = subprocess.check_output(["git", "rev-parse", "--show-toplevel"]).decode().strip()
            if tl:
                root = Path(tl)
        except Exception:
            pass

    cfg = load_config(root)
    included, excluded = collect_docs(root, cfg, args.show_excluded)

    # Sort by kind then path
    included.sort(key=lambda d: (d.kind, str(d.path)))
    excluded.sort(key=lambda d: (d.kind, str(d.path)))

    site_url = infer_site_url(cfg)
    print(f"Site URL: {site_url or '(not set)'}")
    print(f"Eligible documents: {len(included)}")
    kinds = {}
    for d in included:
        kinds[d.kind] = kinds.get(d.kind, 0) + 1
    if kinds:
        print("By type:")
        for k in sorted(kinds):
            print(f"  - {k}: {kinds[k]}")
    print()
    print("Listing eligible URLs (type | lastmod | url | path):")
    for d in included:
        lm = d.lastmod or ""
        print(f"{d.kind:10s} | {lm:20s} | {d.loc or ''} | {norm_slash(str(d.path))}")

    if args.show_excluded and excluded:
        print()
        print(f"Excluded documents: {len(excluded)}")
        for d in excluded:
            print(f"{d.kind:10s} | {d.reason:14s} | {norm_slash(str(d.path))}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
