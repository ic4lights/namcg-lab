VERDICT: ACCEPT | MILESTONE: none | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
All r1 findings are closed in the LaTeX. The block is wording-only against r1, so the mathematics I verified in r1 is unchanged. The block is a bounded, conditional package that changes no label, and I accept it as written for ordinal 25.

## Source reading
- Digest + targeted reads. I did not repeat the full scan.
- The r1 full scan (30 files, ordinal 25) stands because `git status` shows only `M chapters/appH-microscopic-proofs.tex`.
- The appH diff is two 17-line insertions:
  - the 026 paragraph before `\section{Problem C}` (sec:status-B);
  - the 025 block before `\section{Problem G: HBEV}`.
- All chapter and bib files other than appH are unchanged. I read the 026 hunk. It concerns the Euclidean N_s=6, n_D=2 quartic, uses its own notation, and does not interact with 027.
- Nothing was unreadable.

## Claim under review
- **Claim.** Conditional, bounded results for the weight-two coefficient of Problem F in the conjugate-coordinate class, as in r1:
  - the Gaussian lemma;
  - the cone-window moment;
  - the Zeeman closed forms;
  - the vector/ghost/spin terms;
  - the supertrace remainder.
- **Problem F, verbatim from Appendix H.** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating \(G_{\mathrm{eff}}\) as an input leaves F OPEN and does not satisfy the matrix-derived criterion."
- **Problem E, verbatim from Appendix H.** "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. A scope retaining Assumption~\ref{ass:lorentzian} gives up the claim of emergent or matrix-derived Lorentzian signature."
- **Chapter 17.** The critical path remains A, B, C, D1, E, F, G-derived and N. No label changes.

## Checks performed
Direct checks:
- **block-r2.tex vs proposal block.** I extracted the fenced block from `proposal-r2.md` and compared it with `block-r2.tex`. They are identical (they differ only by a trailing newline).
- **Anchor.** `\section{Problem G: HBEV}` occurs exactly once (line 2095 in the working tree). It is immediately preceded by the 025 block, whose last sentence is "This changes no ledger label; Problem~F remains open."
- **Labels.** `ch:vierbein-emergence` and `ass:lorentzian` exist. The block adds no labels, no `\cite` and no bib entries.
- **r1 to r2 diff, finding by finding.**
  - **F1.** The unique-continuation and domain-of-dependence sentence is gone.
    - The block now says "quadrature indicates ... departs from it beyond; this is a numerical observation and is not proved here."
    - The sign of Re N_W is stated as "conditional on the numerical observation".
    - Finiteness is "likewise rested on the shell formula".
    - The window function is described as having a jump at the cone edge, not as Lipschitz.
    - The scope paragraph repeats the conditionality.
    - A grep for "unique continuation", "domain of dependence" and "Lipschitz" in the block returns 0.
  - **F2.** The reference to g is removed.
    - D = D₀(1+D₁+…) is defined, with D₁ depending on a and homogeneous of degree one in (z,w) = (t−is, is).
    - The tr(E+R/6) convention is stated as "exponent Δ+E", and it equals D₁ for one scalar component.
    - x = s/t is defined at use, with "the subtraction at x=1".
  - **F3.** The block states "59 of the 60 points" and gives the whitening cause. It gives 10⁻⁹ except for the base maximum, which is 6·10⁻⁵ over 3000 directions. `flux_closed_forms.out.txt` confirms this: 59 points, centre 2.0e-14 and 1.2e-13, vertical 1.3e-10, base 6.2e-5 and B_base 2.8e-13.
  - **F4.** The rate is "bounded by a quantity linear in the base cutoff, whose fibre part is bounded independently of the base cutoff". The log det has "only integrable logarithmic singularities, at σ=±2f_m, at the leading symbol".
  - **F6.** The renames are complete and consistent.
    - The eigenvalues are f_e and f_m, the form is 𝖪 with 𝖪_uu, 𝖪_uζ and 𝖪_ζζ, the second-moment matrix is 𝖭, and the Jacobian is ϱ.
    - The mass moment is j(a), the window integral is 𝒩_W, and bold 𝐱 is the cone variable.
    - Only 𝒥_ab remains, for the generators. No S, A or B eigenvalue, no ⟨⟩_W, no g, and no 𝒥_a or 𝒥_c remain.
    - S² = 2C₄₁−C₄₂ is retained and no longer clashes.
  - **F7.** The clause is present: on the kernel plane F²/2 is negative for |y⁴|<ℓ, positive above, changing sign exactly at |y⁴|=ℓ. It says this replaces the sample-dependent value of the preceding paragraph on that plane, and that the signs are opposite on the vertical plane.
    - From f_e²−f_m² = |ζ|²(a²−1)/2 on the vertical plane and the (1−a²)/(2(1+2a²)) form on the kernel plane, the signs are indeed opposite.
  - **F8.** The block states the remainder as −(4μ²+n_ex μ_i²) j(a), with Re j = 2/(1+a²) > 0 and "no sign of the mass supertrace itself is claimed". The closing clause reads "does not by itself carry ... whether it arises at higher order ... or through the dependence on A is not computed."
  - **Nothing else changed.** The remaining diff hunks are the F-items above, the F5 and F6 renames, and the scope paragraph updated to match.
