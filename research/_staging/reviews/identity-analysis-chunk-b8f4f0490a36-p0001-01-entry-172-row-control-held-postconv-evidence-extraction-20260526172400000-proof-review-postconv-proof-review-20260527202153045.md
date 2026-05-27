---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260527202153045
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-control-held-postconv-evidence-extraction-20260526172400000.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-control-held-postconv-evidence-extraction-20260526172400000.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526172400000.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Control Conflict

## Blockers First

1. Do not promote the Pulgar/Arriagada birth identity or parent-child relationships yet. The assigned chunk records entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, but the current converted Markdown and page-level conversion record entry 172 as `José Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
2. The referenced raw source image path is unavailable in this workspace, and the manifest page image path is also unavailable. This reviewer could not perform direct visual certification of the register row.
3. The converted file's current SHA-256 does not match the chunk/source-packet `converted_sha256`, so the review context has version drift in addition to the row-content conflict.
4. The staged draft correctly blocks Dario-line identity bridging. This entry, even if later certified as Pulgar/Arriagada, does not by itself prove a same-person identity with Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario J. Pulgar Arriagada, or Dario/Darío Pulgar Arriagada.

## Evidence Strengths

- The assigned chunk and source packet agree that entry 172 is a Pulgar/Arriagada row: child `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, birth on 8 March 1888 at Calle de Valdivia, and registration on 7 April 1888.
- The staged draft preserves the conflict instead of promoting a corrected transcription, which is the appropriate treatment while the source image cannot be checked here.
- Civil birth registration is a strong source type for child identity, birth date/place, and declared parents once the row transcription is visually certified.
- The source packet explicitly limits the father's trailing mark after `Pulgar` and does not force-certify the suffix.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 for the underlying civil birth register type; 4/10 for the accessible review packet because the source image is missing |
| conversion_confidence_score | 2/10 for entry 172 as currently staged, due to direct conflict between chunk/source packet and converted Markdown plus missing image |
| evidence_quantity_score | 3/10 |
| agreement_score | 3/10 overall: chunk and source packet agree with each other, but the converted file and page-level conversion materially disagree |
| identity_confidence_score | 4/10 for the narrow Pulgar/Arriagada birth identity pending image QA; 1/10 for any Dario-line same-person merge |
| claim_probability | 0.55 that entry 172 is the Pulgar/Arriagada row based on chunk/source packet only; 0.95 that a material conversion conflict exists; 0.10 or lower for any Dario-line identity bridge |
| relevance_level | high if certified as Pulgar/Arriagada; medium as a held conflict item |
| relevance_confidence | 0.75 |
| canonical_readiness | hold |

## Review Finding

The staged draft is supported as a held identity and row-control conflict. It should not be promoted to canonical claims, relationships, or person pages until targeted conversion QA can inspect the actual page image and decide whether entry 172 controls as Pulgar/Arriagada or Burgos/de la Cruz.

This review does not certify the Pulgar reading from the visible source because no source image was available to inspect. The only certifiable review conclusion is that the staged draft, source packet, chunk, and current converted Markdown are not in reliable agreement.

## Next Action

Run targeted conversion QA against the source image or restored page image. Certify entry 172's row identity and transcribe the father field only as far as the visible source supports: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. Keep all child identity claims, parent-child relationships, father suffix readings, and Dario-line comparisons on hold until that QA result is available.
