---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/conflicts/chunk-a048d567968b-p0001-02-page-boundary-and-identity-qa.md
worker: postconv-identity-analysis-20260523073341159
staged_draft: research/_staging/conflicts/chunk-a048d567968b-p0001-02-page-boundary-and-identity-qa.md
source_packet: research/_staging/source-packets/chunk-a048d567968b-p0001-02-habitat-revisited-dario-pulgar.md
source_path: raw/sources/Habitat Revisited, Jim Carney, 2006.pdf
converted_file: raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md
chunk: raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-02.md
chunk_id: CHUNK-a048d567968b-P0001-02
analysis_status: hold
canonical_readiness: hold_for_conversion_page_boundary_qa
---

# Identity And Conflict Analysis: CHUNK-a048d567968b-P0001-02

## Blockers

- The exact staged conflict draft analyzed here is `research/_staging/conflicts/chunk-a048d567968b-p0001-02-page-boundary-and-identity-qa.md`.
- Page-boundary QA is the first blocker. The staged draft and source packet report that the assigned chunk is `page_start: 1` / `page_end: 1`, while the chunk body includes converted page metadata and literal transcription for source pages 4, 5, 6, and 7.
- The source packet reports that source page 4 was visually reread and confirms the Saturna passage naming `Dario`, but source page 5's rendered image was not present in this checkout; the `Pulgar` Vancouver group passage was checked through original PDF text extraction instead.
- The claim sentences in this chunk name only `Dario` and `Pulgar`. They do not state the full name `Dario Pulgar` in the same sentences and do not state `Arturo`, `Pulgar-Smith`, `Dario Jose`, `Arriagada`, parentage, spouse, child, grandchild, birth date, or death date.
- Same-source context in the converted file names `Chiliean/Canadian Dario Pulgar` on source page 2 and `Dario Pulgar` on source page 7. That context supports a likely identity inference, but it does not remove the need to label the page-4/page-5 readings as first-name-only and surname-only passages.
- Existing canonical `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied and explicitly warns not to automatically attach records mentioning `Dario`, `Pulgar`, `Pulgar-Arriagada`, or `Pulgar-Smith`.
- No external research was performed. No raw sources, converted Markdown, chunks, source packets, staged drafts, or canonical wiki pages were edited.

## Hypothesis 1: Same Habitat Person As Other Habitat Revisited Dario/Pulgar Mentions

Hypothesis: The `Dario` on source page 4 and `Pulgar` on source page 5 are same-source references to the `Dario Pulgar` identified elsewhere in `Habitat Revisited`.

Literal evidence:

- The page-4 passage reads that the author spent part of the summer, including a weekend at Saturna Island, with `Andreas, Dario, Bo-Eric and I`, developing a project description and budget for the AV Programme.
- The page-5 passage reads that by late spring 1976 a group including `Pulgar`, `Gyborg`, Jane Weiner, Barbara Janes, and the author would go to Vancouver to help get the show on the air.
- The source packet states that same-source context on source page 2 identifies `Chiliean/Canadian Dario Pulgar`.
- The converted file also names `Dario Pulgar` on source page 7 as a UN Habitat Secretariat colleague in the same Habitat/Vision Habitat narrative.

Interpretation:

- This is the strongest identity hypothesis for the assigned draft. The first-name-only and surname-only passages occur in a coherent Habitat AV Programme sequence with same-document full-name anchors.
- The inference should remain within the Habitat source cluster until conversion QA reconciles the authoritative page/chunk citation.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.84 | Same source, same AV Programme context, and nearby full-name anchors support one Habitat worker. |
| conflict_severity | 0.24 | Identity conflict is low if scoped to the same source; citation/page-boundary conflict remains high. |
| evidence_quality | 0.68 | Memoir evidence directly names colleagues in work context, but the claim sentences are partial-name references. |
| conversion_confidence | 0.58 | Page 4 image and PDF text support the words, but page 5 image and page/chunk assignment remain unresolved. |
| claim_probability | 0.86 | Likely same person within the Habitat cluster. |
| relevance | 1.00 | Directly addresses the staged conflict draft. |
| canonical_readiness | 0.26 | Hold until conversion/page-boundary QA and proof review. |

## Hypothesis 2: Same Person As Staged CV Subject Dario Arturo Pulgar

Hypothesis: The Habitat `Dario` / `Pulgar` references are to the staged CV subject `Dario Arturo Pulgar`.

Literal evidence:

- Existing staged CV analyses identify a document-level CV subject named `Dario Arturo Pulgar`.
- Related Habitat analysis for `P0001-03` records that the memoir names `Dario Pulgar` as a Chilean UN Habitat Secretariat colleague with Chile film-distribution experience under Allende and Vision Habitat work.
- The assigned page-4 and page-5 passages concern Habitat AV Programme planning and Vancouver Conference preparation.
- This assigned draft does not include `Arturo`; it uses only `Dario` and `Pulgar` in the claim sentences.

Interpretation:

- The Habitat and CV clusters appear occupationally compatible, especially in Habitat, communications, and film-distribution context.
- The bridge remains indirect for this draft because the assigned claim sentences do not give the full name and the CV identity bridge is itself staged/held.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.68 | Context aligns, but this draft lacks `Arturo` and relies on other staged records. |
| conflict_severity | 0.34 | Premature linkage could misattribute work-context claims. |
| evidence_quality | 0.60 | Cross-source occupational evidence is useful but not a vital or relationship bridge. |
| conversion_confidence | 0.54 | Habitat page assignment and some CV review points remain held. |
| claim_probability | 0.70 | Probable, not proved by this conflict draft alone. |
| relevance | 0.90 | Key comparison for later canonical routing. |
| canonical_readiness | 0.20 | Hold for proof-reviewed CV/Habitat identity bridge. |

## Hypothesis 3: Same Person As Canonical Dario Arturo Pulgar-Smith

Hypothesis: The Habitat `Dario` / `Pulgar` references identify canonical `Dario Arturo Pulgar-Smith`, with the memoir using shorter work-context forms.

Literal evidence:

- The canonical page `wiki/people/dario-arturo-pulgar-smith.md` gives preferred name `Dario Arturo Pulgar-Smith` from family-supplied knowledge and identifies him as Alexander John Heinz's maternal grandfather.
- That page warns that Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records should be attached only after identity review.
- The assigned passages name only `Dario` and `Pulgar`; same-document context names `Dario Pulgar`.
- The assigned draft contains no `Arturo`, no `Smith`, and no family relationship.

Interpretation:

- This hypothesis is plausible only through an evidence chain: first prove the assigned Habitat `Dario`/`Pulgar` passages belong to the same Habitat `Dario Pulgar`; then prove that Habitat `Dario Pulgar` is the staged CV subject `Dario Arturo Pulgar`; then prove that `Dario Arturo Pulgar` and canonical `Dario Arturo Pulgar-Smith` are the same person or controlled surname variants.
- Family context justifies the targeted comparison, not silent normalization from `Pulgar` to `Pulgar-Smith`.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.50 | Name and occupational context are suggestive, but the canonical surname and middle name are absent. |
| conflict_severity | 0.48 | Wrong canonical attachment would create public biography error. |
| evidence_quality | 0.52 | Canonical side is family-supplied; target source gives only partial names. |
| conversion_confidence | 0.56 | Literal words are mostly supported, but citation QA is unresolved. |
| claim_probability | 0.54 | Plausible, not ready. |
| relevance | 0.96 | Main possible canonical destination. |
| canonical_readiness | 0.10 | Do not merge, rename, or promote. |

## Hypothesis 4: Same Person As Dario Jose Pulgar-Arriagada / Dario Pulgar Arriagada

Hypothesis: The Habitat references are to `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, or another Pulgar-Arriagada cluster.

