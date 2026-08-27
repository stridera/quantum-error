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
| **Core mechanic:** | Manager is immune while Puppets live. Kill both Puppets within **20s** of each other or he restrings the first. While the Shield is up no interrupt exists — the only counter is DPS. Once it's down, *keep hitting him* — damage is what stops him restringing. |

---

## Store Manager "Dan"

A mannequin in a wrinkled dress shirt, loose tie, and slacks. Holds a clipboard, a pen tucked under the clip. Name badge reads "STORE MANAGER." Moves with the tired authority of middle management. He holds the far edge of the spotlight and does not fight his own fights while he has staff for that — see Action Item.

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
  - The Manager consults his clipboard, clicks his pen, points at a target, and speaks: *"Let's talk about your numbers."*
  - Target suffers **Performance Anxiety**: -3 accuracy, -3 damage dealt, -25% healing output for 8s.
  - Will save (DC 14) to halve duration (4s).
  - Dispellable only by [Rebekah's Da Capo](../../../classes/temporal-bard.md#da-capo) (rewinds the target to before the Review landed) or by breaking line-of-sight to the Manager. **Not** by [Cleanse](../../../magic/spells/cleanse.md) — that's laundry, it does not touch statuses — and not by [Wade's](../../../characters/party/wade.md) Lesser Restoration, which is physical-only. The Manager attacks through the one channel the healer can't cure.
  - **Single target, and always the healer** once he's shown his hand: the Manager attacks the sustain — dismantle the support and the org chart collapses. (His opening cast may land elsewhere while he watches the party work — Ch 26's first Review hits Clint — but from Wade's first heal onward, every Review is for Wade.)

```text
Performance Anxiety (Mental Debuff)
It's time for your performance review, and you already know it's not going to be good. No amount of extra flair will save you now.

Source: Store Manager "Dan"
Duration: 8s (Will save DC 14: 4s)
Stacks: No (refreshes)
Dispellable: Yes (Da Capo / LOS break)
Effects:
- -3 Accuracy
- -3 Damage dealt
- -25% Healing output
```

### Ability: Emergency Meeting

- **Type:** Spell (AoE Fear)
- **Cost:** None (innate)
- **Cooldown:** 30s
- **Duration:** 4s
- **Targeting:** Room (AoE — All Enemies)
- **Tags:** Fear, Mental, AoE
- **Rules:**
  - The Manager smacks the clipboard against his palm — once, flat, like a gunshot — and shouts: *"EMERGENCY MEETING. NOW."*
  - All enemies in the room make a Will save (DC 12).
  - Failure: 4s **Fear** — cannot approach the Manager, -5 accuracy.
  - Success: 1s **Shaken** — -2 accuracy only.
  - The fear is corporate dread made manifest. The party feels the existential terror of being called into a meeting they didn't prepare for.
  - Used when both Puppets are down or when the party is pushing too aggressively.

### Ability: Action Item

- **Type:** Skill (Ranged)
- **Cost:** None
- **Cooldown:** 10s
- **Damage:** 12 physical (ranged)
- **Targeting:** Enemy
- **Rules:**
  - The Manager finishes a note, clicks his pen, and **hurls the clipboard** spinning across the room. It cracks the target and returns to his hand — middle management never actually lets go of the clipboard.
  - His only damage while the Puppets live: periodic chip pressure from across the room, thrown with the air of a man delegating.
  - Prefers whoever Performance Review is currently on — kick them while they're down; it's efficient.
  - Unavailable while channeling Restring Puppet (the clipboard is tucked under his arm; both hands are on the strings).

### Ability: Pink Slip

- **Type:** Skill (Tank Buster) — Phase 3 only
- **Cost:** None
- **Cooldown:** 15s (10s during Black Friday)
- **Damage:** 150 physical — **unblockable, unparryable**
- **Targeting:** Enemy (highest threat)
- **Rules:**
  - The Manager unclips a **pink sheet** from the clipboard and holds it overhead — a **2-second telegraph** — then serves it: *"You're being let go."* Termination paperwork **pierces block and parry** — a shield does not stop it — but it **respects active defensive cooldowns**: [Exception Handling](../../../classes/paladin-of-the-system.md#exception-handling) (Paladin L8) is the intended counter.
  - Always aimed at the **highest-threat target** — the tank, doing his job. Roughly 15% of [Clint's](../../../characters/party/clint.md) hacked HP pool per slip: **six unhealed Pink Slips end him.** That is the clock [Wade](../../../characters/party/wade.md) is healing against.
  - **The bill for the prize booth:** against the slip itself, what Clint lacks is **three levels** — Exception Handling is L8 and he's ~L5. Against everything else in the phase, what he lacks is the **shield** he spent on [Qubit](../../../items/accessories/mimic-pet.md) — Shield Mastery and Shield Bash sit idle on his sheet. Either way he pays in HP: both surrendered prize-booth items come due in this phase, Qubit repays Wade's ribbon, and **nobody repays Clint's shield.** The console-hacked 999 pool *is* his shield.
  - **Fear interlock:** if Clint fails an Emergency Meeting save he *cannot approach* — and the next Pink Slip serves whoever is left on top of the threat table, i.e. someone squishy. Bless and the Cleric Aura's fear resistance are tank-saving tools in this phase, not flavor. Blessed is load-bearing for **threat** too: Clint's Novice hands hover near a coin flip, and the +5% accuracy is part of what keeps his hits — and therefore his threat — above the party's. An unblessed, whiffing, feared tank is how a Pink Slip finds Vanessa.

### Ability: Corporate Restructuring

- **Type:** Spell (Ground Hazard) — Phase 3 only
- **Cost:** None
- **Cooldown:** 12s
- **Damage:** 15/s to anyone standing in a zone
- **Targeting:** Room (floor zones)
- **Rules:**
  - Caution-tape rectangles snap into being on the floor — **"UNDER RENOVATION — PARDON OUR DUST"** — with a **2-second warning** before they go live. Zones linger ~10s.
  - The 15/s is not the point; the *movement* is. Wade heals on the move, Vanessa's long casts get clipped, and the cornered-Manager dance has to route around taped-off floor — while feared players can't path toward him at all.
  - During **Black Friday**, each cast tapes off more floor. The room gets smaller as he gets angrier.

### Ability: Restring Puppet

- **Type:** Spell (Channel)
- **Cost:** None (innate)
- **Cooldown:** See timing rules below
- **Duration:** Channel — 16s
- **Targeting:** Bone pile (fallen Giant Skeleton Puppet)
- **Rules:**
  - When one Puppet falls, the Manager raises a hand. After a **4-second delay** (he "notices"), fresh strings drop out of the ceiling darkness and begin hooking the bone pile — a **16-second channel** that hauls the Puppet upright at full HP.
  - Total window: **20 seconds** (4s delay + 16s channel) to kill the second Puppet before the first is back on its strings.
  - **Not interruptible while a Puppet lives.** The Manager is immune ([Management Shield](#immunity-management-shield)) and the strings descend from beyond reach — stun, silence, and knockback have nothing to land on. The only counter is killing the second Puppet inside the window.
  - The Manager is **fully occupied** while restringing: no Performance Review, no Emergency Meeting, no Action Item. The room goes quiet except for the surviving Puppet — the silence is the tell that the clock is running.
  - With both Puppets down the Management Shield drops — but he **can** still restring. Channeling while vulnerable is a different proposition: **any damage taken breaks the channel.** He only attempts it if the party lets him — disengage in Phase 3 and strings start dropping out of the dark. Don't stop hitting him.
  - If the channel completes, the Puppet returns at full HP in its original position.

---

## Giant Skeleton Puppet

A 12-foot skeleton made of actual bone (not plastic), held upright by visible strings that disappear into the ceiling darkness. Its ribcage glows faintly. Moves in jerky, marionette-like motions — nothing *inside* it is moving it; the strings are.

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

### Ability: Chain of Command

- **Type:** Passive
- **Cost:** None
- **Rules:**
  - Attacks against the Store Manager pass through him harmlessly ([Management Shield](#immunity-management-shield)) — **and** the nearest Puppet retaliates, its strings yanking it around to punish the attacker with a bonus attack (14 damage).
  - Nothing is intercepted; there is nothing to intercept. The punishment is for **breaching protocol** — all complaints go through your direct supervisor.
  - If both Puppets are alive, they alternate retaliation (each can retaliate once every 8s).
  - Net effect: swinging at the immune boss is costly, not just wasteful. Wrong-target discipline, enforced in damage.

### Passive: Bone, Not Dead

- **Type:** Passive
- **Rules:**
  - The Puppets are **constructs — bone marionettes**, not undead. Real bone, but nothing *in* them is animated; the strings do all the moving.
  - **Immune to Turn Undead.** Holy Light doesn't make them flinch; Consecrate does nothing to them.
  - **Divine Sense reads nothing** — no spirit, no corruption. [Wade](../../../characters/party/wade.md) is L6 and has it: twelve feet of skeleton, and his sense says *empty*. That is the tell, and the horror.
  - If Turn Undead is cast anyway, the bones *try* to obey — the Puppet strains against its strings like a dog hitting the end of a leash — then the strings reel it back. No mechanical effect.
  - **Contrast:** the Graveyard's [Risen Skeletons](mobs.md#risen-skeleton) (+50% from Turn Undead, animated by the Scarecrow) taught the party *skeleton = Turn Undead*. These punish the reflex. One kind of skeleton answers to holy magic; the other answers to management.

### Severed Strings (On Death)

When a Puppet dies, its strings snap visibly — the audience sees them sever. The puppet collapses into a pile of bones. The Manager's expression shifts for the first time: irritation, then focus as he begins to restring it.

**Drops:** Puppet String Bracelet (Rare accessory, +2 DEX. Made from the actual control strings.), Ribcage Vest (Rare armor, +6 AR, bone-plated. Looks intimidating.)

---

## Encounter Phases

### Phase 1: Dual Assault

**Duration:** Until the first Puppet dies.

Both Puppets are active. The Manager is immune and uses abilities freely.

**Behavior:**
- The Puppets flank the party — one on each side. They use Bone Sweep to scatter grouped players and Chain of Command to punish anyone who swings at the Manager.
- The Manager stays across the room, behind his Puppets, watching the fight and making notes. He never closes to melee while a Puppet lives — his contribution is **Action Item** on cooldown: periodic clipboard chip damage from the back of the room.
- The Manager uses **Performance Review** on the highest-performing party member every 15s, reducing their output.
- The Manager uses **Emergency Meeting** once at the start (a "welcome" fear) and again whenever the party starts to find their footing.

**Party strategy:**
- [Clint](../../../characters/party/clint.md) tanks one Puppet. The party focuses fire on the other.
- [Wade](../../../characters/party/wade.md) keeps Clint alive. [Rebekah](../../../characters/party/rebekah.md) buffs damage and keeps Performance Anxiety off **Wade** with [Da Capo](../../../classes/temporal-bard.md#da-capo) — the Review is single-target and aimed at the healer, and at the Phase-1 cadence (15s vs her 12s cooldown) she wins the race: *"I'll keep it off you."*
- [Vanessa](../../../characters/party/vanessa.md) and [Selene](../../../characters/party/selene.md) are the primary DPS on the focus target.
- Avoid clustering — Bone Sweep punishes groups.
- Wade: Turn Undead does nothing here ([Bone, Not Dead](#passive-bone-not-dead)). His job is keeping Clint up, not clearing the field.

### Phase 2: Kill Window

**Duration:** 20 seconds (4s delay + 16s channel).

The first Puppet dies. The Manager pauses for 4 seconds (noticing), then begins a 16-second channel to restring it.

**The race:** The party has 20 seconds to kill the second Puppet (360 HP) before the first is back on its strings.

**Behavior:**
- The surviving Puppet goes aggressive — it knows what's happening. Increased attack speed, uses Bone Sweep on cooldown.
- The Manager is fully occupied restringing — no Reviews, no Meetings, no Action Item for the whole window. A clean race: the party versus one angry Puppet and a clock.
- **The channel cannot be interrupted.** Don't try — the Manager is still immune and Chain of Command still bites.

**Party strategy:**
- Everything on the second Puppet. All cooldowns, all burst.
- There is no backup plan. If DPS falls short, the first Puppet comes back and Phase 1 resumes — rinse and repeat until the party finds the burst. Rebekah's Temporal Boost and Vanessa's burst are the levers.
- With the party's boosted stats (999 HP, 20 in all attributes), they have the raw damage to do this — but they need to execute.

**DPS check (approximate):**
- 360 HP in 20 seconds = 18 DPS required from the party.
- With boosted stats and abilities at L3-5, this is achievable but not trivial. It requires focus and no wasted actions.

### Phase 3: Manager Exposed

**Triggered by:** Both Puppets dying.

The Manager loses his immunity. His expression changes — the corporate veneer cracks. He's angry.

**The phase opens in Crunch Mode.** No 25% wait — the moment he's alone, the tie loosens and the pleasantries stop. With the Puppets gone the party's incoming damage should have collapsed; Crunch is what keeps the pressure on from the first second.

**Behavior (Crunch Mode, from the first second):**
- **Performance Review** every 8s (halved — he's panicking).
- **Emergency Meeting** every 15s (halved).
- **Pink Slip** every 15s — the telegraphed, unblockable tank buster. See the ability block; this is the phase's real damage.
- **Corporate Restructuring** every 12s — the floor starts disappearing behind caution tape. Nobody stands still.
- He keeps his distance, backing away with managerial dignity and throwing **Action Item** on cooldown — but at DEX 4 he shuffles, he does not kite. The party closes the gap fast.
- **If the party stops hitting him** — regrouping, retreating to heal, everyone backing off at once — he starts **Restring Puppet**. Any damage breaks it instantly, so it only ever succeeds against a party that has genuinely disengaged. If it completes, the Shield comes back up and Phase 1 resumes with the party's resources already spent.
- **Clipboard Smack** (cornered): melee attack with the clipboard, 18 physical damage. He swings it flat-side-on, like a paddle. Surprisingly heavy for masonite.
- His melee is trivial; his danger is the debuffs, the paperwork, and the floor plan.
- At 25% HP (225), he enters **Black Friday** — he says it quietly, almost fondly: *"Everything must go."* Review/Meeting go back-to-back (5s/10s), **Pink Slip drops to every 10s**, all his damage gains **+25%**, and Restructuring tapes off more floor per cast. His Reviews stay glued to Wade, now arriving faster than Da Capo can answer. *(The scripted finale cascade — Bless lapse → slip → failed fear save → off-tank relay — is staged in the prose beats below.)*

**Party strategy:**
- Corner him — DEX 4 means he can't stay away from Clint for long. Clint tanks the clipboard swings; Wade heals through the damage.
- **Never fully disengage.** Someone must keep landing hits at all times — one Dust Note is enough to break a restring. Heal on the move; don't reset.
- **Wade's other clock — Bless (60s).** Blessed expires mid-phase, and re-casting costs 20 mana and a cast that isn't a heal. That's the healer's dilemma stated in actions: **re-Bless Clint, or top him up.** Skip the Bless and Clint starts whiffing (threat slips) and failing Meeting saves (fear) — either way the next Pink Slip hunts a squishy. Cast it and Clint sinks deeper into the red on half-strength heals. There is no right answer, only timing.
- **Why not the nova?** The door is closed twice. **Mana:** Broken makes every heal deliver ~a third less per point of mana, and Wade has been solo-healing since Phase 1 — by Black Friday the pool cannot fund a max-Empowered cast *and* the stream of small heals that must follow it. A nova that leaves the tank uncovered for the next two Pink Slips is a wipe with extra steps. **Memory:** the last time he poured everything into a desperate heal ([Ch 17, the bear](../../../story/chapter-summaries.md)), it dragged the twins up with it — and since the Mirror Room the seal is off; he knows exactly what's behind that door. A healer who cracks open mid-fight heals no one. He keeps casting small. That's not fear — it's triage.
- Rebekah's whole fight is the Da Capo race — the Review is single-target and always for Wade, so her *target* never changes; the **coverage** does. Phase 1 (15s vs 12s): she keeps him clean. Crunch (8s): gaps open. Black Friday (5s): the race is unwinnable — Wade is debuffed more often than not. That's the design, not a failure.
- Vanessa and Selene burn the Manager down. 900 HP with full party DPS goes quickly.
- This is **not** a victory lap. The phase is tuned so a Broken Wade cannot quite hold it (see the tuning note below) — the party isn't racing the Manager's 900 HP against their patience, they're racing it against Clint's pool.

**The clutch — Blue Ribbon returns** *(planted in the [carnival](rooms.md#encounter-carnival-set)):* the Review is single-target and **always for Wade** — the Manager attacks the sustain. Phase 1, Rebekah wins the race (*"I'll keep it off you"*). **Crunch breaks it** — *"His cooldown changed. I can't dispel it fast enough"* — and late Crunch is where [Wade](../../../characters/party/wade.md) cracks: still **Broken** (−25% healing) with Performance Anxiety stacking *another* −25% in every gap her cooldown can't cover, his output cratering exactly when the party can least afford it. (The number itself stopped being a surprise in Phase 1 — the first Review to land on him finished [the math he started in the break room](rooms.md#wade-does-the-math); now he lives it in gaps.) **That** is when the [Prize Mimic](../../../items/accessories/mimic-pet.md) pays off: [Selene's](../../../characters/party/selene.md) pet hacks up the **[First-Place Blue Ribbon](rooms.md#encounter-carnival-set)** (+15% healing) it swallowed as a gag back in the carnival — the item Wade *surrendered* for the puppy — handing him the margin that holds the line **through the rest of Crunch and down to 225.** Joy-over-optimization, repaid: the thing they gave up power for gives the power back when it counts. *(Author note: keep it the difference-maker, not a full fix — Wade still nets −10% with the ribbon on, and **Black Friday is deliberately tuned past even ribbon-sustain on a single target**: the ribbon gets them *to* the final phase; the improvised off-tank relay (prose beats) gets them *through* it. And the mimic should surface it inconveniently — sulking, or spitting it at the wrong person first — never heroically.)*

> **Tuning note — the ribbon margin (author-facing).** Phase-3 incoming damage (Pink Slips + Smack/Action Item chip + Restructuring ticks) is calibrated so that holding Clint's pool requires **≈85% of Wade's unimpaired healing output:**
>
> | Wade's state | Output | Result |
> |---|---|---|
> | Broken | 75% | **Slowly losing** — Clint's 999 buys roughly the length of the phase, no more |
> | Broken + Review | 50% | **Free-fall** — the visible crater |
> | Broken + Ribbon | 90% | **Barely winning** — the thin margin is the design: small enough to feel like grace, real enough to close |
> | Broken + Ribbon + Review | 65% | **Under water during Review windows** — Da Capo triage and LOS breaks stay relevant after the ribbon |
>
> If any number in this phase changes (Pink Slip damage, cadences, the Black Friday +25%), re-check it against this table first. **The ribbon must stay the crossover** — never a reset, never irrelevant.
>
> The table also assumes **no Empowered nova** — excluded by design on both mana and memory grounds (see *Why not the nova?* in the strategy). If a future pass reintroduces big burst healing, this entire margin collapses.
>
> **Black Friday intentionally exceeds the table:** at +25% with 10s slips, even 90% ribbon-sustain cannot hold a single tank. The designed answers: a normal party rotates defensive cooldowns (Exception Handling, Guardian Intercept); *this* party rotates **pools** — the off-tank relay in the prose beats. The ribbon buys the ticket to Black Friday; the relay survives it.

---

## Defeat

The Manager staggers. His tie loosens. He drops the clipboard; it hits the floor in a spray of loose performance reviews — every sheet blank except a single printed line: *does not meet expectations.*

*"This... this isn't in the handbook..."*

He collapses into a pile of plastic and cheap fabric. The spotlight flickers off, then on — illuminating a drop pile where he stood.

The dungeon's fog begins to clear. The strobes stop. The doors unlock.

---

## Loot — Boss Drops

The Manager's own pile is deliberately thin: **the boss drops Dan things.** The Manager is a caricature of [Dan](../../../characters/villains/dan.md), and what falls out of him reads as evidence of that — a foreshadow token the party doesn't yet know how to read. The real payout comes from clearing the dungeon (below).

### Dan's Performance Badge
- **Type:** Accessory
- **Quality:** Epic
- **Effect:** +2 to all Will saves. +5% XP gained — **combat XP only**: fixed System awards (quest and completion grants) ignore percentage modifiers ([xp.md](../../../system/xp.md#quests)). It also drops *after* the one fight it would have boosted. Middle management's reward, arriving exactly too late to matter.
- **Appearance:** A plastic name badge: "DAN — EMPLOYEE OF ETERNITY."
- **Flavor:** Wearing it feels like being judged. Somehow, that makes you tougher.

### Manager's Clipboard
- **Type:** Weapon (one-handed, blunt)
- **Quality:** Rare *(demoted from Epic — a curiosity, not a build piece)*
- **Damage:** 10-15 physical
- **Special:** On hit, 10% chance to apply **Performance Anxiety** (3s, reduced version: -2 acc, -2 dmg).
- **Appearance:** A battered masonite clipboard with a chrome clip. Far heavier than it has any right to be. The attached pen is out of ink, forever.

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

## Completion Rewards — "Gifts with Purchase"

As the exit doors finally unlock, the System prints a **receipt** — *"Thank you for shopping! Please enjoy these gifts with purchase"* — and **five gift-wrapped boxes** slide out of the dark, one addressed to each party member. Each item is **soulbound to its recipient on unwrapping.**

**Why completion, not the boss:** it rhymes with the [prize booth](rooms.md#encounter-carnival-set). Every member *surrendered* the personal item they wanted (Clint's shield, Vanessa's Monocle, Wade's ribbon) to buy [Qubit](../../../items/accessories/mimic-pet.md) — and the dungeon hands each of them a personal item anyway. Generosity repaid for joy-over-optimization.

**Dungeon-Tier Cap (shared rule):** every completion item channels at most a **Level-10-equivalent effect**, no matter what is fed into it. Each item expresses the cap its own way (rate, storage, plateau) — the details live in the item files. This keeps the set relevant at L20 without breaking anything.

| Recipient | Item | One line |
|---|---|---|
| [Clint](../../../characters/party/clint.md) | [Lil' Sparkler Glitter Gel Pen](../../../items/accessories/lil-sparkler-gel-pen.md) | Enchanting scribe, writes on anything, L10 rune cap — his Grandmaster layering does the rest. Everything comes out in glitter and crayon doodles. |
| [Selene](../../../characters/party/selene.md) | [Agent's Clip-On Bow Tie](../../../items/accessories/agents-clip-on-bow-tie.md) | Doubles Stealth; non-directional spy score plays while sneaking; 3-day attunement resets if removed. |
| [Rebekah](../../../characters/party/rebekah.md) | [My First Guitar](../../../items/weapons/my-first-guitar.md) | First real instrument — time is the string; +25% song potency; randomly lapses into kid songs mid-buff. |
| [Vanessa](../../../characters/party/vanessa.md) | [Schrödinger's Hat](../../../items/armor/schrodingers-hat.md) | Stores one spell in superposition for instant release (L10 mana cap); sometimes meows. There is no cat. |
| [Wade](../../../characters/party/wade.md) | [Lil' Doc Play Medic Kit](../../../items/accessories/lil-doc-medic-kit.md) | Consent-proof toy stethoscope diagnosis, slow limb-reattaching band-aids, 5 candy heals/day, aura-to-go stickers. |

---

## XP & Graduation

- **The fight pays once per employee.** A restrung Puppet is the **same entity** — killing it again grants no XP (and closes the restring-farming exploit). Pool: Manager 15,000 + 2 × Puppet 6,000 = **27,000**, split risk-weighted per [xp.md](../../../system/xp.md): Clint's tank share is largest, the relay earns Vanessa and Selene genuine shares, and Wade's combat healing under fire pays like DPS.
- **Post-boss: the whole party lands L8.** Clint enters at ~L5 and **triple-dings mid-fight** — the boosted underdog catching up exactly as xp.md designs. (Prose gift: level-up popups during Black Friday that nobody has time to read.)
- **Completion award: 8,000 XP per member,** itemized on [the receipt](#completion-rewards--gifts-with-purchase) — *"LOYALTY REWARD."*
- **Exit levels: Wade, Vanessa, Selene, Rebekah — L10. Clint — L9,** short by roughly a hundred XP. His is the only ledger with no pre-Transition kills and no road XP in it — his class wasn't finalized until the god choice — so he alone graduates a level behind, four levels closed down to one fight's worth. He dings L10 in Part 3's first real skirmish. (The Badge's +5% can't close the gap: it drops after the boss's XP is paid, and the completion grant is a fixed award — [modifiers don't apply](../../../system/xp.md#quests).)
- **Rebekah is not behind.** Her Ch 18 "L4" against Selene's L5 was threshold timing on a front-loaded curve, not a real gap; by the boss her cumulative is level with Selene's and Vanessa's.

---

## Prose Beats — From the Double Kill (author-facing)

> Ch 26 ends mid-Crunch on Clint stating the loss condition. These beats cover the remaining fight and the walk-out; the first two are **revision hooks for Ch 26's tail**, the rest belong to the next chapter. The Ch 26 review's "hold Crunch Mode back" recommendation is superseded — canon now follows the prose (Crunch fires at Shield-fall; **Black Friday** is the 25% escalation).

1. **The double kill.** Second Puppet dies inside the 20s window; both string-sets snap. *(Ch 26 revision hook, per review: move "I held my breath" to before the kill, while both Puppets are red and the clock is running.)*
2. **Crunch, immediately — and the floor starts disappearing.** Shield falls, Emergency Meeting fears Clint out of range (on the page already). Debut **Corporate Restructuring**: the first caution-tape zones snap down. Debut **Pink Slip**: pink sheet overhead, 2s, *"You're being let go"* — 150 into Clint. This retro-justifies Ch 26's closing line (going down faster than Wade can heal); ideally seed the first slip at the very end of Ch 26 in revision.
3. **The fear interlock scare.** A Meeting catches Clint mid-return; the next Pink Slip telegraph swings toward someone squishy. The save that matters is passed on **Bless's +2** — Wade's boring maintenance spell quietly saves a life. Nobody comments. *(Do not kill anyone with this; it's a threat beat.)*
4. **The restring tease.** A Restructuring + Meeting overlap forces everyone off the Manager at once — and strings start dropping toward the bone piles. **Rebekah's Dust Note** — the least lethal spell in the game — snaps the channel. The never-disengage rule, dramatized once.
5. **Late Crunch — the race breaks, and Wade grinds.** *"His cooldown changed. I can't dispel it fast enough."* Reviews land in every Da Capo gap; Clint is sinking faster than Wade can heal. The **Bless timer runs out with Clint deep in the red** — first firing of the dilemma: Wade spends the cast on Bless instead of the heal, Clint drops lower than he ever has, and the *next* Pink Slip stays pointed at him **because** of it. The right call, made with his hands shaking. The **nova is on the table exactly once** — he could dump the pool the way he did under the bear — and he sets it down without a word: the mana isn't there, and he knows what came up with it last time. A glance at the mana bar; no speech, no flashback. He *does not* freeze — he grinds.
6. **The ribbon (late Crunch — it gets them *to* Black Friday).** Even with Rebekah dedicated to him, Wade craters in the Da Capo gaps. **That's** when Qubit — **named on-page before this beat** (review note) — retches like a cat with a hairball and spits the Blue Ribbon at the wrong person; it gets relayed to Wade. +15%. Not a reset: the numbers don't get good, they get *possible* (Clint's flat mechanical register is the right voice). The margin holds the line through the rest of Crunch and carries them down to 225 alive. Inconvenient, never heroic.
7. **Black Friday at 225 HP.** He straightens, almost fond: *"Everything must go."* Back-to-back Reviews aimed at the healer, slips every 10s at +25%, tape until the room is a corridor. Even ribbon-sustain cannot hold one target against this — by design (tuning note). The answer is no longer numbers; it's the relay.
8. **The cascade.** The Bless timer comes due a **second** time — and this time the answer flips: Clint's post-slip HP is too low, Wade must spend the cast on the heal, and **Blessed lapses.** The next Pink Slip puts Clint in the **low double digits** — he is certain the next one ends him. Then **Emergency Meeting**: without Blessed the save is a raw roll, and the dice betray him. Feared — backpedaling through caution tape, unable to approach, threat bleeding out — and the Manager turns on **Vanessa.**
9. **The relay.** Vanessa plants herself and waves Clint off — *"Let me tank. For a bit."* Unlike a normal sorceress, she is also a 999-HP monster: the Clipboard Smacks bounce off her pool, but every hit **interrupts her cast-time spells** ([combat.md](../../../system/combat.md#interrupts-and-control)) — her threat stalls, and **Selene passes her on the damage chain**. Play the System meter gag mid-crisis (Selene smug; Vanessa outraged she's losing a fight she can't even swing in) — and threat follows damage, so the Manager pivots to **Selene** next. This is the thesis beat: a normal party survives Black Friday by rotating cooldowns; this one survives it by rotating **pools**. Their cheat was never a button — it's depth. And a rhyme, unremarked: Vanessa triggered the bear trap that put Clint at 7/999; at his second near-death, she's the one who steps between. The guilt arc pays off without a word.
10. **The return, and the kill.** Ribbon-Wade has poured small casts into Clint through the whole relay — half a pool back. Fear long gone, Clint charges the taped corridor, **Commanding Shout**, takes the Manager back — and they squeak it home. Cornered at DEX 4 against the last untaped wall, the Manager unclips **one final pink sheet — and the killing blow lands first**; the sheet flutters down blank. *"This... this isn't in the handbook..."* Collapse into plastic and cheap fabric; the dropped clipboard sprays performance reviews — every page blank except *does not meet expectations.*
11. **The drop pile.** Someone reads the badge aloud: **"DAN — EMPLOYEE OF ETERNITY."** The party names the wrongness — the dungeon knew their Dan — and gets no answer. (Book-1 knowledge line: nobody solves it, nobody mentions the sim.) The Rare clipboard is pure gag loot; someone claims it for the jokes.
12. **The receipt.** Doors unlock, fog clears, strobes die — and the System prints a receipt: *"Thank you for shopping! Please enjoy these gifts with purchase."* Itemized above the signature line: **"LOYALTY REWARD — 8,000 XP"** (see [XP & Graduation](#xp--graduation)). Five wrapped boxes. Suggested unwrap order, comedy → warmth: **Selene** (bow tie — worn instantly, forever), **Rebekah** (guitar — the demo button blurts on first touch), **Vanessa** (hat — it meows; Qubit locks on; a rivalry is born), **Clint** (pen — *"Writes on ANYTHING!"*; he tests it on the plastic machete and a doodle-dog appears; the Grandmaster implications can wait for Celeste), **Wade last** (the medic kit — a playing-doctor-with-your-kids toy; he laughs, and then can't). Candy-pill rationing joke, stethoscope shrugged at (designed). **Do NOT fire an "I WAS BRAVE" sticker on Wade here — that beat is reserved for Part 4.**
13. **The threshold.** They step out and **Broken lifts** — Wade feels it go. He is still the only one without a Mirror Shard; one quiet line, unremarked. Level-ups land per [XP & Graduation](#xp--graduation): the completion award carries Wade, Vanessa, Selene, and Rebekah to **L10** — and Clint to **L9, about a hundred XP short**, the only ledger the System never front-loaded. He'll ding in the first real fight of Part 3. The dungeon graduates the party and hands Part 3 its opening.

---

## Design Notes

The boss encounter tests everything the dungeon taught:
- **Phase 1** requires tanking, healing, and DPS coordination (Rooms 1-3 taught this).
- **Phase 2** is a DPS race with a timer (the bear trap in Room 1 introduced multi-threat urgency).
- **Phase 3** is a burn phase under real pressure: debuffs (taught by Pinhead's Fascination and the Straitjacket's anti-CC), a telegraphed tank buster with no block answer (Clint's surrendered shield, collected on), and a shrinking floor. The healer check is deliberate — see the tuning note.

The 20-second kill window is the skill check — and it's the *only* check: with no interrupt while the Shield is up, there's no clever way around the DPS requirement. Phase 3 runs the mirror rule — the Shield is down, so *damage* is the interrupt, and the party that stops swinging to regroup hands him the fight back. Parties that focus fire and manage their cooldowns clear it cleanly. Parties that panic, split DPS, or waste time attacking the immune Manager struggle.

**How a normal party solves Phase 3** *(the answer key — the encounter is fair at-level):* an L10 tank pops [Exception Handling](../../../classes/paladin-of-the-system.md#exception-handling) on the Pink Slip telegraph (150 → 75, or 37 on the catastrophic catch), uses Guardian Intercept (L9) when the fear interlock retargets a squishy, and the party dodges Restructuring on the 2s warnings. This party is under-leveled with hacked pools instead: Clint has neither the button nor the shield, so the same encounter resolves through raw HP and the ribbon margin. Same fight, two different solutions — that's the design.

The Manager as a Dan-lookalike adds narrative weight — the party is fighting a caricature of someone who betrayed them. Clint may take this personally.
