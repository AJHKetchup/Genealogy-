---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/conflicts/conflict-stage-chunk-3f469b56e502-p0005-01-handwritten-file-number.md
worker: postconv-identity-analysis-20260523100556384
staged_draft: research/_staging/conflicts/conflict-stage-chunk-3f469b56e502-p0005-01-handwritten-file-number.md
source_path: raw/sources/R3578-50-5569-5569-Jacket5.pdf
source_packet: research/_staging/source-packets/sp-stage-chunk-3f469b56e502-p0005-01-treaty-series-846-cover.md
converted_file: raw/converted/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25.codex.md
chunk: raw/chunks/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25-codex/page-0005-chunk-01.md
chunk_id: CHUNK-3f469b56e502-P0005-01
page_reference: page 5
analysis_status: conversion_metadata_conflict_only
canonical_readiness: do_not_promote
---

# Identity/Conflict Analysis: CHUNK-3f469b56e502-P0005-01

## Blockers

- The exact staged draft reviewed here is `research/_staging/conflicts/conflict-stage-chunk-3f469b56e502-p0005-01-handwritten-file-number.md`.
- The live conflict is a conversion/source-metadata QA issue: the converted page reads the top-center handwritten number as `50 /5509/5509`, while proof review says that exact reading is not clearly supported and the final group may be closer to a `5569`-like value.
- Adjacent source metadata and the raw source filename use `50 5569 5569`, but that context cannot silently correct the literal page reading.
- Page 5 is a government publication cover for Treaty Series No. 846, not a genealogical record. It names no family-tree person and states no kinship, vital event, household, residence, occupation, or chronology for a genealogical subject.
- The staged identity note for this page is negative evidence: `research/_staging/identity/id-stage-chunk-3f469b56e502-p0005-01-no-person-identity.md`.
- No external research was performed. No raw sources, converted Markdown, chunks, or canonical wiki pages were edited.
- The named `$genealogy-proof-review` skill file was not available in the session skill list; this note applies the evidence-contract requirements from the dispatch: literal support separated from interpretation, multiple hypotheses preserved, scored confidence, and no promotion without proof-review resolution.

## Hypothesis 1: The Conflict Is Only A Handwritten Source-Identifier QA Conflict

Hypothesis: the staged draft correctly identifies a conversion/source-metadata conflict about the handwritten file number, not an identity, duplicate-person, relationship, or chronology conflict.

Literal evidence:

- The staged conflict draft quotes the current conversion text as `[Handwritten at top center]` followed by `50 /5509/5509`.
- The staged conflict draft states that proof review did not clearly support that exact reading and that the final group may look closer to a `5569`-like value.
- The source packet repeats the same QA concern and marks reading confidence low for the exact handwritten top-center identifier.
- The raw source path and converted filename contain `R3578-50-5569-5569-Jacket5.pdf`, giving adjacent source-metadata context for `50 5569 5569`.
- The assigned chunk transcribes the page as a printed cover for `TREATY SERIES, No. 846` and a `PRISONERS OF WAR` convention, with the same handwritten number at top center.

Interpretation:

- The strongest conclusion is that this is an administrative identifier conflict that should be routed to conversion QA.
- The exact number should remain unresolved until the page image is reread, preferably as a targeted crop of the top-center handwriting.
- The filename and nearby metadata support a double-check for `5569`, but they are not a substitute for literal image review.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.01 | No genealogical identity is asserted or implied by the handwritten number. |
| conflict_severity | 0.38 | Moderate for source citation metadata, minimal for person identity or relationships. |
| evidence_quality | 0.70 | The staged draft, source packet, chunk, and filenames clearly define the disagreement. |
| conversion_confidence | 0.35 | Printed page text is strong, but the exact handwritten identifier is explicitly low-confidence. |
| claim_probability | 0.82 | High probability that a real transcription conflict exists; lower probability for either exact numeric reading until image QA. |
| relevance | 0.28 | Relevant to source identification and citation hygiene, not to genealogy identity resolution. |
| canonical_readiness | 0.05 | Do not promote the exact handwritten number until conversion QA resolves it. |

## Hypothesis 2: The Page Supplies A Genealogical Person Identity

Hypothesis: page 5 supplies a same-person, duplicate-person, name-variant, relationship, or chronology claim for a genealogical subject.

Literal evidence:

- The page text identifies `TREATY SERIES, No. 846`, `PRISONERS OF WAR`, `CONVENTION BETWEEN THE UNITED STATES OF AMERICA AND OTHER POWERS`, signing and ratification/proclamation dates, and a `RECEIVED IN REGISTRY 19 NOV 1932` stamp.
- The staged source packet states that no direct genealogical person, family unit, or vital event is identified on this page.
- The staged negative identity candidate states that no genealogical person is named or identified in the assigned chunk.

Interpretation:

