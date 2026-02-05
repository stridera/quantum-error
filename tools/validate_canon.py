#!/usr/bin/env python3
"""Minimal canon validation: required files + mapping check."""
from __future__ import annotations

import os
import sys
import yaml

REQUIRED = [
    "CANON.md",
    "characters/roster.md",
    "wiki/mapping.yml",
]


def main() -> int:
    missing = [p for p in REQUIRED if not os.path.exists(p)]
    if missing:
        print("Missing required files:")
        for p in missing:
            print(f"- {p}")
        return 1

    with open("wiki/mapping.yml", "r", encoding="utf-8") as f:
        mapping = yaml.safe_load(f)

    pages = mapping.get("pages", [])
    bad = [p["file"] for p in pages if not os.path.exists(p["file"])]
    if bad:
        print("Mapping references missing files:")
        for p in bad:
            print(f"- {p}")
        return 1

    print("Canon validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
