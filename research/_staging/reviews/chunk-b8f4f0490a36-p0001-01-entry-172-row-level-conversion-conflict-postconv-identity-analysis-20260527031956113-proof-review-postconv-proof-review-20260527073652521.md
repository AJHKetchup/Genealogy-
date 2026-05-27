---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260527073652521
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527031956113.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260527031956113.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260527020803650.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260527020803650.md"
conversion_review_note: "research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260527020803650.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

- The staged draft is correctly held because the current converted Markdown assigns entry `172` to `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, while the chunk, source packet, targeted QA note, and visible source image place physical row `172` on the Pulgar/Arriagada row.
- The father field should remain bounded to `Jose del Carmen Pulgar`; the terminal mark after `Pulgar` is visible but not reliable enough in this review to certify `S.` or any expanded suffix.
- No Dario identity bridge is present. This source names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario, and does not establish attachment to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada`.
- No same-person merge is supported for the Jose/Juana parent candidates. `Juana Arriagada de Pulgar` must not be equated with `Juana de Dios Amagada de Pulgar` from this source alone.
- Canonical promotion must wait for conversion-control reconciliation or annotation of the derivative converted Markdown conflict.

## Evidence Scoring

| Review dimension | Score / level | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.92 | Civil birth-register image is a strong primary source for the row-level facts visible in entry 172. |
| conversion_confidence_score | 0.62 | High for the chunk and image-reviewed Pulgar/Arriagada row; reduced overall because the current converted Markdown contains a contradictory Burgos/de la Cruz entry. |
| evidence_quantity_score | 0.74 | One primary image plus aligned chunk, source packet, and targeted QA note; not enough for cross-person identity merges. |
| agreement_score | 0.63 | Source image, chunk, packet, and QA agree on Pulgar/Arriagada, but the converted file materially disagrees. |
| identity_confidence_score | 0.89 | High that physical row 172 is `Jose del Carmen Segundo Pulgar Arriagada`; low for any Dario or cross-parent merge. |
| claim_probability | 0.90 | Probable that the row-control finding is correct for the literal entry-172 Pulgar/Arriagada facts, with suffix and derivative conflict held. |
| relevance_level | high | Relevant to Pulgar/Arriagada family evidence and conversion conflict control. |
| relevance_confidence | 0.96 | The staged draft and source materials all target the same entry 172 row conflict. |
| canonical_readiness | hold | Suitable as a proof-reviewed hold note, not as canonical claims or relationship promotion. |

## Evidence Strengths

- The source image shows page 58 with entry number `172` aligned to the row containing `Jose del Carmen Segundo Pulgar Arriagada`.
- The visible row supports the core staged facts: registration date `Siete de Abril de mil ochocientos ochenta i ocho`, child name `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`, birth date/time `Ocho de Marzo ... a las tres de la tarde`, birth place `Calle de Valdivia`, father `Jose del Carmen Pulgar`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The assigned chunk agrees with the Pulgar/Arriagada row for entry 172, except that its father-name suffix should remain uncertified.
- The source packet and targeted QA note correctly preserve the derivative conflict instead of silently merging Burgos/de la Cruz facts into the Pulgar/Arriagada family.

## Review Judgment

Accept the staged draft's main proof position: physical entry `172` is a Pulgar/Arriagada birth-registration row, and the Burgos/de la Cruz reading in the current converted Markdown is a derivative conversion conflict for this task.

Revise or hold any claim that would promote `Jose del Carmen Pulgar S.`, bridge the record to any Dario identity, merge Jose parent candidates, merge Juana variants, or create canonical child-parent relationships before conversion-control resolves the conflicting derivative file.

## Next Action

1. Keep this staged identity analysis on `hold`.
2. Send the converted Markdown conflict to conversion-control for reconciliation, supersession, or annotation.
3. After row control is resolved, perform a separate parent-identity proof review for `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` against other Jose/Juana contexts.
4. Do not promote canonical claims, relationships, person merges, family pages, or Dario-line attachments from this staged draft.
