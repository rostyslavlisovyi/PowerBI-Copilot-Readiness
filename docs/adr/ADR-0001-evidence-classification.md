# ADR-0001: Evidence Classification for Readiness Requirements

## Status

Accepted

## Date

2026-07-17

## Context

The Power BI Copilot Readiness requirements matrix contains requirements from several different origins.

Some requirements are explicitly stated in Microsoft documentation. Others are inferred from Microsoft guidance, presented as recommended practices, or introduced by this project based on implementation experience.

Priority alone does not explain the origin or authority of a requirement.

For example, a requirement can have a high priority for a specific implementation without being a mandatory Microsoft prerequisite. Similarly, a Microsoft recommendation can improve answer quality without blocking an MVP pilot.

Without an explicit evidence classification, users of the matrix might:

- treat recommendations as mandatory requirements;
- present project-specific practices as Microsoft requirements;
- spend time implementing optional improvements before completing prerequisites;
- exclude important derived requirements without understanding their rationale;
- lose traceability between requirements and their supporting sources.

## Decision

Every requirement in `requirements_matrix.md` will include an `Evidence Level` field.

The supported evidence levels are:

| Evidence Level | Meaning |
|---|---|
| `Direct` | Microsoft explicitly states the requirement or prerequisite |
| `Derived` | The requirement is inferred from one or more Microsoft sources |
| `Recommended` | Microsoft presents the item as guidance or a best practice rather than a mandatory Copilot requirement |
| `Project` | The requirement is defined by this project based on implementation experience |

Evidence level and priority are independent.

- `Evidence Level` describes the origin and authority of a requirement.
- `Priority` describes the implementation importance of a requirement.
- `Status` describes the current implementation state.

The matrix will therefore use the following core fields:

```text
ID
Requirement
Category
Source_ID
Evidence Level
Priority
Status
Notes
