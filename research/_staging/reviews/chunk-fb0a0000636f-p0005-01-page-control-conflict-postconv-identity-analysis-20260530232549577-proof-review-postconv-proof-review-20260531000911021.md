---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260531000911021
task_id: "proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530232549577.md"
staged_draft: "research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530232549577.md"
source_packet: "research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-hold-postconv-evidence-extraction-20260530224457988.md"
conflict_draft: "research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260530224457988.md"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md"
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: CV Page 5 Page-Control Conflict

## Blockers First

1. Keep all page-5 work-history claims on hold. The assigned chunk for `CHUNK-fb0a0000636f-P0005-01` transcribes a 1979-1970 sequence, while the conversion-job `page-markdown/page-0005.md` transcribes a materially different 1999-1997 sequence.
2. Do not choose either page-5 transcription as controlling from this proof-review pass. The job manifest records `page-images/page-0005.jpg`, but that file path is currently absent, so the physical page image was not available for visual arbitration.
3. Do not promote identity, same-person, or relationship claims from this page. The checked page-5 derivative texts do not independently state `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Pulgar-Arriagada`, parent names, spouse, child, grandchild, or any kinship.
4. The chunk manifest contains duplicate entries for `CHUNK-fb0a0000636f-P0005-01` and hash/count drift. That weakens derivative reliability until conversion QA repairs or reissues the page/chunk controls.

## Evidence Strengths

- The staged identity analysis accurately identifies the controlling issue: local derivatives disagree about what text belongs to page 5.
- The source packet, conflict draft, assigned chunk, aggregate converted file, conversion-job page Markdown, and manifests agree that the source is the CV titled `CV of Dario Arturo Pulgar`.
- The assigned chunk is internally coherent and fully transcribes a 1979-1982 HABITAT entry, 1974-1978 National Film Board of Canada entry, 1972-1973 Chile Films entry, 1970-1972 CITELCO entry, and `EDUCATION` heading.
- The conversion-job `page-markdown/page-0005.md` is also internally coherent and transcribes a separate 1999 PROFONANPE/TVE sequence followed by 1998-1999 Arca Consulting/European Commission and 1997-1998 Klohn Crippen/SNC Lavalin Agriculture entries.
- The aggregate converted file contains both the 1999-1997 page-5 text and the 1979-1970 text later in the document, which supports the staged draft's conclusion that page control is unresolved rather than a simple wording discrepancy.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 6/10 for a named CV source in local custody; reduced because no rendered page image was available for this page-control review |
| conversion_confidence_score | 2/10 for page-5 control; 7/10 for the literal text currently visible in each separate derivative |
| evidence_quantity_score | 4/10 because several local derivative artifacts were available, but no physical page image/PDF-page check was performed in this scoped review |
| agreement_score | 2/10 for page-5 content agreement; 8/10 for document-level source-title agreement |
| identity_confidence_score | 7/10 for document-level attribution to `Dario Arturo Pulgar`; 5/10 for any page-local identity attribution; 2/10 or lower for same-person bridges to `Pulgar-Smith`, `Pulgar-Arriagada`, or Jose/Juana relationship candidates from this page |
| claim_probability | 0.92 that a page-control conflict exists; 0.50 that either competing page-5 work-history transcription is the controlling one without image/PDF arbitration; 0.70 that the CV document is about Dario Arturo Pulgar at document level; 0.10 or lower for relationship claims from this page |
| relevance_level | high |
| relevance_confidence | 0.95 |
| canonical_readiness | hold_for_conversion_qa |

## Review Finding

The staged identity analysis is supported as a hold. Its main claim is not that either work-history sequence is true, but that page-5 derivative control is broken; that claim is well supported by the checked artifacts. The assigned chunk, the conversion-job page Markdown, and the aggregate converted file cannot all be treated as a single stable page-5 transcription.

The document-level label `Dario Arturo Pulgar` is plausible because the source title and conversion metadata consistently name the CV that way. However, page 5 itself, in the derivatives checked here, is not identity-bearing enough to support a canonical same-person bridge or any family relationship claim.

## Next Action

Run conversion QA for this source page before any canonical use: restore or regenerate the recorded page image, compare it to the PDF page, select the controlling page-5 transcription, and repair the duplicate manifest/hash drift. After page control is fixed, run a separate identity-bridge proof review before attaching the CV subject to `Dario Arturo Pulgar-Smith` or any Pulgar-Arriagada/Jose/Juana relationship context.
