VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M3 | FLAGS: PRIOR-CLAIM-ERROR | PROGRESS: first | OPEN: 0/3

PROGRESS: first (round 1). OPEN: 0 blocking / 3 major / 5 minor.

## Verdict

The core result is sound and the prior-claim error is real, but three statements in the insert are not supported as written, so it cannot be integrated yet. The exact cubic Hessian `H_V^K = chi^2(L^2 - kappa S.L)`, `kappa = 2 - c/chi`, the lost second-order cancellation and `V/T -> kappa^2/4` all re-derive. The three problems are: regulated numbers taken from a truncated formula outside its range, a `beta_K` relation said to "stand" beyond the merged scope, and an unqualified "not a one-loop stationary point".

## Source reading

**Digest + targeted reads + corpus-wide grep. The full scan was not done.**

- `make_digest.py --check` printed `DIGEST CURRENT` (head 20741cb, dirty-chapters: no, 30 files). The proposal cites head 54a2dcb; chapters are unchanged between the two.
- Read in full: appH L1660-1689 (F ledger and missing step), L2668-2852 (all product-background and fuzzy-factor paragraphs through the anchor); ch17 L370-509; ch03 L139-186 (`eq:Smatrix`, `def:matrix-coords-ext`); the adversary report; the ledger tail; `MILESTONE.md`; the proposal, the insert and scripts s1-s3 and `apply_check.py`.
- Grep over all `chapters/*.tex` for the cubic term, `C_{\mu\nu\lambda}`, fuzzy sphere, `beta_K` and the example values. The only hits outside L2793-2848 are ch03 L140/161/181 and appH L655, L897; none is made stale by the insert.
- `proposals/049-k-scale-dilaton-response/review-r4.md` was grepped for the cubic and Hessian lines only, not read in full.
- No file was unreadable.
- **Protocol 3(b):** I rule M3 on the mathematics, but I have not read every file in the manifest (about 1.04 MB, of which appH is 624 KB). This verdict is not an ACCEPT, so it triggers no integration. The full scan remains mandatory at the round that issues ACCEPT, as in the 066 precedent recorded in the ledger. Do not treat this review as satisfying 3(b).

## Claim under review

**Claim.** With the cubic term of `eq:Smatrix` read on `K = S^2_N` (`C_ijk = i c eps_ijk/g^2`), the Feynman-gauge operator of the three vector components along K is `chi^2(L^2 - kappa S.L)`. Consequently:
- the merged cubic and mass forms of `beta_K` (L2810), the example at `x = 3/10` (L2824) and "V = T ... does not need a tuned K" (L2844) hold only for the `c = mu = 0` operators;
- on the cubic branch `Uhat` is log divergent, `V/T = (1 - r_c)^2`, and V = T with no negative mode is impossible for `c != 0`;
- the chi exchange adds `q_*^2|_chi = (beta_K L'/4U_4) q_b^2 <= 0`.

**Original target.** Edge `F.t-nonderivative-sector` (049 review-r4 avenue 1): the second-order non-derivative sector of t. That is not delivered, and the proposal says so.

**Current labels, unchanged by this package.**
- Problem F (appH L1669-1672, verbatim): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating \(G_{\mathrm{eff}}\) as an input leaves F OPEN and does not satisfy the matrix-derived criterion."
- ch17 L404: "CRITICAL PATH; OPEN. The conditional heat-kernel identity does not compute the physical coupling."
- Problem C (digest L435-436, line truncated there): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. A scalar-tensor result is a reduced-scope ..."
- Problem N (digest L3243-3244): "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL."

## Checks performed

