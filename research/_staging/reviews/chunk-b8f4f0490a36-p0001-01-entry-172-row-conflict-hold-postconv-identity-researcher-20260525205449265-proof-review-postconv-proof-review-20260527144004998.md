---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260527144004998
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-identity-researcher-20260525205449265.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-identity-researcher-20260525205449265.md"
reviewed_sources:
  - "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
  - "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
  - "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260525202358513.md"
  - "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-evidence-extraction-20260525202358513.md"
  - "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: blocked
promotion_recommendation: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row Conflict Identity Analysis

This review covers only the staged draft `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-identity-researcher-20260525205449265.md`.

## Blockers First

1. The staged draft is literally supported that a row-level derivative conflict exists: the assigned converted Markdown records entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, while the assigned chunk records entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`.
2. The conflict is identity-bearing, not a spelling variant. It changes the child, parents, birth date/time/place, informant, and associated family line.
3. The source image, at visual review level, appears to align with the Pulgar/Arriagada row in the entry-172 position, but this proof-review task must not rewrite the conversion. Targeted conversion QA still needs to certify the controlling transcription and the exact father-field reading.
4. The father-field reading remains unresolved between `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and an uncertain `Jose del Carmen Pulgar [?]`; no normalization or merge is ready.
5. No Dario-line identity or relationship claim is supported by this entry. Any Dario comparison remains anti-conflation context only.

## Evidence Strengths

- The staged draft accurately identifies the core contradiction between the converted Markdown and the chunk/source-packet readings.
- The assigned chunk and source packet are internally consistent for entry 172 as a Pulgar/Arriagada birth-registration row.
- The civil birth register is a relevant original-record source type for a birth, parents, residence, and informant, once the row transcription is certified.
- The source image gives useful visual corroboration for why the chunk/source-packet reading deserves conversion QA attention.
- The staged draft appropriately recommends hold/block rather than promotion.

## Scored Judgment

| Factor | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil birth register image is a strong source type, but the derivative conflict prevents immediate use. |
| conversion_confidence_score | 0.35 | Converted Markdown and chunk disagree across the entire entry 172 row. |
| evidence_quantity_score | 0.55 | One source image plus conflicting derivative transcriptions; enough to identify a conflict, not enough for canonical promotion. |
| agreement_score | 0.20 | Chunk/source packet agree with each other, but the assigned converted Markdown directly conflicts. |
| identity_confidence_score | 0.48 | Pulgar/Arriagada is plausible from chunk and image review, but identity confidence remains reduced until QA certifies the row. |
| claim_probability | 0.58 | Probability that entry 172 is the Pulgar/Arriagada row is above the Burgos/de la Cruz alternative, but not promotion-ready under the task boundary. |
| relevance_level | high | If certified, the row is directly relevant to Pulgar/Arriagada identity and parent-child claims. |
| relevance_confidence | 0.88 | Relevance is clear for the Pulgar/Arriagada family cluster, assuming the row is confirmed. |
| canonical_readiness | blocked | No canonical claim, relationship, identity merge, or wiki update should be made before conversion QA and rerun proof review. |

## Claim-Level Review

| Proposed or implied claim | Review judgment | Claim probability | Canonical readiness |
| --- | --- | ---: | --- |
| Entry 172 is a Pulgar/Arriagada birth row. | Hold. Supported by chunk/source packet and visually plausible in the page image, but contradicted by the assigned converted Markdown. | 0.58 | blocked |
| Child is `Jose del Carmen Segundo Pulgar Arriagada`. | Hold. Literal in chunk/source packet, not in assigned converted Markdown. | 0.56 | blocked |
| Father is `Jose del Carmen Pulgar S.`. | Hold/revise after QA. Literal in chunk/source packet, but suffix/mark needs certification. | 0.50 | blocked |
| Mother is `Juana Arriagada de Pulgar`. | Hold. Literal in chunk/source packet, contradicted by converted Markdown. | 0.55 | blocked |
| Entry supports a Dario Pulgar identity bridge. | Reject for this source. No Dario name or relationship is present in the reviewed evidence. | 0.03 | blocked |

## Next Action

Run targeted conversion QA against the source image, assigned converted Markdown, assigned chunk, and source packet for `CHUNK-b8f4f0490a36-P0001-01`. QA should certify the controlling entry-172 row and explicitly state the father-field reading as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, rerun proof review before promoting any birth, parent, relationship, identity, or Dario-comparison claim.
