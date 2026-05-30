---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530224457330
task_id: proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530222737522.md
staged_draft: research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530222737522.md
reviewed_at: 2026-05-30T22:45:35Z
canonical_readiness: not_ready
next_action: hold_for_conversion_qa
---

# Proof Review: CHUNK-fb0a0000636f-P0005-01 Page-Control Conflict

This review covers staged draft `research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530222737522.md`.

## Blockers First

1. Page control is unresolved. The assigned chunk `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md` transcribes the 1979-1982 HABITAT, 1974-1978 NFB, 1972-1973 Chile Films, and 1970-1972 CITELCO sequence. The conversion job page Markdown `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md` transcribes a different 1999/1998 sequence headed by PROFONANPE, TVE, Arca/European Commission, Klohn Crippen, and SNC Lavalin.
2. Independent source inspection is blocked in this checkout. `raw/sources/CV of Dario Arturo Pulgar.pdf` is absent, and no `page-0005.jpg` exists under the conversion job directory.
3. Provenance metadata is unstable. The chunk records converted SHA-256 `fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0`, but the observed converted file hash is `DA9EC0C3A0F604B4C0E827A2A733A0BA013DD60D86ABEA2B46490D9F8820D288`.
4. The chunk manifest repeats `CHUNK-fb0a0000636f-P0005-01` for the same page/chunk path with conflicting character counts and hashes, so it cannot serve as a reliable control.
5. Page-local identity and relationship support is missing. Neither competing page-5 transcription names `Dario Arturo Pulgar`, `Pulgar-Smith`, `Pulgar-Arriagada`, parents, spouse, children, siblings, or other kinship links.

## Scored Judgment

| Dimension | Score / Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.35 | The cited source is a CV with recorded source metadata, but the source PDF is absent and cannot be directly inspected. |
| conversion_confidence_score | 0.15 | Page-control derivatives materially disagree, the page image is unavailable, the converted-file hash has drifted, and the chunk manifest is duplicated. |
| evidence_quantity_score | 0.30 | There is enough derivative text to identify a page-control conflict, but not enough controlled evidence to promote any page-5 work-history or identity claim. |
| agreement_score | 0.10 | The assigned chunk/aggregate conversion and job page Markdown disagree on the content of page 5. |
| identity_confidence_score | 0.45 | Document-level title context supports association with `Dario Arturo Pulgar`, but this page does not repeat the name or provide an identity bridge. |
| claim_probability | 0.25 | The draft's hold recommendation is well supported; the probability of any specific page-5 occupational claim being canonically usable now is low until QA resolves control. |
| relevance_level | high | A CV titled for `Dario Arturo Pulgar` is relevant to the Pulgar identity cluster and possible later `Dario Arturo Pulgar-Smith` bridge work. |
| relevance_confidence | 0.85 | Relevance follows from the source title and packet, though page-local identity evidence is weak. |
| canonical_readiness | not_ready | No claim, relationship, identity merge, or person-page attachment should be promoted from this draft. |

## Evidence Strengths

- The staged draft accurately identifies the central conflict between the 1979-1970 assigned chunk text and the 1999/1998 conversion job page Markdown text.
- The source packet independently records the same page-control concern, missing page image, hash mismatch, duplicate manifest entries, and hold recommendation.
- The assigned chunk text is internally coherent as a CV work-history page, and the job page Markdown is also internally coherent as a different CV work-history page. That pattern supports a page-control/provenance problem rather than a minor transcription correction.
- The draft correctly avoids promoting family relationships or merging Dario/Pulgar identity candidates from this page.

## Claim Review

### Claim: Page 5 belongs to document-level CV subject `Dario Arturo Pulgar`

Judgment: hold/revise before canonical use.

The source title and source packet identify the document as `CV of Dario Arturo Pulgar`, but page 5 itself does not repeat the name. Because page control is unresolved, this should remain a working document-level attribution only.

Scores: source_quality_score 0.35; conversion_confidence_score 0.15; evidence_quantity_score 0.35; agreement_score 0.10; identity_confidence_score 0.45; claim_probability 0.45; relevance_level high; relevance_confidence 0.85; canonical_readiness not_ready.

### Claim: The CV subject is canonical `Dario Arturo Pulgar-Smith`

Judgment: hold.

This evidence provides only partial name-overlap context through the source title. The reviewed page does not state `Smith`, family relationships, Alexander John Heinz, dates, or another bridge identifier. A later identity-bridge review may ask whether the CV subject is the canonical person, but this page cannot answer it.

Scores: source_quality_score 0.35; conversion_confidence_score 0.15; evidence_quantity_score 0.20; agreement_score 0.10; identity_confidence_score 0.25; claim_probability 0.25; relevance_level medium; relevance_confidence 0.65; canonical_readiness not_ready.

### Claim: The CV subject is `Dario Jose Pulgar-Arriagada` or `Dario/Darío Pulgar Arriagada`

Judgment: hold/reject for this page.

The reviewed page evidence does not state `Jose`, `J.`, `Arriagada`, `Pulgar-Arriagada`, parents, spouse, property context, birth data, or other bridge evidence. Name overlap alone is insufficient and carries high identity-conflation risk.

Scores: source_quality_score 0.35; conversion_confidence_score 0.15; evidence_quantity_score 0.10; agreement_score 0.10; identity_confidence_score 0.05; claim_probability 0.05; relevance_level low; relevance_confidence 0.55; canonical_readiness not_ready.

### Claim: The page supports Jose/Juana parent-candidate relationships

Judgment: unsupported.

No reviewed page-local text names Jose, Juana, parents, children, household members, or kinship. Parent-candidate proof belongs to the relevant identity-bearing relationship records, not this page-control review.

Scores: source_quality_score 0.35; conversion_confidence_score 0.15; evidence_quantity_score 0.05; agreement_score 0.10; identity_confidence_score 0.02; claim_probability 0.01; relevance_level low; relevance_confidence 0.75; canonical_readiness not_ready.

## Source Reliability And Conversion Confidence

The derivative files are useful for locating the conflict, but they are not stable enough for proof. The observed converted file hash does not match the chunk's recorded converted hash, the manifest has duplicate page-5 chunk records with conflicting metadata, the source PDF is absent, and no page image is available for visual page-control verification.

## Identity And Relationship Risk

Identity risk is moderate to high. The evidence supports asking whether the document-level CV subject is `Dario Arturo Pulgar-Smith`, but it does not support answering yes from this page. Relationship risk is high for any parent, spouse, child, sibling, grandchild, or household claim because neither competing page-5 transcription contains kinship text.

## Next Action

Hold for conversion QA. Restore or verify the source PDF/page image, reconcile the converted-file hash drift, repair duplicate manifest entries, and certify the controlling page-5 transcription. After page control is fixed, run a separate identity-bridge proof review before connecting `Dario Arturo Pulgar` to any canonical person page or relationship.

No raw sources, converted Markdown, chunks, source packets, canonical wiki pages, or staged drafts were edited.
