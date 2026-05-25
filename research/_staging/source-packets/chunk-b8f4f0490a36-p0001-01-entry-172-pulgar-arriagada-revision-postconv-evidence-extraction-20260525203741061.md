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
source_type: civil_birth_registration
source_location: "Los Angeles, La Laja, Chile"
source_date: "1888-04-07"
family_relevance: high
matched_terms:
  - Arriagada
  - Pulgar
conversion_confidence: low
conversion_qa_concern: "The assigned chunk and direct image context support a Pulgar/Arriagada row for entry 172, while the current assigned converted Markdown records entry 172 as Jose Miguel, father Oswaldo Burgos, mother Concepcion de la Cruz. This is a row-level conversion or file-assignment conflict. The father field also needs targeted QA to decide whether it reads Jose del Carmen Pulgar, Jose del Carmen Pulgar S., or Jose del Carmen Pulgar [?]."
uncertainty: "Claims from this packet are direct if the Pulgar/Arriagada row controls, but they are blocked by the assigned converted Markdown conflict and father-field suffix uncertainty."
promotion_recommendation: hold_for_conversion_qa
worker: postconv-evidence-extraction-20260525203741061
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
---

# Source Packet: Entry 172 Pulgar/Arriagada Birth Registration

This packet preserves family-relevant evidence for the child recorded in the assigned chunk as `Jose del Carmen Segundo Pulgar Arriagada`. The row is relevant to the Pulgar/Arriagada family because it records a birth, names a Pulgar father, and names an Arriagada mother.

## Literal Support From Assigned Chunk

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | **Nombre.** Jose del Carmen Segundo Pulgar Arriagada **Sexo.** Hombre | **Fecha.** Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde **Lugar.** Calle de Valdivia | **Nombre del padre** Jose del Carmen Pulgar S. **Nac** Chileno **Prof** Empleado **Dom** Calle de Colipí **Nombre de la madre** Juana Arriagada de Pulgar **Nac** Chilena **Prof** Su sexo **Dom** Calle de Colipí | Ernesto Herrera L. Presente al nacimiento **Edad** Veintiseis años **Prof** Empleado **Dom** Calle de Valdivia | **Por los testigos:** --- **Conocido del oficial.** | [signature] Emilio Riquelme V. | |
```

## Conflicting Assigned Converted Markdown

The current assigned converted Markdown gives entry 172 as a different family:

```text
Nombres. Jose Miguel
Nombre del padre: Oswaldo Burgos
Nombre de la madre: Concepcion de la Cruz
```

This is not a spelling difference. It is a row-level conflict between derivative transcripts for the same assigned entry number.

## Image-Reviewed Evidence Boundary

Direct inspection of the source image during this extraction supports the Pulgar/Arriagada row on register page 58, entry 172, rather than the Burgos/de la Cruz row in the converted Markdown. This extraction does not correct the converted file. It preserves the disagreement and routes the packet to targeted conversion QA.

## Required QA

Targeted conversion QA should reconcile the source image, assigned converted Markdown, assigned chunk, and this packet. The QA output should identify the controlling row for entry 172 and explicitly record the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

## Promotion Recommendation

Keep this packet and all dependent child, birth, parent, and relationship drafts at `hold_for_conversion_qa`. After conversion QA, rerun proof review before any canonical claim, relationship, identity merge, parent merge, or Pulgar/Dario-line comparison is promoted.
