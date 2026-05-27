---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260527181212501
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-identity-researcher-20260525210917759.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-identity-researcher-20260525210917759.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-evidence-extraction-20260525202358513.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260525202358513.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row Conflict Hold

## Blockers First

1. The staged draft should remain on hold. The referenced converted file and referenced chunk give incompatible row-172 readings: the converted file reads child `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`; the chunk reads child `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`.
2. The source image path recorded in the staged draft/source packet was not available at review time, so this worker cannot independently certify the visible row or father-field reading from the image.
3. No identity merge, parent-child relationship, Dario-line bridge, or canonical wiki update should be promoted from this draft until targeted conversion QA resolves which transcription controls entry 172.
4. The staged draft's statements about existing canonical wiki pages were not re-verified for this proof review. They are background risk context only, not independently reviewed support for any promotion.

## Evidence Strengths

- The staged draft accurately identifies the core row-level conflict between the assigned chunk/source packet and the current converted Markdown.
- The staged conflict draft and source packet both recommend `hold_for_conversion_qa`, which matches the evidence condition found here.
- The chunk and source packet agree internally on the Pulgar/Arriagada row, including the registration date, child, father, mother, birth date/place, and informant.
- The converted file is internally consistent for a different Burgos/de la Cruz row, which reinforces that this is a row-control conflict rather than a minor spelling or name-order uncertainty.
- The staged draft correctly treats Dario/Dario-line connections as unsupported by the literal entry evidence now available to this reviewer.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 6/10 for civil birth registration as a source type; 3/10 for this review because the source image was unavailable for direct inspection |
| conversion_confidence_score | 2/10 for row 172 because the referenced converted file and chunk conflict materially |
| evidence_quantity_score | 3/10 for the narrow hold judgment; 1/10 for any identity or relationship promotion |
| agreement_score | 2/10 overall; high internal agreement within the chunk/source packet, but direct disagreement with the converted file |
| identity_confidence_score | 2/10 for the Pulgar/Arriagada child identity as promotion-ready; 1/10 for same-person or Dario-line conclusions |
| claim_probability | 0.95 that a conversion row-control conflict exists; 0.35 that the Pulgar/Arriagada row is controlling on currently reviewable materials; 0.10 that the Burgos/de la Cruz row is controlling on currently reviewable materials; 0.02 for any Dario-line bridge |
| relevance_level | high for Pulgar/Arriagada triage if the chunk is confirmed; low for Dario-line identity proof |
| relevance_confidence | 0.80 for conflict triage relevance; 0.20 for Dario-line relevance |
| canonical_readiness | hold_for_conversion_qa |

## Review Finding

The staged identity analysis is supported as a hold, not as a promotable proof. Its main conclusion is appropriately conservative: the row-level conflict must be resolved before any canonical claim, relationship, or identity comparison can use entry 172.

The Pulgar/Arriagada reading has useful internal support from the chunk and source packet, but the converted file supplies a different entry 172 and the source image was not available to this reviewer. That combination keeps conversion confidence too low for canonical use.

## Next Action

Run targeted conversion QA for page 58, entry 172 against the actual source image. QA should decide whether the controlling row is Pulgar/Arriagada or Burgos/de la Cruz and should explicitly certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, rerun proof review before any canonical promotion.
