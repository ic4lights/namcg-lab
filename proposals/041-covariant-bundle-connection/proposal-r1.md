# Proposal 041-covariant-bundle-connection, round 1

## Result

Question (rank-1 open avenue H1 of integrated 039): does the matrix model itself supply a covariant bundle connection for the fluctuation operator of the connection sector, so that the term kappa_X rho^2 X (and with it the B residue c_A - c_T^ext = 2) is removed or changed?

Answer, within the Poisson limit, four matrix coordinates, alpha = 1, one loop, and for the bosonic connection sector only:

1. **No rotation connection on the matrix index.** The Poisson composite connection of the vector operator is B_{c|ab} = w_{a|cb} - w_{b|ca}, the Levi-Civita spin connection of the Theta-built coframe with the form index and one frame index exchanged (exact; independent numerical check 1e-15). Its inhomogeneous rotation law is the exchanged one, so B is not a connection for local rotations of the index, and no choice of Stueckelberg field acting on the index by a local similarity changes any local heat-kernel invariant of the operator (similarity invariance of the heat-kernel diagonal). The extremised frame of 039 is not a matrix background (for generic constant omega-bar no nonzero first-order rotation keeps eta e antisymmetric). Hypothesis class of this no-go: Hessian of the matrix action, fluctuation variables a^mu with the matrix index contracted by eta, rotations implemented as a local similarity or as e -> Lambda e inside the density, Poisson limit.

2. **A covariant description exists in other variables (the relaxation of the presentation hypothesis).** Fluctuations of the embedding functions are exact variations of the symplectic form, delta omega = dA with A_nu = a^mu omega_{mu nu}, and the matrix Lagrangian L(omega) = rho eta eta Theta Theta is an algebraic function of the six components of omega. Hence, up to a term proportional to the tree-level equation J, the Hessian is a generalised Maxwell operator in A, with constitutive tensor exactly (rational arithmetic) 2 M_G + b E: Maxwell in the Theta-built metric G with weight rho, plus an axion coupling b eps FF, theta = rho b a pseudoscalar. At points with J = dJ = 0 the matrix vector operator, transformed by (S a)_nu = a^mu omega_{mu nu}, coincides coefficient by coefficient (principal, first-order, zeroth-order) with the covariant Maxwell-axion operator in rho-weighted Lorenz gauge; the mismatch is linear in J and dJ. In these variables the field has no frame index: the bundle is T*M with the Levi-Civita connection of G. This is diffeomorphism covariance acting on (G, rho, theta); it is not a local Lorentz symmetry.

3. **Effect on X and the B residue.** For the covariant operator a_1 = -R/3 + box ln rho - |V|^2 + 6 s |d theta - theta V|^2 (V = d ln rho, s = +1 Euclid, -1 Lorentz), derived analytically and confirmed numerically; on the stationary set it equals a_1(O_v), so rho^2 X = rho^2 [-R - box ln rho + 6 s |d theta - theta V|^2] there. The six invariants (R, V^2, box ln rho and the three components of |U|^2) obey exactly one relation on the stationary set, s|U|^2 = -R/2 + V^2 - (3/2) box ln rho (numerical, residual 6e-12), so X = -4R + 6V^2 - 10 box ln rho as well. Consequently the Noether coefficient r (coefficient of R in X) is -1 if the gradient of theta is kept as an independent invariant and -4 if it is eliminated; -4 is the on-mode value of the merged normalisation paragraph; the dressed value -2 of 039 (a stipulation) corresponds to neither. At n_D = 0 the fixed-state residue is c_A - c_W = -r = 1 or 4 (merged: 4; 039 conditional: 2). The vector holonomy contact of the merged text has modulus 1. **X does not drop and the residue does not close**: covariance does not fix r; it moves the undetermined quantity from "frame non-invariance of X" to "which of G, rho, theta are held fixed under the variation of the first law" (in the class all three are functions of Theta). This is a sharper location of the missing ingredient (an Iyer-Wald/Noether charge for the constrained class), not a derivation.

4. **Bearing on F.** In the conjugate-coordinate class the Zeeman-dressed vector operator is exactly a total-Lorentz-spin Casimir operator, H_V = -C_41 + C_31^tot - C_V with C_V = -3 (exact polynomial arithmetic). A covariant bundle connection is therefore present there, and the y^mu dependence of A, F1, F2 is not a missing connection: F1 depends on y only through the scalar y^mu y_mu = -ell^2 - (y^4)^2, F2 = kappa^2 (alpha.y)^2 is the only term containing y as a vector, and no point of the Lorentzian leaf is fixed by the matrix Lorentz group ((y^0)^2 >= ell^2). The compact so(6) form has such points. No finite covariant Einstein-Hilbert coefficient results.

5. **Bearing on D.** The bosonic connection sector needs no local Lorentz symmetry for covariance in Moser variables; the Dirac operator gamma^A D_A equals gamma^A e_A^nu d_nu (frame derivative, no spin connection) and is not shown to be covariant, so the spinor sector is where the local-rotation question remains. No local Lorentz symmetry is derived.

Nothing here closes B, D or F. Classification: conditional structural results; one PRIOR-CLAIM qualification (below, soft).

## Target and status

Quoted from the current manuscript (Appendix H ledger; Chapter 17):

