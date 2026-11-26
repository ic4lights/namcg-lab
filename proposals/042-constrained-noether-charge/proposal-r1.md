# Proposal 042-constrained-noether-charge, round 1

## Result

The Noether/Wald charge of the constrained class (G, rho, vartheta all built from one closed omega
with the matrix contraction eta) has been computed on the bifurcation surface. **The first law does
not select r.** This is a bounded indeterminacy theorem (a fork, not a stop). Within its hypotheses
it shows that the residue c_A - c_T = 4 kappa_X (n_D = 0) does not sit in the induced density. It sits
in the edge term of the eta-boost generator: the same kind of superpotential that Chapter 7,
Eq. (Top-FP), absorbs into the area term.

1. **The eta dependence is tensorial (derivation plus exact check).** Write
   gamma_{mu nu} = eta_ab d_mu X^a d_nu X^b, with X^a the matrix coordinates as functions on the leaf.
   - Every local invariant of the Poisson-limit operators is a chart-covariant functional of
     (gamma, omega), with gamma = eta in the matrix chart and Riem(gamma) = 0. The corresponding
     tensors are:
     - e^alpha_mu = gamma^{alpha beta} omega_{mu beta};
     - G = omega gamma^{-1} omega^T;
     - rho = |Pf omega| / sqrt|det gamma|;
     - the torsion of e, taken with the Levi-Civita connection of gamma.
   - gamma is the matrix contraction eta written in another chart. It is not G and adds no field.
   - This resolves the "non-tensorial eta dependence" flag of 041 (review-r1, open item 1).

2. **Joint flow (exact, symbolic).** Take xi to be the rotation (Lorentzian: boost) of the normal
   plane, with omega in the family or in span{e12, e34}.
   - The tensorial Lie derivative of omega vanishes. This is the 038 "joint flow".
   - Then L_xi gamma = 0, and e, G, rho and vartheta are Lie-dragged, with [e, B] = 0 on Sigma.
   - The matrix coordinates are not dragged: L_xi X^a = B^a_b X^b, the rigid eta-rotation.
   - So the Iyer-Wald stationarity hypothesis holds in the variables (gamma, omega) and fails in the
     variables (X, omega) by a global transformation, not a gauge one. This is the precise form of
     the 038 "rigid compensating rotation".

3. **Charges on Sigma (analytic, with exact checks).** In the variables (gamma, omega):
   - Any density of first order in (gamma, omega) has zero charge on Sigma, modulo an exact form.
     This covers rho^2 X, rho^2 calT and rho^2 V^2.
   - The densities sqrt(G) R_G and sqrt(G) R_W have the same charge on Sigma, pointwise, whenever
     [e, B] = 0. Here R_W is the Weitzenboeck curvature scalar built from Riem(gamma).
   - The identity R_G + calT + 2 div V = R_W holds exactly at random jets of a non-flat gamma.
   - Hence for every real r the density L_r = L_0 + r kappa_X sqrt(G) R_W equals L_0 on the whole
     class, not only on the stationary set, and has charge coefficient c_W(r) = N_tot/6 + kappa_X r.
   - L_0, with X the torsion invariant, gives r = 0. This is c_A of the fixed-state replica.

