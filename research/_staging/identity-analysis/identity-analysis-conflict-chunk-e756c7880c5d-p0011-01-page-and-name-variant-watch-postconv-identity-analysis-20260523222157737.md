---
type: identity_conflict_analysis
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/chunk-e756c7880c5d-p0011-01-page-and-name-variant-watch.md"
worker: postconv-identity-analysis-20260523222157737
staged_draft: "research/_staging/conflicts/chunk-e756c7880c5d-p0011-01-page-and-name-variant-watch.md"
subject: "Dr Dario Pulgar A. / Dr Dario Pulgara"
source_packet: "research/_staging/source-packets/chunk-e756c7880c5d-p0011-01-el-aguila-fundo-los-cuartos-dario-pulgar-a.md"
source_path: "raw/sources/El Aguila Nombre Grande Scan.pdf"
converted_file: "raw/converted/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18.codex.md"
chunk: "raw/chunks/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18-codex/page-0011-chunk-01.md"
chunk_id: "CHUNK-e756c7880c5d-P0011-01"
analysis_status: hold_for_conversion_qa
canonical_readiness: hold
---

# Identity/Conflict Analysis: Page And Name Variant Watch

## Blockers First

- This note analyzes the exact staged draft `research/_staging/conflicts/chunk-e756c7880c5d-p0011-01-page-and-name-variant-watch.md`.
- Page provenance is unresolved: the staged draft and chunk path point to assigned page 11, but the Dario article is the text of conversion-job `page-markdown/page-0014.md`; conversion-job `page-markdown/page-0011.md` is a different page with no Dario/Pulgar mention.
- The local conversion job has no `page-images/page-0011.jpg` or `page-images/page-0014.jpg`, so the typed name and handwritten signature cannot be independently reread here.
- The literal source readings must not be normalized: the typed article is transcribed as `DR DARIO PULGAR A,`; the signature is transcribed as `DR. DARIO PULGARA`.
- The article does not state `Arturo`, `Smith`, `Jose`, full `Arriagada`, named parents, spouse, children, birth/death data, or a relationship to Alexander John Heinz.
- No external research was performed. No raw sources, converted Markdown, chunks, conflict drafts, source packets, or canonical wiki pages were edited.

## Literal Evidence

The staged source packet transcribes the core article line:

```text
EL FUNDO LOS CUARTOS PERTENECE COMO YA SE SABE AL DR DARIO PULGAR A,
DISTINGUIDO FACULTATIVO DE CONCEPCION QUIEN HEREDO DE SUS PADRES ESTE
FUNDO ALLA POR EL AÑO 1917
```

It also transcribes the handwritten signature as:

```text
[handwritten signature] DR. DARIO PULGARA [/handwritten signature]
```

Interpretation kept separate: `Pulgar A.` could be a final initial, a spacing/transcription issue, or a second-surname abbreviation. This draft does not prove an expansion to `Arturo` or `Arriagada`.

## Hypothesis 1: Conversion/Page QA Blocker

Supporting evidence:

- The staged draft records that assigned chunk page 11 conflicts with body/page evidence for page 14.
- The source packet says conversion-job `page-markdown/page-0014.md` matches the Dario article, while `page-markdown/page-0011.md` is different.
- Missing page images prevent proof-level reread of the signature and page number.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.10 | The strongest conclusion is not identity; it is page/provenance uncertainty. |
| conflict_severity | 0.82 | A wrong page citation or name reading would affect any promoted claim. |
| evidence_quality | 0.62 | Derivative files agree on the mismatch; image evidence is absent. |
| conversion_confidence | 0.40 | Text can be inspected, but page assignment and signature remain unresolved. |
| claim_probability | 0.90 | The staged draft is very likely a valid QA blocker. |
| relevance | 1.00 | Directly addresses the assigned staged conflict. |
| canonical_readiness | 0.01 | Not ready for canonical use. |

## Hypothesis 2: Narrow Held Identity `Dr Dario Pulgar A.`

Supporting evidence:

- The article directly names `DR DARIO PULGAR A,`.
- It identifies him as a distinguished physician of Concepcion and owner of Fundo Los Cuartos.
- It says he inherited the property from his parents around 1917, but does not name the parents.

Conflicts and limits:

