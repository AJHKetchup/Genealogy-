---
type: identity_conflict_analysis
status: draft
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260524182051046.md"
worker: postconv-identity-analysis-20260524194628683
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

# Identity/Conflict Analysis: Entry 172 Conversion Conflict

## Blockers

- The exact staged draft analyzed here is `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260524182051046.md`.
- The conflict is material and row-level. The staged draft/source packet support entry 172 as a Pulgar/Arriagada birth registration, while the assigned converted Markdown currently carries a non-Pulgar row.
- The assigned chunk reads entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, and mother `Juana Arriagada de Pulgar`.
- The source packet says source-image review supports the Pulgar/Arriagada row and supports broad father reading `Jose del Carmen Pulgar`, but does not settle whether a final `S.` or other mark follows `Pulgar`.
- The current assigned converted Markdown inspected for this analysis reads entry 172 as `José Miguel`, father `Oswaldo Bunster`, and mother `Amelia de la Maza`. The staged conflict draft describes the converted conflict as `Jose Francisco`, father `Oswaldo Gomez`, and mother `Emilia de la Cruz`, so conversion QA must also explain that derivative-state mismatch.
- Existing canonical pages already contain held or low-confidence Pulgar evidence for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar`. No canonical page should be edited or promoted from this conflict draft.
- The entry does not name Dario. Dario-line candidates are relevant only as anti-conflation checks unless later proof-reviewed bridge evidence is found elsewhere.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Registration

Literal evidence:

- The assigned chunk transcribes entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at about 3 p.m. at `Calle de Valdivia`.
- The assigned chunk names father `Jose del Carmen Pulgar S.`, Chilean, `Empleado`, resident at `Calle de Colipí`.
- The assigned chunk names mother `Juana Arriagada de Pulgar`, Chilean, occupation `Su sexo`, resident at `Calle de Colipí`.
- The source packet for this exact revision reports that source-image review supports the Pulgar/Arriagada row as the controlling row, while preserving father-field uncertainty.
- Existing `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` carries this entry as birth-name, birth-date/time, birth-place, and sex evidence. Existing `wiki/people/juana-arriagada-de-pulgar.md` carries this entry as probable mother evidence with very low promoted confidence.

Interpretation:

- This is the leading identity hypothesis for the assigned entry because the chunk and source packet align on the same child-parent cluster.
- It remains not canonical-ready because the converted Markdown and staged conflict wording conflict with the row, and because the father suffix is unresolved.

Scores:

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.87 | Strong local chunk/source-packet support, reduced by derivative conflict and father-suffix uncertainty. |
| conflict_severity | 0.96 | Competing readings change the child, parents, birth date/place, and event participants. |
| evidence_quality | 0.83 | Civil registration context and staged image-reviewed packet are strong, but the controlling converted file is contradicted. |
| conversion_confidence | 0.44 | The chunk/source-packet reading is usable as staged evidence; the assigned converted Markdown is materially unreliable for this row. |
| claim_probability | 0.87 | Most probable current interpretation of the staged/source-packet evidence. |
| relevance | 0.98 | Directly relevant to the Pulgar/Arriagada child-parent cluster. |
| canonical_readiness | 0.13 | Hold for targeted conversion QA and renewed proof review. |

## Hypothesis 2: Entry 172 Is The Non-Pulgar Converted-File Row

Literal evidence:

- The current converted Markdown records entry 172 as `José Miguel`, father `Oswaldo Bunster`, mother `Amelia de la Maza`, born 26 March 1888 at 10 p.m. in `En esta Subdelegacion`.
- The staged conflict draft instead summarizes the converted conflict as `Jose Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`.
- Neither non-Pulgar derivative reading matches the assigned chunk/source-packet Pulgar row.

Interpretation:

- This is a conversion-control hypothesis, not a reliable person-identity conclusion.
- Do not create or promote Bunster, Gomez, de la Maza, de la Cruz, or other non-Pulgar person/relationship claims from this assigned entry unless targeted conversion QA proves the Pulgar/Arriagada row is not the controlling row.

Scores:

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.06 | Supported only by conflicted derivative text. |
| conflict_severity | 0.96 | Accepting it would displace all Pulgar/Arriagada evidence for the assigned draft. |
| evidence_quality | 0.17 | Derivative-only and internally inconsistent between staged summary and current file state. |
| conversion_confidence | 0.09 | The converted file is the disputed artifact. |
| claim_probability | 0.05 | Plausible only as stale conversion, row drift, or file-assignment error. |
| relevance | 0.76 | Relevant as a false-positive guardrail. |
| canonical_readiness | 0.01 | Do not promote. |

## Hypothesis 3: Entry-172 Jose/Juana Parents Match Other Pulgar Parent Candidates

Literal evidence:

- Under the Pulgar hypothesis, entry 172 names father `Jose del Carmen Pulgar` or possible `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- Existing `wiki/people/jose-del-carmen-pulgar.md` has a separate drafted child link to `Tulio Cesar Luis Jose`.
- Existing `wiki/people/juana-arriagada-de-pulgar.md` carries entry-172 evidence for `Jose del Carmen Segundo Pulgar Arriagada`.
- Existing `wiki/people/juana-de-dios-amagada-de-pulgar.md` represents a separate Juana candidate from another Pulgar child-parent cluster; that literal name is not identical to `Juana Arriagada de Pulgar`.

