---
type: source_packet
status: draft
source_title: "Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, entry 172"
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
conversion_qa_concern: "The source image and assigned chunk support entry 172 as the Pulgar/Arriagada row, but the current converted Markdown records entry 172 as a Burgos/de la Cruz row. The father field is readable to at least Jose del Carmen Pulgar; this extraction pass does not certify the trailing initial or mark."
promotion_recommendation: hold_for_conversion_qa
worker: "postconv-evidence-extraction-20260526165552835"
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
---

# Source Packet: Entry 172 Pulgar/Arriagada Birth Registration

This packet is family-relevant for the Pulgar/Arriagada family line. It preserves image-reviewed evidence for `Jose del Carmen Segundo Pulgar Arriagada`, his father `Jose del Carmen Pulgar`, and his mother `Juana Arriagada de Pulgar`, but holds all derivative claims because the converted Markdown and assigned chunk disagree at the row level.

## Literal Support From Assigned Chunk

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | **Nombre.** Jose del Carmen Segundo Pulgar Arriagada **Sexo.** Hombre | **Fecha.** Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde **Lugar.** Calle de Valdivia | **Nombre del padre** Jose del Carmen Pulgar S. **Nac** Chileno **Prof** Empleado **Dom** Calle de Colipí **Nombre de la madre** Juana Arriagada de Pulgar **Nac** Chilena **Prof** Su sexo **Dom** Calle de Colipí | Ernesto Herrera L. Presente al nacimiento **Edad** Veintiseis años **Prof** Empleado **Dom** Calle de Valdivia | **Por los testigos:** --- **Conocido del oficial.** | [signature] Emilio Riquelme V. | |
```

## Image-Reviewed Evidence

The original page image shows entry number `172` on register page 58 as a Pulgar/Arriagada row. Visual review supports the assigned chunk's child name, male sex, birth date/place line, mother name, and informant line in broad terms. The father field is visible as `Jose del Carmen Pulgar`; the final `S.` or any other trailing mark should be certified by targeted conversion QA before promotion.

## Preserved Conflict

- Image/chunk-supported reading: `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at 3 p.m. on Calle de Valdivia; father `Jose del Carmen Pulgar` with unresolved trailing mark; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`
- Current converted Markdown reading: `Jose Miguel`, male, born 6 April 1888 at 10 p.m. in `En esta`; father `Oswaldo Burgos`; mother `Concepcion de la Cruz`; informant `Oswaldo Burgos`.

## Uncertainty And Promotion

Keep this packet and all dependent claims at `hold_for_conversion_qa`. Targeted conversion QA should reconcile the source image, current converted Markdown, assigned chunk, and this packet; decide the controlling entry 172 row; and certify the father field only to the visible extent. Rerun proof review before any canonical claim, relationship, identity merge, or Dario-line comparison is promoted.
