---
canon: true
stability: evolving
last_reviewed: 2026-02-18
---

# Stat Progression

Defines HP, [Mana](mana.md), and Stamina progression formulas for all characters. See `stats.md` for attribute definitions and K-band boundaries.

Adapted from FieryMUD legacy source code (`class.cpp`, `constants.cpp`, `limits.cpp`).

---

## HP Progression

### Starting HP

All characters begin with **15 base HP** plus their first level-up roll at level 1.

### HP per Level

During K1 (levels 1-33), characters roll dice each level. At K2+ (levels 34-99), the gain becomes a fixed value. CON bonus is added every level.

| HP Group | Classes | K1 Roll (avg) | K2+ Fixed |
|----------|---------|---------------|-----------|
| **Heavy Melee** | Warrior, Berserker, Monk, Hunter | 8-13 (10.5) | 10 |
| **Paladin** | Paladin, Anti-Paladin | 7-12 (9.5) | 8 |
| **Ranger** | Ranger | 7-11 (9.0) | 8 |
| **Mercenary** | Mercenary | 5-12 (8.5) | 9 |
| **Rogue** | Thief, Rogue | 5-11 (8.0) | 6 |
| **Assassin** | Assassin | 5-10 (7.5) | 6 |
| **Druid** | Druid | 3-9 (6.0) | 6 |
| **WIS Caster** | Cleric, Shaman, Priest, Mystic | 3-8 (5.5) | 6 |
| **INT Caster** | Sorcerer, Necromancer, Conjurer, Bard, Illusionist | 1-6 (3.5) | 3 |

### CON HP Bonus

Applied every level on top of the base roll or fixed value. Uses the 1-20 attribute scale from `stats.md`.

| CON | Bonus/Level | Notes |
|-----|-------------|-------|
| 1-3 | -3 | Severe penalty |
| 4-6 | -2 | |
| 7-9 | -1 | Below average |
| 10-12 | 0 | Average human |
| 13-14 | +1 | |
| 15-16 | +2 | |
| 17-18 | +3 | |
| 19 | +4 | |
| 20 | +5 | Maximum |

### HP Table: Normal Characters (CON 10, average rolls)

| Class Group | L1 | L10 | L20 | L33 | L50 | L66 | L80 | L99 |
|-------------|-----|-----|-----|-----|-----|-----|-----|-----|
| Heavy Melee | 26 | 120 | 225 | 362 | 532 | 662 | 752 | 882 |
| Paladin | 25 | 110 | 205 | 329 | 465 | 593 | 705 | 857 |
| Ranger | 24 | 105 | 195 | 312 | 448 | 576 | 688 | 840 |
| Mercenary | 24 | 100 | 185 | 296 | 449 | 593 | 719 | 891 |
| Rogue | 23 | 95 | 175 | 279 | 381 | 477 | 561 | 675 |
| Assassin | 23 | 90 | 165 | 263 | 365 | 461 | 545 | 659 |
| Druid | 21 | 75 | 135 | 213 | 315 | 411 | 495 | 609 |
| WIS Caster | 21 | 70 | 125 | 197 | 299 | 395 | 479 | 593 |
| INT Caster | 19 | 50 | 85 | 131 | 182 | 231 | 273 | 329 |

### K-Band Kink

Some classes see a drop in HP gain rate at the K1-K2 boundary (L33 to L34) when the dice average exceeds the fixed value:

| Class | K1 Avg/Lv | K2+ Fixed/Lv | Change |
|-------|-----------|-------------|--------|
| Heavy Melee (Monk/Hunter) | 10.5 | 8 | -24% |
| Rogue | 8.0 | 6 | -25% |
| Assassin | 7.5 | 6 | -20% |

---

## Mana Progression

### Mana Formula

Mana is **accumulated** each level, just like HP. Characters start with **10 base mana** plus their first level-up roll at level 1.

### Mana per Level

During K1 (levels 1-33), characters roll dice each level. At K2+ (levels 34-99), the gain becomes a fixed value. No stat bonus applies to mana -- pool size is purely class-driven.

| Mana Group | Classes | K1 Roll (avg) | K2+ Fixed |
|------------|---------|---------------|-----------|
| **High** | Sorcerer, [Necromancer](../classes/necromancer.md), Conjurer, Illusionist | 7-13 (10) | 10 |
| **Medium** | [Cleric](../classes/cleric-of-healing.md), Bard, Shaman, Priest, Druid, Mystic | 4-10 (7) | 6 |
| **Low** | [Paladin](../classes/paladin-of-the-system.md), Ranger, [Rogue](../classes/veilstepper-rogue.md), Assassin | 2-7 (4.5) | 3 |
| **Minimal** | Warrior, Berserker, Monk, Mercenary, Hunter, Thief | 1-4 (2.5) | 2 |

