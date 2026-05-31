---
type: identity_conflict_analysis
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260531004750573.md"
worker: postconv-identity-analysis-20260531021526319
staged_draft: "research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260531004750573.md"
source_path: "raw/sources/CV of Dario Arturo Pulgar.pdf"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md"
chunk_id: "CHUNK-fb0a0000636f-P0005-01"
page_reference: "page 5"
analysis_status: "hold_for_conversion_qa"
canonical_readiness: "hold"
---

# Identity/Conflict Analysis: CHUNK-fb0a0000636f-P0005-01 Page-Control Conflict

## Blockers

- Exact staged draft analyzed: `research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260531004750573.md`.
- This is a page-control conflict, not a stable identity proof. The assigned chunk and current aggregate converted file preserve a 1979-1970 work-history sequence, while the conversion-job page Markdown preserves a 1999-1997 consulting-work sequence.
- The expected physical-source controls are absent in the current workspace: `raw/sources/CV of Dario Arturo Pulgar.pdf`, the job-local staged PDF, and `page-images/page-0005.jpg` all tested absent.
- The chunk manifest lists duplicate `CHUNK-fb0a0000636f-P0005-01` entries for the same chunk path with different character counts and recorded hashes.
- Current observed hashes do not match recorded metadata: current chunk hash `D6EA4F611EE03000C11CBBA63246E95B55F8A421FCBC87D0D667E91F5C8D0B8D`; current aggregate converted-file hash `DA9EC0C3A0F604B4C0E827A2A733A0BA013DD60D86ABEA2B46490D9F8820D288`; current conversion-job page Markdown hash `B87BD19F16275A992482651063C280BFC303BC6B7B0CD30CFBC2843D6D5E692F`.
- Page 5 does not itself print `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, `Jose`, `Juana`, or any family relationship in either derivative reading.
- The canonical candidate `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied and explicitly warns that similarly named Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records require identity review before attachment.
- No external research was performed. No raw sources, converted Markdown, chunks, reviewed notes, or canonical wiki pages were edited.

## Literal Evidence

From the exact staged draft:

- Source title/path: `raw/sources/CV of Dario Arturo Pulgar.pdf`.
- Converted file: `raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md`.
- Chunk: `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md`.
- The staged draft reports that the assigned chunk preserves `1979 - 1982` HABITAT, `1974 - 1978` National Film Board of Canada, `1972 - 1973` Chile Films, and `1970 - 1972` CITELCO entries.
- The staged draft reports that conversion-job `page-markdown/page-0005.md` preserves a different page with `1999` PROFONANPE and Television Trust for the Environment, `1998 - 1999` Arca Consulting/European Commission, and `1997-1998` Klohn Crippen Consultants and SNC Lavalin Agriculture entries.

From inspected local derivatives:

- The current chunk file contains the 1979-1970 HABITAT/NFB/Chile Films/CITELCO sequence and ends with `EDUCATION`.
- The current aggregate converted file contains both the 1999-1997 sequence under page 5 and, later in the same aggregate file, the 1979-1970 sequence under another unlabeled repeated page metadata block.
- The current conversion-job page Markdown `page-markdown/page-0005.md` contains the 1999-1997 sequence and states that the final line is cut off.
- The job manifest expects `page-images/page-0005.jpg`, but the image file is not present locally.

Interpretation kept separate: both derivative readings may belong somewhere in the same CV, but this staged conflict does not establish which reading controls physical page 5.

## Hypothesis 1: Evidence Belongs To Document-Level CV Subject Dario Arturo Pulgar

Hypothesis: the competing page-5 derivatives are from a CV locally titled for `Dario Arturo Pulgar`, so any surviving work-history page belongs first to a document-level CV subject named `Dario Arturo Pulgar`.

Supporting evidence:

- The source title/path and converted-file title name `Dario Arturo Pulgar`.
- The competing derivative texts are internally consistent with a curriculum vitae work-history chronology.
- Existing staged CV identity analyses in this workspace treat `Dario Arturo Pulgar` as a document-level attribution where body pages do not repeat the personal name.

