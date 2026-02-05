#!/usr/bin/env python3
"""Minimal Markdown to MediaWiki converter."""
from __future__ import annotations

import re
from typing import List


def convert_markdown(md: str) -> str:
    lines = md.splitlines()
    out: List[str] = []
    in_code = False
    code_lang = ""

    for line in lines:
        if line.strip().startswith("```"):
            if not in_code:
                code_lang = line.strip().lstrip("`").strip() or "text"
                out.append(f"<syntaxhighlight lang=\"{code_lang}\">")
                in_code = True
            else:
                out.append("</syntaxhighlight>")
                in_code = False
            continue

        if in_code:
            out.append(line)
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            equals = "=" * level
            out.append(f"{equals} {title} {equals}")
            continue

        # Convert markdown links to MediaWiki style.
        def link_repl(match: re.Match) -> str:
            text = match.group(1)
            url = match.group(2)
            return f"[{url} {text}]"

        line = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link_repl, line)
        out.append(line)

    return "\n".join(out) + "\n"
