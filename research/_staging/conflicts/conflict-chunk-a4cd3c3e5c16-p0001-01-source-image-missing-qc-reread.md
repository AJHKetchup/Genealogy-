---
type: conflict_candidate
status: draft
conflict_type: conversion_qa_blocker
subject: "Andes passenger list, page 1, child Dario Pulgar last UK address"
source_packet: "research/_staging/source-packets/sp-chunk-a4cd3c3e5c16-p0001-01-andes-pulgar-passenger-list.md"
confidence: high
promotion_recommendation: hold_for_conversion_qa
---

# Conflict Candidate: Child Dario Pulgar Address Ditto Requires Reread

Source path: `raw/sources/Passenger List, Royal Mail Lines Limited, August 7, 1953.png`

Converted file: `raw/converted/ca5a5078ab-passenger-list-royal-mai-passenger-list-royal-mail-lines-limited-august-7-1953.codex.md`

Chunk/page reference: `raw/chunks/ca5a5078ab-passenger-list-royal-mai-passenger-list-royal-mail-lines-limited-august-7-1953-codex/page-0001-chunk-01.md`, `CHUNK-a4cd3c3e5c16-P0001-01`, image page 1, passenger list page `P.M. 25.`

## Issue

The controller marked this extraction with `qc:reread-page`, and the prior proof review found that the composite child-row claim was not promotion-ready. Local image review now confirms the source image is present, but the child Dario row's column 6 last-UK-address cell is still not clear enough to promote as a ditto mark for `Bedford Corner Hotel, London.`

## Literal Support

Task metadata:

```text
qc_recommended_actions: reread-page
family_relevance: critical
matched_terms: Dario, John, Juan, Mercedes, Pulgar
```

Prior proof review:

```text
The source image does not clearly show a column 6 ditto mark on the child Dario row.
```

## Conversion Confidence And QA Concern

This is a QA blocker for the child last-UK-address claim only. Draft claims can preserve the image-supported England and Chile fields separately.

## Uncertainty

The converted table renders a ditto mark in the child row address column, but the image-reviewed evidence is weaker for that column than for the child row age, `Student`, England mark, and Chile ditto marks.

## Promotion Recommendation

Hold the child address claim for conversion QA.
