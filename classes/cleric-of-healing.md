---
canon: true
stability: locked
last_reviewed: 2026-02-05
---

# Cleric of Healing

Healers that channel divine power to heal and combat the undead.

A traditional cleric focused on restoration and support. Unlike the [Paladin of the System](paladin-of-the-system.md), the Cleric of Healing has no special system ties—purely divine magic channeled through faith.

## Design Philosophy

- **Role**: Primary healer, party sustain, anti-undead
- **Theme**: Steady, reliable, with subtle trauma cues
- **Unique Mechanic**: Emotional limiter—spells always work, but exact a personal cost

## Emotional Limiter

Wade's class includes an emotional limiter mechanic:
- Healing spells **always function as intended**
- Strong emotions may surface after casting
- Trauma cues are informational; they do not alter spell reliability
- The cost is psychological, not mechanical

## Ability Progression (Levels 1-20)

| Level | Ability | Type | Effect |
|-------|---------|------|--------|
| 1 | Cure Light Wounds | Spell | Restore modest health to a living target |
| 1 | Holy Light | Spell | Conjure steadfast divine light; undead and corrupted entities flinch from its radius. Granted to all holy classes. |
| 1 | Turn Undead | Spell | Repels, weakens, or damages undead creatures |
| 2 | Bless | Spell | Allies gain improved accuracy, resolve, and fear resistance (applies the **Blessed** status) |
| 3 | Cleric Aura | Aura | Passive calm radius — nearby allies gain minor fear resistance and +5% healing received |
| 3 | Cure Poison | Spell | Removes poison effects from a target |
| 4 | Lesser Restoration | Spell | Removes minor debuffs and afflictions |
| 5 | Prayer of Healing | Spell | Gradually restores health to multiple allies (HoT) |
| 6 | Divine Sense | Passive | Sense undead presence and spiritual corruption |
| 7 | Shield of Faith | Spell | Protective blessing reduces incoming damage |
| 8 | Revitalize | Spell | Restore health and stamina |
| 9 | Consecrate | Spell | Sanctify ground, harming undead and disrupting dark forces |
| 10 | Mass Heal | Spell | Instantly restore significant health to allies (AoE) |
| 11 | Divine Resilience | Passive | Allies take reduced damage while critically injured |
| 12 | Remove Curse | Spell | Removes magical curses and afflictions |
| 13 | Beacon of Hope | Spell | Increases effectiveness of healing effects |
| 14 | Radiant Smite | Spell | Deal radiant damage to undead and dark entities |
| 15 | Resurrection | Spell | Restore life to a recently fallen ally (long channel, low HP return, heavy [rez sickness](../system/death.md)) |
| 16 | Spirit Mend | Spell | Heal an ally through obstacles or distance |
| 17 | Sacred Barrier | Spell | Create powerful protective barrier for allies |
| 18 | Faithful Guardian | Passive | Automatically shield the most vulnerable ally |
| 19 | Life Overflow | Passive | Excess healing converts into temporary shields |
| 20 | **Divine Intervention** | Capstone | Once per long interval, prevent a party wipe with overwhelming divine aid |

## Healing Reference (Levels 1–20)

### Design Assumptions (Locked)

- Party HP ≈ 999
- Combat heals never exceed ~40–45% max HP
- "Empowered" = same spell, more mana, faster reconstruction
- Emotional pressure scales with speed + intensity, not spell tier

---

### Single-Target Healing

#### Cure Light Wounds

| Mode | Heal Range | Time | Mana Cost | Notes |
|------|-----------|------|-----------|-------|
| Normal | 60–120 HP | Instant | Low | Safe, routine |
| Empowered | 180–300 HP | Instant | High | Tissue rebuilt rapidly |
| Overdrawn (rare) | 300–380 HP | Instant | Extreme | Causes visible backlash in Wade |

**Empowered Effect**
- Accelerates clotting, lung re-inflation, organ stabilization
- Leaves patient weak, shaken, alive

**Emotional Cost**
- Normal: Minimal
- Empowered: Noticeable
- Overdrawn: Severe (hands shake, dissociation)

> This is the spell you want for Clint's bear trap moment.

---

#### Spirit Mend

| Mode | Heal Range | Time | [Mana](../system/mana.md) Cost | Notes |
|------|-----------|------|-----------|-------|
| Standard | 150–250 HP | 3–6 sec channel | Moderate | Slow reconstruction |
| Sustained | +30–40 HP/sec | Channel | Sustained | Wade prefers this |

