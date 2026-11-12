VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M2 | FLAGS: none | PROGRESS: first | OPEN: 0/2

## Verdict
I re-derived the core mathematics and it holds: the normal form, the two classes, the sector no-go for h in C_0 at every N, the N=2 value formula and the pointwise real-spacelike limit. The insert still has to be revised before integration. Its displayed value formula is off by a factor 2 because of how V is normalised, and its closing summary states the F_E(e^{iπ/4}k·k) value without the h∈C_0 qualifier, which is false on −C_0.

## Source reading
- **Mode.** Digest + targeted reads. Not a full scan.
- **Digest.** `make_digest.py --check` printed DIGEST CURRENT, with dirty-chapters: no and head 6403803. appH is 540605 bytes, sha256 e67297cd…34d7, which equals the stated baseline. `git diff --stat HEAD -- chapters bib` is empty.
- **Read in full:**
  - appH L1480–1534: Problem E ledger label, the 053 block, the 054 block and the Status paragraph;
  - ch17 L394–399 (Problem E) and L710–726 (completion criterion);
  - ch04 L316–334 (Assumption `ass:lorentzian`, defined once at L322);
  - the 053/054 entries of `reports/ledger.md`;
  - MILESTONE.md;
  - the whole proposal and insert.
- **Greps.** `\mathfrak C` occurs nowhere in `chapters/*.tex`, so there is no clash. R_u, F_E and the off-axis caveat occur only in appH. Unreadable files: none.
- **Scan ruling.**
  - CLAUDE.md 3(c) does not apply. No definition, assumption, scope or status passage changes; `\mathfrak C` is a local symbol.
  - 3(d) does not apply, since the digest is current and clean.
  - 3(b) applies only to a milestone verdict that triggers a milestone digest. M2 is non-stopping under the directive, and this verdict is not an ACCEPT, so no full scan is required this round.
  - If r2 earns a plain ACCEPT with M2, the same 3(b) question arises again. Ordinal 53 is not a 5th-item scan; that is due at 55.

## Claim under review
- **Target.** Problem E, "derive Lorentzian signature rather than retain Assumption~\ref{ass:lorentzian}".
- **Ledger (appH, verbatim):** "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. A scope retaining Assumption~\ref{ass:lorentzian} gives up the claim of emergent or matrix-derived Lorentzian signature."
- **ch17 (verbatim):** "OPEN; CRITICAL PATH for the matrix-derived label."
- The two sources agree. The current critical-path set is A, B, C, D1, E, F, G-derived and N.
- **Claim (054 open avenue 2), for linear contours A=ΛX with Λ∈GL(10,C), Definition (A), γ=0, ε→0 first at fixed N:**
  - (P)-characterisation of damping: an equivalence at N=2, an inclusion at N≥3;
  - normal form C = C_0 ∪ −C_0;
  - no path within cl(C) joins the two classes;
  - the bounded-mode sector for h∈C_0 at every N;
  - the value V = F_E(e^{iπ/4} q^T h^{-1} q) at N=2;
  - the pointwise limit F_E(e^{iπ/4}k·k) for every real spacelike k at N=2.

## Checks performed
I re-derived the following by hand.
- **Step 0.**
  - At N=2, Tr[A_μ,A_ν][A^μ,A^ν] = −σ_2(G) with G = X^T h X. Hence S_b = σ_2(G)/4g² and S_E = σ_2(X^TX)/4g², and σ_2(G) = Σ_{a<b}(Λ²h)(x^a∧x^b).
  - (P) ⇒ damping: Im Λ²h ≥ c > 0 on the compact set of unit decomposable bivectors.
  - Damping ⇒ (P): use two colour columns.
  - The su(2)-block embedding gives C^(N) ⊂ C.
  - Cauchy–Binet: |det X^ThX| ≤ ‖Λ³h‖ det X^TX.
  - Independent numeric check (my script `gk.py`, item 1): S_b − σ_2/4 = 1.6e-12 at random complex Λ.
- **Lemma 1.**
  - (a) needs a 9-dimensional hyperplane containing b ∉ Ra, so n≥3. At n=2 the hyperplane is Ra itself. The n=2 counterexample D (arg/π = 0.725) is confirmed.
  - (b) The lift is even (m = −m). Each 2-plane curve is an affine ellipse traced once on [0,π] with winding (α(−a')−α(a'))/2π = 0. That puts 0 outside the filled ellipse, so the curve lies in an open half-plane and its range is < π. The max/min plane argument holds, including the dependent case by evenness.
  - (c) P+iQ = W^T O^T(I+iλ)O W.
  - (d) is the Lagrange identity.
  - (e) The common k: sums sharing an index in different intervals would force |β_ρ−β_ν| > π. Disjoint pairs are linked through a third index.