Literal evidence:

- Existing canonical `wiki/people/dar-o-pulgar-arriagada.md` records `Darío Pulgar Arriagada` in a 5 December 2000 Serviu Región del Bío Bío expropriation notice.
- Other local identity analyses preserve separate staged Pulgar-Arriagada or `Dario Jose Pulgar-Arriagada` clusters, including metadata-dependent or held sources.
- The assigned Habitat draft has no `Jose`, no `Arriagada`, no `Pulgar A.`, no medical/surgeon context, no property/expropriation context, no parentage, and no age.
- The assigned passages are 1975-1976 Habitat AV Programme work-context references.

Interpretation:

- Name overlap alone is insufficient. The Habitat worker should remain separate or unresolved relative to Pulgar-Arriagada clusters unless a proof-reviewed source supplies full-name, date, relationship, or continuous-biography evidence.
- Current evidence favors anti-conflation rather than a same-person finding.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.14 | Only broad Dario/Pulgar overlap appears. |
| conflict_severity | 0.72 | Merging by name alone risks conflating different generations or contexts. |
| evidence_quality | 0.46 | Compared Pulgar-Arriagada evidence is sparse, staged, or outside this source. |
| conversion_confidence | 0.46 | Several compared clusters remain held; this chunk also has page QA. |
| claim_probability | 0.12 | Low from the assigned draft. |
| relevance | 0.78 | Required Pulgar-line guardrail. |
| canonical_readiness | 0.03 | No merge or attachment supported. |

