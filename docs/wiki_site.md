# Wiki Site Automation

The family-facing wiki is published by `.github/workflows/wiki-site.yml` to Cloudflare Workers Static Assets.

GitHub Pages is not the hosting target for this private repository. The current GitHub plan rejected Pages creation for a private repo, so the durable viewing path is a Cloudflare Worker that uploads the generated `site/` directory as static assets.

The workflow runs without provider model API keys and without the local PC:

- on every push to `main` that changes `wiki/`, `research/`, or the site generator
- after a successful `Internal Research Agents` run
- hourly at minute 41
- manually through `workflow_dispatch`

Each run refreshes generated indexes, rebuilds the family tree view, builds the public presentation site from `wiki/` with:

```powershell
python -m historic_doc_ingest.genealogy_wiki site --root . --out site --wiki-only
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
- `CLOUDFLARE_API_TOKEN`

`R2_TOKEN_VALUE` is intentionally not used for the wiki deploy. R2-only tokens can upload bucket objects but cannot create or update the Worker that serves the private-repo wiki site.

Create `CLOUDFLARE_API_TOKEN` as a Cloudflare user API token that can deploy Workers. Cloudflare's own Workers build token includes Account Settings read, Workers Scripts edit, Workers KV edit, Workers R2 edit, Workers Routes edit, and User Details/Memberships read. The required part for this site deploy is Workers Scripts edit on the account, with account/user read permissions useful for Wrangler diagnostics.

The public site intentionally skips `research/` pages and converted-source pages. Research dashboards, source packets, conversion QA, staging drafts, and queue state remain in the repository and hosted agent outputs; reviewed wiki material is what gets published for family-facing exploration.

The site is generated from durable Markdown and JSON state. Do not hand-edit generated `site/` output; change the wiki/research Markdown or the generator instead.
