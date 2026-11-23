# Proposal 076-fc-singlet-kinetic-matrix, round 1

## Result

Target: avenue 2 of the 074 reviews. Compute the kinetic matrix of the two static scalar singlets T and PT, find
the combination that the static channel selects under the recorded matter coupling, and compute the tree
contribution to Sum(C_i - T_i) on that combination. Setting: the conjugate-coordinate class times a fuzzy factor,
the frozen base point y0 with y^i = 0, static q (q.y0 = 0), and the normalisation of the 062-064 identity.

1. **Kinetic matrix (established, exact for the frozen symbol).** L is a second-order operator in the base
   functions:
   - L(fA) = f L A + d_mu f B^mu(A) + d_mu d_nu f R^{mu nu}(A), with R^{mu nu}(A)_a = -m^2(eta^{mu nu} A_a - (delta^mu_a A^nu + delta^nu_a A^mu)/2) and no third-order term.
   - The part that is symmetric under exchange of the two profiles is fixed by the 074 localisation identity.
   - The antisymmetric first-order part has coefficients along y0 at y0, so it vanishes for static q.

   For eps_1(y) T + eps_y(y) PT the static tree form is therefore
   (rho_M/2g^2)(l^2+m^2)[(6 + (2/3) m^2 k^2) eps_1^2 + 2 eps_1 eps_y]. The kinetic matrix is (2/3) m^2 k^2 on eps_1
   and zero in every other entry, because PT vanishes on the fibre over y0.
2. **Matter coupling (established kinematics on top of the recorded coupling).** For X = (1+kappa)T,
   dgamma = m^2(kappa + kappa^T), and the derivative part of the frame change drops out of h_beta^00 at y0.
   Then h_beta^00 = 2m^2[(2 beta_K - 1) eps_1 + (beta_K/2 - 1) eps_y].
   - On the y y channel this is the recorded charge 1 - beta_K/2, and the recorded response is reproduced.
   - The sigma_1-neutral singlet (P_perp - 3P)T has charge **3 for every beta_K**, so under both (S1) and (S2).

   With the tree cross term, this means the y y channel alone does not solve the static equations: the neutral
   singlet is sourced and has to be eliminated.
3. **Selection and the q=0 constant (conditional on H_n).** H_n is the hypothesis that loop and induced terms
   depend on the singlets only through sigma_1, with the y y values of the identity.
   - Eliminating the neutral singlet gives the denominator q^2 + mu + r/(2 - (2/3) m^2 k^2) exactly, with
     r = vartheta varpi/m^2.
   - At q = 0 this adds **+vartheta varpi/2m^2**, the 074 stationary value, for every beta_K. The tree
     contribution to Sum(C - T) on the selected combination is (1/4)(rho_M/g^2)(l^2+m^2).
   - The selected combination is eps_1 = -sigma_1/2, eps_y = sigma_1, plus a source-proportional contact shift.
     Its metric change is isotropic in the rest frame of y0, so the h_beta potential ratio on it is
     (1-beta_K)/(1+beta_K).
   - **Yukawa against the chi exchange** (other entries set to zero) holds iff
     (1/4)(rho_M/g^2)(l^2+m^2) > U'_loop^2/(2 U_chichi). The coefficient A drops out. The condition depends on the
     supplied rho_M/g^2 and on the tree data of K, through U'_loop and U_chichi.
4. **Bounded no-go (established for these forms).** The value r/2 sits at a maximum over the neutral singlet, whose
   own coefficient is -2r. det M(q=0) = -r(2 mu + r).
   - Hence, with the computed tree kinetic term plus the recorded induced q^2 sigma_1^2, or with any
     positive-definite kinetic matrix: whenever the sigma_1 pole is Yukawa (mu + r/2 > 0), the static response
     has **exactly one more pole, at q^2 > 0, with the tachyonic sign**. At mu = 0 the poles are at
     m^2 q^2 = (3/2)(1 ± sqrt(1 + (2/3) vartheta varpi)).
   - For general loop entries 2b sigma_1 eps_1 + nu eps_1^2, with the y y value mu held, the constant after
     elimination is mu - (b-r)^2/(nu-2r). It exceeds mu only if nu < 2r.
   - A static response with no pole at q^2 >= 0 needs the q=0 form to be positive definite. That forces mu > 0
     and a constant <= mu.
   - So under a positive-definite kinetic matrix, the singlet sector moves the tachyonic sign into the neutral
     singlet instead of removing it.
