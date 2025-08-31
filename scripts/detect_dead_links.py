#!/usr/bin/env python3
"""
Detect dead links across Markdown files in this repository.

Features
- Scans all .md/.markdown files (skips .git/ and _site/ by default)
- Extracts Markdown and HTML links/images
- Resolves Jekyll `{{ site.url }}` to the configured site URL
- Classifies links as external HTTP(S), internal HTTP(S), or internal files
- Checks links concurrently with timeouts and minimal GETs when needed
- Writes a JSON report summarizing dead/ok links

Usage
  python scripts/detect_dead_links.py \
    --root . \
    --output scripts/dead_links_report.json \
    --site-url https://cedric.brun.io \
    --concurrency 16 \
    --timeout 8

Notes
- No external dependencies; uses stdlib only.
- HEAD is attempted first; falls back to a tiny GET range.
- Internal assets under /images, /media, /talks are also checked on disk.
- Relative paths (not starting with http(s) or /) are checked on disk.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import contextlib
import json
import os
from pathlib import Path
import re
import socket
import ssl
import sys
import time
import typing as t
import urllib.error
import urllib.parse
import urllib.request


DEFAULT_SITE_URL = "https://cedric.brun.io"
DEFAULT_TIMEOUT = 8
DEFAULT_CONCURRENCY = 16
DEFAULT_EXCLUDED_DOMAINS = ["twitter.com", "x.com"]


def load_site_url_from_config(repo_root: Path) -> str | None:
    cfg = repo_root / "_config.yml"
    if not cfg.exists():
        return None
    try:
        # Minimal parse: find a line starting with 'url:'
        for line in cfg.read_text(encoding="utf-8", errors="ignore").splitlines():
            m = re.match(r"^\s*url\s*:\s*(\S+)\s*$", line)
            if m:
                url = m.group(1)
                # Trim quotes if present
                url = url.strip('"\'')
                return url
    except Exception:
        return None
    return None


def iter_markdown_files(root: Path, include_html: bool = False) -> t.Iterator[Path]:
    exts = {".md", ".markdown"}
    if include_html:
        exts.add(".html")
    skip_dirs = {".git", "_site", "node_modules", "venv", ".venv"}
    for dirpath, dirnames, filenames in os.walk(root):
        # In-place prune
        dirnames[:] = [d for d in dirnames if d not in skip_dirs and not d.startswith(".")]
        for fn in filenames:
            p = Path(dirpath) / fn
            if p.suffix.lower() in exts:
                yield p


MD_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
MD_IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
HTML_HREF_RE = re.compile(r"<a\s+[^>]*href=\"([^\"]+)\"", re.IGNORECASE)
HTML_HREF_SQ_RE = re.compile(r"<a\s+[^>]*href='([^']+)'", re.IGNORECASE)
HTML_SRC_RE = re.compile(r"<img\s+[^>]*src=\"([^\"]+)\"", re.IGNORECASE)
HTML_SRC_SQ_RE = re.compile(r"<img\s+[^>]*src='([^']+)'", re.IGNORECASE)
MD_REFDEF_RE = re.compile(r"^\s*\[([^\]]+)\]:\s*(\S+)\s*(?:\"[^\"]*\"|'[^']*')?\s*$")
MD_REFLINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\[([^\]]+)\]")


def strip_code_fences(text: str) -> str:
    # Remove fenced code blocks to reduce false positives
    return re.sub(r"```[\s\S]*?```", "", text)


def parse_links_from_markdown(path: Path) -> list[dict]:
    content = path.read_text(encoding="utf-8", errors="ignore")
    # strip YAML front matter
    if content.startswith("---\n"):
        end = content.find("\n---\n", 4)
        if end != -1:
            content = content[end + 5 :]
    content_wo_code = strip_code_fences(content)
    lines = content_wo_code.splitlines()

    # Reference definitions
    ref_defs: dict[str, str] = {}
    for ln in lines:
        m = MD_REFDEF_RE.match(ln)
        if m:
            ref_defs[m.group(1).strip().lower()] = m.group(2).strip()

    results: list[dict] = []

    def add_result(url: str, line_no: int, kind: str, raw: str):
        results.append(
            {
                "file": str(path),
                "line": line_no,
                "url_raw": raw,
                "url": url,
                "source": kind,
            }
        )

    for idx, ln in enumerate(lines, start=1):
        # Markdown inline links
        for m in MD_LINK_RE.finditer(ln):
            raw = m.group(1).strip()
            # Keep full raw; normalization will strip optional title
            add_result(raw, idx, "md_link", raw)

        # Markdown images
        for m in MD_IMAGE_RE.finditer(ln):
            raw = m.group(1).strip()
            add_result(raw, idx, "md_image", raw)

        # HTML anchors
        for m in HTML_HREF_RE.finditer(ln):
            add_result(m.group(1).strip(), idx, "html_a", m.group(1).strip())
        for m in HTML_HREF_SQ_RE.finditer(ln):
            add_result(m.group(1).strip(), idx, "html_a", m.group(1).strip())

        # HTML images
        for m in HTML_SRC_RE.finditer(ln):
            add_result(m.group(1).strip(), idx, "html_img", m.group(1).strip())
        for m in HTML_SRC_SQ_RE.finditer(ln):
            add_result(m.group(1).strip(), idx, "html_img", m.group(1).strip())

        # Reference-style links [text][id]
        for m in MD_REFLINK_RE.finditer(ln):
            key = m.group(1).strip().lower()
            if key in ref_defs:
                url = ref_defs[key]
                add_result(url, idx, "md_ref", url)

    return results


SITE_URL_VAR_RE = re.compile(r"\{\{\s*site\.url\s*\}\}")


def normalize_and_classify_url(
    url: str,
    file_path: Path,
    site_url: str,
    repo_root: Path,
) -> dict:
    """Return info with normalized URL and classification.

    Returns keys: kind, url_to_check, file_exists_path (optional), original
    """
    original = url
    url = (url or "").strip()
    if not url:
        return {"kind": "skipped", "reason": "empty", "original": original}

    # Strip optional Markdown title at the end: ... (url "title") or (url 'title')
    url = re.sub(r"\s+(\"[^\"]*\"|'[^']*')\s*$", "", url)
    # Strip angle brackets
    if url.startswith("<") and url.endswith(">"):
        url = url[1:-1].strip()
    # Replace Jekyll site.url (allow it anywhere in the string)
    url = SITE_URL_VAR_RE.sub(site_url, url)

    # If Liquid variables remain, skip (source uses templates we can't resolve here)
    if "{{" in url or "}}" in url:
        return {"kind": "skipped", "reason": "liquid_variable", "original": original}

    # Ignore certain schemes/fragments
    lowered = url.lower()
    if lowered.startswith("#"):
        return {"kind": "skipped", "reason": "fragment", "original": original}
    if any(lowered.startswith(s) for s in ("mailto:", "tel:", "data:", "javascript:")):
        return {"kind": "skipped", "reason": "non-http", "original": original}

    # Remove fragment for checking
    base, _hash, _frag = url.partition("#")
    url = base

    # Protocol-relative
    if url.startswith("//"):
        url = "https:" + url

    # Absolute HTTP(S)
    if re.match(r"^https?://", url, re.IGNORECASE):
        parsed = urllib.parse.urlparse(url)
        if parsed.netloc and parsed.netloc != urllib.parse.urlparse(site_url).netloc:
            return {"kind": "external_http", "url_to_check": url, "original": original}
        else:
            return {"kind": "internal_http", "url_to_check": url, "original": original}

    # Root-relative path
    if url.startswith("/"):
        # Heuristic: if it's under known asset dirs, also check file existence
        file_candidate = None
        if url.startswith("/images/") or url.startswith("/media/") or url.startswith("/talks/"):
            file_candidate = (repo_root / url.lstrip("/")).resolve()
            if not str(file_candidate).startswith(str(repo_root)):
                file_candidate = None
        return {
            "kind": "internal_http",
            "url_to_check": site_url.rstrip("/") + url,
            "file_exists_path": str(file_candidate) if file_candidate else None,
            "original": original,
        }

    # Relative path -> treat as file path against the markdown file location
    abs_file = (file_path.parent / url).resolve()
    if str(abs_file).startswith(str(repo_root)) and abs_file.exists():
        return {"kind": "internal_file", "file_exists_path": str(abs_file), "original": original}
    # Fallback: try as an internal HTTP URL (may be a page permalink)
    return {
        "kind": "internal_http",
        "url_to_check": site_url.rstrip("/") + "/" + url.lstrip("/"),
        "original": original,
    }


class HttpChecker:
    def __init__(self, timeout: int = DEFAULT_TIMEOUT, user_agent: str | None = None, retries: int = 1):
        self.timeout = timeout
        self.user_agent = user_agent or (
            "Mozilla/5.0 (compatible; DeadLinkScanner/1.0; +https://cedric.brun.io)"
        )
        self.retries = max(0, retries)
        self._cache: dict[str, dict] = {}
        self._lock = contextlib.ExitStack()  # dummy for with-like API
        self._cache_lock = None
        # Lightweight lock implemented with list as mutex fallback
        self._cache_lock = object()

    def check(self, url: str) -> dict:
        # Cache to avoid duplicate network calls
        cached = self._cache.get(url)
        if cached is not None:
            return cached

        result = self._check_no_cache(url)
        self._cache[url] = result
        return result

    def _request(self, url: str, method: str) -> t.Tuple[int, str]:
        req = urllib.request.Request(url)
        req.add_header("User-Agent", self.user_agent)
        if method == "HEAD":
            # Override method for HEAD
            req.get_method = lambda: "HEAD"  # type: ignore[attr-defined]
        else:
            # Try tiny range to minimize transfer
            req.add_header("Range", "bytes=0-0")
        with urllib.request.urlopen(req, timeout=self.timeout) as resp:
            code = getattr(resp, "status", resp.getcode())
            # If partial content due to Range, still OK
            msg = getattr(resp, "reason", "") or ""
            return int(code), str(msg)

    def _check_no_cache(self, url: str) -> dict:
        attempts = ["HEAD", "GET"]
        last_error: str | None = None
        last_code: int | None = None
        for i in range(self.retries + 1):
            for method in attempts:
                try:
                    code, msg = self._request(url, method)
                    status = "ok" if code < 400 else "dead"
                    return {"status": status, "http_status": code, "message": msg}
                except urllib.error.HTTPError as e:
                    # HTTPError is also a response (>=400)
                    last_code = e.code
                    if e.code in (405, 501) and method == "HEAD":
                        # Try GET next
                        continue
                    return {"status": "dead", "http_status": int(e.code), "message": str(e)}
                except (urllib.error.URLError, socket.timeout, ssl.SSLError, ConnectionError) as e:
                    last_error = f"{type(e).__name__}: {e}"
                    # Try next attempt/method
                    continue
                except Exception as e:
                    last_error = f"{type(e).__name__}: {e}"
                    continue
        # If here, failed all attempts
        return {
            "status": "dead",
            "http_status": last_code or 0,
            "message": last_error or "Unknown error",
        }


def check_link(record: dict, site_url: str, repo_root: Path, http: HttpChecker) -> dict:
    file_path = Path(record["file"]) if isinstance(record.get("file"), str) else record.get("file")
    norm = normalize_and_classify_url(record["url"], file_path, site_url, repo_root)
    out = {
        "file": record["file"],
        "line": record["line"],
        "url_raw": record["url_raw"],
        "url_normalized": norm.get("url_to_check") or norm.get("file_exists_path") or record["url"],
        "kind": norm.get("kind"),
        "source": record.get("source"),
        "original": norm.get("original", record.get("url")),
    }

    if norm.get("kind") == "skipped":
        out.update({"status": "skipped", "reason": norm.get("reason", "")})
        return out

    if norm.get("kind") == "internal_file":
        exists = Path(norm["file_exists_path"]).exists()
        out.update({"status": "ok" if exists else "dead", "reason": "file_exists" if exists else "file_missing"})
        return out

    # If we also have a file candidate for internal_http, short-circuit to OK when it exists
    file_candidate = norm.get("file_exists_path")
    if file_candidate:
        if Path(file_candidate).exists():
            out.update({"status": "ok", "reason": "file_exists"})
            return out

    # HTTP check
    url_to_check = norm.get("url_to_check")
    if not url_to_check:
        out.update({"status": "skipped", "reason": "no_check_target"})
        return out

    r = http.check(url_to_check)
    out.update(r)
    return out


def _domain_matches(host: str, domain: str) -> bool:
    host = host.lower().split(":", 1)[0]
    domain = domain.lower()
    return host == domain or host.endswith("." + domain)


def _is_excluded(url: str, excluded_domains: list[str]) -> bool:
    try:
        p = urllib.parse.urlparse(url)
        if p.scheme not in ("http", "https") or not p.netloc:
            return False
        for d in excluded_domains:
            if _domain_matches(p.netloc, d):
                return True
    except Exception:
        return False
    return False


def build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Detect dead links in Markdown files")
    p.add_argument("--root", default=str(Path(__file__).resolve().parents[1]), help="Repository root to scan")
    p.add_argument("--output", default=str(Path(__file__).resolve().parent / "dead_links_report.json"), help="JSON report output path")
    p.add_argument("--site-url", default=None, help="Base site URL (defaults from _config.yml or hardcoded fallback)")
    p.add_argument("--concurrency", type=int, default=DEFAULT_CONCURRENCY, help="Number of concurrent workers")
    p.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT, help="Per-request timeout in seconds")
    p.add_argument("--retries", type=int, default=1, help="Number of network retries")
    p.add_argument("--include-html", action="store_true", help="Also scan .html files (archives)")
    p.add_argument(
        "--exclude-domain",
        action="append",
        default=[],
        help="Domain to exclude from HTTP checks (can be passed multiple times)",
    )
    p.add_argument("--no-progress", action="store_true", help="Disable progress output while checking")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    repo_root = Path(args.root).resolve()
    if not repo_root.exists():
        print(f"Root path does not exist: {repo_root}", file=sys.stderr)
        return 2

    site_url = args.site_url or load_site_url_from_config(repo_root) or DEFAULT_SITE_URL
    # Normalize site_url: no trailing slash
    site_url = site_url.rstrip("/")

    files = list(iter_markdown_files(repo_root, include_html=args.include_html))
    all_links: list[dict] = []
    for fp in files:
        all_links.extend(parse_links_from_markdown(fp))

    # Deduplicate by (file,line,url_raw) to avoid repeated checks per line
    seen = set()
    uniq_links = []
    for rec in all_links:
        key = (rec["file"], rec["line"], rec["url_raw"])
        if key not in seen:
            seen.add(key)
            uniq_links.append(rec)

    http = HttpChecker(timeout=args.timeout, retries=args.retries)
    excluded_domains = list(DEFAULT_EXCLUDED_DOMAINS) + list(args.exclude_domain or [])

    total = len(uniq_links)
    ok_count = dead_count = skipped_count = 0
    results: list[dict] = []
    started = time.time()

    if not args.no_progress:
        print(f"Checking {total} unique links with {max(1, args.concurrency)} workers...")

    next_milestone = max(1, total // 20)  # ~5% steps
    last_log = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.concurrency)) as pool:
        fut_to = {}
        done = 0  # progress counter, includes excluded/skipped items
        for rec in uniq_links:
            # Pre-normalize to see if excluded (only for HTTP checks)
            norm = normalize_and_classify_url(rec["url"], Path(rec["file"]), site_url, repo_root)
            url_to_check = norm.get("url_to_check")
            if url_to_check and _is_excluded(url_to_check, excluded_domains):
                # synthesize a skipped result
                results.append(
                    {
                        "file": rec["file"],
                        "line": rec["line"],
                        "url_raw": rec["url_raw"],
                        "url_normalized": url_to_check,
                        "kind": norm.get("kind"),
                        "source": rec.get("source"),
                        "original": norm.get("original", rec.get("url")),
                        "status": "skipped",
                        "reason": "excluded_domain",
                    }
                )
                skipped_count += 1
                done += 1
                continue
            fut = pool.submit(check_link, rec, site_url, repo_root, http)
            fut_to[fut] = rec
        for fut in concurrent.futures.as_completed(fut_to):
            try:
                r = fut.result()
            except Exception as e:
                rec = fut_to[fut]
                r = {
                    "file": rec["file"],
                    "line": rec["line"],
                    "url_raw": rec["url_raw"],
                    "url_normalized": rec.get("url"),
                    "kind": "error",
                    "status": "dead",
                    "message": f"Unhandled: {type(e).__name__}: {e}",
                }
            results.append(r)
            status = r.get("status")
            if status == "ok":
                ok_count += 1
            elif status == "dead":
                dead_count += 1
            else:
                skipped_count += 1
            done += 1

            if not args.no_progress:
                now = time.time()
                if done % next_milestone == 0 or (now - last_log) >= 1.5 or done == total:
                    print(
                        f"Progress: {done}/{total} checked  ok={ok_count} dead={dead_count} skipped={skipped_count}",
                        flush=True,
                    )
                    last_log = now

    duration = time.time() - started

    summary = {
        "total_files": len(files),
        "total_links_found": len(all_links),
        "total_links_checked": len(uniq_links),
        "duration_sec": round(duration, 2),
    }
    counts = {"ok": 0, "dead": 0, "skipped": 0}
    for r in results:
        counts[r.get("status", "skipped")] = counts.get(r.get("status", "skipped"), 0) + 1
    summary.update(counts)

    report = {
        "site_url": site_url,
        "root": str(repo_root),
        "summary": summary,
        "results": sorted(
            results,
            key=lambda r: (0 if r.get("status") == "dead" else 1, str(r.get("file")), int(r.get("line", 0))),
        ),
    }

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    # Console summary
    print(f"Scanned {summary['total_files']} files; checked {summary['total_links_checked']} unique links in {summary['duration_sec']}s")
    print(f"OK: {summary['ok']}  DEAD: {summary['dead']}  SKIPPED: {summary['skipped']}")
    if summary["dead"]:
        print("Sample dead links:")
        shown = 0
        for r in report["results"]:
            if r.get("status") == "dead":
                loc = f"{r.get('file')}:{r.get('line')}"
                print(f"- {loc} -> {r.get('url_normalized')} ({r.get('message') or r.get('http_status')})")
                shown += 1
                if shown >= 10:
                    break
        print(f"Full report at: {out_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
