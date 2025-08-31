#!/usr/bin/env python3
"""
Add specific tags to posts identified by their front-matter title.

Behavior:
- Only modifies files under `_posts/` with YAML front matter.
- Preserves existing tags and order where possible; appends new ones if missing.
- Keeps tags in block list style (`tags:` then `- item`).
- Title matching is flexible: exact match (case-insensitive), then normalized punctuation, then substring contains.

Notes:
- Uses the mapping defined below from title -> list of tags to add.
- Tags are added verbatim with given casing (e.g., `MBSE`, `SysON`).
"""
import os
import re
import unicodedata
from typing import List, Tuple, Dict


TARGETS: Dict[str, List[str]] = {
    # sirius-web group (add sirius-web; plus Company/MBSE where noted)
    "Open Community Experience 2024: Obeo was there!": ["sirius-web", "company", "MBSE"],
    "Advancing Web-Based Modeling Tools with Sirius Web: An Illustration with SysON": ["sirius-web", "MBSE"],
    "How much time do I need to make coffee ?": ["sirius-web"],
    "SVG icons in Sirius Web": ["sirius-web"],
    "(Sirius + Papyrus) × Web: a new Era for Collaborative Engineering tools": ["sirius-web", "MBSE"],
    "What if you could design, simulate and analyze all at once using Open-Source solutions?": ["sirius-web", "MBSE"],
    "Are your engineering tools built on top of strong and well-maintained technologies?": ["sirius-web", "company"],
    "Building Graphical Modeling Tools, Approaches to Reducing Complexity": ["sirius-web"],

    # mbse group
    "Open Community Experience 2024: Obeo was there!": ["MBSE", "sirius-web", "SysON"],
    "(Sirius + Papyrus) × Web: a new Era for Collaborative Engineering tools": ["MBSE", "sirius-web", "SysON"],
    "What if you could design, simulate and analyze all at once using Open-Source solutions?": ["MBSE", "sirius-web", "SysON"],
    "Siemens partnering with Obeo on Model Based Systems Engineering solution – a major recognition for OSS Modeling Techs": ["MBSE", "company", "capella"],
    "SysML Comparison and Contributions": ["MBSE"],

    # ecore group
    "Do you know Ecore? Looking for a reference card?": ["ecore"],
    "Ecore.ecore using EcoreTools": ["ecore"],
    "Metamodel (Ecore) Design Checklist": ["ecore"],
    "Metamodel (Ecore) Design Checklist – part 1": ["ecore"],
    "Metamodel (Ecore) Design Checklist – part 2": ["ecore"],
    "Executing, Debugging and Animating your model": ["ecore"],
    "AQL – a new interpreter for Sirius": ["ecore"],
    "Eclipse Sirius and Obeo Designer": ["ecore", "company"],
    "Sirius 3.0M6 – Anchors for Non-rectangular Images": ["ecore"],
    "EcoreTools 2.0 – The Luna Revival": ["ecore"],
    "Eclipse Modeling Package – The Road to Luna": ["ecore", "company"],
    "Introducing Eclipse Sirius": ["ecore", "company"],
    "EMF Core does not change, but ..": ["ecore"],
    "Graphical, textual, table, trees, its your call, to us its just EMF models": ["ecore"],
    "Do you want to discard this editor's changes ?": ["ecore"],
    "Model Transformation Preview": ["ecore"],
    "Model Comparison: Logical Model, UML, Papyrus, EcoreTools and GMF Integration": ["ecore"],
    "Sequence Diagrams for your DSL’s": ["ecore"],
    "Model Comparison: Patching with MPatch": ["ecore"],
    "Compare/Helios – Every Second Counts": ["ecore"],
    "Diff, Merge and Patch your Models with Helios": ["ecore"],
    "Modeling Project Runaway: ATL": ["ecore"],
    "Ecore In Colors (In Motion)": ["ecore"],
    "Viewpoints-enabled Modeling Tools": ["ecore"],
    "The 20 minute Graphical Modeler based on Eclipse": ["ecore"],
    "Live Models Using JBoss Rules (Drools) and EMF": ["ecore"],
    "EMF Compare now uses XMI_ID": ["ecore"],
    "XML files comparison/merge": ["ecore"],
    "“Simplicity is the ultimate sophistication”": ["ecore"],

    # capella group
    "The Rising Adoption of Capella": ["capella"],
    "Siemens partnering with Obeo on Model Based Systems Engineering solution – a major recognition for OSS Modeling Techs": ["capella", "MBSE", "company"],

    # obeo group
    "Open Community Experience 2024: Obeo was there!": ["obeo", "sirius-web", "SysON", "MBSE"],
    "Wondering what kind of impact a company like Obeo has on Research?": ["obeo"],
    "Interview by Strumenta": ["obeo"],
    "Obeo’s Chronicles, Autumn 2020": ["obeo"],
    "Let’s Do It! Obeo loves The SeaCleaners": ["obeo"],
    "SiriusCon 2018 is SiriusCon Live!": ["obeo"],
    "⦏Breaking News Eclipse Sirius⦎ SiriusCon 2017!": ["obeo"],
    "North America, here we come!": ["obeo"],
    "You only have a few more hours to submit to EclipseCon Europe!": ["obeo"],
    "Graphical Modeling from 2016 to 2017: Better, Faster, Stronger": ["obeo"],
    "⦏Breaking News Eclipse Sirius⦎ SiriusCon 2016 is coming!": ["obeo"],
    "Psst, psst, you might want to submit right now for EclipseCon Europe!": ["obeo"],
    "Eclipse Modeling Package Neon M6 is ready for testing": ["obeo"],
    "Modeling Avengers: OSS Technology Mix for Saving the World": ["obeo", "ecore", "emf"],
    "EclipseCon Europe 2015 is over but SiriusCon is coming!": ["obeo"],
    "What makes EclipseCon Europe a good conference ?": ["obeo"],
    "Eclipse @Devoxx": ["obeo"],
    "Eclipse Modeling Package – The Road to Luna": ["obeo", "ecore", "emf"],
    "Will you be Sirius at EclipseCon Europe ?": ["obeo"],
    "Introducing Eclipse Sirius": ["obeo", "ecore", "emf"],
    "Learning from the source": ["obeo"],
    "EclipseCon Europe – Time to hurry up !": ["obeo"],
    "Eclipse DemoCamp Nantes – Live Broadcast": ["obeo"],
    "Upcoming Events": ["obeo"],
    "Preparing EclipseCon US 2012": ["obeo"],
    "Eclipse Day Paris 2011": ["obeo"],
    "Community and Ecosystem": ["obeo"],
    "Follow the White Rabbit … at Eclipse Day Paris!": ["obeo"],
    "Obeo @ Eclipse Con Europe": ["obeo"],
    "Autumn is a second spring when every leaf is a flower": ["obeo"],
    "Eclipse Helios – a whole year of goodness": ["obeo"],
    "3 Good Reasons to use the Helios Modeling Package": ["obeo"],
    "Forecasts Comparison For The World !": ["obeo"],
    "Eclipse Modeling Survey results": ["obeo"],
    "Eclipse Modeling Package Survey": ["obeo"],
    "I’m a poor, lonesome cowboy ..": ["obeo"],
    "Eclipse Amalgamation 2.0": ["obeo"],
    "Its time already !": ["obeo"],
    "Unusual Propulsion System": ["obeo"],
    "Eclipse Summit: here we come !": ["obeo"],
    "Exploring Eclipse Plugins: beyond Terra Incognita": ["obeo"],
    "Having more control ...": ["obeo"],
    "The 09/09/09 09:09 0.9.0 Release": ["obeo", "ecore", "emf"],
    "Let’s take a step back ...": ["obeo"],
    "Feedback from IT companies leveraging Acceleo": ["obeo", "ecore", "emf"],
    "Eclipse Acceleo Day is going on...": ["obeo", "ecore", "emf"],
    "Galileo Modeling Package is Here": ["obeo"],
    "Quick glimpse at Galileo Modeling Package": ["obeo"],
    "Eclipse Modeling Summer of Code 2009": ["obeo"],
    "ShuangXi effect: UI testing and documentation": ["obeo"],
    "Engineering dictator strikes back: querying your team repository": ["obeo"],
    "2008 was full of excitement, let’s make an even better 2009 !": ["obeo"],
    "Back from ESE 2008: WOW !": ["obeo"],
    "How much computer scientists do you need...": ["obeo"],
    "“Babies are such a nice way to start people”": ["obeo"],
    "Amazing forest": ["obeo"],
    "Chocolate commit": ["obeo"],
    "Modeling at ESE 2007": ["obeo"],
    "“I love deadlines…”": ["obeo"],
    "New licenses for QT: any progress on Eclipse ?": ["obeo"],
    "Beautiful Evidence": ["obeo"],
    "Joining the community": ["obeo"],
}


