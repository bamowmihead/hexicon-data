# The Claude Brain — state and report

**The front door of Brain v3.** The pass reads this file first and appends a
dated entry at the end of every run. Any Claude session reads it to know where
the Brain stands. Newest entry on top of the log. Moved here from the Notion
page "14 · The Claude Brain" on 2026-10-07 (Reece: *"move it off notion"*).

**What:** Golden layer = Hexicon's database, Reece's words only → `snapshot/`
in this repo, pushed by the app on save → `shadow/` (derived by
`tools/rebuild_shadow.py`, plus the pass's inferred layer) →
`questions/inbound.json` back to the app's **? Questions** screen → this
weekly pass. Canon: the Brain v3 contract and the Working SOP (both still in
Notion; moving them here is decision 21, pending). Mirror of the migrated
Brain page: `shadow/systems/14-the-claude-brain.md`.

## Standing rules

- Only Reece's verbatim words make vocabulary (Claude-coined labels are descriptions, not canon).
- Suggestions never merge into canon without explicit acceptance — track Accepted / Rejected / Pending.
- Mystery is the rule: never write a definitive true history of the world.
- Campaign state is a LIVE layer — read roster, balances and prices from `snapshot/`, never from documents that rot (lesson locked 6/07).
- The shadow is rebuildable from the golden layer at any time; Reece never needs to read it.
- The pass writes `shadow/`, `questions/` and `tools/` only; never `snapshot/`, never the code repo, never a device.
- Concept pages follow the rule of two; derived-from-snapshot edges outrank inferred ones.

## Open projects

Personal wing (parked, own project) · session transcription pipeline · claude.ai memory cleanup · remaining OneNote notebooks (Space, New TableTop Gameplay, Channel) · the twenty legacy workspace-root strays in Notion (a question for Reece, not a job to do unasked) · decision 20: the ⇡ Brain line in Hexicon shows the last pass (pending) · decision 21: the contract and SOP move into this repo (pending).

## Log (newest first)

- **2026-10-07 — pass v2, first run (fired by hand).** Snapshot of the same day (schema 392, THERIEGLBOP); the rebuild added two new rules (`world.shear_m`, `world.snapshots_kept`, mentioned under system 13) and two script fixes landed: foci now take their gear row's name (seven files were titled "untitled") and `flavor`, `effect` and `context` count as prose, so the trance and cultivation cards show Reece's flavor text and 147 derived files changed. 40 questions written to `questions/inbound.json` (8 canon-conflict, 5 filing-decision, 27 needs-prose, ranked by closeness to the four PCs); the one resolved row, Reece's own test "Why?" with empty notes, was ingested with nothing to apply. 16 hubs (three biomes, nine locations, Moss, the Cattlepos trance, the Water paint, The Party); 338 of 1 003 derived files are orphans, clustered in abilities (118), equipment (42), rules (34), creatures (27) and consumables (26). Odd: houses, factions, branches, companion kinds, paints and condition tracks have no prose column at all, so needs-prose can never reach them. **Next for Reece:** answer the questions in Hexicon's ☰ → ? Questions; the two Stinky rows and the beast bond on Berserker 2.0 are the ones worth answering first.
- **2026-10-07 — Brain v3 complete; Notion left behind.** Steps ①–④ built. ① verified on Reece's desktop (four real snapshot pushes) and merged with ② (the Questions screen, mig 392; the 390 collision repaired). ③: `shadow/` = 1 001 derived files + the 14 Atlas and 6 Codex pages migrated; Atlas, Codex and the Notion Locations/Biomes databases SUPERSEDED under Archive. ④: Routine "Brain pass v2" (Sundays 09:49 New York, fresh cloud session, data repo only); the 09-21 device-folder task disabled. The snapshot now leaves out paint chunks and the House PIN (merged). Reece, same day: *"I'd really prefer to escape notion … move it off notion"* — this file replaces the Notion Brain page; the pass no longer touches Notion. **Next for Reece:** answer questions in Hexicon's ☰ → ? Questions as they arrive; the first pass's run report is the entry below this one when it lands.
- **2026-10-05 — contract ACCEPTED** as written (Brain v3 — Hexicon ↔ Shadow Contract, Notion, The Hexicon › App Development). Separate data repo `hexicon-data`; shadow lives there as markdown; Atlas/Codex and the Notion Locations/Biomes DBs archive with SUPERSEDED banners once the snapshot exists; hub threshold 15; Reece's own questions share the table. Build order ① repo + snapshot export → ② questions table → ③ shadow rebuild → ④ pass v2 live, old task retired. Also 10-05: the one-task-per-session rule relaxed by Reece for this line.
- **2026-10-04 — Brain v3 direction accepted** (design chat). Problem named by Reece: the same concept lives under several branches → stale copies, confused context, sections dropped. Fix: tree → web. Accepted: (1) two layers kept separate for readability — Reece's wiki inside Hexicon (fields + short notes, written during play, only he edits = golden words) and Claude's shadow web derived from it, rebuildable at any time; (2) transport = route B: Hexicon pushes a TEXT snapshot on change to a private GitHub data repo and pulls Claude's questions file from it; the pass reads from the cloud, no device dependency (M365 connector tested 10-04: not available for personal accounts); (3) a questions table in Hexicon as the shared surface — two writers, separate columns; types canon-conflict · filing-decision · needs-prose; pool cap 40, view of 10, filters, shuffle, refill toggle rank vs random; resolved rows kept 2 weeks after ingest; needs-prose rows generated from empty fields (Reece: nearly everything has fields, little prose; finding what needs prose is the pain); (4) retrieval rules accepted as a set 10-05.
- **2026-09-13 — the maintenance pass lost a tool.** A Windows update dated 09-08 broke Claude's sandbox file mount: the run could read Notion and file names but not open a database, unzip a backup or run a script. Two single points of failure named: the repo off-mount for nine weeks, the DB reachable only through a sandbox that can break. Root patrol found twenty-two workspace-level pages outside the six root nodes, most predating the 07-02 decision; two post-decision strays moved to Inbox; the legacy twenty left as a question for Reece.
- **2026-08-23 — the Working SOP.** Reece created *Hexicon — Claude Working SOP* (08-13, under The Hexicon › App Development, revised 08-16/08-17 with a RUN-MODE contract) — the first Notion page in months that build sessions read rather than only write; its rules match this system's standing rules.
- **2026-08-16 —** a rebuilt sync exists again, machine↔machine (desktop↔laptop by `content_key` + `sync_vector`), not Notion; the 07-10 removal of the Notion push stands.
- **2026-07-03 — Notion retired as a build-status dependency.** The status-page writer gone; the ~524K status page archived; on 07-10 the whole Notion-sync feature (~18k LOC) removed from the repo. Build state lives in the repo's handoffs and git log.
- **2026-07-02 — workspace reorg accepted:** six-node fixed root (Home · Inbox · The Hexicon · Settings · Life · Archive); archive-all convention; Inbox capture pen.
- **2026-06-06 — full corpus ingested:** 98 design chats (2025–2026), play docs, Hexicon specs, OneNote (Crater, DND Multiverse incl. 2019 Star Wars, Settings, journals indexed), old homebrews; 15+ library files in `Caldera/Claude Brain/` (now `Hexicon/docs/corpus/Caldera/Claude Brain/`). ~35-question canon clearance complete. Atlas (14 fixed pages) and Codex (lazy tree) seeded in Notion.

## Links

Claude Brain Library — mining archives (Notion, https://app.notion.com/p/377e50e3bf7981fdaf0fdefed590c7ec) · Parking Lot (Notion, https://app.notion.com/p/34be50e3bf7981c8812ec35505694697) · Recovered Decisions staging (Notion, https://app.notion.com/p/377e50e3bf7981d895e7fe9eed426abb) · contract (Notion, https://app.notion.com/p/3efe50e3bf7981d29ed6e2a4f20f6037) · Working SOP (Notion, https://app.notion.com/p/3bde50e3bf79811b97e1f53eb5eab88f) · code repo `bamowmihead/Hexicon` → `docs/ROADMAP.md` (the plan of record)
