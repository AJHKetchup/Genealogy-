---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260531105231044
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

1. Physical page control is unresolved. The assigned chunk for page 5 contains the 1979-1970 HABITAT, National Film Board of Canada, Chile Films, and CITELCO reading, while the conversion-job page Markdown for `page-0005.md` contains the 1999-1997 PROFONANPE, Television Trust for the Environment, Arca Consulting/European Commission, Klohn Crippen Consultants, and SNC Lavalin Agriculture reading.
2. The aggregate converted file contains both competing readings in different positions, so it does not identify which derivative controls physical page 5.
3. Local checks for `page-images/page-0005.jpg` and `extracted-images/page-0005.jpg` returned absent, so this review cannot compare either derivative against a page image.
4. The chunk manifest repeats `CHUNK-fb0a0000636f-P0005-01` for `page-0005-chunk-01.md` with different character counts and hashes. Observed SHA-256 values for the converted file and chunk also differ from recorded metadata in the checked files.
5. Page-local text does not independently name Dario Arturo Pulgar or prove Dario Arturo Pulgar-Smith, Dario Jose Pulgar-Arriagada, Jose, Juana, parentage, spouse, children, or any family relationship.

## Evidence Strengths

- The staged draft accurately reports the assigned chunk reading: `1979 - 1982` HABITAT in Nairobi, `1974 - 1978` National Film Board of Canada in Montreal, `1972 - 1973` Chile Films in Santiago, and `1970 - 1972` CITELCO in Santiago.
- The staged draft accurately reports the competing conversion-job page Markdown reading: `1999` PROFONANPE in Peru and TVE in London, `1998 - 1999` Arca Consulting/European Commission in Lesotho, `1997-1998` Klohn Crippen Consultants in Huaraz, and SNC Lavalin Agriculture in Maracaibo.
- The source packet and source path identify the document as `CV of Dario Arturo Pulgar`, making the material relevant to a Dario/Pulgar identity review at document level.
- The staged draft keeps source transcription separate from identity interpretation and recommends hold/QA rather than canonical promotion.

## Scored Judgment

| Metric | Score / Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.62 | The underlying source is a named CV and the derivative text is coherent, but the physical page image is unavailable locally and derivative metadata is conflicted. |
| conversion_confidence_score | 0.12 | Two page-5 derivatives conflict, expected page image paths are absent, and chunk/converted hash metadata is inconsistent. |
| evidence_quantity_score | 0.45 | There is enough checked derivative evidence to prove a page-control conflict, but not enough verified evidence to promote either page-5 reading or an identity bridge. |
| agreement_score | 0.18 | The assigned chunk and conversion-job page Markdown disagree on the page-5 text; the aggregate converted file does not resolve the disagreement. |
| identity_confidence_score | 0.34 | The document title supports a Dario Arturo Pulgar subject at document level, but page-local text does not prove a canonical same-person or relationship attachment. |
| claim_probability | 0.90 | The claim that a page-control conflict exists is strongly supported by the checked files; the claim that either derivative controls physical page 5 remains unproved. |
| relevance_level | high | A CV titled for Dario Arturo Pulgar is relevant to the Pulgar identity cluster. |
| relevance_confidence | 0.93 | The source title, staged draft, source packet, and local paths consistently place the material in the Dario/Pulgar review context. |
| canonical_readiness | blocked | No canonical claim, merge, relationship, or wiki update should proceed until page control and metadata are repaired. |

## Claim-Level Findings

| Claim / issue | Review judgment | Probability | Canonical readiness |
| --- | --- | ---: | --- |
| Page-control conflict exists for page 5 | Supported by direct comparison of the staged draft, source packet, assigned chunk, conversion-job page Markdown, aggregate converted file, manifest check, missing image checks, and hash checks. | 0.90 | blocked |
| Assigned chunk contains the 1979-1970 work-history entries | Literally supported in the assigned chunk and also present in the aggregate converted file. | 0.96 | hold |
| Assigned chunk controls physical page 5 | Not proven because the page image is absent and conversion-job page Markdown conflicts. | 0.35 | blocked |
| Conversion-job page Markdown controls physical page 5 | Not proven because the page image is absent and assigned chunk/aggregate content conflicts. | 0.35 | blocked |
| Page 5 proves the CV subject is canonical Dario Arturo Pulgar-Smith | Not supported page-locally; no `Smith`, relationship statement, dates, spouse, child, or other bridge identifier appears in the checked page materials. | 0.24 | blocked |
| Page 5 proves a connection to Dario Jose Pulgar-Arriagada or Jose/Juana parent candidates | Not supported; the checked page materials contain no Jose, Juana, Arriagada, parentage, or lineage evidence. | 0.01 | blocked |

## Next Action

Hold for conversion QA. Restore or re-render the authoritative physical page 5 image, reconcile duplicate chunk-manifest rows and hash disagreement, then select the controlling page-5 transcript. After that, proof-review only narrow occupational/place claims from the verified transcript; handle any Dario/Pulgar same-person bridge as a separate identity proof using direct identifiers.
