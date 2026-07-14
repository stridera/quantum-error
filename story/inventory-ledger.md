---
canon: true
stability: evolving
last_reviewed: 2026-07-03
---

# Inventory Ledger

The party's gear changes constantly — looted, gifted, upgraded, stashed, lost. This file is the **temporal source of truth** for who has what, where they got it, and where it went. It exists because a single "Equipment" list on a character page can't answer "what was Clint wielding in Chapter 17?" or "does he still have the machete after he gets a real sword?" (Answer: yes. He keeps everything. That's the point of a bag of holding.)

## How this works — two layers

1. **Current Party Loadout** (below) — a snapshot table of what everyone has *right now* (latest chapter). This is the at-a-glance answer.
2. **Acquisition & Transfer Log** (below) — an append-only, chapter-keyed event log. This is the *history*. Never delete a row; when an item changes hands or state, add a new row.

Each party page also carries a short **Equipment & Inventory** section listing current equipped items. When those two disagree, **this ledger wins** — update the character page to match.

**Upgrades don't erase the old item.** When Clint eventually gets a real sword, the machete doesn't vanish — the new sword becomes his equipped Weapon and the machete moves to *Carried (backup)*. Record the upgrade as a new log row; the machete keeps its own row. The bag of holding means the party accumulates, it doesn't replace.

### Event types (for the log)

`Crafted` · `Found`/`Looted` · `Bought` · `Given` (party transfer) · `Equipped` · `Unequipped` · `Stashed` (into a bag of holding) · `Dropped` · `Lost` (death/theft/destruction) · `Reclaimed`

---

## Current Party Loadout

*Snapshot as of **Chapter 18** (Spirit Dungeon, post–Mirror Room). Item states in flux this chapter are flagged.*

| Character | Weapon | Off-hand / Focus | Worn (Body) | Head / Accessory | Bag | Companion |
|---|---|---|---|---|---|---|
| **[Clint](../characters/party/clint.md)** | Prop Machete (Common, 4–7 phys; faint Attunement glow) | — *(Aegis away)* | Pirate outfit (costume-rack, Common) | Singed Fedora | **[Fanny Pack of Holding](../items/accessories/fanny-pack-of-holding.md)** (Legendary, soulbound) | — |
| **[Selene](../characters/party/selene.md)** | Prop Cutlass (Common, 5–8 slashing) | — | starting rogue clothes *(declined the Scream Robe)* | — | — | [Prize Mimic](../items/accessories/mimic-pet.md) (pet) |
| **[Vanessa](../characters/party/vanessa.md)** | — *(spells)* | — | Robe of the Silent Judgement (Ch 16) ⚠️ *name not yet in summary prose* | — | — | — |
| **[Wade](../characters/party/wade.md)** | — *(cleric)* | — | starting clothes | Nurse's Cap (Uncommon, +5% healing) | — | — |
| **[Rebekah](../characters/party/rebekah.md)** | — *(songs of light, innate)* | — | starting clothes | — | — | — |

**Shared / soulbound:** **four of the five** carry a [Mirror Shard](../items/accessories/mirror-shards.md) pendant (soulbound, evolving), earned facing their echo in the Mirror Room. **Wade failed his echo** and did *not* earn the Shard of Devotion — recoverable at a future Spirit Dungeon (see [Away Items](#away-items)).

⚠️ **Flagged as in-flux or unstaged** — see [Open Threads](#open-threads--needs-staging).

---

## Away Items

Items that exist in canon but are **not currently held** — record them here so they're never forgotten and their return can be tracked.

| Item | Owner | Where it is | Returns |
|---|---|---|---|
| [Katsuragi, the Singularity Blade](../items/weapons/katsuragi.md) | Clint | Ancient Red Dragon's hoard, with the [Tablet of Annihilation](../lore/tablet-of-annihilation.md) | Reclaimed at **series finale** (L99) |
| [Aegis of Decoherent Deflection](../items/armor/aegis-of-decoherent-deflection.md) | Clint | Ancient Red Dragon's hoard, with the Tablet | Reclaimed at **series finale** (L99) |
| Rebekah's guitar | Rebekah | Destroyed (sniper fire, Ch 13) | Never — replaced by innate songs-of-light |
| [Shard of Devotion](../items/accessories/mirror-shards.md#shard-of-devotion--wade-not-earned) | Wade | Never earned — failed his echo (Ch 18) | Recoverable at a **future** Spirit Dungeon (over-leveled Wade clears it for his shard) |

---

## Acquisition & Transfer Log

Chronological. Append new rows; never rewrite history.

| Ch | Item | Character | Event | Location / Source | Notes |
|----|------|-----------|-------|-------------------|-------|
| 8 | Fanny Pack of Holding | Clint | Crafted | Pre-Transition, Enchanting + console | Legendary, soulbound. First legendary he made. |
| 8 | Katsuragi (sword) | Clint | Crafted | Pre-Transition, Enchanting + console | Unique-tier (console exploit), not Legendary. |
| 8 | Aegis (shield) | Clint | Crafted | Pre-Transition, Enchanting + console | Unique-tier (console exploit), not Legendary. |
| 13 | Rebekah's guitar | Rebekah | Lost | iQuantum HQ, sniper fire | Destroyed. She later plays songs of light instead. |
| 13–14 | Katsuragi | Clint | Lost | Transition / first death | Not soulbound — did not persist through respawn. Ends up in dragon's hoard. |
| 13–14 | Aegis | Clint | Lost | Transition / first death | Not soulbound — did not persist through respawn. Ends up in dragon's hoard. |
| 13–14 | Fanny Pack of Holding | Clint | Retained | Respawn (San Francisco) | Soulbound — the **only** gear that survived death. |
| 15–16 | (Clint's clothes) | Clint | Lost | Spirit Dungeon, Room 1 | Burned off by Vanessa's fireball. → towel. |
| 15–16 | Robe of the Silent Scream | Clint | Looted | Spirit Dungeon, Freddy/Scream mannequin | Common, +2 AR, dark hooded robe. "Better suited for Selene." |
| 16 | Robe of the Silent Judgement | Vanessa | Looted | Spirit Dungeon | Vanessa's caster robe. Name not yet in summary prose — see Open Threads. |
| 17 | Prop Cutlass | Selene | Looted | Spirit Dungeon, Sexy Pirate Mannequin | Common, 5–8 slashing. "Selene keeps it." |
| 17 | Nurse's Cap | Wade | Looted | Spirit Dungeon, Sexy Nurse Mannequin | Uncommon, +5% healing. Wears it anyway. |
| 17 | Robe of the Silent Scream | Clint | Damaged | Spirit Dungeon, Bear Trap encounter | Slashed deep across the chest — leaves it revealing. (Prose currently has a *falling bear* maul Clint, not the trap jaws; see Open Threads.) |
| 18 | Mirror Shard ×4 | Clint, Selene, Vanessa, Rebekah | Looted | Spirit Dungeon, Mirror Room echoes | Soulbound pendants. **Wade failed his echo — no Shard of Devotion.** |
| 18 | Pirate outfit | Clint | Equipped | Spirit Dungeon, costume rack | Common. Clint's current worn outfit. |
| 18 | Costume stack | Clint | Stashed | Spirit Dungeon, costume rack | Remaining costumes stashed in the Fanny Pack "for emergency use." |
| 18 | Robe of the Silent Scream | Clint → Selene | Offered, declined | Spirit Dungeon | Clint offers the (slashed) robe to Selene after donning the pirate outfit; she politely refuses — too revealing. Clint stashes it in the Fanny Pack, **promising to get it repaired for her.** (Repair-and-return is a pending future beat.) |
| ~19 | Prize Mimic | Selene | Won | Spirit Dungeon, Carnival (500 tickets) | Companion/pet, not a container — see [mimic-pet](../items/accessories/mimic-pet.md). |

---

## Open Threads / Needs Staging

Details established by the author but **not yet fully written into prose** — flagged so they can be surfaced in a scene rather than silently assumed.

- **Live grenade in the Fanny Pack.** ⏳ *Undecided.* An old-world (pre-Transition) item Clint is carrying; the author may **retcon** its placement and is weighing it as a **MacGuffin for later** — or dropping it. Recorded on Clint's page as tentative until that call is made.
- **Chest slash on the Robe of the Silent Scream** *(reconciliation)*. Origin is set: the **Ch 17 Bear Trap encounter** cut deep across the chest, leaving the robe revealing. Note the current prose has a *falling bear* Maul Clint (the trap jaws deliberately don't snap) — a line tying the chest wound/robe-tear to that encounter would make it explicit.
- **Vanessa's Robe of the Silent Judgement** *(name)*. Established as her Ch 16 caster robe, paired with Clint's Robe of the Silent Scream. The name isn't in the Ch 15/16 summaries yet ("they loot robes") — surface it there when convenient.

- **Repair-and-return of the Robe of the Silent Scream** *(future beat).* Clint stashed the slashed robe promising to get it repaired for Selene. Pays off when it's mended and she accepts it — needs a repair source (Clint's [Enchanting](../characters/party/clint.md)? a vendor?) and a return scene.

**Resolved:** ~~The Scream Robe handoff~~ — Clint offers the slashed robe to Selene (Ch 18); she politely declines (too revealing). He stashes it, promising a repair. Selene is in her starting rogue clothes; she may still pick up class-appropriate gear from the costume aisle (optional, unstaged).

### Unassigned dungeon loot

Referenced as available in the Spirit Dungeon but not yet given to anyone in prose: **Treat Bag of Holding**, **Bear Claw Necklace** (+1 STR). Assign or drop.
