---
type: research_task
status: draft
task_id: evidence-extraction:CHUNK-3d3ab761209f-P0001-01
worker: postconv-evidence-extraction-20260526233712415
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png"
source_sha256: "05d0627a58615e91315e1e9e2da567034b4f324eb0179240e0f4d5cf985e3545"
converted_file: "raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md"
chunk: "raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-3d3ab761209f-P0001-01"
source_packet: "research/_staging/source-packets/chunk-3d3ab761209f-p0001-01-entry-513-pulgar-hold-postconv-evidence-extraction-20260526233712415.md"
page_reference: "image page 1; register page 172; entries 513-515"
priority: high
family_relevance: high
matched_family_terms: ["Pulgar"]
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Follow-Up: Entry 513 Pulgar Row

## Task

Run targeted row-level conversion QA against the original image, converted Markdown, and assigned chunk for register page 172, entry 513. Use entries 514 and 515 only as row-control context.

## Acceptance Criteria

- Confirm or correct entry 513 child full name, preserving uncertain letters with brackets rather than normalizing.
- Confirm child sex.
- Confirm birth date and time, specifically the day and whether the time is `cuatro`, `cuatro i media`, `manana`, or `tarde`.
- Confirm the exact mother surname: `Amagada`, `Amador`, `Arriagada`, or explicitly uncertain.
- Confirm father/declarant wording, age, occupation, and residence.
- Reconcile entry 515 only enough to prevent lower-row spillover into entry 513.

## Promotion Recommendation

`hold_for_conversion_qa`. After QA, rerun proof review on the atomic child identity, birth-event, father/declarant, mother, and parent-child relationship candidates before any canonical promotion.
