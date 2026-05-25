---
type: identity_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260525091000336
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525081514407.md"
reviewed_staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525081514407.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525081514407.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
canonical_readiness: hold_for_conversion_qa
---

# Identity And Conflict Analysis: Entry 172 Row-Level Conflict

## Blockers

- Material row-level conflict: the staged conflict draft and current chunk identify entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, while the assigned converted Markdown identifies entry 172 as `José Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`.
- This is not a same-person, duplicate-person, or name-variant issue. It is a controlling-row or file-assignment conflict that must be resolved before promotion.
- The father field in the Pulgar/Arriagada reading remains unresolved at the suffix level: possible readings are `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- The entry does not name Dario. It cannot be used to merge or attach claims to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, passenger Dario candidates, or medical/Geneva Dario candidates by surname or family-context hint alone.
- Existing canonical pages already contain low-confidence or draft Pulgar/Juana evidence snapshots. This staged conflict cannot upgrade those pages until conversion QA and proof review resolve the row conflict.

## Literal Evidence

- Staged conflict draft: entry 172 is described as a Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, with a separate warning that the assigned converted Markdown records a different family.
- Staged source packet: current chunk reads child `Jose del Carmen Segundo Pulgar Arriagada`, male, registered `Siete de Abril de mil ochocientos ochenta i ocho`, born `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`, at `Calle de Valdivia`; father `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`.
- Current chunk: page 58, row 172 gives the same Pulgar/Arriagada reading and places the parents at `Calle de Colipí`.
- Assigned converted Markdown: page 58, row 172 gives `José Francisco`, born `El veinte i seis de Marzo de mil ochocientos ochenta i ocho`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`, informant `Oswaldo Gomez`.
- Canonical context: `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, and `wiki/people/juana-arriagada-de-pulgar.md` contain stub or low-confidence evidence snapshots tied to entry-172 staging. `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied only and explicitly warns against automatic merges with similarly named source clusters.

## Hypotheses

| Rank | Hypothesis | Supporting Evidence | Conflicts And Limits | Identity Confidence | Claim Probability | Recommended Handling |
| ---: | --- | --- | --- | ---: | ---: | --- |
| 1 | Current chunk/source-packet row is the intended entry 172 Pulgar/Arriagada birth registration. | Chunk and staged source packet agree on child, parents, dates, place, informant, page 58, and entry 172. Prior reviewed local context also treated the source image as supporting the Pulgar/Arriagada row. | Assigned converted Markdown for the same file and row disagrees completely. Father suffix remains unresolved. | 0.74 | 0.78 | Hold for targeted conversion QA; rerun proof review before any promotion. |
| 2 | Assigned converted Markdown row is the controlling entry 172, and Pulgar/Arriagada row is from a different row/file state. | Converted Markdown is the assigned derivative file and gives internally coherent Gomez/de la Cruz row data for entry 172. | It conflicts with the current chunk, staged packet, and repeated local review notes for the Pulgar/Arriagada row; no Pulgar-line identity can be drawn from the converted row. | 0.26 | 0.22 | Hold; conversion QA must reconcile source image, converted file, and chunk provenance. |
| 3 | `Jose del Carmen Segundo Pulgar Arriagada` is the child of `Jose del Carmen Pulgar` / `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`. | Supported if the current chunk's row is accepted; names and parent roles are literal in the chunk/source packet. | Dependent on row QA; father suffix uncertain; no broader identity bridge for either parent is established here. | 0.70 | 0.76 | Preserve as a staged parent-child hypothesis only. |
| 4 | `Jose del Carmen Pulgar` in this row is the same person as existing canonical `wiki/people/jose-del-carmen-pulgar.md`. | Name compatibility and existing canonical stub has a draft child link in a Pulgar context. | This row has no age, parents, spouse proof beyond `Juana Arriagada de Pulgar`, or other unique identifiers; row conflict blocks canonical readiness. | 0.43 | 0.40 | Require parent-candidate proof review after conversion QA; do not merge by name alone. |
| 5 | `Juana Arriagada de Pulgar` in this row is the same person as existing canonical `wiki/people/juana-arriagada-de-pulgar.md`. | Exact name compatibility and canonical stub already references this staged entry as probable child evidence. | Dependent on row QA; no birth date, age, parents, or independent identity anchors. | 0.58 | 0.62 | Keep as probable local candidate, held for QA and relationship proof review. |
| 6 | The row supports any Dario identity or Dario-line merge. | Only indirect surname/family-context relevance exists if Pulgar/Arriagada row is accepted. | No `Dario`, `Arturo`, `Smith`, `Jose` as Dario middle name, medical role, Geneva role, passenger context, grandchild, or chronology bridge appears in the entry. | 0.04 | 0.03 | Reject from this source; preserve Dario clusters separately. |

