# Requirements Matrix — Power BI Copilot Readiness

> The central project artifact. Every readiness requirement is traced to an official Microsoft source or explicitly identified as a project-specific rule.

## Document Relationships

This matrix is the canonical registry of readiness requirement identifiers.

- [`requirements_matrix.md`](requirements_matrix.md) defines the authoritative `PBI-*` requirements, categories, evidence levels, priorities, and assessment statuses.
- [`references.md`](references.md) defines every permitted `Source_ID`, its Microsoft Learn URL, review status, and verified findings.
- [`review_notes.md`](review_notes.md) records source ambiguities, evidence limitations, and unresolved interpretation questions.
- [`../../rules.yaml`](../../rules.yaml) maps applicable `PBI-*` requirements to executable detection, remediation, and verification rules.
- [`../adr/ADR-0001-evidence-classification.md`](../adr/ADR-0001-evidence-classification.md) defines the evidence-classification decision used by this matrix.

A change to a `PBI-*` identifier, requirement meaning, `Source_ID`, or evidence level must be reviewed against all linked documents.

## Legend

**Priority:** 🔴 Must-have · 🟡 Recommended · 🟢 Nice-to-have

**Status:** `Pending` · `In Progress` · `Met` · `N/A` · `Blocked`

**Evidence Level:** `Direct` · `Derived` · `Recommended` · `Project`

Columns: **ID · Requirement · Category · Source_ID · Evidence Level · Priority · Status · Notes**

> Evidence classifications are considered verified only when every supporting `Source_ID` is marked as `Verified` in [`references.md`](references.md). Requirements mapped to a `Planned` or `Reviewed` source remain pending verification.

## Governance Rules

