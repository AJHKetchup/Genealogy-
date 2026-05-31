---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260531000652338.md
worker: postconv-identity-analysis-20260531001505918
staged_draft: research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260531000652338.md
source: raw/sources/CV of Dario Arturo Pulgar.pdf
source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-hold-postconv-evidence-extraction-20260531000652338.md
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
conversion_job_page_markdown: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md
chunk_id: CHUNK-fb0a0000636f-P0005-01
page_reference: page 5
analysis_status: hold_for_conversion_qa
canonical_readiness: not_ready
promotion_recommendation: hold_for_conversion_qa
created_at: 2026-05-31T00:15:05Z
---

# Identity/Conflict Analysis: CHUNK-fb0a0000636f-P0005-01

## Blockers

- Exact staged draft analyzed: `research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260531000652338.md`.
- Page control is unresolved. The assigned chunk/current aggregate converted file contain a 1979-1970 work-history page, while conversion-job `page-markdown/page-0005.md` contains a 1999-1997 consulting-work page.
- Source visibility is blocked in this checkout: `raw/sources/CV of Dario Arturo Pulgar.pdf`, `page-images/page-0005.jpg`, and `extracted-images/page-0005.jpg` are absent locally. I did not run conversion or source preparation.
- Provenance is blocked: the chunk manifest repeats `CHUNK-fb0a0000636f-P0005-01` for the same path/page with different character counts and hashes, and the source packet records observed hash drift against earlier metadata.
- Neither disputed page-5 body independently states `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, `Jose`, `Juana`, Alexander John Heinz, or a kinship relationship.
- This staged item cannot adjudicate parent candidates, same-person candidates, duplicate-person candidates, or canonical merges. It is a conversion-control conflict first.

## Literal Evidence Reviewed

- Staged conflict draft says the conflict is not yet a contradiction about Dario Arturo Pulgar's life history; it is a conversion-control conflict.
- Source packet identifies the document-level source as `CV of Dario Arturo Pulgar`, but says the assigned page body does not independently restate the subject's full name.
- Assigned chunk literal sequence: `1979 - 1982` HABITAT in Nairobi; `1974 - 1978` National Film Board of Canada in Montreal; `1972 - 1973` Chile Films in Santiago; `1970 - 1972` CITELCO in Santiago; then `EDUCATION`.
- Competing conversion-job page Markdown literal sequence: `1999` PROFONANPE in Peru; `1999` Television Trust for the Environment in London; `1998 - 1999` Arca Consulting/European Commission in Lesotho; `1997-1998` Klohn Crippen Consultants in Huaraz and SNC Lavalin Agriculture in Maracaibo.
- Canonical `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied and explicitly warns that Dario/Pulgar/Pulgar-Arriagada/Pulgar-Smith records should attach only after identity review.
- Canonical `wiki/people/dar-o-pulgar-arriagada.md` is a separate `Dario Pulgar Arriagada` stub with an evidence snapshot for a 2000-12-05 expropriation-resolution event.
- Canonical `wiki/people/dario-pulgar-adult-passenger-age-64.md` and `wiki/people/dario-pulgar-child-passenger-age-11.md` are separate Dario Pulgar passenger-list stubs.
- Canonical Jose/Juana context includes `wiki/people/jose-del-carmen-pulgar.md`, `wiki/people/jose-del-carmen-segundo-pulgar-arriagada.md`, `wiki/people/juana-arriagada-de-pulgar.md`, and `wiki/people/juana-de-dios-amagada-de-pulgar.md`, but this CV page-5 conflict names no parents.

No external research was performed. No raw sources, converted Markdown, chunks, source packets, staged claims, or canonical wiki pages were edited.

## Hypotheses

### H1: The conversion-job page Markdown controls physical page 5

Supporting evidence:

- `page-markdown/page-0005.md` labels itself page 5 for `CV of Dario Arturo Pulgar.pdf`.
- Its 1999-1997 sequence coherently follows page 4's 2000 and 1999-2000 entries in the aggregate converted file.
- The staged draft explicitly preserves this as one of the two derivative readings.

Conflicts:

- The assigned chunk and current aggregate converted file associate the same page/chunk id with a 1979-1970 work-history sequence.
- The source image and source PDF are absent locally, so the derivative cannot be source-certified in this identity pass.

Probability: 0.52. Identity confidence: 0.55 for document-level `Dario Arturo Pulgar`; 0.20 for canonical `Dario Arturo Pulgar-Smith` attachment.

### H2: The assigned chunk controls physical page 5

Supporting evidence:

- The assigned chunk front matter identifies `CHUNK-fb0a0000636f-P0005-01`, `page_start: 5`, and `page_end: 5`.
- The assigned chunk and source packet agree internally on the 1979-1970 HABITAT/NFB/Chile Films/CITELCO sequence.
- The aggregate converted file currently includes the same 1979-1970 sequence under page-5 metadata.

Conflicts:

- `page-markdown/page-0005.md` gives a materially different page-5 transcription.
- Duplicate manifest entries and hash drift make the assigned chunk unsafe as controlling evidence without conversion QA.

Probability: 0.46. Identity confidence: 0.55 for document-level `Dario Arturo Pulgar`; 0.20 for canonical `Dario Arturo Pulgar-Smith` attachment.

### H3: Both derivative texts belong somewhere in the CV, but page assignment/chunking is corrupted

