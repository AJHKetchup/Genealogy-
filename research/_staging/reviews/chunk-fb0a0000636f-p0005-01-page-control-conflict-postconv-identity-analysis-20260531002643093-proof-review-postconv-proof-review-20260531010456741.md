---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260531010456741
task_id: "proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531002643093.md"
staged_draft: "research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531002643093.md"
source_packet: "research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-hold-postconv-evidence-extraction-20260530234356813.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
conversion_job_page_markdown: "raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md"
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
canonical_readiness: not_ready
---

# Proof Review: CV Page 5 Page-Control Conflict

## Blockers First

1. Do not promote page-5 occupational, chronology, place, identity, or relationship claims from this staged draft. The referenced local derivatives disagree about what text controls physical page 5.
2. The assigned chunk transcribes a 1979-1970 work-history page ending with `EDUCATION`, while the conversion-job page Markdown for page 5 transcribes a 1999-1997 consulting-work page ending mid-sentence. These cannot both be treated as the controlling page-5 transcription.
3. The page image referenced in the conversion manifest, `page-images/page-0005.jpg`, is not available at the expected local path in this pass. No `extracted-images/page-0005.jpg` file is available either.
4. The chunk manifest duplicates `CHUNK-fb0a0000636f-P0005-01` with different character counts and hashes. The source packet also records observed hash drift for the converted file and chunk, so derivative provenance is not stable enough for canonical use.
5. No reviewed page-5 body independently states a family relationship, parentage, spouse, child, grandchild, or identity bridge to `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, `Dario Pulgar-Arriagada`, or Jose/Juana parent candidates.

## Evidence Strengths

- The source title, source path, source packet, converted file, assigned chunk, and conversion-job page Markdown consistently identify the document as `CV of Dario Arturo Pulgar`.
- Both competing derivative texts are internally plausible CV work-history transcriptions and contain typed single-column employment entries.
- The assigned chunk and source packet agree on the 1979-1970 sequence: HABITAT in Nairobi, National Film Board of Canada in Montreal, Chile Films in Santiago, and CITELCO in Santiago.
- The aggregate converted file and conversion-job page Markdown agree on the 1999-1997 page-5 sequence: PROFONANPE in Peru, TVE in London, Arca Consulting/European Commission in Lesotho, Klohn Crippen Consultants in Huaraz, and SNC Lavalin Agriculture in Maracaibo.
- The staged identity analysis correctly recommends `hold_for_conversion_qa` and does not ask for canonical promotion.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 5/10 for a CV source identified by local metadata; lowered because the physical page image was unavailable for this review |
| conversion_confidence_score | 2/10 for page-5 control; 7/10 only for the literal readability of each separate derivative transcription |
| evidence_quantity_score | 3/10 for identity or relationship proof; 5/10 for document-level CV context after page control is resolved |
| agreement_score | 2/10 across page-5 derivatives; 8/10 within each isolated derivative's own text |
| identity_confidence_score | 5.5/10 for document-level attribution to `Dario Arturo Pulgar` from title/path metadata; 2/10 or lower for any canonical same-person bridge from this page |
| claim_probability | 0.45 that any specific page-5 occupational sequence is currently safe to cite as page 5; 0.75 that both texts are CV-context material somewhere in the local conversion set; 0.10 or lower for relationship claims |
| relevance_level | high |
| relevance_confidence | 0.95 |
| canonical_readiness | not_ready |

## Review Finding

The staged draft is supported as a hold finding. It accurately identifies a page-control conflict and correctly treats identity expansion and relationship inference as unsafe.

The only narrow claim supported without further QA is that local metadata identifies the source as a CV for `Dario Arturo Pulgar`. The page-5 body itself is not reliable enough to support canonical work-history claims, and it does not support a same-person merge or family relationship.

## Next Action

Keep this item on `hold_for_conversion_qa`. Restore or certify the physical page-5 image, reconcile the duplicate chunk-manifest entries and hash drift, then decide which page-5 transcription controls. After that, rerun proof review only on the surviving work-history claims and run a separate identity-bridge review before attaching the document-level `Dario Arturo Pulgar` to any canonical person.
