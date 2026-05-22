---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260522130719068
task_id: proof-review:research/_staging/claims/chunk-23b2269a97df-p0001-01-002-child-sex.md
staged_draft: research/_staging/claims/chunk-23b2269a97df-p0001-01-002-child-sex.md
reviewed_at: 2026-05-22T13:07:19Z
decision: hold_for_conversion_qa
canonical_readiness: not_ready_conversion_conflict
source_quality_score: 0.90
conversion_confidence_score: 0.25
evidence_quantity_score: 0.66
agreement_score: 0.52
identity_confidence_score: 0.84
claim_probability: 0.91
relevance_level: direct
relevance_confidence: 0.97
next_action: reconcile_assigned_conversion_and_chunk_with_source_image_before_canonical_promotion
---

# Proof Review: Child Sex

## Blockers

- The assigned converted file and assigned chunk materially conflict with the staged claim's subject. They transcribe entry 172 as child `José Miguel`, father `Oswaldo Burgos`, and mother `Concepcion de la Cruz`, while the staged draft and source packet describe the visible source image as child `Jose del Carmen Segundo Pulgar Arriagada`.
- Because the claim depends on a source-image reread rather than the assigned converted text, this claim should remain on hold for conversion QA before canonical promotion.
- The derivative converted text records a male sex value for its mismatched child, but it does not verify that `Jose del Carmen Segundo Pulgar Arriagada` was the child in the assigned transcript. Do not use the derivative agreement on sex alone to bypass the identity/transcription conflict.

## Scores

| Factor | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.90 | The page image is a civil birth register and directly records a sex field in the entry row. |
| conversion_confidence_score | 0.25 | The assigned converted Markdown and chunk do not support the Pulgar/Arriagada subject and instead describe a different entry 172. |
| evidence_quantity_score | 0.66 | One direct page image plus the staged source packet support the sex reading; no independent corroborating source was reviewed. |
| agreement_score | 0.52 | The image and source packet agree with the staged draft. The assigned conversion has a male sex term for a different child, so it only weakly agrees on the sex value and conflicts on identity. |
| identity_confidence_score | 0.84 | The visible row appears to identify the child as `Jose del Carmen Segundo Pulgar Arriagada`; identity risk remains for canonical linking because the derivative text conflicts. |
| claim_probability | 0.91 | The sex field for the visible Pulgar/Arriagada row appears to read `Hombre`, making the claim likely correct despite the conversion mismatch. |
| relevance_level | direct | A birth registration sex field is direct evidence for the recorded sex of the child. |
| relevance_confidence | 0.97 | The staged draft, source packet, image, converted file, and chunk all point to entry 172/page 58 even though their transcriptions conflict. |
| canonical_readiness | not_ready_conversion_conflict | Hold for conversion QA; do not promote until the assigned transcription/chunk is reconciled with the source image. |

## Evidence Strengths

- The visible source image for register page 58, entry 172 appears to show the child name `Jose del Carmen Segundo Pulgar Arriagada` with sex recorded as `Hombre`.
- The staged source packet explicitly records the same image-level sex reading and flags the conversion conflict.
- The source type is a civil birth registration, so the sex field is directly relevant and does not require a relationship inference.
- No reviewed visible-source evidence contradicts the `Hombre` reading; the conflict is in the assigned derivative transcription and its mismatched identity context.

## Review Judgment

This claim has direct visible-source support and a high claim probability, but it is not canonically ready. The assigned converted Markdown and chunk currently represent entry 172 as a different child and family, so the proof must remain on conversion-QA hold.

Treat this as an image-supported recorded-sex claim awaiting transcription reconciliation. Do not promote it from staging or attach it to a canonical person record until the assigned conversion/chunk are corrected or formally superseded by a targeted image reread.

## Next Action

Send the source image, converted file, and chunk through targeted conversion QA for entry 172. After reconciliation, re-review the sex claim using the verified source-visible child and sex fields before any canonical promotion.
