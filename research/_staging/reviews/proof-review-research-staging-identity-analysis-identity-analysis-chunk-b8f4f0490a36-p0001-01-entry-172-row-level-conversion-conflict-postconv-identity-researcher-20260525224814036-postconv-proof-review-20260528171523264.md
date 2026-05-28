---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260528171523264
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525224814036.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525224814036.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525220612902.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525220612902.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
page_reference: "page 1; register page 58; entry 172"
source_quality_score: 0.90
conversion_confidence_score: 0.44
evidence_quantity_score: 0.58
agreement_score: 0.50
identity_confidence_score: 0.60
claim_probability: 0.62
relevance_level: high
relevance_confidence: 0.94
canonical_readiness: not_ready
promotion_recommendation: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

This review covers the staged draft `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525224814036.md`.

## Blockers First

- Conversion-control blocker: the current converted Markdown reads entry 172 as a Burgos/de la Cruz birth, while the assigned chunk and source packet read entry 172 as a Pulgar/Arriagada birth. These are mutually incompatible row readings, not name variants.
- Canonical-readiness blocker: no identity, birth-fact, parent-child, duplicate-person, or Pulgar-to-Dario bridge claim should be promoted while the converted file remains contradicted by the chunk/source packet and source image.
- Father-field blocker: the visible source supports a Pulgar father field, but the suffix/terminal mark after `Jose del Carmen Pulgar` remains a transcription-certification issue. Keep it literal as `Jose del Carmen Pulgar S.` or `Jose del Carmen Pulgar [?]` until conversion QA certifies the reading.
- Relationship-jump blocker: this entry does not name Dario, Arturo, Smith, Dario Jose, Dario J., or Dario/Dario Pulgar Arriagada. It cannot support an identity bridge to those candidates on surname overlap alone.

## Evidence Checked

- Staged identity-analysis draft named above.
- Staged conflict draft `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525220612902.md`.
- Source packet `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525220612902.md`.
- Assigned chunk `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Current converted Markdown `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Source page image `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Evidence Strengths

- The source is a civil birth register page image, a high-quality primary source for the facts visibly recorded in the row.
- Visual inspection of page 58, entry 172 supports the Pulgar/Arriagada row: child `Jose del Carmen Segundo Pulgar Arriagada`, male, registration date 7 April 1888, birth date 8 March 1888, birthplace `Calle de Valdivia`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The assigned chunk and source packet agree closely with the visible page image for the controlling row and with each other for the Pulgar/Arriagada reading.
- The staged draft correctly treats the Burgos/de la Cruz reading in the current converted Markdown as a row-level conversion conflict and recommends hold, not promotion.

## Scored Judgment

| Dimension | Score / value | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.90 | Primary civil register image is strong evidence for visible row facts. |
| conversion_confidence_score | 0.44 | The chunk/source packet and visual check support Pulgar/Arriagada, but the current converted Markdown is materially inconsistent. |
| evidence_quantity_score | 0.58 | One source image plus three derivatives is enough to score the conflict; not enough to promote final canonical claims while derivatives disagree. |
| agreement_score | 0.50 | Source image, chunk, and packet align on the Pulgar/Arriagada row; converted Markdown disagrees on core facts. |
| identity_confidence_score | 0.60 | Moderate confidence that the staged draft identifies the correct conflict and probable row; lower confidence for any canonical attachment. |
| claim_probability | 0.62 | Pulgar/Arriagada birth-registration claims are probable from the visible image and chunk, but not promotion-ready until conversion QA resolves the converted-file conflict. |
| relevance_level | high | If certified, the row is directly relevant to Pulgar/Arriagada research. |
| relevance_confidence | 0.94 | The visible/chunk reading names Pulgar and Arriagada directly. |
| canonical_readiness | not_ready | Hold for conversion QA; do not promote or merge. |

## Review Decision

Hold the staged draft as `hold_for_conversion_qa`. The draft is supported as a conflict analysis, and the visible source favors the Pulgar/Arriagada row over the Burgos/de la Cruz converted-file reading. The support is still not clean enough for canonical promotion because the official converted Markdown for the source remains materially wrong or misaligned.

## Next Action

Run targeted conversion QA for source page 1 / register page 58 / entry 172. The QA note should certify the controlling row against the image and correct/supersede the converted Markdown conflict. If the Pulgar/Arriagada row is certified, the next proof review should be narrow: child identity, birth facts, father field, mother field, informant field, and stated parent-child relationships only.
