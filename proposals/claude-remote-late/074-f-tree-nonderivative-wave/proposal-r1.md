# Proposal 074-f-tree-nonderivative-wave, round 1

## Result

Target: the tree non-derivative terms of the frame wave in the static scalar channel along y^mu y^nu at q=0. This is avenue 1 of the 062-064 review and item F.t-nonderivative-sector of plan-2026-11-21b. The terms are computed exactly in the conjugate-coordinate class times a fuzzy factor.

1. **Localisation identity (established, exact).** Take a wave A^a = eps(y) w^a, where w is a fixed function on the leaf and eps a compactly supported function of the base functions. The exact tree quadratic form has two terms: the recorded leading symbol, and a single non-derivative term eps^2 <w.L(w)>, with L the Hessian. There is no term of first order in d eps, and the tadpole is zero. The proof uses the symmetry of L under the Liouville pairing and the exact Lie-Poisson identity [f,[L,f]] = 2(Df.Df) - 2Df(Df.).
2. **The recorded channel (established, exact).** The channel along y^mu y^nu has the realisation w = P T. This is the rescaling X_{y0} -> (1+eps) X_{y0} of one matrix component. It gives sigma_1 = -eps and sqrt|g| = m^-4/(1+eps) exactly, which is the parametrisation of the 062-064 identity.
   - L(PT) = 2 P_perp T, so <w.L(w)> = 0 on the whole leaf. The leading symbol is also zero on the base fibre.
   - The result holds to all orders. The quartic term with C=0, the bilinear term and the K terms are of degree 2 or 0 in one component. So S(lambda) = S_perp + lambda^2 S_u, also at finite N, and stationarity forces S_u = 0.
   - Hence **T_tree = C_tree = 0**, and the tree non-derivative terms contribute **exactly 0 to Sum(C_i - T_i)**.
   - The sign is therefore determined: it is zero. The tree terms cannot make the first pole Yukawa in this channel, and cannot cancel the U_4 tadpole there.
3. **The level-one realisation of the same channel (established, exact at the frozen point).** This is the recorded amplitude d_q, with w = yhat (qhat.T). Here <w.L(w)> = (l^2+m^2)/3 and sigma_1 = -(k|y0|/3) eps. Per sigma_1^2 the tree form is (3 rho_M/2g^2)(k^-2 - m^2). In the normalisation of the identity this splits into two pieces:
   - the leading symbol contributes -3 varpi/m^2, with the tachyonic sign;
   - the non-derivative term contributes +3 varpi/(m^4 k^2), which is not a q=0 constant.

   So the tree supplies no positive q=0 constant in the recorded channel by either realisation.
4. **Fork: the static singlet sector (conditional route, positive-aimed).** The channel is not L-invariant.
   - On span{PT, P_perp T}, L has eigenvalue 6 on the dilatation T, which carries sigma_1, and -2 on (P_perp - 3P)T, for which t=0. L = -2 on all 9 traceless symmetric constant kappa.
   - The q=0 singlet form is (l^2+m^2)(6 eps_1^2 + 2 eps_1 eps_y), which is indefinite.
   - At fixed sigma_1 its stationary value over the sigma_1-neutral direction is C_tree = (1/4)(rho_M/g^2)(l^2+m^2). This adds **+vartheta varpi/2m^2 > 0** to the denominator: the Yukawa sign, at tree strength.
   - That would be a heavy static scalar, the safe-mass side of Problem C. It applies only if the static channel at q=0 includes the sigma_1-neutral singlet, and that depends on the uncomputed kinetic matrix of the two singlets and on the matter coupling.

Nothing here closes C, F or N. No status label changes.

## Target and status

- **Problem F** (sec:status-F): Status OPEN; Priority CRITICAL PATH; Completion PROGRAMME-CONDITIONAL. The original target (ch17 "Problem F: the rationals A,B,C") is the weighted a_1 and the curvature-linear a_2 on the locked block, with ghosts, thresholds and scheme, and G_eff derived, not input.
- **Problem C** (sec:status-C): Status OPEN; Priority CRITICAL PATH; Completion PROGRAMME-CONDITIONAL. Its target is the full quadratic scalar operator, the pole mass or m_psi/v, the Cassini coupling, and the discharge of Assumption ass:gap-psi. The Missing step (appH L712) already records that "in the conjugate-coordinate class the q=0 non-derivative sector of the static scalar channel carries a bounded obstruction recorded in Section sec:status-F". It stays accurate and is not edited.
- **Dependencies:** D1 gates F and C (pathfinder plan; ch17 order list L645-665). F gates N. C and F are tied through G_eff (appH L712 item (ii)).
- **Package classification:** PROGRAMME-CONDITIONAL. It is a bounded no-go in the recorded channel plus a conditional route; nothing is DERIVED for the original targets.
- **Critical-path set** (re-derived from ch17 L700-725 and appH): A, B, C, D1, E, F, G-derived, N. All 8 are OPEN. There is no discrepancy between ch17 and appH for C and F.

