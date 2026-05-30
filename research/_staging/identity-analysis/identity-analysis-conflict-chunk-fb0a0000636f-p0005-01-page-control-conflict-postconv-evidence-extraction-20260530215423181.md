---
type: identity_conflict_analysis
role: evidence_extractor
task_id: evidence-extraction:CHUNK-fb0a0000636f-P0005-01
worker: postconv-evidence-extraction-20260530215423181
source: raw/sources/CV of Dario Arturo Pulgar.pdf
source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-revision-postconv-evidence-extraction-20260530215423181.md
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
chunk_id: CHUNK-fb0a0000636f-P0005-01
page_reference: page 5 per assigned chunk; page control disputed
analysis_status: hold
canonical_readiness: not_ready
promotion_recommendation: hold_for_conversion_qa
---

# Identity/Page-Control Hold: CHUNK-fb0a0000636f-P0005-01

The source title identifies the broader document as a CV of `Dario Arturo Pulgar`, but the assigned page body does not repeat the name. The page therefore provides document-level subject attribution only, not a page-local identity bridge.

Two derivative readings remain in conflict:

- Assigned chunk reading: 1979-1982 HABITAT in Nairobi; 1974-1978 National Film Board of Canada in Montreal; 1972-1973 Chile Films in Santiago; 1970-1972 CITELCO in Santiago.
- Aggregate converted page-5 reading: 1999 PROFONANPE and TVE entries; 1998-1999 Arca Consulting/European Commission in Lesotho; 1997-1998 Klohn Crippen and SNC Lavalin entries.

Conversion confidence/QA concern: the authoritative rendered page image for page 5 is absent, the chunk manifest duplicates the same chunk id/path with conflicting hashes, and observed hashes differ from recorded metadata. This extraction task did not run source preparation or conversion repair.

Uncertainty: high for which derivative text controls page 5; moderate for attaching the document-level `Dario Arturo Pulgar` CV subject to any canonical family person; no relationship evidence is present.

Recommended action: hold all page-5 occupational and identity attachment claims for conversion QA. After page control is certified, rerun proof review on any surviving claims and run a separate identity-bridge review before canonical attachment.
