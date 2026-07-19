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
| MS-COP-01 | Semantic model naming guidance | Copilot | TBD | Current online documentation | TBD | Planned | Naming and field disambiguation guidance |
| MS-COP-02 | Organize semantic models for Copilot | Copilot | TBD | Current online documentation | TBD | Planned | Model organization, naming, and hidden objects |
| MS-COP-03 | Optimize semantic models for Copilot | Copilot | TBD | Current online documentation | TBD | Planned | Primary Copilot semantic-model guidance |
| MS-COP-04 | Prepare semantic models for AI and Copilot | Copilot | TBD | Current online documentation | TBD | Planned | Model cleanup, AI preparation, approval, and validation |
| MS-PREP-01 | Prepare your data for AI | Prep Data for AI | <https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai> | Current online documentation | 2026-07-17 | Verified | Overview of AI preparation authoring in Power BI Desktop and the Power BI service |
| MS-PREP-02 | Prepare your data for AI: AI data schemas | Prep Data for AI | <https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai-data-schema> | Current online documentation | 2026-07-17 | Verified | AI schema scope, Q&A prerequisite, testing, refresh behavior, and limitations |
| MS-PREP-03 | Prepare your data for AI: Verified answers | Prep Data for AI | <https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai-verified-answers> | Current online documentation | 2026-07-17 | Verified | Verified answers, trigger phrases, supported limits, model storage, and testing |
| MS-PREP-04 | Prepare your data for AI: AI instructions | Prep Data for AI | <https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai-instructions> | Current online documentation | 2026-07-17 | Verified | Business context, terminology, response guidance, testing, and character limit |
| MS-PREP-05 | Prepare your data for AI FAQ | Prep Data for AI | <https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai-faq> | Current online documentation | 2026-07-17 | Verified | Feature applicability, preparation sequence, descriptions, and model-level behavior |
| MS-PREP-06 | Prepare your data for AI: Settings | Prep Data for AI | <https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-prepare-data-ai-settings> | Current online documentation | 2026-07-17 | Verified | Copilot indexing and Local Desktop Indexing settings |
| MS-MODEL-01 | Understand star schema and its relevance to Power BI | Modeling | TBD | Current online documentation | TBD | Planned | Star-schema design guidance |
| MS-MODEL-03 | Model relationships in Power BI Desktop | Modeling | TBD | Current online documentation | TBD | Planned | Cardinality, active relationships, and model integrity |
| MS-MODEL-09 | Calculation groups | Modeling | TBD | Current online documentation | TBD | Planned | Calculation-group behavior and metadata |
| MS-MODEL-11 | Q&A synonyms | Modeling | TBD | Current online documentation | TBD | Planned | Verify direct applicability to Copilot |
| MS-MODEL-12 | Perspectives | Modeling | TBD | Current online documentation | TBD | Planned | Verify direct applicability to Copilot |
| MS-MODEL-13 | Data categories in Power BI Desktop | Modeling | TBD | Current online documentation | TBD | Planned | Data-category metadata |
| MS-FAB-02 | Copilot tenant settings | Fabric Administration | TBD | Current online documentation | TBD | Planned | Tenant settings and cross-region processing |
| MS-FAB-03 | Copilot regional availability and capacity requirements | Fabric Administration | TBD | Current online documentation | TBD | Planned | Capacity, SKU, and regional availability |
| MS-HIDDEN-01 | Use Copilot with semantic models | Model Organization | <https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-semantic-models> | Current online documentation | 2026-07-19 | Verified | Microsoft recommends hiding columns and measures as part of semantic model organization for Copilot |
| MS-SEC-01 | Row-level security (RLS) with Power BI | Security | <https://learn.microsoft.com/en-us/fabric/security/service-admin-row-level-security> | Current online documentation | 2026-07-19 | Verified | Microsoft documents implementing, managing, and validating RLS for semantic models containing restricted data. |

## Verified Findings: Prep Data for AI

### AI preparation overview

- Prep Data for AI features can be authored in Power BI Desktop and the Power BI service.
- Configuration changes are stored in the semantic model rather than an individual report.
- The core preparation features include AI data schemas, verified answers, and AI instructions.
- Changes can require time or a Copilot pane refresh before affecting responses.

Mapped source: `MS-PREP-01`.

### AI data schemas

- Power BI Q&A must be enabled for the semantic model.
- An AI data schema defines a focused subset of model fields for Copilot.
- The reduced schema helps decrease ambiguity and improve response relevance.
- Model relationships continue to be respected.
- Hidden fields are initially excluded when the AI data schema is first configured.
- Consumers cannot disable or view the configured AI data schema.
- The Copilot pane must be closed and reopened after schema changes when testing.

Mapped source: `MS-PREP-02`.

