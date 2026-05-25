---
type: source_packet
status: draft
source_title: "Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172"
source_path: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
chunk_manifest: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/manifest.json"
page_reference: "page 1; register page 58; entry 172"
source_type: civil_birth_register
source_location: "Los Angeles, La Laja, Chile"
source_date: "1888-04-07"
family_relevance: high
matched_terms:
  - Arriagada
  - Pulgar
conversion_confidence: mixed
conversion_qa_concern: "The source image and assigned chunk support a Pulgar/Arriagada birth entry, while the assigned converted Markdown records entry 172 as Jose Miguel, child of Oswaldo Burgos and Concepcion de la Cruz. Targeted conversion QA must decide the controlling row and certify the father-field reading after Pulgar."
promotion_recommendation: hold_for_conversion_qa
worker: postconv-evidence-extraction-20260525193149774
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
---

# Source Packet: Entry 172 Pulgar/Arriagada Birth

This packet stages family-relevant evidence for the child recorded in entry 172 on register page 58. The image-visible row and assigned chunk support a Pulgar/Arriagada birth record. The assigned converted Markdown, however, transcribes a different entry 172 for a Burgos/de la Cruz child. This is a material row/content conflict, so the packet and dependent claims remain on hold for targeted conversion QA.

## Literal Support

From the assigned chunk for page 1, register page 58, entry 172:

```text
172 | Siete de Abril de mil ochocientos ochenta i ocho
```

```text
Nombre. Jose del Carmen Segundo Pulgar Arriagada
Sexo. Hombre
```

```text
Fecha. Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde
Lugar. Calle de Valdivia
```

```text
Nombre del padre Jose del Carmen Pulgar S.
Nac Chileno
Prof Empleado
Dom Calle de Colipi
Nombre de la madre Juana Arriagada de Pulgar
Nac Chilena
Prof Su sexo
Dom Calle de Colipi
```

```text
Ernesto Herrera L. Presente al nacimiento
Edad Veintiseis anos
Prof Empleado
Dom Calle de Valdivia
```

## Converted Markdown Conflict

The current assigned converted Markdown records entry 172 as `Jose Miguel`, born `El seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche`, with father `Oswaldo Burgos` and mother `Concepcion de la Cruz`. That is not a spelling or abbreviation conflict. It represents a different child and parent set from the image-visible Pulgar/Arriagada row.

## Conversion Confidence And QA Concern

Conversion confidence is mixed. The assigned chunk and visual source inspection support the Pulgar/Arriagada row for the image currently assigned to this task. The assigned converted Markdown does not match that row. Targeted conversion QA should reconcile the source image, converted Markdown, chunk, manifest, and source packet, then identify the controlling transcription for entry 172.

## Uncertainty

The father field visibly reads `Jose del Carmen Pulgar` with an unresolved suffix or mark. The chunk reads `Jose del Carmen Pulgar S.`. Because proof review specifically requested certification among `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]`, no father-name or parent-child claim should be promoted until conversion QA records the exact source-visible reading.

## Promotion Recommendation

`hold_for_conversion_qa`. After targeted conversion QA resolves the controlling row and father-field reading, rerun proof review for the child identity, birth facts, parent names, and proposed parent-child relationship.
