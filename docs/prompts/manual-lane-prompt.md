# Manual-Lane Prompt Template

Use for producing Manual-lane deliverables (documents, not model changes) for
a model that has already had its automatable-lane changes applied. Maps to
the "Manual lane" table in `.github/copilot-instructions.md`.

This task never writes to the model itself — only to `docs/manual/{model}/`.

---

```
You are working in the PowerBI-Copilot-Readiness repository. Read and follow
.github/copilot-instructions.md as your operating manual. Read TASKS.md and
find {TASK_ID} for this run.

Produce Manual-lane deliverables for model "{MODEL_NAME}" (slug: {MODEL_SLUG}):

0. **MANDATORY pre-flight sync (do not skip):**
   ```
   git fetch origin
   git checkout main
   git pull origin main
   git rev-parse HEAD
   git rev-parse origin/main
   ```
   The two hashes must match exactly. If a branch for this task already
   exists locally or on origin from an earlier attempt, delete it first and
   branch fresh from this just-pulled `main`.
1. Create and switch to branch docs/{MODEL_SLUG}-manual-lane-{DATE}.
2. Connect using: Connect to '{MODEL_NAME}' in Power BI Desktop
   (read-only -- no write operations in this task).
3. PBI-027 / PBI-033 (Synonyms): read the current Synonyms state (via MCP if
   exposed, or the exported TMDL culture file as a fallback). Draft a
   synonym proposal in docs/manual/{MODEL_SLUG}/synonyms.md covering only
   tables/fields that are missing synonyms -- do not duplicate synonyms that
   already exist. Cross-check proposed terms against
   docs/context/business-glossary.md where available; do not invent
   business terminology that isn't already documented or evident in the
   model.
4. PBI-035 (RLS): document the current security-role/permission state (roles,
   table permissions if any) and produce security-validation evidence in
   docs/manual/{MODEL_SLUG}/security-validation.md. This is documentation and
   a recommendation only -- never an automated RLS change, per the
   relationship/security invariants in .github/copilot-instructions.md and
   rules.yaml excluded_automation.
5. If relevant Prep-for-AI planning is in scope for this task (check
   {TASK_ID} in TASKS.md), also draft:
   - AI data schema field include/exclude list
   - Verified-answer trigger phrases and intended answers for key questions
   - AI instructions text (business context + term mappings)
   as docs/manual/{MODEL_SLUG}/ai-preparation.md, per the Manual lane table.
6. Commit these files and open a PR into main. No model write operations
   should appear in this PR's diff -- only documentation under docs/manual/.
```

---

## Placeholders

- `{MODEL_NAME}` — exact Power BI Desktop file/connection name.
- `{MODEL_SLUG}` — kebab-case of the model name.
- `{DATE}` — `YYYY-MM-DD` for this run.
- `{TASK_ID}` — the `TASK-*` id in `TASKS.md` recording scope for this run.