## Source reading

Digest + targeted reads. `make_digest.py --check` printed DIGEST CURRENT. The digest header says **dirty-chapters: yes** (appH CHANGED), so protocol 3(d) applies and, because this package edits scope lists, so does 3(c). **No full scan was done.** The gatekeeper must do one.

Read in full:
- appH L2614-3122: the whole conjugate-coordinate sequence through the 062-064 paragraph, including the 069 Hessian paragraph L3065-3104;
- appH L548-556 and L700-714: Problem C, including the Missing step;
- appH L1880-1886: the Problem F label;
- ch17 L138-157 (C), L402-412 (F), L645-665 (order) and L700-725 (criterion);
- ch03 L139-158 (eq:Smatrix).

Labels used: ch:vierbein-emergence (1 definition). eq:Smatrix is cited in prose only, not by \ref.

## Research and reasoning

### Conventions

Everything follows appH:
- Poisson limit, leaf CP^{1,2}, T^a = M^{a4}, y^mu = M^{mu5}, m = M^{45}, R = 1;
- the tree action (4g^2)^-1 Int rho_M <F_ab F^ab + 2 mu^2 X_a X^a>, with mu^2 = -3 the bilinear of the class (L2651, not the K mass of L3065ff);
- E_a = -{X^b,{X_b,X_a}} + mu^2 X_a, and L = dE (s2 check (b) reproduces the recorded L of L2653);
- S^(2) = (2g^2)^-1 Int A.L(A);
- identity conventions of L3109-3113: C_i is the sigma_1^2 coefficient of the density, a real wave enters as 1/2 C sigma_hat^2, (L/2m^4)U_4 = -q_b^2, L = 32 pi^2 m^6/A, varpi = 8 pi^2 rho_M m^6/(g^2 A) (L2992).

### (a) Localisation identity

L is symmetric under the Liouville pairing: it is the Hessian of the action, and Poisson brackets integrate by parts. For a multiplication operator eps:

<eps w, L(eps w)> = <w, eps^2 L w> + 1/2 <w, [eps,[L,eps]] w>,

because the symmetric part 1/2<w,[L,eps^2]w> vanishes.

In the Lie-Poisson algebra, exactly (s3 check (iv), random polynomials):

2 f L(fA) - f^2 L(A) - L(f^2 A) = 2(Df.Df)A - 2 Df (Df.A).

This contains no f and no second derivative of f. With D^a eps = s m eta^{a mu} d_mu eps, which is exact for eps(y), the tree form is exactly the displayed formula of the insert. Two consequences follow:
- the "tree non-derivative terms of the wave" are exactly eps^2 <w.Lw>;
- no presentation ambiguity remains.

On the presentation ambiguity: pointwise q=0 canonical densities differ from this by total derivatives, and can even have the other sign. For the dilatation the canonical pointwise value is 6 M.M - 6 T.T = 6 l^2 - 18 m^2 (in units of (rho_M/4g^2) eps^2), against 12 (l^2+m^2) from A.L(A). Relative to l^2+m^2, s3 (iii) gives -17.46 against +12 at the sampled point. The identity removes that ambiguity.

### (b) Constant kappa

The following are exact for both s (s2 (c), (d)):
- L(kappa T) = -2 kappa T + 2 tr(kappa) T for symmetric kappa, and 0 for antisymmetric kappa (Lorentz rotations, gauge);
- L(T) = 6T;
- L(P_u T) = 2 P_perp T.

Orbit identities, numerical at 200 points with residual 6e-13 (s3 (i)):
- T.T = l^2 + m^2;
- y.y(4-dim) = -(l^2+m^2);
- y_mu M^{mu rho} = m T^rho, with T.y = 0;
- M.M = 2 l^2 - 2 m^2.

On the fibre over y0 (y^i = 0), the SO(3) of indices 1..3 fixes y. So the fibre measure is rotation-invariant, T^0 = 0 and <T^i T^j> = (l^2+m^2)/3 delta^{ij}. This is checked by sampling.

