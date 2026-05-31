---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530235734849
task_id: proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530231621335.md
staged_draft: research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530231621335.md
reviewed_source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-hold-postconv-evidence-extraction-20260530224457988.md
reviewed_chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
reviewed_converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
reviewed_conversion_job_page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
source_quality_score: 0.42
conversion_confidence_score: 0.15
evidence_quantity_score: 0.52
agreement_score: 0.18
identity_confidence_score: 0.36
claim_probability: 0.88
relevance_level: high
relevance_confidence: 0.93
canonical_readiness: hold
---

# Proof Review: Page-Control Conflict Identity Analysis

Reviewed staged draft:
`research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530231621335.md`

## Blockers First

1. The staged draft's central hold recommendation is supported. The assigned chunk for `CHUNK-fb0a0000636f-P0005-01` transcribes page 5 as a 1979-1970 CV work-history page, while `page-markdown/page-0005.md` transcribes page 5 as a 1999-1997 CV work-history page.
2. The physical page image cannot be used for adjudication from this review context. The source manifest references `page-images/page-0005.jpg`, but the `page-images` directory/path is absent in the workspace.
3. Provenance is unstable. The source packet records converted SHA-256 drift, and direct hash checks confirm the current converted file hash is `DA9EC0C3A0F604B4C0E827A2A733A0BA013DD60D86ABEA2B46490D9F8820D288`, not the recorded `fb0a0000636f...` value in the chunk metadata.
4. The chunk manifest duplicates `CHUNK-fb0a0000636f-P0005-01` with conflicting `chars` and `sha256` values. Neither manifest hash matches the current chunk hash `D6EA4F611EE03000C11CBBA63246E95B55F8A421FCBC87D0D667E91F5C8D0B8D`.
5. The reviewed page body does not independently identify `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, parents, spouse, child, grandchild, or Alexander John Heinz. No relationship or same-person merge is supportable from this draft.

## Evidence Strengths

- The draft accurately separates verification from transcription and does not choose between the two incompatible derivative transcriptions.
- The source packet directly supports the conclusion that this item should remain held for conversion QA.
- The literal texts in the assigned chunk and page-markdown file are internally coherent CV work-history text, so the conflict is about page control/provenance rather than invented content.
- The document/source title context supports relevance to the Dario Arturo Pulgar research cluster, but only at a provisional document-title level.

## Scores

| Metric | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.42 | A CV is a useful derivative identity/work-history source, but the original page image is unavailable here and page control is disputed. |
| conversion_confidence_score | 0.15 | Two competing page-5 transcriptions, missing page image, converted hash drift, and duplicate manifest entries block conversion reliance. |
| evidence_quantity_score | 0.52 | There is enough local artifact evidence to prove a page-control conflict, but not enough to prove either page-5 work-history sequence or an identity bridge. |
| agreement_score | 0.18 | The assigned chunk, converted file sections, page-markdown file, manifest data, and observed hashes materially disagree. |
| identity_confidence_score | 0.36 | The source title names Dario Arturo Pulgar, but the reviewed page body does not carry independent identity anchors or relationship facts. |
| claim_probability | 0.88 | High probability that the staged draft's claim of a page-control/provenance conflict is correct. Low probability for any promoted work-history or relationship claim. |
| relevance_level | high | The item is relevant to the Dario Arturo Pulgar CV cluster and to preventing Pulgar-line conflation. |
| relevance_confidence | 0.93 | Relevance is supported by the source title, source packet, matched terms, and draft scope. |
| canonical_readiness | hold | Not ready for canonical claims, relationships, person merges, page renames, or wiki edits. |

## Claim Probability By Review Question

| Review question | Probability | Disposition |
| --- | ---: | --- |
| Is the staged draft correct that page control is blocked? | 0.88 | Support; keep held. |
| Does the assigned chunk prove the 1979-1970 sequence as physical page 5? | 0.32 | Hold; conflicting page-5 transcription and missing image prevent reliance. |
| Does `page-markdown/page-0005.md` prove the 1999-1997 sequence as physical page 5? | 0.34 | Hold; conflicting assigned chunk and provenance drift prevent reliance. |
| Does this draft support attaching CV facts to canonical `Dario Arturo Pulgar-Smith`? | 0.20 | Do not attach from this evidence. |
| Does this draft support any parent, spouse, child, grandchild, or Pulgar-Arriagada relationship claim? | 0.01 | Unsupported. |

## Next Action

Keep this staged draft on hold for conversion QA. The next worker should locate or regenerate the physical page-5 image/PDF rendering, reconcile the duplicate chunk manifest entries and hash drift, and then certify the controlling page-5 transcription before any work-history claim proof review or identity-bridge review proceeds.
