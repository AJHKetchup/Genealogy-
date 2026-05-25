---
type: identity_conflict_analysis
status: draft
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-evidence-extraction-20260525202358513.md"
worker: postconv-identity-analysis-20260525211749345
staged_conflict_draft: "research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-evidence-extraction-20260525202358513.md"
source_packet: "research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260525202358513.md"
converted_file: "raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md"
chunk: "raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md"
page_reference: "page 1; register page 58; entry 172"
canonical_readiness: hold_for_conversion_qa
---

# Identity/Conflict Analysis: Entry 172 Pulgar/Arriagada Versus Burgos/de la Cruz

## Blockers First

- The staged conflict draft, source packet, and assigned chunk do not agree with the assigned converted Markdown for entry 172. The chunk/source-packet side reads `Jose del Carmen Segundo Pulgar Arriagada`, father `Jose del Carmen Pulgar S.`, mother `Juana Arriagada de Pulgar`; the converted Markdown reads `Jose Miguel`, father `Oswaldo Burgos`, mother `Concepcion de la Cruz`.
- This is a row-level identity conflict, not a spelling or name-variant problem. It blocks promotion of child identity, birth facts, parent-child relationships, parent attributes, and any Pulgar-line bridge.
- The father field remains unresolved as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`. That suffix or mark must not be normalized away before targeted conversion QA.
- Existing canonical snippets for `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and related claims appear to derive from this same Entry 172 cluster. They are useful as local context, but they cannot override the current row conflict.
- Entry 172 does not literally name `Dario Arturo Pulgar-Smith`, document-level CV subject `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, or canonical `Darío Pulgar Arriagada`. Any Dario comparison here is anti-conflation context only.
- `Juana Arriagada de Pulgar`, `Juana de Dios Amagada de Pulgar`, and other Jose/Juana parent candidates must remain separate unless a later proof review establishes identity continuity.

## Evidence Reviewed

- Staged conflict draft: `research/_staging/conflicts/chunk-b8f4f0490a36-p0001-01-entry-172-row-conflict-hold-postconv-evidence-extraction-20260525202358513.md`.
- Staged source packet: `research/_staging/source-packets/chunk-b8f4f0490a36-p0001-01-entry-172-pulgar-arriagada-hold-postconv-evidence-extraction-20260525202358513.md`.
- Assigned chunk: `raw/chunks/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172-codex/page-0001-chunk-01.md`.
- Assigned converted Markdown: `raw/converted/caaa0e3043-registro-de-nacimientos-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no-172.codex.md`.
- Canonical context pages: `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/juana-arriagada-de-pulgar.md`, `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/dario-arturo-pulgar-smith.md`, `wiki/people/dar-o-pulgar-arriagada.md`.
- Reviewed local context discovered by text search, including proof-review notes that already warn the Entry 172 father and row assignment require conversion QA.

No external research was performed. No raw source, converted Markdown, chunk, or canonical wiki page was edited.

## Literal Source Readings Kept Separate

### Pulgar/Arriagada Reading

The assigned chunk transcribes page 58, entry 172 as:

- Registration date: `Siete de Abril de mil ochocientos ochenta i ocho`.
- Child: `Jose del Carmen Segundo Pulgar Arriagada`; sex `Hombre`.
- Birth: `Ocho de Marzo de mil ochocientos ochenta i ocho`, at `tres de la tarde`, place `Calle de Valdivia`.
- Father field: `Jose del Carmen Pulgar S.`, Chilean, `Empleado`, domicile `Calle de Colipí`.
- Mother field: `Juana Arriagada de Pulgar`, Chilean, `Su sexo`, domicile `Calle de Colipí`.
- Declarant/compareciente: `Ernesto Herrera L.`, present at birth, age 26, employee, domicile `Calle de Valdivia`.

### Burgos/de la Cruz Reading

The assigned converted Markdown reads entry 172 as:

- Child: `José Miguel`; sex `Varon`.
- Birth: `El seis de Abril de mil ochocientos ochenta i ocho`, at `diez de la noche`, place `En esta`.
- Father: `Oswaldo Burgos`.
- Mother: `Concepcion de la Cruz`.
- Declarant: `Oswaldo Burgos`, age 26.

### Interpretation

The two readings describe different children, parents, birth dates, places, declarants, and register-page context. They cannot both be promoted as the same entry 172 reading. The source packet states that image-reviewed context favors a Pulgar/Arriagada row, but this analysis does not perform conversion QA and does not certify the controlling transcription.

## Hypotheses And Evidence

### Hypothesis 1: Entry 172 Controls As The Pulgar/Arriagada Birth Row

This hypothesis says the controlling row is for `Jose del Carmen Segundo Pulgar Arriagada`, child of a father recorded as `Jose del Carmen Pulgar S.` or similar and mother `Juana Arriagada de Pulgar`.

Supporting evidence:

- The staged conflict draft and source packet both identify the assignment as a Pulgar/Arriagada birth-registration row.
- The assigned chunk gives a full row-level transcription for a Pulgar/Arriagada child, parents, birth date/place, declarant, and registration date.
- Existing canonical pages for `Jose del Carmen Segundo Pulgar Arriagada` and `Juana Arriagada de Pulgar` contain generated evidence snapshots matching this Entry 172 cluster.
- Prior local proof-review context found direct relationship support for the narrow mother relationship and high but suffix-sensitive support for the father relationship.

Conflicts and limits:

- The assigned converted Markdown reads the same entry number as Burgos/de la Cruz.
- The father suffix/mark is unresolved.
- Existing canonical generated evidence may be downstream of the same conflicted conversion family and is not independent confirmation.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.72 | Strong agreement among staged draft, source packet, and chunk, but blocked by the assigned converted-file contradiction. |
| conflict_severity | 0.96 | Entire row identity and parent set differ. |
| evidence_quality | 0.68 | Detailed derivative transcription plus local review context, but current conversion set is internally inconsistent. |
| conversion_confidence | 0.38 | Low until targeted QA certifies the controlling row and father field. |
| claim_probability | 0.70 | Probable as a staged hypothesis, not canonically ready. |
| relevance | 0.92 | Highly relevant to Pulgar/Arriagada family context if confirmed. |
| canonical_readiness | 0.15 | Hold for conversion QA and proof review. |

### Hypothesis 2: Entry 172 Controls As The Burgos/de la Cruz Birth Row

This hypothesis says the assigned converted Markdown is the controlling transcription and the Pulgar/Arriagada row belongs to another row, image, or assignment context.

Supporting evidence:

- The assigned converted Markdown explicitly labels entry 172 as `José Miguel`, child of `Oswaldo Burgos` and `Concepcion de la Cruz`.
- It provides internally coherent details for that row: father/declarant `Oswaldo Burgos`, mother `Concepcion de la Cruz`, birth date, and place.

Conflicts and limits:

- The staged conflict draft, source packet, and assigned chunk all reject or contradict this as the family-relevant row.
- The source packet says image-reviewed context aligns at a high level with the Pulgar/Arriagada row.
- This reading has no apparent Pulgar-line relevance unless QA finds that the Pulgar staging was attached to the wrong source.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.40 | One assigned derivative supports it, but all staged task context flags it as conflicting. |
| conflict_severity | 0.96 | Mutually exclusive with the Pulgar/Arriagada row. |
| evidence_quality | 0.44 | Coherent derivative reading, but not supported by the staged source-packet/chunk set. |
| conversion_confidence | 0.34 | Cannot be relied on until QA resolves the mismatch. |
| claim_probability | 0.28 | Plausible as a conversion/assignment survivor, not the leading identity hypothesis. |
| relevance | 0.10 | Low genealogical relevance to the Pulgar-line task unless it proves misassignment. |
| canonical_readiness | 0.05 | Not ready for promotion from this task. |

### Hypothesis 3: The Pulgar/Arriagada Child Matches Existing Canonical Stub `Jose del Carmen Segundo Pulgar Arriagada`

This hypothesis applies only if Hypothesis 1 is confirmed by QA.

Supporting evidence:

- The canonical stub preferred name exactly matches the chunk child name.
- Its evidence snapshot cites birth name, birth date/time, birth place, sex, and source-packet references from this same chunk family.
- The canonical page links to `Juana Arriagada de Pulgar` as probable mother, matching the chunk/source-packet mother field.

Conflicts and limits:

- The canonical page is downstream local context, not independent proof.
- The current row conflict can undercut the canonical claims if the converted-file reading proves controlling.
- No identity bridge to later Dario-line people is provided by this child stub.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.78 | Exact local name and evidence-cluster match if the Pulgar row is confirmed. |
| conflict_severity | 0.82 | Dependent on a severe underlying conversion conflict. |
| evidence_quality | 0.60 | Contextual and derivative; not independent of the conflicted source family. |
| conversion_confidence | 0.38 | Same conversion blocker as Hypothesis 1. |
| claim_probability | 0.66 | Probable staged linkage, held pending QA. |
| relevance | 0.90 | Directly relevant to existing wiki identity management. |
| canonical_readiness | 0.18 | Hold; do not add or revise canonical claims. |

### Hypothesis 4: `Jose del Carmen Pulgar S.` Is The Existing `Jose del Carmen Pulgar`

This hypothesis concerns the father candidate only.

Supporting evidence:

- The father field in the chunk begins with `Jose del Carmen Pulgar`.
- There is an existing canonical stub `Jose del Carmen Pulgar`.
- Other local context has a `Jose del Carmen Pulgar` parent candidate in a separate Entry 513 cluster.

Conflicts and limits:

- The father suffix/mark in Entry 172 is unresolved.
- The existing `Jose del Carmen Pulgar` page is sparse and currently includes a draft child link to `Tulio Cesar Luis Jose`, not a confirmed Entry 172 child-father relationship.
- A same-name father in multiple records may be the same person, a relative, or separate same-name individuals.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.50 | Name overlap is meaningful but not enough for a merge or canonical parent assertion. |
| conflict_severity | 0.70 | Risk lies in false parent merge and suffix loss. |
| evidence_quality | 0.48 | Limited local context, with unresolved father-field transcription. |
| conversion_confidence | 0.36 | Father field requires targeted QA. |
| claim_probability | 0.46 | Possible, not proved. |
| relevance | 0.85 | Important parent candidate if the row is confirmed. |
| canonical_readiness | 0.10 | Hold for father-field QA and parent-candidate proof review. |

### Hypothesis 5: `Juana Arriagada de Pulgar` Matches Existing Canonical Stub `Juana Arriagada de Pulgar`

This hypothesis concerns the mother candidate only.

Supporting evidence:

- The chunk/source-packet mother field and canonical stub preferred name match exactly.
- The canonical page's evidence snapshot names `Jose del Carmen Segundo Pulgar Arriagada` as probable child, matching the Entry 172 cluster.
- Prior local proof-review context treated the narrow child-mother relationship as directly supported but warned against broader mother-name normalization.

Conflicts and limits:

- The row conflict still blocks canonical readiness for this task.
- `Juana Arriagada de Pulgar` is a married-style name; it should not be silently normalized to an unrecorded maiden identity.
- This person must not be merged with `Juana de Dios Amagada de Pulgar`, `Juana de Dios Amador`, or other Juana candidates by visual/name similarity alone.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.74 | Exact local name and relationship-cluster match, subject to row QA. |
| conflict_severity | 0.78 | False merge risk with other Juana candidates is material. |
| evidence_quality | 0.62 | Strong within this cluster, not independent. |
| conversion_confidence | 0.40 | Mother reading is less disputed than father suffix but still tied to the row conflict. |
| claim_probability | 0.68 | Probable as a staged cluster match. |
| relevance | 0.88 | Direct parent identity relevance. |
| canonical_readiness | 0.18 | Hold for conversion QA and mother-identity policy review. |

### Hypothesis 6: Entry 172 Provides A Bridge To `Dario Arturo Pulgar-Smith` Or Document-Level `Dario Arturo Pulgar`

Supporting evidence:

- If the Pulgar/Arriagada row controls, it contains the `Pulgar` surname and a possible family-cluster lead.
- Canonical `Dario Arturo Pulgar-Smith` exists as a family-supplied maternal-grandfather profile and explicitly requires identity review before attaching records mentioning Dario, Pulgar, Pulgar-Arriagada, or Pulgar-Smith.
- Staged CV materials elsewhere use document-level `Dario Arturo Pulgar`, with separate proof-review requirements for identity-bearing CV pages.

Conflicts and limits:

- Entry 172 does not name Dario, Arturo, Smith, Pulgar-Smith, Alexander John Heinz, a grandchild, spouse, or descendant.
- A birth of `Jose del Carmen Segundo Pulgar Arriagada` in 1888 is not same-person evidence for a later `Dario Arturo Pulgar` identity.
- Family-context hints justify a later lineage double-check only after the row is certified. They do not justify a silent bridge.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.12 | No direct same-person or relationship evidence to either Dario Arturo identity. |
| conflict_severity | 0.88 | High false-merge risk if attached by surname context alone. |
| evidence_quality | 0.18 | Only surname/family-context lead. |
| conversion_confidence | 0.38 | Underlying row not certified. |
| claim_probability | 0.08 | Very low as a bridge claim from this source alone. |
| relevance | 0.42 | Useful only as an anti-conflation lead. |
| canonical_readiness | 0.00 | Not ready for canonical Dario attachment. |

### Hypothesis 7: Entry 172 Is Same-Person Evidence For `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, Or `Darío Pulgar Arriagada`

