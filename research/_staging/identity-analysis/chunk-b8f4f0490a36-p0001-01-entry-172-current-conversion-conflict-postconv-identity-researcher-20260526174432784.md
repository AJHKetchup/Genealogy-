---
type: identity_analysis
status: hold_for_conversion_qa
role: identity_researcher
worker: postconv-identity-analysis-20260526174432784
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526170352337.md"
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-current-conversion-conflict-postconv-evidence-extraction-20260526170352337.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-held-postconv-evidence-extraction-20260526170352337.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
created: 2026-05-26
---

# Identity Analysis: Entry 172 Current Conversion Conflict

## Blockers First

1. The staged conflict draft reports a material row-level conversion conflict. The assigned chunk and staged source packet read entry `172` as a Pulgar/Arriagada birth row, while the current converted Markdown reads entry `172` as a Burgos/de la Cruz row.
2. The competing readings change the child identity, birth date/time/place, father, mother, informant, and every dependent relationship candidate. This is not a same-person, duplicate-person, or spelling-variant issue.
3. The Pulgar/Arriagada father field is not fully certified. Preserve `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` as alternatives until targeted conversion QA decides the visible reading.
4. Existing wiki context for `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, and Jose/Juana parent candidates is context for later comparison only. This staged draft does not bridge entry 172 to any Dario candidate or broader parent cluster.
5. No child identity, parent-child relationship, duplicate-person conclusion, parent merge, Dario-line attachment, or canonical fact is ready until conversion QA decides which row controls entry `172`, followed by proof review.

## Literal Evidence

Staged conflict draft:

- Subject: `Entry 172, Los Angeles birth register, 1888`.
- Pulgar/Arriagada reading: child `Jose del Carmen Segundo Pulgar Arriagada`, male; born 8 March 1888 about 3 p.m. at `Calle de Valdivia`; father `Jose del Carmen Pulgar` with unresolved trailing mark; mother `Juana Arriagada de Pulgar`; informant `Ernesto Herrera L.`.
- Current converted Markdown reading: child `Jose Miguel`, male; born 6 April 1888 about 10 p.m. at `En esta`; father `Oswaldo Burgos`; mother `Concepcion de la Cruz`; informant `Oswaldo Burgos`.

Referenced source packet and chunk:

- The source packet states that assigned-chunk and image-reviewed evidence support entry number `172` on register page 58 as the Pulgar/Arriagada row.
- The assigned chunk transcribes entry `172` as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`, and informant `Ernesto Herrera L.`.

Referenced current converted Markdown:

- The converted file transcribes entry `172` as `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`, and informant `Oswaldo Burgos`.

Existing wiki context checked:

- `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied and warns against automatic merges with similar Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records.
- `wiki/people/dar-o-pulgar-arriagada.md` is a stub for `Dario/Dario Pulgar Arriagada` with a 5 December 2000 expropriation event and no entry-172 parent bridge.
- `wiki/people/dario-pulgar-adult-passenger-age-64.md` and `wiki/people/dario-pulgar-child-passenger-age-11.md` preserve separate 1953 passenger-list Dario Pulgar clusters.
- `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/juana-arriagada-de-pulgar.md`, `wiki/people/juana-de-dios-amagada-de-pulgar.md`, and `wiki/people/tulio-cesar-luis-jose.md` contain local Pulgar/Juana context, but the relevant links are draft, low-confidence, or tied to separate conversion-sensitive register clusters.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Row

Hypothesis: the controlling source row for entry `172` is the birth registration of `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar [?]` and `Juana Arriagada de Pulgar`.

Supporting evidence:

- The assigned chunk gives a complete Pulgar/Arriagada row for entry `172`.
- The staged source packet says image review supports the Pulgar/Arriagada row on register page 58.
- The registration date, child name, birth date/time/place, father, mother, and informant form an internally coherent civil birth-registration row.

Conflicts and limits:

- The current converted Markdown gives a complete but incompatible Burgos/de la Cruz row for the same entry number.
- The father's trailing mark is unresolved; `S.` must not be silently promoted as part of the name.
- Existing wiki snapshots based on this cluster remain blocked because row control is unresolved.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.64 | Strong assigned chunk/source-packet support, blocked by conflicting converted Markdown. |
| conflict_severity | 0.95 | Affects identity, parents, birth facts, informant, and all relationships. |
| evidence_quality | 0.72 | Local evidence includes chunk, source packet, and image-review statement, but derivatives disagree. |
| conversion_confidence | 0.38 | The core issue is row-level conversion conflict plus father-field uncertainty. |
| claim_probability | 0.66 | Probable if targeted QA confirms the assigned row. |
| relevance | 1.00 | Directly addresses the staged draft. |
| canonical_readiness | 0.15 | Hold until conversion QA and proof review. |

## Hypothesis 2: Entry 172 Is The Burgos/de la Cruz Row

Hypothesis: the controlling source row for entry `172` is the current converted Markdown row for `Jose Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.