### (c) The rescaling realisation of the yy channel

X = (1 + eps P)T with P = P_{y0} constant. Then:
- E' = (1+eps P)E;
- gamma' = m^2[eta + (2 eps + eps^2)P];
- t = 2 m^2 eps, sigma_1 = -eps;
- sqrt|g| = m^-4 (1+eps)^-1 exactly;
- F' = (1+eps P) F (1+eps P)^T, so the torsion is T' = (1+eps P)(1+eps P) Tbar = (1+eps) Tbar on the base fibre.

**All-orders flatness.** Each monomial of the quartic term contains the u-component at most twice, and [X_u,X_u] = 0. The bilinear eta_ab X^a X^b is diagonal in an eta-orthogonal basis containing u. So S = S_perp + lambda^2 S_u.
- dS/dlambda(1) = 2 S_u = 0 by stationarity, so S is constant in lambda.
- On the non-compact leaf this is the statement that the density change (lambda^2 - 1) L_u is a total derivative, because L_u = 1/2 (E.delta X + div) and E = 0.
- s2 (e) checks exactly that the density depends on eps only via (1+eps)^2.
- s1 checks the matrix identity for random matrices, and checks flatness at finite N on fuzzy spheres (j = 1, 5/2, 4) at stationary points, both Euclidean and Lorentzian contractions, with the per-component bilinear fixed by the field equation.
- The K-sector terms of the product class, [X^i,X^j]^2, the K cubic and the K mass, do not contain X_u. The mixed terms [X_u,X^i]^2 are of degree 2.

**Local form.** <w.L(w)> = 2 PT.P_perp T = 0 identically. Since PT = 0 where y is parallel to y0, the leading symbol is also zero on the base fibre.

**Consequence for the identity.** With T_tree = 0 (E = 0) and C_tree = 0, the tree term contributes nothing to Sum(C_i - T_i) or to Sum T_i. A Yukawa first pole in this channel then still needs the uncomputed loop items of L3113. The cancellation of the U_4 tadpole cannot come from the tree.

**Caution.** The loop C_i recorded in L3043-3113 are for the level-one realisation with the background torsion held. On the rescaling the torsion scales by (1+eps), so the loop profiles differ, for example the index density scales by lambda^2. They are not computed. The insert states this so that the realisations are not mixed.

### (d) The level-one realisation (amplitude d_q)

At y^i = 0 with q = k e_3 (q.y = 0):
- s_3 is parallel to yhat: s3 (v) gives <v (q.T)> along e_0. So D = diag(0,0,d_q) has alpha = f(n) yhat with f proportional to qhat.T, that is, w = yhat (qhat.T).
- w.L(w) = -2 w.(kappa_s T) with kappa_s the symmetric part of yhat ⊗ qhat, which is traceless. This gives (qhat.T)^2 on the base fibre, so <w.Lw> = (l^2+m^2)/3 > 0.
- The derivative part of t is t = 2m<w.v> eps = (2/3) m^2 k |y0| eps, using yhat.v = (m/|y0|) q.T (s3 (v)). The algebraic frame change eps{w,y} ∝ yhat qhat + qhat yhat is traceless.
- The leading symbol is m^2 k^2 <w.w> = -m^2 k^2 (l^2+m^2)/3.

Per sigma_1^2 (density convention) the tree form is therefore (3 rho_M/2g^2)(k^-2 - m^2). Times L/2m^4 this is +3 varpi/(m^4 k^2) - 3 varpi/m^2.

Two further statements are proved:
- For any fibre profile f, with alpha = f yhat, the leading symbol satisfies <= -(3/4)(rho_M/g^2) m^2 sigma_hat^2 (phase-averaged), by Cauchy-Schwarz. Equality holds at level one (s3 (v), sympy).
- This is consistent with L2662: masses enter at relative order 1/(qm)^2.

### (e) Singlet sector

Take w = eps_1 T + eps_y P T with a common profile. On the base fibre <w.Lw> = (l^2+m^2)(6 eps_1^2 + 2 eps_1 eps_y), and sigma_1 = -(4 eps_1 + eps_y) (s3 (iii), numerical to 1e-9, plus the sympy elimination). At fixed sigma_1:
- eps_1 = 0 (the recorded channel) gives 0;
- eps_y = 0 (the pure trace) gives 3/8 sigma^2, that is C = (3/16)(rho_M/g^2)(l^2+m^2);
- the stationary point in the sigma-neutral direction (a maximum, curvature -4) is at eps_1 = -sigma/2 and gives sigma^2/2, that is C = (1/4)(rho_M/g^2)(l^2+m^2).

