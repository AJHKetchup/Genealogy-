---
type: research_task
status: draft
task_id: evidence-extraction:CHUNK-bdb698de8106-P0001-01
worker: postconv-evidence-extraction-20260526214615021
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
source_sha256: 05d0627a58615e91315e1e9e2da567034b4f324eb0179240e0f4d5cf985e3545
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
chunk_id: CHUNK-bdb698de8106-P0001-01
source_packet: research/_staging/source-packets/chunk-bdb698de8106-p0001-01-entry-513-515-proof-review-revision-postconv-evidence-extraction-20260526214615021.md
page_reference: page 1; register page 172; entries 513 and 515
priority: high
family_relevance: high
matched_family_terms: [Pulgar]
promotion_recommendation: hold_for_conversion_qa
---

# Targeted Conversion QA Follow-Up: Entries 513 And 515

## Task

Reread the original page image against the converted transcript for entry 513 and the partial entry 515. Preserve uncertainty explicitly rather than replacing the transcript from inference.

## Literal Support

```text
513 ... Jose del Carmen Pulgar ... Juana de Dios Amador de Pulgar ... Jose del C. Pulgar
515 ... Rosa Elvira del Carmen
```

## Conversion Confidence / QA Concern

Low for canonical promotion. Prior proof review found that row-level image evidence and the derivative transcript disagree in identity-controlling fields.

## Uncertainty

This task is a QA instruction, not a corrected transcription. It should not be used to promote a child name, mother identity, or parent-child link.

## Acceptance Criteria

- For entry 513, confirm, correct, or mark unresolved the child full name, sex, birth date/time/place, father/declarant name, father age/profession/domicile, and mother full name.
- State whether `Jose del C. Pulgar` in the declarant field is supported as the same-row father/declarant if the father field remains `Jose del Carmen Pulgar`.
- State whether the converted mother name `Juana de Dios Amador de Pulgar` is supported, corrected, or unresolved.
- For entry 515, state whether the converted `Rosa Elvira del Carmen` reading is supported, corrected, or unresolved from the partial row.
- Return any corrected claims to proof review before canonical promotion.

## Why It Matters

Entry 513 is high-relevance Pulgar evidence, but unresolved row transcription blocks a family-tree child identity and parent-child relationship.

## Promotion Recommendation

`hold_for_conversion_qa`.
