---
type: proof_review
status: hold_for_conversion_qa
role: claim_reviewer
worker: postconv-proof-review-20260525230319734
task_id: proof-review:research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260525211125251.md
staged_draft: research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260525211125251.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203741061.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
canonical_readiness: not_ready
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

- Canonical readiness is `not_ready`: the assigned converted Markdown and the assigned chunk give incompatible row-level readings for entry 172.
- The source image and chunk support an entry 172 Pulgar/Arriagada birth row, but the assigned converted Markdown records entry 172 as a Burgos/de la Cruz birth. This is a conversion/file-assignment conflict, not a name variant.
- The father field should stay uncertain at the suffix/detail level. The visible source supports the core reading `Jose del Carmen Pulgar`; whether there is a suffix or mark after `Pulgar` still needs targeted conversion QA.
- No Dario-line identity or relationship can be promoted from this entry. Entry 172 does not literally name Dario, Arturo, Smith, Dario Jose, Dario J., or Dario Pulgar.
- Do not merge `Jose del Carmen Pulgar S.` with any existing `Jose del Carmen Pulgar` identity, and do not merge Juana variants, until the controlling row and father field are certified.

## Evidence Checked

- Staged identity analysis: `research/_staging/identity-analysis/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-analysis-20260525211125251.md`
- Staged source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203741061.md`
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`
- Assigned converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`
- Source image: `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`

## Evidence Strengths

- The underlying source is a civil birth registration image, which is a strong source type for a child birth event, registration date, parents, residence, and informant details.
- The page image visibly places entry 172 on page 58 and supports the Pulgar/Arriagada family cluster rather than the Burgos/de la Cruz row in the assigned converted Markdown.
- The assigned chunk and source packet agree on the major claim: entry 172 records `Jose del Carmen Segundo Pulgar Arriagada`, son of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`, with registration on 7 April 1888 and birth on 8 March 1888.
- The staged identity analysis correctly treats Dario-line comparisons as anti-conflation context only.

## Review Scores

| Score | Value | Rationale |
| --- | ---: | --- |
| source_quality_score | 0.90 | Civil registration image is a high-quality source for the event if the row is correctly assigned. |
| conversion_confidence_score | 0.38 | The chunk/source packet/image support Pulgar-Arriagada, while the assigned converted Markdown gives a different entry 172 family. |
| evidence_quantity_score | 0.56 | There is one primary image plus derivative chunk/packet support; no independent corroborating source was reviewed for this task. |
| agreement_score | 0.58 | The image, chunk, and packet agree on the main row, but the assigned converted file directly conflicts. |
| identity_confidence_score | 0.66 | The Pulgar/Arriagada child and parents are probably the correct entry-172 identities, but father-field detail and conversion assignment remain unresolved. |
| claim_probability | 0.76 | The reviewed evidence favors the claim that entry 172 is the Pulgar/Arriagada birth row, but the claim should not be promoted until conversion QA resolves the conflict. |
| relevance_level | high | The row is highly relevant to Pulgar/Arriagada child and parent identity sorting. |
| relevance_confidence | 0.94 | Relevance is clear if the Pulgar/Arriagada row controls; there is no direct relevance to any Dario-line identity beyond anti-conflation. |
| canonical_readiness | not_ready | Hold for targeted conversion QA before promoting claims, relationships, or identity merges. |

## Judgment

The staged identity analysis is supported as a hold/review product. Its central warning is valid: the current evidence set contains a serious row-level conversion conflict. Direct image inspection during this proof review supports the Pulgar/Arriagada row for page 58, entry 172, and the assigned converted Markdown appears inconsistent with the visible source image and chunk.

This review does not authorize a corrected transcription or canonical promotion. The right next step is targeted conversion QA that records the controlling row and father field from the image, then updates downstream proof work from that certified conversion state.

## Next Action

Keep the identity analysis and all dependent child, birth, parent, relationship, same-person, and Dario-line claims at `hold_for_conversion_qa`. Run targeted conversion QA against the page image, assigned converted Markdown, assigned chunk, and source packet. After QA, rerun proof review before any canonical claim or relationship is promoted.
