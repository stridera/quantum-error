---
canon: true
stability: evolving
---

# System UI

This page defines the user interface that characters see after the Transition, how they interact with the system, and the exception that applies to [Clint](../characters/party/clint.md).

## The Standard Interface

When the Transition completes, every person receives a full system UI — a mental overlay projected into their field of vision. It appears immediately and without instruction. People just *have* it, like waking up with a new sense.

The UI is the system's way of making itself legible to humans. It translates raw system data (stats, health, mana, effects) into visual elements that people can read at a glance.

### HUD Elements (Always Visible)

- **Health Bar:** Current / Max HP. Changes color as health drops (green → yellow → red).
- **Mana Bar:** Current / Max mana. Blue. Visible only for characters with a mana pool.
- **Endurance Bar:** Current / Max stamina. Yellow/amber. Depletes with physical exertion.
- **Status Icons:** Active buffs and debuffs displayed as small icons with duration timers. Can be inspected for details (see [UI Popups](ui-popups.md)).
- **Combat Indicators:** In combat, a subtle border or tint signals active engagement. Threat indicators show which enemies are targeting you.

### Party Frames

When in a group, small health/mana bars for each party member appear in a configurable position. Shows name, level, class icon, and current HP/mana percentage. Enough to know who's hurt — not enough to diagnose what's wrong without looking closer.

### Menus (Opened on Demand)

- **Character Sheet:** Full stat breakdown — attributes, derived stats, resistances, profession ranks. Opened by mental intent ("I want to see my stats").
- **Inventory:** Grid of carried items. Equipment slots. Encumbrance. Weight.
- **Ability List:** All known abilities with descriptions, costs, and cooldowns. See [UI Popups](ui-popups.md) for the format.
- **Quest Log:** Active quests with objectives and progress. Quests appear here when accepted.
- **Map:** Area map showing explored terrain. Does not reveal unexplored areas. No GPS-style tracking — you see where you've been, not exactly where you are. Landmarks and safe zones are marked.
- **Inspect:** Focus on another person or creature to see basic information — name, level, class (if visible), health bar. Higher-level or hidden information requires specific abilities or skills to reveal.

### Notifications

The system pushes notifications for significant events:
- Level up
- New ability unlocked (see [UI Popups — New Ability](ui-popups.md#1-new-ability-earned))
- Quest updates
- [Death](death.md) and respawn
- System-wide announcements (rare)

These appear as popup windows that can be dismissed or reviewed later.

### Interaction Model

The UI responds to **mental intent**. There are no physical gestures, voice commands, or button presses. You think "open inventory" and it opens. You think "close" and it closes. You focus on a status icon and the detail popup appears. It's intuitive — the system reads intent, not specific words.

People can customize the UI to a degree — repositioning elements, adjusting opacity, hiding non-essential information. Most people leave it at defaults because they don't know they can change it.

## Clint's Exception: Instinctual Access

[Clint](../characters/party/clint.md) does not have the standard UI. His [Paladin of the System](../classes/paladin-of-the-system.md) class and direct system interface replace it with something fundamentally different: **instinctual knowledge**.

### What He Sees

Nothing. No health bar, no mana bar, no floating icons, no menus. His field of vision is clean — just the world as it is.

### What He Knows

Clint doesn't *see* his health — he **feels** it. Not pain (though pain exists), but a bone-deep awareness of how much damage he can take before he drops. He doesn't check his mana bar — he knows how much he has left the way you know how tired you are. He doesn't open a character sheet — he knows his own capabilities the way a trained athlete knows their body.

This extends to everything the standard UI would show: stats, abilities, cooldowns, active effects. The information is there. He just accesses it differently — not through a visual layer, but through direct knowledge.

### Inspect (Book 1)

In Book 1, Clint must **actively think** about inspecting something to get information about it. He looks at a person and thinks "what are they?" and the knowledge surfaces — their level, class, health, whatever the system would reveal to an Inspect action. It takes conscious effort and a moment of focus.

This is equivalent to the standard UI's Inspect function, but without the visual popup. The information arrives as *knowing* rather than *reading*.

### Progression: Passive Awareness

Over time, Clint's instinctual access deepens. The conscious effort of Book 1 gives way to passive awareness:

- **Book 1:** Manual. He has to think to inspect. Information comes when requested.
- **Later books:** Increasingly automatic. He walks into a room and *knows* the level of every creature in it. He glances at an ally and knows their health, their mana, their active debuffs — without asking. Threats register before he consciously identifies them.
- **Endgame:** Full passive system awareness. He perceives the system the way the system perceives itself. He doesn't read the world — he *understands* it. Think Neo seeing the Matrix.

This progression is one of Clint's defining strengths. The standard UI gives everyone the same information, but Clint's instinctual access is faster, deeper, and eventually reveals things the standard UI can't show.

### Advantages Over Standard UI

- **Speed:** No menu navigation, no reading text. Knowledge is instant.
- **No visual clutter:** His field of vision is never obstructed by interface elements. In combat, this matters — he sees the fight, not a HUD overlaying the fight.
- **Depth:** As his access matures, he perceives system-level information that the UI simplifies or hides from normal users. The UI is a translation layer; Clint eventually bypasses the translation entirely.
- **Cannot be disrupted:** Effects that scramble or disable the UI (if such things exist) don't affect Clint. His access is direct, not mediated through the interface layer.

### Disadvantages

- **Communication gap:** Clint can't easily share what he knows with party members who expect UI-formatted information. He says "that thing is level 22" when others would just Inspect and see a health bar. His knowledge doesn't translate into the visual language everyone else uses.
- **Early learning curve:** In Book 1, the manual inspection is slower and less convenient than just glancing at a health bar. Other characters can see party frames at a glance; Clint has to check each person individually until his passive awareness develops.

## Design Notes

The standard UI exists to make the LitRPG mechanics legible to both characters and readers. When the prose describes what a character sees in their UI, it should follow the formatting conventions in [UI Popups](ui-popups.md).

Clint's instinctual access is a narrative tool — it lets the prose describe his system knowledge as *feeling* rather than *reading*, which differentiates his perspective from other characters. Scenes from other characters' POV should describe UI elements naturally (health bars, popups, menus).

**Prose convention:** Stat blocks and [UI popups](ui-popups.md) still appear in the prose during Clint's POV. These represent what Clint *knows* — formatted for the reader's benefit, not because Clint is reading a screen. The goal is to show the same information other characters would see in their UI, but filtered through Clint's instinctual understanding. The writing around the stat blocks should reflect this — Clint doesn't "open his character sheet," he just *knows*, and the stat block is how the novel presents that knowledge to the reader.
