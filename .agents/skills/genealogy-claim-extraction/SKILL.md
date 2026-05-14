---
name: genealogy-claim-extraction
description: Extract atomic genealogy claims from converted source chunks or staged source packets into `research/_staging/claims/`. Use for names, dates, places, events, relationships, identity clues, occupations, residences, and source-stated facts that need proof review before canonical promotion.
---

# Genealogy Claim Extraction

Use this skill to turn prepared source evidence into staged atomic claims. Claims are drafts until reviewed and promoted.

## Claim Rules

- Create one atomic claim per fact.
- Distinguish source-stated facts from researcher interpretation.
- Keep uncertain readings uncertain with `[?]`, `[illegible]`, alternatives, or date qualifiers.
- Use `draft`, `possible`, `probable`, `disputed`, or `rejected` for staged status. Do not mark a new staged claim `accepted` unless the user explicitly asks.
- Do not create canonical relationship or person facts from claim drafts.

## Workflow

1. Read the assigned `raw/chunks/` manifest, chunk files, converted source, staged source packet, and any relevant `research/_conversion-review/` page queue or suspected-correction note.
2. Extract candidate claims only when literal support is visible.
3. Write claim drafts under `research/_staging/claims/`.
4. Include source path, converted file, chunk/page reference, literal support, interpretation, uncertainty, source reliability, conversion confidence, proposed claim confidence, and promotion recommendation.
5. If a claim depends on a suspicious conversion reading, mark it `hold` or `needs-reread` until the referenced page or region has been checked.
6. Note possible relationship, identity, conflict, task, or source-packet follow-ups, but keep them staged.

## Atomic Claim Shape

Each staged claim should answer:

- Subject: who or what the claim is about.
- Predicate: what is being asserted.
- Object: value, person, place, event, relationship, or source-stated text.
- Date and place, if present.
- Source support: the exact line, field, caption, table row, or page region.
- Source reliability: original, derivative, authored, index, transcript, oral-history, unknown, plus a conservative 0-10 score.
- Conversion confidence: whether the reading itself is high, medium, low, or needs reread.
- Confidence rationale: why the proposed score is conservative.

## Guardrails

- Do not edit canonical `wiki/claims/`.
- Do not infer parent, spouse, sibling, or same-person relationships from proximity alone.
- Do not normalize names, places, or dates inside literal support.
- Preserve conflicting claims as separate drafts instead of resolving them in prose.
