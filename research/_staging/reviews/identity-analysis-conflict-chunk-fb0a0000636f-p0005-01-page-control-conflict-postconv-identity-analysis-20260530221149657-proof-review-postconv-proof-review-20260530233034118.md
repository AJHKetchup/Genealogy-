---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260530233034118
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530221149657.md
staged_draft: research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530221149657.md
reviewed_source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-work-history-hold-postconv-evidence-extraction-20260530213419489.md
reviewed_converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
reviewed_chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
reviewed_conversion_job_page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
source_quality_score: 0.34
conversion_confidence_score: 0.18
evidence_quantity_score: 0.42
agreement_score: 0.18
identity_confidence_score: 0.52
claim_probability: 0.45
relevance_level: direct
relevance_confidence: 0.98
canonical_readiness: not_ready
created_at: 2026-05-30T23:30:34Z
---

# Proof Review: CHUNK-fb0a0000636f-P0005-01 Identity Analysis

## Blockers

- The staged draft correctly remains blocked by page-control failure. The assigned chunk transcribes a `1979 - 1982` through `1970 - 1972` work-history sequence, while the conversion job page Markdown for the same page number transcribes `1999`, `1998 - 1999`, and `1997-1998` entries.
- The source packet reports recorded-vs-observed converted hash drift: recorded `fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0`; observed `da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288`.
- The chunk manifest repeats `CHUNK-fb0a0000636f-P0005-01` for the same path/page with different character counts and hashes.
- The source PDF `raw/sources/CV of Dario Arturo Pulgar.pdf` is not present in this checkout, and `page-images/page-0005.jpg` is also absent, so visual adjudication of the literal page is unavailable.
- The page-5 body text reviewed here does not name `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, parents, spouse, children, or any kinship relationship. Identity attachment beyond document-level `Dario Arturo Pulgar` remains unsupported by this page alone.

## Evidence Strengths

- The staged draft accurately cites the referenced source packet, assigned chunk, aggregate converted file, and conversion job page Markdown.
- Both derivative transcriptions are internally plausible curriculum-vitae work-history text for a document titled `CV of Dario Arturo Pulgar`; the conflict is page/transcript control, not an obvious non-CV intrusion.
- The source packet explicitly limits promotion to work-history context only if conversion QA establishes the controlling page, and it correctly excludes family-relationship claims.
- The staged draft's hold recommendation is consistent with the reviewed evidence and does not attempt to promote a relationship, merge, or canonical identity claim.

## Scores

| field | score | judgment |
| --- | ---: | --- |
| source_quality_score | 0.34 | The nominal source is a CV, but only derivative text is available; the PDF and page image are unavailable for proof review. |
| conversion_confidence_score | 0.18 | Low because the same page has two competing derivative transcriptions, hash drift, and duplicate manifest metadata. |
| evidence_quantity_score | 0.42 | There is substantial derivative text, but it is not controlling evidence until the page-control conflict is resolved. |
| agreement_score | 0.18 | The assigned chunk and conversion job page Markdown materially disagree on page-5 content. |
| identity_confidence_score | 0.52 | Moderate for document-level `Dario Arturo Pulgar` from title/context; low for any canonical person attachment. |
| claim_probability | 0.45 | Work-history claims may belong somewhere in the CV, but exact page-5 claims are not reliably established. |
| relevance_level | direct | The review is directly tied to the assigned staged draft and its referenced page-5 evidence. |
| relevance_confidence | 0.98 | The reviewed files match the staged draft references. |
| canonical_readiness | not_ready | Do not promote, merge, rename, or create canonical claims from this draft. |

## Claim Judgment

The staged identity analysis is well supported as a conflict/hold note. It is not sufficient as proof for a canonical work-history fact, identity merge, parent-child relationship, spouse/child claim, or canonical person-page update. The most probable current interpretation is that both derivative texts may be CV material for the same document-level subject, but the page assignment or chunk manifest is corrupted.

## Next Action

Keep the item on hold for conversion QA. Restore or regenerate the missing source PDF/page image, reconcile the duplicate manifest records and hash drift, and visually compare physical page 5 against both derivative transcriptions before any work-history claim or identity-bridge review is promoted.
