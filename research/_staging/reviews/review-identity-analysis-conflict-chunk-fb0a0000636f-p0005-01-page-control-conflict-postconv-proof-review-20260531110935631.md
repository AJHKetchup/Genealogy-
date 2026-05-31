---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260531110935631
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531020516022.md
staged_draft: research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531020516022.md
reviewed_source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-revision-postconv-evidence-extraction-20260531004750573.md
reviewed_chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
reviewed_conversion_job_page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
source_quality_score: 0.35
conversion_confidence_score: 0.10
evidence_quantity_score: 0.40
agreement_score: 0.15
identity_confidence_score: 0.30
claim_probability: 0.28
relevance_level: direct
relevance_confidence: 0.98
canonical_readiness: blocked
promotion_recommendation: hold_for_conversion_qa
---

# Proof Review: CV Page 5 Control Conflict

## Blockers First

1. The staged draft correctly treats this as a page-control conflict, not a canonical identity proof. The assigned chunk for `CHUNK-fb0a0000636f-P0005-01` contains a 1979-1970 work-history page ending with `EDUCATION`; the conversion-job page Markdown for `page-0005.md` contains a different 1999-1997 consulting-work page.
2. The recorded source PDF `raw/sources/CV of Dario Arturo Pulgar.pdf` is absent at the reviewed path, and `page-images/page-0005.jpg` is absent at the reviewed path. There is no visible physical page in this task to decide which derivative text controls page 5.
3. The chunk manifest contains duplicate entries for `CHUNK-fb0a0000636f-P0005-01` with conflicting character counts and hashes. This independently blocks reliance on the chunk metadata.
4. The page body in the reviewed assigned chunk does not independently name `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada`. The subject attribution is only document-title/path context.
5. No reviewed page-5 evidence states parents, spouse, children, Alexander John Heinz, `Jose`, `Juana`, `Smith`, `Arriagada`, or any kinship link. Same-person and relationship claims must remain blocked.

## Evidence Strengths

- The assigned derivative chunk plainly supports the narrow observation that a local chunk file contains CV-style work-history entries for HABITAT, the National Film Board of Canada, Chile Films, and CITELCO.
- The competing conversion-job page Markdown plainly supports the narrow observation that another local page-5 derivative contains PROFONANPE, TVE, Arca Consulting/European Commission, Klohn Crippen Consultants, and SNC Lavalin Agriculture entries.
- The source packet accurately flags the conflict, source absence, page-image absence, and the need for conversion QA before promotion.
- The staged identity analysis is relevant to the assigned draft and appropriately recommends holding rather than promotion.

## Scores

| Category | Score / Value | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.35 | Source title/path context is useful, but the original PDF and page image needed for control are absent. |
| conversion_confidence_score | 0.10 | Conflicting page-5 derivatives plus duplicate manifest entries and hash drift make page assignment unreliable. |
| evidence_quantity_score | 0.40 | There are multiple derivative artifacts, but they are not independent physical-source evidence and they disagree. |
| agreement_score | 0.15 | Agreement is limited to both derivatives being plausible CV work-history text; the page-5 literal content conflicts. |
| identity_confidence_score | 0.30 | The document-level name `Dario Arturo Pulgar` is plausible from title/path only; page body supplies no bridge identifiers. |
| claim_probability | 0.28 | Page-5 canonical or identity claims are improbable until control is repaired. Narrow local-derivative text claims are stronger but not promotion-ready. |
| relevance_level | direct | The review addresses the exact staged draft and its referenced artifacts. |
| relevance_confidence | 0.98 | The artifacts reviewed are directly named in the staged draft/front matter. |
| canonical_readiness | blocked | No claim, relationship, merge, rename, or wiki update is ready. |

## Claim Judgments

| Claim / hypothesis | Review judgment | Probability | Canonical readiness |
| --- | --- | ---: | --- |
| Assigned chunk text exists locally as 1979-1970 work history. | Supported as a local derivative reading only. | 0.96 | hold |
| Assigned chunk text controls physical page 5. | Not proved; blocked by absent source/page image and competing `page-0005.md`. | 0.28 | blocked |
| Conversion-job `page-0005.md` controls physical page 5. | Not proved; it is a competing derivative, not an adjudicated source. | 0.32 | blocked |
| The CV page belongs to document-level `Dario Arturo Pulgar`. | Plausible from title/path, but not independently stated on the reviewed page body. | 0.55 | hold |
| `Dario Arturo Pulgar` is the same person as `Dario Arturo Pulgar-Smith`. | Insufficient support; no `Smith`, family relationship, or direct identifier appears in reviewed page evidence. | 0.22 | blocked |
| `Dario Arturo Pulgar` is the same person as `Dario Jose Pulgar-Arriagada` or `Dario/Darío Pulgar Arriagada`. | Insufficient support; no `Jose`, `Arriagada`, parentage, residence, or other bridge appears in reviewed page evidence. | 0.05 | blocked |
| Any Jose/Juana parent relationship is supported by page 5. | Unsupported; no parent or lineage statement appears. | 0.01 | blocked |

## Next Action

Run conversion QA for this CV page set before any proof promotion:

1. Restore or regenerate authoritative access to the original PDF or `page-images/page-0005.jpg`.
2. Compare the visible physical page 5 against the assigned chunk, aggregate converted Markdown, conversion-job `page-0005.md`, and manifests.
3. Repair duplicate `CHUNK-fb0a0000636f-P0005-01` manifest metadata and hash drift.
4. Only after page control is certified, run a separate identity-bridge review for the full CV cluster against the Pulgar/Pulgar-Smith/Pulgar-Arriagada candidates.

No raw sources, converted Markdown, chunks, source packets, relationship notes, claims, or canonical wiki pages were edited.
