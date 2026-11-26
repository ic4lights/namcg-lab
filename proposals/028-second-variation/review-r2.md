VERDICT: ACCEPT | MILESTONE: none | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
All six r1 findings are closed. The r2 block is the r1 block with exactly two paragraphs edited, the anchor is unique, and I found no new error. Accept for integration at ordinal 26 as a bounded, conditional no-go and structural lemma that changes no label.

## Source reading
Digest + targeted reads, not a full scan. This is not a cadence item, and no definition, assumption or status text changes. The tree is dirty only in appH, from the accepted 025–027 integrations, as expected. I read the affected passages directly (CLAUDE.md 3(d)).
- Read in full: proposal-r2.md, block-r2.tex, review-r1.md.
- Read: appH lines 2126–2130, the end of the 027 block and the anchor.
- Not re-run: the r1 scripts. I re-verified them in r1 (tensor lemma with an independent Dirac representation, operator identities, toy Duhamel check, s² growth, Hessian statistics), and r2 changes no script or numerical claim. I did not rebuild the PDF; I relied on compile_check_r2.out.txt (0 errors, 0 undefined, 0 multiply defined, 289 pages).

## Claim under review
Within the CP^{1,2} four-matrix class, every species operator has the form H_i = (−Box_X)⊗1 + Σ_i^{ab}⊗{F_ab,·} + m_i for arbitrary X. The weighted supertrace then cancels for the mass-free terms through three Z insertions. The weight-two coefficient reduces to M_str times a first-jet leading-symbol moment. The order-F⁴ term is not expandable in the present window.

Targets: Problem F is "OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL; 'treating G_eff as an input leaves F OPEN'". Problem E is OPEN, CRITICAL PATH for the matrix-derived label, PROGRAMME-CONDITIONAL. Both quotes are as recorded in the 027 review and the r1 review; I did not re-read Appendix H for them. No label is touched. Chapter 17's critical path (A, B, C, D1, E, F, G-derived, N) is unchanged.

