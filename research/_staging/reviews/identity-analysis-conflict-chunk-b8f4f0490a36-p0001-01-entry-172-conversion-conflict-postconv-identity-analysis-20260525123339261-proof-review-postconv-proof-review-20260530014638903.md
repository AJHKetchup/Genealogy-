---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260530014638903
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-postconv-identity-analysis-20260525123339261.md
staged_draft: research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-postconv-identity-analysis-20260525123339261.md
reviewed_converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
reviewed_chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
reviewed_source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115123585.md
reviewed_qa_note: research/_staging/tasks/conversion-review-note-chunk-b8f4f0490a36-p0001-01-entry-172-row-control-postconv-evidence-extraction-20260529000949107.md
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Identity Conflict Analysis

## Blockers First

- Canonical readiness remains `hold_for_conversion_qa`. The staged draft reviews a real row-level conflict, but dependent claims and relationships should not be promoted from this proof note.
- The staged draft and its 2026-05-25 source packet misstate the current converted Markdown conflict. The converted file reviewed here records entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born `El seis de Abril de mil ochocientos ochenta i ocho`; it does not record `Jose Francisco`, `Oswaldo Gomez`, or `Emilia de la Cruz`.
- The assigned chunk records a different entry `172`: `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born `Ocho de Marzo de mil ochocientos ochenta i ocho` at `Calle de Valdivia`.
- A later row-control QA note reports image review and certifies physical row `172` as the Pulgar/Arriagada row, while bounding the father field to `Jose del Carmen Pulgar` and not certifying the trailing mark as `S.`. This review did not edit or promote that QA result.
- The source image path embedded in the metadata was not available at the literal filesystem path during this review, so this proof review relies on the assigned chunk, converted Markdown, source packet, and the later row-control QA note rather than a new image inspection.
- No Dario attachment is supported. Entry `172`, under the Pulgar/Arriagada row-control reading, names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario.

## Evidence Strengths

- The source type is a Chilean civil birth registration, which is a high-quality record type for a child's birth identity and declared parents when the row is controlled.
- The assigned chunk and the later row-control QA note agree that physical entry `172` is the Pulgar/Arriagada row.
- The row-control QA note directly addresses the main conversion conflict and explains that the converted Markdown's Burgos/de la Cruz reading should be preserved as a derivative conflict, not used as the controlling Pulgar/Arriagada extraction.
- The staged draft correctly treats same-person and Dario-line attachments as unproven and correctly keeps canonical promotion blocked.

## Scored Judgment

| Metric | Score / Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth registration is a strong source class, but the image was not directly available to this reviewer at the metadata path. |
| conversion_confidence_score | 0.58 | Later QA supports row control for Pulgar/Arriagada, but the canonical converted Markdown still conflicts materially with the chunk. |
| evidence_quantity_score | 0.64 | One target record plus derivative chunk, source packet, and row-control QA note; no independent collateral source reviewed. |
| agreement_score | 0.52 | Chunk and later QA agree; converted Markdown and older packet wording conflict. |
| identity_confidence_score | 0.72 | Good confidence that the staged Pulgar/Arriagada child identity is the target row after QA note, reduced by unresolved father trailing mark and derivative file conflict. |
| claim_probability | 0.76 | More likely than not that entry `172` should be treated as the Pulgar/Arriagada birth row for further review, but not ready for canonical use. |
| relevance_level | high | Directly relevant to Pulgar/Arriagada identity, parent claims, and anti-conflation controls. |
| relevance_confidence | 0.90 | The names in the chunk and QA note directly match the staged Pulgar/Arriagada issue. |
| canonical_readiness | hold_for_conversion_qa | Requires reconciled conversion control and follow-up proof review before promotion. |

## Claim-Level Notes

- Child identity as `Jose del Carmen Segundo Pulgar Arriagada`: supported by the assigned chunk and later row-control QA note; held because the converted Markdown remains contradictory.
- Father as `Jose del Carmen Pulgar S.`: revise before promotion. The chunk reads `S.`, but the later QA note bounds the visible support to `Jose del Carmen Pulgar` and does not certify the trailing mark.
- Mother as `Juana Arriagada de Pulgar`: supported by the assigned chunk and row-control QA note if Pulgar/Arriagada row control is accepted.
- Same-person claim with canonical `Jose del Carmen Pulgar`: not proven here. Name compatibility alone is insufficient.
- Same-person or normalization claim between `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar`: not supported; keep as anti-conflation risk.
- Dario-line relationship or identity bridge: not supported; surname context alone is insufficient.

## Next Action

Keep this staged draft on hold. The next worker should reconcile or supersede the converted Markdown so the controlling derivative file no longer assigns entry `172` to the Burgos/de la Cruz row, preserve the father as `Jose del Carmen Pulgar` unless a visible-source QA note certifies the suffix, and then rerun proof review for any child, parent, same-person, or Dario-line claim before canonical promotion.
