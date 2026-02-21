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
| 1 | Turn Undead | Spell | Repels, weakens, or damages undead creatures |
| 2 | Bless | Spell | Allies gain improved accuracy, resolve, and fear resistance |
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

> **Migration Note:** This section is a scaffold. Replace the placeholders with the locked progression we designed in chat.

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

> **Migration Note:** Convert every named spell/skill/song into a stat block with hard numbers.
> Use the template from `canon/style-guide.md` and UI popup style from `system/ui-popups.md`.

### Template
#### <Ability Name>
- **Type:** Spell | Skill | Song | Smite | Passive
- **Level:** #
- **Cost:** (mana/stamina/none)
- **Cooldown:** (if any)
- **Duration:** (if any)
- **Targeting:** (self/ally/enemy/area)
- **Rules:** (bullets w/ numbers)
- **Scaling:** (levels or K-bands)

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
