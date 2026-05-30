---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530075027601
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530064641974.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530064641974.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530044358861.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260530044358861.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source_image_present: false
canonical_readiness: blocked
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

- The exact staged draft reviewed is `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260530064641974.md`.
- The original source image referenced by the packet and chunk was not available at either checked `raw/sources/` path variant, so this review cannot certify the full physical row from the original page image.
- The assigned chunk and current converted Markdown materially disagree for entry `172`. The chunk gives a Pulgar/Arriagada birth entry; the converted file gives a Burgos/de la Cruz birth entry.
- The staged crop assets available for review visibly support the lower parent/informant fields for the Pulgar/Arriagada row, but they do not independently certify the full row, the child-name field, or the row-control boundary.
- The father field suffix after `Jose del Carmen Pulgar` remains unresolved. The literal staged chunk has `Jose del Carmen Pulgar S.`, while the visible crop supports the base name but not a promotion-ready suffix decision.
- No canonical claim, relationship, same-person merge, Dario-line bridge, or Jose/Juana cluster merge should be promoted from this staged draft.

## Evidence Strengths

- The staged draft accurately reports the derivative conflict between the assigned chunk and the converted Markdown.
- The assigned chunk is internally coherent for entry `172`: child `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, birth 8 March 1888 at 3 p.m., place Calle de Valdivia, and informant `Ernesto Herrera L.`.
- The source packet repeats the same Pulgar/Arriagada row summary and explicitly flags the conversion conflict and source-image absence.
- The conversion review note correctly states that the current converted Markdown records entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888.
- The two staged crop images inspected in this review visibly support `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, `Ernesto Herrera L.`, `Presente al nacimiento`, `Veintiseis anos`, `Empleado`, and `Calle de Valdivia` for the Pulgar/Arriagada parent/informant area.

## Scored Judgment

| Metric | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.62 | Civil birth register would be high-quality primary evidence, but the original source image is unavailable in this pass; review relies on derivative transcription plus staged crops. |
| conversion_confidence_score | 0.50 | Pulgar/Arriagada chunk and crop evidence agree in part, but the canonical converted file materially conflicts. |
| evidence_quantity_score | 0.58 | Multiple local derivatives and two crop assets support part of the Pulgar/Arriagada reading; full-row image support is missing. |
| agreement_score | 0.42 | Chunk, packet, QA note, and crop assets align for parent/informant fields, while the converted file gives a different family for the same entry number. |
| identity_confidence_score | 0.70 | Probable staged identity for the Pulgar/Arriagada row if row control is confirmed; reduced by unresolved conversion conflict and absent original image. |
| claim_probability | 0.68 | The narrow claim that the assigned chunk represents a Pulgar/Arriagada entry is probable but not promotion-ready. |
| relevance_level | 1.00 | Directly relevant to the staged row-control conflict for entry `172`. |
| relevance_confidence | 0.96 | All reviewed materials concern the same chunk, entry number, and conflict. |
| canonical_readiness | 0.10 | Blocked pending original-image row-control QA and proof acceptance. |

## Claim Review

- Pulgar/Arriagada controls entry `172`: hold. The staged chunk, source packet, QA note, and crop assets support this as the stronger staged hypothesis, especially for parent/informant fields. Probability: `0.68`; canonical_readiness: `blocked`.
- Burgos/de la Cruz controls entry `172`: hold as competing converted-file reading. The current converted Markdown explicitly supports this reading, but it is contradicted by the assigned chunk and staged crop-supported review set. Probability: `0.30`; canonical_readiness: `blocked`.
- Pulgar/Arriagada and Burgos/de la Cruz are the same person or name variants: reject for promotion. The names, parents, dates, places, and informant context are incompatible except for the disputed entry number. Probability: `0.02`; canonical_readiness: `not_ready`.
- Direct Dario Pulgar identity bridge: reject for this source. The reviewed entry does not name Dario, Arturo, Smith, or a later-life identity bridge. Probability: `0.00`; canonical_readiness: `not_ready`.
- Father/mother relationship for `Jose del Carmen Segundo Pulgar Arriagada` to `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`: hold. The crop and chunk support the parent fields, but the row-control conflict blocks canonical promotion. Probability: `0.66`; canonical_readiness: `blocked`.

## Identity And Relationship Risk

- Identity risk is high if the Pulgar/Arriagada row is merged with the Burgos/de la Cruz converted-file reading.
- Relationship risk is high if Burgos/de la Cruz parentage is attached to the Pulgar/Arriagada child or if Pulgar/Arriagada parentage is promoted before row-control QA.
- Broader Jose/Juana cluster merging is not supported by this staged draft alone.
- The father suffix after `Pulgar` must remain literal/uncertain until the original image or a better crop supports a specific reading.

## Next Action

Keep this staged draft at `hold_for_conversion_qa` / `canonical_readiness: blocked`. The next worker should obtain or restore the original source image for source SHA-256 `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2`, then perform targeted row-control QA for page 58, entry `172`, including the child-name field and the father suffix after `Jose del Carmen Pulgar`.
