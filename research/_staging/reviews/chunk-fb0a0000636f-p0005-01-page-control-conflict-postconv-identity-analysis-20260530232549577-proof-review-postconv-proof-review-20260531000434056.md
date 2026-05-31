---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260531000434056
task_id: "proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530232549577.md"
staged_draft: "research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260530232549577.md"
source_packet: "research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-hold-postconv-evidence-extraction-20260530224457988.md"
conflict_candidate: "research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260530224457988.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: CV Page 5 Page-Control Conflict

## Blockers First

1. Keep this staged identity analysis on hold. The assigned chunk and the conversion-job page Markdown give materially different page-5 transcriptions, so neither work-history sequence should be promoted as controlling page-5 evidence.
2. The page image referenced by the conversion-job manifest, `page-images/page-0005.jpg`, is absent in the local workbench. I did not rerun conversion or regenerate page images.
3. The chunk manifest duplicates `CHUNK-fb0a0000636f-P0005-01`, and the converted-file hash recorded in the chunk (`fb0a0000636f...`) differs from the observed converted-file hash (`da9ec0c3...`).
4. Page 5, in either derivative text reviewed here, does not state a family relationship, a parent/child link, `Pulgar-Smith`, `Pulgar-Arriagada`, `Jose`, `Juana`, or Alexander John Heinz.
5. Canonical identity attachment to `Dario Arturo Pulgar-Smith` or any Pulgar-Arriagada/Jose/Juana candidate is not supported by this page-control evidence alone.

## Evidence Strengths

- The staged draft accurately reports the core conflict: the assigned chunk begins with `1979 - 1982` and HABITAT in Nairobi, while the conversion-job page Markdown begins with `1999` and PROFONANPE in Peru.
- The source packet and conflict candidate both preserve the same hold recommendation and correctly treat the conflict as a conversion QA problem rather than an identity conclusion.
- The document-level title and paths consistently identify the broader source as `CV of Dario Arturo Pulgar`, which gives moderate source-level relevance for a later CV-subject review.
- The absence of relationship language is consistent across the checked derivative texts.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 6/10 |
| conversion_confidence_score | 2/10 |
| evidence_quantity_score | 3/10 |
| agreement_score | 2/10 for page-5 work-history content; 7/10 for the existence of a page-control conflict |
| identity_confidence_score | 6/10 for document-level attribution to `Dario Arturo Pulgar`; 2/10 or lower for same-person attachment to Pulgar-Smith or Pulgar-Arriagada candidates from this page |
| claim_probability | 0.92 that page-5 claims should remain held for conversion QA; 0.70 that the CV source is document-level evidence for a Dario Arturo Pulgar; 0.15 or lower for any relationship or merge claim from this page |
| relevance_level | high |
| relevance_confidence | 0.90 |
| canonical_readiness | hold_for_conversion_qa |

## Review Finding

The staged draft is supported as a hold analysis. Its strongest claim is not a biographical fact, but the procedural claim that page-5 evidence is not canonically usable until conversion QA chooses the controlling transcription.

No checked derivative source supports promoting the 1979-1970 work-history sequence, the 1999-1997 work-history sequence, a same-person merge, or a family relationship. The source title supports only a cautious document-level association with `Dario Arturo Pulgar`, not a page-local identity bridge.

## Next Action

Run conversion QA on the source page before any claim promotion: restore or inspect the physical page image/PDF page, decide whether the assigned chunk or the page-markdown transcription controls page 5, and repair the manifest/hash drift. After that, review document-level identity separately before attaching the CV subject to any canonical person page.
