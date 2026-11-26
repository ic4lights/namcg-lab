# Proposal 047-lichnerowicz-torsion-closed-forms, round 1

## Result

This package takes the rank-1 avenue of 046 (the background torsion and the cone at the same order) and SME route R1, and adds five results. All are conditional on the 045/046 class. Nothing critical-path is closed.

1. **Exact closed forms.** The forms sampled numerically in 045 and 046 now have closed expressions on the five traceless polarisations. They depend only on the helicity about y_perp and on one variable x = (l^2 q^2 + (q.y)^2)/(-m^2 q^2). The further form of 046 is identified as q^2 (hbar y).(hbar y). The (3/2) coth^2 tau eigenvalue is helicity two, which 046 left unidentified.

2. **Bounded no-go sharpened (exact within H1-H13, first order in torsion, J = 0 loop modes).** lambda_L = -(6/5)(2 + 1/x) depends on the wave vector. A single coefficient on the five for all q at a base point therefore requires W_R^(1) = 0 and W_X^(2) = 0. The second fails for every non-zero flux of K. So the isolated data of K that 046 left open are excluded at this order, and the 046 values M* belong to one class of q.

3. **Lichnerowicz reduction.**
   - The background torsion is exactly the Levi-Civita spin connection of G = eta/m^2.
   - For fibre-constant modes, rho-divergence-free frames give no term linear in T. For an axial-free frame the Dirac trace is the Levi-Civita Dirac trace of g.
   - The mixed term there is a functional of (g, phi), so `Q_2^D` is only one part of a curvature-squared density (background check: 3125/648 against the complete 1783/648 at (5,3)).
   - The equality of the Dirac cone value with the Einstein coefficient, which 045 inherits as "not derived", is the Lichnerowicz identity with the antiperiodic gluing.
   - The first-term form P2 is complete at order s^2.

4. **The range M ~ coth^2 tau.** The literal frozen Gaussian resummation is done in closed form. It replaces 1/M^2 by a bounded F(M), and the L/c = 0 zeros disappear in the scan. The frozen integral is not a controlled approximation, though: the terms it drops are of the same order. A scale argument (not a theorem) gives M >> m^2 q^2 >> coth^2 tau for any local two-derivative coefficient read from a frozen plane wave. So M <~ coth^2 tau is outside the local question.

5. **A favourable fork on the no-go's hypothesis "five polarisations off shell".**
   - On the null cone the two transverse-traceless polarisations (helicity +-2) have one exact coefficient for every K and n: c_T^TT = (1/6)W_R^(0) + (7/30)W_R^(1) - 2W_X^(0) - (14/5)W_X^(2).
   - By Peierls-Bogoliubov, c_T^TT > 0 for every non-zero flux, and likewise (1/6)W_R - 2W_X > 0, even though W_R has no fixed sign.
   - Against c_T^TT the periodic and smooth replicas have c_A - c_T^TT < 0. The mixed part of the fixed-state gap is also negative, so equality needs the first-term cone part or contact terms.

**R1 outcome.** It is agreement (outcome (a) of the scout). Published (3.31) has the form of the identity here, and the 046 trace regime is the regime of a K scale above the hs masses in 2411.02598. The 046 no-go is not a contradiction with that work, which makes no claim of one coefficient on the polarisations.

**What this does not do.** It does not derive G_eff, identify hbar with the emergent metric, make the Lorentzian evaluation more than formal, or close B or F.

## Target and status

Read from the current working-tree files.

- **Problem F**, `sec:status-F`, appH L1366-1369, verbatim: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion." Missing step, L1375-1382: operators, limits, continuation, scheme, and evaluation of the weighted a_1 and curvature-linear a_2.
- **Problem B**, `sec:status-B`, appH L45-47: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived."
- **Chapter 17**, `sec:ch17-done`, L693-732: item 2 (B is a lemma, including the non-conformal tensor block, no `ass:dictionary`); item 6 (F computed from the specified operators, G_eff not an input). Sub-target used here: G_T = G_A (appH normalisation paragraph, L174-179).
- **Critical-path set as read**: A, B, C, D1, E, F, G-derived, N. No discrepancy between Chapter 17 and Appendix H.
- **Dependencies**: F on D1, E and the class; B on A (replica/state) and F.
- **Classification**: PROGRAMME-CONDITIONAL. Nothing DERIVED.

## Source reading

**Digest + targeted reads.** Not a full scan.

