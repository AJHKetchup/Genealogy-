---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260531015743793
task_id: "proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531002844237.md"
staged_draft: "research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531002844237.md"
source_packet: "research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-hold-postconv-evidence-extraction-20260531000652338.md"
conflict_candidate: "research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260531000652338.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
conversion_job_page_markdown: "raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md"
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
claim_probability: 0.45
relevance_level: high
relevance_confidence: 0.95
canonical_readiness: hold_not_ready
---

# Proof Review: CV Page 5 Control Conflict

## Blockers First

1. Keep this staged draft on hold. The assigned chunk and aggregate converted file include the 1979-1970 HABITAT/National Film Board of Canada/Chile Films/CITELCO sequence, but the conversion-job `page-markdown/page-0005.md` includes the 1999-1997 PROFONANPE/TVE/Arca/Klohn Crippen/SNC Lavalin sequence.
2. The physical control source is unavailable in this checkout. `raw/sources/CV of Dario Arturo Pulgar.pdf`, the page image, and the extracted image for page 5 were not present when checked.
3. Provenance remains unstable. The source packet records observed hash drift, and the chunk manifest contains duplicate `CHUNK-fb0a0000636f-P0005-01` entries with different character counts and hashes.
4. No work-history, place, chronology, identity-merge, name-variant, or relationship claim from this page is ready for canonical promotion.
5. The reviewed page evidence does not state parents, spouse, children, grandchild, Alexander John Heinz, `Pulgar-Smith`, `Pulgar-Arriagada`, or any Jose/Juana relationship bridge.

## Evidence Strengths

- The staged draft correctly treats the problem as a page-control/conversion conflict before treating it as an identity conflict.
- The local derivative files support the narrow finding that two incompatible page-5 transcriptions exist.
- Both competing derivative transcriptions are readable typed CV text, so the likely issue is control/provenance, not an unreadable source page.
- The source title gives document-level relevance to `Dario Arturo Pulgar`, but not enough to attach the page evidence to a canonical person page or relationship.

## Scored Judgment

| metric | score | judgment |
| --- | ---: | --- |
| source_quality_score | 2/10 | The cited original PDF and page image are absent locally, so only derivatives can be checked. |
| conversion_confidence_score | 2/10 | Competing page-5 derivatives, duplicate manifest entries, and hash drift prevent certification. |
| evidence_quantity_score | 4/10 | Several local derivatives exist, but none resolves the physical page-control question. |
| agreement_score | 2/10 | Agreement is limited to the existence of a conflict; the page text itself disagrees materially. |
| identity_confidence_score | 5/10 | Moderate only for document-level `Dario Arturo Pulgar`; low for any canonical same-person attachment. |
| claim_probability | 0.45 | A specific page-5 work-history claim may be true to the CV, but current page control is unproved. |
| relationship_claim_probability | 0.05 | No relationship statement is present in the reviewed page evidence. |
| relevance_level | high | The review directly concerns the assigned staged draft and referenced local files. |
| relevance_confidence | 0.95 | The derivative conflict and hold recommendation are strongly relevant. |
| canonical_readiness | hold_not_ready | Not ready for `research/claims`, `research/relationships`, or canonical wiki updates. |

## Review Finding

The staged draft is supported as a hold/revise item. The only well-supported claim is that the local derivative chain contains an unresolved page-control conflict for page 5 of the CV source. The available evidence does not establish whether the physical page 5 is represented by the 1999-1997 consulting text or the 1979-1970 work-history text.

Literal support is insufficient for canonical occupational, geographic, chronological, same-person, name-variant, or family-relationship claims. The draft's caution against merging or attaching Pulgar candidate identities is appropriate because the reviewed page evidence contains no relationship bridge and no independent full-name variant beyond document-level `Dario Arturo Pulgar`.

## Next Action

Conversion/source QA should restore or re-render the authoritative PDF/page image for page 5, compare it visually against both derivative transcriptions, and reconcile the duplicate manifest/hash drift. After page control is certified, rerun proof review only for the surviving page-5 claims; any attachment to `Dario Arturo Pulgar-Smith` or separation from Pulgar-Arriagada/Jose/Juana candidates should be handled as a separate identity-bridge review.
