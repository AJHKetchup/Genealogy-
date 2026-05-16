(async () => {
  const input = document.getElementById("site-search-input");
  const results = document.getElementById("site-search-results");
  if (!input || !results) {
    return;
  }

  const response = await fetch("search-index.json");
  const payload = await response.json();
  const entries = Array.isArray(payload.entries) ? payload.entries : [];

  function entryText(entry) {
    return [entry.title, entry.kind, entry.excerpt, ...(entry.terms || [])].join(" ").toLowerCase();
  }

  function render(matches) {
    results.innerHTML = "";
    if (!matches.length) {
      const empty = document.createElement("li");
      empty.textContent = "No matching public pages found.";
      results.appendChild(empty);
      return;
    }
    for (const entry of matches) {
      const item = document.createElement("li");
      const link = document.createElement("a");
      link.href = entry.output.replace(/^site\//, "");
      link.textContent = entry.title;
      const kind = document.createElement("span");
      kind.className = "search-kind";
      kind.textContent = entry.kind;
      const excerpt = document.createElement("p");
      excerpt.textContent = entry.excerpt || "";
      item.append(link, kind, excerpt);
      results.appendChild(item);
    }
  }

  function runSearch() {
    const query = input.value.trim().toLowerCase();
    if (!query) {
      render(entries);
      return;
    }
    const terms = query.split(/\s+/).filter(Boolean);
    render(entries.filter((entry) => terms.every((term) => entryText(entry).includes(term))));
  }

  input.addEventListener("input", runSearch);
  render(entries);
})().catch((error) => {
  const results = document.getElementById("site-search-results");
  if (results) {
    results.innerHTML = "";
    const item = document.createElement("li");
    item.textContent = `Search index unavailable: ${error.message}`;
    results.appendChild(item);
  }
});
