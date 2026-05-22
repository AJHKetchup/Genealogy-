---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260522085029881
task_id: proof-review:research/_staging/claims/claim-chunk-3f469b56e502-p0002-01-circulation-range.md
staged_draft: research/_staging/claims/claim-chunk-3f469b56e502-p0002-01-circulation-range.md
reviewed_source_packet: research/_staging/source-packets/sp-stage-chunk-3f469b56e502-p0002-01-league-of-nations-routing-slip.md
reviewed_chunk: raw/chunks/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25-codex/page-0002-chunk-01.md
reviewed_converted_file: raw/converted/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25.codex.md
reviewed_page_image: "unavailable at manifest path raw/codex-conversion-jobs/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25/page-images/page-0002.jpg"
canonical_readiness: hold_for_conversion_qa
claim_probability: 0.82
relevance_level: source_metadata
relevance_confidence: 0.96
source_quality_score: 0.88
conversion_confidence_score: 0.72
evidence_quantity_score: 0.70
agreement_score: 0.80
identity_confidence_score: 0.95
---

# Proof Review: Circulation Date Range

## Blockers

- The page image listed in the manifest for page 2 was not available at the expected path, so this review could not independently compare the handwriting against the visible source image.
- The conversion itself flags uncertain circulation-table readings, including `XXJ`, `1.c.v`, and `The Schwartz`; several entries are struck through. These do not defeat the broad date-range claim, but they block detailed chronology promotion.
- The conversion job manifest still lists page 2 status as `todo`, creating a provenance/QA concern even though page-markdown and chunk files exist.
- Canonical readiness is `hold_for_conversion_qa` until the rendered page image or source page is available and the first and last circulation dates are visually checked.

## Evidence Strengths

- The staged draft cites the expected converted file, source packet, and chunk for `CHUNK-3f469b56e502-P0002-01`, page 2.
- The converted chunk and page-markdown both transcribe a circulation table beginning with `m. Schwartz / Legal Dept` dated `26.5.31`.
- The same converted table transcribes later right-column entries dated `17.5.32`, `20.5.32`, `21.5.32`, and `23.5.32`, supporting the claimed terminal date of 23 May 1932 at the conversion level.
- The source packet interpretation states that the file circulated among administrative recipients from May 1931 through May 1932 and does not treat these names as genealogical identities.
- No relationship jump, person-identity conclusion, vital event, residence claim, or kinship claim is asserted by the staged draft.

## Scoring

| Factor | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | An archival file-cover routing slip is good evidence for its own administrative circulation markings, but it is not genealogical fact evidence. |
| conversion_confidence_score | 0.72 | The broad date range is internally consistent across the converted chunk and page-markdown, but the image was unavailable and the conversion flags uncertain table readings. |
| evidence_quantity_score | 0.70 | The claim rests on one page and one conversion, with multiple table entries supporting the endpoints but no independent source comparison in this review. |
| agreement_score | 0.80 | Staged claim, chunk, page-markdown, and source packet agree on the broad May 1931-May 1932 circulation range; the manifest/image-status issue prevents a higher score. |
| identity_confidence_score | 0.95 | The claim concerns the identified file cover and administrative routing entries, not an inferred person identity. |
| claim_probability | 0.82 | Probable as a broad source-circulation range based on the conversion, but held below high confidence pending visual QA. |
| relevance_level | source_metadata | The fact is useful for archival source context and file-control history. |
| relevance_confidence | 0.96 | The asserted date range is directly relevant to source circulation metadata and not to family relationships. |

## Review Judgment

The staged claim is literally supported by the converted chunk at the broad range level: the first listed circulation date is `26.5.31`, and the latest listed date is `23.5.32`. The claim should remain framed as administrative source-circulation metadata only.

Because the page image was unavailable and the conversion records unresolved uncertain readings, this should not be promoted as canonical metadata yet. It also should not be used for any genealogical identity, relationship, or biographical conclusion.

## Next Action

- Canonical readiness: `hold_for_conversion_qa`.
- Recheck page 2 against the rendered image or source PDF page and confirm the endpoint dates `26.5.31` and `23.5.32`.
- If visual QA confirms only the endpoints while other table cells remain uncertain, promote only the broad circulation range and keep detailed routing entries out of canonical notes.
