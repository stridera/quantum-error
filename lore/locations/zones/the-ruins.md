---
canon: true
stability: evolving
---

# The Ruins (South SF / Daly City, L5-9)

The first outdoor zone south of San Francisco. The suburban sprawl of South San Francisco and Daly City is breaking down — strip malls crumbling, tract housing collapsing, overgrown yards swallowing fences. Wildlife from the hills has moved into the abandoned neighborhoods.

## Description

Leaving the San Francisco safe zone, the landscape shifts from urban density to low suburban sprawl. The tidy rows of houses and strip malls that once defined South SF and Daly City are falling apart. Roofs sag. Windows are dark. Weeds push through every crack in the pavement, growing faster than they should.

The air smells like dry grass, dust, and something animal. Coyotes yip from the hills at dusk. Cats watch from windowsills with too-knowing eyes. The BART stations are dark tunnels now — nobody goes underground if they don't have to.

To the west, the Santa Cruz Mountains loom, their peaks lost in clouds. Occasionally, a silhouette passes across the sky beyond the ridgeline. It's too large to be a bird.

## Level Range

**L5-9.** The zone's threats escalate from minor (feral cats, rubble lurkers) to significant (coyote packs with an Alpha). The Colma Cemetery Dungeon sits at L5-7 within the zone.

## Environmental Traits

- **Suburban Decay:** Collapsed buildings, debris fields, overgrown lots. Line of sight is broken constantly.
- **Open-World:** No zone walls. Mobs roam freely. [Aggro range](../../../system/aggro.md) determines encounter frequency.
- **Hill Country:** The western edge of the zone rises into the foothills. Higher ground = line of sight to the mountain wall and dragon territory beyond.
- **Scavenging:** Ruined buildings contain lootable household goods, tools, and supplies. Most are mundane, but the system occasionally tags an item as Common-quality gear.

## Mob Roster

### Feral Cat Swarm
- **Level:** 5 | **Role:** Minion
- **Theme:** Neighborhood cats gone feral. They move in packs of 6-10, hissing and scratching. Individually nothing — a nuisance. In numbers, they overwhelm.
- **Abilities:** Swarm Attack (multiple small hits per round, hard to target individually).
- **Notes:** Introduction to swarm mechanics. Teaches "lots of weak things at once." Low stakes — even normal people can handle them with effort. The party barely notices.

### Rubble Lurker
- **Level:** 5-6 | **Role:** Normal
- **Theme:** A large lizard or insect (roughly dog-sized) nesting in collapsed buildings. Blends with the debris until it moves. Ambush predator.
- **Abilities:** Camouflage (surprise round from hiding), Skitter (quick repositioning after attacking).
- **Notes:** First encounter with ambush mechanics in the overworld. Rewards paying attention to the environment.

### Scavenger Bandit
- **Level:** 6-7 | **Role:** Normal
- **Theme:** Hostile humans who've staked out territories in the suburbs. Armed with looted melee weapons and improvised armor. Usually in groups of 2-3.
- **Abilities:** Dirty Fighting (bonus damage to flanked targets), Loot Drop (always drops some usable gear).
- **Notes:** Humans fighting humans. The moral discomfort continues from SF's Looters, but these are more organized and aggressive.

### Asphalt Crawler
- **Level:** 7-8 | **Role:** Normal
- **Theme:** A large centipede-like insectoid that emerges from the widening cracks in roads and parking lots. Segmented body, mandibles, too many legs. The pavement literally births them.
- **Abilities:** Mandible Grip (melee attack + brief root), Burrow (can retreat underground and reposition).
- **Notes:** Unsettling. The mundane world is producing monsters from its own decay.

### Coyote
- **Level:** 7-8 | **Role:** Normal
- **Theme:** Post-Transition coyotes are larger and smarter. They hunt in packs of 3-5, using flanking and encirclement. They avoid fights they can't win — but with numbers, they're aggressive.
- **Abilities:** Pack Flanking (bonus damage when 2+ coyotes are on the same target), Howl (alerts nearby coyotes within social aggro radius).
- **Notes:** The pack is the unit, not the individual. Killing them one at a time is fine. The problem is the Alpha.

### Coyote Alpha
- **Level:** 8-9 | **Role:** Elite
- **Theme:** Larger, scarred, with a mana-touched sheen to its fur. Commands the pack. It doesn't just lead — it *summons*.
- **Abilities:**
  - **Alpha Howl:** Summons 2-3 Coyotes every ~15 seconds. Unlimited uses. The adds keep coming.
  - **Savage Lunge:** High-damage opener when it first engages.
