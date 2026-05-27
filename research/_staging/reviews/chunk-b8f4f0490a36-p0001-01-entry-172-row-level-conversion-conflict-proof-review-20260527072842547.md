---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260527072802180
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527031956113.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527031956113.md"
reviewed_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260527020803650.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260527020803650.md"
conversion_review_note: "research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260527020803650.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
canonical_readiness: hold
claim_probability: 0.91
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

- Canonical readiness remains `hold` because the current converted Markdown still records entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, while the source image, assigned chunk, source packet, and targeted QA note support the physical row `172` as the Pulgar/Arriagada entry.
- The father field is only proof-ready as `Jose del Carmen Pulgar`. The terminal mark or suffix after `Pulgar` is not sufficiently reliable for promotion from this review.
- This staged identity analysis does not prove a same-person bridge from this entry to any Dario/Dario Arturo/Dario Jose Pulgar identity.
- This staged identity analysis does not prove that the father `Jose del Carmen Pulgar` is the same person as any existing Jose candidate, or that mother `Juana Arriagada de Pulgar` is the same person as any other Juana variant.
- No canonical claim, relationship, merge, or wiki update should be made from this review until conversion-control reconciles the derivative row conflict.

## Scores

| Dimension | Score / value | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth register image is a strong source, but image resolution/contrast limits the father suffix. |
| conversion_confidence_score | 0.62 | Image-reviewed row control is high, but the derivative converted file directly conflicts with the chunk. |
| evidence_quantity_score | 0.74 | Source image, chunk, source packet, QA note, and converted file were sufficient for row-control review; no independent identity bridge is present. |
| agreement_score | 0.70 | Image, chunk, source packet, and QA note agree on Pulgar/Arriagada, but the converted file disagrees materially. |
| identity_confidence_score | 0.86 | High confidence that physical entry 172 is the Pulgar/Arriagada birth row; low confidence for broader same-person merges. |
| claim_probability | 0.91 | The row-control claim is likely correct: physical row 172 on page 58 is `Jose del Carmen Segundo Pulgar Arriagada`. |
| relevance_level | high | The conflict directly affects Pulgar/Arriagada family evidence and prevents clean canonical promotion. |
| relevance_confidence | 0.96 | The staged draft and referenced materials are all centered on the same entry 172 row-control problem. |
| canonical_readiness | hold | Accept row-control as review-supported, but hold canonical use pending derivative conversion reconciliation and focused identity proof. |

## Evidence Strengths

- The page image shows row number `172` on page 58 aligned with the entry for `Jose del Carmen Segundo Pulgar Arriagada`; the visible parents are `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.
- The assigned chunk transcribes entry `172` as the Pulgar/Arriagada row and matches the staged QA note for child, sex, registration date, birth date/time, birthplace, mother, informant, and official-signature context.
- The source packet and targeted conversion QA note correctly preserve the derivative conflict instead of silently replacing or merging the Burgos/de la Cruz text.
- The staged identity analysis correctly keeps Dario-line attachment, Jose/Juana same-person merges, and parent-child relationship promotion outside this proof review.

## Review Finding

The staged draft is literally supported for its central claim that the current converted Markdown has a row-level conflict: the converted file labels entry `172` as a Burgos/de la Cruz child, while the reviewed source image and assigned chunk support entry `172` as the Pulgar/Arriagada child. The appropriate proof judgment is `hold`, not rejection. The row-control evidence is strong enough to guide later conversion-control work, but not sufficient for canonical promotion while the derivative converted file remains unreconciled.

## Next Action

1. Send this item to conversion-control to reconcile or annotate the converted Markdown conflict for entry `172`.
2. Keep the father name bounded to `Jose del Carmen Pulgar` unless a focused crop or later proof review certifies the terminal suffix.
3. After conversion reconciliation, run a separate parent-identity proof review before merging Jose/Juana candidates or attaching this record to any Dario-line identity.
