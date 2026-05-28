---
type: proof_review
status: complete
role: claim_reviewer
worker: "postconv-proof-review-20260528132702264"
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525224813411.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525224813411.md"
output_area: "research/_staging/reviews/"
source_quality_score: 0.86
conversion_confidence_score: 0.46
evidence_quantity_score: 0.68
agreement_score: 0.44
identity_confidence_score: 0.58
claim_probability: 0.66
relevance_level: "high"
relevance_confidence: 0.94
canonical_readiness: "hold_for_conversion_qa"
promotion_recommendation: "hold"
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

This review covers staged draft `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525224813411.md`.

## Blockers First

1. The referenced converted Markdown and the assigned chunk do not identify the same entry 172 row. The converted file reads entry 172 as `José Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`; the chunk/source packet read entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`.
2. This is not a normal name-variant question. The child name, parent names, birth date, birthplace, and informant differ across the two derivative artifacts.
3. The page image visibly supports the Pulgar/Arriagada row at entry 172, but the repository still contains a conflicting converted file. Canonical promotion should wait for a targeted conversion-QA correction or certification that resolves that artifact conflict.
4. The father field should not be normalized beyond the visible support. The staged draft's caution around `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` is warranted.
5. No Dario, Arturo, Smith, Dario Jose, Dario J., or Dario Pulgar Arriagada identity bridge is supported by this entry alone.

## Evidence Checked

- Staged identity-analysis draft named above.
- Conflict draft `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525215121005.md`.
- Source packet `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525215121005.md`.
- Assigned chunk `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Converted Markdown `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Page image `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Scored Judgment

| Dimension | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth register image is a strong contemporary source for names, dates, parent declarations, and informant details. |
| conversion_confidence_score | 0.46 | The page image and chunk favor the Pulgar/Arriagada row, but the converted Markdown is internally coherent and contradictory. |
| evidence_quantity_score | 0.68 | There is one primary image plus multiple derivative artifacts, but only one event row is at issue and the artifacts conflict. |
| agreement_score | 0.44 | Source packet, chunk, and image agree broadly; converted Markdown disagrees on the entire row. |
| identity_confidence_score | 0.58 | The Pulgar/Arriagada row is likely the relevant row, but canonical person attachment remains unsafe until conversion QA resolves the row-control conflict. |
| claim_probability | 0.66 | It is more likely than not that entry 172 is the Pulgar/Arriagada birth row, based on the image and chunk, but not yet promotion-ready. |
| relevance_level | high | The row directly controls Pulgar/Arriagada child and parent claims. |
| relevance_confidence | 0.94 | If certified, the row is directly relevant; if not certified, the conflict is directly relevant as a blocker. |
| canonical_readiness | hold_for_conversion_qa | Do not promote until the converted-file/chunk/source-image conflict is resolved. |

## Evidence Strengths

- The assigned chunk gives a complete row-level transcription for entry 172 with child, sex, birth date/time, birthplace, father, mother, informant, and official context.
- The source packet correctly identifies the conflict as a row-control or conversion-control problem rather than an identity variant.
- Visual inspection of the page image supports the presence of the Pulgar/Arriagada row at entry 172 on page 58, including the child name cluster, parents, and informant cluster.
- The staged draft appropriately avoids merging the Pulgar/Arriagada row into Dario-line identities or existing Jose/Juana parent candidates.

## Claim Review

| Claim or hypothesis | Review result | Probability | Canonical readiness |
| --- | --- | ---: | --- |
| Entry 172 is the Pulgar/Arriagada row rather than the Burgos/de la Cruz row. | Likely, based on the page image and assigned chunk, but blocked by the conflicting converted Markdown. | 0.66 | hold_for_conversion_qa |
| Child is `Jose del Carmen Segundo Pulgar Arriagada`. | Supported by the chunk and visually plausible from the image; hold until conversion QA certifies row control. | 0.63 | hold_for_conversion_qa |
| Mother is `Juana Arriagada de Pulgar`. | Supported by chunk/source-packet reading and visible row structure; do not merge with other Juana candidates here. | 0.62 | hold_for_conversion_qa |
| Father is `Jose del Carmen Pulgar S.`. | Base name is supported, but suffix/form requires targeted reread. | 0.55 | hold_for_father_field_reread |
| This entry supports Dario-line identity linkage. | Not supported by this source alone. | 0.04 | not_ready |

## Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the page image, assigned chunk, source packet, and current converted Markdown. The QA note should explicitly certify the controlling entry 172 row and separately record the father field only to the visible extent. After that, rerun proof review for any proposed child, parent, parent-child, or Dario-line bridge claim before canonical promotion.