## Checks performed
- **Block identity.** The ```latex block in proposal-r2.md equals block-r2.tex exactly (scripted comparison, CRLF stripped: True).
- **r1 to r2 diff.** Only two lines differ: the "Species sums" paragraph and the "Consequences" paragraph. Nothing else changed, so the generated block has no unintended changes.
- **Anchor.** `\section{Problem G: HBEV}` occurs once, at appH line 2130. It directly follows the 027 block, whose last sentence is "This changes no ledger label; Problem~F remains open." The new heading text occurs nowhere in `chapters/`.
- **Labels.** The only reference is `ch:vierbein-emergence`, which exists. There are no new labels, citations or bib changes. The compile check reports 0 undefined and 0 multiply defined.

Per finding:
- **F1, sign.** Fixed.
  - The block now says "the term linear in the masses and without insertions of 𝒵 is +M_str Tr[χΦ′(H_X)] (for Φ=e^{−(·)} this is −M_str Tr[χ e^{−H_X}])".
  - This is consistent with a scalar m and with the toy script's c_2.
  - Term (ii) reads "proportional to M_str ∫χ(σ_X−i0)^{−1}" and claims no sign.
  - No sign of G_eff is claimed anywhere.
- **F2, flux shift.** Fixed. The shift is stated "at the phase φ=0, where the first-jet terms vanish". The false "enters only through" is gone. The general-phase field is given earlier as W^a − ε sin φ α^a Y_q.
- **F3, K^{μν}.**
  - The K^{μν} language is dropped.
  - The block now says: "depends on A only through its first derivatives, so its second variation contains no second derivative of the fluctuation and no term of Einstein–Hilbert form; the next-to-leading symbol, which involves the second jet of X, is not computed."
  - This is restricted to the leading-symbol term. The closing paragraph also says the next-to-leading symbol and the A-dependence of EH-form terms are not computed, so the earlier tension is gone.
  - Summary item 2 in the proposal body now limits "exactly zero for every A" to the count, spin and cubic terms.
- **F4, covariance wording.**
  - The block says "at fixed proper time and κ=3/4 … in the integrand … through the vector y^μ and the window". It says "its integrand is therefore not Lorentz invariant (the window and the leaf both single out y^μ, and this diagnostic does not separate them)".
  - The 2–180 ratio and the Steinacker comparison appear only in the proposal body, not in the LaTeX.
- **F5, Hessian wording.** Fixed. The block specifies the real (principal-value) part, numerical, 59 draws, frozen coefficients and φ=π/2, with counts 40, 5 and 14 that sum to 59. It says "numerically nonzero in all draws with non-null q"; the gauge-invariance reason is removed.
- **F6.** The Visser eq. 33 versus eq. 35 correction is in the proposal body only. Visser and Steinacker are not cited in the LaTeX.

## Findings
none. Minor, non-blocking observations:
- (iii) says an EH-form term "can therefore enter only through the constants listed above". This is true within the class and the formal expansion, as the next paragraph's scope sentence states. No change is required.
- The closing scope sentence has no repeated status line on consecutive paragraphs, and there is no process language.

## Scope of what is established
- **Established (exact algebra, formal expansion):**
  - The all-X species form H_i, with the same Box_X and the same {F_ab,·} for all species.
  - The tensor identities Σwd = 0 and Σw tr(Z…Z) = 0 for n=1,2,3, with the n=3 cancellation depending on Z_D = −Σ_D.
  - n=4 gives the character coefficient (f_e²+f_m²)², which is nonzero.
  - Each Duhamel term is a species constant times a species-independent operator trace.
  - The count, spin and cubic terms vanish for every X.
  - The first surviving mass constant is M_str = 4μ² + n_ex μ_i², with +M_str Tr[χΦ′(H_X)] at no 𝒵 insertion.
  - Convergence is not claimed.
- **Established (leading symbol, within the class):** the weight-two term depends on A only through the first jet.
- **Numerical, sampled diagnostics only:**
  - Hessian indefiniteness (frozen coefficients, φ=π/2).
  - s² growth of the F⁴ integrand at four orbit points.
  - Integrand-level dependence on q·y at fixed proper time.
- **Not established:**
  - Any EH-form coefficient or its sign, and G_eff.
  - The next-to-leading symbol.
  - The second variation of the closed-form logarithm.
  - The map from A to the emergent metric fluctuation.
  - The Lorentzian meaning of the F⁴ term.
- **Hypothesis class of the no-go:**
  - Poisson limit.
  - One loop.
  - Leading symbol.
  - CP^{1,2} four-matrix class with μ²=−3.
  - Vanishing transverse matrices.
  - Supplied 16-component fermions with no bilinear mass.
  - One species-independent window χ(Δ_κ) built from the fixed T.
  - Formal Duhamel expansion.
- **Labels.** Problems E and F stay OPEN and PROGRAMME-CONDITIONAL. Nothing is DERIVED, and spacetime stays emergent.
- **Open avenues, ranked:**
  1. Next-to-leading symbol (Wigner–Kirkwood, R/6 + E structure) of the M_str term on the six-dimensional leaf. This is the only place in this class where an EH-form piece can enter. It relaxes "leading symbol".
  2. Nilpotent (Landau) resummation of the non-expanded logarithm. It is finite and hypoelliptic, and gives the direct route to an F⁴ constant and its sign. It relaxes the Schwinger expansion.
  3. Fermion mass patterns (scalar m_F or matrix bilinears). These break T_2=0 and relax "no bilinear mass". With M_str = 4μ² + 6μ_i² − 8m_F, the str(m²)=0-type point is reachable.
  4. Transverse flux or fuzzy K with the mixed invariant. This is the Steinacker-type EH route and relaxes "transverse matrices vanishing".
  5. Species- or A-dependent windows. This relaxes the common window and breaks the lemma.
  6. Eight-matrix sets and Moyal terms.

  Items 1 and 2 are the most promising.

## Recommended disposition
Integrate as-is (ordinal 26).

What is accepted: exactly the `\paragraph{Conjugate-coordinate class: the supertrace at an arbitrary matrix fluctuation, …}` block of block-r2.tex (the proposal's LaTeX block, identical). It is inserted immediately before `\section{Problem G: HBEV}` at appH line 2130, after the 027 block. It comprises the heading, the setting paragraph, the "Operators at arbitrary X", "Species sums" and "Consequences" paragraphs, and the closing scope paragraph.

Not accepted as text: the proposal-body statements (2–180 ratio, Steinacker comparison, Visser references, ranked forks). They are for the record only.

No label change. No AUTHOR-DECISION.

## Corrected snippet
none needed.
