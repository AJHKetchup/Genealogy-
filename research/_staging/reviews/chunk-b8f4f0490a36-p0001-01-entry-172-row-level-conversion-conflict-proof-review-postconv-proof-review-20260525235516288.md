---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260525235516288
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525230735548.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525230735548.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525220612902.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
created: 2026-05-25
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. **Converted-file conflict:** the reviewed converted Markdown identifies entry 172 as `José Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, while the reviewed chunk and source packet identify entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`.
2. **Row-control risk:** this is a material row/page-control conflict, not a spelling variant or same-person conflict. Names, parents, birth date, place, and informant differ between the converted file and the chunk/source packet.
3. **Father-field risk:** the visible image and chunk support `Jose del Carmen Pulgar` as the father base name, but the final trailing element after `Pulgar` remains a conversion-confidence risk. Do not promote the suffix as certain without targeted QA.
4. **Relationship/identity risk:** parent-child links for the Pulgar/Arriagada family should remain staged until conversion QA certifies the controlling row and exact father-field reading.
5. **Dario-attachment blocker:** this source names no Dario candidate. It cannot support a Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario/Darío Pulgar Arriagada attachment.

## Scored Judgment

- **source_quality_score:** 0.86
- **conversion_confidence_score:** 0.38
- **evidence_quantity_score:** 0.42
- **agreement_score:** 0.35
- **identity_confidence_score:** 0.62 for the narrow Pulgar/Arriagada entry-172 hypothesis; 0.05 for any Dario identity attachment
- **claim_probability:** 0.70 that the source image/chunk/source packet reflect a real entry-172 Pulgar/Arriagada row; 0.40 that the exact father form includes the trailing `S.`; 0.05 for any direct Dario claim
- **relevance_level:** high for Pulgar/Arriagada family reconstruction; low for Dario identity proof
- **relevance_confidence:** 0.82 for Pulgar/Arriagada relevance; 0.20 for Dario relevance
- **canonical_readiness:** hold_for_conversion_qa

## Evidence Strengths

- The source packet and chunk consistently transcribe entry 172 on page 58 as `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`, with father `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- The referenced page image visibly shows entry 172 on page 58 as a Pulgar/Arriagada registration rather than the Burgos/de la Cruz entry in the current converted Markdown.
- The staged identity analysis correctly keeps the Pulgar/Arriagada reading separate from the Burgos/de la Cruz converted-file reading and recommends `hold_for_conversion_qa`.
- The draft correctly refuses a Dario bridge: no literal Dario name, spouse, child, occupation bridge, or other identity linkage appears in the reviewed entry.

## Review Finding

Revise/hold rather than promote. The staged draft's main conclusion is supported: this is a row-level conversion conflict requiring targeted conversion QA. The Pulgar/Arriagada reading has meaningful support from the chunk, source packet, and visible image, but the conflicting converted Markdown prevents canonical use until the conversion-control problem is resolved. The father suffix should be treated as uncertain or separately certified; the base father name `Jose del Carmen Pulgar` is better supported than the exact `S.` expansion.

## Next Action

Run targeted conversion QA on the source image, converted Markdown, chunk, and source packet. QA should decide whether entry 172 controls as the Pulgar/Arriagada row and should certify the father field exactly as visible. After QA, rerun proof review before any child identity, parent-child relationship, Jose/Juana merge, or Dario-related claim is promoted.
