---
type: identity_conflict_analysis
status: draft
role: identity_researcher
worker: postconv-identity-analysis-20260529214638613
task_id: "identity-analysis:research/_staging/conflicts/chunk-5bfd003c83f8-p0142-01-no-identity-conflict-detected.md"
staged_conflict_draft: "research/_staging/conflicts/chunk-5bfd003c83f8-p0142-01-no-identity-conflict-detected.md"
subject: "Dario Pulgar-Arriagada"
source_packet: "research/_staging/source-packets/chunk-5bfd003c83f8-p0142-01-r3578-jacket5-dutch-chile-dario-pulgar-arriagada.md"
source: "raw/sources/R3578-50-5569-5569-Jacket5.pdf"
converted_file: "raw/converted/ca09a98281-r3578-50-5569-5569-jacke-p0126-0150-r3578-50-5569-5569-jacket5-pages-126-150.codex.md"
chunk: "raw/chunks/ca09a98281-r3578-50-5569-5569-jacke-p0126-0150-r3578-50-5569-5569-jacket5-pages-126-150-codex/page-0142-chunk-01.md"
chunk_id: "CHUNK-5bfd003c83f8-P0142-01"
page_reference: "source page 142; printed page number 78; document page number 514"
analysis_status: hold_for_conversion_qa_and_identity_bridge
canonical_readiness: hold
---

# Identity/Conflict Analysis: Dario Pulgar-Arriagada Dutch Chile Listing

## Blockers First

- Exact staged conflict draft analyzed: `research/_staging/conflicts/chunk-5bfd003c83f8-p0142-01-no-identity-conflict-detected.md`.
- The assigned page has medium conversion confidence only. The chunk was produced by PDF text-layer fallback after a Docling baseline error, has `rough_ok` readability status, and explicitly requires page-image comparison before research extraction.
- Page 142 names only `den Heer Dario Pulgar-Arriagada` in the Chile delegation/listing context. It gives no age, birth date, spouse, child, parent, residence, signature, or family relationship.
- The medical-service title is line-broken as `Genees- / kundigen Dienst`; normalize only after proof review confirms the rendered page.
- Existing local context contains separate or unresolved Pulgar-line clusters: `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario J. Pulgar Arriagada`, `Dario/Darío Pulgar Arriagada`, adult and child `Dario Pulgar` passenger entries, and Jose/Juana parent candidates. This page does not merge them.
- No external research was performed. No raw sources, converted Markdown, chunks, source packets, reviewed notes, or canonical wiki pages were edited.

## Literal Evidence Reviewed

From the staged source packet and assigned chunk:

```text
De President van de Republiek Chili:
den Heer Guillermo Novoa-Sepulveda, Ivolonel, Militair Attach^
bij het Gezantschap van Chili te Berlijn,
den Heer Dario Pulgar-Arriagada, Kapitein
van den
Genees-
kundigen Dienst;
```

Literal reading: the page lists `Dario Pulgar-Arriagada` under the President of the Republic of Chile and gives him a captain title in the medical/health service. Interpretation kept separate: this supports only a page-local official-listing identity and title after conversion QA, not a family relationship or same-person merge.

## Hypothesis 1: Page-Local Dario Pulgar-Arriagada, Medical-Service Captain

Supporting evidence:

- The page literally names `den Heer Dario Pulgar-Arriagada`.
- The title immediately following the name is `Kapitein van den Genees- / kundigen Dienst`.
- No other `Dario`, `Pulgar`, or `Arriagada` person appears on this page, so the staged draft's no intra-chunk identity conflict finding is supported.

Conflicts and limits:

- The conversion requires page-image comparison before promotion.
- The page does not provide enough identifiers to connect the name to a birth, death, family, property, passenger, CV, or later legal-notice cluster.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.82 | Strong for the page-local named official, pending page-image QA. |
| conflict_severity | 0.18 | No direct internal conflict; risk comes from later over-attachment. |
| evidence_quality | 0.68 | Direct listing text, but single page and limited identifiers. |
| conversion_confidence | 0.55 | Medium due to PDF text-layer fallback and required image comparison. |
| claim_probability | 0.80 | Probable narrow claim that the page names Dario Pulgar-Arriagada with this title. |
| relevance | 1.00 | Directly answers the assigned staged conflict draft. |
| canonical_readiness | 0.28 | Hold until conversion QA and proof review. |

## Hypothesis 2: Same As Dario J. Pulgar Arriagada Or Dario Jose Pulgar-Arriagada

Supporting evidence:

- The exact surname combination `Pulgar-Arriagada` overlaps with staged `Dario J. Pulgar Arriagada` and `Dario Jose Pulgar-Arriagada` clusters.
- The medical-service title is compatible with local medical-title comparison tasks for Pulgar-Arriagada identities.

Conflicts and limits:

