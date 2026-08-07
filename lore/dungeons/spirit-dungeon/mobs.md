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
- **XP:** ~0 class XP — the echo is a **trial**, not a lethal threat: it cannot kill you, only reward or break you. The payoff is the [Mirror Shard](#mirror-shard-drops), not levels. See [xp.md § Trials](../../../system/xp.md#trials-will-not-survival).
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

## Graveyard Set

### Scarecrow of the Fallow Row (Graveyard Miniboss)

A scarecrow lashed to a wooden cross-stake at the back of the graveyard, past the wrought-iron fence. Burlap sack head carved into a jack-o'-lantern grin, two embers for eyes. It doesn't move — at first. But the eyes track you, and every time a grave opens, they flare.

- **Level:** 10
- **Role:** Elite (Brute)
- **HP:** 150 | **Damage:** 11 | **Accuracy:** 10 | **AR:** 6
- **XP:** 1,800
- **Attributes:** STR 10, CON 10, WIS 7, DEX 4, INT 4, CHA 4
- **Attacks:** 1 (2 when freed)

Two-phase miniboss. **Bound** while its skeletons stand; **Freed** when the field is cleared.

#### Grave Toll (Passive — Bound phase)
- On the party entering the graveyard, the Scarecrow's eyes flare and **5 [Risen Skeletons](#risen-skeleton)** claw up from the graves.
- Every 15s it can re-raise **one** fallen Risen Skeleton (telegraph: the pumpkin eyes pulse and a low bell tolls). **Maximum 3 re-raises** per fight — then the graves run dry.
- The Scarecrow **frees itself the instant no Risen Skeleton stands and its re-raises are spent.**

#### Staked (Passive — Bound phase)
- While bound, the Scarecrow cannot move and is **out of melee reach behind the fence** — melee attacks can't connect.
- Ranged attacks and spells hit, but the straw body takes only **25% damage** (it doesn't much care). Casters can chip it, not kill it.
- The puzzle: cut down its congregation, don't waste time flailing at the post.

#### Sickle Fling (Bound phase)
- **Type:** Skill
- **Cost:** None
- **Cooldown:** 8s
- **Duration:** Instant
- **Targeting:** Enemy (Line)
- **Rules:**
  - Tears an arm free and hurls a rusted sickle down a lane: 12 physical, boomerangs back to its hand.
  - Telegraphed by the arm winding back across its body (2s). Step out of the lane.

#### Harvest (Freed phase)
- **Type:** Skill
- **Cost:** None
- **Cooldown:** 10s
- **Duration:** Instant
- **Targeting:** Enemy (Cone — up to 2 targets in front)
- **Rules:**
  - On freeing itself, the Scarecrow **rips the cross-stake out of the ground and swings it like a greatsword.** Wide arc: 16 physical to primary, 11 to secondary.
  - 2s wind-up tell (draws the stake back over its shoulder). The Reaper's old lesson — "don't stand in front of this."

#### Reap and Sow (Freed phase — signature, once per fight)
- **Type:** Skill
- **Cost:** None
- **Cooldown:** Once per combat (fires on freeing)
- **Duration:** Instant
- **Targeting:** Enemy
- **Rules:**
  - Its **first** swing on breaking free is an overhead smash that **knocks the struck target back 20 feet — over the fence, into the Carnival section.** 14 physical + 2s prone.
  - The victim lands across a [Zone Line](rooms.md#zone-lines-section-barriers): **threat and taunt don't cross it,** so Clint cannot Commanding Shout the Scarecrow back to him. The party fights the freed miniboss without their tank until he clears the gnomes and returns on foot.
  - **Narrative hook:** this is the beat that launches [Clint](../../../characters/party/clint.md) onto the [Whack-a-Gnome](#whack-a-gnome-game-mechanic--minion), forcing the graveyard and carnival to run at once — the "let's not find out" gun going off.

#### Immune to Fear (Passive)
- It is the thing in the field the crows fear. Cannot be Feared or Charmed.

**Drops:** Stitched Burlap Cowl (Uncommon armor, +4 AR, -1 CHA — smells of hay and grave dirt), Ember Eye (Uncommon accessory, +1 WIS, functions as a faint light source)

---

### Risen Skeleton

A skeleton clawing up out of a foam grave, animated by the Scarecrow. Rusted garden tools for weapons. Falls apart when hit hard — but there are more where it came from, until the graves run dry.

- **Level:** 10
- **Role:** Minion
- **HP:** 15 | **Damage:** 5 | **Accuracy:** 10 | **AR:** 3
- **XP:** 150
- **Attributes:** STR 7, DEX 7, CON 4, INT 4, WIS 4, CHA 4
- **Attacks:** 1

#### Grave-Bound (Passive)
- Animated by the [Scarecrow](#scarecrow-of-the-fallow-row-graveyard-miniboss). Takes **+50% damage from Turn Undead and divine-source abilities**.
- [Wade's](../../../characters/party/wade.md) kit shreds them even while **Broken** — this is the graveyard's gift to the compromised healer: he can't out-heal the room, but he can clear it. Gives Broken-Wade offense while his sustain is weak.
- Summoned/animated, so once [Clint](../../../characters/party/clint.md) hits **L4** here his [Smite: Sanction](../../../classes/paladin-of-the-system.md) also lands **+30% vs summoned entities** on them — his upgraded smite comes online against the very thing that raised them. (See the graveyard [progression beat](rooms.md#encounter-graveyard-set).)

#### Crawling Remains (Passive)
- When a Risen Skeleton is downed, its severed arm often keeps moving — **~50% of the time** it flops into the grass and becomes a [Skeleton Arm Crawler](#skeleton-arm-crawler) after ~2s.
- The arm is **trivial to kill** — a stomp, a stray hit, anything one-shots it — but ignored, it grabs an ankle (3s root) at the worst possible moment. The [Grave Mist](rooms.md#graveyard-grave-mist) hides it until it strikes.
- **Vigilance tax:** clear the arms as you drop the skeletons, or the graveyard floor is a minefield of roots when the Scarecrow finally breaks free.

Comes up in a pack of 5; the Scarecrow re-raises up to 3 more over the fight. The environmental **Skeleton Arm Grab** hazard (see [rooms.md](rooms.md#graveyard-skeleton-arm-grab)) fires independently of these minions.

**Drops:** None (bone dust)

---

### Skeleton Arm Crawler

A skeletal arm and hand that erupts from the graveyard display floor, grabbing at ankles — or the still-twitching remains of a downed [Risen Skeleton](#risen-skeleton) (see Crawling Remains). Hidden in the [Grave Mist](rooms.md#graveyard-grave-mist) until it grabs.

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
  - Comes in groups of 4-6. Individually trivial; collectively they pin you in place for the Scarecrow's Sickle Fling. (Distinct from the [Risen Skeletons](#risen-skeleton) the Scarecrow animates — these are the environmental grab hazard.)

**Drops:** None

---

## Carnival Set

### Whack-a-Gnome (Game Mechanic + Minion)

A carnival arcade game the size of a dining table, riddled with holes. Little gnomes pop up and down at random. Two padded mallets sit in brackets on either side. A hand-painted sign: "WHACK-A-GNOME — 1 PLAY. WINNERS GET TICKETS!"

**The only active enemy in the Carnival** — the Clown and Mimic stay passive (see below). The game activates when its **Start Game button is pressed** or a character steps up to play. (The Scarecrow's [Reap and Sow](#reap-and-sow-freed-phase--signature-once-per-fight) flings [Clint](../../../characters/party/clint.md) onto it — *landing* doesn't start it, but he sets it off leaning on the Start button while scrambling back from the asylum.) The instant it activates, the [Carousel](#carousel--the-motor) begins to turn and gnomes **erupt all at once:** a first wave leaps off the board into the party, and the machine keeps surfacing more **for as long as the carousel spins** — it does not run dry on its own.

**The Gnome (Minion):**

- **Level:** 10
- **Role:** Minion (Swarm)
- **HP:** 15 | **Damage:** 5 | **Accuracy:** 10 | **AR:** —
- **Reward:** 1 Ticket · **no XP** (zero-danger kill — [danger factor](../../../system/xp.md#xp-award-formula) ≈ 0; this is what stops the endless fountain from being a power-leveling exploit)
- **Attributes:** DEX 9, STR 4, CON 4, INT 4, WIS 4, CHA 4
- **Attacks:** 1 (ankle bite — trivial)
- **Defense:** **Invulnerable to all conventional damage.** The lone exception (see [Carnival Rules](#at-the-machine--burrowed)) is deliberately **not surfaced by [Identify](#what-system-identify-gives-clint)** — the party discovers it in-world.

Gnomes have two states — **at the machine** and **loose.**

#### At the Machine — Burrowed (Passive)
- On the board, gnomes are **untargetable and immune while down,** surfacing only ~1.5s at a time.
- **Carnival Rules:** at the machine, **only a Padded Mallet counts as a hit** — swords, spells, fists score "MISS." A mallet whack is an automatic one-shot **and dispenses 1 ticket** (flat, per gnome — win a lot by winning *often*, not big).
- **The source.** Every ~3s the machine surfaces a fresh gnome. If it isn't whacked inside its window, it **leaps off the board and joins the swarm on the party.** Whacking at the machine is the *only* way to cut the flow — which is why whoever lands on the game (Clint) is stuck manning it.
- **The machine never runs dry on its own.** Gnomes spawn endlessly *while the [Carousel](#carousel--the-motor) turns* — the carousel's motor drives the game. The **only** way to end the spawn is to **stop the carousel (kill all four mounts)**; whacking can't outpace it, only hold the loose swarm down. What Clint's console-boosted stamina buys this party is the ability to **man the source indefinitely** while the rest kill the carousel — not a way to make it stop on its own. (Smashing the machine itself, 60 HP, also halts it but **voids all tickets**; the System does not reward vandalism.)

#### Loose — Skittering Swarm (Passive)
- A gnome that escapes the board is a **mobile minion that is *still only killable by a mallet*** — swords, spells, and fire all score "MISS" on a gnome no matter where it is. Carnival rules don't stop at the machine's edge.
- **Random target, taunt-proof:** each loose gnome **picks a party member at random and charges,** immune to Taunt and every form of threat redirection. It will **cross zone lines** to reach them (into the graveyard, wherever they scattered), and per [Zone Lines](rooms.md#zone-lines-section-barriers) it **can't be taunted back** — only killed.
- **Non-mallet allies can't kill gnomes — but they can *control* them:** slow ([Dissonant Chord](../../../classes/temporal-bard.md)), shove, illusion-lure, or knock them into the [Cotton-Candy Webs](rooms.md#carnival-cotton-candy-web) to stick them in place for a mallet-bearer. (Burning the webs frees the trapped gnomes — a real tension with clearing them for movement.)
- **Only two mallets exist,** both chained to the machine on short tethers. Clint works the source on one; to arm a second hunter he must **tear the other mallet free (STR check) and throw it.** The hand-off to [Selene](../../../characters/party/selene.md) is the intended beat — and two mallet-bearers is the hard cap on gnome-killers.

#### Underfoot (Passive — stacking slow)
- Every **loose gnome** in melee with a target clamps onto legs and gear and **drags: −20% movement speed per gnome, stacking.** The bite is nothing; the *pile* is the problem. The more of them on you, the less you can move — it only ever gets worse until they're cleared.
- At **5 stacks the target is fully rooted** (−100%) — still able to act, but nailed in place for whatever else is inbound: the Scarecrow's [Sickle Fling](#scarecrow-of-the-fallow-row-graveyard-miniboss) lane, the Asylum's roving gurney, a carousel [Ground Slam](#carousel--the-motor). Accumulation is the kill vector; the gnomes just hold you still for the thing that actually hurts. (A rooted caster can still cast — [Vanessa](../../../characters/party/vanessa.md) keeps attacking while pinned — which is exactly why the Scarecrow targets her.)
- **You can't shake them off yourself.** Since nothing you can swing damages a gnome ([Carnival Rules](#at-the-machine--burrowed)), a swarmed caster stays pinned until a mallet-bearer peels them — a slow you cannot break on your own. Stacks fall off only as gnomes die. This is what turns "trivial nuisance" into "why can't I *move* — get them **off** me."

```text
┌──────────────────────────────────────────────┐
│ STATUS: Underfoot                            │
├──────────────────────────────────────────────┤
│ Type: Debuff (Snare)                         │
│ Source: Whack-a-Gnome (loose)                │
│ Duration: While gnomes remain in melee       │
│ Stacks: Yes (1 per adjacent loose gnome)     │
│ Dispel: No (kill the gnomes — Mallet only)   │
├──────────────────────────────────────────────┤
│ Summary: They're climbing your legs.         │
├──────────────────────────────────────────────┤
│ Numbers:                                     │
│ - -20% move speed per stack                  │
│ - 5 stacks = fully rooted (-100%)            │
│ - Cannot be cleansed; ends only when the     │
│   gnomes are cleared (Padded Mallet)         │
└──────────────────────────────────────────────┘
```

#### "Gnomes Rule!" (Passive — Sonic Aura)
- The gnomes never shut up. Every gnome — burrowed or loose — chants **"GNOMES RULE!"** on an endless squeaky loop, a wall of noise blanketing the whole carnival section. *(A deliberate easter-egg homage — see [author note](#gnomes-rule--author-note).)*
- **Interrupts casting:** each **"GNOMES RULE!"** is a 1-second Sonic jolt that cuts off an in-progress cast or channel — [Vanessa's](../../../characters/party/vanessa.md) spells and [Rebekah's](../../../characters/party/rebekah.md) sung songs get chopped; instant abilities ([Clint's](../../../characters/party/clint.md) Smites, [Selene's](../../../characters/party/selene.md) strikes) shrug it off. The debuff is **dispellable**, but the chant never stops, so it just re-lands — the real cure is fewer gnomes.
- **Coordination suffers:** stacked on the carnival's music and the zone's [acoustic seal](rooms.md#zone-lines-section-barriers), the din means only short, loud, shouted words carry — part of why [Vanessa's](../../../characters/party/vanessa.md) *"Use the mallet, you idiot!"* reaches [Clint](../../../characters/party/clint.md) only as a scream **relayed by [Strider](../../../characters/party/clint.md#patron-strider)** across the fence (see [the scan](#what-system-identify-gives-clint)).
- **Silence it** the same way you end the swarm: clear the gnomes (mallet) or stop the [Carousel](#carousel--the-motor).

```text
┌──────────────────────────────────────────────┐
│ STATUS: Gnomes Rule                          │
├──────────────────────────────────────────────┤
│ Type: Debuff (Sonic)                         │
│ Source: Whack-a-Gnome (the chant)            │
│ Duration: 1s (re-applied while they chant)   │
│ Stacks: No (refreshes)                       │
│ Dispel: Yes (but they just yell again)       │
├──────────────────────────────────────────────┤
│ Summary: "GNOMES RULE!" — you can't          │
│ concentrate.                                 │
├──────────────────────────────────────────────┤
│ Numbers:                                     │
│ - Interrupts any cast-time / channel ability │
│ - Instant abilities unaffected               │
│ - Ends when the gnomes are silenced (Mallet) │
└──────────────────────────────────────────────┘
```

> <a id="gnomes-rule--author-note"></a>*Author note: the gnomes' **"GNOMES RULE!"** chant is an intentional easter egg. The phrase began as running-joke graffiti in classic MMORPGs (EverQuest, World of Warcraft) and was popularized in the LitRPG scene by Aleron Kong's **The Land** series. Keep the wording verbatim — it's a genre wink, not a continuity slip.*

```text
┌──────────────────────────────────────────────┐
│ WHACK-A-GNOME                                │
├──────────────────────────────────────────────┤
│ Please use the provided MALLET.              │
│ Winners get tickets. Cheaters get nothing.   │
└──────────────────────────────────────────────┘
```

#### What System Identify Gives Clint

Clint's [Innate System](../../../characters/party/clint.md) is interface-free — no [popup](../../../system/ui-popups.md#5-system-identify--entity), he just *knows.* What he knows:

```text
Gnome (Whack-a-Gnome) — Identified
Level: 10 · Type: Construct (Animate Prop) · Threat: Trivial
HP: 15 | Damage: 5 | Accuracy: 10
Defense: INVULNERABLE
Reward: 1 Ticket · grants no XP
```

And that read is wrong in the way that matters. *Invulnerable,* it says — flat, no asterisk, no footnote about foam. The System isn't lying (nothing he can swing hurts them); it just declines to name the one implement that counts. So Clint reads *can't be killed,* pockets it, and starts hunting for a trick — a phase, a switch, a weak point — anything but the padded mallets in the brackets in plain sight. That's the gap [Vanessa](../../../characters/party/vanessa.md) has to scream across the field: *"THE MALLET, CLINT — HIT IT WITH THE MALLET."*

> *Strider, who reads the same data without any popup and is enjoying the silence, to Clint alone:* "Oh, this is going to be good."

**Drops — Whack-a-Gnome Mallet** (Common weapon, 3-6 physical vs normal foes). *Identify the mallet* and the answer the gnome-scan withheld is right there:

```text
Whack-a-Gnome Regulation Mallet
Banishes one gnome per strike; dispenses its ticket.
Non-regulation implements are not recognized by the game.
```

The clue exists — it's just on the object nobody thinks to scan mid-swarm. Two mallets exist, chained to the game on short tethers; tear one free (STR) to carry it off. Squeaks on impact.

---

### Carousel — The Motor

*(Mechanic + 4 Mount-Bosses.)* A spinning carousel of mutated animals, calliope music looping. **It drives the [Whack-a-Gnome](#whack-a-gnome-game-mechanic--minion):** gnomes surface and spawn only while the carousel turns. Stopping it is the one true off-switch for the flood — but four mounts guard it.

**The loop:**
- The motor sits at the central hub, with a **switch.** Flipping the switch stops the carousel — but any **living mount cranks it back on** as it swings past. The switch only sticks once **all four mounts are dead.** Killing the four *is* the off-switch.
- The four mounts are **fixed to their poles and cannot leave the carousel,** so the whole fight is **spatially optional.** Stay off the platform and they can't reach you; step to the edge and you're in it. (A careful party can skip the carousel entirely — yours, forced onto the whack-a-gnome, has to deal with it.)
- **From the edge:** the rotation delivers one mount into reach at a time — slow, methodical, safe.
- **Jumping onto the platform** to burst them makes the carousel **spin double-time → double gnome spawn.** The fast way floods Clint at the source. A patience test.
- **Reward:** stopping the carousel ends the gnome spawn. Mounts drop crafting material and tickets; the *real* payoff is the ticket total the long fight generates — a full clear can reach the **500** [Grand Prize](#ticket--prize-booth-mechanic) mimic (see [Prize Mimic](../../../items/accessories/mimic-pet.md)). [Rebekah](../../../characters/party/rebekah.md), a Temporal Bard, is the one who reads that the gnomes move to the carousel's beat.

Four animals, four mechanics. Each is **Elite (L10) — HP 150 | Damage 11 | Accuracy 10 | XP 1,800**, bound to its pole.

#### The Nightmare (Carousel Horse) — Charger
A fire-maned carousel horse with too many teeth. **AR 6.** Attributes STR 10, DEX 10, CON 7, INT 4, WIS 4, CHA 4.
- **Trample Charge** (Cooldown 8s): breaks from its pole to gallop a straight line — 14 damage + knockback + 1s prone to everything in the lane — then snaps back to its pole. Rears (2s tell) before charging. Punishes the backline.

```text
The Nightmare (Carousel Horse) — Identified
Level: 10 · Type: Construct (Carousel Mount) · Role: Elite (Charger)
HP: 150 | Damage: 11 | Accuracy: 10 | AR: 6
Tell: Rears (2s), then Trample-Charges its lane. Get out of the line.
```

#### The Gilded Lion — Bruiser
Brass lion, mane like blades. **AR 8.** Attributes STR 10, CON 10, CHA 7, DEX 4, INT 4, WIS 4.
- **Brass Roar** (Cooldown 12s): pulls the nearest enemy toward it — a taunt you can't refuse (2s) — then **Pounce Cleave** (14 damage, frontal arc). Front-loaded burst; don't get dragged in undefended.

```text
The Gilded Lion — Identified
Level: 10 · Type: Construct (Carousel Mount) · Role: Elite (Bruiser)
HP: 150 | Damage: 11 | Accuracy: 10 | AR: 8
Tell: Roars to drag the nearest fighter in, then Pounce-Cleaves. Don't get caught alone.
```

#### The Brass Swan — Flyer
A long-necked brass swan that lifts off its pole. **AR 4.** Attributes DEX 10, WIS 7, CON 7, STR 4, INT 4, CHA 4.
- **Take Wing** (Passive): leaves its pole to circle — evasion way up, hard to hit — pelting feathers (ranged chip).
- **Dive-Bomb** (Cooldown 10s): a big telegraphed plunge (16 damage). It is **grounded and vulnerable for ~2s after each dive** — the only reliable window to burst it. A timing check.

```text
The Brass Swan — Identified
Level: 10 · Type: Construct (Carousel Mount) · Role: Elite (Flyer)
HP: 150 | Damage: 11 | Accuracy: 10 | AR: 4
Tell: Airborne = hard to hit. Grounded ~2s after each Dive-Bomb — burst it then.
```

#### The Stone Elephant — Tank / Controller
A ponderous stone elephant. **AR 10 (stone).** Attributes STR 10, CON 10, WIS 7, DEX 4, INT 4, CHA 4.
- **Ground Slam** (Cooldown 10s): rears and stomps — shockwave AoE, 12 damage + knockdown to everyone nearby (2s tell). Area denial; don't cluster. Slow and high-AR — the anchor and the DPS check.

```text
The Stone Elephant — Identified
Level: 10 · Type: Construct (Carousel Mount) · Role: Elite (Tank)
HP: 150 | Damage: 11 | Accuracy: 10 | AR: 10
Tell: Ground Slam is a telegraphed AoE (2s) — spread out. High AR: the DPS check.
```

**Drops (collective):** Carousel Brass (Uncommon crafting material) + a share of tickets. *No mount-summoning bridle* — the pet is this section's signature reward, deliberately kept singular.

---

### Ticket & Prize Booth (Mechanic)

Tickets won at the Whack-a-Gnome are spent at the prize booth counter — the one the [Clown Mannequin](#clown-mannequin) guards. Tickets are shared party loot (they go in the fanny pack).

- **Playing by the rules (redeem):** present tickets at the counter and the Clown honors the exchange — stays passive, hands over the prize, squeaks its horn approvingly. The System enforces arcade fair-play.
- **Cheating (a booth violation — grabbing a prize or the chest without paying, or attacking the Clown or mimic):** everything triggers at once. The Clown [drops the act](#drops-the-act-champion-on-aggro) and fights at Champion strength, the [Obvious Mimic](#obvious-mimic-prize-chest) wakes, the unsold stock [animates and defends itself](#prize-rally-on-aggro) — and the [whole dungeon converges](#store-wide-alert-dungeon-response).

**Why robbery doesn't pay.** The prizes are real — they have to be; the mimic [eats one off the counter](#the-100-ticket-set--the-temptation) and it resurfaces at the boss — but they are not *lootable*. The stock fights back, and an animated prize beaten in the rally is **destroyed**: a snapped saber, shattered shades. **Redemption is the only way a prize leaves the booth intact.** Stack the store-wide convergence on top and the math is closed — rob the booth and you fight a Champion clown, the mimic, the merchandise itself, and every remaining mob in the dungeon at once, and the shelf you did it for is wreckage by the end.

| Tickets | Prize | Effect |
|---------|-------|--------|
| 5 | Bag of Kettle Corn | Consumable — restores 40 HP. Tastes real. |
| 10 | **Carnival Shades** | Common accessory — **reduces strobe/flash accuracy penalties by 3.** (Save these for the Asylum.) |
| 15 | Foam Finger of Provocation | Common accessory — once per fight, taunt a single target for 3s. "WE'RE #1." |
| 25 | Plush Reaper | Uncommon accessory — +1 WIS. A stuffed toy of the thing you just killed. |
| **100 (each)** | **The Big-Prize Shelf** | One genuinely great class item per member — see [The 100-Ticket Set](#the-100-ticket-set--the-temptation). Five of them = the full **500**. |
| **250 (each)** | **The Center Rack** | A cut above — an Epic weapon, shield, or coat. A full clear affords **exactly two.** See [The 250-Ticket Rack](#the-250-ticket-rack--two-or-none). |
| **500** | **GRAND PRIZE — the Mimic** | The gold-chained chest itself. **500 is only reachable by clearing the *entire* carnival — Whack-a-Gnome *and* [Carousel](#carousel--the-motor).** Redeem it and the [Clown](#clown-mannequin) hands it over tame: a soulbound [Prize Mimic pet](../../../items/accessories/mimic-pet.md). Try to *take* it without paying and it's the greed-trap ([Obvious Mimic](#obvious-mimic-prize-chest) + Clown). |

**Tickets:** every gnome killed by a mallet — Clint at the source or Selene loose — yields **1 ticket** (flat; gnomes grant no XP, only tickets). At ~1 ticket a whack the counter climbs on *volume*, so the totals track fight length: a short carnival nets a handful (the 10-ticket Carnival Shades are a quick, easy grab), while reaching the 500 Grand Prize takes the **full, dragged-out Carousel clear** — hundreds of gnomes whacked over a long fight, topped up by the mounts' ticket drops. The grind *is* the price.

**How the winnings pay out — five Gold Century-Tickets.** When the party cashes a full clear (~500), the [Clown](#clown-mannequin) counts it out as **five gold "100" tickets, one pressed into each member's hand** — their equal share of the take (plus any loose change from the grind). Each gold ticket is exactly one [100-set](#the-100-ticket-set--the-temptation) item; the booth makes change for the odd [250-rack](#the-250-ticket-rack--two-or-none) price. This is the prop that makes the sacrifice land: **nobody can buy the 500 chest alone** — it takes all five gold tickets, physically surrendered, to reach the mimic.

**Design intent:** the **Carnival Shades** (10) are the baseline reward — engaging the whack-a-gnome pays off when the Asylum strobes hit -5 accuracy. The **Mimic** (500) is the reward for going the whole distance: same object, **two outcomes decided by virtue** — *buy* it and you tame it, *steal* it and it bites. A normal or impatient party never reaches 500 and only ever meets the mimic as a trap; a thorough party earns a pet.

### The 100-Ticket Set — the Temptation

A full carnival clear nets roughly **500 tickets** — enough for exactly one marquee splurge: **five 100-ticket prizes** (a great item for everyone), **two 250-ticket [rack](#the-250-ticket-rack--two-or-none) picks** (two of you, much stronger), or the **single 500-ticket Mimic.** The shelf is stocked to make the sacrifice hurt.

Each 100-ticket prize is a real Rare-tier upgrade, carnival-skinned:

| For | Prize | Effect |
|---|---|---|
| [Clint](../../../characters/party/clint.md) | **Strongman's Belt** (high-striker prize) | +2 STR, +5% threat. Ring the bell. |
| [Vanessa](../../../characters/party/vanessa.md) | **Sharpshooter's Monocle** (shooting gallery) | +5% spell crit, and her targeted AoE spells can **exclude allies** — the fix to her friend-frying problem. |
| [Rebekah](../../../characters/party/rebekah.md) | **Golden Calliope Reed** | +15% song and buff potency. |
| [Wade](../../../characters/party/wade.md) | **First-Place Blue Ribbon** | +15% healing output — which, while he's **Broken**, is the thing he wants most in the world. |
| [Selene](../../../characters/party/selene.md) | **Funhouse Shard** | +5% crit, +stealth. Her own tempting prize — the one she trades away for the puppy. |

**The beat — five gold tickets, one puppy.** Each member is handed a Gold Century-Ticket ([payout format](#ticket--prize-booth-mechanic)) and drifts to the item it buys: [Clint](../../../characters/party/clint.md) to the [shield](#the-250-ticket-rack--two-or-none) he can finally use, [Vanessa](../../../characters/party/vanessa.md) to the Monocle that ends her friendly-fire, [Wade](../../../characters/party/wade.md) to the Blue Ribbon that claws back his lost healing, [Rebekah](../../../characters/party/rebekah.md) to the Reed, [Selene](../../../characters/party/selene.md) to her Shard. Everyone's drooling.

Then Selene clocks the mimic — 500, out of reach alone — and does the one thing that keeps this from reading as manipulation: **she spends her own gold ticket on the chest first,** giving up her Funhouse Shard before she asks anyone for anything. *Then* the eyes. The campaign goes person to person, and the **order they cave is the characterization:**

- **[Wade](../../../characters/party/wade.md) folds first.** The one who's **[Broken](#echo-double--base-mechanic)** and wants healing more than anyone hands over the **First-Place Blue Ribbon** — the item that would give it back — because after the mirror he needs the *joy* more than the stat. Quiet, and it guts you.
- **[Rebekah](../../../characters/party/rebekah.md)** is an easy yes, delighted by the whole absurd thing.
- **[Vanessa](../../../characters/party/vanessa.md) and [Clint](../../../characters/party/clint.md) are the holdouts** — the two whose items are most *needed* (the friendly-fire fix; the shield that would finally make Clint a tank). They resist on cold logic, and crumble last.

**The button:** the instant the five-gold-ticket group gift crests into something genuinely moving, Selene ruins it — names the mimic **Qubit** on the spot (*"it's in superposition — both a chest and a monster at once"*), and it promptly **eats Wade's surrendered Blue Ribbon** right off the counter. Everyone stares. Warmth and gag, back to back. *(The ribbon is **not** destroyed — a [reluctant bag of holding](../../../items/accessories/mimic-pet.md) hoards what it swallows, it doesn't burn it. This plants the [boss-fight payoff](boss.md#phase-3-manager-exposed).)* Mechanically the whole thing is a terrible trade. That's what makes it land — and Clint walks out still swinging the plastic machete, shieldless, **by choice.**

### The 250-Ticket Rack — Two, or None

A tier above the [100-set](#the-100-ticket-set--the-temptation): fewer, better, and priced so a full clear (~500 tickets) buys **exactly two.** Epic-tier, and pointedly aimed at the party's real gaps.

| Prize | Effect | The pull |
|---|---|---|
| **Carousel Saber** | Epic one-handed sword — 12–18 physical, +5% crit. A *real* weapon. | [Clint's](../../../characters/party/clint.md) plastic machete finally retired — **or** the first weapon [Wade](../../../characters/party/wade.md) has ever held (he's been fighting the Scarecrow with his fists). This is the sword Clint eyes on the counter in [Ch 20](../../../story/chapter-summaries.md) and nearly grabs. |
| **High-Striker Bulwark** | Epic shield — +6 AR, enables shield abilities. | [Clint](../../../characters/party/clint.md) unlocked **Shield Mastery** and **Shield Bash** at L4 and has *no shield to use them* ([Ch 20](../../../story/chapter-summaries.md)). This is the item that turns him from a man with a machete into an actual tank. |
| **Ringmaster's Coat** | Epic armor — +5 AR, +1 CHA, a small all-round bump. | Universal upgrade; whoever's squishiest wants it. |

**The sharper knife:** the 250 rack is worse for the party's wallet and better for their power. Two picks could make [Clint](../../../characters/party/clint.md) a genuine sword-and-board tank in a single stop (**Saber + Bulwark**) — and that's the *entire* budget: no mimic, no five-item set. Three tiers, one pool of ~500 tickets, three different parties you could walk out as: **everyone a little better (5×100), two of you a lot better (2×250), or one ridiculous puppy (500).** They pick the puppy — and Clint keeps swinging the plastic machete, shieldless, by choice.

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

#### Booth Guardian (Passive)
- The Clown does **not** aggro on sight. It patrols the prize booth, honors [ticket redemptions](#ticket--prize-booth-mechanic), and every so often **bonks the [Obvious Mimic](#obvious-mimic-prize-chest) on the lid** to make it hold still — the chest freezes and its eye-glow winks out for a beat. (This foreshadows the mimic while keeping it spottable.)
- Turns hostile only if a character **attacks it, attacks the mimic, or takes a prize without paying.** Then it opens with Honk Horn as written.
- **Threshold tell:** mere *contact* with the mimic (poking it, [petting it](#obvious-mimic-prize-chest)) is not theft — the Clown **visibly tenses** (grip whitening on its horn, a step forward it doesn't complete) but holds. It only snaps the instant someone tries to *take* or *strike*. The strain is the telegraph: the party can read exactly where the line is.

#### Drops the Act (Champion on Aggro)
- The patrolling vendor is the Elite block above. The instant the booth is violated, the Clown **drops the act** — the painted smile splits a little wider, the posture straightens *wrong* — and it fights as a **Champion: HP 360 | Damage 13 | Attacks 2 | XP 6,000** (framework 6x HP / 1.5x dmg / 10x XP; CHA 12 with the Champion +2). Honk Horn and Mallet Slam keep their listed cooldowns.
- At Champion, **Mallet Slam becomes an area slam:** the overhead strike lands as a telegraphed shockwave (2m radius, same 14 damage + 2s stun to everything caught) — the framework's required area-denial mechanic. Same 1.5s wind-up tell; the answer is *spread out*.
- It never fights alone: aggro simultaneously triggers the [Prize Rally](#prize-rally-on-aggro) and the [Store-Wide Alert](#store-wide-alert-dungeon-response). This is a floor-boss-scale fight the party *chose* to start.

#### Prize Rally (On Aggro)
- Every **unsold** prize in the booth animates and defends it. Sold and redeemed items are unaffected — they belong to their buyers.
- The stock fights with what it is: the **Carousel Saber** slashes as a flying blade, the **High-Striker Bulwark** body-checks and walls off the counter, the **Carnival Shades** strafe with strobe-flashes (**-5 accuracy** on whoever they're facing — the Asylum's trick, turned on the party early), the **Foam Finger** taunts ("WE'RE #1"), the **Plush Reaper** goes for ankles, the **Strongman's Belt** constricts (root, STR check to break).
- **Stat guidance:** shelf trinkets (5–25 ticket tier) fight as **Minions** (15 HP, 5 dmg); the [100-set](#the-100-ticket-set--the-temptation) as **Normals** (60 HP, 9 dmg); the two [250-rack](#the-250-ticket-rack--two-or-none) Epics as **Elites** (150 HP, 11 dmg). **No XP from any of them** — the System scores this as vandalism, not combat.
- **Beaten prizes are destroyed.** A "killed" prize breaks — snapped saber, shattered monocle, a belt torn in half. Nothing that fought can be looted. **Redemption is the only way a prize leaves the booth intact.**

#### Store-Wide Alert (Dungeon Response)
- Any [booth violation](#ticket--prize-booth-mechanic) flips the **entire remaining dungeon** hostile at once. The PA crackles overhead — the [Store Manager's](boss.md) voice, pleasant and dead: *"Security to the showroom, please. All associates."* — and every living mob abandons its set and converges on the party.
- **Zone lines stop holding.** Set-by-set containment ([rooms.md](rooms.md#zone-lines-section-barriers)) is store policy, and the store just revoked it: mobs cross the fences freely for the duration. (The threat/taunt rules across lines still apply as written — bodies cross, taunts don't.)
- Only the boss stays put — the Manager doesn't leave the office. It watches the cameras and takes notes for your review.
- The alert ends when the party wipes, flees the dungeon, or kills everything that answered the call. Survivable in principle — that's the point.

**Design intent — why the booth can't be robbed:** the Clown is beatable on purpose; the deterrent is the *bill*. Violence buys a Champion clown plus the animated merchandise plus every remaining mob in the dungeon, simultaneously, with no rest between waves — and the prizes it was all for **break when beaten.** Honest play buys the same items for tickets, one attraction at a time. There is no build, level, or party size for which robbing the booth beats playing the game.

**Drops:** Oversized Mallet (Uncommon weapon, 8-13 physical, two-handed. Slow but hits hard. Has a rubber squeak on impact.)

---

## Asylum Set

The deepest, darkest stripe. A shock-therapy tableau powered by a wheeled ECT cart, a hall of hard strobes (-5 accuracy, persistent — see [rooms.md](rooms.md#asylum-concentrated-strobe)), and a locked "AUTHORIZED PERSONNEL ONLY" door held by two guards. This is where the party's frayed sustain — [Wade](../../../characters/party/wade.md) is still **Broken** — finally bites.

### Shock Cart (Destructible Object / Hazard)

The wheeled ECT cart wired to the Patient's **treatment gurney** — where the Patient is strapped down, stationary. (Not to be confused with the *loose* wheeled gurney that careens the room as a [strobe hazard](rooms.md#asylum-concentrated-strobe) — two different gurneys.)

- **HP:** 30 | **AR:** 0
- **Treatment Pulse:** while an [Asylum Orderly](#asylum-orderly) is channeling, the cart discharges **every 5s.** Each discharge **flares the Asylum strobes to a 1s blackout** (everything in the section drops to **-8 accuracy** for that second) and advances the Treatment by one pulse.
- **The clock — 4 pulses ≈ 20 seconds** to a completed Treatment (see [Lobotomized Patient](#lobotomized-patient-conditional-add)). The party has that window to **smash the cart (30 HP)** or **kill/interrupt the channeling Orderly** — either stops the strobe flares and freezes the Treatment. Interrupting doesn't rewind progress; it just stops the clock.

---

### Asylum Orderly

A mannequin in a stained white coat, calm and unhurried, pressing shock paddles to the Patient's temples. Comes as a pair with the Head Surgeon.

- **Level:** 10
- **Role:** Normal (Controller)
- **HP:** 60 | **Damage:** 9 | **Accuracy:** 10 | **AR:** 6
- **XP:** 600
- **Attributes:** WIS 9, INT 7, CHA 7, STR 4, DEX 4, CON 4
- **Attacks:** 1

#### Administer Treatment (Channel)
- **Type:** Skill (Channel)
- **Targeting:** The Patient (gurney)
- **Rules:**
  - Stands at the treatment gurney channeling. Each [Shock Cart](#shock-cart-destructible-object--hazard) Treatment Pulse (every 5s) advances a hidden timer; **4 pulses (~20s) complete the Treatment** and the [Lobotomized Patient](#lobotomized-patient-conditional-add) rises.
  - Interrupted by stun/knockback, the Orderly's death, or the cart's destruction. Interrupting does **not** reset progress — it just stops the clock.

#### Paddle Shock
- **Type:** Skill
- **Cooldown:** 8s
- **Targeting:** Enemy (adjacent)
- **Rules:**
  - If pulled off the gurney, zaps an adjacent enemy: 9 damage + 1s stun (Will DC 10 negates the stun).

**Drops:** Rubber Gloves (Common, crafting), ECT Paddles (Common weapon, 4-7 lightning, 10% chance 1s stun)

---

### Head Surgeon (holds the key)

A taller mannequin in a blood-flecked surgical gown, a bone saw in one hand and an oversized syringe in the other. A red keycard badge — "AUTHORIZED PERSONNEL" — clipped to its breast pocket.

- **Level:** 10
- **Role:** Elite (Skirmisher)
- **HP:** 150 | **Damage:** 11 | **Accuracy:** 10 | **AR:** 6
- **XP:** 1,800
- **Attributes:** DEX 10, STR 7, WIS 7, INT 4, CON 4, CHA 4
- **Attacks:** 1-2

#### Bone Saw
- **Type:** Skill
- **Cooldown:** None
- **Targeting:** Enemy (melee)
- **Rules:**
  - 13 physical + **Bleed** (2 damage per 2s for 8s).

#### Sedative Syringe
- **Type:** Skill
- **Cooldown:** 12s
- **Targeting:** Enemy (ranged jab)
- **Rules:**
  - 8 damage + **Drowsy** — target's actions slowed 25% for 6s (Will DC 12 halves).
  - On a target already below 25% HP, applies 2s **Sleep** instead (broken by any damage).

#### Authorized Personnel (On Death)
- Drops the **AUTHORIZED PERSONNEL badge** — the keycard that unlocks the exit door. **The party cannot leave the showroom without it.** You must engage the tableau; there is no skipping to the boss.

**Drops:** Authorized Personnel Badge (key item — opens [Room 4](rooms.md#room-4-back-storage-maze)), Bone Saw (Uncommon weapon, 6-11 physical, applies Bleed), Sedative Syringe (Uncommon consumable, single-use Drowsy dart)

---

### Lobotomized Patient (Conditional Add)

Only rises if the **Treatment completes** (4 [Shock Cart](#shock-cart-destructible-object--hazard) pulses land uninterrupted). The mannequin on the gurney sits up, restraints snapping, eyes blank and mismatched. A fresh, mindless berserker — the cost of ignoring the doctors.

- **Level:** 10
- **Role:** Elite (Brute)
- **HP:** 150 | **Damage:** 11 | **Accuracy:** 10 | **AR:** 6
- **XP:** 1,800
- **Attributes:** STR 10, CON 10, DEX 7, INT 4, WIS 4, CHA 4
- **Attacks:** 1-2

#### Mindless (Passive)
- Immune to Fear, Charm, and Taunt. Attacks the nearest living thing — friend or foe. Cannot be reasoned with or controlled.

#### Flailing Strikes
- **Type:** Skill
- **Targeting:** Enemy (nearest)
- **Rules:**
  - Two wild melee swings, 11 each, at -2 of its own accuracy (it isn't aiming).

**This add is entirely preventable.** Its presence is the punishment for tunnel-visioning the Straitjacket or the Guards while the Treatment ran.

**Drops:** Hospital Gown Scraps (Common, crafting)

---

### Asylum Guard (Door Sentinel) ×2

Mannequins in rent-a-cop uniforms flanking the "AUTHORIZED PERSONNEL ONLY" door. They do not roam. They do not chase. They guard.

- **Level:** 10
- **Role:** Elite (Soldier)
- **HP:** 150 | **Damage:** 11 | **Accuracy:** 10 | **AR:** 8 (riot gear)
- **XP:** 1,800
- **Attributes:** STR 10, CON 10, DEX 7, WIS 7, INT 4, CHA 4
- **Attacks:** 1

#### Post Discipline (Passive)
- A Guard will not leave its post. It ignores the party until (a) someone comes **within reach of the door** without the badge, or (b) it is attacked. Then it fights to the death in place.
- **They guard the door, not the room.** Crossing the middle hall at a distance provokes nothing — the Guards *track* whoever passes, heads turning to follow, and do not engage. See [Room 3 — the gate](rooms.md#encounter-asylum-set).

#### Authorized Personnel (Passive)
- **A Guard honors the badge.** Present the [AUTHORIZED PERSONNEL badge](#head-surgeon-holds-the-key) and both Guards straighten, step aside, and let the party through the door unharmed. They do not check the photo. They do not ask where it came from. They do not care that the man it belonged to is dead on the linoleum behind you.
- They are **not defeated** by this — they return to post and remain live Elites at the party's back.
- **Design note:** the Guards are policy, not monsters. Killing them is possible but pointless, and a static two-Elite cleanup after the tableau collapse is the flattest available ending to the room — so the badge is the intended solution. The horror is that murdering a man and taking his ID card makes it *fine*; the beat rhymes forward into the Store Manager's *"Let's discuss your performance."* The gate still can't be skipped, because the badge only drops from the [Head Surgeon](#head-surgeon-holds-the-key). Leaving them alive also keeps [Clint's XP curve on plan](../../../system/xp.md#worked-example-clint-dings-l4) — the tableau alone lands him at **~L5** as designed, while the two Guards' 3,600 would overshoot him into L6 before the boss.

#### Interpose
- **Type:** Skill (Reaction)
- **Rules:**
  - If a character tries to open or force the door **without the badge** while a Guard lives, the nearest Guard intercepts with a shove: 11 damage + knockback.
  - **The door cannot be opened past a living Guard empty-handed.** The badge is the only thing that satisfies them — and it is the only thing that has to.

#### Baton Bash
- **Type:** Skill
- **Targeting:** Enemy (melee)
- **Rules:**
  - 11 physical + 1s stagger.

**The gate:** to leave the showroom, the party needs the Head Surgeon's badge — **that's all.** Present it and the Guards stand aside; they stay alive, at post, behind the party. Beyond the door: [Room 4](rooms.md#room-4-back-storage-maze) ("EMPLOYEES ONLY").

**Drops:** Riot Baton (Common weapon, 5-8 physical, 1s stagger), Guard Cap (Common cosmetic)

---

### Straitjacket Mannequin

A mannequin in a torn straitjacket, arms wrapped tight. Thrashes against its restraints. When it breaks free, things get worse. A yellowed hospital discharge tag is safety-pinned to the canvas — **"TREATMENT: COMPLETE"** — the tell that this was a Patient once. It graduated. It's what the [strapped-down Patient](#lobotomized-patient-conditional-add) across the room becomes if the [Treatment](#asylum-orderly) runs.

- **Level:** 10
- **Role:** Elite (Brute)
- **HP:** 150 | **Damage:** 11 | **Accuracy:** 10 | **AR:** 6
- **XP:** 1,800
- **Attributes:** STR 10, CON 10, DEX 7, INT 4, WIS 4, CHA 4
- **Attacks:** 1 (2 when Berserked)

#### Can't Be Held (Passive)
- A straitjacket will not be restrained. Slows, roots, stuns, and confusion land at **half duration**, and each second it's under any control effect there's a **50% chance it thrashes free early.**
- The party's instinct — *"it's already wrapped up, just park it"* — fails here. Soft CC (Rebekah's [Dissonant Chord](../../../classes/temporal-bard.md) slow, Vanessa's [Minor Illusion](../../../classes/quantum-sorceress.md) lure) barely sticks; it rips loose and **charges whoever tried to control it.** This is the beat that forces the tank to abandon his target and peel.
- Escalates to **full immunity** once it Berserks (below 50% HP). Before Berserk, control *slips*; after, it doesn't land at all.

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

**Narrative:** Displayed on the counter as the **"GRAND PRIZE — 500 TICKETS,"** draped in plastic gold chains. The [Clown](#clown-mannequin) keeps bonking it still; when the Clown looks away, the lid twitches and a wet eye-shine shows between the teeth. [Selene](../../../characters/party/selene.md) clocks it in a heartbeat: "I'd never get fooled by a stupid mimic." (Remember that — setup for Room 5.)

**Clint's [System Identify](#what-system-identify-gives-clint) plays along with the disguise.** The read opens benign — *a treasure chest* — and won't quite hold still:

```text
Object — Identified
"A treasure chest."
Level: 10 · Type: Container · Threat: None
HP: 60 | AR: 8
Note: Gold-chained "GRAND PRIZE." Contents: 500 tickets.
      The teeth along the lid are decorative.
      The teeth along the lid are decorat—
      The teeth are not decorative.
```

The scan never says *mimic* — it snags on the teeth and leaves Clint to finish the sentence, the same way the System [withheld the gnomes' weakness](../../../system/ui-popups.md#5-system-identify--entity). [Selene](../../../characters/party/selene.md) doesn't need it; she made the call in a heartbeat with her own eyes. *(Design note: the read surfaces **nothing of what it can hold** — the [bag-of-holding](../../../items/accessories/mimic-pet.md) is the pet's secret, never shown by Identify, then or later.)*

> *Strider, to Clint alone:* "It's a mimic. Obviously. Even you spotted that one."

**The close call:** to prove the point, Selene **pets it like a housecat** — a couple of easy strokes along the lid while it strains not to bite. The [Clown](#clown-mannequin) tenses hard (see Booth Guardian threshold tell) but doesn't attack, because petting isn't theft. It only animates on an actual take/strike, at which point the Clown joins the fight.

**Two outcomes:**
- **Bought (500 tickets):** the Clown honors it, the mimic goes tame, and it binds to the buyer — [Selene's](../../../characters/party/selene.md) [Prize Mimic pet](../../../items/accessories/mimic-pet.md). Playing by the rules tames it.
- **Stolen (no tickets):** it wakes hostile and the [Clown](#clown-mannequin) piles in. Standard fight, nothing surprising — the party saw it coming.

If Selene ends the carnival with a tame mimic in tow, her **Room 5 couch dive lands harder:** her mimic-guard is now completely down ("we have one as a *pet*"), so the one she doesn't check is the one that gets her. Frame the [Mimic Couch](rooms.md#the-mimic-couch) to resemble the pet.

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
