---
type: identity_conflict_analysis
status: draft
role: identity_researcher
task_id: identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526171029823.md
worker: postconv-identity-analysis-20260526173035518
staged_draft: research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526171029823.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526171029823.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
chunk_id: CHUNK-b8f4f0490a36-P0001-01
canonical_readiness: hold_for_conversion_qa
---

# Identity/Conflict Analysis: Entry 172 Current Conversion Conflict

## Blockers

- The assigned staged draft is a row-level conversion conflict, not a simple same-person, duplicate-person, or name-variant case. The assigned chunk/source packet support a Pulgar/Arriagada row for entry `172`; the current converted Markdown supports a different Burgos/de la Cruz row for entry `172`.
- Do not promote dependent child identity, birth facts, parent-child relationships, parent pair claims, Dario-line comparisons, or canonical wiki edits until targeted conversion QA certifies the controlling row for entry `172`.
- The father field requires targeted visual certification. The assigned chunk reads `Jose del Carmen Pulgar S.` and the staged draft/source packet say the image has a trailing mark compatible with `S.`, but the safe proof-review wording remains `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]` until QA resolves it.
- Existing wiki snapshots already contain staged-looking facts for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar`, but this analysis should not treat those as promotion authority because the current staged draft is explicitly held for conversion QA.
- This source does not name `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario Pulgar Arriagada`, `Dario Pulgar A.`, or any relationship from the 1888 child/parents to a Dario-line person.

## Literal Evidence From Assigned Materials

- Staged draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526171029823.md`.
- Source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526171029823.md`.
- Assigned chunk literal row for page 58, entry `172`: child `Jose del Carmen Segundo Pulgar Arriagada`, male; registration `Siete de Abril de mil ochocientos ochenta i ocho`; birth `Ocho de Marzo de mil ochocientos ochenta i ocho`, about `tres de la tarde`, `Calle de Valdivia`; father `Jose del Carmen Pulgar S.`; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`, present at birth, age 26, employee, resident at `Calle de Valdivia`.
- Current converted Markdown row for entry `172`: child `José Miguel`; birth `El seis de Abril de mil ochocientos ochenta i ocho`, about `diez de la noche`, `En esta`; father `Oswaldo Burgos`; mother `Concepcion de la Cruz`; informant `Oswaldo Burgos`.
- Direct full-page visual check in this analysis corroborated that page 58 entry `172` is the Pulgar/Arriagada row rather than the Burgos/de la Cruz row, but this was not a formal conversion QA pass and does not certify the father suffix.
- Existing canonical/staged context includes pages for `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/juana-arriagada-de-pulgar.md`, and `wiki/people/dario-arturo-pulgar-smith.md`. The Pulgar-Smith page is family supplied and explicitly cautions against attaching similarly named Pulgar records without identity review.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Registration

Interpretation: strongest narrow hypothesis. The controlling row for entry `172` is probably the Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar`/`Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`, but dependent claims remain held until conversion QA certifies the row and father field.

Supporting evidence:

- Assigned chunk and source packet agree on the Pulgar/Arriagada row.
- The staged draft reports source-image support for the Pulgar/Arriagada row and identifies the Burgos/de la Cruz row as the current converted Markdown conflict.
- Direct full-page visual check in this analysis also supports the Pulgar/Arriagada row location for entry `172`.
- The row supplies internally coherent birth-register details: child, registration date, birth date/time/place, father, mother, informant, residences, and official context.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.83 | Strong for row-local child identity if the assigned chunk/source image are controlling; held because converted Markdown conflicts. |
| conflict_severity | 0.94 | The conflict changes child, birth date/time/place, father, mother, and informant. |
| evidence_quality | 0.78 | Civil birth registration plus chunk/source packet and visual row corroboration; father suffix remains uncertain. |
| conversion_confidence | 0.46 | Assigned chunk confidence is high, but current converted Markdown is materially inconsistent. |
| claim_probability | 0.82 | Pulgar/Arriagada is probably the correct row, pending formal QA. |
| relevance | 1.00 | Directly addresses the staged draft. |
| canonical_readiness | 0.18 | Hold; no canonical promotion before conversion QA and proof review. |

## Hypothesis 2: Entry 172 Is The Burgos/de la Cruz Row In Current Converted Markdown

Interpretation: low probability from the assigned evidence. The current converted Markdown may be carrying text from a different image, row, or conversion state, but this analysis found no staged support for treating the Burgos/de la Cruz row as controlling for the assigned source image.

Supporting evidence:

- The current converted Markdown explicitly labels entry `172` as `José Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
- The converted file is the authoritative converted Markdown path referenced by the staged draft and source packet.

