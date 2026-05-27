---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-3d3ab761209f-P0001-01
worker: postconv-evidence-extraction-20260527151218732
source_id: ca05d0627a-los-angeles-birth-register-1889-page-172-entry-513
source_title: "Registro de Nacimientos, Circunscripcion de Los Angeles, La Laja, Chile, 1889, page 172, entry 513"
source_type: civil_birth_register
record_type: birth_registration
jurisdiction: "Los Angeles, La Laja, Chile"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png"
source_sha256: "05d0627a58615e91315e1e9e2da567034b4f324eb0179240e0f4d5cf985e3545"
converted_file: "raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md"
converted_sha256: "3d3ab761209fb351dce29fd110518d75087aa04075890da5943aa4f9d82bf175"
chunk: "raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-3d3ab761209f-P0001-01"
chunk_manifest: "raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/manifest.json"
page_reference: "image page 1; register page 172; entry 513; entries 514-515 used only as row-control context"
page_start: 1
page_end: 1
family_relevance: high
matched_family_terms: ["Pulgar"]
conversion_confidence: low
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Entry 513 Pulgar Birth Registration

## Person-First Focus

Entry 513 is relevant to the Pulgar family because it records a birth registration with father/declarant Jose del Carmen Pulgar / Jose del C. Pulgar and mother Juana de Dios Arriagada de Pulgar. The child appears to be recorded in the Pulgar Arriagada family line, but the derivative transcriptions disagree sharply with the image-reviewed reading, so this packet is a hold item rather than a canonical evidence packet.

## Literal Support

Chunk transcription:

```text
513 | Julio veinte i dos de mil ochocientos ochenta i nueve | Nombre. Pulgar Amagada / Jose Luis | Sexo. Masculino
Fecha. Junio veinte i seis de mil ochocientos ochenta i nueve, a las cuatro i media de la tarde | Lugar. Calle Colon
Nombre del padre. Jose del Carmen Pulgar ... Domicilio. Calle Colon
Nombre de la madre. Juana de Dios Amagada de Pulgar ... Domicilio. Calle Colon
Jose del C. Pulgar / Padre / Edad. Cuarenta i siete Anos / Prof. Agricultor / Dom. Calle Colon
```

Converted-file transcription:

```text
513 | Julio veintidos de mil ochocientos ochenta i nueve | Nombre. Isolina del Carmen / Jose | Sexo. Masculino
Fecha. El mismo veinte dos de mil ochocientos ochenta i nueve, a las cuatro de la manana.
Nombre del padre. Jose del Carmen Pulgar
Nombre de la madre. Juana de Dios Amador de Pulgar
```

Image-reviewed reading in this revision pass:

```text
Paj. 172 ... Rejistro de NACIMIENTOS en la Circunscripcion de Los Angeles, num. 1o de La Laja
513 ... Julio veinte i dos de mil ochocientos ochenta i nueve
Nombre: Pulgar Arriagada / [Dario?]
Sexo: Masculino
Fecha: Junio veinte i dos de mil ochocientos ochenta i nueve, a las cuatro i media de tarde
Lugar: Calle Colon
Nombre del padre: Jose del Carmen Pulgar; Nac. Chileno; Prof. Agricultor; Domicilio: Calle Colon
Nombre de la madre: Juana de Dios Arriagada de Pulgar; Nac. Chilena; Prof. Labores de su sexo; Domicilio: Calle Colon
Compareciente: Jose del C. Pulgar; Padre; Edad cuarenta i siete anos; Prof. Agricultor; Dom. Calle Colon
Identidad: El compareciente es conocido del oficial
```

## Conversion Confidence And QA Concern

Conversion confidence remains low because the chunk, converted file, and image-reviewed reading do not agree on the child full name, the mother's surname, or the birth date/time. The image supports the Pulgar family row and appears to resolve the mother surname as Arriagada, but this evidence extraction is not a conversion-update task and does not edit the converted Markdown.

## Uncertainty

The given-name line for the child is still not fully secure from this pass; it appears compatible with `Dario`, but should be confirmed by targeted row-level conversion QA. Entry 515 is visible enough to show it is a separate Neira row, but its lower fields should remain outside this Pulgar packet.

## Promotion Recommendation

`hold_for_conversion_qa`. Use this packet as an image-reviewed correction map. Do not promote entry 513 claims, parent-child relationships, or identity-cluster links until a QA-certified transcription and proof review exist.
