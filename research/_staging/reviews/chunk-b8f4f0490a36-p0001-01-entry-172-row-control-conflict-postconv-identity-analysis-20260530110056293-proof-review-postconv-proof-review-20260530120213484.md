---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530120213484
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-identity-analysis-20260530110056293.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-identity-analysis-20260530110056293.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530102722394.md"
conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-evidence-extraction-20260530102722394.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source_quality_score: 0.72
conversion_confidence_score: 0.40
evidence_quantity_score: 0.45
agreement_score: 0.30
identity_confidence_score: 0.20
claim_probability: 0.65
relevance_level: high
relevance_confidence: 0.85
canonical_readiness: not_ready
---

# Proof Review: Entry 172 Row-Control Conflict

This review covers only staged draft `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-identity-analysis-20260530110056293.md`.

## Blockers First

1. Row control is not certified. The assigned chunk and source packet read entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, while the current converted Markdown reads entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
2. The original full source image is unavailable in this checkout. `raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png` could not be verified at the referenced path, and the conversion job directory has no `extracted-images` directory visible for direct page review.
3. The Pulgar/Arriagada parent-child claim, birth event, and any identity merge are blocked until full-page conversion QA certifies which physical row controls entry `172`.
4. The father suffix after `Jose del Carmen Pulgar` remains unresolved for canonical purposes. Do not promote `S.` as a certified suffix from this review.
5. No reviewed source text in this packet names Dario, Arturo, Smith, or a later-life identity bridge. The staged draft correctly blocks attachment to Dario Pulgar candidates.

## Evidence Strengths

- The assigned chunk and source packet are internally coherent for a civil birth registration: entry `172`, registration date `Siete de Abril de mil ochocientos ochenta i ocho`, child `Jose del Carmen Segundo Pulgar Arriagada`, mother `Juana Arriagada de Pulgar`, and a birth at `Calle de Valdivia`.
- The current converted Markdown is also internally coherent, but it describes a different entry-172 family: `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born `El seis de Abril de mil ochocientos ochenta i ocho` at `En esta`.
- The staged identity analysis accurately treats this as a derivative row-control conflict, not a spelling variant or same-person identity problem.
- The source type, if row control is later certified from the image, would be strong direct evidence for a birth event and named parent-child relationship.

## Scored Judgment

| Metric | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.72 | Civil birth registration is a strong source class, but this review could not inspect the full original image. |
| conversion_confidence_score | 0.40 | The assigned chunk and current converted Markdown materially disagree on the same entry number. |
| evidence_quantity_score | 0.45 | There is one relevant record transcription stream plus a conflicting conversion stream; no independent corroborating source was reviewed. |
| agreement_score | 0.30 | Agreement is high within each derivative reading, but low across the chunk/source packet and current converted file. |
| identity_confidence_score | 0.20 | The packet supports only a possible Pulgar/Arriagada row after QA; it does not support a Dario identity or canonical merge now. |
| claim_probability | 0.65 | The staged claim that this should be held for row-control QA is well supported; the underlying Pulgar/Arriagada birth claim is not ready. |
| relevance_level | high | The Pulgar/Arriagada reading is directly relevant to the target family cluster if certified. |
| relevance_confidence | 0.85 | Names and family context are highly relevant, but relevance does not overcome the row-control blocker. |
| canonical_readiness | not_ready | Do not promote birth, parent-child, same-person, or wiki facts from this packet. |

## Review Finding

The staged identity analysis is supported as a hold. Its central warning is correct: the available derivative records assign incompatible children, parents, birth dates, birth places, and informants to entry `172`. This review cannot choose the controlling transcription because the full source image was not available for row certification.

The Pulgar/Arriagada row should remain a family-relevant lead only. It is not sufficient evidence to merge or connect `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, or `Juana Arriagada de Pulgar` to canonical persons, and it provides no literal support for Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario Pulgar Arriagada.

## Next Action

Keep `canonical_readiness: not_ready` and retain `hold_for_conversion_qa`. The next worker should locate or restore the full original page image and certify the physical row for entry `172` before any claim extraction, relationship promotion, identity merge, or canonical wiki update is attempted.