Then (L/2m^4) C = 4 pi^2 rho_M m^2 (l^2+m^2)/(g^2 A) = vartheta varpi/(2 m^2), using vartheta = (l^2+m^2)/m^2 at y^i = 0.

The tree leading symbols at y0 are:
- (2/3) m^2 (l^2+m^2) k^2 for T (static q);
- 0 for PT, because PT vanishes on the base fibre.

The induced and loop kinetic parts, and the source couplings, are not computed. So which combination the static channel selects is open.

### No-go hypotheses and relaxations explored (fork record)

The bounded no-go, T_tree = C_tree = 0 in the channel, depends on four hypotheses:
- (H1) the action is the quartic term with C=0 on M plus bilinears diagonal in an eta-orthogonal basis, so it is degree-2 homogeneous in one component;
- (H2) tree stationarity, E = 0;
- (H3) the channel is restricted to y^mu y^nu, so the spatial rescaling is held;
- (H4) the rescaling realisation.

Relaxations explored here:
- **(H4) -> level-one realisation.** Computed in (d). The result is a positive term, but of order k^-2 and not constant, plus a negative leading symbol. This gives no positive constant.
- **(H3) -> singlet sector.** Computed in (e). It gives a positive Yukawa-sign value at tree strength, conditional on the selection.
- **(H1) -> cubic C on M.** This breaks the homogeneity, since S = S_0 + lambda S_1 + lambda^2 S_2, but a constant C destroys the stationarity of T (L2651). It is not pursued.
- **(H1) -> non-diagonal bilinears.** These are outside the class.

Open avenues, ranked derivation-first:
1. **The kinetic matrix of the static singlet sector (eps_1, eps_y) with source couplings, (S1)/(S2)/beta_K.** The tree parts are computed here. Its output decides whether the q=0 static channel carries the +vartheta varpi/2m^2 Yukawa contribution. A heavy scalar would be the safe-mass outcome named in ch17 C. The induced part needs the induced form evaluated on the rescaling and dilatation realisations.
2. **The one-loop potential along the tree-flat rescaling.** This is the loop profiles on a tree modulus. The torsion scales as (1+eps), so at V=T the index part should scale as sqrt|g| X ∝ lambda, while sqrt|g| itself scales as lambda^-1 (observation, not computed). U_2 and the first term along the exact ray are derivation-grade one-loop items.
3. **The remaining loop items of L3113 in the level-one realisation:** second-order U_2, the first term, and the fibre flux.
4. **Bottom of the list:** other bilinear weights, which by (H1) give the same flatness; and a cubic on M, which conflicts with stationarity.

**Gating.** D1 gates F and C (pathfinder plan; ch17 L645-653). The localisation identity and the one-component flatness hold for any stationary background of the quartic-plus-bilinear type, so they carry over to a D1-derived frame background if one is constructed.

### Literature

No literature claim is made or imported. The IMS-type localisation formula is elementary operator algebra and is derived here; it is not cited.

## Claim classification

