# Cloudflare Source Conversion Dispatcher

This Worker is the Cloudflare-side health check for automatic genealogy source conversion.

Current state: deployed as a preflight/dispatcher shell. It verifies:

- Cloudflare Secrets Store bindings
- R2 bucket binding for `genealogy`
- hourly cron trigger wiring
- storage-contract boundaries
- R2 contract audit for misplaced JSON, Markdown, manifests, or code-like objects

Production URL:

- `https://genealogy-source-prep-dispatcher.ajh-genealogy.workers.dev/health`

It does not write JSON or Markdown into R2. R2 remains for raw originals and binary derivatives only. GitHub remains the system of record for converted Markdown and the minimal manifests/queue state needed to resume conversion.

## Bindings

- `GENEALOGY_R2`: R2 bucket binding for `genealogy`
- `GEMINI_API_KEY`: Secrets Store secret
- `GITHUB_TOKEN`: Secrets Store secret
- `R2_ACCOUNT_ID`: Secrets Store secret
- `R2_BUCKET`: Secrets Store secret
- `R2_ENDPOINT_URL`: Secrets Store secret
- `GITHUB_OWNER`: plain Worker var, currently `AJHKetchup`
- `GITHUB_REPO`: plain Worker var, currently `Genealogy-`

## Endpoints

- `/health`
- `/run`

Both return a no-secret JSON preflight report. Secret values are never returned.

The report includes an R2 contract audit sample. Any JSON/Markdown/code/manifest-looking object in R2 is treated as misplaced because those artifacts belong in GitHub.
