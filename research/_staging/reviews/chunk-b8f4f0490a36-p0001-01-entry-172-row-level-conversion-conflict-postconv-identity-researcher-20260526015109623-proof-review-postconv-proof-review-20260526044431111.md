---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260526044431111
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526015109623.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526015109623.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526001440948.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
review_decision: hold
canonical_readiness: blocked
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

- Row-control blocker: the assigned chunk and source packet present entry 172 on register page 58 as `Jose del Carmen Segundo Pulgar Arriagada`, while the converted Markdown presents entry 172 as `José Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`. This materially blocks any canonical child identity, birth fact, parent-child relationship, parent merge, or Dario-line bridge.
- Father-field blocker: the source image visibly supports the father field beginning `Jose del Carmen Pulgar`, but the trailing mark or suffix is not clear enough in this review to certify as `S.`. Do not promote a normalized father identity or merge candidates until targeted conversion QA certifies the field.
- Identity-risk blocker: the draft correctly rejects any same-person or bridge claim from this entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, or `Dario/Darío Pulgar Arriagada`. The entry does not name Dario, Arturo, Smith, or a cross-generation bridge.
- Canonical-readiness blocker: because the controlling row conflicts between the converted Markdown and the assigned chunk/source packet, this review cannot approve promotion to canonical claims or relationships.

## Evidence Checked

- Reviewed staged draft: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526015109623.md`.
- Reviewed source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526001440948.md`.
- Reviewed assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Reviewed converted file excerpt for entry 172: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Visually checked source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Evidence Strengths

- The source image page layout shows page 58, row 172 as a Pulgar/Arriagada row. The visible child field is consistent with `Jose del Carmen Segundo Pulgar Arriagada`, and the mother field is consistent with `Juana Arriagada de Pulgar`.
- The source packet and assigned chunk agree with each other on the Pulgar/Arriagada row, including child name, sex, registration date, birth date/time/place, mother, informant, and residences.
- The converted Markdown clearly contains a different entry 172 with different child, parents, birth date/time/place, and informant. That makes the conflict real and material rather than a minor transcription variant.
- The staged draft is appropriately cautious about the father suffix and about Dario-line anti-conflation.

## Scored Judgment

| Metric | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth register image is a strong primary source for birth identity and parent statements, but this review is limited by image resolution and row-control conflict. |
| conversion_confidence_score | 0.34 | The assigned chunk and converted Markdown disagree on the controlling row for the same entry number. |
| evidence_quantity_score | 0.58 | One source image plus one chunk and one source packet support the Pulgar reading; the current converted file conflicts. |
| agreement_score | 0.46 | Source packet, chunk, and visual check agree generally; converted Markdown disagrees materially. |
| identity_confidence_score | 0.62 | Probable Pulgar/Arriagada row identity, but not canonically certifiable until row-control QA and father-field QA. |
| claim_probability | 0.68 | The claim that entry 172 should be treated as a Pulgar/Arriagada row for QA is more likely than the Burgos/de la Cruz reading, but still held. |
| relevance_level | high | Directly relevant to Pulgar/Arriagada family research and anti-conflation review. |
| relevance_confidence | 0.91 | The names `Pulgar` and `Arriagada` are plainly present in the reviewed chunk/source packet and visible source row. |
| canonical_readiness | blocked | Do not promote while row control and father suffix remain unresolved. |

## Claim Review

- `Entry 172 is the Pulgar/Arriagada birth row`: revise/hold. The source image, source packet, and chunk support this as the preferred QA hypothesis, but the converted Markdown conflict prevents canonical readiness.
- `Jose del Carmen Segundo Pulgar Arriagada was born 8 March 1888 at about 3 p.m. on Calle de Valdivia`: hold. Supported by chunk/source packet and broadly visible in the source image, but row-control QA is still required.
- `Jose del Carmen Segundo Pulgar Arriagada was child of Jose del Carmen Pulgar S. and Juana Arriagada de Pulgar`: hold. The mother and father-start readings are supported; the father suffix is not certified here, and the row-control conflict blocks relationship promotion.
- `Entry 172 is the Burgos/de la Cruz row`: unlikely/hold. Supported by the current converted Markdown only and contradicted by the assigned chunk, source packet, and visible row.
- `Entry 172 bridges to any Dario Pulgar identity`: reject for current proof. No direct name, date, place, parent, or relationship bridge in the reviewed entry supports this.

## Next Action

Hold the staged draft for targeted conversion QA. The next reviewer should compare the source image row numbered 172 against the converted Markdown and assigned chunk, then certify the controlling row and father field only to the visible extent: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that QA, rerun proof review before any canonical claim, relationship, parent merge, or Dario-line comparison is promoted.
