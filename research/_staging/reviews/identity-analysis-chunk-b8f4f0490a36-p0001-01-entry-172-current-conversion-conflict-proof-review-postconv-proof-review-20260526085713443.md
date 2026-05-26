---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260526085713443
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526045537904.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526045537904.md
reviewed: 2026-05-26
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Current Conversion Conflict

## Blockers First

- Canonical readiness is `hold_for_conversion_qa`. The staged identity analysis correctly identifies a material row-level conflict between the current converted Markdown and the current chunk/source packet for the same source and entry number.
- The current converted Markdown reads entry `172` as `José Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`; the current chunk and source packet read entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`.
- The visible page image appears to support the Pulgar/Arriagada row for entry `172`, but this review is not a conversion-correction pass and must not rewrite the canonical conversion from proof review alone.
- The father-field reading remains sensitive. Do not normalize `Jose del Carmen Pulgar S.` to `Jose del Carmen Pulgar` or any other canonical father identity until conversion QA certifies the source reading and identity review follows.
- No Dario-line bridge is supported. This staged draft does not support attaching entry `172` to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada`.

## Evidence Scores

| Metric | Score / Level | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth register image is a high-quality source type for birth, parent, date, place, and informant claims, though the image is a scanned register page and some handwriting remains interpretive. |
| conversion_confidence_score | 0.38 | Derivative conversion artifacts disagree on nearly every substantive field for entry `172`. The image favors the chunk, but the conversion set is not internally stable. |
| evidence_quantity_score | 0.62 | One source image plus multiple derivative artifacts were available; all evidence traces to the same source, so quantity is moderate rather than independently corroborative. |
| agreement_score | 0.44 | Chunk, source packet, staged conflict draft, and visible image broadly agree on Pulgar/Arriagada, but the converted Markdown directly conflicts. |
| identity_confidence_score | 0.64 | The Pulgar/Arriagada child identity is plausible if the chunk controls, but identity confidence remains capped by the unresolved conversion conflict. |
| claim_probability | 0.68 | It is more likely than not that entry `172` is the Pulgar/Arriagada row, based on the chunk and visible image; not high enough for canonical promotion while the converted file conflicts. |
| relevance_level | high | If confirmed, this is directly relevant to Pulgar/Arriagada parent-child identity and birth claims. |
| relevance_confidence | 0.90 | The Pulgar and Arriagada names are directly present in the chunk and visible source row. |
| canonical_readiness | hold_for_conversion_qa | Conversion QA must resolve the controlling row and father-field reading before claims or relationships are promoted. |

## Evidence Strengths

- The staged identity-analysis draft accurately reports the conflict between the current converted Markdown and the chunk/source packet.
- The referenced source packet preserves the Pulgar/Arriagada reading and explicitly flags low conversion confidence and `hold_for_conversion_qa`.
- The referenced page image visibly places `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar S.`, and `Juana Arriagada de Pulgar` in the row marked `172`, which strengthens the probability that the converted Markdown is stale or row-misaligned.
- The staged draft appropriately refuses a same-person merge, parent normalization, or Dario-line attachment.

## Claim Judgments

| Claim | Judgment | Probability | Notes |
| --- | --- | ---: | --- |
| Entry `172` is a Pulgar/Arriagada birth row. | Hold pending conversion QA | 0.68 | Supported by chunk/source packet and visible image; contradicted by current converted Markdown. |
| Child is `Jose del Carmen Segundo Pulgar Arriagada`. | Hold pending conversion QA | 0.66 | Plausible from the row image and chunk, but canonical conversion conflict blocks promotion. |
| Father is `Jose del Carmen Pulgar S.`. | Hold pending conversion QA | 0.61 | The `S.` reading is plausible and should be preserved as written, but needs targeted father-field certification. |
| Mother is `Juana Arriagada de Pulgar`. | Hold pending conversion QA | 0.66 | Plausible from the row image and chunk; dependent on row-control decision. |
| Entry `172` supports a Dario Pulgar identity bridge. | Reject for this draft | 0.03 | No Dario, Arturo, Smith, later-life event, or identity bridge appears in the reviewed evidence. |
| The Burgos/de la Cruz converted-file reading controls entry `172`. | Doubtful, hold for QA | 0.18 | It is present in the converted Markdown but is not supported by the chunk or visible image reviewed here. |

## Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` and the source image. The QA note should decide whether the controlling entry `172` row is Pulgar/Arriagada or Burgos/de la Cruz, then certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, rerun proof review before promoting any child identity, birth fact, parent-child relationship, father candidate, mother candidate, or Dario-line comparison to canonical folders.