- **Digest**: `make_digest.py --check` prints DIGEST CURRENT. Head 2172dd5, chapters-hash 1416784d1e1634a9, dirty-chapters: yes solely from the accepted 046 integration awaiting the author's commit, as the task states. I read the working-tree files directly. The check command's exit code was 1 in my compound command because of a later `wc` on a directory, not the digest.
- **No full scan due**: no definition, assumption, scope or status passage changes. The next gatekeeper scan falls under the 5th-item rule; the gatekeeper should decide its own ordinal.
- **Read in full**: digest; appH L142-207, L221-256, L1362-1385, L2180-2417 (all conjugate-coordinate paragraphs from the Theta-built heat kernel through the 046 paragraph); ch17 L685-744; MILESTONE.md; 046 proposal-r1, proposal-r3, review-r3, forms_lib, s1 (head), s3, s4 (head), s2 L150-223, s5, compile_check; sme-scout-20261101.
- **Ledger**: entries 040-046 by search; long lines were truncated by the search tool, so rejected routes rest on the 045/046 proposals and review-r3 rather than a complete ledger read.
- **Literature**: arXiv:2411.02598 PDF fetched, read Sec. 2.3 part (hs mass replacement), Sec. 3.2-3.3 (3.15)-(3.49), including footnotes 11 and 14.
- **Unreadable files**: none.

## Research and reasoning

### Why this package

Against the alternatives:

- **Rank 1 / R2 (chosen).** This is the avenue the 046 review ranks first. It turned out to decide more than resummation: once T-bar is recognised as a Killing Zeeman term and a spin connection, the 045/046 forms close analytically.
- **R1 (included).** The dictionary needed only Sec. 3 of the paper, and the identity (3.31) is the same object as the Lichnerowicz identity derived here.
- **R3 (not chosen).** The first-term cone value is already fixed by merged text (2 per mode at order Lambda^2, a log proportional to the trace of H_0^K). What remains there is replica selection, which belongs to Problem A. A same-regulator evaluation alone adds little. The first-term cone contribution enters only as the term named at the end of "Sign and replicas".
- **Rank 2 (Schur).** Explored only for the inert amplitudes in the induced forms (s7). It changes helicity +-1 only at three cases. The full elimination is recorded as open.

### 1. Exact background structure (s1)

In the polynomial Lie-Poisson algebra, for both bracket signs:

- F^{ab} = {T^a,T^b} = c M^{ab}, with c = sign of the bracket. So the background flux operator is c J^{ab}, and {F^{ab},y^mu} = eta^{a mu} y^b - eta^{b mu} y^a = Tbar^{ab mu}.
- [Box, J^{ab}] = 0 (appH already states this), hence e^{-sH_i} = e^{s Box} e^{s c Sigma_i^{ab} J_ab} for every species without masses.
- H_i^0 = C_31^{tot,i} - C_41 - C_{Sigma_i}, with C_Sigma = -3 (vector) and -3/2 (Dirac). The vector case is merged; the Dirac case is new. The sign of the index action in C^tot is -c.

In the chart, with m^2 = -y.y - l^2, rho = 1/m, E^{a mu} = m eta^{a mu}:

- Tbar^{ab mu} = [E^a,E^b]^mu;
- d_mu(rho Tbar^{ab mu}) = 0;
- omega_LC mu^{ab} = G_{mu nu} Tbar^{ab nu} for G = eta/m^2 (exact, symbolic).

Also R[G] = 18 c - 24 and e = R/6 + E_0 = 2 - (3/4)c, with c = -y.y/m^2 (= coth^2 tau at y^i = 0). Both hold at the rational points tested. The first matches e + a = -R/12 with a = -(3/4)c, and sqrt|G| e equals the merged (5m^2 - 3l^2)/(4m^6).

### 2. Fibre-constant reduction and the general identity (s2)

For loop modes with J = 0, the J = 0 block of Box_X is rho^{-1} d_mu(rho <E^{a mu}E_a^nu> d_nu), because Hamiltonian fields are Liouville-divergence-free. Up to order epsilon^2 with the second-harmonic product <dE dE>, that is the square of the averaged frame fields Ebar^a. Why this product is lower order in the variables here:

- with h fixed, a phase-averaged <dE dE> enters as a single insertion;
- its non-oscillating part has no power of q in h-counting, so it contributes at q^0 h^2, while the forms here are q^2 h^2;
- its oscillating part averages to zero against background data.

The torsion of the J = 0 block is T^{ab mu} = rho^{-1} d_nu(rho <E^{[a|nu|}E^{b]mu}>), which is antisymmetric in nu, mu. Hence d_mu(rho T^{ab mu}) = 0 identically, and at the order considered T = [Ebar^a, Ebar^b].

Write -H = gamma dd + b d with b^mu = rho^{-1} d_nu(rho g^{nu mu}) - B^mu, B^mu = kappa Sigma_ab T^{ab mu}, kappa = -1. Gilkey's form then gives:

- connection omega_mu = d_mu phi - (1/2) B_mu, with phi = (1/2) ln(rho/sqrt|g|);
- endomorphism E = E_0 + W - (1/4) B.B, with E_0 = -Box_g phi - |d phi|^2 and W = (1/2) rho^{-1} d_mu(rho B^mu) = 0.

