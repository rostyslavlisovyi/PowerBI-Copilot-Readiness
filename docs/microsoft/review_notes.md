# Review Notes — Power BI Copilot Readiness

> Records source ambiguities, evidence limitations, and unresolved interpretation
> questions encountered while reviewing Microsoft sources for
> [`requirements_matrix.md`](requirements_matrix.md) and
> [`references.md`](references.md).

## Purpose

This document exists so that ambiguity is recorded rather than silently resolved.
When a Microsoft source is unclear, incomplete, or open to more than one
interpretation, the ambiguity is logged here instead of being decided unilaterally
in the matrix.

## How to use this file

For each entry, record:

- **Source_ID** — the affected source from `references.md`.
- **Affected requirement(s)** — the related `PBI-*` id(s), if any.
- **Ambiguity or limitation** — what is unclear, missing, or contested.
- **Current interpretation** — how the matrix currently treats it, and why.
- **Resolution status** — `Open` or `Resolved` (with date and reviewer if resolved).

## Open Items

### 2026-07-24 — MS-MODEL-11 (Q&A synonyms): source documents a feature being retired

- **Source_ID:** MS-MODEL-11
- **Affected requirement(s):** None currently mapped in `requirements_matrix.md`. Was under
  consideration as a source for PBI-027/PBI-033 (synonyms).
- **Ambiguity:** The article "Best practices to optimize Q&A in Power BI" documents the
  classic Power BI Q&A feature. Microsoft's own documentation states Q&A experiences are
  being retired in December 2026 in favor of Copilot. It is unclear whether the underlying
  `Synonyms` model property (Tabular Object Model) that Q&A relies on is the *same* property
  Copilot reads, or whether Copilot has a separate/different synonym mechanism.
- **Current interpretation:** MS-DISC-01 ("Use Copilot with semantic models") explicitly
  lists field synonyms as Copilot grounding data, so the underlying model property is treated
  as shared. MS-MODEL-11 is kept as `Reviewed`, not `Verified`, and is not used as a source
  for any current requirement.
- **Resolution status:** Open. Re-review if Microsoft publishes Copilot-specific synonym
  guidance, or when Q&A is fully retired (December 2026) and its documentation may be removed.

### 2026-07-24 — MS-MODEL-12 (Perspectives): no confirmed Copilot applicability

- **Source_ID:** MS-MODEL-12
- **Affected requirement(s):** None currently mapped in `requirements_matrix.md`.
- **Ambiguity:** "Perspectives in tabular models" documents a Fabric/Power BI Premium +
  Analysis Services feature. No Microsoft source found during this review states that
  perspectives affect Copilot grounding, DAX generation, or Q&A/Copilot discoverability in
  any way. Perspectives may be purely a report-authoring/connection-scoping feature that is
  irrelevant to Copilot readiness.
- **Current interpretation:** Not added to `requirements_matrix.md` as a project requirement.
  No evidence currently supports treating perspectives as in-scope for Copilot readiness.
- **Resolution status:** Open. Revisit if a Copilot-specific source is found, or make an
  explicit project decision to exclude perspectives from scope (would require a `DECISIONS.md`
  entry).

### 2026-07-24 — Source granularity: several Source_IDs share one Microsoft article

- **Source_ID:** MS-COP-01, MS-COP-02 (both map to the same URL,
  `tutorial-copilot-power-bi-prepare-model#guidance`); MS-NAME-01 (spans 3 separate URLs).
- **Ambiguity:** `references.md` was originally structured as if each `Source_ID` would have
  its own dedicated Microsoft URL. In practice, Microsoft's documentation bundles several of
  these topics (naming + organization + hidden objects) into single articles, and conversely
  some single topics (naming conventions) are addressed across multiple articles
  (`copilot-evaluate-data`, `copilot-semantic-models`, `semantic-model-best-practices`).
- **Current interpretation:** Kept the existing `Source_ID` granularity (thematic, not
  1:1-with-URL) and allowed a `Source_ID` to cite more than one URL, or two `Source_IDs` to
  cite the same URL with different anchors/notes. This preserves the existing requirement
  mappings without renumbering.
- **Resolution status:** Resolved as a documented modeling choice — no change needed unless
  a future reviewer prefers strict 1:1 Source_ID-to-URL mapping.

## Resolved Items

_None yet — all entries above are still open pending future review triggers._
