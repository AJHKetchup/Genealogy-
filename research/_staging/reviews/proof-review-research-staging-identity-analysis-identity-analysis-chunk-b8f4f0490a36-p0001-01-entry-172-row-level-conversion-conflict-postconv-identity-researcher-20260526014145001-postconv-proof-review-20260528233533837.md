---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260528233455136
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526014145001.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526014145001.md"
reviewed_files:
  - "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526014145001.md"
  - "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526002943637.md"
  - "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526002943637.md"
  - "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
  - "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
  - "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
source_quality_score: 0.88
conversion_confidence_score: 0.46
evidence_quantity_score: 0.72
agreement_score: 0.48
identity_confidence_score: 0.34
claim_probability: 0.30
relevance_level: high_for_row_conflict_low_for_dario_identity
relevance_confidence: 0.86
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

- Canonical readiness remains `hold`. The staged draft is well supported as a conflict/hold analysis, but the repository still contains a row-level contradiction between the referenced chunk/source packet and the current converted Markdown.
- The current converted Markdown reads entry 172 as `Jose Miguel`, son of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888 at about 10 p.m. in `En esta`.
- The referenced chunk and source packet read entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at about 3 p.m. at Calle de Valdivia, with father `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- The source image visually favors the Pulgar/Arriagada row for entry 172, but this review should not silently rewrite the converted Markdown. The safe action is still targeted conversion QA or correction of the controlling conversion artifact before canonical promotion.
- The staged draft's Dario-line caution is supported. Entry 172 does not name Dario, Arturo, Smith, a spouse, a child of Dario, or a passenger-list context. Any Dario identity bridge would be a relationship jump from this source alone.

## Scores

| Category | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth register image is a strong primary source for the row if the row is correctly controlled. Image quality is usable, though small handwriting and table alignment still justify QA. |
| conversion_confidence_score | 0.46 | The chunk/source packet and image agree in substance, but the current converted Markdown gives a different family and event details for entry 172. |
| evidence_quantity_score | 0.72 | There is one primary image plus three local derivative artifacts. Quantity is enough to identify the conflict, not enough to promote while artifacts disagree. |
| agreement_score | 0.48 | Agreement is high among the chunk, source packet, conflict draft, staged identity analysis, and visible image; agreement is broken by the current converted Markdown. |
| identity_confidence_score | 0.34 | The Pulgar/Arriagada row appears likely for entry 172, but identity conclusions remain low because row control and father-name extent are not fully settled. |
| claim_probability | 0.30 | Probability that any canonical claim should be promoted now is low. Probability that the staged hold recommendation is correct is high. |
| relevance_level | high_for_row_conflict_low_for_dario_identity | The item is directly relevant to Pulgar/Arriagada row control, only background-relevant to Dario-line identity work. |
| relevance_confidence | 0.86 | Relevance boundaries are clear from the named persons and absent Dario evidence. |
| canonical_readiness | hold | No canonical claim, relationship, merge, or name variant should be promoted from this staged draft. |

## Evidence Strengths

- The staged draft accurately reports the central conflict: assigned chunk/source packet versus current converted Markdown for entry 172.
- The referenced chunk gives a coherent row 172 transcription for `Jose del Carmen Segundo Pulgar Arriagada`, including registration date, sex, birth date/time/place, parents, parent domicile, and informant.
- The source packet repeats the same Pulgar/Arriagada reading and explicitly recommends `hold_for_conversion_qa`, matching the staged draft's cautious conclusion.
- The source image, inspected only as verification context, visibly aligns with the chunk's Pulgar/Arriagada entry 172 structure more than with the Burgos/de la Cruz converted Markdown.
- The staged draft correctly avoids promoting Dario-line conclusions and flags the risk of merging Jose/Juana candidates by name resemblance.

## Review Judgment

The staged draft is acceptable as a hold analysis. Its literal support is strong for the existence of a row-control conflict and for the recommendation not to promote. Its stronger hypothesis that entry 172 is probably the Pulgar/Arriagada row is reasonable, especially after viewing the image, but the contradiction in the current converted Markdown remains a blocker for canonical use.

Claim probability is therefore split: the probability that the staged draft's hold recommendation is correct is approximately 0.92, while the probability that a canonical identity or relationship claim should be promoted now is 0.30 or lower. The staged draft should remain in staging until conversion QA resolves the controlling row and father-field extent.

## Next Action

Run targeted conversion QA against the source image, the current converted Markdown, and the chunk for entry 172 only. QA should decide whether the controlling row is Pulgar/Arriagada or Burgos/de la Cruz, and if Pulgar/Arriagada controls, certify the visible father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or an explicitly uncertain form. After QA, rerun proof review on the narrow birth and parent-child claims before any canonical action.
