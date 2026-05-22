---
type: conversion_review
status: draft
review_type: metadata_reconciliation
source: raw/sources/R3578-50-5569-5569-Jacket5.pdf
converted_file: raw/converted/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25.codex.md
chunk: raw/chunks/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25-codex/page-0002-chunk-01.md
chunk_id: CHUNK-b986d37e685d-P0002-01
page_reference: "page 2"
source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-b986d37e685d-P0002-01-league-of-nations-file-cover-routing-slip.md
confidence: medium
conversion_confidence: medium_high_for_source_scope_medium_for_handwritten_table
qa_concern: "Proof review found stale chunk identifiers and hash mismatches; current b986 staging still has file-hash divergence from recorded metadata."
promotion_recommendation: hold_for_conversion_qa
tags: [conversion-review, metadata-reconciliation, staging, proof-review-revision]
---

# Conversion Review Note: Metadata Reconciliation

## Finding

The current assigned chunk is `CHUNK-b986d37e685d-P0002-01`, not the older staged `CHUNK-3f469b56e502-P0002-01` identifier cited by prior drafts. This revision stages a current-id circulation-range claim but keeps it blocked for conversion/provenance QA.

## Literal Support

```text
| [Handwritten] IX M. Schwartz<br>legal dept | [Handwritten] 26.5.31 | [Handwritten] IX M. Schwartz<br>legal dept | [Handwritten] 19.10.31 | [Handwritten] Disarmament | [Handwritten] 1.4.32 |
```

```text
| [Handwritten] M. Schwartz<br>legal dept | [Handwritten] 2.7.31 | [Handwritten] X+I M. Schwartz<br>legal dept | [Handwritten] 29.12.31 | [Handwritten] M. Walters | [Handwritten] 23.5.32 |
```

## Source Path

- Source path: `raw/sources/R3578-50-5569-5569-Jacket5.pdf`
- Converted file: `raw/converted/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25.codex.md`
- Chunk/page reference: `CHUNK-b986d37e685d-P0002-01`, page 2.

## Conversion Confidence And QA Concern

The broad source scope and endpoint dates are supported at the converted-text level. The current converted-file SHA-256 is `88e402458471c1e4f84a77cd3c8143e25bc52f7b7a5ea897a1c02fef66089a78`, while recorded metadata still includes `b986d37e685d7788568baf82b8d1c6d9c92b30eda4a02450e64a28471dc92196`. The current chunk-file SHA-256 is `3c0874f5be388c569246e2582a5919a5fd7dc975dafaeb86d5119c7f28fe132c`, while the chunk manifest records `bb0d4e7230c65a332f676aec0dd2294c5e8fa6d977c8633abdefe0e3b16f0530`.

The page also remains subject to the controller `reread-page` action because handwritten routing names and initials include uncertain readings.

## Uncertainty

This note does not alter source text and does not create genealogical identity or relationship evidence. It preserves the disagreement between older derivative staging metadata and the current assigned chunk/provenance state.

## Promotion Recommendation

Hold for conversion/provenance QA. After reconciliation, any promotion should be limited to source-circulation metadata and must not infer genealogical identity or relationship.
