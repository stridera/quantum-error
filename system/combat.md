---
canon: true
stability: evolving
---

# Combat

This page defines the canonical combat loop and resolution pipeline.
Quantum Error combat is **real-time tick-based** under the hood, but it reads like discrete actions.

## Core Model

- Combat occurs in a **room**.
- Entities act when their **action timer** is ready.
- Actions resolve as: **[Targeting](targeting.md) → Hit Check → Damage → [Effects](effects.md) → Death/Downed**.

## Time and Ticks

- **Tick**: the smallest simulation step (implementation detail).
- **Action Cooldown**: time until an entity can act again.
- **Global Cooldown (GCD)**: optional shared delay after any action (used to prevent spam).

Canon assumption:
- If a page or ability uses "seconds" it maps to real-time.
- If it uses "turns", a turn is an abstract chunk of time (use sparingly; prefer seconds).

## Action Types

- **Basic Attack**: weapon attack; usually cheapest and most frequent.
- **Ability**: spell/skill/song/smite; may consume mana/stamina.
- **Reaction (Optional)**: block/parry/interrupt; must be explicitly supported.

## Hit Resolution

### Accuracy vs Evasion

Most offensive actions that can miss use an opposed check:

- **Accuracy**: attacker's ability to land the hit
- **Evasion**: defender's ability to avoid it

The exact formula is implementation-defined, but canon requires:
- Higher Accuracy → higher hit chance
- Higher Evasion → lower hit chance
- Extreme penalties (e.g., heavy encumbrance) must be meaningful

**Design guardrail (canon intent):**
An encumbered attacker with a large accuracy penalty should **not** still hit a nimble target ~95% of the time.
If the formula ever produces that outcome, it should be considered a bug in tuning.

### Guaranteed Hits / Saves

Some abilities do not use Accuracy/Evasion. They must declare:
- `Roll: None` (guaranteed)
or
- `Roll: Save` (defender uses a saving throw/resist stat)

## Criticals and Glancing

Optional but supported conventions:
- **Critical Hit**: increases damage and/or applies a special effect
- **Glancing Blow**: reduced damage on near-miss (use for "always does something" abilities)

If used, declare in the ability:
- `Crit: <chance>`, `Crit Effect: <...>`
- `Glance: <rule>`

## Damage Pipeline

Damage is resolved in this order:

1. **Base Damage** (weapon/spell)
2. **Modifiers** (stats, buffs, vulnerability, amplification)
3. **Mitigation** (armor/resist/soak, reductions, shields)
4. **On-Hit Procs** (status effects, lifesteal)
5. **Death/Downed Check**
6. **Post-Death Triggers** (on-kill effects, summons expiry, etc.)

### Mitigation Conventions

Damage types should declare an **element/type** (physical, fire, arcane, etc.).
Mitigation sources may include:
- Flat reduction
- Percent reduction
- Immunity (rare; must be explicit)
- Absorption shields (consume shield first)

## Threat / Aggro (Canonical)

Threat determines enemy target selection unless overridden by a forced taunt/charm.

- Damage generally increases threat.
- Healing generally increases threat (often split across enemies).
- Some abilities explicitly manipulate threat.

## Interrupts and Control

Crowd control effects (stun, silence, fear, charm) are defined in `effects.md`.
Combat must respect effect tags:
- `Stun`: prevents actions
- `Silence`: prevents spellcasting
- `Disarm`: prevents weapon attacks
- `Charm/Compel`: forces behavior or target priority

## Death and Respawn

Death rules can vary by zone and conditions (see `mana.md` for Null Magic Zones).

Canonical baseline:
- Characters can respawn unless a special condition prevents it.
- Certain environments (e.g., Null Magic Zones) can make death permanent unless extraction occurs.

## Open Questions (Phase 1 capture)

These are acknowledged design points that may be tuned later:
- Exact hit chance formula (logistic vs linear clamp vs opposed roll)
- Whether block/parry exists for all classes or only some
- Whether glancing blows are universal or per-ability
