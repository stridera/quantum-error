---
canon: true
stability: evolving
---

# UI Popups

This document defines the canonical formatting for in-world **System UI** messages as seen by characters.
These conventions are used by:
- Class pages (new abilities)
- Spell/skill pages (help/inspect)
- [Effects](effects.md) (buff/debuff identify)
- [Combat](combat.md) logs (resolution snippets)

## Principles

- **Concise first line**, details below.
- **Hard numbers whenever possible** (cost, duration, cooldown, magnitude).
- **Room-based assumptions** unless a spell explicitly breaks them.
- Use consistent labels and ordering so the UI feels "system-generated."

## Popup Types

### 1) New Ability Earned

Use when a character gains a new skill/spell/song/smite.

```text
╔══════════════════════════════════════════════╗
║ NEW ABILITY UNLOCKED                         ║
╠══════════════════════════════════════════════╣
║ Name:        <Ability Name>                  ║
║ Type:        <Spell/Skill/Song/Passive>      ║
║ Cost:        <Mana/Stamina/None>             ║
║ Cooldown:    <e.g., 12s / 3 turns / None>    ║
║ Duration:    <e.g., 8s / Instant>            ║
║ Targeting:   <Self / Ally / Enemy / Room>    ║
╟──────────────────────────────────────────────╢
║ Summary:     <1–2 lines, player-facing>      ║
╟──────────────────────────────────────────────╢
║ Mechanics:                                   ║
║ - <bullet>                                   ║
║ - <bullet>                                   ║
║ - <bullet>                                   ║
╚══════════════════════════════════════════════╝
```

### 2) Help / Inspect Ability

Use when the player selects **Help** on an ability.

```text
┌──────────────────────────────────────────────┐
│ HELP: <Ability Name>                         │
├──────────────────────────────────────────────┤
│ Type: <Spell/Skill/Song/Passive>             │
│ Cost: <X mana>                               │
│ Cooldown: <Y>                                │
│ Duration: <Z>                                │
│ Targeting: <...>                             │
│ Tags: <Damage / Heal / CC / Utility / ...>   │
├──────────────────────────────────────────────┤
│ Description:                                 │
│ <2–4 lines of prose>                         │
├──────────────────────────────────────────────┤
│ Mechanics:                                   │
│ - Range/Area: <Room-based / Adjacent rooms?> │
│ - Roll: <Accuracy vs Evasion / None>         │
│ - Magnitude: <numbers + scaling rules>       │
│ - Secondary: <status effects>                │
│ - Limits: <immunities/locks/requirements>    │
└──────────────────────────────────────────────┘
```

### 3) Identify Effect (Buff/Debuff)

Use when the character identifies a status effect applied to an entity.

```text
┌──────────────────────────────────────────────┐
│ STATUS: <Effect Name>                         │
├──────────────────────────────────────────────┤
│ Type: <Buff/Debuff/Condition>                │
│ Source: <Caster / Item / Environment>        │
│ Duration: <Remaining / Total / Permanent>    │
│ Stacks: <0/1/N + stacking rule>              │
│ Dispel: <Yes/No; Dispel Tier if used>        │
├──────────────────────────────────────────────┤
│ Summary: <1 line>                            │
├──────────────────────────────────────────────┤
│ Numbers:                                     │
│ - <e.g., -25% Accuracy>                      │
│ - <e.g., Ignores Ally Calls>                 │
│ - <e.g., Break: Eye Contact / Damage / ...>  │
└──────────────────────────────────────────────┘
```

### 4) Combat Resolution Snippet

Use for a single resolved action in combat logs.

```text
<Actor> uses <Ability> on <Target>.
Hit: <Yes/No>  (Roll: <Accuracy> vs <Evasion>)
Damage: <amount> <type>  (Mitigation: <amount/percent>)
Effects: <Applied effects or None>
```

## Worked Example

Example of a debuff identify popup (matches the style requested for [Clint's](../characters/party/clint.md) system identify):

```text
┌──────────────────────────────────────────────┐
│ STATUS: Fascination                          │
├──────────────────────────────────────────────┤
│ Type: Debuff (Charm / Compulsion)            │
│ Source: <Unknown Caster>                     │
│ Duration: 6s                                 │
│ Stacks: 0 (Does not stack; refreshes)        │
│ Dispel: Yes (Cleanse/Dispel)                 │
├──────────────────────────────────────────────┤
│ Summary: Your focus is pulled to the caster. │
├──────────────────────────────────────────────┤
│ Numbers:                                     │
│ - Forces target-priority: Caster             │
│ - -80% threat awareness to other enemies     │
│ - Break on: loss of line-of-sight OR         │
│   forced redirection by ally intervention    │
└──────────────────────────────────────────────┘
```

> Note: If you need to express something that cannot be quantified yet, prefer a **Limit** line over vague prose.
