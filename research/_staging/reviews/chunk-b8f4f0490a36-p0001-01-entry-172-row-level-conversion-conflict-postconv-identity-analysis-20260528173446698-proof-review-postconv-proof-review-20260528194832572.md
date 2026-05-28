---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260528194832572
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260528173446698.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260528173446698.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-row-control-postconv-evidence-extraction-20260528165422297.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260528165422297.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
canonical_readiness: hold_for_conversion_conflict_resolution
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Canonical promotion must remain on hold because the current converted Markdown assigns entry `172` to `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, while the source image, assigned chunk, source packet, and targeted QA note identify physical entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.
2. The father field is supported only as `Jose del Carmen Pulgar` for this review. The assigned chunk reads `Jose del Carmen Pulgar S.`, but the targeted QA note does not certify the terminal `S.` and the image does not make that suffix safe to promote here.
3. The staged identity analysis is correct to reject any Dario-line attachment from this row. The visible source does not name Dario, Arturo, Smith, `Dario Jose Pulgar-Arriagada`, or `Dario Pulgar Arriagada`.
4. The parent-child relationship is directly relevant and probably correct at the row level, but it should be promoted only after the row-control conflict is resolved or explicitly preserved as a superseded derivative-conversion conflict.

## Evidence Reviewed

- Staged draft under review: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260528173446698.md`.
- Source packet: `research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-row-control-postconv-evidence-extraction-20260528165422297.md`.
- Conversion QA note: `research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260528165422297.md`.
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Conflicting converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Source page image: visually checked for row control and name support.

## Evidence Strengths

- The original page image shows entry `172` on page 58 as a Pulgar/Arriagada birth registration and supports the row-control correction made in the QA note.
- The assigned chunk materially agrees with the image-reviewed row: registration date 7 April 1888; child `Jose del Carmen Segundo Pulgar Arriagada`; male; birth 8 March 1888 at 3 p.m.; place `Calle de Valdivia`; mother `Juana Arriagada de Pulgar`; parents' residence `Calle de Colipi`; informant `Ernesto Herrera L.`.
- The converted Markdown conflict is not a minor transcription variant. It differs on child, parents, birth date, birth place, surrounding entries, and official/signature context.
- The staged identity analysis keeps source transcription separate from identity inference and correctly treats Dario-line links as unsupported by this row.

## Scored Judgment

| Item | source_quality_score | conversion_confidence_score | evidence_quantity_score | agreement_score | identity_confidence_score | claim_probability | relevance_level | relevance_confidence | canonical_readiness |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | --- |
| Physical entry `172` is the Pulgar/Arriagada row, not the Burgos/de la Cruz converted text. | 0.92 | 0.82 | 0.84 | 0.78 | 0.91 | 0.91 | high | 0.95 | hold_for_conversion_conflict_resolution |
| Child is recorded as `Jose del Carmen Segundo Pulgar Arriagada`. | 0.92 | 0.84 | 0.82 | 0.86 | 0.90 | 0.90 | high | 0.94 | ready_after_row_control_acceptance |
| Father is recorded as `Jose del Carmen Pulgar`, with terminal `S.` unresolved. | 0.88 | 0.74 | 0.75 | 0.70 | 0.72 | 0.76 | high | 0.90 | revise_suffix_before_promotion |
| Mother is recorded as `Juana Arriagada de Pulgar`. | 0.90 | 0.84 | 0.80 | 0.86 | 0.84 | 0.86 | high | 0.93 | ready_after_row_control_acceptance |
| Row supports parent-child claims for Jose/Juana as parents of the child. | 0.90 | 0.80 | 0.78 | 0.82 | 0.80 | 0.83 | high | 0.92 | hold_until_conversion_conflict_documented |
| Burgos/de la Cruz entry is a variant or duplicate of the Pulgar/Arriagada row. | 0.30 | 0.15 | 0.20 | 0.05 | 0.03 | 0.02 | conflict-control | 0.88 | not_ready_reject_as_identity_evidence |
| Any Dario, Arturo, Smith, or Dario Pulgar identity attachment from this row. | 0.12 | 0.84 | 0.05 | 0.00 | 0.02 | 0.02 | anti-conflation | 0.86 | not_ready_no_source_support |

## Review Decision

The staged identity analysis is supported as a conflict-control note and should remain `hold_for_proof_review` or move to a revise/hold state until the conversion conflict is handled. The best-supported row-level conclusion is that physical entry `172` records `Jose del Carmen Segundo Pulgar Arriagada`, with parents `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.

Do not promote the Burgos/de la Cruz text as evidence for this source. Do not promote the terminal father-name suffix `S.` from this review. Do not attach this row to any Dario-line person or merge these source-named people with canonical stubs from this row alone.

## Next Action

Accept the targeted row-control QA for entry `172`, preserve the converted Markdown's Burgos/de la Cruz content as a derivative conversion conflict, and prepare only narrow row-level claims after the conflict is explicitly documented. Any broader identity merge, parent-candidate merge, father suffix certification, or Dario-line comparison needs a separate proof review with direct bridge evidence.
