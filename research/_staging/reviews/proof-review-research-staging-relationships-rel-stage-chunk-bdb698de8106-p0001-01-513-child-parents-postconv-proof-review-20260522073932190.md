---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260522073932190
task_id: proof-review:research/_staging/relationships/REL-STAGE-CHUNK-bdb698de8106-P0001-01-513-child-parents.md
staged_draft: research/_staging/relationships/REL-STAGE-CHUNK-bdb698de8106-P0001-01-513-child-parents.md
reviewed_source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md
reviewed_source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
reviewed_converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
reviewed_chunk_note: referenced staged chunk path unavailable; current nearby regenerated chunk reviewed only as derivative context
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 513 Child-Parents Relationship

## Blockers

- The staged draft claims a child-parent relationship for child `Isolina del Carmen Jose` with parents `Jose del Carmen Pulgar` and `Juana de Dios Amador de Pulgar`; the restored page image for entry 513 does not visibly support the child name `Isolina del Carmen Jose`.
- The restored image and current regenerated chunk indicate entry 513 is a masculine child record, with the child name appearing closer to `Pulgar ... / Jose Luis` than the staged child identity. This is a material identity conflict, not a minor spelling issue.
- The staged mother reading `Juana de Dios Amador de Pulgar` is not secure against the restored image/current conversion context, where the surname appears closer to `Amagada` or a similar reading. This requires conversion QA before any relationship linkage.
- The staged draft's referenced chunk path is unavailable: `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md`.
- The current available chunk for the same converted file has a different chunk id, `CHUNK-3d3ab761209f-P0001-01`, and materially disagrees with the staged draft on the child identity. It can help identify the conflict, but it does not validate the staged wording.
- Because the staged child identity is unsupported and the maternal surname is disputed, this relationship candidate is not ready for canonical use.

## Evidence Strengths

- The source is a civil birth register page for Los Anjeles/Los Angeles, La Laja, page 172, and entry 513 is visible.
- The record type is directly relevant to parentage because entry 513 has explicit printed fields for child name/sex and named father/mother.
- The father/declarant field in entry 513 visibly supports `Jose del Carmen Pulgar` or a close reading, with occupation and domicile details consistent across the source context.
- The source packet correctly warns of material conflict between the assigned staged/converted transcript layer and the restored image evidence.

## Scoring

- source_quality_score: 8/10
- conversion_confidence_score: 2/10
- evidence_quantity_score: 2/10
- agreement_score: 1/10
- identity_confidence_score: 1/10
- claim_probability: 0.05
- relevance_level: high
- relevance_confidence: 0.90
- canonical_readiness: hold_for_conversion_qa

## Judgment

Hold for conversion QA. The underlying register is a strong and relevant parentage source, but the relationship as staged depends on a child identity and maternal surname not supported by the restored image. The visible source can support review of a corrected entry 513 relationship after transcription is reconciled, but it does not support promoting this staged relationship.

## Next Action

Double-check entry 513 against the restored image and regenerate or revise the candidate after resolving the child name, sex, maternal surname, and current chunk reference. Do not promote this staged relationship to canonical relationship or person pages.
