---
type: identity_conflict_analysis
role: identity_researcher
task_id: "identity-analysis:research/_staging/conflicts/chunk-e756c7880c5d-p0011-01-page-and-name-variant-watch.md"
worker: postconv-identity-analysis-20260523222603019
staged_draft: "research/_staging/conflicts/chunk-e756c7880c5d-p0011-01-page-and-name-variant-watch.md"
subject: "Dr Dario Pulgar A. / Dr Dario Pulgara"
source_packet: "research/_staging/source-packets/chunk-e756c7880c5d-p0011-01-el-aguila-fundo-los-cuartos-dario-pulgar-a.md"
source: "raw/sources/El Aguila Nombre Grande Scan.pdf"
converted_file: "raw/converted/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18.codex.md"
chunk: "raw/chunks/ca51f62b28-el-aguila-nombre-grande-p0004-0018-el-aguila-nombre-grande-scan-pages-4-18-codex/page-0011-chunk-01.md"
chunk_id: "CHUNK-e756c7880c5d-P0011-01"
analysis_status: hold_for_conversion_qa_and_identity_bridge
canonical_readiness: hold
---

# Identity/Conflict Analysis: e756c7880c5d Page And Name Variant Watch

## Blockers First

- The exact staged draft reviewed here is `research/_staging/conflicts/chunk-e756c7880c5d-p0011-01-page-and-name-variant-watch.md`.
- The assigned draft/chunk is page-11 scoped, but its staged source packet says the body is printed page 14 and matches the Fundo Los Cuartos article. The local `raw/chunks/.../page-0011-chunk-01.md` currently reads a different page about electricity and milk processing with no Dario mention.
- The only available local page image in the relevant conversion job directory is `page-0004.jpg`; page images for page 11 or page 14 are absent in this checkout. A related proof review for the page-14 identity analysis reports that a page image was checked elsewhere and supports the typed `DR DARIO PULGAR A,` line, but this e756 task still has a provenance/page-reference blocker.
- The staged e756 packet transcribes the typed article as `DR DARIO PULGAR A,` and the handwritten signature as `DR. DARIO PULGARA`. A related page-14 analysis/proof-review cautions that the handwritten note is lower-confidence and appears closer to `Dr. Dario Pulgar A` than `JR. DARIO PULGARA`; it must not be used to create a separate `Pulgara` identity.
- The source does not name Dario's parents, spouse, children, birth date, death date, `Arturo`, `Smith`, `Jose`, or a full `Arriagada` surname.
- No external research was performed. No raw sources, converted Markdown, chunks, source packets, staged conflict drafts, or canonical wiki pages were edited.

## Literal Evidence

From the staged source packet for this draft:

```text
EL FUNDO LOS CUARTOS PERTENECE COMO YA SE SABE AL DR DARIO PULGAR A,
DISTINGUIDO FACULTATIVO DE CONCEPCION QUIEN HEREDO DE SUS PADRES ESTE
FUNDO ALLA POR EL AÑO 1917
```

The same e756 packet records:

```text
[handwritten signature] DR. DARIO PULGARA [/handwritten signature]
```

Interpretation kept separate: `A.` may be a final initial, a spacing issue, or an abbreviation for a second surname such as Arriagada. The current staged draft does not prove any expansion, and the page-reference mismatch blocks canonical use.

## Hypotheses And Scores