def read_posts() -> List[Tuple[str, str]]:
    posts = []
    for dirpath, _, fns in os.walk("_posts"):
        for fn in fns:
            if not (fn.endswith(".md") or fn.endswith(".html")):
                continue
            p = os.path.join(dirpath, fn)
            try:
                t = open(p, encoding="utf-8", errors="ignore").read()
            except Exception:
                continue
            m = re.search(r"^title:\s*\"?(.+?)\"?\s*$", t, re.M)
            if m:
                title = m.group(1).strip()
                posts.append((title, p))
    return posts


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("—", "-").replace("–", "-")
    s = s.replace("“", '"').replace("”", '"').replace("’", "'")
    return s.lower()


def split_front_matter(text: str):
    lines = text.splitlines()
    if not lines or not lines[0].strip().startswith("---"):
        return [], [], lines
    end = None
    for i in range(1, min(600, len(lines))):
        if lines[i].strip().startswith("---"):
            end = i
            break
    if end is None:
        return [], [], lines
    return lines[:1], lines[1:end], lines[end+1:]


def parse_tags_from_fm(fm: List[str]) -> Tuple[List[str], Tuple[int, int]]:
    # returns (tags_list, (start_index, end_index_exclusive)) if a block exists
    start = None
    for i, line in enumerate(fm):
        if re.match(r"^\s*tags\s*:\s*$", line):
            start = i
            break
        if re.match(r"^\s*tags\s*:\s*\[(.*)\]\s*$", line):
            # inline list -> treat as no block; handled elsewhere
            break
    if start is None:
        return [], (-1, -1)
    items = []
    j = start + 1
    while j < len(fm):
        l = fm[j]
        m = re.match(r"^\s*-\s*(.+?)\s*$", l)
        if m:
            items.append(m.group(1).strip())
            j += 1
            continue
        if l.strip() == "" or l.startswith(" "):
            j += 1
            continue
        break
    return items, (start, j)