- **Notes:** **This is a DPS gate.** If the party doesn't kill the Alpha fast enough, the coyote adds pile up indefinitely. This is the first encounter that teaches "kill the source" — focus the summoner, ignore the adds. A significant challenge for the L3-5 party despite their 999 HP, because the Alpha is higher level, the swarm never stops, and the party has limited abilities.

**Swarm Escalation:**
1. **Feral Cat Swarm (L5):** Intro to swarming. Low stakes, teaches the concept.
2. **Coyote Pack + Alpha (L7-9):** Escalation. Swarm with a source. DPS gate. Must learn to prioritize the summoner.

## Colma Cemetery Dungeon (L5-7)

### Background

Colma, just south of Daly City, is famous as "the City of the Dead" — a real-world town that is almost entirely cemeteries, with far more dead residents than living ones. Post-Transition, they're getting up.

### Description

Rows of gravestones in every direction. Mausoleums with cracked doors. Open graves where something climbed out. The fog sits low here, hugging the ground. The grass is dead despite growing everywhere else in the zone.

A short, instanced dungeon — enter through the main cemetery gates, clear the grounds, and deal with whatever's animating them.

### Mobs

#### Cemetery Skeleton
- **Level:** 5-6 | **Role:** Normal
- **Theme:** Basic undead. Bones held together by mana. Slow, rattling, armed with whatever was buried with them (or just claws).
- **Abilities:** Bone Club (melee), Reassemble (25% chance to get back up 6s after "dying" unless destroyed by holy or fire damage).
- **Notes:** Holy damage bypasses Reassemble entirely. [Clint](../../../characters/party/clint.md) and [Wade](../../../characters/party/wade.md) obliterate these with their Paladin and Cleric holy abilities.

#### Cemetery Ghoul
- **Level:** 6-7 | **Role:** Elite
- **Theme:** Faster, smarter undead. Hunched, clawed, with a paralyzing touch. Hides behind mausoleums and ambushes.
- **Abilities:** Paralyzing Touch (melee attack + 3s stun on failed CON save), Corpse Eater (heals by consuming nearby skeleton corpses).
- **Notes:** The paralyze is the real threat for normal players. For the party, it's a mild inconvenience at worst.

#### Crypt Guardian (Boss)
- **Level:** 7 | **Role:** Elite (borderline Champion)
- **Theme:** A larger, armored undead — possibly a knight or soldier from an older burial. Wears corroded armor and carries a real weapon. The source of the cemetery's animation.
- **Abilities:** Grave Command (summons 3-4 skeletons), Shield Block (high AR), Unholy Aura (nearby undead deal +2 damage).
- **Notes:** A dungeon boss for normal L5-7 players. For the party, a comedy beat — Clint and Wade's holy powers make undead trivially easy. They carve through this dungeon like it's a tutorial, which reinforces how overpowered they are and how different their experience is from normal people.

### Loot

Dungeon-quality gear for L5-7 players. The party may pick up basic holy weapons or undead-themed drops. The real "loot" is the comedic value of the experience.

## Notable Locations

- **Colma Cemetery:** Dungeon. See above.
- **Westborough Shopping Center:** Ruined strip mall. Scavenger Bandit territory.
- **SFO Airport:** A massive concrete wasteland. Dark BART tunnels. Could be a dungeon in the future — for now it's an eerie landmark full of dead planes and silent terminals.
- **The Western Ridgeline:** The foothills where you can see the mountain wall and the dragons beyond. A good vantage point that reinforces the world's boundaries.

## Narrative Notes

This is the party's first time in the open world. [Wade](../../../characters/party/wade.md) rushed south from San Francisco to find his children, dragging the party into the Ruins with no weapons, no equipment, and no plan. They're heading toward Mountain View ([Clint's](../../../characters/party/clint.md) house) and Saratoga ([IQuantum](../../organizations/iquantum.md)).

The coyotes are the zone's defining encounter for the party. Underleveled and unequipped, they're overwhelmed by the L7-9 packs — the Alpha keeps summoning more, and the party can't burn it down fast enough. They flee into a Spirit Halloween store to escape, which turns out to be the [Spirit Dungeon](../../dungeons/spirit-dungeon.md). The dungeon becomes their first real leveling and gearing experience.

The Colma dungeon is a comedy beat — likely visited after the Spirit Dungeon, when the party returns through the area with actual gear and levels. Clint and Wade's holy powers make undead trivially easy, reinforcing how much they've grown.
