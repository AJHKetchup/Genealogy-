---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/conflicts/chunk-759f8ddf442b-p0028-01-juana-diaz-munoz-conversion-and-identity-watch.md
worker: postconv-identity-analysis-20260523081634254
staged_draft: research/_staging/conflicts/chunk-759f8ddf442b-p0028-01-juana-diaz-munoz-conversion-and-identity-watch.md
source_packet: research/_staging/source-packets/chunk-759f8ddf442b-p0028-01-juana-diaz-munoz-medical-guide-listing.md
source_path: raw/sources/Guía Médica Nacional Profesiones Médicas y Paramedicas, Servicio Nacional de Salud, Santiago, Chile, July 1959, First Edition.pdf
converted_file: raw/converted/ca72a88105-gu-a-m-dica-nacional-pro-p0021-0040-gu-a-m-dica-nacional-profesiones-m-dicas-y-paramedicas-servicio-nacional-de-salud-santiago-chile-july-1959-first-edition-pages-21-40.codex.md
chunk: raw/chunks/ca72a88105-gu-a-m-dica-nacional-pro-p0021-0040-gu-a-m-dica-nacional-profesiones-m-dic-5f5453300f/page-0028-chunk-01.md
chunk_id: CHUNK-759f8ddf442b-P0028-01
page_reference: source page 28
analysis_status: hold
canonical_readiness: hold_for_conversion_qa
---

# Identity/Conflict Analysis: Juana Diaz Munoz Directory Row

## Blockers

- Exact staged draft analyzed: `research/_staging/conflicts/chunk-759f8ddf442b-p0028-01-juana-diaz-munoz-conversion-and-identity-watch.md`.
- The controller and source packet both hold this evidence for `qc:reread-page`; the rendered page image path recorded in chunk metadata was not present during extraction.
- The literal local evidence is a single converted directory row: `| Díaz Muñoz, Juana | Darío Urzúa 1660 | Santiago |`.
- The source does not state birth, death, parentage, spouse, child, sibling, household, profession details beyond directory context, or a direct family relationship.
- No canonical wiki page for `Juana Diaz Munoz` or `Juana Díaz Muñoz` was found in the local wiki search. The exact name, diacritics, row alignment, address, locality column, and column headings need visual reread before promotion.
- The named `genealogy-proof-review` skill was not installed in the available skills list, so this note applies the requested proof-review fields directly from local staged, converted, chunk, reviewed-note, and canonical wiki evidence only.
- No external research was performed. No raw sources, converted Markdown, chunks, staged source packets/claims/identities/relationships/conflicts, or canonical wiki pages were edited.

## Hypothesis 1: A Distinct Directory Mention For Juana Diaz Munoz

Hypothesis: the row records a named person, `Díaz Muñoz, Juana`, listed in the July 1959 Chilean medical/paramedical guide with address/contact `Darío Urzúa 1660` and locality `Santiago`.

Literal evidence:

- The assigned conflict draft states that the converted row reads `| Díaz Muñoz, Juana | Darío Urzúa 1660 | Santiago |`.
- The source packet repeats the same row and identifies the source as the July 1959 `Guia Medica Nacional, Profesiones Medicas y Paramedicas`.
- The chunk transcription for source page 28 includes `Díaz Muñoz, Juana` between adjacent Díaz entries, with `Darío Urzúa 1660` in the second column and `Santiago` in the third column.
- Staged claims separately hold the name listing, address/contact, and locality as draft claims pending conversion QA.

Interpretation:

- This is the strongest narrow reading. The row likely supports a directory listing for one person named Juana Diaz Munoz, but only after page-image/PDF reread confirms the table extraction.
- The address should be treated as a directory contact or listing address, not silently promoted as private residence until the page heading/column label is checked.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.70 | Name, address, and city align across the draft, source packet, chunk, and converted file, but page reread is pending. |
| conflict_severity | 0.28 | No direct identity conflict yet; main risk is conversion or over-promotion from a thin row. |
| evidence_quality | 0.58 | Tabular converted text is coherent but unverified against the image/PDF. |
| conversion_confidence | 0.55 | Staged materials call conversion confidence medium and require reread because page image was unavailable. |
| claim_probability | 0.68 | Probable directory-row mention if row alignment survives reread. |
| relevance | 1.00 | Directly relevant to the assigned staged conflict draft. |
| canonical_readiness | 0.18 | Hold for conversion QA; not ready for canonical fact promotion. |

