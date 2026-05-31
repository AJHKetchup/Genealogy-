---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530234355462
task_id: proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530231621335.md
staged_draft: research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530231621335.md
reviewed_at: 2026-05-30T23:50:00Z
canonical_readiness: not_ready
next_action: hold_for_conversion_qa
---

# Proof Review: CHUNK-fb0a0000636f-P0005-01 Page-Control Conflict

This review covers staged draft `research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530231621335.md`.

## Blockers First

1. Page control is unresolved. The assigned chunk `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md` transcribes the 1979-1982 HABITAT through 1970-1972 CITELCO sequence and ends with `EDUCATION`, while the conversion-job page Markdown `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md` transcribes 1999/1998 PROFONANPE, TVE, Arca/European Commission, Klohn Crippen, and SNC Lavalin entries.
2. Independent physical-page verification is blocked in this checkout. `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0005.jpg`, `raw/sources/CV of Dario Arturo Pulgar.pdf`, and the staged job source PDF path were not present when checked.
3. Provenance metadata is unstable. The chunk records converted SHA-256 `fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0`, while the observed converted file hash is `DA9EC0C3A0F604B4C0E827A2A733A0BA013DD60D86ABEA2B46490D9F8820D288`; the observed page-5 chunk hash is `D6EA4F611EE03000C11CBBA63246E95B55F8A421FCBC87D0D667E91F5C8D0B8D`.
4. The chunk manifest repeats `CHUNK-fb0a0000636f-P0005-01` for the same path with conflicting character counts and hashes.
5. The reviewed page-local text does not independently name `Dario Arturo Pulgar`, `Pulgar-Smith`, `Pulgar-Arriagada`, Jose/Juana parent candidates, Alexander John Heinz, or any kinship relationship.

## Scored Judgment

| Dimension | Score / Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.35 | The source packet identifies a CV and source hash, but the source PDF/page image were unavailable for direct inspection. |
| conversion_confidence_score | 0.15 | Two derivative page-5 texts conflict, hashes drift from recorded metadata, and duplicate manifest rows exist. |
| evidence_quantity_score | 0.30 | There is enough derivative evidence to prove a page-control conflict, but not enough controlled evidence for a canonical work-history or identity claim. |
| agreement_score | 0.10 | The assigned chunk and page Markdown materially disagree about the content of page 5. |
| identity_confidence_score | 0.45 | Document title/packet context links the file to `Dario Arturo Pulgar`; the reviewed page body is not identity-bearing. |
| claim_probability | 0.88 | The claim that this staged item is a hold-worthy page-control/provenance conflict is strongly supported by local artifacts. |
| relevance_level | high | A CV for `Dario Arturo Pulgar` is relevant to Pulgar identity analysis and possible later Pulgar-Smith bridge work. |
| relevance_confidence | 0.85 | Relevance follows from the source title and source packet, with page-local relevance limited by absent identity text. |
| canonical_readiness | not_ready | No canonical claim, relationship, identity merge, or work-history promotion should be made until conversion QA resolves page control. |

## Evidence Strengths

- The staged draft accurately identifies the competing derivative readings: the assigned chunk contains the 1979-1970 HABITAT/NFB/Chile Films/CITELCO sequence, while the conversion-job page Markdown contains the 1999-1997 PROFONANPE/TVE/Arca/Klohn/SNC Lavalin sequence.
- The source packet independently records the same conversion QA concern, hash mismatch, duplicate manifest problem, missing page image, and `hold_for_conversion_qa` recommendation.
- Both derivative texts are internally coherent as CV work-history pages, which supports treating this as a page-control/provenance problem rather than a narrow transcription typo.
- The staged draft correctly avoids making parentage, spouse, child, grandchild, same-person merge, or canonical page-update claims from this evidence.

## Claim Review

### Claim: Page 5 belongs to document-level CV subject `Dario Arturo Pulgar`

Judgment: hold before canonical use.

The source title and packet support this as a working document-level attribution. The page body itself does not repeat the subject name, and page control is unresolved.

Scores: source_quality_score 0.35; conversion_confidence_score 0.15; evidence_quantity_score 0.35; agreement_score 0.10; identity_confidence_score 0.45; claim_probability 0.45; relevance_level high; relevance_confidence 0.85; canonical_readiness not_ready.

### Claim: The CV subject is canonical `Dario Arturo Pulgar-Smith`

Judgment: hold.

This page supplies name-overlap context only. It does not contain `Smith`, family relationships, Alexander John Heinz, dates, or another page-local bridge identifier.

Scores: source_quality_score 0.35; conversion_confidence_score 0.15; evidence_quantity_score 0.20; agreement_score 0.10; identity_confidence_score 0.25; claim_probability 0.25; relevance_level medium; relevance_confidence 0.65; canonical_readiness not_ready.

### Claim: The CV subject is `Dario Jose Pulgar-Arriagada` or `Dario Pulgar Arriagada`

Judgment: unsupported for this page.

The reviewed materials do not state `Jose`, `J.`, `Arriagada`, `Pulgar-Arriagada`, parents, spouse, property context, or a medical/Geneva context. Name overlap alone is too risky for identity attachment.

Scores: source_quality_score 0.35; conversion_confidence_score 0.15; evidence_quantity_score 0.10; agreement_score 0.10; identity_confidence_score 0.05; claim_probability 0.05; relevance_level low; relevance_confidence 0.55; canonical_readiness not_ready.

### Claim: The page supports Jose/Juana parent-candidate relationships

Judgment: unsupported.

No reviewed page-local text names Jose, Juana, parents, children, household members, or kinship.

Scores: source_quality_score 0.35; conversion_confidence_score 0.15; evidence_quantity_score 0.05; agreement_score 0.10; identity_confidence_score 0.02; claim_probability 0.01; relevance_level low; relevance_confidence 0.75; canonical_readiness not_ready.

## Next Action

Hold for conversion QA. Restore or verify the authoritative source PDF/page image, reconcile the duplicate `CHUNK-fb0a0000636f-P0005-01` manifest entries and hash drift, then certify which page-5 transcription controls. After page control is fixed, run a separate identity-bridge proof review before connecting `Dario Arturo Pulgar` to `Dario Arturo Pulgar-Smith` or any Pulgar-Arriagada/Jose/Juana cluster.

No raw sources, converted Markdown, chunks, source packets, staged identity drafts, canonical claims, relationships, or wiki pages were edited.
