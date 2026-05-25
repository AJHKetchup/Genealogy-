---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: "postconv-identity-analysis-20260525224309357"
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525220612902.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525220612902.md"
output_scope: "research/_staging/identity-analysis/"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525220612902.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
promotion_recommendation: hold_for_conversion_qa
created: "2026-05-25"
---

# Identity/Conflict Analysis: Entry 172 Row-Level Conversion Conflict

## Blockers First

- Row control is unresolved. The staged conflict draft reports that the assigned chunk/source-packet reading and the current converted Markdown do not identify the same entry 172 family.
- The assigned chunk/source-packet reading is `Jose del Carmen Segundo Pulgar Arriagada`, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, informant `Ernesto Herrera L.`.
- The current converted Markdown reading is `Jose Miguel`, born 6 April 1888 at 10 p.m. at `En esta`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, informant `Oswaldo Burgos`.
- This is a material row-level conversion conflict, not a same-person, duplicate-person, or ordinary name-variant conflict.
- No child identity, father identity, mother identity, parent-child relationship, parent merge, Dario-line bridge, or canonical promotion should be advanced from this draft until targeted conversion QA certifies the controlling row.
- The father field remains uncertified even under the Pulgar-row hypothesis: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` must stay distinct literal-reading possibilities.

## Evidence Reviewed

- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525220612902.md`.
- Current source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525220612902.md`.
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Existing canonical context checked for non-merge comparison: `wiki/people/dario-arturo-pulgar-smith.md`, `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/juana-arriagada-de-pulgar.md`, `wiki/people/juana-de-dios-amagada-de-pulgar.md`, and `wiki/people/dar-o-pulgar-arriagada.md`.

## Hypothesis Ranking

| Rank | Hypothesis | Claim probability | Reason | Required next step |
| ---: | --- | ---: | --- | --- |
| 1 | Entry 172 should control as the Pulgar/Arriagada row. | 0.62 | The assigned chunk and current source packet both transcribe entry 172 as `Jose del Carmen Segundo Pulgar Arriagada` with Pulgar/Arriagada parents. Existing wiki context also contains a scoped `Jose del Carmen Segundo Pulgar Arriagada` page and `Juana Arriagada de Pulgar` mother link derived from this cluster. | Targeted conversion QA must compare the source image, converted Markdown, assigned chunk, and source packet, then certify the controlling entry-172 row. |
| 2 | Entry 172 should control as the Burgos/de la Cruz row. | 0.30 | The current converted Markdown explicitly transcribes entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`. This is the conflicting conversion layer and cannot be ignored. | Same targeted conversion QA must determine whether the converted Markdown is a wrong-row/wrong-image conversion or the assigned chunk/source-packet is stale/misaligned. |
| 3 | Existing canonical `Jose del Carmen Segundo Pulgar Arriagada` is the child in the Pulgar-row reading. | 0.55 | The name, birth date/time, place, and mother relationship on the canonical stub match the assigned chunk/source-packet Pulgar row. | Hold. Reconfirm row control and then rerun proof review before relying on this page for promotion or relationship expansion. |
| 4 | Existing canonical `Juana Arriagada de Pulgar` is the mother in the Pulgar-row reading. | 0.54 | The assigned chunk/source-packet names `Juana Arriagada de Pulgar`; the canonical stub has a probable child link to `Jose del Carmen Segundo Pulgar Arriagada`. | Hold. Reconfirm row control and maternal literal form before promotion or merge. |
| 5 | Existing canonical `Jose del Carmen Pulgar` is the father in the Pulgar-row reading. | 0.42 | The assigned chunk/source-packet names a father broadly read as `Jose del Carmen Pulgar` with a possible suffix/mark. Existing `Jose del Carmen Pulgar` is only a separate stub with a draft child link to `Tulio Cesar Luis Jose`, not a proven same-person bridge to this entry. | If Pulgar row is certified, run a father-field proof review and a separate parent-identity bridge review before attaching to the canonical Jose page. |
| 6 | Entry 172 provides evidence for Dario Arturo Pulgar or Dario Arturo Pulgar-Smith. | 0.08 | The draft contains Pulgar-line surname context but no `Dario`, `Arturo`, `Smith`, grandchild relationship, CV-source context, age, occupation, spouse, or child-to-descendant bridge. | No Dario promotion. Require a proof-reviewed lineage bridge from a confirmed entry-172 person to the CV/family-supplied Dario Arturo Pulgar-Smith context. |
| 7 | Entry 172 provides evidence for Dario Jose Pulgar-Arriagada, Dario J. Pulgar Arriagada, or Darío/Dario Pulgar Arriagada. | 0.05 | The Pulgar/Arriagada row has surname overlap only. It names `Jose del Carmen Segundo`, not Dario, and the existing `Darío Pulgar Arriagada` page is a 2000 legal-notice cluster without a bridge to this 1888 birth row. | Preserve as anti-conflation context. Compare only after row control and a direct identity-bearing bridge are available. |
| 8 | `Juana de Dios Amagada de Pulgar` is the same person as `Juana Arriagada de Pulgar` for this entry. | 0.04 | Existing local context contains a separate `Juana de Dios Amagada de Pulgar` stub tied to `Tulio Cesar Luis Jose`, but this assigned draft/source-packet gives `Juana Arriagada de Pulgar`, not `Amagada` or `de Dios`. | Do not merge. Require source-level comparison across the separate child registrations and a letter-by-letter surname proof review. |

