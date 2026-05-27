---
type: research_task
status: draft
task_id: evidence-extraction:CHUNK-bdb698de8106-P0001-01
worker: postconv-evidence-extraction-20260527045039396
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png"
source_sha256: 05d0627a58615e91315e1e9e2da567034b4f324eb0179240e0f4d5cf985e3545
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
chunk_id: CHUNK-bdb698de8106-P0001-01
source_packet: research/_staging/source-packets/chunk-bdb698de8106-p0001-01-entry-513-515-proof-review-revision-postconv-evidence-extraction-20260527045039396.md
page_reference: page 1; register page 172; entries 513-515
priority: high
family_relevance: high
matched_family_terms: [Pulgar]
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Follow-Up: Entry 513 Pulgar Row

## Task

Create a targeted conversion-review correction note for entry 513 from the original image. Confirm or correct the child full name, sex, birth date/time/place, father/declarant name, father age/profession/domicile, and mother full name/surname.

## Current Image-Review Findings To Check

- Child name appears to begin `Pulgar Rosa ...`; following given-name lines are uncertain. Converted `Isolina del Carmen / Jose` is not supported by this review.
- Sex appears to read `Masculino`.
- Birth field appears to read `Junio veinte i dos ... a las cuatro i media de tarde`, conflicting with converted `El mismo veinte dos ... a las cuatro de la mañana`.
- Father/declarant fields appear to read `Jose del Carmen Pulgar` / `Jose del C. Pulgar`, `Padre`, `Agricultor`, `Calle Colon`.
- Mother appears to read `Juana de Dios Ama[?]gar` or `Ama[?]gada de Pulgar`, not securely `Amador`.
- Entry 515 should be reconciled only enough to confirm it is a separate non-Pulgar row.

## Acceptance Criteria

- Preserve unresolved words with explicit uncertainty markers instead of normalizing from context.
- State whether the converted child name `Isolina del Carmen Jose` is supported, corrected, or unresolved.
- State whether the converted mother name `Juana de Dios Amador de Pulgar` is supported, corrected, or unresolved.
- State whether the birth month/time is `Junio ... cuatro i media de tarde`, converted `El mismo ... cuatro de la mañana`, or unresolved.
- Return these staged claims for proof review after conversion QA; do not promote directly.

## Promotion Recommendation

`hold_for_conversion_qa`.
