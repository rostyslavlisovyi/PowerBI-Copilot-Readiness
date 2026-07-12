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
5. **Git discipline.** Never push to `main`. Create a branch, commit, open a PR.
   A human reviews and merges.
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

| Requirement (PBI-*) | Tool | Operation / property |
|---|---|---|
| PBI-031 / 040 / 041 / 042 descriptions | table/column/measure_operations | Update `.description` (key info in first 200 chars) |
| Format strings | column/measure_operations | Update `.formatString` |
| Display folders | measure_operations | Update `.displayFolder` |
| PBI-060 / 061 / 062 hide technical fields | table/column/measure_operations | Update `.isHidden = true` |
| PBI-020..023 naming | table/column/measure_operations | Rename |
| PBI-045 data category | column_operations | Update `.dataCategory` |
| PBI-013 / 014 relationships | relationship_operations | Create / Update / Activate / Deactivate |
| PBI-017 date table / hierarchies | table_operations MarkAsDateTable; user_hierarchy_operations | designate date table; build hierarchies |
| PBI-065 RLS | security_role_operations | Create + CreatePermissions |
| PBI-043 calc-group docs | calculation_group_operations (verify) else column description | document logic |
| Multi-language (optional) | culture_operations + object_translation_operations | translations |

---

## Manual lane — Power BI Service, NOT the MCP

The agent GENERATES the content and writes it under `docs/` for a human to apply:

| Requirement | Deliverable the agent produces |
|---|---|
| PBI-070 AI data schema (Simplify) | list of fields to include/exclude for Copilot |
| PBI-071 / 071a Verified answers | trigger phrases + intended answer per key question |
| PBI-072 / 072a AI instructions | model AI-instructions text incl. term mappings (this is where "synonyms" are handled — the MCP exposes no synonym write) |
| PBI-074 Approved for Copilot | checklist confirmation only |
| PBI-080..082 Copilot testing + HCAAT | test question set + expected answers |

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

For each run, append to `docs/runs/<model>-<YYYY-MM-DD>.md`:
model name, baseline commit, changes applied (per `PBI-*`), verification result,
and outstanding manual items.
