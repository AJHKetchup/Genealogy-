---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260531090143333
task_id: proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-identity-hold-postconv-evidence-extraction-20260531064559241.md
staged_draft: research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-identity-hold-postconv-evidence-extraction-20260531064559241.md
reviewed_status: hold
source_quality_score: 4.0
conversion_confidence_score: 1.0
evidence_quantity_score: 2.0
agreement_score: 1.0
identity_confidence_score: 1.0
claim_probability: 0.15
relevance_level: high
relevance_confidence: 0.90
canonical_readiness: blocked
---

# Proof Review: CHUNK-fb0a0000636f-P0005-01 Page-Control Identity Hold

## Blockers

- Page-control conflict blocks promotion. The staged draft correctly reports that the assigned chunk is not in agreement with the page-specific conversion artifact. The chunk at `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md` contains 1979-1982 HABITAT and later 1974-1970 work-history entries, while `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md` contains 1999-1997 consulting entries for PROFONANPE, TVE, Arca Consulting/European Commission, Klohn Crippen, and SNC Lavalin Agriculture.
- The source PDF named in the staged draft, `raw/sources/CV of Dario Arturo Pulgar.pdf`, was not locally present during review. The job manifest also names `page-images/page-0005.jpg` and a staged source PDF path, but both tested absent locally. I therefore cannot verify either derivative text against the physical page image or source PDF.
- The chunk manifest has duplicate `CHUNK-fb0a0000636f-P0005-01` rows for the same chunk path with different character counts and hashes. The observed SHA-256 values during review were `DA9EC0C3A0F604B4C0E827A2A733A0BA013DD60D86ABEA2B46490D9F8820D288` for the aggregate converted Markdown and `D6EA4F611EE03000C11CBBA63246E95B55F8A421FCBC87D0D667E91F5C8D0B8D` for the chunk; these do not match the page-5 chunk manifest rows.
- No reviewed page body repeats the CV subject name or supplies a family bridge to `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, `Jose del Carmen Pulgar`, or `Juana Arriagada de Pulgar`. Any identity attachment would depend on document continuity after page control is repaired.

## Evidence Strengths

- The staged draft's hold recommendation is supported by the available derivative artifacts: the page-specific Markdown and the assigned chunk are visibly incompatible.
- The source is relevant to the target identity problem because the job title and source metadata identify a CV of Dario Arturo Pulgar, but that relevance is document-level only until the actual page image/source PDF can be checked.
- The draft preserves the boundary between verification and transcription by recommending conversion QA and a later identity-bridge review rather than rewriting uncertain readings.

## Scores And Judgment

- `source_quality_score`: 4.0/10. A CV can be useful for work-history evidence, but only derivative artifacts were available; the cited source PDF and page image were absent.
- `conversion_confidence_score`: 1.0/10. The page-control conflict, missing page image, missing local source PDF, duplicate chunk manifest rows, and hash drift make conversion reliability blocked.
- `evidence_quantity_score`: 2.0/10. There is enough evidence to support a hold, but not enough verified evidence to support a work-history or identity claim.
- `agreement_score`: 1.0/10. The assigned chunk and page-specific Markdown materially disagree.
- `identity_confidence_score`: 1.0/10. The visible page text does not name the subject or state family relationships; identity is only inferred from document metadata.
- `claim_probability`: 0.15 for canonically using the page-5 work-history/identity claims as presently staged. The probability that the staged draft's hold recommendation is appropriate is high, approximately 0.90.
- `relevance_level`: high.
- `relevance_confidence`: 0.90.
- `canonical_readiness`: blocked.

## Next Action

Keep this staged draft on hold. Restore or regenerate the cited source PDF/page-0005 image, reconcile the duplicate chunk manifest rows and observed hashes, rerun conversion QA for physical page 5, then run a separate identity-bridge proof review before attaching any accepted CV content to a canonical person or family cluster.
