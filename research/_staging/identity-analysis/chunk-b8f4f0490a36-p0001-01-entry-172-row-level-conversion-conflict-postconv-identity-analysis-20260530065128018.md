---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260530065128018
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
tags: [identity-analysis, conflict-review, row-control, pulgar, anti-conflation]
---

# Identity And Conflict Analysis: Entry 172 Row-Control Conflict

## Blockers First

- Exact staged draft reviewed: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260530044358861.md`.
- The source PNG named by the staged packet and chunk is not present at the checked `raw/sources/` paths in this checkout; this analysis did not perform fresh original-image certification.
- The assigned chunk and the current converted Markdown materially conflict for entry `172`.
- The assigned chunk reads entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, son of `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`.
- The current converted Markdown reads entry `172` as `Jose Miguel`, son of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888 at 10 p.m. in `En esta`.
- The referenced conversion review reports staged crop support for the Pulgar/Arriagada parent and informant fields, but it explicitly keeps promotion at `hold_for_conversion_qa`.
- The trailing mark or suffix after `Jose del Carmen Pulgar` is unresolved. Literal chunk text is `Jose del Carmen Pulgar S.`; promotion-ready interpretation is only `Jose del Carmen Pulgar` with suffix unresolved.
- No canonical merge, name normalization, parent-cluster merge, Dario-line attachment, or relationship promotion is supported before original-image row-control QA and proof review.

## Literal Readings Versus Interpretation

Literal assigned chunk reading:

```text
172 | Siete de Abril de mil ochocientos ochenta i ocho | Nombre. Jose del Carmen Segundo Pulgar Arriagada Sexo. Hombre | Fecha. Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde Lugar. Calle de Valdivia | Nombre del padre Jose del Carmen Pulgar S. Nac Chileno Prof Empleado Dom Calle de Colipi Nombre de la madre Juana Arriagada de Pulgar Nac Chilena Prof Su sexo Dom Calle de Colipi | Ernesto Herrera L. Presente al nacimiento Edad Veintiseis anos Prof Empleado Dom Calle de Valdivia
```

Literal current converted Markdown reading:

```text
Entry 172: Jose Miguel; father Oswaldo Burgos; mother Concepcion de la Cruz; birth 6 April 1888 at ten at night; place En esta.
```

Interpretation: these are incompatible row-control readings, not competing spellings or name variants for one person.

## Hypothesis 1: Pulgar/Arriagada Row Controls Entry 172

Evidence supporting:

- The assigned chunk identifies register page 58, entry `172`, as the birth registration of `Jose del Carmen Segundo Pulgar Arriagada`.
- The staged source packet repeats the same child, birth date/time/place, father base name, mother, and informant.
- The conversion review states that existing staged crop assets support the lower parent/informant fields: `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Ernesto Herrera L.`.
- Existing canonical pages already contain low-readiness stubs for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar`, consistent with this staged family cluster but not controlling over the conversion hold.

Conflicts and limits:

- The current converted Markdown assigns the same entry number to a different child and different parents.
- The source image was unavailable for fresh certification in the referenced review and in this identity pass.
- The father suffix `S.` is not certified for promotion.
- This hypothesis supports only a staged birth-entry and stated-parent candidate, not a Dario-line bridge.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.78 | Strong agreement across the assigned chunk, source packet, and crop-review note; held back by unresolved row control. |
| conflict_severity | 0.95 | Child, parents, birth date/time/place, and informant differ from the converted artifact. |
| evidence_quality | 0.68 | Good staged evidence, but no fresh original-image certification. |
| conversion_confidence | 0.52 | The chunk is coherent, while the converted Markdown conflicts materially. |
| claim_probability | 0.72 | Probable staged reading pending original-image QA. |
| relevance | 1.00 | Directly addresses the staged conflict. |
| canonical_readiness | 0.18 | Blocked until proof review accepts row control and father-field wording. |

## Hypothesis 2: Burgos/de la Cruz Row Controls Entry 172

Evidence supporting:

- The current converted Markdown explicitly reads entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.

Conflicts and limits:

- The assigned chunk, staged source packet, and conversion review contradict this as the controlling reading for the Pulgar/Arriagada task.
- No staged evidence links `Jose Miguel`, `Oswaldo Burgos`, or `Concepcion de la Cruz` to the Pulgar/Arriagada child or parents.
- This must not be treated as a Pulgar name variant.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.32 | Present in one derivative converted artifact, but contradicted by the assigned staged review set. |
| conflict_severity | 0.95 | Same entry number with an entirely different family. |
| evidence_quality | 0.42 | Single disputed derivative reading in this task context. |
| conversion_confidence | 0.35 | The converted Markdown is the artifact under conflict review. |
| claim_probability | 0.28 | Possible only if later original-image QA rejects the Pulgar/Arriagada row. |
| relevance | 1.00 | Direct competing row-control reading. |
| canonical_readiness | 0.08 | Not ready for Pulgar-line use. |

## Hypothesis 3: Same Person, Duplicate Person, Or Name Variant

