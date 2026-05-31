---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260531020015906
task_id: identity-analysis:research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260531010209483.md
staged_draft: research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260531010209483.md
source: raw/sources/CV of Dario Arturo Pulgar.pdf
source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-revision-postconv-evidence-extraction-20260531010209483.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
chunk_id: CHUNK-fb0a0000636f-P0005-01
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
conversion_job_page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
canonical_readiness: blocked
promotion_recommendation: hold_for_conversion_qa_then_identity_bridge
---

# Identity/Conflict Analysis: CV Page 5 Control Conflict

## Blockers First

1. Physical page control is unresolved. The assigned chunk for `CHUNK-fb0a0000636f-P0005-01` preserves a 1979-1970 work-history page. The conversion-job `page-markdown/page-0005.md` preserves a different 1999-1997 consulting-work page.
2. The recorded source PDF `raw/sources/CV of Dario Arturo Pulgar.pdf` is absent locally, and no authoritative page-5 image was available under the conversion-job directory for this task.
3. The source packet reports duplicate manifest metadata for the same chunk id, conflicting character counts and hashes, and observed converted/chunk hashes that do not match recorded metadata.
4. Neither derivative page-5 body independently names `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`.
5. No page-5 derivative states parents, spouse, children, `Jose`, `Juana`, `Smith`, `Arriagada`, or a relationship to Alexander John Heinz. Any family connection remains an identity-bridge question, not a page-5 fact.

## Literal Source Readings

Assigned chunk reading:

- `1979 - 1982`, United Nations Centre for Human Settlements (HABITAT), Nairobi, Kenya, Development Support Communications Officer.
- `1974 - 1978`, National Film Board of Canada (NFB), Montreal, Canada, Audio Visual Consultant.
- `1972 - 1973`, Chile Films, Santiago, Chile, General Manager Distribution and Exhibition, Head of International Department.
- `1970 - 1972`, Cine, Television y Comunicaciones (CITELCO), Santiago, Chile, Producer.
- The assigned chunk ends with `EDUCATION`.

Conversion-job page Markdown reading:

- `1999`, National Trust Fund for Protected Areas in Peru (PROFONANPE), Peru, Consultant.
- Television Trust for the Environment (TVE), London, England, Consultant.
- `1998 - 1999`, Arca Consulting/European Commission, Lesotho, Team Leader.
- `1997-1998`, Klohn Crippen Consultants, Huaraz, Peru, Socio-economic Consultant.
- SNC Lavalin Agriculture, Maracaibo, Venezuela, Training Consultant, with the final line continuing at page bottom.

Interpretation:

- These two readings cannot both be the controlling transcription for the same physical page 5 unless one derivative is mislabeled, stale, duplicated, or page-shifted.
- Both readings look like professional CV content for a document whose source title/path names `Dario Arturo Pulgar`, but page 5 itself does not provide an independent identity bridge to a canonical person.

## Ranked Hypotheses

