# Reusable Copilot Prompts

Templates for the recurring task types in this project, so each new model
doesn't require re-deriving the prompt from scratch. Derived from the
`user-usage-analytics` runs (TASK-001 v1–v3, TASK-002).

| Template | Use for | Maps to |
|---|---|---|
| [`audit-prompt.md`](audit-prompt.md) | First read-only assessment of a model (or a re-run if the audit itself needs fixing) | Core workflow steps 1–4 in `.github/copilot-instructions.md` |
| [`apply-prompt.md`](apply-prompt.md) | Applying a human-approved plan from an audit run | Core workflow steps 5–8 |
| [`manual-lane-prompt.md`](manual-lane-prompt.md) | Producing Manual-lane deliverables (synonyms, RLS evidence, AI-prep documents) | Manual lane table in `.github/copilot-instructions.md` |

## How to use a template

1. Copy the template's prompt block.
2. Replace every placeholder:
   - `{MODEL_NAME}` — the exact Power BI Desktop file/connection name, e.g. "User Usage Analytics".
   - `{MODEL_SLUG}` — kebab-case of the model name, e.g. `user-usage-analytics`.
   - `{DATE}` — `YYYY-MM-DD` for today's run.
   - `apply-prompt.md` additionally needs `{AUDIT_DATE}` (the date of the
     audit run whose plan is being applied, if different from today) and
     `{TASK_ID}` (the `TASK-*` id in `TASKS.md` recording the approved scope).
3. Add a `TASKS.md` entry for the run **before** handing the prompt to
   Copilot, following the `docs/runs/<model-slug>/` and per-run-branch
   conventions already documented there. The prompt assumes the task entry
   already exists — it doesn't create one.
4. If a run needs a fix mid-stream (like `user-usage-analytics` needed v2/v3),
   increment with a `-v2`, `-v3`, ... suffix on the branch and filenames, and
   record what changed between versions in `TASKS.md`, the way TASK-001 does.

## Known refinements already baked into these templates

These came from real issues found during the `user-usage-analytics` runs —
don't remove them when adapting a template:

- Audit must read current `Synonyms` state via MCP (fallback: exported TMDL
  culture file) before drafting a PBI-027/033 proposal — never assume blank.
- PBI-056 spelling checks are scoped to table/column/measure objects only;
  file/connection/report titles are out of scope (DECISIONS.md D-010).
- When the Automatable lane groups several `PBI-*` ids in one table row, the
  plan's scope summary must list only the ids that are individually `Not Met`
  — a `Met` sibling in the same row must not appear (DECISIONS.md, TASKS.md
  TASK-001 v3 notes).
- `docs/metrics/token-usage.md` must be appended to, never recreated with a
  different schema — check `main` for the current file before assuming it's
  missing.
