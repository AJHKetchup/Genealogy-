---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260522071255904
task_id: proof-review:research/_staging/relationships/REL-STAGE-CHUNK-bdb698de8106-P0001-01-513-child-parents.md
staged_draft: research/_staging/relationships/REL-STAGE-CHUNK-bdb698de8106-P0001-01-513-child-parents.md
reviewed_source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md
reviewed_source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
reviewed_converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
reviewed_chunk_note: referenced staged chunk path unavailable; nearby regenerated chunk reviewed only as derivative context
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 513 Child-Parents Relationship

## Blockers

- The staged draft claims the child is `Isolina del Carmen Jose`, but the restored source image for entry 513 visibly shows a masculine child record and does not support that child name.
- The staged draft cites literal support for `Isolina del Carmen Jose` and `Juana de Dios Amador de Pulgar`; those readings are not supported by the restored page image reviewed for entry 513.
- The referenced chunk path in the staged draft and source packet is unavailable: `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md`.
- The available converted file and the nearby regenerated chunk disagree materially with the staged draft on the child identity. The derivative texts also conflict with each other in places, but both current image review and nearby chunk context point away from `Isolina del Carmen Jose`.
- The father field is relevant and appears to support `Jose del Carmen Pulgar` or a very close reading, but the mother surname appears closer to `Amagada/Amagada de Pulgar` in the available conversion context and visible image, not staged `Amador de Pulgar`.
- Because the claimed child identity and maternal surname are unsupported or conflicting, the child-parent relationship as staged is not ready for canonical use.

## Evidence Strengths

- The source is a Chilean civil birth register page for Los Anjeles/Los Angeles, La Laja, page 172, and it includes entry 513.
- Entry 513 is a direct birth-registration record with explicit columns for child name/sex, birth details, father, mother, declarant, identity confirmation, and registrar signature.
- The image visibly supports that the father/declarant is `Jose del Carmen Pulgar` or a close reading, with occupation `Agricultor` and domicile `Calle Colon`.
- The record type is highly relevant to parentage when the transcription is reliable, because it names parents in a birth-registration context.

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

Hold for conversion QA. The underlying source is strong and relevant, but the staged relationship is attached to an unsupported child identity and a disputed maternal surname. The restored page image does not justify promoting or revising this relationship into canonical files from the staged wording.

## Next Action

Run conversion QA on entry 513 with the restored image in view. Resolve the child name, sex, maternal surname, and current chunk reference, then regenerate or revise the relationship candidate before any canonical promotion.
