---
canon: true
stability: evolving
---

# Spirit Dungeon — Mobs

Full mob roster for the [Spirit Dungeon](../spirit-dungeon.md) (Level 10). All stat blocks use the [Mob Framework](../../../system/mob-framework.md) L10 baseline.

**L10 Base Stats (Normal):** 60 HP, 9 dmg, 10 acc, 6 AR, 600 XP
**Role Multipliers:** Minion 0.25x HP / 0.5x dmg | Elite 2.5x HP / 1.25x dmg | Champion 6x HP / 1.5x dmg | Boss 15x HP / 2x dmg

---

## Room 1: The Flicker Hall

### Jason Mask Mannequin

A mannequin in a hockey mask and blood-spattered jumpsuit. Holds a prop machete that's heavier than it looks.

- **Level:** 10
- **Role:** Normal (Brute)
- **HP:** 60 | **Damage:** 9 | **Accuracy:** 10 | **AR:** 6
- **XP:** 600
- **Attributes:** STR 9, CON 9, DEX 7, INT 4, WIS 4, CHA 4
- **Attacks:** 1

#### Lunge
- **Type:** Skill
- **Cost:** None
- **Cooldown:** 10s
- **Duration:** Instant
- **Targeting:** Enemy
- **Rules:**
  - Opening attack only (usable once per combat).
  - +3 accuracy on this attack.
  - If it hits, deals normal damage + 3 bonus (12 total).
  - Telegraphed by a slight forward lean before the burst of motion.

**Drops:** Plastic Hockey Mask (Common, cosmetic), Prop Machete (Common weapon, 4-7 physical)

---

### Freddy Mask Mannequin

A mannequin wearing a burned fedora and striped sweater, with a crude metal claw glove on one hand.

- **Level:** 10
- **Role:** Normal (Skirmisher)
- **HP:** 60 | **Damage:** 9 | **Accuracy:** 10 | **AR:** 6
- **XP:** 600
- **Attributes:** STR 7, DEX 9, CON 7, INT 4, WIS 4, CHA 4
- **Attacks:** 1

#### Flank Strike
- **Type:** Skill (Passive trigger)
- **Cost:** None
- **Cooldown:** None
- **Duration:** Instant
- **Targeting:** Enemy
- **Rules:**
  - If an ally is also in melee with the same target, this mob flanks.
  - Flanking attacks deal +4 bonus damage (13 total).
  - Always tries to position opposite its partner.

**Drops:** Prop Claw Glove (Common weapon, 3-6 physical, +1 acc)

---

### Scream Mask Mannequin

A mannequin in a stretched Scream mask, clutching a dull prop knife that becomes sharp when you look away.

- **Level:** 10
- **Role:** Normal (Skirmisher)
- **HP:** 60 | **Damage:** 9 | **Accuracy:** 10 | **AR:** 6
- **XP:** 600
- **Attributes:** STR 7, DEX 9, CON 7, INT 4, WIS 7, CHA 4
- **Attacks:** 1

#### Panic Cut
- **Type:** Skill
- **Cost:** None
- **Cooldown:** 6s
- **Duration:** Instant
- **Targeting:** Enemy
- **Rules:**
  - Standard melee attack.
  - If the target is under a fear, charm, or compulsion effect: damage is increased by 50% (14 total).
  - Synergizes with Pinhead Mask's Fascination — the Scream Mask punishes charmed targets.

**Drops:** Scream Robe (Common armor, +2 AR, dark hooded robe — this is what [Clint](../../../characters/party/clint.md) loots after the second fight)

---

### Pinhead Mask Mannequin

A mannequin wearing a mask studded with pins and nails. When it speaks, your thoughts line up like iron filings.

- **Level:** 10
- **Role:** Elite (Controller)
- **HP:** 150 | **Damage:** 11 | **Accuracy:** 10 | **AR:** 6
- **XP:** 1,800
- **Attributes:** INT 10, CHA 10, WIS 7, STR 4, DEX 4, CON 4
- **Attacks:** 1

#### Fascination
- **Type:** Spell (Charm / Compulsion)
- **Cost:** None (innate)
- **Cooldown:** 15s
- **Duration:** 10s (or until broken)
- **Targeting:** Enemy
- **Tags:** Mental, Charm, Control
- **Rules:**
  - Target is **Compelled** to maintain attention on the caster.
  - -80% threat awareness toward non-caster enemies.
  - 50% chance to fail target selection each action (wastes selection, does not consume action if overridden by ally intervention).
  - **Break conditions:** Loss of line-of-sight, ally shove/taunt (forced redirection), or taking damage above 15 in a single hit.
  - Telegraphed by the pins on the mask beginning to glow faintly.

```text
┌──────────────────────────────────────────────┐
│ STATUS: Fascination                          │
├──────────────────────────────────────────────┤
│ Type: Debuff (Charm / Compulsion)            │
│ Source: Pinhead Mask Mannequin               │
│ Duration: 10s                                │
│ Stacks: 0 (Does not stack; refreshes)        │
│ Dispel: Yes (Cleanse/Dispel)                 │
├──────────────────────────────────────────────┤
│ Summary: Your focus is pulled to the caster. │
├──────────────────────────────────────────────┤
│ Numbers:                                     │
│ - Forces target-priority: Caster             │
│ - -80% threat awareness to other enemies     │
│ - 50% action target failure (non-caster)     │
│ - Break on: LOS break, ally shove/taunt,     │
│   or single hit > 15 damage                  │
└──────────────────────────────────────────────┘
```

#### Pin Jab
- **Type:** Skill
- **Cost:** None
- **Cooldown:** None
- **Duration:** Instant
- **Targeting:** Enemy
- **Rules:**
  - Basic melee attack (11 damage).
  - Used when Fascination is on cooldown or target is already Fascinated.

**Drops:** Pin-Studded Apron (Uncommon armor, +4 AR, -1 CHA. Looks awful.)

---

### Falling Bear

A full-sized bear that drops from the ceiling when the bear trap is triggered. Very real. Very angry.

- **Level:** 10
- **Role:** Elite (Beast)
- **HP:** 150 | **Damage:** 11 | **Accuracy:** 10 | **AR:** 6
- **XP:** 1,800
- **Attributes:** STR 10, CON 10, DEX 7, INT 4, WIS 7, CHA 4
- **Attacks:** 1-2

#### Ceiling Impact
- **Type:** Skill (Trap trigger only)
- **Cost:** None
- **Cooldown:** N/A (one-time)
- **Duration:** Instant
- **Targeting:** Enemy (trap triggerer)
- **Rules:**
  - Occurs on spawn only. The bear lands on whoever triggered the trap.
  - 45 physical damage (ignores AR — crushing weight).
  - Target is knocked prone for 3s.
  - Counts as the bear's first attack; it then acts normally.

