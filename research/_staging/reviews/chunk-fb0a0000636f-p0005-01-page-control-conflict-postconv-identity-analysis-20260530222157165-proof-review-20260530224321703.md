---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530224237893
task_id: proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530222157165.md
staged_draft: research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530222157165.md
reviewed_at: 2026-05-30T22:43:21Z
canonical_readiness: not_ready
next_action: hold_for_conversion_qa
---

# Proof Review: CHUNK-fb0a0000636f-P0005-01 Page-Control Conflict

This review covers staged draft `research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530222157165.md`.

## Blockers First

1. Page control is unresolved. The assigned chunk `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md` transcribes the 1979-1982 HABITAT through 1970-1972 CITELCO sequence and ends with `EDUCATION`, while `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md` transcribes 1999/1998 PROFONANPE, TVE, Arca/EC, Klohn Crippen, and SNC Lavalin entries.
2. The source image and source PDF needed for independent page-control review are unavailable in this checkout: `page-images/page-0005.jpg` is absent, and `raw/sources/CV of Dario Arturo Pulgar.pdf` is absent.
3. Hash drift is confirmed. The chunk/manifest recorded converted SHA-256 is `fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0`; the observed converted file hash is `DA9EC0C3A0F604B4C0E827A2A733A0BA013DD60D86ABEA2B46490D9F8820D288`.
4. The chunk manifest repeats `CHUNK-fb0a0000636f-P0005-01` for the same chunk path with conflicting character counts and hashes, so the manifest is not reliable enough for promotion.
5. The page-local text does not name `Dario Arturo Pulgar`, `Pulgar-Smith`, `Pulgar-Arriagada`, Jose/Juana parent candidates, Alexander John Heinz, or any kinship relationship. Identity is document-level inference from the source title and context only.

## Scored Judgment

| Dimension | Score / Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.35 | The underlying source is a CV and the source packet records a source hash, but the PDF is absent, so the original cannot be inspected. |
| conversion_confidence_score | 0.15 | Two derivative transcriptions disagree on page 5, the observed converted hash differs from recorded metadata, and no page image is available. |
| evidence_quantity_score | 0.30 | There is enough derivative text to identify the nature of the conflict, but not enough reliable controlled evidence to support a canonical claim. |
| agreement_score | 0.10 | The assigned chunk and conversion job page Markdown materially disagree on page content. |
| identity_confidence_score | 0.45 | Document-level title context supports association with `Dario Arturo Pulgar`, but the page itself has no local identity-bearing name or relationship bridge. |
| claim_probability | 0.25 | The draft's main claim that this is a hold-worthy page-control conflict is well supported; any work-history or identity promotion from page 5 is low probability until QA resolves page control. |
| relevance_level | high | A CV for `Dario Arturo Pulgar` is relevant to the Pulgar identity cluster and possible `Dario Arturo Pulgar-Smith` bridge review. |
| relevance_confidence | 0.85 | Relevance follows from the source title and source packet; page-local relevance is limited by absent identity text. |
| canonical_readiness | not_ready | Conversion/page control must be repaired before any claim, relationship, identity merge, or work-history promotion. |

## Evidence Strengths

- The staged draft accurately preserves the central conversion conflict: one derivative page-5 reading is the 1979-1970 HABITAT/NFB/Chile Films/CITELCO page, and another is the 1999/1998 PROFONANPE/TVE/Arca/Klohn/SNC Lavalin page.
- The source packet independently records the same conversion QA concern, the hash mismatch, missing page image, and hold recommendation.
- The assigned chunk text is internally coherent as a CV work-history page, and the conversion job page Markdown is also internally coherent as a CV work-history page; this supports a page-control problem rather than a simple transcription typo.
- The draft correctly avoids using this page for parentage, spouse, child, grandchild, or same-person merge claims.

## Claim Review

### Claim: Page 5 belongs to document-level CV subject `Dario Arturo Pulgar`

Judgment: hold/revise before canonical use.

The source title and packet identify the document as `CV of Dario Arturo Pulgar`, but the page body itself does not repeat the name and the controlling page-5 transcription is unresolved. This can remain a working document-level attribution, not a promoted identity fact.

Scores: source_quality_score 0.35; conversion_confidence_score 0.15; evidence_quantity_score 0.35; agreement_score 0.10; identity_confidence_score 0.45; claim_probability 0.45; relevance_level high; relevance_confidence 0.85; canonical_readiness not_ready.

### Claim: The CV subject is canonical `Dario Arturo Pulgar-Smith`

Judgment: hold.

This page supplies name-overlap context only. It does not contain `Smith`, family relationships, Alexander John Heinz, dates, or another page-local bridge identifier. A later identity-bridge review may ask whether this CV subject is Dario Arturo Pulgar-Smith, but this page cannot answer that question.

Scores: source_quality_score 0.35; conversion_confidence_score 0.15; evidence_quantity_score 0.20; agreement_score 0.10; identity_confidence_score 0.25; claim_probability 0.25; relevance_level medium; relevance_confidence 0.65; canonical_readiness not_ready.

### Claim: The CV subject is `Dario Jose Pulgar-Arriagada` / `Dario Pulgar Arriagada`

Judgment: hold/reject for this page.

The reviewed page evidence does not state `Jose`, `J.`, `Arriagada`, `Pulgar-Arriagada`, parents, spouse, property context, or a medical/Geneva context. Name overlap alone is insufficient and creates a high identity-conflation risk.

Scores: source_quality_score 0.35; conversion_confidence_score 0.15; evidence_quantity_score 0.10; agreement_score 0.10; identity_confidence_score 0.05; claim_probability 0.05; relevance_level low; relevance_confidence 0.55; canonical_readiness not_ready.

### Claim: The page supports Jose/Juana parent-candidate relationships

Judgment: unsupported.

No reviewed page-local text names Jose, Juana, parents, children, household members, or kinship. Relationship claims must remain outside this page-control review.

Scores: source_quality_score 0.35; conversion_confidence_score 0.15; evidence_quantity_score 0.05; agreement_score 0.10; identity_confidence_score 0.02; claim_probability 0.01; relevance_level low; relevance_confidence 0.75; canonical_readiness not_ready.

## Source Reliability And Conversion Confidence

The source packet and chunk metadata are useful for locating the evidence, but they are not stable proof controls. The observed converted file hash does not match the recorded hash, and the manifest has duplicate page-5 chunk records with conflicting metadata. Because the page image and PDF are absent, I cannot resolve which derivative page text corresponds to the physical page 5.

## Identity And Relationship Risk

Identity risk is moderate to high. The evidence can justify the question "is this document-level CV subject Dario Arturo Pulgar-Smith?" but cannot justify silently treating the answer as yes. Relationship risk is high for any parent, spouse, child, or grandchild claim because the page contains no relationship statement.

## Next Action

Hold for conversion QA. Restore or verify the source PDF/page image, reconcile the converted-file hash drift and duplicate manifest entries, and select the controlling page-5 transcription. After page control is fixed, run a separate identity-bridge proof review before connecting `Dario Arturo Pulgar` to any canonical person page or relationship.

No raw sources, converted Markdown, chunks, source packets, canonical wiki pages, or staged drafts were edited.
