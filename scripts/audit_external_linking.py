#!/usr/bin/env python3
"""Create a semicolon-separated inventory for the external-linking review."""

from __future__ import annotations

import csv
import re
from pathlib import Path
from urllib.parse import urlparse

import yaml


TERMS = [
    "SysML v2", "SysMLv2", "SysML", "KerML", "Systems Modeling API", "SysON",
    "Eclipse SysON", "Sirius Web", "Sirius", "Capella", "Eclipse Capella", "Arcadia",
    "Papyrus", "EMF", "Ecore", "Eclipse Foundation", "open source", "open innovation",
    "collaboration", "deployment", "support", "maintenance", "customization",
    "Team for Capella", "Cloud for Capella", "Publication for Capella",
]

TERM_RE = re.compile("|".join(re.escape(term) for term in sorted(TERMS, key=len, reverse=True)), re.IGNORECASE)
URL_RE = re.compile(r"https?://[^\s)>\"]+|\{\{\s*site\.url\s*\}\}[^\s)>\"]*")
FRONT_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)


def front_matter(text: str) -> dict:
    match = FRONT_RE.match(text)
    if not match:
        return {}
    value = yaml.safe_load(match.group(1)) or {}
    return value if isinstance(value, dict) else {}


def public_url(path: Path, data: dict) -> str:
    permalink = data.get("permalink")
    if isinstance(permalink, str) and permalink.strip():
        return permalink.strip()
    if path.parts[:1] == ("_posts",):
        slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", path.stem)
        categories = data.get("categories") or data.get("category") or []
        if isinstance(categories, str):
            categories = [categories]
        prefix = "/".join(str(item).strip() for item in categories if str(item).strip())
        return f"/{prefix + '/' if prefix else ''}{slug}/"
    without_suffix = path.with_suffix("").as_posix()
    if path.stem == "index":
        parent = path.parent.as_posix()
        return "/" if parent == "." else f"/{parent}/"
    return f"/{without_suffix}.html"


def recommendation(term: str) -> str:
    value = term.casefold()
    if "kerml" in value:
        return "https://www.omg.org/spec/KerML/1.0/About-KerML"
    if "systems modeling api" in value:
        return "https://www.omg.org/spec/SystemsModelingAPI/1.0/About-SystemsModelingAPI"
    if "sysml" in value:
        return "https://www.omg.org/sysml/sysmlv2/"
    if "syson" in value:
        return "https://mbse-syson.org/"
    if "arcadia" in value:
        return "https://mbse-capella.org/arcadia.html"
    if "capella" in value:
        return "https://mbse-capella.org/"
    if "sirius web" in value:
        return "https://eclipse.dev/sirius/sirius-web.html"
    if value == "sirius":
        return "https://eclipse.dev/sirius/"
    if value in {"emf", "ecore"}:
        return "https://eclipse.dev/emf/"
    if value == "papyrus":
        return "https://eclipse.dev/papyrus/"
    if "eclipse foundation" in value:
        return "https://www.eclipse.org/projects/handbook/"
    if "open innovation" in value or "customization" in value:
        return "https://www.obeosoft.com/en/services/custom-development/"
    if value in {"support", "maintenance"}:
        return "https://www.obeosoft.com/en/services/support-maintenance/"
    if value in {"collaboration", "deployment"}:
        return "https://www.obeosoft.com/en/products/obeo-enterprise-for-sirius/"
    if "team for capella" in value:
        return "https://www.obeosoft.com/en/products/team-for-capella/"
    if "cloud for capella" in value:
        return "https://www.obeosoft.com/en/products/cloud-for-capella/"
    if "publication for capella" in value:
        return "https://www.obeosoft.com/en/products/publication-for-capella/"
    return ""


def priority(path: Path) -> str:
    strategic = {"syson", "sysml-v2", "capella-arcadia", "modeling-platforms", "open-source-industrial"}
    if path.parts[:1] and path.parts[0] in strategic:
        return "P0"
    if path.parts[:2] == ("_posts", "talks") or path.parts[:1] == ("_posts",):
        return "P1" if path.name[:4].isdigit() and int(path.name[:4]) >= 2023 else "P2"
    return "P2"


def main() -> int:
    root = Path(".").resolve()
    output = root / "audit/external-linking-inventory.csv"
    rows: list[list[str]] = []
    for path in sorted(root.rglob("*.md")):
        if any(part.startswith(".") for part in path.relative_to(root).parts):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        data = front_matter(text)
        if not data:
            continue
        relative = path.relative_to(root)
        for line_number, line in enumerate(text.splitlines(), start=1):
            matches = list(TERM_RE.finditer(line))
            if not matches:
                continue
            current_links = ", ".join(URL_RE.findall(line))
            for match in matches:
                term = match.group(0)
                rows.append([
                    public_url(relative, data),
                    relative.as_posix(),
                    term,
                    line.strip()[:500],
                    current_links,
                    recommendation(term),
                    priority(relative),
                ])
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, delimiter=";")
        writer.writerow(["url_source", "fichier", "expression", "contexte", "lien_actuel", "lien_recommande", "priorite"])
        writer.writerows(rows)
    print(f"Indexed {len(rows)} strategic-term occurrences")
    print(f"CSV: {output.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
