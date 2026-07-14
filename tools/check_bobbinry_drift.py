#!/usr/bin/env python3
"""Report drift between canon Markdown and Bobbinry entities.

Read-only — never pushes. For each entry in bobbinry.yml, compares the file's
last git commit time against the entity's updated_at:

  CANON NEWER   file committed after the entity's last update → push candidate.
  entity newer  normal steady state after a push; only worth a look if nobody
                pushed recently (could be a platform-side hotfix to promote).

Also flags mapped entities missing remotely, remote entities missing from the
mapping, and mapped files with uncommitted local changes.

Auth: BOBBINRY_API_KEY env var, else apiKey from ~/.config/bobbinry/config.json.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import urllib.request
from datetime import datetime, timezone

import yaml

CONFIG_PATH = os.path.expanduser("~/.config/bobbinry/config.json")


def api_key() -> str:
    key = os.environ.get("BOBBINRY_API_KEY")
    if key:
        return key
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            key = json.load(f).get("apiKey")
    except (OSError, json.JSONDecodeError):
        key = None
    if not key:
        sys.exit(f"No API key: set BOBBINRY_API_KEY or apiKey in {CONFIG_PATH}")
    return key


def fetch_json(url: str, key: str):
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {key}"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def fetch_collection(api_url: str, project_id: str, collection: str, key: str) -> dict:
    url = f"{api_url}/api/collections/{collection}/entities?projectId={project_id}&limit=1000"
    data = fetch_json(url, key)
    if isinstance(data, dict):
        data = data.get("entities") or data.get("data") or []
    return {e["id"]: e for e in data}


def parse_ts(value: str | None) -> datetime | None:
    if not value:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def git_commit_time(path: str) -> datetime | None:
    out = subprocess.run(
        ["git", "log", "-1", "--format=%cI", "--", path],
        capture_output=True, text=True,
    ).stdout.strip()
    return parse_ts(out or None)


def git_dirty(path: str) -> bool:
    out = subprocess.run(
        ["git", "status", "--porcelain", "--", path],
        capture_output=True, text=True,
    ).stdout.strip()
    return bool(out)


def main() -> int:
    with open("bobbinry.yml", "r", encoding="utf-8") as f:
        mapping = yaml.safe_load(f)

    key = api_key()
    api_url = mapping["api_url"]
    project_id = mapping["project_id"]
    entries = mapping.get("entities", [])
    known_ids = {e["id"] for e in entries} | {
        e["id"] for e in mapping.get("unmapped_entities", [])
    }

    remote: dict[str, dict] = {}
    for collection in sorted({e["collection"] for e in entries}):
        remote.update(fetch_collection(api_url, project_id, collection, key))

    push_candidates, entity_newer, missing, dirty = [], [], [], []
    for e in entries:
        ent = remote.get(e["id"])
        if ent is None:
            missing.append(e)
            continue
        if git_dirty(e["file"]):
            dirty.append(e)
        file_time = git_commit_time(e["file"])
        ent_time = parse_ts(ent.get("updated_at") or ent.get("updatedAt"))
        if file_time and ent_time:
            if file_time > ent_time:
                push_candidates.append((e, file_time, ent_time))
            else:
                entity_newer.append((e, file_time, ent_time))

    orphans = [ent for eid, ent in remote.items() if eid not in known_ids]

    def show(label, rows):
        if rows:
            print(f"\n{label}:")
            for r in rows:
                print(f"  - {r}")

    if push_candidates:
        print("CANON NEWER — push candidates (spoiler-gate before pushing):")
        for e, ft, et in push_candidates:
            print(f"  - {e['name']:<32} {e['file']}")
            ft, et = ft.astimezone(timezone.utc), et.astimezone(timezone.utc)
            print(f"      file committed {ft:%Y-%m-%d %H:%M}, entity updated {et:%Y-%m-%d %H:%M} (UTC)")
    else:
        print("No push candidates — no mapped file is newer than its entity.")

    show("Mapped entities MISSING remotely", [f"{e['name']} ({e['id']})" for e in missing])
    show("Remote entities not in mapping", [f"{ent.get('name') or ent.get('title', '?')} ({eid})"
                                            for eid, ent in remote.items() if eid not in known_ids])
    show("Mapped files with uncommitted changes", [f"{e['file']} ({e['name']})" for e in dirty])
    print(f"\n{len(entries)} mapped, {len(remote)} remote, "
          f"{len(push_candidates)} push candidates, {len(missing)} missing, {len(orphans)} unmapped remote.")
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
