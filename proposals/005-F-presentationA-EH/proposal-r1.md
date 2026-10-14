# Proposal 005-F-presentationA-EH, round 1

## Result

Target: Problem F, toward discharging Assumption `ass:emergent-op` by a within-core route that is not covered by the integrated Lemma 2 (hypotheses H1-H4). The route is Presentation A in the Poisson (leading semiclassical) limit, with a kinetic metric and regulator built from Theta. Everything below is conditional on the stated model; nothing closes F.

1. **Scalar sector (established algebra, conditional on the Poisson limit).** For a real fluctuation whose kinetic term is the Poisson limit of Tr[X_mu, phi]^2, the operator O_s = -rho^-1 d(rho K d .) is of the form eq:O-eta on the metric G (G^{mu nu} = K^{mu nu}), with an explicit connection omega = -1/2 d ln rho and explicit endomorphism E. For every such Theta, `sqrt|G| (R_G/6 - E) = rho R[g_rho]/6` pointwise (hand proof below; verified at a generic Poisson bivector). So the Lambda^2 term of eq:W-expand has exactly the Sakharov coefficient, 1/(16 pi G) = N Lambda^2 rho/(192 pi^2) per N real components, multiplying the curvature of the Theta-built metric g_rho. This extends the 004 identity (it was stated there for unimodular g_rho and verified on a diagonal family; here it is proved in general and checked on a generic Poisson structure).
2. **The Theta-built metric is a composite metric of Chapter 4 (established algebra).** G_{mu nu} = eta_AB e^A_mu e^B_nu for the coframe e^A_mu = eta^{AB} omega_{mu B}, omega = Theta^-1 (the symplectic form). The coframe is "antisymmetric": eta_AB e^B_mu is antisymmetric in (A, mu). The map Theta -> G has rank 6 (sampled points), so Theta-built metrics form a 6-parameter subfamily of the 10-parameter space of metrics, and (generic points) no linearized-diffeomorphism direction of G lies in its tangent space. Hence if <Phi>/v of eq:vev-is-frame were identified with this coframe, the Presentation-A operator would be the operator of `ass:emergent-op`. That identification is not derived (it is the missing link; it belongs with Problems A and D).
3. **Connection sector: a bounded obstruction (conditional, computed).** The gauge-fixed matrix gauge potential a^mu (background gauge, ghost weight -2) has a Laplace-type operator on G with connection omega_sigma = -1/2 d_sigma ln rho + B_sigma and endomorphism E = div omega + omega.omega, and
   `sqrt|G| tr(R_G/6 - E) = (4/6) rho R[g_rho] + rho^2 X`, with `X = eta^{rho lambda} eta_{mu alpha} eta_{nu beta} d_rho Theta^{mu nu} d_lambda Theta^{alpha beta}`.
   With the ghosts, the connection sector contributes (2/6) rho R[g_rho] + rho^2 X. The first term has the covariant EH form with weight +2. The second, X, has the derivative index contracted with the constant eta (the matrix-model target metric), not with G. For the block family X = 2 K^{mu nu} d_mu ln rho d_nu ln rho; for a generic Poisson bivector it is not (numerical check).
4. **Quadratic form about a constant Theta-bar (conditional, computed).** On the three gauge-invariant modes the second-order terms of rho^2 X and of rho R[g_rho] are both multiples of the tree-level Maxwell kernel M = q^2 eta - q q (q = Theta-bar p), by functions of p_eta^2 = eta^{mu nu} p_mu p_nu. In units rho-bar^2 p_eta^2 relative to M: X gives +1 (three modes); rho R[g_rho] gives -1/4 (two modes, purely transverse-traceless for the EH form, delta rho = 0) and -3/4 (one mode, delta rho != 0). With N_tot = (weighted count of scalar-type components) + 2 (connection sector), the Euclidean Lambda^2 quadratic form is -(Lambda^2/32 pi^2) rho-bar^2 p_eta^2 (1 - N_tot/24) M on the two TT-type modes and (1 - N_tot/8) M on the third. So the TT-type EH term carries the sign of a positive induced 1/G only if N_tot > 24; for the connection sector alone (N_tot = 2) the eta-contracted term X has the opposite sign and dominates. Both terms are multiples of M by functions of p_eta^2, so they do not move the cone q^2 = 0; about a constant background they do not fix G_eff.
5. **Position-dependent cutoff.** Replacing Lambda^2 by Lambda^2 f(rho) (local proper-time cutoff on the diagonal heat kernel) multiplies the EH-type coefficient by f(rho): G_eff^-1 is proportional to f(rho) rho. The 2-mode eigenvalue is unchanged; for f = rho^s the third mode becomes 1 - N_tot (2s+3)/24. The matter frame for scalar-type components is g_rho (minimal coupling), in which the term has Brans-Dicke form with omega_BD = 0 in the scalar sector.

**Hypothesis class of the obstruction in item 3/4** (all must hold): Poisson-limit commutator (Moyal corrections dropped); bosonic 4D matrix Yang-Mills content (no fermions, no extra scalars, no mixing of Phi with a^mu); minimally coupled background-gauge fixing D_mu a^mu with eta contraction; off-shell Gaussian determinant (linear term in a^mu not assumed to vanish); diagonal heat kernel with a local cutoff; Euclidean sign statements. **Next relaxations**, each within the core: (i) fermionic and additional scalar content of the IKKT-type model (changes N_tot and may change X); (ii) Moyal corrections at the cutoff scale; (iii) non-minimal gauges with an on-shell reduction; (iv) a coupling of the internal index to a local frame (Lorentz locking), which is the Presentation-B counterpart and bears on D1; (v) mixing of Phi with a^mu on a non-central <Phi>. None of these is done here.

