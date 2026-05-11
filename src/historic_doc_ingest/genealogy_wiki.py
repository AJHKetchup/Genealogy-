from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path


GENEALOGY_SCHEMA = """# Genealogy Wiki Operating Manual

This wiki follows the LLM-maintained wiki pattern, adapted for genealogical research.

## Layers

- `raw/`: immutable source material. Store original PDFs, images, downloaded records, exports, correspondence, and converted Markdown from document ingestion here. Do not edit these files after ingest.
- `wiki/`: LLM-maintained Markdown knowledge base. This is the working research brain.
- `wiki/index.md`: lineage-first catalog of families, branches, people, relationships, events, places, sources, claims, narratives, and open questions.
- `wiki/log.md`: append-only chronological record of ingests, queries, conclusions, corrections, and lint passes.
- `wiki/research-plan.md`: prioritized open work, next searches, and hypotheses to test.

## Genealogy Rules

- Do not merge two people unless evidence supports identity. Keep possible duplicates separate and cross-link them as candidates.
- Every fact about a person, relationship, event, name variant, date, or place needs a source citation or an explicit `unsourced` marker.
- Distinguish evidence from conclusion. A record may say something; the wiki may conclude something else after weighing conflicts.
- Preserve uncertainty. Use `about`, `before`, `after`, `between`, `possibly`, and `probably` instead of inventing precision.
- Track negative evidence, such as searched collections where a person was not found.
- Keep original spelling, place names, and record language in source notes. Normalize only in separate interpretation fields.
- Prefer small, linked pages over giant narrative dumps.
- Treat atomic claims as the foundation of the system. A biography, family tree, or narrative may summarize claims, but claims are the auditable units.
- Keep relationship assertions separate from person pages and assign relationship type, status, confidence, and evidence.
- Keep source transcription, translation, interpretation, and uncertainty in separate sections.
- Context research is allowed only when tied to a person, relationship, event, place, source, photo, or narrative chapter.

## Lineage-First Architecture

Organize from lineage goals outward:

Family -> Branch -> Person -> Relationship -> Event -> Place -> Source -> Claim -> Narrative.

The wiki can still cross-link freely, but this hierarchy is the default path for research and review.

## Ingest Workflow

When a new source arrives:

1. Add it to `raw/sources/` or `raw/converted/`.
2. Create or update one page under `wiki/sources/`.
3. Create a source packet under `wiki/source-packets/` with separated transcription, translation, interpretation, and uncertainty sections.
4. Extract asserted facts into atomic claim pages under `wiki/claims/`.
5. Create or update relationship assertions under `wiki/relationships/`.
6. Update person, family, branch, place, event, photo, conflict, identity-candidate, and task pages as needed.
7. Update `wiki/index.md`.
8. Append an entry to `wiki/log.md`.

## Query Workflow

When answering a genealogy question:

1. Read `wiki/index.md` first.
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
- Open questions that have no next action.
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
- Relationships: `relationships/R001-person-person-relationship.md`
- Events: `events/EV001-short-event.md`
- Sources: `sources/S001-short-title.md`
- Source packets: `source-packets/SP001-short-title.md`
- Claims: `claims/CL001-short-claim.md`
- Identity: `identity/ID001-person-candidates.md`
- Photos: `photos/PH001-short-description.md`
- Face clusters: `photos/FC001-unknown-cluster.md`
- Tasks: `tasks/T001-short-task.md`
- Narratives: `narratives/N001-short-title.md`
- Conflicts: `conflicts/C001-short-topic.md`
- Questions: `questions/Q001-short-question.md`
"""


INDEX_TEMPLATE = """# Genealogy Wiki Index

## People

## Branches

## Families

## Relationships

## Events

## Places

## Sources

## Source Packets

## Claims

## Evidence

## Conflicts

## Identity Resolution

## Photos And Face Clusters

## Research Questions

## Research Tasks

## Narratives

## Context

## Timelines
"""


LOG_TEMPLATE = """# Genealogy Wiki Log

## [{today}] init | Genealogy wiki created

- Created raw source layer, wiki layer, schema, index, log, and templates.
"""


RESEARCH_PLAN_TEMPLATE = """# Research Plan

## Priority Questions

## Next Searches

## Hypotheses To Test

## Negative Searches

## Lineage Goals
"""


