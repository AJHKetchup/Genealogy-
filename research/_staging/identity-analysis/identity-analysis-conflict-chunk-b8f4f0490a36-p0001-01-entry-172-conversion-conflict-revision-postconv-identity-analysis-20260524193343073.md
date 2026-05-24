---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260524182051046.md
worker: postconv-identity-analysis-20260524193343073
staged_draft: research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260524182051046.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260524182051046.md
source_path: raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: page 1; register page 58; entry 172
analysis_status: hold_for_conversion_qa
canonical_readiness: hold
---

# Identity/Conflict Analysis: Entry 172 Pulgar-Arriagada Conversion Conflict Revision

## Blockers

- The exact staged draft analyzed here is `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-conversion-conflict-revision-postconv-evidence-extraction-20260524182051046.md`.
- The staged draft reports a material row-level conflict: the assigned chunk/source packet support entry 172 as a Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada`, while the assigned converted Markdown records a non-Pulgar child and parents.
- A secondary derivative-artifact discrepancy remains unresolved. The staged draft says the converted Markdown records `Jose Francisco`, father `Oswaldo Gomez`, and mother `Emilia de la Cruz`; the current converted file inspected for this task records entry 172 as `Jose Miguel`, father `Oswaldo Bunster`, and mother `Amelia de la Maza`. Both derivative readings conflict with the assigned chunk/source packet and must be reconciled by conversion QA before promotion.
- The father literal reading is unresolved. The assigned chunk/source packet preserve `Jose del Carmen Pulgar S.` as a possible reading, but the evidence-extraction note says the image review supports the broader father reading `Jose del Carmen Pulgar` without settling a final `S.` or mark.
- No canonical person merge, relationship promotion, or name normalization is ready. This draft should remain `hold_for_conversion_qa` until the controlling row and father field are explicitly decided.
- Entry 172 does not name Dario. Dario-line context is relevant only as an anti-conflation check, not as a bridge to any Dario identity.
- No raw sources, converted Markdown, chunks, staged conflict drafts, source packets, or canonical wiki pages were edited.

## Hypothesis 1: Entry 172 Is The Pulgar-Arriagada Birth Registration

Hypothesis: Register page 58, entry 172 records the birth of `Jose del Carmen Segundo Pulgar Arriagada`, son of `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`; the converted Markdown row is mismatched for this assignment.

Literal evidence:

- The assigned source packet states that the chunk records entry 172 as `Jose del Carmen Segundo Pulgar Arriagada`, male, registered 7 April 1888, born 8 March 1888 about 3 p.m. at `Calle de Valdivia`.
- The assigned chunk transcribes the father as `Jose del Carmen Pulgar S.`, Chilean, `Empleado`, resident at `Calle de Colipi`, and the mother as `Juana Arriagada de Pulgar`, Chilean, `Su sexo`, resident at `Calle de Colipi`.
- The source packet says source-image review in the extraction pass supports the Pulgar/Arriagada row on register page 58, entry 172, and supports `Jose del Carmen Pulgar` as the broad father reading while not settling whether a final `S.` or other mark is present.
- Existing canonical stubs for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar` preserve related local evidence, but their existence does not resolve the conversion conflict.

Interpretation:

- This is the strongest identity hypothesis for the assigned draft because the chunk and source packet agree on the Pulgar/Arriagada family cluster and explicitly identify the converted Markdown as mismatched.
- The child and mother readings are strong enough for staged analysis, but not ready for canonical promotion while the derivative converted file and father suffix remain unresolved.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.89 | Chunk and source packet support the same child-parent cluster; father suffix is still open. |
| conflict_severity | 0.96 | The competing derivative row changes the child, parents, event details, and source family cluster. |
| evidence_quality | 0.84 | Civil-register source packet and assigned chunk are strong, but this note did not rerun image conversion or source preparation. |
| conversion_confidence | 0.42 | The chunk is consistent with the source packet, while the converted Markdown is materially inconsistent. |
| claim_probability | 0.87 | Most likely correct as the intended entry-172 identity cluster. |
| relevance | 0.98 | Directly relevant to Pulgar-line birth and parent-candidate evidence. |
| canonical_readiness | 0.18 | Hold for conversion QA and proof review. |

