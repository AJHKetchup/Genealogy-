---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict.md
worker: postconv-identity-analysis-20260530211411979
staged_draft: research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict.md
source: raw/sources/CV of Dario Arturo Pulgar.pdf
source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-work-history.md
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
conversion_job_page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
chunk_id: CHUNK-fb0a0000636f-P0005-01
page_reference: page 5
analysis_status: hold
canonical_readiness: not_ready
---

# Identity/Conflict Analysis: CHUNK-fb0a0000636f-P0005-01

## Blockers

- Page-control blocker: the staged draft reports that the referenced chunk and staged source packet support 1979-1970 work-history entries, while the conversion job page Markdown for the same page 5 supports 1999/1998 entries. These are competing derivative transcriptions, not a name variant or family-history disagreement.
- Conversion-output blocker: the aggregate converted file contains both the 1999/1998 page-5 text and the later 1979-1970 text in the same converted-file context. The source packet also reports duplicate page-5 chunk manifest records with differing char counts and hashes.
- Promotion blocker: no occupational claim from either derivative text is ready for canonical use until conversion QA identifies the controlling page-5 transcription against the authoritative page image or source PDF page.
- Identity blocker: neither competing page-5 body repeats `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, any Jose parent candidate, or any Juana parent candidate. Page-level subject attribution is document-level only.
- Relationship blocker: the staged page has no birth, death, parent, spouse, child, sibling, grandchild, household, or other kinship evidence. It cannot resolve Jose/Juana parent candidates or any Pulgar-line relationship conflict.
- Canonical blocker: this staged draft does not prove that document-level `Dario Arturo Pulgar` is the same person as canonical `Dario Arturo Pulgar-Smith` or any Pulgar-Arriagada candidate.
- Scope blocker: this note does not edit raw sources, converted Markdown, chunks, source packets, claims, or canonical wiki pages.

## Evidence Reviewed

Literal source/control readings:

- Staged draft: `research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict.md`.
- Source packet: `research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-work-history.md`.
- Referenced chunk: `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md`.
- Aggregate converted file: `raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md`.
- Conversion job page Markdown: `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md`.
- Conversion job manifest: `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/manifest.json`.
- Existing canonical context: `wiki/people/dario-arturo-pulgar-smith.md`, `wiki/people/dar-o-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/juana-arriagada-de-pulgar.md`, and `wiki/people/juana-de-dios-amagada-de-pulgar.md`.

Interpretive boundary: no external research was performed. Literal readings below are kept separate from identity interpretation.

## Hypothesis 1: Page 5 Controls To The 1999/1998 Page-Markdown Text

Interpretation: the conversion job page Markdown may be the controlling page-5 transcription, and the 1979-1970 chunk/source-packet text may be stale, duplicated, or assigned to another page.

Supporting evidence:

- `page-markdown/page-0005.md` labels itself as page 5 and transcribes `1999`, `1998 - 1999`, and `1997-1998` professional entries.
- The conversion job manifest maps page 5 to `page-images/page-0005.jpg` and `page-markdown/page-0005.md`.
- The staged draft correctly treats this as a derivative transcription/provenance conflict.

Conflicts:

- The assigned chunk `CHUNK-fb0a0000636f-P0005-01` and staged source packet quote 1979-1970 entries instead.
- This hypothesis addresses page control only; it does not create a page-local identity bridge to any canonical person.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.55 | Document title supports Dario Arturo Pulgar, but page 5 body is unnamed. |
| conflict_severity | 0.88 | Wrong page control would misplace several work-history claims. |
| evidence_quality | 0.64 | Page Markdown and manifest align, but assigned chunk/source packet disagree. |
| conversion_confidence | 0.38 | Readable derivative text exists, but control is unresolved. |
| claim_probability | 0.52 | Plausible controlling text, not promotion-ready. |
| relevance | 0.95 | Directly addresses the staged conflict. |
| canonical_readiness | 0.05 | Not ready for canonical use. |

## Hypothesis 2: Page 5 Controls To The 1979-1970 Chunk/Source-Packet Text

Interpretation: the referenced chunk and source packet may be the intended page-5 evidence, and the page-markdown file may be the conflicting derivative.

Supporting evidence:

- The chunk front matter is labeled `CHUNK-fb0a0000636f-P0005-01`, with `page_start: 5` and `page_end: 5`.
- The chunk transcribes 1979-1982 HABITAT, 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, and 1970-1972 CITELCO entries.
- The staged source packet quotes the same 1979-1970 sequence and identifies the source identity as `Dario Arturo Pulgar` from the CV title.
- The aggregate converted file also contains the 1979-1970 sequence elsewhere in the broader output.

Conflicts:

- `page-markdown/page-0005.md` transcribes materially different 1999/1998 content for the same page number.
- The source packet itself marks conversion confidence as blocked and requires conversion QA before promotion.
- If the page-markdown and job manifest control page 5, this 1979-1970 text may belong to another page or stale derivative state.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.57 | Document-level source title supports the subject, but page body is unnamed. |
| conflict_severity | 0.88 | A stale or misassigned chunk would create false page-level chronology. |
| evidence_quality | 0.58 | Chunk and packet agree internally but conflict with page Markdown. |
| conversion_confidence | 0.35 | Page-control uncertainty remains severe. |
| claim_probability | 0.48 | Possible, but blocked by contrary derivative evidence. |
| relevance | 0.95 | Directly addresses the assigned chunk and packet. |
| canonical_readiness | 0.05 | Not ready for canonical use. |

## Hypothesis 3: Document-Level Subject Is Dario Arturo Pulgar

Interpretation: whichever page-5 transcription controls, the broader local document is a CV titled for `Dario Arturo Pulgar`.

Supporting evidence:

- The source path is `raw/sources/CV of Dario Arturo Pulgar.pdf`.
- The conversion job title is `CV of Dario Arturo Pulgar pages 4-9`.
- The source packet states that source identity is `Dario Arturo Pulgar`, identified by source title, while warning that page 5 itself does not repeat the name.

Conflicts:

- The page body does not independently name the subject.
- CV pages are professional/occupational evidence, not direct family evidence.
- Page-control QA must precede any claim promotion from this staged draft.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.66 | Consistent document metadata supports the subject at document level. |
| conflict_severity | 0.55 | Identity label is plausible, but page control blocks claim use. |
| evidence_quality | 0.62 | Metadata and packet agree; page-local identity evidence is absent. |
| conversion_confidence | 0.36 | The assigned page remains unresolved. |
| claim_probability | 0.65 | Probable only as document-level attribution. |
| relevance | 0.90 | Needed for downstream CV handling. |
| canonical_readiness | 0.12 | Hold for page-control and identity-bridge review. |

## Hypothesis 4: Dario Arturo Pulgar Is A Variant Of Dario Arturo Pulgar-Smith

Interpretation: `Dario Arturo Pulgar` in the CV may be a shortened or partial form of canonical `Dario Arturo Pulgar-Smith`, but this staged page does not prove it.

Supporting evidence:

- Canonical `wiki/people/dario-arturo-pulgar-smith.md` records the family-supplied name `Dario Arturo Pulgar-Smith`.
- The CV title shares the distinctive `Dario Arturo Pulgar` elements.
- The canonical page warns that records mentioning Dario, Pulgar, Pulgar-Arriagada, or Pulgar-Smith require identity review before attachment.

Conflicts:

- Page 5 does not state `Smith` or `Pulgar-Smith`.
- Page 5 does not state a relationship to Alexander John Heinz.
- Page 5 does not give a birth, death, spouse, child, parent, address, or other bridge to the canonical profile.
- The derivative page-control conflict must be resolved before occupational details can be weighed.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.45 | Plausible name overlap only. |
| conflict_severity | 0.64 | Premature attachment could misattribute work history. |
| evidence_quality | 0.35 | Evidence is contextual, not direct. |
| conversion_confidence | 0.36 | Page control remains unresolved. |
| claim_probability | 0.40 | Possible, not proved. |
| relevance | 0.84 | Relevant to downstream canonical attachment. |
| canonical_readiness | 0.05 | Not ready for attachment or merge. |

## Hypothesis 5: Pulgar-Line Candidates Remain Separate Or Unresolved

Interpretation: for this staged draft, `Dario Arturo Pulgar-Smith`, document-level `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, and Jose/Juana parent candidates must remain separate or unresolved.

