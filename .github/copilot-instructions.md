# Copilot Agent Instructions — Power BI Copilot Readiness

> Operating manual for any AI agent (GitHub Copilot, Devin, etc.) working in this
> repository and connected to the **Power BI Modeling MCP** server
> (<https://github.com/microsoft/powerbi-modeling-mcp>).
> Goal: bring existing Power BI semantic models to Copilot-ready state by applying
> the requirements in `docs/microsoft/requirements_matrix.md`, using only supported
> MCP operations — safely and verifiably.

---

## Scope

**In scope (semantic model metadata & structure):** tables, columns, measures,
relationships, security roles/RLS, descriptions, format strings, display folders,
hidden flags, naming, hierarchies, calculation groups, translations.

**Out of scope for the MCP — never attempt via MCP:** report pages/visuals, diagram
layout, and the Power BI Service "Prep data for AI" features (AI data schema,
Verified answers, AI instructions), marking "Approved for Copilot", and Copilot
question testing. These are applied manually in the Service (see "Manual lane").

---

## Non-negotiable safety rules

1. **Backup first.** No write until a snapshot exists. Export TMDL
   (`database_operations` ExportTMDL / ExportToTmdlFolder) and commit it as baseline.
2. **Transactions always.** Wrap writes in `transaction_operations`:
   Begin → apply → verify → Commit; on any verify failure, Rollback.
   For batches use `options.useTransaction=true`, `options.continueOnError=false`.
3. **Plan before write.** Run a read-only audit and produce a change plan keyed by
   `PBI-*` id. Do not write until the plan is approved.
4. **Least change.** Modify only what a requirement demands. Never delete objects to
   "clean up" unless explicitly instructed.
5. **Git discipline.** Never push to `main`. One branch per *run*, not per
   model: `assessment/<model-slug>-<YYYY-MM-DD>` for read-only audits,
   `fix/<model-slug>-<YYYY-MM-DD>` for runs that apply changes. Commit, open a
   PR into `main`. A human reviews and merges; the branch can then be deleted.
   The permanent record is the `docs/runs/<model-slug>/` folder on `main`
   (one folder per model, every run's files inside it) — not the branch.
6. **Data privacy.** The MCP sends metadata and DAX query *results* to the LLM.
   Do NOT run DAX that returns row-level client / PII / financial data.
   Metadata-only operations are fine; prefer definition/schema checks for validation.
7. **Confirmations.** The server elicits approval before the first write and first
   query. Do not use `--skipconfirmation` on production models.

---

## Connection protocol

Connect before any operation, using one of:

- Desktop: `Connect to '[File Name]' in Power BI Desktop`
- Fabric: `Connect to semantic model '[Name]' in Fabric Workspace '[Workspace]'`
- PBIP/TMDL: `Open semantic model from PBIP folder '[path to TMDL]'`

Prefer the PBIP/TMDL folder workflow when the model lives in this repo, so every
change is diffable in git.

---

## Core workflow (per model)

1. **Connect** (above).
2. **Snapshot:** ExportTMDL → commit as baseline.
3. **Audit (READ only):** enumerate tables/columns/measures/relationships/roles;
   for each requirement in `requirements_matrix.md`, detect pass/fail.
   Output an audit table keyed by `PBI-*`.
4. **Plan:** list concrete changes (object, property, new value, `PBI-*`, `Source_ID`).
5. **Apply (WRITE, in transaction, bulk):** use `*_operations` Update with
   `definitions` arrays. Batch by object type.
6. **Verify:** re-read modified objects; confirm each targeted `PBI-*` now passes.
   Optionally validate DAX via `dax_query_operations` (definition validation, not
   data dumps).
7. **Snapshot after:** ExportTMDL → commit; the git diff is the change record.
8. **Report:** status per `PBI-*` — Met / Pending / Manual / Blocked.

---

## Automatable lane — requirement → MCP operation

IDs below match the current `docs/microsoft/requirements_matrix.md` (PBI-001..055) and
`rules.yaml` `automatable: true` flags. Do not use any PBI-06x/07x/08x identifiers —
`rules.yaml` explicitly rejects them as historical validation fixtures.

| Requirement (PBI-*) | Tool | Operation / property |
|---|---|---|
| PBI-022 / 023 / 024 / 025 / 028 naming | table/column/measure_operations | Rename |
| PBI-026 disambiguating descriptions | table/column/measure_operations | Update `.description` |
| PBI-030 / 031 descriptions | table/column/measure_operations | Update `.description` (front-load business meaning in first 200 chars per MS-COP-03 / D-006) |
| PBI-032 data types, format strings, data categories | column/measure_operations | Update `.formatString`, `.dataCategory` |
| Display folders (implementation detail of PBI-030/031 organization, no dedicated PBI id) | measure_operations | Update `.displayFolder` |
| PBI-034 hide technical fields | table/column/measure_operations | Update `.isHidden = true` |
| PBI-055 model integrity re-verification | read-only re-query of modified/dependent objects | Confirm relationships, measures, field parameters, sort bindings, security still resolve |

**Not automatable — assessment/report only:**

- PBI-010–021 (modeling & relationships): relationships are a protected invariant
  (`rules.yaml` `relationship_invariant`, `excluded_automation`). The agent never
  creates, updates, activates, deactivates, or changes cardinality/cross-filter
  direction. It assesses and reports only.
- Date table designation and hierarchies, and calculation-group documentation, are
  not yet assigned a `PBI-*` id in the current matrix (`MS-MODEL-13` and `MS-MODEL-09`
  are `Planned` sources). Do not automate these until they are added to
  `requirements_matrix.md` with an evidence classification and human review.
- Multi-language/translation support is not yet in the matrix either; propose it as
  a new project requirement before using `culture_operations` / `object_translation_operations`.

---

## Manual lane — Power BI Service, NOT the MCP

The agent GENERATES the content and writes it under `docs/` for a human to apply.
IDs match `docs/microsoft/requirements_matrix.md` (PBI-001..055).

| Requirement | Deliverable the agent produces |
|---|---|
| PBI-001–009 Prerequisites | Recorded confirmation of tenant/capacity/region/access settings (admin-provided; not detectable via MCP) |
| PBI-010–021 Modeling & Relationships | Assessment findings and recommendations only — never auto-applied (relationship invariant) |
| PBI-027 / 033 Synonyms | Proposed synonym list (`docs/manual/{model}/synonyms.md`) — the MCP exposes no synonym write |
| PBI-035 RLS | Security validation evidence (`docs/manual/{model}/security-validation.md`) — excluded from automation |
| PBI-036–038 AI data schema (Simplify) | List of fields to include/exclude for Copilot |
| PBI-039–042 Verified answers | Trigger phrases + intended answer per key question |
| PBI-043–046 AI instructions | Model AI-instructions text incl. term mappings (this is where "synonyms" are handled — the MCP exposes no synonym write) |
| PBI-047 Approved for Copilot | Checklist confirmation only |
| PBI-048 / 049 Copilot indexing | Indexing review notes (Service/Desktop settings) |
| PBI-050–054 Testing | Test question set + expected answers, retest plan |

---

## Capability verification note

The local server's `Help` may enumerate a **subset** of tools. The official server
also exposes `dax_query_operations`, `calculation_group_operations`,
`user_hierarchy_operations`, `culture_operations`, `object_translation_operations`,
and perspective member management. Before relying on any of these, call the tool's
`Help` to confirm it exists in the installed version; if absent, fall back
(e.g., document in a description) and flag for a server update.

---

## Run log

For each run, append to `docs/runs/<model-slug>/<YYYY-MM-DD>.md` (one folder
per model, per the branching convention above): model name, baseline commit,
changes applied (per `PBI-*`), verification result, and outstanding manual
items.
