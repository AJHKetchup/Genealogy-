# R2 Source Intake Preflight

Generated: 2026-05-16T13:22:57Z

Status: missing_config

## Storage Contract

R2 stores raw originals and durable binary assets; GitHub stores code, JSON, Markdown, manifests, queues, chunks, staging/proof data, and final HTML/build files.

## Required Configuration

Missing required config: R2_BUCKET, R2_ACCESS_KEY_ID, R2_SECRET_ACCESS_KEY

| Setting | Present | Source | Accepted Aliases | Secret |
| --- | --- | --- | --- | --- |
| R2_BUCKET | no | missing | none | no |
| R2_ACCESS_KEY_ID | no | missing | AWS_ACCESS_KEY_ID | yes |
| R2_SECRET_ACCESS_KEY | no | missing | AWS_SECRET_ACCESS_KEY | yes |

## Non-Secret Configuration

| Config | Value | Source |
| --- | --- | --- |
| account_id | e49bd1edd9fe4f9384b9cae226f7bf8a | default |
| endpoint_url | https://e49bd1edd9fe4f9384b9cae226f7bf8a.r2.cloudflarestorage.com | default |
| prefix |  | missing |
| raw_dir | raw/sources | default |
| state_dir | .genealogy/raw-cloud | default |

## Expected GitHub Artifacts

- derived_asset_manifest: `raw/r2-derived-assets.json`
- preflight_index: `research/_indexes/r2-source-intake-preflight.json`
- preflight_markdown: `research/r2-source-intake-preflight.md`
- r2_manifest: `raw/r2-raw-sources.json`
- r2_source_intake_state: `research/_automation/r2-source-intake-state.json`
- source_prep_manifest: `raw/source-prep-manifest.json`

## Safety

Only presence and source location are recorded; secret values are never written.

Next step: Set missing R2 config in the environment or .env.r2, then rerun the cloud source-prep heartbeat.
