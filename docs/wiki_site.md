# Wiki Site Automation

The family wiki is published by `.github/workflows/wiki-site.yml` to Cloudflare Workers Static Assets.

GitHub Pages is not the hosting target for this private repository. The current GitHub plan rejected Pages creation for a private repo, so the durable viewing path is a Cloudflare Worker that uploads the generated `site/` directory as static assets.

The workflow runs without provider model API keys and without the local PC:

- on every push to `main` that changes `wiki/`, `research/`, or the site generator
- after a successful `Internal Research Agents` run
- hourly at minute 41
- manually through `workflow_dispatch`

Each run refreshes generated indexes, rebuilds the family tree view, builds the static site with:

```powershell
python -m historic_doc_ingest.genealogy_wiki site --root . --out site
```

and deploys the `site/` folder with:

```powershell
npx --yes wrangler@latest deploy --config cloudflare/wiki-site/wrangler.jsonc
```

Expected production URL:

```text
https://genealogy-wiki-site.ajh-genealogy.workers.dev/
```

Required GitHub Actions secrets:

- `CLOUDFLARE_ACCOUNT_ID` or `R2_ACCOUNT_ID`
- `CLOUDFLARE_API_TOKEN` or `R2_TOKEN_VALUE`

The token must be able to deploy Workers. If the existing `R2_TOKEN_VALUE` is R2-only, replace it or add `CLOUDFLARE_API_TOKEN` with Workers deploy permission.

The site is generated from durable Markdown and JSON state. Do not hand-edit generated `site/` output; change the wiki/research Markdown or the generator instead.
