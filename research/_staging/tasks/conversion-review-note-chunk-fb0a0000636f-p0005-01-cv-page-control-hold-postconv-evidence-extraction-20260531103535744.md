---
type: research_task
status: draft
task_type: conversion_qa
task_id: evidence-extraction:CHUNK-fb0a0000636f-P0005-01
worker: postconv-evidence-extraction-20260531103535744
subject: "CV of Dario Arturo Pulgar page 5 page-control conflict"
source: "raw/sources/CV of Dario Arturo Pulgar.pdf"
converted_file: "raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md"
chunk: "raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md"
chunk_id: "CHUNK-fb0a0000636f-P0005-01"
page_reference: "page 5"
source_packet: "research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-hold-postconv-evidence-extraction-20260531103535744.md"
priority: high
conversion_confidence: low
conversion_qa_concern: "Physical page 5 control is unresolved because assigned chunk text conflicts with conversion-job page Markdown and manifest/hash drift remains."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Required: CV Page 5

## Blocker

The assigned chunk for page 5 reads as 1979-1970 work history, while `raw/codex-conversion-jobs/.../page-markdown/page-0005.md` reads as 1999-1997 consulting work. The source PDF is not present in the checkout, no authoritative rendered page image was available to this extraction task, and the chunk manifest contains duplicate entries for `CHUNK-fb0a0000636f-P0005-01` with conflicting recorded sizes/hashes.

## Required Follow-Up

Restore or regenerate authoritative access to physical page 5, compare it against both derivative readings, repair the converted-file/chunk manifest/hash drift through the conversion workflow, and then rerun proof review. Only after page control is certified should any held work-history claim or identity bridge be considered for canonical promotion.