### Verified answers

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

### AI instructions

- AI instructions provide model-level business context and terminology.
- Instructions can clarify business logic and map user terminology to model concepts.
- AI instructions are limited to 10,000 characters.
- Consumers cannot view or disable model instructions.
- The Copilot pane must be closed and reopened after instruction changes when testing in Power BI Desktop.
- Instructions are intended to refine Copilot behavior after the primary schema and verified-answer configuration has been prepared.

Mapped sources: `MS-PREP-04`, `MS-PREP-05`.

### Copilot indexing

- Copilot indexing indexes model metadata and column values.
- Its purpose is to help Copilot answer data questions faster and more accurately.
- Copilot indexing is editable.
- Local Desktop Indexing is an additional Power BI Desktop setting.
- Local Desktop Indexing applies only to DirectQuery and live connection scenarios.
- Local Desktop Indexing is configured per machine.

Mapped source: `MS-PREP-06`.

## Review Process

For every source:

1. Add the official Microsoft Learn URL.
2. Record the date on which the source was reviewed.
3. Identify all requirements supported by the source.
4. Confirm whether each requirement is `Direct`, `Derived`, or `Recommended`.
5. Add findings and ambiguities to `review_notes.md`.
6. Change the source status to `Verified` only after all mapped requirements have been checked.

## Maintenance Rules

- Review verified sources after significant Microsoft Fabric or Power BI Copilot announcements.
- Do not change an existing `Source_ID` when only the title or URL changes.
- Mark replaced sources as `Deprecated`.
- Add a replacement as a new source when its meaning or scope differs materially.
- Do not delete deprecated sources while requirements or historical notes still reference them.
- Treat the `Last Reviewed` date as the project review date, not as the Microsoft page publication date.

## Verified Findings: Copilot Prerequisites

### Tenant configuration

- Copilot must be enabled by the Power BI or Fabric administrator.
- Tenant settings determine whether users can access Copilot features.
- Cross-region Azure OpenAI processing may be required depending on the tenant configuration.

Mapped source: `MS-FAB-02`.

### Capacity and region

- Copilot requires a supported Fabric capacity.
- Capacity must reside in a supported geographic region.
- Unsupported capacities or regions prevent Copilot usage regardless of model quality.

Mapped source: `MS-FAB-03`.

## MS-FAB-02 — Enable and configure Copilot in Microsoft Fabric

- **Title:** Enable and configure Copilot in Microsoft Fabric
- **Publisher:** Microsoft Learn
- **Status:** Verified
- **Evidence Level:** Direct
- **Last Reviewed:** 2026-07-17
- **Purpose:** Tenant settings, delegated capacity configuration, workspace assignment, and user access requirements.

### Verified findings

- Copilot access is controlled through the `Users can use Copilot and other features powered by Azure OpenAI` setting.
- Copilot settings can be scoped to selected security groups.
- Delegated tenant settings can be configured at the capacity level.
- Workspaces containing Copilot-enabled items must be assigned to a supported capacity.
- Users must be granted access to the relevant workspace.
- Cross-region Azure OpenAI processing is conditional and depends on the applicable geographic and compliance boundary.

## MS-FAB-03 — Enable Fabric Copilot for Power BI

- **Title:** Enable Fabric Copilot for Power BI
- **Publisher:** Microsoft Learn
- **Status:** Verified
- **Evidence Level:** Direct
- **Last Reviewed:** 2026-07-17
- **Purpose:** Power BI-specific capacity, licensing, region, workspace, and Desktop access requirements.

### Verified findings

- Standard Copilot use requires a paid Fabric capacity of F2 or higher or Power BI Premium capacity of P1 or higher.
- Trial SKUs and trial capacities are not supported.
- The capacity must be located in a supported region.
- Power BI Desktop users require Admin, Member, or Contributor access to a compatible workspace.
- Power BI Desktop requires the tenant-level Copilot setting to be enabled.
- Sovereign cloud environments are not currently supported.

## MS-MODEL-01 — Understand star schema and the importance for Power BI

**URL**

https://learn.microsoft.com/power-bi/guidance/star-schema

### Verified findings

- Microsoft recommends designing Power BI semantic models using a star schema.
- Semantic models should separate fact tables from dimension tables.
- Fact and dimension data should not be combined in the same table.
- Fact tables should maintain a consistent grain.
- Relationships should follow the star schema pattern by relating dimension tables to fact tables through one-to-many relationships.

### Evidence classification

Recommended

## MS-MODEL-02 — Use Copilot with semantic models

**URL**

https://learn.microsoft.com/power-bi/create-reports/copilot-semantic-models

### Verified findings

- Following semantic model best practices, including star schema design, improves the quality of Copilot responses.

### Evidence classification

Recommended
