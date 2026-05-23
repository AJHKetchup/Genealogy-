---
type: source_packet
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523225852760
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
source_title: "Habitat Revisited, Jim Carney, 2006"
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_path: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_id: CHUNK-a048d567968b-P0001-03
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
page_reference: "assigned page 1; visual support checked on rendered source images page-0007.jpg and page-0008.jpg, corresponding to printed/source pages 7 and 8 embedded in this chunk"
source_page_images_checked:
  - "raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0007.jpg"
  - "raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0008.jpg"
source_type: memoir
source_date: "2006"
family_relevance: high
matched_terms:
  - Dario
  - Dario Pulgar
  - Pulgar
conversion_confidence: medium-high
conversion_qa_concern: "The relevant Dario Pulgar wording was visually checked against rendered source images page-0007.jpg and page-0008.jpg. The remaining blocker is not missing visual evidence for these passages, but unresolved page/chunk metadata: the task and manifest assign the chunk to page 1 while the support appears on printed/source pages 7 and 8 in the embedded converted text."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet Supplement: Dario Pulgar Page-Image QA

This supplement revises the earlier hold context for `CHUNK-a048d567968b-P0001-03`. The rendered source image for printed/source page 8 is present in this checkout, and the family-relevant Dario Pulgar passages were visually checked.

## Visual Checks

- `page-0007.jpg` visibly supports the Dario Pulgar full-name paragraph, including the Chilean descriptor, the statement that he had been the number two man in Chile's state film distribution system under Allende, and the statement that he reached "The Board" after fleeing Pinochet's 1973 overthrow of the Allende government.
- `page-0008.jpg` visibly supports the sentence `His mother tongue was Spanish`, the related English/French language passage, and the sentence that Dario was primarily occupied with acquiring distribution rights and determining where the off-shore printing materials were.

## Literal Support

```text
A couple of my UN Habitat Secretariat confreres stayed on, notably Dario Pulgar,
a raspy-voiced, incredibly energetic, dynamic Chilean.
```

```text
In Chile under Allende,
though still in his twenties, Dario had been the number two man in Chile's state film
distribution system. He had fetched up at "The Board" after fleeing Pinochet's
overthrow of the Allende government in 1973.
```

```text
His mother tongue was Spanish, but he was fluent in English and had
learned French in Montreal in six weeks, he said.
```

```text
Dario was primarily occupied with acquiring distribution rights and determining
where the off-shore printing materials were.
```

## Conversion Confidence And QA Concern

Conversion confidence for the Dario Pulgar wording is medium-high after visual comparison to rendered source images. The derivative transcript and images agree on the family-relevant text reviewed here.

The evidence remains blocked for canonical promotion because the source-reference layers disagree. The assignment and chunk manifest identify this as page 1 material, while the chunk body includes converted page metadata and text for printed/source pages 7 and 8. This should remain `hold_for_conversion_qa` until the authoritative citation/page-boundary discrepancy is corrected or explicitly documented in the conversion record.

## Uncertainty

This is memoir evidence by Jim Carney, not a contemporary vital, immigration, employment, or language record. It provides useful Dario Pulgar narrative context but does not state a parent, spouse, child, sibling, exact birth date, formal Chilean job title, immigration route, or exact employment date range.

## Promotion Recommendation

Keep all Dario Pulgar claims from this chunk at `hold_for_conversion_qa`. The missing-image blocker for page 8 appears resolved locally, but the page-reference/chunk-boundary blocker remains unresolved.
