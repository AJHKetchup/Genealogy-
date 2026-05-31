---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260530234356813.md
worker: postconv-identity-analysis-20260531003045362
staged_draft: research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260530234356813.md
source_path: raw/sources/CV of Dario Arturo Pulgar.pdf
source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-hold-postconv-evidence-extraction-20260530234356813.md
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
chunk_id: CHUNK-fb0a0000636f-P0005-01
page_reference: page 5
conflict_type: page_control_conflict
analysis_status: hold
canonical_readiness: not_ready_conversion_qa_required
---

# Identity/Conflict Analysis: CHUNK-fb0a0000636f-P0005-01

## Blockers

- Exact staged draft analyzed: `research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260530234356813.md`.
- The blocker is primary: the assigned chunk and the conversion-job page Markdown disagree about what text controls physical page 5.
- Assigned chunk/current page-5 chunk text supports a 1979-1982 through 1970-1972 work-history page beginning with HABITAT in Nairobi and ending with CITELCO in Santiago plus an `EDUCATION` heading.
- Competing conversion-job page Markdown supports a different 1999 through 1997-1998 consulting-work page beginning with PROFONANPE in Peru and including TVE, Arca Consulting/European Commission, Klohn Crippen Consultants, and SNC Lavalin Agriculture.
- The source packet reports duplicate chunk-manifest entries for `CHUNK-fb0a0000636f-P0005-01`, conflicting character counts and hashes, observed converted/chunk hashes that differ from recorded metadata, and no available `page-images/page-0005.jpg` or `extracted-images/page-0005.jpg` in that evidence pass.
- Page 5 body, under either derivative reading, does not literally print the subject's full personal name. `Dario Arturo Pulgar` is document-level attribution from the source title/path and staging metadata.
- The canonical candidate `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied and explicitly warns that records mentioning Dario, Pulgar, Pulgar-Arriagada, or Pulgar-Smith should be attached only after identity review.
- This note does not edit raw sources, converted Markdown, chunks, source packets, or canonical wiki pages. No external research was performed.

## Hypothesis 1: Page 5 Belongs To The Document-Level CV Subject Dario Arturo Pulgar

Literal evidence:

- The source title/path and source packet identify the document as `CV of Dario Arturo Pulgar.pdf`.
- The staged draft subject is `Dario Arturo Pulgar`.
- Both competing derivative readings are CV-style work-history pages and are local derivatives of the same source package.
- Neither derivative page body independently restates `Dario Arturo Pulgar`.

Interpretation:

- The strongest identity conclusion is document-level only: whichever physical page-5 transcription is certified probably belongs to a CV locally titled for `Dario Arturo Pulgar`.
- Because the controlling text is unresolved, no page-5 occupational chronology should be treated as settled evidence yet.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.78 | Source title and staging metadata align, but page body is unnamed and page control is blocked. |
| conflict_severity | 0.86 | The two derivative texts describe different career periods and cannot both control the same physical page 5. |
| evidence_quality | 0.56 | Local metadata is useful, but derivative disagreement and hash drift lower reliability. |
| conversion_confidence | 0.12 | Conversion QA has not selected a controlling transcription and page image was unavailable in the evidence pass. |
| claim_probability | 0.76 | Probable document-level subject attribution, not proof of any specific page-5 job claim. |
| relevance | 1.00 | Directly matches the assigned staged conflict draft. |
| canonical_readiness | 0.05 | Not promotion-ready until conversion QA resolves page control and identity proof review follows. |

## Hypothesis 2: Same Person As Canonical Dario Arturo Pulgar-Smith

Literal evidence:

- The canonical page `wiki/people/dario-arturo-pulgar-smith.md` has preferred name `Dario Arturo Pulgar-Smith`.
- The canonical page states, from family-supplied knowledge, that Dario Arturo Pulgar-Smith is Alexander John Heinz's maternal grandfather.
- The CV document-level subject `Dario Arturo Pulgar` shares the given names `Dario Arturo` and surname element `Pulgar` with the canonical page.
- The staged draft and page-5 derivatives do not state `Smith`, `Pulgar-Smith`, Alexander John Heinz, a spouse, child, grandchild, birth date, or parent relationship.

Interpretation:

- Same-person identity is plausible but unproved. The page-control conflict weakens use of page 5 as an identity bridge because the exact page text is unsettled.
- Family context justifies a targeted proof-review double-check; it does not justify silently normalizing `Dario Arturo Pulgar` to `Dario Arturo Pulgar-Smith`.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.48 | Strong name overlap, but no `Pulgar-Smith` or family bridge in the staged page-5 evidence. |
| conflict_severity | 0.70 | Wrong attachment would promote disputed CV chronology to the family-supplied canonical person. |
| evidence_quality | 0.43 | Current support is name overlap plus canonical family context, not direct source identity. |
| conversion_confidence | 0.12 | Conversion blocker remains independent of the name-variant question. |
| claim_probability | 0.50 | Plausible but not established by this staged draft. |
| relevance | 0.96 | Required Pulgar-line canonical comparison. |
| canonical_readiness | 0.03 | Do not attach page-5 claims or merge identities from this evidence. |

## Hypothesis 3: Same Person As A Broader Dario Arturo Pulgar / Dario Pulgar CV Work-History Cluster

Literal evidence:

- Existing staged CV tasks for the same source ask reviewers to confirm that pages of `CV of Dario Arturo Pulgar.pdf` belong to the same CV subject and then decide whether the document-level subject should link to canonical `Dario Arturo Pulgar-Smith`.
- The assigned chunk reading has 1970-1982 film, NFB, and HABITAT roles.
- The competing page Markdown has 1997-1999/1999 consulting roles.
- Both derivative readings are professional CV entries, but they represent materially different chronological sections.

Interpretation:

- A broader CV work-history cluster for document-level `Dario Arturo Pulgar` is likely, but this specific page cannot currently be used to decide which work-history sequence belongs at page 5.
- Treat same-document continuity as a hypothesis pending conversion QA, not as proof of a settled career chronology.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.68 | Same-source CV context supports a cluster; page-control conflict prevents confident page-specific use. |
| conflict_severity | 0.82 | The chronology conflict changes which career period page 5 documents. |
| evidence_quality | 0.50 | Staged context is relevant, but the operative page is unstable. |
| conversion_confidence | 0.12 | Hash/manifest/page-image problems dominate. |
| claim_probability | 0.66 | Likely same CV cluster, but low certainty for individual page-5 facts. |
| relevance | 0.92 | Helps frame the CV subject identity without promoting facts. |
| canonical_readiness | 0.05 | Hold for conversion QA and subsequent proof review. |

## Hypothesis 4: Same Person As Dario Jose Pulgar-Arriagada / Dario Or Dario Pulgar Arriagada

Literal evidence:

- Existing local Pulgar-line context includes staged and canonical references to `Dario Jose Pulgar-Arriagada`, `Dario Pulgar-Arriagada`, `Dario Pulgar Arriagada`, and related abbreviated forms in other records.
- This staged page-control draft names only `Dario Arturo Pulgar` as document-level subject and does not include `Jose`, `Arriagada`, `Pulgar-Arriagada`, or `Pulgar Arriagada`.
- Page 5, under either derivative reading, is a modern professional CV work-history page and does not provide a parent, birth, spouse, child, military/medical-service, civil-register, or convention-delegate bridge to the Pulgar-Arriagada clusters.

Interpretation:

- Do not merge `Dario Arturo Pulgar` with any Pulgar-Arriagada candidate by name overlap. The current evidence supports only an anti-conflation warning.
- The exact next proof-review step for Pulgar-Arriagada comparison would require a reviewed identity-bearing source that explicitly bridges names, dates, relationships, or continuous biography between the CV subject and those records.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.10 | Shared `Dario`/`Pulgar` elements only; key name elements differ or are absent. |
| conflict_severity | 0.80 | Name-only merger could collapse distinct Pulgar-line people or generations. |
| evidence_quality | 0.38 | The relevant Pulgar-Arriagada evidence is external to this page and remains separately staged/reviewed. |
| conversion_confidence | 0.12 | Page 5 itself is not stable enough for cross-cluster linkage. |
| claim_probability | 0.09 | Low from this staged draft. |
| relevance | 0.85 | Required Pulgar-line anti-conflation comparison. |
| canonical_readiness | 0.00 | No merge, rename, or attachment supported. |

## Hypothesis 5: Relationship To Jose/Juana Parent Candidates

Literal evidence:

- Existing wiki context includes parent-candidate pages such as `Juana Arriagada de Pulgar`, `Juana de Dios Amagada de Pulgar`, and Pulgar entries involving Jose/Juana relationship questions.
- Other staged notes preserve unresolved readings for Pulgar birth-register material involving `Jose del Carmen Pulgar` / `Jose del C. Pulgar` and `Juana de Dios ... de Pulgar`.
- This exact page-control draft does not mention Jose, Juana, a parent, a child, a spouse, a birth record, or a family relationship.

Interpretation:

- Jose/Juana candidates are relevant only as an anti-conflation checklist. This page provides no relationship evidence tying them to the CV subject or to canonical `Dario Arturo Pulgar-Smith`.
- Do not infer parentage or lineage from surname context or family-context hints.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.05 | No direct identity or relationship bridge appears in this draft. |
| conflict_severity | 0.64 | Premature lineage attachment would create unsupported parent-child claims. |
| evidence_quality | 0.34 | Parent-candidate evidence belongs to separate, partly unresolved register work. |
| conversion_confidence | 0.12 | This page-control conflict adds no reliable kinship evidence. |
| claim_probability | 0.04 | Not supported by page-5 evidence. |
| relevance | 0.62 | Required Pulgar-line comparison context only. |
| canonical_readiness | 0.00 | No relationship action supported. |

## Conflicts

- Page-control conflict: assigned chunk/current chunk text and conversion-job page Markdown give incompatible page-5 transcriptions.
- Chronology conflict: one derivative sequence covers 1979-1982, 1974-1978, 1972-1973, and 1970-1972; the other covers 1999, 1998-1999, and 1997-1998.
- Name-variant conflict: the document-level subject is `Dario Arturo Pulgar`; this draft does not resolve `Pulgar` versus `Pulgar-Smith`, `Pulgar-Arriagada`, or `Pulgar Arriagada`.
- Same-person conflict: possible but unproved identity between the CV subject and canonical `Dario Arturo Pulgar-Smith`.
- Duplicate-person risk: high if the CV subject is merged by name alone with `Dario Jose Pulgar-Arriagada`, `Dario Pulgar-Arriagada`, `Dario Pulgar Arriagada`, or related Jose/Juana family clusters.
- Relationship-conflict evidence: none in this draft. No parent, spouse, child, grandchild, or Alexander John Heinz relationship is stated.

## Ranked Hypotheses

| rank | hypothesis | probability | action |
|---:|---|---:|---|
| 1 | Certified page 5, once selected, belongs to document-level CV subject `Dario Arturo Pulgar` | 0.76 | Hold until conversion QA identifies the controlling physical page-5 transcription. |
| 2 | Same broader CV work-history cluster for `Dario Arturo Pulgar` / `Dario Pulgar` | 0.66 | Reassess after page-control QA repairs manifest/hash drift. |
| 3 | Same person as canonical `Dario Arturo Pulgar-Smith` | 0.50 | Require a separate identity-bridge proof review from accepted local evidence. |
| 4 | Same person as `Dario Jose Pulgar-Arriagada` / `Dario Pulgar-Arriagada` / `Dario Pulgar Arriagada` | 0.09 | Preserve separately or unresolved; do not merge by name alone. |
| 5 | Related to Jose/Juana parent candidates | 0.04 | No relationship action from this draft. |

## Recommended Next Action

Keep the staged draft on `hold_for_conversion_qa`. The exact next proof-review step is conversion QA, not canonical identity promotion: restore or inspect the physical page-5 image/PDF page, choose the controlling transcription for `CHUNK-fb0a0000636f-P0005-01`, repair duplicate manifest/hash drift, and then rerun identity proof review against the certified page text.

After conversion QA, run a separate identity-bridge proof review before attaching any page-5 occupational claims to `wiki/people/dario-arturo-pulgar-smith.md`. That proof review must explicitly bridge `Dario Arturo Pulgar` to `Dario Arturo Pulgar-Smith` or keep the CV subject as a separate unresolved document-level identity. Continue to preserve anti-conflation checks for `Dario Jose Pulgar-Arriagada`, `Dario Pulgar-Arriagada`, `Dario Pulgar Arriagada`, and Jose/Juana parent candidates.