Conflicts and limits:

- The body of the disputed page does not name the person.
- Page control is unresolved; two different page-5 readings cannot both be promoted as the same page.
- A CV source is useful occupational evidence after QA, but it is not independent vital-event or kinship evidence.

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.66 | Local document metadata supports `Dario Arturo Pulgar`, but page-local identity and page control are absent. |
| conflict_severity | 0.82 | Wrong page control would attach the wrong occupational sequence to page 5 and downstream citations. |
| evidence_quality | 0.42 | Derivative text is readable, but the controlling source image/PDF and stable hashes are missing. |
| conversion_confidence | 0.22 | Duplicate manifest entries, hash drift, and missing page image block conversion confidence. |
| claim_probability | 0.64 | Probable as document-level CV context only. |
| relevance | 1.00 | Directly addresses the exact staged draft. |
| canonical_readiness | 0.03 | Hold for conversion QA before proof review or promotion. |

## Hypothesis 2: Controlling Page 5 Is The 1999-1997 Consulting Sequence

Hypothesis: authoritative physical page 5 is the conversion-job page Markdown sequence beginning with `1999` PROFONANPE/TVE and continuing through 1997-1998 consulting roles.

Supporting evidence:

- `page-markdown/page-0005.md` is the job page Markdown for page 5 and contains the 1999-1997 sequence.
- The aggregate converted file's labeled page-5 section also contains the 1999-1997 sequence.
- Earlier staged page-5 analyses in the workspace identify this same 1999 sequence as a page-5 candidate.

Conflicts and limits:

- The assigned chunk for `CHUNK-fb0a0000636f-P0005-01` currently contains the 1979-1970 sequence.
- The page image/PDF needed to adjudicate the physical page is absent.
- This hypothesis still does not identify a canonical person beyond document-level `Dario Arturo Pulgar`.

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.58 | If controlling, it is still document-level CV evidence, not page-local identity proof. |
| conflict_severity | 0.80 | Conflicts directly with the assigned chunk content. |
| evidence_quality | 0.46 | Two derivatives agree, but both are secondary to the missing image/PDF. |
| conversion_confidence | 0.26 | Page Markdown is clear, but page authority is not certified. |
| claim_probability | 0.52 | Plausible but not controlling without physical-page QA. |
| relevance | 0.96 | One of the two page-control candidates. |
| canonical_readiness | 0.02 | Not promotable. |

## Hypothesis 3: Controlling Page 5 Is The 1979-1970 HABITAT/NFB/Chile Films/CITELCO Sequence

Hypothesis: authoritative physical page 5 is the assigned chunk/current aggregate later block with HABITAT, National Film Board of Canada, Chile Films, and CITELCO entries.

Supporting evidence:

- The assigned chunk for this task contains the 1979-1970 sequence.
- The current aggregate converted file also contains that sequence.
- The sequence fits a CV chronology and is relevant to the broader Dario Pulgar work-history cluster.

Conflicts and limits:

- Conversion-job `page-markdown/page-0005.md` preserves different page-5 content.
- The aggregate converted file appears internally duplicated or misaligned around page metadata.
- The missing page image/PDF prevents certifying whether this sequence is page 5, another CV page, or a stale chunk artifact.

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.60 | If accepted, it likely belongs to the document-level CV subject, but not to a canonical identity by itself. |
| conflict_severity | 0.84 | Misnumbering this sequence would corrupt page-level citations and work-history chronology. |
| evidence_quality | 0.44 | Clear derivative text, weak provenance control. |
| conversion_confidence | 0.24 | Manifest duplication and missing physical controls dominate. |
| claim_probability | 0.50 | Plausible as real CV content, unproved as page 5. |
| relevance | 0.98 | The assigned chunk's candidate reading. |
| canonical_readiness | 0.02 | Not promotable. |

## Hypothesis 4: Same Person As Canonical Dario Arturo Pulgar-Smith

