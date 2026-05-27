---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-3d3ab761209f-P0001-01
worker: postconv-evidence-extraction-20260527175853458
source_id: ca05d0627a-los-angeles-birth-register-1889-page-172-entry-513
title: "Los Angeles, Chile civil birth register, 1889, register page 172, entry 513"
source_type: civil_birth_register
record_type: birth_registration
source_path: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png"
source_sha256: "05d0627a58615e91315e1e9e2da567034b4f324eb0179240e0f4d5cf985e3545"
converted_file: "raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md"
converted_sha256: "3d3ab761209fb351dce29fd110518d75087aa04075890da5943aa4f9d82bf175"
chunk: "raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-3d3ab761209f-P0001-01"
chunk_manifest: "raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/manifest.json"
page_reference: "image page 1; register page 172; entry 513, with entries 514-515 as row-control context"
page_start: 1
page_end: 1
family_relevance: high
matched_family_terms:
  - Pulgar
conversion_confidence: low
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet Revision: Entry 513 Pulgar Birth Registration

## Person-First Focus

Entry 513 is relevant to the Pulgar family because both derivative transcriptions name `Jose del Carmen Pulgar` in the father field and `Jose del C. Pulgar` as the declarant/father. The record may support a Pulgar child identity, birth event, and parent-child relationship, but the identity-controlling readings remain blocked.

## Source And Chunk References

- Original source image path: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png`
- Converted file: `raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md`
- Chunk: `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md`
- Chunk id: `CHUNK-3d3ab761209f-P0001-01`
- Page reference: image page 1; register page 172; entry 513.

## Literal Support

Assigned chunk transcription for entry 513:

```text
513 | Julio veinte i dos de mil ochocientos ochenta i nueve | Nombre. Pulgar Amagada / Jose Luis | Sexo. Masculino
Fecha. Junio veinte i seis de mil ochocientos ochenta i nueve, a las cuatro i media de la tarde | Lugar. Calle Colon
Nombre del padre. Jose del Carmen Pulgar ... Agricultor ... Domicilio. Calle Colon
Nombre de la madre. Juana de Dios Amagada de Pulgar ... Labores de su sexo ... Domicilio. Calle Colon
Jose del C. Pulgar / Padre / Edad. Cuarenta i siete Anos / Prof. Agricultor / Dom. Calle Colon
```

Assembled converted Markdown for the same entry:

```text
513 | Julio veintidos de mil ochocientos ochenta i nueve | Nombre. Isolina del Carmen / Jose | Sexo. Masculino
Fecha. El mismo veinte dos de mil ochocientos ochenta i nueve, a las cuatro de la manana | Lugar. Calle Colon
Nombre del padre. Jose del Carmen Pulgar ... Agricultor ... Domicilio. Calle Colon
Nombre de la madre. Juana de Dios Amador de Pulgar ... Labores de su sexo ... Domicilio. Calle Colon
Jose del C. Pulgar / Padre / Edad. Cuarenta i siete Anos / Prof. Agricultor / Dom. Calle Colon
```

Earlier image-reviewed staged notes report support for a Pulgar row, male sex, father/declarant `Jose del Carmen Pulgar` / `Jose del C. Pulgar`, place `Calle Colon`, and mother `Juana de Dios Ama[...] de Pulgar`, but those notes did not produce a QA-certified transcription.

## Conversion Confidence And QA Concern

Promotion remains blocked. The derivative transcriptions materially disagree on the child name, birth date/time, mother surname, and official signature. The original PNG and the manifest page image were not present in this checkout during this revision, so this worker could not perform the requested targeted row-level image QA.

Entry 515 also remains row-control context only because derivative rows disagree on child, father, and mother fields. It should not be promoted from this source packet.

## Uncertainty

Do not normalize the mother surname to `Amagada`, `Amador`, or `Arriagada` from this packet alone. Do not attach the entry 513 child to existing Pulgar or Dario/Pulgar identity clusters until targeted conversion QA and proof review resolve or explicitly preserve the conflicting readings.

## Promotion Recommendation

`hold_for_conversion_qa`: run targeted image QA for entry 513 child name/sex, exact birth date/time, mother surname, father/declarant wording, and entry 515 row spillover before any canonical claim, relationship, person page, or family page promotion.
