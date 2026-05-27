---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260527025657315
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260527020803650.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260527020803650.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260527020803650.md"
conversion_review_note: "research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260527020803650.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
conflict_severity_score: 0.92
evidence_quality_score: 0.84
conversion_confidence_score: 0.42
claim_probability_score: 0.78
relevance_score: 0.96
identity_confidence_score: 0.74
canonical_readiness_score: 0.12
---

# Identity And Conflict Analysis: Entry 172 Row-Level Conflict

## Blockers

- Conversion-control blocker: the current converted Markdown records entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888. The assigned chunk, staged source packet, and targeted QA note identify the physical row `172` on register page 58 as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`, born 8 March 1888.
- Material-identity blocker: this is not a name-variant conflict. The competing readings differ on child identity, parents, birth date/time, birthplace/residence context, informant, and officer/signature context.
- Father-field blocker: the assigned chunk reads `Jose del Carmen Pulgar S.`, but the staged source packet and targeted QA note certify only `Jose del Carmen Pulgar`; the terminal suffix or mark is unresolved.
- Canonical-link blocker: this row does not name Dario, Arturo, Smith, Dario Jose, or a Pulgar-Arriagada adult candidate. It cannot bridge this birth registration to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario Pulgar Arriagada` by surname/family context alone.
- Parent-candidate blocker: `Juana Arriagada de Pulgar` in this row must not be silently merged with `Juana de Dios Amagada de Pulgar` or other Juana variants from entry-513 context. The same caution applies to `Jose del Carmen Pulgar` father candidates until a proof-reviewed relationship/identity bridge exists.

## Evidence Supporting Each Hypothesis

