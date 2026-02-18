---
canon: true
stability: evolving
---

# Effects

Effects are the system's unified model for buffs, debuffs, conditions, and persistent room states.

This page defines:
- Effect taxonomy
- Stacking and refresh rules
- Dispel/Cleanse semantics
- Core fields used by spell/skill definitions

## Core Fields

Every effect should be definable with:

- **Name**
- **Type**: Buff / Debuff / Condition / Room Effect
- **Tags**: e.g., Damage, Heal, CC, Detection, Stealth, Shield
- **Duration**: seconds, or Permanent
- **Tick**: optional periodic interval (DoT/HoT)
- **Stacks**: maximum stacks and stacking rule
- **Source**: caster/item/environment
- **Dispel**: whether removable, and by what (Dispel/Cleanse)
- **Immunity Tags**: what blocks it (e.g., Charm Immune)

## Stacking Rules

Declare one of these:

- **Unique**: cannot be applied if already present
- **Refresh**: reapplying resets remaining duration
- **Extend**: reapplying adds duration (up to a cap)
- **Overwrite**: newest replaces old (may change magnitude)
- **Stacks (Independent)**: each application is its own stack with its own timer

## Taxonomy

### 1) Cure (Cleanse)

Removes **non-magical or bodily** afflictions (poison, disease) and optionally some minor conditions.

Common uses:
- Remove Poison
- Remove Disease
- Remove Curse (if declared as bodily/taint rather than magical binding)

### 2) Dispel

Removes **magical** effects.

Dispel should declare:
- `Dispel Tier` (or potency)
- `Allowed Tags` (e.g., removes Buffs, Debuffs, both)
- `Restrictions` (e.g., cannot dispel Permanent, cannot dispel System effects)

### 3) Crowd Control (CC)

Effects that constrain actions or behavior.

Common CC tags:
- **Stun**: no actions
- **Root**: cannot move (movement is rare but still meaningful for flee/position flags)
- **Silence**: cannot cast spells
- **Disarm**: cannot use weapon attacks
- **Fear**: forced flee or forced disengage attempts
- **Charm / Compel**: forced target priority or ally-like behavior

### 4) Detection

Effects that allow perceiving hidden entities.

Examples:
- Detect Stealth
- See Invisible
- Sense Life

Detection effects should specify:
- What they reveal (stealth/invisibility/phase)
- Whether they are passive or active pulse
- Whether they counter specific stealth tiers

### 5) Stealth

Effects that conceal an entity.

Examples:
- Hide
- Invisibility
- Phase / Veil (special-case, may be unique to [Selene's](../characters/party/selene.md) kit)

Stealth effects should specify:
- What they block (targeting, threat, auto-attacks)
- What breaks them (damage, actions, proximity, time)
- What counters them (Detection tags)

### 6) Room Effects

Effects applied to a room rather than an entity.

Examples:
- Silence Field
- Null Magic Zone (environmental; see `mana.md`)
- Burning Ground / Hazard

Room effects should define:
- Area: room (or adjacent rooms if special)
- Inclusion/exclusion: enemies/allies/all
- How entities entering/leaving are handled (apply on enter vs periodic pulse)

### 7) Globe (Spell Blocking)

A globe is a protective field that blocks spells by tier or tag.

Define:
- Block rule: `Blocks <= Tier N` or `Blocks <Tag>`
- Whether it blocks friendly spells too
- Whether it can be pierced (penetration rules)

### 8) Banish

Removes or destroys summoned/constructed entities.

Define:
- Target restriction: summoned only
- Success rule: guaranteed vs contested (summoner level vs banisher)
- Side effects: backlash or partial dismissal

### 9) Resurrect

Returns a dead character to life under defined constraints.

Define:
- Allowed window (seconds since death)
- Allowed location (same room, safe zone)
- Resource cost and drawback (e.g., rez sickness)
- Restrictions (cannot resurrect in Null Magic Zone unless body removed)

## Dispel and Cleanse Semantics

- **Cleanse/Cure** targets bodily/taint effects: poison/disease/curse (as defined).
- **Dispel** targets magical effects.
- Some effects may be flagged `System-Locked` and cannot be removed by normal dispel/cleanse.

## Recommended Effect Declaration Block (for abilities)

```text
Effect:
- Name: <...>
- Type: <Buff/Debuff/Condition/Room>
- Tags: <...>
- Duration: <...>
- Stacks: <...>
- Dispel: <Cleanse/Dispel/None>
- Break: <rules, if any>
- Numbers: <hard values>
```
