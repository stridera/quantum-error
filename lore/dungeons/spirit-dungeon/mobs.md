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
  - No special mechanics. Straightforward DPS.

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

## Room 2: Changing Rooms

### Echo Double

A mirror-spawned copy of a party member. Same build, same face, same gear — but its movements are slightly off, like a reflection that doesn't quite sync.

- **Level:** 10
- **Role:** Normal (mirrors original)
- **HP:** 60 | **Damage:** 9 | **Accuracy:** 10 | **AR:** 6
- **XP:** 600
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
  - If the original leaves the room, the Echo Double fades over 6s.
  - Spawns when a character stares into a mirror for more than 3s. One Echo per mirror, one mirror per character.

**Narrative:** [Selene's](../../../characters/party/selene.md) Echo is the key moment — she sees her true [Nekara](../../../races/nekara.md) form reflected back for the first time. The emotional beat turns to combat when it steps out.

**Drops:** None (dissolves into glass shards on death)

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