- Problem B: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived." Chapter 17: "CRITICAL PATH; OPEN. The fixed-algebra first-law identity is established, but not the required stationarity." Original target: derive delta S_D = 0 at fixed volume from the microscopic action, with the area term and a specified map g^(0) -> g; the sub-target of the 036-039 blocks is the comparison G_T = G_A.
- Problem D: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: D2 ... D remains OPEN and the matrix-derived criterion is unmet." Chapter 17 D1 requires local Lorentz gauge symmetry from the matrix algebra and condensate and the omega, A_mu, B and ghost operators specified.
- Problem F: CRITICAL PATH; OPEN ("The conditional heat-kernel identity does not compute the physical coupling").
- Chapter 17 matrix-derived set: A, B, C, D1, E, F, G-derived, N (unchanged). No discrepancy found between Appendix H and Chapter 17 for B, D, F.
- Completion of this package: PROGRAMME-CONDITIONAL; nothing DERIVED at the level of the original targets. No label change is proposed.

## Source reading

Digest (`scratch/digest.md`, status "dirty-chapters: yes") plus targeted reads in full (CLAUDE.md rule 3(d)): appH Problem B entry (L41-98), the replica/normalisation/gauge/fermion/Lichnerowicz/contact/logarithmic paragraphs (L100-341, including the 036-039 blocks), Problem D head (L508-543), the Presentation-A Poisson-limit paragraphs of Problem F (L1852-2048), the conjugate-coordinate paragraphs (L2109-2306, including the 032/034/040 blocks), ch10 Lorentz locking (L40-208) and the Chapter 17 B, D, F passages. Also read: 039 review-r1 (the rank-1 avenue), 039 scripts s6 and tj.py (reused), the avenue-5 lines of 040 proposal-r1/r2 and review-r2 (targeted). Not read in full: appH L545-1290 (D-section middle), L1308-1850 (F-section middle), the rest of Chapter 17, appendices other than H. This is "digest + targeted reads", not a full scan. No unreadable files.

## Research and reasoning

Conventions: signature (-,+,+,+) for the Lorentzian check; "Euclid" means eta = delta. G is the Theta-built operator metric G^{mu nu} = eta_{ab} Theta^{a mu} Theta^{b nu}; it is not identified with the emergent metric (Assumption emergent-op). a_1 = tr(E + R/6) is Gilkey's sign for O = -(nabla^2 + E), equal to the manuscript's tr(R/6 - E) with E_man = -E (validated: the routine reproduces sqrt(G) a_1 = rho R[g_rho]/6 for the scalar and (4/6) rho R[g_rho] + rho^2 X for O_v pointwise, s5).

### 1. The composite connection (s1)
B^s_{an} = Theta^{rs} d_r Theta_{an} is, in frame components, minus the torsion with its form index first (039 s6). Since de^A = -w^A_B ^ e^B for the Levi-Civita spin connection w, T^a_{cb} = -w_c^a_b + w_b^a_c, hence B_{c|ab} = w_{a|cb} - w_{b|ca} (analytic). s1 checks it against w computed independently from the metric Christoffels, at random class jets (8 draws) and random non-class coframes (2): residual <= 4e-15. Under e -> (1 + eps lam) e the finite-difference shifts are dw = -d_c lam_{ab} and dB = -(d_a lam_{cb} - d_b lam_{ca}) (fits 1e-12), and dB = cross(dw). A connection would shift by d_c lam_{ab}: residual 0.6-1.0.

### 2. Similarity invariance and the dressing (s10, s8)
For any invertible local S(x), tr K_s(x,x) of S O S^{-1} equals that of O (kernel conjugated, trace invariant), hence a_1 pointwise. s10: a_1(O_v) = a_1(S O_v S^{-1}) to 1e-14 at four generic jets. A Stueckelberg field Lambda acting on the matrix index of a^mu through Lambda a is such a similarity: no effect. The 039 dressing e -> Lambda e inside the density replaces B by B[Lambda e], which is not a similarity. s8: about generic constant omega-bar (both signatures, 12 draws) the linear map lam -> {omega-bar eta^-1 lam + lam eta^-1 omega-bar} has trivial kernel, so no nonzero first-order local rotation preserves the class "eta e antisymmetric"; in particular the Goldstone-extremised lam (which exists, rank 3 of the shift map, and removes S) leaves the class. For (anti)self-dual omega-bar a two-dimensional family may stay inside (not tested here).

### 3. Moser variables (s2, s2c)
Leaf-form argument: let X: M -> R^4 be a local diffeomorphism of the symplectic leaf (M, omega_M), y = X(m). Then {X^a, X^b} = Theta_X^{ab}(y) with Theta_X = (omega_X)^{-1}, omega_X = (X^-1)^* omega_M, and the leaf volume is |Pf omega_X| d^4y. So S[X] = int d^4y L(omega_X), L(omega) = |Pf omega| eta_{ac} eta_{bd} Theta^{ab} Theta^{cd}. For X close to the identity, omega_X - omega_M is exact (homotopy formula): omega_X = omega + dA_1 + dA_2 + ..., A_1,nu = a^mu omega_{mu nu} (sign convention immaterial). Then S = S_0[omega] + S_0'[dA_1 + dA_2] + (1/2) S_0''[dA_1, dA_1] + O(a^3). The linear term is -int A.(d dL/domega), and the stationarity of S_0 under all exact variations is the matrix equation (the map a -> A is invertible), i.e. J = 0. So on J = 0 the quadratic action is (1/2) S_0'', an algebraic bilinear form in F = dA_1 with the 6x6 matrix H = d^2 L/d omega d omega. s2 (finite differences, 1e-7) and s2c (sympy, exact rational, three points per signature) give H = 2 M_G + b E with M_G[I,J] = 2 rho (G^{ac}G^{bd} - G^{ad}G^{bc}), E[I,J] = 8 eps_{abcd}, b = -sgn(Pf Theta) I1/8, I1 = eta_{ac} eta_{bd} Theta^{ab} Theta^{cd}. [Not proved for all omega; exact at the sampled rational points.] Gauge function: D_mu a^mu = -rho^-1 d_nu(rho G^{nu lam} A_lam), by d_nu(rho Theta^{nu a}) = 0 (checked 4e-16).

