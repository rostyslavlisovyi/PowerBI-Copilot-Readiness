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
| `Reviewed` | Source has been reviewed, but requirements are not fully verified |
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
- `Recommended` requirements can be excluded from an MVP readiness assessment when time or scope is limited.
- `Project` requirements must not be presented as official Microsoft requirements.
- Every requirement except a purely project-specific requirement must have a valid `Source_ID`.
- A requirement can have only one primary `Evidence Level`.
- Additional context can be documented in `review_notes.md`.

## Source Registry

| Source_ID | Document | Area | URL | Version | Last Reviewed | Status | Notes |
|---|---|---|---|---|---|---|---|
| MS-COP-01 | Semantic model naming guidance | Copilot | TBD | Current online documentation | TBD | Planned | Naming and field disambiguation guidance |
| MS-COP-02 | Organize semantic models for Copilot | Copilot | TBD | Current online documentation | TBD | Planned | Model organization, naming, and hidden objects |
| MS-COP-03 | Optimize semantic models for Copilot | Copilot | TBD | Current online documentation | TBD | Planned | Primary Copilot semantic-model guidance |
| MS-COP-04 | Prepare semantic models for AI and Copilot | Copilot | TBD | Current online documentation | TBD | Planned | Model cleanup, AI preparation, approval, and validation |
| MS-PREP-01 | Prep data for AI overview | Prep Data for AI | TBD | Current online documentation | TBD | Planned | Entry point for AI preparation features |
| MS-PREP-02 | Define an AI data schema | Prep Data for AI | TBD | Current online documentation | TBD | Planned | AI schema scope and object selection |
| MS-PREP-03 | Create verified answers | Prep Data for AI | TBD | Current online documentation | TBD | Planned | Verified answers and trigger phrases |
| MS-PREP-04 | Configure AI instructions | Prep Data for AI | TBD | Current online documentation | TBD | Planned | Business context and response instructions |
| MS-PREP-05 | AI instructions best practices | Prep Data for AI | TBD | Current online documentation | TBD | Planned | Preparation order, terminology, and fine-tuning guidance |
| MS-MODEL-01 | Understand star schema and its relevance to Power BI | Modeling | TBD | Current online documentation | TBD | Planned | Star-schema design guidance |
| MS-MODEL-03 | Model relationships in Power BI Desktop | Modeling | TBD | Current online documentation | TBD | Planned | Cardinality, active relationships, and model integrity |
| MS-MODEL-09 | Calculation groups | Modeling | TBD | Current online documentation | TBD | Planned | Calculation-group behavior and metadata |
| MS-MODEL-11 | Q&A synonyms | Modeling | TBD | Current online documentation | TBD | Planned | Verify direct applicability to Copilot |
| MS-MODEL-12 | Perspectives | Modeling | TBD | Current online documentation | TBD | Planned | Verify direct applicability to Copilot |
| MS-MODEL-13 | Data categories in Power BI Desktop | Modeling | TBD | Current online documentation | TBD | Planned | Data-category metadata |
| MS-FAB-02 | Copilot tenant settings | Fabric Administration | TBD | Current online documentation | TBD | Planned | Tenant settings and cross-region processing |
| MS-FAB-03 | Copilot regional availability and capacity requirements | Fabric Administration | TBD | Current online documentation | TBD | Planned | Capacity, SKU, and regional availability |

## Review Process

For every source:

1. Add the official Microsoft Learn URL.
2. Record the date on which the source was reviewed.
3. Identify the requirements supported by the source.
4. Confirm whether each requirement is `Direct`, `Derived`, or `Recommended`.
5. Add findings and ambiguities to `review_notes.md`.
6. Change the source status to `Verified` only after all mapped requirements have been checked.

## Maintenance Rules

- Review verified sources after significant Microsoft Fabric or Power BI Copilot announcements.
- Do not change an existing `Source_ID` when only the title or URL changes.
- Mark replaced sources as `Deprecated`.
- Add the replacement source as a new registry entry when its meaning or scope differs materially.
- Do not delete deprecated sources while requirements or historical notes still reference them.
