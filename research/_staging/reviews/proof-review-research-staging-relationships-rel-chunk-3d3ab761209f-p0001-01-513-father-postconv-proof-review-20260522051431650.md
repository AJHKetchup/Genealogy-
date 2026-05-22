---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/relationships/rel-chunk-3d3ab761209f-p0001-01-513-father.md
staged_draft: research/_staging/relationships/rel-chunk-3d3ab761209f-p0001-01-513-father.md
reviewer: postconv-proof-review-20260522051431650
review_date: 2026-05-22
canonical_readiness: hold
---

# Proof Review: Entry 513 Father Relationship

## Blockers

- The child identity in the staged draft is not ready for canonical use. The staged draft and assigned chunk identify the child as `Jose Luis Pulgar Amagada` / `Pulgar Amagada José Luis`, while the converted file gives a materially different child-name reading for entry 513. The visible source image appears to support the father field but does not resolve the exact child full-name reading cleanly enough for promotion in this review note.
- The source packet already marks this source `hold_for_conversion_qa` because the assigned chunk and converted file disagree materially on names, dates, places, parent fields, and official signature for entries 513-515. That conflict directly affects this relationship candidate because the child endpoint depends on the disputed entry 513 transcription.
- The mother surname is also unstable across the extraction context: the assigned chunk gives `Juana de Dios Amagada de Pulgar`, the converted file gives `Juana de Dios Amador de Pulgar`, and the image reading requires dedicated conversion QA before normalizing the child's surname.
- Do not merge the abbreviated declarant `José del C. Pulgar` with the named father beyond a provisional review finding until the entry 513 transcription is reconciled. The abbreviation is consistent with the father field, but the draft itself flagged this as an uncertainty.

## Scores

- source_quality_score: 0.90
- conversion_confidence_score: 0.52
- evidence_quantity_score: 0.66
- agreement_score: 0.48
- identity_confidence_score: 0.62
- claim_probability: 0.68
- relevance_level: high
- relevance_confidence: 0.88
- canonical_readiness: hold

## Evidence Strengths

- The evidence is a civil birth-register entry, a high-value source type for parent-child relationships when the transcription is stable.
- Entry 513's father field is visibly and consistently represented as `José del Carmen Pulgar` in both the assigned chunk and converted file, and the source image visibly supports `José del Carmen Pulgar` in the father column.
- The declarant field in the chunk and converted file reads `José del C. Pulgar` followed by `Padre`; the source image visibly supports a father-declarant entry matching the same name pattern.
- The claimed relationship type is directly relevant to the record: a named father in a birth registration is direct evidence for a parent-child relationship, not an inferred collateral relationship.

## Review Judgment

The father side of the claim is well supported: entry 513 identifies `José del Carmen Pulgar` as father, and the declarant appears to be the same man abbreviated as `José del C. Pulgar` with the role `Padre`.

The relationship candidate is still not canonically ready because the child endpoint is not stable. The staged draft's child name and surname are based on the assigned chunk, while the converted file supplies a conflicting child-name reading, and the visible image does not provide a sufficiently clean resolution within this proof-review task. The correct posture is hold/revise, not promotion.

## Next Action

Run conversion QA on entry 513 against the source image, focusing on the child name/surname, mother's surname, birth date, and whether the child should be represented as `José Luis Pulgar Amagada` or revised to the visibly supported reading. After that QA pass, revise this staged relationship if the child identity changes; otherwise retain `José del Carmen Pulgar` as the father only with the reconciled child name.
