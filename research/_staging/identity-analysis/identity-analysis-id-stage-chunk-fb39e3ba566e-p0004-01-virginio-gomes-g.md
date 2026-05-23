---
type: identity_conflict_analysis
role: identity_researcher
task_id: "identity-analysis:research/_staging/identity/ID-STAGE-CHUNK-fb39e3ba566e-P0004-01-virginio-gomes-g.md"
worker: postconv-identity-analysis-20260523073810194
staged_draft: "research/_staging/identity/ID-STAGE-CHUNK-fb39e3ba566e-P0004-01-virginio-gomes-g.md"
subject: "Dr. Virginio Gomes G."
source_packet: "research/_staging/source-packets/SP-STAGE-CHUNK-fb39e3ba566e-P0004-01-el-aguila-dario-pulgar-virginio-gomes.md"
source_path: "raw/sources/El Aguila Nombre Grande Scan.pdf"
converted_file: "raw/converted/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18.codex.md"
chunk: "raw/chunks/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18-codex/page-0004-chunk-01.md"
chunk_id: "CHUNK-fb39e3ba566e-P0004-01"
analysis_status: hold_for_conversion_qa_and_identity_bridge
canonical_readiness: hold
---

# Identity/Conflict Analysis: Dr. Virginio Gomes G.

## Blockers First

- The exact staged draft analyzed here is `research/_staging/identity/ID-STAGE-CHUNK-fb39e3ba566e-P0004-01-virginio-gomes-g.md`.
- The staged draft identifies the article subject as `Dr. Virginio Gomes G.` and explicitly says the surname and final initial must be checked against the page image before canonical identity creation or merge.
- The source packet keeps this page on `hold_for_conversion_qa`; it requests reread-page QA for proper names, punctuation around Hospital San Juan de Dios, and handwritten insertions.
- A prior proof-review note for the same `El Aguila` article claim could not complete rendered page-image reread because the expected page image was absent. It also recorded a chunk/hash mismatch between the staged `CHUNK-fb39e3ba566e-P0004-01` identifier and local chunk metadata.
- The referenced chunk path now carries front matter for `CHUNK-b84806e38e9f-P0004-01`, while the staged draft/source packet use `CHUNK-fb39e3ba566e-P0004-01`. This provenance mismatch blocks canonical use.
- The converted transcription contains irregular readings such as `LECTAIRES`, `CUIDAD`, `IQUQUE`, and `PROFECION`; the article title and surname may be affected by the same conversion quality limits.
- No external research was performed. No raw sources, converted Markdown, chunks, reviewed notes, staged drafts outside this output, or canonical wiki pages were edited.

## Literal Source Reading

The staged identity draft gives the title support as:

```text
_EL_DR_VIRGINIO_GOMES__G__
```

The converted article body later reads:

```text
EL DOCTOR GOMES DEJA UNA HUELLA LUMINOSA
```

The same converted page says the subject was born in `LA CUIDAD DE LOS ANGELES`, practiced in `IQUQUE` and then Concepcion, and was designated director of the old Hospital San Juan de Dios around 1916. These are source readings from the converted page, not corrections or normalized facts.

Interpretation kept separate: this is direct local evidence for an article subject rendered as `Dr. Virginio Gomes G.` in the conversion. It is not yet proof that `Gomes` should be normalized to canonical `Gomez`, or that the final `G.` expands to `Gonzalez`.

## Hypothesis 1: Held Article-Subject Candidate Dr. Virginio Gomes G.

Hypothesis: this staged draft supports a narrow held identity candidate for the `El Aguila` article subject, exactly as converted: `Dr. Virginio Gomes G.`

Supporting evidence:

- The staged identity draft names the candidate identity as `Dr. Virginio Gomes G.`.
- The source packet identifies the page as an article credited to Dr. Dario Pulgar and titled for `EL DR VIRGINIO GOMES G`.
- The converted page title and body both use `GOMES` as transcribed.
- Staged claims from this same source consistently use `Dr. Virginio Gomes G.` for birth place, disappearance, hospital-director, practice-place, and respectable-family assertions.