Supporting evidence:

- The current converted Markdown supplies a complete entry `172` transcription with child, birth details, father, mother, and informant.

Conflicts and limits:

- The assigned chunk and staged source packet explicitly contradict this reading for the same entry number.
- The Burgos/de la Cruz reading appears to be a different row or source-control/conversion problem when compared with the assigned chunk and packet.
- If it is not the controlling row, it contains no Pulgar, Arriagada, Dario, Jose/Juana parent, or family-line evidence relevant to this task.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.28 | Present in the converted file, but contradicted by assigned evidence. |
| conflict_severity | 0.95 | If accepted, it displaces every Pulgar/Arriagada claim from entry 172. |
| evidence_quality | 0.50 | Complete derivative transcription, but unsupported against assigned chunk/source packet. |
| conversion_confidence | 0.25 | The converted file is the conflicted artifact. |
| claim_probability | 0.30 | Possible only if QA finds the chunk/source packet misassigned. |
| relevance | 0.75 | Relevant as the competing row, not as Pulgar-line evidence. |
| canonical_readiness | 0.05 | Hold; do not promote. |

## Hypothesis 3: Father Candidate `Jose del Carmen Pulgar [?]`

Hypothesis: the father in the Pulgar/Arriagada row is a parent candidate compatible with an existing `Jose del Carmen Pulgar` cluster, with the exact suffix unresolved.

Supporting evidence:

- The assigned chunk reads father `Jose del Carmen Pulgar S.`.
- The staged draft and source packet state that the image supports at least `Jose del Carmen Pulgar`, with a trailing mark.
- Existing `wiki/people/jose-del-carmen-pulgar.md` contains separate Pulgar parent-candidate context.

Conflicts and limits:

- The exact father-field reading is not certified.
- The existing `Jose del Carmen Pulgar` page has a separate draft child link to `Tulio Cesar Luis Jose`; this staged draft cannot merge father candidates across entries.
- The current converted Markdown names `Oswaldo Burgos` as father if that row controls.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.46 | Base name is supported in the Pulgar row, but suffix and cross-entry identity are unresolved. |
| conflict_severity | 0.72 | Wrong merge would create parent and duplicate-person errors. |
| evidence_quality | 0.56 | Direct row evidence is useful but conversion-sensitive. |
| conversion_confidence | 0.34 | Father suffix requires targeted QA. |
| claim_probability | 0.44 | Probable father-name candidate if Pulgar row controls; not ready as a merged person. |
| relevance | 0.90 | Direct parent candidate. |
| canonical_readiness | 0.10 | Hold for row QA, father-field QA, and proof review. |

## Hypothesis 4: Mother Candidate `Juana Arriagada de Pulgar`

Hypothesis: the mother in the Pulgar/Arriagada row is compatible with the existing `Juana Arriagada de Pulgar` stub.

Supporting evidence:

- The assigned chunk and staged source packet both read the mother as `Juana Arriagada de Pulgar`.
- Existing `wiki/people/juana-arriagada-de-pulgar.md` preserves an entry-172 child link to `Jose del Carmen Segundo Pulgar Arriagada`, marked probable with very low confidence.

Conflicts and limits:

- The canonical stub's entry-172 evidence depends on this same conflicted cluster; it is not independent corroboration.
- The current converted Markdown names `Concepcion de la Cruz` as mother if its row controls.
- Do not conflate `Juana Arriagada de Pulgar` with `Juana de Dios Amagada de Pulgar` or other Juana candidates from separate entries by family-context similarity.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.55 | Exact local name match, but not independently corroborated beyond the conflicted entry cluster. |
| conflict_severity | 0.74 | Wrong row choice changes the mother completely. |
| evidence_quality | 0.58 | Direct row support if Pulgar row controls; canonical support is derivative of the same cluster. |
| conversion_confidence | 0.38 | Row-level conversion conflict remains unresolved. |
| claim_probability | 0.52 | Plausible mother candidate only after row QA. |
| relevance | 0.92 | Direct parent candidate. |
| canonical_readiness | 0.12 | Hold for QA and proof review. |

