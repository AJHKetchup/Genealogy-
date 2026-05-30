---
type: proof_review
status: complete
role: claim_reviewer
worker: postconv-proof-review-20260530172330919
task_id: "proof-review:research/_staging/identity-analysis/chunk-ff8bc4b91301-p0005-01-pulgar-identity-bridge-hold-postconv-identity-analysis-20260530164612067.md"
staged_draft: "research/_staging/identity-analysis/chunk-ff8bc4b91301-p0005-01-pulgar-identity-bridge-hold-postconv-identity-analysis-20260530164612067.md"
reviewed_claim_type: identity_conflict_analysis
reviewed_subject: "Page-5 surname-only Pulgar identity bridge"
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
source_packet: "research/_staging/source-packets/chunk-ff8bc4b91301-p0005-01-habitat-revisited-pulgar-vancouver-hold-postconv-evidence-extraction-20260530155324642.md"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-page-7cd35b519c/page-0005-chunk-01.md"
chunk_id: CHUNK-ff8bc4b91301-P0005-01
source_page_image_checked: false
source_quality_score: 0.58
conversion_confidence_score: 0.34
evidence_quantity_score: 0.42
agreement_score: 0.46
identity_confidence_score: 0.64
claim_probability: 0.67
relevance_level: direct
relevance_confidence: 0.95
canonical_readiness: hold_for_conversion_qa
---

# Proof Review: Page-5 Pulgar Identity Bridge Hold

## Blockers

- Canonical readiness is `hold_for_conversion_qa`. The staged draft correctly keeps the item out of canonical claims, relationships, and wiki pages.
- The page-5 rendered image is still unavailable at `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0005.jpg`, so the page-5 text was not visually proofed.
- Provenance is inconsistent. The chunk and source packet record converted SHA-256 `ff8bc4b9130169ba6f4ecc103ba089ba6bf26c7162f5dfebbf3bae9ebd3a7271`, while the live converted file hashes to `97c8a1cbf4db9e4e39f2044e3260d5938381e2a89583f8e49e6777c77d13444c`.
- Page 5 literally names only `Pulgar`. It does not state `Dario`, `Arturo`, `Smith`, `Pulgar-Smith`, `Jose`, `Juana`, `Arriagada`, a family relationship, parentage, spouse, child, grandchild, birth detail, or residence lineage.
- The same-source page-7 `Dario Pulgar` context supports a plausible bridge lead, but it is adjacent-context evidence, not a page-5 full-name reading. Existing page-7 proof review also kept that evidence on conversion-QA hold because of metadata inconsistency.
- The source is a 2006 memoir/recollection. It is useful for narrative and occupational context, but weaker than contemporary official records for identity or relationship proof.

## Evidence Strengths

- The referenced page-5 chunk and source packet agree on the key literal passage: a small group including `Pulgar`, `Gyborg`, `Jane Weiner`, `Barbara Janes`, and the narrator would go to Vancouver to help get the show "on the air."
- The same page supports the Vancouver timing and setting in the converted text: the group arrived in Vancouver on May 19 before the May 31 conference opening, then worked in makeshift Begg Building offices.
- The staged draft's ranked hypotheses are appropriately cautious. It gives strongest weight to a source-local surname-only `Pulgar`, treats same-source `Dario Pulgar` as a likely but unproved bridge, and rejects attachment to Pulgar-Smith, Pulgar-Arriagada, passenger, or Jose/Juana parent candidates from page 5 alone.
- No conflict was found between the draft's blockers and the available packet/chunk evidence. The main problem is not overstatement of page-5 literal support; it is the unresolved image/hash QA and bridge evidence limits.

## Scored Judgment

| score | value | rationale |
| --- | ---: | --- |
| source_quality_score | 0.58 | Participant memoir/recollection gives useful firsthand context, but it is retrospective and not a vital, civil, immigration, or relationship record. |
| conversion_confidence_score | 0.34 | Text-layer chunk is readable, but the page image is missing and the live converted hash disagrees with chunk/source-packet metadata. |
| evidence_quantity_score | 0.42 | One direct page-5 surname mention plus same-source page-7 context; no independent corroborating identity or relationship source reviewed for this task. |
| agreement_score | 0.46 | Page-5 chunk and packet agree on substance, but image availability and hash/provenance do not agree. |
| identity_confidence_score | 0.64 | Moderate for one source-local person called `Pulgar`; low for any fuller or canonical identity. |
| claim_probability | 0.67 | Probable that page 5 refers to the same source-local person later named `Dario Pulgar`, but the bridge remains inferential and QA-blocked. |
| relevance_level | direct | The reviewed evidence directly concerns the assigned page-5 Pulgar identity-bridge draft. |
| relevance_confidence | 0.95 | The draft, source packet, and chunk all target the same page-5 `Pulgar` mention. |
| canonical_readiness | hold_for_conversion_qa | Do not promote or attach until page-5 visual/provenance QA and a separate identity bridge review are complete. |

## Claim Probability Detail

| claim | disposition | probability | note |
| --- | --- | ---: | --- |
| Page 5 names a source-local person by surname `Pulgar` in the Vancouver preparation group | supported subject to QA | 0.76 | Literal chunk support is clear, but not visually checked. |
| Page-5 `Pulgar` is the same source-local person as same-source page-7 `Dario Pulgar` | hold | 0.67 | Plausible from source continuity; not literal on page 5 and page-7 metadata is also held. |
| Page 5 supports attachment to `Dario Arturo Pulgar` | hold/revise | 0.30 | Requires an accepted bridge beyond this page. |
| Page 5 supports attachment to canonical `Dario Arturo Pulgar-Smith` | hold/revise | 0.20 | No Smith/Pulgar-Smith or kinship evidence appears on page 5. |
| Page 5 supports merge with `Dario Jose Pulgar-Arriagada` or `Dario/Dario Pulgar Arriagada` | reject for now | 0.07 | Page 5 lacks the given names, maternal surname, occupation, chronology, and relationship details needed for this bridge. |
| Page 5 supports Jose/Juana parent-candidate relationships | reject | 0.02 | No parent or lineage statement appears. |

## Next Action

Keep the staged identity analysis on hold. The next action is conversion/provenance QA for page 5: restore or locate `page-0005.jpg`, reconcile the converted Markdown hash mismatch, and then visually check the `Pulgar` line. After that, run a focused same-source bridge review between page-5 `Pulgar` and proof-reviewed page-7 `Dario Pulgar`. Do not promote facts, merge people, or attach page-5 Vancouver participation to any canonical Pulgar profile or Jose/Juana relationship candidate from this draft.
