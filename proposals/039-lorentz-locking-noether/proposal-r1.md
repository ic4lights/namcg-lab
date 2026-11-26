# Proposal 039-lorentz-locking-noether, round 1

## Result

Bounded result, at the 038 hypotheses plus the Chapter 10 Stueckelberg dressing. It is a partial negative for the
r = -4 match and a definite value for the Noether coefficient.

1. **Invariance (target 1).** Among first-order frame densities
   sqrt|G| (a1 T.T + a2 T_{lmn}T^{mln} + a3 V.V + a4 V.W + a5 W.W), W = d ln rho, rho^2 = |det e|, the variation under
   local frame rotations is a total derivative for every coframe only on span{ calT, W.W }, calT = TEGR combination
   (a1,a2,a3,a4) proportional to (1/4, 1/2, -1, 0), a5 free. Verified for d = 3, 4 and both signatures (s1: null space of
   dimension exactly 2, residual against span{calT, W^2} below 1e-14; s5: exact rational necessity at quadratic order,
   a1 = -a3/4, a2 = -a3/2). The class [X] of 038 is **not** invariant. By the exact irreducible-part identity
   X = 2 calT + (3/2) S^2 + 2 V^2, the entire non-invariance of kappa_X rho^2 X on the Theta-class is the axial term
   (3/2) kappa_X rho^2 S^2. It vanishes for all content only at kappa_X = 0 (n_D = 2 in the ledger weights).
   Extending off the Theta-class by the ambiguity V - W (zero on the class) cannot reach the invariant span.
2. **Noether coefficient (target 2).** With the local rotations restored by the Chapter 10 Stueckelberg field
   (Eq. dressed-omega) and Lambda fixed by its own stationarity, about constant Theta-bar and for plane waves of the Poisson
   class: the stationary point has S = 0, keeps calT and W^2 unchanged, and replaces rho^2 X by 2 calT + 2 V^2. This is
   exactly one half of the on-class value on the two delta-rho = 0 modes (s2: ratio 0.5 to 6e-13, random constant
   Theta-bar, random wave vectors, both signatures). Hence the joint flow with a local internal part selects
   **r = -2**, not -4: c_W = c_T^ext = N_tot/6 - 2 kappa_X. The ledger value r = -2 is therefore not a presentation
   accident: it is the value in which the non-invariant remainder is the axial torsion alone. The "match" r = -4
   corresponds to the on-class form with S^2 retained, for which the compensating rotation is not a symmetry.
3. **Residue.** c_A - c_T^ext = 2 kappa_X (fixed-state replica, n_D = 0) and = 2 for antiperiodic Dirac gluing at every
   N_s and n_D (2 kappa_X + n_D = 2). With the vector holonomy contact -alpha_v sigma: 2 - alpha_v sigma = 1 (n<1), 3 (n>1).
   The dressing halves the 038 gap and does not close it. 1/G_A - 1/G_T^ext = Lambda_{UV,v}^2/pi at n_D = 0.
4. **Replica family.** On Theta^12 = 1/f, Theta^34 = 1, S = 0 pointwise, X = 2 |d ln rho|^2 and the rotation
   (Goldstone) equation holds identically (s4): the family already lies on the stationary set, and r = -2 holds there
   without any extremisation. On generic Theta-class two-jets the rotation equation does not hold (s4 control).
5. **Problem D.** The unitary gauge of Theorem locking (Lambda = 1) can be identified with the Theta-built frame only on
   the stationary set. In the induced action the six rotation parameters acquire the quadratic form kappa_X (Hessian,
   s3): positive definite for eta = delta, indefinite (six positive and six negative among twelve real parameters) in the
   Lorentzian cases tested. No label change.

Nothing here derives the Stueckelberg field or any local rotation symmetry from the matrix model. Problems B, A and D stay
open and PROGRAMME-CONDITIONAL.

## Target and status

Re-read in the current tree (working tree dirty with the accepted 038 integration, expected).

- **Problem B** (appH L41-L330; Chapter 17 "Problem B: entanglement equilibrium from the path integral"):
  "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL." Ch. 17: "CRITICAL PATH; OPEN. The fixed-algebra
  first-law identity is established, but not the required stationarity." Original target: fixed-volume stationarity of the
  tensor (non-conformal) block derived from the microscopic action, with G_T = G_A, no pre-existing metric.
