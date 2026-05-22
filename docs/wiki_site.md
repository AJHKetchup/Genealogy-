# Wiki Site Automation

The family-facing wiki is published by `.github/workflows/wiki-site.yml` to GitHub Pages.

The repository is public, so GitHub Pages is the durable default viewing path. The workflow runs in GitHub Actions, so it does not depend on the local PC being on and does not need Cloudflare or model-provider secrets.

The workflow runs without provider model API keys and without the local PC:

- on every push to `main` that changes `wiki/`, `research/`, or the site generator
- after a successful `Internal Research Agents` run
- hourly at minute 41
- manually through `workflow_dispatch`

Each run refreshes generated indexes, rebuilds the family tree view, builds the public presentation site from `wiki/` with:

```powershell
python -m historic_doc_ingest.genealogy_wiki site --root . --out site --wiki-only
```

Then it uploads the generated `site/` directory as a GitHub Pages artifact and deploys it with GitHub's official Pages actions:

```powershell
actions/configure-pages@v5
actions/upload-pages-artifact@v4
actions/deploy-pages@v4
```

Expected production URL:

```text
https://ajhketchup.github.io/Genealogy-/
```

The public site intentionally skips `research/` pages and converted-source pages. Research dashboards, source packets, conversion QA, staging drafts, and queue state remain in the repository and hosted agent outputs; reviewed wiki material is what gets published for family-facing exploration.

Cloudflare Worker configs remain in `cloudflare/wiki-site/` as optional fallback infrastructure, but the default hosted deploy is GitHub Pages because it avoids Cloudflare entitlement failures and rotating Cloudflare tokens.

The site is generated from durable Markdown and JSON state. Do not hand-edit generated `site/` output; change the wiki/research Markdown or the generator instead.