- **Lemma 2.**
  - At most one β outside (0,π), and at most one outside (−π/2,π/2). The mixed case is excluded via a third index.
  - Sylvester inertia gives ≥9 positive eigenvalues of Re h and of Im h on C_0.
  - A common limit point has ≥8-dimensional kernels of Re h and Im h, which meet in dimension ≥6. So h is singular.
  - η has 9 positive eigenvalues of Re h, so η ∉ cl(−C_0).
  - R_u ∈ C_0 iff 0<u<2. Pair sums are π−πu/2 and πu/2, consistent with 053's Re iS_b = −sin(πu/2)S_E.
- **Step 3.**
  - Mode bounded ⇔ q = Λ^T k real, including the case Im q ∥ Re q.
  - k·k = q^T h^{-1} q. The args −β'_μ lie in [−β'_max, −β'_min] ⊂ (−π, π/2), using β'_max < π, β'_min > −π/2 and spread < π, each via a third index.
  - **The "every N" claim is valid.** It needs only the inclusion C^(N) ⊂ C, not its converse. The sector statement itself is pure linear algebra for h∈C_0 and real q.
  - Independent sampling (`gk.py` item 2): 15000 (h,q) pairs on C_0, all args inside the sector. Minimum count of positive eigenvalues of Re h and Im h was 9 (item 4).
- **Step 4 (N=2).**
  - W is holomorphic on the open set C, with locally uniform domination by 053's k=0 bound. W is even under h → −h.
  - Real covariance: W(h,q) = |det T|³ W(T^ThT, T^Tq).
  - The scaling gives g = f·Πd^{3/2}, constant on the connected D_0, with g ≠ 0 at e^{iπ/4}I (W = −Z_E).
  - The reduction to U(w) is correct. On e^{−iπ/4}R_+^{10} the contour is Euclidean, and SO(10) invariance gives F_E(Σx).
  - Σw stays in the sector, so the identity theorem applies on the maximal totally real open subset.
  - −C_0 follows by evenness.
  - **Normalisation error found:** see F1.
- **Step 5.**
  - Hypotheses: Re iS_b ≤ 0 on cl(C); the regulator real part is ≥ εc|X|² along the path; Stokes at fixed ε; dominated convergence on Λ(1); Jacobians cancel in the ratio.
  - Construction: −e^{i(β_0−π)} = e^{iβ_0}, so h = diag(e^{iβ}). The equations r_1² = 2cos a·r_2² and r_2² = 1/(4cos²a−1) are verified.
  - Pair sums at τ=1 are π−7πu/8, π−πu/2, πu/8 and πu/2, so h(1) ∈ C_0 for 0<u<8/7.
  - Λ(0) = L S_0 is real, and Re Λ^TΛ → S_0^T L^T L S_0 > 0 as u→0. The same argument works with M in place of L^T L.
  - **Independent construction** (`gk.py` item 5), with my own η-Gram–Schmidt, for a boosted k (rapidity 1.2, random spatial rotation):
    - S η S^T = η, h = diag(e^{iβ}) and Im q = 0 all hold to 1e-8 on 201 τ points;
    - min eig Re Λ^TΛ = 0.077, 0.090 and 0.091 at u = 0.05, 0.01 and 0.002;
    - it is negative at u = 0.2, which confirms that "small u" is genuinely needed.
  - **Lorentz invariance.** The value depends only on k·k by the formula, while the regulator breaks boosts. This is correct.
- **Scripts.** All re-run on copies in the scratchpad; the repository was not modified (`git status --short` is clean).
  - `path_check.py`: output identical to `path_check.txt`.
  - `lemma_checks.py`: output identical to `lemma_checks.txt`. Part C (adversarial) is uninformative, as the researcher says.
  - `mc_check.py`: not re-run (long). I read its code. It normalises by ∫w without the trace, i.e. it computes ⟨Tr⟩, which is how F1 was detected.
  - `apply_check.py`: re-run in report mode; output identical to `apply_check.txt`.
  - My own checks are in `C:\Users\redgi\AppData\Local\Temp\claude\3ba14ee056ac155d\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\gk.py`. Numerical output is a check, not a proof.
