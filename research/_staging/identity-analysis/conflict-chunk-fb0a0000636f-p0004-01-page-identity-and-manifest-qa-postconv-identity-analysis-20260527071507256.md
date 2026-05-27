---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/conflicts/conflict-chunk-fb0a0000636f-p0004-01-page-identity-and-manifest-qa.md
worker: postconv-identity-analysis-20260527071507256
staged_draft: research/_staging/conflicts/conflict-chunk-fb0a0000636f-p0004-01-page-identity-and-manifest-qa.md
source: raw/sources/CV of Dario Arturo Pulgar.pdf
source_packet: research/_staging/source-packets/chunk-fb0a0000636f-p0004-01-cv-dario-arturo-pulgar-work-history.md
converted_file: raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md
chunk: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0004-chunk-01.md
chunk_manifest: raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/manifest.json
page_image: raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0004.jpg
chunk_id: CHUNK-fb0a0000636f-P0004-01
page_reference: page 4
analysis_status: hold
canonical_readiness: not_ready
---

# Identity/Conflict Analysis: CHUNK-fb0a0000636f-P0004-01

## Blockers

- Page-control blocker: the existing rendered page image for page 4 matches the current converted file's 2000 and 1999-2000 work-history text, not the referenced chunk/source-packet text for 1988-1989, 1988, 1986-1987, and 1982-1985.
- Manifest blocker: `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/manifest.json` lists `CHUNK-fb0a0000636f-P0004-01` twice for page 4 with the same chunk path but different character counts and hashes.
- Claim-control blocker: staged claims `chunk-fb0a0000636f-p0004-01-001` through `005` cite page 4 for 1982-1989 roles, but the page image and current converted file show different page-4 content. Those claims cannot be promoted from this page reference until source-prep QA reconciles the duplicate chunk records.
- Identity blocker: neither the page image nor the page body names Dario Arturo Pulgar. Subject attribution is document-level from the file/source title and metadata.
- Canonical bridge blocker: page 4 does not prove that `Dario Arturo Pulgar` is the same person as canonical `wiki/people/dario-arturo-pulgar-smith.md`, nor does it connect to `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, `Jose del Carmen Pulgar`, or any Juana parent candidate.
- Scope blocker: this note is an identity/conflict hold only. It does not edit raw sources, converted Markdown, chunks, source packets, claims, or canonical wiki pages.

## Evidence Reviewed

Literal source/control readings:

- Staged conflict draft: `research/_staging/conflicts/conflict-chunk-fb0a0000636f-p0004-01-page-identity-and-manifest-qa.md`.
- Staged source packet: `research/_staging/source-packets/chunk-fb0a0000636f-p0004-01-cv-dario-arturo-pulgar-work-history.md`.
- Referenced chunk: `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/page-0004-chunk-01.md`.
- Current converted file: `raw/converted/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9.codex.md`.
- Chunk manifest: `raw/chunks/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9-codex/manifest.json`.
- Rendered page image: `raw/codex-conversion-jobs/ca07263f40-cv-of-dario-arturo-pulga-p0004-0009-cv-of-dario-arturo-pulgar-pages-4-9/page-images/page-0004.jpg`.
- Canonical context pages reviewed: `wiki/people/dario-arturo-pulgar-smith.md`, `wiki/people/dar-o-pulgar-arriagada.md`, `wiki/people/dario-pulgar-adult-passenger-age-64.md`, `wiki/people/dario-pulgar-child-passenger-age-11.md`, `wiki/people/jose-del-carmen-pulgar.md`, and `wiki/people/juana-arriagada-de-pulgar.md`.

Interpretive note:

- The page-image comparison was a visual review of an existing rendered image, not a new conversion run. No external research was performed.

## Hypothesis 1: Page 4 Controls To The Current Converted Text, Not The Referenced Chunk Text

Hypothesis: the controlling page-4 evidence for `CHUNK-fb0a0000636f-P0004-01` should be treated as unresolved because the page image and current converted file show 2000/1999-2000 content, while the referenced chunk/source packet show 1982-1989 content under the same chunk id and path.

Supporting evidence:

- The current converted file's page 4 starts with continuation text about `Indian States`, `Social impact analysis and consultation processes`, and `Monitoring and evaluation`.
- The rendered page image for page 4 visibly contains the same continuation text and the entries `2000 / International Bank for Reconstruction and Development (IBRD) / Bolivia, Peru / Senior Consultant` and `1999 - 2000 / Antamina Mining Company / Huarmey, Peru / Head Community Relations`.
- The referenced chunk body instead begins with an Egypt-extension continuation and then lists `1988-1989 / Food and Agriculture Organisation of the United Nations (FAO) / Ndola, Zambia / Training and Communication Advisor`, `1988 / Canadian International Development Agency (CIDA) / Ethiopia / Communication Consultant`, `1986 - 1987 / Worldview International Foundation (WIF) / Rome, Italy / Rural Communications and Extension Advisor`, and `1982-1985 / Independent communications consultant / Canadian International Development Agency`.
- The manifest preserves the anomaly directly by listing the same page-4 chunk id/path twice with different `chars` and `sha256` values.

Conflicts:

- Conversion/page-control conflict: high. Two different page bodies are attached to the same page/chunk identity.
- Chronology conflict: procedural, not biographical. The 1982-1989 and 1999-2000 entries could coexist in a CV, but they cannot both be the same page 4 under the same chunk identity without a page-control explanation.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.45 | The source title points to Dario Arturo Pulgar, but the controlling page body for this staged page is unresolved. |
| conflict_severity | 0.90 | The duplicate chunk id/path with different page bodies blocks reliable promotion. |
| evidence_quality | 0.76 | The local page image and converted file directly agree, while the chunk/source packet disagree. |
| conversion_confidence | 0.35 | Text is readable, but page-control integrity is not reliable for this staged chunk. |
| claim_probability | 0.20 | Low for the staged 1982-1989 claims as page-4 claims because the page image does not show them. |
| relevance | 0.95 | Directly relevant to whether this staged conflict can proceed. |
| canonical_readiness | 0.05 | Not ready for canonical use. |

## Hypothesis 2: Document-Level CV Subject Is Dario Arturo Pulgar

Hypothesis: regardless of the page-control conflict, the source package belongs to a CV locally identified as `Dario Arturo Pulgar`.

Supporting evidence:

- The source path is `raw/sources/CV of Dario Arturo Pulgar.pdf`.
- The converted file title is `CV of Dario Arturo Pulgar pages 4-9`.
- The staged source packet and staged claims identify the document-level subject as `Dario Arturo Pulgar`.

Conflicts:

- The page body does not repeat the subject name.
- The page-control conflict weakens confidence that the extracted claims are tied to the correct page.
- The name form `Dario Arturo Pulgar` is not the same as canonical `Dario Arturo Pulgar-Smith`.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.68 | Document metadata consistently identifies the CV subject, but page 4 itself does not name him. |
| conflict_severity | 0.60 | Subject identity is plausible, but the page-control conflict blocks claim-level use. |
| evidence_quality | 0.62 | Metadata evidence is consistent; page-local evidence is absent. |
| conversion_confidence | 0.35 | Page-control integrity remains unresolved. |
| claim_probability | 0.62 | Probable only for document-level subject attribution, not for the specific staged page-4 claims. |
| relevance | 0.88 | Necessary for later CV evidence handling. |
| canonical_readiness | 0.15 | Hold until page-control and identity-bridge review are complete. |

## Hypothesis 3: CV Subject Is The Same Person As Dario Arturo Pulgar-Smith

Hypothesis: `Dario Arturo Pulgar` in the CV is a shortened or partial name form for canonical `Dario Arturo Pulgar-Smith`.

Supporting evidence:

- Canonical `wiki/people/dario-arturo-pulgar-smith.md` records the family-supplied preferred name `Dario Arturo Pulgar-Smith`.
- The CV source title and staged materials use the matching given names `Dario Arturo` and surname element `Pulgar`.
- The canonical page instructs that similarly named `Dario`, `Pulgar`, `Pulgar-Arriagada`, or `Pulgar-Smith` records require identity review before attachment.

Conflicts:

- No reviewed page-4 evidence states `Pulgar-Smith`.
- No reviewed page-4 evidence states the maternal-grandfather relationship to Alexander John Heinz.
- No reviewed page-4 evidence gives birth, spouse, child, parent, residence, or other bridge data.
- Same-person attachment would be risky while the page-control conflict remains open.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.48 | Plausible name overlap, but no page-local bridge to the canonical person. |
| conflict_severity | 0.55 | A mistaken attachment would misattribute career evidence to the canonical person. |
| evidence_quality | 0.38 | The supporting evidence is name overlap plus family context, not direct proof. |
| conversion_confidence | 0.35 | Conversion/page-control blocker still applies. |
| claim_probability | 0.44 | Possible, not proven. |
| relevance | 0.82 | Relevant because staged claims use `Dario Arturo Pulgar`. |
| canonical_readiness | 0.08 | Not ready for canonical attachment or merge. |

## Hypothesis 4: Distinct Or Unresolved Pulgar-Line Dario Candidates

Hypothesis: `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, and `Dario/Dario Pulgar Arriagada` should remain separate or unresolved clusters unless a later proof-review step supplies a bridge.

