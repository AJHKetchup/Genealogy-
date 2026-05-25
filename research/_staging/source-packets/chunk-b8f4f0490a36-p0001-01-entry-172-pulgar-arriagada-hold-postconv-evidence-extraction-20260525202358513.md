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
conversion_qa_concern: "The assigned chunk and image-reviewed row support a Pulgar/Arriagada entry 172, but the current assigned converted Markdown records a different entry 172 for Jose Miguel, father Oswaldo Burgos, mother Concepcion de la Cruz. Targeted conversion QA must decide the controlling row and certify the father-field reading before promotion."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Entry 172 Pulgar/Arriagada Birth Registration

This packet stages the family-relevant evidence for register page 58, entry 172. The family story relevance is high because the row names a Pulgar child and Arriagada mother in a civil birth register.

## Literal Support From Assigned Chunk

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | **Nombre.** Jose del Carmen Segundo Pulgar Arriagada **Sexo.** Hombre | **Fecha.** Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde **Lugar.** Calle de Valdivia | **Nombre del padre** Jose del Carmen Pulgar S. **Nac** Chileno **Prof** Empleado **Dom** Calle de Colipí **Nombre de la madre** Juana Arriagada de Pulgar **Nac** Chilena **Prof** Su sexo **Dom** Calle de Colipí | Ernesto Herrera L. Presente al nacimiento **Edad** Veintiseis años **Prof** Empleado **Dom** Calle de Valdivia | **Por los testigos:** --- **Conocido del oficial.** | [signature] Emilio Riquelme V. | |
```

## Conflicting Converted Markdown

The assigned converted Markdown currently gives a different entry 172:

```text
Nombres. Jose Miguel
Nombre del padre: Oswaldo Burgos
Nombre de la madre: Concepcion de la Cruz
```

That conflict means this packet cannot support promotion-ready canonical claims until targeted conversion QA reconciles the source image, current converted Markdown, assigned chunk, and source packet.

## Conversion Confidence And QA Concern

Conversion confidence is low for the derivative file assignment because the current converted Markdown and chunk disagree on the identity and parents of entry 172. The source image visible in this task aligns with the chunk at a high level for a Pulgar/Arriagada row on page 58, entry 172, but proof review requested targeted conversion QA to certify the controlling transcription and father field specifically.

QA should explicitly choose or explain the father-field reading as one of `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

## Uncertainty

The child name, birth date, registration date, father, mother, and parent-child relationship should remain staged only. The core blocker is not the family relevance; it is the unresolved conflict between derivative transcriptions and the need for a certified father-field reading.

## Promotion Recommendation

Hold for conversion QA. After QA, rerun proof review before any canonical claim, relationship, identity merge, parent merge, or Dario-line comparison is promoted.