#### Maul
- **Type:** Skill
- **Cost:** None
- **Cooldown:** 8s
- **Duration:** Instant
- **Targeting:** Enemy
- **Rules:**
  - Heavy swipe: 16 physical damage.
  - If target is prone or rooted, damage increases to 22.
  - Used in place of normal attack when available.

#### Roar
- **Type:** Skill
- **Cost:** None
- **Cooldown:** Once per combat
- **Duration:** 3s fear + pull trigger
- **Targeting:** Room (AoE — Enemies)
- **Rules:**
  - All enemies in the room make a Will check (DC 12).
  - Failure: 3s Fear (cannot approach the bear, -3 accuracy).
  - **Summon trigger:** Pulls the roaming pack from down the hall. They arrive 10s after the roar.
  - Telegraphed by the bear rearing up on hind legs.

**Drops:** Bear Claw Necklace (Uncommon accessory, +1 STR)

---

### Sexy Nurse Mannequin

A mannequin in a too-short nurse costume, white stockings, and a tiny cap. Carries an oversized syringe.

- **Level:** 10
- **Role:** Normal (Skirmisher)
- **HP:** 60 | **Damage:** 9 | **Accuracy:** 10 | **AR:** 6
- **XP:** 600
- **Attributes:** DEX 9, WIS 7, CHA 7, STR 4, CON 4, INT 4
- **Attacks:** 1

#### Injection
- **Type:** Skill
- **Cost:** None
- **Cooldown:** 12s
- **Duration:** 8s (DoT)
- **Targeting:** Enemy
- **Tags:** Poison
- **Rules:**
  - Melee attack: 6 physical damage on hit.
  - Applies **Nausea** debuff: 2 poison damage per 2s for 8s (8 total) and -2 accuracy for the duration.
  - Dispellable by Cleanse or any poison cure.

```text
┌──────────────────────────────────────────────┐
│ STATUS: Nausea                               │
├──────────────────────────────────────────────┤
│ Type: Debuff (Poison)                        │
│ Source: Sexy Nurse Mannequin                 │
│ Duration: 8s                                 │
│ Stacks: 0 (Does not stack; refreshes)        │
│ Dispel: Yes (Cleanse / Poison Cure)          │
├──────────────────────────────────────────────┤
│ Summary: Queasy and unfocused.               │
├──────────────────────────────────────────────┤
│ Numbers:                                     │
│ - 2 poison damage every 2s (8 total)         │
│ - -2 Accuracy                                │
└──────────────────────────────────────────────┘
```

**Drops:** Nurse's Cap (Uncommon accessory — +5% healing output. Tiny white cap with a red cross. Looks ridiculous on [Wade](../../../characters/party/wade.md). He wears it anyway.)

---

### Sexy Witch Mannequin

A mannequin in a low-cut witch costume, pointed hat, and purple stockings. Waves a sparkly plastic wand that crackles with real energy.

- **Level:** 10
- **Role:** Normal (Caster)
- **HP:** 60 | **Damage:** 9 | **Accuracy:** 10 | **AR:** 6
- **XP:** 600
- **Attributes:** INT 9, CHA 7, WIS 7, STR 4, CON 4, DEX 4
- **Attacks:** 1

#### Hex
- **Type:** Spell
- **Cost:** None (innate)
- **Cooldown:** 10s
- **Duration:** 6s
- **Targeting:** Enemy
- **Tags:** Curse, Debuff
- **Rules:**
  - Ranged spell attack (10-foot range within room).
  - On hit: applies **Hex** — target takes -3 accuracy and -2 damage dealt for 6s.
  - Does no direct damage. Pure debuff.
  - Dispellable by Cleanse.

**Drops:** Sparkly Plastic Wand (Common weapon, 2-5 arcane damage, ranged. Actually works.)

---

### Sexy Pirate Mannequin

A mannequin in a corseted pirate outfit, thigh-high boots, and a tricorn hat. Carries a surprisingly real-looking cutlass.

- **Level:** 10
- **Role:** Normal (Soldier)
- **HP:** 60 | **Damage:** 9 | **Accuracy:** 10 | **AR:** 6
- **XP:** 600
- **Attributes:** STR 9, DEX 7, CON 7, INT 4, WIS 4, CHA 4
- **Attacks:** 1

#### Cutlass Slash
- **Type:** Skill
- **Cost:** None
- **Cooldown:** 8s
- **Duration:** Instant
- **Targeting:** Enemy
- **Rules:**
  - Melee attack: 12 physical damage (9 base + 3 bonus).

#### Healer Hunter
- **Type:** Passive
- **Cost:** None
- **Rules:**
  - Every 15s, the Pirate re-evaluates targets and prioritizes the highest healing output.
  - Clears current threat and switches to the healer, forcing the tank to re-establish aggro.
  - If no healer is present, behaves as a standard Soldier (attacks highest-threat target).
  - Telegraphed by the Pirate turning away from the tank mid-swing — the party learns to watch for the pivot.
  - **Lesson:** Healers aren't safe just because a tank exists. Positioning and re-taunts matter.

**Drops:** Prop Cutlass (Common weapon, 5-8 physical. Surprisingly sharp for plastic.)

---

### Mannequin Minion

A featureless mannequin in a generic costume. Moves jerkily. Not very threatening alone.

- **Level:** 10
- **Role:** Minion
- **HP:** 15 | **Damage:** 5 | **Accuracy:** 10 | **AR:** 6
- **XP:** 150
- **Attributes:** STR 7, DEX 7, CON 7, INT 4, WIS 4, CHA 4
- **Attacks:** 1

No abilities. Attack only. Comes in packs pulled by the bear's Roar. Dangerous through numbers, not mechanics.

**Drops:** None (vendor trash costume scraps)

---

## Room 2: The Mirror Room

### Echo Double — Base Mechanic

A mirror-spawned reflection of a party member. The Spirit Dungeon's mirrors don't show who you are — they show what you're running from. Each echo takes a form unique to its original, targeting their deepest vulnerability. Its movements are slightly off, like a reflection that doesn't quite sync.

