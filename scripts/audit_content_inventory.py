#!/usr/bin/env python3
"""Build a reproducible SEO/editorial inventory of Jekyll content.

The script scans source documents with YAML front matter, derives their public
URLs, extracts content and linking signals, then writes a detailed CSV and a
compact Markdown summary. Editorial classifications are heuristics intended
for review; they never modify source content.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import html
from html.parser import HTMLParser
import os
from pathlib import Path
import re
import subprocess
from typing import Any
from urllib.parse import urljoin, urlparse

import yaml


SITE_URL = "https://cedric.brun.io"
CONTENT_SUFFIXES = {".md", ".markdown", ".html", ".htm"}
EXCLUDED_DIRS = {
    ".git",
    ".jekyll-cache",
    ".obsidian",
    "_site",
    "assets",
    "lib",
    "node_modules",
    "talks",
    "tmp",
    "vendor",
}
NON_CONTENT_FILES = {"AGENTS.md", "AGENTS_HISTORY.md", "REFONTE.md", "README.md"}
MAIN_TAGS = {"sirius-web", "mbse", "ecore", "capella", "obeo"}

CSV_FIELDS = [
    "path",
    "url",
    "content_type",
    "title",
    "h1",
    "seo_title",
    "meta_description",
    "date_published",
    "date_modified",
    "categories",
    "tags",
    "lang",
    "draft",
    "noindex",
    "word_count",
    "internal_links",
    "external_links",
    "inbound_internal_links",
    "links_obeo",
    "links_eclipse",
    "links_omg",
    "images",
    "images_with_alt",
    "images_missing_alt",
    "cluster_probable",
    "intent_probable",
    "primary_query_probable",
    "quality_score",
    "quality_estimated",
    "priority",
    "recommendation",
    "translation_en",
    "translation_fr",
    "canonical_declared",
    "canonical",
    "front_matter_error",
]


class ContentHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[str] = []
        self.images: list[tuple[str, str | None]] = []
        self.h1_parts: list[str] = []
        self._in_h1 = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "a" and values.get("href"):
            self.links.append(values["href"] or "")
        elif tag == "img" and values.get("src"):
            self.images.append((values["src"] or "", values.get("alt")))
        elif tag == "h1":
            self._in_h1 = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "h1":
            self._in_h1 = False

    def handle_data(self, data: str) -> None:
        if self._in_h1:
            self.h1_parts.append(data)


def split_front_matter(text: str) -> tuple[str | None, str]:
    match = re.match(r"\A---\s*\r?\n(.*?)\r?\n---\s*(?:\r?\n|\Z)", text, re.DOTALL)
    if not match:
        return None, text
    return match.group(1), text[match.end() :]


def as_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str):
        return [item for item in re.split(r"[,\s]+", value.strip()) if item]
    return [str(value).strip()]


def as_bool(value: Any) -> bool:
    return str(value).strip().lower() in {"true", "yes", "1", "on"}


def scalar(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (dt.date, dt.datetime)):
        return value.isoformat()
    return str(value).strip()


def strip_markup(content: str) -> str:
    text = re.sub(r"```.*?```", " ", content, flags=re.DOTALL)
    text = re.sub(r"`[^`]*`", " ", text)
    text = re.sub(r"\{[%{].*?[}%]\}", " ", text, flags=re.DOTALL)
    text = re.sub(r"!\[([^]]*)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"<script\b.*?</script>|<style\b.*?</style>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"^\s{0,3}[#>*+-]+\s*", "", text, flags=re.MULTILINE)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def normalize_liquid(content: str) -> str:
    content = re.sub(r"\{\{\s*site\.url\s*\}\}", SITE_URL, content)
    return re.sub(r"\{\{\s*site\.baseurl\s*\}\}", "", content)


def markdown_links(content: str) -> list[str]:
    normalized = normalize_liquid(content)
    links = re.findall(r"(?<!!)\[[^]]*\]\(\s*<?([^)>\s]+)>?(?:\s+['\"][^)]*['\"])?\s*\)", normalized)
    links.extend(re.findall(r"^\s*\[[^]]+\]:\s*<?([^>\s]+)>?", normalized, flags=re.MULTILINE))
    return links


def markdown_images(content: str) -> list[tuple[str, str | None]]:
    normalized = normalize_liquid(content)
    return [
        (url, alt if alt.strip() else None)
        for alt, url in re.findall(r"!\[([^]]*)\]\(\s*<?([^)>\s]+)>?(?:\s+['\"][^)]*['\"])?\s*\)", normalized)
    ]


def extract_content_signals(content: str) -> tuple[list[str], list[tuple[str, str | None]], str]:
    normalized = normalize_liquid(content)
    parser = ContentHTMLParser()
    try:
        parser.feed(normalized)
    except Exception:
        pass
    links = markdown_links(content) + parser.links
    images = markdown_images(content) + parser.images
    markdown_h1 = re.search(r"^#\s+(.+?)\s*$", content, flags=re.MULTILINE)
    html_h1 = re.sub(r"\s+", " ", " ".join(parser.h1_parts)).strip()
    return links, images, markdown_h1.group(1).strip() if markdown_h1 else html_h1


def content_type(path: Path) -> str:
    first = path.parts[0] if path.parts else ""
    if first == "_posts":
        return "post"
    if first == "_drafts":
        return "draft"
    if first == "_talks":
        return "talk-collection"
    if first == "_tag":
        return "tag"
    if first == "_category":
        return "category"
    if first.startswith("_"):
        return "collection"
    return "page"


def post_slug(path: Path) -> str:
    return re.sub(r"^\d{4}-\d{2}-\d{2}-", "", path.stem)


def public_url(path: Path, data: dict[str, Any]) -> str:
    permalink = scalar(data.get("permalink") or data.get("slug"))
    if permalink:
        parsed = urlparse(permalink)
        url = parsed.path if parsed.scheme else permalink
        return url if url.startswith("/") else f"/{url}"

    kind = content_type(path)
    if kind == "post":
        categories = as_list(data.get("categories") or data.get("category"))
        prefix = "/".join(categories)
        return f"/{prefix + '/' if prefix else ''}{post_slug(path)}/"
    if kind in {"tag", "category"}:
        return f"/{kind}/{path.stem}/"
    if kind == "talk-collection":
        return ""
    relative = path.with_suffix("")
    if relative.name == "index":
        parent = relative.parent.as_posix()
        return "/" if parent == "." else f"/{parent}/"
    return f"/{relative.as_posix()}.html"


def git_modified_dates(root: Path) -> dict[str, str]:
    command = ["git", "log", "--format=@@%cs", "--name-only", "--", "*.md", "*.markdown", "*.html"]
    result = subprocess.run(command, cwd=root, text=True, capture_output=True, check=False)
    dates: dict[str, str] = {}
    current = ""
    for line in result.stdout.splitlines():
        if line.startswith("@@"):
            current = line[2:]
        elif line and current and line not in dates:
            dates[line] = current
    return dates


def find_documents(root: Path) -> list[Path]:
    documents: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in CONTENT_SUFFIXES:
            continue
        relative = path.relative_to(root)
        if relative.parts[0] in EXCLUDED_DIRS or any(part.startswith(".") for part in relative.parts) or path.name in NON_CONTENT_FILES:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        front_matter, _ = split_front_matter(text)
        if front_matter is not None:
            documents.append(relative)
    return sorted(documents)


def classify_cluster(title: str, tags: list[str], content: str) -> str:
    title_value = title.lower()
    tag_values = {tag.lower() for tag in tags}

    # Strong title signals express the page's subject more reliably than body mentions.
    if "syson" in title_value:
        return "syson"
    if any(term in title_value for term in ["sysml v2", "sysmlv2", "kerml"]):
        return "sysml-v2"
    if any(term in title_value for term in ["capella", "arcadia"]):
        return "capella-arcadia"
    if any(term in title_value for term in ["sirius web", "web-based modeling", "web based modeling", "modeling platform"]):
        return "modeling-platforms"
    if any(term in title_value for term in ["open source", "open-source", "eclipse foundation", "governance"]):
        return "open-source-industrial"

    if "syson" in tag_values:
        return "syson"
    if tag_values.intersection({"sysmlv2", "sysml-v2", "kerml"}):
        return "sysml-v2"
    if tag_values.intersection({"capella", "arcadia"}):
        return "capella-arcadia"
    if tag_values.intersection({"sirius-web", "sirius", "dsl"}):
        return "modeling-platforms"
    if tag_values.intersection({"opensource", "open-source", "sustainability"}):
        return "open-source-industrial"

    sample = strip_markup(content)[:12000].lower()
    scores = {
        "sysml-v2": score_terms(sample, {"sysml v2": 8, "sysmlv2": 8, "kerml": 7, "sysml v1": 4}),
        "syson": score_terms(sample, {"syson": 10, "eclipse syson": 6}),
        "modeling-platforms": score_terms(
            sample,
            {"sirius web": 9, "web-based modeling": 7, "web based modeling": 7, "modeling platform": 6, "dsl": 2, "sirius": 2},
        ),
        "open-source-industrial": score_terms(
            sample,
            {"open source": 5, "opensource": 5, "eclipse foundation": 7, "governance": 4, "community": 2, "sustainab": 4},
        ),
        "capella-arcadia": score_terms(sample, {"capella": 7, "arcadia": 8, "mbse": 2}),
    }
    # Product-specific clusters win close ties over broader themes.
    tie_order = ["syson", "sysml-v2", "capella-arcadia", "modeling-platforms", "open-source-industrial"]
    winner = max(tie_order, key=lambda key: (scores[key], -tie_order.index(key)))
    return winner if scores[winner] >= 18 and len(sample.split()) >= 250 else "non-strategic"


def score_terms(sample: str, terms: dict[str, int]) -> int:
    return sum(min(sample.count(term), 4) * weight for term, weight in terms.items())


def classify_intent(title: str, content: str) -> str:
    value = title.lower()
    if any(term in value for term in [" vs ", "versus", "comparison", "difference", "compare"]):
        return "comparison"
    if any(term in value for term in ["how to", "tutorial", "guide", "getting started", "cookbook"]):
        return "how-to"
    if any(term in value for term in ["what is", "understanding", "introduction", "overview", "explained"]):
        return "understanding"
    if any(term in value for term in ["release", "available", "announcing", "launch", "new version"]):
        return "release-or-announcement"
    if any(term in value for term in ["conference", "eclipsecon", "models ", "days", "summit", "keynote", "talk"]):
        return "event-or-talk"
    if value.endswith("?") or any(term in value for term in ["why ", "future", "thoughts", "lessons"]):
        return "analysis-or-opinion"
    if len(strip_markup(content).split()) < 180:
        return "short-update"
    return "technical-or-experience-article"


def quality_score(data: dict[str, Any], h1: str, words: int, internal: int, external: int, images: int, missing_alt: int) -> int:
    score = 0
    description = scalar(data.get("description") or data.get("excerpt"))
    score += 15 if scalar(data.get("title")) else 0
    score += 15 if description else 0
    score += 10 if 110 <= len(description) <= 220 else 4 if description else 0
    score += 25 if words >= 800 else 18 if words >= 400 else 10 if words >= 180 else 3
    score += 10 if internal >= 2 else 5 if internal else 0
    score += 8 if external else 0
    score += 7 if not h1 else 2  # Body H1 is undesirable because layouts already emit one.
    score += 5 if images == 0 or missing_alt == 0 else 0
    score += 5 if as_list(data.get("tags")) and MAIN_TAGS.intersection(as_list(data.get("tags"))) else 0
    return min(score, 100)


def estimate_quality(score: int) -> str:
    if score >= 75:
        return "strong"
    if score >= 50:
        return "medium"
    return "weak"


def recommendation(kind: str, cluster: str, words: int, score: int, draft: bool, noindex: bool, date: str) -> str:
    if kind in {"tag", "category"}:
        return "optimize" if cluster != "non-strategic" else "keep-without-major-change"
    if noindex:
        return "keep-excluded-from-index"
    if draft:
        return "enrich" if score < 75 else "optimize"
    if cluster != "non-strategic":
        if score >= 75:
            return "keep-without-major-change"
        return "optimize" if words >= 400 else "enrich"
    year = int(date[:4]) if re.match(r"^\d{4}", date) else 0
    if words < 180 and year and year < 2022:
        return "keep-as-non-strategic-archive"
    return "keep-as-non-strategic-content"


def priority(cluster: str, score: int, kind: str, draft: bool, noindex: bool) -> str:
    if noindex or kind in {"tag", "category", "talk-collection"}:
        return "low"
    if cluster != "non-strategic" and (score < 75 or draft):
        return "high"
    if cluster != "non-strategic":
        return "medium"
    return "low"


def normalize_internal_target(link: str, source_url: str) -> str:
    link = normalize_liquid(link).strip()
    if not link or link.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
        return ""
    parsed = urlparse(link)
    if parsed.scheme in {"http", "https"} and parsed.netloc not in {"cedric.brun.io", "www.cedric.brun.io"}:
        return ""
    if parsed.scheme in {"http", "https"}:
        target = parsed.path
    else:
        target = urlparse(urljoin(f"{SITE_URL}{source_url}", link)).path
    target = re.sub(r"/index\.html$", "/", target)
    return target or "/"


def external_domain(link: str) -> str:
    parsed = urlparse(normalize_liquid(link).strip())
    if parsed.scheme not in {"http", "https"} or parsed.netloc in {"cedric.brun.io", "www.cedric.brun.io"}:
        return ""
    return parsed.netloc.lower().split(":", 1)[0]


def domain_matches(domain: str, suffixes: tuple[str, ...]) -> bool:
    return any(domain == suffix or domain.endswith(f".{suffix}") for suffix in suffixes)


def read_document(root: Path, path: Path, modified_dates: dict[str, str]) -> dict[str, Any]:
    text = (root / path).read_text(encoding="utf-8", errors="replace")
    front_matter, content = split_front_matter(text)
    error = ""
    try:
        data = yaml.safe_load(front_matter or "") or {}
        if not isinstance(data, dict):
            raise ValueError("front matter is not a mapping")
    except Exception as exc:
        data = {}
        error = str(exc).replace("\n", " ")

    links, images, h1 = extract_content_signals(content)
    url = public_url(path, data)
    internal_targets = [normalize_internal_target(link, url) for link in links]
    internal_targets = [target for target in internal_targets if target]
    domains = [external_domain(link) for link in links]
    domains = [domain for domain in domains if domain]
    tags = as_list(data.get("tags"))
    categories = as_list(data.get("categories") or data.get("category"))
    words = len(re.findall(r"\b[\w'-]+\b", strip_markup(content), flags=re.UNICODE))
    date = scalar(data.get("date"))
    if not date and content_type(path) == "post":
        match = re.match(r"(\d{4}-\d{2}-\d{2})-", path.name)
        date = match.group(1) if match else ""
    modified = scalar(data.get("last_modified_at")) or modified_dates.get(path.as_posix(), "")
    description = scalar(data.get("description") or data.get("excerpt"))
    missing_alt = sum(1 for _src, alt in images if alt is None or not alt.strip())
    cluster = classify_cluster(scalar(data.get("title")), tags, content)
    if path.parts[:2] == ("_posts", "twitter"):
        cluster = "non-strategic"
    score = quality_score(data, h1, words, len(internal_targets), len(domains), len(images), missing_alt)
    kind = content_type(path)
    draft = as_bool(data.get("draft")) or kind == "draft"
    noindex = as_bool(data.get("noindex"))
    declared_lang = scalar(data.get("lang"))
    canonical_declared = scalar(data.get("canonical"))
    if canonical_declared.startswith(("http://", "https://")):
        canonical_rendered = canonical_declared
    elif canonical_declared:
        canonical_rendered = f"{SITE_URL}/{canonical_declared.lstrip('/')}"
    else:
        canonical_rendered = f"{SITE_URL}{url}" if url else ""

    return {
        "path": path.as_posix(),
        "url": url,
        "content_type": kind,
        "title": scalar(data.get("title")),
        "h1": h1,
        "seo_title": scalar(data.get("seoTitle")),
        "meta_description": description,
        "date_published": date,
        "date_modified": modified,
        "categories": "|".join(categories),
        "tags": "|".join(tags),
        "lang": declared_lang,
        "draft": str(draft).lower(),
        "noindex": str(noindex).lower(),
        "word_count": words,
        "internal_links": len(internal_targets),
        "external_links": len(domains),
        "inbound_internal_links": 0,
        "links_obeo": sum(domain_matches(domain, ("obeosoft.com", "obeo.fr")) for domain in domains),
        "links_eclipse": sum(domain_matches(domain, ("eclipse.org", "eclipse.dev")) for domain in domains),
        "links_omg": sum(domain_matches(domain, ("omg.org",)) for domain in domains),
        "images": len(images),
        "images_with_alt": len(images) - missing_alt,
        "images_missing_alt": missing_alt,
        "cluster_probable": cluster,
        "intent_probable": classify_intent(scalar(data.get("title")), content),
        "primary_query_probable": scalar(data.get("title")).lower(),
        "quality_score": score,
        "quality_estimated": estimate_quality(score),
        "priority": priority(cluster, score, kind, draft, noindex),
        "recommendation": recommendation(kind, cluster, words, score, draft, noindex, date),
        "translation_en": scalar(data.get("translation_en")),
        "translation_fr": scalar(data.get("translation_fr")),
        "canonical_declared": canonical_declared,
        "canonical": canonical_rendered,
        "front_matter_error": error,
        "_internal_targets": internal_targets,
    }


def url_aliases(url: str) -> set[str]:
    if not url:
        return set()
    aliases = {url}
    if url.endswith("/"):
        aliases.add(f"{url}index.html")
        if url != "/":
            aliases.add(url.rstrip("/"))
    elif url.endswith(".html"):
        aliases.add(url.removesuffix(".html") + "/")
    else:
        aliases.add(f"{url}/")
    return aliases


def add_inbound_counts(rows: list[dict[str, Any]]) -> None:
    lookup: dict[str, int] = {}
    for index, row in enumerate(rows):
        for alias in url_aliases(str(row["url"])):
            lookup[alias] = index
    inbound_sources: list[set[int]] = [set() for _row in rows]
    for source_index, row in enumerate(rows):
        for target in row["_internal_targets"]:
            target_index = lookup.get(target)
            if target_index is not None and target_index != source_index:
                inbound_sources[target_index].add(source_index)
    for index, row in enumerate(rows):
        row["inbound_internal_links"] = len(inbound_sources[index])


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=CSV_FIELDS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def count(rows: list[dict[str, Any]], field: str, value: str) -> int:
    return sum(str(row[field]) == value for row in rows)


def write_summary(path: Path, rows: list[dict[str, Any]]) -> None:
    strategic = [row for row in rows if row["cluster_probable"] != "non-strategic"]
    orphaned = [
        row for row in strategic
        if row["content_type"] in {"post", "page"} and int(row["inbound_internal_links"]) == 0 and row["noindex"] == "false"
    ]
    missing_descriptions = [row for row in rows if not row["meta_description"] and row["noindex"] == "false"]
    body_h1 = [row for row in rows if row["h1"]]
    missing_alt = [row for row in rows if int(row["images_missing_alt"]) > 0]
    malformed = [row for row in rows if row["front_matter_error"]]
    translations_without_lang = [row for row in rows if row["translation_en"] and row["lang"] != "fr"]
    french_canonical_to_english = [
        row for row in rows
        if row["lang"] == "fr"
        and row["translation_en"]
        and urlparse(str(row["canonical"])).path.rstrip("/")
        == str(row["translation_en"]).rstrip("/")
    ]

    duplicate_urls: dict[str, list[str]] = {}
    duplicate_titles: dict[str, list[str]] = {}
    for row in rows:
        if row["url"]:
            duplicate_urls.setdefault(str(row["url"]), []).append(str(row["path"]))
        if row["title"]:
            duplicate_titles.setdefault(str(row["title"]).casefold(), []).append(str(row["path"]))
    duplicate_urls = {url: paths for url, paths in duplicate_urls.items() if len(paths) > 1}
    duplicate_titles = {title: paths for title, paths in duplicate_titles.items() if len(paths) > 1}

    known_url_rows = {
        alias: row
        for row in rows
        for alias in url_aliases(str(row["url"]))
    }
    known_urls = set(known_url_rows)
    unresolved_translations: list[tuple[str, str, str]] = []
    asymmetric_translations: list[tuple[str, str, str, str]] = []
    for row in rows:
        for field in ("translation_en", "translation_fr"):
            target = str(row[field])
            if target and not url_aliases(target).intersection(known_urls):
                unresolved_translations.append((str(row["path"]), field, target))
            elif target:
                matching_alias = next(iter(url_aliases(target).intersection(known_urls)))
                target_row = known_url_rows[matching_alias]
                reciprocal_field = "translation_fr" if field == "translation_en" else "translation_en"
                reciprocal = str(target_row[reciprocal_field])
                if not url_aliases(reciprocal).intersection(url_aliases(str(row["url"]))):
                    asymmetric_translations.append(
                        (str(row["path"]), field, target, reciprocal)
                    )

    lines = [
        "# Content audit summary",
        "",
        "> Generated by `python3.13 scripts/audit_content_inventory.py`. Editorial classifications are review aids, not publishing decisions.",
        "",
        "## Scope",
        "",
        f"- Jekyll source documents with front matter: **{len(rows)}**",
        f"- Posts: **{count(rows, 'content_type', 'post')}**",
        f"- Pages: **{count(rows, 'content_type', 'page')}**",
        f"- Tags and categories: **{count(rows, 'content_type', 'tag') + count(rows, 'content_type', 'category')}**",
        f"- Drafts: **{count(rows, 'draft', 'true')}**",
        f"- Pages marked `noindex`: **{count(rows, 'noindex', 'true')}**",
        "",
        "## Strategic clusters (heuristic)",
        "",
    ]
    for cluster in ["sysml-v2", "syson", "modeling-platforms", "open-source-industrial", "capella-arcadia", "non-strategic"]:
        lines.append(f"- `{cluster}`: **{count(rows, 'cluster_probable', cluster)}**")
    lines.extend(
        [
            "",
            "## Main findings",
            "",
            f"- Missing meta description or excerpt: **{len(missing_descriptions)}**",
            f"- Body-level H1 conflicting with the layout H1: **{len(body_h1)}**",
            f"- Documents with images missing alt text: **{len(missing_alt)}**",
            f"- Strategic pages with no inbound editorial link: **{len(orphaned)}**",
            f"- Duplicate derived URLs: **{len(duplicate_urls)}**",
            f"- Duplicate exact titles: **{len(duplicate_titles)}**",
            f"- Malformed front matter documents: **{len(malformed)}**",
            f"- Translations with `translation_en` but without `lang: fr`: **{len(translations_without_lang)}**",
            f"- French translations canonicalized to English by the current theme: **{len(french_canonical_to_english)}**",
            f"- Translation targets not resolved to an inventoried URL: **{len(unresolved_translations)}**",
            f"- Asymmetric translation pairs: **{len(asymmetric_translations)}**",
            "",
            "## High-priority review queue",
            "",
            "| Page | Cluster | Words | Score | Inbound | Recommendation |",
            "|---|---:|---:|---:|---:|---|",
        ]
    )
    high_priority = sorted(
        (row for row in rows if row["priority"] == "high"),
        key=lambda row: (int(row["quality_score"]), -int(row["word_count"])),
    )[:40]
    for row in high_priority:
        title = str(row["title"]).replace("|", "\\|") or str(row["path"])
        lines.append(
            f"| [{title}]({row['url']}) | `{row['cluster_probable']}` | {row['word_count']} | "
            f"{row['quality_score']} | {row['inbound_internal_links']} | `{row['recommendation']}` |"
        )
    lines.extend(["", "## Duplicate URLs", ""])
    if duplicate_urls:
        for url, paths in sorted(duplicate_urls.items()):
            lines.append(f"- `{url}`: {', '.join(f'`{item}`' for item in paths)}")
    else:
        lines.append("No duplicate derived URLs detected.")
    lines.extend(["", "## Duplicate titles", ""])
    if duplicate_titles:
        for title, paths in sorted(duplicate_titles.items()):
            lines.append(f"- `{title}`: {', '.join(f'`{item}`' for item in paths)}")
    else:
        lines.append("No duplicate exact titles detected.")
    lines.extend(["", "## Unresolved translation targets", ""])
    if unresolved_translations:
        for source, field, target in unresolved_translations:
            lines.append(f"- `{source}`: `{field}: {target}`")
    else:
        lines.append("All translation targets resolve to an inventoried URL.")
    lines.extend(["", "## Asymmetric translation pairs", ""])
    if asymmetric_translations:
        for source, field, target, reciprocal in asymmetric_translations:
            lines.append(
                f"- `{source}`: `{field}: {target}` but reciprocal target is `{reciprocal or '(missing)'}`"
            )
    else:
        lines.append("All translation relationships are symmetric.")
    lines.extend(["", "## Front matter errors", ""])
    if malformed:
        for row in malformed:
            lines.append(f"- `{row['path']}`: {row['front_matter_error']}")
    else:
        lines.append("No malformed front matter detected.")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."), help="Repository root")
    parser.add_argument("--csv", type=Path, default=Path("audit/content-inventory.csv"), help="CSV output path")
    parser.add_argument(
        "--summary", type=Path, default=Path("audit/content-audit-summary.md"), help="Markdown summary output path"
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    documents = find_documents(root)
    modified_dates = git_modified_dates(root)
    rows = [read_document(root, path, modified_dates) for path in documents]
    add_inbound_counts(rows)
    write_csv(root / args.csv, rows)
    write_summary(root / args.summary, rows)
    print(f"Audited {len(rows)} documents")
    print(f"CSV: {args.csv}")
    print(f"Summary: {args.summary}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
