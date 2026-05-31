---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531001505918.md
worker: postconv-proof-review-20260531084907603
staged_draft: research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531001505918.md
review_status: hold_for_conversion_qa
canonical_readiness: not_ready
created_at: 2026-05-31T08:49:07Z
---

# Proof Review: Page-Control Conflict for CHUNK-fb0a0000636f-P0005-01

## Blockers

- The staged draft under review is `research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531001505918.md`.
- The physical source cannot be visually checked in this checkout. `raw/sources/CV of Dario Arturo Pulgar.pdf`, `page-images/page-0005.jpg`, and `extracted-images/page-0005.jpg` are absent locally.
- The assigned chunk and the conversion-job page Markdown disagree materially about page 5:
  - `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md` gives a 1979-1970 sequence ending at `EDUCATION`.
  - `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md` gives a 1999-1997 sequence beginning with PROFONANPE.
- The aggregate converted file includes the 1999-1997 text under page 5 and also includes the 1979-1970 text later under incomplete page metadata, so the current derivative chain does not establish which text controls physical page 5.
- The chunk manifest repeats `CHUNK-fb0a0000636f-P0005-01` for the same path/page with different character counts and hashes. The source packet also records observed hash drift between chunk metadata and current derivative files.
- Page 5 does not independently state a family relationship, parentage, spouse, child, birth fact, or a bridge from document-level `Dario Arturo Pulgar` to any canonical person such as `Dario Arturo Pulgar-Smith` or Pulgar-Arriagada candidates.

## Evidence Strengths

- The source packet and staged identity analysis accurately identify this as a conversion-control conflict rather than a resolved biographical contradiction.
- The assigned chunk is internally coherent and legible as a CV work-history page covering HABITAT, the National Film Board of Canada, Chile Films, and CITELCO.
- The competing page Markdown is also internally coherent and legible as a CV work-history page covering PROFONANPE, Television Trust for the Environment, Arca Consulting/European Commission, Klohn Crippen Consultants, and SNC Lavalin Agriculture.
- The source title and job manifest consistently identify the document as `CV of Dario Arturo Pulgar`, which supports only a document-level subject label until page control and identity bridging are separately reviewed.
- The staged draft correctly avoids promoting occupational, place, relationship, or same-person claims from this conflicted evidence.

## Scores

| field | score | review judgment |
| --- | ---: | --- |
| source_quality_score | 0.45 | The named source is a CV and likely relevant to the document-level subject, but the PDF and rendered page image are unavailable for source control in this review. |
| conversion_confidence_score | 0.20 | Severe page-control conflict, duplicated manifest entries, hash drift, and absent page images prevent certification. |
| evidence_quantity_score | 0.35 | Multiple derivative files were available, but they are conflicting derivatives rather than independent corroboration. |
| agreement_score | 0.25 | The source packet, chunk, page Markdown, aggregate conversion, and manifest agree on provenance labels but disagree on controlling page-5 text. |
| identity_confidence_score | 0.50 | Moderate only for document-level `Dario Arturo Pulgar`; low for any canonical attachment. |
| claim_probability | 0.35 | Specific page-5 occupational/place claims cannot be treated as established until physical page control is restored. |
| relevance_level | high | The reviewed files directly address the assigned staged draft and conflict. |
| relevance_confidence | 0.95 | Scope is tight to the staged draft and its referenced derivative files. |
| canonical_readiness | 0.05 | Not ready for canonical claims, relationships, merges, person-page edits, or promotion. |

## Proof Judgment

Decision: `hold_for_conversion_qa`.

The staged draft is literally supported in its main conclusion: this is a page-control and provenance conflict, not proof of a canonical identity or relationship. The derivative evidence can show that two plausible CV work-history transcriptions exist in the workspace, but it cannot establish which transcription belongs to physical page 5. Because the visible source and page image are unavailable, neither the 1999-1997 nor the 1979-1970 page-5 claim set should be promoted.

Identity risk is material. The document-level title supports only `Dario Arturo Pulgar` as the CV subject. It does not, from this page alone, support merging or attaching the evidence to `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, any Dario Pulgar passenger stub, or Jose/Juana parent candidates.

## Next Action

Restore or locate the authoritative source PDF and rendered page-5 image, then perform conversion QA to decide whether physical page 5 is the 1999-1997 consulting page or the 1979-1970 work-history page. Reconcile the duplicate manifest entries and hash drift before any proof review of the surviving occupational claims. After page control is certified, run a separate identity-bridge review before attaching document-level `Dario Arturo Pulgar` to any canonical person.
