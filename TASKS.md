# Tasks

Backlog for this project. Each task should reference the relevant `PBI-*`
requirement(s) and, once started, log its run under `docs/runs/<model-slug>/`.

**Branching convention:** one branch per *run*, not per model. Never commit
directly to `main` (see "Non-negotiable safety rules" #5 in
`.github/copilot-instructions.md`). Read-only audit runs use
`assessment/<model-slug>-<YYYY-MM-DD>`; runs that apply changes use
`fix/<model-slug>-<YYYY-MM-DD>`. Open a PR into `main` when the run's output
(report and/or applied changes) is ready for review; the branch can be deleted
after merge -- the persistent record lives in the `docs/runs/<model-slug>/`
folder on `main`, not in the branch.

**Model-slug:** kebab-case of the model name, e.g. "User Usage Analytics" ->
`user-usage-analytics`. Each model gets one folder under `docs/runs/` (and
under `docs/manual/` if it has manual-lane deliverables) that persists across
every run for that model.

**Prompt templates:** don't write a new Copilot prompt from scratch for each
task. Use [`docs/prompts/`](docs/prompts/README.md) — `audit-prompt.md` for
audit runs, `apply-prompt.md` for applying an approved plan,
`manual-lane-prompt.md` for manual-lane deliverables. Fill in the
placeholders and add a task entry here first (the prompts assume the task
entry already exists).

## TASK-001 -- Baseline assessment of test semantic model

