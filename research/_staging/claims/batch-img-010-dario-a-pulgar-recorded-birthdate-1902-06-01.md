---
type: staged_claim
status: possible
claim_type: birthdate_recorded
confidence: 6.1
subject: Dario A. Pulgar
predicate: was recorded with birthdate
object: 1 Jun. 1902[?]
date: 1902-06-01
place: Chile
source: raw/codex-conversion-jobs/batch-img-010-arrival-departure-record-form-i-94-b-march-30-1959/source/Arrival-Departure Record, Form I-94 B, March 30, 1959.png
converted_file: raw/converted/batch-img-010-arrival-departure-record-form-i-94-b-march-30-1959.codex.md
source_packet: research/_staging/source-packets/batch-img-010-arrival-departure-record-form-i-94-b-march-30-1959-codex.md
chunk_ref: CHUNK-2080170a5175-P0001-01
page_ref: Page 1
source_reliability_class: original government transit form
source_reliability_score: 8
evidence_type: source-stated birthdate
informant_proximity: Likely self-reported on an official form.
conversion_confidence: high
qa_concern: final birth-year digits are not perfectly clean in the converted reading
promotion_recommendation: revise
tags: [staging, claim, birthdate, pulgar, 1902]
---

# Atomic Claim

## Claim

The I-94 record gives Dario A. Pulgar a recorded birthdate of `1 Jun. 1902[?]` and birthplace `Chile`.

## Status

`possible` because the field is useful but the final digits of the year are not fully clean in the converted reading.

## Confidence

6.1/10. The form is original and the field is legible enough to stage, but this should not be promoted without corroboration from a cleaner source.

## Literal Source Support

```text
Nationality (Citizenship): CHILEAN
Birthplace: CHILE
Birthdate: 1 Jun. 1902[?]
```

## Translation

Not applicable; the source is already in English.

## Interpretation

This is a candidate birthdate-only claim. It is valuable for comparison against CV, passport, or other travel records, but not strong enough yet for confident canonical use.

## Uncertainty

The year reads as `1902[?]` in the conversion. This draft preserves that uncertainty rather than normalizing the date.

## Supports

- `research/_staging/source-packets/batch-img-010-arrival-departure-record-form-i-94-b-march-30-1959-codex.md`

## Conflicts With

No conflicting birthdate source was reviewed in this staging pass.