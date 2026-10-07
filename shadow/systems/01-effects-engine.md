---
title: 01 · Effects Engine
aliases: []
type: system
summary: Universal no-code effect/ability authoring — one engine, many source DBs (items, abilities, conditions all reference it).
last-verified: 2026-09-06
source: inferred
migrated-from: https://app.notion.com/p/377e50e3bf7981a5bd3fcfbb27784192
migrated-on: 2026-10-07
---

# 01 · Effects Engine

**What:** Universal no-code effect/ability authoring — one engine, many source DBs (items, abilities, conditions all reference it).

**Current state:** Spine canon: TARGET → GATE → OPERATION → RESOLUTION; two verbs (ADJUST/CREATE); single multi-select Type field (Sub-Type deleted). Builder Phase C closed 5/25; buff/debuff polish shipped. **Runtime substrate now live in the shipped DB (landed by schema 232; app is at 361 as of 09-06):** a generalized conditions + stat-modifier layer (`entity_modifiers`, `entity_conditions`, `condition_stages/tracks`, `status_conditions`, `restriction_conditions`, `reaction_triggers`, `modifier_fields/ops`), actively written (drives nutrition/thirst, downtime). How the migrations since 232 build the *authoring* side isn't in reachable sources — live repo is off the maintenance mount.

**Open decisions:** Remaining builder sections; runtime-spawn #42; trigger-entity-binding #45; initial-vs-tick #48; universal saves #55.

**⚠ Build flags:** Trances may need a *vocation entity frame* (Reece doubts bare Effects can express them); Grapple missing from HX_DAMAGE_TYPES despite grapple-as-damage-type canon.

**Waiting on Reece:** —

**Links:** Effects Engine v2 Design Canon (Notion, https://app.notion.com/p/36ae50e3bf79812ab3d9dc88f00786ae) · `Claude Brain/library-hexicon-specs.md` · `library-current-state-2026-06.md §1`

## Links

- relation → [[systems/04-combat-and-resolution]] (w=3, inferred)
- relation → [[systems/03-items-materials-and-economy]] (w=3, inferred)
- defines → [[conditions]] (w=3, inferred) — the status conditions and tracks are this engine's runtime rows
- defines → [[abilities]] (w=3, inferred)