Evidence supporting:

- Both readings share the local entry number `172`.

Conflicts and limits:

- The given names, surnames, parents, birth details, and informants do not align.
- `Jose Miguel` Burgos/de la Cruz is not supported as a variant of `Jose del Carmen Segundo Pulgar Arriagada`.
- A merge or duplicate-person resolution from this evidence would create a false composite identity.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.03 | The only overlap is the disputed row number. |
| conflict_severity | 0.98 | Conflation would corrupt both identity clusters. |
| evidence_quality | 0.20 | No shared identity-bearing evidence. |
| conversion_confidence | 0.20 | The issue is row control, not a personal name variation. |
| claim_probability | 0.02 | Same-person interpretation is unsupported. |
| relevance | 0.92 | Important anti-conflation conclusion. |
| canonical_readiness | 0.00 | Reject as a promotion path. |

## Pulgar-Line And Jose/Juana Comparison

- `Dario Arturo Pulgar-Smith`: canonical context identifies this person from family-supplied knowledge as Alexander John Heinz's maternal grandfather. Entry 172 does not name Dario, Arturo, Smith, Alexander, a spouse, a child, or a descendant bridge. Direct identity probability: 0.00; later family-line relevance if row 172 is certified: 0.30.
- `Dario Arturo Pulgar`: staged CV materials use this document-level name, but entry 172 does not name Dario Arturo or provide a CV/source-title bridge. Direct identity probability: 0.00; possible later line-context relevance: 0.25.
- `Dario Jose Pulgar-Arriagada`: staged photo/convention contexts mention this name separately. Entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Jose. Direct identity probability: 0.02.
- `Dario/Dario Pulgar Arriagada`: local staged and canonical contexts include `Dario Pulgar-Arriagada` or `Darío Pulgar Arriagada` in separate official-list/property contexts. Entry 172 provides no Dario given name, occupation, later residence, title, or same-person bridge. Direct identity probability: 0.02.
- `Jose del Carmen Pulgar`: if the Pulgar/Arriagada row controls, this is the father base-name field. Existing wiki context also has a separate `Jose del Carmen Pulgar` stub tied to `Tulio Cesar Luis Jose`; entry 172 alone does not prove all `Jose del Carmen Pulgar` references are one person. Staged father-field probability: 0.74; canonical readiness: 0.18.
- `Juana Arriagada de Pulgar`: if the Pulgar/Arriagada row controls, this is the mother field. Existing wiki context has a matching stub linked as probable mother of `Jose del Carmen Segundo Pulgar Arriagada`, but the row-control hold remains. Staged mother-field probability: 0.76; canonical readiness: 0.18.
- `Juana de Dios Amagada de Pulgar`: existing wiki context ties this separate candidate to `Tulio Cesar Luis Jose`. Entry 172 does not prove identity with `Juana Arriagada de Pulgar`; surname forms and child clusters must remain separate pending independent Jose/Juana parent-cluster proof review. Same-person probability from this task: 0.06.

## Conflict Summary

- Same-person conflict: no supported same-person merge between Pulgar/Arriagada and Burgos/de la Cruz readings.
- Duplicate-person risk: high if `Jose del Carmen Segundo Pulgar Arriagada` is merged into any Dario Pulgar candidate by surname pattern alone.
- Name-variant conflict: `Pulgar Arriagada`, `Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, and `Dario Pulgar-Arriagada` remain separate hypotheses.
- Relationship conflict: parent claims for `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` remain staged only; Burgos/de la Cruz parentage must not be attached to the Pulgar child.
- Chronology conflict: an 1888 birth entry for a Jose child does not bridge to later Dario candidates without independent identity-bearing evidence.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Required next step |
| ---: | --- | ---: | --- |
| 1 | Entry 172 controls as Pulgar/Arriagada | 0.72 | Original-image row-control QA plus proof review, including father suffix decision. |
| 2 | Entry 172 controls as Burgos/de la Cruz | 0.28 | Preserve as competing converted-Markdown reading until QA resolves row control. |
| 3 | Pulgar/Arriagada and Burgos/de la Cruz are same person/name variants | 0.02 | Reject as a promotion path; keep as anti-conflation warning. |
| 4 | Entry 172 directly bridges to any Dario Pulgar identity | 0.02 | Separate Pulgar-line identity-bridge proof review required. |
| 5 | `Juana Arriagada de Pulgar` equals `Juana de Dios Amagada de Pulgar` | 0.06 | Separate Jose/Juana parent-cluster review using independent evidence. |

## Recommended Next Action

Route `CHUNK-b8f4f0490a36-P0001-01`, register page 58, physical row entry 172, to targeted original-image row-control QA. The proof-review step must decide whether the controlling row is Pulgar/Arriagada or Burgos/de la Cruz and must explicitly record the father field as one of `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After proof review, promote only narrow birth-entry claims and stated-parent relationship candidates if accepted. Do not attach this row to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar-Arriagada`, or any broader Jose/Juana cluster without a separate identity-bridge proof-review step.
