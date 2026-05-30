---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260530064155501
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
- The referenced conversion review says the latest evidence-extraction worker could not freshly certify the original source image because the referenced PNG was not present for that worker.
- The current converted Markdown assigns entry `172` to `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888.
- The assigned chunk assigns entry `172` to `Jose del Carmen Segundo Pulgar Arriagada`, father field `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888.
- These are competing row-control readings, not name variants. Do not attach Burgos/de la Cruz facts to the Pulgar/Arriagada child.
- The father suffix after `Jose del Carmen Pulgar` is not promotion-ready. Keep the literal chunk reading separate from the bounded promoted reading.
- No Dario-line identity bridge is created by this record. The entry does not name Dario, Arturo, Smith, a spouse, child, or descendant of any Dario Pulgar candidate.

## Literal Readings

Assigned chunk reading:

```text
172 | Siete de Abril de mil ochocientos ochenta i ocho | Nombre. Jose del Carmen Segundo Pulgar Arriagada Sexo. Hombre | Fecha. Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde Lugar. Calle de Valdivia | Nombre del padre Jose del Carmen Pulgar S. Nac Chileno Prof Empleado Dom Calle de Colipi Nombre de la madre Juana Arriagada de Pulgar Nac Chilena Prof Su sexo Dom Calle de Colipi | Ernesto Herrera L. Presente al nacimiento Edad Veintiseis anos Prof Empleado Dom Calle de Valdivia
```

Converted Markdown reading:

```text
Entry 172: Nombres. Jose Miguel; father Oswaldo Burgos; mother Concepcion de la Cruz; birth 6 April 1888 at ten at night; place En esta.
```

Interpretation: the readings cannot both describe the same child and parents. The conflict is at row-control/conversion level.

## Hypothesis 1: Pulgar/Arriagada Controls Entry 172

Evidence supporting:

