# Proposal 038-lambda2-frame-entropy, round 1

## Result
Bounded, reproducible obstruction at order Lambda^2 under the 031 hypotheses; Problems B and A stay open. No match. Nothing below is a candidate breakthrough.

Hypotheses of the obstruction (all stated in the LaTeX block): Poisson limit, Euclidean section, one loop, alpha = 1, the Lambda^2 term, totally geodesic Sigma, first order in 1-n, the family Theta^12 = 1/f, Theta^34 = 1 with f = |z|^(n-1) (c_a = 1), the first-order additive cross-term rule, the Dirac extension and replica gluing of the ledger, and c_A, c_T taken from Appendix H.

1. Residue before any contact (non-vacuous test). In units S = (Lambda^2 A/8pi) c, 1/G = c Lambda^2/(2pi): c_A = N_tot/6, c_T = N_tot/6 - 4 kappa_X. At n_D = 0: c_A - c_T = 4 for every N_s, that is 1/G_A - 1/G_T = 2 Lambda_{UV,v}^2/pi. It is nonzero before any contact is added (s7).
2. Hypotheses (B-R2). Iyer-Wald needs (i) a diffeomorphism covariant Lagrangian of the dynamical fields, (ii) stationary fields, L_xi phi = 0, (iii) regularity on the bifurcation surface, (iv) the field equations for J = dQ. Results (s3, s5, s8):
   - The scout's boost-invariance observation is true but is not Lie-dragging. The 031 family (any f(r), Euclid rotation and Lorentz boost) and every constant Theta-bar commuting with J_12 (span of e12, e34: 2 of 6 components) are invariant under the JOINT flow (chart and matrix index rotated together). Under the diffeomorphism alone the Lie derivative of Theta-bar = a(e12+e34) is +-a diag(1,1,0,0), nonzero everywhere. In the coframe e^A_mu = eta^{AB} omega_{mu B}, L_xi e^A_nu = e^A_sigma d_nu xi^sigma on Sigma, so e_{A mu} L_xi e^A_nu = nabla_nu xi_mu, the Komar integrand.
   - Regularity holds for the n = 1 background and fails for the replica family at first order: Theta^12 = 1 - (n-1) ln r + O((n-1)^2), X = 2 (n-1)^2 r^(-2n).
   - Covariance: the induced density (N_tot/6) rho R[g_rho] + kappa_X rho^2 X is a diffeomorphism covariant first-order functional of the coframe (X = T_{lmn}T^{lmn} is a coframe scalar), but the Theta-slice (eta_{AB} e^B_mu antisymmetric) is not preserved by chart changes (s3, item 5), so the equations of motion available are the slice equations; and X is not invariant under local frame rotations: among a TT + b TT' + c V^2 only (1/4, 1/2, -1) is (s8, d = 3, 60+ digits).
   - Einstein-aether warning: the failure is of the same type (frame not dragged by xi), with the difference that a compensating rotation exists but is rigid (a global symmetry of the induced density), so the charge of the compensator is not an exact form.