## Hypothesis 5: Relationship To Jose/Juana Parent Candidates

Hypothesis: Jose del Carmen Pulgar, Jose del Carmen Segundo Pulgar Arriagada, Juana Arriagada de Pulgar, or Juana de Dios Amagada de Pulgar connect the assigned Habitat person into a Pulgar lineage.

Literal evidence:

- Existing wiki pages include `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.
- Those pages are tied to separate register-derived evidence clusters, some with draft or low-confidence relationship status and conversion-review concerns.
- The assigned Habitat draft contains no Jose, no Juana, no parent, no spouse, no child, no sibling, no household, and no lineage statement.

Interpretation:

- Jose/Juana candidates are a double-check list only. They do not bridge this Habitat `Dario`/`Pulgar` evidence to any Pulgar-line parentage claim.
- No relationship should be inferred from the Pulgar surname element or from family context alone.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.06 | No direct identity or kinship bridge appears. |
| conflict_severity | 0.60 | Unsupported lineage attachment would create false relationships. |
| evidence_quality | 0.40 | Parent-candidate evidence is separate and includes unresolved readings. |
| conversion_confidence | 0.40 | Related register readings and this Habitat citation both have QA limits. |
| claim_probability | 0.05 | Very low from this staged conflict draft. |
| relevance | 0.62 | Relevant only as required Pulgar-line context. |
| canonical_readiness | 0.01 | No relationship action supported. |

## Conflicts

- Page-boundary conflict: high. The assigned chunk frontmatter says page 1, but the body contains page 4 and page 5 support for the assigned Dario/Pulgar claims, plus later page text.
- Source-verification conflict: medium-high. Page 4 was visually confirmed; page 5 was confirmed by original PDF text extraction because the rendered page 5 image was not present in this checkout.
- Same-person conflict: low within the Habitat source cluster if kept as an inference. Same-document full-name anchors make the `Dario` and `Pulgar` references likely to refer to Dario Pulgar.
- Duplicate-person risk: moderate-high across Pulgar clusters. The assigned draft should not be merged into `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Darío Pulgar Arriagada`, or passenger-list Dario stubs by name alone.
- Name-variant conflict: moderate. The assigned passages support only `Dario` and `Pulgar`; same-source context supports `Dario Pulgar`; no assigned passage proves `Arturo`, `Pulgar-Smith`, `Jose`, `Arriagada`, or `Pulgar A.`.
- Relationship-conflict evidence: none in this draft. No family relationship or Jose/Juana parent candidate is stated.
- Chronology-conflict evidence: none within the assigned passages. Cross-cluster chronology should still be used as an anti-conflation check before any broader Pulgar-line merge.

## Ranked Hypotheses

| rank | hypothesis | probability | next action |
|---:|---|---:|---|
| 1 | Same Habitat person as other `Habitat Revisited` Dario/Pulgar mentions | 0.86 | Reconcile page/chunk citation, then proof-review the Habitat same-source identity cluster. |
| 2 | Same person as staged CV subject `Dario Arturo Pulgar` | 0.70 | Compare only after Habitat page QA and proof-reviewed CV identity/title/work-history review. |
| 3 | Same person as canonical `Dario Arturo Pulgar-Smith` | 0.54 | Require explicit bridge from Habitat `Dario Pulgar` to `Dario Arturo Pulgar` and then to `Pulgar-Smith`. |
| 4 | Same as `Dario Jose Pulgar-Arriagada` / `Dario/Darío Pulgar Arriagada` | 0.12 | Preserve separately or unresolved unless a reviewed source supplies full-name/date/relationship continuity. |
| 5 | Connected to Jose/Juana parent candidates | 0.05 | No relationship action; revisit only with proof-reviewed lineage evidence. |

## Recommended Next Action

Keep `research/_staging/conflicts/chunk-a048d567968b-p0001-02-page-boundary-and-identity-qa.md` on hold. Do not merge people, rename canonical pages, promote facts, or attach these passages to `wiki/people/dario-arturo-pulgar-smith.md`.

The exact next proof-review step is conversion/page-boundary QA for `CHUNK-a048d567968b-P0001-02`: reconcile the authoritative chunk path and source-page references for the source page 4 Saturna `Dario` passage and source page 5 Vancouver `Pulgar` passage; obtain or regenerate the page 5 image through the normal conversion QA workflow; then proof-review the Habitat Dario/Pulgar cluster as a same-source identity inference. Only after that should a separate identity bridge review compare verified Habitat evidence to verified CV evidence for `Dario Arturo Pulgar` and, if supported, to canonical `Dario Arturo Pulgar-Smith`.
