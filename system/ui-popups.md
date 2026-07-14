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

### 5) System Identify — Entity

Use when a character with a **standard System interface** identifies a creature/object (as opposed to a status effect, which uses format #3). Reveals nameplate stats plus the **Assessment** line — a short, dry, System-generated read on the target. The Assessment is where the System's snark lives; keep it one to three lines and in-character for the System's flat, faintly condescending voice.

```text
┌──────────────────────────────────────────────┐
│ SYSTEM IDENTIFY                              │
├──────────────────────────────────────────────┤
│ Entity:  <Name>                              │
│ Level:   <N>       Role: <Minion/…/Boss>     │
│ Type:    <Construct/Undead/Beast/…>          │
│ HP:      <cur/max> AR:   <n / — >            │
│ Threat:  <Trivial/Moderate/Deadly/…>         │
├──────────────────────────────────────────────┤
│ Notable:                                     │
│ - <key mechanic / immunity / weakness>       │
│ - <reward note, if unusual>                  │
├──────────────────────────────────────────────┤
│ Assessment:                                  │
│ <1–3 dry, snarky System lines>               │
└──────────────────────────────────────────────┘
```

- **Threat** is the [danger-factor](xp.md#xp-award-formula) read, *not* the nameplate Level — a L10 gnome reads **Trivial** to a 999-HP party. This is the field that tells the player "the level number is lying to you."
- **The System may withhold.** Identify reports what the System chooses to surface, not the ground truth — it can read **invulnerable** on a target with a hidden weakness (e.g. the [Whack-a-Gnome](../lore/dungeons/spirit-dungeon/mobs.md#what-system-identify-gives-clint) gnomes, immune to everything *except* an implement the scan never names). Use this to gate discoveries: the box tells the party what to fear, not always how to win.
- **Clint is interface-free.** His [Innate System](../characters/party/clint.md) delivers Identify as **direct knowledge, not a rendered popup** — reserve the bordered box above for standard-UI POVs. For Clint (or any natural-knowledge read), set the system info apart with a **plain, borderless fenced code block** — the facts he just *knows*, distinguished from narration without implying a UI he doesn't see. Example: the [Whack-a-Gnome scan](../lore/dungeons/spirit-dungeon/mobs.md#what-system-identify-gives-clint). The information is the same; only the chrome differs.
- **Strider aside (optional):** [Strider doesn't see popups](../characters/party/clint.md#patron-strider) — he reads the same underlying data directly and **just knows.** A patron quip may follow as an italic line only Clint hears, distinct from the System's own Assessment. Use sparingly.

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
