---
type: conflict_candidate
status: draft
task_id: evidence-extraction:CHUNK-3d3ab761209f-P0001-01
source_packet: "research/_staging/source-packets/CHUNK-3d3ab761209f-P0001-01-source-packet.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png"
converted_file: "raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md"
chunk: "raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-3d3ab761209f-P0001-01"
page_reference: "image page 1; register page 172; entries 513-515"
confidence: medium
promotion_recommendation: hold_for_conversion_qa
---

# Conflict And QA Candidates: Birth Register Entries 513-515

## Shared Source Reference

- Source path: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png`
- Converted file: `raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md`
- Chunk/page reference: `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md`, `CHUNK-3d3ab761209f-P0001-01`, image page 1, register page 172

## Image-Reviewed Conflict Notes

| Candidate id | Candidate issue | Literal support | Conversion confidence / QA concern | Uncertainty | Promotion recommendation |
| --- | --- | --- | --- | --- | --- |
| conflict-514-father-unknown | Entry 514 states that the father was unknown in this registration. | Image-visible father field and assigned chunk: `Nombre del padre. Se ignora`. | The assembled converted file conflicts by placing `Mercedes Riquelme` in the father field; the image supports the assigned chunk for this field. | This is negative evidence from this registration only. It does not prove biological paternity was unknowable in all sources. | `do_not_promote` as a tree relationship; keep as a negative-evidence/conflict note after proof review. |
| qa-514-witness-surname | Entry 514 first witness surname is still uncertain. | Assigned chunk: `Benjamin Utiera`; converted file: `Benjamin Utrosa`; image shows `Benjamin Ut...` but the final letters are not secure at this extraction resolution. | Keep both derivative readings as competing transcript evidence. | Do not create or merge a witness identity until a targeted crop is reviewed. | `hold_for_conversion_qa` |
| qa-514-street | Entry 514 street/place reading remains uncertain. | Assigned chunk: `Calle Sanegueso`; current converted file: `Calle Saneguin`; image suggests a `Calle San...` reading but does not fully settle the street form here. | Preserve as a place-reading QA limitation. | Do not normalize to a modern street or attach geocoding from this reading alone. | `hold_for_conversion_qa` |
| qa-515-neira-emendation | Entry 515 has an image-visible surname emendation note. | Image and assigned chunk: `Neira=emendado=` and `vale=`. | Supports that `Neira` was corrected or validated in the entry, but the converted file conflicts on the child/father surname by reading `Leiva`. | The visible note supports a source-context note; it does not by itself resolve all cropped lower-row details. | `hold_for_conversion_qa` pending proof review of the targeted entry 515 crop. |
| qa-515-bottom-crop | The available image cuts off the lower portion of entry 515. | Image shows upper/middle portions of entry 515 but not the complete lower mother/domicile area. | The assigned chunk supplies `Carmen Ulloa`, but the image available in this pass does not visibly confirm the full mother field. | Keep mother relationship and mother vital/residence claims on hold unless a complete image or correction note confirms them. | `hold_for_conversion_qa` |

## Material Derivative-Transcript Conflicts

- Entry 513 child: assigned chunk has `Pulgar Amagada / Jose Luis`; current converted file has `Isolina del Carmen / Jose`. The image supports a `Pulgar Ama...` surname line and a given-name line beginning `Jose ...`, but does not securely support `Jose Luis`; the name should remain held.
- Entry 513 birth: assigned chunk has 26 June 1889 at 4:30 p.m.; converted file has 22 June 1889 at 4:20 p.m.; image review appears to support 22 June 1889 and likely 4:30 p.m., but the time phrase needs targeted QA.
- Entry 513 mother: assigned chunk has `Juana de Dios Amagada de Pulgar`; converted file has `Juana de Dios Amador de Pulgar`; image supports the Pulgar row but the maternal surname remains a QA-sensitive reading.
- Entry 514 child: assigned chunk has `Riquelme Aviles / Juan Bautista`; current converted file has `Riquelme Juan Teodoro`; source image supports `Riquelme / Juan Bautista` and does not visibly support `Aviles`.
- Entry 514 father: assigned chunk and image have `Se ignora`; converted file places `Mercedes Riquelme` in the father field.
- Entry 515 child and parents: assigned chunk has `Neira Ulloa / Laura de la Cruz`, father `Pedro Pablo Neira`, mother `Carmen Ulloa`; current converted file has child `Rosa Elvira del Carmen`, father `Pedro Pablo Leiva`, and no preserved mother name in the mother field. The image supports the `Neira=emendado= / vale=` note and the father area, but the lower mother area remains cropped/insufficiently visible for promotion.

## Promotion Recommendation

`hold_for_conversion_qa`: only the negative-evidence conflict for entry 514's father is currently strong enough to carry forward after proof review, and even that should be promoted as a conflict/negative-evidence note rather than a parent-child tree link.