So W = 0 exactly. There is no term linear in T.

The Dirac operator DD = Gamma_a Ebar^a satisfies DD^2 = Box + (1/2) Gamma^{ab} Z_ab (merged). It is similar through f = (rho/sqrt|g|)^{1/2} to the Levi-Civita Dirac operator of g, up to the axial term (standard frame identity):
Gamma_a Ebar^{a mu} d_mu + (1/2) Gamma_a rho^{-1} d_mu(rho Ebar^{a mu}) = f^{-1} DD_LC f, plus the axial term.

s2 tests the resulting scalar identity at random exact two-jets of arbitrary rho-divergence-free frames:

(1/4) g_{mu nu} tr_D Z^mu Z^nu = -R + 4 Box phi + 4 |d phi|^2 -+ (1/8) A_a A^a,

with fitted coefficients exactly (-1, 4, 4, -1/8) for eta and (-1, 4, 4, +1/8) for delta, zero residual on ten points each. Z.Z is scalar plus a Gamma_5 part, with coefficient -(1/4) eps(T.T).

### 3. Complete a_2

From section 2, the Dirac index part of a_2 (Dirac minus four scalars, mod total derivatives) is

e tr A + (1/2) tr A^2 + (1/12) tr Omega^2, with A = -(1/4) B.B and Omega = -(1/2) dB + (1/4)[B,B].

By powers of Sigma:

- Sigma^4: (1/32) tr(B.B)^2 + (1/192) tr[B,B]^2. This is exactly Q2 of 046, as can be seen from the expansion (1/32 - 1/96 = 1/48 = 2/96, and 1/96).
- Sigma^2 and Sigma^3: e tr A, (1/48) tr(dB)^2, -(1/48) tr(dB [B,B]). These are absent from the frozen symbol. They are of the same order, since d(y/m^2) ~ yy/m^4 + 1/m^2.

For an axial-free frame the Lichnerowicz form gives the sum as R^2/72 - Riem^2/24 - 2 e^2. s4 (D) checks tr Omega^2 = -(1/2) Riem^2 and the equality of the two expressions at two exact points, and gives frozen 3125/648 against complete 1783/648 at (5,3), and 4805/5408 against -14905/5408 at the second point.

**First term.** In v^M - 2 sigma^M every term with fewer than four Sigma, and the tr[B,B]^2 term (a Dynkin-index trace), cancels by the species sums already merged for the four-coordinate class (appH L228). What survives is (1/32)[tr_V (Z.Z)^2 - 2 tr_D (Z.Z)^2], the analogue of (1/2) S_4. So P2 of 046 is complete at order s^2 at J = 0.

### 4. Closed forms (s3, by hand plus exact checks)

Let n be the fibre vector. At y^i = 0, M^{i0} = m n^i and M^{jk} = chi l eps_{ijk} n^i give v.v = m^2 q_0^2 + l^2 |qvec|^2 - y0^2 (n.qvec)^2. So:

- G_ij = a delta_ij - (a-b) qhat_i qhat_j, with a = l^2 q^2 + (q.y)^2 and b = -m^2 q^2;
- D traceless on G splits under rotations about qhat into: helicity 2 (block orthogonal to qhat), helicity 1 (D_{0i}), helicity 0;
- with f = tr(GDGD): tr(DGD)/f = 1/a + ((a-b)/(ab)) phi for phi = 0, 1/2, 2/3, and tr(D^2G^2)/f = 1, (a^2+b^2)/(2ab), 1.

**Forms.** With alpha = n^i D_ij s_j, q.alpha = 0:

- X_hat = m^-4 q^2 (v.v)(alpha.alpha), <n n n n> = (dd+dd+dd)/15, and EH = -q^2 tr(GDGD)/(18 m^4) (from EH2 with h = (2m/3) D s s).
- This gives IX2 eigenvalues -(6/5)[2 + (2+1/x)(1+(x-1)phi)].
- With F1 = -q^2 [2 (alpha.v)^2 + (alpha.alpha)(v.v)], SC2 gives (1/20)[4 + 2r + (2+1/x)(1+(x-1)phi)], with r = (x+1/x)/2 on helicity 1 and 1 otherwise.
- Averaged: dTbar^{ab mu} = -(1/2)(q^a hbar^{b mu} - q^b hbar^{a mu}) (checked, relative 2e-16), Q1 = q^2 hbar.hbar/(4m^2) = -2 m^4 EH.

**Torsion forms.** With F = Tbar.k + t dF, u = hbar k, A_2 = q^2 u.u/4, A_1 = -[(k.q)(y.u) - (k.u)(y.q)], P_1 = -eps(k,y,q,u), Lam^2 = (k.y)^2 - k^2 y^2:

