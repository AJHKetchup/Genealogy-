---
type: identity_conflict_analysis
status: draft
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260524182051046.md"
worker: postconv-identity-analysis-20260524194210355
staged_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260524182051046.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524182051046.md"
source: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: "page 1; register page 58; entry 172"
analysis_status: hold_for_conversion_qa
canonical_readiness: hold
---

# Identity/Conflict Analysis: Entry 172 Conversion Conflict

## Blockers

- The exact staged draft analyzed here is `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260524182051046.md`.
- The staged draft and its source packet identify a material row-level conversion conflict, not a minor name variant.
- The assigned chunk records entry 172 as the Pulgar/Arriagada row for `Jose del Carmen Segundo Pulgar Arriagada`; the assigned converted Markdown currently records entry 172 as a non-Pulgar row for `Jose Miguel`, father `Oswaldo Bunster`, mother `Amelia de la Maza`.
- The staged conflict draft itself describes the converted-file conflict as `Jose Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`. That differs from the current converted Markdown inspected for this analysis. Conversion QA must explain the derivative-state mismatch.
- The father field in the Pulgar/Arriagada row remains unresolved between `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]`.
- No same-person merge, parent merge, Dario attachment, relationship promotion, or canonical fact promotion is ready from this conflict draft.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Registration

Literal evidence:

- The assigned chunk transcribes entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 at about 3 p.m. at `Calle de Valdivia`.
- The same chunk gives father `Jose del Carmen Pulgar S.`, Chilean, `Empleado`, resident at `Calle de Colipi`.
- The same chunk gives mother `Juana Arriagada de Pulgar`, Chilean, `Su sexo`, resident at `Calle de Colipi`.
- The source packet for this exact revision says source-image review supports the Pulgar/Arriagada row as the controlling row and supports the broad father reading `Jose del Carmen Pulgar`, without deciding whether a final `S.` or other mark is present.
- Prior proof-review updates for this chunk support the child name and mother reading after image reread, while keeping father and grouped parent claims on hold for conversion QA.

Interpretation:

- This is the leading identity hypothesis for the assigned draft. The chunk, source packet, and prior reread notes align on the Pulgar/Arriagada family cluster.
- It is not canonical-ready because the assigned converted Markdown and staged derivative-summary wording conflict with the row, and the father suffix is unresolved.

Scores:

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.88 | Strong staged chunk/source-packet support for the child-parent cluster; reduced by derivative conflict and father-suffix uncertainty. |
| conflict_severity | 0.96 | Competing readings change the child, parents, date/place details, and family cluster. |
| evidence_quality | 0.84 | Civil-register source context and chunk are strong, but the converted file is materially contradicted. |
| conversion_confidence | 0.43 | The chunk/source-packet reading is usable for staging, while the assigned converted Markdown is not reliable for this row. |
| claim_probability | 0.87 | Most probable current interpretation of the assigned entry-172 evidence. |
| relevance | 0.98 | Direct Pulgar/Arriagada birth and parent evidence. |
| canonical_readiness | 0.14 | Hold for targeted conversion QA and proof review. |

## Hypothesis 2: Entry 172 Is A Non-Pulgar Converted-File Row

Literal evidence:

- The staged conflict draft reports the converted Markdown as `Jose Francisco`, father `Oswaldo Gomez`, mother `Emilia de la Cruz`.
- The current converted Markdown inspected here instead records entry 172 as `Jose Miguel`, father `Oswaldo Bunster`, mother `Amelia de la Maza`, born 26 March 1888 at 10 p.m. in `En esta Subdelegacion`.
- Neither derivative non-Pulgar reading matches the assigned chunk/source-packet Pulgar row.

Interpretation:

- This is a conversion-control hypothesis, not a person-identity conclusion.
- Do not create or promote non-Pulgar people or relationships from this assigned entry unless targeted conversion QA proves the Pulgar/Arriagada assignment is wrong.

Scores:

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.06 | Supported only by conflicted derivative text. |
| conflict_severity | 0.96 | Accepting it would displace all Pulgar/Arriagada evidence for the assigned draft. |
| evidence_quality | 0.17 | Derivative-only and internally inconsistent between staged summary and current file state. |
| conversion_confidence | 0.09 | The converted file is the disputed artifact. |
| claim_probability | 0.05 | Plausible only as file-assignment, stale-conversion, or row-drift explanation. |
| relevance | 0.78 | Important as a false-positive guardrail. |
| canonical_readiness | 0.01 | Do not promote. |

