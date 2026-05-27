---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260527070451502
task_id: identity-analysis:research/_staging/conflicts/conflict-chunk-fb0a0000636f-p0004-01-page-identity-and-manifest-qa.md
staged_conflict_draft: research/_staging/conflicts/conflict-chunk-fb0a0000636f-p0004-01-page-identity-and-manifest-qa.md
subject: "Dario Arturo Pulgar"
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
source_packet: "research/_staging/source-packets/chunk-fb0a0000636f-p0004-01-cv-dario-arturo-pulgar-work-history.md"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0004-chunk-01.md"
chunk_id: "CHUNK-fb0a0000636f-P0004-01"
page_reference: "page 4"
analysis_status: hold
promotion_recommendation: do_not_promote_until_page_identity_and_manifest_qa
---

# Identity And Conflict Analysis: Page 4 Dario Arturo Pulgar CV QA

## Blockers First

- The staged conflict draft `research/_staging/conflicts/conflict-chunk-fb0a0000636f-p0004-01-page-identity-and-manifest-qa.md` is supported as a procedural identity/provenance hold, not as a biographical contradiction.
- The page-4 chunk body does not print `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Pulgar-Smith`, `Dario Jose`, `Dario J.`, `Pulgar-Arriagada`, `Arriagada`, `Jose`, `Juana`, Alexander John Heinz, or any kinship relationship.
- The chunk manifest lists `CHUNK-fb0a0000636f-P0004-01` twice for page 4 with the same chunk path but different `chars` and `sha256` values. That creates a provenance blocker before claim promotion.
- The conversion-job manifest identifies page 4 and its rendered image path, but the conversion-job page statuses remain `todo`; this identity pass did not run conversion or visual page reread.
- Do not attach page-4 work-history claims to canonical `wiki/people/dario-arturo-pulgar-smith.md` until a proof-reviewed identity-bearing CV page or accepted local bridge connects the CV subject to that canonical person.
- Do not merge or treat as variants any `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, `Dario/Darío Pulgar Arriagada`, or Jose/Juana parent candidates based on this page alone.

## Literal Source Readings

From the current chunk text:

- Page 4 is a typed CV-style work-history page arranged in reverse chronological order.
- Literal entries include `1988-1989`, `Food and Agriculture Organisation of the United Nations (FAO)`, `Ndola, Zambia`, and `Training and Communication Advisor`.
- Literal entries include `1988`, `Canadian International Development Agency (CIDA)`, `Ethiopia`, and `Communication Consultant`.
- Literal entries include `1986 - 1987`, `Worldview International Foundation (WIF)`, `Rome, Italy`, and `Rural Communications and Extension Advisor`.
- Literal entries include `1982-1985`, `Independent communications consultant`, and `Canadian International Development Agency`.
- The page begins as a continuation from a prior entry: `Governorate and the design and implementation of a modified Training and Visit System of Extension...`

These are employment and project-context readings only. They do not state a birth, death, parent, spouse, child, grandchild, household, or same-person bridge.

## Interpretation Kept Separate

The source packet and file paths identify the larger document as `CV of Dario Arturo Pulgar.pdf`, so the work-history page is plausibly document-level evidence for a CV subject named `Dario Arturo Pulgar` after page-continuity and manifest QA. The page body itself is not identity-bearing. It cannot independently prove that the document-level CV subject is canonical `Dario Arturo Pulgar-Smith` or any Pulgar-Arriagada candidate.

## Hypotheses And Evidence

### 1. Page 4 Belongs To The Document-Level CV Subject Dario Arturo Pulgar

Hypothesis: the page-4 work-history entries belong to the document-level subject `Dario Arturo Pulgar`.

Supporting evidence:

- The source packet, converted file path, source path, and conversion-job title all identify the larger source as a CV of Dario Arturo Pulgar.
- The page content is consistent with a continuing CV work-history sequence.
- The work-history entries can coexist chronologically and do not create an internal date conflict.

Conflicting or limiting evidence:

- The page body does not print the subject's name.
- The page begins mid-entry, so identity attribution depends on document continuity from adjacent pages or title/front matter.
- Duplicate page-4 manifest entries with different hash metadata require provenance review.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.66 | Probable document-level attribution, but no page-local name. |
| conflict_severity | 0.58 | Procedural/provenance risk, not a direct biographical contradiction. |
| evidence_quality | 0.62 | Typed text and consistent metadata, weakened by duplicate manifest records. |
| conversion_confidence | 0.72 | Current transcription is coherent and reports no illegible text, but page image was not reread in this pass. |
| claim_probability | 0.70 | Likely page belongs to the titled CV after QA; not ready for promotion. |
| relevance | 0.93 | Directly relevant to Dario Arturo Pulgar work-history staging. |
| canonical_readiness | 0.30 | Hold until page identity and manifest QA are complete. |

### 2. Same Person As Canonical Dario Arturo Pulgar-Smith

Hypothesis: document-level `Dario Arturo Pulgar` in the CV is the same person as canonical `wiki/people/dario-arturo-pulgar-smith.md`.

Supporting evidence:

- Names overlap strongly: `Dario Arturo Pulgar` versus `Dario Arturo Pulgar-Smith`.
- Existing canonical context names `Dario Arturo Pulgar-Smith` as Alexander John Heinz's maternal grandfather from family-supplied knowledge.
- The canonical page itself anticipates identity review for records mentioning Dario, Pulgar, Pulgar-Arriagada, or Pulgar-Smith.

Conflicting or limiting evidence:

- The page-4 body does not name `Dario Arturo Pulgar-Smith` or `Smith`.
- This page gives no family relationship, vital event, residence anchor, or other bridge to Alexander John Heinz.
- Family-supplied canonical knowledge is useful context but does not replace documentary identity proof.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.46 | Plausible name-overlap hypothesis only; bridge is not proved here. |
| conflict_severity | 0.70 | High risk if occupational claims are attached to the canonical person without a bridge. |
| evidence_quality | 0.45 | Existing canonical context is family supplied; page 4 itself is not identity-bearing. |
| conversion_confidence | 0.72 | Conversion may support work history, not canonical identity. |
| claim_probability | 0.48 | Possible same person, but below promotion threshold. |
| relevance | 0.90 | Highly relevant if later bridged. |
| canonical_readiness | 0.18 | Not ready for canonical attachment. |

### 3. Same Person As Dario Jose Pulgar-Arriagada Or Darío J. Pulgar Arriagada

Hypothesis: CV subject `Dario Arturo Pulgar` is the same person as `Dario Jose Pulgar-Arriagada`, `Darío J. Pulgar Arriagada`, or a related medical-title identity cluster.

Supporting evidence:

- Local staged tasks and reviews preserve separate Pulgar-Arriagada comparison targets, including a `Darío J. Pulgar Arriagada` medical-title mention and `Dario Pulgar-Arriagada` health-service style references.
- The surname and given-name overlap justify comparison during proof review.

Conflicting or limiting evidence:

- Page 4 names none of these variants.
- `Arturo` and `Jose` / `J.` are not interchangeable on this evidence.
- `Pulgar-Smith` and `Pulgar-Arriagada` are not proven variants by this page.
- The page gives no age, medical title, parentage, or chronology bridge to an older medical/health-service cluster.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.08 | Name overlap only; no page-local bridge. |
| conflict_severity | 0.82 | Very high conflation risk if merged by name alone. |
| evidence_quality | 0.28 | Comparison target exists in local context, but this page offers no direct support. |
| conversion_confidence | 0.72 | Conversion confidence does not improve this identity bridge. |
| claim_probability | 0.07 | Preserve as separate unresolved cluster. |
| relevance | 0.45 | Relevant as an anti-conflation check. |
| canonical_readiness | 0.00 | Not ready; do not merge or promote. |

### 4. Same Person As Dario/Darío Pulgar Arriagada Or Dario Pulgar-Arriagada

Hypothesis: CV subject `Dario Arturo Pulgar` is the same person as a `Dario/Darío Pulgar Arriagada` or `Dario Pulgar-Arriagada` source cluster.

Supporting evidence:

- Pulgar surname and Dario given name overlap across local staged context.
- Some staged Pulgar notes explicitly require checking these candidates against one another.

Conflicting or limiting evidence:

- Page 4 does not include `Arriagada`, a medical or military title, a Chilean official role, parent names, or any vital details.
- The CV page represents professional communications roles in the 1980s, while some Pulgar-Arriagada context appears tied to older medical/title evidence. No chronological bridge is supplied here.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.10 | Only broad name overlap. |
| conflict_severity | 0.80 | High duplicate/variant-conflation risk. |
| evidence_quality | 0.30 | Local comparison context exists, but page-4 evidence is silent. |
| conversion_confidence | 0.72 | Current transcription does not state variant names. |
| claim_probability | 0.09 | Preserve separate pending direct bridge. |
| relevance | 0.42 | Relevant as a required Pulgar-line comparison. |
| canonical_readiness | 0.00 | Not ready. |

### 5. Jose/Juana Parent Candidate Connections

Hypothesis: page-4 evidence supports or conflicts with Jose/Juana parent candidates such as `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, or `Juana de Dios Amagada de Pulgar`.