Interpretation:

- The shared Jose/Pulgar and Juana/Pulgar family context justifies a targeted cross-entry parent-candidate review after conversion QA.
- It does not justify a merge. `Juana Arriagada de Pulgar`, `Juana de Dios Amagada de Pulgar`, `Jose del Carmen Pulgar`, and `Jose del Carmen Pulgar S.` must remain separate or unresolved candidates until proof review shows the differences are source-visible variants or conversion errors.

Scores:

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.43 | Plausible family cluster, but no cross-entry bridge is proved by this draft. |
| conflict_severity | 0.64 | Premature parent merging could combine distinct people or preserve a conversion error. |
| evidence_quality | 0.53 | Useful local staged/canonical evidence exists, but bridge evidence is incomplete. |
| conversion_confidence | 0.36 | Entry 172 is blocked and related Jose/Juana readings are image-sensitive. |
| claim_probability | 0.41 | Possible, not established. |
| relevance | 0.89 | Important for Pulgar-line parent structure. |
| canonical_readiness | 0.06 | Hold for parent-candidate proof review after conversion QA. |

## Dario-Line Comparison

| candidate | comparison result | probability/action |
| --- | --- | --- |
| `Dario Arturo Pulgar-Smith` | Canonical page is family-supplied as Alexander John Heinz's maternal grandfather and warns against automatic merge with similarly named Pulgar records. Entry 172 does not name Dario, Arturo, Smith, Pulgar-Smith, Alexander John Heinz, or a grandchild relationship. | Direct relevance 0.01; do not attach. |
| `Dario Arturo Pulgar` | Local staged CV work treats this as a document-level CV subject with a separate unresolved bridge to `Dario Arturo Pulgar-Smith`. Entry 172 provides no CV-era identity bridge and does not name Dario Arturo. | Direct relevance 0.01; do not attach. |
| `Dario Jose Pulgar-Arriagada` | Existing staged contexts preserve this as a Dario Jose/Pulgar-Arriagada cluster. Entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Jose. | Same-person probability 0.02; no merge. |
| `Dario/Darío Pulgar Arriagada` | Existing canonical `Darío Pulgar Arriagada` has a 2000 Serviu Región del Bío Bío expropriation event. Entry 172 is an 1888 birth-registration conflict for a different given-name cluster. | Same-person probability 0.01; no merge. |
| Jose/Juana parent candidates | Entry 172 directly names Jose/Juana candidates and may later matter for Pulgar-line structure. | Same-family relevance 0.41; proved same-person merge now 0.12; require separate proof review. |

## Conflicts

- Same-entry conversion conflict: assigned chunk/source packet support Pulgar/Arriagada; assigned converted Markdown supports a non-Pulgar row. Severity: critical.
- Derivative-state conflict: staged conflict summary gives one non-Pulgar row, while the current converted file gives another. Severity: high for auditability.
- Father-name conflict: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` remain unresolved. Severity: moderate-high for father matching.
- Relationship conflict: child-father and child-mother claims are probable only if the Pulgar row is confirmed. Severity: high for canonical readiness.
- Duplicate-person risk: high for non-Pulgar false-positive promotion; moderate for Jose/Juana parent merging by name alone.
- Chronology conflict: the competing rows give different birth dates and places for entry 172. No direct Dario chronology claim is supported.

## Ranked Hypotheses

| rank | hypothesis | probability | canonical action |
| ---: | --- | ---: | --- |
| 1 | Entry 172 is the Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.87 | Hold for conversion QA, then proof-review atomic claims and relationships. |
| 2 | Entry-172 Jose/Juana parents may match other Pulgar-line parent candidates. | 0.41 | Preserve as possible; require cross-entry parent-candidate proof review. |
| 3 | Entry 172 is represented by the non-Pulgar converted Markdown row. | 0.05 | Treat as conversion/file-state conflict unless QA proves otherwise. |
| 4 | Entry 172 directly bridges to any Dario identity. | 0.01 | Reject for this draft; no Dario attachment or merge. |

## Recommended Next Action

Keep the exact staged conflict draft and all dependent identity, claim, relationship, and parent-candidate drafts at `hold_for_conversion_qa`.

Exact next proof-review or promotion step needed: run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image and the current converted Markdown. The QA note must identify the controlling row for register page 58 entry 172, reconcile the staged draft's non-Pulgar derivative wording with the current converted-file row, and explicitly record the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After conversion QA, rerun proof review on child birth name, sex, registration date, birth date/time/place, father, mother, informant, parent attributes, and child-parent relationships. Separately run Jose/Juana parent-candidate identity review before merging `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, `Juana Arriagada de Pulgar`, `Juana de Dios Amagada de Pulgar`, or any other Jose/Juana Pulgar-line candidates. Do not attach this entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, or other Dario candidates without a later reviewed identity bridge.
