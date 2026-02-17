---
canon: true
stability: evolving
last_reviewed: 2026-02-18
---

# Mob Framework

Defines stat progression, role tiers, and encounter design targets for NPCs and monsters in Quantum Error. Designed to produce fights that feel dangerous, tactically interesting, and fair.

Adapted from FieryMUD legacy mob data, with significant rebalancing to fix known issues (flat accuracy, non-scaling stats, underutilized roles, extreme HP asymmetry).

See `stat-progression.md` for player stats and `../items/equipment-framework.md` for weapon/armor targets.

---

## Design Principles

1. **Roles matter.** A Minion, Elite, and Boss of the same level should feel mechanically distinct -- not just have more HP.
2. **Smooth scaling.** No kinks, no clamps, no formula transitions that create discontinuities. Simple polynomials.
3. **K-bands feel different.** K1 teaches fundamentals, K2 demands specialization, K3 requires mastery.
4. **Solo is possible, group is better.** A player can solo Normal mobs at their level. Elites are a challenge. Champions and above require a party.
5. **Stats scale.** Mob attributes increase with level and contribute to combat, not just flavor.

---

## Role Tiers

Every mob has a role that multiplies its base stats and determines its mechanical complexity.

| Role | HP | Damage | Attacks | XP | Loot | Design Intent |
|------|-----|--------|---------|-----|------|---------------|
| **Minion** | 0.25x | 0.5x | 1 | 0.25x | None | Fodder. Dies fast. Comes in packs of 3-8. |
| **Normal** | 1.0x | 1.0x | 1 | 1.0x | Common | Standard encounter. 1v1 fair fight. |
| **Elite** | 2.5x | 1.25x | 1-2 | 3.0x | Uncommon | Named mobs, veteran soldiers. Tough solo. |
| **Champion** | 6.0x | 1.5x | 2 | 10.0x | Rare | Sub-boss. Requires 2-3 players. |
| **Boss** | 15.0x | 2.0x | 2-3 | 25.0x | Epic | Zone boss. Full party (5) required. |
| **Raid** | 40.0x | 2.5x | 3-5 | 75.0x | Legendary | World boss. Multi-party event. |

### Ability Complexity by Role

| Role | Abilities | Mechanics |
|------|-----------|-----------|
| Minion | 0 | Attack only. May flee at low HP. |
| Normal | 0-1 | May have one basic ability (charge, poison, knockback). |
| Elite | 1-2 | Has a signature ability and a "tell" mechanic players can learn to avoid. |
| Champion | 2-3 | Phase transitions, at least one area-denial or "dodge this" mechanic. |
| Boss | 3-5 | Multiple phases, environment interaction, legendary actions (extra turns between player actions). |
| Raid | 5+ | Complex phase scripting, role-specific checks (tank swap, heal check, DPS race), lair effects. |

---

## Base Stat Formulas (Normal Role)

All formulas produce values for a Normal mob. Multiply by role tier for other roles.

### HP

```
mob_hp(level) = 5 * level + 0.1 * level²
```

| Level | Normal | Elite | Champion | Boss | Raid |
|-------|--------|-------|----------|------|------|
| 1     | 5      | 13    | 31       | 77   | 204  |
| 10    | 60     | 150   | 360      | 900  | 2,400 |
| 20    | 140    | 350   | 840      | 2,100 | 5,600 |
| 33    | 274    | 685   | 1,643    | 4,107 | 10,952 |
| 50    | 500    | 1,250 | 3,000    | 7,500 | 20,000 |
| 66    | 766    | 1,914 | 4,593    | 11,483 | 30,620 |
| 80    | 1,040  | 2,600 | 6,240    | 15,600 | 41,600 |
| 99    | 1,475  | 3,688 | 8,850    | 22,125 | 59,000 |

### Damage (per hit)

```
mob_damage(level) = 2 + 0.7 * level + 0.002 * level²
```

