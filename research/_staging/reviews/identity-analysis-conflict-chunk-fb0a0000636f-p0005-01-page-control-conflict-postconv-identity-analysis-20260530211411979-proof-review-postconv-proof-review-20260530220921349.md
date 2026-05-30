---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530220921349
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530211411979.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530211411979.md"
source_packet: "research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-work-history.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
conversion_job_page_markdown: "raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md"
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
source_quality_score: 0.58
conversion_confidence_score: 0.20
evidence_quantity_score: 0.35
agreement_score: 0.25
identity_confidence_score: 0.50
claim_probability: 0.50
relevance_level: high
relevance_confidence: 0.92
canonical_readiness: hold
---

# Proof Review: Page-Control Conflict For CV Page 5

## Blockers First

1. Hold all page-5 occupational claims. The assigned chunk and source packet support 1979-1982 HABITAT, 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, and 1970-1972 CITELCO entries, while `page-markdown/page-0005.md` supports materially different 1999/1998 entries.
2. The authoritative page image was unavailable for this review. The conversion manifest points to `page-images/page-0005.jpg`, but that file is not present in the checked conversion job directory.
3. The chunk manifest has duplicate `CHUNK-fb0a0000636f-P0005-01` records for the same chunk path with different character counts and hashes. This is a provenance/page-control blocker, not a family-history conflict.
4. Page-local identity support is weak. The checked page body does not repeat `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, or Jose/Juana parent candidates; attribution is document-level from source/job title.
5. No relationship claim is supported. The checked materials are CV work-history derivatives and contain no parent, spouse, child, sibling, household, grandchild, or other kinship statement.

## Evidence Strengths

- The staged draft accurately identifies the central issue as a conflict between derivative transcriptions for the same page reference.
- The source packet and assigned chunk agree internally on the 1979-1970 work-history sequence and are legible as a self-contained derivative transcription.
- The conversion job manifest and `page-markdown/page-0005.md` agree on the page-5 page-markdown path, and that page-markdown text is also legible as a self-contained derivative transcription.
- The aggregate converted file contains both 1999/1998 and 1979-1970 material, which supports the staged draft's concern that derivative output state is mixed or stale.
- The broader source metadata consistently identifies the document as a CV of `Dario Arturo Pulgar`, but that supports only cautious document-level attribution.

## Scored Judgment

| metric | score | rationale |
|---|---:|---|
| source_quality_score | 0.58 | A CV is useful for self-reported work history, but the source page image was unavailable and the reviewed evidence is derivative. |
| conversion_confidence_score | 0.20 | Page-markdown, chunk, aggregate conversion, and chunk manifest disagree about page 5 control. |
| evidence_quantity_score | 0.35 | Multiple local derivative files were checked, but there is no authoritative image/source-page confirmation. |
| agreement_score | 0.25 | Agreement is good within each competing derivative text, but poor across the controlling evidence set. |
| identity_confidence_score | 0.50 | Document-level `Dario Arturo Pulgar` attribution is plausible; page-local and canonical identity attachment are not proved. |
| claim_probability | 0.50 | Either competing work-history sequence may be valid somewhere in the CV, but neither is proved as page 5 from this review. |
| relevance_level | high | Directly addresses the assigned identity-analysis conflict and promotion risk. |
| relevance_confidence | 0.92 | The reviewed files are the staged draft's referenced evidence set. |
| canonical_readiness | hold | Do not promote, merge, normalize, or attach claims canonically until page control is resolved. |

## Review Finding

The staged draft is supported as a hold. It should not be treated as proof of an occupational chronology, an identity merge, or a Pulgar-line relationship. The available evidence supports only the procedural conclusion that page-5 derivative control is unresolved.

No checked source text supports changing the name form or attaching this page to canonical `Dario Arturo Pulgar-Smith`. That question remains an identity-bridge problem after conversion/source-prep QA resolves which transcription controls the page.

## Next Action

Hold for conversion/source-prep QA. Restore or regenerate the page-5 image/source-page control, reconcile whether page 5 contains the 1999/1998 text or the 1979-1970 text, repair the duplicate chunk manifest entries, then rerun proof review before any canonical promotion.