Supporting evidence:

- Canonical `Dario Arturo Pulgar-Smith` is family-supplied as Alexander John Heinz's maternal grandfather and explicitly warns against automatic merge with similar names.
- Canonical `Darío Pulgar Arriagada` currently has a separate evidence snapshot tied to a 2000 expropriation resolution.
- Existing local context includes distinct staged clusters for a child passenger age 11 and an adult passenger age 64 named `Dario Pulgar`.
- Existing local context includes separate Jose/Juana parent candidates, including `Jose del Carmen Pulgar`, `Juana Arriagada de Pulgar`, and other held Juana readings. This staged CV page does not name any of them.

Conflicts:

- Same-person and duplicate-person risk is moderate to high if the names are merged by shared `Dario Pulgar` elements alone.
- Relationship-conflict evidence is absent in this staged page; the page cannot resolve parent, child, or grandparent identities.
- Chronology-conflict evidence is not sufficient to merge or split identities because the controlling page text itself is unresolved.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.70 | Strong confidence that the clusters should remain unmerged for now. |
| conflict_severity | 0.75 | Premature merge would affect multiple Pulgar-line candidates. |
| evidence_quality | 0.58 | Canonical and staged context support caution, but this page gives no direct family evidence. |
| conversion_confidence | 0.35 | The assigned page-control issue still limits this staged draft. |
| claim_probability | 0.78 | Probable that no merge is currently supported. |
| relevance | 0.90 | Directly relevant to Pulgar-line identity handling. |
| canonical_readiness | 0.10 | Ready only as a hold recommendation, not as promoted facts. |