- **Level:** 10
- **Role:** Elite (mirrors original's archetype)
- **HP:** 150 | **Damage:** 11 | **Accuracy:** 10 | **AR:** 6
- **XP:** 1,800
- **Attributes:** Copies the original's archetype profile at L10 values
- **Attacks:** 1

#### Mirror Mockery
- **Type:** Passive
- **Cost:** None
- **Cooldown:** None
- **Duration:** Permanent (while alive)
- **Targeting:** Self / linked original
- **Rules:**
  - The Echo Double and its original deal +25% damage to each other.
  - The Echo Double takes +25% damage from its original.
  - Spawns when a character locks eyes with their reflection for more than 3s.
  - One Echo per mirror, one mirror per character.

#### Identity Crisis (Phase 1)
- **Type:** Spell (Psychic / Compulsion)
- **Cost:** None (innate)
- **Cooldown:** 6s between taunts
- **Duration:** Until Phase 2 begins
- **Targeting:** Linked original only
- **Tags:** Mental, Psychic, Identity
- **Rules:**
  - The echo does not attack physically during Phase 1. It speaks.
  - Each taunt deals **20% of target's maximum HP** as psychic damage (ignores AR). Four taunts leave any target at 20% HP regardless of starting pool.
  - Each taunt applies one stack of **Shaken**.
  - Taunts fire every 6s. Maximum 4 taunts before Phase 2 auto-triggers.
  - **Phase 2 triggers when:** (a) the original attacks the echo, (b) 4 taunts have been delivered, or (c) 30s elapse without action.
  - **Design intent:** 20%/taunt is lethal for a normal-HP character, so Phase 2 is where a typical player would already be in real trouble. The party's console-boosted 999-HP pool makes 200 HP (20%) a workable fighting floor — assuming they actually fight. Characters who refuse to engage during Phase 2 get finished by the echo's fifth and final taunt (see Mirror Barrier loss condition).

```text
┌──────────────────────────────────────────────┐
│ STATUS: Shaken                               │
├──────────────────────────────────────────────┤
│ Type: Debuff (Psychic / Identity)            │
│ Source: Echo Double                          │
│ Duration: Until echo is defeated             │
│ Stacks: Yes (max 4)                          │
│ Dispel: No (must be overcome, not cleansed)  │
├──────────────────────────────────────────────┤
│ Summary: Your past has weight.               │
├──────────────────────────────────────────────┤
│ Numbers:                                     │
│ - -2 Accuracy per stack                      │
│ - -1 Damage dealt per stack                  │
│ - Stack removal: each successful hit on the  │
│   echo removes 1 stack                       │
│ - Ally encouragement (verbal, one-time per   │
│   fight): removes 2 stacks                   │
└──────────────────────────────────────────────┘
```

```text
┌──────────────────────────────────────────────┐
│ STATUS: Broken                               │
├──────────────────────────────────────────────┤
│ Type: Debuff (Psychic / Identity)            │
│ Source: Echo Double (final taunt on failure) │
│ Duration: Until the bearer leaves the        │
│   Spirit Dungeon                             │
│ Stacks: No (binary state)                    │
│ Dispel: No (cannot be healed, cleansed, or   │
│   dispelled by any means inside the dungeon) │
├──────────────────────────────────────────────┤
│ Summary: The mirror found the thing you      │
│ couldn't look at yet.                        │
├──────────────────────────────────────────────┤
│ Numbers:                                     │
│ - -3 to all primary attributes               │
│   (STR/DEX/CON/INT/WIS/CHA)                  │
│ - -25% damage dealt                          │
│ - -25% healing effectiveness (incoming and   │
│   outgoing — the healer heals less, AND is   │
│   healed less)                               │
│ - -25% buff effectiveness (songs, shouts,    │
│   blessings all land at three-quarters       │
│   strength)                                  │
│ - Applied alongside HP reduction to 1 by     │
│   the echo's fifth and final taunt           │
│ - Clears automatically on exit from the      │
│   Spirit Dungeon — no action needed          │
├──────────────────────────────────────────────┤
│ Design note: Broken is a dungeon-scope       │
│ narrative debuff, not a persistent injury.   │
│ The party must finish the dungeon with a     │
│ compromised member; the dungeon leaving is   │
│ what heals it. The wound stays. The status   │
│ doesn't.                                     │
└──────────────────────────────────────────────┘
```

#### Mirror Barrier
- **Type:** Environmental (dungeon mechanic)
- **Rules:**
  - When an echo spawns, a translucent barrier seals the section between the mirror wall and the room center.
  - The original is locked inside with their echo. No other entities may enter or attack through the barrier.
  - Allies can see and hear through the barrier. Spells and attacks do not penetrate.
  - **Verbal encouragement** penetrates the barrier. One ally per fight may shout encouragement (costs that ally's action), removing 2 Shaken stacks from the fighter.
  - **Win condition:** When the echo is defeated, it shatters into glass. The glass flies back into the cracked mirror frame and restores the pane, leaving a pulsing crystal [Mirror Shard](#mirror-shard-drops) behind at the mirror's base. The barrier drops. The mirror is whole again.
  - **Loss condition:** If the original does not land a hit on the echo within 30s of Phase 2 starting, the echo delivers one **final taunt** — the fifth — and the fight ends. The final taunt reduces the target to **1 HP** (regardless of current HP) and inflicts **[Broken](#identity-crisis-phase-1)** (−3 all primary stats, −25% damage/healing/buff effectiveness, persists until the bearer leaves the Spirit Dungeon — see the Broken stat block above for full rules). The echo then turns and walks back into the broken frame. The glass does *not* restore — the mirror stays cracked. The shard at the base goes dark. The original is ejected still standing, but barely.
  - One fight at a time. The next mirror activates only after the current barrier drops.

#### Mirror Shard Drops

Each echo drops a class-appropriate **Rare** [Mirror Shard](../../../items/accessories/mirror-shards.md) accessory when defeated. The shard is faintly visible at the base of each mirror before the fight — the party can see the reward. They also know the cost. Mirror Shards are soulbound evolving items — the base effects listed below scale with small milestone bonuses every 10 levels. Full rules in [items/accessories/mirror-shards.md](../../../items/accessories/mirror-shards.md).

| Character | Shard | Effect | Flavor |
|---|---|---|---|
| [Selene](../../../characters/party/selene.md) | Shard of Self | +1 Perception, +5% crit from stealth/Veil | *"It showed you who you were. Now it shows what's coming."* |
| [Wade](../../../characters/party/wade.md) | Shard of Devotion | +10% healing on targets below 25% HP | *"Your hands are steadier now."* |
| [Clint](../../../characters/party/clint.md) | Shard of Duty | +1 AR, +10% threat generation | *"The shield cracked. You didn't."* |
| [Vanessa](../../../characters/party/vanessa.md) | Shard of Control | −5% mana cost, +5% spell accuracy | *"You don't have to become anything else."* |
| [Rebekah](../../../characters/party/rebekah.md) | Shard of Purpose | +10% song/buff duration | *"Your voice carries further than you know."* |

---

### Selene's Echo: Dustin

The mirror shows a [Nekara](../../../races/nekara.md) catgirl — [Selene's](../../../characters/party/selene.md) true form, reflected back for the first time. She stares. The reflection stares back. Then the features shift. The ears recede. The frame broadens. Stringy blond hair, blue eyes, male. Dustin. The person she stopped being.

The echo steps out of the cracked glass wearing her old face.

- **Level:** 10
- **Role:** Elite (Skirmisher)
- **HP:** 150 | **Damage:** 11 | **Accuracy:** 10 | **AR:** 6
- **XP:** 1,800
- **Attributes:** DEX 10, STR 7, CON 7, WIS 7, INT 4, CHA 4
- **Attacks:** 1

#### Identity Crisis — Taunt Sequence
1. "You always ran from me."
2. "You'll never be free of me."
3. "They don't see you. They see what the system made."
4. "Take off the mask, Dustin."

#### Phase 2: Mirrored Rogue

##### Shadowstep Strike
- **Type:** Skill
- **Cost:** None
- **Cooldown:** 10s
- **Duration:** Instant
- **Targeting:** Enemy (Selene)
- **Rules:**
  - Repositions behind Selene and strikes.
  - 14 damage (11 base × 1.25 Mirror Mockery).
  - +4 bonus damage from behind (Backstab).
  - The echo fights with Selene's own movements — same stance, same feints.

##### Bleeding Strike
- **Type:** Skill
- **Cost:** None
- **Cooldown:** 8s
- **Duration:** 8s (DoT)
- **Targeting:** Enemy (Selene)
- **Rules:**
  - On hit: applies 2 damage per 2s for 8s (8 total bleed).
  - Standard melee damage on the initial hit.

**Narrative:** First echo fight. [Rebekah](../../../characters/party/rebekah.md) encourages Selene to approach the mirror. The party doesn't know the mechanic yet — the barrier is a shock. Rebekah shouts through the barrier when the taunts land (clears 2 Shaken stacks). The fourth taunt — the dead name — turns Selene from hurt to furious. She stops fighting Dustin and starts fighting the echo. The distinction matters.

**Drops:** **Shard of Self** — Mirror fragment pendant. +1 Perception, +5% crit chance while in Veil or stealth. *"It showed you who you were. Now it shows what's coming."*

---

### Wade's Echo: The Empty Hands

The mirror shows [Wade](../../../characters/party/wade.md) in a hospital room. His [twins](../../../characters/supporting/the-twins.md) are in his arms. Then they slip through. The reflection looks up with hollow eyes — same face, same dad-bod, same sandy blond hair. Empty.

It steps out slowly, hands open and useless.

- **Level:** 10
- **Role:** Elite (Caster)
- **HP:** 150 | **Damage:** 11 | **Accuracy:** 10 | **AR:** 6
- **XP:** 1,800
- **Attributes:** WIS 10, CHA 7, INT 7, STR 4, DEX 4, CON 7
- **Attacks:** 1

#### Identity Crisis — Taunt Sequence
1. "Your dreams — the ones you never remember — they were funerals."
2. "You keep healing strangers because you couldn't heal them."
3. "Two small coffins. You picked out the flowers. You just won't let yourself remember."
4. "There's nothing waiting for you back home. Part of you already knows."

**Final Taunt** *(only fires if Wade fails to attack during Phase 2 — delivered as the echo turns to leave)*:

5. *"They're gone. You know. You've always known."*

This taunt reduces Wade from 20% HP to 1 HP and inflicts Broken. The echo does not wait to see it land. It just walks back into the frame.

*GM/author note: Wade's echo exploits leaked real-world memory — in the source reality the twins died of the genetic disease Wade couldn't treat. The block on real-world memories is imperfect. Wade's conscious mind doesn't know. His subconscious does, which is why all four Shaken stacks land where other party members shrugged off one or two, and why the fifth taunt lands with the full weight of a truth he has been carrying without permission to name. Do not surface this in character-facing prose until the reveal chapter.*

#### Phase 2: Corrupted Cleric

##### Wound
- **Type:** Spell (Psychic)
- **Cost:** None (innate)
- **Cooldown:** 8s
- **Duration:** Instant
- **Targeting:** Enemy (Wade)
- **Rules:**
  - Reversed [Cure Light Wounds](../../../classes/cleric-of-healing.md). Healing energy flowing backwards.
  - Deals 8% of Wade's current HP as psychic damage (ignores AR).

##### Self-Mend
- **Type:** Spell (Heal)
- **Cost:** None (innate)
- **Cooldown:** 8s
- **Duration:** Instant
- **Targeting:** Self
- **Rules:**
  - Heals the echo for 20 HP.
  - Forces a DPS race. Wade is not a DPS class — this is the mechanical tension.

##### Divine Vulnerability
- **Type:** Passive
- **Rules:**
  - The echo takes +50% damage from [Turn Undead](../../../classes/cleric-of-healing.md) and divine-source abilities.
  - The echo is a spiritual construct in a Spirit Dungeon. Wade's anti-undead kit works.
  - This is the intended breakthrough — Wade stops trying to out-damage a healer and uses divine authority.

**Narrative:** Wade goes last. He watched everyone else succeed. The taunts all land — all four Shaken stacks. Phase 2 begins. Wade has 30 seconds to attack. He doesn't. He freezes. The echo is wearing his face and showing him his empty hands and he can't bring himself to fight it because fighting it means accepting the fear. Someone shouts through the barrier. It clears 2 stacks. It's not enough. The 30 seconds expire. The echo walks back into the mirror. The glass repairs. Wade gets **Broken** (−3 all primary stats, −25% healing effectiveness, persists until rest). No shard. The healer is compromised going into the [boss fight](boss.md).

This is the intended outcome. Wade's trauma — his family, his daughters, the real world — is not something he can face yet. He's the highest-level party member and the one who breaks. [Foreshadows his Post-Book I exit.](../../../characters/party/wade.md)

**Drops (on success):** **Shard of Devotion** — Mirror fragment that pulses with warm light. +10% healing effectiveness on targets below 25% HP. *"Your hands are steadier now."* Wade does not earn this shard.

---

### Clint's Echo: The Broken Shield

The mirror shows [Clint](../../../characters/party/clint.md) standing over a fallen party member — the face keeps cycling through his friends. He's reaching down but his hands pass through them. The reflection's shield is cracked down the middle. Same armor, same stance. Eyes carrying the weight of everyone he couldn't save.

It steps out with a fractured shield raised.

- **Level:** 10
- **Role:** Elite (Soldier)
- **HP:** 150 | **Damage:** 11 | **Accuracy:** 10 | **AR:** 8 (mirrored shield — higher base)
- **XP:** 1,800
- **Attributes:** STR 10, CON 10, DEX 4, INT 4, WIS 7, CHA 4
- **Attacks:** 1

#### Identity Crisis — Taunt Sequence
1. "Respawn brings them back. It doesn't un-break them. Ask Wade in five minutes."
2. "You picked Selene's body. Vanessa's power. Rebekah's voice. None of them got a vote."
3. "The ones who respawn keep respawning. The ones who break, break forever."
4. "You don't know how to get them home. You never did. You just knew how to get them here."

These taunts bypass Clint's usual reflex ("they'll just respawn") by targeting the things respawn cannot fix: agency, consent, and psychological permanence. Taunt #1 is the cruelest — the echo knows what's coming to Wade because echoes know. Taunt #2 is the [system console](../../../characters/party/clint.md) angle: Clint shaped his friends' races, classes, and attributes before the Transition locked everything in, and none of them got to veto the choices. Taunt #4 names the real weight — he's the architect, not the leader.

#### Phase 2: Mirrored Paladin

##### Mirrored Smite
- **Type:** Smite
- **Cost:** None (innate — echoes don't use mana)
- **Cooldown:** 4s
- **Duration:** Instant
- **Targeting:** Enemy (Clint)
- **Rules:**
  - [Smite: Judgment](../../../classes/paladin-of-the-system.md) at L10 values. 15 System damage + standard weapon hit (11).
  - With Mirror Mockery (+25%): ~33 total per Smite hit.
  - The echo smites with higher authority than Clint currently holds (L10 vs Clint's L3).

##### Shield Wall
- **Type:** Passive
- **Rules:**
  - The echo's AR is 8 (vs standard 6). Fights defensively using [Shield Discipline](../../../classes/paladin-of-the-system.md).
  - Damage gets through slowly. Clint has to commit to sustained aggression.
  - The protector must become the attacker — uncomfortable by design.

##### Commanding Shout
- **Type:** Command
- **Cost:** None (innate)
- **Cooldown:** 15s
- **Duration:** 3s
- **Targeting:** Enemy (Clint)
- **Rules:**
  - Forces Clint to focus attacks on the echo for 3s.
  - Mechanically redundant in a 1v1 — thematically significant. The leader being commanded.

**Narrative:** The echo is a better Paladin than Clint is right now (L10 vs L3). It hits harder, blocks better. The taunts don't aim at death — they aim at the things respawn can't fix. Clint's breakthrough isn't a counter-argument. It's an acknowledgment. Yeah, he forgot his own Luck at the console (it's 4, the lowest in the party — he boosted theirs and forgot his own). Yeah, he doesn't know how to get them home. Yeah, Wade is about to break. None of that gets to stop him. *"Then I don't get to stop either."* He keeps hitting. The protector who knows shields break — and built the door they all walked through — shows up anyway.

**Drops:** **Shard of Duty** — Mirror fragment in a cracked shield-shaped frame. +1 AR, +10% threat generation on taunt abilities. *"The shield cracked. You didn't."*

---

### Vanessa's Echo: The Mana Shock

The mirror shows [Vanessa](../../../characters/party/vanessa.md) — but brighter, and wrong. The [mana glow](../../../classes/quantum-sorceress.md) in her veins is blinding white, crackling, unstable. Her eyes are twin stars. The silhouette won't settle — sometimes slimmer, sometimes broader, always a half-second out of sync with itself, as if the echo can't decide which version of her body to commit to. This is 99,999-mana Vanessa. The version that almost lost control. It steps out trailing afterimages and ozone, outline drifting in the air behind it.

- **Level:** 10
- **Role:** Elite (Caster)
- **HP:** 150 | **Damage:** 11 | **Accuracy:** 10 | **AR:** 4 (no armor — raw power, no defense)
- **XP:** 1,800
- **Attributes:** INT 10, CHA 7, WIS 7, STR 4, CON 4, DEX 4
- **Attacks:** 1

#### Identity Crisis — Taunt Sequence
1. "A physicist would have modeled the risk first. You just pushed the button."
2. "99,999 mana. You told yourself it was curiosity. It was panic — you needed to know if you could."
3. "You stopped hating your body. That isn't the same as loving it. You've just been tired of the fight."
4. "They think you're the smart one in the party. You're just the first to answer."

These aren't lies. That's what makes them worse. The echo reframes the Mana Shock not as a power failure but as an *instability* failure — [Vanessa's](../../../characters/party/vanessa.md) hastiness, her intellectual bluffing, and the unresolved peace she's made with her own body are all lies balanced on top of the same unmetabolized impulse. The shifting silhouette is the echo showing her what she already knows.

#### Phase 2: Uncontrolled Sorceress

##### Amplified Bolt
- **Type:** Spell (Arcane)
- **Cost:** None (innate)
- **Cooldown:** 4s
- **Duration:** Instant
- **Targeting:** Enemy (Vanessa)
- **Rules:**
  - 14 arcane damage (11 × 1.25 Mirror Mockery).
  - Reliable ranged damage. Fires constantly.

##### Mana Flare
- **Type:** Spell (AoE)
- **Cost:** None (innate)
- **Cooldown:** 12s
- **Duration:** Instant
- **Targeting:** Mirror section (AoE)
- **Rules:**
  - 6 arcane damage to everything in the mirror section. Unavoidable in the confined space.
  - Represents uncontrolled mana radiation.
  - Each Flare is visually brighter than the last — narrative pressure that something bigger is building.

##### Glass Cannon
- **Type:** Passive
- **Rules:**
  - AR 4 (vs standard 6). The echo trades defense for power.
  - If Vanessa commits to aggression with controlled spells, the echo falls fast.
  - [Anchor](../../../classes/quantum-sorceress.md)-tagged spells (stable, controlled) are the counter to the echo's amplified chaos. Precision beats power.

**Narrative:** The echo is everything Vanessa fears about herself — not the raw power, but the *instability* underneath. Her hastiness, her intellectual bluffs, even the comfort she tells herself she's made with her own body — all of them are lies balanced on top of an impulse she never fully resolved. The 99,999-mana incident wasn't calculation; it was impulse dressed as curiosity. The echo's silhouette never settles because Vanessa's self-acceptance never fully did.

Her breakthrough is slower than the others. She stops trying to be the first to answer and starts being the right one. She uses [Anchor](../../../classes/quantum-sorceress.md)-tagged spells. And somewhere in the middle of the fight, she looks at the echo's shifting outline and realizes she doesn't want *any* of those bodies — because none of them are hers. The one she's standing in is. The physicist stops treating instability as something to outrun and starts treating it as something to measure. She doesn't become anything. She just stops apologizing for what she already is.

**Drops:** **Shard of Control** — Mirror fragment humming at one steady pitch — the note never wavers, even when the wearer does. −5% mana cost, +5% spell accuracy. *"You don't have to become anything else."*

---

### Rebekah's Echo: The Silent One

The mirror shows [Rebekah](../../../characters/party/rebekah.md) — but wrong. The reflection's mouth is moving and no sound comes out. Her hands are on an instrument that isn't making music. She's singing and the world isn't listening. The reflection stops trying. Crosses its arms. Looks at real Rebekah with tired contempt.

It steps out of the mirror in silence.

- **Level:** 10
- **Role:** Elite (Controller)
- **HP:** 150 | **Damage:** 11 | **Accuracy:** 10 | **AR:** 6
- **XP:** 1,800
- **Attributes:** CHA 10, WIS 7, INT 7, STR 4, DEX 4, CON 7
- **Attacks:** 1

#### Identity Crisis — Taunt Sequence
1. "They love what you do for them. That isn't the same thing."
2. "You learned to sing because silence meant they weren't coming back."
3. "Name one person in this party who would cry if you never came home."
4. "The moment your voice goes, so does their interest. You've always known this."

#### Phase 2: Counter-Bard

##### Dissonant Counter
- **Type:** Skill (Reaction)
- **Cost:** None (innate)
- **Cooldown:** 10s
- **Duration:** 6s suppression
- **Targeting:** Enemy (Rebekah)
- **Rules:**
  - When Rebekah activates a song, the echo activates a counter-song that suppresses it for 6s.
  - Only counters one song at a time — the echo does not have [Harmonic Memory](../../../classes/temporal-bard.md) and must commit each counter to a single suppression.
  - **Weakness:** Rebekah *does* have Harmonic Memory (L4). If she layers faster than the echo can counter, the suppression breaks and the extra songs play through.

##### Temporal Snare
- **Type:** Spell
- **Cost:** None (innate)
- **Cooldown:** 12s
- **Duration:** 6s
- **Targeting:** Enemy (Rebekah)
- **Rules:**
  - Reversed [Tempo Boost](../../../classes/temporal-bard.md). Slows Rebekah's actions by 25% for 6s.
  - Standard damage on the initial hit.

##### Silence Aura
- **Type:** Passive (proximity)
- **Rules:**
  - Within melee range of the echo, songs have a 50% chance to fail — including [Dust Note](../../../classes/temporal-bard.md).
  - Forces Rebekah to fight at range.
  - The counter: stay at range, layer songs, and keep plucking Dust Notes between them.

**Narrative:** Rebekah's fight is tonally different from the others. She doesn't get angry — she gets sad. The echo is the version of herself that stopped trying. The breakthrough isn't fury — it's conviction.

She starts by plucking at the empty air. No instrument, no stage, no audience — just [Chrono Resonance](../../../classes/temporal-bard.md) letting her fingers find the strings only a Temporal Bard can feel. The first note is **Dust Note**, the smallest song in her arsenal — one plucked string, one stolen second, 1d4 decay damage to the echo. It's almost nothing. She plays it again. And again. In between, she sings.

Tempo Boost on herself. Dissonant Chord on the echo. Veil of Offbeats so the echo's snares drift around her. The echo counters one song, Rebekah starts another, and another. Harmonic Memory lets her hold more songs than the echo can suppress. The room fills with music — her voice, the invisible strings, the small steady rain of Dust Notes chipping at the echo's HP. None of it is fast. None of it is flashy. But the echo is alone, without Harmonic Memory, and every counter it throws leaves another of her songs playing through.

Rebekah is the last person you'd expect to win a 1v1. She wins by being the most Rebekah she can possibly be — refusing to stop singing, one tiny note at a time, until the echo runs out of silence.

**Story beat:** Rebekah encouraged [Selene](../../../characters/party/selene.md) to look in the first mirror. Now Selene is at the barrier for Rebekah. Reciprocity.

**Drops:** **Shard of Purpose** — Mirror fragment that vibrates at a frequency only the wearer can hear. +10% song and buff duration. *"Your voice carries further than you know."*

---

## Room 3: Seasonal Showroom

### Reaper Mannequin

A tall mannequin in a hooded black robe, carrying a full-sized plastic scythe that's stopped being plastic. Moves with deliberate, sweeping motions.

- **Level:** 10
- **Role:** Elite (Brute)
- **HP:** 150 | **Damage:** 11 | **Accuracy:** 10 | **AR:** 6
- **XP:** 1,800
- **Attributes:** STR 10, CON 10, DEX 4, INT 4, WIS 7, CHA 4
- **Attacks:** 1

#### Reap
- **Type:** Skill
- **Cost:** None
- **Cooldown:** 10s
- **Duration:** Instant
- **Targeting:** Enemy (Cone — up to 2 targets in front)
- **Rules:**
  - Wide scythe arc: 16 physical damage to primary target, 11 to secondary.
  - Telegraphed by a 2s wind-up (the reaper draws the scythe back behind its body).
  - Players who recognize the tell can step out of the arc.
  - **Lesson:** "Don't stand in front of this."

#### Slow Advance
- **Type:** Passive
- **Cost:** None
- **Rules:**
  - Moves at 50% speed. Cannot be hastened.
  - Immune to Fear (it is fear).
  - This mob is about positioning — it's slow but devastating if it catches you.

**Drops:** Plastic Scythe (Uncommon weapon, 7-12 physical, two-handed, -2 accuracy due to weight)

---

### Skeleton Arm Crawler

A skeletal arm and hand that erupts from the graveyard display floor, grabbing at ankles.

- **Level:** 10
- **Role:** Minion
- **HP:** 15 | **Damage:** 5 | **Accuracy:** 10 | **AR:** 3
- **XP:** 150
- **Attributes:** STR 7, DEX 7, CON 4, INT 4, WIS 4, CHA 4
- **Attacks:** 1

#### Ankle Grab
- **Type:** Skill
- **Cost:** None
- **Cooldown:** None
- **Duration:** 3s root
- **Targeting:** Enemy
- **Rules:**
  - Melee attack (must be adjacent / stepped on): 5 physical damage.
  - On hit: target is rooted for 3s (can still attack but cannot move).
  - Destroyable in one hit from most weapons.
  - Comes in groups of 4-6. Individually trivial; collectively they pin you in place for the Reaper.

**Drops:** None

---

### Clown Mannequin

A mannequin in a full clown costume — rainbow wig, red nose, oversized shoes. Carries a comically large mallet and a rubber horn. Not funny when it's trying to kill you.

- **Level:** 10
- **Role:** Elite (Controller)
- **HP:** 150 | **Damage:** 11 | **Accuracy:** 10 | **AR:** 6
- **XP:** 1,800
- **Attributes:** CHA 10, STR 10, DEX 4, INT 4, WIS 7, CON 7
- **Attacks:** 1-2

#### Honk Horn
- **Type:** Skill (Taunt)
- **Cost:** None
- **Cooldown:** 12s
- **Duration:** 3s
- **Targeting:** Enemy
- **Tags:** Compulsion, Sonic
- **Rules:**
  - Squeezes the horn. Target must make a Will check (DC 10).
  - Failure: **Taunted** for 3s — forced to attack the Clown (cannot select other targets).
  - If the taunted target is the party's tank, this is manageable. If it grabs a healer or caster, it's a problem.
  - **Lesson:** Forced engagement. The party learns that CC can affect *them*, not just mobs.

#### Mallet Slam
- **Type:** Skill
- **Cost:** None
- **Cooldown:** 10s
- **Duration:** 2s stun
- **Targeting:** Enemy
- **Rules:**
  - Overhead mallet strike: 14 physical damage.
  - On hit: target is stunned for 2s (cannot act).
  - Telegraphed by the Clown lifting the mallet over its head (1.5s wind-up).
  - Dodge window exists if you recognize the tell.

**Drops:** Oversized Mallet (Uncommon weapon, 8-13 physical, two-handed. Slow but hits hard. Has a rubber squeak on impact.)

---

### Straitjacket Mannequin

A mannequin in a torn straitjacket, arms wrapped tight. Thrashes against its restraints. When it breaks free, things get worse.

- **Level:** 10
- **Role:** Elite (Brute)
- **HP:** 150 | **Damage:** 11 | **Accuracy:** 10 | **AR:** 6
- **XP:** 1,800
- **Attributes:** STR 10, CON 10, DEX 7, INT 4, WIS 4, CHA 4
- **Attacks:** 1 (2 when Berserked)

#### Berserk
- **Type:** Skill (Self-buff)
- **Cost:** None
- **Cooldown:** Once per combat
- **Duration:** 10s
- **Targeting:** Self
- **Rules:**
  - Triggers automatically when HP drops below 50% (75 HP).
  - Breaks free of straitjacket restraints — and any active CC (stun, root, charm).
  - For 10s: +3 damage per hit (14 total), gains a second attack per round, immune to CC.
  - **The anti-control threat.** You can't lock it down once it's Berserked. Burn it fast.
  - Telegraphed by the jacket tearing and a guttural shriek.

```text
┌──────────────────────────────────────────────┐
│ STATUS: Berserk                              │
├──────────────────────────────────────────────┤
│ Type: Buff (Self)                            │
│ Source: Straitjacket Mannequin               │
│ Duration: 10s                                │
│ Stacks: 0 (Does not stack; one-time)         │
│ Dispel: No                                   │
├──────────────────────────────────────────────┤
│ Summary: Restraints broken. Uncontrollable.  │
├──────────────────────────────────────────────┤
│ Numbers:                                     │
│ - +3 damage per hit                          │
│ - Gains second attack per round              │
│ - Immune to all CC effects                   │
│ - Breaks all current CC on activation        │
└──────────────────────────────────────────────┘
```

**Drops:** Torn Straitjacket Scraps (Common, crafting material)

---

### Obvious Mimic (Prize Chest)

A treasure chest sitting in a carnival prize booth. It has teeth-shaped edges, wiggles slightly, and there's a "WINNER!" sign above it. Comically obvious.

- **Level:** 10
- **Role:** Normal (Beast)
- **HP:** 60 | **Damage:** 9 | **Accuracy:** 10 | **AR:** 8 (hard shell)
- **XP:** 600
- **Attributes:** STR 9, CON 9, DEX 4, INT 4, WIS 4, CHA 4
- **Attacks:** 1

#### Jaw Snap
- **Type:** Skill
- **Cost:** None
- **Cooldown:** 8s
- **Duration:** 2s root
- **Targeting:** Enemy (interacting character or nearest)
- **Rules:**
  - On interact (opening/looting): automatic hit, 11 physical damage + 2s root (arm stuck in mouth).
  - After initial snap: standard melee attacks (9 damage).
  - If the party spots it before interacting, it's just a normal fight with no surprise round.

**Narrative:** This is the one [Selene](../../../characters/party/selene.md) spots immediately. "I'd never get fooled by a stupid mimic." (Setup for Room 5.)

**Drops:** Handful of plastic gold coins (worthless, cosmetic)

---

## Room 4: Back Storage Maze

### Crawling Torso

A half-assembled animatronic groundbreaker prop — just a torso and arms. Drags itself along the floor with jerky, mechanical motions. Clearly unfinished. Still coming for you.

- **Level:** 10
- **Role:** Normal (Beast)
- **HP:** 60 | **Damage:** 9 | **Accuracy:** 10 | **AR:** 4 (exposed internals)
- **XP:** 600
- **Attributes:** STR 9, DEX 4, CON 9, INT 4, WIS 4, CHA 4
- **Attacks:** 1

#### Ankle Grab
- **Type:** Skill
- **Cost:** None
- **Cooldown:** 8s
- **Duration:** 3s root
- **Targeting:** Enemy
- **Rules:**
  - Melee attack from floor level: 6 physical damage.
  - On hit: target is rooted for 3s.
  - Moves at 25% speed (dragging itself). Relies on ambush positioning and tight corridors.
  - Can be heard approaching — servo whine and scraping plastic.

**Drops:** Animatronic Servo (Common, crafting material)

---

### Giant Spider Prop

A decorative giant spider that was six feet of wire and fake fur. Now it's six feet of wire and fake fur that wants to eat you. Webs corridors shut and drops from shelves.

- **Level:** 10
- **Role:** Elite (Controller)
- **HP:** 150 | **Damage:** 11 | **Accuracy:** 10 | **AR:** 4
- **XP:** 1,800
- **Attributes:** DEX 10, STR 7, CON 7, INT 4, WIS 7, CHA 4
- **Attacks:** 1-2

#### Web Corridor
- **Type:** Skill
- **Cost:** None
- **Cooldown:** 15s
- **Duration:** Until destroyed
- **Targeting:** Location (corridor section)
- **Rules:**
  - Blocks a corridor section with thick webbing.
  - Characters can force through (STR check DC 10, takes 1 round) or destroy it (15 HP, vulnerable to fire — Vanessa's specialty).
  - Used to cut off escape routes or split the party.

#### Venomous Bite
- **Type:** Skill
- **Cost:** None
- **Cooldown:** 10s
- **Duration:** 6s (DoT)
- **Targeting:** Enemy
- **Rules:**
  - Melee attack: 8 physical damage.
  - On hit: 2 poison damage per 2s for 6s (6 total).
  - Movement speed reduced by 25% for the duration.

#### Ceiling Drop
- **Type:** Skill (Ambush)
- **Cost:** None
- **Cooldown:** Once per combat
- **Duration:** Instant
- **Targeting:** Enemy
- **Rules:**
  - First attack from stealth (hidden on top of shelving unit).
  - Drops onto target: 14 physical damage + 2s prone.
  - Selene's scouting (Perception) can spot it before it drops.

**Drops:** Spider Silk Thread (Uncommon, crafting material — strong as steel wire)

---

### Shrink-Wrapped Mannequin

A standard mannequin still wrapped in industrial plastic from storage. Tears free when someone walks past its pallet. The plastic clings, giving it crude armor but slowing it down.

- **Level:** 10
- **Role:** Normal (Brute)
- **HP:** 60 | **Damage:** 9 | **Accuracy:** 10 | **AR:** 10 (plastic wrap armor)
- **XP:** 600
- **Attributes:** STR 9, CON 9, DEX 4, INT 4, WIS 4, CHA 4
- **Attacks:** 1

No special abilities. Moves at 50% speed due to wrapping. AR is higher than normal (10 vs 6) because the plastic absorbs impacts, but fire damage ignores the AR bonus entirely (melts the wrap).

**Tactical note:** Vanessa's fire spells are ideal but dangerous in tight corridors with allies nearby. This mob forces the "friendly fire" question again in a new context.

**Drops:** Industrial Plastic Sheeting (Common, crafting material)

---

### Severed Hand Swarm

A pack of rubber prop hands that have started crawling on their own, like Thing from the Addams Family. Individually pathetic. In groups, they grab weapons, arms, and interfere with everything.

- **Level:** 10
- **Role:** Minion
- **HP:** 15 | **Damage:** 5 | **Accuracy:** 10 | **AR:** 2
- **XP:** 150
- **Attributes:** DEX 9, STR 4, CON 4, INT 4, WIS 4, CHA 4
- **Attacks:** 1

#### Interfere
- **Type:** Passive
- **Cost:** None
- **Rules:**
  - For every 2 Severed Hands in melee with a target, that target suffers -1 accuracy (they're grabbing your weapon arm, climbing your legs, etc.).
  - Maximum -3 accuracy from 6+ hands.
  - Individually destroyable in one hit. The problem is there are always more.

Comes in groups of 4-8. They swarm from behind shelving when combat starts nearby.

**Drops:** None (they're rubber)

---

### Candy Bowl Mimic

A plastic "Take One" candy bowl sitting on a shelf. Looks completely normal. There are even wrapped candies visible inside. Reaches in and — *chomp*.

- **Level:** 10
- **Role:** Normal (Beast)
- **HP:** 60 | **Damage:** 9 | **Accuracy:** 10 | **AR:** 8
- **XP:** 600
- **Attributes:** STR 9, CON 9, DEX 4, INT 4, WIS 4, CHA 4
- **Attacks:** 1

#### Jaw Snap
- **Type:** Skill
- **Cost:** None
- **Cooldown:** 8s
- **Duration:** 2s root
- **Targeting:** Enemy (interacting character)
- **Rules:**
  - On interact: automatic hit, 11 physical damage + 2s root (hand stuck).
  - Unlike the Obvious Mimic in Room 3, there is **no visual tell**. Looks like a normal candy bowl.
  - After initial snap: standard melee attacks.

**Drops:** Whatever candy was actually in the bowl (Common consumable — minor 5 HP heal. Tastes like plastic.)

---

### Cash Register Mimic

A dusty cash register sitting on a counter in the storage area. The drawer is slightly open, showing bills inside. Press a button and — *cha-ching, chomp*.

- **Level:** 10
- **Role:** Normal (Beast)
- **HP:** 60 | **Damage:** 9 | **Accuracy:** 10 | **AR:** 10 (metal casing)
- **XP:** 600
- **Attributes:** STR 9, CON 9, DEX 4, INT 4, WIS 4, CHA 4
- **Attacks:** 1

#### Jaw Snap
- Same as Candy Bowl Mimic. 11 physical damage + 2s root on interact.
- The "cha-ching" sound on the opener is both the register opening and the mimic's attack sound.

**Drops:** Handful of real dollar bills (Common — actually worth money, but not much)

---

## Room 5: Employee Hallway

### Mimic Couch

A worn break room couch. Looks exhausted and inviting — sagging cushions, a throw blanket draped over one arm. It's been a long dungeon. Surely this one's safe.

It is not safe.

- **Level:** 10
- **Role:** Normal (Beast)
- **HP:** 60 | **Damage:** 9 | **Accuracy:** 10 | **AR:** 4 (upholstery)
- **XP:** 600
- **Attributes:** STR 9, CON 9, DEX 4, INT 4, WIS 4, CHA 9 (deceptively inviting)
- **Attacks:** 1

#### Swallow
- **Type:** Skill
- **Cost:** None
- **Cooldown:** N/A (opener only)
- **Duration:** Until freed
- **Targeting:** Enemy (the fool who sat/dove in)
- **Rules:**
  - On interact (sitting, diving, lying down): automatic hit.
  - Target is swallowed to the waist. Legs sticking out, kicking.
  - Deals 3 physical damage per 2s (chip damage — annoying, not lethal).
  - Target can free themselves with a STR check (DC 8 — easy, but takes a round).
  - Allies can free the target with any attack that deals 10+ damage to the couch, or by pulling (STR check DC 6).
  - **Not actually dangerous** — 999 HP characters lose health at a rate of 1.5/s. It's embarrassing, not lethal.

**Narrative:** [Selene](../../../characters/party/selene.md) dives in without hesitation after a long dungeon. Gets swallowed to the waist. [Rebekah](../../../characters/party/rebekah.md) stops the party from helping immediately — she wants to savor the moment. Callback: *"I'd never get fooled by a stupid mimic."*

**Drops:** Couch Cushion (Common, cosmetic. Smells like mimic.)

---

## Room 6: The Spotlight Room

Boss encounter mobs are defined in [boss.md](boss.md).
