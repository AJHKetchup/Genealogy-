---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260524192929996
task_id: identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260524182051046.md
staged_draft: research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260524182051046.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524182051046.md
source: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: page 1; register page 58; entry 172
analysis_status: hold_for_conversion_qa
canonical_readiness: hold
---

# Identity/Conflict Analysis: Entry 172 Pulgar-Arriagada Conversion Conflict

## Blockers

- The exact staged draft `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260524182051046.md` reports a material row-level conflict: source-packet/chunk evidence supports a Pulgar-Arriagada birth entry, while the assigned converted Markdown records a different family.
- The currently referenced converted file is also unstable against the staged draft's conflict wording. The draft says the converted Markdown records `Jose Francisco`, father `Oswaldo Gomez`, and mother `Emilia de la Cruz`; the current converted file records entry 172 as `Jose Miguel`, father `Oswaldo Bunster`, and mother `Amelia de la Maza`. Both are non-Pulgar readings, but this drift reinforces the need for targeted conversion QA.
- The father reading is not settled. Allowed literal outcomes remain `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
- No canonical merge or relationship promotion is ready. Child-parent claims for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar` must stay staged until conversion QA reconciles or supersedes the converted Markdown and proof review is rerun.
- The entry does not name Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario/Dario Pulgar Arriagada. Pulgar-line context can justify later comparison only; it does not justify a Dario attachment.

## Hypothesis 1: Entry 172 Is The Pulgar-Arriagada Birth Registration

Literal evidence:

- The source packet says entry 172 records child `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at about 3 p.m. at `Calle de Valdivia`.
- The assigned chunk gives the father/mother column as father `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`, with both parents resident at `Calle de Colipi`.
- The source packet says the source-image review supports the Pulgar-Arriagada row and the broad father reading `Jose del Carmen Pulgar`, but does not settle whether a final `S.` or other mark is present.

Interpretation:

- This is the leading row-control and identity hypothesis because the staged source packet and assigned chunk agree on the Pulgar-Arriagada cluster.
- It is not proof-ready for canonical promotion because the assigned converted Markdown remains materially incompatible and the father suffix is unresolved.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.84 | Strong agreement between source packet and chunk for child and mother; reduced by row-level conversion conflict and father-suffix uncertainty. |
| conflict_severity | 0.95 | The conflict changes child identity, parents, birth context, and downstream relationships. |
| evidence_quality | 0.80 | Civil birth-register evidence is specific, but the controlling transcript set is internally conflicted. |
| conversion_confidence | 0.46 | Mixed: chunk/source-packet support Pulgar-Arriagada while converted Markdown gives a non-Pulgar row. |
| claim_probability | 0.82 | Probable as the staged row reading, not yet promotion-ready. |
| relevance | 0.96 | Directly relevant to Pulgar-line child-parent evidence. |
| canonical_readiness | 0.12 | Hold for conversion QA and proof review. |

## Hypothesis 2: Entry 172 Is The Non-Pulgar Converted-Transcript Row

Literal evidence:

- The staged conflict draft reports a derivative row for `Jose Francisco`, father `Oswaldo Gomez`, and mother `Emilia de la Cruz`.
- The currently referenced converted Markdown instead reports entry 172 as `Jose Miguel`, father `Oswaldo Bunster`, and mother `Amelia de la Maza`.
- Neither derivative non-Pulgar reading agrees with the source packet or assigned chunk for the Pulgar-Arriagada row.

Interpretation:

- Preserve this only as the competing derivative-transcript hypothesis and as a row-control warning.
- Do not create or promote non-Pulgar identities from this entry unless targeted conversion QA proves the Pulgar-Arriagada assignment is wrong.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.12 | Supported only by conflicted derivative conversion text. |
| conflict_severity | 0.95 | Accepting this would replace every Pulgar-Arriagada identity and relationship from the staged draft. |
| evidence_quality | 0.25 | Derivative transcript evidence is internally drifting and conflicts with the staged packet/chunk. |
| conversion_confidence | 0.14 | Low for this as the controlling entry-172 row. |
| claim_probability | 0.16 | Possible only if the packet/chunk are attached to the wrong row. |
| relevance | 0.72 | Relevant as a false-positive and conversion-control issue. |
| canonical_readiness | 0.01 | Do not promote. |

## Hypothesis 3: Entry-172 Jose/Juana Parents Match Other Local Jose/Juana Candidates

Literal evidence:

- Under the Pulgar-Arriagada reading, entry 172 names father `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- Existing `wiki/people/jose-del-carmen-pulgar.md` has a drafted child link to `Tulio Cesar Luis Jose` from a separate relationship source, not from this entry.
- Existing `wiki/people/juana-arriagada-de-pulgar.md` carries this b8f4 entry-172 mother evidence for `Jose del Carmen Segundo Pulgar Arriagada`.
- Existing `wiki/people/juana-de-dios-amagada-de-pulgar.md` is a separate candidate cluster tied to `Tulio Cesar Luis Jose`; the literal name is not the same as `Juana Arriagada de Pulgar`.

