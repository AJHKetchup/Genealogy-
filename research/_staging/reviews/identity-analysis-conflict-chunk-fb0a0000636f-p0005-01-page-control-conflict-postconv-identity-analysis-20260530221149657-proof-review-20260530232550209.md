---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530221149657.md
worker: postconv-proof-review-20260530232550209
staged_draft: research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530221149657.md
review_status: hold
canonical_readiness: not_ready
created_at: 2026-05-30T23:25:50Z
---

# Proof Review: Page-Control Conflict for CHUNK-fb0a0000636f-P0005-01

## Blockers

- The exact staged draft reviewed is `research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530221149657.md`.
- The controlling page-5 evidence cannot be certified because `raw/sources/CV of Dario Arturo Pulgar.pdf` is not present in this checkout.
- The page image referenced by the conversion manifest, `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0005.jpg`, is not present, so visual proof review is unavailable.
- The assigned chunk at `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md` transcribes the `1979 - 1982` through `1970 - 1972` HABITAT/NFB/Chile Films/CITELCO sequence.
- The conversion job page Markdown at `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md` transcribes a different page-5 sequence: `1999`, `1998 - 1999`, and `1997-1998` PROFONANPE/TVE/Arca/Klohn Crippen/SNC Lavalin entries.
- The aggregate converted file contains both conflicting sequences under the same converted output, and the chunk manifest repeats `CHUNK-fb0a0000636f-P0005-01` for the same path/page with different character counts and hashes.
- The source packet reports converted-hash drift: recorded `fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0`; observed `da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288`.
- This evidence does not literally name parents, spouse, children, or other kinship relationships. It also does not bridge the document-level `Dario Arturo Pulgar` identity to a canonical person.

## Evidence Strengths

- The assigned chunk is internally coherent CV work-history text and is directly tied by front matter to `CHUNK-fb0a0000636f-P0005-01`, source `CV of Dario Arturo Pulgar.pdf`, and page 5.
- The conversion job page Markdown is also internally coherent CV work-history text and is explicitly labeled page 5 for the same source.
- The source packet accurately preserves the conflict instead of choosing between the derivative texts, and it correctly recommends `hold_for_conversion_qa`.
- The staged identity analysis correctly treats the question as a page-control and provenance problem first, not as a basis for merge, relationship, or canonical work-history promotion.
- The broader document-level identity `Dario Arturo Pulgar` is supported by the source title and conversion metadata, but not by literal text on the disputed page body.

## Scored Judgment

| field | score | judgment |
| --- | ---: | --- |
| source_quality_score | 0.35 | The described source is a CV and would be relevant if available, but the source PDF and page image are missing for this review. |
| conversion_confidence_score | 0.18 | Two derivative page-5 transcriptions conflict, the chunk manifest duplicates the same page/chunk id, and hash drift is documented. |
| evidence_quantity_score | 0.45 | There are multiple derivative texts and a source packet, but no controlling physical image/PDF proof. |
| agreement_score | 0.20 | The assigned chunk and conversion job page Markdown materially disagree about page-5 content. |
| identity_confidence_score | 0.50 | Moderate for document-level `Dario Arturo Pulgar` from title/context; low for attachment to any canonical person. |
| claim_probability | 0.40 | The professional-history content likely belongs somewhere in the CV, but the exact page-5 claim set cannot be selected from this evidence. |
| relevance_level | high | The reviewed files directly match the assigned staged draft and referenced page-control conflict. |
| relevance_confidence | 0.98 | File paths, chunk id, page reference, and source packet all align with the assignment. |
| canonical_readiness | 0.05 | Not ready for canonical promotion, merge, relationship claim, or wiki update. |

## Review Decision

Hold. The staged identity analysis is supported as a cautious page-control conflict analysis, but no work-history claim from this page should be promoted until conversion QA establishes which page-5 transcript is controlling. Do not merge or connect `Dario Arturo Pulgar` to `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, or Jose/Juana parent candidates from this evidence.

## Next Action

Restore or regenerate `page-0005.jpg`, make the source PDF available, reconcile the duplicate chunk manifest entries and converted-file hash drift, then compare the visible source page against both derivative transcriptions. After page control is certified, rerun proof review for the specific work-history claims and only then consider a separate identity-bridge review.