**Empowered Effect**
- Rarely empowered
- Doing so shortens channel but spikes emotional load

**Use Case**
- "You're hurt, but not dying right now."

---

#### Revitalize

| Mode | Heal Range | Time | Mana Cost | Notes |
|------|-----------|------|-----------|-------|
| Standard | 120–200 HP | Short cast + HoT | Moderate | Restores stamina |
| Empowered | 200–260 HP | Faster cast | High | Clears shock/exhaustion |

**Extra Effects**
- Reduces exhaustion
- Stabilizes breathing
- Clears dizziness

**Emotional Cost**
- Low → Medium
- This spell calms Wade. It fixes aftermath, not crisis.

---

### Group Healing

#### Prayer of Healing

| Mode | Heal Range | Time | Mana Cost | Notes |
|------|-----------|------|-----------|-------|
| Standard | 150–220 HP (AoE) | Long cast | Moderate | Out of combat |
| Empowered | Not used | — | — | Wade refuses to rush this |

**Emotional Cost**
- Very low
- Everyone's already stable.

---

#### Mass Heal

| Mode | Heal Range | Time | Mana Cost | Notes |
|------|-----------|------|-----------|-------|
| Standard | 180–260 HP (AoE) | Instant | High | Emergency stabilization |
| Empowered | 260–350 HP | Instant | Extreme | Multiple lives at once |

**Emotional Cost**
- High
- Too many bodies, too much damage input.

---

### Emergency / Line-Crossing

#### Restoration (Lesser / Greater)

| Type | Effect | Time | Mana Cost | Notes |
|------|--------|------|-----------|-------|
| Lesser | Clears poison, paralysis, breathing issues | Short cast | Moderate | Surgical |
| Greater | Clears severe trauma, organ failure | Long cast | High | Drains Wade |

**Key Point:** Restoration does not heal HP — it makes healing possible.

---

#### Resurrection
- **Type:** Spell
- **Source:** [Cleric of Healing](../classes/cleric-of-healing.md)
- **Level:** 15
- **Cost:** High mana (scales with rez tier)
- **Cooldown:** None (limited by mana and channel time)
- **Duration:** Channel (30s+ at L15, scaling shorter with level)
- **Targeting:** Ally (ghost at corpse — rezzer must be physically present)
- **Tags:** Healing, Resurrection
- **Rules:**
  - Target must be in [ghost state](../system/death.md) (not yet released).
  - Rezzer must be at the corpse location.
  - Channeled cast — rezzer cannot take other actions during channel. Interrupted if the rezzer takes damage or moves.
  - Target returns at low HP (10-25% at L15, scaling with level).
  - Target suffers [rez sickness](../system/death.md) — reduced stats for a duration, severity scales inversely with rez quality.
  - At L15, this is a post-combat tool. The 30s+ channel makes mid-fight use nearly impossible without dedicated protection.
- **Scaling:** Channel time decreases, HP on return increases, rez sickness lessens. True Resurrection (~L90-95) is full HP restore with minimal sickness and ~5s channel.

---

## Key Mechanics

### Anti-Undead Kit
- Turn Undead (Level 1)
- Consecrate (Level 9)
- Radiant Smite (Level 14)

### Protection
- Shield of Faith (single target)
- Sacred Barrier (area)
- Faithful Guardian (automatic)
- Life Overflow (excess healing → shields)

## Notable Clerics of Healing

- [Wade](../characters/party/wade.md)

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

