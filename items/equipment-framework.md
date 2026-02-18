---
canon: true
stability: evolving
last_reviewed: 2026-02-18
---

# Equipment Framework

Defines the item budget system, quality tiers, and progression targets for weapons and armor in Quantum Error. All equipment gets a **total power budget** that scales with level, split between the item's primary function (damage or armor) and secondary stat bonuses.

Adapted from analysis of legacy MUD equipment data. See `system/stats.md` for attribute definitions and `system/combat.md` for the damage pipeline.

---

## Quality Tiers

Every item has a quality tier that multiplies its total budget.

| Quality | Multiplier | Color | Use Case |
|---------|-----------|-------|----------|
| **Trash** | 0.4x | Grey | Vendor fodder, generic mob drops |
| **Common** | 0.7x | White | Basic quest rewards, standard gear |
| **Uncommon** | 1.0x | Green | Good quest rewards, crafted items |
| **Rare** | 1.3x | Blue | Dungeon boss drops, named items |
| **Epic** | 1.7x | Purple | Best-in-slot zone rewards, rare world drops |
| **Legendary** | 2.2x | Gold | Best-in-slot endgame, master-crafted artifacts |
| **Unique** | N/A | Red | Items outside the framework entirely |

Legendary is the highest tier the system can produce. Legendary items are rare, often one-of-a-kind, and may have unique abilities.

**Unique items** exist outside the budget system. They were created by exploiting or bypassing the system itself (e.g., direct source code modification via console access). The framework cannot classify, replicate, or constrain them. Their stats exceed the theoretical maximum of any Legendary item. Do not use Unique items as design templates -- they are narrative artifacts, not balance targets. Examples: [Katsuragi](weapons/katsuragi.md), [Aegis of Decoherent Deflection](armor/aegis-of-decoherent-deflection.md).

---

## Item Budget System

### Base Budget Formula

```
base_budget(level) = 1 + 0.15 * level + 0.001 * level²
total_budget = base_budget(level) * quality_multiplier
```

| Level | Base | Trash | Common | Uncommon | Rare | Epic | Legendary |
|-------|------|-------|--------|----------|------|------|-----------|
| 1     | 1.2  | 0.5   | 0.8    | 1.2      | 1.5  | 2.0  | 2.6       |
| 10    | 2.6  | 1.0   | 1.8    | 2.6      | 3.4  | 4.4  | 5.7       |
| 20    | 4.4  | 1.8   | 3.1    | 4.4      | 5.7  | 7.5  | 9.7       |
| 33    | 7.0  | 2.8   | 4.9    | 7.0      | 9.2  | 12.0 | 15.5      |
| 50    | 11.0 | 4.4   | 7.7    | 11.0     | 14.3 | 18.7 | 24.2      |
| 66    | 15.3 | 6.1   | 10.7   | 15.3     | 19.8 | 26.0 | 33.6      |
| 80    | 19.4 | 7.8   | 13.6   | 19.4     | 25.2 | 33.0 | 42.7      |
| 99    | 25.7 | 10.3  | 18.0   | 25.7     | 33.3 | 43.6 | 56.5      |

### Stat Point Costs

Stat points left over after the primary allocation (damage or AR) buy secondary bonuses.

| Stat | Cost (SP) | Notes |
|------|-----------|-------|
| +1 Primary Attribute (STR/DEX/INT/WIS/CON/CHA) | 1.0 | Base unit |
| +1 Accuracy | 1.0 | To-hit rating |
| +1 Attack Power | 1.5 | Flat damage bonus, higher impact |
| +10 HP | 1.0 | Standard health increment |
| +12 [Mana](../system/mana.md) | 1.0 | Caster resource |
| +15 Stamina | 1.0 | Physical resource |
| +1 AR (on non-armor slot) | 0.5 | Defensive stat on offensive item |
| -1 Saving Throw | 0.3 | Niche defensive stat |
| +1 Luck | 2.0 | Rare; Luck is powerful and scarce |

---

## Weapons

### Weapon Class Tiers

Class tier determines what percentage of the weapon budget goes to damage vs stats. All tiers get the **same total budget** -- lower-damage tiers get more stats instead.

