---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/identity/chunk-b8f4f0490a36-p0001-01-entry-172-identity-candidates-20260522150707183.md
worker: postconv-identity-analysis-20260523054849131
staged_draft: research/_staging/identity/chunk-b8f4f0490a36-p0001-01-entry-172-identity-candidates-20260522150707183.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-jose-del-carmen-segundo-pulgar-arriagada.md
source_path: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: page 1; register page 58; entry 172
analysis_status: hold_for_conversion_qa
canonical_readiness: hold
---

# Identity/Conflict Analysis: Entry 172 Identity Candidates

## Blockers

- The exact staged draft analyzed here is `research/_staging/identity/chunk-b8f4f0490a36-p0001-01-entry-172-identity-candidates-20260522150707183.md`.
- The active staged draft and assigned chunk read entry 172 as a Pulgar/Arriagada birth registration, but the assigned converted Markdown file reads entry 172 as an unrelated registration naming a different child and parents. This is a material same-entry conversion conflict.
- The active staged source packet says the original source image and manifest page image were not available in this checkout for direct verification in this revision. Earlier reviewed notes report an image reread supporting the Pulgar/Arriagada row; those notes are useful review context, not a fresh verification for this worker.
- The father's exact recorded name remains unresolved: the assigned chunk gives `Jose del Carmen Pulgar S.`, while earlier image-reread notes report `Jose del Carmen Pulgar` without a clearly visible final `S.` suffix.
- Existing canonical pages already contain promoted or auto-generated evidence from this entry for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar`. This note does not change those pages and does not add any merge or promotion recommendation beyond targeted QA.
- The staged draft does not name Dario. Existing Dario-line pages are relevant only as anti-conflation context; this entry must not be attached to Dario identities by surname or family context alone.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Registration

Literal evidence:

- The staged draft lists `Jose del Carmen Segundo Pulgar Arriagada` as the child, based on the assigned chunk's child field.
- The assigned chunk transcribes entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`, registered `Siete de Abril de mil ochocientos ochenta i ocho`, born `Ocho de Marzo de mil ochocientos ochenta i ocho, a las tres de la tarde`, at `Calle de Valdivia`.
- The assigned chunk names the father as `Jose del Carmen Pulgar S.`, Chilean, employed, resident at `Calle de Colipí`.
- The assigned chunk names the mother as `Juana Arriagada de Pulgar`, Chilean, occupation `Su sexo`, resident at `Calle de Colipí`.
- The active source packet preserves earlier image-reread notes reporting the child as `Jose del Carmen Segundo Pulgar Arriagada`, the father as `Jose del Carmen Pulgar`, and the mother as `Juana Arriagada de Pulgar`.
- Existing canonical `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` contains life facts from this source packet, and `wiki/people/juana-arriagada-de-pulgar.md` contains a probable child link to this child from this entry.

Interpretation:

- This is the leading identity hypothesis for the staged draft because the staged identity draft, assigned chunk, source packet, and prior reread notes all point to the Pulgar/Arriagada row.
- Promotion readiness remains low because the active converted Markdown file contradicts the staged draft and the current checkout did not provide a directly verifiable source image for this worker.
- The father's `S.` suffix should be treated as an unresolved literal-reading issue, not as a normalized identity component.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.78 | Staged draft, chunk, source packet, and prior reread notes align on the Pulgar/Arriagada row, reduced by the current image-availability and converted-file conflict. |
| conflict_severity | 0.94 | The competing converted reading changes the child, parents, event details, and event participants. |
| evidence_quality | 0.72 | Civil birth registration would be strong evidence, but this pass relies on derivative artifacts and prior reviewed notes. |
| conversion_confidence | 0.38 | The chunk supports the Pulgar row while the converted Markdown file gives a different row. |
| claim_probability | 0.76 | More probable than the unrelated converted row on local staged evidence, but blocked for promotion. |
| relevance | 0.96 | Directly relevant to Pulgar/Arriagada identity and parent-child evidence. |
| canonical_readiness | 0.15 | Hold until targeted conversion QA reconciles the source image, chunk, and converted Markdown. |

## Hypothesis 2: Entry 172 Is The Converted Markdown's Unrelated Registration

Literal evidence:

- The active converted Markdown file's entry 172 reads `José Francisco`, father `Oswaldo Gomez`, and mother `Emilia de la Cruz`.
- The staged draft reports a related conversion conflict in which the converted Markdown instead gives `José Miguel`, father `Oswaldo Bunster`, and mother `Amelia de la Maza`.
- Neither converted-reading variant names `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, or `Juana Arriagada de Pulgar`.

Interpretation:

- This hypothesis is preserved only because the assigned converted file is part of the evidence chain and conflicts with the staged draft.
- It should be treated as a conversion/file-assignment conflict, not as identity evidence for Bunster, Gomez, de la Maza, or de la Cruz people, unless targeted QA proves the Pulgar/Arriagada assignment is wrong.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.10 | Supported only by conflicted derivative conversion text. |
| conflict_severity | 0.94 | Accepting it would displace all core Pulgar/Arriagada facts for entry 172. |
| evidence_quality | 0.22 | Derivative-only support contradicted by the staged draft, chunk, source packet, and prior reread context. |
| conversion_confidence | 0.12 | The conversion is the artifact under dispute and appears internally unstable across notes. |
| claim_probability | 0.06 | Plausible only as a source/file-assignment error or unreconciled conversion output. |
| relevance | 0.70 | Relevant as a false-positive guardrail. |
| canonical_readiness | 0.01 | Do not promote or create identities from this mismatch. |

## Hypothesis 3: Entry-172 Jose/Juana Parents Match Other Pulgar-Line Parent Candidates

Literal evidence:

- This entry, under the Pulgar hypothesis, records father `Jose del Carmen Pulgar S.` in the assigned chunk and `Jose del Carmen Pulgar` in earlier image-reread notes.
- This entry records mother `Juana Arriagada de Pulgar`.
- Existing `wiki/people/jose-del-carmen-pulgar.md` contains a drafted child link to `Tulio Cesar Luis Jose` from another staged relationship, not from this entry.
- Existing `wiki/people/juana-de-dios-amagada-de-pulgar.md` contains a drafted child link to `Tulio Cesar Luis Jose`; its literal recorded name differs from `Juana Arriagada de Pulgar`.
- Existing `wiki/people/juana-arriagada-de-pulgar.md` carries this entry-172 mother evidence, not independent proof that she is the same person as `Juana de Dios Amagada de Pulgar`.

Interpretation:

- The repeated `Jose del Carmen Pulgar` form justifies a targeted parent-candidate proof review.
- The Juana candidates must remain separate hypotheses. `Juana Arriagada de Pulgar` and `Juana de Dios Amagada de Pulgar` cannot be merged by surname similarity, married-name styling, or family-context expectation alone.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.46 | Plausible Pulgar-line parent cluster, but cross-entry identity is not proven. |
| conflict_severity | 0.60 | Premature merge could combine separate couples or preserve a misread mother surname. |
| evidence_quality | 0.52 | Local staged and canonical evidence exists, but the bridge across entries is incomplete. |
| conversion_confidence | 0.35 | This b8f4 entry is conversion-blocked; related Pulgar entries have their own QA issues. |
| claim_probability | 0.42 | Possible, not established by this staged draft. |
| relevance | 0.86 | Important for Pulgar-line structure and downstream identity review. |
| canonical_readiness | 0.08 | Hold pending targeted Jose/Juana identity proof review. |

## Hypothesis 4: Event Participants Are Not Family Relationships

Literal evidence:

- Under the assigned chunk's Pulgar reading, `Ernesto Herrera L.` is the compareciente, present at the birth, age 26, employed, resident at `Calle de Valdivia`.
- Under the assigned chunk's Pulgar reading, `[signature] Emilio Riquelme V.` appears as the civil official/signatory.
- The converted Markdown gives different event participants under the unrelated registration reading.

Interpretation:

- If the Pulgar row is confirmed, Ernesto Herrera L. is an event informant only unless another source states kinship.
- Emilio Riquelme V. is an official/signatory only and should not be treated as Pulgar family evidence.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.58 | Supported by the assigned chunk and prior reread context, but affected by the same conversion conflict. |
| conflict_severity | 0.62 | Participant names differ between derivative readings, but family identity turns on the whole-row conflict. |
| evidence_quality | 0.50 | Derivative event-participant evidence only in this pass. |
| conversion_confidence | 0.34 | Blocked by the entry-level conversion mismatch. |
| claim_probability | 0.55 | Plausible within the Pulgar-row hypothesis, uncertain overall. |
| relevance | 0.40 | Useful for source integrity, low for family identity. |
| canonical_readiness | 0.05 | Do not create family links from these participant names. |

## Dario-Line Comparison

- `Dario Arturo Pulgar-Smith`: Existing canonical context identifies him from family-supplied knowledge as Alexander John Heinz's maternal grandfather and explicitly warns not to merge similarly named Pulgar records without identity review. This entry does not name him.
- `Dario Arturo Pulgar`: Staged CV material uses this document-level name form for a twentieth-century CV subject. Entry 172 does not name Dario Arturo and provides no CV-era identity bridge.
- `Dario Jose Pulgar-Arriagada`: Staged ICRC photograph material uses this name from source title or metadata, with high uncertainty about visual identification in the photograph. Entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario Jose Pulgar-Arriagada.
- `Dario Pulgar Arriagada` / `Darío Pulgar Arriagada`: Existing canonical `wiki/people/dar-o-pulgar-arriagada.md` contains a 2000 expropriation event for Darío Pulgar Arriagada. Entry 172 is an 1888 birth-registration conflict for a different given-name cluster.
- `Dario Pulgar` passenger candidates: Existing canonical stubs distinguish an adult passenger aged 64 and a child passenger aged 11 on a 1953 passenger list. Entry 172 does not name either passenger candidate.

Ranked impact:

| rank | identity area | impact |
| ---: | --- | --- |
| 1 | `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar` | Direct identity and relationship impact. |
| 2 | Jose/Juana parent candidates across Pulgar entries | Possible cross-entry identity question requiring targeted proof review. |
| 3 | Dario-line identities | No current evidence bridge; use only as anti-conflation guardrail. |

## Conflicts

- Same-entry conflict: assigned chunk and staged source packet support the Pulgar/Arriagada row; converted Markdown supports unrelated derivative families. Severity: critical.
- Name-variant conflict: `Jose del Carmen Pulgar S.` versus `Jose del Carmen Pulgar`. Severity: moderate because the suffix affects father matching and canonical identity review.
- Relationship conflict: child-father and child-mother links depend on confirming the controlling row for entry 172. Severity: high for promotion readiness.
- Duplicate-person risk: high if unrelated converted-row names are promoted from the mismatch; moderate if Jose/Juana parent candidates are merged across Pulgar entries without proof review.
- Chronology conflict: the competing readings give different birth dates and places. Severity: high for entry 172, low for Dario chronology because no Dario is named.

## Ranked Hypotheses

| rank | hypothesis | probability | action |
| ---: | --- | ---: | --- |
| 1 | Entry 172 is the Pulgar/Arriagada birth registration represented by the staged draft and chunk. | 0.76 | Hold for conversion QA, then proof-review the scoped claims and relationships. |
| 2 | Entry-172 Jose/Juana parents match other Pulgar-line Jose/Juana candidates. | 0.42 | Preserve as possible; require cross-entry parent-candidate proof review. |
| 3 | Entry 172 is the unrelated converted Markdown row. | 0.06 | Treat as conversion/file-assignment conflict unless QA proves otherwise. |
| 4 | Entry 172 bridges to any Dario identity. | 0.01 | No action; do not attach to Dario profiles from this source. |

## Recommended Next Action

Keep this staged identity draft at `hold_for_conversion_qa`.

Exact next proof-review step: run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against the restored source image or authoritative page image, then reconcile the assigned chunk and converted Markdown so entry 172 has one controlling transcript. The QA note must explicitly decide whether the father field reads `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or an uncertain form.

After conversion QA, run proof review on the child birth name, sex, birth date/time/place, registration date, father, mother, informant, and child-parent relationships. Separately run a Jose/Juana parent-candidate identity review before merging `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, `Juana de Dios Amagada de Pulgar`, or any other Jose/Juana candidates. Do not attach this entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, or Dario passenger candidates without a later source that explicitly bridges identity.
