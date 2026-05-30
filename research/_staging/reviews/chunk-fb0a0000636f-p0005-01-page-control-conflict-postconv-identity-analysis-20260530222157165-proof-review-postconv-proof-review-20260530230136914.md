---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530230136914
task_id: proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530222157165.md
staged_draft: research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530222157165.md
reviewed_subject: "Dario Arturo Pulgar, document-level CV subject"
source: raw/sources/CV of Dario Arturo Pulgar.pdf
source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-work-history-hold-postconv-evidence-extraction-20260530213419489.md
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
conversion_job_page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
review_decision: hold
canonical_readiness: not_ready
source_quality_score: 0.35
conversion_confidence_score: 0.15
evidence_quantity_score: 0.30
agreement_score: 0.10
identity_confidence_score: 0.40
claim_probability: 0.35
relevance_level: high
relevance_confidence: 0.85
---

# Proof Review: Page-Control Conflict Identity Analysis

This review covers only staged draft `research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530222157165.md` and its referenced local evidence.

## Blockers First

1. Canonical readiness is `not_ready`. The staged draft correctly identifies a conversion/provenance blocker rather than a promotable identity or work-history claim.
2. The controlling page-5 transcription is unresolved. The assigned chunk reads the page as the 1979-1982 HABITAT / 1974-1978 NFB / 1972-1973 Chile Films / 1970-1972 CITELCO sequence, while the conversion job page Markdown reads page 5 as 1999/1998 PROFONANPE / TVE / Arca / Klohn Crippen / SNC Lavalin text.
3. The page image and source PDF are not available in this checkout at the referenced paths, so the derivative disagreement cannot be resolved by visual source review.
4. Hash/provenance control is weak. The source packet reports converted-file hash drift, and direct hashing confirms the aggregate converted file currently hashes to `da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288`, not the chunk-recorded `fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0`.
5. The chunk manifest repeats `CHUNK-fb0a0000636f-P0005-01` for the same path with different character counts, which blocks clean provenance scoring.
6. The page-local text does not name Dario Arturo Pulgar, Dario Arturo Pulgar-Smith, Dario Jose Pulgar-Arriagada, parents, spouse, children, or Alexander John Heinz. Identity is document-level inference from the CV title/context, not page-local proof.

## Evidence Strengths

- The staged draft accurately preserves the core conflict and recommends holding claims for conversion QA.
- The source packet, conflict candidate, assigned chunk, and conversion-job page Markdown all exist and support the stated derivative disagreement.
- The assigned chunk is internally coherent as CV work-history text and is legible in the conversion derivative.
- The conversion-job page Markdown is also internally coherent as CV work-history text, which increases the probability that both texts belong somewhere in the CV packet even though page-5 control is unresolved.
- The analysis avoids unsupported relationship promotion and explicitly warns against merging similarly named Pulgar identities by name alone.

## Scored Judgment

| Metric | Score / Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.35 | The named source is a CV, but the PDF and page image are absent locally, leaving only derivatives. |
| conversion_confidence_score | 0.15 | Two derivative page-5 readings conflict, with hash drift and duplicate manifest entries. |
| evidence_quantity_score | 0.30 | There are multiple derivatives and staging notes, but no visible source image/PDF for adjudication. |
| agreement_score | 0.10 | The assigned chunk and conversion-job page Markdown materially disagree. |
| identity_confidence_score | 0.40 | The CV title supports document-level `Dario Arturo Pulgar`; page-local identity support is absent. |
| claim_probability | 0.35 | The claim that this draft should remain held is high; any page-5 factual promotion remains low probability until QA. |
| relevance_level | high | A CV for Dario Arturo Pulgar is potentially family-relevant, but only after page and identity control are repaired. |
| relevance_confidence | 0.85 | The source title and staged context make relevance likely despite weak proof control. |
| canonical_readiness | not_ready | No canonical claim, relationship, merge, or work-history promotion should occur from this draft. |

## Claim Review

The staged draft's central claim is supported: this is a derivative transcription/page-control conflict and must be held for conversion QA. The draft's more specific identity hypotheses are appropriately cautious. The evidence can support only a limited document-level inference that the CV packet concerns `Dario Arturo Pulgar`; it cannot prove that this page belongs to canonical `Dario Arturo Pulgar-Smith`, and it cannot bridge to `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, Jose/Juana parent candidates, or any kinship relationship.

The strongest probability judgment is that both derivative text blocks may belong to the same CV conversion set but that page ordering or chunk/control metadata is corrupted. That probability is approximately 0.70. The probability that page 5 can presently support a canonical work-history claim is no higher than 0.20 because the physical page cannot be checked.

## Next Action

Keep the staged draft on hold for conversion QA. Restore or regenerate the source PDF/page image access, repair the duplicate chunk manifest entries, reconcile the converted-file hash drift, and compare the physical page 5 against both derivative readings before any proof review promotes work-history or identity claims.

No raw sources, converted Markdown, chunks, source packets, staged drafts outside this review note, or canonical wiki pages were edited.