| Claim | Class |
|---|---|
| S(lambda) = S_perp + lambda^2 S_u for the quartic term with C=0 plus eta-diagonal bilinears; flat at stationarity, at any N | established identity |
| Poisson density change along the rescaling is a total derivative for all eps | established (exact algebra + E=0) |
| Localisation identity (tree form = eps^2<wLw> + leading symbol) | established (operator identity + Lie-Poisson check) |
| L(kappa T) formulas, L(PT) = 2 P_perp T, eigenvalues 6 and -2 | established (exact, both s) |
| T.T = l^2+m^2, y_mu M^{mu rho} = m T^rho, <T^iT^j> = (T.T/3) delta | established (orbit algebra; numerically checked; moment by SO(3) invariance) |
| T_tree = C_tree = 0 in the rescaling realisation; no tree contribution to Sum(C-T) in the y y channel | conditional on class hypotheses (Poisson limit, bilinear term, product background, frozen base point, parametrisation of L3107) |
| Level-one realisation: (3 rho_M/2g^2)(k^-2 - m^2) per sigma_1^2; -3 varpi/m^2 and +3 varpi/m^4k^2 | conditional (frozen point, inert amplitudes zero, recorded normalisations) |
| Singlet values 0, 3/16, 1/4 (rho_M/g^2)(l^2+m^2); +vartheta varpi/2m^2 | conditional (common profile, frozen point, the identity's L) |
| Which singlet combination is the static channel; sign of the static scalar pole | unresolved |
| Loop profiles on the rescaling (torsion (1+eps) Tbar computed; densities not) | unresolved |

## Proposed changes

All changes are in `chapters/appH-microscopic-proofs.tex`, sec:status-F. The pre-image sha256 is 29ac2a634bb819df7ecb29e138f97ae014656d4c0bb812b86f3573759a872046 and the post-image sha256 is 55c14afca30418c76fdec5467c513bf3ef7004b6e86f8c74b1d15b3a646a8f93.

**E1** (pre L3057, paragraph "response of the scale of K", Vacuum term). Replace the sentence fragment, which occurs once:

`The tree non-derivative terms, the terms that cancel the tadpole of \(U_4\) at \(q=0\), and any term with the same fibre dependence are not computed, and a long-range form needs them or \(\hat U\to0\);`

with:

```latex
The terms that cancel the tadpole of \(U_4\) at \(q=0\) and any term with the same fibre dependence are not computed here, nor are the tree non-derivative terms (paragraphs below), and a long-range form needs them or \(\hat U\to0\);
```

**E2** (pre L3113, paragraph "the tadpole of the static scalar channel at q=0"). Replace, once:

`the part of the first term with the fibre flux, at first and at second order, and the tree non-derivative terms of the wave, which the leading symbol of the tree form drops, none of which is computed.`

with:

```latex
the part of the first term with the fibre flux, at first and at second order, none of which is computed, and the tree non-derivative terms of the wave, which the leading symbol of the tree form drops and which do not supply it in this channel (paragraph on the tree non-derivative terms below).
```

The following sentence ("With them set to zero the pole of this term has the tachyonic sign ...") is kept. It stays true.

**E3** (pre L3121, scope sentence of the same paragraph). Replace, once:

`the term of \(U_2\) proportional to \(W_R\), the tree non-derivative terms, higher loops or the fibre Laplacian`

with:

```latex
the term of \(U_2\) proportional to \(W_R\), higher loops or the fibre Laplacian
```

**E4.** Insert the block `appH_insert.tex` (LF in the folder; converted to CRLF by the script) immediately before the unique line `\section{Problem G: HBEV}`. It goes after the scope sentence of the 062-064 paragraph, which begins "These statements are for the hypotheses of the paragraph on the response of the scale of \(K\), with the operators at" and ends "Problems~C, F and~N remain open and PROGRAMME-CONDITIONAL.", and after its blank line. Full text: see `appH_insert.tex` (6 blocks, 7912 bytes, sha256(LF) 11aba603ba544a7d8f9bcd18a1389ecba95f7fa9ad221f5210b9a6106ef14643). It has one status sentence, at the end: "Problems~C, F and~N remain open and PROGRAMME-CONDITIONAL."

The text kept elsewhere is unchanged:
- L3006 ("the leading symbol for the loop and for the tree form, which drops non-derivative terms and the fibre Laplacian") is a hypothesis statement and stays accurate;
- the C Missing step (L712) stays accurate.

No bibliography entries are added.

## Verification scripts

All run with `python -I` from `proposals/074-f-tree-nonderivative-wave/`.

| Script | Checks | Expected invariant output |
|---|---|---|
| `s1_matrix_flat_direction.py` | (1) S(lambda) polynomial for random Hermitian matrices, eta Lorentzian and Euclidean; (2) fuzzy spheres j = 1, 5/2, 4: EOM residual, flatness, Hessian [[0,4a],[4a,8b]] | coefficients of lam^1, lam^3, lam^4 = 0; `max|S(lam)-S(1)|` < 1e-12; Hessian `[[0,8],[8,8]]` (j=1, Euclidean), det < 0; last line "...det = -16 a^2 < 0: OK" |
| `s2_liepoisson_q0_hessian.py` (about 3 min) | exact polynomial Lie-Poisson algebra so(4,2), s = ±1: (a) E(T)=0 at mu^2=-3; (b) linearised E = recorded L; (c) L(kappa T) for symmetric/antisymmetric kappa; (d) L(P_uT) = 2(1-P_u)T, L(T) = 6T, eigenvalues {6,-2}; (e) density depends on eps only through (1+eps)^2 | every line `True`; "all exact checks passed" |
| `s3_orbit_local_forms.py` | (i) orbit identities at 200 points; (ii) fibre moments; (iii) singlet form coefficients 6, 0, 2, and the sympy elimination (sigma^2/2 stationary, 3 sigma^2/8 pure trace, 0 channel); (iv) [f,[L,f]] identity; (v) yhat.v = (m/|y|) q.T, <(yhat.v)^2> = m^2k^2/3, <v (q.T)> along e_0, the frozen bound -3 m^2 rho sigma^2/(4 g^2) and the contribution -3 varpi/m^2 | residual < 1e-9; "d1^2 6.000000, dy^2 ~0, 2 d1 dy 2.000000"; "value sigma**2/2"; "(iv) ... True"; "= -3 * varpi/m^2"; "all checks passed" |
| `apply_and_build.py [--build]` | pre-hash, unique anchors inside the intended paragraphs, CRLF, labels, no process/label words, post-hash, build on a temp copy outside the repo | pre-hash True; E1/E2/E3 "occurs 1x ... inside intended paragraph True" at lines 3057/3113/3121; post sha256 55c14afc...8f93; with `--build`: pdflatex rc 0 (420 pages), "undefined/multiply-defined warnings: 0", "BUILD CLEAN", "temp copy removed: True" |

The saved outputs are `*_output.txt` in the folder.

## Decisions Taken

- **Which "q=0 wave" to compute.** I computed the tree form exactly for any single-profile wave, via the localisation identity, instead of picking one presentation of pointwise densities. Rejected alternative: pointwise canonical densities at q=0. They are ambiguous up to total derivatives, and their sign can flip (s3 (iii)).
- **Report both realisations of the channel**, the rescaling and the level-one d_q, because the identity's channel admits both and they give different tree forms. Rejected: reporting only the zero, which would hide the k^-2 and leading-symbol structure of the recorded amplitude.
- **Include the singlet-sector fork in the manuscript.** It is the only positive-sign tree route found, and it is directly relevant to Problem C's safe-mass outcome. It is stated as conditional on the selection.
- **Notation.** I use \mathsf P, \mathsf w and eps(y), which do not occur elsewhere in appH. The bilinear coefficient is written as -6 X.X to avoid a clash with the K mass mu of L3065ff.

## Milestone assessment

Routine. This is a bounded no-go in the recorded channel, an exact structural identity, and a conditional route. No critical-path step is derived and no missing link is closed.

## Status-label recommendation

Current critical-path list (ch17 L700-725 and appH): A, B, C, D1, E, F, G-derived, N, all OPEN. Affected labels: none. C, F and N stay OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## Author decision needed

None.

## Remaining open step

- **For the static scalar pole (C/F/N):** the kinetic matrix of the singlets (eps_1, eps_y) at q != 0, which needs the induced and loop forms on these realisations, plus the matter coupling. With them, decide which q=0 combination the static channel is, and the sign of the pole.
- **The one-loop profiles on the tree-flat rescaling,** where the torsion scales by (1+eps).
- **The loop items of L3113.**
- **For the original targets:** G_eff from the locked block for F, and the full scalar operator and m_psi for C. Both remain gated by D1.

## Special instructions for the gatekeeper

- 3(c) and 3(d) apply: E1-E3 edit scope lists, and the digest has dirty-chapters: yes. A full scan is required. I did digest + targeted reads only.
- Re-derive the following:
  - the localisation identity. Check that the symmetric part <w,[L,eps^2]w> vanishes, and that [eps,[L,eps]] has no eps and no second derivative;
  - L(P_uT) = 2 P_perp T;
  - sigma_1 = -eps and sqrt|g| = m^-4/(1+eps) on the rescaling;
  - the level-one numbers: <wLw> = (l^2+m^2)/3, sigma_1 = -(k|y0|/3)eps, the factor (3 rho_M/2g^2)(k^-2 - m^2), and the conversion to ±3 varpi;
  - the singlet values and vartheta varpi/2m^2.
- **Must not be asserted:**
  - that the static scalar pole is Yukawa;
  - that the tree supplies the Yukawa condition in the recorded channel. It does not; it gives 0 there;
  - that the singlet route is selected;
  - any identification of sigma_1, t or the singlets with the emergent metric.
- The flatness at finite N needs the bilinear term to be diagonal in a basis containing u. The class's eta_ab X^a X^b is.
- The torsion statement (1+eps) Tbar is on the base fibre only.
