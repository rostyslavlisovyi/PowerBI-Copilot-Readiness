# Microsoft References

> Official Microsoft documentation used to derive and validate Power BI Copilot Readiness requirements.

## Purpose

This file is the source registry for the project.

Every `Source_ID` used in `requirements_matrix.md` must reference an entry in this document.

Source identifiers must remain stable even when Microsoft changes a document title or URL.

## Source Status

| Status | Meaning |
|---|---|
| `Planned` | Source has been identified but not reviewed |
| `Reviewed` | Source has been reviewed, but mapped requirements are not fully verified |
| `Verified` | Relevant requirements have been traced to the source |
| `Deprecated` | Source is outdated or replaced and should not be used for new requirements |

## Evidence Classification

| Evidence Level | Meaning |
|---|---|
| `Direct` | Microsoft explicitly states the requirement or prerequisite |
| `Derived` | The requirement is inferred from one or more Microsoft sources |
| `Recommended` | Microsoft presents the item as guidance or a best practice rather than a mandatory Copilot requirement |
| `Project` | The requirement is defined by this project based on implementation experience |

## Evidence Usage Rules

- `Direct` requirements should normally be treated as mandatory unless the source explicitly limits their scope.
- `Derived` requirements must include an explanation in the `Notes` column.
- `Recommended` requirements can be deferred from an MVP assessment when they do not affect security, reliability, or core answer quality.
- `Project` requirements must not be presented as official Microsoft requirements.
- Every requirement except a purely project-specific requirement must have at least one valid `Source_ID`.
- A requirement can have only one primary `Evidence Level`.
- Multiple `Source_ID` values can be used when a requirement depends on more than one source.
- Additional findings and ambiguities must be documented in `review_notes.md`.

## Source Registry