### 4. Operator identity (s3, s3b, s3c, s14)
Coefficients of O = -(G^{st} d_s d_t + a^s d_s + b) at x = 0, extracted by applying the operators to test polynomials, for (V) S O_v S^{-1} and (M) (4 rho)^-1 G_{lam nu} P^nu, P^nu = delta S_2/delta A_nu (Maxwell-axion from H) plus the rho-weighted Lorenz gauge function with the Feynman constant fixed by the symbol. Generic jets (J != 0): principal parts agree (1e-15), first- and zeroth-order do not (s3). On J(0) = dJ(0) = 0 jets (20 conditions solved by least squares/linear solve): first-order coefficients agree to 1e-15 (six draws, both signatures), principal to 1e-13, and b vanishes on both sides (s3b). s3c: starting from a stationary jet and moving along a random direction by t, |a_V - a_M| = 19 |J(0)| and |b_V - b_M| = 1.9 |dJ(0)| across t = 1e-3...3e-2 (linear, to the printed digits). s14: J^nu = rho^-1 d_mu(rho G^{mu nu}) equals eta^{-1} times the lowered D^mu Theta_{mu nu} (residual 1e-16), i.e. it is the matrix equation. [Numerical; sampled jets.]

### 5. The covariant a_1 (s11, s11b, s6, s6b, s6c)
Maxwell with dilaton e^-phi = 1/rho (phi = ln rho): O A_lam = -nabla^mu F_{mu lam} + V^mu F_{mu lam} - nabla_lam Xi, Xi = nabla.A - V.A. Using nabla^mu F_{mu lam} = nabla^2 A_lam - nabla_lam nabla.A - R_{lam sigma} A^sigma, O = -nabla^2 + V^mu nabla_mu + (Ric + nabla V), so omega_sigma = -V_sigma/2 and E_G = -(Ric + nabla V) - nabla.omega - omega^2, tr E_G = -R + box ln rho - V^2 and a_1^MD = -R/3 + box ln rho - V^2. s11: the numerical a_1 of the operator built from 2 M_G alone equals this to 8 digits at generic jets (six draws, both signatures; no stationarity needed because the operator is covariant for every G, rho). The axion term adds a first-order piece O_ax A_lam = -2 eps^mu_lam^{cd} U_mu nabla_c A_d, U = d theta - theta V (theta = rho b), traceless connection omega_ax = eps U; tr omega_ax^2 = -6 s|U|^2 and cross terms with the dilaton connection vanish, so a_1 = a_1^MD + 6 s |U|^2. s11b: the axion part divided by 6 s|U|^2 is 1.0000 (Euclid) and -1.0000 (Lorentz) at three jets per signature (agreement of the printed values to 6 digits). s6b/s6c: on 14 stationary jets per signature, a_1(V) = a_1(M) to 1.2e-12 and both equal the covariant formula to 3e-11. Combined with sqrt(G) a_1 = (4/6) rho R[g_rho] + rho^2 X (s5) and rho R[g_rho] = rho^2 (R_G + 3 box ln rho - (3/2) V^2) (conformal rescaling, G = rho g_rho in four dimensions), X = -R - box ln rho + 6 s |U|^2 on the stationary set.

Stationary-set identity: the 6-column invariant matrix (R, V^2, box, th2, vth, t2V2) has singular values with the smallest 7e-14 (Euclid) and 1.4e-14 (Lorentz), the null vector being (1/2, -1, 3/2, 1, -2, 1) (Euclid) and the same with the signs of the R, box columns flipped (Lorentz), i.e. s|U|^2 = -R/2 + V^2 - (3/2) box ln rho, residual 6e-12 and 2e-13. [Numerical, 14 jets per signature; not proved. It is the stationary-set trace identity of the matrix equation J = 0 (4 conditions at the point plus 16 on the second jet); I did not derive it analytically.]

### 6. The plane-wave modes (s12, s13)
s12 reproduces the merged numbers: on two modes with delta rho = 0 about a constant omega-bar, with the phase-averaged densities normalised by eps^2 rho-bar^2 p_eta^2 M(u,u), rho^2 X -> 1 (reference), rho R[g_rho] -> -1/4, a_1(O_v) sqrt(G) -> 5/6 = (4/6)(-1/4) + 1 (Euclid and Lorentz). The covariant pieces are individually mode dependent: sqrt(G) a_1(M) = 1/12 + 6 s|U|^2-term with s|U|^2 = 0.116 and 0.227 (Euclid), 5.54 and 4.37 (Lorentz) on the two modes; the remainder a_1(O_v) - a_1(M) = 3/4 - 6 s U2 (0.054 and -0.613 in Euclid) is the J-proportional part; only the sum is proportional to the tree-level kernel M. The J-proportional part is not a multiple of G_{mu nu}J^mu J^nu (s13): it involves eta-contracted (non-G-covariant) structure. delta theta at first order is independent of delta ln rho (s9), so the two modes with delta rho = 0 do excite the pseudoscalar.

