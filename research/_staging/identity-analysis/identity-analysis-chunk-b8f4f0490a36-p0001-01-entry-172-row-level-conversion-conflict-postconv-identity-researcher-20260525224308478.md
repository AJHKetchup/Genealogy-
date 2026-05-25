---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260525224308478
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525215121005.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525215121005.md"
output_area: "research/_staging/identity-analysis/"
subject: "Entry 172 birth-registration row"
chunk_id: "CHUNK-b8f4f0490a36-P0001-01"
source_path: "raw/sources/Registro de Nacimientos, Circunscripción de Los Ángeles, Chile, 1888, Entry No. 172;.png"
promotion_recommendation: hold_for_conversion_qa
canonical_readiness: not_ready
---

# Identity/Conflict Analysis: Entry 172 Row-Level Conversion Conflict

This note analyzes the staged conflict draft `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525215121005.md`.

## Blockers First

1. Row-control blocker: the referenced current converted Markdown identifies entry 172 as a Burgos/de la Cruz birth, while the referenced current chunk and staged source packet identify entry 172 as a Pulgar/Arriagada birth. These are not name variants of one family.
2. Conversion-certification blocker: no identity promotion should occur until targeted conversion QA compares the source image, current converted Markdown, current chunk, and source packet for entry 172 and records the controlling row.
3. Father-literal blocker: if the Pulgar/Arriagada row is controlling, the father field must be certified only to the visible level: `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.
4. Canonical-dependency blocker: existing wiki pages for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar` contain earlier b8f4-derived evidence snapshots. Because this exact b8f4 conversion is under row-level conflict, those snapshots are cautionary local context, not independent proof for this task.
5. Pulgar-line bridge blocker: this staged draft does not name Dario, Arturo, Smith, Dario Jose, or a later Pulgar-Arriagada public-role/passenger/person cluster. No same-person or family bridge to Dario candidates can be promoted from this row conflict.

## Evidence Reviewed

- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-level-conversion-conflict-postconv-evidence-extraction-20260525215121005.md`.
- Staged source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-revision-postconv-evidence-extraction-20260525215121005.md`.
- Current converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Current chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Existing canonical context: `wiki/people/dario-arturo-pulgar-smith.md`, `wiki/people/dar-o-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/juana-arriagada-de-pulgar.md`, and `wiki/people/juana-de-dios-amagada-de-pulgar.md`.
- Staged Dario context checked only for anti-conflation: source packets for `Dario Jose Pulgar-Arriagada` portrait context, `Dario J. Pulgar Arriagada` 1918 medical-title context, and `Dario Pulgar-Arriagada` 1929 Chile plenipotentiary list context.

## Literal Source Readings

### Reading A: Pulgar/Arriagada Row

The current chunk and the staged source packet read entry 172 on register page 58 as:

- Child: `Jose del Carmen Segundo Pulgar Arriagada`.
- Sex: male / `Hombre`.
- Registration date: 7 April 1888.
- Birth: 8 March 1888 at 3 p.m.
- Birthplace: `Calle de Valdivia`.
- Father: `Jose del Carmen Pulgar S.` in the chunk/source-packet transcription, with the final suffix needing certification.
- Mother: `Juana Arriagada de Pulgar`.
- Parents' residence: `Calle de Colipí`.
- Informant: `Ernesto Herrera L.`, present at birth, age 26, employee, resident at `Calle de Valdivia`.

### Reading B: Burgos/de la Cruz Row

The current converted Markdown reads entry 172 as:

- Child: `José Miguel`.
- Sex: male / `Varon`.
- Registration date: 7 April 1888.
- Birth: 6 April 1888 at 10 p.m.
- Birthplace: `En esta`.
- Father and informant: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Parents described as Chilean, unmarried, and local in the converted transcription.

## Interpretation Kept Separate

Reading A and Reading B describe different children, different parents, different birth dates, different places, and different informants. The conflict is best treated as a row-control or conversion-control conflict, not a same-person, duplicate-person, or name-variant issue.

If Reading A is later certified, it may support a narrow birth-registration identity for `Jose del Carmen Segundo Pulgar Arriagada` with parent candidates `Jose del Carmen Pulgar [S./?]` and `Juana Arriagada de Pulgar`. If Reading B is later certified, the Pulgar/Arriagada claim set for this chunk should not be promoted from this source. This analysis cannot choose between the rows because the assignment forbids conversion work and the staged draft calls for targeted conversion QA.

## Hypotheses And Scores

