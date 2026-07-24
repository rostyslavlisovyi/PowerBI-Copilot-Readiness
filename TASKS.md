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

## TASK-001 -- Baseline assessment of test semantic model

**Status:** Re-run (v2) — original run (PR #4) was reverted; this run adds two
audit-quality fixes discovered in v1 (see notes below). Delete the old
`assessment/user-usage-analytics-2026-07-24` branch (local + remote) before
starting, or use `-v2` suffix if the old branch can't be deleted.
**Owner:** GitHub Copilot (VS Code) + Power BI Modeling MCP
**Model:** User Usage Analytics (Power BI Desktop file) -- slug `user-usage-analytics`
**Branch:** `assessment/user-usage-analytics-2026-07-24-v2`

**What changed since v1:** (1) PBI-027/033 audits must read the model's
current `Synonyms` property via MCP before drafting proposals, instead of
assuming none exist (see `rules.yaml` `read_existing_state`, DECISIONS.md
D-009). (2) New requirement `PBI-056` added: spell-check all visible names and
descriptions (DECISIONS.md D-008) — v1 surfaced a typo ("Analitics") in the
model's own connection name that a spelling pass should have caught and
reported.

**Goal:** Run the read-only Core workflow steps 1-4 from
`.github/copilot-instructions.md` (Connect -> Snapshot -> Audit -> Plan) against a
test semantic model. Produce a findings report before any write happens.

**Steps:**
1. Create and switch to branch `assessment/user-usage-analytics-2026-07-24-v2`.
2. Connect to the test model: `Connect to 'User Usage Analytics' in Power BI Desktop`
   (see "Connection protocol" in `.github/copilot-instructions.md`). The file
   must be open in Power BI Desktop first.
3. Export TMDL and commit it as the baseline snapshot
   (`docs/runs/user-usage-analytics/2026-07-24-v2-baseline/`).
4. Audit the model against every requirement in
   `docs/microsoft/requirements_matrix.md` (now 56 requirements, including
   `PBI-056`), using `rules.yaml` for the exact pass/fail check per rule. Do
   not skip Prerequisites (PBI-001-009) -- record them as Manual/Not-applicable
   if they can't be checked via MCP. For PBI-027/033, read current `Synonyms`
   state first. For PBI-056, spell-check every visible name and description.
5. Produce an audit table keyed by `PBI-*`: Met / Not Met / Manual / Blocked,
   with a one-line reason for each Not Met.
6. From "Not Met" results, build a change plan restricted to the
   **Automatable lane** table in `.github/copilot-instructions.md`. Do NOT
   apply anything yet -- stop after the plan and post it in
   `docs/runs/user-usage-analytics/2026-07-24-v2.md` for human review.
7. Log approximate token cost in `docs/metrics/token-usage.md` in the same PR.
8. Commit and open a PR into `main`. Wait for explicit human approval before
   proceeding to Apply/Verify (Core workflow steps 5-8, in a new
   `fix/user-usage-analytics-<date>` branch as TASK-002).

**Out of scope for this task:** any write operation, any relationship change,
any RLS change, any Prep-for-AI / Approved-for-Copilot change (Manual lane --
produces a document, not a model change).

**Next task (not started):** TASK-002 -- apply approved automatable changes
from TASK-001's plan, in transaction, then re-verify and update
`requirements_matrix.md` `Status` column from `Pending` to `Met` per
requirement.
