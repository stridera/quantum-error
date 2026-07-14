---
canon: true
stability: evolving
---

# Experience & Leveling

This page defines how characters gain experience points (XP) and level up.

## Core Principle: Danger

The system rewards **risk**. XP is granted for actions where the character is in genuine danger of harm or death. The greater the danger, the greater the reward. Safe actions — no matter how skillful — grant minimal or no class XP.

This single rule governs all XP calculations and prevents most forms of exploitation.

## Class XP Sources

### Combat

The primary XP source. Killing or helping kill enemies grants XP to all participants who were **in danger during the fight.** Standing in the back behind an impenetrable shield doesn't count.

- XP scales with the enemy's level relative to the participant's level. Higher-level enemies grant more XP; grey-level enemies grant almost nothing.
- XP is shared among all participants. Larger groups split more, but fighting harder enemies compensates.
- **You must be at risk.** A L99 character cannot shield a L5 character from all harm and expect the L5 to gain full XP. The system recognizes when someone is genuinely in danger vs. being carried.

### Trials (Will, Not Survival)

Some encounters threaten who you *are*, not whether you *live*. The [Mirror Room's Echo Doubles](../lore/dungeons/spirit-dungeon/mobs.md#echo-double--base-mechanic) are the archetype: their taunts deal percentage-based psychic damage that floors the target at 1 HP but **cannot kill them.** The fight is pass/fail on will and reaction — you overcome it (reward) or you don't (the [Broken](../lore/dungeons/spirit-dungeon/mobs.md#identity-crisis-phase-1) status).

Because there is no genuine danger of death, **trials grant little or no class XP.** Their reward sits on a different axis — a [Mirror Shard](../items/accessories/mirror-shards.md), self-knowledge, or a scar. [Wade](../characters/party/wade.md) took no action in his echo fight and was never at risk of dying; he walked out Broken, not dead, and no higher in level. This is why the party's dungeon leveling comes from the [bear](../lore/dungeons/spirit-dungeon/mobs.md#falling-bear), the [graveyard](../lore/dungeons/spirit-dungeon/mobs.md#scarecrow-of-the-fallow-row-graveyard-miniboss), and the boss — the fights that could actually kill them — not from the mirrors.

### Healing (In Danger)

Healers gain class XP for healing, but the amount depends on context:

- **Combat healing** (healing allies while under threat) grants significant XP — comparable to damage-dealing. The healer is in danger, their allies are in danger, and the healing is keeping people alive under pressure.
- **Safe-zone healing** (patching up sick kids, mending injuries in town) grants minimal class XP. The work is valuable, but there's no danger. A healer can level this way, but very slowly.

This is why [Wade](../characters/party/wade.md) reached L5 pre-Transition while the rest of the combat party reached L3 — he healed a large number of people, but much of it was low-danger healing that accumulated slowly. After leaving the party post-Book 1, Wade continues leveling in SF as the city's healer, but his progression slows significantly without combat danger.

### Class-Adjacent Actions

Some non-combat actions grant small amounts of class XP if they align with the class identity:

- **Bard ([Rebekah](../characters/party/rebekah.md)):** Performing music, soothing crowds, calming spirits. Grants minimal XP — there's no danger in a concert. XP increases if the performance has real stakes (calming a hostile crowd, soothing an angry spirit that could attack).
- **Rogue ([Selene](../characters/party/selene.md)):** Scouting, sneaking, stealing. Grants some XP when there's genuine risk of detection and harm. Pickpocketing a sleeping beggar: nothing. Scouting a goblin camp: real XP.
- **Sorceress ([Vanessa](../characters/party/vanessa.md)):** Buffing allies, creating illusions for shows. Minimal XP without danger. However, her Research profession may help her discover obscure spells or techniques that feed back into her class capabilities indirectly.
- **Paladin ([Clint](../characters/party/clint.md)):** Standard combat XP model. Clint's pre-Transition levels were hacked, not earned.

### Quests

System-recognized quests grant XP on completion. Quest XP typically reflects the danger involved — "kill the rats in my basement" grants less than "clear the goblin patrol from the highway."

## Leveling Curve (K1–K3)

XP required to advance **from level L to L+1**:

```
xp_to_next(L) = 50 × L × (L + 1)
```

Cumulative XP to **reach** level L is `(50/3) × (L³ − L)` (≈ cubic). Leveling is **front-loaded**: the first handful of levels cost almost nothing (L1–5 total just 2,000 XP — a few good fights, the "find your class" phase), then it steepens through the teens as the `L²`-scale term takes over, asymptoting to **~10 on-level Normal kills per level**. One smooth polynomial: no band discontinuities, consistent with the [mob framework's](mob-framework.md) "no kinks" principle. The K-bands change *what you fight* (Normals → Elites → Champions), not the curve.

| Level | To Next (L→L+1) | Cumulative to Reach |
|-------|-----------------|---------------------|
| 1 | 100 | 0 |
| 2 | 300 | 100 |
| 3 | 600 | 400 |
| 4 | 1,000 | 1,000 |
| 5 | 1,500 | 2,000 |
| 6 | 2,100 | 3,500 |
| 10 | 5,500 | 16,500 |
| 20 (≈ Book 1) | 21,000 | 133,000 |
| 33 (K1 cap) | 56,100 | 598,400 |
| 40 (≈ Book 2) | 82,000 | 1,066,000 |
| 60 (≈ Book 3) | 183,000 | 3,599,000 |
| 66 (K2 cap) | 221,100 | 4,790,500 |
| 80 (≈ Book 4) | 324,000 | 8,532,000 |
| 99 (cap, ≈ Book 5) | 495,000 | 16,170,000 |

## Pacing: ~20 Levels per Book

The scale is set so the party climbs **~20 class levels per book**, L1 → the L99 cap across the five-book arc:

| Book | Ends ~Level | Cumulative XP |
|------|-------------|---------------|
| 1 | 20 | 133,000 |
| 2 | 40 | 1,066,000 |
| 3 | 60 | 3,599,000 |
| 4 | 80 | 8,532,000 |
| 5 | 99 | 16,170,000 |

Raw XP per book grows steeply (Book 5 needs ~50× Book 1) — and that is correct: enemy XP also scales as ~level², so **income rises in lockstep with the requirement, holding *levels* per book roughly constant even as the numbers balloon.** The `L²` shape is what keeps the pace flat.

Book 1 is deliberately the **fastest**, honoring "early levels come quicker," for two reasons:

- Early per-level costs are tiny — reaching L10 is cheaper than a *single* L40 level-up.
- The boosted party spends Book 1 **punching up**: an L10 Elite is a whole level to an L3, so they close the gap in a rush before the world levels up to meet them.

Levels-per-book is ultimately a **content budget** the author controls — place ~20 levels of danger per book (the cumulative deltas above) and the curve does the rest. The [delta and danger multipliers](#xp-award-formula) are the guardrails that keep the punching-up party from lapping the pace.

## XP Award Formula

For each participant in a fight:

```
xp_gained = Σ_enemies [ mob_xp(enemy) × danger_factor × delta_mult ] × participation_share
```

- **mob_xp(enemy)** — the enemy's own value from the [mob framework](mob-framework.md): `(100 + 5·level²) × role multiplier`. Because this already grows with the enemy's level, **higher-level enemies intrinsically grant more** — no separate "punch-up bonus" is needed. An L10 Elite is worth 1,800 whether an L10 or an L3 lands the kill; for the L3 that is more than a full level, which is exactly why the boosted underdogs catch up fast.
- **delta_mult** — the grey rule, on `delta = enemy_level − your_level`:
  - `delta ≥ 0` → **1.0** (full value).
  - `−9 ≤ delta ≤ −1` → **1 + delta/10** (−10% per level below).
  - `delta ≤ −10` → **0** (grey; "almost nothing"). Anti safe-grinding.
  - *(Optional tunable: a small above-level sweetener, e.g. +5%/level capped at +50%. Off by default — the intrinsic mob_xp growth already rewards punching up, and leaving it off keeps underleveled parties from running away.)*
- **danger_factor** — the [Core Principle](#core-principle-danger) made numeric. The system measures *actual risk*, not nameplate level. A genuine-threat fight is 1.0; a **trivial-threat enemy is near 0 regardless of its level.** A swarm of L10 Whack-a-Gnomes doing 5 chip damage to a 999-HP party is not dangerous, so it grants almost no XP — which is why the party cannot power-level on a gnome fountain that never runs dry.
- **participation_share** — the pool is split among those who were **in danger** in that fight, weighted toward whoever took the most risk (the tank's share exceeds a safe backliner's). Anyone not in the fight — e.g. Clint stuck at the whack-a-gnome while the others fight the carousel — earns **nothing** from it.

### Worked Example: Clint dings L4 (Graveyard, Ch 20)

- **Pool:** 8 [Risen Skeletons](../lore/dungeons/spirit-dungeon/mobs.md#risen-skeleton) (Minion, 150) = 1,200 + [Scarecrow](../lore/dungeons/spirit-dungeon/mobs.md#scarecrow-of-the-fallow-row-graveyard-miniboss) (Elite, 1,800) + ~3 Arm Crawlers (450) ≈ **3,450**.
- delta_mult = 1.0 (all L10 vs his L3); danger_factor = 1.0 (he is tanking an Elite plus adds); risk-weighted share ≈ 25% → **~860 XP**.
- He enters the graveyard partway through L3 (cumulative ~700; the L3 band runs 400 → 1,000). +860 → ~1,560 → **crosses into L4.**
- Then the gnomes grant ~0 (no danger) and he is benched from the carousel (no participation), so his carnival XP ≈ 0; the asylum's Elites carry him to **~L5 by the end of the showroom**, and the [dungeon boss](../lore/dungeons/spirit-dungeon/boss.md) (L10 Boss, 15,000 pool) pushes him toward **~L6–7** by the time the Spirit Dungeon is cleared. See [party progression](../lore/dungeons/spirit-dungeon/rooms.md#encounter-graveyard-set).

## Profession XP

Profession XP is **completely separate** from class XP. Crafting, gathering, building, researching — these advance profession rank but do not contribute to class level.

- [Enchanting](../professions/enchanting.md) an item grants Enchanting profession XP. Zero class XP.
- Harvesting herbs grants Herbalism profession XP. Zero class XP.
- Forging a sword grants Blacksmithing profession XP. Zero class XP.

This is why [Celeste](../characters/supporting/celeste.md) is a Grandmaster Blacksmith but only L5 Barbarian — she's spent years at the forge, not in the field. Her profession is maxed; her class is barely started.

Classless characters can still gain profession XP normally. A classless Master Enchanter has no class level but is highly skilled at their craft.

## Anti-Exploitation

The danger requirement prevents common power-leveling exploits:

- **Shielding:** A high-level character can't make a low-level character immune to damage and feed them XP. The low-level character must be genuinely at risk.
- **Zone leeching:** Being in the same zone as your party while they fight grants nothing. You must be in the fight, taking risk.
- **Safe grinding:** Repeatedly killing enemies far below your level grants negligible XP. The system scales rewards by level delta — if it's not dangerous, it's not worth much.

## Pre-Transition XP

The system was active before the Transition completed. Actions during the pre-Transition events granted XP normally:

- The party collectively killed approximately two dozen of [Eron Vosk's](../characters/villains/eron-vosk.md) soldiers across multiple fights → L3 for combat participants.
- [Wade](../characters/party/wade.md) split off to heal sick children and others → L5 (accumulated healing XP, both from danger-adjacent situations and large volume of safe healing).
- [Clint](../characters/party/clint.md) remained L1 — his Paladin class was [locked](classes-and-professions.md#locked-classes) without a patron god, so XP couldn't apply to class leveling. His Grandmaster Enchanter rank was hacked through direct system access.
- The first [death](death.md) at IQuantum was a freebie — the system was still initializing.