## Hypothesis 2: Entry 172 Is A Non-Pulgar Converted-Transcript Row

Hypothesis: Entry 172 should be represented by the non-Pulgar converted Markdown row, and the Pulgar/Arriagada row belongs to another assignment or file.

Literal evidence:

- The staged conflict draft reports the converted Markdown as `Jose Francisco`, father `Oswaldo Gomez`, and mother `Emilia de la Cruz`.
- The current converted Markdown inspected for this task instead gives entry 172 as `Jose Miguel`, father `Oswaldo Bunster`, and mother `Amelia de la Maza`.
- Neither converted-file reading matches the assigned chunk/source packet's `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar`.

Interpretation:

- This hypothesis is weak as a person-identity conclusion, but important as a conversion-control hypothesis. It may indicate a stale converted file, row drift, source-image mismatch, or prior conversion overwrite.
- No non-Pulgar child or parent should be promoted from this assigned entry unless conversion QA proves that the Pulgar/Arriagada assignment is wrong.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.07 | Supported only by a derivative transcript already flagged as conflicting. |
| conflict_severity | 0.96 | Accepting it would replace all Pulgar/Arriagada facts for the assigned draft. |
| evidence_quality | 0.18 | Derivative support only; internally inconsistent with the staged draft's own derivative summary. |
| conversion_confidence | 0.10 | The converted file is the artifact under dispute. |
| claim_probability | 0.04 | Possible only as a file-assignment or conversion-state explanation. |
| relevance | 0.78 | Critical as a blocker and false-positive guardrail. |
| canonical_readiness | 0.01 | Do not promote. |

## Hypothesis 3: Entry-172 Jose/Juana Parents Match Other Pulgar-Line Parent Candidates

Hypothesis: The entry-172 father `Jose del Carmen Pulgar` / possible `Jose del Carmen Pulgar S.` and mother `Juana Arriagada de Pulgar` may be the same parent candidates as Jose/Juana figures in other Pulgar-line records.

Literal evidence:

- Entry 172 names the father as `Jose del Carmen Pulgar` with unresolved possible suffix `S.`.
- Entry 172 names the mother as `Juana Arriagada de Pulgar`.
- The canonical `Jose del Carmen Pulgar` stub currently has a separate drafted child link to `Tulio Cesar Luis Jose` from another staged relationship.
- The canonical `Juana Arriagada de Pulgar` stub carries entry-172 evidence for `Jose del Carmen Segundo Pulgar Arriagada`.
- The canonical `Juana de Dios Amagada de Pulgar` stub is a separate mother candidate tied to `Tulio Cesar Luis Jose`; this literal name is not the same as `Juana Arriagada de Pulgar`.

Interpretation:

- The shared father name and Pulgar/Arriagada context justify a targeted cross-entry parent-candidate proof review.
- The mother candidates must remain separate hypotheses until a reviewed source resolves whether `Arriagada`, `Amagada`, `de Dios`, or another reading reflects the same woman or separate people.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.46 | Plausible local family cluster, but no cross-entry identity bridge is established by this draft. |
| conflict_severity | 0.64 | Premature merging could combine separate couples or preserve a mother-name misread. |
| evidence_quality | 0.56 | Local staged/canonical context exists, but conversion QA remains outstanding. |
| conversion_confidence | 0.38 | This entry's derivative state is unstable and related Jose/Juana readings are image-sensitive. |
| claim_probability | 0.43 | Possible, not proved. |
| relevance | 0.90 | Important for Pulgar-line parent structure. |
| canonical_readiness | 0.07 | Hold for parent-candidate proof review. |

## Dario-Line Comparison

