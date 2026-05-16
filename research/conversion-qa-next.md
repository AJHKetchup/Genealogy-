# Conversion QA Next

Generated: 2026-05-16T15:36:13Z

This is the current highest-impact conversion-QA focus packet. It is an operational queue aid, not a source interpretation or canonical genealogy artifact.

## Focus Task

- Priority rank: 1
- Task id: `conversion-qa:raw-converted-ca35845f12-acicr-b-cr-177-001-002-p0001-0003-acicr-b-cr-177-001-002-pages-1-3-codex-md`
- Status: `todo`
- Converted file: `raw/converted/ca35845f12-acicr-b-cr-177-001-002-p0001-0003-acicr-b-cr-177-001-002-pages-1-3.codex.md`
- QA prompt: `research/_agent-queues/prompts/conversion-qa/conversion-qa-raw-converted-ca35845f12-acicr-b-cr-177-001-002-p0001-0003-acicr-b-cr-177-001-002-pages-1-3-codex-md.md`
- Triage note: `research/_conversion-review/triage/ca35845f12-acicr-b-cr-177-001-002-p0001-0003-acicr-b-cr-177-001-002-pages-1-3-codex.md`
- Page queue: `research/_conversion-review/page-queues/ca35845f12-acicr-b-cr-177-001-002-p0001-0003-acicr-b-cr-177-001-002-pages-1-3-codex.md`
- Suspected readings: `research/_conversion-review/corrections/ca35845f12-acicr-b-cr-177-001-002-p0001-0003-acicr-b-cr-177-001-002-pages-1-3-codex.md`

## Unblock Impact

- Downstream tasks unlocked after QA completion and queue regeneration: 24
- Blocked queues: evidence_extraction: 3, external_research: 3, research_leads: 14, research_questions: 2, research_staging_backlog: 2

## Downstream Examples

| Queue | Task | Lead/Question/Page | Prompt |
| --- | --- | --- | --- |
| evidence_extraction | evidence-extraction:CHUNK-83011af124e2-P0003-01 | page 3 | research/_agent-queues/prompts/evidence-extraction/evidence-extraction-chunk-83011af124e2-p0003-01.md |
| evidence_extraction | evidence-extraction:CHUNK-83011af124e2-P0001-01 | page 1 | research/_agent-queues/prompts/evidence-extraction/evidence-extraction-chunk-83011af124e2-p0001-01.md |
| evidence_extraction | evidence-extraction:CHUNK-83011af124e2-P0002-01 | page 2 | research/_agent-queues/prompts/evidence-extraction/evidence-extraction-chunk-83011af124e2-p0002-01.md |
| research_questions | research-question:RQ-9ae7e6a2ac30-P0003 | RQ-9ae7e6a2ac30-P0003 | research/_agent-queues/prompts/research-questions/research-question-rq-9ae7e6a2ac30-p0003.md |
| research_questions | research-question:RQ-b4dc978311d3-P0001 | RQ-b4dc978311d3-P0001 | research/_agent-queues/prompts/research-questions/research-question-rq-b4dc978311d3-p0001.md |
| research_leads | research-lead:m-des-gouttes | M. Des Gouttes | research/_agent-queues/prompts/research-leads/research-lead-m-des-gouttes.md |
| research_leads | research-lead:m-dinichert | M. Dinichert | research/_agent-queues/prompts/research-leads/research-lead-m-dinichert.md |
| research_leads | research-lead:m-werner | M. Werner | research/_agent-queues/prompts/research-leads/research-lead-m-werner.md |
| research_leads | research-lead:g-n-ral-marotte | Général Marotte | research/_agent-queues/prompts/research-leads/research-lead-g-n-ral-marotte.md |
| research_leads | research-lead:m-boissier | M. Boissier | research/_agent-queues/prompts/research-leads/research-lead-m-boissier.md |
| research_leads | research-lead:m-de-pfl-gl | M. de Pflügl | research/_agent-queues/prompts/research-leads/research-lead-m-de-pfl-gl.md |
| research_leads | research-lead:m-decenci-re | M. Decencière | research/_agent-queues/prompts/research-leads/research-lead-m-decenci-re.md |

## Done When

- Complete the QA prompt listed above.
- Write/refine conversion-QA artifacts under `research/_conversion-review/`.
- Mark the conversion-QA task done in task state.
- Regenerate queues so blocked extraction, lead, question, and external-research work can move forward.
