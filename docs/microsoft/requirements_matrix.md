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
| PBI-001 | Copilot access is enabled through the `Users can use Copilot and other features powered by Azure OpenAI` setting | Prerequisites | MS-FAB-02 | Direct | 🔴 | Pending | Verify the effective tenant or delegated capacity configuration for the target experience |
| PBI-002 | The workspace uses a paid Fabric capacity of F2 or higher or a Power BI Premium capacity of P1 or higher | Prerequisites | MS-FAB-03 | Direct | 🔴 | Pending | Trial capacities, trial SKUs, Pro-only workspaces, and PPU-only workspaces do not directly satisfy the standard capacity requirement |
| PBI-003 | The capacity is located in a region supported for Copilot | Prerequisites | MS-FAB-03 | Direct | 🔴 | Pending | Validate against the current Microsoft Fabric region availability documentation |
| PBI-004 | Cross-region Azure OpenAI processing is enabled when the capacity region requires it | Prerequisites | MS-FAB-02 | Direct | 🔴 | Pending | Conditional requirement; do not mark as required when Azure OpenAI processing is available within the applicable boundary |
| PBI-005 | The target report or semantic model is stored in a workspace assigned to a Copilot-enabled supported capacity | Prerequisites | MS-FAB-02, MS-FAB-03 | Direct | 🔴 | Pending | Copilot-enabled items must be associated with a supported workspace and capacity |
| PBI-006 | Intended users have access to the workspace and item required for the Copilot experience | Prerequisites | MS-FAB-02 | Direct | 🔴 | Pending | Existing Power BI permissions continue to control accessible data and items |
| PBI-007 | Power BI Desktop users have Admin, Member, or Contributor access to at least one Copilot-compatible workspace | Prerequisites | MS-FAB-03 | Direct | 🟡 | Pending | Applies only when Copilot is used in Power BI Desktop |
| PBI-008 | The capacity is not a trial capacity or trial SKU | Prerequisites | MS-FAB-03 | Direct | 🔴 | Pending | Only paid supported capacities qualify |
| PBI-009 | The deployment does not rely on an unsupported sovereign cloud environment | Prerequisites | MS-FAB-03 | Direct | 🔴 | Pending | Current Microsoft documentation states that sovereign clouds are not supported |

## Modeling and Schema

| ID | Requirement | Evidence | Source |
|----|-------------|----------|--------|
| PBI-010 | Design semantic models using a star schema. | Recommended | MS-MODEL-01 |
| PBI-011 | Separate fact and dimension tables. | Recommended | MS-MODEL-01 |
| PBI-012 | Do not mix fact and dimension data within the same table. | Recommended | MS-MODEL-01 |
| PBI-013 | Maintain a consistent grain within each fact table. | Recommended | MS-MODEL-01 |
| PBI-014 | Configure one-to-many relationships from dimension tables to fact tables. | Recommended | MS-MODEL-01 |

## Relationships

| PBI-015 | Define active relationships whenever possible. | Recommended | MS-MODEL-03 |
| PBI-016 | Duplicate role-playing dimension tables instead of relying on inactive relationships when multiple active filter paths are required. | Recommended | MS-MODEL-03 |
| PBI-017 | Use inactive relationships only for specific calculation scenarios together with USERELATIONSHIP(). | Recommended | MS-MODEL-03 |
| PBI-018 | Minimize the use of bi-directional relationships. | Recommended | MS-MODEL-04 |
| PBI-019 | Use bi-directional filtering only when required for supported modeling scenarios. | Recommended | MS-MODEL-04 |
| PBI-020 | Prefer CROSSFILTER() in DAX over permanent bi-directional relationships for slicer filtering scenarios. | Recommended | MS-MODEL-04 |
| PBI-021 | Do not rely on inactive relationships for Row-Level Security propagation. | Direct | MS-MODEL-03 |

## Naming

| PBI-022 | Use human-readable names for tables, columns, and measures. | Recommended | MS-NAME-01 |
| PBI-023 | Use consistent naming conventions throughout the semantic model. | Recommended | MS-NAME-01 |
| PBI-024 | Avoid excessive acronyms, abbreviations, and punctuation in object names. | Recommended | MS-NAME-01 |
| PBI-025 | Use business-friendly names that reflect how users naturally refer to the data. | Recommended | MS-NAME-02 |
| PBI-026 | Provide descriptions to distinguish similarly named fields when renaming is insufficient. | Recommended | MS-NAME-01 |
| PBI-027 | Add descriptions and synonyms when technical object names cannot be changed. | Recommended | MS-NAME-02 |
| PBI-028 | Name measures in English to improve Copilot understanding. | Recommended | MS-NAME-01 |

## Measures

| PBI-030 | Review Copilot-generated measure descriptions before publishing the semantic model. | Recommended | MS-MEASURE-01 |
| PBI-031 | Every visible measure has an accurate, concise, and helpful description. | Recommended | MS-MEASURE-01 |

## Metadata and Descriptions

| ID | Requirement | Evidence | Source |
|---|---|---|---|
| PBI-040 | Add accurate, concise, and helpful descriptions to visible tables and business-relevant columns. | Recommended | MS-META-01 |
| PBI-041 | Configure data types, format strings, and data categories accurately for fields exposed to Copilot. | Derived | MS-META-01 |

## Discoverability

| ID | Requirement | Category | Source_ID |
|----|-------------|----------|-----------|
| PBI-050 | Add synonyms for important business tables and fields used in natural-language queries. | Discoverability | MS-DISC-01 |

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
| PBI-069 | Power BI Q&A is enabled before configuring AI data schema or verified answers | AI Preparation | MS-PREP-02, MS-PREP-03 | Direct | 🔴 | Pending | Required by the Prep Data for AI features that depend on Q&A |
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

| Category | Total | Met | Pending | Blocked |
|---|---:|---:|---:|---:|
| Prerequisites | 9 | 0 | 9 | 0 |
| Modeling and Schema | 10 | 0 | 10 | 0 |
| Naming | 4 | 0 | 4 | 0 |
| Measures | 3 | 0 | 3 | 0 |
| Metadata and Descriptions | 6 | 0 | 6 | 0 |
| Discoverability | 2 | 0 | 2 | 0 |
| Hidden and Technical Fields | 3 | 0 | 3 | 0 |
| Security | 1 | 0 | 1 | 0 |
| AI Preparation | 14 | 0 | 14 | 0 |
| Testing and Validation | 6 | 0 | 6 | 0 |
| **Total** | **58** | **0** | **58** | **0** |

## Evidence Rollup

Update this table after the source-review process.

| Evidence Level | Total | Verified | Pending Verification |
|---|---:|---:|---:|
| Direct | 30 | 0 | 30 |
| Derived | 6 | 0 | 6 |
| Recommended | 21 | 0 | 21 |
| Project | 1 | 0 | 1 |
| **Total classified requirements** | **58** | **0** | **58** |

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
