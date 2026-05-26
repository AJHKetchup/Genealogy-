---
type: proof_review
status: hold_for_conversion_qa
role: claim_reviewer
worker: postconv-proof-review-20260526095846903
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-identity-researcher-20260526084633493.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-identity-researcher-20260526084633493.md
reviewed_conflict_draft: research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-held-postconv-evidence-extraction-20260526063217904.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526063217904.md
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
source_quality_score: 0.86
conversion_confidence_score: 0.35
evidence_quantity_score: 0.58
agreement_score: 0.42
identity_confidence_score: 0.66
claim_probability: 0.88
relevance_level: high
relevance_confidence: 0.90
canonical_readiness: 0.08
canonical_readiness_label: hold_for_conversion_qa
created: 2026-05-26
---

# Proof Review: Entry 172 Conversion Conflict

## Blockers First

- Canonical readiness remains very low. The staged draft correctly identifies a row-level conversion conflict for entry `172`, and no child identity, birth fact, parent-child relationship, parent merge, or Dario-line bridge should be promoted from this file.
- The current converted Markdown and current chunk disagree materially for the same entry number. The converted Markdown gives a Burgos/de la Cruz child `José Miguel`; the chunk gives a Pulgar/Arriagada child `Jose del Carmen Segundo Pulgar Arriagada`.
- The visible source image supports the Pulgar/Arriagada row for register page 58, entry `172`, but this review does not edit or replace the converted Markdown. Targeted conversion QA must decide the controlling derivative text.
- The father field is not ready for normalization. I can support that the field begins `Jose del Carmen Pulgar`; the terminal `S.` or mark remains uncertain enough to keep `Jose del Carmen Pulgar S.` / `Jose del Carmen Pulgar [?]` unresolved.
- Any wiki-page or prior staged identity context named in the staged draft is not independent proof for this review. It can only be context; it cannot bootstrap the contested entry or a same-person conclusion.

## Evidence Scores

| Score | Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth register image is a strong primary source, and the entry row is visible enough to verify the broad Pulgar/Arriagada reading. |
| conversion_confidence_score | 0.35 | The derivative artifacts conflict sharply: converted Markdown records Burgos/de la Cruz, while the chunk/source packet records Pulgar/Arriagada. |
| evidence_quantity_score | 0.58 | One source image and two derivative pathways are available, but all claims still depend on resolving the row-control conflict. |
| agreement_score | 0.42 | Source packet, chunk, and image align broadly; converted Markdown disagrees on nearly every identity-bearing field. |
| identity_confidence_score | 0.66 | If the Pulgar row controls, the child and parents are plausible as read, but identity confidence is capped by conversion conflict and father-field uncertainty. |
| claim_probability | 0.88 | The claim that this staged item is a row-level conversion conflict is strongly supported. Probability for canonical Pulgar promotion is much lower until QA resolves the conflict. |
| relevance_level | high | A Pulgar/Arriagada birth row would be family-relevant; the Burgos/de la Cruz converted row would not be meaningfully Pulgar-line relevant. |
| relevance_confidence | 0.90 | The relevance judgment is clear because the competing readings either contain Pulgar/Arriagada names directly or do not. |
| canonical_readiness | 0.08 | Hold for conversion QA; no canonical promotion is ready. |

## Evidence Strengths

- The staged draft accurately preserves the central conflict: same entry number, same register page reference, but incompatible derivative readings.
- The source packet and chunk support the Pulgar/Arriagada reading for entry `172`: child `Jose del Carmen Segundo Pulgar Arriagada`, birth `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`, place `Calle de Valdivia`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`
- The converted Markdown supports the competing Burgos/de la Cruz reading for entry `172`: child `José Miguel`, birth `seis de Abril de mil ochocientos ochenta i ocho`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and informant `Oswaldo Burgos`.
- The staged draft's anti-conflation conclusion is appropriate: this evidence does not support merging or attaching the entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`.

## Claim Judgment

| Claim | Support | Probability | Review Judgment |
| --- | --- | ---: | --- |
| Entry `172` currently has a row-level derivative transcript conflict. | Supported by direct comparison of staged conflict draft, source packet, chunk, converted Markdown, and visible source image. | 0.88 | Accept as staged hold/conflict claim. |
| Entry `172` should be canonically treated as the Pulgar/Arriagada birth. | Plausible from image/chunk/source packet, but contradicted by current converted Markdown. | 0.59 | Hold for targeted conversion QA. |
| Entry `172` should be canonically treated as the Burgos/de la Cruz birth. | Supported only by current converted Markdown in this review set; contradicted by image/chunk/source packet. | 0.25 | Hold/revise after QA. |
| Father can be normalized to `Jose del Carmen Pulgar`. | Field begins that way, but terminal mark is unresolved. | 0.52 | Hold; preserve uncertainty. |
| Mother is `Juana Arriagada de Pulgar` if Pulgar row controls. | Directly supported by chunk/source packet and visible row context. | 0.56 | Conditional only; hold. |
| Any Dario Pulgar candidate is the child in this entry. | No literal Dario/Arturo/Smith bridge appears in the reviewed source materials. | 0.02 | Reject for this evidence. |

## Next Action

Keep the staged draft on `hold_for_conversion_qa`. The next required action is targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01`: compare the source image, current converted Markdown, current chunk, and held source packet; decide the controlling entry-172 row; and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, rerun proof review before any canonical claim, relationship, identity merge, or Dario-line bridge is promoted.
