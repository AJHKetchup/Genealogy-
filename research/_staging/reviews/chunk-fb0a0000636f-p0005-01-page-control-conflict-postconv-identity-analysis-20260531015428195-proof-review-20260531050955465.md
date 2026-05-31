---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260531050955465
task_id: "proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531015428195.md"
staged_draft: "research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531015428195.md"
source_packet: "research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-revision-postconv-evidence-extraction-20260531010209483.md"
referenced_conflict_note: "research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260531010209483.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
conversion_job_page_markdown: "raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md"
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: CV Page 5 Control Conflict

## Blockers First

1. Physical page control is not verified. The assigned chunk for `CHUNK-fb0a0000636f-P0005-01` transcribes a 1979-1970 employment-history page, while the conversion-job `page-markdown/page-0005.md` transcribes a different 1999-1997 consulting-history page.
2. The recorded original source PDF `raw/sources/CV of Dario Arturo Pulgar.pdf` is absent locally, and no `page-0005.jpg`, `page-0005.jpeg`, or `page-0005.png` page image was found under the referenced conversion-job directory during this review.
3. The chunk manifest contains duplicate entries for `CHUNK-fb0a0000636f-P0005-01`; the source packet also records observed hash drift for the converted file and assigned chunk. This blocks reliance on the derivative path as the controlling physical page.
4. Page 5 does not independently support a same-person merge to `Dario Arturo Pulgar-Smith`, `Dario Pulgar Arriagada`, or `Dario Jose Pulgar-Arriagada`. It also does not state parents, spouse, children, or Jose/Juana relationship candidates.
5. Any occupational, chronology, place, travel, education-heading, relationship, name-variant, or canonical identity claim from this page should remain on hold until conversion/source QA certifies the controlling transcription.

## Evidence Strengths

- The staged draft is well supported as a conversion/page-control hold. The checked source packet and conflict note both identify the same conflict between the assigned chunk and conversion-job page Markdown.
- The assigned chunk is internally clear and complete as derivative text: it contains HABITAT, National Film Board of Canada, Chile Films, and CITELCO entries from 1979 through 1970, followed by an `EDUCATION` heading.
- The conversion-job page Markdown is also internally clear as derivative text: it contains PROFONANPE, Television Trust for the Environment, Arca Consulting/European Commission, Klohn Crippen Consultants, and SNC Lavalin Agriculture entries from 1999 through 1997, ending mid-sentence.
- The aggregate converted file contains both relevant sequences, which supports the existence of a derivative-control problem but does not select which sequence belongs to physical page 5.
- The document-level subject name `Dario Arturo Pulgar` is supported only by source title/path and derivative metadata, not by either checked page-5 body itself.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 4/10 |
| conversion_confidence_score | 2/10 |
| evidence_quantity_score | 3/10 |
| agreement_score | 2/10 for physical page control; 8/10 that derivative files conflict |
| identity_confidence_score | 5/10 for document-level `Dario Arturo Pulgar`; 2/10 or lower for attaching this page to `Dario Arturo Pulgar-Smith`, `Dario Pulgar Arriagada`, or `Dario Jose Pulgar-Arriagada` |
| claim_probability | 0.90 that this staged item correctly identifies a page-control conflict; 0.50 that either unchecked work-history body is physical page 5; 0.20 or lower for same-person/relationship claims |
| relevance_level | high |
| relevance_confidence | 0.98 |
| canonical_readiness | hold_for_conversion_qa |

## Review Finding

The staged identity/conflict analysis is supported as a hold. The evidence is sufficient to say that local derivative materials disagree about page 5 and that canonical promotion is unsafe. It is not sufficient to certify either the 1979-1970 employment sequence or the 1999-1997 consulting sequence as the physical page-5 text.

The draft appropriately avoids promoting identity merges and family relationships. No checked page-5 text visibly supports expanding or merging the CV subject into `Pulgar-Smith`, `Pulgar-Arriagada`, `Dario Jose`, or Jose/Juana parent candidates.

## Next Action

Run targeted conversion/source QA: restore or regenerate the authoritative source PDF or page-5 image, compare it against both derivative transcriptions, repair duplicate manifest/hash state, and certify the controlling physical page-5 text. After that, rerun proof review for the surviving literal page-5 claims and require a separate identity-bridge review before attaching them to any canonical person profile.
