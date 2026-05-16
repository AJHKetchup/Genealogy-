# Conversion QA Task

Use `$conversion-qa-triage`.

## Assignment

- Role: `conversion_qa_reviewer`
- Converted source: `raw/converted/ca35845f12-acicr-b-cr-177-001-002-p0004-0005-acicr-b-cr-177-001-002-pages-4-5.codex.md`
- Chunk manifest: `raw/chunks/ca35845f12-acicr-b-cr-177-001-002-p0004-0005-acicr-b-cr-177-001-002-pages-4-5-codex/manifest.json`
- Original source: `raw/sources/ACICR_B_CR_177_001_002.pdf`
- Output area: `research/_conversion-review`
- Automatic QC triage: `research/_conversion-review/triage/ca35845f12-acicr-b-cr-177-001-002-p0004-0005-acicr-b-cr-177-001-002-pages-4-5-codex.md`
- Automatic page queue: `research/_conversion-review/page-queues/ca35845f12-acicr-b-cr-177-001-002-p0004-0005-acicr-b-cr-177-001-002-pages-4-5-codex.md`
- Automatic suspected readings: `research/_conversion-review/corrections/ca35845f12-acicr-b-cr-177-001-002-p0004-0005-acicr-b-cr-177-001-002-pages-4-5-codex.md`

## Page Verification Artifacts

Use these page-scoped artifacts to compare the converted Markdown against rendered page images and existing page-level conversion outputs.

| Page | Source Page | Page Image | Page Markdown | Extracted Images | Work Order |
| ---: | ---: | --- | --- | --- | --- |
| 4 | 4 | raw/codex-conversion-jobs/ca35845f12-acicr-b-cr-177-001-002-p0004-0005-acicr-b-cr-177-001-002-pages-4-5/page-images/page-0004.jpg | raw/codex-conversion-jobs/ca35845f12-acicr-b-cr-177-001-002-p0004-0005-acicr-b-cr-177-001-002-pages-4-5/page-markdown/page-0004.md | raw/codex-conversion-jobs/ca35845f12-acicr-b-cr-177-001-002-p0004-0005-acicr-b-cr-177-001-002-pages-4-5/extracted-images/page-0004 | raw/codex-conversion-jobs/ca35845f12-acicr-b-cr-177-001-002-p0004-0005-acicr-b-cr-177-001-002-pages-4-5/work-orders/page-0004.md |
| 5 | 5 | raw/codex-conversion-jobs/ca35845f12-acicr-b-cr-177-001-002-p0004-0005-acicr-b-cr-177-001-002-pages-4-5/page-images/page-0005.jpg | raw/codex-conversion-jobs/ca35845f12-acicr-b-cr-177-001-002-p0004-0005-acicr-b-cr-177-001-002-pages-4-5/page-markdown/page-0005.md | raw/codex-conversion-jobs/ca35845f12-acicr-b-cr-177-001-002-p0004-0005-acicr-b-cr-177-001-002-pages-4-5/extracted-images/page-0005 | raw/codex-conversion-jobs/ca35845f12-acicr-b-cr-177-001-002-p0004-0005-acicr-b-cr-177-001-002-pages-4-5/work-orders/page-0005.md |

## Unblock Impact

- Priority rank: 3
- Downstream tasks blocked by this QA task: 2
- Blocked queues: evidence_extraction: 2

Completing this QA task and regenerating queues should release the downstream work summarized below.

| Queue | Task | Lead/Question/Page | Prompt |
| --- | --- | --- | --- |
| evidence_extraction | evidence-extraction:CHUNK-b88c946c7236-P0004-01 | page 4 | research/_agent-queues/prompts/evidence-extraction/evidence-extraction-chunk-b88c946c7236-p0004-01.md |
| evidence_extraction | evidence-extraction:CHUNK-b88c946c7236-P0005-01 | page 5 | research/_agent-queues/prompts/evidence-extraction/evidence-extraction-chunk-b88c946c7236-p0005-01.md |

## Done When

- Automatic QC findings have been checked and refined where needed.
- Family-relevant pages, suspicious readings, likely name drift, table problems, handwriting uncertainty, and missing visual regions are queued under `research/_conversion-review/`.
- Suspected corrections are documented separately from the converted Markdown.
- The task does not promote claims or edit canonical wiki pages.
