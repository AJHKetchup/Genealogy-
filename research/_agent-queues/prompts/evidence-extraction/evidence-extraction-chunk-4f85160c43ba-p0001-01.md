# Evidence Extraction Task

Use `$genealogy-claim-extraction`.

## Assignment

- Role: `evidence_extractor`
- Chunk: `raw/chunks/ca35845f12-acicr-b-cr-177-001-002-p0001-0002-acicr-b-cr-177-001-002-pages-1-2-codex/page-0001-chunk-01.md`
- Converted source: `raw/converted/ca35845f12-acicr-b-cr-177-001-002-p0001-0002-acicr-b-cr-177-001-002-pages-1-2.codex.md`
- Chunk manifest: `raw/chunks/ca35845f12-acicr-b-cr-177-001-002-p0001-0002-acicr-b-cr-177-001-002-pages-1-2-codex/manifest.json`
- Original source: `raw/sources/ACICR_B_CR_177_001_002.pdf`
- Page range: 1-1
- Staging area: `research/_staging`

## Conversion QA Gate

- Status: `blocked_pending_conversion_qa`
- Conversion QA task: `conversion-qa:raw-converted-ca35845f12-acicr-b-cr-177-001-002-p0001-0002-acicr-b-cr-177-001-002-pages-1-2-codex-md`
- Expected triage note: `research/_conversion-review/triage/ca35845f12-acicr-b-cr-177-001-002-p0001-0002-acicr-b-cr-177-001-002-pages-1-2-codex.md`
- Expected page queue: `research/_conversion-review/page-queues/ca35845f12-acicr-b-cr-177-001-002-p0001-0002-acicr-b-cr-177-001-002-pages-1-2-codex.md`
- Expected suspected readings: `research/_conversion-review/corrections/ca35845f12-acicr-b-cr-177-001-002-p0001-0002-acicr-b-cr-177-001-002-pages-1-2-codex.md`

Do not extract claims from this chunk until the conversion QA task is completed and the extraction queue is regenerated.


## Done When

- Relevant source packets, atomic claim drafts, relationship candidates, identity/conflict candidates, and research tasks are written under `research/_staging/`.
- Every draft has source path, converted file, chunk/page reference, literal support, conversion confidence/QA concern, uncertainty, and promotion recommendation.
- No canonical wiki pages are edited by this extraction task.