| Tier | Damage % | Stat % | Classes |
|------|----------|--------|---------|
| **T1 - Primary Melee** | 80% | 20% | Paladin of the System, Necromancer (melee forms) |
| **T2 - Hybrid** | 65% | 35% | Temporal Bard, Cleric of Healing |
| **T3 - Light Melee** | 50% | 50% | Veilstepper Rogue |
| **T4 - Caster** | 35% | 65% | Quantum Sorceress, Mind Mage, Necromancer (casting) |

**Design intent:** T4 casters deal most of their damage through spells. Their weapons are stat sticks that provide Intelligence, Mana, and utility -- not raw weapon damage.

### Weapon Speed

Per-hit damage scales with attack interval so that **DPS stays constant** across weapon speeds. Faster weapons proc on-hit effects more often; slower weapons hit harder per swing.

```
per_hit_damage = base_damage * (speed_seconds / 4.0)
```

| Speed | Interval | Per-Hit Mult | Examples |
|-------|----------|-------------|---------|
| Very Fast | 2.5s | 0.625x | Daggers, knuckles -- more procs |
| Fast | 3.0s | 0.750x | Short swords, rapiers |
| Medium | 4.0s | 1.000x | Longswords, maces (baseline) |
| Slow | 5.0s | 1.250x | Greatswords, battleaxes |
| Very Slow | 6.0s | 1.500x | Mauls, polearms -- bigger crits |

### Damage Formula

```
damage_per_sp(level) = 2 + 0.02 * level
weapon_damage = base_budget(L) * quality * tier_dmg% * damage_per_sp(L)
```

### Target Damage Table (T1 Primary Melee, Medium Speed)

| Level | Trash | Common | Uncommon | Rare | Epic | Legendary |
|-------|-------|--------|----------|------|------|-----------|
| 1     | 0.7   | 1.1    | 1.6      | 2.1  | 2.8  | 3.6       |
| 10    | 1.6   | 2.8    | 4.0      | 5.2  | 6.8  | 8.8       |
| 20    | 3.0   | 5.2    | 7.4      | 9.6  | 12.6 | 16.3      |
| 33    | 5.5   | 9.6    | 13.8     | 17.9 | 23.4 | 30.2      |
| 50    | 9.2   | 16.2   | 23.1     | 30.0 | 39.3 | 50.9      |
| 66    | 14.3  | 25.0   | 35.8     | 46.5 | 60.8 | 78.7      |
| 80    | 19.6  | 34.2   | 48.9     | 63.6 | 83.1 | 107.5     |
| 99    | 28.6  | 50.0   | 71.5     | 92.9 | 121.5| 157.2     |

*Values are average damage per hit at Medium speed.*

**Other tiers:** multiply by T2 = 0.8125, T3 = 0.625, T4 = 0.4375.

### Target Damage by Class Tier (Uncommon Quality)

| Level | T1 Melee | T2 Hybrid | T3 Light | T4 Caster |
|-------|----------|-----------|----------|-----------|
| 1     | 1.6      | 1.3       | 1.0      | 0.7       |
| 10    | 4.0      | 3.2       | 2.5      | 1.7       |
| 33    | 13.8     | 11.2      | 8.6      | 6.0       |
| 50    | 23.1     | 18.8      | 14.4     | 10.1      |
| 66    | 35.8     | 29.1      | 22.4     | 15.7      |
| 80    | 48.9     | 39.7      | 30.6     | 21.4      |
| 99    | 71.5     | 58.1      | 44.7     | 31.3      |

### Weapon Examples

**Level 50 Rare Longsword (T1, Medium speed):**
- Total budget: 14.3 SP
- Damage: 14.3 x 80% x 3.0 = **34.3 avg** (6d10 ~ 33.0)
- Stats: 14.3 x 20% = 2.9 SP -> +1 Attack Power, +1 Accuracy, +5 HP

**Level 50 Rare Dagger (T3 Rogue, Very Fast):**
- Total budget: 14.3 SP
- Damage: 14.3 x 50% x 3.0 x 0.625 = **13.4 avg** (3d8 ~ 13.5)
- Stats: 14.3 x 50% = 7.2 SP -> +2 DEX, +1 Accuracy, +2 Attack Power, +10 HP
- DPS: 13.4 / 2.5 = 5.4 per weapon (dual-wield for more)

**Level 50 Rare Staff (T4 Caster, Slow):**
- Total budget: 14.3 SP
- Damage: 14.3 x 35% x 3.0 x 1.25 = **18.8 avg** (3d12 ~ 19.5)
- Stats: 14.3 x 65% = 9.3 SP -> +2 INT, +23 HP, +36 Mana

