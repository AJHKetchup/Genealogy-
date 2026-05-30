---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260530233509292
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530221149657.md
staged_draft: research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530221149657.md
review_status: hold
canonical_readiness: not_ready
created_at: 2026-05-30T23:35:09Z
---

# Proof Review: Page-Control Identity Analysis

## Blockers

- The staged draft is correctly centered on a page-control conflict, but no canonical claim should be promoted from it. The source PDF `raw/sources/CV of Dario Arturo Pulgar.pdf` is not present in this checkout, and the referenced page image `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0005.jpg` is also absent.
- The assigned chunk `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md` transcribes the 1979-1982 HABITAT through 1970-1972 CITELCO sequence, while the conversion job page Markdown `page-markdown/page-0005.md` transcribes a different 1999 through 1997-1998 PROFONANPE/TVE/Arca/Klohn Crippen/SNC Lavalin sequence.
- The chunk manifest repeats `CHUNK-fb0a0000636f-P0005-01` for the same path/page with different character counts and hashes. The source packet also records converted-file hash drift: recorded `fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0`, observed `da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288`.
- The page body in the checked derivative files does not literally name `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Darío Pulgar Arriagada`, parents, spouse, children, or any kinship relationship. Any attachment to a canonical person is therefore document-title/context inference only.

## Evidence Strengths

- The review could verify the staged draft against the referenced source packet, assigned chunk, conversion job page Markdown, aggregate converted file, and chunk manifest without editing those files.
- Both competing derivative transcriptions are coherent curriculum-vitae work-history text for a document titled `CV of Dario Arturo Pulgar`; the conflict appears to be conversion/page-control provenance, not a genealogical relationship contradiction.
- The staged draft appropriately recommends `hold_for_conversion_qa` and avoids merging similarly named Pulgar identities or creating Jose/Juana parent claims from this page.
- The assigned chunk has readable, internally consistent work-history text, but it cannot control page 5 until the physical page image/PDF and manifest/hash conflict are resolved.

## Scoring

| field | score | judgment |
| --- | ---: | --- |
| source_quality_score | 0.28 | The described source is a CV, useful for work history but self-reported and currently unavailable for direct inspection. |
| conversion_confidence_score | 0.18 | Low because page-5 derivatives disagree, the page image/PDF are absent, and hash/manifest metadata conflicts persist. |
| evidence_quantity_score | 0.42 | Several derivative files support the existence of a conflict, but none provide independent visual control. |
| agreement_score | 0.22 | Low agreement between assigned chunk and page Markdown; agreement is limited to both being plausible CV work-history text. |
| identity_confidence_score | 0.50 | Moderate for document-level `Dario Arturo Pulgar` from title/context; low for `Dario Arturo Pulgar-Smith` or other canonical attachments. |
| claim_probability | 0.44 | The conflict claim is well supported, but the truth of any specific page-5 work-history claim remains unresolved. |
| relevance_level | 0.98 | Directly relevant to the assigned staged identity-analysis draft and its referenced evidence. |
| relevance_confidence | 0.96 | The reviewed files match the staged draft paths and task scope. |
| canonical_readiness | 0.05 | Not ready for canonical facts, relationships, merges, page renames, or promotion. |

## Review Judgment

Hold. The staged draft's caution is supported: the available files prove a serious page-control and provenance problem, not a promotable identity or relationship conclusion. The draft should remain a QA-blocking identity/conflict analysis until the original PDF or page image is available and the manifest/hash drift is reconciled.

## Next Action

Restore or regenerate the page-5 image and make the source PDF available, then compare the visible physical page 5 with both derivative transcriptions. After the controlling page text is established, rerun proof review for the work-history claims and only then run a separate identity-bridge review for any proposed attachment to `Dario Arturo Pulgar-Smith` or other Pulgar identity clusters.
