---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260530161131773
task_id: "identity-analysis:research/_staging/conflicts/chunk-ff8bc4b91301-p0005-01-pulgar-identity-bridge-hold-postconv-evidence-extraction-20260530154508254.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-ff8bc4b91301-p0005-01-pulgar-identity-bridge-hold-postconv-evidence-extraction-20260530154508254.md"
subject: "Pulgar (source-local surname-only Habitat page 5 person)"
source_packet: "research/_staging/source-packets/chunk-ff8bc4b91301-p0005-01-habitat-revisited-pulgar-vancouver-hold-postconv-evidence-extraction-20260530154508254.md"
source: "raw/sources/Habitat Revisited, Jim Carney, 2006.pdf"
converted_file: "raw/converted/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11.codex.md"
chunk: "raw/chunks/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-page-7cd35b519c/page-0005-chunk-01.md"
chunk_id: "CHUNK-ff8bc4b91301-P0005-01"
page_reference: "page 5"
analysis_status: hold_for_conversion_qa_and_identity_bridge
canonical_readiness: hold
promotion_recommendation: do_not_promote_from_conflict_note
---

# Identity/Conflict Analysis: Habitat Page-5 Surname-Only Pulgar

## Blockers First

1. Exact staged draft analyzed: `research/_staging/conflicts/chunk-ff8bc4b91301-p0005-01-pulgar-identity-bridge-hold-postconv-evidence-extraction-20260530154508254.md`.
2. Page 5 names only `Pulgar`; it does not state a forename, `Dario`, `Arturo`, `Jose`, `Arriagada`, `Smith`, parentage, spouse, child, birth, death, or explicit family relationship.
3. Conversion/provenance QA is blocked: the staged packet reports live converted-file and chunk-file SHA mismatches, and the referenced page-5 image was missing during revision. No visual proofing was possible for this pass.
4. The later page-5 sentences `We arrived in Vancouver on May 19` and `our makeshift offices in the Begg building` are group/pronoun-chain context only; they do not repeat `Pulgar`.
5. Existing local context preserves separate Pulgar-line candidates: canonical `Dario Arturo Pulgar-Smith`, staged/source-local `Dario Pulgar`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, adult and child `Dario Pulgar` passenger stubs, and Jose/Juana parent candidates. Page 5 does not merge them.
6. No external research was performed. Raw sources, converted Markdown, chunks, source packets, reviewed notes, and canonical wiki pages were not edited.

## Literal Evidence Reviewed

From the staged page-5 source packet and assigned chunk:

```text
By the late spring of 1976 it was decided a small group of us, including Pulgar ,
Gyborg, Jane Weiner, and Barbara Janes (later NFB's Director of English Produc-
tion) and myself, would go to Vancouver to help get the show, as I put it, "on the
air".
```

Also from the same page:

```text
We arrived in Vancouver on May 19. The Conference was to begin on May 31.
```

```text
The following three weeks in our makeshift offices in the Begg building I remember
only as a blur, where night was indistinguishable from day and specific events
merged into one continuing effort.
```

Literal reading: page 5 names a surname-only `Pulgar` among a small group selected in late spring 1976 to go to Vancouver for Habitat audiovisual presentation work.

Interpretation kept separate: the group context makes it plausible that this `Pulgar` is the same person as another same-source Habitat `Dario Pulgar` mention, but page 5 itself does not prove the forename or any canonical family identity.

## Hypotheses And Scores

### H1: Page-local surname-only `Pulgar` in the Vancouver preparation group

Supporting evidence:

- Page 5 directly names `Pulgar` in a list with Gyborg, Jane Weiner, Barbara Janes, and the author.
- The local context places the group in late spring 1976 Habitat audiovisual preparation work and Vancouver travel logistics.
- No other `Pulgar` person appears on page 5.

Conflicts and limits:

- The page image was missing during revision and SHA mismatches block promotion.
- Surname-only evidence cannot establish a unique person across the Pulgar line.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.70 | Strong for a page-local surname-only person, pending conversion QA. |
| conflict_severity | 0.28 | Low internal conflict; higher downstream risk if over-attached. |
| evidence_quality | 0.52 | Direct text mention but surname-only and unverified against image. |
| conversion_confidence | 0.20 | Blocked by missing page image and SHA mismatches. |
| claim_probability | 0.66 | Probable narrow reading that page 5 names `Pulgar`. |
| relevance | 1.00 | Directly addresses the assigned staged draft. |
| canonical_readiness | 0.05 | Hold; do not promote or attach canonically. |

### H2: Same as same-source page-7 `Dario Pulgar`

Supporting evidence:

- A separate staged Habitat page-7 note/source packet names `Dario Pulgar` as a UN Habitat Secretariat confrere, a dynamic Chilean, and a person connected to Vision Habitat after the 1976 conference.
- Page 5 lists `Pulgar` among people going to Vancouver; page 7 gives a fuller same-source Habitat identity cluster for `Dario Pulgar`.
- The page-5 list includes Gyborg, and page 7 is in the same memoir/document context.

Conflicts and limits:

- Page 5 does not repeat `Dario`, and page 7 evidence has its own converted-file hash mismatch.
- Same-source continuity is a bridge lead, not proof of canonical identity or family relationship.
- Page 7 still does not state `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, parents, spouse, or descendants.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.56 | Plausible same-source bridge, not yet proof-reviewed. |
| conflict_severity | 0.44 | Moderate risk if page-5 surname-only evidence is used as a full-name claim. |
| evidence_quality | 0.50 | Nearby same-source context is useful but conversion-sensitive. |
| conversion_confidence | 0.28 | Both page-5 and page-7 promotion are blocked or limited by QA issues. |
| claim_probability | 0.52 | More likely than not as a working hypothesis, not promotable. |
| relevance | 0.95 | Required comparison for the staged draft. |
| canonical_readiness | 0.04 | Requires targeted conversion QA and proof review first. |

### H3: Same as canonical `Dario Arturo Pulgar-Smith`

Supporting evidence:

- Canonical `wiki/people/dario-arturo-pulgar-smith.md` is the family-supplied maternal-grandfather profile and explicitly calls for identity review before attaching records mentioning Dario, Pulgar, Pulgar-Arriagada, or Pulgar-Smith.
- The broad surname `Pulgar` overlaps with the canonical page.

Conflicts and limits:

- Page 5 does not state `Dario`, `Arturo`, `Smith`, `Pulgar-Smith`, Alexander John Heinz, maternal grandfather, or any family relationship.
- The only canonical proof for Pulgar-Smith currently cited is family-supplied knowledge, not this Habitat page.
- Attaching page 5 by surname alone would violate the canonical page's identity-review warning.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.08 | Shared surname only. |
| conflict_severity | 0.82 | High risk of false merge into the family-supplied canonical profile. |
| evidence_quality | 0.30 | Relevant family context exists separately, but page 5 gives no bridge identifiers. |
| conversion_confidence | 0.20 | Conversion blocker remains unresolved. |
| claim_probability | 0.06 | Not supported from page 5 alone. |
| relevance | 0.92 | Required Pulgar-Smith anti-conflation check. |
| canonical_readiness | 0.00 | Do not attach to Pulgar-Smith. |

### H4: Same as staged `Dario Arturo Pulgar`

Supporting evidence:

- Local staged research tasks preserve a `Dario Arturo Pulgar` CV/employment cluster as a comparison target.
- The broad `Pulgar` surname and possible same broad career/research domain make this worth later bridge review.

Conflicts and limits:

- Page 5 does not state `Dario Arturo` or cite a CV.
- Existing CV notes require proof review for document attribution and page alignment before promotion.
- No chronology, occupation continuity, residence, signature, or family relationship links page 5 to the CV subject.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.10 | Name overlap is incomplete and indirect. |
| conflict_severity | 0.72 | Premature attachment could collapse separate Dario/Pulgar clusters. |
| evidence_quality | 0.32 | The relevant CV evidence is separate and proof-review pending. |
| conversion_confidence | 0.25 | Page 5 and CV bridge both require QA/proof review. |
| claim_probability | 0.08 | Not proved by page 5. |
| relevance | 0.82 | Required Pulgar-line comparison. |
| canonical_readiness | 0.00 | Do not attach to CV subject. |

### H5: Same as `Dario Jose Pulgar-Arriagada` or `Dario/Dario Pulgar Arriagada`

Supporting evidence:

- Local staged and canonical context contains `Dario Jose Pulgar-Arriagada`, `Dario Pulgar-Arriagada`, and `Darío Pulgar Arriagada` clusters.
- The page-5 surname `Pulgar` is compatible with the surname portion of these candidates.

Conflicts and limits:

- Page 5 does not state `Jose`, `Arriagada`, a hyphenated surname, medical title, legal notice, birth record, or property context.
- Existing Pulgar-Arriagada clusters carry separate proof-review and chronology cautions, including possible early official/medical listings, a 2000 legal/expropriation stub, and disputed birth-register readings.
- A surname-only Habitat mention cannot distinguish a Pulgar-Arriagada candidate from other Pulgar persons.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.07 | Surname-only overlap; no forename or maternal surname. |
| conflict_severity | 0.80 | High risk of conflating different generations or public-record clusters. |
| evidence_quality | 0.28 | Candidate evidence is separate and cannot bridge this page. |
| conversion_confidence | 0.20 | Page-5 QA is blocked. |
| claim_probability | 0.05 | Unsupported from this page. |
| relevance | 0.88 | Required Pulgar-Arriagada comparison. |
| canonical_readiness | 0.00 | Do not merge or attach. |

### H6: Related to Jose/Juana parent candidates

Supporting evidence:

- Existing local context includes Jose/Juana parent candidates: `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.
- Pulgar-line surname overlap makes these candidates worth preserving for future lineage review.

