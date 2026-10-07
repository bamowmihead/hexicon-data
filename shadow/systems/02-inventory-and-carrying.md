---
title: 02 · Inventory & Carrying
aliases: []
type: system
summary: LOCKED hybrid — slots for the worn/wielded layer, nested weight-based containers for storage.
last-verified: 2026-09-06
source: inferred
migrated-from: https://app.notion.com/p/377e50e3bf7981698224d05f9af54edd
migrated-on: 2026-10-07
---

# 02 · Inventory & Carrying

**What:** LOCKED hybrid — slots for the worn/wielded layer (quickslots, armaments, equipment), nested weight-based containers for storage.

**Current state:** Container model is now the **sole inventory renderer** (UniversalItemTable across general/shop/loot/transfer/C&M). **Device/player app ported off legacy slots + verified on-device** (the 6/12 gate). Vehicles and Houses/Companies are container entities; **body plans shipped** (humanoid/quadruped/vehicle); ammo subsystem + held-in-hand live. Capacity math locked: size class × Might, ±30%/pt, 400% wall, Medium base 40 lb; equipped items weigh half; specialty weighs less. Schema 162 (inventory stable and untouched since; app now at schema 361, 09-06).

**Open decisions:** cart-as-vehicle-entity (equippable, own upgrade tree — parked) · quick-slot bonus groups · item-size enum · loot foraging.

**Pending intents (not canon):** creatures may start with no storage container; loot & equip pools randomizing creature gear.

**Waiting on Reece:** higher-tier body-plan slot sets as new creature kinds need them.

**Links:** `Hexicon/docs/specs/CONTAINER_SPEC.md` · `CARRYING_CAPACITY_SPEC.md` · Recovered Decisions staging (Notion, https://app.notion.com/p/377e50e3bf7981d895e7fe9eed426abb) · `library-current-state §2/§14`

## Links

- relation → [[systems/03-items-materials-and-economy]] (w=3, inferred)
- relation → [[systems/10-companions-houses-and-pcs]] (w=3, inferred) — Houses and Companies are container entities
- defines → [[items]] (w=3, inferred)
- defines → [[vehicles]] (w=3, inferred)