## Hypothesis 2: Same Person As Another Juana Diaz Or Diaz Munoz

Hypothesis: this row may refer to another local person with a similar Juana/Diaz/Munoz name variant.

Literal evidence:

- Local searches found this exact Juana Diaz Munoz/Díaz Muñoz evidence only in the assigned staged packet, claims, identity candidate, relationship note, conflict draft, converted file, and chunk.
- Other local hits for `Díaz Muñoz` concern different people or unrelated contexts, such as `Asterio Díaz Muñoz`, `Luis 2.º del Rio Díaz Muñoz`, and `Díaz Muñoz Soto, Ignacio`.
- No existing canonical `Juana Diaz Munoz` page, no duplicate-person profile, and no reviewed note tying this Juana to another Juana Diaz/Munoz candidate was found.

Interpretation:

- A same-person or duplicate-person hypothesis remains possible in the abstract, but the available local evidence does not identify a second candidate to merge or compare.
- Name variants without shared date, address, occupation, family, or source context should not be treated as proof.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.16 | No second local Juana Diaz/Munoz candidate was found. |
| conflict_severity | 0.35 | A future name-only merge could misattach facts, but no active duplicate conflict is proved. |
| evidence_quality | 0.30 | Evidence is mostly absence of local matches plus thin directory data. |
| conversion_confidence | 0.55 | Same underlying conversion hold applies. |
| claim_probability | 0.12 | Low from current evidence. |
| relevance | 0.80 | Required duplicate/name-variant check. |
| canonical_readiness | 0.02 | No merge, rename, or canonical attachment supported. |

## Hypothesis 3: Relationship Or Chronology Conflict In The Row

Hypothesis: the row creates or resolves a relationship or chronology conflict for Juana Diaz Munoz.

Literal evidence:

- The staged relationship note explicitly classifies the row as `no_family_relationship_stated`.
- The row includes only name, address/contact, and locality in the converted table.
- No birth date, death date, age, spouse, parent, child, sibling, household member, or time span beyond the July 1959 source date is stated.

Interpretation:

- The row does not support a relationship claim.
- The only chronology claim reasonably implied is a directory listing in or by July 1959, subject to conversion QA. It does not prove residence duration, vital status, or professional activity dates beyond the directory context.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.20 | Person mention exists, but no relationship identity bridge is present. |
| conflict_severity | 0.18 | Low relationship/chronology conflict severity because the row states little. |
| evidence_quality | 0.52 | Good enough to know no family relationship is stated in the extracted row; still held for reread. |
| conversion_confidence | 0.55 | Medium conversion confidence. |
| claim_probability | 0.10 | Low probability for any relationship or chronology conflict beyond directory listing date. |
| relevance | 0.76 | Directly checks required relationship and chronology conflict classes. |
| canonical_readiness | 0.01 | No relationship promotion supported. |

## Pulgar-Line Anti-Conflation Check

The assigned Juana Diaz Munoz draft does not mention Pulgar, Dario, Jose, Arriagada, or Smith. Existing wiki context does contain Pulgar-line people and Jose/Juana parent candidates, so they are compared here only as an anti-conflation guard.

