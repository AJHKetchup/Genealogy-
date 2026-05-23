from __future__ import annotations

from pathlib import Path


def test_wiki_site_workflow_deploys_cloudflare_worker_site() -> None:
    workflow = (Path(__file__).resolve().parents[1] / ".github" / "workflows" / "wiki-site.yml").read_text(
        encoding="utf-8"
    )

    assert "scripts/build-wiki-site-worker.mjs" in workflow
    assert "site-worker/index.mjs" in workflow
    assert 'node-version: "22"' in workflow
    assert "npx wrangler@latest deploy --config cloudflare/wiki-site/wrangler.embedded.jsonc" in workflow
    assert "CLOUDFLARE_ACCOUNT_ID" in workflow
    assert "secrets.R2_ACCOUNT_ID" in workflow
    assert "CLOUDFLARE_API_TOKEN" in workflow
    assert "genealogy-wiki-site.ajh-genealogy.workers.dev/tree" in workflow
    assert "genealogy-wiki-site.ajh-genealogy.workers.dev/people/dario-arturo-pulgar-smith" in workflow
    assert "Alexander John Heinz" in workflow
    assert "gh-pages" not in workflow
    assert "GitHub Pages" not in workflow
    assert "PAGES_ADMIN_TOKEN" not in workflow
