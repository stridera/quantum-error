---
canon: true
stability: locked
last_reviewed: 2026-08-24
---

# Quantum Sorceress

Using magic to control the world.

Sorceresses channel raw magical power through force of will. The Quantum Sorceress variant draws on principles of quantum mechanics—probability, superposition, and observation effects.

## Design Philosophy

- **Role**: Ranged DPS, area damage, battlefield control
- **Theme**: Emotional amplification, instability as power
- **Unique Mechanic**: Spells tagged as **Anchor** (stable), **Amplified** (scales with emotion), or **Breaking** (reality-altering)

## Instability System

| Tag | Behavior |
|-----|----------|
| **Anchor** | Stable, predictable, emotionally neutral |
| **Amplified** | Emotional load increases power but reduces control |
| **Breaking** | Reality-bending effects with environmental aftermath |

## Ability Progression (Levels 1-20)

| Level | Ability | Type | Tags | Effect |
|-------|---------|------|------|--------|
| 1 | Mana Sense | Passive | perception | Perceive ambient mana density, spell residue, and nearby casting pressure |
| 1 | Arcane Bolt | Spell | anchor | Launch a focused arcane projectile; reliable baseline damage |
| 2 | Spell Focus | Passive | control | Increased spell precision and reduced cast disruption |
| 3 | Mana Shield | Spell | anchor | Convert mana into a protective barrier |
| 3 | Minor Illusion | Spell | anchor | Create a small visual or auditory illusion. Scale increases with INT—at INT 20+, illusions can fill a corridor or replicate full environmental features (walls, terrain, signage). The illusion remains stable (anchor behavior): it's the canvas that grows, not the volatility. This is raw computational power expanding the spell's parameters, not emotional amplification. |
| 4 | Elemental Affinity | Passive | amplified | Emotions bias how magic expresses (fear→cold, rage→fire, focus→lightning) |
| 5 | Fireball | Spell | amplified | Explodes on impact, damaging enemies in an area |
| 6 | Channel Mana | Utility | anchor | Recover mana more efficiently when not actively casting |
| 6 | Fan of Flames | Spell | amplified | Short close-range cone of flame — the smaller, cheaper cousin of Flame Wave (L13). Shown Ch 14. |
| 7 | Frost Bind | Spell | anchor | Deal cold damage and apply slow or brief root |
| 7 | Veil Image | Spell | amplified | Project moving illusory doubles that confuse targeting |
| 8 | Entanglement | Spell | anchor | Link two enemies; a share of damage dealt to either mirrors to the other |
| 9 | Observer Effect | Passive | anchor | Once per cooldown, observe a resolving random outcome — it re-collapses, and the second result stands |
| 10 | Lightning Lance | Spell | amplified | Piercing bolt that excels against armored targets |
| 10 | Displacement | Spell | amplified | Persistent misalignment between where you are and appear |
| 11 | Mana Surge | Utility | amplified | Immediate mana gain; increases escalation risk |
| 12 | Spell Weaving | Passive | anchor | Chaining spells reduces cast time and improves flow |
| 13 | Flame Wave | Spell | amplified | Sweeping cone of flame hitting multiple enemies |
| 14 | Arcane Ward | Spell | anchor | Reactive ward that reduces incoming magical harm |
| 14 | Mirror Phantasm | Spell | amplified | Multiple illusionary selves fracturing enemy targeting |
| 15 | Elemental Mastery I | Passive | amplified | Elemental spells gain secondary effects based on emotional state |
| 16 | Void Pulse | Spell | breaking | Disruptive pulse that destabilizes casting and compresses space |
| 17 | Mana Burn | Spell | breaking | Tears at mana; drains reserves and harms through power |
| 18 | Arcane Instinct | Passive | anchor | When critically threatened, magic reacts first (ward flare, reflexive displacement) |
| 19 | Spell Cascade | Passive | amplified | Area spells expand or chain when emotional load is high |
| 20 | **Cataclysm** | Capstone | breaking | Reality-bending devastation; this is an event, not just damage |

## Mana Lucent

