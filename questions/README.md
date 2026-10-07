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
  "ingested": ["id-of-a-resolved-row", "another"],
  "replies": [
    { "id": "4f1c2b9e-…", "text": "rt-b1bbd0 carries the attunement stars; rt-7cf25d carries the statline.",
      "at": 1760003600, "proposed_answer": "Keep rt-b1bbd0 (Calderan, humanoid, Big)" }
  ]
}
```

A question may also carry (Hexicon mig 393, 2026-10-07):

| Field | Meaning |
|-------|---------|
| `question` | The **one-line ask** only. Lead with the question, not the evidence. |
| `context` | The evidence — the fields, values and ids that make the question worth asking. Shown folded behind "why is this asked?". |
| `choices` | Only for a genuine two-way (or three-way) conflict: the answers as **his own field values**, e.g. `["Keep rt-7cf25d (Goblinoid, quadruped, Huge)", "Keep rt-b1bbd0 (Calderan, humanoid, Big)"]`. The screen adds "other" itself. Leave it out when a question has no natural choices. |

## Threads (mig 393)

Every question is a small discussion. In `snapshot/questions.json` a row's
`thread_json` is `[{who: "reece"|"claude", text, at}]` and `awaiting` is
`"claude"` while Reece's latest message has no reply. **The pass (and any
Claude asked to "answer the threads") answers every row with
`awaiting = "claude"`** by adding to `replies`: the reply text, and
`proposed_answer` when the reply amounts to a concrete resolution Reece could
accept with one click (it becomes his `notes` and resolves the row). A reply
whose text equals the thread's last Claude message is ignored on re-read, so
the file is safe to read twice. Keep replies short and grounded in the
snapshot and the shadow; never decide for him.

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
