---
type: claim
status: draft
claim_type: nationality_residence
confidence: 6.0
subject: "Dario Pulgar (adult passenger, age 64)"
predicate: had_permanent_residence_and_citizenship
object: "last permanent residence: England; intended future permanent residence: Chile; citizen or subject of Chile"
date: "1953-08-07"
source: "raw/converted/ca5a5078ab-passenger-list-royal-mai-passenger-list-royal-mail-lines-limited-august-7-1953.codex.md"
source_path: "raw/sources/Passenger List, Royal Mail Lines Limited, August 7, 1953.png"
source_packet: "research/_staging/source-packets/sp-chunk-a4cd3c3e5c16-p0001-01-andes-pulgar-passenger-list.md"
chunk: "raw/chunks/ca5a5078ab-passenger-list-royal-mai-passenger-list-royal-mail-lines-limited-august-7-1953-codex/page-0001-chunk-01.md"
chunk_id: "CHUNK-a4cd3c3e5c16-P0001-01"
page_reference: "image page 1; passenger list page P.M. 25; Pulgar rows"
conversion_confidence: low
promotion_recommendation: hold_for_conversion_qa
tags: [claim, staging, residence, citizenship, pulgar]
---

# Atomic Claim: Dario Pulgar Residence and Citizenship Fields

## Claim

Dario Pulgar was listed with last permanent residence in England, intended future permanent residence in Chile, and citizenship or subject country Chile.

## Literal Source Support

```text
| | " | PULGAR Dario | " | 64 `92` | | | | | | | | Bedford Corner Hotel, London. | Medical | + | | | | | | | Chile | Chile |
```

The table header places the `+` under `Country of last Permanent Residence* - England`, followed by column 9 `Country of Intended Future Permanent Residence*` and column 10 `Country of which Citizen or Subject`.

## Conversion Confidence And QA Concern

Low for promotion pending page-image reread.

## Uncertainty

This claim combines adjacent residence and citizenship columns from one row. Split before canonical promotion if the target wiki model stores these as separate facts.

## Promotion Recommendation

Hold for conversion QA.
