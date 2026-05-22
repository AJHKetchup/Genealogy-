---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260522064444710
task_id: proof-review:research/_staging/relationships/REL-STAGE-CHUNK-bdb698de8106-P0001-01-513-child-parents.md
staged_draft: research/_staging/relationships/REL-STAGE-CHUNK-bdb698de8106-P0001-01-513-child-parents.md
reviewed_source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md
reviewed_source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
reviewed_converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 513 Child-Parents Relationship

## Blockers

- The staged draft claims child `Isolina del Carmen Jose` with parents `Jose del Carmen Pulgar` and `Juana de Dios Amador de Pulgar`, but the restored page image does not visibly support that child name for entry 513.
- The referenced chunk path in the staged draft and source packet is unavailable: `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md`.
- The available converted/chunk transcription and the source-packet QA notes materially disagree with the staged draft. The current derivative text for entry 513 reads a masculine child with Pulgar surname and given names closer to `Jose Luis`/similar, not `Isolina del Carmen Jose`.
- The father field is strongly relevant to `Jose del Carmen Pulgar`, but the mother field appears closer to `Juana de Dios Amagada/Amagada de Pulgar` in the conversion and image review notes, not the staged `Amador de Pulgar`. This surname difference blocks canonical linkage.
- Because the child identity is unsupported and the mother surname is uncertain/conflicting, the child-parent relationship as staged should not be promoted.

## Evidence Strengths

- The source is a civil birth register page for Los Anjeles/Los Angeles, La Laja, Chile, page 172, including entry 513.
- Entry 513 visibly contains a father field for `Jose del Carmen Pulgar` or a very close reading, with occupation and domicile details consistent across the page image and derivative transcription.
- The record is directly relevant to parentage because it is a birth registration with explicit father and mother columns.

## Scoring

- source_quality_score: 8/10
- conversion_confidence_score: 2/10
- evidence_quantity_score: 2/10
- agreement_score: 1/10
- identity_confidence_score: 1/10
- claim_probability: 0.10
- relevance_level: high
- relevance_confidence: 0.90
- canonical_readiness: hold_for_conversion_qa

## Judgment

Hold. The source type is strong, but the staged relationship depends on a child name and maternal surname not supported by the restored image or the available derivative transcription. Treat this as a conversion/transcription reconciliation problem before any relationship proof review or canonical promotion.

## Next Action

Send entry 513 through conversion QA with the restored image in view. Ask QA to resolve the child name, sex, maternal surname, and correct chunk reference before regenerating or revising relationship candidates. Do not promote this staged relationship as written.
