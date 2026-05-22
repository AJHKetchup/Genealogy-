---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260522131453055
task_id: proof-review:research/_staging/claims/chunk-23b2269a97df-p0001-01-004-birth-place.md
staged_draft: research/_staging/claims/chunk-23b2269a97df-p0001-01-004-birth-place.md
reviewed_at: 2026-05-22T13:14:53Z
decision: hold_for_conversion_qa
canonical_readiness: not_ready_conversion_conflict
source_quality_score: 0.90
conversion_confidence_score: 0.25
evidence_quantity_score: 0.66
agreement_score: 0.36
identity_confidence_score: 0.84
claim_probability: 0.90
relevance_level: direct
relevance_confidence: 0.97
next_action: reconcile_assigned_conversion_and_chunk_with_source_image_before_canonical_promotion
---

# Proof Review: Birth Place

## Blockers

- The assigned converted file and assigned chunk materially conflict with the staged birth-place claim. They transcribe entry 172 as child `Jose Miguel`, born in `En esta`, with parents `Oswaldo Burgos` and `Concepcion de la Cruz`, while the staged draft and source packet describe the visible source image as `Jose del Carmen Segundo Pulgar Arriagada`, born at `Calle de Valdivia`.
- Because the claim depends on a source-image reread rather than the assigned converted text, this claim should remain on hold for conversion QA before canonical promotion.
- Do not use this review to alter the transcript, geocode the street, modernize the place, or normalize the source wording. The visible-source support is sufficient for a scored proof judgment, but the derivative conversion/chunk mismatch must be reconciled first.

## Scores

| Factor | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.90 | The page image is a civil birth register and directly records the birth-place field in the entry row. |
| conversion_confidence_score | 0.25 | The assigned converted Markdown and chunk do not support the Pulgar/Arriagada birth-place claim and instead describe a different entry 172. |
| evidence_quantity_score | 0.66 | One direct page image plus the staged source packet support the place reading; no independent corroborating source was reviewed. |
| agreement_score | 0.36 | The image and source packet agree with the staged draft, but the assigned conversion and chunk conflict on the child identity, birth place, date/time, and family fields. |
| identity_confidence_score | 0.84 | The visible row appears to identify the child as `Jose del Carmen Segundo Pulgar Arriagada`; identity risk remains for canonical linking because the derivative text conflicts. |
| claim_probability | 0.90 | The visible source image appears to read `Calle de Valdivia` in the birth-place field, making the claim likely correct despite the conversion mismatch. |
| relevance_level | direct | A civil birth registration's birth-place field is direct evidence for the recorded birth place. |
| relevance_confidence | 0.97 | The staged draft, source packet, image, converted file, and chunk all point to entry 172/page 58 even though their transcriptions conflict. |
| canonical_readiness | not_ready_conversion_conflict | Hold for conversion QA; do not promote until the assigned transcription/chunk is reconciled with the source image. |

## Evidence Strengths

- The visible source image for register page 58, entry 172 appears to show the birth-place field as `Calle de Valdivia`.
- The staged source packet records the same image-level birth-place reading and explicitly flags the conversion conflict.
- The source type is a civil birth registration, so the birth-place field is directly relevant and does not require a relationship inference.
- No reviewed visible-source evidence contradicts the `Calle de Valdivia` reading; the conflict is in the assigned derivative transcription and its mismatched identity context.

## Review Judgment

This claim has direct visible-source support and a high claim probability, but it is not canonically ready. The assigned converted Markdown and chunk currently represent entry 172 as a different child and birth event, so the proof must remain on conversion-QA hold.

Treat this as an image-supported recorded-birth-place claim awaiting transcription reconciliation. Do not promote it from staging or attach it to a canonical person record until the assigned conversion/chunk are corrected or formally superseded by a targeted image reread.

## Next Action

Send the source image, converted file, and chunk through targeted conversion QA for entry 172. After reconciliation, re-review the birth-place claim using the verified source-visible child and birth-place fields before any canonical promotion.
