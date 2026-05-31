---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260531104214473
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531003657248.md
staged_draft: research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531003657248.md
reviewed_source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-hold-postconv-evidence-extraction-20260531000652338.md
reviewed_chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
reviewed_converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
reviewed_conversion_job_page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
canonical_readiness: blocked
promotion_recommendation: hold_for_conversion_qa
---

# Proof Review: Page 5 Control Conflict

## Blockers First

1. Page control is unresolved. The assigned chunk for page 5 transcribes 1979-1970 work-history entries for HABITAT, National Film Board of Canada, Chile Films, and CITELCO, while the conversion-job page markdown for page 5 transcribes 1999-1997 consulting entries for PROFONANPE, TVE, Arca Consulting/European Commission, Klohn Crippen Consultants, and SNC Lavalin Agriculture.
2. The aggregate converted file contains both derivative readings in different positions, so it does not resolve which transcription controls physical page 5.
3. The local page image checks for `page-images/page-0005.jpg` and `extracted-images/page-0005.jpg` were negative, so this review cannot verify either transcription against the physical page image.
4. The chunk manifest repeats `CHUNK-fb0a0000636f-P0005-01`, matching the staged draft's duplicate-manifest concern and weakening derivative control.
5. Page body evidence does not independently name Dario Arturo Pulgar, Dario Arturo Pulgar-Smith, Dario Jose Pulgar-Arriagada, Jose, Juana, parents, spouse, children, or any family relationship. Any canonical identity bridge or relationship attachment would be unsupported from this page.

## Evidence Strengths

- The staged draft accurately reports the assigned chunk's literal page-5 reading: 1979-1982 HABITAT in Nairobi, 1974-1978 National Film Board of Canada in Montreal, 1972-1973 Chile Films in Santiago, and 1970-1972 CITELCO in Santiago.
- The staged draft accurately reports the competing conversion-job page-markdown reading: 1999 PROFONANPE in Peru, TVE in London, 1998-1999 Arca Consulting/European Commission in Lesotho, 1997-1998 Klohn Crippen Consultants in Huaraz, and SNC Lavalin Agriculture in Maracaibo.
- The source title and paths consistently identify the document as `CV of Dario Arturo Pulgar`, which supports document-level relevance, but not page-local proof of identity or family relationship.
- The draft correctly keeps identity interpretation separate from literal transcription and recommends holding for conversion QA rather than canonical promotion.

## Scored Judgment

| Metric | Score / Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.62 | The underlying source is a named CV and the derivative text is coherent, but page image verification is unavailable and derivative metadata is conflicted. |
| conversion_confidence_score | 0.12 | Two page-5 derivative readings conflict, page images are absent, observed hashes disagree with recorded metadata per the source packet, and the chunk manifest duplicates the page-5 chunk id. |
| evidence_quantity_score | 0.45 | There is enough text to evaluate the page-control problem, but not enough verified evidence to promote work-history claims or identity bridges. |
| agreement_score | 0.18 | Assigned chunk and conversion-job page markdown disagree on the controlling page-5 content; the aggregate converted file includes both readings in separate locations. |
| identity_confidence_score | 0.34 | The document title supports a Dario Arturo Pulgar subject, but page body evidence does not prove Dario Arturo Pulgar-Smith, Dario Jose Pulgar-Arriagada, or any family-role identity. |
| claim_probability | 0.90 | The claim that there is a page-control conflict is strongly supported by the checked files. The claim that either derivative controls physical page 5 remains unproved. |
| relevance_level | high | A CV for Dario Arturo Pulgar is highly relevant to the Pulgar identity question, even though this page cannot attach a canonical identity. |
| relevance_confidence | 0.93 | The source title, staged draft, and source packet consistently place this material in the Dario/Pulgar review cluster. |
| canonical_readiness | blocked | No canonical claim, identity merge, relationship, or wiki update should proceed until conversion QA resolves page control. |

## Claim-Level Findings

| Claim / issue | Review judgment | Probability | Canonical readiness |
| --- | --- | ---: | --- |
| A page-control conflict exists for page 5 | Supported by direct comparison of the staged draft, source packet, assigned chunk, aggregate converted file, page markdown, manifest check, and missing image checks. | 0.90 | blocked |
| Assigned chunk contains the 1979-1970 work-history entries | Literally supported in the assigned chunk and aggregate converted file. | 0.96 | hold |
| Assigned chunk controls physical page 5 | Not proven because page image is absent and page markdown conflicts. | 0.35 | blocked |
| Conversion-job page markdown controls physical page 5 | Not proven for the same reason. | 0.35 | blocked |
| Page 5 proves the CV subject is canonical Dario Arturo Pulgar-Smith | Not supported page-locally; no `Smith`, relationship statement, dates, spouse, child, or other bridge identifier appears in the checked page materials. | 0.24 | blocked |
| Page 5 proves a connection to Dario Jose Pulgar-Arriagada or Jose/Juana parent candidates | Not supported. The page materials contain no Jose, Juana, Arriagada, parentage, or lineage evidence. | 0.01 | blocked |

## Next Action

Hold this staged draft for conversion QA. Re-render or restore the authoritative physical page 5 image, reconcile the duplicate manifest rows and hash disagreement, then decide which page-5 transcript controls. After that, review only narrow occupational/place claims from the verified page transcript and run any Dario/Pulgar same-person bridge as a separate identity proof using direct identifiers.
