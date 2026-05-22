---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/relationships/REL-STAGE-CHUNK-bdb698de8106-P0001-01-513-child-parents.md
staged_draft: research/_staging/relationships/REL-STAGE-CHUNK-bdb698de8106-P0001-01-513-child-parents.md
reviewer: postconv-proof-review-20260522062447806
review_date: 2026-05-22
canonical_readiness: hold
---

# Proof Review: Entry 513 Child-Parents Relationship

## Blockers

- The staged child endpoint `Isolina del Carmen Jose` is not literally supported by the restored page image for entry 513. The visible record 513 child field appears closer to a Pulgar/Jose Luis-style reading and the sex field reads `Masculino`; this conflicts with the staged `Isolina del Carmen Jose` endpoint.
- The staged literal-support block does not match the currently referenced converted file or the available replacement chunk. Both read record 513 child as `Tulio Cesar Luis Jose`/`Tulio Cesar Luis José`, not `Isolina del Carmen Jose`.
- The staged mother endpoint `Juana de Dios Amador de Pulgar` is not conversion-stable. The referenced converted file and available `page-0172-chunk-01.md` read `Juana de Dios Amagada de Pulgar`; the page image supports the given names and `de Pulgar`, but the intervening surname is difficult and should remain under conversion QA.
- The staged draft references `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md`, but that exact chunk file is unavailable. A nearby `page-0172-chunk-01.md` exists in the same chunk folder, and a separate `page-0001-chunk-01.md` exists in another folder, but the referenced path itself cannot be verified.
- The source packet is already marked `hold_for_conversion_qa` and records material conflicts between derivative transcript layers and the page image for this page. This directly affects the relationship because the child identity and mother's surname are disputed.

## Scores

- source_quality_score: 0.90
- conversion_confidence_score: 0.30
- evidence_quantity_score: 0.60
- agreement_score: 0.15
- identity_confidence_score: 0.20
- claim_probability: 0.25
- relevance_level: high
- relevance_confidence: 0.92
- canonical_readiness: hold

## Evidence Strengths

- The underlying source is a Chilean civil birth register, which is direct, high-quality evidence for parent-child relationships when the entry is accurately transcribed.
- Record 513 clearly has father and mother columns, so the relationship type is relevant and not an inferential jump from unrelated text.
- The father field is comparatively strong: the page image, converted file, chunk text, and declarant field all support `José del Carmen Pulgar` or the abbreviated declarant form `José del C. Pulgar`, with role `Padre`.
- The mother field supports a person named `Juana de Dios ... de Pulgar`, but the exact surname between those elements is unresolved and does not support the staged `Amador` reading with enough confidence.

## Review Judgment

This staged relationship is not canonically ready. The source is relevant, and a child-parent relationship is present in record 513, but the staged endpoints are not safely supported. The child name in the staged draft conflicts with the restored page image and with the derivative transcript currently available for verification. The mother surname also conflicts between the staged draft and the available conversion/chunk layer.

Treat this as a hold/revise item, not a promotable relationship. The strongest recoverable element is that `José del Carmen Pulgar` appears as father/declarant for record 513, but this staged draft cannot safely promote him and `Juana de Dios Amador de Pulgar` as parents of `Isolina del Carmen Jose`.

## Next Action

Run or complete conversion QA for record 513 against the restored page image, focused on the child name, sex, mother's surname, and correct chunk path/hash. After QA, revise the staged relationship to the visibly supported child and parent readings, or retire this draft if it was generated from an obsolete or incorrect derivative transcript.