**[Katsuragi](weapons/katsuragi.md) (Unique -- outside framework):**
- Quality: Unique (system console exploit). Does not follow budget rules.
- See [Katsuragi](weapons/katsuragi.md) for stats. Do not use as a design template.

---

## Armor

### Armor Class Tiers

| Tier | AR % | Stat % | Classes |
|------|------|--------|---------|
| **Heavy** | 85% | 15% | [Paladin of the System](../classes/paladin-of-the-system.md) |
| **Medium** | 65% | 35% | [Cleric of Healing](../classes/cleric-of-healing.md), [Temporal Bard](../classes/temporal-bard.md), [Necromancer](../classes/necromancer.md) |
| **Light** | 45% | 55% | [Veilstepper Rogue](../classes/veilstepper-rogue.md) |
| **Cloth** | 25% | 75% | [Quantum Sorceress](../classes/quantum-sorceress.md), [Mind Mage](../classes/mind-mage.md) |

### Armor Slots and Weights

Full set = 8 slots. Slot weight determines what fraction of the total set budget each piece gets.

| Slot | Weight | Notes |
|------|--------|-------|
| Body | 28% | Chestpiece -- largest single piece |
| Head | 12% | Helmets, circlets, hoods |
| Legs | 12% | Greaves, leggings, robes |
| Arms | 10% | Bracers, sleeves |
| Hands | 8% | Gloves, gauntlets |
| Feet | 10% | Boots, sandals |
| About | 10% | Cloaks, tabards |
| Waist | 10% | Belts, sashes |

### AR and Damage Reduction

Armor Rating (AR) converts to Damage Reduction (DR%) using a diminishing-returns formula tied to [K-bands](../system/stats.md):

```
DR% = AR / (AR + K)
```

| K-Band | Levels | K Value | Design Intent |
|--------|--------|---------|---------------|
| K1 | 1-33 | 50 | Fast early progression, mistakes survivable |
| K2 | 34-66 | 100 | Mid-game; specialization matters |
| K3 | 67-99 | 200 | Late-game; heroic scaling, layered defense |

DR% drops at K-band boundaries by design. This prevents power creep and ensures that late-game armor feels meaningful without making characters invincible.

### Target Full-Set AR and DR%

| Level | Heavy AR | DR% | Medium AR | DR% | Light AR | DR% | Cloth AR | DR% |
|-------|---------|-----|----------|-----|---------|-----|---------|-----|
| 1     | 4       | 7%  | 3        | 6%  | 2       | 4%  | 1       | 2%  |
| 10    | 8       | 14% | 6        | 11% | 4       | 7%  | 2       | 4%  |
| 20    | 14      | 22% | 11       | 18% | 8       | 14% | 4       | 7%  |
| 33    | 22      | 31% | 17       | 25% | 12      | 19% | 7       | 12% |
| 50    | 43      | 30% | 33       | 25% | 23      | 19% | 13      | 12% |
| 66    | 55      | 35% | 42       | 30% | 29      | 22% | 16      | 14% |
| 80    | 85      | 30% | 65       | 25% | 45      | 18% | 25      | 11% |
| 99    | 118     | 37% | 91       | 31% | 63      | 24% | 35      | 15% |

*DR% resets at K-band transitions (L33->L34, L66->L67) as K increases.*

### AR Formula

```
ar_per_sp(level) = 1 + 0.01 * level
armor_ar = base_budget(L) * quality * tier_ar% * ar_per_sp(L) * slot_weight
```

### Armor Examples

**Level 50 Rare Plate Chestpiece (Heavy, Body slot):**
- Total budget: 14.3 SP
- AR: 14.3 x 85% x 1.5 x 0.28 = **5.1 AR** (this piece)
- Stats: 14.3 x 15% = 2.1 SP -> +2 CON
- Full rare heavy set at 50: ~56 AR -> DR% = 36%

**Level 50 Rare Leather Vest (Light, Body slot):**
- Total budget: 14.3 SP
- AR: 14.3 x 45% x 1.5 x 0.28 = **2.7 AR** (this piece)
- Stats: 14.3 x 55% = 7.9 SP -> +2 DEX, +1 Accuracy, +1 Attack Power, +20 HP
- Full rare light set at 50: ~30 AR -> DR% = 23%

