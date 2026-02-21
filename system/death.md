---
canon: true
stability: evolving
---

# Death & Respawn

This page defines what happens when a character dies, the ghost state, corpse mechanics, resurrection, and binding.

## Death

When HP reaches 0, the character dies. There is no "downed" or "bleeding out" state — 0 HP is dead.

### Ghost State

On death, the character becomes a **ghost** anchored to their corpse. Ghosts:

- **Cannot move** from their corpse location.
- **Cannot interact** with the living world.
- **Perception of the living world drops to near zero.** You can't scout, spy, or gather useful information while dead. Dying is not a tactical tool.
- **Perception of "the other side" increases.** Ghosts may see or sense things invisible to the living — spirits, echoes, system-layer phenomena. This is rare and narratively significant when it occurs.
- **Have a timer** matching their corpse decay (see below). The ghost knows exactly how long they have before their corpse — and their gear — is gone.

### The Choice

While in ghost state, the character has two options:

1. **Wait for resurrection.** Stay as a ghost and hope a rezzer reaches your corpse in time. If resurrected, you return to your body with all equipped gear intact.
2. **Release.** Respawn at your bind point (default: nearest safe zone). You lose all non-soulbound equipment, which remains on your corpse. Once you release, **you can no longer be resurrected** — the ghost is gone.

This is a trust decision. If your healer is alive and fighting, do you wait? If the party is wiping, do you release and start running back? Every second waiting is a second not spent on the corpse run.

## Corpse

### Gear

All non-soulbound equipment stays on the corpse. Soulbound items return with the player on release.

### Decay Timer

Corpses persist for **24 hours**, then decay along with all gear on them. The ghost timer matches this — if you haven't been rezzed or released within 24 hours, you auto-release and the gear is gone.

24 hours is long enough to organize a recovery effort, but short enough to create urgency. A death deep in high-level territory means the clock is ticking.

### Multiple Corpses

If you die on your corpse run, you now have **two corpses** with gear on them, each with their own 24-hour timer. Death spirals are real — each failed recovery attempt scatters your equipment across increasingly dangerous territory.

### Corpse Recovery

- **Corpse run:** The default. Run back to your body from your bind point, naked or in soulbound gear only. The [aggro system](aggro.md) makes this proportionally harder the further you died from safety.
- **Necromancer summoning:** Necromancers in safe zones can summon a corpse to their location as a professional service. Cost and availability vary. This is a major part of the necromancer service economy.
- **Party assistance:** Other players can escort you on a corpse run, or a rezzer can travel to your corpse and resurrect you there.

## Resurrection

Resurrection restores a ghost to life at their corpse, preserving all equipped gear. It requires the rezzer to be **physically at the corpse** and to channel the spell.

### Key Rules

- **Target must be in ghost state.** If they've released, rez cannot help them.
- **Rezzer must be at the corpse.** No remote resurrection.
- **All resurrection requires channel time.** This is never instant. Rezzing mid-combat means the rezzer is doing nothing else — not healing, not fighting, not dodging.
- **Rez sickness applies.** The resurrected character returns with reduced stats for a duration, scaling with the quality of the rez. You are never at full strength immediately after being brought back.

### Rez Progression

Resurrection quality scales with the caster's level and class. Lower-level rezzes are slow, costly, and return the target in poor condition. Higher-level rezzes are faster and more complete.

| Factor | Low-Level Rez | Mid-Level Rez | High-Level Rez | True Resurrection |
|--------|--------------|---------------|----------------|-------------------|
| **Available** | ~L15 | ~L30-50 | ~L60-80 | ~L90-95 |
| **Channel Time** | 30s+ | 15-20s | 8-12s | 5s |
| **HP on Return** | 10-25% | 25-50% | 50-75% | 100% |
| **Rez Sickness** | Heavy (long duration, major stat penalty) | Moderate | Mild | Minimal |
| **Mana Cost** | High | Very High | Extreme | Extreme |

True Resurrection is endgame. A full restore with minimal sickness, fast channel — the pinnacle of healing magic.

### Classes with Resurrection

- **Cleric of Healing:** Primary rezzer. Gets resurrection around **L15**, scaling through endgame. The best rez in the game at every tier.
- **Paladin:** Gets a lesser resurrection around **L30-40**. Slower channel, lower HP return, heavier sickness than a Cleric of equivalent level. A backup option, never a replacement.
- Other classes: TBD. Resurrection is rare and class-defining — it should not be common.

## Binding

### Default Bind

All characters default to the **nearest safe zone** as their bind point. For most people, this is the safe zone they're currently operating out of. For goblins and other factions, it's their seat of power (e.g., goblins respawn at their stronghold).

### Rebinding

Characters can change their bind point. This is a deliberate, strategic decision:

- **Safe zone binding** is always safe — you respawn somewhere protected.
- **Field binding** (binding at a camp, outpost, or forward position) shortens the corpse run but carries risk. If your bind point is overrun or in hostile territory, you respawn into danger. Repeated deaths at a hostile bind point is an **effective permadeath loop** — you keep dying where you spawn.

Binding mechanics (who can cast it, restrictions, cooldowns) are TBD.

## The Transition Exception

The first death during the Transition was a **freebie**. The system was still initializing — normal death rules were not yet in effect. Characters who died during the Transition event respawned at the nearest safe zone with no penalties, no ghost state, and no gear loss.

This is a one-time narrative exception. All subsequent deaths follow the standard rules above.

## Design Notes

The death system is designed around **meaningful consequences without permadeath:**

- **Corpse run + gear loss** is the primary penalty. It scales naturally with distance from safety.
- **Ghost state** creates a choice (wait vs. release) that adds tension and trust dynamics.
- **Resurrection** is powerful but costly — long channels, mana-intensive, never instant. Having a rezzer in your group is a strategic advantage, not a crutch.
- **The 24-hour timer** creates urgency without being punitive.
- **Binding** adds strategic depth — players must decide where the risk/reward tradeoff of a forward bind is worth it.

A party with a skilled rezzer operates with a safety net. A party *without* one feels every fight differently — because death means the long walk back.