**Reproduction pack.** s1-s4 and `apply_check.py` were re-run; every output is identical to the saved file (s1 worst residual 7.82e-14, PASS; apply_check 17 PASS, sha 5b4340bf...). `s1_cubic_hessian.py` and its output are tracked in commit 20741cb, which is why they do not show as untracked (researcher's note 9).

**Independent derivations (by hand).**
- Normalisation: `(1/3!) Tr(C_ijk [X^i,X^j] X^k)` with `C = i c eps/g^2` gives `(ic/3g^2) eps tr XXX`. Agrees.
- Hessian: the Yang-Mills flux term is `-tr(F_ij [a_i,a_j]) = -i chi^2 eps tr(J_k [a_i,a_j])`; the cubic second variation is `+(i c chi/2) eps tr(J_k [a_i,a_j])`. So `2 chi^2 -> 2 chi^2 - c chi` and `kappa = 2 - c/chi`. The gauge-mode check (`kappa = 0` at `c = 2 chi`) agrees.
- Spectrum and multiplicities from `S.L = l, -1, -(l+1)`. No negative mode exactly for `-1 <= kappa <= 2`; the mode `l = 1, j = 0` is `-2 chi^2` at `kappa = -2`.
- Second moment: `tr(S.L)^2 = 2 sum (2l+1) l(l+1) = N^2(N^2-1)`, so `sum w lambda^2 = (kappa^2 - 4) chi^4 N^2 (N^2-1)`.
- `Vhat -> kappa^2 N^2`, hence `V/T = kappa^2/4`, `W_R = -T r_c(2 - r_c)`. At `r_c = 1`: `c_T = T/3`, `W_R/6 - 2W_X = T/12`, consistent with merged L2755.
- Incomplete-gamma expansion behind the `mathcal U` formula.
- Tree-curve algebra: `1 - r_c = -L'/4Utilde`, `beta_K = 2(r_c-1)/(4-3r_c+delta)`, `r_c = (6+delta)/5`, `2/(delta-2)`.
- Example: `r_c = (3/4)(12.36/7.935) = 1.168`, `kappa = -0.336`, `V/T = 0.0283`, `varrho = 23.9`.
- `q_*^2|_chi`: with the phase average, `-(beta_K L'/4) sigma_1^2 -> M = -beta_K L'/16m^4`, `q_*^2 = 2ML = -beta_K L' L/8m^4`; and `-U_4 L/2m^4` reproduces the merged `q_b^2 = 12 Uhat chi^2/m^2(Vhat + 2That)`. The normalisation is consistent.
- Helicity ±2 vacuum moment: `(1/15)(2 a^2 tr D^2)/2`, with `c.c = a tr D^2`. Agrees.

**Own script** (`C:\Users\redgi\AppData\Local\Temp\claude\3ba14ee056ac155d\8445fbac-1820-4671-b227-7d272a39e1df\scratchpad\gk_check.py`, independent code).
- Moments are exact; `V/T` at N = 64, 512 matches `kappa^2/4`.
- It evaluates the regulated integral exactly as `eps^-2 sum w E_3(eps lambda)` and compares with the truncated closed form. This produced finding F1.

**Anchor and bytes.**
- `\section{Problem G: HBEV}` occurs once (appH L2850), preceded by `...PROGRAMME-CONDITIONAL.\r\n\r\n`.
- appH is CRLF throughout (3378/3378), no BOM. The insert is ASCII, LF only, and ends `.\n\n`; `\n -> \r\n` gives a correct block.
- `bib/namcg.bib` is CRLF; `new_bib_entry.bib` is LF and must also be converted.
- No collision with 067 (text anchor at the end of sec:status-G, before `\section{Problem H...}` at L2896) or 070 (end of sec:status-B). The anchors are textual, so the integration order does not matter.

**LaTeX.** The insert compiles standalone in the scratchpad (book + amsmath/amssymb, exit 0; only the expected undefined refs and cite). The repository build was not run because it writes. The five labels each exist once; there is no new label; the key `IsoKimuraTanakaWakatsuki2001` is absent from the bib.

**Literature.**
- arXiv hep-th/0101102 fetched: title, Nucl. Phys. B604 (2001) 121-147 and DOI match. The abstract says "Chern-Simons term is added in the matrix model to make the fuzzy sphere as a classical solution of the model", which supports the one attributed statement.
- Authors' full first names: not independently verified (the record gives initials).
- Hartnoll-Liu 2409.18706, Imai et al. and Dine-Seiberg are not cited in the insert and were not checked.

**F6.** No "decides" wording. The one-loop/tree ratios (-1, 0.168, -0.32, no tree part) are stated and reproduce.

**Emergence.** Not affected; nothing is made fundamental.

## Findings

**F1. Major. Insert, "Weights with the Hessian" and "Correction"; proposal items 2, 4, 7 and gatekeeper note 4.**
- Finding: the sign statement "negative for `s_Lambda chi^2 N^2 <= 0.9` ... (it vanishes at 0.926, N = 512)" and the values "27.5 at N = 16 and 441 at N = 64" come from the closed form with the `O(s_Lambda)` remainder dropped. At those cutoffs `s_Lambda lambda_max` is of order one, so the remainder is not small.
- Evidence: exact evaluation of the stated integral gives, per `N^4` at `kappa = -0.3365`, N = 512:

  | `s_Lambda chi^2 N^2` | exact | truncated |
  |---|---|---|
  | 0.9 | -1.05 | -0.055 |
  | 0.5 | -1.79 | -1.20 |
  | 0.1 | -4.45 | -4.32 |

  The exact integral has no zero for any sampled limit up to 30 and any sampled `kappa`; the zero at 0.926 is an artefact of the truncation. In the example's units the exact values at limit 1/2 are 41.1 (N = 16) and 659 (N = 64).
- Effect: the qualitative conclusion (order `N^4`, negative, far above the tree quartic) survives and is stronger, but the numbers proposed for the manuscript are not values of the displayed integral.
- Required action: evaluate with the exact incomplete gamma function (add this to s2/s3), replace 27.5 and 441, delete or restate the 0.926 clause, and state the sign for the exact integral. Correct "at least 3.5 times" in the proposal.

**F2. Major. Insert, last sentence of "Correction" and the "Tree curve" paragraph.**
- Finding: "The relation `beta_K = -2 d(rho_M V_t/g^2)/U_chichi` does not use the form of the loop term and stands, with `U_2` now containing `W_R` at leading order" is not established.
- Reason: the first equality at L2808 needs every loop term to respond to the wave through `sqrt|g|` alone. The merged text shows this for `U_4`, the index part of `U_2` and the fibre-constant `Y`, and its scope sentence (L2848) explicitly restricts to "`V = T` where the index part alone enters `U_2` and with `W_R` ... neglected". On the cubic branch `V != T`, and the term `(2 - 3 vartheta/4)(V - T)` (the `R/6 + E_0` part) has a first-order response that nobody has computed.
- Consequence: `beta_K = 2(r_c-1)/(4-3r_c+delta)`, `r_c = (6+delta)/5`, `V/T = (1+delta)^2/25` and `2/(delta-2)` are conditional on that response.
- Not affected: `1 - r_c = -L'/4Utilde` and `V/T = (L'/4Utilde)^2` (stationarity only), and the no-go (V = T forces `kappa = ±2`).
- Required action: state the condition, or compute the response.

**F3. Major. Insert, "Correction": "The example is therefore not a one-loop stationary point of the action with that cubic term".**
- Finding: this is established only for a lower proper-time limit above the spectrum of K and without counterterms. There the exact slope of the replacing term is at least 56 (N = 16), against the merged 5.34.
- Reason: the insert itself says the term is regulator dependent and that the branch is not closed without a mass counterterm. For a limit inside the spectrum, or with cubic and mass counterterms, stationarity at that point is undetermined.
- What is regulator independent: the merged slope `4U_4 + 2U_2 + Y` is not the one-loop slope with the Hessian. `U_2` alone moves from -0.9 to about +0.56.
- Required action: qualify the sentence (snippet below).

**F4. Minor. Notation collisions inside the insert.**
- `c` is the cubic coefficient, but `c\cdot c` in the vacuum-moment sentence is the amplitude sum of the earlier paragraph; `c_T` and "units c" also appear.
- `L'` (loop slope) stands next to `L = 32 pi^2 m^6/A` in `beta_K L' L/8m^4`, and `L^2` is the Casimir.
- `kappa` is already the weight `kappa` of L2767.
- Required action: rename the cubic coefficient (for example `c_3`) and the loop slope (for example `U'_{\mathrm{loop}}`); note the `kappa` reuse or rename it.

**F5. Minor. "no point has `beta_K = 1`, `V = T` and no negative mode".**
- True for `c != 0` at large N, because V = T forces `r_c = 2`; `beta_K` plays no role. As worded it can be read to include `c = 0`, where the statement is about local minima (L2824).
- Required action: write "for `c != 0`, at large N, no point has `V = T` and no negative mode, so none has (S1) with `V = T`".

**F6. Minor. "holds only at `r_c = 0` and at `r_c = 2`, where the negative mode is present".**
- The relative clause applies to `r_c = 2` only. Make that explicit.

**F7. Minor. Correction list is incomplete.**
- Missing: L2810 "`beta_K = 1` is attained in the cubic case at `U_4 = Utilde - (3/2)U_2` and approached from below in the mass case", and L2846 "for `Uhat < 0` ... it is available at negligible `Y`". Both rest on the same forms; the proposal lists L2846 as stale but the insert does not name it.
- Required action: add one clause covering both.
- In-place qualifiers at L2810/L2824 are not required; the L2696/L2707 precedent for a supplementing paragraph is acceptable.

**F8. Minor. Proposal housekeeping.**
- The source-reading section cites digest head 54a2dcb; refresh it.
- Convert the bib entry to CRLF at integration.
- Record that only the authors' initials were verified.

## Scope of what is established

**Proved (exact, within the stated forms).**
- The Feynman-gauge K-vector operator with the cubic term, its spectrum, and the stability range `0 <= c <= 3 chi`.
- `sum w = sum w lambda = 0` and `sum w lambda^2 = (kappa^2 - 4) chi^4 N^2 (N^2 - 1)`, hence the logarithmic divergence of `Uhat`, with counterterm structure `chi^3` and `chi^2`.
- `sum w lambda = 3 mu^2 N^2` for the mass term.
- `1 - r_c = -L'/4Utilde` at a stationary point.
- The elimination identity for the chi exchange.
- The helicity ±2 vacuum moment.

**Numerical (exact spectra).**
- `V/T -> kappa^2/4`.
- The regulated `mathcal U` is negative and of order `N^4` (per F1, for the exact integral at all sampled cutoffs).

**Conditional.**
- `beta_K` on the cubic branch (F2).
- `c_T = T/3` at `r_c = 1` (merged forms, equal weights, supplied K and content; not a sign of `G_eff`).
- `q_*^2|_chi` (first-order responses of L2806, fibre-constant chi, `q^2 < m_chi^2`, merged operators at the example).

**Prior-claim error (M3).** Upheld. L2810 (cubic and mass forms), L2824 (example "`beta_K = 1` is attained at a local minimum with `Uhat > 0`") and L2844 ("does not need a tuned K") were accepted in 049 as one-loop statements for the action with the stabiliser, but they omit the stabiliser's Hessian. At the example that Hessian changes `kappa` from 2 to -0.34 and `V/T` from 1 to 0.028, against the paragraph's own hypothesis `V = T`. The scope sentence at L2848 does not state the restriction. This is a scope omission with a false implication, not a sign or factor error in an equation.

**M2.** Not ruled separately. The bounded no-go removes a branch that existed only through the erroneous claim, so it is subsumed under M3.

**BREAKTHROUGH.** No. No critical-path step is derived.

**No-go class (exact hypotheses).** `K = S^2_N`, `Lambda^i = J^i`; a bosonic cubic term `C_ijk` proportional to `i eps_ijk` on the three K directions, with no fermion bilinear and no mass term; background Feynman gauge; one loop; Poisson limit on M; large N. In this class no `c != 0` has `V = T` without a negative mode. The no-go does not extend beyond this class.

**Everything in the package is PROGRAMME-CONDITIONAL.** F, C and N remain OPEN; there is no label change. The original edge target (second-order `U_2` and first-term response, the first-term constant, the sign of `q_*^2 - q_b^2`) remains open.

**Open avenues that could still favour the IR / full-GR derivation, ranked.**
1. Rotating K (kinetic stabilisation, no tree Hessian): test `V = T` and `beta_K` on its fluctuation operator. Relaxes "static K with tree stabiliser".
2. Completed stabiliser: cubic term with fermion bilinear and masses, where `sum w lambda^2` may cancel. Relaxes "no fermion bilinear". Adopting it in the core would be a structural change to review then; computing it is not.
3. Regulator derived from the matrices of M: fixes the `N^4` term and decides whether any stationary point with the Hessian exists. Relaxes "Poisson limit on M".
4. Response of the `W_R` term to the wave (the gap in F2), then the second-order `U_2` and first-term response with the corrected operators.
5. Other K (`S^2 x S^2`, flux stacks at `f_1 = f_2 + f_3`, where `v = tau` exactly) with their own stabilisers.
6. Higher loops at the tree-stable point `r_c = 1`, where the loop expansion has a small parameter.

## Recommended disposition

Revise (r2), then re-review. Do not integrate r1. At the ACCEPT round the full scan of all `chapters/**/*.tex` is required (3(b)); since `PRIOR-CLAIM-ERROR` is flagged, the item goes to the author rather than to autonomous integration.

## Corrected snippet

No new physics or assumptions. Numbers marked (GK) are from my exact evaluation; the researcher must reproduce them in the pack before using them.

**F1.** Replace "and is negative for \(s_\Lambda\chi^2N^2\le0.9\), a limit above the spectrum of \(K\), for the sampled \(-1<\kappa<2\) (it vanishes at \(s_\Lambda\chi^2N^2=0.926\), \(N=512\));" with:

```latex
and, evaluated without the remainder dropped, is negative for every sampled limit \(s_\Lambda\chi^2N^2\le30\) and the sampled \(-1<\kappa<2\) (exact spectra, \(N\le512\));
```

and replace "\(27.5\) at \(N=16\) and \(441\) at \(N=64\)" with "\(41.1\) at \(N=16\) and \(659\) at \(N=64\)" (GK; exact incomplete gamma function).

**F3.** Replace "The example is therefore not a one-loop stationary point of the action with that cubic term, and" with:

```latex
The slope \(4U_4+2U_2+Y\) used there is therefore not the one-loop slope of the action with that cubic term, and the example is not a stationary point for the sampled lower limits above the spectrum of \(K\) without counterterms; with a regulator from the matrices of \(M\) or with counterterms this is not determined. Further,
```

**F2.** Replace the last sentence of "Correction" with:

```latex
The relation \(\beta_K=-2\,\partial_{\ln\chi}(\rho_MV_{\mathrm t}/g^2)/U_{\chi\chi}\) holds where every one-loop term responds to the wave through \(\sqrt{|g|}\) alone, which the preceding paragraph shows for \(U_4\), the index part of \(U_2\) and the fibre-constant part of \(Y\); for \(V\ne T\) the term of \(U_2\) proportional to \(W_R\) enters at leading order and its response is not computed, so on the cubic branch the relation is conditional on it.
```

In "Tree curve", after "stationarity and the relation above give", insert "(the second under that condition)", and mark `r_c = (6+\delta)/5`, `(1+\delta)^2/25` and `2/(\delta-2)` as holding under the same condition.

**F5.** Replace "Within one loop, on \(S^2_N\) with this cubic term, no point has \(\beta_K=1\), \(V=T\) and no negative mode." with:

```latex
Within one loop, on \(S^2_N\) with this cubic term at \(c\ne0\) and at large \(N\), no point has \(V=T\) and no negative mode, so none has \(\beta_K=1\) with \(V=T\).
```

**F4, F6, F7.** Renaming and one-clause edits as described in the findings.
