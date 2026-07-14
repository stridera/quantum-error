---
canon: true
stability: locked
last_reviewed: 2026-02-05
---

# Quantum Sorceress

Using magic to control the world.

Sorceresses channel raw magical power through force of will. The Quantum Sorceress variant draws on principles of quantum mechanics—probability, superposition, and observation effects.

## Design Philosophy

- **Role**: Ranged DPS, area damage, battlefield control
- **Theme**: Emotional amplification, instability as power
- **Unique Mechanic**: Spells tagged as **Anchor** (stable), **Amplified** (scales with emotion), or **Breaking** (reality-altering)

## Instability System

| Tag | Behavior |
|-----|----------|
| **Anchor** | Stable, predictable, emotionally neutral |
| **Amplified** | Emotional load increases power but reduces control |
| **Breaking** | Reality-bending effects with environmental aftermath |

## Ability Progression (Levels 1-20)

| Level | Ability | Type | Tags | Effect |
|-------|---------|------|------|--------|
| 1 | Mana Sense | Passive | perception | Perceive ambient mana density, spell residue, and nearby casting pressure |
| 1 | Arcane Bolt | Spell | anchor | Launch a focused arcane projectile; reliable baseline damage |
| 2 | Spell Focus | Passive | control | Increased spell precision and reduced cast disruption |
| 3 | Mana Shield | Spell | anchor | Convert mana into a protective barrier |
| 3 | Minor Illusion | Spell | anchor | Create a small visual or auditory illusion. Scale increases with INT—at INT 20+, illusions can fill a corridor or replicate full environmental features (walls, terrain, signage). The illusion remains stable (anchor behavior): it's the canvas that grows, not the volatility. This is raw computational power expanding the spell's parameters, not emotional amplification. |
| 4 | Elemental Affinity | Passive | amplified | Emotions bias how magic expresses (fear→cold, rage→fire, focus→lightning) |
| 5 | Fireball | Spell | amplified | Explodes on impact, damaging enemies in an area |
| 6 | Channel Mana | Utility | anchor | Recover mana more efficiently when not actively casting |
| 6 | Fan of Flames | Spell | amplified | Short close-range cone of flame — the smaller, cheaper cousin of Flame Wave (L13). Shown Ch 14. |
| 7 | Frost Bind | Spell | anchor | Deal cold damage and apply slow or brief root |
| 7 | Veil Image | Spell | amplified | Project moving illusory doubles that confuse targeting |
| 10 | Lightning Lance | Spell | amplified | Piercing bolt that excels against armored targets |
| 10 | Displacement | Spell | amplified | Persistent misalignment between where you are and appear |
| 11 | Mana Surge | Utility | amplified | Immediate mana gain; increases escalation risk |
| 12 | Spell Weaving | Passive | anchor | Chaining spells reduces cast time and improves flow |
| 13 | Flame Wave | Spell | amplified | Sweeping cone of flame hitting multiple enemies |
| 14 | Arcane Ward | Spell | anchor | Reactive ward that reduces incoming magical harm |
| 14 | Mirror Phantasm | Spell | amplified | Multiple illusionary selves fracturing enemy targeting |
| 15 | Elemental Mastery I | Passive | amplified | Elemental spells gain secondary effects based on emotional state |
| 16 | Void Pulse | Spell | breaking | Disruptive pulse that destabilizes casting and compresses space |
| 17 | Mana Burn | Spell | breaking | Tears at mana; drains reserves and harms through power |
| 18 | Arcane Instinct | Passive | anchor | When critically threatened, magic reacts first (ward flare, reflexive displacement) |
| 19 | Spell Cascade | Passive | amplified | Area spells expand or chain when emotional load is high |
| 20 | **Cataclysm** | Capstone | breaking | Reality-bending devastation; this is an event, not just damage |

## Mana Lucent

A concept specific to Vanessa: after her Mana Shock, her eyes and veins glow softly with mana. The glow shifts toward the elemental color of whatever spell she is casting.

## Notable Quantum Sorceresses

- [Vanessa](../characters/party/vanessa.md)

## Progression (1–99)

