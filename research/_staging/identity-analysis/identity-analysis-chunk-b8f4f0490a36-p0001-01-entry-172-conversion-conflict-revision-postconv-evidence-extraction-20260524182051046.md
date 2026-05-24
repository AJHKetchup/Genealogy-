---
type: identity_conflict_analysis
status: draft
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260524182051046.md"
worker: postconv-identity-analysis-20260524193756615
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260524182051046.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524182051046.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
analysis_status: hold_for_conversion_qa
canonical_readiness: hold
tags: [identity-analysis, conflict-review, pulgar, conversion-qa]
---

# Identity/Conflict Analysis: Entry 172 Conversion Conflict Revision

## Blockers

- The exact staged draft is `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260524182051046.md`.
- This draft is blocked by a material row-level transcript conflict. The staged draft and source packet say the assigned chunk/source-image review supports entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar S.`, and mother `Juana Arriagada de Pulgar`.
- The current assigned converted Markdown does not match the Pulgar/Arriagada row. It reads entry 172 as `José Miguel`, father `Oswaldo Bunster`, and mother `Amelia de la Maza`.
- The staged conflict draft itself describes the converted Markdown conflict as `Jose Francisco`, father `Oswaldo Gomez`, and mother `Emilia de la Cruz`. That does not match the current converted file text read for this analysis, so there is an additional derivative-summary inconsistency. Both derivative forms are non-Pulgar rows and neither can be promoted.
- The father-name ending remains unresolved. Preserve the literal alternatives `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` until targeted conversion QA settles the field.
- Existing canonical pages already contain held or low-confidence auto-generated Pulgar evidence for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar`. This analysis does not edit those pages and does not recommend merge or promotion while the conversion is conflicted.
- The entry does not name Dario. Dario-line context is relevant only as an anti-conflation guardrail.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Registration

Literal evidence:

- The assigned chunk transcribes entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at about 3 p.m. at `Calle de Valdivia`.
- The assigned chunk names the father as `Jose del Carmen Pulgar S.`, Chilean, employed, resident at `Calle de Colipí`.
- The assigned chunk names the mother as `Juana Arriagada de Pulgar`, Chilean, occupation `Su sexo`, resident at `Calle de Colipí`.
- The source packet for this exact revision says source-image review supports the controlling row as the Pulgar/Arriagada row and supports broad father reading `Jose del Carmen Pulgar`, while not settling whether a final `S.` or other mark is present.
- Existing canonical `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` carries this entry as birth-name, birth-date/time, birth-place, and sex evidence. Existing `wiki/people/juana-arriagada-de-pulgar.md` carries this entry as probable mother evidence with low confidence.

Interpretation:

- This is the leading identity hypothesis for the row because the assigned chunk and source packet align on the Pulgar/Arriagada child-parent cluster.
- It remains not canonical-ready because the assigned converted Markdown and staged derivative-summary wording conflict with the row, and because the father suffix has not been resolved.

Scores:

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.86 | Strong local chunk/source-packet support for the Pulgar/Arriagada identity cluster, reduced by derivative conversion conflict and father-suffix uncertainty. |
| conflict_severity | 0.95 | Competing readings change the child, both parents, birth date/place details, and event participants. |
| evidence_quality | 0.82 | Civil-registration image and chunk are strong, but the controlling converted file is contradicted. |
| conversion_confidence | 0.48 | The chunk/source-packet reading is usable as staged evidence, but the assigned converted Markdown is materially unreliable for this row. |
| claim_probability | 0.86 | More probable than the non-Pulgar derivative readings on current staged/source-packet evidence. |
| relevance | 0.96 | Directly relevant to the Pulgar/Arriagada child-parent cluster. |
| canonical_readiness | 0.12 | Hold for targeted conversion QA and proof review. |

## Hypothesis 2: Entry 172 Is A Non-Pulgar Converted-File Row

Literal evidence:

