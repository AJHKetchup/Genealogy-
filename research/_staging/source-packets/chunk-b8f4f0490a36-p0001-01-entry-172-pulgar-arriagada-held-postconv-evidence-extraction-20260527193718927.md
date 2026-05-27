---
type: source_packet
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260527193718927"
source_title: "Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172"
source_type: "civil_registration_birth"
source_path: "raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
chunk_manifest: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/manifest.json"
page_reference: "page 1; register page 58; physical row numbered 172"
entry_number: "172"
family_relevance: high
matched_terms:
  - Pulgar
  - Arriagada
conversion_confidence: "blocked_derivative_conflict_no_fresh_image_access"
conversion_qa_concern: "Assigned chunk and prior staged row-control notes support a Pulgar/Arriagada row for physical entry 172, but the current converted Markdown records a different Burgos/de la Cruz entry 172. In this pass, the original source image named in the task was not present under raw/sources and no local image file matched source_sha256 aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2, so fresh targeted image certification could not be completed."
uncertainty: "Use only as staged, noncanonical evidence. The assigned chunk supports the Pulgar/Arriagada details, but canonical promotion remains blocked until conversion-control restores or locates the source image, certifies the controlling row, and resolves the father-field suffix."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Entry 172 Pulgar/Arriagada Birth Registration

This packet preserves family-relevant evidence for `Jose del Carmen Segundo Pulgar Arriagada` from the assigned chunk while maintaining the proof-review blocker.

## Assigned Chunk Support

The assigned chunk transcribes register page 58, entry `172`, as:

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | **Nombre.** Jose del Carmen Segundo Pulgar Arriagada **Sexo.** Hombre | **Fecha.** Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde **Lugar.** Calle de Valdivia | **Nombre del padre** Jose del Carmen Pulgar S. **Nac** Chileno **Prof** Empleado **Dom** Calle de Colipi **Nombre de la madre** Juana Arriagada de Pulgar **Nac** Chilena **Prof** Su sexo **Dom** Calle de Colipi | Ernesto Herrera L. Presente al nacimiento **Edad** Veintiseis anos **Prof** Empleado **Dom** Calle de Valdivia | **Por los testigos:** --- **Conocido del oficial.** | [signature] Emilio Riquelme V. | |
```

## Current Converted Markdown Conflict

The current converted Markdown for the same converted file transcribes entry `172` as a different child and parents:

```text
Entry 172: Nombres. Jose Miguel; father Oswaldo Burgos; mother Concepcion de la Cruz; born El seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche.
```

## Extraction Boundary

The source image could not be accessed in this pass. The literal support above comes from the assigned chunk, not a fresh source-image review. The father field should be preserved at no stronger than `Jose del Carmen Pulgar S.` as the assigned chunk's derivative reading, with the suffix unresolved for canonical use.

Do not promote claims, relationships, identity merges, Dario-line attachments, or wiki updates from this packet until targeted conversion QA locates the original image, certifies which physical row controls entry `172`, and reruns proof review.
