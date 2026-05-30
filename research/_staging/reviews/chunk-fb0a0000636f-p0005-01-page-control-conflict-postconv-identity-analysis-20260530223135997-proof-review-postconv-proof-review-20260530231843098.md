---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530231843098
task_id: "proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530223135997.md"
staged_draft: "research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530223135997.md"
source_packet: "research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-work-history-hold-postconv-evidence-extraction-20260530213419489.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
canonical_readiness: not_ready
---

# Proof Review: Page-Control Conflict For CV Page 5

## Blockers First

1. Keep this item on hold. The assigned chunk and aggregate converted file show a 1979-1982 / 1974-1978 / 1972-1973 / 1970-1972 work-history sequence, while the conversion job `page-markdown/page-0005.md` shows 1999 / 1998-1999 / 1997-1998 entries. These cannot both be the controlling page-5 transcription.
2. The rendered page image needed for visual proof review is unavailable in this checkout. The job manifest references `page-images/page-0005.jpg`, but the `page-images` directory/file is absent locally.
3. The chunk manifest has duplicate `CHUNK-fb0a0000636f-P0005-01` entries with different character counts and hashes. The source packet also records a mismatch between the converted SHA-256 recorded in the chunk metadata and the observed converted file hash.
4. The page body does not repeat the full name `Dario Arturo Pulgar`; identity attachment is document-level context from the CV title/source packet, not a page-local identity statement.
5. No family relationship is supported. The checked materials contain no parent, spouse, child, sibling, household, or descendant statement for this page.

## Evidence Strengths

- The assigned chunk is readable and internally coherent as a CV work-history page, listing HABITAT, National Film Board of Canada, Chile Films, CITELCO, and an `EDUCATION` heading.
- The aggregate converted file currently includes the same 1979-1970 page content found in the assigned chunk.
- The source packet accurately flags the derivative-text conflict, missing image, hash mismatch, and relationship boundary.
- The conversion job page Markdown is also readable and internally coherent as a CV work-history page, but it supports materially different 1999/1998 work-history claims.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 5/10 for the CV as a self-authored career source; reduced because the source image was not available for this review |
| conversion_confidence_score | 2/10 due to direct page-control conflict, missing page image, duplicate chunk manifest entries, and hash mismatch |
| evidence_quantity_score | 3/10 for identity or relationship claims; 5/10 for narrow work-history text after page control is repaired |
| agreement_score | 2/10 across derivative sources for page 5; 8/10 only between the assigned chunk and aggregate converted file |
| identity_confidence_score | 6/10 for document-level `Dario Arturo Pulgar`; 2/10 or lower for any canonical merge or family bridge |
| claim_probability | 0.55 that the assigned chunk may represent a real page from the CV, but 0.20 for accepting it as page 5 without conversion QA; 0.05 for any relationship claim |
| relevance_level | high for Pulgar-line CV/work-history context; low for relationship proof |
| relevance_confidence | 0.80 for CV/work-history relevance; 0.15 for genealogical relationship relevance |
| canonical_readiness | not_ready |

## Review Finding

The staged draft is supported as a hold-for-conversion-QA item. The visible local materials support the existence of a serious derivative page-control conflict, but they do not support choosing either page-5 transcription as controlling. Because the image is missing, this review cannot visually confirm whether page 5 should contain the 1999/1998 consultant sequence or the 1979-1970 HABITAT/NFB/Chile Films/CITELCO sequence.

No checked source text supports changing the subject's name, expanding it to a different Pulgar identity, merging it with a canonical person, or attaching Jose/Juana parent candidates. Any such step would exceed the page evidence.

## Next Action

Run conversion QA before any claim or canonical promotion. The QA worker should restore or regenerate `page-images/page-0005.jpg`, repair the duplicate chunk manifest/hash state, and certify the controlling page-5 transcription. After that, rerun proof review against the certified page text. Until then, keep work-history, identity-bridge, relationship, and canonical wiki actions on hold.
