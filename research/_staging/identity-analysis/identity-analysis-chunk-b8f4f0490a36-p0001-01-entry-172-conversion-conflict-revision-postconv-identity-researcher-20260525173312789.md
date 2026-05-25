---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260525173312789
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525170036486.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260525170036486.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525170036486.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
promotion_recommendation: hold_for_conversion_qa
---

# Identity Analysis: Entry 172 Conversion Conflict

## Blockers

- Controlling-row blocker: the staged draft and source packet say the chunk/source-image review supports entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`; the assigned converted Markdown says entry `172` is `José Francisco`, child of `Oswaldo Gomez` and `Rosario de la Cruz de la Maza`.
- This is not a name variant. The competing row readings differ on child name, parents, birth date, birth place, informant, and place context.
- Father-field blocker: the ending after `Jose del Carmen Pulgar` is unresolved. Preserve the possible proof-review outcomes `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]`.
- Relationship blocker: no child-parent relationship from this entry should be promoted until conversion QA identifies the controlling row and proof review reruns the identity/relationship claims.
- Dario-line blocker: this entry does not name Dario, Arturo, Pulgar-Smith, Dario Jose, or Dario/Darío Pulgar Arriagada. It cannot bridge Dario-line identities by surname or family context alone.

## Literal Evidence

From the exact staged draft and referenced source packet:

- Entry number: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`; place `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar` with unresolved final suffix or mark; chunk reading gives `Jose del Carmen Pulgar S.`.
- Mother: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at birth, age `Veintiseis años`, profession `Empleado`, residence `Calle de Valdivia`.

Contrary literal evidence from the assigned converted Markdown:

- Entry `172` is transcribed as `José Francisco`.
- Father: `Oswaldo Gomez`.
- Mother: `Rosario de la Cruz de la Maza`.
- Birth: `En veinte de Febrero de mil ochocientos ochenta i ocho, a las diez de la noche`; place `En Pellin`.

Interpretation: the Pulgar/Arriagada reading is family-relevant and is the row asserted by the staged draft/source packet, but the assigned converted Markdown conflict blocks canonical promotion and any identity merge.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Registration

Interpretation: the controlling row is the birth registration of `Jose del Carmen Segundo Pulgar Arriagada`, son of `Jose del Carmen Pulgar [ending unresolved]` and `Juana Arriagada de Pulgar`.

Supporting evidence:

- The staged draft explicitly identifies the chunk/source-image-supported row as the Pulgar/Arriagada entry.
- The referenced source packet repeats the same child, registration date, birth date/place, parents, and informant.
- The assigned chunk contains the Pulgar/Arriagada row for entry `172`.
- Existing wiki context has pages for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar`, showing local relevance but not resolving this conversion conflict.

Conflicts and limits:

- The assigned converted Markdown gives a mutually exclusive Gomez/de la Cruz de la Maza row for the same entry number.
- The father's final suffix/mark is not certified.
- Existing canonical pages must not be strengthened from this held draft.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.72 | Strong staged packet/chunk support, reduced by direct converted-file contradiction. |
| conflict_severity | 0.94 | Competing readings identify different children, parents, dates, places, and informants. |
| evidence_quality | 0.68 | Detailed local staged evidence, but derivative outputs disagree. |
| conversion_confidence | 0.45 | Mixed; controlling row and father suffix require targeted QA. |
| claim_probability | 0.70 | Probable as staged held evidence, not ready for promotion. |
| relevance | 0.98 | Directly addresses the assigned draft and Pulgar/Arriagada family context. |
| canonical_readiness | 0.18 | Hold for conversion QA and renewed proof review. |

## Hypothesis 2: Converted Markdown Entry 172 Is The Controlling Row

Interpretation: the controlling row may be the converted Markdown row for `José Francisco`, child of `Oswaldo Gomez` and `Rosario de la Cruz de la Maza`.

Supporting evidence:

- The assigned converted Markdown labels this row as entry `172`.
- It provides a complete alternative identity cluster.

Conflicts and limits:

- The staged draft and source packet were created because chunk/source-image review supports a different row.
- The converted Markdown conflicts with every identity-bearing field needed for this task.
- No Pulgar-line or Dario-line relevance is demonstrated for the Gomez/de la Cruz de la Maza cluster.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.36 | Present in one derivative conversion, but under active staged QA challenge. |
| conflict_severity | 0.94 | Mutually exclusive with the Pulgar/Arriagada row. |
| evidence_quality | 0.42 | Complete transcription, but contradicted by chunk/source-packet review. |
| conversion_confidence | 0.35 | Not reliable enough for promotion in this task. |
| claim_probability | 0.30 | Possible row/file assignment issue, not the leading staged hypothesis. |
| relevance | 0.72 | Relevant as the competing row only. |
| canonical_readiness | 0.02 | No promotion from this conflict draft. |

## Hypothesis 3: Father Candidate Is Existing Jose Del Carmen Pulgar

Interpretation: the father in the Pulgar/Arriagada row may be the same person as `wiki/people/jose-del-carmen-pulgar.md`.

Supporting evidence:

- The row names a father read at least as `Jose del Carmen Pulgar`.
- The existing wiki page has the same preferred name and separate draft Pulgar parent context.

Conflicts and limits:

- The final suffix or mark after `Pulgar` remains unresolved.
- Name overlap alone cannot merge Jose parent candidates across separate records.
- The controlling-row conflict must be resolved before parent identity review.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.48 | Plausible same-name parent candidate, not proved. |
| conflict_severity | 0.70 | Meaningful risk of conflating same-named Jose Pulgar candidates. |
| evidence_quality | 0.52 | Direct name evidence, but suffix and row control remain open. |
| conversion_confidence | 0.45 | Depends on entry-172 conversion QA. |
| claim_probability | 0.46 | Possible parent candidate only. |
| relevance | 0.88 | Direct parent-candidate issue. |
| canonical_readiness | 0.12 | Hold for father-field certification and parent-candidate proof review. |

## Hypothesis 4: Mother Candidate Is Existing Juana Arriagada De Pulgar

Interpretation: the mother in the Pulgar/Arriagada row may be the same person as `wiki/people/juana-arriagada-de-pulgar.md`.

Supporting evidence:

- The row and source packet read the mother as `Juana Arriagada de Pulgar`.
- The existing wiki page uses the same preferred name and has a probable child link to `Jose del Carmen Segundo Pulgar Arriagada`.

Conflicts and limits:

- The main conversion conflict still blocks promotion.
- Do not silently equate this name with other Juana candidates, including `Juana de Dios Amagada de Pulgar` contexts, without proof review.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.66 | Exact-name support within the held row, reduced by conversion conflict. |
| conflict_severity | 0.62 | Main risks are row control and Juana-candidate conflation. |
| evidence_quality | 0.63 | Direct staged row reading, still not final. |
| conversion_confidence | 0.45 | Depends on entry-172 conversion QA. |
| claim_probability | 0.64 | Probable if the Pulgar/Arriagada row is accepted. |
| relevance | 0.90 | Direct parent-candidate issue. |
| canonical_readiness | 0.16 | Hold for conversion QA and relationship proof review. |

## Dario-Line Anti-Conflation Comparison

This staged draft does not name any Dario candidate. It can only trigger a future double-check if a separately reviewed lineage bridge connects the Jose/Juana family context to a Dario-line person.

| Candidate | Local evidence context | Effect of this draft | Probability from this draft |
| --- | --- | --- | ---: |
| `Dario Arturo Pulgar-Smith` | Canonical family-supplied maternal grandfather of Alexander John Heinz; page warns against automatic attachment of similarly named records. | No direct bridge; no Pulgar-Smith name or relationship appears here. | 0.01 |
| `Dario Arturo Pulgar` | Other staged CV evidence uses this document-level name and requires an identity bridge to any canonical person. | No Dario/Arturo/CV evidence appears here. | 0.01 |
| `Dario Jose Pulgar-Arriagada` | Mentioned in other Pulgar-line review contexts. | No support from this entry; do not infer from Pulgar/Arriagada surname pattern. | 0.01 |
| `Dario J. Pulgar Arriagada` | Other staged contexts treat the initial and full-name expansion as unresolved. | No initial, occupation, chronology, or relationship bridge appears here. | 0.01 |
| `Dario Pulgar Arriagada` / `Darío Pulgar Arriagada` | Existing canonical stub has a 2000 expropriation event. | No same-person or chronology evidence. | 0.01 |
| Jose/Juana parent candidates | This draft directly involves `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`. | Relevant only as parent-candidate anti-conflation after row QA. | Jose 0.46; Juana Arriagada 0.64 |

Ranked hypotheses:

| Rank | Hypothesis | Probability | Required next proof-review or promotion step |
| ---: | --- | ---: | --- |
| 1 | Entry `172` supports a held Pulgar/Arriagada birth-registration cluster for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.70 | Targeted conversion QA must identify the controlling row and certify the father field. |
| 2 | The row supplies parent-candidate context for `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`. | 0.55 | After row QA, run parent-candidate proof review against existing Jose/Juana pages. |
| 3 | The row is indirect ancestral context for a later Dario-line person. | 0.08 | Require a separately reviewed lineage bridge from this child/parents to the specific Dario candidate. |
| 4 | Same-person evidence for `Dario Arturo Pulgar-Smith` and `Dario Arturo Pulgar`. | 0.01 | Use identity-bearing CV or family evidence; this draft cannot decide it. |
| 5 | Same-person evidence for `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, or `Dario/Darío Pulgar Arriagada`. | 0.01 | Use full-name, date, occupation, residence, and family-continuity evidence from those source packets. |

## Conflict Summary

- Same-person conflicts: unresolved for father `Jose del Carmen Pulgar` versus existing same-name page; unresolved for mother `Juana Arriagada de Pulgar` because the row is held.
- Duplicate-person risks: high if Jose parent candidates are merged by name alone; high if Juana Arriagada and other Juana variants are normalized silently.
- Name-variant conflicts: father suffix after `Pulgar` remains unresolved; the Gomez/de la Cruz cluster is not a variant of the Pulgar/Arriagada cluster.
- Relationship conflicts: the Pulgar/Arriagada row would support Jose/Juana child-parent relationships, while the assigned converted Markdown supports unrelated Gomez/de la Cruz parents for entry `172`.
- Chronology conflicts: no Dario chronology conflict is proved. The relevant date conflict is between competing entry-172 row readings.

## Recommended Next Action

Keep the exact staged draft and all dependent identity, claim, relationship, parent-candidate, and Dario-line comparison work at `hold_for_conversion_qa`.

Exact next step: targeted conversion QA should compare the source image, assigned converted Markdown, chunk, and referenced source packet for entry `172`; identify the controlling row; and certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. Only after that should proof review rerun child identity, birth facts, child-parent relationships, and parent-candidate comparisons against existing `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` pages. No Dario-line merge, rename, or canonical attachment is supported by this draft.
