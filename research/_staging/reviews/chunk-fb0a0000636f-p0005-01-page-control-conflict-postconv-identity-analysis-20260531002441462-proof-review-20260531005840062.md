---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260531005840062
task_id: "proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531002441462.md"
staged_draft: "research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531002441462.md"
source_packet: "research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-hold-postconv-evidence-extraction-20260531000652338.md"
conflict_draft: "research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260531000652338.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
conversion_job_page_markdown: "raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md"
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
canonical_readiness: hold
---

# Proof Review: CV Page 5 Page-Control Conflict

## Blockers First

1. Do not promote either page-5 occupational sequence. The assigned chunk and the aggregate converted file preserve a 1979-1970 work-history sequence, while the conversion-job `page-markdown/page-0005.md` preserves a different 1999-1997 consulting-work sequence for the same page number.
2. Page control is not certified. The chunk manifest repeats `CHUNK-fb0a0000636f-P0005-01` for `page-0005-chunk-01.md` with different character counts and hashes, and the source packet reports observed hash drift from recorded metadata.
3. No physical page-5 image was found in the reviewed conversion-job artifacts. The locally present page-5 artifacts are derivative Markdown/JSON/work-order files, so this pass cannot visually decide which transcription matches the source page.
4. The checked page-5 bodies do not independently name `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, `Dario Pulgar-Arriagada`, Jose/Juana parent candidates, or Alexander John Heinz. The `Dario Arturo Pulgar` attribution is document/title metadata, not page-body evidence.
5. No relationship claim is supported by this page-control packet. The checked derivatives state no parents, spouse, child, grandchild, household, or other kinship relationship.

## Evidence Strengths

- The staged identity analysis correctly treats the issue as a conversion/page-control conflict and recommends `hold_for_conversion_qa`; that recommendation is supported by the reviewed local files.
- The assigned chunk literally supports the 1979-1982 HABITAT, 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, and 1970-1972 CITELCO text if, and only if, conversion QA later certifies it as the controlling page.
- The conversion-job page Markdown literally supports the 1999 PROFONANPE and TVE entries, 1998-1999 Arca Consulting/European Commission entry, and 1997-1998 Klohn Crippen/SNC Lavalin entries if, and only if, conversion QA later certifies it as the controlling page.
- The source packet and conflict draft accurately disclose the conflict, missing local page imagery, duplicate manifest entries, and hash drift rather than masking those weaknesses.
- Both competing readings are plausible CV work-history material for a document titled `CV of Dario Arturo Pulgar`; the defect is control and attribution, not obvious topical irrelevance.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 4/10 for current review context; the named source is a CV, but only conflicting derivatives were checked for page 5 |
| conversion_confidence_score | 2/10 because page-5 derivatives conflict, manifest entries duplicate, hashes drift, and no page image was available for visual control |
| evidence_quantity_score | 4/10 for general work-history context; 1/10 for identity-bridge or relationship proof |
| agreement_score | 2/10 between page-5 derivatives; 8/10 that the staged packet, conflict draft, and identity analysis agree a hold is required |
| identity_confidence_score | 5/10 for document-level attribution to the CV subject named in source metadata; 2/10 for attachment to canonical `Dario Arturo Pulgar-Smith`; 1/10 or less for Pulgar-Arriagada, Jose/Juana, or Alexander John Heinz connections |
| claim_probability | 0.50 that either occupational sequence belongs somewhere in the CV; 0.20 that either can currently be cited as controlling page-5 evidence; 0.05 for any relationship claim from this packet |
| relevance_level | high |
| relevance_confidence | 0.96 |
| canonical_readiness | hold / not ready |

## Review Finding

The staged draft is supported as a hold. Its main claim, that page-5 control is corrupted or unresolved, is materially supported by the checked source packet, conflict draft, assigned chunk, aggregate converted file, conversion-job page Markdown, and chunk manifest. The proof problem is not a promoted/not-promoted binary; readable occupational text exists, but the controlling page transcription is not established.

This review does not support changing a name reading, merging `Dario Arturo Pulgar` with `Dario Arturo Pulgar-Smith`, attaching the CV subject to `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, `Dario Pulgar-Arriagada`, Jose/Juana parent clusters, or creating any relationship to Alexander John Heinz.

## Next Action

Keep this item on `hold_for_conversion_qa`. Conversion QA should locate or regenerate an authoritative physical page-5 image or page-image equivalent, decide whether the 1999-1997 or 1979-1970 transcription controls physical page 5, and reconcile the duplicate manifest/hash drift. After page control is certified, rerun proof review only for the surviving work-history claims, then perform a separate identity-bridge review before any canonical merge, relationship, or wiki action.