| Rank | Hypothesis | Supporting evidence | Conflicts / limits | Probability | Identity confidence | Claim probability | Canonical readiness |
| ---: | --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | The assigned chunk/source-packet Pulgar/Arriagada row is the intended family-relevant entry 172, but promotion is blocked. | Current chunk and source packet agree on `Jose del Carmen Segundo Pulgar Arriagada`, parents, birth date, place, and informant. | Current converted Markdown gives a completely different entry-172 family. Father suffix unresolved. | 0.64 | 0.50 | 0.55 | Not ready; conversion QA required. |
| 2 | The current converted Markdown Burgos/de la Cruz row is the controlling entry 172. | Converted Markdown gives internally coherent child, parents, birth date, and informant for entry 172. | Current chunk and staged source packet disagree at row level and support Pulgar/Arriagada. | 0.30 | 0.42 | 0.45 | Not ready; conversion QA required. |
| 3 | `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` are literal-reading variants for the father in Reading A. | Base name is stable across the Pulgar/Arriagada reading; the staged draft explicitly identifies the suffix as unresolved. | The suffix/final mark cannot be normalized silently. Existing `Jose del Carmen Pulgar` wiki context also includes a separate child claim from another staged record. | 0.58 | 0.45 | 0.50 | Not ready; certify literal father field first. |
| 4 | `Juana Arriagada de Pulgar` is the mother in Reading A. | Current chunk and source packet agree on the mother name in the Pulgar/Arriagada row. Existing wiki page has earlier b8f4-derived context. | Dependent on row-control QA. Do not merge with `Juana de Dios Amagada de Pulgar` or other Juana candidates by name similarity. | 0.60 | 0.48 | 0.52 | Not ready; row QA and parent proof review required. |
| 5 | `Jose del Carmen Segundo Pulgar Arriagada` is the same person as any Dario candidate. | Shared Pulgar/Arriagada surname pattern is a family-context hint only. | Different given names; no Dario/Arturo/Smith/Jose bridge in this source; no chronology bridge. | 0.03 | 0.02 | 0.02 | Reject/hold; no merge. |
| 6 | The row proves a bridge to `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, or `Dario Pulgar A.`. | Pulgar and Arriagada surnames are relevant enough to flag for later review if the row is certified. | The row does not name any Dario candidate or state a parent/child/spouse/descendant relationship to them. | 0.05 | 0.04 | 0.04 | Not ready; separate identity-bridge proof review required. |

## Pulgar-Line Candidate Comparison

- `Dario Arturo Pulgar-Smith`: canonical page is family-supplied as maternal grandfather of Alexander John Heinz. This entry does not state `Dario`, `Arturo`, `Smith`, a birth/death date for him, or a relationship to Alexander John Heinz. Probability this row alone supports attachment: 0.04.
- `Dario Arturo Pulgar`: staged CV/document-level contexts use this name in other files. This entry does not name `Dario Arturo Pulgar` or provide CV, occupation, residence, or chronology facts that bridge to that document subject. Probability this row alone supports attachment: 0.05.
- `Dario Jose Pulgar-Arriagada`: staged portrait/photograph contexts use this fuller name mostly from source title/path context; this entry does not name Dario Jose or contain a photograph/caption bridge. Probability this row alone supports attachment: 0.05.
- `Dario/Darío Pulgar Arriagada`: local context includes a 1918 `Darío J. Pulgar Arriagada` medical-title source, a 1929 `Dario Pulgar-Arriagada` official listing, and a 2000 canonical `Darío Pulgar Arriagada` expropriation mention. This entry does not bridge any of those public-role/legal-notice identities to the 1888 child or parents. Probability this row alone supports attachment: 0.06.
- Jose/Juana parent candidates: `Jose del Carmen Pulgar [S./?]` and `Juana Arriagada de Pulgar` are plausible only within Reading A. `Juana de Dios Amagada de Pulgar` is a separate local candidate tied to a different staged child context and must not be silently corrected or merged with `Juana Arriagada de Pulgar`.

## Conflict Assessment

- Same-person conflict: no same-person merge is supported. The named child in Reading A and the named child in Reading B should be treated as separate row candidates until conversion QA resolves the row.
- Duplicate-person conflict: no duplicate-person conclusion is ready for `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Juana Arriagada de Pulgar`; existing wiki entries may be earlier b8f4-derived or separate staged contexts.
- Name-variant conflict: the father suffix is a literal-reading issue, not a normalized name variant. Preserve `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, and `Jose del Carmen Pulgar [?]` until certified.
- Relationship conflict: parent-child links in Reading A are blocked by row-control conflict. Reading B has different parent-child relationships and cannot be reconciled as the same family.
- Chronology conflict: Reading A gives birth on 8 March 1888; Reading B gives birth on 6 April 1888. These cannot both be facts for the same child in entry 172.

## Scores

| Dimension | Score | Rationale |
| --- | ---: | --- |
| Identity confidence | 0.50 | Moderate for identifying the competing row candidates; low for canonical attachment because row control is unresolved. |
| Conflict severity | 0.95 | The rows differ across child, parents, date, place, and informant, blocking all dependent claims. |
| Evidence quality | 0.62 | Staged packet and chunk are detailed, but the controlling conversion file contradicts them. |
| Conversion confidence | 0.35 | Current derivatives conflict; targeted conversion QA is required. |
| Claim probability | 0.55 | Pulgar/Arriagada claims are plausible from chunk/packet but not promotable. |
| Relevance | 0.90 | Directly relevant to Pulgar/Arriagada family-line review if the row is confirmed. |
| Canonical readiness | 0.10 | Not ready for canonical promotion or merge. |

## Recommended Next Action

Run targeted conversion QA for `CHUNK-b8f4f0490a36-P0001-01`: compare the source image, current converted Markdown, current chunk, and staged source packet for page 1 / register page 58 / entry 172. The QA note must decide whether the controlling row is the Pulgar/Arriagada row or the Burgos/de la Cruz row, and if Pulgar/Arriagada is controlling, certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After that, run proof review on only the certified row's narrow claims: child identity, birth date/time, birth place, father claim, mother claim, informant claim, and parent-child relationships. A separate identity-bridge proof review is required before connecting any certified Jose/Juana/child evidence to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, `Dario Pulgar A.`, or any other Jose/Juana parent candidate.
