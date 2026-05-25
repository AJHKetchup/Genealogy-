---
type: proof_review
status: hold_for_conversion_qa
role: claim_reviewer
worker: postconv-proof-review-20260525225023906
task_id: proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260525211125251.md
staged_draft: research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260525211125251.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203741061.md
conflict_candidate: research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525203741061.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
canonical_readiness: not_ready
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

- The staged identity analysis is materially supported as a conflict note, but it is not promotion-ready because the assigned chunk and source packet conflict with the assigned converted Markdown for the same entry number.
- The chunk and source packet identify entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`; the converted Markdown identifies entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
- This is a row-level or file-assignment conflict between incompatible family groups, not a spelling or identity-variant conflict.
- The father field remains unresolved at transcription precision: `Jose del Carmen Pulgar S.` is plausible from the chunk, but targeted QA must confirm whether the suffix is `S.`, another mark, or uncertain.
- No Dario/Dario Arturo/Dario Jose identity is named in entry 172. Any Dario-line conclusion from this staged draft would be an unsupported relationship jump.

## Evidence Strengths

- The source is a civil birth registration image, a high-value record type for child, birth, and parent claims once the controlling row is certified.
- The assigned chunk, staged source packet, conflict candidate, and visible source image all support treating the Pulgar/Arriagada reading as a serious candidate for entry 172.
- The staged identity analysis correctly preserves the conflict rather than promoting the Pulgar/Arriagada identities, parent-child relationships, or any Dario-line bridge.
- The converted Markdown is internally complete, which is useful evidence of the conflict, but it appears to describe a different row/page context than the chunk and visible source image.

## Scored Judgment

| Score | Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.90 | Civil birth registration is strong primary evidence, but the proof value is blocked until the row assignment is certified. |
| conversion_confidence_score | 0.28 | The assigned converted Markdown and chunk disagree on child, parents, dates, places, occupations, and official context. |
| evidence_quantity_score | 0.62 | There is one source image plus multiple derivative/staged readings; quantity is moderate, but not independent enough to overcome the conversion conflict. |
| agreement_score | 0.40 | Chunk, source packet, conflict note, and image inspection lean Pulgar/Arriagada, while the converted Markdown directly contradicts them. |
| identity_confidence_score | 0.58 | The Pulgar/Arriagada identification is more likely than the Burgos/de la Cruz reading for this image, but the conflict prevents confident identity action. |
| claim_probability | 0.70 | Narrow claim probability: entry 172 probably corresponds to the Pulgar/Arriagada birth row. This is below promotion threshold because the derivative conversion conflict remains unresolved. |
| relevance_level | high | The row directly affects Pulgar/Arriagada child identity and parent-child relationships. |
| relevance_confidence | 0.88 | Relevance is clear if the Pulgar/Arriagada row controls; Dario relevance remains only anti-conflation context. |
| canonical_readiness | 0.10 | Not ready for canonical claims, relationships, people pages, family pages, or same-person merges. |

## Review Decision

Hold for conversion QA. The staged identity analysis is suitable as a conflict analysis and anti-conflation note, but not as canonical evidence. Do not promote child identity, birth event, parent relationship, same-person merge, or Dario-line bridge from this item.

## Next Action

Run targeted conversion QA against the source image, assigned converted Markdown, assigned chunk, and source packet. The QA note should certify the controlling row for register page 58 entry 172 and explicitly resolve the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, rerun proof review before any canonical promotion.