- The current assigned converted Markdown reads entry 172 as `José Miguel`, father `Oswaldo Bunster`, mother `Amelia de la Maza`, born 26 March 1888 at 10 p.m. in `En esta Subdelegacion`.
- The staged conflict draft describes a different non-Pulgar derivative row: `Jose Francisco`, father `Oswaldo Gomez`, and mother `Emilia de la Cruz`.

Interpretation:

- This hypothesis must be preserved as a conversion/file-assignment conflict, not as a reliable identity conclusion.
- The internal mismatch between the staged summary and current converted Markdown further weakens derivative confidence. Do not create or promote Bunster, Gomez, de la Maza, or de la Cruz people from this entry without conversion QA proving the Pulgar/Arriagada row is not the controlling row.

Scores:

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.08 | Supported only by conflicted derivative text and contradicted by the assigned chunk/source packet. |
| conflict_severity | 0.95 | Accepting this would displace all Pulgar/Arriagada identity and relationship claims for entry 172. |
| evidence_quality | 0.18 | Derivative-only and internally inconsistent between staged summary and current converted file. |
| conversion_confidence | 0.10 | The converted-file row is the artifact under dispute. |
| claim_probability | 0.08 | Plausible only if the source/chunk assignment is wrong or the derivative row belongs to a different image/page. |
| relevance | 0.68 | Relevant as a false-positive guardrail. |
| canonical_readiness | 0.01 | Do not promote. |

## Hypothesis 3: Entry-172 Jose/Juana Parents Match Other Pulgar Parent Candidates

Literal evidence:

- Under the Pulgar hypothesis, entry 172 names father `Jose del Carmen Pulgar` / `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- Existing `wiki/people/jose-del-carmen-pulgar.md` has a drafted child link to `Tulio Cesar Luis Jose` from a different staged relationship, not this entry.
- Existing `wiki/people/juana-de-dios-amagada-de-pulgar.md` has a drafted child link to `Tulio Cesar Luis Jose`; its literal name is not the same as `Juana Arriagada de Pulgar`.
- Existing `wiki/people/juana-arriagada-de-pulgar.md` carries this entry-172 mother evidence but does not independently prove identity with `Juana de Dios Amagada de Pulgar`.

Interpretation:

- The `Jose del Carmen Pulgar` name overlap is a parent-candidate lead, not a merge.
- `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` must remain separate hypotheses until a proof review demonstrates that the differences are source-visible variants rather than distinct people or conversion errors.

Scores:

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.44 | Plausible family cluster, but cross-entry identity is not proven and this entry is conversion-blocked. |
| conflict_severity | 0.62 | Premature parent merging could combine separate couples or preserve a misread mother name. |
| evidence_quality | 0.50 | Local canonical/staged evidence exists, but bridge evidence is incomplete. |
| conversion_confidence | 0.34 | Entry 172 is blocked; other Jose/Juana entries have their own held proof status. |
| claim_probability | 0.40 | Possible, not established. |
| relevance | 0.86 | Important for Pulgar-line structure. |
| canonical_readiness | 0.06 | Hold pending targeted Jose/Juana parent-candidate proof review. |

## Dario-Line Comparison

- `Dario Arturo Pulgar-Smith`: Existing canonical page is family-supplied as Alexander John Heinz's maternal grandfather and warns not to attach similarly named Pulgar records without identity review. Entry 172 does not name Dario, Arturo, Smith, Pulgar-Smith, Alexander John Heinz, or any relationship to him.
- `Dario Arturo Pulgar`: Existing staged CV analyses treat this as a document-level CV subject, with a separate unresolved bridge to `Dario Arturo Pulgar-Smith`. Entry 172 gives no CV-era identity bridge and does not name Dario Arturo.
- `Dario Jose Pulgar-Arriagada`: Local staged Dario Jose/Pulgar-Arriagada contexts are title, metadata, or proof-review-held clusters. Entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, not `Dario Jose Pulgar-Arriagada`.
- `Dario/Darío Pulgar Arriagada`: Existing canonical `wiki/people/dar-o-pulgar-arriagada.md` has a 2000 Serviu Región del Bío Bío expropriation event for `Darío Pulgar Arriagada`. Entry 172 is an 1888 birth-registration conflict for a different given-name cluster.
- Dario passenger or `Dario Pulgar A.` candidates: Existing local contexts distinguish adult and child passenger stubs and held older medical/property hypotheses. Entry 172 provides no `Dario`, `A.`, `Arturo`, `Jose`, physician, passenger, or property bridge.

Ranked Dario impact:

| rank | hypothesis | probability | action |
| ---: | --- | ---: | --- |
| 1 | No Dario identity is supported by this entry. | 0.99 | Preserve as anti-conflation guardrail. |
| 2 | Indirect future relevance through Jose/Juana parent-candidate line work. | 0.18 | Only after entry 172 conversion QA and separate parent-candidate proof review. |
| 3 | Same-person or direct relationship bridge to any Dario candidate. | 0.01 | Do not attach or merge from this source. |

## Conflicts

- Same-entry conflict: assigned chunk/source packet support Pulgar/Arriagada; assigned converted Markdown supports a non-Pulgar row. Severity: critical.
- Derivative-summary conflict: the staged conflict draft's description of the converted row differs from the current converted Markdown text. Severity: high for conversion QA, moderate for identity because both derivative readings are non-Pulgar.
- Name-variant conflict: `Jose del Carmen Pulgar S.` versus `Jose del Carmen Pulgar` versus `Jose del Carmen Pulgar [?]`. Severity: moderate because it affects father identity matching.
- Relationship conflict: child-father and child-mother relationships are probable only under the Pulgar row and must not be promoted until conversion QA identifies the controlling transcript. Severity: high.
- Duplicate-person risk: high if non-Pulgar converted-row names are promoted from this conflicted entry; moderate if Jose/Juana parent candidates are merged across records without proof review.
- Chronology conflict: the competing rows give different birth dates and places for entry 172. There is no Dario-line chronology claim from this source.

## Ranked Hypotheses

| rank | hypothesis | probability | canonical action |
| ---: | --- | ---: | --- |
| 1 | Entry 172 is the Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada`, child of `Jose del Carmen Pulgar` / possible `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`. | 0.86 | Hold for conversion QA, then proof-review child identity, birth facts, and parent links. |
| 2 | Entry-172 Jose/Juana parents are same as other Pulgar-line Jose/Juana candidates. | 0.40 | Preserve as possible; require separate cross-entry parent-candidate identity review. |
| 3 | Entry 172 is the non-Pulgar converted-file row. | 0.08 | Treat as conversion/file-assignment conflict unless QA proves otherwise. |
| 4 | Entry 172 supports any Dario same-person or relationship claim. | 0.01 | No promotion or merge. |

## Recommended Next Action

Keep the exact staged conflict draft and all dependent identity, claim, relationship, and parent-candidate work at `hold_for_conversion_qa`.

Exact next proof-review or promotion step: run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image and the current converted Markdown. The QA note must reconcile the Pulgar/Arriagada chunk/source-packet row against the non-Pulgar converted row and also explain why the staged conflict summary's `Jose Francisco` / `Oswaldo Gomez` / `Emilia de la Cruz` wording differs from the current converted-file `José Miguel` / `Oswaldo Bunster` / `Amelia de la Maza` text.

The same QA must explicitly record the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. After QA, rerun proof review on the child birth name, sex, registration date, birth date/time/place, father, mother, informant, and child-parent relationships. Separately run Jose/Juana parent-candidate proof review before merging `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, `Juana de Dios Amagada de Pulgar`, or any other Jose/Juana Pulgar-line candidate. Do not attach this entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, `Dario Pulgar A.`, or Dario passenger candidates without a later identity-bridging source.
