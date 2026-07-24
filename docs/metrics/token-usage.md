# Token Usage Ledger

Tracks approximate token cost per run, so cost can be compared across models,
tasks, and over time. One row per run (matches `docs/runs/<model-slug>/`).

Numbers are self-reported by the agent (Copilot/VS Code usage panel or
equivalent) at the end of a run — approximate, not billing-accurate.

| Date | Model (slug) | Task | Agent | Tokens (approx.) | Notes |
|---|---|---|---|---:|---|
| 2026-07-24 | user-usage-analytics | TASK-001 v1 (baseline + read-only audit) | GitHub Copilot (VS Code) + Power BI Modeling MCP | 825,000 | First run against a real model; includes exporting/reading full TMDL baseline (~28.6k lines) as context, which likely dominates the token count. |
| 2026-07-24 | user-usage-analytics | TASK-001 v2 (re-run: synonyms read-check + PBI-056 spelling pass) | GitHub Copilot (VS Code) + Power BI Modeling MCP | 135,000 | ~6x cheaper than v1 despite auditing one more requirement (56 vs 55) and adding two read steps. Likely because the model/MCP session context was already warm and the TMDL export didn't need re-reading from scratch in the same way — worth confirming on v3 whether this holds. |
| 2026-07-24 | user-usage-analytics | TASK-001 v3 (re-run: grouped-id scope fix) | GitHub Copilot (VS Code) + Power BI Modeling MCP | 160,000 | Similar to v2, with branch rotation, fresh baseline export, 56-requirement read-only audit, synonym-state read, PBI-056 spelling pass, and corrected automatable-lane scope filtering for grouped requirement rows. |
| 2026-07-24 | user-usage-analytics | TASK-002 (approved-scope apply + verification) | GitHub Copilot (VS Code) + Power BI Modeling MCP | 230,000 | Transactional apply run with precheck drift validation, two full rollbacks for failed attempts, final successful commit, post-change export, and full PBI-055 verification reads. |

## How to add a row

After each run, append one row here in the same PR that adds the
`docs/runs/<model-slug>/<date>.md` report. Include:

- **Task** — which `TASK-*` from `TASKS.md`.
- **Agent** — which tool/model ran it (e.g. "GitHub Copilot (VS Code)", "Claude Sonnet 5").
- **Tokens** — best available estimate; note the source (IDE panel, API usage
  dashboard, etc.) if it's not a plain agent self-report.
- **Notes** — anything that explains an unusually high/low number, e.g. a large
  TMDL export dominating context, a retry, a multi-file audit.

**Append to this file — do not create a new one or change its schema.** If the
file appears missing when starting a run, check `main` again before assuming
it doesn't exist.

## Observations

- v1 → v2 dropped from 825k to 135k tokens (~6x) despite v2 covering more
  ground (56 requirements instead of 55, plus two new read-before-propose
  steps). Re-reading a large TMDL export into context on every run may be the
  dominant cost driver, more than the number of requirements checked.
