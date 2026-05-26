---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260526050206721
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526015109623.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526015109623.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526001440948.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: blocked
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

- Row-control blocker: the reviewed source image and assigned chunk show entry 172 on page 58 as the Pulgar/Arriagada birth row, while the reviewed converted Markdown presents entry 172 as a Burgos/de la Cruz row. This is a material conversion conflict affecting the child, parents, date, place, residence, informant, and all relationship claims.
- Conversion-confidence blocker: the staged identity-analysis draft correctly treats the Pulgar/Arriagada reading as probable but not canonically ready. The current converted file cannot be used as settled support for either row until targeted conversion QA reconciles it with the image and chunk.
- Father-field blocker: the image and staged materials support the visible start `Jose del Carmen Pulgar`; the trailing suffix/mark remains uncertain. Do not certify a fuller father name beyond `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` without targeted QA.
- Identity-risk blocker: this entry does not name Dario, Arturo, Smith, Pulgar-Smith, Dario Jose Pulgar-Arriagada, Dario J. Pulgar Arriagada, or Dario/Dario Pulgar Arriagada. Any bridge to those identities would be unsupported by this source alone.

## Evidence Strengths

- Source reliability is inherently strong: a contemporaneous civil birth register page is a high-value source for birth identity and parent-child relationships once the row transcription is controlled.
- The assigned chunk, source packet, and visual source check are mutually consistent that page 58 entry 172 is the Pulgar/Arriagada row.
- The staged draft accurately identifies the major contradiction with the converted Markdown and appropriately recommends `hold_for_conversion_qa` rather than promotion.
- The staged draft preserves uncertainty around the father suffix and avoids promoting a Dario-line relationship jump.

## Scored Judgment

| Metric | Score | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth register image is a strong source type, but current use is limited by row-control conflict. |
| conversion_confidence_score | 0.35 | The converted Markdown and assigned chunk materially disagree for entry 172. |
| evidence_quantity_score | 0.62 | One direct source image plus chunk and source packet; no independent corroborating record reviewed. |
| agreement_score | 0.55 | Image/chunk/source packet agree with each other, but converted Markdown conflicts completely. |
| identity_confidence_score | 0.66 | Pulgar/Arriagada identity is plausible for entry 172, but unresolved conversion control prevents firm identity certification. |
| claim_probability | 0.70 | More likely than not that the Pulgar/Arriagada row is the row needing certification for entry 172, but not ready as a canonical claim. |
| relevance_level | high | Directly relevant to Pulgar/Arriagada research and to anti-conflation around Dario-line candidates. |
| relevance_confidence | 0.90 | The relevant surnames and row-level conflict are explicit in the reviewed materials. |
| canonical_readiness | blocked | Hold pending targeted conversion QA; do not promote claims or relationships. |

## Claim-Level Review

| Claim or hypothesis | Support | Probability | Canonical readiness |
| --- | --- | ---: | --- |
| Entry 172 is the Pulgar/Arriagada birth row | Supported by reviewed image, assigned chunk, and source packet; contradicted by converted Markdown. | 0.70 | blocked |
| Entry 172 is the Burgos/de la Cruz birth row | Supported only by current converted Markdown; contradicted by reviewed image/chunk/source packet. | 0.18 | blocked |
| Jose del Carmen Segundo Pulgar Arriagada is child of Jose del Carmen Pulgar and Juana Arriagada de Pulgar | Conditionally supported if the Pulgar row is certified; father suffix remains uncertain. | 0.60 | blocked |
| Entry 172 bridges to Dario Arturo Pulgar-Smith or Dario Arturo Pulgar | No literal support in this source. | 0.05 | not_ready |
| Entry 172 person is same as a Dario Pulgar-Arriagada candidate | No shared given-name, date, parent, or event bridge in this reviewed source. | 0.03 | not_ready |

## Review Decision

The staged draft is supported as a cautionary identity-conflict analysis, not as a promotable claim package. Its `hold_for_conversion_qa` recommendation and `canonical_readiness: blocked` status should stand.

## Next Action

Run targeted conversion QA for the source image, assigned chunk, and converted Markdown. The QA task should certify which row controls entry 172 and should separately certify the father field only to the visible extent. After QA, rerun proof review before any child identity, birth fact, parent-child relationship, parent merge, or Dario-line comparison is promoted.
