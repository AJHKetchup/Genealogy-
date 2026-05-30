---
type: proof_review
status: complete
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-identity-analysis-20260530110056293.md"
worker: "postconv-proof-review-20260530121144671"
role: claim_reviewer
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-identity-analysis-20260530110056293.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530102722394.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
review_decision: hold
canonical_readiness: not_ready
source_quality_score: 0.72
conversion_confidence_score: 0.32
evidence_quantity_score: 0.48
agreement_score: 0.18
identity_confidence_score: 0.34
claim_probability: 0.64
relevance_level: high
relevance_confidence: 0.82
---

# Proof Review: Entry 172 Row-Control Conflict Identity Analysis

This review covers only the staged draft `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-control-conflict-postconv-identity-analysis-20260530110056293.md`.

## Blockers First

- Row-control remains unresolved. The assigned chunk transcribes entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`; the current converted Markdown transcribes entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
- The full source image path named by the chunk and source packet is absent in this checkout, so this review cannot certify which physical row controls entry `172`.
- The available staging crop assets are described by the source packet as parent-field portions only; they cannot independently certify row number, page order, or full entry boundaries.
- The father suffix after `Jose del Carmen Pulgar` is not safe to expand or normalize from this review. Preserve it as unresolved unless a full-image QA pass supports the exact reading.
- No Dario identity is literally named in the reviewed source materials. The staged draft correctly treats any Dario comparison as identity-risk context, not as a supported same-person or parent-child claim.

## Evidence Strengths

- The staged draft accurately reports the material disagreement between the assigned chunk and the current converted Markdown: child name, parents, birth date, birth time, birth place, and informant all differ.
- The assigned chunk is internally coherent as a civil birth registration for a Pulgar/Arriagada child, and the current converted file is internally coherent as a different Burgos/de la Cruz entry. This supports a row-control or derivative-conversion conflict rather than a spelling variant.
- The source packet explicitly marks the evidence `hold_for_conversion_qa` and warns not to promote child identity, birth event, parent-child relationships, identity merges, Dario-line attachments, or wiki updates.
- The staged draft's canonical boundary is appropriate: it recommends hold/not-ready and does not ask for promotion to claims, relationships, or wiki pages.

## Scores

| Dimension | Score / Level | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.72 | Civil registration is a strong source class, but this review did not have the original image needed to verify the physical row. |
| conversion_confidence_score | 0.32 | The derivative chunk and converted Markdown conflict on the controlling row and household. |
| evidence_quantity_score | 0.48 | There are two derivative transcriptions plus a source packet, but no full-page image available for final certification. |
| agreement_score | 0.18 | Agreement is low for entry `172`; only the entry number and registration date broadly overlap. |
| identity_confidence_score | 0.34 | Pulgar/Arriagada identity claims are plausible from the chunk but not certifiable while row control is unresolved. |
| claim_probability | 0.64 | The claim that this is a real row-control conflict is well supported; the claim that the Pulgar/Arriagada row controls entry `172` remains probable but unproved. |
| relevance_level | high | The Pulgar/Arriagada names are family-relevant if the row is certified. |
| relevance_confidence | 0.82 | Relevance is high for review triage, though not enough for canonical attachment. |
| canonical_readiness | not_ready | Do not promote, merge, rename, or attach relationships from this packet. |

## Claim Probability Notes

- Probability that the reviewed staged draft correctly identifies a row-control conflict: 0.90.
- Probability that the Pulgar/Arriagada row controls the canonical entry `172` without further QA: 0.64.
- Probability that the Burgos/de la Cruz row controls the canonical entry `172` without further QA: 0.24.
- Probability that this packet supports a direct Dario identity bridge: 0.02.

## Next Action

Keep the item on `hold_for_conversion_qa`. The next worker should locate or restore the full original page image for source SHA-256 `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2`, verify page and row alignment for entry `172`, and then re-review only the certified child, birth-event, parent-name, and parent-child claims. No canonical updates are ready from this review.