- Page 142 does not state `J.`, `Jose`, birth data, or a professional degree.
- Some related ICRC/photo and medical-title contexts are metadata-dependent or separately held for proof review.
- Name plus medical context is a useful bridge-review lead, not same-person proof.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.48 | Surname and medical context are suggestive but incomplete. |
| conflict_severity | 0.58 | Premature merge could collapse distinct Pulgar-Arriagada clusters. |
| evidence_quality | 0.54 | Assigned page is direct for its own name; bridge evidence is separate. |
| conversion_confidence | 0.50 | Both assigned and compared clusters require careful proof review. |
| claim_probability | 0.42 | Plausible, not proved. |
| relevance | 0.92 | Required Pulgar-line comparison. |
| canonical_readiness | 0.08 | Do not merge or promote as same person. |

## Hypothesis 3: Same As Dario/Darío Pulgar Arriagada Legal-Notice Stub

Supporting evidence:

- Existing canonical `wiki/people/dar-o-pulgar-arriagada.md` records a `Darío Pulgar Arriagada` expropriation/legal-notice cluster.
- The visible name form differs only by accent/hyphen/spacing from `Dario Pulgar-Arriagada`.

Conflicts and limits:

- The legal-notice event is dated 2000-12-05, while this official listing appears in a historical diplomatic/convention context with no date on page 142.
- Page 142 provides no age, property, Chiguayante, legal-notice, or residence bridge.
- If this page belongs to an early twentieth-century medical-service official, a direct merge into a 2000 apparent-domain holder requires vital-date proof.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.22 | Name overlap only, with major chronology caution. |
| conflict_severity | 0.72 | High risk of conflating generations or inherited property/name clusters. |
| evidence_quality | 0.50 | Both clusters have local evidence, but no bridge. |
| conversion_confidence | 0.60 | Legal-notice conversion is stronger than this page; both still need scoped review. |
| claim_probability | 0.16 | Low without age or continuity evidence. |
| relevance | 0.82 | Required anti-conflation check. |
| canonical_readiness | 0.03 | Do not attach to the legal-notice stub from this page. |

## Hypothesis 4: Same As Dario Arturo Pulgar Or Canonical Dario Arturo Pulgar-Smith

Supporting evidence:

- All forms share `Dario` and `Pulgar`.
- Canonical `wiki/people/dario-arturo-pulgar-smith.md` is the family-supplied maternal-grandfather page and is an important Pulgar-line comparison target.
- Staged CV material preserves a document-level `Dario Arturo Pulgar` cluster.

Conflicts and limits:

- Page 142 does not state `Arturo`, `Smith`, `Pulgar-Smith`, Alexander John Heinz, or any descendant relationship.
- Existing CV proof-review notes already hold `Dario Arturo Pulgar` pending an identity bridge to canonical `Dario Arturo Pulgar-Smith`.
- The assigned page's `Pulgar-Arriagada` name form is not a silent variant of `Pulgar-Smith` or `Arturo`.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.10 | Shared given name/surname only; no bridge terms. |
| conflict_severity | 0.78 | High duplicate-person and family-attachment risk if merged by name alone. |
| evidence_quality | 0.46 | Good family context exists separately, but this page does not connect to it. |
| conversion_confidence | 0.55 | Conversion confidence does not solve the identity bridge. |
| claim_probability | 0.08 | Not supported from this page. |
| relevance | 0.90 | Required Pulgar-Smith anti-conflation check. |
| canonical_readiness | 0.00 | Do not attach to Pulgar-Smith or CV subject. |

## Hypothesis 5: Same As Adult Or Child Dario Pulgar Passenger Entries

Supporting evidence:

- Existing canonical stubs preserve two 1953 passenger-list entries named `Dario Pulgar`: adult age 64 and child age 11.
- The adult passenger's occupation/calling is staged as medical, making the adult row a possible medical-cluster comparison.

Conflicts and limits:

- Page 142 does not state passenger status, age, 1953, Dorothy, student, or travel-party context.
- It does not state the adult passenger's plain `Dario Pulgar` form or the child passenger's possible CV chronology.
- The child passenger is chronologically incompatible with an early medical-service captain if this page is from an earlier convention-era official list; exact source date still needs proof review.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_confidence | 0.34 adult; 0.03 child | Adult medical context is possible; child fit is unsupported. |
| conflict_severity | 0.66 | Same-name passenger merges carry high chronology and relationship risk. |
| evidence_quality | 0.50 | Passenger evidence is local and useful but unbridged to this page. |
| conversion_confidence | 0.56 | Assigned page is medium; passenger row basics are separately reviewed with caveats. |
| claim_probability | 0.28 adult; 0.02 child | Adult comparison is a lead only; child comparison should remain rejected for this page. |
| relevance | 0.78 | Required Dario Pulgar duplicate-person check. |
| canonical_readiness | 0.04 | No merge or attachment supported. |