- tr_D e^{-sZ} = 2C(A+iP) + 2C(A-iP), tr_V e^{-sZ} = 4 C(A+iP) C(A-iP), C(w) = cosh(s sqrt w). So V - 2D = 4(C_+ - 1)(C_- - 1), the t8-type character of appH L2288.
- t^2 coefficient at s^4: D: (s^4/6)(-2 Lam^2 A_2 + A_1^2 - P_1^2). V - 2D: s^4 (-2 Lam^2 A_2 + A_1^2 + P_1^2).
- Isserlis averaging in q = (q0,0,0,q3), y = (y0,0,0,0) gives symbolically (s3 part B, rational identities in q0, q3, y0, m): Q2_D/m^4 = (3/2)coth^2 + (x-1)phi and P2/m^4 = 9 coth^2 + (x-1)(8-6phi), with <P_1^2>/unit = (x-1)(4-6phi). Rotations and boosts preserving y^i = 0 reduce to this q without loss, since the fibre average is rotation-invariant.
- Hence lambda_L = -(6/5)(2+1/x), reproducing -1.956233 of 046 at x = -2.70412.

**Numerical agreement over the 18 cases (10 from 046, 8 random):**

| Form | Worst error | Note |
|---|---|---|
| IX1 | 3.5e-13 | |
| SC1 | 6e-14 | |
| IX2 | 4.6e-11 | |
| SC2 | 2.1e-12 | |
| Q2D | 4.3e-6 | polynomial-interpolation routine at large eigenvalues; relative tensor residuals at most 3e-7, symbolic part exact |
| P2 | 1.8e-5 | as for Q2D, relative tensor residuals at most 5e-7 |

The range -3.31 <= lambda <= -0.32 in 046 was a sample range. lambda_L runs over -(6/5)(2+1/x), including positive values where m^2 >= 2 l^2 (s3: +4.51 at (13,12)). The 046 statement is correct for its seven points. The insert states the function.

### 5. Wave-vector dependence and the tuned-data exclusion

Eigenvalue of the full form at first order in torsion on J = 0 modes, with x-independent K-weights W_2 (of Q2_D) and W_3 (of P2):

W_R^(0)/6 + W_R^(1)[(1/20)(4 + 2r + (2+1/x)(1+(x-1)phi)) - 1/6] - 2W_X^(0) + W_X^(2)[lambda_IX2 + 2] + W_2[(3/2)coth^2 + (x-1)phi] + W_3[9 coth^2 + (x-1)(8-6phi)].

Independence of helicity and x on the open sets of x fixed by the sampled range of q:

- helicity-1-only term: W_R^(1) (x-1)^2/(20x), so W_R^(1) = 0;
- phi term: (x-1)[(2+1/x)(-(6/5)W_X^(2) + W_R^(1)/20) + W_2 - 6W_3] = 0 for all x, so W_X^(2) = 0.

W_X^(2) = -(1/8) int s^-2 tau^K B_0 with tau^K >= 0 (merged) and B_0 > 0, so it is strictly negative for non-zero flux. The earlier M* rows are therefore one-x statements. s5 (N) gives M* at eight values of x, e.g. n = 30, L/c = 0: 0.29196 at x = -2.70412, 0.22312 at x = 1.32902. Thus claim 15b of 046 is negative at this order. The relaxation is H12: J >= 1 torsion carries its own x-dependence, and that is not computed.

### 6. Frozen resummation (s4, s5 F)

Exact radial integrals give

<D2>_h = unit (-2s) e^{-xi/2} [1 - (1+nu phi) xi + (2/15 + nu phi/5) xi^2], xi = s coth^2 tau / 2, nu = (x-1)/coth^2 tau,

verified symbolically at four q (s5 F) and against a brute-force matrix-exponential Gauss quadrature to at most 3e-8 relative (s4 B). Background traces: 4(1-xi)e^{-xi/2} and 2 + 2(1-4xi)e^{-2xi}.

With M_t = M + coth^2/4, F(M) = 1/M_t^2 - (coth^2/5)/M_t^3 > 0.

Consequences:

- N_frozen(M;x) = W_B lambda_L + F(M) + 24(L/c)/M^2 has no root at L/c = 0 in 960 (n, x) pairs (c = 25/9), because F is bounded by 3.2/coth^4 at M = 0 where the first-order 1/M^2 diverged.
- At L/c = 1, 10 the roots shift by under 2% (largest listed 1.66%, n = 300, x = 1.33, L/c = 1).
- Note that "no electric growth" holds here: k-integration turns boost eigenvalues into Gaussian decay in this formal evaluation. That is specific to the J = 0 sector and to the formal Gaussian moments. It does not bear on the merged electric-growth statements for fixed covectors.

### 7. Locality scale argument (classified conjecture/mechanism, not theorem)

