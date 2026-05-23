---
type: identity_conflict_analysis
role: identity_researcher
task_id: identity-analysis:research/_staging/identity/id-stage-chunk-3f469b56e502-p0003-01-administrative-name-mentions.md
worker: postconv-identity-analysis-20260523102909357
staged_draft: research/_staging/identity/id-stage-chunk-3f469b56e502-p0003-01-administrative-name-mentions.md
source_path: raw/sources/R3578-50-5569-5569-Jacket5.pdf
source_packet: research/_staging/source-packets/sp-stage-chunk-3f469b56e502-p0003-01-league-of-nations-routing-slip.md
converted_file: raw/converted/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25.codex.md
chunk: raw/chunks/ca09a98281-r3578-50-5569-5569-jacke-p0001-0025-r3578-50-5569-5569-jacket5-pages-1-25-codex/page-0003-chunk-01.md
chunk_id: CHUNK-3f469b56e502-P0003-01
page_reference: page 3
analysis_status: administrative_names_only
canonical_readiness: do_not_promote
---

# Identity/Conflict Analysis: Administrative Name Mentions, CHUNK-3f469b56e502-P0003-01

## Blockers

- Exact staged draft reviewed: `research/_staging/identity/id-stage-chunk-3f469b56e502-p0003-01-administrative-name-mentions.md`.
- The source page is a League of Nations archival file cover/routing slip. It records file classification, subject text, routing recipients, and routing dates; it is not a family-history record.
- The named entries `Teixidor`, `Walters`, `Dufour`, `Pantaleoni`, `Poulet`, `Menciatry`, `Dufourhey`, `Pietromarchi`, and `Paulucci` appear only in the `Transmis a / Referred to` circulation table.
- No literal source reading states a vital event, residence, kinship, household membership, family relationship, or genealogical identity for any named routing recipient.
- Several routing-table readings remain conversion-sensitive. The source packet and conversion review preserve QA concerns for uncertain names such as `Poulet` and `Menciatry`, an illegible date, struck-through entries, and row-level date disagreements.
- A `wiki` search found no canonical wiki person pages matching the administrative names in this staged draft. Name-only mentions in other converted archival files are not enough to merge or create people.
- No external research was performed. No raw sources, converted Markdown, chunks, source packets, or canonical wiki pages were edited.
- The requested `$genealogy-proof-review` skill file was not available in this session. This note follows the evidence contract used by local proof-review notes: literal evidence first, interpretation separate, uncertainty preserved, scored readiness, and no promotion without proof review.

## Hypothesis 1: Administrative Routing Mentions Only

Hypothesis: The staged draft correctly treats the listed names as administrative routing recipients, not genealogical identity candidates.

Literal evidence:

- The staged draft classifies the item as `administrative_name_mentions` and recommends `do_not_promote`.
- The assigned chunk describes the page as a pre-printed routing slip or file cover with fields for `Expediteur`, `Date`, `Sujet`, and a table headed `Transmis a / Referred to`.
- The source packet states that the page has source-context relevance only and does not state vital events, kinship, household membership, or family relationships.
- The source packet says names in the circulation table appear to be administrative routing recipients or departments.
- The reviewed conversion note supports the endpoint dates `I M. Teixidor | 31.8.29` and `M. Paulucci ... | 2.4.31`, while keeping row-level transcription QA open.

Interpretation:

- This is the strongest hypothesis. The page can support narrow archival/source-context claims after conversion QA, but it cannot support a same-person conclusion, duplicate-person merge, name-variant assertion, relationship claim, or genealogical chronology claim.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.08 | Names likely refer to real administrative recipients, but the page supplies no genealogical identity facts. |
| conflict_severity | 0.03 | No direct same-person, duplicate-person, relationship, or chronology conflict appears. |
| evidence_quality | 0.76 | The staged draft, chunk, source packet, and reviews agree on the administrative source context. |
| conversion_confidence | 0.62 | Page purpose and major entries are readable; several names/dates remain QA-sensitive. |
| claim_probability | 0.93 | Highly probable that these are administrative routing mentions only. |
| relevance | 0.12 | Low genealogical relevance; useful mainly as negative identity evidence. |
| canonical_readiness | 0.00 | Do not promote to canonical person or relationship pages. |

## Hypothesis 2: Some Routing Names Are Name Variants Of Known Persons

Hypothesis: The routing names may be variants or duplicate references for known people elsewhere in the workspace.

Literal evidence:

- The assigned source gives only surname-style or courtesy-title readings: `M. Teixidor`, `M. Walters`, `M. Dufour`, `M. Pantaleoni`, `Mlle Poulet`, `M. Menciatry`, `M. Dufourhey`, `M. Pietromarchi`, and `M. Paulucci`.
- The source gives no full name, age, birthplace, family role, address, occupation beyond institutional routing, or relationship.
- Local `wiki` search returned no canonical person pages matching these administrative names.
- Other converted archival files contain some repeated administrative names, especially `Walters`, `Dufour`, `Pietromarchi`, and `Paulucci`, but those are also institutional records and do not bridge these page-3 routing entries to genealogical subjects.

