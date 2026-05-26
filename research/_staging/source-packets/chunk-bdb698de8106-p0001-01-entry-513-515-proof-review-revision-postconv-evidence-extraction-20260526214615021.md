---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-bdb698de8106-P0001-01
worker: postconv-evidence-extraction-20260526214615021
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
page_reference: page 1; register page 172; entries 513-515
page_start: 1
page_end: 1
family_relevance: high
matched_family_terms: [Pulgar]
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet Revision: Page 172, Entries 513-515

## Person-First Focus

Entry 513 is the family-relevant row because it identifies `Jose del Carmen Pulgar` in the father field and `Jose del C. Pulgar` as the father/declarant. The row is useful for the Pulgar family story only after conversion QA resolves the child-name and mother-name conflicts noted by proof review.

## Literal Support From Converted Chunk

```text
513 | Julio veintidos de mil ochocientos ochenta i nueve | Nombre. Isolina del Carmen Jose; Sexo. Masculino
Fecha. El mismo veinte dos de mil ochocientos ochenta i nueve, a las cuatro de la manana. Lugar. Calle Colon
Nombre del padre. Jose del Carmen Pulgar ... Nac. Chileno ... Prof. Agricultor ... Domicilio. Calle Colon
Nombre de la madre. Juana de Dios Amador de Pulgar ... Nac. Chilena ... Prof. Labores de su sexo ... Domicilio. Calle Colon
Jose del C. Pulgar; Padre; Edad. Cuarenta i siete Anos; Prof. Agricultor; Dom. Calle Colon
```

Entry 515 is included only because proof review flagged a specific child-name conflict:

```text
515 ... Nombre. Rosa Elvira del Carmen
```

## Conversion Confidence / QA Concern

Low for canonical promotion. The converted file and chunk agree with each other, but prior proof review records material disagreement between the derivative transcript and image-reviewed evidence. For entry 513, the declarant/father column is comparatively strong, yet the child-name field and mother surname remain unresolved enough to block identity and relationship promotion. For entry 515, the visible row was described as partial and not sufficient to promote the converted `Rosa Elvira del Carmen` name.

## Uncertainty

The image-reviewed alternatives are preserved as conflict context only. This source packet does not replace the converted text and does not infer a canonical child identity from either the derivative transcript or the image-review notes.

## Promotion Recommendation

`hold_for_conversion_qa`. Reread the original image against the converted transcript at row level, then send the revised atomic claims and relationship candidate through proof review before canonical promotion.
