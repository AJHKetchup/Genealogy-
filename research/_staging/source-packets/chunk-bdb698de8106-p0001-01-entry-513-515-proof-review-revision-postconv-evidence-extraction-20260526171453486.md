---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-bdb698de8106-P0001-01
worker: postconv-evidence-extraction-20260526171453486
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
matched_terms: [Pulgar]
conversion_confidence: low
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet Revision: Page 172 Entries 513-515

## Person-First Scope

Entry 513 is the family-relevant row because it contains `Pulgar` in the father and declarant fields. Entry 515 is included only because proof review specifically requested continued hold/reconciliation for its child-name draft; it is not used to support the Pulgar family narrative.

## Literal Support From Converted Chunk

```text
513 ... Nombre. Isolina del Carmen / José ... Sexo. Masculino
Nombre del padre. José del Carmen Pulgar
Nombre de la madre. Juana de Dios Amador de Pulgar
José del C. Pulgar / Padre / Edad. Cuarenta i siete Años / Prof. Agricultor / Dom. Calle Colon
```

```text
515 ... Nombre. Rosa Elvira del Carmen
Pedro Pablo Leiva / Padre
```

## Conversion Confidence / QA Concern

Hold for conversion QA. The converted text and the image-reviewed evidence remain materially out of agreement at row level.

- Entry 513: the declarant-column reading `José del C. Pulgar`, `Padre`, age forty-seven, farmer, and `Calle Colon` is comparatively strong, but the same row has unresolved child-name, birth-date/time, and mother-surname conflicts. This prevents promotion of the declarant claim and any parent-child relationship from the row.
- Entry 515: proof review found the converted `Rosa Elvira del Carmen` reading is not securely supported by the partial visible source image. The image-reviewed alternative readings are conflict indicators only, not replacement transcriptions.

## Uncertainty

Do not normalize names or substitute image-review alternatives into canonical claims before targeted conversion QA. Preserve the derivative transcript, image-review disagreement, and proof-review hold together.

## Promotion Recommendation

`hold_for_conversion_qa`. After conversion QA reconciles entries 513 and 515, rerun proof review on any atomic claim before promotion.
