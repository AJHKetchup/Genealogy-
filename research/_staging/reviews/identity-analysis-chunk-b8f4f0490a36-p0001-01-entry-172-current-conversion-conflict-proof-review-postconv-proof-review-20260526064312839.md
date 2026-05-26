---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260526064312839
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

1. The staged draft is supported as a conflict analysis, but it is not proof-ready for canonical promotion because the referenced chunk and current converted Markdown assign entry 172 to different children, parents, dates, places, and informants.
2. The current converted Markdown records entry 172 as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, while the chunk/source packet record entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`.
3. A visual spot check of the source image appears to favor the chunk/source-packet row for entry 172, but this proof review is not a targeted conversion-QA certification. The father field and full row reading should remain unpromoted until QA explicitly certifies them.
4. No Dario-line bridge is supported by this source. The record under review does not name Dario, Arturo, Smith, Alexander John Heinz, or any grandparent relationship.
5. Existing same-cluster canonical wiki context cannot be treated as independent corroboration for this task.

## Evidence Strengths

- The staged identity analysis accurately describes the controlling row-level conflict and keeps the recommendation at `hold_for_conversion_qa`.
- The source packet, conflict candidate, and chunk agree internally on the Pulgar/Arriagada reading for entry 172.
- The current converted Markdown provides the material contradiction that justifies a hold rather than a promotion.
- The source image is available and visibly shows entry 172 on page 58; at review scale, it broadly aligns with the Pulgar/Arriagada row described in the chunk, which raises the probability that the current converted Markdown is attached to or transcribing the wrong row/page context.

## Scored Judgment

| Score field | Score | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.82 | Civil birth registration image is a strong primary source, but this review relies partly on derivative transcriptions and a spot check rather than full conversion QA. |
| conversion_confidence_score | 0.35 | The chunk and source image appear stronger than the converted Markdown, but the file-level conversion conflict remains unresolved. |
| evidence_quantity_score | 0.58 | There is one source image plus two conflicting derivative readings. Quantity is enough to identify the conflict, not enough to promote claims. |
| agreement_score | 0.42 | Chunk/source packet/conflict draft agree with each other, but the converted Markdown materially disagrees. |
| identity_confidence_score | 0.60 | The Pulgar/Arriagada identity is the better current hypothesis, but the unresolved conversion conflict prevents high confidence. |
| claim_probability | 0.64 | Probability that entry 172 is the Pulgar/Arriagada row, based on internal agreement and visual spot check, remains below proof-ready because QA has not certified the row. |
| relevance_level | high | Directly relevant to Pulgar/Arriagada identity and parent-child claims; only anti-conflation relevance for any Dario-line work. |
| relevance_confidence | 0.88 | Family names in the chunk and source packet make the relevance clear if the row is certified. |
| canonical_readiness | 0.10 | Hold for conversion QA. Do not promote child identity, birth facts, parent names, parent-child links, merges, or Dario bridges. |

## Claim-Level Review

| Claim or hypothesis | Support | Probability | Readiness |
| --- | --- | ---: | --- |
| Entry 172 is for `Jose del Carmen Segundo Pulgar Arriagada`. | Supported by chunk and source packet; visually plausible from source image. Contradicted by converted Markdown. | 0.64 | Hold |
| Father is `Jose del Carmen Pulgar S.`. | Supported by chunk/source packet, but the staged draft correctly flags the suffix/father field for QA certification. | 0.58 | Hold |
| Mother is `Juana Arriagada de Pulgar`. | Supported by chunk/source packet and visually plausible; contradicted by converted Markdown mother field. | 0.62 | Hold |
| Entry 172 is for `Jose Miguel`, child of Burgos/de la Cruz. | Supported only by current converted Markdown among reviewed materials; contradicted by chunk/source packet and source-image spot check. | 0.24 | Hold/revise after QA |
| This source bridges to a Dario identity. | No literal support in the reviewed source set. | 0.03 | Reject for current task |

## Source Reliability And Identity Risk

- Source reliability is high at the image level because the underlying item is a civil registration image.
- Derivative reliability is split. The chunk appears more consistent with the visible source image, while the converted Markdown appears materially inconsistent with both the chunk and source packet.
- Identity risk is high if any parent-child relationship is promoted before QA, because the two readings imply mutually exclusive families.
- Relationship-jump risk is high for same-name merges involving `Jose del Carmen Pulgar` or Juana variants.
- Dario-line conflation risk is high if surname context is overused, but direct Dario relevance is low.

## Next Action

Run targeted conversion QA against the source image, current converted Markdown, assigned chunk, and source packet. The QA note should decide the controlling entry-172 row and specifically certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, rerun proof review for the child identity, birth date, birth place, father claim, mother claim, informant claim, and parent-child relationships. No canonical promotion should occur from this staged draft before that renewed proof review.
