---
canon: true
stability: locked
last_reviewed: 2026-08-24
---

# Veilstepper Rogue

Sneaky sneaky.

Rogues specialize in stealth, precision strikes, and exploiting enemy weaknesses. The Veilstepper variant focuses on moving between shadows and dimensions—**phase**, not illusion.

## Design Philosophy

- **Role**: Single-target burst DPS, assassination, isolation
- **Theme**: Phase manipulation, existing between states
- **Unique Mechanic**: Veil—not invisibility, but existing loosely in the present layer

## Core Distinction

| Concept | Description |
|---------|-------------|
| **Stealth** | Conventional hiding; broken by observation |
| **Veil** | Phase state; you are not fully here |
| **Illusion** | False images ([Sorceress](quantum-sorceress.md) domain) |
| **Phase** | Existing across adjacent reality layers |

## Ability Progression (Levels 1-20)

| Level | Ability | Type | Effect |
|-------|---------|------|--------|
| 1 | [Sneak](#sneak) | [Toggle](../system/combat.md#ability-type-vocabulary) | Enter stealth when unobserved; quieter movement |
| 1 | [Backstab](#backstab) | [Attack](../system/combat.md#ability-type-vocabulary) | Increased damage from behind or while Veiled |
| 2 | [Nekara Agility](#nekara-agility) | [Racial Passive](../system/combat.md#ability-type-vocabulary) | Increased evasion, balance, and movement speed |
| 3 | [Veil Sense](#veil-sense) | [Passive](../system/combat.md#ability-type-vocabulary) | Detect things partially absent from the present layer — veiled or phased entities, concealed hazards, and dormant mechanisms (traps read as "waiting" objects). How Selene spotted the L10 Bear Trap (Ch 16). |
| 4 | [Shadowstep](#shadowstep) | [Utility](../system/combat.md#ability-type-vocabulary) | Short-range reposition between nearby shadows |
| 5 | [Bleeding Strike](#bleeding-strike) | [Attack](../system/combat.md#ability-type-vocabulary) | Apply bleeding wound (damage over time) |
| 6 | [Sidestep Between Selves](#sidestep-between-selves) | [Passive](../system/combat.md#ability-type-vocabulary) | Flicker between possible states, causing attacks to miss |
| 7 | [Smoke Veil](#smoke-veil) | [Utility](../system/combat.md#ability-type-vocabulary) | Create visual disruption that breaks observation and allows Veil re-entry |
| 8 | [Chosen Shadow](#chosen-shadow) | [Passive](../system/combat.md#ability-type-vocabulary) | Gain bonuses while unobserved or Veiled |
| 9 | [Weak Point Analysis](#weak-point-analysis) | [Passive](../system/combat.md#ability-type-vocabulary) | Crit chance increases with undetected observation time |
| 10 | [Shadow Ambush](#shadow-ambush) | [Attack](../system/combat.md#ability-type-vocabulary) | Reposition and strike simultaneously; powerful opener |
| 11 | [Evasion Roll](#evasion-roll) | [Reaction](../system/combat.md#ability-type-vocabulary) | Avoid a lethal hit once per cooldown |
| 12 | [Phase Cut](#phase-cut) | [Attack](../system/combat.md#ability-type-vocabulary) | Strike along phase alignment, bypassing armor |
| 13 | [Veil Mastery I](#veil-mastery-i) | [Passive](../system/combat.md#ability-type-vocabulary) | Veil lasts longer and is harder to detect |
| 14 | [Silence](#silence) | [Utility](../system/combat.md#ability-type-vocabulary) | Prevent spellcasting and vocal abilities in small area |
| 15 | [Double Image](#double-image) | [Defensive](../system/combat.md#ability-type-vocabulary) | Leave brief afterimage when attacking or repositioning |
| 16 | [Umbral Dance](#umbral-dance) | [Buff](../system/combat.md#ability-type-vocabulary) | Increased movement speed and crit chance |
| 17 | [Shadow Reversal](#shadow-reversal) | [Reaction](../system/combat.md#ability-type-vocabulary) | Swap position with attacker at moment of impact |
| 18 | [Ghost Strike](#ghost-strike) | [Attack](../system/combat.md#ability-type-vocabulary) | Damages targets in present layer and adjacent phase layers |
| 19 | [Perfect Predator](#perfect-predator) | [Passive](../system/combat.md#ability-type-vocabulary) | Massive bonuses when attacking isolated targets |
| 20 | **[Veil Ascension](#veil-ascension)** | [Capstone](../system/combat.md#ability-type-vocabulary) | Near-total control over phase state; only loosely anchored to present |

## Key Mechanics

### Veil State
- Not invisibility—phase displacement
- Broken by direct observation or interaction
- Enhanced by isolation and shadows
- **Entry (codified):** from **L7**, [Sneak](#sneak) initiated while unobserved deepens into true Veil — the same toggle, a deeper state. [Smoke Veil](#smoke-veil) (L7) is the mid-combat re-entry; before L7, "while Veiled" bonuses are simply unreachable.

### Phase Attacks
- Phase Cut ignores armor
- Ghost Strike hits across phase layers
- Effective against unstable or phased entities

## Notable Veilstepper Rogues

- [Selene](../characters/party/selene.md)

## Beyond Level 20

Levels 1–20 above are Book-1 canon. Post-20 progression is deliberately unlocked: new abilities land every 2–3 levels, passives gain **II / III** tiers (Mastery lines), and capstones acquire upgrades at major bands — but specific abilities get designed and locked **per book, as the story reaches them** (see the [book-level pacing table](../system/xp.md#leveling-curve-k1k3)). Designing L21–99 now would only create canon debt.

- *(TODO: add unresolved items for Veilstepper Rogue, and mirror them into `canon/status.md`.)*

## Ability Stat Blocks

> Full kit, in level order. The Rogue kit runs on stamina, not mana (Low mana group — see [stat progression](../system/stat-progression.md)).
>
> In-prose Help popups are rendered from these blocks **on demand**, using the System-wide shape in [UI Popups §3](../system/ui-popups.md#3-ability--unlock--help) — they are not pre-authored here. The stat block is the source of truth; a popup is a rendering of one.

#### Sneak
- **Type:** Toggle · **Level:** 1 · **Cost:** 1 stamina/s while moving stealthed · **Duration:** Until broken · **Targeting:** Self

**Rules**
- Enter stealth when unobserved; movement is quieter and slower.
- Broken by direct observation, attacking (see Backstab), or loud interaction.
- Pierced for the first time in Ch 20 — the Scarecrow of the Fallow Row sees through it.

**Scaling:** stealth strength rises with skill and DEX; Veil (L7+) supersedes it situationally.

#### Backstab
- **Type:** Attack · **Level:** 1 · **Cost:** 15 stamina · **Cooldown:** 6s · **Targeting:** Enemy (melee)

**Rules**
- Melee strike for **×2 weapon damage** when delivered from behind or while Veiled; +10% crit chance.
- Breaks stealth on use. First shown Ch 7 ("Backstabbed!").

**Scaling:** multiplier ×2.5 at L10, ×3 at L20; synergizes with Weak Point Analysis (L9).

#### Nekara Agility
- **Type:** Racial Passive · **Level:** — (race, [Nekara](../races/nekara.md)) · **Targeting:** Self

**Rules**
- **+10% evasion, +10% movement speed**, and near-perfect balance (falls, ledges, landings).
- Racial, not class — stacks with all class abilities.

**Scaling:** fixed; racial traits don't scale with class level.

#### Veil Sense
- **Type:** Passive · **Level:** 3 · **Targeting:** Self (30 ft)

**Rules**
- Passive detection of things **partially absent from the present layer**: veiled or phased entities, concealed hazards, and dormant mechanisms — traps read as "waiting" objects.
- How Selene spotted the L10 Bear Trap (Ch 16) as the only party member to notice it.

**Scaling:** range +10 ft per 5 levels; at high skill, gives a beat of warning before an ambush triggers.

#### Shadowstep
- **Type:** Utility · **Level:** 4 · **Cost:** 20 stamina · **Cooldown:** 15s · **Duration:** Instant · **Targeting:** Self (20 ft)

**Rules**
- Instant reposition to any shadow or hard cover within 20 ft that she can see. No travel time — she is simply there.
- Does **not** break stealth or Veil. The repositioning tool the rest of the kit is built around.

**Scaling:** +5 ft per 5 levels.

#### Bleeding Strike
- **Type:** Attack · **Level:** 5 · **Cost:** 15 stamina · **Cooldown:** 10s · **Duration:** Bleed 10s · **Targeting:** Enemy (melee)

**Rules**
- Weapon hit + **Bleeding**: 8 damage per 2s for 10s (40 total). Stacks twice.
- **Requires blood.** Skeletons, constructs, mannequins: immune — the Spirit Dungeon was a bad venue for this spell, which is why it barely appears in Book 1's midsection.

**Scaling:** bleed +2 per tick per 5 levels.

#### Sidestep Between Selves
- **Type:** Passive · **Level:** 6 · **Targeting:** Self

**Rules**
- **10% of attacks against her miss outright** — the Selene that was struck turns out to be a Selene that wasn't chosen. Checked before evasion; stacks with it additively in effect.
- Visual: a flicker, like a frame dropped from her.

**Scaling:** +2% per 5 levels.

#### Smoke Veil
- **Type:** Utility · **Level:** 7 · **Cost:** 25 stamina · **Cooldown:** 45s · **Duration:** Smoke 4s · **Targeting:** Area (10 ft burst, self-centered)

**Rules**
- A burst of gray nothing — not smoke exactly; the *absence of looking*. Breaks all observation on her for its duration.
- While inside it she may **re-enter Veil mid-combat** — the only combat re-entry in the kit before L20.
- Enemies inside suffer −5 accuracy against everyone, not just her.

**Scaling:** cooldown −5s per 5 levels.

#### Chosen Shadow
- **Type:** Passive · **Level:** 8 · **Targeting:** Self

**Rules**
- While unobserved or Veiled: **+15% damage, +10% movement speed, stamina regeneration +50%.**
- The class states its thesis: she is more real when nobody is looking.

**Scaling:** damage +3% per 5 levels.

#### Weak Point Analysis
- **Type:** Passive · **Level:** 9 · **Targeting:** Enemy (observed)

**Rules**
- While undetected and watching a target: **+5% crit chance per 2s of observation, max +25%.** The stored crit is consumed by her next attack on that target.
- *Undetected* means not pinpointed — enemies made Alert by, say, [inexplicable spy music](../items/accessories/agents-clip-on-bow-tie.md) still count, as long as they can't place her.

**Scaling:** cap +5% per 5 levels.

#### Shadow Ambush
- **Type:** Attack · **Level:** 10 · **Cost:** 30 stamina · **Cooldown:** 30s · **Duration:** Instant · **Targeting:** Enemy (30 ft)

**Rules**
- [Shadowstep](#shadowstep) and [Backstab](#backstab) fused into one motion: reposition to the target from up to 30 ft and strike at **×2.5 weapon damage** in the same beat.
- If the strike **kills**, half the stamina refunds and the Veil does **not** break — the assassination chain the class has been promising since L1.

**Scaling:** multiplier ×3 at L15.

#### Evasion Roll
- **Type:** Reaction · **Level:** 11 · **Cost:** 25 stamina · **Cooldown:** 60s · **Duration:** Instant · **Targeting:** Self

**Rules**
- Fully avoid one incoming attack she can see coming (declared during telegraph or travel), rolling 10 ft to a position of her choice.
- The panic button — and unlike [Sidestep](#sidestep-between-selves), it's a *choice*, which is why it costs.

**Scaling:** cooldown −10s at L15 and L20.

#### Phase Cut
- **Type:** Attack · **Level:** 12 · **Cost:** 30 stamina · **Cooldown:** 20s · **Duration:** Instant · **Targeting:** Enemy (melee)

**Rules**
- The blade travels along phase alignment instead of through matter: **armor does not apply (AR = 0)**, ×1.5 weapon damage.
- **+50% vs phased or unstable entities** — things not fully committed to the present get cut in *both* places.

**Scaling:** +25% base damage at L20.

#### Veil Mastery I
- **Type:** Passive · **Level:** 13 · **Targeting:** Self

**Rules**
- Veil duration **+50%**; detection checks against her Veil at **−5**; Veiled movement is no longer slowed.
- The state stops being a resource and starts being a home.

**Scaling:** superseded by Veil Mastery II (post-L20, future book).

#### Silence
- **Type:** Utility · **Level:** 14 · **Cost:** 30 stamina · **Cooldown:** 45s · **Duration:** 4s · **Targeting:** Area (10 ft)

**Rules**
- A dome of no-sound: **spellcasting with verbal components and vocal abilities fail** inside for 4s.
- Cuts incantation-casters and shouted commands; does nothing to instant or purely somatic abilities. (An L18+ [Temporal Bard's](temporal-bard.md#perfect-pitch) music transcends the medium and plays straight through it — the counter has a counter.)

**Scaling:** +2s duration at L20.

#### Double Image
- **Type:** Defensive Passive · **Level:** 15 · **Cooldown:** 10s (internal) · **Targeting:** Self

**Rules**
- Attacking or repositioning leaves a **1s afterimage**; the first attack aimed at her in that window strikes the image instead.
- The image is a *was* — a Selene one second stale. Enemies learn to aim ahead of her, and mostly fail.

**Scaling:** afterimage lingers 1.5s at L20.

#### Umbral Dance
- **Type:** Buff · **Level:** 16 · **Cost:** 30 stamina · **Cooldown:** 60s · **Duration:** 10s (extendable) · **Targeting:** Self

**Rules**
- **+25% movement speed, +15% crit chance** for 10s; every attack that misses her during it extends the dance by 1s.
- Aggression pays for itself: the harder they swing at her, the longer she stays fast.

**Scaling:** crit +5% at L20.

#### Shadow Reversal
- **Type:** Reaction · **Level:** 17 · **Cost:** 35 stamina · **Cooldown:** 90s · **Duration:** Instant · **Targeting:** Attacker (melee range)

**Rules**
- At the moment of impact, she **swaps positions with her attacker**: the blow lands where she stood — on whatever now occupies that space — and she is behind them, [Backstab](#backstab) primed.
- The single nastiest trick in the kit: an enemy formation that strikes at her is donating a flank.

**Scaling:** cooldown −15s at L20.

#### Ghost Strike
- **Type:** Attack · **Level:** 18 · **Cost:** 40 stamina · **Cooldown:** 30s · **Duration:** Instant · **Targeting:** Enemy (melee)

**Rules**
- The strike lands in the present **and every adjacent phase layer at once**: phase defenses, Veil states, and ethereality do not mitigate it.
- **×2 damage vs entities not fully present** — the anti-mirror, anti-phased, anti-*things-like-her* weapon. Veilsteppers are the natural predators of other Veilsteppers.

**Scaling:** +25% at L20.

#### Perfect Predator
- **Type:** Passive · **Level:** 19 · **Targeting:** Enemy (isolated)

**Rules**
- Against an **isolated target** — no ally of theirs within 30 ft — she deals **+30% damage** with **+15% crit chance**.
- The kit converges: Shadowstep separates, Silence isolates the caster from help, and Perfect Predator is the reason. The class endgame is not fighting armies; it is making sure, briefly, that there is no army.

**Scaling:** —

#### Veil Ascension
- **Type:** Capstone · **Level:** 20 · **Cost:** 50 stamina · **Cooldown:** once per day · **Duration:** 60s · **Targeting:** Self

**Rules**
- For one minute she is **only loosely anchored to the present**: enter and exit Veil at will, instantly, no cover required; attacks no longer break the Veil (each attack *thins* it — −10s duration per strike).
- She can slip through barriers up to ~1 ft thick (doors, walls of the ordinary kind) — the world's solidity becomes a suggestion.
- Fully stepped-out, she cannot act except to move, and non-phase attacks cannot target her. ([Ghost Strike](#ghost-strike)-class abilities still can. Everything has a predator.)
- **Scaling:** none. This is what L20 *is*.

## Open Questions

- *(TODO: add unresolved items for Veilstepper Rogue, and mirror them into `canon/status.md`.)*
