---
canon: true
stability: locked
last_reviewed: 2026-08-24
---

# Cleric of Healing

Healers that channel divine power to heal and combat the undead.

A traditional cleric focused on restoration and support. Unlike the [Paladin of the System](paladin-of-the-system.md), the Cleric of Healing has no special system ties—purely divine magic channeled through faith.

## Design Philosophy

- **Role**: Primary healer, party sustain, anti-undead
- **Theme**: Steady, reliable, with subtle trauma cues
- **Unique Mechanic**: Emotional limiter—spells always work, but exact a personal cost

## Emotional Limiter

Wade's class includes an emotional limiter mechanic:
- Healing spells **always function as intended**
- Strong emotions may surface after casting
- Trauma cues are informational; they do not alter spell reliability
- The cost is psychological, not mechanical

## Ability Progression (Levels 1-20)

| Level | Ability | Type | Effect |
|-------|---------|------|--------|
| 1 | Cure Light Wounds | Spell | Restore modest health to a living target |
| 1 | Holy Light | Spell | Conjure steadfast divine light; undead and corrupted entities flinch from its radius. Granted to all holy classes. |
| 1 | Turn Undead | Spell | Repels, weakens, or damages undead creatures |
| 2 | Bless | Spell | Allies gain improved accuracy, resolve, and fear resistance (applies the **Blessed** status) |
| 3 | Cleric Aura | Aura | Passive calm radius — nearby allies gain minor fear resistance and +5% healing received |
| 3 | Cure Poison | Spell | Removes poison effects from a target |
| 4 | Lesser Restoration | Spell | Removes minor **physical** afflictions — poison, paralysis, breathing. No mental effects; divine magic fixes bodies, not confidence |
| 5 | Prayer of Healing | Spell | Gradually restores health to multiple allies (HoT) |
| 6 | Divine Sense | Passive | Sense undead presence and spiritual corruption |
| 7 | Shield of Faith | Spell | Protective blessing reduces incoming damage |
| 8 | Revitalize | Spell | Restore health and stamina |
| 9 | Consecrate | Spell | Sanctify ground, harming undead and disrupting dark forces |
| 10 | Mass Heal | Spell | Instantly restore significant health to allies (AoE) |
| 11 | Divine Resilience | Passive | Allies take reduced damage while critically injured |
| 12 | Remove Curse | Spell | Removes magical curses and afflictions |
| 13 | Beacon of Hope | Spell | Increases effectiveness of healing effects |
| 14 | Radiant Smite | Spell | Deal radiant damage to undead and dark entities |
| 15 | Resurrection | Spell | Restore life to a recently fallen ally (long channel, low HP return, heavy [rez sickness](../system/death.md)) |
| 16 | Spirit Mend | Spell | Heal an ally through obstacles or distance |
| 17 | Sacred Barrier | Spell | Create powerful protective barrier for allies |
| 18 | Faithful Guardian | Passive | Automatically shield the most vulnerable ally |
| 19 | Life Overflow | Passive | Excess healing converts into temporary shields |
| 20 | **Divine Intervention** | Capstone | Once per long interval, prevent a party wipe with overwhelming divine aid |

## Healing Reference (Levels 1–20)

### Design Assumptions (Locked)

- Party HP ≈ 999
- Combat heals never exceed ~40–45% max HP
- "Empowered" = same spell, more mana, faster reconstruction
- Emotional pressure scales with speed + intensity, not spell tier

---

### Single-Target Healing

#### Cure Light Wounds

| Mode | Heal Range | Time | Mana Cost | Notes |
|------|-----------|------|-----------|-------|
| Normal | 60–120 HP | Instant | Low | Safe, routine |
| Empowered | 180–300 HP | Instant | High | Tissue rebuilt rapidly |
| Overdrawn (rare) | 300–380 HP | Instant | Extreme | Causes visible backlash in Wade |

**Empowered Effect**
- Accelerates clotting, lung re-inflation, organ stabilization
- Leaves patient weak, shaken, alive

