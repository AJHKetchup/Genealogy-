---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260530013330869
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-postconv-identity-analysis-20260525123339261.md
staged_draft: research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-postconv-identity-analysis-20260525123339261.md
reviewed_converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
reviewed_chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
reviewed_source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115123585.md
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Identity Conflict

## Blockers First

- Canonical readiness remains `hold_for_conversion_qa`. The reviewed converted/page Markdown and the reviewed chunk cannot both be literal transcriptions of the same controlling entry 172 row.
- The source image named in the staged draft, converted file, chunk, source packet, and manifest was not available at `raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png`, and the manifest-referenced page image under the conversion job was also unavailable. This review therefore cannot certify the visible handwriting.
- The staged draft accurately identifies a material row-level conflict, but it misstates the converted file currently on disk. The converted/page Markdown reviewed here reads entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born `El seis de Abril de mil ochocientos ochenta i ocho` at `En esta`; it does not read `Jose Francisco`, `Oswaldo Gomez`, `Emilia de la Cruz`, or `veinte i seis de Marzo`.
- The current chunk and source packet read entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde` at `Calle de Valdivia`.
- Because the visible source image is unavailable and the derivative files disagree, no child identity, parent relationship, father-name suffix, merge candidate, or Dario-line attachment should be promoted from this staged draft.

## Evidence Strengths

- The reviewed chunk and reviewed source packet agree with each other on the Pulgar/Arriagada reading for entry 172.
- The reviewed converted Markdown and its page-level conversion job Markdown agree with each other on a non-Pulgar entry 172 reading.
- The record type, if the correct row is later confirmed, is a civil birth registration and would be a strong source for birth identity and parent relationship claims.
- The staged draft's main caution is supportable: this is a severe row-level conversion or assignment conflict, not a spelling variant.
- The staged draft's negative Dario guardrail is supportable from the reviewed derivative text. Neither the converted reading nor the chunk/source-packet reading names Dario.

## Scored Judgment

| Metric | Score / Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil registration birth records are high-quality sources when the correct row is source-verified. |
| conversion_confidence_score | 0.25 | The two derivative transcript families disagree materially, and the source/page image was unavailable for verification. |
| evidence_quantity_score | 0.45 | There are multiple local derivatives, but they split into two incompatible readings rather than accumulating independent support. |
| agreement_score | 0.20 | Converted/page Markdown support the Burgos/de la Cruz row; chunk/source packet support the Pulgar/Arriagada row. |
| identity_confidence_score | 0.40 | The Pulgar child identity is internally coherent in the chunk packet, but not source-certified and contradicted by the converted/page Markdown. |
| claim_probability | 0.52 | Best judgment is that a Pulgar/Arriagada row may exist in the page image, but this task cannot certify it as controlling entry 172 without targeted QA. |
| relevance_level | high | If confirmed, the chunk directly concerns Pulgar/Arriagada identity and parent claims; it is also relevant as an anti-conflation guardrail. |
| relevance_confidence | 0.82 | Relevance is high under the Pulgar-row hypothesis, but reduced by the unresolved row-control conflict. |
| canonical_readiness | hold_for_conversion_qa | Requires source-image row control and correction or supersession of conflicting derivatives before any promotion. |

## Claim And Identity Risk

- Literal support for the Pulgar/Arriagada birth claim is present in the chunk and source packet only. It is not confirmed against the source image in this review.
- Literal support for the Burgos/de la Cruz entry 172 reading is present in the converted file and page Markdown only. It is also not confirmed against the source image in this review.
- Relationship claims to `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar` are high-risk until the Pulgar row is certified as the controlling entry 172 row.
- The father suffix after `Pulgar` remains unresolved and should not be normalized to a stable identity label.
- Same-person or merge reasoning involving canonical `Jose del Carmen Pulgar`, `Juana de Dios Amagada de Pulgar`, or any Dario candidate is not supported by the reviewed evidence.

## Next Action

Run targeted conversion QA against the actual source/page image for `CHUNK-b8f4f0490a36-P0001-01`. The QA note should explicitly decide which derivative row is controlling for physical entry 172 and should record whether the father field is `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or an uncertain reading. After that, revise or supersede the staged identity analysis and rerun proof review before any canonical claim, relationship, merge, rename, or Dario-line comparison is promoted.
