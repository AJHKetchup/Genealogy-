---
type: proof_review_note
role: claim_reviewer
worker: postconv-proof-review-20260531045655868
task_id: proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531015428195.md
staged_draft: research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531015428195.md
reviewed_source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-revision-postconv-evidence-extraction-20260531010209483.md
reviewed_conflict_note: research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260531010209483.md
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
conversion_job_page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
source: raw/sources/CV of Dario Arturo Pulgar.pdf
status: hold
source_quality_score: 0.30
conversion_confidence_score: 0.20
evidence_quantity_score: 0.35
agreement_score: 0.15
identity_confidence_score: 0.45
claim_probability: 0.49
relevance_level: high
relevance_confidence: 0.99
canonical_readiness: hold_for_conversion_qa
created_at: 2026-05-31T04:56:55Z
---

# Proof Review: Page 5 Control Conflict

## Blockers First

- The staged draft is supported as a hold recommendation. It should not be promoted because page control is unresolved: the assigned chunk transcribes a 1979-1970 work-history page, while the conversion-job page Markdown for page 5 transcribes a materially different 1999-1997 consulting-work page.
- The recorded source PDF `raw/sources/CV of Dario Arturo Pulgar.pdf` was not present at the referenced path during review. The manifest-listed `page-images/page-0005.jpg` was also not present, so the visible physical page could not be checked.
- The chunk manifest contains duplicate `CHUNK-fb0a0000636f-P0005-01` entries pointing to the same chunk path with different metadata, and observed hashes for the converted file and chunk do not match the recorded values cited in the source packet.
- The page-5 evidence does not literally name `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, Jose/Juana parent candidates, or any family relationship. Same-person, duplicate-person, name-variant, and relationship claims must remain unmade from this page.
- The source title/path supports only a document-level association with `Dario Arturo Pulgar`; it does not by itself bridge the CV subject to any canonical person while page control and identity evidence remain unresolved.

## Evidence Strengths

- The staged draft accurately reports the main derivative conflict. The assigned chunk contains entries for HABITAT, National Film Board of Canada, Chile Films, and CITELCO, ending at `EDUCATION`.
- The conversion-job page Markdown for the same page number contains PROFONANPE, Television Trust for the Environment, Arca Consulting/European Commission, Klohn Crippen Consultants, and SNC Lavalin Agriculture entries.
- The aggregate converted file contains both the 1999-1997 consulting sequence and the 1979-1970 work-history sequence, which strengthens the conclusion that the derivatives cannot currently identify the controlling physical page-5 text.
- The staged draft's caution against identity merge or relationship promotion is well supported by absence of kinship language or name-bridge evidence in the checked page-5 materials.

## Scoring

| field | score | judgment |
| --- | ---: | --- |
| source_quality_score | 0.30 | The source is a CV derivative with a named document path, but the original PDF and page image were unavailable for direct verification. |
| conversion_confidence_score | 0.20 | Competing page-5 derivatives, duplicate manifest entries, and hash drift make conversion control low. |
| evidence_quantity_score | 0.35 | There is enough derivative text to identify the conflict, but not enough controlled evidence to prove page-5 facts. |
| agreement_score | 0.15 | The two page-5 derivative bodies disagree substantially. |
| identity_confidence_score | 0.45 | Moderate-low for the document-level `Dario Arturo Pulgar` association; low for attachment to any canonical identity. |
| claim_probability | 0.49 | The claim that this is a conversion/page-control conflict is high, but the underlying page-5 factual claims cannot be selected. |
| relevance_level | high | The reviewed files directly concern the assigned staged draft and page-5 control issue. |
| relevance_confidence | 0.99 | All checked evidence is within the staged draft's cited source packet, chunk, converted file, or conversion job. |
| canonical_readiness | hold_for_conversion_qa | Not ready for canonical facts, relationships, identity merges, name variants, or page-5 chronology claims. |

## Next Action

Keep the staged draft on `hold_for_conversion_qa`. Restore or verify the authoritative source PDF or page-5 image, reconcile duplicate chunk manifest entries and hash drift, and certify which page-5 transcription controls the physical source. After conversion QA, rerun proof review on the surviving literal claims before considering any separate identity-bridge review for `Dario Arturo Pulgar` against canonical Pulgar-Smith or Pulgar-Arriagada candidates.
