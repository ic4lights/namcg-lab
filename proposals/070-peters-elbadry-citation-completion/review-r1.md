# review-r1 — 070-peters-elbadry-citation-completion

NOTE ON PROVENANCE: the gatekeeper subagent delivered this review via its handback message; it did not
write the file itself (same write-path limitation seen in the 2026-11-13 vector-miner run). The orchestrator
persisted the handback text verbatim below, minus the handback framing lines. The approved literal E1/E2
text below is identical to proposal-r1.md.

VERDICT: ACCEPT | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/0

## Verdict
Independent Crossref re-verification of both Peters records, in-tree hash/anchor/grep verification, and an independent re-derivation of the ch14 ratio chain all pass; E1/E2 are a minimal, accurate citation-completion fix, and the E3 hold-out is the correct call (not an omission).

## Source reading
digest + targeted reads. `python scripts/make_digest.py --check` printed `DIGEST CURRENT` at HEAD e033b1b; working tree clean except the untracked proposal folder (066/069 integrations already author-committed, so tree == HEAD for chapters/ and bib/). Targeted reads: `chapters/ch14-dissipation.tex` L210-270; `chapters/appI-gaia-wide.tex` L1-54 (L1,4,32-35,47-48,80); `bib/namcg.bib` tail and key survey (114 entries); `reports/ledger.md` 063 and 066 entries; repo-wide greps on every touched string. Full scan not performed and not required: no definition/assumption/scope/status change (3(c) not triggered), digest current (3(d) not triggered), no milestone verdict (3(b) not triggered). Trigger 3(a) (every 5th integrated item) is indeterminate because the ledger's integrated count is unreconciled (ledger line 990/997 records this discrepancy for the author); content-wise a full scan adds nothing for a citation-only package.

## Claim under review
Citation-completion package for the uncited "Peters--Mathews power" attribution at ch14:226-227; E3 El-Badry cite deliberately held out. No Problem object; no status/priority/completion label touched or implied. Status: N/A (not a critical-path problem).

