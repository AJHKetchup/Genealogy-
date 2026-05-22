---
type: dashboard
status: active
created: 2026-05-17
tags: [dashboard, post-conversion, staging]
---

# Post-Conversion Dashboard

This dashboard is the restart point for automatic work that is not conversion and not external research. The post-conversion lane is API-free: durable queues plus a non-API agent runtime in the Karpathy LLM Wiki style. The PC-off runner is the GitHub-hosted Internal Research Agents workflow; the local PowerShell controller is only an accelerator when this PC is available.

## Current State

- Retired Codex app automation state: [[_agent-queues/post-conversion-buildout]]
- Autopilot architecture: `research/_automation/post-conversion-architecture.json`
- Family presentation architecture: `research/_automation/family-presentation-architecture.json`
- Evidence scoring model: `research/_automation/evidence-scoring-model.json`
- Source relevance feedback: [[_agent-queues/source-relevance-feedback]]
- PC-off workflow: `.github/workflows/internal-research-agents.yml`
- Presentation workflow: `.github/workflows/wiki-site.yml`
- PC-off setup notes: `docs/internal_research_agents_pc_off.md`
- Local controller: `scripts/post-conversion-agent-controller.ps1`
- QA index: [[_conversion-review/qc-index]]
- QA page queue: [[_conversion-review/page-queues/bootstrap-stage-one-source-packets]]
- Source usability: [[_indexes/source-usability]]
- Proof review: [[_staging/reviews/REVIEW-2026-05-17-post-conversion-batch-001]]

## Active Lanes

| Lane | Status | Next action |
| --- | --- | --- |
| Conversion QA gate | active | Reread queued regions before extracting claims that depend on uncertain text. |
| Adaptive conversion | active | High-confidence, high-relevance pages request Pro conversion; complex or suspicious high-relevance pages request Pro with crops. |
| Staging completeness | active | Fill missing `_staging` claims, relationships, identity candidates, conflicts, and reviews. |
| Identity analysis | active | Compare same-person, duplicate, name-variant, and conflict candidates without merging canonical people. |
| Proof review | active | Score source quality, conversion confidence, evidence quantity, agreement/conflict, identity confidence, claim probability, and canonical readiness. |
| Wiki promotion | active, evidence-gated | Scheduled runs use a separate one-worker promotion-only pass after QA/extraction/review; promote only reviewed, evidence-supported material. |
| Family presentation build | active | Rebuild person/tree/narrative-first site from canonical wiki pages after main pushes, hourly schedule, and successful internal agent runs. |

## API-Free Automation

- Automation: GitHub-hosted queue-and-agent harness
- Schedule: minutes 17 and 47 with a 50-minute freshness gate, plus manual dispatch
- Execution: Codex CLI with ChatGPT-managed auth from repository secret
- Provider API dependency: none; provider API keys are forbidden for post-conversion work
- Active runner: `.github/workflows/internal-research-agents.yml`
- Retired local runner: `post-conversion-genealogy-buildout` was removed from the app automation registry because Codex app worktree crons depend on this desktop's process launcher.
- Diagnosis: Codex can do the queue work; GitHub Actions is the no-PC execution surface.
- Parallelism: claim a bounded batch of 3 independent queue tasks per run, up to 6 when write paths are disjoint and risk is low.
- Promotion separation: scheduled runs keep promotion in a separate one-worker pass so canonical wiki updates do not run in the same worker batch as QA, extraction, or proof review.
- Conversion fidelity: do not repeat the same source/page/tier once fulfilled; escalate only to a higher tier when relevance or complexity justifies it.
- Context boundary: outside evidence can ask for a careful reread, but literal transcription changes only when the visible source supports the reading.
- Presentation boundary: the public dashboard is generated from canonical people, relationships, families, events, photos, and narratives; source chunks and queue internals stay in the research backroom.

## Local Controller Commands

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/post-conversion-agent-controller.ps1 -Root . -Once -MaxWorkers 3 -QueueLimit 12
```

Dry run:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/post-conversion-agent-controller.ps1 -Root . -Once -DryRun -NoRefresh -NoWorkers
```

## High-Value Staged Sources

- [[_staging/source-packets/SP-STAGE-2026-05-15-Heinz-Family-Context]]
- [[_staging/source-packets/SP-STAGE-1889-Daniel-Pulgar-Arriagada]]
- [[_staging/source-packets/SP-STAGE-1888-Fidelmiro-Segundo-Pulgar-Arriagada]]
- [[_staging/source-packets/SP-STAGE-1953-Andes-Pulgar-Family]]
- [[_staging/source-packets/SP-STAGE-1959-I94-Dario-A-Pulgar]]

## Holds

- Living-family privacy is not a standalone hold for this internal family project; user approval was recorded on 2026-05-17. Evidence support and proof review still apply.
- The 1888 father-name field stays held until reread.
- The 1953 Pulgar travel group remains a relationship candidate, not a family relationship.
- The 1959 Dario A. Pulgar birthdate and Concepcion address stay held until reread.
- Dario identity matches remain open candidates.
