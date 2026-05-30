---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260530213419489.md
worker: postconv-identity-analysis-20260530220607588
staged_draft: research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260530213419489.md
source: raw/sources/CV of Dario Arturo Pulgar.pdf
source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-work-history-hold-postconv-evidence-extraction-20260530213419489.md
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
conversion_job_page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
chunk_id: CHUNK-fb0a0000636f-P0005-01
page_reference: page 5
analysis_status: hold_for_conversion_qa
canonical_readiness: not_ready
promotion_recommendation: hold_for_conversion_qa
created_at: 2026-05-30T22:06:07Z
---

# Identity/Conflict Analysis: CHUNK-fb0a0000636f-P0005-01

## Blockers

- Exact staged draft analyzed: `research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260530213419489.md`.
- The page-control conflict is unresolved. The assigned chunk has the 1979-1970 HABITAT/NFB/Chile Films/CITELCO sequence, while the conversion job `page-markdown/page-0005.md` has the 1999/1998 PROFONANPE/TVE/Arca/Klohn Crippen/SNC Lavalin sequence.
- The source packet reports observed hash drift: converted SHA-256 recorded in the chunk is `fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0`, while the observed converted SHA-256 is `da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288`.
- The chunk manifest duplicates `CHUNK-fb0a0000636f-P0005-01` for the same path/page with different character counts and hashes.
- The expected rendered page image `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0005.jpg` is absent in this checkout.
- The raw source PDF `raw/sources/CV of Dario Arturo Pulgar.pdf` is absent in this checkout, so no independent visual page-control check was possible.
- The page body in either derivative text does not literally name `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, `Dario J. Pulgar Arriagada`, Jose, Juana, Alexander John Heinz, or any kinship relationship.

## Literal Evidence

- Staged draft subject: `Dario Arturo Pulgar, document-level CV subject`.
- Staged draft literal support: assigned chunk has `1979-1970 HABITAT/NFB/Chile Films/CITELCO text`; conversion job page Markdown has `1999/1998 PROFONANPE/TVE/Arca/Klohn Crippen/SNC Lavalin text`.
- Source packet source identity: `Dario Arturo Pulgar`, identified by source title and document-level CV context; the page body does not repeat the full name.
- Assigned chunk literal sequence: `1979 - 1982` United Nations Centre for Human Settlements (HABITAT), `1974 - 1978` National Film Board of Canada, `1972 - 1973` Chile Films, and `1970 - 1972` Cine, Television y Comunicaciones (CITELCO).
- Conversion job page Markdown literal sequence: `1999` National Trust Fund for Protected Areas in Peru (PROFONANPE), `Television Trust for the Environment (TVE)`, `1998 - 1999` Arca Consulting/European Commission, `1997-1998` Klohn Crippen Consultants, and SNC Lavalin Agriculture.
- Canonical wiki context has a family-supplied profile for `Dario Arturo Pulgar-Smith` as Alexander John Heinz's maternal grandfather, with an explicit note not to automatically merge similarly named Pulgar records.
- Canonical wiki context has a separate stub for `Dario Pulgar Arriagada` with a 2000-12-05 expropriation-event evidence snapshot. That page is not bridged here by the CV page-5 text.

## Hypotheses

### H1: The assigned chunk controls page 5 of the Dario Arturo Pulgar CV

Supporting evidence:

- The assigned chunk front matter identifies `CHUNK-fb0a0000636f-P0005-01`, source `raw/sources/CV of Dario Arturo Pulgar.pdf`, and page start/end 5.
- The aggregate converted file contains the same HABITAT/NFB/Chile Films/CITELCO text later in the file.
- The text is coherent CV work-history content and fits a reverse-chronology sequence if preceded by later roles and followed by education.

Conflicting evidence:

- The conversion job page Markdown for page 5 gives different later work-history content.
- Missing page image and missing PDF prevent visible proof review.
- Duplicate manifest entries and hash drift make page control unreliable.

Probability: 0.46. Confidence: low-moderate, blocked by conversion QA.

### H2: The conversion job page Markdown controls page 5 of the Dario Arturo Pulgar CV

Supporting evidence:

- The page Markdown is explicitly named `page-0005.md` and includes page metadata for page 5 of `CV of Dario Arturo Pulgar.pdf`.
- The 1999/1998 text follows the page-4 aggregate converted-file chronology that ends with 2000 and 1999-2000 entries.
- The text is coherent CV work-history content and appears to continue from page 4 into page 6.

Conflicting evidence:

- The assigned chunk and repeated aggregate converted-file section place the HABITAT/NFB/Chile Films/CITELCO sequence under the same page/chunk id.
- Duplicate manifest entries and hash drift prevent choosing the page Markdown as controlling without source-page QA.

Probability: 0.49. Confidence: low-moderate, blocked by conversion QA.

### H3: Both derivative texts belong somewhere in the same CV, but page 5 assignment is corrupted

Supporting evidence:

- Both texts are plausible work-history sections for a CV titled `Dario Arturo Pulgar`.
- The aggregate converted file includes both a 1999/1998 page-5 section and a later repeated page-metadata-less section with 1979-1970 entries.
- The manifest duplication and observed hash drift are consistent with a conversion/chunking provenance problem rather than a person-identity contradiction.

Conflicting evidence:

- Without the source PDF or page image, the exact physical page order cannot be certified.

Probability: 0.72. Confidence: moderate.

### H4: The CV subject `Dario Arturo Pulgar` is the same person as canonical `Dario Arturo Pulgar-Smith`

Supporting evidence:

- The names overlap strongly at `Dario Arturo Pulgar`.
- The canonical page says records mentioning Dario, Pulgar, Pulgar-Arriagada, or Pulgar-Smith should be attached only after identity review, so this is a proper follow-up candidate.

Conflicting evidence:

- The page body does not state `Smith`, family relationships, dates, Alexander John Heinz, or any bridge identifier.
- The staged conflict is about conversion/page control, not a direct identity bridge.

Probability: 0.43 for this page alone. Identity confidence: low. Hold pending separate identity-bridge proof review after conversion QA.

### H5: The CV subject is the same person as `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, or `Dario J. Pulgar Arriagada`

