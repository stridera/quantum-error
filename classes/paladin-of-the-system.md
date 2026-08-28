---
canon: true
stability: locked
last_reviewed: 2026-08-24
---

# Paladin of the System

Paladins are warriors of their god. They train in weapons, armor, and combat while being able to channel divine magic to heal and combat the undead.

The Paladin of the System is a unique variant with access to [System Magic](../magic/schools/system-magic.md)—a discipline developed specifically for someone with pre-transition system knowledge.

## Design Philosophy

- **Role**: Tank, threat control, party protection
- **Theme**: Authoritative, minimal, System-enforced order
- **Unique Mechanics**:
  - Aura stacking—multiple System auras active simultaneously
  - Smite progression—same ability gains deeper authority over time

## Ability Progression (Levels 1-20)

| Level | Ability | Type | Effect |
|-------|---------|------|--------|
| 1 | [Commanding Shout](#commanding-shout) | [Command](#threat-system) | Forces nearby hostiles to focus on you; overrides threat priority |
| 1 | [Cure Light Wounds](#cure-light-wounds-paladin) | [Spell](../system/combat.md#ability-type-vocabulary) | Restore health to a living target |
| 1 | [Holy Light](#holy-light) | [Spell](../system/combat.md#ability-type-vocabulary) | Conjure steadfast divine light; undead and corrupted entities flinch from its radius. Granted to all holy classes. |
| 1 | [Smite: Judgment](#level-1--smite-judgment-privileged) | [Attack Modifier](#smite-progression-canonical) | See Smite Progression below |
| 2 | [Shield Mastery](#shield-mastery) | [Passive](../system/combat.md#ability-type-vocabulary) | Improved block efficiency and damage smoothing |
| 3 | [System Aura](#system-aura) | [Aura](#system-auras) | Hostile mental influence becomes detectable and interruptible |
| 4 | [Shield Bash](#shield-bash) | [Attack](../system/combat.md#ability-type-vocabulary) | Strike with shield, stunning target and increasing threat |
| 4 | [Smite: Sanction](#level-4--smite-sanction) | [Upgrade](#smite-progression-canonical) | Smite: Judgment upgrades automatically |
| 5 | [Judged Strike](#judged-strike) | [Attack](../system/combat.md#ability-type-vocabulary) | Increased damage to entities exerting unauthorized control |
| 6 | [Resolve](#resolve) | [Passive](../system/combat.md#ability-type-vocabulary) | Reduced duration of stun, fear, and control effects |
| 7 | [Reinforcing Command](#reinforcing-command) | [Command](#threat-system) | Refreshes taunt effects and bolsters allied defenses |
| 7 | [Escalating Sanctions](#level-7--passive-escalating-sanctions) | [Passive](../system/combat.md#ability-type-vocabulary) | Smite stacks debuff on repeated hits |
| 8 | [System Weapon](#system-weapon) | [Buff](../system/combat.md#ability-type-vocabulary) | Weapon gains anti-anomaly properties and enhanced threat generation |
| 8 | [Exception Handling](#exception-handling) | [Buff](../system/combat.md#ability-type-vocabulary) | Defensive cooldown: damage taken −50% for 6s; a single catastrophic hit is caught and reduced further. The tank-buster answer. |
| 9 | [Guardian Intercept](#guardian-intercept) | [Reaction](../system/combat.md#ability-type-vocabulary) | Redirect incoming damage from an ally to yourself |
| 10 | [Aura of Cognitive Stability](#aura-of-cognitive-stability) | [Aura](#system-auras) | Allies gain resistance to charm, domination, and coercion |
| 11 | [Smite: Enforcement](#level-11--smite-enforcement) | [Upgrade](#smite-progression-canonical) | Smite: Sanction upgrades automatically |
| 12 | [Cure Moderate Wounds](#cure-moderate-wounds-paladin) | [Spell](../system/combat.md#ability-type-vocabulary) | Restore a greater amount of health |
| 13 | [System Judgment](#system-judgment) | [Attack](../system/combat.md#ability-type-vocabulary) | Punishes entities exerting unauthorized control or coercion |
| 14 | [Bulwark of Order](#bulwark-of-order) | [Aura](#system-auras) | Party-wide damage smoothing and reduced spike damage |
| 15 | [Oath Mastery I](#oath-mastery-i) | [Passive](../system/combat.md#ability-type-vocabulary) | Increases range and effectiveness of all active System auras |
| 15 | [Harmonized Enforcement](#level-15--passive-harmonized-enforcement) | [Passive](../system/combat.md#ability-type-vocabulary) | Aura-Smite synergy |
| 16 | [Radiant Charge](#radiant-charge) | [Attack](../system/combat.md#ability-type-vocabulary) | Gap-closer that stuns target and forces focus |
| 17 | [Unyielding Protocol](#unyielding-protocol) | [Passive](../system/combat.md#ability-type-vocabulary) | Prevent death once when damage would be fatal |
| 18 | [Rebuke Anomaly](#rebuke-anomaly) | [Reaction](../system/combat.md#ability-type-vocabulary) | Reflect or suppress hostile anomalous effects |
| 19 | [Dominion Protocol](#dominion-protocol) | [Passive](../system/combat.md#ability-type-vocabulary) | Control over System-sanctioned areas and engagement zones |
| 19 | [Smite: Verdict](#level-19--smite-verdict) | [Upgrade](#smite-progression-canonical) | Smite: Enforcement upgrades automatically |
| 20 | **[Avatar of the System](#avatar-of-the-system)** | [Capstone](../system/combat.md#ability-type-vocabulary) | Become a System anchor; all auras amplified and cannot be suppressed; permanent threat lock |

---

## Smite Progression (Canonical)

Smite is **privileged from Level 1**. Clint does not learn new smites—he is trusted with more consequences. The same smite call grows more dangerous over time.

> **Naming note:** early prose (Ch 5, console era) calls this ability **"Divine Strike"** — same smite, pre-activation name. Prose revision may align the name later; treat Divine Strike ≡ Smite: Judgment.

> "I didn't change what I was doing. The system changed what it allowed me to do."

> **Smite is consumed on the hit, not on the swing.** Smite is an **Attack Modifier** — it arms the next connecting blow. A miss costs nothing: no mana, no cooldown, no wasted charge. The smite stays armed until it lands.
>
> This matters enormously for Clint, whose [Novice hands](../system/proficiencies.md#the-gap-hacked-stats-novice-hands) put him near a coin flip against L10s. At roughly **three swings per 4-second cooldown** ([combat.md](../system/combat.md#actions-misses-and-ability-cooldowns)), he lands a smite in ~87% of windows when clean and ~56% under a −5 accuracy debuff. A bad hit rate makes his smites **slip a window** occasionally; it does not multiply their cooldown. The basic attacks in between still miss at the full rate — which is why his damage falls off a cliff under accuracy denial even though his smite cadence mostly holds.
>
> **And why he grapples.** Against a [pinned target evasion doesn't apply at all](../system/combat.md#grappled-and-pinned-targets). A fighter who can't reliably hit a dodging opponent solves it by holding on to one.

### Level 1 — Smite: Judgment (Privileged)

| | |
|---|---|
| **Type** | Attack Modifier |
| **Cost** | 10 Mana |
| **Cooldown** | 0 sec |
| **Authority Level** | 1 |

**Visible Effect**
- +15 flat System damage
- +5% weapon damage

**System-Level Behavior**
- Attack executed with privileged authority
- Target evaluated for: validity, alignment, enforcement eligibility
- No rules bypassed, no corrections applied
- Logging: `ACTION_TYPE: ENFORCEMENT | AUTHORITY_LEVEL: 1 | CORRECTIVE_ACTION: NONE`

**System Attunement (Visual)**: Any weapon used to deliver a privileged smite develops a faint glow—the visual residue of system-authorized force passing through a physical object. At Authority Level 1, the effect is subtle and cosmetic. It intensifies with authority level, foreshadowing the formal System Weapon buff at Level 8.

**Design Notes**: Functionally similar to a normal paladin's early smite, but crucially different in execution path. Clint can (and will) use this on every landed hit early. No system instability yet—only observation. *This is `sudo ls`. Same result. Different context.*

---

### Level 4 — Smite: Sanction

*Upgrades Smite: Judgment automatically*

| | |
|---|---|
| **Cost** | 15 [Mana](../system/mana.md) |
| **Cooldown** | 4 sec |
| **Authority Level** | 2 |

**Visible Effect**
- +30 flat System damage
- +10% weapon damage
- +30% damage vs summoned entities, corrupted entities, system-flagged anomalies

**New Enforcement Behavior**
- Performs active validity checks
- If target is invalid: applies Stagger (0.5 sec)
- Logging: `CORRECTIVE_ACTION: VALIDITY_CHECK | TARGET_VALIDITY: {VALID | INVALID}`

**Design Notes**: First smite that does real system work. Still feels like "just more damage" at a glance. This is where frequency begins to matter. Soft warnings may appear, but no penalties yet.

---

### Level 7 — Passive: Escalating Sanctions

*Smite Interaction Passive*

**Effect**
- Repeated smites against the same target apply: −3% mitigation per stack
- Max 3 stacks
- Stacks decay after 10 sec
- Bosses cap at 1 stack

**System Meaning**: Target is being marked as persistently noncompliant. Reinforces focused enforcement, not cleave spam.

**Design Notes**: Rewards Clint for staying on the problem. Encourages deliberate target selection. Still not about raw DPS.

---

### Level 11 — Smite: Enforcement

*Upgrades Smite: Sanction automatically*

| | |
|---|---|
| **Cost** | 25 Mana |
| **Cooldown** | 6 sec |
| **Authority Level** | 3 |

**Visible Effect**
- +45 flat System damage
- +15% weapon damage
- **Enforcement Debuff** (8 sec): −10% damage dealt, −10% evasion
- If target has illegal/temporary buffs: debuff increases to −15%

**System-Level Behavior**
- Logging: `CORRECTIVE_ACTION: PRIVILEGE_REDUCTION | TARGET_PRIVILEGES: DEGRADED`

**Design Notes**: Smite now weakens enemies, not just hurts them. Enforcement frequency now meaningfully impacts system stability. Clint starts choosing *when* to smite, not just *if*.

---

### Level 15 — Passive: Harmonized Enforcement

*Aura–Smite Synergy*

**Effect**
- While [System Aura](#system-aura) or [Aura of Cognitive Stability](#aura-of-cognitive-stability) is active:
  - Smite debuff duration +2 sec
  - Smite ignores 25% resistance

**System Meaning**: Stable battlefield = higher enforcement tolerance. Authority works best when order is maintained.

**Design Notes**: Encourages Clint to hold ground. Smite is strongest when Clint is doing his job.

---

### Level 19 — Smite: Verdict

*Early Apex — Book One*

| | |
|---|---|
| **Cost** | 40 Mana |
| **Cooldown** | 10 sec |
| **Authority Level** | 4 |

**Visible Effect**
- +65 flat System damage
- +20% weapon damage
- **Verdict Mark** (10 sec): Target takes +12% damage from allies
- Mark collapses if Clint disengages

**System-Level Behavior**
- Logging: `CORRECTIVE_ACTION: TARGET_MARKED | STATUS: UNDER_REVIEW`

**Design Notes**: Smite fully transitions from personal damage → party amplification. Extremely effective vs boss adds, elite summons, high-threat anomalies. This is where smite feels *judicial*.

---

### Smite Progression Summary

| Level | Smite Name | What Changed |
|-------|------------|--------------|
| 1 | Judgment | Privileged execution, no bypass |
| 4 | Sanction | Validity checks + control |
| 7 | Escalation | Persistent offender pressure |
| 11 | Enforcement | Privilege reduction |
| 15 | Harmony | Aura-synergized authority |
| 19 | Verdict | Party-wide judgment |

---

## Key Mechanics

### System Auras
- Multiple auras can be active simultaneously
- Auras stack with each other
- Oath Mastery I expands aura radius and effectiveness

### Threat System
- Commands establish and maintain combat authority
- System Weapon enhances threat generation
- Avatar of the System grants permanent threat lock

### Unauthorized Control (the class's legal theory)

The System keeps a **consent ledger**. Control of a sentient being — or of remains with a standing claim — without System-recognized authorization is a violation, and half this kit keys off it.

**Licensed (no grounds for enforcement):**
- Sanctioned content controlling its own mobs — the [Store Manager's](../lore/dungeons/spirit-dungeon/boss.md) puppets are dungeon property on dungeon strings. Judged Strike returns `NO GROUNDS` inside licensed content.
- Class abilities operating as designed: a summoner's summons, a tamed pet ([Qubit](../items/accessories/mimic-pet.md)), a [Necromancer](necromancer.md) raising **unclaimed** remains. The class is licensed; the license is the authorization.

**Unauthorized (enforcement-eligible):**
- **Mental domination of a sentient** — charm, coercion, thrall-binding. [Eron Vosk's](../characters/villains/eron-vosk.md) entire kit.
- **Animating claimed dead** — puppeting remains against the person's standing claim on their own body. [Dan](../characters/villains/dan.md) converting the raids' dead is this, by name.
- Possession, puppeteering a living body, exploit-driven control the System never granted.

**The lattice exception (load-bearing for Books 1–4):** enforcement abilities cut **live channels** — control that is actively maintained. An **installed lattice with no live tether** ([Amanda](../characters/supporting/amanda.md)) is not a channel; there is nothing to cut. This is why nothing in this kit — at any level — can free her, and why the Null Zone plan has to exist.

### Smite Philosophy
- Smite is privileged from Level 1
- Early smite is frequent and necessary
- Power comes from authority depth, not spam
- The same smite call grows more dangerous over time

## Notable Paladins

- [Clint](../characters/party/clint.md)

## Ability Stat Blocks

> Full kit, in level order (smites and their passives live in [Smite Progression](#smite-progression-canonical)). In-world grounding per block; log lines are the System's own voice. Costs assume the **Low mana group** (L1 ≈ 15, L10 ≈ 55 — see [stat progression](../system/stat-progression.md)); Clint's hacked 999 pool makes them trivial for him, which is the point.
>
> In-prose Help popups are rendered from these blocks **on demand**, using the System-wide shape in [UI Popups §3](../system/ui-popups.md#3-ability--unlock--help) — they are not pre-authored here. The stat block is the source of truth; a popup is a rendering of one.

#### Commanding Shout
- **Type:** Command · **Level:** 1 · **Cost:** 10 stamina · **Cooldown:** 8s · **Duration:** 6s · **Targeting:** Area (15 ft)

**Rules**
- All hostiles within 15 ft are forced to target the Paladin for 6s (threat set to top-of-table +20%).
- Does **not** cross [Zone Lines](../lore/dungeons/spirit-dungeon/rooms.md#zone-lines-section-barriers) — threat and taunt don't propagate through them (Ch 20, the Scarecrow pull).
- Bosses: threat bump only, no hard target lock.

**Scaling:** +5 ft radius per 5 levels; threat bonus grows with authority level.

#### Cure Light Wounds (Paladin)
- **Type:** Spell · **Level:** 1 · **Cost:** 15 mana · **Cooldown:** none · **Duration:** Instant (1s cast) · **Targeting:** Touch (ally or self)

**Rules**
- Restores 40–80 HP — deliberately weaker than the [Cleric version](cleric-of-healing.md#cure-light-wounds) (60–120). A Paladin patches; a Cleric heals.

**Scaling:** +10 HP to both ends per 5 levels.

#### Holy Light
- **Type:** Spell · **Level:** 1 · **Cost:** 5 mana + 1 mana/min upkeep · **Cooldown:** none · **Duration:** Sustained (up to ~10 min) · **Targeting:** Self (30 ft radius)

**Rules**
- Steady divine light, 30 ft radius. No damage.
- Undead and corrupted entities inside suffer −5% accuracy and will not willingly cross the lit edge unless commanded or already aggroed.
- Granted to **all holy classes** (Paladin, [Cleric](cleric-of-healing.md)).

**Scaling:** +5 ft radius and −1% additional accuracy per 5 levels; at high level begins to reveal hidden corruption (Divine Sense synergy).

#### Shield Mastery
- **Type:** Passive · **Level:** 2 · **Targeting:** Self (requires equipped shield)

**Rules**
- +15% block efficiency.
- Damage smoothing: any single blocked hit above 20% max HP is reduced by 10%.
- **Currently idle** — Clint has no shield equipped (Ch 20).

**Scaling:** +5% block efficiency per 5 levels.

#### System Aura
- **Type:** Aura · **Level:** 3 · **Cost:** toggle, 2 mana/min upkeep · **Duration:** Sustained · **Targeting:** Allies within 20 ft

**Rules**
- Hostile mental influence (charm, domination, coercion) on allies in radius is **flagged** — a System notification visible to the Paladin.
- The flagged victim immediately receives a fresh resistance check; the Paladin can force one re-check by touch.
- Stacks with other System auras (class mechanic). This is the aura protecting [Amanda](../characters/supporting/amanda.md) from re-domination.
- **Ambient [Cleanse](../magic/spells/cleanse.md) — as *correction*, not care.** The aura's integrity monitor doesn't only watch for hostile influence; it watches for **deviation from filed state**, and dirt qualifies. Blood on a tabard is unlogged material. Mud is an unauthorized modification. The aura quietly reverts it, the same way it would revert anything else that isn't supposed to be there.
- Logging: `ACTION_TYPE: INTEGRITY_MONITOR | SCOPE: PARTY` · `CORRECTIVE_ACTION: STATE_RECONCILE | DEVIATION: SURFACE_MATTER`

**Scaling:** +5 ft radius per 5 levels; Oath Mastery I (L15) amplifies range and effect.

> **Same outcome, opposite meaning.** [Wade's Cleric Aura](cleric-of-healing.md#cleric-aura) does this too, and the contrast is the joke and the characterization in one. Wade's aura cleans you because restoration is what it does and you were in range — it's care, given without being asked. Clint's cleans you because **you were out of compliance.** One of them is looking after you. The other is filing a correction.
>
> Clint does not discover this in Book 1 — though Ch 22 has him learn that *Wade's* aura does it, which is the setup. **Staged for Book 2**, after [Wade leaves](../system/xp.md) and the party has spent weeks casting Cleanse by hand: the convenience quietly returns, someone works out that it's Clint, and he pulls the log line. *"Surface matter. Deviation."* He is not sure how to feel about being told his friends were out of spec.
>
> The sequence matters — **Wade's version, then its absence, then Clint's.** The third beat only reads if the first two happened, and it should land as a cold echo of something that used to be warm.

#### Shield Bash
- **Type:** Attack · **Level:** 4 · **Cost:** 10 stamina · **Cooldown:** 12s · **Targeting:** Enemy (melee, requires equipped shield)

**Rules**
- 8–14 physical damage + 1s stun + heavy threat (top-of-table +15%).
- Stun halves against Elites; bosses are immune (threat only).
- **Currently idle** alongside Shield Mastery — no shield equipped.

**Scaling:** damage +4 per 5 levels; stun +0.5s at L10 and L20.

#### Judged Strike
- **Type:** Attack · **Level:** 5 · **Cost:** 10 mana + 10 stamina · **Cooldown:** 12s · **Targeting:** Enemy (melee)

**Rules**
- A weapon strike delivered as an enforcement action. Against an entity **currently exerting [unauthorized control](#unauthorized-control-the-classs-legal-theory)**: **+50 flat System damage**, and the hit **jolts every control channel the target maintains** — each victim immediately receives a fresh resistance check (the strike is the battlefield version of [System Aura's](#system-aura) touch re-check).
- Against anyone else it is an ordinary hit: the System evaluates, finds no grounds, applies nothing. Cooldown is still spent — filing a claim costs the same whether it's upheld.
- Inside licensed content it returns `NO GROUNDS` — the Spirit Dungeon's puppets are authorized. (Prose hook, unspent: Clint dings L5 *before* the Manager fight; a Judged Strike that comes back `AUTHORIZED CONTROL — NO GROUNDS` against a Puppet teaches the ledger in one line and plants the Eron payoff.)
- Logging: `ACTION_TYPE: ENFORCEMENT | GROUNDS: UNAUTHORIZED_CONTROL | CORRECTIVE_ACTION: CHANNEL_DISRUPTION`

**Scaling:** +10 flat damage per 5 levels; at L15+ the channel jolt applies −2 to the controller's re-establishment checks for 10s.

> **Stacked filings (design note).** An armed smite discharges on the next connecting blow — and a Judged Strike *is* a connecting blow. Smite → Judged Strike on one swing is legal and intended: at L5 that's Sanction's +30 flat / +10% weapon **plus** Judged Strike's +50 flat, with both riders (validity check + channel jolt) served in a single hit. On a whiff the smite stays armed but Judged Strike's 12s cooldown is burned — so the play is always to stop the target moving first, and *how* he does that is an era marker: bare-handed and Novice, he **grapples** ([pinned targets can't evade](../system/combat.md#grappled-and-pinned-targets)); once Celeste's sword-and-shield kit lands, **Shield Bash's stun** (L4, currently idle) does the same job without the wrestling; by L16, **Radiant Charge** does it from 30 feet. The combo never changes — only how politely he holds you still for it. Deliberate balance: Judged Strike's damage alone is ~half of what smiting the same window yields, so it never replaces smite — the jolt, not the number, is why he presses it.

#### Resolve
- **Type:** Passive · **Level:** 6 · **Targeting:** Self

**Rules**
- Stun, fear, and control effects on the Paladin run **−25% duration**. In-world: every control effect that lands on him is automatically appealed, and the appeal is usually partially upheld.
- Does not prevent application — he still gets feared; he just gets *less* of it.
- Logging: `INCIDENT: CONTROL_EFFECT | APPEAL: FILED | DURATION: REDUCED`

**Scaling:** −5% further per 5 levels (−40% at L20 with Avatar active).

#### Reinforcing Command
- **Type:** Command · **Level:** 7 · **Cost:** 15 stamina · **Cooldown:** 20s · **Duration:** 6s · **Targeting:** Area (15 ft)

**Rules**
- *"Hold the line."* Refreshes the taunt timer on every enemy currently held by [Commanding Shout](#commanding-shout) (no new targets), and allies in radius take **−10% damage** for the duration.
- The defensive half works even out of taunt range — it's a rallying order, not just threat upkeep.
- Logging: `ACTION_TYPE: REINFORCEMENT | SCOPE: FORMATION`

**Scaling:** damage reduction −2% further per 5 levels.

#### System Weapon
- **Type:** Buff · **Level:** 8 · **Cost:** toggle, 3 mana/min upkeep · **Duration:** Sustained · **Targeting:** Weapon (held)

**Rules**
- The held weapon is registered as a **System-sourced instrument**: +20% damage vs corrupted entities, system-flagged anomalies, and unauthorized summons; **all threat generated +25%**.
- Formalizes the smite glow — the "visual residue" of Authority Level 1 becomes a steady, legible light. Enemies that can read the System know what's coming; most things that need hitting can't.
- Registration follows the weapon: disarm it and the buff waits; it does not transfer.
- Logging: `INSTRUMENT: REGISTERED | SOURCE: SYSTEM | THREAT_PROFILE: ELEVATED`

**Scaling:** +5% anomaly damage per 5 levels.

#### Exception Handling
- **Type:** Buff (defensive cooldown) · **Level:** 8 · **Cost:** 20 stamina · **Cooldown:** 60s · **Duration:** 6s · **Targeting:** Self

**Rules**
- The System wraps the paladin in a handler: **damage taken −50%** for the duration.
- Any single hit that would still exceed **25% of max HP** is *caught* — reduced by **75%** instead. The killing blow becomes a logged incident: *"Exception caught. Continuing execution."*
- The hit still happens; the System catches it before it propagates. Works against **unblockable** attacks — cooldowns are the counter the block rules can't provide (see [Pink Slip](../lore/dungeons/spirit-dungeon/boss.md#ability-pink-slip)).
- The party will inevitably call it **"Try/Catch."**

**Scaling:** duration +1s per 5 levels; the catastrophic-catch threshold loosens with Oath Mastery.

> **Design note:** this is the MMO-standard tank cooldown, expressed in System vocabulary — the answer key for telegraphed tank busters. Clint is ~L5 in the [Spirit Dungeon](../lore/dungeons/spirit-dungeon/boss.md) and does not have it yet; a normal at-level party does. That gap is deliberate: his hacked HP pool substitutes for the button he hasn't earned.

#### Guardian Intercept
- **Type:** Reaction · **Level:** 9 · **Cost:** 20 stamina · **Cooldown:** 30s · **Targeting:** Ally within 15 ft

**Rules**
- One incoming single-target hit aimed at an ally is **redirected to the Paladin** — he takes it in full, with his own defenses applied (block rules included, shield permitting).
- Reaction window: declared during the attack's telegraph or travel; cannot intercept ground effects or AoE — you can't stand in front of everywhere.
- In-world: he files himself as the target of record. The System honors the paperwork; the hit never learns it was redirected.
- The normal-party answer when a tank buster retargets a squishy (see [Pink Slip's fear interlock](../lore/dungeons/spirit-dungeon/boss.md#ability-pink-slip)).
- Logging: `TARGET_OF_RECORD: AMENDED | LIABILITY: TRANSFERRED`

**Scaling:** cooldown −5s at L15 and L20.

#### Aura of Cognitive Stability
- **Type:** Aura · **Level:** 10 · **Cost:** toggle, 3 mana/min upkeep · **Duration:** Sustained · **Targeting:** Allies within 20 ft

**Rules**
- Allies gain **+4 to resistance checks** vs charm, domination, and coercion.
- **Continuous revalidation:** any ongoing mental-control effect on an ally in radius must re-win its check every **10s** or break. Control inside this aura is a subscription, not a purchase.
- Stacks with [System Aura](#system-aura): detection + forced re-check (L3) and resistance + revalidation (L10) are two layers of the same shield. Together they are what makes [Amanda](../characters/supporting/amanda.md) safe from **re**-domination at the finale — while the [installed lattice](#unauthorized-control-the-classs-legal-theory) remains untouchable, because it isn't a live effect to revalidate.
- Logging: `ACTION_TYPE: INTEGRITY_MONITOR | SCOPE: COGNITION | POLICY: REVALIDATE_10S`

**Scaling:** +1 resistance per 5 levels; revalidation tightens to 8s at L15, 6s at L20.

#### Cure Moderate Wounds (Paladin)
- **Type:** Spell · **Level:** 12 · **Cost:** 30 mana · **Cooldown:** none · **Duration:** Instant (1s cast) · **Targeting:** Touch (ally or self)

**Rules**
- Restores **100–180 HP**. Same doctrine as [Cure Light Wounds](#cure-light-wounds-paladin): deliberately below the Cleric's equivalent tier. A Paladin patches; a Cleric heals.

**Scaling:** +15 HP to both ends per 5 levels.

#### System Judgment
- **Type:** Attack · **Level:** 13 · **Cost:** 30 mana + 20 stamina · **Cooldown:** 45s · **Targeting:** Enemy (melee)

**Rules**
- The enforcement action Judged Strike grows up into. Against an entity exerting [unauthorized control](#unauthorized-control-the-classs-legal-theory): **+100 flat System damage**, and **one live control channel of the Paladin's choice is severed outright** — the victim is freed on the spot, and the controller cannot re-establish over that victim for **30s**.
- A severed necromantic puppet **drops where it stands** — the animating claim is voided, the corpse re-deads. Against [Dan's](../characters/villains/dan.md) converted raid-dead this is one person's remains given back per cast: meaningful in a fight, and it does not trivialize a screen of dozens.
- **Cuts channels, not lattices.** An installed, tetherless lattice is not a live channel; the ability will not even cast — `NO CHANNEL FOUND`. (This line is why [Amanda](../characters/supporting/amanda.md) cannot be lawyered free.)
- Refuses to cast without grounds. The System does not swing this hammer on spec.
- Logging: `CORRECTIVE_ACTION: CHANNEL_SEVERED | RE-ESTABLISHMENT: BARRED_30S`

**Scaling:** +20 flat damage per 5 levels; the re-establishment bar lengthens with authority.

#### Bulwark of Order
- **Type:** Aura · **Level:** 14 · **Cost:** toggle, 4 mana/min upkeep · **Duration:** Sustained · **Targeting:** Allies within 20 ft

**Rules**
- Party-wide damage smoothing: any single hit to an ally exceeding **15% of that ally's max HP** is reduced by **15%**.
- Spikes only — steady chip damage passes untouched. The System objects to *discontinuities*: order means nothing changes too fast.
- Stacks with his other auras (class mechanic).
- Logging: `POLICY: RATE_LIMIT | SCOPE: PARTY | SPIKE_TOLERANCE: 15PCT`

**Scaling:** reduction +5% at L20.

#### Oath Mastery I
- **Type:** Passive · **Level:** 15 · **Targeting:** Self

**Rules**
- All System auras: **+10 ft radius, +25% magnitude** (resistance bonuses, smoothing percentages, revalidation pressure).
- [Exception Handling's](#exception-handling) catastrophic-catch threshold loosens from 25% to **20%** of max HP.
- In-world: the System extends his jurisdiction. Not new powers — a bigger precinct.

**Scaling:** superseded by Oath Mastery II (post-L20, future book).

#### Radiant Charge
- **Type:** Attack · **Level:** 16 · **Cost:** 20 stamina · **Cooldown:** 25s · **Targeting:** Enemy (30 ft dash)

**Rules**
- Gap-closer: the Paladin crosses up to 30 ft in a burst of System light, striking for **40 physical damage**, stunning **1.5s**, and forcing focus for **4s** (the target attacks him).
- Bosses: stun reads as a 0.5s stagger; the forced focus is threat-only.
- The dash is *authorized transit* — it ignores difficult ground and hostile bodies but not walls. The System expedites its officer; it does not clip him through geometry.
- Logging: `TRANSIT: EXPEDITED | RESPONSE: PRIORITY`

**Scaling:** +10 damage per 5 levels.

#### Unyielding Protocol
- **Type:** Passive · **Level:** 17 · **Cooldown:** 10 min (internal) · **Targeting:** Self

**Rules**
- The first damage that would kill the Paladin instead leaves him at **1 HP**, followed by **3s of 90% damage reduction**.
- In-world: his death is a fatal exception the System **defers** — the incident is logged, the process continues, the review is scheduled for later. ([Exception Handling](#exception-handling) catches hits; this catches *endings*.)
- Logging: `FATAL_EXCEPTION: DEFERRED | PROCESS: CONTINUING | REVIEW: SCHEDULED`

**Scaling:** the post-survival window lengthens to 4s at L20.

#### Rebuke Anomaly
- **Type:** Reaction · **Level:** 18 · **Cost:** 25 mana · **Cooldown:** 45s · **Targeting:** Self (triggered)

**Rules**
- When a hostile **anomalous effect** targets the Paladin — mental control, necromantic seizure, exploit-sourced abilities, anything the System flags as outside spec — he may **suppress it entirely** and **reflect a 50%-strength copy at its source**.
- The reflection carries his authority, not the attacker's: a reflected domination attempt arrives as a *sanction* (brief stun + Enforcement-grade debuff), not as mind control — the Paladin does not get to dominate people, even on the rebound.
- Anti–[Mind Mage](mind-mage.md) tech, tier two: [Eron](../characters/villains/eron-vosk.md) casting at Clint directly is a mistake he makes exactly once.
- Logging: `EFFECT: REJECTED | ORIGIN: CITED | PENALTY: RETURNED_50PCT`

**Scaling:** reflection strengthens to 75% at L20.

#### Dominion Protocol
- **Type:** Active · **Level:** 19 · **Cost:** 40 mana · **Cooldown:** 60s · **Duration:** 20s · **Targeting:** Area (30 ft zone, centered on cast)

**Rules**
- The Paladin **files the battlefield**: a 30 ft engagement zone becomes System-sanctioned ground for 20s.
- Inside it: his auras **cannot be suppressed or dispelled**; allies resist forced movement (knockback and pull effects −50%); enemy teleports, phase-steps, and escape abilities must beat his authority check or fail.
- It does not damage anyone. It makes the ground itself take his side — the fight happens *here*, on the record, to the end.
- Logging: `ZONE: SANCTIONED | JURISDICTION: ESTABLISHED | EGRESS: RESTRICTED`

**Scaling:** duration +5s and radius +5 ft at L20.

#### Avatar of the System
- **Type:** Capstone · **Level:** 20 · **Cost:** 50 mana · **Cooldown:** once per day · **Duration:** 120s · **Targeting:** Self

**Rules**
- The Paladin becomes a **System anchor** — for two minutes, local reality treats him as infrastructure:
  - All auras: **+50% magnitude**, unsuppressable, radius doubled.
  - **Permanent threat lock:** every enemy within 30 ft treats him as top threat; even bosses cannot drop him below their top two.
  - Smite cooldowns **halved**; [Resolve](#resolve) deepens to −40%.
  - His log lines become **visible to everyone present**. *"This action is logged"* (Ch 16) was the seed; this is the tree — every swing in the finale annotated in the System's flat voice, readable by friend, enemy, and reader alike.
- Designed as the tactical spine of the [Eron](../characters/villains/eron-vosk.md) fight: a L25 Mind Mage against a L20 anchor whose party cannot be turned, moved, or taken from him for 120 seconds.
- Logging: `ROLE: ANCHOR | SCOPE: LOCAL | ALL ACTIONS ARE LOGGED.`

**Scaling:** none. This is what L20 *is*.

## Open Questions

- **"Divine Touch" (Ch 5, console era):** tentatively maps to Cure Light Wounds — mapping unconfirmed by author.
- ~~**Meta Magic (Ch 5, console era, "Legendary — Mastered"):** post-respawn status unresolved.~~ **RESOLVED 2026-08-09** — it is a **school** ([Metamagic](../magic/schools/metamagic.md)), Clint still holds the rank, and he cannot use it. The rank survived the Transition the way his stat pool did; the [proficiency](../system/proficiencies.md) behind it never existed, because it was written to his record by console rather than earned. The purest instance of his hacked-stats / Novice-hands gap — and the only ability where the gap is *total*. Prose spelling "Meta Magic" should align to **Metamagic** in the Ch 5 revision pass. Staging, the Identify block, and the *"Wait — I have that"* beat all live in [`magic/schools/metamagic.md`](../magic/schools/metamagic.md).
