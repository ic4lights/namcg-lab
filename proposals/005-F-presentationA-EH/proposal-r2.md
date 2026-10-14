# Proposal 005-F-presentationA-EH, round 2

## Changelog against r1 (every review-r1 finding)

| Finding | Action in r2 |
|---|---|
| F1 (major, sign sentence) | Adopted the reviewer's replacement: the EH-type piece always has the positive-1/G sign (coefficient +N_tot/24 on the TT-type modes); the NET coefficient 1 - N_tot/24 of the Maxwell kernel M has it only for N_tot > 24; stated as a Maxwell-kernel coefficient on the gauge-built modes, not about G_eff. "rho^2 X has the opposite sign and dominates" for the connection sector alone kept. |
| F2 (major, X non-covariance, obstruction wording) | X is compared only with 2K dlnrho dlnrho in the block-family sentence, no non-covariance claimed from that. Result reclassified as a **conditional computation**, not an obstruction/no-go; all "obstruction", "M2" wording removed; milestone: none. The reviewer's observation (alpha = -4 reproduces X at quadratic order) is confirmed and investigated beyond quadratic order: new section 7 and scripts. Outcome: alpha = beta = -4 is forced by the quadratic data, and the **cubic order fails** (relative residual 0.32): X is not equal to any alpha rho R[g_rho] + beta rho\|grad ln rho\|^2 modulo total derivatives. The manuscript block now states this with its scope (sampled counterexample, listed candidate class). |
| F3 (major, N_tot) | Adopted: N_tot = N_s + 2 with N_s counting, with statistical sign, the real components whose fluctuation operator is O_s with the common cutoff; an input, not derived. The 32-component remark is removed from the manuscript block and kept only in this ledger text. |
| F4(a) | "At the sample points tested" now qualifies both clauses (rank six; no pure-gauge direction in the tangent space). |
| F4(b) | The closing reference to "the preceding scaffold-rotation paragraph" is replaced by a description. appH has no `\label` on that statement (grep: the only `lem:` use in appH is `lem:msigma`, unrelated; the manuscript does not name hypotheses "H1-H4"), so it is cited by what it says ("the scaffold-rotation statement above, which assumes a flat scaffold, a rotation-preserving regulator, an invariant vacuum and a composite-metric fluctuation that is a fixed linear image of Phi"). No new label is introduced. The r1 proposal's own "Lemma 2/H1-H4" shorthand is dropped from the manuscript text. |
| F4(c) | Symbol clash resolved: background components `Theta^{01}=a`, `Theta^{23}=b` are renamed `\vartheta_1(x^0,x^1)`, `\vartheta_2(x^2,x^3)` in the block; `a^mu` keeps the gauge potential. (The scripts keep their internal variable names; they are not manuscript text.) |
| F4(d) | "Euclidean" added where eigenvalue signs/values are quoted. |

Also re-verified: the insertion anchor (last sentence of the paragraph "What the two preceding results imply for Problem~F", `Presentation~A in general. No value or sign of \(G_{\mathrm{eff}}\)` / `follows. Problems~B, C, D and~F remain open.`, appH L1646-1648) occurs once; `\section{Problem G: HBEV}` occurs once (appH L1650); 003's text did not move them.

## Result

Target: Problem F, toward discharging Assumption `ass:emergent-op` by a within-core route not covered by the integrated scaffold-rotation statement (Presentation A, Poisson limit, kinetic metric and regulator built from Theta). **Everything is a conditional computation; nothing closes F, nothing is an obstruction or no-go.**