What is **not** shown: `ass:emergent-op` is not discharged (the identification of <Phi>/v with the coframe omega is not derived, the Phi-a mixing is not treated, and the Poisson limit is not controlled at the cutoff); the locked-block F target is not computed; no value or sign of G_eff follows; the matrix-to-dictionary map (Problem A) is not derived.

## Target and status

- Problem F, `sec:status-F` (appH L1103-1127): **Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL.** "Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion." Missing step (appH L1116): specify the gauge-fixed fluctuation, Goldstone, diffeomorphism-ghost and local-Lorentz-ghost operators and weights, limits, continuation, finite-counterterm scheme; then evaluate weighted a_1 and curvature-linear a_2.
- Chapter 17 (`sec:ch17-coeff`, L403-471; `sec:ch17-done`, L688-735): F "CRITICAL PATH; OPEN". Original target: evaluate the weighted a_1 and the curvature-linear part of a_2 on the **locked block**, including diffeomorphism and local-Lorentz ghosts and the radial-mode threshold, with a scheme stated. Completion item 6: A, B, C coefficients and the sign/scheme dependence of G_eff computed from the specified operators; G_eff not an input. Dependencies: D1 (operators omega, A_mu, B and ghosts), A (dictionary), C, N.
- Critical-path set re-derived from `sec:ch17-done` (items 1-8): A, B, C, D1, E, F, G-derived, N. All OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL in the entries I read (F, A in full; others by the 003/004 reviews and the ledger, not re-read end to end). No discrepancy found between Chapter 17 and Appendix H for F.
- This proposal's classification: **PROGRAMME-CONDITIONAL** (a conditional sub-lemma on the form of `ass:emergent-op` in Presentation A plus a bounded obstruction). It does not meet the F original target (locked block, local-Lorentz and diffeomorphism ghosts, radial threshold are not touched).
- Relation to the ch17 sentence "The asserted net +2 from the on-shell TT count is not an off-shell heat-kernel trace": the weight count (4 - 2) = 2 of item 3 is an off-shell trace in a stated gauge for the Presentation-A matrix gauge sector only, and it is accompanied by X. It does not assert the "+2 TT count" and does not specify the locked-block ghosts.

## Source reading

Digest + targeted reads (not a full scan). `python scripts/make_digest.py --check` printed `DIGEST CURRENT` (chapters-hash 196b7f142fde8bc9). Read in full or in the relevant ranges: CLAUDE.md, MILESTONE.md, `reports/ledger.md`, `proposals/004-author-questions/recommendations-r2.md` and `review-r1.md`, the 004 script `check_weighted_laplacian_a1.py`; appH L12-40 (A), L1103-1127 and L1472-1650 (F, including Lemma 2 and the "What the two preceding results imply" paragraph), L780-830 and L905-925; ch03 L59-172 (two presentations, Presentation A), L299-755 (dictionary, `rem:ch3-moyal-check`, `rem:ch3-trace-quadratic`, `rem:ch3-varying-theta`); ch04 L31-312 (composite metric, SW); ch08 L20-100, L120-160, L195-235, L278-335 (`sec:ch8-which-g`, `ass:emergent-op`, `rem:ch8-scaffold-vs-emergent`); ch09 L150-200; appA L60-106; ch17 L403-475, L640-735. Not read this round: the other chapters beyond the digest outline (no full-scan trigger: the proposed text adds a conditional paragraph and changes no definition, assumption, scope or status passage). No unreadable files.

## Research and reasoning

### 0. Setup (conditional inputs, stated)

