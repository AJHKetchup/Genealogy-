from __future__ import annotations

import html
import json
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

WIKI_ONLY_EXCLUDE_DIRS = {"_templates"}
RESEARCH_EXCLUDE_DIRS = {
    "_agent-queues",
    "_automation",
    "_conversion-review",
    "_staging",
    "_templates",
}
RESEARCH_EXCLUDE_FILES = {"log.md"}

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

    return pages


def read_site_page(path: Path, root: Path, source_root: str) -> SitePage:
    source_base = root / source_root
    vault_rel = path.relative_to(source_base).as_posix()
    text = path.read_text(encoding="utf-8")
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
        page.frontmatter.get("birth", ""),
        page.frontmatter.get("death", ""),
        page.frontmatter.get("created", ""),
        page.frontmatter.get("updated", ""),
    ]
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
    dates: list[str] = []
    for match in DATE_RE.finditer(value or ""):
        year, month, day = match.groups()
        if month and day:
            dates.append(f"{int(year):04d}-{int(month):02d}-{int(day):02d}")
        elif month:
            dates.append(f"{int(year):04d}-{int(month):02d}")
        else:
            dates.append(f"{int(year):04d}")
    return dates


def build_site_data(root: Path, pages: list[SitePage], link_map: dict[str, SitePage]) -> dict[str, object]:
    page_items = []
    graph_edges = []
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
        for date in page.dates
    ]
    timeline_items.sort(key=lambda item: item["date"])

    return {
        "generatedAt": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "pages": page_items,
        "links": dedupe_edges(graph_edges),
        "counts": dict(sorted(counts.items())),
        "timeline": timeline_items[:500],
        "sections": [
            {"id": section, "label": section_label(section), "count": count}
            for section, count in sorted(counts.items())
        ],
    }


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
    featured = sorted(pages, key=lambda page: (page.source_root != "wiki", page.section, page.title))[:8]
    cards = "\n".join(
        f"""
        <a class="feature-card" href="{escape_attr(page.site_rel)}">
          <span>{html.escape(section_label(page.section))}</span>
          <strong>{html.escape(page.title)}</strong>
          <small>{html.escape(page.text[:110])}</small>
        </a>
        """
        for page in featured
    )
    stats = "\n".join(
        f"""<div class="stat"><strong>{section['count']}</strong><span>{html.escape(section['label'])}</span></div>"""
        for section in data.get("sections", [])
    )
    body = f"""
    <section class="hero">
      <div>
        <p class="eyebrow">Family Wiki</p>
        <h1>Genealogy, sources, and evidence in one living view.</h1>
        <p>The site rebuilds from the Markdown vault automatically, so new promoted people, claims, relationships, sources, photos, and narratives appear here without hand-publishing.</p>
      </div>
      <div class="hero-panel" aria-label="Wiki stats">
        {stats or '<div class="stat"><strong>0</strong><span>Pages yet</span></div>'}
      </div>
    </section>
    <section class="tool-grid">
      <a href="graph.html" class="tool-link"><strong>Graph</strong><span>Follow people, claims, source packets, and relationships as a connected map.</span></a>
      <a href="timeline.html" class="tool-link"><strong>Timeline</strong><span>Scan dated events and source moments as they enter the wiki.</span></a>
      <a href="collections.html" class="tool-link"><strong>Collections</strong><span>Browse the vault by shelf: people, places, sources, photos, claims, and more.</span></a>
    </section>
    <section>
      <div class="section-heading"><h2>Start Here</h2><span>{len(pages)} rendered pages</span></div>
      <div class="feature-grid">{cards}</div>
    </section>
    """
    return render_shell("Genealogy Wiki", body, active="home")


def render_special_page(title: str, body: str) -> str:
    return render_shell(title, body, active=slugify(title))


