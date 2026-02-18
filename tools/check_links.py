#!/usr/bin/env python3
"""Check for unlinked cross-references in canon Markdown files.

Builds a term dictionary from wiki/mapping.yml titles and CANON.md file
headings, then scans all Markdown files for mentions that aren't wrapped
in a Markdown link.  Reports the first unlinked mention per term per file.

Skips terms that are already linked at least once in the same file
(convention: link on first mention, don't repeat).

Advisory only -- exits 0 even when issues are found.
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

# ── configuration ────────────────────────────────────────────────────
MIN_TERM_LENGTH = 4

# Terms that are too generic or structural to auto-link.
SKIP_TERMS: set[str] = {
    "Quantum Error",
    "Quantum Error/Lore",
    "Quantum Error/System",
    "Quantum Error/Stats",
    "Quantum Error/Stat Progression",
    "Quantum Error/Mob Framework",
    "Equipment Framework",
    "Locations",
    "Magic",
}

# Directories to skip when scanning.
SKIP_DIRS: set[str] = {"tools", "wiki", "images", "_layouts", "_site", "canon"}

# Files to skip (relative to repo root).
SKIP_FILES: set[str] = {"CANON.md"}

# Lines matching these patterns are stat labels, not concept references.
STAT_LABEL_RE = re.compile(
    r"^\s*[-|]\s*(Mana|Hit Points|Endurance|Stamina|Health)\s*[:|-]",
    re.IGNORECASE,
)


# ── helpers ──────────────────────────────────────────────────────────
def _strip_links(line: str) -> str:
    """Remove Markdown link text and image alt text so we don't double-count."""
    line = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", line)   # images
    line = re.sub(r"\[[^\]]*\]\([^)]*\)", "", line)     # links
    return line


def _extract_linked_terms(content: str, terms_sorted: list[tuple[str, str]]) -> set[str]:
    """Return the set of terms that appear inside at least one Markdown link."""
    linked: set[str] = set()
    # Find all link texts: [link text](url)
    link_texts = re.findall(r"\[([^\]]*)\]\([^)]*\)", content)
    all_link_text = " ".join(link_texts)
    for term, _ in terms_sorted:
        pattern = re.compile(r"(?<!\w)" + re.escape(term) + r"(?!\w)")
        if pattern.search(all_link_text):
            linked.add(term)
    return linked


def load_terms() -> dict[str, str]:
    """Return {display_name: canon_file_path} from mapping + headings."""
    import yaml

    terms: dict[str, str] = {}

    # 1) wiki/mapping.yml titles
    if os.path.exists("wiki/mapping.yml"):
        with open("wiki/mapping.yml", "r", encoding="utf-8") as f:
            mapping = yaml.safe_load(f)
        for page in mapping.get("pages", []):
            title = page.get("title", "")
            fpath = page.get("file", "")
            if title and fpath and title not in SKIP_TERMS and len(title) >= MIN_TERM_LENGTH:
                terms[title] = fpath

    # 2) H1 headings from every file listed in CANON.md
    canon_files: list[str] = []
    if os.path.exists("CANON.md"):
        with open("CANON.md", "r", encoding="utf-8") as f:
            for line in f:
                m = re.match(r"^- `(.+\.md)`", line.strip())
                if m:
                    canon_files.append(m.group(1))

    for cf in canon_files:
        if not os.path.exists(cf):
            continue
        in_fm = False
        with open(cf, "r", encoding="utf-8") as f:
            for line in f:
                stripped = line.strip()
                if stripped == "---":
                    in_fm = not in_fm
                    continue
                if in_fm:
                    continue
                m = re.match(r"^#\s+(.+)$", stripped)
                if m:
                    heading = m.group(1).strip()
                    if heading not in SKIP_TERMS and len(heading) >= MIN_TERM_LENGTH:
                        terms.setdefault(heading, cf)
                    break  # only the first H1

    return terms


def _build_subsume_map(terms_sorted: list[tuple[str, str]]) -> dict[str, str]:
    """Map short terms to longer terms that point to the same target.

    e.g. "Paladin" -> "Paladin of the System" (both map to paladin-of-the-system.md).
    When the longer form is already linked/seen, the short form is skipped.
    """
    subsume: dict[str, str] = {}
    for i, (short_term, short_target) in enumerate(terms_sorted):
        for long_term, long_target in terms_sorted[:i]:
            if (
                os.path.normpath(short_target) == os.path.normpath(long_target)
                and short_term.lower() in long_term.lower()
                and short_term != long_term
            ):
                subsume[short_term] = long_term
                break
    return subsume


def find_unlinked(
    filepath: str,
    terms_sorted: list[tuple[str, str]],
    subsume: dict[str, str],
) -> list[tuple[int, str, str]]:
    """Return [(line_number, term, target_file)] for first unlinked mention per term."""
    results: list[tuple[int, str, str]] = []

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Terms already linked at least once in this file — skip entirely.
    already_linked = _extract_linked_terms(content, terms_sorted)

    # Track which terms (and their longer parents) we've seen.
    seen: set[str] = set()

    lines = content.split("\n")
    in_fm = False
    in_code = False

    for line_num, line in enumerate(lines, 1):
        stripped = line.strip()

        if stripped == "---":
            in_fm = not in_fm
            continue
        if in_fm:
            continue
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if stripped.startswith("#"):
            continue
        if STAT_LABEL_RE.match(stripped):
            continue

        cleaned = _strip_links(line)

        for term, target in terms_sorted:
            if term in seen:
                continue
            if term in already_linked:
                seen.add(term)
                continue
            if os.path.normpath(filepath) == os.path.normpath(target):
                continue

            # If this is a short form and the long form is already linked/seen, skip.
            long_form = subsume.get(term)
            if long_form and (long_form in already_linked or long_form in seen):
                seen.add(term)
                continue

            pattern = re.compile(r"(?<!\w)" + re.escape(term) + r"(?!\w)")
            if pattern.search(cleaned):
                results.append((line_num, term, target))
                seen.add(term)

    return results


# ── main ─────────────────────────────────────────────────────────────
def main() -> int:
    terms = load_terms()
    if not terms:
        print("No terms found. Ensure CANON.md and wiki/mapping.yml exist.")
        return 1

    # Sort longest-first so "Paladin of the System" matches before "Paladin".
    terms_sorted = sorted(terms.items(), key=lambda t: len(t[0]), reverse=True)
    subsume = _build_subsume_map(terms_sorted)

    # Collect markdown files.
    md_files: list[str] = []
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d not in SKIP_DIRS]
        for f in files:
            rel = os.path.relpath(os.path.join(root, f), ".")
            if f.endswith(".md") and rel not in SKIP_FILES:
                md_files.append(os.path.join(root, f))

    total = 0
    for md_file in sorted(md_files):
        issues = find_unlinked(md_file, terms_sorted, subsume)
        for line_num, term, target in issues:
            from_dir = os.path.dirname(os.path.abspath(md_file))
            rel_path = os.path.relpath(os.path.abspath(target), from_dir)
            print(f"  {md_file}:{line_num}: \"{term}\" -> [{term}]({rel_path})")
            total += 1

    if total == 0:
        print("Cross-reference check passed. No unlinked mentions found.")
    else:
        print(f"\n{total} unlinked mention(s) found.")

    return 0  # advisory


if __name__ == "__main__":
    raise SystemExit(main())
