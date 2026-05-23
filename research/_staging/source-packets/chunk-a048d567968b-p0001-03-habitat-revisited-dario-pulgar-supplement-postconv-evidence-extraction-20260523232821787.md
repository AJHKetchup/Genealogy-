---
type: source_packet
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260523232821787
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
page_reference: "assigned page 1; literal Dario Pulgar support appears on rendered source image page-0007.jpg / printed page 7 and page-0008.jpg / printed page 8 embedded in this chunk"
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
conversion_qa_concern: "The wording of the family-relevant Dario Pulgar passages is visually supported by rendered images in this checkout. The unresolved blocker is citation/page control: the task and chunk manifest assign this chunk to page 1, while the supporting source images are printed pages 7 and 8 and the chunk body continues across later page metadata."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet Supplement: Dario Pulgar Page-Boundary Hold

This supplement records the current worker's evidence-extraction revision for `CHUNK-a048d567968b-P0001-03`. It does not edit raw sources, converted Markdown, chunks, source images, or canonical wiki pages.

## Visual Checks

- `page-0007.jpg` is present and visibly supports the Dario Pulgar paragraph: the source names `Dario Pulgar`, describes him as Chilean, says he had been the number two man in Chile's state film distribution system under Allende while still in his twenties, and says he reached "The Board" after fleeing Pinochet's 1973 overthrow of the Allende government.
- `page-0008.jpg` is present and visibly supports the sentence `His mother tongue was Spanish`, the English/French language context, and the statement that Dario was primarily occupied with acquiring distribution rights and determining where the off-shore printing materials were.

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

## Extraction Scope

The staged atomic claims already present for this chunk remain appropriate as staged, held evidence for Dario Pulgar's descriptor, Chile film-distribution role, 1973 flight context, language context, and Vision Habitat distribution-rights work. This source packet supplement adds no new relationship claim because the chunk states no parent, spouse, child, sibling, or other kinship link.

## Conversion Confidence And QA Concern

Conversion confidence is medium-high for the literal wording after visual review of the rendered page images. The derivative transcript and source images agree on the reviewed Dario Pulgar wording.

The promotion blocker remains unresolved: the controller assignment and manifest identify the chunk as page 1, while the family-relevant evidence is on rendered/printed pages 7 and 8 and the chunk body carries later page metadata. This disagreement should be kept visible until conversion/page-boundary QA establishes the authoritative citation.

## Uncertainty

The source is memoir evidence, not a vital, immigration, employment, or language record. It provides useful person-linked narrative context, but it does not prove a formal job title, exact Chile employment dates, exact birth date, route of flight, or a family relationship.

## Promotion Recommendation

Keep related Dario Pulgar claims on `hold_for_conversion_qa`. The page-8 image availability issue is resolved in this checkout, but the page-reference/chunk-boundary discrepancy still blocks canonical promotion.
