---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260531042428535
task_id: "proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531003129113.md"
staged_draft: "research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531003129113.md"
source_packet: "research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-hold-postconv-evidence-extraction-20260530234356813.md"
conflict_draft: "research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260530234356813.md"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md"
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
canonical_readiness: hold_conversion_qa_required
---

# Proof Review: CHUNK-fb0a0000636f-P0005-01 Page-Control Identity Analysis

## Blockers First

1. The staged identity analysis should remain on hold. The assigned chunk and current aggregate converted file support a 1979-1982 through 1970-1972 CV work-history page beginning with United Nations Centre for Human Settlements (HABITAT), while the conversion-job page Markdown for page 5 supports a different 1999 through 1997-1998 consulting-work page beginning with PROFONANPE.
2. No page-5 occupational claim is canonically usable yet. The two derivative readings cannot both control the same physical page 5, and the chunk manifest lists `CHUNK-fb0a0000636f-P0005-01` twice with different character counts and SHA-256 values.
3. Page-image verification is blocked in this review. The conversion-job manifest lists `page-images/page-0005.jpg` and `extracted-images/page-0005`, but those paths are not present in the workspace checks performed for this review.
4. Identity attachment to canonical `Dario Arturo Pulgar-Smith` is not proven by this page. The page body in either derivative does not state `Pulgar-Smith`, Alexander John Heinz, a spouse, child, parent, birth detail, or any family relationship.
5. Do not merge this draft with Pulgar-Arriagada or Jose/Juana parent-candidate clusters. Those remain anti-conflation context only because the reviewed page-control materials contain no direct relationship bridge.

## Evidence Strengths

- The staged draft accurately preserves the core page-control conflict and does not try to promote either derivative transcription.
- The source packet and source metadata consistently identify the source package as `CV of Dario Arturo Pulgar`, giving moderate document-level support for the CV subject name.
- The assigned chunk is internally coherent and literally supports the HABITAT/NFB/Chile Films/CITELCO sequence as text in that derivative.
- The conversion-job page Markdown is internally coherent and literally supports the PROFONANPE/TVE/Arca/Klohn Crippen/SNC Lavalin sequence as text in that derivative.
- The staged analysis correctly treats `Dario Arturo Pulgar` versus `Dario Arturo Pulgar-Smith` as an identity question requiring a separate bridge, not a transcription change.

## Scored Judgment

| metric | score | rationale |
|---|---:|---|
| source_quality_score | 5/10 | The source is a local CV PDF with stable document-level title and SHA-256 metadata, but the reviewed page-specific derivatives are unstable. |
| conversion_confidence_score | 1/10 | Physical page-5 control is unresolved; literal confidence applies only within each derivative file, not to which derivative controls page 5. |
| evidence_quantity_score | 3/10 | There is enough local derivative evidence to identify the conflict, but not enough direct evidence for page claims, canonical identity attachment, or relationships. |
| agreement_score | 2/10 | Derivatives agree on the broader CV source package but disagree materially on page-5 text and chronology. |
| identity_confidence_score | 7/10 document-level; 4.5/10 canonical Pulgar-Smith; 1/10 Pulgar-Arriagada/Jose-Juana | The source title supports `Dario Arturo Pulgar`; this page does not bridge to Pulgar-Smith or other Pulgar-line candidates. |
| claim_probability | 0.75 document-level CV subject; 0.50 same person as canonical Pulgar-Smith; 0.05 relationship claims | Page 5 probably belongs to the CV source subject once certified, but no relationship claim is stated and canonical identity remains unproved. |
| relevance_level | high | This review directly addresses the assigned staged draft and its referenced page-control conflict. |
| relevance_confidence | 0.96 | The reviewed files match the staged draft, source packet, converted file, chunk, and conversion-job page Markdown. |
| canonical_readiness | hold_conversion_qa_required | Not ready for claims, relationships, wiki person attachment, or identity merge. |

## Review Finding

The staged identity/conflict analysis is supported as a hold decision. Its strongest supported conclusion is procedural: `CHUNK-fb0a0000636f-P0005-01` requires conversion QA before any page-5 occupational chronology or identity bridge can be used.

The source title and local metadata make `Dario Arturo Pulgar` a reasonable document-level subject label, but this review found no literal page-body support for `Dario Arturo Pulgar-Smith`, Pulgar-Arriagada identity, Jose/Juana parentage, or any family relationship. Normalizing or merging names from this draft would exceed the visible support.

## Next Action

Send the item to conversion QA. QA should restore or inspect the physical page-5 image/PDF page, select the controlling transcription for `CHUNK-fb0a0000636f-P0005-01`, and repair the duplicate manifest/hash drift. After that, run a separate identity-bridge proof review before attaching any certified page-5 fact to `wiki/people/dario-arturo-pulgar-smith.md` or any other canonical person page.
