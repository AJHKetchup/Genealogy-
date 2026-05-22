---
type: conflict_candidate
status: draft
conflict_type: conversion_qa_blocker
subject: "Andes passenger list, page 1, Pulgar rows"
source_packet: "research/_staging/source-packets/sp-chunk-a4cd3c3e5c16-p0001-01-andes-pulgar-passenger-list.md"
confidence: high
promotion_recommendation: hold_for_conversion_qa
---

# Conflict Candidate: Missing Source Image and Reread Requirement

Source path: `raw/sources/Passenger List, Royal Mail Lines Limited, August 7, 1953.png`

Converted file: `raw/converted/ca5a5078ab-passenger-list-royal-mai-passenger-list-royal-mail-lines-limited-august-7-1953.codex.md`

Chunk/page reference: `raw/chunks/ca5a5078ab-passenger-list-royal-mai-passenger-list-royal-mail-lines-limited-august-7-1953-codex/page-0001-chunk-01.md`, `CHUNK-a4cd3c3e5c16-P0001-01`, image page 1, passenger list page `P.M. 25.`

## Issue

The controller marked this extraction with `qc:reread-page`, and conversion-review triage lists the page as critical relevance with low confidence and action `reread-page`. The original image was not found at the task's `source_path` during this extraction pass, so image-level verification could not be completed.

## Literal Support

Task metadata:

```text
qc_recommended_actions: reread-page
family_relevance: critical
matched_terms: Dario, John, Juan, Mercedes, Pulgar
```

Conversion-review triage:

```text
| 1 | critical | low | reread-page | none | Dario, John, Juan, Mercedes, Pulgar |
```

## Conversion Confidence And QA Concern

This is a QA blocker for promotion. Draft claims can preserve the extracted evidence, but proof review should not promote them until the page image is restored or reread.

## Uncertainty

The converted Pulgar rows appear coherent, but unverified source-image readings could affect names, ages, ditto marks, or column alignment.

## Promotion Recommendation

Hold for conversion QA.
