---
title: 09 · Political Engine & Factions
aliases: []
type: system
summary: One graph / two views; two-week simultaneous-blind faction turns; faction stats ARE resources; factions transform rather than die.
last-verified: 2026-09-06
source: inferred
migrated-from: https://app.notion.com/p/377e50e3bf7981518074d96014a96fea
migrated-on: 2026-10-07
---

# 09 · Political Engine & Factions

**What:** One graph / two views; two-week simultaneous-blind faction turns; faction stats ARE resources; factions transform rather than die. Founding philosophy (Nov 2025, day one): "There aren't really bad guys... different factions."

**Current state:** Design phase. Faction = social structure answering a societal question; values-with-shadows drive negotiation; governance-from-purpose. Church soul web mostly canon (roads ARE the web, life-force taxation, corpse-golem labor; soulstone details open). Faction shop tables canon. Druid Circle session (6/07, canon): the Circle is anarchist — elders counsel, never command; Sensates are also elders but judge and command ("same thing, different expression"); Church = the Circle's foil; the Guild (capitalism = inherently extractive) = its rival. Circle×Academy relationship = open, parked for a Lore Room convening. Lost factions returning eventually: Industrial Incursion(→Guild?), River Pirates boat-city, the Resistance, War Mind, Mimics + elder cycle. **Character-book units (6/26):** 9 named retinue templates — Iron Band, Fletcher's Co-op, Blood Badgers, Ash Grove, Exiled Chapter, Keethee, Fungal Research Unit, Eternal Chapter, Black Company — now spawn as roster units; faction reputations + Eternal Chapter faces parked.

**App DB:** the application carries **5 faction rows** — The Underworld, The Runites, The Sensates, The Guild, The Druidic Circle — the first faction data to land in the app (design still pre-build). "The Underworld" / "The Runites" read as new vocab — confirm before they become canon (**asked 08-09 and 08-16, still open**). See [[factions]].

**New 08-22 (DB 8/23, schema 333) — attitude is now a stored fact.** A `retinue_stances` table recorded, per save, how one roster group regards another (viewer group → target group → stance); it held one row, `hostile`. **New 08-24→08-27 — a sixth faction, and attitude changed shape.** **RULED 08-24 (Reece): the batkin are an explosives + firearms faction**, and the opposition for the **09-04** session — the first faction defined by its technology rather than its social question, and the first to arrive as an army before it arrives as a politics. Meanwhile `retinue_stances` went back to **0 rows**, and a **`hostility`** column appeared instead on `roster_groups`, `retinue_templates` and `roster_instances`. **Claude's read, not canon:** that is a move from *pairwise* attitude (A regards B) to a *per-group flag* (this group is hostile, full stop) — fine for running a fight on the grid, but it cannot express the one-graph/two-views design or values-with-shadows negotiation. If the pairwise table is meant to survive, it needs saying before the flag becomes the habit.

**🔨 PARKED SESSIONS:** Stability stat ("feels off"); negotiation stack reconciliation (Patience/Interest × 12→6 value pairs × Believer/Idealist/Shadow/Defector).

**Waiting on Reece:** both sessions; the Underworld / Runites vocabulary confirmation.

**Links:** `library-current-state §5` · `library-2026-01-02.md` (soul web, negotiation genesis) · Parking Lot (Notion, https://app.notion.com/p/34be50e3bf7981c8812ec35505694697)

## Links

- defines → [[factions]] (w=3, inferred)
- defines → [[retinues]] (w=3, inferred)
- defines → [[branches]] (w=3, inferred)
- relation → [[systems/07-species-and-bestiary]] (w=3, inferred) — the batkin
- relation → [[systems/08-ecology-engine-and-hex-profiles]] (w=3, inferred) — one graph, two views
- relation → [[systems/10-companions-houses-and-pcs]] (w=3, inferred)