5. **Hypothesis to relax (computed observation).** The Fierz-Pauli form on these metric data is
   4m^4 q^2 (3 eps_1^2 + 2 eps_1 eps_y). It is indefinite and zero on the y y channel, which is the lapse-like
   structure of the GR static sector. An Einstein-Hilbert-type induced kinetic matrix therefore violates the
   no-go's hypothesis. The induced kinetic matrix of the singlets has not been computed.

Nothing here closes C, F or N, and no label changes.

## Target and status
- **Problem F** (sec:status-F): OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. Original target (ch17 L403-412): the
  weighted a_1 and the curvature-linear a_2 on the locked block, with ghosts, thresholds and scheme, and G_eff
  derived rather than input.
- **Problem C** (sec:status-C, L548-713): OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. Original target (ch17
  L139-157; appH Missing step L712): the full quadratic scalar operator, its matter coupling, the pole mass or
  m_psi/v, the Cassini comparison, and the discharge of ass:gap-psi. L712 records "a bounded obstruction" in the
  q=0 non-derivative sector of the static scalar channel. It stays accurate and is not edited.
- **N**: OPEN (dependent on F).
- **Dependencies:** ch17 order L646-665 is D1 -> C -> F -> N. Both the localisation-based kinetic matrix and the
  bound in item 4 are algebraic statements about a stationary background with a positive-definite kinetic
  matrix, so they transfer to a D1-derived frame background once one is constructed.
- **Package classification:** PROGRAMME-CONDITIONAL. Exact partial computations plus a bounded no-go. Nothing is
  DERIVED for the original targets.
- **Critical-path set**, re-derived from ch17 L700-730 and appH ledger labels: A, B, C, D1, E, F, G-derived, N.
  All 8 are OPEN, so **OPEN 8/8**. No discrepancy found between ch17 and appH.

## Source reading
Digest + targeted reads. `make_digest.py --check` printed DIGEST CURRENT. The header shows dirty-chapters: yes,
and this package edits two "not computed" passages, so protocol 3(c)/3(d) applies. **No full scan was done; the
gatekeeper must do it.** The live appH sha256 was re-checked at resume: 8aed4519...e229.

Read in full:
- appH L3002-3163: fibre-point forms; response of the scale of K, including (S1)/(S2)/beta_K, the vacuum term
  and the scalar channel; the 069 Hessian paragraph; the 062-064 tadpole paragraph; the 074 paragraph;
- appH L548-566 and L700-714 (Problem C);
- appH L1905-1926 (F ledger and Missing step);
- ch17 L139-158, L403-414, L640-665, L700-730.

Paragraphs L2936-3001 were read through the digest titles and the 074 record only. Labels used:
ch:vierbein-emergence, defined once.

## Research and reasoning
Notation follows appH and 074:
- T^a = M^{a4}, y^mu = M^{mu5}, m = M^{45};
- L is the Hessian of (4g^2)^{-1} Int rho_M <F^2 - 6X.X>, and the tree density is (rho_M/2g^2)<A.L(A)>;
- the identity normalisation is that density coefficients C of sigma_1^2 enter the denominator as (L/2m^4)C,
  with L = 32 pi^2 m^6/A, varpi = 8 pi^2 rho_M m^6/(g^2 A) and vartheta = (l^2+m^2)/m^2.

**(a) Taylor form and the two-profile tree form.**
- L is a differential operator of order two in multiplication by base functions. The third finite difference
  vanishes exactly (s1 b), so L(fA) = fLA + df B + ddf R.
- BCH with f = q.y and the 074 identity [f,[L,f]] = 2(Df.Df) - 2Df(Df.) give
  -q q R = m^2(q^2 A - q (q.A)). This is checked exactly in s1 (b).
- Write the cross term as Q_12(f,g) = Int rho <f w1 . L(g w2)> and split it into S + A (symmetric and
  antisymmetric under f <-> g). S is determined by its diagonal f = g, which the localisation identity gives
  exactly: N^sym = (<w_i.Lw_j> + <w_j.Lw_i>)/2 plus the polarised leading symbol.
