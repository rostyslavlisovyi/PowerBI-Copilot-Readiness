# Architecture & Rule Decisions

> Deliberate decisions taken while building the Copilot Readiness rule set.
> Recorded so they are not re-litigated later.

---

## D-001 — Synonyms handled via AI instructions, not model synonyms
The PBI Modeling MCP exposes no synonym write operation. Synonyms are therefore
delivered through AI instructions in Power BI Service (PBI-043/PBI-044), not written
into the model. Refs: MS-PREP-04.

## D-002 — RLS is out of scope
Row-level security is intentionally excluded from this rule set. RLS + Copilot must
be tested per-model by a human; automating it is out of scope here.

## D-003 — Relationships are an invariant, never edited
Relationships are captured (relationships.lock) at assessment, guarded on every
per-table verify, and re-checked at finalization. They are never created, updated,
or deleted by the agent. Renames/hides that could touch a relationship carry
`relationship_guard: true`.

## D-004 — Name/description contradiction is flag-only
When a measure's name and description contradict each other (e.g. "Users on Current
Application Version" whose description describes an OUTDATED version), the agent does
NOT auto-fix and does NOT propose a fix. It records the case in
docs/manual/name-description-conflicts.md and moves on. Rationale: the correct fix
(rename vs rewrite) is a human authoring decision; guessing risks breaking dependent
measures and enshrining wrong meaning that Copilot would then state confidently.

## D-005 — Descriptions are never generated without business context
Per Microsoft guidance (skills-for-fabric), AI-only descriptions restate structure
and add no value. Branch A of PBI-031 writes descriptions only from
docs/context/business-glossary.md (or existing model context), never invented.

## D-006 — 200-char front-loading is a Microsoft rule, not an assumption
Copilot reads only the first 200 chars of a description (MS-COP-03). Front-loading
business meaning and not restating the name is Microsoft's own recommendation
(skills-for-fabric). PBI-031 is therefore a hard check, not a soft one.

## D-007 — Processing unit is one table, with a review gate
Two phases: assessment scans the whole model once (matrix + relationships.lock +
queue); iteration processes ONE table at a time and stops for review before the
next. Queue is ordered by simplicity (easiest first) for the trial stage.

## D-008 — Spelling check added as PBI-056 (Project evidence, no Microsoft source)
TASK-001's first real run against `user-usage-analytics` surfaced a spelling error
in the model's own internal connection name ("Analitics"). No Microsoft source
requires a spelling check, so this is added as the project's first `Project`
evidence-level requirement (ADR-0001) rather than attributed to a `Source_ID`.
Scope: visible table/column/measure names and their descriptions, checked in the
report's display language. Remediation reuses the existing rename/description-
update automatable operations already defined for PBI-022–031; PBI-056 only adds
a detection step, not a new MCP operation.

## D-009 — Manual-lane items are still read via MCP where the property is readable
PBI-027/033 (synonyms) were being marked `Manual` in audits without checking
whether synonyms already exist in the model — the MCP has no *write* operation
for synonyms, but reading the `Synonyms` property is a separate capability.
`rules.yaml` now requires reading current state first for both, so audit status
reflects the model's real content instead of assuming nothing exists. This is a
general principle, not specific to synonyms: a requirement is only marked
`Manual` outright when its evidence cannot be read via MCP at all (e.g.
tenant/capacity settings, PBI-001–009), not merely because remediation requires
a human step.
