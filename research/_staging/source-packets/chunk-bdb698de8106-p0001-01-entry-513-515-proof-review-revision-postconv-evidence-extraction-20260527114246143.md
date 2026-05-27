---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-bdb698de8106-P0001-01
worker: postconv-evidence-extraction-20260527114246143
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

# Source Packet Revision: Entry 513 Pulgar Birth Row

## Person-First Focus

Entry 513 is family-relevant because the father/declarant fields in the derivative transcript name `Jose del Carmen Pulgar` / `Jose del C. Pulgar`. The row may later support a Pulgar birth event and parent-child relationship, but proof review has repeatedly found the child name, birth-row alignment, mother surname, and adjacent entry 515 boundary fields not yet promotion-ready.

Entry 515 is included only as row-boundary control. No Pulgar-family claim is inferred from entry 515.

## Literal Support From Converted Chunk

```text
513 ... Nombre. Isolina del Carmen / Jose ... Sexo. Masculino
Fecha. El mismo veinte dos de mil ochocientos ochenta i nueve, a las cuatro de la mañana. Lugar. Calle Colon
Nombre del padre. Jose del Carmen Pulgar ... Nac. Chileno Prof. Agricultor ... Domicilio. Calle Colon
Nombre de la madre. Juana de Dios Amador de Pulgar ... Nac. Chilena Prof. Labores de su sexo ... Domicilio. Calle Colon
Jose del C. Pulgar ... Padre ... Edad. Cuarenta i siete Anos ... Prof. Agricultor ... Dom. Calle Colon
```

## Preserved Disagreement / QA Concern

Prior proof-review revision notes and staged image-review drafts disagree with the derivative transcript in identity-controlling fields. They indicate that the child-name line may not support `Isolina del Carmen Jose`, the mother surname may not securely read `Amador`, the birth date/time may need rereading, and entry 515 must be checked to prevent row spillover. This extraction does not alter the raw source, converted Markdown, chunk, or page Markdown.

## Conversion Confidence

Low for canonical promotion. The father/declarant name `Jose del Carmen Pulgar` and occupation/residence fields are comparatively stronger than the child and mother fields, but they still depend on the same disputed row and should remain staged only.

## Uncertainty

Do not normalize the child name, mother surname, birth date/time, or parent-child relationship from this packet. Preserve the disagreement between the derivative transcript and image-reviewed concerns until targeted conversion QA supplies a stable literal reading or explicit `[?]` uncertainty markers.

## Promotion Recommendation

`hold_for_conversion_qa`. After targeted conversion QA, rerun proof review on separate atomic claims for child name/sex, birth date/time/place, father/declarant, mother, and parent-child relationship.
