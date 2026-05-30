---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260530213419489.md
worker: postconv-identity-analysis-20260530221149657
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
created_at: 2026-05-30T22:11:49Z
---

# Identity/Conflict Analysis: CHUNK-fb0a0000636f-P0005-01

## Blockers

- Exact staged draft analyzed: `research/_staging/conflicts/chunk-fb0a0000636f-p0005-01-page-control-conflict-postconv-evidence-extraction-20260530213419489.md`.
- The controlling page-5 transcription is unresolved. The assigned chunk contains the `1979 - 1982` through `1970 - 1972` HABITAT/NFB/Chile Films/CITELCO sequence, while the conversion job `page-markdown/page-0005.md` contains the `1999`, `1998 - 1999`, and `1997-1998` PROFONANPE/TVE/Arca/Klohn Crippen/SNC Lavalin sequence.
- The source packet reports hash drift: the chunk records converted SHA-256 `fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0`, but the observed converted SHA-256 is `da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288`.
- The chunk manifest repeats `CHUNK-fb0a0000636f-P0005-01` for the same path/page with different character counts and hashes.
- `raw/sources/CV of Dario Arturo Pulgar.pdf` and `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0005.jpg` are not present in this checkout, so this worker could not do independent visual proof review.
- Neither derivative page-5 text literally names `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar Arriagada`, `Darío Pulgar Arriagada`, Jose, Juana, Alexander John Heinz, or a kinship relationship.

## Literal Evidence

- Staged draft subject: `Dario Arturo Pulgar, document-level CV subject`.
- Source packet identity basis: `Dario Arturo Pulgar`, from the source title and document-level CV context; the page body does not repeat the full name.
- Assigned chunk literal work-history sequence:
  - `1979 - 1982`, United Nations Centre for Human Settlements (HABITAT), Nairobi, Kenya, Development Support Communications Officer.
  - `1974 - 1978`, National Film Board of Canada (NFB), Montreal, Canada, Audio Visual Consultant.
  - `1972 - 1973`, Chile Films, Santiago, Chile, General Manager Distribution and Exhibition, Head of International Department.
  - `1970 - 1972`, Cine, Television y Comunicaciones (CITELCO), Santiago, Chile, Producer.
- Conversion job page Markdown literal work-history sequence:
  - `1999`, National Trust Fund for Protected Areas in Peru (PROFONANPE), Peru, Consultant.
  - `1999`, Television Trust for the Environment (TVE), London, England, Consultant.
  - `1998 - 1999`, Arca Consulting/European Commission, Lesotho, Team Leader.
  - `1997-1998`, Klohn Crippen Consultants, Huaraz, Peru, Socio-economic Consultant, followed by SNC Lavalin Agriculture, Maracaibo, Venezuela, Training Consultant.
- Canonical `wiki/people/dario-arturo-pulgar-smith.md` is family-supplied and explicitly warns not to automatically merge similarly named Dario/Pulgar records.
- Canonical `wiki/people/dar-o-pulgar-arriagada.md` is a separate stub with a 2000-12-05 expropriation-event evidence snapshot for `Darío Pulgar Arriagada`.
- Other staged context has a `Dario Jose Pulgar-Arriagada` portrait packet where the name comes from source title/path only, and a separate 1929 Chile listing packet naming `Dario Pulgar-Arriagada` as a Captain of the Health Service. Those materials are relevant anti-conflation context but do not bridge this CV page-5 conflict.
- Existing wiki context has Jose/Juana parent candidates, including `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar`, but this page-5 evidence does not name parents.

## Hypotheses

### H1: The assigned chunk is the controlling page 5 of the CV for document-level `Dario Arturo Pulgar`

Supporting evidence:

- The assigned chunk front matter identifies source `raw/sources/CV of Dario Arturo Pulgar.pdf`, page start/end 5, and chunk id `CHUNK-fb0a0000636f-P0005-01`.
- The HABITAT/NFB/Chile Films/CITELCO sequence is coherent CV work-history content.
- The aggregate converted file includes the same 1979-1970 section.

Conflicting evidence:

- The conversion job page Markdown for `page-0005.md` gives a different page-5 transcription.
- Manifest duplication, hash drift, missing page image, and missing PDF prevent selecting this derivative text as controlling.

Probability: 0.46. Identity confidence: 0.55 for document-level `Dario Arturo Pulgar`; 0.25 for canonical attachment.

### H2: The conversion job page Markdown is the controlling page 5 of the CV for document-level `Dario Arturo Pulgar`

Supporting evidence:

- The file is explicitly `page-markdown/page-0005.md` with metadata for page 5 of `CV of Dario Arturo Pulgar.pdf`.
- The 1999/1998 sequence coherently follows the page-4 chronology ending with 2000 and 1999-2000 entries.

Conflicting evidence:

- The assigned chunk and aggregate converted file also associate the 1979-1970 sequence with the same page/chunk identifier.
- The same manifest/hash/page-image blockers prevent selecting this derivative text as controlling.

Probability: 0.49. Identity confidence: 0.55 for document-level `Dario Arturo Pulgar`; 0.25 for canonical attachment.

