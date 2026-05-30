---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-a4cd3c3e5c16-P0001-01
worker: postconv-evidence-extraction-20260530193655008
source_path: "raw/sources/Passenger List, Royal Mail Lines Limited, August 7, 1953.png"
source_sha256: "5a5078ab4b0d50fdd2cdefb4aa21ffaf6524824329254788ab4437bff500c6d3"
converted_file: "raw/converted/ca5a5078ab-passenger-list-royal-mai-passenger-list-royal-mail-lines-limited-august-7-1953.codex.md"
chunk: "raw/chunks/ca5a5078ab-passenger-list-royal-mai-passenger-list-royal-mail-lines-limited-august-7-1953-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-a4cd3c3e5c16-P0001-01"
page_reference: "image page 1; passenger list page P.M. 25; Pulgar rows"
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Andes Pulgar Child Address Hold

## Literal Converted Support

```text
| | " | PULGAR Dario | " | 64 `92` | | | | | | | | Bedford Corner Hotel, London. | Medical | + | | | | | | | Chile | Chile |
| | " | " Dorothy | " | | 49 `92` | | | | | | | " | - | + | | | | | | | " | " |
| | " | " Dario | " | | | | | 11 | | | | " | Student | + | | | | | | | " | " |
```

## Revision Result

The prior composite child-row claim has been kept superseded and should not be promoted. It bundled address, residence, intended residence, and citizenship into one claim and overstated the unclear column 6 address mark.

The following child-row facts are preserved as separate atomic claims with narrow scope: passenger event on `ANDES`, age `11`, occupation/calling `Student`, last permanent residence marked in the England subcolumn, intended future permanent residence `Chile` by ditto mark, and citizen/subject country `Chile` by ditto mark.

## Remaining Conversion-QA Blocker

The child Dario row's column 6 last-United-Kingdom-address cell remains unresolved. The converted transcript renders a ditto mark that would repeat `Bedford Corner Hotel, London.`, but proof-review revision context says that mark was not sufficiently clear for promotion. This task pass also could not locate the source image at `raw/sources/Passenger List, Royal Mail Lines Limited, August 7, 1953.png` or the rendered page image under the conversion job page-images path.

Do not promote a child-row last-UK-address claim until a targeted page-image reread verifies column 6. Preserve the disagreement between the derivative transcript and the image-reviewed evidence.

## Relationship And Identity Limits

The passenger list does not explicitly state that Dorothy is the adult Dario Pulgar's wife or that the younger Dario is their child. It also does not bridge the younger Dario to a fuller `Dario Arturo Pulgar` or `Dario Arturo Pulgar-Smith` identity. Relationship candidates from this source remain research clues only and should stay `do_not_promote`.

## Promotion Recommendation

Hold this conversion-review issue for conversion QA. The narrow, image-reviewed child-row claims may proceed only through normal proof review with their scope notes intact; the child last-UK-address reading remains held.