def ensure_block_list_tags(fm: List[str]) -> Tuple[List[str], List[str]]:
    # Returns (new_fm, current_tags)
    # Detect inline or scalar and convert
    out = []
    i = 0
    current_tags: List[str] = []
    changed = False
    while i < len(fm):
        line = fm[i]
        m_inline = re.match(r"^(?P<indent>\s*)tags\s*:\s*\[(?P<inner>.*)\]\s*$", line)
        m_scalar = None
        if not m_inline:
            m_scalar = re.match(r"^(?P<indent>\s*)tags\s*:\s*(?P<value>(?!\[).+?)\s*$", line)
        if m_inline:
            indent = m_inline.group("indent")
            inner = m_inline.group("inner")
            items = [p.strip() for p in inner.split(",") if p.strip()]
            tags = []
            for it in items:
                if (it.startswith('"') and it.endswith('"')) or (it.startswith("'") and it.endswith("'")):
                    it = it[1:-1].strip()
                if it:
                    tags.append(it)
            out.append(f"{indent}tags:")
            for t in tags:
                out.append(f"{indent}  - {t}")
            current_tags = tags[:]
            changed = True
            i += 1
            continue
        elif m_scalar:
            indent = m_scalar.group("indent")
            value = m_scalar.group("value").strip()
            if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
                value = value[1:-1].strip()
            out.append(f"{indent}tags:")
            if value:
                out.append(f"{indent}  - {value}")
                current_tags = [value]
            changed = True
            i += 1
            continue
        else:
            out.append(line)
            i += 1
    if not changed:
        # Already block style; collect existing tags
        tags, _rng = parse_tags_from_fm(fm)
        current_tags = tags
        return fm, current_tags
    return out, current_tags


def add_tags_to_post(path: str, add_tags: List[str]) -> bool:
    txt = open(path, encoding="utf-8", errors="ignore").read()
    pre, fm, body = split_front_matter(txt)
    if not fm:
        return False
    new_fm, existing = ensure_block_list_tags(fm)
    # Insert new tags (preserving existing case), avoid duplicates by case-insensitive compare
    existing_lower = {t.lower(): t for t in existing}
    final = list(existing)
    # find insertion index after 'tags:' header
    # Find start index of block
    start_idx = None
    for idx, line in enumerate(new_fm):
        if re.match(r"^\s*tags\s*:\s*$", line):
            start_idx = idx
            break
    for t in add_tags:
        if t.lower() not in existing_lower:
            # append new item at the end of the block
            if start_idx is not None:
                # determine indent from next tag item or default two spaces
                indent = "  "
                if start_idx + 1 < len(new_fm):
                    m = re.match(r"^(\s*)-\s*", new_fm[start_idx + 1])
                    if m:
                        indent = m.group(1)
                    else:
                        m = re.match(r"^(\s*)", new_fm[start_idx + 1])
                        indent = (m.group(1) if m else "  ")
                insert_at = start_idx + 1
                # find end of block
                j = insert_at
                while j < len(new_fm) and re.match(r"^\s*-\s*", new_fm[j]):
                    j += 1
                new_fm.insert(j, f"{indent}- {t}")
                existing_lower[t.lower()] = t
                final.append(t)
    new_text = "\n".join(pre + new_fm + ["---"] + body)
    if new_text != txt:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_text)
        return True
    return False


def main() -> None:
    posts = read_posts()
    # Build lookup structures
    by_lower = {norm(t): p for t, p in posts}
    changed = []
    for title, tags in TARGETS.items():
        tgt = by_lower.get(norm(title))
        if not tgt:
            # second pass: contains
            for t, p in posts:
                if norm(title) in norm(t):
                    tgt = p
                    break
        if not tgt:
            # Not found; skip silently (old HTML or archive titles)
            continue
        if add_tags_to_post(tgt, tags):
            changed.append((title, tgt, tags))
    print(f"Updated {len(changed)} posts with additional tags")
    for t, p, tags in changed[:50]:
        print(f" - {t} => {p} (+{', '.join(tags)})")
    if len(changed) > 50:
        print(f" ... and {len(changed)-50} more")


if __name__ == "__main__":
    main()