## Literal Readings Versus Interpretation

Literal, Pulgar-row layer:

- Entry number: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho`, about `tres de la tarde`.
- Birthplace: `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar S.` in the assigned chunk/source-packet; exact suffix not certified by the conflict draft.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at birth.

Literal, converted-Markdown layer:

- Entry number: `172`.
- Child: `Jose Miguel`.
- Sex: `Varon`.
- Birth: `El seis de Abril de mil ochocientos ochenta i ocho`, about `diez de la noche`.
- Birthplace: `En esta`.
- Father/informant: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.

Interpretation:

- The two layers describe different children, different parents, different birth dates, different birthplaces, different informants, and apparently different page/table context. They cannot be reconciled by spelling normalization.
- The Pulgar-row evidence is family-relevant and may connect to existing Jose/Juana stubs, but the conversion conflict makes current claim probability and canonical readiness low.
- Dario-line context is a double-check requirement only. This entry does not itself name Dario or prove any Dario/Pulgar-Smith/Pulgar-Arriagada identity.

## Conflict Assessment

- Same-person conflict: unresolved between the Pulgar-row child and the converted-Markdown child. Current evidence supports treating them as different row candidates until row control is certified.
- Duplicate-person risk: high if `Jose del Carmen Segundo Pulgar Arriagada` is promoted while the current converted Markdown still controls as `Jose Miguel`; high if `Jose del Carmen Pulgar` is merged with the existing stub without father-field proof review; high if `Juana Arriagada de Pulgar` is merged with `Juana de Dios Amagada de Pulgar` by surname resemblance.
- Name-variant conflict: `Jose del Carmen Segundo Pulgar Arriagada` versus `Jose Miguel` is not a name variant; `Juana Arriagada` versus `Juana de Dios Amagada` is not resolved as a variant; `Pulgar S.` cannot be silently expanded.
- Relationship conflict: Pulgar-row parent-child relationships conflict with Burgos/de la Cruz parent-child relationships for the same entry number. Only one row-control layer can support entry 172 after QA.
- Chronology conflict: Pulgar-row birth date/time is 8 March 1888 at 3 p.m.; converted-Markdown birth date/time is 6 April 1888 at 10 p.m. These cannot both be the same birth event.

## Scores

| Target | Identity confidence | Conflict severity | Evidence quality | Conversion confidence | Claim probability | Relevance | Canonical readiness |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Pulgar/Arriagada row as assigned chunk/source-packet | 0.62 | 0.92 | 0.68 | 0.40 | 0.62 | 1.00 | 0.12 |
| Burgos/de la Cruz row as current converted Markdown | 0.30 | 0.92 | 0.55 | 0.35 | 0.30 | 0.95 | 0.05 |
| `Jose del Carmen Segundo Pulgar Arriagada` child identity | 0.55 | 0.88 | 0.64 | 0.40 | 0.55 | 1.00 | 0.10 |
| `Jose del Carmen Pulgar` father candidate | 0.42 | 0.80 | 0.52 | 0.36 | 0.42 | 0.95 | 0.06 |
| `Juana Arriagada de Pulgar` mother candidate | 0.54 | 0.82 | 0.62 | 0.40 | 0.54 | 0.95 | 0.10 |
| `Juana de Dios Amagada de Pulgar` as same mother | 0.04 | 0.74 | 0.30 | 0.25 | 0.04 | 0.70 | 0.00 |
| Dario Arturo Pulgar / Dario Arturo Pulgar-Smith bridge | 0.08 | 0.70 | 0.24 | 0.30 | 0.08 | 0.85 | 0.00 |
| Dario Jose / Dario J. / Darío Pulgar Arriagada bridge | 0.05 | 0.76 | 0.22 | 0.30 | 0.05 | 0.80 | 0.00 |

Score key: higher conflict severity means greater risk if promoted without resolving the conflict; higher canonical readiness means more suitable for immediate canonical promotion.

## Required Pulgar-Line Comparison

| Candidate | Evidence in this task | Analysis result |
| --- | --- | --- |
| Dario Arturo Pulgar-Smith | Existing canonical page is family-supplied as Alexander John Heinz's maternal grandfather and warns against automatic merging with similarly named Pulgar records. This staged entry does not name Dario, Arturo, Smith, Alexander, or any grandchild relationship. | Not the same-person evidence. Probability 0.08 only as remote family-context lead. |
| Dario Arturo Pulgar | Existing staged CV context elsewhere uses `Dario Arturo Pulgar`; this staged entry does not contain the CV source/title or the name Arturo. | No attachment from this draft. Require a proof-reviewed lineage or identity bridge. |
| Dario Jose Pulgar-Arriagada | This entry's Pulgar-row child is `Jose del Carmen Segundo Pulgar Arriagada`, not `Dario Jose Pulgar-Arriagada`. | Do not merge by shared Jose/Pulgar/Arriagada elements. |
| Dario/Darío Pulgar Arriagada | Existing canonical `Darío Pulgar Arriagada` is represented by a 2000 Serviu legal-notice cluster. This 1888 entry has no Dario and no legal-notice context. | Preserve as separate. Any connection would require independent chronology and identity bridge evidence. |
| Jose/Jose parent candidates | The Pulgar-row father is `Jose del Carmen Pulgar S.` or similar; existing `Jose del Carmen Pulgar` stub has separate draft evidence tied to `Tulio Cesar Luis Jose`. | Plausible parent-name overlap, but no merge. First certify row and father-field suffix, then compare person identity across registrations. |
| Juana parent candidates | The Pulgar-row mother is `Juana Arriagada de Pulgar`. Existing `Juana de Dios Amagada de Pulgar` is a separate candidate from other local evidence. | Keep separate. `Arriagada` and `Amagada` cannot be normalized without proof review. |

## Recommended Next Action

Exact next proof-review/conversion step: targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` and the source image `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`. The QA worker should compare the source image, current converted Markdown, assigned chunk, and current source packet, then explicitly decide whether entry 172 controls as the Pulgar/Arriagada row or the Burgos/de la Cruz row.

If the Pulgar row is confirmed, the next proof-review step is a father-field reread that records the visible form as exactly one of: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, run a separate identity bridge review before attaching the father to the existing `Jose del Carmen Pulgar` page, comparing `Juana Arriagada de Pulgar` with any Juana candidates, or using this birth entry in any Dario Arturo Pulgar, Dario Arturo Pulgar-Smith, Dario Jose Pulgar-Arriagada, or Darío Pulgar Arriagada lineage argument.

Until QA is complete: hold all promotion, merge, rename, parent-child relationship expansion, and Dario-line attachment from this staged draft.
