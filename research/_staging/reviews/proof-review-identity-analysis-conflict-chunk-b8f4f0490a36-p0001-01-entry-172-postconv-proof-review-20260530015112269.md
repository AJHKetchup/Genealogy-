---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260530015112269
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-postconv-identity-analysis-20260525123339261.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-postconv-identity-analysis-20260525123339261.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115123585.md"
reviewed_followup_task: "research/_staging/tasks/task-chunk-b8f4f0490a36-p0001-01-entry-172-source-image-row-control-followup-postconv-evidence-extraction-20260530014639534.md"
canonical_readiness: hold_for_conversion_qa
source_quality_score: 0.78
conversion_confidence_score: 0.20
evidence_quantity_score: 0.42
agreement_score: 0.18
identity_confidence_score: 0.38
claim_probability: 0.50
relevance_level: high
relevance_confidence: 0.86
---

# Proof Review: Entry 172 Identity Conflict

## Blockers First

- Canonical readiness remains `hold_for_conversion_qa`. The staged draft correctly identifies a material row-level conflict, but the visible source image is unavailable in this workspace, so this review cannot certify whether physical entry `172` is the Pulgar/Arriagada row or the Burgos/de la Cruz row.
- The referenced source image path `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png` could not be opened from the workspace. The conversion job manifest points to a page image path under `raw/codex-conversion-jobs/.../page-images/page-0001.png`, but that image is also absent.
- The assigned converted Markdown and the assigned chunk disagree on nearly every identity-controlling field for entry `172`: child, parents, birth date, birth place, informant, and official context. These derivative files cannot both be literal readings of the same physical row.
- The staged draft overstates one detail of the converted Markdown. The currently reviewed converted file reads entry `172` as `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born `El seis de Abril...`; it does not read `Jose Francisco`, `Oswaldo Gomez`, `Emilia de la Cruz`, or `veinte i seis de Marzo`.
- The father-field suffix in the Pulgar-row reading remains uncertified. Preserve `Jose del Carmen Pulgar S.` only as a chunk/source-packet reading until image QA confirms whether the visible source supports `S.`, no suffix, or an uncertain mark.
- No Dario attachment is supported by the reviewed files. The reviewed entry candidates do not name Dario, and surname/context overlap is not sufficient for a relationship or same-person claim.

## Evidence Strengths

- The staged draft's central conclusion is supported: this is a severe conversion/file-assignment conflict, not a spelling variant or minor transcription difference.
- The assigned chunk and source packet agree with each other that entry `172` is the Pulgar/Arriagada row: `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born `Ocho de Marzo...` at `Calle de Valdivia`.
- The assigned converted Markdown consistently gives a different row for entry `172`: `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born `El seis de Abril...` at `En esta`.
- The source type, if the image is recovered and verified, is a strong civil birth registration source for child identity, parent names, birth date/place, and informant context.
- The staged draft appropriately keeps dependent identity and relationship conclusions out of canonical promotion and treats Dario-line linkage as unsupported.

## Scored Judgment

| Metric | Score / Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.78 | Civil registration is a strong source class, but the source image is missing for this review. |
| conversion_confidence_score | 0.20 | The converted Markdown and chunk materially disagree, and no page image was available to arbitrate. |
| evidence_quantity_score | 0.42 | There are two derivative readings plus a source packet and follow-up note, but no source-image verification. |
| agreement_score | 0.18 | Chunk/source packet agree with each other, but conflict with the assigned converted Markdown on identity-controlling fields. |
| identity_confidence_score | 0.38 | The Pulgar-row identity is internally coherent in the chunk, but row control is unresolved. |
| claim_probability | 0.50 | No promoted identity claim should be made from this packet until image QA resolves which row controls entry `172`. |
| relevance_level | high | If the Pulgar row is confirmed, the entry is directly relevant to Pulgar/Arriagada parent-child evidence; if not, it is relevant as an anti-attachment guardrail. |
| relevance_confidence | 0.86 | The conflict directly concerns the assigned family-relevant row and Dario anti-conflation controls. |
| canonical_readiness | hold_for_conversion_qa | Targeted source-image row-control QA is required before any canonical claim, relationship, merge, or Dario-line comparison. |

## Review Decision

Hold the staged draft for conversion QA, with one revision note: future reviewers should use the current converted Markdown wording (`José Miguel`, `Oswaldo Burgos`, `Concepcion de la Cruz`, `El seis de Abril...`) rather than the older/incorrect converted-file summary preserved in the staged draft.

## Next Action

Locate the original source image or equivalent page image for SHA-256 `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2`, then perform targeted visual QA for physical entry `172` on register page `58`. The QA note must decide whether the controlling row is Pulgar/Arriagada or Burgos/de la Cruz and must certify the father field if the Pulgar row controls. After that, rerun proof review before any canonical promotion.