## Hypothesis 5: Bridge To `Dario Arturo Pulgar-Smith` Or `Dario Arturo Pulgar`

Hypothesis: the entry-172 Pulgar/Arriagada row may connect to canonical family-supplied `Dario Arturo Pulgar-Smith` or document-level staged `Dario Arturo Pulgar`.

Supporting evidence:

- The row is Pulgar/Arriagada family-relevant if confirmed.
- Existing local context contains a family-supplied canonical `Dario Arturo Pulgar-Smith` page and staged CV analyses for document-level `Dario Arturo Pulgar`.

Conflicts and limits:

- Entry 172 does not name Dario, Arturo, Smith, Pulgar-Smith, a spouse, a child named Dario, a grandchild, Alexander John Heinz, or a CV source.
- Existing CV analyses keep `Dario Arturo Pulgar` to `Dario Arturo Pulgar-Smith` on hold pending an identity-bearing bridge.
- Family-line context can justify later comparison only; it cannot attach the 1888 birth row to Pulgar-Smith.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.05 | Shared broad Pulgar-line context only. |
| conflict_severity | 0.80 | Premature attachment would create a major identity and lineage error. |
| evidence_quality | 0.30 | No direct bridge in this staged draft. |
| conversion_confidence | 0.35 | Conversion QA would certify the row, not the Dario identity bridge. |
| claim_probability | 0.04 | Not supported as a same-person or relationship claim. |
| relevance | 0.72 | Required Pulgar-line anti-conflation comparison. |
| canonical_readiness | 0.00 | Do not attach or merge. |

## Hypothesis 6: Bridge To `Dario Jose Pulgar-Arriagada` Or `Dario/Dario Pulgar Arriagada`

