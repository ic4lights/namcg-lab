# Proposal 048-fibre-resolved-two-point, round 2

This round applies the gatekeeper's replacements and aligns the record with them. It adds no new research and no new claims. The only new computations are checks of statements that `review-r1.md` required or stated.

## Result

Everything below sits in the frozen 045-047 class. It is conditional, and it closes nothing.

1. **Fibre-point forms (exact).** For any amplitude with q.alpha = 0:
   - X_n = m^-4 q^2 (v.v)(alpha.alpha);
   - SC_n = -(1/24) m^-4 q^2 [(v.v)(alpha.alpha) + 2 (alpha.v)^2].

   Averaged over the fibre, these give IX2 and SC2 on all nine D, polynomial in the amplitude c. As an algebraic statement, 1/x comes from dividing by hbar.hbar. L_2 vanishes on all nine D at gauge zero, which sharpens the merged "on the five". **This denominator reading supersedes the avenue text of the 047 review and ledger entry that said 1/x "comes from restricting to level one".** That text is in a review and the ledger, not in the manuscript, so no manuscript edit follows.

2. **Published form checked, not just read.** IX2 = (q^2/15m^4)(trG delta_ij + 2G_ij) c_i.c_j equals the bracket of Eq. (4.41) of 2601.08031 up to the exact term l^2 k^2 (4 delta_ij - 2 qhat qhat). The 1/3, 1/5 and 3/5 are moments of one fibre function, cos^2 theta, against the weights 1, n_perp^2 and n_par^2. That is a concrete reading of the paper's own unresolved "1/3 vs 1/5". Overall normalisations are not compared.

3. **R1, helicity +-2 with the tree form (exact for these forms).** S_L = c.c Z (q0^2 - k^2)(q0^2 - w^2). The massless root has the healthy sign. The extra root has the opposite sign, in both c and hbar, wherever w^2 >= 0.
   - This is a bounded obstruction bearing on N, not a proof of a propagating ghost.
   - At the extra root the one-loop term equals minus the tree term for every k, so the question turns on higher-loop control.
   - v^2 -> 1/5 at large tau means c_T^TT = 4 kappa, one linear condition on the weights. Among equal weights it holds only at V = T. It does not hold for V_i = T_i alone unless T_0 = T_2. In general the limit is kappa/(c_T^TT + kappa).

4. **R2, static channel: the scout's sign claim fails as stated at late times, and the finite-tau sign is not fixed.** The helicity-0 eigenvalue is indeed negative and of size sinh^2 tau at late times (confirmed exactly). But the source does not act on that polarisation alone. At late times the level-one static response has the sign of c_T^TT, for every weight (ratio 10 c_T^TT/(5V_0 + 4(V_1-T_1) + 4T_2) > 0 under S1).

   **Correction of round 1.** Round 1 said a sign change "survives only at intermediate tau" and gave one interval. That was incomplete. For **V_i = T_i = T** and S1 the ratio is 2(s^4 - 10 s^2 + 4)/((s^2 - 4)(3 s^2 - 2)), with s^2 = sinh^2 tau. It is negative on **two** intervals:
   - 5 - sqrt 21 < s^2 < 2/3;
   - 4 < s^2 < 5 + sqrt 21.

   It is positive on the other three intervals of s^2 > 0 and tends to 2/3. The formula does not extend to V_i = T_i in general: with T_0 = 1, T_1 = T_2 = 2 at s^2 = 100 the value is 37677/53452, against 2251/3576 from the formula.

