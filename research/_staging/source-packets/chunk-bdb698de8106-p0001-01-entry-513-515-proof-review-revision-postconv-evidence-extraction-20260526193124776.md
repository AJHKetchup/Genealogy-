---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-bdb698de8106-P0001-01
worker: postconv-evidence-extraction-20260526193124776
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

## Family-Relevant Focus

Entry 513 is the family-relevant row. The current converted/chunk transcript names `José del Carmen Pulgar` as father and `José del C. Pulgar` as the father/declarant, age forty-seven, agriculturist, domiciled at Calle Colon.

## Literal Support From Converted Chunk

```text
513 | Julio veintidos de mil ochocientos ochenta i nueve | Nombre. Isolina del Carmen José; Sexo. Masculino
Fecha. El mismo veinte dos de mil ochocientos ochenta i nueve, a las cuatro de la mañana. Lugar. Calle Colon
Nombre del padre. José del Carmen Pulgar ... Domicilio. Calle Colon
Nombre de la madre. Juana de Dios Amador de Pulgar ... Domicilio. Calle Colon
José del C. Pulgar; Padre; Edad. Cuarenta i siete Años; Prof. Agricultor; Dom. Calle Colon
```

Entry 515 is retained only as a conversion-QA control because proof review specifically flagged its child-name draft:

```text
515 ... Nombre. Rosa Elvira del Carmen
```

## Conversion Confidence / QA Concern

Source identity, page number, jurisdiction, and the presence of entries 513-515 are stable enough for source-scoped staging. Promotion is blocked because direct image-reviewed notes disagree materially with the derivative transcript for row-level fields.

For entry 513, the Pulgar father/declarant evidence is comparatively strong, but the child-name field, mother surname, and related row details remain unresolved. Image-reviewed notes indicate the child-name field may preserve a Pulgar-surname line rather than the converted `Isolina del Carmen José`; the mother surname may not be the converted `Amador`.

For entry 515, the visible image was described as partial and not sufficient to promote the converted `Rosa Elvira del Carmen` reading.

## Uncertainty

The image-reviewed alternatives are conflict indicators, not replacement transcriptions. Do not normalize names, create a canonical child identity, or attach parent-child relationships until targeted conversion QA reconciles the derivative transcript with the original image.

## Promotion Recommendation

`hold_for_conversion_qa`. After row-level conversion QA, rerun proof review on each atomic claim and relationship candidate before canonical promotion.
