---
canon: true
stability: locked
last_reviewed: 2026-02-05
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
| 1 | Commanding Shout | Command | Forces nearby hostiles to focus on you; overrides threat priority |
| 1 | Cure Light Wounds | Spell | Restore health to a living target |
| 1 | Holy Light | Spell | Conjure steadfast divine light; undead and corrupted entities flinch from its radius. Granted to all holy classes. |
| 1 | Smite: Judgment | Attack Modifier | See Smite Progression below |
| 2 | Shield Mastery | Passive | Improved block efficiency and damage smoothing |
| 3 | System Aura | Aura | Hostile mental influence becomes detectable and interruptible |
| 4 | Shield Bash | Attack | Strike with shield, stunning target and increasing threat |
| 4 | Smite: Sanction | Upgrade | Smite: Judgment upgrades automatically |
| 5 | Judged Strike | Attack | Increased damage to entities exerting unauthorized control |
| 6 | Resolve | Passive | Reduced duration of stun, fear, and control effects |
| 7 | Reinforcing Command | Command | Refreshes taunt effects and bolsters allied defenses |
| 7 | Escalating Sanctions | Passive | Smite stacks debuff on repeated hits |
| 8 | System Weapon | Buff | Weapon gains anti-anomaly properties and enhanced threat generation |
| 9 | Guardian Intercept | Reaction | Redirect incoming damage from an ally to yourself |
| 10 | Aura of Cognitive Stability | Aura | Allies gain resistance to charm, domination, and coercion |
| 11 | Smite: Enforcement | Upgrade | Smite: Sanction upgrades automatically |
| 12 | Cure Moderate Wounds | Spell | Restore a greater amount of health |
| 13 | System Judgment | Attack | Punishes entities exerting unauthorized control or coercion |
| 14 | Bulwark of Order | Aura | Party-wide damage smoothing and reduced spike damage |
| 15 | Oath Mastery I | Passive | Increases range and effectiveness of all active System auras |
| 15 | Harmonized Enforcement | Passive | Aura-Smite synergy |
| 16 | Radiant Charge | Attack | Gap-closer that stuns target and forces focus |
| 17 | Unyielding Protocol | Passive | Prevent death once when damage would be fatal |
| 18 | Rebuke Anomaly | Reaction | Reflect or suppress hostile anomalous effects |
| 19 | Dominion Protocol | Passive | Control over System-sanctioned areas and engagement zones |
| 19 | Smite: Verdict | Upgrade | Smite: Enforcement upgrades automatically |
| 20 | **Avatar of the System** | Capstone | Become a System anchor; all auras amplified and cannot be suppressed; permanent threat lock |

---

## Smite Progression (Canonical)

Smite is **privileged from Level 1**. Clint does not learn new smites—he is trusted with more consequences. The same smite call grows more dangerous over time.

> **Naming note:** early prose (Ch 5, console era) calls this ability **"Divine Strike"** — same smite, pre-activation name. Prose revision may align the name later; treat Divine Strike ≡ Smite: Judgment.

> "I didn't change what I was doing. The system changed what it allowed me to do."

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
- While Combat Alignment or Truth Radius is active:
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

### Smite Philosophy
- Smite is privileged from Level 1
- Early smite is frequent and necessary
- Power comes from authority depth, not spam
- The same smite call grows more dangerous over time

## Notable Paladins

- [Clint](../characters/party/clint.md)

## Ability Stat Blocks

> Blocks below cover the kit shown in prose through Ch 21 (smites live in [Smite Progression](#smite-progression-canonical)). Remaining abilities gain blocks as they enter the story. Costs assume the **Low mana group** (L1 ≈ 15, L10 ≈ 55 — see [stat progression](../system/stat-progression.md)); Clint's hacked 999 pool makes them trivial for him, which is the point.

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

- **"Divine Touch" (Ch 5, console era):** tentatively maps to Cure Light Wounds — mapping unconfirmed by author.
- ~~**Meta Magic (Ch 5, console era, "Legendary — Mastered"):** post-respawn status unresolved.~~ **RESOLVED 2026-08-09** — it is a **school** ([Metamagic](../magic/schools/metamagic.md)), Clint still holds the rank, and he cannot use it. The rank survived the Transition the way his stat pool did; the [proficiency](../system/proficiencies.md) behind it never existed, because it was written to his record by console rather than earned. The purest instance of his hacked-stats / Novice-hands gap — and the only ability where the gap is *total*. Prose spelling "Meta Magic" should align to **Metamagic** in the Ch 5 revision pass. Staging, the Identify block, and the *"Wait — I have that"* beat all live in [`magic/schools/metamagic.md`](../magic/schools/metamagic.md).