- `PBI-*` identifiers are stable and must not be reused for a different requirement.
- Every non-project requirement must reference at least one registered `Source_ID`.
- Every referenced `Source_ID` must exist in the Source Registry in [`references.md`](references.md#source-registry).
- Requirements mapped to multiple sources are verified only when all supporting sources are `Verified`.
- [`rules.yaml`](../../rules.yaml) must not use `PBI-*` identifiers outside the range defined in this matrix.
- Implementation guidance in `rules.yaml` must not be represented as an additional Microsoft requirement unless it is added here with an evidence classification.
- Source ambiguities and incomplete evidence must be recorded in [`review_notes.md`](review_notes.md).
- Changes to requirement numbering or meaning must include a repository-wide reference check.

## Prerequisites

| ID | Requirement | Category | Source_ID | Evidence Level | Priority | Status | Notes |
|---|---|---|---|---|---|---|---|
| PBI-001 | Copilot access is enabled through the `Users can use Copilot and other features powered by Azure OpenAI` setting | Prerequisites | MS-FAB-02 | Direct | 🔴 | Pending | Verify the effective tenant or delegated capacity configuration for the target experience |
| PBI-002 | The workspace uses a paid Fabric capacity of F2 or higher or a Power BI Premium capacity of P1 or higher | Prerequisites | MS-FAB-03 | Direct | 🔴 | Pending | Trial capacities, trial SKUs, Pro-only workspaces, and PPU-only workspaces do not directly satisfy the standard capacity requirement |
| PBI-003 | The capacity is located in a region supported for Copilot | Prerequisites | MS-FAB-03 | Direct | 🔴 | Pending | Validate against the current Microsoft Fabric region availability documentation |
| PBI-004 | Cross-region Azure OpenAI processing is enabled when the capacity region requires it | Prerequisites | MS-FAB-02 | Direct | 🔴 | Pending | Conditional requirement; mark `N/A` only when cross-region processing is not required for the applicable boundary |
| PBI-005 | The target report or semantic model is stored in a workspace assigned to a Copilot-enabled supported capacity | Prerequisites | MS-FAB-02, MS-FAB-03 | Direct | 🔴 | Pending | Copilot-enabled items must be associated with a supported workspace and capacity |
| PBI-006 | Intended users have access to the workspace and item required for the Copilot experience | Prerequisites | MS-FAB-02 | Direct | 🔴 | Pending | Existing Power BI permissions continue to control accessible data and items |
| PBI-007 | Power BI Desktop users have Admin, Member, or Contributor access to at least one Copilot-compatible workspace | Prerequisites | MS-FAB-03 | Direct | 🟡 | Pending | Applies only when Copilot is used in Power BI Desktop |
| PBI-008 | The capacity is not a trial capacity or trial SKU | Prerequisites | MS-FAB-03 | Direct | 🔴 | Pending | Only paid supported capacities qualify |
| PBI-009 | The deployment does not rely on an unsupported sovereign cloud environment | Prerequisites | MS-FAB-03 | Direct | 🔴 | Pending | Current Microsoft documentation states that sovereign clouds are not supported |

## Modeling and Schema

| ID | Requirement | Category | Source_ID | Evidence Level | Priority | Status | Notes |
|---|---|---|---|---|---|---|---|
| PBI-010 | Design semantic models using a star schema | Modeling and Schema | MS-MODEL-01 | Recommended | 🟡 | Pending | Assess the overall model structure and document material deviations |
| PBI-011 | Separate fact and dimension tables | Modeling and Schema | MS-MODEL-01 | Recommended | 🟡 | Pending | Classify relevant tables as fact, dimension, bridge, or technical |
| PBI-012 | Do not mix fact and dimension data within the same table | Modeling and Schema | MS-MODEL-01 | Recommended | 🟡 | Pending | Document exceptions where mixed responsibilities cannot yet be refactored |
| PBI-013 | Maintain a consistent grain within each fact table | Modeling and Schema | MS-MODEL-01 | Recommended | 🟡 | Pending | Record the expected grain of each assessed fact table |
| PBI-014 | Configure one-to-many relationships from dimension tables to fact tables | Modeling and Schema | MS-MODEL-01 | Recommended | 🟡 | Pending | Relationship changes require explicit human approval under the relationship invariant in `rules.yaml` |

## Relationships

| ID | Requirement | Category | Source_ID | Evidence Level | Priority | Status | Notes |
|---|---|---|---|---|---|---|---|
| PBI-015 | Define active relationships whenever possible | Relationships | MS-MODEL-03 | Recommended | 🟡 | Pending | Review and justify each inactive relationship |
| PBI-016 | Duplicate role-playing dimension tables instead of relying on inactive relationships when multiple active filter paths are required | Relationships | MS-MODEL-03 | Recommended | 🟡 | Pending | Assess dimensions that serve multiple semantic roles |
| PBI-017 | Use inactive relationships only for specific calculation scenarios together with `USERELATIONSHIP()` | Relationships | MS-MODEL-03 | Recommended | 🟡 | Pending | Confirm that each inactive relationship has a documented calculation use |
| PBI-018 | Minimize the use of bi-directional relationships | Relationships | MS-MODEL-04 | Recommended | 🟡 | Pending | Document the reason for each bi-directional relationship |
| PBI-019 | Use bi-directional filtering only when required for supported modeling scenarios | Relationships | MS-MODEL-04 | Recommended | 🟡 | Pending | Flag ambiguous or unsupported filter paths |
| PBI-020 | Prefer `CROSSFILTER()` in DAX over permanent bi-directional relationships for slicer filtering scenarios | Relationships | MS-MODEL-04 | Recommended | 🟡 | Pending | Review whether filter-direction changes can be limited to individual calculations |
| PBI-021 | Do not rely on inactive relationships for Row-Level Security propagation | Relationships | MS-MODEL-03 | Direct | 🔴 | Pending | Validate RLS filter paths independently of inactive relationships |

## Naming

| ID | Requirement | Category | Source_ID | Evidence Level | Priority | Status | Notes |
|---|---|---|---|---|---|---|---|
| PBI-022 | Use human-readable names for tables, columns, and measures | Naming | MS-NAME-01 | Recommended | 🟡 | Met | TASK-002 applied approved naming scope; one approved rename (_Measures -> Measures) was skipped due reserved engine name restriction and documented in run notes |
| PBI-023 | Use consistent naming conventions throughout the semantic model | Naming | MS-NAME-01 | Recommended | 🟡 | Met | TASK-002 applied approved naming scope and verified post-apply consistency for changed objects |
| PBI-024 | Avoid excessive acronyms, abbreviations, and punctuation in object names | Naming | MS-NAME-01 | Recommended | 🟡 | Met | TASK-002 removed approved technical punctuation-style naming in scope and verified the resulting renamed field |
| PBI-025 | Use business-friendly names that reflect how users naturally refer to the data | Naming | MS-NAME-02 | Recommended | 🟡 | Met | TASK-002 applied approved business-facing rename in scope and verified dependent references resolved |
| PBI-026 | Provide descriptions to distinguish similarly named fields when renaming is insufficient | Naming | MS-NAME-01 | Recommended | 🟡 | Met | TASK-002 added the approved disambiguating descriptions to key identity fields |
| PBI-027 | Add descriptions and synonyms when technical object names cannot be changed | Naming | MS-NAME-02 | Recommended | 🟡 | Pending | Synonyms may require manual application when the MCP does not support writes |
| PBI-028 | Name measures in English to improve Copilot understanding | Naming | MS-NAME-01 | Recommended | 🟡 | Pending | Rename only when an approved English business term is available |

## Measures

| ID | Requirement | Category | Source_ID | Evidence Level | Priority | Status | Notes |
|---|---|---|---|---|---|---|---|
| PBI-029 | Review Copilot-generated measure descriptions before publishing the semantic model | Measures | MS-MEASURE-01 | Recommended | 🟡 | Pending | Human review must confirm meaning, calculation interpretation, units, and usage |
| PBI-030 | Every visible measure has an accurate, concise, and helpful description | Measures | MS-MEASURE-01 | Recommended | 🟡 | Met | TASK-002 added descriptions to all approved missing visible measures and verified post-apply state |

## Metadata and Descriptions

| ID | Requirement | Category | Source_ID | Evidence Level | Priority | Status | Notes |
|---|---|---|---|---|---|---|---|
| PBI-031 | Add accurate, concise, and helpful descriptions to visible tables and business-relevant columns | Metadata and Descriptions | MS-META-01 | Recommended | 🟡 | Met | TASK-002 added approved descriptions for 24 in-scope visible business columns |
| PBI-032 | Configure data types, format strings, and data categories accurately for fields exposed to Copilot | Metadata and Descriptions | MS-META-01 | Derived | 🟡 | Met | TASK-002 set approved Country/City data categories for all four in-scope geographic fields |

## Discoverability

| ID | Requirement | Category | Source_ID | Evidence Level | Priority | Status | Notes |
|---|---|---|---|---|---|---|---|
| PBI-033 | Add synonyms for important business tables and fields used in natural-language queries | Discoverability | MS-DISC-01 | Recommended | 🟡 | Pending | Maintain proposed synonyms in the manual lane when write support is unavailable |

## Hidden and Technical Fields

| ID | Requirement | Category | Source_ID | Evidence Level | Priority | Status | Notes |
|---|---|---|---|---|---|---|---|
| PBI-034 | Hide technical columns and measures that are not intended for report consumers or Copilot interactions | Hidden and Technical Fields | MS-HIDDEN-01 | Recommended | 🟡 | Met | TASK-002 applied the single approved hide action (Session Count) and verified no additional hides were introduced |

## Security

| ID | Requirement | Category | Source_ID | Evidence Level | Priority | Status | Notes |
|---|---|---|---|---|---|---|---|
| PBI-035 | Implement and validate Row-Level Security when the semantic model contains data that requires restricted access | Security | MS-SEC-01 | Direct | 🔴 | Pending | Record representative user-context testing or document why RLS is not applicable |

## AI Preparation

| ID | Requirement | Category | Source_ID | Evidence Level | Priority | Status | Notes |
|---|---|---|---|---|---|---|---|
| PBI-036 | Power BI Q&A is enabled before configuring AI data schemas or verified answers | AI Preparation | MS-PREP-02, MS-PREP-03 | Direct | 🔴 | Pending | Required by Prep Data for AI features that depend on Q&A |
| PBI-037 | An AI data schema is defined and limited to fields relevant to Copilot questions | AI Preparation | MS-PREP-02 | Direct | 🔴 | Pending | A focused schema reduces ambiguity; model relationships continue to be respected |
| PBI-038 | Hidden, technical, confusing, and irrelevant fields are excluded from the AI data schema | AI Preparation | MS-PREP-02 | Recommended | 🟡 | Pending | Prioritize clean fields with limited ambiguity |
| PBI-039 | Verified answers are created for common, important, or nuanced business questions | AI Preparation | MS-PREP-03 | Recommended | 🟡 | Pending | Verified answers are stored in the semantic model |
| PBI-040 | Each verified answer uses representative trigger phrases within supported limits | AI Preparation | MS-PREP-03 | Recommended | 🟢 | Pending | Microsoft recommends five to seven phrases; the supported maximum is 15 phrases and 500 combined characters |
| PBI-041 | Verified answers use supported visuals and supported semantic-model connection modes | AI Preparation | MS-PREP-03 | Direct | 🟡 | Pending | Validate visual type, model type, filters, and report context |
| PBI-042 | Verified-answer trigger behavior is tested without unrelated Copilot authoring skills interfering | AI Preparation | MS-PREP-03 | Recommended | 🟡 | Pending | Use the skill selector during Desktop testing where applicable |
| PBI-043 | AI instructions define relevant business context, terminology, and interpretation rules | AI Preparation | MS-PREP-04 | Direct | 🔴 | Pending | Instructions are model-level configuration and support up to 10,000 characters |
| PBI-044 | AI instructions map alternative business terms to model concepts where needed | AI Preparation | MS-PREP-04, MS-PREP-05 | Recommended | 🟡 | Pending | Define terminology that Copilot cannot reliably infer from model metadata |
| PBI-045 | AI instructions contain only guidance that is valid across the semantic model | AI Preparation | MS-PREP-04 | Derived | 🟡 | Pending | Consumers cannot inspect or disable the instructions; avoid report-specific or temporary guidance |
| PBI-046 | AI preparation follows a deliberate sequence: AI data schema, verified answers, and then AI instructions | AI Preparation | MS-PREP-05 | Recommended | 🟡 | Pending | Use instructions for final refinement after reducing schema ambiguity and configuring curated answers |
| PBI-047 | The semantic model is marked as Approved for Copilot | AI Preparation | MS-COP-04 | Direct | 🔴 | Pending | Mark the semantic model as Approved for Copilot after completing AI preparation and review |
| PBI-048 | Copilot indexing is reviewed and configured for the semantic model | AI Preparation | MS-PREP-06 | Direct | 🟡 | Pending | Indexes model metadata and column values to improve speed and accuracy |
| PBI-049 | Local Desktop Indexing is reviewed for DirectQuery and live connection scenarios | AI Preparation | MS-PREP-06 | Direct | 🟡 | Pending | Configured per machine in Power BI Desktop; mark `N/A` for Import models |

## Testing and Validation

| ID | Requirement | Category | Source_ID | Evidence Level | Priority | Status | Notes |
|---|---|---|---|---|---|---|---|
| PBI-050 | The AI data schema is tested with included and excluded fields | Testing and Validation | MS-PREP-02 | Direct | 🔴 | Pending | Copilot should answer using included fields and avoid answering from fields outside the configured schema |
| PBI-051 | Verified answers are tested with representative trigger phrases and filter combinations | Testing and Validation | MS-PREP-03 | Direct | 🔴 | Pending | Validate that the expected approved visual is returned |
| PBI-052 | AI instructions are tested against representative business-language questions | Testing and Validation | MS-PREP-04 | Direct | 🔴 | Pending | Confirm that terminology and interpretation rules affect responses as intended |
| PBI-053 | The Copilot pane is refreshed after changes to AI data schemas or AI instructions | Testing and Validation | MS-PREP-02, MS-PREP-04 | Direct | 🟡 | Pending | Close and reopen the pane before evaluating updated behavior in Power BI Desktop |
| PBI-054 | Prep Data for AI changes are retested after publication to the Power BI service | Testing and Validation | MS-PREP-01, MS-PREP-02 | Recommended | 🟡 | Pending | Allow configuration changes to propagate before repeating representative tests |
| PBI-055 | Model integrity is verified after renames or structural changes | Testing and Validation | MS-MODEL-03 | Derived | 🔴 | Met | TASK-002 re-verified all modified objects plus relationships and security invariants before commit |
| PBI-056 | Visible table, column, and measure names, and their descriptions, are free of spelling errors | Quality and Consistency | None (Project) | Project | 🟡 | Pending | Added after TASK-001 found a spelling error in a model's own internal naming ("Analitics"); see `DECISIONS.md` D-008 |

## Requirement Summary

| Category | Total | Met | Pending | Blocked |
|---|---:|---:|---:|---:|
| Prerequisites | 9 | 0 | 9 | 0 |
| Modeling and Schema | 5 | 0 | 5 | 0 |
| Relationships | 7 | 0 | 7 | 0 |
| Naming | 7 | 5 | 2 | 0 |
| Measures | 2 | 1 | 1 | 0 |
| Metadata and Descriptions | 2 | 2 | 0 | 0 |
| Discoverability | 1 | 0 | 1 | 0 |
| Hidden and Technical Fields | 1 | 1 | 0 | 0 |
| Security | 1 | 0 | 1 | 0 |
| AI Preparation | 14 | 0 | 14 | 0 |
| Testing and Validation | 6 | 1 | 5 | 0 |
| Quality and Consistency | 1 | 0 | 1 | 0 |
| **Total** | **56** | **10** | **46** | **0** |

## Evidence Rollup

Evidence verification is derived from the current Source Registry in [`references.md`](references.md#source-registry).

A requirement is counted as verified only when every supporting `Source_ID` has status `Verified`.
`Project`-level requirements have no `Source_ID` by definition (ADR-0001) — their record of
origin is a `DECISIONS.md` entry instead, and they are counted as verified on that basis.

| Evidence Level | Total | Verified | Pending Verification |
|---|---:|---:|---:|
| Direct | 22 | 22 | 0 |
| Derived | 3 | 3 | 0 |
| Recommended | 30 | 30 | 0 |
| Project | 1 | 1 | 0 |
| **Total classified requirements** | **56** | **56** | **0** |

### Verification Boundary

As of 2026-07-24, every requirement's supporting `Source_ID`(s) are recorded as `Verified`
in [`references.md`](references.md#source-registry). The 20 requirements previously pending
(`PBI-015`–`PBI-021`, `PBI-022`–`PBI-033`, `PBI-055`) are now backed by real Microsoft Learn
URLs (`MS-MODEL-03`, `MS-MODEL-04`, `MS-NAME-01`, `MS-NAME-02`, `MS-MEASURE-01`, `MS-META-01`,
`MS-DISC-01`).

This resolves **evidence verification** only, not **implementation status** — see the
per-requirement `Status` column above, which remains `Pending` until an actual model is
assessed. Two related sources (`MS-MODEL-11` Q&A synonyms, `MS-MODEL-12` Perspectives) were
also reviewed but are not currently mapped to any `PBI-*` requirement and carry open
applicability questions — see `review_notes.md`.

This rollup describes **evidence verification**, not implementation status. A requirement can have verified evidence while its assessment status remains `Pending`.

## Executable Rule Coverage

[`rules.yaml`](../../rules.yaml) is the executable companion to this matrix.

- Environment, capacity, security, AI preparation, and service-level requirements can be assessment-only or manual.
- Metadata requirements can be automated only when the required business context is available.
- Relationship requirements are protected by the relationship invariant and are not automatically modified.
- Requirements without supported write operations must produce manual-lane deliverables rather than untracked changes.
- Any rule that cannot map to one of the `PBI-*` identifiers in this matrix must be treated as implementation guidance or proposed as a new project requirement.

## MVP Scope Guidance

For an initial readiness assessment:

- Include all 🔴 requirements.
- Include requirements classified as `Direct`.
- Review `Derived` requirements individually.
- Include 🟡 requirements when they affect answer quality, security, or model reliability.
- Defer 🟢 requirements when they do not block the pilot.
- Exclude `Project` requirements from Microsoft compliance claims.
- Record deferred requirements as `N/A` only when they are genuinely not applicable.
- Keep applicable but postponed requirements as `Pending`.

## Maintenance Checklist

When this matrix changes:

1. Confirm that requirement IDs remain unique and contiguous where intended.
2. Update the Source Registry and verified findings in [`references.md`](references.md).
3. Update executable mappings in [`rules.yaml`](../../rules.yaml).
4. Record evidence ambiguities in [`review_notes.md`](review_notes.md).
5. Review relevant architecture decisions under [`../adr/`](../adr/).
6. Search the entire repository for obsolete `PBI-*` and `Source_ID` references.
7. Recalculate the Requirement Summary and Evidence Rollup.
8. Record the change below.

## Change Log

| Date | Change | By |
|---|---|---|
| 2026-07-12 | Initial matrix seeded from Microsoft sources | Rostyslav Lisovyi |
| 2026-07-17 | Added evidence classification and MVP scope guidance | Rostyslav Lisovyi |
| 2026-07-19 | Aligned requirement numbering, source verification, executable-rule mappings, cross-document links, summaries, and evidence rollup | Rostyslav Lisovyi |
| 2026-07-23 | Fixed `.github/copilot-instructions.md` and `DECISIONS.md` to use current PBI-001..055 ids instead of rejected historical ids (PBI-060/065/070/072/074/080-082); removed an incorrect claim that relationships are MCP-automatable (they are a protected invariant); created missing `docs/microsoft/review_notes.md`; fixed `PROJECT.md` file-name reference | Claude (repository engineer skill) |
| 2026-07-24 | Verified 14 previously-`Planned` sources against Microsoft Learn (real URLs added); 12 moved to `Verified`, 2 (`MS-MODEL-11`, `MS-MODEL-12`) moved to `Reviewed` with open applicability questions logged in `review_notes.md`; Evidence Rollup now shows 55/55 requirements with verified evidence; corroborated the existence of the official Power BI Modeling MCP server (github.com/microsoft/powerbi-modeling-mcp) referenced by `.github/copilot-instructions.md` | Claude (repository engineer skill) |
| 2026-07-24 | Reverted TASK-001's baseline+audit merge for `user-usage-analytics` (PR #4) to re-run it with two audit-quality fixes applied first. Added `PBI-056` (spelling check on visible names/descriptions), the first `Project`-evidence-level requirement — see `DECISIONS.md` D-008. Updated `rules.yaml` PBI-027/033 to require reading the current `Synonyms` state via MCP before drafting proposals, rather than assuming a blank slate. Requirement Summary and Evidence Rollup now cover 56 requirements | Claude (repository engineer skill) |
| 2026-07-24 | Applied TASK-002 approved automatable scope for `user-usage-analytics` and updated implementation statuses to `Met` for PBI-022, 023, 024, 025, 026, 030, 031, 032, 034, and 055; recalculated Requirement Summary totals | GitHub Copilot (GPT-5.3-Codex) + Power BI Modeling MCP |
