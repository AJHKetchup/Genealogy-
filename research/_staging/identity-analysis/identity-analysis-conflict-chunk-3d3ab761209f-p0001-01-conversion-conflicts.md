---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/conflicts/conflict-chunk-3d3ab761209f-p0001-01-conversion-conflicts.md
staged_draft: research/_staging/conflicts/conflict-chunk-3d3ab761209f-p0001-01-conversion-conflicts.md
source_packet: research/_staging/source-packets/sp-chunk-3d3ab761209f-p0001-01-los-angeles-birth-register-page-172.md
source_path: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1889, Certificate No. 513..png
converted_file: raw/converted/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513.codex.md
chunk: raw/chunks/ca05d0627a-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificate-no-513-codex/page-0001-chunk-01.md
chunk_id: CHUNK-3d3ab761209f-P0001-01
analysis_status: hold
canonical_readiness: hold
---

# Identity Analysis: Conflict Chunk 3d3ab761209f P0001-01

## Blockers

- Exact staged draft analyzed: `research/_staging/conflicts/conflict-chunk-3d3ab761209f-p0001-01-conversion-conflicts.md`.
- This analysis uses staged drafts, referenced converted/chunk/source files, proof-review notes, and existing canonical wiki pages only. No external research was performed.
- The assigned chunk and current assembled converted Markdown materially disagree on identity-bearing fields for entries 513-515. The staged conflict draft reports that the source image supports the assigned chunk more than the assembled converted Markdown, but several readings remain image-sensitive.
- Entry 513 is Pulgar-line relevant, but not promotion-ready: the source packet says the image supports a `Pulgar Ama...` surname line, a given-name line beginning `Jose ...`, father `Jose del Carmen Pulgar`, and a mother line best read as `Juana de Dios Amagada de Pulgar`, with the child full name, mother surname, and birth time still requiring targeted QA.
- Existing wiki context contains separate Pulgar-related pages for `Dario Arturo Pulgar-Smith`, `Darío Pulgar Arriagada`, `Jose del Carmen Pulgar`, `Juana de Dios Amagada de Pulgar`, `Juana Arriagada de Pulgar`, and `Jose del Carmen Segundo Pulgar Arriagada`. These pages do not prove a same-person or ancestor bridge from this conflicted 1889 entry.
- Do not merge people, rename canonical pages, promote facts, infer `Amagada` as `Arriagada`, or attach this register page to any Dario/Pulgar canonical identity until conversion QA and identity proof review resolve the literal readings.

## Hypothesis 1: Registration-Scoped Identities Only

Hypothesis: Entries 513-515 should remain staged, registration-scoped identities with no canonical same-person match yet.

Literal evidence:

- The assigned chunk reads entry 513 as child `Pulgar Amagada / Jose Luis`, father/declarant `Jose del Carmen Pulgar` / `Jose del C. Pulgar`, and mother `Juana de Dios Amagada de Pulgar`.
- The staged conflict draft says the image supports the Pulgar family row and `Jose ...`, but not the complete assigned-chunk child name with enough confidence for promotion.
- The assigned chunk reads entry 514 as child `Riquelme Aviles / Juan Bautista`, father `Se ignora`, and mother/declarant `Mercedes Riquelme`; the assembled converted Markdown conflicts by naming `Belisario Riquelme` and a derivative `Juan Soler` note.
- The assigned chunk reads entry 515 as child `Neira Ulloa / Laura de la Cruz`, father/declarant `Pedro Pablo Neira`, and mother `Carmen Ulloa`; the staged conflict draft says the bottom mother field remains cropped or not fully visible.

Interpretation:

- This is the leading hypothesis. The page supports local identity candidates and same-entry parent/declarant relationships, but the conversion conflict blocks canonical promotion and broader same-person matching.
- Entry 514's father field is negative evidence for the registration only. It should not be treated as a final disproof of later father evidence from a separate source.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.72 | Good for local register-row labels; insufficient for canonical same-person matches. |
| conflict_severity | 0.70 | Principal names and relationships differ across derivative layers. |
| evidence_quality | 0.72 | Civil birth register and image-reviewed staging notes are strong, but several readings need targeted QA. |
| conversion_confidence | 0.46 | Assigned chunk and assembled converted Markdown disagree on multiple identity fields. |
| claim_probability | 0.76 | Probable as entry-level people; exact normalized names remain held. |
| relevance | 0.94 | Directly addresses the assigned conflict draft. |
| canonical_readiness | 0.16 | Hold for conversion QA and proof review. |

## Hypothesis 2: Entry 513 Jose/Juana Pair Matches Existing Jose/Juana Amagada Stubs

