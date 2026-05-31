---
type: proof_review_note
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260531085135447
task_id: proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-identity-hold-postconv-evidence-extraction-20260531064559241.md
staged_draft: research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-identity-hold-postconv-evidence-extraction-20260531064559241.md
source: raw/sources/CV of Dario Arturo Pulgar.pdf
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
conversion_job_page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
chunk_id: CHUNK-fb0a0000636f-P0005-01
page_reference: page 5
source_quality_score: 0.30
conversion_confidence_score: 0.10
evidence_quantity_score: 0.20
agreement_score: 0.05
identity_confidence_score: 0.15
claim_probability: 0.20
relevance_level: high
relevance_confidence: 0.85
canonical_readiness: blocked
promotion_recommendation: hold_for_conversion_qa
---

# Proof Review: Page-Control Identity Hold

## Blockers

- Page-control conflict remains. The assigned chunk and current aggregate converted file contain a 1979-1970 work-history sequence: HABITAT, National Film Board of Canada, Chile Films, and CITELCO. The conversion-job page markdown for `page-0005.md` instead contains a 1999-1997 consulting-work sequence: PROFONANPE, Television Trust for the Environment, Arca Consulting/European Commission, Klohn Crippen, and SNC Lavalin Agriculture.
- Physical-page verification is blocked. The manifest records `page-images/page-0005.jpg`, but that image is not present locally. The referenced raw source PDF and the job-local staged source PDF are also absent locally, so the visible source cannot be checked against either derivative transcript.
- Provenance consistency is weak. The chunk manifest lists `CHUNK-fb0a0000636f-P0005-01` twice for the same chunk path with different character counts and SHA-256 values. Current observed hashes for the aggregate converted file and the assigned chunk differ from the recorded converted SHA-256.
- Identity attachment is not page-local. The page text available in the assigned chunk does not repeat the CV subject name and does not state `Pulgar-Smith`, parents, spouse, children, or any family bridge.

## Evidence Strengths

- The staged draft accurately identifies the conflict between the assigned chunk/current aggregate converted file and the conversion-job page markdown.
- The staged draft appropriately treats the CV subject attribution as a document-continuity hypothesis only, not as page-local proof.
- The negative relationship caution is supported: neither competing page-5 derivative transcript states a kinship relationship or a family identity bridge.

## Scored Judgment

- `source_quality_score`: 0.30. The source is a CV packet identified by title/manifest, but the raw PDF and local staged PDF are unavailable for direct review.
- `conversion_confidence_score`: 0.10. Competing derivative transcripts disagree for page 5, and the page image is unavailable.
- `evidence_quantity_score`: 0.20. There is enough derivative evidence to justify a hold, but not enough source-visible evidence to support promotion.
- `agreement_score`: 0.05. The key page-control witnesses materially disagree.
- `identity_confidence_score`: 0.15. Attribution to Dario Arturo Pulgar is plausible from document context, but not page-local and not source-verified here.
- `claim_probability`: 0.20. The claim that page-5 work-history content belongs to the CV subject remains possible but unproven under the current page-control conflict.
- `relevance_level`: high.
- `relevance_confidence`: 0.85.
- `canonical_readiness`: blocked.

## Next Action

Hold this staged draft from canonical promotion. Conversion QA should restore or regenerate the authoritative page-5 image, reconcile `page-markdown/page-0005.md`, the aggregate converted file, and the chunk manifest, then rerun identity proof review before any page-5 claim is attached to a canonical person or relationship.
