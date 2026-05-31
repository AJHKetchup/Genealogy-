---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260531004749754
task_id: "proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531002441462.md"
staged_draft: "research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531002441462.md"
source_packet: "research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-hold-postconv-evidence-extraction-20260531000652338.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
conversion_job_page_markdown: "raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md"
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
canonical_readiness: hold
---

# Proof Review: CV Page 5 Page-Control Conflict

## Blockers First

1. Do not promote occupational, place, chronology, identity-bridge, or relationship claims from this staged draft. Page 5 control is unresolved: the assigned chunk contains a 1979-1970 HABITAT/NFB/Chile Films/CITELCO sequence, while the conversion-job page Markdown for `page_num: 5` contains a materially different 1999-1997 PROFONANPE/TVE/Arca/Klohn Crippen/SNC Lavalin sequence.
2. The source packet's conversion QA blocker is supported. The local `page-images/page-0005.jpg` and `extracted-images/page-0005.jpg` paths are absent, so I could not visually certify which derivative text reflects physical page 5.
3. The chunk manifest contains duplicate entries for `CHUNK-fb0a0000636f-P0005-01` with different character counts, and the source packet reports observed hash drift from recorded converted/chunk metadata. This prevents treating either derivative as controlling proof.
4. The reviewed page text does not independently state a family relationship, parent, spouse, child, grandchild, or connection to Alexander John Heinz. It also does not prove `Pulgar-Smith`, `Pulgar-Arriagada`, or `Dario Jose` variants.

## Evidence Strengths

- The source packet, assigned chunk, aggregate converted file, and conversion-job page Markdown all consistently identify the document source as `CV of Dario Arturo Pulgar.pdf`.
- The assigned chunk is internally readable and supports, only as a derivative reading, entries for HABITAT in Nairobi, the National Film Board of Canada in Montreal, Chile Films in Santiago, and CITELCO in Santiago.
- The conversion-job page Markdown is also internally readable and supports, only as a derivative reading, consulting entries for PROFONANPE, Television Trust for the Environment, Arca Consulting/European Commission, Klohn Crippen Consultants, and SNC Lavalin Agriculture.
- The staged draft correctly treats the issue as a conversion/page-control blocker before any canonical identity or relationship conclusion.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 4/10 |
| conversion_confidence_score | 2/10 |
| evidence_quantity_score | 3/10 |
| agreement_score | 2/10 for page-5 control; 8/10 that the local derivatives are CV-context materials for a source titled `CV of Dario Arturo Pulgar` |
| identity_confidence_score | 5/10 for document-level attribution to the CV title only; 2/10 or lower for same-person attachment to any canonical Dario/Pulgar variant from this page |
| claim_probability | 0.50 that either derivative sequence belongs somewhere in the CV; 0.25 that the assigned chunk is certified physical page 5 without QA; 0.10 or lower for any identity merge or relationship claim |
| relevance_level | high |
| relevance_confidence | 0.95 |
| canonical_readiness | hold / not ready |

## Review Finding

The staged draft is supported as a hold. Its central conclusion is correct: this evidence is not ready for canonical claims because page-control provenance is broken and the page text lacks direct identity-bridge or kinship statements.

The only supported assertion at this stage is narrow and procedural: local derivatives for the same CV source disagree about the content of page 5, and conversion QA must resolve that conflict before any proof review of work-history claims can proceed.

## Next Action

Keep the draft on `hold_for_conversion_qa`. Locate or regenerate a controlled physical page-5 image or page-image equivalent, decide which page-5 transcription is authoritative, reconcile the duplicate/stale manifest and hash metadata, then rerun proof review only for the surviving work-history claims. Identity-bridge review should remain separate and should not infer `Pulgar-Smith`, `Pulgar-Arriagada`, `Dario Jose`, or family relationships from this page alone.
