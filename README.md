# Power BI Copilot Readiness

> Microsoft Learn–based framework for assessing and improving Power BI semantic models for Microsoft Copilot.

## Purpose

This repository translates Microsoft Learn guidance into a structured set of readiness requirements for assessing Power BI semantic models.

It provides:

- a canonical requirements matrix;
- Microsoft source traceability;
- evidence classification;
- executable assessment rules;
- governance for safe remediation.

## Repository

```text
docs/
├── microsoft/
│   ├── requirements_matrix.md
│   ├── references.md
│   └── review_notes.md
├── adr/
│   └── ADR-0001-evidence-classification.md

.github/
└── copilot-instructions.md

rules.yaml
PROJECT.md
TASKS.md
DECISIONS.md
```

## Readiness Model

Current baseline:

- 55 readiness requirements (`PBI-001`–`PBI-055`)
- Microsoft Learn source registry
- Evidence classification
- Requirement priorities
- Assessment statuses
- Executable rule mappings

Categories:

- Prerequisites
- Modeling
- Relationships
- Naming
- Measures
- Metadata
- Discoverability
- Hidden Objects
- Security
- AI Preparation
- Testing

## Evidence Levels

| Level | Meaning |
|-------|---------|
| Direct | Explicit Microsoft requirement |
| Derived | Inferred from Microsoft guidance |
| Recommended | Microsoft best practice |
| Project | Project-specific rule |

## Assessment Workflow

```text
Semantic Model
      ↓
Baseline Assessment
      ↓
Findings
      ↓
Recommendations
      ↓
Human Approval
      ↓
Remediation
      ↓
Re-assessment
```

Assessment is read-only by default.

Automatic modification of relationships, security, or business metadata is outside the MVP scope.

## Current Scope

Implemented:

- ✅ Microsoft Learn evidence registry
- ✅ Requirements matrix
- ✅ Cross-document traceability
- ✅ Governance rules
- ✅ Assessment framework

Next:

- Live semantic model assessment
- Baseline generation
- Findings report
- Controlled remediation
- MCP automation

## Development

Clone:

```bash
git clone https://github.com/rostyslavlisovyi/PowerBI-Copilot-Readiness.git
cd PowerBI-Copilot-Readiness
```

Validate YAML:

```bash
ruby -e "require 'yaml'; YAML.load_file('rules.yaml'); puts 'rules.yaml: valid'"
```

Commit using Conventional Commits, for example:

```text
docs: update readiness requirements
feat: add live model assessment
fix: align executable rules
test: validate requirement mappings
```

## Disclaimer

This project is an independent implementation based on Microsoft Learn documentation and is not an official Microsoft product.