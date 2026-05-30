---
type: proof_review_note
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530073606664
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530064641974.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530064641974.md"
reviewed_context:
  - "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260530044358861.md"
  - "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530044358861.md"
  - "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260530044358861.md"
  - "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
  - "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
canonical_readiness: blocked
promotion_recommendation: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Control Conflict

## Blockers First

- Exact staged draft reviewed: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530064641974.md`.
- The original source PNG named in the source packet and chunk is not present in this checkout under either checked path:
  - `raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png`
  - `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`
- The assigned chunk and current converted Markdown materially disagree on entry `172`; this is a row-control conflict, not a normal identity variant.
- The converted Markdown has entry `172` as `José Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888.
- The assigned chunk has entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`, born 8 March 1888.
- The reviewed crop assets support the lower Pulgar/Arriagada parent and informant area, but they do not provide complete fresh original-image certification for the whole row.
- The trailing mark after `Jose del Carmen Pulgar` remains unresolved. Do not promote it as more than the literal or bounded reading `Jose del Carmen Pulgar S.` / `Jose del Carmen Pulgar [?]`.

## Evidence Strengths

- The staged draft accurately reports the central conflict between the assigned chunk and the current converted Markdown.
- The assigned chunk is internally coherent and gives a full table-row reading for entry `172` on page 58.
- The source packet and conversion review consistently preserve the same hold recommendation and warn against canonical promotion.
- The reviewed staged crop `research/_staging/conversion-review-assets/chunk-b8f4f0490a36-entry-172-parent-fields-postconv-evidence-extraction-20260529000036877.png` visibly supports Pulgar/Arriagada lower-row parent and informant content, including `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Ernesto Herrera L.`.
- The staged draft correctly rejects same-person, duplicate-person, and Dario-line bridge hypotheses from this record alone.

## Scored Judgment

| Metric | Score | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.64 | Civil birth register would be high-quality primary evidence, but this review had no original source PNG; available support is derivative conversion text plus staged crop assets. |
| conversion_confidence_score | 0.52 | Pulgar/Arriagada chunk and crop evidence are coherent, but the controlling converted Markdown conflicts at the same entry number. |
| evidence_quantity_score | 0.58 | One assigned chunk, one source packet, one conversion review, and staged crop support; no full original-image confirmation. |
| agreement_score | 0.46 | Staged packet, chunk, and crop agree on Pulgar/Arriagada, while the converted Markdown gives a completely different Burgos/de la Cruz row. |
| identity_confidence_score | 0.76 | The Pulgar/Arriagada identity reading is probable within staged materials; broader identity attachment is not supported. |
| claim_probability | 0.70 | Probable that the staged Pulgar/Arriagada row is the intended row-control correction, but not promotion-ready without original-image QA. |
| relevance_level | 1.00 | Directly relevant to entry `172` and the staged row-level conflict. |
| relevance_confidence | 0.98 | The reviewed files all concern the exact staged draft and chunk id. |
| canonical_readiness | 0.12 | Blocked; hold until row-control QA resolves the conversion conflict against the original image. |

## Claim-Level Findings

- Pulgar/Arriagada controls entry `172`: revise/hold. The claim is probable in staged evidence, but original-image row-control QA is required before canonical promotion.
- Burgos/de la Cruz controls entry `172`: hold as competing derivative conversion reading. It is not supported by the assigned chunk or staged crop review, but it remains present in the current converted Markdown.
- Pulgar/Arriagada and Burgos/de la Cruz are the same person or family: reject for promotion. The overlap is only the disputed row number.
- Direct bridge to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario Pulgar-Arriagada`: reject for promotion from this evidence. The entry does not name those persons or supply a descendant bridge.
- Same-person merge between `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar`: hold/reject from this record alone. The staged draft correctly requires separate identity-bridge proof.

## Next Action

Keep the staged draft at `hold_for_conversion_qa` with `canonical_readiness: blocked`. Route entry `172`, register page 58, to targeted original-image row-control QA. The next reviewer should certify the physical row against the original PNG and explicitly resolve whether the father field should remain `Jose del Carmen Pulgar S.`, `Jose del Carmen Pulgar [?]`, or a narrower base-name-only reading.
