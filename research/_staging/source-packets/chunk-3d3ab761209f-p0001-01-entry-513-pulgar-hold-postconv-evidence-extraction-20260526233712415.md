---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-3d3ab761209f-P0001-01
worker: postconv-evidence-extraction-20260526233712415
source_id: ca05d0627a-los-anjeles-la-laja-birth-register-1889-page-172-entry-513
source_title: "Registro de Nacimientos, Circunscripcion de Los Anjeles, num. 1o de La Laja, Chile, 1889, page 172, entry 513"
source_type: civil_birth_register
record_type: birth_registration
jurisdiction: "Los Anjeles, La Laja, Chile"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png"
source_sha256: "05d0627a58615e91315e1e9e2da567034b4f324eb0179240e0f4d5cf985e3545"
converted_file: "raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md"
converted_sha256: "3d3ab761209fb351dce29fd110518d75087aa04075890da5943aa4f9d82bf175"
chunk: "raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-3d3ab761209f-P0001-01"
chunk_manifest: "raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/manifest.json"
page_reference: "image page 1; register page 172; entry 513, with entries 514-515 as row-control context"
page_start: 1
page_end: 1
family_relevance: high
matched_family_terms: ["Pulgar"]
conversion_confidence: low
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Entry 513 Pulgar Birth Registration Hold

## Person-First Focus

Entry 513 is relevant to the Pulgar family because the father and declarant fields identify `Jose del Carmen Pulgar` / `Jose del C. Pulgar`, and the child-name field begins with a `Pulgar Ama...`-style surname line. The record may support a Pulgar parent-child relationship after conversion QA, but it is not ready for canonical promotion.

## Literal Support

Derivative chunk support:

```text
513 | Julio veinte i dos de mil ochocientos ochenta i nueve | Nombre. Pulgar Amagada / Jose Luis | Sexo. Masculino
Fecha. Junio veinte i seis de mil ochocientos ochenta i nueve, a las cuatro i media de la tarde | Lugar. Calle Colon
Nombre del padre. Jose del Carmen Pulgar ... Prof. Agricultor ... Domicilio. Calle Colon
Nombre de la madre. Juana de Dios Amagada de Pulgar ... Labores de su sexo ... Domicilio. Calle Colon
Jose del C. Pulgar / Padre / Edad. Cuarenta i siete Anos / Prof. Agricultor / Dom. Calle Colon
```

Conflicting converted-file support:

```text
513 | Julio veintidos de mil ochocientos ochenta i nueve | Nombre. Isolina del Carmen / Jose | Sexo. Masculino
Fecha. El mismo veinte dos de mil ochocientos ochenta i nueve, a las cuatro de la manana.
Nombre de la madre. Juana de Dios Amador de Pulgar
```

Image-reviewed support from this revision:

```text
Paj. 172 ... Rejistro de NACIMIENTOS en la Circunscripcion de Los Anjeles, num. 1o de La Laja
513 ... Nombre ... Pulgar Ama[...] / Jose [...]
Sexo ... Masculino
Fecha ... Junio veinte i dos ... a las cuatro i media ... tarde
Lugar ... Calle Colon
Nombre del padre ... Jose del Carmen Pulgar
Nombre de la madre ... Juana de Dios Ama[...] de Pulgar
Compareciente ... Jose del C. Pulgar / Padre / Edad cuarenta i siete anos / Prof. Agricultor / Dom. Calle Colon
```

## Conversion Confidence And QA Concern

Conversion confidence is low for promotion. The source image supports a Pulgar family row and supports the father/declarant as Jose del Carmen Pulgar, but the derivative transcripts disagree on the child name, birth date/time, and mother surname. The image favors a `Pulgar Ama...` child surname line rather than the converted-file `Isolina del Carmen`, but this extraction task should preserve the disagreement until targeted conversion QA issues a corrected or explicitly uncertain transcription.

Entry 514 and entry 515 remain row-control context only. Their derivative conflicts should be reconciled to prevent row spillover, not promoted as broad non-family claims from this packet.

## Uncertainty

Do not normalize `Ama[...]` to `Amagada`, `Amador`, or `Arriagada` from this packet alone. Do not attach this entry to Dario/Pulgar canonical clusters or existing Jose/Juana pages until a proof-reviewed identity analysis follows corrected conversion QA.

## Promotion Recommendation

`hold_for_conversion_qa`. The Pulgar evidence is family-relevant, but identity-controlling readings remain unresolved.
