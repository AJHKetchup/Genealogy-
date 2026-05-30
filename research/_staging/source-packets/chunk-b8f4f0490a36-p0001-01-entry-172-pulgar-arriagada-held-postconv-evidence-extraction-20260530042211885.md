---
type: source_packet
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: postconv-evidence-extraction-20260530042028956
source_title: "Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172"
source_type: civil_registration_birth
source_path: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
chunk_manifest: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/manifest.json"
page_reference: "page 1; register page 58; entry 172"
entry_number: "172"
family_relevance: high
matched_terms:
  - Arriagada
  - Pulgar
conversion_confidence: low
conversion_qa_concern: "The assigned chunk reads entry 172 as the Pulgar/Arriagada birth row, but the current converted Markdown reads entry 172 as a Burgos/de la Cruz row. In this checkout the original PNG and manifest page image are absent, so this worker could not certify the physical row from the original image. Existing cropped review assets show a Pulgar/Arriagada parent/informant section and support preserving the father only as at least 'Jose del Carmen Pulgar' with a possible unresolved suffix, but they do not by themselves certify row number/control."
uncertainty: "High for promotion readiness because row control is not image-certified in this pass and derivative transcripts disagree. Moderate for whether the father field should be recorded as 'Jose del Carmen Pulgar', 'Jose del Carmen Pulgar S.', or 'Jose del Carmen Pulgar [?]'."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Entry 172 Pulgar/Arriagada Birth Registration

This packet stages the family-relevant Pulgar/Arriagada reading from the assigned chunk while preserving the row-level disagreement with the current converted Markdown. It should not promote to canonical claims or relationships until targeted conversion QA can inspect the original source image or full page image and certify which physical row controls entry `172`.

## Literal Support From Assigned Chunk

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | **Nombre.** Jose del Carmen Segundo Pulgar Arriagada **Sexo.** Hombre | **Fecha.** Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde **Lugar.** Calle de Valdivia | **Nombre del padre** Jose del Carmen Pulgar S. **Nac** Chileno **Prof** Empleado **Dom** Calle de Colipí **Nombre de la madre** Juana Arriagada de Pulgar **Nac** Chilena **Prof** Su sexo **Dom** Calle de Colipí | Ernesto Herrera L. Presente al nacimiento **Edad** Veintiseis años **Prof** Empleado **Dom** Calle de Valdivia
```

## Conflicting Converted Markdown Reading

The current converted Markdown on disk instead records entry `172` as `Jose Miguel`, male, born `El seis de Abril de mil ochocientos ochenta i ocho`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and informant `Oswaldo Burgos`.

## Conversion QA Status

The source manifest names a page image at `raw/codex-conversion-jobs/.../page-images/page-0001.png`, and a raw source PNG under `raw/sources/`, but neither file is present in this checkout. Existing cropped review assets under `research/_staging/conversion-review-assets/` show a Pulgar/Arriagada parent/informant section, including a father name beginning `Jose del Carmen Pulgar` and mother `Juana Arriagada de Pulgar`, but those crops do not include enough full-page context to certify the entry number by themselves.

## Promotion Recommendation

Hold for conversion QA. A proof reviewer should not promote this packet, dependent claims, or child-parent relationships until a full-image QA note certifies the controlling row for entry `172` and records the father field only to the visible level of certainty.
