---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-3d3ab761209f-P0001-01
source_id: ca05d0627a-los-anjeles-la-laja-birth-register-1889-page-172
title: "Registro de Nacimientos, Circunscripcion de Los Anjeles, num. 1o de La Laja, Chile, 1889, page 172"
source_path: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png"
source_sha256: "05d0627a58615e91315e1e9e2da567034b4f324eb0179240e0f4d5cf985e3545"
converted_file: "raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md"
chunk: "raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-3d3ab761209f-P0001-01"
page_reference: "image page 1; register page 172; entries 513-515"
jurisdiction: "Circunscripcion de Los Anjeles, num. 1o de La Laja"
record_type: "civil birth register"
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet Draft: Los Anjeles Birth Register, 1889, Page 172

## Source Reference

- Source path: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png`
- Source SHA-256: `05d0627a58615e91315e1e9e2da567034b4f324eb0179240e0f4d5cf985e3545`
- Converted file: `raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md`
- Chunk/page reference: `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md`, `CHUNK-3d3ab761209f-P0001-01`, image page 1, register page 172
- Chunk manifest: `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/manifest.json`

## Source Description

Civil birth register page for the Circunscripcion de Los Anjeles, num. 1o de La Laja, Chile. The image shows register page 172 with entries 513, 514, and the upper portion of 515. Entry 515 continues into the lower crop; its child, father, declarant, witness, and emendation areas are visible, but the mother-field details are not fully supportable from the available image.

## Literal Support

- Image-reviewed page heading: `1889.-Rejistro de NACIMIENTOS en la Circunscripcion de Los Anjeles, num. 1o de La Laja`
- Register page: `Paj. 172`
- Visible entries: registration numbers `513`, `514`, and `515`
- Entry 513 image-supported fields include child surname/name in the Pulgar row, father `Jose del Carmen Pulgar`, mother `Juana de Dios ... de Pulgar`, domicile `Calle Colon`, and officer signature beginning `Emilio ...`.
- Entry 514 image-supported fields include child `Riquelme / Juan Bautista`, father field `Se ignora`, mother/declarant `Mercedes Riquelme`, and witnesses beginning `Benjamin ...` and `Ignacio ...`.
- Entry 515 image-supported fields include child `Neira Ulloa / Laura de la Cruz`, father/declarant `Pedro Pablo Neira`, witness names, and right-column note `Neira=emendado= / vale=`.

## Conversion Confidence And QA Concern

Conversion confidence remains mixed. The page image supports the chunk transcription more than the assembled converted Markdown for the principal identities in entries 513-515, but the derivative transcripts still disagree materially. The converted Markdown has alternate readings for the 513 child and mother, 514 child/father/place/witnesses, 515 child/father/mother, and the officer signature. Those disagreements should remain visible until the conversion layer is corrected or formally annotated.

Image review reduces, but does not eliminate, the previous blocker:

- The source image is now available and confirms the heading as `Los Anjeles, num. 1o de La Laja`, not `Los Angeles ... de Julio`.
- Entry 514's father field is image-supported as `Se ignora`; any claim naming a father from the conflicting converted file should not be promoted from this packet.
- Entry 514 witness surname and street/place remain difficult enough to preserve as QA limitations rather than canonical identity/place facts.
- Entry 515 `Neira=emendado= / vale=` is visible, but the lower part of entry 515 is cropped; the mother details cannot be promoted from this image-reviewed packet.
- Officer-signature support should be limited to the visible signature area and should not be normalized beyond the legible reading without separate QA.

## Uncertainty

Do not normalize place spelling, nineteenth-century orthography, surname parsing, witness identities, or officer names from this packet alone. Do not promote record 515 mother claims unless a complete lower crop or corrected conversion note supports the mother field.

## Promotion Recommendation

`hold_for_conversion_qa`: use this packet as a revised staging packet and QA map. Promote only after proof review accepts the image-reviewed corrections and the derivative transcript conflict is resolved or preserved in canonical source notes.
