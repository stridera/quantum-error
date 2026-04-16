---
canon: true
stability: evolving
---

# Spirit Dungeon — Rooms

Room-by-room walkthrough for the [Spirit Dungeon](../spirit-dungeon.md). Each room includes physical description, encounters, environmental effects, traps, and story beats.

For mob stat blocks, see [mobs.md](mobs.md). For the boss encounter, see [boss.md](boss.md).

---

## Exterior

From the outside, it looks like any other Spirit Halloween — a temporary storefront jutting from a strip mall, orange and black signage, plastic skeletons flanking the entrance. The front center has a small entrance vestibule protruding from the building.

Post-Transition, the store is alive. The system recognizes it as a Level 10 dungeon. The party doesn't know this yet.

---

## Vestibule (Safe Zone)

A small glass-walled entrance chamber, roughly 10 × 10 feet. Automatic sliding doors on the outside, heavy double doors leading into the store. Shopping carts stacked to one side. A "WELCOME — ENTER IF YOU DARE" banner hangs overhead.

**Rules:**
- **Safe Zone.** No mobs spawn or enter here. Resting regen rate applies.
- Once the party enters, the outer doors lock. They cannot leave until the dungeon is cleared.
- The inner double doors can be opened and closed freely. When closed, the vestibule is sealed from the dungeon.
- **Respawn behavior:** If the party retreats to the vestibule and closes the inner doors, the entry pair mannequins in Room 1 respawn with different costumes. First time: Jason + Freddy masks. Second time: Pinhead + Scream masks.

---

## Room 1: The Flicker Hall

*The main corridor — the party's introduction to dungeon combat.*

### Description

The inner doors open onto a long corridor built from mobile retail partitions — the kind stores use to create aisles. The partitions are immovable despite looking temporary; even applying force won't shift them. Looking over the top reveals nothing but dark fog.

The corridor is longer than it should be. From outside, the store is maybe 80 feet deep. This hallway stretches well beyond that. The ceiling is lost in darkness above the fluorescent strip lights, which strobe at irregular intervals.

Fog drifts at ankle height. Costume racks line the walls between the partitions. Somewhere deeper in, a music box plays a few notes, then stops.

### Environmental Effects

