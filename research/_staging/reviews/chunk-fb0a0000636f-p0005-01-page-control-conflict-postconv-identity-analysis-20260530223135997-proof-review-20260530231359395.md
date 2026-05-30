---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530231359395
task_id: "proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530223135997.md"
staged_draft: "research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530223135997.md"
source_packet: "research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-work-history-hold-postconv-evidence-extraction-20260530213419489.md"
conflict_candidate: "research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260530213419489.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
canonical_readiness: not_ready
---

# Proof Review: Page-Control Conflict For CV Page 5

## Blockers First

1. Do not promote any page-5 work-history claim from this staged draft yet. The assigned chunk gives a 1979-1982 / 1974-1978 / 1972-1973 / 1970-1972 career sequence, while the conversion job `page-markdown/page-0005.md` gives a conflicting 1999 / 1998-1999 / 1997-1998 sequence.
2. Do not use this item for a same-person merge to `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, or `Dario Pulgar Arriagada`. The page-local text does not repeat a full personal name, surname variant, age, birth, spouse, child, parent, or other bridge fact.
3. The page image expected at `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0005.jpg` is absent in this checkout, so visual verification of the controlling page text is blocked.
4. The chunk manifest lists `CHUNK-fb0a0000636f-P0005-01` twice with different character counts and hashes, and the source packet records a converted-file hash mismatch. This makes the derivative chain unreliable until conversion QA resolves provenance.

## Evidence Strengths

- The assigned chunk is internally readable and supports narrow derivative-text claims for HABITAT in Nairobi, National Film Board of Canada in Montreal, Chile Films in Santiago, and CITELCO in Santiago if that chunk is later certified as the controlling page.
- The aggregate converted file contains both the 1999/1998 text and the 1979-1970 text in different positions, which supports the staged draft's conclusion that this is a page-control/provenance conflict rather than a genealogical relationship conflict.
- The source packet correctly limits identity to the document-level CV title `CV of Dario Arturo Pulgar` and does not treat the page body as an independent name statement.
- No checked derivative text contains Jose/Juana parent candidates, spouse, children, siblings, household members, or a relationship term.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 5/10 for the CV as a potentially direct autobiographical/professional source, but unreviewed visually for this page |
| conversion_confidence_score | 2/10 because page image is missing, page-markdown and chunk text conflict, and manifest/hash metadata are unstable |
| evidence_quantity_score | 3/10 for identity/relationship purposes; 5/10 for later work-history extraction after page control is fixed |
| agreement_score | 2/10 across derivative page-5 records; 8/10 only within the assigned chunk/source-packet pair |
| identity_confidence_score | 6/10 for document-level attribution to `Dario Arturo Pulgar`; 2/10 or lower for any canonical merge or Pulgar-line relationship bridge |
| claim_probability | 0.55 that the assigned chunk may preserve real CV work-history text; 0.20 that it is currently ready to support a claim; 0.05 or lower for any family relationship claim |
| relevance_level | high |
| relevance_confidence | 0.85 |
| canonical_readiness | not_ready; hold_for_conversion_qa |

## Review Finding

The staged identity/conflict analysis is supported as a hold. Its key claim is not that either transcription is proved, but that both competing page-5 derivatives cannot simultaneously control the same page. The checked files support that conclusion.

The safest evidence interpretation is: this is relevant CV material for a document titled `CV of Dario Arturo Pulgar`, but current page-control and provenance defects prevent canonical promotion. The item does not support any family relationship, same-person merge, or silent name expansion.

## Next Action

Send this item to conversion QA. Restore or regenerate the page-5 image, repair the duplicate chunk manifest entries and hash mismatch, and certify whether page 5 is controlled by the 1999/1998 page-markdown text or the 1979-1970 assigned-chunk text. After certification, run a fresh visual proof review before any work-history claim or identity bridge is promoted.
