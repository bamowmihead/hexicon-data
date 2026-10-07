---
title: 13 · Hexicon App
aliases: []
type: system
summary: Tauri/Rust/SQLite + React GM desktop app + LAN player devices. Build state lives in the repo's git log and docs/ROADMAP.md; schema is read from the snapshot manifest.
last-verified: 2026-10-07
source: inferred
migrated-from: https://app.notion.com/p/377e50e3bf79811bb71ef522f705b05b
migrated-on: 2026-10-07
---

# 13 · Hexicon App

**What:** Tauri/Rust/SQLite + React GM desktop app + LAN player devices. The industrialized product (manifesto predates Claude: June 2025 "Product Ideas"). Publication ethos LOCKED: "everyone involved gets a big cut"; product shapes open.

**Where the truth is now (2026-10-07):** the **plan of record is `docs/ROADMAP.md` in `bamowmihead/Hexicon`**, edited in the same commit as the work; `git log` is the build log; the **schema number is `schema` in `snapshot/_manifest.json`** of this repo, written by the app itself on every push. This page is a map, not a status page — the ten-week "repo off the mount" blind spot the Notion original complained about is closed by the data repo: the pass reads the snapshot from the cloud and never needs a device.

**Shipped and stable, one line each:** the container inventory rewrite is the sole renderer and the device app runs on it; trances, cultivation, vehicles, downtime + Alchemy v1; nav/maps/travel/encounters (route planner over the 61-node graph, radial pathway authoring, water bodies, two-tier fog, terrain sculpting, the detail-map disk bake); holdings/facilities; the Targeting resolver; the survival/hunting loop and Rummage; the tactical grid (dimensions, ground paints, wall presets, per-row hostility/colour/symbol) and the ordnance + senses layers; the Channeler vocation, sessions and point ledger, the tree engine (authoring only), memorials (migs 368–375); the database viewer (mig 381–382); world ownership — paint, walls and bodies belong to the world, world shear snapshots (migs 367, 389–391); **Brain v3 steps ① and ②** — the snapshot push and the Questions screen (mig 392). Notion coupling stays retired as an app dependency.

**Machines:** the desktop `THERIEGLBOP` is where he authors; the laptop `LAPTOPI6GA2VOC` runs sessions; `DESKTOPKLQEOS0` appeared 09-18 (queued question, unresolved). Desktop↔laptop sync is machine↔machine by changesets over the OneDrive backups folder (`content_key` + `sync_vector`), not Notion.

**⚠ Build flags:** Grapple damage type missing; Origins/Genomes required in final product; iceberg philosophy is a hard UI constraint.

**Working agreement:** the Claude Working SOP (Notion, https://app.notion.com/p/3bde50e3bf79811b97e1f53eb5eab88f) — Reece-editable, treated as canon by build sessions; the one-task-per-session rule was relaxed by him on 2026-10-05.

**Waiting on Reece:** the `BACKLOG_TRIAGE.md` QA queue D1–D8, with **D8 player-vs-GM routing discrepancy** still the one real bug; the design-gated queue (water/arrow kinds, ammo-selection rule, table-filter spec, treated-wound flag, camp rules); the downtime-surface redesign and the wound-system pass; the board's baked-layers design (ROADMAP item 8); the two world-ground answers asked 2026-09-22.

**Links:** `Hexicon/CLAUDE.md` · `Hexicon/docs/ROADMAP.md` · `BACKLOG_TRIAGE.md` · Map Systems Handoff (Notion, https://app.notion.com/p/387e50e3bf79818b8e5ef40fca26c64e) · `library-hexicon-specs.md`

## Links

- relation → [[systems/14-the-claude-brain]] (w=3, inferred)
- relation → [[systems/12-session-play-and-gm-tools]] (w=3, inferred)
- defines → [[questions]] (w=3, inferred) — the Questions screen's rows
- defines → [[rules/worldshear-m]] (w=3, inferred) — new in the 2026-10-07 snapshot; the world-shear threshold, its note says the number is Claude's until Reece has seen a place shear
- defines → [[rules/worldsnapshots-kept]] (w=3, inferred) — new in the 2026-10-07 snapshot; sculpt snapshots kept per location
