---
canon: true
stability: evolving
---

# UI Popups & Stat Blocks

This document defines the canonical formatting for in-world **System** text as it appears in the prose — identify reads, status effects, ability unlocks, item descriptions, combat snippets.
These conventions are used by:
- Class pages (new abilities)
- Spell/skill pages (help/inspect)
- [Effects](effects.md) (buff/debuff identify)
- [Combat](combat.md) logs (resolution snippets)
- Bestiary and dungeon pages (entity identify)

## Principles

- **No box chrome.** Blocks are plain fenced `text` — no `┌─┐` borders, no column alignment, no `[SYSTEM HELP]` brackets. Bobbinry renders fenced blocks as `<code>`, which already sets them apart from narration. Borders just add noise.
- **One shape for everyone.** The block looks the same whether the POV has a standard UI or is [Clint](../characters/party/clint.md), who is interface-free after Ch 14. The difference is in the *narration around it*: a standard-UI character reads a popup; Clint just knows, and the block is how the novel shows the reader what he knows. See [System UI](ui.md#clints-exception-instinctual-access).
- **Header, flavor, fields.** First line is `Name (Kind)`. Then optional flavor text. Then a blank line, then the hard numbers.
- **Hard numbers whenever possible** (cost, duration, cooldown, magnitude). If something can't be quantified yet, prefer a **Limit** line over vague prose.
- **Consistent units and labels** so the System feels system-generated: `8s` not `8 Seconds`; `Dispellable: Yes/No`; `HP: 150 | Damage: 11 | AR: 6` on one pipe-separated line.

## The Shape

```text
<Name> (<Kind>)
<Optional flavor text — one to three sentences, in the voice appropriate to the source; see "Two Voices" below.>

<Field>: <value>
<Field>: <value>
Effects:
- <hard-number bullet>
- <hard-number bullet>
```

`Kind` is whatever the reader most needs to parse the block: `Mental Debuff`, `Elite`, `Boss`, `Uncommon Accessory`, `Passive`, `Smite`. Stacks, sources, and dispel rules are fields, not part of the header.

## Two Voices

The flavor text is real, in-world text — not authorial decoration — and it comes in two registers that map onto the [simulation tiers](../meta/real-world.md):

1. **The core System — flat, bureaucratic, faintly condescending.** *"This action is logged."* *"You no longer require an interface."* *"Sudden exposure to massive amounts of mana floods your system."* Used for abilities, core status effects, system notices, and anything the simulator itself owns.
2. **Generated content — the carnival barker.** *"Try not to enjoy it too much."* *"Dressed to kill — and patient enough to wait for the perfect moment."* *"The teeth are not decorat—."* This is the **template engine narrating what it generated**, in the personality of the thing it generated. The Spirit Dungeon's items sound like the Spirit Dungeon. It is allowed to taunt, to coach in second person (*"Get out of the line."*), and — rarely, deliberately — to glitch or change mid-read, because it is live text, not a static label.

Ch 1's *"Welcome to Universe System Simulator 0.8, where you can create and simulate entire worlds!"* is the second voice, seeded on page one. The distinction is never explained in Book 1; it's there for a later book to notice.

A **Strider aside** is a third thing: an italic line in the prose, not inside the block, heard by Clint alone. See [Patron: Strider](../characters/party/clint.md#patron-strider).

## Block Types

### 1) Identify — Entity

What an Identify (or Clint's System Identify) returns on a creature or object. In Book 1 the read is **thin**: Level, Kind, HP, Damage, AR, and at most one notable mechanic. No attributes, no XP, no resistances — that depth is gated behind later progression, and its absence is the hook.

```text
Prop Spider (Elite)
A decorative giant spider that was six feet of wire and fake fur. Now it's six feet of wire and fake fur that wants to eat you.

Level: 10
HP: 160 | Damage: 11 | AR: 4
```

- **The System may withhold.** Identify reports what the System chooses to surface, not the ground truth — it can read **INVULNERABLE** on a target with a hidden weakness (the [Whack-a-Gnome](../lore/dungeons/spirit-dungeon/mobs.md#what-system-identify-gives-clint) gnomes). Use this to gate discoveries: the block tells the party what to fear, not always how to win.
- A `Threat:` field (Trivial / Moderate / Deadly) may appear when the [danger factor](xp.md#xp-award-formula) diverges from the nameplate level. It's the line that says "the level number is lying to you."

### 2) Status Effect (Buff / Debuff)

```text
Performance Review (Mental Debuff)
It's time for your performance review, and you already know it's not going to be good. No amount of extra flair will save you now.

Source: Store Manager "Dan"
Duration: 8s (Will Save DC 14: 4s)
Stacks: No (refreshes)
Dispellable: Yes
Effects:
- -3 Accuracy
- -3 Damage Dealt
- -25% Healing Output
```

Field order: `Source`, `Duration`, `Stacks`, `Dispellable`, `Effects`. Effects applied **to the POV character** always appear in full — the System reports what's being done to your body without being asked. Effects on *others* show the name passively and the numbers only on inspect (see [System UI](ui.md#system-synesthesia-how-pools-feel)). Omit fields that don't apply; don't write `Stacks: No` on a block where stacking was never in question.

### 3) Ability — Unlock / Help

Use when a character gains or inspects a skill, spell, song, or smite.

```text
Smite: Sanction (Smite)
You may channel System authority through a physical strike, marking a hostile entity as noncompliant and applying corrective force. This action is logged.

Cost: 15 mana
Cooldown: 4s
Targeting: Enemy (melee)
Effects:
- +30 flat System damage
- +10% weapon damage
- +30% damage vs summoned, corrupted, or system-flagged entities
```

A level-up or unlock *notification* is a single line, not a block: `You have achieved Level 4!`

### 4) Item

```text
Shard of Duty (Rare Accessory — Evolving)
Mirror fragment in a cracked shield-shaped frame.

+1 AR
+10% threat generation on taunt abilities

"The shield cracked. You didn't."
```

Items put their bonuses as bare `+N` lines rather than an `Effects:` list, and may close with a quoted tagline.

### 5) Combat Resolution Snippet

A single resolved action, in-line, for combat logs or healing readouts.

```text
Cure Light Wounds (Empowered)
- Healing Output: +284 HP
- Bleeding: Removed
- Chest Trauma: Stabilized
```

```text
<Actor> uses <Ability> on <Target>.
Hit: <Yes/No>  (Roll: <Accuracy> vs <Evasion>)
Damage: <amount> <type>  (Mitigation: <amount/percent>)
Effects: <Applied effects or None>
```

## Console-Era Blocks (Ch 4–13)

Before the Transition, the party edits the simulation through a memory-editor console. That text looks different on purpose — single-line records with memory IDs — and should stay that way:

```text
Vanessa Wong(#124823). Age 28. Female Human(#1) Sorceress(#28). Level 1.

Affected by: Severe Mana Lock(#495323)
```

Don't retrofit console-era text to the post-Transition shape.