Interpretation:

- `Jose del Carmen Pulgar` may be a useful cross-entry parent candidate after row control and father-suffix QA.
- `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` must remain separate hypotheses unless a later proof-reviewed source establishes a variant reading or same-person bridge.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.43 | Plausible local family cluster, but cross-entry identity is not established. |
| conflict_severity | 0.62 | Premature merging could combine distinct couples or mother-name readings. |
| evidence_quality | 0.50 | Local staged/wiki evidence exists but depends on unresolved conversion QA. |
| conversion_confidence | 0.34 | Entry 172 remains conversion-blocked; related entries have separate review histories. |
| claim_probability | 0.40 | Possible, not proven. |
| relevance | 0.88 | Important for Pulgar-line structure after row control is settled. |
| canonical_readiness | 0.08 | Hold pending conversion QA and parent-candidate proof review. |

## Dario-Line Comparison

| candidate | allowed local evidence | rank/probability | required next step |
| --- | --- | ---: | --- |
| `Dario Arturo Pulgar-Smith` | Canonical family-supplied page identifies him as Alexander John Heinz's maternal grandfather and warns against attaching similar Pulgar records without identity review. Entry 172 does not name him. | 0.03 | Require a proof-reviewed bridge from the Entry 172 Jose/Juana/child cluster to the canonical Pulgar-Smith line before any attachment. |
| `Dario Arturo Pulgar` | Local CV staging uses this as document-level CV identity, not as an Entry 172 person. Entry 172 has no Dario Arturo, CV, occupation chronology, spouse, child, or grandchild evidence. | 0.02 | Require an identity-bearing local source connecting document-level `Dario Arturo Pulgar` to the Entry 172 family cluster. |
| `Dario Jose Pulgar-Arriagada` | Local staged context includes this name in other materials, but Entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Jose. | 0.02 | Require a proof-reviewed bridge naming both identity contexts; do not merge by shared Pulgar-Arriagada surname. |
| `Dario/Dario Pulgar Arriagada` | Canonical `wiki/people/dar-o-pulgar-arriagada.md` has a 2000 event for `Dario Pulgar Arriagada`. Entry 172 is an 1888 birth registration for a different given-name cluster. | 0.01 | Keep separate unless later proof review connects the 1888 child/parents to the 2000 legal-notice person. |
| Jose/Juana parent candidates | Directly relevant only for `Jose del Carmen Pulgar` / `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`; `Juana de Dios Amagada de Pulgar` remains a separate candidate from another entry. | 0.40 for cross-entry parent-candidate match; 0.82 for narrow Entry 172 parent readings after QA | First settle row control and father suffix, then run Jose/Juana parent-candidate proof review. |

## Conflicts

- Same-person/duplicate-person conflict: unresolved for Jose/Juana parent candidates across entries; no same-person evidence connects this entry to any Dario identity.
- Name-variant conflict: `Jose del Carmen Pulgar` versus `Jose del Carmen Pulgar S.` / uncertain suffix; `Juana Arriagada de Pulgar` versus `Juana de Dios Amagada de Pulgar` is not a proven variant.
- Relationship conflict: child-parent relationships from Entry 172 cannot be promoted while the row-level conversion conflict remains open.
- Chronology conflict: the competing row readings give different birth contexts; no Dario chronology claim is supported by this entry.
- Conversion conflict: critical row-level conflict among staged draft wording, assigned converted Markdown, current chunk, and source-packet evidence.

## Recommended Next Action

Keep the exact staged conflict and all dependent identity, claim, relationship, and parent-candidate drafts at `hold_for_conversion_qa`.

Exact next proof-review/promotion step: perform targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the referenced source image, reconcile or supersede the assigned converted Markdown, confirm the correct entry 172 row, and explicitly record whether the father field reads `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, rerun proof review for child identity, birth facts, father, mother, and child-parent relationships before any canonical promotion.

Do not merge or attach this entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada` unless a later proof-reviewed local source supplies an explicit identity bridge.
