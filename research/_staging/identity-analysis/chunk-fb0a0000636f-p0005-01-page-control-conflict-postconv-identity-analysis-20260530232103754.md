---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260530224457988.md
worker: postconv-identity-analysis-20260530232103754
staged_draft: research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260530224457988.md
source_path: raw/sources/CV of Dario Arturo Pulgar.pdf
source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-hold-postconv-evidence-extraction-20260530224457988.md
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
chunk_id: CHUNK-fb0a0000636f-P0005-01
page_reference: page 5
analysis_status: hold
canonical_readiness: hold_for_conversion_qa
---

# Identity/Conflict Analysis: Page 5 Derivative Texts Disagree

## Blockers

- The exact staged draft analyzed here is `research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260530224457988.md`.
- This is primarily a page-control/conversion conflict, not a resolved same-person or relationship conflict. The assigned chunk and conversion-job page Markdown give materially different page-5 work histories.
- The assigned chunk reads page 5 as a 1979-1970 sequence beginning with HABITAT/Nairobi and ending at `EDUCATION`.
- The conversion-job `page-markdown/page-0005.md` reads page 5 as a 1999-1997 sequence beginning with PROFONANPE/Peru and ending mid-sentence in an SNC Lavalin Agriculture entry.
- The chunk manifest duplicates `CHUNK-fb0a0000636f-P0005-01` with different character counts and hashes. The source packet also records a mismatch between the chunk's recorded converted hash and the observed converted-file hash.
- The job manifest lists `page-images/page-0005.jpg`, but that file is absent in this checkout. I did not rerun conversion or edit conversion outputs.
- Page 5 itself does not independently print `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, parents, spouse, child, or relationship to Alexander John Heinz.

## Hypothesis 1: Hold All Page-5 Claims Until Conversion QA Selects The Controlling Text

Hypothesis: The two derivative page-5 transcriptions cannot both control the same physical page, so identity and chronology claims from page 5 must remain staged until conversion QA certifies the correct page text.

Literal evidence:

- The staged conflict draft states that the assigned chunk supports a 1979-1982 HABITAT sequence, while competing page Markdown supports a 1999 PROFONANPE sequence.
- The source packet records the same contradiction and says the manifest duplicates the chunk id with conflicting counts and hashes.
- The chunk file literally contains 1979-1982 HABITAT, 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, 1970-1972 CITELCO, and `EDUCATION`.
- The job page Markdown literally contains 1999 PROFONANPE, Television Trust for the Environment, 1998-1999 Arca Consulting/European Commission, 1997-1998 Klohn Crippen Consultants, and SNC Lavalin Agriculture.

Interpretation:

- This is the controlling issue. The conflict affects occupational chronology, places, role titles, and any later identity-bridge comparison that relies on a page-5 work history.
- Neither page-5 work-history sequence should be promoted or used to distinguish identities until a restored page image/PDF QA review selects one transcription and repairs the manifest/hash drift.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.55 | The source is titled for Dario Arturo Pulgar, but the disputed page text itself is not identity-bearing. |
| conflict_severity | 0.92 | The competing derivative texts describe different years, employers, places, and page endings. |
| evidence_quality | 0.46 | Local derivative evidence is explicit but internally inconsistent; physical page control is unavailable here. |
| conversion_confidence | 0.18 | Page image is absent and manifest/hash drift is documented. |
| claim_probability | 0.50 | One sequence may be correct, but this pass cannot choose which. |
| relevance | 1.00 | Directly controls the assigned staged conflict draft. |
| canonical_readiness | 0.03 | Not ready for canonical promotion or person attachment. |

## Hypothesis 2: The Page Belongs To Document-Level CV Subject Dario Arturo Pulgar

Hypothesis: Whichever page-5 transcription ultimately controls, it belongs to the CV source locally identified as `CV of Dario Arturo Pulgar`.

Literal evidence:

- The source path, source packet, converted file title, and job manifest all identify the source as `CV of Dario Arturo Pulgar.pdf` or `CV of Dario Arturo Pulgar pages 4-9`.
- The source packet states that `Dario Arturo Pulgar` is named in the source title and CV context, while the assigned page-5 chunk body does not independently restate the full name.
- The competing page-5 text likewise does not print the subject's full name in the page body.

Interpretation:

- Document-level attribution to `Dario Arturo Pulgar` is plausible, but page 5 is not an identity-bearing page.
- Conversion QA must precede proof review of any page-5 occupational facts. A separate identity-bridge proof review is still required before attaching the CV subject to a canonical person page.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.72 | Source-level context consistently names Dario Arturo Pulgar, but page 5 itself is unnamed. |
| conflict_severity | 0.62 | The identity label is less disputed than the page text, but page-control failure blocks use of claims. |
| evidence_quality | 0.58 | Source metadata and staged packet align; page-body identity evidence is absent. |
| conversion_confidence | 0.18 | Page-control conflict remains unresolved. |
| claim_probability | 0.70 | Probable as a document-level attribution only. |
| relevance | 0.96 | Necessary for later CV-subject proof review. |
| canonical_readiness | 0.12 | Hold for conversion QA and identity bridge. |

## Hypothesis 3: Same Person As Canonical Dario Arturo Pulgar-Smith

Hypothesis: The CV subject `Dario Arturo Pulgar` is the same person as canonical `wiki/people/dario-arturo-pulgar-smith.md`, with the CV using a shortened surname form.

Literal evidence:

- The canonical page's preferred name is `Dario Arturo Pulgar-Smith`, based on family-supplied knowledge.
- The canonical page states that Dario Arturo Pulgar-Smith is Alexander John Heinz's maternal grandfather.
- The name elements `Dario Arturo` and `Pulgar` align with the CV source title.
- The staged conflict draft and both page-5 derivative texts do not state `Pulgar-Smith`, `Smith`, a family relationship, or Alexander John Heinz.
- The canonical page warns that records mentioning Dario, Pulgar, Pulgar-Arriagada, or Pulgar-Smith should be attached only after identity review.

Interpretation:

- Same-person identity is plausible but not proven by this conflict draft. Family context justifies a targeted double-check, not silent normalization from `Dario Arturo Pulgar` to `Dario Arturo Pulgar-Smith`.
- This hypothesis cannot advance while page-5 control is blocked, because the page's occupational sequence itself is uncertain.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.60 | Strong name overlap, but no direct `Pulgar-Smith` bridge in this evidence. |
| conflict_severity | 0.48 | Incorrect attachment would misattribute whichever disputed page-5 work sequence is later selected. |
| evidence_quality | 0.50 | Evidence is source-title name overlap plus family-supplied canonical context. |
| conversion_confidence | 0.18 | Conversion conflict blocks page-5 claim use. |
| claim_probability | 0.58 | Plausible but unproved here. |
| relevance | 0.92 | Important nominated canonical candidate. |
| canonical_readiness | 0.06 | No merge, rename, or fact promotion. |

## Hypothesis 4: Same Person As Dario Jose Pulgar-Arriagada Or Dario/Dario Pulgar Arriagada

Hypothesis: The CV subject is the same person as `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, or related Pulgar-Arriagada clusters.