| rank | hypothesis | supporting evidence | conflicts/limits | probability | identity confidence | conflict severity | evidence quality | conversion confidence | relevance | canonical readiness |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | This is primarily a page-reference/conversion QA blocker. | e756 draft says assigned page 11, body page 14; local page-0011 chunk is a different page; page-14 derivatives carry the Dario article. | Missing page-11/page-14 images in this checkout; e756 chunk id and current chunk content do not align cleanly. | 0.90 | 0.12 | 0.82 | 0.64 | 0.38 | 1.00 | 0.01 |
| 2 | Held narrow person candidate `Dr Dario Pulgar A.` owner/physician of Fundo Los Cuartos. | Typed article names `DR DARIO PULGAR A,`, calls him a distinguished physician of Concepcion, and says he inherited the fundo from unnamed parents around 1917. Related proof review supports the typed name line. | Single periodical item; provenance mismatch; no full name, vital data, named parents, or bridge source. | 0.82 | 0.74 | 0.30 | 0.68 | 0.66 | 0.98 | 0.16 |
| 3 | Same older medical cluster as 1928 `Dario Pulgar A.` and/or 1953 adult `Dario Pulgar`. | Name/initial and physician/medical context align; 1928 passenger row has `Dario Pulgar A.` medical surgeon age 39; 1953 adult row has `Dario Pulgar` age 64 and medical context. | No source in this draft gives age, travel context, full surname, or direct bridge. 1953 list also has a separate child Dario who must remain distinct. | 0.52 | 0.56 | 0.66 | 0.56 | 0.50 | 0.92 | 0.08 |
| 4 | Same as `Dario Jose Pulgar-Arriagada` / `Dario J. Pulgar Arriagada`. | `A.` could mean Arriagada, and medical/professional context is compatible with some older Pulgar-Arriagada staging. | This draft does not state `Jose`, `J.`, or `Arriagada`; photograph/title contexts are metadata-sensitive; signature cannot prove expansion. | 0.31 | 0.35 | 0.74 | 0.44 | 0.42 | 0.88 | 0.04 |
| 5 | Same as canonical `Darío Pulgar Arriagada`. | Shared `Dario/Darío Pulgar` and possible `A.`/Arriagada lead; canonical stub has a 2000 Chiguayante expropriation mention. | No age, occupation, Fundo Los Cuartos, or identity bridge on the canonical stub; older medical chronology could conflict with a 2000 legal-notice person. | 0.13 | 0.16 | 0.84 | 0.48 | 0.54 | 0.82 | 0.02 |
| 6 | Same as `Dario Arturo Pulgar` / `Dario Arturo Pulgar-Smith`. | Shared `Dario Pulgar`; canonical Pulgar-Smith page is the family-supplied maternal-grandfather anchor and warns against unreviewed attachment. | This source lacks `Arturo`, `Smith`, `Pulgar-Smith`, Alexander John Heinz, CV/work-history context, or family bridge. `A.` is not proof of `Arturo`. | 0.10 | 0.14 | 0.78 | 0.40 | 0.48 | 0.90 | 0.01 |
| 7 | Jose/Juana parent candidates are the unnamed parents. | Article says Dario inherited the fundo from `sus padres`; wiki/staging has Jose/Juana Pulgar-line candidates. | The article names no parent; Jose/Juana clusters have their own conversion/proof-review cautions; surname context is not relationship evidence. | 0.04 | 0.06 | 0.68 | 0.34 | 0.36 | 0.70 | 0.00 |

## Conflicts

- Page-reference conflict: high. The e756 task is page-11 scoped, but the useful Dario article evidence belongs to the page-14 derivative cluster.
- Name-variant conflict: medium-high. Literal typed support is `Dario Pulgar A.`; `Pulgara` is a low-confidence or spacing-sensitive handwritten/signature reading and should not be normalized silently.
- Same-person conflict: unresolved. The safest person conclusion is only a held `Dr Dario Pulgar A.` candidate.
- Duplicate-person risk: high if this source is merged into `Dario Arturo Pulgar-Smith`, `Dario Arturo Pulgar`, `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, or passenger-list Dario clusters by name alone.
- Relationship-conflict evidence: limited to unnamed parents. No Jose/Juana named-parent relationship is supported.
- Chronology-conflict evidence: older physician/property context is more compatible with an older medical Dario cluster than the later CV/Pulgar-Smith cluster, but that is only an interpretive lead.

## Recommended Next Action

Keep `research/_staging/conflicts/chunk-e756c7880c5d-p0011-01-page-and-name-variant-watch.md` on hold as a conversion QA and identity-bridge caution. Do not promote as a canonical conflict, merge people, rename pages, expand `A.` to `Arriagada` or `Arturo`, create a `Pulgara` person, or attach named Jose/Juana parents.

The exact next proof-review step is provenance QA for `CHUNK-e756c7880c5d-P0011-01`: reconcile why the assigned page-11 chunk/source packet points to the page-14 Fundo Los Cuartos article, restore or locate the relevant page image, and confirm the source reading as `DR DARIO PULGAR A,` versus any signature variant. After that, run a targeted identity-bridge proof review comparing the confirmed reading first to older medical Dario candidates, then separately to `Dario Jose Pulgar-Arriagada`, `Dario/Darío Pulgar Arriagada`, `Dario Arturo Pulgar`, `Dario Arturo Pulgar-Smith`, and Jose/Juana parent candidates.
