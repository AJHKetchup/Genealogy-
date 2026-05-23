---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-conversion-conflict-candidates.md
worker: postconv-identity-analysis-20260523053537290
staged_draft: research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-conversion-conflict-candidates.md
source_packet: research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-jose-del-carmen-segundo-pulgar-arriagada.md
source_path: raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png
converted_file: raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md
chunk: raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md
chunk_id: CHUNK-b8f4f0490a36-P0001-01
page_reference: page 1; register page 58; entry 172
analysis_status: hold_for_conversion_qa
canonical_readiness: hold
---

# Identity/Conflict Analysis: Entry 172 Conversion Conflict Candidates

## Blockers

- The exact staged draft analyzed here is `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-conversion-conflict-candidates.md`.
- The assigned chunk and directly inspected source image support entry 172 as a Pulgar/Arriagada birth registration, while the converted Markdown file's entry 172 is an unrelated Jose Francisco / Gomez / de la Cruz derivative row. This is a material same-entry conversion conflict.
- The father-name suffix remains unresolved. The assigned chunk reads `Jose del Carmen Pulgar S.`, but the source image supports `Jose del Carmen Pulgar` and does not show a dependable final `S.` suffix in this review.
- No parent-child relationship, duplicate-person merge, or canonical name normalization should be promoted until conversion QA reconciles the converted Markdown with the source image and records the exact father-name reading.
- The entry does not name Dario. Existing Dario-line context is relevant only as an anti-conflation guardrail.
- No raw sources, converted Markdown, chunks, source packets, staged conflict drafts, or canonical wiki pages were edited.

## Hypothesis 1: Entry 172 Is The Pulgar/Arriagada Birth Registration

Hypothesis: Register page 58, entry 172 records the birth of `Jose del Carmen Segundo Pulgar Arriagada`, son of `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`; the converted Markdown file is mismatched for this entry.

Literal evidence:

- The directly inspected source image shows entry 172 on page 58 and supports the child name `Jose del Carmen Segundo Pulgar Arriagada`, sex `Hombre`, registration date `Siete de Abril de mil ochocientos ochenta i ocho`, birth date `Ocho de Marzo de mil ochocientos ochenta i ocho`, and birthplace `Calle de Valdivia`.
- The source image supports father `Jose del Carmen Pulgar`, Chilean, employed, resident at `Calle de Colipí` or `Calle de Colipi`; a final `S.` suffix is not dependable from the image.
- The source image supports mother `Juana Arriagada de Pulgar`, Chilean, resident at `Calle de Colipí` or `Calle de Colipi`.
- The assigned chunk gives the same Pulgar/Arriagada row, except it includes father `Jose del Carmen Pulgar S.`.
- The source packet reports earlier image-reread notes supporting the Pulgar/Arriagada row and warning that the converted Markdown file is mismatched.
- Existing wiki pages for `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar` preserve related staged evidence, but their presence is context rather than proof that the conversion conflict has been resolved.

Interpretation:

- This is the leading hypothesis. The source image, assigned chunk, source packet, and staged conflict draft all support the Pulgar/Arriagada identity cluster for the intended entry.
- Canonical readiness remains low because the controlling converted Markdown must be corrected or retired before derivative promotion can safely proceed, and the father suffix needs an explicit QA decision.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.90 | Direct image inspection and the assigned chunk support the same child and mother; father suffix remains open. |
| conflict_severity | 0.95 | The competing converted reading changes the child, both parents, event details, and event participants. |
| evidence_quality | 0.88 | Civil birth-register image evidence is strong, with derivative conflict still unresolved. |
| conversion_confidence | 0.45 | The chunk aligns with the image, but the converted Markdown file does not. |
| claim_probability | 0.88 | Highly probable as the correct source-image identity cluster for entry 172. |
| relevance | 0.98 | Directly relevant to Pulgar-line identity and parent-child evidence. |
| canonical_readiness | 0.20 | Hold until conversion QA reconciles the derivative files and father suffix. |

## Hypothesis 2: Entry 172 Is The Gomez/de la Cruz Derivative Row

Hypothesis: Entry 172 should be represented by the converted Markdown row naming a different child and parents, and the Pulgar/Arriagada row belongs to another source assignment.

Literal evidence:

- The converted Markdown file's entry 172 does not name the Pulgar/Arriagada child. It gives a different child and parents: `Jose Francisco`, `Oswaldo Gomez`, and `Emilia de la Cruz`.
- The staged conflict draft preserves this as a literal converted-file conflict, not as image-verified evidence.

Interpretation:

- This hypothesis is weak. It is necessary to preserve as a conflict candidate because the converted file is assigned to the task, but direct image inspection of the referenced source supports the Pulgar/Arriagada row instead.
- Do not create or promote Gomez or de la Cruz people from this entry unless later conversion QA proves the current source-image assignment is wrong.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.08 | Supported only by a mismatched derivative transcript. |
| conflict_severity | 0.95 | Accepting it would displace every core Pulgar/Arriagada fact for entry 172. |
| evidence_quality | 0.20 | Derivative-only support contradicted by the referenced source image. |
| conversion_confidence | 0.12 | The conversion is the artifact under conflict. |
| claim_probability | 0.05 | Possible only as a file-assignment error, not as the visible source-image reading. |
| relevance | 0.70 | Relevant as a false-positive guardrail. |
| canonical_readiness | 0.01 | Do not promote. |