Hypothesis: document-level `Dario Arturo Pulgar` in this CV is the same person as canonical `Dario Arturo Pulgar-Smith`, with the CV using a shorter surname form.

Supporting evidence:

- The name elements `Dario Arturo` and `Pulgar` align with canonical `Dario Arturo Pulgar-Smith`.
- The canonical page represents Alexander John Heinz's maternal grandfather from family-supplied knowledge.
- Existing staged CV notes identify `wiki/people/dario-arturo-pulgar-smith.md` as a likely candidate to test.

Conflicts and limits:

- Neither competing page-5 derivative states `Smith`, `Pulgar-Smith`, Alexander John Heinz, a parent, spouse, child, grandchild, birth data, or other direct bridge.
- The canonical page warns against attaching Dario/Pulgar records without identity review.
- Family context justifies a double-check; it does not justify silently normalizing `Dario Arturo Pulgar` to `Dario Arturo Pulgar-Smith`.

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.48 | Plausible name overlap, weakened by page-control failure and absent surname/family bridge. |
| conflict_severity | 0.58 | Premature attachment would misattribute unstable CV claims to a family-supplied canonical person. |
| evidence_quality | 0.34 | Evidence is name overlap plus local family context, not a direct source statement. |
| conversion_confidence | 0.22 | Conversion conflict does not resolve the name-variant question. |
| claim_probability | 0.46 | Possible, unproved. |
| relevance | 0.94 | Main canonical candidate for the CV subject. |
| canonical_readiness | 0.01 | No merge, rename, or fact attachment. |

## Hypothesis 5: Same Person As Dario Jose Pulgar-Arriagada / Dario Pulgar Arriagada

Hypothesis: document-level `Dario Arturo Pulgar` is the same person as `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario/Dario Pulgar Arriagada`, or canonical `wiki/people/dar-o-pulgar-arriagada.md`.

Supporting evidence:

- Existing local context includes Pulgar-Arriagada candidates and a canonical `Dario Pulgar Arriagada` stub.
- The names share broad `Dario` and `Pulgar` elements.

Conflicts and limits:

- This staged draft and both derivative page readings contain no `Jose`, `J.`, `Arriagada`, `Pulgar-Arriagada`, or `Pulgar A.` reading.
- The canonical `Dario Pulgar Arriagada` stub currently preserves a narrow 2000 expropriation event, not CV work-history or family-bridge evidence.
- Older Pulgar-Arriagada medical, delegate, passenger, or property clusters must not be collapsed into this CV subject by name alone.

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.10 | Only broad name overlap exists. |
| conflict_severity | 0.86 | Name-only merge could collapse distinct generations, careers, and surname lines. |
| evidence_quality | 0.30 | Compared evidence is separate and not cited by this page. |
| conversion_confidence | 0.20 | Current page conflict plus separate Pulgar-Arriagada QA limits. |
| claim_probability | 0.08 | Low on current local evidence. |
| relevance | 0.88 | Required Pulgar-line anti-conflation comparison. |
| canonical_readiness | 0.00 | Do not attach or merge. |

## Hypothesis 6: Relationship To Jose/Juana Parent Candidates

Hypothesis: Jose del Carmen Pulgar, Jose del Carmen Segundo Pulgar Arriagada, Juana Arriagada de Pulgar, Juana de Dios Amagada de Pulgar, or related Jose/Juana candidates connect this CV subject to the Pulgar line.

Supporting evidence:

