---
type: proof_review
role: claim_reviewer
status: completed
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-analysis-20260526134239386.md
worker: postconv-proof-review-20260530013944131
staged_draft: research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-analysis-20260526134239386.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526095657171.md
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
chunk_id: CHUNK-b8f4f0490a36-P0001-01
source_quality_score: 0.86
conversion_confidence_score: 0.34
evidence_quantity_score: 0.62
agreement_score: 0.22
identity_confidence_score: 0.78
claim_probability: 0.82
relevance_level: high
relevance_confidence: 0.96
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Current Conversion Conflict

## Blockers

- The exact staged draft reviewed is `research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-identity-analysis-20260526134239386.md`.
- The referenced converted file and referenced chunk materially disagree for register page 58, entry 172. The converted file reads entry 172 as a Burgos/de la Cruz birth for `Jose Miguel`; the chunk reads entry 172 as a Pulgar/Arriagada birth for `Jose del Carmen Segundo Pulgar Arriagada`.
- The source packet reports image review supporting the Pulgar/Arriagada row, but it also marks conversion confidence low and requires targeted conversion QA before promotion.
- The father field is not fully certified. The chunk reads `Jose del Carmen Pulgar S.`, while the source packet certifies only `Jose del Carmen Pulgar` and leaves any trailing initial or mark unresolved.
- Parent-child relationship claims are not canonical-ready because they depend on resolving the row-level derivative conflict.
- No Dario identity appears in the staged draft, source packet, chunk, or converted-file reading. Any Dario attachment would be unsupported in this review.

## Scores

| score | value | rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth registration is a strong direct source type for birth and parent fields, assuming the row is correctly identified. |
| conversion_confidence_score | 0.34 | The chunk and source packet align, but the main converted Markdown contradicts them at the row level. |
| evidence_quantity_score | 0.62 | Three local artifacts were available: staged draft, source packet with image-review summary, and both derivative transcriptions. Quantity is enough to identify the conflict, not enough to resolve it. |
| agreement_score | 0.22 | Agreement is low because the converted file and chunk assign entry 172 to different people, parents, dates, places, and informants. |
| identity_confidence_score | 0.78 | The Pulgar/Arriagada identity is probable on the chunk plus source-packet image-review summary, but reduced by the contradictory converted file. |
| claim_probability | 0.82 | Probability that the staged conflict analysis is correct to hold the Pulgar/Arriagada reading pending QA; not probability for canonical promotion. |
| relevance_level | high | Entry 172 is directly relevant to the staged Pulgar/Arriagada conflict and anti-conflation review. |
| relevance_confidence | 0.96 | The reviewed artifacts all reference the same chunk id, source image path, and entry number. |
| canonical_readiness | hold_for_conversion_qa | Do not promote identity, birth, parent-child, parent-pair, merge, or Dario-line claims until conversion QA resolves the controlling row. |

## Evidence Strengths

- The chunk gives a coherent row for entry 172: registration on 7 April 1888; child `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`; birth on 8 March 1888 at 3 p.m.; place `Calle de Valdivia`; father `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`.
- The source packet independently preserves the same Pulgar/Arriagada reading and states that image review supports that row over the Burgos/de la Cruz row in the converted Markdown.
- The source packet correctly limits the father reading to `Jose del Carmen Pulgar` with the trailing mark unresolved, which is a useful guardrail against over-normalizing the name.
- The staged draft correctly treats Dario-line context as an anti-conflation issue rather than as evidence for a Dario identity.

## Review Judgment

The staged draft is supported as a conflict/hold analysis. It should not be revised into a promotion-ready proof note because the controlling transcription is unresolved. The Pulgar/Arriagada row is more probable than the Burgos/de la Cruz row for this staged evidence set, but that probability depends on a source-packet image-review summary and a chunk that contradicts the current converted Markdown.

The Burgos/de la Cruz reading remains relevant only as the competing derivative transcription. It should not generate canonical Burgos/de la Cruz identities or displace the Pulgar/Arriagada row unless targeted conversion QA proves the chunk or source-packet attachment is wrong.

## Next Action

Hold for targeted conversion QA of `CHUNK-b8f4f0490a36-P0001-01` against the original page image, the converted Markdown, the current chunk, and the source packet. QA should explicitly decide whether entry 172 is the Pulgar/Arriagada row or the Burgos/de la Cruz row and should certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or an unresolved marked form.

After QA, rerun proof review before promoting any child identity, birth fact, parent-child relationship, parent-pair claim, parent identity merge, or Dario-line comparison.
