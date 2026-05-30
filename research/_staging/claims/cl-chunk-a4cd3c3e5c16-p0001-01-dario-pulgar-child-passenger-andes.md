---
type: claim
status: draft
claim_type: event
confidence: 7.5
subject: "Dario Pulgar (child passenger, age 11)"
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
conversion_confidence: medium
promotion_recommendation: promote_after_review
tags: [claim, staging, passenger_list, pulgar]
---

# Atomic Claim: Child Dario Pulgar Passenger on Andes

## Claim

Dario Pulgar, the child passenger aged 11, traveled first class on the Royal Mail Lines ship `ANDES`, departing Southampton on 7 August 1953 for South America, with Buenos Aires as the contracted landing port.

## Literal Source Support

```text
| | " | " Dario | " | | | | | 11 | | | | " | Student | + | | | | | | | " | " |
```

## Conversion Confidence And QA Concern

Medium. A prior proof review reports visible-image support for the narrow passenger-event claim: the child row for ditto-surname Dario appears in the Pulgar group on the `ANDES` passenger list, with age `11`, class by ditto from first class, and Buenos Aires by ditto as the contracted landing port.

The current revision pass could not locate the source image at the manifest path, so this claim should keep its proof-review scope note. The unresolved conversion-QA issue is limited to the child row's column 6 last-United-Kingdom-address cell and should not block this narrow passenger-event claim.

## Uncertainty

The row does not state that this child is the child of the adult Dario and Dorothy Pulgar.

## Promotion Recommendation

Promote after proof review with scope note. Do not use this claim to infer parentage, spouse relationships, or identity linkage to a canonical person outside this passenger-list row.
