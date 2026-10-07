#!/usr/bin/env python3
"""Rebuild the DERIVED layer of the shadow from the snapshot.

Brain v3, step 3 (contract section 5, accepted as a set 2026-10-05).

    python3 tools/rebuild_shadow.py            # from the repo root
    python3 tools/rebuild_shadow.py --check    # report only, write nothing

What it writes
--------------
One markdown file per concept-bearing row of the snapshot, under
``shadow/<kind>/<slug>.md``, plus ``shadow/_index.md``. Each file has:

* a YAML header: title, aliases (Reece's words only; empty unless the data
  carries one), type, one-line summary (his own tagline/description, first
  sentence), last-verified (the snapshot's date), source (``snapshot``), the
  row's id and table, and ``hub: true`` when the file has 15 or more links;
* ``## Fields`` -- the golden fields, verbatim, non-empty scalars only;
* ``## Links`` -- typed, weighted edges, derived from the row's ``*_id``
  columns and ``*_json`` id lists (cheap: parent/child, defines, relation)
  and from name matches in prose (expensive: mentions), followed by the
  reverse edges other files point at this one;
* ``## Inferred`` -- the pass's layer. **Preserved across rebuilds, byte for
  byte.** Everything above this heading is regenerated; everything below it
  is kept. This is the only part of a snapshot-derived file the pass edits.

Files whose header says ``source: inferred`` (the migrated Atlas and Codex
pages under ``shadow/systems/`` and ``shadow/concepts/``) are never
regenerated or touched; they are read for the index and for link targets.

Rules carried from the contract
-------------------------------
* Edge weights: tree / defines / relation = 3 (cheap), mentions = 1
  (expensive), pinned = 5 (overrides the hub stop; set only in Inferred).
* Hubs: 15 links or more (count-detected), or type-declared (session, root).
* Derived-from-snapshot edges outrank inferred-from-prose edges; the file
  says which is which.
* Nothing here invents vocabulary. Titles are the row's own ``name``;
  summaries are the row's own tagline or description, cut at a sentence.
* Deterministic: the same snapshot gives the same bytes, so a rebuild with
  no data change is an empty diff.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = ROOT / "snapshot"
SHADOW = ROOT / "shadow"

HUB_THRESHOLD = 15
W_CHEAP = 3
W_MENTION = 1

# ---------------------------------------------------------------------------
# WHAT BECOMES A FILE
# ---------------------------------------------------------------------------
# table -> (kind folder, type label). Only rows of these tables become files.
# Everything else in the snapshot (play state, logs, chart cells, link rows)
# is read for edges where useful but is not a concept.
PER_ROW = {
    "creature_types": ("creatures", "creature"),
    "pcs": ("pcs", "pc"),
    "named_characters": ("characters", "character"),
    "houses": ("houses", "house"),
    "companies": ("companies", "company"),
    "memorials": ("memorials", "memorial"),
    "factions": ("factions", "faction"),
    "branches": ("branches", "branch"),
    "locations": ("locations", "location"),
    "holdings": ("places", "holding"),
    "camps": ("places", "camp"),
    "facilities": ("places", "facility"),
    "shops": ("places", "shop"),
    "biomes": ("biomes", "biome"),
    "storylines": ("storylines", "storyline"),
    "armaments": ("items", "armament"),
    "equipment": ("items", "equipment"),
    "gear": ("items", "gear"),
    "consumables": ("items", "consumable"),
    "recipes": ("recipes", "recipe"),
    "loot_tables": ("loot", "loot-table"),
    "creature_abilities": ("abilities", "ability"),
    "traits": ("traits", "trait"),
    "status_conditions": ("conditions", "status-condition"),
    "condition_tracks": ("conditions", "condition-track"),
    "vocations": ("vocations", "vocation"),
    "skills": ("skills", "skill"),
    "trees": ("trees", "tree"),
    "companion_kinds": ("companions", "companion-kind"),
    "sessions": ("sessions", "session"),
    "rules": ("rules", "rule"),
    "foci": ("foci", "focus"),
    "trance_forms": ("trances", "trance-form"),
    "trances": ("trances", "trance-card"),
    "cultivations": ("plants", "cultivation-card"),
    "cultivations2": ("plants", "plant-card"),
    "plants2": ("plants", "grown-plant"),
    "gardens": ("plants", "garden"),
    "ground_paints": ("paints", "ground-paint"),
    "sense_kinds": ("senses", "sense"),
    "vehicles": ("vehicles", "vehicle"),
    "retinue_templates": ("retinues", "retinue-template"),
    "named_retinues": ("retinues", "named-retinue"),
    "encounter_tables": ("encounters", "encounter-table"),
    "tags": ("tags", "tag"),
    "questions": ("questions", "question"),
}
# Type-declared hubs (contract section 5): a session and the root.
HUB_TYPES = {"session"}

# ``<column>_id`` -> table, mirrored from Hexicon's dbview.rs so the two agree.
ID_COLUMNS = {
    "house_id": "houses", "company_id": "companies", "pc_id": "pcs",
    "type_id": "creature_types", "creature_type_id": "creature_types",
    "companion_type_id": "creature_types", "companion_pc_id": "pcs",
    "location_id": "locations", "death_location_id": "locations",
    "holding_id": "holdings", "camp_id": "camps", "tree_id": "trees",
    "template_tree_id": "trees", "template_id": "trees", "node_id": "tree_nodes",
    "kind_id": "companion_kinds", "vocation_id": "vocations",
    "ability_id": "creature_abilities", "group_id": "roster_groups",
    "session_id": "sessions", "save_id": "expeditions", "hex_id": "hexes",
    "biome_id": "biomes", "shop_id": "shops", "faction_id": "factions",
    "branch_id": "branches", "gear_id": "gear", "effect_id": "soul_effects",
    "trance_id": "trances", "cultivation_id": "cultivations", "plant_id": "plants2",
    "garden_id": "gardens", "instance_id": "roster_instances",
    "parent_creature_id": "creature_types", "parent_vehicle_id": "vehicles",
    "memorial_id": "memorials", "bond_id": "companion_bonds",
    "parent_id": "locations", "active_trance_id": "trances",
}
# Columns holding vocation NAMES (the old shape) rather than ids.
VOCATION_NAME_LISTS = {"primary_vocation_json", "secondary_vocation_json"}
# Edge type by column. Anything else that resolves is a plain ``relation``.
EDGE_TYPE = {
    "parent_creature_id": "parent", "parent_id": "parent", "parent_vehicle_id": "parent",
    "house_id": "member-of", "company_id": "member-of", "faction_id": "member-of",
    "location_id": "located-in", "hex_id": "located-in", "death_location_id": "died-at",
    "holding_id": "located-in", "camp_id": "located-in",
    "abilities_json": "defines", "traits_json": "defines", "features_json": "defines",
    "vocation_id": "practices", "primary_vocation_json": "practices", "secondary_vocation_json": "practices",
    "biomes_json": "found-in", "biome_id": "found-in",
    "characters_json": "has-member", "bestiary_members_json": "has-member", "groups_json": "has-member",
    "branches_json": "has-branch", "location_json": "located-in",
    "links_json": "about",
}
# ``*_json`` columns that are NOT id lists (mirrors dbview.rs). Skipped for edges.
NOT_ID_LISTS = {
    "attrs_json", "ui_state_json", "config_json", "params_json", "effects_json", "grants_json", "spec_json",
    "history_json", "cost_json", "refund_json", "crit_json", "runoff_json", "outcome_json", "sources_json",
    "dice_json", "faces_json", "achievement_json", "break_rule_json", "skills_json", "target_options_json",
    "save_outcomes_json", "save_tiers_json", "heals_json", "removes_json", "consumes_json", "gains_json",
    "resource_locks_json", "keywords_json", "tags_json", "category_json", "damage_types_json", "senses_json",
    "movements_json", "loot_json", "butcher_json", "motivations_json", "pitfalls_json", "weaknesses_json",
    "resistances_json", "immunities_json", "aversions_json", "affinities_json", "type_categories_json",
    "soul_tiers_json", "beast_gear_json", "trance_mods_json", "healing_rows_json", "damage_rows_json",
    "conditionals_json", "flags_json", "attr_mods_json", "scale_mods_json", "stat_mods_json",
    "starting_grants_json", "faction_json", "value_json", "extent_json", "reveals_json",
    "living_armor_json", "harvest_json", "equipped_json", "armaments_json", "doc_json",
}
# Prose columns scanned for mentions (expensive edges), and used for summaries.
PROSE = ("tagline", "summary", "description", "bio", "notes", "note", "epitaph", "question", "text", "body", "tactics", "script")
# Columns never printed under Fields: plumbing, not facts.
HIDDEN = {
    "id", "content_key", "notion_page_id", "notion_last_synced_at", "local_last_modified_at", "sync_id",
    "sort_order", "portrait_path", "symbol", "symbol_color", "symbol_opacity", "symbol_size", "pin",
    "created_at", "updated_at", "dev_unlock_until", "scratch", "ui_state_json", "config_json",
}


def slugify(s: str) -> str:
    s = re.sub(r"[^\w\s-]", "", s.lower(), flags=re.UNICODE)
    s = re.sub(r"[\s_]+", "-", s).strip("-")
    return s or "untitled"


def first_sentence(s: str, limit: int = 160) -> str:
    s = " ".join(str(s).split())
    if not s:
        return ""
    m = re.match(r"(.+?[.!?])(\s|$)", s)
    out = m.group(1) if m and len(m.group(1)) <= limit else s[:limit].rstrip()
    if len(out) < len(s) and not out.endswith((".", "!", "?")):
        out += "…"
    return out


def yaml_str(s) -> str:
    s = str(s)
    if s == "" or re.search(r'[:#\[\]{}"\'\n]|^\s|\s$|^[-?&*!|>%@`]', s) or s.lower() in ("yes", "no", "true", "false", "null", "~"):
        return json.dumps(s, ensure_ascii=False)
    return s


def load_snapshot() -> dict[str, list[dict]]:
    tables: dict[str, list[dict]] = {}
    for p in sorted(SNAPSHOT.glob("*.json")):
        if p.name.startswith("_"):
            continue
        with p.open(encoding="utf-8") as f:
            rows = json.load(f)
        if isinstance(rows, list):
            tables[p.stem] = rows
    return tables


def snapshot_date() -> str:
    try:
        out = subprocess.run(["git", "-C", str(ROOT), "log", "-1", "--format=%cs", "--", "snapshot"], capture_output=True, text=True, check=True).stdout.strip()
        if out:
            return out
    except Exception:
        pass
    import datetime as _dt
    return _dt.date.today().isoformat()


def row_id(row: dict, table: str) -> str | None:
    for k in ("id", "key", "slug"):
        if k in row and row[k] is not None:
            return str(row[k])
    return None


def row_name(row: dict) -> str:
    for k in ("name", "title", "label", "key", "slug", "question", "number"):
        v = row.get(k)
        if v not in (None, ""):
            s = str(v)
            return s if k != "number" else f"Session {s}"
    return row_id(row, "") or "untitled"


class Node:
    def __init__(self, table: str, row: dict):
        self.table = table
        self.row = row
        self.kind, self.type = PER_ROW[table]
        self.id = row_id(row, table) or ""
        self.title = row_name(row)
        self.path = f"{self.kind}/{slugify(self.title)}"
        self.edges: list[tuple[str, str, int, str]] = []  # (type, target path, weight, origin)
        self.back: list[tuple[str, str, int]] = []        # (type, from path, weight)

    @property
    def summary(self) -> str:
        for k in PROSE:
            v = self.row.get(k)
            if isinstance(v, str) and v.strip():
                return first_sentence(v)
        return ""


def build_nodes(tables: dict[str, list[dict]]) -> tuple[list[Node], dict[str, Node], dict[str, Node]]:
    nodes: list[Node] = []
    by_id: dict[str, Node] = {}
    by_path: dict[str, Node] = {}
    for table in PER_ROW:
        for row in tables.get(table, []):
            n = Node(table, row)
            nodes.append(n)
    # Disambiguate slugs: two "Harness" rows become harness and harness-2.
    seen: dict[str, int] = defaultdict(int)
    for n in sorted(nodes, key=lambda n: (n.path, n.id)):
        seen[n.path] += 1
        if seen[n.path] > 1:
            n.path = f"{n.path}-{seen[n.path]}"
    for n in nodes:
        by_path[n.path] = n
        if n.id:
            # First claim wins for a bare id; table-qualified key always works.
            by_id.setdefault(n.id, n)
            by_id[f"{n.table}:{n.id}"] = n
            if n.row.get("notion_page_id"):
                npid = str(n.row["notion_page_id"])
                by_id.setdefault(npid, n)
                by_id.setdefault(npid.replace("-", ""), n)
    return nodes, by_id, by_path


def resolve(by_id: dict[str, Node], value, table_hint: str | None) -> Node | None:
    if value is None or value == "":
        return None
    s = str(value)
    if table_hint and f"{table_hint}:{s}" in by_id:
        return by_id[f"{table_hint}:{s}"]
    return by_id.get(s)


def derive_edges(nodes: list[Node], by_id: dict[str, Node], tables: dict[str, list[dict]]) -> None:
    # Hexes are not files; a location's hex points at the biome of the hex when known.
    hex_biome: dict[str, str] = {}
    for h in tables.get("hexes", []):
        if h.get("id") is not None and h.get("biome_id") is not None:
            hex_biome[str(h["id"])] = str(h["biome_id"])
    for n in nodes:
        for col, val in n.row.items():
            if val is None or val == "":
                continue
            if col in ID_COLUMNS:
                target_table = ID_COLUMNS[col]
                if target_table == "hexes":
                    b = resolve(by_id, hex_biome.get(str(val)), "biomes")
                    if b and b is not n:
                        n.edges.append(("found-in", b.path, W_CHEAP, "snapshot"))
                    continue
                t = resolve(by_id, val, target_table)
                if t and t is not n:
                    n.edges.append((EDGE_TYPE.get(col, "relation"), t.path, W_CHEAP, "snapshot"))
            elif col in VOCATION_NAME_LISTS and isinstance(val, list):
                for name in val:
                    for v in nodes:
                        if v.table == "vocations" and isinstance(name, str) and v.title.lower() == name.lower():
                            n.edges.append(("practices", v.path, W_CHEAP, "snapshot"))
            elif col.endswith("_json") and col not in NOT_ID_LISTS and isinstance(val, list):
                etype = EDGE_TYPE.get(col, "relation")
                for item in val:
                    key = item if not isinstance(item, dict) else (item.get("id") or item.get("page_id"))
                    t = resolve(by_id, key, None)
                    if t and t is not n:
                        n.edges.append((etype, t.path, W_CHEAP, "snapshot"))
            elif col in ("vocation", "species", "side") and isinstance(val, str):
                # A creature's vocation by NAME (the old column) -> the vocation row.
                if col == "vocation":
                    for v in nodes:
                        if v.table == "vocations" and v.title.lower() == val.lower():
                            n.edges.append(("practices", v.path, W_CHEAP, "snapshot"))
    # Mentions: a prose field naming another file's title. Expensive, weight 1.
    names = sorted(((n.title, n) for n in nodes if len(n.title) >= 4), key=lambda x: -len(x[0]))
    pattern = re.compile(r"\b(" + "|".join(re.escape(t) for t, _ in names) + r")\b", re.IGNORECASE) if names else None
    title_to_node = {t.lower(): n for t, n in names}
    for n in nodes:
        if not pattern:
            break
        prose = " ".join(str(n.row.get(k) or "") for k in PROSE if isinstance(n.row.get(k), str))
        if not prose.strip():
            continue
        hit: set[str] = set()
        for m in pattern.finditer(prose):
            t = title_to_node.get(m.group(1).lower())
            if t and t is not n and t.path not in hit:
                hit.add(t.path)
                n.edges.append(("mentions", t.path, W_MENTION, "prose"))
    # Dedupe, keeping the strongest, and sort for determinism.
    for n in nodes:
        best: dict[tuple[str, str], tuple[str, str, int, str]] = {}
        for e in n.edges:
            k = (e[0], e[1])
            if k not in best or e[2] > best[k][2]:
                best[k] = e
        n.edges = sorted(best.values(), key=lambda e: (-e[2], e[0], e[1]))


def backlinks(nodes: list[Node], by_path: dict[str, Node]) -> None:
    for n in nodes:
        for etype, target, w, _ in n.edges:
            t = by_path.get(target)
            if t:
                t.back.append((etype, n.path, w))
    for n in nodes:
        n.back = sorted(set(n.back), key=lambda e: (-e[2], e[0], e[1]))


def link_count(n: Node) -> int:
    return len({e[1] for e in n.edges} | {b[1] for b in n.back})


def fmt_value(v) -> str:
    if isinstance(v, (dict, list)):
        s = json.dumps(v, ensure_ascii=False, sort_keys=True)
        return f"`{s}`" if len(s) <= 300 else f"`{s[:297]}…`"
    s = " ".join(str(v).split())
    return s if len(s) <= 600 else s[:597] + "…"


def render(n: Node, date: str, existing_inferred: str | None) -> str:
    links = link_count(n)
    hub = links >= HUB_THRESHOLD or n.type in HUB_TYPES
    head = [
        "---",
        f"title: {yaml_str(n.title)}",
        "aliases: []",
        f"type: {n.type}",
        f"summary: {yaml_str(n.summary)}",
        f"last-verified: {date}",
        "source: snapshot",
        f"id: {yaml_str(n.id)}",
        f"table: {n.table}",
        f"links: {links}",
    ]
    if hub:
        head.append("hub: true")
    head.append("---")
    out = head + ["", f"# {n.title}", ""]
    if n.summary:
        out += [n.summary, ""]
    out += ["## Fields", ""]
    any_field = False
    for col in sorted(n.row):
        if col in HIDDEN or col in PROSE:
            continue
        v = n.row[col]
        if v is None or v == "" or v == [] or v == {}:
            continue
        out.append(f"- **{col}:** {fmt_value(v)}")
        any_field = True
    if not any_field:
        out.append("- *(no fields set)*")
    prose_written = False
    for k in PROSE:
        v = n.row.get(k)
        if isinstance(v, str) and v.strip():
            if not prose_written:
                out += ["", "## In his words", ""]
                prose_written = True
            out += [f"**{k}:** {' '.join(v.split())}", ""]
    out += ["", "## Links", ""]
    if n.edges:
        for etype, target, w, origin in n.edges:
            out.append(f"- {etype} → [[{target}]] (w={w}, {origin})")
    else:
        out.append("- *(none derived)*")
    if n.back:
        out += ["", "Linked from:", ""]
        for etype, src, w in n.back:
            out.append(f"- ← [[{src}]] ({etype}, w={w})")
    out += ["", "## Inferred", ""]
    if existing_inferred is not None and existing_inferred.strip():
        # Strip the surrounding blank lines, or every rebuild adds one more.
        out.append(existing_inferred.strip("\n"))
    else:
        out.append("<!-- The pass writes below this line: aliases from Reece's own words, relations it infers, pinned links (w=5). Kept across rebuilds. -->")
    return "\n".join(out).rstrip("\n") + "\n"


def read_inferred(path: Path) -> str | None:
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    marker = "\n## Inferred\n"
    i = text.find(marker)
    if i < 0:
        return None
    return text[i + len(marker):]


def front_matter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    fm: dict = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            v = v.strip()
            if v.startswith('"') and v.endswith('"'):
                try:
                    v = json.loads(v)
                except Exception:
                    pass
            fm[k.strip()] = v
    return fm


def write_index(nodes: list[Node], inferred_files: list[tuple[str, dict]], date: str) -> str:
    out = [
        "---",
        "title: Shadow index",
        "type: root",
        f"last-verified: {date}",
        "source: snapshot",
        "hub: true",
        "---",
        "",
        "# Shadow index",
        "",
        f"Rebuilt from the snapshot of {date}. {len(nodes)} derived files, {len(inferred_files)} inferred files.",
        "Hubs (15+ links, or a session) load but do not expand; see the contract, section 5.",
        "",
        "## Hubs",
        "",
    ]
    hubs = sorted((n for n in nodes if link_count(n) >= HUB_THRESHOLD or n.type in HUB_TYPES), key=lambda n: (-link_count(n), n.path))
    for n in hubs:
        out.append(f"- [[{n.path}]] · {n.type} · {link_count(n)} links")
    if not hubs:
        out.append("- *(none yet)*")
    out += ["", "## Inferred layer (Atlas and Codex, migrated)", ""]
    for rel, fm in sorted(inferred_files):
        out.append(f"- [[{rel}]] · {fm.get('type', '?')} · {fm.get('title', rel)}")
    if not inferred_files:
        out.append("- *(none yet)*")
    out += ["", "## Derived files by kind", ""]
    by_kind: dict[str, list[Node]] = defaultdict(list)
    for n in nodes:
        by_kind[n.kind].append(n)
    for kind in sorted(by_kind):
        ns = sorted(by_kind[kind], key=lambda n: n.path)
        out.append(f"### {kind} ({len(ns)})")
        out.append("")
        for n in ns:
            summ = f" — {n.summary}" if n.summary else ""
            out.append(f"- [[{n.path}]]{summ}")
        out.append("")
    return "\n".join(out).rstrip("\n") + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="report what would change; write nothing")
    args = ap.parse_args()

    if not SNAPSHOT.exists():
        print("no snapshot/ folder", file=sys.stderr)
        return 2
    tables = load_snapshot()
    date = snapshot_date()
    nodes, by_id, by_path = build_nodes(tables)
    derive_edges(nodes, by_id, tables)
    backlinks(nodes, by_path)

    # Inferred files: anything under shadow/ whose header says source: inferred.
    inferred_files: list[tuple[str, dict]] = []
    for p in sorted(SHADOW.rglob("*.md")):
        if p.name == "README.md" or p.name == "_index.md":
            continue
        fm = front_matter(p)
        if fm.get("source") == "inferred":
            inferred_files.append((p.relative_to(SHADOW).with_suffix("").as_posix(), fm))

    wanted: dict[Path, str] = {}
    for n in nodes:
        p = SHADOW / f"{n.path}.md"
        wanted[p] = render(n, date, read_inferred(p))
    wanted[SHADOW / "_index.md"] = write_index(nodes, inferred_files, date)

    # Stale derived files: a row that is gone takes its file with it. Inferred
    # files and READMEs are never removed.
    derived_dirs = {SHADOW / kind for kind, _ in PER_ROW.values()}
    stale: list[Path] = []
    for d in derived_dirs:
        if d.exists():
            for p in d.glob("*.md"):
                if p not in wanted and front_matter(p).get("source") == "snapshot":
                    stale.append(p)

    changed = [p for p, text in wanted.items() if not p.exists() or p.read_text(encoding="utf-8") != text]
    print(f"{len(nodes)} derived files from {len([t for t in PER_ROW if t in tables])} tables; {len(changed)} to write, {len(stale)} stale to remove; {len(inferred_files)} inferred files indexed")
    hubs = [n for n in nodes if link_count(n) >= HUB_THRESHOLD or n.type in HUB_TYPES]
    print(f"hubs: {len(hubs)}" + (" — " + ", ".join(n.path for n in hubs[:12]) if hubs else ""))
    if args.check:
        return 0
    for p, text in wanted.items():
        if p in changed:
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(text, encoding="utf-8")
    for p in stale:
        p.unlink()
    return 0


if __name__ == "__main__":
    sys.exit(main())