## Hypothesis 6: Jose/Juana Parent Candidates Connect To This Dario Pulgar-Arriagada

Supporting evidence:

- Existing local context includes `Jose del Carmen Pulgar`, `Jose del Carmen Segundo Pulgar Arriagada`, `Juana Arriagada de Pulgar`, and `Juana de Dios Amagada de Pulgar`.
- Pulgar/Arriagada surname overlap makes these candidates worth preserving for future lineage review.

Conflicts and limits:

- Page 142 names no Jose, no Juana, and no parent, spouse, child, sibling, or household relationship.
- The Jose/Juana materials carry separate conversion and proof-review cautions, including father-field suffix and row-control issues.
- Family-context hints justify a double-check later; they do not support named parent assignment here.

| Metric | Score | Rationale |
| --- | ---: | --- |
| identity_or_relationship_confidence | 0.05 | No direct relationship evidence on the assigned page. |
| conflict_severity | 0.74 | Unsupported named-parent attachment would create serious relationship conflict. |
| evidence_quality | 0.36 | Parent-candidate evidence is separate and conversion-sensitive. |
| conversion_confidence | 0.40 | Related register clusters have unresolved QA issues. |
| claim_probability | 0.04 | No Jose/Juana relationship is supported by this page. |
| relevance | 0.70 | Required Pulgar-line checklist item. |
| canonical_readiness | 0.00 | No relationship promotion. |

## Conflict Summary

- Same-person conflict: none within the assigned page; unresolved across all external Pulgar clusters.
- Duplicate-person risk: high if `Dario Pulgar-Arriagada` is merged with `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, passenger `Dario Pulgar` entries, or the 2000 `Darío Pulgar Arriagada` stub by name alone.
- Name-variant evidence: page 142 supports only `Dario Pulgar-Arriagada`; it does not prove `Dario Arturo`, `Pulgar-Smith`, `Dario Jose`, `Dario J.`, or plain `Dario Pulgar`.
- Relationship-conflict evidence: none on page 142. No Jose/Juana parent, spouse, child, or descendant relationship is stated.
- Chronology-conflict evidence: no internal chronology appears on page 142. Cross-cluster chronology must be reviewed before comparing this medical-service official with 1918 medical-title, 1928/1953 passenger, 2000 legal-notice, or CV work-history clusters.
- Conversion-confidence conflict: the family-relevant name is clear in the text layer, but canonical use is blocked until page-image QA confirms name, title, and reading order.

## Ranked Hypotheses

| Rank | Candidate or interpretation | Probability | Required next step |
| ---: | --- | ---: | --- |
| 1 | Page-local `Dario Pulgar-Arriagada`, medical-service captain | 0.80 | Page-image conversion QA, then proof review for narrow official-listing/title claim. |
| 2 | Same as `Dario J. Pulgar Arriagada` / `Dario Jose Pulgar-Arriagada` | 0.42 | Targeted medical-title identity bridge comparing full name, title, date, and source context. |
| 3 | Same as adult passenger `Dario Pulgar`, medical, age 64 in 1953 | 0.28 | Compare only after both sources have proof-reviewed dates, ages, and occupation readings. |
| 4 | Same as `Dario/Darío Pulgar Arriagada` legal-notice stub | 0.16 | Require vital-date or property/identity continuity evidence before any merge. |
| 5 | Same as `Dario Arturo Pulgar` / canonical `Dario Arturo Pulgar-Smith` | 0.08 | Require explicit reviewed bridge from `Pulgar-Arriagada` to `Arturo` or `Pulgar-Smith`. |
| 6 | Related to Jose/Juana parent candidates | 0.04 | No action; revisit only if a relationship-bearing source names parents or kin. |
| 7 | Same as child passenger `Dario Pulgar`, age 11 in 1953 | 0.02 | Treat as unsupported for this page; do not merge. |

## Recommended Next Action

Keep the staged conflict draft as a narrow no-intra-chunk-conflict finding. Do not promote or attach it canonically yet.

Exact next proof-review step: first run targeted conversion QA against the rendered page image for `CHUNK-5bfd003c83f8-P0142-01` to confirm the name `Dario Pulgar-Arriagada`, the line-broken title `Kapitein van den Genees-/kundigen Dienst`, and the Chile listing context. If confirmed, proof review may promote only a narrow page-local claim that Dario Pulgar-Arriagada was listed as a Chilean medical-service captain in this official convention/diplomatic text.

The next identity bridge, after that proof review, should compare this confirmed medical-service title against proof-reviewed `Dario J. Pulgar Arriagada`, `Dario Jose Pulgar-Arriagada`, and adult medical-passenger evidence. Preserve `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, the 2000 `Darío Pulgar Arriagada` legal-notice stub, and all Jose/Juana parent candidates as separate hypotheses until a source supplies explicit identity or relationship evidence.
