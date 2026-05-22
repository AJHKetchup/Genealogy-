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

THROUGHLINE_SPECS = [
    {
        "id": "pulgar-arriagada-roots",
        "label": "Family line",
        "title": "Pulgar-Arriagada roots",
        "description": "Civil records, named records, and visual items that anchor the family line in Chile.",
        "primaryTerms": ["Pulgar", "Arriagada", "Birth records"],
        "terms": ["Pulgar", "Arriagada", "Birth records"],
        "keywords": ["registro", "nacimiento", "birth", "portrait"],
    },
    {
        "id": "dario-jose-trail",
        "label": "Person trail",
        "title": "Dario Jose Pulgar-Arriagada",
        "description": "Records that cluster around Dario Jose, including travel, institutional, and international material.",
        "primaryTerms": ["Dario"],
        "terms": ["Dario", "Jose", "Pulgar", "Arriagada", "Passenger"],
        "keywords": ["dario", "arturo", "cv", "passport", "passenger"],
    },
    {
        "id": "chile-places",
        "label": "Place context",
        "title": "Los Angeles and Concepcion",
        "description": "Chilean place records and institutional context connected to the family story.",
        "primaryTerms": ["Los Angeles", "Concepcion"],
        "terms": ["Los Angeles", "Concepcion", "Birth records", "Pulgar"],
        "keywords": ["hospital", "universidad", "chile", "concepcion"],
    },
    {
        "id": "geneva-hague",
        "label": "International thread",
        "title": "Geneva and The Hague",
        "description": "International records that connect family names to conferences, travel, and public-facing archives.",
        "primaryTerms": ["Geneva", "The Hague"],
        "terms": ["Geneva", "The Hague", "Dario", "Jose"],
        "keywords": ["geneva", "ginebra", "hague", "haya", "conference"],
    },
    {
        "id": "travel-movement",
        "label": "Movement",
        "title": "Travel and passenger movement",
        "description": "Passenger, arrival, departure, and identity records that help trace movement across places.",
        "primaryTerms": ["Passenger"],
        "terms": ["Passenger", "Dario", "Jose"],
        "keywords": ["passenger", "arrival", "departure", "ship", "passport"],
    },
    {
        "id": "visual-public-records",
        "label": "Visual record",
        "title": "Portraits, photographs, and public images",
        "description": "Image-bearing records, portraits, and visual source items useful for the family narrative.",
        "primaryTerms": [],
        "terms": ["Pulgar", "Arriagada", "Victor", "Geneva"],
        "keywords": ["photograph", "portrait", "photo", "audiovisual"],
        "requireKeyword": True,
    },
]

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
    write_text(output / "tree.html", render_tree_page(data))
    write_text(output / "people.html", render_people_page(data))
    write_text(output / "research.html", render_research_dashboard_page(pages, data))
    write_text(output / "graph.html", render_special_page("Evidence Map", graph_body()))
    write_text(output / "timeline.html", render_special_page("Family Timeline", timeline_body()))
    write_text(output / "collections.html", render_special_page("Collections", collections_body()))
    write_text(output / "sources.html", render_special_page("Source Library", sources_body()))

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
    markers = ("\u00c3", "\u00c2", "\u00e2")
    if not any(marker in value for marker in markers):
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
    return value.count("\u00c3") + value.count("\u00c2") + value.count("\u00e2")


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
    source_by_url = {str(source.get("id")): source for source in source_summaries}
    for page in pages:
        display_title = page_display_title(page, source_by_url)
        page_items.append(
            {
                "id": page.site_rel,
                "title": display_title,
                "technicalTitle": page.title if display_title != page.title else "",
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
        for date in public_timeline_dates(page)
    ]
    for item in timeline_items:
        page = page_by_url_candidate(pages, str(item["url"]))
        if page:
            item["title"] = page_display_title(page, source_by_url)
    timeline_items.sort(key=lambda item: item["date"])
    deduped_edges = dedupe_edges(graph_edges)
    graph_nodes = build_graph_nodes(page_items, deduped_edges, source_summaries)
    family_wiki = build_family_wiki(root, pages, link_map, timeline_items)
    dashboard = build_dashboard(root, pages, source_summaries, chunk_stats, queue_summaries, timeline_items)
    presentation = build_presentation(pages, source_summaries, timeline_items, family_wiki)

    return {
        "generatedAt": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "pages": page_items,
        "links": deduped_edges,
        "graphNodes": graph_nodes,
        "counts": dict(sorted(counts.items())),
        "timeline": timeline_items[:500],
        "dashboard": dashboard,
        "presentation": presentation,
        "familyWiki": family_wiki,
        "sections": [
            {"id": section, "label": section_label(section), "count": count}
            for section, count in sorted(counts.items())
        ],
    }


def page_by_url_candidate(pages: list[SitePage], url: str) -> SitePage | None:
    for page in pages:
        if page.site_rel == url:
            return page
    return None


def page_display_title(page: SitePage, source_by_url: dict[str, dict[str, object]]) -> str:
    if page.source_root == "converted":
        source = source_by_url.get(page.site_rel)
        if source:
            return str(source.get("displayTitle") or source.get("title") or page.title)
    return page.title


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
            "technicalTitle": page.title,
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
        summary["sourceLabel"] = source_cluster_label(summary)
        summary["displayTitle"] = friendly_source_title(summary)
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


def source_cluster_label(summary: dict[str, object]) -> str:
    title = str(summary.get("title") or "").lower()
    haystack = " ".join(
        str(summary.get(key) or "")
        for key in ("title", "technicalTitle", "displayTitle", "snippet", "path", "source")
    ).lower()
    terms = set(str(term) for term in summary.get("terms", []) if term)
    if any(word in haystack for word in ("photograph", "portrait", "photo", "image-bearing")):
        return "Photographs and portraits"
    if "Birth records" in terms or "nacimiento" in title or "birth" in title:
        return "Birth and civil records"
    if "Passenger" in terms or any(word in haystack for word in ("passenger", "arrival", "departure", "passport")):
        return "Travel and identity records"
    if "Geneva" in terms or "The Hague" in terms or any(word in haystack for word in ("geneva", "hague", "ginebra", "haya")):
        return "International records"
    if "Concepcion" in terms or "Los Angeles" in terms:
        return "Chile place records"
    if "Pulgar" in terms or "Arriagada" in terms:
        return "Family records"
    return str(summary.get("documentType") or "Archival source").strip() or "Archival source"


def friendly_source_title(summary: dict[str, object]) -> str:
    title = repair_mojibake(str(summary.get("title") or "")).strip()
    if not title:
        title = "Archival source"
    page_range = str(summary.get("pageRange") or "").strip()
    terms = set(str(term) for term in summary.get("terms", []) if term)
    lower = title.lower()
    cleaned = clean_source_title(title)

    if "photograph" in lower or "portrait" in lower:
        return cleaned
    if lower.startswith("v-p-hist"):
        return f"Visual archive item {title}"
    special_title = special_presentation_title(cleaned, page_range)
    if special_title:
        return special_title
    if looks_like_archive_batch_title(title):
        label = source_cluster_label(summary)
        if "Dario" in terms and ("Geneva" in terms or "The Hague" in terms):
            label = "Dario Jose international record packet"
        elif "Dario" in terms and "Passenger" in terms:
            label = "Dario Jose travel record packet"
        elif "Pulgar" in terms and "Arriagada" in terms:
            label = "Pulgar-Arriagada record packet"
        code = archive_batch_code(title)
        if code:
            label = f"{label} {code}"
        suffix = f", pages {page_range}" if page_range else ""
        return f"{label}{suffix}"
    return cleaned


def looks_like_archive_batch_title(title: str) -> bool:
    lower = title.lower()
    return bool(
        re.match(r"^[rs]\d", lower)
        or lower.startswith("v-p-hist")
        or lower.startswith("ca")
        or "jacket" in lower
        or re.match(r"^[a-z]-?\d", lower)
    )


def clean_source_title(title: str) -> str:
    value = re.sub(r"\s+", " ", title).strip(" ;")
    value = value.replace("Circunscripcion", "Circunscripcion")
    value = value.replace("Clinico", "Clinico")
    return value


def special_presentation_title(title: str, page_range: str) -> str:
    lower = title.lower()
    suffix = f", pages {page_range}" if page_range else ""
    if "hospital" in lower and "concepci" in lower:
        return f"Hospital Clinico Regional de Concepcion history{suffix}"
    if "pioneers of a century" in lower or "anatomical teaching" in lower:
        return f"Concepcion medical teaching history{suffix}"
    if "anales de la universidad de chile" in lower:
        return f"University of Chile public instruction records{suffix}"
    if "camara de senadores" in lower or "cámara de senadores" in lower:
        year = next(iter(extract_dates(title)), "")
        year_text = f", {year}" if year else ""
        return f"Senate records{year_text}{suffix}"
    if "el aguila" in lower:
        return f"El Aguila article scan{suffix}"
    if "geneva convention" in lower:
        return f"Geneva Convention records{suffix}"
    if "la haye" in lower or "conférence internationale" in lower or "conference internationale" in lower:
        return f"The Hague conference records{suffix}"
    if "guia medica" in lower or "guía médica" in lower:
        return f"National medical guide{suffix}"
    if "cv of dario" in lower:
        return f"Dario Arturo Pulgar CV{suffix}"
    if "passenger and crew lists" in lower:
        return "Passenger and crew list archive record"
    if "arrival-departure record" in lower:
        return "Arrival-departure identity record"
    if "passenger list, pacific" in lower:
        return "Pacific Steam Navigation passenger list"
    return ""


def archive_batch_code(title: str) -> str:
    match = re.match(r"^(.+?)\s+pages\b", title, flags=re.IGNORECASE)
    if not match:
        return ""
    code = match.group(1).strip()
    code = re.sub(r"[-_]?Jacket", " Jacket", code, flags=re.IGNORECASE)
    return code


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
                "title": source.get("displayTitle") or source["title"],
                "technicalTitle": source.get("technicalTitle") or source.get("title", ""),
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
    return bool(public_timeline_dates(page))


def public_timeline_dates(page: SitePage) -> list[str]:
    if page.source_root != "wiki":
        return []
    lower_title = page.title.lower()
    if any(term in lower_title for term in ("dashboard", "index", "log", "research plan", "source usability")):
        return []
    if page.section == "people":
        return timeline_dates_from_fields(page, ["birth", "death", "baptism", "burial"])
    if page.section == "events":
        dates = timeline_dates_from_fields(page, ["date", "year", "event_date", "start_date", "end_date"])
        return dates or page.dates[:1]
    if page.section in {"families", "relationships"}:
        return timeline_dates_from_fields(page, ["marriage", "date", "event_date", "start_date"])
    if page.section in {"photos", "places"}:
        return timeline_dates_from_fields(page, ["date", "year", "event_date"])
    if page.section == "narratives":
        return timeline_dates_from_fields(page, ["event_date", "timeline_date"])
    return []


def timeline_dates_from_fields(page: SitePage, fields: list[str]) -> list[str]:
    dates: list[str] = []
    for field in fields:
        for date in extract_dates(page.frontmatter.get(field, "")):
            if date not in dates:
                dates.append(date)
    return dates


NON_PERSON_PRESENTATION_PREFIXES = (
    "birth registration entry",
    "death registration entry",
    "marriage registration entry",
    "registration entry",
    "record entry",
    "certificate no",
    "certificate number",
    "source packet",
    "passenger list",
    "document page",
    "page ",
)


def include_family_person_page(page: SitePage) -> bool:
    title = str(page.frontmatter.get("display_name") or page.title or "").strip()
    lowered = " ".join(title.lower().split())
    return not any(lowered.startswith(prefix) for prefix in NON_PERSON_PRESENTATION_PREFIXES)


def include_presentation_person_page(page: SitePage, relationship_targets: set[str]) -> bool:
    if not include_family_person_page(page):
        return False
    if frontmatter_bool(page.frontmatter.get("home_person", "")):
        return True
    if str(page.frontmatter.get("relation_to_home") or "").strip():
        return True
    target = normalize_link_key(page.vault_rel)
    if target in relationship_targets:
        return True
    status = str(page.frontmatter.get("status") or "").strip().lower().replace("-", "_")
    tags = str(page.frontmatter.get("tags") or "").strip().lower().replace("-", "_")
    if status == "source_mentioned" or "source_mentioned" in tags:
        return False
    return True


def include_presentation_relationship_card(relationship: dict[str, object]) -> bool:
    status = str(relationship.get("status") or "").strip().lower().replace("-", "_")
    if status in {"", "draft", "hold", "held", "rejected", "do_not_promote", "blocked"}:
        return False
    person_a = relationship.get("personA") if isinstance(relationship.get("personA"), dict) else {}
    person_b = relationship.get("personB") if isinstance(relationship.get("personB"), dict) else {}
    return bool(person_a.get("target") and person_b.get("target"))


def relationship_person_targets(relationships: list[dict[str, object]]) -> set[str]:
    targets: set[str] = set()
    for relationship in relationships:
        person_a = relationship.get("personA") if isinstance(relationship.get("personA"), dict) else {}
        person_b = relationship.get("personB") if isinstance(relationship.get("personB"), dict) else {}
        for person in [person_a, person_b]:
            target = str(person.get("target") or "")
            if target.startswith("people/"):
                targets.add(normalize_link_key(target))
    return targets


def build_family_wiki(
    root: Path,
    pages: list[SitePage],
    link_map: dict[str, SitePage],
    timeline_items: list[dict[str, object]],
) -> dict[str, object]:
    relationship_pages = sorted(
        [
            page
            for page in pages
            if page.section == "relationships" and page.source_root in {"wiki", "research"}
        ],
        key=lambda page: (page.source_root != "wiki", page.title.lower()),
    )
    family_pages = sorted(
        [page for page in pages if page.source_root == "wiki" and page.section in {"branches", "families"}],
        key=lambda page: page.title.lower(),
    )
    narrative_pages = sorted(
        [page for page in pages if page.source_root == "wiki" and page.section == "narratives"],
        key=lambda page: page.title.lower(),
    )
    event_pages = sorted(
        [page for page in pages if page.source_root == "wiki" and page.section == "events"],
        key=lambda page: page.title.lower(),
    )
    photo_pages = sorted(
        [page for page in pages if page.source_root == "wiki" and page.section == "photos"],
        key=lambda page: page.title.lower(),
    )
    source_pages = sorted(
        [page for page in pages if page.source_root == "wiki" and page.section in {"sources", "source-packets"}],
        key=lambda page: page.title.lower(),
    )
    relationships = dedupe_relationship_cards(
        [
            *relationship_cards_from_index(root, link_map),
            *[relationship_card(page, link_map) for page in relationship_pages],
        ]
    )
    relationships = [relationship for relationship in relationships if include_presentation_relationship_card(relationship)]
    relationship_targets = relationship_person_targets(relationships)
    people_pages = sorted(
        [
            page
            for page in pages
            if page.source_root == "wiki"
            and page.section == "people"
            and include_presentation_person_page(page, relationship_targets)
        ],
        key=lambda page: (not frontmatter_bool(page.frontmatter.get("home_person", "")), page.title.lower()),
    )
    people = [family_page_card(page) for page in people_pages]
    families = [family_page_card(page) for page in family_pages]
    narratives = [family_page_card(page) for page in narrative_pages]
    events = [family_page_card(page) for page in event_pages]
    photos = [family_page_card(page) for page in photo_pages]
    sources = [family_page_card(page) for page in source_pages]
    home_person = next((person for person in people if person.get("homePerson")), people[0] if people else None)
    direct_relationships = direct_relationships_for_home(relationships, home_person)
    stats = [
        {"label": "People", "value": len(people), "detail": "canonical family profiles"},
        {"label": "Relationships", "value": len(relationships), "detail": "tree connections"},
        {"label": "Family Lines", "value": len(families), "detail": "branches and families"},
        {"label": "Stories", "value": len(narratives), "detail": "family-history chapters"},
    ]
    return {
        "homePerson": home_person,
        "people": people,
        "relationships": relationships,
        "directRelationships": direct_relationships,
        "families": families,
        "narratives": narratives,
        "events": events,
        "photos": photos,
        "sources": sources,
        "timelinePreview": timeline_items[:10],
        "stats": stats,
    }


def family_page_card(page: SitePage) -> dict[str, object]:
    return {
        "title": page.title,
        "url": page.site_rel,
        "section": page.section,
        "type": page.page_type,
        "status": page.frontmatter.get("status", ""),
        "relationToHome": page.frontmatter.get("relation_to_home", ""),
        "homePerson": frontmatter_bool(page.frontmatter.get("home_person", "")),
        "dates": public_timeline_dates(page)[:3],
        "snippet": page.text[:280],
    }


def relationship_card(page: SitePage, link_map: dict[str, SitePage]) -> dict[str, object]:
    relationship_type = page.frontmatter.get("relationship_type", "relationship")
    person_a = resolve_page_reference(page.frontmatter.get("person_a", ""), link_map)
    person_b = resolve_page_reference(page.frontmatter.get("person_b", ""), link_map)
    return {
        "path": f"{page.source_root}/{page.vault_rel}",
        "title": page.title,
        "url": page.site_rel,
        "type": relationship_type,
        "label": relationship_type_label(relationship_type),
        "status": page.frontmatter.get("status", ""),
        "confidence": page.frontmatter.get("confidence", ""),
        "personA": person_a,
        "personB": person_b,
        "snippet": page.text[:280],
    }


def relationship_cards_from_index(root: Path, link_map: dict[str, SitePage]) -> list[dict[str, object]]:
    payload = load_json(root / "research" / "_indexes" / "relationships.json")
    records = payload.get("relationships", []) if isinstance(payload, dict) else []
    if not isinstance(records, list):
        return []
    cards: list[dict[str, object]] = []
    for record in records:
        if not isinstance(record, dict):
            continue
        relationship_type = str(record.get("relationship_type") or "relationship")
        person_a = resolve_page_reference(str(record.get("person_a") or ""), link_map)
        person_b = resolve_page_reference(str(record.get("person_b") or ""), link_map)
        label = relationship_type_label(relationship_type)
        title = " ".join(
            part
            for part in [
                str(person_a.get("label") or "").strip(),
                label,
                str(person_b.get("label") or "").strip(),
            ]
            if part
        )
        cards.append(
            {
                "path": str(record.get("path") or ""),
                "title": title or prettify_stem(Path(str(record.get("path") or "relationship")).stem),
                "url": relationship_url_from_path(str(record.get("path") or ""), link_map),
                "type": relationship_type,
                "label": label,
                "status": str(record.get("status") or ""),
                "confidence": str(record.get("confidence") or ""),
                "personA": person_a,
                "personB": person_b,
                "snippet": str(record.get("evidence_for") or "")[:280],
            }
        )
    return cards


def relationship_url_from_path(path: str, link_map: dict[str, SitePage]) -> str:
    normalized = normalize_link_key(path)
    candidates = [
        normalized,
        normalized.removeprefix("wiki/"),
        normalized.removeprefix("research/"),
    ]
    for candidate in candidates:
        resolved = link_map.get(candidate)
        if resolved:
            return resolved.site_rel
    return ""


def dedupe_relationship_cards(relationships: list[dict[str, object]]) -> list[dict[str, object]]:
    seen: set[str] = set()
    output: list[dict[str, object]] = []
    for relationship in relationships:
        person_a = relationship.get("personA") if isinstance(relationship.get("personA"), dict) else {}
        person_b = relationship.get("personB") if isinstance(relationship.get("personB"), dict) else {}
        key = "|".join(
            [
                str(relationship.get("path") or ""),
                str(relationship.get("type") or ""),
                str(person_a.get("target") or person_a.get("label") or ""),
                str(person_b.get("target") or person_b.get("label") or ""),
            ]
        )
        if key in seen:
            continue
        seen.add(key)
        output.append(relationship)
    return output


def resolve_page_reference(value: str, link_map: dict[str, SitePage]) -> dict[str, str]:
    value = (value or "").strip()
    if value.startswith("[[") and value.endswith("]]"):
        value = value[2:-2]
    target, label = split_wikilink(value)
    resolved = link_map.get(normalize_link_key(target))
    if resolved:
        return {"label": resolved.title, "url": resolved.site_rel, "target": normalize_link_key(target)}
    return {"label": label or target, "url": "", "target": normalize_link_key(target)}


def direct_relationships_for_home(
    relationships: list[dict[str, object]],
    home_person: dict[str, object] | None,
) -> list[dict[str, object]]:
    if not home_person:
        return relationships[:8]
    home_url = str(home_person.get("url") or "")
    direct = []
    for relationship in relationships:
        person_a = relationship.get("personA") if isinstance(relationship.get("personA"), dict) else {}
        person_b = relationship.get("personB") if isinstance(relationship.get("personB"), dict) else {}
        if person_a.get("url") == home_url or person_b.get("url") == home_url:
            direct.append(relationship)
    return direct


def frontmatter_bool(value: str) -> bool:
    return str(value).strip().lower() in {"true", "yes", "1"}


def relationship_type_label(value: str) -> str:
    labels = {
        "parent_child": "parent of",
        "proven_parent": "parent of",
        "probable_parent": "probable parent of",
        "possible_parent": "possible parent of",
        "spouse": "spouse of",
        "child": "child of",
        "sibling": "sibling of",
        "maternal_grandfather": "maternal grandfather of",
        "paternal_grandfather": "paternal grandfather of",
        "maternal_grandmother": "maternal grandmother of",
        "paternal_grandmother": "paternal grandmother of",
        "grandparent": "grandparent of",
        "grandchild": "grandchild of",
        "same_person_candidate": "possible same person as",
        "name_variant": "name variant of",
    }
    return labels.get(value, prettify_stem(value or "connected to").lower())


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


def build_presentation(
    pages: list[SitePage],
    source_summaries: list[dict[str, object]],
    timeline_items: list[dict[str, object]],
    family_wiki: dict[str, object],
) -> dict[str, object]:
    throughlines = build_throughlines(source_summaries)
    canonical_pages = [page for page in pages if page.source_root == "wiki" and page.page_type != "template"]
    return {
        "stats": family_wiki.get("stats", []),
        "homePerson": family_wiki.get("homePerson"),
        "people": family_wiki.get("people", [])[:8],
        "relationships": family_wiki.get("directRelationships", [])[:8],
        "families": family_wiki.get("families", [])[:6],
        "narratives": family_wiki.get("narratives", [])[:6],
        "photos": family_wiki.get("photos", [])[:6],
        "sourceShelfCount": len(family_wiki.get("sources", [])) + len(source_summaries),
        "publicTimelineCount": len(timeline_items),
        "throughlines": throughlines,
        "featuredSources": select_featured_sources(source_summaries)[:4],
        "timelinePreview": timeline_items[:8],
        "canonicalPageCount": len(canonical_pages),
    }


def build_throughlines(source_summaries: list[dict[str, object]]) -> list[dict[str, object]]:
    threads: list[dict[str, object]] = []
    for spec in THROUGHLINE_SPECS:
        matches = matching_sources_for_throughline(source_summaries, spec)
        dates = sorted({date for source in matches for date in source.get("dates", []) if isinstance(date, str)})
        featured = [
            {
                "title": source.get("displayTitle") or source.get("title", ""),
                "url": source.get("url", ""),
                "label": source.get("sourceLabel", ""),
            }
            for source in matches[:3]
        ]
        threads.append(
            {
                "id": spec["id"],
                "label": spec["label"],
                "title": spec["title"],
                "description": spec["description"],
                "sourceCount": len(matches),
                "dateRange": compact_date_range(dates, total=len(matches)),
                "featuredSources": featured,
            }
        )
    threads.sort(key=lambda item: (-int(item.get("sourceCount", 0)), str(item.get("title", ""))))
    return threads


def matching_sources_for_throughline(
    source_summaries: list[dict[str, object]],
    spec: dict[str, object],
) -> list[dict[str, object]]:
    wanted_terms = set(str(term) for term in spec.get("terms", []) if term)
    primary_terms = set(str(term) for term in spec.get("primaryTerms", []) if term)
    keywords = [str(keyword).lower() for keyword in spec.get("keywords", []) if keyword]
    require_keyword = bool(spec.get("requireKeyword"))
    ranked: list[tuple[int, str, dict[str, object]]] = []
    for source in source_summaries:
        source_terms = set(str(term) for term in source.get("terms", []) if term)
        haystack = " ".join(
            str(source.get(key) or "")
            for key in ("title", "technicalTitle", "displayTitle", "snippet", "sourceLabel", "path")
        ).lower()
        term_hits = len(wanted_terms & source_terms)
        primary_hits = len(primary_terms & source_terms)
        keyword_hits = sum(1 for keyword in keywords if keyword in haystack)
        keyword_hit = keyword_hits > 0
        if require_keyword and not keyword_hit:
            continue
        if primary_terms and not primary_hits and not keyword_hit:
            continue
        if term_hits >= 2 or (term_hits and keyword_hit) or keyword_hit:
            rank = primary_hits * 40 + keyword_hits * 24 + term_hits * 8 + min(20, int(source.get("score", 0) or 0))
            ranked.append((rank, str(source.get("displayTitle") or source.get("title") or ""), source))
    ranked.sort(key=lambda item: (-item[0], item[1].lower()))
    return [source for _, _, source in ranked]


def compact_date_range(dates: list[str], total: int = 0) -> str:
    if not dates:
        return "undated records"
    if total and len(dates) < max(2, total // 3):
        return "mostly undated"
    years = sorted({date[:4] for date in dates if len(date) >= 4})
    if not years:
        return "dated records"
    if len(years) == 1:
        return years[0]
    return f"{years[0]}-{years[-1]}"


def select_featured_sources(source_summaries: list[dict[str, object]]) -> list[dict[str, object]]:
    preferred = []
    seen = set()
    for spec in THROUGHLINE_SPECS:
        for source in matching_sources_for_throughline(source_summaries, spec):
            source_id = str(source.get("id"))
            if source_id not in seen:
                preferred.append(source)
                seen.add(source_id)
                break
    if len(preferred) < 8:
        for source in source_summaries:
            source_id = str(source.get("id"))
            if source_id not in seen:
                preferred.append(source)
                seen.add(source_id)
            if len(preferred) >= 8:
                break
    return preferred


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
    presentation = data.get("presentation", {}) if isinstance(data.get("presentation"), dict) else {}
    family_wiki = data.get("familyWiki", {}) if isinstance(data.get("familyWiki"), dict) else {}
    stats = render_dashboard_stats(presentation.get("stats", []))
    home_person = render_home_person_card(presentation.get("homePerson"))
    tree_preview = render_tree_preview(family_wiki)
    relationships = render_relationship_cards(presentation.get("relationships", []))
    people = render_person_cards(presentation.get("people", []))
    families = render_family_cards(presentation.get("families", []))
    narratives = render_narrative_cards(presentation.get("narratives", []))
    timeline = render_timeline_preview(presentation.get("timelinePreview", []), empty="No dated family events yet.")
    canonical_count = int(presentation.get("canonicalPageCount", 0) or 0)
    source_count = int(presentation.get("sourceShelfCount", 0) or 0)
    body = f"""
    <section class="family-hero">
      <div class="story-copy">
        <p class="eyebrow">Family History</p>
        <h1>Alexander John Heinz Family History</h1>
        <p>A person-first family wiki that opens with the tree, then follows people, relationships, LifeStory chapters, facts, places, photos, and the records that support them.</p>
      </div>
      {home_person}
    </section>
    <section class="metric-grid story-metrics">{stats}</section>
    <section class="section-heading">
      <h2>Family Tree</h2>
      <span>Built automatically from reviewed relationship evidence</span>
    </section>
    {tree_preview}
    <section class="section-heading">
      <h2>Explore</h2>
      <span>Family-facing views first, research operations separate</span>
    </section>
    <section class="tool-grid presentation-tools">
      <a class="tool-link" href="tree.html"><span>Tree</span><strong>Family Tree</strong><small>People and relationships around the home person.</small></a>
      <a class="tool-link" href="people.html"><span>Profiles</span><strong>People</strong><small>Individual pages, relationship positions, facts, and stories.</small></a>
      <a class="tool-link" href="timeline.html"><span>Life Events</span><strong>Family Timeline</strong><small>Births, marriages, residences, migrations, deaths, and story events.</small></a>
      <a class="tool-link" href="sources.html"><span>Citations</span><strong>Source Library</strong><small>Records and citations that support the family pages.</small></a>
      <a class="tool-link research-tool" href="research.html"><span>Backroom</span><strong>Research Dashboard</strong><small>QA, staging, proof review, queues, and automation state.</small></a>
    </section>
    <section class="family-grid">
      <article>
        <div class="panel-head"><h2>People</h2><a href="people.html">All people</a></div>
        <div class="person-card-grid">{people}</div>
      </article>
      <article>
        <div class="panel-head"><h2>Direct Relationships</h2><a href="tree.html">Tree</a></div>
        <div class="relationship-list">{relationships}</div>
      </article>
      <article>
        <div class="panel-head"><h2>Family Lines</h2><a href="people.html">People</a></div>
        <div class="person-card-grid">{families}</div>
      </article>
      <article>
        <div class="panel-head"><h2>LifeStory Chapters</h2><a href="wiki/index.html">Wiki index</a></div>
        <div class="story-card-grid">{narratives}</div>
      </article>
      <article>
        <div class="panel-head"><h2>Family Timeline</h2><a href="timeline.html">Timeline</a></div>
        {timeline}
      </article>
      <article class="research-summary">
        <div class="panel-head"><h2>Research Backroom</h2><a href="research.html">Dashboard</a></div>
        <p>{canonical_count} canonical wiki pages are available now. {source_count} supporting record pages are kept as citations and source-library material, not as the narrative itself.</p>
      </article>
    </section>
    """
    return render_shell("Family History Dashboard", body, active="home")


def render_home_person_card(home_person: object) -> str:
    if not isinstance(home_person, dict):
        return """
        <aside class="home-person-card">
          <span>Home Person</span>
          <strong>Not set yet</strong>
          <small>Add a canonical person page with <code>home_person: true</code>.</small>
        </aside>
        """
    relation = str(home_person.get("relationToHome") or "Home person")
    return f"""
    <aside class="home-person-card">
      <span>Home Person</span>
      <strong>{html.escape(str(home_person.get("title", "")))}</strong>
      <small>{html.escape(relation)}</small>
      <a href="{escape_attr(str(home_person.get("url", "#")))}">Open profile</a>
    </aside>
    """


def render_tree_preview(family_wiki: dict[str, object]) -> str:
    home_person = family_wiki.get("homePerson") if isinstance(family_wiki.get("homePerson"), dict) else None
    relationships = family_wiki.get("relationships", [])
    if not home_person or not isinstance(relationships, list) or not relationships:
        return '<section class="tree-board"><div class="empty-state">No family relationships are ready for the presentation tree yet.</div></section>'
    home_url = str(home_person.get("url") or "")
    home_html = render_tree_person(
        {"label": str(home_person.get("title", "")), "url": str(home_person.get("url", ""))},
        {"label": "home person", "status": str(home_person.get("status", "")), "confidence": ""},
        home=True,
    )
    edges = [render_tree_edge(relationship, home_url) for relationship in relationships[:24] if isinstance(relationship, dict)]
    remaining = max(0, len(relationships) - len(edges))
    remaining_html = f'<div class="tree-more">{remaining} more relationship(s) in the evidence list below.</div>' if remaining else ""
    return f"""
    <section class="tree-board tree-network-board">
      <div class="tree-generation home-row">{home_html}</div>
      <div class="tree-network">{"".join(edges)}</div>
      {remaining_html}
    </section>
    """


def render_tree_edge(relationship: dict[str, object], home_url: str) -> str:
    person_a = relationship.get("personA") if isinstance(relationship.get("personA"), dict) else {}
    person_b = relationship.get("personB") if isinstance(relationship.get("personB"), dict) else {}
    label = str(relationship.get("label") or "connected to")
    status = str(relationship.get("status") or "").replace("_", " ")
    confidence = str(relationship.get("confidence") or "")
    meta = " / ".join(part for part in [status, f"confidence {confidence}" if confidence else ""] if part)
    home_related = person_a.get("url") == home_url or person_b.get("url") == home_url
    class_name = "tree-edge home-related-edge" if home_related else "tree-edge"
    href = str(relationship.get("url") or "#")
    return f"""
    <a class="{class_name}" href="{escape_attr(href)}">
      <span>{html.escape(str(person_a.get("label") or "Unknown person"))}</span>
      <strong>{html.escape(label)}</strong>
      <span>{html.escape(str(person_b.get("label") or "Unknown person"))}</span>
      <small>{html.escape(meta)}</small>
    </a>
    """


def render_tree_person(person: object, relationship: object, home: bool = False) -> str:
    person = person if isinstance(person, dict) else {}
    relationship = relationship if isinstance(relationship, dict) else {}
    title = str(person.get("label") or "Unknown person")
    href = str(person.get("url") or "#")
    label = str(relationship.get("label") or "")
    status = str(relationship.get("status") or "").replace("_", " ")
    confidence = str(relationship.get("confidence") or "")
    meta = " / ".join(part for part in [label, status, f"confidence {confidence}" if confidence else ""] if part)
    class_name = "tree-person home-person" if home else "tree-person"
    return f"""
    <a class="{class_name}" href="{escape_attr(href)}">
      <strong>{html.escape(title)}</strong>
      <small>{html.escape(meta)}</small>
    </a>
    """


def render_person_cards(people: object) -> str:
    if not isinstance(people, list) or not people:
        return '<div class="empty-state">No canonical people are ready yet.</div>'
    return "\n".join(render_family_card(person, class_name="person-card") for person in people if isinstance(person, dict))


def render_family_cards(families: object) -> str:
    if not isinstance(families, list) or not families:
        return '<div class="empty-state">No family branches have been added yet.</div>'
    return "\n".join(render_family_card(family, class_name="person-card family-card") for family in families if isinstance(family, dict))


def render_narrative_cards(narratives: object) -> str:
    if not isinstance(narratives, list) or not narratives:
        return '<div class="empty-state">No LifeStory chapters have been compiled yet.</div>'
    return "\n".join(render_family_card(narrative, class_name="story-card") for narrative in narratives if isinstance(narrative, dict))


def render_family_card(item: dict[str, object], class_name: str) -> str:
    meta_parts = [
        str(item.get("relationToHome") or "").strip(),
        str(item.get("status") or "").replace("_", " ").strip(),
        ", ".join(str(date) for date in item.get("dates", [])[:2]) if isinstance(item.get("dates"), list) else "",
    ]
    meta = " | ".join(part for part in meta_parts if part)
    return f"""
    <a class="{class_name}" href="{escape_attr(str(item.get("url", "#")))}">
      <strong>{html.escape(str(item.get("title", "")))}</strong>
      <small>{html.escape(meta)}</small>
      <p>{html.escape(str(item.get("snippet", "")))}</p>
    </a>
    """


def render_relationship_cards(relationships: object) -> str:
    if not isinstance(relationships, list) or not relationships:
        return '<div class="empty-state">No relationship pages are ready yet.</div>'
    cards = []
    for relationship in relationships:
        if not isinstance(relationship, dict):
            continue
        person_a = relationship.get("personA") if isinstance(relationship.get("personA"), dict) else {}
        person_b = relationship.get("personB") if isinstance(relationship.get("personB"), dict) else {}
        meta_parts = [
            str(relationship.get("status") or "").replace("_", " "),
            f"confidence {relationship.get('confidence')}" if relationship.get("confidence") else "",
        ]
        meta = " | ".join(part for part in meta_parts if part)
        href = str(relationship.get("url") or "#")
        cards.append(
            f"""
            <a class="relationship-card" href="{escape_attr(href)}">
              <span>{html.escape(str(person_a.get("label") or "Unknown person"))}</span>
              <strong>{html.escape(str(relationship.get("label") or "connected to"))}</strong>
              <span>{html.escape(str(person_b.get("label") or "Unknown person"))}</span>
              <small>{html.escape(meta)}</small>
            </a>
            """
        )
    return "\n".join(cards)


def render_tree_page(data: dict[str, object]) -> str:
    family_wiki = data.get("familyWiki", {}) if isinstance(data.get("familyWiki"), dict) else {}
    tree_preview = render_tree_preview(family_wiki)
    relationships = render_relationship_cards(family_wiki.get("relationships", []))
    body = f"""
    <section class="page-head">
      <p class="eyebrow">Family Tree</p>
      <h1>Tree View</h1>
      <p>A presentation tree generated from canonical people and reviewed relationship evidence. Research candidates stay out of this view until reviewed and promoted.</p>
    </section>
    {tree_preview}
    <section class="section-heading">
      <h2>Relationship Evidence</h2>
      <span>Canonical relationship pages feeding the tree</span>
    </section>
    <section class="relationship-list tree-relationship-list">{relationships}</section>
    """
    return render_shell("Family Tree", body, active="tree")


def render_people_page(data: dict[str, object]) -> str:
    family_wiki = data.get("familyWiki", {}) if isinstance(data.get("familyWiki"), dict) else {}
    stats = render_dashboard_stats(family_wiki.get("stats", []))
    people = render_person_cards(family_wiki.get("people", []))
    families = render_family_cards(family_wiki.get("families", []))
    narratives = render_narrative_cards(family_wiki.get("narratives", []))
    body = f"""
    <section class="page-head">
      <p class="eyebrow">People</p>
      <h1>Family Profiles</h1>
      <p>Profiles are the center of the public wiki. Sources, chunks, and research queues support these pages rather than replacing them.</p>
    </section>
    <section class="metric-grid story-metrics">{stats}</section>
    <section class="section-heading"><h2>People</h2><span>Canonical person pages</span></section>
    <section class="person-card-grid">{people}</section>
    <section class="section-heading"><h2>Family Lines</h2><span>Branches and families</span></section>
    <section class="person-card-grid">{families}</section>
    <section class="section-heading"><h2>LifeStory Chapters</h2><span>Narratives built from the proof layer</span></section>
    <section class="story-card-grid">{narratives}</section>
    """
    return render_shell("People", body, active="people")


def render_research_dashboard_page(pages: list[SitePage], data: dict[str, object]) -> str:
    dashboard = data.get("dashboard", {}) if isinstance(data.get("dashboard"), dict) else {}
    stats = render_dashboard_stats(dashboard.get("stats", []))
    alerts = render_alerts(dashboard.get("alerts", []))
    sources = render_source_cards(dashboard.get("sources", [])[:12], mode="research")
    queues = render_queue_table(dashboard.get("queues", []))
    usability = render_status_bars(dashboard.get("usabilityStatus", {}))
    timeline = render_timeline_preview(dashboard.get("timelinePreview", []))
    body = f"""
    <section class="dashboard-head">
      <div>
        <p class="eyebrow">Research Backroom</p>
        <h1>Internal Research Operations</h1>
        <p>Source QA, agent queues, source usability, and pipeline status stay here so the family-history dashboard can stay narrative-first.</p>
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
      <article class="panel">
        <div class="panel-head"><h2>Rendered Shelves</h2></div>
        <div class="ops-link-list">
          <a href="collections.html">All rendered wiki and research shelves</a>
          <a href="wiki/index.html">Canonical wiki shelf</a>
          <a href="graph.html">Evidence map</a>
        </div>
      </article>
    </section>
    """
    return render_shell("Research Backroom", body, active="research")


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


def render_throughline_cards(throughlines: object) -> str:
    if not isinstance(throughlines, list) or not throughlines:
        return '<div class="empty-state">No family-history throughlines have been assembled yet.</div>'
    cards = []
    for thread in throughlines:
        if not isinstance(thread, dict):
            continue
        links = "".join(
            f'<a href="{escape_attr(str(source.get("url", "#")))}">{html.escape(str(source.get("title", "")))}</a>'
            for source in thread.get("featuredSources", [])
            if isinstance(source, dict)
        )
        count = int(thread.get("sourceCount", 0) or 0)
        cards.append(
            f"""
            <article class="throughline-card">
              <span>{html.escape(str(thread.get("label", "")))}</span>
              <h3>{html.escape(str(thread.get("title", "")))}</h3>
              <p>{html.escape(str(thread.get("description", "")))}</p>
              <div class="thread-meta"><strong>{count}</strong> records <i>{html.escape(str(thread.get("dateRange", "")))}</i></div>
              <div class="thread-links">{links}</div>
            </article>
            """
        )
    return "\n".join(cards)


def render_source_cards(sources: object, mode: str = "presentation") -> str:
    if not isinstance(sources, list) or not sources:
        return '<div class="empty-state">No converted sources found in this checkout.</div>'
    cards = []
    for source in sources:
        if not isinstance(source, dict):
            continue
        terms = " ".join(f"<span>{html.escape(str(term))}</span>" for term in source.get("terms", []))
        if mode == "research":
            meta_parts = [
                str(source.get("documentType") or source.get("sourceLabel") or "").strip(),
                f"pages {source.get('pageRange')}" if source.get("pageRange") else "",
                f"{source.get('chunks')} chunks" if source.get("chunks") else "",
                str(source.get("status") or "").replace("_", " "),
            ]
        else:
            dates = ", ".join(str(date) for date in source.get("dates", [])[:2])
            meta_parts = [
                str(source.get("sourceLabel") or source.get("documentType") or "").strip(),
                f"pages {source.get('pageRange')}" if source.get("pageRange") else "",
                dates,
            ]
        meta = " | ".join(part for part in meta_parts if part)
        title = source.get("displayTitle") or source.get("title", "")
        technical_title = str(source.get("technicalTitle") or source.get("title") or "")
        title_attr = (
            f' title="{escape_attr(technical_title)}"'
            if technical_title and technical_title != str(title)
            else ""
        )
        cards.append(
            f"""
            <a class="source-card" href="{escape_attr(str(source.get("url", "#")))}"{title_attr}>
              <strong>{html.escape(str(title))}</strong>
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


def render_timeline_preview(items: object, empty: str = "No dated family events yet.") -> str:
    if not isinstance(items, list) or not items:
        return f'<div class="empty-state">{html.escape(empty)}</div>'
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
      <h1>Names, Places, And Records</h1>
      <p>Family names, places, and record groups connected from the converted archive and promoted wiki pages.</p>
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
      <h1>Family Timeline</h1>
      <p>Family events and person facts only. Source dates, conversion dates, and research-operation dates stay in the source library and backroom dashboards.</p>
    </section>
    <section id="timeline-list" class="timeline-list"></section>
    """


def collections_body() -> str:
    return """
    <section class="page-head">
      <p class="eyebrow">Research Backroom</p>
      <h1>Rendered Shelves</h1>
      <p>Every rendered wiki and research page, grouped by internal shelf.</p>
    </section>
    <section id="collection-list" class="collection-list"></section>
    """


def sources_body() -> str:
    return """
    <section class="page-head">
      <p class="eyebrow">Source Library</p>
      <h1>Family Records And Archive Sources</h1>
      <p>Converted source groups are shown with presentation labels first; exact filenames and provenance remain inside each record page.</p>
    </section>
    <section class="source-browser-controls">
      <input id="source-filter" type="search" placeholder="Filter records, names, places">
    </section>
    <section id="source-browser" class="source-browser"></section>
    """


def render_markdown_page(page: SitePage, pages: list[SitePage], link_map: dict[str, SitePage]) -> str:
    source_link = html.escape(page.source_path.as_posix())
    display_title = page.title
    body_markdown = page.body
    original_title = ""
    if page.source_root == "converted":
        display_title = converted_page_presentation_title(page)
        body_markdown = strip_leading_heading(page.body)
        if display_title != page.title:
            original_title = f'<p class="source-path">Original source title: {html.escape(page.title)}</p>'
    body = f"""
    <article class="wiki-article">
      <header class="page-head">
        <p class="eyebrow">{html.escape(section_label(page.section))}</p>
        <h1>{html.escape(display_title)}</h1>
        {original_title}
        <p class="source-path">{source_link}</p>
      </header>
      {frontmatter_table(page.frontmatter)}
      {markdown_to_html(body_markdown, page, link_map)}
    </article>
    """
    depth = len(Path(page.site_rel).parent.parts)
    if page.source_root == "converted":
        active = "source-library"
    elif page.source_root == "wiki" and page.vault_rel == "index.md":
        active = "wiki-index"
    else:
        active = page.section
    return render_shell(display_title, body, active=active, depth=depth)


def converted_page_presentation_title(page: SitePage) -> str:
    summary = {
        "title": page.title,
        "technicalTitle": page.title,
        "documentType": page.frontmatter.get("document_type", ""),
        "pageRange": source_page_range(page.source_path.name),
        "terms": matched_focus_terms(f"{page.title} {page.text}"),
    }
    summary["sourceLabel"] = source_cluster_label(summary)
    return friendly_source_title(summary)


def strip_leading_heading(markdown: str) -> str:
    lines = markdown.splitlines()
    if lines and lines[0].startswith("# "):
        return "\n".join(lines[1:]).lstrip()
    return markdown


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
        ("index.html", "Home", "home"),
        ("tree.html", "Tree", "tree"),
        ("people.html", "People", "people"),
        ("timeline.html", "Timeline", "family-timeline"),
        ("sources.html", "Sources", "source-library"),
        ("research.html", "Research", "research"),
    ]
    nav_html = "\n".join(
        f'<a href="{prefix}{href}" class="{"active" if key == active else ""}">{label}</a>' for href, label, key in nav
    )
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)} | Family History</title>
  <link rel="stylesheet" href="{prefix}assets/styles.css">