Supporting evidence:

- Existing wiki and staging context include Jose/Juana Pulgar-line parent candidates.
- Those names are relevant anti-conflation comparison targets because Pulgar-line evidence is currently fragmented.

Conflicting or limiting evidence:

- Page 4 does not name Jose, Juana, parentage, birth registration, household, or family structure.
- It offers no evidence for whether any Jose/Juana candidate is a parent of a Dario candidate.

Scores:

| score | value | rationale |
| --- | ---: | --- |
| identity_confidence | 0.02 | No direct evidence on page 4. |
| conflict_severity | 0.55 | Moderate risk if family links are inferred from surname context. |
| evidence_quality | 0.05 | No page-local Jose/Juana evidence. |
| conversion_confidence | 0.72 | Current conversion is irrelevant to parent identification. |
| claim_probability | 0.01 | No supported parent-candidate claim from this page. |
| relevance | 0.25 | Contextual only. |
| canonical_readiness | 0.00 | Not ready. |

## Conflict Assessment

- Same-person conflict: unresolved between document-level `Dario Arturo Pulgar` and canonical `Dario Arturo Pulgar-Smith`; page 4 cannot resolve it.
- Duplicate-person risk: high if CV `Dario Arturo Pulgar` is merged with Pulgar-Smith or Pulgar-Arriagada clusters by name alone.
- Name-variant conflict: page 4 supports no page-local variant beyond document-context `Dario Arturo Pulgar`.
- Relationship conflict: no relationship evidence appears on this page.
- Chronology conflict: no internal work-history chronology conflict is visible; the listed 1982-1989 roles can coexist, though claims remain held for provenance/page QA.
- Conversion/provenance conflict: the duplicate page-4 chunk-manifest entries with different hashes are the controlling blocker for promotion.

