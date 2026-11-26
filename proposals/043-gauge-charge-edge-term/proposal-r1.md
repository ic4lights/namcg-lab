# Proposal 043-gauge-charge-edge-term, round 1

## Result

Strategy-assessment candidates 1 and 3 were run as one package, as the SME scout recommended. Both are negative within
their hypothesis classes, and both are bounded. Together they move the whole B residue onto the state (Problem A) and
onto the class question. Neither a symmetry of the density nor the stress fixes it.

1. **(i) Gauge-covariant charge: the edge term is not selected.**
   - **The realisation is general but tautological.**
     - For every background invariant under the joint flow (on a star-shaped domain, both signatures), the 1-form
       iota_xi omega is closed. Hence iota_xi omega = d eps, with eps = 0 and d eps = 0 on Sigma and
       Hess eps|_Sigma = B^T omega != 0.
     - Then {eps, f} = xi.d f for every function f, and in the matrix chart {eps, X^a} = B^a_b X^b.
     - This is the Poincare lemma together with the fact that Poisson-limit gauge transformations act on the X^a as
       omega-preserving diffeomorphisms. It adds no symmetry, and it is an isotropy of the background, not a local
       rotation of the matrix index.
     - For constant omega it is the Poisson limit of the metaplectic quadratic generator already merged in
       Problem D (the constant-stabiliser paragraph, L676-705).
   - **Gauge-covariant (momentum-map / Lie-Lorentz) charge.** Take the matrix (Moser) variables (X^a on the leaf,
     omega fixed).
     - Here delta_eps = L_zeta with zeta = xi. So the gauge charge equals the diffeomorphism charge of xi, and the
       combined transformation (xi, -eps) leaves every field invariant; its charge vanishes identically.
     - The gauge charge alone is nonzero on Sigma for curvature densities, although eps = d eps = 0 there, because it
       depends on Hess eps. The SME expectation ("the momentum-map term vanishes on Sigma") therefore fails in this
       reading.
     - It holds in the other reading: in the gauge-invariant chart variables Theta(x), with a potential A, the
       compensating parameter iota_xi A + eps - epsbar vanishes on Sigma.
     - In both readings the 042 term Y(phi, L_xi X) = Y(phi, delta_eps X) is untouched, so r is not selected.

2. **(ii) The superpotential of T^op and the edge term: no edge term from the stress.**
   - **Exact classification (sympy, both signatures).** On flat space:
     - the identically conserved symmetric two-derivative tensors linear in h span {G1[h], (dd - eta box) tr h};
     - every single-divergence superpotential with symmetric divergence lands in that span;
     - each element is a double divergence dd U of a curvature-symmetric U (Abbott-Deser form for G1).
   - **Wedge and diamond.** On a Killing wedge its boost charge is the pure edge term d xi . U on Sigma. On a diamond,
     with its conformal Killing field, a bulk (dd xi) U term remains.
   - **Consequence for Eq. (Top-FP).** On traceless T, the superpotential of Eq. (Top-FP) is lambda E[T]. "Absorbing
     its edge term into the area term" therefore changes the coefficient of E. It is not an independent term.
   - **T^op on the delta rho = 0 modes.** Define T^op as the response of the induced quadratic action to G on these
     modes. Then the Euler operator fixes its coefficient at c_T = c_W(-4): the edge term carried by T^op is that of
     r = -4 by construction.
   - **What the first law then needs.** With the fixed-state replica area coefficient c_A = c_W(0), the requirement
     G_A = G_T needs -4 kappa_X from the modular Hamiltonian of the state. **The stress supplies no part of it.**
   - **Answer to "for which r does the first law close with no extra edge term".** For none of the merged replicas.
     The T^op side is r = -4. The replica side is:
     - r = 0 for the fixed-state replica;
     - r = -1 if the state carries the Maxwell edge sector (below);
     - r = -2 only with the stipulated 039 dressing.

3. **Chen-type consistency (verified in Chen 2202.00680, pp. 1-5, 26-31, 63-80).**
   - **What Chen shows.**
     - The thermal modular Hamiltonian is the integrated matter Noether current, plus a term at the outer boundary
       ((3.35), (3.59)).
     - Relative to the stress integral it differs on sigma by the matter Noether charge, with Y = Z = 0 chosen
       (footnote 40), and by an anomalous measure term (App. E, (E.62)-(E.65)).
   - **Applied to NAMCG.**
     - The tree-level fluctuation Lagrangians of the Poisson-limit class depend on the background only through
       (gamma, omega) and first derivatives. So their Noether charge on Sigma vanishes for regular fluctuations
       (042 first-order lemma): the Chen edge term is 0.
     - Chen's measure term is defined via a deformation localised near sigma that multiplies the opening angle by n
       (footnote 92, (E.26)-(E.27)). In the class, about constant Theta-bar with Theta the only field, a localised
       first-order perturbation changes no opening angle. This is the merged statement that the integral of R_G^(1)
       over the normal plane is -2 times the flux of grad ln rho. So Chen's construction is not available in the
       class.
   - **The Maxwell edge sector (new link between merged 036 and 041 statements).** In Moser variables:
     - the linearised gauge transformation acts as delta A = -d lambda on A = a.omega (exact);
     - the operator is Hodge-type with a Ricci coupling.
     So the U(1) structure and Ricci coupling that 036 said O_v lacks in the (G, rho, d Theta) variables are present.
     If the state carries that edge sector (Donnelly-Wall, Kabat value -1), then c_A - 1 = c_W(-1). The remaining
     3 kappa_X is the part that the 041 stationary-set identity assigns to the gradient of the axion vartheta. That
     is a first-order invariant with no Noether charge and no edge-mode term.

