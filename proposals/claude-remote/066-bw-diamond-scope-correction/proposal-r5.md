# Proposal 066-bw-diamond-scope-correction, round 5

## Change list r4 -> r5

The r4 chain (F0-F10 in appH, F8 in bib) was never integrated; the manuscript has since moved. Round 5 re-anchors that chain to the current baselines and adds the two edits the gatekeeper required in review-r4.

| review-r4 finding | Severity | Action in r5 |
|---|---|---|
| F1. Free/Poisson: "Hence the charge is a vacuum modular Hamiltonian only where it coincides with one of …" asserts an unestablished necessity condition (implicitly, non-geometric massive diamond flow). Origin: gatekeeper's own r2 snippet. | major | **S1 applied verbatim** from review-r4 "Corrected snippet" (insertion of "known to be", with the review's re-wrap). |
| F2. General sector: "That matching has not been performed for higher-order, interacting, or fluctuating-Theta terms and is not a routine specialisation of the free-field result." implies the matching was performed in the quadratic sector, and calls a now-conditional statement a "result". (pre-existing text) | minor, required | **S2 applied verbatim** from review-r4 "Corrected snippet". |

- **F0-F10 and F8 are byte-identical to `apply_check_066_r4.py`.** Verified by line-for-line textual comparison of the constant blocks (helpers `L`/`c`, `SQ`/`TH`/`MAP`, `E1_HEAD`, `R2_TAIL`, `BASE_L30_34`, `E0`-`E8`, `NORM`, `B1_OLD/NEW`, `F9_OLD/NEW`, `F10_OLD/NEW`); only the baseline hashes and the r1-r3 chain records differ. Operationally, every F OLD now occurs exactly once in the *current* file (see Verification).
- **S1/S2 are byte-identical to review-r4.** `verbatim_check_066_r5.py` extracts the four fenced `latex` blocks under review-r4 "## Corrected snippet" and compares them to the constants used in the apply script: `VERBATIM CHECK PASS` (all four True; also `S1_OLD ==` junction of F1 NEW lines, `S2_OLD ==` F10 NEW last line + two baseline lines). An earlier throwaway inline check had reported False; that was a bug in the inline expected-string construction, not in the chain, and the persistent script supersedes it.
- **Re-anchoring to the drifted baseline.** The appH baseline moved from 624232 B / `c2dac013…` (r4 era) to the current 688007 B / `382389a4…`; bib from 29781 B / `28fdd7f8…` to 36133 B / `bd0d8a80…` (064/065/069-era integrations). Within Problem A the only drift is the new paragraph "Explicit Weyl data and per-order error in the flat Abelian class." at current L63-109 (added on the local lineage at commit 3452566); current L12-61 is byte-identical to the r4-era text, so **no OLD/NEW text changed** — only positions in the file. The r1-r3 chain hashes recorded in `apply_check_066_r4.py` cannot be reproduced from the current baseline and are *recorded but not re-derived* in the r5 script; they were not forced or paraphrased.
- Anchor positions in the current baseline (pre-patch): F0 L28; F1 L30-34; F2 L36; F7 L37-39; F9 L43-45; F10 L45-48; F3 L50; F6 L54; F4 L56-58; F5 L59-61; F8 in bib at L267. Mid-chain hit lines are in `apply_check_066_r5_output.txt` (F0@28 F1@31 F2@51 F3@67 F4@73 F5@77 F6@71 F7@54 F9@61 F10@65 S1@40 S2@71; F8@267).

## Result

The package result is unchanged from r1-r4 and was confirmed by the gatekeeper at r4 (M3, PRIOR-CLAIM-ERROR), provisional pending a full scan.
- appH L30-31 is a prior-claim error: BW is a wedge theorem (any Wightman mass); the geometric causal-diamond modular result is Hislop-Longo (CMP 84 (1982) 71-85, DOI 10.1007/BF01208372), for the free massless scalar only. The quoted lemma's sector contains the massive radial mode m_sigma.
- The K_0 Weyl-symbol identification, the half-sided-inclusion step, the cyclic/separating state and the O(R sqrt||deltaTheta||) estimates are marked as not derived; the General-sector diamond claim is conditional.
- r5 adds exactly the two gatekeeper-mandated substitutions: S1 removes the implicit non-geometricity/necessity claim; S2 states that the symbol matching has **not** been performed even in the quadratic sector and refers to the "free-field case" instead of a "result".

