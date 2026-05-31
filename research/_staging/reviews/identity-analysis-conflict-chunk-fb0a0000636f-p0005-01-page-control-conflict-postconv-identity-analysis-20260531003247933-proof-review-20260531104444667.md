---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260531104444667
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531003247933.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531003247933.md"
source_packet: "research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-hold-postconv-evidence-extraction-20260531000652338.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
canonical_readiness: hold
---

# Proof Review: Page-Control Conflict For CV Page 5

## Blockers First

1. Do not promote any page-5 occupational, place, identity, or relationship claim from this staged draft. Page control is unresolved: the assigned chunk gives a 1979-1970 HABITAT/NFB/Chile Films/CITELCO sequence, while `page-markdown/page-0005.md` gives a 1999-1997 PROFONANPE/TVE/Arca/Klohn/SNC Lavalin sequence.
2. The physical page image could not be checked from the referenced conversion job because `page-images/page-0005.jpg` and `extracted-images/page-0005.jpg` are absent locally, despite the source manifest listing a page-5 image path and hash.
3. The chunk manifest duplicates `CHUNK-fb0a0000636f-P0005-01` with different character counts and hashes, and the source packet records observed hash mismatches. That prevents treating either derivative transcription as controlling.
4. Page-local identity support is weak. The source title and metadata identify the document as the CV of `Dario Arturo Pulgar`, but the reviewed page-5 derivatives do not independently state `Dario Arturo Pulgar`, `Pulgar-Smith`, `Pulgar-Arriagada`, Alexander John Heinz, parents, spouse, child, or any kinship relationship.
5. The staged draft should be revised if reused where it says the current aggregate converted file contains only the 1979-1970 work-history text. In this review, the aggregate converted file was observed to contain both the 1999-1997 consulting sequence and the 1979-1970 work-history sequence in separate page-like sections.

## Evidence Strengths

- The staged identity analysis correctly identifies the issue as a page-control/provenance conflict rather than a resolved life-history contradiction.
- The assigned chunk literally supports the 1979-1982 United Nations Centre for Human Settlements (HABITAT), 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, and 1970-1972 CITELCO entries, but only as text in that derivative chunk.
- The conversion-job page Markdown literally supports the competing 1999 PROFONANPE and TVE entries, 1998-1999 Arca Consulting/European Commission entry, and 1997-1998 Klohn Crippen and SNC Lavalin entries, but only as text in that derivative page Markdown.
- The source packet accurately reports high uncertainty, absent local page images, duplicate manifest entries, and the need to hold promotion pending conversion QA.
- The document-level title is relevant to the Pulgar family research question, but it is not enough to bridge this page to `Dario Arturo Pulgar-Smith` or any Pulgar-Arriagada candidate.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 6/10 for a named CV source in the repository; reduced because the physical page image was unavailable for this review |
| conversion_confidence_score | 1.5/10 for page 5 control; 8/10 only for the fact that each derivative text is internally readable |
| evidence_quantity_score | 2/10 for identity and relationship claims; 4/10 for staged occupational leads after page-control repair |
| agreement_score | 1/10 between the assigned chunk and conversion-job page Markdown for page 5; 3/10 across the aggregate conversion because both competing sequences appear |
| identity_confidence_score | 5/10 for document-level `Dario Arturo Pulgar`; 2/10 for connection to `Dario Arturo Pulgar-Smith`; 1/10 or lower for Pulgar-Arriagada or Jose/Juana relationship candidates |
| claim_probability | 0.75 that this is a real page-control conflict; 0.50 that the CV source concerns document-level `Dario Arturo Pulgar`; 0.15 or lower for any canonical identity merge; 0.05 for any relationship claim |
| relevance_level | high |
| relevance_confidence | 0.90 |
| canonical_readiness | hold / not ready |

## Review Finding

The staged draft is supported as a hold recommendation. Its central blocker is real: the available derivatives disagree on what controls page 5, and the local evidence reviewed here does not include a page image that can resolve the conflict.

No reviewed text supports changing a name reading to `Dario Arturo Pulgar-Smith`, merging this CV subject with a Pulgar-Arriagada person, or adding a parent, spouse, child, grandchild, or Alexander John Heinz relationship. Any such claim would be a relationship or identity jump from document context rather than literal page-5 support.

## Next Action

Hold for conversion QA. Restore or re-render physical page 5 from `raw/sources/CV of Dario Arturo Pulgar.pdf`, compare it directly against the assigned chunk and `page-markdown/page-0005.md`, reconcile the duplicate manifest rows and hash mismatches, then run a separate identity-bridge proof review before attaching any page-5 CV content to a canonical person page.
