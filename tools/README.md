# tools/ — the pass's scripts

Run by Claude's weekly pass (and by Claude in any session), never by Hexicon.

* `rebuild_shadow.py` — rebuilds the **derived layer** of `shadow/` from
  `snapshot/`: one file per concept-bearing row, typed and weighted links,
  backlinks, hubs, and `shadow/_index.md`. The `## Inferred` section of every
  derived file is preserved byte for byte; files whose header says
  `source: inferred` (the migrated Atlas and Codex pages) are never touched.
  Deterministic: an unchanged snapshot is an empty diff.

  ```
  python3 tools/rebuild_shadow.py          # write
  python3 tools/rebuild_shadow.py --check  # report only
  ```

  Standard library only. Python 3.10+.