| Rank | Hypothesis | Literal source/evidence support | Interpretation | Probability | Identity confidence | Canonical readiness |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | Physical row `172` for this source task is the Pulgar/Arriagada birth registration | The chunk transcribes entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`; the staged source packet and targeted QA note say direct image review places row number `172` on the Pulgar/Arriagada row. | Strongest local reading for the source image and chunk; still held because the converted Markdown conflicts. | 0.82 | 0.78 | 0.18 |
| 2 | The converted Markdown's Burgos/de la Cruz entry is stale, row-shifted, or from a different page/image set | The converted file gives entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, while the staged QA note says this does not match the visible physical row for this task. | Plausible explanation for the row-level conflict; not a basis to edit conversion output in this task. | 0.76 | 0.70 | 0.10 |
| 3 | Father should be carried only as `Jose del Carmen Pulgar` for now | The staged source packet and targeted QA note explicitly bound the father field to `Jose del Carmen Pulgar`; the chunk has an additional `S.` that is not certified by image review. | Use the base father reading in staged identity analysis, preserving the unresolved suffix as a conversion/proof-review issue. | 0.72 | 0.68 | 0.16 |
| 4 | `Jose del Carmen Pulgar` in this row is the same as the canonical/stub `wiki/people/jose-del-carmen-pulgar.md` | Existing wiki has a `Jose del Carmen Pulgar` stub with a separate draft child link to `Tulio Cesar Luis Jose`; this row supplies a same-name father candidate. | Possible same-person candidate, but the row alone does not prove duplicate identity across entries. | 0.50 | 0.42 | 0.08 |
| 5 | `Juana Arriagada de Pulgar` in this row is the same as canonical/stub `wiki/people/juana-arriagada-de-pulgar.md` | Existing wiki has a `Juana Arriagada de Pulgar` stub and evidence snapshot already tied to this entry's child as probable. | Likely intended canonical target for this exact row, but promotion remains blocked by conversion conflict and low existing confidence. | 0.64 | 0.58 | 0.14 |
| 6 | This row connects to `Dario Arturo Pulgar-Smith` or document-level `Dario Arturo Pulgar` | Canonical Dario Arturo Pulgar-Smith is family-supplied as Alexander John Heinz's maternal grandfather; staged CV materials preserve document-level `Dario Arturo Pulgar` separately. This row does not name either. | Broad Pulgar-line relevance only; no direct same-person or ancestor bridge from this source. | 0.08 | 0.06 | 0.01 |
| 7 | This row connects to `Dario Jose Pulgar-Arriagada` / `Dario Pulgar Arriagada` | Existing staged Dario Jose/Dario Pulgar Arriagada materials include portrait, medical, delegate, and expropriation clusters; this row names a different 1888 child and parents. | Name-family overlap only; preserve as separate/unresolved until a proof-reviewed bridge is found. | 0.06 | 0.05 | 0.01 |
| 8 | `Juana Arriagada de Pulgar` is the same as `Juana de Dios Amagada de Pulgar` | Existing wiki has a separate `Juana de Dios Amagada de Pulgar` stub tied to a different draft child link. This row says `Juana Arriagada de Pulgar`. | Possible OCR/spelling-family question only; not supportable as a merge from this entry. | 0.18 | 0.14 | 0.02 |

## Literal Readings Kept Separate

- Staged draft: current converted Markdown says entry `172` is `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`; staged image-reviewed evidence says physical row `172` is `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.
- Source packet: child `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`; registration date `Siete de Abril de mil ochocientos ochenta i ocho`; birth date/time `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`; birthplace `Calle de Valdivia`; father field certified only as `Jose del Carmen Pulgar`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`.
- Chunk: same Pulgar/Arriagada row, but father is transcribed as `Jose del Carmen Pulgar S.`.
- Converted file: internally coherent but conflicting Burgos/de la Cruz transcription for entry `172`.

## Conflicts

- Same-person/duplicate-person: no same-person merge is supported between the entry-172 child and any Dario candidate. `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` are parent candidates, not automatically duplicate persons across other Pulgar-line pages.
- Name-variant: `Jose del Carmen Pulgar` versus `Jose del Carmen Pulgar S.` is unresolved; treat `S.` as an uncertified terminal mark/suffix. `Juana Arriagada de Pulgar` versus `Juana de Dios Amagada de Pulgar` remains a separate Juana-candidate question.
- Relationship-conflict: the converted file's Burgos/de la Cruz parent pair directly conflicts with the staged Pulgar/Arriagada parent pair for the same entry number.
- Chronology-conflict: the converted file gives birth on 6 April 1888 at 10 p.m.; the staged Pulgar/Arriagada row gives birth on 8 March 1888 at 3 p.m. Registration date remains 7 April 1888 in both competing row contexts.
- Canonical-context conflict: existing wiki snapshots already contain probable or draft facts from this entry, but this analysis should not promote or repair those pages while the current staged draft remains `hold_for_conversion_qa`.

## Scores

| Metric | Score | Judgment |
| --- | ---: | --- |
| conflict_severity | 0.92 | Severe row-level conflict affecting identity, parents, date, and source assignment. |
| evidence_quality | 0.84 | Civil birth register image and image-reviewed staged packet are strong, but the derivative transcript conflict lowers immediate usability. |
| conversion_confidence | 0.42 | Mixed: chunk and QA align with Pulgar/Arriagada; current converted file conflicts materially. |
| claim_probability | 0.78 | Likely that the staged conflict candidate correctly identifies a row-control problem and that the visible row is Pulgar/Arriagada. |
| relevance | 0.96 | High Pulgar-line relevance and high risk of incorrect canonical attachment. |
| identity_confidence | 0.74 | Moderate-high for the local row identity, low for any broader same-person bridge. |
| canonical_readiness | 0.12 | Hold for conversion QA and proof review; no merge, rename, or promoted fact is ready. |

## Recommended Next Action

Run proof review against this exact staged conflict draft, source packet, and targeted conversion QA note. The proof-review/promote decision needed next is: accept or reject the row-control QA that physical entry `172` is the Pulgar/Arriagada row, explicitly decide whether the father field is `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`, and keep all tree-impacting claims on hold until conversion-control reconciles or supersedes the conflicting converted Markdown. After that, a separate identity-bridge proof review is required before linking this row to `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, or any Jose/Juana parent candidate outside this row.
