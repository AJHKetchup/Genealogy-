---
type: conversion_review_correction
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260524013220161
task_id: evidence-extraction:CHUNK-a048d567968b-P0001-03
chunk_id: CHUNK-a048d567968b-P0001-03
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_sha256: fbbc662e55670a0ad524c3f13256eaef1e62ef32b2b5d1417d601cb40f3313d9
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
converted_sha256: a048d567968b8a75637cfd97335b19160a7580fb273b37a293712691ec678466
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/page-0001-chunk-03.md"
chunk_manifest: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11-codex/manifest.json"
source_packet: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar.md"
source_packet_supplement: "research/_staging/source-packets/chunk-a048d567968b-p0001-03-habitat-revisited-dario-pulgar-supplement-postconv-evidence-extraction-20260524013220161.md"
page_reference: "assigned page 1 in controller/chunk/manifest; family-relevant support is associated in staging with rendered/printed pages 7 and 8"
literal_support: "Dario Pulgar is described as a Chilean UN Habitat Secretariat confrere; the passage states his Chile state film-distribution role under Allende, flight after the 1973 overthrow, Spanish mother tongue, English/French language context, and Vision Habitat distribution-rights work."
conversion_confidence: medium-high
conversion_qa_concern: "The literal Dario Pulgar wording is staged with medium-high confidence, but canonical promotion remains blocked by the unresolved page-reference/chunk-boundary discrepancy between assigned page 1 and image-reviewed support on pages 7-8."
uncertainty: "This is memoir evidence and gives contextual life/work facts, not a vital-record identity proof or kinship relationship. The chunk does not itself prove Arturo, Pulgar-Smith, Pulgar-Arriagada, parents, spouse, or children."
promotion_recommendation: hold_for_conversion_qa
---

# Conversion QA Correction Note

This worker-specific revision keeps the Dario Pulgar evidence in staging and preserves the disagreement between derivative transcripts and image-reviewed evidence.

## Current Findings

The chunk is family relevant because it names Dario Pulgar and gives contextual biographical details: Chilean descriptor, Chile state film-distribution work under Allende, displacement after Pinochet's 1973 overthrow, Spanish mother tongue, English/French language context, and Vision Habitat distribution-rights work.

The staged claim set already keeps those items atomic and held. The relationship staging correctly records negative evidence: no family relationship is stated in this chunk.

## Remaining Blocker

The blocker is conversion/citation QA, not a new substantive contradiction in the Dario Pulgar wording.

- The controller assignment, chunk frontmatter, and chunk manifest identify `CHUNK-a048d567968b-P0001-03` as page 1.
- The chunk body embeds later converted page metadata and text, including Dario Pulgar passages associated by prior staging with rendered/printed pages 7 and 8.
- The source images `page-0007.jpg` and `page-0008.jpg` are present in the Habitat conversion job folder, but this extraction task is not authorized to repair conversion output or page Markdown.

## Recommendation

Keep the Dario Pulgar source packet and claim drafts on `promotion_recommendation: hold_for_conversion_qa` until conversion QA reconciles or formally documents the authoritative source-page citation for the Dario passages. After that, proof review can reconsider the claims as memoir-attributed contextual evidence.

Do not promote relationship candidates from this chunk. It states no parent, spouse, child, sibling, or other kinship relationship.