**The chain applies cleanly to the current baseline: ALL CHECKS PASS** (13/13 edits single-hit; no anchor failed; no OLD was forced or paraphrased). The r5-patched appH builds clean: 0 undefined, 0 multiply-defined, HislopLongo1982 in the .bbl, 398 pages.

## Target and status

Unchanged. Problem A (`sec:status-A`): verbatim from current appH L16-20 — "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. The general matrix-to-modular map remains unproved. A scope-limited Presentation-B model may retain Assumption~\ref{ass:dictionary} and claims no derivation from the matrix model." The ch17 entry (L377-392, `ass:dictionary`) carries the same status. Original target: the matrix-to-modular dictionary with Hilbert space, Weyl map, continuum limit and error control at each order in Theta. This package is a correction plus scoping of evidence; it derives nothing and **changes no label**.

## Source reading

digest + targeted reads. This is not a full scan; the full scan is a gatekeeper precondition this round (see Special instructions).
- `python scripts/make_digest.py --check` printed `DIGEST CURRENT`; digest appH hash matches the baseline used here.
- Read in full: review-r4.md; proposal-r1..r4.md; current Problem A L12-118 including the new Weyl paragraph L63-109 and the Missing-step paragraph L111-118; current L16-20 status lines; ch17-agenda L377-392 (Problem A item; status line L378 matches appH); appB `sec:appB-BW` (wedge statement, correct); bib BW entry region; `apply_check_066_r4.py` constant block; reports/ledger.md tail (L880-990).
- Files unreadable: none.

## Research and reasoning

No new mathematics in r5. The two carried edits are scoping corrections of the text only.

- **S1.** "is a vacuum modular Hamiltonian only where it coincides with one of these generators" is a necessity statement: any vacuum modular Hamiltonian must equal the wedge boost or the diamond conformal-Killing charge. Not established: for a massive diamond, H_D exists by general theory but no geometric form is known, and K_0 could equal it without matching either generator. "is known to be …" is the epistemic form consistent with "No such geometric identification is used here" (F1) and "not known to suffice" (F10).
- **S2.** After F0/F1 the Weyl-symbol identification of K_0 is "taken here" and not derived even in the quadratic sector; the Moyal-element reading of H_quad in fact gives a dilatation weighting (i/2) x.der h, not a boost/diamond charge (`moyal_K0_symbol_066.py`, r2). The old sentence's case-list therefore implied a completed quadratic matching. S2 removes that implication and de-reifies "the free-field result".
- **Interaction with the drifted Weyl paragraph (L63-109).** No edit touches it. It pins Weyl data in the flat Abelian constant-Theta class and per-order Moyal errors; it makes no modular/diamond identification claim, and its closing sentence explicitly disclaims deriving Assumption~\ref{ass:dictionary}. The S2 phrase "the Weyl-symbol identification above is not derived" points to F0's "is taken here …" sentence in the Free/Poisson paragraph, which is above the Weyl paragraph too — the pointer remains accurate either way; nothing in the paragraph is stale after the chain. Verified by the baseline->r5 diff: exactly two hunks, both in Problem A (F0/F1/S1/F2/F7 and F9/F10/S2/F3/F6/F4/F5); the Weyl paragraph and the Missing-step paragraph are untouched.

## Claim classification

As in r3/r4, with the S1/S2 effects:
- Established (correction): the L30-31 misattribution and over-stated range; BW = wedge (any mass); geometric diamond modular group = Hislop-Longo, free massless scalar.
- Conditional computation: under the Moyal-element reading of H_quad, K_0 carries the dilatation weighting.
- Unresolved, and now marked as such in text: the K_0 symbol identification (including the quadratic sector — S2); the half-sided-inclusion step; the state; the deltaTheta estimates; sufficiency of vector-field matching outside sectors with known geometric diamond modular flow.
- Not claimed: non-geometricity of massive diamond modular flow (S1 enforces this).
- Input/fit: none added. Conjecture: none added.

## Proposed changes

### `chapters/appH-microscopic-proofs.tex`

Apply to the current baseline, in this order (order is load-bearing: S1's OLD is the F1 NEW junction line; S2's OLD is the F10 NEW last line plus two baseline lines; F3 must precede S2 and F9 must precede F10):

F0, F1, F2, F3, F4, F5, F6, F7, F9, F10 — exactly the OLD/NEW pairs listed in proposal-r2.md (F0-F7), proposal-r3.md (F9) and proposal-r4.md (F10), byte-identical in `apply_check_066_r5.py` — then:

