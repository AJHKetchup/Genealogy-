---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-585b6f62d484-P0001-01
worker: postconv-evidence-extraction-20260529002111370
source_id: ccebfd8b-passenger-and-crew-lists-nai-2848504-i94-pulgar
title: "Arrival-Departure Record Form I-94 B for PULGAR, JARIO"
source_path: "raw/sources/Passenger and Crew Lists, The National Archives at Washington, D.C.; NAI Number 2848504; Record Group Title Records of the Immigration and Naturalization Service, 1787–2004.png"
source_sha256: "ccebfd8b8589a86a954826dec91d3ba8f755749eb297cd686fc9d6af65885d30"
converted_file: "raw/converted/caccebfd8b-passenger-and-crew-lists-passenger-and-crew-lists-the-national-archives-at-washington-d-c-nai-number-2848504-record-group-title-records-of-the-immigration-and-naturalization-service-1787-2004.codex.md"
chunk: "raw/chunks/caccebfd8b-passenger-and-crew-lists-passenger-and-crew-lists-the-national-archives-at-5c40abe8fd/page-0001-chunk-01.md"
chunk_id: "CHUNK-585b6f62d484-P0001-01"
chunk_manifest: "raw/chunks/caccebfd8b-passenger-and-crew-lists-passenger-and-crew-lists-the-national-archives-at-5c40abe8fd/manifest.json"
page_reference: "page 1"
record_type: "arrival_departure_record_form_i94_b"
repository: "The National Archives at Washington, D.C."
nai_number: "2848504"
record_group_title: "Records of the Immigration and Naturalization Service, 1787-2004"
family_relevance: high
matched_terms: ["Pulgar"]
conversion_confidence: "medium-low"
conversion_qa_concern: "Converted text says the image quality is poor with significant noise and speckling; the original source PNG/page image was not present in this checkout for visual reread."
uncertainty: "Given name is transcribed as JARIO, which may be a distinct name or a conversion/read error for a Dario/Dario-like Pulgar family candidate. Passport number, permanent street address, and date/stamp meanings are uncertain."
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet Draft: I-94 B Arrival-Departure Record For PULGAR, JARIO

## Person-First Relevance

This record is family-relevant because it names a person with surname `PULGAR` and records immigration/travel fields. The known family context includes unresolved Dario/Pulgar identity clusters and a canonical warning not to merge Pulgar records into `Dario Arturo Pulgar-Smith` without identity review. This packet therefore stages the record as `PULGAR, JARIO` with a possible Dario/Pulgar identity question, not as a proved canonical person attachment.

## Source Reference

- Source path: `raw/sources/Passenger and Crew Lists, The National Archives at Washington, D.C.; NAI Number 2848504; Record Group Title Records of the Immigration and Naturalization Service, 1787–2004.png`
- Source SHA-256: `ccebfd8b8589a86a954826dec91d3ba8f755749eb297cd686fc9d6af65885d30`
- Converted file: `raw/converted/caccebfd8b-passenger-and-crew-lists-passenger-and-crew-lists-the-national-archives-at-washington-d-c-nai-number-2848504-record-group-title-records-of-the-immigration-and-naturalization-service-1787-2004.codex.md`
- Chunk/page reference: `raw/chunks/caccebfd8b-passenger-and-crew-lists-passenger-and-crew-lists-the-national-archives-at-5c40abe8fd/page-0001-chunk-01.md`, `CHUNK-585b6f62d484-P0001-01`, page 1
- Chunk manifest: `raw/chunks/caccebfd8b-passenger-and-crew-lists-passenger-and-crew-lists-the-national-archives-at-5c40abe8fd/manifest.json`

## Literal Support

```text
| Surname | Given Name | Passport Number |
| PULGAR | JARIO | 288 D[?]456 |

| Nationality (Citizenship) | Birthplace | Birthdate |
| CHILEAN | CONCEPCION CHILE | June 14 |

| United States Address |
| [blank] |

| Permanent Address |
| [illegible] CONCEPCION CHILE |

| Vessel Name or Airline and Flight No. of Arrival |
| KLM 493 |

| Passenger Boarded At |
| CURACAO |

[Stamped] 12 59 NYC
[Handwritten] KLM 632 NYC
[Handwritten] 1-3-57
```

## Conversion Confidence And QA Concern

The converted chunk explicitly reports poor image quality and marks the passport number and permanent address as uncertain or illegible. The original PNG path named in the conversion metadata was not found under `raw/sources`, and the conversion job folder did not include a page image for visual verification. Treat all extracted claims as draft leads pending source-image QA.

## Uncertainty

- The given name is `JARIO` in the converted text. Do not normalize it to `Dario` without image reread or corroborating evidence.
- The birthdate gives only `June 14`, with no year in the converted field.
- The permanent address includes only a readable place, `CONCEPCION CHILE`; the street or number is illegible.
- `12 59 NYC`, `KLM 632 NYC`, and `1-3-57` are present as stamps/notes, but their event meaning is not sufficiently clear from the converted text alone.

## Promotion Recommendation

`hold_for_conversion_qa`: this is a high-relevance Pulgar immigration/travel lead, but the missing image and uncertain given name/address/passport fields require proof review and image reread before canonical promotion or identity attachment.
