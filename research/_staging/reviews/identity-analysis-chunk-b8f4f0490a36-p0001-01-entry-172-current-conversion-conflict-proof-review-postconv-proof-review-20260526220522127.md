---
type: proof_review
status: hold_for_conversion_qa
role: claim_reviewer
worker: postconv-proof-review-20260526220522127
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526173959405.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526173959405.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526170352337.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
created: 2026-05-26
source_quality_score: 0.82
conversion_confidence_score: 0.35
evidence_quantity_score: 0.62
agreement_score: 0.45
identity_confidence_score: 0.64
claim_probability: 0.66
relevance_level: high
relevance_confidence: 0.95
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Current Conversion Conflict

## Blockers First

1. Canonical promotion is blocked because the assigned chunk/source packet and the current converted Markdown attach different people and relationships to entry `172`.
2. The current converted Markdown reads entry `172` as `Jose Miguel`, son of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888 at about 10 p.m. in `En esta`.
3. The assigned chunk and staged source packet read entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, son of `Jose del Carmen Pulgar S.` or unresolved `Jose del Carmen Pulgar [?]` and `Juana Arriagada de Pulgar`, born 8 March 1888 at about 3 p.m. at `Calle de Valdivia`.
4. The father field cannot be proof-certified beyond the visible/source-reviewed uncertainty already stated in the packet: preserve `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` as unresolved alternatives until targeted conversion QA decides the reading.
5. No relationship, merge, identity bridge, or canonical page update involving Dario-name Pulgar clusters is supported by this entry alone.

## Review Judgment

The staged identity analysis is supported as a hold, not as a promotable proof conclusion. The local evidence establishes a material row-level conversion conflict for entry `172`. The source image view and assigned chunk favor the Pulgar/Arriagada row, but the canonical conversion file still contains the incompatible Burgos/de la Cruz row under the same entry number. Because the conversion artifacts disagree, this review should not promote child identity, birth event, parent-child relationships, or same-person conclusions.

## Evidence Strengths

- The source packet explicitly documents the conversion conflict and already marks promotion as `hold_for_conversion_qa`.
- The assigned chunk gives a full table row for entry `172` with child, sex, birth date/time/place, father, mother, informant, and official signature.
- The source image shows entry `172` on page 58 in the position described by the chunk and packet; the visible row is consistent with the Pulgar/Arriagada family reading.
- The competing converted Markdown reading is concrete and therefore reviewable: it names a different child, parent pair, birth date, birth place, and informant, making this a row-control problem rather than a spelling variant.

## Scoring

| Category | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil birth register image is a strong primary source, but the review relies on conversion artifacts for detail certification. |
| conversion_confidence_score | 0.35 | Low for canonical use because chunk/source packet and converted Markdown disagree on the entry-172 row. |
| evidence_quantity_score | 0.62 | Multiple local artifacts were available: staged draft, conflict draft, source packet, chunk, converted Markdown, and source image. They are not independent corroborating sources. |
| agreement_score | 0.45 | Source packet, chunk, and image review align broadly, but the current converted Markdown materially conflicts. |
| identity_confidence_score | 0.64 | Pulgar/Arriagada is the leading row identity, but not proof-level until conversion QA reconciles the file conflict. |
| claim_probability | 0.66 | Probable that entry `172` is the Pulgar/Arriagada birth row if the chunk/image row controls; not ready for canonical assertion. |
| relevance_level | high | Directly relevant to Pulgar/Arriagada identity and anti-conflation review. |
| relevance_confidence | 0.95 | The staged draft and source packet are explicitly about entry `172` and the Pulgar/Arriagada conflict. |
| canonical_readiness | hold_for_conversion_qa | Hold all dependent claims and relationships pending targeted conversion QA. |

## Risk Assessment

- Literal support risk: high if the current converted Markdown remains the authority for downstream extraction.
- Identity risk: high for conflating `Jose del Carmen Segundo Pulgar Arriagada` with unrelated `Jose Miguel`.
- Relationship jump risk: high for prematurely attaching parents because the two row readings name completely different parent pairs.
- Conflict severity: high; the conflict changes every genealogically meaningful field for the entry.
- Source reliability: strong primary image, but derivative conversion disagreement prevents proof-level certainty.
- Claim confidence: moderate for a hold judgment; insufficient for canonical promotion.

## Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, assigned chunk, source packet, and current converted Markdown. The QA note should decide which row controls entry `172` and certify the father field only to the visible extent. After that QA exists, rerun proof review before any canonical claim, relationship, merge, or wiki-page update.