| candidate | local evidence considered | result |
| --- | --- | --- |
| `Dario Arturo Pulgar-Smith` | Canonical page identifies him from family-supplied knowledge as Alexander John Heinz's maternal grandfather and warns against automatic merge with similarly named Pulgar records. | Entry 172 does not name him, `Arturo`, `Smith`, Alexander John Heinz, or a grandchild relationship. Probability of direct same-person relevance from this draft: 0.01. |
| `Dario Arturo Pulgar` | Staged CV analyses use this as a document-level subject for `CV of Dario Arturo Pulgar.pdf`, with separate proof-review needed before any bridge to `Dario Arturo Pulgar-Smith`. | Entry 172 does not name Dario Arturo and supplies no CV-era bridge. Probability of direct same-person relevance from this draft: 0.01. |
| `Dario Jose Pulgar-Arriagada` | Existing staged photograph/source-metadata context preserves this name as unresolved and not yet bridged to other Dario identities. | Entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, a different given-name cluster, and no Dario. Probability of direct same-person relevance from this draft: 0.02. |
| `Dario/Dario Pulgar Arriagada` and `Darío Pulgar Arriagada` | Canonical `Darío Pulgar Arriagada` is a separate stub with a 2000 expropriation event; staged notes preserve multiple Dario/Pulgar-Arriagada variants as unresolved. | Entry 172 is an 1888 birth registration for a non-Dario child. No merge or attachment is supported. Probability of direct same-person relevance from this draft: 0.01. |
| Jose/Juana parent candidates | Entry 172 directly names `Jose del Carmen Pulgar` or possible `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`; existing wiki also has `Juana de Dios Amagada de Pulgar` in another child-parent cluster. | Directly relevant, but only as held parent-candidate evidence pending conversion QA and cross-entry proof review. Probability of same-family relevance: 0.43; probability of proved same-person merge now: 0.12. |

## Conflicts

- Same-entry conversion conflict: assigned chunk/source packet support Pulgar/Arriagada; converted Markdown supports non-Pulgar rows. Severity: critical.
- Derivative-state conflict: the staged draft's description of the converted row does not match the current converted file's row. Severity: high for auditability and conversion QA.
- Name-variant conflict: `Jose del Carmen Pulgar` versus `Jose del Carmen Pulgar S.` versus `Jose del Carmen Pulgar [?]`. Severity: moderate-high for father matching.
- Relationship conflict: child-father and child-mother links are probable from the chunk/source packet but should not be promoted while the controlling transcript is unresolved. Severity: high for canonical readiness.
- Duplicate-person risk: high if non-Pulgar converted rows are promoted from this assignment; moderate if Jose/Juana parent candidates are merged across entries by name resemblance.
- Chronology conflict: the derivative converted rows carry different birth dates, places, and participants than the Pulgar/Arriagada row. Severity: high for entry 172; no direct Dario chronology conflict because no Dario is named.

## Ranked Hypotheses

| rank | hypothesis | probability | action |
| ---: | --- | ---: | --- |
| 1 | Entry 172 is the Pulgar/Arriagada birth registration for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.87 | Hold for conversion QA, then proof-review atomic claims and relationships. |
| 2 | Entry-172 Jose/Juana parents may match other Pulgar-line parent candidates. | 0.43 | Preserve as possible; require targeted cross-entry parent-candidate proof review. |
| 3 | Entry 172 is represented by the non-Pulgar converted Markdown row. | 0.04 | Treat as conversion/file-state conflict unless QA proves source-assignment error. |
| 4 | Entry 172 bridges to any Dario identity. | 0.01 | Reject for this draft; do not attach to Dario profiles without a later identity-bearing bridge. |

## Recommended Next Action

Keep the assigned staged conflict draft and all dependent identity, relationship, parent-candidate, and claim drafts at `hold_for_conversion_qa`.

Exact next proof-review or promotion step needed: targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against `raw/sources/Registro de Nacimientos, Circunscripcion de Los Angeles, Chile, 1888, Entry No. 172;.png`. The QA note must identify the controlling row for register page 58 entry 172, reconcile why the staged draft and current converted file report different non-Pulgar derivative rows, and explicitly record the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After conversion QA, rerun proof review on the child birth name, sex, birth date/time/place, registration date, father, mother, informant, parent attributes, and child-parent relationships. Run a separate Jose/Juana parent-candidate identity review before merging `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, `Juana Arriagada de Pulgar`, `Juana de Dios Amagada de Pulgar`, or any other Jose/Juana candidates. Do not attach this entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada` unless a later reviewed source supplies an explicit identity or relationship bridge.
