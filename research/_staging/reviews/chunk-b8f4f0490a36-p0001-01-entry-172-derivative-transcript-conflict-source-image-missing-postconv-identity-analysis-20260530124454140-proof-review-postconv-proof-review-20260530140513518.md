---
type: proof_review
status: complete
role: claim_reviewer
worker: "postconv-proof-review-20260530140513518"
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124454140.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124454140.md"
reviewed_files:
  - "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124454140.md"
  - "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-evidence-extraction-20260530115033211.md"
  - "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-source-image-missing-postconv-evidence-extraction-20260530115033211.md"
  - "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-source-image-missing-conflict-qa-postconv-evidence-extraction-20260530115033211.md"
  - "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
  - "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source_quality_score: 0.52
conversion_confidence_score: 0.36
evidence_quantity_score: 0.42
agreement_score: 0.18
identity_confidence_score: 0.54
claim_probability: 0.60
relevance_level: "conditional_high"
relevance_confidence: 0.70
canonical_readiness: "not_ready_hold_for_conversion_qa"
promotion_recommendation: "hold_for_conversion_qa"
---

# Proof Review: Entry 172 Identity Conflict

This review covers the exact staged draft `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-transcript-conflict-source-image-missing-postconv-identity-analysis-20260530124454140.md`.

## Blockers First

- The original source image `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png` is not present in this workspace.
- The conversion-job page image `raw/codex-conversion-jobs/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172/page-images/page-0001.png` is not present in this workspace.
- Row control is unresolved because the assigned chunk and source packet identify entry `172` as a Pulgar/Arriagada child, while the current converted Markdown identifies entry `172` as a Burgos/de la Cruz child.
- The conflict is material: child name, parent set, birth date/time/place, and informant differ. This is not a harmless spelling or transcription variant.
- No canonical claim, parent-child relationship, same-person merge, Dario-line attachment, page rename, or wiki update is ready from this draft.
- The father reading `Jose del Carmen Pulgar S.` is derivative-only in this review context; the final `S.` or terminal mark cannot be promoted without image-controlled QA.

## Evidence Strengths

- The staged identity-analysis note accurately reports the major conflict between the assigned chunk/source packet and the converted Markdown.
- The assigned chunk and source packet are internally consistent for the Pulgar/Arriagada version of entry `172`: child `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`, birth on `Ocho de Marzo de mil ochocientos ochenta i ocho` at about three in the afternoon on `Calle de Valdivia`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`
- The current converted Markdown is internally consistent for the competing Burgos/de la Cruz version of entry `172`: child `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born `El seis de Abril de mil ochocientos ochenta i ocho` at about ten at night in `En esta`, with `Oswaldo Burgos` as compareciente.
- The conversion review note correctly treats this as unresolved derivative-transcript conflict and recommends `hold_for_conversion_qa`.

## Scored Judgment

| Dimension | Score | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.52 | Civil birth registration would be high-quality if image-controlled, but this review could inspect only derivative transcripts and notes. |
| conversion_confidence_score | 0.36 | The chunk and converted Markdown materially disagree, and both referenced image paths are missing. |
| evidence_quantity_score | 0.42 | There are multiple derivative layers, but no available image or independent source page to certify which row controls. |
| agreement_score | 0.18 | Agreement is low across the full evidence set because the chunk/source packet and converted Markdown describe different families under the same entry number. |
| identity_confidence_score | 0.54 | The Pulgar/Arriagada row is plausible within the assigned chunk and packet, but identity confidence is capped by unresolved row control. |
| claim_probability | 0.60 | Probability that the staged identity-analysis conclusion is correct: hold the Pulgar/Arriagada candidate pending conversion QA, with no canonical promotion. |
| relevance_level | conditional_high | High relevance if the Pulgar/Arriagada row is certified; low relevance if the Burgos/de la Cruz row controls entry `172`. |
| relevance_confidence | 0.70 | The relevance conditional is clear, but the controlling row is not. |
| canonical_readiness | not_ready_hold_for_conversion_qa | Not ready for promotion or canonical edits. |

## Claim Probability Notes

- Probability that entry `172` is the Pulgar/Arriagada row: 0.60. This is supported by the assigned chunk and source packet but not image-certified.
- Probability that entry `172` is the Burgos/de la Cruz row: 0.28. This is supported by the current converted Markdown and contradicted by the assigned chunk/source packet.
- Probability that the files reflect a row-control, page-control, or derivative substitution problem: 0.88. The two readings are too different to resolve as name variation.
- Probability that this evidence supports any Dario Pulgar identity attachment: 0.02. No Dario, Arturo, Smith, Dario Jose, or Dario Pulgar A. form appears in the reviewed literal evidence.

## Identity And Relationship Risk

- Same-person evidence for any Dario candidate is absent.
- Parent-child evidence for `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar` is possible only if the Pulgar/Arriagada row is later certified.
- Duplicate-person and relationship-jump risk is high if a worker promotes the Pulgar/Arriagada parent-child facts before row-control QA.
- The staged draft's boundary language is appropriate: it permits later double-checking of Pulgar-line relevance but does not instruct a transcription change unsupported by visible source evidence.

## Next Action

Keep the staged identity-analysis draft on hold. A conversion-QA worker must restore or locate the original source image or certified page image, then compare physical entry `172` against both derivative readings. Only after row control is certified should proof review score the child name, birth details, father field, mother field, informant, and any parent-child relationship for canonical readiness.