**S1** (Free/Poisson; replaces exactly the two quoted lines at current L29-30 region after F1; everything else in the paragraph stays). OLD (occurs once in the F-chain result):
```latex
mass \(m_\sigma\) of Section~\ref{sec:ch3-scales}. Hence the charge
is a vacuum modular Hamiltonian only where it coincides with one of
```
NEW:
```latex
mass \(m_\sigma\) of Section~\ref{sec:ch3-scales}. Hence the charge
is known to be a vacuum modular Hamiltonian only where it coincides
with one of
```

**S2** (General sector; replaces the three quoted lines at current L48-50 region after F10; the following "estimate, which is not derived here (in a norm not specified here)," line produced by F3 stays). OLD (occurs once in the F-chain result):
```latex
elsewhere that recovery is not known to suffice. That matching has
not been performed for higher-order, interacting, or fluctuating-\(\Theta\)
terms and is not a routine specialisation of the free-field result. The
```
NEW:
```latex
elsewhere that recovery is not known to suffice. That matching has
not been performed, even in the quadratic sector, where the Weyl-symbol
identification above is not derived; for higher-order, interacting, or
fluctuating-\(\Theta\) terms it would not be a routine specialisation of
the free-field case. The
```

S1/S2 OLD/NEW are verbatim from review-r4 "Corrected snippet" (verified by script, see below). No new `\ref` or `\cite` is added; labels used by the F chain were verified in earlier rounds (`sec:appB-BW`, `sec:ch3-scales`, `sec:status-A`, `ass:dictionary`), all unique in the digest label index.

**Final appH result:** 689657 bytes, sha256 `2cd28354af3486f5934b0f01674804746a8f90fddf648798ae16ed38d535b255`, CRLF = LF = 3763, bare LF = 0, no BOM. Cite counts: HislopLongo1982 = 1, BisognanoWichmann1976 = 1.

### `bib/namcg.bib`

F8 unchanged (adds the `HislopLongo1982` entry after the BW entry, anchor at current L267):
```bibtex
@article{HislopLongo1982,
  author  = {Hislop, Peter D. and Longo, Roberto},
  title   = {Modular Structure of the Local Algebras Associated with
             the Free Massless Scalar Field Theory},
  journal = {Communications in Mathematical Physics},
  volume  = {84},
  number  = {1},
  pages   = {71--85},
  year    = {1982},
  doi     = {10.1007/BF01208372}
}
```
(Record verified in r1: DOI arXiv-free Springer record; pages 71-85.)
**Final bib result:** 36511 bytes, sha256 `36931b9313266d619003b6a42af882dda2ab825d22551055cd124eb1527e2761`, CRLF = LF = 1209, bare LF = 0, no BOM.

Stale passages elsewhere: none found in targeted reads (appB `sec:appB-BW` states the wedge theorem correctly). A full scan must confirm.

## Verification scripts

All in this proposal folder; run with `python -I`.
- `apply_check_066_r5.py <repo_root> <out_dir_outside_repo>` — report-only; asserts out-dir outside repo; backslashes via `chr(92)`; checks both baselines (current values, plus r4-era values recorded only); applies F0-F7,F9,F10,S1,S2 (appH) and F8 (bib) with per-edit asserts OLD==1 before, NEW==0 before, NEW==1 after; failures print OLD/NEW bytes and context and are never forced; checks result sha256/size, CRLF==LF, no bare LF, no BOM, cite counts. Output: `apply_check_066_r5_output.txt` — **ALL CHECKS PASS**; patched copies written to a temp dir outside the repo (`/tmp/tmp.npxgfcsoBE/out066r5/`, msys path).
- `verbatim_check_066_r5.py <repo_root>` — compares the four S1/S2 constants to the review-r4 "Corrected snippet" fenced blocks and to the F1/F10 NEW line junctions. Output: `verbatim_check_066_r5_output.txt` — **VERBATIM CHECK PASS** (4/4 True; both junction asserts True).
- Scratch build (outside the repo, fresh dir `/tmp/tmp.91s1uqsQHn/build066r5`, only .tex/bib/figs copied, no stale aux/bbl): `scratch_build_066_r5_output.txt`. Hashes of the patched files confirmed inside the build copy. pdflatex -> bibtex -> pdflatex -> pdflatex, all exit 0; bibtex 0 warnings; final log: 0 "undefined", 0 "multiply"; `\bibitem[Hislop and Longo(1982)]{HislopLongo1982}` at bbl L86; **398 pages** (current manuscript; the r4-era 380 predates the 053-056/069 integrations). Build copy left in place (no rm -rf was run); it is outside the repository.
- Earlier-round scripts and outputs kept unchanged (r1-r4 apply checks, Moyal check, lattice illustration).

