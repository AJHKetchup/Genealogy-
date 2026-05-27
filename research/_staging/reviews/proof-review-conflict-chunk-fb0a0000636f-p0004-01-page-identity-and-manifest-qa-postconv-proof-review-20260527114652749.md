---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260527114652749
task_id: proof-review:research/_staging/identity-analysis/conflict-chunk-fb0a0000636f-p0004-01-page-identity-and-manifest-qa-postconv-identity-analysis-20260527071507256.md
staged_draft: research/_staging/identity-analysis/conflict-chunk-fb0a0000636f-p0004-01-page-identity-and-manifest-qa-postconv-identity-analysis-20260527071507256.md
reviewed: 2026-05-27
canonical_readiness: blocked
---

# Proof Review: CHUNK-fb0a0000636f-P0004-01 Page Identity And Manifest QA

## Blockers First

1. Page-control conflict blocks promotion. The rendered page image for page 4 shows continuation text followed by `2000` IBRD / Bolivia, Peru / Senior Consultant and `1999 - 2000` Antamina Mining Company / Huarmey, Peru / Head Community Relations. The referenced chunk and source packet instead contain 1988-1989 FAO, 1988 CIDA, 1986-1987 WIF, and 1982-1985 independent consultant entries.
2. Manifest integrity is unresolved. The chunk manifest lists `CHUNK-fb0a0000636f-P0004-01` twice for the same page path and page number with different `chars` and `sha256` values.
3. The source-packet occupational claims are not safely promotable as page-4 claims. They are supported by the current chunk file, but not by the visible page-4 image.
4. The page body does not name `Dario Arturo Pulgar`. Subject attribution is document-level from the PDF title and converted-file title, not page-local identity proof.
5. No reviewed evidence from this page supports any relationship claim, same-person merge, parent/child bridge, or attachment to canonical Pulgar-line candidates.

## Evidence Reviewed

- Staged draft: `research/_staging/identity-analysis/conflict-chunk-fb0a0000636f-p0004-01-page-identity-and-manifest-qa-postconv-identity-analysis-20260527071507256.md`.
- Conflict candidate: `research/_staging/conflicts/conflict-chunk-fb0a0000636f-p0004-01-page-identity-and-manifest-qa.md`.
- Source packet: `research/_staging/source-packets/chunk-fb0a0000636f-p0004-01-cv-dario-arturo-pulgar-work-history.md`.
- Referenced chunk: `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0004-chunk-01.md`.
- Converted Markdown: `raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md`.
- Chunk manifest: `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/manifest.json`.
- Rendered page image: `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0004.jpg`.

## Scored Judgment

| score | value | rationale |
|---|---:|---|
| source_quality_score | 0.66 | The source is a local CV with a rendered page image, but the assigned page/chunk controls are inconsistent. |
| conversion_confidence_score | 0.34 | Individual text is readable, but page identity and manifest integrity are not reliable for this staged chunk. |
| evidence_quantity_score | 0.58 | There are multiple local controls, yet they disagree on the page body attached to this chunk id. |
| agreement_score | 0.36 | Page image and current converted page agree with each other; chunk and source packet agree with each other; the two groups conflict. |
| identity_confidence_score | 0.62 | Document-level subject attribution to Dario Arturo Pulgar is plausible from titles, but page-local identity proof is absent. |
| claim_probability | 0.90 | High probability that the staged draft correctly identifies a page-control/manifest conflict; only 0.18 for promoting the 1982-1989 entries as page-4 claims now. |
| relevance_level | high | The conflict directly controls whether claims from this staged draft can be used. |
| relevance_confidence | 0.96 | The reviewed materials all concern the same assigned staged draft and chunk id. |
| canonical_readiness | blocked | Source-prep/conversion QA must reconcile the duplicate manifest and page identity before proof promotion. |

## Evidence Strengths

The staged draft's hold recommendation is supported. The page image visibly matches the current converted file's page-4 text for the 2000 IBRD and 1999-2000 Antamina entries, while the referenced chunk and source packet consistently preserve the 1982-1989 occupational text. This supports treating the issue as a control problem rather than a genealogical contradiction.

The source title and converted-file title support tentative document-level attribution to `Dario Arturo Pulgar`. That attribution should not be expanded into a canonical identity bridge because the reviewed page body gives no name, family relationship, birth detail, residence bridge, or other same-person proof.

## Next Action

Hold the staged draft for targeted source-prep/conversion QA. Reconcile the duplicate `CHUNK-fb0a0000636f-P0004-01` manifest entries, determine which physical page controls the 1982-1989 text, and regenerate affected source packets or staged claims through the proper workflow. Rerun proof review after QA before any canonical claim, relationship, merge, or wiki update.
