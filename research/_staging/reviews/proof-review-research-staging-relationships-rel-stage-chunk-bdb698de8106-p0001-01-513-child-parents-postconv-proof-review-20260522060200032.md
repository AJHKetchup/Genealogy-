---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/relationships/REL-STAGE-CHUNK-bdb698de8106-P0001-01-513-child-parents.md
staged_draft: research/_staging/relationships/REL-STAGE-CHUNK-bdb698de8106-P0001-01-513-child-parents.md
reviewer: postconv-proof-review-20260522060200032
review_date: 2026-05-22
canonical_readiness: hold
---

# Proof Review: Entry 513 Child-Parents Relationship

## Blockers

- The staged child endpoint `Isolina del Carmen Jose` is not supported by the currently referenced converted file or by the available chunk variants checked for entry 513. The converted file reads `Tulio Cesar Luis José`; one available chunk variant reads `Pulgar Amagada / José Luis`; the source packet says targeted image review appears closer to `Pulgar ... / José Luis` and explicitly not the converted `Isolina del Carmen José`.
- The staged mother endpoint `Juana de Dios Amador de Pulgar` is unstable. The converted file and available chunk variants checked in this review read `Juana de Dios Amagada de Pulgar`, while the source packet flags the mother surname as needing conversion QA.
- The staged draft references `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md`, but that exact path is unavailable. A nearby `page-0172-chunk-01.md` exists for the same chunk folder and a separate `page-0001-chunk-01.md` exists in a different chunk folder, but they do not agree on the entry 513 child reading.
- The source packet is already marked `hold_for_conversion_qa` because image-reviewed evidence materially conflicts with derivative transcripts for entries 513-515. This directly affects the relationship claim because both the child identity and mother-name reading are disputed.
- Do not promote or normalize this relationship into canonical files until conversion QA reconciles the source image, converted file, and chunk layer.

## Scores

- source_quality_score: 0.90
- conversion_confidence_score: 0.35
- evidence_quantity_score: 0.62
- agreement_score: 0.18
- identity_confidence_score: 0.25
- claim_probability: 0.30
- relevance_level: high
- relevance_confidence: 0.90
- canonical_readiness: hold

## Evidence Strengths

- The source type is a Chilean civil birth register, which is generally strong direct evidence for child-parent relationships when the entry transcription is stable.
- The father field is relatively consistent across the checked derivative layers for entry 513 as `José del Carmen Pulgar`, and the declarant field also gives `José del C. Pulgar` with role `Padre`.
- The record context is directly relevant: entry 513 is a birth registration with explicit father and mother columns, so the relationship type is not a relationship jump when the child and parent names are reliably transcribed.

## Review Judgment

This staged relationship is not canonically ready. The relationship concept may be present in entry 513, but the staged draft's exact child-parent statement is not presently supported: the child name in the staged draft conflicts with both checked derivative transcripts and with the source packet's image-review note, and the mother's surname is not conversion-stable.

Treat this as a hold/revise item. The father `José del Carmen Pulgar` is the strongest element, but it cannot safely be promoted as parent of `Isolina del Carmen Jose` from this staged draft because the child endpoint appears wrong or at least unreconciled.

## Next Action

Run conversion QA on entry 513 against the page image, focused on the child name, sex, birth date, mother's surname, and the correct chunk path/hash for this staged draft. After QA, revise the staged relationship to the visibly supported child and parent readings, or retire this staged draft if it was generated from the wrong derivative transcript.
