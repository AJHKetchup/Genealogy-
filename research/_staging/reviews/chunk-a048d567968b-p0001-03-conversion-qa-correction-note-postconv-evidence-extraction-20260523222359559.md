---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523222359559
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
supplemental_source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar-supplement-postconv-evidence-extraction-20260523222359559.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1 in manifest/frontmatter; Dario Pulgar evidence appears in embedded converted text for printed/source pages 7-8 and rendered page images page-0007.jpg/page-0008.jpg"
literal_support: "The staged Dario Pulgar claims are supported by passages naming him as a UN Habitat Secretariat colleague, describing him as Chilean, stating his Allende-era Chile state film distribution role, stating he fled after the 1973 overthrow, giving Spanish as his mother tongue, noting English/French language context, and describing Vision Habitat distribution-rights/off-shore printing-materials work."
conversion_confidence: medium-high
conversion_qa_concern: "This revision confirms that page-0008.jpg is present in the current checkout and that prior staged outputs already preserve visual-review findings. The remaining blocker is not image availability but citation integrity: derivative chunk metadata assigns page 1 while the family-relevant evidence is printed/rendered pages 7-8."
uncertainty: "Do not alter source wording or collapse the metadata/image disagreement. The memoir source supports contextual narrative claims only; it does not establish kinship or exact formal employment dates."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This worker reviewed the current staging state for `CHUNK-a048d567968b-P0001-03` after proof review requested conversion-QA reconciliation.

## Findings

- The current checkout contains `page-0007.jpg` and `page-0008.jpg` in the conversion job page-images directory.
- Existing staged claim drafts and prior correction notes already record visual verification of the Dario Pulgar passages on those rendered images.
- The Dario Pulgar claims remain person-first and family-relevant as contextual narrative evidence: identity descriptor, Chile work history, displacement context, language context, and Vision Habitat duties.
- The unresolved blocker is the page/citation boundary: the manifest and chunk frontmatter assign the chunk to page 1, while the image-reviewed evidence belongs to printed/rendered pages 7 and 8 and appears within a chunk body that includes later converted page metadata.

## Staging Decision

Do not promote the related Dario Pulgar claims yet. Keep `promotion_recommendation: hold_for_conversion_qa` until conversion QA corrects or formally documents the authoritative citation/page boundary.

No family relationship is stated in this chunk; the negative relationship note should remain `do_not_promote`.