## Conflict Summary

- Same-person evidence: insufficient for attaching this page to `Dario Arturo Pulgar-Smith`; document-level `Dario Arturo Pulgar` remains plausible but unbridged.
- Duplicate-person evidence: unresolved; keep Dario Arturo Pulgar, Dario Arturo Pulgar-Smith, Dario Jose Pulgar-Arriagada, Darío Pulgar Arriagada, child/adult passenger Dario Pulgar candidates, and Jose/Juana parent candidates separate unless a later proof review supplies direct bridging evidence.
- Name-variant evidence: `Dario Arturo Pulgar` could be a variant of `Dario Arturo Pulgar-Smith`, but this staged draft does not prove the variant.
- Relationship-conflict evidence: none on this page. No parent, spouse, child, grandparent, Jose, or Juana relationship claim is supported here.
- Chronology-conflict evidence: no direct biographical contradiction; the apparent chronology issue is a page-control/manifest conflict, not proof that one person could not have held the roles.
- Conversion/page-control evidence: severe blocker. The page image and current converted file support 2000/1999-2000 page-4 text; the referenced chunk/source packet support 1982-1989 text under the same page/chunk identity.

## Recommended Next Action

Run a targeted source-prep/conversion QA review, not canonical promotion. The exact next proof-review or promotion prerequisite is:

1. Reconcile `CHUNK-fb0a0000636f-P0004-01` in the chunk manifest against the existing page image and current converted file.
2. Decide whether the 1982-1989 work-history text belongs to another page number or stale chunk state, and update/regenerate staged source packets and claims only through the appropriate source-prep workflow.
3. After page-control QA, rerun proof review for any surviving employment claims.
4. Only after page-control QA and proof review, perform a separate identity-bridge review before attaching any CV claims to canonical `Dario Arturo Pulgar-Smith` or merging any Pulgar-line candidates.

Current promotion decision: `do_not_promote`.
