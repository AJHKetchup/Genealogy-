---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260530091835235
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526013245826.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526013245826.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526001440948.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
page_markdown: "raw/codex-conversion-jobs/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172/page-markdown/page-0001.md"
source: "raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; entry 172"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers

- The raw source image referenced by the staged draft, source packet, chunk, converted Markdown, and manifest was not available at `raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png` during review. The manifest also references `page-images/page-0001.png`, but that file is not present in the conversion job folder. I therefore cannot independently certify the visible handwriting from the image.
- The available conversion artifacts materially conflict on the same entry number. The chunk reads entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`; the converted file and page Markdown read entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
- Because the source image is unavailable and the conversion artifacts disagree, the father-field reading cannot be proof-certified as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or another variant.
- No child identity, parent-child relationship, parent merge, Juana-name merge, birth-event claim, or Dario-line comparison is canonical-ready from this review.

## Evidence Strengths

- The staged draft correctly identifies the controlling issue as a row-level conversion conflict, not a normal identity merge or surname variant question.
- The source packet and chunk agree with each other on the Pulgar/Arriagada reading for entry 172 and preserve useful candidate details for later QA: child name, birth date and place, parents, residences, and informant.
- The converted file and conversion job page Markdown agree with each other on a different Burgos/de la Cruz reading, which makes the conflict concrete and reproducible from local text artifacts.
- The staged draft appropriately keeps Dario-related conclusions blocked; the available local artifacts for this entry do not name Dario, Arturo, Smith, or a descendant bridge.

## Scores

| item | score |
| --- | ---: |
| source_quality_score | 0.70 |
| conversion_confidence_score | 0.25 |
| evidence_quantity_score | 0.45 |
| agreement_score | 0.20 |
| identity_confidence_score | 0.25 |
| claim_probability | 0.40 |
| relevance_level | high_if_pulgar_row_certified |
| relevance_confidence | 0.60 |
| canonical_readiness | hold_for_conversion_qa |

## Claim Probability Assessment

- Pulgar/Arriagada entry-172 reading: 0.55 probability based on agreement between the chunk and source packet, reduced because the image was unavailable and the converted/page Markdown disagree.
- Burgos/de la Cruz entry-172 reading: 0.35 probability based on agreement between the converted file and page Markdown, reduced because a later source packet claims image review contradicted it.
- Any canonical parent-child claim involving `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar`: 0.25 probability for promotion readiness, because the row-control problem blocks proof use.
- Any Dario-line attachment from this source: 0.02 probability; the reviewed artifacts provide no direct Dario identity bridge.

## Next Action

Keep the staged draft on `hold_for_conversion_qa`. Restore or locate the exact source/page image with SHA-256 `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2`, then perform targeted conversion QA for register page 58, entry 172. After QA certifies the controlling row and father-field reading, rerun proof review before any canonical promotion or identity merge.