1. **Scalar sector (established algebra, conditional on the Poisson limit).** The Poisson-limit scalar operator O_s = -rho^-1 d(rho K d .) has the form eq:O-eta on G (G^{mu nu} = K^{mu nu}), with omega = -1/2 d ln rho; `sqrt|G|(R_G/6 - E) = rho R[g_rho]/6` pointwise for every Poisson Theta. Unchanged from r1.
2. **The Theta-built metric is a composite metric of Chapter 4 (established algebra).** G = eta_AB e^A e^B for the antisymmetric coframe e = eta^-1 Theta^-1; at the sample points tested the map Theta -> G has rank 6 and no linearized-diffeomorphism direction lies in its tangent space. The identification of <Phi>/v with this coframe is not derived. Unchanged from r1 with "sample points tested" qualifying both clauses.
3. **Connection sector (conditional computation).** In background gauge, `sqrt|G| tr(R_G/6 - E) = (4/6) rho R[g_rho] + rho^2 X`, X = eta^{rl} eta_{ma} eta_{nb} d_r Theta^{mn} d_l Theta^{ab}; with ghosts (2/6) rho R[g_rho] + rho^2 X. X has its derivative index contracted with the constant eta. On the block family X = 2K dlnrho dlnrho, i.e. rho^2 X = 2 rho |grad ln rho|^2_{g_rho}; at a generic Poisson bivector X differs from that one expression.
4. **Quadratic form about constant Theta-bar (conditional computation, Euclidean).** In units rho-bar^2 p_eta^2 relative to the tree-level Maxwell kernel M = q^2 eta - q q: X gives +1 (three modes); rho R[g_rho] gives -1/4 (two TT-type modes) and -3/4 (one mode with delta rho != 0). With N_tot = N_s + 2 (input count), the Euclidean Lambda^2 form is -(Lambda^2/32 pi^2) rho-bar^2 p_eta^2 (1 - N_tot/24) M on the TT-type modes and (1 - N_tot/8) M on the third. The EH-type piece alone always has the positive-1/G sign; the net Maxwell-kernel coefficient on the TT-type modes has it only for N_tot > 24; for the connection sector alone rho^2 X dominates with the opposite sign. This is a statement about a Maxwell-kernel coefficient on gauge-built modes, not about G_eff; both pieces are multiples of M by functions of p_eta^2, so they do not move the cone q^2 = 0.
5. **Position-dependent cutoff** (unchanged): coefficient of rho R[g_rho] becomes f(rho) rho; TT-type factor unchanged; third mode 1 - N_tot(2s+3)/24 for f = rho^s.
6. **New in r2: X is not a covariant term of the (g_rho, rho) family beyond quadratic order (sampled counterexample).** At quadratic order about constant Theta-bar, rho^2 X coincides with -4 rho R[g_rho] - 4 rho|grad ln rho|^2_{g_rho} (alpha = beta = -4 are forced by the data: the quadratic fit residual is 1e-15, and by the eigenvalues +1 vs -1/4, -1/4, -3/4 and 0, 0, 1/2). At cubic order, on the exact Darboux pullback class Theta = (psi^* omega-bar)^-1, psi = x + w, 40 random momentum-conserving plane-wave triples, both signatures, no pair of constants fits: relative residual 0.316 for the best fit and 0.317 at (-4,-4). Hence rho^2 X + 4 rho R[g_rho] + 4 rho|grad ln rho|^2 is not a total derivative, and every weight-rho two-derivative scalar density of (g_rho, rho) is a combination of these two modulo total derivatives. Consequence: the net EH coefficient is not obtained by reinterpreting X as a covariant term; the quadratic agreement is an accident of quadratic order. Scope: double-precision computation on random samples (a counterexample, not a symbolic proof); candidate class = diffeomorphism-covariant scalars of (g_rho, rho); covariance involving other tensors (e.g. eta) is not tested.

**Hypothesis class of the computation in items 3-6** (all must hold): Poisson-limit commutator (Moyal corrections dropped); bosonic 4D matrix Yang-Mills content (no fermions, no extra scalars, no mixing of Phi with a^mu); minimally coupled background-gauge fixing D_mu a^mu with eta contraction; off-shell Gaussian determinant; diagonal heat kernel with a local cutoff; Euclidean sign statements. Within-core relaxations: (i) fermionic/extra scalar content; (ii) Moyal corrections at the cutoff scale; (iii) non-minimal gauges with on-shell reduction; (iv) coupling of the internal index to a local frame (Presentation-B counterpart, bears on D1); (v) Phi-a^mu mixing on a non-central <Phi>. None is done here, and the computation excludes nothing beyond these hypotheses.

What is **not** shown: `ass:emergent-op` is not discharged (identification <Phi>/v = coframe not derived; Phi-a mixing and Moyal corrections not treated); the locked-block F target is not computed; no value or sign of G_eff follows; the matrix-to-dictionary map (A) is not derived.

## Target and status

- Problem F, `sec:status-F` (appH L1103-1127): **Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL.** "Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion." Missing step: specify the gauge-fixed fluctuation, Goldstone, diffeomorphism-ghost and local-Lorentz-ghost operators and weights, limits, continuation, finite-counterterm scheme; evaluate weighted a_1 and curvature-linear a_2.
- Chapter 17 (`sec:ch17-coeff`, `sec:ch17-done`): F "CRITICAL PATH; OPEN"; original target: weighted a_1 and curvature-linear a_2 on the **locked block**, including diffeomorphism and local-Lorentz ghosts and the radial threshold, with a scheme stated; completion item 6: G_eff not an input. Dependencies: D1, A, C, N.
- Critical-path set from `sec:ch17-done`: A, B, C, D1, E, F, G-derived, N (all OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL as recorded in F and A entries read; others by earlier reviews/ledger). No Chapter 17 / Appendix H discrepancy found for F.
- Classification of this proposal: **PROGRAMME-CONDITIONAL** (conditional computation on the form of `ass:emergent-op` in Presentation A). It does not meet the F original target.
- The ch17 sentence "The asserted net +2 from the on-shell TT count is not an off-shell heat-kernel trace" is not contradicted: the weight 4 - 2 = 2 here is an off-shell trace in a stated gauge for the Presentation-A matrix gauge sector only.