## Checks performed
Directly verified:
1. Crossref fetched by me (not the researcher's excerpt):
   - 10.1103/physrev.131.435: Peters, P. C. & Mathews, J., "Gravitational Radiation from Point Masses in a Keplerian Orbit", Physical Review **131**, 435-440, issued 1963-07-01, ISSN 0031-899X. Matches the proposed `PetersMathews1963` entry exactly (entry omits issue "1" — acceptable, standard practice).
   - 10.1103/physrev.136.b1224: Peters, P. C., "Gravitational Radiation and the Motion of Two Point Masses", Physical Review **136** issue **4B**, **B1224-B1232**, issued 1964-11-23. Matches the proposed `Peters1964` entry exactly.
2. Pre-edit hashes/sizes: `chapters/ch14-dissipation.tex` 17336 B sha256 b1fefa68...976dd2 (equals ledger 063 post-integration hash, ledger L887); `bib/namcg.bib` 36511 B sha256 36931b93...2761 (equals ledger 066 post-integration hash, ledger L996). All three touched files CRLF, ASCII, no BOM.
3. Anchor: OLD two-line block matches ch14:226-227 exactly and is single-hit ("the Peters--Mathews power" occurs once; "Isaacson flux of the tensor block" once).
4. Grep claims: bib/ contains no Peters key (only "Mem. Acad. St. Petersbourg", bib:39); no `\cite{Peters...` anywhere in chapters/; no El-Badry bib key; `bib/namcg.bib` has 114 entries, zero duplicate keys, proposed keys absent (no collision); bib tail entry is `FlissFrenkelHartnollSoni2025` ending `}\r\n`, entry style (`doi` field, `author  = {...}`) matches proposed entries.
5. Independent re-derivation (sympy, plus hand algebra): from eq:Peters `P_GW=(32/5)G_eff mu^2 d^4 Omega^6` and eq:Pent `P_ent=eta mu v^2/d^4` with `v^2=G_eff M/d`, `Omega^2=G_eff M/d^3`: P_GW=(32/5)G^4 mu^2 M^3 d^-5, P_ent=eta mu G M d^-5, ratio = 5 eta/(32 G^3 M^2 mu) — exactly eq:ratio, both powers d^-5. The (32/5) orbit-averaged quadrupole form is the standard Peters-1964 circular-orbit content (c absorbed into G_eff, a pre-existing unit convention), so citing Peters is consistent with what eq:Peters claims. Also verified the d^{4-n} generalization in the following paragraph is algebraically consistent.
6. E3 hold-out verified independently: Crossref 10.1093/mnras/stab323 = El-Badry, Rix & Heintz, "A million binaries from Gaia eDR3...", MNRAS 506, 2269-2295, issued 2021-02-09 — title explicitly eDR3. My own Crossref bibliographic search ("El-Badry wide binaries Gaia DR3") surfaced no El-Badry DR3-era catalogue paper. Citing the 2021 paper against "Gaia DR3" text would be a release-mismatched provenance attribution; hold-out is correct.

Not verified (not needed for verdict): equation-level content of the Peters papers (record-level only, as the proposal itself states); La Piana & Morsella record (report-only, no edit); the unused ApJ 138 (1963) 470 record (correctly excluded as unverified).

## Findings
1. Severity minor; proposal L14-15 ("only externally-named formula in the section without a citation"). The same sentence names "Isaacson flux", also uncited — no Isaacson bib key exists and ch14-dissipation.tex contains zero `\cite` commands (Isaacson named at ch11:55,406-407 and ch14:226). Charitably read (eq:Peters is the section's only externally *attributed displayed formula*), the claim holds; E1/E2 are still correct and self-contained. The Isaacson citation gap is recorded as an open follow-up for the researcher to package separately; it does not gate this package.
2. Severity minor; proposal L86 ("no other passage pins the data release"). Literally inaccurate: "Gaia DR3" naming also appears at appI-gaia-wide.tex L1 (chapter title), L4, L80 and ch18-epilogue.tex:49. This does not change the E3 verdict (hold-out correct), but it matters for the author's option (i): changing appI:32 alone to "eDR3" would leave the chapter title, intro, conclusion and ch18 inconsistent. Any future E3 fix must touch all five sites coherently.
3. Severity info; ledger 063/066 hash cross-records match the live tree exactly; digest current; no stale integrated-count assertion made.

No blocking or major findings.

## Scope of what is established
Established: E1/E2 complete a genuinely missing attribution with two Crossref-verified primary records; label hygiene clean; the cited convention matches the displayed equation. Conditional/open (unchanged by this package): equation-vs-paper content match remains the manuscript's existing claim at record level only; E3 remains OPEN for the author among the proposal's three options (I recommend option (i) only if applied across all five DR3-naming sites, since no El-Badry DR3-era catalogue record could not be found [sic: "could be found"]). BisognanoWichmann1976 page-range completeness (bib shows "303") and La Piana & Morsella remain report-only author items.

## Recommended disposition
Integrate E1 and E2 exactly as submitted. E3: do not edit (author decision, with finding-2 scope note). Side notes stay report-only.

## Corrected snippet
No revision needed. Approved literal E1 NEW (two lines, CRLF, replacing ch14:226-227):

    The Isaacson flux of the tensor block for a weak, slow binary is
    the Peters--Mathews power~\cite{PetersMathews1963,Peters1964}

Approved literal E2 (append after `FlissFrenkelHartnollSoni2025` closing brace, blank-line-separated, CRLF, matching file style):

    @article{PetersMathews1963,
      author  = {Peters, P. C. and Mathews, J.},
      title   = {Gravitational Radiation from Point Masses in a {Keplerian} Orbit},
      journal = {Physical Review},
      volume  = {131},
      pages   = {435--440},
      year    = {1963},
      doi     = {10.1103/physrev.131.435}
    }

    @article{Peters1964,
      author  = {Peters, P. C.},
      title   = {Gravitational Radiation and the Motion of Two Point Masses},
      journal = {Physical Review},
      volume  = {136},
      number  = {4B},
      pages   = {B1224--B1232},
      year    = {1964},
      doi     = {10.1103/physrev.136.b1224}
    }

Post-integration gate as proposed: build_check PASS, bibtex resolves both keys, 0 undefined/multiply-defined, CRLF preserved.
