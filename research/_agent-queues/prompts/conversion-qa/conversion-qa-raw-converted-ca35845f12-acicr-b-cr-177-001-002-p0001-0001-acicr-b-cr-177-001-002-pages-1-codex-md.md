# Conversion QA Task

Use `$conversion-qa-triage`.

## Assignment

- Role: `conversion_qa_reviewer`
- Converted source: `raw/converted/ca35845f12-acicr-b-cr-177-001-002-p0001-0001-acicr-b-cr-177-001-002-pages-1.codex.md`
- Chunk manifest: `raw/chunks/ca35845f12-acicr-b-cr-177-001-002-p0001-0001-acicr-b-cr-177-001-002-pages-1-codex/manifest.json`
- Original source: `raw/sources/ACICR_B_CR_177_001_002.pdf`
- Output area: `research/_conversion-review`
- Automatic QC triage: `research/_conversion-review/triage/ca35845f12-acicr-b-cr-177-001-002-p0001-0001-acicr-b-cr-177-001-002-pages-1-codex.md`
- Automatic page queue: `research/_conversion-review/page-queues/ca35845f12-acicr-b-cr-177-001-002-p0001-0001-acicr-b-cr-177-001-002-pages-1-codex.md`
- Automatic suspected readings: `research/_conversion-review/corrections/ca35845f12-acicr-b-cr-177-001-002-p0001-0001-acicr-b-cr-177-001-002-pages-1-codex.md`

## Unblock Impact

- Priority rank: 4
- Downstream tasks blocked by this QA task: 1
- Blocked queues: evidence_extraction: 1

Completing this QA task and regenerating queues should release the downstream work summarized below.

| Queue | Task | Lead/Question | Prompt |
| --- | --- | --- | --- |
| evidence_extraction | evidence-extraction:CHUNK-d7d2f04f14d2-P0001-01 | none | research/_agent-queues/prompts/evidence-extraction/evidence-extraction-chunk-d7d2f04f14d2-p0001-01.md |

## Done When

- Automatic QC findings have been checked and refined where needed.
- Family-relevant pages, suspicious readings, likely name drift, table problems, handwriting uncertainty, and missing visual regions are queued under `research/_conversion-review/`.
- Suspected corrections are documented separately from the converted Markdown.
- The task does not promote claims or edit canonical wiki pages.