**Emotional Cost**
- Normal: Minimal
- Empowered: Noticeable
- Overdrawn: Severe (hands shake, dissociation)

> This is the spell you want for Clint's bear trap moment.

---

#### Spirit Mend

| Mode | Heal Range | Time | [Mana](../system/mana.md) Cost | Notes |
|------|-----------|------|-----------|-------|
| Standard | 150–250 HP | 3–6 sec channel | Moderate | Slow reconstruction |
| Sustained | +30–40 HP/sec | Channel | Sustained | Wade prefers this |

**Empowered Effect**
- Rarely empowered
- Doing so shortens channel but spikes emotional load

**Use Case**
- "You're hurt, but not dying right now."

---

#### Revitalize

| Mode | Heal Range | Time | Mana Cost | Notes |
|------|-----------|------|-----------|-------|
| Standard | 120–200 HP | Short cast + HoT | Moderate | Restores stamina |
| Empowered | 200–260 HP | Faster cast | High | Clears shock/exhaustion |

**Extra Effects**
- Reduces exhaustion
- Stabilizes breathing
- Clears dizziness

**Emotional Cost**
- Low → Medium
- This spell calms Wade. It fixes aftermath, not crisis.

---

### Group Healing

#### Prayer of Healing

| Mode | Heal Range | Time | Mana Cost | Notes |
|------|-----------|------|-----------|-------|
| Standard | 150–220 HP (AoE) | Long cast | Moderate | Out of combat |
| Empowered | Not used | — | — | Wade refuses to rush this |

**Emotional Cost**
- Very low
- Everyone's already stable.

---

#### Mass Heal

| Mode | Heal Range | Time | Mana Cost | Notes |
|------|-----------|------|-----------|-------|
| Standard | 180–260 HP (AoE) | Instant | High | Emergency stabilization |
| Empowered | 260–350 HP | Instant | Extreme | Multiple lives at once |

**Emotional Cost**
- High
- Too many bodies, too much damage input.

---

### Emergency / Line-Crossing

#### Restoration (Lesser / Greater)

| Type | Effect | Time | Mana Cost | Notes |
|------|--------|------|-----------|-------|
| Lesser | Clears poison, paralysis, breathing issues | Short cast | Moderate | Surgical |
| Greater | Clears severe trauma, organ failure | Long cast | High | Drains Wade |

**Key Point:** Restoration does not heal HP — it makes healing possible.

---

#### Resurrection
- **Type:** Spell
- **Source:** [Cleric of Healing](../classes/cleric-of-healing.md)
- **Level:** 15
- **Cost:** High mana (scales with rez tier)
- **Cooldown:** None (limited by mana and channel time)
- **Duration:** Channel (30s+ at L15, scaling shorter with level)
- **Targeting:** Ally (ghost at corpse — rezzer must be physically present)
- **Tags:** Healing, Resurrection
- **Rules:**
  - Target must be in [ghost state](../system/death.md) (not yet released).
  - Rezzer must be at the corpse location.
  - Channeled cast — rezzer cannot take other actions during channel. Interrupted if the rezzer takes damage or moves.
  - Target returns at low HP (10-25% at L15, scaling with level).
  - Target suffers [rez sickness](../system/death.md) — reduced stats for a duration, severity scales inversely with rez quality.
  - At L15, this is a post-combat tool. The 30s+ channel makes mid-fight use nearly impossible without dedicated protection.
- **Scaling:** Channel time decreases, HP on return increases, rez sickness lessens. True Resurrection (~L90-95) is full HP restore with minimal sickness and ~5s channel.

---

## Key Mechanics

### Anti-Undead Kit
- Turn Undead (Level 1)
- Consecrate (Level 9)
- Radiant Smite (Level 14)

### Protection
- Shield of Faith (single target)
- Sacred Barrier (area)
- Faithful Guardian (automatic)
- Life Overflow (excess healing → shields)

## Notable Clerics of Healing

- [Wade](../characters/party/wade.md)

