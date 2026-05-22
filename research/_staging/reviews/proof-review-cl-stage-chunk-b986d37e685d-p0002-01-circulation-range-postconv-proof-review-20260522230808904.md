---
type: proof_review
role: claim_reviewer
status: complete
task_id: proof-review:research/_staging/claims/CL-STAGE-CHUNK-b986d37e685d-P0002-01-circulation-range.md
worker: postconv-proof-review-20260522230808904
staged_draft: research/_staging/claims/CL-STAGE-CHUNK-b986d37e685d-P0002-01-circulation-range.md
reviewed_claim: CL-STAGE-CHUNK-b986d37e685d-P0002-01-circulation-range
source_packet: research/_staging/source-packets/SP-STAGE-CHUNK-b986d37e685d-P0002-01-league-of-nations-file-cover-routing-slip.md
chunk: raw/chunks/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25-codex/page-0002-chunk-01.md
converted_file: raw/converted/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25.codex.md
source: raw/sources/R3578-50-5569-5569-Jacket5.pdf
canonical_readiness: hold_for_conversion_qa
claim_probability: 0.82
source_quality_score: 0.74
conversion_confidence_score: 0.68
evidence_quantity_score: 0.76
agreement_score: 0.90
identity_confidence_score: 0.20
relevance_level: low_genealogical_relevance
relevance_confidence: 0.95
---

# Proof Review: Circulation Date Range

## Blockers

- Canonical readiness: `hold_for_conversion_qa`.
- The current converted-file SHA-256 is `88e402458471c1e4f84a77cd3c8143e25bc52f7b7a5ea897a1c02fef66089a78`, while the chunk front matter and source packet preserve the recorded converted SHA-256 as `b986d37e685d7788568baf82b8d1c6d9c92b30eda4a02450e64a28471dc92196`.
- The current chunk-file SHA-256 is `3c0874f5be388c569246e2582a5919a5fd7dc975dafaeb86d5119c7f28fe132c`, while the source packet reports the chunk manifest value as `bb0d4e7230c65a332f676aec0dd2294c5e8fa6d977c8633abdefe0e3b16f0530`.
- The claim relies on handwritten table entries. The converted chunk supports the endpoint dates, but the staged draft and source packet both preserve a page-reread/provenance QA concern.
- This is source-circulation metadata only. It should not be used to promote identity, vital-event, residence, kinship, household, or relationship claims.

## Evidence Strengths

- Literal support exists in the referenced chunk and converted file for a first dated routing entry of `26.5.31` in the row beginning `[Handwritten] IX M. Schwartz legal dept`.
- Literal support exists in the same table for a later dated routing entry of `23.5.32` with `[Handwritten] M. Walters`.
- The staged claim, source packet, chunk, and converted file agree that page 2 is a League of Nations administrative file cover/routing slip and that the relevant table records routing/circulation entries.
- The claim is narrowly scoped to the page's administrative circulation date range and does not overstate genealogical identity or relationships.

## Scoring

- `source_quality_score`: 0.74. The source is an archival administrative file cover, suitable for source-circulation metadata but not a genealogical identity source.
- `conversion_confidence_score`: 0.68. The endpoint dates are legible in the conversion, but handwritten entries and unresolved provenance/hash mismatch lower confidence.
- `evidence_quantity_score`: 0.76. Two direct table entries support the start and end dates, with multiple intervening dates supporting a 1931-1932 circulation sequence.
- `agreement_score`: 0.90. The staged claim, source packet, chunk, and converted file agree on the endpoint-date reading.
- `identity_confidence_score`: 0.20. Named people are administrative routing recipients only; no genealogical identity is established.
- `claim_probability`: 0.82. The date-range claim is probably correct at the converted-text level, pending conversion/provenance QA.
- `relevance_level`: low_genealogical_relevance.
- `relevance_confidence`: 0.95.
- `canonical_readiness`: hold_for_conversion_qa.

## Next Action

Hold for conversion/provenance QA and page reread. If the hash mismatch is reconciled and the page reread confirms the endpoint dates, the claim may be revised/promoted only as scoped source-circulation metadata, not as a person, family, relationship, or vital-event claim.
