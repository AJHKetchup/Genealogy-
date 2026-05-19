# Wiki Site Automation

The family wiki is published by `.github/workflows/wiki-site.yml`.

The workflow runs without provider API keys and without the local PC:

- on every push to `main` that changes `wiki/`, `research/`, or the site generator
- after a successful `Internal Research Agents` run
- hourly at minute 41
- manually through `workflow_dispatch`

Each run refreshes generated indexes, rebuilds the family tree view, builds the static site with:

```powershell
python -m historic_doc_ingest.genealogy_wiki site --root . --out site
```

and deploys the `site/` folder to GitHub Pages.

The workflow also attempts to create/configure the repository's GitHub Pages site with `build_type: workflow`, so the first successful run should not require a manual Pages-settings click.

The site is generated from durable Markdown and JSON state. Do not hand-edit generated `site/` output; change the wiki/research Markdown or the generator instead.
