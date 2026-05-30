---
type: source_packet
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260530074050814"
source_title: "Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172"
source_type: civil_registration_birth
source_path: "raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png"
source_sha256: aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
chunk_manifest: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/manifest.json"
page_reference: "page 1; register page 58; entry 172"
entry_number: "172"
family_relevance: high
matched_terms:
  - Arriagada
  - Pulgar
conversion_confidence: low
conversion_qa_concern: "The assigned chunk stages entry 172 as the Pulgar/Arriagada row, while the current converted Markdown on disk stages entry 172 as a Burgos/de la Cruz row. The proof-review follow-up requires targeted full-image QA, but both referenced full-page image paths are absent in this checkout, so this worker cannot certify which physical row controls entry 172."
uncertainty: "High for canonical promotion and row control; moderate for the father-field suffix after Pulgar. The father should be preserved only as Jose del Carmen Pulgar unless a later full-image QA certifies a suffix."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Entry 172 Pulgar/Arriagada Revision Hold

This packet starts with the family-relevant people named by the assigned chunk: child `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar`, and mother `Juana Arriagada de Pulgar`. It preserves the evidence as a Pulgar/Arriagada lead, but it is not promotion-ready.

## Literal Support From Assigned Chunk

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | Nombre. Jose del Carmen Segundo Pulgar Arriagada Sexo. Hombre | Fecha. Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde Lugar. Calle de Valdivia | Nombre del padre Jose del Carmen Pulgar S. Nac Chileno Prof Empleado Dom Calle de Colipi Nombre de la madre Juana Arriagada de Pulgar Nac Chilena Prof Su sexo Dom Calle de Colipi | Ernesto Herrera L. Presente al nacimiento Edad Veintiseis anos Prof Empleado Dom Calle de Valdivia
```

## Conflicting Converted Markdown Reading

The current converted Markdown records entry `172` as `Jose Miguel`, male, born `El seis de Abril de mil ochocientos ochenta i ocho`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and informant `Oswaldo Burgos`. That is a row-level conflict, not a spelling variant.

## QA Blocker

The manifest references the original raw PNG and `page-images/page-0001.png`, but `Test-Path` returned false for both files in this checkout. Because the proof-review request asks for full-image row certification, this extraction pass cannot safely certify whether the Pulgar/Arriagada row or the Burgos/de la Cruz row controls entry `172`.

Limited staged crop assets support a father field beginning `Jose del Carmen Pulgar` and a mother field `Juana Arriagada de Pulgar`, but those crops do not replace full-page row-control QA. The suffix after `Pulgar` remains unresolved.

## Promotion Recommendation

Keep this packet and all dependent claims and relationships at `hold_for_conversion_qa`. After the full source image is restored or located, targeted conversion QA should certify the controlling physical row, decide whether the converted Markdown is stale, row-shifted, or sourced from another image/page, and preserve the father field only to the visible certified level.
