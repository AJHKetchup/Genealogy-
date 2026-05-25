---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260525160625903
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525121552105.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525121552105.md"
review_decision: revise_noncanonical_hold
canonical_readiness: hold_for_conversion_qa
source_quality_score: 0.88
conversion_confidence_score: 0.58
evidence_quantity_score: 0.64
agreement_score: 0.54
identity_confidence_score: 0.76
claim_probability: 0.74
relevance_level: high
relevance_confidence: 0.90
---

# Proof Review: Entry 172 Identity/Conflict Analysis

## Blockers First

1. The staged draft's core hold recommendation is supported, but one literal conflict detail is not supported by the current converted Markdown. The staged draft says the converted file assigns entry 172 to `Jose Francisco`, father `Oswaldo Gomez`, and mother `Emilia de la Cruz`; the reviewed converted file instead assigns entry 172 to `José Miguel`, father `Oswaldo Bunster`, and mother `Amelia de la Maza`.
2. A material derivative-text conflict remains. The current chunk and source image support entry 172 as the Pulgar/Arriagada row, while the converted Markdown has a different entry-172 child-parent cluster. This blocks canonical promotion until conversion QA reconciles the converted file, chunk, and image.
3. The exact father-name ending remains a transcription-risk point. The chunk reads `Jose del Carmen Pulgar S.`, and the image appears broadly consistent with a suffix/mark after Pulgar, but proof review should not force a normalized father form from this review note.
4. No Dario-line or later Pulgar identity bridge is directly supported by entry 172. The source names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario, Arturo, Smith, Dario Jose, or Darío.
5. Existing canonical or staged Pulgar/Juana context derived from this evidence cluster is not independent corroboration while the conversion conflict remains unresolved.

## Evidence Reviewed

- Staged draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525121552105.md`.
- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525115123585.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115123585.md`.
- Chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Converted file: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Page image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Evidence Strengths

- The source image is a civil birth registration page, a strong source class for the registration date, child name, sex, birth date/place, parents, informant, and residence fields.
- The chunk's entry 172 row is materially supported by the visible image: `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at Calle de Valdivia, father `Jose del Carmen Pulgar ...`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The source packet accurately preserves the main Pulgar/Arriagada row and correctly treats the father suffix as unresolved for canonical use.
- The staged draft correctly identifies high identity risk and correctly recommends no canonical promotion, no relationship promotion, and no Dario-line bridge from this entry.

## Scored Judgment

| Metric | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil registration birth record with visible row-level evidence; image quality is usable but not perfect for all small handwriting. |
| conversion_confidence_score | 0.58 | Chunk and image agree on the Pulgar/Arriagada row, but the converted file materially disagrees and the staged draft misstates the converted row's current names. |
| evidence_quantity_score | 0.64 | One direct source image plus derivative chunk/source packet; no independent corroborating source reviewed for identity extension. |
| agreement_score | 0.54 | Image and chunk/source packet agree, but converted Markdown conflicts and the staged draft repeats an outdated or mismatched version of that conflict. |
| identity_confidence_score | 0.76 | Good confidence that the visible entry 172 is a Pulgar/Arriagada birth row; very low confidence for any Dario-line attachment. |
| claim_probability | 0.74 | Probable that entry 172 concerns `Jose del Carmen Segundo Pulgar Arriagada`, but not ready for canonical use while derivative conversion records disagree. |
| relevance_level | high | Directly relevant to Pulgar/Arriagada parent-child candidates and local Pulgar-line identity work. |
| relevance_confidence | 0.90 | The names and family cluster are visibly relevant; downstream Dario relevance remains indirect only. |
| canonical_readiness | hold_for_conversion_qa | Conversion QA must reconcile the row conflict and father suffix before promotion. |

## Claim Probability Notes

- `Entry 172 is the Pulgar/Arriagada birth registration for Jose del Carmen Segundo Pulgar Arriagada`: 0.74, hold pending conversion QA.
- `Jose del Carmen Pulgar S.` is the exact father form: 0.62, hold pending targeted father-field review.
- `Juana Arriagada de Pulgar` is the mother named in this entry: 0.82, hold only because the controlling derivative conversion must be reconciled.
- `This entry supports a Dario/Darío/Arturo/Smith identity bridge`: 0.03, unsupported by this source.

## Next Action

Revise the staged identity/conflict analysis or supersede it with a corrected note that states the current converted-file conflict accurately: converted entry 172 reads `José Miguel` with parents `Oswaldo Bunster` and `Amelia de la Maza`, while the chunk and image support the Pulgar/Arriagada row. Then run targeted conversion QA against the image, converted file, and chunk, with explicit certification of the entry-172 row and father field before any canonical claim, relationship, merge, or Dario-line comparison is promoted.
