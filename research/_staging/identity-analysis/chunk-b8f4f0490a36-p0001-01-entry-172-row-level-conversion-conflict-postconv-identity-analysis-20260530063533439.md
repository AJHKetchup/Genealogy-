---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260530063533439
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260530044358861.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260530044358861.md"
source_packet: "research/_staging/source-packets/sp-chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260530044358861.md"
conversion_review_note: "research/_staging/conversion-reviews/chunk-b8f4f0490a36-p0001-01-entry-172-targeted-row-control-qa-postconv-evidence-extraction-20260530044358861.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
page_reference: "page 1; register page 58; physical row entry 172"
promotion_recommendation: hold_for_conversion_qa
canonical_readiness: blocked
tags: [identity-analysis, conflict-review, row-control, pulgar]
---

# Identity And Conflict Analysis: Entry 172 Row-Control Conflict

## Blockers First

- The exact staged draft under review is `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260530044358861.md`.
- The latest source packet and conversion review both say the original source PNG was not present for that worker. The latest review therefore could not freshly certify the original image.
- The current converted Markdown at `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md` records entry 172 as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, born 6 April 1888.
- The chunk at `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md` records entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father field `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, born 8 March 1888.
- This is a row-control/conversion conflict, not a same-person, duplicate-person, or spelling-variant conflict. Do not attach Burgos/de la Cruz details to the Pulgar/Arriagada child, and do not promote Pulgar/Arriagada relationships until row-control QA and proof review accept a controlling reading.
- Existing canonical pages already contain low-confidence or draft auto-generated Pulgar/Arriagada evidence from this source cluster. This note does not make those pages promotion-ready.

## Literal Source Readings

Chunk reading:

```text
172 | Siete de Abril de mil ochocientos ochenta i ocho | Nombre. Jose del Carmen Segundo Pulgar Arriagada Sexo. Hombre | Fecha. Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde Lugar. Calle de Valdivia | Nombre del padre Jose del Carmen Pulgar S. Nac Chileno Prof Empleado Dom Calle de Colipi Nombre de la madre Juana Arriagada de Pulgar Nac Chilena Prof Su sexo Dom Calle de Colipi | Ernesto Herrera L. Presente al nacimiento Edad Veintiseis anos Prof Empleado Dom Calle de Valdivia
```

Converted Markdown reading:

```text
Entry 172: Nombres. Jose Miguel; father Oswaldo Burgos; mother Concepcion de la Cruz; birth 6 April 1888 at ten at night; place En esta.
```

Interpretation: these are competing row assignments for entry 172. They cannot both describe the same birth registration row.

## Hypothesis 1: Pulgar/Arriagada Is The Controlling Entry 172 Row

Supporting evidence:

- The assigned chunk explicitly transcribes entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888 and born 8 March 1888 at Calle de Valdivia.
- The latest source packet says existing staged crop assets support the base parent and informant fields for the Pulgar/Arriagada row.
- The latest conversion review says the staged crop `research/_staging/conversion-review-assets/chunk-b8f4f0490a36-entry-172-parent-fields-postconv-evidence-extraction-20260529000036877.png` visibly supports `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and `Ernesto Herrera L.`.
- Earlier local staged notes repeatedly describe image-reviewed or crop-supported Pulgar/Arriagada readings, though this worker did not rely on them as final certification.

Conflicts and limits:

- The latest worker could not locate the original source PNG for fresh source-image certification.
- The current converted Markdown materially disagrees and supplies an unrelated Burgos/de la Cruz family.
- The father-field suffix after `Jose del Carmen Pulgar` is not promotion-ready; preserve only the base name unless proof review certifies `S.` or another suffix.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.78 | Strong for a staged Pulgar/Arriagada row identity from the chunk and crop review; not final because original-image certification is missing in the latest review. |
| conflict_severity | 0.94 | The competing readings change child, parents, birth date/time/place, and informant. |
| evidence_quality | 0.68 | Useful staged chunk and crop evidence, but derivative and not freshly certified from the original source image here. |
| conversion_confidence | 0.52 | Chunk confidence is moderate-high; whole conversion confidence is reduced by the current converted Markdown conflict. |
| claim_probability | 0.72 | Probable staged reading, but not ready for canonical promotion. |
| relevance | 1.00 | Directly addresses the staged conflict draft. |
| canonical_readiness | 0.18 | Blocked pending row-control QA and proof review. |

## Hypothesis 2: Burgos/de la Cruz Is The Controlling Entry 172 Row

Supporting evidence:

- The current converted Markdown explicitly records entry 172 as `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`, born 6 April 1888.
- The converted file is the canonical conversion artifact currently referenced by the chunk metadata.

Conflicts and limits:

- The chunk for the same converted/source path now records the Pulgar/Arriagada row.
- The staged conflict draft, source packet, and conversion review all classify the Burgos/de la Cruz reading as a derivative row-control conflict.
- No staged family context connects Burgos/de la Cruz to the Pulgar/Arriagada child. Treating them as variants would create false parentage and chronology.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.32 | The converted Markdown is explicit, but it is isolated against the assigned chunk and staged crop-supported review. |
| conflict_severity | 0.94 | Same material row-control conflict as above. |
| evidence_quality | 0.42 | Single derivative conversion reading, contradicted by targeted review. |
| conversion_confidence | 0.35 | Low for entry 172 until the row-control conflict is resolved. |
| claim_probability | 0.28 | Possible only if later original-image QA rejects the Pulgar/Arriagada row. |
| relevance | 1.00 | Direct competing reading. |
| canonical_readiness | 0.08 | Not ready to promote or attach to this Pulgar-line task. |

## Hypothesis 3: Same-Person Or Name-Variant Link Between The Two Rows

