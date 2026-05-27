---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-bdb698de8106-P0001-01
worker: postconv-evidence-extraction-20260527153302921
source_title: Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1889, page 172
source_type: civil_birth_register
record_type: birth_register_page
jurisdiction: Los Angeles, La Laja, Chile
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png"
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

# Source Packet: Entry 513 Pulgar Birth Register Hold

## Person-First Focus

Entry 513 is relevant to the Pulgar family because the father and declarant fields in the converted chunk read `Jose del Carmen Pulgar` and `Jose del C. Pulgar`. The entry may eventually support a child birth event and parent-child relationship, but the child name, birth date/time, mother surname, and adjacent entry 515 boundary fields remain disputed between the derivative transcript and image-reviewed staging notes.

Entry 515 is retained only as row-boundary context to prevent spillover into entry 513. It is not extracted as Pulgar family evidence.

## Literal Support From Converted Chunk

```text
513 ... Nombre. Isolina del Carmen / Jose ... Sexo. Masculino
Fecha. El mismo veinte dos de mil ochocientos ochenta i nueve, a las cuatro de la mañana.
Lugar. Calle Colon
Nombre del padre. Jose del Carmen Pulgar ... Nac. Chileno Prof. Agricultor ... Domicilio. Calle Colon
Nombre de la madre. Juana de Dios Amador de Pulgar ... Nac. Chilena Prof. Labores de su sexo ... Domicilio. Calle Colon
Jose del C. Pulgar ... Padre ... Edad. Cuarenta i siete Anos ... Prof. Agricultor ... Dom. Calle Colon
```

## Preserved Disagreement

Prior proof reviews and image-review notes report that the converted child name `Isolina del Carmen Jose`, birth wording, and mother surname `Amador` are not stable. The image-reviewed notes point toward a child-name field beginning with a Pulgar line and a mother surname closer to `Ama[?]gada` or another unresolved form, but those readings should remain conflict indicators until formal conversion QA creates an amended transcription with explicit `[?]` uncertainty markers.

## Conversion Confidence / QA Concern

Low for promotion. The father/declarant wording is the strongest family clue, but it sits inside a row whose identity-controlling fields are not settled. This packet does not amend the raw source, converted Markdown, chunk Markdown, or page Markdown.

## Promotion Recommendation

`hold_for_conversion_qa`. After targeted conversion QA, rerun proof review on separate atomic claims for child name/sex, birth date/time/place, father/declarant, mother, and any parent-child relationship.
