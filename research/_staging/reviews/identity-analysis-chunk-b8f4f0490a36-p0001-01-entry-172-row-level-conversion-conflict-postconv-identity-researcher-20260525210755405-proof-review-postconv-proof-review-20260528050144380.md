---
type: proof_review
status: hold
role: claim_reviewer
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525210755405.md
reviewer: postconv-proof-review-20260528050144380
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525210755405.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203741061.md
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers

- The staged identity analysis is supported as a hold, not as a promotable claim package. The assigned converted Markdown gives entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, while the assigned chunk gives entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`.
- This is a row-level family-cluster conflict, not a name spelling or variant-reading problem. No child identity, parent identity, birth event, parent-child relationship, or downstream Pulgar/Dario relationship should be promoted from this draft until conversion QA resolves the controlling row.
- Direct image review in this proof-review pass supports the Pulgar/Arriagada row for visible entry 172, but the converted file remains contradictory and must not be edited or bypassed by this review note.
- The father field remains a field-level uncertainty. The chunk reads `Jose del Carmen Pulgar S.`, and the source packet asks QA to decide between `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- Entry 172 does not visibly or derivatively name Dario, Arturo, Smith, or any grandchild link. It cannot support a bridge to any Dario Pulgar identity cluster on its own.

## Evidence Strengths

- The source type is a civil birth register, which is generally high-quality direct evidence for birth registration facts when the row is correctly controlled.
- The assigned chunk gives a coherent complete row for entry 172: registration date 7 April 1888; child `Jose del Carmen Segundo Pulgar Arriagada`; male; birth 8 March 1888 at 3 p.m.; place `Calle de Valdivia`; father `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`
- The source packet explicitly preserves the same Pulgar/Arriagada reading and states that direct image context favored that row while routing the conflict to conversion QA.
- The page image reviewed for this task visibly aligns with the chunk on the main row identity and family cluster for entry 172. The father suffix is not strong enough for final normalization in this review.
- The staged identity analysis correctly separates the Pulgar/Arriagada hypothesis, the Burgos/de la Cruz hypothesis, and the rejected same-person/name-variant hypothesis.

## Scored Judgment

| Metric | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth register image is a strong source for the registered birth row, but this task is reviewing a conflict rather than issuing a final transcription correction. |
| conversion_confidence_score | 0.35 | The assigned chunk and image align, but the assigned converted Markdown materially contradicts the row and remains unresolved. |
| evidence_quantity_score | 0.62 | One source image plus the chunk, converted file, conflict draft, and source packet are enough to identify the conflict and likely row direction, not enough for canonical promotion while conversion disagreement persists. |
| agreement_score | 0.48 | Chunk, source packet, and visible image agree on Pulgar/Arriagada; the converted Markdown disagrees on every major family field. |
| identity_confidence_score | 0.72 | Confidence is moderately high that the visible entry 172 row concerns the Pulgar/Arriagada child, but identity claims remain held because the conversion layer is internally inconsistent. |
| claim_probability | 0.74 | The Pulgar/Arriagada row is the more probable controlling row based on chunk, packet, and image review; the score is held below promotion level due to unresolved conversion QA and father suffix uncertainty. |
| relevance_level | 1.00 | The review directly concerns the assigned staged identity-analysis draft for entry 172. |
| relevance_confidence | 1.00 | All consulted files are directly referenced by the staged draft and source packet. |
| canonical_readiness | 0.10 | Hold for targeted conversion QA; do not promote to canonical claims, relationships, or person pages from this task. |

## Claim And Identity Risk

- Literal support for the Pulgar/Arriagada entry is stronger than support for the Burgos/de la Cruz entry in the reviewed context, but the conflict must be resolved by conversion QA rather than by this proof-review note.
- The staged draft's conclusion that the two rows are not same-person or same-family variants is well supported. The child names, parent names, dates, places, and informant context are materially different.
- Parent identity linkage remains risky. `Juana Arriagada de Pulgar` should not be merged with similarly named Juana/Amagada candidates, and `Jose del Carmen Pulgar S.` should not be normalized to an existing Jose page until the father field and identity context are separately reviewed.
- No Dario-line identity bridge is supported. Shared Pulgar/Arriagada surname elements alone do not establish a relationship to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario/Darío Pulgar Arriagada.

## Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, assigned converted Markdown, assigned chunk, and source packet. The QA result should state which row controls entry 172 and explicitly certify the father field.

After QA, rerun proof review only on the certified row-level claims. Until then, keep this staged identity analysis and all dependent birth, identity, parent, relationship, and Pulgar/Dario comparison claims at `hold`.