Conflicts and limits:

- Page 5 names no Jose and no Juana.
- Page 5 states no parent, spouse, child, sibling, household, descendant, or birth relationship.
- Related register clusters have their own conversion/proof-review issues, including row-control, child-name, mother-name, and father-suffix uncertainty.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_or_relationship_confidence | 0.02 | No relationship evidence on page 5. |
| conflict_severity | 0.78 | Unsupported parent/lineage attachment would create a serious relationship conflict. |
| evidence_quality | 0.24 | Parent-candidate evidence is separate and QA-sensitive. |
| conversion_confidence | 0.20 | Page-5 and register-related QA are unresolved. |
| claim_probability | 0.01 | No Jose/Juana relationship is supported here. |
| relevance | 0.72 | Required Pulgar-line checklist item. |
| canonical_readiness | 0.00 | No relationship promotion. |

## Conflict Findings

- Same-person evidence: supported only for a page-local surname-only `Pulgar` in the page-5 Vancouver preparation group.
- Duplicate-person evidence: unresolved. Do not merge page-5 `Pulgar` with same-source `Dario Pulgar`, `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, or passenger/legal-register clusters by name alone.
- Name-variant evidence: page 5 supports only `Pulgar`. It does not prove `Dario`, `Dario Arturo`, `Dario Jose`, `Pulgar-Arriagada`, `Pulgar-Smith`, or any Jose/Juana-derived family name.
- Relationship-conflict evidence: none on page 5. No parent, spouse, child, or descendant relationship is stated.
- Chronology-conflict evidence: page 5 gives a late spring 1976/Vancouver Habitat context, but no age or vital data. Cross-cluster chronology must be reviewed before comparing it with birth-register, passenger, CV, official-listing, legal-notice, or canonical family-supplied clusters.
- Conversion-confidence conflict: the staged extraction is blocked by missing image and SHA mismatches, so no canonical promotion should happen from this page.

## Ranked Conclusion

| Rank | Candidate or interpretation | Probability | Current disposition |
| ---: | --- | ---: | --- |
| 1 | Page-local surname-only `Pulgar` in the Habitat Vancouver preparation group | 0.66 | Hold for conversion QA; no canonical attachment. |
| 2 | Same as same-source Habitat page-7 `Dario Pulgar` | 0.52 | Plausible bridge hypothesis; requires targeted visual/proof review across pages 5 and 7. |
| 3 | Same as staged `Dario Arturo Pulgar` | 0.08 | Unsupported; preserve only as a later bridge-review target. |
| 4 | Same as canonical `Dario Arturo Pulgar-Smith` | 0.06 | Unsupported from page 5; do not attach. |
| 5 | Same as `Dario Jose Pulgar-Arriagada` / `Dario/Dario Pulgar Arriagada` | 0.05 | Surname-only overlap; do not merge. |
| 6 | Jose/Juana parent or relationship candidate | 0.01 | No relationship evidence; no action. |

## Recommended Next Action

Keep the staged conflict draft as a surname-only identity-bridge hold. Do not promote page-5 facts, do not merge any person, and do not attach this page to a canonical Pulgar profile.

Exact next proof-review step: first resolve conversion/provenance QA for `CHUNK-ff8bc4b91301-P0005-01` by reconciling the live converted-file and chunk-file SHA mismatches and restoring or regenerating the rendered page image at `raw/codex-conversion-jobs/cafbbc662e-habitat-revisited-jim-ca-p0001-0011-habitat-revisited-jim-carney-2006-pages-1-11/page-images/page-0005.jpg`. Then visually verify the page-5 `Pulgar` reading.

After page-5 QA passes, run a targeted identity-bridge proof review comparing the verified page-5 surname-only `Pulgar` with the same-source page-7 `Dario Pulgar` cluster. Only after that should any separate bridge review compare the resulting page-local Habitat person against `Dario Arturo Pulgar`, canonical `Dario Arturo Pulgar-Smith`, `Dario Jose Pulgar-Arriagada`, `Dario/Dario Pulgar Arriagada`, or Jose/Juana parent candidates using direct identifiers such as full name, age, dates, occupation continuity, residence, parents, spouse, children, or source provenance.