- This hypothesis is not supported by the assigned evidence.
- The page is useful as source-context evidence only. It should not create or update a person, relationship, or family chronology claim.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.00 | No person identity appears in the page evidence. |
| conflict_severity | 0.02 | No same-person, duplicate-person, relationship, or chronology conflict exists. |
| evidence_quality | 0.80 | Multiple local staging layers agree that the page is administrative/source context. |
| conversion_confidence | 0.86 | Printed title and dates are readable and not material to a person identity. |
| claim_probability | 0.01 | Very low probability that this page supports a genealogy identity claim. |
| relevance | 0.10 | Relevant only as a negative check. |
| canonical_readiness | 0.00 | Do not promote to canonical person or relationship pages. |

## Hypothesis 3: Metadata Reading `50 5569 5569` Should Replace The Converted `50 /5509/5509`

Hypothesis: adjacent metadata and the filename are enough to normalize the page's top-center handwritten number to `50 5569 5569`.

Literal evidence:

- The raw source filename is `R3578-50-5569-5569-Jacket5.pdf`.
- The converted document title and other nearby metadata include `50-5569-5569`.
- The staged conflict draft says the page image does not clearly support the converted `50 /5509/5509` and that the final group may look closer to a `5569`-like value.

Interpretation:

- `50 5569 5569` is the leading contextual hypothesis for the source identifier, but it is not yet a proof-reviewed literal reading for page 5.
- The correct action is to preserve both readings until targeted conversion QA confirms the image.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.00 | This is a source number, not a person identity. |
| conflict_severity | 0.36 | A wrong file number can affect citation control, but not family-tree identity directly. |
| evidence_quality | 0.62 | Filename and nearby metadata are useful contextual evidence, but not direct image transcription. |
| conversion_confidence | 0.42 | Conversion is low for the exact handwritten number. |
| claim_probability | 0.64 | `50 5569 5569` is plausible from metadata context, pending image reread. |
| relevance | 0.30 | Relevant to source packet metadata and citation alignment. |
| canonical_readiness | 0.08 | Hold until image-reviewed QA settles the literal reading. |

## Pulgar-Line Anti-Conflation Check

The staged draft, source packet, assigned chunk, and negative identity candidate do not mention Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario/Dario Pulgar Arriagada, Jose del Carmen Pulgar, Jose del Carmen Segundo Pulgar Arriagada, Juana Arriagada de Pulgar, or Juana de Dios Amagada de Pulgar.

Existing wiki context remains separate:

- `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied as Alexander John Heinz's maternal grandfather and warns not to merge similarly named Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records without identity review.
- `wiki/people/dar-o-pulgar-arriagada.md` records a separate evidence snapshot for `Darío Pulgar Arriagada` in a 2000 expropriation context.
- `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` records reviewed but still qualified birth-register evidence and a probable low-confidence mother link to Juana Arriagada de Pulgar.

Ranked Pulgar hypotheses for this staged draft:

| rank | hypothesis | probability | action |
|---:|---|---:|---|
| 1 | The Treaty Series cover is unrelated to all Pulgar-line identity clusters. | 0.99 | No Pulgar merge, attachment, rename, or promotion from this draft. |
| 2 | The file identifier indirectly supplies context for Dario Arturo Pulgar-Smith or Dario Arturo Pulgar. | 0.01 | Reject unless a later reviewed local source explicitly links this League file to that person. |
| 3 | The file identifier supplies evidence for Dario Jose Pulgar-Arriagada or Dario/Dario Pulgar Arriagada. | 0.01 | Reject for this draft; maintain those as separate Pulgar-Arriagada proof-review contexts. |
| 4 | The page supplies evidence for Jose/Juana parent candidates. | 0.00 | Reject; no Jose/Juana names, parentage, or household evidence appears here. |

Exact next Pulgar proof-review step needed next: none for this staged draft. Pulgar-line work should continue only in the separate staged drafts, reviewed notes, and canonical candidates that actually name Pulgar, Jose, or Juana persons.

## Conflicts

- Same-person conflict: none.
- Duplicate-person conflict: none.
- Name-variant conflict: none.
- Relationship conflict: none.
- Chronology conflict: none for genealogical persons.
- Conversion/source-metadata conflict: unresolved top-center handwritten file number, with current conversion `50 /5509/5509` versus contextual metadata `50 5569 5569` and proof-review concern that the final group may look closer to `5569`.

## Recommended Next Action

Keep this staged conflict on `hold_for_conversion_qa`. The next proof-review step is a targeted image reread of the top-center handwritten file number on page 5, ideally documenting whether the literal reading is `50 /5509/5509`, `50 /5569/5569`, `50 5569 5569`, or another uncertain form. Do not promote the exact handwritten number to canonical source metadata until that QA step is complete. Do not create, merge, rename, or attach any person or relationship claim from this page.