3. Main computation (B-R1, s2, s7). Contacts at Lambda^2 (n_D = 0, alpha_v = 1, sigma = +1 on n<1):
   - Endomorphism contact (E_V, E_f with the uniform delta, Q = 1/4): -N_tot/4. It carries N_s, so it cannot follow a gap that does not depend on N_s. With the connection sector at its own cutoff the residue is (7/2) Lambda_v^2 - (N_s/4) Lambda_s^2.
   - Vector holonomy contact: from the exact twisted-cone constant C(n,a) = B_2(a)/(2n) - n/12 (agrees with a Bessel-order sum to 1e-12), the shift is -alpha_v sigma. For alpha_v = 1: -1 on n<1 (the Kabat value in these units), +1 on n>1.
   - Dirac holonomy contact: zero at first order (a^2 + 1/6 per block, symmetric twists sum to zero).
   - Residues c - c_T: fixed-state 4; fixed-state + holonomy 3 (n<1) / 5 (n>1); E_delta only 7/2 - N_s/4; E_delta + holonomy 5/2 - N_s/4 / 9/2 - N_s/4. With fermions: 4 - n_D, 4 - n_D - alpha_v sigma. Zeros only at special content (N_s = 14, 10, 18; n_D = 4, 3), never for all N_s.
   - Noether term of rho^2 X: the pure-diffeomorphism charge of any first-order frame Lagrangian is Q^{mu nu} = pi^{mu nu}_A e^A_sigma xi^sigma (J = dQ - E e xi checked at three random fields to 1e-30), so it vanishes on Sigma, and the Noether coefficient is the coefficient of R in the chosen presentation. It is not unique because R = -calT - 2 div V. With X = (2/3)V^2 + S^2 + q^2, calT = -(2/3)V^2 - (1/4)S^2 + (1/2)q^2 (exact), the R-coefficient of X is r = 0 (variables (G,rho,b)), -2 (keep V^2,S^2: the ledger identity, re-verified), 1, 4, or any real r. c_W(r) = N_tot/6 + kappa_X r and c_W - c_T = kappa_X (r+4): zero for all contents only at r = -4, the presentation whose torsion remainder vanishes on every delta-rho = 0 mode (on those modes S^2 : q^2 : X = 1/3 : 2/3 : 1 and <R> = -<X>/4) and not on pairs of modes. The ledger value r = -2 leaves 2 kappa_X.
   - Cross term of rho^2 X with the cone connection b = (1-n) J dtheta is (n-1) int Omega_12 ln(L/r) d^2x (exact for polynomial beta, s6): a bulk term with Green-function weight, not an area term.
4. Outcome: mismatch. No contact examined and no Noether value supplies the required -4 kappa_X of c; the available vector contact has modulus 1, the E_delta contact depends on N_s, and the Noether coefficient is a free real until the frame is dragged by a flow whose internal part is a local symmetry (Problem D link). The same residue 2 kappa_X appears at order W in 037 (E(1,1) - E(2,2) = 2 kappa_X) and here for the ledger presentation r = -2: in both cases it equals the on-mode value carried by the non-Levi-Civita part (axial torsion S here, the part N of the bundle curvature there).

## Target and status
Problems B and A (Appendix H, working tree). B: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL." A: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL." Chapter 17 (L123-L139 re-read): B "CRITICAL PATH; OPEN", closure requires fixed-volume variations of the non-conformal tensor block from the microscopic action, a specified map g^(0) -> g, and no use of an existing metric; Chapter 17 requires A, B, C, D1, E, F, G-derived, N, and H, I, J optional. No discrepancy found between Chapter 17 and Appendix H for B and A. Original target of B: derive the stationarity delta S_D = 0 and the area term from the microscopic dynamics. This package is PROGRAMME-CONDITIONAL and closes nothing.

## Source reading
Digest + targeted reads, not a full scan. scratch/digest.md read first (it reports dirty-chapters: yes, as expected after 037). Read in full: Appendix H Problem B section L41-L305 (including the normalisation paragraph L174-L179, the 031, 033, 035, 036, 037 blocks), reports/sme-scout-BF-20261024.md, proposals/037-comparator-first-law/proposal-r2.md and review-r2.md, the Presentation-A paragraph and the torsion-invariant paragraph in Problem F (L1815-L1870, L2013-L2020), the Chapter 17 B entry and status words. Sources opened: Iyer-Wald arXiv PDF text (equations for the ambiguities, Theorem 6.1, the line "Since L_xi phi = 0 the term Y vanishes"), Jacobson 0801.1547 PDF text (G_N formula, black-hole thermodynamics remark). Abstract pages only: Jacobson-Kang-Myers, Foster, Mohd, Hammad et al., Ding-Zhai, Solodukhin 1502.03758.

## Research and reasoning
Setting and notation as in the 031 hypotheses and the block. Everything below is either an exact computation (script, saved output) or marked.

