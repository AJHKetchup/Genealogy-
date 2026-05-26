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
conversion_qa_concern: "The assigned chunk and direct image review support entry 172 as the Pulgar/Arriagada row, while the current converted Markdown records entry 172 as a Burgos/de la Cruz row. Father field is visible to at least Jose del Carmen Pulgar, but the trailing S. or mark remains uncertified."
promotion_recommendation: hold_for_conversion_qa
worker: "postconv-evidence-extraction-20260526170241068"
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
created: 2026-05-26
---

# Source Packet: Entry 172 Pulgar/Arriagada Birth Registration

This packet is family-relevant for the Pulgar/Arriagada line. It preserves the image-reviewed and assigned-chunk evidence for a birth registration of `Jose del Carmen Segundo Pulgar Arriagada`, but all dependent claims remain held because the current converted Markdown gives a different entry 172 row.

## Literal Support From Assigned Chunk

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | **Nombre.** Jose del Carmen Segundo Pulgar Arriagada **Sexo.** Hombre | **Fecha.** Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde **Lugar.** Calle de Valdivia | **Nombre del padre** Jose del Carmen Pulgar S. **Nac** Chileno **Prof** Empleado **Dom** Calle de Colipí **Nombre de la madre** Juana Arriagada de Pulgar **Nac** Chilena **Prof** Su sexo **Dom** Calle de Colipí | Ernesto Herrera L. Presente al nacimiento **Edad** Veintiseis años **Prof** Empleado **Dom** Calle de Valdivia | **Por los testigos:** --- **Conocido del oficial.** | [signature] Emilio Riquelme V. | |
```

## Image-Reviewed Evidence

The original page image shows register page 58 with entry number `172` in the second row on the left page. That row is visually consistent with the Pulgar/Arriagada reading in the assigned chunk: child `Jose del Carmen Segundo Pulgar Arriagada`, male; birth on 8 March 1888 at about 3 p.m. at Calle de Valdivia; father `Jose del Carmen Pulgar` with a trailing letter or mark; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.` present at the birth.

The father field should be preserved as unresolved until targeted conversion QA certifies it as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

## Current Converted Markdown Conflict

The current converted Markdown records entry `172` as a different row: child `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. in `En esta`, with `Oswaldo Burgos` as informant. This is a material row-level conflict, not a name variant.

## Promotion Hold

Keep this source packet, claims, relationship candidates, and identity/conflict notes at `hold_for_conversion_qa`. Targeted conversion QA should reconcile the source image, converted Markdown, assigned chunk, and staged packets; decide which row controls entry `172`; and certify the father-field reading only to the visible extent. Rerun proof review before any canonical claim, relationship, merge, or wiki-page update.
