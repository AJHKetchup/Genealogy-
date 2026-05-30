---
type: proof_review
status: complete
role: claim_reviewer
worker: "postconv-proof-review-20260530135126736"
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124454140.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124454140.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-source-image-missing-postconv-evidence-extraction-20260530115033211.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-source-image-missing-conflict-qa-postconv-evidence-extraction-20260530115033211.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
page_reference: "page 1; register page 58; entry 172"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Derivative Transcript Conflict

This review covers the exact staged draft `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124454140.md`.

## Blockers First

- The source image `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png` is not present in this workspace.
- The conversion-job page image `raw/codex-conversion-jobs/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172/page-images/page-0001.png` is not present in this workspace.
- Row control is unresolved. The assigned chunk and source packet read entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`; the current converted Markdown reads entry `172` as `José Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
- The conflict is material, not a spelling or name-normalization issue. The two derivative layers differ on child, parents, birth date, birth time, birth place, and informant.
- No canonical person page, relationship, merge, Dario-line attachment, or parent-child claim should be promoted from this staged draft until image-controlled conversion QA resolves the physical row.

## Evidence Strengths

- The staged draft accurately reports the core conflict between the assigned chunk/source packet and the current converted Markdown.
- The source packet and assigned chunk agree internally on a Pulgar/Arriagada reading for entry `172`: registration on 7 April 1888; male child `Jose del Carmen Segundo Pulgar Arriagada`; birth on 8 March 1888 about 3 p.m. at Calle de Valdivia; father `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`.
- The converted Markdown independently gives a coherent but incompatible entry `172`: `José Miguel`; born 6 April 1888 about 10 p.m. in `En esta`; father/informant `Oswaldo Burgos`; mother `Concepcion de la Cruz`.
- The staged identity analysis appropriately treats Dario-related attachment as unsupported by this entry. No reviewed verification file literally names `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, or `Dario Pulgar A.`

## Scores

| Field | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.55 | A civil birth register would be high-quality direct evidence if image-controlled, but this task has only conflicting derivative text and missing images. |
| conversion_confidence_score | 0.30 | The assigned chunk and converted Markdown disagree materially, and neither can be checked against the source image here. |
| evidence_quantity_score | 0.45 | There are multiple derivative layers, but only one target source event and no available image or corroborating accepted record in this review scope. |
| agreement_score | 0.20 | The chunk and source packet agree with each other, but they directly conflict with the current converted Markdown on the same entry number. |
| identity_confidence_score | 0.50 | The Pulgar/Arriagada candidate is internally coherent in the chunk, but identity confidence is capped by unresolved row control. Dario identity confidence from this evidence is near zero. |
| claim_probability | 0.60 | It is plausible that the Pulgar/Arriagada row is the intended target because the assigned chunk/source packet match, but the converted Markdown conflict prevents a stronger judgment. |
| relevance_level | high_if_pulgar_row_controls; low_if_burgos_row_controls | The evidence is family-relevant only if entry `172` is certified as the Pulgar/Arriagada row. |
| relevance_confidence | 0.55 | Relevance is clear under one hypothesis and absent under the competing hypothesis, so it depends on unresolved conversion QA. |
| canonical_readiness | hold_for_conversion_qa | Not ready for canonical promotion, relationship attachment, merge, rename, or wiki update. |

## Claim Judgment

The staged draft is supportable as a conflict analysis and should remain staged. It should not be converted into canonical claims. The safest proof judgment is `hold_for_conversion_qa` because the visible verification context contains two incompatible derivative transcriptions and no available image for row-control certification.

Specific probabilities:

| Claim | Probability | Judgment |
| --- | ---: | --- |
| Entry `172` is the Pulgar/Arriagada row described by the assigned chunk. | 0.60 | Plausible, not certified. |
| Entry `172` is the Burgos/de la Cruz row described by the converted Markdown. | 0.25 | Plausible competing derivative reading, not certified. |
| The two derivative readings describe different physical rows/pages under one target. | 0.85 | Likely, based on broad field-level mismatch. |
| This entry supports attaching any Dario Pulgar/Pulgar-Smith identity. | 0.02 | Unsupported; no literal Dario evidence appears. |
| This entry supports canonical parent-child relationships for Jose/Juana and the named child now. | 0.30 | Possible only after row-control QA. |

## Next Action

Keep the staged identity analysis on hold. A conversion-QA worker needs to restore or locate the source/page image and perform an image-controlled reread of physical entry `172`, then decide whether the controlling row is Pulgar/Arriagada or Burgos/de la Cruz. Only after that should proof review consider any child identity, parent names, parent-child relationships, or Dario-line comparison.
