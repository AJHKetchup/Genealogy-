---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260525194426729
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525122915316.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525122915316.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115123585.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Conversion Conflict

## Blockers First

- Canonical readiness is `hold_for_conversion_qa`. The staged identity analysis depends on a material row-level conflict: the assigned chunk and visible source image support entry 172 as a Pulgar/Arriagada birth registration, while the assigned converted Markdown records entry 172 as a different child-parent cluster.
- The assigned converted Markdown cannot be used as literal support for the Pulgar/Arriagada claims in its current state. It records entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. in `En esta`; the staged draft describes a closely related Gomez/de la Cruz conflict reading, but the current converted file read during this review is Burgos/de la Cruz.
- The father field in the Pulgar/Arriagada row remains unresolved for canonical naming. The chunk reads `Jose del Carmen Pulgar S.`, while the image is compatible with `Jose del Carmen Pulgar` plus an uncertain or abbreviated ending; this should not be normalized without targeted conversion QA.
- No Dario identity, Dario relationship, or Dario-line bridge is supported by this entry. The reviewed row names Jose del Carmen Segundo Pulgar Arriagada if the Pulgar row controls; surname overlap alone is not proof.
- Do not merge `Juana Arriagada de Pulgar` with `Juana de Dios Amagada de Pulgar` or any other Juana candidate from this draft alone.

## Evidence Scores

| Score | Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth register image is a direct source for the registration, and the page image is present and legible enough for the main row identity. |
| conversion_confidence_score | 0.42 | The assigned chunk aligns with the visible Pulgar/Arriagada row, but the assigned converted Markdown transcribes a different entry 172 row. |
| evidence_quantity_score | 0.58 | Evidence includes staged draft, source packet, converted Markdown, chunk, and source image, but only one source page is involved and derivatives conflict. |
| agreement_score | 0.48 | Source image, chunk, and source packet agree on the Pulgar/Arriagada cluster; the converted Markdown disagrees materially. |
| identity_confidence_score | 0.70 | Probable identity if the image/chunk row controls, but not proof-ready until the derivative assignment conflict is resolved. |
| claim_probability | 0.72 | The visible source and chunk probably support entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, child of Jose del Carmen Pulgar/Pulgar S. and Juana Arriagada de Pulgar. |
| relevance_level | high | The reviewed materials directly concern page 58, entry 172 and the staged identity-conflict analysis. |
| relevance_confidence | 0.96 | The draft, source packet, chunk, converted file, and source image all point to the same assigned source package and entry number. |
| canonical_readiness | hold_for_conversion_qa | A controlling conversion/row-assignment conflict and father-name suffix uncertainty block promotion. |

## Evidence Strengths

- The visible source image shows page 58, entry 172 in the left-page middle row and supports the Pulgar/Arriagada row at the level of child name, parents, residence, informant, and registration context.
- The assigned chunk gives a coherent full-row transcription for entry 172: `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, parents at `Calle de Colipi`, and informant `Ernesto Herrera L.`
- The source packet accurately preserves the core proof problem: family-relevant Pulgar/Arriagada evidence exists, but the derivative conversion set is internally inconsistent.
- The staged identity analysis is appropriately cautious on Dario-line anti-conflation and does not promote surname-context relationships as proof.

## Review Judgment

The staged draft is supportable as a conflict-aware identity analysis, but it should remain in staging. The strongest current reading is that the source image and chunk probably identify entry 172 as the Pulgar/Arriagada birth registration. That is a probability judgment only. The assigned converted Markdown currently carries a different entry 172 transcription, and the father suffix after `Pulgar` is still not certified.

Claim support is therefore `hold`, not canonical. Child identity, birth facts, parent-child relationships, parent identity candidates, and any Dario-line comparison should wait for targeted conversion QA.

## Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, assigned converted Markdown, assigned chunk, and source packet. The QA note should decide whether the controlling source row for page 58, entry 172 is the Pulgar/Arriagada row or whether the converted Markdown/chunk assignment must be superseded, and it should certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, rerun proof review before promoting any canonical claim, relationship, person page update, or parent merge.
