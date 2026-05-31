---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260531000215236
task_id: proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530231621335.md
staged_draft: research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530231621335.md
reviewed_conflict_draft: research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260530224457988.md
reviewed_source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-hold-postconv-evidence-extraction-20260530224457988.md
reviewed_chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
reviewed_converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
reviewed_conversion_job_page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
source_quality_score: 0.42
conversion_confidence_score: 0.16
evidence_quantity_score: 0.58
agreement_score: 0.22
identity_confidence_score: 0.34
claim_probability: 0.90
relevance_level: high
relevance_confidence: 0.92
canonical_readiness: not_ready
promotion_recommendation: hold_for_conversion_qa
---

# Proof Review: Page-Control Conflict Identity Analysis

This review covers only the staged draft `research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530231621335.md` and the local artifacts it references.

## Blockers First

1. Canonical readiness is `not_ready`. The reviewed draft is correct to hold because the assigned chunk and conversion-job page Markdown both claim page 5 but transcribe materially different CV periods.
2. The source image for `page-images/page-0005.jpg` is unavailable in the reviewed conversion job, so I could not adjudicate which derivative text matches the physical page.
3. Provenance is unstable. The source packet records a mismatch between the chunk-recorded converted SHA-256 and the observed converted SHA-256, and the chunk manifest repeats `CHUNK-fb0a0000636f-P0005-01` with conflicting character counts.
4. The page body reviewed here is not identity-bearing beyond the document title and CV context. It does not independently name `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, parents, spouse, child, grandchild, or Alexander John Heinz.
5. No work-history, family relationship, same-person merge, person-page rename, or canonical wiki update should be promoted from this draft.

## Scored Judgment

| Field | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.42 | The underlying source is a CV PDF with a stable source title and source SHA-256 in metadata, but the physical page image was not available for review. |
| conversion_confidence_score | 0.16 | Two page-5 derivative texts disagree, aggregate conversion text contains both sequences, and manifest/hash issues remain unresolved. |
| evidence_quantity_score | 0.58 | There are several local derivative artifacts, but they are derivative and conflicting; there is no image-level verification. |
| agreement_score | 0.22 | The artifacts agree that this is a page-control conflict, but they do not agree on the controlling page-5 text. |
| identity_confidence_score | 0.34 | Document-level title supports a provisional CV subject, but the disputed page body supplies no independent identity bridge to a canonical person. |
| claim_probability | 0.90 | The claim that this staged analysis correctly identifies a hold-worthy page-control/provenance conflict is well supported. |
| relevance_level | high | The conflict is directly relevant to the Pulgar CV staging and any later identity or work-history use. |
| relevance_confidence | 0.92 | The staged draft, conflict draft, source packet, chunk, and page markdown all point to the same disputed page-control issue. |
| canonical_readiness | not_ready | Conversion QA and identity-bridge review are required before canonical use. |

## Evidence Strengths

- The staged draft accurately reports the central conflict: the assigned chunk begins with the `1979 - 1982` HABITAT sequence, while the conversion-job page Markdown begins with the `1999` PROFONANPE sequence.
- The source packet independently documents the same conflict, notes the absent page image, and recommends `hold_for_conversion_qa`.
- The assigned chunk literally contains the 1979-1970 work-history sequence ending at `EDUCATION`.
- The conversion-job `page-markdown/page-0005.md` literally contains the 1999-1997 consultant sequence and notes the final line is cut off.
- The aggregate converted file contains both the 1999 PROFONANPE text and the 1979 HABITAT text in different locations, reinforcing that the derivative text set is not a single authoritative page-5 reading.

## Identity And Relationship Risk

- Same-person risk is high if document-level `Dario Arturo Pulgar` is attached to `Dario Arturo Pulgar-Smith` by name/title alone.
- Relationship inference risk is high. No reviewed page text states a parent, spouse, child, grandchild, or maternal-grandfather relationship.
- Pulgar-Arriagada conflation risk remains active. This draft does not support `Jose`, `Arriagada`, `Dario Jose Pulgar-Arriagada`, or `Dario Pulgar Arriagada` variants.
- Work-history chronology risk is high because the two candidate page-5 transcriptions cover mutually incompatible date ranges.

## Next Action

Keep the staged draft on `hold_for_conversion_qa`. Locate or restore the physical page image/PDF page, reconcile the manifest duplicate and hash drift, and certify the controlling page-5 transcription before any claim extraction or canonical attachment. After page control is fixed, run a separate identity-bridge proof review before connecting the CV subject to `Dario Arturo Pulgar-Smith` or any Pulgar-Arriagada/Jose/Juana cluster.
