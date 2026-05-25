---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260525192412321
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525121046889.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-researcher-20260525121046889.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525115651976.md"
reviewed_conflict: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525115651976.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
review_decision: hold_with_revision_required
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Identity Analysis

## Blockers First

1. Canonical promotion remains blocked by a material row-level conversion conflict. The source image and current chunk support entry 172 as the Pulgar/Arriagada birth row, while the currently referenced converted Markdown records entry 172 as a different child-parent row.

2. The staged identity analysis and its referenced conflict/source-packet notes misstate the current converted Markdown. The current converted file reviewed here gives entry 172 as `José Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at `En esta`; it does not currently give `José Francisco`, `Oswaldo Gomez`, or `Emilia de la Cruz`.

3. The father-field ending after `Jose del Carmen Pulgar` is still not proof-ready. The source image supports a Pulgar father in the entry-172 row, but the terminal mark/suffix should remain open as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` until targeted conversion QA certifies the visible form.

4. No Dario-line identity or relationship bridge is supported by this source. The entry does not name Dario, Arturo, Smith, or a later adult identity, and it supplies no same-person or lineage bridge to Dario candidates.

5. Existing canonical or staged downstream Pulgar/Juana pages are not independent proof for this review. They may explain identity risk, but they must not be used to bootstrap promotion while this row-level conversion conflict remains unresolved.

## Evidence Strengths

- The source image visibly supports the current chunk for the controlling row: register page 58, entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`, registered 7 April 1888, born 8 March 1888 at about 3 p.m. at Calle de Valdivia.
- The source image and current chunk both support a father field beginning `Jose del Carmen Pulgar` and a mother field `Juana Arriagada de Pulgar`.
- The staged identity analysis reaches the correct high-level disposition: hold for conversion QA, preserve uncertainty, and do not merge Pulgar/Arriagada evidence into Dario-line candidates.

## Scored Judgment

| Review dimension | Score / value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth register image is a direct source for birth-registration facts; row-level legibility is sufficient for the Pulgar/Arriagada versus non-Pulgar conflict. |
| conversion_confidence_score | 0.40 | The chunk agrees with the source image for the relevant row, but the converted file materially disagrees and the staged draft misquotes the converted-file conflict. |
| evidence_quantity_score | 0.64 | One direct source image plus chunk, source packet, and conflict note; enough to score the conflict and relevance, not enough for canonical promotion. |
| agreement_score | 0.52 | Source image, chunk, and packet agree on Pulgar/Arriagada; converted Markdown disagrees, and the staged note's converted-layer details are stale. |
| identity_confidence_score | 0.72 | Entry 172 in the visible image is probably the Pulgar/Arriagada row, but derivative-file disagreement and father suffix uncertainty keep identity proof below promotion level. |
| claim_probability | 0.74 | Probability that the source-visible entry 172 is for `Jose del Carmen Segundo Pulgar Arriagada`; lower for any promoted canonical claim until conversion QA is complete. |
| relevance_level | high | The source-visible row directly contains Pulgar and Arriagada names. |
| relevance_confidence | 0.90 | Family-relevant names are visible in the image and repeated in the current chunk/source packet. |
| canonical_readiness | hold_for_conversion_qa | Do not promote claims, relationships, or identity bridges until targeted conversion QA reconciles the converted file and certifies the father field. |

## Claim-Level Review

- Supported with hold: the source image/current chunk identify entry 172 as a birth registration for `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888 and born 8 March 1888 at about 3 p.m. at Calle de Valdivia.
- Supported with uncertainty: the father is source-visible as `Jose del Carmen Pulgar` plus an unresolved terminal mark or suffix. Do not standardize the ending without targeted QA.
- Supported with hold: the mother field is `Juana Arriagada de Pulgar` in the source image/current chunk.
- Revise required: the staged identity analysis should update its description of the current converted Markdown to `José Miguel` / `Oswaldo Burgos` / `Concepcion de la Cruz` / 6 April 1888 / `En esta`, unless a different converted file version is intentionally being referenced and made available.
- Not supported: any same-person, parent-child, or ancestral bridge from this entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, or `Dario Pulgar A.`

## Next Action

Keep the staged identity analysis at `hold_for_conversion_qa` and revise its converted-file description before downstream proof or promotion. Then route targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01`, entry 172, to reconcile the source image/current chunk against the converted Markdown and settle the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
