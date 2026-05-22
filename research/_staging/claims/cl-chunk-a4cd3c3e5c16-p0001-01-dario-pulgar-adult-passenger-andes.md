---
type: claim
status: draft
claim_type: event
confidence: 6.0
subject: "Dario Pulgar (adult passenger, age 64)"
predicate: traveled_as_passenger_on
object: "Royal Mail Lines ship ANDES departing Southampton for South America on 1953-08-07; contracted to land at Buenos Aires; first class"
date: "1953-08-07"
place: "Southampton, England"
source: "raw/converted/ca5a5078ab-passenger-list-royal-mai-passenger-list-royal-mail-lines-limited-august-7-1953.codex.md"
source_path: "raw/sources/Passenger List, Royal Mail Lines Limited, August 7, 1953.png"
source_packet: "research/_staging/source-packets/sp-chunk-a4cd3c3e5c16-p0001-01-andes-pulgar-passenger-list.md"
chunk: "raw/chunks/ca5a5078ab-passenger-list-royal-mai-passenger-list-royal-mail-lines-limited-august-7-1953-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-a4cd3c3e5c16-P0001-01"
page_reference: "image page 1; passenger list page P.M. 25; Pulgar rows"
conversion_confidence: low
promotion_recommendation: hold_for_conversion_qa
tags: [claim, staging, passenger_list, pulgar]
---

# Atomic Claim: Dario Pulgar Passenger on Andes

## Claim

Dario Pulgar, the adult male Pulgar passenger aged 64, traveled first class on the Royal Mail Lines ship `ANDES`, departing Southampton on 7 August 1953 for South America, with Buenos Aires as the contracted landing port.

## Literal Source Support

```text
Name of Ship "ANDES"
Date of Departure 7th. August 1953.
Where Bound SOUTH AMERICA.
| | BUENOS AIRES | ... |
| | " | PULGAR Dario | " | 64 `92` | ... |
```

## Source Path

- Source path: `raw/sources/Passenger List, Royal Mail Lines Limited, August 7, 1953.png`
- Converted file: `raw/converted/ca5a5078ab-passenger-list-royal-mai-passenger-list-royal-mail-lines-limited-august-7-1953.codex.md`
- Chunk/page reference: `CHUNK-a4cd3c3e5c16-P0001-01`, page 1, passenger list page `P.M. 25.`

## Conversion Confidence And QA Concern

Low for promotion. The row is clear in the converted table, but page-level QC requires reread and the original image was not found at the task source path during extraction.

## Uncertainty

The adult passenger is identified here as `Dario Pulgar (adult passenger, age 64)` to avoid conflation with the separate child row also named Dario.

## Promotion Recommendation

Hold for conversion QA.
