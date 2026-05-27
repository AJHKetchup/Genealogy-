---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260527031003832
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260527020803650.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260527020803650.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-imageqa-postconv-evidence-extraction-20260527020803650.md"
conversion_review_note: "research/_staging/conversion-review/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-conversion-qa-note-postconv-evidence-extraction-20260527020803650.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
canonical_readiness: hold_for_conversion_qa_and_proof_review
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

- Conversion-control blocker: the exact staged draft reports a row-level conflict for entry `172`. The current converted Markdown says entry `172` is `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888. The assigned chunk, source packet, and targeted QA note say physical row `172` on register page 58 is `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`, born 8 March 1888.
- Material identity blocker: this is not a name-variant-only issue. The competing layers differ on child name, parents, birth date/time, birth place or residence context, informant, and row-control authority.
- Father-field blocker: the chunk reads `Jose del Carmen Pulgar S.`, while the staged source packet and QA note certify only `Jose del Carmen Pulgar`; the terminal mark or suffix is not proof-ready.
- Dario-line blocker: this entry does not name `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`. It cannot bridge any Dario identity by Pulgar/Arriagada surname overlap alone.
- Jose/Juana parent-candidate blocker: `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` are row-local parent candidates here. `Juana Arriagada de Pulgar` must not be merged with `Juana de Dios Amagada de Pulgar` or other Juana variants without a separate proof-reviewed identity bridge.
- Canonical-edit blocker: existing wiki pages already contain promoted or stub material touching this source, but this task is identity analysis only. No canonical page, relationship, source packet, converted file, chunk, or raw source is changed by this note.

## Evidence Supporting Each Hypothesis

| Rank | Hypothesis | Literal source/staging support | Interpretation | Probability | Identity confidence | Canonical readiness |
| ---: | --- | --- | --- | ---: | ---: | ---: |
| 1 | Physical row `172` for this source task is the Pulgar/Arriagada birth registration. | Assigned chunk: entry `172` names `Jose del Carmen Segundo Pulgar Arriagada`; father `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`. Source packet and QA note state direct image review places row number `172` on the Pulgar/Arriagada row. | Strongest local row-control reading, but not ready for new canonical promotion while the converted Markdown materially conflicts. | 0.82 | 0.78 | 0.18 |
| 2 | The converted Markdown's Burgos/de la Cruz entry is stale, row-shifted, or from another page/image set. | Converted Markdown: entry `172` is `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`; QA note says this does not match the visible physical row for this task. | Plausible explanation for the conflict; not authority for this worker to edit conversion output. | 0.76 | 0.70 | 0.10 |
| 3 | Father should be bounded to `Jose del Carmen Pulgar` in this staged review. | Source packet and QA note explicitly certify only `Jose del Carmen Pulgar`; the chunk's `S.` remains uncertified. | Use the base father reading only; carry the terminal mark as unresolved. | 0.72 | 0.68 | 0.16 |
| 4 | `Jose del Carmen Pulgar` here may be the same person as canonical/stub `wiki/people/jose-del-carmen-pulgar.md`. | Wiki stub has the same preferred name and a separate draft child link to `Tulio Cesar Luis Jose`; this row supplies a same-name father candidate. | Possible duplicate-person lead only. The row does not provide enough unique identifiers for a merge. | 0.50 | 0.42 | 0.08 |
| 5 | `Juana Arriagada de Pulgar` here corresponds to canonical/stub `wiki/people/juana-arriagada-de-pulgar.md`. | Wiki stub uses the same preferred name and its evidence snapshot links her as probable mother of `Jose del Carmen Segundo Pulgar Arriagada` from this source family. | Likely intended row-local target, but no broader Juana merge follows from this note. | 0.64 | 0.58 | 0.14 |
| 6 | `Juana Arriagada de Pulgar` is the same as `Juana de Dios Amagada de Pulgar`. | Separate wiki stub `wiki/people/juana-de-dios-amagada-de-pulgar.md` links to a different draft child, `Tulio Cesar Luis Jose`; entry 172 reads `Juana Arriagada de Pulgar`. | Possible family-name or conversion question only; not a merge candidate from entry 172 evidence. | 0.18 | 0.14 | 0.02 |
| 7 | This row connects to `Dario Arturo Pulgar-Smith` or document-level `Dario Arturo Pulgar`. | Canonical `Dario Arturo Pulgar-Smith` is family-supplied as Alexander John Heinz's maternal grandfather; other staged files discuss document-level `Dario Arturo Pulgar`. Entry 172 does not name Dario, Arturo, Smith, a child/grandchild bridge, or later occupation/residence facts. | Broad Pulgar-line relevance only. No same-person or lineage bridge is proved here. | 0.08 | 0.06 | 0.01 |
| 8 | This row connects to `Dario Jose Pulgar-Arriagada` or `Dario/Dario Pulgar Arriagada`. | Existing wiki context includes `wiki/people/dar-o-pulgar-arriagada.md` from a 2000 expropriation source and staged Dario Jose/Pulgar-Arriagada materials elsewhere. Entry 172 names a different child born in 1888 and does not name Dario. | Name-family overlap only; keep as a separate identity-bridge question. | 0.06 | 0.05 | 0.01 |

## Literal Readings Kept Separate

- Staged conflict draft: current converted Markdown records entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`; staged row-control evidence identifies physical row `172` as `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.
- Source packet and QA note: child `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`; registration date `Siete de Abril de mil ochocientos ochenta i ocho`; birth date/time `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`; birth place `Calle de Valdivia`; father certified only as `Jose del Carmen Pulgar`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`, present at the birth.
- Assigned chunk: agrees with the Pulgar/Arriagada row but transcribes father as `Jose del Carmen Pulgar S.`.
- Converted Markdown: internally presents a Burgos/de la Cruz entry 172 and should be preserved as conflicting derivative evidence until conversion-control resolves it.