- **Saved outputs.**
  - `tangency_identity.out.txt`, `shell_apex_lemma.out.txt`, `cone_window_geometry.out.txt`, `cone_window_moment.out.txt`, `sd_scalar_vs_exact.out.txt` and `flux_closed_forms.out.txt` exist.
  - Their numbers match the r1 re-runs: 7.95e-10 geometry deviation, I₀ = 32.172127 against the closed form, the trace identity 34.198648 on both sides, apex-inside 14.19139 against 14.18981, and the SD difference ~1e-125 at three points.
  - The divide-by-zero warnings in `cone_window_geometry.out.txt` and `flux_closed_forms.out.txt` are disclosed.
- **Compile.** `compile_check_r2.out.txt` shows anchor unique, rc 0 on all passes, 0 errors, 0 undefined, 0 multiply defined, 285 pages. I did not re-run it. The r1 compile of the same structure passed on my side, and no label or cite was added.

Not verified:
- The Seeley–DeWitt machinery beyond the r1 re-runs.
- The fermion content, which is a supplied input.
- Any literature: none is cited.

## Findings

**1. Minor, not manuscript-affecting. Location: `sd_scalar_vs_exact.py` line 15, the "repaired" det check.**
- The condition is an `or` of three sign alternatives (`abs(1/dd)−ell²/m2`, `1/dd+ell²/m2`, `1/dd−ell²/m2`). It prints True for either sign of det, so it is weak as a test.
- The explicit inverse check passes, and the 125-digit SD comparison is the load-bearing check.
- Optional tidy-up: test the single sign actually claimed. This does not block integration.

No other findings. No PRIOR-CLAIM-ERROR. The 025 sentence that the Lorentzian moments are "numerical" is superseded only for Gaussian windows and, conditionally, for the cone window. The block says so and leaves it untouched, which is acceptable.

## Scope of what is established
Proved (class: Poisson limit, one loop, leading symbol, invariant sector, four-matrix class with μ²=−3):
- For every Gaussian window of the class, Re M>0 and Im M>0. This rests on σ(□) having rank 4 and signature (3,1) for y⁴≠0.
- The apex-inside shell formula.
- The spin-term sum rules and the Dirac/vector trace relation, by algebra.
- The Zeeman character identity.

Established numerically at sampled points (geometry identities, Zeeman closed forms, the SD route against the exact scalar D₁, the vector and Dirac traces, closed-form Q_μ and Q_sp). These are not proofs.

Conditional on a numerical observation: the continuation of the shell formula to spacelike p with |p|≥R up to R·cothτ. This makes Re N_W>0 and the finiteness of N_W conditional.

Bounded no-go, within its stated hypotheses. For the supplied IKKT content (16 real fermion components, no bilinear mass, n_ex=6, same window for bosons and fermions), the species-independent curvature/connection part of the weight-two term at A=0 does not by itself carry the Newton coefficient. The count, index and F² terms cancel. The remainder is the mass supertrace times j(a). No sign of G_eff or w is obtained.

Problem F remains OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. Problem E is untouched except for the caveat on `ass:lorentzian`.

Open avenues, ranked (most promising first):
1. The A-dependence (second variation under the matrix fluctuation) of the mass-supertrace term, and the order-s⁴ Zeeman-character term (f_e²+f_m²)². This is the hypothesis "A=0 and species-independent part only".
2. Fermion content or mass pattern beyond "no bilinear mass" (supersymmetric bilinears, fermion masses, the eight-matrix (5,1) set). This relaxes the supplied-input hypothesis.
3. A window with |p|<r, or a proof of the continuation. This would turn the conditional sign into a theorem.
4. The exact vector kernel and Plancherel/finite N, which tests the assumption that the SD coefficient is the weight-two term.
5. The real/imaginary identification, and non-Gaussian windows built from dynamical matrices.
6. Moyal terms and the SO(4,1)→SO(3,1) branching.

## Recommended disposition
Integrate as-is. Accepted: exactly the LaTeX block in `/c/Users/redgi/Projects/namcg-lab/proposals/027-fibre-window-spin1/block-r2.tex`, which is identical to the fenced block in `proposal-r2.md`.
- Insert it immediately before the unique `\section{Problem G: HBEV}`, after the 025 block, as ordinal 25.
- Convert it to CRLF.
- Change no labels.
- Leave the 025 closing sentence untouched.

## Corrected snippet
None needed.
