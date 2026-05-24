---
type: proof_review
role: claim_reviewer
worker: postconv-proof-review-20260524144124499
task_id: proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524141515582.md
staged_draft: research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524141515582.md
review_status: hold
canonical_readiness: hold_for_conversion_qa
reviewed:
  - research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524141515582.md
  - research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524141515582.md
  - raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
  - raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
  - raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
---

# Proof Review: Entry 172 Pulgar/Arriagada Identity Analysis Revision

## Blockers

- Canonical readiness is `hold_for_conversion_qa`. The assigned chunk and visible page image support the Pulgar/Arriagada entry-172 row, but the assigned converted Markdown still transcribes entry 172 as a materially different Gomez/de la Cruz cluster.
- The conversion conflict is row-level and identity-critical. The conflicting files disagree on child name, parents, birth date/time, birthplace, informant, and official-signature context.
- The father field is sufficiently supported for broad identity as `Jose del Carmen Pulgar`, but the final suffix or mark after `Pulgar` is not resolved enough for canonical normalization.
- The source does not name Dario. This staged identity analysis cannot support attaching entry 172 to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario Pulgar Arriagada, or any Dario passenger candidate without a separate bridging source.

## Evidence Strengths

- The original civil birth-register image is available and directly relevant to page 58, entry 172.
- Visual review of the page image supports the assigned chunk/source-packet reading for the entry-172 row: `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at about 3 p.m. at `Calle de Valdivia`, with father `Jose del Carmen Pulgar`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`
- The staged draft correctly identifies the converted Markdown conflict and recommends hold rather than promotion.
- The draft handles identity risk conservatively by separating the Pulgar/Arriagada row from any Dario candidate and by requiring conversion QA before later parent-child or merge analysis.

## Scoring

| metric | score | rationale |
|---|---:|---|
| source_quality_score | 0.86 | Civil birth registration is direct, contemporary evidence; the photographed row is visible, though small handwriting limits suffix certainty. |
| conversion_confidence_score | 0.42 | The assigned chunk now supports the Pulgar/Arriagada row, but the assigned converted Markdown still gives a different entry-172 family. |
| evidence_quantity_score | 0.64 | One direct image, the staged draft, source packet, assigned chunk, and conflicting converted file were reviewed; no independent corroborating source was reviewed. |
| agreement_score | 0.55 | Image, chunk, source packet, and staged draft broadly agree, while the converted Markdown remains materially contradictory. |
| identity_confidence_score | 0.82 | Strong support for the Pulgar/Arriagada identity cluster in the visible entry; reduced by unresolved conversion conflict and father-suffix uncertainty. |
| claim_probability | 0.84 | The staged draft's main judgment is well supported: the Pulgar/Arriagada row is likely correct for the image/chunk, but canonical use must wait for QA. |
| relevance_level | critical | This controls child identity, parent-child relationships, and false-positive prevention for later Pulgar/Dario identity work. |
| relevance_confidence | 0.96 | All reviewed materials are tied to the assigned staged identity-analysis draft and entry 172. |
| canonical_readiness | hold_for_conversion_qa | Do not promote until conversion QA reconciles or supersedes the conflicting converted Markdown and records the father-name suffix policy. |

## Review Judgment

Hold. The staged identity analysis is a sound review-layer assessment, not a promotion-ready identity proof. The source image and assigned chunk support the Pulgar/Arriagada identity cluster, but the converted Markdown conflict is still active and affects core identity fields.

The staged draft should remain available as a QA-directed identity-analysis note. It should not be used as canonical support for claims, relationships, person pages, family pages, or Dario identity attachment until the derivative conversion conflict is resolved.

## Next Action

Send to conversion QA for `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md` and the associated chunk set. QA should reconcile the entry-172 row against the source image and explicitly record whether the father should be transcribed as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`; then rerun proof review before canonical promotion.
