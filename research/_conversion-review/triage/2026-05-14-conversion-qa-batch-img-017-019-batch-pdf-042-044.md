# Conversion QA Triage - 2026-05-14

Role: `conversion_qa_reviewer`
Branch context: `codex/local-codex-conversion-workbench`

## Sources Triaged

### `raw/converted/batch-img-017-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1888-entry-no.codex.md`

- Source reliability: High. Civil birth-register image with strong genealogical value.
- Conversion confidence: Moderate. The target entry is detailed, but two high-value name fields still look unstable.
- Recommended action: `reread-region`

Concerns:

1. Child given name may still drift.
   - Converted text: `Nombre: Fidelmiro Segundo Pulgar Arriagada`
   - Page/chunk reference: `Page 1`, entry 172 name line
   - Why it looks odd: `Fidelmiro` is plausible but uncommon, and the conversion itself notes a prior reread.
   - Possible alternate reading: `Fidemiro` or a nearby variant
   - Source reliability: High
   - Conversion confidence: Moderate
   - Recommended action: `reread-region`

2. Father's full name remains suspicious.
   - Converted text: `Nombre del padre: Juan de Casanova Pulgar`
   - Page/chunk reference: `Page 1`, entry 172 father line
   - Why it looks odd: `de Casanova` could be a true middle-name phrase, but it also reads like a segmentation or handwriting-resolution risk.
   - Possible alternate reading: `Juan Casanova Pulgar` or another `Juan de ... Pulgar` expansion
   - Source reliability: High
   - Conversion confidence: Moderate
   - Recommended action: `reread-region`

Notes:

- The rest of the target entry is coherent and structurally aligned.
- Neighboring entries are intentionally partial and do not block evidence extraction for entry 172.

### `raw/converted/batch-img-019-registro-de-nacimientos-circunscripci-n-de-los-ngeles-chile-1889-certificat.codex.md`

- Source reliability: High. Civil birth-register image with strong genealogical value.
- Conversion confidence: High for genealogically material fields; low only for the official signature.
- Recommended action: `pass`

Concerns:

1. Official signature remains uncertain.
   - Converted text: `Firma del oficial: Emilio Quiroga[?]`
   - Page/chunk reference: `Page 1`, entry 513 signature line
   - Why it looks odd: Surname ending is soft in the scan and not fully clean.
   - Possible alternate reading: `Emilio Quiroga`
   - Source reliability: High
   - Conversion confidence: High for the record body; low for the signature only
   - Recommended action: `pass`

Notes:

- Child, parents, date, place, and informant relationship are internally consistent.
- Signature uncertainty is low priority for genealogy extraction.

### `raw/converted/batch-pdf-042-c-mara-de-senadores-de-la-naci-n-1936-pages-1-5.codex.md`

- Source reliability: Unclear at the source-identity level.
- Conversion confidence: Low for source identity, moderate for literal reading of visible wrapper pages.
- Recommended action: `hold-for-human`

Concerns:

1. Source-title mismatch suggests wrong document, wrong slice, or bad source labeling.
   - Converted text: `LEY Y REGLAMENTO GENERAL DE LOS FERROCARRILES NACIONALES`
   - Page/chunk reference: `Page 5`
   - Why it looks odd: The converted source title says `Cámara de Senadores de la Nación, 1936 pages 1-5`, but the first substantive cover page is a railways regulation publication.
   - Possible alternate reading: None needed; the main issue is source identity, not line-level OCR.
   - Source reliability: Unclear until source identity is reconciled
   - Conversion confidence: Low
   - Recommended action: `hold-for-human`

2. Pages 1-4 appear to be wrapper or filing material with no Senate-specific confirmation.
   - Converted text: `BULKY DOCUMENT ENCLOSURE.` / `9A/31064/25420` / `Registry[?]`
   - Page/chunk reference: `Pages 1-4`
   - Why it looks odd: The job front matter looks like archival wrappers, but nothing in the visible text ties the slice to the titled Senate source.
   - Possible alternate reading: N/A
   - Source reliability: Unclear
   - Conversion confidence: Moderate for the visible words, low for source association
   - Recommended action: `hold-for-human`

Notes:

- This is primarily a source-prep or assembly problem, not just a transcription problem.
- Do not promote claims from this source until the underlying raw PDF identity is checked.

### `raw/converted/batch-pdf-043-s495-2-2.codex.md`

- Source reliability: Unknown from the current artifact because the converted output is empty.
- Conversion confidence: Failed.
- Recommended action: `rerun-conversion`

Concerns:

1. Converted markdown is empty while the source-prep manifest marks the source as converted.
   - Converted text: `[empty file]`
   - Page/chunk reference: Entire converted artifact
   - Why it looks odd: This reads like a failed assembly or an incomplete chunk/merge step rather than a successfully reviewed source.
   - Possible alternate reading: None
   - Source reliability: Unknown from the current artifact
   - Conversion confidence: Failed
   - Recommended action: `rerun-conversion`

Notes:

- Block evidence extraction until the conversion is regenerated and checked.

### `raw/converted/batch-pdf-044-s522bis-29-3.codex.md`

- Source reliability: Unknown from the current artifact because the converted output is empty.
- Conversion confidence: Failed.
- Recommended action: `rerun-conversion`

Concerns:

1. Converted markdown is empty while the source-prep manifest marks the source as converted.
   - Converted text: `[empty file]`
   - Page/chunk reference: Entire converted artifact
   - Why it looks odd: This reads like a failed assembly or an incomplete chunk/merge step rather than a successfully reviewed source.
   - Possible alternate reading: None
   - Source reliability: Unknown from the current artifact
   - Conversion confidence: Failed
   - Recommended action: `rerun-conversion`

Notes:

- Block evidence extraction until the conversion is regenerated and checked.

## Canonical Context Notes

- Branch-visible wiki context is still sparse in `wiki/index.md`; only `[[people/dario-pulgar-smith]]` is indexed there.
- No branch-local canonical linkage for the two Los Angeles birth records was available through the accessible repo views during this pass.

## Concise Report

- Sources triaged: `batch-img-017`, `batch-img-019`, `batch-pdf-042`, `batch-pdf-043`, `batch-pdf-044`
- Reliability notes: the two civil-register images are high-reliability originals; the Senate-labeled PDF slice has a source-identity problem; the two large-PDF outputs are empty and cannot yet be rated
- Pages or regions queued: entry 172 child-name line and father-name line in `batch-img-017`
- Suspected readings: `Fidelmiro`, `Juan de Casanova Pulgar`, and the `Cámara de Senadores` versus `Ferrocarriles Nacionales` title conflict
- Confusing sections: wrapper pages 1-4 in `batch-pdf-042`; entire empty outputs for `batch-pdf-043` and `batch-pdf-044`
- Low-priority sources: `batch-img-019` after current pass; signature uncertainty only
- Blockers for human review: reconcile source identity for `batch-pdf-042`; rerun or reassemble `batch-pdf-043` and `batch-pdf-044` before extraction