> **Migration Note:** This section is a scaffold. Replace the placeholders with the locked progression once finalized.

### Table
| Level | Unlocks |
|---:|---|
| 1 | *(TODO)* |
| 2 | *(TODO)* |
| 3 | *(TODO)* |
| 4 | *(TODO)* |
| 5 | *(TODO)* |
| 6 | *(TODO)* |
| 7 | *(TODO)* |
| 8 | *(TODO)* |
| 9 | *(TODO)* |
| 10 | *(TODO)* |
| 11 | *(TODO)* |
| 12 | *(TODO)* |
| 13 | *(TODO)* |
| 14 | *(TODO)* |
| 15 | *(TODO)* |
| 16 | *(TODO)* |
| 17 | *(TODO)* |
| 18 | *(TODO)* |
| 19 | *(TODO)* |
| 20 | *(TODO)* |
| 21–99 | *(TODO: expand or define scaling + "every N levels" unlock cadence)* |

## Ability Stat Blocks

> Blocks below cover the kit shown in prose through Ch 21; remaining abilities gain blocks as they enter the story. Costs assume the **High mana group** (L1 ≈ 20, L10 ≈ 110 — see [stat progression](../system/stat-progression.md)); Vanessa's 9,999 pool + Mana Lucent (spells act two levels higher) makes her wildly over-spec.

#### Mana Shield
- **Type:** Spell (anchor) · **Level:** 3 · **Cost:** 20 mana · **Cooldown:** 10s after break · **Duration:** Until broken or dismissed · **Targeting:** Self

**Rules**
- Converts mana into a barrier absorbing **60 damage** at base.
- While the shield holds, no HP damage is taken; overflow damage passes through on break.
- Console-raised to spell level 10 ("Mastered") for Vanessa in Ch 7 — her version absorbs ~240.

**Scaling:** +20 absorption per spell level.

#### Minor Illusion
- **Type:** Spell (anchor) · **Level:** 3 · **Cost:** 10–30 mana by scale · **Duration:** Sustained (light concentration) · **Targeting:** Area

**Rules**
- Creates a stable visual or auditory illusion. Base canvas: object or sound up to person-size.
- Scale grows with INT — at INT 20+, illusions can fill a corridor or replicate full environmental features (fake detour signs, fallen trees, a driver's face — Ch 11).
- Anchor behavior: the canvas grows, not the volatility. Computational power, not emotional amplification.

**Scaling:** canvas size with INT; fidelity with spell level.

#### Fireball
- **Type:** Spell (amplified) · **Level:** 5 · **Cost:** 30 mana · **Cooldown:** 6s · **Duration:** Instant · **Targeting:** Area (20 ft blast, thrown)

**Rules**
- 30–50 fire damage in the blast, 25% chance to ignite (1d4 burn, 2 rounds).
- **Amplified:** under high emotional load, damage rises up to +50% and the blast radius grows — with matching loss of placement control. Vanessa has dropped one on her own tank (Ch 20, deliberately).
- Full version distinct from Fan of Flames (Ch 15).

**Scaling:** +10 damage per 5 levels; Mana Lucent casts act two levels higher.

#### Fan of Flames
- **Type:** Spell (amplified) · **Level:** 6 · **Cost:** 20 mana · **Cooldown:** 4s · **Duration:** Instant · **Targeting:** Area (15 ft cone)

**Rules**
- 18–30 fire damage in a close cone — the smaller, cheaper cousin of Flame Wave (L13).
- Amplified: emotional load widens the cone before it deepens the damage.
- Shown Ch 14 (post-Transition coyote fights).

**Scaling:** +6 damage per 5 levels.

## UI Popups

> **Migration Note:** Add one "Help" popup per ability, matching the in-world system UI.

### Template
```text
[SYSTEM HELP] <Ability Name>
Type: <Spell/Skill/Song/Passive>
Cost: <...>
Cooldown: <...>
Duration: <...>
Targeting: <...>

<1–3 line in-world description>

Mechanics:
- <bullet>
- <bullet>
```

## Open Questions

- *(TODO: add unresolved items for Quantum Sorceress, and mirror them into `canon/status.md`.)*
