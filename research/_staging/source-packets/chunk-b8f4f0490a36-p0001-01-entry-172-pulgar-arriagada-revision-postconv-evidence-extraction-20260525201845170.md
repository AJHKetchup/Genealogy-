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
conversion_qa_concern: "The assigned chunk records a Pulgar/Arriagada entry 172, but the assigned converted Markdown records a Burgos/de la Cruz entry 172. Targeted conversion QA must decide the controlling row and certify the father-field reading before promotion."
promotion_recommendation: hold_for_conversion_qa
worker: postconv-evidence-extraction-20260525201845170
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
supersedes_worker_outputs:
  - postconv-evidence-extraction-20260525193809709
---

# Source Packet: Entry 172 Pulgar/Arriagada Birth

This packet stages the family-relevant Pulgar/Arriagada evidence from the assigned chunk while preserving the material disagreement with the assigned converted Markdown. The evidence is not promotion-ready because the same converted file currently gives entry 172 as a different child and parent set.

## Literal Support From Assigned Chunk

Assigned chunk, page 1, register page 58, entry 172:

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

The assigned converted Markdown records entry 172 as `Jose Miguel`, born `El seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche`, with father `Oswaldo Burgos` and mother `Concepcion de la Cruz`. That is a different family and birth event, not a spelling variant of the Pulgar/Arriagada row.

## Conversion Confidence And QA Concern

Conversion confidence is mixed. The assigned chunk supports a Pulgar/Arriagada birth registration; the assigned converted Markdown supports a Burgos/de la Cruz birth registration. Targeted conversion QA should compare the source image, converted Markdown, chunk, manifest, and this packet, then identify the controlling entry 172 row.

## Uncertainty

The father field must remain held. The chunk reads `Jose del Carmen Pulgar S.`, while proof review requested certification among `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]`.

## Promotion Recommendation

`hold_for_conversion_qa`. After targeted conversion QA resolves the controlling row and father-field reading, rerun proof review for the child identity, birth facts, parent names, and proposed parent-child relationships.
