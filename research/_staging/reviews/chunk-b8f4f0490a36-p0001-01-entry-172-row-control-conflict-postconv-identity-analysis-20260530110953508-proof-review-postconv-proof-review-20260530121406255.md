---
type: proof_review
status: complete
role: claim_reviewer
worker: "postconv-proof-review-20260530121406255"
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-identity-analysis-20260530110953508.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-identity-analysis-20260530110953508.md"
reviewed_source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530102722394.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
canonical_readiness: not_ready
claim_probability: 0.66
relevance_level: high_if_pulgar_row_certified
relevance_confidence: 0.86
source_quality_score: 0.78
conversion_confidence_score: 0.40
evidence_quantity_score: 0.46
agreement_score: 0.28
identity_confidence_score: 0.38
---

# Proof Review: Entry 172 Row-Control Conflict

This review covers the exact staged draft `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-identity-analysis-20260530110953508.md`.

## Blockers First

- Canonical readiness: `not_ready`. No claim, relationship, identity merge, or wiki update should be promoted from this draft.
- Row-control blocker: the assigned chunk and revised source packet identify entry `172` as the Pulgar/Arriagada row, while the current converted Markdown identifies entry `172` as the Burgos/de la Cruz row.
- Image-access blocker: the referenced original PNG path `raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png` is not present in this checkout. The conversion job directory contains manifest/page-markdown/work-order files but no available page image directory for independent visual certification.
- Relationship blocker: the two derivative readings name different children, parents, birth dates, birth places, and informants. Parent-child claims are therefore held.
- Father-field blocker: the assigned chunk reads `Jose del Carmen Pulgar S.`, but the source packet reasonably bounds this as `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar [?]` until the suffix can be checked against the visible source.
- Identity-risk blocker: this entry does not literally name Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario Pulgar Arriagada, or Dario Pulgar A. Any Dario connection would be an unsupported relationship jump from this draft.

## Evidence Strengths

- The assigned chunk is internally specific and gives a coherent civil birth-register row for entry `172`: `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 about three in the afternoon at `Calle de Valdivia`, with father transcribed as `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- The revised source packet accurately summarizes that assigned-chunk reading and explicitly warns that the current converted Markdown has a conflicting row for the same entry number.
- The current converted Markdown also gives a coherent but incompatible entry `172`: `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at `En esta`.
- The staged identity analysis correctly treats the conflict as row control, not spelling variation. The conflict affects identity, birth event, parentage, and relevance.

## Scored Judgment

| Dimension | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.78 | Civil birth registration is a strong source class, but the original image is unavailable for this review. |
| conversion_confidence_score | 0.40 | Derivative layers materially disagree on the entry-172 row. |
| evidence_quantity_score | 0.46 | There are multiple derivative texts, but only two disagreeing transcription layers and no usable full-image check. |
| agreement_score | 0.28 | The chunk/source-packet pair agrees internally, but the converted Markdown conflicts on all identity-controlling fields. |
| identity_confidence_score | 0.38 | Possible Pulgar/Arriagada identity cluster, but not safe to attach until row control is certified. |
| claim_probability | 0.66 | Probability that the Pulgar/Arriagada row controls the assigned review target, based on the chunk and revised packet, remains moderate rather than proven. |
| relevance_level | high_if_pulgar_row_certified | The draft is highly relevant only if the Pulgar/Arriagada row is confirmed. |
| relevance_confidence | 0.86 | If that row is certified, the Pulgar/Arriagada family relevance is direct. |
| canonical_readiness | not_ready | Hold for conversion QA; do not promote. |

## Claim Probability By Reading

| Reading | Probability | Rationale |
| --- | ---: | --- |
| Entry `172` is the Pulgar/Arriagada row | 0.66 | Supported by assigned chunk and revised source packet; not visually certified in this review. |
| Entry `172` is the Burgos/de la Cruz row | 0.22 | Supported by current converted Markdown; contradicted by the assigned chunk and revised packet. |
| This is a derivative row/page mismatch | 0.84 | Different child, parents, dates, places, and informants indicate row-control conflict rather than normal variant evidence. |
| The entry supports a Dario identity claim | 0.02 | No literal Dario/Arturo/Smith/Dario Jose reading appears in the checked draft or referenced transcription layers. |

## Next Action

Keep the staged draft on hold for conversion QA. The next reviewer should locate or restore the original full-page image, certify which physical row controls entry `172`, and then re-check the father field suffix. Only after that should narrow claims be reconsidered: child name, birth date/time/place, father name, mother name, informant, and parent-child relationships.
