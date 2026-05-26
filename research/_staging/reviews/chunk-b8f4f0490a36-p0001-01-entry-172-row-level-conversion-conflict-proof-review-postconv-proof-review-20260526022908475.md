---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260526022908475
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260526013800320.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260526013800320.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526001440948.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
created: "2026-05-26"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Row-control conflict remains material. The chunk, source packet, and visible page image support entry 172 as a Pulgar/Arriagada row, while the referenced converted Markdown records entry 172 as a Burgos/de la Cruz row.
2. The converted Markdown cannot be used as a stable controlling transcription for entry 172 until targeted conversion QA reconciles it with the chunk and page image.
3. The father field is partly supported as beginning `Jose del Carmen Pulgar`, but the trailing mark or suffix is not proof-reviewed enough here to promote `S.` as a final reading.
4. The draft correctly blocks Dario-line attachment. The source evidence reviewed here does not identify the child as Dario, Arturo, Smith, or any Dario candidate.
5. Parent-identity merges remain blocked. This source may later support a Pulgar/Arriagada child-parent claim, but it does not prove that any existing Jose/Juana clusters are duplicates.

## Evidence Strengths

- The source type is strong: a civil birth register page for Los Angeles, Chile, with entry numbers, registration dates, child names, birth details, parent fields, informant fields, and official signatures.
- The source packet accurately flags a conversion conflict and recommends `hold_for_conversion_qa`.
- The assigned chunk reads entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at about 3 p.m. at Calle de Valdivia, with father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`
- Visual review of the page image supports the chunk/source-packet row identity over the converted Markdown's Burgos/de la Cruz row.
- The staged identity analysis preserves uncertainty and avoids promoting the Pulgar/Arriagada facts, Dario comparison, or parent merges.

## Scored Judgment

| Metric | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth registration is high-quality direct evidence for a birth row, though this review used a page image and derivative files rather than a fresh archival citation audit. |
| conversion_confidence_score | 0.42 | The assigned chunk and image agree at row level, but the canonical converted Markdown materially contradicts them. |
| evidence_quantity_score | 0.70 | One direct register page plus chunk and source packet; enough for row-control review, not enough for broader identity merges. |
| agreement_score | 0.58 | Chunk, source packet, and visible image agree broadly; converted Markdown disagrees completely on entry 172. |
| identity_confidence_score | 0.72 | Probable that the row names `Jose del Carmen Segundo Pulgar Arriagada`, reduced for father-suffix uncertainty and unresolved conversion conflict. |
| claim_probability | 0.74 | The Pulgar/Arriagada row is the more probable reading for entry 172 on current evidence, but it remains held pending conversion QA. |
| relevance_level | 0.90 | Directly relevant to Pulgar/Arriagada birth and parentage analysis; relevant to Dario only as an anti-conflation check. |
| relevance_confidence | 0.86 | The names and parent fields make family relevance clear if the row is certified. |
| canonical_readiness | 0.10 | Hold; not ready for canonical claims, relationships, merges, or Dario attachments until targeted conversion QA is complete. |

## Claim-Level Review

| Claim Or Hypothesis | Support | Probability | Canonical Readiness |
| --- | --- | ---: | --- |
| Entry 172 is the Pulgar/Arriagada birth row | Supported by chunk, source packet, and visible image; contradicted by converted Markdown | 0.74 | Hold |
| Father can be promoted as `Jose del Carmen Pulgar S.` | Partly supported, but suffix is not secure enough in this review | 0.58 | Hold |
| Mother is `Juana Arriagada de Pulgar` if the row controls | Supported by chunk and visible row context | 0.76 | Hold |
| Converted Markdown Burgos/de la Cruz row controls entry 172 | Supported only by converted Markdown and contradicted by chunk/source packet/image | 0.16 | Hold/Revise after QA |
| Entry-172 child is the same person as a Dario candidate | No direct source support; given names conflict with Dario hypothesis | 0.05 | Not ready |
| Jose/Juana parent candidates are duplicate identities | Name-context question only; no proof bridge in this source | 0.28 | Not ready |

## Source Reliability And Conversion Notes

- The page image is readable enough to verify the row-control issue at a high level.
- The chunk appears to be a corrected or alternate conversion aligned with the visible image.
- The converted Markdown appears to describe a different set of rows for entries 171-176 and should be treated as unreliable for entry 172 until QA explains the mismatch.
- This proof review does not alter transcription text and does not certify the father's suffix beyond the visibly supported start `Jose del Carmen Pulgar`.

## Identity And Relationship Risk

- Identity risk is high if this source is attached to Dario candidates because the entry does not name Dario.
- Relationship risk is high if parent-child relationships are promoted before row-control QA because the current converted Markdown names an entirely different child-parent set.
- Parent-merge risk is moderate to high because similar Jose/Juana/Pulgar/Arriagada names could invite unsupported consolidation across clusters.

## Next Action

Run targeted conversion QA on the source image, converted Markdown, and chunk to certify the controlling row for entry 172 and the father field reading. After that, rerun proof review for the child identity, birth facts, parent names, informant, and any parent-cluster comparison. Do not promote this staged draft to canonical claims or relationships in its current state.