Hypothesis: Entry 513's parents may correspond to the existing `Jose del Carmen Pulgar` and `Juana de Dios Amagada de Pulgar` canonical stubs.

Literal evidence:

- `wiki/people/jose-del-carmen-pulgar.md` has a draft child link to `Tulio Cesar Luis Jose`.
- `wiki/people/juana-de-dios-amagada-de-pulgar.md` has a draft child link to `Tulio Cesar Luis Jose`.
- The assigned chunk and staged conflict draft instead keep entry 513's child name unstable: assigned chunk `Jose Luis`, assembled conversion `Isolina del Carmen / Jose`, and image review only securely begins `Jose ...`.

Interpretation:

- The parent-name match is plausible, but the child identity and maternal surname are not stable enough to merge or update canonical pages.
- The existing stubs may represent the same register context or a related extraction cluster, but they cannot be used to silently correct the staged conflict draft.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.56 | Parent names align, but supporting child and surname evidence is conflicted. |
| conflict_severity | 0.72 | Premature merge could propagate the wrong child name or maternal surname. |
| evidence_quality | 0.58 | Stubs are draft-derived and this conflict draft is held. |
| conversion_confidence | 0.42 | The decisive entry 513 readings remain unresolved. |
| claim_probability | 0.52 | Possible correspondence, not proved. |
| relevance | 0.88 | Important for Pulgar-line identity control. |
| canonical_readiness | 0.10 | Hold; no canonical update. |

## Hypothesis 3: Entry 513 Is Near The Juana Arriagada / Jose del Carmen Segundo Pulgar Arriagada Cluster

Hypothesis: Entry 513's `Pulgar Ama...` and `Juana de Dios Amagada` readings may be related to, or confused with, the existing `Juana Arriagada de Pulgar` and `Jose del Carmen Segundo Pulgar Arriagada` cluster.

Literal evidence:

- `wiki/people/juana-arriagada-de-pulgar.md` links to `Jose del Carmen Segundo Pulgar Arriagada` as a probable child from a separate staged source.
- `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` records birth on 1888-03-08 at Calle de Valdivia, Los Angeles, from a different source packet.
- The current staged draft is an 1889 page 172 conflict, with entry 513 at Calle Colon and no confirmed `Arriagada` reading.

Interpretation:

- The overlap in `Pulgar`, `Jose`, `Juana`, and Los Angeles register context justifies a later double-check.
- The source/date/place and surname differences argue against merging. `Amagada` must remain a literal-reading issue, not a silent correction to `Arriagada`.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.24 | Shared name context only; source facts differ. |
| conflict_severity | 0.78 | Merging could collapse separate children or mothers. |
| evidence_quality | 0.52 | Both clusters have staged or held evidence. |
| conversion_confidence | 0.40 | The possible `Amagada`/`Arriagada` bridge is unresolved. |
| claim_probability | 0.22 | Plausible review lead, low same-person probability. |
| relevance | 0.80 | Required Pulgar-line comparison. |
| canonical_readiness | 0.04 | Do not merge or attach. |

## Hypothesis 4: Entry 513 Connects To Dario Arturo Pulgar-Smith Or Dario Arturo Pulgar

Hypothesis: The Pulgar entry may be an ancestor-line lead for canonical `Dario Arturo Pulgar-Smith` or staged `Dario Arturo Pulgar` CV material.

Literal evidence:

- `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied as Alexander John Heinz's maternal grandfather and explicitly warns not to automatically merge similarly named Pulgar records.
- Staged CV packets identify a document-level `Dario Arturo Pulgar`, but the assigned conflict draft contains no `Dario`, `Arturo`, `Smith`, CV, grandparent, descendant, or lineage statement.
- The staged conflict draft concerns a conflicted 1889 birth-register page with entry 513 parent candidates, not a Dario identity record.

Interpretation:

- This is a family-context lead only. `Pulgar` plus possible Jose/Juana parent names is not an identity bridge to Dario.
- Exact next proof step: after conversion QA, compare the confirmed entry 513 child/parents against evidence-grade lineage records that explicitly connect the verified register family to `Dario Arturo Pulgar`, and only then separately review whether `Dario Arturo Pulgar` is the same as `Dario Arturo Pulgar-Smith`.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.08 | No direct Dario or Smith evidence in the assigned draft. |
| conflict_severity | 0.70 | Premature attachment would create unsupported ancestor-line claims. |
| evidence_quality | 0.42 | This rests on surname/family context, not direct evidence. |
| conversion_confidence | 0.46 | Register conflict remains unresolved. |
| claim_probability | 0.10 | Very low from this source alone. |
| relevance | 0.68 | Relevant as a guarded Pulgar-line lead. |
| canonical_readiness | 0.01 | No canonical action supported. |

## Hypothesis 5: Same As Dario Jose Pulgar-Arriagada Or Dario/Darío Pulgar Arriagada

Hypothesis: Entry 513's Pulgar child or parents are the same identity cluster as `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, or canonical `Darío Pulgar Arriagada`.

