# Proposal 030-subleading-symbol, round 1

## Result
Bounded no-go plus a conditional Einstein--Hilbert (EH) form limit for the next-to-leading symbol of the M_str term, +M_str Tr[chi (H_X - i0)^{-1}], in the 028 class (Poisson limit, one loop, CP^{1,2} four-matrix class, mu^2=-3, supplied IKKT content with no bilinear fermion mass, one species-independent Gaussian window of Delta_{3/4}, formal expansion). Nothing closes F or E.

1. **Reduction (established).** The order eps^2 q^4 sector (all derivatives on A) is computed with the first jet of T frozen and constant window symbol; window gradients and d^2T carry fewer q. There H_X = eta^{ab} Pi_a Pi_b, Pi_a = omega_a - eps alpha_a zeta sin(phi), [omega_a,phi] = -i kappa_a, zeta central. Weight-two resolvent symbol derived by left-symbol recursion (`nlo_symbol.py`, `expand_eps2.py`).
2. **Validation.** 1D heat-kernel coefficient and 2D Maxwell coefficient to 1e-11 (`validate_1d.py`); leading Hessian of 028 reproduced (ratios 1 +- 1e-6, `check_leading.py`); the non-degenerate case reproduces the Seeley-DeWitt a_1 = R/6 + E at second order, (4pi)^2 c1/<sqrt g a_1> = i to 12 digits (`validate_seeley_4d.py`; Fierz-Pauli normalisation checked on conformal metrics).
3. **Large-s structure (numerical, sampled).** K(s) = c0 + c1/s + ... (`nlo_scan.py`).
   - c0 is real and equals the Maxwell coefficient of the induced gauge field a_b = eps zeta alpha_b sin(phi): Q0 = lambda0 Gm, Gm = (kappa.kappa) eta - kappa kappa, residual <= 1e-14 (`tail_structure.py`, `maxwell_check.py`). It is gauge invariant, has the sign of the Gram determinant (indefinite), and its s-integral diverges linearly: the first-order mass term has no finite local coefficient at this order; the derivative expansion is non-uniform at small non-kernel momenta (a mass insertion into massless propagators).
   - c1 is purely imaginary; for the actual window it is not gauge invariant (violation 0.04-0.6), not covariant (fit residual 0.06-0.99), with eigenvalues of both signs.
