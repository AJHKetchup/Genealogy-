---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/relationships/REL-STAGE-CHUNK-bdb698de8106-P0001-01-513-child-parents.md
staged_draft: research/_staging/relationships/REL-STAGE-CHUNK-bdb698de8106-P0001-01-513-child-parents.md
reviewed_source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md
reviewed_converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
reviewed_chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
reviewed_source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
source_quality_score: 0.86
conversion_confidence_score: 0.28
evidence_quantity_score: 0.42
agreement_score: 0.18
identity_confidence_score: 0.22
claim_probability: 0.16
relevance_level: direct_but_conflicted
relevance_confidence: 0.94
canonical_readiness: hold_for_conversion_qa
reviewed_at: 2026-05-22T08:36:55Z
---

# Proof Review: Entry 513 Child-Parents Relationship

## Blockers

- The staged child endpoint `Isolina del Carmen Jose` is not supported by the restored source image for entry 513. The visible entry is a masculine record and the child-name area appears closer to a Pulgar/Jose reading than to `Isolina del Carmen Jose`.
- The staged literal-support block conflicts with the referenced converted file, which reads entry 513 as `Isidoro del Carmen Diaz`, and with the source packet image-QA note, which says the image appears closer to `Pulgar ... / José Luis`.
- The staged mother endpoint `Juana de Dios Amador de Pulgar` is not conversion-stable. The restored image supports `Juana de Dios ... de Pulgar`, but the intervening surname is difficult; the source packet and chunk variants record disagreement between `Amador` and `Amagada`-style readings.
- The staged draft's cited chunk path `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md` is unavailable in the workspace. A nearby chunk exists as `page-0172-chunk-01.md`, but this review does not treat the missing cited chunk as resolved.
- Because the child identity is the relationship subject, the parent relationship as written cannot be promoted even though parts of the parent fields are relevant.

## Evidence Strengths

- The restored source image is a direct civil birth-register page for register page 172 and entry 513, so the source type is strong for birth and parentage if the transcription layer is reconciled.
- The father field is comparatively strong: the restored image visibly supports `José del Carmen Pulgar` or a very close reading, and the declarant field also names `José del C. Pulgar` with role `Padre`.
- The mother field is relevant and partially supported: the image shows `Juana de Dios ... de Pulgar`, with domicile and nationality lines below. The exact surname remains too uncertain for canonical use from this staged draft.
- The source packet appropriately flags material derivative-transcript conflicts and recommends holding for conversion QA.

## Scored Judgment

- `source_quality_score`: 0.86. Direct civil register image, but page condition and handwriting limit some fields.
- `conversion_confidence_score`: 0.28. The derivative layers materially disagree on child name, mother surname, and some associated details.
- `evidence_quantity_score`: 0.42. One direct record is available, but the relationship endpoint depends on unresolved transcription.
- `agreement_score`: 0.18. Staged draft, converted file, source packet QA, and visible image do not agree on the child identity.
- `identity_confidence_score`: 0.22. The father is likely correctly identified, but the claimed child identity and exact mother surname are not secure.
- `claim_probability`: 0.16. Low probability that the relationship as written, with child `Isolina del Carmen Jose`, is correct.
- `relevance_level`: direct_but_conflicted.
- `relevance_confidence`: 0.94. The reviewed evidence is directly about entry 513, even though it conflicts with the staged claim.
- `canonical_readiness`: hold_for_conversion_qa.

## Next Action

Hold this staged relationship for conversion QA. Reconcile the entry 513 child-name/sex reading and the mother surname directly against the restored image, then regenerate or revise the staged relationship before any promotion to canonical relationship, claim, person, or family pages.
