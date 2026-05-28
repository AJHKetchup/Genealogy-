---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260528132455739
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525224308478.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260525224308478.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525215121005.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525215121005.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Do not promote the child identity, birth facts, parents, informant, or parent-child relationships while the current converted Markdown and current chunk disagree at the row level for entry 172.
2. Do not treat the Burgos/de la Cruz reading and the Pulgar/Arriagada reading as name variants or duplicate-person evidence. They describe different children, parents, birth dates, places, and informants.
3. Do not normalize the father name beyond the visible source support. The father field remains a literal-reading issue: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
4. Do not bridge this row to Dario, Arturo, Smith, Dario Jose, or later Pulgar-Arriagada public-role/person clusters. The reviewed row does not name those people or state a connecting relationship.
5. Canonical pages that already contain b8f4-derived evidence are dependent local context only, not independent proof for resolving this conversion conflict.

## Evidence Strengths

- The staged draft accurately reports the conflict between the current converted Markdown and the current chunk/source packet.
- The current chunk and source packet agree on a Pulgar/Arriagada reading for entry 172: `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, birth on 8 March 1888 at 3 p.m., and informant `Ernesto Herrera L.`.
- The current converted Markdown gives a coherent but different entry-172 reading: `José Miguel`, father/informant `Oswaldo Burgos`, mother `Concepcion de la Cruz`, birth on 6 April 1888 at 10 p.m.
- Limited visual verification of the referenced source image supports that the visible entry 172 row is a Pulgar/Arriagada row rather than the Burgos/de la Cruz row. This check supports the staged draft's row-control concern but does not replace targeted conversion QA.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 |
| conversion_confidence_score | 4/10 overall because derivative transcriptions conflict; 7/10 for the narrow observation that the visible image appears to support a Pulgar/Arriagada entry-172 row |
| evidence_quantity_score | 5/10 |
| agreement_score | 5/10 overall: chunk, source packet, and image agree against the current converted Markdown |
| identity_confidence_score | 6/10 for the Pulgar/Arriagada row as the likely visible entry; 2/10 or lower for any Dario/Arturo/Smith bridge |
| claim_probability | 0.75 that the visible source image supports the Pulgar/Arriagada entry-172 row; 0.20 that the current converted Markdown's Burgos/de la Cruz row is the controlling row for this source image; 0.05 or lower for any Dario identity bridge from this row alone |
| relevance_level | high |
| relevance_confidence | 0.90 |
| canonical_readiness | hold; not ready for canonical promotion until targeted conversion QA records the controlling row and father-name reading |

## Review Finding

The staged identity/conflict analysis is supported. It correctly treats the issue as a row-level conversion conflict and correctly blocks canonical promotion of the child identity, parent claims, parent-child relationships, and Pulgar-to-Dario bridge claims.

The only adjustment is evidentiary weight: visual inspection of the referenced source image gives additional support to the Pulgar/Arriagada row being the visible entry 172, but the converted Markdown remains contradictory. That contradiction should be fixed or formally resolved by conversion QA before any downstream claim is promoted.

## Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, current converted Markdown, current chunk, and source packet. The QA note should identify the controlling entry-172 row and certify the father field only to the visible level before any proof review promotes child, parent, informant, or relationship claims.