- A = (1/2) Int rho <w1.(f[L,g] - g[L,f]) w2>. Its B-part is (f dg - g df)<w1.B w2>. Its R-part becomes, after
  integration by parts, -(f dg - g df) rho^{-1} d_mu(rho <w1 R^{mu nu} w2>).
- At y0 all <w_i.B^mu w_j> have zero spatial part (s1 c, max 2.5e-17). <T R PT> vanishes at y0. Its divergence
  is along y0: by the covariant moment <T^mu T^nu>(y) = (-(y.y) eta + y y)/3 (checked at boosted base points to
  7e-14), the divergence is (-Y0/2, 0, 0, 0) (s1 d).
- So for static q there is no first-order term. Because PT = 0 on the fibre over y0, the kinetic entries with PT
  vanish, and Z_11 = (2/3) m^2 k^2 (l^2+m^2) (s1 c, from both forms).

**(b) Source.** delta E^{a mu} = eps s m kappa^{a mu} + w^a {eps, y^mu}, with {y^nu, y^mu} = -s M^{nu mu}.
- For w = T the derivative part of h^00 is 2smT^0 X^0, which is 0 on the fibre over y0.
- Its contribution to t is fibre-averaged <T_nu M^{nu rho}> q_rho, which is 0 because only rho = 0 survives (s1 c).
- PT = 0 there, so it contributes no derivative part.
- This gives h_beta^00 = 2m^2[(2bK-1) eps_1 + (bK/2-1) eps_y].
- Charges: 3 on (1-4P)T, 2bK-1 on T, bK/2-1 on PT (s2 item 4).
- Restricting to eps_1 = 0 reproduces the recorded -L rho0^2 (1-bK/2)^2/(q^2+mu) (s2 item 4b).

**(c) Elimination.**
- In (sigma_1, eps_1), the tree form is r[(lam q^2 - 2) eps_1^2 - 2 sigma eps_1] with lam = 2m^2/3. Its Schur
  complement is r/(2 - lam q^2), exact (s2 item 2).
- At q = 0 the selected combination is eps_1 = -sigma/2, eps_y = sigma, with kappa = sigma(P - 1/2). Then
  dgamma^{mu mu} = -m^2 sigma for all mu, which is isotropic, and the h_beta ratio is (1-bK)/(1+bK) (s2 item 3).
- With the source included, z = -sigma/4 - 3J/4r, and Ft_eff = (mu + r/2) sigma^2 + J(1+bK)/2 sigma + 9J^2/8r
  (s2 item 6).