## Source reading

Digest + targeted reads (not a full scan); digest CURRENT (chapters-hash 196b7f142fde8bc9) per orchestrator. In r2 re-read: proposal-r1.md and review-r1.md in full; appH L1470-1650 (scaffold-metric paragraph, scaffold-rotation paragraph, "What the two preceding results imply"; anchors and absence of a Lemma label verified by grep); r1 reading list stands for the rest (appH F/A entries, ch03, ch04, ch08, ch17). No unreadable files. No full-scan trigger: the block adds a conditional paragraph and changes no definition, assumption, scope or status passage.

## Research and reasoning

Sections 0-6 of proposal-r1.md (setup, scalar sector, frame, connection sector, quadratic forms, `ass:emergent-op`/scaffold statement, literature) are unchanged except as listed in the changelog; the scripts of r1 were not modified. Revised or new points:

### 4'. Sign sentence (F1)
Per component of scalar type the TT-type eigenvalue contribution is c_s = (1/6)(-1/4)(-1) in the Euclidean form -(Lambda^2/32 pi^2) rho-bar^2 p_eta^2 [...]M, i.e. +1/24 each in the bracket with the same sign as the tree EH term; the bracket is 1 - N_tot/24 where "1" is X (opposite sign) and "-N_tot/24" the EH pieces. Hence the EH-type piece has the positive-1/G sign for every N_tot > 0, the net coefficient changes sign at N_tot = 24. N_tot = N_s + 2: the connection sector contributes net weight 2 on rho R/6 (4 connection components minus 2 for the ghost weight), and N_s counts real components with operator O_s and the same cutoff, signed by statistics. This is an input count. (Reviewer verified the arithmetic; unchanged.)