Interpretation:

- This is the strongest direct identity conclusion from the assigned staged draft. It should remain a held local candidate until conversion QA verifies the surname and final initial against the page image.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.76 | The staged draft, source packet, converted page, and related staged claims agree on the candidate as converted. |
| conflict_severity | 0.24 | Low if kept as a held article-subject candidate; higher only if merged prematurely. |
| evidence_quality | 0.60 | Direct periodical article text, but derivative, single-source, and QA-held. |
| conversion_confidence | 0.63 | The name appears in title/body, but page reread and metadata reconciliation are required. |
| claim_probability | 0.80 | Probable that the converted article concerns a doctor rendered as Virginio Gomes/Gomez with final initial G. |
| relevance | 1.00 | Directly answers the assigned staged identity draft. |
| canonical_readiness | 0.18 | Hold for conversion QA before promotion or merge. |

## Hypothesis 2: Same Person As Canonical Virginio Gomez

Hypothesis: the staged `Dr. Virginio Gomes G.` is the same person as canonical `wiki/people/virginio-gomez.md`.

Supporting evidence:

- The canonical page `wiki/people/virginio-gomez.md` exists as a stub for `Virginio Gomez`.
- The canonical evidence snapshot contains a reviewed birth-place fact: `was born in: Los Angeles`, sourced to the Osorio anatomy article packet.
- Reviewed local proof notes for Osorio page 2 say the source names `Dr. Virginio Gomez`, born in Los Angeles in 1877, and connects him to San Juan de Dios Hospital / University of Concepcion context.
- The `El Aguila` converted article also says the subject was born in Los Angeles and was associated with Hospital San Juan de Dios and the University of Concepcion context.
- The `Gomes` versus `Gomez` difference is a plausible conversion/name-variant issue, especially because the staged draft itself requests reread for the surname.

Conflicts and limits:

- The `El Aguila` page as converted says `GOMES`, not `GOMEZ`.
- The canonical page has preferred name `Virginio Gomez` and does not currently list `Virginio Gomes G.` as an accepted variant.
- The Osorio evidence is secondary and separately conversion/page-boundary sensitive in earlier staging, though later proof reviews accepted the narrow birth-place statement as likely.
- The `El Aguila` page image was not reread for this task, so the spelling bridge cannot be accepted silently.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.72 | Shared rare given name, doctor title, Los Angeles birth-place, San Juan de Dios, and University of Concepcion context strongly suggest same person, but surname spelling is unresolved. |
| conflict_severity | 0.48 | Moderate: wrong merge would alter name normalization and attach article claims to the canonical stub. |
| evidence_quality | 0.66 | Multiple local sources agree on context, but both are derivative/secondary or conversion-held. |
| conversion_confidence | 0.62 | Osorio page 2 was reviewed more strongly; this `El Aguila` page still needs image reread. |
| claim_probability | 0.74 | Probable same person, not ready for canonical merge from this draft alone. |
| relevance | 0.96 | Direct duplicate/same-person check against existing canonical wiki. |
| canonical_readiness | 0.22 | Hold until `Gomes/Gomez` and final initial are verified. |

## Hypothesis 3: Same Person As Virginio Gomez Gonzalez

Hypothesis: the final `G.` in `Dr. Virginio Gomes G.` is an initial for `Gonzalez`, matching local page 3/figure-caption context that names `Dr. Virginio Gomez Gonzalez`.

Supporting evidence:

- Staged Osorio identity-scope notes report adjacent page 3 or figure-caption material reading `Dr. Virginio Gomez Gonzalez`.
- Local raw chunks from the Osorio article include image/caption context for `Dr. Virginio Gomez Gonzalez`.
- The `El Aguila` article title supplies a final `G.` after `GOMES`, which could correspond to a second surname initial.
- The professional and institutional context overlaps with the canonical `Virginio Gomez` cluster.

