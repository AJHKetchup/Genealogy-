---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
worker: postconv-evidence-extraction-20260522150707183
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
conversion_confidence: mixed_after_image_reread
conversion_qa_concern: "Controller flagged qc:reread-page. The assigned chunk supports the Pulgar/Arriagada entry, but the converted Markdown file's entry 172 is an unrelated Oswaldo Burgos/Concepcion de la Cruz entry. Earlier staged notes report an image reread supporting the Pulgar/Arriagada row, but in this 2026-05-22 revision the original source image and manifest page-image path could not be located in the checkout for direct verification. Within the Pulgar/Arriagada row, the assigned chunk records father 'Jose del Carmen Pulgar S.' while earlier image-reread notes report 'Jose del Carmen Pulgar' without a clearly visible final 'S.' suffix."
uncertainty: "High for promotion readiness because the original image is unavailable in this checkout and the converted Markdown file conflicts with the assigned chunk; moderate for the father's final abbreviated element and for exact residence spelling/normalization."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Birth Registration Entry 172

This packet stages evidence from entry 172 of the 1888 Los Angeles, Chile civil birth register. The assigned chunk directly names the child Jose del Carmen Segundo Pulgar Arriagada and his parents. The converted Markdown file at `raw/converted/...entry-no-172.codex.md` instead gives entry 172 as an Oswaldo Burgos/Concepcion de la Cruz birth registration, so that converted file should not be treated as reliable literal support for this entry until conversion QA reconciles the mismatch. Earlier staged notes report an image reread supporting the Pulgar/Arriagada row, but the original image path and manifest page-image path are not present in this checkout for direct verification in this revision. Within the Pulgar/Arriagada row, the assigned chunk gives the father as `Jose del Carmen Pulgar S.`; earlier image-reread notes support `Jose del Carmen Pulgar` and do not report a clearly legible final `S.` suffix.

## Literal Support

Assigned chunk literal support:

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | **Nombre.** Jose del Carmen Segundo Pulgar Arriagada **Sexo.** Hombre | **Fecha.** Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde **Lugar.** Calle de Valdivia | **Nombre del padre** Jose del Carmen Pulgar S. **Nac** Chileno **Prof** Empleado **Dom** Calle de Colipí **Nombre de la madre** Juana Arriagada de Pulgar **Nac** Chilena **Prof** Su sexo **Dom** Calle de Colipí | Ernesto Herrera L. Presente al nacimiento **Edad** Veintiseis años **Prof** Empleado **Dom** Calle de Valdivia | **Por los testigos:** --- **Conocido del oficial.** | [signature] Emilio Riquelme V. | |
```

Conflicting converted Markdown literal support:

```text
**Entry 172**
**Nombres.** José Miguel
**Nombre del padre:** Oswaldo Burgos
**Nombre de la madre:** Concepcion de la Cruz
```

## Evidence Scope

Supports birth-name, sex, birth date/time, birth place, registration date, parent-child relationships, parents' stated nationality/occupation/residence, informant details, and registering official. The source is a civil birth registration, not a later family-history compilation.

## QA Notes

The original image was not available at `raw/sources/...Entry No. 172;.png`, and the manifest page image `raw/codex-conversion-jobs/.../page-images/page-0001.png` is also missing in this checkout. Preserve the earlier image-reread notes as review context, not as a fresh verification from this revision. The child-name blocker is therefore not promotion-ready in this pass: the assigned chunk supports the Pulgar/Arriagada row, but the converted Markdown file does not match this entry and the father-name suffix remains a conversion QA concern. The assigned chunk includes `S.`, while earlier image-reread notes read `Jose del Carmen Pulgar` without a clearly visible suffix. Do not promote father-name-dependent claims, combined parent links, or any other tree claims until conversion QA restores or verifies the source image and resolves whether the suffix is present, absent, or uncertain. Do not expand the father's identity or normalize `Jose` to `José` without a separate identity/style decision.

## Prior Image Reread Notes

- Earlier staged notes report that entry 172 is visible on register page 58.
- The child name reads as `Jose del Carmen Segundo Pulgar Arriagada`, written over three lines.
- The sex field reads `Hombre`.
- The birth date/time field reads `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`.
- The birthplace field reads `Calle de Valdivia`.
- The father field is image-read as `Jose del Carmen Pulgar`; the assigned chunk's final `S.` is not clearly visible in the image.
- The mother field reads `Juana Arriagada de Pulgar`.
- The informant field reads `Ernesto Herrera L.`, present at the birth, age 26, employed, resident at Calle de Valdivia.
