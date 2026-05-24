---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-b8f4f0490a36-P0001-01
worker: postconv-evidence-extraction-20260524140648224
source_title: "Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172"
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
  - Pulgar
  - Arriagada
conversion_confidence: mixed
conversion_qa_concern: "The page image and assigned chunk support a Pulgar/Arriagada entry 172, but the assigned converted Markdown still gives a materially different Gomez/de la Maza entry 172. The father's exact field remains unresolved between Jose del Carmen Pulgar, Jose del Carmen Pulgar S., or an uncertain suffix."
uncertainty: "High for canonical promotion because the controlling derivative transcript is unreconciled; moderate for the father's exact recorded suffix; low that the visible row is family-relevant Pulgar/Arriagada."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Entry 172 Pulgar/Arriagada Birth Registration

Known family members and relationships in this source packet center on the Pulgar/Arriagada child-parent cluster. The page image and assigned chunk support a birth registration for `Jose del Carmen Segundo Pulgar Arriagada`, with parents recorded as `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`.

This packet is not promotion-ready because the assigned converted Markdown for the same chunk and entry number gives a different row: child `Jose Francisco`, father `Oswaldo Gomez`, and mother `Rosario de la Cruz de la Maza`, with Pellin birth/residence details. That is a row-level conflict, not a spelling variant.

## Literal Support From Assigned Chunk

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | **Nombre.** Jose del Carmen Segundo Pulgar Arriagada **Sexo.** Hombre | **Fecha.** Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde **Lugar.** Calle de Valdivia | **Nombre del padre** Jose del Carmen Pulgar S. **Nac** Chileno **Prof** Empleado **Dom** Calle de Colipí **Nombre de la madre** Juana Arriagada de Pulgar **Nac** Chilena **Prof** Su sexo **Dom** Calle de Colipí | Ernesto Herrera L. Presente al nacimiento **Edad** Veintiseis años **Prof** Empleado **Dom** Calle de Valdivia | **Por los testigos:** --- **Conocido del oficial.** | [signature] Emilio Riquelme V. | |
```

## Image-Reviewed Evidence

Direct visual review of the source image confirms that page 58, entry 172 is the Pulgar/Arriagada row, not the Gomez/de la Maza row in the assigned converted Markdown. The image supports the child name, sex, registration date, birth date/time, birth place, mother, informant, and broad father reading. The final father-name suffix is not sufficiently settled for canonical use from this extraction.

## Promotion Blocker

Keep this source packet and all dependent claims at `hold_for_conversion_qa` until targeted conversion QA corrects or supersedes the converted Markdown and explicitly records whether the father field reads `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or an uncertain form.
