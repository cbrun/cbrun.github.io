#!/usr/bin/env python3
"""
Summarize dead links from scripts/detect_dead_links.py JSON report.

Outputs a readable text summary grouped by HTTP status code, listing in which
files each dead link appears, showing INTERNAL links first, then EXTERNAL.

Usage:
  python scripts/summarize_dead_links.py \
    --report scripts/dead_links_report.json

Options:
  --report PATH   Path to JSON report (default: scripts/dead_links_report.json)
  --markdown      Emit Markdown-friendly output
  --output PATH   Write summary to file instead of stdout
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import typing as t


def load_report(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"Report not found: {path}", file=sys.stderr)
        sys.exit(2)


def code_label(code: int | None, kind: str, reason: str | None) -> str:
    labels = {
        400: "400 Bad Request",
        401: "401 Unauthorized",
        403: "403 Forbidden",
        404: "404 Not Found",
        410: "410 Gone",
        429: "429 Too Many Requests",
        500: "500 Internal Server Error",
        502: "502 Bad Gateway",
        503: "503 Service Unavailable",
        504: "504 Gateway Timeout",
    }
    if kind == "internal_file" and reason == "file_missing":
        return "FILE MISSING (local asset)"
    if isinstance(code, int) and code > 0:
        return labels.get(code, f"{code}")
    return "NETWORK/OTHER ERROR"


def is_internal(rec: dict) -> bool:
    k = rec.get("kind")
    return k in {"internal_http", "internal_file"}


def group_dead_links(results: list[dict]) -> tuple[dict, dict]:
    """Return (internal_groups, external_groups) where each is {group_key: {...}}.

    group_key is a tuple used for ordering: (order_rank, http_code_or_rank, label)
    values are dict with keys: label, items (list of recs)
    """
    internal_groups: dict[tuple, dict] = {}
    external_groups: dict[tuple, dict] = {}
    for r in results:
        status = r.get("status")
        if status != "dead":
            continue
        kind = r.get("kind")
        code = r.get("http_status")
        reason = r.get("reason") or None
        label = code_label(code if isinstance(code, int) else None, kind, reason)

        # determine group ordering
        if label.startswith("FILE MISSING"):
            rank = (1_000_000,)  # after numeric status codes
        elif isinstance(code, int) and code > 0:
            rank = (code,)
        else:
            rank = (2_000_000,)

        key = (0,) + rank + (label,) if is_internal(r) else (1,) + rank + (label,)
        target = internal_groups if is_internal(r) else external_groups
        bucket = target.setdefault(key, {"label": label, "items": []})
        bucket["items"].append(r)
    return internal_groups, external_groups


def url_key(rec: dict) -> str:
    # Prefer normalized URL when HTTP, otherwise show original/raw
    k = rec.get("url_normalized") or rec.get("original") or rec.get("url_raw") or ""
    return str(k)


def _extract_domain(rec: dict) -> str:
    from urllib.parse import urlparse

    url = rec.get("url_normalized") or rec.get("original") or rec.get("url_raw") or ""
    kind = rec.get("kind")
    reason = rec.get("reason")
    if kind == "internal_file" or (kind == "internal_http" and reason == "file_exists"):
        return "local-asset"
    try:
        p = urlparse(str(url))
        if p.scheme in ("http", "https") and p.netloc:
            return p.netloc.lower()
    except Exception:
        pass
    return "unknown"


def _build_pivot(results: list[dict]) -> dict[str, dict[str, int]]:
    pivot: dict[str, dict[str, int]] = {}
    for r in results:
        if r.get("status") != "dead":
            continue
        label = code_label(r.get("http_status") if isinstance(r.get("http_status"), int) else None, r.get("kind"), r.get("reason") or None)
        dom = _extract_domain(r)
        pivot.setdefault(dom, {})[label] = pivot.setdefault(dom, {}).get(label, 0) + 1
    return pivot


def _label_sort_key(lbl: str) -> tuple:
    # Order numeric HTTP first by code, then FILE MISSING, then NETWORK
    if lbl.startswith("FILE MISSING"):
        return (1_000_000, lbl)
    if lbl.startswith("NETWORK/OTHER ERROR"):
        return (2_000_000, lbl)
    # Try parse leading int
    try:
        num = int(lbl.split()[0])
        return (num, lbl)
    except Exception:
        return (1_500_000, lbl)


def _render_pivot_table(title: str, pivot: dict[str, dict[str, int]], markdown: bool) -> str:
    if not pivot:
        return (f"{title}: none\n\n" if not markdown else f"### {title}: none\n\n")

    # Collect and sort columns (labels)
    all_labels = set()
    for row in pivot.values():
        all_labels.update(row.keys())
    labels = sorted(all_labels, key=_label_sort_key)

    # Sort domains by total desc then name
    domains = sorted(pivot.keys(), key=lambda d: (-sum(pivot[d].values()), d))

    lines = []
    if markdown:
        lines.append(f"### {title}\n")
        header = "| Domain | " + " | ".join(labels) + " | Total |\n"
        sep = "|---|" + "|".join(["---" for _ in labels]) + "|---|\n"
        lines.append(header)
        lines.append(sep)
        for dom in domains:
            row = pivot[dom]
            cells = [str(row.get(lbl, 0)) for lbl in labels]
            total = sum(row.values())
            lines.append("| " + dom + " | " + " | ".join(cells) + f" | {total} |\n")
        lines.append("\n")
    else:
        # Plain text table with simple padding
        col_widths = {"Domain": max(6, max((len(d) for d in domains), default=6))}
        for lbl in labels:
            col_widths[lbl] = max(len(lbl), max((len(str(pivot[d].get(lbl, 0))) for d in domains), default=1))
        col_widths["Total"] = max(5, max((len(str(sum(pivot[d].values()))) for d in domains), default=1))

        def fmt_cell(text: str, key: str) -> str:
            return text.ljust(col_widths[key])

        lines.append(f"{title}\n")
        header = fmt_cell("Domain", "Domain") + " | " + " | ".join(fmt_cell(lbl, lbl) for lbl in labels) + " | " + fmt_cell("Total", "Total") + "\n"
        sep = "-" * len(header) + "\n"
        lines.append(header)
        lines.append(sep)
        for dom in domains:
            row = pivot[dom]
            cells = [fmt_cell(str(row.get(lbl, 0)), lbl) for lbl in labels]
            total = fmt_cell(str(sum(row.values())), "Total")
            lines.append(fmt_cell(dom, "Domain") + " | " + " | ".join(cells) + " | " + total + "\n")
        lines.append("\n")
    return "".join(lines)


def format_summary(report: dict, markdown: bool = False) -> str:
    results = report.get("results", [])
    internal, external = group_dead_links(results)

    def fmt_header(text: str) -> str:
        return (f"## {text}\n" if markdown else f"{text}\n")

    def fmt_subheader(text: str) -> str:
        return (f"### {text}\n" if markdown else f"{text}\n")

    def fmt_bullet(text: str, indent: int = 0) -> str:
        prefix = ("  " * indent) + ("- " if markdown else "- ")
        return f"{prefix}{text}\n"

    out = []
    site_url = report.get("site_url") or ""
    src = report.get("root") or ""
    out.append(fmt_header("Dead Links Summary"))
    out.append(f"Report source: {src}\n")
    if site_url:
        out.append(f"Site URL: {site_url}\n")
    out.append("\n")

    def emit_section(title: str, groups: dict):
        if not groups:
            out.append(fmt_subheader(f"{title}: none"))
            return
        out.append(fmt_subheader(title))
        for key in sorted(groups.keys()):
            bucket = groups[key]
            label = bucket["label"]
            items = bucket["items"]
            # Group by URL to consolidate occurrences
            url_to_locs: dict[str, list[str]] = {}
            for r in items:
                url = url_key(r)
                loc = f"{r.get('file')}:{r.get('line')}"
                url_to_locs.setdefault(url, []).append(loc)
            # Order by number of occurrences desc, then URL
            ordered = sorted(url_to_locs.items(), key=lambda kv: (-len(kv[1]), kv[0]))
            out.append(fmt_bullet(f"{label} — {len(items)} occurrence(s) across {len(ordered)} link(s)"))
            for url, locs in ordered:
                out.append(fmt_bullet(f"{url}", indent=1))
                # compact locations on one line if short
                if len(locs) <= 6:
                    out.append(fmt_bullet("locations: " + ", ".join(locs), indent=2))
                else:
                    out.append(fmt_bullet("locations:", indent=2))
                    for loc in locs:
                        out.append(fmt_bullet(loc, indent=3))
        out.append("\n")

    emit_section("INTERNAL", internal)
    emit_section("EXTERNAL", external)

    # Domain x Error pivot tables
    internal_dead = [r for r in results if r.get("status") == "dead" and is_internal(r)]
    external_dead = [r for r in results if r.get("status") == "dead" and not is_internal(r)]
    out.append(_render_pivot_table("INTERNAL — Domain × Error", _build_pivot(internal_dead), markdown))
    out.append(_render_pivot_table("EXTERNAL — Domain × Error", _build_pivot(external_dead), markdown))

    return "".join(out)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Summarize dead links report")
    ap.add_argument("--report", default=str(Path(__file__).resolve().parent / "dead_links_report.json"))
    ap.add_argument("--markdown", action="store_true", help="Emit Markdown output")
    ap.add_argument("--output", default=None, help="Write summary to file")
    args = ap.parse_args(argv)

    report_path = Path(args.report)
    report = load_report(report_path)
    summary = format_summary(report, markdown=args.markdown)

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(summary, encoding="utf-8")
        print(f"Summary written to {out_path}")
    else:
        print(summary)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
