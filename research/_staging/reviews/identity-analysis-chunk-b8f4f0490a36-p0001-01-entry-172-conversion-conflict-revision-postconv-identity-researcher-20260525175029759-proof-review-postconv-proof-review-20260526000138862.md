---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260526000138862
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525175029759.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525175029759.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525170607416.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
review_decision: hold_for_conversion_qa
canonical_readiness: hold
---

# Proof Review: Entry 172 Conversion Conflict Revision

## Blockers First

- Canonical readiness remains `hold`: the assigned converted Markdown and assigned chunk still describe different entry-172 rows.
- The staged draft/source packet state that the converted Markdown gives `Jose Francisco`, father `Oswaldo Gomez`, mother `Rosario de la Cruz de la Maza`, birth 20 February 1888 at Pellin. The actual referenced converted Markdown reviewed here gives entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 in `En esta`. This mismatch is itself a blocker and should be revised before any downstream use.
- The visible source image and chunk support the Pulgar/Arriagada row for entry 172, but proof review should not rewrite the conversion layer. A targeted conversion QA note must decide row control and explain why the converted Markdown diverges.
- The father-name ending after `Jose del Carmen Pulgar` remains unresolved at proof level. The chunk reads `Jose del Carmen Pulgar S.`, while the image-visible ending is not certain enough here to certify beyond `Jose del Carmen Pulgar [?]` without conversion QA.
- No Dario identity bridge is supported. The source image, chunk, and source packet for entry 172 do not name Dario, Arturo, Smith, Pulgar-Smith, or a later Dario candidate.

## Evidence Checked

- Staged draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525175029759.md`
- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525170607416.md`
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525170607416.md`
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`
- Assigned converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`
- Source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`

## Evidence Strengths

- Source quality is high: a civil birth register is direct contemporary evidence for a birth registration, child name, birth date/place, declared parents, informant, and registration date.
- The visible source image for page 58, entry 172 appears consistent with the chunk's Pulgar/Arriagada reading: child `Jose del Carmen Segundo Pulgar Arriagada`, birth `Ocho de Marzo` at `Calle de Valdivia`, father beginning `Jose del Carmen Pulgar`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`
- The staged draft correctly treats the problem as a row-level conversion conflict rather than a spelling variant or identity merge.
- The staged draft correctly blocks parent-child promotion, parent-candidate merging, and Dario-line attachment while conversion control is unresolved.

## Scorecard

| Metric | Score | Review Judgment |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth register is direct and contemporary, but derivative conversion artifacts disagree. |
| conversion_confidence_score | 0.32 | The chunk and source image support Pulgar/Arriagada; the converted Markdown gives a different row, and the staged draft misstates that converted row. |
| evidence_quantity_score | 0.63 | One source image plus the chunk and packet support the Pulgar/Arriagada reading; one converted file conflicts. |
| agreement_score | 0.40 | Agreement is strong between image/chunk/source packet, but weak across all referenced materials because the converted file and staged description diverge. |
| identity_confidence_score | 0.56 | Pulgar/Arriagada is the probable row identity, but the exact father suffix and conversion-control conflict prevent identity certification. |
| claim_probability | 0.72 | Probable that entry 172 on the visible source is the Pulgar/Arriagada birth registration; not ready as a canonical claim. |
| relevance_level | direct | The draft directly reviews the assigned entry-172 row conflict and anti-conflation issue. |
| relevance_confidence | 0.98 | All checked files and the image are tied to the assigned staged draft and source. |
| canonical_readiness | 0.05 | Hold for targeted conversion QA and corrected staged wording before promotion. |

## Claim Review

The staged draft is substantially supported in its main proof judgment: entry 172 has a material row-level conversion conflict and should remain on hold. The source image and chunk make the Pulgar/Arriagada reading more probable than the converted Markdown's current entry-172 reading.

The staged draft needs revision because its description of the converted Markdown does not match the actual referenced converted file. That does not make the Pulgar/Arriagada row unsupported, but it lowers agreement and conversion confidence and prevents canonical readiness.

No relationship jump is supported. This evidence may be relevant to a Pulgar/Arriagada family cluster after QA, but it does not attach any Dario identity candidate and should not be used as a bridge by surname or family context alone.

## Next Action

Revise the staged conflict/identity wording to quote the actual referenced converted Markdown conflict, then run targeted conversion QA against the source image, converted Markdown, chunk, and source packet. QA should decide the controlling row for register page 58, entry 172 and certify the father field only to the visible-source standard: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, rerun proof review before promoting child identity, birth facts, parent-child relationships, parent-candidate merges, or any Dario-line comparison.
