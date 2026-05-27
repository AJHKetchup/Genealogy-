---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: "postconv-identity-analysis-20260527224037974"
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-postconv-evidence-extraction-20260527221218880.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-postconv-evidence-extraction-20260527221218880.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-rowcert-postconv-evidence-extraction-20260527221218880.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
canonical_readiness: hold_for_proof_review
promotion_recommendation: promote_after_review
created: 2026-05-27
---

# Identity And Conflict Analysis: Entry 172 Derivative Row Conflict

## Blockers First

- The exact staged conflict draft reports a material row-control conflict: the assigned chunk and row-certified source packet identify physical entry `172` as a Pulgar/Arriagada birth registration, while the current converted Markdown identifies entry `172` as a Burgos/de la Cruz row.
- This is not a same-person, duplicate-person, or name-variant conflict. The competing readings differ on child, parents, birth date/time, birthplace, and informant.
- The row-certified packet says the original source image controls this staging pass and supports the Pulgar/Arriagada row, but the active converted Markdown remains contradictory. Any canonical promotion still needs proof review that explicitly accepts the row-certified packet over the stale or misaligned converted Markdown.
- The father field is bounded to `Jose del Carmen Pulgar`. The trailing `S.` in the chunk is not promoted and still needs a targeted proof-review decision as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- This entry does not name `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, or `Darío Pulgar Arriagada`. Pulgar-line family context supports anti-conflation review only, not a Dario identity bridge.
- Existing wiki pages for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar` are local context, not authority to silently resolve the row conflict or merge parent candidates.

## Evidence Reviewed

- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-derivative-row-conflict-postconv-evidence-extraction-20260527221218880.md`.
- Row-certified source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-rowcert-postconv-evidence-extraction-20260527221218880.md`.
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Existing canonical context: `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/juana-arriagada-de-pulgar.md`, `wiki/people/juana-de-dios-amagada-de-pulgar.md`, `wiki/people/dario-arturo-pulgar-smith.md`, `wiki/people/dar-o-pulgar-arriagada.md`, `wiki/people/dario-pulgar-child-passenger-age-11.md`, and `wiki/people/dario-pulgar-adult-passenger-age-64.md`.

## Literal Source Readings

### Assigned Chunk And Row-Certified Packet

- Entry number: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`.
- Birthplace: `Calle de Valdivia`.
- Father field: chunk reads `Jose del Carmen Pulgar S.`; row-certified packet stages only `Jose del Carmen Pulgar`.
- Mother field: `Juana Arriagada de Pulgar`.
- Informant: `Ernesto Herrera L.`, present at birth, age 26, employed, resident at `Calle de Valdivia`.

### Current Converted Markdown

- Entry number: `172`.
- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose Miguel`; sex `Varon`.
- Birth: `El seis de Abril de mil ochocientos ochenta i ocho, a las diez de la noche`.
- Birthplace: `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Informant/declarant: `Oswaldo Burgos`.

## Hypothesis 1: Physical Entry 172 Is The Pulgar/Arriagada Row

Evidence supporting:

- The exact row-certified packet says the original image and assigned chunk identify physical row `172` as `Jose del Carmen Segundo Pulgar Arriagada`, son of a Pulgar father and Arriagada mother.
- The assigned chunk gives a coherent civil-register row: registration date, child name/sex, birth date/time/place, parent fields, and informant details all align with the Pulgar/Arriagada row.
- Existing canonical pages already contain local Pulgar/Arriagada context for the child and mother, which is consistent with this reading.

Conflicts and limits:

- The current converted Markdown still records a different `172` row.
- The father suffix after `Pulgar` remains unaccepted.
- Existing wiki context does not prove that `Jose del Carmen Pulgar` in this row is the same person as any other Jose Pulgar candidate.

Scores:

| Metric | Score | Judgment |
| --- | ---: | --- |
| identity_confidence | 0.86 | Strong for the child/mother row if the row-certified packet is accepted. |
| conflict_severity | 0.95 | Wrong row control would attach the wrong child, parents, date, place, and informant. |
| evidence_quality | 0.84 | Civil-registration row plus image-reviewed packet and chunk agreement. |
| conversion_confidence | 0.68 | Improved by row certification, still limited by contradictory converted Markdown. |
| claim_probability | 0.86 | Most likely controlling reading for this staged Pulgar task. |
| relevance | 0.99 | Directly governs the staged conflict draft. |
| canonical_readiness | 0.55 | Potentially promotable only after proof review accepts row control and father boundary. |

## Hypothesis 2: Entry 172 Is The Burgos/de la Cruz Row

Evidence supporting:

- The current converted Markdown explicitly assigns entry `172` to `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
- The converted file is still the active derivative conversion referenced in the staged conflict metadata.