The frozen plane wave needs m^2 q^2 above the background variation scale. Exact background data: the G-norm of d ln m is coth^2 tau in Box units, R[G] = 18 coth^2 - 24, e = 2 - (3/4)coth^2. The two-derivative truncation at weight s ~ 1/M needs m^2 q^2 << M. Together: M >> coth^2 tau. Below that, no local two-derivative form is defined by this method. A nonlocal effective action could exist there, and nothing here excludes it.

### 8. Null cone and sign (s5 O, P, G)

As q^2 -> 0 at fixed q.y != 0: x -> infinity, yhat_perp -> direction of q, and hbar y_perp = 0 means the TT polarisations in the gauge hbar_{mu nu} y^nu = 0. Eigenvalues: IX2 -> -24/5, SC2 -> 2/5, checked numerically at q^2 = 0.21, 0.0201, 0.002.

The form per polarisation is (finite) q^2 hbar.hbar, so the pole stays at q^2 = 0, apart from the first-term piece 8(x-1) f_1 = 8[y^2 q^2 - (q.y)^2] hbar.hbar/m^2, which shifts it (pole at q^2 proportional to (L/c)(q.y)^2/(M^2 W m^2)). This cone shift of the helicity-two pole relative to G, from the first term, is a finding in its own right. It is flagged as model-level because L is not computed.

**Positivity.** tr Sigma = 0 gives <Z> = 0 in the state e^{-s H_0}, so Peierls-Bogoliubov gives v^K, tau^K >= 0 for Hermitian Zeeman coupling (s5 P: random non-commuting data, 72 evaluations, all positive). B_0 - B_1 = int (1 - 6a(1-a)) e^{-xa} da >= 0: 1 - 6a + 6a^2 is the shifted Legendre P_2, and e^{-xa} is convex with positive P_2 coefficient. Then:

- averaged: (1/6)W_R - 2W_X = (1/6)V + (1/12)T > 0; for four coordinates (1/6)W_R - 4W_X = (1/6)V + (1/3)T > 0;
- on TT: c_T^TT = (1/6)V_0 + (1/12)T_0 + (7/30)(V_1 - T_1) + (7/20)T_2 >= (1/6)V_0 + (1/12)T_0 + (7/30)V_1 + (7/60)T_2 > 0.

This does not contradict the merged statement that W_R has no fixed sign, nor "no value or sign of G_eff follows" (which also rests on K, the emergent-metric identification, and the Wick question). It does add a fact: the sign of these coefficients in the class does not depend on the sign of W_R. Assumed: V_i, T_i finite. If H_V^K has a negative mode, V diverges and the proper-time representation fails; merged text already covers that.

**BPS-type K (s5 B).** For commuting fluxes with f1 = f2 + f3 on every mode, v^K = tau^K identically (from 4 cosh(a+b) cosh a cosh b = cosh(2a+2b) + cosh 2a + cosh 2b + 1), so every W_R vanishes and the scalar leak is absent. No such K is constructed here. Note that the merged mixed term assumes the K flux operators need not commute; for this statement they must.

**Replicas.** From the merged cone values:

| Replica | c_A - c_T^TT |
|---|---|
| periodic | -(1/4)T_0 - (7/30)(V_1-T_1) - (7/20)T_2 < 0 |
| smooth | -(1/4)V_0 - (7/30)(V_1-T_1) - (7/20)T_2 < 0 |
| fixed-state, finite mixed part | -(7/30)(V_1-T_1) - (7/20)T_2 < 0 |

The fixed-state replica has in addition the positive cutoff-dependent first-term part. So equality on TT is possible only through that part or through contact/edge terms: one condition, not derived.

### 9. Cone at the same order

For the mixed term in the axial-free J = 0 sector, merged L248 states that the first-order surface term is the cross term of the bulk a_2 with conical deltas. Applied to R^2/72 - Riem^2/24 - 2e^2 with only the geometric deltas (rho regular, fixed state), it gives (1-n) pi [R/9 - R_ijij/3 - (8/3) e].

The Dirac part reproduces the merged Dirac weights: (pi/9) R matches -(1/2) c_B tr(R/6 - R/4), and -(pi/3) R_ijij matches -(1/2) sum a_k^2 tr(gamma^12 Omega_12) with Omega the LC curvature. The latter requires merged units to carry the relative factor 4 pi implied by the ratio 3/2 : 1 of X' to tau_Omega in the merged sigma_log. I checked that ratio; the spin term is not separately re-derived, and this is stated as "matches".

Inference: at J = 0 the cone at this order is the Wald-type variation of the same density, so it is not independent. This inherits the assumption that the geometric deltas are the complete delta content (as flagged in merged L254).

### 10. Dictionary with arXiv:2411.02598 (verified in the full text I read)

