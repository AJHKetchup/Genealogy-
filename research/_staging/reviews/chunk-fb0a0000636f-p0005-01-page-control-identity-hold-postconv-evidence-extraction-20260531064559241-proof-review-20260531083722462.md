---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260531083722462
task_id: "proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-identity-hold-postconv-evidence-extraction-20260531064559241.md"
staged_draft: "research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-identity-hold-postconv-evidence-extraction-20260531064559241.md"
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
conversion_job_page_markdown: "raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md"
canonical_readiness: blocked
---

# Proof Review: Page-5 CV Identity Hold

## Blockers First

1. Do not promote page-5 work-history claims from this staged draft. The referenced chunk transcribes a 1979-1970 employment page, while the conversion-job page Markdown for page 5 transcribes a 1999-1997 consulting page. The local evidence set therefore has a page-control conflict.
2. Do not attach this item to `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Darío Pulgar Arriagada`, `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, or any family relationship. Neither checked page text repeats the subject name or states parent, spouse, child, sibling, or other kinship evidence.
3. The source PDF path `raw/sources/CV of Dario Arturo Pulgar.pdf`, the staged source PDF path in the manifest, and the rendered page image path for `page-0005.jpg` are not available locally. Without the visible source image, the reviewer cannot adjudicate which page transcription is physically correct.
4. File-integrity metadata is not stable. The chunk front matter records `converted_sha256` as `fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0`, while the current converted file hashes to `da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288` and the current chunk hashes to `d6ea4f611ee03000c11cbba63246e95b55f8a421fcbc87d0d667e91f5c8d0b8d`.

## Evidence Strengths

- The staged draft accurately identifies the central support problem: the chunk and conversion-job page Markdown disagree about the contents of page 5.
- The checked chunk supports that one local derivative contains the 1979-1982 HABITAT, 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, and 1970-1972 CITELCO entries.
- The checked conversion-job page Markdown supports that another local derivative for page 5 contains 1999 PROFONANPE and Television Trust for the Environment, 1998-1999 Arca Consulting/European Commission, 1997-1998 Klohn Crippen, and SNC Lavalin Agriculture entries.
- The converted file contains both sequences in different locations, which supports the conclusion that chunk/page derivation or page-control metadata needs QA before claim extraction.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 3/10: CV source type may be relevant, but the source PDF and rendered page image are unavailable for this review |
| conversion_confidence_score | 1/10 for page-5 claim extraction because the page Markdown and chunk conflict and the image is unavailable |
| evidence_quantity_score | 2/10: only derivative text was available; no visible source image or independent identity bridge was available |
| agreement_score | 1/10 between page-5 derivatives; high disagreement on the actual page contents |
| identity_confidence_score | 2/10 for treating this as a document-continuity lead for `Dario Arturo Pulgar`; 0.5/10 for any merge to `Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, parents, or family relationships |
| claim_probability | 0.20 that the staged page-5 work-history claims are physically assigned to the correct page; 0.05 or lower for any identity merge or relationship claim |
| relevance_level | high |
| relevance_confidence | 0.80: if page control is resolved, a CV page may be relevant to the named CV subject, but it is not currently reliable enough for canonical use |
| canonical_readiness | blocked |

## Review Finding

The staged draft is supported as a hold. Its caution against attaching the page-5 derivative text to canonical people or relationships is warranted because the local derivatives disagree and the source image needed to resolve the conflict is absent.

The draft should not be upgraded to a promoted claim. The only defensible reviewed conclusion is a QA hold for page-control resolution and identity-bridge review after the physical page 5 image or source PDF is available.

## Next Action

Run conversion/page-control QA for this source packet and restore or regenerate the rendered page image/source PDF before any work-history facts from this page are staged as claims. After QA certifies the physical page content, perform a separate identity proof review before linking the CV subject to any canonical person or family relationship.
