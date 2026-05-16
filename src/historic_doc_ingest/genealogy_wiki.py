from __future__ import annotations

import argparse
import base64
import concurrent.futures
from contextlib import contextmanager
import hashlib
import html as html_lib
import json
import os
import re
import shutil
import subprocess
import time
import tempfile
import threading
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass, field
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

from historic_doc_ingest.raw_cloud import (
    build_raw_cloud_manifest,
    build_raw_cloud_manifest_from_remote,
    cleanup_remote_json_manifests,
    upload_derived_assets_to_cloud,
    load_raw_cloud_config,
    restore_raw_from_cloud,
    upload_raw_to_cloud,
    verify_raw_cloud,
    write_derived_asset_inventory,
    write_raw_cloud_inventory,
)


GENEALOGY_SCHEMA = """# Genealogy Wiki Operating Manual

This wiki follows the LLM-maintained wiki pattern, adapted for genealogical research.

## Layers

- `raw/`: immutable source material. Store original PDFs, images, downloaded records, exports, correspondence, converted Markdown, chunks, and conversion jobs here. Do not edit these files after ingest.
- `research/`: source/research Obsidian vault. This drives source inspection, conversion dashboards, page transcription, conversion QA, staging drafts, indexes, templates, and agent work queues.
- `wiki/`: family-history Obsidian vault. This is the final evolving product for people, families, branches, narratives, photos, context, timelines, and tree views.
- `research/00 Research Start.md`: Obsidian front door for source work and agent flow.
- `research/index.md`: source-oriented catalog of sources, source packets, transcriptions, conversion views, staging, and agent work.
- `research/log.md`: append-only chronological record of source preparation, conversion, QA, staging, agent work, and promoted product changes.
- `research/research-plan.md`: prioritized open work, next searches, unresolved questions, and hypotheses to test.
- `research/questions/` and `research/tasks/`: research questions and work queues outside the product vault.
- `wiki/Family Tree.md`: front-facing family tree view generated from proof-layer relationship pages in `research/relationships/`.
- `wiki/index.md`: lineage-first catalog of families, branches, people, relationships, claims, narratives, and family-history pages.

## Genealogy Rules

- Do not merge two people unless evidence supports identity. Keep possible duplicates separate and cross-link them as candidates.
- Every fact about a person, relationship, event, name variant, date, or place needs a source citation or an explicit `unsourced` marker.
- Keep source reliability, conversion confidence, and claim confidence separate. A primary record with a clear image is different from an authored family story, an index, a derivative transcript, or a low-confidence reading.
- Distinguish evidence from conclusion. A record may say something; the wiki may conclude something else after weighing conflicts.
- Preserve uncertainty. Use `about`, `before`, `after`, `between`, `possibly`, and `probably` instead of inventing precision.
- Track negative evidence, such as searched collections where a person was not found.
- Keep original spelling, place names, and record language in source notes. Normalize only in separate interpretation fields.
- Prefer small, linked pages over giant narrative dumps.
- Treat atomic claims as the foundation of the system. A biography, family tree, or narrative may summarize claims, but claims are the auditable units.
- Keep relationship assertions separate from person pages and assign relationship type, status, confidence, and evidence.
- Keep source transcription, translation, interpretation, and uncertainty in separate sections.
- Context research is allowed only when it explains the lived history of this family through a person, relationship, event, place, source, photo, or narrative chapter.
- Every canonical person page should eventually have a narrative layer: a sourced life story in `wiki/narratives/` built only from accepted or probable claims plus relevant family-specific historical context.
- Treat `raw/chunks/` as non-interpretive navigation aids. Chunks may repeat source text and provenance, but they must not add summaries, normalized facts, or claims.
- Keep rough discovery/OCR/Docling output separate from evidence-grade conversion. Converter mechanisms may judge technical readability, but research agents decide research importance and request upgraded Gemini conversion when context makes a page matter.
- Treat `research/_conversion-review/` as the quality gate between verbatim conversion and research extraction. Queue suspicious readings, likely name drift, and family-relevant pages there without editing converted Markdown.
- Treat QC-held pages as page-specific extraction blocks. Do not freeze a whole archive when only exact pages or regions need reread.
- Treat old OCR, text-layer, or image-only page outputs as repair inputs unless they satisfy the current full page conversion contract.
- Put LLM-derived source packets, claims, relationship candidates, identity candidates, and person-page updates in `research/_staging/` first.
- Keep source-context portrait crops, face references, and face-cluster drafts in `research/_staging/photos/` until explicitly promoted as product-ready photo pages.
- Only a review/promotion pass, performed by the `wiki_promoter` role or an equivalent explicit human direction, may move staged material into canonical wiki folders.
- Keep research navigation, plans, logs, questions, and tasks in `research/`. Keep `wiki/` focused on the genealogy product and family-tree view.

## Lineage-First Architecture

Organize from lineage goals outward:

Family -> Branch -> Person -> Relationship -> Event -> Place -> Source -> Claim -> Narrative.

The wiki can still cross-link freely, but this hierarchy is the default path for research and review.

## Ingest Workflow

When a new source arrives:

1. Add it to `raw/sources/`.
2. Run `genealogy-wiki prepare-sources --root .` to inventory sources, split large PDFs into page-range jobs, create missing Codex conversion jobs, assemble completed jobs, and chunk completed conversions.
3. Run `genealogy-wiki agent-queues --root . --stale-minutes 360` to write source-prep and evidence-extraction queues plus per-task prompt packets, release abandoned task leases, and reuse cached page-output reviews.
4. Research agents can run `genealogy-wiki source-relevance mark ...` when an exact page becomes newly important enough to deserve Pro or Pro+crops treatment. Converter jobs should only auto-upgrade for technical unreadability, not for genealogy importance.
5. Run `genealogy-wiki source-status --root .` to see which raw sources are usable, still converting, or held only on specific pages.
6. Let source-prep Codex agents and page/range subagents consume queued work orders using the project skills. Workers should use `agent-task ... --no-refresh` during a bounded batch, then refresh queues once at the end. OCR and PDF text layers are hints only, not the conversion authority.
7. Create staged source packets and staged claim drafts under `research/_staging/` from `raw/converted/`, `raw/chunks/`, and research relevance feedback.
8. Keep separated transcription, translation, interpretation, uncertainty, and promotion recommendation sections in staged drafts.
9. Review staged claims for literal support, source path, chunk/page reference, uncertainty, status, confidence, and conflicts.
10. Run `genealogy-wiki promote-staged --root .` after review to promote eligible staged material into `research/claims/`, `research/relationships/`, product person pages, indexes, and the generated family tree; source packets stay in `research/source-packets/`.
11. Run `genealogy-wiki lint --root .` and fix canonical lint issues before moving on.
12. Review the promotion manifest under `research/_staging/promotions/` and the backstage entry in `research/log.md`.

## Post-Conversion Agent Workflow

After conversion, use this order:

`raw/converted/` + `raw/chunks/` -> research agents -> page-scoped `source-relevance mark` feedback for important pages -> upgraded conversion when needed -> `research/_staging/` source packets -> staged claims -> proof review -> research proof layer plus wiki product updates.

Staged outputs must include source path, chunk or page reference, literal support, uncertainty notes, proposed claim status, and a promotion recommendation. Canonical pages should cite reviewed staged evidence, not raw chunks directly. Parallel subagents are optional and must be explicitly requested by the user.

## Query Workflow

When answering a genealogy question:

1. Read `wiki/index.md` first for the family-history product, then check `research/index.md` only when source or task context is needed.
2. Read the relevant person, family, source, evidence, conflict, and place pages.
3. Answer with citations to wiki pages and source pages.
4. If the answer creates a useful synthesis, file it as a new or updated wiki page.
5. Log the query and outcome.

## Lint Workflow

Periodically check for:

- Person pages with no source links.
- Family pages missing relationship evidence.
- Event pages without dates, places, or participants.
- Conflicting dates, places, names, or relationships not represented in `wiki/conflicts/`.
- Orphaned pages missing links from `wiki/index.md`.
- Source pages that do not list extracted claims.
- Source pages missing source reliability notes.
- Research questions in `research/questions/` that have no next action.
- Possible duplicates that need identity analysis.
- Claim pages missing status, confidence, source, or evidence.
- Relationship pages missing relationship type, status, confidence, or supporting claims.
- Source packets missing transcription, translation, interpretation, or uncertainty separation.
- Context pages without a linked genealogy entity.
- Suspicious chronology, such as a parent born after a child, childbearing before age 12, marriage after death, or events after death.

## Citation Style

Use this compact style in wiki pages:

```markdown
[^S001]: [[sources/S001-1850-us-census-smith-household]].
```

Inside facts, cite the source footnote:

```markdown
- Birth: about 1842, Ohio.[^S001]
```

## Page Naming

- People: `people/surname-given-birthyear-deathyear.md`
- Families: `families/surname-surname-marriageyear.md`
- Places: `places/country-region-locality.md`
- Branches: `branches/branch-name.md`
- Relationships: `research/relationships/R001-person-person-relationship.md`
- Events: `events/EV001-short-event.md`
- Research sources: `research/sources/S001-short-title.md`
- Research source packets: `research/source-packets/SP001-short-title.md`
- Claims: `research/claims/CL001-short-claim.md`
- Conversion QA: `research/_conversion-review/<triage|page-queues|corrections>/<source-id>.md`
- Staged drafts: `research/_staging/<workflow>/<draft-id>.md`
- Identity: `identity/ID001-person-candidates.md`
- Product photos: `photos/PH001-short-description.md`
- Product face clusters: `photos/FC001-unknown-cluster.md`
- Staged photo evidence: `research/_staging/photos/<photo-or-face-reference>.md`
- Research tasks: `research/tasks/T001-short-task.md`
- Narratives: `narratives/N001-short-title.md`
- Conflicts: `conflicts/C001-short-topic.md`
- Research questions: `research/questions/Q001-short-question.md`
"""


INDEX_TEMPLATE = """# Family History Index

Start with the tree, then follow people, families, branches, places, photos, and narratives.

## Family Tree

- [[Family Tree]]

## People

## Branches

## Families

## Events

## Places

## Conflicts

## Identity Resolution

## Photos And Face Clusters

## Narratives

## Context

## Timelines
"""


FAMILY_TREE_TEMPLATE = """---
type: tree
status: generated
tags: [tree]
---

# Family Tree

```mermaid
flowchart TD
  empty[No relationship pages found]
```

This view shows the family connections currently represented in the wiki.
"""


LOG_TEMPLATE = """# Genealogy Wiki Log

## [{today}] init | Genealogy wiki created

- Created raw source layer, wiki layer, schema, index, log, and templates.
"""


RESEARCH_PLAN_TEMPLATE = """# Research Plan

This is the research-vault work queue. Agents should keep it useful for online research, archive follow-up, source review, and unresolved proof problems.

## Current Focus

## Priority Questions

## Next Searches

## Sources To Find Or Review

## Hypotheses To Test

## Negative Searches

## Lineage Goals

## Recently Promoted Findings
"""


RESEARCH_INDEX_TEMPLATE = """# Research Vault Index

## Start Here

- [[00 Research Start]]
- [[research-plan]]
- [[Conversion Dashboard]]
- [[log]]

## Sources

## Source Packets

## Claims

## Relationships

## Evidence

## Context

## Events

## Source Transcriptions

## Conversion Views

## Agent Work

## Questions

## Tasks

## Staging
"""


RESEARCH_START_TEMPLATE = """# Research Start

This Obsidian vault drives the source engine and agent stack.

Use this vault for source intake, conversion review, page-level transcription, staged extraction, and proof-review handoff. Use the sibling `wiki/` vault for the final family-history product, lineage pages, narratives, and tree views.

## Working Flow

1. Put immutable source files under `raw/sources/`.
2. Prepare conversion jobs, assembled Markdown, chunks, and source inventories under `raw/`.
3. Inspect prepared conversions from [[Conversion Dashboard]] and page-level transcription notes.
4. Put QA notes under `_conversion-review/` and LLM-derived drafts under `_staging/`.
5. Promote reviewed claims, relationships, people, families, narratives, and tree updates into `wiki/`.

## Boundaries

- `sources`, `source-packets`, and `sources/transcriptions` are the research/source view.
- `questions`, `tasks`, `research-plan`, `_conversion-review`, `_staging`, `_agents`, `_indexes`, and `_templates` are the agent stack.
- The `wiki/` vault is the readable family-history product and should not receive unreviewed extraction drafts.
"""


RESEARCH_LOG_TEMPLATE = """# Research Vault Log

## [{today}] init | Research vault created

- Created the source/research vault, source shelves, conversion review folders, staging folders, agent folders, indexes, and templates.
"""


TEMPLATES = {
    "branch.md": """---
type: branch
status: stub
tags: [branch]
family:
focus_people: []
---

# Branch Name

## Overview

## Key People

## Family Connections

## Places

## Story So Far

## Open Questions
""",
    "person.md": """---
type: person
status: stub
tags: [person]
person_id:
display_name:
birth_year:
death_year:
---

# Person Name

## Overview

## Names

- Preferred name:
- Other names:

## Family

- Parents:
- Spouses:
- Children:
- Siblings:

## Life

| Date | Place | What happened |
| --- | --- | --- |

## Places

## Story

## Open Questions

## Photos

## Sources
""",
    "relationship.md": """---
type: relationship
status: draft
relationship_type: parent_child
confidence: 0.0
person_a:
person_b:
supporting_claims: []
conflicting_claims: []
tags: [relationship]
---

# Relationship Assertion

## Assertion

Use one of: `proven_parent`, `probable_parent`, `possible_sibling`, `disputed_spouse`, `same_person_candidate`, `name_variant`, `spouse`, `child`, `sibling`, `household_member`.

## Evidence For

## Evidence Against

## Reasoning

## Current Status
""",
    "event.md": """---
type: event
status: draft
event_type:
date:
place:
participants: []
supporting_claims: []
tags: [event]
---

# Event

## What Happened

## Participants

## Place

## Source Evidence

## Chronology Notes
""",
    "family.md": """---
type: family
status: stub
tags: [family]
family_id:
branch:
---

# Family

## Overview

## People

## Family Connections

## Places

## Timeline

| Date | Place | What happened |
| --- | --- | --- |

## Story So Far

## Open Questions
""",
    "source.md": """---
type: source
status: draft
source_reliability: unknown
source_reliability_score: 0.0
source_type:
evidence_type:
informant_proximity:
tags: [source]
---

# Source Title

## Source Identity

- Repository:
- Collection:
- Record type:
- Date:
- Place:
- File:
- Source packet:

## Source Reliability

- Reliability class: original, derivative, authored, index, transcript, abstract, oral-history, unknown.
- Reliability score: 0-10.
- Evidence type: primary, secondary, mixed, unknown.
- Informant proximity: direct participant, witness, official recorder, family informant, later compiler, unknown.
- Bias or limitation:
- Reliability notes:

## Transcription Or Abstract

## Extracted Claims

| Claim | People/Places | Status | Confidence | Claim Page |
| --- | --- | --- | --- | --- |

## Image/Layout Notes

## Citation
""",
    "source-packet.md": """---
type: source_packet
status: draft
source_id:
source_kind:
source_reliability: unknown
source_reliability_score: 0.0
evidence_type:
informant_proximity:
raw_file:
created:
tags: [source-packet]
---

# Source Packet

## Source Identity

## Source Reliability

- Reliability class:
- Reliability score:
- Evidence type:
- Informant proximity:
- Bias or limitation:
- Reliability notes:

## Page And Image Map

## Literal Transcription

What the source literally says. Preserve spelling, line breaks, column labels, marginalia, captions, and uncertainty.

## Translation

Only translated text. Leave blank if the source is already in the working language.

## Interpretation

What the system infers from the source. Keep this separate from the literal transcription.

## Uncertain Or Illegible

## Extracted Atomic Claims

| Claim | Status | Confidence | Claim Page |
| --- | --- | --- | --- |

## Linked Photos Or Images
""",
    "claim.md": """---
type: claim
status: draft
claim_type:
confidence: 0.0
subject:
predicate:
object:
date:
place:
source:
source_packet:
source_reliability:
source_reliability_score:
conversion_confidence:
relationship:
tags: [claim]
---

# Atomic Claim

## Claim

## Status

Use one of: `draft`, `accepted`, `probable`, `possible`, `disputed`, `rejected`.

## Confidence

Use a 0-10 claim-confidence score and explain why. Keep this separate from source reliability and conversion confidence.

## Source Reliability

- Reliability class:
- Reliability score:
- Evidence type:
- Informant proximity:
- Reliability effect on this claim:

## Conversion Confidence

- Reading confidence:
- QA note:
- Page or region reread needed:

## Literal Source Support

## Translation

## Interpretation

## Uncertainty

## Supports

## Conflicts With
""",
    "evidence.md": """---
type: evidence
status: draft
tags: [evidence]
---

# Evidence Claim

## Claim

## Source

## Analysis

## Supports

## Conflicts With

## Confidence
""",
    "identity.md": """---
type: identity
status: open
tags: [identity]
candidates: []
confidence: 0.0
---

# Same Person Candidate

## Candidate Names

## Comparison Matrix

| Feature | Candidate A | Candidate B | Match Strength | Notes |
| --- | --- | --- | --- | --- |
| Name variants | | | | |
| Dates | | | | |
| Places | | | | |
| Relatives | | | | |
| Occupations | | | | |
| Signatures | | | | |
| Migration patterns | | | | |
| Source reliability | | | | |

## Evidence For Same Person

## Evidence Against Same Person

## Working Conclusion
""",
    "photo.md": """---
type: photo
status: draft
tags: [photo]
photo_id:
file:
date_estimate:
place_estimate:
people_confirmed: []
people_suggested: []
face_clusters: []
---

# Photo

## Image

## Front Description

## Back Transcription

## Translation

## Interpretation

## Faces

| Face | Identity Status | Person | Confidence | Notes |
| --- | --- | --- | --- | --- |

## Scene And Object Clues

## Linked Events And Places
""",
    "face-cluster.md": """---
type: face_cluster
status: open
tags: [face-cluster]
cluster_id:
confirmed_identity:
suggested_identities: []
photos: []
---

# Face Cluster

## Cluster Summary

## Confirmed Identity

## Suggested Identities

## Photo Appearances

## Visual Notes

## Evidence Needed
""",
    "task.md": """---
type: research_task
status: open
priority: medium
linked_claim:
linked_relationship:
lineage_goal:
tags: [task]
---

# Research Task

## Task

## Linked Claim Or Relationship

## Proof Needed

## Suggested Search

## Repositories Or Collections

## Date And Place Scope

## Outcome
""",
    "narrative.md": """---
type: narrative
status: draft
tags: [narrative]
subject:
claim_scope: accepted_probable
---

# Narrative

## Scope

- Subject:
- Narrative type: individual biography, family chapter, branch history, migration story, source appendix, or uncertainty note.
- Use only accepted or probable claims plus context directly relevant to this family.

## Draft Narrative

Write the person's or family's story from accepted or probable research-vault claims. Do not write directly from raw sources.

## Timeline

## Photo Captions

## Family-Relevant Historical Context

Include broader history only when it helps explain the subject's choices, constraints, records, migration, occupation, faith, language, community, conflict, illness, or legal status.

## Source Appendix

## Uncertainty Notes
""",
    "context.md": """---
type: context
status: draft
tags: [context]
linked_entity:
---

# Historical Context

## Linked Genealogy Entity

Context is allowed only when linked to a person, relationship, place, event, source, photo, or narrative chapter in this family history.

## Context Summary

## Relevance To This Family

Explain how this context shaped or clarifies the family's lived experience, records, migration, occupation, community, or identity. Do not keep broad background notes that cannot answer that question.

## Sources
""",
    "tree.md": """---
type: tree
status: generated
tags: [tree]
---

# Family Tree View

This file is generated from relationship pages.
""",
    "conflict.md": """---
type: conflict
status: open
conflict_type:
linked_claims: []
linked_relationships: []
tags: [conflict]
---

# Conflict Topic

## Conflict

## Competing Claims

| Claim | Source | Confidence | Notes |
| --- | --- | --- | --- |

## Current Working Conclusion

## Needed Evidence
""",
    "question.md": """---
type: question
status: open
tags: [question]
---

# Research Question

## Question

## Why It Matters

## Known Evidence

## Next Actions

## Resolution
""",
}


WIKI_PRODUCT_FORBIDDEN_PHRASES = (
    "research vault",
    "proof-layer",
    "proof layer",
    "research/_staging",
    "_staging",
    "staged",
    "staging",
    "source-context",
    "source context",
    "proof review",
    "promoted",
    "promotion",
    "canonical graph",
    "relationship assertion",
    "atomic claims",
    "claim extraction",
    "family tree view",
    "status: draft",
)


REQUIRED_DIRECTORIES = [
    ("raw", "sources"),
    ("raw", "converted"),
    ("raw", "chunks"),
    ("raw", "assets"),
    ("raw", "codex-conversion-jobs"),
    ("research",),
    ("research", "sources"),
    ("research", "sources", "transcriptions"),
    ("research", "source-packets"),
    ("research", "claims"),
    ("research", "relationships"),
    ("research", "evidence"),
    ("research", "context"),
    ("research", "events"),
    ("research", "_assets"),
    ("research", "_conversion-review"),
    ("research", "_conversion-review", "triage"),
    ("research", "_conversion-review", "page-queues"),
    ("research", "_conversion-review", "corrections"),
    ("research", "_staging"),
    ("research", "_staging", "photos"),
    ("research", "_indexes"),
    ("research", "_templates"),
    ("research", "_agents"),
    ("research", "questions"),
    ("research", "tasks"),
    ("wiki", "branches"),
    ("wiki", "people"),
    ("wiki", "families"),
    ("wiki", "events"),
    ("wiki", "places"),
    ("wiki", "conflicts"),
    ("wiki", "identity"),
    ("wiki", "photos"),
    ("wiki", "narratives"),
    ("wiki", "context"),
    ("wiki", "timelines"),
    ("wiki", "trees"),
]


@dataclass(frozen=True)
class WikiPaths:
    root: Path

    @property
    def raw(self) -> Path:
        return self.root / "raw"

    @property
    def research(self) -> Path:
        return self.root / "research"

    @property
    def wiki(self) -> Path:
        return self.root / "wiki"

    @property
    def templates(self) -> Path:
        return self.research / "_templates"

    @property
    def staging(self) -> Path:
        return self.research / "_staging"

    @property
    def conversion_review(self) -> Path:
        return self.research / "_conversion-review"

    @property
    def indexes(self) -> Path:
        return self.research / "_indexes"


@dataclass(frozen=True)
class ClaimRecord:
    id: str
    path: str
    status: str
    claim_type: str
    confidence: float | None
    subject: str
    predicate: str
    object: str
    date: str
    place: str
    source: str
    source_packet: str
    relationship: str
    text: str
    supports: list[str]
    conflicts_with: list[str]


@dataclass(frozen=True)
class RelationshipRecord:
    id: str
    path: str
    status: str
    relationship_type: str
    confidence: float | None
    calculated_confidence: float | None
    person_a: str
    person_b: str
    supporting_claims: list[str]
    conflicting_claims: list[str]
    evidence_for: str
    evidence_against: str


@dataclass(frozen=True)
class PreparedSourceResult:
    source: str
    media_type: str
    status: str
    converted_file: str
    chunk_manifest: str
    warnings: list[str]
    conversion_jobs: list[str] = field(default_factory=list)
    converted_files: list[str] = field(default_factory=list)
    chunk_manifests: list[str] = field(default_factory=list)


def init_genealogy_wiki(root: Path, force: bool = False) -> list[Path]:
    paths = WikiPaths(root.resolve())
    created: list[Path] = []

    for parts in REQUIRED_DIRECTORIES:
        directory = paths.root.joinpath(*parts)
        directory.mkdir(parents=True, exist_ok=True)
        created.append(directory)

    write_file(paths.root / "GENEALOGY_WIKI.md", GENEALOGY_SCHEMA, force, created)
    write_file(paths.research / "00 Research Start.md", RESEARCH_START_TEMPLATE, force, created)
    write_file(paths.research / "index.md", RESEARCH_INDEX_TEMPLATE, force, created)
    write_file(paths.research / "log.md", RESEARCH_LOG_TEMPLATE.format(today=date.today().isoformat()), force, created)
    write_file(paths.research / "research-plan.md", RESEARCH_PLAN_TEMPLATE, force, created)
    write_file(paths.wiki / "Family Tree.md", FAMILY_TREE_TEMPLATE, force, created)
    write_file(paths.wiki / "index.md", INDEX_TEMPLATE, force, created)

    for filename, content in TEMPLATES.items():
        write_file(paths.templates / filename, content, force, created)

    return created


def lint_genealogy_wiki(root: Path) -> list[str]:
    paths = WikiPaths(root.resolve())
    issues: list[str] = []

    required = [
        paths.raw,
        paths.raw / "sources",
        paths.raw / "converted",
        paths.raw / "chunks",
        paths.research,
        paths.research / "sources",
        paths.research / "source-packets",
        paths.research / "claims",
        paths.research / "relationships",
        paths.research / "evidence",
        paths.research / "context",
        paths.research / "events",
        paths.research / "index.md",
        paths.research / "log.md",
        paths.research / "research-plan.md",
        paths.research / "questions",
        paths.research / "tasks",
        paths.wiki,
        paths.wiki / "Family Tree.md",
        paths.wiki / "narratives",
        paths.staging,
        paths.indexes,
        paths.templates,
        paths.wiki / "index.md",
        paths.root / "GENEALOGY_WIKI.md",
    ]
    for path in required:
        if not path.exists():
            issues.append(f"missing required path: {path}")

    if not paths.wiki.exists():
        return issues

    issues.extend(lint_wiki_product_language(paths))

    index_text = read_text(paths.wiki / "index.md")
    index_targets = {wikilink_target(link) for link in extract_wikilinks(index_text)}
    for page in paths.wiki.rglob("*.md"):
        if should_skip_wiki_lint_page(page):
            continue
        rel = page.relative_to(paths.wiki).as_posix()
        if rel not in index_text and rel.removesuffix(".md") not in index_targets:
            issues.append(f"page not referenced from index: {rel}")
        text = read_text(page)
        frontmatter = parse_frontmatter(text)
        if "type: person" in text and "[[" not in text:
            issues.append(f"person page has no wiki links: {rel}")
        if frontmatter.get("type") == "source" and "## Extracted Claims" not in text:
            issues.append(f"source page missing extracted claims section: {rel}")
        if frontmatter.get("type") == "claim":
            issues.extend(lint_claim_page(rel, frontmatter, text))
        if frontmatter.get("type") == "relationship":
            issues.extend(lint_relationship_page(rel, frontmatter, text))
        if frontmatter.get("type") == "source_packet":
            issues.extend(lint_source_packet_page(rel, text))
        if frontmatter.get("type") == "conflict":
            issues.extend(lint_conflict_page(rel, frontmatter, text))
        if frontmatter.get("type") == "identity":
            issues.extend(lint_identity_page(rel, text))
        if frontmatter.get("type") == "context" and not frontmatter.get("linked_entity"):
            issues.append(f"context page missing linked_entity: {rel}")
        if frontmatter.get("type") == "research_task" and not (
            frontmatter.get("linked_claim") or frontmatter.get("linked_relationship") or frontmatter.get("lineage_goal")
        ):
            issues.append(f"research task is detached from lineage goal or claim: {rel}")

    issues.extend(lint_research_proof_pages(paths))
    claim_index = build_claim_index(paths.root)
    issues.extend(lint_claim_cross_references(paths.root, claim_index))
    relationship_index = build_relationship_index(paths.root, claim_index)
    issues.extend(lint_relationship_cross_references(paths.root, relationship_index, claim_index))
    issues.extend(lint_chronology(paths))

    return issues


def lint_research_proof_pages(paths: WikiPaths) -> list[str]:
    issues: list[str] = []
    for page in claim_pages(paths):
        text = read_text(page)
        frontmatter = parse_frontmatter(text)
        if frontmatter.get("type") == "claim":
            issues.extend(lint_claim_page(page.relative_to(paths.root).as_posix(), frontmatter, text))
    for page in relationship_pages(paths):
        text = read_text(page)
        frontmatter = parse_frontmatter(text)
        if frontmatter.get("type") == "relationship":
            issues.extend(lint_relationship_page(page.relative_to(paths.root).as_posix(), frontmatter, text))
    for page in sorted((paths.research / "source-packets").glob("*.md")):
        text = read_text(page)
        frontmatter = parse_frontmatter(text)
        if frontmatter.get("type") == "source_packet":
            issues.extend(lint_source_packet_page(page.relative_to(paths.root).as_posix(), text))
    return issues


def should_skip_wiki_lint_page(page: Path) -> bool:
    parts = set(page.parts)
    return (
        page.name in {"index.md"}
        or {"sources", "transcriptions"}.issubset(parts)
    )


def lint_wiki_product_language(paths: WikiPaths) -> list[str]:
    issues: list[str] = []
    for page in sorted(paths.wiki.rglob("*.md")):
        if ".obsidian" in page.parts:
            continue
        rel = page.relative_to(paths.wiki).as_posix()
        lower_text = read_text(page).lower()
        for phrase in WIKI_PRODUCT_FORBIDDEN_PHRASES:
            if phrase in lower_text:
                issues.append(f"wiki product page uses research workflow language '{phrase}': {rel}")
    return issues


def create_claim(
    root: Path,
    claim_id: str,
    claim_text: str,
    claim_type: str,
    subject: str,
    source: str,
    status: str = "draft",
    confidence: float = 0.0,
    predicate: str = "",
    object_value: str = "",
    claim_date: str = "",
    place: str = "",
    source_packet: str = "",
    relationship: str = "",
    force: bool = False,
) -> Path:
    paths = WikiPaths(root.resolve())
    claims_dir = paths.research / "claims"
    claims_dir.mkdir(parents=True, exist_ok=True)
    claim_path = claims_dir / f"{slug(claim_id)}-{slug(claim_text)[:48]}.md"
    if claim_path.exists() and not force:
        raise FileExistsError(claim_path)

    content = TEMPLATES["claim.md"]
    replacements = {
        "status: draft": f"status: {status}",
        "claim_type:": f"claim_type: {claim_type}",
        "confidence: 0.0": f"confidence: {confidence}",
        "subject:": f"subject: {subject}",
        "predicate:": f"predicate: {predicate}",
        "object:": f"object: {object_value}",
        "date:": f"date: {claim_date}",
        "place:": f"place: {place}",
        "source:": f"source: {source}",
        "source_packet:": f"source_packet: {source_packet}",
        "relationship:": f"relationship: {relationship}",
        "# Atomic Claim": f"# {claim_text}",
        "## Claim\n": f"## Claim\n\n{claim_text}\n",
    }
    for old, new in replacements.items():
        content = content.replace(old, new, 1)
    claim_path.write_text(content.strip() + "\n", encoding="utf-8")
    append_index_reference(paths.research / "index.md", "Claims", f"[[claims/{claim_path.stem}]]")
    append_log(paths.research / "log.md", f"claim | Created {claim_path.relative_to(paths.root).as_posix()}")
    return claim_path


def create_relationship(
    root: Path,
    relationship_id: str,
    relationship_type: str,
    person_a: str,
    person_b: str,
    status: str = "draft",
    confidence: float = 0.0,
    supporting_claims: list[str] | None = None,
    conflicting_claims: list[str] | None = None,
    force: bool = False,
) -> Path:
    paths = WikiPaths(root.resolve())
    relationships_dir = paths.research / "relationships"
    relationships_dir.mkdir(parents=True, exist_ok=True)
    relationship_path = relationships_dir / (
        f"{slug(relationship_id)}-{slug(person_a)}-{slug(person_b)}-{slug(relationship_type)}.md"
    )
    if relationship_path.exists() and not force:
        raise FileExistsError(relationship_path)

    supporting_claims = supporting_claims or []
    conflicting_claims = conflicting_claims or []
    content = TEMPLATES["relationship.md"]
    replacements = {
        "status: draft": f"status: {status}",
        "relationship_type: parent_child": f"relationship_type: {relationship_type}",
        "confidence: 0.0": f"confidence: {confidence}",
        "person_a:": f"person_a: {person_a}",
        "person_b:": f"person_b: {person_b}",
        "supporting_claims: []": f"supporting_claims: {format_inline_list(supporting_claims)}",
        "conflicting_claims: []": f"conflicting_claims: {format_inline_list(conflicting_claims)}",
        "# Relationship Assertion": f"# {mermaid_label(person_a)} -> {mermaid_label(person_b)}",
    }
    for old, new in replacements.items():
        content = content.replace(old, new, 1)
    relationship_path.write_text(content.strip() + "\n", encoding="utf-8")
    append_index_reference(paths.research / "index.md", "Relationships", f"[[relationships/{relationship_path.stem}]]")
    append_log(paths.research / "log.md", f"relationship | Created {relationship_path.relative_to(paths.root).as_posix()}")
    return relationship_path


def create_source_packet(
    root: Path,
    source_file: Path,
    packet_id: str,
    title: str,
    source_kind: str,
    force: bool = False,
) -> Path:
    paths = WikiPaths(root.resolve())
    packets_dir = paths.research / "source-packets"
    packets_dir.mkdir(parents=True, exist_ok=True)
    packet_path = packets_dir / f"{slug(packet_id)}-{slug(title)}.md"
    if packet_path.exists() and not force:
        raise FileExistsError(packet_path)

    content = TEMPLATES["source-packet.md"]
    content = content.replace("source_id:", f"source_id: {packet_id}")
    content = content.replace("source_kind:", f"source_kind: {source_kind}")
    content = content.replace("raw_file:", f"raw_file: {source_file.as_posix()}")
    content = content.replace("created:", f"created: {date.today().isoformat()}")
    content = content.replace("# Source Packet", f"# {title}")
    packet_path.write_text(content.strip() + "\n", encoding="utf-8")
    append_index_reference(paths.research / "index.md", "Source Packets", f"[[source-packets/{packet_path.stem}]]")
    append_log(paths.research / "log.md", f"source-packet | Created {packet_path.relative_to(paths.root).as_posix()}")
    return packet_path


def promote_staged_drafts(
    root: Path,
    *,
    force: bool = False,
    dry_run: bool = False,
    include_revise: bool = False,
    include_hold: bool = False,
) -> dict[str, object]:
    """Promote reviewed staging drafts into the canonical research/wiki shelves."""
    paths = WikiPaths(root.resolve())
    summary: dict[str, object] = {
        "dry_run": dry_run,
        "source_packets": [],
        "claims": [],
        "relationships": [],
        "people": [],
        "sources": [],
        "skipped": [],
        "manifest": "",
    }

    staged_packets = sorted((paths.staging / "source-packets").glob("*.md"))
    staged_claims = sorted((paths.staging / "claims").glob("*.md"))
    staged_relationships = sorted((paths.staging / "relationships").glob("*.md"))

    packet_map: dict[str, str] = {}
    packet_records: list[dict[str, object]] = []
    for staged_packet in staged_packets:
        canonical_path = paths.research / "source-packets" / f"{slug(staged_packet.stem)}.md"
        canonical_link = f"[[source-packets/{canonical_path.stem}]]"
        add_staged_reference_mapping(packet_map, paths, staged_packet, canonical_link)
        packet_records.append(
            {
                "staged": staged_packet,
                "canonical_path": canonical_path,
                "canonical_link": canonical_link,
                "text": read_text(staged_packet),
            }
        )

    promoted_claims: list[dict[str, str]] = []
    claim_map: dict[str, str] = {}
    for staged_claim in staged_claims:
        text = read_text(staged_claim)
        frontmatter = parse_frontmatter(text)
        if frontmatter.get("type") != "claim":
            continue
        if not is_stage_eligible_for_promotion(text, frontmatter, include_revise, include_hold):
            summary_list(summary, "skipped").append(
                {
                    "path": staged_claim.relative_to(paths.root).as_posix(),
                    "reason": promotion_recommendation(text, frontmatter) or "no promotion recommendation",
                }
            )
            continue

        canonical_path = paths.research / "claims" / f"{slug(staged_claim.stem)}.md"
        canonical_link = f"[[claims/{canonical_path.stem}]]"
        add_staged_claim_reference_mapping(claim_map, paths, staged_claim, canonical_link)
        subject_name = frontmatter.get("subject", "")
        subject_link = ensure_person_page(paths, subject_name, summary, dry_run=dry_run)
        packet_link = lookup_staged_reference(frontmatter.get("source_packet", ""), packet_map)
        source_link = ensure_source_page(
            paths,
            frontmatter.get("source", ""),
            packet_link,
            summary,
            dry_run=dry_run,
        )
        relationship_link = lookup_staged_reference(frontmatter.get("relationship", ""), {})
        claim_text = update_markdown_frontmatter(
            text,
            {
                "subject": subject_link,
                "source": source_link,
                "source_packet": packet_link,
                "relationship": relationship_link,
            },
        )
        if not dry_run:
            canonical_path.parent.mkdir(parents=True, exist_ok=True)
            if canonical_path.exists() and not force:
                summary_list(summary, "skipped").append(
                    {
                        "path": staged_claim.relative_to(paths.root).as_posix(),
                        "reason": f"canonical claim exists: {canonical_path.relative_to(paths.root).as_posix()}",
                    }
                )
                continue
            canonical_path.write_text(claim_text.strip() + "\n", encoding="utf-8")
            append_index_reference(paths.research / "index.md", "Claims", canonical_link)
            append_source_claim_row(paths, source_link, canonical_link, subject_link, frontmatter, dry_run=False)
        promoted_claims.append(
            {
                "staged_path": staged_claim.relative_to(paths.root).as_posix(),
                "canonical_path": canonical_path.relative_to(paths.root).as_posix(),
                "canonical_link": canonical_link,
                "subject_name": subject_name,
                "subject": subject_link,
                "predicate": frontmatter.get("predicate", ""),
                "object": frontmatter.get("object", ""),
                "claim_type": frontmatter.get("claim_type", ""),
            }
        )
        summary_list(summary, "claims").append(canonical_path.relative_to(paths.root).as_posix())

    for packet_record in packet_records:
        staged_packet = packet_record["staged"]
        canonical_path = packet_record["canonical_path"]
        canonical_link = packet_record["canonical_link"]
        if not isinstance(staged_packet, Path) or not isinstance(canonical_path, Path) or not isinstance(canonical_link, str):
            continue
        packet_text = str(packet_record.get("text", ""))
        packet_text = replace_promoted_references(packet_text, claim_map)
        packet_text = replace_promoted_references(packet_text, packet_map)
        packet_text = update_markdown_frontmatter(packet_text, {"status": "promoted"})
        if not dry_run:
            canonical_path.parent.mkdir(parents=True, exist_ok=True)
            if canonical_path.exists() and not force:
                summary_list(summary, "skipped").append(
                    {
                        "path": staged_packet.relative_to(paths.root).as_posix(),
                        "reason": f"canonical source packet exists: {canonical_path.relative_to(paths.root).as_posix()}",
                    }
                )
                continue
            canonical_path.write_text(packet_text.strip() + "\n", encoding="utf-8")
            append_index_reference(paths.research / "index.md", "Source Packets", canonical_link)
        summary_list(summary, "source_packets").append(canonical_path.relative_to(paths.root).as_posix())

    relationship_map: dict[str, str] = {}
    for staged_relationship in staged_relationships:
        text = read_text(staged_relationship)
        frontmatter = parse_frontmatter(text)
        if not is_stage_eligible_for_promotion(text, frontmatter, include_revise, include_hold):
            summary_list(summary, "skipped").append(
                {
                    "path": staged_relationship.relative_to(paths.root).as_posix(),
                    "reason": promotion_recommendation(text, frontmatter) or "no promotion recommendation",
                }
            )
            continue
        promoted = promote_staged_relationship(
            paths,
            staged_relationship,
            text,
            frontmatter,
            promoted_claims,
            packet_map,
            relationship_map,
            summary,
            force=force,
            dry_run=dry_run,
        )
        summary_list(summary, "relationships").extend(promoted)

    if not dry_run:
        write_claim_index(paths.root)
        write_relationship_index(paths.root)
        write_relationship_graph(paths.root)
        generate_tree(paths.root)
        append_log(
            paths.research / "log.md",
            "promote-staged | Promoted "
            f"{len(summary_list(summary, 'source_packets'))} source packet(s), "
            f"{len(summary_list(summary, 'claims'))} claim(s), "
            f"{len(summary_list(summary, 'relationships'))} relationship(s)",
        )
        manifest_path = write_promotion_manifest(paths, summary)
        summary["manifest"] = manifest_path.relative_to(paths.root).as_posix()

    return summary


def summary_list(summary: dict[str, object], key: str) -> list:
    value = summary.setdefault(key, [])
    if not isinstance(value, list):
        raise TypeError(f"promotion summary field is not a list: {key}")
    return value


def promotion_recommendation(text: str, frontmatter: dict[str, str]) -> str:
    value = normalize_promotion_value(frontmatter.get("promotion_recommendation", ""))
    if value:
        return value
    section = extract_section(text, "Promotion Recommendation").lower()
    if not section:
        return ""
    if "reject" in section or "do not promote" in section:
        return "reject"
    if "hold" in section:
        return "hold"
    if "revise" in section or "revision" in section:
        return "revise"
    if "promote" in section:
        return "promote"
    return ""


def normalize_promotion_value(value: str) -> str:
    normalized = value.strip().lower().replace("-", "_").replace(" ", "_")
    if normalized in {"promote", "approved", "ready", "ready_to_promote"}:
        return "promote"
    if normalized in {"revise", "needs_revision", "needs_review", "review"}:
        return "revise"
    if normalized in {"hold", "blocked", "defer"}:
        return "hold"
    if normalized in {"reject", "rejected", "do_not_promote"}:
        return "reject"
    return normalized


def is_stage_eligible_for_promotion(
    text: str,
    frontmatter: dict[str, str],
    include_revise: bool,
    include_hold: bool,
) -> bool:
    recommendation = promotion_recommendation(text, frontmatter)
    if recommendation == "promote":
        return True
    if recommendation == "revise":
        return include_revise
    if recommendation in {"hold", "reject"}:
        return include_hold
    return False


def add_staged_reference_mapping(mapping: dict[str, str], paths: WikiPaths, staged_path: Path, canonical_link: str) -> None:
    rel = staged_path.relative_to(paths.root).as_posix()
    rel_no_ext = rel.removesuffix(".md")
    variants = {
        rel,
        rel_no_ext,
        staged_path.as_posix(),
        staged_path.with_suffix("").as_posix(),
        staged_path.name,
        staged_path.stem,
        f"[[{rel_no_ext}]]",
    }
    for variant in variants:
        mapping[normalize_reference_key(variant)] = canonical_link


def add_staged_claim_reference_mapping(mapping: dict[str, str], paths: WikiPaths, staged_path: Path, canonical_link: str) -> None:
    add_staged_reference_mapping(mapping, paths, staged_path, canonical_link)
    mapping[normalize_reference_key(f"[[claims/{staged_path.stem}]]")] = canonical_link
    mapping[normalize_reference_key(f"claims/{staged_path.stem}")] = canonical_link


def normalize_reference_key(value: str) -> str:
    value = value.strip().strip("`").replace("\\", "/")
    if looks_like_wikilink(value):
        value = wikilink_target(value)
    return value.removesuffix(".md")


def lookup_staged_reference(value: str, mapping: dict[str, str]) -> str:
    if not value:
        return ""
    key = normalize_reference_key(value)
    candidates = [key, Path(key).name, Path(key).stem]
    for candidate in candidates:
        if candidate in mapping:
            return mapping[candidate]
    if looks_like_wikilink(value):
        target = wikilink_target(value)
        if target.startswith(("source-packets/", "relationships/", "claims/")):
            return value
    return ""


def replace_promoted_references(text: str, mapping: dict[str, str]) -> str:
    for old, new in sorted(mapping.items(), key=lambda item: len(item[0]), reverse=True):
        if not old:
            continue
        text = text.replace(f"[[{old}]]", new)
        text = text.replace(old, new)
    return text


def update_markdown_frontmatter(
    text: str,
    updates: dict[str, str],
    remove: set[str] | None = None,
) -> str:
    remove = remove or set()
    match = re.match(r"---\s*\n(.*?)\n---\s*\n?", text, flags=re.DOTALL)
    body = text
    lines: list[str] = []
    if match:
        lines = match.group(1).splitlines()
        body = text[match.end() :]
    seen: set[str] = set()
    output: list[str] = []
    for line in lines:
        if ":" not in line:
            output.append(line)
            continue
        key = line.split(":", 1)[0].strip()
        if key in remove:
            seen.add(key)
            continue
        if key in updates:
            output.append(f"{key}: {clean_frontmatter_value(updates[key])}")
            seen.add(key)
        else:
            output.append(line)
    for key, value in updates.items():
        if key not in seen and key not in remove:
            output.append(f"{key}: {clean_frontmatter_value(value)}")
    return "---\n" + "\n".join(output).rstrip() + "\n---\n\n" + body.lstrip("\n")


def clean_frontmatter_value(value: str) -> str:
    return str(value).replace("\n", " ").strip()


def ensure_person_page(
    paths: WikiPaths,
    value: str,
    summary: dict[str, object],
    *,
    dry_run: bool,
) -> str:
    clean = clean_person_name(value)
    existing = find_existing_person_page(paths, clean)
    if existing:
        return f"[[people/{existing.stem}]]"
    if looks_like_wikilink(value):
        target = wikilink_target(value)
        if target.startswith("people/"):
            stem = target.split("/", 1)[1]
            clean = clean or stem.replace("-", " ")
        else:
            stem = slug(clean or target)
    else:
        stem = slug(clean)
    page_path = paths.wiki / "people" / f"{stem}.md"
    link = f"[[people/{page_path.stem}]]"
    if page_path.exists():
        return link
    summary_list(summary, "people").append(page_path.relative_to(paths.root).as_posix())
    if dry_run:
        return link
    page_path.parent.mkdir(parents=True, exist_ok=True)
    title = clean or stem.replace("-", " ").title()
    content = TEMPLATES["person.md"]
    replacements = {
        "person_id:": f"person_id: {page_path.stem}",
        "display_name:": f"display_name: {title}",
        "# Person Name": f"# {title}",
        "- Preferred name:": f"- Preferred name: {title}",
        "## Open Questions\n": "## Open Questions\n\n## See Also\n\n- [[Family Tree]]\n",
    }
    for old, new in replacements.items():
        content = content.replace(old, new, 1)
    page_path.write_text(content.strip() + "\n", encoding="utf-8")
    append_index_reference(paths.wiki / "index.md", "People", link)
    return link


def clean_person_name(value: str) -> str:
    value = value.strip()
    if looks_like_wikilink(value):
        value = wikilink_target(value)
    value = value.replace("people/", "").replace("_", " ")
    value = Path(value).stem if "/" in value or "\\" in value else value
    return value.replace("-", " ").strip()


def find_existing_person_page(paths: WikiPaths, name: str) -> Path | None:
    if not name:
        return None
    target_slug = slug(name)
    for page in sorted((paths.wiki / "people").glob("*.md")):
        text = read_text(page)
        frontmatter = parse_frontmatter(text)
        candidates = [page.stem, frontmatter.get("display_name", ""), extract_markdown_title(text)]
        if any(candidate and slug(candidate) == target_slug for candidate in candidates):
            return page
    return None


def extract_markdown_title(text: str) -> str:
    match = re.search(r"^#\s+(.+)$", text, flags=re.MULTILINE)
    return match.group(1).strip() if match else ""


def ensure_source_page(
    paths: WikiPaths,
    source_ref: str,
    packet_link: str,
    summary: dict[str, object],
    *,
    dry_run: bool,
) -> str:
    clean_ref = normalize_source_reference(source_ref)
    if looks_like_wikilink(source_ref):
        target = wikilink_target(source_ref)
        if target.startswith("sources/") and wiki_target_exists(paths.research, target):
            return source_ref
    existing = find_existing_source_page(paths, clean_ref)
    if existing:
        link = f"[[sources/{existing.stem}]]"
        if packet_link and not dry_run:
            append_markdown_section_entry(existing, "Source Identity", f"- Promoted source packet: {packet_link}")
        return link
    stem_source = clean_ref or packet_link or "promoted-source"
    digest = hashlib.sha1(stem_source.encode("utf-8")).hexdigest()[:12]
    source_stem = f"src-{digest}-{slug(Path(stem_source).stem)[:60]}"
    page_path = paths.research / "sources" / f"{source_stem}.md"
    link = f"[[sources/{page_path.stem}]]"
    summary_list(summary, "sources").append(page_path.relative_to(paths.root).as_posix())
    if dry_run:
        return link
    title = Path(clean_ref).stem.replace("-", " ").title() if clean_ref else page_path.stem
    page_path.parent.mkdir(parents=True, exist_ok=True)
    page_path.write_text(
        "\n".join(
            [
                "---",
                "type: source",
                "status: draft",
                "source_reliability: unknown",
                "source_reliability_score: 0.0",
                "source_type: promoted_staging_reference",
                "evidence_type:",
                "informant_proximity:",
                "tags: [source, promoted]",
                f"raw_file: {clean_frontmatter_value(clean_ref)}",
                f"source_packet: {packet_link}",
                "---",
                "",
                f"# {title}",
                "",
                "## Source Identity",
                "",
                f"- File: `{clean_ref}`" if clean_ref else "- File:",
                f"- Source packet: {packet_link}" if packet_link else "- Source packet:",
                "",
                "## Source Reliability",
                "",
                "- Reliability class: unknown.",
                "- Reliability score: 0-10.",
                "- Evidence type: unknown.",
                "- Informant proximity: unknown.",
                "- Bias or limitation:",
                "- Reliability notes:",
                "",
                "## Transcription Or Abstract",
                "",
                "See linked source packet and converted source artifacts.",
                "",
                "## Extracted Claims",
                "",
                "| Claim | People/Places | Status | Confidence | Claim Page |",
                "| --- | --- | --- | --- | --- |",
                "",
                "## Image/Layout Notes",
                "",
                "## Citation",
                "",
                "Citation not finalized.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    append_index_reference(paths.research / "index.md", "Sources", link)
    return link


def normalize_source_reference(value: str) -> str:
    value = value.strip().strip("`").replace("\\", "/")
    if looks_like_wikilink(value):
        value = wikilink_target(value)
    return value.removesuffix(".md") + (".md" if value.endswith(".md") else "")


def find_existing_source_page(paths: WikiPaths, source_ref: str) -> Path | None:
    if not source_ref:
        return None
    normalized = source_ref.replace("\\", "/")
    for page in sorted((paths.research / "sources").glob("*.md")):
        text = read_text(page)
        frontmatter = parse_frontmatter(text)
        haystack = text.replace("\\", "/")
        if normalized in haystack:
            return page
        for key in ["raw_file", "converted_file", "source_file"]:
            value = frontmatter.get(key, "").replace("\\", "/")
            if value and (value == normalized or Path(value).name == Path(normalized).name):
                return page
    return None


def append_markdown_section_entry(path: Path, heading: str, entry: str) -> bool:
    text = read_text(path)
    if entry in text:
        return False
    heading_text = f"## {heading}"
    if heading_text not in text:
        text = text.rstrip() + f"\n\n{heading_text}\n\n{entry}\n"
        path.write_text(text, encoding="utf-8")
        return True
    heading_start = text.index(heading_text)
    body_start = heading_start + len(heading_text)
    next_heading = re.search(r"\n## ", text[body_start:])
    insert_at = body_start + next_heading.start() if next_heading else len(text)
    before = text[:insert_at].rstrip()
    after = text[insert_at:].lstrip("\n")
    text = f"{before}\n{entry}\n\n{after}" if after else f"{before}\n{entry}\n"
    path.write_text(text, encoding="utf-8")
    return True


def append_person_section_entry(
    paths: WikiPaths,
    person_link: str,
    heading: str,
    entry: str,
    *,
    dry_run: bool,
) -> None:
    if dry_run or not looks_like_wikilink(person_link):
        return
    target = wikilink_target(person_link)
    if not target.startswith("people/"):
        return
    page_path = paths.wiki / f"{target}.md"
    if page_path.exists():
        append_markdown_section_entry(page_path, heading, entry)


def append_source_claim_row(
    paths: WikiPaths,
    source_link: str,
    claim_link: str,
    subject_link: str,
    frontmatter: dict[str, str],
    *,
    dry_run: bool,
) -> None:
    if dry_run or not looks_like_wikilink(source_link):
        return
    target = wikilink_target(source_link)
    if not target.startswith("sources/"):
        return
    page_path = paths.research / f"{target}.md"
    if not page_path.exists():
        return
    status = frontmatter.get("status", "")
    confidence = frontmatter.get("confidence", "")
    row = f"| {claim_link} | {subject_link} | {status} | {confidence} | {claim_link} |"
    append_markdown_section_entry(page_path, "Extracted Claims", row)


def promote_staged_relationship(
    paths: WikiPaths,
    staged_relationship: Path,
    text: str,
    frontmatter: dict[str, str],
    promoted_claims: list[dict[str, str]],
    packet_map: dict[str, str],
    relationship_map: dict[str, str],
    summary: dict[str, object],
    *,
    force: bool,
    dry_run: bool,
) -> list[str]:
    if frontmatter.get("type") == "relationship":
        person_a = ensure_person_page(paths, frontmatter.get("person_a", ""), summary, dry_run=dry_run)
        person_b = ensure_person_page(paths, frontmatter.get("person_b", ""), summary, dry_run=dry_run)
        relationship_type = frontmatter.get("relationship_type", "possible_parent")
        canonical_path = paths.research / "relationships" / f"{slug(staged_relationship.stem)}.md"
        relationship_link = f"[[relationships/{canonical_path.stem}]]"
        add_staged_reference_mapping(relationship_map, paths, staged_relationship, relationship_link)
        relationship_text = update_markdown_frontmatter(
            text,
            {
                "type": "relationship",
                "person_a": person_a,
                "person_b": person_b,
                "relationship_type": relationship_type,
            },
        )
        return write_promoted_relationship_page(
            paths,
            canonical_path,
            relationship_link,
            relationship_text,
            [person_a, person_b],
            staged_relationship,
            summary,
            force=force,
            dry_run=dry_run,
        )

    if frontmatter.get("type") != "relationship_candidate":
        return []
    relationship_type = frontmatter.get("relationship_type", "")
    if relationship_type not in {"recorded_parent_child", "parent_child", "probable_parent", "possible_parent"}:
        summary_list(summary, "skipped").append(
            {
                "path": staged_relationship.relative_to(paths.root).as_posix(),
                "reason": f"unsupported relationship candidate type: {relationship_type}",
            }
        )
        return []
    child = frontmatter.get("child", "")
    parents = parse_listish(frontmatter.get("parents", ""))
    child_link = ensure_person_page(paths, child, summary, dry_run=dry_run)
    confidence = frontmatter.get("confidence", "0.0")
    canonical_relationship_type = "probable_parent" if float_or_zero(confidence) >= 8.0 else "possible_parent"
    written: list[str] = []
    for parent in parents:
        parent_link = ensure_person_page(paths, parent, summary, dry_run=dry_run)
        supporting_claims = matching_parentage_claims(promoted_claims, child, parent)
        relationship_stem = slug(f"{staged_relationship.stem}-{parent}-parent")
        canonical_path = paths.research / "relationships" / f"{relationship_stem}.md"
        relationship_link = f"[[relationships/{canonical_path.stem}]]"
        add_staged_reference_mapping(relationship_map, paths, staged_relationship, relationship_link)
        relationship_text = render_promoted_parent_relationship(
            parent_link=parent_link,
            child_link=child_link,
            relationship_type=canonical_relationship_type,
            status=frontmatter.get("status", "draft"),
            confidence=confidence,
            supporting_claims=supporting_claims,
            staged_path=staged_relationship.relative_to(paths.root).as_posix(),
            source_packet=lookup_staged_reference(frontmatter.get("source_packet", ""), packet_map),
            source_text=extract_section(text, "Literal Support"),
            interpretation=extract_section(text, "Interpretation"),
            uncertainty=extract_section(text, "Uncertainty"),
        )
        written.extend(
            write_promoted_relationship_page(
                paths,
                canonical_path,
                relationship_link,
                relationship_text,
                [parent_link, child_link],
                staged_relationship,
                summary,
                force=force,
                dry_run=dry_run,
            )
        )
    return written


def matching_parentage_claims(promoted_claims: list[dict[str, str]], child: str, parent: str) -> list[str]:
    child_slug = slug(clean_person_name(child))
    parent_slug = slug(clean_person_name(parent))
    matches: list[str] = []
    for claim in promoted_claims:
        if claim.get("claim_type") != "parentage":
            continue
        if slug(clean_person_name(claim.get("subject_name", ""))) != child_slug:
            continue
        if slug(clean_person_name(claim.get("object", ""))) != parent_slug:
            continue
        matches.append(claim["canonical_link"])
    return matches


def render_promoted_parent_relationship(
    *,
    parent_link: str,
    child_link: str,
    relationship_type: str,
    status: str,
    confidence: str,
    supporting_claims: list[str],
    staged_path: str,
    source_packet: str,
    source_text: str,
    interpretation: str,
    uncertainty: str,
) -> str:
    claim_list = format_inline_list(supporting_claims)
    evidence_lines = [f"- Promoted from staged relationship candidate `{staged_path}`."]
    if source_packet:
        evidence_lines.append(f"- Source packet: {source_packet}.")
    if supporting_claims:
        evidence_lines.append(f"- Supporting claims: {', '.join(supporting_claims)}.")
    if source_text:
        evidence_lines.append(f"- Literal support: {source_text}")
    return "\n".join(
        [
            "---",
            "type: relationship",
            f"status: {status or 'draft'}",
            f"relationship_type: {relationship_type}",
            f"confidence: {confidence or '0.0'}",
            f"person_a: {parent_link}",
            f"person_b: {child_link}",
            f"supporting_claims: {claim_list}",
            "conflicting_claims: []",
            "tags: [relationship, promoted]",
            "---",
            "",
            f"# {mermaid_label(parent_link)} -> {mermaid_label(child_link)}",
            "",
            "## Assertion",
            "",
            f"{parent_link} is represented as a {relationship_type} of {child_link}.",
            "",
            "## Evidence For",
            "",
            *evidence_lines,
            "",
            "## Evidence Against",
            "",
            "No conflicting claims were identified in the promoted staged draft.",
            "",
            "## Reasoning",
            "",
            interpretation or "Promoted from reviewed staged evidence.",
            "",
            "## Current Status",
            "",
            uncertainty or "No additional uncertainty was recorded in the staged draft.",
        ]
    )


def write_promoted_relationship_page(
    paths: WikiPaths,
    canonical_path: Path,
    relationship_link: str,
    relationship_text: str,
    person_links: list[str],
    staged_relationship: Path,
    summary: dict[str, object],
    *,
    force: bool,
    dry_run: bool,
) -> list[str]:
    rel_path = canonical_path.relative_to(paths.root).as_posix()
    if dry_run:
        return [rel_path]
    canonical_path.parent.mkdir(parents=True, exist_ok=True)
    if canonical_path.exists() and not force:
        summary_list(summary, "skipped").append(
            {
                "path": staged_relationship.relative_to(paths.root).as_posix(),
                "reason": f"canonical relationship exists: {rel_path}",
            }
        )
        return []
    canonical_path.write_text(relationship_text.strip() + "\n", encoding="utf-8")
    append_index_reference(paths.research / "index.md", "Relationships", relationship_link)
    return [rel_path]


def write_promotion_manifest(paths: WikiPaths, summary: dict[str, object]) -> Path:
    promotions_dir = paths.staging / "promotions"
    promotions_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = promotions_dir / f"{date.today().isoformat()}-{datetime.now().strftime('%H%M%S')}-promote-staged.json"
    manifest_summary = dict(summary)
    manifest_summary["manifest"] = manifest_path.relative_to(paths.root).as_posix()
    manifest = {
        "generated": datetime.now().isoformat(timespec="seconds"),
        "summary": manifest_summary,
    }
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return manifest_path


def create_material_packet(
    root: Path,
    source_file: Path,
    packet_id: str,
    title: str,
    source_kind: str = "unknown",
    features: list[str] | None = None,
    copy_source: bool = True,
    force: bool = False,
) -> Path:
    paths = WikiPaths(root.resolve())
    packets_dir = paths.research / "source-packets"
    packets_dir.mkdir(parents=True, exist_ok=True)
    packet_path = packets_dir / f"{slug(packet_id)}-{slug(title)}.md"
    if packet_path.exists() and not force:
        raise FileExistsError(packet_path)

    staged_source = (
        stage_source_material(paths.root, source_file, packet_id, title, force=force)
        if copy_source
        else source_file.resolve()
    )
    if not staged_source.exists():
        raise FileNotFoundError(staged_source)
    source_page = write_material_source_page(paths.root, staged_source, packet_id, title, source_kind, force=force)
    width, height = image_dimensions(staged_source)
    media_type = detect_media_type(staged_source)
    content = build_material_packet_content(
        root=paths.root,
        source_file=staged_source,
        source_page=source_page,
        packet_id=packet_id,
        title=title,
        source_kind=source_kind,
        media_type=media_type,
        features=features or [],
        width=width,
        height=height,
    )
    packet_path.write_text(content.strip() + "\n", encoding="utf-8")
    append_index_reference(paths.research / "index.md", "Sources", f"[[sources/{source_page.stem}]]")
    append_index_reference(paths.research / "index.md", "Source Packets", f"[[source-packets/{packet_path.stem}]]")
    append_log(paths.research / "log.md", f"material-packet | Created {packet_path.relative_to(paths.root).as_posix()}")
    return packet_path


def stage_source_material(root: Path, source_file: Path, packet_id: str, title: str, force: bool = False) -> Path:
    source_file = source_file.resolve()
    if not source_file.exists():
        raise FileNotFoundError(source_file)

    destination_dir = root / "raw" / "sources" / f"{slug(packet_id)}-{slug(title)}"
    destination_dir.mkdir(parents=True, exist_ok=True)
    destination = destination_dir / source_file.name
    if destination.exists() and not force:
        raise FileExistsError(destination)
    if source_file != destination.resolve():
        shutil.copy2(source_file, destination)
    return destination


def write_material_source_page(
    root: Path,
    source_file: Path,
    packet_id: str,
    title: str,
    source_kind: str,
    force: bool = False,
) -> Path:
    paths = WikiPaths(root.resolve())
    source_dir = paths.research / "sources"
    source_dir.mkdir(parents=True, exist_ok=True)
    source_page = source_dir / f"{slug(packet_id)}-{slug(title)}.md"
    if source_page.exists() and not force:
        raise FileExistsError(source_page)

    packet_link = f"[[source-packets/{slug(packet_id)}-{slug(title)}]]"
    raw_path = relative_to_root(source_file, root)
    content = f"""---
type: source
source_id: {packet_id}
source_kind: {source_kind}
raw_file: {raw_path}
source_packet: {packet_link}
status: draft
---

# {title}

## Source Identity

- Repository:
- Collection:
- Record type: {source_kind}
- Date:
- Place:
- File: {raw_path}
- Source packet: {packet_link}
- Reliability:

## Transcription Or Abstract

See {packet_link}.

## Extracted Claims

| Claim | People/Places | Status | Confidence | Claim Page |
| --- | --- | --- | --- | --- |

## Image/Layout Notes

## Citation
"""
    source_page.write_text(content.strip() + "\n", encoding="utf-8")
    return source_page


def build_material_packet_content(
    root: Path,
    source_file: Path,
    source_page: Path,
    packet_id: str,
    title: str,
    source_kind: str,
    media_type: str,
    features: list[str],
    width: int | None,
    height: int | None,
) -> str:
    paths = WikiPaths(root.resolve())
    raw_path = relative_to_root(source_file, root)
    source_link = f"[[sources/{source_page.stem}]]"
    packet_dir = paths.research / "source-packets"
    media_link = relative_path(packet_dir, source_file)
    preview = f"![Source image]({media_link})" if media_type == "image" else f"[Source file]({media_link})"
    feature_lines = "\n".join(f"- {feature}" for feature in features) if features else "- To be profiled dynamically."
    dimensions = f"{width} x {height} px" if width and height else "unknown or not image-based"

    return f"""---
type: source_packet
status: draft
source_id: {packet_id}
source_kind: {source_kind}
media_type: {media_type}
raw_file: {raw_path}
source_page: {source_link}
created: {date.today().isoformat()}
tags: [source-packet, dynamic-source]
---

# {title}

## Source Identity

- Source page: {source_link}
- Source kind: {source_kind}
- Media type: {media_type}
- Raw file: {raw_path}
- Dimensions: {dimensions}
- Processing stance: document-agnostic dynamic layout analysis

## Source Media

{preview}

## Verbatim Extraction Contract

- Do not summarize, shorten, modernize, or paraphrase printed headers, handwritten labels, captions, marginalia, stamps, seals, page numbers, or notes.
- If a table is too wide for readable Markdown, transcribe the full printed header text in the header inventory first, then use stable short field keys in split tables.
- Preserve blank cells as blank, mark uncertain readings with `[?]`, mark unreadable text as `[illegible]`, and record all uncertainty below.
- Expand ditto marks only when the repeated value is clear; otherwise transcribe the mark literally and explain the uncertainty.
- Every extracted claim must point back to a literal source location, not only to an interpreted table row.

## Dynamic Material Profile

Observed or expected features. Add only what is visible in this source; do not force a preset schema.

{feature_lines}

## Printed Header And Label Inventory

Transcribe every visible printed header, field label, caption, note label, page number label, and column label literally before shortening anything for tables.

| Label ID | Region ID | Exact text | Short key | Applies to | Notes |
| --- | --- | --- | --- | --- | --- |

## Layout Inventory

Describe each visual or textual region before transcription. Use bounding boxes when available.

| Region ID | Region type | Bounding box | Reading order | Description | Confidence |
| --- | --- | --- | --- | --- | --- |

## Reading Order

List the order in which the source should be read by a human or LLM. Include headers, marginalia, captions, tables, seals, stamps, page numbers, and image regions.

## Literal Transcription

What the source literally says. Preserve spelling, line breaks, column labels, marginalia, captions, page numbers, handwriting, punctuation, and uncertainty markers.

## Structured Transcription Tables

Use as many tables as needed to keep the source readable. Short column names are allowed only when mapped to exact labels in `Printed Header And Label Inventory`.

## Translation

Only translated text. Leave blank if the source is already in the working language.

## Interpretation

What the system infers from the source. Keep this separate from the literal transcription and translation.

## Uncertain Or Illegible

Track every unreadable, ambiguous, cropped, overwritten, or low-confidence mark.

| Location | Literal mark | Possible readings | Reason uncertain | Review priority |
| --- | --- | --- | --- | --- |

## Extracted Entities

| Entity | Entity type | Literal form | Normalized form | Source location | Confidence |
| --- | --- | --- | --- | --- | --- |

## Extracted Atomic Claims

| Claim | Status | Confidence | Source location | Claim Page |
| --- | --- | --- | --- | --- |

## Relationship Evidence Candidates

| People | Relationship candidate | Evidence location | Status | Confidence | Relationship Page |
| --- | --- | --- | --- | --- | --- |

## Conflict Candidates

| Conflict type | Evidence in this source | Evidence to compare | Conflict Page |
| --- | --- | --- | --- |

## Research Tasks Suggested

| Task | Linked claim or relationship | Proof needed | Suggested search | Priority |
| --- | --- | --- | --- | --- |

## Linked Photos Or Images

| Region ID | Description | Linked people/events/places | Caption or back text | Confidence |
| --- | --- | --- | --- | --- |

## Completeness Audit

Check this packet against the source image or media after transcription.

| Audit item | Expected from source | Present in packet | Missing, shortened, or uncertain items | Reviewer |
| --- | --- | --- | --- | --- |
| Page/source metadata | | | | |
| Printed headers and labels | | | | |
| Body rows or entries | | | | |
| Blank rows, crossed-out areas, or end notes | | | | |
| Captions, marginalia, stamps, seals, and page numbers | | | | |

## Recommended Model Review Passes

1. Layout pass: identify regions, reading order, page metadata, and all printed labels.
2. Header pass: transcribe exact headers and labels without shortening.
3. Body pass: transcribe entries, tables, handwriting, captions, and notes.
4. Audit pass: compare the packet against the source and list omissions or suspected truncation.

## Processing Notes

- This packet is intentionally source-type agnostic.
- Add document-specific fields only when the source itself requires them.
- Keep transcription, translation, interpretation, and uncertainty separate.
"""


def detect_media_type(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in {".jpg", ".jpeg", ".png", ".tif", ".tiff", ".bmp", ".gif", ".webp"}:
        return "image"
    if suffix == ".pdf":
        return "pdf"
    if suffix in {".mp3", ".wav", ".m4a", ".aac", ".flac", ".ogg"}:
        return "audio"
    if suffix in {".mp4", ".mov", ".avi", ".mkv", ".webm"}:
        return "video"
    if suffix in {".doc", ".docx", ".rtf", ".odt"}:
        return "document"
    if suffix in {".txt", ".md", ".csv", ".tsv", ".json", ".xml", ".html", ".htm"}:
        return "text"
    return "binary"


def image_dimensions(path: Path) -> tuple[int | None, int | None]:
    if detect_media_type(path) != "image":
        return None, None
    try:
        from PIL import Image
    except ImportError:
        return None, None

    try:
        with Image.open(path) as image:
            return image.width, image.height
    except OSError:
        return None, None


def create_codex_conversion_job(
    root: Path,
    source_file: Path,
    job_id: str,
    title: str,
    page_range: str | None = None,
    image_scale: float = 2.0,
    force: bool = False,
) -> Path:
    paths = WikiPaths(root.resolve())
    original_source = source_file.resolve()
    if not original_source.exists():
        raise FileNotFoundError(original_source)
    if image_scale <= 0:
        raise ValueError("image_scale must be greater than zero")

    job_slug = f"{slug(job_id)}-{slug(title)}"
    job_dir = paths.raw / "codex-conversion-jobs" / job_slug
    if job_dir.exists() and force:
        shutil.rmtree(job_dir)
    if job_dir.exists() and not force:
        raise FileExistsError(job_dir)
    source_dir = job_dir / "source"
    pages_dir = job_dir / "page-images"
    work_dir = job_dir / "work-orders"
    output_dir = job_dir / "page-markdown"
    extracted_images_dir = job_dir / "extracted-images"
    for directory in (source_dir, pages_dir, work_dir, output_dir, extracted_images_dir):
        directory.mkdir(parents=True, exist_ok=True)

    source_sha256 = file_sha256(original_source)
    staged_source = source_dir / staged_source_filename(original_source, source_sha256)
    if original_source != staged_source.resolve():
        shutil.copy2(original_source, staged_source)

    media_type = detect_media_type(staged_source)
    page_specs = render_codex_job_pages(staged_source, pages_dir, media_type, page_range, image_scale)
    manifest_source = original_source
    try:
        manifest_source.relative_to(paths.root)
    except ValueError:
        manifest_source = staged_source
    manifest = {
        "job_id": job_id,
        "title": title,
        "source_file": relative_to_root(manifest_source, paths.root),
        "local_staged_source_file": relative_to_root(staged_source, paths.root),
        "source_sha256": source_sha256,
        "source_bytes": staged_source.stat().st_size,
        "media_type": media_type,
        "created": date.today().isoformat(),
        "conversion_engine": "codex-thread-vision",
        "status": "prepared",
        "chunking": {
            "unit": "page",
            "max_pages_per_work_order": 1,
            "page_range": page_range or "all",
            "rationale": "Use one page per work order so massive sources can be converted, reviewed, and retried incrementally.",
        },
        "extracted_images_dir": relative_to_root(extracted_images_dir, paths.root),
        "instructions": [
            "Convert each page from the rendered page image using Codex vision in this workspace.",
            "Write one Markdown file per page under page-markdown/.",
            "Crop each meaningful photograph, illustration, seal, signature, chart, map, or other non-text visual region into extracted-images/ and reference it inline in the page Markdown.",
            "Keep transcription, translation, interpretation, uncertainty, and image/caption notes separate.",
            "Do not modernize spelling or silently repair source errors.",
        ],
        "pages": [],
    }
    for spec in page_specs:
        page_no = spec["page"]
        output_path = output_dir / f"page-{page_no:04d}.md"
        work_order_path = work_dir / f"page-{page_no:04d}.md"
        page_image_path = Path(str(spec["image_path"]))
        page_image_output_dir = extracted_images_dir / f"page-{page_no:04d}"
        page_image_output_dir.mkdir(parents=True, exist_ok=True)
        spec["image_sha256"] = file_sha256(page_image_path)
        spec["image_path"] = relative_to_root(page_image_path, paths.root)
        spec["image_output_dir"] = relative_to_root(page_image_output_dir, paths.root)
        spec["output_path"] = relative_to_root(output_path, paths.root)
        spec["work_order_path"] = relative_to_root(work_order_path, paths.root)
        spec["status"] = "todo"
        work_order_path.write_text(
            build_codex_page_work_order(paths.root, job_id, title, spec, output_path),
            encoding="utf-8",
        )
        manifest["pages"].append(spec)

    manifest_path = job_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    (job_dir / "README.md").write_text(build_codex_job_readme(paths.root, manifest_path, manifest), encoding="utf-8")
    append_log(paths.research / "log.md", f"codex-conversion-job | Prepared {manifest_path.relative_to(paths.root).as_posix()}")
    return manifest_path


def render_codex_job_pages(
    source_file: Path,
    pages_dir: Path,
    media_type: str,
    page_range: str | None,
    image_scale: float,
) -> list[dict[str, object]]:
    if media_type == "pdf":
        try:
            import fitz
        except ImportError as exc:
            raise RuntimeError("PyMuPDF is required to prepare PDF conversion jobs.") from exc

        doc = fitz.open(source_file)
        selected_pages = parse_page_range(page_range, len(doc))
        specs: list[dict[str, object]] = []
        for page_no in selected_pages:
            page = doc[page_no - 1]
            pix = page.get_pixmap(matrix=fitz.Matrix(image_scale, image_scale), alpha=False)
            image_path = pages_dir / f"page-{page_no:04d}.jpg"
            pix.save(image_path, jpg_quality=90)
            specs.append(
                {
                    "page": page_no,
                    "source_page": page_no,
                    "image_path": image_path.as_posix(),
                    "width_px": pix.width,
                    "height_px": pix.height,
                    "image_bytes": image_path.stat().st_size,
                }
            )
        return specs

    if media_type == "image":
        image_path = pages_dir / f"page-0001{source_file.suffix.lower()}"
        shutil.copy2(source_file, image_path)
        width, height = image_dimensions(image_path)
        return [
            {
                "page": 1,
                "source_page": 1,
                "image_path": image_path.as_posix(),
                "width_px": width,
                "height_px": height,
                "image_bytes": image_path.stat().st_size,
            }
        ]

    copied_path = pages_dir / source_file.name
    shutil.copy2(source_file, copied_path)
    return [
        {
            "page": 1,
            "source_page": 1,
            "image_path": copied_path.as_posix(),
            "width_px": None,
            "height_px": None,
            "image_bytes": copied_path.stat().st_size,
            "note": "Non-image source staged as a single work item.",
        }
    ]


def ensure_source_prep_page_image(root: Path, batch: dict[str, object]) -> Path | None:
    paths = WikiPaths(root.resolve())
    page = first_source_prep_batch_page(batch)
    rel_page_image = str(page.get("page_image", "")).strip()
    if not rel_page_image:
        return None
    page_image = paths.root / rel_page_image
    if page_image.exists():
        return page_image

    manifest_rel = str(batch.get("job_manifest") or page.get("job_manifest") or "").strip()
    if not manifest_rel:
        return None
    manifest_path = paths.root / manifest_rel
    if not manifest_path.exists():
        return None

    manifest = read_json_payload(manifest_path, {})
    page_number = safe_int(page.get("page") or batch.get("first_page"), 1)
    page_spec = find_manifest_page_spec(manifest, page_number)
    source_page = safe_int(page_spec.get("source_page") or page.get("source_page") or page_number, page_number)
    source_file = find_existing_source_file_for_job(paths.root, manifest)
    if source_file is None:
        return None

    media_type = str(manifest.get("media_type") or detect_media_type(source_file))
    page_image.parent.mkdir(parents=True, exist_ok=True)
    if media_type == "pdf":
        try:
            import fitz
        except ImportError as exc:
            raise RuntimeError("PyMuPDF is required to regenerate PDF page images.") from exc

        doc = fitz.open(source_file)
        try:
            if source_page < 1 or source_page > len(doc):
                return None
            pix = doc[source_page - 1].get_pixmap(matrix=fitz.Matrix(2.0, 2.0), alpha=False)
            if page_image.suffix.lower() in {".jpg", ".jpeg"}:
                pix.save(page_image, jpg_quality=90)
            else:
                pix.save(page_image)
            page_spec["width_px"] = pix.width
            page_spec["height_px"] = pix.height
        finally:
            doc.close()
    else:
        if source_file.resolve() != page_image.resolve():
            shutil.copy2(source_file, page_image)
        width, height = image_dimensions(page_image)
        page_spec["width_px"] = width
        page_spec["height_px"] = height

    if page_image.exists():
        page_spec["image_path"] = relative_to_root(page_image, paths.root)
        page_spec["image_bytes"] = page_image.stat().st_size
        page_spec["image_sha256"] = file_sha256(page_image)
        manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
        return page_image
    return None


def safe_int(value: object, default: int) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def find_manifest_page_spec(manifest: dict[str, object], page_number: int) -> dict[str, object]:
    pages = manifest.get("pages", [])
    if isinstance(pages, list):
        for page in pages:
            if isinstance(page, dict) and safe_int(page.get("page"), -1) == page_number:
                return page
    page_spec: dict[str, object] = {"page": page_number, "source_page": page_number}
    if isinstance(pages, list):
        pages.append(page_spec)
    else:
        manifest["pages"] = [page_spec]
    return page_spec


def find_existing_source_file_for_job(root: Path, manifest: dict[str, object]) -> Path | None:
    for key in ("source_file", "local_staged_source_file"):
        value = str(manifest.get(key) or "").strip()
        if not value:
            continue
        path = Path(value)
        candidate = path if path.is_absolute() else root / path
        if candidate.exists():
            return candidate
    return None


def parse_page_range(page_range: str | None, page_count: int) -> list[int]:
    if page_count < 1:
        return []
    if not page_range:
        return list(range(1, page_count + 1))
    selected: set[int] = set()
    for part in page_range.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start_text, end_text = part.split("-", 1)
            start = int(start_text)
            end = int(end_text)
            if start > end:
                raise ValueError(f"invalid descending page range: {part}")
            selected.update(range(start, end + 1))
        else:
            selected.add(int(part))
    invalid = [page for page in selected if page < 1 or page > page_count]
    if invalid:
        raise ValueError(f"page range includes pages outside 1-{page_count}: {invalid}")
    return sorted(selected)


def build_codex_page_work_order(root: Path, job_id: str, title: str, page: dict[str, object], output_path: Path) -> str:
    image_abs = (root / str(page["image_path"])).resolve()
    image_output_abs = (root / str(page["image_output_dir"])).resolve()
    return f"""# Codex Conversion Work Order

- Job: {job_id}
- Title: {title}
- Page: {page["page"]}
- Source image: `{image_abs}`
- Extracted image output folder: `{image_output_abs}`
- Output file: `{output_path.resolve()}`
- Status: todo

## Instructions For Codex

View the source image and convert the page to Markdown without intentional truncation.

Preserve:

- page numbers and visible page labels
- titles, headers, mastheads, column order, captions, marginalia, stamps, signatures, and image positions
- literal spelling, punctuation, line breaks where genealogically meaningful, and uncertain readings
- separation between literal transcription, visual notes, uncertainty, and completeness notes
- no translation, interpretation, summary, or genealogy claim extraction

Extract images:

- Crop only substantial visuals likely to be useful as standalone wiki assets: portraits, headshots, group photographs, labeled photographs, substantial maps, large illustrations, or source-meaningful diagrams/charts.
- Do not crop marginal numbers, checkmarks, filing marks, short handwritten notes, ordinary stamps, seals, signatures, decorative rules, page labels, or tiny marks unless the visual itself is unusually important and cannot be captured by transcription.
- Transcribe or describe minor marks in the Markdown instead of cropping them.
- Name crops `page-{int(page["page"]):04d}-image-01.png`, `page-{int(page["page"]):04d}-image-02.png`, and so on.
- Insert each crop inline in the Markdown near its source position using descriptive alt text and the visible caption when present.
- If a visible image cannot be cropped confidently, add an uncertainty note with its approximate location and reason.

Use this page-level structure:

```markdown
# Page {page["page"]}

## Page Metadata

## Layout And Reading Order

## Literal Transcription

## Images, Captions, And Visual Notes

Inline extracted images here, placed in reading order, with captions and crop uncertainty.

## Uncertain Or Illegible

## Completeness Audit
```
"""


def build_codex_job_readme(root: Path, manifest_path: Path, manifest: dict[str, object]) -> str:
    next_page = next((page for page in manifest["pages"] if page["status"] == "todo"), None)
    next_line = ""
    if next_page:
        next_line = f"\nNext page work order: `{next_page['work_order_path']}`\n"
    return f"""# Codex Conversion Job

Title: {manifest["title"]}

Manifest: `{relative_to_root(manifest_path, root)}`
Source: `{manifest["source_file"]}`
Pages: {len(manifest["pages"])}
{next_line}
This job is designed for conversion by Codex in the workspace. Page images are disposable render cache regenerated from the raw source when needed, and each completed page Markdown file can be assembled into a full converted document.
"""


def next_codex_conversion_work_order(root: Path, manifest_path: Path) -> Path | None:
    paths = WikiPaths(root.resolve())
    manifest_path = manifest_path if manifest_path.is_absolute() else paths.root / manifest_path
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for page in manifest.get("pages", []):
        output_path = paths.root / page["output_path"]
        if page.get("status") == "done" or output_path.exists():
            continue
        return paths.root / page["work_order_path"]
    return None


def assemble_codex_conversion_job(root: Path, manifest_path: Path, out: Path | None = None) -> Path:
    paths = WikiPaths(root.resolve())
    manifest_path = manifest_path if manifest_path.is_absolute() else paths.root / manifest_path
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    job_dir = manifest_path.parent
    output_path = out or (paths.raw / "converted" / f"{job_dir.name}.codex.md")
    if not output_path.is_absolute():
        output_path = paths.root / output_path

    missing: list[str] = []
    parts = [
        f"# {manifest['title']}",
        "",
        "## Conversion Metadata",
        "",
        f"- Source: `{manifest['source_file']}`",
        f"- Source SHA-256: `{manifest.get('source_sha256', '')}`",
        f"- Manifest: `{relative_to_root(manifest_path, paths.root)}`",
        "- Conversion method: Codex local vision workbench",
        f"- Extracted images: `{manifest.get('extracted_images_dir', '')}`",
        "",
    ]
    for page in manifest.get("pages", []):
        page_output = paths.root / page["output_path"]
        if not page_output.exists():
            missing.append(page["output_path"])
            continue
        parts.append(page_output.read_text(encoding="utf-8").strip())
        parts.append("")

    if missing:
        missing_list = "\n".join(f"- {item}" for item in missing)
        parts.extend(["## Missing Pages", "", missing_list, ""])
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")
    append_log(paths.research / "log.md", f"codex-conversion-job | Assembled {output_path.relative_to(paths.root).as_posix()}")
    return output_path


def prepare_raw_sources(
    root: Path,
    force: bool = False,
    page_range: str | None = None,
    image_scale: float = 2.0,
    pages_per_job: int = 50,
    new_pages_limit: int = 0,
    max_chars: int = 12000,
) -> list[PreparedSourceResult]:
    """Create or advance Codex-agent conversion jobs for every raw source.

    This is the simplified primary path: drop files into raw/sources, run one
    command, and let the source-prep agent queue page-scoped Codex conversion
    jobs. OCR and PDF text layers are only possible signals inside the page
    conversion workflow; they are not treated as the converter.
    """
    paths = WikiPaths(root.resolve())
    raw_sources = paths.raw / "sources"
    results: list[PreparedSourceResult] = []

    for source in sorted(raw_sources.rglob("*")):
        if not source.is_file() or source.name == ".gitkeep":
            continue
        results.append(
            prepare_raw_source_for_agent_conversion(
                paths.root,
                source,
                force=force,
                page_range=page_range,
                image_scale=image_scale,
                pages_per_job=pages_per_job,
                new_pages_limit=new_pages_limit,
                max_chars=max_chars,
            )
        )

    write_source_prep_index(paths.root)
    if results:
        append_log(paths.research / "log.md", f"prepare-sources | Prepared {len(results)} raw source(s)")
    return results


def prepare_raw_source_for_agent_conversion(
    root: Path,
    source: Path,
    force: bool = False,
    page_range: str | None = None,
    image_scale: float = 2.0,
    pages_per_job: int = 50,
    new_pages_limit: int = 0,
    max_chars: int = 12000,
) -> PreparedSourceResult:
    paths = WikiPaths(root.resolve())
    source = source.resolve()
    digest = file_sha256(source)
    media_type = detect_media_type(source)
    warnings: list[str] = []

    jobs = source_prep_jobs_by_hash(paths.root).get(digest, [])
    if jobs and not force and media_type != "pdf":
        job_manifests = [paths.root / str(job["manifest"]) for job in jobs]
    elif jobs and not force and media_type == "pdf":
        job_manifests = [paths.root / str(job["manifest"]) for job in jobs]
        page_count = pdf_page_count(source)
        existing_pages = existing_pdf_job_pages(jobs, page_count)
        selected_pages = [page for page in parse_page_range(page_range, page_count) if page not in existing_pages]
        if new_pages_limit > 0:
            selected_pages = selected_pages[:new_pages_limit]
        if selected_pages:
            job_manifests.extend(
                create_agent_conversion_jobs_for_pdf_pages(
                    paths.root,
                    source,
                    digest=digest,
                    pages=selected_pages,
                    image_scale=image_scale,
                    pages_per_job=pages_per_job,
                    force=force,
                )
            )
    else:
        job_manifests = create_agent_conversion_jobs_for_source(
            paths.root,
            source,
            digest=digest,
            page_range=page_range,
            image_scale=image_scale,
            pages_per_job=pages_per_job,
            new_pages_limit=new_pages_limit,
            force=force,
        )

    job_statuses: list[str] = []
    converted_files: list[str] = []
    chunk_manifests: list[str] = []
    for job_manifest in job_manifests:
        job_statuses.append(advance_agent_conversion_job(paths.root, job_manifest))
        converted_file = converted_path_for_job(paths.root, {"manifest": relative_to_root(job_manifest, paths.root)})
        if converted_file.exists():
            converted_files.append(relative_to_root(converted_file, paths.root))
            chunk_manifest_path = chunk_converted_markdown(paths.root, converted_file, max_chars=max_chars)
            chunk_manifests.append(relative_to_root(chunk_manifest_path, paths.root))

    status = summarize_prepared_source_status(job_statuses, converted_files)
    converted_file = converted_files[0] if converted_files else ""
    chunk_manifest = chunk_manifests[0] if chunk_manifests else ""

    return PreparedSourceResult(
        source=relative_to_root(source, paths.root),
        media_type=media_type,
        status=status,
        converted_file=converted_file,
        chunk_manifest=chunk_manifest,
        warnings=warnings,
        conversion_jobs=[relative_to_root(job_manifest, paths.root) for job_manifest in job_manifests],
        converted_files=converted_files,
        chunk_manifests=chunk_manifests,
    )


def create_agent_conversion_jobs_for_source(
    root: Path,
    source: Path,
    digest: str,
    page_range: str | None,
    image_scale: float,
    pages_per_job: int,
    new_pages_limit: int,
    force: bool,
) -> list[Path]:
    media_type = detect_media_type(source)
    if media_type != "pdf":
        return [
            create_codex_conversion_job(
                root,
                source,
                job_id=agent_conversion_job_id(source, digest),
                title=source.stem,
                page_range=page_range,
                image_scale=image_scale,
                force=force,
            )
        ]

    page_count = pdf_page_count(source)
    selected_pages = parse_page_range(page_range, page_count)
    if new_pages_limit > 0:
        selected_pages = selected_pages[:new_pages_limit]
    return create_agent_conversion_jobs_for_pdf_pages(
        root,
        source,
        digest=digest,
        pages=selected_pages,
        image_scale=image_scale,
        pages_per_job=pages_per_job,
        force=force,
    )


def existing_pdf_job_pages(jobs: list[dict[str, str]], page_count: int) -> set[int]:
    pages: set[int] = set()
    for job in jobs:
        page_range = str(job.get("page_range", "")).strip()
        if not page_range or page_range == "all":
            pages.update(range(1, page_count + 1))
            continue
        try:
            pages.update(parse_page_range(page_range, page_count))
        except (TypeError, ValueError):
            continue
    return pages


def create_agent_conversion_jobs_for_pdf_pages(
    root: Path,
    source: Path,
    *,
    digest: str,
    pages: list[int],
    image_scale: float,
    pages_per_job: int,
    force: bool,
) -> list[Path]:
    page_groups = group_pages_for_agent_jobs(pages, pages_per_job)
    manifests: list[Path] = []
    for group in page_groups:
        group_range = format_page_range(group)
        job_id = f"{agent_conversion_job_id(source, digest)}-p{group[0]:04d}-{group[-1]:04d}"
        title = f"{source.stem} pages {group_range}"
        manifests.append(
            create_codex_conversion_job(
                root,
                source,
                job_id=job_id,
                title=title,
                page_range=group_range,
                image_scale=image_scale,
                force=force,
            )
        )
    return manifests


def advance_agent_conversion_job(root: Path, manifest_path: Path) -> str:
    if next_codex_conversion_work_order(root, manifest_path) is not None:
        return "queued_for_agent_conversion"
    output_path = assemble_codex_conversion_job(root, manifest_path)
    return "assembled" if output_path.exists() else "queued_for_agent_conversion"


def agent_conversion_job_id(source: Path, digest: str) -> str:
    return f"CA{digest[:8]}-{slug(source.stem)[:24] or 'source'}"


def summarize_prepared_source_status(job_statuses: list[str], converted_files: list[str]) -> str:
    if not job_statuses:
        return "no_sources"
    if all(status == "assembled" for status in job_statuses):
        return "assembled"
    if converted_files:
        return "partially_converted"
    return "queued_for_agent_conversion"


def group_pages_for_agent_jobs(pages: list[int], pages_per_job: int) -> list[list[int]]:
    if pages_per_job < 1:
        raise ValueError("pages_per_job must be at least 1")
    return [pages[index : index + pages_per_job] for index in range(0, len(pages), pages_per_job)]


def format_page_range(pages: list[int]) -> str:
    if not pages:
        return ""
    ranges: list[str] = []
    start = previous = pages[0]
    for page in pages[1:]:
        if page == previous + 1:
            previous = page
            continue
        ranges.append(f"{start}-{previous}" if start != previous else str(start))
        start = previous = page
    ranges.append(f"{start}-{previous}" if start != previous else str(start))
    return ",".join(ranges)


def pdf_page_count(source: Path) -> int:
    try:
        import fitz
    except ImportError as exc:
        raise RuntimeError("PyMuPDF is required to batch PDF conversion jobs.") from exc

    with fitz.open(source) as doc:
        return len(doc)


def write_source_prep_index(root: Path, output: Path | None = None) -> Path:
    paths = WikiPaths(root.resolve())
    output_path = output or (paths.raw / "source-prep-manifest.json")
    if not output_path.is_absolute():
        output_path = paths.root / output_path

    jobs_by_hash = source_prep_jobs_by_hash(paths.root)
    conversions_by_hash = source_prep_conversions_by_hash(paths.root)
    cloud_sources_by_path = raw_cloud_sources_by_path(paths.root)
    sources = []
    local_raw_paths: set[str] = set()
    for source in sorted((paths.raw / "sources").rglob("*")):
        if not source.is_file() or source.name == ".gitkeep":
            continue
        digest = file_sha256(source)
        jobs = jobs_by_hash.get(digest, [])
        conversions = conversions_by_hash.get(digest, [])
        raw_path = relative_to_root(source, paths.root)
        local_raw_paths.add(raw_path)
        entry = {
            "id": f"SRC-{digest[:12]}",
            "title": source.stem,
            "raw_path": raw_path,
            "media_type": detect_media_type(source),
            "bytes": source.stat().st_size,
            "sha256": digest,
            "status": source_prep_status(jobs, conversions),
            "conversion_jobs": jobs,
            "converted_sources": conversions,
        }
        cloud_entry = cloud_sources_by_path.get(raw_path)
        if cloud_entry:
            entry["cloud"] = {
                "provider": "cloudflare-r2",
                "key": cloud_entry.get("key", ""),
                "sha256": cloud_entry.get("sha256", ""),
                "bytes": cloud_entry.get("bytes", 0),
                "media_type": cloud_entry.get("media_type", ""),
            }
        sources.append(entry)

    for raw_path, cloud_entry in sorted(cloud_sources_by_path.items()):
        if raw_path in local_raw_paths:
            continue
        sources.append(build_cloud_only_source_prep_entry(raw_path, cloud_entry, jobs_by_hash, conversions_by_hash))

    manifest = {
        "created": date.today().isoformat(),
        "source_root": "raw/sources",
        "purpose": "Inventory raw source files before document-preparation conversion.",
        "pipeline_stage": "source-prep",
        "sources": sources,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    return output_path


def raw_cloud_sources_by_path(root: Path) -> dict[str, dict[str, object]]:
    sources_by_path: dict[str, dict[str, object]] = {}
    try:
        cloud_config = load_raw_cloud_config(root, require_credentials=False)
        cloud_manifest = build_raw_cloud_manifest(root, cloud_config)
        sources_by_path.update(raw_cloud_manifest_files_by_path(cloud_manifest))
    except Exception:
        pass
    sources_by_path.update(raw_cloud_manifest_files_by_path(read_tracked_raw_cloud_manifest(root)))
    return sources_by_path


def read_tracked_raw_cloud_manifest(root: Path) -> dict[str, object]:
    path = root.resolve() / "raw" / "r2-raw-sources.json"
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return payload if isinstance(payload, dict) else {}


def raw_cloud_manifest_files_by_path(manifest: dict[str, object]) -> dict[str, dict[str, object]]:
    files = manifest.get("files", []) if isinstance(manifest, dict) else []
    if not isinstance(files, list):
        return {}
    return {
        str(item.get("path", "")).strip(): item
        for item in files
        if isinstance(item, dict) and str(item.get("path", "")).strip()
    }


def build_cloud_only_source_prep_entry(
    raw_path: str,
    cloud_entry: dict[str, object],
    jobs_by_hash: dict[str, list[dict[str, str]]],
    conversions_by_hash: dict[str, list[dict[str, str]]],
) -> dict[str, object]:
    digest = str(cloud_entry.get("sha256", "")).strip()
    identity_digest = digest or hashlib.sha256(
        f"{raw_path}|{cloud_entry.get('key', '')}".encode("utf-8")
    ).hexdigest()
    jobs = jobs_by_hash.get(digest, []) if digest else []
    conversions = conversions_by_hash.get(digest, []) if digest else []
    return {
        "id": f"SRC-{identity_digest[:12]}",
        "title": Path(raw_path).stem,
        "raw_path": raw_path,
        "media_type": detect_media_type(Path(raw_path)),
        "bytes": safe_int(cloud_entry.get("bytes"), 0),
        "sha256": digest,
        "status": source_prep_status(jobs, conversions) if (jobs or conversions) else "cloud_registered",
        "local_cache": "missing",
        "conversion_jobs": jobs,
        "converted_sources": conversions,
        "cloud": {
            "provider": "cloudflare-r2",
            "key": cloud_entry.get("key", ""),
            "sha256": digest,
            "bytes": safe_int(cloud_entry.get("bytes"), 0),
            "media_type": cloud_entry.get("media_type", ""),
        },
    }


def chunk_converted_markdown(
    root: Path,
    converted_file: Path,
    output_dir: Path | None = None,
    max_chars: int = 12000,
) -> Path:
    if max_chars < 1000:
        raise ValueError("max_chars must be at least 1000")

    paths = WikiPaths(root.resolve())
    converted_file = converted_file if converted_file.is_absolute() else paths.root / converted_file
    converted_file = converted_file.resolve()
    if not converted_file.exists():
        raise FileNotFoundError(converted_file)

    chunk_dir = output_dir or (paths.raw / "chunks" / slug(converted_file.stem))
    if not chunk_dir.is_absolute():
        chunk_dir = paths.root / chunk_dir
    chunk_dir.mkdir(parents=True, exist_ok=True)
    for old_chunk in chunk_dir.glob("page-*-chunk-*.md"):
        if old_chunk.is_file():
            old_chunk.unlink()

    text = converted_file.read_text(encoding="utf-8")
    converted_hash = file_sha256(converted_file)
    source_path, source_hash, source_manifest = parse_conversion_metadata(text)
    chunks = []
    chunk_number = 1

    for page_number, page_text in split_page_markdown(text):
        for part_number, chunk_text in enumerate(split_chunk_text(page_text, max_chars), start=1):
            chunk_id = f"CHUNK-{converted_hash[:12]}-P{page_number:04d}-{part_number:02d}"
            chunk_path = chunk_dir / f"page-{page_number:04d}-chunk-{part_number:02d}.md"
            content = build_chunk_markdown(
                chunk_id=chunk_id,
                converted_file=relative_to_root(converted_file, paths.root),
                converted_hash=converted_hash,
                source_path=source_path,
                source_hash=source_hash,
                source_manifest=source_manifest,
                page_number=page_number,
                part_number=part_number,
                chunk_text=chunk_text,
            )
            chunk_path.write_text(content, encoding="utf-8")
            chunks.append(
                {
                    "chunk_id": chunk_id,
                    "chunk_number": chunk_number,
                    "path": relative_to_root(chunk_path, paths.root),
                    "page_start": page_number,
                    "page_end": page_number,
                    "part": part_number,
                    "chars": len(chunk_text),
                    "sha256": file_sha256(chunk_path),
                }
            )
            chunk_number += 1

    manifest = {
        "created": date.today().isoformat(),
        "converted_file": relative_to_root(converted_file, paths.root),
        "converted_sha256": converted_hash,
        "source": source_path,
        "source_sha256": source_hash,
        "source_manifest": source_manifest,
        "chunking": {
            "unit": "page",
            "max_chars": max_chars,
            "overflow": "split within page by Markdown sections and paragraph boundaries",
        },
        "chunks": chunks,
    }
    manifest_path = chunk_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    append_log(paths.research / "log.md", f"prep-chunk | Wrote {manifest_path.relative_to(paths.root).as_posix()}")
    return manifest_path


def write_post_conversion_qc(root: Path, output_dir: Path | None = None) -> list[Path]:
    """Write page-level conversion QC artifacts without editing conversions.

    This is the post-conversion loop: find pages that are obviously poor,
    family-relevant, or suspicious compared with known wiki names, then queue
    only those exact pages/regions for careful reread.
    """
    paths = WikiPaths(root.resolve())
    review_dir = output_dir or paths.conversion_review
    if not review_dir.is_absolute():
        review_dir = paths.root / review_dir
    triage_dir = review_dir / "triage"
    queue_dir = review_dir / "page-queues"
    correction_dir = review_dir / "corrections"
    for directory in (triage_dir, queue_dir, correction_dir):
        directory.mkdir(parents=True, exist_ok=True)

    family_terms = build_family_context_terms(paths.root)
    index_entries = []
    page_index_entries = []
    written: list[Path] = []
    for manifest_path in sorted((paths.raw / "chunks").glob("*/manifest.json")):
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        converted_file = paths.root / str(manifest.get("converted_file", ""))
        if not converted_file.exists():
            continue
        page_reviews = analyze_converted_source_pages(paths.root, converted_file, manifest_path, family_terms)
        source_slug = slug(converted_file.stem)
        for review in page_reviews:
            page_index_entries.append(
                {
                    "converted_file": relative_to_root(converted_file, paths.root),
                    "chunk_manifest": relative_to_root(manifest_path, paths.root),
                    "source_manifest": str(manifest.get("source_manifest", "")),
                    "page": review["page"],
                    "recommended_action": review["recommended_action"],
                    "conversion_confidence": review["conversion_confidence"],
                    "family_relevance": review["family_relevance"],
                    "quality_flags": review["quality_flags"],
                    "matched_terms": review["matched_terms"],
                    "suspicious_readings": review["suspicious_readings"],
                }
            )

        triage_path = triage_dir / f"{source_slug}.md"
        triage_path.write_text(
            build_conversion_qc_triage_markdown(paths.root, converted_file, manifest_path, page_reviews),
            encoding="utf-8",
        )
        written.append(triage_path)

        queued_pages = [review for review in page_reviews if review["recommended_action"] != "pass"]
        queue_path = queue_dir / f"{source_slug}.md"
        queue_path.write_text(
            build_conversion_qc_page_queue_markdown(paths.root, converted_file, manifest_path, queued_pages),
            encoding="utf-8",
        )
        written.append(queue_path)

        corrections = [
            correction
            for review in page_reviews
            for correction in review.get("suspicious_readings", [])
            if isinstance(correction, dict)
        ]
        correction_path = correction_dir / f"{source_slug}.md"
        correction_path.write_text(
            build_conversion_qc_corrections_markdown(paths.root, converted_file, manifest_path, corrections),
            encoding="utf-8",
        )
        written.append(correction_path)

        index_entries.append(
            {
                "converted_file": relative_to_root(converted_file, paths.root),
                "chunk_manifest": relative_to_root(manifest_path, paths.root),
                "page_count": len(page_reviews),
                "queued_pages": len(queued_pages),
                "suspected_corrections": len(corrections),
                "triage": relative_to_root(triage_path, paths.root),
                "page_queue": relative_to_root(queue_path, paths.root),
                "corrections": relative_to_root(correction_path, paths.root),
            }
        )

    index_path = review_dir / "qc-index.json"
    index_path.write_text(
        json.dumps(
            {
                "created": date.today().isoformat(),
                "purpose": "Page-level post-conversion quality control queue.",
                "family_context_terms": sorted(family_terms.values()),
                "sources": index_entries,
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    written.append(index_path)
    page_index_path = review_dir / "qc-pages.json"
    page_index_path.write_text(
        json.dumps(
            {
                "created": date.today().isoformat(),
                "purpose": "Page-level QC decisions used to block unsafe extraction.",
                "pages": page_index_entries,
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    written.append(page_index_path)
    append_log(paths.research / "log.md", f"conversion-qc | Wrote {len(written)} QC artifact(s)")
    return written


def analyze_converted_source_pages(
    root: Path,
    converted_file: Path,
    chunk_manifest: Path,
    family_terms: dict[str, str],
) -> list[dict[str, object]]:
    text = converted_file.read_text(encoding="utf-8")
    reviews = []
    for page_number, page_text in split_page_markdown(text):
        reviews.append(analyze_conversion_page(root, converted_file, chunk_manifest, page_number, page_text, family_terms))
    return reviews


def analyze_conversion_page(
    root: Path,
    converted_file: Path,
    chunk_manifest: Path,
    page_number: int,
    page_text: str,
    family_terms: dict[str, str],
) -> dict[str, object]:
    status, base_flags = assess_conversion_page_quality(page_text)
    flags = list(dict.fromkeys(base_flags + detect_conversion_text_flags(page_text)))
    matched_terms = find_family_context_matches(page_text, family_terms)
    suspicious_readings = find_suspicious_name_readings(page_text, family_terms)
    family_relevance = conversion_family_relevance(matched_terms, suspicious_readings)
    recommended_action = conversion_recommended_action(flags, family_relevance, suspicious_readings)
    confidence = conversion_confidence(flags, suspicious_readings)
    return {
        "converted_file": relative_to_root(converted_file, root),
        "chunk_manifest": relative_to_root(chunk_manifest, root),
        "page": page_number,
        "status": status,
        "quality_flags": flags,
        "family_relevance": family_relevance,
        "matched_terms": matched_terms,
        "suspicious_readings": suspicious_readings,
        "conversion_confidence": confidence,
        "recommended_action": recommended_action,
    }


def detect_conversion_text_flags(page_text: str) -> list[str]:
    flags: list[str] = []
    lower_text = page_text.lower()
    text_outside_fences = strip_fenced_code_blocks(page_text)
    alpha_words = re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ]{2,}", page_text)
    if "## literal transcription" not in lower_text:
        flags.append("missing_literal_transcription_section")
    missing_sections = [
        section for section in SOURCE_PREP_REQUIRED_PAGE_SECTIONS if f"## {section.lower()}" not in lower_text
    ]
    if missing_sections:
        flags.append("missing_conversion_contract_sections")
    if len(alpha_words) < 15 and ("![source page]" in lower_text or "page image" in lower_text):
        flags.append("image_only_or_too_little_text")
    if len(alpha_words) < 8 and "[no automated transcription" in lower_text:
        flags.append("no_transcription")
    if page_text.count("[illegible]") + page_text.count("[?]") >= 5:
        flags.append("many_uncertain_readings")
    reread_text = re.sub(r"(?m)^-\s*technical reread clues:\s*none\s*$", "", lower_text)
    if re.search(r"\b(second review|reread|re-read|before being treated as final)\b", reread_text):
        flags.append("explicit_reread_needed")
    if re.search(r"\b[a-zA-Z]{25,}\b", page_text):
        flags.append("possible_ocr_garbage_token")
    if "\t" in text_outside_fences or re.search(r"\S\s{8,}\S", text_outside_fences):
        flags.append("possible_table_layout_loss")
    return flags


def strip_fenced_code_blocks(text: str) -> str:
    return re.sub(r"(?ms)^```.*?^```", "", text)


def build_family_context_terms(root: Path) -> dict[str, str]:
    terms: dict[str, str] = {}
    wiki = root / "wiki"
    research = root / "research"
    candidates = []
    for directory in (
        wiki / "people",
        wiki / "families",
        wiki / "relationships",
        wiki / "claims",
        wiki / "identity",
        wiki / "conflicts",
        wiki / "narratives",
        research / "source-packets",
    ):
        if directory.exists():
            candidates.extend(sorted(directory.rglob("*.md")))
    for path in candidates:
        add_family_terms_from_text(path.stem.replace("-", " "), terms)
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        for heading in re.findall(r"^#\s+(.+)$", text, flags=re.MULTILINE):
            add_family_terms_from_text(heading, terms)
        for link in extract_wikilinks(text):
            add_family_terms_from_text(link.replace("/", " ").replace("-", " "), terms)
    return terms


FAMILY_CONTEXT_STOPWORDS = {
    "claim",
    "claims",
    "source",
    "sources",
    "packet",
    "family",
    "families",
    "person",
    "relationship",
    "possible",
    "probable",
    "accepted",
    "draft",
    "event",
    "place",
    "unknown",
    "page",
    "record",
}


SUSPICIOUS_NAME_READING_STOPWORDS = FAMILY_CONTEXT_STOPWORDS | {
    "acta",
    "acts",
    "archivo",
    "boletin",
    "boletín",
    "card",
    "context",
    "daily",
    "diario",
    "diarios",
    "document",
    "documentation",
    "evidence",
    "gazette",
    "index",
    "journal",
    "official",
    "oficial",
    "photo",
    "photograph",
    "photographs",
    "photos",
    "portrait",
    "press",
    "prensa",
    "reference",
    "register",
    "registro",
    "revista",
    "session",
    "sessions",
    "sesion",
    "sesión",
    "sesiones",
    "tourist",
    "travel",
}


SUSPICIOUS_NAME_CONTEXT_CUES = {
    "apellido",
    "apellidos",
    "delegate",
    "delegada",
    "delegado",
    "doctor",
    "daughter",
    "father",
    "hija",
    "hijo",
    "husband",
    "madre",
    "mother",
    "name",
    "named",
    "names",
    "nombre",
    "nombres",
    "nombrada",
    "nombrado",
    "padre",
    "senor",
    "señor",
    "senora",
    "señora",
    "spouse",
    "wife",
}


def add_family_terms_from_text(text: str, terms: dict[str, str]) -> None:
    words = [word for word in re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ]{4,}", text) if word.lower() not in FAMILY_CONTEXT_STOPWORDS]
    for word in words:
        key = word.lower()
        if key not in terms or (terms[key].islower() and not word.islower()):
            terms[key] = word
    if 1 < len(words) <= 5:
        phrase = " ".join(words)
        terms.setdefault(phrase.lower(), phrase)


def find_family_context_matches(page_text: str, family_terms: dict[str, str]) -> list[str]:
    lower_text = page_text.lower()
    matches = []
    for key, label in family_terms.items():
        if " " in key:
            if key in lower_text:
                matches.append(label)
            continue
        if re.search(rf"\b{re.escape(key)}\b", lower_text):
            matches.append(label)
    return sorted(set(matches))


def find_suspicious_name_readings(page_text: str, family_terms: dict[str, str]) -> list[dict[str, str]]:
    page_words = [
        (match.group(0), match.group(0).lower())
        for match in re.finditer(r"[A-Za-zÀ-ÖØ-öø-ÿ]{4,}", page_text)
    ]
    suspicious: list[dict[str, str]] = []
    seen_pairs: set[tuple[str, str]] = set()
    family_name_keys = {
        key
        for key, label in family_terms.items()
        if " " not in key
        and len(key) >= 4
        and key not in SUSPICIOUS_NAME_READING_STOPWORDS
        and label[:1].isupper()
    }
    term_items = [
        (key, label)
        for key, label in family_terms.items()
        if key in family_name_keys and len(key) >= 5
    ]
    for index, (word, lower_word) in enumerate(page_words):
        if lower_word in SUSPICIOUS_NAME_READING_STOPWORDS:
            continue
        for key, label in term_items:
            if lower_word == key or abs(len(lower_word) - len(key)) > 2:
                continue
            if lower_word[0] != key[0]:
                continue
            distance = levenshtein_distance_bounded(lower_word, key, 2)
            if distance is not None and 0 < distance <= 2:
                if lower_word[-1] != key[-1] and not word[0].isupper():
                    continue
                if not has_suspicious_name_context(page_words, index, key, family_name_keys):
                    continue
                pair = (lower_word, key)
                if pair in seen_pairs:
                    continue
                seen_pairs.add(pair)
                suspicious.append(
                    {
                        "literal": word,
                        "suspected": label,
                        "reason": f"near match to known family context term `{label}`",
                    }
                )
                break
    return suspicious[:25]


def has_suspicious_name_context(
    page_words: list[tuple[str, str]],
    index: int,
    suspected_key: str,
    family_name_keys: set[str],
) -> bool:
    start = max(0, index - 4)
    end = min(len(page_words), index + 5)
    nearby_words = [lower_word for _, lower_word in page_words[start:end]]
    for nearby in nearby_words:
        if nearby in family_name_keys and nearby != suspected_key:
            return True
    return any(nearby in SUSPICIOUS_NAME_CONTEXT_CUES for nearby in nearby_words)


def levenshtein_distance_bounded(a: str, b: str, max_distance: int) -> int | None:
    if abs(len(a) - len(b)) > max_distance:
        return None
    previous = list(range(len(b) + 1))
    for index_a, char_a in enumerate(a, start=1):
        current = [index_a]
        row_min = current[0]
        for index_b, char_b in enumerate(b, start=1):
            cost = 0 if char_a == char_b else 1
            current.append(min(current[-1] + 1, previous[index_b] + 1, previous[index_b - 1] + cost))
            row_min = min(row_min, current[-1])
        if row_min > max_distance:
            return None
        previous = current
    return previous[-1] if previous[-1] <= max_distance else None


def conversion_family_relevance(matched_terms: list[str], suspicious_readings: list[dict[str, str]]) -> str:
    if suspicious_readings and matched_terms:
        return "critical"
    if suspicious_readings:
        return "high"
    if len(matched_terms) >= 3:
        return "high"
    if matched_terms:
        return "medium"
    return "none"


def conversion_recommended_action(
    flags: list[str],
    family_relevance: str,
    suspicious_readings: list[dict[str, str]],
) -> str:
    severe_flags = {"placeholder_transcription", "image_preserved_not_transcribed", "no_transcription"}
    structural_flags = {
        "image_only_or_too_little_text",
        "possible_ocr_garbage_token",
        "possible_table_layout_loss",
        "many_uncertain_readings",
        "explicit_reread_needed",
    }
    if severe_flags.intersection(flags):
        return "reread-page"
    if "text_layer_only" in flags:
        return "reread-page"
    if suspicious_readings:
        return "reread-page"
    if family_relevance in {"high", "critical"} and flags:
        return "reread-page"
    if structural_flags.intersection(flags):
        return "spot-check"
    return "pass"


def conversion_confidence(flags: list[str], suspicious_readings: list[dict[str, str]]) -> str:
    severe_flags = {"placeholder_transcription", "image_preserved_not_transcribed", "no_transcription"}
    if severe_flags.intersection(flags):
        return "low"
    if suspicious_readings:
        return "low"
    if flags:
        return "medium"
    return "high"


def build_conversion_qc_triage_markdown(
    root: Path,
    converted_file: Path,
    chunk_manifest: Path,
    page_reviews: list[dict[str, object]],
) -> str:
    lines = conversion_qc_header(root, "Conversion QC Triage", converted_file, chunk_manifest)
    lines.extend(["## Page Summary", "", "| Page | Relevance | Confidence | Action | Flags | Matched Terms |", "| --- | --- | --- | --- | --- | --- |"])
    for review in page_reviews:
        lines.append(
            "| "
            f"{review['page']} | {review['family_relevance']} | {review['conversion_confidence']} | "
            f"{review['recommended_action']} | {', '.join(review['quality_flags']) or 'none'} | "
            f"{', '.join(review['matched_terms']) or 'none'} |"
        )
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def build_conversion_qc_page_queue_markdown(
    root: Path,
    converted_file: Path,
    chunk_manifest: Path,
    queued_pages: list[dict[str, object]],
) -> str:
    lines = conversion_qc_header(root, "Conversion QC Page Queue", converted_file, chunk_manifest)
    if not queued_pages:
        lines.extend(["## Queued Pages", "", "No pages queued for reread.", ""])
        return "\n".join(lines).rstrip() + "\n"
    lines.extend(["## Queued Pages", ""])
    for review in queued_pages:
        lines.extend(
            [
                f"### Page {review['page']}",
                "",
                f"- Recommended action: `{review['recommended_action']}`",
                f"- Conversion confidence: `{review['conversion_confidence']}`",
                f"- Family relevance: `{review['family_relevance']}`",
                f"- Quality flags: {', '.join(review['quality_flags']) or 'none'}",
                f"- Matched family context: {', '.join(review['matched_terms']) or 'none'}",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def build_conversion_qc_corrections_markdown(
    root: Path,
    converted_file: Path,
    chunk_manifest: Path,
    corrections: list[dict[str, str]],
) -> str:
    lines = conversion_qc_header(root, "Conversion QC Suspected Readings", converted_file, chunk_manifest)
    if not corrections:
        lines.extend(["## Suspected Readings", "", "No suspected readings generated by automatic QC.", ""])
        return "\n".join(lines).rstrip() + "\n"
    lines.extend(["## Suspected Readings", ""])
    for correction in corrections:
        lines.extend(
            [
                f"- Literal converted text: `{correction['literal']}`",
                f"  Suspected reading: `{correction['suspected']}`",
                f"  Reason: {correction['reason']}",
                "  Verification target: reread the page image or exact region before using this in a claim.",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def conversion_qc_header(root: Path, title: str, converted_file: Path, chunk_manifest: Path) -> list[str]:
    return [
        f"# {title}: {converted_file.stem}",
        "",
        f"- Converted file: `{relative_to_root(converted_file, root)}`",
        f"- Chunk manifest: `{relative_to_root(chunk_manifest, root)}`",
        "- Rule: do not edit converted Markdown here; queue exact pages or regions for reread.",
        "",
    ]


VAULT_TRANSCRIPTION_MAX_CHARS = 20000
PAGE_STATUS_ORDER = ["editable", "needs_visual_review", "transcription_pending", "needs_visual_conversion"]
QUALITY_FLAG_DESCRIPTIONS = {
    "placeholder_transcription": "The batch pass did not transcribe visible text.",
    "image_preserved_not_transcribed": "The page image was preserved, but the visible content still needs transcription.",
    "text_layer_only": "The page came from an automated PDF text layer and needs visual comparison.",
    "no_visual_crops": "No embedded image, stamp, signature, or layout crops were extracted.",
    "encoding_mojibake": "The text contains likely character encoding damage.",
    "missing_converted_markdown": "No assembled conversion exists for this page yet.",
    "missing_conversion_contract_sections": "The page output does not follow the required source-prep conversion sections.",
}
MOJIBAKE_MARKERS = ("\u00c3", "\u00c2", "\ufffd", "\u00e2\u20ac")


def assess_conversion_page_quality(page_text: str) -> tuple[str, list[str]]:
    flags: list[str] = []
    lower_text = page_text.lower()
    if "[no visible text transcribed in this batch pass.]" in lower_text:
        flags.append("placeholder_transcription")
    if "full standalone image copied" in lower_text or "full image copied as extracted visual evidence" in lower_text:
        flags.append("image_preserved_not_transcribed")
    if "pdf text-layer extraction may omit" in lower_text or "automated text-layer batch pass" in lower_text:
        flags.append("text_layer_only")
    if "no image crop was extracted" in lower_text:
        flags.append("no_visual_crops")
    if any(marker in page_text for marker in MOJIBAKE_MARKERS):
        flags.append("encoding_mojibake")

    if "placeholder_transcription" in flags or "image_preserved_not_transcribed" in flags:
        return "needs_visual_conversion", flags
    if flags:
        return "needs_visual_review", flags
    return "editable", flags


def source_status_from_page_records(page_records: list[dict[str, object]], converted_exists: bool) -> str:
    if not converted_exists:
        return "transcription_pending"
    statuses = {str(record.get("status", "")) for record in page_records}
    if "needs_visual_conversion" in statuses:
        return "needs_visual_conversion"
    if "transcription_pending" in statuses:
        return "transcription_pending"
    if "needs_visual_review" in statuses:
        return "needs_visual_review"
    if page_records:
        return "editable"
    return "transcription_pending"


def count_page_statuses(page_records: list[dict[str, object]]) -> dict[str, int]:
    counts = {status: 0 for status in PAGE_STATUS_ORDER}
    for record in page_records:
        status = str(record.get("status", "editable"))
        counts[status] = counts.get(status, 0) + 1
    return counts


def yaml_inline_list(values: list[str]) -> str:
    return "[" + ", ".join(json.dumps(value, ensure_ascii=False) for value in values) + "]"


def quality_flags_for_record(record: dict[str, object]) -> list[str]:
    flags = record.get("quality_flags", [])
    if not isinstance(flags, list):
        return []
    return [str(flag) for flag in flags]


def format_quality_flags_cell(flags: list[str]) -> str:
    if not flags:
        return "none"
    return ", ".join(f"`{flag}`" for flag in flags)


def build_quality_flags_section(flags: list[str]) -> str:
    lines = ["## Quality Flags", ""]
    if not flags:
        lines.append("No automated quality flags.")
    else:
        lines.extend(f"- `{flag}`: {QUALITY_FLAG_DESCRIPTIONS.get(flag, 'Review before research use.')}" for flag in flags)
    return "\n".join(lines)


def update_existing_vault_page_quality(page_path: Path, status: str, flags: list[str]) -> bool:
    if not page_path.exists():
        return False
    text = page_path.read_text(encoding="utf-8")
    updated = update_frontmatter_value(text, "status", status)
    updated = update_frontmatter_value(updated, "quality_flags", yaml_inline_list(flags))
    updated = upsert_markdown_section(updated, "Quality Flags", build_quality_flags_section(flags), before_heading="Page Image")
    if updated == text:
        return False
    page_path.write_text(updated, encoding="utf-8")
    return True


def update_frontmatter_value(text: str, key: str, value: str) -> str:
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---", 4)
    if end == -1:
        return text
    frontmatter = text[4:end].strip("\n").splitlines()
    replacement = f"{key}: {value}"
    for index, line in enumerate(frontmatter):
        if line.startswith(f"{key}:"):
            frontmatter[index] = replacement
            break
    else:
        frontmatter.append(replacement)
    return "---\n" + "\n".join(frontmatter).rstrip() + "\n---" + text[end + 4 :]


def upsert_markdown_section(text: str, heading: str, section: str, before_heading: str | None = None) -> str:
    pattern = rf"(?ms)^## {re.escape(heading)}\n.*?(?=^## |\Z)"
    if re.search(pattern, text):
        return re.sub(pattern, section.rstrip() + "\n\n", text, count=1)
    if before_heading:
        marker = f"\n## {before_heading}\n"
        if marker in text:
            return text.replace(marker, "\n" + section.rstrip() + "\n\n" + f"## {before_heading}\n", 1)
    return text.rstrip() + "\n\n" + section.rstrip() + "\n"


def sync_vault_transcriptions(root: Path, force: bool = False) -> list[Path]:
    """Expose conversions as small editable Obsidian source/page notes.

    The flat note under research/sources/transcriptions is only an index. Editable
    text lives in child page or page-part notes so Obsidian never has to render a
    giant source in one buffer.
    """
    paths = WikiPaths(root.resolve())
    manifest_path = paths.raw / "source-prep-manifest.json"
    if not manifest_path.exists():
        manifest_path = write_source_prep_index(paths.root)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))

    written: list[Path] = []
    dashboard_rows = []
    for source in manifest.get("sources", []):
        job = first_available_conversion_job(paths.root, source)
        if not job:
            continue

        source_page = find_or_default_source_page(paths.root, source)
        source_stem = source_page.stem
        transcription_index = paths.research / "sources" / "transcriptions" / f"{source_stem}.md"
        pages_dir = paths.research / "sources" / "transcriptions" / source_stem
        converted_file = converted_path_for_job(paths.root, job)
        chunk_manifest = chunk_manifest_for_converted(paths.root, converted_file)
        job_manifest = paths.root / job["manifest"]

        archive_legacy_transcription_note(paths.root, transcription_index)
        copy_conversion_assets_to_vault(paths.root, source_stem, job_manifest, force=force)
        page_records, page_paths = write_vault_transcription_page_notes(
            root=paths.root,
            source=source,
            source_page=source_page,
            transcription_index=transcription_index,
            pages_dir=pages_dir,
            converted_file=converted_file,
            chunk_manifest=chunk_manifest,
            job_manifest=job_manifest,
            source_stem=source_stem,
            force=force,
        )
        written.extend(page_paths)

        transcription_index.parent.mkdir(parents=True, exist_ok=True)
        transcription_index.write_text(
            build_vault_transcription_index_markdown(
                root=paths.root,
                source=source,
                source_page=source_page,
                transcription_index=transcription_index,
                pages_dir=pages_dir,
                converted_file=converted_file,
                chunk_manifest=chunk_manifest,
                job_manifest=job_manifest,
                page_records=page_records,
            ),
            encoding="utf-8",
        )
        written.append(transcription_index)

        update_source_page_with_transcription_link(source_page, transcription_index, paths.research)
        source_status = source_status_from_page_records(page_records, converted_file.exists())
        dashboard_rows.append(
            {
                "title": str(source.get("title", "")),
                "status": source_status,
                "source_page": source_page,
                "transcription": transcription_index,
                "page_count": len(page_records),
                "status_counts": count_page_statuses(page_records),
            }
        )

    write_conversion_dashboard(paths.root, dashboard_rows)
    update_index_with_transcriptions(paths.root, dashboard_rows)
    if written:
        append_log(paths.research / "log.md", f"vault-transcriptions | Wrote {len(written)} index/page notes")
    return written


def first_available_conversion_job(root: Path, source: dict[str, object]) -> dict[str, str] | None:
    jobs = [
        {key: str(value) for key, value in job.items()}
        for job in source.get("conversion_jobs", [])
        if isinstance(job, dict) and job.get("manifest") and (root / str(job["manifest"])).exists()
    ]
    for job in jobs:
        if converted_path_for_job(root, job).exists():
            return job
    return jobs[0] if jobs else None


def converted_path_for_job(root: Path, job: dict[str, str]) -> Path:
    manifest_path = root / job["manifest"]
    return root / "raw" / "converted" / f"{manifest_path.parent.name}.codex.md"


def chunk_manifest_for_converted(root: Path, converted_file: Path) -> Path:
    return root / "raw" / "chunks" / slug(converted_file.stem) / "manifest.json"


def find_or_default_source_page(root: Path, source: dict[str, object]) -> Path:
    source_dir = WikiPaths(root.resolve()).research / "sources"
    prefix = slug(str(source.get("id", "")))
    title_slug = slug(str(source.get("title", "")))[:96]
    exact = source_dir / f"{prefix}-{title_slug}.md"
    if exact.exists():
        return exact
    matches = sorted(path for path in source_dir.glob(f"{prefix}-*.md") if path.parent == source_dir)
    if matches:
        return matches[0]
    return exact


def archive_legacy_transcription_note(root: Path, transcription_index: Path) -> None:
    if not transcription_index.exists():
        return
    text = transcription_index.read_text(encoding="utf-8")
    if "type: source_transcription_index" in text:
        return
    if "type: source_transcription" not in text and "# Page " not in text:
        return
    archive_dir = WikiPaths(root.resolve()).staging / "legacy-transcription-notes"
    archive_dir.mkdir(parents=True, exist_ok=True)
    archive_path = archive_dir / f"{transcription_index.stem}.full.md"
    if not archive_path.exists():
        shutil.copy2(transcription_index, archive_path)


def copy_conversion_assets_to_vault(root: Path, source_stem: str, manifest_path: Path, force: bool = False) -> None:
    if not manifest_path.exists():
        return
    job_dir = manifest_path.parent
    asset_root = WikiPaths(root.resolve()).research / "_assets" / "conversions" / source_stem
    for folder_name in ["page-images", "extracted-images"]:
        source_dir = job_dir / folder_name
        if not source_dir.exists():
            continue
        destination_dir = asset_root / folder_name
        for source_file in source_dir.rglob("*"):
            if not source_file.is_file():
                continue
            destination = destination_dir / source_file.relative_to(source_dir)
            destination.parent.mkdir(parents=True, exist_ok=True)
            if force or not destination.exists():
                shutil.copy2(source_file, destination)


def write_vault_transcription_page_notes(
    root: Path,
    source: dict[str, object],
    source_page: Path,
    transcription_index: Path,
    pages_dir: Path,
    converted_file: Path,
    chunk_manifest: Path,
    job_manifest: Path,
    source_stem: str,
    force: bool,
) -> tuple[list[dict[str, object]], list[Path]]:
    pages_dir.mkdir(parents=True, exist_ok=True)
    manifest_pages = load_job_pages(root, job_manifest)
    page_records: list[dict[str, object]] = []
    written: list[Path] = []

    if converted_file.exists():
        converted_text = converted_file.read_text(encoding="utf-8")
        for page_number, page_text in split_page_markdown(converted_text):
            parts = split_chunk_text(page_text, VAULT_TRANSCRIPTION_MAX_CHARS)
            for part_number, part_text in enumerate(parts, start=1):
                split_page = len(parts) > 1
                page_path = pages_dir / (
                    f"page-{page_number:04d}-part-{part_number:02d}.md" if split_page else f"page-{page_number:04d}.md"
                )
                status, quality_flags = assess_conversion_page_quality(part_text)
                page_record = build_page_record(
                    root=root,
                    source_stem=source_stem,
                    page_path=page_path,
                    page_number=page_number,
                    part_number=part_number,
                    split_page=split_page,
                    manifest_page=manifest_pages.get(page_number),
                    status=status,
                )
                page_record["quality_flags"] = quality_flags
                page_records.append(page_record)
                if force or not page_path.exists():
                    page_path.write_text(
                        build_vault_transcription_page_markdown(
                            root=root,
                            source=source,
                            source_page=source_page,
                            transcription_index=transcription_index,
                            converted_file=converted_file,
                            chunk_manifest=chunk_manifest,
                            job_manifest=job_manifest,
                            page_record=page_record,
                            page_text=rewrite_conversion_asset_links(
                                part_text,
                                source_stem,
                                asset_prefix="../../../_assets/conversions/",
                            ),
                        ),
                        encoding="utf-8",
                    )
                    written.append(page_path)
                elif update_existing_vault_page_quality(page_path, status, quality_flags):
                    written.append(page_path)
        return page_records, written

    for page_number, manifest_page in sorted(manifest_pages.items()):
        page_path = pages_dir / f"page-{page_number:04d}.md"
        quality_flags = ["missing_converted_markdown"]
        page_record = build_page_record(
            root=root,
            source_stem=source_stem,
            page_path=page_path,
            page_number=page_number,
            part_number=1,
            split_page=False,
            manifest_page=manifest_page,
            status="transcription_pending",
        )
        page_record["quality_flags"] = quality_flags
        page_records.append(page_record)
        if force or not page_path.exists():
            page_path.write_text(
                build_pending_vault_page_markdown(
                    root=root,
                    source=source,
                    source_page=source_page,
                    transcription_index=transcription_index,
                    job_manifest=job_manifest,
                    page_record=page_record,
                ),
                encoding="utf-8",
            )
            written.append(page_path)
        elif update_existing_vault_page_quality(page_path, "transcription_pending", quality_flags):
            written.append(page_path)
    return page_records, written


def load_job_pages(root: Path, job_manifest: Path) -> dict[int, dict[str, object]]:
    if not job_manifest.exists():
        return {}
    try:
        manifest = json.loads(job_manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    pages: dict[int, dict[str, object]] = {}
    for page in manifest.get("pages", []):
        try:
            pages[int(page["page"])] = page
        except (KeyError, TypeError, ValueError):
            continue
    return pages


def build_page_record(
    root: Path,
    source_stem: str,
    page_path: Path,
    page_number: int,
    part_number: int,
    split_page: bool,
    manifest_page: dict[str, object] | None,
    status: str = "editable",
) -> dict[str, object]:
    image_path = ""
    generated_page = ""
    if manifest_page:
        raw_image = str(manifest_page.get("image_path", ""))
        if raw_image:
            image_path = relative_path(
                page_path.parent,
                WikiPaths(root.resolve()).research
                / "_assets"
                / "conversions"
                / source_stem
                / "page-images"
                / Path(raw_image).name,
            )
        raw_page = str(manifest_page.get("output_path", ""))
        if raw_page:
            generated_page = raw_page
    return {
        "path": page_path,
        "page_number": page_number,
        "part_number": part_number,
        "split_page": split_page,
        "status": status,
        "image_path": image_path,
        "generated_page": generated_page,
    }


def rewrite_conversion_asset_links(
    text: str,
    source_stem: str,
    asset_prefix: str = "../../_assets/conversions/",
) -> str:
    def replace(match: re.Match[str]) -> str:
        alt_text = match.group(1)
        target = match.group(2).strip()
        if target.startswith(("http://", "https://", "file:", "#")):
            return match.group(0)
        normalized = target.strip("<>")
        if normalized.startswith("../extracted-images/"):
            asset_target = asset_prefix + source_stem + "/extracted-images/" + normalized.removeprefix(
                "../extracted-images/"
            )
        elif normalized.startswith("../page-images/"):
            asset_target = asset_prefix + source_stem + "/page-images/" + normalized.removeprefix("../page-images/")
        else:
            return match.group(0)
        return f"![{alt_text}]({asset_target})"

    return re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", replace, text)


def build_vault_transcription_index_markdown(
    root: Path,
    source: dict[str, object],
    source_page: Path,
    transcription_index: Path,
    pages_dir: Path,
    converted_file: Path,
    chunk_manifest: Path,
    job_manifest: Path,
    page_records: list[dict[str, object]],
) -> str:
    title = str(source.get("title", "Untitled source"))
    status = source_status_from_page_records(page_records, converted_file.exists())
    status_counts = count_page_statuses(page_records)
    status_summary = "\n".join(f"- `{key}`: {status_counts.get(key, 0)}" for key in PAGE_STATUS_ORDER)
    rows = "\n".join(
        "| "
        f"{wiki_link_for_path(record['path'], WikiPaths(root.resolve()).research, page_record_label(record))} | "
        f"{record['status']} | "
        f"{format_quality_flags_cell(quality_flags_for_record(record))} |"
        for record in page_records
        if isinstance(record.get("path"), Path)
    )
    return f"""---
type: source_transcription_index
status: {status}
source_id: {yaml_string(str(source.get("id", "")))}
media_type: {yaml_string(str(source.get("media_type", "")))}
raw_file: {yaml_string(str(source.get("raw_path", "")))}
source_sha256: {yaml_string(str(source.get("sha256", "")))}
generated_from: {yaml_string(relative_to_root(converted_file, root) if converted_file.exists() else "")}
conversion_manifest: {yaml_string(relative_to_root(job_manifest, root))}
chunk_manifest: {yaml_string(relative_to_root(chunk_manifest, root) if chunk_manifest.exists() else "")}
quality_page_counts: {json.dumps(status_counts, ensure_ascii=False)}
source_page: {yaml_string(wiki_link_for_path(source_page, WikiPaths(root.resolve()).research))}
page_folder: {yaml_string(wiki_link_for_path(pages_dir / "page-0001.md", WikiPaths(root.resolve()).research) if page_records else "")}
tags: [source-transcription, transcription-index]
---

# {title}

## Edit By Page

Open the page notes below for manual correction. This index intentionally stays small so Obsidian does not need to render the full source at once.

## Source Links

- Source page: {wiki_link_for_path(source_page, WikiPaths(root.resolve()).research)}
- Original raw source: [{source.get("raw_path", "")}]({relative_path(transcription_index.parent, root / str(source.get("raw_path", "")))})
- Generated Markdown: {format_optional_file_link(transcription_index.parent, converted_file, root)}
- Conversion manifest: [{relative_to_root(job_manifest, root)}]({relative_path(transcription_index.parent, job_manifest)})
- Chunk manifest: {format_optional_file_link(transcription_index.parent, chunk_manifest, root)}

## Quality Summary

{status_summary}

## Page Notes

| Page Note | Status | Quality Flags |
| --- | --- | --- |
{rows}
"""


def page_record_label(record: dict[str, object]) -> str:
    page_number = int(record.get("page_number", 1))
    if record.get("split_page"):
        return f"Page {page_number}, part {int(record.get('part_number', 1))}"
    return f"Page {page_number}"


def build_vault_transcription_page_markdown(
    root: Path,
    source: dict[str, object],
    source_page: Path,
    transcription_index: Path,
    converted_file: Path,
    chunk_manifest: Path,
    job_manifest: Path,
    page_record: dict[str, object],
    page_text: str,
) -> str:
    page_path = page_record["path"]
    if not isinstance(page_path, Path):
        raise TypeError("page_record path must be a Path")
    page_number = int(page_record.get("page_number", 1))
    part_number = int(page_record.get("part_number", 1))
    part_label = f" Part {part_number}" if page_record.get("split_page") else ""
    status = str(page_record.get("status", "editable"))
    quality_flags = quality_flags_for_record(page_record)
    page_image = str(page_record.get("image_path", ""))
    page_image_block = f"![Prepared page image]({page_image})" if page_image else "No rendered page image linked."
    generated_page = str(page_record.get("generated_page", ""))
    generated_page_link = (
        f"[{generated_page}]({relative_path(page_path.parent, root / generated_page)})" if generated_page else "not available"
    )
    return f"""---
type: source_transcription_page
status: {status}
source_id: {yaml_string(str(source.get("id", "")))}
source_page_number: {page_number}
part: {part_number}
raw_file: {yaml_string(str(source.get("raw_path", "")))}
source_sha256: {yaml_string(str(source.get("sha256", "")))}
generated_from: {yaml_string(relative_to_root(converted_file, root))}
generated_page_markdown: {yaml_string(generated_page)}
conversion_manifest: {yaml_string(relative_to_root(job_manifest, root))}
chunk_manifest: {yaml_string(relative_to_root(chunk_manifest, root) if chunk_manifest.exists() else "")}
source_page: {yaml_string(wiki_link_for_path(source_page, WikiPaths(root.resolve()).research))}
transcription_index: {yaml_string(wiki_link_for_path(transcription_index, WikiPaths(root.resolve()).research))}
quality_flags: {yaml_inline_list(quality_flags)}
tags: [source-transcription, transcription-page, editable]
---

# {source.get("title", "Untitled source")} - Page {page_number}{part_label}

## Breadcrumbs

- Transcription index: {wiki_link_for_path(transcription_index, WikiPaths(root.resolve()).research)}
- Source page: {wiki_link_for_path(source_page, WikiPaths(root.resolve()).research)}
- Original raw source: [{source.get("raw_path", "")}]({relative_path(page_path.parent, root / str(source.get("raw_path", "")))})
- Generated conversion: [{relative_to_root(converted_file, root)}]({relative_path(page_path.parent, converted_file)})
- Generated page Markdown: {generated_page_link}
- Conversion manifest: [{relative_to_root(job_manifest, root)}]({relative_path(page_path.parent, job_manifest)})
- Chunk manifest: {format_optional_file_link(page_path.parent, chunk_manifest, root)}

{build_quality_flags_section(quality_flags)}

## Page Image

{page_image_block}

## Editable Conversion Text

{page_text.strip()}
"""


def build_pending_vault_page_markdown(
    root: Path,
    source: dict[str, object],
    source_page: Path,
    transcription_index: Path,
    job_manifest: Path,
    page_record: dict[str, object],
) -> str:
    page_path = page_record["path"]
    if not isinstance(page_path, Path):
        raise TypeError("page_record path must be a Path")
    page_number = int(page_record.get("page_number", 1))
    quality_flags = quality_flags_for_record(page_record)
    page_image = str(page_record.get("image_path", ""))
    page_image_block = f"![Prepared page image]({page_image})" if page_image else "No rendered page image linked."
    return f"""---
type: source_transcription_page
status: transcription_pending
source_id: {yaml_string(str(source.get("id", "")))}
source_page_number: {page_number}
part: 1
raw_file: {yaml_string(str(source.get("raw_path", "")))}
source_sha256: {yaml_string(str(source.get("sha256", "")))}
conversion_manifest: {yaml_string(relative_to_root(job_manifest, root))}
source_page: {yaml_string(wiki_link_for_path(source_page, WikiPaths(root.resolve()).research))}
transcription_index: {yaml_string(wiki_link_for_path(transcription_index, WikiPaths(root.resolve()).research))}
quality_flags: {yaml_inline_list(quality_flags)}
tags: [source-transcription, transcription-page, transcription-pending]
---

# {source.get("title", "Untitled source")} - Page {page_number}

## Breadcrumbs

- Transcription index: {wiki_link_for_path(transcription_index, WikiPaths(root.resolve()).research)}
- Source page: {wiki_link_for_path(source_page, WikiPaths(root.resolve()).research)}
- Original raw source: [{source.get("raw_path", "")}]({relative_path(page_path.parent, root / str(source.get("raw_path", "")))})
- Conversion manifest: [{relative_to_root(job_manifest, root)}]({relative_path(page_path.parent, job_manifest)})

{build_quality_flags_section(quality_flags)}

## Page Image

{page_image_block}

## Literal Transcription

[Manual transcription pending.]

## Images, Captions, And Visual Notes

## Translation

## Interpretation

## Uncertain Or Illegible

## Completeness Audit
"""


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def wiki_link_for_path(path: Path, wiki_root: Path, alias: str | None = None) -> str:
    target = path.with_suffix("").resolve().relative_to(wiki_root.resolve()).as_posix()
    return f"[[{target}|{alias}]]" if alias else f"[[{target}]]"


def format_optional_file_link(from_dir: Path, path: Path, root: Path) -> str:
    if not path.exists():
        return "not available"
    return f"[{relative_to_root(path, root)}]({relative_path(from_dir, path)})"


def update_source_page_with_transcription_link(
    source_page: Path,
    transcription_index: Path,
    wiki_root: Path,
) -> None:
    if not source_page.exists():
        return
    text = source_page.read_text(encoding="utf-8")
    transcription_link = wiki_link_for_path(transcription_index, wiki_root, "Open transcription index")
    text = text.replace("Edit full transcription in Obsidian", "Open transcription index")
    if transcription_link not in text:
        entry = f"- {transcription_link}"
        if "## Obsidian Inspection" in text:
            text = text.replace("## Obsidian Inspection\n", f"## Obsidian Inspection\n\n{entry}\n", 1)
        else:
            text = text.replace("## Conversion Artifacts", f"## Obsidian Inspection\n\n{entry}\n\n## Conversion Artifacts", 1)
    text = text.replace(
        "Use the converted Markdown and chunk manifest above as the prepared source text. Do not create claims directly from this page without checking the converted source and original image/file evidence.",
        f"Open the page-level editable transcription from {transcription_link}. Each page note links back to the original source material and generated conversion artifacts.",
    )
    text = re.sub(
        r"Edit the full prepared transcription in \[\[sources/transcriptions/[^\]]+\|(?:Edit full transcription in Obsidian|Open transcription index)\]\]\. Check the original image/file evidence before creating claims\.",
        f"Open the page-level editable transcription from {transcription_link}. Each page note links back to the original source material and generated conversion artifacts.",
        text,
    )
    source_page.write_text(text, encoding="utf-8")


def count_chunks(chunk_manifest: Path) -> int:
    if not chunk_manifest.exists():
        return 0
    try:
        manifest = json.loads(chunk_manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return 0
    chunks = manifest.get("chunks", [])
    return len(chunks) if isinstance(chunks, list) else 0


def count_markdown_files(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for item in path.rglob("*.md") if item.is_file())


def write_conversion_dashboard(root: Path, rows: list[dict[str, object]]) -> Path:
    paths = WikiPaths(root.resolve())
    dashboard = paths.research / "Conversion Dashboard.md"
    rows = sorted(rows, key=lambda item: str(item["title"]).lower())
    lines = [
        "# Conversion Dashboard",
        "",
        "Use this page to inspect and edit prepared source conversions from inside the Obsidian vault.",
        "",
        f"- Source transcription indexes: {len(rows)}",
        f"- Page or page-part notes: {sum(int(row.get('page_count', 0)) for row in rows)}",
        f"- Pages needing visual conversion: {sum(int(row.get('status_counts', {}).get('needs_visual_conversion', 0)) for row in rows if isinstance(row.get('status_counts'), dict))}",
        f"- Pages needing visual review: {sum(int(row.get('status_counts', {}).get('needs_visual_review', 0)) for row in rows if isinstance(row.get('status_counts'), dict))}",
        "- Source material links are preserved on every page note.",
        "",
        "| Source | Status | Page Notes | Needs Visual Conversion | Needs Visual Review | Source Page |",
        "| --- | --- | ---: | ---: | ---: | --- |",
    ]
    wiki_root = paths.research
    for row in rows:
        transcription = row["transcription"]
        source_page = row["source_page"]
        if not isinstance(transcription, Path) or not isinstance(source_page, Path):
            continue
        status_counts = row.get("status_counts", {})
        if not isinstance(status_counts, dict):
            status_counts = {}
        lines.append(
            "| "
            f"{wiki_link_for_path(transcription, wiki_root, str(row['title']))} | "
            f"{row['status']} | "
            f"{row['page_count']} | "
            f"{status_counts.get('needs_visual_conversion', 0)} | "
            f"{status_counts.get('needs_visual_review', 0)} | "
            f"{wiki_link_for_path(source_page, wiki_root, 'Source page')} |"
        )
    dashboard.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return dashboard


def update_index_with_transcriptions(root: Path, rows: list[dict[str, object]]) -> None:
    paths = WikiPaths(root.resolve())
    index_path = paths.research / "index.md"
    append_index_reference(index_path, "Conversion Views", "[[Conversion Dashboard]]")
    for row in sorted(rows, key=lambda item: str(item["title"]).lower()):
        transcription = row.get("transcription")
        if isinstance(transcription, Path):
            append_index_reference(
                index_path,
                "Source Transcriptions",
                wiki_link_for_path(transcription, paths.research, str(row["title"])),
            )

def parse_conversion_metadata(text: str) -> tuple[str, str, str]:
    return (
        extract_markdown_metadata_value(text, "Source"),
        extract_markdown_metadata_value(text, "Source SHA-256"),
        extract_markdown_metadata_value(text, "Manifest"),
    )


def extract_markdown_metadata_value(text: str, label: str) -> str:
    pattern = rf"^- {re.escape(label)}: `([^`]+)`"
    match = re.search(pattern, text, flags=re.MULTILINE)
    return match.group(1) if match else ""


def split_page_markdown(text: str) -> list[tuple[int, str]]:
    matches = list(re.finditer(r"^# Page\s+(\d+)\s*$", text, flags=re.MULTILINE))
    if not matches:
        metadata_matches = list(re.finditer(r"^## Page Metadata\s*$", text, flags=re.MULTILINE | re.IGNORECASE))
        if metadata_matches:
            pages: list[tuple[int, str]] = []
            for index, match in enumerate(metadata_matches):
                start = 0 if index == 0 else match.start()
                end = metadata_matches[index + 1].start() if index + 1 < len(metadata_matches) else len(text)
                page_text = text[start:end].strip()
                page_number = markdown_page_number(page_text, index + 1)
                if page_text:
                    pages.append((page_number, page_text))
            if pages:
                return pages
        return [(1, text.strip())] if text.strip() else []

    pages: list[tuple[int, str]] = []
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        pages.append((int(match.group(1)), text[start:end].strip()))
    return pages


def markdown_page_number(text: str, fallback: int) -> int:
    for pattern in (
        r"^\s*-\s*(?:\*\*)?(?:page[_ -]?number|page)(?:\*\*)?\s*:\s*`?(\d+)`?",
        r":p0*(\d+)\b",
    ):
        match = re.search(pattern, text, flags=re.MULTILINE | re.IGNORECASE)
        if match:
            page = safe_int(match.group(1), 0)
            if page > 0:
                return page
    return fallback


def split_chunk_text(text: str, max_chars: int) -> list[str]:
    if len(text) <= max_chars:
        return [text.strip()]

    sections = split_markdown_sections(text)
    chunks: list[str] = []
    current = ""
    for section in sections:
        if len(section) > max_chars:
            if current.strip():
                chunks.append(current.strip())
                current = ""
            chunks.extend(split_long_text(section, max_chars))
            continue
        if current and len(current) + len(section) + 2 > max_chars:
            chunks.append(current.strip())
            current = section
        else:
            current = f"{current.rstrip()}\n\n{section.strip()}".strip() if current else section

    if current.strip():
        chunks.append(current.strip())
    return chunks


def split_markdown_sections(text: str) -> list[str]:
    matches = list(re.finditer(r"^##\s+.+$", text, flags=re.MULTILINE))
    if not matches:
        return [text.strip()] if text.strip() else []

    sections: list[str] = []
    if matches[0].start() > 0:
        sections.append(text[: matches[0].start()].strip())
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        section = text[start:end].strip()
        if section:
            sections.append(section)
    return [section for section in sections if section]


def split_long_text(text: str, max_chars: int) -> list[str]:
    parts: list[str] = []
    current = ""
    for paragraph in re.split(r"(\n\s*\n)", text):
        if not paragraph:
            continue
        if len(paragraph) > max_chars:
            if current.strip():
                parts.append(current.strip())
                current = ""
            parts.extend(split_by_lines(paragraph, max_chars))
            continue
        if current and len(current) + len(paragraph) > max_chars:
            parts.append(current.strip())
            current = paragraph
        else:
            current += paragraph
    if current.strip():
        parts.append(current.strip())
    return parts


def split_by_lines(text: str, max_chars: int) -> list[str]:
    parts: list[str] = []
    current = ""
    for line in text.splitlines(keepends=True):
        if current and len(current) + len(line) > max_chars:
            parts.append(current.strip())
            current = line
        else:
            current += line
    if current.strip():
        parts.append(current.strip())
    return parts


def build_chunk_markdown(
    chunk_id: str,
    converted_file: str,
    converted_hash: str,
    source_path: str,
    source_hash: str,
    source_manifest: str,
    page_number: int,
    part_number: int,
    chunk_text: str,
) -> str:
    return f"""---
type: source_prep_chunk
chunk_id: {chunk_id}
source_converted: {converted_file}
converted_sha256: {converted_hash}
source: {source_path}
source_sha256: {source_hash}
source_manifest: {source_manifest}
page_start: {page_number}
page_end: {page_number}
part: {part_number}
---

{chunk_text.strip()}
"""


def source_prep_jobs_by_hash(root: Path) -> dict[str, list[dict[str, str]]]:
    jobs: dict[str, list[dict[str, str]]] = {}
    jobs_dir = root / "raw" / "codex-conversion-jobs"
    if not jobs_dir.exists():
        return jobs
    for manifest_path in jobs_dir.glob("*/manifest.json"):
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        digest = manifest.get("source_sha256")
        if not digest:
            continue
        chunking = manifest.get("chunking", {})
        page_range = ""
        if isinstance(chunking, dict):
            page_range = str(chunking.get("page_range", ""))
        jobs.setdefault(digest, []).append(
            {
                "job_id": str(manifest.get("job_id", "")),
                "title": str(manifest.get("title", "")),
                "manifest": relative_to_root(manifest_path, root),
                "status": str(manifest.get("status", "")),
                "page_range": page_range,
            }
        )
    return jobs


def source_prep_conversions_by_hash(root: Path) -> dict[str, list[dict[str, str]]]:
    conversions: dict[str, list[dict[str, str]]] = {}
    converted_dir = root / "raw" / "converted"
    if not converted_dir.exists():
        return conversions
    for converted_path in converted_dir.rglob("*.md"):
        try:
            text = converted_path.read_text(encoding="utf-8")
        except OSError:
            continue
        source_path, source_hash, source_manifest = parse_conversion_metadata(text)
        if not source_hash:
            continue
        conversions.setdefault(source_hash, []).append(
            {
                "path": relative_to_root(converted_path, root),
                "source": source_path,
                "source_manifest": source_manifest,
                "sha256": file_sha256(converted_path),
            }
        )
    return conversions


def source_prep_status(jobs: list[dict[str, str]], conversions: list[dict[str, str]]) -> str:
    if conversions and jobs and len(conversions) < len(jobs):
        return "partially_converted"
    if conversions:
        return "converted"
    if jobs:
        return "queued_for_agent_conversion"
    return "raw"


AGENT_TASK_STATE_STATUSES = {"claimed", "in_progress", "done", "failed", "released"}


def utc_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def parse_utc_timestamp(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    cleaned = value.strip()
    if not cleaned:
        return None
    if cleaned.endswith("Z"):
        cleaned = f"{cleaned[:-1]}+00:00"
    try:
        parsed = datetime.fromisoformat(cleaned)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def agent_task_state_path(root: Path) -> Path:
    return root.resolve() / "research" / "_agent-queues" / "task-state.json"


@contextmanager
def agent_task_state_lock(root: Path, timeout_seconds: float = 60.0):
    path = agent_task_state_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    lock_path = path.with_suffix(path.suffix + ".lock")
    deadline = time.monotonic() + timeout_seconds

    with lock_path.open("a+b") as lock_file:
        lock_file.seek(0)
        if not lock_file.read(1):
            lock_file.write(b"0")
            lock_file.flush()
        lock_file.seek(0)

        locked = False
        while not locked:
            try:
                if os.name == "nt":
                    import msvcrt

                    msvcrt.locking(lock_file.fileno(), msvcrt.LK_NBLCK, 1)
                else:
                    import fcntl

                    fcntl.flock(lock_file.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                locked = True
            except OSError as exc:
                if time.monotonic() >= deadline:
                    raise TimeoutError(f"timed out waiting for task-state lock: {lock_path}") from exc
                time.sleep(0.1)

        try:
            yield
        finally:
            lock_file.seek(0)
            if os.name == "nt":
                import msvcrt

                msvcrt.locking(lock_file.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                import fcntl

                fcntl.flock(lock_file.fileno(), fcntl.LOCK_UN)


def read_agent_task_state_payload(root: Path) -> dict[str, object]:
    path = agent_task_state_path(root)
    if not path.exists():
        return {"created": utc_timestamp(), "updated": utc_timestamp(), "tasks": {}}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"created": utc_timestamp(), "updated": utc_timestamp(), "tasks": {}}
    if not isinstance(payload, dict):
        return {"created": utc_timestamp(), "updated": utc_timestamp(), "tasks": {}}
    if not isinstance(payload.get("tasks"), dict):
        payload["tasks"] = {}
    return payload


def load_agent_task_state(root: Path) -> dict[str, dict[str, object]]:
    payload = read_agent_task_state_payload(root)
    tasks = payload.get("tasks", {})
    if not isinstance(tasks, dict):
        return {}
    return {str(task_id): dict(state) for task_id, state in tasks.items() if isinstance(state, dict)}


def save_agent_task_state(root: Path, task_state: dict[str, dict[str, object]]) -> Path:
    existing = read_agent_task_state_payload(root)
    path = agent_task_state_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "created": str(existing.get("created") or utc_timestamp()),
        "updated": utc_timestamp(),
        "purpose": "Durable claim/start/finish state for Codex agent queue tasks.",
        "tasks": task_state,
    }
    tmp_path = path.with_name(f"{path.name}.tmp")
    tmp_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    tmp_path.replace(path)
    return path


def update_agent_task_states(
    root: Path,
    task_ids: list[str],
    status: str,
    agent: str = "",
    note: str = "",
) -> Path:
    if status not in AGENT_TASK_STATE_STATUSES:
        raise ValueError(f"unsupported task status: {status}")
    with agent_task_state_lock(root):
        task_state = load_agent_task_state(root)
        now = utc_timestamp()
        for task_id in task_ids:
            current = dict(task_state.get(task_id, {}))
            current["status"] = status
            current["updated_at"] = now
            if agent:
                current["agent"] = agent
            if note:
                current["note"] = note
            if status in {"claimed", "in_progress"} and "claimed_at" not in current:
                current["claimed_at"] = now
            if status == "in_progress" and "started_at" not in current:
                current["started_at"] = now
            if status == "done":
                current["completed_at"] = now
            if status == "failed":
                current["failed_at"] = now
            if status == "released":
                released_by = agent or str(current.get("agent", "")).strip()
                if released_by:
                    current["released_by"] = released_by
                current.pop("agent", None)
                current["released_at"] = now
            task_state[task_id] = current
        return save_agent_task_state(root, task_state)


def update_agent_task_state(root: Path, task_id: str, status: str, agent: str = "", note: str = "") -> Path:
    return update_agent_task_states(root, [task_id], status, agent=agent, note=note)


def release_stale_agent_tasks(root: Path, stale_minutes: int = 360) -> int:
    if stale_minutes <= 0:
        return 0
    with agent_task_state_lock(root):
        task_state = load_agent_task_state(root)
        if not task_state:
            return 0

        now = datetime.now(timezone.utc)
        cutoff = now - timedelta(minutes=stale_minutes)
        now_text = now.isoformat(timespec="seconds").replace("+00:00", "Z")
        released_count = 0
        for task_id, current in list(task_state.items()):
            status = str(current.get("status", "")).strip()
            if status not in {"claimed", "in_progress"}:
                continue
            last_update = (
                parse_utc_timestamp(current.get("updated_at"))
                or parse_utc_timestamp(current.get("started_at"))
                or parse_utc_timestamp(current.get("claimed_at"))
            )
            if last_update is None or last_update > cutoff:
                continue
            updated = dict(current)
            updated["status"] = "released"
            released_by = str(updated.get("agent", "")).strip()
            if released_by:
                updated["released_by"] = released_by
            updated.pop("agent", None)
            updated["released_at"] = now_text
            updated["updated_at"] = now_text
            updated["stale_after_minutes"] = stale_minutes
            updated["note"] = f"Released after no heartbeat/update for at least {stale_minutes} minutes."
            task_state[task_id] = updated
            released_count += 1

        if released_count:
            save_agent_task_state(root, task_state)
        return released_count


def apply_agent_task_state(task: dict[str, object], state: dict[str, object]) -> None:
    if not state:
        return
    state_status = str(state.get("status", "")).strip()
    if state_status not in AGENT_TASK_STATE_STATUSES:
        return

    for key in (
        "agent",
        "released_by",
        "note",
        "claimed_at",
        "started_at",
        "completed_at",
        "failed_at",
        "released_at",
        "updated_at",
    ):
        if state_status == "released" and key == "agent":
            continue
        if key in state:
            task[key] = state[key]

    base_status = str(task.get("status", "todo"))
    if (
        state_status == "released"
        or base_status == "done"
        or base_status.startswith("blocked")
        or (base_status == "needs_reread" and state_status == "done")
    ):
        task["task_state_status"] = state_status
        return
    task["status"] = state_status


SOURCE_PREP_REQUIRED_PAGE_SECTIONS = [
    "Page Metadata",
    "Layout And Reading Order",
    "Literal Transcription",
    "Images, Captions, And Visual Notes",
    "Uncertain Or Illegible",
    "Completeness Audit",
]
SOURCE_PREP_REPAIR_FLAGS = {
    "placeholder_transcription",
    "image_preserved_not_transcribed",
    "text_layer_only",
    "no_transcription",
    "image_only_or_too_little_text",
    "missing_literal_transcription_section",
    "possible_ocr_garbage_token",
    "possible_table_layout_loss",
    "many_uncertain_readings",
    "encoding_mojibake",
    "missing_conversion_contract_sections",
}
SOURCE_PREP_PAGE_CACHE_VERSION = 1


def review_source_prep_page_output(output_path: Path) -> dict[str, object]:
    if not output_path.exists():
        return {"status": "todo", "quality_flags": [], "missing_sections": []}
    if output_path.is_dir():
        return {"status": "todo", "quality_flags": [], "missing_sections": []}
    try:
        text = output_path.read_text(encoding="utf-8")
    except OSError:
        return {"status": "needs_reread", "quality_flags": ["unreadable_page_output"], "missing_sections": []}

    _, base_flags = assess_conversion_page_quality(text)
    flags = list(dict.fromkeys(base_flags + detect_conversion_text_flags(text)))
    lower_text = text.lower()
    missing_sections = [
        section for section in SOURCE_PREP_REQUIRED_PAGE_SECTIONS if f"## {section.lower()}" not in lower_text
    ]
    if missing_sections:
        flags.append("missing_conversion_contract_sections")
    flags = list(dict.fromkeys(flags))
    status = "needs_reread" if SOURCE_PREP_REPAIR_FLAGS.intersection(flags) else "done"
    return {"status": status, "quality_flags": flags, "missing_sections": missing_sections}


def review_source_prep_page_output_for_cli(root: Path, output_path: Path) -> dict[str, object]:
    path = output_path if output_path.is_absolute() else root.resolve() / output_path
    review = review_source_prep_page_output(path)
    review["path"] = relative_to_root(path, root.resolve())
    return review


def source_prep_page_cache_path(root: Path) -> Path:
    return root.resolve() / "research" / "_agent-queues" / "source-prep-page-cache.json"


def load_source_prep_page_cache(root: Path) -> dict[str, object]:
    path = source_prep_page_cache_path(root)
    if not path.exists():
        return {"version": SOURCE_PREP_PAGE_CACHE_VERSION, "entries": {}}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"version": SOURCE_PREP_PAGE_CACHE_VERSION, "entries": {}}
    if not isinstance(payload, dict) or payload.get("version") != SOURCE_PREP_PAGE_CACHE_VERSION:
        return {"version": SOURCE_PREP_PAGE_CACHE_VERSION, "entries": {}}
    entries = payload.get("entries", {})
    if not isinstance(entries, dict):
        entries = {}
    return {"version": SOURCE_PREP_PAGE_CACHE_VERSION, "entries": entries}


def save_source_prep_page_cache(root: Path, cache: dict[str, object]) -> Path:
    path = source_prep_page_cache_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    entries = cache.get("entries", {})
    if not isinstance(entries, dict):
        entries = {}
    payload = {
        "version": SOURCE_PREP_PAGE_CACHE_VERSION,
        "updated": utc_timestamp(),
        "purpose": "Cached source-prep page output review keyed by page Markdown path, file size, and mtime.",
        "entries": entries,
    }
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return path


def cached_review_source_prep_page_output(
    root: Path,
    output_path: Path,
    cache: dict[str, object],
) -> tuple[dict[str, object], bool]:
    if not output_path.exists() or output_path.is_dir():
        return review_source_prep_page_output(output_path), False
    try:
        stat = output_path.stat()
    except OSError:
        return review_source_prep_page_output(output_path), False

    entries = cache.setdefault("entries", {})
    if not isinstance(entries, dict):
        cache["entries"] = {}
        entries = cache["entries"]
    cache_key = relative_to_root(output_path, root)
    existing = entries.get(cache_key)
    if isinstance(existing, dict):
        review = existing.get("review")
        if (
            existing.get("mtime_ns") == stat.st_mtime_ns
            and existing.get("size") == stat.st_size
            and isinstance(review, dict)
        ):
            return dict(review), False

    review = review_source_prep_page_output(output_path)
    entries[cache_key] = {
        "mtime_ns": stat.st_mtime_ns,
        "size": stat.st_size,
        "review": review,
    }
    return review, True


def write_agent_queues(
    root: Path,
    output_dir: Path | None = None,
    stale_minutes: int = 360,
    include_conversion_qa: bool = True,
) -> list[Path]:
    paths = WikiPaths(root.resolve())
    queue_dir = output_dir or (paths.research / "_agent-queues")
    if not queue_dir.is_absolute():
        queue_dir = paths.root / queue_dir
    queue_dir.mkdir(parents=True, exist_ok=True)

    released_count = release_stale_agent_tasks(paths.root, stale_minutes=stale_minutes)
    task_state = load_agent_task_state(paths.root)
    queues = {
        "source-prep": build_source_prep_agent_tasks(paths.root),
    }
    queues["conversion-qa"] = build_conversion_qa_agent_tasks(paths.root) if include_conversion_qa else []
    queues["evidence-extraction"] = build_evidence_extraction_agent_tasks(paths.root)
    written = [write_agent_queue(paths.root, queue_dir, name, tasks, task_state) for name, tasks in queues.items()]
    log_message = f"agent-queues | Wrote {len(written)} queue manifest(s)"
    if not include_conversion_qa:
        log_message += "; conversion QA queue disabled by source-prep settings"
    if released_count:
        log_message += f"; released {released_count} stale task(s)"
    append_log(paths.research / "log.md", log_message)
    return written


def write_agent_queue(
    root: Path,
    queue_dir: Path,
    name: str,
    tasks: list[dict[str, object]],
    task_state: dict[str, dict[str, object]] | None = None,
    purpose: str = "",
) -> Path:
    task_state = task_state or {}
    prompts_dir = queue_dir / "prompts" / name
    prompts_dir.mkdir(parents=True, exist_ok=True)
    serialized_tasks = []
    expected_prompt_names: set[str] = set()
    for task in tasks:
        task_copy = dict(task)
        prompt = str(task_copy.pop("prompt"))
        prompt_path = prompts_dir / f"{slug(str(task_copy['task_id']))}.md"
        prompt_path.write_text(prompt, encoding="utf-8")
        expected_prompt_names.add(prompt_path.name)
        task_copy["prompt_path"] = relative_to_root(prompt_path, root)
        apply_agent_task_state(task_copy, task_state.get(str(task_copy["task_id"]), {}))
        serialized_tasks.append(task_copy)
    for prompt_path in prompts_dir.glob("*.md"):
        if prompt_path.name not in expected_prompt_names:
            prompt_path.unlink()

    queue_path = queue_dir / f"{name}.json"
    payload = {
        "created": date.today().isoformat(),
        "queue": name,
        "task_count": len(serialized_tasks),
        "status_counts": count_task_statuses(serialized_tasks),
        "tasks": serialized_tasks,
    }
    if purpose.strip():
        payload["purpose"] = purpose.strip()
    queue_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return queue_path


SOURCE_PREP_BATCHABLE_STATUSES = ("needs_reread", "todo")
SOURCE_PREP_BATCH_STATUS_PRIORITY = {"needs_reread": 0, "todo": 1}
SOURCE_PREP_MAX_PAGES_PER_WORKER = 1
SOURCE_RELEVANCE_VALUES = ("low", "medium", "high", "critical")
SOURCE_RELEVANCE_PRIORITY = {value: index for index, value in enumerate(SOURCE_RELEVANCE_VALUES)}
SOURCE_RELEVANCE_TREATMENTS = ("lite", "pro", "pro_with_crops", "reread")
SOURCE_RELEVANCE_PAGE_SCOPED_VALUES = {"high", "critical"}
SOURCE_RELEVANCE_PAGE_SCOPED_TREATMENTS = {"pro", "pro_with_crops", "reread"}
SOURCE_RELEVANCE_ACTIVE_STATUSES = {"active", "open", "todo"}
RESEARCH_ANALYZER_VERSION = 4
RESEARCH_ANALYZER_UPGRADE_SCORE = 50
RESEARCH_ANALYZER_SIGNAL_SCORE = 20
RESEARCH_ANALYZER_QUESTION_SCORE = 20
RESEARCH_ANALYZER_MAX_REPORT_PAGES = 250
RESEARCH_ANALYZER_RELATIONSHIP_CUES = {
    "aunt",
    "brother",
    "child",
    "children",
    "daughter",
    "father",
    "granddaughter",
    "grandfather",
    "grandmother",
    "grandson",
    "heir",
    "hija",
    "hijo",
    "husband",
    "madre",
    "mother",
    "padre",
    "parent",
    "parents",
    "sibling",
    "sister",
    "spouse",
    "uncle",
    "wife",
}
RESEARCH_ANALYZER_LIFE_EVENT_CUES = {
    "baptism",
    "baptized",
    "birth",
    "born",
    "burial",
    "census",
    "death",
    "died",
    "emigrated",
    "immigrated",
    "marriage",
    "married",
    "naturalization",
    "obituary",
    "probate",
    "residence",
    "resident",
}
RESEARCH_ANALYZER_VISUAL_CROP_KINDS = {
    "certificate",
    "face",
    "handwriting",
    "map",
    "photo",
    "photograph",
    "portrait",
    "seal",
    "signature",
}
STORAGE_LIFECYCLE_VERSION = 1
STORAGE_LIFECYCLE_MIN_USABLE_CHARS = 200
STORAGE_LIFECYCLE_HIGH_CONFIDENCE_CHARS = 600
STORAGE_LIFECYCLE_DEACCESSION_STATUSES = {
    "deaccession_candidate",
}
STORAGE_LIFECYCLE_PRESERVE_STATUSES = {
    "preserve_raw",
}
STORAGE_LIFECYCLE_GENEALOGY_CUES = (
    RESEARCH_ANALYZER_RELATIONSHIP_CUES
    | RESEARCH_ANALYZER_LIFE_EVENT_CUES
    | {
        "ancestor",
        "baptismal",
        "cemetery",
        "christened",
        "civil register",
        "certificate",
        "family",
        "genealogy",
        "given name",
        "godfather",
        "godmother",
        "index",
        "maiden",
        "surname",
        "transcript",
        "witness",
    }
)
STORAGE_LIFECYCLE_PAGE_LEVEL_MEDIA_TYPES = {"image"}


def source_relevance_feedback_path(root: Path) -> Path:
    return root.resolve() / "research" / "_agent-queues" / "source-relevance-feedback.json"


def load_source_relevance_feedback(root: Path) -> dict[str, object]:
    path = source_relevance_feedback_path(root)
    if not path.exists():
        return {
            "created": utc_timestamp(),
            "updated": utc_timestamp(),
            "purpose": "Research-to-conversion relevance hints for source-prep model routing.",
            "hints": [],
        }
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        payload = {}
    if not isinstance(payload, dict):
        payload = {}
    hints = payload.get("hints", [])
    if not isinstance(hints, list):
        hints = []
    payload["hints"] = [hint for hint in hints if isinstance(hint, dict)]
    payload.setdefault("created", utc_timestamp())
    payload.setdefault("purpose", "Research-to-conversion relevance hints for source-prep model routing.")
    payload["updated"] = str(payload.get("updated") or utc_timestamp())
    return payload


def save_source_relevance_feedback(root: Path, payload: dict[str, object]) -> Path:
    path = source_relevance_feedback_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload["updated"] = utc_timestamp()
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return path


def source_relevance_hint_identity(hint: dict[str, object]) -> str:
    values = [
        str(hint.get("task_id", "")).strip(),
        str(hint.get("job_manifest", "")).strip(),
        str(hint.get("source_sha256", "")).strip(),
        str(hint.get("source", "")).strip(),
        str(hint.get("converted_file", "")).strip(),
        str(hint.get("page", "")).strip(),
    ]
    digest = hashlib.sha256("|".join(values).encode("utf-8")).hexdigest()[:12]
    return f"source-relevance:{digest}"


def normalize_source_relevance(value: str) -> str:
    normalized = value.strip().lower()
    if normalized not in SOURCE_RELEVANCE_VALUES:
        raise ValueError(f"unsupported source relevance: {value}")
    return normalized


def normalize_source_relevance_treatment(value: str) -> str:
    normalized = value.strip().lower().replace("-", "_")
    if normalized == "expensive":
        normalized = "pro_with_crops"
    if normalized not in SOURCE_RELEVANCE_TREATMENTS:
        raise ValueError(f"unsupported source relevance treatment: {value}")
    return normalized


def source_relevance_task_page_from_id(task_id: str) -> int:
    match = re.search(r"(?:^|[:/_-])p(?:age[-_]?)?0*(\d+)(?:$|[:/_-])", task_id, flags=re.IGNORECASE)
    if not match:
        return 0
    try:
        return int(match.group(1))
    except ValueError:
        return 0


def source_relevance_requires_page_scope(relevance: str, treatment: str) -> bool:
    return relevance in SOURCE_RELEVANCE_PAGE_SCOPED_VALUES or treatment in SOURCE_RELEVANCE_PAGE_SCOPED_TREATMENTS


def source_relevance_page_numbers_for_target(
    root: Path,
    *,
    task_id: str = "",
    job_manifest: str = "",
    source: str = "",
    source_sha256: str = "",
    converted_file: str = "",
) -> list[int]:
    root = root.resolve()
    pages: set[int] = set()
    if job_manifest.strip():
        manifest_path = Path(job_manifest.strip())
        if not manifest_path.is_absolute():
            manifest_path = root / manifest_path
        manifest = read_json_payload(manifest_path, {})
        for page in manifest.get("pages", []) if isinstance(manifest.get("pages", []), list) else []:
            if not isinstance(page, dict):
                continue
            page_number = safe_int(page.get("page"), 0)
            if page_number > 0:
                pages.add(page_number)

    if pages:
        return sorted(pages)

    probe = {
        "task_id": task_id.strip(),
        "job_manifest": job_manifest.strip(),
        "source": source.strip(),
        "source_sha256": source_sha256.strip(),
        "converted_file": converted_file.strip(),
        "page": 0,
    }
    try:
        for task in build_source_prep_agent_tasks(root):
            if source_relevance_hint_matches_task(probe, task):
                page_number = safe_int(task.get("page"), 0)
                if page_number > 0:
                    pages.add(page_number)
    except Exception:
        return []
    return sorted(pages)


def mark_source_relevance_feedback(
    root: Path,
    *,
    task_id: str = "",
    job_manifest: str = "",
    source: str = "",
    source_sha256: str = "",
    converted_file: str = "",
    page: int = 0,
    relevance: str = "high",
    treatment: str = "pro_with_crops",
    reason: str = "",
    entities: list[str] | None = None,
    terms: list[str] | None = None,
    agent: str = "",
) -> tuple[Path, dict[str, object]]:
    if page < 0:
        raise ValueError("page must be zero or positive")
    if not any(str(value).strip() for value in (task_id, job_manifest, source, source_sha256, converted_file)):
        raise ValueError("source-relevance mark requires a task id, job manifest, source path, source hash, or converted file")
    normalized_relevance = normalize_source_relevance(relevance)
    normalized_treatment = normalize_source_relevance_treatment(treatment)
    if page == 0:
        page = source_relevance_task_page_from_id(task_id)
    target_pages = [page] if page > 0 else [0]
    if page < 1 and source_relevance_requires_page_scope(normalized_relevance, normalized_treatment):
        target_pages = source_relevance_page_numbers_for_target(
            root,
            task_id=task_id,
            job_manifest=job_manifest,
            source=source,
            source_sha256=source_sha256,
            converted_file=converted_file,
        )
        if not target_pages:
            raise ValueError(
                "source-relevance mark for high/critical relevance or pro/pro_with_crops/reread treatment must become page-level orders. "
                "Pass --page N, a page-scoped --task-id such as source-prep:job:p0001, or target a prepared job/source whose pages can be enumerated."
            )
    now = utc_timestamp()

    payload = load_source_relevance_feedback(root)
    hints = payload.setdefault("hints", [])
    if not isinstance(hints, list):
        hints = []
        payload["hints"] = hints
    written_hints: list[dict[str, object]] = []
    for target_page in target_pages:
        hint: dict[str, object] = {
            "status": "active",
            "created": now,
            "updated": now,
            "task_id": task_id.strip(),
            "job_manifest": job_manifest.strip(),
            "source": source.strip(),
            "source_sha256": source_sha256.strip(),
            "converted_file": converted_file.strip(),
            "page": target_page,
            "relevance": normalized_relevance,
            "requested_treatment": normalized_treatment,
            "reason": reason.strip(),
            "entities": [entity.strip() for entity in entities or [] if entity.strip()],
            "matched_terms": [term.strip() for term in terms or [] if term.strip()],
            "agent": agent.strip(),
        }
        hint["id"] = source_relevance_hint_identity(hint)
        replaced = False
        for index, existing in enumerate(hints):
            if isinstance(existing, dict) and str(existing.get("id", "")) == str(hint["id"]):
                hint["created"] = str(existing.get("created") or now)
                hints[index] = hint
                replaced = True
                break
        if not replaced:
            hints.append(hint)
        written_hints.append(hint)
    path = save_source_relevance_feedback(root, payload)
    if len(written_hints) == 1:
        result_hint = written_hints[0]
    else:
        result_hint = {
            "id": "source-relevance:expanded-pages",
            "expanded": True,
            "page_count": len(written_hints),
            "pages": [hint["page"] for hint in written_hints],
            "hint_ids": [hint["id"] for hint in written_hints],
            "relevance": normalized_relevance,
            "requested_treatment": normalized_treatment,
        }
    append_log(
        root.resolve() / "research" / "log.md",
        f"source-relevance | Marked {len(written_hints)} page hint(s) {normalized_relevance} {normalized_treatment}",
    )
    return path, result_hint


def active_source_relevance_hints(root: Path) -> list[dict[str, object]]:
    payload = load_source_relevance_feedback(root)
    hints = payload.get("hints", [])
    if not isinstance(hints, list):
        return []
    return [
        hint
        for hint in hints
        if isinstance(hint, dict)
        and str(hint.get("status", "active")).strip().lower() in SOURCE_RELEVANCE_ACTIVE_STATUSES
    ]


def source_relevance_hint_matches_task(hint: dict[str, object], task: dict[str, object]) -> bool:
    try:
        hint_page = int(hint.get("page", 0) or 0)
    except (TypeError, ValueError):
        hint_page = 0
    try:
        task_page = int(task.get("page", 0) or 0)
    except (TypeError, ValueError):
        task_page = 0
    if hint_page:
        if not task_page or task_page != hint_page:
            return False

    comparisons = (
        ("task_id", "task_id"),
        ("job_manifest", "job_manifest"),
        ("source_sha256", "source_sha256"),
        ("source", "source"),
        ("converted_file", "converted_file"),
    )
    for hint_key, task_key in comparisons:
        hint_value = str(hint.get(hint_key, "")).strip()
        task_value = str(task.get(task_key, "")).strip()
        if hint_value and task_value and hint_value == task_value:
            return True
    return False


def apply_source_relevance_feedback(task: dict[str, object], hints: list[dict[str, object]]) -> None:
    matches = [hint for hint in hints if source_relevance_hint_matches_task(hint, task)]
    if not matches:
        return

    strongest = max(
        matches,
        key=lambda hint: SOURCE_RELEVANCE_PRIORITY.get(str(hint.get("relevance", "")).strip().lower(), -1),
    )
    relevance = str(strongest.get("relevance", "high")).strip().lower()
    treatment = normalize_source_relevance_treatment(str(strongest.get("requested_treatment", "pro_with_crops")))
    reasons = [str(hint.get("reason", "")).strip() for hint in matches if str(hint.get("reason", "")).strip()]
    entities = [
        str(entity)
        for hint in matches
        for entity in (hint.get("entities", []) if isinstance(hint.get("entities", []), list) else [])
        if str(entity).strip()
    ]
    matched_terms = [
        str(term)
        for hint in matches
        for term in (hint.get("matched_terms", []) if isinstance(hint.get("matched_terms", []), list) else [])
        if str(term).strip()
    ]

    task["research_relevance"] = relevance
    task["requested_treatment"] = treatment
    task["relevance_feedback_ids"] = [str(hint.get("id", "")) for hint in matches if str(hint.get("id", ""))]
    if reasons:
        task["research_relevance_reasons"] = list(dict.fromkeys(reasons))
    if entities:
        task["research_entities"] = list(dict.fromkeys(entities))
    if matched_terms:
        existing_terms = [str(term) for term in task.get("matched_terms", []) or []]
        task["matched_terms"] = list(dict.fromkeys(existing_terms + matched_terms))

    if str(task.get("status", "")) == "done" and (
        treatment in {"pro", "pro_with_crops", "reread"} or relevance in {"high", "critical"}
    ):
        task["status"] = "needs_reread"
        task["repair_reason"] = "research_relevance_feedback"


def research_analyzer_state_path(root: Path) -> Path:
    return root.resolve() / "research" / "_automation" / "research-analyzer-state.json"


def research_analyzer_index_path(root: Path) -> Path:
    return root.resolve() / "research" / "_indexes" / "research-analyzer.json"


def research_staging_opportunities_index_path(root: Path) -> Path:
    return root.resolve() / "research" / "_indexes" / "research-staging-opportunities.json"


def research_staging_opportunities_markdown_path(root: Path) -> Path:
    return root.resolve() / "research" / "staging-opportunities.md"


def write_research_analyzer_state(root: Path, summary: dict[str, object]) -> Path:
    path = research_analyzer_state_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    return path


def write_research_analyzer_index(root: Path, payload: dict[str, object], out: Path | None = None) -> Path:
    path = out or research_analyzer_index_path(root)
    if not path.is_absolute():
        path = root.resolve() / path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return path


def write_research_staging_opportunities(
    root: Path,
    pages: list[dict[str, object]],
    payload: dict[str, object] | None = None,
) -> tuple[Path, Path]:
    paths = WikiPaths(root.resolve())
    payload = payload or build_research_staging_opportunities_payload(paths.root, pages)
    json_path = research_staging_opportunities_index_path(paths.root)
    markdown_path = research_staging_opportunities_markdown_path(paths.root)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    markdown_path.write_text(build_research_staging_opportunities_markdown(payload), encoding="utf-8")
    append_index_reference(paths.research / "index.md", "Agent Work", "[[staging-opportunities]]")
    append_log(paths.research / "log.md", f"research-analyzer | Wrote {relative_to_root(json_path, paths.root)}")
    return json_path, markdown_path


def build_research_staging_opportunities_payload(root: Path, pages: list[dict[str, object]]) -> dict[str, object]:
    qc_blocked_by_source = load_qc_blocked_pages(root)
    task_state = load_agent_task_state(root)
    opportunities = []
    type_counts: dict[str, int] = {}
    action_counts: dict[str, int] = {}
    readiness_counts: dict[str, int] = {}
    for page in pages:
        if not isinstance(page, dict):
            continue
        recommendations = [
            recommendation
            for recommendation in page.get("staging_recommendations", [])
            if isinstance(recommendation, dict)
        ]
        if not recommendations:
            continue
        for recommendation in recommendations:
            rec_type = str(recommendation.get("type", "unknown")).strip() or "unknown"
            type_counts[rec_type] = type_counts.get(rec_type, 0) + 1
        action = str(page.get("recommended_action", "unknown")).strip() or "unknown"
        action_counts[action] = action_counts.get(action, 0) + 1
        readiness = research_staging_opportunity_readiness(page, qc_blocked_by_source, task_state)
        readiness_status = str(readiness.get("status", "unknown")).strip() or "unknown"
        readiness_counts[readiness_status] = readiness_counts.get(readiness_status, 0) + 1
        opportunities.append(
            {
                "source": str(page.get("source", "")),
                "source_sha256": str(page.get("source_sha256", "")),
                "converted_file": str(page.get("converted_file", "")),
                "chunk_manifest": str(page.get("chunk_manifest", "")),
                "page": safe_int(page.get("page"), 0),
                "score": safe_int(page.get("score"), 0),
                "recommended_action": action,
                "chunks": page.get("chunks", []),
                "reasons": page.get("reasons", []),
                "staging_recommendations": recommendations,
                "readiness": readiness,
            }
        )
    return {
        "version": RESEARCH_ANALYZER_VERSION,
        "created": utc_timestamp(),
        "purpose": (
            "Page-level research-analyzer staging opportunities. These are instructions for draft work under "
            "research/_staging/ or conversion review, not canonical genealogy facts."
        ),
        "inputs": {
            "chunks": "raw/chunks/*/manifest.json",
            "research_analyzer": relative_to_root(research_analyzer_index_path(root), root),
        },
        "summary": {
            "opportunity_page_count": len(opportunities),
            "recommendation_count": sum(type_counts.values()),
            "recommendation_type_counts": dict(sorted(type_counts.items())),
            "recommended_action_counts": dict(sorted(action_counts.items())),
            "readiness_status_counts": dict(sorted(readiness_counts.items())),
        },
        "opportunities": opportunities,
        "storage_contract": (
            "GitHub stores this JSON/Markdown opportunity map. R2 continues to hold raw originals and durable "
            "binary assets."
        ),
    }


def research_staging_opportunity_readiness(
    page: dict[str, object],
    qc_blocked_by_source: dict[str, dict[int, dict[str, object]]],
    task_state: dict[str, dict[str, object]],
) -> dict[str, object]:
    converted_file = str(page.get("converted_file", ""))
    page_number = safe_int(page.get("page"), 0)
    source_slug = slug(Path(converted_file).stem)
    qc_hold = qc_blocked_by_source.get(converted_file, {}).get(page_number)
    if qc_hold:
        return {
            "status": "blocked_needs_reread",
            "block_reason": "post_conversion_qc_hold",
            "qc_recommended_action": qc_hold.get("recommended_action", ""),
            "qc_quality_flags": qc_hold.get("quality_flags", []),
            "qc_page_queue": f"research/_conversion-review/page-queues/{source_slug}.md",
            "qc_corrections": f"research/_conversion-review/corrections/{source_slug}.md",
        }
    if converted_file and not conversion_qa_is_done(task_state, converted_file):
        return {
            "status": "blocked_pending_conversion_qa",
            "block_reason": "pending_conversion_qa",
            "conversion_qa_task_id": conversion_qa_task_id_for_converted_file(converted_file),
            "conversion_qa_triage": f"research/_conversion-review/triage/{source_slug}.md",
            "conversion_qa_page_queue": f"research/_conversion-review/page-queues/{source_slug}.md",
            "conversion_qa_corrections": f"research/_conversion-review/corrections/{source_slug}.md",
        }
    return {
        "status": "ready_for_extraction",
        "block_reason": "",
    }


def build_research_staging_opportunities_markdown(payload: dict[str, object]) -> str:
    summary = payload.get("summary", {})
    if not isinstance(summary, dict):
        summary = {}
    opportunities = payload.get("opportunities", [])
    if not isinstance(opportunities, list):
        opportunities = []
    rows = [
        "| Page | Score | Action | Readiness | Suggested Outputs | Source |",
        "| ---: | ---: | --- | --- | --- | --- |",
    ]
    for opportunity in opportunities:
        if not isinstance(opportunity, dict):
            continue
        recommendations = opportunity.get("staging_recommendations", [])
        if not isinstance(recommendations, list):
            recommendations = []
        rec_types = [
            str(recommendation.get("type", "")).strip()
            for recommendation in recommendations
            if isinstance(recommendation, dict) and str(recommendation.get("type", "")).strip()
        ]
        rows.append(
            "| "
            + " | ".join(
                [
                    markdown_table_cell(opportunity.get("page", "")),
                    markdown_table_cell(opportunity.get("score", "")),
                    markdown_table_cell(opportunity.get("recommended_action", "")),
                    markdown_table_cell(dict_value(opportunity.get("readiness", {}), "status", "unknown")),
                    markdown_table_cell(", ".join(rec_types) or "none"),
                    markdown_table_cell(opportunity.get("source", "")),
                ]
            )
            + " |"
        )
    return f"""# Research Staging Opportunities

Generated: {payload.get("created", "")}

These are analyzer recommendations for draft work. They do not promote claims or edit canonical wiki pages.

## Summary

- Opportunity pages: {dict_value(summary, "opportunity_page_count")}
- Recommendation count: {dict_value(summary, "recommendation_count")}
- Recommendation types: {format_status_counts(dict_value(summary, "recommendation_type_counts", {}))}
- Readiness: {format_status_counts(dict_value(summary, "readiness_status_counts", {}))}
- Recommended actions: {format_status_counts(dict_value(summary, "recommended_action_counts", {}))}

## Opportunities

{chr(10).join(rows)}
"""


def research_analyzer_existing_feedback_ids(root: Path) -> set[str]:
    return {
        str(hint.get("id", "")).strip()
        for hint in active_source_relevance_hints(root)
        if str(hint.get("id", "")).strip()
    }


def research_analyzer_run(
    root: Path,
    *,
    limit: int = 5,
    question_limit: int = 5,
    out: Path | None = None,
    dry_run: bool = False,
) -> dict[str, object]:
    """Scan prepared chunks for research signals, upgrade requests, and research questions."""
    paths = WikiPaths(root.resolve())
    family_terms = build_family_context_terms(paths.root)
    pages = []
    blockers: list[str] = []
    for manifest_path in sorted((paths.raw / "chunks").glob("*/manifest.json")):
        try:
            pages.extend(research_analyzer_pages_from_manifest(paths.root, manifest_path, family_terms))
        except Exception as exc:
            blockers.append(f"{relative_to_root(manifest_path, paths.root)}: {exc}")

    pages.sort(key=research_analyzer_page_sort_key)
    report_pages = pages[:RESEARCH_ANALYZER_MAX_REPORT_PAGES]
    upgrade_candidates = [
        page for page in pages if str(page.get("recommended_action", "")) == "request_page_upgrade"
    ]
    existing_feedback_ids = research_analyzer_existing_feedback_ids(paths.root)
    written_requests = []
    existing_requests = []
    for candidate in upgrade_candidates:
        if limit >= 0 and len(written_requests) >= limit:
            break
        request = research_analyzer_upgrade_request(candidate)
        request_id = source_relevance_hint_identity(request)
        if request_id in existing_feedback_ids:
            existing_requests.append(request_id)
            continue
        if not dry_run:
            _, hint = mark_source_relevance_feedback(
                paths.root,
                job_manifest=str(request.get("job_manifest", "")),
                source=str(request.get("source", "")),
                source_sha256=str(request.get("source_sha256", "")),
                converted_file=str(request.get("converted_file", "")),
                page=safe_int(request.get("page"), 0),
                relevance=str(request.get("relevance", "high")),
                treatment=str(request.get("requested_treatment", "pro")),
                reason=str(request.get("reason", "")),
                entities=[str(value) for value in candidate.get("entities", []) if str(value).strip()],
                terms=[str(value) for value in candidate.get("matched_terms", []) if str(value).strip()],
                agent="research-analyzer",
            )
            written_requests.append(str(hint.get("id", request_id)) if isinstance(hint, dict) else request_id)
            existing_feedback_ids.add(request_id)
        else:
            written_requests.append(request_id)

    question_candidates = [
        page for page in pages if safe_int(page.get("score"), 0) >= RESEARCH_ANALYZER_QUESTION_SCORE
    ]
    existing_question_ids = research_analyzer_existing_question_ids(paths.root)
    written_questions = []
    existing_questions = []
    refreshed_questions = []
    for candidate in question_candidates:
        if question_limit >= 0 and len(written_questions) >= question_limit:
            break
        question_id = research_analyzer_question_id(candidate)
        if question_id in existing_question_ids:
            existing_questions.append(question_id)
            if not dry_run:
                question_path = refresh_research_analyzer_question(paths.root, candidate, question_id)
                if question_path:
                    refreshed_questions.append(relative_to_root(question_path, paths.root))
            continue
        if not dry_run:
            question_path = write_research_analyzer_question(paths.root, candidate, question_id)
            written_questions.append(relative_to_root(question_path, paths.root))
            existing_question_ids.add(question_id)
        else:
            written_questions.append(question_id)

    question_queue_path = paths.research / "_agent-queues" / "research-questions.json"
    if not dry_run:
        write_research_question_queue(paths.root, pages)
    staging_payload = build_research_staging_opportunities_payload(paths.root, pages)
    staging_json_path = research_staging_opportunities_index_path(paths.root)
    staging_markdown_path = research_staging_opportunities_markdown_path(paths.root)
    if not dry_run:
        staging_json_path, staging_markdown_path = write_research_staging_opportunities(paths.root, pages, staging_payload)
    staging_summary = staging_payload.get("summary", {})
    if not isinstance(staging_summary, dict):
        staging_summary = {}

    index_payload = {
        "version": RESEARCH_ANALYZER_VERSION,
        "created": date.today().isoformat(),
        "purpose": (
            "Automated research-analyzer signals from converted chunks, including page-level upgrade candidates "
            "and research-question work items."
        ),
        "family_context_terms": sorted(family_terms.values()),
        "pages_scanned": len(pages),
        "upgrade_candidates": len(upgrade_candidates),
        "upgrade_requests_written": len(written_requests),
        "upgrade_requests_existing": len(existing_requests),
        "research_question_candidates": len(question_candidates),
        "research_questions_written": len(written_questions),
        "research_questions_existing": len(existing_questions),
        "research_questions_refreshed": len(refreshed_questions),
        "research_question_queue": relative_to_root(question_queue_path, paths.root),
        "staging_opportunities": relative_to_root(staging_json_path, paths.root),
        "staging_opportunity_pages": safe_int(staging_summary.get("opportunity_page_count"), 0),
        "staging_recommendation_counts": staging_summary.get("recommendation_type_counts", {}),
        "staging_readiness_counts": staging_summary.get("readiness_status_counts", {}),
        "dry_run": dry_run,
        "pages": report_pages,
    }
    index_path = write_research_analyzer_index(paths.root, index_payload, out)
    summary: dict[str, object] = {
        "version": RESEARCH_ANALYZER_VERSION,
        "created": date.today().isoformat(),
        "mode": "research-analyzer",
        "root": str(paths.root),
        "dry_run": dry_run,
        "limit": limit,
        "question_limit": question_limit,
        "pages_scanned": len(pages),
        "pages_with_signals": len([page for page in pages if safe_int(page.get("score"), 0) >= RESEARCH_ANALYZER_SIGNAL_SCORE]),
        "upgrade_candidates": len(upgrade_candidates),
        "upgrade_requests_written": len(written_requests),
        "upgrade_requests_existing": len(existing_requests),
        "research_question_candidates": len(question_candidates),
        "research_questions_written": len(written_questions),
        "research_questions_existing": len(existing_questions),
        "research_questions_refreshed": len(refreshed_questions),
        "index": relative_to_root(index_path, paths.root),
        "feedback": relative_to_root(source_relevance_feedback_path(paths.root), paths.root),
        "research_question_queue": relative_to_root(question_queue_path, paths.root),
        "staging_opportunities": relative_to_root(staging_json_path, paths.root),
        "staging_opportunity_pages": safe_int(staging_summary.get("opportunity_page_count"), 0),
        "staging_recommendation_counts": staging_summary.get("recommendation_type_counts", {}),
        "staging_readiness_counts": staging_summary.get("readiness_status_counts", {}),
        "blockers": blockers,
    }
    state_path = write_research_analyzer_state(paths.root, summary)
    summary["state"] = relative_to_root(state_path, paths.root)
    if written_requests and not dry_run:
        append_log(paths.research / "log.md", f"research-analyzer | Wrote {len(written_requests)} page upgrade request(s)")
    if written_questions and not dry_run:
        append_log(paths.research / "log.md", f"research-analyzer | Wrote {len(written_questions)} research question(s)")
    return summary


def research_analyzer_pages_from_manifest(
    root: Path,
    manifest_path: Path,
    family_terms: dict[str, str],
) -> list[dict[str, object]]:
    manifest = read_json_payload(manifest_path, {})
    chunks = manifest.get("chunks", [])
    if not isinstance(chunks, list):
        return []
    grouped: dict[int, list[dict[str, object]]] = {}
    for chunk in chunks:
        if not isinstance(chunk, dict):
            continue
        chunk_rel_path = str(chunk.get("path", "")).strip()
        chunk_path = Path(chunk_rel_path)
        if chunk_rel_path and not chunk_path.is_absolute():
            chunk_path = root / chunk_path
        chunk_text = ""
        if chunk_rel_path and chunk_path.exists():
            chunk_text = chunk_path.read_text(encoding="utf-8")
        pages = storage_lifecycle_pages_for_chunk(root, manifest, chunk, chunk_text)
        for page in pages:
            if page > 0:
                grouped.setdefault(page, []).append(chunk)

    pages = []
    for page_number, page_chunks in sorted(grouped.items()):
        chunk_texts = []
        chunk_paths = []
        for chunk in sorted(page_chunks, key=lambda item: safe_int(item.get("part"), safe_int(item.get("chunk_number"), 0))):
            chunk_rel_path = str(chunk.get("path", "")).strip()
            chunk_path = Path(chunk_rel_path)
            if not chunk_path.is_absolute():
                chunk_path = root / chunk_path
            if not chunk_path.exists():
                continue
            chunk_paths.append(relative_to_root(chunk_path, root))
            chunk_texts.append(chunk_path.read_text(encoding="utf-8"))
        if not chunk_texts:
            continue
        pages.append(
            analyze_research_chunk_page(
                root=root,
                manifest=manifest,
                manifest_path=manifest_path,
                page_number=page_number,
                chunk_paths=chunk_paths,
                page_text="\n\n".join(chunk_texts),
                family_terms=family_terms,
            )
        )
    return pages


def research_analyzer_page_from_chunk_path(path: str) -> int:
    match = re.search(r"page-0*(\d+)-chunk", path)
    if not match:
        return 0
    return safe_int(match.group(1), 0)


def analyze_research_chunk_page(
    *,
    root: Path,
    manifest: dict[str, object],
    manifest_path: Path,
    page_number: int,
    chunk_paths: list[str],
    page_text: str,
    family_terms: dict[str, str],
) -> dict[str, object]:
    matched_terms = find_family_context_matches(page_text, family_terms)
    suspicious_readings = find_suspicious_name_readings(page_text, family_terms)
    genealogy_leads = extract_research_analyzer_genealogy_leads(page_text)
    relationship_cues = research_analyzer_matched_cues(page_text, RESEARCH_ANALYZER_RELATIONSHIP_CUES)
    life_event_cues = research_analyzer_matched_cues(page_text, RESEARCH_ANALYZER_LIFE_EVENT_CUES)
    visual_kinds = research_analyzer_visual_kinds(page_text)
    uncertainty_count = research_analyzer_uncertainty_count(page_text)
    score = 0
    reasons = []

    if matched_terms:
        score += 50
        reasons.append(f"matched known family term(s): {', '.join(matched_terms[:8])}")
    if suspicious_readings:
        score += 45
        reasons.append("possible name drift near known family terms")
    if genealogy_leads:
        score += 20
        reasons.append(f"genealogy lead section names {len(genealogy_leads)} candidate(s)")
    if relationship_cues:
        score += 12
        reasons.append(f"relationship cue(s): {', '.join(relationship_cues[:8])}")
    if life_event_cues:
        score += 12
        reasons.append(f"life event cue(s): {', '.join(life_event_cues[:8])}")
    if visual_kinds:
        score += 15
        reasons.append(f"visual evidence cue(s): {', '.join(visual_kinds[:8])}")
    if uncertainty_count and (matched_terms or suspicious_readings):
        score += 10
        reasons.append(f"uncertain reading marker(s): {uncertainty_count}")

    has_family_context = bool(matched_terms or suspicious_readings)
    recommended_action = "monitor"
    if has_family_context and score >= RESEARCH_ANALYZER_UPGRADE_SCORE:
        recommended_action = "request_page_upgrade"
    elif score >= RESEARCH_ANALYZER_SIGNAL_SCORE:
        recommended_action = "record_signal"
    requested_treatment = "pro_with_crops" if visual_kinds else "pro"
    relevance = "critical" if score >= 80 and has_family_context else "high" if has_family_context else "medium"
    entities = sorted(set(matched_terms + [lead for lead in genealogy_leads if lead in matched_terms]))
    staging_recommendations = research_analyzer_staging_recommendations(
        score=score,
        matched_terms=matched_terms,
        suspicious_readings=suspicious_readings,
        genealogy_leads=genealogy_leads,
        relationship_cues=relationship_cues,
        life_event_cues=life_event_cues,
        visual_kinds=visual_kinds,
        uncertainty_count=uncertainty_count,
    )
    return {
        "converted_file": str(manifest.get("converted_file", "")),
        "chunk_manifest": relative_to_root(manifest_path, root),
        "source": str(manifest.get("source", "")),
        "source_sha256": str(manifest.get("source_sha256", "")),
        "source_manifest": str(manifest.get("source_manifest", "")),
        "page": page_number,
        "chunks": chunk_paths,
        "score": score,
        "relevance": relevance,
        "recommended_action": recommended_action,
        "requested_treatment": requested_treatment,
        "reasons": reasons,
        "matched_terms": matched_terms,
        "entities": entities,
        "genealogy_leads": genealogy_leads,
        "suspicious_readings": suspicious_readings,
        "relationship_cues": relationship_cues,
        "life_event_cues": life_event_cues,
        "visual_kinds": visual_kinds,
        "uncertainty_markers": uncertainty_count,
        "staging_recommendations": staging_recommendations,
    }


def research_analyzer_staging_recommendations(
    *,
    score: int,
    matched_terms: list[str],
    suspicious_readings: list[dict[str, str]],
    genealogy_leads: list[str],
    relationship_cues: list[str],
    life_event_cues: list[str],
    visual_kinds: list[str],
    uncertainty_count: int,
) -> list[dict[str, str]]:
    if score < RESEARCH_ANALYZER_SIGNAL_SCORE:
        return []

    recommendations = [
        {
            "type": "source_packet",
            "target": "research/_staging/source-packets",
            "reason": "Preserve page-level literal support and provenance before extracting claims.",
        }
    ]
    if matched_terms or genealogy_leads or life_event_cues:
        recommendations.append(
            {
                "type": "claim",
                "target": "research/_staging/claims",
                "reason": "Names or life-event cues may support atomic fact drafts after source review.",
            }
        )
    if relationship_cues:
        recommendations.append(
            {
                "type": "relationship",
                "target": "research/_staging/relationships",
                "reason": "Relationship language may support a relationship candidate after evidence extraction.",
            }
        )
    identity_visuals = {"face", "photo", "photograph", "portrait", "signature"}
    if suspicious_readings or (matched_terms and identity_visuals.intersection(set(visual_kinds))):
        recommendations.append(
            {
                "type": "identity",
                "target": "research/_staging/identity",
                "reason": "Name drift or identity-linked visual evidence may require same-person analysis.",
            }
        )
    if uncertainty_count and matched_terms:
        recommendations.append(
            {
                "type": "conversion_review",
                "target": "research/_conversion-review/corrections",
                "reason": "Uncertain readings near known family terms should be checked before promotion.",
            }
        )
    return recommendations


def research_analyzer_page_sort_key(page: dict[str, object]) -> tuple[int, int, str, int]:
    action_priority = 0 if str(page.get("recommended_action", "")) == "request_page_upgrade" else 1
    return (
        action_priority,
        -safe_int(page.get("score"), 0),
        str(page.get("chunk_manifest", "")),
        safe_int(page.get("page"), 0),
    )


def research_analyzer_upgrade_request(candidate: dict[str, object]) -> dict[str, object]:
    reasons = [str(value) for value in candidate.get("reasons", []) if str(value).strip()]
    return {
        "status": "active",
        "task_id": "",
        "job_manifest": str(candidate.get("source_manifest", "")),
        "source": str(candidate.get("source", "")),
        "source_sha256": str(candidate.get("source_sha256", "")),
        "converted_file": str(candidate.get("converted_file", "")),
        "page": safe_int(candidate.get("page"), 0),
        "relevance": str(candidate.get("relevance", "high")),
        "requested_treatment": str(candidate.get("requested_treatment", "pro")),
        "reason": "; ".join(reasons[:4]),
    }


def research_analyzer_questions_dir(root: Path) -> Path:
    return root.resolve() / "research" / "questions"


def research_analyzer_question_queue_path(root: Path) -> Path:
    return root.resolve() / "research" / "_agent-queues" / "research-questions.json"


def research_analyzer_question_id(candidate: dict[str, object]) -> str:
    values = [
        str(candidate.get("source_sha256", "")).strip(),
        str(candidate.get("source", "")).strip(),
        str(candidate.get("converted_file", "")).strip(),
        str(candidate.get("page", "")).strip(),
    ]
    digest = hashlib.sha256("|".join(values).encode("utf-8")).hexdigest()[:12]
    return f"RQ-{digest}-P{safe_int(candidate.get('page'), 0):04d}"


def research_analyzer_existing_question_ids(root: Path) -> set[str]:
    ids = set()
    queue = read_json_payload(research_analyzer_question_queue_path(root), {"tasks": []})
    tasks = queue.get("tasks", [])
    if isinstance(tasks, list):
        ids.update(
            str(task.get("question_id", "")).strip()
            for task in tasks
            if isinstance(task, dict) and str(task.get("question_id", "")).strip()
        )
    for path in research_analyzer_questions_dir(root).glob("*.md") if research_analyzer_questions_dir(root).exists() else []:
        text = read_text(path)
        frontmatter = parse_frontmatter(text)
        question_id = str(frontmatter.get("question_id", "")).strip()
        ids.add(question_id or path.stem)
    return ids


def research_analyzer_question_path(root: Path, question_id: str) -> Path:
    return research_analyzer_questions_dir(root) / f"{slug(question_id)}.md"


def write_research_analyzer_question(root: Path, candidate: dict[str, object], question_id: str) -> Path:
    path = research_analyzer_question_path(root, question_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(build_research_analyzer_question_markdown(candidate, question_id), encoding="utf-8")
    return path


def refresh_research_analyzer_question(root: Path, candidate: dict[str, object], question_id: str) -> Path | None:
    path = research_analyzer_question_path(root, question_id)
    if not path.exists():
        return write_research_analyzer_question(root, candidate, question_id)
    frontmatter = parse_frontmatter(read_text(path))
    if str(frontmatter.get("type", "")).strip() != "research_question":
        return None
    if str(frontmatter.get("status", "")).strip() not in {"", "todo"}:
        return None
    path.write_text(build_research_analyzer_question_markdown(candidate, question_id), encoding="utf-8")
    return path


def build_research_analyzer_question_markdown(candidate: dict[str, object], question_id: str) -> str:
    page = safe_int(candidate.get("page"), 0)
    question = research_analyzer_question_text(candidate)
    reasons = candidate.get("reasons", [])
    if not isinstance(reasons, list):
        reasons = []
    chunks = candidate.get("chunks", [])
    if not isinstance(chunks, list):
        chunks = []
    matched_terms = candidate.get("matched_terms", [])
    if not isinstance(matched_terms, list):
        matched_terms = []
    genealogy_leads = candidate.get("genealogy_leads", [])
    if not isinstance(genealogy_leads, list):
        genealogy_leads = []
    staging_lines = format_research_analyzer_staging_recommendations(candidate)
    return f"""---
type: research_question
status: todo
question_id: {yaml_string(question_id)}
source: {yaml_string(str(candidate.get("source", "")))}
source_sha256: {yaml_string(str(candidate.get("source_sha256", "")))}
converted_file: {yaml_string(str(candidate.get("converted_file", "")))}
page: {page}
analyzer_score: {safe_int(candidate.get("score"), 0)}
recommended_action: {yaml_string(str(candidate.get("recommended_action", "")))}
---

# {question_id}: Page {page} Research Question

## Question

{question}

## Source Context

- Source: `{candidate.get("source", "")}`
- Converted file: `{candidate.get("converted_file", "")}`
- Chunk manifest: `{candidate.get("chunk_manifest", "")}`
- Page: {page}
- Chunks: {", ".join(f"`{chunk}`" for chunk in chunks) or "`none`"}

## Analyzer Signals

- Score: {safe_int(candidate.get("score"), 0)}
- Recommended action: `{candidate.get("recommended_action", "")}`
- Matched family terms: {", ".join(str(value) for value in matched_terms) or "none"}
- Genealogy leads: {", ".join(str(value) for value in genealogy_leads) or "none"}
- Reasons: {", ".join(str(value) for value in reasons) or "none"}

## Suggested Staging Outputs

{staging_lines}

## Next Action

- Review the cited chunks and decide whether to create staged source packets, staged claims, relationship candidates, identity/conflict candidates, or an external archive/web search task.
- Keep any derived drafts under `research/_staging/` until proof review.
"""


def research_analyzer_question_text(candidate: dict[str, object]) -> str:
    page = safe_int(candidate.get("page"), 0)
    source = Path(str(candidate.get("source", ""))).name or "this source"
    matched_terms = [str(value) for value in candidate.get("matched_terms", []) if str(value).strip()]
    suspicious = candidate.get("suspicious_readings", [])
    genealogy_leads = [str(value) for value in candidate.get("genealogy_leads", []) if str(value).strip()]
    relationship_cues = [str(value) for value in candidate.get("relationship_cues", []) if str(value).strip()]
    life_event_cues = [str(value) for value in candidate.get("life_event_cues", []) if str(value).strip()]
    if matched_terms:
        return (
            f"What evidence on page {page} of `{source}` supports or complicates the known family term(s) "
            f"{', '.join(matched_terms[:6])}?"
        )
    if suspicious:
        return f"Does page {page} of `{source}` contain a name-drift or transcription issue that changes a family identity clue?"
    if genealogy_leads:
        return (
            f"Who are the genealogy leads named on page {page} of `{source}`, and do any connect to the family tree "
            f"or known research gaps?"
        )
    if relationship_cues or life_event_cues:
        cues = relationship_cues[:4] + life_event_cues[:4]
        return f"Do the {', '.join(cues)} cue(s) on page {page} of `{source}` support a staged claim or relationship?"
    return f"Does page {page} of `{source}` contain evidence worth staging, or can it remain a low-priority signal?"


def build_research_question_task(
    root: Path,
    candidate: dict[str, object],
    qc_hold: dict[str, object] | None = None,
) -> dict[str, object]:
    question_id = research_analyzer_question_id(candidate)
    question_path = research_analyzer_question_path(root, question_id)
    converted_file = str(candidate.get("converted_file", ""))
    source_slug = slug(Path(converted_file).stem)
    page = safe_int(candidate.get("page"), 0)
    task = {
        "task_id": f"research-question:{question_id}",
        "queue": "research-questions",
        "role": "evidence_extractor",
        "skill": "genealogy-claim-extraction",
        "status": "blocked_needs_reread" if qc_hold else "todo",
        "question_id": question_id,
        "question_path": relative_to_root(question_path, root),
        "source": str(candidate.get("source", "")),
        "source_sha256": str(candidate.get("source_sha256", "")),
        "converted_file": converted_file,
        "chunk_manifest": str(candidate.get("chunk_manifest", "")),
        "chunks": candidate.get("chunks", []),
        "page": page,
        "score": safe_int(candidate.get("score"), 0),
        "recommended_action": str(candidate.get("recommended_action", "")),
        "staging_recommendations": candidate.get("staging_recommendations", []),
        "prompt": build_research_question_task_prompt(candidate, question_id, question_path, root, qc_hold),
    }
    if qc_hold:
        task.update(
            {
                "blocked_pages": [page],
                "block_reason": "post_conversion_qc_hold",
                "qc_recommended_action": qc_hold.get("recommended_action", ""),
                "qc_quality_flags": qc_hold.get("quality_flags", []),
                "qc_page_queue": f"research/_conversion-review/page-queues/{source_slug}.md",
                "qc_corrections": f"research/_conversion-review/corrections/{source_slug}.md",
            }
        )
    return task


def build_research_question_task_prompt(
    candidate: dict[str, object],
    question_id: str,
    question_path: Path,
    root: Path,
    qc_hold: dict[str, object] | None = None,
) -> str:
    staging_lines = format_research_analyzer_staging_recommendations(candidate)
    hold_section = ""
    if qc_hold:
        hold_section = f"""

## QC Hold

This research question touches a page that is currently held by conversion QA.

- QC recommended action: `{qc_hold.get("recommended_action", "")}`
- QC quality flags: {", ".join(str(flag) for flag in qc_hold.get("quality_flags", []) or []) or "none"}

Do not extract claims or create staged evidence from this page until the reread is resolved or the page is re-queued.
""".rstrip()
    return f"""# Research Question Task

Use `$genealogy-claim-extraction` if evidence can be staged from the cited chunks.

## Assignment

- Question: `{relative_to_root(question_path, root)}`
- Source: `{candidate.get("source", "")}`
- Converted source: `{candidate.get("converted_file", "")}`
- Page: {safe_int(candidate.get("page"), 0)}
- Chunks: {", ".join(f"`{chunk}`" for chunk in candidate.get("chunks", []) if str(chunk).strip()) or "`none`"}{hold_section}

## Suggested Staging Outputs

{staging_lines}

## Done When

- The question is answered in `research/_staging/` drafts or left as a documented hold.
- Any staged draft includes source path, converted file, chunk/page reference, literal support, uncertainty notes, and promotion recommendation.
- No canonical wiki page is edited directly.
"""


def format_research_analyzer_staging_recommendations(candidate: dict[str, object]) -> str:
    recommendations = candidate.get("staging_recommendations", [])
    if not isinstance(recommendations, list) or not recommendations:
        return "- None"
    lines = []
    for recommendation in recommendations:
        if not isinstance(recommendation, dict):
            continue
        rec_type = str(recommendation.get("type", "draft")).strip() or "draft"
        target = str(recommendation.get("target", "research/_staging")).strip() or "research/_staging"
        reason = str(recommendation.get("reason", "")).strip()
        lines.append(f"- `{rec_type}` -> `{target}`: {reason}")
    return "\n".join(lines) if lines else "- None"


def write_research_question_queue(root: Path, pages: list[dict[str, object]]) -> Path:
    candidates = [
        page for page in pages if safe_int(page.get("score"), 0) >= RESEARCH_ANALYZER_QUESTION_SCORE
    ]
    qc_blocked_by_source = load_qc_blocked_pages(root)
    tasks = [
        build_research_question_task(
            root,
            page,
            qc_blocked_by_source.get(str(page.get("converted_file", "")), {}).get(safe_int(page.get("page"), 0)),
        )
        for page in candidates
    ]
    tasks.sort(
        key=lambda task: (
            -safe_int(task.get("score"), 0),
            str(task.get("source", "")),
            safe_int(task.get("page"), 0),
            str(task.get("question_id", "")),
        )
    )
    path = research_analyzer_question_queue_path(root)
    task_state = load_agent_task_state(root)
    path = write_agent_queue(
        root,
        path.parent,
        "research-questions",
        tasks,
        task_state,
        purpose="Research-analyzer questions queued for staged evidence extraction or external research follow-up.",
    )
    for task in tasks:
        question_path = root / str(task.get("question_path", ""))
        if question_path.exists():
            append_index_reference(root / "research" / "index.md", "Questions", f"[[questions/{question_path.stem}]]")
    cleanup_stale_research_analyzer_questions(
        root,
        {str(task.get("question_id", "")).strip() for task in tasks if str(task.get("question_id", "")).strip()},
    )
    return path


def cleanup_stale_research_analyzer_questions(root: Path, active_question_ids: set[str]) -> list[Path]:
    removed = []
    questions_dir = research_analyzer_questions_dir(root)
    if not questions_dir.exists():
        return removed
    for question_path in sorted(questions_dir.glob("*.md")):
        text = read_text(question_path)
        frontmatter = parse_frontmatter(text)
        if str(frontmatter.get("type", "")).strip() != "research_question":
            continue
        question_id = str(frontmatter.get("question_id", "")).strip() or question_path.stem
        if question_id in active_question_ids:
            continue
        if str(frontmatter.get("status", "")).strip() not in {"", "todo"}:
            continue
        question_path.unlink()
        remove_index_reference(root / "research" / "index.md", f"[[questions/{question_path.stem}]]")
        removed.append(question_path)
    return removed


def extract_research_analyzer_genealogy_leads(page_text: str) -> list[str]:
    section = extract_section(page_text, "Extracted Genealogy Leads")
    if not section:
        return []
    leads: list[str] = []
    for value in re.findall(r"\*\*([^*]{2,120})\*\*", section):
        cleaned = clean_research_analyzer_lead(value)
        if cleaned:
            leads.append(cleaned)
    for value in re.findall(r"(?:^|\s)-\s+([^.;\n]{2,120})", section):
        cleaned = clean_research_analyzer_lead(value)
        if cleaned:
            leads.append(cleaned)
    return sorted(set(leads))[:25]


def clean_research_analyzer_lead(value: str) -> str:
    cleaned = re.sub(r"`|\[|\]|\(|\)|\*", "", value)
    cleaned = re.sub(r"\s+", " ", cleaned).strip(" :-")
    if not cleaned or len(cleaned) < 2:
        return ""
    if cleaned.lower().startswith(("none", "no ", "not ")):
        return ""
    return cleaned


def research_analyzer_matched_cues(page_text: str, cues: set[str]) -> list[str]:
    lower_text = page_text.lower()
    return sorted(cue for cue in cues if re.search(rf"\b{re.escape(cue)}\b", lower_text))


def research_analyzer_visual_kinds(page_text: str) -> list[str]:
    kinds = {
        value.strip().lower()
        for value in re.findall(r'"kind"\s*:\s*"([^"]+)"', page_text)
        if value.strip()
    }
    return sorted(kinds & RESEARCH_ANALYZER_VISUAL_CROP_KINDS)


def research_analyzer_uncertainty_count(page_text: str) -> int:
    return page_text.count("[?]") + page_text.lower().count("[illegible]")


def storage_lifecycle_index_path(root: Path) -> Path:
    return root.resolve() / "research" / "_indexes" / "storage-lifecycle.json"


def write_storage_lifecycle_report(
    root: Path,
    output: Path | None = None,
    markdown_output: Path | None = None,
    record_dir: Path | None = None,
) -> list[Path]:
    """Write non-destructive page-level R2 retention rankings and candidate records."""
    paths = WikiPaths(root.resolve())
    page_records = build_storage_lifecycle_pages(paths.root)
    page_records.sort(key=storage_lifecycle_sort_key)

    candidate_records = []
    candidate_dir = record_dir or (paths.research / "_staging" / "deaccession")
    if not candidate_dir.is_absolute():
        candidate_dir = paths.root / candidate_dir
    for record in page_records:
        if str(record.get("retention_status", "")) in STORAGE_LIFECYCLE_DEACCESSION_STATUSES:
            candidate_path = write_storage_deaccession_record(paths.root, record, candidate_dir)
            record["deaccession_record"] = relative_to_root(candidate_path, paths.root)
            candidate_records.append(candidate_path)

    output_path = output or storage_lifecycle_index_path(paths.root)
    markdown_path = markdown_output or (paths.research / "storage-lifecycle.md")
    if not output_path.is_absolute():
        output_path = paths.root / output_path
    if not markdown_path.is_absolute():
        markdown_path = paths.root / markdown_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)

    payload = {
        "version": STORAGE_LIFECYCLE_VERSION,
        "created": utc_timestamp(),
        "purpose": (
            "Non-destructive page-level storage lifecycle ranking for R2 raw material. "
            "GitHub keeps these JSON/Markdown records; raw originals and durable binary assets remain in R2."
        ),
        "inputs": {
            "chunks": "raw/chunks/*/manifest.json",
            "source_prep_manifest": "raw/source-prep-manifest.json",
            "source_relevance_feedback": "research/_agent-queues/source-relevance-feedback.json",
            "conversion_qc_pages": "research/_conversion-review/qc-pages.json",
            "research_analyzer": "research/_indexes/research-analyzer.json",
        },
        "summary": build_storage_lifecycle_summary(page_records, candidate_records),
        "pages": page_records,
        "deaccession_records": [relative_to_root(path, paths.root) for path in candidate_records],
        "storage_contract": (
            "R2 holds raw originals and durable binary assets. GitHub holds this lifecycle index, "
            "candidate records, converted Markdown, chunks, manifests, queues, and final HTML/build files."
        ),
    }
    output_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    markdown_path.write_text(build_storage_lifecycle_markdown(payload), encoding="utf-8")
    append_index_reference(paths.research / "index.md", "Agent Work", "[[storage-lifecycle]]")
    append_log(paths.research / "log.md", f"storage-lifecycle | Wrote {relative_to_root(output_path, paths.root)}")
    return [output_path, markdown_path, *candidate_records]


def build_storage_lifecycle_pages(root: Path) -> list[dict[str, object]]:
    paths = WikiPaths(root.resolve())
    source_lookup = storage_lifecycle_source_lookup(paths.root)
    family_terms = build_family_context_terms(paths.root)
    relevance_hints = active_source_relevance_hints(paths.root)
    qc_blocked = load_qc_blocked_pages(paths.root)
    analyzer_pages = storage_lifecycle_research_analyzer_pages(paths.root)
    reference_index = storage_lifecycle_reference_index(paths.root)

    groups: dict[str, dict[str, object]] = {}
    for manifest_path in sorted((paths.raw / "chunks").glob("*/manifest.json")):
        manifest = read_json_payload(manifest_path, {})
        chunks = manifest.get("chunks", [])
        if not isinstance(chunks, list):
            continue
        source = str(manifest.get("source", "")).strip()
        source_sha256 = str(manifest.get("source_sha256", "")).strip()
        converted_file = str(manifest.get("converted_file", "")).strip()
        source_manifest = str(manifest.get("source_manifest", "")).strip()
        for chunk in chunks:
            if not isinstance(chunk, dict):
                continue
            chunk_path = str(chunk.get("path", "")).strip()
            text = storage_lifecycle_read_chunk_text(paths.root, chunk_path) if chunk_path else ""
            page_numbers = storage_lifecycle_pages_for_chunk(paths.root, manifest, chunk, text)
            for page_number in page_numbers:
                key = storage_lifecycle_page_key(source_sha256, source, page_number)
                group = groups.setdefault(
                    key,
                    {
                        "source": source,
                        "source_sha256": source_sha256,
                        "page": page_number,
                        "source_manifests": set(),
                        "converted_files": set(),
                        "chunk_manifests": set(),
                        "chunks": set(),
                        "chunk_chars": 0,
                        "texts": [],
                    },
                )
                if source_manifest:
                    cast_set(group, "source_manifests").add(source_manifest)
                if converted_file:
                    cast_set(group, "converted_files").add(converted_file)
                cast_set(group, "chunk_manifests").add(relative_to_root(manifest_path, paths.root))
                if chunk_path:
                    cast_set(group, "chunks").add(chunk_path)
                    if text:
                        group["texts"].append(text)
                        group["chunk_chars"] = safe_int(group.get("chunk_chars"), 0) + len(text)

    records = []
    for group in groups.values():
        records.append(
            build_storage_lifecycle_page_record(
                root=paths.root,
                group=group,
                source_lookup=source_lookup,
                family_terms=family_terms,
                relevance_hints=relevance_hints,
                qc_blocked=qc_blocked,
                analyzer_pages=analyzer_pages,
                reference_index=reference_index,
            )
        )
    return records


def cast_set(group: dict[str, object], key: str) -> set[str]:
    value = group.setdefault(key, set())
    return value if isinstance(value, set) else set()


def storage_lifecycle_page_key(source_sha256: str, source: str, page: int) -> str:
    identity = source_sha256 or source
    return f"{identity}|{page}"


def storage_lifecycle_read_chunk_text(root: Path, chunk_path: str) -> str:
    path = Path(chunk_path)
    if not path.is_absolute():
        path = root / path
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def storage_lifecycle_pages_for_chunk(
    root: Path,
    manifest: dict[str, object],
    chunk: dict[str, object],
    text: str,
) -> list[int]:
    text_pages = storage_lifecycle_original_pages_from_text(text)
    if text_pages:
        return text_pages

    page_start = safe_int(chunk.get("page_start"), 0)
    page_end = safe_int(chunk.get("page_end"), page_start)
    if page_start <= 0:
        page_start = research_analyzer_page_from_chunk_path(str(chunk.get("path", "")))
        page_end = page_start
    if page_start <= 0:
        return []
    if page_end < page_start:
        page_end = page_start

    manifest_pages = storage_lifecycle_source_manifest_pages(root, str(manifest.get("source_manifest", "")))
    if manifest_pages:
        if page_start == 1 and page_end == 1:
            return manifest_pages
        mapped = []
        for page in range(page_start, page_end + 1):
            index = page - 1
            if 0 <= index < len(manifest_pages):
                mapped.append(manifest_pages[index])
        if mapped:
            return sorted(set(mapped))

    return list(range(page_start, page_end + 1))


def storage_lifecycle_original_pages_from_text(text: str) -> list[int]:
    pages = {
        safe_int(value, 0)
        for value in re.findall(r"(?:\*\*)?Page number(?:\*\*)?\s*:\s*(\d+)", text, flags=re.IGNORECASE)
    }
    pages.update(
        safe_int(value, 0)
        for value in re.findall(r":p0*(\d+)\b", text, flags=re.IGNORECASE)
    )
    return sorted(page for page in pages if page > 0)


def storage_lifecycle_source_manifest_pages(root: Path, source_manifest: str) -> list[int]:
    if not source_manifest:
        return []
    path = Path(source_manifest)
    if not path.is_absolute():
        path = root / path
    manifest = read_json_payload(path, {})
    pages = manifest.get("pages", [])
    if not isinstance(pages, list):
        return []
    source_pages = []
    for page in pages:
        if not isinstance(page, dict):
            continue
        page_number = safe_int(page.get("source_page"), safe_int(page.get("page"), 0))
        if page_number > 0:
            source_pages.append(page_number)
    return sorted(set(source_pages))


def build_storage_lifecycle_page_record(
    *,
    root: Path,
    group: dict[str, object],
    source_lookup: dict[str, dict[str, object]],
    family_terms: dict[str, str],
    relevance_hints: list[dict[str, object]],
    qc_blocked: dict[str, dict[int, dict[str, object]]],
    analyzer_pages: dict[str, dict[str, object]],
    reference_index: list[dict[str, str]],
) -> dict[str, object]:
    source = str(group.get("source", "")).strip()
    source_sha256 = str(group.get("source_sha256", "")).strip()
    page = safe_int(group.get("page"), 0)
    converted_files = sorted(cast_set(group, "converted_files"))
    chunks = sorted(cast_set(group, "chunks"))
    source_manifests = sorted(cast_set(group, "source_manifests"))
    chunk_manifests = sorted(cast_set(group, "chunk_manifests"))
    text = "\n\n".join(str(value) for value in group.get("texts", []) if str(value).strip())
    source_entry = storage_lifecycle_source_entry(source_lookup, source_sha256, source)
    signals = storage_lifecycle_page_signals(
        text=text,
        page=page,
        source=source,
        source_sha256=source_sha256,
        converted_files=converted_files,
        chunks=chunks,
        family_terms=family_terms,
        relevance_hints=relevance_hints,
        qc_blocked=qc_blocked,
        analyzer_pages=analyzer_pages,
        reference_index=reference_index,
    )
    usable_conversion, conversion_blockers = storage_lifecycle_usable_conversion(text, converted_files, chunks, signals)
    locator_strength, locator_notes = storage_lifecycle_locator_strength(
        root,
        source=source,
        source_sha256=source_sha256,
        converted_files=converted_files,
        source_manifests=source_manifests,
        source_entry=source_entry,
    )
    page_storage_unit = storage_lifecycle_page_storage_unit(source_entry, source)
    relevance_score = storage_lifecycle_relevance_score(signals)
    irrelevance_confidence = storage_lifecycle_irrelevance_confidence(text, usable_conversion, signals)
    retention_status, retention_reasons, deaccession_allowed, deaccession_blockers = storage_lifecycle_retention_decision(
        usable_conversion=usable_conversion,
        conversion_blockers=conversion_blockers,
        locator_strength=locator_strength,
        page_storage_unit=page_storage_unit,
        relevance_score=relevance_score,
        irrelevance_confidence=irrelevance_confidence,
        signals=signals,
    )
    record_id_digest = hashlib.sha256(storage_lifecycle_page_key(source_sha256, source, page).encode("utf-8")).hexdigest()
    reacquisition = storage_lifecycle_reacquisition_record(source_entry, source, source_sha256, source_manifests, converted_files)
    return {
        "id": f"SL-{record_id_digest[:12]}-P{page:04d}",
        "source": source,
        "source_sha256": source_sha256,
        "page": page,
        "retention_status": retention_status,
        "retention_reasons": retention_reasons,
        "relevance_score": relevance_score,
        "irrelevance_confidence": irrelevance_confidence,
        "usable_conversion": usable_conversion,
        "conversion_blockers": conversion_blockers,
        "source_locator_strength": locator_strength,
        "source_locator_notes": locator_notes,
        "page_storage_unit": page_storage_unit,
        "deaccession_allowed": deaccession_allowed,
        "deaccession_blockers": deaccession_blockers,
        "signals": signals,
        "converted_files": converted_files,
        "chunk_manifests": chunk_manifests,
        "chunks": chunks,
        "source_manifests": source_manifests,
        "chunk_chars": safe_int(group.get("chunk_chars"), 0),
        "reacquisition": reacquisition,
    }


def storage_lifecycle_source_lookup(root: Path) -> dict[str, dict[str, object]]:
    payload = read_json_payload(root / "raw" / "source-prep-manifest.json", {"sources": []})
    sources = payload.get("sources", [])
    lookup: dict[str, dict[str, object]] = {}
    if not isinstance(sources, list):
        return lookup
    for source in sources:
        if not isinstance(source, dict):
            continue
        digest = str(source.get("sha256", "")).strip()
        raw_path = str(source.get("raw_path", "")).strip()
        if digest:
            lookup[f"sha:{digest}"] = source
        if raw_path:
            lookup[f"path:{raw_path}"] = source
    return lookup


def storage_lifecycle_source_entry(
    lookup: dict[str, dict[str, object]],
    source_sha256: str,
    source: str,
) -> dict[str, object]:
    if source_sha256 and f"sha:{source_sha256}" in lookup:
        return lookup[f"sha:{source_sha256}"]
    if source and f"path:{source}" in lookup:
        return lookup[f"path:{source}"]
    return {}


def storage_lifecycle_page_signals(
    *,
    text: str,
    page: int,
    source: str,
    source_sha256: str,
    converted_files: list[str],
    chunks: list[str],
    family_terms: dict[str, str],
    relevance_hints: list[dict[str, object]],
    qc_blocked: dict[str, dict[int, dict[str, object]]],
    analyzer_pages: dict[str, dict[str, object]],
    reference_index: list[dict[str, str]],
) -> dict[str, object]:
    matched_terms = find_family_context_matches(text, family_terms)
    suspicious_readings = find_suspicious_name_readings(text, family_terms)
    genealogy_leads = extract_research_analyzer_genealogy_leads(text)
    relationship_cues = research_analyzer_matched_cues(text, RESEARCH_ANALYZER_RELATIONSHIP_CUES)
    life_event_cues = research_analyzer_matched_cues(text, RESEARCH_ANALYZER_LIFE_EVENT_CUES)
    visual_kinds = research_analyzer_visual_kinds(text)
    uncertainty_markers = research_analyzer_uncertainty_count(text)
    generic_cues = research_analyzer_matched_cues(text, STORAGE_LIFECYCLE_GENEALOGY_CUES)
    page_hints = [
        hint
        for hint in relevance_hints
        if storage_lifecycle_hint_matches_page(hint, page, source, source_sha256, converted_files)
    ]
    qc_pages = [
        qc_blocked.get(converted_file, {}).get(page)
        for converted_file in converted_files
        if qc_blocked.get(converted_file, {}).get(page)
    ]
    analyzer_matches = [
        analyzer_pages[key]
        for key in storage_lifecycle_analyzer_keys(source_sha256, source, converted_files, page)
        if key in analyzer_pages
    ]
    cited_in = storage_lifecycle_cited_in(reference_index, source, converted_files, chunks, page)
    return {
        "family_terms": matched_terms,
        "suspicious_readings": suspicious_readings,
        "genealogy_leads": genealogy_leads,
        "relationship_cues": relationship_cues,
        "life_event_cues": life_event_cues,
        "visual_kinds": visual_kinds,
        "uncertainty_markers": uncertainty_markers,
        "generic_genealogy_cues": generic_cues,
        "relevance_hints": [
            {
                "id": hint.get("id", ""),
                "relevance": hint.get("relevance", ""),
                "requested_treatment": hint.get("requested_treatment", ""),
                "reason": hint.get("reason", ""),
            }
            for hint in page_hints
        ],
        "qc_holds": [
            {
                "recommended_action": page_payload.get("recommended_action", ""),
                "quality_flags": page_payload.get("quality_flags", []),
            }
            for page_payload in qc_pages
            if isinstance(page_payload, dict)
        ],
        "research_analyzer": [
            {
                "score": page_payload.get("score", 0),
                "recommended_action": page_payload.get("recommended_action", ""),
                "relevance": page_payload.get("relevance", ""),
            }
            for page_payload in analyzer_matches
            if isinstance(page_payload, dict)
        ],
        "cited_in": cited_in,
    }


def storage_lifecycle_hint_matches_page(
    hint: dict[str, object],
    page: int,
    source: str,
    source_sha256: str,
    converted_files: list[str],
) -> bool:
    hint_page = safe_int(hint.get("page"), 0)
    if hint_page and hint_page != page:
        return False
    if str(hint.get("source_sha256", "")).strip() and str(hint.get("source_sha256", "")).strip() == source_sha256:
        return True
    if str(hint.get("source", "")).strip() and str(hint.get("source", "")).strip() == source:
        return True
    hint_converted = str(hint.get("converted_file", "")).strip()
    return bool(hint_converted and hint_converted in converted_files)


def storage_lifecycle_research_analyzer_pages(root: Path) -> dict[str, dict[str, object]]:
    payload = read_json_payload(root / "research" / "_indexes" / "research-analyzer.json", {})
    pages = payload.get("pages", [])
    index: dict[str, dict[str, object]] = {}
    if not isinstance(pages, list):
        return index
    for page in pages:
        if not isinstance(page, dict):
            continue
        page_number = safe_int(page.get("page"), 0)
        if page_number <= 0:
            continue
        source_sha256 = str(page.get("source_sha256", "")).strip()
        source = str(page.get("source", "")).strip()
        converted_file = str(page.get("converted_file", "")).strip()
        for key in storage_lifecycle_analyzer_keys(source_sha256, source, [converted_file], page_number):
            index[key] = page
    return index


def storage_lifecycle_analyzer_keys(
    source_sha256: str,
    source: str,
    converted_files: list[str],
    page: int,
) -> list[str]:
    keys = []
    if source_sha256:
        keys.append(f"sha:{source_sha256}:p:{page}")
    if source:
        keys.append(f"source:{source}:p:{page}")
    keys.extend(f"converted:{converted_file}:p:{page}" for converted_file in converted_files if converted_file)
    return keys


def storage_lifecycle_reference_index(root: Path) -> list[dict[str, str]]:
    search_roots = [
        root / "research" / "_staging",
        root / "research" / "claims",
        root / "research" / "relationships",
        root / "research" / "source-packets",
        root / "wiki",
    ]
    references = []
    for search_root in search_roots:
        if not search_root.exists():
            continue
        for path in sorted(search_root.rglob("*.md")):
            try:
                text = path.read_text(encoding="utf-8")
            except OSError:
                continue
            references.append({"path": relative_to_root(path, root), "text": text.lower()})
    return references


def storage_lifecycle_cited_in(
    reference_index: list[dict[str, str]],
    source: str,
    converted_files: list[str],
    chunks: list[str],
    page: int,
) -> list[str]:
    targets = [source, *converted_files, *chunks]
    lowered_targets = [target.lower() for target in targets if target]
    page_markers = {
        f"page {page}",
        f"page: {page}",
        f"page_start: {page}",
        f"p{page:04d}",
    }
    cited = []
    for reference in reference_index:
        text = reference.get("text", "")
        if not any(target in text for target in lowered_targets):
            continue
        if any(chunk.lower() in text for chunk in chunks if chunk):
            cited.append(reference.get("path", ""))
            continue
        if any(marker in text for marker in page_markers):
            cited.append(reference.get("path", ""))
    return sorted(set(path for path in cited if path))


def storage_lifecycle_usable_conversion(
    text: str,
    converted_files: list[str],
    chunks: list[str],
    signals: dict[str, object],
) -> tuple[bool, list[str]]:
    blockers = []
    if not converted_files:
        blockers.append("missing_converted_file")
    if not chunks:
        blockers.append("missing_page_chunks")
    if len(text.strip()) < STORAGE_LIFECYCLE_MIN_USABLE_CHARS:
        blockers.append("short_or_empty_conversion_text")
    lower_text = text.lower()
    if "[no visible text transcribed in this batch pass.]" in lower_text:
        blockers.append("placeholder_transcription")
    if signals.get("qc_holds"):
        blockers.append("conversion_qc_hold")
    return not blockers, blockers


def storage_lifecycle_locator_strength(
    root: Path,
    *,
    source: str,
    source_sha256: str,
    converted_files: list[str],
    source_manifests: list[str],
    source_entry: dict[str, object],
) -> tuple[str, list[str]]:
    notes = []
    cloud = source_entry.get("cloud", {}) if isinstance(source_entry, dict) else {}
    cloud_key = str(cloud.get("key", "")).strip() if isinstance(cloud, dict) else ""
    local_source = root / source if source else Path()
    has_source_locator = bool(cloud_key or (source and local_source.exists()))
    if cloud_key:
        notes.append(f"cloud key: {cloud_key}")
    elif source and local_source.exists():
        notes.append(f"local source path exists: {source}")
    else:
        notes.append("no cloud key or local source path available")
    if source_sha256:
        notes.append("source SHA-256 present")
    if source_manifests:
        notes.append("conversion manifest present")
    if converted_files:
        notes.append("converted Markdown present")
    strong = bool(has_source_locator and source_sha256 and source_manifests and converted_files)
    return ("strong" if strong else "weak"), notes


def storage_lifecycle_page_storage_unit(source_entry: dict[str, object], source: str) -> str:
    media_type = str(source_entry.get("media_type", "")).strip().lower()
    if not media_type and source:
        media_type = detect_media_type(Path(source))
    if media_type in STORAGE_LIFECYCLE_PAGE_LEVEL_MEDIA_TYPES:
        return "page_level_raw_object"
    return "whole_source_object"


def storage_lifecycle_relevance_score(signals: dict[str, object]) -> int:
    score = 0
    if signals.get("family_terms"):
        score += 60
    if signals.get("suspicious_readings"):
        score += 55
    if signals.get("qc_holds"):
        score += 50
    if signals.get("cited_in"):
        score += 50
    if signals.get("visual_kinds"):
        score += 20
    if signals.get("genealogy_leads"):
        score += 20
    if signals.get("relationship_cues"):
        score += 16
    if signals.get("life_event_cues"):
        score += 16
    if safe_int(signals.get("uncertainty_markers"), 0):
        score += 10
    for hint in signals.get("relevance_hints", []) if isinstance(signals.get("relevance_hints"), list) else []:
        if not isinstance(hint, dict):
            continue
        relevance = str(hint.get("relevance", "")).strip().lower()
        score += {"critical": 80, "high": 60, "medium": 30, "low": 5}.get(relevance, 0)
    for page in signals.get("research_analyzer", []) if isinstance(signals.get("research_analyzer"), list) else []:
        if isinstance(page, dict):
            score += min(safe_int(page.get("score"), 0), 80)
    return score


def storage_lifecycle_irrelevance_confidence(
    text: str,
    usable_conversion: bool,
    signals: dict[str, object],
) -> str:
    if not usable_conversion:
        return "low"
    if storage_lifecycle_has_preserve_signal(signals):
        return "low"
    if storage_lifecycle_has_research_signal(signals):
        return "medium"
    if len(text.strip()) >= STORAGE_LIFECYCLE_HIGH_CONFIDENCE_CHARS:
        return "high"
    return "medium"


def storage_lifecycle_has_preserve_signal(signals: dict[str, object]) -> bool:
    if signals.get("family_terms") or signals.get("suspicious_readings") or signals.get("qc_holds") or signals.get("cited_in"):
        return True
    for hint in signals.get("relevance_hints", []) if isinstance(signals.get("relevance_hints"), list) else []:
        if isinstance(hint, dict) and str(hint.get("relevance", "")).strip().lower() in {"critical", "high"}:
            return True
    for page in signals.get("research_analyzer", []) if isinstance(signals.get("research_analyzer"), list) else []:
        if isinstance(page, dict) and str(page.get("recommended_action", "")).strip() == "request_page_upgrade":
            return True
    return False


def storage_lifecycle_has_research_signal(signals: dict[str, object]) -> bool:
    signal_keys = (
        "genealogy_leads",
        "relationship_cues",
        "life_event_cues",
        "visual_kinds",
        "generic_genealogy_cues",
        "relevance_hints",
        "research_analyzer",
    )
    if any(signals.get(key) for key in signal_keys):
        return True
    return safe_int(signals.get("uncertainty_markers"), 0) > 0


def storage_lifecycle_retention_decision(
    *,
    usable_conversion: bool,
    conversion_blockers: list[str],
    locator_strength: str,
    page_storage_unit: str,
    relevance_score: int,
    irrelevance_confidence: str,
    signals: dict[str, object],
) -> tuple[str, list[str], bool, list[str]]:
    reasons = []
    blockers = []
    if not usable_conversion:
        reasons.append("Raw preserved because the page does not yet have a safe usable conversion.")
        blockers.extend(conversion_blockers)
        return "preserve_raw", reasons, False, blockers
    if storage_lifecycle_has_preserve_signal(signals):
        reasons.append("Raw preserved because research/QC/citation signals make this page important or uncertain.")
        return "preserve_raw", reasons, False, blockers
    if storage_lifecycle_has_research_signal(signals) or relevance_score > 0:
        reasons.append("Cold retained because the page has generic genealogy or research signals but no direct family match yet.")
        return "cold_retain", reasons, False, blockers

    if locator_strength != "strong":
        blockers.append("weak_reacquisition_locator")
    if irrelevance_confidence != "high":
        blockers.append("irrelevance_confidence_not_high")
    if page_storage_unit != "page_level_raw_object":
        blockers.append("raw_source_is_not_page_level")
    deaccession_allowed = not blockers
    if deaccession_allowed:
        reasons.append("Page has usable conversion, strong locator, high irrelevance confidence, and page-level raw storage.")
        return "deaccession_candidate", reasons, True, []
    reasons.append("Cold retained because deaccession prerequisites are not all satisfied.")
    return "cold_retain", reasons, False, blockers


def storage_lifecycle_reacquisition_record(
    source_entry: dict[str, object],
    source: str,
    source_sha256: str,
    source_manifests: list[str],
    converted_files: list[str],
) -> dict[str, object]:
    cloud = source_entry.get("cloud", {}) if isinstance(source_entry, dict) else {}
    return {
        "raw_path": source,
        "cloud_key": str(cloud.get("key", "")).strip() if isinstance(cloud, dict) else "",
        "source_sha256": source_sha256,
        "source_manifests": source_manifests,
        "converted_files": converted_files,
        "note": "Retain these GitHub records even if page-level raw material is later removed from R2.",
    }


def build_storage_lifecycle_summary(
    page_records: list[dict[str, object]],
    candidate_records: list[Path],
) -> dict[str, object]:
    status_counts = count_task_statuses(
        [{"status": str(page.get("retention_status", "unknown"))} for page in page_records]
    )
    return {
        "page_count": len(page_records),
        "retention_status_counts": status_counts,
        "preserve_raw_count": status_counts.get("preserve_raw", 0),
        "cold_retain_count": status_counts.get("cold_retain", 0),
        "deaccession_candidate_count": status_counts.get("deaccession_candidate", 0),
        "deaccession_record_count": len(candidate_records),
    }


def storage_lifecycle_sort_key(page: dict[str, object]) -> tuple[int, str, int]:
    status_rank = {"preserve_raw": 0, "cold_retain": 1, "deaccession_candidate": 2}
    return (
        status_rank.get(str(page.get("retention_status", "")), 9),
        str(page.get("source", "")),
        safe_int(page.get("page"), 0),
    )


def write_storage_deaccession_record(root: Path, record: dict[str, object], record_dir: Path) -> Path:
    record_dir.mkdir(parents=True, exist_ok=True)
    source_slug = slug(Path(str(record.get("source", "source"))).stem or "source")
    page = safe_int(record.get("page"), 0)
    path = record_dir / f"{source_slug}-page-{page:04d}.md"
    text = build_storage_deaccession_markdown(record)
    path.write_text(text, encoding="utf-8")
    return path


def build_storage_deaccession_markdown(record: dict[str, object]) -> str:
    reacquisition = record.get("reacquisition", {})
    if not isinstance(reacquisition, dict):
        reacquisition = {}
    reasons = record.get("retention_reasons", [])
    if not isinstance(reasons, list):
        reasons = []
    blockers = record.get("deaccession_blockers", [])
    if not isinstance(blockers, list):
        blockers = []
    converted_files = record.get("converted_files", [])
    if not isinstance(converted_files, list):
        converted_files = []
    return f"""---
type: storage-deaccession-candidate
status: candidate
source: {yaml_string(str(record.get("source", "")))}
source_sha256: {yaml_string(str(record.get("source_sha256", "")))}
page: {safe_int(record.get("page"), 0)}
retention_status: {yaml_string(str(record.get("retention_status", "")))}
---

# Deaccession Candidate: {Path(str(record.get("source", "source"))).name} Page {safe_int(record.get("page"), 0)}

This is a non-destructive candidate record. No R2 object was deleted by the lifecycle ranking command.

## Decision

- Status: `{record.get("retention_status", "")}`
- Deaccession allowed: `{record.get("deaccession_allowed", False)}`
- Irrelevance confidence: `{record.get("irrelevance_confidence", "")}`
- Source locator strength: `{record.get("source_locator_strength", "")}`
- Page storage unit: `{record.get("page_storage_unit", "")}`

## Reasons

{format_markdown_bullets(reasons)}

## Blockers

{format_markdown_bullets(blockers or ["None"])}

## Reacquisition

- Raw path: `{reacquisition.get("raw_path", "")}`
- Cloud key: `{reacquisition.get("cloud_key", "")}`
- Source SHA-256: `{reacquisition.get("source_sha256", "")}`
- Conversion manifests: {", ".join(f"`{value}`" for value in reacquisition.get("source_manifests", []) if str(value).strip()) or "`none`"}
- Converted files: {", ".join(f"`{value}`" for value in converted_files if str(value).strip()) or "`none`"}
"""


def build_storage_lifecycle_markdown(payload: dict[str, object]) -> str:
    summary = payload.get("summary", {})
    pages = payload.get("pages", [])
    rows = [
        "| Source | Page | Status | Relevance | Irrelevance | Deaccession Blockers |",
        "| --- | ---: | --- | ---: | --- | --- |",
    ]
    if isinstance(pages, list):
        for page in pages[:250]:
            if not isinstance(page, dict):
                continue
            blockers = page.get("deaccession_blockers", [])
            if not isinstance(blockers, list):
                blockers = []
            rows.append(
                "| "
                + " | ".join(
                    [
                        markdown_table_cell(page.get("source", "")),
                        markdown_table_cell(page.get("page", "")),
                        markdown_table_cell(page.get("retention_status", "")),
                        markdown_table_cell(page.get("relevance_score", "")),
                        markdown_table_cell(page.get("irrelevance_confidence", "")),
                        markdown_table_cell(", ".join(str(value) for value in blockers) or "none"),
                    ]
                )
                + " |"
            )
    return f"""# Storage Lifecycle

Generated: {payload.get("created", "")}

This report is non-destructive. It ranks source pages for retention and writes candidate records only; it does not delete R2 objects.

## Summary

- Pages ranked: {dict_value(summary, "page_count")}
- Preserve raw: {dict_value(summary, "preserve_raw_count")}
- Cold retain: {dict_value(summary, "cold_retain_count")}
- Deaccession candidates: {dict_value(summary, "deaccession_candidate_count")}
- Candidate records: {dict_value(summary, "deaccession_record_count")}

## Ranked Pages

{chr(10).join(rows)}
"""


def format_markdown_bullets(values: list[object]) -> str:
    if not values:
        return "- None"
    return "\n".join(f"- {value}" for value in values)


SOURCE_PREP_DISCOVERY_VERSION = 1
SOURCE_PREP_DISCOVERY_TASK_STATUS = "rough_discovery"
SOURCE_PREP_DISCOVERY_ACCEPTED_STATUS = "rough_ok"
SOURCE_PREP_DISCOVERY_UNUSABLE_STATUS = "rough_unusable"
SOURCE_PREP_DISCOVERY_TERMINAL_STATUSES = {
    SOURCE_PREP_DISCOVERY_ACCEPTED_STATUS,
    SOURCE_PREP_DISCOVERY_UNUSABLE_STATUS,
    "error",
    "skipped",
}
SOURCE_PREP_DISCOVERY_ALLOWED_STATUSES = {"todo"}
SOURCE_PREP_DISCOVERY_MIN_TEXT_CHARS = 120
SOURCE_PREP_DISCOVERY_MIN_ALPHA_CHARS = 60
SOURCE_PREP_DISCOVERY_MIN_WORDS = 18
SOURCE_PREP_DISCOVERY_MAX_ODD_CHAR_RATIO = 0.08


def source_prep_discovery_state_path(root: Path) -> Path:
    return root.resolve() / "research" / "_agent-queues" / "source-prep-discovery.json"


def source_prep_docling_state_path(root: Path) -> Path:
    return root.resolve() / "research" / "_automation" / "source-prep-docling-state.json"


def load_source_prep_discovery_state(root: Path) -> dict[str, object]:
    path = source_prep_discovery_state_path(root)
    if not path.exists():
        return {
            "version": SOURCE_PREP_DISCOVERY_VERSION,
            "created": utc_timestamp(),
            "updated": utc_timestamp(),
            "purpose": "Rough non-evidence Docling discovery outputs used for source triage and Gemini routing.",
            "entries": {},
        }
    payload = read_json_payload(path, {})
    if payload.get("version") != SOURCE_PREP_DISCOVERY_VERSION:
        payload = {}
    entries = payload.get("entries", {}) if isinstance(payload, dict) else {}
    if not isinstance(entries, dict):
        entries = {}
    return {
        "version": SOURCE_PREP_DISCOVERY_VERSION,
        "created": str(payload.get("created") or utc_timestamp()) if isinstance(payload, dict) else utc_timestamp(),
        "updated": str(payload.get("updated") or utc_timestamp()) if isinstance(payload, dict) else utc_timestamp(),
        "purpose": "Rough non-evidence Docling discovery outputs used for source triage and Gemini routing.",
        "entries": entries,
    }


def save_source_prep_discovery_state(root: Path, payload: dict[str, object]) -> Path:
    path = source_prep_discovery_state_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    entries = payload.get("entries", {})
    if not isinstance(entries, dict):
        entries = {}
    output = {
        "version": SOURCE_PREP_DISCOVERY_VERSION,
        "created": str(payload.get("created") or utc_timestamp()),
        "updated": utc_timestamp(),
        "purpose": "Rough non-evidence Docling discovery outputs used for source triage and Gemini routing.",
        "entries": entries,
    }
    path.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
    return path


def write_source_prep_docling_state(root: Path, summary: dict[str, object]) -> Path:
    path = source_prep_docling_state_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    return path


def source_prep_discovery_key(task_id: str, source_sha256: str) -> str:
    return f"{task_id.strip()}|{source_sha256.strip()}"


def source_prep_discovery_cache_key(task: dict[str, object]) -> str:
    return source_prep_discovery_key(
        str(task.get("task_id", "")).strip(),
        str(task.get("source_sha256", "")).strip(),
    )


def source_prep_discovery_output_path(root: Path, task: dict[str, object]) -> Path:
    job_manifest = Path(str(task.get("job_manifest", "")).strip())
    job_slug = job_manifest.parent.name if job_manifest.parent.name else str(task.get("job_id", "source"))
    page_number = safe_int(task.get("page"), 1)
    return root.resolve() / "raw" / "discovery" / "docling" / slug(job_slug) / f"page-{page_number:04d}.md"


def source_prep_record_has_relevance_request(*records: dict[str, object]) -> bool:
    for record in records:
        relevance = str(record.get("research_relevance", "")).strip()
        treatment = str(record.get("requested_treatment", "")).strip()
        repair = str(record.get("repair_reason", "")).strip()
        recommended_action = str(record.get("recommended_action", "")).strip()
        if relevance or treatment or repair or recommended_action:
            return True
    return False


def source_prep_discovery_entry_for_task(
    root: Path,
    task: dict[str, object],
    entries: dict[str, object] | None = None,
) -> dict[str, object] | None:
    if entries is None:
        entries = load_source_prep_discovery_state(root).get("entries", {})
    if not isinstance(entries, dict):
        return None
    entry = entries.get(source_prep_discovery_cache_key(task))
    return entry if isinstance(entry, dict) else None


def source_prep_discovery_is_usable(root: Path, entry: dict[str, object] | None) -> bool:
    if not entry or str(entry.get("status", "")).strip() != SOURCE_PREP_DISCOVERY_ACCEPTED_STATUS:
        return False
    discovery_path = str(entry.get("discovery_path", "")).strip()
    if not discovery_path:
        return False
    return (root.resolve() / discovery_path).exists()


def apply_source_prep_discovery_state(
    root: Path,
    task: dict[str, object],
    entries: dict[str, object],
) -> None:
    entry = source_prep_discovery_entry_for_task(root, task, entries)
    if not entry:
        return
    task["rough_discovery_status"] = str(entry.get("status", "")).strip()
    if entry.get("discovery_path"):
        task["rough_discovery_path"] = str(entry.get("discovery_path", ""))
    if entry.get("readability_flags"):
        task["rough_discovery_flags"] = entry.get("readability_flags")
    if not source_prep_discovery_is_usable(root, entry):
        return
    if str(task.get("status", "")).strip() not in SOURCE_PREP_DISCOVERY_ALLOWED_STATUSES:
        return
    if source_prep_record_has_relevance_request(task):
        return
    task["status"] = SOURCE_PREP_DISCOVERY_TASK_STATUS


def source_prep_discovery_batch_skip_reason(
    root: Path,
    batch: dict[str, object],
    entries: dict[str, object],
) -> str:
    page = first_source_prep_batch_page(batch)
    if str(batch.get("status", "")).strip() != "todo":
        return ""
    if source_prep_record_has_relevance_request(batch, page):
        return ""
    task_id = source_prep_gemini_task_id(batch)
    source_sha256 = str(batch.get("source_sha256", "") or page.get("source_sha256", "")).strip()
    entry = entries.get(source_prep_discovery_key(task_id, source_sha256)) if isinstance(entries, dict) else None
    if isinstance(entry, dict) and source_prep_discovery_is_usable(root, entry):
        return "rough_docling_discovery_available"
    return ""


def profile_source_prep_discovery_markdown(markdown: str) -> dict[str, object]:
    text = re.sub(r"```.*?```", " ", markdown, flags=re.DOTALL)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", text)
    text = re.sub(r"<[^>]+>", " ", text)
    stripped = re.sub(r"\s+", " ", text).strip()
    nonspace = len(re.sub(r"\s+", "", stripped)) or 1
    alpha_chars = len(re.findall(r"[A-Za-z\u00c0-\u017f]", stripped))
    words = re.findall(r"[A-Za-z\u00c0-\u017f0-9][A-Za-z\u00c0-\u017f0-9'’-]*", stripped)
    odd_chars = len(re.findall(r"[^A-Za-z0-9\u00c0-\u017f\s.,;:!?()\[\]{}'\"/\\\-+&%$#@*=<>|’‘“”áéíóúÁÉÍÓÚñÑüÜ]", stripped))
    flags: list[str] = []
    if len(stripped) < SOURCE_PREP_DISCOVERY_MIN_TEXT_CHARS:
        flags.append("insufficient_text")
    if alpha_chars < SOURCE_PREP_DISCOVERY_MIN_ALPHA_CHARS:
        flags.append("insufficient_alpha_text")
    if len(words) < SOURCE_PREP_DISCOVERY_MIN_WORDS:
        flags.append("insufficient_words")
    if any(marker in stripped for marker in MOJIBAKE_MARKERS):
        flags.append("encoding_mojibake")
    if odd_chars / nonspace > SOURCE_PREP_DISCOVERY_MAX_ODD_CHAR_RATIO:
        flags.append("possible_ocr_garbage")
    status = SOURCE_PREP_DISCOVERY_ACCEPTED_STATUS if not flags else SOURCE_PREP_DISCOVERY_UNUSABLE_STATUS
    return {
        "status": status,
        "text_chars": len(stripped),
        "alpha_chars": alpha_chars,
        "word_count": len(words),
        "odd_char_ratio": odd_chars / nonspace,
        "readability_flags": flags,
    }


def build_source_prep_discovery_markdown(
    task: dict[str, object],
    docling_markdown: str,
    profile: dict[str, object],
) -> str:
    page_number = safe_int(task.get("page"), 1)
    fence = markdown_fence_for_text(docling_markdown)
    status = str(profile.get("status", "")).strip()
    flags = ", ".join(str(flag) for flag in profile.get("readability_flags", []) or []) or "none"
    return f"""# Rough Docling Discovery: Page {page_number}

> This is rough discovery text for browsing and triage only. It is not evidence-grade transcription and should not be cited as a source conversion.

## Discovery Metadata

- Task id: `{task.get("task_id", "")}`
- Source title: {task.get("title", "")}
- Source file: `{task.get("source", "")}`
- Source SHA-256: `{task.get("source_sha256", "")}`
- Job manifest: `{task.get("job_manifest", "")}`
- Source page: {page_number}
- Evidence-grade output target if upgraded: `{task.get("output_path", "")}`
- Discovery method: Docling rough markdown export.
- Discovery status: `{status}`
- Readability flags: {flags}
- Text characters: {profile.get("text_chars", 0)}
- Alpha characters: {profile.get("alpha_chars", 0)}
- Word count: {profile.get("word_count", 0)}

## Rough Markdown

{fence}markdown
{docling_markdown.strip()}
{fence}
"""


def source_prep_docling_input_path(root: Path, task: dict[str, object], temp_dir: Path) -> Path:
    source_path = root.resolve() / str(task.get("source", ""))
    manifest_path = root.resolve() / str(task.get("job_manifest", ""))
    manifest = read_json_payload(manifest_path, {}) if manifest_path.exists() else {}
    source_file = find_existing_source_file_for_job(root.resolve(), manifest) if manifest else None
    if source_file is None and source_path.exists():
        source_file = source_path
    if source_file is None:
        page_image = root.resolve() / str(task.get("page_image", ""))
        if page_image.exists():
            return page_image
        raise FileNotFoundError(source_path)

    media_type = str(manifest.get("media_type") or detect_media_type(source_file))
    if media_type != "pdf":
        page_image = root.resolve() / str(task.get("page_image", ""))
        return page_image if page_image.exists() else source_file

    try:
        import fitz
    except ImportError as exc:
        raise RuntimeError("PyMuPDF is required to prepare page-scoped Docling PDF inputs.") from exc

    page_number = safe_int(task.get("page"), 1)
    page_spec = find_manifest_page_spec(manifest, page_number) if manifest else {}
    source_page = safe_int(page_spec.get("source_page"), page_number)
    if source_page < 1:
        raise ValueError(f"invalid source page for {task.get('task_id', '')}: {source_page}")

    target = temp_dir / f"{slug(str(task.get('task_id', 'page')))}.pdf"
    with fitz.open(source_file) as doc:
        if source_page > len(doc):
            raise ValueError(f"source page {source_page} is outside {source_file}")
        out_doc = fitz.open()
        try:
            out_doc.insert_pdf(doc, from_page=source_page - 1, to_page=source_page - 1)
            out_doc.save(target)
        finally:
            out_doc.close()
    return target


def convert_source_with_docling(input_path: Path, *, document_timeout: float = 90.0) -> str:
    try:
        from docling.datamodel.base_models import InputFormat
        from docling.datamodel.pipeline_options import PdfPipelineOptions
        from docling.document_converter import DocumentConverter, PdfFormatOption
    except ImportError as exc:
        raise RuntimeError("Docling is required for source-prep discovery. Install with the discovery extra.") from exc

    pipeline_options = PdfPipelineOptions()
    pipeline_options.document_timeout = document_timeout
    pipeline_options.do_table_structure = False
    pipeline_options.do_picture_description = False
    pipeline_options.do_picture_classification = False
    pipeline_options.do_formula_enrichment = False
    pipeline_options.do_code_enrichment = False
    if hasattr(pipeline_options, "do_chart_extraction"):
        pipeline_options.do_chart_extraction = False

    converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options),
        }
    )
    result = converter.convert(str(input_path), max_num_pages=1)
    document = getattr(result, "document", None)
    if document is None:
        raise RuntimeError("Docling returned no document.")
    return str(document.export_to_markdown()).strip()


def source_prep_docling_discovery_run(
    root: Path,
    *,
    limit: int = 100,
    scan_limit: int = 1000,
    stale_minutes: int = 360,
    agent: str = "source-prep-docling-discovery",
    dry_run: bool = False,
) -> dict[str, object]:
    if limit < 1:
        raise ValueError("limit must be at least 1")
    if scan_limit < 1:
        raise ValueError("scan_limit must be at least 1")

    paths = WikiPaths(root.resolve())
    release_stale_agent_tasks(paths.root, stale_minutes=stale_minutes)
    task_state = load_agent_task_state(paths.root)
    discovery_state = load_source_prep_discovery_state(paths.root)
    entries = discovery_state.setdefault("entries", {})
    if not isinstance(entries, dict):
        entries = {}
        discovery_state["entries"] = entries

    tasks = [
        task
        for task in materialize_source_prep_tasks(paths.root, task_state)
        if str(task.get("status", "")).strip() in SOURCE_PREP_DISCOVERY_ALLOWED_STATUSES
        and not source_prep_record_has_relevance_request(task)
    ]
    tasks.sort(
        key=lambda task: (
            str(task.get("source", "")),
            str(task.get("job_manifest", "")),
            safe_int(task.get("page"), 0),
        )
    )

    summary: dict[str, object] = {
        "created": utc_timestamp(),
        "mode": "source-prep-docling-discovery",
        "dry_run": dry_run,
        "agent": agent,
        "limit": limit,
        "scan_limit": scan_limit,
        "inspected": 0,
        "accepted": 0,
        "unusable": 0,
        "errors": 0,
        "skipped": {},
        "tasks": [],
        "blockers": [],
    }
    changed = False

    def count_skip(reason: str) -> None:
        skipped = summary.setdefault("skipped", {})
        if isinstance(skipped, dict):
            skipped[reason] = int(skipped.get(reason, 0)) + 1

    with tempfile.TemporaryDirectory(prefix="source-prep-docling-") as tmp:
        temp_dir = Path(tmp)
        for task in tasks:
            if int(summary["accepted"]) >= limit or int(summary["inspected"]) >= scan_limit:
                break
            task_id = str(task.get("task_id", "")).strip()
            cache_key = source_prep_discovery_cache_key(task)
            cached = entries.get(cache_key)
            if isinstance(cached, dict) and str(cached.get("status", "")).strip() in SOURCE_PREP_DISCOVERY_TERMINAL_STATUSES:
                count_skip(f"cached_{cached.get('status')}")
                continue

            summary["inspected"] = int(summary["inspected"]) + 1
            task_report: dict[str, object] = {
                "task_id": task_id,
                "source": task.get("source", ""),
                "page": task.get("page", 0),
            }
            try:
                input_path = source_prep_docling_input_path(paths.root, task, temp_dir)
                docling_markdown = convert_source_with_docling(input_path)
                profile = profile_source_prep_discovery_markdown(docling_markdown)
                status = str(profile.get("status", SOURCE_PREP_DISCOVERY_UNUSABLE_STATUS))
                discovery_path = source_prep_discovery_output_path(paths.root, task)
                discovery_markdown = build_source_prep_discovery_markdown(task, docling_markdown, profile)
                task_report.update(
                    {
                        "status": status,
                        "discovery_path": relative_to_root(discovery_path, paths.root),
                        "readability_flags": profile.get("readability_flags", []),
                        "text_chars": profile.get("text_chars", 0),
                    }
                )
                if not dry_run:
                    discovery_path.parent.mkdir(parents=True, exist_ok=True)
                    discovery_path.write_text(discovery_markdown, encoding="utf-8")
                    entries[cache_key] = {
                        "status": status,
                        "updated": utc_timestamp(),
                        "agent": agent,
                        "task_id": task_id,
                        "source": str(task.get("source", "")),
                        "source_sha256": str(task.get("source_sha256", "")),
                        "job_manifest": str(task.get("job_manifest", "")),
                        "page": safe_int(task.get("page"), 0),
                        "discovery_path": relative_to_root(discovery_path, paths.root),
                        "evidence_output_path": str(task.get("output_path", "")),
                        "method": "docling",
                        "evidence_grade": False,
                        **profile,
                    }
                    changed = True
                if status == SOURCE_PREP_DISCOVERY_ACCEPTED_STATUS:
                    summary["accepted"] = int(summary["accepted"]) + 1
                else:
                    summary["unusable"] = int(summary["unusable"]) + 1
            except RuntimeError as exc:
                if "Docling is required" in str(exc):
                    summary["blockers"] = [str(exc)]
                    task_report["status"] = "blocked"
                    task_report["error"] = str(exc)
                    cast_tasks = summary.setdefault("tasks", [])
                    if isinstance(cast_tasks, list):
                        cast_tasks.append(task_report)
                    break
                summary["errors"] = int(summary["errors"]) + 1
                task_report["status"] = "error"
                task_report["error"] = str(exc)
                if not dry_run:
                    entries[cache_key] = {
                        "status": "error",
                        "updated": utc_timestamp(),
                        "agent": agent,
                        "task_id": task_id,
                        "source": str(task.get("source", "")),
                        "source_sha256": str(task.get("source_sha256", "")),
                        "job_manifest": str(task.get("job_manifest", "")),
                        "page": safe_int(task.get("page"), 0),
                        "error": str(exc)[:500],
                        "evidence_grade": False,
                    }
                    changed = True
            except Exception as exc:
                summary["errors"] = int(summary["errors"]) + 1
                task_report["status"] = "error"
                task_report["error"] = str(exc)
                if not dry_run:
                    entries[cache_key] = {
                        "status": "error",
                        "updated": utc_timestamp(),
                        "agent": agent,
                        "task_id": task_id,
                        "source": str(task.get("source", "")),
                        "source_sha256": str(task.get("source_sha256", "")),
                        "job_manifest": str(task.get("job_manifest", "")),
                        "page": safe_int(task.get("page"), 0),
                        "error": str(exc)[:500],
                        "evidence_grade": False,
                    }
                    changed = True

            cast_tasks = summary.setdefault("tasks", [])
            if isinstance(cast_tasks, list):
                cast_tasks.append(task_report)

    if changed and not dry_run:
        discovery_path = save_source_prep_discovery_state(paths.root, discovery_state)
        summary["discovery_state_path"] = relative_to_root(discovery_path, paths.root)
    summary["finished"] = utc_timestamp()
    state_path = write_source_prep_docling_state(paths.root, summary)
    summary["state_path"] = relative_to_root(state_path, paths.root)
    append_log(
        paths.research / "log.md",
        "source-prep-docling-discovery | "
        f"inspected {summary['inspected']}, accepted {summary['accepted']}, unusable {summary['unusable']}, "
        f"errors={summary['errors']}, dry_run={dry_run}",
    )
    return summary


def write_source_prep_batches(
    root: Path,
    output_dir: Path | None = None,
    max_pages: int = SOURCE_PREP_MAX_PAGES_PER_WORKER,
    limit: int = 50,
    stale_minutes: int = 360,
    statuses: list[str] | None = None,
) -> Path:
    paths = WikiPaths(root.resolve())
    queue_dir = output_dir or (paths.research / "_agent-queues")
    if not queue_dir.is_absolute():
        queue_dir = paths.root / queue_dir
    queue_dir.mkdir(parents=True, exist_ok=True)

    released_count = release_stale_agent_tasks(paths.root, stale_minutes=stale_minutes)
    task_state = load_agent_task_state(paths.root)
    source_tasks = materialize_source_prep_tasks(paths.root, task_state)
    effective_max_pages = min(max_pages, SOURCE_PREP_MAX_PAGES_PER_WORKER)
    batches = build_source_prep_batch_agent_tasks(
        source_tasks,
        max_pages=effective_max_pages,
        limit=limit,
        statuses=statuses,
    )
    queue_path = write_agent_queue(paths.root, queue_dir, "source-prep-batches", batches, {})
    log_message = (
        "source-prep-batches | "
        f"Wrote {len(batches)} batch task(s), max {effective_max_pages} page(s) each"
    )
    if released_count:
        log_message += f"; released {released_count} stale task(s)"
    append_log(paths.research / "log.md", log_message)
    return queue_path


SOURCE_PREP_FASTLANE_CACHE_VERSION = 1
SOURCE_PREP_FASTLANE_MIN_TEXT_CHARS = 300
SOURCE_PREP_FASTLANE_MAX_FULL_PAGE_IMAGE_RATIO = 0.55
SOURCE_PREP_FASTLANE_MAX_TABLE_LINE_RATIO = 0.35
SOURCE_PREP_FASTLANE_ALLOWED_STATUSES = {"needs_reread", "todo"}
SOURCE_PREP_FASTLANE_SKIP_CACHEABLE_REASONS = {
    "not_pdf",
    "pdf_open_failed",
    "page_out_of_range",
    "insufficient_native_text",
    "full_page_image_scan",
    "no_native_text_blocks",
    "possible_encoding_damage",
    "possible_ocr_garbage",
    "table_like_layout",
    "possible_ligature_text_loss",
}


def source_prep_fastlane_cache_path(root: Path) -> Path:
    return root.resolve() / "research" / "_agent-queues" / "source-prep-fastlane-cache.json"


def load_source_prep_fastlane_cache(root: Path) -> dict[str, object]:
    path = source_prep_fastlane_cache_path(root)
    if not path.exists():
        return {"version": SOURCE_PREP_FASTLANE_CACHE_VERSION, "entries": {}}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"version": SOURCE_PREP_FASTLANE_CACHE_VERSION, "entries": {}}
    if not isinstance(payload, dict) or payload.get("version") != SOURCE_PREP_FASTLANE_CACHE_VERSION:
        return {"version": SOURCE_PREP_FASTLANE_CACHE_VERSION, "entries": {}}
    entries = payload.get("entries", {})
    if not isinstance(entries, dict):
        entries = {}
    return {"version": SOURCE_PREP_FASTLANE_CACHE_VERSION, "entries": entries}


def save_source_prep_fastlane_cache(root: Path, cache: dict[str, object]) -> Path:
    path = source_prep_fastlane_cache_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    entries = cache.get("entries", {})
    if not isinstance(entries, dict):
        entries = {}
    payload = {
        "version": SOURCE_PREP_FASTLANE_CACHE_VERSION,
        "updated": utc_timestamp(),
        "purpose": "Cached deterministic source-prep fast-lane page decisions.",
        "entries": entries,
    }
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return path


def source_prep_fastlane_cache_key(task: dict[str, object]) -> str:
    task_id = str(task.get("task_id", "")).strip()
    digest = str(task.get("source_sha256", "")).strip()
    return f"{task_id}|{digest}"


def profile_source_prep_fastlane_pdf_page(page: object) -> dict[str, object]:
    text = str(page.get_text("text") or "")
    try:
        page_dict = page.get_text("dict")
    except Exception:
        page_dict = {}
    blocks = page_dict.get("blocks", []) if isinstance(page_dict, dict) else []
    page_rect = page.rect
    page_area = max(float(page_rect.width) * float(page_rect.height), 1.0)
    image_blocks: list[dict[str, object]] = []
    text_block_count = 0
    for block in blocks if isinstance(blocks, list) else []:
        if not isinstance(block, dict):
            continue
        block_type = block.get("type")
        bbox = block.get("bbox")
        if not isinstance(bbox, (list, tuple)) or len(bbox) != 4:
            continue
        x0, y0, x1, y1 = [float(value) for value in bbox]
        area_ratio = max(0.0, (x1 - x0) * (y1 - y0)) / page_area
        if block_type == 0:
            text_block_count += 1
        elif block_type == 1:
            image_blocks.append(
                {
                    "bbox": [x0, y0, x1, y1],
                    "area_ratio": area_ratio,
                }
            )

    nonspace = len(re.sub(r"\s+", "", text)) or 1
    alpha_chars = len(re.findall(r"[A-Za-z\u00c0-\u017f]", text))
    odd_chars = len(re.findall(r"[^A-Za-z0-9\u00c0-\u017f\s.,;:!?()\[\]{}'\"/\\\-+&%$#@*=<>|]", text))
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    table_like_lines = [line for line in lines if re.search(r"\S\s{4,}\S", line)]
    lower_text = text.lower()
    ligature_dropouts = re.findall(r"\b(?:ilm|ilms|irst|inal|igure|igures|ield|ields|ile|iles)\b", lower_text)
    long_alpha_tokens = re.findall(r"\b[A-Za-z]{26,}\b", text)
    largest_image_ratio = max((float(block["area_ratio"]) for block in image_blocks), default=0.0)
    flags: list[str] = []
    if len(text.strip()) < SOURCE_PREP_FASTLANE_MIN_TEXT_CHARS or alpha_chars < 120:
        flags.append("insufficient_native_text")
    if text_block_count < 1:
        flags.append("no_native_text_blocks")
    if largest_image_ratio >= SOURCE_PREP_FASTLANE_MAX_FULL_PAGE_IMAGE_RATIO:
        flags.append("full_page_image_scan")
    if any(marker in text for marker in MOJIBAKE_MARKERS):
        flags.append("possible_encoding_damage")
    if odd_chars / nonspace > 0.025 or len(long_alpha_tokens) >= 2:
        flags.append("possible_ocr_garbage")
    if lines and len(table_like_lines) / len(lines) > SOURCE_PREP_FASTLANE_MAX_TABLE_LINE_RATIO:
        flags.append("table_like_layout")
    if len(ligature_dropouts) >= 3:
        flags.append("possible_ligature_text_loss")

    return {
        "eligible": not flags,
        "flags": flags,
        "text": text.strip(),
        "text_chars": len(text.strip()),
        "alpha_chars": alpha_chars,
        "text_block_count": text_block_count,
        "image_blocks": image_blocks,
        "largest_image_ratio": largest_image_ratio,
        "table_like_line_count": len(table_like_lines),
        "line_count": len(lines),
    }


def markdown_fence_for_text(text: str) -> str:
    fence = "```"
    while fence in text:
        fence += "`"
    return fence


def source_prep_fastlane_image_references(
    root: Path,
    task: dict[str, object],
    profile: dict[str, object],
) -> list[dict[str, object]]:
    page_number = int(task.get("page", 0) or 0)
    output_path = root / str(task.get("output_path", ""))
    image_output_dir = root / str(task.get("image_output_dir", ""))
    page_image = root / str(task.get("page_image", ""))
    page_suffix = page_image.suffix.lower() if page_image.suffix else ".jpg"
    refs: list[dict[str, object]] = [
        {
            "kind": "full_page",
            "description": "Full-page audit image",
            "path": image_output_dir / f"page-{page_number:04d}-image-01-full-page-audit{page_suffix}",
            "source": page_image,
        }
    ]
    for index, block in enumerate(profile.get("image_blocks", []) or [], start=2):
        if not isinstance(block, dict):
            continue
        area_ratio = float(block.get("area_ratio", 0.0) or 0.0)
        if area_ratio < 0.01 or area_ratio >= SOURCE_PREP_FASTLANE_MAX_FULL_PAGE_IMAGE_RATIO:
            continue
        refs.append(
            {
                "kind": "pdf_image_block",
                "description": f"Native image block {index - 1}",
                "path": image_output_dir / f"page-{page_number:04d}-image-{index:02d}-native-image-block.png",
                "bbox": block.get("bbox", []),
            }
        )
        if len(refs) >= 13:
            break

    for ref in refs:
        ref["markdown_path"] = relative_path(output_path.parent, Path(ref["path"]))
    return refs


def write_source_prep_fastlane_images(
    root: Path,
    task: dict[str, object],
    image_refs: list[dict[str, object]],
) -> None:
    try:
        from PIL import Image
    except ImportError as exc:
        raise RuntimeError("Pillow is required for source-prep fast-lane image extraction.") from exc

    image_output_dir = root / str(task.get("image_output_dir", ""))
    page_image = root / str(task.get("page_image", ""))
    image_output_dir.mkdir(parents=True, exist_ok=True)
    if not page_image.exists():
        raise FileNotFoundError(page_image)

    for ref in image_refs:
        target = Path(str(ref["path"]))
        target.parent.mkdir(parents=True, exist_ok=True)
        if ref.get("kind") == "full_page":
            shutil.copy2(page_image, target)
            continue

        bbox = ref.get("bbox")
        if not isinstance(bbox, (list, tuple)) or len(bbox) != 4:
            continue
        with Image.open(page_image) as image:
            page_width = float(task.get("width_px") or image.width)
            page_height = float(task.get("height_px") or image.height)
            # The rendered page image was generated from PDF page coordinates at a fixed scale.
            # Use the image dimensions as the final authority so crops stay aligned after rerenders.
            source_pdf_width = float(ref.get("pdf_width") or 0.0)
            source_pdf_height = float(ref.get("pdf_height") or 0.0)
            if not source_pdf_width or not source_pdf_height:
                source_pdf_width = max(float(max(bbox[0], bbox[2])), 1.0)
                source_pdf_height = max(float(max(bbox[1], bbox[3])), 1.0)
            scale_x = page_width / source_pdf_width
            scale_y = page_height / source_pdf_height
            x0 = max(0, int(float(bbox[0]) * scale_x) - 8)
            y0 = max(0, int(float(bbox[1]) * scale_y) - 8)
            x1 = min(image.width, int(float(bbox[2]) * scale_x) + 8)
            y1 = min(image.height, int(float(bbox[3]) * scale_y) + 8)
            if x1 <= x0 or y1 <= y0:
                continue
            image.crop((x0, y0, x1, y1)).save(target)


def build_source_prep_fastlane_markdown(
    root: Path,
    task: dict[str, object],
    profile: dict[str, object],
    image_refs: list[dict[str, object]],
) -> str:
    page_number = int(task.get("page", 0) or 0)
    text = str(profile.get("text", "")).strip()
    fence = markdown_fence_for_text(text)
    image_lines = []
    for ref in image_refs:
        image_lines.append(f"- {ref['description']}: ![{ref['description']}]({ref['markdown_path']})")
    if not image_lines:
        image_lines.append("- Full-page audit image could not be generated; page was not completed by the fast lane.")

    return f"""# Page {page_number}

## Page Metadata

- Source title: {task.get("title", "")}
- Source file: `{task.get("source", "")}`
- Source SHA-256: `{task.get("source_sha256", "")}`
- Job manifest: `{task.get("job_manifest", "")}`
- Source page: {page_number}
- Rendered page image: `{task.get("page_image", "")}`
- Conversion method: deterministic PDF-native fast lane for born-digital/vector text pages only.

## Layout And Reading Order

The page was accepted for the fast lane because the PDF exposes native text blocks, the largest raster image block covers {float(profile.get("largest_image_ratio", 0.0) or 0.0):.1%} of the page, and the extraction profile did not show scan, table-loss, encoding, or garbage-token warning signs. Text is preserved in PDF block order.

## Literal Transcription

{fence}text
{text}
{fence}

## Images, Captions, And Visual Notes

{chr(10).join(image_lines)}

No portrait, handwriting-only region, full-page scan layer, or damaged raster document image was accepted by this fast lane. Pages with those traits remain queued for visual Codex conversion.

## Uncertain Or Illegible

No uncertain readings were flagged by the deterministic safety profile. If downstream research finds a family-name conflict or a suspicious reading, queue this exact page for targeted visual reread.

## Completeness Audit

- Native text characters captured: {profile.get("text_chars", 0)}
- Native text blocks detected: {profile.get("text_block_count", 0)}
- Non-full-page image regions referenced: {max(len(image_refs) - 1, 0)}
- Full-page audit image referenced: yes
- Safety gate: skipped for any full-page scan, damaged text, table-heavy layout, or suspected OCR garbage.
- Completion gate: this Markdown must pass `review_source_prep_page_output` before the task is marked done.
"""


def source_prep_fastlane_run(
    root: Path,
    limit: int = 100,
    scan_limit: int = 1000,
    agent: str = "source-prep-fastlane",
    stale_minutes: int = 360,
    dry_run: bool = False,
) -> dict[str, object]:
    if limit < 1:
        raise ValueError("limit must be at least 1")
    if scan_limit < 1:
        raise ValueError("scan_limit must be at least 1")

    paths = WikiPaths(root.resolve())
    release_stale_agent_tasks(paths.root, stale_minutes=stale_minutes)
    task_state = load_agent_task_state(paths.root)
    tasks = [
        task
        for task in materialize_source_prep_tasks(paths.root, task_state)
        if str(task.get("status", "")).strip() in SOURCE_PREP_FASTLANE_ALLOWED_STATUSES
    ]
    tasks.sort(
        key=lambda task: (
            0 if str(task.get("status", "")) == "needs_reread" else 1,
            str(task.get("source", "")),
            int(task.get("page", 0) or 0),
        )
    )

    try:
        import fitz
    except ImportError:
        return {
            "inspected": 0,
            "converted": 0,
            "dry_run": dry_run,
            "skipped": {"pymupdf_missing": len(tasks)},
            "converted_tasks": [],
            "failed_tasks": [],
        }

    cache = load_source_prep_fastlane_cache(paths.root)
    entries = cache.setdefault("entries", {})
    if not isinstance(entries, dict):
        entries = {}
        cache["entries"] = entries
    docs: dict[str, object] = {}
    inspected = 0
    converted = 0
    skipped: dict[str, int] = {}
    converted_tasks: list[str] = []
    failed_tasks: list[dict[str, str]] = []
    cache_changed = False

    def count_skip(reason: str) -> None:
        skipped[reason] = skipped.get(reason, 0) + 1

    try:
        for task in tasks:
            if converted >= limit or inspected >= scan_limit:
                break
            task_id = str(task.get("task_id", "")).strip()
            cache_key = source_prep_fastlane_cache_key(task)
            cached = entries.get(cache_key)
            if isinstance(cached, dict) and cached.get("decision") == "skip":
                reason = str(cached.get("reason", "cached_skip"))
                count_skip(f"cached_{reason}")
                continue

            inspected += 1
            source_path = paths.root / str(task.get("source", ""))
            if source_path.suffix.lower() != ".pdf":
                count_skip("not_pdf")
                entries[cache_key] = {"decision": "skip", "reason": "not_pdf", "updated": utc_timestamp()}
                cache_changed = True
                continue

            try:
                doc = docs.get(str(source_path))
                if doc is None:
                    doc = fitz.open(source_path)
                    docs[str(source_path)] = doc
            except Exception as exc:
                reason = "pdf_open_failed"
                count_skip(reason)
                entries[cache_key] = {
                    "decision": "skip",
                    "reason": reason,
                    "error": str(exc),
                    "updated": utc_timestamp(),
                }
                cache_changed = True
                continue

            page_number = int(task.get("page", 0) or 0)
            if page_number < 1 or page_number > len(doc):
                reason = "page_out_of_range"
                count_skip(reason)
                entries[cache_key] = {"decision": "skip", "reason": reason, "updated": utc_timestamp()}
                cache_changed = True
                continue

            page = doc[page_number - 1]
            profile = profile_source_prep_fastlane_pdf_page(page)
            profile["pdf_width"] = float(page.rect.width)
            profile["pdf_height"] = float(page.rect.height)
            for ref_block in profile.get("image_blocks", []) or []:
                if isinstance(ref_block, dict):
                    ref_block["pdf_width"] = profile["pdf_width"]
                    ref_block["pdf_height"] = profile["pdf_height"]
            if not bool(profile.get("eligible")):
                profile_flags = [str(flag) for flag in profile.get("flags", []) or []]
                reason = next(
                    (
                        flag
                        for flag in (
                            "full_page_image_scan",
                            "no_native_text_blocks",
                            "insufficient_native_text",
                            "table_like_layout",
                            "possible_encoding_damage",
                            "possible_ocr_garbage",
                            "possible_ligature_text_loss",
                        )
                        if flag in profile_flags
                    ),
                    profile_flags[0] if profile_flags else "not_eligible",
                )
                count_skip(reason)
                if reason in SOURCE_PREP_FASTLANE_SKIP_CACHEABLE_REASONS:
                    entries[cache_key] = {
                        "decision": "skip",
                        "reason": reason,
                        "flags": profile_flags,
                        "updated": utc_timestamp(),
                    }
                    cache_changed = True
                continue

            image_refs = source_prep_fastlane_image_references(paths.root, task, profile)
            for ref in image_refs:
                for key in ("pdf_width", "pdf_height"):
                    ref[key] = profile.get(key)
            markdown = build_source_prep_fastlane_markdown(paths.root, task, profile, image_refs)
            output_path = paths.root / str(task.get("output_path", ""))
            tmp_review_path = output_path.with_suffix(output_path.suffix + ".fastlane-review.tmp")
            tmp_review_path.parent.mkdir(parents=True, exist_ok=True)
            tmp_review_path.write_text(markdown, encoding="utf-8")
            review = review_source_prep_page_output(tmp_review_path)
            try:
                tmp_review_path.unlink()
            except OSError:
                pass
            if str(review.get("status", "")) != "done":
                failed_tasks.append(
                    {
                        "task_id": task_id,
                        "reason": "generated_markdown_failed_review",
                        "flags": ",".join(str(flag) for flag in review.get("quality_flags", []) or []),
                    }
                )
                continue

            if dry_run:
                converted += 1
                converted_tasks.append(task_id)
                continue

            try:
                update_agent_task_state(paths.root, task_id, "claimed", agent=agent, note="deterministic PDF-native fast lane")
                update_agent_task_state(paths.root, task_id, "in_progress", agent=agent, note="writing fast-lane page output")
                write_source_prep_fastlane_images(paths.root, task, image_refs)
                output_path.parent.mkdir(parents=True, exist_ok=True)
                output_path.write_text(markdown, encoding="utf-8")
                final_review = review_source_prep_page_output(output_path)
                missing_images = [str(ref["path"]) for ref in image_refs if not Path(str(ref["path"])).exists()]
                if str(final_review.get("status", "")) != "done" or missing_images:
                    failed_tasks.append(
                        {
                            "task_id": task_id,
                            "reason": "final_review_failed",
                            "flags": ",".join(str(flag) for flag in final_review.get("quality_flags", []) or []),
                        }
                    )
                    update_agent_task_state(
                        paths.root,
                        task_id,
                        "released",
                        agent=agent,
                        note="fast-lane output failed final quality gate; released for visual conversion",
                    )
                    continue
                update_agent_task_state(
                    paths.root,
                    task_id,
                    "done",
                    agent=agent,
                    note="completed by deterministic PDF-native fast lane",
                )
            except Exception as exc:
                failed_tasks.append({"task_id": task_id, "reason": str(exc)})
                update_agent_task_state(
                    paths.root,
                    task_id,
                    "released",
                    agent=agent,
                    note=f"fast-lane error; released for visual conversion: {exc}",
                )
                continue

            converted += 1
            converted_tasks.append(task_id)
            entries[cache_key] = {
                "decision": "converted",
                "updated": utc_timestamp(),
                "text_chars": profile.get("text_chars", 0),
            }
            cache_changed = True
    finally:
        for doc in docs.values():
            try:
                doc.close()
            except Exception:
                pass
        if cache_changed:
            save_source_prep_fastlane_cache(paths.root, cache)

    append_log(
        paths.research / "log.md",
        "source-prep-fastlane | "
        f"inspected {inspected}, converted {converted}, dry_run={dry_run}, skipped={skipped}, failed={len(failed_tasks)}",
    )
    return {
        "inspected": inspected,
        "converted": converted,
        "dry_run": dry_run,
        "skipped": skipped,
        "converted_tasks": converted_tasks,
        "failed_tasks": failed_tasks,
    }


GEMINI_SOURCE_PREP_LITE_MODEL = "gemini-2.5-flash-lite"
GEMINI_SOURCE_PREP_PRO_MODEL = "gemini-2.5-pro"
GEMINI_SOURCE_PREP_BATCHABLE_STATUSES = {"needs_reread", "todo"}
GEMINI_SOURCE_PREP_RELEVANT_VALUES = {"high", "critical"}
GEMINI_SOURCE_PREP_COMPLEX_FLAG_TOKENS = (
    "handwrit",
    "table",
    "layout_loss",
    "illegible",
    "uncertain",
    "ocr_garbage",
    "mojibake",
    "encoding",
    "image_only",
    "image_preserved",
    "scan",
    "stamp",
    "seal",
    "signature",
    "marginal",
    "column",
)
GEMINI_SOURCE_PREP_COMPLEX_TEXT_TOKENS = (
    "passenger list",
    "passenger and crew",
    "registro de nacimientos",
    "civil register",
    "birth register",
    "manifest",
    "census",
    "schedule",
    "index card",
    "ficha",
)
GEMINI_SOURCE_PREP_IMAGE_SIZE_COMPLEX_BYTES = 4 * 1024 * 1024


def first_source_prep_batch_page(batch: dict[str, object]) -> dict[str, object]:
    pages = batch.get("pages", [])
    if isinstance(pages, list) and pages and isinstance(pages[0], dict):
        return pages[0]
    return {}


def source_prep_gemini_task_id(batch: dict[str, object]) -> str:
    task_ids = batch.get("task_ids", [])
    if isinstance(task_ids, list) and task_ids:
        return str(task_ids[0])
    return str(batch.get("task_id", ""))


def source_prep_gemini_combined_values(batch: dict[str, object], keys: tuple[str, ...]) -> list[str]:
    page = first_source_prep_batch_page(batch)
    values: list[str] = []
    for source in (batch, page):
        for key in keys:
            value = source.get(key)
            if isinstance(value, list):
                values.extend(str(item) for item in value if str(item).strip())
            elif value:
                values.append(str(value))
    return list(dict.fromkeys(values))


def source_prep_gemini_pdf_profile(root: Path, batch: dict[str, object]) -> dict[str, object]:
    source_path = root.resolve() / str(batch.get("source", ""))
    if source_path.suffix.lower() != ".pdf" or not source_path.exists():
        return {}
    try:
        import fitz
    except ImportError:
        return {}

    page_number = int(batch.get("first_page", 0) or 0)
    if page_number < 1:
        return {}
    try:
        with fitz.open(source_path) as doc:
            if page_number > len(doc):
                return {}
            return profile_source_prep_fastlane_pdf_page(doc[page_number - 1])
    except Exception:
        return {}


def classify_gemini_source_prep_batch(
    root: Path,
    batch: dict[str, object],
    *,
    lite_model: str = GEMINI_SOURCE_PREP_LITE_MODEL,
    pro_model: str = GEMINI_SOURCE_PREP_PRO_MODEL,
) -> dict[str, object]:
    page = first_source_prep_batch_page(batch)
    reasons: list[str] = []
    flags = [flag.lower() for flag in source_prep_gemini_combined_values(batch, ("quality_flags", "qc_quality_flags"))]
    suspicious = source_prep_gemini_combined_values(batch, ("suspicious_readings",))
    relevance = str(
        page.get("research_relevance")
        or batch.get("research_relevance")
        or ""
    ).strip().lower()
    requested_treatment = str(page.get("requested_treatment") or batch.get("requested_treatment") or "").strip().lower()
    recommended_action = str(batch.get("recommended_action", "")).strip().lower()
    title_source_text = " ".join(
        [
            str(batch.get("title", "")),
            str(batch.get("source", "")),
            str(page.get("page_image", "")),
            recommended_action,
        ]
    ).lower()

    relevant = False
    complex_page = False
    if relevance in GEMINI_SOURCE_PREP_RELEVANT_VALUES:
        relevant = True
        reasons.append(f"research_relevance:{relevance}")
    if suspicious:
        complex_page = True
        reasons.append("suspicious_readings")
    if requested_treatment == "pro_with_crops":
        relevant = True
        reasons.append("requested_pro_with_crops")

    if requested_treatment in {"pro", "reread"}:
        complex_page = True
        reasons.append(f"requested_{requested_treatment}")
    if any(token in flag for flag in flags for token in GEMINI_SOURCE_PREP_COMPLEX_FLAG_TOKENS):
        complex_page = True
        reasons.append("complex_quality_flags")
    if any(token in title_source_text for token in GEMINI_SOURCE_PREP_COMPLEX_TEXT_TOKENS):
        complex_page = True
        reasons.append("complex_source_type")
    page_image = root.resolve() / str(page.get("page_image", ""))
    try:
        if page_image.exists() and page_image.stat().st_size >= GEMINI_SOURCE_PREP_IMAGE_SIZE_COMPLEX_BYTES:
            complex_page = True
            reasons.append("large_page_image")
    except OSError:
        pass

    pdf_profile = source_prep_gemini_pdf_profile(root, batch)
    profile_flags = [str(flag).lower() for flag in pdf_profile.get("flags", []) or []]
    if profile_flags:
        if any(flag in profile_flags for flag in ("table_like_layout", "full_page_image_scan", "possible_ocr_garbage")):
            complex_page = True
            reasons.append("pdf_profile_complex")
    elif pdf_profile.get("eligible"):
        reasons.append("pdf_native_text_safe")

    if relevant:
        return {
            "tier": "pro_with_crops",
            "model": pro_model,
            "use_crops": True,
            "relevant": True,
            "complex": complex_page,
            "reasons": list(dict.fromkeys(reasons)) or ["research_relevance"],
        }
    if complex_page:
        return {
            "tier": "pro",
            "model": pro_model,
            "use_crops": False,
            "relevant": False,
            "complex": True,
            "reasons": list(dict.fromkeys(reasons)) or ["complex_page"],
        }
    return {
        "tier": "lite",
        "model": lite_model,
        "use_crops": False,
        "relevant": False,
        "complex": False,
        "reasons": list(dict.fromkeys(reasons)) or ["simple_page"],
    }


def source_prep_gemini_mime_type(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in {".jpg", ".jpeg"}:
        return "image/jpeg"
    if suffix == ".png":
        return "image/png"
    if suffix == ".webp":
        return "image/webp"
    return "application/octet-stream"


def create_gemini_source_prep_crops(
    root: Path,
    batch: dict[str, object],
    *,
    max_crops: int = 4,
) -> list[Path]:
    if max_crops <= 0:
        return []
    try:
        from PIL import Image
    except ImportError:
        return []

    page = first_source_prep_batch_page(batch)
    page_number = int(page.get("page") or batch.get("first_page") or 0)
    page_image = root.resolve() / str(page.get("page_image", ""))
    if not page_image.exists():
        return []
    image_output_dir = root.resolve() / str(page.get("image_output_dir", ""))
    if not str(image_output_dir).strip():
        return []
    crop_dir = image_output_dir / "_gemini-input-crops" / f"page-{page_number:04d}"
    crop_dir.mkdir(parents=True, exist_ok=True)

    with Image.open(page_image) as image:
        width, height = image.size
        if width < 100 or height < 100:
            return []
        if width > height * 1.25:
            boxes = [
                ("left", (0, 0, int(width * 0.52), height)),
                ("center", (int(width * 0.24), 0, int(width * 0.76), height)),
                ("right", (int(width * 0.48), 0, width, height)),
                ("middle", (0, int(height * 0.20), width, int(height * 0.80))),
            ]
        else:
            boxes = [
                ("top", (0, 0, width, int(height * 0.38))),
                ("middle", (0, int(height * 0.31), width, int(height * 0.69))),
                ("bottom", (0, int(height * 0.62), width, height)),
                ("center", (int(width * 0.15), int(height * 0.20), int(width * 0.85), int(height * 0.80))),
            ]

        written: list[Path] = []
        for index, (name, box) in enumerate(boxes[:max_crops], start=1):
            target = crop_dir / f"page-{page_number:04d}-gemini-crop-{index:02d}-{name}.png"
            image.crop(box).save(target)
            written.append(target)
        return written


def build_gemini_source_prep_prompt(batch: dict[str, object], route: dict[str, object], crop_paths: list[Path]) -> str:
    page = first_source_prep_batch_page(batch)
    flags = source_prep_gemini_combined_values(batch, ("quality_flags", "qc_quality_flags"))
    suspicious_items: list[object] = []
    for source in (batch, page):
        value = source.get("suspicious_readings")
        if isinstance(value, list):
            suspicious_items.extend(value)
    suspicious = format_suspicious_readings(suspicious_items)
    crop_note = (
        "The first attached image is the full page. Additional attached images are zoom crops of the same page; "
        "use them only to verify difficult or family-relevant details while preserving full-page reading order."
        if crop_paths
        else "The attached image is the full page."
    )
    return f"""Convert this genealogy source page into high-accuracy source-prep Markdown.

{crop_note}

## Assignment

- Task id: `{source_prep_gemini_task_id(batch)}`
- Model route: `{route.get("tier", "")}`
- Route reasons: {", ".join(str(reason) for reason in route.get("reasons", []) or [])}
- Source: `{batch.get("source", "")}`
- Job manifest: `{batch.get("job_manifest", "")}`
- Work order: `{page.get("work_order", "")}`
- Page: {page.get("page") or batch.get("first_page")}
- Output Markdown target: `{page.get("output_path", "")}`
- External research relevance: `{page.get("research_relevance", "")}`
- External requested treatment: `{page.get("requested_treatment", "")}`
- External relevance reasons: {", ".join(str(reason) for reason in page.get("research_relevance_reasons", []) or []) or "none"}
- Recommended action: `{batch.get("recommended_action", "")}`
- Quality flags: {", ".join(str(flag) for flag in flags) or "none"}
- Technical reread clues: {suspicious}

## Required Output

Write Markdown using these exact top-level sections:

## Page Metadata
## Layout And Reading Order
## Literal Transcription
## Images, Captions, And Visual Notes
## Uncertain Or Illegible
## Completeness Audit
## Visual Region Manifest

Accuracy rules:

- Transcribe from the visible page image, not from old OCR or prior Markdown.
- Preserve tables, forms, columns, captions, stamps, signatures, marginalia, and handwritten insertions in reading order.
- Preserve original spelling, punctuation, capitalization, line breaks, and source language as much as possible.
- Use `[?]` for uncertain readings and `[illegible]` only when no plausible reading is possible.
- If the page is too dense to complete without truncation, preserve the full-page reading order and clearly state what remains unresolved in the completeness audit.
- Do not invent missing text, dates, names, or relationships.
- Do not translate, summarize, interpret, or extract genealogy leads. Preserve evidence for downstream agents.
- Do not decide whether this page is genealogically important. Research agents decide relevance and may request upgraded conversion later.

Visual extraction rules:

- In `## Images, Captions, And Visual Notes`, describe meaningful visual evidence in reading order.
- Create crop bounding boxes only for substantial visuals likely to be useful as standalone wiki assets: portraits, headshots, group photographs, labeled photographs, substantial maps, large illustrations, or source-meaningful diagrams/charts.
- Do not create crop boxes for marginal numbers, checkmarks, filing marks, short handwritten notes, ordinary stamps, seals, signatures, decorative rules, page labels, or tiny marks unless the visual itself is unusually important and cannot be captured by transcription.
- Transcribe or describe minor marks in the Markdown instead of cropping them.
- In `## Visual Region Manifest`, include exactly one fenced `json` object with a `visual_regions` array.
- If there are no meaningful visual regions, return `{{"visual_regions": [], "no_visual_regions_reason": "..."}}`.
- For each visual region, include: `region_id`, `kind`, `bbox_pct`, `caption_literal`, `caption_type`, `identity_basis`, `source_context`, `confidence`, `suggested_filename`, and `inline_anchor`.
- `bbox_pct` must be `[x0, y0, x1, y1]` as percentages of the full page image from top-left, with values from 0 to 100.
- `caption_type` must be one of `source-caption`, `source-field`, `nearby-text`, or `converter-description`.
- Label people only from source context. Do not infer identity from facial appearance.
- The pipeline will crop these boxes from the full page image and write the actual crop files; do not invent final crop paths.
"""


VISUAL_REGION_MANIFEST_HEADING = "Visual Region Manifest"
VISUAL_REGION_CAPTION_TYPES = {"source-caption", "source-field", "nearby-text", "converter-description"}
VISUAL_REGION_KIND_ALIASES = {
    "headshot": "portrait",
    "passport_photo": "portrait",
    "passport photo": "portrait",
    "id_photo": "portrait",
    "id photo": "portrait",
    "photo": "photograph",
    "group photo": "group_photograph",
    "group_photo": "group_photograph",
    "image": "visual",
}
DURABLE_VISUAL_REGION_KINDS = {
    "portrait",
    "photograph",
    "group_photograph",
    "map",
    "illustration",
    "diagram",
    "chart",
    "drawing",
    "painting",
}
DURABLE_VISUAL_REGION_KEYWORDS = (
    "portrait",
    "headshot",
    "photograph",
    "photo",
    "group picture",
    "group photo",
    "map",
    "illustration",
    "diagram",
    "chart",
    "drawing",
    "painting",
)


def strip_markdown_code_fence(text: str) -> str:
    stripped = text.strip()
    if not stripped.startswith("```"):
        return stripped
    lines = stripped.splitlines()
    if len(lines) >= 2 and lines[-1].strip().startswith("```"):
        return "\n".join(lines[1:-1]).strip()
    return stripped


def source_prep_visual_manifest_path(output_path: Path) -> Path:
    return output_path.with_suffix(".visuals.json")


def extract_markdown_section_body(text: str, heading: str) -> str:
    pattern = rf"^## {re.escape(heading)}\s*\n(.*?)(?=^## |\Z)"
    match = re.search(pattern, text, flags=re.MULTILINE | re.DOTALL)
    return match.group(1).strip() if match else ""


def parse_gemini_visual_region_manifest(markdown: str) -> tuple[dict[str, object], list[str]]:
    section = extract_markdown_section_body(markdown, VISUAL_REGION_MANIFEST_HEADING)
    if not section:
        return {}, ["visual_region_manifest_missing"]

    fenced = re.search(r"```(?:json)?\s*(.*?)\s*```", section, flags=re.IGNORECASE | re.DOTALL)
    json_text = fenced.group(1).strip() if fenced else section.strip()
    try:
        payload = json.loads(json_text)
    except json.JSONDecodeError as exc:
        return {}, [f"visual_region_manifest_json_invalid:{exc.msg}"]

    if isinstance(payload, list):
        payload = {"visual_regions": payload}
    if not isinstance(payload, dict):
        return {}, ["visual_region_manifest_not_object"]
    regions = payload.get("visual_regions", [])
    if not isinstance(regions, list):
        return {}, ["visual_regions_not_list"]
    payload["visual_regions"] = regions
    return payload, []


def coerce_visual_region_bbox(region: dict[str, object], image_width: int, image_height: int) -> tuple[list[float], tuple[int, int, int, int], list[str]]:
    flags: list[str] = []
    bbox_pct_raw = region.get("bbox_pct")
    bbox_pixels_raw = region.get("bbox_pixels")
    bbox_pct: list[float] | None = None

    if isinstance(bbox_pct_raw, dict):
        values = [
            bbox_pct_raw.get("x0", bbox_pct_raw.get("left")),
            bbox_pct_raw.get("y0", bbox_pct_raw.get("top")),
            bbox_pct_raw.get("x1", bbox_pct_raw.get("right")),
            bbox_pct_raw.get("y1", bbox_pct_raw.get("bottom")),
        ]
    elif isinstance(bbox_pct_raw, (list, tuple)):
        values = list(bbox_pct_raw)
    else:
        values = []
    if len(values) == 4:
        try:
            bbox_pct = [float(value) for value in values]
            if max(bbox_pct) <= 1.0:
                bbox_pct = [value * 100.0 for value in bbox_pct]
        except (TypeError, ValueError):
            bbox_pct = None

    if bbox_pct is None:
        if isinstance(bbox_pixels_raw, dict):
            pixel_values = [
                bbox_pixels_raw.get("x0", bbox_pixels_raw.get("left")),
                bbox_pixels_raw.get("y0", bbox_pixels_raw.get("top")),
                bbox_pixels_raw.get("x1", bbox_pixels_raw.get("right")),
                bbox_pixels_raw.get("y1", bbox_pixels_raw.get("bottom")),
            ]
        elif isinstance(bbox_pixels_raw, (list, tuple)):
            pixel_values = list(bbox_pixels_raw)
        else:
            pixel_values = []
        if len(pixel_values) == 4:
            try:
                x0, y0, x1, y1 = [float(value) for value in pixel_values]
                bbox_pct = [
                    x0 / image_width * 100.0,
                    y0 / image_height * 100.0,
                    x1 / image_width * 100.0,
                    y1 / image_height * 100.0,
                ]
            except (TypeError, ValueError, ZeroDivisionError):
                bbox_pct = None

    if bbox_pct is None:
        return [], (0, 0, 0, 0), ["visual_region_bbox_missing"]

    x0, y0, x1, y1 = bbox_pct
    x0, x1 = sorted((max(0.0, min(100.0, x0)), max(0.0, min(100.0, x1))))
    y0, y1 = sorted((max(0.0, min(100.0, y0)), max(0.0, min(100.0, y1))))
    if x1 - x0 < 0.5 or y1 - y0 < 0.5:
        flags.append("visual_region_bbox_too_small")

    px0 = max(0, int(round(x0 / 100.0 * image_width)) - 4)
    py0 = max(0, int(round(y0 / 100.0 * image_height)) - 4)
    px1 = min(image_width, int(round(x1 / 100.0 * image_width)) + 4)
    py1 = min(image_height, int(round(y1 / 100.0 * image_height)) + 4)
    if px1 <= px0 or py1 <= py0:
        flags.append("visual_region_bbox_invalid")
    return [round(x0, 3), round(y0, 3), round(x1, 3), round(y1, 3)], (px0, py0, px1, py1), flags


def normalize_visual_region_kind(value: object) -> str:
    kind = str(value or "visual").strip().lower().replace("-", "_")
    kind = VISUAL_REGION_KIND_ALIASES.get(kind, kind)
    kind = re.sub(r"[^a-z0-9_]+", "_", kind).strip("_")
    return kind or "visual"


def normalize_visual_caption_type(value: object) -> str:
    caption_type = str(value or "").strip().lower().replace("_", "-")
    if caption_type not in VISUAL_REGION_CAPTION_TYPES:
        return "converter-description"
    return caption_type


def is_durable_visual_region(region: dict[str, object], kind: str) -> bool:
    if kind in DURABLE_VISUAL_REGION_KINDS:
        return True
    context = " ".join(
        str(region.get(key) or "")
        for key in ("caption_literal", "source_context", "identity_basis", "inline_anchor", "suggested_filename")
    ).lower()
    return any(keyword in context for keyword in DURABLE_VISUAL_REGION_KEYWORDS)


def visual_region_filename(page_number: int, index: int, region: dict[str, object]) -> str:
    suggested = Path(str(region.get("suggested_filename") or "")).name
    suggested_stem = Path(suggested).stem if suggested else ""
    suffix_source = suggested_stem or str(region.get("caption_literal") or region.get("source_context") or region.get("kind") or "")
    suffix = slug(suffix_source)[:64] or normalize_visual_region_kind(region.get("kind"))
    return f"page-{page_number:04d}-image-{index:02d}-{suffix}.png"


def visual_region_markdown_label(record: dict[str, object]) -> str:
    caption = str(record.get("caption_literal") or "").strip()
    source_context = str(record.get("source_context") or "").strip()
    caption_type = str(record.get("caption_type") or "converter-description")
    kind = str(record.get("kind") or "visual")
    if caption:
        return f"{caption_type}: {caption}"
    if source_context:
        return f"{caption_type}: {source_context}"
    return f"{caption_type}: {kind}"


def insert_visual_crop_references(markdown: str, records: list[dict[str, object]], output_path: Path) -> str:
    if not records:
        return markdown
    section_match = re.search(
        r"(^## Images, Captions, And Visual Notes\s*\n)",
        markdown,
        flags=re.MULTILINE,
    )
    if not section_match:
        return markdown
    lines = ["Pipeline-extracted visual crops:"]
    for record in records:
        crop_path = Path(str(record.get("crop_path", "")))
        rel_crop = relative_path(output_path.parent, crop_path) if crop_path else ""
        label = visual_region_markdown_label(record)
        lines.append(f"- ![{label}]({rel_crop})")
        lines.append(
            "  - "
            f"Kind: {record.get('kind', 'visual')}; "
            f"label basis: {record.get('caption_type', 'converter-description')}; "
            f"bbox_pct: {record.get('bbox_pct', [])}"
        )
        source_context = str(record.get("source_context") or "").strip()
        if source_context:
            lines.append(f"  - Source context: {source_context}")
    insertion = section_match.group(1) + "\n".join(lines) + "\n\n"
    return markdown[: section_match.start(1)] + insertion + markdown[section_match.end(1) :]


def materialize_gemini_visual_regions(
    root: Path,
    batch: dict[str, object],
    markdown: str,
    *,
    require_manifest: bool = False,
) -> dict[str, object]:
    page = first_source_prep_batch_page(batch)
    page_number = int(page.get("page") or batch.get("first_page") or 0)
    page_image = root.resolve() / str(page.get("page_image", ""))
    output_path = root.resolve() / str(page.get("output_path", ""))
    image_output_dir = root.resolve() / str(page.get("image_output_dir", ""))
    manifest_path = source_prep_visual_manifest_path(output_path)
    parsed, flags = parse_gemini_visual_region_manifest(markdown)
    if flags:
        if require_manifest:
            raise RuntimeError(";".join(flags))
        return {"records": [], "flags": flags, "manifest_path": ""}

    raw_regions = parsed.get("visual_regions", [])
    if not isinstance(raw_regions, list):
        raise RuntimeError("visual_regions_not_list")

    records: list[dict[str, object]] = []
    crop_flags: list[str] = []
    skipped_regions: list[dict[str, object]] = []
    output_path.parent.mkdir(parents=True, exist_ok=True)
    if not raw_regions:
        payload = {
            "created": utc_timestamp(),
            "schema": "source-prep-visual-regions-v1",
            "purpose": "GitHub-tracked metadata for visual crops whose binary files are R2 derived assets.",
            "source": str(batch.get("source", "")),
            "source_sha256": str(batch.get("source_sha256", "")),
            "job_manifest": str(batch.get("job_manifest", "")),
            "page": page_number,
            "page_image": str(page.get("page_image", "")),
            "output_markdown": str(page.get("output_path", "")),
            "no_visual_regions_reason": str(parsed.get("no_visual_regions_reason") or "").strip(),
            "visual_regions": [],
            "skipped_regions": [],
            "flags": [],
        }
        manifest_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
        return {
            "records": records,
            "flags": crop_flags,
            "manifest_path": relative_to_root(manifest_path, root.resolve()),
            "region_count": 0,
            "declared_region_count": 0,
            "skipped_region_count": 0,
        }

    try:
        from PIL import Image
    except ImportError as exc:
        raise RuntimeError("Pillow is required for visual region extraction.") from exc

    image_output_dir.mkdir(parents=True, exist_ok=True)

    with Image.open(page_image) as image:
        width, height = image.size
        for index, raw_region in enumerate(raw_regions, start=1):
            if not isinstance(raw_region, dict):
                crop_flags.append(f"visual_region_{index}_not_object")
                continue
            kind = normalize_visual_region_kind(raw_region.get("kind"))
            if not is_durable_visual_region(raw_region, kind):
                skipped_regions.append(
                    {
                        "region_id": str(raw_region.get("region_id") or f"VR-{page_number:04d}-{index:02d}"),
                        "kind": kind,
                        "reason": "low_value_visual_region_not_saved",
                        "caption_literal": str(raw_region.get("caption_literal") or "").strip(),
                        "source_context": str(raw_region.get("source_context") or "").strip(),
                    }
                )
                continue
            bbox_pct, bbox_pixels, bbox_flags = coerce_visual_region_bbox(raw_region, width, height)
            if bbox_flags:
                crop_flags.extend(f"visual_region_{index}_{flag}" for flag in bbox_flags)
                continue
            caption_type = normalize_visual_caption_type(raw_region.get("caption_type"))
            target = image_output_dir / visual_region_filename(page_number, index, {**raw_region, "kind": kind})
            target.parent.mkdir(parents=True, exist_ok=True)
            image.crop(bbox_pixels).save(target)
            record = {
                "region_id": str(raw_region.get("region_id") or f"VR-{page_number:04d}-{index:02d}"),
                "kind": kind,
                "caption_literal": str(raw_region.get("caption_literal") or "").strip(),
                "caption_type": caption_type,
                "identity_basis": str(raw_region.get("identity_basis") or caption_type).strip(),
                "source_context": str(raw_region.get("source_context") or "").strip(),
                "confidence": str(raw_region.get("confidence") or "").strip(),
                "inline_anchor": str(raw_region.get("inline_anchor") or "").strip(),
                "bbox_pct": bbox_pct,
                "bbox_pixels": list(bbox_pixels),
                "crop_path": target,
                "crop_path_rel": relative_to_root(target, root.resolve()),
                "page_image": str(page.get("page_image", "")),
                "source": str(batch.get("source", "")),
                "source_sha256": str(batch.get("source_sha256", "")),
                "job_manifest": str(batch.get("job_manifest", "")),
                "page": page_number,
                "output_markdown": str(page.get("output_path", "")),
            }
            records.append(record)

    payload = {
        "created": utc_timestamp(),
        "schema": "source-prep-visual-regions-v1",
        "purpose": "GitHub-tracked metadata for visual crops whose binary files are R2 derived assets.",
        "source": str(batch.get("source", "")),
        "source_sha256": str(batch.get("source_sha256", "")),
        "job_manifest": str(batch.get("job_manifest", "")),
        "page": page_number,
        "page_image": str(page.get("page_image", "")),
        "output_markdown": str(page.get("output_path", "")),
        "no_visual_regions_reason": str(parsed.get("no_visual_regions_reason") or "").strip(),
        "visual_regions": [
            {key: (str(value) if isinstance(value, Path) else value) for key, value in record.items()}
            for record in records
        ],
        "skipped_regions": skipped_regions,
        "flags": crop_flags,
    }
    manifest_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    if crop_flags and (require_manifest or raw_regions):
        raise RuntimeError(";".join(crop_flags))
    return {
        "records": records,
        "flags": crop_flags,
        "manifest_path": relative_to_root(manifest_path, root.resolve()),
        "region_count": len(records),
        "declared_region_count": len(raw_regions),
        "skipped_region_count": len(skipped_regions),
    }


def call_gemini_generate_content(
    *,
    api_key: str,
    model: str,
    prompt: str,
    media_paths: list[Path],
    max_output_tokens: int,
    timeout_seconds: int = 360,
) -> dict[str, object]:
    parts: list[dict[str, object]] = [{"text": prompt}]
    for media_path in media_paths:
        parts.append(
            {
                "inline_data": {
                    "mime_type": source_prep_gemini_mime_type(media_path),
                    "data": base64.b64encode(media_path.read_bytes()).decode("ascii"),
                }
            }
        )
    payload = {
        "contents": [{"role": "user", "parts": parts}],
        "generationConfig": {
            "temperature": 0,
            "maxOutputTokens": max_output_tokens,
        },
    }
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
            response_payload = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Gemini HTTP {exc.code}: {detail[:800]}") from exc

    candidate = (response_payload.get("candidates") or [{}])[0]
    content = candidate.get("content", {}) if isinstance(candidate, dict) else {}
    text = ""
    if isinstance(content, dict):
        for part in content.get("parts", []) or []:
            if isinstance(part, dict) and part.get("text"):
                text += str(part["text"])
    return {
        "text": strip_markdown_code_fence(text),
        "finish_reason": str(candidate.get("finishReason", "")) if isinstance(candidate, dict) else "",
        "usage": response_payload.get("usageMetadata", {}),
    }


def source_prep_gemini_state_path(root: Path) -> Path:
    return root.resolve() / "research" / "_automation" / "gemini-source-prep-state.json"


def write_source_prep_gemini_state(root: Path, summary: dict[str, object]) -> Path:
    path = source_prep_gemini_state_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    return path


def source_prep_gemini_run(
    root: Path,
    *,
    limit: int = 25,
    queue_limit: int = 160,
    stale_minutes: int = 360,
    api_key: str = "",
    lite_model: str = GEMINI_SOURCE_PREP_LITE_MODEL,
    pro_model: str = GEMINI_SOURCE_PREP_PRO_MODEL,
    max_output_tokens_lite: int = 65536,
    max_output_tokens_pro: int = 65536,
    crop_relevance: bool = True,
    crop_count: int = 4,
    parallelism: int = 1,
    agent: str = "gemini-source-prep",
    dry_run: bool = False,
    refresh_queue: bool = True,
) -> dict[str, object]:
    if limit < 1:
        raise ValueError("limit must be at least 1")
    if parallelism < 1:
        raise ValueError("parallelism must be at least 1")
    paths = WikiPaths(root.resolve())
    if not api_key and not dry_run:
        api_key = os.environ.get("GEMINI_API_KEY", "") or os.environ.get("GOOGLE_API_KEY", "")
    if not api_key and not dry_run:
        raise RuntimeError("GEMINI_API_KEY or GOOGLE_API_KEY is required in the cloud automation environment.")

    if refresh_queue:
        write_source_prep_batches(
            paths.root,
            max_pages=1,
            limit=queue_limit,
            stale_minutes=stale_minutes,
        )

    queue_path = paths.research / "_agent-queues" / "source-prep-batches.json"
    queue_payload = read_json_payload(queue_path, {"tasks": []})
    queue_tasks = queue_payload.get("tasks", [])
    if not isinstance(queue_tasks, list):
        queue_tasks = []

    task_state = load_agent_task_state(paths.root)
    discovery_entries = load_source_prep_discovery_state(paths.root).get("entries", {})
    if not isinstance(discovery_entries, dict):
        discovery_entries = {}
    summary: dict[str, object] = {
        "created": utc_timestamp(),
        "mode": "gemini-source-prep",
        "dry_run": dry_run,
        "limit": limit,
        "parallelism": min(parallelism, limit),
        "queue": relative_to_root(queue_path, paths.root),
        "models": {"lite": lite_model, "pro": pro_model},
        "processed": 0,
        "completed": 0,
        "released": 0,
        "skipped": 0,
        "discovery_skipped": 0,
        "route_counts": {},
        "tasks": [],
        "usage": {"prompt_tokens": 0, "candidate_tokens": 0, "total_tokens": 0},
        "visual_regions": {"declared": 0, "cropped": 0, "skipped": 0, "manifests": 0},
    }

    def add_route_count(tier: str) -> None:
        route_counts = summary.setdefault("route_counts", {})
        if isinstance(route_counts, dict):
            route_counts[tier] = int(route_counts.get(tier, 0)) + 1

    def result_payload(
        task_report: dict[str, object],
        *,
        processed: int = 0,
        completed: int = 0,
        released: int = 0,
        skipped: int = 0,
        discovery_skipped: int = 0,
        usage: dict[str, object] | None = None,
        visual_regions: dict[str, object] | None = None,
    ) -> dict[str, object]:
        return {
            "task_report": task_report,
            "processed": processed,
            "completed": completed,
            "released": released,
            "skipped": skipped,
            "discovery_skipped": discovery_skipped,
            "usage": usage or {},
            "visual_regions": visual_regions or {},
        }

    def apply_result(result: dict[str, object]) -> None:
        task_report = result.get("task_report", {})
        if isinstance(task_report, dict):
            cast_tasks = summary.setdefault("tasks", [])
            if isinstance(cast_tasks, list):
                cast_tasks.append(task_report)
        summary["processed"] = int(summary["processed"]) + int(result.get("processed", 0) or 0)
        summary["completed"] = int(summary["completed"]) + int(result.get("completed", 0) or 0)
        summary["released"] = int(summary["released"]) + int(result.get("released", 0) or 0)
        summary["skipped"] = int(summary["skipped"]) + int(result.get("skipped", 0) or 0)
        summary["discovery_skipped"] = int(summary["discovery_skipped"]) + int(result.get("discovery_skipped", 0) or 0)
        usage = result.get("usage", {})
        if isinstance(usage, dict):
            summary_usage = summary.setdefault("usage", {})
            if isinstance(summary_usage, dict):
                summary_usage["prompt_tokens"] = int(summary_usage.get("prompt_tokens", 0)) + int(usage.get("promptTokenCount", 0) or 0)
                summary_usage["candidate_tokens"] = int(summary_usage.get("candidate_tokens", 0)) + int(usage.get("candidatesTokenCount", 0) or 0)
                summary_usage["total_tokens"] = int(summary_usage.get("total_tokens", 0)) + int(usage.get("totalTokenCount", 0) or 0)
        visual_result = result.get("visual_regions", {})
        if isinstance(visual_result, dict):
            visual_summary = summary.setdefault("visual_regions", {})
            if isinstance(visual_summary, dict):
                visual_summary["declared"] = int(visual_summary.get("declared", 0)) + int(visual_result.get("declared_region_count", 0) or 0)
                visual_summary["cropped"] = int(visual_summary.get("cropped", 0)) + int(visual_result.get("region_count", 0) or 0)
                visual_summary["skipped"] = int(visual_summary.get("skipped", 0)) + int(visual_result.get("skipped_region_count", 0) or 0)
                if visual_result.get("manifest_path"):
                    visual_summary["manifests"] = int(visual_summary.get("manifests", 0)) + 1

    state_lock = threading.Lock()

    def update_task_status(task_id: str, status: str, note: str) -> None:
        with state_lock:
            update_agent_task_state(paths.root, task_id, status, agent=agent, note=note)

    prepared_tasks: list[dict[str, object]] = []
    selected_count = 0
    for raw_task in queue_tasks:
        if selected_count >= limit:
            break
        if not isinstance(raw_task, dict):
            continue
        if int(raw_task.get("page_count", 0) or 0) != 1:
            apply_result(result_payload({"status": "skipped", "reason": "not_one_page_batch"}, skipped=1))
            continue
        status = str(raw_task.get("status", "")).strip()
        if status not in GEMINI_SOURCE_PREP_BATCHABLE_STATUSES:
            continue
        task_id = source_prep_gemini_task_id(raw_task)
        state_status = str(task_state.get(task_id, {}).get("status", "")).strip()
        if state_status in {"claimed", "in_progress", "done"}:
            apply_result(
                result_payload(
                    {"task_id": task_id, "batch_task_id": raw_task.get("task_id", ""), "status": "skipped", "reason": f"task_state_{state_status}"},
                    skipped=1,
                )
            )
            continue

        page = first_source_prep_batch_page(raw_task)
        discovery_skip_reason = source_prep_discovery_batch_skip_reason(paths.root, raw_task, discovery_entries)
        if discovery_skip_reason:
            discovery_entry = source_prep_discovery_entry_for_task(
                paths.root,
                {
                    "task_id": task_id,
                    "source_sha256": raw_task.get("source_sha256", "") or page.get("source_sha256", ""),
                },
                discovery_entries,
            )
            task_report = {
                "task_id": task_id,
                "batch_task_id": raw_task.get("task_id", ""),
                "status": "skipped",
                "reason": discovery_skip_reason,
                "discovery_path": str(discovery_entry.get("discovery_path", "")) if discovery_entry else "",
            }
            apply_result(result_payload(task_report, skipped=1, discovery_skipped=1))
            continue
        page_image = paths.root / str(page.get("page_image", ""))
        output_path = paths.root / str(page.get("output_path", ""))
        if not page_image.exists():
            try:
                regenerated = ensure_source_prep_page_image(paths.root, raw_task)
                if regenerated is not None:
                    page_image = regenerated
            except Exception:
                pass
        if not page_image.exists():
            task_report = {
                "task_id": task_id,
                "status": "skipped",
                "reason": "page_image_missing",
                "page_image": relative_to_root(page_image, paths.root),
            }
            apply_result(result_payload(task_report, skipped=1))
            continue

        route = classify_gemini_source_prep_batch(paths.root, raw_task, lite_model=lite_model, pro_model=pro_model)
        if not crop_relevance:
            route["use_crops"] = False
            if route.get("tier") == "pro_with_crops":
                route["tier"] = "pro"
        add_route_count(str(route.get("tier", "")))
        max_output_tokens = max_output_tokens_pro if str(route.get("model")) == pro_model else max_output_tokens_lite
        task_report: dict[str, object] = {
            "task_id": task_id,
            "batch_task_id": raw_task.get("task_id", ""),
            "route": route,
            "page_image": relative_to_root(page_image, paths.root),
            "output_path": relative_to_root(output_path, paths.root),
        }

        selected_count += 1
        if dry_run:
            task_report["status"] = "planned"
            apply_result(result_payload(task_report, processed=1))
            continue

        update_task_status(task_id, "claimed", f"Gemini route {route.get('tier')}")
        update_task_status(task_id, "in_progress", f"Using {route.get('model')}")
        prepared_tasks.append(
            {
                "task_id": task_id,
                "raw_task": raw_task,
                "route": route,
                "page_image": page_image,
                "output_path": output_path,
                "task_report": task_report,
            }
        )

    def process_prepared_task(prepared_task: dict[str, object]) -> dict[str, object]:
        task_id = str(prepared_task["task_id"])
        raw_task = prepared_task["raw_task"]
        route = prepared_task["route"]
        page_image = prepared_task["page_image"]
        output_path = prepared_task["output_path"]
        task_report = dict(prepared_task["task_report"])
        max_output_tokens = max_output_tokens_pro if str(route.get("model")) == pro_model else max_output_tokens_lite
        try:
            crops = create_gemini_source_prep_crops(paths.root, raw_task, max_crops=crop_count) if route.get("use_crops") else []
            prompt = build_gemini_source_prep_prompt(raw_task, route, crops)
            media_paths = [page_image, *crops]
            response = call_gemini_generate_content(
                api_key=api_key,
                model=str(route.get("model")),
                prompt=prompt,
                media_paths=media_paths,
                max_output_tokens=max_output_tokens,
            )
            usage = response.get("usage", {})
            task_report["usage"] = usage
            task_report["finish_reason"] = response.get("finish_reason", "")
            if str(response.get("finish_reason", "")) == "MAX_TOKENS":
                update_task_status(
                    task_id,
                    "released",
                    "Gemini output hit max tokens; retry full-page conversion with a higher output budget or targeted crop attachments.",
                )
                task_report["status"] = "released"
                task_report["reason"] = "max_tokens"
                return result_payload(task_report, processed=1, released=1, usage=usage if isinstance(usage, dict) else {})

            markdown = str(response.get("text", "")).strip()
            try:
                visual_result = materialize_gemini_visual_regions(
                    paths.root,
                    raw_task,
                    markdown,
                    require_manifest=True,
                )
            except Exception as exc:
                update_task_status(
                    task_id,
                    "released",
                    f"Gemini visual crop extraction failed: {str(exc)[:180]}",
                )
                task_report["status"] = "released"
                task_report["reason"] = "visual_crop_extraction_failed"
                task_report["error"] = str(exc)
                return result_payload(task_report, processed=1, released=1, usage=usage if isinstance(usage, dict) else {})
            task_report["visual_regions"] = {
                "manifest_path": visual_result.get("manifest_path", ""),
                "declared": visual_result.get("declared_region_count", 0),
                "cropped": visual_result.get("region_count", 0),
                "skipped": visual_result.get("skipped_region_count", 0),
                "flags": visual_result.get("flags", []),
            }
            records = visual_result.get("records", [])
            if isinstance(records, list):
                markdown = insert_visual_crop_references(markdown, records, output_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(markdown, encoding="utf-8")
            review = review_source_prep_page_output(output_path)
            task_report["review"] = review
            if str(review.get("status", "")) == "done":
                update_task_status(
                    task_id,
                    "done",
                    f"Completed by Gemini route {route.get('tier')}",
                )
                task_report["status"] = "done"
                return result_payload(
                    task_report,
                    processed=1,
                    completed=1,
                    usage=usage if isinstance(usage, dict) else {},
                    visual_regions=visual_result if isinstance(visual_result, dict) else {},
                )
            else:
                flags = ",".join(str(flag) for flag in review.get("quality_flags", []) or [])
                update_task_status(
                    task_id,
                    "released",
                    f"Gemini output failed source-prep review: {flags or 'missing contract sections'}",
                )
                task_report["status"] = "released"
                task_report["reason"] = "review_failed"
                return result_payload(
                    task_report,
                    processed=1,
                    released=1,
                    usage=usage if isinstance(usage, dict) else {},
                    visual_regions=visual_result if isinstance(visual_result, dict) else {},
                )
        except Exception as exc:
            update_task_status(
                task_id,
                "released",
                f"Gemini conversion error: {str(exc)[:220]}",
            )
            task_report["status"] = "released"
            task_report["reason"] = "gemini_error"
            task_report["error"] = str(exc)
            return result_payload(task_report, processed=1, released=1)

    if prepared_tasks:
        max_workers = min(int(summary["parallelism"]), len(prepared_tasks))
        if max_workers <= 1:
            for prepared_task in prepared_tasks:
                apply_result(process_prepared_task(prepared_task))
        else:
            completed_results: list[tuple[int, dict[str, object]]] = []
            with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
                future_to_index = {
                    executor.submit(process_prepared_task, prepared_task): index
                    for index, prepared_task in enumerate(prepared_tasks)
                }
                for future in concurrent.futures.as_completed(future_to_index):
                    completed_results.append((future_to_index[future], future.result()))
            for _, result in sorted(completed_results, key=lambda item: item[0]):
                apply_result(result)

    summary["finished"] = utc_timestamp()
    state_path = write_source_prep_gemini_state(paths.root, summary)
    summary["state_path"] = relative_to_root(state_path, paths.root)
    append_log(
        paths.research / "log.md",
        "gemini-source-prep | "
        f"processed {summary['processed']}, completed {summary['completed']}, released {summary['released']}, "
        f"parallelism={summary['parallelism']}, routes={summary.get('route_counts', {})}, dry_run={dry_run}",
    )
    return summary


def materialize_source_prep_tasks(
    root: Path,
    task_state: dict[str, dict[str, object]],
) -> list[dict[str, object]]:
    tasks: list[dict[str, object]] = []
    for task in build_source_prep_agent_tasks(root):
        task_copy = dict(task)
        task_copy.pop("prompt", None)
        apply_agent_task_state(task_copy, task_state.get(str(task_copy.get("task_id", "")), {}))
        tasks.append(task_copy)
    return tasks


def build_source_prep_batch_agent_tasks(
    source_tasks: list[dict[str, object]],
    max_pages: int = SOURCE_PREP_MAX_PAGES_PER_WORKER,
    limit: int = 50,
    statuses: list[str] | None = None,
) -> list[dict[str, object]]:
    if max_pages < 1:
        raise ValueError("max_pages must be at least 1")
    if limit < 1:
        raise ValueError("limit must be at least 1")
    max_pages = min(max_pages, SOURCE_PREP_MAX_PAGES_PER_WORKER)
    allowed_statuses = tuple(statuses or SOURCE_PREP_BATCHABLE_STATUSES)
    unknown_statuses = set(allowed_statuses).difference(SOURCE_PREP_BATCHABLE_STATUSES)
    if unknown_statuses:
        raise ValueError(f"unsupported source-prep batch status: {', '.join(sorted(unknown_statuses))}")

    available = [
        task
        for task in source_tasks
        if str(task.get("status", "")).strip() in allowed_statuses
    ]
    available.sort(
        key=lambda task: (
            SOURCE_PREP_BATCH_STATUS_PRIORITY.get(str(task.get("status", "")), 99),
            str(task.get("job_manifest", "")),
            int(task.get("page", 0) or 0),
        )
    )

    batches: list[dict[str, object]] = []
    current: list[dict[str, object]] = []
    current_key: tuple[object, ...] | None = None
    last_page = 0

    def flush_current() -> None:
        nonlocal current, current_key, last_page
        if current and len(batches) < limit:
            batches.append(build_source_prep_batch_task(current))
        current = []
        current_key = None
        last_page = 0

    for task in available:
        if source_prep_task_requires_single_page_batch(task):
            flush_current()
            if len(batches) >= limit:
                break
            batches.append(build_source_prep_batch_task([task]))
            continue

        page_number = int(task.get("page", 0) or 0)
        key = source_prep_batch_group_key(task)
        if (
            current
            and key == current_key
            and page_number == last_page + 1
            and len(current) < max_pages
        ):
            current.append(task)
            last_page = page_number
            if len(current) >= max_pages:
                flush_current()
            continue

        flush_current()
        if len(batches) >= limit:
            break
        current = [task]
        current_key = key
        last_page = page_number
        if len(current) >= max_pages:
            flush_current()

    if len(batches) < limit:
        flush_current()
    return batches


def source_prep_task_requires_single_page_batch(task: dict[str, object]) -> bool:
    if task.get("suspicious_readings"):
        return True
    if task.get("relevance_feedback_ids") or task.get("requested_treatment"):
        return True
    action = str(task.get("recommended_action", ""))
    relevance = str(task.get("family_relevance", ""))
    return relevance == "critical" and action in {"reread-page", "reread-region", "hold-for-human"}


def source_prep_batch_group_key(task: dict[str, object]) -> tuple[object, ...]:
    return (
        str(task.get("job_manifest", "")),
        str(task.get("status", "")),
        str(task.get("repair_reason", "")),
        str(task.get("recommended_action", "")),
        tuple(str(flag) for flag in task.get("quality_flags", []) or []),
        tuple(str(section) for section in task.get("missing_sections", []) or []),
        tuple(str(flag) for flag in task.get("qc_quality_flags", []) or []),
    )


def build_source_prep_batch_task(page_tasks: list[dict[str, object]]) -> dict[str, object]:
    first = page_tasks[0]
    last = page_tasks[-1]
    first_page = int(first.get("page", 0) or 0)
    last_page = int(last.get("page", 0) or 0)
    job_slug = Path(str(first.get("job_manifest", ""))).parent.name
    if first_page == last_page:
        page_range = f"p{first_page:04d}"
    else:
        page_range = f"p{first_page:04d}-p{last_page:04d}"
    pages = [source_prep_batch_page_record(task) for task in page_tasks]
    batch = {
        "task_id": f"source-prep-batch:{job_slug}:{page_range}",
        "queue": "source-prep-batches",
        "role": "source_converter",
        "skill": "historical-document-conversion",
        "status": str(first.get("status", "")),
        "source": str(first.get("source", "")),
        "source_sha256": str(first.get("source_sha256", "")),
        "job_manifest": str(first.get("job_manifest", "")),
        "job_id": str(first.get("job_id", "")),
        "title": str(first.get("title", "")),
        "first_page": first_page,
        "last_page": last_page,
        "page_count": len(page_tasks),
        "task_ids": [str(task.get("task_id", "")) for task in page_tasks],
        "pages": pages,
    }
    if first.get("repair_reason"):
        batch["repair_reason"] = first["repair_reason"]
    if first.get("recommended_action"):
        batch["recommended_action"] = first["recommended_action"]
    batch["prompt"] = build_source_prep_batch_agent_prompt(batch)
    return batch


def source_prep_batch_page_record(task: dict[str, object]) -> dict[str, object]:
    record = {
        "page": int(task.get("page", 0) or 0),
        "task_id": str(task.get("task_id", "")),
        "page_image": str(task.get("page_image", "")),
        "work_order": str(task.get("work_order", "")),
        "output_path": str(task.get("output_path", "")),
        "image_output_dir": str(task.get("image_output_dir", "")),
    }
    for key in (
        "quality_flags",
        "missing_sections",
        "qc_quality_flags",
        "family_relevance",
        "research_relevance",
        "requested_treatment",
        "research_relevance_reasons",
        "research_entities",
        "relevance_feedback_ids",
        "matched_terms",
        "suspicious_readings",
    ):
        value = task.get(key)
        if value:
            record[key] = value
    return record


SOURCE_PREP_CANONICAL_TASK_STATUS_PRIORITY = {
    "needs_reread": 0,
    "done": 1,
    SOURCE_PREP_DISCOVERY_TASK_STATUS: 2,
    "todo": 3,
}


def source_prep_canonical_task_key(task: dict[str, object]) -> tuple[str, int] | None:
    source_identity = str(task.get("source_sha256", "") or task.get("source", "")).strip()
    source_page = safe_int(task.get("source_page"), safe_int(task.get("page"), 0))
    if not source_identity or source_page < 1:
        return None
    return (source_identity, source_page)


def source_prep_canonical_task_rank(task: dict[str, object]) -> tuple[int, int, str]:
    status = str(task.get("status", "")).strip()
    relevance_rank = 0 if task.get("relevance_feedback_ids") or task.get("requested_treatment") else 1
    status_rank = SOURCE_PREP_CANONICAL_TASK_STATUS_PRIORITY.get(status, 9)
    return (status_rank, relevance_rank, str(task.get("job_manifest", "")))


def select_canonical_source_prep_tasks(tasks: list[dict[str, object]]) -> list[dict[str, object]]:
    selected: dict[tuple[str, int], tuple[int, dict[str, object]]] = {}
    unkeyed: list[tuple[int, dict[str, object]]] = []
    for index, task in enumerate(tasks):
        key = source_prep_canonical_task_key(task)
        if key is None:
            unkeyed.append((index, task))
            continue
        existing = selected.get(key)
        if existing is None or source_prep_canonical_task_rank(task) < source_prep_canonical_task_rank(existing[1]):
            selected[key] = (index, task)
    return [task for _, task in sorted([*selected.values(), *unkeyed], key=lambda item: item[0])]


def build_source_prep_agent_tasks(root: Path, *, write_page_review_cache: bool = True) -> list[dict[str, object]]:
    tasks: list[dict[str, object]] = []
    jobs_dir = root / "raw" / "codex-conversion-jobs"
    if not jobs_dir.exists():
        return tasks
    qc_repair_by_manifest = load_qc_repair_pages(root)
    relevance_hints = active_source_relevance_hints(root)
    discovery_entries = load_source_prep_discovery_state(root).get("entries", {})
    if not isinstance(discovery_entries, dict):
        discovery_entries = {}
    page_review_cache = load_source_prep_page_cache(root)
    page_review_cache_changed = False
    for manifest_path in sorted(jobs_dir.glob("*/manifest.json")):
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        job_slug = manifest_path.parent.name
        manifest_key = relative_to_root(manifest_path, root)
        qc_repair_pages = qc_repair_by_manifest.get(manifest_key, {})
        for page in manifest.get("pages", []):
            if not isinstance(page, dict):
                continue
            page_number = int(page.get("page", 0))
            output_path = root / str(page.get("output_path", ""))
            qc_hold = qc_repair_pages.get(page_number)
            output_review, cache_changed = cached_review_source_prep_page_output(root, output_path, page_review_cache)
            page_review_cache_changed = page_review_cache_changed or cache_changed
            status = str(output_review["status"])
            if output_path.exists() and qc_hold:
                status = "needs_reread"
            image_output_dir = str(page.get("image_output_dir") or "")
            if not image_output_dir:
                image_output_dir = relative_to_root(manifest_path.parent / "extracted-images" / f"page-{page_number:04d}", root)
            task = {
                "task_id": f"source-prep:{job_slug}:p{page_number:04d}",
                "queue": "source-prep",
                "role": "source_converter",
                "skill": "historical-document-conversion",
                "status": status,
                "source": str(manifest.get("source_file", "")),
                "source_sha256": str(manifest.get("source_sha256", "")),
                "job_manifest": relative_to_root(manifest_path, root),
                "job_id": str(manifest.get("job_id", "")),
                "title": str(manifest.get("title", "")),
                "page": page_number,
                "source_page": safe_int(page.get("source_page"), page_number),
                "page_image": normalize_job_artifact_reference(
                    root,
                    manifest_path,
                    str(page.get("image_path", "")),
                    f"page-images/page-{page_number:04d}",
                ),
                "work_order": str(page.get("work_order_path", "")),
                "output_path": str(page.get("output_path", "")),
                "image_output_dir": image_output_dir,
            }
            if output_review.get("quality_flags"):
                task["quality_flags"] = output_review["quality_flags"]
            if output_review.get("missing_sections"):
                task["missing_sections"] = output_review["missing_sections"]
            if qc_hold:
                task.update(
                    {
                        "repair_reason": "post_conversion_qc_hold",
                        "recommended_action": qc_hold.get("recommended_action", ""),
                        "conversion_confidence": qc_hold.get("conversion_confidence", ""),
                        "family_relevance": qc_hold.get("family_relevance", ""),
                        "qc_quality_flags": qc_hold.get("quality_flags", []),
                        "matched_terms": qc_hold.get("matched_terms", []),
                        "suspicious_readings": qc_hold.get("suspicious_readings", []),
                        "converted_file": qc_hold.get("converted_file", ""),
                        "chunk_manifest": qc_hold.get("chunk_manifest", ""),
                    }
                )
            apply_source_relevance_feedback(task, relevance_hints)
            apply_source_prep_discovery_state(root, task, discovery_entries)
            task["prompt"] = build_source_prep_agent_prompt(task)
            tasks.append(task)
    if page_review_cache_changed and write_page_review_cache:
        save_source_prep_page_cache(root, page_review_cache)
    return select_canonical_source_prep_tasks(tasks)


def build_conversion_qa_agent_tasks(root: Path) -> list[dict[str, object]]:
    tasks: list[dict[str, object]] = []
    for manifest_path in sorted((root / "raw" / "chunks").glob("*/manifest.json")):
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        converted_file = str(manifest.get("converted_file", ""))
        source_slug = slug(Path(converted_file).stem)
        task = {
            "task_id": conversion_qa_task_id_for_converted_file(converted_file),
            "queue": "conversion-qa",
            "role": "conversion_qa_reviewer",
            "skill": "conversion-qa-triage",
            "status": "todo",
            "converted_file": converted_file,
            "chunk_manifest": relative_to_root(manifest_path, root),
            "source": str(manifest.get("source", "")),
            "source_sha256": str(manifest.get("source_sha256", "")),
            "source_manifest": str(manifest.get("source_manifest", "")),
            "output_dir": "research/_conversion-review",
            "auto_qc_triage": f"research/_conversion-review/triage/{source_slug}.md",
            "auto_qc_page_queue": f"research/_conversion-review/page-queues/{source_slug}.md",
            "auto_qc_corrections": f"research/_conversion-review/corrections/{source_slug}.md",
        }
        task["prompt"] = build_conversion_qa_agent_prompt(task)
        tasks.append(task)
    return tasks


def conversion_qa_task_id_for_converted_file(converted_file: str) -> str:
    return f"conversion-qa:{slug(converted_file)}"


def conversion_qa_is_done(task_state: dict[str, dict[str, object]], converted_file: str) -> bool:
    task_id = conversion_qa_task_id_for_converted_file(converted_file)
    state = task_state.get(task_id, {})
    return str(state.get("status", "")).strip() == "done"


def load_qc_blocked_pages(root: Path) -> dict[str, dict[int, dict[str, object]]]:
    qc_pages_path = root / "research" / "_conversion-review" / "qc-pages.json"
    if not qc_pages_path.exists():
        return {}
    try:
        payload = json.loads(qc_pages_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    pages = payload.get("pages", []) if isinstance(payload, dict) else []
    if not isinstance(pages, list):
        return {}

    task_state = load_agent_task_state(root)
    blocked: dict[str, dict[int, dict[str, object]]] = {}
    for page in pages:
        if not isinstance(page, dict):
            continue
        if str(page.get("recommended_action", "")) == "pass":
            continue
        converted_file = str(page.get("converted_file", ""))
        if not converted_file:
            continue
        try:
            page_number = int(page.get("page", 0))
        except (TypeError, ValueError):
            continue
        if page_number < 1:
            continue
        source_manifest = str(page.get("source_manifest", "")).strip()
        if not source_manifest:
            source_manifest = source_manifest_for_qc_page(root, page)
        if qc_page_reread_is_resolved(root, source_manifest, page_number, task_state):
            continue
        blocked.setdefault(converted_file, {})[page_number] = page
    return blocked


def load_qc_repair_pages(root: Path) -> dict[str, dict[int, dict[str, object]]]:
    qc_pages_path = root / "research" / "_conversion-review" / "qc-pages.json"
    if not qc_pages_path.exists():
        return {}
    try:
        payload = json.loads(qc_pages_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    pages = payload.get("pages", []) if isinstance(payload, dict) else []
    if not isinstance(pages, list):
        return {}

    task_state = load_agent_task_state(root)
    repairs: dict[str, dict[int, dict[str, object]]] = {}
    for page in pages:
        if not isinstance(page, dict):
            continue
        if str(page.get("recommended_action", "")) == "pass":
            continue
        source_manifest = str(page.get("source_manifest", "")).strip()
        if not source_manifest:
            source_manifest = source_manifest_for_qc_page(root, page)
        if not source_manifest:
            continue
        try:
            page_number = int(page.get("page", 0))
        except (TypeError, ValueError):
            continue
        if page_number < 1:
            continue
        if qc_page_reread_is_resolved(root, source_manifest, page_number, task_state):
            continue
        repairs.setdefault(source_manifest, {})[page_number] = page
    return repairs


def source_prep_task_id_for_manifest_page(source_manifest: str, page_number: int) -> str:
    job_slug = Path(source_manifest).parent.name
    return f"source-prep:{job_slug}:p{page_number:04d}"


def qc_page_reread_is_resolved(
    root: Path,
    source_manifest: str,
    page_number: int,
    task_state: dict[str, dict[str, object]],
) -> bool:
    if not source_manifest:
        return False
    task_id = source_prep_task_id_for_manifest_page(source_manifest, page_number)
    state = task_state.get(task_id, {})
    if str(state.get("status", "")).strip() != "done":
        return False

    manifest_path = Path(source_manifest)
    if not manifest_path.is_absolute():
        manifest_path = root / manifest_path
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False

    for page in manifest.get("pages", []):
        if not isinstance(page, dict):
            continue
        try:
            manifest_page_number = int(page.get("page", 0))
        except (TypeError, ValueError):
            continue
        if manifest_page_number != page_number:
            continue
        output_path = root / str(page.get("output_path", ""))
        return str(review_source_prep_page_output(output_path).get("status", "")) == "done"
    return False


def source_manifest_for_qc_page(root: Path, page: dict[str, object]) -> str:
    chunk_manifest_value = str(page.get("chunk_manifest", ""))
    if chunk_manifest_value:
        chunk_manifest = root / chunk_manifest_value
        try:
            manifest = json.loads(chunk_manifest.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            manifest = {}
        source_manifest = str(manifest.get("source_manifest", "")).strip()
        if source_manifest:
            return source_manifest

    converted_file_value = str(page.get("converted_file", ""))
    if not converted_file_value:
        return ""
    converted_file = root / converted_file_value
    try:
        text = converted_file.read_text(encoding="utf-8")
    except OSError:
        return ""
    _, _, source_manifest = parse_conversion_metadata(text)
    return source_manifest


def qc_blocked_pages_for_range(
    blocked_pages: dict[int, dict[str, object]],
    page_start: int,
    page_end: int,
) -> list[int]:
    if not blocked_pages:
        return []
    if page_start < 1:
        return sorted(blocked_pages)
    if page_end < page_start:
        page_end = page_start
    return [page for page in sorted(blocked_pages) if page_start <= page <= page_end]


def chunk_manifests_by_converted_file(root: Path) -> dict[str, list[str]]:
    manifests: dict[str, list[str]] = {}
    for manifest_path in sorted((root / "raw" / "chunks").glob("*/manifest.json")):
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        converted_file = str(manifest.get("converted_file", ""))
        if not converted_file:
            continue
        manifests.setdefault(converted_file, []).append(relative_to_root(manifest_path, root))
    return manifests


def source_usability_status(
    source_status: str,
    conversion_jobs: list[dict[str, object]],
    converted_files: list[str],
    chunk_manifests: list[str],
    qc_hold_count: int,
    page_repair_count: int,
) -> str:
    if not converted_files:
        return "conversion_in_progress" if conversion_jobs else "conversion_not_started"
    if not chunk_manifests:
        return "needs_chunking"
    if page_repair_count:
        return "usable_with_page_repairs"
    if source_status == "partially_converted":
        return "partial_with_page_holds" if qc_hold_count else "partially_usable_for_extraction"
    if qc_hold_count:
        return "usable_with_page_holds"
    return "usable_for_extraction"


def source_prep_task_counts_by_hash(root: Path) -> dict[str, dict[str, int]]:
    counts: dict[str, dict[str, int]] = {}
    for task in build_source_prep_agent_tasks(root, write_page_review_cache=False):
        digest = str(task.get("source_sha256", ""))
        if not digest:
            continue
        status = str(task.get("status", "unknown"))
        source_counts = counts.setdefault(digest, {})
        source_counts[status] = source_counts.get(status, 0) + 1
    return counts


def markdown_table_cell(value: object) -> str:
    return str(value).replace("|", "\\|")


def build_source_usability_markdown(payload: dict[str, object]) -> str:
    summary = payload.get("summary", {})
    sources = payload.get("sources", [])
    summary_lines = []
    if isinstance(summary, dict):
        status_counts = summary.get("status_counts", {})
        if isinstance(status_counts, dict):
            for status, count in sorted(status_counts.items()):
                summary_lines.append(f"- {status}: {count}")
    if not summary_lines:
        summary_lines.append("- No raw sources found.")

    rows = [
        "| Source | Status | Converted | Chunks | Pages needing repair | QC-held pages |",
        "| --- | --- | ---: | ---: | ---: | ---: |",
    ]
    if isinstance(sources, list):
        for source in sources:
            if not isinstance(source, dict):
                continue
            rows.append(
                "| "
                + " | ".join(
                    [
                        markdown_table_cell(source.get("raw_path", "")),
                        markdown_table_cell(source.get("status", "")),
                        markdown_table_cell(source.get("converted_file_count", 0)),
                        markdown_table_cell(source.get("chunk_manifest_count", 0)),
                        markdown_table_cell(source.get("page_repair_count", 0)),
                        markdown_table_cell(source.get("qc_hold_count", 0)),
                    ]
                )
                + " |"
            )

    return f"""# Source Usability

Generated: {payload.get("created", "")}

This report answers whether each raw source is ready for LLM extraction, still waiting on conversion, or held only on specific pages that need reread.

## Summary

{chr(10).join(summary_lines)}

## Sources

{chr(10).join(rows)}
"""


def write_source_usability_report(
    root: Path,
    output: Path | None = None,
    markdown_output: Path | None = None,
) -> list[Path]:
    paths = WikiPaths(root.resolve())
    write_source_prep_index(paths.root)
    prep_manifest_path = paths.raw / "source-prep-manifest.json"
    try:
        prep_manifest = json.loads(prep_manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        prep_manifest = {"sources": []}

    chunks_by_converted = chunk_manifests_by_converted_file(paths.root)
    qc_blocked_by_source = load_qc_blocked_pages(paths.root)
    prep_task_counts = source_prep_task_counts_by_hash(paths.root)
    entries = []
    sources = prep_manifest.get("sources", []) if isinstance(prep_manifest, dict) else []
    if not isinstance(sources, list):
        sources = []

    for source in sources:
        if not isinstance(source, dict):
            continue
        conversion_jobs = [job for job in source.get("conversion_jobs", []) if isinstance(job, dict)]
        converted_sources = [item for item in source.get("converted_sources", []) if isinstance(item, dict)]
        converted_files = [str(item.get("path", "")) for item in converted_sources if item.get("path")]
        chunk_manifests = sorted(
            {
                manifest
                for converted_file in converted_files
                for manifest in chunks_by_converted.get(converted_file, [])
            }
        )
        qc_holds = []
        for converted_file in converted_files:
            for page_number, page in sorted(qc_blocked_by_source.get(converted_file, {}).items()):
                qc_holds.append(
                    {
                        "converted_file": converted_file,
                        "page": page_number,
                        "recommended_action": page.get("recommended_action", ""),
                        "quality_flags": page.get("quality_flags", []),
                        "matched_terms": page.get("matched_terms", []),
                        "suspicious_readings": page.get("suspicious_readings", []),
                    }
                )
        status = source_usability_status(
            str(source.get("status", "")),
            conversion_jobs,
            converted_files,
            chunk_manifests,
            len(qc_holds),
            prep_task_counts.get(str(source.get("sha256", "")), {}).get("needs_reread", 0),
        )
        source_task_counts = prep_task_counts.get(str(source.get("sha256", "")), {})
        entries.append(
            {
                "id": source.get("id", ""),
                "raw_path": source.get("raw_path", ""),
                "media_type": source.get("media_type", ""),
                "status": status,
                "source_prep_status": source.get("status", ""),
                "conversion_job_count": len(conversion_jobs),
                "converted_file_count": len(converted_files),
                "chunk_manifest_count": len(chunk_manifests),
                "qc_hold_count": len(qc_holds),
                "source_prep_task_counts": source_task_counts,
                "page_repair_count": source_task_counts.get("needs_reread", 0),
                "conversion_jobs": conversion_jobs,
                "converted_files": converted_files,
                "chunk_manifests": chunk_manifests,
                "qc_holds": qc_holds,
            }
        )

    status_counts = count_task_statuses(entries)
    payload = {
        "created": utc_timestamp(),
        "purpose": "Source-readiness report for raw source -> LLM-readable source pipeline.",
        "inputs": {
            "source_prep_manifest": relative_to_root(prep_manifest_path, paths.root),
            "qc_pages": "research/_conversion-review/qc-pages.json",
        },
        "summary": {
            "total_sources": len(entries),
            "status_counts": status_counts,
        },
        "sources": entries,
    }

    output_path = output or (paths.indexes / "source-usability.json")
    markdown_path = markdown_output or (paths.research / "source-usability.md")
    if not output_path.is_absolute():
        output_path = paths.root / output_path
    if not markdown_path.is_absolute():
        markdown_path = paths.root / markdown_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    markdown_path.write_text(build_source_usability_markdown(payload), encoding="utf-8")
    append_log(paths.research / "log.md", f"source-status | Wrote {relative_to_root(output_path, paths.root)}")
    return [output_path, markdown_path]


def write_system_status_dashboard(
    root: Path,
    output: Path | None = None,
    markdown_output: Path | None = None,
    *,
    refresh_source_status: bool = True,
) -> list[Path]:
    paths = WikiPaths(root.resolve())
    blockers: list[str] = []
    if refresh_source_status:
        try:
            write_source_usability_report(paths.root)
        except Exception as exc:
            blockers.append(f"source-status refresh: {exc}")

    payload = build_system_status_payload(paths.root, blockers)
    output_path = output or (paths.indexes / "system-status.json")
    markdown_path = markdown_output or (paths.research / "System Dashboard.md")
    if not output_path.is_absolute():
        output_path = paths.root / output_path
    if not markdown_path.is_absolute():
        markdown_path = paths.root / markdown_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    markdown_path.write_text(build_system_status_markdown(payload), encoding="utf-8")
    append_index_reference(paths.research / "index.md", "Agent Work", "[[System Dashboard]]")
    append_log(paths.research / "log.md", f"system-status | Wrote {relative_to_root(output_path, paths.root)}")
    return [output_path, markdown_path]


def build_system_status_payload(root: Path, blockers: list[str] | None = None) -> dict[str, object]:
    paths = WikiPaths(root.resolve())
    prep_manifest = read_json_payload(paths.raw / "source-prep-manifest.json", {"sources": []})
    raw_cloud = read_json_payload(paths.raw / "r2-raw-sources.json", {"files": []})
    derived_assets = read_json_payload(paths.raw / "r2-derived-assets.json", {"files": []})
    source_usability = read_json_payload(paths.indexes / "source-usability.json", {})
    research_analyzer = read_json_payload(paths.indexes / "research-analyzer.json", {})
    relevance_feedback = load_source_relevance_feedback(paths.root)

    queue_dir = paths.research / "_agent-queues"
    queues = {
        "source_prep_batches": system_queue_summary(paths.root, queue_dir / "source-prep-batches.json"),
        "source_prep": system_queue_summary(paths.root, queue_dir / "source-prep.json"),
        "conversion_qa": system_queue_summary(paths.root, queue_dir / "conversion-qa.json"),
        "evidence_extraction": system_queue_summary(paths.root, queue_dir / "evidence-extraction.json"),
        "research_questions": system_queue_summary(paths.root, queue_dir / "research-questions.json"),
    }
    payload = {
        "created": utc_timestamp(),
        "purpose": "Whole-system dashboard for the cloud-first genealogy research pipeline.",
        "source_conversion": build_system_source_conversion_summary(prep_manifest, raw_cloud, source_usability),
        "research_readiness": build_system_research_readiness_summary(paths.root, source_usability, research_analyzer),
        "page_upgrades": build_system_page_upgrade_summary(relevance_feedback, research_analyzer),
        "queues": queues,
        "storage": build_system_storage_summary(raw_cloud, derived_assets),
        "final_site": build_system_final_site_summary(paths.root),
        "storage_lifecycle": build_system_lifecycle_summary(paths.root),
        "recent_automation": build_system_recent_automation_summary(paths.root),
        "blockers": blockers or [],
    }
    payload["next_actions"] = build_system_next_actions(payload)
    return payload


def build_system_next_actions(payload: dict[str, object]) -> list[dict[str, object]]:
    queues = payload.get("queues", {})
    source_conversion = payload.get("source_conversion", {})
    page_upgrades = payload.get("page_upgrades", {})
    lifecycle = payload.get("storage_lifecycle", {})
    actions: list[dict[str, object]] = []

    def add(
        area: str,
        priority: str,
        reason: str,
        next_step: str,
        *,
        count: int = 0,
        queue: str = "",
    ) -> None:
        action: dict[str, object] = {
            "area": area,
            "priority": priority,
            "reason": reason,
            "next_step": next_step,
        }
        if count:
            action["count"] = count
        if queue:
            action["queue"] = queue
        actions.append(action)

    source_prep = queue_payload(queues, "source_prep")
    source_prep_open = queue_status_total(
        source_prep,
        ("todo", "claimed", "in_progress", "rough_discovery", "needs_reread"),
    )
    if source_prep_open:
        add(
            "source_prep",
            "high",
            f"{source_prep_open} source-prep task(s) still need page-level conversion or review.",
            "Complete source-prep work before downstream conversion QA and extraction can progress.",
            count=source_prep_open,
            queue=str(source_prep.get("path", "")),
        )

    conversion_qa = queue_payload(queues, "conversion_qa")
    conversion_qa_open = queue_status_total(conversion_qa, ("todo", "claimed", "in_progress"))
    if conversion_qa_open:
        add(
            "conversion_qa",
            "high",
            f"{conversion_qa_open} converted source(s) are waiting for conversion-QA triage.",
            "Run conversion-QA triage and mark completed tasks done so extraction can use reviewed pages.",
            count=conversion_qa_open,
            queue=str(conversion_qa.get("path", "")),
        )

    evidence_extraction = queue_payload(queues, "evidence_extraction")
    blocked_extraction = queue_status_total(evidence_extraction, ("blocked_pending_conversion_qa",))
    if blocked_extraction:
        add(
            "evidence_extraction",
            "high",
            f"{blocked_extraction} evidence-extraction task(s) are blocked by the conversion-QA gate.",
            "Finish the matching conversion-QA tasks, then regenerate agent queues to release extraction.",
            count=blocked_extraction,
            queue=str(evidence_extraction.get("path", "")),
        )
    else:
        extraction_open = queue_status_total(evidence_extraction, ("todo", "claimed", "in_progress"))
        if extraction_open:
            add(
                "evidence_extraction",
                "medium",
                f"{extraction_open} reviewed chunk(s) are ready for staged source-packet or claim extraction.",
                "Create staging drafts under research/_staging before proof review or canonical promotion.",
                count=extraction_open,
                queue=str(evidence_extraction.get("path", "")),
            )

    research_questions = queue_payload(queues, "research_questions")
    question_open = queue_status_total(research_questions, ("todo", "claimed", "in_progress"))
    if question_open:
        add(
            "research_questions",
            "medium",
            f"{question_open} research-analyzer question task(s) are queued.",
            "Work the prompt packets and keep results in research questions or staging drafts.",
            count=question_open,
            queue=str(research_questions.get("path", "")),
        )

    active_upgrades = safe_int(dict_value(page_upgrades, "active_request_count"), 0)
    if active_upgrades:
        add(
            "page_upgrades",
            "medium",
            f"{active_upgrades} page-level conversion upgrade request(s) are active.",
            "Route high-value pages through advanced conversion or reread before deeper extraction.",
            count=active_upgrades,
        )

    conversion_not_started = safe_int(
        dict_value(dict_value(source_conversion, "usability_status_counts", {}), "conversion_not_started"),
        0,
    )
    if conversion_not_started:
        add(
            "source_conversion",
            "low",
            f"{conversion_not_started} source(s) are registered but not yet converted.",
            "Prepare the next bounded raw-source batch while preserving originals in R2.",
            count=conversion_not_started,
        )

    deaccession_candidates = safe_int(dict_value(lifecycle, "deaccession_candidate_count"), 0)
    if deaccession_candidates:
        add(
            "storage_lifecycle",
            "low",
            f"{deaccession_candidates} page(s) are marked as non-destructive deaccession candidates.",
            "Review candidate records manually before any future R2 lifecycle action.",
            count=deaccession_candidates,
        )

    return actions[:6]


def build_system_source_conversion_summary(
    prep_manifest: dict[str, object],
    raw_cloud: dict[str, object],
    source_usability: dict[str, object],
) -> dict[str, object]:
    sources = prep_manifest.get("sources", [])
    if not isinstance(sources, list):
        sources = []
    cloud_files = raw_cloud.get("files", [])
    if not isinstance(cloud_files, list):
        cloud_files = []
    usability_summary = source_usability.get("summary", {}) if isinstance(source_usability, dict) else {}
    status_counts = usability_summary.get("status_counts", {}) if isinstance(usability_summary, dict) else {}
    if not isinstance(status_counts, dict):
        status_counts = {}
    return {
        "source_count": len(sources),
        "local_source_count": len([source for source in sources if isinstance(source, dict) and source.get("local_cache") != "missing"]),
        "cloud_registered_count": len([source for source in sources if isinstance(source, dict) and source.get("local_cache") == "missing"]),
        "r2_raw_file_count": len(cloud_files),
        "r2_raw_total_bytes": sum(safe_int(item.get("bytes"), 0) for item in cloud_files if isinstance(item, dict)),
        "converted_file_count": sum(
            len(source.get("converted_sources", []))
            for source in sources
            if isinstance(source, dict) and isinstance(source.get("converted_sources", []), list)
        ),
        "conversion_job_count": sum(
            len(source.get("conversion_jobs", []))
            for source in sources
            if isinstance(source, dict) and isinstance(source.get("conversion_jobs", []), list)
        ),
        "usability_status_counts": status_counts,
    }


def build_system_research_readiness_summary(
    root: Path,
    source_usability: dict[str, object],
    research_analyzer: dict[str, object],
) -> dict[str, object]:
    sources = source_usability.get("sources", []) if isinstance(source_usability, dict) else []
    if not isinstance(sources, list):
        sources = []
    qa_pages = read_json_payload(root / "research" / "_conversion-review" / "qc-pages.json", {"pages": []}).get("pages", [])
    if not isinstance(qa_pages, list):
        qa_pages = []
    return {
        "usable_source_count": len(
            [
                source
                for source in sources
                if isinstance(source, dict) and str(source.get("status", "")).startswith("usable")
            ]
        ),
        "sources_needing_conversion_or_repair": len(
            [
                source
                for source in sources
                if isinstance(source, dict)
                and str(source.get("status", ""))
                in {"conversion_not_started", "conversion_in_progress", "needs_chunking", "usable_with_page_repairs"}
            ]
        ),
        "qc_page_count": len(qa_pages),
        "analyzer_pages_scanned": safe_int(research_analyzer.get("pages_scanned"), 0),
        "analyzer_upgrade_candidates": safe_int(research_analyzer.get("upgrade_candidates"), 0),
        "analyzer_staging_opportunity_pages": safe_int(research_analyzer.get("staging_opportunity_pages"), 0),
        "analyzer_staging_recommendations": research_analyzer.get("staging_recommendation_counts", {}),
        "analyzer_staging_readiness": research_analyzer.get("staging_readiness_counts", {}),
        "staging_counts": {
            "source_packets": count_markdown_files(root / "research" / "_staging" / "source-packets"),
            "claims": count_markdown_files(root / "research" / "_staging" / "claims"),
            "relationships": count_markdown_files(root / "research" / "_staging" / "relationships"),
            "identity": count_markdown_files(root / "research" / "_staging" / "identity"),
        },
    }


def build_system_page_upgrade_summary(
    relevance_feedback: dict[str, object],
    research_analyzer: dict[str, object],
) -> dict[str, object]:
    hints = relevance_feedback.get("hints", []) if isinstance(relevance_feedback, dict) else []
    if not isinstance(hints, list):
        hints = []
    active_hints = [
        hint
        for hint in hints
        if isinstance(hint, dict)
        and str(hint.get("status", "active")).strip().lower() in SOURCE_RELEVANCE_ACTIVE_STATUSES
    ]
    return {
        "active_request_count": len(active_hints),
        "critical_or_high_count": len(
            [
                hint
                for hint in active_hints
                if str(hint.get("relevance", "")).strip().lower() in {"critical", "high"}
            ]
        ),
        "pro_or_reread_count": len(
            [
                hint
                for hint in active_hints
                if str(hint.get("requested_treatment", "")).strip().lower() in {"pro", "pro_with_crops", "reread"}
            ]
        ),
        "analyzer_upgrade_candidates": safe_int(research_analyzer.get("upgrade_candidates"), 0),
        "analyzer_upgrade_requests_written": safe_int(research_analyzer.get("upgrade_requests_written"), 0),
    }


def build_system_storage_summary(raw_cloud: dict[str, object], derived_assets: dict[str, object]) -> dict[str, object]:
    raw_files = raw_cloud.get("files", []) if isinstance(raw_cloud, dict) else []
    asset_files = derived_assets.get("files", []) if isinstance(derived_assets, dict) else []
    if not isinstance(raw_files, list):
        raw_files = []
    if not isinstance(asset_files, list):
        asset_files = []
    return {
        "r2_raw_file_count": len(raw_files),
        "r2_raw_total_bytes": sum(safe_int(item.get("bytes"), 0) for item in raw_files if isinstance(item, dict)),
        "r2_derived_asset_count": len(asset_files),
        "r2_derived_asset_bytes": sum(safe_int(item.get("bytes"), 0) for item in asset_files if isinstance(item, dict)),
        "contract": "R2 stores raw originals and durable binary assets; GitHub stores JSON, Markdown, manifests, queues, chunks, staging/proof data, and final HTML/build files.",
    }


def build_system_final_site_summary(root: Path) -> dict[str, object]:
    candidates = [root / "site", root / "dist", root / "public"]
    existing = [relative_to_root(path, root) for path in candidates if path.exists()]
    return {
        "status": "structure_present" if existing else "not_started",
        "candidate_roots": existing,
        "html_file_count": sum(count_files_with_suffix(path, ".html") for path in candidates if path.exists()),
    }


def build_system_lifecycle_summary(root: Path) -> dict[str, object]:
    lifecycle_path = root / "research" / "_indexes" / "storage-lifecycle.json"
    payload = read_json_payload(lifecycle_path, {})
    pages = payload.get("pages", []) if isinstance(payload, dict) else []
    if not isinstance(pages, list):
        pages = []
    status_counts = count_task_statuses(
        [{"status": str(page.get("retention_status", "unknown"))} for page in pages if isinstance(page, dict)]
    )
    candidate_records = payload.get("deaccession_records", []) if isinstance(payload, dict) else []
    if not isinstance(candidate_records, list):
        candidate_records = []
    return {
        "status": "active" if lifecycle_path.exists() else "not_started",
        "index": relative_to_root(lifecycle_path, root),
        "page_rank_count": len(pages),
        "retention_status_counts": status_counts,
        "preserve_raw_count": status_counts.get("preserve_raw", 0),
        "cold_retain_count": status_counts.get("cold_retain", 0),
        "deaccession_candidate_count": status_counts.get("deaccession_candidate", 0),
        "deaccession_record_count": len(candidate_records),
    }


def build_system_recent_automation_summary(root: Path) -> dict[str, object]:
    automation_dir = root / "research" / "_automation"
    states: dict[str, object] = {}
    for path in sorted(automation_dir.glob("*.json")) if automation_dir.exists() else []:
        payload = read_json_payload(path, {})
        states[path.stem] = {
            "path": relative_to_root(path, root),
            "created": payload.get("created", ""),
            "mode": payload.get("mode", ""),
            "blockers": payload.get("blockers", []),
        }
    return states


def system_queue_summary(root: Path, path: Path) -> dict[str, object]:
    summary = queue_summary(path)
    summary["path"] = relative_to_root(path, root)
    return summary


def queue_payload(queues: object, name: str) -> dict[str, object]:
    if not isinstance(queues, dict):
        return {}
    queue = queues.get(name, {})
    return queue if isinstance(queue, dict) else {}


def queue_status_total(queue: dict[str, object], statuses: tuple[str, ...]) -> int:
    counts = queue.get("status_counts", {})
    if not isinstance(counts, dict):
        return 0
    return sum(safe_int(counts.get(status), 0) for status in statuses)


def count_files_with_suffix(path: Path, suffix: str) -> int:
    if not path.exists():
        return 0
    return sum(1 for item in path.rglob(f"*{suffix}") if item.is_file())


def build_system_status_markdown(payload: dict[str, object]) -> str:
    source_conversion = payload.get("source_conversion", {})
    research_readiness = payload.get("research_readiness", {})
    page_upgrades = payload.get("page_upgrades", {})
    storage = payload.get("storage", {})
    final_site = payload.get("final_site", {})
    lifecycle = payload.get("storage_lifecycle", {})
    blockers = payload.get("blockers", [])
    blocker_lines = [f"- {blocker}" for blocker in blockers] if isinstance(blockers, list) and blockers else ["- None"]
    next_actions = payload.get("next_actions", [])
    action_lines = [
        "- **"
        + str(dict_value(action, "priority", "medium"))
        + "** `"
        + str(dict_value(action, "area", "unknown"))
        + "`: "
        + str(dict_value(action, "next_step", ""))
        + " ("
        + str(dict_value(action, "reason", ""))
        + ")"
        for action in next_actions
        if isinstance(action, dict)
    ]
    if not action_lines:
        action_lines = ["- None"]
    queues = payload.get("queues", {})
    queue_rows = [
        "| Queue | Tasks | Status Counts |",
        "| --- | ---: | --- |",
    ]
    if isinstance(queues, dict):
        for name, queue in sorted(queues.items()):
            if not isinstance(queue, dict):
                continue
            queue_rows.append(
                "| "
                + " | ".join(
                    [
                        markdown_table_cell(name),
                        markdown_table_cell(queue.get("task_count", 0)),
                        markdown_table_cell(format_status_counts(queue.get("status_counts", {}))),
                    ]
                )
                + " |"
            )
    return f"""# System Dashboard

Generated: {payload.get("created", "")}

## Source Conversion

- Sources: {dict_value(source_conversion, "source_count")}
- Local source cache entries: {dict_value(source_conversion, "local_source_count")}
- Cloud-registered sources awaiting local cache: {dict_value(source_conversion, "cloud_registered_count")}
- Conversion jobs: {dict_value(source_conversion, "conversion_job_count")}
- Converted Markdown files: {dict_value(source_conversion, "converted_file_count")}
- Usability: {format_status_counts(dict_value(source_conversion, "usability_status_counts", {}))}

## Research Readiness

- Usable sources: {dict_value(research_readiness, "usable_source_count")}
- Sources needing conversion or page repair: {dict_value(research_readiness, "sources_needing_conversion_or_repair")}
- QC pages: {dict_value(research_readiness, "qc_page_count")}
- Analyzer pages scanned: {dict_value(research_readiness, "analyzer_pages_scanned")}
- Analyzer upgrade candidates: {dict_value(research_readiness, "analyzer_upgrade_candidates")}
- Analyzer staging opportunity pages: {dict_value(research_readiness, "analyzer_staging_opportunity_pages")}
- Analyzer staging recommendations: {format_status_counts(dict_value(research_readiness, "analyzer_staging_recommendations", {}))}
- Analyzer staging readiness: {format_status_counts(dict_value(research_readiness, "analyzer_staging_readiness", {}))}
- Staging drafts: {format_status_counts(dict_value(research_readiness, "staging_counts", {}))}

## Page Upgrades

- Active page upgrade requests: {dict_value(page_upgrades, "active_request_count")}
- Critical or high relevance requests: {dict_value(page_upgrades, "critical_or_high_count")}
- Pro/reread requests: {dict_value(page_upgrades, "pro_or_reread_count")}
- Analyzer requests written last run: {dict_value(page_upgrades, "analyzer_upgrade_requests_written")}

## Next Actions

{chr(10).join(action_lines)}

## Queues

{chr(10).join(queue_rows)}

## Storage

- R2 raw files: {dict_value(storage, "r2_raw_file_count")}
- R2 raw bytes: {dict_value(storage, "r2_raw_total_bytes")}
- R2 durable derived assets: {dict_value(storage, "r2_derived_asset_count")}
- R2 durable derived asset bytes: {dict_value(storage, "r2_derived_asset_bytes")}
- Storage lifecycle status: {dict_value(lifecycle, "status")}
- Storage lifecycle ranked pages: {dict_value(lifecycle, "page_rank_count")}
- Storage lifecycle retention: {format_status_counts(dict_value(lifecycle, "retention_status_counts", {}))}
- Deaccession candidates: {dict_value(lifecycle, "deaccession_candidate_count")}
- Deaccession records: {dict_value(lifecycle, "deaccession_record_count")}

## Final Site

- Status: {dict_value(final_site, "status")}
- HTML files: {dict_value(final_site, "html_file_count")}

## Blockers

{chr(10).join(blocker_lines)}
"""


def dict_value(payload: object, key: str, default: object = 0) -> object:
    if not isinstance(payload, dict):
        return default
    return payload.get(key, default)


def format_status_counts(value: object) -> str:
    if not isinstance(value, dict) or not value:
        return "none"
    return ", ".join(f"{key}: {value[key]}" for key in sorted(value))


def read_json_payload(path: Path, default: dict[str, object] | None = None) -> dict[str, object]:
    if not path.exists():
        return dict(default or {})
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return dict(default or {})
    return payload if isinstance(payload, dict) else dict(default or {})


def queue_summary(path: Path) -> dict[str, object]:
    payload = read_json_payload(path, {"tasks": []})
    tasks = payload.get("tasks", [])
    if not isinstance(tasks, list):
        tasks = []
    return {
        "path": str(path),
        "task_count": len(tasks),
        "status_counts": payload.get("status_counts", count_task_statuses([task for task in tasks if isinstance(task, dict)])),
    }


def r2_source_intake_state_path(root: Path) -> Path:
    return root.resolve() / "research" / "_automation" / "r2-source-intake-state.json"


def write_r2_source_intake_state(root: Path, summary: dict[str, object]) -> Path:
    output_path = r2_source_intake_state_path(root)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    return output_path


def monitor_r2_source_intake(
    root: Path,
    *,
    limit: int | None = None,
    dry_run: bool = False,
) -> dict[str, object]:
    paths = WikiPaths(root.resolve())
    config = load_raw_cloud_config(paths.root, require_credentials=True)
    previous_manifest = read_tracked_raw_cloud_manifest(paths.root)
    previous_by_path = raw_cloud_manifest_files_by_path(previous_manifest)
    remote_manifest = build_raw_cloud_manifest_from_remote(paths.root, config, limit=limit)
    remote_by_path = raw_cloud_manifest_files_by_path(remote_manifest)

    new_paths = sorted(path for path in remote_by_path if path not in previous_by_path)
    removed_paths = sorted(path for path in previous_by_path if path not in remote_by_path)
    changed_paths = sorted(
        path
        for path, current in remote_by_path.items()
        if path in previous_by_path and raw_cloud_file_changed(previous_by_path[path], current)
    )

    r2_manifest_path = paths.raw / "r2-raw-sources.json"
    source_manifest_path = paths.raw / "source-prep-manifest.json"
    if not dry_run:
        r2_manifest_path.parent.mkdir(parents=True, exist_ok=True)
        r2_manifest_path.write_text(json.dumps(remote_manifest, indent=2, ensure_ascii=False), encoding="utf-8")
        source_manifest_path = write_source_prep_index(paths.root)

    summary: dict[str, object] = {
        "created": utc_timestamp(),
        "mode": "r2-source-intake",
        "root": str(paths.root),
        "dry_run": dry_run,
        "limit": limit or 0,
        "remote_file_count": len(remote_by_path),
        "new_file_count": len(new_paths),
        "changed_file_count": len(changed_paths),
        "removed_file_count": len(removed_paths),
        "new_files": [remote_by_path[path] for path in new_paths],
        "changed_files": [remote_by_path[path] for path in changed_paths],
        "removed_files": [previous_by_path[path] for path in removed_paths],
        "r2_manifest": relative_to_root(r2_manifest_path, paths.root),
        "source_prep_manifest": relative_to_root(source_manifest_path, paths.root),
        "blockers": [],
    }
    if not dry_run:
        state_path = write_r2_source_intake_state(paths.root, summary)
        summary["state"] = relative_to_root(state_path, paths.root)
        append_log(
            paths.research / "log.md",
            f"r2-source-intake | Registered {len(new_paths)} new, {len(changed_paths)} changed, {len(removed_paths)} removed remote source(s)",
        )
    return summary


def raw_cloud_file_changed(previous: dict[str, object], current: dict[str, object]) -> bool:
    for key in ("key", "bytes", "sha256", "media_type"):
        if str(previous.get(key, "")).strip() != str(current.get(key, "")).strip():
            return True
    return False


def write_cloud_source_prep_heartbeat_state(root: Path, summary: dict[str, object]) -> Path:
    paths = WikiPaths(root.resolve())
    output_path = paths.research / "_automation" / "cloud-source-prep-heartbeat-state.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    return output_path


def cloud_source_prep_heartbeat(
    root: Path,
    *,
    restore_raw: bool = True,
    upload_assets: bool = True,
    research_analyzer: bool = True,
    research_analyzer_limit: int = 5,
    research_question_limit: int = 5,
    conversion_qc: bool = False,
    conversion_only: bool = False,
    page_range: str | None = None,
    restore_limit: int | None = None,
    pages_per_job: int = 25,
    new_pages_limit: int = 0,
    batch_pages: int = 1,
    queue_limit: int = 80,
    stale_minutes: int = 360,
    max_chars: int = 12000,
    fastlane_limit: int = 0,
    fastlane_scan_limit: int = 250,
    dry_run: bool = False,
) -> dict[str, object]:
    paths = WikiPaths(root.resolve())
    summary: dict[str, object] = {
        "created": utc_timestamp(),
        "mode": "cloud-first-source-prep-heartbeat",
        "root": str(paths.root),
        "r2": {
            "restore_raw": restore_raw,
            "upload_assets": upload_assets,
        },
        "settings": {
            "conversion_qc": conversion_qc,
            "conversion_only": conversion_only,
            "research_analyzer": research_analyzer,
            "research_analyzer_limit": research_analyzer_limit,
            "research_question_limit": research_question_limit,
            "page_range": page_range or "",
            "restore_limit": restore_limit or 0,
            "pages_per_job": pages_per_job,
            "new_pages_limit": new_pages_limit,
            "batch_pages": batch_pages,
            "queue_limit": queue_limit,
            "stale_minutes": stale_minutes,
            "fastlane_limit": fastlane_limit,
            "dry_run": dry_run,
        },
        "steps": [],
        "blockers": [],
    }

    def record_step(name: str, status: str, detail: object = "") -> None:
        step: dict[str, object] = {"name": name, "status": status}
        if detail:
            step["detail"] = detail
        cast_steps = summary.setdefault("steps", [])
        if isinstance(cast_steps, list):
            cast_steps.append(step)

    if restore_raw:
        try:
            if dry_run:
                record_step("r2-source-intake", "skipped-dry-run")
            else:
                intake_report = monitor_r2_source_intake(paths.root)
                record_step("r2-source-intake", "ran", intake_report)
        except Exception as exc:
            summary["blockers"].append(f"r2-source-intake: {exc}")
            record_step("r2-source-intake", "failed", str(exc))

        try:
            config = load_raw_cloud_config(paths.root, require_credentials=not dry_run)
            if dry_run:
                record_step("raw-cloud restore", "skipped-dry-run")
            else:
                report = restore_raw_from_cloud(paths.root, config, limit=restore_limit)
                record_step("raw-cloud restore", "ran", report)
        except Exception as exc:
            summary["blockers"].append(f"raw-cloud restore: {exc}")
            record_step("raw-cloud restore", "failed", str(exc))

    try:
        prepared = prepare_raw_sources(
            paths.root,
            page_range=page_range,
            pages_per_job=pages_per_job,
            new_pages_limit=new_pages_limit,
            max_chars=max_chars,
        )
        record_step("prepare-sources", "ran", {"prepared_sources": len(prepared)})
    except Exception as exc:
        summary["blockers"].append(f"prepare-sources: {exc}")
        record_step("prepare-sources", "failed", str(exc))

    if conversion_only:
        record_step("conversion-qc", "skipped", "conversion-only run")
    elif conversion_qc:
        try:
            qc_paths = write_post_conversion_qc(paths.root)
            record_step("conversion-qc", "ran", {"written": [relative_to_root(path, paths.root) for path in qc_paths]})
        except Exception as exc:
            summary["blockers"].append(f"conversion-qc: {exc}")
            record_step("conversion-qc", "failed", str(exc))
    else:
        record_step("conversion-qc", "skipped", "disabled; use source-relevance feedback for research-to-conversion routing")

    if conversion_only:
        record_step("agent-queues", "skipped", "conversion-only run")
    else:
        try:
            queue_paths = write_agent_queues(paths.root, stale_minutes=stale_minutes, include_conversion_qa=conversion_qc)
            record_step("agent-queues", "ran", {"written": [relative_to_root(path, paths.root) for path in queue_paths]})
        except Exception as exc:
            summary["blockers"].append(f"agent-queues: {exc}")
            record_step("agent-queues", "failed", str(exc))

    try:
        batch_path = write_source_prep_batches(
            paths.root,
            max_pages=batch_pages,
            limit=queue_limit,
            stale_minutes=stale_minutes,
        )
        record_step("source-prep-batches", "ran", {"written": relative_to_root(batch_path, paths.root)})
    except Exception as exc:
        summary["blockers"].append(f"source-prep-batches: {exc}")
        record_step("source-prep-batches", "failed", str(exc))

    if fastlane_limit > 0:
        try:
            if dry_run:
                record_step("source-prep-fastlane", "skipped-dry-run")
            else:
                fastlane = source_prep_fastlane_run(
                    paths.root,
                    limit=fastlane_limit,
                    scan_limit=fastlane_scan_limit,
                    agent="cloud-source-prep-fastlane",
                    stale_minutes=stale_minutes,
                )
                record_step("source-prep-fastlane", "ran", fastlane)
        except Exception as exc:
            summary["blockers"].append(f"source-prep-fastlane: {exc}")
            record_step("source-prep-fastlane", "failed", str(exc))

    if conversion_only:
        record_step("source-status", "skipped", "conversion-only run")
    else:
        try:
            source_status_paths = write_source_usability_report(paths.root)
            record_step(
                "source-status",
                "ran",
                {"written": [relative_to_root(path, paths.root) for path in source_status_paths]},
            )
        except Exception as exc:
            summary["blockers"].append(f"source-status: {exc}")
            record_step("source-status", "failed", str(exc))

    if conversion_only:
        record_step("research-analyzer", "skipped", "conversion-only run")
    elif not research_analyzer:
        record_step("research-analyzer", "skipped", "disabled")
    else:
        try:
            analyzer_summary = research_analyzer_run(
                paths.root,
                limit=research_analyzer_limit,
                question_limit=research_question_limit,
                dry_run=dry_run,
            )
            record_step("research-analyzer", "ran", analyzer_summary)
            if analyzer_summary.get("blockers"):
                summary["blockers"].extend(
                    f"research-analyzer: {blocker}" for blocker in analyzer_summary.get("blockers", [])
                )
        except Exception as exc:
            summary["blockers"].append(f"research-analyzer: {exc}")
            record_step("research-analyzer", "failed", str(exc))

    if upload_assets:
        try:
            config = load_raw_cloud_config(paths.root, require_credentials=not dry_run)
            asset_report = upload_derived_assets_to_cloud(paths.root, config, dry_run=dry_run)
            record_step("raw-cloud asset-upload", "ran", asset_report)
        except Exception as exc:
            summary["blockers"].append(f"raw-cloud asset-upload: {exc}")
            record_step("raw-cloud asset-upload", "failed", str(exc))

    queue_dir = paths.research / "_agent-queues"
    summary["queues"] = {"source_prep_batches": system_queue_summary(paths.root, queue_dir / "source-prep-batches.json")}
    if not conversion_only:
        cast_queues = summary["queues"]
        if isinstance(cast_queues, dict):
            cast_queues.update(
                {
                    "source_prep": system_queue_summary(paths.root, queue_dir / "source-prep.json"),
                    "conversion_qa": system_queue_summary(paths.root, queue_dir / "conversion-qa.json"),
                    "evidence_extraction": system_queue_summary(paths.root, queue_dir / "evidence-extraction.json"),
                    "research_questions": system_queue_summary(paths.root, queue_dir / "research-questions.json"),
                }
            )
    summary["finished"] = utc_timestamp()
    state_path = write_cloud_source_prep_heartbeat_state(paths.root, summary)
    summary["state_path"] = relative_to_root(state_path, paths.root)
    append_log(paths.research / "log.md", f"cloud-source-prep-heartbeat | Wrote {summary['state_path']}")
    return summary


GITHUB_DATABASE_INCLUDE_PATHS = (
    "raw/source-prep-manifest.json",
    "raw/r2-storage.json",
    "raw/r2-raw-sources.json",
    "raw/r2-derived-assets.json",
    "raw/codex-conversion-jobs",
    "raw/discovery",
    "raw/converted",
    "raw/chunks",
    "research",
    "wiki",
)
SOURCE_CONVERSION_INCLUDE_PATHS = (
    "raw/source-prep-manifest.json",
    "raw/r2-storage.json",
    "raw/r2-raw-sources.json",
    "raw/r2-derived-assets.json",
    "raw/codex-conversion-jobs",
    "raw/discovery",
    "raw/converted",
    "raw/chunks",
    "research/_agent-queues/source-prep-batches.json",
    "research/_agent-queues/source-prep-discovery.json",
    "research/_agent-queues/task-state.json",
    "research/_automation",
    "research/log.md",
)
GITHUB_DATABASE_FORBIDDEN_PREFIXES = (
    "raw/sources/",
    "raw/assets/",
    "research/_assets/",
    ".genealogy/",
    "obsidian-offline/",
)
GITHUB_DATABASE_FORBIDDEN_JOB_FRAGMENTS = (
    "/source/",
    "/page-images/",
    "/extracted-images/",
    "/audio-transcription/",
    "/video-frames/",
)


def run_git(root: Path, args: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        ["git", *args],
        cwd=root,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if check and result.returncode != 0:
        detail = (result.stderr or result.stdout).strip()
        raise RuntimeError(f"git {' '.join(args)} failed: {detail}")
    return result


def github_database_forbidden_path(path: str) -> bool:
    normalized = path.replace("\\", "/")
    if any(normalized.startswith(prefix) for prefix in GITHUB_DATABASE_FORBIDDEN_PREFIXES):
        return True
    if normalized.startswith("raw/codex-conversion-jobs/"):
        return any(fragment in normalized for fragment in GITHUB_DATABASE_FORBIDDEN_JOB_FRAGMENTS)
    return False


def sync_github_database(
    root: Path,
    *,
    message: str = "",
    dry_run: bool = False,
    no_push: bool = False,
    source_conversion_only: bool = False,
) -> dict[str, object]:
    paths = WikiPaths(root.resolve())
    run_git(paths.root, ["rev-parse", "--show-toplevel"])
    cached = run_git(paths.root, ["diff", "--cached", "--quiet"], check=False)
    if cached.returncode != 0:
        raise RuntimeError("Refusing to sync because staged changes already exist.")

    include_paths = SOURCE_CONVERSION_INCLUDE_PATHS if source_conversion_only else GITHUB_DATABASE_INCLUDE_PATHS
    existing = [path for path in include_paths if (paths.root / path).exists()]
    summary: dict[str, object] = {
        "dry_run": dry_run,
        "no_push": no_push,
        "source_conversion_only": source_conversion_only,
        "included": existing,
        "staged": [],
        "committed": False,
        "pushed": False,
    }
    if not existing:
        return summary

    if dry_run:
        add_args = ["add", "--dry-run", "-A"]
        if source_conversion_only:
            add_args.append("-f")
        add_args.extend(["--", *existing])
        planned = run_git(paths.root, add_args)
        summary["planned"] = [line for line in planned.stdout.splitlines() if line.strip()]
        return summary

    add_args = ["add", "-A"]
    if source_conversion_only:
        add_args.append("-f")
    add_args.extend(["--", *existing])
    run_git(paths.root, add_args)
    staged = run_git(paths.root, ["diff", "--cached", "--name-only"]).stdout.splitlines()
    summary["staged"] = staged
    if not staged:
        return summary

    forbidden = [path for path in staged if github_database_forbidden_path(path)]
    if forbidden:
        run_git(paths.root, ["restore", "--staged", "--", *forbidden], check=False)
        if not source_conversion_only:
            raise RuntimeError("Refusing to commit R2-only or local-cache paths: " + ", ".join(forbidden))
        summary["unstaged_forbidden"] = forbidden
        staged = run_git(paths.root, ["diff", "--cached", "--name-only"]).stdout.splitlines()
        summary["staged"] = staged
        if not staged:
            return summary

    if not message.strip():
        message = f"Sync genealogy GitHub database {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    run_git(paths.root, ["commit", "-m", message])
    summary["committed"] = True
    if not no_push:
        run_git(paths.root, ["push"])
        summary["pushed"] = True
    return summary


def build_evidence_extraction_agent_tasks(root: Path) -> list[dict[str, object]]:
    tasks: list[dict[str, object]] = []
    qc_blocked_by_source = load_qc_blocked_pages(root)
    task_state = load_agent_task_state(root)
    for manifest_path in sorted((root / "raw" / "chunks").glob("*/manifest.json")):
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        converted_file = str(manifest.get("converted_file", ""))
        source_slug = slug(Path(converted_file).stem)
        conversion_qa_done = conversion_qa_is_done(task_state, converted_file)
        for chunk in manifest.get("chunks", []):
            if not isinstance(chunk, dict):
                continue
            chunk_id = str(chunk.get("chunk_id", ""))
            page_start = int(chunk.get("page_start") or 0)
            page_end = int(chunk.get("page_end") or page_start or 0)
            blocked_pages = qc_blocked_pages_for_range(
                qc_blocked_by_source.get(converted_file, {}),
                page_start,
                page_end,
            )
            pending_conversion_qa = not blocked_pages and not conversion_qa_done
            task = {
                "task_id": f"evidence-extraction:{chunk_id}",
                "queue": "evidence-extraction",
                "role": "evidence_extractor",
                "skill": "genealogy-claim-extraction",
                "status": (
                    "blocked_needs_reread"
                    if blocked_pages
                    else "blocked_pending_conversion_qa"
                    if pending_conversion_qa
                    else "todo"
                ),
                "chunk_id": chunk_id,
                "chunk_path": str(chunk.get("path", "")),
                "converted_file": converted_file,
                "chunk_manifest": relative_to_root(manifest_path, root),
                "source": str(manifest.get("source", "")),
                "source_sha256": str(manifest.get("source_sha256", "")),
                "page_start": page_start,
                "page_end": page_end,
                "staging_dir": "research/_staging",
            }
            if blocked_pages:
                task.update(
                    {
                        "blocked_pages": blocked_pages,
                        "block_reason": "post_conversion_qc_hold",
                        "qc_page_queue": f"research/_conversion-review/page-queues/{source_slug}.md",
                        "qc_corrections": f"research/_conversion-review/corrections/{source_slug}.md",
                    }
                )
            elif pending_conversion_qa:
                task.update(
                    {
                        "block_reason": "pending_conversion_qa",
                        "conversion_qa_task_id": conversion_qa_task_id_for_converted_file(converted_file),
                        "conversion_qa_triage": f"research/_conversion-review/triage/{source_slug}.md",
                        "conversion_qa_page_queue": f"research/_conversion-review/page-queues/{source_slug}.md",
                        "conversion_qa_corrections": f"research/_conversion-review/corrections/{source_slug}.md",
                    }
                )
            task["prompt"] = build_evidence_extraction_agent_prompt(task)
            tasks.append(task)
    return tasks


def build_source_prep_agent_prompt(task: dict[str, object]) -> str:
    repair_section = ""
    if str(task.get("status", "")) == "needs_reread":
        repair_section = f"""
## Repair Context

This page has an existing output file, but it is not trusted by the current source-prep contract.

- Existing output: `{task["output_path"]}`
- Automated quality flags: {", ".join(str(flag) for flag in task.get("quality_flags", [])) or "none"}
- Missing contract sections: {", ".join(str(section) for section in task.get("missing_sections", [])) or "none"}
- QC recommended action: `{task.get("recommended_action", "")}`
- QC quality flags: {", ".join(str(flag) for flag in task.get("qc_quality_flags", [])) or "none"}
- Matched family context: {", ".join(str(term) for term in task.get("matched_terms", [])) or "none"}
- Suspicious readings: {format_suspicious_readings(task.get("suspicious_readings", []))}

Overwrite the assigned page Markdown with a fresh visual conversion. Treat the old output, OCR, and PDF text layers only as hints.
"""
    return f"""# Source Conversion Task

Use `$source-prep-pipeline` and `$historical-document-conversion`.

## Assignment

- Role: `{task["role"]}`
- Job manifest: `{task["job_manifest"]}`
- Work order: `{task["work_order"]}`
- Source: `{task["source"]}`
- Page image: `{task["page_image"]}`
- Page: {task["page"]}
- Output Markdown: `{task["output_path"]}`
- Extracted image folder: `{task["image_output_dir"]}`
{repair_section}

## Done When

- The page image has been visually converted, not OCR-copied blindly.
- `{task["output_path"]}` exists and follows the work-order page structure.
- Meaningful photos, signatures, seals, maps, stamps, charts, illustrations, and other visual evidence are cropped into `{task["image_output_dir"]}` and referenced inline when present.
- Literal transcription, translation, interpretation, uncertainty, genealogy leads, and completeness audit are separate.
"""


def build_source_prep_batch_agent_prompt(batch: dict[str, object]) -> str:
    task_ids = [str(task_id) for task_id in batch.get("task_ids", [])]
    quoted_task_ids = " ".join(f'"{task_id}"' for task_id in task_ids)
    validation_commands: list[str] = []
    page_lines = [
        "| Page | Task ID | Page Image | Output Markdown | Extracted Images | Flags | Suspicious Readings |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for page in batch.get("pages", []):
        if not isinstance(page, dict):
            continue
        flags = list(
            dict.fromkeys(
                [str(flag) for flag in page.get("quality_flags", []) or []]
                + [str(flag) for flag in page.get("qc_quality_flags", []) or []]
            )
        )
        combined_flags = ", ".join(flags) or "none"
        suspicious_readings = format_suspicious_readings(page.get("suspicious_readings", []))
        output_path = str(page.get("output_path", "")).strip()
        if output_path:
            validation_commands.append(f'genealogy-wiki source-prep-review-page "{output_path}" --root .')
        page_lines.append(
            "| "
            f"{page.get('page', '')} | "
            f"`{page.get('task_id', '')}` | "
            f"`{page.get('page_image', '')}` | "
            f"`{page.get('output_path', '')}` | "
            f"`{page.get('image_output_dir', '')}` | "
            f"{combined_flags} | "
            f"{suspicious_readings} |"
        )

    repair_section = ""
    if str(batch.get("status", "")) == "needs_reread":
        repair_section = f"""
## Repair Context

These pages have existing output files, but they are not trusted by the current source-prep contract.

- Repair reason: `{batch.get("repair_reason", "")}`
- QC recommended action: `{batch.get("recommended_action", "")}`

Overwrite each assigned page Markdown with a fresh visual conversion. Treat old output, OCR, and PDF text layers only as hints.
"""

    return f"""# Source Conversion Page Assignment

Use `$source-prep-pipeline` and `$historical-document-conversion`.

This assignment is one page, not a quality shortcut. Throughput comes from running more workers, not from assigning multiple pages to one worker.

## Assignment

- Role: `{batch["role"]}`
- Job manifest: `{batch["job_manifest"]}`
- Source: `{batch["source"]}`
- Page: {batch["first_page"]} ({batch["page_count"]} page)
- Status: `{batch["status"]}`
{repair_section}

## Page Work

{chr(10).join(page_lines)}

## Task State

If a dispatcher assigned this page and already claimed the task, do not run task-state commands; the dispatcher owns final task state so parallel workers cannot race. If running this prompt standalone, claim and start the page tasks before editing:

```powershell
genealogy-wiki agent-task claim {quoted_task_ids} --root . --agent "<worker-label>" --no-refresh
genealogy-wiki agent-task start {quoted_task_ids} --root . --agent "<worker-label>" --no-refresh
```

Validate each page output before reporting completion:

```powershell
{chr(10).join(validation_commands)}
```

If running standalone and validation passes, complete the page task:

```powershell
genealogy-wiki agent-task complete {quoted_task_ids} --root . --agent "<worker-label>" --no-refresh
```

If the page is too dense, handwritten, table-heavy, damaged, family-critical, or otherwise likely to lose accuracy in this run, release it with a note instead of guessing.

## Done When

- The page image has been visually converted, not OCR-copied blindly.
- The page has its own output Markdown and extracted-image folder populated as needed.
- Meaningful photos, signatures, seals, maps, stamps, charts, illustrations, and other visual evidence are cropped and referenced inline when present.
- Literal transcription, translation, interpretation, uncertainty, genealogy leads, and completeness audit are separate.
"""


def format_suspicious_readings(readings: object) -> str:
    if not isinstance(readings, list) or not readings:
        return "none"
    formatted = []
    for reading in readings:
        if not isinstance(reading, dict):
            continue
        literal = str(reading.get("literal", "")).strip()
        suspected = str(reading.get("suspected", "")).strip()
        if literal and suspected:
            formatted.append(f"{literal} -> {suspected}")
    return ", ".join(formatted) or "none"


def build_conversion_qa_agent_prompt(task: dict[str, object]) -> str:
    return f"""# Conversion QA Task

Use `$conversion-qa-triage`.

## Assignment

- Role: `{task["role"]}`
- Converted source: `{task["converted_file"]}`
- Chunk manifest: `{task["chunk_manifest"]}`
- Original source: `{task["source"]}`
- Output area: `{task["output_dir"]}`
- Automatic QC triage: `{task["auto_qc_triage"]}`
- Automatic page queue: `{task["auto_qc_page_queue"]}`
- Automatic suspected readings: `{task["auto_qc_corrections"]}`

## Done When

- Automatic QC findings have been checked and refined where needed.
- Family-relevant pages, suspicious readings, likely name drift, table problems, handwriting uncertainty, and missing visual regions are queued under `research/_conversion-review/`.
- Suspected corrections are documented separately from the converted Markdown.
- The task does not promote claims or edit canonical wiki pages.
"""


def build_evidence_extraction_agent_prompt(task: dict[str, object]) -> str:
    hold_section = ""
    if str(task.get("block_reason", "")) == "pending_conversion_qa":
        hold_section = f"""
## Conversion QA Gate

- Status: `{task["status"]}`
- Conversion QA task: `{task.get("conversion_qa_task_id", "")}`
- Expected triage note: `{task.get("conversion_qa_triage", "")}`
- Expected page queue: `{task.get("conversion_qa_page_queue", "")}`
- Expected suspected readings: `{task.get("conversion_qa_corrections", "")}`

Do not extract claims from this chunk until the conversion QA task is completed and the extraction queue is regenerated.
"""
    elif str(task.get("status", "")).startswith("blocked"):
        hold_section = f"""
## QC Hold

- Status: `{task["status"]}`
- Blocked pages: {", ".join(str(page) for page in task.get("blocked_pages", []))}
- Page reread queue: `{task.get("qc_page_queue", "")}`
- Suspected readings: `{task.get("qc_corrections", "")}`

Do not extract claims from this chunk until the blocked page reread is resolved or the chunk is re-queued.
"""
    return f"""# Evidence Extraction Task

Use `$genealogy-claim-extraction`.

## Assignment

- Role: `{task["role"]}`
- Chunk: `{task["chunk_path"]}`
- Converted source: `{task["converted_file"]}`
- Chunk manifest: `{task["chunk_manifest"]}`
- Original source: `{task["source"]}`
- Page range: {task["page_start"]}-{task["page_end"]}
- Staging area: `{task["staging_dir"]}`
{hold_section}

## Done When

- Relevant source packets, atomic claim drafts, relationship candidates, identity/conflict candidates, and research tasks are written under `research/_staging/`.
- Every draft has source path, converted file, chunk/page reference, literal support, conversion confidence/QA concern, uncertainty, and promotion recommendation.
- No canonical wiki pages are edited by this extraction task.
"""


def count_task_statuses(tasks: list[dict[str, object]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for task in tasks:
        status = str(task.get("status", "unknown"))
        counts[status] = counts.get(status, 0) + 1
    return counts


def normalize_job_artifact_reference(root: Path, manifest_path: Path, value: str, fallback_stem: str) -> str:
    if not value:
        return first_existing_job_artifact(root, manifest_path, fallback_stem)

    path = Path(value)
    if not path.is_absolute():
        return value
    if path.exists():
        return value

    normalized = value.replace("\\", "/")
    marker = "/raw/"
    if marker in normalized:
        candidate = root / normalized.split(marker, 1)[1]
        if candidate.exists():
            return relative_to_root(candidate, root)

    return first_existing_job_artifact(root, manifest_path, fallback_stem)


def first_existing_job_artifact(root: Path, manifest_path: Path, fallback_stem: str) -> str:
    fallback = manifest_path.parent / fallback_stem
    if fallback.exists():
        return relative_to_root(fallback, root)
    matches = sorted(fallback.parent.glob(f"{fallback.name}.*"))
    if matches:
        return relative_to_root(matches[0], root)
    return relative_to_root(fallback, root)


def relative_to_root(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def staged_source_filename(source_file: Path, digest: str, max_stem_length: int = 48) -> str:
    stem = slug(source_file.stem)[:max_stem_length] or "source"
    suffix = source_file.suffix.lower()
    return f"{stem}-{digest[:12]}{suffix}"


def relative_path(from_dir: Path, to_path: Path) -> str:
    return Path(os.path.relpath(to_path.resolve(), from_dir.resolve())).as_posix()


def append_index_reference(index_path: Path, section: str, wiki_link: str) -> None:
    index_path.parent.mkdir(parents=True, exist_ok=True)
    text = read_text(index_path)
    if not text:
        text = RESEARCH_INDEX_TEMPLATE if index_path.name == "index.md" and index_path.parent.name == "research" else INDEX_TEMPLATE
    entry = f"- {wiki_link}"
    if entry in text:
        return

    heading = f"## {section}"
    if heading not in text:
        text = text.rstrip() + f"\n\n{heading}\n\n{entry}\n"
        index_path.write_text(text, encoding="utf-8")
        return

    heading_start = text.index(heading)
    body_start = heading_start + len(heading)
    next_heading = re.search(r"\n## ", text[body_start:])
    insert_at = body_start + next_heading.start() if next_heading else len(text)
    before = text[:insert_at].rstrip()
    after = text[insert_at:].lstrip("\n")
    text = f"{before}\n\n{entry}\n\n{after}" if after else f"{before}\n\n{entry}\n"
    index_path.write_text(text, encoding="utf-8")


def remove_index_reference(index_path: Path, wiki_link: str) -> None:
    text = read_text(index_path)
    if not text:
        return
    entry = f"- {wiki_link}"
    lines = [line for line in text.splitlines() if line.strip() != entry]
    cleaned = "\n".join(lines).rstrip() + "\n"
    if cleaned != text:
        index_path.write_text(cleaned, encoding="utf-8")


def claim_pages(paths: WikiPaths) -> list[Path]:
    pages = list((paths.research / "claims").glob("*.md"))
    pages.extend((paths.wiki / "claims").glob("*.md"))
    return sorted(pages)


def relationship_pages(paths: WikiPaths) -> list[Path]:
    pages = list((paths.research / "relationships").glob("*.md"))
    pages.extend((paths.wiki / "relationships").glob("*.md"))
    return sorted(pages)


def build_claim_index(root: Path) -> list[ClaimRecord]:
    paths = WikiPaths(root.resolve())
    records: list[ClaimRecord] = []
    for page in claim_pages(paths):
        text = read_text(page)
        frontmatter = parse_frontmatter(text)
        if frontmatter.get("type") != "claim":
            continue
        records.append(
            ClaimRecord(
                id=page.stem.split("-", 1)[0],
                path=page.relative_to(paths.root).as_posix(),
                status=frontmatter.get("status", ""),
                claim_type=frontmatter.get("claim_type", ""),
                confidence=float_or_none(frontmatter.get("confidence", "")),
                subject=frontmatter.get("subject", ""),
                predicate=frontmatter.get("predicate", ""),
                object=frontmatter.get("object", ""),
                date=frontmatter.get("date", ""),
                place=frontmatter.get("place", ""),
                source=frontmatter.get("source", ""),
                source_packet=frontmatter.get("source_packet", ""),
                relationship=frontmatter.get("relationship", ""),
                text=extract_section(text, "Claim"),
                supports=parse_listish(frontmatter.get("supports", "")) or extract_wikilinks(extract_section(text, "Supports")),
                conflicts_with=parse_listish(frontmatter.get("conflicts_with", ""))
                or extract_wikilinks(extract_section(text, "Conflicts With")),
            )
        )
    return records


def build_relationship_index(root: Path, claims: list[ClaimRecord] | None = None) -> list[RelationshipRecord]:
    paths = WikiPaths(root.resolve())
    claims = claims if claims is not None else build_claim_index(paths.root)
    claim_lookup = {f"[[claims/{Path(record.path).stem}]]": record for record in claims}
    records: list[RelationshipRecord] = []
    for page in relationship_pages(paths):
        text = read_text(page)
        frontmatter = parse_frontmatter(text)
        if frontmatter.get("type") != "relationship":
            continue
        supporting_claims = parse_listish(frontmatter.get("supporting_claims", ""))
        conflicting_claims = parse_listish(frontmatter.get("conflicting_claims", ""))
        records.append(
            RelationshipRecord(
                id=page.stem.split("-", 1)[0],
                path=page.relative_to(paths.root).as_posix(),
                status=frontmatter.get("status", ""),
                relationship_type=frontmatter.get("relationship_type", ""),
                confidence=float_or_none(frontmatter.get("confidence", "")),
                calculated_confidence=calculate_relationship_confidence(
                    supporting_claims,
                    conflicting_claims,
                    claim_lookup,
                ),
                person_a=frontmatter.get("person_a", ""),
                person_b=frontmatter.get("person_b", ""),
                supporting_claims=supporting_claims,
                conflicting_claims=conflicting_claims,
                evidence_for=extract_section(text, "Evidence For"),
                evidence_against=extract_section(text, "Evidence Against"),
            )
        )
    return records


def write_claim_index(root: Path, output: Path | None = None) -> Path:
    paths = WikiPaths(root.resolve())
    output = output or (paths.indexes / "claims.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    claims = [asdict(record) for record in build_claim_index(paths.root)]
    output.write_text(json.dumps({"claims": claims}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return output


def write_relationship_index(root: Path, output: Path | None = None) -> Path:
    paths = WikiPaths(root.resolve())
    output = output or (paths.indexes / "relationships.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    claims = build_claim_index(paths.root)
    relationships = [asdict(record) for record in build_relationship_index(paths.root, claims)]
    output.write_text(
        json.dumps({"relationships": relationships}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return output


def write_relationship_graph(root: Path, output: Path | None = None) -> Path:
    paths = WikiPaths(root.resolve())
    output = output or (paths.indexes / "relationship-graph.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    claims = build_claim_index(paths.root)
    relationships = build_relationship_index(paths.root, claims)
    nodes: dict[str, dict[str, str]] = {}
    edges: list[dict[str, object]] = []
    for relationship in relationships:
        for person in [relationship.person_a, relationship.person_b]:
            if person:
                nodes.setdefault(
                    person,
                    {
                        "id": person,
                        "label": mermaid_label(person),
                        "target": wikilink_target(person) if looks_like_wikilink(person) else person,
                    },
                )
        edges.append(
            {
                "id": relationship.id,
                "path": relationship.path,
                "from": relationship.person_a,
                "to": relationship.person_b,
                "type": relationship.relationship_type,
                "status": relationship.status,
                "confidence": relationship.confidence,
                "calculated_confidence": relationship.calculated_confidence,
                "supporting_claims": relationship.supporting_claims,
                "conflicting_claims": relationship.conflicting_claims,
            }
        )
    output.write_text(
        json.dumps({"nodes": list(nodes.values()), "edges": edges}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return output


def generate_tree(root: Path, output: Path | None = None) -> Path:
    paths = WikiPaths(root.resolve())
    output = output or (paths.wiki / "Family Tree.md")
    output.parent.mkdir(parents=True, exist_ok=True)
    pages = relationship_pages(paths)

    lines = [
        "---",
        "type: tree",
        "status: generated",
        "tags: [tree]",
        "---",
        "",
        "# Family Tree",
        "",
        "```mermaid",
        "flowchart TD",
    ]
    warnings: list[str] = []
    link_styles: list[str] = []
    for page in pages:
        frontmatter = parse_frontmatter(read_text(page))
        person_a = frontmatter.get("person_a")
        person_b = frontmatter.get("person_b")
        relationship_type = frontmatter.get("relationship_type", "relationship")
        status = frontmatter.get("status", "draft")
        confidence = frontmatter.get("confidence", "0.0")
        if not person_a or not person_b:
            warnings.append(f"- Missing endpoint in {page.relative_to(paths.root).as_posix()}")
            continue
        person_a_label = public_person_label(paths, person_a)
        person_b_label = public_person_label(paths, person_b)
        edge_label = family_tree_edge_label(relationship_type)
        lines.append(
            f"  {node_id(person_a)}[\"{mermaid_node_label(person_a_label)}\"] -->|{edge_label}| "
            f"{node_id(person_b)}[\"{mermaid_node_label(person_b_label)}\"]"
        )
        link_styles.append(edge_style(status, confidence))

    if len(lines) == 10:
        lines.append("  empty[No relationship pages found]")
    for index, style in enumerate(link_styles):
        lines.append(f"  linkStyle {index} {style}")
    lines.extend(["```", ""])
    if warnings:
        lines.extend(["## Duplicate Or Relationship Warnings", *warnings, ""])
    lines.append("This view shows the family connections currently represented in the wiki.")
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return output


def compile_narrative(root: Path, subject: str, output: Path | None = None) -> Path:
    paths = WikiPaths(root.resolve())
    subject_slug = slug(subject)
    output = output or (paths.wiki / "narratives" / f"N-{subject_slug}.md")
    output.parent.mkdir(parents=True, exist_ok=True)

    claims: list[ClaimRecord] = []
    for record in build_claim_index(paths.root):
        if record.status not in {"accepted", "probable"}:
            continue
        if subject not in record.text and subject not in record.subject:
            continue
        claims.append(record)

    lines = [
        "---",
        "type: narrative",
        "status: draft",
        "tags: [narrative]",
        f"subject: {subject}",
        "narrative_type: individual_biography",
        "claim_scope: accepted_probable",
        "---",
        "",
        f"# {subject}",
        "",
        "## Scope",
        "",
        "This narrative is a family-history view compiled from accepted or probable claims. Add broader history only when it explains this person's life, records, migration, work, community, or constraints.",
        "",
        "## Draft Narrative",
        "",
    ]
    if claims:
        for claim in claims:
            confidence = claim.confidence if claim.confidence is not None else "unknown"
            claim_stem = Path(claim.path).stem
            lines.append(f"- {claim.text or claim_stem} (confidence: {confidence}; claim: [[claims/{claim_stem}]])")
    else:
        lines.append("No accepted or probable claims were found for this subject.")

    lines.extend(
        [
            "",
            "## Family-Relevant Historical Context",
            "",
            "Add linked context here only when it explains this subject's lived experience.",
            "",
            "## Uncertainty Notes",
            "",
            "This narrative was compiled only from accepted or probable claim pages.",
        ]
    )
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return output


SITE_EXCLUDED_WIKI_DIRS = {"_templates"}
SITE_EXCLUDED_WIKI_FILES = {"log.md", "research-plan.md"}
SITE_CSS = """
:root {
  color-scheme: light;
  --ink: #17202a;
  --muted: #5d6b7a;
  --line: #d8dee5;
  --paper: #f7f5ef;
  --surface: #ffffff;
  --accent: #315f72;
  --accent-soft: #e6f0f2;
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  background: var(--paper);
  color: var(--ink);
  font-family: Georgia, "Times New Roman", serif;
  line-height: 1.58;
}

.site-shell {
  display: grid;
  grid-template-columns: minmax(220px, 280px) minmax(0, 1fr);
  min-height: 100vh;
}

.site-nav {
  background: var(--surface);
  border-right: 1px solid var(--line);
  padding: 24px;
}

.site-nav h1 {
  font-size: 1.1rem;
  margin: 0 0 18px;
}

.site-nav a {
  color: var(--accent);
  text-decoration: none;
}

.site-nav ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.site-nav li {
  margin: 0 0 10px;
}

.site-main {
  max-width: 900px;
  width: 100%;
  padding: 42px 48px 72px;
}

.source-note {
  color: var(--muted);
  font-size: 0.9rem;
  margin-bottom: 28px;
}

a {
  color: var(--accent);
}

h1,
h2,
h3 {
  line-height: 1.2;
}

h1 {
  font-size: 2.2rem;
  margin: 0 0 16px;
}

h2 {
  border-top: 1px solid var(--line);
  margin-top: 34px;
  padding-top: 22px;
}

table {
  border-collapse: collapse;
  width: 100%;
  margin: 18px 0;
  background: var(--surface);
}

th,
td {
  border: 1px solid var(--line);
  padding: 8px 10px;
  text-align: left;
  vertical-align: top;
}

pre {
  background: #1e252b;
  color: #f3f5f7;
  overflow-x: auto;
  padding: 16px;
  border-radius: 6px;
}

.mermaid {
  background: var(--accent-soft);
  color: var(--ink);
}

@media (max-width: 760px) {
  .site-shell {
    display: block;
  }

  .site-nav {
    border-right: 0;
    border-bottom: 1px solid var(--line);
  }

  .site-main {
    padding: 28px 20px 52px;
  }
}
""".strip()


def build_static_site(root: Path, output_dir: Path | None = None) -> list[Path]:
    paths = WikiPaths(root.resolve())
    site_dir = output_dir or (paths.root / "site")
    if not site_dir.is_absolute():
        site_dir = paths.root / site_dir
    site_dir.mkdir(parents=True, exist_ok=True)
    assets_dir = site_dir / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)

    tree_path = generate_tree(paths.root)
    pages = collect_site_pages(paths.root)
    nav = build_site_nav(pages)
    written: list[Path] = [tree_path]
    css_path = assets_dir / "site.css"
    css_path.write_text(SITE_CSS + "\n", encoding="utf-8")
    written.append(css_path)

    page_records = []
    for page in pages:
        markdown_path = page["source"]
        output_path = site_dir / str(page["output"])
        output_path.parent.mkdir(parents=True, exist_ok=True)
        text = markdown_path.read_text(encoding="utf-8")
        title = str(page["title"])
        body = site_markdown_to_html(text, str(page["output"]))
        html_text = build_site_html_document(
            title=title,
            body=body,
            nav=nav,
            output_rel=str(page["output"]),
            source_rel=relative_to_root(markdown_path, paths.root),
        )
        output_path.write_text(html_text, encoding="utf-8")
        written.append(output_path)
        page_records.append(
            {
                "title": title,
                "source": relative_to_root(markdown_path, paths.root),
                "output": relative_to_root(output_path, paths.root),
            }
        )

    manifest = {
        "created": utc_timestamp(),
        "purpose": "Static HTML build manifest for the user-facing genealogy site.",
        "site_root": relative_to_root(site_dir, paths.root),
        "source_root": "wiki",
        "page_count": len(page_records),
        "asset_count": 1,
        "storage_contract": "HTML, CSS, and build manifests are GitHub files; raw originals and durable binary assets remain in R2.",
        "pages": page_records,
    }
    manifest_path = site_dir / "site-manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    written.append(manifest_path)
    append_log(paths.research / "log.md", f"site-build | Wrote {relative_to_root(manifest_path, paths.root)}")
    return written


def collect_site_pages(root: Path) -> list[dict[str, object]]:
    wiki = root / "wiki"
    pages = []
    if not wiki.exists():
        return pages
    for markdown_path in sorted(wiki.rglob("*.md")):
        rel = markdown_path.relative_to(wiki)
        if any(part in SITE_EXCLUDED_WIKI_DIRS for part in rel.parts):
            continue
        if markdown_path.name in SITE_EXCLUDED_WIKI_FILES:
            continue
        text = read_text(markdown_path)
        title = extract_markdown_title(text) or title_from_slug(markdown_path.stem)
        pages.append(
            {
                "source": markdown_path,
                "wiki_rel": rel.as_posix(),
                "output": site_output_rel_for_wiki_rel(rel),
                "title": title,
            }
        )
    return sorted(pages, key=site_page_sort_key)


def site_page_sort_key(page: dict[str, object]) -> tuple[int, str]:
    output = str(page.get("output", ""))
    if output == "index.html":
        return (0, output)
    if output == "family-tree.html":
        return (1, output)
    return (2, output)


def site_output_rel_for_wiki_rel(rel: Path) -> str:
    if rel.as_posix() == "index.md":
        return "index.html"
    parts = list(rel.parts)
    parts[-1] = f"{slug(Path(parts[-1]).stem)}.html"
    if len(parts) == 1 and parts[0] == "family-tree.html":
        return "family-tree.html"
    return Path(*parts).as_posix()


def build_site_nav(pages: list[dict[str, object]]) -> list[dict[str, str]]:
    return [{"title": str(page["title"]), "output": str(page["output"])} for page in pages]


def build_site_html_document(
    *,
    title: str,
    body: str,
    nav: list[dict[str, str]],
    output_rel: str,
    source_rel: str,
) -> str:
    css_href = site_relative_url(output_rel, "assets/site.css")
    nav_items = "\n".join(
        f'<li><a href="{html_lib.escape(site_relative_url(output_rel, item["output"]), quote=True)}">'
        f'{html_lib.escape(item["title"])}</a></li>'
        for item in nav
    )
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html_lib.escape(title)} | Family History</title>
  <link rel="stylesheet" href="{html_lib.escape(css_href, quote=True)}">
</head>
<body>
  <div class="site-shell">
    <nav class="site-nav" aria-label="Site navigation">
      <h1>Family History</h1>
      <ul>
{nav_items}
      </ul>
    </nav>
    <main class="site-main">
      <div class="source-note">Generated from {html_lib.escape(source_rel)}</div>
{body}
    </main>
  </div>
</body>
</html>
"""


def site_markdown_to_html(text: str, output_rel: str) -> str:
    text = strip_frontmatter(text)
    lines = text.splitlines()
    html_lines: list[str] = []
    paragraph: list[str] = []
    in_list = False
    index = 0

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            html_lines.append(f"<p>{site_render_inline(' '.join(line.strip() for line in paragraph), output_rel)}</p>")
            paragraph = []

    def close_list() -> None:
        nonlocal in_list
        if in_list:
            html_lines.append("</ul>")
            in_list = False

    while index < len(lines):
        line = lines[index]
        stripped = line.strip()
        if not stripped:
            flush_paragraph()
            close_list()
            index += 1
            continue
        if stripped.startswith("```"):
            flush_paragraph()
            close_list()
            language = stripped.strip("`").strip()
            code_lines = []
            index += 1
            while index < len(lines) and not lines[index].strip().startswith("```"):
                code_lines.append(lines[index])
                index += 1
            index += 1
            class_attr = ' class="mermaid"' if language == "mermaid" else ""
            html_lines.append(f"<pre{class_attr}><code>{html_lib.escape(chr(10).join(code_lines))}</code></pre>")
            continue
        if is_markdown_table_start(lines, index):
            flush_paragraph()
            close_list()
            table_lines = []
            while index < len(lines) and lines[index].strip().startswith("|"):
                table_lines.append(lines[index])
                index += 1
            html_lines.append(site_table_to_html(table_lines, output_rel))
            continue
        heading = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if heading:
            flush_paragraph()
            close_list()
            level = len(heading.group(1))
            heading_text = heading.group(2).strip()
            html_lines.append(
                f'<h{level} id="{html_lib.escape(slug(heading_text), quote=True)}">'
                f"{site_render_inline(heading_text, output_rel)}</h{level}>"
            )
            index += 1
            continue
        list_item = re.match(r"^-\s+(.+)$", stripped)
        if list_item:
            flush_paragraph()
            if not in_list:
                html_lines.append("<ul>")
                in_list = True
            html_lines.append(f"<li>{site_render_inline(list_item.group(1), output_rel)}</li>")
            index += 1
            continue
        paragraph.append(line)
        index += 1

    flush_paragraph()
    close_list()
    return "\n".join(f"      {line}" for line in html_lines)


def strip_frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return text
    match = re.match(r"---\s*\n.*?\n---\s*\n?", text, flags=re.DOTALL)
    return text[match.end() :] if match else text


def site_render_inline(text: str, output_rel: str) -> str:
    escaped = html_lib.escape(text)

    def replace_wikilink(match: re.Match[str]) -> str:
        target, label = split_site_wikilink(match.group(1))
        href = site_href_for_wikilink(output_rel, target)
        return f'<a href="{html_lib.escape(href, quote=True)}">{html_lib.escape(label)}</a>'

    escaped = re.sub(r"\[\[([^\]]+)\]\]", replace_wikilink, escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda match: f'<a href="{html_lib.escape(match.group(2), quote=True)}">{match.group(1)}</a>',
        escaped,
    )
    return escaped


def split_site_wikilink(value: str) -> tuple[str, str]:
    target, _, label = value.partition("|")
    label = label or title_from_slug(target.split("/")[-1])
    return target.strip(), label.strip()


def site_href_for_wikilink(output_rel: str, target: str) -> str:
    target, _, anchor = target.partition("#")
    if not target:
        href = output_rel
    else:
        target_rel = site_output_rel_for_target(target)
        href = site_relative_url(output_rel, target_rel)
    if anchor:
        href = f"{href}#{slug(anchor)}"
    return href


def site_output_rel_for_target(target: str) -> str:
    target = target.strip().strip("/")
    if target.endswith(".md"):
        target = target[:-3]
    if target.lower() == "index":
        return "index.html"
    parts = [slug(part) for part in target.replace("\\", "/").split("/") if part.strip()]
    if not parts:
        return "index.html"
    if len(parts) == 1 and parts[0] == "family-tree":
        return "family-tree.html"
    parts[-1] = f"{parts[-1]}.html"
    return Path(*parts).as_posix()


def site_relative_url(from_output_rel: str, to_output_rel: str) -> str:
    start_dir = Path(from_output_rel).parent
    rel = Path(os.path.relpath(to_output_rel, start_dir.as_posix() or ".")).as_posix()
    return rel if rel != "." else Path(to_output_rel).name


def is_markdown_table_start(lines: list[str], index: int) -> bool:
    if index + 1 >= len(lines):
        return False
    current = lines[index].strip()
    separator = lines[index + 1].strip()
    return current.startswith("|") and separator.startswith("|") and bool(re.fullmatch(r"[\s|:-]+", separator))


def site_table_to_html(table_lines: list[str], output_rel: str) -> str:
    if len(table_lines) < 2:
        return ""
    header = split_markdown_table_row(table_lines[0])
    body_rows = [split_markdown_table_row(line) for line in table_lines[2:]]
    header_html = "".join(f"<th>{site_render_inline(cell, output_rel)}</th>" for cell in header)
    body_html = "\n".join(
        "<tr>" + "".join(f"<td>{site_render_inline(cell, output_rel)}</td>" for cell in row) + "</tr>"
        for row in body_rows
    )
    return f"<table><thead><tr>{header_html}</tr></thead><tbody>{body_html}</tbody></table>"


def split_markdown_table_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def lint_claim_page(rel: str, frontmatter: dict[str, str], text: str) -> list[str]:
    issues: list[str] = []
    for field in ["status", "confidence", "source"]:
        if not frontmatter.get(field):
            issues.append(f"claim page missing {field}: {rel}")
    status = frontmatter.get("status", "")
    if status and status not in {"draft", "accepted", "probable", "possible", "disputed", "rejected"}:
        issues.append(f"claim page has invalid status '{status}': {rel}")
    confidence = float_or_none(frontmatter.get("confidence", ""))
    if confidence is None:
        issues.append(f"claim page confidence is not numeric: {rel}")
    elif confidence < 0 or confidence > 10:
        issues.append(f"claim page confidence outside 0-10 range: {rel}")
    for section in ["Literal Source Support", "Interpretation", "Uncertainty"]:
        if f"## {section}" not in text:
            issues.append(f"claim page missing {section} section: {rel}")
    return issues


def lint_claim_cross_references(root: Path, claims: list[ClaimRecord]) -> list[str]:
    paths = WikiPaths(root.resolve())
    issues: list[str] = []
    claim_by_wikilink = {f"[[claims/{Path(record.path).stem}]]": record for record in claims}
    for claim in claims:
        for field, required_prefix in [
            ("subject", None),
            ("source", "sources/"),
            ("source_packet", "source-packets/"),
            ("relationship", "relationships/"),
        ]:
            value = getattr(claim, field)
            if not value:
                continue
            if not looks_like_wikilink(value):
                issues.append(f"claim {claim.path} {field} should be a wiki link: {value}")
                continue
            target = wikilink_target(value)
            if required_prefix and not target.startswith(required_prefix):
                issues.append(f"claim {claim.path} {field} should link to {required_prefix}: {value}")
            target_root = paths.research if target.startswith(("sources/", "source-packets/", "claims/", "relationships/")) else paths.wiki
            if not wiki_target_exists(target_root, target):
                issues.append(f"claim {claim.path} {field} target missing: {value}")
        for linked_claim in claim.supports + claim.conflicts_with:
            if linked_claim and linked_claim not in claim_by_wikilink:
                issues.append(f"claim {claim.path} references missing claim: {linked_claim}")
    return issues


def lint_relationship_cross_references(
    root: Path,
    relationships: list[RelationshipRecord],
    claims: list[ClaimRecord],
) -> list[str]:
    paths = WikiPaths(root.resolve())
    issues: list[str] = []
    claim_by_wikilink = {f"[[claims/{Path(record.path).stem}]]": record for record in claims}
    for relationship in relationships:
        for field in ["person_a", "person_b"]:
            value = getattr(relationship, field)
            if not value:
                continue
            if not looks_like_wikilink(value):
                issues.append(f"relationship {relationship.path} {field} should be a wiki link: {value}")
                continue
            target = wikilink_target(value)
            if not target.startswith("people/"):
                issues.append(f"relationship {relationship.path} {field} should link to people/: {value}")
            if not wiki_target_exists(paths.wiki, target):
                issues.append(f"relationship {relationship.path} {field} target missing: {value}")
        for linked_claim in relationship.supporting_claims + relationship.conflicting_claims:
            if linked_claim and linked_claim not in claim_by_wikilink:
                issues.append(f"relationship {relationship.path} references missing claim: {linked_claim}")
    return issues


def lint_relationship_page(rel: str, frontmatter: dict[str, str], text: str) -> list[str]:
    issues: list[str] = []
    for field in ["relationship_type", "status", "confidence", "person_a", "person_b"]:
        if not frontmatter.get(field):
            issues.append(f"relationship page missing {field}: {rel}")
    relationship_type = frontmatter.get("relationship_type", "")
    if relationship_type and relationship_type not in {
        "parent_child",
        "proven_parent",
        "probable_parent",
        "possible_parent",
        "possible_sibling",
        "disputed_spouse",
        "same_person_candidate",
        "name_variant",
        "spouse",
        "child",
        "sibling",
        "household_member",
    }:
        issues.append(f"relationship page has invalid relationship_type '{relationship_type}': {rel}")
    confidence = float_or_none(frontmatter.get("confidence", ""))
    if confidence is None:
        issues.append(f"relationship page confidence is not numeric: {rel}")
    elif confidence < 0 or confidence > 10:
        issues.append(f"relationship page confidence outside 0-10 range: {rel}")
    if "## Evidence For" not in text or "## Evidence Against" not in text:
        issues.append(f"relationship page must show evidence on both sides: {rel}")
    return issues


def lint_source_packet_page(rel: str, text: str) -> list[str]:
    issues: list[str] = []
    for section in ["Literal Transcription", "Translation", "Interpretation", "Uncertain Or Illegible"]:
        if f"## {section}" not in text:
            issues.append(f"source packet missing {section} section: {rel}")
    if "dynamic-source" in text:
        for section in ["Verbatim Extraction Contract", "Printed Header And Label Inventory", "Completeness Audit"]:
            if f"## {section}" not in text:
                issues.append(f"dynamic source packet missing {section} section: {rel}")
    return issues


def lint_conflict_page(rel: str, frontmatter: dict[str, str], text: str) -> list[str]:
    issues: list[str] = []
    if not frontmatter.get("conflict_type"):
        issues.append(f"conflict page missing conflict_type: {rel}")
    for section in ["Competing Claims", "Needed Evidence"]:
        if f"## {section}" not in text:
            issues.append(f"conflict page missing {section} section: {rel}")
    return issues


def lint_identity_page(rel: str, text: str) -> list[str]:
    issues: list[str] = []
    for section in ["Comparison Matrix", "Evidence For Same Person", "Evidence Against Same Person"]:
        if f"## {section}" not in text:
            issues.append(f"identity page missing {section} section: {rel}")
    return issues


def lint_chronology(paths: WikiPaths) -> list[str]:
    issues: list[str] = []
    people = load_people(paths.wiki / "people")
    for page in relationship_pages(paths):
        frontmatter = parse_frontmatter(read_text(page))
        relationship_type = frontmatter.get("relationship_type", "")
        if relationship_type not in {"parent_child", "proven_parent", "probable_parent"}:
            continue
        parent = people.get(frontmatter.get("person_a", ""))
        child = people.get(frontmatter.get("person_b", ""))
        if not parent or not child:
            continue
        parent_birth = int_or_none(parent.get("birth_year", ""))
        child_birth = int_or_none(child.get("birth_year", ""))
        if parent_birth is None or child_birth is None:
            continue
        rel = page.relative_to(paths.research if paths.research in page.parents else paths.wiki).as_posix()
        if parent_birth > child_birth:
            issues.append(f"chronology impossible, parent born after child: {rel}")
        if child_birth - parent_birth < 12:
            issues.append(f"chronology suspicious, parent younger than 12 at child birth: {rel}")
    issues.extend(lint_event_chronology(paths.wiki, people))
    return issues


def lint_event_chronology(wiki: Path, people: dict[str, dict[str, str]]) -> list[str]:
    issues: list[str] = []
    seen: dict[tuple[str, str], tuple[str, str]] = {}
    for page in (wiki / "events").glob("*.md"):
        frontmatter = parse_frontmatter(read_text(page))
        event_date = frontmatter.get("date", "")
        event_year = first_year(event_date)
        place = frontmatter.get("place", "")
        participants = parse_listish(frontmatter.get("participants", ""))
        rel = page.relative_to(wiki).as_posix()
        for participant in participants:
            person = people.get(participant)
            if person:
                death_year = int_or_none(person.get("death_year", ""))
                if death_year is not None and event_year is not None and event_year > death_year:
                    issues.append(f"chronology impossible, event after participant death: {rel}")
            if event_date:
                key = (participant, event_date)
                previous = seen.get(key)
                if previous and previous[0] and place and previous[0] != place:
                    issues.append(
                        f"chronology suspicious, participant appears in two places on {event_date}: "
                        f"{previous[1]} and {rel}"
                    )
                seen[key] = (place, rel)
    return issues


def load_people(people_dir: Path) -> dict[str, dict[str, str]]:
    people: dict[str, dict[str, str]] = {}
    for page in people_dir.glob("*.md"):
        frontmatter = parse_frontmatter(read_text(page))
        key = f"[[people/{page.stem}]]"
        people[key] = frontmatter
        people[page.stem] = frontmatter
    return people


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    match = re.match(r"---\s*\n(.*?)\n---", text, flags=re.DOTALL)
    if not match:
        return {}
    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def parse_listish(value: str) -> list[str]:
    value = value.strip()
    if not value or value == "[]":
        return []
    if value.startswith("[") and value.endswith("]"):
        return [item.strip().strip('"').strip("'") for item in value[1:-1].split(",") if item.strip()]
    return [value]


def extract_wikilinks(text: str) -> list[str]:
    return [f"[[{match}]]" for match in re.findall(r"\[\[([^\]]+)\]\]", text)]


def looks_like_wikilink(value: str) -> bool:
    return value.startswith("[[") and value.endswith("]]")


def wikilink_target(value: str) -> str:
    return value.strip()[2:-2].split("|", 1)[0]


def wiki_target_exists(wiki: Path, target: str) -> bool:
    path = wiki / f"{target}.md"
    return path.exists()


def first_year(value: str) -> int | None:
    match = re.search(r"\b(\d{4})\b", value)
    if not match:
        return None
    return int(match.group(1))


def extract_section(text: str, heading: str) -> str:
    pattern = rf"^## {re.escape(heading)}\s*\n(.*?)(?=^## |\Z)"
    match = re.search(pattern, text, flags=re.MULTILINE | re.DOTALL)
    if not match:
        return ""
    return " ".join(match.group(1).strip().split())


def append_log(log_path: Path, entry: str) -> None:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    existing = read_text(log_path)
    addition = f"\n## [{date.today().isoformat()}] {entry}\n"
    log_path.write_text((existing.rstrip() + addition).lstrip(), encoding="utf-8")


def slug(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "untitled"


def node_id(value: str) -> str:
    return "n_" + slug(value).replace("-", "_")


def mermaid_label(value: str) -> str:
    value = value.replace("[[", "").replace("]]", "").split("/")[-1]
    return title_from_slug(value).replace('"', "'")


def title_from_slug(value: str) -> str:
    value = value.replace("_", " ").replace("-", " ").strip()
    if not value:
        return ""
    lower_particles = {"a", "da", "de", "del", "dos", "das", "la", "las", "los", "y", "of", "the"}
    words = []
    for index, word in enumerate(value.split()):
        if index > 0 and word.lower() in lower_particles:
            words.append(word.lower())
        elif len(word) == 1:
            words.append(word.upper())
        else:
            words.append(word[:1].upper() + word[1:])
    return " ".join(words)


def public_person_label(paths: WikiPaths, value: str) -> str:
    if looks_like_wikilink(value):
        target = wikilink_target(value)
        if target.startswith("people/"):
            page = paths.wiki / f"{target}.md"
            if page.exists():
                text = read_text(page)
                frontmatter = parse_frontmatter(text)
                return (
                    frontmatter.get("display_name")
                    or extract_markdown_title(text)
                    or title_from_slug(Path(target).stem)
                ).replace('"', "'")
    return mermaid_label(value)


def family_tree_edge_label(relationship_type: str) -> str:
    return {
        "parent_child": "parent of",
        "proven_parent": "parent of",
        "probable_parent": "probable parent of",
        "possible_parent": "possible parent of",
        "spouse": "spouse of",
        "child": "child of",
        "sibling": "sibling of",
        "possible_sibling": "possible sibling of",
        "household_member": "household member",
        "same_person_candidate": "same person?",
        "name_variant": "name variant",
    }.get(relationship_type, "connected to")


def mermaid_node_label(value: str) -> str:
    return value.replace('"', "'")


def edge_style(status: str, confidence: str) -> str:
    score = float_or_zero(confidence)
    if status in {"disputed", "possible"} or score < 5:
        return "stroke:#c53030,stroke-width:2px,stroke-dasharray: 5 5;"
    if status in {"probable"} or score < 8:
        return "stroke:#b7791f,stroke-width:2px;"
    return "stroke:#2f855a,stroke-width:3px;"


def int_or_none(value: str) -> int | None:
    try:
        return int(value)
    except ValueError:
        return None


def float_or_zero(value: str) -> float:
    try:
        return float(value)
    except ValueError:
        return 0.0


def float_or_none(value: str) -> float | None:
    try:
        return float(value)
    except ValueError:
        return None


def calculate_relationship_confidence(
    supporting_claims: list[str],
    conflicting_claims: list[str],
    claim_lookup: dict[str, ClaimRecord],
) -> float | None:
    support_scores = [
        record.confidence
        for claim in supporting_claims
        if (record := claim_lookup.get(claim))
        and record.confidence is not None
        and record.status in {"accepted", "probable", "possible"}
    ]
    conflict_scores = [
        record.confidence
        for claim in conflicting_claims
        if (record := claim_lookup.get(claim))
        and record.confidence is not None
        and record.status in {"accepted", "probable", "possible", "disputed"}
    ]
    if not support_scores and not conflict_scores:
        return None
    support = sum(support_scores) / len(support_scores) if support_scores else 0.0
    conflict_penalty = (sum(conflict_scores) / len(conflict_scores) * 0.5) if conflict_scores else 0.0
    return round(max(0.0, min(10.0, support - conflict_penalty)), 2)


def format_inline_list(values: list[str]) -> str:
    if not values:
        return "[]"
    formatted = []
    for value in values:
        if any(char in value for char in "[],:{}#") or "," in value:
            formatted.append('"' + value.replace('"', '\\"') + '"')
        else:
            formatted.append(value)
    return "[" + ", ".join(formatted) + "]"


def write_file(path: Path, content: str, force: bool, created: list[Path]) -> None:
    if path.exists() and not force:
        return
    path.write_text(content.strip() + "\n", encoding="utf-8")
    created.append(path)


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage a genealogy-focused LLM wiki workspace.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Create a genealogy wiki scaffold.")
    init_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    init_parser.add_argument("--force", action="store_true", help="Overwrite existing scaffold files.")

    lint_parser = subparsers.add_parser("lint", help="Check the genealogy wiki structure.")
    lint_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")

    packet_parser = subparsers.add_parser("packet", help="Create a structured source evidence packet.")
    packet_parser.add_argument("source_file", type=Path, help="Raw or converted source file.")
    packet_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    packet_parser.add_argument("--id", required=True, help="Packet/source id, such as SP001.")
    packet_parser.add_argument("--title", required=True, help="Human-readable source title.")
    packet_parser.add_argument("--kind", default="unknown", help="Source kind, such as census, church_register, photo, interview.")
    packet_parser.add_argument("--force", action="store_true", help="Overwrite an existing packet.")

    material_parser = subparsers.add_parser(
        "material",
        help="Stage any source file and create a dynamic, document-agnostic evidence packet.",
    )
    material_parser.add_argument("source_file", type=Path, help="Raw source file: image, PDF, text, audio, video, or other media.")
    material_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    material_parser.add_argument("--id", required=True, help="Packet/source id, such as SP001.")
    material_parser.add_argument("--title", required=True, help="Human-readable source title.")
    material_parser.add_argument("--kind", default="unknown", help="Descriptive source kind, not a fixed extraction schema.")
    material_parser.add_argument(
        "--feature",
        action="append",
        default=[],
        help="Observed feature to include in the dynamic material profile. May be repeated.",
    )
    material_parser.add_argument("--no-copy", action="store_true", help="Link to the source file instead of copying it into raw/sources.")
    material_parser.add_argument("--force", action="store_true", help="Overwrite an existing packet, source page, or staged file.")

    codex_job_parser = subparsers.add_parser(
        "codex-job",
        help="Prepare a local page-by-page conversion job for Codex vision work.",
    )
    codex_job_parser.add_argument("source_file", type=Path, help="Source PDF, image, or other file to prepare.")
    codex_job_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    codex_job_parser.add_argument("--id", required=True, help="Job id, such as CJ001.")
    codex_job_parser.add_argument("--title", required=True, help="Human-readable source title.")
    codex_job_parser.add_argument("--pages", help="Optional page range, such as 1,3-5. Defaults to all pages.")
    codex_job_parser.add_argument("--image-scale", type=float, default=2.0, help="PDF render scale for page images. Default: 2.0.")
    codex_job_parser.add_argument("--force", action="store_true", help="Overwrite an existing conversion job.")

    codex_next_parser = subparsers.add_parser(
        "codex-next",
        help="Print the next unfinished Codex conversion work order for a prepared job.",
    )
    codex_next_parser.add_argument("manifest", type=Path, help="Path to a codex-job manifest.json.")
    codex_next_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")

    codex_assemble_parser = subparsers.add_parser(
        "codex-assemble",
        help="Assemble completed Codex page Markdown files into one converted document.",
    )
    codex_assemble_parser.add_argument("manifest", type=Path, help="Path to a codex-job manifest.json.")
    codex_assemble_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    codex_assemble_parser.add_argument("--out", type=Path, help="Output Markdown path. Defaults to raw/converted/<job>.codex.md.")

    prep_index_parser = subparsers.add_parser(
        "prep-index",
        help="Inventory raw/sources for the document-preparation pipeline.",
    )
    prep_index_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    prep_index_parser.add_argument("--out", type=Path, help="Output JSON path. Default: raw/source-prep-manifest.json.")

    raw_cloud_parser = subparsers.add_parser(
        "raw-cloud",
        help="Inventory, upload, verify, or restore raw source originals and binary derivatives using Cloudflare R2.",
    )
    raw_cloud_parser.add_argument(
        "action",
        choices=["inventory", "upload", "verify", "restore", "asset-inventory", "asset-upload", "cleanup-manifests"],
    )
    raw_cloud_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    raw_cloud_parser.add_argument("--env-file", type=Path, help="R2 env file. Default: .env.r2 when present.")
    raw_cloud_parser.add_argument(
        "--config",
        type=Path,
        help="Non-secret R2 config JSON. Default: raw/r2-storage.json.",
    )
    raw_cloud_parser.add_argument("--account-id", help="Cloudflare account id. Default comes from R2_ACCOUNT_ID or config.")
    raw_cloud_parser.add_argument("--endpoint-url", help="R2 S3 endpoint URL. Default uses account id.")
    raw_cloud_parser.add_argument("--bucket", help="R2 bucket name. Default comes from R2_BUCKET or config.")
    raw_cloud_parser.add_argument("--prefix", help="Optional object key prefix. Default comes from R2_PREFIX or config.")
    raw_cloud_parser.add_argument(
        "--raw-dir",
        type=Path,
        default=Path("raw") / "sources",
        help="Raw source directory to sync. Default: raw/sources.",
    )
    raw_cloud_parser.add_argument(
        "--state-dir",
        type=Path,
        help="Local state/report directory. Default: .genealogy/raw-cloud.",
    )
    raw_cloud_parser.add_argument("--limit", type=int, help="Limit files for a test run.")
    raw_cloud_parser.add_argument("--out", type=Path, help="Inventory output path for the inventory action.")
    raw_cloud_parser.add_argument("--manifest", type=Path, help="Local manifest path to use for restore.")
    raw_cloud_parser.add_argument("--dry-run", action="store_true", help="For upload, write a plan without network writes.")
    raw_cloud_parser.add_argument("--force", action="store_true", help="Re-upload or overwrite restored files.")

    r2_source_intake_parser = subparsers.add_parser(
        "r2-source-intake",
        help="List R2 raw sources and register cloud-only source-prep manifest entries.",
    )
    r2_source_intake_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    r2_source_intake_parser.add_argument("--limit", type=int, help="Limit remote R2 objects for a bounded test run.")
    r2_source_intake_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="List remote sources and report changes without writing manifests.",
    )

    prepare_sources_parser = subparsers.add_parser(
        "prepare-sources",
        help="Queue Codex-agent conversion jobs for raw/sources and chunk completed conversions.",
    )
    prepare_sources_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    prepare_sources_parser.add_argument("--pages", help="Optional page range for newly-created jobs, such as 1,3-5.")
    prepare_sources_parser.add_argument(
        "--image-scale",
        type=float,
        default=2.0,
        help="PDF render scale for newly-created page images. Default: 2.0.",
    )
    prepare_sources_parser.add_argument(
        "--pages-per-job",
        type=int,
        default=50,
        help="Maximum PDF pages per conversion job so agent workers can own manageable ranges. Default: 50.",
    )
    prepare_sources_parser.add_argument(
        "--new-pages-limit",
        type=int,
        default=0,
        help="Maximum not-yet-jobed PDF pages to create jobs for per source. Use 0 for no cap. Default: 0.",
    )
    prepare_sources_parser.add_argument("--max-chars", type=int, default=12000, help="Chunk size for completed conversions.")
    prepare_sources_parser.add_argument("--force", action="store_true", help="Recreate existing conversion jobs.")

    agent_queues_parser = subparsers.add_parser(
        "agent-queues",
        help="Write Codex agent task queues for source prep, conversion QA, and evidence extraction.",
    )
    agent_queues_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    agent_queues_parser.add_argument(
        "--out-dir",
        type=Path,
        help="Output queue directory. Default: research/_agent-queues.",
    )
    agent_queues_parser.add_argument(
        "--stale-minutes",
        type=int,
        default=360,
        help="Release claimed/in-progress tasks with no update for this many minutes. Use 0 to disable. Default: 360.",
    )

    source_prep_batches_parser = subparsers.add_parser(
        "source-prep-batches",
        help="Write bounded contiguous source-prep batch prompts for faster high-quality conversion work.",
    )
    source_prep_batches_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    source_prep_batches_parser.add_argument(
        "--out-dir",
        type=Path,
        help="Output queue directory. Default: research/_agent-queues.",
    )
    source_prep_batches_parser.add_argument(
        "--max-pages",
        type=int,
        default=SOURCE_PREP_MAX_PAGES_PER_WORKER,
        help="Maximum contiguous pages per batch prompt; source-prep policy caps this at 1. Default: 1.",
    )
    source_prep_batches_parser.add_argument(
        "--limit",
        type=int,
        default=50,
        help="Maximum batch prompts to write. Default: 50.",
    )
    source_prep_batches_parser.add_argument(
        "--stale-minutes",
        type=int,
        default=360,
        help="Release claimed/in-progress tasks with no update for this many minutes. Use 0 to disable. Default: 360.",
    )
    source_prep_batches_parser.add_argument(
        "--status",
        action="append",
        choices=list(SOURCE_PREP_BATCHABLE_STATUSES),
        help="Task status to include in batches. May be repeated. Default: needs_reread and todo.",
    )

    cloud_source_prep_parser = subparsers.add_parser(
        "cloud-source-prep-heartbeat",
        help="Cloud-first source-prep heartbeat: restore raw R2 cache, refresh GitHub queues, and upload binary derivatives.",
    )
    cloud_source_prep_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    cloud_source_prep_parser.add_argument("--pages", help="Optional page range for newly-created jobs, such as 1,3-5.")
    cloud_source_prep_parser.add_argument("--restore-limit", type=int, help="Maximum raw R2 objects to restore for this run.")
    cloud_source_prep_parser.add_argument("--pages-per-job", type=int, default=25, help="Maximum PDF pages per conversion job.")
    cloud_source_prep_parser.add_argument("--new-pages-limit", type=int, default=0, help="Maximum not-yet-jobed PDF pages to create jobs for per source. Use 0 for no cap.")
    cloud_source_prep_parser.add_argument("--batch-pages", type=int, default=1, help="Pages per source-prep batch. Capped at one.")
    cloud_source_prep_parser.add_argument("--queue-limit", type=int, default=80, help="Maximum source-prep batches to materialize.")
    cloud_source_prep_parser.add_argument("--stale-minutes", type=int, default=360, help="Release stale claimed tasks after this many minutes.")
    cloud_source_prep_parser.add_argument("--max-chars", type=int, default=12000, help="Chunk size for completed conversions.")
    cloud_source_prep_parser.add_argument("--fastlane-limit", type=int, default=0, help="Optional deterministic born-digital PDF page limit.")
    cloud_source_prep_parser.add_argument("--fastlane-scan-limit", type=int, default=250, help="Optional deterministic fastlane scan limit.")
    cloud_source_prep_parser.add_argument("--no-research-analyzer", action="store_true", help="Skip the automated research-analyzer pass.")
    cloud_source_prep_parser.add_argument("--research-analyzer-limit", type=int, default=5, help="Maximum new page-upgrade requests from the analyzer. Use -1 for no cap.")
    cloud_source_prep_parser.add_argument("--research-question-limit", type=int, default=5, help="Maximum new research questions from the analyzer. Use -1 for no cap.")
    cloud_source_prep_parser.add_argument("--conversion-qc", action="store_true", help="Run legacy conversion-QC artifacts and queues. Default is off.")
    cloud_source_prep_parser.add_argument("--conversion-only", action="store_true", help="Only prepare/assemble source conversions; skip research/QC/status queues.")
    cloud_source_prep_parser.add_argument("--no-restore", action="store_true", help="Do not restore raw originals from R2 first.")
    cloud_source_prep_parser.add_argument("--no-asset-upload", action="store_true", help="Do not upload durable crops/assets to R2.")
    cloud_source_prep_parser.add_argument("--dry-run", action="store_true", help="Skip R2 writes and raw restore; still refresh local queue outputs.")

    sync_github_parser = subparsers.add_parser(
        "sync-github-database",
        help="Commit and optionally push GitHub-backed genealogy JSON/Markdown/code state without R2-only binaries.",
    )
    sync_github_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    sync_github_parser.add_argument("--message", default="", help="Commit message. Default includes a timestamp.")
    sync_github_parser.add_argument("--dry-run", action="store_true", help="Show what would be added without staging or committing.")
    sync_github_parser.add_argument("--no-push", action="store_true", help="Create a local commit but do not push.")
    sync_github_parser.add_argument("--source-conversion-only", action="store_true", help="Sync only raw conversion artifacts and minimal automation state.")

    source_prep_fastlane_parser = subparsers.add_parser(
        "source-prep-fastlane",
        help="Bulk-complete only deterministic born-digital PDF pages that pass the source-prep quality gate.",
    )
    source_prep_fastlane_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    source_prep_fastlane_parser.add_argument(
        "--limit",
        type=int,
        default=100,
        help="Maximum pages to complete in this run. Default: 100.",
    )
    source_prep_fastlane_parser.add_argument(
        "--scan-limit",
        type=int,
        default=1000,
        help="Maximum queued pages to inspect before stopping. Default: 1000.",
    )
    source_prep_fastlane_parser.add_argument(
        "--agent",
        default="source-prep-fastlane",
        help="Agent label recorded in task-state.json. Default: source-prep-fastlane.",
    )
    source_prep_fastlane_parser.add_argument(
        "--stale-minutes",
        type=int,
        default=360,
        help="Release claimed/in-progress tasks with no update for this many minutes. Use 0 to disable. Default: 360.",
    )
    source_prep_fastlane_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Inspect and report eligible pages without writing page Markdown or task state.",
    )

    source_prep_docling_parser = subparsers.add_parser(
        "source-prep-docling-discovery",
        help="Write rough non-evidence Docling page discovery output for readable pages before Gemini.",
    )
    source_prep_docling_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    source_prep_docling_parser.add_argument(
        "--limit",
        type=int,
        default=100,
        help="Maximum readable rough-discovery pages to accept in this run. Default: 100.",
    )
    source_prep_docling_parser.add_argument(
        "--scan-limit",
        type=int,
        default=1000,
        help="Maximum queued pages to inspect before stopping. Default: 1000.",
    )
    source_prep_docling_parser.add_argument(
        "--agent",
        default="source-prep-docling-discovery",
        help="Agent label recorded in discovery state. Default: source-prep-docling-discovery.",
    )
    source_prep_docling_parser.add_argument(
        "--stale-minutes",
        type=int,
        default=360,
        help="Release claimed/in-progress tasks with no update for this many minutes. Use 0 to disable. Default: 360.",
    )
    source_prep_docling_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Inspect and report pages without writing rough discovery output or discovery state.",
    )

    source_prep_review_page_parser = subparsers.add_parser(
        "source-prep-review-page",
        help="Review one source-prep page Markdown output against the conversion contract.",
    )
    source_prep_review_page_parser.add_argument("output_path", type=Path, help="Page Markdown path to review.")
    source_prep_review_page_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")

    gemini_source_prep_parser = subparsers.add_parser(
        "gemini-source-prep",
        help="Convert queued one-page source-prep tasks with Gemini model routing.",
    )
    gemini_source_prep_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    gemini_source_prep_parser.add_argument("--limit", type=int, default=25, help="Maximum one-page tasks to process. Default: 25.")
    gemini_source_prep_parser.add_argument(
        "--parallelism",
        type=int,
        default=1,
        help="Maximum Gemini page conversions to run at the same time. Default: 1.",
    )
    gemini_source_prep_parser.add_argument(
        "--queue-limit",
        type=int,
        default=160,
        help="Maximum source-prep batch tasks to materialize before processing. Default: 160.",
    )
    gemini_source_prep_parser.add_argument(
        "--stale-minutes",
        type=int,
        default=360,
        help="Release stale claimed tasks after this many minutes. Default: 360.",
    )
    gemini_source_prep_parser.add_argument(
        "--lite-model",
        default=GEMINI_SOURCE_PREP_LITE_MODEL,
        help=f"Model for simple/basic pages. Default: {GEMINI_SOURCE_PREP_LITE_MODEL}.",
    )
    gemini_source_prep_parser.add_argument(
        "--pro-model",
        default=GEMINI_SOURCE_PREP_PRO_MODEL,
        help=f"Model for complex or family-relevant pages. Default: {GEMINI_SOURCE_PREP_PRO_MODEL}.",
    )
    gemini_source_prep_parser.add_argument(
        "--max-output-tokens-lite",
        type=int,
        default=65536,
        help="Max output tokens for lite-model pages. Default: 65536.",
    )
    gemini_source_prep_parser.add_argument(
        "--max-output-tokens-pro",
        type=int,
        default=65536,
        help="Max output tokens for pro-model pages. Default: 65536.",
    )
    gemini_source_prep_parser.add_argument(
        "--crop-count",
        type=int,
        default=4,
        help="Zoom crops to attach for Pro family-relevant pages. Default: 4.",
    )
    gemini_source_prep_parser.add_argument(
        "--no-crops",
        action="store_true",
        help="Disable crop attachments for family-relevant Pro pages.",
    )
    gemini_source_prep_parser.add_argument(
        "--agent",
        default="gemini-source-prep",
        help="Agent label recorded in task-state.json. Default: gemini-source-prep.",
    )
    gemini_source_prep_parser.add_argument(
        "--api-key-env",
        default="",
        help="Optional environment variable name containing the Gemini API key. Defaults to GEMINI_API_KEY or GOOGLE_API_KEY.",
    )
    gemini_source_prep_parser.add_argument(
        "--no-refresh-queue",
        action="store_true",
        help="Use the existing source-prep-batches queue instead of refreshing it first.",
    )
    gemini_source_prep_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Plan model routing without calling Gemini or writing outputs.",
    )

    source_relevance_parser = subparsers.add_parser(
        "source-relevance",
        help="Record or list research-to-conversion relevance feedback.",
    )
    source_relevance_parser.add_argument("action", choices=["mark", "list"], help="Action to run.")
    source_relevance_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    source_relevance_parser.add_argument("--task-id", default="", help="Source-prep task id to target.")
    source_relevance_parser.add_argument("--job-manifest", default="", help="Conversion job manifest path to target.")
    source_relevance_parser.add_argument("--source", default="", help="Raw/source path to target.")
    source_relevance_parser.add_argument("--source-sha256", default="", help="Source SHA-256 to target.")
    source_relevance_parser.add_argument("--converted-file", default="", help="Converted Markdown file to target.")
    source_relevance_parser.add_argument(
        "--page",
        type=int,
        default=0,
        help=(
            "Page number to target. For high/critical relevance or pro/pro_with_crops/reread treatment, "
            "0 expands the prepared target into one hint per page."
        ),
    )
    source_relevance_parser.add_argument(
        "--relevance",
        choices=list(SOURCE_RELEVANCE_VALUES),
        default="high",
        help="Research relevance level. Default: high.",
    )
    source_relevance_parser.add_argument(
        "--treatment",
        choices=list(SOURCE_RELEVANCE_TREATMENTS),
        default="pro_with_crops",
        help="Requested conversion treatment. Default: pro_with_crops.",
    )
    source_relevance_parser.add_argument("--reason", default="", help="Concise reason the source/page matters.")
    source_relevance_parser.add_argument("--entity", action="append", default=[], help="Family person/entity this hint relates to. May repeat.")
    source_relevance_parser.add_argument("--term", action="append", default=[], help="Matched family term or search clue. May repeat.")
    source_relevance_parser.add_argument("--agent", default="", help="Research agent label recording the hint.")

    research_analyzer_parser = subparsers.add_parser(
        "research-analyzer",
        help="Scan converted chunks for genealogy signals and write page-level upgrade requests.",
    )
    research_analyzer_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    research_analyzer_parser.add_argument(
        "--limit",
        type=int,
        default=5,
        help="Maximum new page-level upgrade requests to write. Use -1 for no cap. Default: 5.",
    )
    research_analyzer_parser.add_argument(
        "--question-limit",
        type=int,
        default=5,
        help="Maximum new research question pages to write. Use -1 for no cap. Default: 5.",
    )
    research_analyzer_parser.add_argument(
        "--out",
        type=Path,
        help="Output research-analyzer JSON index. Default: research/_indexes/research-analyzer.json.",
    )
    research_analyzer_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Write analyzer status without adding source-relevance feedback.",
    )

    conversion_qc_parser = subparsers.add_parser(
        "conversion-qc",
        help="Write page-level post-conversion QC triage, reread queues, and suspected readings.",
    )
    conversion_qc_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    conversion_qc_parser.add_argument(
        "--out-dir",
        type=Path,
        help="Output review directory. Default: research/_conversion-review.",
    )

    source_status_parser = subparsers.add_parser(
        "source-status",
        aliases=["source-usability"],
        help="Write a source usability report for raw source preparation and QC holds.",
    )
    source_status_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    source_status_parser.add_argument(
        "--out",
        type=Path,
        help="Output JSON path. Default: research/_indexes/source-usability.json.",
    )
    source_status_parser.add_argument(
        "--markdown",
        type=Path,
        help="Output Markdown path. Default: research/source-usability.md.",
    )

    system_status_parser = subparsers.add_parser(
        "system-status",
        aliases=["system-dashboard"],
        help="Write a whole-system source, research, queue, storage, and site dashboard.",
    )
    system_status_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    system_status_parser.add_argument(
        "--out",
        type=Path,
        help="Output JSON path. Default: research/_indexes/system-status.json.",
    )
    system_status_parser.add_argument(
        "--markdown",
        type=Path,
        help="Output Markdown path. Default: research/System Dashboard.md.",
    )
    system_status_parser.add_argument(
        "--no-refresh-source-status",
        action="store_true",
        help="Read existing source usability reports instead of refreshing them first.",
    )

    storage_lifecycle_parser = subparsers.add_parser(
        "storage-lifecycle",
        aliases=["storage-ranking"],
        help="Write non-destructive page-level storage lifecycle rankings and deaccession candidate records.",
    )
    storage_lifecycle_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    storage_lifecycle_parser.add_argument(
        "--out",
        type=Path,
        help="Output JSON path. Default: research/_indexes/storage-lifecycle.json.",
    )
    storage_lifecycle_parser.add_argument(
        "--markdown",
        type=Path,
        help="Output Markdown path. Default: research/storage-lifecycle.md.",
    )
    storage_lifecycle_parser.add_argument(
        "--record-dir",
        type=Path,
        help="Output directory for candidate records. Default: research/_staging/deaccession.",
    )

    agent_task_parser = subparsers.add_parser(
        "agent-task",
        help="Claim, start, complete, fail, or release an agent queue task.",
    )
    agent_task_parser.add_argument("action", choices=["claim", "start", "complete", "fail", "release"])
    agent_task_parser.add_argument("task_id", nargs="+", help="Task id from a queue manifest. May be repeated for batch updates.")
    agent_task_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    agent_task_parser.add_argument("--agent", default="", help="Agent or worker label to record.")
    agent_task_parser.add_argument("--note", default="", help="Short status note.")
    agent_task_parser.add_argument(
        "--no-refresh",
        action="store_true",
        help="Only update durable task state; skip regenerating queue manifests.",
    )

    prep_chunk_parser = subparsers.add_parser(
        "prep-chunk",
        help="Chunk a converted Markdown source into page-scoped research prep chunks.",
    )
    prep_chunk_parser.add_argument("converted_file", type=Path, help="Converted Markdown file under raw/converted.")
    prep_chunk_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    prep_chunk_parser.add_argument("--out-dir", type=Path, help="Output chunk directory. Default: raw/chunks/<converted-file>.")
    prep_chunk_parser.add_argument("--max-chars", type=int, default=12000, help="Maximum characters per chunk. Default: 12000.")

    vault_transcriptions_parser = subparsers.add_parser(
        "vault-transcriptions",
        help="Copy converted Markdown into editable Obsidian transcription notes.",
    )
    vault_transcriptions_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    vault_transcriptions_parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing editable transcription notes. Default preserves manual edits.",
    )

    promote_staged_parser = subparsers.add_parser(
        "promote-staged",
        help="Promote reviewed staging drafts into canonical source packets, claims, relationships, indexes, and tree.",
    )
    promote_staged_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    promote_staged_parser.add_argument("--force", action="store_true", help="Overwrite existing promoted pages.")
    promote_staged_parser.add_argument("--dry-run", action="store_true", help="Report what would be promoted without writing.")
    promote_staged_parser.add_argument(
        "--include-revise",
        action="store_true",
        help="Also promote staged drafts whose recommendation is revise.",
    )
    promote_staged_parser.add_argument(
        "--include-hold",
        action="store_true",
        help="Also promote staged drafts whose recommendation is hold or reject. Use only for manual recovery.",
    )

    claim_parser = subparsers.add_parser("claim", help="Create an atomic genealogy claim page.")
    claim_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    claim_parser.add_argument("--id", required=True, help="Claim id, such as CL001.")
    claim_parser.add_argument("--text", required=True, help="Literal atomic claim text.")
    claim_parser.add_argument("--type", required=True, help="Claim type, such as event, birth, death, residence, relationship.")
    claim_parser.add_argument("--subject", required=True, help="Subject wiki link, such as [[people/person-name]].")
    claim_parser.add_argument("--source", required=True, help="Source wiki link, such as [[sources/S001-record]].")
    claim_parser.add_argument("--status", default="draft", help="draft, accepted, probable, possible, disputed, or rejected.")
    claim_parser.add_argument("--confidence", type=float, default=0.0, help="Confidence score from 0 to 10.")
    claim_parser.add_argument("--predicate", default="", help="Predicate or relation label.")
    claim_parser.add_argument("--object", default="", help="Object value for the claim.")
    claim_parser.add_argument("--date", default="", help="Claim date.")
    claim_parser.add_argument("--place", default="", help="Place wiki link or text.")
    claim_parser.add_argument("--source-packet", default="", help="Source packet wiki link.")
    claim_parser.add_argument("--relationship", default="", help="Relationship wiki link.")
    claim_parser.add_argument("--force", action="store_true", help="Overwrite an existing claim.")

    relationship_parser = subparsers.add_parser("relationship", help="Create a relationship assertion page.")
    relationship_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    relationship_parser.add_argument("--id", required=True, help="Relationship id, such as R001.")
    relationship_parser.add_argument("--type", required=True, help="Relationship type, such as proven_parent or spouse.")
    relationship_parser.add_argument("--person-a", required=True, help="First person wiki link.")
    relationship_parser.add_argument("--person-b", required=True, help="Second person wiki link.")
    relationship_parser.add_argument("--status", default="draft", help="draft, accepted, probable, possible, disputed, or rejected.")
    relationship_parser.add_argument("--confidence", type=float, default=0.0, help="Confidence score from 0 to 10.")
    relationship_parser.add_argument("--supporting-claim", action="append", default=[], help="Supporting claim wiki link. May be repeated.")
    relationship_parser.add_argument("--conflicting-claim", action="append", default=[], help="Conflicting claim wiki link. May be repeated.")
    relationship_parser.add_argument("--force", action="store_true", help="Overwrite an existing relationship.")

    index_parser = subparsers.add_parser("index", help="Write structured JSON indexes from wiki pages.")
    index_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    index_parser.add_argument("--out", type=Path, help="Claim index output path. Default: research/_indexes/claims.json.")

    graph_parser = subparsers.add_parser("graph", help="Write a relationship graph JSON view.")
    graph_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    graph_parser.add_argument("--out", type=Path, help="Output path. Default: research/_indexes/relationship-graph.json.")

    tree_parser = subparsers.add_parser("tree", help="Generate a Mermaid family tree view from relationship pages.")
    tree_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    tree_parser.add_argument("--out", type=Path, help="Output Markdown path. Default: wiki/Family Tree.md.")

    site_parser = subparsers.add_parser(
        "site-build",
        aliases=["build-site"],
        help="Build the final user-facing static HTML genealogy site from wiki pages.",
    )
    site_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    site_parser.add_argument("--out-dir", type=Path, help="Output site directory. Default: site/.")

    narrative_parser = subparsers.add_parser("narrative", help="Compile a narrative from accepted/probable claim pages.")
    narrative_parser.add_argument("subject", help="Person, family, branch, or entity label to compile.")
    narrative_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    narrative_parser.add_argument("--out", type=Path, help="Output Markdown path.")

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "init":
        created = init_genealogy_wiki(args.root, force=args.force)
        print(f"Initialized genealogy wiki at {args.root.resolve()}")
        print(f"Created or ensured {len(created)} paths")
        return 0

    if args.command == "lint":
        issues = lint_genealogy_wiki(args.root)
        if not issues:
            print("Genealogy wiki lint passed")
            return 0
        print("Genealogy wiki lint found issues:")
        for issue in issues:
            print(f"- {issue}")
        return 1

    if args.command == "packet":
        packet_path = create_source_packet(args.root, args.source_file, args.id, args.title, args.kind, args.force)
        print(f"Created source packet {packet_path}")
        return 0

    if args.command == "material":
        packet_path = create_material_packet(
            root=args.root,
            source_file=args.source_file,
            packet_id=args.id,
            title=args.title,
            source_kind=args.kind,
            features=args.feature,
            copy_source=not args.no_copy,
            force=args.force,
        )
        print(f"Created dynamic material packet {packet_path}")
        return 0

    if args.command == "codex-job":
        manifest = create_codex_conversion_job(
            root=args.root,
            source_file=args.source_file,
            job_id=args.id,
            title=args.title,
            page_range=args.pages,
            image_scale=args.image_scale,
            force=args.force,
        )
        print(f"Prepared Codex conversion job {manifest}")
        next_work = next_codex_conversion_work_order(args.root, manifest)
        if next_work:
            print(f"Next work order {next_work}")
        return 0

    if args.command == "codex-next":
        next_work = next_codex_conversion_work_order(args.root, args.manifest)
        if next_work is None:
            print("No unfinished Codex conversion work orders")
            return 0
        print(next_work)
        return 0

    if args.command == "codex-assemble":
        output_path = assemble_codex_conversion_job(args.root, args.manifest, out=args.out)
        print(f"Assembled Codex conversion document {output_path}")
        return 0

    if args.command == "prep-index":
        output_path = write_source_prep_index(args.root, args.out)
        print(f"Wrote source preparation manifest {output_path}")
        return 0

    if args.command == "r2-source-intake":
        summary = monitor_r2_source_intake(args.root, limit=args.limit, dry_run=args.dry_run)
        print("r2-source-intake | summary")
        print(json.dumps(summary, indent=2, ensure_ascii=False))
        return 1 if summary.get("blockers") else 0

    if args.command == "raw-cloud":
        needs_credentials = (
            args.action in {"verify", "restore", "cleanup-manifests"}
            or (args.action in {"upload", "asset-upload"} and not args.dry_run)
        )
        config = load_raw_cloud_config(
            root=args.root,
            env_file=args.env_file,
            config_file=args.config,
            endpoint_url=args.endpoint_url,
            account_id=args.account_id,
            bucket=args.bucket,
            prefix=args.prefix,
            raw_dir=args.raw_dir,
            state_dir=args.state_dir,
            require_credentials=needs_credentials,
        )
        if args.action == "inventory":
            output_path = write_raw_cloud_inventory(args.root, config, limit=args.limit, out=args.out)
            manifest = json.loads(output_path.read_text(encoding="utf-8"))
            total_bytes = sum(item["bytes"] for item in manifest["files"])
            print(f"Wrote raw cloud inventory {output_path}")
            print(f"files={len(manifest['files'])} bytes={total_bytes}")
            return 0
        if args.action == "asset-inventory":
            output_path = write_derived_asset_inventory(args.root, config, limit=args.limit, out=args.out)
            manifest = json.loads(output_path.read_text(encoding="utf-8"))
            total_bytes = sum(item["bytes"] for item in manifest["files"])
            print(f"Wrote derived asset cloud inventory {output_path}")
            print(f"files={len(manifest['files'])} bytes={total_bytes}")
            return 0
        if args.action == "upload":
            summary = upload_raw_to_cloud(
                args.root,
                config,
                dry_run=args.dry_run,
                force=args.force,
                limit=args.limit,
            )
            print(
                "raw-cloud upload | "
                f"files={summary['total_files']} bytes={summary['total_bytes']} "
                f"uploaded={summary['uploaded']} skipped={summary['skipped']} "
                f"planned={summary['planned']} dry_run={summary['dry_run']} "
                f"errors={len(summary['errors'])}"
            )
            return 1 if summary["errors"] else 0
        if args.action == "asset-upload":
            summary = upload_derived_assets_to_cloud(
                args.root,
                config,
                dry_run=args.dry_run,
                force=args.force,
                limit=args.limit,
                out=args.out,
            )
            print(
                "raw-cloud asset-upload | "
                f"files={summary['total_files']} bytes={summary['total_bytes']} "
                f"uploaded={summary['uploaded']} skipped={summary['skipped']} "
                f"planned={summary['planned']} dry_run={summary['dry_run']} "
                f"errors={len(summary['errors'])}"
            )
            return 1 if summary["errors"] else 0
        if args.action == "cleanup-manifests":
            report = cleanup_remote_json_manifests(config)
            print(
                "raw-cloud cleanup-manifests | "
                f"deleted={len(report['deleted'])} missing={len(report['missing'])} "
                f"remaining={len(report['remaining'])} errors={len(report['errors'])}"
            )
            for key in report["deleted"]:
                print(f"deleted: {key}")
            for key in report["missing"]:
                print(f"missing: {key}")
            for key in report["remaining"]:
                print(f"remaining: {key}")
            for item in report["errors"]:
                print(f"error: {item['key']} {item['error']}")
            return 1 if report["errors"] or report["remaining"] else 0
        if args.action == "verify":
            report = verify_raw_cloud(args.root, config, limit=args.limit)
            print(
                "raw-cloud verify | "
                f"files={report['total_files']} verified={report['verified']} issues={len(report['issues'])}"
            )
            return 1 if report["issues"] else 0
        if args.action == "restore":
            report = restore_raw_from_cloud(
                args.root,
                config,
                manifest_path=args.manifest,
                force=args.force,
                limit=args.limit,
            )
            print(
                "raw-cloud restore | "
                f"files={report['total_files']} restored={report['restored']} "
                f"skipped={report['skipped']} errors={len(report['errors'])}"
            )
            return 1 if report["errors"] else 0

    if args.command == "prepare-sources":
        results = prepare_raw_sources(
            root=args.root,
            force=args.force,
            page_range=args.pages,
            image_scale=args.image_scale,
            pages_per_job=args.pages_per_job,
            new_pages_limit=args.new_pages_limit,
            max_chars=args.max_chars,
        )
        print(f"Prepared {len(results)} raw source(s)")
        for result in results:
            print(f"- {result.status}: {result.source}")
            for job in result.conversion_jobs:
                print(f"  job: {job}")
            if result.converted_file:
                print(f"  converted: {result.converted_file}")
            if result.chunk_manifest:
                print(f"  chunks: {result.chunk_manifest}")
        return 0

    if args.command == "agent-queues":
        written = write_agent_queues(args.root, args.out_dir, stale_minutes=args.stale_minutes)
        for path in written:
            print(f"Wrote agent queue {path}")
        return 0

    if args.command == "source-prep-batches":
        output_path = write_source_prep_batches(
            root=args.root,
            output_dir=args.out_dir,
            max_pages=args.max_pages,
            limit=args.limit,
            stale_minutes=args.stale_minutes,
            statuses=args.status,
        )
        print(f"Wrote source-prep batch queue {output_path}")
        return 0

    if args.command == "cloud-source-prep-heartbeat":
        summary = cloud_source_prep_heartbeat(
            root=args.root,
            restore_raw=not args.no_restore,
            upload_assets=not args.no_asset_upload,
            research_analyzer=not args.no_research_analyzer,
            research_analyzer_limit=args.research_analyzer_limit,
            research_question_limit=args.research_question_limit,
            conversion_qc=args.conversion_qc,
            conversion_only=args.conversion_only,
            page_range=args.pages,
            restore_limit=args.restore_limit,
            pages_per_job=args.pages_per_job,
            new_pages_limit=args.new_pages_limit,
            batch_pages=args.batch_pages,
            queue_limit=args.queue_limit,
            stale_minutes=args.stale_minutes,
            max_chars=args.max_chars,
            fastlane_limit=args.fastlane_limit,
            fastlane_scan_limit=args.fastlane_scan_limit,
            dry_run=args.dry_run,
        )
        print("cloud-source-prep-heartbeat | summary")
        print(json.dumps(summary, indent=2, ensure_ascii=False))
        return 1 if summary.get("blockers") else 0

    if args.command == "sync-github-database":
        summary = sync_github_database(
            args.root,
            message=args.message,
            dry_run=args.dry_run,
            no_push=args.no_push,
            source_conversion_only=args.source_conversion_only,
        )
        print("sync-github-database | summary")
        print(json.dumps(summary, indent=2, ensure_ascii=False))
        return 0

    if args.command == "source-prep-fastlane":
        summary = source_prep_fastlane_run(
            root=args.root,
            limit=args.limit,
            scan_limit=args.scan_limit,
            agent=args.agent,
            stale_minutes=args.stale_minutes,
            dry_run=args.dry_run,
        )
        print(
            "source-prep-fastlane | "
            f"inspected={summary['inspected']} converted={summary['converted']} dry_run={summary['dry_run']}"
        )
        skipped = summary.get("skipped", {})
        if isinstance(skipped, dict) and skipped:
            print("skipped:")
            for reason, count in sorted(skipped.items()):
                print(f"- {reason}: {count}")
        converted_tasks = summary.get("converted_tasks", [])
        if isinstance(converted_tasks, list) and converted_tasks:
            print("converted tasks:")
            for task_id in converted_tasks[:25]:
                print(f"- {task_id}")
            if len(converted_tasks) > 25:
                print(f"- ... {len(converted_tasks) - 25} more")
        failed_tasks = summary.get("failed_tasks", [])
        if isinstance(failed_tasks, list) and failed_tasks:
            print("failed tasks:")
            for failure in failed_tasks[:25]:
                print(f"- {failure}")
            if len(failed_tasks) > 25:
                print(f"- ... {len(failed_tasks) - 25} more")
        return 0

    if args.command == "source-prep-docling-discovery":
        summary = source_prep_docling_discovery_run(
            root=args.root,
            limit=args.limit,
            scan_limit=args.scan_limit,
            agent=args.agent,
            stale_minutes=args.stale_minutes,
            dry_run=args.dry_run,
        )
        print(
            "source-prep-docling-discovery | "
            f"inspected={summary['inspected']} accepted={summary['accepted']} "
            f"unusable={summary['unusable']} errors={summary['errors']} dry_run={summary['dry_run']}"
        )
        blockers = summary.get("blockers", [])
        if isinstance(blockers, list) and blockers:
            print("blockers:")
            for blocker in blockers:
                print(f"- {blocker}")
        skipped = summary.get("skipped", {})
        if isinstance(skipped, dict) and skipped:
            print("skipped:")
            for reason, count in sorted(skipped.items()):
                print(f"- {reason}: {count}")
        return 1 if summary.get("blockers") else 0

    if args.command == "source-prep-review-page":
        review = review_source_prep_page_output_for_cli(args.root, args.output_path)
        print(json.dumps(review, indent=2, ensure_ascii=False))
        return 0 if str(review.get("status", "")) == "done" else 1

    if args.command == "gemini-source-prep":
        api_key = ""
        if args.api_key_env:
            api_key = os.environ.get(args.api_key_env, "")
            if not api_key and not args.dry_run:
                raise RuntimeError(f"{args.api_key_env} is required for gemini-source-prep.")
        summary = source_prep_gemini_run(
            root=args.root,
            limit=args.limit,
            queue_limit=args.queue_limit,
            stale_minutes=args.stale_minutes,
            api_key=api_key,
            lite_model=args.lite_model,
            pro_model=args.pro_model,
            max_output_tokens_lite=args.max_output_tokens_lite,
            max_output_tokens_pro=args.max_output_tokens_pro,
            crop_relevance=not args.no_crops,
            crop_count=args.crop_count,
            parallelism=args.parallelism,
            agent=args.agent,
            dry_run=args.dry_run,
            refresh_queue=not args.no_refresh_queue,
        )
        print("gemini-source-prep | summary")
        print(json.dumps(summary, indent=2, ensure_ascii=False))
        return 0

    if args.command == "source-relevance":
        if args.action == "list":
            payload = load_source_relevance_feedback(args.root)
            print(json.dumps(payload, indent=2, ensure_ascii=False))
            return 0
        path, hint = mark_source_relevance_feedback(
            args.root,
            task_id=args.task_id,
            job_manifest=args.job_manifest,
            source=args.source,
            source_sha256=args.source_sha256,
            converted_file=args.converted_file,
            page=args.page,
            relevance=args.relevance,
            treatment=args.treatment,
            reason=args.reason,
            entities=args.entity,
            terms=args.term,
            agent=args.agent,
        )
        print(f"Wrote source relevance feedback {path}")
        print(json.dumps(hint, indent=2, ensure_ascii=False))
        return 0

    if args.command == "research-analyzer":
        summary = research_analyzer_run(
            args.root,
            limit=args.limit,
            question_limit=args.question_limit,
            out=args.out,
            dry_run=args.dry_run,
        )
        print("research-analyzer | summary")
        print(json.dumps(summary, indent=2, ensure_ascii=False))
        return 1 if summary.get("blockers") else 0

    if args.command == "conversion-qc":
        written = write_post_conversion_qc(args.root, args.out_dir)
        print(f"Wrote {len(written)} conversion QC artifact(s)")
        return 0

    if args.command in {"source-status", "source-usability"}:
        written = write_source_usability_report(args.root, args.out, args.markdown)
        for path in written:
            print(f"Wrote source usability report {path}")
        return 0

    if args.command in {"system-status", "system-dashboard"}:
        written = write_system_status_dashboard(
            args.root,
            output=args.out,
            markdown_output=args.markdown,
            refresh_source_status=not args.no_refresh_source_status,
        )
        for path in written:
            print(f"Wrote system status dashboard {path}")
        return 0

    if args.command in {"storage-lifecycle", "storage-ranking"}:
        written = write_storage_lifecycle_report(
            args.root,
            output=args.out,
            markdown_output=args.markdown,
            record_dir=args.record_dir,
        )
        for path in written:
            print(f"Wrote storage lifecycle artifact {path}")
        return 0

    if args.command == "agent-task":
        status_by_action = {
            "claim": "claimed",
            "start": "in_progress",
            "complete": "done",
            "fail": "failed",
            "release": "released",
        }
        state_path = update_agent_task_states(
            args.root,
            args.task_id,
            status_by_action[args.action],
            agent=args.agent,
            note=args.note,
        )
        if not args.no_refresh:
            write_agent_queues(args.root)
        print(f"Updated agent task state {state_path} ({len(args.task_id)} task(s))")
        return 0

    if args.command == "prep-chunk":
        manifest_path = chunk_converted_markdown(
            root=args.root,
            converted_file=args.converted_file,
            output_dir=args.out_dir,
            max_chars=args.max_chars,
        )
        print(f"Wrote source preparation chunks {manifest_path}")
        return 0

    if args.command == "vault-transcriptions":
        written = sync_vault_transcriptions(args.root, force=args.force)
        if args.force:
            print(f"Synced {len(written)} vault transcription index/page notes")
        else:
            print(f"Synced {len(written)} vault transcription index/page notes; existing page notes were preserved")
        return 0

    if args.command == "promote-staged":
        summary = promote_staged_drafts(
            args.root,
            force=args.force,
            dry_run=args.dry_run,
            include_revise=args.include_revise,
            include_hold=args.include_hold,
        )
        print(
            "promote-staged | "
            f"source_packets={len(summary_list(summary, 'source_packets'))} "
            f"claims={len(summary_list(summary, 'claims'))} "
            f"relationships={len(summary_list(summary, 'relationships'))} "
            f"people={len(summary_list(summary, 'people'))} "
            f"sources={len(summary_list(summary, 'sources'))} "
            f"dry_run={summary['dry_run']}"
        )
        manifest = summary.get("manifest")
        if manifest:
            print(f"manifest: {manifest}")
        skipped = summary_list(summary, "skipped")
        if skipped:
            print("skipped:")
            for item in skipped[:25]:
                print(f"- {item}")
            if len(skipped) > 25:
                print(f"- ... {len(skipped) - 25} more")
        return 0

    if args.command == "claim":
        claim_path = create_claim(
            root=args.root,
            claim_id=args.id,
            claim_text=args.text,
            claim_type=args.type,
            subject=args.subject,
            source=args.source,
            status=args.status,
            confidence=args.confidence,
            predicate=args.predicate,
            object_value=args.object,
            claim_date=args.date,
            place=args.place,
            source_packet=args.source_packet,
            relationship=args.relationship,
            force=args.force,
        )
        print(f"Created claim {claim_path}")
        return 0

    if args.command == "relationship":
        relationship_path = create_relationship(
            root=args.root,
            relationship_id=args.id,
            relationship_type=args.type,
            person_a=args.person_a,
            person_b=args.person_b,
            status=args.status,
            confidence=args.confidence,
            supporting_claims=args.supporting_claim,
            conflicting_claims=args.conflicting_claim,
            force=args.force,
        )
        print(f"Created relationship {relationship_path}")
        return 0

    if args.command == "index":
        output = write_claim_index(args.root, args.out)
        print(f"Wrote claim index {output}")
        relationship_output = write_relationship_index(args.root)
        print(f"Wrote relationship index {relationship_output}")
        return 0

    if args.command == "graph":
        output = write_relationship_graph(args.root, args.out)
        print(f"Wrote relationship graph {output}")
        return 0

    if args.command == "tree":
        output = generate_tree(args.root, args.out)
        print(f"Wrote tree view {output}")
        return 0

    if args.command in {"site-build", "build-site"}:
        written = build_static_site(args.root, args.out_dir)
        print(f"Wrote static genealogy site files: {len(written)}")
        print(f"manifest: {(args.out_dir or Path('site')) / 'site-manifest.json'}")
        return 0

    if args.command == "narrative":
        output = compile_narrative(args.root, args.subject, args.out)
        print(f"Wrote narrative {output}")
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
