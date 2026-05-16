# Conversion QA Task

Use `$conversion-qa-triage`.

## Assignment

- Role: `conversion_qa_reviewer`
- Converted source: `raw/converted/ca35845f12-acicr-b-cr-177-001-002-p0001-0003-acicr-b-cr-177-001-002-pages-1-3.codex.md`
- Chunk manifest: `raw/chunks/ca35845f12-acicr-b-cr-177-001-002-p0001-0003-acicr-b-cr-177-001-002-pages-1-3-codex/manifest.json`
- Original source: `raw/sources/ACICR_B_CR_177_001_002.pdf`
- Output area: `research/_conversion-review`
- Automatic QC triage: `research/_conversion-review/triage/ca35845f12-acicr-b-cr-177-001-002-p0001-0003-acicr-b-cr-177-001-002-pages-1-3-codex.md`
- Automatic page queue: `research/_conversion-review/page-queues/ca35845f12-acicr-b-cr-177-001-002-p0001-0003-acicr-b-cr-177-001-002-pages-1-3-codex.md`
- Automatic suspected readings: `research/_conversion-review/corrections/ca35845f12-acicr-b-cr-177-001-002-p0001-0003-acicr-b-cr-177-001-002-pages-1-3-codex.md`

## Research Analyzer Context

These analyzer opportunities are waiting on this conversion-QA task before staged extraction can proceed.

| Page | Score | Readiness | Signals | Suggested Outputs | Reasons | Chunks |
| ---: | ---: | --- | --- | --- | --- | --- |
| 3 | 35 | blocked_pending_conversion_qa | Général Marotte, M. Des Gouttes, M. Dinichert, M. Sakalauskas, M. Werner, M. de Pflügl, MM, MM. Audeoud, MM. Logoz | source_packet, claim | genealogy lead section names 9 candidate(s); visual evidence cue(s): handwriting | raw/chunks/ca35845f12-acicr-b-cr-177-001-002-p0001-0003-acicr-b-cr-177-001-002-pages-1-3-codex/page-0003-chunk-01.md |
| 1 | 20 | blocked_pending_conversion_qa | M. Boissier, M. Decencière, M. Des Gouttes, M. Dinichert, M. Huber, M. Lipiansky, M. Motta, M. Ratzenberger, M. Werner | source_packet, claim | genealogy lead section names 9 candidate(s) | raw/chunks/ca35845f12-acicr-b-cr-177-001-002-p0001-0003-acicr-b-cr-177-001-002-pages-1-3-codex/page-0001-chunk-01.md |

## Done When

- Automatic QC findings have been checked and refined where needed.
- Family-relevant pages, suspicious readings, likely name drift, table problems, handwriting uncertainty, and missing visual regions are queued under `research/_conversion-review/`.
- Suspected corrections are documented separately from the converted Markdown.
- The task does not promote claims or edit canonical wiki pages.
