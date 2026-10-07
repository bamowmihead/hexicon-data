---
title: Field Stabilise
aliases: []
type: ability
summary: "Stop a dying character's death timer WITHOUT healing them — WOUND_SPEC's own stabilisation, no endurance restored and no wound cleared."
last-verified: 2026-10-07
source: snapshot
id: ca-newt-stabilise
table: creature_abilities
links: 1
---

# Field Stabilise

Stop a dying character's death timer WITHOUT healing them — WOUND_SPEC's own stabilisation, no endurance restored and no wound cleared.

## Fields

- **activation:** Instant
- **activation_cost:** 1 AP
- **blocked_by_cover:** 0
- **blocks_los:** 0
- **blocks_movement:** 0
- **charges_max:** 0
- **charges_on_empty:** inert
- **charges_recovery_amount:** 1
- **charges_refill_from_consumes:** 0
- **charges_type:** charges
- **completion:** Incomplete
- **damage_fixed:** 0
- **duration:** Instant
- **effect_types_json:** `["Healing"]`
- **fuse_adjustable:** 0
- **fuse_rounds:** 0
- **is_deactivation_reactionary:** 0
- **is_reactionary:** 0
- **kind:** Stabilise
- **movable_range_m:** 0
- **name:** Field Stabilise
- **persists_without_source:** 0
- **produce_quantity:** 1
- **range:** 1m
- **requires_line_of_sight:** 0
- **restrictions_json:** `{"disable": [], "require": [{"id": "rc-target-dying"}]}`
- **sticky:** 0
- **store_capacity:** 1
- **target:** Single
- **target_shape:** Single
- **tick_kind:** time

## In his words

**effect:** Stop a dying character's death timer WITHOUT healing them — WOUND_SPEC's own stabilisation, no endurance restored and no wound cleared. Requires a target who is dying. NOTE: every creature already has the universal 1 AP Stabilize action; this is Newt's named version of it, not a second rule.


## Links

- mentions → [[creatures/newt]] (w=1, prose)

## Inferred

<!-- The pass writes below this line: aliases from Reece's own words, relations it infers, pinned links (w=5). Kept across rebuilds. -->
