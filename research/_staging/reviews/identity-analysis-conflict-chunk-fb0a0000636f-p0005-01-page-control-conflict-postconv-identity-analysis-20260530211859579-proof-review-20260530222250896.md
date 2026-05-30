---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530222157791
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530211859579.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530211859579.md"
source_packet: "research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-work-history.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
conversion_job_page_markdown: "raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md"
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
canonical_readiness: hold
---

# Proof Review: Page 5 CV Control Conflict

## Blockers First

1. Keep this item on hold. The staged draft is supported as a conversion/provenance conflict, but neither derivative transcription can be treated as controlling page 5 without restored or inspected page-image/source-page control.
2. The assigned chunk and source packet support 1979-1982 through 1970-1972 work-history entries, while the conversion job page Markdown for page 5 supports 1999, 1998-1999, and 1997-1998 entries. These cannot both be the same page-5 transcription.
3. The chunk manifest lists `CHUNK-fb0a0000636f-P0005-01` twice for page 5 with different character counts and SHA-256 values, matching the staged draft's provenance concern.
4. The conversion job manifest references `page-images/page-0005.jpg`, but the `page-images` directory was not present during review, so visual source control could not be checked.
5. No reviewed page-5 derivative body states a birth, parent, spouse, child, household, or other relationship. No same-person merge or relationship claim is supported from this staged draft.
6. The CV title/source metadata support only a document-level subject label of `Dario Arturo Pulgar`; they do not prove that the CV subject is canonical `Dario Arturo Pulgar-Smith` or any Pulgar-Arriagada candidate.

## Evidence Strengths

- The staged identity/conflict analysis accurately identifies the central issue as a derivative transcription page-control conflict rather than a genealogical fact conflict.
- The source packet explicitly marks conversion confidence as blocked and recommends holding for conversion QA.
- The assigned chunk is internally legible for the 1979-1970 sequence, and the conversion job page Markdown is internally legible for the 1999-1997 sequence; the defect is provenance/page control, not ordinary illegibility.
- The conversion job manifest maps page 5 to `page-markdown/page-0005.md` and the absent `page-images/page-0005.jpg`, while the chunk manifest duplicates page-5 chunk metadata. This gives concrete support for the staged draft's hold recommendation.
- The staged draft correctly avoids promoting occupational, identity-bridge, or family-relationship claims to canonical pages.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 5/10 |
| conversion_confidence_score | 3/10 |
| evidence_quantity_score | 4/10 |
| agreement_score | 2/10 for page-control agreement; 8/10 that a conflict exists |
| identity_confidence_score | 6/10 for document-level `Dario Arturo Pulgar`; 4/10 or lower for attachment to canonical `Dario Arturo Pulgar-Smith`; 1/10 for any parent/relationship claim |
| claim_probability | 0.88 that the staged item correctly identifies a page-control conflict; 0.50 or lower for either disputed page-5 transcription as controlling; 0.10 for any relationship claim |
| relevance_level | high |
| relevance_confidence | 0.95 |
| canonical_readiness | hold / not_ready |

## Review Finding

The staged draft is literally supported as a hold-for-conversion-QA analysis. The conflict is visible in local derivatives: the assigned chunk/source packet contain the 1979-1970 work-history block, while the page-specific conversion Markdown contains the 1999-1997 work-history block. The aggregate converted file also contains both content families in the page range, and the chunk manifest has duplicate page-5 entries with different hashes.

The review cannot certify either transcription as the true page 5 because the referenced page image was unavailable in the workspace. This limitation lowers conversion confidence but strengthens the hold recommendation.

## Next Action

Keep `canonical_readiness` as `hold` / `not_ready`. Conversion QA should restore or regenerate the page image/source-page control, compare actual page 5 against the two derivative text blocks, repair duplicate chunk manifest state, and regenerate stale derivatives before proof review reruns. Do not promote any occupational, same-person, or relationship claim from this item until that page-control issue is resolved.
