---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530092624923
task_id: "proof-review:research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526013245826.md"
staged_draft: "research/_staging/identity-analysis/identity-analysis-conflict-chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-identity-researcher-20260526013245826.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260526001440948.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526001440948.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
source_quality_score: 4
conversion_confidence_score: 3
evidence_quantity_score: 4
agreement_score: 3
identity_confidence_score: 5
claim_probability: 0.60
relevance_level: high_if_pulgar_row_confirmed
relevance_confidence: 0.80
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Entry 172 Row-Level Conversion Conflict

## Blockers First

1. The referenced source PNG was not available at `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png` during this review, so I could not independently verify the handwriting or certify the visible row from the image.
2. The assigned chunk and source packet read entry 172 as a Pulgar/Arriagada birth row, while the current converted Markdown reads entry 172 as a Burgos/de la Cruz birth row. This blocks promotion of child identity, birth facts, parent names, parent-child relationships, residences, and informant facts.
3. The father field in the Pulgar/Arriagada reading is still not certified beyond the alternatives already preserved in the staged draft: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
4. No Dario, Arturo, Smith, Dario Jose, or Dario Pulgar Arriagada bridge is supported by this entry. Any Dario-line attachment remains a separate identity-risk problem requiring later proof-reviewed bridge evidence.

## Evidence Strengths

- The staged draft accurately reports the material row-control conflict between the assigned chunk/source packet and the current converted Markdown.
- The assigned chunk is internally coherent for a civil birth registration and gives entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`, with mother `Juana Arriagada de Pulgar`, father read as `Jose del Carmen Pulgar S.`, and informant `Ernesto Herrera L.`.
- The source packet states that image review supported the Pulgar/Arriagada row while explicitly preserving uncertainty about the father-field suffix or trailing mark.
- The current converted Markdown is internally coherent but describes a different entry 172: child `Jose Miguel`, born 6 April 1888 at about 10 p.m. in `En esta`, father and informant `Oswaldo Burgos`, and mother `Concepcion de la Cruz`.
- The staged draft appropriately keeps relationship jumps, parent merges, Juana-name merges, and Dario-line comparisons out of canonical scope.

## Scored Judgment

| Metric | Score |
| --- | --- |
| source_quality_score | 4/10 for this review pass: civil birth registers are strong source types, but the referenced image was unavailable for direct verification here. |
| conversion_confidence_score | 3/10 overall because the assigned chunk and current converted Markdown disagree on the controlling row. |
| evidence_quantity_score | 4/10: one candidate civil-registration row plus source-packet/chunk support, offset by a conflicting converted transcription and no independent bridge source. |
| agreement_score | 3/10 overall; high agreement among the staged draft, source packet, conflict note, and chunk that a row-control conflict exists, but very low agreement between the chunk and converted Markdown for the actual facts. |
| identity_confidence_score | 5/10 for the Pulgar/Arriagada child-row hypothesis pending image QA; 2/10 for merging the father to an existing `Jose del Carmen Pulgar` candidate; 0.5/10 for any Dario-line attachment. |
| claim_probability | 0.60 that the assigned row for this task is the Pulgar/Arriagada row; 0.20 that the Burgos/de la Cruz converted text controls this task; 0.05 or lower for any Dario-line bridge. |
| relevance_level | High for Pulgar/Arriagada family research if row control is confirmed; low for Dario-line attachment at this stage. |
| relevance_confidence | 0.80 for Pulgar/Arriagada relevance under the Pulgar-row hypothesis; 0.15 for Dario-line relevance. |
| canonical_readiness | `hold_for_conversion_qa` |

## Review Finding

The staged identity analysis is supported only as a hold. It correctly treats the issue as a conversion-control conflict rather than a promoted identity conclusion. Literal support for the Pulgar/Arriagada reading exists in the assigned chunk and source packet, but the current converted Markdown contains a materially different row and the source image was not available for this reviewer to certify the row directly.

Do not promote either the Pulgar/Arriagada reading or the Burgos/de la Cruz reading from this proof review. Do not merge the father candidate with any existing `Jose del Carmen Pulgar` page, do not merge `Juana Arriagada de Pulgar` with any other Juana candidate, and do not attach this evidence to a Dario identity cluster.

## Next Action

Keep the staged draft on `hold_for_conversion_qa`. The next action is targeted row-control QA after restoring or locating the original source image or an equivalent page image for SHA-256 `aa0e304338ce3e1bf5ae9a1c695a405c862eb81fba66361d1874b7ca9da981b2`. That QA must decide whether entry 172 is controlled by the Pulgar/Arriagada row or the Burgos/de la Cruz row and certify the father field only to the visible extent before proof review or canonical promotion is rerun.