- **Hashes.** Baseline 540605 / e67297cd3066e3f4795ed81875d5075dfec3fe98ba5a8d8feb0bfcb733e134d7. Anchor 61 bytes, count 1, line 1529. Insert LF 9324 bytes / ca32f192…5b1, CRLF 9345 bytes / 3b14cca7…945. Result 549952 bytes / 008db280ef2bebae769670a5b8ea498ab1cd6ae9539253b878e615beef83f1c5, CRLF 3242, bare LF 0. All reproduced. They will change with the required revisions.
- **LaTeX and wording.**
  - The only reference is `\ref{ass:lorentzian}`, which exists once. No labels, no citations.
  - No process language. The "round" hit is "around".
  - Finsler, Calabi and Brickman are absent from the insert, and the proposal marks them "not independently verified". The Lemma 1 proof is self-contained and verified, so no citation is needed.
  - The insert block in the proposal is byte-identical to `appH_insert.tex`.
- **Status labels.** No status, priority or completion label changes.

## Findings
1. **Major — insert (iv), definition of V and the displayed formula: factor 2 normalisation error.**
   - W(h,q) contains Tr e^{iq·X}, so W(h,0) contains Tr 1 = 2 and V(h,0) = 1. But F_E(0) = Tr 1 = 2, and F_E(t) = ⟨Tr e^{i√t Ã_0}⟩_E is normalised by the partition function without the trace.
   - At the Euclidean point the insert's V equals F_E(|q|²)/2, so the display V = F_E(…) is wrong by a factor 2. `mc_check.py` uses the correct normalisation (est = mean(w·O)/mean(w)), so the scripts do not see the error.
   - (v) is correct only once V is normalised by the partition function.
   - Required: replace `and let \(V(h,q)=W(h,q)/W(h,0)\).` with `and let \(V(h,q)=2W(h,q)/W(h,0)\).` The statement about W(·,0) is unchanged. The proposal Step 4 has the same slip; correct it there too.
2. **Major — closing paragraph, first sentence: overstatement on −C_0.**
   - "the contour integrals with bounded Fourier modes are therefore at N=2 values of F_E at e^{iπ/4}k^μk_μ" is false for h∈−C_0, where (iv) itself gives F_E(−e^{iπ/4}k·k).
   - Required: replace `the contour integrals with bounded Fourier modes are therefore at \(N=2\) values of` with `the contour integrals with \(h\in\mathfrak C_0\) and bounded Fourier modes are therefore at \(N=2\) values of`.
3. **Minor — closing paragraph: the scope of the no-go should say explicitly that −C_0 contours do reach real timelike k.**
   - I verified an example: A_0 = X_0, A_i = e^{2πi/3}X_i. This is R_{4/3} times i, with h = diag(−1, e^{4πi/3}) and −h ∈ C_0 (phases 0, π/3).
   - It is damped (Re iS_b = −sin(2π/3)S_E), and q = (κ,0,…) is real for k = κδ_0. Its value is F_E(e^{iπ/4}κ²).
   - It is not joined to the Hermitian contour within cl(C), by (ii).
   - Without this sentence, "exactly the nonzero causal ones" reads as a statement about all linear contours.
   - Required: after `are exactly the nonzero causal ones, \(k^\mu k_\mu\le0\).` insert the sentence `Contours with \(h\in-\mathfrak C_0\) do make the mode bounded at real timelike \(k\), for example \(A_0=X_0\), \(A_i=\mathrm e^{2\pi\mathrm i/3}X_i\) at \(k^\mu=\kappa\delta^\mu_0\), with the value \(F_{\mathrm E}(\mathrm e^{\mathrm i\pi/4}\kappa^2)\) at \(N=2\), but by (ii) no path along which \(h\) stays in the closure of \(\mathfrak C\) joins them to the Hermitian contour.`
4. **Minor — (iii): incomplete inference.** Lying in "an open half-plane" alone does not give the sector (−π, π/2). The proof also needs β_max < π, β_min > −π/2 and spread < π.
   - Required: replace `For \(h\in\mathfrak C_0\) the directions \(\mathrm e^{-\mathrm i\beta_\mu}\) lie in an open half-plane, so \(k^\mu k_\mu\) lies in the sector` with `For \(h\in\mathfrak C_0\) the pairwise conditions, applied with a third index, put the arguments \(-\beta_\mu\) of the directions \(\mathrm e^{-\mathrm i\beta_\mu}\) in an interval of length less than \(\pi\) inside \((-\pi,\pi/2)\), so \(k^\mu k_\mu\neq0\) lies in the sector`.