Literal evidence:

- `wiki/people/dar-o-pulgar-arriagada.md` currently records a 2000 expropriation event, with no parent or birth bridge to this 1889 register page.
- Separate staged ICRC/Geneva and portrait materials use `Dario Jose Pulgar-Arriagada` or similar source-title identity labels, but those are separate adult/professional or image contexts.
- The assigned conflict draft contains no settled `Dario` given name and no confirmed `Arriagada` surname.

Interpretation:

- This is not supported as a same-person hypothesis. It is a name-cluster guardrail: keep the clusters separate until a proof-review bridge exists.
- Exact next proof step: after entry 513 literal child and mother names are QA-confirmed, run a Pulgar-Arriagada identity proof review comparing dates, parents, occupations, places, and source contexts across the Dario Jose / Dario Arriagada clusters.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.04 | No Dario or confirmed Arriagada evidence in this draft. |
| conflict_severity | 0.84 | Name-only merging could conflate separate generations or unrelated clusters. |
| evidence_quality | 0.38 | Compared Dario clusters are outside the assigned conflict and have their own QA holds. |
| conversion_confidence | 0.40 | The only possible surname bridge is unresolved. |
| claim_probability | 0.04 | Not probable from current evidence. |
| relevance | 0.64 | Required Pulgar-line comparison. |
| canonical_readiness | 0.00 | Do not merge, rename, or promote. |

## Conflicts

- Same-person conflict: unresolved. No person in the assigned draft can be safely merged with an existing canonical page.
- Duplicate-person risk: moderate for `Jose del Carmen Pulgar` and `Juana de Dios Amagada de Pulgar` because similar canonical stubs exist; high if unresolved child readings are used to force a match.
- Name-variant conflict: `Amagada` versus assembled-conversion `Amador`, plus family-context temptation to read `Arriagada`. Treat these as literal-reading conflicts, not normalized variants.
- Relationship conflict: entry 514 father should remain registration-scoped negative evidence only. The staged conflict draft and image review support `Se ignora`; the assembled converted Markdown's `Belisario Riquelme` should not be promoted.
- Chronology conflict: none proved within this assigned draft. Cross-cluster Dario comparisons are premature because the draft lacks Dario identity evidence.
- Conversion conflict: promotion-blocking. Entry 513 child/mother/date-time, entry 514 father/child/place/witnesses, and entry 515 child/father/mother fields require targeted QA before identity promotion.

## Ranked Hypotheses

| rank | hypothesis | probability | action |
|---:|---|---:|---|
| 1 | Registration-scoped identities only | 0.76 | Hold staged identities pending conversion QA. |
| 2 | Entry 513 Jose/Juana pair may match existing Jose/Juana Amagada stubs | 0.52 | Revisit only after child and mother readings are QA-confirmed. |
| 3 | Entry 513 may be near Juana Arriagada / Jose del Carmen Segundo Pulgar Arriagada cluster | 0.22 | Preserve as a review lead; do not correct `Amagada` to `Arriagada`. |
| 4 | Ancestor-line lead for Dario Arturo Pulgar-Smith / Dario Arturo Pulgar | 0.10 | Requires explicit lineage bridge after register QA. |
| 5 | Same as Dario Jose Pulgar-Arriagada / Dario or Darío Pulgar Arriagada | 0.04 | Keep separate; compare only after literal entry QA. |

## Recommended Next Action

Keep `research/_staging/conflicts/conflict-chunk-3d3ab761209f-p0001-01-conversion-conflicts.md` on hold. Do not promote facts, merge people, rename canonical pages, or attach this page to any Dario/Pulgar canonical identity.

The exact next step is targeted conversion QA/proof review for the source image and derivative transcripts: confirm entry 513 child full name, entry 513 mother surname, entry 513 birth date/time, entry 514 father field, entry 514 child/place/witness readings, and entry 515 mother field/crop completeness. After that, run a focused identity proof review comparing the confirmed entry 513 Jose/Juana/child readings against `Jose del Carmen Pulgar`, `Juana de Dios Amagada de Pulgar`, `Juana Arriagada de Pulgar`, and `Jose del Carmen Segundo Pulgar Arriagada` before any Pulgar-line promotion.
