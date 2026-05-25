---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260525232708252
task_id: proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260525211627479.md
staged_draft: research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260525211627479.md
reviewed:
  - raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
  - raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
  - research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203741061.md
  - raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
created: 2026-05-25
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

- The staged draft is materially supported: the assigned converted Markdown and assigned chunk are incompatible for entry 172. The converted file records `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`; the assigned chunk records `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`.
- Direct visual review of the page image supports the chunk/source-packet row for entry 172 more strongly than the converted-file row. The visible entry 172 child reads as `Jose del Carmen Segundo Pulgar Arriagada`; the father/mother fields appear consistent with `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.
- The father suffix or terminal mark after `Pulgar` is not fully resolved from this review. The chunk's `Jose del Carmen Pulgar S.` is plausible, but targeted conversion QA should still decide whether the literal field is `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- The converted Markdown is not reliable enough for entry 172 claims without correction or reassignment. No canonical claim, relationship, merge, page rename, or Dario-line bridge should be promoted from this draft.
- The draft properly avoids converting the review instruction "double-check whether this is Dario" into a correction. The visible source does not name Dario, Arturo, Smith, or any same-person bridge to Dario candidates.

## Evidence Strengths

- The source type is a civil birth register, which is a strong source class for birth, parentage as declared, residence, and registration-date claims.
- The assigned chunk gives a coherent full-row transcription for entry 172: registration on 1888-04-07; child `Jose del Carmen Segundo Pulgar Arriagada`; birth on 1888-03-08 at 3 p.m.; place `Calle de Valdivia`; father `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; compareciente `Ernesto Herrera L.`
- The source packet correctly flags the row-level conflict and does not promote dependent claims. Its recommendation to hold for targeted conversion QA is appropriate.
- The staged identity analysis accurately treats the Burgos/de la Cruz reading as a derivative conflict rather than a name variant, and it correctly rejects any current identity bridge to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Darío/Dario Pulgar Arriagada, or Dario Pulgar A.

## Scored Judgment

| Metric | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.86 | Civil birth register image is a strong primary source for the row if the row is correctly read. |
| conversion_confidence_score | 0.42 | Chunk and visible image align, but the assigned converted file contradicts the row and must be corrected or explained. |
| evidence_quantity_score | 0.62 | One primary page image plus two derivative transcriptions; quantity is limited but sufficient to identify the conflict. |
| agreement_score | 0.48 | Chunk, source packet, and image agree broadly; converted Markdown strongly disagrees. |
| identity_confidence_score | 0.70 | High enough to treat Pulgar/Arriagada as the likely entry 172 row, but father suffix and derivative conflict prevent promotion. |
| claim_probability | 0.68 | The draft's main Pulgar/Arriagada hypothesis is probable, pending conversion QA. |
| relevance_level | high | The row directly concerns a Pulgar/Arriagada child-parent cluster. |
| relevance_confidence | 0.93 | The visible row and chunk both include Pulgar and Arriagada names. |
| canonical_readiness | 0.20 | Hold for conversion QA before any canonical use. |

## Claim-Level Review

| Claim or hypothesis | Review judgment | Probability | Canonical readiness |
| --- | --- | ---: | --- |
| Entry 172 is the Pulgar/Arriagada birth row | Supported by chunk, source packet, and visible image, but blocked by converted-file conflict. | 0.68 | hold_for_conversion_qa |
| Entry 172 is the Burgos/de la Cruz birth row | Supported only by the assigned converted Markdown; contradicted by chunk, source packet, and visible image. | 0.18 | reject_or_reassign_after_qa |
| Father reads `Jose del Carmen Pulgar S.` | Plausible from chunk and image, but terminal suffix needs focused image QA. | 0.58 | hold_for_father_field_qa |
| Mother reads `Juana Arriagada de Pulgar` | Supported by chunk and visible image. | 0.74 | hold_until_row_qa |
| Child is any Dario candidate | Not supported by this source. | 0.03 | not_ready |
| The row proves a Dario-line relationship bridge | Not supported; surname relevance is only a future research lead. | 0.05 | not_ready |

## Reliability And Risk

- Literal support: adequate for holding a Pulgar/Arriagada hypothesis; inadequate for canonical promotion while derivative outputs conflict.
- Source reliability: high as a civil register image; current transcription reliability is mixed because the converted Markdown appears to describe different rows/families.
- Conversion confidence: low-to-moderate overall, despite the chunk being better supported by the image.
- Claim confidence: moderate for the Pulgar/Arriagada row, low for father suffix normalization, near zero for Dario same-person or relationship claims.
- Identity risk: high if the Pulgar/Arriagada child is merged with any Dario candidate; moderate if `Jose del Carmen Pulgar S.` is silently normalized to `Jose del Carmen Pulgar`.
- Relationship jumps: parent-child claims should remain held until targeted conversion QA resolves the row and father field.
- Conflicts: full child/parent/date/place conflict between derivative files, not a spelling issue.

## Next Action

Keep the staged identity analysis and dependent claims at `hold_for_conversion_qa`. The next worker should perform targeted conversion QA against the source image, the converted Markdown, and the chunk, then explicitly decide:

1. Whether entry 172 controls the Pulgar/Arriagada row or the Burgos/de la Cruz row.
2. Whether the father field reads `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
3. Whether the converted Markdown should be corrected, regenerated, or treated as a wrong-row/file-assignment derivative.

No canonical promotion is recommended from this proof review.
