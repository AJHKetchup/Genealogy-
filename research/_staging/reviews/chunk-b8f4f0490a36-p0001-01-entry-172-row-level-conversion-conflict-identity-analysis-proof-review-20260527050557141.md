---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527030052086.md
staged_draft: research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527030052086.md
reviewer: postconv-proof-review-20260527050557141
review_date: 2026-05-27
review_status: hold
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict Identity Analysis

## Blockers

- Hold for conversion QA: the staged identity analysis is correct to identify a severe row-level conflict. The source image and assigned chunk support physical entry `172` as the Pulgar/Arriagada row, while the current converted Markdown records entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
- The converted file cannot be used as canonical support for the Pulgar/Arriagada birth claim until conversion-control reconciles or supersedes the conflicting Burgos/de la Cruz transcription.
- The father field should not be promoted with the chunk's terminal `S.`. The source packet and targeted QA note certify only `Jose del Carmen Pulgar`; the mark after `Pulgar` remains unresolved from this review.
- No relationship or identity bridge is supported from this row to `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`. The row names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario or Arturo.
- Parent candidates must remain scoped to this entry. This review does not merge `Jose del Carmen Pulgar` or `Juana Arriagada de Pulgar` with same-name or variant-name canonical/stub people outside the row.

## Scores

- source_quality_score: 0.88
- conversion_confidence_score: 0.46
- evidence_quantity_score: 0.70
- agreement_score: 0.58
- identity_confidence_score: 0.76
- claim_probability: 0.82
- relevance_level: critical
- relevance_confidence: 0.96
- canonical_readiness: hold_for_conversion_qa

## Evidence Strengths

- The original source image is available and visibly shows page 58, physical row `172`, with the child name read as `Jose del Carmen Segundo Pulgar Arriagada`.
- The visible row supports the staged packet's main facts: registration date `Siete de Abril`, birth date `Ocho de Marzo`, father `Jose del Carmen Pulgar`, mother `Juana Arriagada de Pulgar`, informant `Ernesto Herrera L.`, and page/entry control for row `172`.
- The assigned chunk agrees with the Pulgar/Arriagada row on the central identity, parent, date, and informant fields.
- The staged identity analysis preserves the derivative conflict and appropriately recommends `hold_for_conversion_qa` rather than canonical promotion.

## Review Judgment

The staged identity analysis is well supported as a conflict analysis. Physical row `172` in the referenced source image is the Pulgar/Arriagada registration, not the Burgos/de la Cruz entry currently present in the converted Markdown. The claim probability is high for the local row-control finding and moderate-high for the identity of the registered child within this source.

Canonical readiness remains low because the verification context is internally split across derivative layers. The image, chunk, source packet, and targeted QA note support the Pulgar/Arriagada reading; the converted Markdown materially disagrees on child, parents, birth date, birthplace/residence context, informant, and officer/signature context. That disagreement must be resolved before tree-impacting claims or relationships are promoted.

## Next Action

Send to conversion-control for reconciliation of `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md` and the associated chunk/page derivatives against the source image for page 58, entry `172`.

After conversion reconciliation, rerun proof review for any promoted child-birth, parent-child, or identity-merge claims. Carry the father as `Jose del Carmen Pulgar` with suffix unresolved unless a focused source review certifies the terminal mark.
