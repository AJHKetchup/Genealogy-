---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530222647546
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530211859579.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530211859579.md"
source_packet: "research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-work-history.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
conversion_job_page_markdown: "raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md"
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
canonical_readiness: hold_not_ready
---

# Proof Review: Page 5 Control Conflict

## Blockers First

1. Keep the staged draft on hold. The reviewed evidence supports a conversion/provenance conflict, not a promotion-ready identity or relationship claim.
2. The assigned chunk and source packet transcribe 1979-1982 through 1970-1972 work-history entries for page 5, while the conversion job page Markdown for page 5 transcribes 1999, 1998-1999, and 1997-1998 entries. These derivative texts cannot both control the same page.
3. The chunk manifest lists `CHUNK-fb0a0000636f-P0005-01` twice for page 5 with different character counts and SHA-256 values, so the chunk provenance is unstable.
4. The conversion job manifest references `page-images/page-0005.jpg`, but that image file is not present at the referenced path. I could not verify the true page-5 text visually.
5. Neither disputed page-5 derivative body repeats the subject name. The CV title and file/job metadata support only document-level attribution to `Dario Arturo Pulgar`.
6. The reviewed materials contain no birth, parent, spouse, child, household, or other kinship statement. No Pulgar-line merge, parent candidate, or relationship conclusion is supported by this item.

## Evidence Strengths

- The staged draft is literally supported in its main conclusion: page 5 has a controlling transcription dispute and should remain `hold_for_conversion_qa`.
- The source packet correctly reports blocked conversion confidence and describes the same 1979-1970 versus 1999/1998 derivative conflict.
- The assigned chunk is internally legible for the 1979-1970 work-history sequence.
- The conversion job page Markdown is internally legible for the 1999/1998 work-history sequence.
- The aggregate converted file contains both disputed text families within the converted page range, corroborating the staged draft's provenance concern.
- The staged draft appropriately avoids canonical promotion and does not treat document-level `Dario Arturo Pulgar` metadata as proof of identity with any canonical person.

## Scored Judgment

| Metric | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 5/10 | The underlying source is a named CV packet, but the visible page-control source is unavailable. |
| conversion_confidence_score | 3/10 | Two local derivatives disagree materially and the referenced page image is missing. |
| evidence_quantity_score | 4/10 | Multiple derivatives were available, but they conflict rather than accumulate into proof. |
| agreement_score | 2/10 | Low agreement on page-5 content; high agreement only that a conflict exists. |
| identity_confidence_score | 6/10 | Moderate for document-level `Dario Arturo Pulgar`; low for any page-local or canonical identity attachment. |
| claim_probability | 0.88 | High probability that the staged draft correctly identifies a page-control conflict; 0.50 or lower for either transcription as controlling without image/source-page QA; 0.05 for any relationship claim. |
| relevance_level | high | Directly reviews the assigned staged identity/conflict draft. |
| relevance_confidence | 0.96 | The checked files are the draft's cited derivatives and manifests. |
| canonical_readiness | hold_not_ready | No canonical claim should be promoted until page control is resolved. |

## Review Finding

The staged draft is supported as a hold recommendation. It correctly treats the item as a conversion control conflict: chunk/source-packet evidence supports one page-5 transcription family, while the conversion job page Markdown supports another. Because the referenced page image is missing, proof review cannot certify which text controls the true page 5.

The draft should not be used to promote occupational claims, same-person claims, name-variant claims, or relationship claims. Any identity use remains limited to a cautious document-level subject label from the CV title/source metadata.

## Next Action

Keep `canonical_readiness` at `hold_not_ready`. Conversion QA should restore or regenerate `page-images/page-0005.jpg` or otherwise compare the actual source page against both derivative transcriptions, repair the duplicate page-5 chunk manifest state, and regenerate stale derivative outputs before proof review reruns.
