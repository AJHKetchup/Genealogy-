---
type: conflict_candidates
status: draft
task_id: evidence-extraction:CHUNK-bdb698de8106-P0001-01
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
source_sha256: 05d0627a58615e91315e1e9e2da567034b4f324eb0179240e0f4d5cf985e3545
source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
chunk_id: CHUNK-bdb698de8106-P0001-01
page_reference: page 1; register page 172
confidence: low
promotion_recommendation: hold_for_conversion_qa
---

# Conflict And QA Candidates

## Shared Source Reference

- Source path: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png`
- Converted file: `raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md`
- Chunk/page reference: `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md`, `CHUNK-bdb698de8106-P0001-01`, page 1, register page 172

| Candidate | Literal support | Conversion confidence / QA concern | Uncertainty | Promotion recommendation |
| --- | --- | --- | --- | --- |
| Heading jurisdiction | Converted/chunk text reads `Los Anjeles`, `La Laja`; image review supports these readings. | Medium-high. | Preserve archaic spelling; do not modernize to `Los Ángeles` in literal support. | Hold packet for conversion QA because other rows conflict. |
| Entry 513 child name/sex conflict | Converted text reads `Isolina del Carmen José`; image appears to begin with `Pulgar...` and end with a `José` line; sex `Masculino` is visible. | Low for converted child-name reading. | This is a material identity conflict, not only a gender/name-order tension. The image note is not yet a full replacement transcription. | Hold for conversion QA. |
| Entry 513 birth-event subject conflict | Converted text reads `El mismo veinte dos ... a las cuatro de la mañana`; `Lugar. Calle Colon`. Proof review asks QA to reconcile child identity, sex, birth date, birth time, and place. | Low to medium. `Calle Colon` has row support, but the subject identity is unresolved. | Retain only as a row-level staged claim until the child identity is settled. | Hold for conversion QA. |
| Entry 513 mother surname conflict | Converted text reads `Juana de Dios Amador de Pulgar`; proof-review/image notes preserve possible `Juana de Dios Amagada de Pulgar`. | Low. Surname choice affects the parent relationship and identity matching. | Do not normalize to either surname before image QA. | Hold for conversion QA. |
| Entry 513 declarant profession conflict | Converted text reads `Prof. Agricultor`; proof review asks QA to reconcile `Agricultor` versus `Jornalero`. | Medium. Name, role, age, and domicile are stronger than the profession reading. | Keep the complete declarant claim staged until profession and row conflicts are reconciled. | Hold for conversion QA. |
| Entry 514 child name conflict | Converted text reads `Riquelme Juan Teodoro`; image appears closer to `Riquelme / Juan Bautista`. | Low for converted name reading. | Do not create a canonical person from either name until image QA is resolved. | Hold for conversion QA. |
| Entry 514 father conflict | Converted text reads `Nombre del padre. Belisario Riquelme`; image appears to read `Se ignora` in the father field. | Low for converted father claim. | Treat `Belisario Riquelme` as unsupported by the visible image for this bdb packet. | Hold for conversion QA; do not promote father relationship. |
| Entry 514 witness and street readings | Converted text reads witnesses `Benjamin Utrosa`, `Ignacio Jara` and `Calle Saneguin`; image appears to support `Benjamin Utrosa`/similar and `Ignacio Jara`, with street closer to `Calle San...`/`Calle Sanegueso`. | Medium-low. | Witness surname and street spelling remain paleographically uncertain. | Hold for conversion QA. |
| Official signature | Converted text reads `Emilio Lininger / O. del R. C.`; image is broadly consistent with `Emilio Lininger` or similar but difficult. | Medium. | Do not use as an official-name authority without proof review. | Hold for conversion QA. |
| Entry 515 completeness and identity conflict | Converted text presents entry 515 as complete enough for `Rosa Elvira del Carmen` and `Pedro Pablo Leiva`; image is bottom-cropped and appears to show `Rosa Elvira` followed by an unresolved `Laura de Car...`/`Laura de la Cruz...` line, with father/declarant surname closer to `Neira` than `Leiva`. | Low for converted entry-515 identity readings. | Entry 515 is partial in the source image; missing lower text may contain material data. | Hold for conversion QA; do not promote entry 515 claims. |

## Promotion Recommendation

Preserve these as staged conflict candidates only. No canonical wiki pages should be edited from this packet, and no child identity or parent-child tree link from entries 513-515 should flow forward until conversion QA stabilizes the source text.
