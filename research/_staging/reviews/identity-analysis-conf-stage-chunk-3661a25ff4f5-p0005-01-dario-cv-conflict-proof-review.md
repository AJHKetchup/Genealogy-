---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260523053153899
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-conf-stage-chunk-3661a25ff4f5-p0005-01-dario-cv-conflict.md
staged_draft: research/_staging/identity-analysis/identity-analysis-conf-stage-chunk-3661a25ff4f5-p0005-01-dario-cv-conflict.md
review_status: hold
canonical_readiness: hold
---

# Proof Review: Page 5 Dario CV Identity Conflict

## Blockers

- The page-5 source image and transcription support occupational entries, but the page body does not state `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Smith`, a birth date, a family relationship, or any other direct identity bridge.
- The attribution to `Dario Arturo Pulgar` is document-level only, from the source title/path and conversion metadata. It should not be treated as a page-body identification.
- The canonical candidate `wiki/people/dario-arturo-pulgar-smith.md` remains unproved from page 5. Page 5 does not support normalizing `Dario Arturo Pulgar` to `Dario Arturo Pulgar-Smith`.
- The chunk metadata is not clean: the assigned/staged id is `CHUNK-3661a25ff4f5-P0005-01`, while the referenced chunk frontmatter says `chunk_id: CHUNK-f1fd1ec4cb77-P0005-01` and `converted_sha256: f1fd1ec4...`. This metadata drift should be reconciled before canonical promotion.
- The page-level conversion metadata still carries a QA flag saying a rendered page image was missing and rerun QA was needed. The image now exists and was visually checked for this review, but the stale QA flag should be cleared only by the proper conversion-QA workflow, not by this proof review.
- The final `SNC Lavalin Agriculture` entry continues off page 5 onto the next page. Do not promote a complete date range or complete duty description for that entry from page 5 alone.
- Hypotheses in the staged draft about child passenger, Pulgar-Arriagada, expropriation, Jose/Juana, and other Pulgar-line clusters are relevant anti-conflation context, but they are not proved by page 5 and were not independently revalidated as source claims in this review.

## Evidence Strengths

- The source packet, converted page, chunk text, and page image agree on the main page-5 occupational headings:
  - `1999` PROFONANPE, Peru, Consultant.
  - `1999` Television Trust for the Environment, London, England, Consultant.
  - `1998 - 1999` Arca Consulting/European Commission, Lesotho, Team Leader.
  - `1997-1998` Klohn Crippen Consultants, Huaraz, Peru, Socio-economic Consultant.
  - `SNC Lavalin Agriculture`, Maracaibo, Venezuela, Training Consultant.
- Visual comparison of `page-0005.jpg` supports the converted text for the headings and major body text on page 5.
- The staged draft correctly treats the evidence as a hold for canonical use and flags the identity risk around `Pulgar` versus `Pulgar-Smith`.
- The staged draft correctly avoids claiming parent, spouse, child, grandchild, or broader family relationships from page 5.

## Scores

| metric | value | rationale |
|---|---:|---|
| source_quality_score | 0.62 | A CV is useful for occupational chronology but is self-reported/derivative for proof purposes, and page 5 does not independently name the person. |
| conversion_confidence_score | 0.86 | The current page image is legible and matches the transcription well; the stale missing-image QA flag and metadata drift keep this below final-ready. |
| evidence_quantity_score | 0.54 | One page plus document-level metadata supports limited occupational evidence, not a robust identity bridge. |
| agreement_score | 0.72 | Source packet, conversion, chunk, and image agree on the page text; chunk-id/sha metadata conflict and overbroad identity hypotheses reduce agreement. |
| identity_confidence_score | 0.58 | Probable document-level attribution to `Dario Arturo Pulgar`, but page 5 does not prove the canonical `Pulgar-Smith` identity. |
| claim_probability | 0.60 | Plausible that the CV subject is the canonical candidate, but page 5 alone does not demonstrate it. The narrower claim that page 5 belongs to a CV titled for Dario Arturo Pulgar is stronger, about 0.82. |
| relevance_level | high | The draft directly addresses the nominated page-5 identity conflict and canonical attachment risk. |
| relevance_confidence | 0.93 | The reviewed materials are the assigned staged draft and its direct page-5 support files. |
| canonical_readiness | hold | Do not promote or attach to canonical person pages until identity bridge and metadata/QA issues are resolved. |

## Review Judgment

Hold. The staged draft's main conclusion is directionally sound: page 5 can support held CV-reported occupational chronology for the document-level subject `Dario Arturo Pulgar`, but it is not ready for canonical attachment to `Dario Arturo Pulgar-Smith` or any other Pulgar-line person.

The draft should be treated as an identity-risk analysis, not as proof of the wider hypotheses. Any statements about child passenger, Pulgar-Arriagada, expropriation, or Jose/Juana clusters need separate proof reviews against their own source packets and images before they are used for canonical identity decisions.

## Next Action

Keep the staged identity/conflict analysis on hold. Reconcile the chunk id/converted sha metadata, clear or rerun the page-image QA through the conversion-QA workflow, and perform a targeted CV identity review using identity-bearing CV pages before promoting page-5 occupations to any canonical page.
