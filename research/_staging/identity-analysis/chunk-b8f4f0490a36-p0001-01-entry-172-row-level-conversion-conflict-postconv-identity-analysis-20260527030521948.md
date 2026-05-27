---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260527030521948
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260527020803650.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260527020803650.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260527020803650.md"
conversion_review_note: "research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260527020803650.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa
identity_confidence_score: 0.74
conflict_severity_score: 0.92
evidence_quality_score: 0.84
conversion_confidence_score: 0.42
claim_probability_score: 0.78
relevance_score: 0.96
canonical_readiness_score: 0.12
---

# Identity And Conflict Analysis: Entry 172 Row-Level Conversion Conflict

## Blockers

- Conversion-control blocker: the current converted Markdown records entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888. The assigned chunk, staged source packet, and targeted conversion QA note identify physical row `172` on register page 58 as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`, born 8 March 1888.
- Material-identity blocker: this is not a simple name variant. The competing readings differ on child, parents, birth date/time, birthplace or residence context, informant, and row-control source layer.
- Father-field blocker: the assigned chunk reads `Jose del Carmen Pulgar S.`, but the staged source packet and QA note certify only `Jose del Carmen Pulgar`; the terminal mark or suffix remains unresolved.
- Dario-line blocker: this row does not name Dario, Arturo, Smith, Dario Jose, or a later Pulgar-Arriagada adult. It cannot bridge the birth entry to `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada` by surname or family context alone.
- Parent-candidate blocker: `Juana Arriagada de Pulgar` must remain separate from `Juana de Dios Amagada de Pulgar` and other Juana variants unless a later proof-review explicitly supports a merge. `Jose del Carmen Pulgar` in this entry is a parent candidate, not automatically the same person as every same-named Jose Pulgar stub or staged entry.

## Evidence Supporting Each Hypothesis

| Rank | Hypothesis | Literal evidence support | Interpretation | Probability | Identity confidence | Canonical readiness |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | Physical row `172` in this source task is the Pulgar/Arriagada birth registration. | The assigned chunk transcribes entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`; the source packet and QA note say direct image review places row number `172` on the Pulgar/Arriagada row. | Strongest local identity reading, but held because the current converted Markdown materially conflicts. | 0.82 | 0.78 | 0.18 |
| 2 | The converted Markdown's Burgos/de la Cruz entry is stale, row-shifted, or from a different page/image set. | The converted file gives entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`; the QA note says this does not match the visible physical row for this task. | Plausible explanation for the conflict, not authority for editing conversion output in this task. | 0.76 | 0.70 | 0.10 |
| 3 | Father should be bounded to `Jose del Carmen Pulgar` for this staged review. | The packet and QA note explicitly certify only `Jose del Carmen Pulgar`; the chunk's final `S.` is not certified. | Use the base father reading and preserve the terminal mark as a proof-review question. | 0.72 | 0.68 | 0.16 |
| 4 | `Jose del Carmen Pulgar` here may be the same as the canonical/stub `wiki/people/jose-del-carmen-pulgar.md`. | The wiki stub has the same preferred name and a separate draft child link to `Tulio Cesar Luis Jose`; this entry supplies a same-name father candidate. | Possible duplicate-person lead, but not proved by this row alone. | 0.50 | 0.42 | 0.08 |
| 5 | `Juana Arriagada de Pulgar` here may correspond to the canonical/stub `wiki/people/juana-arriagada-de-pulgar.md`. | The wiki stub uses the same preferred name and has evidence snapshot material tied to `Jose del Carmen Segundo Pulgar Arriagada`. | Likely intended target for this exact row, but still blocked by conversion conflict and low canonical confidence. | 0.64 | 0.58 | 0.14 |
| 6 | This row connects to `Dario Arturo Pulgar-Smith` or document-level `Dario Arturo Pulgar`. | `Dario Arturo Pulgar-Smith` is family-supplied as Alexander John Heinz's maternal grandfather; other staged materials discuss Dario/Dario Arturo Pulgar clusters. This row does not name Dario or Arturo. | Broad Pulgar-line relevance only; no same-person or lineage bridge from this source. | 0.08 | 0.06 | 0.01 |
| 7 | This row connects to `Dario Jose Pulgar-Arriagada` or `Dario/Darío Pulgar Arriagada`. | Existing wiki context has a `Darío Pulgar Arriagada` stub from a 2000 expropriation source; this row names a different 1888 child and parents. | Name-family overlap only; keep separate pending a bridge source. | 0.06 | 0.05 | 0.01 |
| 8 | `Juana Arriagada de Pulgar` is the same as `Juana de Dios Amagada de Pulgar`. | A separate wiki stub names `Juana de Dios Amagada de Pulgar` and links her to an entry-513 draft child; entry 172 says `Juana Arriagada de Pulgar`. | Possible spelling/OCR-family question only; not a merge candidate from this evidence. | 0.18 | 0.14 | 0.02 |

