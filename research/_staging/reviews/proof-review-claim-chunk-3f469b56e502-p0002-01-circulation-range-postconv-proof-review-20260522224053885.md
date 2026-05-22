---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/claims/claim-chunk-3f469b56e502-p0002-01-circulation-range.md
staged_draft: research/_staging/claims/claim-chunk-3f469b56e502-p0002-01-circulation-range.md
reviewer: postconv-proof-review-20260522224053885
review_date: 2026-05-22
canonical_readiness: hold_for_metadata_reconciliation
---

# Proof Review: Circulation Date Range

## Blockers

- The staged draft and source packet identify the chunk as `CHUNK-3f469b56e502-P0002-01`, but the referenced chunk file front matter identifies itself as `CHUNK-b986d37e685d-P0002-01`.
- The referenced chunk file's current SHA-256 is `3c0874f5be388c569246e2582a5919a5fd7dc975dafaeb86d5119c7f28fe132c`, which does not match the chunk front matter `converted_sha256` value `b986d37e685d7788568baf82b8d1c6d9c92b30eda4a02450e64a28471dc92196`.
- The referenced converted file's current SHA-256 is `88e402458471c1e4f84a77cd3c8143e25bc52f7b7a5ea897a1c02fef66089a78`, which does not match the source packet's `converted_sha256` value `3f469b56e5024d7d0328377f23de9b911d9cfe6353b581c4f564b96ca15981f2`.
- The claim is source-administrative metadata only. It does not support a genealogical person identity, vital event, kinship, household membership, or relationship.

## Scores

- source_quality_score: 0.78
- conversion_confidence_score: 0.72
- evidence_quantity_score: 0.66
- agreement_score: 0.86
- identity_confidence_score: 0.20
- claim_probability: 0.88
- relevance_level: low
- relevance_confidence: 0.92
- canonical_readiness: hold_for_metadata_reconciliation

## Claim Review

| Claim | Judgment | Claim probability | Notes |
| --- | --- | ---: | --- |
| The page records administrative circulation entries dated from 26 May 1931 through 23 May 1932. | supported_but_hold_for_metadata_reconciliation | 0.88 | The converted page text, chunk transcription, and restored page image support the visible endpoint dates `26.5.31` and `23.5.32` in the routing table. Promotion should wait for chunk identifier/hash reconciliation. |

## Evidence Strengths

- The referenced source is an archival League of Nations registry file cover/routing slip, appropriate for source-circulation metadata.
- The source PDF hash matches the packet and chunk metadata: `09a9828166381d0dbd9fe5fbfebb432548bf6f216d51556bdf77fe23dcce018f`.
- The converted Markdown at `raw/converted/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25.codex.md` records the first relevant dated entry as `26.5.31` and the last visible dated entry in the routing table as `23.5.32`.
- The chunk at `raw/chunks/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25-codex/page-0002-chunk-01.md` records the same endpoint dates.
- The restored page image at `raw/codex-conversion-jobs/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25/page-images/page-0002.jpg` visibly supports `26.5.31` near the beginning of the table and `23.5.32` near the right-column lower portion.
- No conflicting earlier or later date was found in the staged draft, source packet, referenced chunk, converted page text, or checked page image.

## Review Judgment

The narrow circulation-range claim is probably correct as source-administrative metadata. The dates are visible enough to support the range from 26 May 1931 through 23 May 1932, but the conflicting chunk identifiers and stale hash metadata make the item unsuitable for canonical promotion as-is.

## Next Action

Hold for metadata/conversion QA to reconcile the staged draft, source packet, chunk identifier, and current file hashes. After reconciliation, promote only as scoped source-circulation metadata, with no inferred genealogical identity or relationship.
