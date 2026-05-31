---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260531104950928
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531003247933.md
staged_draft: research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531003247933.md
review_status: hold
canonical_readiness: not_ready
created: 2026-05-31
---

# Proof Review: Page-Control Conflict For CHUNK-fb0a0000636f-P0005-01

## Blockers

- The staged draft is supported as a page-control conflict, not as a promotion-ready identity or work-history proof.
- The assigned chunk at `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md` contains the 1979-1970 HABITAT/NFB/Chile Films/CITELCO sequence, while `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md` contains the 1999-1997 PROFONANPE/TVE/Arca/Klohn/SNC Lavalin sequence.
- The aggregate converted file at `raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md` currently includes both page-5 candidate readings in different sections, so it does not resolve which derivative controls physical page 5.
- The chunk manifest duplicates `CHUNK-fb0a0000636f-P0005-01` with different character counts and hashes, and the source packet reports observed converted/chunk hashes that differ from recorded metadata.
- The manifest records `page-images/page-0005.jpg`, but the local page image and extracted image path checked for page 5 were unavailable, so direct visual verification was not possible in this review.
- The page body in both candidate readings does not independently name `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, parent candidates, spouse, child, grandchild, or Alexander John Heinz. Subject attribution remains document-level from title/path/metadata only.
- No canonical person, relationship, or claim should be updated from this staged draft until conversion QA certifies the controlling page-5 transcript and a separate identity bridge is reviewed.

## Scores

| metric | score | rationale |
| --- | ---: | --- |
| source_quality_score | 0.55 | A curriculum vitae is potentially useful for self-reported work history, and the source title identifies Dario Arturo Pulgar, but the raw PDF and page image were unavailable locally for direct verification. |
| conversion_confidence_score | 0.12 | Two incompatible page-5 derivatives, duplicate manifest rows, hash mismatches, and unavailable page image prevent confidence in page control. |
| evidence_quantity_score | 0.42 | There is substantial derivative text, but only for occupational sequences; there is no page-local identity bridge or relationship evidence. |
| agreement_score | 0.18 | The assigned chunk, page Markdown, aggregate converted file, and manifest metadata do not agree enough to choose a controlling transcription. |
| identity_confidence_score | 0.50 | Document-level attribution to Dario Arturo Pulgar is plausible from the source title, but page-local identity and canonical `Dario Arturo Pulgar-Smith` attachment are unproved. |
| claim_probability | 0.30 | The claim that a page-control conflict exists is high probability, but any specific page-5 work-history claim has low probability until the controlling page is certified. |
| relevance_level | high | The CV subject and work-history content are family-relevant if the document-level identity is later bridged correctly. |
| relevance_confidence | 0.86 | The source packet and file paths consistently place this in the Dario Arturo Pulgar CV workflow, even though page control is blocked. |
| canonical_readiness | 0.02 | Not ready for canonical promotion because conversion control and identity attachment are unresolved. |

## Evidence Strengths

- The staged draft accurately identifies the dominant problem as a page-control/provenance conflict rather than a resolved biographical contradiction.
- The assigned chunk literally supports only the 1979-1982 HABITAT, 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, and 1970-1972 CITELCO work-history sequence as derivative text.
- The competing page Markdown literally supports only the 1999 PROFONANPE/TVE, 1998-1999 Arca Consulting/European Commission, 1997-1998 Klohn Crippen Consultants, and SNC Lavalin Agriculture sequence as derivative text.
- The source packet correctly warns that no family relationship is stated in the assigned derivative chunk and that canonical attachment to `Dario Arturo Pulgar-Smith` requires separate identity-bridge proof.

## Claim Judgment

The reviewed staged draft should remain on hold. It is well supported as a conversion/page-control conflict and as a warning against identity or relationship promotion, but it does not support selecting either occupational sequence as the physical page-5 reading. It also does not support merging document-level `Dario Arturo Pulgar` with `Dario Arturo Pulgar-Smith`, Pulgar-Arriagada candidates, or Jose/Juana parent clusters.

## Next Action

Run conversion QA for physical page 5: restore or re-render the page image from the source PDF, compare it against both page-5 derivative readings, reconcile the duplicate manifest rows and hash drift, and certify one controlling transcript. After that, run a separate identity-bridge proof review before attaching any page-5 CV claims to a canonical person.