5. **All-harmonic elimination at equal weights (the gatekeeper's first avenue, tested in one regime).** The induced form is a multiplication operator on the fibre, so elimination is pointwise. For V = T with the coupling S1, the static dust response and the TT pole have **one coefficient T/2, attractive sign, for every q with q.u = 0, every base point and every tau, with no principal value**. The level-one mismatch of 2/3 is a truncation effect in this reading.
   - The one-coefficient value is -64 pi^2 m^6 (T^m.T^m - (1/2)(trT^m)^2)/(c q^2), and X_3.X_3 - (tr X_3)^2 = T^m.T^m - (1/2)(trT^m)^2 = rho0^2/2. Here X_3 is the projection of X on the three-space orthogonal to q.
   - The ratio of the two potentials, read in hhat, is g(tau) -> 1.
   - The result depends on three unproved inputs: V = T, equal weights and S1.

6. **The new sharp fork is the matter coupling.** The literal Poisson-limit coupling S2 (rigid K mass) gives response 4g(tau) times the one-coefficient value at c = c^TT. Read in hbar, the variable to which S2 couples, the second potential vanishes and the ratio is 0. In hhat the same solution has ratio 1, and the sum of the two potentials is the same in both readings. On the mass shell, S1 and S2 differ exactly by a mass dependence M^2 proportional to rho/sqrt|g|. So the value 1 of the ratio, read in the variable the source couples to, hangs on how K masses respond to the dilaton. That is a concrete, computable form of Problem C's matter-coupling step.

Not established: any value of G_eff, a Cassini bound, a statement about ghosts for the emergent metric, one coefficient off shell or beyond dust.

## Target and status

| Problem | appH label (verbatim, re-read this round) | Original target | Classification here |
|---|---|---|---|
| F (L1366-1369) | "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion." | Ch.17 item: A, B, C and sign/scheme of G_eff computed from specified operators | PROGRAMME-CONDITIONAL |
| N (L2827-2828) | "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL." | No propagating Ostrogradsky ghost for p < L_UV in the derived two-point function, with the region stated | PROGRAMME-CONDITIONAL |
| C (L404-407) | "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. A scalar-tensor result is a reduced-scope outcome only when its operator, coupling and phenomenological test are supplied; it does not by itself meet the matrix-derived criterion." | Scalar operator, coupling, Cassini comparison; Assumption gap-psi discharged | PROGRAMME-CONDITIONAL |

- **Dependencies:** the 045-047 paragraphs (setting, weights V_i, T_i, B_i), plus supplied IKKT content.
- **Critical-path set re-derived from Ch.17 L690-749:** A, B, C, D1, E, F, G-derived, N. This matches CLAUDE.md, with no discrepancy.

## Source reading

**Digest + targeted reads. This is not a full scan.**

- **Digest status:** `make_digest.py --check` printed `DIGEST STALE (head changed)`, with `dirty-chapters: yes`. The digest head is ff2f286 and HEAD is 9418f47; the only difference between them is `review-r1.md`. I recomputed the digest's 30 stored file hashes against the working tree and found no mismatches, so the staleness is the HEAD move alone. I did not regenerate the digest, because that writes outside the proposal folder.
- **Rule to flag:** CLAUDE.md protocol item 3(d) literally asks for a full scan when the digest is stale or `dirty-chapters: yes`. I did not do one. This round adds no new claim and changes no definition, assumption, scope or status passage, and the gatekeeper ruled in review-r1 that none is required for this package. The orchestrator has stated that the dirty flag comes solely from the accepted 046 and 047 integrations. Please confirm that ruling still covers r2.
- **Read in full this round:** review-r1.md, proposal-r1.md, appH_insert.tex, s3, s5, compile_check.py and their saved outputs.
- **Read in part this round:** appH L404-407, L1366-1369, L2827-2828 (labels); ch17 L690-749 (filtered to the problem items, not read line by line); s4 L160-171.
- **Carried from round 1, not re-read:** the other passages listed in proposal-r1.md.
- **Unreadable:** none.
- **Process notes:**
  - My first tool round batched read-only calls, against the sequential rule. Nothing changed; later calls were serial.
  - The permission system denied one combined Bash command (patch s5, run it, test a copy, remove the copy with `rm -rf`). I reran the steps as separate commands without the removal, so working files stay in the session scratchpad (`s5copy/`, `patch_s5.py`, `s3_tail.txt`, `patch_r2.py`). Nothing outside the proposal folder and the scratchpad was written.

## Research and reasoning

### How each review finding was addressed

| Finding | Severity | Addressed by |
|---|---|---|
| 1, three-space calibration and "same source" | major | R1-R5 in the insert; Results 5, 6; section D below; s3 R2.1 |
| 2, variable behind "potential ratio 0" | major | R9-R12 in the insert; Results 5, 6; sections E, F; O2; s3 R2.5 |
| 3, omitted negative interval; V_i = T_i = T | major | R6, R7 in the insert; Result 4; classification row; s3 R2.2, R2.3 |
| 4, "needs these weights" | minor | R8 in the insert; Result 3; s3 R2.4 |
| 5, mirage sentence | minor | R13-R15 in the insert; section G |
| 6, on-shell condition | minor | R12 in the insert; Result 6; section F |
| 7, notation (T, A) | minor | R16-R21 in the insert; T^m used below |
| 8, "as a square root" | minor | Verification caveat below; s6 |

I disagree with no finding. One reading is made explicit: the two regulator forms of check 5 hold for the deficit of 4 I, not of I (see the caveat under Verification scripts).

### Conventions

- q = (q0,0,0,k), lower index, at y^i = 0.
- a = m^2 q0^2 + l^2 k^2, b = m^2 (q0^2 - k^2), sinh^2 tau = m^2/l^2, theta = 1 + l^2/m^2.
- **Amplitude convention:** phase average of a real wave throughout. A^a = alpha^a cos u, delta E = alpha v sin u. This is the insert's "for a real wave averaged over its phase", not the unit amplitude of delta T_0 that 047 used for Q_i. No Q_i is used here.
- **Notation changed in round 2:** T^m is the stress and T the weight. A is (V+2T)/24, and SC2 is written with DG explicitly.

### A. Fibre-point forms

Since q.alpha = q.v = 0, h_n = m(alpha v + v alpha) has q.h_n = 0. Then:
- EH2 reduces to -(q^2/8m^6)(h.h - t^2) with t = 2m alpha.v, and the dilaton term gives q^2 t^2/(32 m^6);
- this yields SC_n, and X_n is the merged index density;
- the fourth fibre moment gives IX2, SC2.

Checks:
- pointwise at 5 cases x 4 fibre points;
- averages at 9 cases, including q0 = 0;
- gauge independence, all with exact residual zero (s1);
- s5(A) confirms that for transverse h, EH(h - (1/2) eta t) = -(q^2/8m^6)(h.h - t^2/2) exactly. So at V = T the pointwise form is the Einstein-Hilbert form of the trace-reversed variable.

### B. Helicity +-2

- c(x) = c_T^TT + kappa/x (scout's formula, verified symbolically);
- hbar.hbar = (4m^2/9) a c.c;
- tree (rho_M/4g^2) m^2 q^2 c.c/3.

Hence the factorised S_L with Z, v^2, mu^2 of the insert (s2 A-C). The scout's v^2 formula is **correct**. Form checks of IX2, SC2 and EH on helicity 2 by direct cp12_forms pass at four cases (s2 D).

**The value 1/5.** With c_T^TT - 4 kappa = V_0/6 + T_0/12 + (V_1-T_1)/30 - T_2/4, the value 1/5 is one linear condition. At equal weights the expression is (V - T)/5, so it forces V = T. At V_i = T_i it is (T_0 - T_2)/4 (s3 R2.4).

**Sign of the tree relative to the induced term.** Both are positive in S_E in the formal evaluation. The published (4.44) has the same relative sign: its factor (d0^2 - d^2/5 - m^2) is -(q0^2 - k^2/5 + m^2) in Fourier space (s1 P3b), the factor printed in (4.46).

**Quartic lemma.** For any real quadratic in q0^2 with distinct real roots, the two coefficients have opposite signs. So V00, V01 cannot remove the sign unless they make the roots complex. They do shift the near-null root by (V00 + V01 k^2)/(k^2 - w^2).

### C. Level-one static block

D = diag(d_perp, d_perp, d_q). All forms are symbolic in l, m, k (s3), with F_qq, F_qp, F_pp printed for general weights. L1 + L2 = SC2 - SC1 is exact and L2 = 0. Solving gives the ratios quoted. Every ratio is to the one-coefficient value, for S1 and for S2 alike; it is not a ratio to the response of the form c EH to that same source.

Signs of the S1 ratio at V_i = T_i = T, from exact roots (s3 R2.2):

| s^2 interval | sign |
|---|---|
| (0, 5 - sqrt 21) | + |
| (5 - sqrt 21, 2/3) | - |
| (2/3, 4) | + |
| (4, 5 + sqrt 21) | - |
| (5 + sqrt 21, infinity) | + |

Exact samples are -6/7 at s^2 = 1/2 and -134/55 at s^2 = 9/16.

Helicity-0 eigenvalues at (5,3): -67/72 and 2063/8640, matching the printed closed form and the scout's values exactly (s1 P5).

### D. All-harmonic response

alpha(n) is free at each n, modulo gauge gamma(n) q, so:
- Q_n = C[(v.v) 1 + (B/A) v v];
- Q_n^-1 follows by the Sherman-Morrison identity, tested exactly (s4 A);
- on the null cone v lies in a 2-plane with a uniform angle, so I = (1/4)(1 + rho) X.X.

For dust, X = rho0(uu + eta/2) has X eta^-1 X = (1/4) rho0^2 eta (exact, including boosted u), so the numerator cancels v.v.

**Calibration (corrected in round 2).** On transverse hbar the elimination uses the projection X_3 of X on the three-space orthogonal to q. The one-coefficient form gives -64 pi^2 m^6 (X_3.X_3 - (tr X_3)^2)/(c q^2). For T^m on that three-space and X_3 = T^m - (1/2) eta_3 trT^m, the identity X_3.X_3 - (tr X_3)^2 = T^m.T^m - (1/2)(trT^m)^2 holds for any symmetric T^m, and the dust value is rho0^2/2 (s3 R2.1, residual 0).

Round 1's form with the four-dimensional X gives X.X = rho0^2, tr_3 X = rho0/2 and a difference of (3/4) rho0^2, so it was false as printed. With X = T^m (S2) that form gives 0, so it cannot serve as the reference for S2. With the corrected form, -32 pi^2 m^6 I/(q^2 A) at I = rho0^2/4 and A = T/8 equals the one-coefficient value at c = T/2 (residual 0). The coefficient c = T/2 therefore stands.

Galerkin truncation in odd J <= N (s4 D):
- reproduces the level-one values at N = 1 (c_1/A = 24/5, ratios 0.66631 and 2.66684 against s3);
- on the null cone tends to 8/(1+rho);
- in the static channel, with regulator eps, converges to the regulated N = infinity value, and the regulated value tends to the eps -> 0 value (s4 G).

### E. Potentials

- rho = 1, S1: hbar^00 proportional to f/2, hbar^11 proportional to -(1+f)/4, f = -g. Trace reversal gives hhat^00 = -1/4 (constant) and hhat^11 = -g/4. So the ratio read in hhat, the variable to which S1 couples, is g.
- The hhat^33 entry differs from hhat^11 by a term along qhat qhat, removable by the static gauge xi along qhat.
- Quadrature confirms this (s4 G).
- General rho: K(tau) closed by finite parts, against the regulator (s5 B); the ratio tends to 1 numerically at rho = 0.75, 1.25 (s5 C). The s5 (C) values above 1 are regulator noise. The gatekeeper's parameter-differentiated finite parts tend to 1 from below (0.99967, 0.99988 at s^2 = 1e4; review-r1 check 5, not recomputed by me).
- S2 at V = T: hbar^00 = H and hbar^ab = 0 on the two directions orthogonal to q and u. So hbar^11/hbar^00 = 0, hhat^11/hhat^00 = 1 and the sum hbar^00 + hbar^11 = hhat^00 + hhat^11 (s3 R2.5). The fork is real only with the reading "potentials in the variable the source couples to". The two gamma-like values are then g for S1 and 0 for S2.

### F. S1 versus S2

For S_E = (1/2) rho_M (gamma dphi dphi + M^2 phi^2) the source of hbar is dphi dphi. For dust at rest that is T^m_00 only (S2). With M^2 e^{2 delta phi}, where delta phi = t/(4 m^2) (the merged phi = (1/2) ln(rho/sqrt|g|)), the source becomes (1/2) rho_M [dphi dphi + M^2 phi^2 eta/(2m^2)].

**On the mass shell,** M^2 <phi^2>/m^2 = <phi_dot^2>, so X = rho0(uu + eta/2) for dust, and X = T^m - (1/2) eta trT^m for any free massive mode. This is hand algebra, re-derived by the gatekeeper (review-r1 check 6) and recorded rather than symbol-checked. Its independent reading: hhat = delta(e^{-2 phi} gamma), so S1 is a rigid mass in the frame with cometric e^{-2 phi} gamma, which is the G of (3.9). S1 stays an input: the insert says "not derived".

### G. Literature

Downloaded arXiv source and PDF of 2601.08031 (TeX sha256 233dc123..., PDF 56cc0783...; kept outside the repo).

**Confirmed verbatim from TeX, equation numbers from the PDF text (the gatekeeper's own confirmations are listed in review-r1 check 7):**
- (3.1), (3.9), (3.12), (3.25), (3.37);
- (4.33) [F F]_0 = (2/3) A Box A;
- (4.41), (4.42) (the printed (4.42) has a typo, t in place of u, in one term);
- (4.43)-(4.46), m^2 = 32 pi G_N alpha^2 r^-4;
- Box-tilde ~ d0^2 - (1/3) d_i d^i;
- "all hs contributions were ignored";
- "There is no issue with ghost-like signatures in the action, since the extra modes arises only after quantization, and only affect the background geometry";
- "the geometric treatment in section 3 does not fully capture the hs sector".

**Correction to the reading of (3.25).** Equation (3.25) prints the factor (1 - m^2 tilde-Box^-1). The quotient tilde-Box/(tilde-Box - m^2) is its inverse. The insert now says the fibre-resolved factor "has the structure of" tilde-Box/(tilde-Box - varpi/m^2), that the mass of the inverse factor is read as varpi/m^2, and that this normalisation is not compared.

**Scout's readings:** all those I used are confirmed. The velocity statements (c/3 for extra modes in Sec. 3) are confirmed for 2601 only.

**Not independently verified / not used:** 2609.08955, 1910.00839, 2312.01317, 2405.09804 (scout's reading only, not cited in the insert). The appendix values of V00, V01 were seen but not derived. KumarSteinacker2023 is cited only to say it is not compared. No new bib entry is needed.

**What is not claimed about 2601.** I do not present any of this as an obstruction to the published theory and do not cite it as deriving a single G on polarisations. The surviving differences are:
- (i) the mirage correction sign at k above crossover: fibre-resolved 1 - varpi/(mk)^2 against 1 + 3 varpi/(mk)^2. The algebra (review-r1 ruling on item 6) is factor = 1 + sigma PV int dc/(c^2 - sigma) = 1 - sigma + ..., against 1/(1 - 3 sigma); both tend to -1/(3 sigma) as k -> 0. Exact hypotheses: V = T, S1, equal weights, q.y = 0, large tau, principal value, fibre Laplacian dropped. It could be an artefact of the frozen symbol or of the equal-weight trace, because the sign comes from the resonance near v.v = -varpi, where the fibre Laplacian is largest. The paper itself says the hs parts were ignored there, so no conclusion on that work is drawn.
- (ii) the residue signs: a property of the form. The paper's "no issue" sentence is a statement about quantization that I neither derive nor refute.

### Hypotheses and forks (per the author directive)

Adopted from review-r1. **None of these classes closes a direction outside its hypotheses.**

- **O1, opposite sign at the extra root.** Frozen symbol; leading-symbol tree dropping non-derivative terms and the fibre Laplacian; one-loop truncation; formal continuation; helicity +-2 or alpha.alpha > 0 pointwise; w^2 >= 0 for the hbar reading.
- **O2, ratio 0 in hbar.** Rigid K mass; V = T; equal weights; q.y = 0.
- **O3, no single coefficient off shell or beyond dust.** Equal weights at V = T.

What each relaxation gave for O1:

| Relaxation | Explored here | Result |
|---|---|---|
| Other weights | yes | Sign independent of V_i, T_i given c_T^TT, c_T^TT + kappa > 0 |
| All harmonics | yes, equal weights | Becomes a continuum; sign stays on alpha.alpha > 0; polarisation alpha.alpha < 0 has the opposite sign |
| Non-derivative terms | yes, as a lemma | Real roots keep opposite signs; a complex pair needs a negative discriminant; near-null root shifts |
| Change of variable c to hbar | yes | Same sign for w^2 >= 0 |
| Source channel | yes | Static dust at rho = 1 and varpi = 0 has a response with no singular denominator; this does not remove the state |
| Higher loops / large number of K modes | no | Open, avenue 2 |
| Fibre Laplacian and cross term | no | Open, avenues 2 and 3; they can split the continuum and may matter at the resonance |
| Inert and trace at w | partly | Pointwise form covers them at equal weights |

For O2 the relaxation is the K-scale response to the dilaton (avenue 1, not computed). For O3 the relaxations are non-equal weights and torsion orders. They are not ranked as a separate avenue, because this class criterion is the one the scout advises not to narrow further.

The ranked list of open avenues is under "Remaining open step".

### Rulings adopted from review-r1

- **Equal weights:** stated as a hypothesis in the opening sentence of the block and again as "an assumption" in the scope paragraph. Nothing reads as a derivation of Newtonian gravity.
- **Extra root:** not claimed as a state. It is a bounded obstruction bearing on N, and whether it is a state "depends on the control of higher loops". N's target concerns the emergent graviton two-point function, which the insert disclaims.
- **Mirage sentence:** kept, scoped by R13-R15.
- **Merged claims:** none is false, so there is no PRIOR-CLAIM-ERROR. c_T^TT at level one stands; "L_2 vanishes on the five" is sharpened, not contradicted; the inert-elimination sentence at L2448 concerns level-one inert amplitudes, not higher harmonics; the phase-average convention matches L2398.
- **Ledger note (for the integrator; I do not edit the ledger):** the 047 avenue text on 1/x is superseded by the denominator reading.
- **L2092:** stays true as scoped. No edit and no full scan on its account.
- **Labels and emergence:** labels unchanged, one scoped closing status sentence. hbar, hhat, h_n are composites and are disclaimed against the emergent metric. No process language.
- **Split:** none needed. Results 1-6 share the pointwise form and the same source updates.

## Claim classification

| Claim | Class |
|---|---|
| X_n, SC_n, IX2, SC2 on nine D; L_2 = 0 at gauge zero; EH of trace-reversed variable | established (exact, frozen symbol) |
| Dictionary with (4.41), moments 1/3, 1/5, 3/5 | established algebra; identification with the published amplitude is a structural comparison, normalisation not compared |
| S_L factorisation, Z, v^2, mu^2, sign of coefficients | established for these forms; conditional on formal continuation and leading symbol |
| v^2 -> 1/5 | established: holds iff c_T^TT = 4 kappa; among equal weights only at V = T |
| Extra root is a propagating ghost | **not claimed**; unresolved (higher-loop control) |
| Quartic lemma | established |
| Level-one static ratios | established for these forms, by exact symbolic closed forms; conditional on source S1 or S2 |
| **Level-one sign (corrected)** | Established for these forms. Late-time ratio 10 c_T^TT/(5V_0 + 4(V_1-T_1) + 4T_2) > 0 under S1 and four times it under S2, at fixed weights. At V_i = T_i = T under S1 only: negative on 5 - sqrt 21 < s^2 < 2/3 and on 4 < s^2 < 5 + sqrt 21, positive otherwise, tending to 2/3. The closed formula does not hold for V_i = T_i with unequal T_i. Conditional on S1 as an input |
| Equal-weight pointwise elimination | conditional (weight independent of external harmonic order: assumption outside M above the levels) |
| Null TT coefficient 8A/(1+rho) | conditional as above; exact within it; numeric truncation check |
| X_3.X_3 - (tr X_3)^2 = T^m.T^m - (1/2)(trT^m)^2 = rho0^2/2 | established identity (for T^m on the three-space orthogonal to q) |
| Dust I = rho0^2/4 at V = T, S1, every q with q.u = 0; c = T/2 = c^TT with attractive sign | conditional on equal weights, V = T, S1; exact within it |
| g(tau) -> 1 as the ratio read in hhat; K(tau) | conditional; principal or finite-part prescription; numeric checks |
| V != T large-tau statements | conditional, wider: finite part; numerics at two rho |
| S2: response 4g(tau) times the one-coefficient value; ratio 0 read in hbar, 1 in hhat | conditional on S2, rigid K mass, V = T, equal weights, q.y = 0 |
| S1 as matter coupling; V = T; equal weights above J = 1; rho_M and g; formal continuation | **inputs**, not derived |
| S1 from M^2 proportional to rho/sqrt|g|, on the mass shell | conditional hand algebra; dependence not derived |
| Mirage sign difference | conditional, on the principal value and on dropping the fibre Laplacian; possibly an artefact; no conclusion on that work |
| Fibre Laplacian needs varpi >> 1 | scale estimate |

**Open:** C, F, N remain OPEN and PROGRAMME-CONDITIONAL. Nothing is DERIVED.

## Proposed changes

**File `chapters/appH-microscopic-proofs.tex`.** One insertion, no replacement.

- **Anchor:** immediately before the line `\section{Problem G: HBEV}` (occurs once, s5 E, re-run this round), so after the 047 closing sentence "...Problems~B and~F remain open and PROGRAMME-CONDITIONAL."
- **Kept:** everything. Nothing is removed.
- **Text:** `proposals/048-fibre-resolved-two-point/appH_insert.tex`, byte-exact, **16390 bytes, sha256 6124496b4d016b93ba3fa385e93eddd30b9347e63e491119869e092d7988804f**, ASCII, LF, no BOM. The integrator restores CRLF. This file is the `latex` block; it is not duplicated here, so there is one source of truth.
- **Change from round 1:** exactly R1-R21 of review-r1.md, applied in sequence by `apply_r2_replacements.py` from raw review text. Each old string occurred exactly once, both in the round-1 text and at its turn. The count equals the review's 16390. The round-1 text is kept as `appH_insert.r1.tex` (15572 bytes, sha256 6ec4f657...).
- **Labels verified:** `ch:vierbein-emergence` (1), `ass:lorentzian` (1).
- **Cites verified:** `Steinacker2026`, `KumarSteinacker2023`. No new labels and no bib change.

**appH L2092, "These results have not been checked against the present operators."** No edit proposed. As ruled in review-r1, the sentence stays true as scoped: its "present operators" are G, K of that D-coordinate paragraph. This package compares the level-one forms on CP^{1,2} x K with the named equations only.

**Stale passages elsewhere:** none. The 047 sentence "the trace polarisation or a Newtonian limit" states what that paragraph did not compute, and it remains true of that paragraph. Likewise the merged "L_2 vanishes on the five" stays true and is sharpened, not contradicted.

## Verification scripts

All are in `proposals/048-fibre-resolved-two-point/`. Except for `apply_r2_replacements.py`, all print to stdout and write nothing; compile_check builds and removes its own scratch copy outside the repo. Round-1 outputs `*.out.txt` are kept unchanged, and round-2 outputs are the new `*.r2.out.txt`. The scripts import `../046-fibre-regime-interpolation/forms_lib.py` read-only.

| Script | Round 2 status | Checked | Result |
|---|---|---|---|
| apply_r2_replacements.py | new | Applies R1-R21 from raw review text; refuses on input sha, parse, count, ASCII, CR, BOM or size mismatch; `--check` never writes | All 21 old strings occur once; 16390 characters; output in `apply_r2_replacements.r2.out.txt` |
| s1_pointwise_forms.py | unchanged, not re-run | P1 pointwise, P2 averages (9 cases), P3 dictionary, P3b Fourier sign, P4 moments, P5 helicity-0 values | all residuals exact zero; scout's helicity-0 values reproduce |
| s2_helicity_two_poles.py | unchanged, not re-run | c(x), factorisation, v^2, mu^2, residues, four direct form checks, quartic lemma | zero residuals |
| s3_static_level_one.py | docstring reworded; section R2 appended | static block forms, sources, ratios, general weight limit; **R2.1** calibration; **R2.2** negative intervals as roots; **R2.3** V_i = T_i counterexample; **R2.4** 1/5 condition; **R2.5** readings of the ratio | The round-1 output is an exact prefix of the r2 output. R2.1 residuals 0, values rho0^2/2, (3/4) rho0^2 and 0. R2.2 negative set equals the corrected union (exact). R2.3 37677/53452 against 2251/3576. R2.4, R2.5 as stated |
| s4_all_harmonic_response.py | unchanged, not re-run | pointwise inverse, null TT, g(tau) closed against numeric PV, Galerkin N up to 513, crossover, h(x), regulator sequence, stress entries, potentials | agree; regulator trends stated, finite-eps values differ as expected |
| s5_finite_part_and_mechanics.py | part E made robust; re-run | EH of trace-reversed variable, K(tau), general-rho potentials, S1-S2 note, insert mechanics | Only the byte count differs from round 1 (16390 vs 15572). ASCII True, CR 0, BOM False, anchor 1, labels 1, cites 1, new labels none, one status sentence, 9 paragraphs, process scan empty |
| s6_regulator_deficit.py | new | the two regulator forms of review-r1 check 5 | see caveat below |
| compile_check.py | unchanged; re-run on the new bytes | build with and without the insert, outside the repo | exit [0,0,0,0] both; 329 and 333 pages; 0 undefined refs and citations; 0 multiply defined; scratch removed. Output in `compile_check.r2.out.txt`, same text as round 1. Rendered pages not inspected |

**s3 zero and pole reporting.** The printed zero and pole lists were already correct, and no printed label repeated a corrected claim. Only the docstring's "the same source" did, so that was reworded. R2.2 adds the sign table and the point s^2 = 1/2 that the grid omitted.

**s5 part E.** It now finds the manuscript through `NAMCG_REPO` or the nearest ancestor holding the sources. If none is found it prints an explicit `SKIPPED` line for the anchor, label and cite counts, and still runs the insert-only checks. Tested from a copy outside the repo, with and without `NAMCG_REPO`: exit 0 both ways.

**Caveats.**
- s3 prints a "Solution direction" gamma at level one, s^2(s^2-4)/(s^4-10s^2+4), which is not quoted in the insert.
- The regulated static values at eps = 0.02 are visibly below the eps -> 0 values (0.2107 against 0.25); s4 G shows the trend (0.2492 at eps = 2e-5).
- **Correction of round 1.** Round 1 said convergence in eps is slow "as a square root". That holds only for eps >> c0^2; below that the deficit is linear. With s6 at s^2 = 1e4 (c0^2 about 1e-4), 4(1/4 - I_eps) follows sqrt(eps) pi/(2 sqrt 2) at eps = 0.02 (0.15733 against 0.15708) and pi eps/(2 c0 theta) at eps = 2e-6 (0.00031 against 0.00031). Neither form fits near the crossover, at eps = 2e-4. **These forms are for the deficit of 4 I; for I itself each carries a factor 1/4.** Review-r1 check 5 does not state the normalisation, and s6 settles it. The sequence continues to 0.2499921 at eps = 2e-7, the review's value. The 0.2492 at eps = 2e-5 is therefore a regulator effect. This is not in the insert.

## Decisions Taken

Round 1 decisions stand:
1. **Target:** R1 + R2 + equal-weight all-harmonic elimination, rather than R1 alone or D1.
2. **Scout's sign claim:** reported as failing in the source channel at late times, with its eigenvalue arithmetic confirmed. Round 2 corrects the finite-tau statement.
3. **Matter coupling:** record both S1 and S2 rather than choose one. No coupling is derived, and choosing S1 alone would hide O2. Favouring the derivation means pointing at the exact missing input, not assuming it.
4. **L2092:** no edit.
5. **Variables:** the two-point function is presented in the amplitude c, the matrix variable, with hbar derived. The metric stays composite throughout, and nothing makes a metric fundamental.
6. **Fibre-resolved "metric" language:** h_n is a form variable, disclaimed against the emergent metric.

Round 2 decisions (routine, none affects a label):
7. **R1-R21 taken verbatim,** with no rewording. s3 section R2 checks the calibration behind R1-R5, the statements of R6-R8 and the readings in R10; I checked R21 by hand (tr AA^T = tr DG^2D^T, tr A^2 = tr DGDG). The other replacements are wording and notation, taken on the review's checks.
8. **Round-1 insert kept** as `appH_insert.r1.tex`, so the replacement script can be re-run and nothing is overwritten silently. The integrator must use `appH_insert.tex`.
9. **s3 extended in place,** keeping the round-1 output as an exact prefix, rather than a separate script that would duplicate its setup.
10. **Replica numbers dropped.** Round 1's "Remaining open step" quoted two mixed-gap values not in the insert. I did not re-check them this round, so the avenue is recorded without them.

No RESEARCHER-DECISION flag was raised in review-r1.

## Milestone assessment

**Routine.** The gatekeeper's r1 assessment is MILESTONE: none (conditional result, not a breakthrough, by the same standard as 044-047), and this round adds nothing that would change it. A real breakthrough would need V = T for a constructed K, S1 derived from the K-scale response, and equal weights justified.

## Status-label recommendation

Critical-path list from Ch.17 and appH: A, B, C, D1, E, F, G-derived, N. Affected labels: none. C, F, N stay OPEN, CRITICAL PATH (for N: "for the matrix-derived label"), PROGRAMME-CONDITIONAL.

## Author decision needed

None. Advice carried from the scout, no action required: whether B's tensor block is to be judged on all five off-shell polarisations or on the on-shell sector plus source channels. Results 3-6 bear on that but change no label.

## Remaining open step

To close F, N, C in this class the following are still needed. This is the ranked avenue list adopted from review-r1. Each keeps spacetime emergent, and none is the only route.

1. **K-scale response to the dilaton:** is the K mass rigid in the e^{-2 phi} gamma frame? This decides S1 against S2 and is the sharpest computable step for C. A possible form is the one-loop vacuum functional of K (2601 Eq. (3.12) has the form rho^-2 V_0).
2. **Control of the extra root:** higher loops or a large number of K modes, with the fibre Laplacian and cross term kept near the resonance, for N.
3. **Fibre Laplacian retained in the static channel:** decides whether the mirage sign difference and the principal value survive.
4. **Level-dependent weights,** including the external-harmonic vertices above J = 1, away from M above the levels. The singular eliminator needs high J, so this tests the equal-weight hypothesis directly.
5. **V = T:** existence of K with W_R = 0, or the V != T static and TT forms.
6. **Tree non-derivative terms and V00, V01 on level one.**
7. **A fibre-resolved cone for the replica gap at c^TT = T/2.**

D1, A, E and G-derived are untouched by this package.

## Special instructions for the gatekeeper

**Please check:**
- that `appH_insert.tex` differs from `appH_insert.r1.tex` by exactly R1-R21 (`python apply_r2_replacements.py --check`);
- s3 section R2 and s5(E);
- the normalisation note on the regulator forms (s6), which makes explicit a point check 5 left unstated;
- whether the review's no-full-scan ruling still covers r2, given `DIGEST STALE (head changed)` and protocol item 3(d). The stored file hashes all match, and only `review-r1.md` changed between digest head and HEAD.

**Byte note:** the sha256 above is of the working-tree LF bytes. Git warns that LF would become CRLF the next time it touches these files under this checkout's settings. If the insert is committed and checked out again, the hash must be taken after normalising to LF, and `apply_r2_replacements.py` would refuse a CRLF copy rather than guess.

**Not re-verified this round:** s1, s2, s4 (scripts and inputs unchanged); rendered pages; the gatekeeper's finite-part values quoted in section E.

**Must not be asserted:**
- that a ghost exists in NAMCG or in the published model;
- that 1/x is removed off shell (it is replaced by h(x));
- that G_stat = G_TT holds without V = T, S1 and equal weights;
- that the published theory is contradicted;
- that the negative intervals or the closed ratio hold outside V_i = T_i = T;
- that the ratio 0 for S2 holds in hhat;
- any Cassini bound (the number in `s4` is an arithmetic illustration and is not in the insert).

Insert length: 16.4 kB, 9 blocks. Result 5 remains the claim of highest risk.