- (3.15)-(3.21): flux operator as Weitzenboeck torsion on plane waves, hs-valued. Footnote 11: hs generators dropped, stated as appearing subleading.
- (3.31): R = -(1/2) H_grav - (1/2) T_mu T^mu + dilaton terms, the same form as section 2. The normalisation of their dual is not compared.
- (2.36)-(2.37) and footnote 14: m_s replaced by a generic positive scale m_J, K scale above J scale, modes truncated at J where hs masses are neglected. That is the 046 trace regime (mu_J << M). In (3.46)-(3.48) the trace produces the J^2 factor, which matches sum_{J<=n}(2J+1) in W_1 up to the replacement of mu_J by one scale.
- (3.33): 1/G_N is proportional to Tr_hs of the K[2] weight, and (3.32) says "EH is part of" the action. No statement of one coefficient on polarisations was found in these sections.

So outcome (a): agreement, not contradiction, as a dictionary of structures. Not independently verified: JHEP reference (from the scout); the rest of that paper; 2601.08031 "mirage matter". The J(J+2) vs 3s question is not resolved here: that paper replaces m_s by a positive scale and calls the negative sign an artefact, so it does not fix the spectrum, and the conclusions here do not use it.

### 11. Fork record for the sharpened no-go

Hypotheses and what each avenue gave:

| Hypothesis | Relaxation | Explored? Outcome | Rank of what stays open |
|---|---|---|---|
| Five traceless, all q | Two on-shell TT polarisations | Done: one coefficient, positive | follow-up: gap, Newtonian coupling, cone shift |
| H12: first-order torsion | Frozen exact resummation | Done: closed; invalid beyond xi small as an approximation | replaced by complete a_2 |
| H12: frozen symbol, J = 0 | Complete a_2, LC form | Structure done; second variation of the curvature-squared density at q^2 h^2 not computed | 3 |
| H12: J = 0 only | Torsion on J >= 1 loop modes | Not done; only route that can restore x-independence | 1 |
| Cone not at same order | Wald cross term | Done conditional on delta content | 5 |
| Inert = 0 | Schur with induced forms only | Done at 3 cases: helicity +-1 only, TT unchanged | tree-included elimination: 2 |
| Level-one frame rank one | Other fibre amplitudes | Lead only: see below | 2 |
| H10 cross term | Include in weights | Not done; on null cone needs m q components below sqrt M | 6 |
| S^2-M first term | Compute | Not done | 4 |
| Product K | Equivariant K / mixed flux | Not done | 7 |
| Single-scale K | Any K: W's general; BPS commuting flux | Partial: W_R = 0 lemma | no K construction, 8 |

**Lead for rank 2, not in the insert.** The index form is ultralocal on the fibre, <(v.v) alpha(n).alpha(n)>. With hbar = <alpha sym v> held fixed and all fibre harmonics of alpha free, stationarity gives alpha^mu = Lambda^{mu nu} v_nu/(v.v), so the form is tr(Lambda P Lambda) with hbar = Lambda P + P Lambda, P = <v v/(v.v)>. This is proportional to hbar.hbar exactly if P is isotropic on the three-space. It is not isotropic for x != 1, and v.v changes sign on the fibre for x < 0, so a principal value is needed. Conjecture-level; a later package should compute it with the tree form.

## Claim classification

