---
title: 03 · Items, Materials & Economy
aliases: []
type: system
summary: Four item DBs (Armaments / Equipment / Consumables / Gear); items link into the Effects Engine — the weapon is purely the physical object.
last-verified: 2026-09-06
source: inferred
migrated-from: https://app.notion.com/p/377e50e3bf798139a432c71b5083bdf5
migrated-on: 2026-10-07
---

# 03 · Items, Materials & Economy

**What:** Four item DBs (Armaments / Equipment / Consumables / Gear; shields = armaments); items link into the Effects Engine — the weapon is purely the physical object.

**Current state:** Currency = open faction-indexed set. Live today: **Salt Cubes + Reagents as liquid currency** (salt is now app-tracked, not paper). Faction consumables = payment, never tradeable currency. **Gold→Salt 1:1 LOCKED (6/07)** — Oct-2025 anchor prices ARE Salt prices. **Reagent economics canon (6/07):** reagents = egalitarian currency produced through alchemy. **Alchemy v1 shipped (mig 162):** six T1 base cards (Tar = renamed Steady Coating), reagent YIELD +2/+5/+10, net-zero Dim/Base/Enh adjustment, brews mint as real items, Alchemist's Kit + tar-base crafting. **41-item catalog imported** (explosives/brews/tack/saddlebags/cart upgrades); per-item **salt_value editor** (Reece authors values). **6/26 character-book catalog:** +31 items (21 NPC gear incl. 6 tattoos + 10 Rathos anomalous gifts); live catalog (DB 09-06, schema 361) **81 armaments / 74 equipment / 67 consumables / 23 gear**; weights/values still placeholder. The 08-24 week's additions were all ordnance — Powder Keg and Separator's Bench in equipment, and the Frag / Impact Frag / Sticky Frag grenades, Mining / Tree Ripper / Timed charges and Exploding Arrows re-stamped as consumables. **Nothing drops:** `loot_tables` is created but holds **0 rows**, and `recipes` is empty, so the only item entering play from the world is hunted meat.

**NEW 08-17→08-22 — a composable EXPLOSIVES materials system (migs 285–333), the first real materials layer in the app.** A charge is assembled from four authored tables rather than being a single item: **`powder_kinds`** (3 — Black Powder d4/L Force, ignores armour; Hearth Powder d6/L Heat, goblin-made, armour still counts; Smoke Powder, 4 m² light smoke per litre and no damage), **`filler_kinds`** (6 — Rocks d10 · Musket Balls d6 · Glandes d6 · Ball Bearings d4 · Caltrops d4 · Nails d4, each with a kg/L density so mass trades against reach), **`charge_containers`** (now **18** — 8 wood, Jug 4 L → Tun 512 L, plus **10 clay added 08-24**, Phial → Clay vat, each with empty weight + integrity), and **`container_materials`** (Wood: burns, heat ×2, d4 splinters · Clay: shatters, concussive ×2, d6 shards). A **`fuse_cordages`** table (4) joined them — see [[systems/04-combat-and-resolution]]. Also new: the **Goblin Glass** armament line, and a **`tags`** vocabulary whose first entry is `Person` — "a people, not an animal; cannot be field dressed or butchered," i.e. the butchering gate is now data, not GM judgement.

**Reece's 08-24 rulings on this system (canon):** charges are **crafted dynamically** — fill a container with powders and fillers, then mix; **powders and fillers are stored like liquids**, in bulk, in containers. He wants **sacks, glass containers, metal casings and tubes** added as container types — *not built* (materials are still only wood and clay). ⚠ **The in-DB flavour text is NOT canon:** Reece confirmed a build session generated the powder / filler / container descriptions; they are placeholder until his pass. The *name* "hearth powder" is his. "Glandes," "Goblin Glass" and the goblin-metallurgy implication remain unconfirmed — don't cite them.

**Still open (the economy never shipped with the mechanics):** none of the four tables carries a salt value, a recipe, shop stock or a biome source, so **raw powders and fillers cannot be bought, made or found**. Charges can be assembled out of materials that have no way into the world.

**Open decisions:** alchemy tier ladder above T1 (bases locked: oil/tar/tincture/elixir/sand/powder + ingredient/base/catalyst/reagent quad); ingredient catalog + per-ingredient effects (do not fabricate — Gourmand's Gift rule); regional ore ladder (inside geography merge); item weights are placeholders.

**Waiting on Reece:** how raw powder/filler enters the world (buy · find · craft — the old *Druid Circle Clay-Metal Armor & Gunpowder* parking-lot question, now live — **the 09-04 session has passed and nothing moved: zero powder instances exist anywhere in the game and `charge_builds` is still 0 rows**) · his pass on the placeholder flavour text · ingredient/catalyst authoring (Amber catalyst awaits) · item-weight tuning pass.

**Links:** `library-docs-caldera.md` (gear catalog) · `DOWNTIME_ALCHEMY_SPEC.md` · `library-current-state §3` · Ferry Walk Market docx

## Links

- defines → [[items]] (w=3, inferred) — the four item tables
- defines → [[recipes]] (w=3, inferred)
- defines → [[loot]] (w=3, inferred)
- relation → [[systems/04-combat-and-resolution]] (w=3, inferred) — ordnance
- relation → [[systems/01-effects-engine]] (w=3, inferred)
- relation → [[tags/person]] (w=3, inferred)