### H3: Both derivative texts belong somewhere in the same Dario Arturo Pulgar CV, but page assignment/chunking is corrupted

Supporting evidence:

- Both texts are plausible CV work-history content and fit a reverse-chronology professional record.
- The aggregate converted file contains both sequences under problematic page metadata.
- Duplicate manifest entries and hash drift fit a provenance/page-control problem better than a same-person contradiction.

Conflicting evidence:

- Without the page image or source PDF, the physical order and exact page-5 text cannot be certified.

Probability: 0.72. Confidence: 0.62.

### H4: Document-level `Dario Arturo Pulgar` is the same person as canonical `Dario Arturo Pulgar-Smith`

Supporting evidence:

- Strong name overlap: `Dario Arturo Pulgar`.
- The canonical Pulgar-Smith page is the expected family-supplied candidate for Pulgar-line review.

Conflicting evidence:

- The page body does not state `Smith`, birth/death data, family relationships, Alexander John Heinz, spouse/child context, or any independent bridge identifier.
- The canonical page warns against automatic merges by name.
- The immediate conflict is conversion/page control, not identity proof.

Probability: 0.43 from this page alone. Confidence: low. Required next step: after page-control QA, run a separate identity-bridge proof review using the full CV title/opening pages and canonical Pulgar-Smith evidence.

### H5: Document-level `Dario Arturo Pulgar` is the same person as `Dario Jose Pulgar-Arriagada`, `Dario Pulgar-Arriagada`, `Dario Pulgar Arriagada`, or `Darío Pulgar Arriagada`

Supporting evidence:

- Name overlap at `Dario` and `Pulgar` makes these legitimate anti-conflation candidates.
- Workspace context has separate staged or canonical evidence for `Dario Jose Pulgar-Arriagada`, `Dario Pulgar-Arriagada`, and `Darío Pulgar Arriagada`.

Conflicting evidence:

- This staged draft and page-5 evidence do not include `Jose`, `J.`, `Arriagada`, `Pulgar-Arriagada`, a health-service/military title, Geneva convention context, property context, or parentage.
- Existing canonical context keeps `Dario Arturo Pulgar-Smith` and `Darío Pulgar Arriagada` separate.

Probability: 0.08 from this page alone. Confidence: very low. Required next step: do not merge; compare only in a later identity-bridge proof review that uses evidence naming both identity clusters.

### H6: Jose/Juana parent candidates connect to this page-5 CV subject

Supporting evidence:

- Existing wiki context has `Jose del Carmen Pulgar` and `Juana Arriagada de Pulgar` candidates elsewhere in the Pulgar line.

Conflicting evidence:

- This page-5 conflict contains no father, mother, parent, spouse, child, household, birth, or registration evidence.
- Family-context hints cannot correct or extend the literal CV page reading.

Probability: 0.02 from this page alone. Relationship confidence: very low. Required next step: no parent claim from this evidence; use separate relationship proof review only when a source names the relationship.

## Conflict Assessment

- Same-person conflict: unresolved and not directly adjudicable from this page. Document-level `Dario Arturo Pulgar` is the only named subject candidate, and canonical `Dario Arturo Pulgar-Smith` remains an unproved attachment.
- Duplicate-person conflict: not established. Do not merge `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, or Jose/Juana candidates from this evidence.
- Name-variant conflict: possible as a research question only. Page 5 does not provide literal name variants.
- Relationship conflict: none proved. No Jose/Juana/Alexander relationship claim appears in the page-5 materials.
- Chronology conflict: high derivative-work-history conflict. Two different work-history sequences are assigned to page 5; this blocks all page-5 chronology promotion until conversion QA establishes the controlling page.

## Scores

| field | score | judgment |
| --- | ---: | --- |
| identity_confidence | 0.55 | Moderate for document-level `Dario Arturo Pulgar` from CV title/context; low for any canonical person attachment. |
| conflict_severity | 0.86 | High page-control conflict blocks promotion of page-5 work-history claims. |
| evidence_quality | 0.38 | Derivative texts are readable, but controlling source/page image is unavailable and metadata conflicts. |
| conversion_confidence | 0.20 | Manifest duplication, hash drift, and absent page image make conversion control unreliable. |
| claim_probability | 0.49 | Either work-history sequence may belong to the CV, but exact page-5 claims are not established. |
| relevance | 0.99 | Directly addresses the assigned staged draft and referenced files. |
| canonical_readiness | 0.05 | Not ready for canonical facts, relationships, merges, page renames, or promotion. |

## Recommended Next Action

Keep the staged draft and source packet on `hold_for_conversion_qa`. The exact next proof-review step is to restore or regenerate `page-0005.jpg`, make the source PDF available, reconcile the duplicate manifest entries and hash drift, and compare the visible physical page 5 against both derivative transcriptions. After page control is certified, rerun proof review for the work-history claims.

Only after that QA should a separate identity-bridge proof review decide whether document-level `Dario Arturo Pulgar` attaches to canonical `Dario Arturo Pulgar-Smith` or remains separate from `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, and Jose/Juana parent clusters.

No raw sources, converted Markdown, chunks, source packets, staged claims, or canonical wiki pages were edited for this identity analysis.