### Mana Table: Normal Characters

| Mana Group | L1 | L10 | L20 | L33 | L50 | L66 | L80 | L99 |
|------------|-----|-----|-----|-----|-----|-----|-----|-----|
| High | 20 | 110 | 210 | 340 | 510 | 670 | 810 | 1,000 |
| Medium | 17 | 80 | 150 | 241 | 343 | 439 | 523 | 637 |
| Low | 15 | 55 | 100 | 159 | 210 | 258 | 300 | 357 |
| Minimal | 13 | 35 | 60 | 93 | 127 | 159 | 187 | 225 |

Casters are differentiated by pool size. A High caster at L99 has ~1,000 mana (enough for 10 Ultimate casts). A Minimal martial has ~225 (enough for a few special abilities).

See `mana.md` for cost tiers (Cantrip 0-5, Basic 10-20, Intermediate 25-40, Advanced 50-100, Ultimate 100+).

---

## Stamina (Move)

### Starting Stamina

```
base_stamina = max(100, CON * 10)
```

At CON 10 (average): 100. At CON 20 (max): 200.

### Per-Level Gains (K1 only, levels 1-33)

Stamina stops growing after K1. It represents physical conditioning, not heroic scaling.

| Component | Bonus |
|-----------|-------|
| Base | +2/level |
| Rogue or Cleric class | +1/level (total +3) |
| DEX 13-16 | +1/level |
| DEX 17+ | +2/level |

### Stamina at L33+ (CON 10)

| Scenario | L33 Stamina | Notes |
|----------|------------|-------|
| Standard, DEX < 13 | 166 | Base only |
| Standard, DEX 13-16 | 199 | +DEX bonus |
| Standard, DEX 17+ | 232 | +DEX bonus |
| Rogue/Cleric, DEX 17+ | 265 | Class + DEX |

Stamina is relatively flat compared to HP. It's a minor resource -- a non-factor in class balance.

---

## Regen Rates

### HP Regen per Tick

```
base_regen = (max_hp * 0.05) + regen_bonus + 2
```

**Position multipliers:**

| Position | Multiplier |
|----------|-----------|
| Sleeping | 5x |
| Resting | 3x |
| Sitting | 1.5x |
| Standing | 1x |
| Fighting | 0.5x |

**Class regen factor:**

| Factor | Classes |
|--------|---------|
| 100% | All martial classes (Warrior, Paladin, Ranger, Rogue, etc.) |
| 85% | Druid |
| 80% | All casters (Sorcerer, Cleric, Necromancer, etc.) |

**Race modifiers:**
- [Troll](../races/troll.md): 2x HP regen

---

## Main Party Progression

The main party members had their stats boosted via the system console before the Transition. Their base pools (999 HP, 999 Mana) are permanent overrides that exist outside the normal formulas. Progression from L2 onward follows normal rules, adding on top of the boosted base.

> **System Note:** These characters' starting pools were set by directly modifying source code. The system tracks them as valid but cannot explain or replicate them. They are the stat equivalent of [Unique items](../items/equipment-framework.md).

### Party Class Mapping

| Character | Class | HP Group | Mana Group | CON | CON Bonus |
|-----------|-------|----------|------------|-----|-----------|
| Clint | Paladin of the System | Paladin | Low | 20 | +5 |
| Vanessa | Quantum Sorceress | INT Caster | High | 20 | +5 |
| Rebekah | Temporal Bard | INT Caster | Medium | 20 | +5 |
| Selene | Veilstepper Rogue | Rogue | Low | 20 | +5 |
| Wade | Cleric of Healing | WIS Caster | Medium | 20 | +5 |

### Party Per-Level Gains

| Character | HP K1/Lv | HP K2+/Lv | Mana K1/Lv | Mana K2+/Lv |
|-----------|---------|----------|-----------|------------|
| Clint | 14.5 | 13 | 4.5 | 3 |
| Vanessa | 8.5 | 8 | 10.0 | 10 |
| Rebekah | 8.5 | 8 | 7.0 | 6 |
| Selene | 13.0 | 11 | 4.5 | 3 |
| Wade | 10.5 | 11 | 7.0 | 6 |

### Party HP by Level

Starting from 999 HP at L1. Normal gains from L2 onward.

