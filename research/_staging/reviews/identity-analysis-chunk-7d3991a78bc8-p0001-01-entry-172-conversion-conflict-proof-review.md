---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260523035853440
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-7d3991a78bc8-p0001-01-entry-172-conversion-conflict.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-7d3991a78bc8-p0001-01-entry-172-conversion-conflict.md
review_status: hold
canonical_readiness: hold
reviewed:
  - research/_staging/identity-analysis/identity-analysis-chunk-7d3991a78bc8-p0001-01-entry-172-conversion-conflict.md
  - research/_staging/source-packets/chunk-7d3991a78bc8-p0001-01-entry-172-image-reread-pulgar-arriagada.md
  - raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
  - raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-nge-09220dde10/page-0001-chunk-01.md
  - raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
---

# Proof Review: Entry 172 Conversion Conflict

## Blockers

- Canonical readiness is `hold`. The staged identity analysis is supported as a conflict analysis, but the assigned converted Markdown and chunk still transcribe entry 172 as `Jose Miguel`, son of `Oswaldo Bunster` and `Amelia de la Maza`, while the source packet and visible source image support a different entry-172 identity: `Jose del Carmen Segundo Pulgar Arriagada`, son of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.
- The derivative conversion conflict is material, not clerical. The two readings disagree on child identity, parents, birth date/time, birthplace, informant, and official. No person, parent-child relationship, or Dario-line bridge should be promoted from this staged draft until conversion QA corrects or retires the disputed derivative transcript.
- The father-name suffix remains unresolved. The visible row supports `Jose del Carmen Pulgar`; any final suffix or expansion should remain uncertain unless a later QA reread documents it.
- The record does not name Dario. The staged draft correctly treats Dario-related identities as comparison context only, not as literal support for attaching this entry to any Dario person.

## Evidence Strengths

- Source quality is strong in principle: the cited evidence is a civil birth registration image for register page 58, entry 172, with the relevant row visible.
- The source packet's image-reread is materially consistent with the visible row: entry 172 appears to name `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 at about 3 p.m. at `Calle de Valdivia`, with father `Jose del Carmen Pulgar` and mother `Juana Arriagada de Pulgar`.
- The staged identity analysis accurately preserves both sides of the conflict instead of silently replacing the derivative text. It keeps the Bunster/de la Maza reading as derivative-only support and assigns low readiness to any promotion.
- The analysis appropriately avoids relationship jumps. It does not merge the entry-172 child or parents into Dario identities, and it flags the separate risk of merging Jose/Juana Pulgar parent candidates without a targeted proof review.

## Scores

| metric | score | rationale |
|---|---:|---|
| source_quality_score | 0.86 | Civil registration image is direct evidence for the birth registration; image legibility is usable but not perfect. |
| conversion_confidence_score | 0.28 | The assigned converted Markdown and chunk conflict with the visible source image and source packet for entry 172. |
| evidence_quantity_score | 0.62 | One direct source image plus one image-reread packet and the disputed derivative files are available; no independent corroborating source was reviewed. |
| agreement_score | 0.40 | Source image and source packet agree with each other, but they sharply disagree with the assigned converted Markdown/chunk. |
| identity_confidence_score | 0.82 | High for the claim that the visible entry-172 image belongs to the Pulgar/Arriagada identity cluster; reduced by the unreconciled conversion conflict. |
| claim_probability | 0.80 | The staged conflict analysis is probably correct that entry 172 should be held as Pulgar/Arriagada pending QA, not promoted as Bunster/de la Maza. |
| relevance_level | critical | The conflict controls whether tree-impacting child, parent, and relationship claims can safely be staged or promoted. |
| relevance_confidence | 0.95 | The row is exactly the assigned entry 172 and directly affects the named identity cluster. |
| canonical_readiness | hold | Conversion QA must reconcile the derivative transcript before any canonical claim or relationship promotion. |

## Judgment

The staged draft is adequately supported as a conflict analysis and should remain on hold. The best-supported reading from the visible source image and source packet is the Pulgar/Arriagada entry, but the current converted Markdown and chunk still carry the Bunster/de la Maza reading. That contradiction prevents canonical promotion from this draft.

The Bunster/de la Maza hypothesis has derivative-only support in the reviewed materials and should not be used for canonical person or relationship creation unless conversion QA later determines that the image-reread packet was assigned to the wrong source, page, or row. The Dario comparisons are relevant only as guardrails against false attachment.

## Next Action

Run conversion QA for `CHUNK-7d3991a78bc8-P0001-01` against the source image. The QA note should decide whether to correct or retire the Bunster/de la Maza derivative transcript, preserve the Pulgar/Arriagada reading if confirmed, and document the unresolved father suffix. After that, review the individual child-name, birth-event, father, mother, and parent-child claims before any canonical promotion.