- Chi condition (s2 item 9): (L/2m^4)C + q_*^2|chi = (L/2m^4)(C - U'^2/2U_chichi).

**(d) Bound.**
- M(q^2) = M0 + q^2 K with K positive definite. Then det M is a quadratic in q^2 with det M(0) = -r(2mu + r) < 0
  whenever mu + r/2 > 0, and leading coefficient det K > 0.
- Hence exactly one root has q^2 > 0, and the product of the roots is negative (s2 items 5 and 7; 1620 random
  cases with an extra PSD kinetic term).
- General loop entries: Schur complement = mu - (b - r)^2/(nu - 2r) (s2 item 8, exact).
- If M0 is positive definite, M(q^2) is positive definite for q^2 >= 0, so there is no pole at q^2 >= 0. If M0 is
  indefinite, a root exists. So "no pole at q^2 >= 0" is equivalent to M0 > 0, which implies mu > 0 and Schur <= mu
  (869 random cases, all consistent).
- The minimum principle is the reason: stationarity over a positive-curvature direction can only lower the value.

**(e) Fork record (hypotheses of item 4 and their relaxations).**
- (K+) The kinetic matrix is positive definite.
  - Relaxation: the induced kinetic matrix of the singlets. If it is of EH type, it is indefinite: s2 item 11
    gives the FP form 4m^4 q^2(3eps_1^2 + 2eps_1 eps_y), gauge-checked. Then the bound does not apply, and the
    static sector becomes constraint-like, as in GR.
  - Not computed here. **Ranked 1** (positive-aimed): it decides whether a Yukawa sigma_1 without a tachyonic
    partner is possible, and the induced singlet form is a derivation-grade object that C and F both consume.
- (H_n) Loop terms act through sigma_1 alone.
  - Relaxed in item 8: general b and nu give the same bound. **Ranked 3**: under (K+) they can only lower the
    constant, so the outcome is more of the same no-go.
- (H_y) The y y values mu of the identity.
  - The uncomputed loop items of the 062-064 list (second-order U_2, first term, fibre flux) decide whether
    mu > 0. **Ranked 2** (positive-aimed): mu > 0 is now shown to be necessary for an all-Yukawa static channel.
- (F) The frozen base point.
  - The roots lie in the controlled region only for vartheta varpi >> sinh^4 tau. Non-frozen profiles are
    avenue 1 of 074 (the identity's own profile). **Ranked 4.**

## Claim classification
| Claim | Class |
|---|---|
| Taylor form of L in base functions, the R formula, no third order | established (exact, both s) |
| N = [[6,2],[0,0]] pointwise, symmetrised [[6,1],[1,0]]; Z = diag(2/3 m^2k^2, 0)(l^2+m^2); no first-order static term | established for the frozen symbol at y0 |
| h_beta^00 on singlets; charge 3 on the neutral singlet for every beta_K | established kinematics, conditional on the recorded (S1)/(S2)/beta_K coupling (supplied) |
| Schur r/(2 - lam q^2), +vartheta varpi/2m^2 at q=0, selected combination, isotropy, ratio (1-bK)/(1+bK), charge -(1+bK)/2 | conditional (H_n, frozen point, identity normalisation) |
| Yukawa vs chi iff (rho_M/4g^2)(l^2+m^2) > U'^2/2U_chichi | conditional; depends on supplied rho_M/g^2, tree data of K, other uncomputed entries set to zero |
| Tachyonic partner; constant <= mu without a pole at q^2 >= 0 | established for these forms under (K+) (bounded no-go) |
| FP form on singlet data indefinite | established (standard linearised EH algebra; not the induced form of the class) |
| Induced/loop kinetic matrix, b, nu, mu; sign of the static scalar pole | unresolved |

## Proposed changes
File `chapters/appH-microscopic-proofs.tex`. Pre sha256 8aed4519472ef5ec9b1c8a4668e39b02b0882b5e7edb2cf9a9e0b5ba513ae229;
post sha256 deec6c35b66b2e07a2e1060642a74cc7b1a7997cc8cfd812d7c9a5dbab427a69 (794207 bytes, 3771 lines, CRLF).

**E1** (L3138, the tadpole paragraph, "Profile and stationarity"; the anchor occurs once). Replace
`(on two other realisations of this channel the tree terms supply no positive constant; paragraph on the tree non-derivative terms below)`
with
```latex
(on two other realisations of this channel the tree terms supply no positive constant, and on the singlet sector they supply one only together with a static pole of the tachyonic sign in the neutral singlet; paragraphs on the tree non-derivative terms and on the kinetic matrix of the static scalar singlets below)
```
The following sentence ("With them set to zero ...") is kept.

**E2** (L3159, the 074 paragraph, "The singlet sector at q=0"; the anchor occurs once). Replace
`and the induced and loop parts of that matrix are not computed.` with
```latex
and the induced and loop parts of that matrix are not computed (for its tree part, the recorded coupling and the combination they select see the paragraph on the kinetic matrix of the static scalar singlets below).
```

**E3.** Insert `appH_insert_r1.tex` (LF in the folder, CRLF on insertion; 8220 bytes, sha256(LF)
620aba21...27ba; 6 blocks) immediately before the unique line `\section{Problem G: HBEV}`. It goes after the 074
scope sentence ("These statements are for the Poisson limit on \(M\), tree level, ..." ending "Problems~C, F
and~N remain open and PROGRAMME-CONDITIONAL.") and its blank line. It contains one status sentence, at the end,
matching its neighbours. The full text is in the file.

Kept unchanged: the 074 scope sentence, which correctly describes what that paragraph computes; the 074
Consequence; and C Missing step L712.

No bibliography entries.

## Verification scripts
All run from `proposals/076-fc-singlet-kinetic-matrix/` with `python -I`.
- `s1_singlet_symbol.py` (about 3 min). It imports the head of 074's s2 read-only. Expected output: (a) True,
  True for both s; (b) "R^(mu nu)... exactly: True; third-order Taylor coefficient zero: True"; (c) N = [[6,2],[0,0]],
  Z/(m^2k^2(l^2+m^2)) = [[0.666666667,0],[0,0]] from both forms, "spatial parts of all B^mu_ij: max 2.5e-17",
  <T_mu M^(mu rho)> nonzero only at rho=0; (d) residual ~7e-14, divergence [-Y0/2,0,0,0]; "all checks passed".
  Output file: `s1_singlet_symbol_output.txt`.
- `s2_static_singlet_response.py` (seconds). Items 1-11; expected invariants: Schur -r/(lam*q2 - 2); stationary
  eps_1 = -sigma/2, eps_y = sigma; isotropic dgamma; ratio (1-beta_K)/(beta_K+1); charges 3, 2bK-1, bK/2-1; y y
  reproduction (beta_K-2)^2/(4(mu+q2)); det M = r(lam mu q2 + lam q2^2 - 2mu - 2q2 - r); product of roots
  (-2mu - r)/lam; Ft_eff = 9J^2/(8r) + sigma^2(mu + r/2) + sigma(J beta_K/2 + J/2); 1620 random cases; Schur
  mu - (b-r)^2/(nu-2r); 869 random cases True; FP form 4 eps_1 k^2 m^4 (3eps_1 + 2eps_y), gauge check 0;
  "all checks passed". Output file: `s2_static_singlet_response_output.txt`.
- `apply_and_build_r1.py [--build]`. Expected: pre-hash True; E1 at line 3138 and E2 at line 3159, each 1x and
  inside the intended paragraph; insert at line 3165; post deec6c35...7a69; label ch:vierbein-emergence defined 1;
  one status sentence; with --build, pdflatex rc 0 (426 pages), 0 undefined/multiply-defined, BUILD CLEAN, temp
  copy removed. Output file: `apply_and_build_r1_output.txt`.

## Decisions Taken
- **Which kinetic matrix:** the tree two-derivative form at the frozen base point, as dispatched. The induced
  kinetic matrix was not computed. It is recorded as the hypothesis (K+) and ranked first, together with the FP
  observation that shows why it matters.
- **Parametrisation of loop entries:** the general entries are written around the y y channel (z' = eps_1 at fixed
  sigma_1), so that the identity's y y value mu stays fixed. Rejected alternative: entries on the (1-4P)T
  coordinate with mu fixed, which silently changes the y y value. In an exploratory step that gave a spurious
  positive range up to 3r/8; it is not used.
- **Recording the isotropy / (S2) ratio:** included as one exact sentence, because it is data for Problem C. It is
  explicitly not a long-range statement.
- **Stale lists:** only E1 and E2. The 074 scope sentence still describes that paragraph's own content correctly.

## Milestone assessment
Routine. Item 3 confirms the positive constant on the selected combination, but item 4 shows it comes with a
forced tachyonic partner under (K+). No critical-path step is derived.

## Status-label recommendation
None. A, B, C, D1, E, F, G-derived and N all remain OPEN (8/8); C, F and N stay CRITICAL PATH /
PROGRAMME-CONDITIONAL.

## Author decision needed
None.

## Remaining open step
- The one-loop induced kinetic matrix of the two singlets at V=T with equal weights. It decides (K+), and so
  whether the static scalar channel can be all-Yukawa with mu <= 0.
- The y y-channel loop entries of the 062-064 list, which decide mu.
- The loop entries b and nu on the neutral singlet (the response of U_2 and Y along the dilatation; the p
  hypothesis).
- For the original targets: the C operator and m_psi, and G_eff (F), both gated by D1.

## Special instructions for the gatekeeper
- A full scan is owed (3(c)/(d)).
- Re-derive:
  - the R formula and the absence of a static first-order term, including the R-divergence via the covariant
    moment;
  - h_beta^00 on the singlets and the charge 3;
  - the Schur complement r/(2 - lam q^2);
  - det M(0) = -r(2mu + r) and the one-positive-root argument;
  - mu - (b-r)^2/(nu-2r).
- Must not be asserted:
  - that the static scalar pole is Yukawa;
  - that the singlet sector removes the tachyonic sign;
  - any long-range or Cassini statement from the isotropic combination;
  - any identification with the emergent metric.
- The FP form is the standard linearised EH form. It is not claimed to be the induced form of the class.