| candidate | local evidence context | comparison to Juana Diaz Munoz row |
|---|---|---|
| `Dario Arturo Pulgar-Smith` | Canonical family-supplied maternal grandfather of Alexander John Heinz; wiki page warns not to merge Pulgar records by name alone. | No name, date, place, address, or relationship bridge to `Díaz Muñoz, Juana`. Probability 0.01. |
| `Dario Arturo Pulgar` | Staged CV subject in separate drafts, usually document-title/source-context based. | No overlap except broad Chilean research corpus. Probability 0.01. |
| `Dario Jose Pulgar-Arriagada` | Separate staged photograph/source-title or register-related Pulgar-Arriagada contexts, held for identity proof review. | No overlap with the medical-guide row. Probability 0.01. |
| `Dario/Darío Pulgar Arriagada` | Canonical/staged expropriation and Pulgar-Arriagada contexts, including a 2000 event. | No overlap with a 1959 Santiago `Díaz Muñoz, Juana` directory row. Probability 0.01. |
| `Jose del Carmen Pulgar` | Canonical stub tied to a draft parent link for `Tulio Cesar Luis Jose`. | No row evidence connects him to Juana Diaz Munoz. Probability 0.01. |
| `Jose del Carmen Segundo Pulgar Arriagada` | Canonical stub tied to a probable low-confidence mother-child cluster with `Juana Arriagada de Pulgar`. | No same-person or relationship bridge. Probability 0.01. |
| `Juana Arriagada de Pulgar` | Canonical stub tied to a probable low-confidence mother-child register cluster. | Shares only the given name `Juana`; surnames, family context, and source context differ. Do not merge. Probability 0.02. |
| `Juana de Dios Amagada de Pulgar` | Canonical stub tied to a separate draft parent cluster; maternal surname remains image-sensitive in reviewed notes. | Shares only the given name `Juana`; no Diaz/Munoz, address, or directory link. Do not merge. Probability 0.02. |

Ranked Pulgar-line conclusion:

| rank | hypothesis | probability | action |
|---:|---|---:|---|
| 1 | Juana Diaz Munoz is unrelated to the currently visible Pulgar-line candidates in this staged evidence | 0.96 | Preserve as a separate directory mention. |
| 2 | Juana Diaz Munoz is a name variant or same person as a Jose/Juana Pulgar parent candidate | 0.02 | Do not merge; require a direct source bridge naming Díaz/Muñoz with Pulgar/Arriagada family context. |
| 3 | Juana Diaz Munoz connects to Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, or Dario/Darío Pulgar Arriagada | 0.01 | No Pulgar-line promotion step from this draft. |

The exact next Pulgar-line proof-review step is none from this draft. If future evidence links this Juana to the Pulgar line, first perform a separate identity proof review comparing the confirmed source reading against `Dario Arturo Pulgar-Smith`, staged `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar` before any merge or relationship promotion.

## Conflicts

- Same-person conflict: unresolved only in the general sense that `Juana Diaz Munoz` is not yet tied to a canonical person. No competing same-person candidate is proved locally.
- Duplicate-person risk: low current risk, moderate future risk if another Juana Diaz/Munoz appears and the row is merged by name alone.
- Name-variant conflict: exact diacritics and spelling should remain `Díaz Muñoz, Juana` as the literal converted reading until page reread confirms or corrects it. Do not silently normalize to `Juana Diaz Munoz` for canonical use.
- Relationship conflict: none stated. The row does not name parents, spouse, children, household, or Pulgar-line family members.
- Chronology conflict: none stated. The source date supports at most a July 1959 directory context after reread.
- Conversion/provenance conflict: active blocker. The row is coherent in converted Markdown, but page reread is required and the rendered page image was unavailable.

## Ranked Hypotheses

| rank | hypothesis | probability | action |
|---:|---|---:|---|
| 1 | A distinct 1959 directory mention for `Díaz Muñoz, Juana` at `Darío Urzúa 1660`, Santiago | 0.68 | Hold for visual reread, then proof review as a directory listing/contact claim. |
| 2 | Same person as another local Juana Diaz/Munoz candidate | 0.12 | Preserve as possible only; no candidate currently found. |
| 3 | Row creates a relationship or chronology conflict | 0.10 | Do not promote relationship or chronology conflict. |
| 4 | Same as or related to Pulgar-line Dario/Jose/Juana candidates | 0.01-0.02 | Do not attach or merge; anti-conflation only. |

## Recommended Next Action

Keep `research/_staging/conflicts/chunk-759f8ddf442b-p0028-01-juana-diaz-munoz-conversion-and-identity-watch.md` on hold for conversion QA. Do not promote a canonical conflict, merge people, rename pages, or attach the row to any Pulgar-line or Juana parent candidate.

The exact next proof-review step is the existing reread-page task: locate or regenerate the rendered page image for source page 28, compare the printed PDF/image against `| Díaz Muñoz, Juana | Darío Urzúa 1660 | Santiago |`, confirm column headings and row alignment, and only then move the directory listing, address/contact, and locality claims into proof review.