- `DR. DARIO PULGARA` may be a signature reading, a joined surname/initial, or a transcription issue.
- No full-name, vital, or relationship bridge is present.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.70 | The typed name is direct derivative evidence, subject to page/image QA. |
| conflict_severity | 0.35 | Low if held literally; higher if expanded or merged. |
| evidence_quality | 0.64 | Direct article text, but single-source and derivative-only here. |
| conversion_confidence | 0.52 | Typed body is more stable than signature and page metadata. |
| claim_probability | 0.78 | Probable the source names a physician/property owner as `Dr Dario Pulgar A.`. |
| relevance | 0.98 | This is the named person in the staged draft. |
| canonical_readiness | 0.12 | Hold pending page/signature proof review. |

## Hypothesis 3: Same As Older Medical `Dario Pulgar A.` / Adult `Dario Pulgar`

Supporting evidence:

- This article has `Dr Dario Pulgar A.` and `facultativo de Concepcion`.
- Existing local staging preserves older medical Dario comparisons, including `Dario Pulgar A.` and an adult `Dario Pulgar` passenger cluster.
- The 1917 inheritance context is compatible with an older professional identity, but only as chronology context.

Conflicts and limits:

- This draft gives no age, passenger data, full name, or explicit cross-source bridge.
- Other Dario Pulgar clusters have their own QA and identity holds.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.52 | Name, initial, occupation, and chronology are suggestive, not conclusive. |
| conflict_severity | 0.64 | False merge risk is material. |
| evidence_quality | 0.54 | Relevant staged evidence, still QA-sensitive. |
| conversion_confidence | 0.46 | Compared evidence depends on unresolved derivative readings. |
| claim_probability | 0.48 | Plausible same-person hypothesis only. |
| relevance | 0.90 | Important duplicate-person check. |
| canonical_readiness | 0.08 | No merge supported. |

## Hypothesis 4: Same As `Dario Jose Pulgar-Arriagada` / `Dario J. Pulgar Arriagada`

Supporting evidence:

- `A.` could potentially indicate `Arriagada`.
- Other staged Pulgar-Arriagada medical/professional contexts exist locally.

Conflicts and limits:

- This article does not state `Jose`, `J.`, `Arriagada`, or `Pulgar-Arriagada`.
- Local `Dario Jose Pulgar-Arriagada` photograph evidence is title/metadata-sensitive or otherwise held.
- A signature reading of `PULGARA` cannot substitute for a full-name bridge.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.32 | Initial compatibility only, with no full-name proof. |
| conflict_severity | 0.76 | Expanding initials by assumption creates high false-merge risk. |
| evidence_quality | 0.42 | Compared evidence is staged and partly metadata-dependent. |
| conversion_confidence | 0.42 | Signature and comparison sources need proof review. |
| claim_probability | 0.28 | Possible but unresolved. |
| relevance | 0.88 | Required Pulgar-line comparison. |
| canonical_readiness | 0.04 | Preserve separately. |

## Hypothesis 5: Same As Canonical `Darío Pulgar Arriagada`

Supporting evidence:

- The names share `Dario/Darío Pulgar`.
- Existing canonical context has a separate `Darío Pulgar Arriagada` page with a narrow 2000 expropriation-resolution fact.

Conflicts and limits:

- The canonical page gives no bridge to the Fundo Los Cuartos physician/owner.
- The apparent chronology gap creates a serious conflation risk without vital-date or property-continuity evidence.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.14 | Shared name elements only. |
| conflict_severity | 0.82 | High chronology and property-context risk if merged. |
| evidence_quality | 0.46 | Each source supports only its own narrow fact. |
| conversion_confidence | 0.52 | The bridge, not the separate facts, is missing. |
| claim_probability | 0.10 | Low on current evidence. |
| relevance | 0.82 | Relevant because `A.` might invite Arriagada expansion. |
| canonical_readiness | 0.02 | Do not attach. |

## Hypothesis 6: Same As `Dario Arturo Pulgar` / `Dario Arturo Pulgar-Smith`

Supporting evidence:

- The names share `Dario Pulgar`.
- The canonical `Dario Arturo Pulgar-Smith` page is family-supplied and explicitly warns against automatic merging with similarly named Pulgar records.
- Existing CV staging uses `Dario Arturo Pulgar`, but keeps the bridge to `Dario Arturo Pulgar-Smith` on proof-review hold.

Conflicts and limits:

- This draft does not state `Arturo`, `Smith`, `Pulgar-Smith`, the CV context, or any family relationship.
- `A.` is not proof of `Arturo`.
- Family-context hints justify only a double-check, not attachment.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.12 | Shared given name and surname only. |
| conflict_severity | 0.78 | Wrong attachment would contaminate the family-supplied anchor person. |
| evidence_quality | 0.40 | Family context exists, but not as a source bridge here. |
| conversion_confidence | 0.48 | Image QA cannot supply the absent identity bridge. |
| claim_probability | 0.08 | Low on local evidence. |
| relevance | 0.90 | Required Pulgar-Smith comparison. |
| canonical_readiness | 0.01 | No canonical attachment supported. |

## Hypothesis 7: Jose/Juana Parent Candidates Are The Unnamed Parents

Supporting evidence:

- The article states only that Dario inherited the fundo from `sus padres` around 1917.
- Existing local wiki/staging context includes Jose and Juana Pulgar-line parent candidates.

Conflicts and limits:

- No parent is named in this draft.
- Jose/Juana candidates belong to separate records and separate proof-review problems.
- `Dario Jose` contexts elsewhere are not parent evidence.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.05 | The draft contains unnamed parents only. |
| conflict_severity | 0.68 | Unsupported named-parent attachment would create relationship conflicts. |
| evidence_quality | 0.32 | Parent-candidate evidence is separate and QA-sensitive. |
| conversion_confidence | 0.36 | Current page and parent clusters both require review. |
| claim_probability | 0.03 | No specific Jose/Juana parent claim is supported. |
| relevance | 0.70 | Relevant because parents are mentioned generically. |
| canonical_readiness | 0.00 | No relationship promotion supported. |

## Ranked Hypotheses

| rank | hypothesis | probability | disposition |
|---:|---|---:|---|
| 1 | Page-reference and conversion QA blocker | 0.90 | Hold; reconcile page 11 versus page 14 and locate image. |
| 2 | Narrow held candidate `Dr Dario Pulgar A.` | 0.78 | Preserve literal reading; do not expand. |
| 3 | Same older medical person as other `Dario Pulgar A.` / adult `Dario Pulgar` clusters | 0.48 | Possible only; requires explicit bridge. |
| 4 | Same as `Dario Jose Pulgar-Arriagada` / `Dario J. Pulgar Arriagada` | 0.28 | Preserve as unresolved; do not merge by initial. |
| 5 | Same as canonical `Darío Pulgar Arriagada` | 0.10 | Low; do not attach without vital/property bridge. |
| 6 | Same as `Dario Arturo Pulgar` / `Dario Arturo Pulgar-Smith` | 0.08 | Low; require proof-reviewed CV/Pulgar-Smith bridge. |
| 7 | Jose/Juana candidates are Dario's parents | 0.03 | Unsupported; require a source naming parents. |

## Conflict Summary

- Same-person evidence is unresolved.
- Duplicate-person risk is high if this record is merged by name alone with `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, adult/child `Dario Pulgar` passenger clusters, or Jose/Juana line candidates.
- Name-variant evidence supports only the literal forms `DR DARIO PULGAR A,` and `DR. DARIO PULGARA` until image reread.
- Relationship-conflict evidence is limited to unnamed parents; no Jose/Juana parent claim is supported.
- Chronology evidence favors treating this as an older physician/property-owner candidate, but that is only context, not proof.

## Recommended Next Action

Keep the staged draft on hold as a conversion QA and identity-bridge caution. The exact next proof-review step is page-image/provenance QA for `CHUNK-e756c7880c5d-P0011-01`: reconcile why the assigned page-11 chunk/source packet points to the page-14 Fundo Los Cuartos article, locate or regenerate the relevant page image, and reread the typed line and handwritten signature.

After that, run a targeted identity proof review against older medical `Dario Pulgar A.` evidence first, then separately compare `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, adult/child passenger clusters, and Jose/Juana parent candidates. Do not promote, merge, rename, or attach named parents from this draft alone.
