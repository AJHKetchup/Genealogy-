---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530135345959
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124059453.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124059453.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-evidence-extraction-20260530115033211.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-source-image-missing-postconv-evidence-extraction-20260530115033211.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-source-image-missing-conflict-qa-postconv-evidence-extraction-20260530115033211.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Derivative Transcript Conflict

This review covers the exact staged draft `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124059453.md`.

## Blockers First

1. Source-image control is missing. The referenced original image `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png` is not present in this workspace, and the referenced conversion-job page image `raw/codex-conversion-jobs/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172/page-images/page-0001.png` is also not present.
2. The assigned chunk and current converted Markdown conflict materially for entry `172`. The chunk/source-packet layer gives `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`; the converted-file layer gives `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
3. The conflict is not a name variant or minor reading issue. It changes child identity, parent set, birth date, birth place, and informant.
4. No Dario identity attachment is supported by the reviewed text. The reviewed files do not literally name `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, or `Dario Pulgar A.`
5. Parent-child relationships involving `Jose del Carmen Pulgar S.` or `Juana Arriagada de Pulgar` must remain on hold until a later image-controlled QA certifies the physical row.

## Evidence Strengths

- The assigned chunk and staged source packet agree internally on a Pulgar/Arriagada reading for entry `172`: registration date `Siete de Abril de mil ochocientos ochenta i ocho`, child `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`, birth date `Ocho de Marzo de mil ochocientos ochenta i ocho`, birth place `Calle de Valdivia`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`
- The current converted Markdown consistently gives a different entry `172`: child `José Miguel`, sex `Varon`, birth date `El seis de Abril de mil ochocientos ochenta i ocho`, place `En esta`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and informant `Oswaldo Burgos`.
- The conversion-review note correctly identifies this as unresolved derivative conflict with source image missing, and it recommends `hold_for_conversion_qa`.
- The staged identity analysis is appropriately conservative: it does not promote a canonical claim, merge, Dario-line attachment, or relationship.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 for the underlying civil birth register type if image-certified; 4/10 for this review because only conflicting derivative text is available |
| conversion_confidence_score | 3/10 |
| evidence_quantity_score | 4/10 |
| agreement_score | 3/10 overall; 8/10 within the chunk/source-packet layer; 2/10 between chunk and converted file |
| identity_confidence_score | 5.5/10 for a staged Pulgar/Arriagada candidate existing in the chunk layer; 2.5/10 for the converted Burgos/de la Cruz reading controlling this target; 0.2/10 for any Dario attachment |
| claim_probability | 0.64 that the assigned chunk's Pulgar/Arriagada row is the intended target; 0.24 that the current converted Markdown's Burgos/de la Cruz row controls entry `172`; 0.88 that the workspace contains a row/page-control or derivative-substitution conflict; 0.03 or lower for a Dario same-person claim |
| relevance_level | high if the Pulgar/Arriagada row is certified; low if the Burgos/de la Cruz row is certified |
| relevance_confidence | 0.75, conditional on unresolved row control |
| canonical_readiness | hold_for_conversion_qa; not ready for canonical claim, relationship, merge, rename, or wiki update |

## Review Finding

The staged draft is supported as a hold, not as promotion-ready proof. The reviewed derivative materials establish a serious conflict for entry `172`, but they do not establish which physical row controls the source target because the referenced source image and conversion-job page image are unavailable.

The Pulgar/Arriagada reading may be preserved only as derivative chunk-supported, unresolved evidence. It should not be used to promote a birth fact, parent-child relationship, same-person conclusion, Dario-line connection, or canonical wiki update until image-controlled conversion QA certifies the row and then proof review accepts the certified literal reading.

## Next Action

Keep this item on `hold_for_conversion_qa`. A conversion-QA worker should restore or locate the original/page image and compare physical entry `172` against both derivative readings. After that, run a new proof review on the certified child name, birth facts, father field, mother field, informant field, and any proposed relationship or identity claim.
