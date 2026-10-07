# shadow/ — written by Claude's weekly pass only

Claude's web: one markdown file per concept, derived from `snapshot/` plus
Claude's inferred layer, with typed and weighted links between files. Step ③
of the Brain v3 contract (section 5, accepted as a set 2026-10-05).

* **Writer:** the weekly pass, and only the pass (and Claude in a session,
  acting as the pass). **Hexicon never writes here.**
* **Reader:** Claude, in any session, as its memory of the campaign.
* **Rebuildable from scratch** at any time: `python3 tools/rebuild_shadow.py`.
  Reece never needs to read this folder.

## Two layers, one folder

| Header `source:` | Where | Who writes | Regenerated? |
|------------------|-------|------------|--------------|
| `snapshot` | `creatures/`, `pcs/`, `locations/`, `items/`, `abilities/`, `rules/`, … (one folder per kind) and `_index.md` | the rebuild script, from `snapshot/` | **Yes**, every pass — except each file's `## Inferred` section, which is kept byte for byte |
| `inferred` | `systems/` (the 14 Atlas pages, migrated 2026-10-07) and `concepts/` (the Codex pages) | the pass, by hand | **Never** by the script; it only indexes them |

## A file

```
---
title: Bledger            # the row's own name — Reece's word
aliases: []               # ONLY his verbatim words; the pass adds them from his notes
type: pc                  # creature · pc · location · item · rule · system · concept · session …
summary: ""               # his tagline/description, first sentence; never invented
last-verified: 2026-10-07 # the snapshot's date (derived) or the page's (inferred)
source: snapshot          # or inferred
id: pc-193c2a             # the row's id (derived files)
table: pcs
links: 4
hub: true                 # present when links ≥ 15, or type is session/root
---
# Bledger
## Fields        — golden fields, verbatim, non-empty only
## In his words  — the prose columns (tagline, description, bio, notes …), verbatim
## Links         — `- <type> → [[kind/slug]] (w=N, snapshot|prose|inferred|pinned)` then `Linked from:`
## Inferred      — the pass's layer: aliases from his words, inferred relations, pinned links (w=5)
```

## Edges

* **Types:** `parent` / `child` (tree), `defines`, relations (`member-of`,
  `located-in`, `practices`, `found-in`, `has-member`, `about`, …),
  `mentions`, `pinned`.
* **Weights:** tree / defines / relation = 3 (cheap), mentions = 1
  (expensive), pinned = 5 (overrides the hub stop).
* **Origin:** `snapshot` (an id column or id list in the data), `prose` (a
  name matched in his text), `inferred` (the pass's reading), `pinned`.
  Derived-from-snapshot edges outrank inferred-from-prose edges.
* A link to a bare kind (`[[items]]`, `[[creatures]]`) means the whole folder.

## Retrieval (contract §5)

Seed = aliases in the message → canonical file; the seed always expands one
layer. Hubs (`hub: true`) are loaded but not expanded; a pinned link
overrides the stop; hubs vote on candidates reached by other paths. Rank by
connectedness to the working set, not hop distance. Budget + tiers: full
text for the seed and the top-ranked, one-line summaries beyond.