Interpretation:

- The duplicate/name-variant hypothesis remains weak. Repeated surnames in League of Nations routing contexts may be useful for institutional source metadata, but same-person or variant conclusions require a later reviewed source with identity-bearing details.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.18 | Repeated institutional surnames suggest possible real officials, not proved genealogy identities. |
| conflict_severity | 0.10 | Main risk is false attachment or duplicate noise if promoted by name alone. |
| evidence_quality | 0.38 | Evidence is name-only and some readings are uncertain. |
| conversion_confidence | 0.52 | Stable for some surnames, weaker for `Poulet`, `Menciatry`, and row details. |
| claim_probability | 0.16 | Low probability that this page alone proves a known-person variant. |
| relevance | 0.06 | Minimal direct relevance to the family-history wiki. |
| canonical_readiness | 0.00 | Do not create, merge, rename, or attach canonical people from this evidence. |

## Hypothesis 3: Conversion Uncertainty Creates An Identity Conflict

Hypothesis: Uncertain readings such as `Poulet`, `Menciatry`, date discrepancies, and struck-through entries create an identity or chronology conflict.

Literal evidence:

- The assigned chunk flags `Poulet` as a best-effort reading and `Menciatry` as uncertain.
- The source packet records that the right-column `Health S` date may differ from the converted transcript, and that the `Social S` date may be closer to `7.10.29` than `[?]7.9.29`.
- The conversion review note says these disagreements block detailed row-by-row circulation chronology, not the narrow endpoint-date claim.

Interpretation:

- These are conversion and administrative-routing QA issues. They do not become genealogical identity, relationship, or chronology conflicts unless a later proof-reviewed claim tries to attach one of these readings to a person profile.

Scores:

| score | value | rationale |
|---|---:|---|
| identity_confidence | 0.05 | No identity-bearing claim depends on the uncertain readings. |
| conflict_severity | 0.18 | Moderate for source-metadata precision; low for genealogy identity. |
| evidence_quality | 0.54 | QA notes are specific, but the disputed data are not genealogical facts. |
| conversion_confidence | 0.45 | Table details need targeted review before detailed administrative chronology use. |
| claim_probability | 0.22 | Possible source-metadata conflict, not a person-identity conflict. |
| relevance | 0.20 | Relevant to conversion QA and proof-review gating only. |
| canonical_readiness | 0.00 | Hold routing-table detail; do not promote person facts. |

## Pulgar-Line Anti-Conflation Check

The staged draft and referenced page do not mention Dario Arturo Pulgar-Smith, Dario Arturo Pulgar, Dario Jose Pulgar-Arriagada, Dario/Dario Pulgar Arriagada, Jose del Carmen Pulgar, Jose del Carmen Segundo Pulgar Arriagada, Juana Arriagada de Pulgar, or Juana de Dios Amagada de Pulgar.

Ranked Pulgar hypotheses for this staged draft:

| rank | hypothesis | probability | action |
|---:|---|---:|---|
| 1 | This League of Nations routing slip is unrelated to Pulgar-line identity clusters. | 0.99 | No Pulgar merge, attachment, or promotion from this draft. |
| 2 | The page indirectly supports Dario Arturo Pulgar or Dario Arturo Pulgar-Smith. | 0.01 | Reject unless a later reviewed source explicitly links this League file to that person. |
| 3 | The page supports Dario Jose Pulgar-Arriagada or Dario/Dario Pulgar Arriagada. | 0.01 | Reject for this draft; preserve those clusters in separate Pulgar proof reviews. |
| 4 | The page supports Jose/Juana parent candidates. | 0.00 | Reject; no Jose/Juana parent names or relationships appear here. |

Exact next Pulgar proof-review step needed: none for this staged draft. Pulgar-line work should continue only in source packets, identity drafts, and canonical candidates that actually name those people.

## Conflicts

- Same-person conflict: none supported by this staged draft.
- Duplicate-person conflict: none supported by this staged draft.
- Name-variant conflict: none supported by this staged draft.
- Relationship conflict: none supported by this staged draft.
- Chronology conflict: none supported by this staged draft for genealogical persons.
- Conversion conflict: table-level administrative routing QA remains open; it does not justify a genealogy identity claim.

## Recommended Next Action

Complete this identity-analysis task as `do_not_promote`. Keep the staged identity draft as negative identity evidence for administrative names only. Do not create canonical people for Teixidor, Walters, Dufour, Pantaleoni, Poulet, Menciatry, Dufourhey, Pietromarchi, or Paulucci from this page; do not merge them with any existing person by name alone; and do not attach Pulgar-line or Jose/Juana facts. Any future use of this page should be limited to source-context or routing metadata after targeted conversion QA.
