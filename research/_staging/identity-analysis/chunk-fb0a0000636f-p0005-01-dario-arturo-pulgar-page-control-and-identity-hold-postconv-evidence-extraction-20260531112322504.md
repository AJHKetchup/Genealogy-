---
type: identity_conflict_analysis
status: draft
role: evidence_extractor
worker: postconv-evidence-extraction-20260531112322504
task_id: evidence-extraction:CHUNK-fb0a0000636f-P0005-01
subject: "Dario Arturo Pulgar, document-level CV subject"
source: raw/sources/CV of Dario Arturo Pulgar.pdf
source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0005-01-cv-dario-arturo-pulgar-page-control-hold-postconv-evidence-extraction-20260531112322504.md
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0005-chunk-01.md
chunk_id: CHUNK-fb0a0000636f-P0005-01
page_reference: page 5
conflict_type: derivative_transcription_page_control_and_identity_bridge
analysis_status: hold_for_conversion_qa
canonical_readiness: not_ready
promotion_recommendation: hold_for_conversion_qa
---

# Identity/Conflict Hold: Page 5 CV Claims

## Blockers

1. The assigned chunk reads page 5 as a 1979-1970 work-history page for HABITAT, NFB, Chile Films, and CITELCO.
2. The conversion-job `page-markdown/page-0005.md` reads page 5 as a 1999-1997 work-history page for PROFONANPE, TVE, Arca/European Commission, Klohn Crippen, and SNC Lavalin.
3. The original PDF and `page-images/page-0005.jpg` are absent in this checkout, so no physical page-control review was possible in this task.
4. The manifest repeats `CHUNK-fb0a0000636f-P0005-01` with incompatible counts and hashes, and the observed converted-file hash differs from the recorded converted hash.
5. The assigned page body does not state `Dario Arturo Pulgar-Smith`, Alexander John Heinz, Jose, Juana, or any family relationship.

## Identity Handling

This extraction uses `Dario Arturo Pulgar` only as the document-level CV subject supplied by the source title/path. It does not merge the CV subject into `wiki/people/dario-arturo-pulgar-smith.md`, `Dario Pulgar Arriagada`, a Jose/Juana parent cluster, or any other canonical person.

After conversion QA certifies the controlling physical page-5 text, a separate identity-bridge proof review is still required before attaching accepted CV claims to any canonical person page.

## Recommendation

Keep all page-5 work-history claims staged with `promotion_recommendation: hold_for_conversion_qa`. Do not promote any page-5 claim, relationship, or identity attachment until authoritative page control and identity bridge review are complete.
