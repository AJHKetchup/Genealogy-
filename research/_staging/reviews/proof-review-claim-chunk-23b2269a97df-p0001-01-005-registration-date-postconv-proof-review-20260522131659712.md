---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260522131659712
task_id: proof-review:research/_staging/claims/chunk-23b2269a97df-p0001-01-005-registration-date.md
staged_draft: research/_staging/claims/chunk-23b2269a97df-p0001-01-005-registration-date.md
reviewed_at: 2026-05-22T13:17:45Z
decision: hold_for_conversion_qa
canonical_readiness: not_ready_conversion_conflict
source_quality_score: 0.90
conversion_confidence_score: 0.25
evidence_quantity_score: 0.66
agreement_score: 0.36
identity_confidence_score: 0.84
claim_probability: 0.91
relevance_level: direct
relevance_confidence: 0.97
next_action: reconcile_assigned_conversion_and_chunk_with_source_image_before_canonical_promotion
---

# Proof Review: Registration Date

## Blockers

- The assigned converted file and assigned chunk materially conflict with the staged registration-date claim's identity context. They transcribe entry 172 as child `Jose Miguel`, with parents `Oswaldo Burgos` and `Concepcion de la Cruz`, while the staged draft and source packet describe the visible source image as `Jose del Carmen Segundo Pulgar Arriagada`, child of the Pulgar/Arriagada family.
- The date value itself is not the main conflict: the assigned conversion/chunk and the source-image reread both place entry 172's registration date on `Siete de Abril de mil ochocientos ochenta i ocho`. The blocker is that the derivative text attaches that date to a different transcribed entry identity and surrounding event data.
- Because the claim depends on a source-image reread for the subject identity, this claim should remain on hold for conversion QA before canonical promotion.
- Do not use this review to alter the transcript, normalize the Spanish wording, or promote the claim to a canonical person page. The visible-source support is sufficient for a scored proof judgment, but the derivative conversion/chunk mismatch must be reconciled first.

## Scores

| Factor | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.90 | The page image is a civil birth register and directly records the registration date in the entry row. |
| conversion_confidence_score | 0.25 | The assigned converted Markdown and chunk preserve the same registration date but do not support the Pulgar/Arriagada subject identity and instead describe a different entry 172. |
| evidence_quantity_score | 0.66 | One direct page image plus the staged source packet support the registration-date reading; no independent corroborating source was reviewed. |
| agreement_score | 0.36 | The image, source packet, staged draft, conversion, and chunk agree on 7 April 1888 as the registration date, but the derivative conversion and chunk conflict on child identity, birth event, and family fields. |
| identity_confidence_score | 0.84 | The visible row appears to identify the child as `Jose del Carmen Segundo Pulgar Arriagada`; identity risk remains for canonical linking because the derivative text conflicts. |
| claim_probability | 0.91 | The visible source image appears to read `Siete de Abril ... de mil ochocientos ochenta i ocho`, and the derivative text also has this registration date, making the date claim highly probable despite identity-context conflict. |
| relevance_level | direct | A civil birth registration's registration-date field is direct evidence for the date the entry was registered. |
| relevance_confidence | 0.97 | The staged draft, source packet, image, converted file, and chunk all point to entry 172/page 58 even though their subject transcriptions conflict. |
| canonical_readiness | not_ready_conversion_conflict | Hold for conversion QA; do not promote until the assigned transcription/chunk is reconciled with the source image. |

## Evidence Strengths

- The visible source image for register page 58, entry 172 appears to show the registration-date field as `Siete de Abril ... de mil ochocientos ochenta i ocho`.
- The staged source packet records the same image-level registration-date reading and explicitly flags the conversion conflict.
- The assigned converted file and chunk also transcribe the entry 172 registration date as `Siete de Abril de mil ochocientos ochenta i ocho`, so the date value is unusually well aligned even though the surrounding identity context is not.
- The source type is a civil birth registration, so the registration-date field is directly relevant and does not require a relationship inference.

## Review Judgment

This claim has direct visible-source support and a high claim probability for the registration date `1888-04-07`, but it is not canonically ready. The assigned converted Markdown and chunk currently represent entry 172 as a different child and family, so the proof must remain on conversion-QA hold.

Treat this as an image-supported recorded-registration-date claim awaiting transcription reconciliation. Do not promote it from staging or attach it to a canonical person record until the assigned conversion/chunk are corrected or formally superseded by a targeted image reread.

## Next Action

Send the source image, converted file, and chunk through targeted conversion QA for entry 172. After reconciliation, re-review the registration-date claim using the verified source-visible child identity and registration-date field before any canonical promotion.
