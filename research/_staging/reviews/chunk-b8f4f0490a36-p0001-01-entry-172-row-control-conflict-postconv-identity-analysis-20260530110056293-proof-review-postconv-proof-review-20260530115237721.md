---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530115237721
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-identity-analysis-20260530110056293.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-identity-analysis-20260530110056293.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-evidence-extraction-20260530102722394.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530102722394.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source_image_checked: "absent: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
page_image_checked: "absent: raw/codex-conversion-jobs/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172/page-images/page-0001.png"
crop_assets_checked:
  - "research/_staging/conversion-review-assets/chunk-b8f4f0490a36-entry-172-parent-fields-postconv-evidence-extraction-20260529000036877.png"
  - "research/_staging/conversion-review-assets/chunk-b8f4f0490a36-entry-172-parent-fields-bottom-postconv-evidence-extraction-20260529000036877.png"
canonical_readiness: not_ready
---

# Proof Review: Entry 172 Row-Control Conflict

This review covers only the staged draft `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-identity-analysis-20260530110056293.md`.

## Blockers First

1. Row control is unresolved. The assigned chunk transcribes entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`; the current converted Markdown transcribes entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
2. The full source image and conversion-job page image are absent in this checkout. I could not visually certify which physical row controls entry `172`.
3. The available crop assets show parent-field portions consistent with the Pulgar/Arriagada row, but they do not show enough full-page or row-number context to resolve the conflict.
4. The father suffix after `Jose del Carmen Pulgar` remains uncertified. Do not promote or expand the suffix beyond the literal uncertain staged reading until full-image QA confirms it.
5. No reviewed material names Dario, Arturo, Smith, Dario Jose, or Darío/Dario Pulgar Arriagada. The staged draft correctly blocks any same-person merge or family bridge from this entry to Dario-line candidates.
6. No canonical person, relationship, birth event, parent-child link, or wiki page should be promoted or strengthened from this packet while row control remains unresolved.

## Evidence Strengths

- The staged identity analysis accurately reports the direct conflict between the assigned chunk and the converted Markdown for the same entry number.
- The assigned chunk and source packet are internally coherent for a Pulgar/Arriagada birth row: child `Jose del Carmen Segundo Pulgar Arriagada`, registration date 7 April 1888, birth date 8 March 1888, birth place `Calle de Valdivia`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`
- The current converted Markdown is internally coherent for a different Burgos/de la Cruz row: child `Jose Miguel`, birth date 6 April 1888, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and informant `Oswaldo Burgos`.
- The checked crop assets provide partial visual support for Pulgar/Arriagada parent-field text, including `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`, but only as partial-field support.
- Civil birth registration is a strong source type if row alignment and transcription are certified.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 7/10 for the underlying civil registration source type; 4/10 for current usable review context because the full image is absent |
| conversion_confidence_score | 4/10 |
| evidence_quantity_score | 3/10 |
| agreement_score | 2/10 for entry-172 identity facts across chunk and converted Markdown; 7/10 for the narrow fact that a Pulgar/Arriagada parent-field crop exists |
| identity_confidence_score | 3/10 for attaching the Pulgar/Arriagada row to entry `172`; 1/10 or lower for any Dario-line same-person claim |
| claim_probability | 0.60 that the assigned Pulgar/Arriagada row is a real row in the source; 0.45 that it controls entry `172` without full-page QA; 0.03 or lower for any Dario identity bridge |
| relevance_level | high for Pulgar/Arriagada family research if certified; low for Dario identity proof at this stage |
| relevance_confidence | 0.80 for Pulgar/Arriagada relevance; 0.20 for Dario relevance |
| canonical_readiness | not_ready |

## Review Finding

The staged draft is supported as a conflict and hold analysis. It should not be revised into a promoted claim because the materials currently available do not resolve the row-control disagreement between the assigned chunk and the converted Markdown.

The safest proof judgment is `hold_for_conversion_qa`: the Pulgar/Arriagada reading has partial support from the chunk, source packet, and crop assets, but the controlling entry number cannot be certified without the full source/page image. The Burgos/de la Cruz reading remains a direct contradictory conversion reading, not a minor spelling or name-variant issue.

## Next Action

Keep the staged draft on hold for targeted conversion QA. Restore or locate the full source image or conversion-job page image, then verify the physical row for entry `172` against the chunk and converted Markdown. Only after row control is certified should downstream review consider the child birth facts, parent names, parent-child relationships, or any broader identity comparison.
