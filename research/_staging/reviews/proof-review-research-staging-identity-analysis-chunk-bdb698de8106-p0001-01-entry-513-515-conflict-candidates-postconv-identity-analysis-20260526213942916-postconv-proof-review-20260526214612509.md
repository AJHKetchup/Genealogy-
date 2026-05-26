---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260526214612509
task_id: "proof-review:research/_staging/identity-analysis/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-postconv-identity-analysis-20260526213942916.md"
staged_draft: "research/_staging/identity-analysis/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-postconv-identity-analysis-20260526213942916.md"
reviewed:
  - "raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md"
  - "raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md"
  - "research/_staging/source-packets/chunk-bdb698de8106-p0001-01-entry-513-515-proof-review-revision-postconv-evidence-extraction-20260526193717806.md"
  - "research/_staging/conflicts/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-evidence-extraction-20260526193717806.md"
  - "research/_staging/relationships/chunk-bdb698de8106-p0001-01-513-child-parents-proof-review-revision-postconv-evidence-extraction-20260526193717806.md"
  - "research/_staging/reviews/conversion-review-note-CHUNK-bdb698de8106-P0001-01-proof-review-revision-20260526.md"
  - "research/_staging/reviews/conversion-review-note-CHUNK-bdb698de8106-P0001-01-entry-513-image-reconciliation.md"
source_quality_score: 0.78
conversion_confidence_score: 0.28
evidence_quantity_score: 0.58
agreement_score: 0.40
identity_confidence_score: 0.36
claim_probability: 0.48
relevance_level: high
relevance_confidence: 0.96
canonical_readiness: hold
promotion_recommendation: hold_for_conversion_qa
created: 2026-05-26
---

# Proof Review: Entry 513 And 515 Conflict Candidates

## Blockers First

1. The staged identity-analysis draft is properly held. Its main conclusion depends on unresolved conversion conflicts in entry 513 child identity, entry 513 mother surname, and entry 515 child/father readings.
2. The converted file and chunk literally support the derivative readings `Isolina del Carmen Jose`, `Jose del Carmen Pulgar`, `Juana de Dios Amador de Pulgar`, `Jose del C. Pulgar`, `Rosa Elvira del Carmen`, and `Pedro Pablo Leiva`; however, the referenced conversion-review notes directly challenge key row-level fields and require targeted QA before promotion.
3. Entry 513 may be Pulgar-family relevant, but it cannot support a canonical child identity or parent-child relationship while the child-name/sex field and mother surname remain unstable.
4. Entry 515 has low claim value for the Pulgar question and is retained only as a conversion-QA control. Its converted child and father/declarant readings should not be promoted.
5. No reviewed source text names Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario J. Pulgar Arriagada, or Dario Pulgar Arriagada. Any Dario connection remains unsupported by this staged draft.

## Evidence Strengths

- The source type is a civil birth register page, which is generally high-quality direct evidence when the row transcription is stable.
- Source identity is well controlled: the converted file, chunk, source packet, and conflict draft all point to the same source image SHA-256 and chunk id `CHUNK-bdb698de8106-P0001-01`.
- The derivative conversion and chunk agree with each other for the entry 513 Pulgar father/declarant reading.
- The staged draft correctly keeps image-review alternatives as conflict indicators rather than silently replacing the converted transcription.
- The staged draft correctly recommends `hold_for_conversion_qa` and does not promote a canonical merge, rename, parent-child attachment, or Dario-line bridge.

## Scored Judgment

| Metric | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.78 | Civil register evidence is strong in principle, but this review relies on staged derivative and review layers rather than a certified final transcription. |
| conversion_confidence_score | 0.28 | Multiple referenced notes identify unresolved row-level transcription conflicts. |
| evidence_quantity_score | 0.58 | There is enough local evidence to justify a hold and targeted QA, but not enough stable evidence for atomic identity promotion. |
| agreement_score | 0.40 | Converted file and chunk agree with each other, but conflict with image-review notes on material fields. |
| identity_confidence_score | 0.36 | Entry 513 is plausibly Pulgar-relevant; exact child, mother, and cross-record identities remain uncertain. |
| claim_probability | 0.48 | The broad hold analysis is more probable than any promoted identity claim. Exact endpoint claims remain below promotion threshold. |
| relevance_level | high | The staged draft directly addresses the assigned conflict candidates and Pulgar-line guardrails. |
| relevance_confidence | 0.96 | The reviewed files all reference the assigned staged draft, source packet, chunk, or directly related QA notes. |
| canonical_readiness | hold | No canonical action is ready. |

## Claim-Level Review

| Claim or hypothesis | Literal support | Risk | Probability | Canonical readiness |
| --- | --- | --- | ---: | --- |
| Entry 513 is Pulgar-family relevant | Converted/chunk text gives father `Jose del Carmen Pulgar` and declarant `Jose del C. Pulgar`. | Moderate: row is still conversion-conflicted. | 0.62 | hold |
| Entry 513 child is `Isolina del Carmen Jose` | Converted/chunk text supports this derivative reading. | High: conversion-review notes challenge the child-name field. | 0.30 | hold |
| Entry 513 mother is `Juana de Dios Amador de Pulgar` | Converted/chunk text supports this derivative reading. | High: conversion-review notes preserve `Amagada`/`Arriagada`-style alternatives. | 0.34 | hold |
| Entry 513 father/declarant is `Jose del Carmen Pulgar` / `Jose del C. Pulgar` | Converted/chunk and review notes treat this as the stronger part of the row. | Moderate: same-name merge to an existing person is not proved. | 0.58 | hold |
| Entry 513 establishes a parent-child relationship | Father and mother fields exist in the derivative transcript. | High: child endpoint and mother surname are unstable. | 0.32 | hold |
| Entry 515 is `Rosa Elvira del Carmen`, child of `Pedro Pablo Leiva` | Converted/chunk text supports this derivative reading. | High: referenced notes say the entry is partial/conflicted. | 0.25 | hold |
| Any Dario/Pulgar-Arriagada or Pulgar-Smith bridge | No direct literal support in the reviewed register material. | Very high: would conflate identities by surname context only. | 0.03 | not ready |

## Reliability And Conflict Assessment

The staged draft's caution is supported. The converted/chunk text is useful as a derivative reference but not sufficient for promotion because the referenced QA notes identify material disagreements with direct image review. The father/declarant reading for entry 513 is the strongest family-relevant element, but it still does not prove a same-person match to an existing `Jose del Carmen Pulgar` page or any Dario-line identity.

Relationship jumps are the main risk. A parent-child claim requires a stable child endpoint, and entry 513 does not yet have one. A mother identity claim also remains unsafe because `Amador`, `Amagada`, and `Arriagada`-style readings are not interchangeable without a certified source reading.

## Next Action

Keep the staged identity-analysis draft on `hold_for_conversion_qa`. Run the already requested targeted conversion QA for `CHUNK-bdb698de8106-P0001-01`, then rerun proof review on separate atomic claims for entry 513 child name/sex, mother surname, father/declarant, and any relationship candidate. Do not promote or attach any Dario-line identity from this evidence.
