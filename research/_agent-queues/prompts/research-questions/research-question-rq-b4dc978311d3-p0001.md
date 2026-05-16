# Research Question Task

Use `$genealogy-claim-extraction` if evidence can be staged from the cited chunks.

## Assignment

- Question: `research/questions/rq-b4dc978311d3-p0001.md`
- Source: `raw/sources/ACICR_B_CR_177_001_002.pdf`
- Converted source: `raw/converted/ca35845f12-acicr-b-cr-177-001-002-p0001-0003-acicr-b-cr-177-001-002-pages-1-3.codex.md`
- Page: 1
- Chunks: `raw/chunks/ca35845f12-acicr-b-cr-177-001-002-p0001-0003-acicr-b-cr-177-001-002-pages-1-3-codex/page-0001-chunk-01.md`

## Conversion QA Gate

This research question touches a converted source that still needs conversion QA before staged evidence extraction.

- Status: `blocked_pending_conversion_qa`
- Conversion QA task: `conversion-qa:raw-converted-ca35845f12-acicr-b-cr-177-001-002-p0001-0003-acicr-b-cr-177-001-002-pages-1-3-codex-md`
- Expected triage note: `research/_conversion-review/triage/ca35845f12-acicr-b-cr-177-001-002-p0001-0003-acicr-b-cr-177-001-002-pages-1-3-codex.md`
- Expected page queue: `research/_conversion-review/page-queues/ca35845f12-acicr-b-cr-177-001-002-p0001-0003-acicr-b-cr-177-001-002-pages-1-3-codex.md`
- Expected suspected readings: `research/_conversion-review/corrections/ca35845f12-acicr-b-cr-177-001-002-p0001-0003-acicr-b-cr-177-001-002-pages-1-3-codex.md`

Do not extract claims or create staged evidence from this page until the conversion QA task is completed and the queue is regenerated.

## Suggested Staging Outputs

- `source_packet` -> `research/_staging/source-packets`: Preserve page-level literal support and provenance before extracting claims.
- `claim` -> `research/_staging/claims`: Names or life-event cues may support atomic fact drafts after source review.

## Done When

- The question is answered in `research/_staging/` drafts or left as a documented hold.
- Any staged draft includes source path, converted file, chunk/page reference, literal support, uncertainty notes, and promotion recommendation.
- No canonical wiki page is edited directly.
