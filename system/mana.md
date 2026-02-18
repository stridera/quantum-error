---
canon: true
stability: evolving
---

# Mana

Mana is the energy that powers all magic in the system.

## Pre-Transition: Null Mana Zone

Before the Transition, Earth existed as a **Null Mana Zone**:
- Mana did not naturally regenerate
- Magic could not be cast without manual intervention
- The party worked around this by manually setting mana values via the system console
- This limitation meant early experiments required careful mana management

## Post-Transition

When [Clint](../characters/party/clint.md) changed the world template from Technology to RPG:
- Mana began regenerating naturally worldwide
- Magic became fully functional
- Safe Zones maintain stable mana levels
- Mana density may vary by region (unconfirmed)

## Mana Conditions

### Mana Lucent

A permanent condition caused by severe mana overflow.

**Cause**: Vanessa accidentally set her mana to 99,999 instead of 999, triggering **Severe Mana Lock**. Clint reduced it to 9,999 to stabilize her, but the damage was done.

**[Effects](effects.md)**:
- Eyes glow permanently with mana energy
- Veins visibly glow, especially when casting
- Glow color changes based on spell being cast
- Enhanced mana perception
- Spells cast at higher effective level

**Known Afflicted**: [Vanessa](../characters/party/vanessa.md)

## Null Magic Zones

A Null Magic Zone is an area where ambient mana does not exist. These can occur naturally or be created artificially.

### Effects
- **No mana regeneration** — Ambient mana is absent; you cannot regenerate naturally
- **Spells require internal mana** — You can still cast, but must fuel spells entirely from your own mana pool
- **Enchantments go dormant** — Magical items lose their effects while inside the zone
- **Buffs/debuffs fade instantly** — Effects dissipate unless actively channeled using internal mana
- **Death is permanent** — If you die inside a Null Magic Zone, you cannot respawn *unless your body is removed from the zone*

### Strategic Implications

The key danger is resource attrition. A mage entering a Null Magic Zone has only their current mana pool to work with—no regeneration, no item bonuses. Extended combat becomes a war of attrition.

### Notable Uses

[Eron Vosk](../characters/villains/eron-vosk.md) created an artificial Null Magic Zone at his stronghold as a trap. His intention was to entomb the party where, if killed, they would never respawn.

However, Null Magic Zones also break persistent magical effects like mind control, which the party exploited to free [Amanda](../characters/supporting/amanda.md) from Eron's domination.

## Mana Costs

Standard mana costs vary by spell tier and class. See individual class files for specific ability costs.

| Tier | Typical Cost Range |
|------|-------------------|
| Cantrip | 0-5 |
| Basic | 10-20 |
| Intermediate | 25-40 |
| Advanced | 50-100 |
| Ultimate | 100+ |

## Spend Rules (Canonical)

### Minimum Cost
Every spell/ability that uses mana has a **minimum cost**. If a spell supports variable power, you may spend more than the minimum.

- If you cannot pay the minimum cost, the spell fails (fizzle) unless explicitly defined as a backlash spell.

### Variable Spend (Overchannel)
Some spells allow additional mana spend to increase magnitude.

If an ability supports variable spend, its definition must include:
- Minimum cost
- Maximum spend (or "up to current mana")
- Scaling rule (e.g., +X damage per +Y mana)

### Dumping the Pool (High-Risk Casting)
Spending a very large fraction of your pool at once is allowed **only if** the ability explicitly supports it.
When it happens, the system may apply consequences:

Common consequences (choose per ability/class):
- **Mana Burn**: temporary reduction to mana regen
- **Mana Lock**: cannot cast above a tier for a duration
- **Backlash Damage**: self-inflicted arcane damage
- **Mana Lucent Flare**: visible signature; enemies can detect caster easier

### Mana Lucent Interaction
Mana Lucent amplifies spell output, but also increases the likelihood/severity of overchannel consequences.
If an ability is cast while Mana Lucent, it should declare whether it:
- increases effective tier, or
- increases scaling coefficient, or
- increases critical chance for arcane spells

## Canon Note: Power Fantasy with Limits
Party members may have unusually large pools (e.g., 999 baseline; Vanessa larger),
but **resource risk** and **environmental constraints** (e.g., Null Magic Zones) preserve tension.
