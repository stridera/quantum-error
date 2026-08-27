---
canon: true
stability: locked
last_reviewed: 2026-08-24
---

# Temporal Bard

Charisma-based magic users who cast using their voices and instruments. This subclass specializes in temporal manipulation through song.

## Design Philosophy

- **Role**: Support, buffs/debuffs, action economy manipulation
- **Theme**: Time effects primarily alter order, timing, and outcomes — direct damage is the exception, not the rule
- **Unique Mechanic**: Song stacking—multiple songs active concurrently up to song limit

## Core Rules

- All songs affect listeners within audible range
- Songs can stack; they do not replace each other
- Duration: sustained while singing plus fade time
- Time effects primarily manipulate order and timing. Only one minimal direct-damage song exists (**Dust Note**, L1), reserved as a baseline self-defense option. Every class gets some way to protect itself; the Temporal Bard's version is the least lethal in the game.

### Songs vs. Refrains

The Bard has **two** ability types, and the distinction is the class's whole economy.

| | **Song** | **Refrain** |
|---|---|---|
| Duration | Sustained while singing, plus fade | Played once; persists for hours |
| Slot cost | **Occupies a concurrent-song slot** | **None** |
| Mana | Upkeep, drains while playing | One-time cost at performance |
| Where | In combat | Out of combat only — cannot be started while in combat |
| Interrupt | Drops when she's hit or silenced | Already set; damage doesn't touch it |

A **Song** is a thing she is *doing.* A **Refrain** is a thing she has *done* — a settled pattern laid into the local timeline that keeps running without her. She hums it at camp and then goes to sleep.

