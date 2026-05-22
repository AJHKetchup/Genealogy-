---
type: staged_relationship_candidates
task_id: evidence-extraction:CHUNK-3d3ab761209f-P0001-01
chunk_id: CHUNK-3d3ab761209f-P0001-01
status: draft
promotion_recommendation: promote_after_identity_review
---

# Relationship Candidates: Birth Register Entries 513-515

## Shared Source Reference

- Source path: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png`
- Converted file: `raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md`
- Chunk/page reference: `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md`, CHUNK-3d3ab761209f-P0001-01, page range 1-1, register page 172
- Conversion confidence / QA concern: high for principal names and parent fields; no parent-name QA issue noted for these entries.

| Candidate id | Relationship candidate | Literal support | Uncertainty | Promotion recommendation |
| --- | --- | --- | --- | --- |
| rel-513-father | Jose del Carmen Pulgar is father of Jose Luis Pulgar Amagada. | Child: "**Nombre.** Pulgar Amagada<br>José Luis"; parent field: "**Nombre del padre.**<br>José del Carmen Pulgar"; declarant: "José del C. Pulgar<br>Padre" | The declarant abbreviation "Jose del C." should be reviewed before using it as additional identity support; father field itself is direct. | Promote after identity review. |
| rel-513-mother | Juana de Dios Amagada de Pulgar is mother of Jose Luis Pulgar Amagada. | Child: "**Nombre.** Pulgar Amagada<br>José Luis"; parent field: "**Nombre de la madre.**<br>Juana de Dios Amagada de Pulgar" | Married surname form may obscure birth surname; do not merge without corroboration. | Promote after identity review. |
| rel-514-mother | Mercedes Riquelme is mother of Juan Bautista Riquelme Aviles. | Child: "**Nombre.**<br>Riquelme Aviles<br>Juan Bautista"; parent field: "**Nombre de la madre.**<br>Mercedes Riquelme<br>Pidió se consignara su nombre"; declarant: "Mercedes Riquelme<br>Madre" | Direct mother relationship; note the father is recorded as unknown. | Promote after identity review. |
| rel-515-father | Pedro Pablo Neira is father of Laura de la Cruz Neira Ulloa. | Child: "**Nombre.**<br>Neira Ulloa<br>Laura de la Cruz"; parent field: "**Nombre del padre.**<br>Pedro Pablo Neira"; declarant: "Pedro Pablo Neira<br>Padre" | Entry has an emendation note for "Neira"; verify image before final surname normalization. | Promote after identity review and image check of emendation. |
| rel-515-mother | Carmen Ulloa is mother of Laura de la Cruz Neira Ulloa. | Child: "**Nombre.**<br>Neira Ulloa<br>Laura de la Cruz"; parent field: "**Nombre de la madre.**<br>Carmen Ulloa" | Direct mother relationship; identity merge still requires review. | Promote after identity review. |

## Non-relationship Note

Record 514 states "**Nombre del padre.**<br>Se ignora". This should be treated as an unknown father statement, not as a relationship candidate.
