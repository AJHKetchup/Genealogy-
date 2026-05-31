---
type: identity_conflict_analysis
status: complete
role: identity_researcher
worker: postconv-identity-analysis-20260531051213878
task_id: identity-analysis:research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260531040158454.md
staged_draft: research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260531040158454.md
source: raw/sources/CV of Dario Arturo Pulgar.pdf
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
conversion_job_page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
chunk_id: CHUNK-fb0a0000636f-P0005-01
page_reference: page 5
analysis_status: hold_for_conversion_qa
canonical_readiness: blocked
promotion_recommendation: hold_for_conversion_qa
---

# Identity/Conflict Analysis: CHUNK-fb0a0000636f-P0005-01 Page-Control Conflict

This note analyzes staged conflict draft `research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260531040158454.md`.

## Blockers First

1. The controlling page-5 transcription is unresolved. The assigned chunk file for `CHUNK-fb0a0000636f-P0005-01` preserves a 1979-1970 CV work-history sequence ending at `EDUCATION`; the conversion-job `page-0005.md` preserves a different 1999-1997 consulting-work sequence.
2. The source PDF `raw/sources/CV of Dario Arturo Pulgar.pdf` is absent locally, and no `page-0005.jpg`, `page-0005.jpeg`, or `page-0005.png` was found under the conversion-job directory. The physical page cannot be used here to choose between derivatives.
3. The chunk manifest duplicates `CHUNK-fb0a0000636f-P0005-01` with conflicting character counts and hashes. This metadata drift blocks proof-controlled chronology and identity attachment.
4. Neither derivative page-5 reading literally names the person in the page body. `Dario Arturo Pulgar` is supported only by document title/path and surrounding CV context.
5. Page 5 contains no literal `Pulgar-Smith`, `Jose`, `Juana`, `Arriagada`, parent, spouse, child, grandchild, birth, death, residence, or explicit family relationship statement.
6. No same-person merge, duplicate-person resolution, name-variant normalization, relationship claim, or canonical fact promotion is ready from this conflict note.

## Literal Evidence Reviewed

- Staged draft: records the source as `raw/sources/CV of Dario Arturo Pulgar.pdf`, source availability as false, low confidence, and `hold_for_conversion_qa`.
- Assigned chunk: reads as a CV page with 1979-1982 United Nations Centre for Human Settlements (HABITAT), 1974-1978 National Film Board of Canada, 1972-1973 Chile Films, and 1970-1972 CITELCO entries.
- Conversion-job page Markdown: reads as a CV page with 1999 PROFONANPE and TVE, 1998-1999 Arca Consulting/European Commission, and 1997-1998 Klohn Crippen and SNC Lavalin entries.
- Aggregate converted file: identifies the document as `CV of Dario Arturo Pulgar pages 4-9`, but page 5 remains internally conflicted because the same chunk/page control points to incompatible content.
- Canonical `wiki/people/dario-arturo-pulgar-smith.md`: represents `Dario Arturo Pulgar-Smith` from family-supplied knowledge and explicitly warns not to automatically merge similarly named Dario/Pulgar/Pulgar-Smith clusters.
- Canonical `wiki/people/dar-o-pulgar-arriagada.md`: preserves a separate `Darío Pulgar Arriagada` stub supported by a 2000 Chiguayante expropriation notice.
- Canonical Jose/Juana stubs exist in separate register-derived contexts; they are not named in this page-5 conflict.

## Hypothesis 1: Page 5 Belongs To Document-Level CV Subject `Dario Arturo Pulgar`

Supporting evidence:

- The document title/path and aggregate converted header identify the source as the CV of `Dario Arturo Pulgar`.
- Both competing page-5 derivatives are plausible CV work-history pages, so they likely belong somewhere in the same CV source set.

Conflicts and limits:

- The physical page cannot be checked, and the two derivatives cannot both be the same controlling page 5.
- Page-body identity is absent; the attribution is document-level, not a literal source reading from page 5.

Scores:

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.45 | Document context supports the subject, but page-local identity is absent and page control is broken. |
| conflict_severity | 0.88 | Conflicting page content blocks chronology and identity attachment. |
| evidence_quality | 0.32 | Derivative evidence only; physical source/image missing locally. |
| conversion_confidence | 0.15 | Two incompatible page-5 derivatives and duplicate manifest records. |
| claim_probability | 0.55 | Probable the source set concerns Dario Arturo Pulgar, not proved for either page-5 derivative. |
| relevance | 0.95 | Directly relevant to the assigned CV/Pulgar conflict. |
| canonical_readiness | 0.03 | Blocked until conversion QA certifies page control. |

## Hypothesis 2: `Dario Arturo Pulgar` Is Same Person As Canonical `Dario Arturo Pulgar-Smith`

Supporting evidence:

- The names share `Dario Arturo Pulgar`.
- The canonical Pulgar-Smith page is the family-supplied home for Alexander John Heinz's maternal grandfather and expects future source attachment after identity review.

Conflicts and limits:

- This page and the document title do not include `Smith`, a family relationship, a birth date, a spouse, a child, or any bridge to Alexander John Heinz.
- Family context can justify a targeted bridge review, but it cannot silently convert `Pulgar` to `Pulgar-Smith`.

Scores:

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.25 | Meaningful name overlap, but no direct bridge on the conflicted page. |
| conflict_severity | 0.70 | Premature attachment could misattribute a conflicted CV chronology to the canonical person. |
| evidence_quality | 0.24 | Mostly title/path plus family-supplied canonical context. |
| conversion_confidence | 0.15 | Page control is unresolved; conversion cannot support the bridge yet. |
| claim_probability | 0.30 | Plausible future bridge hypothesis only. |
| relevance | 0.95 | Directly relevant Pulgar-Smith comparison. |
| canonical_readiness | 0.00 | Do not attach or promote. |