TEMPLATES = {
    "branch.md": """---
type: branch
status: draft
tags: [branch]
family:
focus_people: []
---

# Branch Name

## Lineage Goal

## Key People

## Proven Relationships

## Probable Or Possible Relationships

## Open Problems

## Sources
""",
    "person.md": """---
type: person
status: draft
tags: [person]
person_id:
birth_year:
death_year:
---

# Person Name

## Identity

- Preferred name:
- Name variants:
- Sex/gender:
- Birth:
- Death:
- Burial:

## Relationships

- Parents: link to `wiki/relationships/` pages.
- Spouses: link to `wiki/relationships/` pages.
- Children: link to `wiki/relationships/` pages.
- Siblings: link to `wiki/relationships/` pages.
- Same-person candidates: link to `wiki/identity/` pages.

## Timeline

| Date | Event | Place | Evidence |
| --- | --- | --- | --- |

## Evidence Summary

## Atomic Claims

## Conflicts And Uncertainty

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
status: draft
tags: [family]
family_id:
branch:
---

# Family

## Couple Or Household

## Children

## Timeline

| Date | Event | Place | Evidence |
| --- | --- | --- | --- |

## Relationship Evidence

## Relationship Assertions

## Conflicts And Uncertainty

## Sources
""",
    "source.md": """---
type: source
status: draft
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
- Reliability:

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
raw_file:
created:
tags: [source-packet]
---

# Source Packet

## Source Identity

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
relationship:
tags: [claim]
---

# Atomic Claim

## Claim

## Status

Use one of: `draft`, `accepted`, `probable`, `possible`, `disputed`, `rejected`.

## Confidence

Use a 0-10 score and explain why.

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

## Draft Narrative

Write only from accepted or probable wiki claims. Do not write directly from raw sources.

## Timeline

## Photo Captions

## Historical Context

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

Context is allowed only when linked to a person, relationship, place, event, source, photo, or narrative chapter.

## Context Summary

## Relevance To The Lineage

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


REQUIRED_DIRECTORIES = [
    ("raw", "sources"),
    ("raw", "converted"),
    ("raw", "assets"),
    ("wiki", "branches"),
    ("wiki", "people"),
    ("wiki", "families"),
    ("wiki", "relationships"),
    ("wiki", "events"),
    ("wiki", "places"),
    ("wiki", "sources"),
    ("wiki", "source-packets"),
    ("wiki", "claims"),
    ("wiki", "evidence"),
    ("wiki", "conflicts"),
    ("wiki", "identity"),
    ("wiki", "photos"),
    ("wiki", "questions"),
    ("wiki", "tasks"),
    ("wiki", "narratives"),
    ("wiki", "context"),
    ("wiki", "timelines"),
    ("wiki", "trees"),
    ("wiki", "_indexes"),
    ("wiki", "_templates"),
]


@dataclass(frozen=True)
class WikiPaths:
    root: Path

    @property
    def raw(self) -> Path:
        return self.root / "raw"

    @property
    def wiki(self) -> Path:
        return self.root / "wiki"

    @property
    def templates(self) -> Path:
        return self.wiki / "_templates"


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


def init_genealogy_wiki(root: Path, force: bool = False) -> list[Path]:
    paths = WikiPaths(root.resolve())
    created: list[Path] = []

    for parts in REQUIRED_DIRECTORIES:
        directory = paths.root.joinpath(*parts)
        directory.mkdir(parents=True, exist_ok=True)
        created.append(directory)

    write_file(paths.root / "GENEALOGY_WIKI.md", GENEALOGY_SCHEMA, force, created)
    write_file(paths.wiki / "index.md", INDEX_TEMPLATE, force, created)
    write_file(paths.wiki / "log.md", LOG_TEMPLATE.format(today=date.today().isoformat()), force, created)
    write_file(paths.wiki / "research-plan.md", RESEARCH_PLAN_TEMPLATE, force, created)

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
        paths.wiki,
        paths.wiki / "claims",
        paths.wiki / "relationships",
        paths.wiki / "source-packets",
        paths.wiki / "tasks",
        paths.wiki / "narratives",
        paths.wiki / "_indexes",
        paths.wiki / "index.md",
        paths.wiki / "log.md",
        paths.wiki / "research-plan.md",
        paths.root / "GENEALOGY_WIKI.md",
    ]
    for path in required:
        if not path.exists():
            issues.append(f"missing required path: {path}")

    if not paths.wiki.exists():
        return issues

    index_text = read_text(paths.wiki / "index.md")
    for page in paths.wiki.rglob("*.md"):
        if "_templates" in page.parts or page.name in {"index.md", "log.md", "research-plan.md"}:
            continue
        rel = page.relative_to(paths.wiki).as_posix()
        if rel not in index_text and f"[[{rel.removesuffix('.md')}]]" not in index_text:
            issues.append(f"page not referenced from index: {rel}")
        text = read_text(page)
        frontmatter = parse_frontmatter(text)
        if "type: person" in text and "[[" not in text:
            issues.append(f"person page has no wiki links: {rel}")
        if "type: source" in text and "## Extracted Claims" not in text:
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

    claim_index = build_claim_index(paths.root)
    issues.extend(lint_claim_cross_references(paths.root, claim_index))
    relationship_index = build_relationship_index(paths.root, claim_index)
    issues.extend(lint_relationship_cross_references(paths.root, relationship_index, claim_index))
    issues.extend(lint_chronology(paths.wiki))

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
    claims_dir = paths.wiki / "claims"
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
    append_log(paths.wiki / "log.md", f"claim | Created {claim_path.relative_to(paths.root).as_posix()}")
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
    relationships_dir = paths.wiki / "relationships"
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
    append_log(paths.wiki / "log.md", f"relationship | Created {relationship_path.relative_to(paths.root).as_posix()}")
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
    packets_dir = paths.wiki / "source-packets"
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
    append_log(paths.wiki / "log.md", f"source-packet | Created {packet_path.relative_to(paths.root).as_posix()}")
    return packet_path


def build_claim_index(root: Path) -> list[ClaimRecord]:
    paths = WikiPaths(root.resolve())
    records: list[ClaimRecord] = []
    for page in sorted((paths.wiki / "claims").glob("*.md")):
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
    for page in sorted((paths.wiki / "relationships").glob("*.md")):
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
    output = output or (paths.wiki / "_indexes" / "claims.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    claims = [asdict(record) for record in build_claim_index(paths.root)]
    output.write_text(json.dumps({"claims": claims}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return output


def write_relationship_index(root: Path, output: Path | None = None) -> Path:
    paths = WikiPaths(root.resolve())
    output = output or (paths.wiki / "_indexes" / "relationships.json")
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
    output = output or (paths.wiki / "_indexes" / "relationship-graph.json")
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
    output = output or (paths.wiki / "trees" / "family-tree.md")
    output.parent.mkdir(parents=True, exist_ok=True)
    relationship_pages = list((paths.wiki / "relationships").glob("*.md"))

    lines = [
        "---",
        "type: tree",
        "status: generated",
        "tags: [tree]",
        "---",
        "",
        "# Family Tree View",
        "",
        "```mermaid",
        "flowchart TD",
    ]
    warnings: list[str] = []
    link_styles: list[str] = []
    for page in relationship_pages:
        frontmatter = parse_frontmatter(read_text(page))
        person_a = frontmatter.get("person_a")
        person_b = frontmatter.get("person_b")
        relationship_type = frontmatter.get("relationship_type", "relationship")
        status = frontmatter.get("status", "draft")
        confidence = frontmatter.get("confidence", "0.0")
        if not person_a or not person_b:
            warnings.append(f"- Missing endpoint in {page.relative_to(paths.root).as_posix()}")
            continue
        lines.append(
            f"  {node_id(person_a)}[{mermaid_label(person_a)}] -->|{relationship_type} {status} {confidence}| "
            f"{node_id(person_b)}[{mermaid_label(person_b)}]"
        )
        link_styles.append(edge_style(status, confidence))

    if len(lines) == 10:
        lines.append("  empty[No relationship pages found]")
    for index, style in enumerate(link_styles):
        lines.append(f"  linkStyle {index} {style}")
    lines.extend(["```", ""])
    if warnings:
        lines.extend(["## Duplicate Or Relationship Warnings", *warnings, ""])
    lines.append("Generated from `wiki/relationships/`, not from a separate database.")
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
        "claim_scope: accepted_probable",
        "---",
        "",
        f"# {subject}",
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

    lines.extend(["", "## Uncertainty Notes", "", "This narrative was compiled only from accepted or probable claim pages."])
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return output


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
            if not wiki_target_exists(paths.wiki, target):
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


def lint_chronology(wiki: Path) -> list[str]:
    issues: list[str] = []
    people = load_people(wiki / "people")
    for page in (wiki / "relationships").glob("*.md"):
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
        rel = page.relative_to(wiki).as_posix()
        if parent_birth > child_birth:
            issues.append(f"chronology impossible, parent born after child: {rel}")
        if child_birth - parent_birth < 12:
            issues.append(f"chronology suspicious, parent younger than 12 at child birth: {rel}")
    issues.extend(lint_event_chronology(wiki, people))
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
    return "[" + ", ".join(values) + "]"


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
    index_parser.add_argument("--out", type=Path, help="Claim index output path. Default: wiki/_indexes/claims.json.")

    graph_parser = subparsers.add_parser("graph", help="Write a relationship graph JSON view.")
    graph_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    graph_parser.add_argument("--out", type=Path, help="Output path. Default: wiki/_indexes/relationship-graph.json.")

    tree_parser = subparsers.add_parser("tree", help="Generate a Mermaid family tree view from relationship pages.")
    tree_parser.add_argument("--root", type=Path, default=Path("."), help="Workspace root. Default: current directory.")
    tree_parser.add_argument("--out", type=Path, help="Output Markdown path. Default: wiki/trees/family-tree.md.")

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

    if args.command == "narrative":
        output = compile_narrative(args.root, args.subject, args.out)
        print(f"Wrote narrative {output}")
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
