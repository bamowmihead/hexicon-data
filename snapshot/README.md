# snapshot/ — written by Hexicon only

A text copy of Hexicon's database, one JSON file per entity type
(`creature_types.json`, `locations.json`, `vocations.json`, …), plus
`_manifest.json` naming the schema version, the machine that pushed, the time,
and the row count of every file.

* **Writer:** the Hexicon desktop app, from Reece's machine, on save (batched:
  about two minutes after the last edit, or every ten minutes during a long
  editing run, and once more when the app closes).
* **Readers:** Claude's weekly pass and any Claude session that needs the
  campaign's current facts.
* **Overwritten in place.** The newest commit is the current state; the git
  history is the archive.
* **Never edit by hand and never from the pass.** Anything written here from
  anywhere but Hexicon is overwritten by its next push, and a hand edit here
  does not reach the database. The database is the source of truth; this is a
  mirror of it.

Each entity file is a JSON array of row objects, sorted by id, with one key per
database column. Columns whose name ends in `_json` are unpacked into real JSON
so diffs read field by field. Binary columns are left out.