> Healing spells have full numbers in the [Healing Reference](#healing-reference-levels-120) above. Blocks below cover the rest of the kit shown in prose through Ch 21; remaining abilities gain blocks as they enter the story. Costs assume the **Medium mana group** (L1 ≈ 17, L10 ≈ 80 — see [stat progression](../system/stat-progression.md)).

#### Holy Light
- **Type:** Spell · **Level:** 1 · **Cost:** 5 mana + 1 mana/min upkeep · **Duration:** Sustained (up to ~10 min) · **Targeting:** Self (30 ft radius)

**Rules**
- Identical to the [Paladin block](paladin-of-the-system.md#holy-light) — granted to all holy classes. Steady divine light; no damage; undead/corrupted suffer −5% accuracy inside and won't willingly cross the lit edge unless commanded or aggroed.

**Scaling:** +5 ft radius and −1% additional accuracy per 5 levels.

#### Turn Undead
- **Type:** Spell · **Level:** 1 · **Cost:** 15 mana · **Cooldown:** 20s · **Duration:** Instant (effects 6s) · **Targeting:** Area (20 ft, undead only)

**Rules**
- Undead at or below the Cleric's level **flee** for 6s or take 10–20 radiant damage if they cannot path away.
- Elites and bosses: no flee — instead −10% damage dealt for 6s.
- First shown Ch 20 (Risen Skeletons).

**Scaling:** damage +5 per 5 levels; the flee threshold tracks Cleric level (level-delta rules apply).

#### Bless
- **Type:** Spell · **Level:** 2 · **Cost:** 20 mana · **Cooldown:** none · **Duration:** 60s · **Targeting:** Group

**Rules**
- Allies gain the **Blessed** status: +5% accuracy, +2 to resistance checks against fear.
- One Blessed instance per caster; recasting refreshes duration.
- Prose note: Ch 16's "Blessed" is this status — *Bless* is the spell, *Blessed* is what it applies.

**Scaling:** +1% accuracy per 5 levels; duration +30s at L10 and L20.

#### Cleric Aura
- **Type:** Aura · **Level:** 3 · **Cost:** none (always on) · **Duration:** Permanent · **Targeting:** Allies within 15 ft

**Rules**
- Passive calm radius: allies gain minor fear resistance (+1 to fear resistance checks) and **+5% healing received**.
- **Ambient [Cleanse](../magic/spells/cleanse.md).** The aura continuously runs the beginner cleaning cantrip on everyone inside it. Not instant — it works the way sunlight dries something. Walk near Wade for a while and the blood comes off your gear, the smell goes, and you arrive somewhere looking like a person. Nobody casts anything. Nobody asks.
- Stacks with Blessed. Shown on Wade's sheet Ch 12.

**Scaling:** +5 ft radius per 5 levels; healing bonus +1% per 10 levels.

> **The Wade of it.** This is the ability that characterizes him best. His magic tidies people up as a side effect of him standing near them, without being asked and without him getting any credit — the passive, unglamorous, permanently-on version of care, which is Wade entire.
>
> **It is named on-page in Ch 22, and it should be.** *(Supersedes an earlier draft of this note, which held that Wade never mentions it and nobody notices.)* Wade says his aura already has a cleaning effect; Clint answers *"I wondered why I was still so clean. I assumed it was because Vanessa kept burning off my clothes."* That is the correct call and the earlier instinct was wrong: **the reader cannot miss something they never knew existed.** Establishing the effect once, as a joke, is precisely what makes its absence legible later. Plant it in comedy; collect on it in silence.
>
> **The Book 2 consequence:** Wade [leaves the party after Book 1](../system/xp.md). The party does not lose the *capability* — [Cleanse](../magic/spells/cleanse.md) is a beginner spell anyone can learn, and they all know it. What they lose is **never having to think about it.** They go back to casting it on themselves, manually, every day, forever. Because Ch 22 named the effect, the reader gets there before the party does and spends a few chapters waiting for one of them to say it out loud. When somebody finally does, it should land harder than any line about missing him — and it should arrive **before** anyone says his name.
>
> **The wish (Book 1) — delivered Ch 22.** Wade wonders whether he could get [Rebekah's](../characters/party/rebekah.md) [Rejuvenation](temporal-bard.md#rejuvenation) folded into his aura: always on, covering everyone near him, nobody having to ask. He is describing a thing he wants to be. *(See `characters/party/wade.md` — deliberate long-range foreshadow of the [substrate ending](../meta/real-world.md). Do not return to it; it is planted and it is enough.)*

#### Lesser Restoration
- **Type:** Spell · **Level:** 4 · **Cost:** 25 mana · **Cooldown:** none · **Duration:** Instant (short cast, ~2s) · **Targeting:** Touch (ally)

**Rules**
- Clears poison, paralysis, and breathing obstruction. Surgical — one affliction category per cast.
- Restoration does not heal HP; it makes healing possible (see the [Restoration table](#restoration-lesser--greater)).

**Scaling:** cast time shortens; Greater Restoration (higher tier) clears severe trauma and organ failure.

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

- *(TODO: add unresolved items for Cleric Of Healing, and mirror them into `canon/status.md`.)*