</head>
<body data-active="{html.escape(active)}">
  <header class="topbar">
    <a class="brand" href="{prefix}index.html">Family History</a>
    <input id="site-search" type="search" placeholder="Search people, families, stories, records">
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
.story-head {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(260px, 360px);
  gap: 22px;
  align-items: end;
  margin: 18px 0 18px;
}
.story-copy h1 {
  margin: 0;
  max-width: 980px;
  font-size: clamp(2.4rem, 5vw, 5rem);
  line-height: 1.02;
  letter-spacing: 0;
}
.story-copy p {
  max-width: 820px;
  color: var(--muted);
  font-size: 1.08rem;
}
.story-note {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 16px;
  border: 1px solid var(--line);
  border-left: 4px solid var(--teal);
  border-radius: 8px;
  background: #fff;
  box-shadow: var(--shadow);
}
.story-note strong { color: var(--ink); }
.story-note span { color: var(--muted); font-size: .92rem; }
.family-hero {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(260px, 360px);
  gap: 22px;
  align-items: end;
  margin: 18px 0 18px;
}
.home-person-card {
  display: flex;
  min-width: 0;
  min-height: 190px;
  flex-direction: column;
  justify-content: flex-end;
  gap: 8px;
  padding: 18px;
  border: 1px solid var(--line);
  border-top: 4px solid var(--moss);
  border-radius: 8px;
  background: #fff;
  box-shadow: var(--shadow);
}
.home-person-card span {
  color: var(--clay);
  font-size: .76rem;
  font-weight: 800;
  text-transform: uppercase;
}
.home-person-card strong {
  color: var(--ink);
  font-size: 1.45rem;
  line-height: 1.12;
}
.home-person-card small { color: var(--muted); }
.home-person-card a { font-weight: 800; }
.tree-board {
  display: grid;
  gap: 10px;
  min-height: 250px;
  padding: clamp(18px, 3vw, 34px);
  border: 1px solid var(--line);
  border-radius: 8px;
  background:
    linear-gradient(#edf2f7 1px, transparent 1px),
    linear-gradient(90deg, #edf2f7 1px, transparent 1px),
    #fff;
  background-size: 34px 34px;
  box-shadow: var(--shadow);
}
.tree-network-board {
  min-height: 0;
  align-items: start;
}
.tree-generation {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  align-items: center;
  justify-content: center;
}
.home-row { align-items: stretch; }
.tree-person {
  display: flex;
  min-width: min(260px, 100%);
  max-width: 340px;
  min-height: 88px;
  flex-direction: column;
  justify-content: center;
  gap: 6px;
  padding: 14px 16px;
  border: 1px solid #bfd1cf;
  border-radius: 8px;
  background: #fff;
  color: var(--ink);
  box-shadow: 0 8px 22px rgba(21, 26, 35, 0.08);
}
.tree-person:hover { border-color: var(--teal); text-decoration: none; }
.tree-person strong { line-height: 1.15; }
.tree-person small { color: var(--muted); }
.home-person {
  border-color: var(--teal);
  border-width: 2px;
}
.tree-placeholder {
  padding: 12px 14px;
  border: 1px dashed #b9c4d2;
  border-radius: 8px;
  background: rgba(255, 255, 255, .78);
  color: var(--muted);
}
.tree-connector {
  width: 2px;
  height: 28px;
  justify-self: center;
  background: var(--teal);
}
.tree-network {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 12px;
}
.tree-edge {
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto minmax(0, 1fr);
  gap: 10px;
  align-items: center;
  min-height: 96px;
  padding: 14px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #fff;
  color: var(--ink);
}
.tree-edge:hover {
  border-color: var(--teal);
  text-decoration: none;
}
.tree-edge span,
.tree-edge strong {
  overflow-wrap: anywhere;
}
.tree-edge strong {
  color: var(--teal);
  text-align: center;
  font-size: 0.78rem;
  text-transform: uppercase;
}
.tree-edge small {
  grid-column: 1 / -1;
  color: var(--muted);
}
.home-related-edge {
  border-color: var(--teal);
  box-shadow: inset 4px 0 0 var(--teal);
}
.tree-more {
  color: var(--muted);
  font-weight: 700;
  text-align: center;
}
.family-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 20px;
  margin-top: 24px;
}
.family-grid > article {
  min-width: 0;
  padding-top: 6px;
  border-top: 2px solid var(--line);
}
.person-card-grid,
.story-card-grid,
.relationship-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 12px;
}
.person-card,
.story-card,
.relationship-card {
  display: flex;
  min-width: 0;
  min-height: 150px;
  flex-direction: column;
  gap: 8px;
  padding: 14px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #fff;
  color: var(--ink);
  box-shadow: var(--shadow);
}
.person-card:hover,
.story-card:hover,
.relationship-card:hover {
  border-color: #a8b8cc;
  text-decoration: none;
}
.person-card strong,
.story-card strong { line-height: 1.18; }
.person-card small,
.story-card small,
.relationship-card small {
  color: var(--muted);
}
.person-card p,
.story-card p,
.research-summary p {
  margin: 0;
  color: #405064;
  font-size: .92rem;
}
.family-card { border-top: 4px solid var(--gold); }
.story-card { border-top: 4px solid var(--blue); }
.relationship-card { min-height: 118px; }
.relationship-card span {
  color: var(--muted);
  overflow-wrap: anywhere;
}
.relationship-card strong {
  color: var(--teal);
  line-height: 1.15;
}
.tree-relationship-list { margin-top: 14px; }
.research-summary {
  color: var(--muted);
}
.story-metrics { grid-template-columns: repeat(4, minmax(0, 1fr)); }
.throughline-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 14px;
}
.throughline-card {
  display: flex;
  min-width: 0;
  min-height: 245px;
  flex-direction: column;
  gap: 10px;
  padding: 18px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #fff;
  box-shadow: var(--shadow);
}
.throughline-card > span {
  color: var(--gold);
  font-size: .76rem;
  font-weight: 800;
  text-transform: uppercase;
}
.throughline-card h3 {
  margin: 0;
  font-size: 1.18rem;
  line-height: 1.18;
}
.throughline-card p {
  margin: 0;
  color: var(--muted);
}
.thread-meta {
  display: flex;
  gap: 8px;
  align-items: baseline;
  color: var(--muted);
  font-size: .9rem;
}
.thread-meta strong { color: var(--teal); font-size: 1.45rem; }
.thread-meta i { margin-left: auto; font-style: normal; color: var(--clay); font-weight: 800; }
.thread-links {
  display: flex;
  flex-direction: column;
  gap: 5px;
  margin-top: auto;
}
.thread-links a {
  overflow-wrap: anywhere;
  color: var(--teal);
  font-size: .9rem;
}
.presentation-tools {
  grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
}
.research-tool {
  border-left: 4px solid var(--clay);
}
.story-grid {
  margin-top: 24px;
  grid-template-columns: minmax(0, 1.35fr) minmax(320px, .65fr);
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
.ops-link-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.ops-link-list a {
  padding: 10px 12px;
  border: 1px solid var(--line);
  border-radius: 6px;
  background: #fff;
  color: var(--ink);
}
.ops-link-list a:hover { border-color: #a8b8cc; text-decoration: none; }
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
  .topbar {
    grid-template-columns: 1fr;
    gap: 8px;
    padding: 10px 16px;
  }
  nav {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    justify-content: stretch;
    overflow: visible;
    padding-bottom: 0;
  }
  nav a {
    display: flex;
    min-height: 34px;
    align-items: center;
    justify-content: center;
    padding: 6px;
    text-align: center;
    white-space: normal;
    line-height: 1.15;
    font-size: .86rem;
  }
  .story-head { grid-template-columns: 1fr; }
  .family-hero { grid-template-columns: 1fr; }
  .family-grid { grid-template-columns: 1fr; }
  .tree-person { min-width: 100%; }
  .story-metrics { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .dashboard-head { display: block; }
  .alert-strip { grid-template-columns: 1fr; }
  .metric-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .dashboard-grid { grid-template-columns: 1fr; }
  .story-grid { grid-template-columns: 1fr; }
  .family-grid { grid-template-columns: 1fr; }
  .hero { grid-template-columns: 1fr; min-height: auto; }
  .hero-panel { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .timeline-item { grid-template-columns: 1fr; gap: 4px; }
}
@media (min-width: 761px) and (max-width: 1120px) {
  .metric-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .dashboard-grid { grid-template-columns: 1fr; }
  .story-metrics { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .story-grid { grid-template-columns: 1fr; }
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
      const active = document.body && document.body.dataset ? document.body.dataset.active : "";
      const publicOnly = !["research", "source-library", "evidence-map"].includes(active);
      const matches = data.pages
        .filter((page) => !publicOnly || page.sourceRoot === "wiki")
        .filter((page) => `${page.title} ${page.technicalTitle || ""} ${page.section} ${page.snippet}`.toLowerCase().includes(query))
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
      : '<div class="empty-state">No dated family events yet. Births, marriages, residences, migrations, deaths, and person-linked story events will appear here after review and promotion.</div>';
  }

  function renderSources() {
    const target = document.getElementById("source-browser");
    const filter = document.getElementById("source-filter");
    if (!target) return;
    const sources = (data.dashboard && data.dashboard.sources) || [];
    function draw() {
      const query = (filter && filter.value || "").trim().toLowerCase();
      const rows = sources
        .filter((source) => !query || `${source.displayTitle || ""} ${source.title} ${source.technicalTitle || ""} ${source.sourceLabel || ""} ${source.status} ${source.snippet} ${(source.terms || []).join(" ")}`.toLowerCase().includes(query))
        .slice(0, 120);
      target.innerHTML = rows.length
        ? rows.map((source) => {
          const terms = (source.terms || []).map((term) => `<span>${escapeHtml(term)}</span>`).join("");
          const bits = [source.sourceLabel || source.documentType, source.pageRange ? `pages ${source.pageRange}` : "", (source.dates || []).slice(0, 2).join(", ")].filter(Boolean).join(" &middot; ");
          const title = source.displayTitle || source.title;
          return `<a class="source-row" href="${escapeHtml(source.url)}" title="${escapeHtml(source.technicalTitle || source.title || "")}"><strong>${escapeHtml(title)}</strong><small>${escapeHtml(bits)}</small><p>${escapeHtml(source.snippet || "")}</p><span class="term-list">${terms}</span></a>`;
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
        const keep = new Set(nodes.filter((node) => `${node.title} ${node.technicalTitle || ""} ${node.section}`.toLowerCase().includes(query)).map((node) => node.id));
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