Hypothesis: the entry-172 child or parents may connect to `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, or canonical `Dario/Dario Pulgar Arriagada`.

Supporting evidence:

- The confirmed Pulgar-row child name would include the surname combination `Pulgar Arriagada`.
- Existing wiki context has a `Dario/Dario Pulgar Arriagada` stub with a 2000 expropriation event.
- Prior local staging preserves Dario Jose/Pulgar-Arriagada and older medical/title clusters as unresolved Pulgar-line hypotheses.

Conflicts and limits:

- Entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Jose or Dario Pulgar Arriagada.
- The 2000 `Dario/Dario Pulgar Arriagada` stub has no age, parentage, or entry-172 bridge.
- `Dario Jose Pulgar-Arriagada` evidence in local staging is held or metadata-dependent and cannot be linked through this row by surname alone.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.03 | Only surname-cluster relevance. |
| conflict_severity | 0.78 | High conflation risk across Pulgar-Arriagada people. |
| evidence_quality | 0.28 | No direct bridge in this source. |
| conversion_confidence | 0.35 | Even confirmed row text would not name these Dario candidates. |
| claim_probability | 0.02 | Not supported as a same-person or relationship claim. |
| relevance | 0.70 | Required Pulgar-line comparison. |
| canonical_readiness | 0.00 | Do not attach or merge. |

## Hypothesis 7: Relationship To Jose/Juana Parent Candidates From Other Register Clusters

Hypothesis: entry 172 may connect to other Jose/Juana parent candidates, including `Jose del Carmen Pulgar`, `Juana de Dios Amagada de Pulgar`, `Juana Arriagada de Pulgar`, and related child `Tulio Cesar Luis Jose`.

Supporting evidence:

- Existing wiki pages preserve Pulgar/Juana parent-candidate context from separate staged register work.
- The name `Jose del Carmen Pulgar` overlaps with the entry-172 father reading if the Pulgar row controls.
- `Juana Arriagada de Pulgar` is directly named in the entry-172 Pulgar reading.

Conflicts and limits:

- Separate register clusters include conversion-sensitive child-name, mother-surname, and parent-field issues.
- `Juana de Dios Amagada de Pulgar` is not the same literal name as `Juana Arriagada de Pulgar`.
- This staged draft cannot infer spouse, sibling, ancestry, or duplicate-person status across Jose/Juana candidates until each source is proof-reviewed and a bridge is stated.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.18 | Some direct father/mother name overlap, but broader Jose/Juana linkage is unproved. |
| conflict_severity | 0.70 | Unsupported parent merges would distort the Pulgar line. |
| evidence_quality | 0.40 | Local context exists but is spread across held or draft clusters. |
| conversion_confidence | 0.32 | Multiple related register readings are conversion-sensitive. |
| claim_probability | 0.16 | Limited to future comparison, not present promotion. |
| relevance | 0.82 | Directly relevant to parent-candidate guardrails. |
| canonical_readiness | 0.03 | Hold; no relationship promotion. |

## Conflict Summary

- Same-person conflict: `Jose del Carmen Segundo Pulgar Arriagada` and `Jose Miguel` are competing row readings with different parents and birth details. Treat them as different candidate rows, not one child with variant names.
- Duplicate-person risk: high if `Jose del Carmen Pulgar S.` is merged into a suffix-free `Jose del Carmen Pulgar` cluster, or if Juana/Pulgar candidates from separate entries are merged before row and field QA.
- Name-variant conflict: `Jose del Carmen Pulgar` versus `Jose del Carmen Pulgar S.` is a transcription issue. `Pulgar Arriagada`, `Pulgar-Smith`, `Dario Arturo Pulgar`, and `Dario Jose Pulgar-Arriagada` are not proved variants here.
- Relationship conflict: the competing rows name wholly different parent pairs: `Jose del Carmen Pulgar [?]` and `Juana Arriagada de Pulgar` versus `Oswaldo Burgos` and `Concepcion de la Cruz`.
- Chronology conflict: the Pulgar/Arriagada reading gives birth on 8 March 1888, while the current converted Markdown gives birth on 6 April 1888.
- Conversion conflict: the row-control disagreement is severe enough that all dependent claims remain on hold.

## Overall Scores

| Category | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.64 | Highest for the Pulgar/Arriagada row as assigned, but blocked by contradictory converted Markdown. |
| conflict_severity | 0.95 | The conflict changes the full identity and family structure of entry 172. |
| evidence_quality | 0.70 | Good local staged evidence, but unsettled because derivatives disagree. |
| conversion_confidence | 0.35 | Row-level conversion QA is required before proof review can promote anything. |
| claim_probability | 0.66 | Pulgar/Arriagada is probable if assigned chunk/source-packet image review is certified. |
| relevance | 0.95 | Directly relevant to Pulgar/Arriagada and required Dario-line anti-conflation work. |
| canonical_readiness | 0.10 | Not ready for canonical promotion or merge. |

## Ranked Hypotheses

| Rank | Hypothesis | Probability | Required next proof-review or promotion step |
| ---: | --- | ---: | --- |
| 1 | Entry 172 is the Pulgar/Arriagada row for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.66 | Targeted conversion QA must decide row control and certify the father field. |
| 2 | Entry 172 is the Burgos/de la Cruz row for `Jose Miguel`. | 0.30 | Hold as competing conversion reading; promote only if QA rejects the Pulgar/Arriagada row. |
| 3 | Father is a `Jose del Carmen Pulgar [?]` candidate compatible with existing Jose del Carmen Pulgar context. | 0.44 | After row QA, run proof review on the exact father field and a separate identity bridge before any merge. |
| 4 | Mother is `Juana Arriagada de Pulgar`, compatible with the existing stub of that literal name. | 0.52 | After row QA, run parent-child proof review before promotion. |
| 5 | Entry 172 bridges to `Dario Arturo Pulgar-Smith` or document-level `Dario Arturo Pulgar`. | 0.04 | Require an independent identity-bearing bridge; do not attach from this draft. |
| 6 | Entry 172 bridges to `Dario Jose Pulgar-Arriagada` or `Dario/Dario Pulgar Arriagada`. | 0.02 | Preserve as later surname-cluster comparison only; require direct continuity evidence. |
| 7 | Entry 172 resolves broader Jose/Juana parent candidates from other entries. | 0.16 | Compare only after each register cluster is proof-reviewed; do not infer relationships here. |

## Recommended Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image, assigned chunk, current converted Markdown, staged source packet, and staged conflict draft. The QA result must decide which row controls entry `172` and certify the father field only to the visible extent: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, run proof review before promoting any child identity, birth fact, parent-child relationship, same-person conclusion, duplicate-person decision, parent merge, or canonical attachment. The next Pulgar-line proof-review step must explicitly compare the certified entry-172 evidence against `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, `Juana de Dios Amagada de Pulgar`, and related Jose/Juana candidates, preserving separate hypotheses unless a direct bridge is found.
