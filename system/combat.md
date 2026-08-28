---
canon: true
stability: evolving
---

# Combat

This page defines the canonical combat loop and resolution pipeline.
Quantum Error combat is **real-time tick-based** under the hood, but it reads like discrete actions.

## Core Model

- Combat occurs in a **room**.
- Entities act when their **action timer** is ready.
- Actions resolve as: **[Targeting](targeting.md) → Hit Check → Damage → [Effects](effects.md) → Death/Downed**.

## Time and Ticks

- **Tick**: the smallest simulation step (implementation detail).
- **Action Cooldown**: time until an entity can act again.
- **Global Cooldown (GCD)**: optional shared delay after any action (used to prevent spam).

Canon assumption:
- If a page or ability uses "seconds" it maps to real-time.
- If it uses "turns", a turn is an abstract chunk of time (use sparingly; prefer seconds).

## Action Types

- **Basic Attack**: weapon attack; usually cheapest and most frequent.
- **Ability**: spell/skill/song/smite; may consume mana/stamina.
- **Reaction (Optional)**: block/parry/interrupt; must be explicitly supported.

### Ability Type Vocabulary

The `Type:` field on class stat blocks draws from this shared vocabulary. Class files link here; mechanics a single class owns (smites, songs, System auras) stay in their class files.

