---
title: 04 · Combat & Resolution
aliases: []
type: system
summary: 2d10 + attribute; 3 AP + 2 reactions; no HP — Endurance + wound slots; flat-DR armor; attacks auto-hit.
last-verified: 2026-09-06
source: inferred
migrated-from: https://app.notion.com/p/377e50e3bf7981d0ac4cd7883ac73292
migrated-on: 2026-10-07
---

# 04 · Combat & Resolution

**What:** 2d10 + attribute; 3 AP + 2 reactions (stable since Nov 2025); no HP — Endurance + wound slots (size-based, invented Crater 5/02/24); flat-DR armor.

**Current state:** Resolution canon (6/07 anchor-doc Q&A): **no roll to hit — attacks auto-hit**; Defense = flat damage soak; some actions COST Endurance ("it's not a measure of health, it's a measure of endurance"). Wound engine = canon as design, unused at table — pending app implementation, not abandoned. 10-damage-type rule catalog, resistance/weakness tiers, action/cover economy all designed in April play docs (pre-Effects wording — needs forward-port). Grapple is a damage type (Grapple→Pin→Restrained), replacing the old grapple action. App vocabularies: 19 damage types, 16 senses.

**In app (per Reece's 08-05 Test Guide, master @ ~273):** a **Targeting** resolver is live GM-side — pick ability → target → roll a dice grid → resolve. Damage buckets apply BEFORE Defense: Affinity heals ½ · Immunity none · Resistance ½-before-Defense · none = full − Defense · Aversion ×2 · Weakness = auto-crit (no Endurance dmg, Endurance set to MAX, a wound lands, on-hit condition applies). NOT yet built: AP/ammo spend on Targeting, Intuition-filtered target list, condition rendering on sheets, lethal wounds/death timers, staged attribute saves, self-ability effects.

**New 08-17→08-22 (DB 8/23, schema 333) — ordnance joins the resolver.** Explosives are now assembled from materials rather than authored as items (powder × filler × container × container-material — see [[systems/03-items-materials-and-economy]]), and the damage they throw is *derived*: powder rating gives dice per litre, filler gives its own die and type, the container's material adds fragments (wood d4 splinters / clay d6 shards, 5 m spread) and decides whether heat or concussion wrecks it early. **RULED 08-24 (Reece, verbatim): "Force damage is concussive force damage which does ignore armor."** Force is a damage *type* that bypasses Defense — Black Powder's `ignores_defense` flag is one instance of the rule, not an item quirk. *(Claude suggestion, Pending: model it on the damage type rather than a per-powder column.)* **New 08-24→08-27 — ordnance has now been exercised in play.** `live_explosives` holds 3 rows from 08-24 bench throws (Frag and Sticky Frag, one thrower, armed round → detonate round, with concussive and fragment face-rolls stored). Eight ordnance abilities exist — Throw Frag / Impact Frag / Sticky Frag · Set Mining / Tree Ripper / Timed Charge · Detonate Powder Keg · Exploding Arrow Burst — over a new **fuse layer**: `fuse_cordages` (Slow Match 1 cm per round · Quick Cord 6 m · Flash Cord 60 m · Poured Black Powder, which costs you the powder you pour) plus `fuse_rounds` / `fuse_adjustable` / `sticky` / `conditionals_json` on creature abilities. Reece ruled 08-24 that **a fused container is still a container**, and that **a powder-holding container ignites from Heat damage with no fuse at all**. **`trap_kinds`** holds its first row: Bomb Trap, 3d6 Force, step-triggered, detection 3.

**Also new — a SENSES / SIGNATURE engine (first detection layer).** `sense_kinds` (3) × `signature_emitters` (11) resolve one signature so far, **reactive** — a nose smells powder and the charges built from it. Scent: 30 m, reports *how much* is in reach; how well it can name *where* trades against how far it reaches. Echolocation (19 batkin already have it at 30 m) and the Cackler's Blood Nostril (1 mile; the matriarch's at six) are catalogued for vocabulary only — the engine resolves no signature for them yet.

**Open decisions:** whether Force-bypasses-Defense reopens armour design generally (it is now a whole damage type, not one column) · forward-port combat math into Effects wording; armor system port; the 20-body-region wound table (Crater salvage) as Effects conditions feed.

**Waiting on Reece:** whether the ignore-armour behaviour moves onto the Force damage type in data (currently a per-powder column) · the **09-04 has passed and whether ordnance or the grid were exercised is unknown** — the DB shows no play writes after 08-24, but that inference was wrong once before, so it is queued as a question, not recorded as fact. What is certain from the data: `charge_builds` is still 0 rows, so no charge has ever been assembled in the app.

**Links:** `library-docs-caldera.md` (combat math) · `library-onenote-crater.md` (wound table salvage) · GM Sheets docx

## Links

- relation → [[systems/01-effects-engine]] (w=3, inferred)
- relation → [[systems/03-items-materials-and-economy]] (w=3, inferred) — ordnance materials
- relation → [[systems/05-magic-and-the-artes]] (w=3, inferred) — soul transfer rides the targeting loop
- defines → [[senses]] (w=3, inferred)
- defines → [[abilities]] (w=3, inferred)