| Level | Normal | Elite | Champion | Boss | Raid |
|-------|--------|-------|----------|------|------|
| 1     | 3      | 4     | 5        | 6    | 8    |
| 10    | 9      | 11    | 14       | 18   | 23   |
| 20    | 17     | 21    | 26       | 34   | 43   |
| 33    | 27     | 34    | 41       | 54   | 68   |
| 50    | 42     | 53    | 63       | 84   | 105  |
| 66    | 57     | 71    | 86       | 114  | 143  |
| 80    | 71     | 89    | 107      | 142  | 178  |
| 99    | 91     | 114   | 137      | 182  | 228  |

### Accuracy

```
mob_accuracy(level) = 5 + 0.5 * level
```

| Level | Accuracy |
|-------|----------|
| 1     | 6        |
| 10    | 10       |
| 33    | 22       |
| 50    | 30       |
| 66    | 38       |
| 99    | 55       |

Accuracy scales smoothly across the full range. No minimum clamp -- low-level mobs *should* miss evasive players. Bosses and Raid mobs get +5 and +10 accuracy respectively, reflecting their threat.

### Armor Rating

```
mob_ar(level) = 0.5 * level + 0.005 * level²
```

| Level | AR  | DR% (K1) | DR% (K2) | DR% (K3) |
|-------|-----|----------|----------|----------|
| 1     | 1   | 2%       | --       | --       |
| 10    | 6   | 11%      | --       | --       |
| 20    | 12  | 19%      | --       | --       |
| 33    | 22  | 31%      | --       | --       |
| 50    | 38  | --       | 28%      | --       |
| 66    | 55  | --       | 35%      | --       |
| 80    | 72  | --       | --       | 26%      |
| 99    | 99  | --       | --       | 33%      |

Uses the same DR% formula and K-band constants as player armor. Mob DR ranges from 2% to 33%, mirroring the medium-heavy armor tier for players. Bosses and Raids may have additional Soak or resistance.

---

## Mob Attributes (1-20 Scale)

Unlike legacy mobs (flat ~70 across all levels), QE mob attributes scale with level and vary by archetype.

### Archetype Stat Profiles

| Archetype | Primary | Secondary | Weak | Examples |
|-----------|---------|-----------|------|---------|
| **Brute** | STR, CON | DEX | INT, CHA | Ogres, trolls, bears |
| **Soldier** | STR, DEX | CON | WIS | Guards, knights, warriors |
| **Skirmisher** | DEX | STR, WIS | CON | Wolves, bandits, scouts |
| **Caster** | INT or WIS | CHA | STR, CON | Mages, priests, liches |
| **Controller** | INT, CHA | WIS | STR, DEX | Mind flayers, sirens |
| **Beast** | STR, CON | DEX | INT, WIS, CHA | Animals, elementals |

### Stat Scaling

```
primary_stat(level)   = 8 + level / 10     (cap 18)
secondary_stat(level) = 6 + level / 15     (cap 14)
weak_stat(level)      = 4 + level / 25     (cap 8)
```

| Level | Primary | Secondary | Weak |
|-------|---------|-----------|------|
| 1     | 8       | 6         | 4    |
| 10    | 9       | 7         | 4    |
| 20    | 10      | 7         | 5    |
| 33    | 11      | 8         | 5    |
| 50    | 13      | 9         | 6    |
| 66    | 15      | 10        | 7    |
| 80    | 16      | 11        | 7    |
| 99    | 18      | 13        | 8    |

**Role stat bonuses:** Elite +1 to primary, Champion +2, Boss +3, Raid +4 (can exceed 18, cap 22).

---

## Encounter Balance

### Rounds to Kill (Player vs Normal Mob, Same Level)

Using Uncommon T1 weapon damage from the [Equipment Framework](../items/equipment-framework.md):

| Level | Player DPS (T1 Uncommon) | Normal Mob HP | Rounds (~4s each) |
|-------|------------------------|---------------|-------------------|
| 10    | 1.0                    | 60            | ~60 rounds        |
| 20    | 1.9                    | 140           | ~74 rounds        |
| 33    | 3.5                    | 274           | ~78 rounds        |
| 50    | 5.8                    | 500           | ~86 rounds        |
| 99    | 17.9                   | 1,475         | ~82 rounds        |

