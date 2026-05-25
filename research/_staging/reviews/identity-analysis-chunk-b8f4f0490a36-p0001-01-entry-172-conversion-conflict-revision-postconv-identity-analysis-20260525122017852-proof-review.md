---
type: proof_review
status: hold_for_conversion_qa
role: claim_reviewer
worker: postconv-proof-review-20260525171910923
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525122017852.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525122017852.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115651976.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Identity Conflict Analysis

## Blockers First

1. The staged identity analysis is supported as a conflict analysis, but not as a canonical claim package. The referenced converted Markdown and the referenced chunk assign different families to entry 172.
2. The converted file reads entry 172 as `Jose Francisco`, son of `Oswaldo Gomez` and `Rosario de la Cruz de la Maza`, born `veinte de Febrero` at `Pellin`; the source packet's conflict note instead says the converted Markdown reads mother `Emilia de la Cruz`, birth `veinte i seis de Marzo`, and place `En esta`. That mismatch within the conflict description itself needs cleanup in conversion QA or follow-up staging.
3. The referenced chunk and page image support the Pulgar/Arriagada row for entry 172, but the existence of a contradictory converted file means dependent identity, parent-child, and merge claims must remain held.
4. The father field should not be normalized beyond the visible/derivative support. The chunk reads `Jose del Carmen Pulgar S.`; the image appears consistent with a Pulgar father, but the final suffix/initial still warrants targeted field-level QA.
5. No relationship bridge to any Dario/Darío Pulgar candidate is present in this entry. Any Dario-line attachment would be a surname-pattern jump.

## Evidence Reviewed

- Staged draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525122017852.md`.
- Referenced conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525115651976.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115651976.md`.
- Chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Converted file: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Page image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Scored Judgment

| Metric | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth registration is a strong source class, and the page image is available for direct checking. |
| conversion_confidence_score | 0.38 | The converted file and chunk are materially inconsistent for entry 172; the chunk/image alignment improves confidence but does not resolve the derivative conflict. |
| evidence_quantity_score | 0.58 | One source image plus two derivative readings were reviewed; there is enough evidence to identify the conflict, not enough to promote relationships. |
| agreement_score | 0.42 | Chunk/source packet/page image broadly agree on Pulgar/Arriagada, but the converted file disagrees and the source packet misstates some converted-file details. |
| identity_confidence_score | 0.68 for Pulgar/Arriagada row; 0.04 for Dario-line attachment | Entry 172 appears to be the Pulgar/Arriagada row in the visible page/chunk, while no Dario identity evidence appears. |
| claim_probability | 0.66 | The staged conclusion that this is a row-level conversion conflict is well supported; the Pulgar/Arriagada identity is probable but held pending QA. |
| relevance_level | high | The entry directly concerns Pulgar/Arriagada parent-child candidates and anti-conflation with Pulgar-line identities. |
| relevance_confidence | 0.91 | If the chunk/image row is certified, the evidence is directly relevant; if not, it remains highly relevant as a conflict-control item. |
| canonical_readiness | hold_for_conversion_qa | Do not promote facts, relationships, person merges, or Dario comparisons until targeted conversion QA certifies the controlling row and father-field reading. |

## Evidence Strengths

- The page image and current chunk visibly and textually support entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`, with father read as `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- The staged identity analysis correctly treats the issue as a row-level conversion or assignment conflict rather than a spelling variant.
- The staged analysis correctly blocks Dario/Darío Pulgar attachment because the entry does not name Dario, Arturo, Smith, a spouse, child, later occupation, passenger record, or other bridging context.

## Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, chunk, and converted Markdown. The QA note should certify the controlling entry-172 row and explicitly record the father field ending after `Pulgar`; it should also reconcile the source packet's description of the converted-file row with the actual converted-file text.