## Conflicts

- Same-person/duplicate-person: no same-person conclusion is supported between the entry-172 child and any Dario identity. The row-local father and mother are not automatically duplicate matches to every same-named Jose or Juana candidate.
- Name-variant: `Jose del Carmen Pulgar` versus `Jose del Carmen Pulgar S.` remains unresolved. `Juana Arriagada de Pulgar` versus `Juana de Dios Amagada de Pulgar` is a separate Juana-candidate issue and should not be silently corrected.
- Relationship-conflict: Burgos/de la Cruz parentage in the converted file directly conflicts with Pulgar/Arriagada parentage in the assigned chunk, source packet, and targeted QA note for the same entry number.
- Chronology-conflict: the converted file gives birth on 6 April 1888 at 10 p.m.; the staged Pulgar/Arriagada evidence gives birth on 8 March 1888 at 3 p.m. Both layers place registration on 7 April 1888.
- Canonical-context conflict: the existing wiki already has scoped evidence for the child and mother relationship from this source family, but this newly staged conflict still requires proof review before any further father claim, suffix decision, merge, or Dario-line bridge.

## Scores

| Metric | Score | Judgment |
| --- | ---: | --- |
| identity_confidence | 0.74 | Moderate-high for local Pulgar/Arriagada row identity; low for broader Dario, Jose, or Juana merges. |
| conflict_severity | 0.92 | Severe row-level conflict affecting identity, parents, birth chronology, and source assignment. |
| evidence_quality | 0.84 | Civil birth-register evidence plus image-reviewed staging is strong, but derivative disagreement limits immediate proof use. |
| conversion_confidence | 0.42 | Mixed: assigned chunk and QA support Pulgar/Arriagada, while current converted Markdown conflicts materially. |
| claim_probability | 0.78 | Likely that the staged draft correctly identifies a row-control problem and that visible row `172` is Pulgar/Arriagada. |
| relevance | 0.96 | High Pulgar-line relevance and high risk of erroneous canonical attachment. |
| canonical_readiness | 0.12 | Hold for conversion QA and proof review; no new tree-impacting promotion is ready. |

## Recommended Next Action

Run proof review against the exact staged conflict draft, source packet, targeted conversion QA note, assigned chunk, and current converted Markdown. The proof-review decision needed next is narrow:

1. Accept or reject that physical entry `172` on register page 58 is the Pulgar/Arriagada row rather than the Burgos/de la Cruz row.
2. Decide whether the father field should be carried as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
3. State whether conversion-control must repair, supersede, or quarantine the current converted Markdown before any further claim or relationship promotion.

A separate identity-bridge proof review is required before linking this entry to `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, or any Jose/Juana parent candidate outside this row.