**Why this matters mechanically:** [Harmonic Memory](#harmonic-memory) caps her at **2 concurrent songs**, and Temporal Boost + Veil of Offbeats already fill both in a real fight. If restorative music competed for those slots, every quality-of-life effect would cost the party its buffs. Refrains sit outside that economy entirely — the Bard's utility kit grows without ever taxing her combat kit.

> **Design note:** Refrains are the designated home for future non-combat temporal magic. Anything that should feel like *maintenance of the world* rather than *action in a fight* belongs here.

## Ability Progression (Levels 1-20)

| Level | Ability | Type | Effect |
|-------|---------|------|--------|
| 1 | [Chrono Resonance](../magic/spells/chrono-resonance.md) | Passive | Songs interact with temporal threads; songs function without instrument if needed |
| 1 | Temporal Boost | Song | Allies act and move faster. The party calls it "the haste song"; System-identified as Temporal Boost (Ch 16) — advanced temporal reference frame; stacks "by increasing certainty, not speed." |
| 1 | Dust Note | Song (damage) | Single plucked note inflicts a moment of accelerated decay on one target. Minimal damage — reserved as baseline self-defense. |
| 2 | Veiled | Passive | Ambient music makes the party unremarkable — observers overlook them unless actively searching (social stealth, not invisibility). Shown Ch 9, after Rebekah hit L2 in the first guard fight. |
| 2 | [Rejuvenation](#rejuvenation) | **Refrain** | Suspends the body's maintenance overhead for everyone who heard it. The reason nobody in this story ever has to stop and deal with being a body. |
| 2 | Rewind Note | Utility | Slightly rolls back a recent cooldown or timing mistake |
| 3 | Dissonant Chord | Song | Enemies fall out of sync—minor slow and confusion |
| 3 | Veil of Offbeats | Song | Allies blur across adjacent timelines, increasing evasion |
| 4 | Harmonic Memory | Passive | Maintain multiple learned songs concurrently |
| 4 | Da Capo | Utility | Rewinds one ally's mental state a few seconds — a fresh Mental debuff never happened. Single target, not herself. |
| 5 | Accelerando | Song | Increases ally attack and casting speed |
| 6 | Time Slip | Utility | Minor self rewind—adjusts position or state from moments ago |
| 7 | Echo Verse | Song | Periodically re-pulses the last song's effect |
| 8 | Temporal Awareness | Passive | Sense out-of-sync entities, altered timelines, and temporal interference |
| 9 | Lullaby of Pauses | Song | Enemies experience brief temporal stalls (hesitation, skipped beats) |
| 10 | Chrono Shield | Song | Incoming damage is delayed and softened as time absorbs the impact |
| 11 | Polyphonic Casting | Passive | Increases maximum concurrent songs |
| 12 | Stolen Moment | Utility | Chance to gain an extra action by borrowing from an adjacent beat |
| 13 | Dirge of Delay | Song | Enemy action economy slows (longer windups, delayed responses) |
| 14 | Refrain of Continuity | Song | Extends duration of active buffs and beneficial effects |
| 15 | Temporal Mastery I | Passive | Songs affect wider area and maintain coherence at greater distance |
| 16 | Time Ripple | Song | Songs can affect enemies not yet present in the immediate moment |
| 17 | Finale: Split Second | Song | Party acts before enemies at start of engagement |
| 18 | Perfect Pitch | Passive | Songs no longer require a *medium* — they function under Silence, underwater, for the deafened. (Instrument-free casting is L1 [Chrono Resonance](#chrono-resonance).) |
| 19 | Grand Cadence | Song | Powerful multi-buff crescendo affecting allies across timing dimensions |
| 20 | **Time Unbound** | Capstone | Ignore certain time-based restrictions (cooldowns, delays, sequence penalties) |

## Song Limit

The number of concurrent songs is limited and increases with:
- Harmonic Memory (Level 4)
- Polyphonic Casting (Level 11)

## Design Notes

Inspired by D&D Homebrew College of Time subclass.

## Notable Temporal Bards

- [Rebekah](../characters/party/rebekah.md)

## Beyond Level 20

Levels 1–20 above are Book-1 canon. Post-20 progression is deliberately unlocked: new abilities land every 2–3 levels, passives gain **II / III** tiers (Mastery lines), and capstones acquire upgrades at major bands — but specific abilities get designed and locked **per book, as the story reaches them** (see the [book-level pacing table](../system/xp.md#leveling-curve-k1k3)). Designing L21–99 now would only create canon debt.

- *(TODO: add unresolved items for Temporal Bard, and mirror them into `canon/status.md`.)*

## Ability Stat Blocks

> Blocks below cover the kit shown in prose through Ch 21; remaining abilities gain blocks as they enter the story. Costs assume the **Medium mana group** (L1 ≈ 17, L10 ≈ 80 — see [stat progression](../system/stat-progression.md)). Songs cost upkeep, not casts — a Bard's mana drains while the music plays.

#### Chrono Resonance
- **Type:** Passive · **Level:** 1 · **Targeting:** Self

**Rules**
- Songs interact with temporal threads directly; all songs **function without an instrument**.
- Visual: the bard plays an invisible harp, threads of golden-silver light materializing per note ([spell page](../magic/spells/chrono-resonance.md)).
- Rebekah's core identity ability since her guitar died at the Transition (Ch 13).

**Scaling:** temporal song potency rises with temporal spell skill (proficiency-style scaler, Ch 13).

#### Temporal Boost
- **Type:** Song · **Level:** 1 · **Cost:** 3 mana per 6s upkeep · **Duration:** Sustained + ~6s fade · **Targeting:** Listeners (allies)

**Rules**
- Allies act and move **+10% faster** — an advanced temporal reference frame that stacks "by increasing certainty, not speed" (Ch 16).
- The party calls it "the haste song" (Ch 13, her first instrument-less cast).

**Scaling:** +2% per temporal-skill tier; stacking depth grows with skill.

#### Rejuvenation
- **Type:** **Refrain** · **Level:** 2 · **Cost:** 20 mana (one-time) · **Duration:** 12 hours · **Targeting:** Listeners (everyone in audible range at performance)

**Rules**
- **Suspends the body's maintenance overhead.** Hunger, thirst, waste, fatigue-poisons, cycles — the whole biological billing department stops sending invoices. The body keeps running; it just stops *needing things* for the duration.
- Does **not** heal, restore HP or mana, cure status effects, or replace sleep. It removes the *chores* of having a body, not the body's actual condition. A starving person is still starving underneath — Rejuvenation only means they aren't spending the day thinking about it.
- Cannot be started in combat. Rebekah sings it at camp, usually while doing something else, usually badly.

**Scaling:** duration +6h per 5 levels; radius grows with charisma and skill.

> **Author-facing — this is a handwave, and it should stay invisible.**
>
> The effect is written deliberately broad and **must never be enumerated on-page.** Nobody says "and menstruation." The phrasing is *"the body stops billing you,"* and it covers everything — including everything not thought of yet. A spell with a specific list is a spell that keeps drawing attention to the list; the entire purpose here is that these problems leave the narrative and don't come back.
>
> Two consequences worth holding onto:
> - It means the story never has to stage a bathroom break, a ration count, or a period, in a genre that otherwise has to keep pretending those don't exist.
> - It never raises a question about [Selene's](../characters/party/selene.md) body, because it never distinguishes between bodies. The broad phrasing isn't squeamishness — it's the version that requires the narrative to have no position at all.
>
> Pair with **[Cleanse](../magic/spells/cleanse.md)** and the [holy auras](cleric-of-healing.md#cleric-aura), which handle the external half. Between them, hygiene and biology are closed subjects.

#### Dust Note
- **Type:** Song (damage) · **Level:** 1 · **Cost:** 5 mana per note · **Cooldown:** none · **Duration:** Instant · **Targeting:** Enemy

**Rules**
- A single plucked note inflicts a moment of accelerated decay: **4–8 damage**.
- Deliberately minimal — the least lethal self-defense option in the game. Named on-page Ch 18, used as a steady damage drip in her echo fight.

**Scaling:** +2 damage per 5 levels. It never becomes a nuke; that's the point.

#### Veiled
- **Type:** Passive · **Level:** 2 · **Cost:** none · **Targeting:** Party (while performing casually)

**Rules**
- Ambient music makes the party unremarkable: uninterested observers overlook them (−20% to notice checks) unless actively searching.
- Social stealth, not invisibility — broken by hostile intent, combat, or drawing direct attention. Shown Ch 9 (the party walks out of a gunfight).

**Scaling:** notice penalty deepens with charisma and skill.

#### Rewind Note
- **Type:** Utility · **Level:** 2 · **Cost:** 10 mana · **Cooldown:** 30s · **Duration:** Instant · **Targeting:** Self (own actions)

**Rules**
- Rolls back one of **her own** mistakes from the last ~2s: a just-spent cooldown returns, a mistimed note un-plays, a fumbled action resets as if never attempted.
- Self-scope only — this is the personal editing tool; rewinding *other people's* moments is [Da Capo's](#da-capo) job, two levels later.
- The do-over before the do-over. She uses it constantly and admits to it never.

**Scaling:** rewind window widens to ~3s at L10, ~4s at L20.

#### Dissonant Chord
- **Type:** Song · **Level:** 3 · **Cost:** 10 mana + 2 per 6s upkeep · **Duration:** Sustained · **Targeting:** Area (enemies in audible range)

**Rules**
- Enemies fall out of sync: **−10% attack and move speed**, minor confusion (skipped beats, stumbled openings).
- The "discordant trip-song" of Ch 14; named on-page Ch 18.

**Scaling:** slow deepens +2% per 5 levels.

#### Veil of Offbeats
- **Type:** Song · **Level:** 3 · **Cost:** 3 mana per 6s upkeep · **Duration:** Sustained + fade · **Targeting:** Listeners (allies)

**Rules**
- Allies blur across adjacent timelines: **+10% evasion**.
- Named on-page Ch 18; her half of the Ch 17 dual-song weave.

**Scaling:** +2% evasion per 5 levels.

#### Harmonic Memory
- **Type:** Passive · **Level:** 4 · **Targeting:** Self

**Rules**
- Maintain **one additional concurrent song** (base 1 → 2). This is the dual-song weaving shown Ch 17 (haste + evasion together), named on-page Ch 18.
- Song limit rises again with Polyphonic Casting (L11).

**Scaling:** upkeep efficiency of concurrent songs improves with skill.

#### Da Capo
- **Type:** Utility · **Level:** 4 · **Cost:** 15 mana per cast · **Cooldown:** 12s · **Duration:** Instant · **Targeting:** Single ally (not self)

**Rules**
- *"From the top."* A short sung phrase rewinds one ally's **mental state** by a few seconds: one recently applied **Mental debuff** (fear, confusion, anxiety effects) simply **never happened** from the target's perspective. One debuff per cast.
- **Cannot target herself.** She is the reference clock — she cannot step outside her own timeline to rewind it. When the enemy debuffs *her*, there is no counter.
- **Only rewinds seconds.** Long-standing conditions — [Broken](../lore/dungeons/spirit-dungeon/mobs.md), hours old — are far outside the window. Da Capo undoes *moments*, not states.
- Not encouragement and not healing: the target doesn't recover from the hit — the hit is **un-said**. The party calls it "the do-over."
- A Utility, not a Song: it never occupies a [Harmonic Memory](#harmonic-memory) slot, so using it doesn't cost the party a running buff.

**Scaling:** rewind window widens slightly with skill; cooldown shortens at higher tiers.

> **Design note — the cooldown is load-bearing.** 12s is deliberately longer than a fast-cycling debuffer's cadence (the [Store Manager's](../lore/dungeons/spirit-dungeon/boss.md) Black-Friday Reviews land every ~5s). Da Capo **triages**; it does not blanket. Shorten it and every mental-pressure encounter in the book collapses.

#### Accelerando
- **Type:** Song · **Level:** 5 · **Cost:** 4 mana per 6s upkeep · **Duration:** Sustained + fade · **Targeting:** Listeners (allies)

**Rules**
- Allies' attack and casting speed **ramp** — the musical term is the mechanic: +4% per 6s of continuous play, to a maximum of **+12%**. Dropping the song drops the ramp.
- Distinct from [Temporal Boost](#temporal-boost) (flat +10% act/move, instant): Boost is the sprint, Accelerando is the build. Late fights favor the ramp; openers favor the flat.

**Scaling:** cap +2% per 5 levels.

#### Time Slip
- **Type:** Utility · **Level:** 6 · **Cost:** 15 mana · **Cooldown:** 45s · **Duration:** Instant · **Targeting:** Self

**Rules**
- Rebekah **rejoins her own position from ~3s ago** — a sideways step through her recent timeline. Any single attack currently inbound on her present position misses: she was never there.
- Movement, not healing — damage already taken stays taken. It corrects *place*, not *state*.
- The escape she didn't have in the [Mirror Room](../lore/dungeons/spirit-dungeon/rooms.md); the class hands it to her one dungeon too late, which is the class being honest about how growth works.

**Scaling:** lookback window +1s per 5 levels.

#### Echo Verse
- **Type:** Song · **Level:** 7 · **Cost:** 5 mana per 6s upkeep · **Duration:** Sustained · **Targeting:** Self (modifies her other songs)

**Rules**
- While sustained, her **most recently started other song re-pulses its on-apply effect every 6s** — Dissonant Chord re-stumbles the room, Temporal Boost re-surges, a Refrain re-asserts.
- It occupies a [Harmonic Memory](#harmonic-memory) slot to amplify another: one voice spent making a second voice louder. The first song she has that is *about* her other songs.

**Scaling:** pulse interval tightens to 5s at L15.

#### Temporal Awareness
- **Type:** Passive · **Level:** 8 · **Targeting:** Self (60 ft)

**Rules**
- Rebekah feels things that are **not keeping proper time**: haste and slow effects, temporal magic, entities running out-of-sync with the local beat ([Echo Doubles](../lore/dungeons/spirit-dungeon/mobs.md#echo-double); a [Veilstepper](veilstepper-rogue.md) mid-step reads as a skipped bar).
- Directional and textural, not visual — she describes it as hearing a musician rush ahead of the orchestra.
- No range through heavy barriers; distance muffles.

**Scaling:** +10 ft per 5 levels; at L15+ she can estimate *how far* out of sync something is.

#### Lullaby of Pauses
- **Type:** Song · **Level:** 9 · **Cost:** 8 mana per 6s upkeep · **Duration:** Sustained · **Targeting:** Area (enemies in audible range)

**Rules**
- Enemies suffer **micro-stalls**: every 6s, a 0.5s hesitation — a skipped beat where nothing they do advances. Enemy cast times run **+0.5s** while the lullaby holds.
- Not a stun and never breaks on damage — it is the whole room being *slightly late*, forever, which compounds worse than it reads.

**Scaling:** stall +0.1s per 5 levels.

#### Chrono Shield
- **Type:** Song · **Level:** 10 · **Cost:** 10 mana per 6s upkeep · **Duration:** Sustained · **Targeting:** Listeners (allies)

**Rules**
- Incoming hits on allies are **partially deferred**: 80% lands now, 10% arrives 6 seconds later, 10% never arrives — time absorbs the impact.
- Net −10% damage and, more importantly, **spike-flattening**: the killing blow becomes two survivable ones. Her answer to burst damage, in the same design family as [Bulwark of Order](paladin-of-the-system.md#bulwark-of-order).

**Scaling:** deferred share +5% per 5 levels (the *never-arrives* share grows).

#### Polyphonic Casting
- **Type:** Passive · **Level:** 11 · **Targeting:** Self

**Rules**
- Maintain **one additional concurrent song** (2 → 3, with [Harmonic Memory](#harmonic-memory)).
- The support ceiling rises: Boost + Offbeats + one *choice* — the first level where her fights include a decision she didn't have to make before.

**Scaling:** —

#### Stolen Moment
- **Type:** Passive · **Level:** 12 · **Targeting:** Self

**Rules**
- After any action, **10% chance** to immediately gain a **second action** — a beat borrowed from the adjacent bar.
- Time keeps books: the borrowed beat is repaid — her next action after a steal starts **0.5s late**.
- The System's log calls it arbitrage. Rebekah calls it syncopation.

**Scaling:** +2% chance per 5 levels.

#### Dirge of Delay
- **Type:** Song · **Level:** 13 · **Cost:** 10 mana per 6s upkeep · **Duration:** Sustained · **Targeting:** Area (enemies in audible range)

**Rules**
- Enemy action economy runs thick: attack intervals and cast times **+15%**, ability cooldowns recover **+2s slower**.
- Stacks with [Lullaby of Pauses](#lullaby-of-pauses) — the lullaby skips their beats; the dirge stretches them. Together an enemy rotation simply comes apart.

**Scaling:** +3% further per 5 levels.

#### Refrain of Continuity
- **Type:** Song · **Level:** 14 · **Cost:** 8 mana per 6s upkeep · **Duration:** Sustained · **Targeting:** Listeners (allies)

**Rules**
- Beneficial effects on allies **age at half speed** while she plays — a 60s buff spends its duration at 30s/min. Buffs, HoTs, food effects, [Blessed](cleric-of-healing.md#bless): all of it, sustained instead of re-cast.
- The late-kit answer to the [Bless dilemma](../lore/dungeons/spirit-dungeon/boss.md#phase-3-manager-exposed) the party once faced with no answer: at L14, upkeep is *her* job, and casters cast.

**Scaling:** aging slows to 40% at L20.

#### Temporal Mastery I
- **Type:** Passive · **Level:** 15 · **Targeting:** Self

**Rules**
- Song radius **+50%**; songs hold coherence while she moves (no fade on repositioning); all song upkeep **−20%**.
- Not new music — a bigger hall.

**Scaling:** superseded by Temporal Mastery II (post-L20, future book).

#### Time Ripple
- **Type:** Song · **Level:** 16 · **Cost:** 12 mana per 6s upkeep · **Duration:** Sustained (+10s linger) · **Targeting:** Area

**Rules**
- Her debuff songs **soak into the ground**: for 10s after an enemy-affecting song passes over an area, enemies *arriving* in that area receive the effect on entry.
- She can pre-seed a battlefield — the reinforcements walk into a song that ended before they got there. Fighting the past, and losing.

**Scaling:** linger +5s per 5 levels.

#### Finale: Split Second
- **Type:** Song (opener) · **Level:** 17 · **Cost:** 40 mana (one-time) · **Cooldown:** 5 min · **Duration:** Instant · **Targeting:** Party

**Rules**
- Struck at the moment of engagement: the party **acts first** — every member resolves one full action before any enemy moves. The fight starts on beat two, and the enemy never heard beat one.
- Requires an actual engagement start; cannot be re-triggered mid-fight.

**Scaling:** cooldown −60s at L20.

#### Perfect Pitch
- **Type:** Passive · **Level:** 18 · **Targeting:** Self

**Rules**
- Her songs no longer require a **medium**. They function under Silence, underwater, in a windstorm, for deafened allies — the song was always temporal structure; sound was just the interface.
- Closes the class's one historic counter: silencing the bard stops working, permanently.
- *(Instrument-free casting is not this — that's L1 [Chrono Resonance](#chrono-resonance), hers since Ch 13.)*

**Scaling:** —

#### Grand Cadence
- **Type:** Song (crescendo) · **Level:** 19 · **Cost:** 60 mana (one-time) · **Cooldown:** 3 min · **Duration:** 10s + aftermath · **Targeting:** Listeners (allies)

**Rules**
- A 10-second crescendo in which [Temporal Boost](#temporal-boost), [Accelerando](#accelerando), and [Veil of Offbeats](#veil-of-offbeats) all peak simultaneously at **+50% of their normal effect**, regardless of slots.
- The bill: for 60s afterward those three songs are **spent** and cannot be sustained. The party's biggest ten seconds, purchased with its quietest minute.

**Scaling:** aftermath shortens to 45s at L20.

#### Time Unbound
- **Type:** Capstone · **Level:** 20 · **Cost:** 80 mana · **Cooldown:** once per day · **Duration:** 30s · **Targeting:** Self

**Rules**
- For 30 seconds, **time-based restrictions do not apply to her**: no cooldowns ([Da Capo](#da-capo) on every beat), no song limit, no ramp-up time — every song starts at full effect.
- Thirty seconds in which the party's support ceiling is simply *removed*. Then it ends, all at once, and the silence afterward is total: every song must be rebuilt from nothing.
- **Scaling:** none. This is what L20 *is*.

## UI Popups

> **Migration Note:** Add one "Help" popup per ability, matching the in-world system UI.

### Template
```text
[SYSTEM HELP] <Ability Name>
Type: <Spell/Skill/Song/Passive>
Cost: <...>
Cooldown: <...>
Duration: <...>
Targeting: <...>

<1–3 line in-world description>

Mechanics:
- <bullet>
- <bullet>
```

## Open Questions

- *(TODO: add unresolved items for Temporal Bard, and mirror them into `canon/status.md`.)*
