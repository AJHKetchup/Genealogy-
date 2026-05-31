---
type: source_packet
status: draft
task_id: evidence-extraction:CHUNK-fb0a0000636f-P0005-01
worker: postconv-evidence-extraction-20260531045657514
source_title: CV of Dario Arturo Pulgar
source_type: curriculum_vitae
source: raw/sources/CV of Dario Arturo Pulgar.pdf
source_path: raw/sources/CV of Dario Arturo Pulgar.pdf
source_sha256: 07263f404e4c433d8b9ae10daf26700d22b79b1ae725325a9d37a64d60434424
source_file_observed: absent_at_recorded_path
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
converted_sha256_recorded: fb0a0000636f2cbe69d6963c635af04e8b14130daa310ed08dffdd82728f27f0
converted_sha256_observed: da9ec0c3a0f604b4c0e827a2a733a0ba013dd60d86abea2b46490d9f8820d288
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
chunk_id: CHUNK-fb0a0000636f-P0005-01
chunk_sha256_observed: d6ea4f611ee03000c11cbba63246e95b55f8a421fcbc87d0d667e91f5c8d0b8d
chunk_manifest: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/manifest.json
page_reference: page 5
page_start: 5
page_end: 5
source_identity: Dario Arturo Pulgar, identified by the source title and converted document title rather than by page-body text.
family_relevance: high
matched_terms: Dario; Pulgar
literal_support: Assigned chunk text includes 1979-1982 HABITAT/Nairobi, 1974-1978 NFB/Montreal, 1972-1973 Chile Films/Santiago, and 1970-1972 CITELCO/Santiago entries; conversion-job page Markdown for the same page includes competing 1999-1997 consulting entries.
conversion_confidence: blocked
conversion_qa_concern: Physical page 5 is not under control. The source PDF was absent at the recorded path during this extraction pass; no authoritative page image was used; the assigned chunk text conflicts with raw/codex-conversion-jobs/.../page-markdown/page-0005.md; the chunk manifest lists the same page-5 chunk id twice with different char counts and hashes; observed converted and chunk SHA256 values differ from recorded metadata.
uncertainty: High for which derivative text controls physical page 5; moderate for attaching either derivative page to canonical Dario Arturo Pulgar-Smith because the page body does not repeat the full person name or prove the surname variant.
promotion_recommendation: hold_for_conversion_qa
---

# Source Packet Revision: CV of Dario Arturo Pulgar, Page 5

This revision stages the page-5 evidence as blocked rather than promotion-ready. The document title/source path identify the CV subject as Dario Arturo Pulgar, but the page body in the assigned chunk does not repeat the subject's name and does not bridge the source-title identity to `Dario Arturo Pulgar-Smith`.

## Assigned Chunk Literal Support

```text
1979 - 1982
United Nations Centre for Human Settlements (HABITAT)
Nairobi, Kenya
Development Support Communications Officer
```

```text
Supervise operations of five regional information offices in Amman, Jordan; Bangkok, Thailand; Dakar, Senegal; Mexico City, Mexico and Geneva, Switzerland.
```

```text
1974 - 1978
National Film Board of Canada (NFB)
Montreal, Canada
Audio Visual Consultant
```

```text
1972 - 1973
Chile Films
Santiago, Chile
General Manager Distribution and Exhibition, Head of International Department
```

```text
1970 - 1972
Cine, Televisión y Comunicaciones (CITELCO)
Santiago, Chile
Producer
```

## Competing Derivative Reading

The conversion-job page Markdown at `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-markdown/page-0005.md` instead begins with `1999`, `National Trust Fund for Protected Areas in Peru (PROFONANPE)`, `Television Trust for the Environment (TVE)`, `1998 - 1999 Arca Consulting/ European Commission`, `1997-1998 Klohn Crippen Consultants`, and `SNC Lavalin Agriculture`.

## Evidence Scope

If conversion QA certifies the assigned chunk as the controlling page-5 transcription, it may support narrow narrative claims about Dario Arturo Pulgar's work history, work places, regional assignments, travel, and conference-related film work from 1970 to 1982. It does not state a birth, death, parent, spouse, child, sibling, household, or other family relationship.

## Promotion Hold

Keep this packet and all related page-5 claims on `hold_for_conversion_qa`. Required next actions are to restore or regenerate authoritative access to physical page 5, compare the physical page against both derivative readings, repair manifest/hash drift through the conversion workflow, and run a separate identity-bridge proof review before attaching accepted claims to a canonical person page.