Supporting evidence:

- The Pulgar/Arriagada surname pair overlaps with existing local Pulgar-Arriagada identity clusters.
- Canonical `Darío Pulgar Arriagada` exists with a 2000 expropriation event.
- Other staged identity notes preserve variants such as `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, and `Dario Pulgar A.` as unresolved candidates.

Conflicts and limits:

- Entry 172 names `Jose del Carmen Segundo Pulgar Arriagada`, not Dario.
- The entry is a birth registration from 1888, while the canonical `Darío Pulgar Arriagada` page currently has a 2000 legal-notice event and no proved birth/parent bridge in this analysis set.
- No reviewed note in this task links the Entry 172 child to any Dario variant by parentage, date, place, spouse, occupation, or continuity of residence.

Scores:

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.05 | Surname overlap only; given names conflict. |
| conflict_severity | 0.92 | Very high false-conflation risk. |
| evidence_quality | 0.12 | No direct identity bridge from this entry. |
| conversion_confidence | 0.38 | Underlying row not certified. |
| claim_probability | 0.03 | Reject as same-person evidence from this source. |
| relevance | 0.35 | Relevant as anti-conflation context. |
| canonical_readiness | 0.00 | No promotion or merge. |

## Conflict Analysis

- Same-person evidence: strongest only within the narrow Entry 172 Pulgar/Arriagada cluster, and only if conversion QA confirms the Pulgar row.
- Duplicate-person risk: moderate for `Jose del Carmen Pulgar S.` versus existing `Jose del Carmen Pulgar`; moderate for `Juana Arriagada de Pulgar` versus other Juana variants; high for any Dario merge.
- Name-variant risk: `Jose del Carmen Pulgar S.` must not be automatically reduced to `Jose del Carmen Pulgar`; `Juana Arriagada de Pulgar` must not be changed to `Juana de Dios Amagada de Pulgar`, `Juana de Dios Amador`, or another normalized form.
- Relationship conflict: the converted-file parents `Oswaldo Burgos` and `Concepcion de la Cruz` are incompatible with the chunk/source-packet parents `Jose del Carmen Pulgar S.` and `Juana Arriagada de Pulgar`.
- Chronology conflict: the two readings give different birth dates and places. This blocks birth-date, birth-place, and parent-attribute promotion.
- Canonical state conflict: existing canonical/generated Entry 172 evidence should be treated as a held local cluster, not as an independent resolution of the current conversion conflict.

## Ranked Conclusions

| Rank | Hypothesis | Probability | Next proof-review or promotion step required |
| ---: | --- | ---: | --- |
| 1 | The controlling row is the Pulgar/Arriagada birth for `Jose del Carmen Segundo Pulgar Arriagada`. | 0.70 | Targeted conversion QA against the source image, assigned converted Markdown, assigned chunk, and source packet. |
| 2 | The Pulgar/Arriagada child matches the existing canonical stub of the same name. | 0.66 | After row QA, proof-review the child identity and already-promoted/generated claims for consistency. |
| 3 | `Juana Arriagada de Pulgar` matches the existing canonical stub of the same name. | 0.68 | After row QA, proof-review mother identity as recorded, preserving married-style name uncertainty. |
| 4 | `Jose del Carmen Pulgar S.` is the existing `Jose del Carmen Pulgar`. | 0.46 | Father-field QA first; then parent-candidate review comparing all Jose del Carmen Pulgar records. |
| 5 | The controlling row is the Burgos/de la Cruz child `Jose Miguel`. | 0.28 | Conversion QA must explain whether the Pulgar staging is misassigned or the converted file is wrong. |
| 6 | Entry 172 is an ancestor-line lead for `Dario Arturo Pulgar-Smith` or CV `Dario Arturo Pulgar`. | 0.08 | Only after Entry 172 QA and a separate lineage bridge review; then separately bridge `Dario Arturo Pulgar` to `Dario Arturo Pulgar-Smith`. |
| 7 | Entry 172 is same-person evidence for `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, or canonical `Darío Pulgar Arriagada`. | 0.03 | No merge; require direct continuity evidence before any comparison can advance. |

## Recommended Next Action

Hold this staged conflict for targeted conversion QA. The exact QA step is: compare the source image for page 58, entry 172 against the assigned converted Markdown, assigned chunk, and source packet; certify whether entry 172 is the Pulgar/Arriagada row or the Burgos/de la Cruz row; and, if Pulgar/Arriagada controls, certify the father field as `Jose del Carmen Pulgar`, `Jose del Carmen Pulgar S.`, or `Jose del Carmen Pulgar [?]`.

After QA, rerun proof review before any canonical promotion. The proof review should be scoped in this order:

1. Child identity and birth facts for `Jose del Carmen Segundo Pulgar Arriagada`.
2. Mother relationship and mother-name identity handling for `Juana Arriagada de Pulgar`.
3. Father relationship and father-candidate handling for `Jose del Carmen Pulgar` or `Jose del Carmen Pulgar S.`.
4. Anti-conflation review against `Juana de Dios Amagada de Pulgar`, `Juana de Dios Amador`, Entry 513 parent candidates, `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, and `Darío/Dario Pulgar Arriagada`.

Do not merge people, rename canonical pages, promote new facts, or attach this evidence to any Dario-line person until those steps are complete.
