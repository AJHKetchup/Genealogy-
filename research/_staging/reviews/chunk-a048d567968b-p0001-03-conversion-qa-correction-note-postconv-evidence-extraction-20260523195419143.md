---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523195419143
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1; converted chunk body includes text and page metadata for later source pages, with prior staged notes associating Dario Pulgar support with rendered/printed pages 7 and 8"
literal_support: "Converted chunk text includes `Dario Pulgar`, `dynamic Chilean`, `Dario had been the number two man in Chile's state film distribution system`, `after fleeing Pinochet's overthrow of the Allende government in 1973`, `His mother tongue was Spanish`, and `Dario was primarily occupied with acquiring distribution rights and determining where the off-shore printing materials were`."
conversion_confidence: medium
conversion_qa_concern: "The Dario Pulgar text remains readable in the converted chunk, but this worker could not independently repeat visual QA because `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg` and `page-0008.jpg` are absent in the current checkout. The conversion job manifest still lists those page-image paths. The chunk manifest assigns CHUNK-a048d567968b-P0001-03 to page 1 while the family-relevant support appears in later embedded page text."
uncertainty: "This note does not edit raw sources, converted Markdown, chunks, or page Markdown. It preserves the disagreement between derivative transcript page assignment, prior reported image-reviewed evidence, and the current checkout's missing rendered images."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This revision reviewed `CHUNK-a048d567968b-P0001-03` and the existing staged Dario Pulgar drafts for the controller task `evidence-extraction:CHUNK-a048d567968b-P0001-03`.

## Staged Evidence State

The existing staged source packet, six atomic Dario Pulgar claim drafts, negative relationship note, and conversion-QA research task are appropriate to keep in staging. They identify family-relevant narrative context for Dario Pulgar without promoting it:

- Dario Pulgar described as a dynamic Chilean.
- Dario Pulgar's role as the number two man in Chile's state film distribution system under Allende.
- Dario Pulgar's flight after Pinochet's 1973 overthrow of the Allende government.
- Dario Pulgar's mother tongue as Spanish.
- Dario Pulgar's English and French language context.
- Dario Pulgar's Vision Habitat work acquiring distribution rights and locating off-shore printing materials.

No new family relationship candidate should be promoted from this chunk. The staged relationship draft correctly remains negative evidence because the chunk describes colleagues and work context, not kinship.

## Current QA Finding

The converted text is clear enough for draft extraction, but the proof-review blocker remains unresolved. In this checkout, both checks below returned false:

```text
raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg
raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg
```

The conversion job manifest still lists those image paths and image hashes, so this is an image-availability/citation-QA problem rather than evidence to alter the transcript. Prior correction notes report visual checks on rendered pages 7 and 8; this worker cannot independently confirm those visual checks from the current filesystem state.

## Remaining Blocker

Keep all promotable Dario Pulgar drafts from this chunk at `promotion_recommendation: hold_for_conversion_qa`.

The unresolved blocker is authoritative page/citation reconciliation:

- the chunk manifest assigns the chunk to page 1;
- the converted chunk body includes page metadata and transcription for later pages;
- prior staged notes associate the Dario Pulgar support with rendered/printed pages 7 and 8;
- the current checkout lacks the rendered page images needed for repeat visual verification.

No external research was performed.
