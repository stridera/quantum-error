---
canon: true
stability: evolving
---

# Spirit Dungeon — Boss: Store Manager "Dan"

The final encounter of the [Spirit Dungeon](../spirit-dungeon.md). A mannequin in a rumpled suit that looks disturbingly like [Dan](../../../characters/villains/dan.md), flanked by two Giant Skeleton Puppets on visible strings.

For room context, see [Room 6](rooms.md#room-6-the-spotlight-room-boss). For mob stat formulas, see [Mob Framework](../../../system/mob-framework.md).

---

## Overview

| Element | Details |
|---------|---------|
| **Boss:** | Store Manager "Dan" (Boss tier, L10) |
| **Adds:** | 2 × Giant Skeleton Puppet (Champion tier, L10) |
| **Party size:** | 5 (full party) |
| **Estimated duration:** | 90-120 seconds |
| **Core mechanic:** | Manager is immune while Puppets live. Kill both Puppets within 16s of each other or he resummons the first. |

---

## Store Manager "Dan"

A mannequin in a wrinkled dress shirt, loose tie, and slacks. Holds a briefcase. Name badge reads "STORE MANAGER." Moves with the tired authority of middle management.

- **Level:** 10
- **Role:** Boss
- **HP:** 900 | **Damage:** 18 | **Accuracy:** 15 (Boss +5) | **AR:** 6
- **XP:** 15,000
- **Attributes:** INT 12, CHA 12, WIS 10, STR 7, CON 7, DEX 4
- **Attacks:** 2-3

### Immunity: Management Shield

While at least one Giant Skeleton Puppet is alive, the Store Manager is **immune to all damage**. Attacks pass through him like he's a hologram. He can still act and use abilities.

This is the core puzzle: the party must kill the Puppets first.

### Ability: Performance Review

- **Type:** Spell (Debuff)
- **Cost:** None (innate)
- **Cooldown:** 15s
- **Duration:** 8s
- **Targeting:** Enemy
- **Tags:** Mental, Debuff
- **Rules:**
  - The Manager points at a target and speaks: *"Let's talk about your numbers."*
  - Target suffers **Performance Anxiety**: -3 accuracy, -3 damage dealt, -25% healing output for 8s.
  - Will save (DC 14) to halve duration (4s).
  - Dispellable by Cleanse, ally encouragement (Rebekah's songs), or breaking line-of-sight to the Manager.
  - He uses this on whoever is performing best — typically the highest DPS or the healer.

```text
┌──────────────────────────────────────────────┐
│ STATUS: Performance Anxiety                  │
├──────────────────────────────────────────────┤
│ Type: Debuff (Mental)                        │
│ Source: Store Manager "Dan"                  │
│ Duration: 8s (Will save DC 14: 4s)           │
│ Stacks: 0 (Does not stack; refreshes)        │
│ Dispel: Yes (Cleanse / Bardic / LOS break)   │
├──────────────────────────────────────────────┤
│ Summary: Your confidence crumbles.           │
├──────────────────────────────────────────────┤
│ Numbers:                                     │
│ - -3 Accuracy                                │
│ - -3 Damage dealt                            │
│ - -25% Healing output                        │
└──────────────────────────────────────────────┘
```

### Ability: Emergency Meeting

- **Type:** Spell (AoE Fear)
- **Cost:** None (innate)
- **Cooldown:** 30s
- **Duration:** 4s
- **Targeting:** Room (AoE — All Enemies)
- **Tags:** Fear, Mental, AoE
- **Rules:**
  - The Manager slams his briefcase on the ground and shouts: *"EMERGENCY MEETING. NOW."*
  - All enemies in the room make a Will save (DC 12).
  - Failure: 4s **Fear** — cannot approach the Manager, -5 accuracy.
  - Success: 1s **Shaken** — -2 accuracy only.
  - The fear is corporate dread made manifest. The party feels the existential terror of being called into a meeting they didn't prepare for.
  - Used when both Puppets are down or when the party is pushing too aggressively.

### Ability: Resummon Puppet

- **Type:** Spell (Summon)
- **Cost:** None (innate)
- **Cooldown:** See timing rules below
- **Duration:** Channel — 12s
- **Targeting:** Corpse (dead Giant Skeleton Puppet)
- **Rules:**
  - When one Puppet dies, the Manager begins a 12-second channel to resummon it at full HP.
  - **4-second delay** before the channel starts (the Manager "notices" the Puppet is down).
  - Total window: 16 seconds (4s delay + 12s channel) to kill the second Puppet before the first returns.
  - Channel is interruptible: stun, silence, or knockback resets the channel.
  - If both Puppets are dead, the Manager cannot resummon (no corpse to raise — both are gone).
  - If the channel completes, the Puppet returns at full HP in its original position.

---

## Giant Skeleton Puppet

A 12-foot skeleton made of actual bone (not plastic), held upright by visible strings that disappear into the ceiling darkness. Its ribcage glows faintly. Moves in jerky, marionette-like motions.

- **Level:** 10
- **Role:** Champion
- **HP:** 360 | **Damage:** 14 | **Accuracy:** 10 | **AR:** 8 (bone)
- **XP:** 6,000
- **Attributes:** STR 11, CON 11, DEX 7, INT 4, WIS 7, CHA 4
- **Attacks:** 2

### Ability: Bone Sweep

- **Type:** Skill (AoE)
- **Cost:** None
- **Cooldown:** 12s
- **Duration:** Instant
- **Targeting:** Room (AoE — Enemies, Cone in front)
- **Rules:**
  - Wide sweeping arm strike: 14 physical damage to all enemies in a frontal cone.
  - Knockback: targets pushed 10 feet away.
  - Telegraphed by the puppet drawing its arm back (2s wind-up, strings tighten visibly).
  - Can hit multiple party members if they're clustered.

### Ability: Guard Protocol

- **Type:** Passive
- **Cost:** None
- **Rules:**
  - If a party member tries to attack the Store Manager while a Puppet is alive, the nearest Puppet intercepts — stepping between the attacker and the Manager and retaliating with a bonus attack (14 damage).
  - This makes it mechanically impossible to ignore the Puppets. They are bodyguards.
  - If both Puppets are alive, they alternate interception (each can intercept once every 8s).

### Severed Strings (On Death)

When a Puppet dies, its strings snap visibly — the audience sees them sever. The puppet collapses into a pile of bones. The Manager's expression shifts for the first time: irritation, then focus as he begins the resummon channel.

**Drops:** Puppet String Bracelet (Rare accessory, +2 DEX. Made from the actual control strings.), Ribcage Vest (Rare armor, +6 AR, bone-plated. Looks intimidating.)

---

## Encounter Phases

### Phase 1: Dual Assault

**Duration:** Until the first Puppet dies.

Both Puppets are active. The Manager is immune and uses abilities freely.

**Behavior:**
- The Puppets flank the party — one on each side. They use Bone Sweep to scatter grouped players and Guard Protocol to protect the Manager.
- The Manager uses **Performance Review** on the highest-performing party member every 15s, reducing their output.
- The Manager uses **Emergency Meeting** once at the start (a "welcome" fear) and again whenever the party starts to find their footing.

**Party strategy:**
- [Clint](../../../characters/party/clint.md) tanks one Puppet. The party focuses fire on the other.
- [Wade](../../../characters/party/wade.md) keeps Clint alive. [Rebekah](../../../characters/party/rebekah.md) buffs damage and dispels Performance Anxiety with her songs.
- [Vanessa](../../../characters/party/vanessa.md) and [Selene](../../../characters/party/selene.md) are the primary DPS on the focus target.
- Avoid clustering — Bone Sweep punishes groups.

### Phase 2: Kill Window

**Duration:** 16 seconds (4s delay + 12s channel).

The first Puppet dies. The Manager pauses for 4 seconds (noticing), then begins a 12-second channel to resummon it.

**The race:** The party has 16 seconds to kill the second Puppet (360 HP) before the first returns.

**Behavior:**
- The surviving Puppet goes aggressive — it knows what's happening. Increased attack speed, uses Bone Sweep on cooldown.
- The Manager is channeling but can still use Emergency Meeting if interrupted (it breaks his channel, but he'd rather delay than lose both Puppets).
- Interrupting the channel buys time but doesn't kill the Puppet.

**Party strategy:**
- Everything on the second Puppet. All cooldowns, all burst.
- Someone must be ready to interrupt the Manager's channel as a backup plan if DPS is tight.
- With the party's boosted stats (999 HP, 20 in all attributes), they have the raw damage to do this — but they need to execute.

**DPS check (approximate):**
- 360 HP in 16 seconds = ~22.5 DPS required from the party.
- With boosted stats and abilities at L3-5, this is achievable but not trivial. It requires focus and no wasted actions.

### Phase 3: Manager Exposed

**Triggered by:** Both Puppets dying.

The Manager loses his immunity. His expression changes — the corporate veneer cracks. He's angry.

**Behavior:**
- **Performance Review** every 10s (reduced cooldown — he's panicking).
- **Emergency Meeting** every 20s (reduced cooldown).
- **Briefcase Slam** (new attack): melee attack with the briefcase, 18 physical damage. He swings it like a weapon. Surprisingly heavy.
- He's a caster-type Boss with 900 HP and no physical threat beyond the briefcase. His danger is in the debuffs, fear, and pressure.
- At 25% HP (225), he enters **Crunch Mode**: all cooldowns halved, casts Performance Review and Emergency Meeting back-to-back.

**Party strategy:**
- Clint tanks the briefcase swings. Wade heals through the damage.
- Rebekah keeps dispelling Performance Anxiety and buffing the group.
- Vanessa and Selene burn the Manager down. 900 HP with full party DPS goes quickly.
- The fight is a victory lap if the Puppets went smoothly. If the party is battered from Phases 1-2, it's a survival check.

---

## Defeat

The Manager staggers. His tie loosens. He drops the briefcase.

*"This... this isn't in the handbook..."*

He collapses into a pile of plastic and cheap fabric. The spotlight flickers off, then on — illuminating a drop pile where he stood.

The dungeon's fog begins to clear. The strobes stop. The doors unlock.

---

## Loot

### Manager's Briefcase
- **Type:** Weapon (one-handed, blunt)
- **Quality:** Epic
- **Damage:** 10-15 physical
- **Special:** On hit, 10% chance to apply **Performance Anxiety** (3s, reduced version: -2 acc, -2 dmg).
- **Appearance:** A battered leather briefcase. Heavy. Contains nothing but dread.

### Dan's Performance Badge
- **Type:** Accessory
- **Quality:** Epic
- **Effect:** +2 to all Will saves. +5% XP gained.
- **Appearance:** A plastic name badge: "DAN — EMPLOYEE OF ETERNITY."
- **Flavor:** Wearing it feels like being judged. Somehow, that makes you tougher.

### Puppet String Bracelet (from Puppets)
- **Type:** Accessory
- **Quality:** Rare
- **Effect:** +2 DEX
- **Appearance:** Thin, nearly invisible strings woven into a bracelet. They move on their own sometimes.

### Ribcage Vest (from Puppets)
- **Type:** Armor (chest)
- **Quality:** Rare
- **AR:** +6
- **Appearance:** A vest of interlocking bone plates. Looks like you're wearing a skeleton's ribcage. Because you are.

---

## Design Notes

The boss encounter tests everything the dungeon taught:
- **Phase 1** requires tanking, healing, and DPS coordination (Rooms 1-3 taught this).
- **Phase 2** is a DPS race with a timer (the bear trap in Room 1 introduced multi-threat urgency).
- **Phase 3** is a "burn phase" where debuffs are the threat (Pinhead's Fascination and the Straitjacket's anti-CC taught the party about status effects).

The 16-second kill window is the skill check. Parties that focus fire and manage their cooldowns clear it cleanly. Parties that panic, split DPS, or waste time attacking the immune Manager struggle.

The Manager as a Dan-lookalike adds narrative weight — the party is fighting a caricature of someone who betrayed them. Clint may take this personally.
