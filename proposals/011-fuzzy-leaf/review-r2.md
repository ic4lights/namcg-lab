VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M2 | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
F1, F2 and F4–F7 are closed. The torsion identity is now a correct derivation, and I verified its imported classical step independently. Two small wording corrections to the proposed LaTeX are still required: add "modulo total derivatives" to the linear-dependence sentence, and soften how the imported identity is described. After those, the text can be integrated.

## Source reading
- Digest and targeted reads only.
- I read `proposal-r2.md` and `review-r1.md` in full and diffed r2 against r1.
- I read `check_torsion_exact.py` and re-ran it and `check_zero_mode_nogo.py`.
- I checked the anchor and labels in `chapters/appH-microscopic-proofs.tex`.
- The chapters are unchanged since my r1 full scan, which was done at ordinal 10 (all 30 chapter files, ch01–ch18 and appA–appL, with appH in full). That scan satisfies the 5th-item requirement.
- Literature: I did not re-fetch Steinacker2023. The r1 verification of its (4.13), (4.16)–(4.18) and (7.19)–(7.24) stands. Kumar–Steinacker and Steinacker2026 are not independently verified and are not cited in the proposed text.

## Claim under review
- **Target:** Problem F (`ass:emergent-op`) is primary. A, D1 and E are affected by dependency.
- **Problem F, Appendix H verbatim:** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion."
- **A and E:** "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL."
- **Chapter 17:** the criterion lists A, B, C, D1, E, F, G-derived and N. I found no discrepancy with the ledger.
- **Claims in r2:** a bounded no-go on the leaf-dimension relaxation, the CP^{1,2} class, a conditional heat-kernel factorisation, and the torsion identity for X, now claimed proved.
- **Original F target:** NOT met.

## Checks performed

**Torsion proof, step by step (hand re-derivation).**
- **(i)** Using η^{-1}=ΘGΘ^T and dω=0, X=I_A. I verified the index manipulation in the text, X=G_{μν}T^{αβμ}T_{αβ}{}^ν with T^{αβμ}=Θ^{μρ}∂_ρΘ^{αβ}.
- **(ii)** V_μ=∂_μ ln|Pf ω|. The chain is ∂_β Θ^{αβ}=−Θ^{αa}∂_a ln Pf ω, then V_μ=−ω_{μα}∂_βΘ^{αβ}. It is correct.
- **(iii)** The teleparallel identity R[G]=−(I_A/4+I_B/2−V²)−2∇_μV^μ is the imported step. See the dedicated paragraph below.
- **(iv)** S²=(I_A−2I_B)/3. The algebra is right. Substituting gives I_A=−2R+(3/2)S²+2V²−4∇V.
- **(v)** For G=ρ g_ρ in 4D, R[G]=ρ^{-1}(R_g−3□lnρ−(3/2)|∇lnρ|²). The unimodularity step ρ□lnρ=td−r is right. This gives ρ²R=h+(3/2)r−3td.
- **Combination:** −2(h+(3/2)r−3td)+(3/2)ρ²S²+2r−4td=−2h−r+(3/2)ρ²S²+2td. This matches the stated identity.

**Exact script.**
- `check_torsion_exact.py` re-ran in 15 s. All seven checks passed in all 12 cases (6 seeds, both signatures), with lhs equal to rhs.
- The teleparallel identity also passed for generic non-closed coframes.
- Jet truncation is adequate: ω is degree 2, curvature needs second derivatives of G, and T and ∇V need only the first-order jet of T. The `==` comparison on Fractions is exact.
- The curvature convention is standard (MTW, Ric_{bd}=R^a{}_{bad}).
- This tests the identity at finite amplitude on random jets. It is not a proof, but it supports the hand proof.

**Imported teleparallel identity, verified independently.**
- I wrote my own sympy script, `C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\4d0177a0-6b3d-45ad-bb6d-645d2be99f00\scratchpad\tele.py`. It uses a different dimension (3D), Lorentzian η, a random polynomial non-closed coframe, and MTW curvature with ∇V from Christoffels.
- It gives R−[−(I_A/4+I_B/2−V²)−2∇V] = 0 exactly at the origin, with both sides −0.5545. So the identity holds in the proposal's own index convention (V_μ=G^{ln}T_{lmn}, T_{lmn}=η_{AB}e^A_l T^B_{mn}).
- This agrees with the standard form R=−T+(boundary term). I did not fetch Aldrovandi–Pereira or Steinacker (4.13) this round. Their sign conventions differ in the index placement of V, so I did not check against them. The literature match is therefore "not independently verified". The exact symbolic and rational checks are what I rely on.
- With the identity independently confirmed in the stated convention, the whole chain is established.

**F1 (c>0 / c<0 split).**
- K=θ^T gθ=−θgθ, so K=c g^{-1} is N²=−c·I for N=θg.
- For c>0, det N=c^m>0, whereas det N=Pf(θ)² det g<0. This is excluded.
- For c<0, N^T g=−gN. N²=|c|·I makes N real-diagonalisable with eigenvalues ±√|c|. For eigenvectors u, u′ of the same eigenvalue, 2√|c| g(u,u′)=0, so each eigenspace is totally null. The Witt index of a Lorentzian form is 1, so each has dimension ≤1 and 2m≤2.
- The 2m=2 counterexample θ=2ε, g=diag(−1,1), K=−4g^{-1} is correct. The script's item (d) now prints it, with null eigenvectors, and no longer prints "impossible" at 2m=2.
- The determinant-sign illustrations at dimensions 2, 4, 6 and the Witt statements are fine. The wording "dim 2 ... c>0 excluded" is accurate.
- Theorem 1 itself re-ran with unchanged results. K=0 gives Θ^{Iμ}=0 for all I and μ≤3, including Θ^{0k}=−Θ^{k0}, so the K=0 exclusion is complete.