Conflicts and limits:

- The assigned `El Aguila` staged draft does not expand the final `G.`.
- Earlier Osorio page 2 notes warn that page 3 material was outside some assigned page-2 extraction ranges or involved page-boundary contamination; it should not be silently imported as support for the `El Aguila` page.
- `Gomes G.` could represent another spelling or another surname initial until the image is reread.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.64 | The initial aligns plausibly with local `Gomez Gonzalez` context, but the `El Aguila` title does not spell it out. |
| conflict_severity | 0.44 | Moderate if used to expand the name without direct support. |
| evidence_quality | 0.55 | Useful local context, but partly adjacent/out-of-scope for earlier chunks. |
| conversion_confidence | 0.54 | Final initial and surname both require image verification. |
| claim_probability | 0.62 | Plausible expansion, not proved. |
| relevance | 0.90 | Important name-variant and duplicate-person check. |
| canonical_readiness | 0.12 | Do not promote expanded full name from this draft. |

## Hypothesis 4: Separate Person Named Dr. Virginio Gomes G.

Hypothesis: `Dr. Virginio Gomes G.` is a distinct person from canonical `Virginio Gomez`.

Supporting evidence:

- The literal converted `El Aguila` title and body read `GOMES`.
- The staged draft explicitly sets `possible_canonical_match: null`, which means the extraction worker did not assert a canonical match.
- No direct full-name expansion, birth year, or source-image verified spelling is available in the assigned draft.

Conflicts and limits:

- The combined local context is unusually aligned: doctor title, Los Angeles birthplace, San Juan de Dios directorship context, University of Concepcion connection, and `Virginio` with surname `Gomes/Gomez`.
- Existing canonical `Virginio Gomez` is the only obvious local canonical page found for this identity cluster.
- Treating the `s` spelling as a separate person without reread would give the conversion more authority than the source image.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.20 | Possible only because spelling is unresolved; contextual overlap favors a variant rather than a separate person. |
| conflict_severity | 0.38 | Premature separate-page creation could duplicate the existing Virginio Gomez cluster. |
| evidence_quality | 0.42 | The only separation evidence is the converted surname spelling. |
| conversion_confidence | 0.40 | The same source asks for proper-name reread. |
| claim_probability | 0.18 | Low but must be preserved until image QA. |
| relevance | 0.86 | Direct duplicate-person risk. |
| canonical_readiness | 0.04 | Do not create or promote a separate canonical person yet. |

## Relationship And Chronology Conflicts

- Relationship-conflict evidence: none stated. The staged relationship note for this chunk says Dr. Dario Pulgar is the credited writer and Dr. Virginio Gomes G. is the article subject; it states no parent, spouse, child, sibling, household, or other kinship wording.
- The phrase that the article subject belonged to a respectable family does not identify relatives and should not be promoted as a tree relationship.
- Chronology support from this page is partial: it reports a disappearance aboard the ship `Alondra`, a birthplace in Los Angeles, medical practice in Iquique and Concepcion, and designation as director of the old Hospital San Juan de Dios around 1916. No birth date, death date, parents, spouse, or children are stated in this chunk.
- The Osorio/context cluster has a reviewed secondary birth year of 1877 and related hospital/university details, but this staged identity analysis does not use those to silently correct the `El Aguila` reading. They justify the next same-person proof review after conversion QA.

## Pulgar-Line Comparison Required By Contract

The assigned source context names Dr. Dario Pulgar as article author, but this staged identity draft concerns Dr. Virginio Gomes G. The following Pulgar comparisons are included only to prevent relationship or author/subject conflation:

