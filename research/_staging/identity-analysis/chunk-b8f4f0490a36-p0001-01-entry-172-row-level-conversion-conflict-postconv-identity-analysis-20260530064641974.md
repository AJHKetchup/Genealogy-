---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260530064641974
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260530044358861.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260530044358861.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530044358861.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260530044358861.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row entry 172"
promotion_recommendation: hold_for_conversion_qa
canonical_readiness: blocked
tags: [identity-analysis, conflict-review, row-control, pulgar]
---

# Identity And Conflict Analysis: Entry 172 Row-Control Conflict

## Blockers First

- Exact staged draft reviewed: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260530044358861.md`.
- The original source PNG named by the staged source packet and conversion review is not present in this checkout under either the unaccented or accented `raw/sources/` path checked during this analysis.
- The current converted Markdown and the assigned chunk materially disagree about entry `172`.
- The converted Markdown reads entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888.
- The assigned chunk reads entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, father field `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888.
- The referenced conversion review reports staged crop support for the Pulgar/Arriagada parent and informant fields, but it did not complete fresh original-image certification.
- The final mark or suffix after `Jose del Carmen Pulgar` is not promotion-ready. Keep literal readings (`Jose del Carmen Pulgar S.`) separate from bounded interpretation (`Jose del Carmen Pulgar` with suffix unresolved).
- No canonical merge, Dario-line attachment, Jose/Juana parent-cluster merge, or relationship promotion is supported until row-control QA and proof review resolve the derivative conflict.

## Literal Source Readings

Assigned chunk reading:

```text
172 | Siete de Abril de mil ochocientos ochenta i ocho | Nombre. Jose del Carmen Segundo Pulgar Arriagada Sexo. Hombre | Fecha. Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde Lugar. Calle de Valdivia | Nombre del padre Jose del Carmen Pulgar S. Nac Chileno Prof Empleado Dom Calle de Colipi Nombre de la madre Juana Arriagada de Pulgar Nac Chilena Prof Su sexo Dom Calle de Colipi | Ernesto Herrera L. Presente al nacimiento Edad Veintiseis anos Prof Empleado Dom Calle de Valdivia
```

Converted Markdown reading:

```text
Entry 172: Nombres. Jose Miguel; father Oswaldo Burgos; mother Concepcion de la Cruz; birth 6 April 1888 at ten at night; place En esta.
```

Interpretation: these are not competing spellings of one person. They are incompatible row-control readings.

## Hypothesis 1: Pulgar/Arriagada Controls Entry 172

Evidence supporting:

- The assigned chunk identifies physical row `172` on register page `58` as a birth registration for `Jose del Carmen Segundo Pulgar Arriagada`.
- The staged source packet repeats the same child, birth date/time, mother, father base name, and informant.
- The conversion review says staged crop assets support the lower parent/informant fields for `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Ernesto Herrera L.`.
- Existing canonical wiki context already has stubs for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar`, but their generated evidence is low-confidence/probable and should not override the row-control hold.

Conflicts and limits:

- The converted Markdown currently records a different entry `172`.
- The latest referenced review lacked fresh original-image certification.
- The father suffix `S.` remains unresolved and should not be promoted.
- This hypothesis supports only a staged row-level birth/parent reading, not a broader identity merge.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.78 | Strong staged chunk/source-packet agreement, reduced by unresolved row-control conflict. |
| conflict_severity | 0.95 | Child, parents, birth date/time/place, and informant differ from converted Markdown. |
| evidence_quality | 0.68 | Good local staged evidence plus crop-review report; no fresh original image in this pass. |
| conversion_confidence | 0.52 | Chunk is coherent, but converted artifact conflicts materially. |
| claim_probability | 0.72 | Probable staged reading pending QA. |
| relevance | 1.00 | Directly answers the staged conflict. |
| canonical_readiness | 0.18 | Blocked until row-control QA and proof review. |

## Hypothesis 2: Burgos/de la Cruz Controls Entry 172

Evidence supporting:

- The current converted Markdown explicitly assigns entry `172` to `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.

Conflicts and limits:

- The assigned chunk, source packet, and conversion review contradict this as the controlling Pulgar/Arriagada row.
- No staged evidence links the Burgos/de la Cruz family to the Pulgar/Arriagada child or parents.
- Treating this as a name variant would create a false composite person.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.32 | Explicit in one converted artifact, but contradicted by the staged review set. |
| conflict_severity | 0.95 | Same row-number conflict with entirely different family details. |
| evidence_quality | 0.42 | Single derivative conversion reading for this conflict. |
| conversion_confidence | 0.35 | Current conversion is the artifact under dispute. |
| claim_probability | 0.28 | Possible only if later QA rejects the Pulgar/Arriagada row. |
| relevance | 1.00 | Direct competing reading. |
| canonical_readiness | 0.08 | Not ready for Pulgar-line promotion. |

## Hypothesis 3: Same Person, Duplicate Person, Or Name Variant

Evidence supporting:

- Both readings use entry number `172` in local artifacts.

Conflicts and limits:

- The personal names, surnames, parents, birth date, birth place wording, and informant do not align.
- `Jose Miguel` Burgos/de la Cruz is not supported as a name variant of `Jose del Carmen Segundo Pulgar Arriagada`.
- No same-person or duplicate-person merge path should be opened from this evidence.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.03 | Shared entry number only. |
| conflict_severity | 0.98 | A merge would corrupt both identities. |
| evidence_quality | 0.20 | No identity-bearing overlap beyond the disputed row label. |
| conversion_confidence | 0.20 | Conflict is about row control, not identity variation. |
| claim_probability | 0.02 | Same-person interpretation is unsupported. |
| relevance | 0.92 | Important anti-conflation finding. |
| canonical_readiness | 0.00 | Reject for promotion. |

## Pulgar-Line Comparison

- `Dario Arturo Pulgar-Smith`: canonical wiki context identifies him from family-supplied knowledge as Alexander John Heinz's maternal grandfather. Entry 172 does not name Dario, Arturo, Smith, Alexander John Heinz, a spouse, child, or descendant bridge. Direct identity probability: 0.00. Relevance as a later family-line clue if row 172 is certified: 0.30.
- `Dario Arturo Pulgar`: staged CV tasks and source packets identify a document-level CV subject by this name, with repeated warnings that identity bridge to canonical `Dario Arturo Pulgar-Smith` requires separate proof review. Entry 172 does not name Dario Arturo. Direct identity probability: 0.00. Possible later family-line relevance: 0.25.
- `Dario Jose Pulgar-Arriagada`: staged tasks mention `Dario Jose Pulgar-Arriagada` or `Dario J. Pulgar Arriagada` in separate medical/title and convention contexts. Entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Jose. Direct identity probability: 0.02.
- `Dario/Dario Pulgar Arriagada`: local staged convention-listing packets name `Dario Pulgar-Arriagada` under Chile-related official-list contexts. Entry 172 gives no occupation, later-life context, title, or Dario given name. Direct identity probability: 0.02.
- `Jose del Carmen Pulgar`: if the Pulgar/Arriagada row controls, this is the father base-name field. Existing wiki context has a separate `Jose del Carmen Pulgar` stub with another draft child link to `Tulio Cesar Luis Jose`. This entry alone does not prove all `Jose del Carmen Pulgar` references are one person. Staged father-name probability: 0.74; canonical readiness: 0.18.
- `Juana Arriagada de Pulgar`: if the Pulgar/Arriagada row controls, this is the mother-name field. Existing wiki context has a `Juana Arriagada de Pulgar` stub linked as probable mother of `Jose del Carmen Segundo Pulgar Arriagada`. Staged mother-name probability: 0.76; canonical readiness: 0.18.
- `Juana de Dios Amagada de Pulgar`: existing wiki context has this as a separate candidate linked to `Tulio Cesar Luis Jose`. Entry 172 does not prove this person is the same as `Juana Arriagada de Pulgar`; the surname forms and child clusters must remain separate until independent identity evidence is reviewed. Same-person probability from this entry alone: 0.06.

## Conflict Summary

- Same-person conflict: no supported same-person merge between the Pulgar/Arriagada and Burgos/de la Cruz readings.
- Duplicate-person risk: high if `Jose del Carmen Segundo Pulgar Arriagada` is merged with any Dario Pulgar candidate by surname pattern alone.
- Name-variant conflict: `Pulgar Arriagada`, `Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, and `Dario Pulgar-Arriagada` remain separate hypotheses.
- Relationship conflict: parent claims for `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` remain staged only; Burgos/de la Cruz parentage must not be attached to the Pulgar child.
- Chronology conflict: the 1888 Pulgar/Arriagada child cannot be linked to later Dario candidates without independent identity-bearing evidence. No chronology bridge is supplied here.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Required next step |
| ---: | --- | ---: | --- |
| 1 | Entry 172 controls as Pulgar/Arriagada | 0.72 | Original-image row-control QA plus proof review, including father suffix decision. |
| 2 | Entry 172 controls as Burgos/de la Cruz | 0.28 | Preserve as competing converted-Markdown reading until QA resolves row control. |
| 3 | Pulgar/Arriagada and Burgos/de la Cruz are same person/name variants | 0.02 | Reject as a promotion path; keep as anti-conflation warning. |
| 4 | Entry 172 directly bridges to a Dario Pulgar identity | 0.02 | Separate Pulgar-line identity-bridge proof review required. |
| 5 | `Juana Arriagada de Pulgar` equals `Juana de Dios Amagada de Pulgar` | 0.06 | Separate Jose/Juana parent-cluster review using independent evidence. |

## Recommended Next Action

Route `CHUNK-b8f4f0490a36-P0001-01`, register page 58, physical row entry 172, to targeted original-image row-control QA. The QA/proof-review step must certify whether the controlling row is Pulgar/Arriagada or Burgos/de la Cruz and must explicitly decide the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After row-control proof review, promote only narrow birth-entry claims and stated-parent relationship candidates if accepted. Do not attach this row to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar-Arriagada`, or any broader Jose/Juana cluster without a separate identity-bridge proof review.
