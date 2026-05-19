from __future__ import annotations

import html
import hashlib
import json
import os
import re
import shutil
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote


WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
INLINE_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
DATE_RE = re.compile(r"\b(1[5-9]\d{2}|20\d{2})(?:[-/](\d{1,2})(?:[-/](\d{1,2}))?)?\b")
SOURCE_META_RE = re.compile(r"^-\s+(?:\*\*)?([^:*`]+?)(?:\*\*)?:\s*(.*)$")
PAGE_RANGE_RE = re.compile(r"-p(\d{4})(?:-(\d{4}))?", re.IGNORECASE)

WIKI_ONLY_EXCLUDE_DIRS = {"_templates"}
RESEARCH_EXCLUDE_DIRS = {
    "_agent-queues",
    "_automation",
    "_conversion-review",
    "_staging",
    "_templates",
}
RESEARCH_EXCLUDE_FILES = {"log.md"}

FOCUS_TERMS = {
    "Pulgar": ["pulgar"],
    "Arriagada": ["arriagada"],
    "Dario": ["dario", "dario jose", "dario arturo"],
    "Jose": ["jose"],
    "Victor": ["victor", "victor manuel"],
    "Geneva": ["geneva", "ginebra", "geneve"],
    "The Hague": ["la haye", "hague", "haya"],
    "Los Angeles": ["los angeles"],
    "Concepcion": ["concepcion"],
    "Passenger": ["passenger", "arrival", "departure"],
    "Birth records": ["nacimiento", "nacimientos", "birth register"],
}

TIMELINE_SECTIONS = {
    "claims",
    "events",
    "families",
    "identity",
    "narratives",
    "people",
    "photos",
    "places",
    "relationships",
    "source-packets",
    "sources",
}

SECTION_LABELS = {
    "branches": "Branches",
    "claims": "Claims",
    "conflicts": "Conflicts",
    "context": "Context",
    "events": "Events",
    "evidence": "Evidence",
    "families": "Families",
    "identity": "Identity",
    "narratives": "Narratives",
    "people": "People",
    "photos": "Photos",
    "places": "Places",
    "questions": "Questions",
    "relationships": "Relationships",
    "source-packets": "Source Packets",
    "sources": "Sources",
    "tasks": "Tasks",
    "timelines": "Timelines",
    "trees": "Trees",
}


@dataclass
class SitePage:
    source_path: Path
    source_root: str
    vault_rel: str
    site_rel: str
    title: str
    frontmatter: dict[str, str]
    body: str
    section: str
    page_type: str
    text: str
    links: list[str] = field(default_factory=list)
    dates: list[str] = field(default_factory=list)


def build_wiki_site(root: Path, output: Path | None = None, include_research: bool = True) -> Path:
    """Build a static, searchable HTML view of the genealogy wiki."""
    root = root.resolve()
    output = (output or root / "site").resolve()
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True, exist_ok=True)
    (output / "assets").mkdir(parents=True, exist_ok=True)

    pages = collect_pages(root, include_research=include_research)
    link_map = build_link_map(pages)
    for page in pages:
        page.links = extract_wikilink_targets(page.body)
        page.dates = extract_page_dates(page)

    data = build_site_data(root, pages, link_map)
    write_text(output / ".nojekyll", "")
    write_text(output / "assets" / "site-data.js", "window.GENEALOGY_SITE_DATA = " + json.dumps(data, ensure_ascii=False) + ";\n")
    write_text(output / "assets" / "styles.css", SITE_CSS)
    write_text(output / "assets" / "app.js", SITE_JS)

    write_text(output / "index.html", render_home_page(pages, data))
    write_text(output / "graph.html", render_special_page("Research Graph", graph_body()))
    write_text(output / "timeline.html", render_special_page("Timeline", timeline_body()))
    write_text(output / "collections.html", render_special_page("Collections", collections_body()))
    write_text(output / "sources.html", render_special_page("Sources", sources_body()))

    for page in pages:
        html_path = output / page.site_rel
        html_path.parent.mkdir(parents=True, exist_ok=True)
        write_text(html_path, render_markdown_page(page, pages, link_map))

    return output


def collect_pages(root: Path, include_research: bool = True) -> list[SitePage]:
    pages: list[SitePage] = []
    wiki_root = root / "wiki"
    if wiki_root.exists():
        for path in sorted(wiki_root.rglob("*.md")):
            if any(part in WIKI_ONLY_EXCLUDE_DIRS for part in path.relative_to(wiki_root).parts):
                continue
            pages.append(read_site_page(path, root, "wiki"))

    if include_research:
        research_root = root / "research"
        if research_root.exists():
            for path in sorted(research_root.rglob("*.md")):
                rel_parts = path.relative_to(research_root).parts
                if not rel_parts:
                    continue
                if rel_parts[0] in RESEARCH_EXCLUDE_DIRS or path.name in RESEARCH_EXCLUDE_FILES:
                    continue
                pages.append(read_site_page(path, root, "research"))

        converted_root = root / "raw" / "converted"
        if converted_root.exists():
            for path in sorted(converted_root.glob("*.md")):
                if path.name == ".gitkeep":
                    continue
                pages.append(read_converted_source_page(path, root))

    return pages


def read_site_page(path: Path, root: Path, source_root: str) -> SitePage:
    source_base = root / source_root
    vault_rel = path.relative_to(source_base).as_posix()
    text = read_text_file(path)
    frontmatter, body = split_frontmatter(text)
    title = frontmatter.get("display_name") or frontmatter.get("title") or extract_title(body) or prettify_stem(path.stem)
    section = page_section(vault_rel)
    page_type = frontmatter.get("type") or section.rstrip("s") or "page"
    return SitePage(
        source_path=path,
        source_root=source_root,
        vault_rel=vault_rel,
        site_rel=site_rel_for(source_root, vault_rel),
        title=title,
        frontmatter=frontmatter,
        body=body,
        section=section,
        page_type=page_type,
        text=plain_text(body),
    )


def read_converted_source_page(path: Path, root: Path) -> SitePage:
    raw_text = read_text_file(path, errors="replace")
    display_text = repair_mojibake(raw_text)
    title = extract_title(display_text) or prettify_source_name(path.stem)
    metadata = extract_source_metadata(display_text)
    metadata.setdefault("converted_path", path.relative_to(root).as_posix())
    metadata.setdefault("type", "converted-source")
    date_values = extract_dates(title)
    if date_values:
        metadata.setdefault("date", date_values[0])
    return SitePage(
        source_path=path,
        source_root="converted",
        vault_rel=path.relative_to(root / "raw" / "converted").as_posix(),
        site_rel=f"sources/{source_slug(path)}.html",
        title=title,
        frontmatter=metadata,
        body=display_text,
        section="sources",
        page_type="converted-source",
        text=plain_text(display_text),
    )


def repair_mojibake(value: str) -> str:
    if "Ã" not in value and "Â" not in value and "â" not in value:
        return value
    original_badness = mojibake_badness(value)
    for encoding in ("cp1252", "latin1"):
        try:
            candidate = value.encode(encoding, errors="ignore").decode("utf-8", errors="ignore")
        except UnicodeError:
            continue
        if candidate and mojibake_badness(candidate) < original_badness:
            return candidate
    return value


def mojibake_badness(value: str) -> int:
    return value.count("Ã") + value.count("Â") + value.count("â")


def read_text_file(path: Path, errors: str = "strict") -> str:
    try:
        return path.read_text(encoding="utf-8", errors=errors)
    except FileNotFoundError:
        if os.name != "nt":
            raise
        long_path = "\\\\?\\" + str(path.resolve())
        with open(long_path, encoding="utf-8", errors=errors) as handle:
            return handle.read()


def extract_source_metadata(text: str) -> dict[str, str]:
    metadata: dict[str, str] = {}
    for line in text.splitlines()[:80]:
        match = SOURCE_META_RE.match(line.strip())
        if not match:
            continue
        key = slugify(match.group(1)).replace("-", "_")
        value = match.group(2).strip().strip("`")
        if value:
            metadata[key] = value
    return metadata


