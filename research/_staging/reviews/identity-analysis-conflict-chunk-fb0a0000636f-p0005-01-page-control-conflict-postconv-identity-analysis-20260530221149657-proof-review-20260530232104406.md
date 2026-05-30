---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260530232104406
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530221149657.md
staged_draft: research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530221149657.md
review_status: hold
canonical_readiness: not_ready
created_at: 2026-05-30T23:21:04Z
---

# Proof Review: Page-Control Conflict for CHUNK-fb0a0000636f-P0005-01

## Blockers

- The reviewed staged draft is `research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530221149657.md`.
- Page control is not reliable. The assigned chunk `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md` transcribes a 1979-1982 through 1970-1972 work-history sequence, while `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md` transcribes a different 1999 through 1997-1998 work-history sequence for page 5.
- The aggregate converted file contains both derivative sequences under the same conversion set, so it does not independently resolve which text controls physical page 5.
- The chunk manifest duplicates `CHUNK-fb0a0000636f-P0005-01` for the same page/path with different character counts and SHA-256 values.
- The source packet records hash drift between the chunk-recorded converted SHA-256 and the observed converted SHA-256.
- `raw/sources/CV of Dario Arturo Pulgar.pdf` is not present in this checkout, and the expected page image `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0005.jpg` is also not present. Independent visual proof review is therefore unavailable.
- The page-5 derivative text does not literally name a canonical person, a parent, spouse, child, sibling, or other kinship relationship. Any attachment to `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, Jose/Juana parent candidates, or Alexander John Heinz would be an identity bridge not proved by this page.

## Evidence Strengths

- The staged draft accurately identifies the main conversion conflict and properly recommends `hold_for_conversion_qa`.
- The source packet is consistent with the staged draft: it describes the same page-control dispute, the same missing page image problem, and the same document-level subject basis from the CV title/context.
- Both derivative transcriptions are internally coherent CV work-history text, and both appear relevant to a document titled `CV of Dario Arturo Pulgar`.
- The assigned chunk can support narrow work-history extraction only if later QA establishes that this chunk is the controlling physical page 5.
- The page-markdown file can support a different set of narrow work-history extraction only if later QA establishes that it is the controlling physical page 5.

## Scores

| field | score | judgment |
| --- | ---: | --- |
| source_quality_score | 0.35 | The source type is potentially strong because it is a CV, but the actual PDF and page image are absent, leaving only conflicting derivatives. |
| conversion_confidence_score | 0.20 | Duplicate manifest entries, hash drift, and contradictory page-5 transcriptions block confidence in the conversion state. |
| evidence_quantity_score | 0.45 | There are several relevant derivative files, but they conflict on the controlling text and no visible source can arbitrate them. |
| agreement_score | 0.30 | The staged draft and source packet agree about the hold, but the assigned chunk and page-markdown disagree materially. |
| identity_confidence_score | 0.55 | Moderate for document-level `Dario Arturo Pulgar` from title/context; low for any canonical person attachment from this page alone. |
| claim_probability | 0.42 | The claim that page 5 supports a specific work-history sequence is possible but not currently provable because two incompatible sequences are assigned to page 5. |
| relevance_level | high | The reviewed files directly address the assigned staged draft and page-control conflict. |
| relevance_confidence | 0.98 | The draft, packet, chunk, page-markdown, converted file, and manifest all reference the same conversion/chunk family. |
| canonical_readiness | not_ready | Do not promote facts, relationships, merges, redirects, page renames, or canonical identity conclusions from this staged draft. |

## Claim Judgment

The staged draft is supported as a hold/review-control analysis, not as promotable evidence for a canonical work-history fact or identity relationship. Its central assertion that page 5 has a conversion/page-control conflict is verified by the referenced derivative files and manifest. The draft's caution against merging or attaching the document-level CV subject to canonical Pulgar identities is warranted because the reviewed page evidence does not provide literal kinship, parentage, spouse/child, birth/death, or alias evidence.

The review cannot certify either derivative transcription as the physical page-5 text. Because the source PDF and expected page image are unavailable, the evidence remains derivative-only and internally conflicted.

## Next Action

Keep this item on hold for conversion QA. Restore or regenerate `page-0005.jpg`, make `raw/sources/CV of Dario Arturo Pulgar.pdf` available in the expected path, repair the duplicate chunk manifest/hash drift, and compare the visible physical page 5 against both derivative transcriptions. After page control is resolved, rerun proof review for the specific work-history claims and only then consider a separate identity-bridge review for any canonical person attachment.