Counter-evidence / limits:

- The assigned chunk, source packet, staged draft, and direct full-page visual check point to the Pulgar/Arriagada row for page 58, entry `172`.
- The Burgos/de la Cruz row conflicts across all identity-bearing and relationship-bearing fields.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.12 | Only the current converted Markdown supports this row for the assigned entry. |
| conflict_severity | 0.94 | If promoted, it would attach an entirely different family to entry `172`. |
| evidence_quality | 0.30 | One conflicting conversion output against stronger assigned chunk/source-packet evidence. |
| conversion_confidence | 0.20 | The converted row appears materially mismatched to the assigned source context. |
| claim_probability | 0.10 | Possible conversion-state artifact, not supported as controlling. |
| relevance | 1.00 | This is the conflicting reading under review. |
| canonical_readiness | 0.00 | Do not promote from this conflict state. |

## Hypothesis 3: Jose del Carmen Segundo Pulgar Arriagada Is The Existing Wiki Stub Person

Interpretation: probable if conversion QA confirms the Pulgar/Arriagada row. Existing wiki context already has a stub for `Jose del Carmen Segundo Pulgar Arriagada` with the same row-derived birth and mother evidence, but this analysis should not silently treat that as a completed identity attachment.

Supporting evidence:

- The existing wiki stub `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` has the same preferred name as the assigned row.
- Its evidence snapshot points to the same chunk/source-packet family for birth name, birth date/time, birth place, sex, and mother relationship.
- Existing parent stubs for `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` match the assigned row's parent candidates.

Counter-evidence / limits:

- The current staged draft recommends `hold_for_conversion_qa`.
- The wiki snapshot lists low or unknown confidence for some row-derived facts and does not resolve the current converted Markdown conflict.
- Father suffix/name-form remains uncertified.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.72 | Name and row-derived context match, but conversion QA is still open. |
| conflict_severity | 0.70 | Premature canonical use could embed a row conflict in the person page. |
| evidence_quality | 0.62 | Existing wiki context is derivative of the same unresolved source cluster. |
| conversion_confidence | 0.46 | Same row-level conversion conflict controls readiness. |
| claim_probability | 0.70 | Likely same staged person if Pulgar row is certified. |
| relevance | 0.90 | Direct canonical candidate for the row child. |
| canonical_readiness | 0.20 | Hold until conversion QA plus proof review. |

## Hypothesis 4: Jose/Juana Parent Candidates From This Row Are A Stable Parental Pair

Interpretation: plausible row-local parent pair, not yet promotion-ready. The assigned row names a father and mother, but relationship promotion depends on the same row-control decision and father-field certification.

Supporting evidence:

- Assigned chunk/source packet name father `Jose del Carmen Pulgar S.` or `Jose del Carmen Pulgar` with a possible suffix.
- Assigned chunk/source packet name mother `Juana Arriagada de Pulgar`.
- The parent residences and attributes are internally coherent in the row: Chilean, father employee, mother `Su sexo`, both at `Calle de Colipi`.
- Existing wiki stubs contain these parent candidates and a probable mother-child link.

Counter-evidence / limits:

- The current converted Markdown supplies entirely different parents: `Oswaldo Burgos` and `Concepcion de la Cruz`.
- Father suffix is not certified.
- No independent same-person bridge was reviewed here for `Jose del Carmen Pulgar` across other wiki children or for `Juana Arriagada de Pulgar` beyond this row.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.68 | Good row-local support, but not yet cross-record identity proof. |
| conflict_severity | 0.88 | Parent relationships are directly affected by the row conflict. |
| evidence_quality | 0.66 | Civil-register row evidence is strong if controlling; father suffix remains uncertain. |
| conversion_confidence | 0.46 | Row conflict prevents promotion. |
| claim_probability | 0.67 | Plausible after QA, not ready now. |
| relevance | 0.95 | Directly controls parent-child relationship candidates. |
| canonical_readiness | 0.16 | Hold all parent relationship promotion. |

## Hypothesis 5: Same Person Or Direct Identity Bridge To Dario-Line Candidates

Interpretation: unsupported by this source. The row may later become useful Pulgar-line context, but it does not itself name or bridge to any Dario candidate. Do not merge by surname, Arriagada surname, or family-context hint.

Required comparisons:

