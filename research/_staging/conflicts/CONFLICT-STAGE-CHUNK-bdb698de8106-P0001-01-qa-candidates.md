---
type: conflict_candidates
status: draft
task_id: evidence-extraction:CHUNK-bdb698de8106-P0001-01
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
chunk_id: CHUNK-bdb698de8106-P0001-01
page_reference: page 1; register page 172
promotion_recommendation: hold_for_conversion_qa
---

# Conflict And QA Candidates

| Candidate | Literal support | Conversion confidence / QA concern | Uncertainty | Promotion recommendation |
| --- | --- | --- | --- | --- |
| Entry 513 child name/sex tension | `Isolina del Carmen José`; `Sexo. Masculino` | Medium. | Could be a transcription, reading-order, or name-structure issue. | Hold for conversion QA. |
| Entry 514 street spelling | `Calle Saneguin`; conversion note says spelling is uncertain and may be `Sanequin` or similar. | Medium. | Place authority should not be created from this spelling yet. | Hold for conversion QA. |
| Entry 514 mother's spouse clue vs named father | Father: `Belisario Riquelme`; declarant: `Mercedes Riquelme ... Esposa de Juan Soler`. | Medium-high. | Juan Soler is not named as father in this entry; avoid parentage inference. | Promote only as an identity/spouse clue after review. |
| Entry 515 missing fields | `Sexo.` blank; `Lugar.` blank; `Nombre de la madre.` blank. | Medium. | Do not infer sex, birthplace, or mother. | Do not promote missing-field inferences. |
