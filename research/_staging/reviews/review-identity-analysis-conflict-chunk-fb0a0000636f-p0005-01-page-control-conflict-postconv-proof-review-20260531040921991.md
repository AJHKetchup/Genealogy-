---
type: proof_review
role: claim_reviewer
task_id: proof-review:research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531003857892.md
worker: postconv-proof-review-20260531040921991
staged_draft: research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531003857892.md
reviewed_status: hold
canonical_readiness: hold_for_conversion_qa
source_quality_score: 0.50
conversion_confidence_score: 0.18
evidence_quantity_score: 0.46
agreement_score: 0.16
identity_confidence_score: 0.55
claim_probability: 0.52
relevance_level: high
relevance_confidence: 0.97
---

# Proof Review: Page 5 CV Control Conflict

## Blockers

- The staged draft under review is `research/_staging/identity-analysis/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-identity-analysis-20260531003857892.md`.
- Page control is not resolved. The assigned chunk and aggregate converted file support a 1979-1982 through 1970-1972 work-history page, while the conversion-job page Markdown for page 5 supports a different 1999 through 1997-1998 consulting-work page.
- The chunk manifest lists `CHUNK-fb0a0000636f-P0005-01` twice with conflicting character counts and SHA-256 values. The source packet also reports observed converted/chunk hashes that differ from recorded metadata.
- The manifest references `page-images/page-0005.jpg`, but `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0005.jpg` is not currently available. No `extracted-images/page-0005.jpg` is available either.
- Neither derivative page body independently states `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Pulgar-Smith`, `Arriagada`, or any family relationship. The identity cue is document-level source/title context, not page-local text.
- No work-history claim from this page should be promoted until conversion QA identifies the physical page-5 controlling transcription and resolves the duplicate manifest/hash drift.

## Evidence Strengths

- The source packet, assigned chunk, aggregate converted file, and conflict candidate all consistently identify the source as `raw/sources/CV of Dario Arturo Pulgar.pdf`.
- The assigned chunk literally supports the 1979-1982 HABITAT / Nairobi / Development Support Communications Officer sequence and later NFB, Chile Films, and CITELCO entries, if that derivative is later confirmed as the controlling page.
- The conversion-job page Markdown literally supports the 1999 PROFONANPE / Peru / Consultant sequence and later TVE, Arca Consulting/European Commission, Klohn Crippen Consultants, and SNC Lavalin Agriculture entries, if that derivative is later confirmed as the controlling page.
- The staged identity analysis correctly treats the conflict as a hold rather than selecting one derivative by inference.

## Scored Judgment

| score | value | rationale |
|---|---:|---|
| source_quality_score | 0.50 | The named CV source is local and relevant, but the specific physical page image is unavailable for this review. |
| conversion_confidence_score | 0.18 | Competing derivative transcriptions, duplicate manifest entries, and hash drift make the page conversion unreliable for promotion. |
| evidence_quantity_score | 0.46 | There are multiple local derivatives and a source packet, but they do not agree on the controlling page text. |
| agreement_score | 0.16 | Agreement is limited to document/source context; the page-5 content materially conflicts. |
| identity_confidence_score | 0.55 | `Dario Arturo Pulgar` is supported by source title/path context, but not by page-local identity text or a Pulgar-Smith bridge. |
| claim_probability | 0.52 | It is plausible that the CV belongs to the document-level subject, but no specific page-5 occupational sequence is more probable from the verified derivatives alone. |
| relevance_level | high | The conflict directly affects family-relevant CV identity and work-history staging. |
| relevance_confidence | 0.97 | All reviewed materials concern the assigned page-5 CV control problem. |
| canonical_readiness | hold_for_conversion_qa | Not ready for `research/claims`, `research/relationships`, `wiki/people`, `wiki/families`, or other canonical folders. |

## Identity And Relationship Risk

- Identity risk is moderate for attaching the CV source title `Dario Arturo Pulgar` to canonical `Dario Arturo Pulgar-Smith`; name overlap is relevant but not sufficient here.
- Identity risk is high for merging this CV subject with any `Pulgar-Arriagada`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, or Jose/Juana parent-candidate cluster from this page-control evidence.
- Relationship risk is high for any lineage claim because neither competing page-5 derivative names parents, spouse, children, grandchildren, or family relationships.

## Next Action

Keep the staged identity analysis on `hold_for_conversion_qa`. The next action is targeted page-control QA: restore or recheck the physical page-5 image/PDF page for `raw/sources/CV of Dario Arturo Pulgar.pdf`, compare it against both derivative texts, repair the manifest/hash inconsistencies, and only then run a separate identity-bridge review before attaching any page-5 facts to a canonical person.
