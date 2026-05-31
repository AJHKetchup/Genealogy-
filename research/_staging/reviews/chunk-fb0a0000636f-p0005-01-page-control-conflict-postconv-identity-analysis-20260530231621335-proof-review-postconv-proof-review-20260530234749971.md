---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530234749971
task_id: "proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530231621335.md"
staged_draft: "research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530231621335.md"
source_packet: "research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-hold-postconv-evidence-extraction-20260530224457988.md"
conflict_draft: "research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260530224457988.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
conversion_job_page_markdown: "raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md"
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
canonical_readiness: hold
---

# Proof Review: Page-Control Conflict For CV Page 5

This review covers the exact staged draft `research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530231621335.md`.

## Blockers First

1. Page control is not resolved. The assigned chunk for page 5 contains the `1979 - 1982` HABITAT entry followed by 1974-1978, 1972-1973, and 1970-1972 work-history entries. The conversion-job page Markdown for page 5 contains a different `1999` PROFONANPE/TVE sequence followed by 1998-1999 and 1997-1998 entries.
2. The physical page image was not available in the referenced conversion job. `page-images/page-0005.jpg` is absent, so this review cannot choose which derivative transcription controls physical page 5.
3. Provenance is unstable. The source packet records a mismatch between converted SHA-256 recorded in the chunk and the observed converted SHA-256, and the chunk manifest duplicates `CHUNK-fb0a0000636f-P0005-01` with conflicting counts and hashes.
4. No family relationship is supported by the reviewed page-5 derivative texts. Neither derivative text states a parent, spouse, child, grandchild, or Alexander John Heinz relationship.
5. No same-person merge is ready. The reviewed page text does not independently state `Pulgar-Smith`, `Pulgar-Arriagada`, `Dario Jose`, Jose/Juana parent candidates, or another identity bridge beyond the document-level CV title `CV of Dario Arturo Pulgar`.

## Evidence Strengths

- The staged draft accurately identifies a real conflict between the assigned chunk and the conversion-job page Markdown.
- The source packet independently flags the same page-control conflict and recommends `hold_for_conversion_qa`.
- The assigned chunk is internally coherent as a typed CV work-history page, but its page control is disputed.
- The conversion-job page Markdown is also internally coherent as typed CV work-history text, but it conflicts materially with the assigned chunk.
- The aggregate converted file contains both sequences in different locations, reinforcing that derivative assembly or page mapping needs QA before claim promotion.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 5/10 for derivative CV text; the underlying source is a named CV PDF, but the physical page was not checked in this review |
| conversion_confidence_score | 2/10 because page 5 has competing derivative transcriptions, missing page image, duplicate manifest entries, and hash drift |
| evidence_quantity_score | 4/10 for the narrow existence of a page-control conflict; 1/10 for identity or relationship claims |
| agreement_score | 2/10 for page-5 content across derivative files; 8/10 that the local staging artifacts agree a hold is needed |
| identity_confidence_score | 5/10 for provisional document-level `Dario Arturo Pulgar` CV context; 2/10 or lower for any merge to `Pulgar-Smith`, `Pulgar-Arriagada`, `Dario Jose`, or Jose/Juana lineage candidates |
| claim_probability | 0.92 that this is a valid page-control/provenance conflict; 0.38 that the assigned chunk controls physical page 5; 0.36 that the page Markdown controls physical page 5; 0.10 or lower for any relationship claim from this evidence |
| relevance_level | high for conversion QA and later CV work-history extraction; low for immediate genealogy relationship proof |
| relevance_confidence | 0.90 for conversion QA relevance; 0.35 for identity-bridge relevance |
| canonical_readiness | hold / not ready |

## Review Finding

The staged identity/conflict analysis is supported as a hold. Its strongest claim is not a biographical fact, identity merge, or relationship; it is the procedural claim that page 5 has unresolved derivative text and provenance conflicts.

The reviewed materials do not support promoting either page-5 work-history sequence. They also do not support attaching this evidence to `Dario Arturo Pulgar-Smith`, merging it with any Pulgar-Arriagada candidate, or creating Jose/Juana parent-child relationships.

## Next Action

Keep the draft on `hold_for_conversion_qa`. Restore or regenerate the missing page image, recheck physical PDF page 5, reconcile the duplicate manifest entries and hash drift, and then run a fresh claim proof review only on the certified controlling page text.