Supporting evidence:

- Both derivative texts are plausible reverse-chronology CV work-history material.
- The dispute is better explained by page-control/provenance corruption than by a life-history contradiction.
- The manifest duplication and observed hash drift fit a stale or conflicting derivative-chain problem.

Conflicts:

- Without page images or the source PDF, this cannot be verified or repaired in identity analysis.

Probability: 0.72. Confidence: 0.64. This is the best current explanation, but it remains a hold item.

### H4: Document-level `Dario Arturo Pulgar` is the same person as canonical `Dario Arturo Pulgar-Smith`

Supporting evidence:

- The source title and conversion metadata consistently name `Dario Arturo Pulgar`.
- Canonical `Dario Arturo Pulgar-Smith` is the closest existing family-supplied candidate by given names and Pulgar surname.

Conflicts:

- Page 5 does not state `Smith`, a birth date, spouse, child, grandchild, Alexander John Heinz, or another identity bridge.
- The canonical page warns against automatic attachment by name.
- Page-control QA must precede use of this page's occupational chronology in any bridge argument.

Probability from this staged draft alone: 0.40. Identity confidence: low. Required next step: separate identity-bridge proof review after page-control QA.

### H5: Document-level `Dario Arturo Pulgar` is the same person as `Dario Jose Pulgar-Arriagada` or `Dario/Dario Pulgar Arriagada`

Supporting evidence:

- The shared `Dario` and `Pulgar` name elements justify explicit anti-conflation review.
- Existing workspace context has separate Dario/Pulgar-Arriagada candidates in convention, medical, passenger, and property contexts.

Conflicts:

- This staged draft does not contain `Jose`, `J.`, `Arriagada`, `Pulgar-Arriagada`, a medical/military title, Geneva context, parentage, or property context.
- Existing canonical context keeps `Dario Arturo Pulgar-Smith`, `Dario Pulgar Arriagada`, Dario Pulgar passenger stubs, and Jose/Juana clusters separate.

Probability from this staged draft alone: 0.08. Identity confidence: very low. Required next step: do not merge; compare only in a later bridge review that uses sources naming both clusters.

### H6: Jose/Juana parent candidates connect to this page-5 CV subject

Supporting evidence:

- The Pulgar-line context includes Jose del Carmen Pulgar and Juana-name parent candidates elsewhere.

Conflicts:

- This page-5 conflict contains no father, mother, parent, spouse, child, household, birth-registration, or relationship statement.
- Family-context hints cannot silently correct or extend the literal page reading.

Probability from this staged draft alone: 0.02. Relationship confidence: very low. Required next step: no parent claim from this evidence; use a separate relationship proof review only when a source names the relationship.

## Conflict Assessment

- Same-person evidence: insufficient for any canonical same-person conclusion.
- Duplicate-person evidence: no duplicate-person merge is supported.
- Name-variant evidence: `Dario Arturo Pulgar` may be a shortened form of `Dario Arturo Pulgar-Smith`, but this staged draft does not prove the variant.
- Relationship-conflict evidence: absent from the page-5 materials.
- Chronology-conflict evidence: severe at the derivative-control level. The 1999-1997 and 1979-1970 sequences cannot both be promoted as the same physical page-5 transcription.
- Conversion conflict: severe and controlling.

## Scores

| field | score | judgment |
| --- | ---: | --- |
| identity_confidence | 0.55 | Moderate only for document-level `Dario Arturo Pulgar`; low for any canonical person attachment. |
| conflict_severity | 0.90 | Page-control conflict could misplace multiple occupational and chronology claims. |
| evidence_quality | 0.38 | Derivative texts are readable, but source image/PDF control and manifest provenance are blocked. |
| conversion_confidence | 0.20 | Missing page images/PDF, duplicate manifest entries, and hash drift prevent certification. |
| claim_probability | 0.49 | Either work-history sequence may belong to the CV, but exact page-5 claims are not established. |
| relevance | 0.99 | Directly addresses the assigned staged draft and referenced files. |
| canonical_readiness | 0.05 | Not ready for canonical facts, relationships, merges, renames, or promotion. |

## Ranked Assessment

1. Preserve this as a conversion-control conflict and keep all page-5 claims on `hold_for_conversion_qa`.
2. Treat `Dario Arturo Pulgar` only as the document-level CV subject until page-control and identity-bridge review are complete.
3. Do not attach this page's claims to canonical `Dario Arturo Pulgar-Smith`.
4. Do not merge `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, Dario Pulgar passenger stubs, Jose del Carmen candidates, or Juana candidates from this evidence.

## Recommended Next Action

Current decision: `do_not_promote`; keep on `hold_for_conversion_qa`.

Exact next proof-review prerequisite:

1. Conversion/source-prep QA must restore or locate the authoritative source PDF and page-5 image.
2. QA must visually decide whether physical page 5 controls to `page-markdown/page-0005.md` with 1999-1997 entries or to `page-0005-chunk-01.md` with 1979-1970 entries.
3. QA must reconcile duplicate manifest entries and stale/observed hash differences.
4. After page control is certified, rerun proof review for the surviving work-history claims.
5. Only after that should a separate identity-bridge proof review decide whether document-level `Dario Arturo Pulgar` attaches to canonical `Dario Arturo Pulgar-Smith` or remains separate from Pulgar-Arriagada and Jose/Juana clusters.