A concept specific to Vanessa: after her Mana Shock, her eyes and veins glow softly with mana. The glow shifts toward the elemental color of whatever spell she is casting.

## Notable Quantum Sorceresses

- [Vanessa](../characters/party/vanessa.md)

## Beyond Level 20

Levels 1–20 above are Book-1 canon. Post-20 progression is deliberately unlocked: new abilities land every 2–3 levels, passives gain **II / III** tiers (Mastery lines), and capstones acquire upgrades at major bands — but specific abilities get designed and locked **per book, as the story reaches them** (see the [book-level pacing table](../system/xp.md#leveling-curve-k1k3)). Designing L21–99 now would only create canon debt.

- *(TODO: add unresolved items for Quantum Sorceress, and mirror them into `canon/status.md`.)*

## Ability Stat Blocks

> Full kit, in level order. Costs assume the **High mana group** (L1 ≈ 20, L10 ≈ 110 — see [stat progression](../system/stat-progression.md)); Vanessa's 9,999 pool + Mana Lucent (spells act two levels higher) makes her wildly over-spec.

#### Mana Sense
- **Type:** Passive (perception) · **Level:** 1 · **Targeting:** Self (60 ft)

**Rules**
- Perceives **ambient mana density** (rich, thin, null), **spell residue** (what was cast here, legible for hours), and **casting pressure** — someone winding up a spell nearby registers before it fires.
- The caster's early-warning system, and the reason a sorceress is never surprised by magic — only by everything else.

**Scaling:** +20 ft per 5 levels; residue legibility sharpens (by L10 she can name the school; by L20, nearly the spell).

#### Arcane Bolt
- **Type:** Spell (anchor) · **Level:** 1 · **Cost:** 8 mana · **Cooldown:** none · **Duration:** Instant (1s cast) · **Targeting:** Enemy (60 ft)

**Rules**
- Focused arcane projectile: **12–18 damage**, reliable, emotionally inert. The baseline she can always fall back to.
- **Naming note:** prose (Ch 18, her echo fight) calls this **Magic Missile** — same spell, player nickname. Treat Magic Missile ≡ Arcane Bolt.

**Scaling:** +4 to both ends per 5 levels.

#### Spell Focus
- **Type:** Passive (control) · **Level:** 2 · **Targeting:** Self

**Rules**
- **25% chance** that taking a hit mid-cast does **not** interrupt the cast ([casting under fire](../system/combat.md#interrupts-and-control)); spell placement precision improves (drift on thrown/area spells roughly halved).
- Mitigation, not immunity — under sustained melee she still locks up, as the [Manager's relay beat](../lore/dungeons/spirit-dungeon/boss.md#prose-beats--from-the-double-kill-author-facing) shows.

**Scaling:** +5% interrupt resistance per 5 levels.

#### Mana Shield
- **Type:** Spell (anchor) · **Level:** 3 · **Cost:** 20 mana · **Cooldown:** 10s after break · **Duration:** Until broken or dismissed · **Targeting:** Self

**Rules**
- Converts mana into a barrier absorbing **60 damage** at base.
- While the shield holds, no HP damage is taken; overflow damage passes through on break.
- Console-raised to spell level 10 ("Mastered") for Vanessa in Ch 7 — her version absorbs ~240.

**Scaling:** +20 absorption per spell level.

#### Minor Illusion
- **Type:** Spell (anchor) · **Level:** 3 · **Cost:** 10–30 mana by scale · **Duration:** Sustained (light concentration) · **Targeting:** Area

**Rules**
- Creates a stable visual or auditory illusion. Base canvas: object or sound up to person-size.
- Scale grows with INT — at INT 20+, illusions can fill a corridor or replicate full environmental features (fake detour signs, fallen trees, a driver's face — Ch 11).
- Anchor behavior: the canvas grows, not the volatility. Computational power, not emotional amplification.

**Scaling:** canvas size with INT; fidelity with spell level.

#### Elemental Affinity
- **Type:** Passive (amplified) · **Level:** 4 · **Targeting:** Self

**Rules**
- Emotion biases elemental expression: **fear→cold, rage→fire, focus→lightning.** Casting the element that matches her current state: **+10% effect.** Casting against her own weather: **+10% mana cost.**
- This is the amplified tag's foundation — her power is honest about her state whether she is or not, which makes her spell choices a mood ring the party learns to read.

**Scaling:** matched-element bonus +2% per 5 levels.

#### Fireball
- **Type:** Spell (amplified) · **Level:** 5 · **Cost:** 30 mana · **Cooldown:** 6s · **Duration:** Instant · **Targeting:** Area (20 ft blast, thrown)

**Rules**
- 30–50 fire damage in the blast, 25% chance to ignite (1d4 burn, 2 rounds).
- **Amplified:** under high emotional load, damage rises up to +50% and the blast radius grows — with matching loss of placement control. Vanessa has dropped one on her own tank (Ch 20, deliberately).
- Full version distinct from Fan of Flames (Ch 15).

**Scaling:** +10 damage per 5 levels; Mana Lucent casts act two levels higher.

#### Fan of Flames
- **Type:** Spell (amplified) · **Level:** 6 · **Cost:** 20 mana · **Cooldown:** 4s · **Duration:** Instant · **Targeting:** Area (15 ft cone)

**Rules**
- 18–30 fire damage in a close cone — the smaller, cheaper cousin of Flame Wave (L13).
- Amplified: emotional load widens the cone before it deepens the damage.
- Shown Ch 14 (post-Transition coyote fights).

**Scaling:** +6 damage per 5 levels.

#### Channel Mana
- **Type:** Utility (anchor) · **Level:** 6 · **Cost:** none · **Duration:** Sustained stillness · **Targeting:** Self

**Rules**
- After 3s without casting, mana regeneration runs at **×3** until she casts or takes damage.
- Doing nothing, weaponized. The discipline is the cost — the fight rarely lets her have three quiet seconds.

**Scaling:** ×4 at L15.

#### Frost Bind
- **Type:** Spell (anchor) · **Level:** 7 · **Cost:** 25 mana · **Cooldown:** 8s · **Duration:** Instant (effects 4s) · **Targeting:** Enemy (40 ft)

**Rules**
- **20–30 cold damage + 30% slow** for 4s; against an already-slowed target, a **1s root** instead.
- Anchor: single-target, no blast, no drift — the control spell that **cannot hit a friend**, which is exactly why it exists in this kit and why she reaches for it when her hands aren't steady.

**Scaling:** +6 to both ends per 5 levels.

#### Veil Image
- **Type:** Spell (amplified) · **Level:** 7 · **Cost:** 30 mana · **Cooldown:** 30s · **Duration:** 20s · **Targeting:** Self

**Rules**
- Two moving illusory doubles; enemies have a **30% chance to mistarget** among the set. Doubles pop on any hit.
- **Amplified:** high emotional load adds a third double — but loaded doubles mimic her *feelings*, not her plan. They flinch when she flinches. A perceptive enemy reads the real her off the copies.

**Scaling:** +1 double at L15.

#### Entanglement
- **Type:** Spell (anchor) · **Level:** 8 · **Cost:** 30 mana · **Cooldown:** 20s · **Duration:** 10s · **Targeting:** Two enemies within 30 ft of each other

**Rules**
- Links two enemies at the quantum level: **30% of damage dealt to either is mirrored to the other.** The mirrored share is *her* damage — threat and kill credit route to her.
- **Anchor on purpose:** the link is precise, single-pair, and **cannot touch allies** — like [Frost Bind](#frost-bind), a spell she can cast with unsteady hands. Mid-book Vanessa is learning control; her new tools should show it.
- Breaks early if the pair moves more than 60 ft apart. Flavor: the particles never forgave each other.

**Scaling:** mirrored share +5% per 5 levels.

#### Observer Effect
- **Type:** Passive (anchor) · **Level:** 9 · **Cooldown:** 30s (internal) · **Targeting:** Self (30 ft, witnessed events)

**Rules**
- Once per cooldown, when a **random outcome resolves in her sight** — a crit roll, a save, a miss chance affecting her or an ally within 30 ft — she may *observe* it: the outcome **re-collapses (rerolled), and the second result stands.**
- The quantum joke made mechanical: measured systems behave differently. She doesn't change what happened — she was simply watching more carefully than reality expected.
- **Not time magic.** [Rebekah](temporal-bard.md) rewinds what already happened; Vanessa collapses what hasn't finished resolving. Post-hoc versus pre-resolution — the two schools coexist without touching.

**Scaling:** cooldown −5s per 5 levels.

#### Lightning Lance
- **Type:** Spell (amplified) · **Level:** 10 · **Cost:** 35 mana · **Cooldown:** 10s · **Duration:** Instant (1.5s cast) · **Targeting:** Line (80 ft)

**Rules**
- Piercing bolt down a full 80 ft line: **40–60 lightning, ignores 50% of armor**, hits *everything* in the line.
- Everything. The lance does not curve and does not care who is standing in the corridor — the kit's sharpest expression of her friendly-fire problem, and the spell her [Metamagic ally-exclusion work](../magic/schools/metamagic.md) most wants to fix.

**Scaling:** +10 to both ends per 5 levels.

#### Displacement
- **Type:** Spell (amplified) · **Level:** 10 · **Cost:** 30 mana · **Cooldown:** none · **Duration:** 60s · **Targeting:** Self

**Rules**
- She is persistently **~3 ft from where she appears**: attacks against her suffer **−15% accuracy**.
- A melee swing that misses *because of the offset* reveals her true position for 1s — the trick spends itself on use.
- **Amplified:** under load the offset wanders, which is better (unpredictable) and worse (she has clipped doorframes).

**Scaling:** −3% further accuracy per 5 levels.

#### Mana Surge
- **Type:** Utility (amplified) · **Level:** 11 · **Cost:** none · **Cooldown:** 60s · **Duration:** Instant · **Targeting:** Self

**Rules**
- Instantly recover **30% of max mana**, torn out of ambient rather than channeled.
- The bill: her next amplified spell within 10s **auto-amplifies** — full power, reduced control, whether she wanted it or not. Emergency mana is emotionally expensive by definition; the tag system knows.

**Scaling:** +5% recovery per 5 levels.

#### Spell Weaving
- **Type:** Passive (anchor) · **Level:** 12 · **Targeting:** Self

**Rules**
- Casting spells back-to-back (≤2s between casts) reduces each subsequent cast time by **10%, stacking to 30%.** Broken by pausing or being interrupted.
- Flow state, mechanized: a sorceress mid-weave is visibly *conducting*, and the party learns not to talk to her.

**Scaling:** cap 40% at L20.

#### Flame Wave
- **Type:** Spell (amplified) · **Level:** 13 · **Cost:** 45 mana · **Cooldown:** 12s · **Duration:** Instant · **Targeting:** Area (30 ft cone)

**Rules**
- Sweeping sheet of fire: **50–70 damage** across the cone, 50% ignite (1d4 burn, 2 rounds). The grown-up [Fan of Flames](#fan-of-flames).
- **Amplified:** load widens the cone first, then deepens the damage — anger makes it *bigger* before it makes it worse, which is not the order anyone would choose.

**Scaling:** +10 to both ends per 5 levels.

#### Arcane Ward
- **Type:** Spell (anchor) · **Level:** 14 · **Cost:** 30 mana · **Cooldown:** none · **Duration:** 10 min · **Targeting:** Self or Ally

**Rules**
- Standing ward vs magic: **−30% magical damage taken**; the first magical hit in any 30s window is reduced **−60%** instead.
- Castable on allies — her first true protection spell, fourteen levels in. The kit admits, late, that other people exist.

**Scaling:** −5% further per 5 levels.

#### Mirror Phantasm
- **Type:** Spell (amplified) · **Level:** 14 · **Cost:** 45 mana · **Cooldown:** 45s · **Duration:** 15s · **Targeting:** Self

**Rules**
- **Four phantasm selves** acting independently — walking, gesturing, visibly "casting" (visual-only). Enemies must actively check to find the real her each time they target.
- **Amplified:** under high load the phantasms *diverge* — one of them starts doing what she **wants** to do rather than what she's doing. The party has learned to watch for the copy that's angrier than she's letting herself be.

**Scaling:** +1 phantasm at L20.

#### Elemental Mastery I
- **Type:** Passive (amplified) · **Level:** 15 · **Targeting:** Self

**Rules**
- Elemental spells gain a secondary effect keyed to her current state: **cold → Brittle** (target +10% damage taken, 4s) · **fire → spreading ignite** (burn jumps to an adjacent enemy) · **lightning → stagger** (0.5s).
- With [Elemental Affinity](#elemental-affinity), her emotional state now chooses both the element *and* its consequence. Reading Vanessa mid-fight is reading the battlefield's next ten seconds.

**Scaling:** superseded by Elemental Mastery II (post-L20, future book).

#### Void Pulse
- **Type:** Spell (breaking) · **Level:** 16 · **Cost:** 60 mana · **Cooldown:** 60s · **Duration:** Instant (+aftermath) · **Targeting:** Area (20 ft radius, 60 ft range)

**Rules**
- A pulse of compressed nothing: **40 void damage**, every enemy cast in the radius **interrupted**, and space itself contracts — everything in the zone is dragged **5 ft inward** toward the center.
- **Breaking aftermath:** the zone stays *wrong* for ~60s — dim, flat-sounding, mana-thin. Breaking spells leave marks on the world; that's what the tag means.

**Scaling:** +10 damage and +5 ft radius per 5 levels.

#### Mana Burn
- **Type:** Spell (breaking) · **Level:** 17 · **Cost:** 50 mana · **Cooldown:** 30s · **Duration:** Instant · **Targeting:** Enemy (40 ft)

**Rules**
- Tears at the target's reserves: destroys up to **100 mana**; the target takes **1 damage per 2 mana burned**. Manaless targets are untouched — this is an anti-caster scalpel, not a nuke.
- **Breaking aftermath:** burned mana doesn't disperse — it's *gone*, leaving a cold spot in the ambient field that [Mana Sense](#mana-sense) reads like a scar.

**Scaling:** +25 mana burned per 5 levels.

#### Arcane Instinct
- **Type:** Passive (anchor) · **Level:** 18 · **Cooldown:** 60s (internal) · **Targeting:** Self

**Rules**
- When a hit would drop her below **30% max HP**, her magic reacts **before she does**: an automatic [Mana Shield](#mana-shield) (if ≥20 mana) or a reflexive 10 ft displacement — no cast, no action, no decision.
- Anchor-tagged on purpose: the reflex is the *calmest* magic she has, which she finds insulting.

**Scaling:** trigger threshold rises to 35% at L20.

#### Spell Cascade
- **Type:** Passive (amplified) · **Level:** 19 · **Targeting:** —

**Rules**
- At high emotional load, area spells **chain**: 30% chance the AoE re-casts itself at 50% power centered on the nearest untouched enemy cluster. A chained cast can chain again (15%, then done).
- The cascade inherits her amplification and **does not distinguish zones a friend is standing in** — her friendly-fire arc, scaled up to its endgame stakes. The only leash is her [Metamagic](../magic/schools/metamagic.md) exclusion work; the class itself will not save anyone.

**Scaling:** —

#### Cataclysm
- **Type:** Capstone (breaking) · **Level:** 20 · **Cost:** all remaining mana (min 150) · **Cooldown:** once per day · **Duration:** 10s channel · **Targeting:** Area (60 ft zone)

**Rules**
- Reality-bending devastation: **200 damage across the zone, +1 per 10 mana spent above the minimum.** Terrain is permanently altered — glassed ground, wrong-angled light, an ambient mana scar that reads for days. The System logs it the way it logs weather.
- This is an **event, not a rotation**: a 10s channel, a once-a-day bill, and consequences the party has to walk through afterward.
- **Author note:** with Vanessa's 9,999 pool the mana-scaled term is apocalyptic — a full-pool Cataclysm is a *city-block decision*, and writing one is a book decision, not a combat beat. The number is the temptation; the aftermath is the theme.
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

- *(TODO: add unresolved items for Quantum Sorceress, and mirror them into `canon/status.md`.)*
