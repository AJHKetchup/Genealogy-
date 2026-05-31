---
type: proof_review_note
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260531111832755
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531020516022.md
staged_draft: research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531020516022.md
source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-revision-postconv-evidence-extraction-20260531004750573.md
relationship_note: research/_staging/relationships/relationship-negative-chunk-fb0a0000636f-p0005-01-no-kinship-revision-hold-postconv-evidence-extraction-20260531004750573.md
conversion_review_note: research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260531004750573.md
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
conversion_job_page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
source_quality_score: 0.28
conversion_confidence_score: 0.10
evidence_quantity_score: 0.45
agreement_score: 0.18
identity_confidence_score: 0.34
claim_probability: 0.32
relevance_level: direct
relevance_confidence: 1.00
canonical_readiness: blocked
review_decision: hold_for_conversion_qa
---

# Proof Review: CV Page 5 Control Conflict

## Blockers First

1. The staged draft is not canonically ready. It correctly identifies a page-control and derivative-integrity conflict, but the controlling physical page 5 cannot be selected from the available local evidence.
2. The recorded source PDF `raw/sources/CV of Dario Arturo Pulgar.pdf` is absent locally. The named page image `page-images/page-0005.jpg` and named extracted image path are also absent, so the physical page cannot be visually verified.
3. The assigned chunk contains a 1979-1970 work-history page ending with `EDUCATION`; the conversion-job `page-markdown/page-0005.md` contains a different 1999-1997 consulting-work page. Both readings cannot be accepted as the controlling transcription for the same physical page 5 without QA repair.
4. The chunk manifest lists `CHUNK-fb0a0000636f-P0005-01` twice for `page-0005-chunk-01.md`, with different character counts and hashes. Observed hashes for the aggregate converted file and the assigned chunk differ from recorded metadata.
5. Page-body identity support is weak. Neither derivative page-5 reading independently names `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, or `Dario Pulgar Arriagada`; `Dario Arturo Pulgar` comes from source title/path context.
6. No relationship claim is supported. The assigned derivative chunk states no parents, spouse, children, siblings, household members, or kinship language, and that negative relationship note cannot be generalized to the whole CV while page control is disputed.

## Evidence Strengths

- Literal local support exists for the assigned chunk's 1979-1970 work-history text: HABITAT in Nairobi, National Film Board of Canada in Montreal, Chile Films in Santiago, and CITELCO in Santiago.
- Literal local support also exists for the competing job page Markdown's 1999-1997 consulting-work text: PROFONANPE in Peru, TVE in London, Arca Consulting/European Commission in Lesotho, Klohn Crippen in Huaraz, and SNC Lavalin Agriculture in Maracaibo.
- The staged draft accurately preserves uncertainty instead of forcing an identity merge or source transcription correction.
- The relationship risk is handled conservatively: the draft treats name overlap as a bridge-check target only, not as proof that `Dario Arturo Pulgar` is the same person as any Pulgar-Smith or Pulgar-Arriagada candidate.

## Scores

| Category | Score / value | Review judgment |
| --- | ---: | --- |
| source_quality_score | 0.28 | The cited source is a derivative CV cluster with title/path context, but the original PDF and page image are unavailable for this task. |
| conversion_confidence_score | 0.10 | Conflicting page-5 derivatives, duplicate manifest entries, and hash drift block reliance on page assignment. |
| evidence_quantity_score | 0.45 | There is enough derivative text to document the conflict, but not enough authoritative evidence to resolve it. |
| agreement_score | 0.18 | The assigned chunk and conversion-job page Markdown materially disagree on page-5 content. |
| identity_confidence_score | 0.34 | Document title/path point to `Dario Arturo Pulgar`, but page body lacks direct name or bridge identifiers to canonical candidates. |
| claim_probability | 0.32 | Probability that any specific page-5 occupational claim controls physical page 5 remains low until image/PDF QA. |
| relevance_level | direct | The review directly concerns the exact staged draft and its referenced artifacts. |
| relevance_confidence | 1.00 | The reviewed files are the staged draft's cited verification context. |
| canonical_readiness | blocked | No canonical fact, relationship, merge, rename, or identity attachment should be promoted. |

## Claim-Level Probability

| Claim or inference | Probability | Disposition |
| --- | ---: | --- |
| The assigned chunk locally contains the 1979-1970 work-history text described in the staged draft. | 0.96 | Supported as derivative text only. |
| The conversion-job page Markdown locally contains the 1999-1997 consulting-work text described in the staged draft. | 0.96 | Supported as derivative text only. |
| The assigned chunk is the controlling transcription for physical page 5. | 0.32 | Hold for conversion QA. |
| The conversion-job page Markdown is the controlling transcription for physical page 5. | 0.34 | Hold for conversion QA. |
| Page 5 proves a same-person bridge to `Dario Arturo Pulgar-Smith`. | 0.20 | Not supported by this page evidence. |
| Page 5 proves a same-person bridge to `Dario Jose Pulgar-Arriagada` or `Dario/Dario Pulgar Arriagada`. | 0.04 | Not supported by this page evidence. |
| Page 5 supports any parent, spouse, child, or kinship relationship claim. | 0.01 | Not supported. |

## Source Reliability And Identity Risk

The source title/path is useful for identifying the CV cluster as `Dario Arturo Pulgar`, but it is not a substitute for page-level control or identity proof. The body of the disputed page provides occupational and place chronology only. It does not contain the surname forms, family relationships, birth/death facts, spouse/child identifiers, or other bridge evidence needed to connect this CV page to a canonical person.

Identity risk is high if this page is used for merging because the proof rests mainly on name-token overlap plus document context. Relationship-jump risk is also high: the negative relationship note is valid only for the currently assigned derivative chunk and should not be interpreted as evidence about the full CV or the competing page-5 transcription.

## Next Action

Keep this staged draft on `hold_for_conversion_qa`. Conversion QA should restore or regenerate authoritative access to the original PDF or rendered page image for page 5, reconcile the duplicate chunk manifest entries and hash drift, and certify which derivative transcription controls physical page 5. After that repair, a separate identity-bridge proof review can compare the full CV cluster against Pulgar-Smith and Pulgar-Arriagada candidates using direct identifiers rather than name overlap alone.

No raw sources, converted Markdown, chunks, source packets, relationship notes, claims, or canonical wiki pages were edited.
