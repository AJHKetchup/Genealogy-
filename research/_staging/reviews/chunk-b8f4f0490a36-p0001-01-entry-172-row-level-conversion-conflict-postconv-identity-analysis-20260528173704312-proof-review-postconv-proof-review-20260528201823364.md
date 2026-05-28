---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260528201823364
task_id: "proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260528173704312.md"
staged_draft: "research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260528173704312.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-row-control-postconv-evidence-extraction-20260528170150642.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260528170150642.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. Do not promote the current converted Markdown's `Jose Miguel` / `Oswaldo Burgos` / `Concepcion de la Cruz` entry as the controlled reading for physical entry `172`. The staged row-control packet, QA note, assigned chunk, and page image support a different physical row: `Jose del Carmen Segundo Pulgar Arriagada`, son of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.
2. Do not promote the father's name with the trailing `S.` from this review. The assigned chunk includes `Jose del Carmen Pulgar S.`, but the targeted QA note certifies only `Jose del Carmen Pulgar`, and the page image does not provide enough confidence here to promote the terminal mark.
3. Do not attach this source to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada`. The visible row does not name Dario, Arturo, Smith, spouse, later-life identifiers, or any identity bridge to those clusters.
4. Do not merge `Juana Arriagada de Pulgar` with `Juana de Dios Amagada de Pulgar` from this item alone. The source supports the narrow mother-name reading only.
5. Canonical promotion should remain on hold until a downstream claim workflow accepts the row-control correction and handles the derivative conversion conflict explicitly.

## Evidence Strengths

- The source is an 1888 civil birth register spread for Los Angeles, Chile, with numbered entries and structured fields for child, birth, parents, and informant.
- The assigned chunk transcribes entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, male, born 8 March 1888 about 3 p.m. at `Calle de Valdivia`, with parents `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`.
- The targeted conversion review independently states that direct image review controls the middle row on page 58 as the Pulgar/Arriagada registration, not the Burgos/de la Cruz text in the converted Markdown.
- The source packet correctly preserves the converted Markdown as a derivative conflict and bounds the father field to `Jose del Carmen Pulgar`.
- Visual review of the page image is consistent with the packet and QA note at the row level: entry `172` is the middle row on page 58 and visibly contains the Pulgar/Arriagada family names, while the Burgos/de la Cruz content is not the controlled row for this source image.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 8/10 |
| conversion_confidence_score | 8/10 for row identity and core Pulgar/Arriagada fields; 5/10 for the father's terminal mark; 2/10 for the conflicting converted Markdown's entry-172 content |
| evidence_quantity_score | 4/10 |
| agreement_score | 8/10 among source packet, QA note, assigned chunk, and page image for the narrow row-control claim; 2/10 including the current converted Markdown |
| identity_confidence_score | 8.5/10 for the row naming `Jose del Carmen Segundo Pulgar Arriagada`; 5.5/10 for attaching the father to an existing same-named canonical person; 6.5/10 for attaching the mother to an existing same-named canonical person; 0.5/10 for any Dario-line bridge |
| claim_probability | 0.90 that physical entry `172` is the Pulgar/Arriagada birth registration; 0.88 that the child is recorded as `Jose del Carmen Segundo Pulgar Arriagada`; 0.84 that the mother is recorded as `Juana Arriagada de Pulgar`; 0.75 that the father base name is `Jose del Carmen Pulgar`; 0.20 that the father suffix `S.` is promotable from this review; 0.02 or lower for Dario-line attachment |
| relevance_level | high |
| relevance_confidence | 0.93 |
| canonical_readiness | hold for canonical promotion; acceptable only as reviewed staging evidence for a narrow row-control correction and bounded birth/parentage claims |

## Review Finding

The staged identity analysis is supported as a proof-review hold with a strong narrow conclusion: physical entry `172` on page 58 is the Pulgar/Arriagada birth registration, and the Burgos/de la Cruz text in the current converted Markdown should be treated as a derivative conversion conflict.

The row supports staged claims for the recorded child name, sex, registration date, birth date/time and place, mother name, father base name, parent residence, and informant details. It does not support identity merges, Dario-line relationships, or a certified father-name suffix.

## Next Action

Keep canonical readiness on hold. The next safe action is a downstream claim-stage decision that accepts the row-control QA, preserves the Burgos/de la Cruz text as a conversion conflict, and promotes only narrow row-level claims if the claim workflow permits. Any father-suffix certification, parent-candidate merge, Juana variant merge, or Dario-line bridge needs a separate proof review with direct supporting evidence.