Conflicts and limits:

- The row-certified packet says the current converted Markdown is not the controlling reading for the physical Pulgar/Arriagada row.
- The Burgos/de la Cruz reading has no Pulgar/Arriagada family relevance unless proof review rejects the row-certified packet or proves a source-assignment problem.

Scores:

| Metric | Score | Judgment |
| --- | ---: | --- |
| identity_confidence | 0.18 | Low as the controlling identity for this Pulgar-line task. |
| conflict_severity | 0.95 | Direct contradiction of every core family field. |
| evidence_quality | 0.35 | Derivative conversion only, contradicted by assigned chunk and row-certified packet. |
| conversion_confidence | 0.30 | The conversion artifact is the source of the conflict. |
| claim_probability | 0.14 | Preserved only as the conflicting derivative reading. |
| relevance | 0.20 | Relevant to conversion QA, not to Pulgar identity unless it controls. |
| canonical_readiness | 0.03 | Do not promote from this task. |

## Hypothesis 3: The Two Readings Are Same-Person Or Name Variants

Evidence supporting:

- None beyond sharing the entry number `172` and registration date in conflicting derivative artifacts.

Conflicts and limits:

- `Jose del Carmen Segundo Pulgar Arriagada` is not a plausible variant of `Jose Miguel`.
- `Jose del Carmen Pulgar` is not a plausible variant of `Oswaldo Burgos`.
- `Juana Arriagada de Pulgar` is not a plausible variant of `Concepcion de la Cruz`.
- Birth date, birth time, place, and informant also differ.

Scores:

| Metric | Score | Judgment |
| --- | ---: | --- |
| identity_confidence | 0.01 | No same-person basis. |
| conflict_severity | 0.95 | Treating them as variants would create severe false relationships. |
| evidence_quality | 0.90 | The rejection is well supported by direct field disagreement. |
| conversion_confidence | 0.68 | Row-control conflict explains the disagreement better than identity variation. |
| claim_probability | 0.01 | Reject as identity hypothesis. |
| relevance | 0.95 | Important anti-merge finding. |
| canonical_readiness | 0.00 | Do not merge or normalize. |

## Hypothesis 4: The Pulgar/Arriagada Row Provides A Dario-Line Bridge

Evidence supporting:

- Only broad surname context: the row contains `Pulgar` and `Arriagada`, and the broader workspace has several unresolved Dario/Pulgar/Pulgar-Arriagada clusters.

Conflicts and limits:

- The row names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario.
- It gives no `Arturo`, `Smith`, `Dario Jose`, `Dario J.`, `Dario Pulgar A.`, Alexander Heinz relationship, spouse, child, or descendant bridge.
- The 1888 child identity cannot be attached to modern Dario clusters by surname pattern alone.

Scores:

| Metric | Score | Judgment |
| --- | ---: | --- |
| identity_confidence | 0.03 | No direct Dario bridge in this source. |
| conflict_severity | 0.70 | High risk of long-range Pulgar-line conflation. |
| evidence_quality | 0.18 | Surname context only. |
| conversion_confidence | 0.68 | Even accepting H1 does not create a Dario bridge. |
| claim_probability | 0.02 | Unsupported from this draft. |
| relevance | 0.65 | Required anti-conflation check. |
| canonical_readiness | 0.00 | No Dario attachment. |

## Pulgar-Line Required Comparison