- Existing canonical wiki context contains Jose/Juana Pulgar-line candidates, including `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.
- Some staged relationship notes elsewhere preserve Jose/Juana parent-child readings for separate register-derived clusters.

Conflicts and limits:

- The exact staged draft and both page-5 derivative readings contain no Jose or Juana name.
- No parent, child, spouse, household, birth-register, or lineage statement appears in the evidence for this task.
- Jose/Juana context can guide future checks only; it cannot bridge the CV subject to a family cluster here.

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.03 | No direct identity or kinship bridge appears. |
| conflict_severity | 0.66 | Unsupported lineage attachment would create relationship conflicts. |
| evidence_quality | 0.24 | Parent-candidate evidence is outside this staged draft and separately unresolved. |
| conversion_confidence | 0.20 | This page does not bear on those register readings. |
| claim_probability | 0.03 | No relationship claim is supported by this task. |
| relevance | 0.58 | Relevant only as required anti-conflation context. |
| canonical_readiness | 0.00 | No relationship action supported. |

## Conflicts

- Same-person conflict: unresolved between document-level `Dario Arturo Pulgar` and canonical `Dario Arturo Pulgar-Smith`.
- Duplicate-person risk: moderate for `Dario Arturo Pulgar` versus `Dario Arturo Pulgar-Smith`; high if merged by name alone with `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario/Dario Pulgar Arriagada`, `Dario Pulgar Arriagada`, or Jose/Juana parent clusters.
- Name-variant conflict: this staged draft supports only document-level `Dario Arturo Pulgar` from file/title context. It does not prove `Pulgar-Smith`, `Pulgar-Arriagada`, `Dario Jose`, `Dario J.`, or Jose/Juana variants.
- Relationship-conflict evidence: none in this staged draft. No parent, spouse, child, grandchild, or Alexander John Heinz relationship is stated.
- Chronology-conflict evidence: the page-control conflict creates a chronology-placement problem for page 5: either a 1999-1997 sequence or a 1979-1970 sequence may be the controlling page. Cross-cluster chronology also argues against merging with older Pulgar-Arriagada or Jose/Juana clusters by name alone.
- Conversion/provenance conflict: missing source/image controls, duplicate chunk manifest rows, and hash drift block all claim promotion.

## Ranked Hypotheses

| rank | hypothesis | probability | required next step |
|---:|---|---:|---|
| 1 | Evidence belongs somewhere in the document-level CV for `Dario Arturo Pulgar` | 0.64 | Restore authoritative source/page image and certify page/chunk provenance. |
| 2 | Controlling page 5 is the 1999-1997 consulting sequence | 0.52 | Compare physical page 5 against `page-markdown/page-0005.md`, aggregate converted file, and chunk manifest. |
| 3 | Controlling page 5 is the 1979-1970 HABITAT/NFB/Chile Films/CITELCO sequence | 0.50 | Compare physical page 5 against assigned chunk and aggregate converted file. |
| 4 | Same person as canonical `Dario Arturo Pulgar-Smith` | 0.46 | After conversion QA, run a separate identity-bridge proof review from `Dario Arturo Pulgar` to `Pulgar-Smith`. |
| 5 | Same as `Dario Jose Pulgar-Arriagada` / `Dario J. Pulgar Arriagada` / `Dario/Dario Pulgar Arriagada` | 0.08 | Preserve separately; require explicit reviewed full-name/date/relationship bridge before comparison can advance. |
| 6 | Connected to Jose/Juana parent candidates | 0.03 | No action from this draft; revisit only with relationship-bearing evidence. |

## Recommended Next Action

Keep `research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260531004750573.md` and all page-5 claims on `hold_for_conversion_qa`.

Exact next proof-review/promotion sequence:

1. Restore or regenerate authoritative access to `raw/sources/CV of Dario Arturo Pulgar.pdf` or the rendered `page-images/page-0005.jpg`.
2. Compare the physical page 5 against both derivative readings: the 1999-1997 conversion-job page Markdown and the 1979-1970 assigned chunk/current aggregate sequence.
3. Repair or supersede the duplicate `CHUNK-fb0a0000636f-P0005-01` manifest rows and reconcile current hash drift.
4. Only after page control is certified, rerun proof review for surviving page-5 occupational claims as document-level `Dario Arturo Pulgar` CV evidence.
5. Run a separate identity-bridge proof review before attaching any accepted CV claim to `wiki/people/dario-arturo-pulgar-smith.md` or any Pulgar-line canonical family cluster.

Do not merge people, rename canonical pages, promote facts, or infer Jose/Juana relationships from this staged draft.
