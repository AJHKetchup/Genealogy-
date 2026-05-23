---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
worker: postconv-evidence-extraction-20260523181508215
source_title: "Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172"
source_type: civil_registration_birth
source_path: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
chunk_manifest: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/manifest.json"
page_reference: "page 1; register pages 58-59; entry 172 on page 58"
entry_number: "172"
jurisdiction: "Los Angeles, Circunscripcion de La Laja, Chile"
registration_date: "1888-04-07"
family_relevance: critical
matched_terms:
  - Carmen
  - Jose
  - Juan
  - Juana
  - Luis
  - Pulgar
  - Riquelme
conversion_confidence: mixed_after_source_image_reread
conversion_qa_concern: "The source image is present and was reread for this revision. The visible source supports the Pulgar/Arriagada row for entry 172, while the assigned converted Markdown file still gives a conflicting Gomez/de la Cruz row for entry 172. Within the visible Pulgar/Arriagada row, the father field appears to read 'Jose del Carmen Pulgar' with no clear final suffix; the assigned chunk records 'Jose del Carmen Pulgar S.', so conversion QA must explicitly record whether there is no suffix, a clear 'S.', or an uncertain suffix."
uncertainty: "High for promotion readiness because derivative transcripts disagree; moderate for the father's final abbreviated element and for exact residence spelling/normalization. Low that the visible image supports the Pulgar/Arriagada row rather than the converted Markdown's Gomez/de la Cruz row."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Birth Registration Entry 172

This packet stages evidence from entry 172 of the 1888 Los Angeles, Chile civil birth register. The source image is now present at the expected `raw/sources` path and was reread directly for this revision. The visible image supports the Pulgar/Arriagada row: child Jose del Carmen Segundo Pulgar Arriagada, father Jose del Carmen Pulgar, and mother Juana Arriagada de Pulgar. The converted Markdown file at `raw/converted/...entry-no-172.codex.md` instead gives entry 172 as a Jose Francisco birth registration for parents Oswaldo Gomez and Emilia de la Cruz, so that converted file should not be treated as reliable literal support for this Pulgar/Arriagada entry until conversion QA reconciles or supersedes the mismatch. Within the Pulgar/Arriagada row, the assigned chunk gives the father as `Jose del Carmen Pulgar S.`; this image reread does not show a clear final `S.` suffix.

## Literal Support

Assigned chunk literal support:

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | **Nombre.** Jose del Carmen Segundo Pulgar Arriagada **Sexo.** Hombre | **Fecha.** Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde **Lugar.** Calle de Valdivia | **Nombre del padre** Jose del Carmen Pulgar S. **Nac** Chileno **Prof** Empleado **Dom** Calle de Colipí **Nombre de la madre** Juana Arriagada de Pulgar **Nac** Chilena **Prof** Su sexo **Dom** Calle de Colipí | Ernesto Herrera L. Presente al nacimiento **Edad** Veintiseis años **Prof** Empleado **Dom** Calle de Valdivia | **Por los testigos:** --- **Conocido del oficial.** | [signature] Emilio Riquelme V. | |
```

Conflicting converted Markdown literal support:

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | Nombres. José Francisco<br>Sexo. Varon. | Fecha. El veinte i seis de Marzo de mil ochocientos ochenta i ocho, a las diez de la noche.<br>Lugar. En esta. | Nombre del padre: Oswaldo Gomez<br>Nac.: chileno Prof.: Militar<br>Dom.: En esta<br>Nombre de la madre: Emilia de la Cruz<br>Nac.: chilena Prof.: Su labor<br>Dom.: En esta | Oswaldo Gomez | Edad: Veinte i seis años<br>Prof.: Militar<br>Dom.: En esta<br>Por los testigos:<br>Conocido del oficial: | Camilo Henriquez | |
```

## Evidence Scope

Supports birth-name, sex, birth date/time, birth place, registration date, parent-child relationships, parents' stated nationality/occupation/residence, informant details, and registering official. The source is a civil birth registration, not a later family-history compilation.

## QA Notes

The original image is available at `raw/sources/...Entry No. 172;.png` and directly supports the Pulgar/Arriagada row. The child-name blocker is nevertheless not promotion-ready in this pass because the assigned converted Markdown file does not match the visible entry and the father-name suffix remains a conversion QA concern. The assigned chunk includes `S.`, while this source-image reread reads `Jose del Carmen Pulgar` without a clearly visible suffix. Do not promote father-name-dependent claims, combined parent links, or any other tree claims until conversion QA corrects or supersedes the converted Markdown and records whether the suffix is present, absent, or uncertain. Do not expand the father's identity or normalize `Jose` to `José` without a separate identity/style decision.

## Source Image Reread Notes

- This 2026-05-23 revision directly inspected the source image at the expected raw source path.
- Entry 172 is visible on register page 58.
- The child name reads as `Jose del Carmen Segundo Pulgar Arriagada`, written over three lines.
- The sex field reads `Hombre`.
- The birth date/time field reads `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`.
- The birthplace field reads `Calle de Valdivia`.
- The father field is image-read as `Jose del Carmen Pulgar`; the assigned chunk's final `S.` is not clearly visible in the image.
- The mother field reads `Juana Arriagada de Pulgar`.
- The informant field reads `Ernesto Herrera L.`, present at the birth, age 26, employed, resident at Calle de Valdivia.