def source_slug(path: Path) -> str:
    slug = slugify(path.stem.removesuffix(".codex"))
    if len(slug) <= 96:
        return slug
    digest = hashlib.sha1(path.name.encode("utf-8")).hexdigest()[:10]
    return f"{slug[:82].rstrip('-')}-{digest}"


def prettify_source_name(stem: str) -> str:
    stem = stem.removesuffix(".codex")
    stem = re.sub(r"^ca[0-9a-f]{8,12}-", "", stem, flags=re.IGNORECASE)
    stem = PAGE_RANGE_RE.sub("", stem)
    return prettify_stem(stem)


def split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values, text[match.end() :]


def extract_title(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def plain_text(markdown: str) -> str:
    text = FRONTMATTER_RE.sub("", markdown)
    text = WIKILINK_RE.sub(lambda m: m.group(1).split("|")[-1], text)
    text = re.sub(r"`{1,3}", "", text)
    text = re.sub(r"[*_#>\-|]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def page_section(vault_rel: str) -> str:
    parts = vault_rel.split("/")
    if len(parts) == 1:
        return "home" if parts[0].lower() == "index.md" else "overview"
    return parts[0]


def site_rel_for(source_root: str, vault_rel: str) -> str:
    parts = vault_rel.split("/")
    parts[-1] = slugify(Path(parts[-1]).stem) + ".html"
    return "/".join([source_root, *parts])


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "page"


def prettify_stem(stem: str) -> str:
    return re.sub(r"[-_]+", " ", stem).strip().title()


def build_link_map(pages: list[SitePage]) -> dict[str, SitePage]:
    mapping: dict[str, SitePage] = {}
    for page in pages:
        rel_no_ext = str(Path(page.vault_rel).with_suffix("")).replace("\\", "/")
        candidates = {
            rel_no_ext,
            f"{page.source_root}/{rel_no_ext}",
            Path(rel_no_ext).name,
            page.title,
        }
        for candidate in candidates:
            key = normalize_link_key(candidate)
            mapping.setdefault(key, page)
    return mapping


def normalize_link_key(value: str) -> str:
    value = value.strip().replace("\\", "/")
    value = value.split("#", 1)[0]
    if value.endswith(".md"):
        value = value[:-3]
    return value.strip("/").lower()


def extract_wikilink_targets(text: str) -> list[str]:
    targets: list[str] = []
    for match in WIKILINK_RE.finditer(text):
        target = match.group(1).split("|", 1)[0].split("#", 1)[0].strip()
        if target:
            targets.append(target)
    return targets


def extract_page_dates(page: SitePage) -> list[str]:
    candidates = [
        page.frontmatter.get("date", ""),
        page.frontmatter.get("year", ""),
        page.frontmatter.get("birth", ""),
        page.frontmatter.get("death", ""),
        page.frontmatter.get("created", ""),
        page.frontmatter.get("updated", ""),
    ]
    if page.source_root == "converted":
        candidates.append(page.title)
        matches: list[str] = []
        for value in candidates:
            matches.extend(date for date in extract_dates(value) if date not in matches)
        return matches[:2]
    matches: list[str] = []
    for value in candidates:
        matches.extend(date for date in extract_dates(value) if date not in matches)
    for date in extract_dates(page.body):
        if date not in matches:
            matches.append(date)
        if len(matches) >= 3:
            break
    return matches


def extract_dates(value: str) -> list[str]:
    value = suppress_broad_date_ranges(value or "")
    dates: list[str] = []
    for match in DATE_RE.finditer(value):
        year, month, day = match.groups()
        if month and day:
            dates.append(f"{int(year):04d}-{int(month):02d}-{int(day):02d}")
        elif month:
            dates.append(f"{int(year):04d}-{int(month):02d}")
        else:
            dates.append(f"{int(year):04d}")
    return dates


def suppress_broad_date_ranges(value: str) -> str:
    def replace(match: re.Match[str]) -> str:
        start = int(match.group(1))
        end = int(match.group(2))
        return " " if abs(end - start) > 50 else match.group(0)

    return re.sub(r"\b(1[5-9]\d{2}|20\d{2})\s*[-\u2013\u2014]\s*(1[5-9]\d{2}|20\d{2})\b", replace, value)


def build_site_data(root: Path, pages: list[SitePage], link_map: dict[str, SitePage]) -> dict[str, object]:
    page_items = []
    graph_edges = []
    chunk_stats = collect_chunk_stats(root)
    queue_summaries = collect_queue_summaries(root)
    source_summaries = build_source_summaries(root, pages, chunk_stats)
    for page in pages:
        page_items.append(
            {
                "id": page.site_rel,
                "title": page.title,
                "url": page.site_rel,
                "sourceRoot": page.source_root,
                "vaultRel": page.vault_rel,
                "section": page.section,
                "type": page.page_type,
                "snippet": page.text[:260],
                "dates": page.dates,
            }
        )
        for target in page.links:
            resolved = link_map.get(normalize_link_key(target))
            if resolved:
                graph_edges.append({"source": page.site_rel, "target": resolved.site_rel, "type": "wikilink"})

    graph_edges.extend(source_focus_edges(source_summaries))
    page_by_url = {page.site_rel: page for page in pages}
    for edge in relationship_edges_from_index(root, page_by_url, link_map):
        graph_edges.append(edge)

    counts = Counter(page.section for page in pages)
    timeline_items = [
        {
            "date": date,
            "title": page.title,
            "url": page.site_rel,
            "section": page.section,
            "type": page.page_type,
        }
        for page in pages
        if include_in_timeline(page)
        for date in page.dates
    ]
    timeline_items.sort(key=lambda item: item["date"])
    deduped_edges = dedupe_edges(graph_edges)
    graph_nodes = build_graph_nodes(page_items, deduped_edges, source_summaries)
    dashboard = build_dashboard(root, pages, source_summaries, chunk_stats, queue_summaries, timeline_items)

    return {
        "generatedAt": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "pages": page_items,
        "links": deduped_edges,
        "graphNodes": graph_nodes,
        "counts": dict(sorted(counts.items())),
        "timeline": timeline_items[:500],
        "dashboard": dashboard,
        "sections": [
            {"id": section, "label": section_label(section), "count": count}
            for section, count in sorted(counts.items())
        ],
    }


def load_json(path: Path) -> object:
    if not path.exists():
        return {}
    try:
        return json.loads(read_text_file(path))
    except (OSError, json.JSONDecodeError):
        return {}


def normalize_repo_path(value: object) -> str:
    return str(value or "").replace("\\", "/").strip()


def collect_chunk_stats(root: Path) -> dict[str, object]:
    by_converted: dict[str, dict[str, object]] = {}
    parent_to_converted: dict[str, str] = {}
    manifest_count = 0
    chunk_count = 0
    chunks_root = root / "raw" / "chunks"
    for manifest in sorted(chunks_root.glob("*/manifest.json")) if chunks_root.exists() else []:
        payload = load_json(manifest)
        if not isinstance(payload, dict):
            continue
        converted = normalize_repo_path(payload.get("converted_file"))
        chunks = payload.get("chunks") if isinstance(payload.get("chunks"), list) else []
        manifest_count += 1
        chunk_count += len(chunks)
        if converted:
            info = by_converted.setdefault(
                converted,
                {"manifest_count": 0, "chunk_count": 0, "page_count": 0, "manifests": []},
            )
            info["manifest_count"] = int(info.get("manifest_count", 0)) + 1
            info["chunk_count"] = int(info.get("chunk_count", 0)) + len(chunks)
            info["manifests"] = [*list(info.get("manifests", [])), manifest.relative_to(root).as_posix()]
            pages = {
                chunk.get("page_start")
                for chunk in chunks
                if isinstance(chunk, dict) and chunk.get("page_start") is not None
            }
            info["page_count"] = int(info.get("page_count", 0)) + len(pages)
            parent_to_converted[manifest.parent.relative_to(root).as_posix()] = converted
    return {
        "manifest_count": manifest_count,
        "chunk_count": chunk_count,
        "by_converted": by_converted,
        "parent_to_converted": parent_to_converted,
    }


def collect_queue_summaries(root: Path) -> list[dict[str, object]]:
    queue_specs = [
        ("conversion-qa", "Conversion QA"),
        ("evidence-extraction", "Evidence Extraction"),
        ("proof-review", "Proof Review"),
        ("wiki-promotion", "Wiki Promotion"),
    ]
    summaries: list[dict[str, object]] = []
    for queue_id, label in queue_specs:
        path = root / "research" / "_agent-queues" / f"{queue_id}.json"
        payload = load_json(path)
        if not isinstance(payload, dict):
            summaries.append({"id": queue_id, "label": label, "total": 0, "statusCounts": {}, "path": path.relative_to(root).as_posix(), "missing": True})
            continue
        tasks = payload.get("tasks") if isinstance(payload.get("tasks"), list) else []
        status_counts = payload.get("status_counts") if isinstance(payload.get("status_counts"), dict) else Counter(
            str(task.get("status") or "unknown") for task in tasks if isinstance(task, dict)
        )
        summaries.append(
            {
                "id": queue_id,
                "label": label,
                "total": int(payload.get("task_count") or len(tasks)),
                "statusCounts": dict(status_counts),
                "path": path.relative_to(root).as_posix(),
                "missing": False,
            }
        )
    return summaries


def build_source_summaries(root: Path, pages: list[SitePage], chunk_stats: dict[str, object]) -> list[dict[str, object]]:
    qc_by_converted = qc_index_by_converted(root)
    usability_by_converted = usability_index_by_converted(root)
    by_converted = chunk_stats.get("by_converted") if isinstance(chunk_stats.get("by_converted"), dict) else {}
    source_pages = [page for page in pages if page.source_root == "converted"]
    summaries: list[dict[str, object]] = []
    for page in source_pages:
        converted_path = normalize_repo_path(page.frontmatter.get("converted_path") or page.source_path.relative_to(root).as_posix())
        chunk_info = by_converted.get(converted_path, {}) if isinstance(by_converted, dict) else {}
        qc = qc_by_converted.get(converted_path, {})
        usability = usability_by_converted.get(converted_path, {})
        terms = matched_focus_terms(f"{page.title} {page.text}")
        dates = page.dates[:3]
        status = str(usability.get("status") or "converted")
        summary = {
            "id": page.site_rel,
            "title": page.title,
            "url": page.site_rel,
            "path": converted_path,
            "source": page.frontmatter.get("source", ""),
            "status": status,
            "sourcePrepStatus": usability.get("source_prep_status", ""),
            "sourceGroup": usability.get("id", ""),
            "documentType": page.frontmatter.get("document_type", ""),
            "language": page.frontmatter.get("language", ""),
            "location": page.frontmatter.get("location", ""),
            "pageRange": source_page_range(page.source_path.name),
            "dates": dates,
            "chunks": int(chunk_info.get("chunk_count", 0)) if isinstance(chunk_info, dict) else 0,
            "chunkManifests": int(chunk_info.get("manifest_count", 0)) if isinstance(chunk_info, dict) else 0,
            "qcQueuedPages": int(qc.get("queued_pages", 0) or 0) if isinstance(qc, dict) else 0,
            "qcSuspectedCorrections": int(qc.get("suspected_corrections", 0) or 0) if isinstance(qc, dict) else 0,
            "qcHoldCount": int(usability.get("qc_hold_count", 0) or 0) if isinstance(usability, dict) else 0,
            "terms": terms,
            "snippet": source_excerpt(page),
        }
        summary["score"] = source_priority_score(summary)
        summaries.append(summary)
    summaries.sort(key=lambda item: (-int(item.get("score", 0)), str(item.get("title", "")).lower()))
    return summaries


def qc_index_by_converted(root: Path) -> dict[str, dict[str, object]]:
    payload = load_json(root / "research" / "_conversion-review" / "qc-index.json")
    if not isinstance(payload, dict):
        return {}
    output: dict[str, dict[str, object]] = {}
    for source in payload.get("sources", []):
        if not isinstance(source, dict):
            continue
        converted = normalize_repo_path(source.get("converted_file"))
        if converted:
            output[converted] = source
    return output


def usability_index_by_converted(root: Path) -> dict[str, dict[str, object]]:
    payload = load_json(root / "research" / "_indexes" / "source-usability.json")
    if not isinstance(payload, dict):
        return {}
    output: dict[str, dict[str, object]] = {}
    for source in payload.get("sources", []):
        if not isinstance(source, dict):
            continue
        for converted in source.get("converted_files", []) if isinstance(source.get("converted_files"), list) else []:
            output[normalize_repo_path(converted)] = source
    return output


def source_page_range(filename: str) -> str:
    match = PAGE_RANGE_RE.search(filename)
    if not match:
        return ""
    start, end = match.groups()
    if end and end != start:
        return f"{int(start)}-{int(end)}"
    return str(int(start))


def matched_focus_terms(text: str) -> list[str]:
    normalized = repair_mojibake(text).lower()
    matched = []
    for label, variants in FOCUS_TERMS.items():
        if any(variant in normalized for variant in variants):
            matched.append(label)
    return matched


def source_excerpt(page: SitePage) -> str:
    sections = ["## Layout And Reading Order", "## Literal Transcription", "## Page Metadata"]
    for section in sections:
        start = page.body.find(section)
        if start < 0:
            continue
        end = page.body.find("\n## ", start + len(section))
        block = page.body[start:end if end > start else len(page.body)]
        excerpt = first_meaningful_source_line(block)
        if excerpt:
            return excerpt
    return first_meaningful_source_line(page.body) or page.text[:260]


def first_meaningful_source_line(text: str) -> str:
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("- Source") or line.startswith("- Manifest") or line.startswith("- Conversion"):
            continue
        if line.startswith("- Extracted images") or line.startswith("- Source SHA"):
            continue
        if line.startswith("|") or line.startswith("```"):
            continue
        text = plain_text(line)
        if len(text) >= 60:
            return text[:260]
    return ""


def source_priority_score(summary: dict[str, object]) -> int:
    score = len(summary.get("terms", [])) * 20
    status = str(summary.get("status", ""))
    if "usable" in status:
        score += 12
    if summary.get("qcHoldCount"):
        score += 8
    if summary.get("qcQueuedPages") or summary.get("qcSuspectedCorrections"):
        score += 6
    if summary.get("dates"):
        score += 4
    score += min(10, int(summary.get("chunks", 0) or 0))
    return score


def source_focus_edges(source_summaries: list[dict[str, object]]) -> list[dict[str, str]]:
    edges: list[dict[str, str]] = []
    for source in source_summaries[:40]:
        for term in source.get("terms", [])[:4]:
            edges.append({"source": str(source["id"]), "target": f"focus:{slugify(str(term))}", "type": "mentions"})
    return edges


def build_graph_nodes(page_items: list[dict[str, object]], edges: list[dict[str, str]], source_summaries: list[dict[str, object]]) -> list[dict[str, object]]:
    page_by_id = {str(page["id"]): page for page in page_items}
    connected = {edge["source"] for edge in edges} | {edge["target"] for edge in edges}
    nodes = [page_by_id[node_id] for node_id in sorted(connected) if node_id in page_by_id and include_in_graph(page_by_id[node_id])]
    existing = {str(node["id"]) for node in nodes}
    for source in source_summaries[:40]:
        if source["id"] in existing:
            continue
        nodes.append(
            {
                "id": source["id"],
                "title": source["title"],
                "url": source["url"],
                "section": "sources",
                "type": "converted-source",
                "snippet": source.get("snippet", ""),
            }
        )
        existing.add(str(source["id"]))
    for label in FOCUS_TERMS:
        node_id = f"focus:{slugify(label)}"
        if node_id in connected:
            nodes.append(
                {
                    "id": node_id,
                    "title": label,
                    "url": "",
                    "section": "focus",
                    "type": "focus-term",
                    "snippet": "Family/source focus term",
                }
            )
    return nodes


def include_in_graph(page_item: dict[str, object]) -> bool:
    section = str(page_item.get("section") or "")
    if section in {"overview", "home"}:
        return False
    return section in TIMELINE_SECTIONS or str(page_item.get("sourceRoot")) == "converted"


def include_in_timeline(page: SitePage) -> bool:
    if page.source_root == "research" and page.section in {"overview", "home"}:
        return False
    if page.section not in TIMELINE_SECTIONS:
        return False
    lower_title = page.title.lower()
    if any(term in lower_title for term in ("dashboard", "index", "log", "research plan", "source usability")):
        return False
    return bool(page.dates)


def build_dashboard(
    root: Path,
    pages: list[SitePage],
    source_summaries: list[dict[str, object]],
    chunk_stats: dict[str, object],
    queue_summaries: list[dict[str, object]],
    timeline_items: list[dict[str, object]],
) -> dict[str, object]:
    usability = load_json(root / "research" / "_indexes" / "source-usability.json")
    usability_summary = usability.get("summary", {}) if isinstance(usability, dict) and isinstance(usability.get("summary"), dict) else {}
    usability_status = usability_summary.get("status_counts", {}) if isinstance(usability_summary.get("status_counts"), dict) else {}
    converted_count = len(source_summaries)
    wiki_pages = len([page for page in pages if page.source_root == "wiki"])
    evidence_queue = next((queue for queue in queue_summaries if queue["id"] == "evidence-extraction"), {})
    qa_queue = next((queue for queue in queue_summaries if queue["id"] == "conversion-qa"), {})
    blocked_evidence = int((evidence_queue.get("statusCounts") or {}).get("blocked_needs_reread", 0)) if isinstance(evidence_queue.get("statusCounts"), dict) else 0
    usable_groups = sum(int(count) for status, count in usability_status.items() if "usable" in str(status) or "partial" in str(status))
    alerts = []
    if blocked_evidence:
        alerts.append(f"{blocked_evidence} evidence tasks are waiting on reread before extraction.")
    needs_chunking = int(usability_status.get("needs_chunking", 0) or 0)
    if needs_chunking:
        alerts.append(f"{needs_chunking} source groups still need chunking before extraction.")
    if converted_count and not usable_groups:
        alerts.append("Converted source files exist, but usability scoring has not caught up yet.")
    stats = [
        {"label": "Converted sources", "value": converted_count, "detail": f"{len(source_summaries[:12])} surfaced below"},
        {"label": "Chunk manifests", "value": int(chunk_stats.get("manifest_count", 0)), "detail": f"{int(chunk_stats.get('chunk_count', 0))} chunks"},
        {"label": "QA queue", "value": int(qa_queue.get("total", 0) or 0), "detail": status_summary(qa_queue.get("statusCounts", {}))},
        {"label": "Evidence queue", "value": int(evidence_queue.get("total", 0) or 0), "detail": status_summary(evidence_queue.get("statusCounts", {}))},
        {"label": "Usable groups", "value": usable_groups, "detail": f"{int(usability_summary.get('total_sources', 0) or 0)} source groups scored"},
        {"label": "Wiki pages", "value": wiki_pages, "detail": "canonical layer"},
    ]
    return {
        "stats": stats,
        "sources": source_summaries,
        "queues": queue_summaries,
        "usabilityStatus": dict(usability_status),
        "alerts": alerts,
        "timelinePreview": timeline_items[:10],
    }


def status_summary(status_counts: object) -> str:
    if not isinstance(status_counts, dict) or not status_counts:
        return "not generated"
    parts = [f"{count} {prettify_stem(str(status))}" for status, count in sorted(status_counts.items())]
    return ", ".join(parts[:2])


def relationship_edges_from_index(root: Path, page_by_url: dict[str, SitePage], link_map: dict[str, SitePage]) -> list[dict[str, str]]:
    graph_path = root / "research" / "_indexes" / "relationship-graph.json"
    if not graph_path.exists():
        return []
    try:
        payload = json.loads(graph_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
    edges = []
    for edge in payload.get("edges", []):
        source = resolve_graph_endpoint(edge.get("source") or edge.get("person_a") or edge.get("from"), link_map)
        target = resolve_graph_endpoint(edge.get("target") or edge.get("person_b") or edge.get("to"), link_map)
        if source and target and source.site_rel in page_by_url and target.site_rel in page_by_url:
            edges.append(
                {
                    "source": source.site_rel,
                    "target": target.site_rel,
                    "type": str(edge.get("type") or edge.get("relationship_type") or "relationship"),
                }
            )
    return edges


def resolve_graph_endpoint(value: object, link_map: dict[str, SitePage]) -> SitePage | None:
    if not isinstance(value, str):
        return None
    value = value.strip()
    if value.startswith("[[") and value.endswith("]]"):
        value = value[2:-2]
    return link_map.get(normalize_link_key(value))


def dedupe_edges(edges: list[dict[str, str]]) -> list[dict[str, str]]:
    seen = set()
    output = []
    for edge in edges:
        key = (edge["source"], edge["target"], edge.get("type", ""))
        if key in seen or edge["source"] == edge["target"]:
            continue
        seen.add(key)
        output.append(edge)
    return output


def section_label(section: str) -> str:
    return SECTION_LABELS.get(section, prettify_stem(section))


def render_home_page(pages: list[SitePage], data: dict[str, object]) -> str:
    dashboard = data.get("dashboard", {}) if isinstance(data.get("dashboard"), dict) else {}
    stats = render_dashboard_stats(dashboard.get("stats", []))
    alerts = render_alerts(dashboard.get("alerts", []))
    sources = render_source_cards(dashboard.get("sources", [])[:12])
    queues = render_queue_table(dashboard.get("queues", []))
    usability = render_status_bars(dashboard.get("usabilityStatus", {}))
    timeline = render_timeline_preview(dashboard.get("timelinePreview", []))
    body = f"""
    <section class="dashboard-head">
      <div>
        <p class="eyebrow">Research Dashboard</p>
        <h1>Internal Family Research</h1>
      </div>
      <div class="generated-at">Updated {html.escape(str(data.get("generatedAt", "")))}</div>
    </section>
    {alerts}
    <section class="metric-grid">{stats}</section>
    <section class="dashboard-grid">
      <article class="panel panel-wide">
        <div class="panel-head"><h2>Priority Sources</h2><a href="sources.html">All sources</a></div>
        <div class="source-card-grid">{sources}</div>
      </article>
      <article class="panel">
        <div class="panel-head"><h2>Agent Queues</h2></div>
        {queues}
      </article>
      <article class="panel">
        <div class="panel-head"><h2>Source Usability</h2></div>
        {usability}
      </article>
      <article class="panel panel-wide">
        <div class="panel-head"><h2>Chronology Preview</h2><a href="timeline.html">Timeline</a></div>
        {timeline}
      </article>
    </section>
    """
    return render_shell("Genealogy Wiki", body, active="home")


def render_dashboard_stats(stats: object) -> str:
    if not isinstance(stats, list) or not stats:
        return '<div class="metric"><strong>0</strong><span>No dashboard data yet</span></div>'
    return "\n".join(
        f"""
        <div class="metric">
          <strong>{html.escape(str(item.get("value", "")))}</strong>
          <span>{html.escape(str(item.get("label", "")))}</span>
          <small>{html.escape(str(item.get("detail", "")))}</small>
        </div>
        """
        for item in stats
        if isinstance(item, dict)
    )


def render_alerts(alerts: object) -> str:
    if not isinstance(alerts, list) or not alerts:
        return ""
    items = "".join(f"<li>{html.escape(str(alert))}</li>" for alert in alerts)
    return f'<section class="alert-strip"><strong>Needs attention</strong><ul>{items}</ul></section>'


def render_source_cards(sources: object) -> str:
    if not isinstance(sources, list) or not sources:
        return '<div class="empty-state">No converted sources found in this checkout.</div>'
    cards = []
    for source in sources:
        if not isinstance(source, dict):
            continue
        terms = " ".join(f"<span>{html.escape(str(term))}</span>" for term in source.get("terms", []))
        meta = " · ".join(
            part
            for part in [
                str(source.get("documentType") or "").strip(),
                f"pages {source.get('pageRange')}" if source.get("pageRange") else "",
                f"{source.get('chunks')} chunks" if source.get("chunks") else "",
                str(source.get("status") or "").replace("_", " "),
            ]
            if part
        )
        cards.append(
            f"""
            <a class="source-card" href="{escape_attr(str(source.get("url", "#")))}">
              <strong>{html.escape(str(source.get("title", "")))}</strong>
              <small>{html.escape(meta)}</small>
              <p>{html.escape(str(source.get("snippet", "")))}</p>
              <span class="term-list">{terms}</span>
            </a>
            """
        )
    return "\n".join(cards)


def render_queue_table(queues: object) -> str:
    if not isinstance(queues, list):
        return '<div class="empty-state">No queue state found.</div>'
    rows = []
    for queue in queues:
        if not isinstance(queue, dict):
            continue
        rows.append(
            f"""
            <tr>
              <th>{html.escape(str(queue.get("label", "")))}</th>
              <td>{html.escape(str(queue.get("total", 0)))}</td>
              <td>{html.escape(status_summary(queue.get("statusCounts", {})))}</td>
            </tr>
            """
        )
    return f'<table class="compact-table"><tbody>{"".join(rows)}</tbody></table>'


def render_status_bars(status_counts: object) -> str:
    if not isinstance(status_counts, dict) or not status_counts:
        return '<div class="empty-state">No source usability index yet.</div>'
    total = sum(int(value) for value in status_counts.values()) or 1
    rows = []
    for status, count in sorted(status_counts.items(), key=lambda item: (-int(item[1]), str(item[0]))):
        pct = max(2, round((int(count) / total) * 100))
        rows.append(
            f"""
            <div class="status-row">
              <span>{html.escape(prettify_stem(str(status)))}</span>
              <strong>{html.escape(str(count))}</strong>
              <i style="--pct:{pct}%"></i>
            </div>
            """
        )
    return "".join(rows)


def render_timeline_preview(items: object) -> str:
    if not isinstance(items, list) or not items:
        return '<div class="empty-state">No dated source events yet.</div>'
    rows = []
    for item in items[:8]:
        if not isinstance(item, dict):
            continue
        rows.append(
            f"""
            <a class="mini-timeline-item" href="{escape_attr(str(item.get("url", "#")))}">
              <span>{html.escape(str(item.get("date", "")))}</span>
              <strong>{html.escape(str(item.get("title", "")))}</strong>
            </a>
            """
        )
    return "".join(rows)


def render_special_page(title: str, body: str) -> str:
    return render_shell(title, body, active=slugify(title))


def graph_body() -> str:
    return """
    <section class="page-head">
      <p class="eyebrow">Evidence Map</p>
      <h1>Research Graph</h1>
      <p>Converted sources are connected to recurring family names, places, and record groups.</p>
    </section>
    <section class="graph-toolbar">
      <input id="graph-filter" type="search" placeholder="Filter graph nodes">
      <button id="graph-reset" type="button">Reset</button>
    </section>
    <section class="graph-stage">
      <svg id="graph-svg" role="img" aria-label="Interactive genealogy graph"></svg>
    </section>
    """


def timeline_body() -> str:
    return """
    <section class="page-head">
      <p class="eyebrow">Chronology</p>
      <h1>Timeline</h1>
      <p>Dated source groups and canonical family events, excluding operations pages.</p>
    </section>
    <section id="timeline-list" class="timeline-list"></section>
    """


def collections_body() -> str:
    return """
    <section class="page-head">
      <p class="eyebrow">Vault Shelves</p>
      <h1>Collections</h1>
      <p>Every rendered wiki and research page, grouped by shelf.</p>
    </section>
    <section id="collection-list" class="collection-list"></section>
    """


def sources_body() -> str:
    return """
    <section class="page-head">
      <p class="eyebrow">Converted Sources</p>
      <h1>Sources</h1>
    </section>
    <section class="source-browser-controls">
      <input id="source-filter" type="search" placeholder="Filter converted sources">
    </section>
    <section id="source-browser" class="source-browser"></section>
    """


def render_markdown_page(page: SitePage, pages: list[SitePage], link_map: dict[str, SitePage]) -> str:
    source_link = html.escape(page.source_path.as_posix())
    body = f"""
    <article class="wiki-article">
      <header class="page-head">
        <p class="eyebrow">{html.escape(section_label(page.section))}</p>
        <h1>{html.escape(page.title)}</h1>
        <p class="source-path">{source_link}</p>
      </header>
      {frontmatter_table(page.frontmatter)}
      {markdown_to_html(page.body, page, link_map)}
    </article>
    """
    depth = len(Path(page.site_rel).parent.parts)
    active = "wiki-index" if page.source_root == "wiki" and page.vault_rel == "index.md" else page.section
    return render_shell(page.title, body, active=active, depth=depth)


def frontmatter_table(frontmatter: dict[str, str]) -> str:
    visible = {key: value for key, value in frontmatter.items() if value and key not in {"display_name", "title"}}
    if not visible:
        return ""
    rows = "\n".join(
        f"<tr><th>{html.escape(key.replace('_', ' ').title())}</th><td>{html.escape(value)}</td></tr>"
        for key, value in sorted(visible.items())
    )
    return f'<details class="frontmatter"><summary>Page Details</summary><table>{rows}</table></details>'


def markdown_to_html(markdown: str, current: SitePage, link_map: dict[str, SitePage]) -> str:
    lines = markdown.splitlines()
    output: list[str] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        if not line.strip():
            index += 1
            continue
        if line.startswith("```"):
            language = line.strip("`").strip()
            code_lines = []
            index += 1
            while index < len(lines) and not lines[index].startswith("```"):
                code_lines.append(lines[index])
                index += 1
            index += 1
            class_name = "mermaid-code" if language == "mermaid" else ""
            output.append(f'<pre class="{class_name}"><code>{html.escape(chr(10).join(code_lines))}</code></pre>')
            continue
        if line.startswith("#"):
            level = min(len(line) - len(line.lstrip("#")), 4)
            text = line[level:].strip()
            output.append(f"<h{level}>{render_inline(text, current, link_map)}</h{level}>")
            index += 1
            continue
        if is_table_start(lines, index):
            table_lines = []
            while index < len(lines) and lines[index].strip().startswith("|"):
                table_lines.append(lines[index])
                index += 1
            output.append(render_table(table_lines, current, link_map))
            continue
        if re.match(r"^\s*[-*]\s+", line):
            items = []
            while index < len(lines) and re.match(r"^\s*[-*]\s+", lines[index]):
                items.append(re.sub(r"^\s*[-*]\s+", "", lines[index]).strip())
                index += 1
            output.append("<ul>" + "".join(f"<li>{render_inline(item, current, link_map)}</li>" for item in items) + "</ul>")
            continue
        if re.match(r"^\s*\d+\.\s+", line):
            items = []
            while index < len(lines) and re.match(r"^\s*\d+\.\s+", lines[index]):
                items.append(re.sub(r"^\s*\d+\.\s+", "", lines[index]).strip())
                index += 1
            output.append("<ol>" + "".join(f"<li>{render_inline(item, current, link_map)}</li>" for item in items) + "</ol>")
            continue
        if line.startswith(">"):
            quotes = []
            while index < len(lines) and lines[index].startswith(">"):
                quotes.append(lines[index].lstrip("> ").strip())
                index += 1
            output.append("<blockquote>" + markdown_to_html("\n".join(quotes), current, link_map) + "</blockquote>")
            continue
        paragraph = [line.strip()]
        index += 1
        while index < len(lines) and lines[index].strip() and not starts_block(lines[index]):
            paragraph.append(lines[index].strip())
            index += 1
        output.append(f"<p>{render_inline(' '.join(paragraph), current, link_map)}</p>")
    return "\n".join(output)


def starts_block(line: str) -> bool:
    return (
        line.startswith("#")
        or line.startswith("```")
        or line.startswith(">")
        or line.strip().startswith("|")
        or bool(re.match(r"^\s*([-*]|\d+\.)\s+", line))
    )


def is_table_start(lines: list[str], index: int) -> bool:
    return index + 1 < len(lines) and lines[index].strip().startswith("|") and set(lines[index + 1].strip()) <= {"|", "-", ":", " "}


def render_table(lines: list[str], current: SitePage, link_map: dict[str, SitePage]) -> str:
    rows = [[cell.strip() for cell in line.strip().strip("|").split("|")] for line in lines]
    if len(rows) >= 2 and all(re.fullmatch(r":?-{3,}:?", cell or "---") for cell in rows[1]):
        header = rows[0]
        body_rows = rows[2:]
    else:
        header = []
        body_rows = rows
    head = ""
    if header:
        head = "<thead><tr>" + "".join(f"<th>{render_inline(cell, current, link_map)}</th>" for cell in header) + "</tr></thead>"
    body = "<tbody>" + "".join(
        "<tr>" + "".join(f"<td>{render_inline(cell, current, link_map)}</td>" for cell in row) + "</tr>"
        for row in body_rows
    ) + "</tbody>"
    return f"<table>{head}{body}</table>"


def render_inline(text: str, current: SitePage, link_map: dict[str, SitePage]) -> str:
    tokens: list[str] = []

    def wikilink_token(match: re.Match[str]) -> str:
        raw = match.group(1)
        target, label = split_wikilink(raw)
        resolved = link_map.get(normalize_link_key(target))
        if resolved:
            href = relative_href(current.site_rel, resolved.site_rel)
            token = f'<a class="wiki-link" href="{escape_attr(href)}">{html.escape(label)}</a>'
        else:
            token = f'<span class="missing-link">{html.escape(label)}</span>'
        tokens.append(token)
        return f"\u0000{len(tokens) - 1}\u0000"

    text = WIKILINK_RE.sub(wikilink_token, text)
    escaped = html.escape(text)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", escaped)
    escaped = INLINE_LINK_RE.sub(lambda m: f'<a href="{escape_attr(m.group(2))}">{m.group(1)}</a>', escaped)
    for idx, token in enumerate(tokens):
        escaped = escaped.replace(f"\u0000{idx}\u0000", token)
    return escaped


def split_wikilink(raw: str) -> tuple[str, str]:
    if "|" in raw:
        target, label = raw.split("|", 1)
    else:
        target = raw
        label = raw.split("/")[-1]
    label = label.split("#", 1)[0].strip()
    return target.strip(), label or target.strip()


def relative_href(from_rel: str, to_rel: str) -> str:
    from_dir = Path(from_rel).parent
    value = Path(*([".."] * len(from_dir.parts))) / to_rel if str(from_dir) != "." else Path(to_rel)
    return quote(value.as_posix(), safe="/#?=&%.-_")


def escape_attr(value: str) -> str:
    return html.escape(value, quote=True)


def render_shell(title: str, body: str, active: str = "", depth: int = 0) -> str:
    prefix = "../" * depth
    nav = [
        ("index.html", "Dashboard", "home"),
        ("sources.html", "Sources", "sources"),
        ("graph.html", "Graph", "research-graph"),
        ("timeline.html", "Timeline", "timeline"),
        ("collections.html", "Collections", "collections"),
        ("wiki/index.html", "Wiki Index", "wiki-index"),
    ]
    nav_html = "\n".join(
        f'<a href="{prefix}{href}" class="{"active" if key == active else ""}">{label}</a>' for href, label, key in nav
    )
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)} | Genealogy Wiki</title>
  <link rel="stylesheet" href="{prefix}assets/styles.css">
</head>
<body data-active="{html.escape(active)}">
  <header class="topbar">
    <a class="brand" href="{prefix}index.html">Genealogy Wiki</a>
    <input id="site-search" type="search" placeholder="Search people, sources, claims">
    <nav>{nav_html}</nav>
  </header>
  <div id="search-results" class="search-results" hidden></div>
  <main>{body}</main>
  <script src="{prefix}assets/site-data.js"></script>
  <script src="{prefix}assets/app.js"></script>
</body>
</html>
"""


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


SITE_CSS = r"""
:root {
  color-scheme: light;
  --ink: #151a23;
  --muted: #607083;
  --paper: #f5f7fb;
  --panel: #ffffff;
  --line: #d9e0ea;
  --teal: #0f766e;
  --blue: #2563eb;
  --moss: #58743d;
  --clay: #a34d37;
  --gold: #b7791f;
  --rose: #be185d;
  --shadow: 0 12px 30px rgba(21, 26, 35, 0.08);
}
* { box-sizing: border-box; }
body {
  margin: 0;
  color: var(--ink);
  background: var(--paper);
  font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  line-height: 1.55;
}
a { color: var(--teal); text-decoration: none; }
a:hover { text-decoration: underline; }
.topbar {
  position: sticky;
  top: 0;
  z-index: 10;
  display: grid;
  grid-template-columns: minmax(150px, 220px) minmax(220px, 1fr) auto;
  gap: 16px;
  align-items: center;
  padding: 12px clamp(18px, 3vw, 42px);
  border-bottom: 1px solid var(--line);
  background: rgba(255, 255, 255, 0.94);
  backdrop-filter: blur(12px);
}
.brand { color: var(--ink); font-weight: 800; letter-spacing: 0; }
nav { display: flex; gap: 6px; flex-wrap: wrap; justify-content: flex-end; }
nav a {
  padding: 7px 10px;
  color: var(--muted);
  border-radius: 6px;
}
nav a.active, nav a:hover { color: var(--ink); background: #eef4ff; text-decoration: none; }
input[type="search"] {
  width: 100%;
  min-height: 38px;
  border: 1px solid var(--line);
  border-radius: 6px;
  padding: 8px 12px;
  color: var(--ink);
  background: #fff;
}
main {
  width: min(1320px, calc(100vw - 32px));
  margin: 0 auto;
  padding: 24px 0 70px;
}
.dashboard-head {
  display: flex;
  justify-content: space-between;
  gap: 24px;
  align-items: end;
  margin: 18px 0 18px;
}
.dashboard-head h1 {
  margin: 0;
  font-size: clamp(2rem, 4vw, 3.4rem);
  line-height: 1.05;
  letter-spacing: 0;
}
.generated-at { color: var(--muted); font-size: .9rem; }
.alert-strip {
  display: grid;
  grid-template-columns: 160px 1fr;
  gap: 16px;
  align-items: start;
  margin: 0 0 16px;
  padding: 14px 16px;
  border: 1px solid #f0c9aa;
  border-left: 4px solid var(--gold);
  border-radius: 8px;
  background: #fff8ed;
}
.alert-strip strong { color: #7a3d12; }
.alert-strip ul { margin: 0; padding-left: 18px; color: #6d4b2a; }
.metric-grid {
  display: grid;
  grid-template-columns: repeat(6, minmax(0, 1fr));
  gap: 12px;
  margin: 0 0 18px;
}
.metric {
  min-height: 112px;
  padding: 16px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--panel);
  box-shadow: var(--shadow);
}
.metric strong { display: block; font-size: 2.15rem; line-height: 1; color: var(--blue); }
.metric span { display: block; margin-top: 8px; color: var(--ink); font-weight: 750; }
.metric small { display: block; margin-top: 4px; color: var(--muted); }
.dashboard-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.5fr) minmax(320px, .75fr);
  gap: 16px;
}
.panel {
  min-width: 0;
  padding: 18px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--panel);
  box-shadow: var(--shadow);
}
.panel-wide { grid-column: span 1; }
.panel-head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 12px;
}
.panel-head h2 { margin: 0; font-size: 1.08rem; letter-spacing: 0; }
.source-card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 12px;
}
.source-card, .source-row {
  display: flex;
  flex-direction: column;
  gap: 7px;
  min-width: 0;
  padding: 14px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #fff;
  color: var(--ink);
}
.source-card:hover, .source-row:hover { border-color: #a8b8cc; text-decoration: none; }
.source-card strong, .source-row strong {
  color: var(--ink);
  line-height: 1.25;
  overflow-wrap: anywhere;
}
.source-card small, .source-row small { color: var(--muted); }
.source-card p, .source-row p {
  margin: 0;
  color: #405064;
  font-size: .92rem;
}
.term-list {
  display: flex;
  flex-wrap: wrap;
  gap: 5px;
  min-height: 22px;
}
.term-list span {
  padding: 2px 7px;
  border-radius: 999px;
  background: #eef4ff;
  color: #1d4ed8;
  font-size: .72rem;
  font-weight: 750;
}
.compact-table { margin: 0; font-size: .92rem; }
.compact-table th { width: 38%; }
.status-row {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 8px;
  align-items: center;
  margin: 10px 0;
}
.status-row span { color: var(--ink); font-weight: 700; }
.status-row strong { color: var(--muted); }
.status-row i {
  grid-column: 1 / -1;
  height: 8px;
  border-radius: 999px;
  background: linear-gradient(90deg, var(--teal) var(--pct), #e7edf5 var(--pct));
}
.mini-timeline-item {
  display: grid;
  grid-template-columns: 96px 1fr;
  gap: 12px;
  padding: 9px 0;
  border-top: 1px solid var(--line);
  color: var(--ink);
}
.mini-timeline-item span { color: var(--clay); font-weight: 800; }
.source-browser-controls { margin: 12px 0 16px; }
.source-browser {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 12px;
}
.hero {
  min-height: 360px;
  display: grid;
  grid-template-columns: minmax(0, 1.25fr) minmax(280px, 0.75fr);
  gap: clamp(22px, 5vw, 64px);
  align-items: center;
  padding: clamp(28px, 6vw, 74px) 0 32px;
}
.hero h1, .page-head h1 {
  margin: 0;
  max-width: 900px;
  font-size: clamp(2rem, 5vw, 4.8rem);
  line-height: 1.02;
  letter-spacing: 0;
}
.hero p, .page-head p { max-width: 760px; color: var(--muted); font-size: 1.05rem; }
.eyebrow {
  margin: 0 0 10px;
  color: var(--clay);
  font-weight: 800;
  text-transform: uppercase;
  font-size: .78rem;
}
.hero-panel {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 10px;
}
.stat, .tool-link, .feature-card {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 8px;
  box-shadow: var(--shadow);
}
.stat { min-height: 96px; padding: 18px; }
.stat strong { display: block; color: var(--teal); font-size: 2rem; line-height: 1; }
.stat span { color: var(--muted); font-size: .9rem; }
.tool-grid, .feature-grid, .collection-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
  gap: 14px;
}
.tool-link, .feature-card {
  display: flex;
  min-height: 138px;
  flex-direction: column;
  gap: 8px;
  padding: 18px;
  color: var(--ink);
}
.tool-link strong, .feature-card strong { font-size: 1.05rem; }
.tool-link span, .feature-card small { color: var(--muted); }
.feature-card span { color: var(--gold); font-size: .78rem; font-weight: 800; text-transform: uppercase; }
.section-heading {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 16px;
  margin: 36px 0 14px;
}
.section-heading h2 { margin: 0; font-size: 1.35rem; }
.section-heading span, .source-path { color: var(--muted); font-size: .88rem; }
.wiki-article {
  display: block;
  max-width: 920px;
  margin: 0 auto;
}
.wiki-article h1, .wiki-article h2, .wiki-article h3 { line-height: 1.18; letter-spacing: 0; }
.wiki-article h2 { margin-top: 34px; border-bottom: 1px solid var(--line); padding-bottom: 6px; }
.wiki-article p, .wiki-article li { font-size: 1rem; }
.frontmatter {
  margin: 18px 0 24px;
  padding: 12px 14px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #fff;
}
.frontmatter summary { cursor: pointer; font-weight: 700; }
table {
  width: 100%;
  margin: 16px 0;
  border-collapse: collapse;
  background: #fff;
  border: 1px solid var(--line);
}
th, td { padding: 9px 11px; border: 1px solid var(--line); vertical-align: top; text-align: left; }
th { background: #f0f4ef; }
pre {
  overflow: auto;
  padding: 14px;
  background: #17201d;
  color: #f7f4ee;
  border-radius: 8px;
}
code { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; }
.wiki-link { font-weight: 700; }
.missing-link {
  color: var(--clay);
  border-bottom: 1px dashed var(--clay);
}
.search-results {
  position: fixed;
  top: 62px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 20;
  width: min(760px, calc(100vw - 32px));
  max-height: min(620px, calc(100vh - 90px));
  overflow: auto;
  background: #fff;
  border: 1px solid var(--line);
  border-radius: 8px;
  box-shadow: var(--shadow);
  padding: 8px;
}
.search-results a { display: block; padding: 10px 12px; border-radius: 6px; color: var(--ink); }
.search-results a:hover { background: #edf4ef; text-decoration: none; }
.graph-toolbar { display: flex; gap: 10px; margin: 18px 0; }
.graph-toolbar button {
  min-width: 84px;
  border: 1px solid var(--line);
  border-radius: 6px;
  background: #fff;
  color: var(--ink);
}
.graph-stage {
  height: min(720px, calc(100vh - 220px));
  min-height: 420px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #fff;
  overflow: hidden;
}
#graph-svg { width: 100%; height: 100%; display: block; }
.clickable-node { cursor: pointer; }
.timeline-list { max-width: 920px; }
.timeline-item {
  display: grid;
  grid-template-columns: 120px 1fr;
  gap: 18px;
  padding: 14px 0;
  border-bottom: 1px solid var(--line);
}
.timeline-date { color: var(--clay); font-weight: 800; }
.empty-state {
  padding: 28px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #fff;
  color: var(--muted);
}
@media (max-width: 760px) {
  .topbar { grid-template-columns: 1fr; }
  nav { justify-content: flex-start; }
  .dashboard-head { display: block; }
  .alert-strip { grid-template-columns: 1fr; }
  .metric-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .dashboard-grid { grid-template-columns: 1fr; }
  .hero { grid-template-columns: 1fr; min-height: auto; }
  .hero-panel { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .timeline-item { grid-template-columns: 1fr; gap: 4px; }
}
@media (min-width: 761px) and (max-width: 1120px) {
  .metric-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .dashboard-grid { grid-template-columns: 1fr; }
}
"""


SITE_JS = r"""
(function () {
  const data = window.GENEALOGY_SITE_DATA || { pages: [], links: [], timeline: [], sections: [] };
  const graphNodes = data.graphNodes || data.pages || [];
  const byId = new Map(graphNodes.map((page) => [page.id, page]));

  function rootPrefix() {
    const path = window.location.pathname.replace(/\\/g, "/");
    const segments = path.split("/").filter(Boolean);
    const marker = segments.findIndex((segment) => segment === "wiki" || segment === "research" || segment === "sources");
    if (marker >= 0) return "../".repeat(Math.max(0, segments.length - marker - 1));
    return "";
  }

  function wireSearch() {
    const input = document.getElementById("site-search");
    const results = document.getElementById("search-results");
    if (!input || !results) return;
    input.addEventListener("input", () => {
      const query = input.value.trim().toLowerCase();
      if (!query) {
        results.hidden = true;
        results.innerHTML = "";
        return;
      }
      const matches = data.pages
        .filter((page) => `${page.title} ${page.section} ${page.snippet}`.toLowerCase().includes(query))
        .slice(0, 12);
      results.innerHTML = matches.length
        ? matches.map((page) => `<a href="${rootPrefix()}${page.url}"><strong>${escapeHtml(page.title)}</strong><br><small>${escapeHtml(page.section)} &middot; ${escapeHtml(page.snippet || "")}</small></a>`).join("")
        : '<div class="empty-state">No matches yet.</div>';
      results.hidden = false;
    });
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape") {
        results.hidden = true;
        input.blur();
      }
      if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === "k") {
        event.preventDefault();
        input.focus();
      }
    });
  }

  function renderCollections() {
    const target = document.getElementById("collection-list");
    if (!target) return;
    const grouped = new Map();
    data.pages.forEach((page) => {
      if (!grouped.has(page.section)) grouped.set(page.section, []);
      grouped.get(page.section).push(page);
    });
    target.innerHTML = [...grouped.entries()].sort().map(([section, pages]) => {
      const links = pages
        .sort((a, b) => a.title.localeCompare(b.title))
        .map((page) => `<li><a href="${page.url}">${escapeHtml(page.title)}</a></li>`)
        .join("");
      return `<article class="feature-card"><span>${escapeHtml(section)}</span><strong>${pages.length} pages</strong><ul>${links}</ul></article>`;
    }).join("") || '<div class="empty-state">No collections yet.</div>';
  }

  function renderTimeline() {
    const target = document.getElementById("timeline-list");
    if (!target) return;
    target.innerHTML = data.timeline.length
      ? data.timeline.map((item) => `<a class="timeline-item" href="${item.url}"><span class="timeline-date">${escapeHtml(item.date)}</span><span><strong>${escapeHtml(item.title)}</strong><br><small>${escapeHtml(item.section)} &middot; ${escapeHtml(item.type)}</small></span></a>`).join("")
      : '<div class="empty-state">No dated wiki pages yet. As agents promote sourced events, this timeline will fill itself in.</div>';
  }

  function renderSources() {
    const target = document.getElementById("source-browser");
    const filter = document.getElementById("source-filter");
    if (!target) return;
    const sources = (data.dashboard && data.dashboard.sources) || [];
    function draw() {
      const query = (filter && filter.value || "").trim().toLowerCase();
      const rows = sources
        .filter((source) => !query || `${source.title} ${source.status} ${source.snippet} ${(source.terms || []).join(" ")}`.toLowerCase().includes(query))
        .slice(0, 120);
      target.innerHTML = rows.length
        ? rows.map((source) => {
          const terms = (source.terms || []).map((term) => `<span>${escapeHtml(term)}</span>`).join("");
          const bits = [source.documentType, source.pageRange ? `pages ${source.pageRange}` : "", source.chunks ? `${source.chunks} chunks` : "", source.status].filter(Boolean).join(" &middot; ");
          return `<a class="source-row" href="${escapeHtml(source.url)}"><strong>${escapeHtml(source.title)}</strong><small>${escapeHtml(bits)}</small><p>${escapeHtml(source.snippet || "")}</p><span class="term-list">${terms}</span></a>`;
        }).join("")
        : '<div class="empty-state">No matching converted sources.</div>';
    }
    if (filter) filter.addEventListener("input", draw);
    draw();
  }

  function renderGraph() {
    const svg = document.getElementById("graph-svg");
    if (!svg) return;
    const filter = document.getElementById("graph-filter");
    const reset = document.getElementById("graph-reset");
    function draw() {
      const query = (filter && filter.value || "").trim().toLowerCase();
      let nodes = graphNodes.map((page) => ({ ...page }));
      let links = data.links.map((link) => ({ ...link }));
      if (query) {
        const keep = new Set(nodes.filter((node) => `${node.title} ${node.section}`.toLowerCase().includes(query)).map((node) => node.id));
        links.forEach((link) => {
          if (keep.has(link.source) || keep.has(link.target)) {
            keep.add(link.source);
            keep.add(link.target);
          }
        });
        nodes = nodes.filter((node) => keep.has(node.id));
        links = links.filter((link) => keep.has(link.source) && keep.has(link.target));
      }
      drawGraph(svg, nodes, links);
    }
    if (filter) filter.addEventListener("input", draw);
    if (reset) reset.addEventListener("click", () => { if (filter) filter.value = ""; draw(); });
    draw();
  }

  function drawGraph(svg, nodes, links) {
    const width = svg.clientWidth || 900;
    const height = svg.clientHeight || 520;
    svg.setAttribute("viewBox", `0 0 ${width} ${height}`);
    svg.innerHTML = "";
    if (!nodes.length) {
      svg.innerHTML = '<text x="24" y="44" fill="#61706b">No graph nodes yet.</text>';
      return;
    }
    const nodeMap = new Map(nodes.map((node, index) => {
      const angle = (Math.PI * 2 * index) / Math.max(nodes.length, 1);
      node.x = width / 2 + Math.cos(angle) * Math.min(width, height) * 0.32;
      node.y = height / 2 + Math.sin(angle) * Math.min(width, height) * 0.32;
      node.vx = 0;
      node.vy = 0;
      return [node.id, node];
    }));
    const activeLinks = links
      .map((link) => ({ ...link, sourceNode: nodeMap.get(link.source), targetNode: nodeMap.get(link.target) }))
      .filter((link) => link.sourceNode && link.targetNode);
    for (let step = 0; step < 260; step += 1) {
      for (let i = 0; i < nodes.length; i += 1) {
        for (let j = i + 1; j < nodes.length; j += 1) {
          const a = nodes[i], b = nodes[j];
          let dx = b.x - a.x, dy = b.y - a.y;
          const dist = Math.max(24, Math.sqrt(dx * dx + dy * dy));
          const force = 1300 / (dist * dist);
          dx /= dist; dy /= dist;
          a.vx -= dx * force; a.vy -= dy * force;
          b.vx += dx * force; b.vy += dy * force;
        }
      }
      activeLinks.forEach((link) => {
        const a = link.sourceNode, b = link.targetNode;
        const dx = b.x - a.x, dy = b.y - a.y;
        const dist = Math.max(1, Math.sqrt(dx * dx + dy * dy));
        const force = (dist - 145) * 0.012;
        a.vx += (dx / dist) * force; a.vy += (dy / dist) * force;
        b.vx -= (dx / dist) * force; b.vy -= (dy / dist) * force;
      });
      nodes.forEach((node) => {
        node.vx += (width / 2 - node.x) * 0.002;
        node.vy += (height / 2 - node.y) * 0.002;
        node.x = Math.max(24, Math.min(width - 24, node.x + node.vx));
        node.y = Math.max(24, Math.min(height - 24, node.y + node.vy));
        node.vx *= 0.82; node.vy *= 0.82;
      });
    }
    activeLinks.forEach((link) => {
      const line = svgEl("line", { x1: link.sourceNode.x, y1: link.sourceNode.y, x2: link.targetNode.x, y2: link.targetNode.y, stroke: "#c8d2ca", "stroke-width": "1.2" });
      svg.appendChild(line);
    });
    nodes.forEach((node, index) => {
      const group = svgEl("g", { tabindex: "0", role: "link" });
      const color = colorFor(node.section);
      const radius = node.section === "focus" ? 10 : (node.section === "people" ? 9 : 6);
      group.appendChild(svgEl("circle", { cx: node.x, cy: node.y, r: radius, fill: color, stroke: "#fff", "stroke-width": "2" }));
      group.appendChild(svgEl("title", {}, node.title));
      const showLabel = node.section === "focus" || node.type !== "converted-source" || nodes.length <= 38 || index < 18;
      if (showLabel) {
        const label = truncateLabel(node.title, node.section === "focus" ? 24 : 38);
        group.appendChild(svgEl("text", { x: node.x + radius + 5, y: node.y + 4, fill: "#17201d", "font-size": node.section === "focus" ? "13" : "11" }, label));
      }
      if (node.url) {
        group.classList.add("clickable-node");
        group.addEventListener("click", () => { window.location.href = rootPrefix() + node.url; });
        group.addEventListener("keydown", (event) => { if (event.key === "Enter") window.location.href = rootPrefix() + node.url; });
      }
      svg.appendChild(group);
    });
  }

  function colorFor(section) {
    const colors = { people: "#0f766e", families: "#496b3a", claims: "#9a4f2f", relationships: "#b7791f", sources: "#2563eb", focus: "#be185d", "source-packets": "#7c3aed", photos: "#be185d", places: "#0891b2" };
    return colors[section] || "#61706b";
  }

  function truncateLabel(value, max) {
    value = String(value || "");
    return value.length > max ? `${value.slice(0, max - 1)}...` : value;
  }

  function svgEl(name, attrs, text) {
    const element = document.createElementNS("http://www.w3.org/2000/svg", name);
    Object.entries(attrs || {}).forEach(([key, value]) => element.setAttribute(key, value));
    if (text) element.textContent = text;
    return element;
  }

  function escapeHtml(value) {
    return String(value).replace(/[&<>"']/g, (char) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[char]));
  }

  wireSearch();
  renderCollections();
  renderTimeline();
  renderSources();
  renderGraph();
})();
"""
