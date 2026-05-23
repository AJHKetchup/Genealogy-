---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/conflicts/conflict-stage-chunk-3f469b56e502-p0005-01-source-metadata-qa.md
worker: postconv-identity-analysis-20260523100814079
staged_draft: research/_staging/conflicts/conflict-stage-chunk-3f469b56e502-p0005-01-source-metadata-qa.md
source_path: raw/sources/R3578-50-5569-5569-Jacket5.pdf
source_packet: research/_staging/source-packets/sp-stage-chunk-3f469b56e502-p0005-01-treaty-series-846-cover.md
converted_file: raw/converted/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25.codex.md
chunk: raw/chunks/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25-codex/page-0005-chunk-01.md
chunk_id: CHUNK-3f469b56e502-P0005-01
page_reference: page 5
analysis_status: source_metadata_conflict_only
canonical_readiness: do_not_promote
---

# Identity/Conflict Analysis: CHUNK-3f469b56e502-P0005-01

## Blockers

- Exact staged draft reviewed: `research/_staging/conflicts/conflict-stage-chunk-3f469b56e502-p0005-01-source-metadata-qa.md`.
- The live issue is source-metadata/conversion QA, not a same-person, duplicate-person, name-variant, relationship, or chronology conflict.
- Literal conversion reads the top-center handwritten number as `50 /5509/5509`, but the staged draft and source packet say proof review did not clearly confirm that exact reading and adjacent jacket metadata uses `50 5569 5569`.
- The filename and adjacent metadata can justify a double-check for `5569`; they cannot silently replace the literal page reading.
- Page 5 names no genealogical person and states no kinship, residence, occupation, vital event, household membership, or family chronology.
- No external research was performed. No raw sources, converted Markdown, chunks, or canonical wiki pages were edited.
- The named `$genealogy-proof-review` skill file was not available in the session skill list; this note follows the dispatched proof-review contract by separating literal readings from interpretation, preserving hypotheses, scoring evidence, and withholding promotion.

## Hypothesis 1: Source-Metadata QA Conflict Only

Hypothesis: the staged draft correctly identifies a source identifier transcription conflict, not a genealogical identity conflict.

Literal evidence:

- The staged draft reports the converted top-center handwriting as `50 /5509/5509`.
- The staged draft says proof review did not clearly support that exact reading and that adjacent jacket metadata uses `50 5569 5569`.
- The source packet marks reading confidence high for printed title/date text but low for the exact handwritten top-center identifier.
- The assigned chunk transcribes the page as a government publication cover headed `TREATY SERIES, No. 846` and `PRISONERS OF WAR`, with registry receipt date `19 NOV 1932`.
- The related staged claim says only that a top-center handwritten file number is present and that the exact reading remains unresolved.

Interpretation:

- This is the strongest hypothesis. The current evidence supports a real administrative-number conflict but does not resolve the number.
- `50 5569 5569` is the leading contextual reading because the raw source path is `R3578-50-5569-5569-Jacket5.pdf`, but it still needs targeted image reread before use as canonical metadata.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.01 | The evidence identifies a source page, not a person. |
| conflict_severity | 0.36 | Moderate for citation/source control; negligible for genealogy identity. |
| evidence_quality | 0.72 | Staged draft, source packet, chunk, and claim all define the same unresolved identifier. |
| conversion_confidence | 0.35 | Printed text is high-confidence, but the exact handwritten number is explicitly low-confidence. |
| claim_probability | 0.84 | High probability that a metadata transcription conflict exists; exact value remains unsettled. |
| relevance | 0.28 | Relevant to source metadata hygiene, not to family reconstruction. |
| canonical_readiness | 0.05 | Do not promote the exact handwritten number until conversion QA resolves it. |

## Hypothesis 2: Converted Reading `50 /5509/5509` Is Correct

Hypothesis: the current converted text accurately transcribes the top-center handwritten number.

Literal evidence:

- The assigned chunk and converted derivative read `[Handwritten at top center]` followed by `50 /5509/5509`.
- The same reading is preserved in the source packet as the current conversion layer.

Interpretation:

- This remains possible but is not the leading conclusion because the staged draft records proof-review doubt and nearby metadata points toward `5569`.
- The converted reading should be preserved as an evidence layer, not promoted as settled.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.00 | No person identity is involved. |
| conflict_severity | 0.34 | A wrong file identifier could affect citation precision. |
| evidence_quality | 0.46 | The reading exists in conversion output but is directly challenged by review. |
| conversion_confidence | 0.30 | Low for this handwritten field. |
| claim_probability | 0.32 | Possible, pending targeted image review. |
| relevance | 0.25 | Source-control relevance only. |
| canonical_readiness | 0.03 | Not ready as canonical metadata. |

## Hypothesis 3: Contextual Reading `50 5569 5569` Is Correct

Hypothesis: adjacent source metadata and filename identify the handwritten number as `50 5569 5569`.

Literal evidence:

- The raw source path is `raw/sources/R3578-50-5569-5569-Jacket5.pdf`.
- The converted filename and source packet metadata also carry `50-5569-5569`.
- The staged draft says adjacent jacket metadata uses `50 5569 5569` and that the image-reviewed evidence does not clearly support the exact converted `5509/5509` reading.

Interpretation:

- This is plausible contextual evidence, and it is the main reason to request targeted reread.
- It is not direct proof of the literal page handwriting. Promotion should wait for a proof-reviewed image crop or page reread.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.00 | This is an administrative identifier, not a person. |
| conflict_severity | 0.36 | Meaningful for source metadata, not family identity. |
| evidence_quality | 0.64 | Multiple metadata layers align, but they are contextual rather than a fresh literal reading. |
| conversion_confidence | 0.42 | Context improves plausibility but does not settle handwriting. |
| claim_probability | 0.66 | More likely than the converted exact value, but still unresolved. |
| relevance | 0.30 | Relevant to source packet and citation alignment. |
| canonical_readiness | 0.08 | Hold for conversion QA before promotion. |

## Hypothesis 4: Page 5 Supports A Genealogical Person Or Relationship

Hypothesis: the page supports a same-person, duplicate-person, name-variant, relationship, or chronology claim.

Literal evidence:

- The assigned chunk contains treaty title text, United States ratification/proclamation dates, publication imprint, registry receipt stamp, and an administrative handwritten number.
- The staged negative identity candidate states that no genealogical person is named or identified in this assigned chunk.
- The source packet says no family relationship evidence is stated on this page.

Interpretation:

- This hypothesis is not supported. The page should not create or alter a person, relationship, family chronology, or identity cluster.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.00 | No genealogical identity appears. |
| conflict_severity | 0.02 | No person conflict exists. |
| evidence_quality | 0.82 | The local staged layers agree that this is source context only. |
| conversion_confidence | 0.86 | Printed text is adequate for the negative identity conclusion. |
| claim_probability | 0.01 | Very low probability that this page supports a genealogy identity claim. |
| relevance | 0.10 | Useful as a negative check only. |
| canonical_readiness | 0.00 | Do not promote to canonical person or relationship pages. |

## Pulgar-Line Anti-Conflation Check

The staged draft, source packet, assigned chunk, staged claim, and negative identity candidate do not mention Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario/Dario Pulgar Arriagada, Jose del Carmen Pulgar, Jose del Carmen Segundo Pulgar Arriagada, Juana Arriagada de Pulgar, or Juana de Dios Amagada de Pulgar.

Existing wiki context remains separate:

- `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied as Alexander John Heinz's maternal grandfather and warns not to attach similarly named Pulgar records without identity review.
- `wiki/people/dar-o-pulgar-arriagada.md` records a separate reviewed expropriation-context evidence snapshot for Dario Pulgar Arriagada.
- `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` records birth-register evidence and a probable low-confidence mother link to Juana Arriagada de Pulgar.
- `wiki/people/jose-del-carmen-pulgar.md` and `wiki/people/juana-de-dios-amagada-de-pulgar.md` relate to a different staged child-parent context for Tulio Cesar Luis Jose.

Ranked Pulgar hypotheses for this staged draft:

| rank | hypothesis | probability | next step |
| ---: | --- | ---: | --- |
| 1 | The Treaty Series cover is unrelated to all Pulgar-line identity clusters. | 0.99 | No Pulgar merge, rename, attachment, or promotion from this draft. |
| 2 | The source identifier indirectly supplies context for Dario Arturo Pulgar-Smith or Dario Arturo Pulgar. | 0.01 | Reject unless a later reviewed local source explicitly links this League file page to that person. |
| 3 | The source identifier supplies evidence for Dario Jose Pulgar-Arriagada or Dario/Dario Pulgar Arriagada. | 0.01 | Reject for this draft; keep those as separate proof-review contexts. |
| 4 | The page supplies evidence for Jose/Juana parent candidates. | 0.00 | Reject; no Jose/Juana names, parentage, or household evidence appears here. |

Exact Pulgar proof-review or promotion step needed next: none for this staged draft. Continue Pulgar-line review only in staged drafts or reviewed notes that actually name Pulgar, Jose, or Juana persons.

## Conflicts

- Same-person conflict: none.
- Duplicate-person conflict: none.
- Name-variant conflict: none.
- Relationship conflict: none.
- Chronology conflict: none for genealogical persons.
- Conversion/source-metadata conflict: unresolved handwritten file number on page 5, with evidence layers `50 /5509/5509`, proof-review doubt about that exact reading, and contextual metadata `50 5569 5569`.

## Recommended Next Action

Keep the staged draft on `hold_for_conversion_qa`. The exact next proof-review step is a targeted page-image reread of the top-center handwritten number on page 5, preferably documenting whether the literal reading is `50 /5509/5509`, `50 /5569/5569`, `50 5569 5569`, or an explicitly uncertain form. Do not promote the exact handwritten number as canonical source metadata until that reread is complete. Do not create, merge, rename, attach, or promote any person or relationship claim from this page.
