---
canon: true
stability: evolving
---

# Stats

Seven core attributes define character capabilities, ranging from 1 to 20.

## Strength

Physical power and brawn.

| Level | Description |
|-------|-------------|
| 1 | Minimal physical capability |
| 10 | Average human strength |
| 20 | Pinnacle of brawn; able to out-lift several people in a combined effort |

**Uses**: Resist movement restriction, direct strength contests (arm wrestling, breaking items)

## Dexterity

Agility, reflexes, and coordination.

| Level | Description |
|-------|-------------|
| 1 | Barely mobile; probably significantly paralyzed |
| 10 | Average human agility |
| 20 | Moves like water; reacting to all situations with almost no effort |

**Uses**: Dodge attack resistances

## Constitution

Physical resilience and endurance.

| Level | Description |
|-------|-------------|
| 1 | Minimal immune system |
| 10 | Average human resilience |
| 20 | Tireless paragon of physical endurance |

**Uses**: Illness resistance, fatigue recovery

## Intelligence

Knowledge, reasoning, and learning ability.

| Level | Description |
|-------|-------------|
| 1 | Animalistic; no longer capable of logic or reason |
| 10 | Average human intelligence |
| 20 | Famous as a sage and genius |

**Uses**: Knowledge checks, learning speed, magical theory

## Wisdom

Insight, perception, and intuition.

| Level | Description |
|-------|-------------|
| 1 | Seemingly incapable of thought |
| 10 | Average human perception |
| 20 | Nearly prescient; able to reason far beyond logic |

**Uses**: Reading people and situations

## Charisma

Social influence, personality, and presence.

| Level | Description |
|-------|-------------|
| 1 | Barely conscious; probably acts very alien |
| 10 | Average human charisma |
| 20 | Renowned for wit, personality, and/or looks |

**Uses**: Social influence, likability, bard magic

## Luck

Fortune and circumstance.

| Level | Description |
|-------|-------------|
| 0 | World is against you |
| 10 | Average fortune |
| 20 | Luck of the gods |

**Uses**: Affects how circumstances align for the character

**Note**: Luck ranges from 0-20, unlike other stats which range from 1-20.

---

## Levels (1–99)

Attributes describe *what you are*; **levels** describe *how far you've progressed* in the system.

Canon intent:
- Levels scale to **99**.
- Attributes are still described on a **1–20** human-readable scale, but higher levels increase:
  - derived pools (HP/Mana/Stamina)
  - bonuses (accuracy/evasion, healing power, mitigation)
  - access to class features and scaling multipliers

### K-Bands (Current Canon)

For tuning and content scaling, we use **3 K-bands** as anchors:

- **K1 (1–33)**: early progression, fast learning, survivable mistakes
- **K2 (34–66)**: mid progression, specialization, build identity emerges
- **K3 (67–99)**: late progression, heroic scaling, boss mechanics matter

This is a design anchor for damage/mitigation curves and encounter design.

## Derived Pools

### Health (HP)
Represents survivability. HP scales primarily with:
- Level
- Constitution
- Class base HP multiplier

### Mana
Represents magical capacity. Mana scales primarily with:
- Level
- Class base mana multiplier
- Certain conditions (e.g., Mana Lucent) as exceptions

### Stamina (Optional)
If used, stamina fuels physical techniques and prolonged exertion.
If a class does not use stamina, treat it as flavor-only or omit it.

## Secondary Combat Stats (Conceptual)

These are common secondary stats referenced by class mechanics:

- **Accuracy**: chance to land attacks (see `combat.md`)
- **Evasion**: chance to avoid attacks (see `combat.md`)
- **Mitigation**: damage reduction via armor/resistance/soak
- **Healing Power**: increases heals and shielding
- **Threat**: influences enemy target selection

> Exact formulas are implementation-defined, but all class pages should describe their abilities using these common terms.