These are intentionally long for solo play with Uncommon gear. With Rare/Epic weapons, Attack Power bonuses, and abilities (not just auto-attacks), actual kill times are much shorter:

| Level | Realistic Solo DPS (T1, Rare + abilities) | Normal Mob HP | Time |
|-------|------------------------------------------|---------------|------|
| 10    | ~4                                       | 60            | ~15s |
| 33    | ~12                                      | 274           | ~23s |
| 50    | ~22                                      | 500           | ~23s |
| 99    | ~50                                      | 1,475         | ~30s |

**Design target:** A same-level Normal mob should take **15-30 seconds** to kill solo with level-appropriate gear and active ability use.

### Rounds to Kill (Normal Mob vs Player, Same Level)

Using Normal Paladin HP (CON 10) from `stat-progression.md`, with Heavy armor DR%:

| Level | Mob DPR (1 atk) | After DR% | Player HP (Paladin) | Survival Time |
|-------|-----------------|-----------|--------------------|--------------|
| 10    | 9               | 8 (14% DR) | 110               | ~55s         |
| 33    | 27              | 19 (31% DR) | 329              | ~69s         |
| 50    | 42              | 29 (30% DR) | 465              | ~64s         |
| 99    | 91              | 57 (37% DR) | 857              | ~60s         |

**Design target:** A same-level Normal mob should take **45-90 seconds** to kill an unhealable player. Long enough to feel fair, short enough to feel dangerous.

### Party vs Boss (Level 50, Rare Quality)

Full party of 5 vs a L50 Boss (7,500 HP, 84 damage, 2-3 attacks):

| Role | DPS Contribution | Notes |
|------|-----------------|-------|
| Clint (Tank) | ~15 | Holding aggro, mitigating |
| Selene (DPS) | ~25 | Burst windows, positioning |
| Vanessa (DPS) | ~30 | Spell damage, area control |
| Rebekah (Support) | ~10 | Buffs increasing party DPS |
| Wade (Healer) | ~5 | Keeping tank alive |
| **Total Party DPS** | **~85** | |

- **Time to kill Boss:** 7,500 / 85 = ~88 seconds
- **Boss DPR (2.5 avg attacks):** 84 × 2.5 = 210. After Clint's DR (30%): 147/round
- **Clint survival without healing:** 465 / 147 = ~3.2 rounds (~13 seconds)
- **With Wade healing ~40/s:** (147 - 40) = 107 net. 465 / 107 = ~4.3 rounds (~17 seconds)
- **Fight requires:** Active mitigation, healer attention, DPS uptime

This creates a tense ~90 second boss fight where the tank is under pressure, the healer must stay focused, and DPS needs to perform.

### Party (Boosted) vs Boss (Level 50)

Same boss, but with the party's console-boosted stats:

- **Clint HP:** 1,684. After DR: 147/round. Without healing: ~46 seconds. With healing: ~75 seconds.
- **Total DPS with Unique weapons:** ~150+
- **Time to kill:** 7,500 / 150 = ~50 seconds

The boosted party handles the same boss much more comfortably. They can survive mistakes and push damage harder. This is the intended power fantasy -- challenging content becomes achievable, not trivial.

---

## K-Band Design Notes

### K1 (Levels 1-33): Learning

- Normal mobs are the primary encounter type
- Elites appear as zone capstones or guarded areas
- First Bosses appear around L20-25
- Mechanics are simple: dodge the telegraph, don't stand in fire
- Party learns roles (tank, heal, DPS) during this band
- **Mob density:** High. Fast leveling with many targets.

### K2 (Levels 34-66): Specialization

- Normal mobs require some attention; can't just auto-attack through
- Elites are regular encounters in dangerous zones
- Champions guard dungeon wings and key objectives
- Boss mechanics become multi-phase; require coordination
- **Mob density:** Moderate. Quality encounters over quantity.