Supporting evidence:

- Both readings are labeled entry 172 in local artifacts.

Conflicts and limits:

- Names, parents, birth details, and informants do not match.
- `Jose Miguel` with parents `Oswaldo Burgos` and `Concepcion de la Cruz` is not a plausible name variant of `Jose del Carmen Segundo Pulgar Arriagada` with parents `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`.
- No relationship evidence links the Burgos/de la Cruz family to the Pulgar/Arriagada family.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.03 | Same entry number only; all identity-bearing fields conflict. |
| conflict_severity | 0.98 | Merge would create a false composite person. |
| evidence_quality | 0.20 | The only commonality is artifact-level numbering. |
| conversion_confidence | 0.20 | Row-control uncertainty prevents identity use. |
| claim_probability | 0.02 | Same-person interpretation is effectively unsupported. |
| relevance | 0.92 | Important anti-conflation conclusion. |
| canonical_readiness | 0.00 | Do not merge or normalize. |

## Pulgar-Line Comparison

`Dario Arturo Pulgar-Smith`: canonical page is family-supplied as Alexander John Heinz's maternal grandfather and explicitly warns against attaching Dario/Pulgar/Pulgar-Arriagada records without identity review. Entry 172 does not name Dario Arturo, Smith, Alexander John Heinz, or a direct bridge to this person. Probability of direct same-person identity with the 1888 child is 0.00; probability of possible family-line relevance if Pulgar/Arriagada row is confirmed is 0.35.

`Dario Arturo Pulgar`: local CV tasks support a document-level `Dario Arturo Pulgar` cluster but repeatedly hold canonical attachment to Pulgar-Smith and warn against Pulgar-Arriagada merges by name alone. Entry 172 does not name Dario Arturo. Probability of direct identity is 0.00; possible future genealogical relevance is 0.25.

`Dario Jose Pulgar-Arriagada`: local ICRC/staged contexts use this form, but identity is not established from this entry. Entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Jose. The shared surname combination is a family-context lead only. Probability of direct identity is 0.02; possible family-line relevance after row QA is 0.30.

`Dario/Dario Pulgar Arriagada`: local canonical `wiki/people/dar-o-pulgar-arriagada.md` is a separate stub tied to a 2000 expropriation event, not this 1888 birth entry. No age/vital-date bridge links that person to the child or parents here. Probability of direct identity is 0.02; possible family-line relevance after row QA is 0.30.

`Jose del Carmen Pulgar`: if the Pulgar/Arriagada row is accepted, this is the likely father-name field, but the suffix after `Pulgar` must remain uncaptured or uncertain until proof review certifies it. Existing canonical `wiki/people/jose-del-carmen-pulgar.md` also has a separate draft child link to Tulio Cesar Luis Jose, so do not assume all Jose del Carmen Pulgar instances are the same person. Probability this entry names a father `Jose del Carmen Pulgar`: 0.74 staged / 0.18 canonical-ready.

`Juana Arriagada de Pulgar`: if the Pulgar/Arriagada row is accepted, this is the likely mother-name field. Existing canonical `wiki/people/juana-arriagada-de-pulgar.md` already has a low-confidence probable child link to Jose del Carmen Segundo Pulgar Arriagada from this source cluster, but it remains conversion-sensitive. Probability this entry names mother `Juana Arriagada de Pulgar`: 0.76 staged / 0.18 canonical-ready.

`Juana de Dios Amagada de Pulgar`: existing canonical page is a separate stub with draft evidence for child Tulio Cesar Luis Jose. The name resembles but does not match `Juana Arriagada de Pulgar`; do not correct or merge by family context. Probability of same person from this entry alone: 0.06.

## Conflict Summary

- Same-person conflict: no valid same-person merge between Pulgar/Arriagada and Burgos/de la Cruz readings.
- Duplicate-person risk: high if `Jose del Carmen Segundo Pulgar Arriagada` is treated as a duplicate of any Dario Pulgar candidate by surname context alone.
- Name-variant conflict: `Pulgar Arriagada`, `Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, and `Dario Pulgar Arriagada` remain separate hypotheses unless an identity-bearing bridge is reviewed.
- Relationship conflict: parent claims for `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` are staged only; Burgos/de la Cruz details must not be attached to the Pulgar child.
- Chronology conflict: none within the Pulgar/Arriagada row itself if accepted; major chronology risk would arise only from merging the 1888 child with later Dario candidates without vital-date evidence.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Action |
| ---: | --- | ---: | --- |
| 1 | Entry 172 controlling row is Pulgar/Arriagada | 0.72 | Hold for original-image row-control QA and proof review. |
| 2 | Entry 172 controlling row is Burgos/de la Cruz | 0.28 | Preserve as competing converted-Markdown reading until QA resolves it. |
| 3 | Pulgar/Arriagada and Burgos/de la Cruz are same person/name variants | 0.02 | Reject for promotion; use only as anti-conflation warning. |
| 4 | Entry 172 directly bridges to any Dario Pulgar identity | 0.02 | Do not merge; requires separate identity-bearing Pulgar-line proof review. |

## Recommended Next Action

Run the exact proof-review/conversion-QA step requested by the staged draft: original-image row-control certification for `CHUNK-b8f4f0490a36-P0001-01`, register page 58, physical row entry 172. The reviewer must decide the controlling row and explicitly certify whether the father field reads `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or another uncertain suffix.

Only after that row-control decision should a new proof-review or promotion step evaluate the narrow claims: child name/sex, birth date/time/place, father base name, mother name, informant, and any canonical relationship pages. A separate Pulgar-line identity bridge review is required before connecting this entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, or any Jose/Juana parent cluster beyond the literal row fields.
