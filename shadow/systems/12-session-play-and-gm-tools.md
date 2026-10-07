---
title: 12 · Session Play & GM Tools
aliases: []
type: system
summary: The play loop — small rewarding adventures out of Ferry Landing; create the scene, not the outcome. Campaign facts are read from the database, never from documents.
last-verified: 2026-10-04
source: inferred
migrated-from: https://app.notion.com/p/377e50e3bf79810aab2dd8275e3508d4
migrated-on: 2026-10-07
---

# 12 · Session Play & GM Tools

**What:** The play loop — "small rewarding adventures... go out, come back, go out one more time" (Ferrywalk shop / Ferrylanding FOB). Create the scene, not the outcome; a knowledge-based game where you prepare for threats you've studied.

**Current state:** Downtime (nutrition, Break/Rest + points, camps, Alchemy v1), Travel + Encounters (stepped travel, 138-row 2d10 biome tables, fog of war, GM cockpit), the survival loop (hunt → kill → field-dress → butcher → cook → eat), Rummage, the Targeting resolver and the holdings/facilities foundation are all in. **⚠ Biggest gap unchanged: there is nothing to find.** `loot_tables` has **never appeared in a single sync operation** across the whole change-set history — weeks at 0 rows, and not one write ever. `charge_builds` is the same: no charge has ever been assembled in the app.

**⚠ Standing rule (learned from the 07/24 correction): DB activity is NOT a proxy for play.** Read everything below as inventory, never as attendance.

**Campaign now — read from the snapshot, not from this page.** The golden facts (PCs, salt, reagents, houses, catalog counts) are in [[pcs]], [[houses]], [[companies]] and [[items]], rebuilt from `snapshot/` on every pass. The last figures written here by hand (2026-10-04): 4 PCs, all fielded — **Bledger** (Jarraxus, Berserker, salt 500, reagents 65; **died 09-18, memorialised**) · **Korven** (Shawnanigans, Berserker, salt 0, reagents 80) · **Semille** (Serenity, Ranger, salt 0, reagents 60) · **Verdant** (Gallia, Ranger, salt 0, reagents 100); companion Stinky the cattlepos. **Note on "house salt":** the DB has no separate house-ledger column — salt/reagents live on the `pcs` row itself, keyed by `house_id`. Catalog census (10-04): 81 armaments / 74 equipment / 67 consumables / 33 gear, 190 creature types, 43 locations / 11 biomes; `loot_tables` 0 and `charge_builds` 0 still.

**Sessions as data (since 2026-09-28):** a `sessions` table and a point ledger; **End session** in the ☰ menu awards 3 vocation + 3 attribute points to the PCs who played. Sessions are type-declared hubs in this web — see [[sessions]].

**Open (from the build docs):** loot-system scope (no reader on `loot_tables`); hunt `BASE_PCT=25` tuning; the shop→location name mismatch (Ferry Landing Market is attached to Riftstone, not Ferry Landing); the two-point-ledger question (wallet vs `spent_points`); the duplicate camp key on hex 139; "Find Campsite" build-or-not (`DOWNTIME_PAGE_SPEC §7b`). "???" top hunt-tier name still parked; "revenant" vs "remnant" vocab open.

**Waiting on Reece:** the loot-system scope call; hunt-odds tuning + the 11-row hunt table; the Ferry-shop naming pick; author the 61 empty consumable effects + the 18 cultivation ingredients that exist only as card text.

**Links:** Reece's 08-xx build docs (Work Queue Board · Test Guide @273 · Content Catalog · Location Page Rev 6 — in Inbox) · `library-current-state §12` · `DOWNTIME_ALCHEMY_SPEC.md` · `SESSION_HANDOFF_2026-06-12.md`

## Links

- defines → [[sessions]] (w=3, inferred)
- defines → [[encounters]] (w=3, inferred)
- defines → [[loot]] (w=3, inferred)
- defines → [[recipes]] (w=3, inferred)
- pinned → [[locations/ferry-landing]] (w=5, pinned) — the FOB
- relation → [[systems/10-companions-houses-and-pcs]] (w=3, inferred)
- relation → [[systems/13-hexicon-app]] (w=3, inferred)