| Character | L1 | L10 | L20 | L33 | L50 | L66 | L80 | L99 |
|-----------|-----|------|------|------|------|------|------|------|
| **Clint** | 999 | 1,130 | 1,275 | 1,463 | 1,684 | 1,892 | 2,074 | 2,321 |
| **Selene** | 999 | 1,116 | 1,246 | 1,415 | 1,602 | 1,778 | 1,932 | 2,141 |
| **Wade** | 999 | 1,094 | 1,199 | 1,335 | 1,522 | 1,698 | 1,852 | 2,061 |
| **Vanessa** | 999 | 1,076 | 1,161 | 1,271 | 1,407 | 1,535 | 1,647 | 1,799 |
| **Rebekah** | 999 | 1,076 | 1,161 | 1,271 | 1,407 | 1,535 | 1,647 | 1,799 |

### Party vs Normal HP at Level 99

| Character | Party HP (L99) | Normal Equivalent (CON 10) | Advantage |
|-----------|---------------|---------------------------|-----------|
| Clint | 2,321 | 857 (Paladin) | 2.7x |
| Selene | 2,141 | 675 (Rogue) | 3.2x |
| Wade | 2,061 | 593 (WIS Caster) | 3.5x |
| Vanessa | 1,799 | 329 (INT Caster) | 5.5x |
| Rebekah | 1,799 | 329 (INT Caster) | 5.5x |

The advantage comes from two sources: the +974 to +980 HP console boost at L1, and the +5 CON bonus per level from maxed Constitution. The gap is largest for INT casters whose normal HP is very low.

### Party Mana by Level

Starting from 999 Mana at L1 (Vanessa: 9,999). Normal accumulated gains from L2 onward.

| Character | L1 | L10 | L20 | L33 | L50 | L66 | L80 | L99 |
|-----------|-----|------|------|------|------|------|------|------|
| **Vanessa** | 9,999 | 10,089 | 10,189 | 10,319 | 10,489 | 10,649 | 10,789 | 10,979 |
| **Rebekah** | 999 | 1,062 | 1,132 | 1,223 | 1,325 | 1,423 | 1,507 | 1,621 |
| **Wade** | 999 | 1,062 | 1,132 | 1,223 | 1,325 | 1,423 | 1,507 | 1,621 |
| **Clint** | 999 | 1,040 | 1,085 | 1,143 | 1,194 | 1,243 | 1,285 | 1,341 |
| **Selene** | 999 | 1,040 | 1,085 | 1,143 | 1,194 | 1,243 | 1,285 | 1,341 |

### Party vs Normal Mana at Level 99

| Character | Party Mana (L99) | Normal Equivalent | Advantage |
|-----------|-----------------|-------------------|-----------|
| Vanessa | 10,979 | 1,000 (High) | 11.0x |
| Rebekah | 1,621 | 637 (Medium) | 2.5x |
| Wade | 1,621 | 637 (Medium) | 2.5x |
| Clint | 1,341 | 357 (Low) | 3.8x |
| Selene | 1,341 | 357 (Low) | 3.8x |

The 999 mana base gives the party a large early advantage that narrows as they level. By L99, non-Vanessa members are 2.5-3.8x above normal -- meaningful but not absurd. Vanessa's 9,999 from the Mana Lucent incident keeps her permanently at 11x, making her the party's dominant caster resource.

---

## Appendix: Quick Reference Formulas

```python
# === HP ===
starting_hp = 15

# Per level (K1, levels 1-33): roll between min and max for class group
# Per level (K2+, levels 34-99): fixed value for class group
# CON bonus added every level

# CON bonus (1-20 scale):
# CON 1-3: -3, CON 4-6: -2, CON 7-9: -1, CON 10-12: 0
# CON 13-14: +1, CON 15-16: +2, CON 17-18: +3, CON 19: +4, CON 20: +5

# === MANA ===
starting_mana = 10
# Per level (K1, levels 1-33): roll between min and max for class mana group
# Per level (K2+, levels 34-99): fixed value for class mana group
# No stat bonus on mana -- pool size is purely class-driven
# Mana groups: High (7-13/10), Medium (4-10/6), Low (2-7/3), Minimal (1-4/2)

# === STAMINA ===
base_stamina = max(100, CON * 10)
# +2/level during K1 (1-33), no gains after K1
# +1/level if Rogue or Cleric
# +1/level if DEX 13-16, +2/level if DEX 17+

# === REGEN ===
hp_regen = (max_hp * 0.05 + regen_bonus + 2) * position_mult * class_factor
# position: sleep 5x, rest 3x, sit 1.5x, stand 1x, fight 0.5x
# class: martial 100%, druid 85%, caster 80%
```
