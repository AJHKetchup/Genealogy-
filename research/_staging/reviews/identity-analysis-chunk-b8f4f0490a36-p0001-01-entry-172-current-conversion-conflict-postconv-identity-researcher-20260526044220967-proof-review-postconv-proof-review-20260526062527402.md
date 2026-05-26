---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260526062527402
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526044220967.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-researcher-20260526044220967.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526020438864.md"
reviewed_conflict_candidate: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526020438864.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Current Conversion Conflict

## Blockers First

1. The staged draft is correctly blocked from canonical promotion because the referenced chunk and the referenced converted Markdown disagree at the row level for entry 172.
2. The chunk/source packet identify entry 172 as a Pulgar/Arriagada birth registration, while the converted Markdown identifies entry 172 as a Burgos/de la Cruz birth registration. This is not a spelling or normalization issue; it changes the child, birth event, parents, residence, and informant.
3. The source image, at review resolution, supports the broad Pulgar/Arriagada placement for entry 172 on page 58, but this proof review is not a full conversion-QA recertification. The father-field detail, especially whether the terminal mark is `S.` or should remain uncertain, still needs targeted QA.
4. No Dario/Darío identity or relationship claim is source-supported by this entry. Any Dario-line use must remain anti-conflation context only.
5. Canonical pages or earlier same-cluster notes must not be used as independent corroboration for this draft because the controlling transcription conflict remains unresolved.

## Evidence Strengths

- The staged draft accurately reports the core conflict between the chunk/source-packet reading and the converted-file reading.
- The referenced chunk gives a coherent row for entry 172: child `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`, birth date `Ocho de Marzo de mil ochocientos ochenta i ocho`, place `Calle de Valdivia`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`
- The referenced source packet explicitly flags low conversion confidence and recommends holding for targeted conversion QA.
- The referenced source image visually aligns with the chunk at the broad row level for entry 172: the entry appears to name `Jose del Carmen Segundo Pulgar Arriagada` and the parent area appears to include `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.
- The staged draft appropriately resists a parent merge, Dario-line bridge, or canonical relationship promotion from this disputed source cluster.

## Evidence And Probability Scoring

| Metric | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.78 | Civil birth registration image is a high-value original/near-original source for a birth event, but this review used it only for limited visual verification. |
| conversion_confidence_score | 0.42 | Chunk and image broadly agree, but the converted Markdown contradicts the same entry and the father-field suffix remains uncertified. |
| evidence_quantity_score | 0.46 | One source image plus two conflicting derivative transcriptions; no independent corroborating source was reviewed or needed for this task. |
| agreement_score | 0.35 | Chunk/source packet/source image broadly agree against the converted Markdown, but the official converted file remains materially inconsistent. |
| identity_confidence_score | 0.62 | The Pulgar/Arriagada child reading is the better-supported local hypothesis, but not proof-ready until QA resolves the conversion conflict. |
| claim_probability | 0.64 | Probable that entry 172 is the Pulgar/Arriagada registration, not the Burgos/de la Cruz row, based on the chunk and image; still below canonical threshold because the conversion conflict is unresolved. |
| relevance_level | high | Directly relevant to Pulgar/Arriagada identity and parent-child claims; only minimally relevant to Dario-line work. |
| relevance_confidence | 0.86 | Family terms and visible row content make the Pulgar/Arriagada relevance clear if the row is certified. |
| canonical_readiness | hold_for_conversion_qa | Do not promote child identity, birth facts, parent names, parent-child relationships, or merges from this draft. |

## Claim Review

| Claim or hypothesis | Review judgment | Probability | Notes |
| --- | --- | ---: | --- |
| Entry 172 is `Jose del Carmen Segundo Pulgar Arriagada` | hold pending QA | 0.64 | Supported by chunk and broadly by image; contradicted by converted Markdown. |
| Father is `Jose del Carmen Pulgar S.` | revise/hold pending QA | 0.55 | The name `Jose del Carmen Pulgar` is broadly supported; the suffix/terminal mark needs targeted image QA. |
| Mother is `Juana Arriagada de Pulgar` | hold pending QA | 0.66 | Supported by chunk and broadly visible in the source image; blocked by converted-file conflict. |
| Entry 172 is `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz` | likely conversion mismatch | 0.18 | Present in converted Markdown, but not supported by the viewed entry-172 row in the referenced source image. |
| This entry supports any Dario/Darío Pulgar identity bridge | not supported | 0.03 | No Dario/Darío name or bridging relationship appears in the reviewed entry. |

## Next Action

Run targeted conversion QA against the source image, chunk, and converted Markdown. QA should decide the controlling entry-172 row and explicitly certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, rerun proof review before any canonical identity, birth fact, parent-child relationship, parent merge, or Dario-line bridge is promoted.