- **Problem D** (appH L497-L1277; Ch. 17 "Problem D: local Lorentz invariance from Presentation A"):
  "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: D2 ... D remains OPEN
  and the matrix-derived criterion is unmet." Original target D1: derive local Lorentz gauge symmetry from the matrix
  algebra and condensate.
- **Problem A** (appH L12-L40): "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion:
  PROGRAMME-CONDITIONAL." Only the replica/holonomy side (Missing step) is touched by the residue statement.
- Current critical-path set (Ch. 17, matrix-derived scope): A, B, C, D1, E, F, G-derived, N. No discrepancy found between
  Ch. 17 and Appendix H for B, D, A.
- Classification of this package: PROGRAMME-CONDITIONAL (conditional on the Stueckelberg dressing and tree-level
  stationarity, which Problem D leaves undefended). Dependencies: 038 block (ledger L306-L330), 037 block, torsion-invariant
  paragraph (L2039-L2046), Theorem locking and Assumption local-lorentz (ch10), fixed-state replica and fermionic-content
  paragraphs (L188-L204).

## Source reading

Digest plus targeted reads. Digest regenerated for this run (`dirty-chapters: yes`, expected: the uncommitted 038
integration). Read in full: appH L142-L330 (replica, normalisation, fermionic content, fixed-state replica, 037 and 038
blocks), L497-L875 (Problem D head, Presentation A symmetry paragraphs, locked-block paragraphs), L1841-L2046
(Presentation A Poisson limit, connection sector, torsion invariant), ch10 L1-L260 (Lorentz locking), ch08 L270-L315
(emergent operator), ch17 D/D1/D2 passage (L329-L370) and B passage (L121-L137), proposals/038 review-r1.md (review-r2
verdict ACCEPT per the commit log; not re-read in full), reports/sme-scout-BF-20261024.md B-R1..B-R4. Not a full scan.
No unreadable files.

## Research and reasoning

### 1. What local rotations do to a first-order frame density (target 1, target 4)

Let delta e^A = lambda^A_B(x) e^B, lambda_{AB} antisymmetric. Then G and rho are unchanged. With
ell_{m|ln} := (d_m lambda_{AB}) e^A_l e^B_n the homogeneous part of delta T cancels and
delta T_{lmn} = ell_{m|ln} - ell_{n|lm}, delta V_m = -G^{ls} ell_{s|lm}, delta W = 0. Hence

delta( sqrt|G| L ) = sqrt|G| P^{m|ln} ell_{m|ln},
P^{m|ln} = 2 a1 (T^{lmn} - T^{nml}) + a2 [ (T^{mln} - T^{nlm}) - (T^{mnl} - T^{lnm}) ]
           - a3 (G^{ml} V^n - G^{mn} V^l) - (a4/2)(G^{ml} W^n - G^{mn} W^l).

(s1 checks this against a finite variation of L at random jets: agreement 1e-8 to 1e-9 in d = 3, 4, both signatures.)
Invariance mod total derivative is d_m( sqrt|G| P^{m|ln} e^A_l e^B_n ) = 0 for every e. s1 evaluates this divergence at
random 2-jets for d = 3, 4, Euclidean and Lorentzian, and finds the null space of the (a1..a5) -> divergence map to be
exactly two-dimensional and equal to span{(1/4,1/2,-1,0,0), (0,0,0,0,1)} (residual < 1e-14). That recovers the 038
d = 3 null direction (1/4, 1/2, -1) and extends it to d = 4 and to the enlarged family with W.

Analytic content: sufficiency is structural, because calT = -R - 2 nabla.V is a function of G up to a total derivative and
W^2 is a function of G. Necessity at quadratic order about a constant frame is a finite linear-algebra problem; s5 solves it
in exact rational arithmetic (generic rational wave vector, d = 3, 4, both signatures) with result a1 = -a3/4, a2 = -a3/2,
a4 and a5 free at that order (the V.W term is removed only by the nonlinear s1 test, which shows a4 = 0). The relation to
the literature (TEGR as the unique locally Lorentz invariant member of the new-general-relativity family, Hayashi and
Shirafuji, Phys. Rev. D 19, 3524 (1979); Crossref confirms title, volume and pages) is a consistency remark only: the claim
here was derived independently and the paper's content is not independently re-read.

### 2. The Lorentz-violating class on the Theta-class

