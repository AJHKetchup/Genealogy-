---
type: source_packet
status: draft
task_id: "evidence-extraction:CHUNK-b8f4f0490a36-P0001-01"
worker: "postconv-evidence-extraction-20260527020704452"
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
family_relevance: "high"
matched_terms:
  - "Arriagada"
  - "Pulgar"
conversion_confidence: "mixed_derivative_conflict_image_reviewed"
conversion_qa_concern: "The assigned chunk and direct source-image review support the Pulgar/Arriagada physical row for entry 172, but the current converted Markdown records a different Burgos/de la Cruz entry 172. The father field is visible as Jose del Carmen Pulgar; a terminal suffix is not certified from this review."
uncertainty: "Low that the visible physical row for entry 172 is Pulgar/Arriagada; moderate for the father's terminal mark or suffix; high for canonical promotion until proof review accepts the row-control QA and the stale or row-shifted converted Markdown is reconciled."
promotion_recommendation: "hold_for_conversion_qa"
---

# Source Packet: Entry 172 Pulgar/Arriagada Birth Registration

This source packet stages the person-first evidence for `Jose del Carmen Segundo Pulgar Arriagada`, whose birth registration appears as physical entry `172` on register page 58 of the Los Angeles civil birth register. The relevant family entities are the child, father `Jose del Carmen Pulgar`, and mother `Juana Arriagada de Pulgar`.

## Literal Support

Assigned chunk support:

```text
| 172 | Siete de Abril de mil ochocientos ochenta i ocho | **Nombre.** Jose del Carmen Segundo Pulgar Arriagada **Sexo.** Hombre | **Fecha.** Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde **Lugar.** Calle de Valdivia | **Nombre del padre** Jose del Carmen Pulgar S. **Nac** Chileno **Prof** Empleado **Dom** Calle de Colipí **Nombre de la madre** Juana Arriagada de Pulgar **Nac** Chilena **Prof** Su sexo **Dom** Calle de Colipí | Ernesto Herrera L. Presente al nacimiento **Edad** Veintiseis años **Prof** Empleado **Dom** Calle de Valdivia | **Por los testigos:** --- **Conocido del oficial.** | [signature] Emilio Riquelme V. | |
```

Conflicting current converted Markdown support:

```text
Entry 172: Nombres. Jose Miguel; father Oswaldo Burgos; mother Concepcion de la Cruz; born El seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche.
```

Direct image review for this revision found that the physical row numbered `172` on the left page is the Pulgar/Arriagada row. The child name, sex, registration date, birth date/time, birth place, mother name, informant, and official signature agree with the assigned chunk. The father field is bounded here to `Jose del Carmen Pulgar`; the assigned chunk's final `S.` is not certified from the image review.

## Extracted Family Evidence

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Birth date/time: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`.
- Birth place: `Calle de Valdivia`.
- Father field: `Jose del Carmen Pulgar`; suffix unresolved.
- Mother field: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at the birth, age 26, employed, resident on Calle de Valdivia.

## QA And Promotion Boundary

This packet preserves the disagreement between derivative transcripts and image-reviewed evidence. It does not edit raw sources, the current converted Markdown, the chunk, or page Markdown. Keep tree-impacting claims and relationship candidates on `hold_for_conversion_qa` until proof review accepts the targeted QA note or conversion-control updates the derivative Markdown.
