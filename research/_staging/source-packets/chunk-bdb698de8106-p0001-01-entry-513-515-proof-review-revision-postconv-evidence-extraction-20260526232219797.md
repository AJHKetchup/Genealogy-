---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-bdb698de8106-P0001-01
worker: postconv-evidence-extraction-20260526232219797
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
chunk_manifest: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/manifest.json
page_reference: page 1; register page 172; entries 513-515
page_start: 1
page_end: 1
family_relevance: high
matched_family_terms: [Pulgar]
conversion_confidence: low
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet Revision: Page 172 Entries 513-515

## Person-First Focus

Entry 513 is the family-relevant evidence because the derivative transcript names `Jose del Carmen Pulgar` as father and `Jose del C. Pulgar` as father/declarant. That evidence could support a Pulgar family narrative after targeted conversion QA, but it is not promotion-ready because proof review reports unresolved row-level disagreement in identity-controlling fields.

Entry 515 is retained only as a boundary/control issue because proof review found possible row-spillover or partial-row problems. It does not add Pulgar family evidence.

## Literal Support From Converted Chunk

```text
513 ... Nombre. Isolina del Carmen / Jose ... Sexo. Masculino
Fecha. El mismo veinte dos de mil ochocientos ochenta i nueve, a las cuatro de la manana. Lugar. Calle Colon
Nombre del padre. Jose del Carmen Pulgar ... Nac. Chileno ... Prof. Agricultor ... Domicilio. Calle Colon
Nombre de la madre. Juana de Dios Amador de Pulgar ... Nac. Chilena ... Prof. Labores de su sexo ... Domicilio. Calle Colon
Jose del C. Pulgar ... Padre ... Edad. Cuarenta i siete Anos ... Prof. Agricultor ... Dom. Calle Colon
```

```text
515 ... Nombre. Rosa Elvira del Carmen
Pedro Pablo Leiva ... Padre
```

## Conversion Confidence / QA Concern

Low for canonical promotion. The converted Markdown and chunk agree with each other, but prior proof review reports material disagreement between derivative text and image-reviewed evidence.

The held fields are:

- Entry 513 child full name and sex.
- Entry 513 birth date/time/place at row level.
- Entry 513 mother surname, especially `Amador` versus an image-reviewed `Amagada`-style concern.
- Entry 513 father/declarant profession if older notes preserve `Agricultor` versus `Jornalero`.
- Entry 515 child name and father/declarant surname, only enough to prevent row spillover into the Pulgar row.

## Uncertainty

This packet preserves the disagreement. It does not substitute image-review alternatives into the transcription and does not normalize `Amador`, `Amagada`, or `Arriagada` as variants.

## Promotion Recommendation

`hold_for_conversion_qa`. After targeted conversion QA issues a stable corrected transcription or explicit uncertainty markers, rerun proof review on each atomic claim and relationship candidate before any canonical edit.