4. **EH-form limit (conditional).** Scale by f the part of the window quadratic in omega_a, vertical block fixed. As f -> 0, Im c1 -> lambda1 A with parameter-free lambda1 = |det Lambda|^-1 (4pi)^-3 det(P'_kk)^-1/2 > 0, error O(f) (8e-4 ... 8e-5 relative at f=1e-3, `eh_limit.py`). A is the second variation of sqrt(g)(R/6 - (1/4)(grad lambda)^2) of the canonical base cometric gbar^{mu nu} = eta^{ab} W_a(y^mu) W_b(y^nu):
   A = (1/24)[ v^2((q.a)^2 - q^2 a^2) - 2 q^2 (a.v)^2 ] = EH part -(q^2/24)(a^2 v^2 - (a.v)^2) plus dilaton-gradient part -(1/8) q^2 (a.v)^2, with v = {phi,y} (q.v=0). It is gauge invariant under a -> a + lambda q (1e-16), nonzero and indefinite in general (positive on the 3-dimensional quotient only for q time-like, v space-like).
5. **Covariance.** theta^{mu nu} = {y^mu,y^nu} = M^{mu nu} and theta eta theta^T = c0 eta + y y - t t (exact, six points, `theta_structure.py`), so v^2 = c0 q^2 + (q.y)^2 - (q.t)^2: Lorentz violation through the time-like vector y^mu and the fibre vector t^mu. Haar-averaged over the fibre (`fibre_average.py`), A stays gauge invariant (1e-16) but is not proportional to q^2 eta - q q (remainder 0.8-1.0 of its norm), and its covariant part changes by a factor about 2 between rapidities 0 and 0.8 at fixed q.q. The window also singles out y; the check does not separate the two.

## Target and status
Problem F (OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL; treating G_eff as an input leaves F OPEN) and E (OPEN, CRITICAL PATH for the matrix-derived label), as in the 028 review; Chapter 17 critical path A, B, C, D1, E, F, G-derived, N unchanged (taken from the 028 review and the task statement, not re-derived from Chapter 17 in full this round). Original target of F: A, B, C, G_eff from the matrix theory. This is ranked avenue 2 of the 028 review. Class: PROGRAMME-CONDITIONAL bounded no-go. No label affected.

## Source reading
Digest + targeted reads: 028 proposal-r2/review-r2, SME scout `sme-scout-second-variation-20261017.md`, appH lines 2040-2150 (018-028 blocks), 028 geometry scripts (copied into this folder). Anchor `\section{Problem G: HBEV}` unique at line 2150 of the working tree; the accepted 029 block lies in sec:status-B, elsewhere. Not a full scan.

## Research and reasoning
Derivative counting: with A = eps alpha cos(q.y), delta w_a = -eps sin(phi) alpha_a Y, Y = O(q); each x-derivative gives q or kappa. The q^4 eps^2 part comes only from x-derivatives on A, hence the frozen sector. With a constant window symbol, chi o r = chi r plus total x-derivatives. Left-symbol recursion in omega'_a = omega_a - eps zeta alpha_a S, D_xi = kappa.d/d omega; weight 2:
p2 r2 + p1 r1 + (D p2)(-i d_phi r1) + (1/2)(D^2 p2)(-d_phi^2 r0) = 0, p1 = i eps (alpha.kappa) zeta cos(phi).
Then the eps^2 expansion, phi average, Gaussian moments by Isserlis with covariance (P + i s G0)^-1/2 (G0 = sum eta_a W_a W_a^T), real s, determinant branch by continuity.
Interpretation: kernel momenta xi_k are charges, a_b = eps zeta alpha_b sin(phi) a gauge field, the tetrad change a metric; c0 is the a_2 (F^2) heat-kernel term, c1 contains a_1 plus window-dependent corrections of relative order P/s (controlled decoupled KK model: the residual of the EH + Maxwell fit falls linearly with the horizontal window scale, `controlled_kk.py`, `controlled_kk_scan.py`).
Pauli-Sakharov remark (conjecture): at the a_1 level only the common operator survives (traceless Sigma), so with masses kept non-perturbatively the coefficient would be a_1 (M_str ln Lambda^2 - sum w d m ln m), the structure of Visser eq. 36 (read in 028); for mu^2 = -3, mu_i^2 = 2 the sum is 12(ln(2/3) + i pi) with the -i0 branch. Not derived for the hypoelliptic operator.
Literature: Steinacker arXiv:2303.08012 (key Steinacker2023 already in bib): Sec 7.1.2 after Eq. (7.13), the contraction "is not Lorentz invariant a priori, reflecting the presence of a time-like vector field on the FLRW space-time"; Sec 7.2.1, "the latter is not Lorentz invariant, and should be suppressed to obtain a reasonable gravity theory" (from an ar5iv fetch summary; equation numbers as reported, not independently re-checked). The y y - t t structure here is a derived analogue; no equation-level match is claimed. Not cited in the LaTeX.

## Claim classification
- Frozen-sector reduction and symbol recursion: established (three independent checks).
- c0 = Maxwell term and its linear divergence: established numerically (sampled; tensor identity 1e-14).
- c1 imaginary, non-invariant, indefinite for the actual window: numerical, sampled.
- f -> 0 limit equals lambda1 A: numerical (error O(f)); A analytic FP form: established algebra.
- theta theta^T identity: established numerically (six points, 1e-15).
- Fibre-average non-covariance: numerical, one base point, 300 Haar points.
- Pauli-Sakharov completion: conjecture. Sign of G_eff, map to the emergent metric: unresolved.

## Proposed changes
File chapters/appH-microscopic-proofs.tex, immediately before `\section{Problem G: HBEV}` (unique; after the 028 block whose last sentence is "This changes no ledger label; Problem~F remains open."). Label used: ch:vierbein-emergence (exists). No cite, no bib. Scratch-copy compile check outside the repo: 0 errors, 0 undefined, 0 multiply defined, 291 pages (`compile_check_r1.out.txt`). Block identical to `block-r1.tex`:

```latex
\paragraph{Conjugate-coordinate class: the next-to-leading symbol of the mass-supertrace term at order \(\epsilon^2\) (conditional; bounded no-go with a conditional Einstein--Hilbert-form limit).}
Keep the setting of the preceding paragraph and the term \(+M_{\mathrm{str}}\operatorname{Tr}[\chi\,(H_X-\mathrm i0)^{-1}]\), \(H_X=-\Box_X\). Take \(A^a=\epsilon\alpha^a\cos\phi\), \(\phi=q\cdot y\), \(W_a\) the Hamiltonian field of \(T^a\), \(Y=q_\mu\{y^\mu,\cdot\}\), \(\kappa_a=W_a(\phi)\) (so \(Y(\phi)=0\)) and the Gaussian window of \(\Delta_{3/4}\). Terms of fourth order in \(q\) at order \(\epsilon^2\) contain all derivatives on \(A\); they are computed with the first jet of \(T\) frozen and the window symbol constant, since window gradients and \(\partial^2T\) carry fewer powers of \(q\) (derivative counting; the window symbol being constant makes the composition terms with \(\chi\) total derivatives). In this sector \(H_X=\eta^{ab}\Pi_a\Pi_b\), \(\Pi_a=\omega_a-\epsilon\alpha_a\zeta\sin\phi\), \(\omega_a=\xi(W_a)\), \(\zeta=\xi(Y)\), \([\omega_a,\phi]=-\mathrm i\kappa_a\), with \(\zeta\) commuting with everything.

\emph{Symbol and checks.} The weight-two symbol of the resolvent was derived by the left-symbol recursion, expanded to \(\epsilon^2\) and averaged over \(\phi\) (the weight-one terms average to zero). It reproduces (a) the one-dimensional coefficient \(-\tfrac1{12}V'^2\) and the two-dimensional Maxwell coefficient \(-\tfrac1{12}F_{ab}F^{ab}\) to \(10^{-11}\); (b) the leading-symbol Hessian of the preceding paragraph; (c) in the non-degenerate case, with the vector fields divergence free, the Seeley--DeWitt coefficient \(\sqrt{|g|}(R/6-\tfrac14(\nabla\lambda)^2)\), \(\lambda=\ln\sqrt{|g|}\), at second order (Fierz--Pauli form), with relative phase \(\mathrm i\) to \(12\) digits.

\emph{Result in the class.} The integrand \(K(s)\) of the proper time \(s\) is finite at small \(s\) and has at large \(s\) the form \(c_0+c_1/s+O(s^{-2})\), checked at orbit points with random \(q,\alpha\). (i) \(c_0\) is real and is the Maxwell coefficient of the gauge field \(a_b=\epsilon\zeta\alpha_b\sin\phi\) induced by the kernel momenta: \(c_0=\lambda_0\,G(\alpha)\) with \(G=(\kappa\cdot\kappa)(\alpha\cdot\alpha)-(\kappa\cdot\alpha)^2\) (agreement to \(10^{-14}\) in the tensor, \(\lambda_0>0\) at all sampled points). It is gauge invariant (\(\alpha\propto\kappa\)), of the sign of \(G\), which is indefinite in Lorentzian signature, and the integral \(\int^{s_{\max}}\mathrm ds\,c_0\) diverges linearly: the first-order mass term has no finite local coefficient at this order, and the derivative expansion is not uniform at small \(\xi\) of the non-kernel directions. (ii) \(c_1\) is purely imaginary and, for the window of \(\Delta_{3/4}\) at the sampled points, is neither invariant under \(\alpha\to\alpha+\lambda\kappa\) (relative violation \(0.04\)--\(0.6\)) nor of covariant form, and has eigenvalues of both signs. (iii) Let \(V'\) be the vertical tangent space (common kernel of the \(\mathrm dy^\mu\)) and scale by \(f\) the part of the window quadratic form in \(\omega_a\) in the splitting \(\xi\mapsto(\xi(W_a),\xi(v_k))\). As \(f\to0\), \(c_1\to\mathrm i\lambda_1 A\) with \(\lambda_1=|\det\Lambda|^{-1}(4\pi)^{-3}\det(P'_{kk})^{-1/2}>0\) (\(\Lambda\) the matrix of the splitting, \(P'_{kk}\) the vertical block of the window form) and no free parameter; the difference is \(O(f)\) at four orbit points (relative \(8\cdot10^{-4}\), \(1.4\cdot10^{-3}\), \(7\cdot10^{-4}\), \(8\cdot10^{-5}\) at \(f=10^{-3}\)). Here, with the base cometric \(\bar g^{\mu\nu}=\eta^{ab}W_a(y^\mu)W_b(y^\nu)\), \(h^{\mu\nu}\) its first-order change \(-\sin\phi\,(u^\mu v^\nu+v^\mu u^\nu)\), \(u^\mu=\eta^{ab}\alpha_aW_b(y^\mu)\), \(v^\mu=\{\phi,y^\mu\}\) (so \(q\cdot v=0\)) and \(a_\mu=\bar g_{\mu\nu}u^\nu\),
\[
A=\tfrac1{24}\Bigl[v^2\bigl((q\cdot a)^2-q^2a^2\bigr)-2q^2(a\cdot v)^2\Bigr],
\]
the sum of the Einstein--Hilbert second variation \(\tfrac16\,\mathrm{FP}[h]=-\tfrac{q^2}{24}\bigl(a^2v^2-(a\cdot v)^2\bigr)\) and the dilaton-gradient term \(-\tfrac18q^2(a\cdot v)^2\) of the Liouville measure. \(A\) is invariant under \(a\to a+\lambda q\) (checked to \(10^{-16}\)), vanishes only on that direction, and is indefinite in general (definite only for \(q\) time-like and \(v\) space-like, where it is positive). (iv) The base two-form \(\theta^{\mu\nu}=\{y^\mu,y^\nu\}=M^{\mu\nu}\) satisfies \(\theta^{\rho\mu}\eta_{\mu\nu}\theta^{\sigma\nu}=c_0\eta^{\rho\sigma}+y^\rho y^\sigma-t^\rho t^\sigma\), \(y^\mu=M^{\mu5}\), \(t^\mu=M^{\mu4}\) (exact at six points), so \(v^2=c_0q^2+(q\cdot y)^2-(q\cdot t)^2\) depends on the time-like vector \(y^\mu\) and on the fibre point. After a Haar average over the fibre at a base point with \(y^i=0\), the \(A\)-form (weighted by the Liouville density and \(\lambda_1\)) remains gauge invariant but is not proportional to \(q^2\eta_{ab}-q_aq_b\) (remainder \(0.8\)--\(1\) of its norm), and its covariant part changes by a factor \(2\) between boosts of rapidity \(0\) and \(0.8\) at fixed \(q\cdot q\). The window and the leaf both single out \(y^\mu\), which this check does not separate.

\emph{What is not shown.} The Pauli--Sakharov completion (the term \(M_{\mathrm{str}}\) multiplying the logarithm of the cutoff is accompanied by \(-\sum_iw_id_im_i\ln m_i\) when the masses are kept non-perturbatively) is expected from the Euclidean heat-kernel structure and is not derived for this hypoelliptic operator. The background flux, which cuts off large \(s\) in the full leaf, is not included, so the divergence in (i) is not resolved.

This is a statement for the Poisson limit, one loop, the term linear in the masses, the order \(\epsilon^2q^4\) with the first jet frozen, the supplied content with no bilinear fermion mass, the Gaussian window of \(\Delta_{3/4}\), and numerical sampling; the limit in (iii) is a limit of the window family and not the window of the class. It identifies no induced form with the emergent metric of Chapter~\ref{ch:vierbein-emergence}, makes no Wick-rotation claim, and gives no value or sign of \(G_{\mathrm{eff}}\). This changes no ledger label; Problem~F remains open.
```

Stale passages: the 028 sentence that the value in the six-dimensional leaf "requires the next-to-leading symbol and is not computed" remains true for the full leaf; the new block treats the frozen q^4 sector only.

## Verification scripts
`nlo_symbol.py` (recursion), `expand_eps2.py` (eps^2 and phase mean), `gauss_tools.py`, `tail_coeffs.py`, `validate_1d.py`, `check_leading.py`, `validate_seeley_4d.py`, `nlo_scan.py`, `maxwell_check.py`, `tail_structure.py`, `controlled_kk.py`, `controlled_kk_scan.py`, `eh_decomposition.py`, `eh_limit.py`, `theta_structure.py`, `fibre_average.py`, `compile_check_r1.py`, with outputs `*.out.txt`; geometry copies `cp12_realisation.py`, `symbol_tools.py`, `sym_signatures.py`, `geom28.py`. `validate_1d.out.txt` has IntegrationWarning lines filtered. Run with `python -B`. `controlled_kk.out.txt` and `expand_eps2.out.txt` may need re-running if absent.

## Decisions Taken
- The q^4 eps^2 sector with frozen first jet is "the EH-form term" (derivative counting); the log coefficient is the 1/s tail, with no ad hoc cutoff.
- The EH form is reported only as a window-limit statement and is not identified with the emergent metric.
- The Pauli-Sakharov completion stays out of the LaTeX as unproved.
- Rejected: any sign for G_eff; any Wick-rotation claim.

## Milestone assessment
Not a breakthrough. A useful conditional structural result: it locates the EH-form content (canonical base cometric plus dilaton term, gauge invariant) and shows it is masked by an IR-divergent Maxwell term and window artefacts. No trigger claimed.

## Status-label recommendation
None. F, E and all critical-path labels unchanged.

## Author decision needed
none

## Remaining open step (ranked avenues)
No-go class: Poisson limit, one loop, first-order mass term, frozen first jet, Gaussian window of Delta_{3/4}, no bilinear fermion mass.
1. Background-flux (Landau/nilpotent) resummation as the IR cutoff of the c0 divergence: relaxes first-order mass expansion and frozen background; needs a quadratic-X model with Mehler kernel at eps^2.
2. Non-perturbative masses: derive the Pauli-Sakharov completion for the hypoelliptic operator, including the tachyonic mu^2 branch.
3. A gauge/diffeo-covariant window (built from X, or the compact fibre bound) to remove the window artefacts.
4. Fermion mass patterns (M_str = 4mu^2 + 6mu_i^2 - 8m_F): M_str = 0 plane, sign of the log-weighted sum.
5. Transverse flux K (Steinacker mixed term): outside the class.
6. Exact second-order (non-expanded in q) Hessian of the frozen sector, to display the non-analytic q-dependence.
Afterwards: map to the emergent metric and a derivation of the matrix content.

## Special instructions for the gatekeeper
- The block claims: tail structure of the finite-s integrand, Maxwell identification of c0 (numerical), non-invariance of c1 for the actual window, an f -> 0 window limit equal to lambda1 A, the theta theta^T identity, fibre-average non-covariance. It claims no sign of G_eff, no emergent-metric identification, no finite coefficient.
- Re-run `validate_seeley_4d.py` (end-to-end check) and `eh_limit.py`; the sector definition (frozen first jet, constant window symbol) is the key hypothesis.
- The fibre average uses one base point; the Steinacker quotes come from a fetch summary.
