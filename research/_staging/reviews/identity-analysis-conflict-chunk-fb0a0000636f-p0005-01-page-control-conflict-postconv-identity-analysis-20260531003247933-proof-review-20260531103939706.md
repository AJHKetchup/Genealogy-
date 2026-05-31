---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531003247933.md
worker: postconv-proof-review-20260531103939706
staged_draft: research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531003247933.md
review_status: hold
canonical_readiness: not_ready
created: 2026-05-31
---

# Proof Review: Page 5 CV Identity/Control Conflict

## Blockers

- Exact staged draft reviewed: `research/_staging/identity-analysis/identity-analysis-conflict-chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531003247933.md`.
- Canonical readiness is `not_ready`. No promotion or canonical update is supported from this staged draft.
- Page control is unresolved. The assigned chunk `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md` transcribes the 1979-1970 HABITAT/NFB/Chile Films/CITELCO sequence, while `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md` transcribes the 1999-1997 PROFONANPE/TVE/Arca/Klohn Crippen/SNC Lavalin sequence.
- The aggregate converted file contains both competing sequences in separate page sections, so it does not by itself certify which text controls physical page 5.
- Local page image checks found `page-images/page-0005.jpg` and `extracted-images/page-0005.jpg` absent, despite the source manifest listing a page-5 image path and hash.
- Hash control is broken. The source packet's observed converted hash `da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288` and observed chunk hash `d6ea4f611ee03000c11cbba63246e95b55f8a421fcbc87d0d667e91f5c8d0b8d` were reproduced, and both differ from recorded manifest or chunk metadata.
- Page-local identity support is absent. The competing page bodies do not independently state `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, a Smith surname, Arriagada variant, parents, spouse, child, grandchild, or Alexander John Heinz. The subject name comes from document-level title/path metadata only.
- The staged draft includes useful hypothesis scores, but it does not provide the required proof-review field names `source_quality_score`, `conversion_confidence_score`, `evidence_quantity_score`, `agreement_score`, `identity_confidence_score`, `relevance_level`, and `relevance_confidence`; this review supplies them below.

## Evidence Strengths

- The staged draft's central hold recommendation is supported by the referenced source packet, assigned chunk, competing page Markdown, aggregate converted file, and manifests.
- The assigned derivative chunk clearly supports only a narrow derivative reading of the 1979-1970 work-history sequence: HABITAT in Nairobi, NFB in Montreal, Chile Films in Santiago, and CITELCO in Santiago.
- The conversion-job page Markdown clearly supports only a competing derivative reading of the 1999-1997 consulting sequence: PROFONANPE in Peru, TVE in London, Arca Consulting/European Commission in Lesotho, Klohn Crippen in Huaraz, and SNC Lavalin Agriculture in Maracaibo.
- The source packet correctly warns that no family relationship or canonical identity attachment should be made from this evidence before page-control repair and a separate identity-bridge proof review.

## Scores

| field | score | rationale |
| --- | ---: | --- |
| source_quality_score | 0.62 | A CV is direct for occupational chronology if authenticated, but this review could not inspect the physical page image and source control is currently derivative-only. |
| conversion_confidence_score | 0.15 | Two page-5 derivatives disagree, page image files are absent locally, and hash/manifest control is inconsistent. |
| evidence_quantity_score | 0.38 | There are multiple local derivatives and manifests, but no controlling image or reconciled conversion for page 5. |
| agreement_score | 0.18 | Agreement is strong only that a conflict exists; the page-5 content itself is materially inconsistent. |
| identity_confidence_score | 0.35 | Document-level title supports `Dario Arturo Pulgar`; page-local text does not bridge to `Dario Arturo Pulgar-Smith` or any Pulgar-Arriagada/Jose/Juana cluster. |
| claim_probability | 0.70 | The claim that this is a page-control conflict is probable; the probability of either occupational sequence controlling physical page 5 remains below promotion level. |
| relevance_level | high | The source is family-relevant by title and potential CV subject, and the conflict directly affects staged identity/claim handling. |
| relevance_confidence | 0.90 | Relevance to the Dario/Pulgar review queue is clear even though canonical identity attachment is unresolved. |
| canonical_readiness | 0.00 | Not ready for canonical promotion, relationship creation, or identity merge. |

## Claim Judgment

- Revise/hold the staged draft rather than promote it. Its overall recommendation is correct, but the proof-review record should note that the aggregate converted file contains both competing sequences rather than serving as a clean control for the HABITAT/NFB/Chile Films/CITELCO text.
- Treat the staged occupational claims as derivative observations only. Neither the 1979-1970 sequence nor the 1999-1997 sequence should become a canonical work-history claim until physical page 5 is restored or re-rendered and compared against both derivatives.
- Treat all identity-link hypotheses as unresolved. The evidence supports document-level `Dario Arturo Pulgar` by source title, but does not prove equivalence with `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Darío/Dario Pulgar Arriagada`, or Jose/Juana parent candidates.

## Next Action

Hold for conversion QA. Restore or re-render physical page 5 from `raw/sources/CV of Dario Arturo Pulgar.pdf`, reconcile the missing page image files, duplicate manifest rows, and mismatched hashes, then certify one controlling page-5 transcription. After that, run a separate identity-bridge proof review before attaching any page-5 CV claim to a canonical person page.
