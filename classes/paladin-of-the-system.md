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
| 1 | Smite: Judgment | Attack Modifier | See Smite Progression below |
| 2 | Shield Discipline | Passive | Improved block efficiency and damage smoothing |
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

**Design Notes**: Functionally similar to a normal paladin's early smite, but crucially different in execution path. Clint can (and will) use this on every landed hit early. No system instability yet—only observation. *This is `sudo ls`. Same result. Different context.*

---

### Level 4 — Smite: Sanction

*Upgrades Smite: Judgment automatically*

| | |
|---|---|
| **Cost** | 15 Mana |
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
