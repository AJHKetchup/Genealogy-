---
type: proof_review
status: hold_for_conversion_qa
role: claim_reviewer
worker: postconv-proof-review-20260525225858229
task_id: proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260525211125251.md
staged_draft: research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260525211125251.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203741061.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
canonical_readiness: not_ready
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

- The staged identity analysis is materially supported as a conflict analysis, but it is not ready for canonical promotion because the assigned converted Markdown contradicts the assigned chunk, source packet, and visible page image for the same entry number.
- The assigned chunk and source packet identify entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`; the assigned converted Markdown identifies entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
- This is a row-level conversion or file-assignment conflict between incompatible family clusters, not a name-variant conflict.
- The visible source image supports the Pulgar/Arriagada row for page 58 entry 172, but this review does not edit the converted Markdown or certify a corrected transcription.
- The father field still needs targeted transcription QA to decide whether the final element reads `S.`, another mark, or should remain uncertain.
- Entry 172 does not name Dario, Dario Arturo, Dario Jose, Darío J., Smith, or any direct Dario-line bridge. Any Dario-line use should remain anti-conflation context only.

## Evidence Strengths

- The underlying source is a civil birth registration image, a strong primary-source type for child identity, birth details, and stated parents once the controlling row is certified.
- The assigned chunk, staged source packet, and visible page image agree on the Pulgar/Arriagada family cluster for register page 58 entry 172.
- The staged identity analysis correctly preserves the conflict and recommends `hold_for_conversion_qa` rather than promoting a child identity, parent-child relationship, same-person merge, or Dario-line bridge.
- The converted Markdown is useful as conflict evidence because it gives a complete but incompatible Burgos/de la Cruz row under the same assigned entry number.

## Scored Judgment

| Score | Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.90 | Civil birth registration is strong primary evidence, but its canonical proof value is blocked until the row assignment and father field are certified. |
| conversion_confidence_score | 0.30 | The assigned converted Markdown conflicts with the chunk/source-packet/image reading on child, parents, dates, places, and family cluster. |
| evidence_quantity_score | 0.64 | There is one source image and several derivative/staged readings; useful but not independent enough to resolve the conversion conflict alone. |
| agreement_score | 0.42 | Chunk, source packet, and visible image agree on Pulgar/Arriagada, while the converted Markdown directly disagrees. |
| identity_confidence_score | 0.60 | The Pulgar/Arriagada reading is the better-supported identity for the visible image, but identity action remains blocked by the converted-file conflict. |
| claim_probability | 0.72 | Narrow probability that the controlling visible row is the Pulgar/Arriagada birth is probable, not promotion-ready. |
| relevance_level | high | The item directly affects Pulgar/Arriagada identity and parent-child relationship claims. |
| relevance_confidence | 0.88 | Relevance is clear for Pulgar/Arriagada sorting; Dario relevance is only negative/anti-conflation context. |
| canonical_readiness | 0.10 | Not ready for canonical claims, relationships, people pages, family pages, or same-person merges. |

## Review Decision

Hold for conversion QA. The staged draft is acceptable as a conflict analysis, but it must not be promoted as canonical evidence while the assigned converted Markdown remains incompatible with the chunk/source-packet/image reading.

## Next Action

Run targeted conversion QA against the source image, assigned converted Markdown, assigned chunk, and staged source packet. The QA note should certify the controlling row for page 58 entry 172 and explicitly record the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. Rerun proof review after QA before any canonical promotion.
