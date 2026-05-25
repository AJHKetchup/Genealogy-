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
conversion_qa_concern: "The source image and assigned chunk support a Pulgar/Arriagada birth entry, but the assigned converted Markdown's entry 172 is for Jose Miguel with father Oswaldo Burgos and mother Concepcion de la Cruz. Targeted conversion QA must decide the controlling row and certify whether the father field reads Jose del Carmen Pulgar, Jose del Carmen Pulgar S., or Jose del Carmen Pulgar [?]."
promotion_recommendation: hold_for_conversion_qa
worker: postconv-evidence-extraction-20260525192412933
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
---

# Source Packet: Entry 172 Pulgar/Arriagada Birth

This packet stages family-relevant evidence for the child recorded in entry 172 of the Los Angeles civil birth register. The source image and assigned chunk indicate a Pulgar/Arriagada child, but the assigned converted Markdown transcribes a different entry 172. No canonical claims, relationships, identity merges, or broader line comparisons should be promoted until targeted conversion QA resolves the row assignment.

## Literal Support From Source Image And Chunk

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
Edad Veintiseis años
Prof Empleado
Dom Calle de Valdivia
```

## Converted Markdown Conflict

The current assigned converted Markdown's entry 172 instead gives `Jose Miguel`, born `El seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche`, with father `Oswaldo Burgos` and mother `Concepcion de la Cruz`. That conflict is not a spelling variant; it is a different child and parent set.

## Conversion Confidence And QA Concern

Confidence is mixed. The source image and chunk support the Pulgar/Arriagada family-relevant row, but the assigned converted Markdown is materially inconsistent with the image/chunk. Targeted conversion QA must reconcile the source image, converted Markdown, chunk, and source packet before proof review.

## Uncertainty

The exact final character or suffix after the father name remains unresolved. The chunk reads `Jose del Carmen Pulgar S.`, while prior review requests require QA to certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

## Promotion Recommendation

Hold for conversion QA. After QA identifies the controlling row and certifies the father-field reading, rerun proof review for the child identity, birth facts, parent names, and proposed parent-child relationship before canonical promotion.