def graph_body() -> str:
    return """
    <section class="page-head">
      <p class="eyebrow">Evidence Map</p>
      <h1>Research Graph</h1>
      <p>Links are generated from wiki links and relationship indexes. Use the search box to focus the map.</p>
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
      <p>Dates are extracted from frontmatter and visible page text, then updated whenever the site rebuilds.</p>
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
        ("index.html", "Home", "home"),
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
  --ink: #17201d;
  --muted: #61706b;
  --paper: #f7f4ee;
  --panel: #ffffff;
  --line: #d8ded6;
  --teal: #0f766e;
  --moss: #496b3a;
  --clay: #9a4f2f;
  --gold: #b7791f;
  --shadow: 0 18px 45px rgba(31, 35, 31, 0.12);
}
* { box-sizing: border-box; }
body {
  margin: 0;
  color: var(--ink);
  background: linear-gradient(180deg, #fbfaf6 0%, var(--paper) 100%);
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
  grid-template-columns: minmax(150px, 210px) minmax(180px, 1fr) auto;
  gap: 16px;
  align-items: center;
  padding: 12px clamp(18px, 3vw, 42px);
  border-bottom: 1px solid var(--line);
  background: rgba(255, 255, 255, 0.92);
  backdrop-filter: blur(12px);
}
.brand { color: var(--ink); font-weight: 800; letter-spacing: 0; }
nav { display: flex; gap: 6px; flex-wrap: wrap; justify-content: flex-end; }
nav a {
  padding: 7px 10px;
  color: var(--muted);
  border-radius: 6px;
}
nav a.active, nav a:hover { color: var(--ink); background: #edf4ef; text-decoration: none; }
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
  width: min(1180px, calc(100vw - 32px));
  margin: 0 auto;
  padding: 26px 0 70px;
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
  .hero { grid-template-columns: 1fr; min-height: auto; }
  .hero-panel { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .timeline-item { grid-template-columns: 1fr; gap: 4px; }
}
"""


SITE_JS = r"""
(function () {
  const data = window.GENEALOGY_SITE_DATA || { pages: [], links: [], timeline: [], sections: [] };
  const byId = new Map(data.pages.map((page) => [page.id, page]));

  function rootPrefix() {
    const path = window.location.pathname.replace(/\\/g, "/");
    const segments = path.split("/").filter(Boolean);
    const marker = segments.findIndex((segment) => segment === "wiki" || segment === "research");
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
        ? matches.map((page) => `<a href="${rootPrefix()}${page.url}"><strong>${escapeHtml(page.title)}</strong><br><small>${escapeHtml(page.section)} · ${escapeHtml(page.snippet || "")}</small></a>`).join("")
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
      ? data.timeline.map((item) => `<a class="timeline-item" href="${item.url}"><span class="timeline-date">${escapeHtml(item.date)}</span><span><strong>${escapeHtml(item.title)}</strong><br><small>${escapeHtml(item.section)} · ${escapeHtml(item.type)}</small></span></a>`).join("")
      : '<div class="empty-state">No dated wiki pages yet. As agents promote sourced events, this timeline will fill itself in.</div>';
  }

  function renderGraph() {
    const svg = document.getElementById("graph-svg");
    if (!svg) return;
    const filter = document.getElementById("graph-filter");
    const reset = document.getElementById("graph-reset");
    function draw() {
      const query = (filter && filter.value || "").trim().toLowerCase();
      let nodes = data.pages.map((page) => ({ ...page }));
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
    nodes.forEach((node) => {
      const group = svgEl("g", { tabindex: "0", role: "link" });
      const color = colorFor(node.section);
      group.appendChild(svgEl("circle", { cx: node.x, cy: node.y, r: node.section === "people" ? 9 : 7, fill: color, stroke: "#fff", "stroke-width": "2" }));
      group.appendChild(svgEl("text", { x: node.x + 11, y: node.y + 4, fill: "#17201d", "font-size": "12" }, node.title));
      group.addEventListener("click", () => { window.location.href = node.url; });
      group.addEventListener("keydown", (event) => { if (event.key === "Enter") window.location.href = node.url; });
      svg.appendChild(group);
    });
  }

  function colorFor(section) {
    const colors = { people: "#0f766e", families: "#496b3a", claims: "#9a4f2f", relationships: "#b7791f", sources: "#5b5f97", "source-packets": "#7c3aed", photos: "#be185d", places: "#2563eb" };
    return colors[section] || "#61706b";
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
  renderGraph();
})();
"""
