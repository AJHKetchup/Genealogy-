---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260530225440429
task_id: "proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530222737522.md"
staged_draft: research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530222737522.md
source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-work-history-hold-postconv-evidence-extraction-20260530213419489.md
source: raw/sources/CV of Dario Arturo Pulgar.pdf
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
canonical_readiness: hold
---

# Proof Review: Page 5 CV Control Conflict

## Blockers First

- Hold. The staged identity analysis is supported in its central warning: the assigned chunk for page 5 contains the 1979-1982 HABITAT, 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, and 1970-1972 CITELCO sequence, while the conversion job page Markdown and one section of the aggregate converted file contain a different 1999/1998 sequence headed by PROFONANPE, Television Trust for the Environment, Arca Consulting/European Commission, Klohn Crippen, and SNC Lavalin.
- The visible page image needed to decide which derivative transcription controls is unavailable at the manifest path `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0005.jpg`. The manifest lists that image and hash, but the file is not present locally.
- Provenance remains blocked. The chunk metadata records converted SHA-256 `fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0`, while the observed aggregate converted file SHA-256 is `da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288`; the observed assigned chunk SHA-256 is `d6ea4f611ee03000c11cbba63246e95b55f8a421fcbc87d0d667e91f5c8d0b8d`, not either page-5 manifest entry.
- Page 5 does not name parents, spouse, children, siblings, or other kin. It also does not repeat the subject's full name in the page body, so person attachment relies on document-level CV context rather than page-internal identity evidence.
- The identity-analysis draft discusses canonical Dario/Pulgar candidates, but this proof review did not verify those canonical pages because the immediate staged claim is a page-control conflict and the reviewed page evidence does not support a relationship or merge.

## Evidence Strengths

- The staged draft accurately preserves the conflict instead of choosing one derivative text. The assigned chunk and the aggregate converted file include the 1979-1970 work-history sequence; the conversion job page Markdown includes the 1999/1998 sequence.
- The source packet accurately reports the core provenance concerns: recorded-versus-observed converted hash mismatch, duplicate chunk manifest entries for `CHUNK-fb0a0000636f-P0005-01`, and missing page image at the expected page-images path.
- Both derivative readings look like plausible CV work-history content for the same source packet, so the draft's recommendation to hold for conversion QA is proportionate. Neither derivative provides direct family-relationship evidence.

## Scores

| Category | Score | Review Judgment |
| --- | ---: | --- |
| source_quality_score | 0.55 | A CV can be useful for biographical/employment claims, but this review could not inspect the source image for page 5 and did not verify the underlying PDF page directly. |
| conversion_confidence_score | 0.20 | Severe derivative conflict, missing page image, stale manifest image reference, duplicate chunk manifest entries, and hash mismatch prevent proof-ready conversion use. |
| evidence_quantity_score | 0.35 | There are multiple derivative texts and metadata records, but only one disputed page and no visual source confirmation. |
| agreement_score | 0.15 | The assigned chunk and job page Markdown materially disagree about the controlling page-5 text. |
| identity_confidence_score | 0.70 | Reasonable for document-level attribution to `Dario Arturo Pulgar` from the source title and CV context, but page 5 itself does not repeat the name. |
| claim_probability | 0.50 | Either competing page-5 sequence may be the correct controlling transcription; the available evidence does not justify preferring one. |
| relevance_level | 0.70 | Relevant as potential Pulgar biography/work-history evidence after QA, not relevant as kinship proof. |
| relevance_confidence | 0.80 | The source title and CV context make biography relevance likely, while the page-control issue limits use. |
| canonical_readiness | 0.10 | Not ready for canonical promotion, person-page attachment, relationship promotion, merge, or rename. |

## Claim Review

- Page-control claim: supported. There is a real derivative transcription conflict between the assigned chunk and the conversion job page Markdown.
- Work-history claims from either sequence: hold. Literal derivative support exists, but visual and provenance support are insufficient to certify which sequence is page 5.
- Identity attachment to canonical `Dario Arturo Pulgar-Smith`: hold. Name overlap and source title support further review, but this page does not provide a `Smith` bridge, family relationship, birth/death data, spouse/child link, or other identity anchor.
- Relationship claims involving Jose/Juana or other Pulgar candidates: unsupported by this reviewed page.

## Next Action

Run conversion QA for `CHUNK-fb0a0000636f-P0005-01`: restore or regenerate `page-0005.jpg`, reconcile the aggregate converted file hash and chunk manifest entries, and certify the controlling page-5 transcription before any occupational claim is promoted. After page control is fixed, run a separate identity-bridge proof review before attaching any accepted CV claims to a canonical person page.