Supporting evidence:

- The broader workspace has separate Pulgar-Arriagada candidates and a canonical `Dario Pulgar Arriagada` stub.
- Name overlap at `Dario` and `Pulgar` justifies checking, but not merging.

Conflicting evidence:

- This staged draft and referenced page-5 materials do not state `Jose`, `J.`, `Arriagada`, `Pulgar-Arriagada`, medical title, convention/delegate role, expropriation property context, or parentage.
- Existing canonical context keeps `Dario Arturo Pulgar-Smith` and `Dario Pulgar Arriagada` separate.

Probability: 0.08 for this page alone. Identity confidence: very low. Do not merge or attach from this evidence.

### H6: Jose/Juana parent candidates connect to this page-5 CV subject

Supporting evidence:

- Existing wiki and staged materials contain Jose/Juana Pulgar-line candidates elsewhere.

Conflicting evidence:

- This page-5 conflict contains no parent, mother, father, spouse, child, household, or kinship language.
- The page-control problem must be solved before any biographical claim; parentage would still require a separate relationship proof review.

Probability: 0.02 for this page alone. Relationship confidence: very low. Unsupported from this staged draft.

## Conflict Assessment

- Same-person conflict: unresolved but not directly evidenced by this page. The only reasonable same-person candidate from this page is document-level `Dario Arturo Pulgar`; canonical `Pulgar-Smith` attachment remains unproved.
- Duplicate-person conflict: not established. Do not treat `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, and `Dario/Dario Pulgar Arriagada` as duplicates from this evidence.
- Name-variant conflict: possible only at a planning level. The page does not provide enough literal name data to adjudicate variants.
- Relationship conflict: none proved. No Jose/Juana/Alexander relationship claim is stated in the page-5 evidence.
- Chronology conflict: high at the derivative-page level because two different work-history sequences are assigned to page 5. This is a conversion/provenance chronology conflict, not a biological chronology conflict.

## Scores

| field | score | judgment |
| --- | ---: | --- |
| identity_confidence | 0.55 | Moderate for document-level `Dario Arturo Pulgar`; low for any canonical person attachment because the page body is unnamed. |
| conflict_severity | 0.86 | High page-control conflict blocks promotion of all page-5 work-history claims. |
| evidence_quality | 0.38 | Multiple derivative texts are readable, but raw PDF/page image are absent and manifest/hash evidence conflicts. |
| conversion_confidence | 0.20 | Page assignment is not reliable until source-page QA reconciles page Markdown, chunk, manifest, and hashes. |
| claim_probability | 0.49 | The work-history text probably belongs to the CV somewhere, but the exact page-5 claim is not established. |
| relevance | 0.99 | Analysis directly addresses the assigned staged draft and referenced artifacts. |
| canonical_readiness | 0.05 | Not ready for canonical facts, relationships, merges, or page renames. |

## Recommended Next Action

Keep this staged conflict and the associated source packet on `hold_for_conversion_qa`. The exact next proof-review/promotional step is: restore or regenerate `page-0005.jpg` and the source PDF access, reconcile the duplicate manifest entries and hash drift, compare the visible physical page 5 against both derivative transcriptions, then rerun proof review. Only after page control is certified should a separate identity-bridge proof review evaluate whether document-level `Dario Arturo Pulgar` can be attached to canonical `Dario Arturo Pulgar-Smith` or kept separate from Pulgar-Arriagada and Jose/Juana parent clusters.

No raw sources, converted Markdown, chunks, source packets, staged claims, or canonical wiki pages were edited for this identity analysis.
