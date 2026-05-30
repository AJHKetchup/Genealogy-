---
type: proof_review
status: complete
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-identity-analysis-20260530110953508.md"
worker: "postconv-proof-review-20260530120921996"
role: claim_reviewer
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-identity-analysis-20260530110953508.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530102722394.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
canonical_readiness: "not_ready"
review_decision: "hold_for_conversion_qa"
---

# Proof Review: Entry 172 Row-Control Conflict

This review covers only the staged identity-analysis draft `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-identity-analysis-20260530110953508.md`.

## Blockers First

- Row-control blocker: the assigned chunk transcribes entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`, while the referenced converted Markdown transcribes entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
- Source-image blocker: local verification found the referenced full PNG absent at `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`. The conversion job directory contains `page-markdown`, `work-orders`, `manifest.json`, and `README.md`, but no available page image for visual row-control verification.
- Relationship blocker: the conflicting derivative readings disagree on child, parents, birth date, birth place, and informant. No parent-child relationship can be promoted from this review.
- Identity-risk blocker: the draft correctly treats Dario/Pulgar comparisons as anti-conflation checks. This record does not literally name `Dario`, `Arturo`, `Smith`, `Dario Jose Pulgar-Arriagada`, or `Dario Pulgar A.`.
- Father-field blocker: the chunk reading `Jose del Carmen Pulgar S.` cannot be independently certified from the visible original source in this pass. Keep the suffix uncertain until image QA can verify it.

## Evidence Strengths

- The staged draft accurately reports the material conflict between the chunk/source-packet reading and the converted Markdown reading.
- The assigned chunk and source packet are internally consistent for the Pulgar/Arriagada reading: entry `172`, registration date 7 April 1888, child `Jose del Carmen Segundo Pulgar Arriagada`, birth 8 March 1888 at about three in the afternoon at `Calle de Valdivia`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The converted Markdown is internally consistent for the Burgos/de la Cruz reading: entry `172`, child `Jose Miguel`, birth 6 April 1888 at ten at night at `En esta`, father/informant `Oswaldo Burgos`, and mother `Concepcion de la Cruz`.
- The source type, if visually certified, would be high-value direct civil birth-registration evidence for birth and parentage. The current problem is not source class but derivative agreement and missing image access.

## Scores

| Dimension | Score / Level | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil birth registration is a strong source class for birth identity and parentage, but the original image was unavailable for this review. |
| conversion_confidence_score | 0.35 | The assigned chunk and converted Markdown materially disagree on identity-controlling fields for the same entry number. |
| evidence_quantity_score | 0.45 | Two derivative readings and one source packet were available, but no original image or certified crop with row context was available. |
| agreement_score | 0.20 | The two derivative layers agree on entry number and registration date only; they conflict on child, parents, birth event, place, and informant. |
| identity_confidence_score | 0.30 | Identity confidence is low because row control is unresolved. Confidence that this is not a Dario identity from this draft is high. |
| claim_probability | 0.58 | Probability that the staged identity-analysis conclusion should remain on hold is high; probability of any specific parent-child claim being promotion-ready is low. |
| relevance_level | conditional_high | High only if image QA certifies the Pulgar/Arriagada row; otherwise low/no Pulgar-line relevance. |
| relevance_confidence | 0.62 | The chunk/source packet are relevant to Pulgar/Arriagada, but relevance depends on unresolved row control. |
| canonical_readiness | not_ready | No canonical person, relationship, birth fact, merge, or Dario-line bridge should be promoted. |

## Claim Probability Details

| Claim | Probability | Review judgment |
| --- | ---: | --- |
| Entry `172` is the Pulgar/Arriagada row in the assigned chunk | 0.62 | Plausible from chunk and source packet, but not certified without the original image. |
| Entry `172` is the Burgos/de la Cruz row in the converted Markdown | 0.25 | Plausible from the converted Markdown alone, but contradicted by the assigned chunk and source packet. |
| The conflict is a derivative row/page mismatch rather than a normal name variant | 0.86 | Strongly supported because every identity-controlling field differs. |
| `Jose del Carmen Pulgar` is the father in a promotion-ready parent-child claim | 0.28 | Possible only after row-control and suffix QA. |
| `Juana Arriagada de Pulgar` is the mother in a promotion-ready parent-child claim | 0.34 | Possible only after row-control QA. |
| This draft supports a Dario Pulgar / Pulgar-Smith identity bridge | 0.02 | No literal Dario/Arturo/Smith evidence appears in the reviewed material. |

## Canonical Readiness

Canonical readiness is `not_ready`.

Do not promote this staged draft to `research/claims`, `research/relationships`, `wiki/people`, `wiki/families`, or any other canonical path. Do not attach entry `172` to any Dario identity. Do not merge Jose/Juana candidates from this review.

## Next Action

Keep the staged identity-analysis draft on `hold_for_conversion_qa`.

The next action is targeted conversion QA using the original full-page image, the assigned chunk, and the converted Markdown. QA must certify which physical row controls entry `172` and must bound the father-field reading as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, run a narrow proof review only on the certified child name, birth event, father, mother, informant, and parent-child claims.
