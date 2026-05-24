---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260524143708653
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524141515582.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524141515582.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524141515582.md
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
source_quality_score: 0.86
conversion_confidence_score: 0.45
evidence_quantity_score: 0.62
agreement_score: 0.38
identity_confidence_score: 0.74
claim_probability: 0.72
relevance_level: high
relevance_confidence: 0.92
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Pulgar/Arriagada Identity Analysis Revision

## Blockers

- The revised staged draft correctly identifies a material row-level conflict: the referenced converted Markdown transcribes entry 172 as a Gomez/de la Maza birth, while the referenced chunk and visible source image show entry 172 as the Pulgar/Arriagada birth registration. This is not a minor name-reading disagreement and blocks canonical promotion.
- The father's surname suffix remains unresolved. The image and chunk support `Jose del Carmen Pulgar` as the father, but the final mark after `Pulgar` is not reliable enough for a canonical suffix value without targeted conversion QA.
- The converted Markdown cannot be used as reliable literal support for the Pulgar/Arriagada claims in its current state because it carries a different entry 172 transcription.
- No Dario identity is named in the visible entry. The staged draft's guardrail against attaching this record to any Dario candidate by surname or family context alone is supported.

## Evidence Strengths

- The source image is a civil birth register image with visible page 58, entry 172. As a source class, it is strong direct evidence for the birth registration and stated child-parent cluster.
- The referenced chunk aligns with the source image on the main Pulgar/Arriagada facts: child `Jose del Carmen Segundo Pulgar Arriagada`, male sex, registration date of 7 April 1888, birth date of 8 March 1888 at about 3 p.m., birth place `Calle de Valdivia`, father `Jose del Carmen Pulgar`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The source packet accurately surfaces the conversion conflict and recommends holding for conversion QA rather than promoting unsupported canonical conclusions.
- Identity relevance is high for the Pulgar/Arriagada cluster because the source directly names the child and parents in one birth-registration row.

## Scored Judgment

| Metric | Score / Value | Rationale |
| :--- | :--- | :--- |
| source_quality_score | 0.86 | Direct civil registration image, visible and broadly legible, but some handwriting details remain uncertain. |
| conversion_confidence_score | 0.45 | The chunk fits the image, but the converted Markdown for the same entry is materially wrong or mismatched. |
| evidence_quantity_score | 0.62 | One direct source image plus one aligned chunk and source packet; no independent corroborating source in scope. |
| agreement_score | 0.38 | Strong agreement between image, chunk, and source packet; poor agreement with the converted Markdown. |
| identity_confidence_score | 0.74 | Main Pulgar/Arriagada identity cluster is likely, but canonical identity confidence is reduced by the conversion conflict and father suffix uncertainty. |
| claim_probability | 0.72 | The child-parent cluster is probably supported by the visible register row, but not ready for canonical use until conversion QA reconciles the transcript. |
| relevance_level | high | The entry directly concerns the named Pulgar/Arriagada child and parents. |
| relevance_confidence | 0.92 | The relevant names appear in the source image and chunk. |
| canonical_readiness | hold_for_conversion_qa | Promotion should wait for corrected/superseded converted Markdown and an explicit father-suffix decision. |

## Review Decision

Hold the staged identity analysis for conversion QA. The staged draft is appropriately conservative and should not be promoted to canonical claims, relationships, or person/family pages yet.

## Next Action

Send this record to targeted conversion QA to reconcile the converted Markdown with the source image and chunk, then rerun proof review for the child identity, birth facts, parent relationships, and the exact father-name rendering.
