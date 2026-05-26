---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-bdb698de8106-P0001-01
worker: postconv-evidence-extraction-20260526061757672
source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
source_sha256: 05d0627a58615e91315e1e9e2da567034b4f324eb0179240e0f4d5cf985e3545
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
chunk_id: CHUNK-bdb698de8106-P0001-01
page_reference: page 1; register page 172; entries 513-515
family_relevance: high
matched_family_terms: ["Pulgar"]
conversion_confidence: low
promotion_recommendation: hold_for_conversion_qa
---

# Evidence Extraction Closure Note: CHUNK-bdb698de8106-P0001-01

## Scope

This revision reviewed the restored bdb chunk and existing staged source packet, atomic claims, relationship candidates, conflict notes, identity analysis, and conversion-QA tasks for page 172, entries 513-515. No raw source, converted Markdown, chunk Markdown, page Markdown, or canonical wiki page was edited.

## Staged Evidence State

The current bdb staged outputs cite the correct restored chunk path and chunk id:

- Source packet: `research/_staging/source-packets/SP-STAGE-CHUNK-bdb698de8106-P0001-01-los-angeles-birth-register-1889-page-172.md`
- Atomic claims: `research/_staging/claims/CL-STAGE-CHUNK-bdb698de8106-P0001-01-*.md`
- Relationship candidates: `research/_staging/relationships/REL-STAGE-CHUNK-bdb698de8106-P0001-01-*.md`
- Conflict note: `research/_staging/conflicts/CONFLICT-STAGE-CHUNK-bdb698de8106-P0001-01-qa-candidates.md`
- Identity analysis: `research/_staging/identity-analysis/identity-analysis-id-stage-chunk-bdb698de8106-p0001-01-identity-candidates.md`
- Conversion-QA follow-up: `research/_staging/tasks/task-chunk-bdb698de8106-p0001-01-conversion-qa-followup-revision-20260526.md`

The atomic claim and relationship frontmatter includes the required source path, converted file, chunk reference, chunk id, page reference, confidence, and promotion recommendation fields.

## Literal Family-Relevant Support

The derivative transcript for entry 513 contains the family-relevant Pulgar evidence:

```text
Nombre del padre.
José del Carmen Pulgar
Nombre de la madre.
Juana de Dios Amador de Pulgar
José del C. Pulgar
Padre
Edad. Cuarenta i siete Años
Prof. Agricultor
Dom. Calle Colon
```

## QA Blocker

These drafts remain blocked because the derivative transcript and image-reviewed evidence disagree on identity-controlling fields. Entry 513 child name and mother surname are unresolved; entry 513 declarant evidence is stronger but still belongs to the same row-level conflict; entry 515 is partial and conflicts with the converted name/father readings. These disagreements must be preserved rather than resolved by inference.

## Promotion Recommendation

Keep all current bdb entry 513-515 source packet, claim, relationship, conflict, and identity drafts at `hold_for_conversion_qa`. After targeted conversion QA produces a corrected row-level transcription, rerun proof review on separate atomic claims before any canonical promotion, merge, rename, or tree attachment.