Literal evidence:

- Existing canonical context includes `wiki/people/dar-o-pulgar-arriagada.md`, a stub with an auto-generated 5 December 2000 expropriation-event claim for `Darío Pulgar Arriagada`.
- Existing staged Pulgar-line context elsewhere preserves `Dario Jose Pulgar-Arriagada`, `Dario Pulgar A.`, and Pulgar-Arriagada comparisons as unresolved or held where identity-bearing evidence is limited.
- This staged conflict draft and both derivative page-5 texts do not contain `Jose`, `Arriagada`, `Pulgar A.`, a 1929 Geneva context, a medical/surgeon role, or a parent/child bridge.

Interpretation:

- Name overlap alone is insufficient. This page-control conflict should not merge the CV subject with Pulgar-Arriagada clusters.
- If page-5 work history is later certified, it may become useful chronology context, but only after a separate anti-conflation proof review compares full names, dates, occupations, and relationships.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.12 | Only broad Dario/Pulgar overlap is present in this staged draft. |
| conflict_severity | 0.78 | Name-only merger could collapse distinct surname lines or generations. |
| evidence_quality | 0.42 | Comparison context is sparse and partly held outside this page. |
| conversion_confidence | 0.18 | Page-control conflict prevents chronology use. |
| claim_probability | 0.10 | Low probability from this evidence alone. |
| relevance | 0.82 | Required Pulgar-line anti-conflation comparison. |
| canonical_readiness | 0.02 | Do not attach or merge. |

