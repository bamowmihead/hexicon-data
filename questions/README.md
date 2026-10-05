# questions/ — written by Claude's weekly pass only

The channel from Claude back to Reece (Brain v3 contract §3).

* **Writer:** the weekly pass, and only the pass. It writes **one file**,
  `inbound.json`, and overwrites it in place each run.
* **Reader:** Hexicon. On every snapshot cycle (about two minutes after
  Reece's last edit, and on close) it reads `inbound.json`, adds the questions
  it has not seen, stamps the resolved rows named in `ingested`, and removes
  resolved rows fourteen days after that stamp. The very next
  `snapshot/questions.json` already shows the stamps.
* **Hexicon never writes here.** Reece's answers travel back the other way,
  inside `snapshot/questions.json` (`status`, `notes`, `resolved_at`).

## `inbound.json` — the shape Hexicon reads

```json
{
  "format": 1,
  "written_at": "2026-10-12T06:00:00Z",
  "questions": [
    {
      "id": "4f1c2b9e-…",
      "question": "Is the Nail a focus or a vessel? The chart says focus; Bledger's sheet says vessel.",
      "type": "canon-conflict",
      "difficulty": 2,
      "links": ["pc-b", "foci-nail"],
      "rank": 3.5,
      "raised_at": 1760000000,
      "raised_by": "claude"
    }
  ],
  "ingested": ["id-of-a-resolved-row", "another"]
}
```

Field by field:

| Field | Required | Meaning |
|-------|----------|---------|
| `id` | yes | A UUID the pass mints. The same id is skipped on later reads, so the file is safe to re-read. |
| `question` | yes | Reece's words for the things named; the question itself may be Claude's. Empty = skipped and named in the status. |
| `type` | no | `canon-conflict` · `filing-decision` · `needs-prose`. Default `filing-decision`; anything else = skipped. |
| `difficulty` | no | 1 easy · 2 · 3 hard. Default 2. Reece may change it. |
| `links` | should be ≥1 | Element ids from the snapshot (`pcs.id`, `creature_types.id`, …). Hexicon resolves them to chips. A question with none is still stored and flagged. |
| `rank` | no | The pass's order, lower first. Hexicon's "refill by rank" uses it. |
| `raised_at` | no | Unix seconds. Default: when ingested. |
| `raised_by` | no | Default `claude`. Reece's own questions are `reece` and never come from this file. |
| `ingested` | no | Ids of **resolved** rows the pass has read (status + notes consumed). Hexicon stamps `ingested_at` once; an open id is ignored. |

Pool rule (§3): the pass keeps **40** open, topping up by rank each run. Hexicon
reports the count on its screen but does not enforce the cap.
