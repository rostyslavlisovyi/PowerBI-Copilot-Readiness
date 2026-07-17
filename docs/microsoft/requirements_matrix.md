# Requirements Matrix — Power BI Copilot Readiness

> The central artifact of the project. Every readiness requirement is traced to an official Microsoft source or explicitly identified as a project-specific rule.

## Legend

**Priority:** 🔴 Must-have · 🟡 Recommended · 🟢 Nice-to-have

**Status:** `Pending` · `In Progress` · `Met` · `N/A` · `Blocked`

**Evidence Level:** `Direct` · `Derived` · `Recommended` · `Project`

Columns: **ID · Requirement · Category · Source_ID · Evidence Level · Priority · Status · Notes**

> Evidence classifications in this initial version are provisional until each Microsoft source is reviewed and marked as `Verified` in `references.md`.

## Prerequisites

| ID | Requirement | Category | Source_ID | Evidence Level | Priority | Status | Notes |
|---|---|---|---|---|---|---|---|
| PBI-001 | Copilot is enabled at the tenant level by a Fabric administrator | Prerequisites | MS-FAB-02 | Direct | 🔴 | Pending | Required before Copilot features become available |
| PBI-002 | The semantic model is hosted in a supported Fabric capacity | Prerequisites | MS-FAB-03 | Direct | 🔴 | Pending | Verify supported SKU |
| PBI-003 | The Fabric capacity is located in a region where Copilot is supported | Prerequisites | MS-FAB-03 | Direct | 🔴 | Pending | Verify regional availability |
| PBI-004 | Cross-region Azure OpenAI processing is enabled when required | Prerequisites | MS-FAB-02 | Direct | 🔴 | Pending | Required for some tenant configurations |
| PBI-005 | Power BI Q&A is enabled before configuring Prep Data for AI features | Prerequisites | MS-PREP-02, MS-PREP-03 | Direct | 🔴 | Pending | Required for AI data schema and verified answers |
| PBI-006 | The user has permission to create or edit AI preparation artifacts | Prerequisites | MS-PREP-01 | Direct | 🟡 | Pending | Author permissions are required |
| PBI-007 | The semantic model is stored in a supported workspace | Prerequisites | MS-FAB-03 | Direct | 🔴 | Pending | Unsupported workspaces cannot use Copilot |
| PBI-008 | The semantic model is refreshable and accessible | Prerequisites | MS-COP-03 | Derived | 🟡 | Pending | Copilot depends on an accessible semantic model |

## Modeling and Schema

| ID | Requirement | Category | Source_ID | Evidence Level | Priority | Status | Notes |
|---|---|---|---|---|---|---|---|
| PBI-010 | Star schema design is used | Modeling | MS-MODEL-01 | Recommended | 🔴 | Pending | Foundation for reliable model behavior; confirm whether Copilot guidance states this directly |
| PBI-011 | Fact tables are clearly delineated | Modeling | MS-COP-03 | Recommended | 🔴 | Pending | |
| PBI-012 | Dimension tables hold descriptive attributes | Modeling | MS-COP-03 | Recommended | 🔴 | Pending | |
| PBI-013 | Relationships are defined with correct cardinality | Relationships | MS-COP-03 | Direct | 🔴 | Pending | `1:*`, `*:1`, and `*:*` relationships are explicit |
| PBI-014 | Active and inactive relationships are configured correctly | Relationships | MS-MODEL-03 | Recommended | 🟡 | Pending | Role-playing dimensions are inactive where required |
| PBI-015 | The model contains no ambiguous relationships or disconnected field-parameter traps | Modeling | MS-COP-04 | Derived | 🟡 | Pending | Explain the supporting Microsoft guidance during source review |
| PBI-016 | Unused model objects are removed | Modeling | MS-COP-04 | Recommended | 🟡 | Pending | Includes unused tables, fields, and measures |
| PBI-017 | Hierarchies are established for common drill-down paths | Modeling | MS-COP-03 | Recommended | 🟢 | Pending | Example: Year > Quarter > Month |
| PBI-018 | Column data types are correct and consistent | Modeling | MS-COP-03 | Recommended | 🟡 | Pending | |
| PBI-019 | Values within columns use standardized casing and terminology | Modeling | MS-COP-03 | Recommended | 🟢 | Pending | Example: Open, Closed, Pending |

## Naming

| ID | Requirement | Category | Source_ID | Evidence Level | Priority | Status | Notes |
|---|---|---|---|---|---|---|---|
| PBI-020 | Tables use human-readable business names without unnecessary technical suffixes | Naming | MS-COP-02 | Direct | 🔴 | Pending | Avoid names such as `Customer Table` |
| PBI-021 | Measure names reflect their calculation and business purpose | Naming | MS-COP-03 | Direct | 🔴 | Pending | Avoid cryptic abbreviations |
| PBI-022 | Column names are unambiguous and do not expose unnecessary raw IDs or codes | Naming | MS-COP-03 | Direct | 🔴 | Pending | |
| PBI-023 | Duplicate field names across tables are disambiguated | Naming | MS-COP-01 | Direct | 🔴 | Pending | Example: `Customer[Name]` versus `Store[Name]` |