### 7. Consequences
(a) Residue. With c_W = N_tot/6 + kappa_X r, c_A = N_tot/6 + n_D (fixed-state, antiperiodic Dirac), c_A - c_W = n_D - kappa_X r. For n_D = 0: 4 (r = -4, merged), 2 (r = -2, dressed, conditional on the stipulation), 1 (r = -1, Moser variables with theta independent). For n_D > 0 the Dirac X-term enters with coefficient r_D that this package does not determine: c_A - c_T = n_D - r_V + (n_D/2) r_D (r_V the vector's coefficient). [Conditional.] The vector holonomy contact of the merged text is -alpha_v sigma = -1 on n < 1, +1 on n > 1; it is not a continuation of Tr rho^n at integer n (merged text), so no closure is claimed at r = -1.
(b) Where the ambiguity sits. The identity of section 5 is a relation among curvature and gradient invariants on shell; whether the Wald-type coefficient of R in the induced action is -1/3 per vector (theta, rho independent fields) or -10/3 (theta eliminated) depends on the variation held fixed. In the class G, rho and theta are all functions of Theta (rank-6 map), and G itself is not a tensor under chart diffeomorphisms (it is built with the constant eta contracted with the chart index), so the Iyer-Wald hypotheses (independent covariant fields, diffeomorphism-covariant Lagrangian) are not met in the variable Theta. This is the missing ingredient located by the result.
(c) 039's H1 expectation ("a covariant operator has no X term; kappa_X -> 0 at the density level") is not what the matrix model gives: the covariant operator has a Ricci coupling E_G = -Ric (R-coefficient 4/6 - 1 = -1/3 for the vector), which is not the 4/6 of four scalars.

### 8. Problem F (s7)
Exact polynomial arithmetic on the Lie-Poisson algebra so(4,2): Box = C_41 - C_31 (the merged statement; zero residual at three random polynomials), and for the vector operator H_V eps_a = -Box eps_a - 2{F_ab, eps^b} on upper-index components, with R^{ab} the vector-representation generators of the sign for which J^{ab} + R^{ab} commutes with H_V (the other sign does not; with the opposite Zeeman sign no identity), H_V = -C_41 + C_31^tot + 3, where the vector Casimir is C_V = -3 (symbolic solve of alpha, beta, gamma: (1, 1, 3)). From the displayed formulas of the merged text: F1 = y^2((k.a)^2 - k^2 a^2) with y^2 = -ell^2 - (y^4)^2 a scalar; F2 = k^2 (a.y)^2. With y.y = -ell^2 ((y^0)^2 = ell^2 + y^i y^i + (y^4)^2 >= ell^2) no base point is Lorentz-fixed; for so(6) with delta, y^mu = 0 at |y^4| = ell is allowed and is where the merged text finds f1 = f2.

### Literature
None used. Standard facts (Cartan homotopy formula for exactness of omega_X - omega, Gilkey's formulas for Laplace-type operators, Hodge-de Rham operator on 1-forms with a_1 = (D-6)R/6 per vector) were derived or re-checked here (s5, s11); nothing was imported.

### Hypotheses of every no-go or bounded statement, and the forks
- "No rotation connection / no Stueckelberg effect": Hessian operator in the a^mu variables; rotations as local similarity or e -> Lambda e in the density. Forks explored: Moser variables (positive result); similarity (null); dressing leaves class (null). Forks open: Dirac sector (frame derivative without spin connection); more than four coordinates (tangent/normal split); the Phi-block of Assumption local-lorentz (an independent diagonal connection would make the Phi fluctuation operator covariant by construction, with its own a_1 and no X; relation to a^mu not derived).
- "Covariance does not fix r": needs the stationary-set identity, the J-terms and the choice of independent fields. Forks open: the J-proportional part (explicit form), Wald charge for the constrained class, gauge parameter alpha != 1 (in covariant variables the longitudinal tower again shifts the R-coefficient), replica/tip domain for the covariant operator.

## Claim classification

| # | Claim | Class |
|---|---|---|
| 1 | B_{c|ab} = w_{a|cb} - w_{b|ca} for every coframe | established identity (analytic; checked 4e-15) |
| 2 | B is not a connection for local rotations (shift exchanged) | established (follows from 1; checked) |
| 3 | local similarity leaves a_1 pointwise unchanged | established (standard; checked 1e-14) |
| 4 | no nonzero first-order rotation preserves "eta e antisymmetric" for generic constant omega-bar | established numerically (12 draws); generic only |
| 5 | S[X] = int L(omega_X); quadratic action = (1/2) S_0'' on J = 0 | established derivation (Poisson limit, Tr -> int rho) |
| 6 | S_0'' = 2 M_G + b E, b = -sgn(PfTheta) I1/8 | exact at 6 rational points; not proved for all omega |
| 7 | S O_v S^-1 = covariant Maxwell-axion operator at J = dJ = 0; mismatch linear in J, dJ | numerical (6 jets coefficientwise, 28 jets for a_1) |
| 8 | a_1 = -R/3 + box ln rho - V^2 + 6 s |U|^2 for the covariant operator | derived + numerical (8 digits / 6 digits) |
| 9 | X = -R - box ln rho + 6 s|U|^2 on the stationary set | conditional on 7 (numerical) |
| 10 | s|U|^2 = -R/2 + V^2 - (3/2) box ln rho on the stationary set | numerical (null vector exact to 1e-6; not proved) |
| 11 | r = -1 or -4 depending on representation; r = -2 corresponds to neither | conditional on 9, 10 |
| 12 | residue at n_D = 0 is 1 or 4; vector contact modulus 1 | conditional; no closure |
| 13 | H_V = -C_41 + C_31^tot - C_V, C_V = -3 | established algebraic identity (exact on random polynomials) |
| 14 | no Lorentz-fixed base point on the Lorentzian leaf; F1 invariant, F2 explicit y | established consequence of the displayed formulas |
| 15 | Dirac gamma^A D_A = gamma^A e_A^nu d_nu | established (definition) |
| 16 | the axial torsion S is the dual of a gradient of theta | tested and not true (s4: residual 0.3-1.0); negative check |
| 17 | Wald-type coefficient / which fields are held fixed | unresolved |
| 18 | Dirac sector covariance, replica/tip domain for the covariant operator, gauge dependence | unresolved |

## Proposed changes

File: `chapters/appH-microscopic-proofs.tex` (insert only; no edit of an existing equation). The full text of the two blocks is in `proposals/041-covariant-bundle-connection/appH_insert.tex` (UTF-8, LF, ASCII only; the integrator converts to CRLF). It uses no `\ref`, `\eqref`, `\cite` or `\label`, so no new reference is needed. Compile check in a scratch copy outside the repository: `compile_check.py` / `compile_check.out.txt`: two pdflatex passes exit 0, 307 pages, no undefined `\ref`, no multiply defined labels (undefined citations only because bibtex is not run in the scratch copy).

**BLOCK 1 (Problem B).** Anchor: the unique line `\section{Problem C: conformal mode and Cassini}` (confirmed to occur exactly once; its last preceding paragraph ends "... Problems~B and~D remain open and PROGRAMME-CONDITIONAL."). Insert the block immediately before this line, followed by a blank line. Existing text is kept.

```latex
\paragraph{Moser variables: the covariant form of the connection sector on the stationary set and an identity between curvature and gradient invariants (conditional; not closure).}
Keep the setting of the two preceding paragraphs: four matrix coordinates, the Poisson limit, \(\omega=\Theta^{-1}\) closed, \(e^A{}_\mu=\eta^{AB}\omega_{\mu B}\), \(\rho=\lvert\operatorname{Pf}\omega\rvert\), \(G^{\mu\nu}=\eta_{\alpha\beta}\Theta^{\alpha\mu}\Theta^{\beta\nu}\), \(V_\mu=\partial_\mu\ln\rho\), the vector operator \(\mathcal O_v\) in the background gauge with \(\alpha=1\), and the tree-level equation \(\mathfrak J^\nu=\Box_Gx^\nu-G^{\mu\nu}\partial_\mu\ln\rho=\rho^{-1}\partial_\mu(\rho G^{\mu\nu})=0\). Write \(s_\eta=+1\) for \(\eta=\delta\) and \(s_\eta=-1\) for \(\eta=\operatorname{diag}(-1,1,1,1)\).

\emph{The composite connection.} Let \(w_{c|ab}\) be the components along \(e_c\) of the Levi-Civita spin connection of \(e\), and \(B_{c|ab}=-T_{c|ab}\) the composite connection of \(\mathcal O_v\) in the frame components of the torsion. Then \(B_{c|ab}=w_{a|cb}-w_{b|ca}\) for every coframe: the form index and one frame index of the spin connection are exchanged (this is \(\mathrm de^A=-w^A{}_B\wedge e^B\); checked against \(w\) computed from the metric at random jets, residual \(10^{-15}\), both signatures). Under \(e\to(1+\epsilon\lambda)e\) with \(\lambda_{AB}=-\lambda_{BA}\) the inhomogeneous part of \(w_{c|ab}\) is \(\partial_c\lambda_{ab}\) (up to a convention-dependent sign) and that of \(B_{c|ab}\) is the exchanged expression \(\partial_a\lambda_{cb}-\partial_b\lambda_{ca}\) with the same sign: \(B\) is not a connection for local rotations of the matrix index. A local similarity \(\mathcal O\mapsto S\mathcal OS^{-1}\), \(S(x)\) invertible, leaves the diagonal of the heat kernel, hence \(a_1\) pointwise, unchanged (checked, \(10^{-14}\)), so no Stueckelberg field acting on the index by such a similarity changes a local heat-kernel invariant of \(\mathcal O_v\). The dressing of the preceding paragraph replaces \(B\) by \(B[\Lambda e]\) and is not a similarity. About a generic constant \(\bar\omega\) the only first-order rotation that keeps \(\eta_{AB}e^B{}_\mu\) antisymmetric (the condition for \(e\) to come from a two-form) is \(\lambda=0\), so the Goldstone-extremised frame is not the coframe of any matrix background (twelve draws, both signatures).

\emph{Moser variables.} For embedding functions \(X\) of a fixed symplectic leaf, \(S[X]=\int\mathrm d^4y\,L(\omega_X)\) with \(L(\omega)=\rho\,\eta_{ac}\eta_{bd}\Theta^{ab}\Theta^{cd}\) and \(\omega_X\) the push-forward of the leaf form. A variation \(a^\mu\) of \(X\) changes \(\omega_X\) by \(\mathrm dA\), \(A_\nu=a^\mu\omega_{\mu\nu}\) to first order, and \(L\) is an algebraic function of the six components of \(\omega\). The second-order term of \(S\) is therefore half the Hessian of \(L\) along \(\mathrm dA\) plus a term proportional to \(\mathfrak J\). That Hessian is, exactly (rational arithmetic at six points, both signatures), \(\partial^2L/\partial\omega\partial\omega=2\mathsf M_G+b\,\mathsf E\): \(\mathsf M_G\) is the quadratic form \(\rho\,G^{\mu\rho}G^{\nu\sigma}F_{\mu\nu}F_{\rho\sigma}\), \(\mathsf E\) the form \(\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}\), and \(b=-\operatorname{sgn}(\operatorname{Pf}\Theta)\,\eta_{ac}\eta_{bd}\Theta^{ab}\Theta^{cd}/8\). Apart from the term proportional to \(\mathfrak J\), the connection sector is a Maxwell field of the metric \(G\) with weight \(\rho\), coupled to the pseudoscalar \(\vartheta=\rho b\) through \(b\,\epsilon FF\); the gauge function \(D_\mu a^\mu\) equals \(-\rho^{-1}\partial_\nu(\rho G^{\nu\lambda}A_\lambda)\). At points with \(\mathfrak J=0\) and \(\partial\mathfrak J=0\) the operator \(S\mathcal O_vS^{-1}\), \((Sa)_\nu=a^\mu\omega_{\mu\nu}\), has the same principal, first-order and zeroth-order coefficients as the Maxwell--axion operator in the \(\rho\)-weighted Lorenz gauge (six draws, first-order coefficients to \(10^{-15}\), both vanishing at zeroth order); away from \(\mathfrak J=0\) the mismatch is linear in \(\mathfrak J\) and \(\partial\mathfrak J\). In these variables the field has no frame index: the bundle is the cotangent bundle with the Levi-Civita connection of \(G\), and \(\ln\rho\) and \(\vartheta\) enter as tensor couplings. This is a covariance under diffeomorphisms of the chart acting on \((G,\rho,\vartheta)\); it is not a local Lorentz symmetry of the matrix index.

\emph{Heat-kernel coefficient.} For the Maxwell--axion operator, \(a_1=\operatorname{tr}(E+R_G/6)\) is
\[
  a_1=-\tfrac13R_G+\Box_G\ln\rho-\lvert V\rvert_G^2+6s_\eta\,\lvert\partial\vartheta-\vartheta V\rvert_G^2
\]
(the Hodge operator with the dilaton term \(V\) and the axion term; checked at generic jets, relative agreement \(10^{-6}\) or better, both signatures). At points with \(\mathfrak J=\partial\mathfrak J=0\) it equals \(a_1(\mathcal O_v)\), for which \(\sqrt{\lvert G\rvert}\,a_1=\tfrac46\rho R[g_\rho]+\rho^2X\) (fourteen random stationary jets per signature, \(3\times10^{-11}\)). With \(\rho R[g_\rho]=\rho^2(R_G+3\Box_G\ln\rho-\tfrac32\lvert V\rvert_G^2)\) this gives, on the stationary set,
\[
  X=-R_G-\Box_G\ln\rho+6s_\eta\,\lvert\partial\vartheta-\vartheta V\rvert_G^2 .
\]
On the same jets the invariants satisfy exactly one linear relation (rank five of six),
\[
  s_\eta\,\lvert\partial\vartheta-\vartheta V\rvert_G^2=-\tfrac12R_G+\lvert V\rvert_G^2-\tfrac32\Box_G\ln\rho
\]
(residual \(6\times10^{-12}\)), so that on the stationary set also \(X=-4R_G+6\lvert V\rvert_G^2-10\Box_G\ln\rho\).

\emph{Consequence for the Noether coefficient.} With \(c_W=N_{\mathrm{tot}}/6+\kappa_Xr\) as in the paragraph on the order \(\Lambda^2\), the coefficient of \(R_G\) in \(X\) is \(r=-1\) when the gradient of \(\vartheta\) is kept as an independent invariant and \(r=-4\) when it is eliminated by the identity above. The value \(r=-4\) is the on-mode value of the normalisation paragraph; the value \(r=-2\) of the preceding paragraph, which rests on the stipulated dressing, corresponds to neither. For \(n_D=0\) the residue of the fixed-state replica is \(c_A-c_W=-r\), that is \(1\) or \(4\), to be compared with the vector holonomy contact of modulus \(1\) of the paragraph on the order \(\Lambda^2\). Covariance of the density therefore does not fix \(r\): it leaves two representations related by one identity of the stationary set, and the choice between them is the choice of which of \(G\), \(\rho\), \(\vartheta\) are held fixed under the variation of the first law; in the class all three are functions of \(\Theta\). On the two modes with \(\delta\rho=0\) the term in \(\lvert\partial\vartheta-\vartheta V\rvert^2\) and the part of \(a_1(\mathcal O_v)-a_1\) proportional to \(\mathfrak J\) are each mode dependent and not proportional to the tree-level kernel; their sum is, and gives the value \(\rho^2X\to1\) in the units of that paragraph.

These statements are for the Poisson limit, four matrix coordinates, \(\alpha=1\), one loop, the density \(a_1\), points with \(\mathfrak J=\partial\mathfrak J=0\) for the operator identity (numerical, at sampled jets), and the covariant formula for \(a_1\). They do not cover the Dirac sector for \(n_D>0\), whose X-term enters with its own coefficient and whose operator \(\gamma^AD_A\) is the frame derivative \(\gamma^Ae_A{}^\nu\partial_\nu\) without spin connection and is not shown to have a covariant form; the terms proportional to \(\mathfrak J\) off the stationary set; the replica, the tip domain or the choice of independent fields in the first law; the gauge parameters other than \(\alpha=1\); more than four matrix coordinates; or a value or sign of \(G_{\mathrm{eff}}\). They derive no local Lorentz symmetry. Problems~B and~D remain open and PROGRAMME-CONDITIONAL.
```

**BLOCK 2 (Problem F).** Anchor: the unique line `\section{Problem G: HBEV}` (occurs once; the preceding paragraph ends "... This changes no ledger label; Problem~F remains open."). Insert immediately before it.

```latex
\paragraph{Conjugate-coordinate class: the Casimir form of the Zeeman-dressed vector operator and the base-point dependence (conditional; bounded no-go).}
Keep the Poisson limit, the leaf \(\mathbb{CP}^{1,2}\) of \(\mathfrak{so}(4,2)\), \(T^a=M^{a4}\), \(D^a=\{T^a,\cdot\}\), \(J^{AB}=\{M^{AB},\cdot\}\), \(F_{ab}=\{T_a,T_b\}\), \(\Box=\eta_{ab}D^aD^b\) and the vector operator \(H_V\varepsilon_a=-\Box\varepsilon_a-2\{F_{ab},\varepsilon^b\}\) of the paragraph on the \(\Theta\)-built heat kernel. Let \(C_{41}=\tfrac12J^{AB}J_{AB}\) and \(C_{31}=\tfrac12J^{ab}J_{ab}\) (indices \(\le4\) and \(\le3\)) act on functions, let \(R^{ab}\) be the generators of the vector representation of \(\mathfrak{so}(3,1)\) with the sign for which \(J^{ab}+R^{ab}\) commutes with \(H_V\), and \(C_{31}^{\mathrm{tot}}\) the Casimir of \(J^{ab}+R^{ab}\). In exact polynomial arithmetic (random polynomial fields), \(\Box=C_{41}-C_{31}\) and
\[
  H_V=-C_{41}+C_{31}^{\mathrm{tot}}-C_V,\qquad C_V=-3 ,
\]
the other sign of \(R^{ab}\) and the opposite sign of the Zeeman term giving no such identity. In this class the vector operator is therefore a Casimir operator of the total Lorentz spin: a bundle connection covariant under \(J^{ab}+R^{ab}\) is present, and the dependence of \(A\), \(F_1\) and \(F_2\) of the paragraph on the Zeeman-dressed vector sector on \(y^\mu\) is not the absence of a connection. From the displayed definitions, \(F_1=y^2\bigl((\kappa\cdot\alpha)^2-\kappa^2\alpha^2\bigr)\) depends on the base point only through the scalar \(y^\mu y_\mu=-\ell^2-(y^4)^2\), and \(F_2=\kappa^2(\alpha\cdot y)^2\) is the term that contains \(y^\mu\) as a vector. Since \(y\cdot y=-\ell^2\) in the five-dimensional contraction, \((y^0)^2=\ell^2+y^iy^i+(y^4)^2\ge\ell^2\): no point of the leaf is fixed by the matrix Lorentz group, so a local density cannot be evaluated at a Lorentz-symmetric base point. For the compact form \(\mathfrak{so}(6)\) with \(\delta\) the points \(y^\mu=0\), \(\lvert y^4\rvert=\ell\) exist, and they are the points where the preceding paragraphs find \(f_1=f_2\).

This is a statement for the Poisson limit, the Lie--Poisson algebra \(\mathfrak{so}(4,2)\), the operator without the mass term and with the background gauge function, and the algebraic identity on polynomials; the sign of \(R^{ab}\) is fixed by invariance, not by an independent convention. It does not compute a finite coefficient, does not treat fermions, the window or the Zeeman-dressed resolvent at order \(\epsilon^2\), and gives no value or sign of \(G_{\mathrm{eff}}\). This changes no ledger label; Problem~F remains open.
```

### Stale or overstated passages elsewhere (PRIOR-CLAIM qualification, soft)

(a) Overstated by the result (not false in the coframe variables, but "stays undetermined until D is settled" is no longer the only determination route). File `chapters/appH-microscopic-proofs.tex`, unique string (occurs once):

OLD: `It stays undetermined until the frame is dragged by a flow whose internal part is a local symmetry, that is until the question of local frame rotations (Problem~D) is settled.`

NEW: `In the coframe variables it stays undetermined until the frame is dragged by a flow whose internal part is a local symmetry, that is until the question of local frame rotations (Problem~D) is settled; in the Moser variables of the paragraph on the connection sector on the stationary set it takes two values related by one identity.`

(b) Optional clarification (unique string, occurs once):

OLD: `The frame sector of the induced density is therefore not invariant under local rotations of the \(\Theta\)-built frame unless \(\kappa_X=0\), that is \(n_D=2\) in the weights of the paragraph on fermionic content.`

NEW: `The formula \(\kappa_X\rho^2X\), taken as a function of an arbitrary coframe, is therefore not invariant under local rotations of the \(\Theta\)-built frame unless \(\kappa_X=0\), that is \(n_D=2\) in the weights of the paragraph on fermionic content; this concerns the extension of the formula off the coframes of the form \(\eta^{-1}\omega\), and on the stationary set the density is a function of \(G\), \(\rho\) and one pseudoscalar (paragraph on Moser variables).`

No merged equation is false. The limitation sentence of the 039 block ("they do not derive ... a covariant bundle connection for the fluctuation operator") remains literally true for that block and is partly addressed by BLOCK 1; no edit is proposed. The claim "the difference is the term rho^2 X of the connection sector, which ... contributes no entropy" in the normalisation paragraph refers to the fixed-state replica with rho regular and is unaffected.

## Verification scripts

All in `proposals/041-covariant-bundle-connection/` with saved `.out.txt` (Python 3.11, numpy 2.4, scipy 1.17, sympy 1.14; `tj.py` is the jet class of 039, `geom.py` the shared Christoffel/Gilkey routines):

- `s1_crossed_spin_connection.py` (+`.out.txt`): B = crossed w (class and non-class coframes), rotation laws.
- `s2_constitutive_tensor.py`, `s2c_constitutive_exact.py`: Hessian of L, finite differences and exact rational.
- `s3_operator_identity.py` (library), `s3b_J0_comparison.py`, `s3c_J_scaling.py`: operator coefficient comparison on stationary and perturbed jets; `s14_J_forms.py`: the two forms of J.
- `s4_axial_torsion_is_dual_gradient.py`: negative check (S is not dual to d theta).
- `s5_scalar_and_vector_a1.py`: validation of the Gilkey routine against the merged formulas.
- `s6_covariant_a1_fit.py` (first fit, four invariants), `s6b_covariant_a1_fit.py` (two-stage stationary sampler, six invariants, `s6b_samples.pkl`), `s6c_stationary_identity.py` (null vector, identity, formula checks).
- `s7_casimir_structure.py`: Casimir identity on so(4,2) (symbolic).
- `s8_goldstone_leaves_class.py`: class exit of the extremised rotation.
- `s9_theta_first_order.py`: first-order delta theta versus delta ln rho.
- `s10_similarity_invariance.py`: Lemma S.
- `s15_gauge_function.py`: D_mu a^mu = -rho^-1 d_nu(rho G^{nu lam} A_lam).
- `s3_operator_identity.out.txt`: output of the generic-jet comparison (J != 0) and of the symbol checks.
- `s11_hodge_check.py`, `s11b_axion_term.py`: analytic a_1 versus numerical at generic jets.
- `s12_planewave_decomposition.py`, `s13_J_term_planewave.py`: plane-wave decomposition of the quadratic forms.
- `compile_check.py` / `compile_check.out.txt`: scratch build.

Run-time notes: s6b/s12 take several minutes (heat-kernel operator applications on jets).

## Decisions Taken

1. Route: investigate the matrix model's own covariant structure rather than extend the Stueckelberg stipulation. Reason: 039's dressing is gauge-redundant in unitary gauge and was shown here to be either a null similarity or a map out of the matrix-realisable class; the exact-variation (Moser) structure is intrinsic to the matrix action. Rejected: adding an independent diagonal connection (Chapter 10) as the default, because that adds field content the matrix model does not supply.
2. Keep both values of r (-1, -4) and do not select one. Reason: choosing requires specifying which fields are varied in the first law, which is a modelling choice; selecting r = -1 because it brings the n_D = 0 residue to the available contact modulus would be selecting by the match (the same defect 038 recorded for r = -4). The ranked avenue is the Wald/Noether charge of the constrained class.
3. Dirac sector not covariantised: no matrix-native covariant structure was found (frame derivative without spin connection); stated as a limit, not extrapolated from the vector.
4. PRIOR-CLAIM: recorded as soft qualifications (a), (b); no merged equation is false.
5. No `\ref` or citations used in the inserted text to avoid dependence on label stability; descriptions by paragraph name follow the existing style.

## Milestone assessment

Routine for the milestone triggers: no critical-path step is derived and no missing link is closed. It is a direction-changing structural result (location of the missing ingredient moves from local-frame invariance of X to the Noether/Wald charge of the constrained class, plus an exact covariant form of the bosonic connection sector on the stationary set), which I recommend the gatekeeper weigh as "consequential, not a breakthrough".

## Status-label recommendation

None. B, D, F (and A, C, E, G-derived, N) keep their current labels: OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL where so stated. No label edit appears in the LaTeX.

## Author decision needed

None. (The choice between r = -1 and r = -4 is a modelling choice inside the core, recorded under Decisions Taken, not a change to status, scope or core assumptions. No option that makes spacetime non-emergent is involved.)

## Remaining open step

Ranked open avenues (the no-go "X cannot be removed by a rotation connection" is bounded by the hypothesis class stated above):

1. **Off-shell J-terms (explicit).** Derive analytically S O_v S^-1 - O_M as first/zeroth-order operators linear in J, dJ (coefficients 19 and 1.9 numerically), identify their eta-contracted structure, and decide whether they are removable by a redefinition of the background (EOM-proportional). This ties the plane-wave eigenvalue to the covariant functional and is needed before any claim about "G_T" on the modes.
2. **Wald/Noether charge for the constrained class** (the located missing ingredient): Iyer-Wald entropy for the single field Theta with L(G(Theta), rho(Theta), theta(Theta)), including the non-tensorial dependence through the constant eta; decides between r = -1 and r = -4 (or a third value).
3. **Dirac sector**: look for a Moser-type exact structure for the fermionic Hessian or a supersymmetric completion (the (N_s, n_D) = (6, 2) point); until then the n_D > 0 residue formula keeps r_D open.
4. **Replica for the covariant operator**: domain at the tip, rotated versus unrotated vector gluing, whether the Ricci-type delta (contact modulus 1) is carried by the matrix state; relation to the non-analyticity at n = 1.
5. **Gauge dependence in Moser variables** (alpha != 1, longitudinal tower) and the sign/definiteness of the axion term (Lorentzian).
6. **Leaf dimension above four**: tangent/normal split of the ambient index in the exact-variation argument (normal components are scalars).
7. **Analytic proof** of the Hessian identity (section 3) and of the stationary-set identity (section 5), which would convert two numerical statements into derivations.
8. **Phi-block** (Assumption local-lorentz): covariance by construction; relation of its fluctuation operator to a^mu.
9. Problem E tie: the covariance of the F-leaf coefficients at Lorentz-fixed points exists only in the compact real form.

## Special instructions for the gatekeeper

- Do not read "covariant" as local Lorentz symmetry: BLOCK 1 states a diffeomorphism covariance in (G, rho, theta) of the transformed operator at J = dJ = 0, nothing about D1.
- Do not read r = -1 as the Noether coefficient: both -1 and -4 are recorded and the choice is explicitly left open; the residue 1 at n_D = 0 is not a closure (the contact of modulus 1 is not derived, and is not a continuation of Tr rho^n).
- Re-run: s1 (seconds), s2c (seconds), s7 (about 1-2 min), s8, s9, s10, s11, s11b (tens of seconds each), s6c (from the pickle), s3b (about 1 min); s6b and s12 (several minutes). Check that the Gilkey routine reproduces the merged formulas (s5), because every a_1 statement uses it.
- Re-derive the analytic a_1 of the covariant operator (section 5): the sign of the dilaton term (V enters as +V.nabla) was initially mis-signed in my own first pass; s11 now matches to 8 digits.
- The operator identity is numerical at sampled jets (stationary jets are constructed by least squares; they are not special families). The Hessian identity is exact only at the sampled rational points.
- Verify the unique anchors: `\section{Problem C: conformal mode and Cassini}` and `\section{Problem G: HBEV}` (once each) and the uniqueness of the two OLD strings in the PRIOR-CLAIM section.
- Scope statements to preserve: bosonic connection sector, four matrix coordinates, alpha = 1, one loop, stationary set for the operator identity; Dirac, replica, tip domain, first-law variables, G_eff untouched.