Supporting evidence:

- `Dario Arturo Pulgar-Smith` is family-supplied as Alexander John Heinz's maternal grandfather and explicitly guarded against automatic merge with similar names.
- Canonical `Dario Pulgar Arriagada` is a separate stub with a promoted evidence snapshot tied to a 2000 expropriation resolution, not this CV page.
- Canonical `Jose del Carmen Segundo Pulgar Arriagada` is a separate birth-registration person with a probable mother link to `Juana Arriagada de Pulgar`.
- Canonical `Jose del Carmen Pulgar` and `Juana de Dios Amagada de Pulgar` appear in a different parent cluster for Tulio Cesar Luis Jose.
- This page-control conflict names none of the Jose/Juana candidates and provides no parent, child, spouse, grandchild, or household evidence.

Conflicts:

- Same-person and duplicate-person risks remain high if `Dario Pulgar` names are merged by name alone.
- Relationship conflicts cannot be resolved from this page because it has no relationship evidence.
- Chronology evidence cannot be used as identity separation while page control is unresolved.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.78 | Strong confidence that no merge is supported from this draft. |
| conflict_severity | 0.72 | Mistaken merges would affect multiple Pulgar-line clusters. |
| evidence_quality | 0.60 | Canonical context supports caution; assigned page gives no family evidence. |
| conversion_confidence | 0.36 | Conversion blocker still applies to any CV claim. |
| claim_probability | 0.82 | Current correct action is to preserve separate hypotheses. |
| relevance | 0.90 | Directly satisfies Pulgar-line comparison requirements. |
| canonical_readiness | 0.10 | Ready only as a hold/review recommendation. |