## Decisions Taken

- **Apply S1 and S2 verbatim from review-r4 rather than my r4 drafts.** The review's wraps/wording ("where the Weyl-symbol identification above is not derived", "free-field case") supersede my r4 proposed wording ("(see above)", "result"), per the review's own instruction; verbatim match is script-verified. Rejected: paraphrase.
- **Do not re-derive or force the r1-r3 chain hashes on the drifted baseline.** They are historical artifacts of the r4-era file; the r5 script records them without asserting reproducibility, and the direct F-chain single-hit asserts on the current file replace that role. Rejected: rewriting history or editing the old scripts.
- **Keep the whole F-chain re-applied on the current baseline as one package** (rather than only S1/S2 as a diff over the never-integrated r4 text): the integrator applies exactly the 12 appH + 1 bib OLD/NEW pairs to current sources, which is the smallest self-contained, verifiable unit.
- **Anchor text unchanged**: no OLD was re-worded; drift did not move any anchor text (byte-identical L12-61), so no re-anchoring paraphrase was needed.

## Milestone assessment

M3 carry-over: correction of a materially false prior claim (PRIOR-CLAIM-ERROR) in author-committed text (commit 6aa4490), confirmed by the gatekeeper at r1-r4, **provisional until the full scan**. r5 is the mechanical completion (two verbatim substitutions). Not a breakthrough; no new milestone trigger.

## Status-label recommendation

Current critical-path set re-derived from the manuscript (ch17 CRITICAL PATH entries at L123, L140, L330/344, L378, L395, L404, L475, L498; matching the ledger): A, B, C, D1, E, F, G-derived, N. **No label is affected by this package.** Problem A stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## Author decision needed

Only the carried report-only item: ch17 frames Problem A as the infrared dictionary while appH frames it as the "matrix-to-modular map" (definitional/scope mismatch). No edit is proposed here; recommendation from r1 stands (align appH wording with ch17, option (i)).

## Remaining open step

Unchanged (this package closes none of them):
1. Define H_quad and determine which charge K_0 equals (operator-level definition, then the symbol computation).
2. The half-sided-inclusion step in both sectors, with a specified cyclic and separating state.
3. The deltaTheta estimate in a specified norm.

Ranked avenues (carried from r4):
1. Wedge reformulation (BW applies directly, any mass).
2. Operator-level H_quad/K_0 via in-core forks (i) and (iii).
3. The IR theory below m_sigma.
4. Small-diamond error control.
5. Maxwell and fermion diamond results.

## Special instructions for the gatekeeper

- **A full scan is mandatory this round** before any plain ACCEPT or integration (CLAUDE.md 3(b): milestone verdict triggering a milestone digest — M3 — and 3(c): the package touches a status-adjacent passage; your r4 ruling said the same). Your r4 promise: "If r5 applies exactly S1 and S2, I will issue a plain ACCEPT conditional on the full scan."
- **Re-verify S1/S2 verbatim against review-r4.md "Corrected snippet"** (byte-exact, CRLF). You may re-run `verbatim_check_066_r5.py`; or extract the four blocks yourself.
- Re-run `apply_check_066_r5.py` report-only into your scratchpad; confirm baselines (appH 688007 B `382389a4…`; bib 36133 B `bd0d8a80…`) and that all 13 OLDs hit exactly once on the current file with no forced edits.
- Re-derive the central claims as in r1-r4 (BW wedge / Hislop-Longo massless-scalar diamond; the S1 necessity analysis; the S2 staleness).
- **Check the drifted paragraph** (appH L63-109 "Explicit Weyl data and per-order error in the flat Abelian class.") for interactions with F9/F10/S2 and for whether the drift made any other Problem A sentence stale. My assessment (targeted): none; it claims no modular/diamond identification and closes with an explicit non-derivation of `ass:dictionary`.
- **Integration ordinal: do not assert one.** The ledger's last logged integrated count is **63** (065, ledger L959/L977); L990 records that merges c7b9fa7..d8585c4 and local proposals 060R-068R have no ledger entries and that ledger/proposal numbering schemes collide; the orchestrator did not increment the count for 069. Historical ordinals ("Next … at 65", r2-r4's "64") are therefore unreliable; the earlier rounds' "Integration ordinal: 64" should not be carried.
- Must not be asserted in the final text: that massive diamond modular flow is non-geometric (S1 enforces); that the quadratic-sector matching was performed (S2 enforces); any closure of Problem A.
