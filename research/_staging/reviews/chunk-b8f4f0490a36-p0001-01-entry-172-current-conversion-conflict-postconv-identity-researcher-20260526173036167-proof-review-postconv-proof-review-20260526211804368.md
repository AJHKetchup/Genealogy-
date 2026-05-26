---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260526211804368
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526173036167.md"
reviewed_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526173036167.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526170352337.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
review_status: hold_for_conversion_qa
canonical_readiness: hold
created: 2026-05-26
---

# Proof Review: Entry 172 Current Conversion Conflict

## Blockers First

- The staged identity analysis is correctly blocked by a row-level conversion conflict. The assigned chunk and source packet identify entry `172` as the Pulgar/Arriagada birth registration, but the current converted Markdown identifies entry `172` as a Burgos/de la Cruz registration.
- The conflict changes the child, parents, birth date, birth place, informant, residences, and dependent relationships. This is not a spelling variant or same-person question.
- The father field is not exact-name ready. The source image and chunk support at least `Jose del Carmen Pulgar`; the trailing mark or suffix after `Pulgar` remains uncertain and must not be silently normalized.
- No canonical claim, relationship, person merge, or Dario-line attachment is ready from this draft until conversion QA reconciles the image, chunk, source packet, and current converted Markdown.

## Evidence Checked

- Reviewed staged draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526173036167.md`.
- Reviewed referenced source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526170352337.md`.
- Reviewed assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Reviewed current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Reviewed source image visually: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.
- No external research was performed.

## Literal Support

The source image shows register page 58, entry `172`, in the second row on the left page. The visible row supports the staged draft's Pulgar/Arriagada side: child `Jose del Carmen Segundo Pulgar Arriagada`, male; registration date 7 April 1888; birth on 8 March 1888 at about 3 p.m. at `Calle de Valdivia`; father at least `Jose del Carmen Pulgar`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`, present at the birth.

The assigned chunk agrees with that row and gives the father as `Jose del Carmen Pulgar S.`. The source packet preserves the safer reading as at least `Jose del Carmen Pulgar` with the trailing mark unresolved.

The current converted Markdown does not agree. It transcribes entry `172` as `Jose Miguel`, male, born 6 April 1888 at 10 p.m. in `En esta`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, informant `Oswaldo Burgos`. This converted-file row is materially incompatible with the image-reviewed Pulgar/Arriagada row.

## Evidence Strengths

- The source image, source packet, and assigned chunk all support the staged draft's main conclusion that the active issue is row control/conversion QA, not identity promotion.
- The Pulgar/Arriagada row is internally coherent for a birth registration and supports a probable child-parent event if, and only if, conversion QA confirms that row as controlling entry `172`.
- The staged draft appropriately protects against relationship jumps to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario/Dario Pulgar Arriagada, and passenger candidates; this record does not name those people or bridge to them.

## Scores

| metric | score | rationale |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil birth register image is a strong source type; image is readable enough for row-level verification, though father suffix remains unclear. |
| conversion_confidence_score | 0.35 | The chunk/source packet and current converted Markdown conflict on the controlling row for entry `172`. |
| evidence_quantity_score | 0.62 | One source image plus two derivative local readings support the Pulgar/Arriagada row, but there is no independent corroborating source in scope. |
| agreement_score | 0.58 | Image, chunk, and source packet agree broadly; current converted Markdown directly disagrees. |
| identity_confidence_score | 0.66 | Probable for the source-local Pulgar/Arriagada child identity if the image/chunk controls; capped by conversion conflict and father-field uncertainty. |
| claim_probability | 0.64 | The staged draft's hold-for-QA conclusion is well supported; promotion-level factual claims remain below threshold. |
| relevance_level | high | Pulgar and Arriagada names are directly present in the image-reviewed row and match the family-relevant terms. |
| relevance_confidence | 0.88 | Relevance to the Pulgar/Arriagada research cluster is high, even though canonical attachment is not ready. |
| canonical_readiness | 0.08 | Hold for targeted conversion QA; do not promote or merge from this draft. |

## Review Judgment

The staged draft is supported as a conflict-analysis and hold note. Its main claim, that entry `172` has a material current-conversion conflict requiring targeted QA, is well supported by the referenced materials and source image.

Dependent genealogical claims should remain held. If QA confirms the Pulgar/Arriagada row as controlling entry `172`, the child birth event and child-parent relationships can be proof-reviewed again with the father field preserved only to the visible extent. If QA confirms the Burgos/de la Cruz conversion as controlling, the Pulgar/Arriagada claims from this source path should be revised or withdrawn.

## Next Action

Perform targeted conversion QA for the source image, assigned chunk, source packet, and current converted Markdown. Certify which row controls entry `172`, then rerun proof review before any canonical claim, relationship, identity merge, or Dario-line attachment.
