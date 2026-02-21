---
canon: true
stability: evolving
---

# Economy

This page defines how currency, trade, and the system-driven economy work after the Transition.

## Currency: Gold

The system uses a single currency: **gold.** Old-world money (dollars, euros, etc.) is worthless paper. Gold is the universal medium of exchange, created and managed by the system.

Gold is **system-tracked.** Each character has a gold balance visible in their [UI](ui.md). Transactions in safe zones are instant — when you buy a sword, the gold transfers automatically. No counting coins, no making change. The system handles it.

### Where Gold Comes From

- **Mob drops:** Enemies drop gold when killed. The gold is physical on the mob's body and auto-converts to system gold when looted. Higher-level mobs drop more.
- **Quest rewards:** The system pays gold for completed quests — combat quests, profession quests, civic quests. This is how non-adventurers earn gold.
- **System bounties:** Standing offers from the system for specific tasks (clear this area, deliver these supplies, craft these items).

### Where Gold Goes

- **Goods and services:** Food, gear, materials, housing, professional services (repairs, [corpse summoning](death.md), binding, etc.).
- **System buy-orders:** The system is the economy's largest customer. Every profession has standing system quests to produce goods — "forge 10 swords," "brew 20 potions," "grow 50 bushels of wheat." Crafters sell to the system at fair prices, creating a reliable income floor and a consistent gold sink.
- **Materials:** Crafters buy raw materials to produce goods. Higher-tier crafting requires increasingly expensive materials, scaling gold drain with profession rank.
- **Repair costs:** Gear degrades with use. Repairs cost gold. Active adventurers spend more on repairs than anyone — a natural drain on the heaviest gold earners.
- **Consumables:** Potions, food buffs, ammunition, and other single-use items are a steady gold drain.

### The Loop

The system functions as both central bank and largest employer. It creates gold (mob drops, quest rewards) and absorbs gold (buy-orders, material vendors, services). This closed loop keeps gold circulating without hyperinflation, as long as the system calibrates its inputs and outputs.

```
  System creates gold          System absorbs gold
  ┌─────────────────┐          ┌──────────────────┐
  │ Mob drops        │          │ System buy-orders │
  │ Quest rewards    │ ──gold──▶│ Material vendors  │
  │ System bounties  │          │ Repair costs      │
  └─────────────────┘          │ Services/fees     │
         │                     └──────────────────┘
         ▼                              ▲
  ┌─────────────────────────────────────┐
  │          Player Economy             │
  │  Adventurers ──▶ Crafters ──▶ Goods │
  │  Farmers ──▶ Food ──▶ Everyone      │
  │  Miners ──▶ Materials ──▶ Crafters  │
  └─────────────────────────────────────┘
```

## Transactions

### Safe Zone Commerce

In safe zones, all transactions are system-mediated:

- **Instant transfer.** Buyer and seller agree on a price, gold moves automatically.
- **Theft prevention.** You can't walk out of a shop with goods you haven't paid for — the system blocks it or auto-deducts. Safe zones are functionally theft-proof for commerce.
- **No haggling with the system.** System buy-orders and vendor prices are fixed. Player-to-player prices are negotiable.

This creates a **utopian commercial environment** in safe zones. No robbery, no fraud, no counterfeiting. People focus on producing and trading, not protecting their money.

### Outside Safe Zones

The system's commercial protections don't extend beyond safe zone boundaries. Gold on mobs is physical until looted. Rogue abilities like pickpocketing work on NPCs and mobs in the wild. Bandit NPCs can take your gear (though not your system gold balance — that's always safe).

## Barter Period

In the first days after the Transition, gold meant nothing. People bartered — food for labor, medicine for shelter, tools for protection. The barter period was brief. As mobs started dropping gold and quests started paying it, people naturally adopted the system currency because it was universal and reliable. Within weeks, gold was the standard.

## Profession Economy

The system actively sustains professions through quest-based demand:

- **[Builders](../lore/overview.md#profession-translation)** get quests to maintain and fortify structures. Paid in gold and profession XP.
- **Farmers** get quests for seed and cultivation. Sell produce to other residents and the system.
- **[Blacksmiths](../characters/supporting/celeste.md)** buy metal from miners, forge weapons and armor, sell to adventurers and fill system buy-orders.
- **[Enchanters](../professions/enchanting.md)** buy base items from crafters, enchant them, sell the finished product at a premium.
- **Miners, tanners, weavers, etc.** feed raw materials into the crafting chain.

Every profession has a place in the loop. The system ensures demand exists even when player demand is low — if nobody needs swords this week, the system still has buy-orders. This prevents any profession from becoming economically unviable.

## Pricing (Rough Scale)

Exact prices are flexible, but the general magnitude:

| Category | Example | Gold |
|----------|---------|------|
| Trivial | A meal, basic supplies | 1-5 |
| Cheap | Simple tools, common ingredients | 5-20 |
| Moderate | Basic weapon, common armor, a night at an inn | 20-100 |
| Expensive | Quality weapon, good armor set, professional services | 100-500 |
| Very Expensive | Rare materials, enchanted gear, specialized services | 500-5,000 |
| Extravagant | Master-crafted equipment, property, rare enchantments | 5,000+ |

These are rough anchors, not a price list. The system adjusts dynamically based on supply and demand.

## Design Notes

The economy is designed to be **invisible in the prose** most of the time. Gold exists, things cost money, people earn a living — but the novel shouldn't read like an accounting ledger. The system-tracked gold and instant transactions allow commerce scenes to focus on the *what* (Celeste forges a sword, the party buys supplies) rather than the *how* (counting coins, making change).

The system-as-customer model means every crafter has a floor income and every profession is viable. This supports the safe-zone-as-functional-society worldbuilding without requiring the novel to explain macroeconomics.