**F2 (linear-dependence sentence).**
- 005 places ρ²X in span(h,r) mod total derivatives. Combined with the identity, ρ²S² is then in span(h,r) mod total derivatives.
- So the dependence holds only modulo total derivatives, because the identity carries the term 2td. The proposed sentence says "linearly dependent" without that qualifier, which is imprecise. See Finding 1.
- The net coefficient 1−N_tot/24 is unchanged. The "(N_tot−12)/6" content is gone from the text.

**Anchor and labels.**
- The sentence "This changes no ledger label; Problem~F remains open." occurs exactly once, in `chapters/appH-microscopic-proofs.tex` at line 1835, and `\section{Problem G: HBEV}` is at line 1837.
- The new text uses `\ref` only on labels I verified in r1 (`def:matrix-coords-ext`, `thm:Geff`, `ch:vierbein-emergence`). It uses `\cite{Steinacker2023}` only. No new labels.
- The status sentence now closes only the last paragraph (F7 closed).
- The git working tree is clean.

**Emergence and labels.**
- Spacetime stays emergent. The y^μ and G are functions on a leaf of a matrix orbit. The text explicitly does not identify G or η with the emergent metric.
- No label change.

## Findings

**1. Minor (required).** Torsion paragraph, last sentence: "the invariants ρR[g_ρ], ρ g_ρ^{μν}∂lnρ∂lnρ and ρ²S² are linearly dependent".
- **Finding:** The dependence holds modulo total derivatives (through the identity's 2td term and 005's mod-td statement), not exactly.
- **Required action:** insert "modulo total derivatives" (see snippet).

**2. Minor (required).** Torsion paragraph, "With the classical teleparallel identity ..." and "one finds the exact pointwise identity". The proof imports the Weitzenböck identity without a citation.
- **Finding:** The text calls the step "classical", and the proposal itself says it was not looked up against a source. I verified it independently in the stated convention by an exact calculation (above), and the proposal's script does too. The manuscript should not rest on an uncited "classical" label, and no bib key exists.
- **Required action:** state it as "the identity for the Weitzenböck connection of a coframe, in the present index convention (checked by direct computation, not taken from a reference)". Do not invent a citation.

**3. Minor.** The sentence "The identity was also verified in exact rational arithmetic ..." is fine. Keep it as a check, not as the proof.

## Scope of what is established
- **"Proved" wording.**
  - "Proved" is not honest as a bare word.
  - Steps (i), (ii), (iv) and (v) are proved by hand.
  - Step (iii) is imported, but I confirmed it independently by an exact computation. It is an established standard identity but is not cited.
  - The accurate classification is: derived from the Weitzenböck identity, which is stated explicitly and verified by exact computation, and confirmed on 12 finite-amplitude cases.
  - The corrected LaTeX below uses "one finds" and "derived", not "proved all orders". That wording is acceptable.
- **Exact:**
  - Theorem 1, with hypotheses: real Θ, y^μ equal to four of the matrix coordinates, positive fibre average, nondegenerate Θ.
  - The 2m≥4 leaf-level no-go.
  - X=I_A and V=dlnρ.
  - The torsion identity for four matrix coordinates, with real nondegenerate Θ satisfying Jacobi.
  - The Lie–Poisson algebra and K=(M^{45}/R²)² η^{-1} on CP^{1,2}.
- **Conditional:** the heat-kernel factorisation and thresholds.
- **Open:**
  - the Einstein rank in the conjugate-coordinate class;
  - why y^μ=M^{μ5} are the base functions;
  - the Φ-to-coframe dictionary;
  - the transverse-scalar gap;
  - any G_eff value or sign.
- **Relaxable hypotheses for a within-core route:**
  - y^μ not matrices (the CP^{1,2} class);
  - non-positive measure or complex Θ;
  - dynamical fibre geometry.
- **Critical path:** A, B, C, D1, E, F, G-derived and N all remain OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. No label change.

## BREAKTHROUGH assessment
Not a breakthrough, and I am not flagging it.
- The torsion identity rewrites the existing term X as −2ρR[g_ρ]−ρ|∇lnρ|²+(3/2)ρ²S²+2td. It derives no heat-kernel coefficient, no G_eff, and no discharge of `ass:emergent-op`.
- It is a proved sub-lemma (given the verified Weitzenböck identity). It resolves 005's question about the η-using rewriting, but nothing on the critical path is derived from it.
- The no-go is a bounded M2 result, within the stated hypothesis class.

## Recommended disposition
Revise with the two minor corrections below, then integrate. No further full review is needed. Keeping claims 1–5 together is acceptable, since they share the Poisson-limit chain.

## Corrected snippet
No new physics is needed.

1. Replace the last sentence of the torsion paragraph's first block with:
```latex
At quadratic order about constant \(\bar\Theta\), for the perturbations of the Poisson class, the invariants \(\rho R[g_\rho]\), \(\rho\,g_\rho^{\mu\nu}\partial_\mu\ln\rho\,\partial_\nu\ln\rho\) and \(\rho^2S_{\lambda\mu\nu}S^{\lambda\mu\nu}\) are linearly dependent modulo total derivatives, so this decomposition does not alter the net coefficient \(1-N_{\mathrm{tot}}/24\) stated above.
```

2. Replace "With the classical teleparallel identity" by "With the identity for the Weitzenb\"ock connection of the coframe \(e\) (in the present index convention, checked by direct computation)". Leave the displayed formula unchanged.
