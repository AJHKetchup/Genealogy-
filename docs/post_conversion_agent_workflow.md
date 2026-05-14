# Post-Conversion Agent Workflow

This playbook starts after source conversion and chunking are complete. It connects immutable prepared sources to the LLM-maintained genealogy wiki without letting draft inference overwrite canonical research.

Codex reference points: [customization](https://developers.openai.com/codex/concepts/customization), [AGENTS.md](https://developers.openai.com/codex/guides/agents-md), [skills](https://developers.openai.com/codex/skills), [subagents](https://developers.openai.com/codex/subagents), and [best practices](https://developers.openai.com/codex/learn/best-practices).

## Pipeline

Use this order:

`raw/converted/` + `raw/chunks/` -> `genealogy-wiki conversion-qc` -> `research/_conversion-review/` QA triage -> `research/_staging/` source packets -> staged claims -> proof review -> canonical wiki promotion.

Rules:

- Keep `raw/sources/`, `raw/converted/`, and `raw/chunks/` immutable during research work.
- Treat chunks as source navigation only. They can repeat source text and provenance, but they must not add summaries, conclusions, claims, or normalized facts.
- Treat conversion QA as a gate, not a rewrite step. Suspicious readings and important page regions are queued separately under `research/_conversion-review/`.
- Let automatic conversion QC narrow the source first. If a 1,000-page source has 10 family-relevant or suspicious pages, queue those pages or regions instead of rereading the whole source.
- Existing converted files from older pipelines are not trusted by existence alone. If a page lacks the current conversion sections or looks like OCR/text-layer/image-only output, it goes back to source-prep as `needs_reread`.
- Evidence extraction may continue for clean chunks from the same source. Chunks overlapping non-`pass` QC pages are marked `blocked_needs_reread` in `research/_agent-queues/evidence-extraction.json`.
- Keep source reliability, conversion confidence, and claim confidence separate throughout the pipeline.
- Put every LLM-derived draft under `research/_staging/` before canonical promotion.
- Promote into canonical wiki folders only after proof review.

## Agent Roles

- `conversion_qa_reviewer`: reads converted Markdown, chunks, page images, conversion manifests, and known family context; writes triage notes, page queues, and suspected correction notes under `research/_conversion-review/` without editing the conversion.
- `evidence_extractor`: reads assigned converted sources or chunks and writes staged source-packet and claim drafts under `research/_staging/`.
- `claim_reviewer`: stays read-only by default and reviews staged drafts for literal support, uncertainty, conflicts, status, confidence, and promotion readiness.
- `identity_researcher`: compares same-person, duplicate, name-variant, and conflict candidates without merging canonical people.
- `wiki_promoter`: the only role allowed to move reviewed drafts into `wiki/claims/`, `wiki/relationships/`, `wiki/people/`, or related canonical product folders. Source packets and transcriptions stay in `research/`.

Subagents are opt-in. Use them only when the user explicitly asks for parallel agents, one agent per source, one agent per question, or similar delegation.

## Staging Contract

Every staged output must include:

- Source path.
- Converted file path and chunk or page reference.
- Source reliability class, reliability score, evidence type, and informant proximity when knowable.
- Conversion confidence or QA concern when the page/region has suspicious readings.
- Literal source support, quoted or transcribed only as needed.
- Translation when the source is not in the working language.
- Interpretation separated from transcription.
- Uncertainty notes, including `[?]`, `[illegible]`, alternatives, or unresolved regions.
- Proposed claim status and confidence.
- Promotion recommendation: `promote`, `revise`, `hold`, or `reject`.

Recommended staging folders:

- `research/_conversion-review/triage/`
- `research/_conversion-review/page-queues/`
- `research/_conversion-review/corrections/`
- `research/_staging/source-packets/`
- `research/_staging/claims/`
- `research/_staging/relationships/`
- `research/_staging/identity/`
- `research/_staging/conflicts/`
- `research/_staging/reviews/`
- `research/_staging/promotions/`

## Review Gates

Before evidence extraction, check conversion QA:

- `genealogy-wiki conversion-qc --root .` has written or refreshed `research/_conversion-review/qc-index.json`.
- `research/_conversion-review/qc-pages.json` exists and `genealogy-wiki agent-queues --root .` has refreshed extraction blocks.
- `genealogy-wiki source-status --root .` shows whether each raw source is ready, still converting, or usable with page holds.
- High-value family pages or regions have been identified for large sources.
- Suspicious readings are documented separately from the verbatim conversion.
- Known family names are used as clues only. For example, if a conversion says `David` but surrounding records and page image suggest `Dario`, queue the page or region for reread instead of silently editing the transcript.
- Page queues include exact page, chunk, row, caption, signature, marginal note, or image-region references.
- Low-relevance pages in huge sources may pass as low priority, while relevant pages move forward for careful extraction.

Before promotion, check:

- The draft points back to source path, converted Markdown, and chunk or page reference.
- Each claim is atomic: one person, relationship, event, date, place, name variant, or source-stated fact.
- Literal support is present and does not rely on a summary.
- Claim confidence accounts for source reliability and conversion confidence instead of treating every source as equal.
- Relationship and identity conclusions remain candidates unless direct evidence supports promotion.
- Conflicts are preserved instead of resolved silently.
- Canonical targets exist or the promotion draft creates them intentionally.

## Promotion

The `wiki_promoter` role applies reviewed staging drafts to canonical wiki pages. Promotion should:

- Move accepted claims and relationship/person/family updates into canonical folders. Keep accepted source packets in `research/source-packets/` and link to them from promoted claims when useful.
- Create or update relationship, identity, conflict, person, family, event, place, source, task, and narrative pages only as supported by reviewed evidence.
- Update `wiki/index.md`.
- Append the action and source/staging paths to `research/log.md`.
- Leave rejected or held drafts in `research/_staging/` with review notes.

Run `genealogy-wiki lint --root .` after promotion and fix canonical lint issues before moving on.