### K3 (Levels 67-99): Mastery

- Normal mobs hit hard enough to threaten careless players
- Champions are standard dungeon content
- Bosses have complex scripted encounters
- Raid bosses appear as world-threatening events
- Mob abilities interact with each other (healer + DPS pairs, buff combos)
- **Mob density:** Focused. Every encounter is designed, not filler.

---

## Experience Points

```
mob_xp(level) = 100 + 5 * level²
```

| Level | Normal | Elite | Champion | Boss | Raid |
|-------|--------|-------|----------|------|------|
| 1     | 105    | 315   | 1,050    | 2,625 | 7,875 |
| 10    | 600    | 1,800 | 6,000    | 15,000 | 45,000 |
| 20    | 2,100  | 6,300 | 21,000   | 52,500 | 157,500 |
| 33    | 5,545  | 16,635 | 55,450  | 138,625 | 415,875 |
| 50    | 12,600 | 37,800 | 126,000 | 315,000 | 945,000 |
| 66    | 21,880 | 65,640 | 218,800 | 547,000 | 1,641,000 |
| 99    | 49,105 | 147,315 | 491,050 | 1,227,625 | 3,682,875 |

XP scales quadratically, making higher-level mobs significantly more rewarding. Role multipliers ensure that harder fights give proportionally better rewards.

---

## Loot and Drops

Mob role determines the quality ceiling of dropped items.

| Role | Max Drop Quality | Notes |
|------|-----------------|-------|
| Minion | Trash | Vendor fodder only |
| Normal | Common | Standard gear, materials |
| Elite | Uncommon | Named items, useful upgrades |
| Champion | Rare | Dungeon-quality gear |
| Boss | Epic | Best-in-slot for the zone's level range |
| Raid | Legendary | Endgame items with unique abilities |

Unique items cannot drop -- they exist outside the system (see [Equipment Framework](../items/equipment-framework.md)).

---

## Complete Formula Reference

```python
# === BASE STATS (Normal Role) ===
mob_hp(level)      = 5 * level + 0.1 * level²
mob_damage(level)  = 2 + 0.7 * level + 0.002 * level²
mob_accuracy(level)= 5 + 0.5 * level
mob_ar(level)      = 0.5 * level + 0.005 * level²
mob_xp(level)      = 100 + 5 * level²

# === ATTRIBUTES (1-20 scale) ===
primary_stat(level)   = 8 + level / 10     # cap 18
secondary_stat(level) = 6 + level / 15     # cap 14
weak_stat(level)      = 4 + level / 25     # cap 8

# === ROLE MULTIPLIERS ===
#          HP     Dmg    Atks   XP     Accuracy Bonus
# Minion:  0.25x  0.5x   1      0.25x  +0
# Normal:  1.0x   1.0x   1      1.0x   +0
# Elite:   2.5x   1.25x  1-2    3.0x   +0
# Champion:6.0x   1.5x   2      10.0x  +0
# Boss:    15.0x  2.0x   2-3    25.0x  +5
# Raid:    40.0x  2.5x   3-5    75.0x  +10

# === DEFENSE ===
# Uses player DR% formula: DR% = AR / (AR + K)
# K = {K1 (1-33): 50, K2 (34-66): 100, K3 (67-99): 200}
```

---

## Open Questions

- **Spell-casting mobs:** How do caster mob abilities interact with the damage formula? Should spells replace or supplement auto-attacks?
- **Flee/morale:** Should mobs below a certain HP% attempt to flee or call for reinforcements?
- **Aggro radius:** How does mob detection range scale with level and Perception stat?
- **Respawn timers:** How quickly should mobs respawn? Should Bosses have longer lockouts?
- **Level scaling:** Should any mobs scale to the player's level, or is all content fixed-level?
- **XP-to-level curve:** The XP rewards are defined here, but the XP required per level needs its own document.
