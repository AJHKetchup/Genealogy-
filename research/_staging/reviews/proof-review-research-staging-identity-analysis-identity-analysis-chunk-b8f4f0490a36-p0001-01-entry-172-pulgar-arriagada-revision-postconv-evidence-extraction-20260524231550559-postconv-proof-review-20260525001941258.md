---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524231550559.md
worker: postconv-proof-review-20260525001941258
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524231550559.md
reviewed_at: 2026-05-25T00:19:41Z
decision: hold
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524231550559.md
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
referenced_chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
source_image: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
source_quality_score: 0.88
conversion_confidence_score: 0.38
evidence_quantity_score: 0.64
agreement_score: 0.46
identity_confidence_score: 0.74
claim_probability: 0.78
relevance_level: critical
relevance_confidence: 0.94
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Pulgar/Arriagada Identity Analysis

## Blockers

- Canonical readiness is blocked by an unresolved derivative-transcription conflict. The referenced chunk and visible source image support entry 172 as the Pulgar/Arriagada row, but the referenced converted Markdown currently transcribes entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 in `En esta`.
- The staged draft and source packet correctly identify a material conflict, but their description of the converted-file error does not match the converted file reviewed for this task. They say the assigned converted Markdown gives `Jose Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`, born in `Pellin`; that exact set of details was not present in the converted file at review time.
- The father-name suffix remains unresolved. The chunk gives `Jose del Carmen Pulgar S.`, while the source packet and visible-source review allow only the broad father reading `Jose del Carmen Pulgar` until targeted QA decides whether an `S.` or other mark is source-visible.
- Do not promote child identity, birth facts, parent-child relationships, parent-candidate merge claims, or any Dario attachment from this staged draft while conversion QA is outstanding.
- Do not attach this entry to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario Pulgar Arriagada, or any Dario passenger candidate. The reviewed source context does not name Dario and supplies no lineage bridge.

## Evidence Strengths

- The raw source image is available and visibly shows register page 58, entry 172 as a civil birth-register row for `Jose del Carmen Segundo Pulgar Arriagada`.
- The referenced chunk agrees with the visible source image on the core identity cluster: child `Jose del Carmen Segundo Pulgar Arriagada`, mother `Juana Arriagada de Pulgar`, informant `Ernesto Herrera L.`, and broad father identity `Jose del Carmen Pulgar`.
- The source type is strong for the fact type. A civil birth registration is direct evidence for the registered child identity, birth registration context, and declared parents once the derivative transcription conflict is reconciled.
- The staged draft is appropriately conservative in its main recommendation: `hold_for_conversion_qa`, with no Dario-line attachment by surname or family context alone.

## Scored Judgment

| factor | score / value | rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | The source image is a civil birth register, a high-quality source class for birth and declared-parent facts, though handwriting and row alignment require QA. |
| conversion_confidence_score | 0.38 | The assigned converted Markdown conflicts materially with the chunk and visible image for entry 172. |
| evidence_quantity_score | 0.64 | One source image, one chunk, one converted file, and one source packet were reviewed; enough to diagnose the conflict but not enough for canonical promotion. |
| agreement_score | 0.46 | The image, chunk, and core staged conclusion agree on the Pulgar/Arriagada row, while the converted file and some conflict-description details disagree. |
| identity_confidence_score | 0.74 | The Pulgar/Arriagada row identity is probable from image/chunk review, but father suffix uncertainty and conversion lineage conflict reduce confidence. |
| claim_probability | 0.78 | Probable that entry 172 is the Pulgar/Arriagada birth entry described in broad terms; not yet ready for canonical use. |
| relevance_level | critical | The evidence directly determines whether this staged identity analysis can be used. |
| relevance_confidence | 0.94 | The staged draft, chunk, source packet, and image all point to the same source image, page 58, entry 172, despite derivative-text conflict. |
| canonical_readiness | hold_for_conversion_qa | Hold until targeted conversion QA reconciles or supersedes the converted Markdown and records the father-field reading. |

## Claim Review

- Entry 172 Pulgar/Arriagada identity cluster: hold. The image and chunk support the broad cluster, but the converted-file conflict prevents promotion.
- Father identity field: revise after QA. Do not assert the suffix `S.` as settled unless targeted source-image QA records that reading.
- Dario-related identity or relationship claim: unsupported from this source. The claim probability for same-person or lineage attachment to a Dario candidate from this entry alone is near zero.

## Next Action

Send to targeted conversion QA. Reconcile or supersede the referenced converted Markdown for page 58, entry 172 against the source image; correct the conflict description to match the actual converted file or updated QA result; and explicitly record whether the father field reads `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. Rerun proof review before any canonical claim, relationship, identity merge, or wiki promotion.