## Measures

| ID | Requirement | Category | Source_ID | Evidence Level | Priority | Status | Notes |
|---|---|---|---|---|---|---|---|
| PBI-030 | Measures use standardized and explainable logic | Measures | MS-COP-03 | Recommended | 🟡 | Pending | |
| PBI-031 | Every visible measure has a description | Metadata | MS-COP-03 | Direct | 🔴 | Pending | Copilot quality depends on clear metadata |
| PBI-032 | Common business KPIs are predefined as measures | Measures | MS-COP-03 | Recommended | 🟡 | Pending | Examples: YTD and month-over-month |

## Metadata and Descriptions

| ID | Requirement | Category | Source_ID | Evidence Level | Priority | Status | Notes |
|---|---|---|---|---|---|---|---|
| PBI-040 | Tables have descriptions | Metadata | MS-COP-03 | Direct | 🔴 | Pending | |
| PBI-041 | Business-relevant columns have descriptions | Metadata | MS-COP-03 | Direct | 🟡 | Pending | Confirm whether Microsoft requires descriptions for every visible column |
| PBI-042 | Key information is placed within the first 200 characters of a description | Metadata | MS-COP-03 | Direct | 🔴 | Pending | Confirm the current documented processing limit |
| PBI-043 | Calculation groups are documented through the calculation-group column description | Metadata | MS-MODEL-09 | Derived | 🟡 | Pending | Calculation items might not be represented independently in metadata |
| PBI-044 | Model structure is documented in a data dictionary | Metadata | MS-COP-03 | Project | 🟢 | Pending | Project-level maintainability practice |
| PBI-045 | Data categories are set where relevant | Metadata | MS-MODEL-13 | Recommended | 🟢 | Pending | Examples: geography and URL fields |

## Discoverability

| ID | Requirement | Category | Source_ID | Evidence Level | Priority | Status | Notes |
|---|---|---|---|---|---|---|---|
| PBI-050 | Synonyms are added for key business objects | Discoverability | MS-MODEL-11 | Recommended | 🟡 | Pending | Confirm direct applicability to current Copilot experiences |
| PBI-051 | Perspectives are evaluated as a model-scoping mechanism | Discoverability | MS-MODEL-12 | Derived | 🟢 | Pending | Do not treat as mandatory until direct Copilot relevance is confirmed |

## Hidden and Technical Fields

| ID | Requirement | Category | Source_ID | Evidence Level | Priority | Status | Notes |
|---|---|---|---|---|---|---|---|
| PBI-060 | Technical relationship keys and raw IDs are hidden from report consumers and AI experiences | Model Organization | MS-COP-04 | Direct | 🔴 | Pending | |
| PBI-061 | Sort-order helper fields are excluded from the AI schema or hidden | Model Organization | MS-COP-04 | Recommended | 🟡 | Pending | Example: Month Sort Order |
| PBI-062 | Intermediate calculation measures are hidden | Model Organization | MS-COP-02 | Recommended | 🟡 | Pending | |

## Security

| ID | Requirement | Category | Source_ID | Evidence Level | Priority | Status | Notes |
|---|---|---|---|---|---|---|---|
| PBI-065 | Row-level security roles are defined where sensitive data requires them | Security | MS-COP-03 | Derived | 🔴 | Pending | Security requirement derived from data-access obligations; validate before rollout |

## AI Preparation