**Status:** Complete (v3 merged, PR #6). Result: audit found 20 `Not Met`
requirements with an automatable-lane fix; see
`docs/runs/user-usage-analytics/2026-07-24-v3.md` for the approved plan
now executed as TASK-002.
**Owner:** GitHub Copilot (VS Code) + Power BI Modeling MCP
**Model:** User Usage Analytics (Power BI Desktop file) -- slug `user-usage-analytics`
**Branch:** `assessment/user-usage-analytics-2026-07-24-v3`

**What changed since v2:** Clarified that when an Automatable-lane row groups
several `PBI-*` ids together (e.g. "PBI-022 / 023 / 024 / 025 / 028"), the
plan's list of in-scope ids must be filtered to only the ids that are
individually `Not Met` — a `Met` sibling id in the same row must NOT appear
in the plan's scope list. `PBI-055` remains listed separately as a
verification gate, not a plan item.

**What changed since v1 (for reference):** (1) PBI-027/033 audits must read the model's
current `Synonyms` property via MCP before drafting proposals, instead of
assuming none exist (see `rules.yaml` `read_existing_state`, DECISIONS.md
D-009). (2) New requirement `PBI-056` added: spell-check all visible names and
descriptions (DECISIONS.md D-008) — v1 surfaced a typo ("Analitics") in the
model's own connection name. v2 confirmed this typo lives in the Desktop
connection/file title, out of PBI-056's table/column/measure scope — this
stays as a documented, accepted scope boundary (DECISIONS.md D-010), not a bug
to fix in v3.

**Goal:** Run the read-only Core workflow steps 1-4 from
`.github/copilot-instructions.md` (Connect -> Snapshot -> Audit -> Plan) against a
test semantic model. Produce a findings report before any write happens.

**Steps:**
1. Create and switch to branch `assessment/user-usage-analytics-2026-07-24-v3`.
2. Connect to the test model: `Connect to 'User Usage Analytics' in Power BI Desktop`
   (see "Connection protocol" in `.github/copilot-instructions.md`). The file
   must be open in Power BI Desktop first.
3. Export TMDL and commit it as the baseline snapshot
   (`docs/runs/user-usage-analytics/2026-07-24-v3-baseline/`).
4. Audit the model against every requirement in
   `docs/microsoft/requirements_matrix.md` (56 requirements, including
   `PBI-056`), using `rules.yaml` for the exact pass/fail check per rule. Do
   not skip Prerequisites (PBI-001-009) -- record them as Manual/Not-applicable
   if they can't be checked via MCP. For PBI-027/033, read current `Synonyms`
   state first. For PBI-056, spell-check every visible name and description.
5. Produce an audit table keyed by `PBI-*`: Met / Not Met / Manual / Blocked,
   with a one-line reason for each Not Met.
6. From "Not Met" results, build a change plan restricted to the
   **Automatable lane** table in `.github/copilot-instructions.md`. When a
   table row groups multiple `PBI-*` ids, include in the plan's scope list
   ONLY the ids that are individually `Not Met` from step 5 — double-check
   this before writing the summary line. Do NOT apply anything yet -- stop
   after the plan and post it in
   `docs/runs/user-usage-analytics/2026-07-24-v3.md` for human review.
7. Log approximate token cost as a new row in the existing
   `docs/metrics/token-usage.md` (append to it — do not create a new file or
   change its existing schema).
8. Commit and open a PR into `main`. Wait for explicit human approval before
   proceeding to Apply/Verify (Core workflow steps 5-8, in a new
   `fix/user-usage-analytics-<date>` branch as TASK-002).

**Out of scope for this task:** any write operation, any relationship change,
any RLS change, any Prep-for-AI / Approved-for-Copilot change (Manual lane --
produces a document, not a model change).

## TASK-002 -- Apply the approved TASK-001 v3 plan

**Status:** Approved, ready to start
**Owner:** GitHub Copilot (VS Code) + Power BI Modeling MCP
**Model:** User Usage Analytics (Power BI Desktop file) -- slug `user-usage-analytics`
**Branch:** `fix/user-usage-analytics-2026-07-24`
**Source plan:** `docs/runs/user-usage-analytics/2026-07-24-v3.md`,
sections 1-6 (section 7 is the PBI-055 verification gate, always applied,
not a separate item).

**Approved scope (human sign-off recorded here):**
1. **Naming (PBI-022/023/024/025):** `_Measures` -> `Measures`;
   `PostHog Application Usage Events[session_count]` -> `Session Count`.
   No other renames -- do not extend beyond what section 1 of the v3 plan
   names explicitly.
2. **Disambiguating descriptions (PBI-026):** add descriptions to the 6
   named identity/key fields in section 2 of the v3 plan.
3. **Measure descriptions (PBI-030):** add descriptions to the 10 named
   measures in section 3, plus the missing display folder for
   `WAU Trend Previous Week`.
4. **Column/table descriptions (PBI-031):** add descriptions to the 24
   named columns in section 4.
5. **Data categories (PBI-032):** set `Country`/`City` data categories on
   the 4 named geographic fields in section 5.
6. **Hide technical fields (PBI-034) -- SCOPE LIMITED:** hide only
   `PostHog Application Usage Events[session_count]` (already renamed to
   `Session Count` per item 1). Do **NOT** hide any other "key/helper"
   field from section 6's vague "join aids" language -- that part of the
   v3 plan was not specific enough to approve; propose a concrete list as
   a separate future task if desired.
7. **Verification gate (PBI-055):** required after every batch, per
   `.github/copilot-instructions.md` Non-negotiable safety rule #2 and #5.

**Explicitly out of scope (unchanged from TASK-001):** any relationship
edit, any RLS change, any Prep-for-AI / Verified Answers / AI Instructions
change, and any hide action beyond the one field named above.

**Steps (Core workflow steps 5-8 from `.github/copilot-instructions.md`):**
1. Create and switch to branch `fix/user-usage-analytics-2026-07-24`.
2. Re-connect to the model; confirm the baseline snapshot in
   `docs/runs/user-usage-analytics/2026-07-24-v3-baseline/` still matches
   the current model state before writing anything (if it doesn't, stop
   and report the drift instead of proceeding).
3. Apply the approved scope above inside a single `transaction_operations`
   Begin -> apply -> verify -> Commit. Use bulk `*_operations` Update with
   `definitions` arrays, batched by object type (rename batch, description
   batch, format/data-category batch, hidden-flag batch). If any step's
   verification fails, Rollback the whole transaction and report -- do not
   partially apply.
4. Verify (PBI-055): re-read every modified object; confirm relationships,
   dependent measures, field parameters, sort bindings, and security still
   resolve.
5. Export TMDL again -> commit as the post-change snapshot
   (`docs/runs/user-usage-analytics/2026-07-24-fix-after/`). The git diff
   between the v3 baseline and this snapshot is the change record.
6. Write a run report to `docs/runs/user-usage-analytics/2026-07-24-fix.md`:
   what changed per `PBI-*`, verification result, anything skipped from the
   approved scope and why.
7. Update `docs/microsoft/requirements_matrix.md`: change `Status` from
   `Pending` to `Met` for PBI-022, 023, 024, 025, 026, 030, 031, 032, 034,
   055 only (the ones actually changed/reverified here). Recompute the
   Requirement Summary table's Met/Pending counts.
8. Append one new row to the existing `docs/metrics/token-usage.md` (same
   schema -- do not create a new file).
9. Commit and open a PR into `main`. Wait for human review before merging
   (this PR contains actual model changes, review more carefully than the
   read-only audit PRs).

**Next task (not started):** TASK-003 -- Manual-lane deliverables (synonyms
proposal, RLS security-validation evidence) for `user-usage-analytics`,
per `docs/manual/{model}/` conventions in `.github/copilot-instructions.md`.