## Ranked Identity/Conflict Assessment

1. Preserve the page-control conflict as a conversion/provenance blocker, not a genealogical fact conflict.
2. Treat `Dario Arturo Pulgar` only as a document-level CV subject until page control and identity bridge are reviewed.
3. Do not attach this page to canonical `Dario Arturo Pulgar-Smith` yet.
4. Do not merge or normalize `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, `Jose del Carmen Segundo Pulgar Arriagada`, `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, or `Juana de Dios Amagada de Pulgar`.

## Conflict Summary

- Same-person evidence: insufficient for canonical attachment to `Dario Arturo Pulgar-Smith`.
- Duplicate-person evidence: unresolved; name overlap alone is not enough.
- Name-variant evidence: `Dario Arturo Pulgar` may be a partial form of `Dario Arturo Pulgar-Smith`, but this page does not prove the variant.
- Relationship-conflict evidence: none in the assigned page-5 evidence.
- Chronology-conflict evidence: procedural only. The 1999/1998 and 1979-1970 entries may both belong in the CV chronology, but they cannot both be accepted as the same page-5 transcription.
- Conversion conflict: severe and controlling for this staged draft.

## Recommended Next Action

Hold this staged draft for source-prep/conversion QA. The exact next proof-review or promotion prerequisite is:

1. Compare page 5 against the authoritative rendered page image or source PDF page.
2. Decide whether `page-markdown/page-0005.md` with 1999/1998 entries or `page-0005-chunk-01.md` with 1979-1970 entries controls page 5.
3. Repair or regenerate stale derivative outputs through the existing conversion-QA/source-prep workflow if needed.
4. Rerun proof review only after page control is certified.
5. Run a separate identity-bridge review before attaching any surviving CV claims to canonical `Dario Arturo Pulgar-Smith` or merging any Pulgar-line candidates.

Current promotion decision: `do_not_promote`.
