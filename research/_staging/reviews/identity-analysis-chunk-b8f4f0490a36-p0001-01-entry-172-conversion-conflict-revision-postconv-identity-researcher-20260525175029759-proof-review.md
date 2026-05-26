---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260526000555453
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525175029759.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525175029759.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525170607416.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Conversion Conflict Identity Analysis

## Blockers First

- Hold for targeted conversion QA. The source image and assigned chunk support entry 172 as a Pulgar/Arriagada birth registration, but the assigned converted Markdown transcribes entry 172 as a different non-Pulgar row.
- The staged identity-analysis draft correctly identifies the row-level conflict in substance, but it inaccurately summarizes the current converted Markdown. The draft says the converted Markdown gives child `Jose Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`, birth `20 February 1888`, place `Pellin`; the converted file actually gives child `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, birth `6 April 1888`, place `En esta`.
- The father field in the source-supported Pulgar/Arriagada row remains unresolved at the ending after `Pulgar`. The assigned chunk reads `Jose del Carmen Pulgar S.`, but the staged packet preserves `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` as QA outcomes.
- No Dario is named in the checked source image, chunk, source packet, or converted file. This item cannot bridge or merge any Dario Pulgar identity cluster by surname or family context alone.
- Do not promote child identity, birth facts, parent-child relationships, parent-candidate merges, or Dario-line comparisons until the controlling transcription is certified.

## Evidence Strengths

- The source image visibly shows register page 58, entry 172, with child name consistent with `Jose del Carmen Segundo Pulgar Arriagada`, sex male, birth on 8 March 1888 at about 3 p.m., place `Calle de Valdivia`, father `Jose del Carmen Pulgar...`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The assigned chunk gives the same Pulgar/Arriagada row for entry 172 and includes father/mother attributes and informant details.
- The source packet clearly flags the conflict as row-level or file-assignment, not a spelling variant, and recommends `hold_for_conversion_qa`.
- The staged identity-analysis draft is appropriately conservative on canonical action and correctly rejects any Dario attachment.

## Review Scores

| Dimension | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth register image is direct evidence for the birth entry; visual legibility is good enough for the core row but not perfect for the father's terminal mark. |
| conversion_confidence_score | 0.40 | The chunk aligns with the visible source image, but the converted Markdown is materially inconsistent with both. |
| evidence_quantity_score | 0.62 | One direct source image plus two derivative staging/transcription artifacts; no independent corroborating record checked for this task. |
| agreement_score | 0.46 | Source image, chunk, and source packet agree on the Pulgar/Arriagada cluster, while the converted file and the staged draft's summary of it conflict. |
| identity_confidence_score | 0.72 | Probable that the source-supported entry 172 is the Pulgar/Arriagada child, but confidence is capped by conversion conflict and father-ending uncertainty. |
| claim_probability | 0.76 | The Pulgar/Arriagada reading is more probable than the converted Markdown row for this source image, but not promotion-ready. |
| relevance_level | 0.93 | Directly relevant to Pulgar/Arriagada identity controls and anti-conflation safeguards. |
| relevance_confidence | 0.95 | The reviewed draft, source packet, chunk, and image all concern the exact assigned entry 172 conflict. |
| canonical_readiness | 0.15 | Hold; needs targeted conversion QA before any canonical promotion. |

## Judgment

The staged draft should remain a hold/revise item, not a promotion source. Its core caution is well supported: entry 172 has a serious derivative-transcription conflict, and the visible source favors the Pulgar/Arriagada row over the converted Markdown row. However, the staged draft's description of what the converted Markdown says is not literally supported by the current converted file, so the review should not be treated as cleanly verified until that discrepancy is resolved.

## Next Action

Run targeted conversion QA against the source image, assigned converted Markdown, assigned chunk, and source packet. The QA note should certify the controlling entry 172 row and the exact father-field ending after `Pulgar`, then route the item back for proof review before any canonical promotion.
