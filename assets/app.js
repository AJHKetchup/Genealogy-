
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
