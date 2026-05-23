---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/conflicts/conflict-stage-chunk-3f469b56e502-p0006-01-french-ocr-qa.md
worker: postconv-identity-analysis-20260523101028232
staged_draft: research/_staging/conflicts/conflict-stage-chunk-3f469b56e502-p0006-01-french-ocr-qa.md
source_path: raw/sources/R3578-50-5569-5569-Jacket5.pdf
source_packet: research/_staging/source-packets/sp-stage-chunk-3f469b56e502-p0006-01-proclamation-convention-opening.md
converted_file: raw/converted/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25.codex.md
chunk: raw/chunks/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25-codex/page-0006-chunk-01.md
chunk_id: CHUNK-3f469b56e502-P0006-01
page_reference: page 6
analysis_status: conversion_qa_conflict_only
canonical_readiness: do_not_promote
---

# Identity/Conflict Analysis: CHUNK-3f469b56e502-P0006-01

## Blockers

- The exact staged draft reviewed here is `research/_staging/conflicts/conflict-stage-chunk-3f469b56e502-p0006-01-french-ocr-qa.md`.
- The staged conflict is a conversion-QA issue: likely OCR degradation in printed French treaty text, party names, diacritics, and country/state-office wording.
- The linked chunk was produced by Docling basic conversion and is marked `rough_ok`; the source packet holds promotion for conversion QA.
- The page is a United States treaty publication page beginning the French text of the 1929 Prisoners of War Convention. It does not identify a private genealogical person, family relationship, vital event, residence, household, or family chronology.
- Literal source readings must not be silently normalized from family context or from expected French spellings. Suspect OCR readings need page-image comparison before promotion.
- No external research was performed. No raw sources, converted Markdown, chunks, source packets, conflict drafts, or canonical wiki pages were edited.
- The named `$genealogy-proof-review` skill file was not available in the session skill list; this note applies the evidence-contract requirements from the dispatch: literal support separated from interpretation, multiple hypotheses preserved, scored confidence, and no promotion without proof-review resolution.

## Hypothesis 1: The Conflict Is Only A French OCR Conversion-QA Conflict

Hypothesis: the staged draft correctly identifies OCR/diacritic degradation in a printed treaty text page, not a same-person, duplicate-person, name-variant, relationship, or chronology conflict.

Literal evidence:

- The staged conflict draft quotes suspect conversion strings: `Autriclie`, `Beiges`, `frangaise`, and `d^sireux de d^velopper`.
- The linked source packet says reading confidence is medium overall but lower for exact French spellings and party names, and gives additional suspect examples including `Sudde`.
- The assigned chunk records the page metadata as source page 6, conversion method `Docling basic conversion`, readability status `rough_ok`, and page image `raw/codex-conversion-jobs/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25/page-images/page-0006.jpg`.
- The chunk body begins with `By the President of the United States of America`, `A PROCLAMATION`, and a statement that a Convention Relating to the Treatment of Prisoners of War was signed at Geneva on July 27, 1929.
- The French title is converted as `Convention relative au traitement des prisonniers DE GUERRE DU 27 JUILLET 1929.`

Interpretation:

- The strongest conclusion is that this is a source-text QA issue affecting exact treaty wording, country names, and titles.
- The page can support only staged source-context claims until the French text is image-checked.
- Because the suspect strings are country/title words rather than family names, this staged draft does not support a genealogical identity conflict.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.00 | No private person identity is asserted by the staged conflict, source packet, or chunk. |
| conflict_severity | 0.34 | Material for exact source-context transcription, minimal for genealogical identity. |
| evidence_quality | 0.72 | Staged draft, source packet, and chunk agree on the OCR concern and source context. |
| conversion_confidence | 0.45 | General reading order is usable, but exact French spellings and diacritics are held for QA. |
| claim_probability | 0.86 | High probability that a real conversion-QA problem exists. |
| relevance | 0.26 | Relevant to citation/source-context hygiene, not to person identity resolution. |
| canonical_readiness | 0.05 | Do not promote exact French wording, titles, or party names until image QA. |

## Hypothesis 2: The Page Supplies A Genealogical Person Identity Or Relationship

Hypothesis: page 6 supplies a same-person, duplicate-person, name-variant, relationship, or chronology claim for a genealogical subject.

Literal evidence:

- The source packet states that genealogical relevance is source-context evidence only and that the page names governments and state offices as treaty parties.
- The source packet states that this page does not identify a private person, family relationship, vital event, residence, or household.
- The assigned chunk lists no genealogy leads from the Docling conversion pass.
- The staged conflict draft itself states that the candidate is a conversion-QA conflict, not a genealogical identity conflict.

Interpretation:

- This hypothesis is not supported by the assigned evidence.
- Named heads of state or offices in a treaty preamble are not genealogical person candidates in this workspace unless a separate reviewed local source connects them to a family line, which this draft does not do.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.00 | No family-tree person appears in the relevant staged evidence. |
| conflict_severity | 0.01 | No same-person, duplicate-person, relationship, or chronology conflict exists. |
| evidence_quality | 0.80 | Multiple local layers explicitly classify the page as non-genealogical source context. |
| conversion_confidence | 0.70 | The broad non-genealogical character is clear despite OCR noise. |
| claim_probability | 0.01 | Very low probability that this page supports a genealogy identity claim. |
| relevance | 0.08 | Relevant only as a negative identity check. |
| canonical_readiness | 0.00 | Do not promote to canonical person or relationship pages. |

## Hypothesis 3: Suspect French Readings Can Be Silently Corrected Before QA

Hypothesis: expected French spellings and known treaty-party names are sufficient to replace the converted readings before image-level proof review.

Literal evidence:

- The conversion currently reads examples such as `Autriclie`, `Beiges`, `frangaise`, `Sudde`, and `d^sireux de d^velopper`.
- The source packet marks the page `hold_for_conversion_qa` and says image comparison is required before exact titles, country names, or French wording are promoted.
- The chunk's own QA language says conversion QA must compare the output with the rendered page image before research extraction.

Interpretation:

- Expected French forms are useful hypotheses for QA, but not promoted literal readings.
- A proof-review note should record the image-reviewed correction, uncertainty, or retained literal OCR form before any normalized treaty text appears in canonical source notes.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.00 | This hypothesis concerns treaty text, not person identity. |
| conflict_severity | 0.30 | Silent correction could corrupt source transcription, but it does not affect a family identity. |
| evidence_quality | 0.66 | The suspect readings are explicit; exact corrections require image comparison. |
| conversion_confidence | 0.38 | The specific words under review are low-confidence until visual QA. |
| claim_probability | 0.20 | Some expected corrections are likely, but the exact proof-reviewed text is not yet established. |
| relevance | 0.24 | Relevant to source-context claims and OCR QA only. |
| canonical_readiness | 0.04 | Hold all exact normalized forms until conversion QA documents them. |

## Pulgar-Line Anti-Conflation Check

The staged draft, source packet, and assigned chunk do not mention Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario/Dario Pulgar Arriagada, Jose del Carmen Pulgar, Jose del Carmen Segundo Pulgar Arriagada, Juana Arriagada de Pulgar, or Juana de Dios Amagada de Pulgar.

Existing wiki context remains separate:

- `wiki/people/dario-arturo-pulgar-smith.md` represents Dario Arturo Pulgar-Smith from family-supplied knowledge as Alexander John Heinz's maternal grandfather and warns not to automatically merge similarly named Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records.
- `wiki/people/dar-o-pulgar-arriagada.md` records a separate `Darío Pulgar Arriagada` evidence snapshot for a 2000 expropriation context.
- `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md` records a separate birth-registration cluster with a low-confidence/probable mother link to `Juana Arriagada de Pulgar`.
- `wiki/people/jose-del-carmen-pulgar.md` and `wiki/people/juana-de-dios-amagada-de-pulgar.md` are tied to a separate staged child-parent cluster for `Tulio Cesar Luis Jose`.

Ranked Pulgar hypotheses for this staged draft:

| rank | hypothesis | probability | action |
|---:|---|---:|---|
| 1 | The page-6 treaty text is unrelated to all Pulgar-line identity clusters. | 0.99 | No Pulgar merge, attachment, rename, or promotion from this draft. |
| 2 | The treaty page indirectly supplies context for Dario Arturo Pulgar-Smith or Dario Arturo Pulgar. | 0.01 | Reject unless a later reviewed local source explicitly links this treaty publication to that person. |
| 3 | The treaty page supplies evidence for Dario Jose Pulgar-Arriagada or Dario/Dario Pulgar Arriagada. | 0.01 | Reject for this draft; maintain those as separate Pulgar-Arriagada proof-review contexts. |
| 4 | The page supplies evidence for Jose/Juana parent candidates. | 0.00 | Reject; no Jose/Juana names, parentage, or household evidence appears here. |

Exact next Pulgar proof-review step needed next: none for this staged draft. Pulgar-line work should continue only in separate staged drafts, reviewed notes, and canonical candidates that actually name Pulgar, Jose, or Juana persons.

## Conflicts

- Same-person conflict: none.
- Duplicate-person conflict: none.
- Name-variant conflict: none for genealogical persons.
- Relationship conflict: none.
- Chronology conflict: none for genealogical persons.
- Conversion/source-text conflict: unresolved French OCR degradation in country names, offices, diacritics, and treaty wording; examples include `Autriclie`, `Beiges`, `frangaise`, `Sudde`, and `d^sireux de d^velopper`.

## Recommended Next Action

Keep this staged conflict on `hold_for_conversion_qa`. The next proof-review step is a targeted image comparison of page 6 against the converted French text, especially the treaty-party list, diacritics, and suspect words named above. After image QA, update or supersede the conversion-QA note with documented literal readings and normalized interpretations where appropriate. Do not create, merge, rename, or attach any person or relationship claim from this page.
