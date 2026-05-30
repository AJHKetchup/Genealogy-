---
type: conversion_review_note
status: draft
task_id: evidence-extraction:CHUNK-a4cd3c3e5c16-P0001-01
worker: postconv-evidence-extraction-20260530192337986
source_path: "raw/sources/Passenger List, Royal Mail Lines Limited, August 7, 1953.png"
source_sha256: "5a5078ab4b0d50fdd2cdefb4aa21ffaf6524824329254788ab4437bff500c6d3"
converted_file: "raw/converted/ca5a5078ab-passenger-list-royal-mai-passenger-list-royal-mail-lines-limited-august-7-1953.codex.md"
chunk: "raw/chunks/ca5a5078ab-passenger-list-royal-mai-passenger-list-royal-mail-lines-limited-august-7-1953-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-a4cd3c3e5c16-P0001-01"
page_reference: "image page 1; passenger list page P.M. 25; Pulgar rows"
promotion_recommendation: hold_for_conversion_qa
---

# Conversion Review Note: Andes Pulgar Source Image And Address Hold

## Evidence To Preserve

- Converted row context lists three consecutive Pulgar passengers contracted to land at Buenos Aires: `PULGAR Dario`, ditto `Dorothy`, and ditto `Dario`.
- The age-11 Dario row is transcribed as a child passenger with occupation/calling `Student`.
- Prior staged proof reviews report visible-image support for the age-11 Dario row's `+` mark under the England subcolumn of column 8 and ditto marks in columns 9 and 10 following `Chile`.
- The earlier composite child-row address/residence/citizenship claim has been superseded by atomic claims and should not be promoted.

## Derivative Transcript Conflict

The converted table renders a ditto mark in the age-11 Dario row's column 6 last-United-Kingdom-address cell. The proof-review revision context states that this address ditto was not clear enough on image review for promotion. Do not silently convert this into a canonical `Bedford Corner Hotel, London.` address claim for the child row.

## Current File Availability

This revision pass could not locate the source image at `raw/sources/Passenger List, Royal Mail Lines Limited, August 7, 1953.png`. It also could not locate the rendered page image named in the conversion job manifest at `raw/codex-conversion-jobs/ca5a5078ab-passenger-list-royal-mai-passenger-list-royal-mail-lines-limited-august-7-1953/page-images/page-0001.png`.

## Blocker

Keep the source packet and any child-row last-UK-address claim on `hold_for_conversion_qa` until the source/page image is restored or regenerated through the normal conversion QA workflow and the child Dario row's column 6 cell is reread. The proof-reviewed child-row England and Chile field claims may remain separate, narrow, and scoped to their specific row fields; relationship claims remain `do_not_promote`.