## Ranked Hypotheses

| rank | hypothesis | probability | next proof-review step |
| ---: | --- | ---: | --- |
| 1 | Page 4 is document-level CV work-history evidence for `Dario Arturo Pulgar`. | 0.70 | Reconcile duplicate page-4 manifest entries and proof-review page 4 against the rendered page image/source PDF for continuity. |
| 2 | CV subject `Dario Arturo Pulgar` may be canonical `Dario Arturo Pulgar-Smith`. | 0.48 | Review an identity-bearing CV title/front-matter page or accepted local bridge that explicitly connects the CV subject to the canonical Pulgar-Smith person. |
| 3 | CV subject is the same as `Dario/Darío Pulgar Arriagada` or `Dario Pulgar-Arriagada`. | 0.09 | Keep separate; require a proof-reviewed record with compatible full name, age/chronology, occupation, and relationship/vital anchors. |
| 4 | CV subject is the same as `Dario Jose Pulgar-Arriagada` / `Darío J. Pulgar Arriagada`. | 0.07 | Keep separate; require a direct identity bridge before variant treatment. |
| 5 | Page 4 supports Jose/Juana parent candidates. | 0.01 | No action from this page; use only birth/register evidence after its own conversion QA and proof review. |

## Recommended Next Action

Hold the staged conflict draft from canonical promotion. The exact next step is page identity and manifest QA for `CHUNK-fb0a0000636f-P0004-01`: reconcile why the chunk manifest contains duplicate page-4 entries with different `chars` and `sha256` values, verify the current page-4 chunk against the rendered image or source PDF page, and confirm continuity from an identity-bearing CV page. Only after that should a proof-review worker decide whether the page-4 work-history claims can be promoted as document-level evidence for `Dario Arturo Pulgar`. A separate identity-bridge proof review is still required before attaching those claims to `wiki/people/dario-arturo-pulgar-smith.md` or any Pulgar-Arriagada/Jose/Juana cluster.
