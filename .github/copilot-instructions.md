# GitHub Copilot Instructions

## Project Context

This repository contains a project for preparing a Power BI semantic model for full compatibility with Microsoft Copilot in Power BI.

The target state is a Copilot Ready semantic model with clear business semantics, high-quality metadata, consistent naming, reliable relationships, documented measures and AI-friendly model structure.

## Primary Objective

Support the assessment, documentation and transformation of the Power BI semantic model into a Copilot Ready state.

All recommendations and generated changes must improve:

- semantic clarity;
- metadata quality;
- business context;
- measure discoverability;
- naming consistency;
- model maintainability;
- Copilot interpretation accuracy;
- natural-language analytics readiness.

## Working Principles

- Never invent model objects, tables, columns, measures or business rules.
- Clearly distinguish confirmed facts from assumptions.
- Ask for clarification when business meaning is unclear.
- Prefer incremental and reviewable changes.
- Do not modify business logic without explicit approval.
- Preserve existing functionality unless a change is explicitly requested.
- Explain the impact of every proposed model change.
- Identify risks, dependencies and possible regressions.

## Power BI Semantic Model Standards

When reviewing or modifying the model, evaluate:

- table and column naming;
- measure naming;
- descriptions for tables, columns and measures;
- display folders;
- relationships and cardinality;
- active and inactive relationships;
- star schema alignment;
- hidden technical fields;
- date tables;
- hierarchies;
- synonyms;
- format strings;
- data categories;
- aggregation behavior;
- calculation groups;
- DAX readability and maintainability;
- ambiguous business terminology;
- duplicate or unused objects.

## Copilot Readiness

Prioritize changes that help Copilot understand the model correctly.

Ensure that:

- business-facing objects have clear descriptions;
- technical names are not exposed unnecessarily;
- measures use explicit and meaningful names;
- columns have clear business definitions;
- synonyms support common user terminology;
- relationships reflect the intended analytical paths;
- ambiguous fields are renamed or documented;
- key business concepts are consistently represented;
- time intelligence is predictable;
- hidden objects do not confuse end users;
- model metadata supports natural-language queries.

## DAX Guidelines

For DAX:

- prefer readable and maintainable expressions;
- use variables for complex logic;
- avoid unnecessary complexity;
- preserve filter context intentionally;
- identify potential performance issues;
- explain semantic changes;
- do not rewrite validated measures without a clear benefit;
- provide before-and-after logic when refactoring.

## Documentation Guidelines

Documentation must be:

- concise;
- structured;
- enterprise-oriented;
- technically accurate;
- implementation-focused.

For each proposed change, provide:

1. Current state.
2. Identified issue.
3. Recommended change.
4. Copilot readiness benefit.
5. Technical impact.
6. Validation steps.

## Decision-Making

When multiple solutions are possible:

1. Compare alternatives.
2. Explain trade-offs.
3. Identify risks.
4. Recommend one option.
5. Explain why it best supports Copilot readiness.

## Repository Safety

- Do not delete existing files without explicit approval.
- Do not overwrite important documentation silently.
- Prefer diffs and targeted edits.
- Preserve change history.
- Keep Markdown compatible with markdownlint.
- Use only one H1 heading per Markdown document.
