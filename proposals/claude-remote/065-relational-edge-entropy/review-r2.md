VERDICT: ACCEPT | MILESTONE: none | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
Plain ACCEPT. The r2 insertion is byte-identical to the r1 insertion with all seven r1 findings (F1–F7, including the F3 snippet) applied verbatim, and nothing else changed. The apply-check hashes, placement, references and build all reproduce.

## Source reading
- **Mode:** digest plus targeted reads. No full scan was done.
- **Digest:** HEAD is eeb0a28 and `make_digest.py --check` printed `DIGEST CURRENT`.
- **Working tree:** the only modified file is `chapters/appH-microscopic-proofs.tex`, which still carries the uncommitted 064 change. Its sha256 is 7d15a3f2… and the bib is 1d280848…, so both baselines are unchanged from r1.
- **Read in full:**
  - `proposal-r2.md`: the changes table and Result. Sections 1–10 differ from r1 only by the matching corrections listed in the table.
  - `appH_insert.tex` (r2).
  - `appH_insert.r1.tex`.
  - `apply_r2_edits.out.txt`, `apply_check.r2.out.txt` and `build_r2.txt`.
- **Manuscript passages:** the passages read in r1 (appH sec:status-G and its surroundings, the ch17 G entries, ch12, ch03, ch04, ch06) have not changed since r1. The digest is current and appH has the same hash.
- **Scan ruling, same as r1:**
  - 3(a) does not apply: this is ordinal 63, and the next scan falls at 65.
  - 3(b) does not apply: there is no milestone.
  - 3(c) does not apply: this is one conditional paragraph next to the ledger section. No definition, assumption, scope statement or status text changes. The closing sentence restates the existing label.
  - Adding the first paragraph to sec:status-G does not change that section's scope.
- **055 process note:** it does not concern this package. `git status` shows nothing modified under `proposals/`.

## Claim under review
- **Claim:** unchanged from r1. Exact lemmas on a compact fuzzy factor for the relational block entropy of 2408.05274, a Poisson-limit inequality and scalar-proxy numerics. The conclusion is a bounded, conditional no-go: the construction is not the density of ass:Sent-density, and the state, l_c and the frame subgroup are supplied inputs.
- **Target:** G-derived.
- **Appendix H Ledger label (verbatim):** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope results: G-model and G-external support at most a scope-limited model; G remains OPEN and neither satisfies the matrix-derived criterion."
- **ch17 (verbatim):** "CRITICAL PATH; mechanism CLOSED CONDITIONALLY, derivation OPEN."

## Checks performed
- **Independent diff check:**
  - I wrote my own script in the scratchpad: `C:\Users\redgi\AppData\Local\Temp\claude\3ba14ee056ac155d\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\gk065r2\exp.py`.
  - It starts from `appH_insert.r1.tex` (sha256 09adefe9…, the file reviewed in r1) and applies exactly the r1 replacement texts. Those are F1a/b, F2, F4, F5a/b, F6, F7a/b, plus the F3 snippet replacing "For two separated caps" through "the form of Assumption~\ref{ass:Sent-density}.".
  - The result is IDENTICAL to r2 `appH_insert.tex` (9627 B, sha256 11e2d9eb…b5f8). So every finding is applied verbatim and no other byte changed.
- **Re-verification of each r1 finding in the r2 text:**
  - F1: x^a is defined as the symbol of X^a, and φ is the flow of the symbol of n·J. Fixed.
  - F2: the two-cap union is restricted to the coaxial caps, with the band width taken in the n·J eigenbasis. Fixed.
  - F3: the fixed-frame statement, the one-sided estimate without the factor 2, the note that two-sided diagrams are not computed, the weakened counterterm sentence and the "(conditional)" conclusion are all present. Fixed.
  - F4: the frame subgroup is now listed as an input. Fixed.
  - F5: "positive and integrable" and the Lorentzian sentence are present. Fixed.
  - F6: the ⟨ℓ²⟩=4s²W wording is present. Fixed.
  - F7: "squared norm" and "polynomial diagram" are present. Fixed.
  - No new mathematics was introduced, and the r1 derivations and script outputs still stand. s1–s5 were re-run byte-identical in r1, and the researcher states that no script changed.
