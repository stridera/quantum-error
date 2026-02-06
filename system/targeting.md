---
canon: true
stability: evolving
---

# Targeting

Quantum Error combat is primarily **room-based**: most abilities can only affect entities in the same room.
This page defines the canonical targeting model used by spells, skills, items, and system effects.

## Target Sets

All abilities must declare a `Targeting` category.

- **Self**: the caster/user only.
- **Ally**: a friendly entity in the room (party member, friendly NPC).
- **Enemy**: a hostile entity in the room.
- **Room (AoE)**: affects multiple entities in the room.
- **Corpse**: a corpse entity in the room.
- **Item**: an item in inventory or on the ground (must declare which).
- **Location (Special)**: modifies the room itself (rare; see `Room Effects` in `effects.md`).

## Valid Selection Rules

### Single-Target (Self/Ally/Enemy/Corpse/Item)

- Requires an explicit target selection unless the ability is Self.
- If no valid target exists, the action fails and consumes **no** resource unless otherwise specified by the ability.

### Room (AoE)

AoE abilities must declare:
- **Inclusion**: `Enemies`, `Allies`, or `All`
- **Exclusions**: optional explicit exclusions (e.g., "exclude caster", "exclude party")
- **Cap**: optional maximum number of entities affected (default: all valid in room)

If multiple entities qualify and a cap is set, selection priority is:
1. Explicitly targeted entity (if ability supports both "Room" + "primary target")
2. Closest threat / highest threat (system-defined)
3. Tiebreak: stable deterministic order (prevents RNG exploits)

## Line of Effect (Room-Based)

Unless an ability says otherwise, **line of effect** is considered valid if:
- The caster and target are in the same room, and
- The target is not explicitly flagged as *out of phase*, *untargetable*, or *hidden beyond detection*.

### Hidden / Invisible Targets

Abilities that can affect hidden targets must explicitly declare a detection bypass, e.g.:
- `Requires: Detect Stealth`
- `Ignores: Invisibility`
- `Cannot Target: Phased`

Detection rules live in `effects.md` under **Detection**.

## Special Targeting

### Adjacent Rooms (Rare)

Some abilities may target adjacent rooms (e.g., dungeon traps, boss mechanics, system-admin style actions).
These must declare:
- `Range: Adjacent`
- `Requires: Line of Effect (exit exists and not sealed)`
- The UI should clearly warn the player when cross-room targeting occurs.

### Multi-Target (Chain / Spread)

If an ability jumps between targets:
- Declare `Primary Target` selection rule
- Declare `Jump Rule`: random, threat-based, nearest, etc.
- Declare `Max Jumps` and whether jumps can repeat targets

## Failure Modes

Abilities should define what happens when targeting fails:
- **Fizzle**: no effect, no resource cost (default for mis-targeting)
- **Backlash**: consumes cost or harms caster (rare; must be explicit)
- **Partial**: applies to a reduced subset (AoE with cap and insufficient targets)

## Suggested Declaration Block

Use this block in ability definitions for consistency:

```text
Targeting:
- Category: <Self/Ally/Enemy/Room/Corpse/Item>
- Inclusion: <Enemies/Allies/All> (if Room)
- Exclusions: <...> (optional)
- Cap: <N> (optional)
- Line of Effect: <Room / Adjacent / Special>
```
