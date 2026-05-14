# Genealogy Wiki Strategy

This is the genealogy-specific version of the LLM-maintained wiki pattern.

## Core Principle

The wiki is not a loose summary system. It is a family-history research system built from atomic, sourced claims.

Narratives, biographies, family trees, and research summaries are views over the claim and relationship layer. They should not bypass it. Broader historical context belongs in the wiki only when it helps explain this family's lived experience, records, migration, work, community, or constraints.

Confidence is layered: source reliability, conversion confidence, and claim confidence are related but separate. A derivative index, an oral history, and an original civil registration record should not carry the same weight, even when the converted text is clear.

## Requirement Map

| Need | Implementation |
| --- | --- |
| Claim-level evidence | `wiki/claims/` and `research/_templates/claim.md` |
| Relationship confidence | `wiki/relationships/` and `research/_templates/relationship.md` |
| Family tree visualization | `genealogy-wiki tree`, output to `wiki/Family Tree.md` by default |
| Dynamic source material converter | `genealogy-wiki prepare-sources` queues Codex-agent conversion jobs from `raw/sources/` and splits large PDFs into page-range jobs; `genealogy-wiki codex-job`, `codex-assemble`, and `prep-chunk` remain lower-level primitives |
| Transcription vs translation vs interpretation | Required sections in source packet, claim, and photo templates |
| Conflicting records model | `wiki/conflicts/` and `research/_templates/conflict.md` |
| Person identity resolution | `wiki/identity/` and `research/_templates/identity.md` |
| Photo and face clustering | `wiki/photos/`, `research/_templates/photo.md`, and `research/_templates/face-cluster.md` |
| Research task layer | `research/tasks/` and `research/_templates/task.md` |
| Narrative builder | `genealogy-wiki narrative`, output to `wiki/narratives/` |
| Historical context relevance filter | `wiki/context/` plus lint requirement for `linked_entity` |
| Generational chronology checks | `genealogy-wiki lint` parent/child and event chronology checks |
| Lineage-first architecture | `GENEALOGY_WIKI.md`, `wiki/branches/`, `wiki/index.md`, `wiki/Family Tree.md`, and `research/research-plan.md` |
| Conversion QA triage | `research/_conversion-review/`, `conversion-qa-triage`, and the `conversion_qa_reviewer` role |
| Post-conversion draft staging | `research/_staging/`, `docs/post_conversion_agent_workflow.md`, and the post-conversion repo skills/custom agents |

## Workflow

1. Put immutable source files in `raw/sources/`.
2. Run `genealogy-wiki prepare-sources --root .` to inventory raw sources, split large PDFs into page-range jobs, create missing Codex conversion jobs, assemble completed jobs, and chunk completed converted Markdown.
3. Run `genealogy-wiki agent-queues --root . --stale-minutes 360` to write source-prep, conversion-QA, and evidence-extraction queues plus per-task prompt packets, release abandoned worker leases, and reuse cached page-output reviews.
4. Let the source-prep Codex agent and source-converter subagents consume queued page work orders using the project skills. Workers should use `agent-task ... --no-refresh` during bounded batches and refresh queues once at the end. OCR and PDF text layers are hints only, not the conversion authority.
5. Run `genealogy-wiki conversion-qc --root .` to write page-level triage, reread queues, and suspected reading notes.
6. Run conversion QA triage into `research/_conversion-review/` for family-relevant, noisy, handwritten, multilingual, tabular, or conflicting pages and regions.
7. Stage LLM-derived source packets, claims, relationships, identity candidates, conflicts, and proposed wiki updates under `research/_staging/`.
8. Review staged drafts for source path, chunk/page reference, literal support, uncertainty, status/confidence, and promotion recommendation.
9. Promote reviewed material into canonical wiki folders, then link claims into relationship, person, family, event, place, identity, conflict, task, and photo pages.
10. Export indexes with `genealogy-wiki index` or a relationship graph with `genealogy-wiki graph`.
11. Run `genealogy-wiki lint` to catch missing evidence, detached tasks/context, weak packets, and suspicious chronology.
12. Generate tree views with `genealogy-wiki tree`.
13. Compile biographies or branch chapters with `genealogy-wiki narrative`.

## Guardrails

- Do not treat relationship links as facts unless a relationship page supports them.
- Do not collapse same-person candidates into one person page until the identity page supports that conclusion.
- Do not write narrative directly from raw source text.
- Do not write LLM-derived post-conversion drafts directly into canonical wiki folders before review.
- Do not put summaries, claims, or normalized conclusions in `raw/chunks/`.
- Do not edit verbatim converted Markdown just because QA suspects a better reading. Queue the page or region and keep the suspected correction separate.
- Do not let context research drift away from a linked family member, family group, branch, place, event, source, photo, or narrative chapter.
- Do not hide contradictions in prose. Represent them in `wiki/conflicts/`.
- Do not add record-type-specific injectors as the main path. Let the converter infer structure from the source, with optional overlays only when they do not replace the generic evidence model.
- Do not accept "meaning-preserving" header summaries as complete transcription. Exact labels belong in the printed header inventory, even if split tables use shorter field keys.
