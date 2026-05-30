---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530042428564
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525205831848.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525205831848.md"
reviewed:
  - "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203040850.md"
  - "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-evidence-extraction-20260525203040850.md"
  - "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
  - "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
  - "raw/codex-conversion-jobs/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172/page-markdown/page-0001.md"
source_quality_score: 0.70
conversion_confidence_score: 0.30
evidence_quantity_score: 0.48
agreement_score: 0.28
identity_confidence_score: 0.52
claim_probability: 0.58
relevance_level: high
relevance_confidence: 0.95
canonical_readiness: hold_for_conversion_qa
created: 2026-05-30
---

# Proof Review: Entry 172 Row-Conflict Identity Analysis

This note reviews the exact staged draft `research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-identity-researcher-20260525205831848.md`.

## Blockers First

1. Canonical readiness is `hold_for_conversion_qa`. The staged draft depends on a row-level conversion conflict that remains unresolved.
2. The referenced raw source image path is not available in this workspace during review, and the job manifest's `page-images/page-0001.png` is also absent. This review cannot independently certify the visible handwriting.
3. The available derivatives materially disagree. The assigned chunk/source packet read entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`; the converted Markdown and conversion-job page Markdown read entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. in `En esta`.
4. The disagreement changes child identity, parent identities, date, time, place, and informant context. It is not a spelling variant or a same-person merge question.
5. The father field `Jose del Carmen Pulgar S.` cannot be promoted or normalized from this review. Targeted source-image QA must certify the reading only as far as visible.
6. No Dario-line claim is supported by the available entry-172 derivatives. The draft's Dario discussion should remain anti-conflation guidance only.

## Evidence Strengths

- The staged draft correctly preserves the conflict as a hold rather than promoting a child, birth, parent, or relationship claim.
- The assigned chunk and source packet agree internally on a coherent Pulgar/Arriagada row for entry 172.
- The converted Markdown and conversion-job page Markdown agree internally on a different Burgos/de la Cruz row for entry 172, which makes the row-assignment conflict explicit and reviewable.
- The staged draft correctly treats the current problem as conversion QA, not as proof of a relationship jump or a canonical person merge.
- The draft appropriately warns against attaching this entry to any Dario candidate without a separate proof-reviewed bridge.

## Scoring

| Metric | Score / Level | Judgment |
| --- | ---: | --- |
| source_quality_score | 0.70 | Civil birth registration would be strong direct evidence, but the source image/page image is unavailable for this review, so only derivative reliability can be scored. |
| conversion_confidence_score | 0.30 | Two derivative streams disagree at row level for entry 172. |
| evidence_quantity_score | 0.48 | Multiple staged derivatives were reviewed, but no visible source image or independent corroborating record was available. |
| agreement_score | 0.28 | Agreement exists within each derivative stream, but the controlling streams contradict each other on all key identity facts. |
| identity_confidence_score | 0.52 | The Pulgar/Arriagada interpretation is plausible from the assigned chunk/source packet, but cannot be certified without source-image QA. |
| claim_probability | 0.58 | The staged draft's hold/conflict judgment is well supported; the underlying Pulgar identity claim remains only moderately probable pending QA. |
| relevance_level | high | Directly relevant to the assigned staged draft and entry-172 source packet. |
| relevance_confidence | 0.95 | All reviewed files point to the same chunk/task even though their readings conflict. |
| canonical_readiness | hold_for_conversion_qa | Do not promote to canonical claims, relationships, people, or family pages. |

## Claim-Specific Assessment

| Claim Or Hypothesis | Probability | Review Judgment |
| --- | ---: | --- |
| Entry 172 is the Pulgar/Arriagada row for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.58 | Supported by assigned chunk/source packet; blocked by converted Markdown disagreement and unavailable source image. |
| Entry 172 is the Burgos/de la Cruz row for `Jose Miguel`. | 0.32 | Supported by converted Markdown and job page Markdown; conflicts with the assigned chunk/source packet. |
| The conflict represents stale, mismatched, or misassigned derivative conversion state. | 0.78 | Strongly supported by incompatible row readings under the same entry number. |
| Father field is exactly `Jose del Carmen Pulgar S.`. | 0.40 | Present in the assigned chunk, but not certifiable without visible-source QA. |
| Mother field is `Juana Arriagada de Pulgar`. | 0.55 | Present in the assigned chunk/source packet if the Pulgar row controls; still held because row control is unresolved. |
| This entry supports any Dario identity bridge. | 0.02 | No reviewed derivative names Dario or provides a Dario relationship bridge. |

## Next Action

Keep this staged draft and all dependent claims on `hold_for_conversion_qa`.

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` with the actual source image restored or otherwise accessible. The QA note should decide the controlling row for entry 172 and certify the father field only as far as the image supports: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, rerun proof review before promoting any child identity, birth fact, parent-name claim, parent-child relationship, Jose/Juana merge, or Dario-line comparison.