## Hypothesis 5: Relationship To Jose/Juana Parent Candidates

Hypothesis: Jose del Carmen Pulgar, Jose del Carmen Segundo Pulgar Arriagada, Juana Arriagada de Pulgar, or Juana de Dios Amagada/de Pulgar may connect to the broader Pulgar line, but this page-control conflict does not connect them to the CV subject.

Literal evidence:

- Existing canonical pages include `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.
- Existing staged register notes preserve image-sensitive Jose/Juana readings and unresolved parent-name/surname details.
- This staged conflict draft and both derivative page-5 texts contain no Jose or Juana name and no parent, spouse, child, household, or birth-register statement.

Interpretation:

- Jose/Juana names are only an anti-conflation checklist for this task. The page-control conflict provides no relationship evidence.
- Do not infer ancestry or parentage from Pulgar surname context.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.05 | No direct identity or kinship evidence appears. |
| conflict_severity | 0.60 | Unsupported lineage attachment would create false relationships. |
| evidence_quality | 0.36 | Related parent-candidate evidence is outside this page and partly unresolved. |
| conversion_confidence | 0.18 | Page-control conflict does not help relationship evidence. |
| claim_probability | 0.04 | This evidence does not support a Jose/Juana relationship claim. |
| relevance | 0.58 | Relevant only as required Pulgar-line comparison context. |
| canonical_readiness | 0.01 | No relationship action supported. |

## Conflicts

- Page-control conflict: assigned chunk and conversion-job page Markdown are materially incompatible for page 5.
- Chronology conflict: 1979-1970 work history conflicts with 1999-1997 work history for the same page reference.
- Same-person conflict: unresolved between document-level `Dario Arturo Pulgar` and canonical `Dario Arturo Pulgar-Smith`.
- Duplicate-person risk: moderate for CV `Dario Arturo Pulgar` versus canonical `Dario Arturo Pulgar-Smith`; high if merged by name alone with `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, or Jose/Juana parent clusters.
- Name-variant conflict: this evidence does not resolve `Pulgar` versus `Pulgar-Smith`, `Pulgar-Arriagada`, or `Pulgar Arriagada`.
- Relationship-conflict evidence: none on this page. No parent, spouse, child, grandchild, or relationship to Alexander John Heinz is stated.

## Ranked Hypotheses

| rank | hypothesis | probability | action |
|---:|---|---:|---|
| 1 | Page-5 claims must be held until conversion QA selects the controlling derivative text | 0.92 | Restore/check page image or PDF page, choose controlling transcription, repair manifest/hash drift. |
| 2 | The certified page belongs to document-level CV subject `Dario Arturo Pulgar` | 0.70 | Treat only as document-level CV attribution after conversion QA. |
| 3 | Same person as canonical `Dario Arturo Pulgar-Smith` | 0.58 | Require explicit identity-bridge proof review before canonical attachment. |
| 4 | Same person as `Dario Jose Pulgar-Arriagada` or `Dario/Darío Pulgar Arriagada` | 0.10 | Preserve separately/unresolved; do not merge by name alone. |
| 5 | Connected to Jose/Juana parent candidates | 0.04 | No action from this page; revisit only if lineage evidence appears. |

## Recommended Next Action

Keep `research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260530224457988.md` on `hold_for_conversion_qa`. Do not promote either page-5 work-history sequence, merge people, rename canonical pages, or attach page-5 facts to `wiki/people/dario-arturo-pulgar-smith.md`.

The exact next proof-review step is conversion QA first: restore or recheck `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0005.jpg` or the physical PDF page; decide whether the controlling page-5 text is the 1979-1970 assigned chunk or the 1999-1997 page Markdown; and repair the duplicate manifest/hash drift. After that, run a separate identity-bridge proof review to decide whether document-level `Dario Arturo Pulgar` is the same person as canonical `Dario Arturo Pulgar-Smith`, while explicitly anti-conflating `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, and the Jose/Juana parent candidates.
