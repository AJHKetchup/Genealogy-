---
type: proof_review
status: hold
role: claim_reviewer
worker: postconv-proof-review-20260529215027737
task_id: "proof-review:research/_staging/identity-analysis/chunk-a7725d7a5344-p0036-01-page-alignment-and-identity-watch-postconv-identity-analysis-20260529193123014.md"
staged_draft: "research/_staging/identity-analysis/chunk-a7725d7a5344-p0036-01-page-alignment-and-identity-watch-postconv-identity-analysis-20260529193123014.md"
source_packet: "research/_staging/source-packets/chunk-a7725d7a5344-p0036-01-dario-pulgar-arriagada-chile-delegate.md"
converted_file: "raw/converted/ca09a98281-r3578-50-5569-5569-jacke-p0026-0050-r3578-50-5569-5569-jacket5-pages-26-50.codex.md"
chunk: "raw/chunks/ca09a98281-r3578-50-5569-5569-jacke-p0026-0050-r3578-50-5569-5569-jacket5-pages-26-50-codex/page-0036-chunk-01.md"
reviewed_at: 2026-05-29
canonical_readiness: hold
---

# Proof Review: Dario Pulgar-Arriagada Delegate Entry

## Blockers First

1. Source/image verification is blocked in this checkout. `raw/sources/R3578-50-5569-5569-Jacket5.pdf` is not present, and the cited conversion-job `page-images` directory is not present, so I could not visually verify the source page.
2. Page alignment remains unresolved. `page-markdown/page-0036.md` contains unrelated French medical-condition text, while `page-markdown/page-0041.md` contains internal page number `36` and the Chile delegate-list text naming `Captain Dario Pulgar-Arriagada, Medical Corps;`.
3. Provenance identifiers are inconsistent. The staged draft and source packet cite `CHUNK-a7725d7a5344-P0036-01` and converted SHA `a7725d7a...`, while the actual referenced chunk and chunk manifest report `CHUNK-93fa0ef652f0-P0036-01` and converted SHA `93fa0ef6...`.
4. The reviewed derivative text gives no age, birth date, residence, parents, spouse, children, signature, full middle name, or family relationship. It does not support attachment to `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario Pulgar A.`, passenger stubs, property clusters, or Jose/Juana parent candidates.

## Evidence Strengths

The staged draft, source packet, aggregate converted file, chunk text, and `page-markdown/page-0041.md` agree on the narrow derivative reading under `THE PRESIDENT OF THE REPUBLIC OF CHILE`:

```text
Captain Dario Pulgar-Arriagada, Medical Corps;
```

This supports only a page-local delegate-list identity and rank/service claim if source-page alignment is later verified. The source type appears stronger than casual narrative because it is an official convention delegate list, but current source access is derivative-only.

## Scored Judgment

| metric | score | rationale |
| --- | ---: | --- |
| source_quality_score | 0.62 | Official delegate-list source context appears reliable, but the raw PDF and rendered page image are unavailable for direct review. |
| conversion_confidence_score | 0.56 | The key name/rank/service line is stable across derivative files, but page 36/page 41 and hash/id mismatches materially reduce confidence. |
| evidence_quantity_score | 0.40 | One page-local entry only; no independent bridge, vital record, household record, or relationship evidence was reviewed. |
| agreement_score | 0.70 | Derivative texts agree on the narrow wording, but conversion-job page alignment conflicts with the assigned page reference. |
| identity_confidence_score | 0.84 | Strong for the page-local `Dario Pulgar-Arriagada` delegate identity only; weak for any broader same-person merge. |
| claim_probability | 0.74 | Likely as a derivative-text claim, but not ready for canonical use until visible source/page alignment is resolved. |
| relevance_level | high | Directly reviews the assigned staged identity-analysis draft and cited Pulgar-Arriagada evidence. |
| relevance_confidence | 0.96 | The reviewed files are the exact staged draft, cited source packet, cited chunk, cited converted aggregate, and implicated page Markdown. |
| canonical_readiness | 0.18 | Hold. Do not promote until source/page-image alignment and provenance identifiers are reconciled. |

## Identity And Relationship Risk

Identity risk is moderate to high if the entry is merged by name alone. The reviewed entry states a Chile delegate-list name, rank, and Medical Corps affiliation, but it does not establish middle names, parents, family line, property ownership, passenger identity, or later CV/Habitat identity.

Relationship risk is high for any Jose/Juana lineage claim because no Jose, Juana, parent, spouse, child, household, or family relationship appears in the reviewed text.

## Review Decision

Hold. The derivative files plausibly support a bounded claim that `Dario Pulgar-Arriagada` appears under Chile as `Captain ... Medical Corps`, but the claim is not canonical-ready because the source PDF/page image is unavailable and the page-control metadata conflicts.

## Next Action

Restore or locate the raw PDF/rendered page image, then compare internal printed page `36`, conversion-job `page-markdown/page-0041.md`, aggregate converted-file lines for the Chile delegate section, and the assigned chunk path. If the visible source confirms the line and the page offset is explained, promote only the narrow delegate/rank/service claim. Run a separate identity-bridge review before attaching the claim to any broader Pulgar, Pulgar-Arriagada, Pulgar-Smith, passenger, property, CV, or Jose/Juana cluster.