### 7. Can X be rewritten covariantly beyond quadratic order?
Question (reviewer's observation): is rho^2 X = alpha rho R[g_rho] + beta rho|grad ln rho|^2_{g_rho} + total derivative, for constants alpha, beta, on the Poisson class?

Candidate class. Modulo total derivatives, every diffeomorphism-covariant two-derivative scalar density of weight rho built from (g_rho, rho) is a combination of rho R and rho|grad ln rho|^2: with sqrt(g_rho) = 1, rho Box ln rho = d(rho g d ln rho) - rho|grad ln rho|^2, and the only scalar with two derivatives linear in curvature is R. The weight is forced by constant rescaling Theta -> lambda Theta: g_rho is invariant, rho -> lambda^-2 rho, rho^2 X -> lambda^-2 rho^2 X, so a term f(rho) R needs f proportional to rho.

Quadratic data. In units rho-bar^2 p_eta^2 relative to M on the quotient: X: (1,1,1); rho R: (-1/4,-1/4,-3/4); rho|grad ln rho|^2: (0,0,1/2) (computed by `check_X_covariant_sanity.py`). Matching requires alpha(-1/4) = 1, i.e. alpha = -4, and 1 = (-4)(-3/4) + beta/2, i.e. beta = -4. The unique candidate is alpha = beta = -4.

Test beyond quadratic order. Exact local parametrization of nondegenerate Poisson bivectors by Darboux pullback: omega := Theta^-1 = psi^* omega-bar, omega_{mn} = (d_m psi^a) omega-bar_ab (d_n psi^b), psi = x + w(x), w an arbitrary vector field. Take w = sum_j eps_j u_j exp(i p_j.x), eps_j^2 = 0, sum_j p_j = 0. Fields are stored as {subset of {1,2,3}: coefficient} with the exponential implicit (products of disjoint subsets, derivatives multiply by i P_subset), so arithmetic is exact apart from double precision. The eps_1 eps_2 eps_3 coefficient of a Lagrangian is x-independent and any total derivative has zero such coefficient. Computed: C_h, C_r, C_x of rho R[g_rho], rho|grad ln rho|^2, rho^2 X (g_rho^{mu nu} = rho K^{mu nu}, K = Theta^T eta Theta, rho = 1/Pf Theta, Christoffel/Riemann built from jets) for 40 random samples: random eta signature, background Theta-bar^{01}, Theta-bar^{23} from omega-bar entries (a,b) in [0.5, 2.5], integer momenta, random u_j.
- Quadratic (eps_1 eps_2, p_2 = -p_1): fit X = alpha h + beta r: alpha = beta = -4, relative residual 1.3e-15.
- Cubic: best fit (alpha, beta) = (-3.55, -3.19), relative residual 0.316; at (-4,-4), 0.317. 
- Machinery check (`check_X_covariant_sanity.py`): independent of the r1 scripts (pullback parametrization, complex jets), it reproduces the generalized eigenvalues (-3/4, -1/4, -1/4) of h relative to X on the quotient by q = omega-bar^-1 p (both signatures) and the exact gauge invariance B q = 0 for both forms.

Conclusion (classification: computed counterexample, double precision; not a symbolic proof): rho^2 X is not equal modulo total derivatives to any covariant combination in the candidate class; the quadratic agreement with -4 rho R - 4 rho|grad ln rho|^2 is specific to quadratic order. Therefore (a) the net EH coefficient is not obtained by reinterpreting X (the quadratic N_tot > 24 statement stays a Maxwell-kernel statement for these modes); (b) the Presentation-A connection-sector Lambda^2 density contains a piece outside the covariant (g_rho, rho) family, within the stated hypothesis class; (c) this does not exclude the route: other sector content, Moyal terms, gauges or Phi-a mixing may change the weight of X, and the sector sum is not computed. Scope caveat: only (g_rho, rho)-covariant candidates were tested; a rewriting with extra structure (e.g. a second metric built from eta) is not excluded and not needed for the claims.

Also not tested: whether the cubic part of X + 4 rho R + 4 rho|grad ln rho|^2 is a recognizable invariant (a cubic-order eta-dependent term); not pursued.

## Claim classification

| Claim | Class |
|---|---|
| L = D_mu D^mu = rho^-1 d(rho K d), Liouville, [D,D] = {Theta,.} | established identity |
| O_s = -D^2 + E on G with omega = -1/2 d ln rho; sqrt\|G\|(R_G/6 - E) = rho R[g_rho]/6 | established identity (hand proof; symbolic/numeric checks, re-verified by gatekeeper) |
| Lambda^2 coefficient -(Lambda^2/192 pi^2) int rho R[g_rho] per component | conditional (Poisson limit; truncated expansion of thm:Geff; constant Lambda; Euclid) |
| G = eta_AB e^A e^B for e = eta^-1 Theta^-1 | established identity |
| rank(Theta -> G) = 6; no diffeo direction in tangent space | computed at sample points tested; not proved generically |
| connection-sector trace: (4/6) rho R + rho^2 X (net 2/6 with ghosts) | established algebra given the stated quadratic action; hypothesis class as listed |
| quadratic action in background gauge from eq:Smatrix in the Poisson limit | conditional |
| eigenvalues +1, -1/4, -3/4, 0, 0, +1/2 (Euclid; units rho-bar^2 p_eta^2 relative to M) | computed (symbolic in p for six cases in r1; numerically re-derived in r2 by an independent code path) |
| EH-type piece always positive-1/G sign; net 1 - N_tot/24 changes sign at N_tot = 24 | conditional arithmetic on computed eigenvalues; N_tot an input count |
| f(rho) cutoff: TT unchanged, third mode 1 - N_tot(2s+3)/24 | conditional; TT part from delta rho = 0, third mode sampled |
| rho^2 X not equal to alpha rho R + beta rho\|grad ln rho\|^2 mod total derivatives at cubic order | computed counterexample (double precision, 40 random samples, both signatures); candidate class = (g_rho, rho)-covariant scalars |
| X covariant in some other sense (extra tensors) | unresolved / not tested |
| `ass:emergent-op` discharged; <Phi>/v = coframe | **unresolved** (not derived) |
| Moyal corrections, fermions, Phi-a mixing, locked-block ghosts, G_eff value or sign | **unresolved / not treated** |

## Proposed changes

Single file: `chapters/appH-microscopic-proofs.tex`. One new paragraph, nothing replaced or removed.

**Anchor.** Insert immediately after the paragraph "What the two preceding results imply for Problem~F (conditional; not closure).", whose last sentence is

> "... Presentation~A in general. No value or sign of \(G_{\mathrm{eff}}\) follows. Problems~B, C, D and~F remain open."

(occurs once, appH L1646-1648; grep re-run in r2), and before `\section{Problem G: HBEV}` (once, appH L1650). **Kept:** everything above the insertion point.

Labels referenced, each verified to occur once in `chapters/`: `rem:ch3-varying-theta`, `rem:ch3-trace-quadratic`, `thm:Geff`, `eq:O-eta`, `eq:W-expand`, `eq:g-from-e`, `eq:vev-is-frame`, `def:composite-metric`, `eq:Smatrix`, `ass:emergent-op`, `ch:vierbein-emergence`. `\LUV` is an existing macro in appH. No new label. Citation: none (the `Steinacker2010` citation of r1 was not used in the block). Please re-run the label grep (r1 verified the list; the reviewer confirmed it and `ch:vierbein-emergence`).

```latex
\paragraph{Presentation~A in the Poisson limit: the \(\Theta\)-built metric and the connection sector (conditional; not closure).}
Let \(\Theta^{\mu\nu}(x)\) be a nondegenerate Poisson bivector and
\(\rho=1/|\operatorname{Pf}\Theta|\), so that
\(\partial_\mu(\rho\,\Theta^{\mu\nu})=0\). Keep the leading
semiclassical order only:
\([\cdot,\cdot]\to i\{\cdot,\cdot\}\) with
\(\{f,g\}=\Theta^{\mu\nu}\partial_\mu f\,\partial_\nu g\),
\(\operatorname{Tr}\to\int\mathrm{d}^4x\,\rho\), and matrix-coordinate
indices contracted with \(\eta\). With
\(K^{\mu\nu}=\eta_{\alpha\beta}\Theta^{\alpha\mu}\Theta^{\beta\nu}\) and
\(g_\rho^{\mu\nu}=\rho K^{\mu\nu}\) as in
Remark~\ref{rem:ch3-varying-theta}, let \(G\) be the metric with
\(G^{\mu\nu}=K^{\mu\nu}\); then \(G=\rho\,g_\rho\),
\(|\det g_\rho|=1\) and \(\sqrt{|G|}=\rho^2\). Higher Moyal terms are
dropped. They are not small at momenta of order \(\LUV\), so the
coefficients below are those of the Poisson-limit operators within the
truncated expansion of Theorem~\ref{thm:Geff}. Signs and eigenvalues
refer to the Euclidean section \(\eta=\delta\); the algebraic identities
do not depend on the signature.

\emph{Scalar sector.} A real fluctuation whose kinetic term is the
Poisson limit of \(\operatorname{Tr}[\hat X_\mu,\varphi]^2\) has the
operator
\(\mathcal O_s=-\rho^{-1}\partial_\mu(\rho K^{\mu\nu}\partial_\nu\,\cdot\,)\).
On the metric \(G\) it has the form~\eqref{eq:O-eta}, with
\(D=\nabla+\omega\), \(\omega_\mu=-\tfrac12\partial_\mu\ln\rho\) and
\(E=-\tfrac12\Box_G\ln\rho
+\tfrac14G^{\mu\nu}\partial_\mu\ln\rho\,\partial_\nu\ln\rho\).
Since \(G=\rho\,g_\rho\) in four dimensions,
\(R_G=\rho^{-1}\bigl[R-3\Box_{g_\rho}\ln\rho
-\tfrac32|\nabla\ln\rho|^2_{g_\rho}\bigr]\) and
\(E=\rho^{-1}\bigl[-\tfrac12\Box_{g_\rho}\ln\rho
-\tfrac14|\nabla\ln\rho|^2_{g_\rho}\bigr]\), so that
\[
  \sqrt{|G|}\Bigl(\tfrac16R_G-E\Bigr)=\tfrac16\,\rho\,R[g_\rho]
\]
pointwise. For a constant \(\LUV\), one such component contributes
\(-\tfrac{\LUV^2}{192\pi^2}\int\mathrm{d}^4x\,\rho\,R[g_\rho]\)
to~\eqref{eq:W-expand}: the coefficient of
Theorem~\ref{thm:Geff}, multiplying the curvature of the
\(\Theta\)-built metric \(g_\rho\) with a factor \(\rho\). The
component is minimally coupled to \(g_\rho\).

\emph{Frame.} Let \(\omega=\Theta^{-1}\), \(\omega_{\mu B}\Theta^{B\nu}
=\delta_\mu{}^\nu\), and \(e^A{}_\mu=\eta^{AB}\omega_{\mu B}\). Then
\(G_{\mu\nu}=\eta_{AB}e^A{}_\mu e^B{}_\nu\), which is the
form~\eqref{eq:g-from-e} of Definition~\ref{def:composite-metric} for
a coframe with \(\eta_{AB}e^B{}_\mu\) antisymmetric in \((A,\mu)\).
At the sample points tested the map \(\Theta\mapsto G\) has rank six,
so that the \(\Theta\)-built metrics form a six-parameter subfamily of
the metrics, and no pure-gauge perturbation
\(p_{(\mu}\xi_{\nu)}\) of \(G\) lies in its tangent space. If
\(\langle\Phi\rangle/v\) of~\eqref{eq:vev-is-frame} were identified with
this coframe, the operator above would be that of
Assumption~\ref{ass:emergent-op} for the metric \(G\). This
identification is not derived.

\emph{Connection sector.} In background gauge with gauge-fixing term
\(\tfrac12\rho\,(D_\mu a^\mu)^2\), \(D^\mu=\{x^\mu,\cdot\}\), the part of
\eqref{eq:Smatrix} quadratic in the matrix gauge potential \(a^\mu\)
is, up to a constant factor,
\(\int\mathrm{d}^4x\,\rho\,[K^{\rho\sigma}\partial_\rho a_\nu\partial_\sigma a^\nu
-2a^\mu\{\Theta_{\mu\nu},a^\nu\}]\), the term linear in \(a^\mu\) not
being assumed to vanish. The ghost operator is
\(D_\mu D^\mu=-\mathcal O_s\), of weight \(-2\). The operator
\(\mathcal O_va^\mu=\mathcal O_sa^\mu
-2\eta^{\mu\alpha}\{\Theta_{\alpha\nu},a^\nu\}\) has the
form~\eqref{eq:O-eta} on \(G\) with
\(\omega_\sigma=-\tfrac12\partial_\sigma\ln\rho\,\mathbb I+\mathcal B_\sigma\),
\((\mathcal B^\sigma)^\mu{}_\nu=\eta^{\mu\alpha}\Theta^{\rho\sigma}
\partial_\rho\Theta_{\alpha\nu}\), and
\(E=\nabla_\sigma\omega^\sigma+\omega_\sigma\omega^\sigma\). Then
\[
  \sqrt{|G|}\operatorname{tr}\Bigl(\tfrac16R_G-E\Bigr)
  =\tfrac46\,\rho\,R[g_\rho]+\rho^2X,\qquad
  X=\eta^{\rho\lambda}\eta_{\mu\alpha}\eta_{\nu\beta}\,
    \partial_\rho\Theta^{\mu\nu}\,\partial_\lambda\Theta^{\alpha\beta},
\]
and with the ghosts the connection sector contributes
\(\tfrac26\rho R[g_\rho]+\rho^2X\). The derivative index of \(X\) is
contracted with \(\eta\) and not with \(G\). For
\(\Theta^{01}=\vartheta_1(x^0,x^1)\), \(\Theta^{23}=\vartheta_2(x^2,x^3)\)
one finds
\(X=2K^{\mu\nu}\partial_\mu\ln\rho\,\partial_\nu\ln\rho\); for a
generic Poisson bivector \(X\) differs from this one expression.

\emph{Quadratic form about constant \(\bar\Theta\).} Let
\(\Theta=\bar\Theta+\epsilon T\), \(T^{\mu\nu}
=\bar\Theta^{\mu\rho}\partial_\rho a^\nu-\bar\Theta^{\nu\rho}\partial_\rho a^\mu\),
\(a^\mu=u^\mu\cos(p\cdot x)\). With \(q^\mu=\bar\Theta^{\mu\rho}p_\rho\),
the phase-averaged second-order terms of \(\rho R[g_\rho]\) and
\(\rho^2X\) are quadratic forms on the three-dimensional quotient by
\(u\propto q\). Relative to the tree-level kernel
\(M=q^2\eta-qq\) of Remark~\ref{rem:ch3-trace-quadratic}, with
\(p_\eta^2=\eta^{\mu\nu}p_\mu p_\nu\) and
\(\bar\rho=1/|\operatorname{Pf}\bar\Theta|\), their Euclidean
eigenvalues are
\(\bar\rho^{2}p_\eta^2\) (three modes) for \(\rho^2X\), and
\(-\tfrac14\bar\rho^{2}p_\eta^2\) (two modes with \(\delta\rho=0\), for
which the linearized Einstein--Hilbert form of \(\delta g_\rho\) equals
that of its transverse-traceless part with respect to \(p\) and
\(\bar g_\rho\)) and \(-\tfrac34\bar\rho^{2}p_\eta^2\) (one mode with
\(\delta\rho\ne0\)) for \(\rho R[g_\rho]\). Let
\(N_{\mathrm{tot}}=N_s+2\), where \(N_s\) counts, with statistical
sign, the real components whose fluctuation operator is
\(\mathcal O_s\) with the same cutoff; it is an input, not a derived
count. In the Euclidean section the \(\LUV^2\) quadratic form is
\(-\tfrac{\LUV^2}{32\pi^2}\bar\rho^{2}p_\eta^2\,
(1-N_{\mathrm{tot}}/24)\,M\) on the two transverse-traceless-type
modes and \((1-N_{\mathrm{tot}}/8)\,M\) on the third. The net
coefficient on the two transverse-traceless-type modes has the sign of
a positive induced Einstein--Hilbert term only if
\(N_{\mathrm{tot}}>24\); the Einstein--Hilbert-type piece itself always
has that sign. For the connection sector alone, \(\rho^2X\) has the
opposite sign and dominates. This is a statement about the
Maxwell-kernel coefficient on these modes. Both pieces are multiples of
\(M\) by functions of \(p_\eta^2\), so they do not move the cone
\(q^2=0\), and about a constant background they do not fix
\(G_{\mathrm{eff}}\).

\emph{Beyond quadratic order.} Nondegenerate Poisson bivectors near
\(\bar\Theta\) are \(\Theta=(\psi^*\bar\omega)^{-1}\),
\(\bar\omega=\bar\Theta^{-1}\), \(\psi=x+w(x)\). Modulo total
derivatives, the scalar densities of weight \(\rho\) with two
derivatives built covariantly from \(g_\rho\) and \(\rho\) are the
combinations of \(\rho R[g_\rho]\) and
\(\rho\,g_\rho^{\mu\nu}\partial_\mu\ln\rho\,\partial_\nu\ln\rho\). At
quadratic order about constant \(\bar\Theta\), \(\rho^2X\) coincides
with \(-4\rho R[g_\rho]-4\rho\,g_\rho^{\mu\nu}\partial_\mu\ln\rho\,
\partial_\nu\ln\rho\) for the random backgrounds and both signatures
sampled. In a numerical test (double precision, \(w\) a sum of three
plane waves with \(\sum p_j=0\), forty random samples) the cubic
coefficient of \(\rho^2X\) is not of the form
\(c_1\rho R[g_\rho]+c_2\rho\,g_\rho^{\mu\nu}\partial_\mu\ln\rho\,
\partial_\nu\ln\rho\) for any constants (relative residual about
\(0.3\) for the best fit). So, on this sample, \(\rho^2X\) is not a
combination of these two covariant densities modulo total derivatives,
and the quadratic agreement does not extend. Rewritings that use
further structure, such as the constant \(\eta\), are not tested.

If \(\LUV^2\) is replaced by \(\LUV^2f(\rho)\) (a local proper-time
cutoff on the diagonal heat kernel), the coefficient of
\(R[g_\rho]\) becomes \(f(\rho)\rho\); with
\(\hat g=f\rho\,g_\rho\),
\(\int f\rho R[g_\rho]=\int\sqrt{\hat g}\,[\hat R
-\tfrac32\hat g^{\mu\nu}\partial_\mu\ln(f\rho)\partial_\nu\ln(f\rho)]\).
The factor on the two transverse-traceless-type modes is unchanged, and
for \(f=\rho^s\) the third becomes \(1-N_{\mathrm{tot}}(2s+3)/24\).

This is a computation for Poisson-limit operators of a bosonic
four-dimensional matrix gauge sector in a stated gauge, off shell or
about a constant background. It does not identify \(G\) with the
emergent metric of Chapter~\ref{ch:vierbein-emergence}, does not
treat Moyal corrections at the cutoff, fermionic or additional scalar
fields, the mixing of \(\Phi\) with \(a^\mu\), the locked-block
diffeomorphism and local-Lorentz ghosts, or the relation of the induced
term to the tree-level term of~\eqref{eq:Smatrix}, and gives no value or
sign of \(G_{\mathrm{eff}}\). The kinetic metric and regulator here
are built from \(\Theta\), and the map \(\Theta\mapsto G\) is nonlinear,
so the hypotheses of the scaffold-rotation statement above (a flat
scaffold, a rotation-preserving regulator, an invariant vacuum, and a
composite-metric fluctuation that is a fixed linear image of \(\Phi\))
do not apply; no linearized-diffeomorphism invariance is claimed.
Problems~B, C, D and~F remain open.
```

**Stale passages elsewhere:** none found that this block makes false (`rem:ch3-varying-theta` is consistent: Laplace type with drift connection, identity for R[g_rho]; appH "ties derivative indices to tangent indices" and the ch17 F missing step are not contradicted). Note for the integrator: the rank/pure-gauge qualifier "at the sample points tested" now covers both clauses.

## Verification scripts

All in `proposals/005-F-presentationA-EH/`; sympy 1.14.0 / numpy / Python 3.11. Checks, not proofs. The r1 scripts and outputs are unchanged (see proposal-r1.md table). New in r2:

| Script | Output | What it checked |
|---|---|---|
| `check_X_covariant_rewrite.py [nsamples]` | `check_X_covariant_rewrite.out.txt` | Exact multilinear plane-wave jets on the Darboux pullback class omega = psi^* omega-bar; least-squares X = alpha h + beta r (h = rho R[g_rho], r = rho\|grad ln rho\|^2, x = rho^2 X): quadratic order alpha = beta = -4, residual 1.3e-15; cubic order best fit (-3.55, -3.19), residual 0.316. Runs in about a second. (Its "td" entry, the cubic coefficient of the total derivative d_a(g^{ab} d_b rho), is zero by construction at zero total momentum; it only confirms the extraction.) |
| `check_X_covariant_sanity.py` | `check_X_covariant_sanity.out.txt` | Independent code path check: generalized eigenvalues of h relative to x on the quotient by q = omega-bar^-1 p are (-3/4,-1/4,-1/4) for both signatures (matching r1), B q = 0 exactly for both forms, eigenvalues of r relative to x are (0,0,1/2), cubic residual at fixed (-4,-4) is 0.317 |

Run from the proposal folder: `python check_X_covariant_rewrite.py 40`, `python check_X_covariant_sanity.py`.

## Decisions Taken

- **Follow the gatekeeper's X observation to a conclusion** (RESEARCHER-DECISION by directive): tested beyond quadratic order by exact multilinear jets on the full Poisson class rather than argue. Alternatives rejected: leaving it as an open caveat (uninformative for the full-GR derivation, since the sign of the net EH coefficient hinges on it); symbolic generic-Theta Euler-Lagrange comparison on the constrained Poisson class (heavy, adds nothing over a counterexample).
- **Candidate class** restricted to (g_rho, rho)-covariant scalars, justified by scaling and total derivatives; covariance with extra structure is left untested and stated as such.
- **Classification**: conditional computation, not an obstruction; milestone none; the "bounded obstruction" language removed everywhere.
- **No fundamental metric**: Theta, eta and G remain matrix-model objects; no route in this proposal makes spacetime fundamental.
- **Lemma citation**: by description because no label exists; no new label introduced.
- **No assumption label** for <Phi>/v = coframe; it stays an "if ... were identified" hypothetical. N_tot and the 32-component remark stay in the ledger, not in the manuscript.

## Milestone assessment

Routine (none). It is not M1: no critical-path step is derived from the matrix theory. It is not M2: nothing is excluded beyond the stated hypotheses, and the covariance test is a sampled counterexample within a listed candidate class, not a no-go for the route. No M3, M4, M5.

## Status-label recommendation

None. F, A, B, C, D1, E, G-derived and N stay OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL. No label edit appears in the LaTeX.

## Author decision needed

None.

## Remaining open step

To close the F original target and discharge `ass:emergent-op`: (1) derive <Phi>/v = coframe omega from the matrix theory (A, D1) or replace the assumption by a derived statement; (2) control Moyal corrections at p ~ Lambda_UV; (3) include the full IKKT-type content and the Phi-a mixing and determine whether X is cancelled or reweighted (the new covariance result shows X cannot be absorbed into the covariant EH coefficient, so its fate decides the net EH coefficient: this is now the sharpest sub-question; the fermionic/extra-scalar traces of the same Poisson-limit operators are the next computation); (4) non-minimal gauges with on-shell reduction and a comparison with the tree term, including the cubic-order structure that quadratic forms about a constant Theta-bar cannot probe; (5) locked-block diffeomorphism and local-Lorentz ghosts (D1); (6) Lorentzian continuation and the sign of X.

## Special instructions for the gatekeeper

- Do not accept: `ass:emergent-op` discharged; any value/sign of G_eff; that the route is excluded; that X is non-covariant in any sense beyond the stated candidate class (the block says "not tested" for rewritings using extra structure such as eta).
- Re-run `python check_X_covariant_rewrite.py 40` and `python check_X_covariant_sanity.py` (seconds). Check the parametrization: omega = (d psi)^T omega-bar (d psi) is closed and nondegenerate, so Theta is Poisson; the gauge direction is q = omega-bar^-1 p (the r1 sanity run with the wrong q is not in the delivered script). Check the claim that the eps_1 eps_2 eps_3 coefficient at zero total momentum kills all total derivatives, and that the candidate-class argument (scaling, rho Box ln rho identity) is complete for diffeomorphism-covariant scalars of (g_rho, rho).
- A float residual of 0.3 is far from rounding; if you want more assurance, any single sample with the printed `fit` demonstrates the failure, and you may vary the seed.
- The quadratic fit (-4,-4) is the reviewer's observation made exact.
- Anchors verified once; no label edits; no label changes proposed.
