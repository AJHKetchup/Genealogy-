---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260522125900173
task_id: proof-review:research/_staging/relationships/chunk-23b2269a97df-p0001-01-001-child-mother.md
staged_draft: research/_staging/relationships/chunk-23b2269a97df-p0001-01-001-child-mother.md
reviewed_at: 2026-05-22T12:59:00Z
decision: hold_for_conversion_qa
canonical_readiness: not_ready_conversion_conflict
source_quality_score: 0.90
conversion_confidence_score: 0.25
evidence_quantity_score: 0.68
agreement_score: 0.38
identity_confidence_score: 0.82
claim_probability: 0.88
relevance_level: direct
relevance_confidence: 0.96
next_action: reconcile_assigned_conversion_and_chunk_with_source_image_before_canonical_promotion
---

# Proof Review: Child-Mother Relationship

## Blockers

- The assigned converted file and chunk materially conflict with the staged relationship. They transcribe entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, and mother `Concepcion de la Cruz`, while the staged draft and source packet describe the visible source image as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar`, and mother `Juana Arriagada de Pulgar`.
- Because the claim depends on a source-image reread rather than the assigned converted text, this relationship should remain on hold for conversion QA before canonical promotion.
- Canonical identity handling remains unresolved for the mother name form `Juana Arriagada de Pulgar`; do not normalize or merge that name to a canonical identity from this review alone.

## Scores

| Factor | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.90 | The page image is a civil birth register and directly names parents in the child row, but the review is constrained by the transcription mismatch. |
| conversion_confidence_score | 0.25 | The assigned converted Markdown and chunk do not support the staged Pulgar/Arriagada relationship and instead describe a different entry 172. |
| evidence_quantity_score | 0.68 | One direct page image plus the staged source packet support the relationship; no independent corroborating source was reviewed. |
| agreement_score | 0.38 | The image and source packet agree with the staged draft, but the assigned conversion and chunk conflict on the child and mother fields. |
| identity_confidence_score | 0.82 | The visible row appears to tie the named child to the named mother in the parent column; identity risk remains for canonical linking and married-name style. |
| claim_probability | 0.88 | The mother-child relationship is likely as read from the image, but the derivative-text conflict prevents a higher proof judgment. |
| relevance_level | direct | A birth registration naming a child and mother is direct evidence for a child-mother relationship. |
| relevance_confidence | 0.96 | The staged draft, source packet, image, converted file, and chunk all point to entry 172/page 58 even though their transcriptions conflict. |
| canonical_readiness | not_ready_conversion_conflict | Hold for conversion QA; do not promote to canonical relationship folders until the assigned transcription/chunk is reconciled. |

## Evidence Strengths

- The visible source image for register page 58, entry 172 appears to show the child name `Jose del Carmen Segundo Pulgar Arriagada`.
- In the same visible entry row, the mother field appears to read `Juana Arriagada de Pulgar`.
- The source packet explicitly flags the conversion conflict and records the Pulgar/Arriagada mother-child reading from the source image.
- The relationship inference itself is not a multi-step relationship jump: the source is a birth register and the mother is named in the parent field for the child.

## Review Judgment

This relationship candidate has direct visible-source support, but the assigned conversion/chunk are materially unreliable for this entry. The proof should be treated as a high-probability image-supported claim on QA hold, not as canonically ready evidence.

There is no reviewed conflict in the visible source against the mother-child relationship itself. The blocking problem is provenance and transcription reliability: the workspace derivative text currently represents entry 172 as a different child and mother.

## Next Action

Send the source image, converted file, and chunk through targeted conversion QA for entry 172. After the assigned conversion/chunk are reconciled with the page image, re-review the child-mother relationship for scoped promotion using the recorded mother name or an already-established canonical identity mapping.
