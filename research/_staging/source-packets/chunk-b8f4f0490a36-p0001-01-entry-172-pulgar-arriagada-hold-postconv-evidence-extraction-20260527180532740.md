---
type: source_packet
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260527180532740"
source_title: "Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172"
source_type: civil_registration_birth
source_path: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
chunk_manifest: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/manifest.json"
page_reference: "page 1; register pages 58-59; entry 172 on page 58 per assigned chunk"
entry_number: "172"
family_relevance: high
matched_terms:
  - Pulgar
  - Arriagada
conversion_confidence: "derivative_conflict_unresolved_in_this_worker"
conversion_qa_concern: "The assigned chunk records entry 172 as Pulgar/Arriagada, while the current converted Markdown records entry 172 as Burgos/de la Cruz. The original source image and job page image are not present in this checkout, so this worker cannot independently certify the physical row or the father-field suffix."
uncertainty: "High for canonical promotion until source image row-control is available to proof review; moderate for the father's terminal suffix even under the Pulgar/Arriagada reading."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Entry 172 Birth Registration Hold

This held packet concerns the family-relevant Pulgar/Arriagada reading of entry `172`.

## Literal Support From Assigned Chunk

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | Nombre. Jose del Carmen Segundo Pulgar Arriagada Sexo. Hombre | Fecha. Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde Lugar. Calle de Valdivia | Nombre del padre Jose del Carmen Pulgar S. Nac Chileno Prof Empleado Dom Calle de Colipi Nombre de la madre Juana Arriagada de Pulgar Nac Chilena Prof Su sexo Dom Calle de Colipi | Ernesto Herrera L. Presente al nacimiento Edad Veintiseis anos Prof Empleado Dom Calle de Valdivia |
```

## Conflicting Converted Markdown

The current converted Markdown instead reads entry `172` as `Jose Miguel`, son of `Oswaldo Burgos` and `Concepcion de la Cruz`, born `El seis de Abril de mil ochocientos ochenta i ocho`.

## QA Boundary

The image path in the manifest could not be opened in this worker: the file is absent from `raw/sources`, and the job's `page-images/page-0001.png` directory is also absent. This packet therefore does not certify row control. It stages the family-relevant evidence only as a held derivative packet pending targeted conversion QA or proof-review acceptance of an already staged image-reviewed QA note.

No canonical claim, relationship, identity merge, or wiki update should be promoted from this packet until the row-control conflict is resolved.
