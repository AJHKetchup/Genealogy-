---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260531105727445
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531003657248.md
staged_draft: research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531003657248.md
reviewed_source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-hold-postconv-evidence-extraction-20260531000652338.md
reviewed_chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
reviewed_converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
reviewed_conversion_job_page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
canonical_readiness: blocked
promotion_recommendation: hold_for_conversion_qa
---

# Proof Review: Page 5 Identity Analysis Conflict

## Blockers First

1. Page control is unresolved. The assigned chunk for page 5 preserves 1979-1982 HABITAT, 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, and 1970-1972 CITELCO. The conversion-job page Markdown for page 5 preserves a different 1999-1997 consulting sequence beginning with PROFONANPE and ending mid-entry at SNC Lavalin Agriculture.
2. The aggregate converted file contains both derivative text clusters: the 1999-1997 consulting entries near the earlier part of the file and the 1979-1970 entries later in the file. That supports the existence of both transcriptions locally, but it does not prove which one controls physical page 5.
3. The source packet reports missing local page images for page 5, and a local search under the conversion-job directory did not find `page-0005.jpg`. The physical page cannot be visually checked in this review.
4. The chunk manifest repeats `CHUNK-fb0a0000636f-P0005-01` for the same path/page. The source packet also reports observed hashes differing from recorded metadata, so derivative integrity is not clean enough for canonical use.
5. The page body in the checked derivatives does not state the subject's full name, parents, spouse, children, or any relationship to Pulgar-Smith, Arriagada, Jose, Juana, or Alexander John Heinz. Any identity bridge from this page alone would be a relationship jump.

## Evidence Strengths

- The assigned chunk clearly supports the local existence of the 1979-1970 work-history transcription.
- The conversion-job page Markdown clearly supports the local existence of the competing 1999-1997 consulting transcription.
- The source title/path and packet identify the document as a CV of Dario Arturo Pulgar, which is relevant identity context, but it is document-level context rather than page-body proof.
- The staged draft accurately treats this as a conversion/page-control conflict and does not promote a relationship claim.

## Scored Judgment

| Score category | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.62 | The underlying source is a named CV packet, but this review only had derivative text and no page image for direct verification. |
| conversion_confidence_score | 0.12 | Competing page-5 derivatives, duplicated manifest entries, missing page image, and hash disagreement block reliance on either page-5 transcription as authoritative. |
| evidence_quantity_score | 0.46 | There is enough derivative evidence to diagnose the conflict, but not enough independent or visual evidence to resolve it. |
| agreement_score | 0.18 | The assigned chunk and conversion-job page Markdown disagree materially on the page's contents. |
| identity_confidence_score | 0.34 | Document-level context points to Dario Arturo Pulgar, but page-local identity proof and bridge identifiers are absent. |
| claim_probability | 0.90 | High probability that a page-control conflict exists; low probability that either derivative can be treated as canonical page-5 proof before QA. |
| relevance_level | high | The CV subject is relevant to Pulgar identity analysis and possible later bridge work. |
| relevance_confidence | 0.92 | The source title and staged packet make the relevance clear even though identity attachment is not ready. |
| canonical_readiness | blocked | No canonical claim, relationship, merge, or identity attachment should be promoted from this staged draft. |

## Claim-Level Probability

| Claim under review | Probability | Review action |
| --- | ---: | --- |
| A local derivative chunk contains the 1979-1970 HABITAT/NFB/Chile Films/CITELCO sequence. | 0.96 | supported_as_derivative_text |
| The 1979-1970 sequence controls physical page 5. | 0.35 | hold_for_conversion_qa |
| The 1999-1997 PROFONANPE/TVE/Arca/Klohn/SNC sequence controls physical page 5. | 0.35 | hold_for_conversion_qa |
| Page 5 independently identifies the CV subject as Dario Arturo Pulgar. | 0.20 | not_page_body_supported |
| Page 5 proves the CV subject is Dario Arturo Pulgar-Smith. | 0.24 | blocked_identity_bridge |
| Page 5 proves a relationship to Arriagada, Jose, Juana, or Alexander John Heinz. | 0.01 | unsupported |

## Identity And Relationship Risk

- Identity risk is high for canonical attachment because page 5 does not contain a full-name bridge, surname variant, family relationship, date of birth, parents, spouse, child, or grandchild statement.
- Relationship risk is very high for any Jose/Juana or Alexander John Heinz connection because none of those relationships appears in the reviewed page-5 material.
- Source reliability is limited here by derivative-control failure, not by an apparent contradiction in the CV person's life history.

## Next Action

Hold this staged draft for conversion QA. The next worker should restore or regenerate the authoritative page 5 image, compare it against the assigned chunk, aggregate converted file, conversion-job page Markdown, and manifest, then reconcile the duplicated manifest/hash state. Only after page control is fixed should a separate identity-bridge proof review consider whether the document-level Dario Arturo Pulgar is the same person as any canonical Pulgar-line subject.
