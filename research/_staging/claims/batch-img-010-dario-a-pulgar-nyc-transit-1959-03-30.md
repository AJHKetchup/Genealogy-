---
type: staged_claim
status: probable
claim_type: travel
confidence: 7.8
subject: Dario A. Pulgar
predicate: transited through
object: New York City on 30 March 1959 after boarding BOAC BA 549 at London, England
date: 1959-03-30
place: New York City, United States
source: raw/codex-conversion-jobs/batch-img-010-arrival-departure-record-form-i-94-b-march-30-1959/source/Arrival-Departure Record, Form I-94 B, March 30, 1959.png
converted_file: raw/converted/batch-img-010-arrival-departure-record-form-i-94-b-march-30-1959.codex.md
source_packet: research/_staging/source-packets/batch-img-010-arrival-departure-record-form-i-94-b-march-30-1959-codex.md
chunk_ref: CHUNK-2080170a5175-P0001-01
page_ref: Page 1
source_reliability_class: original government transit form
source_reliability_score: 8
evidence_type: direct travel-event evidence
informant_proximity: Self-reported travel identity on an official form with arrival stamp.
conversion_confidence: medium
qa_concern: dated QA review requires identity caution and a targeted reread of adjacent identity and travel fields
promotion_recommendation: revise
tags: [staging, claim, travel, transit, pulgar, 1959]
---

# Atomic Claim

## Claim

The I-94 record states that Dario A. Pulgar transited New York City on 30 March 1959 after boarding BOAC flight BA 549 in London, England.

## Status

`probable` because the flight and arrival-stamp fields are clear, even though the broader identity block is still on a targeted reread queue.

## Confidence

7.8/10. Strong official travel evidence, reduced slightly because the dated QA pass still wants a local reread of surrounding fields and warns against premature identity merging.

## Literal Source Support

```text
Surname: PULGAR
Given Name: DARIO
Initial: A
Vessel Name or Airline and Flight No. of Arrival:
BOAC BA 549
Passenger Boarded At:
London England
[stamp]
MAR 30 '59 N Y C
```

## Translation

Not applicable; the source is already in English.

## Interpretation

This is a solid staged travel claim for a mid-century Pulgar transit event, but it should remain detached from `Dario Pulgar Smith` until identity review resolves the generational mismatch concern.

## Uncertainty

The claim does not depend on the ambiguous birthdate or permanent-address city, but the surrounding identity context remains sensitive enough that promotion should stay conservative.

## Supports

- `research/_staging/source-packets/batch-img-010-arrival-departure-record-form-i-94-b-march-30-1959-codex.md`

## Conflicts With

- Potential identity conflict with the existing `Dario Pulgar Smith` branch context if this traveler is incorrectly merged without further review.