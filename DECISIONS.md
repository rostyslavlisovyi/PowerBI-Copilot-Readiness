# Architecture & Rule Decisions

> Deliberate decisions taken while building the Copilot Readiness rule set.
> Recorded so they are not re-litigated later.

---

## D-001 — Synonyms handled via AI instructions, not model synonyms
The PBI Modeling MCP exposes no synonym write operation. Synonyms are therefore
delivered through AI instructions in Power BI Service (PBI-072), not written into
the model. Refs: MS-PREP-04.

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
(skills-for-fabric). PBI-042 is therefore a hard check, not a soft one.

## D-007 — Processing unit is one table, with a review gate
Two phases: assessment scans the whole model once (matrix + relationships.lock +
queue); iteration processes ONE table at a time and stops for review before the
next. Queue is ordered by simplicity (easiest first) for the trial stage.
