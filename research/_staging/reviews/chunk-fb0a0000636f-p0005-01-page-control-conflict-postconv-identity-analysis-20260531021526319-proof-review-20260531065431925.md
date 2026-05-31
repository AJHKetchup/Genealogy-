---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260531065431925
task_id: "proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531021526319.md"
staged_draft: "research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531021526319.md"
review_status: hold
canonical_readiness: hold
---

# Proof Review: Page-Control Conflict For CHUNK-fb0a0000636f-P0005-01

## Blockers

- The exact staged draft under review recommends `hold_for_conversion_qa`, and local verification supports that hold.
- The raw source `raw/sources/CV of Dario Arturo Pulgar.pdf` is not present locally.
- The expected page image `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0005.jpg` is not present locally.
- The assigned chunk `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md` contains the 1979-1970 HABITAT, National Film Board of Canada, Chile Films, and CITELCO sequence.
- The conversion-job page Markdown `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md` contains a different 1999-1997 PROFONANPE, TVE, Arca Consulting/European Commission, Klohn Crippen Consultants, and SNC Lavalin Agriculture sequence.
- The aggregate converted file contains both the 1999-1997 and 1979-1970 work-history sequences, so it does not resolve physical page control by itself.
- The chunk manifest duplicates `CHUNK-fb0a0000636f-P0005-01`, and observed file hashes differ from recorded metadata:
  - current chunk SHA256: `D6EA4F611EE03000C11CBBA63246E95B55F8A421FCBC87D0D667E91F5C8D0B8D`
  - current aggregate converted-file SHA256: `DA9EC0C3A0F604B4C0E827A2A733A0BA013DD60D86ABEA2B46490D9F8820D288`
  - current page Markdown SHA256: `B87BD19F16275A992482651063C280BFC303BC6B7B0CD30CFBC2843D6D5E692F`
- Neither competing page-5 derivative prints the CV subject's personal name on the page body, and neither states a family relationship.
- No claim from this staged draft is ready for canonical promotion or attachment to `Dario Arturo Pulgar-Smith`, Pulgar-Arriagada candidates, or Jose/Juana family candidates.

## Evidence Strengths

- The staged draft accurately identifies the core page-control conflict between the assigned chunk and the conversion-job page Markdown.
- The chunk and page Markdown are both readable derivative texts and each preserves an internally coherent CV work-history page.
- The document-level file and path context support treating `Dario Arturo Pulgar` as a candidate CV subject after conversion QA, but only as document-level context, not page-local proof.
- The staged draft appropriately separates identity review from transcription correction and does not claim family relationships from the page.

## Scores

| score | value | rationale |
|---|---:|---|
| source_quality_score | 0.35 | The source appears to be a CV, useful for occupational context, but the raw PDF and page image are unavailable for direct verification. |
| conversion_confidence_score | 0.18 | Page-control conflict, missing image/PDF controls, duplicate manifest rows, and hash drift prevent trusting a controlling page transcript. |
| evidence_quantity_score | 0.42 | There are multiple derivative texts, but they disagree on the page and cannot substitute for the physical source. |
| agreement_score | 0.20 | The assigned chunk conflicts directly with the page Markdown; the aggregate contains both sequences. |
| identity_confidence_score | 0.46 | Document title/path supports a `Dario Arturo Pulgar` CV context, but the disputed page body gives no page-local name or identity bridge. |
| claim_probability | 0.34 | The safest reviewed claim is only that unresolved derivative evidence exists for page 5; no occupational or identity claim is stable enough for promotion. |
| relevance_level | 1.00 | The reviewed evidence directly concerns the exact staged draft and assigned chunk. |
| relevance_confidence | 0.98 | The inspected files are the staged draft's referenced chunk, converted file, and page Markdown controls. |
| canonical_readiness | 0.00 | Hold; no canonical fact, relationship, merge, or identity attachment is supported. |

## Review Judgment

The staged draft is literally supported as a conflict analysis and should remain on `hold_for_conversion_qa`. The page-control conflict is not a minor uncertainty: two incompatible work-history sequences are attached to page 5 through different derivative paths, and the physical source controls needed to adjudicate them are absent.

The only supported conclusion is that page 5 cannot currently be used for canonical occupational, identity, or relationship claims. The document-level title can justify later checking whether the CV belongs to `Dario Arturo Pulgar`, but the page body does not prove `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, or any Jose/Juana relationship.

## Next Action

Keep the staged draft and dependent page-5 claims on hold. Restore or regenerate the raw PDF or authoritative `page-0005.jpg`, compare it against both derivative readings, reconcile the duplicate chunk manifest rows and hash drift, and then rerun proof review for the surviving page-5 transcript before any canonical promotion or identity-bridge review.