4. **Compensation (exact polynomial identity).** Adding f^{abcd} Riem(gamma)_{abcd}:
   - shifts the eta-stress by the identically conserved improvement E^{bd} = -2 d_a d_c f^{abcd};
   - satisfies d_b Q^{ab} = 2 xi_c E^{ac}, with Q = -2 f d xi - 4 (d f) xi.
   So the shift of the Sigma charge equals the boost charge of the improvement, and the Iyer-Wald
   first law holds for every r. In the variables (X, omega) the same freedom is the ambiguity
   Theta -> Theta + dY. It does not drop out, because L_xi X != 0 (JKM's hypothesis fails).

5. **Consequence for B.**
   - r = -1 and -4 (041), -2 (039) and 0 (replica) are all values of an edge term of the
     eta-boost generator.
   - c_A = c_T (n_D = 0) is equivalent to the statement that the edge term accompanying the
     fixed-state replica is the one of r = -4, that is -4 kappa_X in units of c relative to L_0.
   - That is a property of the modular Hamiltonian of the state at Sigma (Problem A), or of a
     local symmetry that makes the compensating rotation a gauge transformation (Problem D1). It is
     not a property of the induced density.
   - The 041 question "which of G, rho, vartheta are held fixed" has no answer inside the first law.
     None of them is an independent field, and the freedom is the edge term.

6. **Constraint term of the composite connection (SME route B-R3, 037 open item).**
   - A multiplier term for b = F[Theta] depends only on first derivatives of (gamma, omega). It has
     zero charge on Sigma.
   - The two readings in the 037 comparator paragraph are two extensions of the same density, and
     they differ by an f·Riem(gamma) term:
     - "tied to the frame" (charge 2 (dL/dOmega)·B, H = J): Omega taken with Riem(gamma);
     - "not tied" (charge 0): Omega - Riem(gamma).
   - So the log-order comparator choice and the Lambda^2 choice of r are the same edge ambiguity.

The B residue therefore **narrows but stays open**. Nothing closes, no label changes, and this is
not a breakthrough.

## Target and status

- **Problem B** (Appendix H, ledger label, verbatim): "Status: OPEN. Priority: CRITICAL PATH.
  Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity
  condition for the tensor block is not derived."
  - Chapter 17: "CRITICAL PATH; OPEN. The fixed-algebra first-law identity is established, but not
    the required stationarity."
  - Closure (Ch. 17 sec:ch17-done item 2) requires Assumption EE to be derived, for fixed-volume
    variations including the non-conformal tensor block, without Assumption dictionary.
  - Sub-target addressed here: the tensor-versus-area normalisation, c_A versus c_T. The located
    missing ingredient (041) is the Noether/Wald charge of the constrained class and the selection
    of r.
- **Problem D**: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL.
  Reduced-scope result: D2, imposed local Lorentz symmetry, supports only a scope-limited
  Presentation-B model; D remains OPEN and the matrix-derived criterion is unmet."
- **Problem A**: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion:
  PROGRAMME-CONDITIONAL."
- **Dependencies.** The result moves the selection of r to the modular Hamiltonian (A) or to a local
  symmetry (D1).
- **Critical-path set**, re-derived from Ch. 17 sec:ch17-done: A, B, C, D1, E, F, G-derived and N.
  This agrees with the Appendix H ledger lines. No discrepancy found.
- **Classification**: PROGRAMME-CONDITIONAL. Nothing is DERIVED at the level of the original target.

## Source reading

Digest plus targeted reads. `make_digest.py --check` printed DIGEST CURRENT. The digest reports
`dirty-chapters: yes` (the uncommitted 041 integration), so under CLAUDE.md 3(d) I read the affected
passages directly from the working tree. This is not a full scan, and the proposal changes no
definition, assumption, scope statement or status line.

Read in full:
- **Appendix H, Problem A head**: L12-39.
- **Appendix H, Problem B**, all of it up to `\section{Problem C...}` (L41-367):
  - ledger label, missing step, which-first-law, replica insertion and replica cone paragraphs;
  - the normalisation paragraph (L174-179);
  - every block 031-041, including the 038 paragraph with the edited sentence (L306-330), the 039
    paragraph (L332-341) and the new Moser-variables paragraph (L343-366).
- **Appendix H, Problem D head**: L533-570.
- **Chapter 17**:
  - B passage (L120-137);
  - A passage (L377-391);
  - D passage (L328-350);
  - completion criterion (L691-731).
- **Chapter 10**: L26-140 (groups, Assumption local-lorentz, locking, eq. dressed-omega) and L309-330
  (diffeomorphisms).
- **Chapter 6**: L200-260 (eq. first-law, eq. first-law-zero).
- **Chapter 7**: L130-240 (eq. Top-FP, Top-improved, deltaA-G, substitution).
- **Reviews**: 041 review-r1 and review-r2, 038 review-r1, 039 review-r1, and the 041 proposal-r2.
- **SME**: reports/sme-scout-BF-20261024.md, the B section (routes B-R1 to B-R4).

No unreadable files.

## Research and reasoning

### Hypotheses (H)

- **H1.** Four matrix coordinates, the Poisson limit, omega = Theta^{-1} closed, both signatures.
- **H2.** The order LUV^2 density (N_tot/6) rho R[g_rho] + kappa_X rho^2 X, bosonic sectors, n_D = 0.
  The Dirac sector has a frame derivative with an internal spinor index and is not covered (041).
- **H3.** The "first law" is the Iyer-Wald identity for the induced density as a classical local
  covariant functional: Noether charge on Sigma against boost charge on a Cauchy surface C of the
  wedge. Charges and edge terms are local.
- **H4.** Backgrounds invariant under the joint flow and regular on Sigma (the family; constant
  omega in the span).
- **H5.** gamma is not independently dynamical. It is the pull-back of eta, so Riem(gamma) = 0 on
  the class, as in the matrix model.

### Step 1: covariant variables

**Derivation.**
- The Poisson-limit operators are built from {X^a, .} = Theta^{mu nu} d_mu X^a d_nu and from
  eta-contractions of matrix indices. The vector fluctuation carries a matrix index a.
- Their local invariants are diffeomorphism covariant, with the X^a as scalars. They are invariant
  under the global eta-Poincare group of the matrix coordinates, and translations drop out.
- A local diffeomorphism X onto flat space is fixed by gamma = X^* eta up to an eta-isometry. So
  Poincare-invariant functions of the jets of (X, omega) are functions of the jets of (gamma, omega).
- Converting the matrix index to a tangent index with dX gives e^alpha_mu = gamma^{alpha beta}
  omega_{mu beta}. In the matrix chart this is the 038 coframe e^A_mu = eta^{AB} omega_{mu B}.
  It also gives G = omega gamma^{-1} omega^T and rho = |Pf omega| / sqrt|det gamma|.
- The torsion of e uses nabla^gamma:
  T^alpha_{mu nu} = nabla_mu e^alpha_nu - nabla_nu e^alpha_mu.

**Check (s1a).** A random closed omega (constant part plus d of a cubic) was pulled back by a random
cubic chart change, with gamma = phi^* eta non-constant. The quantities X, TT', V^2, calT, div V and
R_G at the image point equal the matrix-chart values. The exact rational difference is 0 for all
six, in both signatures.

### Step 2: joint flow and stationarity

**Check (s2, symbolic, both signatures).**
- L_xi eta = 0.
- For omega constant in span{e01, e23}, and for the family omega_01 = -f(r), omega_23 = -1:
  - the tensorial L_xi omega = 0;
  - L_xi of the (1,1)-tensor e is 0, and L_xi G = 0;
  - the internal-index derivative satisfies L^int_xi e = B e != 0 (the 038 statement);
  - [e, B] = 0 at Sigma.
- For a generic constant omega every one of these fails.
- L_xi X^a = B^a_b X^b, so the matrix coordinates are not invariant.

Script indices 0..3 correspond to manuscript indices 1..4. The plane is (x^1, x^2), and in the
Lorentzian case x^1 is time.

### Step 3: charges on Sigma

(a) **First-order densities.** Let L depend on (gamma, d gamma, omega, d omega).
- Theta = (dL/d d phi) delta phi. With delta phi = L_xi phi, the current J = Theta(L_xi phi) - xi.L
  contains at most first derivatives of xi.
- In the off-shell identity J = dQ + xi^a C_a, the coefficient X^{mu nu alpha}_beta of
  d_alpha xi^beta in Q^{mu nu} must therefore satisfy X^{mu(nu alpha)} = 0. Together with the
  antisymmetry in mu nu, this makes it totally antisymmetric.
- That part equals d(X xi) minus (dX) xi, an exact form plus terms in xi. So the charge on Sigma
  (xi = 0) vanishes modulo an exact form, for regular fields.
- This applies to X = T.T, TT', calT and V^2 (T contains Gamma[gamma] and d omega).
- sqrt(G) div V is a divergence d mu, whose charge is xi.mu, zero on Sigma.
- This agrees with the merged 038 coframe result (Q proportional to xi). The difference here is
  that the variables are now ones in which the background is stationary.

(b) **Curvature densities.** Take L = sqrt(G) l(R), with R the curvature of a torsion-free
connection Gamma.
- Then Theta = 2 P delta Gamma, with P = dL/dR^a_{b mu nu}.
- L_xi Gamma = nabla nabla xi + R xi, which gives Q = 2 P_a^{b mu nu} nabla_b xi^a, plus terms in
  xi.
- On Sigma, nabla xi = d xi = B for every connection.

For R_G: P.B = sqrt(G) antisym(B G^{-1}).

For R_W:
- R_W = G^{s nu} (e^{-1})^mu_a R[gamma]^a_{b mu nu} e^b_s.
- P.B = sqrt(G) antisym(e^{-1} B e G^{-1}).
- If [e, B] = 0 (stationarity, s2), the two are identical.

**s3** checks this numerically: the difference is 1e-16 with [e,B] = 0, and O(1) to O(100)
otherwise. The identity itself is analytic.

(c) **The identity.**
- R_G + calT + 2 div V = R_W. This is the decomposition of the curvature of the metric-compatible
  Weitzenboeck connection Gamma_W = e^{-1} nabla^gamma e, whose curvature is
  e^{-1} Riem(gamma) e.
- **s1b**: exact difference 0 at three random non-flat gamma per signature, with R_W != 0.
- At flat gamma it is the merged identity R = -calT - 2 div V, which s1a also re-confirms.

(d) **Conclusion.**
- L_0 = (N_tot/6) rho R[g_rho] + kappa_X rho^2 X has charge coefficient N_tot/6. The charge of
  rho R[g_rho] equals that of sqrt(G) R_G: with sqrt g_rho = rho^{-2} sqrt G and g_rho^{-1} = rho
  G^{-1}, P.B is the same.
- L_r := L_0 + r kappa_X sqrt(G) R_W equals L_0 identically on the class, since R_W = 0 at flat
  gamma. Its charge is c_W(r) = N_tot/6 + kappa_X r.
- Equivalently, L_r = L_0 + r kappa_X sqrt(G)(R_G + calT + 2 div V), which is the presentation r of
  the 038 paragraph, now with an exact meaning off the class.

### Step 4: compensation (why every r gives a valid first law)

(i) **Improvement.** Varying f^{abcd} R_{abcd}[gamma] at flat gamma gives
E^{bd} = -2 d_a d_c f^{abcd}.
- This is identically conserved, by the Bianchi symmetry and commuting derivatives.
- **s4(i)**: exact for random polynomial f with curvature-tensor symmetries (first Bianchi checked),
  both signatures.

(ii) **Boost charge.** For a Killing xi of flat eta:
- d_b Q^{ab} = 2 xi_c E^{ac}, with Q^{ab} = -2 f^{abcd} d_c xi_d - 4 (d_d f^{abcd}) xi_c.
- **s4(ii)**: exact polynomial identity, both signatures. The coefficients (-2, -4, 2) were also
  obtained as the unique solution of the matching problem.
- On Sigma, Q^{ab} = -2 f^{abcd} d_c xi_d, nonzero for the sampled f. This is the Iyer-Wald charge
  of f Riem.
- By Stokes on C, the improvement's boost charge equals its Sigma charge, so the Iyer-Wald identity
  (charge on Sigma = boost charge of the eta-stress, plus boundary at infinity) holds for every r.

(iii) **The same freedom in embedding variables.**
- In the variables (X, omega), Theta is ambiguous by dY(phi, delta phi). This changes Q by
  Y(phi, L_xi phi).
- JKM (and the merged 038 text) use L_xi phi = 0 to drop it. Here L_xi X = B X != 0.
- For example, Y^{mu nu} = eps^{mu nu rho sigma} Z_{rho sigma}^{alpha beta}(phi)
  eta_ab d_[alpha X^a d_beta] delta X^b is local and covariant. At delta X = B X it reduces on
  Sigma to Z contracted with the binormal, which gives any edge density, including r times the
  G-area.

### Step 5: what this means for B, and how it connects to Chapter 7

**Chapter 7 already records the structure.** It says that the canonical and metric stress differ by
a superpotential, and that "On a diamond the superpotential contributes only at the edge B. That edge
contribution is absorbed into the area term of the first law."

The present result identifies, for the class, which superpotentials are available:
- exactly the r-family, together with other local edge densities;
- the density does not fix it.

**Numbers** (n_D = 0, units of c, where S = (Lambda^2 A_G / 8 pi) c):
- c_A = N_tot/6 = c_W(0);
- c_T = N_tot/6 - 4 kappa_X = c_W(-4).

So c_A = c_T is equivalent to "the area coefficient that accompanies the fixed-state replica contains
the edge term of r = -4", that is -4 kappa_X (-4 at n_D = 0).

This does not derive that the edge term has this value. It states where the value must come from:
- the modular Hamiltonian of the one-loop state at Sigma, with its edge term (Problem A); or
- a local symmetry that makes the compensating rotation gauge. Then JKM uniqueness applies to the
  combined gauge flow and fixes r (Problem D1). The 039 stipulated dressing gave r = -2 there.

### Step 6: constraint-term charge (B-R3) and the comparator readings

Take a composite b = F(gamma, omega, d gamma, d omega) and a density L_0(b, nabla^gamma b, gamma).
- Theta_comp = (dL_0/d d b) delta b + E_b (dF/d d phi) delta phi.
- With delta = L_xi, b is a tensor, so L_xi b has only first derivatives of xi, and so does L_xi phi.
- The constraint (multiplier, lambda = E_b) term and the L_0 term therefore both have no charge on
  Sigma.

If instead L_0 depends on Omega = Riem(Gamma[gamma] - V/2 + b) = Riem(gamma) + (D b + b b):
- the Riem(gamma) dependence gives the charge 2 (dL/dOmega)·B (the H = J reading of 037);
- the Omega - Riem(gamma) form gives zero (the "not tied" reading);
- on the class the two are the same density.

So the 037 alternatives E(1,1) versus 0 are the same f·Riem(gamma) edge freedom. The literature gap
noted by the SME (no paper treats the multiplier charge of a composite connection) is answered here
for this class: the multiplier carries no charge on Sigma.

### Fork: hypotheses, relaxations, what was explored

| Hypothesis | Relaxation | Explored here? | Outcome |
|---|---|---|---|
| H3 classical local Noether charge | the quantum modular Hamiltonian of the one-loop state (fluctuation fields with their rigid target-index rotation) | no, too large | open avenue 1; decides which edge term accompanies the replica |
| rigid compensating rotation (L_xi X = BX, global) | a local (gauge) compensating rotation, i.e. D1 | argued | if derived, JKM uniqueness fixes r; 039's stipulated dressing gave r = -2; open avenue 2 |
| H5 gamma flat / not dynamical | gamma dynamical with its own field equation | **excluded** | it would make the pulled-back eta an independent geometry, against the emergence directive and the core |
| H1 four coordinates | more than four matrix coordinates (curved induced gamma, extrinsic curvature K) | argued | does not remove the freedom: Riem(gamma) = K K identically on embeddings, so f(Riem - KK) is a new extension ambiguity, and Y(phi, L_xi X) persists; not computed |
| H3 local edge terms | nonlocal or edge-mode contributions (Donnelly-Wall type) | no | open avenue 4 |
| H4 regular stationary backgrounds | singular-rho smooth replica (Lewkowycz-Maldacena) | no | open avenue 5 |
| the choice of T^op in Ch. 7 | define T^op as the response to a specified background (G-bar) on the delta rho = 0 modes and compute its superpotential | no | open avenue 3; this fixes the edge term by definition and tests whether it is -4 kappa_X |
| B-R3 constraint term | composite versus auxiliary connection | **done** | zero charge on Sigma; comparator readings unified |

### Literature checked versus not verified

- **Iyer-Wald 1994** (PRD 50, 846) and **Jacobson-Kang-Myers 1994** (PRD 49, 6587) are already in
  bib/namcg.bib (L585, L597). They were verified against Crossref and abstracts by the 038 gatekeeper
  (038 review-r1).
- The specific statements used are:
  - the Noether charge construction, with the stationarity and regularity hypotheses;
  - the Y-ambiguity drops out for stationary fields.
  Both are the statements already attributed to these papers in the merged 038 paragraph. I did not
  re-fetch the papers this round.
- Not cited, not verified:
  - Prabhu 1511.00388;
  - Wald's lemma on identically closed forms;
  - the standard Q-formula for f·Riem with my normalisation. I re-derived the latter (s4) rather
    than citing it.
- No new BibTeX.

## Claim classification

| # | Claim | Class |
|---|---|---|
| 1 | Local invariants of the Poisson-limit operators are covariant functionals of (gamma, omega), gamma = X^* eta | established derivation (invariant theory plus construction); exact check at one jet per signature (s1a) |
| 2 | Tensorial L_xi omega = 0 for the family and the span; L_xi X = B X; [e,B] = 0 on Sigma | established (symbolic, s2) |
| 3 | First-order densities in (gamma, omega) have zero charge on Sigma mod exact | established derivation (standard structure; regularity assumed) |
| 4 | Charges of sqrt(G) R_G and sqrt(G) R_W coincide on Sigma iff [e,B] = 0 | established (analytic; numeric s3) |
| 5 | R_G + calT + 2 div V = R_W off flat gamma | established identity (Weitzenboeck decomposition), exact at sampled jets (s1b) |
| 6 | L_r = L_0 on the class with charge c_W(r), any real r | established, given 3-5 |
| 7 | Improvement E = -2 dd f and d_b Q^{ab} = 2 xi_c E^{ac} | established (exact polynomial identity at sampled f, s4; analytic) |
| 8 | The first law (Iyer-Wald identity for the class density) holds for every r; it does not select r | conditional on H1-H5 (bounded indeterminacy) |
| 9 | c_A = c_T is equivalent to an edge term -4 kappa_X of the boost generator accompanying the replica | conditional reformulation (n_D = 0, H1-H5); not a derivation of the edge term |
| 10 | The selection belongs to the modular Hamiltonian (A) or to a local compensating symmetry (D1) | conjecture/mechanism (the D1 statement is argued from JKM, not computed) |
| 11 | The multiplier term of b = F[Theta] has zero charge on Sigma; the 037 readings differ by f·Riem(gamma) | established derivation (H1, regular stationary fields) |
| 12 | More than four coordinates does not remove the freedom | conjecture (argued, not computed) |

## Proposed changes

**File:** `chapters/appH-microscopic-proofs.tex`. **Insert only.** No existing sentence is replaced.

**Anchor:** insert the content of `appH_insert.tex` (one paragraph, five `\emph` sub-items and a
closing scope paragraph) immediately before the unique line
`\section{Problem C: conformal mode and Cassini}`, with one blank line before that line. The insert
therefore follows the 041 "Moser variables" paragraph.
- The anchor occurs exactly once in the current working tree; verified with Python after CRLF
  normalisation.
- The paragraph title "Covariant variables, the joint flow" occurs 0 times in the file.

**Mechanics of appH_insert.tex:**
- 7854 bytes, UTF-8, LF, ASCII only (0 non-ASCII, 0 CR, 0 TAB);
- braces net 0, `\(`/`\)` net 0, one `\[ \]` pair;
- no `\label`;
- references: `\eqref{eq:Top-FP}` (label at chapters/ch07-massless-tensor.tex:149, unique), and
  `\cite{IyerWald1994}` and `\cite{JacobsonKangMyers1994}` (bib L585, L597);
- `\LUV` is defined in the preamble (used by the merged blocks);
- one closing status sentence.

Cross-references in the text resolve to existing paragraphs:
- "paragraph on Moser variables" (041);
- "paragraph on the order \(\Lambda^2\)" (038);
- "paragraph on local frame rotations" (039, title "Order LUV^2: local frame rotations, ...");
- "paragraph on the comparator" (037, "Comparator for the entropy of the bundle curvature ...").

Full text: see `appH_insert.tex` in this folder. It is the exact text proposed for integration;
integrate verbatim and convert to CRLF.

**PRIOR-CLAIM-ERROR: none.** No merged sentence becomes false.
- 038: "In the coframe variables it stays undetermined until the frame is dragged by a flow whose
  internal part is a local symmetry ..." remains true. A local symmetry would restore JKM uniqueness.
  The present result adds that covariant variables alone do not.
- 041: "the choice between them is the choice of which of G, rho, vartheta are held fixed under the
  variation of the first law" is an interpretation that the new paragraph sharpens ("none is
  independent; the freedom is an edge term"). It is not false, so no edit is proposed. The
  gatekeeper may prefer a clarifying edit there; I do not request one.
- 031 normalisation paragraph, "contributes no entropy": consistent. It is the r = 0 extension,
  which is also how the merged 038 sentence reads it.

## Verification scripts

All are in `proposals/042-constrained-noether-charge/` and were re-run for this round. Outputs are
saved next to each script.

- `jetlib.py`: exact truncated second-order jets in four variables (sympy Poly over QQ). Provides
  the series inverse, Christoffels, Riemann at a point, and the covariant torsion package (X, TT',
  V^2, calT, div V, R_G, R_W).
- `s1_covariant_eta.py` → `s1_covariant_eta.out.txt` (about 2 min):
  - (a) matrix chart versus random polynomial chart with gamma = phi^* eta: six invariants, exact
    difference 0, both signatures;
  - (b) R_G + calT + 2 div V - R_W = 0 exactly at 3 non-flat gamma per signature, R_W != 0.
- `s2_stationarity.py` → `s2_stationarity.out.txt`: symbolic Lie derivatives as listed in Step 2,
  both signatures.
- `s3_sigma_charge_RW_RG.py` → `s3_sigma_charge_RW_RG.out.txt`: pointwise equality of the Sigma
  charge densities when [e,B] = 0 (difference about 1e-16), and inequality otherwise.
- `s4_improvement_edge.py` → `s4_improvement_edge.out.txt`: the Euler-Lagrange derivative of
  f·R^(1) is -2 dd f; d_b Q^{ab} = 2 xi_c E^{ac}; Q on Sigma is the Wald form. Exact, both
  signatures.
- `compile_check.py` → `compile_check.out.txt`:
  - builds a copy of the **current working tree** (including the uncommitted 041 integration) in
    the session scratchpad outside the repository, with and without the insert;
  - runs pdflatex, bibtex, pdflatex, pdflatex; all exit codes are 0;
  - baseline 313 pages, with insert 315 pages; 0 undefined refs, 0 undefined citations, 0 multiply
    defined labels;
  - the scratch copy was deleted.

## Decisions Taken

1. **Variables.** I treated the eta dependence by covariantising (gamma = X^* eta). I rejected
   "eta as a fixed background tensor", because that makes the flow non-stationary and hides the
   structure. I also rejected promoting gamma to an independent dynamical field, because that is a
   core change and an emergence violation. Covariantising favours the full-GR route: G is the only
   metric, and gamma is the matrix contraction in another chart.
2. **Target of the charge.** I computed the honest charge of the class density with its full
   off-flat freedom rather than choosing one of r = -1 or -4. Choosing one would be a selection by
   fiat, which the 038 and 041 reviews already flagged.
3. **Recording the result.** I recorded it as a conditional paragraph with a bounded
   indeterminacy, and made no label change. The "consequence" sentence is phrased as an equivalence,
   not as a derivation.
4. **Dirac sector.** Left out of scope (n_D = 0), as in 041. The internal spinor index is not
   covered by the covariantisation.
5. **Stationary-set and Hessian identities (041).** No analytic proof is attempted. It is not needed:
   the conclusion holds for every r by an identity valid on the whole class, so it does not depend
   on the numerical stationary-set relation that links r = -1 and r = -4. Recorded as remaining work.

## Milestone assessment

Routine, consequential narrowing. No MILESTONE trigger:
- No critical-path step is derived.
- The B residue is relocated precisely, to the edge term of the eta-boost generator, that is to the
  modular Hamiltonian (A) or to a local compensating symmetry (D1).
- The 037 constraint-term item is closed as zero on Sigma.

## Status-label recommendation

The critical-path set from Ch. 17 sec:ch17-done is A, B, C, D1, E, F, G-derived and N. Affected
labels: none. B, A and D stay OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL.

## Author decision needed

None.

## Remaining open step

To close the 4 kappa_X part of the B normalisation gap at this order, one of the following is needed
(ranked by expected yield for the infrared / full-GR derivation):

1. **Modular Hamiltonian edge term (A ∩ B).** Compute the boost generator of the one-loop
   fluctuation fields in a joint-flow-stationary background, including its edge term at Sigma:
   - the fields are the scalars, a^a (including the rigid rotation of its matrix index) and the
     ghosts, in the canonical form fixed by the fluctuation action;
   - compute it at order LUV^2;
   - test whether the edge term is -4 kappa_X relative to L_0, that is whether the replica's
     modular Hamiltonian carries the r = -4 superpotential.
2. **D1.** Derive whether the compensating rotation can be a local symmetry of the class. JKM
   uniqueness then fixes r. The 039 stipulated dressing gives r = -2, which leaves 2 kappa_X.
3. **Ch. 7 T^op.** Fix T^op as the response to a specified background on the delta rho = 0 modes
   and compute its superpotential edge term. Compare with -4 kappa_X.
4. **Edge modes and nonlocal edge terms** of the connection sector (symplectic gauge group).
5. **Lewkowycz-Maldacena dynamical replica** for the singular-rho smooth family.
6. **Remaining 041 items**:
   - analytic proofs of the 041 Hessian and stationary-set identities;
   - the Dirac sector;
   - more than four coordinates (computation of the f(Riem - KK) and Y freedom);
   - the J-proportional part.

## Special instructions for the gatekeeper

- **Do not assert** that B, or the c_A versus c_T gap, is closed or reduced in value. The result is
  an indeterminacy plus an equivalence. No value of the edge term is derived.
- **Re-check the load-bearing analytic step** (Step 3a). In variables in which ALL fields are
  stationary, a first-order density has no charge on Sigma.
  - The covariance of the torsion with nabla^gamma (s1a) and the stationarity of (gamma, omega)
    (s2) are what make the merged 038 "Q proportional to xi" statement apply with stationarity.
  - Also check that rho^2 X is first order in (gamma, omega). T uses Gamma[gamma], which is first
    order in gamma.
- **Re-check s3's analytic content.** The charge on Sigma of a curvature density is
  2 P_a^{b mu nu} B^a_b for any torsion-free connection, because xi = 0 there. For R_W the relevant
  connection is that of gamma.
- **Re-check the sign and normalisation in s4.** The script solves for the coefficients. The
  identity d_b Q^{ab} = 2 xi_c E^{ac} fixes Q = -2 f d xi - 4 (df) xi with E = -2 dd f.
- **Emergence.** gamma = X^* eta is the matrix contraction in another chart. It is never made
  dynamical or identified with spacetime. Option H5-relaxation ("dynamical gamma") is excluded, not
  listed as an option.
- **Insert indices.** The Lorentzian sentence uses x^1 as time for the boost of the (x^1, x^2)
  plane, consistent with s2 (script index 0 = manuscript x^1).
- **Integration.** Integrate `appH_insert.tex` verbatim with CRLF, then run
  `python scripts/build_check.py`.
