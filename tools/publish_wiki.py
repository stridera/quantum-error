#!/usr/bin/env python3
"""Publish mapped Markdown files to MediaWiki."""
from __future__ import annotations

import os
import sys
import subprocess
import yaml
import requests

from md_to_mediawiki import convert_markdown


def get_git_sha() -> str:
    try:
        sha = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], text=True).strip()
    except Exception:
        sha = "unknown"
    return sha


def get_edit_token(session: requests.Session, api_url: str) -> str:
    params = {
        "action": "query",
        "meta": "tokens",
        "type": "csrf",
        "format": "json",
    }
    data = session.get(api_url, params=params).json()
    return data["query"]["tokens"]["csrftoken"]


def login(session: requests.Session, api_url: str, username: str, password: str) -> None:
    token_params = {
        "action": "query",
        "meta": "tokens",
        "type": "login",
        "format": "json",
    }
    token_data = session.get(api_url, params=token_params).json()
    login_token = token_data["query"]["tokens"]["logintoken"]

    login_params = {
        "action": "login",
        "lgname": username,
        "lgpassword": password,
        "lgtoken": login_token,
        "format": "json",
    }
    session.post(api_url, data=login_params).raise_for_status()


def main() -> int:
    api_url = os.getenv("MW_API_URL")
    username = os.getenv("MW_BOT_USERNAME")
    password = os.getenv("MW_BOT_PASSWORD")
    user_agent = os.getenv("MW_USER_AGENT", "QuantumErrorBot/0.1")

    if not api_url or not username or not password:
        print("Missing MW_API_URL / MW_BOT_USERNAME / MW_BOT_PASSWORD", file=sys.stderr)
        return 1

    with open("wiki/mapping.yml", "r", encoding="utf-8") as f:
        mapping = yaml.safe_load(f)

    pages = mapping.get("pages", [])
    if not pages:
        print("No pages found in wiki/mapping.yml", file=sys.stderr)
        return 1

    sha = get_git_sha()

    session = requests.Session()
    session.headers.update({"User-Agent": user_agent})

    login(session, api_url, username, password)
    token = get_edit_token(session, api_url)

    for page in pages:
        file_path = page["file"]
        title = page["title"]
        categories = page.get("categories", [])

        with open(file_path, "r", encoding="utf-8") as f:
            md = f.read()

        mw = convert_markdown(md)
        if categories:
            mw += "\n" + "\n".join([f"[[Category:{c}]]" for c in categories]) + "\n"

        summary = f"Publish from git {sha}: {file_path}"

        edit_params = {
            "action": "edit",
            "title": title,
            "text": mw,
            "summary": summary,
            "token": token,
            "format": "json",
        }
        resp = session.post(api_url, data=edit_params)
        resp.raise_for_status()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