| Source_ID | Document | Area | URL | Version | Last Reviewed | Status | Notes |
|---|---|---|---|---|---|---|---|
| MS-COP-01 | Copilot in Power BI tutorial: Prepare semantic model for AI (Guidance section) | Copilot | <https://learn.microsoft.com/power-bi/create-reports/tutorial-copilot-power-bi-prepare-model#guidance> | Current online documentation | 2026-07-24 | Verified | Naming and field disambiguation guidance (distinguishing "Name" in Customer vs. Store) |
| MS-COP-02 | Copilot in Power BI tutorial: Prepare semantic model for AI (Guidance section) | Copilot | <https://learn.microsoft.com/power-bi/create-reports/tutorial-copilot-power-bi-prepare-model#guidance> | Current online documentation | 2026-07-24 | Verified | Model organization, naming, and hidden objects (same source article as MS-COP-01, different section emphasis) |
| MS-COP-03 | Optimize your semantic model for Copilot in Power BI | Copilot | <https://learn.microsoft.com/power-bi/create-reports/copilot-evaluate-data> | Current online documentation | 2026-07-24 | Verified | Primary Copilot semantic-model guidance: model structure, measures/KPIs, naming, data quality, refresh/security/metadata |
| MS-COP-04 | Prepare your data for AI to improve Copilot results (preview) | Copilot | <https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai> | Current online documentation | 2026-07-19 | Verified | AI preparation workflow, Approved for Copilot, testing guidance, and upgrade considerations |
| MS-PREP-01 | Prepare your data for AI | Prep Data for AI | <https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai> | Current online documentation | 2026-07-17 | Verified | Overview of AI preparation authoring in Power BI Desktop and the Power BI service |
| MS-PREP-02 | Prepare your data for AI: AI data schemas | Prep Data for AI | <https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai-data-schema> | Current online documentation | 2026-07-17 | Verified | AI schema scope, Q&A prerequisite, testing, refresh behavior, and limitations |
| MS-PREP-03 | Prepare your data for AI: Verified answers | Prep Data for AI | <https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai-verified-answers> | Current online documentation | 2026-07-17 | Verified | Verified answers, trigger phrases, supported limits, model storage, and testing |
| MS-PREP-04 | Prepare your data for AI: AI instructions | Prep Data for AI | <https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai-instructions> | Current online documentation | 2026-07-17 | Verified | Business context, terminology, response guidance, testing, and character limit |
| MS-PREP-05 | Prepare your data for AI FAQ | Prep Data for AI | <https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai-faq> | Current online documentation | 2026-07-17 | Verified | Feature applicability, preparation sequence, descriptions, and model-level behavior |
| MS-PREP-06 | Prepare your data for AI: Settings | Prep Data for AI | <https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai-settings> | Current online documentation | 2026-07-17 | Verified | Copilot indexing and Local Desktop Indexing settings |
| MS-MODEL-01 | Understand star schema and its relevance to Power BI | Modeling | <https://learn.microsoft.com/power-bi/guidance/star-schema> | Current online documentation | 2026-07-19 | Verified | Star-schema design guidance for semantic models |
| MS-MODEL-02 | Use Copilot with semantic models | Modeling | <https://learn.microsoft.com/power-bi/create-reports/copilot-semantic-models> | Current online documentation | 2026-07-19 | Verified | Connects semantic-model best practices with improved Copilot response quality |
| MS-MODEL-03 | Model relationships in Power BI Desktop | Modeling | <https://learn.microsoft.com/power-bi/transform-model/desktop-relationships-understand> | Current online documentation | 2026-07-24 | Verified | Cardinality, cross filter direction, active vs. inactive relationships; RLS propagation is documented in the linked "Active vs inactive relationship guidance" and "Row-level security (RLS)" articles, not this page directly |
| MS-MODEL-04 | Bi-directional relationship guidance | Modeling | <https://learn.microsoft.com/power-bi/guidance/relationships-bidirectional-filtering> | Current online documentation | 2026-07-24 | Verified | Bi-directional filtering, CROSSFILTER() DAX function, and recommendation to minimize bi-directional relationships |
| MS-MODEL-09 | Create calculation groups | Modeling | <https://learn.microsoft.com/power-bi/transform-model/calculation-groups> | Current online documentation | 2026-07-24 | Verified | Calculation-group creation and behavior; description guidance for calculation items is in MS-COP-03, not this page |
| MS-MODEL-11 | Add synonyms to tables and columns (Q&A best practices) | Modeling | <https://learn.microsoft.com/power-bi/natural-language/q-and-a-best-practices#normalize-your-model> | Current online documentation | 2026-07-24 | Reviewed | CAUTION: classic Power BI Q&A is being retired in December 2026 in favor of Copilot (per Microsoft's own deprecation notice). Direct applicability to Copilot is NOT confirmed by this source; Copilot's own use of field synonyms as grounding data is documented separately in MS-MODEL-02 ("Use Copilot with semantic models"). See `review_notes.md`. |
| MS-MODEL-12 | Perspectives in tabular models | Modeling | <https://learn.microsoft.com/analysis-services/tabular-models/perspectives-ssas-tabular> | Current online documentation | 2026-07-24 | Reviewed | Perspectives are a Fabric/Power BI Premium capacity + Analysis Services feature; no Microsoft source found stating perspectives affect Copilot grounding or DAX generation. Direct applicability to Copilot remains unconfirmed. See `review_notes.md`. |
| MS-MODEL-13 | Specify data categories in Power BI Desktop | Modeling | <https://learn.microsoft.com/power-bi/transform-model/desktop-data-categorization> | Current online documentation | 2026-07-24 | Verified | Data-category metadata (e.g. geography categories) and how Power BI uses it for visualizations |
| MS-NAME-01 | Optimize your semantic model for Copilot in Power BI / Use Copilot with semantic models / Semantic model best practices for data agent | Naming | <https://learn.microsoft.com/power-bi/create-reports/copilot-evaluate-data#considerations-for-semantic-models-for-copilot-use>; <https://learn.microsoft.com/power-bi/create-reports/copilot-semantic-models#develop-a-semantic-model-with-help-from-copilot>; <https://learn.microsoft.com/fabric/data-science/semantic-model-best-practices#common-pitfalls-to-avoid> | Current online documentation | 2026-07-24 | Verified | Human-readable names, naming consistency, avoiding acronyms/abbreviations/punctuation, English measure names. Spans 3 related Microsoft articles rather than one dedicated page |
| MS-NAME-02 | Best practices for configuring your data agent | Naming | <https://learn.microsoft.com/fabric/data-science/data-agent-configuration-best-practices#5-define-business-terms-abbreviations-and-synonyms> | Current online documentation | 2026-07-24 | Verified | Business vocabulary, abbreviations, and synonyms guidance ("Define business terms, abbreviations, and synonyms"). This article targets Fabric data agent rather than Copilot in Power BI specifically; content is directly transferable but framing differs |
| MS-MEASURE-01 | Optimize your semantic model for Copilot in Power BI (Measures and KPIs section) | Measures | <https://learn.microsoft.com/power-bi/create-reports/copilot-evaluate-data#considerations-for-semantic-models-for-copilot-use> | Current online documentation | 2026-07-24 | Verified | Standardized calculation logic, measure naming conventions, predefined measures/KPIs, and descriptions |
| MS-META-01 | Optimize your semantic model for Copilot in Power BI (Columns/data quality and Refresh/security/metadata sections) | Metadata | <https://learn.microsoft.com/power-bi/create-reports/copilot-evaluate-data#considerations-for-semantic-models-for-copilot-use> | Current online documentation | 2026-07-24 | Verified | Descriptions (200-char limit), format strings implied via data-type accuracy, data types, and metadata documentation; data-category specifics are in MS-MODEL-13 |
| MS-DISC-01 | Use Copilot with semantic models (grounding data / synonyms) | Discoverability | <https://learn.microsoft.com/power-bi/create-reports/copilot-semantic-models#develop-a-semantic-model-with-help-from-copilot> | Current online documentation | 2026-07-24 | Verified | Field synonyms are explicitly listed as Copilot grounding data; consistent naming/limited punctuation improves synonym usefulness. Prefer this over MS-MODEL-11 (Q&A synonyms), which documents a feature being retired |
| MS-FAB-02 | Enable and configure Copilot in Microsoft Fabric | Fabric Administration | <https://learn.microsoft.com/fabric/fundamentals/copilot-enable-fabric> | Current online documentation | 2026-07-17 | Verified | Tenant settings, delegated capacity configuration, workspace assignment, cross-region processing, and user access |
| MS-FAB-03 | Enable Fabric Copilot for Power BI | Fabric Administration | <https://learn.microsoft.com/power-bi/create-reports/copilot-enable-power-bi> | Current online documentation | 2026-07-17 | Verified | Capacity, licensing, region, workspace, Desktop access, and sovereign-cloud limitations |
| MS-HIDDEN-01 | Use Copilot with semantic models | Model Organization | <https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-semantic-models> | Current online documentation | 2026-07-19 | Verified | Microsoft recommends hiding columns and measures that are not intended for report consumers |
| MS-SEC-01 | Row-level security with Power BI | Security | <https://learn.microsoft.com/en-us/fabric/security/service-admin-row-level-security> | Current online documentation | 2026-07-19 | Verified | Implementation, management, and validation of RLS for semantic models containing restricted data |

