---
type: proof_review
status: completed
role: claim_reviewer
worker: "postconv-proof-review-20260528222528558"
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526013246594.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526013246594.md"
review_date: 2026-05-28
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

- Canonical readiness blocker: keep this item at `hold_for_conversion_qa`. The source image, assigned chunk, source packet, and staged conflict draft support the Pulgar/Arriagada row for entry 172, but the current converted Markdown still records a different Burgos/de la Cruz row for the same entry number.
- Conversion blocker: the converted Markdown is materially unreliable for entry 172 because it changes the child, parents, birth date, birth place, and informant. Do not promote claims from the converted Markdown as currently written.
- Literal-certification blocker: the source image supports the father as `Jose del Carmen Pulgar`; the possible trailing `S.` is not certified by this review beyond the chunk/source-packet reading. A targeted conversion QA pass should certify the father field exactly to the visible extent.
- Identity-risk blocker: no same-person or relationship claim should be made to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario J. Pulgar Arriagada, or Dario/Dario Pulgar Arriagada from this entry alone. The entry does not name Dario, Arturo, Smith, or any direct bridge to those candidates.

## Evidence Reviewed

- Staged draft: `research/_staging/identity-analysis/identity-analysis-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526013246594.md`.
- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526002943637.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526002943637.md`.
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Source page image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`.

## Evidence Strengths

- The source image visibly places entry 172 on page 58 and supports the Pulgar/Arriagada row: child `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 about 3 p.m. at Calle de Valdivia, with father `Jose del Carmen Pulgar`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.
- The assigned chunk and source packet are consistent with the source-image row and give detailed field-level support for the Pulgar/Arriagada reading.
- The staged identity analysis correctly treats Dario-line comparisons and Jose/Juana parent merges as blocked until row-control and identity proof are complete.

## Weaknesses And Conflicts

- The current converted Markdown gives entry 172 as `Jose Miguel`, son of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888 at `En esta`. This is not supported by the reviewed image for the assigned entry row.
- Because the canonical pipeline references the converted Markdown, this is still a conversion QA problem even though the image favors the Pulgar/Arriagada row.
- The father suffix or trailing mark after `Jose del Carmen Pulgar` remains lower confidence from the image view than the rest of the row.

## Scores

| Category | Score | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.90 | Civil birth register image is a direct contemporary source for the birth entry; image quality is usable though handwriting and scale affect suffix certainty. |
| conversion_confidence_score | 0.35 | The assigned chunk is strong, but the current converted Markdown is materially wrong for the reviewed row. |
| evidence_quantity_score | 0.70 | One direct source image plus consistent chunk/source-packet derivatives; no independent corroborating source reviewed. |
| agreement_score | 0.62 | Image, chunk, source packet, and staged conflict agree on Pulgar/Arriagada; converted Markdown disagrees completely. |
| identity_confidence_score | 0.82 | High for entry 172 as the Pulgar/Arriagada birth row after image review; low for any broader identity merge or Dario-line attachment. |
| claim_probability | 0.86 | The Pulgar/Arriagada row is more probable than the Burgos/de la Cruz conversion for this source image and entry. |
| relevance_level | high | Directly relevant to Pulgar/Arriagada identity and parent-child claims if conversion QA is corrected. |
| relevance_confidence | 0.88 | Family relevance is clear for Pulgar/Arriagada; relevance to Dario-line candidates remains indirect and unproven. |
| canonical_readiness | 0.10 | Hold for conversion QA; not ready for canonical claims, relationships, merges, or wiki attachment. |

## Claim Probability Detail

| Claim Or Hypothesis | Probability | Review Judgment |
| --- | ---: | --- |
| Entry 172 is the Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.86 | Supported by the image, chunk, source packet, and staged conflict draft. |
| Entry 172 is the Burgos/de la Cruz row for `Jose Miguel`. | 0.08 | Present in converted Markdown but not supported by the reviewed source image for this row. |
| Father can be cited exactly as `Jose del Carmen Pulgar S.`. | 0.58 | Chunk/source packet read `S.`; image supports `Jose del Carmen Pulgar`, with trailing suffix needing QA certification. |
| Entry 172 supports a parent-child claim to Jose del Carmen Pulgar and Juana Arriagada de Pulgar. | 0.78 | Substantively supported if row-control QA accepts the image/chunk reading, but not canonically ready while conversion conflict remains. |
| Entry 172 supports any Dario-line same-person or relationship claim. | 0.03 | Not supported; no direct Dario/Arturo/Smith bridge in this entry. |

## Next Action

Run targeted conversion QA on the source image, assigned chunk, and converted Markdown, then revise or supersede the converted Markdown through the approved conversion workflow. After that, rerun proof review before promoting any child identity, birth fact, parent-child relationship, Jose/Juana parent merge, or Dario-line comparison.
