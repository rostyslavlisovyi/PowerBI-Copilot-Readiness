# Apply Prompt Template

Use for applying a human-approved plan from a prior audit run. Maps to Core
workflow steps 5–8 in `.github/copilot-instructions.md`.

Requires a `TASKS.md` entry that records the **approved scope** explicitly
(see TASK-002 for `user-usage-analytics` as an example) — this prompt applies
only what's recorded there, never the full source plan by default, since a
plan may contain vague or unapproved items (e.g. TASK-002 excluded part of
its source plan's "hide fields" section for being too vague to approve as
written).

---

```
You are working in the PowerBI-Copilot-Readiness repository. Read and follow
.github/copilot-instructions.md as your operating manual. Read TASKS.md and
find {TASK_ID}, which records the human-approved scope for this run.

Apply {TASK_ID}'s approved scope for model "{MODEL_NAME}" (slug: {MODEL_SLUG}):

1. Create and switch to branch fix/{MODEL_SLUG}-{DATE}.
2. Re-connect to the model; confirm the baseline snapshot in
   docs/runs/{MODEL_SLUG}/{AUDIT_DATE}-baseline/ still matches the current
   model state before writing anything. If it doesn't, STOP and report the
   drift instead of proceeding.
3. Apply ONLY the scope recorded as approved in TASKS.md {TASK_ID} -- do not
   apply anything from the source audit plan that isn't explicitly listed as
   approved there, even if it appears in the plan document. Wrap everything
   in a single transaction_operations Begin -> apply -> verify -> Commit.
   Batch by object type (rename batch, description batch, format/data-category
   batch, hidden-flag batch, etc). If any verification step fails, Rollback
   the whole transaction and report -- do not partially apply.
4. Verify (PBI-055): re-read every modified object; confirm relationships,
   dependent measures, field parameters, sort bindings, and security still
   resolve.
5. Export TMDL again -> commit as the post-change snapshot
   (docs/runs/{MODEL_SLUG}/{DATE}-fix-after/). The git diff between the
   baseline and this snapshot is the change record.
6. Write a run report to docs/runs/{MODEL_SLUG}/{DATE}-fix.md: what changed
   per PBI-*, verification result, and anything skipped from the approved
   scope and why.
7. Update docs/microsoft/requirements_matrix.md: change Status from Pending
   to Met only for the PBI-* ids actually changed/reverified in this run.
   Recompute the Requirement Summary table's Met/Pending counts.
8. Append one new row to the existing docs/metrics/token-usage.md (same
   schema -- do not create a new file).
9. Commit and open a PR into main. Note in the PR description that this PR
   contains actual model changes, not just documentation/read-only findings.
```

---

## Placeholders

- `{MODEL_NAME}` — exact Power BI Desktop file/connection name.
- `{MODEL_SLUG}` — kebab-case of the model name.
- `{DATE}` — `YYYY-MM-DD` for this apply run.
- `{AUDIT_DATE}` — the date (and `-v2`/`-v3` suffix if applicable) of the
  audit run whose baseline snapshot this apply run re-verifies against.
- `{TASK_ID}` — the `TASK-*` id in `TASKS.md` that records the human-approved
  scope for this run.
