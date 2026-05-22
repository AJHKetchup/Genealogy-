---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-bdb698de8106-P0001-01
source_title: Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1889, page 172
source_type: civil_birth_register
record_type: birth_register_page
jurisdiction: Los Angeles, La Laja, Chile
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
source_sha256: 05d0627a58615e91315e1e9e2da567034b4f324eb0179240e0f4d5cf985e3545
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
converted_sha256: bdb698de810680fda5a8207dc19746550a2bfbba789d92ab01a18646d925b060
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
chunk_id: CHUNK-bdb698de8106-P0001-01
page_reference: page 1; register page 172
page_start: 1
page_end: 1
entries: [513, 514, 515]
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Los Angeles Birth Register, 1889, Page 172

## Source Reference

- Source path: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png`
- Converted file: `raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md`
- Chunk/page reference: `CHUNK-bdb698de8106-P0001-01`, page 1, register page 172
- Chunk manifest: `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/manifest.json`

## Literal Support

```text
Páj. 172
1889.—Rejistro de NACIMIENTOS en la Circunscripcion de Los Anjeles, núm. 1º de La Laja
```

The table includes birth registrations numbered `513`, `514`, and `515`.

## Image QA And Derivative-Transcript Conflict

Targeted review of the original image supports the page heading as `Los Anjeles`, `núm. 1º de La Laja`, matching the assigned bdb chunk on that point. The same image review found material conflicts between the assigned converted/chunk transcript and visible record evidence:

- Record 513: the image appears to show a child-name field beginning with `Pulgar...` and ending with a `José` line, with `Sexo. Masculino`, not the converted `Isolina del Carmen José`; the full child name remains unresolved.
- Record 514: the image appears to show child `Riquelme / Juan Bautista`, father field `Se ignora`, mother/declarant `Mercedes Riquelme`, witnesses probably `Benjamin Utrosa` and `Ignacio Jara`, and a street reading closer to `Calle San...`/`Calle Sanegueso` than the converted `Riquelme Juan Teodoro`, `Belisario Riquelme`, and `Calle Saneguin`.
- Official signature: the image appears consistent with `Emilio Lininger` or a similar reading, but the surname remains difficult and should not be promoted without proof review.
- Record 515: only the upper portion is visible in the source image. The image appears to show child `Neira Elvira / Laura de la Cruz...`, father/declarant `Pedro Pablo Neira`, and witnesses beginning with `Jose D. Ramirez H.` and `Santiago Fuentes`; this conflicts with the converted `Rosa Elvira del Carmen` and `Pedro Pablo Leiva`.

## Conversion Confidence And QA Concern

Overall confidence is high for source identity, page 172, the heading `Los Anjeles`, `La Laja`, and the presence of records 513, 514, and a partial 515. Confidence is low for the assigned converted transcript's person-name, parentage, witness, street, and record-completeness readings. Preserve the disagreement between derivative transcript and image-reviewed evidence; do not promote claims from this packet until conversion QA reconciles the bdb converted text with the image. The image-reviewed alternatives are conflict indicators, not replacement canonical transcriptions.

## Uncertainty

Do not normalize names, nineteenth-century spelling, or street names before conversion QA. Preserve both layers: the assigned bdb converted text and the image-reviewed disagreement notes above.

## Promotion Recommendation

Hold for conversion QA before proof review or canonical promotion. The packet now cites the correct bdb chunk path and chunk ID, but the converted transcript conflicts materially with the source image.