## Hypothesis 3: Same Person As `Dario Jose Pulgar-Arriagada`

Supporting evidence:

- The broader Pulgar-line context includes a staged `Dario Jose Pulgar-Arriagada` candidate.
- The shared elements `Dario` and `Pulgar` justify comparison.

Conflicts and limits:

- The CV title uses `Arturo`, not `Jose`; page 5 does not include `Jose` or `Arriagada`.
- Existing `Dario Jose Pulgar-Arriagada` context is not a page-5 bridge and has its own identity-basis limits.

Scores:

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.06 | Shared first name/surname only. |
| conflict_severity | 0.76 | A name-only merge could collapse separate Pulgar generations or surname lines. |
| evidence_quality | 0.18 | No direct page-5 evidence for this identity. |
| conversion_confidence | 0.15 | Current page-control conflict prevents use. |
| claim_probability | 0.06 | Very weak same-person hypothesis. |
| relevance | 0.70 | Required anti-conflation comparison. |
| canonical_readiness | 0.00 | No merge or attachment. |

## Hypothesis 4: Same Person As `Dario/Darío Pulgar Arriagada`

Supporting evidence:

- Existing canonical context has a separate `Darío Pulgar Arriagada` stub.
- The names share `Dario/Darío Pulgar`.

Conflicts and limits:

- The canonical `Darío Pulgar Arriagada` evidence is a 2000 Chiguayante expropriation-notice cluster; this CV page gives no `Arriagada`, Chiguayante, property, age, residence, or family bridge.
- The page-control conflict means even the CV chronology on page 5 is not stable.

Scores:

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.07 | Shared given name and surname are insufficient. |
| conflict_severity | 0.72 | High duplicate-person and chronology risk if merged by name alone. |
| evidence_quality | 0.22 | The expropriation stub is separate evidence; page 5 supplies no bridge. |
| conversion_confidence | 0.15 | Page 5 cannot yet support chronology or identity. |
| claim_probability | 0.06 | Weak and unproved. |
| relevance | 0.74 | Required Pulgar-Arriagada comparison. |
| canonical_readiness | 0.00 | Keep separate. |

## Hypothesis 5: Page 5 Supports Jose/Juana Parent Candidates

Supporting evidence:

- Separate local context includes `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.
- Those names are relevant to a future Pulgar-line checklist.

Conflicts and limits:

- The staged page-5 draft and both derivative page-5 readings do not name Jose or Juana.
- There is no parent, child, spouse, household, birth-register, or lineage evidence on this CV page.

Scores:

| metric | score | rationale |
| --- | ---: | --- |
| identity_confidence | 0.01 | No same-person evidence. |
| conflict_severity | 0.62 | Unsupported lineage attachment would create serious relationship conflict. |
| evidence_quality | 0.10 | Only unrelated contextual existence of Jose/Juana stubs. |
| conversion_confidence | 0.15 | Page-control conflict remains; Jose/Juana names are absent anyway. |
| claim_probability | 0.01 | No relationship claim is supported. |
| relevance | 0.45 | Relevant only as required anti-conflation context. |
| canonical_readiness | 0.00 | No relationship action. |

## Conflict Summary

- Same-person conflict: unresolved between the document-level `Dario Arturo Pulgar` CV subject and canonical `Dario Arturo Pulgar-Smith`; no same-person conclusion is ready.
- Duplicate-person conflict: high risk if `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, or `Dario/Darío Pulgar Arriagada` are merged from this page-control conflict.
- Name-variant conflict: page 5 does not prove `Pulgar` as a shortened form of `Pulgar-Smith`, nor `Arturo` as compatible with `Jose`, nor `Pulgar` as equivalent to `Pulgar-Arriagada`.
- Relationship conflict: none supported. Jose/Juana parent candidates and the Alexander John Heinz grandparent relationship are outside this page's literal evidence.
- Chronology conflict: material. The assigned chunk's 1979-1970 sequence conflicts with the conversion-job page Markdown's 1999-1997 sequence; all page-5 work-history claims must remain held.

## Ranked Hypotheses

| rank | hypothesis | probability | action |
| ---: | --- | ---: | --- |
| 1 | The source set is a CV for document-level subject `Dario Arturo Pulgar` | 0.55 | Hold until page control is repaired. |
| 2 | The CV subject may be canonical `Dario Arturo Pulgar-Smith` | 0.30 | Require a separate identity-bridge proof review before attachment. |
| 3 | Same as `Dario/Darío Pulgar Arriagada` | 0.06 | Preserve as separate; no merge from page 5. |
| 4 | Same as `Dario Jose Pulgar-Arriagada` | 0.06 | Preserve as separate; compare only if future bridge evidence appears. |
| 5 | Page 5 supports Jose/Juana parent candidates | 0.01 | No relationship action. |

## Recommended Next Action

Keep the staged conflict draft on `hold_for_conversion_qa`. The exact next proof-review step is not identity promotion; it is conversion QA to restore or confirm the source PDF or authoritative rendered page-5 image, compare it against both derivative readings, repair the duplicate manifest/hash drift, and certify the controlling page-5 transcription.

After conversion QA certifies page control, run proof review on the accepted page-5 work-history claims. Only then run a separate identity-bridge review for `Dario Arturo Pulgar` versus `Dario Arturo Pulgar-Smith`, with explicit anti-conflation checks for `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, and Jose/Juana parent candidates. Do not merge, rename, normalize, or promote any relationship from this page-control conflict.
