---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530092229781
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526013245826.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526013245826.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526001440948.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526001440948.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. The source image path recorded in the staged materials could not be resolved locally during this proof review. The review therefore cannot independently certify the visible handwriting or the row image; it can only compare the staged draft, source packet, assigned chunk, conflict note, and current converted Markdown.
2. The assigned chunk and source packet read entry 172 as the Pulgar/Arriagada birth row, while the current converted Markdown reads entry 172 as a Burgos/de la Cruz birth row. This is a controlling-row conflict affecting the child, parents, birth date, birth place, informant, and residences.
3. No child identity, parent-child relationship, parent merge, Juana-name merge, or Dario-line bridge is canonical-ready from this staged draft.
4. The father field in the Pulgar/Arriagada reading remains uncertified beyond the staged alternatives: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

## Evidence Strengths

- The staged draft accurately reports the conflict between the assigned chunk/source packet and the current converted Markdown.
- The assigned chunk is internally coherent for a civil birth registration: entry 172, registration date 7 April 1888, child `Jose del Carmen Segundo Pulgar Arriagada`, male, birth 8 March 1888 at 3 p.m. at `Calle de Valdivia`, father read as `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The source packet explicitly says a visual image review supported the Pulgar/Arriagada row and not the Burgos/de la Cruz row, while preserving uncertainty on the father's trailing suffix or mark.
- The current converted Markdown is also internally coherent but describes a materially different row: child `Jose Miguel`, born 6 April 1888 at about 10 p.m. in `En esta`, father and informant `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
- The staged draft appropriately treats Dario, Arturo, Smith, Dario Jose, and Dario Pulgar Arriagada links as unsupported because none of those names or bridge relationships appear in either entry-172 reading.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 for the underlying civil birth register type; 4/10 for this review pass because the source image was unavailable for direct verification |
| conversion_confidence_score | 3/10 overall because the assigned chunk and current converted Markdown disagree on the controlling row; 6/10 for the Pulgar/Arriagada row as staged packet evidence; 2/10 for treating the Burgos/de la Cruz conversion as controlling for this task |
| evidence_quantity_score | 4/10: one civil-registration entry candidate plus conflicting conversion artifacts, with no independent bridge source |
| agreement_score | 3/10 overall; 8/10 between staged draft, source packet, conflict note, and assigned chunk for the existence of a row-control conflict; 1/10 between the assigned chunk and converted Markdown for the actual entry-172 facts |
| identity_confidence_score | 5/10 for a possible `Jose del Carmen Segundo Pulgar Arriagada` birth-row identity pending image QA; 2/10 for any merge to an existing `Jose del Carmen Pulgar` father stub; 0.5/10 for any Dario-line attachment |
| claim_probability | 0.60 that the assigned row for this task is the Pulgar/Arriagada row; 0.20 that the current Burgos/de la Cruz converted text is the controlling row for this task; 0.05 or lower for any Dario-line bridge |
| relevance_level | high for the Pulgar/Arriagada family if row control is confirmed; low for Dario-line attachment at this stage |
| relevance_confidence | 0.80 for family relevance under the Pulgar/Arriagada hypothesis; 0.15 for Dario-line relevance |
| canonical_readiness | hold_for_conversion_qa |

## Review Finding

The staged identity analysis is supported as a hold. It does not over-promote the conflict and correctly identifies this as a row-control and conversion-confidence problem rather than a ready identity conclusion.

Literal support is present in the assigned chunk and source packet for a Pulgar/Arriagada entry-172 reading, but that support is not enough for canonical promotion because the current converted Markdown records a different entry-172 row and the source image was not available to this reviewer for direct handwriting verification. The Burgos/de la Cruz reading should also not be promoted from this task because it conflicts with the assigned chunk, source packet, and staged conflict note.

## Next Action

Keep the staged draft on `hold_for_conversion_qa`. The next action is targeted source-image row-control QA for page 58, entry 172, using an available page image or recovered source image. That QA must decide whether entry 172 is the Pulgar/Arriagada row or the Burgos/de la Cruz row and must certify the father's visible field only to the supported extent before any proof review or canonical claim promotion is rerun.
