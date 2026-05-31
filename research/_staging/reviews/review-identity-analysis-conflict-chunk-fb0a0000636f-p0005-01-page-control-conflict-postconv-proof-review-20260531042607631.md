---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531003857892.md
worker: postconv-proof-review-20260531042607631
staged_draft: research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531003857892.md
reviewed_source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-hold-postconv-evidence-extraction-20260530234356813.md
reviewed_chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
reviewed_converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
reviewed_page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
source: raw/sources/CV of Dario Arturo Pulgar.pdf
chunk_id: CHUNK-fb0a0000636f-P0005-01
review_status: hold
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Page 5 CV Identity/Control Conflict

## Blockers

- Hold the staged draft. The central page-control conflict is supported: the assigned chunk for `CHUNK-fb0a0000636f-P0005-01` contains the 1979-1982 HABITAT through 1970-1972 CITELCO work-history text, while `page-markdown/page-0005.md` contains the 1999 PROFONANPE/TVE through 1997-1998 Klohn Crippen/SNC Lavalin consulting text.
- Do not promote either page-5 work-history sequence. The physical page image `page-images/page-0005.jpg` and extracted image `extracted-images/page-0005.jpg` were not present in this workspace pass, so no visible source page was available to certify which derivative controls physical page 5.
- Revise/qualify one literal-support detail in the staged identity analysis before any downstream use: it says the assigned chunk/current aggregate converted file support the 1979-1982 through 1970-1972 page. Current inspection of the aggregate converted file shows its page-5 section contains the 1999 PROFONANPE text, while the 1979 HABITAT text appears later under page-9 metadata. This strengthens the hash/page-control concern but makes the phrase "current aggregate converted file" stale or inaccurate.
- The chunk manifest duplicates `CHUNK-fb0a0000636f-P0005-01` with conflicting character counts and recorded hashes, and observed file hashes do not match the recorded chunk/converted hashes. This prevents using the derivative files as stable proof.
- Page-local identity support is weak. The source title and derivative metadata name `CV of Dario Arturo Pulgar.pdf`, but the page-5 body itself does not restate a full personal name or any family relationship.
- No relationship claim is supported. Neither competing page-5 text names a parent, spouse, child, grandchild, Jose/Juana candidate, `Pulgar-Smith`, or `Pulgar-Arriagada`.

## Evidence Strengths

- The draft correctly treats identity as a scored judgment and keeps the strongest support at document-title/source-context level rather than page-local proof.
- The source packet literally records the conversion concern, missing page images, hash drift, and `hold_for_conversion_qa` recommendation.
- The assigned chunk literally supports the HABITAT/NFB/Chile Films/CITELCO sequence if and only if later QA certifies that chunk as the controlling physical page.
- The page Markdown and current aggregate page-5 section literally support the PROFONANPE/TVE/Arca/Klohn Crippen/SNC Lavalin sequence if and only if later QA certifies that page as controlling.
- The staged draft's anti-conflation cautions are appropriate: this page-control conflict alone cannot merge `Dario Arturo Pulgar` with `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Darío Pulgar Arriagada`, or Jose/Juana parent candidates.

## Scores

| score | value | rationale |
|---|---:|---|
| source_quality_score | 0.58 | The source is a local CV PDF with stable source SHA-256 in metadata, but the reviewed evidence here is derivative text without an available page image. |
| conversion_confidence_score | 0.16 | Conflicting derivative page text, duplicate manifest entries, hash drift, and missing page image keep conversion confidence very low. |
| evidence_quantity_score | 0.42 | Multiple local derivatives and a source packet are available, but all meaningful page-5 facts depend on unresolved page control. |
| agreement_score | 0.22 | Sources agree on document title/context, but disagree materially on page-5 body text and metadata/hash control. |
| identity_confidence_score | 0.54 | Document-level attribution to `Dario Arturo Pulgar` is plausible from title/context; page-local identity and canonical identity bridge are absent. |
| claim_probability | 0.50 | The hold/page-control-conflict claim is highly probable; any occupational or canonical identity claim from this page remains conditional and unpromotable. |
| relevance_level | high | Directly relevant to whether page-5 CV evidence can be used for identity or work-history claims. |
| relevance_confidence | 0.96 | All reviewed files are the exact staged draft references or immediate page-control verification materials. |
| canonical_readiness | hold_for_conversion_qa | No canonical claim, relationship, person merge, or wiki update should be made until page image/PDF page control and manifest/hash drift are resolved. |

## Review Judgment

The staged draft's overall recommendation to hold is supported. Its broad identity caution is also supported: `Dario Arturo Pulgar` is a document-level/source-title identity in this evidence set, not a page-local identity statement and not a proof-reviewed bridge to `Dario Arturo Pulgar-Smith` or any Pulgar-Arriagada/Jose/Juana candidate.

The draft should not be treated as fully clean because it appears to overstate which current derivative supports the 1979 HABITAT text. Current files show the conflict as assigned chunk versus current page-5 page Markdown/current aggregate page-5 section, with the 1979 text associated with the assigned chunk and appearing later in the aggregate under page-9 metadata. That discrepancy is itself a blocker, not a reason to promote either text.

## Next Action

Keep this staged draft and dependent work-history/identity claims on `hold_for_conversion_qa`. The next safe action is targeted page-control QA from the physical source page: restore or access `page-images/page-0005.jpg` or the corresponding PDF page, compare it against both competing derivative transcriptions, then repair the duplicate manifest/hash drift before any identity bridge or canonical promotion review.
