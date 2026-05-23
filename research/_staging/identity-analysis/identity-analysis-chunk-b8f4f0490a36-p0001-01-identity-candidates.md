---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/identity/chunk-b8f4f0490a36-p0001-01-identity-candidates.md
staged_draft: research/_staging/identity/chunk-b8f4f0490a36-p0001-01-identity-candidates.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-jose-del-carmen-segundo-pulgar-arriagada.md
source_path: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
chunk_id: CHUNK-b8f4f0490a36-P0001-01
analysis_status: hold_for_conversion_qa
canonical_readiness: hold
worker: postconv-evidence-extraction-20260523181508215
---

# Identity Analysis: Entry 172 Identity Candidates

## Blockers

- The exact staged draft `research/_staging/identity/chunk-b8f4f0490a36-p0001-01-identity-candidates.md` depends on a conflicted transcription set. The source image and assigned chunk/source packet support entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar` / `Jose del Carmen Pulgar S.`, and mother `Juana Arriagada de Pulgar`; the converted Markdown reads entry 172 as `Jose Francisco`, father `Oswaldo Gomez`, and mother `Emilia de la Cruz`.
- The source image is now available and was directly reread for this revision. It supports the Pulgar/Arriagada row, so the remaining blocker is the conflicting assigned converted Markdown plus unresolved father-name suffix.
- The father-name reading is not stable enough for identity merging: the assigned chunk has `Jose del Carmen Pulgar S.`, while the direct image reread supports `Jose del Carmen Pulgar` without a clearly visible final `S.` suffix.
- Existing canonical pages already contain auto-generated evidence from this b8f4 entry for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar`. Because the controlling conversion remains conflicted, no additional promotion, canonical normalization, or relationship merge should occur from this staged identity draft.
- The staged draft does not name any Dario. Dario-line context is relevant only as a guardrail against name-based merging into `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario Pulgar Arriagada`.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Registration

Literal evidence:

- The assigned chunk transcribes entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at 3 p.m. at `Calle de Valdivia`.
- The assigned chunk names the father as `Jose del Carmen Pulgar S.`, Chilean, employed, resident at `Calle de Colipí`.
- The assigned chunk names the mother as `Juana Arriagada de Pulgar`, Chilean, occupation `Su sexo`, resident at `Calle de Colipí`.
- The source packet repeats this reading and now records a direct source-image reread supporting `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar`.
- Existing canonical `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` and `wiki/people/juana-arriagada-de-pulgar.md` contain auto-generated evidence from this source packet, with the mother-child link labeled probable at very low confidence.

Interpretation:

- This is the leading identity hypothesis for the staged draft because the staged identity draft, assigned chunk, and source packet all point to the Pulgar/Arriagada row.
- It is not canonical-ready because the converted Markdown gives a different family and the current worker cannot verify the image directly.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.86 | Strong agreement among source image, staged draft, chunk, and source packet, reduced by converted-file conflict and father-suffix uncertainty. |
| conflict_severity | 0.94 | The competing reading changes the child, both parents, birth date/place, informant, and official. |
| evidence_quality | 0.84 | Civil registration image is available and supports the row, but derivative transcript conflict remains. |
| conversion_confidence | 0.50 | The source image and assigned chunk support the Pulgar row, but the converted file contradicts it. |
| claim_probability | 0.86 | More probable than the Gomez/de la Cruz reading on current source-image evidence, but still blocked. |
| relevance | 0.96 | Directly relevant to Pulgar/Arriagada parent-child identity and relationship evidence. |
| canonical_readiness | 0.15 | Hold pending targeted conversion QA and source-image reconciliation. |

## Hypothesis 2: Entry 172 Is The Gomez/de la Cruz Birth Registration

Literal evidence:

- The converted Markdown reads entry 172 as `Jose Francisco`, male, born 26 March 1888 at 10 p.m.
- The converted Markdown names father/informant `Oswaldo Gomez` and mother `Emilia de la Cruz`.
- The converted Markdown names `Camilo Henriquez` in the official/identity-control area, not `Emilio Riquelme V.`

Interpretation:

- This is a competing derivative-reading hypothesis only because it appears in the assigned converted file.
- It should not be used to create or promote Gomez/de la Cruz identity facts unless conversion QA proves that the chunk/source-packet assignment is wrong or that the converted file is the controlling transcript.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.10 | Supported by one conflicted converted transcript and contradicted by the visible source image. |
| conflict_severity | 0.94 | Accepting it would displace the complete Pulgar/Arriagada identity cluster for this entry. |
| evidence_quality | 0.28 | Derivative-only support in conflict with the staged draft, chunk, and source packet. |
| conversion_confidence | 0.12 | Low because local staging and the direct source-image reread flag the converted file as mismatched. |
| claim_probability | 0.14 | Plausible only if the Pulgar/Arriagada chunk/source packet is attached to the wrong converted source. |
| relevance | 0.70 | Relevant as a false-positive guardrail. |
| canonical_readiness | 0.01 | Do not promote. |

## Hypothesis 3: Jose/Juana Parent Candidates Are The Same Couple Across Pulgar Entries

Literal evidence:

- This b8f4 entry, if the Pulgar reading is accepted, names father `Jose del Carmen Pulgar S.` or `Jose del Carmen Pulgar` and mother `Juana Arriagada de Pulgar`.
- Existing `wiki/people/jose-del-carmen-pulgar.md` has a drafted child link to `Tulio Cesar Luis Jose` from a different staged relationship, not from this b8f4 entry.
- Existing `wiki/people/juana-de-dios-amagada-de-pulgar.md` has a drafted child link to `Tulio Cesar Luis Jose`; this is not the same literal name as `Juana Arriagada de Pulgar`.
- Existing `wiki/people/juana-arriagada-de-pulgar.md` carries this b8f4 entry-172 mother evidence, not independent proof that she is the same person as `Juana de Dios Amagada de Pulgar`.

Interpretation:

- The repeated `Jose del Carmen Pulgar` father-name form supports a parent-candidate review, but the b8f4 father suffix issue and separate Juana surname/name readings prevent a same-person merge.
- `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` must remain separate hypotheses unless proof review establishes that the apparent surname and given-name differences are variant readings of one person.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.46 | Plausible same-family cluster, not proven across entries. |
| conflict_severity | 0.58 | Premature merge could combine separate Jose/Juana couples or preserve a misread mother surname. |
| evidence_quality | 0.52 | Local staged/canonical evidence exists, but cross-entry identity proof is incomplete. |
| conversion_confidence | 0.35 | The b8f4 entry remains conversion-blocked; related Pulgar/Amagada entries have separate QA concerns. |
| claim_probability | 0.42 | Possible, but unresolved. |
| relevance | 0.86 | Important to Pulgar-line structure and later Dario-line review. |
| canonical_readiness | 0.08 | Hold pending targeted Jose/Juana identity proof review. |

## Hypothesis 4: Ernesto Herrera L. And Emilio Riquelme V. Are Event Participants Only

Literal evidence:

- The assigned chunk names `Ernesto Herrera L.` as compareciente/informant, present at the birth, age 26, employed, resident at `Calle de Valdivia`.
- The assigned chunk signs the official field as `[signature] Emilio Riquelme V.`
- The converted Markdown instead gives `Oswaldo Gomez` as informant and `Camilo Henriquez` in the official/identity-control area.

Interpretation:

- Under the Pulgar/Arriagada hypothesis, Ernesto Herrera L. is an event informant/witness-type participant, not a stated relative.
- Emilio Riquelme V. is a civil official/signatory, not family evidence.
- Neither person should be linked into the Pulgar family without a separate source stating kinship.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.58 | Supported by the assigned chunk, but affected by the converted-file conflict. |
| conflict_severity | 0.62 | Names differ from the converted Markdown but do not directly affect parent-child identity unless the whole entry reading changes. |
| evidence_quality | 0.50 | Derivative event-participant evidence only. |
| conversion_confidence | 0.34 | Blocked by the same entry-level conversion mismatch. |
| claim_probability | 0.55 | Plausible within Hypothesis 1, uncertain overall. |
| relevance | 0.40 | Useful for entry integrity, low for family identity. |
| canonical_readiness | 0.05 | Do not create or promote family relationships. |

## Dario-Line Comparison

- `Dario Arturo Pulgar-Smith`: Existing canonical context identifies him from family-supplied knowledge as Alexander John Heinz's maternal grandfather and warns not to merge similarly named Pulgar records without identity review. This entry does not name him.
- `Dario Arturo Pulgar`: CV staged material uses this document-level name form. This entry does not name Dario Arturo and provides no CV-era bridge.
- `Dario Jose Pulgar-Arriagada`: Staged ICRC/Geneva photograph material uses this name from source title or metadata. This entry names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Jose Pulgar-Arriagada.
- `Dario Pulgar Arriagada` / `Darío Pulgar Arriagada`: Existing canonical `wiki/people/dar-o-pulgar-arriagada.md` contains a 2000 expropriation event. This entry is an 1888 birth-registration conflict for a different given-name cluster.
- Ranked impact: (1) direct impact on `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar`; (2) indirect guardrail for Jose/Juana parent-candidate review; (3) no present evidence to attach this entry to any Dario identity.

## Conflicts

- Same-entry conflict: Pulgar/Arriagada source image, assigned chunk, and source packet versus Gomez/de la Cruz converted Markdown. Severity: critical.
- Duplicate-person risk: high if Gomez/de la Cruz people are promoted from the converted mismatch; moderate if Jose/Juana parent candidates are merged across Pulgar entries without proof review.
- Name-variant conflict: `Jose del Carmen Pulgar S.` versus `Jose del Carmen Pulgar`. Severity: moderate because it affects father matching.
- Relationship conflict: parent-child links from this entry are not promotion-ready until conversion QA establishes the controlling row. Severity: high.
- Chronology conflict: the competing readings give different birth dates and places for entry 172. Severity: high for this entry, low for Dario-line chronology because no Dario is named.

## Recommended Next Action

Keep the staged identity draft and all affected identity/relationship claims at `hold_for_conversion_qa`.

Exact next proof-review step: perform targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the restored source image or authoritative page image, then reconcile the converted Markdown/chunk assignment so entry 172 has one controlling transcript. The QA must explicitly decide whether the father field reads `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or an uncertain form.

After conversion QA, run proof review on the child birth-name, birth event, father, mother, and parent-child relationships. Separately run a Jose/Juana parent-candidate identity review before merging `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, or `Juana de Dios Amagada de Pulgar`. Do not attach this entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario Pulgar Arriagada` without a later source that explicitly bridges identity.
