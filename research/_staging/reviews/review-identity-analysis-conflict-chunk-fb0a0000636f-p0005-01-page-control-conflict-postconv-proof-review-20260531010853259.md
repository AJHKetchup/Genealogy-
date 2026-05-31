---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260531010853259
task_id: proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531002643093.md
staged_draft: research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531002643093.md
reviewed_source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-hold-postconv-evidence-extraction-20260530234356813.md
source: raw/sources/CV of Dario Arturo Pulgar.pdf
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
conversion_job_page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
review_status: hold
canonical_readiness: hold_for_conversion_qa
source_quality_score: 0.48
conversion_confidence_score: 0.20
evidence_quantity_score: 0.42
agreement_score: 0.18
identity_confidence_score: 0.55
claim_probability: 0.49
relevance_level: direct
relevance_confidence: 0.99
created_at: 2026-05-31T01:08:53Z
---

# Proof Review: Page 5 Control Conflict

## Blockers First

- Decision: `hold_for_conversion_qa`; do not promote any page-5 occupational, place, chronology, identity-bridge, or relationship claim from this draft.
- The exact reviewed draft is `research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531002643093.md`.
- Page control is unresolved. The assigned chunk preserves a `1979 - 1982` through `1970 - 1972` work-history page ending at `EDUCATION`, while the conversion-job page Markdown for page 5 preserves a materially different `1999` through `1997-1998` consulting-work page.
- The recorded page image path `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0005.jpg` is listed in the conversion manifest, but the file is not currently present locally. No extracted page-5 image was present either.
- The chunk manifest duplicates `CHUNK-fb0a0000636f-P0005-01` with conflicting character counts and hashes. Current observed hashes also differ from recorded metadata for both the aggregate converted file and the assigned chunk.
- The page-5 body, under either derivative reading, does not independently state a family relationship, parent, spouse, child, grandchild, or a bridge from document-level `Dario Arturo Pulgar` to canonical `Dario Arturo Pulgar-Smith`.

## Evidence Strengths

- The source packet and source/manifest metadata consistently identify the document title/source as `CV of Dario Arturo Pulgar`.
- The assigned chunk is internally readable and supports only literal work-history text if later certified as the controlling physical page 5: HABITAT in Nairobi, National Film Board of Canada in Montreal, Chile Films in Santiago, and CITELCO in Santiago.
- The conversion-job page Markdown is also internally readable and supports only literal work-history text if later certified as the controlling physical page 5: PROFONANPE in Peru, TVE in London, Arca Consulting/European Commission in Lesotho, Klohn Crippen Consultants in Huaraz, and SNC Lavalin Agriculture in Maracaibo.
- Canonical `wiki/people/dario-arturo-pulgar-smith.md` appropriately warns against automatic attachment of Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records without identity review; this draft does not overcome that warning.

## Scored Judgment

| field | score | judgment |
| --- | ---: | --- |
| source_quality_score | 0.48 | The document-level source is a named CV PDF, but the proof item depends on conflicted derivatives and a missing page image. |
| conversion_confidence_score | 0.20 | Page image unavailable, derivative page text conflicts, duplicate manifest entries exist, and observed hashes do not match recorded metadata. |
| evidence_quantity_score | 0.42 | There is enough derivative text to identify the conflict, but not enough controlled evidence to select the true page-5 transcription. |
| agreement_score | 0.18 | The two page-5 derivative readings materially disagree on dates, organizations, locations, and page content. |
| identity_confidence_score | 0.55 | Moderate only for document-level attribution to the CV subject named in the source title; low for any canonical same-person merge or relationship attachment. |
| claim_probability | 0.49 | Either work-history sequence may belong somewhere in the CV, but the claim that either sequence is the controlling physical page 5 remains unproved. |
| relevance_level | direct | The reviewed evidence directly concerns the staged page-control conflict. |
| relevance_confidence | 0.99 | The staged draft, packet, chunk, converted file, and page Markdown all reference the same CV/page-5 control problem. |
| canonical_readiness | hold_for_conversion_qa | Not ready for canonical facts, relationships, identity merges, name-variant promotion, or wiki updates. |

## Next Action

Keep the staged draft on hold. Conversion/source QA should restore or regenerate the authoritative page-5 image, verify it against the manifest hash if possible, reconcile the duplicate chunk manifest entries and stale hashes, and then certify whether the controlling page-5 transcription is the 1999-1997 consulting page or the 1979-1970 HABITAT/NFB/Chile Films/CITELCO page. After that, rerun proof review only for the surviving literal work-history claims and handle any `Dario Arturo Pulgar` to `Dario Arturo Pulgar-Smith` attachment as a separate identity-bridge review.
