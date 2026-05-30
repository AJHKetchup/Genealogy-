---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260530043211284
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525210248504.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525210248504.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203040850.md"
reviewed_conflict_note: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-evidence-extraction-20260525203040850.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source_quality_score: 0.78
conversion_confidence_score: 0.30
evidence_quantity_score: 0.45
agreement_score: 0.35
identity_confidence_score: 0.56
claim_probability: 0.62
relevance_level: high
relevance_confidence: 0.82
canonical_readiness: hold_for_conversion_qa
created: 2026-05-30
---

# Proof Review: Entry 172 Row Conflict

This review covers the exact staged draft `research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525210248504.md`.

## Blockers First

1. Canonical readiness remains `hold_for_conversion_qa`. The cited chunk/source packet and cited converted Markdown assign materially different identities and parent sets to entry 172.
2. The cited chunk and source packet read entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`.
3. The cited converted Markdown reads entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. in `En esta`.
4. The source image paths recorded in the packet/manifest were not available in this workspace at review time, so this proof review cannot independently certify the visible row or father-field suffix from the image.
5. The staged draft's identity judgments must not be promoted into child identity, birth, parent-name, parent-child relationship, same-person, duplicate-person, or Dario-line bridge claims until row-control QA resolves the conflict.

## Evidence Strengths

- The staged draft accurately preserves the row-level conflict instead of normalizing it into a spelling variant or a same-person problem.
- The chunk, source packet, and conflict note agree with each other on the Pulgar/Arriagada reading and give a coherent civil birth-registration row.
- The converted Markdown gives a coherent but incompatible Burgos/de la Cruz row. This strengthens the conclusion that the problem is row assignment or conversion state, not a minor transcription disagreement.
- The source type, if correctly assigned, is a civil birth register and would normally be strong direct evidence for child name, birth facts, and parents. That evidentiary strength is currently limited by the unresolved conversion conflict.

## Scored Judgment

| Dimension | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.78 | Civil birth registration is high-quality direct evidence in principle, but this review could not inspect the unavailable source image. |
| conversion_confidence_score | 0.30 | The assigned converted file and assigned chunk disagree on child, parents, birth date/time/place, residence, and informant context. |
| evidence_quantity_score | 0.45 | The review has one cited record cluster with conflicting derivative representations, not multiple independent corroborating sources. |
| agreement_score | 0.35 | Chunk/source packet/conflict note agree with each other, but the converted Markdown materially conflicts. |
| identity_confidence_score | 0.56 | The Pulgar/Arriagada identity is plausible from the chunk/source packet but not certified because row control and the father suffix remain unresolved. |
| claim_probability | 0.62 | The staged draft's Pulgar/Arriagada row hypothesis is more likely than the converted Markdown for family relevance, but it is not promotion-ready without image-based QA. |
| relevance_level | high | Directly relevant to Pulgar/Arriagada parent candidates if the row is certified; only anti-conflation context for Dario identities. |
| relevance_confidence | 0.82 | The conflict is clearly relevant to whether this staged evidence can support Pulgar/Arriagada claims. |
| canonical_readiness | hold_for_conversion_qa | No canonical promotion or merge should proceed from this staged draft. |

## Identity And Relationship Risk

- Identity risk is high because two distinct child/parent clusters are competing for the same entry number.
- Relationship risk is high because promoting the Pulgar/Arriagada row would create parent-child assertions that the converted Markdown directly contradicts.
- The father field `Jose del Carmen Pulgar S.` must remain literal and unresolved; do not silently normalize it to `Jose del Carmen Pulgar`.
- No Dario identity bridge is supported here. The staged draft correctly treats any Dario-line comparison as anti-conflation context only.

## Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against an available source image/page asset, the assigned chunk, the assigned converted Markdown, and the staged source packet. The QA note should identify which row controls entry 172 and certify the father field only to the extent visible: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After that QA, rerun proof review before promoting any child identity, birth fact, parent-name claim, parent-child relationship, parent-pair clue, duplicate-person decision, same-person merge, or Dario-line attachment.
