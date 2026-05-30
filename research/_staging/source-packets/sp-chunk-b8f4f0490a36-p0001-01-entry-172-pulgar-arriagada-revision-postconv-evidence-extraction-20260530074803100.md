---
type: source_packet
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260530074803100"
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
conversion_qa_concern: "The assigned chunk records entry 172 as the Pulgar/Arriagada row, but the current converted Markdown records entry 172 as a Burgos/de la Cruz row. The original source image and page image are absent in this checkout, so this extraction pass cannot certify physical row control."
uncertainty: "High for canonical promotion and row control; moderate for the father-field suffix after Pulgar. Preserve the father only as Jose del Carmen Pulgar until full-image QA certifies any suffix."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Entry 172 Pulgar/Arriagada Revision Hold

This packet starts with the family-relevant people named in the assigned chunk: child `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar`, and mother `Juana Arriagada de Pulgar`.

## Literal Support From Assigned Chunk

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | Nombre. Jose del Carmen Segundo Pulgar Arriagada Sexo. Hombre | Fecha. Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde Lugar. Calle de Valdivia | Nombre del padre Jose del Carmen Pulgar S. Nac Chileno Prof Empleado Dom Calle de Colipi Nombre de la madre Juana Arriagada de Pulgar Nac Chilena Prof Su sexo Dom Calle de Colipi | Ernesto Herrera L. Presente al nacimiento Edad Veintiseis anos Prof Empleado Dom Calle de Valdivia
```

## Conflicting Converted Markdown Reading

The current converted Markdown on disk records entry `172` as `Jose Miguel`, male, born `El seis de Abril de mil ochocientos ochenta i ocho`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and informant `Oswaldo Burgos`. This is a row-level conflict, not a spelling or normalization variant.

## QA Blocker

This pass checked for the full source image named by the chunk and for image assets under the conversion job. The conversion job contains manifest, README, page Markdown, visual JSON, and work order files, but no page image. The source PNG also could not be located by the expected name or by local image search terms.

Because proof review specifically requested full-image row certification, these staged claims preserve only the assigned-chunk Pulgar/Arriagada lead and remain held. The father-field suffix after `Pulgar` is not certified; dependent claims preserve the father as `Jose del Carmen Pulgar`.

## Promotion Recommendation

Keep this packet and all dependent claims and relationships at `hold_for_conversion_qa`. After the full source image is restored or located, targeted conversion QA should certify whether physical entry `172` is the Pulgar/Arriagada row or the Burgos/de la Cruz row, decide whether the converted Markdown is stale, row-shifted, or sourced from another page, and preserve the father field only to the visible certified reading.