## Beyond Level 20

Levels 1–20 above are Book-1 canon. Post-20 progression is deliberately unlocked: new abilities land every 2–3 levels, passives gain **II / III** tiers (Mastery lines), and capstones acquire upgrades at major bands — but specific abilities get designed and locked **per book, as the story reaches them** (see the [book-level pacing table](../system/xp.md#leveling-curve-k1k3)). Designing L21–99 now would only create canon debt.

- *(TODO: add unresolved items for Cleric Of Healing, and mirror them into `canon/status.md`.)*

## Ability Stat Blocks

> Full kit, in level order. Healing spells keep their full numbers in the [Healing Reference](#healing-reference-levels-120) above — their blocks here point to it. Costs assume the **Medium mana group** (L1 ≈ 17, L10 ≈ 80, L20 ≈ 150 — see [stat progression](../system/stat-progression.md)).

#### Cure Light Wounds
- **Type:** Spell · **Level:** 1 · **Cost:** 12 mana (Empowered 45 · Overdrawn 90) · **Cooldown:** none · **Duration:** Instant (1s cast) · **Targeting:** Ally (30 ft)

**Rules**
- Numbers and modes in the [Healing Reference](#cure-light-wounds): 60–120 normal, 180–300 Empowered, 300–380 Overdrawn.
- The workhorse. The [emotional limiter](#emotional-limiter) scales with speed and intensity, not tier — Overdrawn is the mode Wade [will not reach for again](../lore/dungeons/spirit-dungeon/boss.md#phase-3-manager-exposed).

**Scaling:** +10 HP to both ends per 5 levels.

#### Holy Light
- **Type:** Spell · **Level:** 1 · **Cost:** 5 mana + 1 mana/min upkeep · **Duration:** Sustained (up to ~10 min) · **Targeting:** Self (30 ft radius)

**Rules**
- Identical to the [Paladin block](paladin-of-the-system.md#holy-light) — granted to all holy classes. Steady divine light; no damage; undead/corrupted suffer −5% accuracy inside and won't willingly cross the lit edge unless commanded or aggroed.

**Scaling:** +5 ft radius and −1% additional accuracy per 5 levels.

#### Turn Undead
- **Type:** Spell · **Level:** 1 · **Cost:** 15 mana · **Cooldown:** 20s · **Duration:** Instant (effects 6s) · **Targeting:** Area (20 ft, undead only)

**Rules**
- Undead at or below the Cleric's level **flee** for 6s or take 10–20 radiant damage if they cannot path away.
- Elites and bosses: no flee — instead −10% damage dealt for 6s.
- First shown Ch 20 (Risen Skeletons).

**Scaling:** damage +5 per 5 levels; the flee threshold tracks Cleric level (level-delta rules apply).

#### Bless
- **Type:** Spell · **Level:** 2 · **Cost:** 20 mana · **Cooldown:** none · **Duration:** 60s · **Targeting:** Group

**Rules**
- Allies gain the **Blessed** status: +5% accuracy, +2 to resistance checks against fear.
- One Blessed instance per caster; recasting refreshes duration.
- Prose note: Ch 16's "Blessed" is this status — *Bless* is the spell, *Blessed* is what it applies.

**Scaling:** +1% accuracy per 5 levels; duration +30s at L10 and L20.

#### Cleric Aura
- **Type:** Aura · **Level:** 3 · **Cost:** none (always on) · **Duration:** Permanent · **Targeting:** Allies within 15 ft

**Rules**
- Passive calm radius: allies gain minor fear resistance (+1 to fear resistance checks) and **+5% healing received**.
- **Ambient [Cleanse](../magic/spells/cleanse.md).** The aura continuously runs the beginner cleaning cantrip on everyone inside it. Not instant — it works the way sunlight dries something. Walk near Wade for a while and the blood comes off your gear, the smell goes, and you arrive somewhere looking like a person. Nobody casts anything. Nobody asks.
- Stacks with Blessed. Shown on Wade's sheet Ch 12.

**Scaling:** +5 ft radius per 5 levels; healing bonus +1% per 10 levels.

> **The Wade of it.** This is the ability that characterizes him best. His magic tidies people up as a side effect of him standing near them, without being asked and without him getting any credit — the passive, unglamorous, permanently-on version of care, which is Wade entire.
>
> **It is named on-page in Ch 22, and it should be.** *(Supersedes an earlier draft of this note, which held that Wade never mentions it and nobody notices.)* Wade says his aura already has a cleaning effect; Clint answers *"I wondered why I was still so clean. I assumed it was because Vanessa kept burning off my clothes."* That is the correct call and the earlier instinct was wrong: **the reader cannot miss something they never knew existed.** Establishing the effect once, as a joke, is precisely what makes its absence legible later. Plant it in comedy; collect on it in silence.
>
> **The Book 2 consequence:** Wade [leaves the party after Book 1](../system/xp.md). The party does not lose the *capability* — [Cleanse](../magic/spells/cleanse.md) is a beginner spell anyone can learn, and they all know it. What they lose is **never having to think about it.** They go back to casting it on themselves, manually, every day, forever. Because Ch 22 named the effect, the reader gets there before the party does and spends a few chapters waiting for one of them to say it out loud. When somebody finally does, it should land harder than any line about missing him — and it should arrive **before** anyone says his name.
>
> **The wish (Book 1) — delivered Ch 22.** Wade wonders whether he could get [Rebekah's](../characters/party/rebekah.md) [Rejuvenation](temporal-bard.md#rejuvenation) folded into his aura: always on, covering everyone near him, nobody having to ask. He is describing a thing he wants to be. *(See `characters/party/wade.md` — deliberate long-range foreshadow of the [substrate ending](../meta/real-world.md). Do not return to it; it is planted and it is enough.)*

#### Cure Poison
- **Type:** Spell · **Level:** 3 · **Cost:** 15 mana · **Cooldown:** none · **Duration:** Instant (2s cast) · **Targeting:** Touch (ally)

**Rules**
- Removes one poison effect of the Cleric's level or below. Higher-level venoms are *suppressed* (paused, not cleared) for 60s per cast.
- The narrow forerunner of [Lesser Restoration](#lesser-restoration), kept because it's cheaper and faster at the one job.

**Scaling:** clears poisons up to level+2 at L10, level+5 at L20.

#### Lesser Restoration
- **Type:** Spell · **Level:** 4 · **Cost:** 25 mana · **Cooldown:** none · **Duration:** Instant (short cast, ~2s) · **Targeting:** Touch (ally)

**Rules**
- Clears poison, paralysis, and breathing obstruction. Surgical — one affliction category per cast.
- Restoration does not heal HP; it makes healing possible (see the [Restoration table](#restoration-lesser--greater)).

**Scaling:** cast time shortens; Greater Restoration (higher tier) clears severe trauma and organ failure.

#### Prayer of Healing
- **Type:** Spell · **Level:** 5 · **Cost:** 40 mana · **Cooldown:** none · **Duration:** 8s cast · **Targeting:** Group (30 ft)

**Rules**
- Numbers in the [Healing Reference](#prayer-of-healing): 150–220 HP to every ally in range. The 8s cast makes it an **out-of-combat** tool by design — a said-aloud prayer, unhurried.
- Wade refuses to Empower it. Everyone is already stable; rushing a prayer is the tell that something is wrong with *him*.

**Scaling:** +15 HP to both ends per 5 levels.

#### Divine Sense
- **Type:** Passive · **Level:** 6 · **Targeting:** Self (60 ft)

**Rules**
- Undead presence and spiritual corruption register as directional *pressure* — through walls, muffled by distance. No count, no map; a compass needle, not a radar.
- **Reads only what has (or had) a spirit.** Constructs return nothing: twelve feet of [bone on strings](../lore/dungeons/spirit-dungeon/boss.md#passive-bone-not-dead) reads *empty*, and the emptiness is itself information.
- Passive and always on. Wade describes it as a draft from a door that shouldn't be open.

**Scaling:** +10 ft per 5 levels; at L15+ he can distinguish *kinds* of wrongness (undeath vs. corruption vs. desecrated ground).

#### Shield of Faith
- **Type:** Spell · **Level:** 7 · **Cost:** 25 mana · **Cooldown:** none · **Duration:** 60s · **Targeting:** Ally (30 ft)

**Rules**
- One ally takes **−15% damage** from all sources. One instance per caster — moving it means recasting it.
- The pre-fight gift: it goes on the tank walking in, or on whoever Wade is most worried about, which is not always the same person.

**Scaling:** −3% further per 5 levels.

#### Revitalize
- **Type:** Spell · **Level:** 8 · **Cost:** 30 mana · **Cooldown:** none · **Duration:** Short cast + HoT · **Targeting:** Ally (30 ft)

**Rules**
- Numbers in the [Healing Reference](#revitalize): 120–200 HP plus **+50 stamina**, clears exhaustion, dizziness, shock.
- The aftermath spell — it fixes the state a fight leaves a body in, not the fight itself. Canonically the cast that calms *Wade* down.

**Scaling:** stamina restore +10 per 5 levels.

#### Consecrate
- **Type:** Spell · **Level:** 9 · **Cost:** 35 mana · **Cooldown:** 30s · **Duration:** 60s · **Targeting:** Area (20 ft circle)

**Rules**
- Sanctifies the ground: undead inside deal **−20% damage** and take **10 radiant per 3s**; necromantic and dark-magic channels cast into or out of the circle suffer −2 to their checks.
- **No corpse animates on holy ground.** Raising, converting, or re-stringing the dead simply fails inside the circle — the direct counter to [Dan's](../characters/villains/dan.md) battlefield conversions in Part 3.
- The circle is visible: soft light in the grass. Undead path around it, which is its own kind of crowd control.

**Scaling:** +5 ft radius and +5 radiant per 5 levels.

#### Mass Heal
- **Type:** Spell · **Level:** 10 · **Cost:** 70 mana · **Cooldown:** 30s · **Duration:** Instant · **Targeting:** Group (30 ft)

**Rules**
- Numbers in the [Healing Reference](#mass-heal): 180–260 HP to every ally, instantly. Emergency stabilization — the spell for the moment everything went wrong at once.
- Highest sustained [emotional cost](#emotional-limiter) in the kit: too many bodies, too much damage input, all of it at once.

**Scaling:** +20 HP to both ends per 5 levels.

#### Divine Resilience
- **Type:** Passive · **Level:** 11 · **Targeting:** Allies (30 ft)

**Rules**
- Allies below **25% max HP** take **−15% damage**. No action, no cost — the worse it gets, the harder his people are to finish.
- Deliberately rhymes with his cracked [Shard of Devotion](../items/accessories/mirror-shards.md) (+10% healing on targets below 25%): Wade's whole late kit bends toward the almost-lost.

**Scaling:** −5% further at L20.

#### Remove Curse
- **Type:** Spell · **Level:** 12 · **Cost:** 40 mana · **Cooldown:** none · **Duration:** Instant (4s cast) · **Targeting:** Touch (ally)

**Rules**
- Removes magical curses, hexes, and afflictions of the Cleric's level or below.
- **Not mental domination.** Domination is [unauthorized control](paladin-of-the-system.md#unauthorized-control-the-classs-legal-theory), not a curse — a different category of wrong, and divine magic fixes bodies, not sovereignty. An installed lattice ([Amanda](../characters/supporting/amanda.md)) is untouchable from this side too: there is nothing cursed to lift.
- The distinction is load-bearing: the Part 3 [diagnosis scene](../story/outline-part3-4.md) only lands if the reader already knows Wade's entire class has no lever here.

**Scaling:** curse level ceiling rises with level; cast shortens to 2s at L20.

#### Beacon of Hope
- **Type:** Spell · **Level:** 13 · **Cost:** 30 mana · **Cooldown:** none · **Duration:** 60s · **Targeting:** Ally (30 ft)

**Rules**
- One ally receives **+25% from all healing** and HoT effects on them tick **25% faster**. One beacon at a time.
- Multiplies with the [Cleric Aura's](#cleric-aura) +5% and the [Blue Ribbon](../lore/dungeons/spirit-dungeon/rooms.md#encounter-carnival-set) class of bonuses — the late-game answer to healing checks is stacking the *received* side.

**Scaling:** +5% further per 5 levels.

#### Radiant Smite
- **Type:** Spell · **Level:** 14 · **Cost:** 30 mana · **Cooldown:** 10s · **Duration:** Instant · **Targeting:** Enemy (40 ft)

**Rules**
- A bar of daylight: **40–60 radiant damage**, **doubled vs undead and corrupted entities**.
- The healer's only real weapon, given fourteen levels late — the class states its priorities in its level order.

**Scaling:** +10 to both ends per 5 levels.

#### Resurrection
- **Type:** Spell · **Level:** 15 — full block in [Emergency / Line-Crossing](#resurrection) above (30s+ channel, ghost-at-corpse, [rez sickness](../system/death.md)).

#### Spirit Mend
- **Type:** Spell · **Level:** 16 · **Cost:** 35 mana (or sustained) · **Cooldown:** none · **Duration:** 3–6s channel · **Targeting:** Ally (100 ft, **no line of sight required**)

**Rules**
- Numbers in the [Healing Reference](#spirit-mend): 150–250 HP, or +30–40 HP/s sustained.
- Heals **through obstacles and distance** — the spell follows the bond, not the body. The one heal for the person he cannot reach.

**Scaling:** range +20 ft per 5 levels.

#### Sacred Barrier
- **Type:** Spell · **Level:** 17 · **Cost:** 60 mana · **Cooldown:** 60s · **Duration:** 10s · **Targeting:** Area (15 ft dome)

**Rules**
- A dome of held light: absorbs up to **400 damage** total before collapsing.
- It stops force, not feet — enemies can walk in, which keeps it a shelter, not a fortress. Its best use is buying a channel: a [Resurrection](#resurrection) cast inside a Barrier is the intended combo.

**Scaling:** +100 absorption per 5 levels.

#### Faithful Guardian
- **Type:** Passive · **Level:** 18 · **Cooldown:** 30s (internal) · **Targeting:** Allies (30 ft)

**Rules**
- Whenever an ally drops below **30% max HP**, they automatically gain a **100 HP shield** (8s). No cast, no action, no choice on Wade's part.
- The class thesis, mechanized: care that arrives without being asked, before he has even turned around.

**Scaling:** shield +25 HP per 5 levels.

#### Life Overflow
- **Type:** Passive · **Level:** 19 · **Targeting:** Allies

**Rules**
- **50% of overhealing** converts to a shield on the target (cap 150, lasts 10s).
- Nothing he gives is wasted anymore. Late-kit economy: at L19 the limiting factor is his attention, not his mana.

**Scaling:** cap +50 at L20.

#### Divine Intervention
- **Type:** Capstone · **Level:** 20 · **Cost:** all remaining mana (min 100) · **Cooldown:** once per day · **Duration:** Instant + 5s · **Targeting:** Party (40 ft)

**Rules**
- The god picks up the phone: every ally is instantly healed **300 HP**, every ally is **immune to damage for 5s**, and every fallen ally still in [ghost state](../system/death.md) returns at **15% HP** (full rez sickness).
- Once per day, and it takes everything he has left — the cast ends with Wade at zero mana, on his knees, and the fight still to finish around him.
- [Emotional cost](#emotional-limiter): total. This is the spell that only exists for the day he'd have paid anything anyway.

**Scaling:** none. This is what L20 *is*.

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

- *(TODO: add unresolved items for Cleric Of Healing, and mirror them into `canon/status.md`.)*