## Verified Findings

### Prep Data for AI Overview

- Prep Data for AI features can be authored in Power BI Desktop and the Power BI service.
- Configuration changes are stored in the semantic model rather than in an individual report.
- The core preparation features include AI data schemas, verified answers, and AI instructions.
- Changes can require time or a Copilot pane refresh before affecting responses.

Mapped source: `MS-PREP-01`.

### AI Data Schemas

- Power BI Q&A must be enabled for the semantic model.
- An AI data schema defines a focused subset of model fields for Copilot.
- The reduced schema helps decrease ambiguity and improve response relevance.
- Model relationships continue to be respected.
- Hidden fields are initially excluded when the AI data schema is first configured.
- Consumers cannot disable or view the configured AI data schema.
- The Copilot pane must be closed and reopened after schema changes when testing.

Mapped source: `MS-PREP-02`.

### Verified Answers

- Verified answers associate approved visuals with predefined trigger phrases.
- Verified answers are stored in the semantic model.
- Microsoft recommends using five to seven trigger phrases for each verified answer.
- A verified answer supports up to 15 trigger phrases.
- Trigger phrases have a combined limit of 500 characters.
- A semantic model supports up to 250 verified answers.
- A verified answer supports up to 10 filter permutations.
- Not every visual type is supported.
- Verified answers should be tested with relevant Copilot authoring skills disabled when those skills could interfere with trigger testing.

Mapped source: `MS-PREP-03`.

### AI Instructions

- AI instructions provide model-level business context and terminology.
- Instructions can clarify business logic and map user terminology to model concepts.
- AI instructions are limited to 10,000 characters.
- Consumers cannot view or disable model instructions.
- The Copilot pane must be closed and reopened after instruction changes when testing in Power BI Desktop.
- Instructions are intended to refine Copilot behavior after the primary schema and verified-answer configuration has been prepared.

Mapped sources: `MS-PREP-04`, `MS-PREP-05`.

### Copilot Indexing

- Copilot indexing includes model metadata and column values.
- Its purpose is to help Copilot answer data questions faster and more accurately.
- Copilot indexing can be configured for the semantic model.
- Local Desktop Indexing is an additional Power BI Desktop setting.
- Local Desktop Indexing applies only to DirectQuery and live connection scenarios.
- Local Desktop Indexing is configured per machine.

Mapped source: `MS-PREP-06`.

### Approved for Copilot

