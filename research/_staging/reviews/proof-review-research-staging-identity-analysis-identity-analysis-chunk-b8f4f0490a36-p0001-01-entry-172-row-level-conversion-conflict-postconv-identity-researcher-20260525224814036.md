---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260528165331821
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525224814036.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525224814036.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525220612902.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
page_reference: "page 1; register page 58; entry 172"
source_quality_score: 0.88
conversion_confidence_score: 0.42
evidence_quantity_score: 0.55
agreement_score: 0.48
identity_confidence_score: 0.58
claim_probability: 0.60
relevance_level: high
relevance_confidence: 0.92
canonical_readiness: not_ready
promotion_recommendation: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

This review covers the staged draft `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525224814036.md`.

## Blockers First

- Conversion-control blocker: the assigned chunk/source packet and the current converted Markdown identify materially different entry-172 families. The chunk/source packet read a Pulgar/Arriagada child; the converted Markdown reads a Burgos/de la Cruz child.
- Canonical-readiness blocker: no identity, parent-child, duplicate-person, or Dario-line bridge claim should be promoted from this draft until the row-control conflict is resolved by targeted conversion QA.
- Father-field blocker: even under the Pulgar/Arriagada reading, the father should remain literal and uncertified pending QA of whether the visible source supports `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- Relationship-jump blocker: the draft correctly warns that this entry does not name Dario, Arturo, Smith, Dario Jose, Dario J., or Darío/Dario Pulgar Arriagada. Surname overlap is not enough for an identity bridge.

## Evidence Checked

- Staged identity-analysis draft named above.
- Source packet `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525220612902.md`.
- Assigned chunk `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Current converted Markdown `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Source page image `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Evidence Strengths

- The source is a civil birth register image, so source reliability is high for facts visibly present in the entry.
- The chunk and source packet agree on the Pulgar/Arriagada reading: child `Jose del Carmen Segundo Pulgar Arriagada`, registration date 7 April 1888, birth date 8 March 1888, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`
- A visual check of the cited source image supports that page 58 entry 172 is in the Pulgar/Arriagada area of the page, not the Burgos/de la Cruz reading in the current converted Markdown.
- The staged draft is appropriately cautious: it classifies the issue as a row-level conversion conflict and recommends hold rather than promotion.

## Scored Judgment

| Dimension | Score / value | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.88 | Primary register image is strong evidence, but the review did not perform a full new diplomatic transcription. |
| conversion_confidence_score | 0.42 | The derivatives materially disagree, so conversion confidence remains low despite visual support for the chunk. |
| evidence_quantity_score | 0.55 | One source image plus conflicting derivatives; enough to classify the conflict, not enough to promote final claims. |
| agreement_score | 0.48 | Chunk and packet agree with each other; converted Markdown disagrees on central identity facts. |
| identity_confidence_score | 0.58 | Moderate confidence that the staged draft identifies the correct conflict; not high enough for canonical attachment. |
| claim_probability | 0.60 | The Pulgar/Arriagada row is probable from the chunk and visual check, but the unresolved converted-file conflict blocks promotion. |
| relevance_level | high | Directly relevant to Pulgar/Arriagada evidence if row control is certified. |
| relevance_confidence | 0.92 | The entry names Pulgar and Arriagada in the chunk/source-packet reading. |
| canonical_readiness | not_ready | Hold for conversion QA; no canonical identity or relationship update. |

## Review Decision

Hold the staged draft as `hold_for_conversion_qa`. The staged analysis is well supported as a conflict note, but it is not proof-ready as a promoted identity or relationship claim because the converted Markdown contradicts the assigned chunk/source packet on the child, parents, birth date, birthplace, and informant.

## Next Action

Run targeted conversion QA for source page 1 / register page 58 / entry 172. The QA note should decide which row controls the assigned source and should certify only the visible father-field reading. After that, a narrow proof review can score the child identity, birth facts, father claim, mother claim, informant claim, and parent-child relationships from the certified row.
