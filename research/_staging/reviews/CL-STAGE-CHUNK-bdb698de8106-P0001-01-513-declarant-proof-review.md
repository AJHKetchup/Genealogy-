---
type: proof_review
role: claim_reviewer
status: complete
worker: postconv-proof-review-20260522231355679
task_id: proof-review:research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-declarant.md
staged_draft: research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-513-declarant.md
source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
reviewed_at: 2026-05-22
source_quality_score: 0.86
conversion_confidence_score: 0.68
evidence_quantity_score: 0.78
agreement_score: 0.74
identity_confidence_score: 0.82
claim_probability: 0.86
relevance_level: high
relevance_confidence: 0.94
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 513 Declarant

## Blockers

- Canonical readiness is **hold_for_conversion_qa**. The staged draft and derivative transcript directly support the declarant claim, and the page image broadly agrees for the declarant column, but the source packet documents material image/transcript conflicts in the same entry, especially the child-name field. This row should not be promoted until conversion QA reconciles the entry-level transcription.
- The abbreviated declarant name `José del C. Pulgar` is probably the same person as the parent field `José del Carmen Pulgar`, but this review treats that as a high-confidence same-row identity judgment rather than a separate canonical identity merge.
- Do not replace the converted transcript with image-reviewed alternatives from the QA note. The image check is verification context only.

## Evidence Strengths

- The staged claim says `Jose del C. Pulgar` appeared as declarant for entry 513, as father, age 47, farmer, domiciled Calle Colon.
- The converted file and chunk transcribe entry 513's declarant column as `José del C. Pulgar`, `Padre`, `Edad. Cuarenta i siete Años`, `Prof. Agricultor`, and `Dom. Calle Colon`.
- Direct image review of the entry 513 declarant column visibly supports the same core reading: `José del C. Pulgar`, `Padre`, age `Cuarenta i siete Años`, profession `Agricultor`, domicile `Calle Colon`.
- The parent column in the same row gives the father as `José del Carmen Pulgar`, Chilean, farmer, domiciled Calle Colon, which agrees with the declarant being the father and supports the abbreviated middle-name reading.

## Scored Judgment

- `source_quality_score`: 0.86. Civil birth register image is an original/near-original register source for the event and declarant role, though image quality is uneven.
- `conversion_confidence_score`: 0.68. The declarant field is readable and corroborated visually, but conversion QA flags significant conflicts elsewhere in the same row/page.
- `evidence_quantity_score`: 0.78. One strong register entry supports the claim; no independent corroborating source was reviewed for this task.
- `agreement_score`: 0.74. Draft, converted text, chunk, and image agree on the narrow declarant fields, while the broader row has unresolved transcription conflicts.
- `identity_confidence_score`: 0.82. Same-row father/declarant details strongly support `José del C. Pulgar` as `José del Carmen Pulgar`; abbreviation and handwriting keep this below certain.
- `claim_probability`: 0.86. The claim is probably correct as a source-level appearance claim.
- `relevance_level`: high.
- `relevance_confidence`: 0.94. Declarant/father appearance in a civil birth registration is directly relevant to identity, residence, occupation, and family reconstruction.
- `canonical_readiness`: hold_for_conversion_qa.

## Next Action

Keep the staged claim on hold pending conversion QA for entry 513. After QA resolves the row-level transcription conflict, this specific declarant appearance claim can be reconsidered for promotion with a high probability score if the declarant column remains unchanged.
