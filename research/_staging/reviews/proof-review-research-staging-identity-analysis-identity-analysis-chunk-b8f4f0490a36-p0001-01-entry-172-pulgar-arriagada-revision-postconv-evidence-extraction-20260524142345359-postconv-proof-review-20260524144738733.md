---
type: proof_review
role: claim_reviewer
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524142345359.md"
worker: postconv-proof-review-20260524144738733
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524142345359.md"
reviewed_subject: "Jose del Carmen Segundo Pulgar Arriagada"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524142345359.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Pulgar/Arriagada Identity Analysis

## Blockers

- The referenced converted Markdown materially conflicts with the source image and assigned chunk for register page 58, entry 172. It transcribes entry 172 as `José Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`, while the image-visible row and assigned chunk support a Pulgar/Arriagada birth entry.
- The father's final mark after `Pulgar` remains uncertain. The source image supports `Jose del Carmen Pulgar` as the broad father reading, but the possible suffix or mark should not be normalized canonically without targeted conversion QA.
- This source does not name Dario, `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or any Dario passenger candidate. No identity merge or lineage bridge to a Dario cluster is supported by this entry alone.
- Relationship use should remain limited to the entry-local child-parent cluster until the row-level conversion conflict is reconciled. Do not promote dependent claims or relationships from the conflicting derivative set.

## Evidence Strengths

- The original source image is present and directly relevant to the staged draft. Visual review of page 58, entry 172 supports a birth registration row for `Jose del Carmen Segundo Pulgar Arriagada`, male, with father `Jose del Carmen Pulgar` and mother `Juana Arriagada de Pulgar`.
- The assigned chunk matches the image-visible Pulgar/Arriagada row closely enough to support the staged draft's hold recommendation and guardrails.
- The staged identity analysis correctly preserves uncertainty instead of forcing the father suffix or attaching the entry to a Dario candidate.
- The source type is strong for birth identity and parent names because it is a civil birth register, but the current derivative conflict lowers readiness for canonical use.

## Scores

| score | value | rationale |
| :--- | :--- | :--- |
| source_quality_score | 0.86 | Civil birth register image is a strong direct source for the entry-local identity facts. |
| conversion_confidence_score | 0.42 | The assigned chunk agrees with the image, but the referenced converted Markdown gives a different entry 172 row. |
| evidence_quantity_score | 0.64 | One direct source image plus one supporting chunk; no independent corroborating source in this review scope. |
| agreement_score | 0.50 | Image and chunk agree on the Pulgar/Arriagada row, while the converted Markdown sharply disagrees. |
| identity_confidence_score | 0.74 | Good confidence for the entry-local child identity; reduced by father-suffix uncertainty and derivative conflict. |
| claim_probability | 0.72 | The staged identity analysis is probably correct as a cautious Pulgar/Arriagada entry-local analysis, but not canonically ready. |
| relevance_level | direct | The reviewed image, chunk, packet, and converted file all concern the assigned entry 172 source. |
| relevance_confidence | 0.97 | The staged draft cites the exact local source image and derivative files reviewed here. |
| canonical_readiness | hold_for_conversion_qa | Hold until targeted QA reconciles or supersedes the converted Markdown and records the father-name suffix/mark policy. |

## Claim Probability Notes

| claim or interpretation | probability | review judgment |
| :--- | :--- | :--- |
| Entry 172 is the Pulgar/Arriagada birth row described in the staged draft. | 0.82 | Supported by source image and assigned chunk, but still blocked by derivative conflict. |
| The child is recorded as `Jose del Carmen Segundo Pulgar Arriagada`. | 0.80 | Visibly supported and chunk-supported; keep spelling/diacritics conservative. |
| The father can be canonically normalized beyond `Jose del Carmen Pulgar` from this review alone. | 0.45 | Hold; final mark or suffix after Pulgar is unresolved. |
| The entry supports attachment to any Dario candidate. | 0.02 | Unsupported; no Dario is named in this source. |

## Next Action

Keep the staged identity analysis at `hold_for_conversion_qa`. Run targeted conversion QA for page 58, entry 172 to reconcile the converted Markdown against the source image/current chunk and explicitly decide how to transcribe the father field after `Pulgar`. After that, rerun proof review for the child identity, birth facts, child-parent relationships, and any parent-candidate merge question before canonical promotion.
