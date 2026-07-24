# Audit Prompt Template

Use for a first read-only assessment of a model, or a re-run (`-v2`, `-v3`, ...)
if a previous audit needs correcting. Maps to Core workflow steps 1–4 in
`.github/copilot-instructions.md`.

Add a `TASKS.md` entry for this run before using this prompt (see
`docs/prompts/README.md`).

---

```
You are working in the PowerBI-Copilot-Readiness repository. Read and follow
.github/copilot-instructions.md as your operating manual. Read TASKS.md and
find the task for this run.

Execute a read-only baseline assessment for model "{MODEL_NAME}"
(slug: {MODEL_SLUG}):

0. **MANDATORY pre-flight sync (do not skip):**
   ```
   git fetch origin
   git checkout main
   git pull origin main
   git rev-parse HEAD
   git rev-parse origin/main
   ```
   The two hashes must match exactly. If a branch for this task already
   exists locally or on origin from an earlier attempt, delete it first
   (`git push origin --delete <branch>`, `git branch -D <branch>`) and
   branch fresh from this just-pulled `main`. Do not resume or branch from
   any other state.
1. If re-running the same day, delete any existing
   assessment/{MODEL_SLUG}-{DATE}* branch (local and remote) first, then
   create and switch to: assessment/{MODEL_SLUG}-{DATE}
2. Connect using: Connect to '{MODEL_NAME}' in Power BI Desktop
   (or the Fabric/PBIP connection string — see "Connection protocol" in
   .github/copilot-instructions.md)
3. Export TMDL and save it as the baseline snapshot in
   docs/runs/{MODEL_SLUG}/{DATE}-baseline/
4. Run a READ-ONLY audit of the model against ALL requirements currently in
   docs/microsoft/requirements_matrix.md, using rules.yaml as the exact
   pass/fail check for each rule. Do not skip Prerequisites (PBI-001-009) --
   record them as Manual if they can't be checked via MCP.
   - For PBI-027/033: read the model's current Synonyms property first (via
     MCP if exposed, or from the exported TMDL culture file as a fallback)
     before drafting any synonym proposal. Never assume a blank slate.
   - For PBI-056: spell-check every visible table/column/measure name and
     description in the report's display language. File/connection/report
     titles are out of scope for this check.
5. Output a table: PBI-* | Met/Not Met/Manual/Blocked | one-line reason.
6. From the "Not Met" results, build a change plan restricted ONLY to the
   "Automatable lane" table in .github/copilot-instructions.md.
   IMPORTANT: when a table row groups several PBI-* ids together (e.g.
   "PBI-022/023/024/025/028"), include in your plan's scope summary ONLY the
   ids that are individually Not Met from step 5 -- double-check this before
   writing the summary line. List any verification-gate id (PBI-055)
   separately, not as a plan item. Do NOT apply anything yet -- stop after
   the plan.
7. Write the result (audit + plan) to docs/runs/{MODEL_SLUG}/{DATE}.md
8. Sync any requirement found `Met` purely by observation (no automatable
   fix needed, e.g. star schema already correct, measures already English)
   into `docs/microsoft/requirements_matrix.md`'s `Status` column now --
   don't wait for an apply/fix task to do this. Only requirements the audit
   found `Not Met` stay `Pending` here (they'll update after an apply task).
   Recompute the Requirement Summary table.
9. Append one new row to the EXISTING docs/metrics/token-usage.md (same
   schema as the current rows there) -- do not create a new file or change
   its schema. If the file appears missing, re-check main before assuming
   it doesn't exist.
10. Commit and open a PR into main.

Do not perform any write operations. Do not touch relationships. This is a
read-only step. Stop and wait for my approval of the plan.
```

---

## Placeholders

- `{MODEL_NAME}` — exact Power BI Desktop file/connection name.
- `{MODEL_SLUG}` — kebab-case of the model name.
- `{DATE}` — `YYYY-MM-DD`, append `-v2`/`-v3` etc. to both the branch name and
  filenames if this is a re-run on the same day.