5. **Minor — closing sentence repeats the 054 block's closing clause.** "Problem~E keeps its ledger label" is identical to the end of the preceding paragraph, which itself follows 053's status line. That makes repeated status closings on consecutive paragraphs.
   - Required: replace `so no signature is derived, Assumption~\ref{ass:lorentzian} is not discharged, and Problem~E keeps its ledger label.` with `so no signature is derived and Assumption~\ref{ass:lorentzian} is not discharged.`
6. **Minor — (iv): ambiguous "zero components of q".** It is T^{-T}q that is rescaled.
   - Required: replace `zero components of \(q\) follow by continuity` with `zero components of \(T^{-\mathrm T}q\) follow by continuity in \(q\)`.
7. **Minor — (v): regularity of the path.** Stokes' theorem on the swept region needs a piecewise C¹ homotopy. The explicit path is smooth, so this costs nothing.
   - Required: replace `Let \(\Lambda(\tau)\), \(0\le\tau\le1\), be continuous,` with `Let \(\Lambda(\tau)\), \(0\le\tau\le1\), be piecewise continuously differentiable,`.

**Note (not a finding).** The orchestrator's summary phrase "GL(10,C) linear contours never enlarge the sector" is accurate only for h∈C_0. The proposal Result item 2 correctly states "Suppose h is in C_0".

## Scope of what is established
- **Established identities (exact):**
  - S_b = σ_2(X^ThX)/4g² at N=2;
  - damping ⇔ (P) at N=2, and C^(N) ⊂ C at N≥3;
  - Lemma 1 (C = C_0 ∪ −C_0, needs n≥3) and Lemma 2 (disjoint closures on invertible h; η ∈ cl C_0 \ cl(−C_0)).
- **Bounded no-go (exact, every N).** Exact hypothesis class: linear contours A = ΛX with Λ ∈ GL(10,C), damping Re iS_b ≤ −c S_E, h ∈ C_0 (the class adjacent to the Hermitian contour), and observable Tr e^{ik·A} required to be bounded on the contour. Under these hypotheses k·k lies in −π < arg < π/2, and real causal k ≠ 0 is unreachable. This does not hold for −C_0, which reaches real timelike k (Finding 3).
- **Proved at N=2, conditional on 053's N=2 flat-direction bound and 054 (iv) holomorphy of F_E, both already in the manuscript:**
  - the value formula on C_0 (with corrected normalisation);
  - the pointwise ε→0 limit for every real spacelike k, equal to F_E(e^{iπ/4}k·k), regulator- and boost-independent.
- **Classification.** PROGRAMME-CONDITIONAL sharpening plus a bounded no-go (M2: it settles the off-axis/index-mixing route that 054 left open). Not a breakthrough: η is an input to S_b and no signature is derived.
- **Problem E stays OPEN; CRITICAL PATH for the matrix-derived label; PROGRAMME-CONDITIONAL.** No label change.
- **Relaxations that remain open**, ranked by how promising I judge them for reaching real causal k:
  1. Paths leaving cl(C) but keeping Re iS_b ≤ 0 (Lemma 2's hypothesis). The class D = {Im Λ²h ≥ 0 on decomposables} strictly contains cl(C); real h of any signature has Re iS_b = 0. Because −C_0 already reaches real timelike k, connectivity of the Hermitian contour to −C_0 through D (with the regulator kept admissible) is the sharpest open question.
  2. Non-linear (thimble) contours at real causal k, N=2.
  3. Direct oscillatory analysis of the real-timelike/null pointwise limit at N=2. The Step 6.4 power count is heuristic only.
  4. N→∞ first.
  5. N≥3 for (iv) and (v), which needs an independent proof of 053's bound for general h.
  6. γ≠0 and Definitions (B) and (C).
  7. OS positivity.

  None of these would by itself derive signature while η is put into S_b by hand.

## Recommended disposition
Revise: apply Findings 1–7 verbatim, regenerate apply_check hashes, and rebuild. On resubmission I expect the content to be acceptable without new mathematics. Under the plain-ACCEPT rule, this must go to r2.

## Corrected snippet
The replacements are given exactly in Findings 1–7. They need no new physics or assumptions. The −C_0 example in Finding 3 was verified above.

VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M2 | FLAGS: none | PROGRESS: first | OPEN: 0/2