**The residue therefore localises as follows (n_D = 0, units of c):**

| Part | Size | What it is | Status |
|---|---|---|---|
| Kabat / Maxwell edge part | kappa_X | Edge modes of the linearised symplectic U(1) in Moser variables | A published mechanism exists. Whether the matrix state carries it is open (A) |
| Axion-gradient part | 3 kappa_X | Non-edge in every local reading examined; tied to vartheta being slaved to G in the four-coordinate class | Open; points to the class question (F, candidate 2) |

Nothing closes, no label changes, and this is not a breakthrough. These are two bounded no-gos with a sharper location
of the missing ingredient.

**Side finding (pre-existing, not caused by this package).** Ch. 7 Eq. (xi-RNC) has the wrong sign on its spatial
term. The vector written there is not conformal Killing; Jacobson's diamond field has -2t x^i d_i (exact check in s2).
See the special instructions.

## Target and status

The verbatim ledger labels read in this session:

- **Problem B (Appendix H, L44-47):** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The
  first-law identity is established, but the stationarity condition for the tensor block is not derived."
  - Chapter 17 (L121-137): "CRITICAL PATH; OPEN. The fixed-algebra first-law identity is established, but not the
    required stationarity."
  - Closure (sec:ch17-done item 2) requires that Assumption EE be derived for fixed-volume variations, including the
    non-conformal tensor block, without Assumption dictionary.
  - Sub-target here: the G_T = G_A edge term (042), via the gauge-covariant charge (candidate 1) and the T^op
    superpotential (candidate 3, which was the 042 review's rank-1 avenue).
- **Problem D (Appendix H, L555-559):** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL.
  Reduced-scope result: D2, imposed local Lorentz symmetry, supports only a scope-limited Presentation-B model; D
  remains OPEN and the matrix-derived criterion is unmet."
  - Chapter 17 (L329-370): D1 closure requires SO(3,1) gauge symmetry derived from the matrix algebra and condensate,
    with the operators and field content specified, and with frame existence and non-degeneracy derived.
- **Problem A (Appendix H, L15-20):** "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion:
  PROGRAMME-CONDITIONAL. The matrix-to-modular map remains unproved. ..."
- **Critical-path set**, re-derived from sec:ch17-done: A, B, C, D1, E, F, G-derived, N. Appendix H agrees. I found no
  label discrepancy between Chapter 17 and Appendix H.
- **Classification:** PROGRAMME-CONDITIONAL. Nothing is DERIVED.
- **Dependencies:** B depends on A (the state's edge term) and on F (the class in which the axion is not slaved). D1 is
  unchanged.

## Source reading

**Full scan.** `make_digest.py --check` printed `DIGEST STALE (head changed)`. HEAD moved because the 042 integration
was committed (9278fe2) and the SME scout was added (d99eb08). `git status` was clean for chapters/ at the start. I
did not rely on the digest.

Read in full in this session:
- **Chapters:** ch01-ch18. ch06, ch07, ch10 and ch17 were read line by line for this target.
- **Appendices:** appA-appL.
- **Appendix H:** all 2861 lines, read in chunks. This includes:
  - every B block, 031 through 042 (L41-385);
  - the whole Problem D section (L552-1331), including the metaplectic constant-stabiliser paragraph and the
    Hamiltonian-frame paragraph;
  - all F, G, H, I, J and N sections.
- **Other files:** `proposals/strategy-20261025/assessment.md` and its `check_hamiltonian_rotation.py`/out,
  `reports/sme-scout-20261025.md` in full, `proposals/042-constrained-noether-charge/review-r1.md` and
  `proposal-r1.md`, and the `bib/namcg.bib` entries used.

No unreadable files.

## Research and reasoning

### Hypotheses (class)

- **H1.** Poisson limit, four matrix coordinates, omega = Theta^{-1} closed, both signatures; the n_D = 0 bosonic
  content; the LUV^2 density with c_W(r) = N_tot/6 + kappa_X r (merged 038/042).
- **H2.** Backgrounds invariant under the joint flow (tensorial L_xi omega = 0), regular on Sigma, on a star-shaped
  domain (H^1 = 0).
- **H3.** Classical local Noether charges (Iyer-Wald). Closed Sigma or fall-off.
- **H4.** For (ii): linear order about flat space; T^op is the Euler-Lagrange response on the two delta rho = 0 modes.
  The values c_A, c_T are the merged ones (015).
- **H5.** gamma = X*eta is not an independent field (emergence; 042). No other metric is used.

### Part (i): the gauge realisation and the gauge-covariant charge

**Lemma 1 (realisation).** Suppose L_xi omega = 0 and d omega = 0. Cartan's formula gives
d(iota_xi omega) = L_xi omega - iota_xi d omega = 0, so on a star-shaped domain iota_xi omega = d eps.
- **On Sigma.** There xi = 0, so d eps = 0; eps is constant on the connected Sigma and is normalised to 0.
- **Hessian.** d_k d_l eps = d_k xi^n omega_{nl} + xi^n d_k omega_{nl}. On Sigma this is (B^T omega)_{kl}.
  - It is symmetric because (L_xi omega)|_Sigma = (B^T omega + omega B) = 0.
  - It is nonzero because omega is invertible and B != 0.
- **The bracket.** With zeta^n := Theta^{mn} d_m eps one has zeta = xi (contract with omega). Hence
  {eps, f} = zeta.d f = xi.d f for every f. In the matrix chart X^a = x^a and xi^a = B^a_b x^b.

Check (s1, exact): both signatures, for omega = omega_bar + dA with A a random polynomial 1-form invariant under the
joint flow (built from invariant functions and invariant 1-forms). This is a non-family, non-constant omega:
- (a) L_xi omega = 0;
- (b) d eps = iota_xi omega;
- (c) zeta = xi at random points (exact rational);
- (d) eps = d eps = 0 on Sigma, and Hess = B^T omega, symmetric and nonzero;
- (e) xi^a = B^a_b x^b.

The strategy check covered only the Euclidean constant and cone family. This removes that restriction.

**Not new, and tautological in the Poisson limit.**
- The Poisson-limit gauge group acts on the X^a by pull-back along Hamiltonian flows, that is, as Symp(M, omega).
  "The rotation is a gauge transformation" is therefore the statement that xi is a symplectic vector field.
- For constant omega_bar the realisation is merged already (Problem D, constant-stabiliser paragraph: the quadratic
  generator G = 1/4 H{X, X} with delta X = A X, and the metaplectic unitary).
- For quadratic eps (constant omega) the Moyal bracket with any f equals i{eps, f} exactly, so the finite-N inner
  automorphism is the metaplectic one. For non-quadratic eps (the cone family) Moyal corrections make it
  non-geometric. That is a relaxation (avenue 4 below).
- **D1 consequence.** Inside Symp, the stabiliser of a point acts on the jet dX|_p by right multiplication with
  sp(T_p M, omega), as a diffeomorphism. On the gauge-invariant chart data Theta(x) it acts trivially. It is not a
  local SO(eta) action on the matrix index. So no local frame rotation is supplied.

**Lemma 2 (gauge-covariant charge).** In the Moser variables the fields are X^a: M -> R^4, and omega on M is fixed
(not varied). The Poisson-limit gauge transformation is delta_eps X = {eps, X} = L_zeta X, with zeta the Hamiltonian
field.
- **Gauge current equals diffeomorphism current.** Since omega is not varied, delta_eps and L_zeta are the same vector
  field on field space. For a Diff-covariant L(X; omega) one has delta_eps L = L_zeta L = d(iota_zeta L). With the same
  Theta, J_eps := Theta(delta_eps X) - iota_zeta L = J_zeta, so Q_eps = Q_zeta, with identical Y and Z ambiguities.
- **The combined transformation.** It is the Jacobson-Mohd / Prabhu / Elgood-Ortin-type combination: diffeomorphism
  xi followed by the compensating gauge transformation -eps. It acts on the fields as L_xi - L_zeta = 0, identically
  (zeta = xi for all configurations, because omega is fixed). Its Noether current and charge therefore vanish
  identically, and the first law built on it is empty.
- **The gauge charge alone does not vanish on Sigma.** Q_eps = Q_xi depends on d zeta = d(Theta d eps), which involves
  Hess eps != 0 on Sigma. For L = sqrt(G) R_G the Komar density on Sigma is nonzero (s1(g): Q^12 = 8 in both
  signatures for the sample omega). Contrary to the SME expectation, eps = d eps = 0 on Sigma does not make the gauge
  charge vanish: matrix gauge charges carry second derivatives of the parameter.
- **The nontrivial first law in these variables.** On the background, L_xi X = R_B X (the global eta-rotation)
  = delta_eps X. Hence omega(phi; delta phi, L_xi phi) = omega(phi; delta phi, delta_eps phi) = d(delta Q_eps) on
  shell. The identity reads delta Q_eps|_Sigma = (target-space boost charge of the global rotation current through C)
  + infinity, which is the 042 identity with S = Q_eps = Q_xi.
- **The ambiguity.** Y(phi, delta_eps phi) = Y(phi, B X) != 0 on Sigma, as 042 found. Gauge covariance does not
  restrict Y: Y built from (X, omega) is gauge-covariant automatically, since gauge transformations are diffeomorphisms.
- **The x-chart (gauge-invariant) reading.**
  - The push-forward Theta(x) is invariant under Symp, so no matrix gauge freedom remains. If omega = omega_bar + dA
    is written with a potential, the residual freedom is A -> A + d lambda. Under the linearised matrix gauge
    transformation, A_nu = a^mu omega_{mu nu} transforms exactly so (s1(f)).
  - Stationarity up to gauge: L_xi A = d(iota_xi A + eps - epsbar), with d epsbar = iota_xi omega_bar. The compensator
    vanishes on Sigma. With Theta = E-frak wedge delta A plus delta omega-terms (A entering only through omega), the
    compensating charge is lambda E-frak, which vanishes on Sigma (the SME expectation holds here).
  - The remaining charge is 042's, with the same Y ambiguity (Y(dlambda) can be nonzero).

**Hypothesis class of the no-go (i).** H1-H3 and the Poisson limit, with gauge = Symp acting geometrically. Not
covered:
- Moyal / finite-N corrections with non-quadratic generators;
- the CP^{1,2} class, whose fibre-harmonic gauge parameters Lambda = lambda_i(y) e^i act on the level-one frame-type
  amplitudes (merged L2104-2131);
- more coordinates;
- edge-mode extended phase spaces (Donnelly-Freidel, Speranza, which fix the corner Y by boundary data);
- the Dirac sector.

### Part (ii): the superpotential of T^op and the edge terms

**Lemma 3 (classification; s2, exact, both signatures).**
- (a) Write the general symmetric two-derivative tensor linear in h as T = c1 box h + c2 (d d.h + sym) + c3 dd h
  + c4 eta box h + c5 eta dd.h. Identical conservation leaves a two-dimensional space, spanned by G1[h] and
  (dd - eta box) tr h.
- (b) Take the general Sigma_{rho mu nu} linear in d h (nine structures), antisymmetric in (rho, mu), with
  d^rho Sigma symmetric for all h. It has eight free parameters, and every such divergence lies in the span of (a).
- (c) G1 = -k^r k^s K_{m r n s}[h], with K = 1/2(eta H + eta H - eta H - eta H) and H = h - (1/2) eta tr h. This is
  curvature-symmetric (the Abbott-Deser superpotential).
- (d) For a Killing xi and any curvature-symmetric U (generic polynomial Kulkarni-Nomizu sample):
  - xi^nu d^rho d^sigma U_{mu rho nu sigma} = d^rho F_{rho mu}, with F antisymmetric;
  - on Sigma, F reduces to the d xi . U term (the W part vanishes);
  - for the diamond conformal Killing field (the bulk term (dd xi).U) the remainder is nonzero.

**Consequence for Eq. (Top-FP).**
- On traceless T (and at fixed volume) any superpotential in delta<T^op> is lambda E[T]. On the wedge, its edge term
  is the lambda-multiple of the Abbott-Deser charge, that is, of the area-type term of Jacobson's identity.
- "Absorbing the edge contribution into the area term" is therefore equivalent to shifting the coefficient of E in
  the stress. The Remark after Theorem thm:mT in Ch. 7 already says the E-coefficient equality belongs to hypotheses 5 and 6.
  There is no conflict, so no PRIOR-CLAIM-ERROR.
- The sentence "On a diamond the superpotential contributes only at the edge" holds only up to the (dd xi) bulk term,
  which the fixed-volume constraint handles. It is not made false here.

**T^op on the delta rho = 0 modes.**
- If T^op is the metric response, it is the Euler-Lagrange expression of the on-mode quadratic action. That action is
  c_T x (linearised EH) (merged 015). The Euler operator annihilates total divergences, so there is no superpotential
  freedom in the bulk, and the coefficient is c_T = N_tot/6 - 4 kappa_X = c_W(-4).
- The edge term "implied by T^op" is thus the r = -4 term, by construction: r = -4 is defined by on-mode agreement
  (merged 038/041).
- The first law, with the area term of the fixed-state replica, has c_A = c_W(0). Closing it needs -4 kappa_X from the
  modular Hamiltonian.
- **Answer to the question.** The T^op side is fixed (-4). The replica side is 0 (fixed-state), -1 (with the Maxwell
  edge sector), or -2 (only with the stipulated 039 dressing). They match for no merged replica.

**Chen-type consistency (Chen 2202.00680, verified; pages read listed in Result).**
- (3.35)/(3.59): K^mat = integral of J^mat_xi + integral over R of xi.L^{M,mat}, where R is the outer boundary. There
  is no term at sigma in this form.
- Writing J = dQ + xi.C, with C_g proportional to the stress ((E.40)), the stress-integral form of K differs at sigma
  by -integral of Q^mat: the Wald-like terms (abstract; Section 1).
- Footnote 40: Y = 0 and Z = 0 must be chosen to equate Wald-Dong and Noether-charge entropies.
- App. E: the background dependence of the measure gives theta^an, Q^an and J^an ((E.43)-(E.44)). The anomalous
  Wald-Dong entropy is defined by the replicated measure ((E.26)-(E.27)), with •_{×n} "a deformation localized in the
  tiny neighbourhood N_a(sigma) which multiplies the opening angle around exactly sigma by n" (footnote 92).
- **NAMCG, tree-level fluctuation Lagrangians.**
  - The scalar is rho K^{mu nu} d phi d phi.
  - The connection is rho [K d a d a - 2 a{Theta, a}] with the gauge-fixing rho (D.a)^2, or in Moser form
    rho G G F F + b eps F F.
  - The ghosts are algebraic in, or first-order in, the background.
  - So Q^mat|_Sigma = 0 for regular fluctuations: the 042 Step-3a lemma applies to all first-order densities,
    fluctuations included.
  - The Chen Wald-like edge term is therefore 0, and r_eff = 0.
- **The measure term.**
  - In the class, about constant Theta-bar with Theta the only field, a compactly supported first-order perturbation
    has zero flux of grad ln rho at large radius. By the merged identity (integral of R_G^(1) over the normal plane
    = -2 x flux), the total deficit is zero.
  - So no localised deformation changes the opening angle. Chen's construction of S^{WD,an} cannot be realised in the
    class: the same obstruction the merged text records for Lewkowycz-Maldacena.
  - Conclusion: Chen's consistency theorem does not apply inside the four-coordinate class and selects nothing there.

**The Maxwell edge sector in Moser variables (bridging merged 036 and 041).**
- Merged 036 (replica-prescriptions paragraph): the Kabat contact "presupposes a U(1) structure and a Ricci coupling
  that the operator O_v does not have in the variables (G, rho, d Theta) ... it remains an input".
- Merged 041: on J = dJ = 0 jets (numerically), S O_v S^{-1} equals the Maxwell-axion operator, that is, Hodge with
  dilaton and axion terms. Its a_1 is -R/3 + ... = 4/6 - 1 per vector, so the Ricci coupling is present.
- The linearised gauge transformation delta a^mu = Theta^{mu rho} d_rho lambda (Remark ch3-trace-quadratic) acts as
  delta A_nu = -d_nu lambda on A_nu = a^mu omega_{mu nu}, exactly (s1(f), opposite sign convention there). So the U(1)
  structure is present too.
- With the Kabat value -1 (merged: "the value that takes the vector with its ghosts from 1/3 to -2/3", the edge-mode
  term of Donnelly-Wall), the area coefficient becomes c_A - 1 = c_W(-1) at n_D = 0 (s3(2)).
- The remainder c_W(-1) - c_W(-4) = 3 kappa_X is, by the 041 stationary-set identity
  6 s|d theta - theta V|^2 = -3 R_G + 6|V|^2 - 9 box ln rho (s3(3)), the axion-gradient term.
  - That term is first-order in (G, rho, vartheta): no Noether charge on Sigma, no Wald-like term, and no Maxwell edge
    term.
  - On the off-shell modes, 041 records that the axion term and the J-proportional part are each mode-dependent and
    only their sum is proportional to the kernel. The on-mode split is therefore stated only through the
    stationary-set identity, and the J-part is not characterised here.
- **Status of this decomposition.** It is an observation from merged results plus one exact identity (s1(f)). It is
  not a derivation that the state carries the edge sector.

**Fork table (no-go is a fork).**

| Hypothesis | Relaxation | Explored here? | Outcome |
|---|---|---|---|
| Poisson-limit gauge = Symp (geometric) | Moyal / finite-N inner automorphisms with non-quadratic generators | argued | quadratic: exactly metaplectic, so no change; non-quadratic: non-geometric corrections O(theta^3 d^3 eps d^3 f), not computed (avenue 4) |
| Momentum-map term built on the gauge charge | gauge-invariant chart variables | done | vanishes on Sigma; charge = 042's |
| Classical local charges (Y free) | edge-mode extended phase space fixing the corner term | no | avenue 2 |
| T^op as EL response | T^op as target-space T_eta (042) | done (042) | any r, by improvements; no selection |
| T^op superpotential | single- or double-divergence, local, linear | done (classified) | always lambda E: no independent edge term |
| Chen Wald-like term | tree-level fluctuation Lagrangians | done | zero on Sigma |
| Chen measure term | localised opening-angle deformation | done (merged obstruction) | unavailable in the class |
| Edge modes | Maxwell edge sector of the symplectic U(1) (Moser) | done (bookkeeping) | supplies kappa_X (Kabat value), if carried by the state |
| vartheta slaved to G (four coordinates) | class with vartheta independent of the tensor modes (rank-6 / more coordinates / CP^{1,2}) | argued | then c_T would be c_W(-1) (if the R-coefficient stays the Hodge one), and the Maxwell edge would close the first law; conjecture, avenue 1 |
| n_D = 0 | Dirac sector (kappa_X = 1 - n_D/2) | no | avenue 5 |

### Literature checked

**Fetched in this session:**
- Chen, "The generalized first law for more general matter", arXiv:2202.00680, JHEP 04 (2022) 076,
  doi:10.1007/JHEP04(2022)076. Checked against the arXiv API: title, author, journal_ref and doi. Full-text pages
  read: 1-5, 26-31, 63-80.
- Jacobson-Mohd, arXiv:1507.01054, PRD 92, 124010. Abstract checked via the arXiv API: entropy is the Noether charge of
  the combined diffeomorphism plus local Lorentz transformation; the diffeomorphism charge alone fails because a
  regular frame cannot be invariant at the bifurcation surface.

**Not fetched; used only as merged manuscript statements:** Donnelly-Wall (in bib, used in merged text), Kabat,
Herzog-Nishioka, Iyer-Wald, JKM.

**Not independently verified; mentioned only in this proposal, not in the insert:** Prabhu 1511.00388 and
Elgood-Meessen-Ortin 2006.02792 (the SME read them at abstract level; I did not fetch them).

## Claim classification

| Claim | Class |
|---|---|
| iota_xi omega = d eps, eps = d eps = 0 on Sigma, Hess = B^T omega != 0, {eps, f} = xi.d f, for every joint-flow-invariant omega on a star-shaped domain | established (proof; exact checks s1(a)-(e)) |
| The rigid rotation is a Poisson-limit gauge transformation; not new; isotropy, not local Lorentz | established (proof); the "not new" part is a comparison with the merged D paragraph |
| Q_eps = Q_zeta in Moser variables; the combined (xi, -eps) charge vanishes identically; the gauge charge on Sigma is nonzero for curvature densities | established (formal proof; s1(g) sample) |
| In the x-chart potential reading, the compensating charge vanishes on Sigma | established for Theta = E-frak wedge delta A (presentation stated); Y-dependence noted |
| Gauge covariance does not select r | established within H1-H3 (bounded no-go) |
| Classification of identically conserved two-derivative tensors, single divergences, Abbott-Deser form | established (exact, s2) |
| Boost charge of dd U: pure edge on a Killing wedge; bulk remainder on a diamond | established (exact identity, s2) |
| T^op on the modes carries the r = -4 edge term; the stress supplies none of the gap | established, conditional on merged c_T and c_A (015) |
| Chen: K = integral of J^mat + outer term; Wald-like and measure terms; Y = Z = 0 choice | literature, verified |
| Chen Wald-like term zero for NAMCG tree-level fluctuations | established (042 first-order lemma applied) |
| Chen measure construction unavailable in the class about constant Theta-bar | conditional (merged flux identity; first order) |
| delta A = -d lambda for A = a.omega (exact); Moser operator has the Ricci coupling (merged, numerical on the stationary set) | established / conditional (merged numerical) |
| Kabat / DW contact gives c_W(-1); remainder 3 kappa_X = axion-gradient part | conditional: input contact, numerical stationary-set identity |
| A class with vartheta independent would close with the DW edge | conjecture |
| Ch. 7 Eq. (xi-RNC) sign error | established (exact CKV check, s2) |

## Proposed changes

**File `chapters/appH-microscopic-proofs.tex`.**
- Insert the block `appH_insert.tex` (UTF-8, LF, ASCII, 7.6 kB; braces and \( \) balanced) immediately before the
  unique line `\section{Problem C: conformal mode and Cassini}`, with one blank line before it.
- The anchor was checked: it occurs exactly once (L387).
- The new paragraph title "Matrix gauge realisation of the compensating rotation, the superpotential of the stress and
  the edge term" occurs 0 times in the chapters.
- Nothing existing is replaced. The block closes with one scoped status sentence ("Problems~B and~D remain open and
  PROGRAMME-CONDITIONAL.").

```latex
% contents: see appH_insert.tex in this folder (verbatim; not duplicated here to avoid drift)
```

**Labels used, each verified to occur exactly once:**
- `sec:status-D` (appH L553);
- `eq:Top-FP` (ch07 L149);
- `rem:ch3-trace-quadratic` (ch03 L450).

**Macros and citations:**
- `\LUV` is defined at `namcg-book7.tex:54`.
- `JacobsonMohd2015` and `DonnellyWall2016` are each present once in `bib/namcg.bib`.
- `Chen2022` is new.

**File `bib/namcg.bib` (integrator).** Add the entry in `bib_add.bib`. It was verified against the arXiv API (doi and
journal_ref); a duplicate check finds no "Chen2022" or "2202.00680" in the bib.

```bibtex
@article{Chen2022,
  author  = {Chen, Hong Zhe},
  title   = {The generalized first law for more general matter},
  journal = {Journal of High Energy Physics},
  volume  = {2022},
  number  = {4},
  pages   = {076},
  year    = {2022},
  doi     = {10.1007/JHEP04(2022)076},
  eprint  = {2202.00680},
  archivePrefix = {arXiv}
}
```

**Stale passages.**
- I found no merged sentence that this result makes false.
- The 036 replica-prescriptions sentence ("Its use presupposes a U(1) structure and a Ricci coupling that the operator
  O_v does not have in the variables (G, rho, d Theta) ... it remains an input") stays true. It is scoped to those
  variables, and the insert keeps the contact as an input ("If the state carries that edge sector").
- The 042 consequence sentence ("... or of a local symmetry under which the compensating rotation would be a gauge
  transformation ...") stays true. The insert shows that the Poisson-limit gauge realisation is not such a local
  symmetry of the index.

**Separate side finding (not part of the insert; recommended as its own one-line correction item).**
- `chapters/ch07-massless-tensor.tex` Eq. `eq:xi-RNC` (L224-227), old (occurs once):
  `   \bigl((\ell^2-t^2-r^2)\partial_t^\mu+2t\,x^\mu\bigr)`
- New: `   \bigl((\ell^2-t^2-r^2)\partial_t^\mu-2t\,x^i\delta^\mu_i\bigr)`
- Reason: with +2t x^i the field is not conformal Killing (d_0 xi_i + d_i xi_0 = 4A x_i != 0). Jacobson's diamond field
  is (l^2 - t^2 - r^2) d_t - 2 t r d_r. The s2 output records the exact check.
- Classification: pre-existing error, independent of this package. I flag it rather than fold it into the insert.

## Verification scripts

| File | Runtime | What it checks |
|---|---|---|
| `s1_gauge_realisation.py` / `.out.txt` | ~1 min | Lemma 1, both signatures, non-constant non-family invariant omega: (a) invariance; (b) d eps = iota_xi omega; (c) zeta = xi; (d) Sigma data and Hessian; (e) the matrix-chart rotation. Also (f) delta A = d lambda for the linearised gauge transformation (sign convention {lam, x^mu}), and (g) a nonzero Komar density of sqrt(G) R_G on Sigma for the gauge field. Result: ALL CHECKS PASSED |
| `s2_superpotential.py` / `.out.txt` | ~10 min | Lemma 3 (a)-(d), both signatures; the diamond CKV check and the Ch. 7 sign side finding. Result: ALL CHECKS PASSED |
| `s3_edge_bookkeeping.py` / `.out.txt` | seconds | Kabat trace of the Ricci delta (tr Q = 1); the Hodge R-coefficient -1/3 giving r = -1; the stationary-set split -4 = -1 + (-3); the residue table |
| `compile_check.py` / `.out.txt` | — | Scratch compile outside the repository of the CURRENT working tree, baseline and with the insert plus bib entry, then deletion of the scratch copy |

Compile results:
- **Baseline:** 315 pages, exit codes [0,0,0,0], 0 undefined references or citations, 0 multiply defined labels.
- **With the insert:** 317 pages, the same zero counts.
- CRLF line endings preserved; scratch copy removed. `git status` afterwards shows only this proposal folder.

## Decisions Taken

1. **Both readings of "gauge-covariant charge" were run** (the matrix/Moser variables and the gauge-invariant chart
   with a potential). They are the two natural presentations, and the SME expectation holds in one and fails in the
   other. Rejected alternative: running only the Elgood-type momentum-map reading, which would have suggested a clean
   "vanishes on Sigma" and hidden that the charge in matrix variables is the Wald charge itself.
2. **T^op was defined as the Euler-Lagrange response to G on the delta rho = 0 modes**, following the 042 review
   avenue 1 and Ch. 6 Prop. ward ("metric variation of the quadratic action of that block"). Rejected alternatives:
   - the target-space T_eta, already treated by 042 (any r);
   - a response at fixed complementary variables, which needs off-class variations of G and is not physical in the
     class.
3. **Chen was chosen as the published consistency mechanism and actually checked** (full text, not only the abstract).
   It led to the class obstruction on the measure term. Rejected alternative: asserting "edge = Wald-Dong, hence
   r = -4". That would have been circular, because r = -4 is defined by on-mode agreement.
4. **The Maxwell edge-sector observation was recorded as conditional** ("if the state carries that edge sector"). It is
   not recorded as a derivation, and it is kept inside the insert because it changes how the residue reads (kappa_X +
   3 kappa_X). This favours the full-GR route by pointing to a specific missing ingredient: an independent
   pseudoscalar.
5. **The Ch. 7 sign error is reported as a separate side finding**, not folded into this insert. It is unrelated to B's
   residue, and smallest-change discipline argues against bundling.
6. **No structural change and no emergence violation.** gamma is never made dynamical, and the potential A is a
   bookkeeping variable for the closed omega, not a field.

## Milestone assessment

Routine. Two bounded no-gos (gauge covariance in the Poisson limit; the T^op superpotential) and a conditional
localisation of the residue. No critical-path step is derived, and no M-trigger applies. This is not a breakthrough:
r is not fixed from matrix data.

## Status-label recommendation

The critical-path list from sec:ch17-done is A, B, C, D1, E, F, G-derived, N. Affected labels: none. B, D and A stay
"OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL". No label change is proposed.

## Author decision needed

None.

## Remaining open step

To close the G_T = G_A sub-target of B, one of the following is needed:

1. **(A ∩ B; highest)** Derive the modular Hamiltonian of the one-loop state on a joint-flow-stationary background,
   with its edge sector, and decide whether it carries the Maxwell edge modes of the symplectic U(1) (kappa_X) and
   what supplies the remaining 3 kappa_X. A first package: the free connection sector in Moser variables, comparing
   the Frenkel-Hartnoll Gauss-law edge entropy with the DW edge density.
2. **(F/B class transfer; candidate 2)** In a rank-6 class (D >= 7 embedding, or CP^{1,2}, or fuzzy-K), test whether
   the pseudoscalar vartheta (or its analogue) decouples from the tensor polarisations. If it does, c_T = c_W(-1),
   and the DW edge closes the first law: a concrete, falsifiable conjecture from this package.
3. **(Corner data)** Use an edge-mode extended phase space (Donnelly-Freidel, Speranza) for the symplectic gauge
   sector to fix Y on Sigma by boundary data, not by the density.
4. **(D1, beyond the Poisson limit)** Moyal/finite-N inner automorphisms with non-quadratic generators, and the
   CP^{1,2} fibre-harmonic gauge parameters acting on the level-one frame amplitudes: do they contain local rotations
   of the frame index?
5. **(Dirac)** Repeat the bookkeeping with kappa_X = 1 - n_D/2 and the Lichnerowicz contact.

The overall closure target of B (Assumption EE derived for the tensor block without Assumption dictionary) stays
open, with all of A, D1 and F as dependencies.

## Special instructions for the gatekeeper

- **Do not assert:**
  - that the matrix gauge group supplies local Lorentz symmetry;
  - that r is fixed;
  - that the DW/Kabat edge sector is carried by the matrix state;
  - that a class with independent vartheta exists or closes B.
  The last two are conditional or conjectural.
- **Re-derive Lemma 2 independently.** In the Moser variables omega is held fixed, so delta_eps = L_zeta exactly on
  field space. This is the step that makes the combined charge vanish identically and the gauge charge equal the Wald
  charge. If omega were varied, zeta would depend on delta omega; that is outside the matrix model, where omega on
  the leaf is fixed.
- **Check s2(b).** It finds 8 free parameters for single divergences. The claim is only that their divergences lie in
  span{G1, trace term}. The number of parameters includes identically divergence-free pieces, which carry no
  current.
- **Scope of the Chen measure-term obstruction.** It uses the merged flux identity (appH replica-prescriptions
  paragraph, "Intermediate flux") about constant Theta-bar at first order, so it is scoped "about constant
  Theta-bar". Please confirm footnote 92 and (E.26)-(E.27) of Chen; the saved PDF pages 64-80 were read.
- **Scope of the 3 kappa_X attribution.** It rests on the 041 stationary-set identity (numerical, J = dJ = 0 jets).
  On the off-shell modes, 041 says the axion and J-parts are separately mode-dependent. The insert attributes 3 kappa_X
  to the axion gradient only "by the stationary-set identity".
- **The Ch. 7 Eq. (xi-RNC) side finding** is outside this insert. Please verify it (CKV condition) and route it as a
  separate item if confirmed.
- **Hard-coded numbers.** The insert uses none (it refers to "Section~\ref{sec:status-D}", "Remark~\ref{...}", and
  "the paragraph on ...").
