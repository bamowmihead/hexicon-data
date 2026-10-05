# hexicon-data

The data side of **Brain v3**. Hexicon's own database is the single source of
truth for the Caldera campaign (Reece's words only); this repo holds a text
copy of it, the questions that flow back to him, and Claude's derived web.
Canon: the Brain v3 contract page in Notion ("Hexicon ↔ Shadow Contract",
accepted 2026-10-05).

Three folders, three writers. **Nobody writes in another's folder.**

| Folder       | Written by                    | Read by                        |
|--------------|-------------------------------|--------------------------------|
| `snapshot/`  | **Hexicon**, on save          | Claude's weekly pass           |
| `questions/` | **Claude's weekly pass**      | Hexicon (ingest, step ②)       |
| `shadow/`    | **Claude's weekly pass**      | Claude, in any session         |

Each folder's own README says what it holds.

## Walls

* Hexicon never writes outside `snapshot/`. Its commits touch that folder only.
* The weekly pass never writes under `snapshot/`.
* The pass is never attached to the code repo (`bamowmihead/Hexicon`); it reads
  and writes this repo only.
* Text only. The SQLite file itself never lands here.

## History is the archive

Every file in `snapshot/` is overwritten in place on each push, so the current
state is always the newest commit and every earlier state is in `git log`.
Nothing here needs a date in its filename.