## Hypothesis 3: Entry-172 Jose/Juana Parents Match Other Pulgar-Line Parent Candidates

Hypothesis: The entry-172 father `Jose del Carmen Pulgar` and mother `Juana Arriagada de Pulgar` may be the same Jose/Juana parent candidates appearing elsewhere in local Pulgar-line staging.

Literal evidence:

- Entry 172 names father `Jose del Carmen Pulgar` on the source image; the assigned chunk's added `S.` suffix remains unresolved.
- Entry 172 names mother `Juana Arriagada de Pulgar`.
- Existing `wiki/people/jose-del-carmen-pulgar.md` contains a drafted child link to `Tulio Cesar Luis Jose` from another staged relationship, not this entry.
- Existing `wiki/people/juana-de-dios-amagada-de-pulgar.md` is a separate mother candidate from another Pulgar-line birth-register cluster; its literal name is not the same as `Juana Arriagada de Pulgar`.
- Existing `wiki/people/juana-arriagada-de-pulgar.md` carries this entry-172 mother evidence, not independent proof that she is the same person as `Juana de Dios Amagada de Pulgar`.

Interpretation:

- The father-name overlap justifies a targeted parent-candidate proof review.
- The mother candidates must remain separate hypotheses. `Arriagada`, `de Dios Amagada`, and other Juana readings cannot be merged by surname similarity or married-name style alone.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.48 | Plausible same-family cluster, but cross-entry identity is unproved. |
| conflict_severity | 0.62 | Premature merging could combine separate Jose/Juana couples or preserve a mother-name misread. |
| evidence_quality | 0.58 | Local staged and canonical evidence exists, but the cross-entry bridge is incomplete. |
| conversion_confidence | 0.42 | This entry's image is usable, but derivative files and related Pulgar entries still have QA issues. |
| claim_probability | 0.44 | Possible, not established by this staged draft. |
| relevance | 0.88 | Important for Pulgar-line structure and downstream identity review. |
| canonical_readiness | 0.08 | Hold pending targeted Jose/Juana proof review. |

## Dario-Line Comparison

- `Dario Arturo Pulgar-Smith`: Existing canonical context identifies him from family-supplied knowledge as Alexander John Heinz's maternal grandfather and warns not to merge similarly named Pulgar records without identity review. Entry 172 does not name him.
- `Dario Arturo Pulgar`: Staged CV context uses this document-level name form. Entry 172 does not name Dario Arturo and provides no CV-era bridge.
- `Dario Jose Pulgar-Arriagada`: Staged ICRC/Geneva photograph context names this person from source titles or metadata. Entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, not `Dario Jose Pulgar-Arriagada`.
- `Dario Pulgar Arriagada` / `Darío Pulgar Arriagada`: Existing canonical `wiki/people/dar-o-pulgar-arriagada.md` has a 2000 expropriation event. Entry 172 is an 1888 birth registration for a different given-name cluster.
- Ranked impact: (1) direct impact on `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, and `Juana Arriagada de Pulgar`; (2) indirect Jose/Juana parent-candidate review; (3) no current basis to attach entry 172 to any Dario identity.

## Conflicts

- Same-entry conflict: source image and assigned chunk support Pulgar/Arriagada; converted Markdown supports unrelated derivative families. Severity: critical.
- Name-variant conflict: `Jose del Carmen Pulgar` versus `Jose del Carmen Pulgar S.`. Severity: moderate because it affects father identity matching.
- Relationship conflict: child-father and child-mother relationships are likely correct for the source image but should remain held until derivative conversion QA reconciles the entry. Severity: high for promotion readiness.
- Duplicate-person risk: high if Gomez/de la Cruz people are promoted from the mismatched conversion; moderate if Jose/Juana candidates are merged across Pulgar entries without proof review.
- Chronology conflict: the competing derivative readings carry different birth dates and places. Severity: high for entry 172; low for Dario chronology because no Dario is named.

## Ranked Hypotheses

| rank | hypothesis | probability | action |
| ---: | --- | ---: | --- |
| 1 | Entry 172 is the Pulgar/Arriagada birth registration visible in the source image | 0.88 | Hold for conversion QA, then proof-review claims and relationships. |
| 2 | Entry-172 Jose/Juana parents match other Pulgar-line Jose/Juana candidates | 0.44 | Preserve as possible; require targeted cross-entry parent-candidate proof review. |
| 3 | Entry 172 is the Gomez/de la Cruz derivative row | 0.05 | Treat as conversion mismatch unless QA proves a source-assignment error. |
| 4 | Entry 172 bridges to any Dario identity | 0.01 | No action; do not attach to Dario-line profiles from this source. |

## Recommended Next Action

Keep the staged conflict draft and all dependent identity/relationship claims at `hold_for_conversion_qa`.

Exact next proof-review step: targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01` against `raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png`. The QA note should confirm the Pulgar/Arriagada row as the controlling transcript for page 58 entry 172, correct or retire the mismatched converted Markdown row for this assignment, and state whether the father field reads `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or an uncertain form.

After conversion QA, run proof review on the child birth-name, sex, birth date/time/place, registration date, father, mother, informant, and child-parent relationship claims. Separately run a Jose/Juana parent-candidate identity review before merging `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, `Juana de Dios Amagada de Pulgar`, or any other Jose/Juana parent candidates across records. Do not attach this entry to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or `Dario Pulgar Arriagada` without a later identity-bridging source.