- The semantic model can be marked as Approved for Copilot.
- Approval is part of the broader AI preparation workflow.
- Approval should be applied after the semantic model has been prepared and reviewed.
- Approval does not replace model testing or validation.

Mapped source: `MS-COP-04`.

### Copilot Tenant Configuration

- Copilot access is controlled through the `Users can use Copilot and other features powered by Azure OpenAI` setting.
- Copilot settings can be scoped to selected security groups.
- Delegated tenant settings can be configured at the capacity level.
- Workspaces containing Copilot-enabled items must be assigned to a supported capacity.
- Users must be granted access to the relevant workspace.
- Cross-region Azure OpenAI processing is conditional and depends on the applicable geographic and compliance boundary.

Mapped source: `MS-FAB-02`.

### Copilot Capacity and Region

- Standard Copilot use requires a paid Fabric capacity of F2 or higher or a Power BI Premium capacity of P1 or higher.
- Trial SKUs and trial capacities are not supported.
- The capacity must be located in a supported region.
- Power BI Desktop users require Admin, Member, or Contributor access to a compatible workspace.
- Power BI Desktop requires the tenant-level Copilot setting to be enabled.
- Sovereign cloud environments are not currently supported.

Mapped source: `MS-FAB-03`.

### Star Schema

- Microsoft recommends designing Power BI semantic models using a star schema.
- Semantic models should separate fact tables from dimension tables.
- Fact and dimension data should not be combined in the same table.
- Fact tables should maintain a consistent grain.
- Relationships should follow the star-schema pattern by relating dimension tables to fact tables through one-to-many relationships.

Evidence classification: `Recommended`.

Mapped source: `MS-MODEL-01`.

### Semantic Model Best Practices for Copilot

- Following semantic-model best practices can improve the quality of Copilot responses.
- Star-schema design is relevant not only to general model quality but also to Copilot answer quality.
- Semantic-model organization affects the fields and concepts available to Copilot.

Evidence classification: `Recommended`.

Mapped source: `MS-MODEL-02`.

### Hidden Objects

- Columns and measures that are not intended for report consumers should be hidden.
- Hiding technical and intermediate objects reduces the number of irrelevant fields exposed to consumers.
- Hidden objects can still participate in relationships and dependent calculations.

Evidence classification: `Recommended`.

Mapped source: `MS-HIDDEN-01`.

### Row-Level Security

- Row-level security can restrict access to rows for users or roles.
- Existing semantic-model permissions and security rules remain relevant when users interact with Power BI content.
- RLS should be implemented when the semantic model contains data requiring restricted access.
- RLS behavior should be validated using representative user contexts.

Evidence classification: `Direct`.

Mapped source: `MS-SEC-01`.

## Planned Source Work

As of 2026-07-24, all 14 sources previously listed here have been reviewed against Microsoft
Learn. 12 are now `Verified` (`MS-COP-01`, `MS-COP-02`, `MS-COP-03`, `MS-MODEL-03`,
`MS-MODEL-04`, `MS-MODEL-09`, `MS-MODEL-13`, `MS-NAME-01`, `MS-NAME-02`, `MS-MEASURE-01`,
`MS-META-01`, `MS-DISC-01`). 2 remain `Reviewed` pending an open applicability question logged
in `review_notes.md`:

- `MS-MODEL-11` (Q&A synonyms) — documents a feature being retired in December 2026; not used
  as a source for any current requirement.
- `MS-MODEL-12` (Perspectives) — no confirmed Copilot applicability found; not used as a source
  for any current requirement.

No sources currently remain in the `Planned` state.

## Review Process

For every source:

1. Add the official Microsoft Learn URL.
2. Record the date on which the source was reviewed.
3. Identify all requirements supported by the source.
4. Confirm whether each mapped requirement is `Direct`, `Derived`, or `Recommended`.
5. Add findings and ambiguities to `review_notes.md`.
6. Change the source status to `Verified` only after all mapped requirements have been checked.

## Maintenance Rules

- Review verified sources after significant Microsoft Fabric or Power BI Copilot announcements.
- Do not change an existing `Source_ID` when only the document title or URL changes.
- Mark replaced sources as `Deprecated`.
- Add a replacement as a new source when its meaning or scope differs materially.
- Do not delete deprecated sources while requirements or historical notes still reference them.
- Treat the `Last Reviewed` date as the project review date, not as the Microsoft page publication date.
- Keep the Source Registry as the authoritative list of source identifiers and statuses.
- Do not add a detailed findings section for a source unless the source has been reviewed.
- Do not mark a source as `Verified` when its URL is still `TBD`.