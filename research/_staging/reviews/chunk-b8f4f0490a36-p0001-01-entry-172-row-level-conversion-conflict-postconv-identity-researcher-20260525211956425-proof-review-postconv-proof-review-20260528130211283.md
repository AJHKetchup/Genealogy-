---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260528130211283
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525211956425.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525211956425.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525203741061.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203741061.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Do not promote any child identity, birth event, parent-child relationship, or parent identity merge from this staged draft until conversion QA resolves the row-control conflict.
2. The referenced converted Markdown identifies entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, while the referenced chunk and source packet identify entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`.
3. The visible page image supports the Pulgar/Arriagada row for entry 172, but this proof review does not correct the converted Markdown or replace the conversion layer.
4. The father field has residual paleography risk. It visibly supports `Jose del Carmen Pulgar` plus a trailing mark or suffix, but whether the literal field should be `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` still needs targeted conversion QA.
5. No reviewed source text names Dario, Arturo, Smith, Dario Jose, or Darío/Dario Pulgar Arriagada. Any Dario-line bridge remains unsupported.

## Evidence Strengths

- The source is a contemporary civil birth register image for Los Angeles, Chile, 1888, and is directly relevant to entry 172.
- The chunk and source packet agree on the Pulgar/Arriagada child, registration date, birth date, birth place, parents, and informant.
- The page image visibly aligns entry number `172` with the Pulgar/Arriagada row on page 58, not with the Burgos/de la Cruz row from the converted Markdown.
- The staged identity analysis correctly treats this as a row-level conversion conflict rather than a name variant or same-person problem.
- The staged identity analysis correctly blocks canonical edits and Dario-line comparison claims.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 |
| conversion_confidence_score | 3/10 overall because the assigned converted Markdown conflicts with the chunk and source image; 7/10 for the chunk's narrow Pulgar/Arriagada row reading except the father suffix |
| evidence_quantity_score | 4/10 |
| agreement_score | 6/10 overall: chunk, source packet, and image agree, but converted Markdown materially disagrees |
| identity_confidence_score | 7/10 for the narrow existence of an entry-172 Pulgar/Arriagada birth row; 3/10 for linking the father to any canonical `Jose del Carmen Pulgar` page; 0.5/10 for any Dario-line bridge |
| claim_probability | 0.88 that the visible source image for entry 172 records `Jose del Carmen Segundo Pulgar Arriagada` with parents in the Pulgar/Arriagada cluster; 0.35 that the father should be promoted as the existing canonical `Jose del Carmen Pulgar`; 0.02 that this entry supports a Dario-line identity |
| relevance_level | high for Pulgar/Arriagada birth and parent-candidate research; low for Dario-line identity claims |
| relevance_confidence | 0.90 for Pulgar/Arriagada relevance; 0.20 for Dario-line relevance |
| canonical_readiness | hold_for_conversion_qa |

## Review Finding

The staged draft is supported as a hold. It accurately identifies the controlling risk: derivative conversion layers disagree about the entire entry-172 row. Visual review of the source image increases confidence that the Pulgar/Arriagada row is the relevant row, but the converted Markdown remains an unresolved contradictory derivative source and must not be silently overridden in this review.

The only source-supported narrow direction is: entry 172 appears to concern `Jose del Carmen Segundo Pulgar Arriagada`, with parent fields for `Jose del Carmen Pulgar` plus an unresolved suffix/mark and `Juana Arriagada de Pulgar`. This is not yet canonically ready because the conversion conflict and father-field uncertainty remain open.

## Next Action

Run targeted conversion QA for page 58, entry 172 against the source image, converted Markdown, chunk, and source packet. The QA note should decide the controlling row and certify the father field before any claim promotion, relationship promotion, identity merge, wiki update, or Dario-line comparison.