With the vector, axial and tensor parts of the torsion (ledger L326), X = (2/3)V^2 + S^2 + q^2 and
calT = -(2/3)V^2 - (1/4)S^2 + (1/2)q^2, so X - 2 calT = 2 V^2 + (3/2) S^2 exactly (q^2 cancels). On the class
V = W (checked at random jets, 1e-16). The invariants are therefore calT and V^2 = W^2, and the non-invariant content of
kappa_X rho^2 X is exactly (3/2) kappa_X rho^2 S^2. This is the pointwise form of the ledger identity
rho^2 X = -2 rho R[g_rho] - rho|d ln rho|^2 + (3/2) rho^2 S^2 + td, which fixes why S^2 is the remainder there.

Extension off the class. Two extensions of X to arbitrary coframes agree on the class if they differ by multiples of
(V - W). In the coefficient basis (T.T, TT', V.V, V.W, W.W) these add (0,0,g1, g2-g1, -g2), and (1,0,0,0,0) + such a vector
is never in span{(1/4,1/2,-1,0,0),(0,0,0,0,1)} because the TT' coefficient of the target is 0 while the invariant span
needs it equal to twice the T.T coefficient. So the non-invariance of [X] is not an artefact of the choice of extension.
Obstruction class (target 3): [X] in (class densities)/(invariants), one-dimensional, represented by (3/2) S^2; its
measure is the rotation equation A_{AB} = d_m( sqrt|G| P_X^{m|ln} e^A_l e^B_n ). s1: |A| = 15.2, 12.7, 30.8, 25.1 on random
frames (X alone) against 1e-15 for calT; s4 control: on generic Theta-class two-jets A[X] ~ 1e-1 to 1e1 while A[calT] ~ 1e-14.

Presentations and the symmetry. Write X = c_N calT + c_W W^2 + t Z with Z a rotation-violating density, Z = alpha T.T +
beta TT' (mod W^2). Solving the T.T and TT' coefficients gives r = -c_N = 4 beta/(2 alpha - beta). Z = TT' gives r = -4
(the match), Z = S^2 (alpha = 1, beta = -2) gives r = -2, Z = q^2 (alpha = beta = 2/3) gives r = 4, Z = X gives r = 0:
these reproduce the 038 values -4, -2, 4, 0. The symmetry fixes the class [X] but not the representative Z, so imposing
invariance alone does not choose r. A choice requires the remainder to vanish on the set where the compensating rotation is
a symmetry, which is the stationary set of the next subsection.

### 3. Dressed density and the stationary set (target 2)

The within-core mechanism is Chapter 10: replace e by Lambda e with the Stueckelberg field of Eq. (dressed-omega). The dressed
density is invariant under (e, Lambda) -> (Lambda' e, Lambda Lambda'^{-1}) and Lambda becomes a field whose equation is the
rotation equation A_{AB}[Lambda e] = 0. Assumption local-lorentz and Theorem locking are used as stated; they are not
derived.

Quadratic order about constant Theta-bar. Take the class perturbation Theta = Theta-bar + eps T, T^{mn} = q^m u^n - q^n u^m,
q = Theta-bar p, so delta omega = p ^ (u.omega-bar) is closed and the first-order frame amplitude is
ehat^A_n = eta^{AB} delta omega_{nB}. The first-order torsion is T-hat = p ^ ehat and the phase-averaged second-order
invariants are quadratic in T-hat (T-bar = 0). The rotation shifts ehat by lambda e-bar. s2 minimises/extremises X over the
twelve real amplitudes of lambda_{AB} at fixed class amplitude, for random constant Theta-bar (non-isotropic), random wave
vectors, Euclidean and Lorentzian eta, delta-rho = 0 modes and a generic polarisation:

- ledger ratios reproduced: S^2 : X = 1/3, calT = X/4 on delta-rho = 0 modes; identity X = 2 calT + (3/2) S^2 + 2 V^2 to 1e-12;
- calT is constant on the orbit (to 1e-12); at the stationary point S = 0 (3e-25) and X_ext = 2 calT + 2 W^2 on all modes
  (7.5e-13), so X_ext / X_class = 1/2 on the delta-rho = 0 modes (6.2e-13);
- Hessian over the rotation amplitudes: positive definite for eta = delta (all 12 eigenvalues positive), six positive and
  six negative for the Lorentzian eta (s3), non-degenerate in all trials.

Analytic reason for S = 0: S_{lmn} is the 3-form e_A ^ d e^A. Its first-order amplitude satisfies p ^ S-hat = 0 (checked 1e-16),
while a rotation shifts it by p ^ Phi with Phi = lambda_{AB} e-bar^A e-bar^B an arbitrary 2-form, whose image is exactly
{3-forms annihilated by p ^} (Koszul exactness for p != 0). So S can be rotated away exactly. The vector part V is not
changed along p (a rotation shifts V only orthogonally to p, while on the class V is parallel to p), so V^2 = W^2 remains.
Thus X_ext = 2 calT + 2 W^2.

Replica family. s4: on Theta^12 = 1/f, Theta^34 = 1 (f = r^{n-1}, n = 0.8, 1.0, 1.2) S^2 = 0 and X = 2 |d ln rho|^2 and
A_{AB}[X] = 1e-16 at a generic point (A[calT], A[W^2] = 0). The family sits on the stationary set with Lambda = 1.

### 4. The Noether coefficient and the residue

On the stationary set the dressed density depends on e only through G and rho, and calT ~ -R up to a total derivative, so
rho^2 X -> -2 R + 2 V.V: the coefficient of R is -2. This is the same number as the tensor coefficient: calT is invariant,
so c_T^ext = N_tot/6 - 2 kappa_X (s2: eigenvalue 1/2 of X) equals c_W(r = -2) = N_tot/6 + kappa_X r. Two independent
routes (the algebraic decomposition and the eigenvalue) agree. This uses the Noether structure of the preceding (038) block:
the coefficient of R in the presentation whose remainder carries no charge. The torsion-trace remainder 2 V.V carries no
charge on a Killing-invariant rho (V normal to the bifurcation surface vanishes there); the axial remainder vanishes on the
stationary set. The full entropy of the rigid compensating rotation (the Iyer-Wald hypothesis of Lie dragging with an
internal symmetry) is not computed.

Residue. c_A is unchanged (X is bounded on the fixed-state cover). Ledger values: c_A - c_T = 4 - n_D (antiperiodic,
= 4 kappa_X + n_D). With c_T^ext = c_T + 2 kappa_X: c_A - c_T^ext = 2 kappa_X + n_D = 2 for every N_s, n_D; at n_D = 0 equal to
2 kappa_X = 2. With the 038 vector contact: 2 - alpha_v sigma = 1 (n<1), 3 (n>1). The E_delta-type uniform contact
(-N_tot/4, not part of the fixed-state class, N_s dependent) would give 3/2 - N_s/4, zero at N_s = 6 only: this is a
content choice of the type already recorded and is not offered as a match. At n_D = 2, N_s = 6 (kappa_X = 0) nothing
changes: c_T = 0, c_A = 2.

### 5. No-go as a fork (author directive 2026-10-15)

The statement "r = -4 is not selected by local rotation symmetry" depends on the following hypotheses; each is listed with
the relaxation and what was explored.

| # | Hypothesis | Relaxation | Outcome / status |
|---|-----------|------------|------------------|
| H1 | Rotation restored by the Stueckelberg field only (6 parameters), the bundle connection of the fluctuation operator is the Poisson composite | independent diagonal connection B with the operator covariant under the diagonal group | explored structurally, not computed: the composite equals the torsion 1-form B_sigma^{AB} = -T_sigma^{AB} (s6: residual 4e-16 at random class jets, both signatures); it is not a connection under local rotations, so the operator is not diagonal-covariant. A covariant operator has no X term; then kappa_X -> 0 at the density level and the gap is the standard contact term. OPEN, ranked 1. |
| H2 | Tree-level stationarity of Lambda | loop average over Lambda; frozen Lambda = 1 | frozen: r undefined (no symmetry), 038 indeterminacy returns; average: not computed. OPEN, rank 3. |
| H3 | Quadratic order, plane waves, constant Theta-bar | non-linear stationary set | S = 0 and A = 0 verified exactly on the cone family only. OPEN, rank 4. |
| H4 | Bosonic-weighted kappa_X from the ledger; Dirac via the same weights | spinor-lift check of the fermion X-term under the same rotations | not computed; the fermion torsion coupling is the spinor lift of B (ledger L189), same structure. OPEN, rank 5. |
| H5 | Fixed-state replica, c_A = N_tot/6 | replica from modular flow, second circulation, edge/mediator contacts | residue 2 (n<1 holonomy gives 1) is a number the contact must supply: modulus 2 versus available 1. OPEN, rank 2. |
| H6 | Euclidean eigenvalue conventions for c | Lorentzian Hessian indefinite | Lorentzian ghost-sign Goldstones if dynamical (s3); not resolved. Relevant to D. |
| H7 | Noether coefficient = coefficient of R (038 definition) | direct Lorentz-Noether charge | consistent with the eigenvalue route; the direct charge of the rigid compensating rotation is not computed. |

Ranked open avenues: (1) covariant bundle connection for the fluctuation operator (H1) and what it does to kappa_X;
(2) the origin of a contact of modulus 2 (holonomy of the dressed bundle connection around Sigma, with the Goldstone
rotation contributing in addition to the cone holonomy); (3) loop-level treatment of Lambda; (4) nonlinear stationary set;
(5) the fermion X-term under the same rotations.

## Claim classification

| Claim | Class |
|-------|-------|
| Rotation-invariant span is span{calT, W^2}; exact necessity at quadratic order; nonlinear null space dimension 2 | established (identity-level algebra, exact rational s5; nonlinear s1 numerical to 1e-14) |
| X - 2 calT = 2V^2 + (3/2)S^2; non-invariant content is (3/2) kappa_X S^2 | established |
| Extension ambiguity V - W cannot reach the invariant span | established |
| r(Z) = 4 beta/(2 alpha - beta) and the values -4, -2, 4, 0 | established |
| Orbit-stationary X_ext = 2 calT + 2 W^2, ratio 1/2, S = 0 (plane waves, constant Theta-bar) | established numerically (1e-12) with an analytic reason for S = 0 |
| Hessian signature (positive definite Euclid; (6,6) Lorentz) | numerical, tested cases only |
| Cone family on the stationary set | numerical (1e-16) |
| Stueckelberg dressing, local rotation symmetry, tree-level stationarity | input / conditional (Assumption local-lorentz) |
| r = -2 and G_T^ext = G_W | conditional on the dressing |
| Residue 2 (all N_s, n_D), halving of the gap | conditional (ledger inputs c_A, c_T) |
| The matrix model supplies the dressing or the replica | unresolved |

## Proposed changes

Single insertion into `chapters/appH-microscopic-proofs.tex`, file `appH_insert.tex` in this folder.

- **Anchor.** Immediately before `\section{Problem C: conformal mode and Cassini}` (the line is unique: grep count 1, line 332).
  It follows the 038 block, whose last sentence is "Problem~B stays open and PROGRAMME-CONDITIONAL." (L330). Nothing in
  the 038 block is replaced.
- **Placement justification.** The block uses the symbols c_A, c_T, kappa_X, r and the fixed-state replica defined in
  the Problem B ledger, and it completes the 038 sentence "until the question of local frame rotations (Problem D) is settled".
  A copy in Problem D would need those definitions repeated. The block states its D bearing in its text. No change to the D
  ledger text.
- **Labels.** `\ref`: only `eq:dressed-omega` (ch10, L136). Verified present, unique. `\LUV` is defined in the preamble
  (used by the 038 block). No `\label` introduced. No new citation, no BibTeX needed.
- **Checks.** Bytes: 5588, 0 TAB, 0 CR, 0 non-ASCII or control characters (LF; the integrator applies CRLF). Scratch compile
  outside the repository with the block inserted at the anchor in CRLF: two pdflatex passes rc = 0, 0 undefined references,
  0 multiply defined labels (the 80 citation warnings are pre-existing because bibtex is not run in the scratch copy;
  `compile_check.out.txt`). Scratch copy deleted.
- **Stale passages.** None. The 038 closing sentence "It stays undetermined until the frame is dragged by a flow whose
  internal part is a local symmetry ..." remains true; the new block bounds it. The 038 statement "the class of X modulo that
  direction is canonical" is consistent.

The block text is the contents of `appH_insert.tex` (not repeated here to avoid divergence).

## Verification scripts

All in this folder; Python 3 with numpy, sympy; each prints and the output is saved as `*.out.txt`.

- `tj.py`: truncated Taylor-jet helper (multivariate, order 2-3) used by s1 and s4.
- `s1_rotation_noether_identity.py`: superpotential P checked against a finite variation (d = 3, 4, both signatures);
  null space of the divergence map on the five-term family at random 2-jets; violation norms of X, calT, W^2.
- `s2_goldstone_extremum.py`: class plane waves about constant Theta-bar, identities, orbit stationary point, ratio 1/2,
  S = 0, X_ext = 2 calT + 2 W^2, p ^ S = 0, Hessian signs; summary line with maximal deviations.
- `s3_goldstone_kinetic_signs.py`: Hessian diagonal entries on boost and rotation pairs and eigenvalue sign counts. The
  Lorentzian boost/rotation sign assignment depends on the wave vector; only the (6,6) count is claimed.
- `s4_cone_family_goldstone_equation.py`: rotation equation on the cone family (zero) and on generic class jets (nonzero).
- `s5_quadratic_orbit_invariance_exact.py`: exact rational solution of the orbit-invariance conditions at quadratic order.
- `s6_composite_connection_is_torsion.py`: the bundle connection B^s_{an} = Theta^{rs} d_r Theta_{an} of the vector operator
  equals minus the frame-component torsion with its form index s (residual 4e-16). Used only in H1; no claim of the block
  relies on it.
- The V = W check on the class is reproduced inside s4 (printed "V.V - W.W", about 1e-17) and via V-amplitude in s2.

## Decisions Taken

- **Mechanism.** Used the Chapter 10 Stueckelberg dressing (the manuscript's own locking route), not an imported
  mechanism. Rejected: importing covariant teleparallel (inertial spin connection) Noether charges from the literature, which
  would introduce an independent connection with its own dynamics and bypass Problem D.
- **Stationarity.** Chose tree-level stationarity of Lambda because the rotation equation is the manuscript's own consequence
  of the dressed density at the same derivative order as the tensor term; loop averaging deferred (H2).
- **Placement.** One block after the 038 block (Problem B), cross-bearing on D stated in the text.
- **Wording of the result.** "selects r = -2; r = -4 is not selected" rather than "excludes the match", to respect the bounded
  hypothesis class (rule: no-go bounded by hypotheses). The residue 2 is reported as a number the contacts must supply.
- **No new bibliography.** Hayashi-Shirafuji is mentioned only in this report as a consistency remark; no manuscript citation.

## Milestone assessment

Routine for the manuscript trigger list: it narrows an indeterminacy to a definite value (-2) and halves the gap but does
not close or derive a critical-path step, and the dressing is an input. I claim no breakthrough. For the gatekeeper's
assessment: the identification of the ledger value r = -2 with the symmetry-adapted representative, and the uniform residue 2
independent of N_s and n_D, are the two statements that change what the next package should aim at (a contact of modulus 2).

## Status-label recommendation

None. B, A and D remain OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL as they stand. No label edit appears in the block.

## Author decision needed

None.

## Remaining open step

For B: a contact (or a modular-flow replica with holonomy) supplying exactly 2 in the units above, or a derivation that the
fluctuation operator is diagonal-covariant (H1), which removes X; the entropy of the rigid compensating rotation; the matrix
origin of the replica. For D: derivation of the Stueckelberg field and local rotation symmetry from the matrix algebra (D1);
the ghost-sign structure of the Lorentzian Goldstone Hessian. For A: the replica/holonomy selection.

## Special instructions for the gatekeeper

- The result is conditional on the Chapter 10 dressing and tree-level stationarity. Do not read "r = -2" as a derivation of
  local Lorentz symmetry or as closure of anything. It does not say G_T != G_A in general.
- Re-run s1, s2, s5 (s4 takes seconds; s3 imports s2). Re-check: the P formula against the finite variation (s1 first line
  of each case), the exact identity X - 2 calT = 2V^2 + (3/2)S^2 from the ledger decomposition, the r(Z) formula, the
  Koszul argument for S = 0, and that V is shifted only orthogonally to p by rotations while V = W is parallel to p.
- Check that the block's sentence "no addition of multiples of V - d ln rho reaches the invariant span" agrees with the
  coefficient argument in section 2.
- Check the residue arithmetic: c_A - c_T = 4 - n_D (ledger L189) and c_T^ext = c_T + 2 kappa_X with kappa_X = 1 - n_D/2.
- The statement that the V^2 remainder carries no charge relies on Killing invariance of rho at the bifurcation surface; it
  is stated in this report, not in the manuscript block.
- The block does not claim the Iyer-Wald hypotheses for the rigid compensating rotation; it lists that as not derived.