## Literal Readings Kept Separate

- Staged conflict draft: current converted Markdown says entry `172` is `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`; staged image-reviewed evidence says physical row `172` is `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.
- Source packet and QA note: child `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`; registration date `Siete de Abril de mil ochocientos ochenta i ocho`; birth date/time `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`; birthplace `Calle de Valdivia`; father certified only as `Jose del Carmen Pulgar`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`, present at the birth.
- Assigned chunk: agrees with the Pulgar/Arriagada row but transcribes the father as `Jose del Carmen Pulgar S.`.
- Current converted file: internally coherent Burgos/de la Cruz transcription for entry `172`, conflicting with the staged row-control review.

## Conflicts

- Same-person/duplicate-person: no merge is supported between the entry-172 child and any Dario identity. `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` are parent candidates only.
- Name-variant: `Jose del Carmen Pulgar` versus `Jose del Carmen Pulgar S.` is unresolved. `Juana Arriagada de Pulgar` versus `Juana de Dios Amagada de Pulgar` must remain a separate Juana-candidate question.
- Relationship-conflict: Burgos/de la Cruz parentage in the converted file directly conflicts with Pulgar/Arriagada parentage in the staged chunk, source packet, and QA note for the same entry number.
- Chronology-conflict: the converted file gives birth on 6 April 1888 at 10 p.m.; the staged Pulgar/Arriagada evidence gives birth on 8 March 1888 at 3 p.m. Both competing layers place registration on 7 April 1888.
- Canonical-context conflict: existing wiki snapshots already contain probable or draft facts related to this entry, but this task must not promote, repair, merge, rename, or overwrite canonical pages while the staged conflict remains on hold.

## Scores

| Metric | Score | Judgment |
| --- | ---: | --- |
| identity_confidence | 0.74 | Moderate-high for the local Pulgar/Arriagada row identity; low for any broader same-person bridge. |
| conflict_severity | 0.92 | Severe row-level conflict affecting identity, parents, birth chronology, and source assignment. |
| evidence_quality | 0.84 | Civil birth-register evidence and image-reviewed staging are strong, but derivative disagreement reduces immediate proof usability. |
| conversion_confidence | 0.42 | Mixed: chunk and QA align with Pulgar/Arriagada, while the current converted Markdown conflicts materially. |
| claim_probability | 0.78 | Likely that the staged draft correctly identifies a row-control problem and that visible row `172` is Pulgar/Arriagada. |
| relevance | 0.96 | High Pulgar-line relevance and high risk of incorrect canonical attachment. |
| canonical_readiness | 0.12 | Hold for conversion QA and proof review; no tree-impacting promotion is ready. |

## Recommended Next Action

Run proof review against the exact staged conflict draft, source packet, and targeted conversion QA note. The required proof-review decision is to accept or reject the row-control finding that physical entry `172` is the Pulgar/Arriagada row, and to settle whether the father field should be carried as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After row-control proof review, conversion-control must reconcile or supersede the conflicting converted Markdown before any promoted claim, relationship, or canonical page update. A separate identity-bridge proof review is required before linking this row to `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, or any Jose/Juana parent candidate outside this row.