**Level 50 Rare Wizard Robe (Cloth, Body slot):**
- Total budget: 14.3 SP
- AR: 14.3 x 25% x 1.5 x 0.28 = **1.5 AR** (this piece)
- Stats: 14.3 x 75% = 10.7 SP -> +3 INT, +36 Mana, +20 HP
- Full rare cloth set at 50: ~17 AR -> DR% = 15%
- Casters supplement with spell-based Ward% (mage armor, shields, etc.)

---

## Defense Layers

Survivability comes from stacking multiple defensive layers, not just high AR. Each role relies on a different mix.

| Layer | Source | Example |
|-------|--------|---------|
| **DR%** | Armor Rating | Physical damage reduction from gear |
| **Ward%** | Spells/Enchantments | Magical damage reduction (mage armor, shields) |
| **Evasion** | DEX + Light Armor | Chance to dodge attacks entirely |
| **Block** | Shield | Chance to negate/reduce an attack |
| **Parry** | Weapon Skill | Chance to deflect melee attacks |
| **Soak** | Heavy Armor | Flat damage reduction per hit |

### Effective Mitigation by Role (Level 50, Rare Quality)

| Role | AR | DR% | Ward% | Soak | Block% | Parry% | Dodge% | Eff. Mitigation |
|------|-----|-----|-------|------|--------|--------|--------|--------------------|
| Heavy (Paladin) | 56 | 36% | 0% | 5 | 25% | 20% | 5% | ~72% |
| Medium (Cleric/Bard) | 33 | 25% | 0% | 2 | 0% | 20% | 15% | ~58% |
| Light (Rogue) | 30 | 23% | 0% | 0 | 0% | 15% | 25% | ~55% |
| Cloth (Sorceress) | 17 | 15% | 30% | 0 | 0% | 0% | 10% | ~52% |

*Eff. Mitigation combines avoidance and reduction. Casters rely on Ward% from spells to reach parity.*

---

## Complete Formula Reference

```python
# === SHARED ===
base_budget(level) = 1 + 0.15 * level + 0.001 * level²
quality_mult = {Trash: 0.4, Common: 0.7, Uncommon: 1.0, Rare: 1.3,
                Epic: 1.7, Legendary: 2.2, Unique: N/A (outside budget)}

# === WEAPONS ===
damage_per_sp(level) = 2 + 0.02 * level
weapon_damage = base_budget(L) * quality * weapon_tier_dmg% * damage_per_sp(L)
weapon_dps    = weapon_damage / speed_seconds
weapon_stats  = base_budget(L) * quality * (1 - weapon_tier_dmg%)
speed_scaling = speed_seconds / 4.0   # multiply per-hit damage

weapon_tier = {T1: 0.80, T2: 0.65, T3: 0.50, T4: 0.35}

# === ARMOR ===
ar_per_sp(level) = 1 + 0.01 * level
armor_ar    = base_budget(L) * quality * armor_tier_ar% * ar_per_sp(L) * slot_weight
armor_stats = base_budget(L) * quality * (1 - armor_tier_ar%)
slot_weight = {Body: 0.28, Head: 0.12, Legs: 0.12, Arms: 0.10,
               Hands: 0.08, Feet: 0.10, About: 0.10, Waist: 0.10}

armor_tier = {Heavy: 0.85, Medium: 0.65, Light: 0.45, Cloth: 0.25}

# === DEFENSE ===
DR% = AR / (AR + K)
K   = {K1 (1-33): 50, K2 (34-66): 100, K3 (67-99): 200}
```

---

## Open Questions

- **Shields:** Should shields be a separate slot or use the off-hand weapon slot? What AR budget do they get?
- **Accessories:** Rings, amulets, and trinkets (like the [Fanny Pack of Holding](accessories/fanny-pack-of-holding.md)) need their own budget rules -- likely stat-only with no AR.
- **Set Bonuses:** Should matching gear sets provide bonus effects? If so, how does this interact with the budget system?
- **Enchanting:** How does Clint's [Enchanting](../professions/enchanting.md) profession interact with quality tiers? Can it upgrade an item's quality, or does it add effects on top of the existing budget?
- **Ward% Sources:** Specific spell values for mage armor, shield, and other defensive spells need to be defined to validate the cloth caster mitigation targets.
- **Soak Values:** Flat damage reduction from heavy armor needs concrete per-level values.