- The assigned chunk and source packet identify row `172` as `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888 and born 8 March 1888 at Calle de Valdivia.
- The conversion review reports staged crop support for the Pulgar/Arriagada parent and informant fields: `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Ernesto Herrera L.`.
- Prior staged proof-review notes in this workspace repeatedly warn that the Burgos/de la Cruz text is a derivative converted-Markdown conflict and that the father suffix remains unresolved.

Conflicts and limits:

- Latest referenced review did not freshly certify the original image.
- The converted Markdown remains materially conflicting.
- `Jose del Carmen Pulgar S.` is a literal chunk reading, but only `Jose del Carmen Pulgar` is bounded enough for staged discussion until targeted proof review accepts the suffix.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.78 | Strong staged support for the Pulgar/Arriagada row, reduced by unresolved conversion control. |
| conflict_severity | 0.94 | Child, parents, birth date/time/place, and informant differ. |
| evidence_quality | 0.68 | Chunk plus staged crop review, but latest review lacks fresh original-image certification. |
| conversion_confidence | 0.52 | Good chunk-level reading; poor artifact-level agreement. |
| claim_probability | 0.72 | Probable staged row reading, not promotion-ready. |
| relevance | 1.00 | Directly resolves the staged conflict question at hypothesis level. |
| canonical_readiness | 0.18 | Blocked pending row-control QA and proof review. |

## Hypothesis 2: Burgos/de la Cruz Controls Entry 172

Evidence supporting:

- The current converted Markdown explicitly records entry `172` as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.

Conflicts and limits:

- The assigned chunk, source packet, and conversion review all contradict this as the controlling reading for the assigned Pulgar/Arriagada chunk.
- No staged evidence connects Burgos/de la Cruz to the Pulgar/Arriagada family.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.32 | Explicit in the converted Markdown, but isolated against the staged review set. |
| conflict_severity | 0.94 | Same material row-control conflict. |
| evidence_quality | 0.42 | Single derivative conversion artifact. |
| conversion_confidence | 0.35 | Low until conversion control is repaired or annotated. |
| claim_probability | 0.28 | Possible only if later QA rejects the Pulgar/Arriagada row. |
| relevance | 1.00 | Direct competing reading. |
| canonical_readiness | 0.08 | Not ready for this Pulgar-line task. |

## Hypothesis 3: Same Person Or Name Variant

Evidence supporting:

- Both readings carry entry number `172` in local artifacts.

Conflicts and limits:

- The names, parents, birth date, birth place, and informant do not match.
- `Jose Miguel` Burgos/de la Cruz is not a supported variant of `Jose del Carmen Segundo Pulgar Arriagada`.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.03 | Shared entry number only. |
| conflict_severity | 0.98 | A merge would create a false composite person. |
| evidence_quality | 0.20 | No identity-bearing overlap. |
| conversion_confidence | 0.20 | Row-control uncertainty only; no person-level bridge. |
| claim_probability | 0.02 | Same-person interpretation is unsupported. |
| relevance | 0.92 | Important anti-conflation finding. |
| canonical_readiness | 0.00 | Reject for promotion. |

## Pulgar-Line Comparison

- `Dario Arturo Pulgar-Smith`: existing wiki context identifies him from family-supplied knowledge as Alexander John Heinz's maternal grandfather. Entry 172 does not name Dario Arturo, Smith, Alexander John Heinz, or a descendant bridge. Direct identity probability: 0.00. Possible family-line relevance if row 172 is certified: 0.35.
- `Dario Arturo Pulgar`: staged CV contexts support a separate Dario Arturo Pulgar cluster, but this entry does not name Dario Arturo. Direct identity probability: 0.00. Possible later family relevance: 0.25.
- `Dario Jose Pulgar-Arriagada`: this record names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Jose. Shared surname structure is only a double-check lead. Direct identity probability: 0.02.
- `Dario/Dario Pulgar Arriagada`: the canonical Darío Pulgar Arriagada page is tied to later modern context, including a 2000 expropriation event. No chronology or relationship bridge links that person to this 1888 child. Direct identity probability: 0.02.
- `Jose del Carmen Pulgar`: if the Pulgar/Arriagada row controls, this is the father-name field. Do not assume all canonical or staged `Jose del Carmen Pulgar` references are one person. Claim probability for father base name: 0.74 staged; 0.18 canonical-ready.
- `Juana Arriagada de Pulgar`: if the Pulgar/Arriagada row controls, this is the mother-name field. Claim probability for mother name: 0.76 staged; 0.18 canonical-ready.
- `Juana de Dios Amagada de Pulgar`: existing wiki context has a separate page/name form in another child cluster. This entry does not prove she is the same person as `Juana Arriagada de Pulgar`. Same-person probability from this entry alone: 0.06.

## Conflict Summary

- Same-person conflict: no supported same-person merge between the Pulgar/Arriagada and Burgos/de la Cruz readings.
- Duplicate-person risk: high if `Jose del Carmen Segundo Pulgar Arriagada` is merged with any Dario Pulgar candidate by surname context alone.
- Name-variant conflict: `Pulgar Arriagada`, `Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, and `Dario Pulgar Arriagada` remain separate hypotheses.
- Relationship conflict: parent claims for `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` are staged only; Burgos/de la Cruz parentage must not be attached to the Pulgar child.
- Chronology conflict: no internal Pulgar/Arriagada chronology conflict if the row controls; major chronology risk arises only if the 1888 child is bridged to later Dario candidates without identity-bearing evidence.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Required next step |
| ---: | --- | ---: | --- |
| 1 | Entry 172 controls as Pulgar/Arriagada | 0.72 | Original-image row-control QA plus proof review. |
| 2 | Entry 172 controls as Burgos/de la Cruz | 0.28 | Preserve as competing converted-Markdown reading until QA resolves it. |
| 3 | Pulgar/Arriagada and Burgos/de la Cruz are same person/name variants | 0.02 | Reject as a promotion path; retain only as anti-conflation warning. |
| 4 | Entry 172 directly bridges to any Dario Pulgar identity | 0.02 | Separate Pulgar-line identity proof review required. |

## Recommended Next Action

Run targeted original-image row-control certification for `CHUNK-b8f4f0490a36-P0001-01`, register page 58, physical row entry 172. The proof-review step must decide the controlling row and explicitly certify whether the father field should be recorded as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or an uncertain bounded form such as `Jose del Carmen Pulgar [?]`.

After row-control proof review, evaluate only the narrow birth-entry claims and parent-child relationships. A separate identity-bridge review is required before connecting this entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, or any broader Jose/Juana parent cluster.