- `Dario Arturo Pulgar-Smith`: canonical family-supplied maternal-grandfather page exists, but this 1888 row does not state `Dario`, `Arturo`, `Smith`, Alexander John Heinz, or a grandchild relationship. Same-person probability with the 1888 child is effectively nil from this source; ancestor/lineage relevance is only contextual.
- `Dario Arturo Pulgar`: staged CV context elsewhere names `Dario Arturo Pulgar`, but this birth row does not name him or provide a document-level bridge to the CV subject. Same-person probability with the 1888 child is effectively nil from this source; possible lineage relevance requires later proof-reviewed relationship evidence.
- `Dario Jose Pulgar-Arriagada` / `Dario J. Pulgar Arriagada` / `Dario Pulgar-Arriagada`: the shared `Pulgar Arriagada` elements justify an anti-conflation check, especially because an 1888-born person could be chronologically plausible for some early twentieth-century Dario/J. contexts. However, this source names the child `Jose del Carmen Segundo Pulgar Arriagada`, not `Dario`, `Dario Jose`, or `Dario J.`.
- `Dario/Darío Pulgar Arriagada`: existing canonical/staged context includes a later `Darío Pulgar Arriagada` cluster, but this row does not prove that `Jose del Carmen Segundo Pulgar Arriagada` used `Dario` or was the same person.
- Jose/Juana parent candidates: the row may identify parents for the 1888 child if certified, but it does not prove those parents are ancestors, parents, or relatives of any Dario-line candidate.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.08 | No Dario name or direct identity bridge appears in the row. |
| conflict_severity | 0.76 | A name-only or surname-only merge could conflate generations and unrelated source clusters. |
| evidence_quality | 0.22 | Dario comparison is contextual only; the assigned row is not Dario-bearing. |
| conversion_confidence | 0.46 | Even row-local facts are held, and Dario facts are absent. |
| claim_probability | 0.06 | No same-person Dario claim is supported here. |
| relevance | 0.72 | Required Pulgar-line anti-conflation check; not direct evidence. |
| canonical_readiness | 0.00 | No Dario attachment, merge, or variant promotion. |

## Conflicts

- Same-person conflict: no Dario same-person claim is supported. The meaningful same-person question is whether the row child should attach to the existing `Jose del Carmen Segundo Pulgar Arriagada` stub after conversion QA.
- Duplicate-person risk: moderate for duplicate staged/wiki handling of `Jose del Carmen Segundo Pulgar Arriagada`; high risk if merged with Dario Arturo, Dario Jose, Dario J., Dario/Dario Pulgar Arriagada, or Pulgar-Smith by name elements alone.
- Name-variant conflict: this row supports `Jose del Carmen Segundo Pulgar Arriagada`; it does not support `Dario`, `Arturo`, `Smith`, `Dario Jose`, `Dario J.`, or `Dario Pulgar A.` as variants.
- Relationship conflict: severe row-level parent conflict between `Jose del Carmen Pulgar` / `Juana Arriagada de Pulgar` and `Oswaldo Burgos` / `Concepcion de la Cruz`.
- Chronology conflict: row-local Pulgar chronology is coherent if certified. Cross-cluster Dario chronology remains unproved; do not infer that an 1888-born Pulgar Arriagada is any later Dario without an identity-bearing source.
- Conversion conflict: material. Assigned chunk/source packet/source image support one row; current converted Markdown records a different row for the same entry number.

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Disposition |
| ---: | --- | ---: | --- |
| 1 | Entry `172` is the Pulgar/Arriagada birth row for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.82 | Hold for targeted conversion QA and father-field certification. |
| 2 | The row child is the same staged/wiki person as `Jose del Carmen Segundo Pulgar Arriagada`. | 0.70 | Probable after QA; do not promote yet. |
| 3 | `Jose del Carmen Pulgar`/`Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar` are the row-local parents. | 0.67 | Hold for row-control QA and father suffix proof review. |
| 4 | The current converted Markdown Burgos/de la Cruz row is controlling for this source/entry. | 0.10 | Treat as conversion conflict pending QA, not promotion evidence. |
| 5 | The row child or parents directly bridge to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, or `Dario/Dario Pulgar Arriagada`. | 0.06 | Preserve as unresolved/contextual only; no merge or attachment. |

## Recommended Next Action

Keep the staged draft on `hold_for_conversion_qa`. The exact next proof-review/promotion step is targeted conversion QA comparing the source image, current converted Markdown, assigned chunk, and staged source packet to certify the controlling row for entry `172` and record the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After conversion QA, rerun proof review on the child identity, birth date/time/place, father claim, mother claim, informant claim, parent-child relationships, and possible parent-pair clue. Only after that proof review should any canonical attachment be considered for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, or `Juana Arriagada de Pulgar`.

Before any Pulgar-line promotion, run a separate identity-bridge review that explicitly compares the certified row against `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario/Dario Pulgar Arriagada`, and the Jose/Juana parent candidates. Do not merge these people by name alone.
