---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-7d3991a78bc8-P0001-01
worker: postconv-evidence-extraction-20260523003053538
source_title: "Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172"
source_type: civil_registration_birth
source_path: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: 7d3991a78bc8f002318210ab216f0f597953a45a5c2e1dd55903ddc9e85686e3
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-09220dde10/page-0001-chunk-01.md"
chunk_id: CHUNK-7d3991a78bc8-P0001-01
chunk_manifest: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-09220dde10/manifest.json"
page_reference: "page 1; register page 58; entry 172"
entry_number: "172"
jurisdiction: "Los Angeles, Chile"
registration_date: "1888-04-07"
family_relevance: critical
matched_terms:
  - Carmen
  - Entries
  - Osorio
conversion_confidence: image_reread_conflicts_with_assigned_derivative
conversion_qa_concern: "Controller flagged qc:reread-page. The original source image was present at the expected Unicode path and was reread for register page 58, entry 172. The image supports a Pulgar/Arriagada entry, while the assigned chunk and converted file transcribe the same entry as Jose Miguel, son of Oswaldo Bunster and Amelia de la Maza. Preserve both readings until conversion QA corrects or retires the derivative transcript."
uncertainty: "Moderate for exact father suffix and informant initials; high for promotion while the assigned converted derivative remains unreconciled. The source image does not support the Bunster/de la Maza relationship candidate."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Entry 172, Image-Reviewed Pulgar/Arriagada Birth Registration Candidate

This revision stages the evidence visible in the original source image for `CHUNK-7d3991a78bc8-P0001-01`. It preserves the conflict with the assigned chunk and converted derivative, which incorrectly present entry 172 as a Bunster/de la Maza birth. This update responds to the proof-review revision requests for the staged birth-name, sex, birth date/time, birth place, child-father, child-mother, and child-parents drafts.

## Literal Support

Image reread of register page 58, entry 172:

```text
Nombres: Jose del Carmen Segundo Pulgar Arriagada
Sexo: Hombre
Fecha de inscripcion: Siete de Abril de mil ochocientos ochenta i ocho
Fecha de nacimiento: Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde
Lugar: Calle de Valdivia
Nombre del padre: Jose del Carmen Pulgar
Nac.: Chileno; Prof.: Agricultor; Dom.: Calle de Co...
Nombre de la madre: Juana Arriagada de Pulgar
Nac.: Chilena; Dom.: Calle de Co...
Compareciente: Ernesto Herrera L.; presente al nacimiento; edad veintiseis anos; prof. empleado; dom. Calle de Valdivia
Firma del oficial: Emilio Riquelme V.
```

## Evidence Scope

The source image supports draft birth-name, sex, birth date/time, birth place, registration date, parent-name, informant, residence, occupation, and registering-official claims for entry 172. Father suffix, some domicile words, and the informant's final initial remain image-sensitive.

## Conversion Confidence And QA Concern

The original source image was located and reread. Image-reviewed evidence agrees with prior Pulgar/Arriagada staging and conflicts with the assigned derivative text. Because raw converted Markdown and the assigned chunk were not changed in this task, keep all tree-impacting drafts on `hold_for_conversion_qa` until conversion QA reconciles the derivative transcript.

## Uncertainty

The child name, sex, registration date, birth date/time, birthplace, mother name, and official signature are readable enough for staging. The father is readable as `Jose del Carmen Pulgar`; a final suffix such as `S.` is not clearly visible. Some residence fields are partly unclear.

## Promotion Recommendation

Use `hold_for_conversion_qa`. Do not promote any tree claim from this packet until conversion QA records the image-reviewed correction or retires the conflicting Bunster/de la Maza derivative reading.
