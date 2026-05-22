---
type: claim
status: draft
claim_type: event
confidence: 6.0
subject: [[people/dario-pulgar-adult-passenger-age-64]]
predicate: traveled_as_passenger_on
object: "Royal Mail Lines ship ANDES departing Southampton for South America on 1953-08-07; contracted to land at Buenos Aires; first class"
date: "1953-08-07"
place: "Southampton, England"
source: [[sources/src-3f6223e0e2c1-ca5a5078ab-passenger-list-royal-mai-passenger-list-royal-mai]]
source_path: "raw/sources/Passenger List, Royal Mail Lines Limited, August 7, 1953.png"
source_packet: [[source-packets/sp-chunk-a4cd3c3e5c16-p0001-01-andes-pulgar-passenger-list]]
chunk: "raw/chunks/ca5a5078ab-passenger-list-royal-mai-passenger-list-royal-mail-lines-limited-august-7-1953-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-a4cd3c3e5c16-P0001-01"
page_reference: "image page 1; passenger list page P.M. 25; Pulgar rows"
conversion_confidence: low
promotion_recommendation: promote_after_review
tags: [claim, staging, passenger_list, pulgar]
relationship: 
proof_review: research/_staging/reviews/proof-review-claim-chunk-a4cd3c3e5c16-p0001-01-dario-pulgar-adult-passenger-andes.md
review_status: ready_with_scope_note
canonical_readiness: ready_with_scope_note
source_quality_score: 0.88
conversion_confidence_score: 0.90
evidence_quantity_score: 0.72
agreement_score: 0.94
identity_confidence_score: 0.74
claim_probability: 0.91
relevance_level: high
relevance_confidence: 0.90
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

The extraction-stage draft recorded low promotion confidence because the image was not found at the original task source path during extraction. The proof review resolved that access blocker by visually reviewing `raw/sources/Passenger List, Royal Mail Lines Limited, August 7, 1953.png` and found the source image, converted file, chunk, and source packet all support the scoped travel-event claim.

## Interpretation

The travel event is promoted only for the passenger-list identity `Dario Pulgar (adult passenger, age 64)`. Buenos Aires is interpreted as the contracted landing port because the adult Pulgar row uses a ditto mark under the port column following a `BUENOS AIRES` entry.

## Uncertainty

The adult passenger is identified here as `Dario Pulgar (adult passenger, age 64)` to avoid conflation with the separate child row also named Dario.

## Promotion Recommendation

Promoted after proof review with a scope note.

## Proof Review Scope Note

Promoted after proof review as a scoped passenger-list event claim for the adult passenger-list identity only. The review found strong support for the travel event, age-64 disambiguator, first-class listing, Southampton departure on 1953-08-07, and Buenos Aires contracted landing port. It does not establish a broader canonical identity merge, spouse relationship, or parent-child relationship from the adjacent Pulgar rows. The red handwritten age annotation is not promoted as a vital fact.
