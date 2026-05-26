---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260526061755102
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526044220967.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526044220967.md"
reviewed_context:
  - "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526020438864.md"
  - "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526020438864.md"
  - "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
  - "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
  - "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold
---

# Proof Review: Entry 172 Identity Conflict Analysis

## Blockers First

1. The staged identity-analysis draft is correctly treating this as a material row-level conflict. The referenced chunk and source packet identify entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, while the referenced converted Markdown identifies entry 172 as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
2. The converted Markdown is not reliable for canonical use in its current form because it contradicts the chunk and the visible page image for entry 172. This affects the child name, birth date, birth place, parents, informant, and downstream relationship claims.
3. The visible image supports the Pulgar/Arriagada row at entry 172, but this proof-review note should not rewrite the conversion or promote claims. A targeted conversion-QA correction remains the required next step.
4. The father-field suffix remains a proof-sensitive uncertainty. The visible row supports `Jose del Carmen Pulgar` and appears consistent with a trailing `S.` or similar mark, but the exact suffix should be certified by conversion QA before any father identity or merge claim is promoted.
5. No reviewed evidence names Dario or supplies a relationship bridge to any Dario/Dario/Darío Pulgar identity. Any Dario-line use should remain anti-conflation context only.

## Evidence Strengths

- The source is a civil birth register image with direct, event-level evidence for an entry numbered 172 on page 58.
- The chunk transcription is internally coherent and matches the visible page image at the row level: entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, with father `Jose del Carmen Pulgar`, mother `Juana Arriagada de Pulgar`, and compareciente `Ernesto Herrera L.`
- The source packet accurately flags low conversion confidence and recommends holding for targeted QA rather than promoting a parent-child relationship.
- The staged identity-analysis draft appropriately treats same-cluster canonical pages as derivative, not independent corroboration.
- The draft's high conflict severity is supported: the two derivative text layers describe different children, dates, places, parents, and informants.

## Scored Judgment

| Factor | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.86 | Direct civil registration image; high-value source type, though handwriting and page spread layout require careful row control. |
| conversion_confidence_score | 0.34 | The chunk aligns with the visible image, but the converted Markdown for the same source has a severe conflicting row. |
| evidence_quantity_score | 0.58 | One direct source image plus derivative chunk/source-packet layers; no independent corroborating source reviewed. |
| agreement_score | 0.42 | Chunk, source packet, and image agree broadly, but the converted Markdown sharply disagrees. |
| identity_confidence_score | 0.66 | Better support for the Pulgar/Arriagada entry-172 identity than the Burgos/de la Cruz reading, but not ready for canonical identity promotion while the conversion conflict remains unresolved. |
| claim_probability | 0.70 | Probable that the source page's entry 172 is the Pulgar/Arriagada row; probability is limited by unresolved conversion QA and father suffix uncertainty. |
| relevance_level | high | Directly relevant to Pulgar/Arriagada identity and parent-child candidates; only low relevance to Dario-line bridge questions. |
| relevance_confidence | 0.88 | The visible row and chunk contain Pulgar and Arriagada names, making family relevance clear even while proof status is held. |
| canonical_readiness | hold | Do not promote until targeted conversion QA resolves the conversion file conflict and certifies the father-field reading. |

## Claim-Level Review

| Claim or hypothesis | Probability | Review decision | Rationale |
| --- | ---: | --- | --- |
| Entry 172 is the birth registration for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.70 | hold_pending_conversion_qa | Supported by chunk, source packet, and visible image; blocked by contradictory converted Markdown. |
| Entry 172 is the converted-file `Jose Miguel` / Burgos / de la Cruz row. | 0.12 | revise_or_reject_after_qa | The visible source image for entry 172 does not support this reading; it appears to be a conversion row/source mismatch. |
| Father is `Jose del Carmen Pulgar S.`. | 0.56 | hold_pending_suffix_certification | Father name is visibly Pulgar and likely Jose del Carmen; suffix requires targeted visual QA before canonical use. |
| Mother is `Juana Arriagada de Pulgar`. | 0.72 | hold_pending_conversion_qa | The image and chunk support this reading, but promotion should wait until row conflict resolution. |
| Parent-child relationship between the child and Jose/Juana. | 0.68 | hold_pending_conversion_qa | Relationship is directly stated if the Pulgar row is certified, but not ready while the conversion conflict remains open. |
| Any bridge to Dario Arturo Pulgar-Smith or other Dario/Darío Pulgar identities. | 0.03 | reject_for_this_source | No Dario name, relationship bridge, or chronology bridge is present in the reviewed evidence. |

## Source Reliability And Identity Risk

- Source reliability is strong because the underlying record is an official civil birth register, but extraction reliability is compromised by competing derivative transcriptions.
- Identity risk is high for automatic promotion because the wrong row would create an entirely different child and parent set.
- Relationship jump risk is high for any parent-child claim before QA; it is especially high for any merge of `Jose del Carmen Pulgar S.` into another Jose del Carmen Pulgar identity.
- Relevance is high for Pulgar/Arriagada research and low for Dario-line proof except as a warning against surname-based conflation.

## Next Action

Run targeted conversion QA for the source image, chunk, and converted Markdown. The QA note should explicitly decide that page 58 entry 172 is the Pulgar/Arriagada row or explain any contrary finding, then certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review for the child identity, birth facts, parent names, and parent-child relationship claims before any canonical promotion.