#### Strobe Flicker
The fluorescent lights cut out every ~10 seconds for 2 seconds of near-darkness.
- During strobe: **-3 accuracy** for all entities in the room (mobs included).
- Mobs are slightly better adapted (plastic eyes don't need to adjust).
- Creates windows where movement is harder to track — adds tension to combat.

#### Whisper Lure
Faint whispers drift from deeper in the corridor — indistinct phrases, fragments that almost sound like your name.
- Out of combat: Will check (DC 8) or suffer 1s **Distracted** (attention pulled toward the sound).
- In combat: suppressed (adrenaline overrides). No mechanical effect.
- Narrative flavor. Establishes the dungeon as psychologically oppressive.

### Encounter 1: Entry Pair (Jason + Freddy)

**Triggered by:** Opening the inner doors for the first time.

Two mannequins stand just inside the vestibule doors, positioned like they were waiting. [Jason Mask](mobs.md#jason-mask-mannequin) on the left (hockey mask, machete), [Freddy Mask](mobs.md#freddy-mask-mannequin) on the right (fedora, claw glove).

They animate the moment the party enters.

**Behavior:**
- Jason opens with Lunge on the nearest target (likely [Clint](../../../characters/party/clint.md), who's in front).
- Freddy tries to circle behind for Flank Strike bonus damage.
- Simple melee. No special mechanics. The party's first real fight.

**Story beat:** [Vanessa](../../../characters/party/vanessa.md) defaults to her high-damage spell (fireball) and can't exclude friendlies. Clint's clothes burn off. Teaches AoE friendly fire the hard way. The mannequins are destroyed, but Clint is standing in burned rags.

**Aftermath:** Clint wraps himself in a towel. The party retreats to the vestibule to regroup.

### Encounter 2: Respawn Pair (Pinhead + Scream)

**Triggered by:** Re-entering from the vestibule after retreating.

The entry mannequins have respawned with new costumes. [Pinhead Mask](mobs.md#pinhead-mask-mannequin) (pin-studded mask, standing still with an unsettling calm) and [Scream Mask](mobs.md#scream-mask-mannequin) (stretched white mask, prop knife).

**Behavior:**
- Pinhead opens with Fascination on the most visible target (Clint, the tank).
- Scream Mask exploits the charm with Panic Cut (+50% damage to CC'd targets).
- Pinhead is an Elite — 150 HP, takes real effort to bring down.

**Story beat:** The party's first CC encounter. Clint is Fascinated — his attention locks onto the Pinhead, and he can't focus on the Scream Mask attacking him. The party must learn to break the effect (ally shove, breaking line-of-sight, or hard damage).

Clint fights this encounter in a towel. After winning, he loots a [Scream Robe](mobs.md#scream-mask-mannequin) — a dark hooded robe that's better suited for [Selene](../../../characters/party/selene.md), but he needs *something*.

**Lesson:** Crowd control exists. Mental effects are real. Allies need to help each other, not just do damage.

### Encounter 3: The Bear Trap

**Location:** Midway down the corridor, past the entry area. The aisle widens slightly around a display of camping/outdoor props.

**The trap:** A giant bear trap sits on the floor among the camping props. Oversized, theatrical — looks like a decoration. A faint chain runs from it up into the ceiling darkness. Scuff marks on the ceiling tiles above. A pressure plate in front of it is slightly too clean.

**Trigger:** Stepping on the pressure plate (or interacting with the trap without disarming it).

**Disarm:** [Selene](../../../characters/party/selene.md) can attempt a trap disarm (Moderate difficulty for L10). If the party doesn't think to check, Clint's Luck (4) makes him the likely trigger.

**On trigger:**
1. The jaws don't snap shut — instead, a full-sized bear drops from the ceiling.
2. **Ceiling Impact:** 45 physical damage (ignores AR) to the triggering character + 3s prone.
3. The [Falling Bear](mobs.md#falling-bear) immediately attacks the prone target with Maul (16 damage, or 22 vs prone).
4. After 1 round, the bear uses **Roar** — all enemies in room make Will check (DC 12) or suffer 3s Fear.
5. The roar summons the roaming pack from down the hall. They arrive 10 seconds later.

### Encounter 4: The Roaming Pack

**Triggered by:** The bear's Roar.

Three mannequins in "sexy" costumes come running (as much as mannequins run) from deeper in the corridor: [Sexy Nurse](mobs.md#sexy-nurse-mannequin), [Sexy Witch](mobs.md#sexy-witch-mannequin), and [Sexy Pirate](mobs.md#sexy-pirate-mannequin).

**Behavior:**
- Nurse targets whoever is lowest HP (Injection for poison DoT).
- Witch hangs back and Hexes the highest-threat target (-3 acc, -2 dmg).
- Pirate charges the nearest enemy with Cutlass Slash.
- Combined with the bear, this is a 4-mob fight — the most the party has faced at once.

**Story beat:** The party is dealing with the bear when three more threats arrive. Multi-target management. [Wade](../../../characters/party/wade.md) is healing, [Rebekah](../../../characters/party/rebekah.md) may need to use crowd control songs. The party is learning to fight together.

**Loot highlight:** The Sexy Nurse drops a **Nurse's Cap** — a tiny white cap with a red cross that gives +5% healing output. Wade can't justify ignoring the stats. He puts it on. It's too small, perched on top of his head. The party says nothing. Then everyone says something.

**Lesson:** Multi-threat management. Prioritize targets. Healers heal, tanks tank, DPS focuses fire.

---

## Room 2: Changing Rooms (Optional)

*A side area accessible from the end of the Flicker Hall. The party can skip this, but there's reason to go in.*

### Description

A doorway to the right at the end of the Flicker Hall opens into a narrow corridor — a costume aisle. Packaged costumes hang on racks along both walls, organized by theme (Superheroes, Classic Monsters, Occupations, "Sexy" Everything). The lighting shifts from strobes to warm incandescent. The fog thins. It feels almost safe.

The aisle runs about twenty feet before opening into a larger chamber: a hexagonal room with polished floors and steady lighting. Five of the six walls are floor-to-ceiling mirrors, each mounted in a heavy frame. The sixth wall is the entrance from the costume aisle.

The mirrors are clean. Too clean for a dungeon. They reflect everything perfectly — every detail, every scar, every piece of gear. The room is still. The only movement is yours.

### Environmental Effects

#### Mirror Spawn
Any character who locks eyes with their own reflection for more than 3 seconds triggers an [Echo Double](mobs.md#echo-double--base-mechanic) — a mirror-spawned copy that steps out of the glass and attacks.

- One Echo per mirror, one mirror per character. Five mirrors, five party members.
- The mirror cracks when an Echo spawns but the frame holds.
- On victory, the defeated echo shatters into glass. The shards fly back into the frame and restore the mirror — whole again, as if nothing had happened — leaving a single pulsing crystal [Mirror Shard](mobs.md#mirror-shard-drops) at the base. On failure, the echo walks back into the broken frame and the glass stays cracked.
- Each mirror has a faint glow at its base — the shard is visible before the fight. The reward is known.

#### Mirror Barrier
When an Echo spawns, a translucent [barrier](mobs.md#mirror-barrier) seals the section between that mirror wall and the room center. The original is locked inside with their Echo. Allies watch through the barrier — they can see and hear everything but cannot enter, attack, or cast through it.

One fight at a time. The barrier drops when the Echo is defeated (or when the fighter loses).

**While watching someone else's fight:** The remaining party members stand in the center of a hexagonal room surrounded by mirrors. They're watching their friend fight, and actively avoiding looking at the other four walls. The tension of *don't look don't look don't look* while someone you care about is taking psychic damage three feet away.

### Encounters

The room is quiet until someone looks. All five party members fight their echoes. Four succeed. One doesn't.

#### 1. Selene's Echo — Dustin

[Rebekah](../../../characters/party/rebekah.md) encourages [Selene](../../../characters/party/selene.md) to approach a mirror. Selene glances and turns away by habit — Dustin avoided mirrors. Rebekah tells her to look closer.

Selene sees her [Nekara](../../../races/nekara.md) form for the first time. Cat ears, fair complexion, the body the system gave her — the one that's actually hers. She stares.

Then the reflection shifts. The ears recede. The frame broadens. Dustin stares back.

The [Echo](mobs.md#selenes-echo-dustin) steps out. The barrier drops. The party didn't know this was coming.

The taunts target her identity — her past, her transition, her dead name. Rebekah is at the barrier immediately. She can't get through. She shouts — not a song, not a buff, just her voice. It's enough to clear some of the weight.

The fourth taunt — the dead name — turns Selene from hurt to furious. She stops fighting Dustin and starts fighting the echo. The kill is fast and vicious. She knows every move because they're her moves.

**Shard of Self** drops. The party processes what just happened.

#### 2. Clint's Echo — The Broken Shield

[Clint](../../../characters/party/clint.md) steps up immediately after Selene. That's what a Paladin does.

The [Echo](mobs.md#clints-echo-the-broken-shield) shows him standing over his fallen friends — faces cycling, hands passing through them. The cracked shield. The weight of everyone he couldn't save.

The taunts land but don't paralyze him. Clint is an EMT. He's lived with the knowledge that he can't save everyone. The echo is a better [Paladin](../../../classes/paladin-of-the-system.md) than he is right now (L10 vs his L3) — it smites harder, blocks better. But it can't outlast him. Clint doesn't have a dramatic breakthrough. He just keeps hitting. The protector who knows shields break and shows up anyway.

**Shard of Duty** drops. Clint's fight sets the baseline: the echoes are beatable. The reader relaxes.

#### 3. Vanessa's Echo — The Mana Shock

[Vanessa](../../../characters/party/vanessa.md) watched two fights. She's calculated her approach.

The [Echo](mobs.md#vanessas-echo-the-mana-shock) is 99,999-mana Vanessa — unstable, blinding, a walking [Mana Lucent](../../../classes/quantum-sorceress.md) flare. The taunts aren't lies, which makes them worse. But Vanessa is a physicist. She doesn't panic at dangerous data — she solves it. She wins by being precise — controlled amplification over raw force. [Anchor](../../../classes/quantum-sorceress.md) spells over amplified chaos. The physicist harnesses the instability instead of fearing it.

**Shard of Control** drops. Three for three. The pattern holds.

#### 4. Rebekah's Echo — The Silent One

[Rebekah](../../../characters/party/rebekah.md) encouraged Selene to look in the first mirror. Now it's her turn.

The [Echo](mobs.md#rebekahs-echo-the-silent-one) is the version of herself that stopped trying — mouth moving, no sound. The emotional anchor who fears she's just background music. The echo counters her songs, silences her in melee, reverses her tempo. Rebekah doesn't get angry — she gets sad. Then she starts singing anyway. [Harmonic Memory](../../../classes/temporal-bard.md) lets her layer songs faster than the echo can suppress them. She wins by being the most Rebekah she can possibly be.

[Selene](../../../characters/party/selene.md) is at the barrier for this one. Reciprocity.

**Shard of Purpose** drops. Four for four. One mirror left. Everyone turns to [Wade](../../../characters/party/wade.md).

#### 5. Wade's Echo — The Empty Hands (FAILURE)

Wade is last. He watched everyone succeed. He's the highest-level party member (L6), the steadiest hand, the one who's been holding everyone together. The expectation is total.

He walks to his mirror.

The [Echo](mobs.md#wades-echo-the-empty-hands) shows him his [twins](../../../characters/supporting/the-twins.md) in his arms. Then they slip through. The reflection looks up with hollow eyes. It steps out slowly, hands open and useless.

The taunts come every six seconds, and every one of them carves a piece out of him. Each taunt is 20% of his maximum HP — psychic damage that ignores AR, ignores Ward, ignores everything he's ever built to protect himself.

1. *"Your dreams — the ones you never remember — they were funerals."* — 80% HP.
2. *"You keep healing strangers because you couldn't heal them."* — 60% HP.
3. *"Two small coffins. You picked out the flowers. You just won't let yourself remember."* — 40% HP.
4. *"There's nothing waiting for you back home. Part of you already knows."* — 20% HP.

All four Shaken stacks land. They land because they're true, and because some buried part of Wade recognizes them before his conscious mind can push back. Phase 2 begins. The echo starts using Wound and Self-Mend. Wade has 30 seconds to attack.

He doesn't.

Someone shouts through the barrier — Clint, probably. It clears 2 Shaken stacks. It's not enough. Wade is staring at his own empty hands. The hands that heal everyone except the people who matter most. He's not afraid of the echo. He's afraid it's right, and afraid of *why* it feels right.

The 30 seconds expire. The echo stops attacking. It looks at him almost gently — the only time any echo has looked at its original with anything other than contempt — and delivers the final taunt in Wade's own voice:

> *"They're gone. You know. You've always known."*

Wade's HP drops from 20% to 1. He does not fall. Some small cruel mechanic of the system keeps him standing.

The echo turns and walks back into the broken frame. The glass does not restore — it stays cracked, the only mirror in the room still broken. The shard at the base goes dark. The barrier drops. Wade is on his feet at 1 HP with **[Broken](mobs.md#identity-crisis-phase-1)** (−3 all primary stats, −25% damage/healing/buff effectiveness, persists until the party leaves the Spirit Dungeon) and no loot.

The room goes quiet. Four whole mirrors with pulsing crystal shards at their bases. One cracked mirror with a dark one.

Nobody says anything. What would you say?

### Consequences

Wade is the healer. **Broken** means −25% healing effectiveness going into the [boss fight](mobs.md#room-6-the-spotlight-room). The Spirit Dungeon didn't just hurt Wade — it hurt the whole party through him. The Store Manager encounter is harder because the party's sustain is compromised.

Nobody blames him. That almost makes it worse.

This is the first crack in Wade's foundation. It foreshadows his [Post-Book I decision](../../../characters/party/wade.md) to step away from adventuring entirely. The mirror room is where the reader first sees that the steadiest person in the party might not hold.

### Story Beat: Clint's Outfit

The costume aisle has actual inventory. [Clint](../../../characters/party/clint.md) can finally ditch the Scream Robe and find something appropriate — the system converts costume quality to actual armor stats (Common tier). [Selene](../../../characters/party/selene.md) may also find class-appropriate gear among the racks.

This happens on the way in, before the mirror room. The shopping is the bait. The mirrors are the trap.

### Story Beat: Looking Again

After the echoes are gone and the room is quiet, the four who won can return to their mirrors. The glass is whole again — each defeated echo shattered and restored the frame it walked out of, leaving a pulsing crystal shard at the base. The reflections are clean. And what they show isn't the present. It's a glimpse of who the bearer is becoming. A future self further along the path. Higher level. Better gear. Unafraid.

[Selene](../../../characters/party/selene.md) is the one who goes back first, and the one the party remembers. She walks to her mirror alone while the others look elsewhere. The glass shows her older, sharper, standing in a full set of Epic-quality armor — not leather scraps, not the starter kit the system handed her. A [Nekara](../../../races/nekara.md) [Veilstepper](../../../classes/veilstepper-rogue.md) who has been doing this for a long time and is very good at it. The reflection does not shift. It does not become Dustin. It is just her, further along.

She stares. The reflection stares back. Then she says something under her breath — *try it again* — and turns away. The mirror stays lit.

[Clint](../../../characters/party/clint.md), [Vanessa](../../../characters/party/vanessa.md), and [Rebekah](../../../characters/party/rebekah.md) each get their own quiet moment with their own mirrors. The details are private to each of them. [Wade](../../../characters/party/wade.md) does not look. No one asks him to.

This is a purely narrative beat — no mechanical effect. The [Mirror Shards](../../../items/accessories/mirror-shards.md) do the mechanical work; the mirrors do the emotional work. Use this scene in prose when the story wants to remind the reader what the party is becoming rather than what the dungeon cost them.

### Lesson

Identity. The Spirit Dungeon tests who you are, not just what you can do. The Mirror Shards are earned through self-confrontation — but not every wound is ready to be faced. Level doesn't protect you from this. Being the strongest, the steadiest, the most needed — none of it matters if the mirror finds the thing you can't look at yet.

---

## Room 3: Seasonal Showroom

*The main floor — a large open area with three themed horror display sets. The party's first true test of coordination and environmental awareness.*

### Description

The corridor opens into a cavernous space — the main retail floor. The ceiling is higher here (or appears to be; the dark fog still obscures it). The room is divided into three themed display sections arranged left to right:

**Left: The Graveyard.** Foam tombstones, plastic skeletons half-buried in fake grass, a wrought-iron fence prop, dead trees with hanging moss. A fog machine pumps ground-level mist. A tall hooded figure stands motionless among the graves.

**Center: The Carnival.** A prize booth with stuffed animals and a suspicious-looking chest. Cotton candy machines trailing sticky web-like strands. Spinning carousel props. A mannequin in a clown costume stands behind the prize booth counter, holding a mallet.

**Right: The Asylum.** Padded walls (foam panels), a metal gurney on wheels, harsh overhead strobes. A mannequin in a torn straitjacket thrashes silently against its bindings, head jerking. Medical equipment props litter the area.

### Environmental Effects

#### Progressive Activation
The sets activate left to right as the party moves through them. Entering the Graveyard section activates its mobs and hazards. Pushing into the Carnival activates it while the Graveyard hazards **keep running**. By the Asylum, all three sets' environmental effects are layered.

This rewards pushing forward as a group. Hesitating or splitting up means dealing with compounding hazards. The party can't clear one set and rest — the dungeon keeps pressure on.

#### Graveyard: Skeleton Arm Grab
Skeletal arms erupt from the fake grass at random intervals.
- 5 physical damage + 3s root on contact.
- Affects any entity walking through the graveyard section (including mobs if repositioned there).
- The arms retract after grabbing — they're environmental, not mobs. But [Skeleton Arm Crawlers](mobs.md#skeleton-arm-crawler) are also present as actual minion-tier enemies.

#### Carnival: Cotton Candy Web
Sticky strands of cotton candy-like substance coat surfaces in the carnival section.
- Characters who move through webbed areas suffer -50% movement speed.
- Destroyable by fire (burns away instantly — Vanessa's element).
- Reforms over 30s if not fully cleared.

#### Asylum: Concentrated Strobe
The overhead lights in the asylum section are more intense and irregular than the Flicker Hall's.
- **-5 accuracy** for all entities in the asylum section (persistent, not intermittent).
- Stacks with the Flicker Hall's strobe if somehow both apply.
- The gurney rolls toward the loudest sound every ~20s (10 physical damage on collision, knockback).

### Encounter: Graveyard Set

**Activated by:** Entering the graveyard section.

The tall hooded figure is a [Reaper Mannequin](mobs.md#reaper-mannequin) (Elite). It begins a slow advance toward the party. 4-6 [Skeleton Arm Crawlers](mobs.md#skeleton-arm-crawler) (Minion) erupt from the ground around the tombstones.

**Behavior:**
- Skeleton Arms root targets in place. The Reaper advances slowly but hits devastatingly with Reap (16 damage cone, 2s telegraph).
- The combination is dangerous: get rooted in front of the Reaper and eat a full Reap.
- **Counter:** Don't stand in front of it. Watch the wind-up. Kill the Crawlers to keep mobile.

### Encounter: Carnival Set

**Activated by:** Entering the carnival section (or as the party pushes past the Graveyard).

The [Clown Mannequin](mobs.md#clown-mannequin) (Elite) steps out from behind the prize booth counter. It squeezes its horn.

**Behavior:**
- Opens with Honk Horn — taunting one party member (forces them to attack the Clown for 3s).
- If it taunts a healer or caster, the party loses support at a critical moment.
- Follows up with Mallet Slam (14 damage + 2s stun) on the taunted target.
- The cotton candy webs slow movement, making it harder to reposition away from the Clown.

**The Obvious Mimic:**
The prize booth has a treasure chest sitting on the counter. It has teeth-shaped edges. It wiggles. There's a "WINNER!" sign above it.

If anyone interacts with it, it's an [Obvious Mimic](mobs.md#obvious-mimic-prize-chest) — standard fight, nothing surprising. The party spots this one a mile away.

**Selene's line:** "I'd never get fooled by a stupid mimic."

(Remember this.)

### Encounter: Asylum Set

**Activated by:** Entering the asylum section.

The [Straitjacket Mannequin](mobs.md#straitjacket-mannequin) (Elite) is thrashing against its bindings. It's not hostile yet — it activates when a character enters the asylum section or when it takes damage.

**Behavior:**
- Initially restrained — can only use basic melee (11 damage) while in the jacket.
- At 50% HP (75), it triggers **Berserk** — tears free, breaks all CC, gains +3 damage and a second attack.
- Berserk cannot be controlled, stunned, or charmed. You can only burn it down fast.
- The -5 accuracy from the asylum strobes makes this harder.

**Story beat:** The party has been learning CC all dungeon. Now they face something CC doesn't work on. Adaptation.

### Lesson

Positioning matters. Environment awareness matters. Three different Elite archetypes teach three different lessons:
- **Reaper:** Don't stand in front of the big hit (telegraphed avoidance).
- **Clown:** CC can target *you* — protect your backline (forced engagement).
- **Straitjacket:** Some things can't be controlled — recognize when to just burn (anti-CC).

---

## Room 4: Back Storage Maze

*Behind the retail floor — the storage area. Tight corridors, low visibility, ambushes. The deadliest room before the boss.*

### Description

A heavy "EMPLOYEES ONLY" door leads from the showroom into the back storage area. The atmosphere shifts immediately — no more themed displays or theatrical lighting. This is industrial: metal shelving units eight feet tall forming tight corridors, fluorescent tubes buzzing overhead (some broken, some flickering), concrete floor, the smell of cardboard and dust.

Visibility drops to about 10 feet. The corridors are narrow — only two people can walk side by side. Boxes are stacked on shelves, some spilling open to reveal stored Halloween inventory: masks, props, costumes, animatronic parts.

Somewhere deeper in, a servo motor whines and stops.

### Environmental Effects

#### Fog Machines
Industrial fog machines stored throughout the maze area. Some activate when the party enters nearby corridors, filling them with thick magical fog.
- **-3 accuracy** in fogged corridors. Stacks with any other accuracy penalties.
- **50% reduced visibility** (5-foot effective sight range).
- Fog machines can be found and destroyed (10 HP each). The fog clears over 10s once the machine is destroyed.
- Selene can spot active machines while scouting ahead.

#### Shelf Collapse
The tall shelving units are overloaded and unstable. Heavy melee combat near them can trigger a collapse.
- **Trigger:** 25% chance per round of melee combat adjacent to an unstable shelf (Selene can spot these with Perception).
- **Effect:** Domino collapse in a line — 10 physical damage + 1s stagger + prone to anyone caught.
- Can block a corridor until cleared (STR check DC 10 or 1 round of work).
- Can be intentionally triggered as a tactic against pursuing mobs.

#### Falling Boxes
Lighter version of Shelf Collapse.
- **Trigger:** 50% chance when melee occurs near loaded shelves.
- **Effect:** 6 physical damage + 1s stagger. No prone, no corridor block.
- Annoying but not dangerous. Adds to the claustrophobic feel.

### Encounter 1: Crawling Torsos

**Triggered by:** Moving through the first corridor section.

2-3 [Crawling Torsos](mobs.md#crawling-torso) drag themselves along the floor between shelving units. They're heard before they're seen (servo whine, scraping plastic).

**Behavior:**
- Ambush from floor level. Ankle Grab roots targets in place.
- In tight corridors, getting rooted means blocking the path for allies behind you.
- Individually manageable. The danger is getting rooted when something else is coming.

### Encounter 2: The Spider

**Triggered by:** Reaching a T-intersection deeper in the maze.

A [Giant Spider Prop](mobs.md#giant-spider-prop) drops from the top of a shelving unit onto whoever is in front (likely Clint, or Selene if she's scouting).

**Behavior:**
- Opens with Ceiling Drop (14 damage + 2s prone) from stealth.
- Immediately Webs the corridor behind the party (cutting off easy retreat).
- Alternates between Venomous Bite (damage + poison DoT + slow) and repositioning to web more corridors.
- Selene's Perception can spot it before the ambush — this is where the Rogue's scouting proves critical.

**Story beat:** If Selene is scouting ahead, she spots the spider and warns the party. If she isn't, someone gets ambushed. The dungeon rewards rogue gameplay.

### Encounter 3: Shrink-Wrapped Mannequins

**Triggered by:** Walking past storage pallets in a wider section of the maze.

2-3 [Shrink-Wrapped Mannequins](mobs.md#shrink-wrapped-mannequin) tear free from plastic wrap as the party passes.

**Behavior:**
- Slow but armored (AR 10 vs normal 6). Basic melee, no abilities.
- Fire damage ignores their AR bonus (melts the wrap).
- In tight corridors, Vanessa's fire is effective but risks hitting allies.
- The friendly fire question returns in a new context: can Vanessa use fire without burning the party *again*?

### Encounter 4: Severed Hand Swarm

**Triggered by:** Combat noise in the maze. Hands emerge from boxes on shelves.

4-8 [Severed Hands](mobs.md#severed-hand-swarm) swarm toward whoever is fighting.

**Behavior:**
- Climb onto fighters, grab weapons and arms. -1 accuracy per 2 hands in melee (max -3).
- Individually one-shottable but they keep coming from the shelves.
- Best dealt with by AoE (Rebekah's songs, Vanessa's spells) or by moving away from the infested corridor.

### The Mimics

Scattered throughout the maze. Not triggered by movement — triggered by **interaction** (trying to loot, open, or use the object).

**[Candy Bowl Mimic](mobs.md#candy-bowl-mimic):** A "Take One" candy bowl on a shelf. Looks completely normal. Jaw Snap on interaction (11 damage + 2s root).

**[Cash Register Mimic](mobs.md#cash-register-mimic):** A dusty cash register on a counter. Drawer slightly open showing bills. *Cha-ching — chomp.* (11 damage + 2s root).

These have **no visual tell**. Unlike the obvious chest in Room 3's carnival, these look like normal objects. The party learns that "loot everything" has consequences.

### Story Beat: Selene's Value

This room is where the Rogue justifies her existence. Tight corridors, ambushes, traps, hidden threats — Selene scouting ahead spots:
- Unstable shelves before they collapse
- The Giant Spider before it drops
- Fog machines before they activate
- Potentially the mimics (Perception check)

If the party lets Selene scout, the maze is manageable. If they charge in together, it's a meat grinder.

This builds Selene's confidence — including her confidence that she can spot mimics. Important for Room 5.

### Lesson

Scouting matters. Rogues matter. Tight spaces change everything — AoE is dangerous, healing requires line of sight, the group can't rely on the same tactics that worked in the open showroom. Don't blindly loot.

---

## Room 4a: Supply Closet (Optional — Hidden)

*A hidden side room off the maze. Reward for Rogue gameplay.*

### Description

A section of the maze wall that looks slightly different — the partition seam is less visible, and there's a faint outline of a door frame under the shelving. A padlock secures a latch that's mostly hidden behind a box.

**Discovery:** Selene spots the hidden door (Perception or Stealth awareness — she's looking for anomalies while scouting). The padlock requires lockpicking (Moderate difficulty for L10).

### Interior

Small room — 8 × 8 feet. A metal desk, a rolling chair, cleaning supplies on a shelf, a mop bucket. Paperwork scattered on the desk.

**Dan foreshadowing:**
- A name badge on the desk: "DAN — Store Manager"
- A "MANAGER OF THE MONTH" plaque on the wall (every month for the last year, all Dan)
- A scheduling board: "DAN - ALL SHIFTS"
- A motivational note pinned to the corkboard: "If you're reading this, you're already behind on stocking."

The room feels less like a dungeon and more like a sad office. Which makes it creepier.

### Loot

On the desk, partially hidden under paperwork: a **Halloween Treat Bag**.

Candy-pumpkin shaped, bright orange, made of a material that feels sturdier than it looks. The system recognizes it as:

**Treat Bag of Holding**
- **Type:** Accessory (belt-attachable)
- **Quality:** Uncommon
- **Effect:** Functions as a small bag of holding. Limited capacity (roughly a large backpack's worth — not as large as [Clint's](../../../characters/party/clint.md) Fanny Pack of Holding, but practical).
- **Appearance:** An orange jack-o-lantern trick-or-treat bag with a drawstring top. Looks like a child's Halloween candy bag. Is actually a pocket dimension.

No encounter. The loot is the reward for Selene finding and opening the door.

---

## Room 5: Employee Hallway

*The calm before the storm. Comedy relief, dread, and one more mimic.*

### Description

The maze ends at a plain door marked "BREAK ROOM →". Beyond it: bare drywall, steady fluorescent lighting (no strobes — the normalcy is almost unsettling after the rest of the dungeon), linoleum floor.

The hallway has the trappings of a real workplace:
- A time clock with blank time cards
- A bulletin board with employee notices ("Mandatory Fun Day — Saturday!" "Please label your food in the fridge." "HR reminder: costumes must be returned WASHED.")
- Motivational posters featuring skeletons in business suits: "SYNERGY IS OUR STRENGTH." "TEAMWORK MAKES THE DREAM WORK." "YOUR PERFORMANCE REVIEW IS OVERDUE."
- A scheduling board outside the break room: "DAN - ALL SHIFTS" (echoing the supply closet)
- A vending machine that appears functional but dispenses only dust

### The Break Room

A small room with a table, two chairs, a microwave, a mini-fridge (empty), and a **couch**.

The couch looks exhausted and inviting. Sagging cushions, a throw blanket draped over one arm. After the Flicker Hall, the Bear Trap, the Showroom, and the Storage Maze, it is the most beautiful thing anyone has ever seen.

### The Mimic Couch

Selene sees the couch. She doesn't hesitate. She doesn't check. She dives.

The [Mimic Couch](mobs.md#mimic-couch) swallows her to the waist. Just her legs sticking out, kicking.

The rest of the party rushes to help — but [Rebekah](../../../characters/party/rebekah.md) holds up a hand. *Wait.*

Selene's not in real danger. Her 999 HP pool means the mimic's chip damage (3 per 2s) is doing effectively nothing. Rebekah wants to savor this. She may actually sit on the floor and watch.

Callback: *"I'd never get fooled by a stupid mimic."*

Eventually someone (probably [Wade](../../../characters/party/wade.md), too nice to leave her) pulls Selene free. The couch snaps at them and becomes a normal (easy) fight.

### The Door

At the end of the hallway: a door marked "MANAGER'S OFFICE." The motivational poster next to it shows a skeleton in a suit pointing at the viewer: "YOU'RE NEXT FOR YOUR REVIEW."

Beyond: the boss room.

### Lesson

Comedy relief. Tension release before the final fight. Character moment for Selene and Rebekah. The corporate horror aesthetic shifts the dungeon's tone — the real monster was management all along.

---

## Room 6: The Spotlight Room (Boss)

See [boss.md](boss.md) for the full encounter.

### Description

The manager's office opens into something much larger than it should be — a vast, dark space. The floor is polished concrete. A single spotlight illuminates the center.

Standing in the spotlight is a mannequin in a rumpled suit, holding a briefcase. It looks like [Dan](../../../characters/villains/dan.md). Same build, same posture, same condescending tilt of the head. A name badge reads "STORE MANAGER."

Flanking it on either side, just outside the light: two Giant Skeleton Puppets, 12 feet tall, held upright by visible strings that disappear into the darkness above. Their ribcages glow faintly.

The Store Manager adjusts his tie.

*"Let's discuss your performance."*
