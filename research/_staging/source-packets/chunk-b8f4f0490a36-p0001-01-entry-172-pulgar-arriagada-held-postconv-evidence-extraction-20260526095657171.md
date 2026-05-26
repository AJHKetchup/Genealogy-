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
conversion_qa_concern: "The current converted Markdown transcribes entry 172 as a Burgos/de la Cruz birth, while the current chunk and original page image support a Pulgar/Arriagada entry. Image review during this extraction supports the Pulgar/Arriagada row as register entry 172, but targeted conversion QA is still required before promotion because the derivative transcripts disagree. The father field is visible as Jose del Carmen Pulgar with any final initial or suffix not certified here."
promotion_recommendation: hold_for_conversion_qa
worker: "postconv-evidence-extraction-20260526095545484"
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
---

# Source Packet: Entry 172 Pulgar/Arriagada Birth Registration

This packet stages the family-relevant evidence for register page 58, entry 172, without promoting it canonically. The known family surnames are Pulgar and Arriagada. The original page image and assigned chunk support a birth registration for a male child named `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.

## Literal Support From Assigned Chunk

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | **Nombre.** Jose del Carmen Segundo Pulgar Arriagada **Sexo.** Hombre | **Fecha.** Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde **Lugar.** Calle de Valdivia | **Nombre del padre** Jose del Carmen Pulgar S. **Nac** Chileno **Prof** Empleado **Dom** Calle de Colipí **Nombre de la madre** Juana Arriagada de Pulgar **Nac** Chilena **Prof** Su sexo **Dom** Calle de Colipí | Ernesto Herrera L. Presente al nacimiento **Edad** Veintiseis años **Prof** Empleado **Dom** Calle de Valdivia | **Por los testigos:** --- **Conocido del oficial.** | [signature] Emilio Riquelme V. | |
```

## Image-Reviewed Evidence

The original page image shows entry number `172` on page 58. Visual inspection supports the Pulgar/Arriagada row rather than the Burgos/de la Cruz row now present in the converted Markdown. The child name, mother name, and general birth/registration fields align with the assigned chunk. The father field is readable to the extent `Jose del Carmen Pulgar`; a final `S.` or other trailing mark is not certified in this extraction.

## Conversion Confidence And QA Concern

Conversion confidence is low for promotion because the derivative files disagree at the row level. This packet preserves the disagreement:

- Current chunk/image-supported reading: `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at 3 p.m. on Calle de Valdivia; father `Jose del Carmen Pulgar` with unresolved trailing mark; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`
- Current converted Markdown reading: `Jose Miguel`, male, born 6 April 1888 at 10 p.m. in `En esta`; father `Oswaldo Burgos`; mother `Concepcion de la Cruz`; informant `Oswaldo Burgos`.

## Uncertainty

The controlling entry appears to be the Pulgar/Arriagada row in the image and chunk, but the assigned converted file remains contradictory. Parent-child and identity claims must remain blocked until targeted conversion QA reconciles the source image, converted Markdown, current chunk, and source packet and certifies the father field.

## Promotion Recommendation

Hold for conversion QA. After QA, rerun proof review before promoting any child identity, birth fact, parent-child relationship, parental pair, parent identity merge, or Dario-line comparison.
