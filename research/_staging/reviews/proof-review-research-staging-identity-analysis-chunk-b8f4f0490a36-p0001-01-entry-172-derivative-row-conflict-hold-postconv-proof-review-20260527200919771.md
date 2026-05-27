---
type: proof_review
status: hold
role: claim_reviewer
worker: "postconv-proof-review-20260527200919771"
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-hold-postconv-identity-analysis-20260527195958685.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-hold-postconv-identity-analysis-20260527195958685.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260527180532740.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register pages 58-59; entry 172"
canonical_readiness: hold_for_conversion_qa
promotion_recommendation: hold_for_conversion_qa
---

# Proof Review: Entry 172 Derivative Row Conflict

## Blockers

1. The staged draft is literally supported as a conflict/hold analysis, but the underlying identity claim is not ready for canonical promotion because the referenced derivatives disagree on the physical row for entry `172`.
2. The assigned chunk/source packet read entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`; the current converted Markdown reads entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
3. The source image path `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png` is absent in this checkout, and the conversion job folder does not contain a page image directory available for image-level review.
4. The father-field suffix in the Pulgar/Arriagada derivative cannot be normalized beyond what is written in the assigned chunk. This review does not convert `Jose del Carmen Pulgar S.` into a fuller identity.
5. No reviewed source for this task names any Dario candidate in entry `172`; any Dario-line attachment would be unsupported by this evidence.

## Scores

| Dimension | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.78 | Civil birth registration is a strong source type in principle, but this review only had derivative transcriptions, not the visible source image. |
| conversion_confidence_score | 0.28 | The assigned chunk and current converted Markdown materially conflict on entry number, child, parents, dates, and register context. |
| evidence_quantity_score | 0.52 | There are multiple internal derivatives and a staged packet, but no independent image inspection in this review. |
| agreement_score | 0.24 | The key derivatives disagree on the controlling row; agreement exists only between the assigned chunk and held packet. |
| identity_confidence_score | 0.60 | Moderate that the draft correctly identifies a Pulgar/Arriagada-vs-Burgos/de la Cruz conflict; not enough for person or relationship promotion. |
| claim_probability | 0.83 | High probability that the staged item should remain held for conversion QA; lower probability for any promoted identity claim. |
| relevance_level | high | The conflict directly affects a family-relevant Pulgar/Arriagada row and possible parent-child claims. |
| relevance_confidence | 0.90 | The names Pulgar and Arriagada are present in the assigned chunk/source packet and are central to the staged analysis. |
| canonical_readiness | hold_for_conversion_qa | Do not promote, merge, rename, or update relationships from this staged draft until row control is resolved. |

## Evidence Strengths

- The staged draft accurately reports the main derivative conflict and does not attempt to resolve the row by guessing.
- The source packet preserves the assigned chunk's Pulgar/Arriagada reading and explicitly flags the current converted Markdown conflict.
- The assigned chunk gives a coherent table row for entry `172` on page 58 with child, birth details, father, mother, informant, and official signature context.
- The converted Markdown gives a different coherent row for entry `172`, which strengthens the conclusion that this is a row-control or derivative-source conflict rather than a minor transcription variant.
- The staged draft's recommendation to hold for conversion QA is proportionate to the available evidence.

## Verification Notes

Reviewed materials:

- Staged draft: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-hold-postconv-identity-analysis-20260527195958685.md`
- Conflict candidate: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-hold-postconv-evidence-extraction-20260527180532740.md`
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260527180532740.md`
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`

No external research was performed. No raw sources, converted Markdown, chunks, source packets, staged identity drafts, or canonical wiki pages were edited.

## Next Action

Keep the staged draft on `hold_for_conversion_qa`. The next reviewer should perform targeted image-level row control for physical entry `172`, then either reconcile the current converted Markdown with the assigned chunk or mark one derivative as stale/misassigned. Until then, do not promote entry-172 child identity, parent-child relationships, father suffix normalization, or Dario-line identity bridges.
