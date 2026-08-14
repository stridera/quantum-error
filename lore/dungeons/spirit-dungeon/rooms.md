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

The glimpse is a **shared scene**: the four who won stand among the restored mirrors and see *each other* in the glass, transformed — narrated through [Clint's](../../../characters/party/clint.md) POV (the only POV we ever get). Everything in the glass carries a deep power pulsing through it:

- **Clint** — black plate mail with glowing purple sigils (System script, brightening across pauldrons and gauntlets as he moves), his sword and shield glowing softly. The sword flickers faintly at the edges, as if it can't settle on a single reality; the shield carries a hexagonal scale motif. *(Subtle nod to [Katsuragi](../../../items/weapons/katsuragi.md) and the [Aegis](../../../items/armor/aegis-of-decoherent-deflection.md) — never named in prose.)*
- **Vanessa** — robes that shift colors, sigils appearing and disappearing as she moves, the cloth cycling in step with her Mana Lucent glow.
- **Selene** (the group glimpse, distinct from her private return below) — clad in shadows, hard to look at; a wicked dagger in each hand, pulsing with red energy.
- **Rebekah** — a beautiful dress, and a guitar half-medieval, half-futuristic: carved lute-like body on one half, luminous fretwork and strings of hard light on the other.

[Wade](../../../characters/party/wade.md) gets none of it. He failed the challenge, so the glass offers him no idealized self — while the other four stand reflected in their epic gear, Wade is on the floor, crying. The contrast is the point: the room shows the party what they're becoming, and shows Wade only what he couldn't face. *(Author canon, unrevealed in prose: his mirror **does** hold a future self — the most radiant kit in the room, white-and-gold vestment-plate that gives light rather than reflecting it, a staff crowned by a slow-turning halo of System script, healing light pooling at his feet. Everyone else's reflection is armed; Wade's is what keeps them standing. It stays in the glass for a future Spirit Dungeon.)*

This is a purely narrative beat — no mechanical effect. The [Mirror Shards](../../../items/accessories/mirror-shards.md) do the mechanical work; the mirrors do the emotional work. Use this scene in prose when the story wants to remind the reader what the party is becoming rather than what the dungeon cost them.

### Lesson

Identity. The Spirit Dungeon tests who you are, not just what you can do. The Mirror Shards are earned through self-confrontation — but not every wound is ready to be faced. Level doesn't protect you from this. Being the strongest, the steadiest, the most needed — none of it matters if the mirror finds the thing you can't look at yet.

---

## Room 3: Seasonal Showroom

*The main floor — a large open area with three themed horror display sets. The party's first true test of coordination and environmental awareness.*

### Description

The corridor opens into a cavernous space — the main retail floor. The ceiling is higher here (or appears to be; the dark fog still obscures it). The room is divided into three themed display sections arranged left to right:

**Left: The Graveyard.** Foam tombstones, plastic skeletons half-buried in fake grass, dead trees with hanging moss. A fog machine pumps ground-level mist. A wrought-iron fence prop closes off the back, and lashed to a cross-stake beyond it stands a **scarecrow** — burlap sack head carved into a grin, two embers for eyes that track the party and flare each time a grave opens.

**Center: The Carnival.** Packed dirt underfoot. A wall of popcorn and cotton-candy machines trailing sticky web-like strands; a spinning carousel of mutated animals. In the middle, a **whack-a-gnome** arcade game — mallets racked on either side, little gnomes popping up and down. Across from it, a prize booth stuffed with plush animals and a suspicious gold-chained chest labeled "GRAND PRIZE," with a mannequin in a clown costume behind the counter holding a mallet.

**Right: The Asylum.** Foam padded rooms, harsh strobes over grimy linoleum. On the left, a mannequin in a torn straitjacket thrashes silently against its bindings. On the right, a shock-therapy tableau: a mannequin patient on a wheeled gurney, one lab-coated mannequin pressing shock paddles to its temples and another looming with a syringe and a bone saw. At the back, a locked "AUTHORIZED PERSONNEL ONLY" door flanked by two guard mannequins.

### Environmental Effects

#### Progressive Activation
The sets activate left to right as the party moves through them. Entering the Graveyard section activates its mobs and hazards. Pushing into the Carnival activates it while the Graveyard hazards **keep running**. By the Asylum, all three sets' environmental effects are layered.

This rewards pushing forward as a group. Hesitating or splitting up means dealing with compounding hazards. The party can't clear one set and rest — the dungeon keeps pressure on.

#### Zone Lines (Section Barriers)
The three sets are divided by hard scene borders — the wrought-iron fence, and the change in flooring (grass → packed dirt → linoleum). Mechanically these act as **threat boundaries:**
- **Threat, taunt, and forced-focus effects do not cross a zone line.** Clint's [Commanding Shout](../../../classes/paladin-of-the-system.md) can pull a mob within his current section, but **cannot reach across the fence.** If he's knocked into the Carnival, he cannot yank the freed Scarecrow to him — and vice versa.
- Most mobs hold their own set. **Exceptions chase:** loose [Gnomes](mobs.md#whack-a-gnome-game-mechanic--minion) will cross a zone line to reach their random target, and a **knockback** (the Scarecrow's Reap and Sow) or an illusion can *force* any body across — which is how the sections bleed together. Either way threat still can't follow: **you cannot taunt a crosser back to you.**
- **Damage still crosses.** Ranged attacks and spells work across the line (Vanessa can bolt the Scarecrow from the carnival). It's *threat/taunt* that's blocked, not harm.
- **Each zone is its own sealed world — sight crosses, sound doesn't.** Stepping over a line drops you bodily into that set's ambiance: the **graveyard** becomes muted night — a moon behind moving cloud, cold soil and the sour tang of death, swaying trees, an owl somewhere, knee-deep mist — while the **carnival** is bright and *loud*, calliope music, popcorn, and the gnomes' chant piled on top of one another. You can still **see** into the neighboring zones (and the showroom ceiling overhead), but you **can't hear across a line** and your own voice doesn't carry out. A character launched into the carnival watches his party shout from the graveyard with no sound reaching him — and his [Commanding Shout](../../../classes/paladin-of-the-system.md) dies unheard at the fence (threat *and* sound both stop at the border).
- **The relay — Clint's one loophole.** [Strider](../../../characters/party/clint.md#patron-strider) hears everything and pipes it straight into Clint's head, so a cut-off Clint still gets his teammates' shouts — *relayed,* filtered through a god who editorializes (*"Vanessa is screaming at you. Understandable."*) and quotes at his leisure (*"She said, and I quote, 'Use the mallet, you idiot.'"*). It's the party's only cross-zone comms, routed through the one member who can't mute it.

This is what makes the launch bite: Clint is stuck whacking gnomes, and the party fights the freed Scarecrow a fence away — without their tank's taunt to bail them out, and without a word passing between them except whatever Strider feels like relaying.

#### Graveyard: Skeleton Arm Grab
Skeletal arms erupt from the fake grass at random intervals.
- 5 physical damage + 3s root on contact.
- Affects any entity walking through the graveyard section (including mobs if repositioned there).
- The arms retract after grabbing — they're environmental, not mobs. But [Skeleton Arm Crawlers](mobs.md#skeleton-arm-crawler) are also present as actual minion-tier enemies — and **every downed [Risen Skeleton](mobs.md#risen-skeleton) can leave one behind** (see Crawling Remains). Stomp the arms as you go or get pinned when the Scarecrow breaks free.

#### Graveyard: Grave Mist
The fog machine keeps a knee-deep layer of mist across the graveyard.
- **Low concealment:** anything at ground level — arm grabs, [Arm Crawlers](mobs.md#skeleton-arm-crawler), a downed skeleton's twitching arm — is **hidden in the mist until it strikes.** No pre-spot, no telegraph. This is what turns the arms into a real vigilance tax.
- **Perception/Veil Sense sees through it:** [Selene](../../../characters/party/selene.md) can pick the low threats out of the mist — the Rogue's job, and why she opened the scene stealthed here.
- **Veil-friendly:** anyone crouched in the mist gets a small bonus to stealth/Veil re-entry.
- **Fire burns it off:** a Fireball or Flame Wave clears the mist in its radius for ~10s, exposing everything low — a real reason for Vanessa to torch the graves despite the friendly-fire risk.
- Standing figures aren't obscured — the Scarecrow's embers still glow through it.

#### Carnival: Cotton Candy Web
Sticky strands of cotton candy-like substance coat surfaces in the carnival section.
- Characters who move through webbed areas suffer -50% movement speed.
- Destroyable by fire (burns away instantly — Vanessa's element).
- Reforms over 30s if not fully cleared.
- **Traps gnomes:** a loose [Gnome](mobs.md#whack-a-gnome-game-mechanic--minion) knocked or lured into the webs is stuck in place — the way non-mallet allies pin one for a mallet-bearer. Note the tension: burning the webs for mobility also *frees* any trapped gnomes.

#### Carnival: Carousel (The Motor)
A spinning carousel of mutated animals, calliope music looping. **It drives the whole gnome problem** — full rules and the four mount-bosses in [Carousel — The Motor](mobs.md#carousel--the-motor).
- Gnomes spawn *only while the carousel turns.* Its motor is the **one true off-switch** — but the central switch only sticks once all **four mounts are dead** (a living mount cranks it back on).
- The four mounts are **bound to the platform and can't leave it,** so the carousel is **spatially optional** — a careful party stays off it; yours gets forced onto the whack-a-gnome and has to deal with it. Fighting from the edge feeds one mount at a time; **jumping on to rush the motor spins it double-time → double gnome spawn.**
- Killing the four ends the gnome flood. [Rebekah](../../../characters/party/rebekah.md), a Temporal Bard, is the one who reads that the gnomes move to the carousel's beat.

#### Carnival: Popcorn (Flavor)
The popcorn machines along the wall still work — the smell of butter cutting through the fog.
- Mostly atmosphere. The "real" carnival snack is the [Bag of Kettle Corn](mobs.md#ticket--prize-booth-mechanic) ticket prize; loose popcorn on the floor is just popcorn (a trivial nibble, no buff).
- **One light touch:** kernels are **loud underfoot** — crunching through a drift is a soft stealth tell, one more thing [Selene](../../../characters/party/selene.md) has to mind when she's picking her footing. Easily ignored or cut; upgrade to a greasy slip-hazard if you want a second movement wrinkle.

#### Asylum: Concentrated Strobe
The overhead lights in the asylum section are more intense and irregular than the Flicker Hall's.
- **-5 accuracy** for all entities in the asylum section (persistent, not intermittent).
- Stacks with the Flicker Hall's strobe if somehow both apply.
- A **loose wheeled gurney** (empty — *not* the Patient's strapped-down treatment table) rolls toward the loudest sound every ~20s: 10 physical damage + knockback on collision. It hunts casters and singers — [Rebekah's](../../../characters/party/rebekah.md) songs and [Vanessa's](../../../characters/party/vanessa.md) casting draw it.
- **It's a trap on wheels.** On collision, its restraint straps snap out and **buckle the caught character down.** A dented **crash cart** is bolted to the gurney's lower shelf — paddles on retractable arms that clamp to the victim's chest the moment the straps close. The gurney does not need the doctors. It is equipped to work alone.
- **Cardiac Cycle (the teeth).** Once a victim is strapped, the cart discharges **every 3s**: 8 damage and **Convulsing** (1s) — *any action in progress is lost.* A cast dies mid-word, a song drops, a drawn weapon clatters. Each discharge also adds a stack of **Fibrillation**; at **5 stacks the victim goes Unresponsive** — downed at 1 HP, out of the fight until a Cleric brings them back. That's a **~15-second clock** that runs whether or not anything else in the room is alive.
- **The trap is the flailing, not the straps.** Party STR is 20 across the board and the straps *are* beatable by a rip (STR check) — but ripping out takes a committed, unglamorous second, and the obvious instinct is to blast the thing holding you. Every cast gets eaten by the next discharge. **The victim's own panic is what keeps them on the table**; a calm character walks away from this hazard, which is precisely why it catches [Vanessa](../../../characters/party/vanessa.md) (hastiness under pressure is her flaw of record). Ally rescue is 10+ damage to the gurney, a hard pull, or cutting the straps.
- **Two outcomes, and the Orderly picks which.** If an [Orderly](mobs.md#asylum-orderly) still lives, the gurney *also* careens back toward the treatment tableau to make the victim the **next Patient** — arrival starts a fresh full [Treatment](mobs.md#asylum-orderly) on a party member, the same ~20s clock, ending in one of their own rising as a [Lobotomized Patient](mobs.md#lobotomized-patient-conditional-add). If the Orderlies are dead, the gurney simply **parks where it stopped and cooks the victim on its own.** Killing the Orderly removes the worst branch; it does not make the gurney safe.
- The [Head Surgeon's](mobs.md#head-surgeon-holds-the-key) Sedative (**Sleep** on a target already below 25% HP) is what makes the grab stick — a downed caster can't thrash free on their own.

### Encounter: Graveyard Set

**Activated by:** Entering the graveyard section.

The [Scarecrow of the Fallow Row](mobs.md#scarecrow-of-the-fallow-row-graveyard-miniboss) (Elite miniboss) is lashed to its cross-stake behind the fence. As the party enters, its eyes flare and **5 [Risen Skeletons](mobs.md#risen-skeleton)** (Minion) claw up from the graves. The Scarecrow itself is **bound** — it cannot move or be reached in melee, and only takes 25% damage from ranged/spells while staked.

**Behavior — Bound phase:**
- The Scarecrow harasses at range with **Sickle Fling** (12 damage, telegraphed line) while re-raising fallen skeletons (max 3 re-raises, telegraphed by pulsing eyes and a tolling bell).
- Killing skeletons is the whole job. When none stand and its re-raises are spent, the Scarecrow **rips the stake from the ground and breaks free.**
- **[Wade](../../../characters/party/wade.md)'s Turn Undead / divine damage does +50% to the skeletons** — his one strong lever while **Broken**. Let the compromised healer clear the graveyard.

**Behavior — Freed phase:**
- The Scarecrow becomes a fully attackable Elite (150 HP) wielding the stake as a greatsword: **Harvest** (16/11 cone, 2s tell).
- Its **first** swing on freeing is **Reap and Sow** — an overhead smash that knocks the struck target 20 feet back, over the fence and onto the [Whack-a-Gnome](mobs.md#whack-a-gnome-game-mechanic--minion) in the carnival. This is the intended beat that forces the graveyard and carnival to run simultaneously (see below).
- **Counter:** don't stand in the cone. Burn it while the rest of the party keeps the launched member alive across the fence.

**Progression beat — Clint dings L4.** He's tanked L10 content as an L3 since Ch 15 (Flicker Hall, the bear at 7 HP, his own echo); the five-plus summoned L10 skeletons here finally tip the backlog over. He hits **L4 mid-clear**, and the timing lands: **Smite: Sanction** comes online with **+30% vs summoned entities**, so his upgraded smite immediately bonus-chews the [Risen Skeletons](mobs.md#risen-skeleton) and the scarecrow's re-raises — the anti-summon smite arriving against an actual summoner. He also unlocks **Shield Bash** (stun + threat). Cruel timing: seconds later Reap and Sow flings him onto the whack-a-gnome, where his whole kit is offline — he carries the new tools to the Asylum instead, and is on track for **L5 by the end of the showroom** (carousel Elites + asylum).

### Encounter: Carnival Set

**Activated by:** Pressing the game's **Start Game** button, or stepping up to play. The Scarecrow's Reap and Sow launches [Clint](../../../characters/party/clint.md) onto the machine — *landing* on it doesn't trigger it (his Luck holds), but **leaning on the Start button** as he scrambles back from the asylum guards does. (Entering the carnival on foot also activates the set.)

**The Whack-a-Gnome & the Carousel (one fight, one motor):** these read as two attractions but they're a single machine — the [carousel](#carnival-carousel-the-motor) *is* the whack-a-gnome's motor, and the swarm only ends when the carousel stops. Clint is flung over the fence by Reap and Sow, lands on the game (Luck spares him from triggering it on impact), and then — backing away from the asylum guards he's nearly stumbled into — leans on the **Start Game** button and sets the whole thing running. The carousel lurches to life with its own blaring song, and gnomes erupt from the holes: a first wave onto Clint, then an endless stream. Each loose [Gnome](mobs.md#whack-a-gnome-game-mechanic--minion) **picks a random party member and charges, taunt-proof,** crossing the fence to reach them. Three things land on Clint at once: his [System Identify](mobs.md#what-system-identify-gives-clint) reads the gnomes **INVULNERABLE** (and his machete skidded into off-limits asylum territory anyway), the [Underfoot](mobs.md#underfoot-passive--stacking-slow) slow stacks toward a root, and the [Gnomes Rule!](mobs.md#gnomes-rule-passive--sonic-aura) chant chops any cast. He can see Vanessa screaming across the graveyard line but **can't hear a word** — until [Strider relays it](#zone-lines-section-barriers): *"She said, and I quote, 'Use the mallet, you idiot.'"* The racked **Padded Mallets** are the only thing that touches a gnome anywhere, so he grabs one and plays; gnomes he can't reach get **kicked into the [cotton-candy webs](#carnival-cotton-candy-web)** to hang helpless — the party's stopgap while nobody else has a mallet. He snaps the second (chained) mallet free — promising the [Clown](mobs.md#clown-mannequin) he'll "fix it after," which settles it — and tosses it to **Selene,** the mobile gnome-hunter. Two mallet-bearers is the hard cap.

**The source never runs dry until the carousel does.** Whacking gnomes does **not** thin the flow — the motor spawns them forever and keeps spinning no matter how many fall. The *only* off-switch is killing all **four [mount-bosses](mobs.md#carousel--the-motor)** bound to the platform; a living mount cranks the motor back on, so the central switch only sticks when the last one dies. That makes the whole thing one long hold: mallets + webs to contain the swarm while the party burns down first the freed **Scarecrow**, then the **four carousel mounts** — and only on the fourth mount's death do the gnomes finally go quiet. For *this* party there's no urgency at the source — Clint's hacked stamina lets him whack indefinitely (his arms give out long before he's in any danger). The mounts are **spatially optional and bound to the platform:** fight them **from the edge** and the rotation feeds one at a time; **jump aboard** to rush the motor and it spins **double-time → double gnome spawn** (the impatient route just floods Clint harder). The upside of the grind: every mallet-kill drops **1 ticket**, and a full clear stacks toward the **500** Grand Prize — the [Prize Mimic](../../../items/accessories/mimic-pet.md), redeemed honest and tame. A careful party could skip the carousel entirely; yours is forced onto the game and walks out with a companion for the trouble.

**Tickets → Prizes:** tickets redeem at the booth counter for tiered prizes (see [Ticket & Prize Booth](mobs.md#ticket--prize-booth-mechanic)). The one that matters: **Carnival Shades** (10 tickets) cut the Asylum's strobe accuracy penalty by 3 — the reward for engaging instead of rushing past. Redeeming honestly keeps the Clown passive; **stealing** flips it hostile and wakes the mimic.

**The Clown:** the [Clown Mannequin](mobs.md#clown-mannequin) (Elite) is a **passive booth guardian** — it patrols, honors ticket redemptions, and periodically bonks the mimic still. It only turns hostile if someone attacks it, attacks the mimic, or grabs a prize/the chest without paying. Then it opens with **Honk Horn** (taunt, 3s) → **Mallet Slam** (14 + 2s stun). If it taunts a healer or caster, the party loses support at a bad moment. Cotton-candy webs (-50% move, burn with fire) make repositioning away from it hard. **Robbing the booth is a mug's game:** aggro the Clown and it [drops the act as a Champion](mobs.md#drops-the-act-champion-on-aggro), the unsold prizes [animate and fight for it](mobs.md#prize-rally-on-aggro) (and **break when beaten** — nothing that fought can be looted), and the [Store-Wide Alert](mobs.md#store-wide-alert-dungeon-response) sounds: the Manager's voice on the PA, and **every remaining mob in the dungeon converges at once,** zone lines no longer holding them to their sets. You *can* kill the Clown — it just costs the whole dungeon simultaneously, and the shelf is wreckage by the end.

**The Obvious Mimic:** the gold-chained chest displayed as "GRAND PRIZE — 500 TICKETS." Teeth-shaped edges; wiggles; a wet eye-shine flashes when the Clown looks away. Priced so nobody can buy it — the only way to "claim" it is to **steal** it, which triggers both the [mimic](mobs.md#obvious-mimic-prize-chest) and the Clown. The party spots it a mile away.

**Selene's line + the close call:** "I'd never get fooled by a stupid mimic." To prove it, she **pets the chest like a housecat** — a couple of unhurried strokes along the lid. The Clown tenses hard (grip whitening on its horn, a half-step it doesn't finish) but doesn't attack: petting isn't theft, and it can read exactly where the line is. Nobody triggers anything. It's the loaded gun that never fires — and it's what makes the [Room 5](#the-mimic-couch) couch dive land as the universe finally collecting.

**Compounding-hazard beat:** because the launch happens *before* the graveyard is finished, the party is now split — one member soloing the gnome puzzle while the rest fight the freed Scarecrow one fence over, both sections' hazards live at once. And per [Zone Lines](#zone-lines-section-barriers), **Clint can't Commanding Shout the Scarecrow across the fence** — no taunting it off his friends from the gnome pit. This is the dungeon punishing their "one section at a time" theory — the realized version of "what happens if we step into the next section? Let's not find out."

**The cost — and the beat:** the win pays out as **five Gold Century-Tickets, one per member** ([format](mobs.md#ticket--prize-booth-mechanic)), and each drifts to the item it buys — Clint to the shield, Vanessa to the friendly-fire Monocle, Wade to the Blue Ribbon, and so on. Then Selene, eyeing the 500 mimic, **spends her own ticket on it first** and turns the big-cat eyes on the rest. The **cave order is the characterization:** [Wade](../../../characters/party/wade.md) folds first — the Broken one giving up the healing item he wants most, because he needs the *joy* more — then Rebekah, with Vanessa and Clint (whose items are most *needed*) holding out longest before they crumble. **The button:** as the group-gift moment crests, the newly-tamed mimic **eats Wade's surrendered Blue Ribbon** off the counter — warmth then gag, back to back. *(The ribbon is **stored,** not lost — [it resurfaces at the boss](boss.md#phase-3-manager-exposed).)* A terrible trade, and Clint walks out still swinging the plastic machete by choice — which is exactly why it lands. (Full scene: [The 100-Ticket Set](mobs.md#the-100-ticket-set--the-temptation); the middle option is two Epic [250-rack](mobs.md#the-250-ticket-rack--two-or-none) picks.)

### Encounter: Asylum Set

**Activated by:** Entering the asylum section. The climax of the showroom and the **gate out of it** — the locked door leads into the back half of the dungeon ([Room 4](#room-4-back-storage-maze) onward), not straight to the boss.

This is one machine with four moving parts, all live at once:

**1. The Treatment (soft timer).** Two mannequin doctors work the strapped-down Patient: an [Asylum Orderly](mobs.md#asylum-orderly) channeling shock paddles and a [Head Surgeon](mobs.md#head-surgeon-holds-the-key) with a bone saw and syringe. The wired [Shock Cart](mobs.md#shock-cart-destructible-object--hazard) discharges **every 5s**, and each discharge **flares the strobes to a 1s blackout** (-8 acc that second) *and* advances the Treatment. **4 pulses ≈ a 20-second clock**, and the [Lobotomized Patient](mobs.md#lobotomized-patient-conditional-add) rises as a bonus Elite. Kill the Orderly or smash the cart (30 HP) to stop it. This add is entirely preventable — it's the punishment for tunnel-vision.

**2. The Straitjacket (anti-CC).** The [Straitjacket Mannequin](mobs.md#straitjacket-mannequin) (Elite) *looks* like a free park — it's already wrapped up — so the instinct is to leave a caster babysitting it on soft CC and focus elsewhere. That's the trap. **Can't Be Held** means slows and lures barely stick (half duration, 50%/s to break early); it rips loose and **charges whoever tried to control it,** forcing the tank to peel off his own target to body-block. Below 50% HP it **Berserks** — full CC-immunity, +3 damage, a second attack. There was never a way to lock it; the only answer is to burn it, and to have the tank ready the instant it slips. Its discharge tag reads **"TREATMENT: COMPLETE"** — it's a former Patient, a preview of what the strapped one becomes.

**3. The strobes (accuracy denial).** Persistent **-5 accuracy** across the asylum, spiking to blackout on every Treatment Pulse. The **Carnival Shades** from the whack-a-gnome (-3 to this penalty) are the reward for having engaged the carnival properly. Stacked with **Wade's Broken -25% healing**, this is where sloppy play finally can't be papered over.

**4. The gate.** The locked "AUTHORIZED PERSONNEL ONLY" door sits at the **back-center**, with two [Asylum Guards](mobs.md#asylum-guard-door-sentinel-2) flanking it — squarely **between** the treatment tableau on one side and the straitjacket cell on the other. They don't roam. **They guard the door, not the hall.** Crossing the middle hall at a distance is safe — the Guards *track* whoever passes, heads turning to follow, but they do not engage. They wake only when someone comes **within reach of the door** or attacks them, and then defend it to the death and **Interpose** anyone who grabs at it. The geometry is still the trap, just a tighter one: the *fastest* line from the Surgeon to the straitjacket cell hugs the door, and the safe line is a wide berth that costs seconds the [Treatment clock](mobs.md#shock-cart-destructible-object--hazard) doesn't have. A composed peel goes around. A panicked one cuts the corner and wakes them.

**The way out is the badge, and only the badge.** [Authorized Personnel](mobs.md#asylum-guard-door-sentinel-2): hold up the keycard the [Head Surgeon](mobs.md#head-surgeon-holds-the-key) dropped and both Guards straighten, step aside, and let the party through. They don't check the photo. They don't ask where it came from. They don't care that the man it belonged to is face-down on the linoleum behind you — he was authorized, the badge is authorized, the door opens. **The Guards are never killed and never need to be**; they return to post and stay live Elites at the party's back. Fighting them is possible, pointless, and the flattest available end to the room. The gate still holds, because the badge only drops from the Surgeon — *engaging the tableau was always the price.* The door opens into [Room 4](#room-4-back-storage-maze) ("EMPLOYEES ONLY").

**The last image of the showroom:** [Clint](../../../characters/party/clint.md) holding up a dead man's ID while two mannequins in rent-a-cop uniforms nod him through. Nobody says anything. It is the corporate-horror motif landing clean, and it rhymes forward into the Store Manager's *"Let's discuss your performance."*

**Hazard — the roving gurney.** Every ~20s the empty gurney rolls at the loudest thing in the room (10 damage + knockback), homing on [Rebekah's](../../../characters/party/rebekah.md) songs and [Vanessa's](../../../characters/party/vanessa.md) casting. On a hit its straps snap shut, its bolted-on crash cart clamps paddles to the victim's chest, and the **Cardiac Cycle** starts: a discharge every 3s that eats whatever action was in progress, stacking toward **Unresponsive** in ~15 seconds. If an Orderly lives it also hauls them back to the doctors for a full Treatment; if not, it parks and works alone — see [Concentrated Strobe](#asylum-concentrated-strobe). The backline can't just out-cast the room; being *loud* is what gets you strapped down, and **trying to cast your way off the table is what keeps you there.**

**The plan — and how it comes apart.** [Clint's](../../../characters/party/clint.md) [Identify](../../../characters/party/clint.md) reads the Patient on the gurney: *Treatment completing — hostile Elite in ~20s.* So the party plans around the clock. **Selene** is sent to burst the channeling [Orderly](mobs.md#asylum-orderly) — kill the clock, deny the elite. **Rebekah and Vanessa** are to park the [Straitjacket](mobs.md#straitjacket-mannequin) with soft CC (Dissonant Chord slow + a Minor Illusion lure). **Clint** takes the [Head Surgeon](mobs.md#head-surgeon-holds-the-key) for the badge.

**It goes sideways in order — and the whole collapse fits inside one 20-second window.** Clint's six [Smite: Sanction](../../../classes/paladin-of-the-system.md#level-4--smite-sanction) punches run on a 4s cooldown; the [Treatment](mobs.md#shock-cart-destructible-object--hazard) runs 4 pulses at 5s. **They are the same twenty seconds.** Run them as one clock, with a blackout flare marking every fifth second.

**1. The grapple is a trap, not a win.** Clint tackles the Head Surgeon and pins it — the correct play, since raw STR 20 beats a Skirmisher's DEX where his Novice proficiency can't. But the pin commits both hands *and his position*, and his entire kit is short-range: [Commanding Shout](../../../classes/paladin-of-the-system.md) is a **15 ft** area. He has put himself across the room from every problem he is about to have, face-down on the one thing they cannot leave without. Between smites he can do nothing but hold on and count.

**2. The Straitjacket takes Rebekah, and competence is what gets punished.** It **shrugs the soft CC almost instantly** ([Can't Be Held](mobs.md#straitjacket-mannequin)) and charges **the caster who actually touched it.** Vanessa's Minor Illusion is a lure — no damage, no threat — so her *failure* is what keeps her safe. Rebekah's Dissonant Chord is a real debuff, so it comes for her. [Wade](../../../characters/party/wade.md) steps in front of her with **no taunt in his kit at any level he has**, while **Broken** (−25% output): body and voice only, against an Elite Brute that Berserks at 75 HP.

**3. Clint learns the room fell apart from his own status bar.** [Temporal Boost](../../../classes/temporal-bard.md) has a **~6s fade** — when Rebekah is charged and her songs drop, Clint's haste *decays* rather than snapping off. He feels it sag while pinned, facing the wrong way, and knows what it means before anyone screams. **He should never turn his head in this fight**; the blackout flares and the fading buff carry it.

**4. Selene's choice.** She's two hits from the channeling Orderly when Rebekah gets hit thirty feet behind her. **She finishes the kill** — it's the correct triage (denies the second Elite, freezes the Treatment, and defangs the gurney's worst branch), and it takes two seconds she will not forgive herself for. Then she breaks for Rebekah — and the roving gurney, homing on the loudest thing in the room, takes her **mid-run, one second after the choice.**

**5. Vanessa has to act, and her one tool is poisoned.** Freeing a strapped victim needs 10+ damage to the gurney, and **without the [Sharpshooter's Monocle](mobs.md#the-100-ticket-set--the-temptation)** — the ally-excluding prize she traded away for Selene's mimic — a Fireball into that gurney torches Selene too. She throws it anyway. Selene **rips the straps herself** in the same second (a beatable STR check that costs one committed beat) and **twists through the blast**: singed, ears smoking, tail smoldering, still moving — she is the party's **highest Luck (15)** and it shows, where Clint's **Luck 4** is why the same spell has stripped *him* to the skin twice. Both women acted; neither knew the other was. The relief is not vindication — it nearly killed a teammate, everyone saw it, and Vanessa now knows exactly what the Monocle was worth. [Strider](../../../characters/party/clint.md#patron-strider) needles Clint about the traded upgrade — a voice only Clint hears — and Clint has to relay it mid-fight, catching a glare for the messenger's trouble. *Oh — that's what those prizes were for.* Not a mechanic they get to fix; just the cost of the puppy, landing quietly mid-fight.

**The shape:** everyone is stuck watching someone they can't reach. Clint pinned. Selene strapped. Rebekah mauled. Wade holding with his body. Vanessa the only free hand, and her best spell hurts her friends. **The one person who cannot act without causing harm is the only one who can act** — and the chapter turns on her doing it anyway.

**Story beat:** the darkest stripe (shock therapy, bone saw, the implied lobotomy) sets the tone for the corporate-horror boss still to come — the "treatment / make you compliant" motif rhymes with the Store Manager's *"Let's discuss your performance."* The party clears the gate and pushes into the back half already worn thin, sustain compromised — the reason the whole run-up to the boss stays hard.

### Lesson

Positioning, environment awareness, and resource management under pressure. Each stripe teaches something distinct:
- **Graveyard (Scarecrow):** clear the adds to reach the real threat; don't stand in the big cone; a divine-damage healer has offense even when he can't heal.
- **Carnival (Whack-a-Gnome / Clown):** the world has *rules* — the right tool matters, greed is punished, and forced overlap breaks a tidy plan. CC can target *you*.
- **Asylum (tableau):** triage under a soft timer with accuracy denial, some threats can't be controlled (just burn), and progress is gated behind fully engaging the fight — no skipping to the boss. The reward from an earlier section (Carnival Shades) pays off here.

The showroom is also the first sustained test of the party **with a compromised healer** — Wade is still Broken out of the Mirror Room, and the strobes + compounding hazards mean his -25% output finally bites. They should reach the boss threshold worn down.

---

## Room 4: Back Storage Maze

*Behind the retail floor — the storage area. Tight corridors, low visibility, ambushes. The deadliest room before the boss.*

### Description

A heavy "EMPLOYEES ONLY" door leads from the showroom into the back storage area. The atmosphere shifts immediately — no more themed displays or theatrical lighting. This is industrial: metal shelving units eight feet tall forming tight corridors, fluorescent tubes buzzing overhead (some broken, some flickering), concrete floor, the smell of cardboard and dust.

Visibility drops to about 10 feet. The corridors are narrow — only two people can walk side by side. Boxes are stacked on shelves, some spilling open to reveal stored Halloween inventory: masks, props, costumes, animatronic parts.

Somewhere deeper in, a servo motor whines and stops.

### Design Principle: This Room Has No Encounters

**Room 4 is one continuous traverse, not a series of fights.** Every mob in it is individually trivial to this party — a [Crawling Torso](mobs.md#crawling-torso) is 60 HP at 25% movement speed, a [Shrink-Wrapped Mannequin](mobs.md#shrink-wrapped-mannequin) is a slow punching bag with no abilities — and against 999 HP pools none of them can generate a real healing callout. Run one at a time against a tank with a taunt, they are *"stand and hit until dead,"* and no amount of HP tuning fixes that.

**So the room is not asking whether they can win a fight. It is asking how much they have left when they come out the other side.** Wade is still [Broken](../../../characters/party/wade.md) (−25% healing) until dungeon exit, and `Lesson` below is explicit that they should reach the boss worn thin. Room 4 is the only place that bill comes due.

The mechanism is that **fighting is the failure state.** Combat makes noise, noise brings more of the maze, more of the maze means longer fights, and longer fights make more noise. The correct play is to route around contact entirely — which is what makes [Selene's scouting](#story-beat-selenes-value) load-bearing instead of flavor.

**What breaks their formation.** Clint-front / Wade-healing / ranged-behind is a *corridor* formation and it works fine in a corridor. Three things in this room dismantle it:

- **Taunt is shorter than the maze.** [Commanding Shout](../../../classes/paladin-of-the-system.md) is a **15 ft area**; visibility is **10 feet**, and **5 in fog**. Clint cannot hold a line he can't see or taunt something that hasn't arrived yet. Things simply get past him.
- **The shelves are eight feet tall.** Anything that comes *over* the top lands behind him, in the middle of the line, next to the healer. A tank in a corridor can only face one way.
- **A rooted tank is a wall.** [Ankle Grab](mobs.md#crawling-torso) is only 3 seconds — nothing in the open. In a corridor two people wide, a rooted Clint **blocks his own party**: nobody gets past him and the ranged line can't reposition.

> **Clint can heal.** [Cure Light Wounds](../../../classes/paladin-of-the-system.md#cure-light-wounds-paladin) restores 40–80 (vs the Cleric's 60–120) — *a Paladin patches; a Cleric heals.* This matters when the party splits: Clint's half does not die for lack of a healer. It **stalls**, because every heal he casts is a smite he doesn't. A healing tank deals almost no damage, and a fight he can't end is a fight that keeps making noise.

### Environmental Effects

#### The Noise Clock

**The room's core mechanic, and the thing that converts trivial mobs into real pressure.** [Encounter 4's](#the-traverse) original trigger — *"combat noise in the maze"* — generalized into a rising meter that governs the whole traverse.

**It never resets.** It decays slowly while the party is quiet, and only while they're quiet.

| Adds noise | Weight |
|---|---|
| Melee exchange | Low, but constant — long fights are the main source |
| [Rebekah's songs](../../../classes/temporal-bard.md) | **Moderate and continuous.** She is a Bard; buffing the party is *audible* |
| Commanding Shout | Moderate — the taunt is literally shouting |
| Spell impacts | Moderate |
| [Shelf Collapse](#shelf-collapse) | High, one-time |
| **Fire** | **Severe** — see [Fire in the Stacks](#fire-in-the-stacks) |

| Threshold | The maze answers |
|---|---|
| **1 — Quiet** | Nothing. Achievable only by avoiding contact |
| **2 — Noticed** | [Severed Hands](mobs.md#severed-hand-swarm) pour out of boxes on nearby shelves (−1 accuracy per 2 in melee, max −3) |
| **3 — Converging** | [Crawling Torsos](mobs.md#crawling-torso) start dragging toward the sound **from corridors already behind them** |
| **4 — Located** | The [Giant Spider](mobs.md#giant-spider-prop) repositions to cut off the route forward and webs to split the group |

**The teaching mechanic — noise is a debt, not a cost.** Torsos move at **25% speed.** Noise made now doesn't punish them now; it arrives four corridors later, from behind, while they're busy with something else. By the time the party understands the rule, they have already spent it. Rebekah is the one who works it out — she's the loudest member and the only one tracking rhythm.

**The bind this creates:** Rebekah's songs are the party's force multiplier *and* the steadiest noise source in the room. Buffed and hunted, or quiet and unbuffed. There is no third option, and Clint has to be the one to ask her to stop singing.

#### Fire in the Stacks

**Triggered by:** [Vanessa](../../../characters/party/vanessa.md) using fire to clear a corridor. Which is the correct read of the tactical problem — [Shrink-Wrapped Mannequins](mobs.md#shrink-wrapped-mannequin) take full damage through their AR from fire, the corridor ahead is packed, and a Fireball solves it.

It also solves it into **eight-foot steel shelving loaded with cardboard boxes, costume fabric, and stored plastic.**

- **The maze catches.** Fire spreads along the shelving line, corridor to corridor, faster than the party moves. It does not stop and cannot be fought.
- **Smoke replaces fog — permanently.** Same −3 accuracy and 5-foot visibility as the [fog machines](#fog-machines), except **there is no machine to destroy.** Vanessa's solution deletes the party's own counterplay: the one environmental hazard in this room they *could* switch off is now moot, and the replacement is worse and spreading.
- **It's the loudest thing in the room.** Roaring, collapsing stock, bursting aerosol cans in the cleaning supplies. The [Noise Clock](#the-noise-clock) goes straight to threshold 4 and stays there.
- **No backtracking.** The route behind them closes. Whatever they left unresolved, they left it.
- **Only forward.** This is the pressure that stops the traverse from ever becoming a defensive stand. They cannot hold a corridor, because the corridor is on fire.

> **The point of the beat:** Vanessa does the smart thing and it is a catastrophe. Not a mistake — a *correct read of the wrong system.* She is still thinking in open-showroom terms, where fire is an answer, and the maze is made of fuel. It rhymes with the [Asylum fireball](#encounter-asylum-set) (right call, terrible cost) and it is the second time in two rooms that her best tool is the problem. She should notice that.

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

### The Traverse

**Not four encounters — one running gauntlet.** The four mob groups below are the room's *instruments*, and each one attacks a different part of the party's formation. Run sequentially they are trivial. Run **concurrently, under a rising [Noise Clock](#the-noise-clock)**, they compound into the hardest stretch before the boss.

| Instrument | What it attacks | Run it with |
|---|---|---|
| [Crawling Torsos](mobs.md#crawling-torso) | **The front.** Root the tank; a rooted Clint plugs the corridor for his own party | Anything that needs him somewhere else |
| [Giant Spider](mobs.md#giant-spider-prop) | **Above and behind.** Ceiling Drop past the tank; webs to split the group | While they're pinned by torsos |
| [Shrink-Wrapped Mannequins](mobs.md#shrink-wrapped-mannequin) | **Nothing — it's a timer.** AR 10 sponge that makes a fight take twenty seconds | The Noise Clock, always |
| [Severed Hands](mobs.md#severed-hand-swarm) | **Accuracy.** −1 per 2 in melee, max −3 | Spawned *by* the clock automatically |

**The Shrink-Wrapped Mannequins are the key reframe.** As a fight they're nothing: 60 HP, no abilities, half speed. As a *timer* under a noise clock they're the worst thing in the room — twenty seconds the party cannot afford, getting louder the whole time, and the fastest way through them is Vanessa's fire, which sets the maze on fire. The mob whose entire design is "boring to fight" becomes the mob you desperately don't want to have to fight.

**Suggested shape of the traverse** (beats, not a script):

1. **First contact is cheap and teaches nothing.** Two torsos, heard before seen. Clint flattens them. Everyone relaxes. The clock ticks up and nobody knows there is a clock.
2. **The hands arrive** — threshold 2 — and read as an annoyance rather than a consequence.
3. **The wrapped mannequins block the corridor.** Now the party is fighting something slow while something fast is spawning behind them, and the fight *will not end quickly.* This is where Vanessa reaches for fire.
4. **[Fire in the stacks](#fire-in-the-stacks).** Clock to 4. No retreat, smoke everywhere, forced forward.
5. **The split** — see below.
6. **The Spider** takes the fractured party from above, in smoke, at 5-foot visibility, with everything they made noise about earlier now dragging itself up the corridor behind them.

### The Split

Fire, [webs](mobs.md#giant-spider-prop), and a [shelf collapse](#shelf-collapse) across a corridor should **separate the party** — and who lands where is the whole scene.

**The good split (use this one):** **Clint + Selene** forward, **Wade + Vanessa + Rebekah** back.

- **Clint's half stalls.** He can [patch](../../../classes/paladin-of-the-system.md#cure-light-wounds-paladin) Selene at 40–80 a cast, but every heal is a smite he isn't casting. A healing tank does no damage, so nothing dies, so the fight continues, so the noise continues. He is not losing — he is *stuck*, which in this room is the same thing.
- **Wade's half survives on his healing and has no front line.** The casters cannot be hit, so positioning becomes everything, and Wade — Broken, −25% — is the only reason it holds.
- **The near-miss is the point.** Wade happened to be at the back with the casters. Had the collapse landed one corridor forward, the casters would have had no healer and Clint would have had no damage. Somebody should say so out loud, and be right.

**Regrouping is navigation, not combat.** The two halves have to find each other in a burning maze with 5-foot visibility, which means **shouting** — and shouting is noise. The reunion costs them the thing they've been carefully hoarding, and there is no way to avoid paying it.

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

### Qubit Smells His Own Kind

**[Qubit](../../../items/accessories/mimic-pet.md) reacts to the maze's hidden mimics.** The [Candy Bowl](mobs.md#candy-bowl-mimic) and [Cash Register](mobs.md#cash-register-mimic) have **no visual tell** — that's their whole design — but the tame mimic trotting at Selene's heel knows exactly what they are. He goes **rigid and silent**, lid half-open, pointed like a bird dog. It is the only time in the dungeon he is ever quiet.

Selene reads him instantly and calls the mimics before anyone touches them. She takes the credit, obviously. *"I'd never be fooled by a stupid mimic."*

> **This is a trap, and it's the Room 5 setup.** For an entire room Selene has a **working mimic detector**, and it is flawless. She stops checking for herself, because she doesn't have to — the pet does it, every time, and being right over and over is what builds the confidence that kills her.
>
> **The payoff at the [Mimic Couch](#the-mimic-couch):** Qubit *does* react. He goes rigid and points, exactly as he has all dungeon — and **Selene misreads it**, because she's already moving, and because a chest going stiff at the sight of an enormous comfortable sofa reads as *him wanting it too.* She doesn't check. She dives.
>
> The detector never failed. She stopped listening to it. That's better than the pet being absent or asleep, because nothing malfunctioned — she simply trusted a system until she stopped reading its output, which is the same mistake the whole party makes about the [System](../../../system/overview.md) itself.

### Lesson

Scouting matters. Rogues matter. Tight spaces change everything — AoE is dangerous, healing requires line of sight, the group can't rely on the same tactics that worked in the open showroom. Don't blindly loot.

**And the room's real lesson: noise is a resource.** Everything the party is good at — taunting, singing, casting, winning fights quickly — is *loud*, and this is the first place in the story where being effective is what gets them hurt. They cannot fight their way through a room that manufactures enemies in response to fighting. The only winning line is the one Selene walks: quiet, ahead, and around.

---

## Room 4a: Supply Closet (Optional — Hidden)

*A hidden side room off the maze. Reward for Rogue gameplay.*

### Description

A section of the maze wall that looks slightly different — the partition seam is less visible, and there's a faint outline of a door frame under the shelving. A padlock secures a latch that's mostly hidden behind a box.

**Discovery:** Selene spots the hidden door (Perception or Stealth awareness — she's looking for anomalies while scouting). The padlock requires lockpicking (Moderate difficulty for L10).

### Story Beat: How Did You Learn To Do That?

**Selene has no lockpicks.** Her [inventory](../../../characters/party/selene.md#equipment--inventory) is a Prop Cutlass, rogue clothes, a Mirror Shard, and a mimic — the Transition didn't hand her a thieves' kit, and nobody has looted one.

So she takes two **hairpins** out of her hair and opens the padlock in under a minute, by feel, in a smoke-choked corridor at 5-foot visibility, without ever really looking at it.

**Clint is agog.** *"How did you learn to do that?"*

**The answer she gives** is breezy and immediate: it's a hobby. There's a whole community. It's mostly physics and patience. She used to sit through Zoom calls with her hands under the desk, working a practice lock by touch while three VPs argued about roadmap — *all feel, no sight, and nobody on the call ever knew.* She's laughing while she says it. It is completely true.

> **The answer she doesn't give.** She spent those years being someone who needed **privacy** — things that locked, and a life she kept in them. The hobby is real; so is the reason it stuck. She doesn't offer it and Clint doesn't hear it, and the only tell is that she answers **too fast**, the way she answers everything that isn't Rebekah asking.
>
> Play it as a comic beat. It should not land as a revelation until reread. See [Selene](../../../characters/party/selene.md#lockpicking-pre-transition).

**Why it matters mechanically:** she learned to do this **without looking.** That's the origin *and* the reason the skill works here — a maze at 5-foot visibility, full of smoke, is exactly the condition Dustin practiced in. The hobby's constraint is the skill's advantage, and it should be the same sentence.

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

**The tell (play it small).** Rebekah is the only one who doesn't even glance at Selene's HP before calling the hold — she already knows, because she tracks it. The scene stays 90% comic; the warmth is one beat, unremarked, and [Clint](../../../characters/party/clint.md) reports it without understanding what he's looking at. Something on the order of *she wasn't laughing at Selene so much as enjoying her* — then straight back to the joke. First-time readers should clock it only in retrospect. See [Rebekah](../../../characters/party/rebekah.md#selene) and [Selene](../../../characters/party/selene.md#rebekah); the setup beat is Selene's hesitation in the [Asylum](#encounter-asylum-set).

**Pet payoff:** if Selene bought the carnival's [Prize Mimic](../../../items/accessories/mimic-pet.md), she's had a tame one riding along all dungeon — which is *exactly* why her guard is down here. She dives on the couch because she "has one at home." The couch should visually echo the pet: the mimic she owns is the reason the mimic she doesn't check finally gets her.

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
