---
type: conflict_candidates
status: draft
task_id: evidence-extraction:CHUNK-d6a12b291d94-P0172-01
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-d6a12b291d94-P0172-01-los-angeles-birth-register-1889-page-172.md
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md
chunk_id: CHUNK-d6a12b291d94-P0172-01
page_reference: page 172; entries 513-515
promotion_recommendation: hold_for_conversion_qa
---

# Conflict And QA Candidates

## Literal Support

See the table below for the exact text behind each QA candidate.

## Conversion Confidence / QA Concern

The converted chunk reports complete transcription and no uncertainty. Proof review adds one independent image-review finding: entry 515 is cropped in the available PNG before the mother field can be checked.

## Uncertainty

Uncertainty is mostly normal proof-review risk for names, sparse fields, and role interpretation, except entry 515 where there is a conversion-QA blocker caused by incomplete visible source evidence.

| Candidate | Literal support | Conversion confidence / QA concern | Uncertainty | Promotion recommendation |
| --- | --- | --- | --- | --- |
| Archaic spellings in heading | `Rejistro`, `Circunscripcion`, `Los Anjeles`, `i`. | High within the converted chunk. | Preserve as literal spellings; normalize only in interpreted place labels. | Promote after review. |
| Entry 513 maternal surname spelling | `Juana de Dios Amagada de Pulgar`. | Medium-high within the converted chunk. | Surname should be proof-read before canonical identity promotion. | Promote after review. |
| Entry 514 father has blank attributes | `Nombre del padre. Belisario Riquelme`; `Nac. Prof.`; `Domicilio`. | Medium-high for the name, blank for attributes. | Do not infer nationality, profession, or residence for Belisario Riquelme from this entry. | Promote after review. |
| Entry 514 spouse clue vs father field | `Mercedes Riquelme ... Esposa de Juan Soler`; father field names `Belisario Riquelme`. | High within the converted chunk. | Juan Soler is spouse of declarant, not stated as the child's father in this record. | Promote after review. |
| Entry 515 cropped lower row | Converted support says `Nombre. Rosa Elvira del Carmen`, `Nombre del padre. Pedro Pablo Leiva`, and `Nombre de la madre. Carmen Fuentes`. | The source image visibly supports the entry context and appears to support the father/declarant field, but the mother field is below the visible cropped area. | Preserve disagreement between derivative transcript and image-reviewed evidence; do not promote `Carmen Fuentes` or the combined child-parents relationship until complete-row QA. | Hold for conversion QA. |
| Witness identity only | `Benjamin Utria`, `Ignacio Jara`, `Jose D. Ramirez`, `Santiago Fuentes`. | Medium-high within the converted chunk. | Witness names are not enough for canonical identity merges. | Do not promote. |
| Official signature | `Emilio Lininger O. del R. C.` appears for all entries. | Medium-high within the converted chunk. | Treat as official attribution, not a family relationship. | Do not promote. |