| candidate | relationship to this draft | identity conclusion |
|---|---|---|
| Dario Arturo Pulgar-Smith | Existing canonical family-supplied maternal-grandfather profile. | No evidence this Virginio identity draft links to him. Do not attach a relationship or article authorship claim from this subject draft. |
| Dario Arturo Pulgar | Staged CV subject in other local drafts. | No direct link from Virginio's identity to the CV subject. The article author line is a separate Dario proof problem. |
| Dario Jose Pulgar-Arriagada | Staged/metadata-dependent Pulgar candidate in other local source packets. | No link from this Virginio identity draft; no Jose/Juana parent evidence appears in the article subject claim. |
| Dario/Dario Pulgar Arriagada | Existing canonical/staged Arriagada contexts, including a 2000 notice and older medical leads. | No link from this Virginio identity draft; preserve separately. |
| Jose/Juana parent candidates | Existing Pulgar-line birth-register candidates. | No parent, spouse, child, or household wording appears for Virginio or Dario in this article page. No relationship action supported. |

Ranked Pulgar conclusion: the only direct Pulgar evidence in this page is a held author credit to `Dr. Dario Pulgar`; it is not evidence about Virginio's family and not a bridge to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario/Dario Pulgar Arriagada, or Jose/Juana parent candidates. The exact next step for Pulgar-line use is the separate author identity proof review after the page image and chunk metadata are reconciled.

## Conflict Summary

- Same-person conflict: unresolved but leaning probable that `Dr. Virginio Gomes G.` is the same person as canonical `Virginio Gomez`, possibly fuller `Virginio Gomez Gonzalez`.
- Duplicate-person risk: moderate if a new canonical `Virginio Gomes G.` page is created before verifying whether `Gomes` is a conversion/spelling variant of `Gomez`.
- Name-variant conflict: live. The source currently reads `Gomes`, while existing canonical/reviewed context uses `Gomez` and sometimes `Gomez Gonzalez`.
- Relationship-conflict evidence: none. No family relationship is stated between Dario Pulgar and Virginio Gomes/Gomez, and no Jose/Juana parent candidate appears in this subject evidence.
- Chronology-conflict evidence: none direct. The `El Aguila` context around 1916 hospital directorship is broadly compatible with reviewed Osorio context, but exact wording/date must remain held until reread.
- Conversion/provenance conflict: material blocker. The image reread is incomplete and the staged chunk id does not match current local chunk metadata.

## Ranked Hypotheses

| rank | hypothesis | probability | next step |
|---:|---|---:|---|
| 1 | Held article-subject candidate `Dr. Virginio Gomes G.` | 0.80 | Restore/locate page image and reconcile chunk/hash metadata; verify title/body name. |
| 2 | Same as canonical `Virginio Gomez` | 0.74 | After image QA, run identity proof review comparing surname, birthplace, hospital, university, and disappearance context. |
| 3 | Same as fuller `Virginio Gomez Gonzalez` | 0.62 | Use only after a reviewed source confirms the final `G.` expansion or an accepted canonical alias decision. |
| 4 | Separate person `Dr. Virginio Gomes G.` | 0.18 | Preserve as a minority hypothesis until the surname image reread is complete. |

## Recommended Next Action

Keep `research/_staging/identity/ID-STAGE-CHUNK-fb39e3ba566e-P0004-01-virginio-gomes-g.md` on hold. Do not merge, rename, create a new canonical person, or promote claims from this identity draft yet.

The exact next proof-review step is conversion/provenance QA for `CHUNK-fb39e3ba566e-P0004-01`: restore or locate the rendered page image for source page range 4 / converted handwritten page 7, reread the article title and the later `EL DOCTOR GOMES` body line, and reconcile the staged `fb39e3ba566e` identifier with the current local chunk/manifest identifier mismatch. If the image confirms `Gomez G.` or `Gomes G.`, then run a focused identity proof review against canonical `wiki/people/virginio-gomez.md`, preserving `Gomes` as a literal source reading if that is what the page shows.
