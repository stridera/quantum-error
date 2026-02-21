---
canon: true
stability: evolving
---

# Aggro & Detection

Defines how mobs detect and engage players in the overworld. The core mechanic: higher-level mobs notice you from farther away, making it progressively harder to travel through zones above your level.

## Detection Range

### Base Formula

```
detection_range(mob_level, player_level) = max(10, 30 + (mob_level - player_level) × 10)
```

- **Base range:** 30 feet (same-level mob)
- **Per level above player:** +10 feet
- **Per level below player:** -5 feet
- **Minimum:** 10 feet (even trivial mobs react if stepped on)
- **Maximum:** 200 feet (cap — prevents infinite detection)

### Detection Range Table

| Mob vs Player Delta | Detection Range | Notes |
|---------------------|----------------|-------|
| -10 (grey mob) | 10 ft | Minimum. Barely notices you. |
| -5 | 10 ft | Still at minimum. |
| -2 | 20 ft | Aware but not aggressive at range. |
| 0 (same level) | 30 ft | Standard. |
| +2 | 50 ft | Noticeable increase. |
| +5 | 80 ft | Hard to avoid. |
| +10 | 130 ft | Very hard to avoid. |
| +15 | 180 ft | Practically zone-wide. |
| +17+ | 200 ft | Cap. |

### Examples (Party at Level 5)

| Mob Level | Detection Range | Experience |
|-----------|----------------|------------|
| L3 | 10 ft | Walk right past. |
| L5 | 30 ft | Standard encounter distance. |
| L8 | 60 ft | Need to be careful. |
| L10 | 80 ft | Actively hunting you. |
| L15 | 130 ft | Chasing you from across the street. |
| L20 | 180 ft | You can't enter the zone without being noticed. |

## Aggro Behavior

### Initial Detection

When a mob detects a player within its detection range:

1. **Hostile mobs** immediately move to engage.
2. **Neutral mobs** (animals, some humanoids) may observe before attacking. Approaching closer triggers aggro.
3. **Passive mobs** never aggro (quest NPCs, livestock, non-combatants).

### Social Aggro

Mobs may alert nearby mobs when they detect a threat.

- **Social radius:** 30 feet from the alerted mob (fixed, not level-scaled).
- **Same-type only:** A coyote alerts other coyotes, not nearby bandits.
- **Chain limit:** Social aggro does not chain indefinitely. Only mobs within social radius of the *originally detecting* mob are alerted.
- **Summoners** (e.g., Coyote Alpha) bypass the chain limit — their summoning ability explicitly calls reinforcements regardless of distance.

### Level-Based Aggro Behavior

| Player vs Mob Delta | Mob Behavior |
|---------------------|-------------|
| Player 10+ levels above | Mob flees on detection (grey mob). |
| Player 5-9 levels above | Mob hesitates, may not engage unless provoked. |
| Same level (±4) | Normal aggro behavior. |
| Mob 5-9 levels above | Mob is aggressive, pursues longer before leashing. |
| Mob 10+ levels above | Mob pursues indefinitely within its zone. Will not leash. |

### Leashing

Mobs that lose their target (player outruns them, line-of-sight breaks for extended period) will eventually return to their patrol area.

- **Standard leash distance:** 100 feet from spawn point.
- **High-delta leash:** Mobs 10+ levels above the player extend leash to 300 feet or zone boundary.
- **Boss/Champion mobs:** Do not leash within their zone.

## Stealth Interaction

[Stealth](../classes/veilstepper-rogue.md) reduces the effective detection range against the stealthed character.

- **Stealth reduction:** Detection range is halved (rounded down) against a stealthed character.
- **Level delta still applies:** A L20 mob has 180 ft detection vs a L5 player, reduced to 90 ft by stealth. Still dangerous.
- **Detection check:** If a stealthed character enters the reduced detection range, the mob makes a Perception vs Stealth check. Failure means the mob is unaware. Success means normal aggro.

## Open Questions

- **Dungeon aggro:** Do dungeon mobs use the same formula, or do dungeons have fixed aggro rules (room-based)?
- **Mount speed:** If mounts are introduced, does movement speed affect the ability to outrun aggro?
- **Party size aggro:** Should larger parties increase detection range (more noise)?
