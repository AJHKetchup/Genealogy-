---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260528200643293
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260528173924316.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260528173924316.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-row-control-postconv-evidence-extraction-20260528165422297.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260528165422297.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Do not promote from the current converted Markdown as-is. Its entry `172` is a different Burgos/de la Cruz birth entry, while the source image, assigned chunk, source packet, and conversion review support physical row `172` as a Pulgar/Arriagada birth registration.
2. Do not promote the father's terminal mark or suffix. The assigned chunk reads `Jose del Carmen Pulgar S.`, but the targeted image review certifies only `Jose del Carmen Pulgar`; the visible image is consistent with a possible trailing mark, but not clear enough here to promote it.
3. Do not merge or attach this row to any Dario-line person. The source row does not name Dario, Arturo, Smith, Alexander John Heinz, a spouse, a child of a later Dario, or any later-life identifier.
4. Do not treat Burgos/de la Cruz as a name variant or duplicate of Pulgar/Arriagada. It is a derivative conversion conflict for this task, not relationship or identity evidence.
5. Parent relationships are source-stated for this row but should remain staged until the row-control conflict is handled in the normal claim workflow.

## Evidence Strengths

- The source image shows page 58, physical row `172`, with child name `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`, registration date `Siete de Abril de mil ochocientos ochenta i ocho`, and birth date/time/place matching the assigned chunk.
- The source image, assigned chunk, source packet, and targeted conversion review agree that physical entry `172` names the parents as `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`, with residence at `Calle de Colipi`.
- The informant/declarant evidence is internally consistent across the source image and assigned chunk: `Ernesto Herrera L.`, present at the birth, age 26, employed, resident at `Calle de Valdivia`.
- The staged identity analysis correctly preserves the conflict boundary: it accepts the Pulgar/Arriagada row-control evidence while holding Dario-line bridges and broader identity merges.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 |
| conversion_confidence_score | 8/10 for the assigned chunk and row-control packet; 2/10 for the conflicting converted Markdown entry `172`; 6/10 for the father field because the base name is supported but the terminal mark is not |
| evidence_quantity_score | 5/10 |
| agreement_score | 8/10 among source image, assigned chunk, packet, and conversion review for the Pulgar/Arriagada row; 2/10 when the older converted Markdown is included |
| identity_confidence_score | 8/10 for the narrow source-row identity of `Jose del Carmen Segundo Pulgar Arriagada`; 6/10 for source-stated parents as named in this row; 1/10 or lower for any Dario-line bridge |
| claim_probability | 0.90 that physical row `172` is the Pulgar/Arriagada birth registration; 0.88 that the child is source-named `Jose del Carmen Segundo Pulgar Arriagada`; 0.82 that the mother is source-named `Juana Arriagada de Pulgar`; 0.72 that the father base name is `Jose del Carmen Pulgar`; 0.10 for promoting `Pulgar S.`; 0.01-0.04 for Dario-line attachment |
| relevance_level | high |
| relevance_confidence | 0.95 |
| canonical_readiness | hold for canonical promotion until the conversion conflict and father-name boundary are explicitly handled; ready only as a reviewed staging decision that the Burgos/de la Cruz text is not the image-controlled row |

## Review Finding

The staged identity analysis is substantially supported as a conflict-control and anti-conflation note. The strongest supported conclusion is that physical row `172` on page 58 is the birth registration for `Jose del Carmen Segundo Pulgar Arriagada`, with source-stated parents `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.

The current converted Markdown should not be used for this row without correction or an explicit conflict note, because it gives a materially different child, parent set, birth date, place, and declarant context. This conflict lowers canonical readiness even though the image-controlled row reading is strong.

## Next Action

Hold this staged draft from canonical promotion. The next action is to accept the row-control QA for the narrow Pulgar/Arriagada physical row, preserve the Burgos/de la Cruz text as a derivative conversion conflict, and stage only bounded claims: child name, sex, registration date, birth date/time/place, mother name, father base name, parent residence, and informant details. Keep the father suffix and all Dario-line identity bridges out of canonical claims pending separate proof review.
