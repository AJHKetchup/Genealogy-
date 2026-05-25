---
type: identity_conflict_analysis
status: hold_for_conversion_qa
role: identity_researcher
worker: postconv-identity-analysis-20260525211540757
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-evidence-extraction-20260525203040850.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-evidence-extraction-20260525203040850.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525203040850.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
canonical_readiness: not_ready
---

# Identity/Conflict Analysis: Entry 172 Row Conflict Revision

## Blockers First

- Exact staged draft reviewed: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-revision-postconv-evidence-extraction-20260525203040850.md`.
- The assigned chunk and revised source packet read entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`.
- The current converted Markdown reads entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. in `En esta`.
- This is a row-level conversion conflict, not a spelling variant. No child identity, parent identity, birth fact, residence, informant, or relationship claim should be promoted from this entry until targeted conversion QA certifies the controlling row.
- The Pulgar father field remains unresolved for promotion: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- Canonical wiki pages for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar` contain local Pulgar-line context, but those pages do not resolve this conversion conflict.
- The staged draft does not literally name `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada`. Any Dario-line use is blocked pending a separate identity-bridge proof review.

## Literal Evidence

Assigned chunk and revised source packet:

- Entry number `172`, registered 7 April 1888.
- Child `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`.
- Birth date/time/place: 8 March 1888, 3 p.m., `Calle de Valdivia`.
- Father field: `Jose del Carmen Pulgar S.` in the chunk/source packet reading; Chilean; employed; resident `Calle de Colipí`.
- Mother field: `Juana Arriagada de Pulgar`; Chilean; `Su sexo`; resident `Calle de Colipí`.
- Informant: `Ernesto Herrera L.`, present at birth, age 26, employed, resident `Calle de Valdivia`.

Current converted Markdown:

- Entry number `172`, registered 7 April 1888.
- Child `José Miguel`; sex `Varon`.
- Birth date/time/place: 6 April 1888, 10 p.m., `En esta`.
- Father `Oswaldo Burgos`; mother `Concepcion de la Cruz`.
- Informant `Oswaldo Burgos`, age 26, employed, resident `En esta`.

Existing canonical context reviewed:

- `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` has generated entry-172-derived birth facts and a probable mother link to `Juana Arriagada de Pulgar`.
- `wiki/people/juana-arriagada-de-pulgar.md` has an entry-172-derived probable child link to `Jose del Carmen Segundo Pulgar Arriagada`.
- `wiki/people/jose-del-carmen-pulgar.md` is a separate stub with a draft child link to `Tulio Cesar Luis Jose`; it does not prove that the entry-172 father candidate is the same person.
- `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied and explicitly warns against attaching similarly named Pulgar records without identity review.

## Hypotheses, Evidence, And Scores

| rank | hypothesis | supporting evidence | conflicts/limits | identity confidence | conflict severity | evidence quality | conversion confidence | claim probability | relevance | canonical readiness |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | Entry 172 is the Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada`. | Assigned chunk and revised source packet agree on the Pulgar/Arriagada row; existing wiki snapshots reflect this cluster. | Current converted Markdown gives a complete Burgos/de la Cruz row for the same entry number; father suffix remains unresolved. | 0.66 | 0.95 | 0.78 | 0.35 | 0.72 | 0.98 | 0.10 |
| 2 | Entry 172 is the Burgos/de la Cruz birth row for `Jose Miguel`. | Current converted Markdown explicitly transcribes this row. | Directly conflicts with the assigned chunk and revised source packet; gives no Pulgar/Arriagada family relevance. | 0.25 | 0.95 | 0.45 | 0.35 | 0.18 | 0.90 | 0.05 |
| 3 | Both readings are real rows, but one derivative artifact is assigned to the wrong row/image/page context. | The two readings are internally coherent but incompatible under one entry number. | Requires targeted conversion QA; identity analysis cannot choose the controlling artifact. | 0.50 | 0.93 | 0.65 | 0.25 | 0.62 | 0.95 | 0.05 |
| 4 | The Pulgar-row father candidate is canonical `Jose del Carmen Pulgar`. | Name core matches `Jose del Carmen Pulgar`; canonical page has another local Pulgar parent context. | `S.` or final mark is unresolved; no spouse/child bridge from this draft proves same-person identity. | 0.30 | 0.60 | 0.55 | 0.30 | 0.35 | 0.70 | 0.05 |
| 5 | `Juana Arriagada de Pulgar` is the Pulgar-row mother and matches the canonical Juana page. | Exact literal name under the Pulgar row; canonical page carries the same entry-derived mother-child cluster. | Relationship depends on row-control QA and cannot be used to merge Juana variants. | 0.62 | 0.85 | 0.76 | 0.35 | 0.70 | 0.95 | 0.10 |
| 6 | This entry directly bridges a Dario Pulgar identity cluster. | Only broad Pulgar/Arriagada surname context if the Pulgar row controls. | No Dario, Arturo, Smith, Dario Jose, spouse, child, grandchild, CV, or other identity bridge appears in this entry. | 0.03 | 0.80 | 0.20 | 0.35 | 0.02 | 0.25 | 0.00 |

## Conflict Analysis

- Same-person conflict: unresolved for `Jose del Carmen Pulgar S.` versus canonical `Jose del Carmen Pulgar`; unresolved for Juana candidates only after row-control QA. No same-person evidence supports any Dario merge from this draft.
- Duplicate-person risk: high if `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or Juana parent candidates are merged by name alone.
- Name-variant conflict: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` must remain separate literal possibilities until the father field is certified. `Jose Miguel` is not a variant of `Jose del Carmen Segundo Pulgar Arriagada`.
- Relationship conflict: high. The two readings attach different children to different parents under the same entry number.
- Chronology conflict: high at the row level. Pulgar/Arriagada gives birth on 8 March 1888; Burgos/de la Cruz gives birth on 6 April 1888.
- Conversion conflict: severe. The assigned chunk and current converted Markdown cannot both be treated as controlling for entry 172.

## Pulgar-Line Anti-Conflation Ranking

| candidate | rank for this draft | comparison |
| --- | ---: | --- |
| Jose/Juana parent candidates | 1 | Only these are directly implicated if the Pulgar/Arriagada row controls. Next step is conversion QA, then proof review of parent identity and relationships. |
| Dario Arturo Pulgar-Smith | 5 | Canonical page is family-supplied as Alexander John Heinz's maternal grandfather. This entry has no Dario, Arturo, Smith, or grandchild bridge. |
| Dario Arturo Pulgar | 5 | CV-related staged evidence elsewhere supports a document-level `Dario Arturo Pulgar` cluster, but this 1888 birth entry does not name or bridge to him. |
| Dario Jose Pulgar-Arriagada | 4 | The Pulgar-row child is `Jose del Carmen Segundo Pulgar Arriagada`, not `Dario Jose`; surname overlap is insufficient. |
| Dario/Darío Pulgar Arriagada | 4 | Existing local context treats this as a separate cluster. This entry supplies no Dario/Darío name or chronology bridge. |

## Recommended Next Action

Keep this exact staged conflict on `hold_for_conversion_qa`. The required next proof-review step is targeted conversion QA against the source image, current converted Markdown, assigned chunk, and revised source packet to decide the controlling entry-172 row and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, rerun proof review before any child identity promotion, birth-fact promotion, parent-child relationship promotion, Jose/Juana same-person analysis, canonical wiki update, or Dario-line identity bridge. Do not merge or attach this entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada` by name overlap alone.