Nondegenerate Poisson bivector Theta^{mu nu}(x) (Jacobi), rho = 1/|Pf Theta|, so d_mu(rho Theta^{mu nu}) = 0 (Liouville; checked symbolically for the block family and numerically for a generic Darboux pushforward). Poisson limit: [.,.] -> i{.,.}, {f,g} = Theta^{mu nu} d_mu f d_nu g, Tr -> int d^4x rho. D^mu f := {x^mu, f} is anti-self-adjoint with respect to rho d^4x, and (Jacobi) [D^mu, D^nu] f = {Theta^{mu nu}, f}. Matrix-coordinate indices are contracted with eta, which is already part of eq:Smatrix (it is the matrix model's internal contraction, not a spacetime metric). K^{mu nu} = eta_ab Theta^{a mu} Theta^{b nu}; g_rho^{mu nu} = rho K^{mu nu} (as in `rem:ch3-varying-theta`); G with G^{mu nu} = K^{mu nu}. Then G = rho g_rho, |det g_rho| = 1, sqrt|G| = rho^2. The Moyal corrections O(Theta^3 d^3) are dropped; since Theta p^2 ~ 1 at p ~ Lambda_UV ~ Theta^-1/2 they are not small at the cutoff, so the numerical coefficients are those of the Poisson-limit operator (the same truncated-expansion status as Theorem thm:Geff).

### 1. Scalar sector

D_mu D^mu f = K^{rs} d_r d_s f + Theta^{mu r} d_r Theta_mu^s d_s f = rho^-1 d(rho K d f) =: L f, using Liouville. With sqrt|G| = rho^2 and G^{mu nu} = K^{mu nu}: L f = Lap_G f - G^{mu nu} d_mu ln rho d_nu f, hence O_s = -L = -D^2 + E with D = nabla + omega, omega = -1/2 d ln rho (real, pure gradient, curvature-free), E = div omega + omega^2 = -1/2 Box_G ln rho + 1/4 |d ln rho|_G^2.

Hand proof of the a_1 identity (no unimodular family assumption). For G = rho g (g = g_rho, sqrt g = 1) in 4D, Omega^2 = rho:
- R_G = rho^-1 [R - 3 Box_g ln rho - 3/2 |grad ln rho|_g^2] (standard conformal formula, 4D).
- Box_G phi = (1/sqrt G) d(sqrt G G^{mu nu} d phi) = rho^-2 d(rho g^{mu nu} d phi) = rho^-1 (Box_g phi + grad ln rho . grad phi), and |d ln rho|_G^2 = rho^-1 |grad ln rho|_g^2.
- So E = rho^-1 [-1/2 Box_g ln rho - 1/2 |grad ln rho|_g^2 + 1/4 |grad ln rho|_g^2] = rho^-1 [-1/2 Box_g ln rho - 1/4 |grad ln rho|_g^2].
- R_G/6 - E = rho^-1 [R/6 - 1/2 Box ln rho - 1/4 |grad ln rho|^2 + 1/2 Box ln rho + 1/4 |grad ln rho|^2] = rho^-1 R[g]/6, and sqrt|G| = rho^2 gives rho R[g]/6.

This is an algebraic identity; with det g = -1 or +1 and either signature it holds. Verified: `check_vector_sector_block.py` (4a), `check_vector_sector_generic.py` (iii-a).

Meaning: with a constant cutoff, one real scalar-type component gives W_E contains -(Lambda^2/192 pi^2) int d^4x rho R[g_rho] (eq:W-expand with a_1; limits Lambda, mu -> mu dropped). This is the coefficient of Theorem thm:Geff (1/(16 pi G) = N Lambda^2/(192 pi^2); it matches the "N_0 Lambda^2/(192 pi^2)" already used in appH) multiplying the curvature of g_rho with a factor rho. The kinetic term is sqrt(g_rho) g_rho^{mu nu} d phi d phi: minimally coupled to g_rho. The ρ-dependence is a Brans-Dicke-type field (omega_BD = 0 in this sector, no kinetic term for rho from this term).

### 2. Frame and class (the Theta-built metric is a composite metric)

omega := Theta^-1 (omega_{mu B} Theta^{B nu} = delta_mu^nu), e^A_mu := eta^{AB} omega_{mu B}. Then eta_AB e^A_mu e^B_nu = (omega eta^-1 omega^T)_{mu nu} = ((Theta^T eta Theta)^-1)_{mu nu} = G_{mu nu}. So G is the composite metric of eq:g-from-e for this coframe; eta_AB e^B_mu = omega_{mu A} is antisymmetric. (`check_soldering_and_frames.py`, both signatures.)

Class and symmetry. Pointwise, Theta -> G has rank 6 (sampled points, both signatures; the Euclidean point a = b has rank 4, a degenerate case). The mixed endomorphism K eta has two doubly degenerate eigenvalues (K eta = -N^2 for the Lorentz generator N = Theta eta), a codimension-4 condition on the metric. A diffeomorphism acts as K -> J K J^T and maps the class to itself only for J in O(eta): the class is invariant under the rigid target group only. At generic (Theta-bar, p) no pure-gauge perturbation p_(mu xi_nu) lies in the tangent space (`check_class_vs_diffeo.py`; sampled points). So this route does not realise linearized-diffeomorphism invariance of the Theta-built metric; what Lemma 2 excluded for a fixed linear image of Phi is relaxed here (nonlinear, 6-dimensional composite map, non-invariant background), but no gauge symmetry protects any induced term.

Physical modes. With a^mu = Theta^{mu rho} a_rho (a_rho a covector; delta a^mu = Theta^{mu rho} d_rho lambda <-> delta a_rho = d_rho lambda), the linear part of the matrix field strength is Theta f Theta with f = da; i.e. omega -> omega - f: the internal index of the matrix gauge potential is the frame index of the one-form a_rho in the coframe e. (Not needed for the claims; recorded because it is the Presentation-A analogue of "tying derivative index to tangent index".)

### 3. Connection sector

Quadratic action. S = (1/4g^2) Tr (Theta + F)_{mu nu}(Theta + F)^{mu nu} with F^{mu nu} = D^mu a^nu - D^nu a^mu + {a^mu, a^nu}, so to second order
(1/4g^2) int rho [F1^2 + 2 Theta_{mu nu}{a^mu, a^nu}], F1^{mu nu} = D^mu a^nu - D^nu a^mu.
Integrating by parts with the anti-self-adjointness of D and [D_mu, D^nu] = {Theta_mu^nu, .}:
(1/2g^2) int rho [D_mu a_nu D^mu a^nu - (D.a)^2 + a_nu {Theta_mu^nu, a^mu}] from the F1^2 term, and the Theta{a,a} term equals -a^mu {Theta_{mu nu}, a^nu} up to the cyclicity int rho f{g,h} = int rho g{h,f}, which has the same form as the last term of the bracket. Adding the gauge-fixing term +1/2 rho (D.a)^2 cancels (D.a)^2 and the total is
(1/2g^2) int rho [K^{rho sigma} d_rho a_nu d_sigma a^nu - 2 a^mu {Theta_{mu nu}, a^nu}].
(The scripts derive the Euler-Lagrange operator directly from the unreduced Lagrangian `F1^2/4 + Theta{a,a}/2 + (D.a)^2/2`; no integration by parts is trusted.) Operator: (O_v a)^mu = O_s a^mu - 2 eta^{mu alpha} {Theta_{alpha nu}, a^nu}. Ghost: gauge condition D_mu a^mu, delta a^mu = D^mu lambda + ..., Faddeev-Popov operator D_mu D^mu = L = -O_s, weight -2.

Laplace form. -O_v = L + 2 B^sigma d_sigma with (B^sigma)^mu_nu = eta^{mu alpha} Theta^{rho sigma} d_rho Theta_{alpha nu}, so omega^sigma = -1/2 G^{sigma tau} d_tau ln rho . 1 + B^sigma and E = nabla_sigma omega^sigma + omega_sigma omega^sigma (O_v has no zeroth-order term in the Cartesian internal trivialization). tr B = 0, tr(B_sigma) = 0, so tr E = 4 E_s + tr(B_sigma B^sigma) and tr(B_sigma B^sigma) = -G_{sigma tau} B^sigma_{mu nu} B^{tau mu nu} = -eta^{rho lambda} d_rho Theta_{mu nu} d_lambda Theta^{mu nu} = -X, using Theta G Theta^T = eta^-1 (from K = Theta^T eta Theta). Hence sqrt|G| tr(R_G/6 - E) = 4 rho R[g_rho]/6 + rho^2 X.

Checks: Euler-Lagrange operator of the Lagrangian equals eta O_v (block family, exact, both signatures; generic Poisson bivector at a rational point), -D^2 + E = O_v (same), the trace identity (same). In the block family B_sigma, lowered with G, equals the Levi-Civita spin connection of G in the coframe e; for a generic Poisson bivector it does not (`check_B_equals_LC_generic.py`), so I make no claim that the connection is the Levi-Civita one.

Non-covariance of X. X has the derivative index contracted with eta. Block family: X = 2 K^{mu nu} d_mu ln rho d_nu ln rho. Generic Poisson bivector (Darboux pushforward, polynomial embedding): X = -2.878..., 2 K d ln rho d ln rho = 2.548... (`check_xspin_generic.py`). I do not claim that no G-covariant rewriting of X exists: the comparison is against one covariant candidate, and (see item 4) at quadratic order about a constant background X is indistinguishable from a multiple of the covariant EH term. The relevant structural fact is different: Theta is determined by G only through eta (the map Theta -> G needs the constant eta), the Theta-class is not diffeo-invariant (item 2), and no symmetry relates the coefficient of X to that of rho R[g_rho]. X is also not invariant under local rotations of the internal index (the matrix model has only the global SO(3,1)); this is the Presentation-A face of Problem D, and I do not claim more.

### 4. Quadratic form about constant Theta-bar

Take Theta = Theta-bar + eps T, T^{mu nu} = Theta-bar^{mu rho} d_rho a^nu - Theta-bar^{nu rho} d_rho a^mu, a^mu = u^mu cos(p.x). T is invariant under delta a^mu = Theta-bar^{mu rho} d_rho lambda (u -> u + c q, q^mu = Theta-bar^{mu rho} p_rho), so the phase-averaged second-order terms of L_h := rho R[g_rho] and L_x := rho^2 X are quadratic forms on the 3-dimensional quotient. Only the linear part of delta Theta is used: the {a,a} part of delta Theta enters L_h at second order only through R^(1)[h2], a total derivative about a flat constant background, and enters L_x at third order. Every nondegenerate constant Theta-bar is brought by a global SO(4) or SO(3,1) transformation to Theta^01 = a, Theta^23 = b.

Results (exactly, in p; `check_quadratic_form_sym.py`, `analyze_quadratic_forms_symbolic.py`; (eta signature, a, b) = (+,1,1), (+,1,2), (+,2,3), (-,1,1), (-,1,2), (-,3,1)): M q = 0 for both forms, and relative to M = q^2 eta - q q (Remark `rem:ch3-trace-quadratic`) on the quotient, with rho-bar = 1/(ab):
- L_x: (lambda - rho-bar^2 p_eta^2)^3 = 0, three-fold. This one is elementary: X is quadratic in d Theta, so about a constant background (rho^2 X)^(2) = rho-bar^2 eta^{rho lambda} d_rho T_{mu nu} d_lambda T^{mu nu}, whose phase average is rho-bar^2 p_eta^2 times the phase average of T_{mu nu} T^{mu nu} = 2 (q^2 u.u - (q.u)^2) sin^2, i.e. the Maxwell kernel M.
- L_h: (lambda + rho-bar^2 p_eta^2/4)^2 (lambda + 3 rho-bar^2 p_eta^2/4) = 0.
Independent check of L_h: `check_fp_crosscheck.py` recomputes <(rho R)^(2)> from the Fierz-Pauli form rho0 L_FP(h1) + rho1 R^(1)[h1] and matches the brute-force Ricci-scalar matrices exactly (both signatures). `check_tt_content.py`: for the two-fold eigenspace delta rho = 0, tr h = 0, and the FP form equals its TT projection with respect to p and g_rho-bar; for the single mode delta rho != 0 and it does not. `check_cutoff_split.py`: <(rho R)^(2)> = rho0 <L_FP> + <rho1 R^(1)>, with eigenvalues -rho-bar^2 p_eta^2/4 (three-fold) and {0, 0, -rho-bar^2 p_eta^2/2} respectively (sampled p, two cases).

Therefore, for N_s additional real scalar-type components of form (item 1) and the connection sector (weights 4 - 2 = 2 on rho R/6 plus one X):
Euclidean W_E^(2) = -(Lambda^2/32 pi^2) rho-bar^2 p_eta^2 [ (1 - N_tot/24) on the two TT-type modes, (1 - N_tot/8) on the third ] M, N_tot = N_s + 2.
Position-dependent cutoff: Lambda^2 -> Lambda^2 f(rho) multiplies both L_h and L_x by f; (f rho R)^(2) = f-bar [ (rho R)^(2) + s rho1 R^(1) ] for f = rho^s; since delta rho = 0 on the TT modes their factor is unchanged, and the third mode's factor is 1 - N_tot (2s+3)/24. The frame statement is the 4D conformal identity int f rho R[g_rho] = int sqrt(g_hat) [R_hat - (3/2) g_hat^{mu nu} d_mu ln(f rho) d_nu ln(f rho)], g_hat = f rho g_rho (pointwise difference is 6 d_mu(sqrt g Omega g^{mu nu} d_nu Omega); `check_soldering_and_frames.py`). Whether the manuscript's cutoff Lambda_UV ~ Theta^-1/2 corresponds to a constant or to a local proper-time cutoff for O_s is a scheme choice; the manuscript's explicit computations use a constant Lambda_UV. If the cutoff is the image of a momentum cutoff p^2 <~ Theta^-1, the cutoff on O_s ~ K p p is ~ Theta ~ rho^-1/2 (s = -1/2); this is a scheme illustration, not a derivation.

Interpretation, with its limits. (i) Around a constant background all three Lambda^2 forms are multiples of M by functions of p_eta^2 alone, so they do not move the cone q^2 = 0 and, at this order, are removable by a local redefinition of a^mu; in particular they cannot be used to read off G_eff, and relative to the tree-level kinetic structure of eq:Smatrix they are corrections of relative order Lambda^2 p^2 (rho-bar-weighted). (ii) The sign comparison above is between the covariant EH piece (N_tot/6 x (-1/4)) and the eta-contracted piece (+1): N_tot > 24 is needed for the TT-type form to keep the sign of a positive induced 1/G. With the manuscript's 32 Phi components, N_tot = 34 would exceed 24 only if all 32 enter as free scalars of form (item 1) with a common cutoff and without mixing with a^mu; that is an input, not a result, and the Phi-a mixing on a non-central <Phi> is not computed.

### 5. What this does to Assumption `ass:emergent-op` and Lemma 2

Lemma 2's hypotheses are relaxed as follows: H1/H3 (flat scaffold with invariant vacuum) and H4 (h a fixed linear image of Phi) do not hold for the Theta-class (nonlinear, 6-dimensional, non-invariant background), H2 (rotation-preserving regulator) does not hold (K_Theta-built operator). The result: (a) the **form** of `ass:emergent-op` (operator of eq:O-eta built from a metric, with a specified E) holds for the Presentation-A scalar sector for the metric G, with no scaffold metric in the scalar sector; (b) the connection sector carries an eta-contracted term of the same order. The remaining content of `ass:emergent-op` is (i) <Phi>/v = coframe omega (not derived), (ii) Moyal corrections, (iii) the sector sum with the correct field content and mixing. This narrows the premise; it does not discharge it.

### 6. Literature

`Steinacker2010` (in bib; arXiv:1003.4134, CQG 27:133001): the abstract was fetched and confirms that matrix-model fluctuations couple to an effective metric in the semiclassical limit; I did not compare its operators or normalization. Blaschke-Steinacker, arXiv:1003.4132 (CQG 27:165010): the abstract was fetched ("gravitational actions, especially Einstein-Hilbert, derived from additional terms added to Yang-Mills matrix models"); not cited in the proposed text, not compared. `Steinacker2023`, arXiv:2411.02598: **not independently verified** (not re-fetched). All results above were derived independently here.

## Claim classification

| Claim | Class |
|---|---|
| L = D_mu D^mu = rho^-1 d(rho K d), Liouville, [D,D] = {Theta,.} | established identity (Jacobi; symbolic block family, numeric generic) |
| O_s = -D^2 + E on G with omega = -1/2 d ln rho; sqrt\|G\|(R_G/6 - E) = rho R[g_rho]/6 | established identity (hand proof; symbolic and generic numeric checks) |
| Lambda^2 term = -(Lambda^2/192 pi^2) int rho R[g_rho] per component | conditional (Poisson limit; truncated expansion of thm:Geff; constant Lambda; Euclid) |
| G = eta_AB e^A e^B for e = eta^-1 Theta^-1, antisymmetric coframe | established identity (symbolic/numeric, both signatures) |
| rank(Theta -> G) = 6; no diffeo orbit in tangent space | computed at sampled points; generic claim not proved |
| (O_v, omega, E) of the connection sector; sqrt\|G\| tr(R_G/6 - E) = (4/6) rho R + rho^2 X | established algebra given the stated quadratic action (block family exact; generic point numeric) |
| quadratic action in background gauge from eq:Smatrix in the Poisson limit | conditional (leading order only; off-shell; gauge choice) |
| X not a function of (G, rho) by the one covariant candidate 2K dln rho dln rho | numerical comparison only; no general non-covariance theorem claimed |
| eigenvalues +1, -1/4, -3/4 (units rho-bar^2 p_eta^2) | computed symbolically in p for six (signature, a, b) cases; FP cross-check |
| c_TT = 1 - N_tot/24, c_S = 1 - N_tot/8 | conditional on the model and on N_tot counting |
| f(rho) cutoff: TT unchanged, third mode 1 - N_tot(2s+3)/24 | conditional; TT part follows from delta rho = 0; third mode sampled numerically plus linearity |
| bounded obstruction: Presentation-A connection sector gives rho R[g_rho] plus eta-contracted X | conditional on the hypothesis class listed in Result |
| e[Phi] = coframe omega | **unresolved** (not derived) |
| Moyal corrections, fermions, Phi-a mixing, locked-block ghosts | **unresolved / not treated** |

## Proposed changes

Single file: `chapters/appH-microscopic-proofs.tex`. One new paragraph.

**Anchor.** Insert immediately after the paragraph "What the two preceding results imply for Problem~F (conditional; not closure)." (appH L1627-1648), whose last sentence is quoted below (occurs once; grep over `chapters/`), and before `\section{Problem G: HBEV}` (once, appH L1650):

> "... Presentation~A in general. No value or sign of \(G_{\mathrm{eff}}\) follows. Problems~B, C, D and~F remain open."

**Kept:** everything above the insertion point; nothing is replaced or removed. Labels used, each verified to occur exactly once in `chapters/`: `rem:ch3-varying-theta`, `rem:ch3-trace-quadratic`, `thm:Geff`, `eq:O-eta`, `eq:W-expand`, `eq:g-from-e`, `eq:vev-is-frame`, `def:composite-metric`, `eq:Smatrix`, `ass:emergent-op`, `sec:status-D`. Citation key `Steinacker2010` exists in `bib/namcg.bib`. No new label is introduced. `\LUV` is an existing macro used elsewhere in appH. The symbols a^mu (matrix gauge potential; as in `rem:ch3-trace-quadratic`) and \mathcal B are used to avoid the existing coefficients A, B, C and the connection A_mu.

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
truncated expansion of Theorem~\ref{thm:Geff}. Signs refer to the
Euclidean section \(\eta=\delta\); the algebraic identities do not
depend on the signature.

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
so the \(\Theta\)-built metrics form a six-parameter subfamily of the
metrics, and at generic \(\Theta\) and \(p\) no pure-gauge perturbation
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
\(\Theta^{01}=a(x^0,x^1)\), \(\Theta^{23}=b(x^2,x^3)\) one finds
\(X=2K^{\mu\nu}\partial_\mu\ln\rho\,\partial_\nu\ln\rho\); for a
generic Poisson bivector this fails.

\emph{Quadratic form about constant \(\bar\Theta\).} Let
\(\Theta=\bar\Theta+\epsilon T\), \(T^{\mu\nu}
=\bar\Theta^{\mu\rho}\partial_\rho a^\nu-\bar\Theta^{\nu\rho}\partial_\rho a^\mu\),
\(a^\mu=u^\mu\cos(p\cdot x)\). With \(q^\mu=\bar\Theta^{\mu\rho}p_\rho\),
the phase-averaged second-order terms of \(\rho R[g_\rho]\) and
\(\rho^2X\) are quadratic forms on the three-dimensional quotient by
\(u\propto q\). Relative to the tree-level kernel
\(M=q^2\eta-qq\) of Remark~\ref{rem:ch3-trace-quadratic}, with
\(p_\eta^2=\eta^{\mu\nu}p_\mu p_\nu\) and
\(\bar\rho=1/|\operatorname{Pf}\bar\Theta|\), their eigenvalues are
\(\bar\rho^{2}p_\eta^2\) (three modes) for \(\rho^2X\), and
\(-\tfrac14\bar\rho^{2}p_\eta^2\) (two modes with \(\delta\rho=0\), for
which the linearized Einstein--Hilbert form of \(\delta g_\rho\) equals
that of its transverse-traceless part with respect to \(p\) and
\(\bar g_\rho\)) and \(-\tfrac34\bar\rho^{2}p_\eta^2\) (one mode with
\(\delta\rho\ne0\)) for \(\rho R[g_\rho]\). Let \(N_{\mathrm{tot}}\) be
the weighted number of components of scalar type, plus the net \(2\) of
the connection sector. In the Euclidean section the \(\LUV^2\)
quadratic form is
\(-\tfrac{\LUV^2}{32\pi^2}\bar\rho^{2}p_\eta^2\,
(1-N_{\mathrm{tot}}/24)\,M\) on the two transverse-traceless-type
modes and \((1-N_{\mathrm{tot}}/8)\,M\) on the third. The
Einstein--Hilbert-type piece has the sign of a positive induced
\(1/G_{\mathrm{eff}}\) in the first form only if \(N_{\mathrm{tot}}>24\);
for the connection sector alone \(\rho^2X\) has the opposite sign and
dominates. Both pieces are multiples of \(M\) by functions of
\(p_\eta^2\), so they do not move the cone \(q^2=0\), and about a
constant background they do not fix \(G_{\mathrm{eff}}\).

If \(\LUV^2\) is replaced by \(\LUV^2f(\rho)\) (a local proper-time
cutoff on the diagonal heat kernel), the coefficient of
\(R[g_\rho]\) becomes \(f(\rho)\rho\); with
\(\hat g=f\rho\,g_\rho\),
\(\int f\rho R[g_\rho]=\int\sqrt{\hat g}\,[\hat R
-\tfrac32\hat g^{\mu\nu}\partial_\mu\ln(f\rho)\partial_\nu\ln(f\rho)]\).
The factor on the two transverse-traceless-type modes is unchanged, and
for \(f=\rho^s\) the third becomes \(1-N_{\mathrm{tot}}(2s+3)/24\).

This is a computation for Poisson-limit operators of a bosonic
four-dimensional matrix gauge sector in a stated gauge, about an
off-shell or constant background. It does not identify \(G\) with the
emergent metric of Chapter~\ref{ch:vierbein-emergence}, does not
treat Moyal corrections at the cutoff, fermionic or additional scalar
fields, the mixing of \(\Phi\) with \(a^\mu\), the locked-block
diffeomorphism and local-Lorentz ghosts, or the relation of the induced
term to the tree-level term of~\eqref{eq:Smatrix}, and gives no value or
sign of \(G_{\mathrm{eff}}\). The kinetic metric and regulator here
are built from \(\Theta\), and the map \(\Theta\mapsto G\) is nonlinear,
so the hypotheses of the preceding scaffold-rotation paragraph do not
apply; no linearized-diffeomorphism invariance is claimed.
Problems~B, C, D and~F remain open.
```

**Stale passages elsewhere:** none found that this block makes false. `rem:ch3-varying-theta` states that the Poisson-trace operator is not the Laplace-Beltrami operator and "need not have the same spectrum or heat kernel": consistent (here it is Laplace type with a drift connection omega and E, and the identity is for R[g_rho], not for the toy-model tilde R). appH L1631-1648 ("an ingredient that ties derivative indices to tangent indices") and the ch17 F missing step are consistent with, and not contradicted by, the new block.

## Verification scripts

All in `proposals/005-F-presentationA-EH/` (sympy 1.14.0 / Python 3.11 on this machine); outputs are saved next to each script. Checks, not proofs.

| Script | Output | What it checked |
|---|---|---|
| `check_vector_sector_block.py` (arg -1 or +1) | `check_vector_sector_block.out.txt`, `..._euclid.out.txt` | Block family a(x0,x1), b(x2,x3): Jacobi, Liouville, EL operator of the unreduced gauge-fixed Lagrangian = eta O_v, D_mu D^mu = L, -D^2+E = O_v, scalar identity (4a), vector identity (4b) with X = 2(a_0^2 - a_1^2 + b_2^2 + b_3^2) (Lorentz) |
| `check_vector_sector_generic.py` | `check_vector_sector_generic.out.txt` | Same on a generic Poisson bivector (Darboux pushforward with random rational polynomial embedding, rho non-constant), at a rational point: EL = eta O_v, -D^2+E = O_v, scalar and vector identities (all zero) |
| `check_xspin_generic.py` | `check_xspin_generic.out.txt` | Generic point: X = -2.878..., 2 K dln rho dln rho = 2.548..., Liouville numeric |
| `check_soldering_and_frames.py` | `check_soldering_and_frames.out.txt` | K^-1 = e eta e^T for e = omega eta^-1 (both signatures); antisymmetry of eta e; K eta has two double eigenvalues; rank 6 of Theta -> K^-1; conformal-frame formula (difference = 6 d(sqrt g Omega g d Omega)) |
| `check_class_vs_diffeo.py` | `check_class_vs_diffeo.out.txt` | dim(T cap S_p) = 0 at generic points; exceptional Euclidean a = b (rank 4, dim 2) |
| `check_quadratic_form.py` / `check_quadratic_form_sym.py` | `check_quadratic_form.out.txt`, `check_quadratic_form_sym_*.out.txt`, `quadratic_forms_*.srepr` | Brute-force Ricci scalar to O(eps^2) of g_rho(Theta-bar + eps T); gauge invariance M q = 0 symbolic in p |
| `analyze_quadratic_forms.py`, `analyze_quadratic_forms_symbolic.py` | `analyze_quadratic_forms*.out.txt` | Generalized eigenvalues relative to M on the quotient; symbolic in p for six (signature,a,b) cases: +1 (x3), -1/4 (x2), -3/4 (x1) in units rho-bar^2 p_eta^2 |
| `check_fp_crosscheck.py` | `check_fp_crosscheck.out.txt` | Independent Fierz-Pauli recomputation of <(rho R)^(2)>: equals the brute-force matrix (both signatures) |
| `check_tt_content.py` | `check_tt_content.out.txt` | Two-fold eigenspace: delta rho = 0, FP form = TT projection; the one-fold mode has delta rho != 0 |
| `check_cutoff_split.py` | `check_cutoff_split.out.txt` | rho0 L_FP and rho1 R^(1) eigenvalue split (sampled p, two cases) for the f(rho) cutoff |
| `check_internal_connection_vs_LC.py`, `check_B_equals_LC_generic.py` | `.out.txt` | Block family: B_sigma = LC spin connection of G in the frame e; generic: not equal |

Run from the proposal folder: `python <script> [args]`; the `check_quadratic_form_sym.py` runs take about one minute each and write the `.srepr` files that the analysis scripts read.

## Decisions Taken

- **Package choice.** I combined candidates (a) and (b) because they share one derivation: the Presentation-A Poisson-limit operator set. (a) alone would give a Theta-built-metric result with no statement about the Chapter-4 composite metric; the frame lemma (item 2) is a two-line consequence of the same algebra and sharpens the 004 caveat into one identifiable missing link (the identification of <Phi>/v with omega). I did not take (c) (non-invariant vacuum in Presentation B): there is no matrix-derived definition of such a vacuum in the manuscript and the computation would not touch the Presentation-A kinetic metric that 004 identified.
- **No fundamental metric, no S1.** The Theta-built G and the contraction eta are objects of the matrix model (eq:Smatrix already contracts with eta); nothing here turns eta or G into a fundamental spacetime metric, and I do not reorient F to "matrix fluctuations" (004's S1). The result is stated about a sector of the Presentation-A operator set.
- **Cutoff.** The manuscript uses a constant Lambda_UV in every computation; I treat the local cutoff as a parametrized variant f(rho) and state which results depend on it, rather than choosing one.
- **No ch16 inventory entry / no new assumption label.** The identification of <Phi>/v with the coframe omega is recorded in the proposed text as a hypothetical ("if ... were identified"), not as an assumption with a label. Adding it to the ch16 inventory would be an author-approval item and is not proposed.
- **Claims I did not make.** I did not claim that X cannot be rewritten covariantly (only one candidate was tested, and at quadratic order about a constant background it is indistinguishable from a multiple of the covariant EH form); I did not claim B_sigma is the Levi-Civita connection (false for a generic Poisson bivector, true on the block family); I did not use a physical "G_eff" statement from the quadratic forms.

## Milestone assessment

- **M2 (candidate, bounded):** a reproducible obstruction for the Presentation-A route listed in the integrated text as "not covered": within the stated hypothesis class (Poisson limit, bosonic 4D matrix gauge sector, minimal background gauge, constant background, Euclid signs) the connection-sector Lambda^2 term is the covariant EH term of g_rho plus an eta-contracted term X of the same order, and the TT-type form keeps the EH sign only for N_tot > 24. It rules out reading the Presentation-A Lambda^2 term as a pure EH functional of the Theta-built metric; it does not rule out the route beyond the hypotheses (fermions, Moyal terms, Phi mixing, internal local frame, other gauges are the relaxations).
- **Not M1.** The scalar-sector form of `ass:emergent-op` is a conditional sub-lemma; the identification with the Chapter-4 frame, the locked block, the ghosts and the sector sum are not derived. No critical-path step is derived from the matrix theory.
- No M3 (no merged claim is wrong; the check against appH L1631-1648, `rem:ch3-varying-theta`, ch17 F missing step found no conflict), no M4 (no label change), no M5.

## Status-label recommendation

None. F, A, B, C, D1, E, G-derived and N stay OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL. No label edit appears in the proposed LaTeX.

## Author decision needed

None for this proposal. Later, optional: whether to list the soldering identification <Phi>/v = coframe omega as a named assumption in the ch16 inventory if and when a derivation attempt for it is made (an inventory edit is an author-approval item).

## Remaining open step

To close the original F target (locked block, mixing, ghosts) and to discharge `ass:emergent-op`:
1. Derive, from the matrix theory, the identification of the Chapter-4 frame <Phi>/v with the Presentation-A coframe omega (or replace `ass:emergent-op` by a derived statement); this is where Problems A and D1 enter. Decide which is correct for the locked block, since the Theta-class is a 6-parameter subfamily and the locked frame has 16 components.
2. Control the Moyal corrections at p ~ Lambda_UV (at least show the structure rho R[g_rho] + eta-contracted terms survives, and fix the scheme dependence).
3. Compute the Phi-a^mu mixing on a non-central <Phi>, the extra scalar and fermionic content of an IKKT-type completion, and decide whether X is cancelled or reweighted (relaxation i); compute N_tot for the locked block with thresholds.
4. Repeat in a non-minimal gauge with an on-shell reduction (the constant-background forms are proportional to the linearized equation of motion, so only a non-constant background or sources can fix G_eff), and compare the induced term with the tree-level term of eq:Smatrix.
5. Specify the locked-block diffeomorphism and local-Lorentz ghost operators (D1); the Presentation-A gauge sector here is a different, matrix-gauge sector.
6. Continue to Lorentzian signature along the G-time direction (for Theta^01 = a the odd-signed direction of K is x^1, see `rem:ch3-moyal-check`) and recheck the sign of X.

## Special instructions for the gatekeeper

- Do not accept any statement that `ass:emergent-op` is discharged, that G_eff has a value or sign, that X is non-covariant in general, or that the Presentation-A route is excluded beyond the listed hypotheses.
- Please re-run `check_vector_sector_generic.py` (about 3 minutes), `check_vector_sector_block.py -1`, `check_soldering_and_frames.py`, `check_fp_crosscheck.py 1 1 2 1 2 3 5`, and `analyze_quadratic_forms_symbolic.py 1 1 2` (needs the `.srepr` files present). The symbolic-in-p claims rest on the `.srepr` outputs of `check_quadratic_form_sym.py` (about one minute per case).
- Re-derive by hand: (1) the quadratic action and the claim that the unreduced Lagrangian's Euler-Lagrange operator equals eta O_v (the scripts do this without relying on my integration by parts); (2) tr(B_sigma B^sigma) = -X using Theta G Theta^T = eta^-1; (3) the conformal formulas used in the scalar identity.
- Check the following specific places where an error would matter: the ghost weight -2 and gauge-fixing coefficient +1/2 (principal part must be K d d on all four components); the factor 1/2 conventions between the tree-level kernel M and the averaged forms (both are averages of quadratic forms in u, M defined as q^2 eta - q q); the claim that the phase-averaged cross terms and the {a,a} term of delta Theta drop out; the Euclid/Lorentz treatment of signs (eigenvalue ratios are signature independent, absolute signs are asserted only for Euclid).
- The N_tot > 24 criterion is conditional arithmetic on top of the computed eigenvalues; please test that the "N_tot" counting (connection sector net 2 plus N_s) is what the eigenvalue statement uses, and that the 32-component remark is clearly labelled an input.
- Anchors: the quoted last sentence of the existing paragraph and `\section{Problem G: HBEV}` each occur once in appH (verified by grep before submission). The proposed block contains no `ef` to a label outside the verified list.
- Per the autonomy directive I did not mark any label change and did not add an assumption label.
