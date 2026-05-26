---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260526220304765
task_id: "proof-review:research/_staging/identity-analysis/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-postconv-identity-analysis-20260526213942916.md"
staged_draft: "research/_staging/identity-analysis/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-postconv-identity-analysis-20260526213942916.md"
reviewed:
  - "research/_staging/conflicts/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-evidence-extraction-20260526193717806.md"
  - "research/_staging/source-packets/chunk-bdb698de8106-p0001-01-entry-513-515-proof-review-revision-postconv-evidence-extraction-20260526193717806.md"
  - "raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md"
  - "raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md"
  - "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png"
created: 2026-05-26
canonical_readiness: hold
---

# Proof Review: Entries 513 And 515 Identity Analysis

## Blockers First

1. Canonical readiness is `hold`. The reviewed identity-analysis draft correctly treats entries 513 and 515 as conversion-QA blocked rather than promotion-ready.
2. Entry 513 has direct Pulgar-family relevance, but the child-name field is not stable enough to support a canonical child identity. The converted/chunk text reads `Isolina del Carmen` / `Jose` with sex `Masculino`, while the source image visibly supports a Pulgar-related child-name concern and warrants targeted paleographic QA before any endpoint is fixed.
3. Entry 513 mother identity is unresolved. The converted/chunk text reads `Juana de Dios Amador de Pulgar`, but the visible source and prior QA concern make this a material surname-reading conflict, not a safe normalization to Amador, Amagada, Arriagada, or any other Juana candidate.
4. Entry 515 remains a conversion-QA control only. The converted/chunk text reads `Rosa Elvira del Carmen` and `Pedro Pablo Leiva`, but the row sits at the lower edge of the provided page image and prior proof concern reports partial/bottom-crop uncertainty. No entry-515 identity or relationship should be promoted from this review.
5. The staged draft does not literally name or bridge to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or related Dario/Pulgar-Arriagada candidates. Those remain anti-conflation guardrails only.

## Evidence Strengths

- The converted file, chunk, source packet, and conflict draft consistently identify the same source page: Los Angeles, La Laja, Chile civil birth register page 172, entries 513-515.
- Entry 513 father/declarant support is comparatively strong. The converted/chunk text names `Jose del Carmen Pulgar` as father and `Jose del C. Pulgar` as father/declarant; the source image visibly supports a Pulgar father/declarant reading at a high level.
- The staged identity-analysis draft does not overpromote the evidence. Its `hold_for_conversion_qa` status and low canonical-readiness conclusion are aligned with the unresolved row-level reading conflicts.
- The draft keeps image-review alternatives separate from replacement transcription, which preserves the boundary between verification context and source transcription.

## Scores

| Metric | Score | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.78 | Civil birth register page is a strong source type, but the available image is high-contrast and difficult in key handwritten fields. |
| conversion_confidence_score | 0.30 | Converted/chunk readings are internally consistent, but entry 513 child/mother fields and entry 515 identity fields remain materially disputed. |
| evidence_quantity_score | 0.46 | One direct page plus derivative conversion/chunk/source-packet layers; not enough independent evidence for identity merges. |
| agreement_score | 0.42 | Converted and chunk text agree with each other, but proof-review/image-review concerns disagree on the fields that matter most. |
| identity_confidence_score | 0.36 | Adequate for treating entry 513 as Pulgar-relevant; insufficient for a stable child identity, mother identity, or cross-record merge. |
| claim_probability | 0.52 | Probable that entry 513 contains Pulgar-family evidence; not probable enough that the exact staged identity endpoints are correct. |
| relevance_level | 0.96 | Directly relevant to the staged identity analysis and Pulgar-line conflict review. |
| relevance_confidence | 0.94 | The reviewed materials all point to the same page, chunk, source packet, and entry cluster. |
| canonical_readiness | 0.06 | Hold. No promotion, merge, rename, or parent-child attachment should follow until targeted conversion QA is complete. |

## Claim Probability Notes

- Entry 513 as a Pulgar-family register row: moderate probability, approximately 0.65, because father/declarant Pulgar support is visible and repeated across derivative files.
- Entry 513 exact child identity as converted: low probability, approximately 0.28, because the child-name field is one of the central unstable readings.
- Entry 513 exact mother identity as `Juana de Dios Amador de Pulgar`: low-to-moderate probability, approximately 0.34, because it is supported by conversion text but materially challenged by review context.
- Entry 515 exact child-father identity as converted: low probability, approximately 0.24, because the row is partial/edge-affected and already flagged for QA.
- Any Dario/Pulgar-Smith or Dario/Pulgar-Arriagada bridge from this draft: unsupported, approximately 0.03.

## Next Action

Run targeted conversion QA against the source image for entry 513 child name/sex, mother surname, father/declarant occupation, and entry 515 child/father-declarant fields. After QA, rerun proof review on atomic claims and relationship candidates before any canonical edit.
