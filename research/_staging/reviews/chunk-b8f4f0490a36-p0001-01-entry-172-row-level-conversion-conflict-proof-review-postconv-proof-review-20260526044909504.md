---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260526044909504
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526015109623.md"
reviewed_staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526015109623.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526001440948.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
review_recommendation: hold_for_conversion_qa
canonical_readiness: blocked
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

- Canonical readiness is blocked. The referenced source image and assigned chunk support entry 172 as a Pulgar/Arriagada birth row, while the referenced converted Markdown assigns entry 172 to a different Burgos/de la Cruz row.
- The converted Markdown cannot be used as reliable row control for this image without targeted conversion QA, because it conflicts with the visible source image for entry 172 and with the assigned chunk.
- The father field should not be normalized beyond visible support. The source image supports `Jose del Carmen Pulgar` as the father-field start, with a possible trailing mark or suffix; `Jose del Carmen Pulgar S.` remains plausible from the chunk but should stay uncertified pending QA.
- No relationship or identity bridge to any Dario/Pulgar-Smith/Pulgar-Arriagada person is proven by this staged draft. Such bridge claims must remain blocked.

## Scores

| Metric | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.90 | Civil birth register image is a strong primary-style source for the row once row control is settled. |
| conversion_confidence_score | 0.35 | The conversion set is internally inconsistent: chunk/source packet/image support Pulgar, while converted Markdown supports Burgos. |
| evidence_quantity_score | 0.65 | One source image plus chunk and packet review support the Pulgar row, but there is only one underlying record. |
| agreement_score | 0.55 | Source image, chunk, and source packet broadly agree; converted Markdown materially disagrees. |
| identity_confidence_score | 0.70 | The visible entry supports a child named Jose del Carmen Segundo Pulgar Arriagada, but the conversion conflict and father suffix uncertainty prevent higher confidence. |
| claim_probability | 0.72 | The most probable reading for this source image's entry 172 is the Pulgar/Arriagada row, not the Burgos/de la Cruz row. |
| relevance_level | high | Directly relevant to Pulgar/Arriagada identity and parent-child claims; Dario relevance is only a cautionary research context. |
| relevance_confidence | 0.90 | The names Pulgar and Arriagada are plainly present in the row and packet. |
| canonical_readiness | blocked | Hold until targeted conversion QA resolves row control and father-field certification. |

## Evidence Strengths

- The source image visibly places entry number 172 on page 58 in the Pulgar/Arriagada row.
- The assigned chunk transcribes entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 about 3 p.m. at Calle de Valdivia, with father `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- The source packet correctly identifies the row-control conflict and limits the father reading to `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` pending targeted QA.
- The current converted Markdown's Burgos/de la Cruz entry 172 is not supported by the visible row in the referenced image.

## Claim Review

- Pulgar row control for entry 172: revise/hold. The source image strongly favors the Pulgar/Arriagada row, but canonical use requires conversion QA because the converted Markdown disagrees.
- Child identity as `Jose del Carmen Segundo Pulgar Arriagada`: hold. Literal source support appears strong, but promotion should wait until row-control QA.
- Parent-child relationship to `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`: hold. The mother is well supported in the visible row and chunk; the father is supported at least as `Jose del Carmen Pulgar`, but the suffix remains unresolved.
- Burgos/de la Cruz row as the controlling entry 172 for this source image: revise/reject for this image pending QA. It is contradicted by the visible row and assigned chunk.
- Bridge to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario J. Pulgar Arriagada, or Dario/Dario Pulgar Arriagada: hold/reject as proof. The staged draft provides no direct identity, relationship, date, place, or parent bridge to those people.

## Next Action

Run targeted conversion QA against `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`, the converted Markdown, and the assigned chunk. Certify the controlling row for entry 172 and the father-field reading before any canonical promotion or relationship creation.