- **Spell** — mana-fueled, with a cast time unless marked Instant; a direct hit during the wind-up interrupts the cast (see [Interrupts and Control](#interrupts-and-control)).
- **Skill** — stamina-fueled trained action; how well it executes is governed by the relevant [Proficiency](proficiencies.md).
- **Attack** — a strike resolved through normal [hit resolution](#hit-resolution), usually carrying a rider (stun, bleed, reposition).
- **Attack Modifier** — arms the next connecting blow and is consumed on the hit, not the swing; the [Smite line](../classes/paladin-of-the-system.md#smite-progression-canonical) is the canonical example.
- **Passive** — always on; no cost or cooldown unless the block states an internal one.
- **Racial Passive** — a Passive granted by race rather than class; stacks with the full class kit.
- **Utility** — an active effect that is none of attack, heal, or buff: repositions, rewinds, tools, problem-solvers.
- **Buff** — applies a beneficial status to self or an ally for a duration; visible as a [status effect](ui-popups.md#2-status-effect-buff--debuff).
- **Defensive** — a Buff or trigger whose only job is avoiding or mitigating damage.
- **Aura** — a sustained radius effect centered on the bearer, toggled on with per-minute upkeep; it moves with them. (Paladin [System Auras](../classes/paladin-of-the-system.md#system-auras) add class-specific stacking rules.)
- **Toggle** — an on/off state maintained until broken by cost, damage, or observation (e.g. [Sneak](../classes/veilstepper-rogue.md#sneak)).
- **Reaction** — resolves inside another actor's action window, per the list above; must be explicitly supported by an ability.
- **Command** — a vocal order carrying System authority; threat and formation effects (Paladin [Threat System](../classes/paladin-of-the-system.md#threat-system)).
- **Song / Refrain** — the Temporal Bard's two ability types; the full economy lives in [Songs vs. Refrains](../classes/temporal-bard.md#songs-vs-refrains).
- **Capstone** — the Level-20 class-defining ability; once-per-day scale, built to headline a fight rather than a rotation.

## Hit Resolution

### The Formula

```
hit% = 50 + 5 × (Accuracy − Evasion)          clamped to [5%, 95%]
```

> ### **One point of accuracy = 5 percentage points of hit chance.**
> This is the only number you need to remember. Everything below is derived from it.

**Where the inputs come from:**

```
Accuracy    = level/2  +  proficiency_rank/10  +  (governing attribute − 10)/4
Evasion     = level/2  +  (DEX − 10)/4  +  gear/effects
Mob Evasion = level/2
```

Mob **Accuracy** uses the [framework formula](mob-framework.md#accuracy) `5 + 0.5 × level`. Note that mobs are slightly better at hitting than dodging by design — a L10 mob has Accuracy 10 and Evasion 5.

**Note the weighting.** A full **10 ranks** of [proficiency](proficiencies.md) is worth **1 point of accuracy** — the same as 4 points of attribute. Attributes are a rounding error here; proficiency is the whole game. That is deliberate, and it is the mechanical statement of *"[power is not mastery](proficiencies.md#the-gap-hacked-stats-novice-hands)."*

### What a Penalty Actually Costs

| Penalty | Hit chance lost | Feels like |
|---|---|---|
| −1 | −5 points | Noticeable over a long fight |
| −2 | −10 points | A real handicap |
| **−3** | **−15 points** | **Roughly a third of your output, gone** |
| **−5** | **−25 points** | **Half your swings stop landing** |
| −8 | −40 points | You are not meaningfully attacking |

### Worked Example: Clint vs a Level 10 Mob

The canonical reference case. [Clint](../characters/party/clint.md) is **L4**, **DEX 20** (console-boosted), **Novice 3** weapon proficiency.

```
Clint Accuracy = 4/2  +  3/10  +  (20−10)/4  =  2 + 0.3 + 2.5  =  4.8
L10 Mob Evasion = 10/2 = 5
hit% = 50 + 5 × (4.8 − 5) = 49%
```

**He is a coin flip against L10s** — which is exactly what [his sheet claims](../characters/party/clint.md): *"misses often against L10s, survives on stat pool."*

Now the same fight under debuffs:

| Condition | Accuracy | Hit% |
|---|---|---|
| Clean | 4.8 | **49%** |
| −3 ([Severed Hands](../lore/dungeons/spirit-dungeon/mobs.md#severed-hand-swarm)) | 1.8 | **34%** |
| −5 ([Asylum strobes](../lore/dungeons/spirit-dungeon/rooms.md#asylum-concentrated-strobe)) | −0.2 | **24%** |
| −5 strobes, **with [Carnival Shades](../lore/dungeons/spirit-dungeon/mobs.md#the-100-ticket-set--the-temptation)** (−3 to the penalty) | 2.8 | **39%** |

And incoming, for contrast:

```
L10 Mob Accuracy = 10
Clint Evasion = 4/2 + (20−10)/4 = 4.5
hit% = 50 + 5 × (10 − 4.5) = 77.5%   →  L10 mobs hit Clint ~78% of the time
```

> ### Why This Matters More To This Party Than Anyone Else
>
> They console-boosted attributes, HP, and mana to the ceiling. **They never touched [proficiencies](proficiencies.md).** So DEX 20 buys Clint +2.5 accuracy while his Novice hands buy +0.3, and there is no stat in the game that fixes it.
>
> **Accuracy debuffs bypass the cheat completely.** A −5 strobe barely inconveniences a normally-progressed party and takes half this party's offense away. It is the one lever a dungeon has that their 999 HP pool cannot absorb — which is why the showroom leans on it, and why the Carnival Shades are a genuinely valuable prize rather than a trinket (**+15 points of hit chance** for 10 tickets).

### Grappled and Pinned Targets

**A grappled, pinned, or otherwise immobilized target has no Evasion. Attacks against it ignore the evasion term entirely and simply hit.**

```
hit% = 95% (the clamp ceiling)   —   you are holding it; it is very hard to miss
```

This makes grappling **the correct mechanical answer to an accuracy problem.** A fighter with hacked attributes and novice technique cannot reliably land a swing on something that dodges — so he removes dodging from the equation. It costs him his position and both hands (see the [Asylum tableau](../lore/dungeons/spirit-dungeon/rooms.md#encounter-asylum-set), where Clint pins the Head Surgeon under −5 strobes and lands six consecutive smites he would otherwise have hit with roughly one swing in four).

### Actions, Misses, and Ability Cooldowns

- Characters attempt **one attack per round**.
- **An ability tied to an attack is consumed on the hit, not on the swing.** A missed swing does not spend the mana, does not trigger the cooldown, and does not waste the charge — the ability stays armed until it lands.

This is the rule that keeps a low hit rate from being multiplicative misery. A **4-second** ability cooldown gives roughly **three swings** per window, so most windows still land the ability even at a poor hit rate:

| Hit% per swing | Chance of landing within one 4s window (3 swings) |
|---|---|
| 49% (clean) | **87%** |
| 34% (−3) | **71%** |
| 24% (−5) | **56%** |

So a heavy accuracy debuff doesn't multiply an ability's cooldown — it makes it **slip a window** now and then. Under −5 strobes, Clint lands a smite roughly every other cooldown rather than every one: meaningfully slower, not catastrophically so. Basic attacks in the gaps still miss at the full rate.

> **Round length:** treat a basic-attack round as **~1.3 seconds** for this purpose (≈3 per 4-second cooldown). The *"~4s rounds"* used in [mob-framework.md's](mob-framework.md#rounds-to-kill-player-vs-normal-mob-same-level) rounds-to-kill tables is a coarser abstraction for DPS estimation and is not the same unit.

### Guardrail

**Design guardrail (canon intent):**
An encumbered attacker with a large accuracy penalty should **not** still hit a nimble target ~95% of the time.
If the formula ever produces that outcome, it should be considered a bug in tuning. *(The formula above satisfies this: −8 accuracy against an evasive target floors out near 10%.)*

### Guaranteed Hits / Saves

Some abilities do not use Accuracy/Evasion. They must declare:
- `Roll: None` (guaranteed)
or
- `Roll: Save` (defender uses a saving throw/resist stat)

## Criticals and Glancing

Optional but supported conventions:
- **Critical Hit**: increases damage and/or applies a special effect
- **Glancing Blow**: reduced damage on near-miss (use for "always does something" abilities)

If used, declare in the ability:
- `Crit: <chance>`, `Crit Effect: <...>`
- `Glance: <rule>`

## Damage Pipeline

Damage is resolved in this order:

1. **Base Damage** (weapon/spell)
2. **Modifiers** (stats, buffs, vulnerability, amplification)
3. **Mitigation** (armor/resist/soak, reductions, shields)
4. **On-Hit Procs** (status effects, lifesteal)
5. **Death/Downed Check**
6. **Post-Death Triggers** (on-kill effects, summons expiry, etc.)

### Mitigation Conventions

Damage types should declare an **element/type** (physical, fire, arcane, etc.).
Mitigation sources may include:
- Flat reduction
- Percent reduction
- Immunity (rare; must be explicit)
- Absorption shields (consume shield first)

## Threat / Aggro (Canonical)

Threat determines enemy target selection unless overridden by a forced taunt/charm.

- Damage generally increases threat.
- Healing generally increases threat (often split across enemies).
- Some abilities explicitly manipulate threat.

## Interrupts and Control

Crowd control effects (stun, silence, fear, charm) are defined in `effects.md`.
Combat must respect effect tags:
- `Stun`: prevents actions
- `Silence`: prevents spellcasting
- `Disarm`: prevents weapon attacks
- `Charm/Compel`: forces behavior or target priority

**Casting under fire:** taking a direct hit while winding up a **cast-time** spell interrupts the cast. Instant abilities and *sustained* effects (maintained songs, auras) are unaffected — they are upkeep, not wind-up. (The gnomes' "GNOMES RULE!" jolt is a stronger, weaponized version — it chops even sustained songs and channels, which ordinary hits do not.)

## Death and Respawn

Death rules can vary by zone and conditions (see `mana.md` for Null Magic Zones).

Canonical baseline:
- Characters can respawn unless a special condition prevents it.
- Certain environments (e.g., Null Magic Zones) can make death permanent unless extraction occurs.

## Open Questions (Phase 1 capture)

These are acknowledged design points that may be tuned later:
- ~~Exact hit chance formula (logistic vs linear clamp vs opposed roll)~~ — **RESOLVED 2026-08-15.** Linear opposed check with a [5,95] clamp at **5 percentage points per point of accuracy**. See [Hit Resolution](#hit-resolution).
- Whether block/parry exists for all classes or only some
- Whether glancing blows are universal or per-ability
- Percentage-phrased evasion buffs (e.g. [Veil of Offbeats](../classes/temporal-bard.md) "+10% evasion") should be read as **+10 percentage points of dodge chance = +2 Evasion**. Applied consistently, but not yet restated on the ability pages.
