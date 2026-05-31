---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260531082442790
task_id: "proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-dario-arturo-pulgar-identity-hold-postconv-identity-analysis-20260531065431265.md"
staged_draft: "research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-dario-arturo-pulgar-identity-hold-postconv-identity-analysis-20260531065431265.md"
source_packet: "research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-revision-postconv-evidence-extraction-20260531045753452.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
canonical_readiness: blocked
---

# Proof Review: Dario Arturo Pulgar CV Page 5 Identity Hold

## Blockers First

1. Do not promote identity or relationship claims from this staged draft. The page-5 body checked in the assigned chunk contains work-history text, but it does not print `Dario Arturo Pulgar`, `Pulgar-Smith`, birth details, parents, spouse, children, or any other identity-bridge fact.
2. Page control is blocked. The assigned chunk for page 5 contains 1979-1982 HABITAT, 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, and 1970-1972 CITELCO entries. The conversion-job page Markdown for the same page contains a different 1999-1997 consulting sequence beginning with PROFONANPE/TVE, Arca Consulting/European Commission, Klohn Crippen, and SNC Lavalin Agriculture.
3. Source reliability for this review is limited by local custody problems. The source packet records the source PDF as absent at the recorded path during extraction, and direct local path check in this review also found `raw/sources/CV of Dario Arturo Pulgar.pdf` absent.
4. The chunk manifest is internally inconsistent for this page: it lists `CHUNK-fb0a0000636f-P0005-01` twice with different character counts and hashes. The observed source packet also records hash drift between recorded and observed converted/chunk values.
5. Do not merge or attach this page to canonical `wiki/people/dario-arturo-pulgar-smith.md`. The canonical page is family-supplied and explicitly warns that Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records need identity review before attachment.

## Evidence Strengths

- The converted document title and source path identify the broader source as `CV of Dario Arturo Pulgar`.
- The assigned chunk is internally coherent as a typed CV page with work-history entries and a stated completeness audit.
- The staged identity draft and source packet correctly characterize the page-body name support as absent and recommend `hold_for_conversion_qa`.
- The item remains relevant to Pulgar identity research because the source title names `Dario Arturo Pulgar`, but its usable value is only document-level until page control is certified.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 3/10 |
| conversion_confidence_score | 1.5/10 |
| evidence_quantity_score | 2/10 |
| agreement_score | 2/10 |
| identity_confidence_score | 5/10 for broad document-title association with `Dario Arturo Pulgar`; 2.5/10 for attachment to `Dario Arturo Pulgar-Smith`; 0.5/10 for any parent/spouse/child relationship |
| claim_probability | 0.58 that the broader document is a CV of `Dario Arturo Pulgar`; 0.25 that this page currently supports attachable work-history claims for that person; 0.20 that this page supports attachment to canonical `Dario Arturo Pulgar-Smith`; 0.01 for any family relationship claim |
| relevance_level | high |
| relevance_confidence | 0.90 |
| canonical_readiness | blocked |

## Review Finding

The staged analysis is supported as a hold. The only identity support comes from the document-level title/path, not from the literal page-5 body. The literal checked page evidence is not stable enough for canonical use because two local derivatives disagree about what page 5 says, the physical source file was unavailable at the recorded path, and the chunk manifest/hash metadata is inconsistent.

No reviewed source text supports changing, expanding, or normalizing the page subject to `Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Darío Pulgar Arriagada`, or any Jose/Juana parent candidate. No reviewed source text supports a relationship claim.

## Next Action

Keep this staged draft on `hold_for_conversion_qa`. The next required action is page-control QA: restore or verify the authoritative PDF/page image, determine which page-5 derivative is physically correct, repair manifest/hash drift through the conversion workflow, and then run a separate identity-bridge review before attaching any accepted CV claims to a canonical person page.
