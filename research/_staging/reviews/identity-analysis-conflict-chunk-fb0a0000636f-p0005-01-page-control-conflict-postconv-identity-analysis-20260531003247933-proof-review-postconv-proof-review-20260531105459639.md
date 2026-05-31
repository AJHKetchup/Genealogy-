---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260531105459639
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531003247933.md
staged_draft: research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531003247933.md
reviewed_source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-hold-postconv-evidence-extraction-20260531000652338.md
reviewed_chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
reviewed_converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
reviewed_conversion_job_page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
created: 2026-05-31
canonical_readiness: blocked
promotion_recommendation: hold_for_conversion_qa
---

# Proof Review: Page 5 Control Conflict

## Blockers

1. Physical page control is not verified. The assigned chunk contains the 1979-1970 HABITAT, National Film Board of Canada, Chile Films, and CITELCO work-history sequence, while the conversion-job `page-0005.md` contains the 1999-1997 PROFONANPE, TVE, Arca Consulting/European Commission, Klohn Crippen Consultants, and SNC Lavalin Agriculture sequence.
2. The aggregate converted file contains both candidate page-5 readings in different sections and therefore does not resolve which derivative transcription controls the physical page.
3. No local page image or extracted page image for page 5 was available in the checked conversion-job image folders, so neither derivative could be visually verified against the source page during this review.
4. The chunk manifest duplicates `CHUNK-fb0a0000636f-P0005-01` for the same chunk path with different character counts and hashes; the source packet also reports observed hash values that differ from recorded metadata.
5. Neither candidate page-5 body independently names `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, Jose/Juana parent candidates, Alexander John Heinz, spouse, child, grandchild, or a family relationship.
6. Canonical promotion is blocked. This staged draft supports a conversion/page-control warning, not a canonical identity merge, relationship claim, or occupational claim.

## Evidence Strengths

- The staged draft accurately frames the issue as a page-control/provenance conflict rather than a resolved life-history contradiction.
- The assigned chunk literally supports the derivative presence of the 1979-1982 HABITAT, 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, and 1970-1972 CITELCO entries.
- The conversion-job page Markdown literally supports the competing derivative presence of the 1999 PROFONANPE and TVE entries, the 1998-1999 Arca Consulting/European Commission entry, and the 1997-1998 Klohn Crippen/SNC Lavalin entries.
- The source packet correctly treats `Dario Arturo Pulgar` as document-level attribution from the CV title/path and warns that no family relationship is stated in the assigned page body.

## Scored Judgment

| metric | score / value | rationale |
| --- | ---: | --- |
| source_quality_score | 0.58 | A CV titled for Dario Arturo Pulgar is potentially useful for work-history evidence, but the raw page image was unavailable locally for direct verification in this review. |
| conversion_confidence_score | 0.12 | Incompatible derivative readings, duplicate manifest rows, hash drift, and absent page image make page-control confidence very low. |
| evidence_quantity_score | 0.44 | There is enough derivative evidence to prove a control conflict, but not enough verified evidence to choose a transcript or support identity/relationship promotion. |
| agreement_score | 0.18 | The assigned chunk, conversion-job page Markdown, aggregate converted file, and manifest metadata do not agree on page 5. |
| identity_confidence_score | 0.36 | The document title supports a Dario Arturo Pulgar context, but page-local text does not bridge to a canonical person or family relationship. |
| claim_probability | 0.91 | The probability that a page-control conflict exists is high; the probability that either candidate reading controls physical page 5 remains low until QA. |
| relevance_level | high | The CV is relevant to the Dario/Pulgar identity cluster and possible later work-history claims. |
| relevance_confidence | 0.90 | The source title, source packet, staged draft, and local paths consistently place the material in the Dario Arturo Pulgar CV workflow. |
| canonical_readiness | blocked | No canonical claim, relationship, merge, or wiki update should proceed from this page until conversion QA and separate identity-bridge review are complete. |

## Claim Judgment

| claim / issue | review judgment | probability | canonical_readiness |
| --- | --- | ---: | --- |
| A page-control conflict exists for page 5 | Supported by direct comparison of the staged draft, source packet, assigned chunk, aggregate converted file, conversion-job page Markdown, manifest metadata, and absent image paths. | 0.91 | blocked |
| The assigned derivative chunk contains the 1979-1970 work-history sequence | Literally supported in the assigned chunk. | 0.97 | hold |
| The 1979-1970 sequence controls physical page 5 | Not proven without page image verification and manifest/hash repair. | 0.34 | blocked |
| The 1999-1997 sequence controls physical page 5 | Not proven because it conflicts with the assigned chunk and lacks page image verification. | 0.34 | blocked |
| Page 5 proves canonical `Dario Arturo Pulgar-Smith` identity | Not supported page-locally; no `Smith`, relationship statement, date bridge, spouse, child, grandchild, or Alexander John Heinz reference appears in the checked page materials. | 0.22 | blocked |
| Page 5 proves a Pulgar-Arriagada or Jose/Juana lineage connection | Not supported; the checked page materials contain no Jose, Juana, Arriagada, parentage, or lineage evidence. | 0.01 | blocked |

## Next Action

Hold for conversion QA. Restore or re-render the authoritative physical page 5 image from `raw/sources/CV of Dario Arturo Pulgar.pdf`, compare it against both derivative readings, reconcile duplicate manifest rows and hash disagreement, and certify one controlling transcript. After page-control repair, review only narrow occupational/place claims from the verified transcript and handle any attachment to `Dario Arturo Pulgar-Smith` as a separate identity-bridge proof.
