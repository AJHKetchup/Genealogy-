---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260528194409696
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260528173446698.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260528173446698.md"
reviewed_claim_type: identity_conflict_analysis
reviewed_subject: "Los Angeles birth register entry 172"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-row-control-postconv-evidence-extraction-20260528165422297.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260528165422297.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
source_page_image_checked: "yes; original page image reviewed for physical row 172 on page 58"
source_quality_score: 0.88
conversion_confidence_score: 0.80
evidence_quantity_score: 0.66
agreement_score: 0.72
identity_confidence_score: 0.88
claim_probability: 0.89
relevance_level: high
relevance_confidence: 0.93
canonical_readiness: hold_for_conversion_conflict_resolution
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers

- Canonical readiness is `hold_for_conversion_conflict_resolution`. The source image, assigned chunk, source packet, and conversion-review note support physical entry `172` as the Pulgar/Arriagada birth registration, but the current converted Markdown records a materially different Burgos/de la Cruz entry under the same number.
- The father-name suffix remains unresolved. The assigned chunk reads `Jose del Carmen Pulgar S.`, while the image-reviewed row-control note certifies only `Jose del Carmen Pulgar`; no claim should promote the terminal `S.` from this review.
- The staged identity analysis correctly rejects Dario-line attachment from this row. Entry `172` does not name Dario, Arturo, Smith, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`, so any such merge or relationship would be an unsupported identity jump.
- Existing canonical stubs or family-supplied pages are not sufficient bridge evidence for same-person conclusions about the parents. This review verifies row-level support only and does not certify merges to canonical people.

## Evidence Strengths

- The original page image visibly places physical row `172` on page 58 as a Pulgar/Arriagada birth entry, not the Burgos/de la Cruz text found in the converted Markdown.
- The assigned chunk and source packet agree that row `172` records `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at 3 p.m. on Calle de Valdivia.
- The same row names parents as `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`, with residence at Calle de Colipi, and names `Ernesto Herrera L.` as informant.
- The staged identity analysis preserves the conversion conflict instead of treating Burgos/de la Cruz as a spelling variant, duplicate, or alternate identity for the Pulgar/Arriagada child.

## Scored Judgment

- `source_quality_score: 0.88` - civil birth register image, contemporary to the event, with direct row-level parent and child evidence.
- `conversion_confidence_score: 0.80` - high for row control after image review and chunk agreement; reduced because the canonical converted Markdown is the conflicting derivative text and the father suffix is not certified.
- `evidence_quantity_score: 0.66` - one primary page image plus staged row-control notes and chunk transcription; no independent corroborating record reviewed for this task.
- `agreement_score: 0.72` - source image, chunk, packet, and QA note agree on the Pulgar/Arriagada row, but the converted Markdown strongly disagrees.
- `identity_confidence_score: 0.88` - high that physical row `172` is the source-named child `Jose del Carmen Segundo Pulgar Arriagada`; lower for attaching parents to any broader canonical identities.
- `claim_probability: 0.89` - probable that the physical row supports the Pulgar/Arriagada birth registration and rejects the Burgos/de la Cruz derivative reading for this row.
- `relevance_level: high`; `relevance_confidence: 0.93` - directly relevant to Pulgar/Arriagada parent-child evidence and to preventing Dario-line conflation.
- `canonical_readiness: hold_for_conversion_conflict_resolution`.

## Review Judgment

The staged identity analysis is literally supported as a conflict-control note. It should remain in staging until the conversion conflict is resolved or explicitly documented in the promotion path. The row-level claim for `Jose del Carmen Segundo Pulgar Arriagada` is strong, and the source names `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` as parents, but this review does not certify parent identity merges beyond the source-literal row.

## Next Action

Resolve the derivative converted Markdown conflict before canonical promotion. If the row-control QA is accepted, promote only narrow source-literal evidence for physical entry `172`: child `Jose del Carmen Segundo Pulgar Arriagada`, mother `Juana Arriagada de Pulgar`, father bounded to `Jose del Carmen Pulgar`, and the birth/registration details. Keep the father suffix and all Dario-line identity bridges on hold pending separate proof.
