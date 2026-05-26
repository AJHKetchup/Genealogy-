---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-bdb698de8106-P0001-01
worker: postconv-evidence-extraction-20260526214615021
source_packet: research/_staging/source-packets/chunk-bdb698de8106-p0001-01-entry-513-515-proof-review-revision-postconv-evidence-extraction-20260526214615021.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
source_sha256: 05d0627a58615e91315e1e9e2da567034b4f324eb0179240e0f4d5cf985e3545
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-5ed7132d63/page-0001-chunk-01.md
chunk_id: CHUNK-bdb698de8106-P0001-01
page_reference: page 1; register page 172; entries 513-515
conversion_confidence: low
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Current Worker Revision

## Revision Summary

This worker revision adds a fresh source packet, five atomic claim drafts, one relationship candidate, identity/conflict notes, and a targeted conversion-QA follow-up. It does not edit raw sources, converted Markdown, chunk Markdown, page Markdown, or canonical wiki pages.

## Promotion Blocker

Entry 513 contains high-value Pulgar evidence through the father/declarant fields, but promotion remains blocked by unresolved row-level transcription conflicts involving the child-name field and mother surname. Entry 515 remains a partial/conflicted control row and should not promote the converted `Rosa Elvira del Carmen` reading.

## Literal Support

```text
513 ... Nombre del padre. Jose del Carmen Pulgar
513 ... Nombre de la madre. Juana de Dios Amador de Pulgar
513 ... Jose del C. Pulgar; Padre; Edad. Cuarenta i siete Anos
515 ... Nombre. Rosa Elvira del Carmen
```

## Conversion Confidence / QA Concern

Low for canonical promotion. This note preserves the disagreement between derivative transcript claims and proof-review image concerns; it does not alter source text.

## Uncertainty

The declarant/father fields appear comparatively stronger than the child and mother identity fields, but the row should remain blocked until targeted conversion QA rereads the original image.

## New Staged Outputs

- `research/_staging/source-packets/chunk-bdb698de8106-p0001-01-entry-513-515-proof-review-revision-postconv-evidence-extraction-20260526214615021.md`
- `research/_staging/claims/chunk-bdb698de8106-p0001-01-513-declarant-proof-review-revision-postconv-evidence-extraction-20260526214615021.md`
- `research/_staging/claims/chunk-bdb698de8106-p0001-01-513-father-proof-review-revision-postconv-evidence-extraction-20260526214615021.md`
- `research/_staging/claims/chunk-bdb698de8106-p0001-01-513-mother-conflict-proof-review-revision-postconv-evidence-extraction-20260526214615021.md`
- `research/_staging/claims/chunk-bdb698de8106-p0001-01-513-child-name-sex-conflict-proof-review-revision-postconv-evidence-extraction-20260526214615021.md`
- `research/_staging/claims/chunk-bdb698de8106-p0001-01-515-child-name-conflict-proof-review-revision-postconv-evidence-extraction-20260526214615021.md`
- `research/_staging/relationships/chunk-bdb698de8106-p0001-01-513-child-parents-proof-review-revision-postconv-evidence-extraction-20260526214615021.md`
- `research/_staging/identity-analysis/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-postconv-evidence-extraction-20260526214615021.md`
- `research/_staging/conflicts/chunk-bdb698de8106-p0001-01-entry-513-515-conflict-candidates-proof-review-revision-postconv-evidence-extraction-20260526214615021.md`
- `research/_staging/research-tasks/chunk-bdb698de8106-p0001-01-entry-513-515-targeted-conversion-qa-proof-review-revision-postconv-evidence-extraction-20260526214615021.md`

## Recommendation

Keep all revised drafts on `hold_for_conversion_qa`. After targeted conversion QA resolves the row-level transcription conflict, rerun proof review before any canonical promotion.
