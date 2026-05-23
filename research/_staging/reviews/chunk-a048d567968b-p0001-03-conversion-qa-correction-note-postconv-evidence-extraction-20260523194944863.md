---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523194944863
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1; converted chunk body includes later page metadata and Dario Pulgar support associated in prior review notes with rendered/printed pages 7 and 8"
literal_support: "Converted chunk text includes `Dario Pulgar`, `In Chile under Allende... Dario had been the number two man in Chile's state film distribution system`, `His mother tongue was Spanish`, and `Dario was primarily occupied with acquiring distribution rights and determining where the off-shore printing materials were`."
conversion_confidence: medium
conversion_qa_concern: "In this checkout, the conversion job manifest lists page image paths including page-0007.jpg and page-0008.jpg, but the page-images directory is absent. This worker could not independently repeat visual QA for the prior image-reviewed evidence. The derivative page-boundary conflict also remains: the chunk manifest assigns CHUNK-a048d567968b-P0001-03 to page 1 while family-relevant support appears in embedded later-page transcription/page metadata."
uncertainty: "This note does not alter raw source, converted Markdown, chunks, or page Markdown. Earlier proof/correction notes disagree about whether page-0008.jpg was available in their checkout; this revision records only the current worker's filesystem state and keeps the derivative-transcript/image-reviewed-evidence disagreement explicit."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This evidence-extraction revision reviewed the assigned chunk and existing staged outputs for `CHUNK-a048d567968b-P0001-03`.

The current staged source packet, six Dario Pulgar atomic claims, and negative relationship note already preserve the family-relevant evidence without promoting it. The claims remain appropriate as staged contextual evidence only:

- Dario Pulgar described as Chilean.
- Dario Pulgar's Chile state film-distribution role under Allende.
- Dario Pulgar fleeing after Pinochet's 1973 overthrow of the Allende government.
- Dario Pulgar's mother tongue as Spanish.
- Dario Pulgar's English/French language context.
- Dario Pulgar's Vision Habitat distribution-rights/off-shore printing-materials work.

## Current QA State

The converted chunk text is clear enough for staging, but not for canonical promotion. The conversion job manifest records rendered page-image paths for `page-0007.jpg` and `page-0008.jpg`; however, this checkout does not contain the `page-images` directory under:

```text
raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/
```

Because those image files are absent here, this worker did not independently verify the printed page 7 or printed page 8 passages against rendered images. Prior proof-review and correction notes remain useful as review history, but this note should not be read as a new visual verification.

## Remaining Blocker

Keep all promotable Dario Pulgar claims from this chunk on `hold_for_conversion_qa`. The unresolved blocker is authoritative conversion/page-reference QA:

- chunk manifest assignment: page 1;
- converted chunk body: includes later page metadata and transcription;
- prior image-reviewed evidence: reported against rendered/printed pages 7 and 8;
- current checkout: page images unavailable for repeat visual QA.

The negative relationship note remains `do_not_promote` because this chunk states no family relationship.
