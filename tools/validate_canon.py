#!/usr/bin/env python3
"""Minimal canon validation: required files + Bobbinry mapping check."""
from __future__ import annotations

import os
import sys
import yaml

REQUIRED = [
    "CANON.md",
    "characters/roster.md",
    "bobbinry.yml",
]


def main() -> int:
    missing = [p for p in REQUIRED if not os.path.exists(p)]
    if missing:
        print("Missing required files:")
        for p in missing:
            print(f"- {p}")
        return 1

    with open("bobbinry.yml", "r", encoding="utf-8") as f:
        mapping = yaml.safe_load(f)

    entries = mapping.get("entities", [])
    bad = [e["file"] for e in entries if not os.path.exists(e["file"])]
    if bad:
        print("Mapping references missing files:")
        for p in bad:
            print(f"- {p}")
        return 1

    ids = [e["id"] for e in entries]
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        print("Duplicate entity ids in mapping:")
        for i in sorted(dupes):
            print(f"- {i}")
        return 1

    print("Canon validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
