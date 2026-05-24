---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524144531925.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524144531925.md
reviewer: postconv-proof-review-20260524153405204
review_date: 2026-05-24
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Pulgar/Arriagada Identity Analysis

## Blockers

- The referenced converted Markdown and the referenced chunk do not agree at the row level. The converted Markdown gives entry 172 as child `Jose Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`, born 26 March 1888 at 10 p.m. The chunk gives entry 172 as child `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888 at 3 p.m.
- This is a material conversion/file-assignment conflict, not a spelling or normalization issue. Canonical promotion should wait for targeted conversion QA that either corrects or supersedes the converted Markdown.
- The father's final mark or suffix after `Pulgar` is not secure enough for canonical identity construction. Use `Jose del Carmen Pulgar` only as the broad supported reading until QA resolves whether the source supports `Pulgar S.` or an uncertain final mark.
- Do not connect this entry to any Dario candidate. The visible source, chunk, source packet, and staged draft do not name Dario, and surname/family context alone is not sufficient for an identity bridge.

## Scores

- source_quality_score: 0.86
- conversion_confidence_score: 0.42
- evidence_quantity_score: 0.68
- agreement_score: 0.48
- identity_confidence_score: 0.70
- claim_probability: 0.72
- relevance_level: high
- relevance_confidence: 0.88
- canonical_readiness: hold_for_conversion_qa

## Evidence Strengths

- The source is a civil birth register image, close to the event and strong for registration-scoped birth facts, named parents, and informant/declarant details.
- Direct image review supports that register page 58, entry 172 is the Pulgar/Arriagada row rather than the Gomez/de la Cruz row described in the converted Markdown.
- The assigned chunk and source packet consistently support the staged draft's core identity cluster: child `Jose del Carmen Segundo Pulgar Arriagada`, mother `Juana Arriagada de Pulgar`, informant `Ernesto Herrera L.`, registration date 7 April 1888, and birth date 8 March 1888 at about 3 p.m. on Calle de Valdivia.
- The staged draft appropriately preserves uncertainty and recommends `hold_for_conversion_qa` instead of promoting dependent claims.

## Claim Review

| Claim area | Judgment | Claim probability | Notes |
| --- | --- | ---: | --- |
| Child identity as `Jose del Carmen Segundo Pulgar Arriagada` in entry 172 | supported_with_conversion_conflict | 0.78 | Supported by image, chunk, and source packet; contradicted by assigned converted Markdown. Hold until conversion QA resolves the derivative transcript conflict. |
| Birth facts: 8 March 1888, about 3 p.m., Calle de Valdivia | supported_with_conversion_conflict | 0.74 | Supported by image/chunk/source packet; contradicted by converted Markdown. Suitable for staged analysis only. |
| Mother as `Juana Arriagada de Pulgar` | supported_with_conversion_conflict | 0.76 | Supported by image/chunk/source packet; contradicted by converted Markdown. Do not use for canonical relationship promotion yet. |
| Father as `Jose del Carmen Pulgar` / possible suffix | revise_before_canonical | 0.64 | Broad father reading is supported, but the final suffix/mark after Pulgar is unresolved. Canonical identity should not encode the suffix until rechecked. |
| Informant as `Ernesto Herrera L.` | supported_with_conversion_conflict | 0.72 | Supported by image/chunk/source packet; contradicted by converted Markdown's different informant. Hold with the rest of the row. |
| Negative Dario attachment | supported_guardrail | 0.92 | No Dario is named. The draft correctly blocks identity linkage to Dario Arturo Pulgar-Smith or related Dario candidates without independent evidence. |

## Review Judgment

The staged identity analysis is a cautious and well-framed review note, not a canonically promotable proof. The best available verification context supports the Pulgar/Arriagada row in the image and assigned chunk, but the assigned converted Markdown describes a different entry. That conflict reduces conversion confidence and agreement enough that all dependent claims should remain held.

Canonical readiness is `hold_for_conversion_qa`. After QA reconciles the converted Markdown with the image/chunk and records the father suffix decision, rerun proof review on child identity, birth facts, parent-child relationships, parent attributes, and any proposed parent/person merge.

## Next Action

Run targeted conversion QA for the referenced conversion file and entry 172. The QA note should explicitly decide whether the canonical verification transcript should follow the visible Pulgar/Arriagada row and how to represent the father field after `Jose del Carmen Pulgar`.