| Rank | Hypothesis | Evidence supporting | Evidence against / limits | Identity confidence | Conflict severity | Evidence quality | Conversion confidence | Claim probability | Relevance | Canonical readiness |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | This is a page-control and derivative-integrity conflict, not a resolved identity event. | Staged draft and source packet report two competing derivative page-5 readings, absent source PDF/page image, duplicate chunk metadata, and hash drift. | The physical page cannot be checked in this task. | 0.93 | 0.90 | 0.78 | 0.10 | 0.92 | 0.96 | blocked |
| 2 | Page 5 belongs to a document-level `Dario Arturo Pulgar` CV cluster after conversion QA. | Source title/path and adjacent converted pages identify a CV of `Dario Arturo Pulgar`; both page-5 readings are plausible CV work-history content. | Page body does not repeat the subject name, and page control is unresolved. | 0.66 | 0.70 | 0.60 | 0.10 | 0.54 | 0.91 | hold |
| 3 | `Dario Arturo Pulgar` in this CV is the same person as canonical `Dario Arturo Pulgar-Smith`. | Canonical wiki context has a family-supplied maternal-grandfather profile named `Dario Arturo Pulgar-Smith`; the name overlap `Dario Arturo Pulgar` makes this a reasonable bridge target. | The staged draft does not state `Smith`, a family relationship, birth/death data, spouse, child, grandchild, or any direct identifier tying the CV subject to the canonical page. | 0.33 | 0.74 | 0.44 | 0.10 | 0.23 | 0.87 | blocked |
| 4 | The CV subject is the same as `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, or canonical `Darío Pulgar Arriagada`. | Existing local Pulgar context includes separate Arriagada name-form clusters; there is surname/given-name overlap on `Dario Pulgar`. | This staged draft does not mention `Jose`, `Arriagada`, `Pulgar-Arriagada`, medical occupation, parents, property records, or any direct bridge. Name overlap alone is insufficient. | 0.07 | 0.80 | 0.34 | 0.10 | 0.04 | 0.70 | blocked |
| 5 | Jose/Juana parent candidates connect to this page-5 CV subject. | Existing wiki/staged context contains Jose del Carmen Pulgar, Juana de Dios Amagada de Pulgar, and Juana Arriagada de Pulgar as Pulgar-line candidates requiring comparison. | Page 5 contains no Jose, Juana, parent, child, spouse, birth registration, or lineage statement. These candidates are checklist items only here. | 0.01 | 0.74 | 0.28 | 0.10 | 0.01 | 0.52 | blocked |

## Conflicts

- Same-person conflict: unresolved. The staged evidence cannot distinguish or merge `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, or `Dario/Dario Pulgar Arriagada`.
- Duplicate-person conflict: unresolved. No duplicate-person merge is supported from page 5.
- Name-variant conflict: unresolved. `Dario Arturo Pulgar` may be a document-level short form, but page 5 does not prove `Pulgar-Smith`, `Pulgar-Arriagada`, or `Jose`.
- Relationship conflict: absent in the page-5 evidence. No parent, spouse, child, grandchild, Jose, or Juana relationship is stated.
- Chronology conflict: procedural rather than biographical. The two competing page-5 readings describe different career periods on the same labeled page; both could exist elsewhere in a CV, but only one can control physical page 5.

## Scores

| Category | Score | Rationale |
| --- | ---: | --- |
| Identity confidence for document-level `Dario Arturo Pulgar` | 0.66 | Source title/path support the document subject; page body and page control do not independently confirm it. |
| Identity confidence for same as `Dario Arturo Pulgar-Smith` | 0.33 | Plausible family-context target only; no direct `Smith` or relationship bridge. |
| Identity confidence for same as `Dario Jose Pulgar-Arriagada` | 0.07 | No `Jose` or `Arriagada` appears in this staged draft. |
| Identity confidence for same as `Dario/Dario Pulgar Arriagada` | 0.07 | Name overlap is too thin, and existing canonical context keeps this as a separate stub. |
| Identity confidence for Jose/Juana parent attachment | 0.01 | No parent or lineage evidence appears on page 5. |
| Conflict severity | 0.90 | High for conversion control and promotion risk. |
| Evidence quality | 0.60 | Local derivative text is readable, but metadata integrity and physical control are compromised. |
| Conversion confidence | 0.10 | Source PDF/page image absence, duplicate manifest entries, and hash drift block reliance. |
| Claim probability that the assigned-chunk literal text exists locally | 0.96 | The assigned derivative chunk plainly contains the 1979-1970 entries. |
| Claim probability that assigned-chunk text controls physical page 5 | 0.34 | Plausible but unproved without image/manifest repair. |
| Claim probability that job page Markdown controls physical page 5 | 0.34 | Plausible but unproved for the same reason. |
| Relevance | 0.96 | The CV subject and Pulgar-line identity bridge are highly relevant. |
| Canonical readiness | 0.00 | No promotion, merge, rename, relationship attachment, or wiki update is ready. |

## Recommended Next Action

1. Conversion QA must restore or re-render the authoritative physical page 5 image and compare it against the assigned chunk, aggregate converted file, conversion-job page Markdown, and manifests.
2. Conversion QA must reconcile duplicate `CHUNK-fb0a0000636f-P0005-01` metadata and verify the source, converted-file, and chunk hashes.
3. After the controlling page-5 transcription is certified, run a separate identity-bridge proof review for the whole CV cluster. That review must compare `Dario Arturo Pulgar` against canonical `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, canonical `Darío Pulgar Arriagada`, and Jose/Juana parent candidates using direct identifiers, not name overlap.
4. Promote no page-5 occupational claim until the page-control issue is repaired. If either derivative reading is certified later, promote only narrow work-history/place claims after proof review and keep family identity attachment separate.

Current action: hold for conversion QA, then identity-bridge proof review. No canonical action is supported from this staged draft.
