# Evidence Extraction Task

Use `$genealogy-claim-extraction`.

## Assignment

- Role: `evidence_extractor`
- Chunk: `raw/chunks/ca35845f12-acicr-b-cr-177-001-002-p0001-0003-acicr-b-cr-177-001-002-pages-1-3-codex/page-0001-chunk-01.md`
- Converted source: `raw/converted/ca35845f12-acicr-b-cr-177-001-002-p0001-0003-acicr-b-cr-177-001-002-pages-1-3.codex.md`
- Chunk manifest: `raw/chunks/ca35845f12-acicr-b-cr-177-001-002-p0001-0003-acicr-b-cr-177-001-002-pages-1-3-codex/manifest.json`
- Original source: `raw/sources/ACICR_B_CR_177_001_002.pdf`
- Page range: 1-1
- Priority rank: 2
- Priority reason: `research_analyzer_staging_backlog`
- Staging area: `research/_staging`

## Research Analyzer Staging Handoff

The analyzer flagged page-level staged work for this chunk. Use these targets only after conversion QA clears the source.

- Max analyzer score: 20

Backlog items:

- `staging-backlog:raw-converted-ca35845f12-acicr-b-cr-177-001-002-p0001-0003-acicr-b-cr-177-001-002-pages-1-3-codex-md:p0001` page 1, score 20, outputs: claim, source_packet

Suggested staging outputs:

- `claim` -> `research/_staging/claims`: Names or life-event cues may support atomic fact drafts after source review.
- `source_packet` -> `research/_staging/source-packets`: Preserve page-level literal support and provenance before extracting claims.

## Conversion QA Gate

- Status: `blocked_pending_conversion_qa`
- Conversion QA task: `conversion-qa:raw-converted-ca35845f12-acicr-b-cr-177-001-002-p0001-0003-acicr-b-cr-177-001-002-pages-1-3-codex-md`
- Expected triage note: `research/_conversion-review/triage/ca35845f12-acicr-b-cr-177-001-002-p0001-0003-acicr-b-cr-177-001-002-pages-1-3-codex.md`
- Expected page queue: `research/_conversion-review/page-queues/ca35845f12-acicr-b-cr-177-001-002-p0001-0003-acicr-b-cr-177-001-002-pages-1-3-codex.md`
- Expected suspected readings: `research/_conversion-review/corrections/ca35845f12-acicr-b-cr-177-001-002-p0001-0003-acicr-b-cr-177-001-002-pages-1-3-codex.md`

Do not extract claims from this chunk until the conversion QA task is completed and the extraction queue is regenerated.


## Done When

- Relevant source packets, atomic claim drafts, relationship candidates, identity/conflict candidates, and research tasks are written under `research/_staging/`.
- Every draft has source path, converted file, chunk/page reference, literal support, conversion confidence/QA concern, uncertainty, and promotion recommendation.
- No canonical wiki pages are edited by this extraction task.
