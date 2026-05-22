---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260522130511490
task_id: proof-review:research/_staging/claims/chunk-23b2269a97df-p0001-01-001-child-birth-name.md
staged_draft: research/_staging/claims/chunk-23b2269a97df-p0001-01-001-child-birth-name.md
reviewed_at: 2026-05-22T13:05:11Z
decision: hold_for_conversion_qa
canonical_readiness: not_ready_conversion_conflict
source_quality_score: 0.90
conversion_confidence_score: 0.25
evidence_quantity_score: 0.66
agreement_score: 0.38
identity_confidence_score: 0.84
claim_probability: 0.89
relevance_level: direct
relevance_confidence: 0.97
next_action: reconcile_assigned_conversion_and_chunk_with_source_image_before_canonical_promotion
---

# Proof Review: Child Birth Name

## Blockers

- The assigned converted file and assigned chunk materially conflict with the staged claim. They transcribe entry 172 as child `Jose Miguel`, father `Oswaldo Burgos`, and mother `Concepcion de la Cruz`, while the staged draft and source packet describe the visible source image as child `Jose del Carmen Segundo Pulgar Arriagada`.
- Because the claim depends on a source-image reread rather than the assigned converted text, this claim should remain on hold for conversion QA before canonical promotion.
- The exact canonical name handling should stay unresolved in this review. The visible entry supports the recorded birth-name form, but this review should not normalize accents, spelling, or identity linkage beyond the source-visible name.

## Scores

| Factor | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.90 | The page image is a civil birth register and directly records the child name in the entry row. |
| conversion_confidence_score | 0.25 | The assigned converted Markdown and chunk do not support the Pulgar/Arriagada child-name claim and instead describe a different entry 172. |
| evidence_quantity_score | 0.66 | One direct page image plus the staged source packet support the name; no independent corroborating source was reviewed. |
| agreement_score | 0.38 | The image and source packet agree with the staged draft, but the assigned conversion and chunk conflict on the child-name field and related fields. |
| identity_confidence_score | 0.84 | The visible row appears to identify the child as `Jose del Carmen Segundo Pulgar Arriagada`; identity risk remains for canonical linking because the derivative text conflicts. |
| claim_probability | 0.89 | The claim is likely correct from the visible source image, but the conversion mismatch prevents a higher proof judgment. |
| relevance_level | direct | A birth registration naming the child is direct evidence for a recorded birth name. |
| relevance_confidence | 0.97 | The staged draft, source packet, image, converted file, and chunk all point to entry 172/page 58 even though their transcriptions conflict. |
| canonical_readiness | not_ready_conversion_conflict | Hold for conversion QA; do not promote until the assigned transcription/chunk is reconciled with the source image. |

## Evidence Strengths

- The visible source image for register page 58, entry 172 appears to show the child name `Jose del Carmen Segundo Pulgar Arriagada`.
- The staged source packet explicitly records the same child-name reading from the source image and flags the conversion conflict.
- The source type is a civil birth registration, so the child-name field is directly relevant to the claim and does not require a relationship or identity inference.
- No reviewed visible-source evidence contradicts the Pulgar/Arriagada child-name reading; the conflict is in the assigned derivative transcription.

## Review Judgment

This claim has direct visible-source support and a high claim probability, but it is not canonically ready. The assigned converted Markdown and chunk currently represent entry 172 as a different child and family, so the proof must remain on conversion-QA hold.

Treat this as an image-supported birth-name claim awaiting transcription reconciliation. Do not promote it from staging or use it to normalize a canonical person record until the assigned conversion/chunk are corrected or formally superseded by a targeted image reread.

## Next Action

Send the source image, converted file, and chunk through targeted conversion QA for entry 172. After reconciliation, re-review the birth-name claim using the verified source-visible name form before any canonical promotion.
