---
type: source_packet
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260527045037624"
source_title: "Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172"
source_type: "civil_registration_birth"
source_path: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_sha256: "aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
converted_sha256: "b8f4f0490a36d838c04400174e89d8c22b73e59109785c89dcb0fe13b095013f"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
chunk_manifest: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/manifest.json"
page_reference: "page 1; register page 58; physical row entry 172"
entry_number: "172"
family_relevance: high
matched_terms:
  - Pulgar
  - Arriagada
conversion_confidence: "mixed_derivative_conflict_image_reviewed"
conversion_qa_concern: "Direct image review and the assigned chunk support physical row 172 as the Pulgar/Arriagada birth registration. The current converted Markdown records a different Burgos/de la Cruz entry 172. The father field is preserved only to the visible certified reading: Jose del Carmen Pulgar; any terminal suffix after Pulgar remains unresolved."
uncertainty: "Low for physical row control and core Pulgar/Arriagada row assignment; moderate for the father field's terminal suffix and some residence-field diacritics/spelling; high for promotion because derivative Markdown still conflicts."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet: Entry 172 Pulgar/Arriagada Birth Registration

This packet stages family-relevant evidence from the visible physical row numbered `172` on register page 58. The row concerns `Jose del Carmen Segundo Pulgar Arriagada`.

## Literal Support

Assigned chunk:

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | **Nombre.** Jose del Carmen Segundo Pulgar Arriagada **Sexo.** Hombre | **Fecha.** Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde **Lugar.** Calle de Valdivia | **Nombre del padre** Jose del Carmen Pulgar S. **Nac** Chileno **Prof** Empleado **Dom** Calle de Colipí **Nombre de la madre** Juana Arriagada de Pulgar **Nac** Chilena **Prof** Su sexo **Dom** Calle de Colipí | Ernesto Herrera L. Presente al nacimiento **Edad** Veintiseis años **Prof** Empleado **Dom** Calle de Valdivia | **Por los testigos:** --- **Conocido del oficial.** | [signature] Emilio Riquelme V. | |
```

Conflicting current converted Markdown:

```text
Entry 172: Nombres. Jose Miguel; father Oswaldo Burgos; mother Concepcion de la Cruz; born El seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche.
```

Direct image review for this worker confirms that the visible physical row numbered `172` on the left page/register page 58 is the Pulgar/Arriagada row, not the Burgos/de la Cruz row. The father field is readable to `Jose del Carmen Pulgar`; a possible terminal suffix or mark after `Pulgar` is not certified here.

## Person-First Evidence

- Child/family subject: `Jose del Carmen Segundo Pulgar Arriagada`.
- Father field: `Jose del Carmen Pulgar`; suffix unresolved.
- Mother field: `Juana Arriagada de Pulgar`.
- Birth event: 8 March 1888, about 3 p.m., Calle de Valdivia.
- Registration event: 7 April 1888, Los Angeles civil birth register, entry 172.
- Informant: `Ernesto Herrera L.`, recorded as present at the birth, age 26, employed, resident on Calle de Valdivia.

## Promotion Boundary

Do not promote this source packet, claim drafts, relationship candidates, identity merges, Dario-line attachments, or wiki updates until proof review accepts the row-control finding or conversion-control reconciles the derivative Markdown conflict.