- **apply_check:**
  - Re-run in report mode into `C:\Users\redgi\AppData\Local\Temp\claude\3ba14ee056ac155d\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\gk065r2apply`: APPLY CHECK PASS.
  - Baselines: 614579 B / 7d15a3f2… and 29360 B / 1d280848….
  - Anchor: occurs exactly once, at L2868, with the insertion after L2869 (before `\section{Problem H…}`).
  - Resulting appH: 624232 B, sha256 c2dac013f275fed851d53e8086bc3eceef717c5b607b10c09ae7541c43558b5c, 3378 CRLF, 0 bare LF.
  - Resulting bib: 29781 B, 28fdd7f8cb62b2ad23da3cc05d819a0b750f7fdec096511fca60ab02135ea64d, 994 CRLF, 0 bare LF. This is unchanged from r1.
  - I hashed both output files myself and they match.
  - References: all 8 labels exist exactly once, there are no new labels, both cites resolve, and no process language was found.
  - My stdout matches `apply_check.r2.out.txt`, apart from the output-directory line.
  - The repository was unchanged after the run.
- **Build:**
  - `build_r2.txt` reports PASS at 380 pages, with 0 undefined and 0 multiply defined references.
  - It also reports 24 overfull boxes, equal to the baseline, and 0 bibtex warnings.
  - I did not rebuild it myself.
- **`apply_r2_edits.py`:** it writes only `appH_insert.tex` in the proposal folder. That is the researcher's own deliverable, not a write elsewhere in the repository.
- **Literature:** no change since r1, so the r1 verification of 2408.05274, Crossref and the 2303.08012 abstract stands.

## Findings
none (blocking/major/minor).

One non-blocking observation, which does not affect the manuscript text:
- In `proposal-r2.md`, Result item 4 still says "It is also not additive over two separated caps" without saying that this holds at a fixed frame.
- The integrated LaTeX states it correctly, so no action is required for integration.

## Scope of what is established
Unchanged from review-r1, and the integrated text now matches it.
- **Exact at finite N:**
  - Lemma 1 (edge identity).
  - Lemma 2: the rank-one block and s²=¼M(N−M)(σ₁²+σ₂²).
  - Lemma 3: the charge spectrum, and the union for coaxial caps with banded momenta.
  - The Schur row sums.
  - The rank derivative for a polynomial diagram.
- **Poisson limit (kinematic, X=AJ):** P ≤ 2√2πs, with equality iff σ₁=σ₂.
- **Numerical, scalar proxy:** the coefficient of (3.14) is reproduced, and the power of l_c differs between the two states.
- **Conditional on the imported leading-order saddle of 2408.05274:**
  - fixed-frame non-additivity;
  - "not of the form of ass:Sent-density".
- **Inputs:** the state, l_c and the frame subgroup.
- **Unresolved:**
  - the map from s to eq:g-from-e (A, D1);
  - the sector mismatch.
- **Not derived:** no S_ent on ∂M, no eq:bdy-EE, no Λ_eff.
- **Labels:** G remains OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL, and no label change is proposed.
- **What the no-go covers:** a compact internal factor with positive contraction, a fixed-frame single projector or coaxial cap pair, leading order with one dominant irrep, Gaussian proxy states and the FFHS block algebra.
- **Open avenues, ranked as in r1:**
  1. A spacetime-block subsystem (a 4D region × fibre, with a 3D edge).
  2. A within-core state via OS reconstruction on the fibre modes.
  3. An alternative subsystem algebra, or a first-law or mutual-information test of the M-dependence.
  4. A stationary non-symmetric background with the state response.
  5. Tying l_c and p to scales of the integral.
  6. The 2303.08012 vacuum term.
- **Milestone:** none. M2 is not met: the excluded class is not a route the manuscript keeps open, and the replica route of ass:Sent-density is untouched.
- **Discrepancy noted in r1, still open for the author:** sec:status-G has no "Missing step" paragraph, and the ch12 dimensional gap in eq:Leff is not recorded there.

## Recommended disposition
Integrate as-is:
- the r2 `appH_insert.tex`, converted to CRLF and placed after "scope-limited model." in sec:status-G, giving appH sha256 c2dac013…;
- the bib entry FlissFrenkelHartnollSoni2025, giving bib sha256 28fdd7f8….

## Corrected snippet
None required.

VERDICT: ACCEPT | MILESTONE: none | FLAGS: none | PROGRESS: improving | OPEN: 0/0