| Candidate | Local evidence context | Relation to this draft | Probability / confidence | Required next step |
| --- | --- | --- | ---: | --- |
| `Dario Arturo Pulgar-Smith` | Canonical family-supplied maternal grandfather of Alexander John Heinz; page warns against automatic merge with Dario/Pulgar clusters. | Not named. No Smith, Arturo, Alexander, or family bridge appears in entry 172. | 0.01 | Separate identity-bridge proof review only; no action from this entry. |
| `Dario Arturo Pulgar` | Existing staged CV/document-title cluster elsewhere. | Not named. No CV/work-history evidence appears here. | 0.02 | Require proof-reviewed bridge from CV subject to canonical person before attachment. |
| `Dario Jose Pulgar-Arriagada` | Existing local photograph/portrait/Geneva context elsewhere. | Not named. Shared Pulgar-Arriagada pattern only. | 0.02 | Preserve separately unless a proof-reviewed identity chain connects them. |
| `Dario/Dario Pulgar Arriagada` / `Darío Pulgar Arriagada` | Existing wiki page has a 2000 expropriation event for `Darío Pulgar Arriagada`; other staged records use related Dario forms. | Not named. No chronological, property, parent, or residence bridge from entry 172. | 0.03 | Do not merge; require chronological and relational bridge evidence. |
| `Jose del Carmen Pulgar` | Under H1, the father field is staged as `Jose del Carmen Pulgar`, with possible suffix unresolved. Existing wiki has a separate draft child link to `Tulio Cesar Luis Jose`. | Strong father-name candidate for this row only. Broader same-person comparison to other Jose records is unresolved. | 0.86 as row father; 0.35 as broader merge | Proof review must certify row control and father field, then compare Jose parent candidates side by side. |
| `Juana Arriagada de Pulgar` | Under H1, the assigned chunk and row-certified packet name her as mother. Existing wiki has a probable child link to `Jose del Carmen Segundo Pulgar Arriagada`. | Strong mother candidate if the Pulgar/Arriagada row controls. | 0.88 | Proof review should accept scoped child-mother relationship before any broader Juana merge. |
| `Juana de Dios Amagada de Pulgar` | Existing wiki/staged context names her in a separate Pulgar parent cluster. | Not named in entry 172. Similar married-style `de Pulgar` is not enough to substitute for `Juana Arriagada de Pulgar`. | 0.12 | Do not merge; require side-by-side proof review of Juana records and name forms. |

## Relationship And Chronology Conflicts

- Same-entry conflict: entry `172` maps to two incompatible rows across local artifacts.
- Relationship conflict: H1 gives parents `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`; H2 gives parents `Oswaldo Burgos` and `Concepcion de la Cruz`.
- Chronology conflict: H1 birth is 1888-03-08 at 3 p.m.; H2 birth is 1888-04-06 at 10 p.m.
- Place conflict: H1 gives `Calle de Valdivia`; H2 gives `En esta`.
- Informant conflict: H1 gives `Ernesto Herrera L.`; H2 gives `Oswaldo Burgos`.
- Name-variant conflict: none of the H2 names are plausible variants of the H1 names.
- Parent-candidate conflict: do not merge `Juana Arriagada de Pulgar` with `Juana de Dios Amagada de Pulgar`, or `Jose del Carmen Pulgar` with other Jose Pulgar candidates, from this row alone.

## Ranked Conclusion

| Rank | Hypothesis | Probability | Action |
| ---: | --- | ---: | --- |
| 1 | The active issue is conversion/row control, not duplicate identity. | 0.94 | Preserve conflict and prevent automatic merge or promotion. |
| 2 | Physical entry 172 is the Pulgar/Arriagada row described by the assigned chunk and row-certified packet. | 0.86 | Send to proof review for row-control acceptance and scoped promotion. |
| 3 | Father should be staged only as `Jose del Carmen Pulgar` pending suffix review. | 0.82 | Do not promote `S.` or merge father candidates. |
| 4 | The converted Markdown's Burgos/de la Cruz row controls this Pulgar task. | 0.14 | Keep only as the conflicting derivative reading unless proof review reverses row control. |
| 5 | Entry 172 bridges to a Dario Pulgar identity. | 0.02 | Unsupported; require separate identity-bridge proof review. |

## Recommended Next Action

Exact next proof-review step: review the row-certified source packet against the original image, assigned chunk, and current converted Markdown, then issue a proof-review note that explicitly accepts or rejects the packet's statement that physical row `172` is the Pulgar/Arriagada row and that the converted Markdown's Burgos/de la Cruz row is stale, row-shifted, or misassigned.

The same review must separately certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After that, run scoped promotion review for the child birth-name/sex, birth date/time/place, child-mother relationship, child-father relationship, and Jose/Juana parent-candidate comparison. Do not attach this entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario Pulgar Arriagada` without a separate proof-reviewed identity bridge.
