---
type: staged_identity_candidates
task_id: evidence-extraction:CHUNK-3d3ab761209f-P0001-01
chunk_id: CHUNK-3d3ab761209f-P0001-01
status: draft
promotion_recommendation: hold_for_conversion_qa
---

# Identity Candidates: Birth Register Entries 513-515

## Shared Source Reference

- Source path: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png`
- Converted file: `raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md`
- Chunk/page reference: `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md`, CHUNK-3d3ab761209f-P0001-01, page range 1-1, register page 172
- Conversion confidence / QA concern: mixed. The assigned chunk, assembled converted Markdown, and image-reviewed evidence disagree on identity-bearing fields for entries 513-515. Treat these as identity candidates only until conversion QA resolves the derivative-transcript conflict.

| Candidate id | Identity candidate | Literal support | Uncertainty | Promotion recommendation |
| --- | --- | --- | --- | --- |
| id-513-child | Create/reconcile person: entry 513 Pulgar Amagada child, male, born in entry 513 at Calle Colon, Los Anjeles registration district. | Source image supports a `Pulgar Ama...` surname line and sex `Masculino`; assigned chunk reads `Jose Luis`; current converted file conflicts with `Isolina del Carmen / Jose`. | Given-name parsing and exact birth date/time should wait for targeted image QA. | `hold_for_conversion_qa` |
| id-513-father | Create/reconcile person: Jose del Carmen Pulgar / Jose del C. Pulgar, Chilean agriculturist, age 47 in July 1889, domiciled Calle Colon. | "**Nombre del padre.**<br>José del Carmen Pulgar"; "José del C. Pulgar<br>Padre"; "**Edad.** Cuarenta i siete Años" | Same-entry abbreviation supports but does not independently prove broader identity matches. | `hold_for_conversion_qa` |
| id-513-mother | Create/reconcile person: Juana de Dios Amagada de Pulgar, Chilean, domiciled Calle Colon. | Assigned chunk: "**Nombre de la madre.**<br>Juana de Dios Amagada de Pulgar"; converted file conflicts with `Amador`. | Maternal surname and married-name form remain QA-sensitive. | `hold_for_conversion_qa` |
| id-514-child | Create/reconcile person: Juan Bautista Riquelme, male, born 23 June 1889, in the entry 514 place field. | Source image supports `Riquelme / Juan Bautista`; assigned chunk adds `Aviles`; current converted file conflicts with `Riquelme Juan Teodoro`. | Street name and child surname/given-name structure require conversion QA. | `hold_for_conversion_qa` |
| id-514-mother | Create/reconcile person: Mercedes Riquelme, Chilean seamstress, age 21 in July 1889. | "**Nombre de la madre.**<br>Mercedes Riquelme"; "Mercedes Riquelme<br>Madre"; "**Edad.** Veintiun Años" | Same-entry mother/declarant identity is likely but should be reviewed; street name has QA note. | `hold_for_conversion_qa` |
| id-514-witness-1 | Possible witness identity: Benjamin Utiera. | "**Por los testigos:**<br>Benjamin Utiera" | Surname is difficult and conflicts with the current converted-file reading `Benjamin Utrosa`. | `hold_for_conversion_qa` |
| id-514-witness-2 | Possible witness identity: Ignacio Soto. | "**Por los testigos:**<br>Benjamin Utiera<br>Ignacio Soto" | Witness-only mention; no age/residence, and the current converted file conflicts with `Ignacio Jara`. | `hold_for_conversion_qa` |
| id-515-child | Create/reconcile person: Laura de la Cruz Neira Ulloa, female, born 18 July 1889, Calle Santiago. | Assigned chunk: "**Nombre.**<br>Neira Ulloa<br>Laura de la Cruz"; converted file conflicts with `Rosa Elvira del Carmen`; image shows `Neira=emendado= / vale=` note. | Entry includes emendation note and lower crop limitation; check image before finalizing surname and birth facts. | `hold_for_conversion_qa` |
| id-515-father | Create/reconcile person: Pedro Pablo Neira, Chilean agriculturist, age 26 in July 1889, domiciled Santiago. | Assigned chunk: "**Nombre del padre.**<br>Pedro Pablo Neira"; converted file conflicts with `Pedro Pablo Leiva`; image supports the `Neira` emendation context. | Same-entry father/declarant identity is likely but should be reviewed. | `hold_for_conversion_qa` |
| id-515-mother | Create/reconcile person: Carmen Ulloa, Chilean, domiciled Santiago. | Assigned chunk: "**Nombre de la madre.**<br>Carmen Ulloa"; current converted file does not preserve a mother name in the entry 515 mother field. | Lower-row crop prevents confident image confirmation in this pass. | `hold_for_conversion_qa` |
| id-515-witnesses | Possible witness identities: Rosendo Ramirez H.; Santiago Perez. | "**Por los testigos:**<br>Rosendo Ramirez H.<br>Santiago Perez" | Witness-only mentions; the current converted file conflicts with `Jose D. Ramirez H.` and `Santiago Fuentes`. | `hold_for_conversion_qa` |
