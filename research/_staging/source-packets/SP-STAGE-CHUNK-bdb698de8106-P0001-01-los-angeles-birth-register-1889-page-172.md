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
promotion_recommendation: promote_after_review
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

## Conversion Confidence And QA Concern

Overall confidence is medium-high for the tabular structure, dates, principal names, parent fields, and declarant fields. QA concerns remain for record 513 because the child name field reads `Isolina del Carmen` followed by `José` while the sex field says `Masculino`; for record 514 because the place/street is transcribed as `Calle Saneguin`; and for record 515 because sex, birthplace, mother, and some declarant details are blank in the converted table.

## Uncertainty

Do not normalize names, nineteenth-century spelling, or street names before image/proof review. Preserve `Los Anjeles`, `Calle Colon`, and `Calle Saneguin` as transcribed.

## Promotion Recommendation

Promote after proof review as a source packet for the three transcribed civil birth registrations.