## Dario-Line Comparison

- `Dario Arturo Pulgar-Smith`: canonical page is family-supplied as Alexander John Heinz's maternal grandfather. This entry supplies no `Dario`, `Arturo`, `Smith`, grandchild, spouse, child, birth, death, or residence bridge to him.
- `Dario Arturo Pulgar`: existing staged CV contexts use document-level attribution and often require identity-bridge proof review. This birth entry is for `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Arturo Pulgar.
- `Dario Jose Pulgar-Arriagada`: existing local staging includes photo/Geneva metadata and other held identity contexts. This entry does not state Dario Jose or a Geneva/ICRC role.
- `Dario/Darío Pulgar Arriagada`: existing canonical/staged contexts include a 2000 expropriation cluster and official-role lists. This 1888 birth row does not name Dario and should not be merged into those clusters.
- Jose/Juana parent candidates: `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` are plausible parent candidates only if the Pulgar/Arriagada row is confirmed. The separate canonical `Juana de Dios Amagada de Pulgar` remains a distinct candidate from other staging and is not resolved by this entry.

## Conflicts

- Same-person conflict: none resolved. The source is blocked from proving any same-person merge beyond a local child/parent row hypothesis.
- Duplicate-person conflict: possible duplicates involving `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` remain unresolved; no duplicate resolution is supported now.
- Name-variant conflict: `Jose del Carmen Pulgar` vs `Jose del Carmen Pulgar S.` is a literal-reading issue, not a normalization decision. `Arriagada` must not be treated as a Dario identity bridge.
- Relationship conflict: Pulgar/Arriagada parent-child claims conflict with the assigned converted Markdown's Gomez/de la Cruz parent-child row.
- Chronology conflict: no internal chronology conflict if the Pulgar row is accepted; birth 1888 for Jose del Carmen Segundo is not direct evidence for later Dario adult, CV, medical, passenger, or 2000 expropriation candidates.

## Scores

| Score | Value | Reason |
| --- | ---: | --- |
| identity_confidence | 0.70 | Good row-level identity if the current chunk controls, but blocked by derivative row conflict. |
| conflict_severity | 0.95 | Different child, parents, birth date/place, and informant for the same entry number. |
| evidence_quality | 0.82 | Civil birth-register image/chunk context is strong, but derivative evidence disagrees. |
| conversion_confidence | 0.38 | Current chunk and converted Markdown conflict materially. |
| claim_probability | 0.76 | Pulgar/Arriagada child-parent claim is probable only under the current chunk reading. |
| relevance | 0.90 | High Pulgar-line relevance if row is confirmed; low for Dario-specific attachment. |
| canonical_readiness | 0.10 | Not ready; requires conversion QA and proof review before promotion. |

## Recommended Next Action

Run targeted conversion QA for `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png` against the assigned converted file and current chunk. The QA note must explicitly choose or mark uncertain the controlling entry-172 row and record the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After conversion QA, rerun proof review on the child identity, birth facts, father claim, mother claim, child-parent relationships, and Jose/Juana parent-candidate questions. Do not promote, merge, rename, or attach this entry to any Dario identity until a separate proof-reviewed identity bridge supplies direct evidence.