## Hypothesis 3: Entry-172 Jose/Juana Parents Match Other Pulgar Parent Candidates

Literal evidence:

- Under the Pulgar hypothesis, entry 172 names father `Jose del Carmen Pulgar` or possible `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar`.
- Existing canonical `wiki/people/jose-del-carmen-pulgar.md` has a separate drafted child link to `Tulio Cesar Luis Jose` from another staged relationship.
- Existing canonical `wiki/people/juana-arriagada-de-pulgar.md` carries entry-172 evidence for `Jose del Carmen Segundo Pulgar Arriagada`.
- Existing local context also has a separate `Juana de Dios Amagada de Pulgar` candidate tied to another Pulgar child-parent cluster; that literal name is not identical to `Juana Arriagada de Pulgar`.

Interpretation:

- The shared Jose/Pulgar and Juana/Pulgar family context justifies a targeted cross-entry parent-candidate review.
- It does not justify a merge. `Juana Arriagada de Pulgar`, `Juana de Dios Amagada de Pulgar`, and any other Jose/Juana candidates must remain separate until proof review shows the differences are source-visible variants or conversion errors.

Scores:

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.45 | Plausible local family cluster, but no cross-entry bridge is proved by this conflict draft. |
| conflict_severity | 0.64 | Premature parent merging could combine distinct people or preserve a conversion error. |
| evidence_quality | 0.55 | Useful local staged/canonical evidence, but conversion QA is still outstanding. |
| conversion_confidence | 0.37 | Entry 172 is blocked and related Jose/Juana readings are image-sensitive. |
| claim_probability | 0.42 | Possible, not established. |
| relevance | 0.90 | Directly relevant to Pulgar-line parent structure. |
| canonical_readiness | 0.06 | Hold for parent-candidate proof review after conversion QA. |

## Dario-Line Comparison

| candidate | comparison result | probability/action |
| --- | --- | --- |
| `Dario Arturo Pulgar-Smith` | Canonical page is family-supplied as Alexander John Heinz's maternal grandfather and explicitly warns against automatic merge with similarly named Pulgar records. Entry 172 does not name Dario, Arturo, Smith, Pulgar-Smith, Alexander John Heinz, or a grandchild relationship. | Direct relevance 0.01; do not attach. |
| `Dario Arturo Pulgar` | Local staged CV work treats this as a document-level CV subject with a separate unresolved bridge to `Dario Arturo Pulgar-Smith`. Entry 172 provides no CV-era identity bridge and does not name Dario Arturo. | Direct relevance 0.01; do not attach. |
| `Dario Jose Pulgar-Arriagada` | Existing staged contexts preserve this as a distinct Dario Jose/Pulgar-Arriagada cluster. Entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Jose. | Same-person probability 0.02; no merge. |
| `Dario/Dario Pulgar Arriagada` | Existing canonical `Darío Pulgar Arriagada` is a separate 2000 expropriation-event stub. Entry 172 is an 1888 birth-registration conflict for a different given-name cluster. | Same-person probability 0.01; no merge. |
| Jose/Juana parent candidates | Entry 172 directly names Jose/Juana candidates and may later matter for Pulgar-line structure. | Same-family relevance 0.42; proved same-person merge now 0.12; require separate proof review. |

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
| 2 | Entry-172 Jose/Juana parents may match other Pulgar-line parent candidates. | 0.42 | Preserve as possible; require cross-entry parent-candidate proof review. |
| 3 | Entry 172 is represented by the non-Pulgar converted Markdown row. | 0.05 | Treat as conversion/file-state conflict unless QA proves otherwise. |
| 4 | Entry 172 directly bridges to any Dario identity. | 0.01 | Reject for this draft; no Dario attachment or merge. |

## Recommended Next Action

Keep the exact staged conflict draft and all dependent identity, claim, relationship, and parent-candidate drafts at `hold_for_conversion_qa`.

Exact next proof-review or promotion step needed: run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the source image and the current converted Markdown. The QA note must identify the controlling row for register page 58 entry 172, reconcile the staged draft's non-Pulgar derivative wording with the current converted-file row, and explicitly record the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After conversion QA, rerun proof review on child birth name, sex, registration date, birth date/time/place, father, mother, informant, parent attributes, and child-parent relationships. Separately run Jose/Juana parent-candidate identity review before merging `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, `Juana Arriagada de Pulgar`, `Juana de Dios Amagada de Pulgar`, or any other Jose/Juana Pulgar-line candidates. Do not attach this entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, or other Dario candidates without a later reviewed identity bridge.
