---
canon: true
stability: evolving
---

# Style Guide

This repo is designed for humans *and* LLM tooling.

## File rules
- Prefer Markdown (`.md`) in the existing folder structure.
- One concept per file when possible.
- Link to other files using relative links.

## Status tags
At the top of new canon files, include:

> **Status:** DRAFT | LOCKED
> **Last Reviewed:** YYYY-MM-DD

## Mechanics formatting

### Ability / Spell Stat Block (canonical)
Use this template (copy/paste) for any spell/skill/song/smite:

#### <Ability Name>
- **Type:** Spell | Skill | Song | Smite | Passive
- **Source:** Class/Race/Item (link)
- **Level:** #
- **Cost:** X mana (min Y, max Z) / stamina / none
- **Cooldown:** #s / # rounds / none
- **Duration:** Instant / #s / # rounds
- **Targeting:** Self | Ally | Enemy | Area (Room) | Cone (Room) | etc
- **Tags:** (e.g., Illusion, Healing, System, Temporal, Control)
- **Rules:** 3–8 bullet points with hard numbers.
- **Scaling:** What changes at 10/20/50/99 (or per K-band)

### UI "Help Popup"
Abilities should also have a UI popup snippet (see `system/ui-popups.md`) so the story can show in-world tooltips.

## Naming
- Prefer in-world names, but allow "legacy/pop-culture" names if they are common and not trademark-problematic.
- Keep internal IDs snake_case if you add them (e.g., `arcane_bolt`), and display names Title Case.

## Open questions
If something is not decided, add a clearly labeled section:

> **Open Questions:**
> - …

…and add it to `canon/status.md`.