A. Hypotheses (target 1).
- s3: joint versus pure Lie derivative of Theta^{mu A}; invariant subspace of constant Theta-bar (only t12, t34 survive); family invariant for arbitrary f(r) in both signatures; finite rotation check; regularity of the family (Theta^12 = r^(1-n), X = 2(n-1)^2 r^(-2n), X u^2 = 2(n-1)^2/n^2 with u the proper distance, as in the ledger); a nonlinear chart change leaves the antisymmetric slice.
- Iyer-Wald (arXiv text read): the charge decomposes as W xi + X nabla xi + Y(phi, L_xi phi) + dZ with ambiguity Q -> Q + xi.mu + Y + dZ, and Theorem 6.1 removes Y because L_xi phi = 0. So uniqueness of the entropy needs L_xi phi = 0. Here L_xi e|_Sigma != 0 for a boost.
- Foster (abstract): in Einstein-aether theory the standard first-law derivation breaks down because the unit vector must be singular at the bifurcation surface; no definitive entropy. Jacobson 0801.1547 (text): G_N = G/(1 - c_14/2) and the black-hole entropy is not identified; this is the same structure as G_T versus G_A (a first-derivative coefficient separates the tensor/Newtonian normalisation from the action's R coefficient). The scout attributed the Lie-dragged-and-regular requirement to Mohd 1309.0907; the abstract I read does not say that, so I do not use that attribution.
- s5: for L(e, de) = sqrt(g)(a TT + b TT' + c V^2) in d = 2, J^mu = d_nu Q^{mu nu} - E^mu_A e^A_sigma xi^sigma with Q^{mu nu} = pi^{mu nu}_A e^A_sigma xi^sigma, residual about 1e-30 at three random polynomial fields (Hessian chain rule, 30 digits). The derivation (Noether identity plus GL(d) covariance) is dimension independent. Hence torsion invariants have no pure-diffeomorphism charge on Sigma.
- Consistency of the non-uniqueness: R + calT + 2 div V = 0 is an identity of functionals of e, so sqrt(g)(R + calT + 2 div V) is a total derivative and its charge is Y(e, L_xi e) + dZ, which at Sigma is the Komar quantity above; flat-space Rindler shows it concretely (Komar nonzero, torsion charge zero). The teleparallel literature points the same way (Hammad et al.: the Noether-charge entropy of teleparallel gravity is expressed as a volume integral; abstract only).
- s8: antisymmetric part of E^mu_A e_{B mu} computed numerically in d = 3; its null direction in (TT, TT', V^2) is (1/4, 1/2, -1) to 10 digits, residual 1.7e-29 (TEGR combination), while X alone gives 4.6. So the class of X modulo that direction (a 2-dimensional quotient) is canonical and nonzero for kappa_X != 0.

B. Torsion algebra (s1, s4).
- s1 (exact rationals): TT = (2/3)V^2 + S^2 + q^2; TT' = (1/3)V^2 - S^2 + (1/2)q^2; calT = -(2/3)V^2 - (1/4)S^2 + (1/2)q^2. R-coefficient of X after eliminating q^2, S^2, V^2: -2, 4, 1 (with S^2 coefficient 3/2 and V^2 coefficient 2 for the first, equal to the ledger identity rho^2 X = -2 rho R[g_rho] - ... + (3/2) rho^2 S^2 + ...). At three random two-jets of a closed omega (Euclid): V_mu = d_mu ln rho, R = -calT - 2 div V, E_s = R/4 + TT/16 + TT'/8, sqrt(G) = rho^2, and the ledger identity for rho^2 X, all exact.
- s4: on delta-rho = 0 modes about constant SD and ASD Theta-bar (three backgrounds), S^2/X = 1/3, q^2/X = 2/3, -calT/X = -1/4, V = 0. Therefore the ledger's mode eigenvalues (X: 1, rho R: -1/4) are reproduced, and the R-free remainder X + 4R = 2S^2 - q^2 vanishes on every mode (cross terms between modes of different wave vector are nonzero, so it is not null as a quadratic form; the values on modes do not fix the entropy, the Lambda^2 analogue of the 037 finding).

C. Contacts (target 2).
- s2: C(n,a) = B_2(a)/(2n) - n/12 against the Bessel-order integral sum over m of I_{|m+a|/n}: agreement 1e-12 at 12 pairs (n,a) including n = 1, a = 0.3, 0.5, 0.8 (Aharonov-Bohm -a(1-a)/2). First order: per twisted component shift/eps = -alpha/2 (n<1), two components with J = +-1: -alpha_v sigma.
- s7: Dirac: sum over a_k of (a_k + d)^2 has no term linear in d for n = 2, 3, 4, 5, 7 (assert); table of residues; per-sector cutoffs: after E_delta residue (7/2) Lambda_v^2 - (N_s/4) Lambda_s^2; c-to-G conversion 1/G_A - 1/G_T = 2 Lambda_v^2/pi.
- The Kabat check: the vector contact for alpha_v = 1 is -1 on n<1 = the ledger's Kabat value (vector with ghosts 1/3 -> -2/3), obtained here from the twisted-cone constant and not imported.

D. Comparison and decision (target 3). Residue before contact: 4 (c units) = 2 Lambda_{UV,v}^2/pi, nonzero. After each contact the residue is nonzero for all N_s (rows 1-2) or N_s-dependent (rows 3-4). A match for all N_s and Lambda_{UV,v} is not obtained. Matches at special content (N_s = 14, 10, 18 or n_D = 4, 3) are content choices and are not used. A second circulation |c_b| = 3 would close the bosonic gap but is fiat and singular.

E. What was not done / limits. The first-order additive rule is assumed for the combined E_delta + holonomy row; the exact spectrum of the singular cone with both the first-derivative term -(1/2) d ln rho and the holonomy (indices of the type sqrt((k+a)^2 + eta^2)/n, not verified) would make the first-order coefficient non-rational and is not computed. Dirac extension, gluing and c_T are inputs from the ledger.

Literature checked and not used in the block: Hammad et al. 1912.08811 (PRD 100, 124040; abstract), Ding-Zhai 2001.06261 (CQG 37, 185015; abstract: the Wald method does not work in their theory, Killing-horizon entropy A/4 in their solutions), Solodukhin 1502.03758 (PRD 91, 084028 per the arXiv page; abstract: contact terms arise from mediators, proposes S_BH = S_ent in theories with mediators), Mohd 1309.0907 (abstract). Not independently verified: any statement beyond the abstract in those four papers; Prabhu 1511.00388 not opened.

## Claim classification
- Established (exact or high-precision computation): twisted-cone constant and the first-order holonomy contact; the table of residues (given the ledger inputs); the torsion decomposition and the R-coefficients -2, 4, 1; the identities R = -calT - 2 div V, V = d ln rho, the ledger identity for rho^2 X; S^2 : q^2 : X = 1/3 : 2/3 : 1 on the modes; J = dQ - E e xi with Q proportional to xi; joint versus pure Lie derivative; singularity of the replica family; the cone cross term as int Omega ln(L/r); the TEGR null direction (numerical, d = 3).
- Conditional: all statements about entropy of rho^2 X (they use the Iyer-Wald structure for the coframe presentation); the additive rule for the combined row; Dirac holonomy contact zero (less singular extension); c_A, c_T inputs.
- Input: c_T = N_tot/6 - 4 kappa_X, c_A, delta content, Dirac gluing (ledger).
- Conjecture/mechanism: the link of the free r with Problem D (local Lorentz) and the statement that a local-symmetry compensator would fix r.
- Unresolved: the first law with the rigid compensating rotation; the exact singular-cone spectrum; the replica selected by the matrix state; the constraint-term charge.

## Proposed changes
File chapters/appH-microscopic-proofs.tex: insert the block of appH_insert.tex (10032 bytes, 0 TAB, 0 CR, ASCII, balanced braces and math delimiters) immediately before `\section{Problem C: conformal mode and Cassini}`, after the 037 block that ends "Problem~B stays open and PROGRAMME-CONDITIONAL." followed by one blank line. The anchor occurs exactly once (line 306 of the working tree, checked with grep). Nothing is replaced. No `\label` and no `\ref`. New cite keys: IyerWald1994, JacobsonKangMyers1994, Foster2006 (BibTeX below, Crossref-verified: DOI records returned the stated authors, titles, volumes and pages; none of the three keys exists in bib/namcg.bib, checked). Existing key used: LewkowyczMaldacena2013. Compile check in a scratch copy outside the repository (block and bib entries inserted, pdflatex, bibtex, pdflatex x2): 305 pages, 0 undefined or multiply defined references, no overfull box reported at the block's lines (compile_check.out.txt).

The LaTeX block is the file `proposals/038-lambda2-frame-entropy/appH_insert.tex` (identical text; not repeated here to avoid divergence). Its stale-passage consequences: none (the block adds a paragraph; the sentence in the normalisation paragraph "contributes no entropy" is unchanged and still correct for the fixed-state replica; the 037 block's remark that the Lambda^2 gap "is not addressed" is now addressed by the new block at the stated hypotheses).

BibTeX (append to bib/namcg.bib):
```bibtex
@article{IyerWald1994,
  author  = {Iyer, Vivek and Wald, Robert M.},
  title   = {Some properties of the {Noether} charge and a proposal for dynamical black hole entropy},
  journal = {Physical Review D},
  volume  = {50},
  pages   = {846--864},
  year    = {1994},
  doi     = {10.1103/PhysRevD.50.846},
  eprint  = {gr-qc/9403028},
  archivePrefix = {arXiv}
}

@article{JacobsonKangMyers1994,
  author  = {Jacobson, Ted and Kang, Gungwon and Myers, Robert C.},
  title   = {On black hole entropy},
  journal = {Physical Review D},
  volume  = {49},
  pages   = {6587--6598},
  year    = {1994},
  doi     = {10.1103/PhysRevD.49.6587},
  eprint  = {gr-qc/9312023},
  archivePrefix = {arXiv}
}

@article{Foster2006,
  author  = {Foster, Brendan Z.},
  title   = {Noether charges and black hole mechanics in {Einstein}-aether theory},
  journal = {Physical Review D},
  volume  = {73},
  pages   = {024005},
  year    = {2006},
  doi     = {10.1103/PhysRevD.73.024005},
  eprint  = {gr-qc/0509121},
  archivePrefix = {arXiv}
}
```

## Verification scripts
Run with `python <script>` from the proposal folder (sympy 1.14, numpy, scipy, mpmath; no imports between scripts). Saved outputs `*.out.txt`.
- s1_torsion_presentations.py (28 s): irreducible split of TT, TT', calT; R-coefficients -2, 4, 1; random two-jet checks of V = d ln rho, R = -calT - 2 div V, E_s identity, sqrt(G) = rho^2 and the ledger identity for rho^2 X.
- s2_twisted_cone_constant.py: Bessel-sum check of C(n,a) and the first-order holonomy shift.
- s3_dragging_regularity.py: joint versus pure Lie derivative, invariant subspace, family invariance (Euclid and Lorentz), finite rotation, regularity, slice leaving.
- s4_mode_split_of_X.py: mode ratios 1/3 : 2/3 : 1 and -1/4; pair cross terms of the mode-null remainder.
- s5_noether_frame_charge.py (slow, minutes): J = dQ - E e xi at random fields; flat-frame boost check of e L_xi e = nabla xi.
- s6_cone_cross_term_nonlocal.py: b of the cone family and the identity int b.beta = (n-1) int Omega ln(L/r).
- s7_lambda2_bookkeeping.py: table of residues, Dirac shift assertion, per-sector cutoffs, Noether presentations.
- s8_local_lorentz_null_direction.py (about 1 min): TEGR null direction at 70 digits.
- compile_check.out.txt: scratch compile summary.

## Decisions Taken
- Treated the Noether coefficient as a presentation family instead of selecting a value: choosing r = -4 or any other value to match c_T would be matching by fiat (task rule). The block states c_W(r) and which r would match, and that no replica data supplies it.
- Used the first-order additive rule only where the ledger already uses it, and said so; did not compute the exact singular-cone spectrum (it would require an unverified index formula).
- Excluded the hybrid "replica contact + Wald presentation" sum: they are two descriptions of one quantity (S_BH = S_ent - Q), so adding them would double count.
- Kept the block to one paragraph with tabular; no status text beyond the closing line; no \ref.
- Declined to rely on the scout's attribution to Mohd, and on Hammad et al. and Ding-Zhai beyond the abstract (not cited in the block).

## Milestone assessment
Routine (bounded obstruction with a reproducible presentation-dependence statement). No MILESTONE.md trigger is claimed. Breakthrough self-assessment: none; the residue is not removed. The structurally useful items for the gatekeeper's assessment are the Lie-dragging diagnosis and the canonical Lorentz-violating class of X, which relocate the missing ingredient to the local-frame-rotation question (Problem D), but they are conditional and derive nothing about the matrix state.

## Status-label recommendation
None. B and A remain OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. Critical-path set per Chapter 17: A, B, C, D1, E, F, G-derived, N (H, I, J optional); no change.

## Author decision needed
None.

## Remaining open step
To close B at order Lambda^2 one needs a derivation, from the matrix theory, of the replica (state, holonomy, continuation in n) and of the entropy of the first-derivative frame term. Ranked open avenues (the orchestrator may queue them):
1. Problem D link. The residue 4 kappa_X is carried entirely by the canonical Lorentz-violating class [X] of the induced density (nonzero for kappa_X != 0, zero at n_D = 2, N_s = 6 where kappa_X = N_tot = 0). Decide whether the matrix theory (Lorentz locking, local rotations of the matrix index) forces or suppresses [X]. If the density is made local-frame-rotation invariant, the Noether coefficient is unique and G_T = G_A is automatic for the invariant part (trivially: a metric functional has Einstein quadratic form and Wald coefficient with the same coefficient); if not, the mismatch is a prediction with a calculable Lorentz-violating coefficient.
2. First law with the rigid compensating rotation. Hamiltonian H_xi + J_lambda, non-exact charge of the global rotation; parity suggests its first-order contribution on a symmetric diamond vanishes for odd modes; second order and even modes not examined. This decides whether the bulk piece can carry the 4 kappa_X.
3. Replica from the modular flow (Problem A): alpha_v, the n > 1 branch, analytic continuation, the Dirac extension (componentwise-regular domain gives a first-order Dirac holonomy term for odd n, not computed).
4. Exact spectrum of the singular Poisson cone with the first-derivative term and the holonomy (non-additive, irrational first-order coefficient expected); test of the additive rule.
5. Constraint-term charge for the composite connection (scout B-R3): at this order b-bar = 0 on the constant background, so the charge starts at first order in the amplitude and is odd; compute and show it vanishes or enters.
6. Fermion and edge-mode contacts at order Lambda^2 (Donnelly-Wall type) and the second circulation in Theta^34 with a regular Sigma metric.

## Special instructions for the gatekeeper
- The block must not be read as G_T != G_A in general: it is a statement at the 031 hypotheses and the first-order additive rule. It does not say that the Noether entropy of rho^2 X is zero; it says the pure-diffeomorphism charge vanishes on Sigma and that the coefficient is presentation dependent because the frame is not Lie-dragged.
- Re-check: (i) C(n,a) and the sign sigma of the holonomy contact; (ii) the table arithmetic from c_A, c_T (inputs from the ledger, L189 and L177); (iii) the identity R = -calT - 2 div V and that c_W - c_T = kappa_X (r+4); (iv) that "r = -4 is the only value zero for every content" is meant at kappa_X != 0; (v) the Iyer-Wald paraphrase (Y linear in L_xi phi, drops for stationary fields).
- The Dirac holonomy zero uses the less singular extension of the ledger; with the componentwise-regular domain the statement is not made.
- The Einstein-aether analogy is structural only; the block does not claim the entropy is unidentified for NAMCG, only that this derivation does not fix it.
- Scratch compile copy is in the session scratchpad, outside the repository.
