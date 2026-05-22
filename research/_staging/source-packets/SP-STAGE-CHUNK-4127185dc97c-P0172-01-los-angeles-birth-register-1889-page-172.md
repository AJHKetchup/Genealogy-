---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-4127185dc97c-P0172-01
source_title: Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1889, page 172
source_type: civil_birth_register
record_type: birth_register_page
jurisdiction: Los Angeles, La Laja, Chile
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
source_sha256: 05d0627a58615e91315e1e9e2da567034b4f324eb0179240e0f4d5cf985e3545
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
converted_sha256: 4127185dc97cb6f665c861db838f9a2b65cfc248bcc49324cad1a8e38bedd959
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0172-chunk-01.md
chunk_id: CHUNK-4127185dc97c-P0172-01
page_reference: page 172; register page 172; entries 513-515
page_start: 172
page_end: 172
entries: [513, 514, 515]
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Los Angeles Birth Register, 1889, Page 172

## Source Reference

- Source path: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png`
- Converted file: `raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md`
- Chunk/page reference: `CHUNK-4127185dc97c-P0172-01`, page 172, register page 172
- Chunk manifest: `raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/manifest.json`

## Literal Support

```text
Páj. 172
1889.—Rejistro de NACIMIENTOS en la Circunscripcion de Los Angeles, núm. 1º de Julio
```

The assigned chunk transcribes birth registrations numbered `513`, `514`, and `515`.

## Conversion Confidence / QA Concern

Low to medium. The page identity, register page number, year, and presence of entries 513-515 are supported. Targeted review of the original image shows material conflicts with the assigned converted/chunk transcript in the heading and several name fields. The visible heading appears closer to `Los Anjeles` and `La Laja` than `Los Angeles` and `Julio`. Entry 513 appears to record a child with surname `Pulgar` and given names closer to `Jose Dani...`, not `Isidoro del Carmen Diaz`. Entry 514 appears to include `Rigoberto Juan Bautista`, but the father field appears closer to `se ignora` while the mother/declarant is `Mercedes Riquelme`. Entry 515 is partly visible and appears to record surnames closer to `Neira`, conflicting with the chunk's `Leiva` readings.

## Uncertainty

Do not normalize or promote person names, parentage, street names, or jurisdiction wording until conversion QA reconciles the assigned chunk with the original source image.

## Promotion Recommendation

Hold for conversion QA before proof review or canonical promotion.