| # | Claim | Class |
|---|---|---|
| 1 | F^{ab} = c M^{ab}, Tbar formula, [Box, J] = 0, H_i^0 Casimir form (V, D) | established (exact, polynomial algebra) |
| 2 | Tbar = LC spin connection of eta/m^2; divergence; R[G] = 18c - 24; e = 2 - 3c/4 | established (exact symbolic; two closed forms by evaluation and identity) |
| 3 | d_mu(rho T^{ab mu}) = 0 for J = 0 block; W = 0 | established |
| 4 | Index identity -R + 4 Box phi + 4 |d phi|^2 -+ A^2/8 | established at random exact jets; the structure is the standard Lichnerowicz/Weitzenboeck identity |
| 5 | Closed forms IX2, SC2 | established (exact derivation; numerics agree) |
| 6 | Closed forms Q2_D, P2; lambda_L(x) | established (symbolic rational identity at the q-plane; numerics agree) |
| 7 | Identification of the further form and of helicity two | established |
| 8 | Exclusion of isolated K data for all q | conditional (H1-H13, first-order torsion, J = 0); exact within that |
| 9 | M* depends on x | established within the model; numbers single-scale |
| 10 | Frozen closed resummation; F(M) | established as a statement about the frozen integral |
| 11 | L/c = 0 zeros absent | numerical scan, frozen integral, c = 25/9 |
| 12 | Terms dropped by freezing are of the same order | established (a_2 decomposition, exact background numbers) |
| 13 | Locality M >> coth^2 tau | conjecture/mechanism (scale argument) |
| 14 | Mixed term is a (g, phi) functional on axial-free J = 0 frames | conditional (order counting of <dE dE>, axial and dphi vanish at first order at leading symbol) |
| 15 | Order s^2 density of the mixed term | conditional on 14; algebra checked at background |
| 16 | P2 complete at order s^2 | established in the J = 0 reduction via species sums |
| 17 | Lichnerowicz origin of the equality of cone value and Einstein coefficient | conditional (quasi-free antiperiodic gluing of merged text, Kabat's statement cited, not re-derived) |
| 18 | Cone cross-term density | conditional (delta content assumption; 4 pi unit check by ratio, not independent derivation) |
| 19 | Fibre-point decomposition -4 EH + (alpha.v)^2; half axial | established algebraically (exact at six points; axial part checked by hand) |
| 20 | Dictionary with 2411.02598 | structural comparison, normalisations not compared |
| 21 | TT limit values, c_T^TT | established at frozen symbol under H10-H11, with W's general |
| 22 | c_T^TT > 0, averaged coefficient > 0 | conditional (Hermitian coupling, finite integrals, formal Lorentzian M); not a sign of G_eff |
| 23 | v^K = tau^K for commuting f1 = f2 + f3 | established identity; no K constructed |
| 24 | Replica gaps against c_T^TT negative | conditional (merged cone values, no contacts) |
| 25 | First-term cone shift | conditional, L not computed |
| 26 | Inert Schur: helicity +-1 only | numerical, 3 cases, induced forms alone |
| 27 | G_eff, emergent-metric identification, Newtonian limit, Lorentzian status | unresolved |

## Proposed changes

### `chapters/appH-microscopic-proofs.tex`

**Candidate text.** `proposals/047-lichnerowicz-torsion-closed-forms/appH_insert.tex` is the authoritative copy (ASCII, LF, no CR, no TAB). Its size and sha256 are in "Verification scripts".

**Anchor.** Immediately before the line `\section{Problem G: HBEV}` (exactly one occurrence, in appH only), with one blank line before the anchor. The preceding line is the 046 closing, ending "...the replicas are those of Section~\ref{sec:status-B}. Problems~B and~F remain open and PROGRAMME-CONDITIONAL." Nothing is replaced or removed. The integrator converts to CRLF.

**Labels verified** (s6): `sec:status-B`, `ch:vierbein-emergence`, `ass:lorentzian` each once. **Cites verified**: `Kabat1995`, `MantaSteinackerTran2024` one bib entry each. No new label, no new bib entry. `\mathcal S_4` and `\mathcal Z_{ab}` are existing notation in appH.

**Merged text kept, with what the new paragraph refines:**
- 046 sentence "isolated values of the data of \(K\) ... are not excluded": stands as a statement within 046; the new paragraph narrows it at first order. No edit.
- 046 "\(M^*\)" values: remain true for the stated wave vector. New paragraph states the x-dependence. No edit.
- 046 "the part of \(Q_2\) ... is the first background-torsion correction of the mixed term": new paragraph says it is the part of fourth order in Z of the complete density. No edit; this is a soft refinement. See "Special instructions".
- 045 "this inherits the equality ... does not derive": remains true of that paragraph; derived here conditionally.

**Stale passages elsewhere.** None. **BibTeX.** None new.

## Verification scripts

All are in `proposals/047-lichnerowicz-torsion-closed-forms/`. Scripts print to stdout and write no files. The saved `.out.txt` files come from shell redirection, so re-running cannot overwrite them silently. Scripts import `forms_lib.py` read-only from the 046 folder with bytecode writing disabled.

| Script | Checks | Result summary |
|---|---|---|
| `s1_exact_structure.py` | section 1 | all True for both brackets, C3/C4 zero at 3 points |
| `s2_lichnerowicz_general.py` | section 2 | fit (-1,4,4,-1/8) and (-1,4,4,1/8), residual zero, divergence zero |
| `s3_closed_forms.py` | section 4 | worst errors in the section 4 table; symbolic part zero for all helicities |
| `s4_frozen_resummation.py` | sections 3, 6 | series and brute force agree (at most 3e-8 relative), background completeness exact at 2 points |
| `s5_consequences.py` | sections 5, 6, 8; fibre-point | see output; L/c = 0 frozen scan 0 of 960; on-shell limits; identity at 6 fibre points |
| `s6_insert_mechanics.py` | insert bytes, labels, cites, anchor | all pass |
| `s7_inert_schur.py` | fork: inert | helicity +-1 only at 3 cases |
| `compile_check.py <scratch>` | scratch build outside repo | see `compile_check.out.txt`: exit codes 0, no undefined or multiply defined, CRLF preserved, scratch removed; run on the final insert |

Scratch exploration scripts stayed in the OS scratchpad and are not relied on. The chapters tree is unchanged by me (`git status`: only the pre-existing appH modification and this folder).

**Insert at submission.** 12497 bytes, ASCII, LF, 0 CR, 0 TAB, sha256 `f1ce7fdae8cb3d7291867ed5ba01f1a7f1997925dec42fae05d9856212506efa`.

## Decisions Taken

1. **Target.** Rank 1 plus R1, with rank 2 explored minimally; R3 rejected as a standalone (reason above). Favours the F/B chain because it replaces numerics by exact statements and exposes the one-coefficient TT sector.
2. **"Decide" the range M ~ coth^2 tau.** I report both the literal frozen result and why it does not decide physics. Rejected: presenting the frozen integral as the resummation answer.
3. **Fork on the five-polarisation hypothesis.** I treat on-shell TT as a within-core relaxation, keep the emergent metric composite, and leave the five-polarisation tensor requirement of the first law visibly unmet. Rejected: redefining the target of F or B, which would be a scope change, and no label moves.
4. **Sign statement.** Stated only for the K-induced coefficients in the class, with the closing sentence excluding a sign of G_eff for the emergent metric. Rejected: dropping the fact because of the earlier "no sign follows" wording, since that wording is about G_eff.
5. **046 sentences.** Not edited; refined in the new paragraph, the merged pattern for such refinements.
6. **Scope of insert.** The Schur-all-harmonics lead stays out of the manuscript text until computed.
7. **No spacetime or metric is made fundamental.** All metrics here are composite in the frame fields; the Lichnerowicz form is on g = (E E)^{-1}.

## Milestone assessment

My assessment, for the gatekeeper to decide:

- **M2 candidate (bounded):** tuned K data are excluded at first order in torsion on J = 0 modes, and the literal frozen-resummation route is shown non-decisive. J >= 1 torsion stays open, so this is bounded and may not meet the M2 standard used in 044-046.
- **M1 weak candidate for F:** the Lichnerowicz reduction and the sign of the coefficient are sub-steps toward "A, B, C and sign/scheme" but do not derive the F target. I do not claim M1.
- **M3:** not triggered in my reading. No merged claim is shown false: 046's lambda range is a sampled range, its M* are one-q values, "not excluded" is narrowed by a stronger result. I flag the Q_2 wording for a ruling.
- **Breakthrough:** no.

## Status-label recommendation

None. Critical-path set A, B, C, D1, E, F, G-derived, N, with B and F OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. No status, priority or completion label is changed.

## Author decision needed

None.

## Remaining open step

For a matrix-derived Einstein coefficient with G_A = G_T in this class, ranked:

1. Torsion corrections on J >= 1 loop modes (relaxes H12; the only route that could cancel x-dependence).
2. Full elimination of the inert and higher-harmonic amplitudes including the tree form; the all-harmonic Schur formula above is the starting point.
3. Second variation of the order s^2 density on the leaf, with a stated envelope, for the off-shell non-Einstein question.
4. S^2-M fibre-flux part with the cross term (needed for the first-term cone shift and on the null cone).
5. Replica: whether the first-term cone part or contacts can equal the negative mixed gap on TT, or which replica the state selects (Problem A).
6. Newtonian limit and trace polarisation (static q has x = -l^2/m^2, so the static coefficient differs from c_T^TT unless W_X^(2) = W_R^(1) = 0; not computed).
7. K itself; emergent-metric identification; Lorentzian status (Problem E).

Closing F or B would need all of this and more; see items 2 and 6 of `sec:ch17-done`.

## Special instructions for the gatekeeper

**Please re-derive:**
- (a) W = 0 and T = [Ebar, Ebar], including my order counting for <dE dE>.
- (b) the closed forms by hand from the fourth moment.
- (c) the Peierls argument for v^K, with the sign convention of the Zeeman term on K.
- (d) the helicity-to-TT limit.
- (e) the replica gap algebra (s5 G).

**Please rule on:**
1. Whether the 046 sentence calling Q_2's quadratic part "the first background-torsion correction of the mixed term" needs an erratum or whether the new paragraph's refinement suffices. It is a true statement of the frozen symbol and incomplete as an order-s^2 statement.
2. Whether "\(c_T^{\mathrm{TT}}\)... one coefficient for every K and every n" is adequately scoped by the closing sentence (frozen leading symbol, cross term dropped, H10-H11).
3. Whether the scale argument should stay in the insert, as it does now, labelled "(a scale argument)".
4. The cone density's match to merged Dirac weights rests on a 4 pi unit inference. If you judge that insufficient, narrow "which matches the Dirac weights stated there" to a statement about the R-term only.

**Do not assert:**
- a value or a sign of G_eff;
- any closure;
- that G_A = G_T holds on TT;
- that frozen resummation is a controlled result at M ~ coth^2 tau;
- that any K with f1 = f2 + f3 exists;
- that the first-term cone shift has a computed size;
- that the cited work claims or denies one coefficient beyond the sections read.
