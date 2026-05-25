---
type: proof_review
status: completed
role: claim_reviewer
worker: postconv-proof-review-20260525080201970
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525070907893.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-identity-analysis-20260525070907893.md"
reviewed_source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525051608746.md"
reviewed_conflict_candidate: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525051608746.md"
reviewed_converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
reviewed_chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
reviewed_source_image: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Conversion Conflict Identity Analysis

## Blockers First

1. The assigned converted Markdown is materially inconsistent with the page image, chunk, source packet, and conflict draft. The converted Markdown records entry 172 as `Jose Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`, while the image-visible entry 172 and current chunk support `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar` with a possible suffix/final mark, and mother `Juana Arriagada de Pulgar`.
2. The father-name ending is not proof-ready. The review can support the base reading `Jose del Carmen Pulgar`, but the final mark or suffix after `Pulgar` needs targeted conversion QA before any parent identity or relationship promotion.
3. No Dario, Arturo, Smith, occupational, passenger, Geneva/ICRC, expropriation, or later-life bridge appears in the reviewed source context. The staged identity analysis is useful as an anti-conflation check, not as support for a Dario identity.
4. No canonical page, claim, relationship, raw source, converted Markdown, chunk, or source packet should be edited or promoted from this review.

## Scores

| Metric | Score / Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.88 | Civil birth register image is a direct contemporary source for the birth entry; image quality is adequate but compressed and small handwriting limits final-mark confidence. |
| conversion_confidence_score | 0.42 | The chunk/source packet align with the visible source image, but the assigned converted Markdown is a different row set, so the conversion package is internally conflicted. |
| evidence_quantity_score | 0.70 | One direct source image plus one chunk and source packet support the Pulgar/Arriagada row; only one record is involved. |
| agreement_score | 0.52 | Image, chunk, source packet, conflict draft, and staged identity analysis agree broadly; assigned converted Markdown sharply disagrees. |
| identity_confidence_score | 0.72 | The child-parent cluster is coherent for entry 172, but exact father suffix and conversion assignment remain unresolved. |
| claim_probability | 0.74 | It is probable that the intended entry 172 source row is the Pulgar/Arriagada birth registration, but not ready for canonical use until conversion QA reconciles the converted file. |
| relevance_level | high | The source directly concerns a Pulgar/Arriagada birth registration and parent pair relevant to the Pulgar-line staging. |
| relevance_confidence | 0.91 | The Pulgar and Arriagada names are visible in the source image and repeated in the chunk/source packet. |
| canonical_readiness | hold_for_conversion_qa | Row-level conversion conflict blocks promotion or relationship attachment. |

## Evidence Strengths

- The source image visibly places entry 172 on page 58 and supports a child name consistent with `Jose del Carmen Segundo Pulgar Arriagada`.
- The reviewed chunk transcribes entry 172 with registration date `Siete de Abril de mil ochocientos ochenta i ocho`, birth date `Ocho de Marzo de mil ochocientos ochenta i ocho`, birth place `Calle de Valdivia`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The source packet correctly treats the row as family-relevant and explicitly flags conversion confidence as mixed because the assigned converted Markdown gives an incompatible row.
- The staged identity analysis preserves uncertainty instead of forcing a merge, and correctly keeps Dario-related identities out of the support chain.

## Claim Review

| Reviewed claim or hypothesis | Judgment | Probability | Canonical readiness |
| --- | --- | ---: | --- |
| Entry 172 concerns `Jose del Carmen Segundo Pulgar Arriagada` | Supported by image/chunk/source packet, blocked by converted-file conflict | 0.74 | hold_for_conversion_qa |
| Father is `Jose del Carmen Pulgar` / possible `Pulgar S.` | Partly supported, exact final mark unresolved | 0.62 | hold_for_conversion_qa |
| Mother is `Juana Arriagada de Pulgar` | Supported by image/chunk/source packet | 0.78 | hold_for_conversion_qa |
| Converted Markdown's `Jose Francisco` row is the controlling row for this source image | Not supported by the reviewed image context | 0.12 | not_ready |
| Entry 172 supports a Dario Arturo, Dario Jose, or Darío Pulgar identity | Unsupported in reviewed source context | 0.02 | not_ready |
| `Juana Arriagada de Pulgar` should be merged with other Juana variants from separate staging | Unsupported by this record alone | 0.15 | not_ready |

## Next Action

Send the conversion package to targeted conversion QA for page 58, entry 172. QA should reconcile the source image, current chunk, and assigned converted Markdown; determine whether the converted Markdown is from a wrong image/row set or needs replacement; and record the father field conservatively as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, rerun proof review before any canonical claim, parent-child relationship, or person-page merge.