| ID | Requirement | Category | Source_ID | Evidence Level | Priority | Status | Notes |
|---|---|---|---|---|---|---|---|
| PBI-070 | An AI data schema is defined and limited to fields relevant to Copilot questions | AI Preparation | MS-PREP-02 | Direct | 🔴 | Pending | A focused schema reduces ambiguity; model relationships continue to be respected |
| PBI-070a | Hidden, technical, confusing, and irrelevant fields are excluded from the AI data schema | AI Preparation | MS-PREP-02 | Recommended | 🟡 | Pending | Prioritize clean columns with limited ambiguity |
| PBI-071 | Verified answers are created for common, important, or nuanced business questions | AI Preparation | MS-PREP-03 | Recommended | 🟡 | Pending | Verified answers are stored in the semantic model |
| PBI-071a | Each verified answer uses representative trigger phrases within supported limits | AI Preparation | MS-PREP-03 | Recommended | 🟢 | Pending | Microsoft recommends 5–7 phrases; supported maximum is 15 phrases and 500 combined characters |
| PBI-071b | Verified answers use supported visuals and supported semantic-model connection modes | AI Preparation | MS-PREP-03 | Direct | 🟡 | Pending | Validate visual type, model type, filters, and report context |
| PBI-071c | Verified-answer trigger behavior is tested without unrelated Copilot authoring skills interfering | AI Preparation | MS-PREP-03 | Recommended | 🟡 | Pending | Use the skill selector during Desktop testing where applicable |
| PBI-072 | AI instructions define relevant business context, terminology, and interpretation rules | AI Preparation | MS-PREP-04 | Direct | 🔴 | Pending | Instructions are model-level configuration and support up to 10,000 characters |
| PBI-072a | AI instructions map alternative business terms to model concepts where needed | AI Preparation | MS-PREP-04, MS-PREP-05 | Recommended | 🟡 | Pending | Define terminology that Copilot cannot reliably infer from model metadata |
| PBI-072b | AI instructions contain only guidance that is valid across the semantic model | AI Preparation | MS-PREP-04 | Derived | 🟡 | Pending | Consumers cannot inspect or disable the instructions |
| PBI-073 | AI preparation follows a deliberate sequence: AI data schema, verified answers, and then AI instructions | AI Preparation | MS-PREP-05 | Recommended | 🟡 | Pending | Use instructions for final refinement after reducing schema ambiguity and configuring curated answers |
| PBI-074 | The semantic model is marked as approved for Copilot | AI Preparation | MS-COP-04 | Direct | 🔴 | Pending | Verification remains pending until MS-COP-04 is reviewed |
| PBI-075 | Copilot indexing is reviewed and configured for the semantic model | AI Preparation | MS-PREP-06 | Direct | 🟡 | Pending | Indexes model metadata and column values to improve speed and accuracy |
| PBI-075a | Local Desktop Indexing is reviewed for DirectQuery and live connection scenarios | AI Preparation | MS-PREP-06 | Direct | 🟡 | Pending | Power BI Desktop setting configured per machine; not applicable to Import models |

## Testing and Validation

| ID | Requirement | Category | Source_ID | Evidence Level | Priority | Status | Notes |
|---|---|---|---|---|---|---|---|
| PBI-080 | The AI data schema is tested with included and excluded fields | Testing | MS-PREP-02 | Direct | 🔴 | Pending | Copilot should answer with included fields and avoid answering from fields outside the configured schema |
| PBI-081 | Verified answers are tested with representative trigger phrases and filter combinations | Testing | MS-PREP-03 | Direct | 🔴 | Pending | Validate that the expected approved visual is returned |
| PBI-082 | AI instructions are tested against representative business-language questions | Testing | MS-PREP-04 | Direct | 🔴 | Pending | Confirm that terminology and interpretation rules affect responses as intended |
| PBI-083 | The Copilot pane is refreshed after changes to AI data schemas or AI instructions | Testing | MS-PREP-02, MS-PREP-04 | Direct | 🟡 | Pending | Close and reopen the pane before evaluating updated behavior in Power BI Desktop |
| PBI-084 | Prep Data for AI changes are retested after publication to the Power BI service | Testing | MS-PREP-01, MS-PREP-02 | Recommended | 🟡 | Pending | Changes can take time before affecting Copilot results |
| PBI-085 | Model integrity is verified after renames or structural changes | Testing | MS-MODEL-03 | Derived | 🔴 | Pending | Check relationships, RLS, field parameters, and dependent objects; source verification remains pending |

## Rollup

Fill this table during the model review.

| Category | Total | Met | Pending | Blocked |
|---|---:|---:|---:|---:|
| Prerequisites | 5 | 0 | 5 | 0 |
| Modeling and Schema | 10 | 0 | 10 | 0 |
| Naming | 4 | 0 | 4 | 0 |
| Measures | 3 | 0 | 3 | 0 |
| Metadata and Descriptions | 6 | 0 | 6 | 0 |
| Discoverability | 2 | 0 | 2 | 0 |
| Hidden and Technical Fields | 3 | 0 | 3 | 0 |
| Security | 1 | 0 | 1 | 0 |
| AI Preparation | 13 | 0 | 13 | 0 |
| Testing and Validation | 6 | 0 | 6 | 0 |
| Prerequisites | 8 | 0 | 8 | 0 |
| **Total** | **56** | **0** | **56** | **0** |

## Evidence Rollup

Update this table after the source-review process.

| Evidence Level | Total | Verified | Pending Verification |
|---|---:|---:|---:|
| Direct | 20 | 0 | 20 |
| Derived | 7 | 0 | 7 |
| Recommended | 16 | 0 | 16 |
| Project | 1 | 0 | 1 |
| **Total classified requirements** | **44** | **0** | **44** |

> The evidence rollup counts `PBI-071a` and `PBI-072a` as independent requirements. Recalculate the totals whenever requirements or classifications change.

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

## Change Log

| Date | Change | By |
|---|---|---|
| 2026-07-12 | Initial matrix seeded from Microsoft sources | Rostyslav Lisovyi |
| 2026-07-17 | Added evidence classification and MVP scope guidance | Rostyslav Lisovyi |
