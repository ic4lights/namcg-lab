# Proposal 048-fibre-resolved-two-point, round 1

## Result

Everything below sits in the frozen 045-047 class. It is conditional, and it closes nothing.

1. **Fibre-point forms (exact).** For any amplitude with q.alpha = 0:
   - X_n = m^-4 q^2 (v.v)(alpha.alpha);
   - SC_n = -(1/24) m^-4 q^2 [(v.v)(alpha.alpha) + 2 (alpha.v)^2].

   Averaged over the fibre, these give IX2 and SC2 on all nine D, polynomial in the amplitude c. The scout's "1/x is a change-of-variables denominator" holds as an algebraic statement: 1/x comes from dividing by hbar.hbar. L_2 vanishes on all nine D at gauge zero, which is stronger than the merged "on the five".

2. **Published form checked, not just read.** IX2 = (q^2/15m^4)(trG delta_ij + 2G_ij) c_i.c_j equals the bracket of Eq. (4.41) of 2601.08031 up to an exact term l^2 k^2 (4 delta_ij - 2 qhat qhat). The 1/3, 1/5 and 3/5 are moments of one fibre function, cos^2 theta, against the weights 1, n_perp^2 and n_par^2. That is a concrete reading of the paper's own unresolved "1/3 vs 1/5".

3. **R1, helicity +-2 with the tree form (exact for these forms).** S_L = c.c Z (q0^2 - k^2)(q0^2 - w^2). The massless root has the healthy sign. The extra root has the opposite sign, in both c and hbar, wherever w^2 >= 0.
   - This is a bounded obstruction bearing on N, not a proof of a propagating ghost.
   - At the extra root the one-loop term equals minus the tree term for every k, so the question turns on higher-loop control.

4. **R2, static channel: the scout's sign claim fails as stated.** The helicity-0 eigenvalue is indeed negative and of size sinh^2 tau at late times (confirmed exactly). But the source does not act on that polarisation alone. At late times the level-one static response has the sign of c_T^TT, for every weight (ratio 10 c_T^TT/(5V_0 + 4(V_1-T_1) + 4T_2) > 0 under S1). A sign change survives only at intermediate tau: for V_i = T_i the ratio is negative on 4 < sinh^2 tau < 5 + sqrt 21.

5. **All-harmonic elimination at equal weights (the gatekeeper's first avenue, tested in one regime).** The induced form is a multiplication operator on the fibre, so elimination is pointwise. For V = T with the coupling S1, the static dust response and the TT pole have **one coefficient T/2, attractive sign, for every q with q.u = 0, every base point and every tau, with no principal value**. The level-one mismatch of 2/3 is a truncation effect in this reading.
   - The potential ratio is g(tau) -> 1.
   - The result depends on three unproved inputs: V = T, equal weights and S1.

6. **The new sharp fork is the matter coupling.** The literal Poisson-limit coupling S2 (rigid K mass) gives response 4g(tau) and potential ratio 0 at V = T. S1 and S2 differ exactly by a mass dependence M^2 proportional to rho/sqrt|g|. So the value 1 of the potential ratio in this class hangs on how K masses respond to the dilaton. That is a concrete, computable form of Problem C's matter-coupling step.

Not established: any value of G_eff, a Cassini bound, a statement about ghosts for the emergent metric, one coefficient off shell or beyond dust.

## Target and status

| Problem | appH label (verbatim) | Original target | Classification here |
|---|---|---|---|
| F (L1366-1369) | "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN..." | Ch.17 item: A, B, C and sign/scheme of G_eff computed from specified operators | PROGRAMME-CONDITIONAL |
| N (L2827-2828) | "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL." | No propagating Ostrogradsky ghost for p < L_UV in the derived two-point function, with the region stated | PROGRAMME-CONDITIONAL |
| C (L404-407) | "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL..." | Scalar operator, coupling, Cassini comparison; Assumption gap-psi discharged | PROGRAMME-CONDITIONAL |

- **Dependencies:** the 045-047 paragraphs (setting, weights V_i, T_i, B_i), plus supplied IKKT content.
- **Critical-path set re-derived from Ch.17 L690-749:** A, B, C, D1, E, F, G-derived, N. This matches CLAUDE.md, with no discrepancy.
- **Note on appH wording:** ch17 L140 says "CRITICAL PATH; OPEN" for C, consistent with appH L404.

## Source reading

**Digest + targeted reads.** No full scan, and none is required: no definition, assumption, scope or status passage changes.

- `make_digest --check` printed DIGEST CURRENT (`dirty-chapters: yes`, explained by the uncommitted 046/047).
- Working-tree files were read directly.
- **Read in full:** digest; appH L2370-2459 (the 044-047 paragraphs); appH L1362-1401; L2825-2894 (N, part); L2085-2100 (the L2092 passage); L400-420 and L470-512 (C); ch17 L138-170, L395-420, L495-520, L690-749; MILESTONE.md; 047 review-r3; sme-scout-20261101-after45; forms_lib.py; 046 s2; 047 s3.
- **Unreadable:** none.
- **Process slip:** my first tool round batched three read-only calls, against the sequential rule. Nothing changed, and later calls were serial.

**Why this target over the alternatives.** The gatekeeper ranked all-harmonic and inert elimination first; the scout ranked R1 and R2 first and argued the 1/x is a denominator. They turned out not to compete: the cheap lemma (result 1) confirmed the denominator reading, and it also showed the form is pointwise on the fibre. That makes the gatekeeper's avenue doable at equal weights inside the same package, and it changes the answer to R2 (2/3 becomes 1 under S1). So I combined R1, R2 and that case. D1 (R3) stays next in line. It was not chosen because the F/N/C channel had a sharp, verifiable computation available, and that computation also tested a sign claim that would otherwise have steered the programme.

## Research and reasoning

### Conventions

- q = (q0,0,0,k), lower index, at y^i = 0.
- a = m^2 q0^2 + l^2 k^2, b = m^2 (q0^2 - k^2), sinh^2 tau = m^2/l^2, theta = 1 + l^2/m^2.
- **Amplitude convention:** phase average of a real wave throughout. A^a = alpha^a cos u, delta E = alpha v sin u. This is the insert's "for a real wave averaged over its phase", not the unit amplitude of delta T_0 that 047 used for Q_i. No Q_i is used here.

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

**Sign of the tree relative to the induced term.** Both are positive in S_E in the formal evaluation. The published (4.44) has the same relative sign: its factor (d0^2 - d^2/5 - m^2) is -(q0^2 - k^2/5 + m^2) in Fourier space (s1 P3b), the factor printed in (4.46).

**Quartic lemma.** For any real quadratic in q0^2 with distinct real roots, the two coefficients have opposite signs. So V00, V01 cannot remove the sign unless they make the roots complex. They do shift the near-null root by (V00 + V01 k^2)/(k^2 - w^2).

### C. Level-one static block

D = diag(d_perp, d_perp, d_q). All forms are symbolic in l, m, k (s3), with F_qq, F_qp, F_pp printed for general weights. L1 + L2 = SC2 - SC1 is exact and L2 = 0. Solving gives the ratios quoted.

Helicity-0 eigenvalues at (5,3): -67/72 and 2063/8640, matching the printed closed form and the scout's values exactly (s1 P5).

### D. All-harmonic response

alpha(n) is free at each n, modulo gauge gamma(n) q, so:
- Q_n = C[(v.v) 1 + (B/A) v v];
- Q_n^-1 follows by the Sherman-Morrison identity, tested exactly (s4 A);
- on the null cone v lies in a 2-plane with a uniform angle, so I = (1/4)(1 + rho) X.X.

For dust, X = rho0(uu + eta/2) has X eta^-1 X = (1/4) rho0^2 eta (exact, including boosted u), so the numerator cancels v.v.

Galerkin truncation in odd J <= N (s4 D):
- reproduces the level-one values at N = 1 (c_1/A = 24/5, ratios 0.66631 and 2.66684 against s3);
- on the null cone tends to 8/(1+rho);
- in the static channel, with regulator eps, converges to the regulated N = infinity value, and the regulated value tends to the eps -> 0 value (s4 G).

### E. Potentials

- rho = 1, S1: hbar^00 proportional to f/2, hbar^11 proportional to -(1+f)/4, f = -g. Trace reversal gives hhat^00 = -1/4 (constant) and hhat^11 = -g/4.
- The hhat^33 entry differs from hhat^11 by a term along qhat qhat, removable by the static gauge xi along qhat.
- Quadrature confirms this (s4 G).
- General rho: K(tau) closed by finite parts, against the regulator (s5 B); ratio tends to 1 numerically at rho = 0.75, 1.25 (s5 C).

### F. S1 versus S2

For S_E = (1/2) rho_M (gamma dphi dphi + M^2 phi^2) the source of hbar is dphi dphi. For dust at rest that is T_00 only (S2). With M^2 e^{2 delta phi}, where delta phi = t/(4m^2) (the merged phi = (1/2) ln(rho/sqrt|g|)), the source gains M^2 phi^2 eta/(2m^2), which on shell for dust is (1/2) rho0 eta, giving exactly X of S1 (s5 D). This is hand algebra, recorded rather than symbol-checked.

### G. Literature

Downloaded arXiv source and PDF of 2601.08031 (TeX sha256 233dc123..., PDF 56cc0783...; kept outside the repo).

**Confirmed verbatim from TeX, equation numbers from the PDF text:**
- (3.1), (3.9), (3.25), (3.37);
- (4.33) [F F]_0 = (2/3) A Box A;
- (4.41), (4.42) (the printed (4.42) has a typo, t in place of u, in one term);
- (4.43)-(4.46), m^2 = 32 pi G_N alpha^2 r^-4;
- Box-tilde ~ d0^2 - (1/3) d_i d^i;
- "all hs contributions were ignored";
- "There is no issue with ghost-like signatures in the action, since the extra modes arises only after quantization, and only affect the background geometry";
- "the geometric treatment in section 3 does not fully capture the hs sector".

**Scout's readings:** all those I used are confirmed. The velocity statements (c/3 for extra modes in Sec. 3) are confirmed for 2601 only.

**Not independently verified / not used:** 2609.08955, 1910.00839, 2312.01317, 2405.09804 (scout's reading only, not cited in the insert). The appendix values of V00, V01 were seen but not derived. KumarSteinacker2023 is cited only to say it is not compared. No new bib entry is needed.

**What is not claimed about 2601.** I do not present any of this as an obstruction to the published theory and do not cite it as deriving a single G on polarisations. The surviving differences are:
- (i) the mirage correction sign at k above crossover: fibre-resolved 1 - varpi/(mk)^2 against 1 + 3 varpi/(mk)^2. Exact hypotheses: V = T, S1, equal weights, q.y = 0, large tau, principal value, fibre Laplacian dropped. It could be an artefact of the frozen symbol or of the equal-weight trace, because the sign comes from the resonance near v.v = -varpi, where the fibre Laplacian is largest. The paper itself says the hs parts were ignored there.
- (ii) the residue signs: a property of the form. The paper's "no issue" sentence is a statement about quantization that I neither derive nor refute.

### Hypotheses and forks (per the author directive)

**Obstruction O1: negative-sign extra root.** Hypotheses: H1 frozen symbol; H2 tree at leading symbol; H3 one-loop truncation; H4 formal continuation; H5 helicity 2 or pointwise polarisations alpha.alpha > 0; H6 fibre Laplacian dropped.

| Relaxation | Explored here | Result |
|---|---|---|
| Other weights | yes | Sign independent of V_i, T_i given c_T^TT, c_T^TT + kappa > 0 |
| All harmonics (H5) | yes, equal weights | Becomes a continuum; sign stays on alpha.alpha > 0; polarisation alpha.alpha < 0 has the opposite sign |
| Non-derivative terms | yes, as a lemma | Real roots keep opposite signs; a complex pair needs a negative discriminant; near-null root shifts |
| Change of variable c to hbar | yes | Same sign for w^2 >= 0 |
| Source channel | yes | Static dust at rho = 1 and varpi = 0 has a response with no singular denominator; this does not remove the state |
| Higher loops / large number of K modes (H3) | no | Open, rank 1 for N |
| Fibre Laplacian and cross term (H6) | no | Open; they can split the continuum and may matter at the resonance |
| Inert and trace at w | partly | Pointwise form covers them at equal weights |

**Obstruction O2: S2 gives potential ratio 0.** Hypotheses: rigid K mass, Poisson limit, V = T, equal weights. The relaxation is K-scale response to the dilaton: not computed, rank 1 for C.

**Obstruction O3: no single coefficient off shell or beyond dust.** Factor h(x) on helicity 2 and the p^2 term (s4 F, G). Relaxation: non-equal weights, torsion orders. Rank low, because this class criterion is the one the scout advises not to narrow further.

## Claim classification

| Claim | Class |
|---|---|
| X_n, SC_n, IX2, SC2 on nine D; L_2 = 0 at gauge zero; EH of trace-reversed variable | established (exact, frozen symbol) |
| Dictionary with (4.41), moments 1/3, 1/5, 3/5 | established algebra; identification with the published amplitude is a structural comparison, normalisation not compared |
| S_L factorisation, Z, v^2, mu^2, sign of coefficients | established for these forms; conditional on formal continuation and leading symbol |
| Extra root is a propagating ghost | **not claimed**; unresolved (higher-loop control) |
| Quartic lemma | established |
| Level-one static ratios | established for these forms; conditional on source S1 or S2 |
| Equal-weight pointwise elimination | conditional (weight independent of external harmonic order: assumption outside M above the levels) |
| Null TT coefficient 8A/(1+rho) | conditional as above; exact within it; numeric truncation check |
| Dust I = rho0^2/4 at V = T, S1; one coefficient T/2 | conditional; exact within it |
| g(tau), K(tau), potentials | conditional; principal or finite-part prescription; numeric checks |
| S1 as matter coupling; V = T | **inputs**, not derived |
| S1 from M^2 proportional to rho/sqrt|g| | conditional hand algebra; dependence not derived |
| Mirage sign difference | conditional; possibly artefact |
| Fibre Laplacian needs varpi >> 1 | scale estimate |

## Proposed changes

**File `chapters/appH-microscopic-proofs.tex`.** One insertion, no replacement.

- **Anchor:** immediately before the line `\section{Problem G: HBEV}` (occurs once, s5 E), so after the 047 closing sentence "...Problems~B and~F remain open and PROGRAMME-CONDITIONAL."
- **Kept:** everything. Nothing is removed.
- **Text:** `proposals/048-fibre-resolved-two-point/appH_insert.tex`, byte-exact, 15572 bytes, sha256 6ec4f65732b683bb5320deb5fd54733640b977ebeb39f0f509ab9b379ac87a5c, ASCII, LF, no BOM. The integrator restores CRLF. This file is the `latex` block; it is not duplicated here, so there is one source of truth.
- **Labels verified:** `ch:vierbein-emergence` (1), `ass:lorentzian` (1).
- **Cites verified:** `Steinacker2026`, `KumarSteinacker2023`. No new labels and no bib change.

**appH L2092, "These results have not been checked against the present operators."** No edit proposed. The sentence sits in the paragraph on more than four matrix coordinates, whose "present operators" are G, K on a four-dimensional leaf with D coordinates. This package compares the level-one forms on CP^{1,2} x K with Eqs. (3.9), (3.25), (4.41)-(4.46) only. It does not check those results against the operators of that paragraph, so the sentence stays true as scoped. The new paragraph states what it compares and, in its scope sentence, what it does not. An edit would touch a scope passage and require a full scan for no gain in accuracy.

**Stale passages elsewhere:** none. The 047 sentence "the trace polarisation or a Newtonian limit" is a statement of what that paragraph did not compute, and it remains true of that paragraph. Likewise the merged "L_2 vanishes on the five" stays true and is sharpened, not contradicted.

## Verification scripts

All are in `proposals/048-fibre-resolved-two-point/`. All print to stdout and write nothing. Saved outputs are `*.out.txt`, produced by shell redirection. They import `../046-fibre-regime-interpolation/forms_lib.py` read-only.

| Script | Checked | Result |
|---|---|---|
| s1_pointwise_forms.py | P1 pointwise, P2 averages (9 cases), P3 dictionary, P3b Fourier sign, P4 moments, P5 helicity-0 values | all residuals exact zero; scout's helicity-0 values reproduce |
| s2_helicity_two_poles.py | c(x), factorisation, v^2, mu^2, residues, four direct form checks, quartic lemma | zero residuals |
| s3_static_level_one.py | static block forms, sources, ratios, general weight limit | closed forms; zeros and poles by roots, not grid points |
| s4_all_harmonic_response.py | pointwise inverse, null TT, g(tau) closed against numeric PV, Galerkin N up to 513, crossover, h(x), regulator sequence, stress entries, potentials | agree; regulator trends stated, finite-eps values differ as expected |
| s5_finite_part_and_mechanics.py | EH of trace-reversed variable, K(tau), general-rho potentials, S1-S2 note, insert mechanics | exact, or numeric as stated; ASCII, anchor 1, labels 1, one status sentence |
| compile_check.py | build with and without the insert, outside the repo | exit [0,0,0,0]; 329 and 333 pages; 0 undefined; 0 multiply defined; scratch removed |

Caveats: s3 prints a "Solution direction" gamma at level one, s^2(s^2-4)/(s^4-10s^2+4), which is not quoted in the insert. The regulated static values at eps = 0.02 are visibly below the eps -> 0 values (0.2107 against 0.25); s4 G shows the trend (0.2492 at eps = 2e-5). Convergence in eps is slow, as a square root.

## Decisions Taken

1. **Target (routine):** R1 + R2 + equal-weight all-harmonic elimination, rather than R1 alone or D1. Reason above. Rejected: narrowing "one coefficient on five polarisations" further; the scout's advice stands, and O3 is recorded rather than pursued.
2. **Report the scout's sign claim as failing in the source channel,** while confirming its eigenvalue arithmetic.
3. **Matter coupling:** record both S1 and S2 rather than choose one. No coupling is derived, and choosing S1 alone would hide O2. Favouring the derivation means pointing at the exact missing input, not assuming it.
4. **L2092:** no edit, for the reason above; avoids an unneeded scope edit.
5. **Variables:** present the two-point function in the amplitude c, the matrix variable, with hbar as derived. The metric stays composite throughout; the fibre family h_n and hhat_n are composites of matrix amplitudes. Nothing makes a metric fundamental.
6. **Fibre-resolved "metric" language:** I call h_n a form variable and disclaim identifying it with the emergent metric.

## Milestone assessment

**Routine by my reading, with one item for the gatekeeper to rule on.** I do not claim Trigger 1: nothing is derived without inputs, since V = T, equal weights and S1 are supplied. Trigger 2 (new no-go) does not clearly apply, because O1 and O2 are bounded obstructions that close no route the manuscript keeps open. Trigger 3: no merged claim is shown wrong; merged text is sharpened only.

The item to rule on: result 5 (one coefficient for TT and static dust, every tau, at V = T under S1) is the strongest statement in the class so far, but I do not mark it a breakthrough because its inputs are unproved. A real breakthrough would need V = T for a constructed K, S1 derived from the K-scale response, and equal weights justified.

## Status-label recommendation

Critical-path list from Ch.17 and appH: A, B, C, D1, E, F, G-derived, N. Affected labels: none. C, F, N stay OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL.

## Author decision needed

None. Advice carried from the scout, no action required: whether B's tensor block is to be judged on all five off-shell polarisations or on the on-shell sector plus source channels. Results 3-6 bear on that but change no label.

## Remaining open step

To close F, N, C in this class the following are still needed, ranked by consequence for the derivation.

1. **K-scale response to the dilaton (C):** is M^2 proportional to rho/sqrt|g| produced, for example through the one-loop vacuum functional of K (2601 Eq. (3.12) has the form rho^-2 V_0)? Decides S1 against S2. Computable in the class.
2. **Control of the extra root (N):** higher loops or a large-K-modes expansion, with the fibre Laplacian and cross term retained near the resonance.
3. **V = T:** a K with W_R = 0 on the required modes, or the static and TT forms at V != T beyond the closed results given. Existence not shown (047's avenue 8), now with a concrete reason to want it.
4. **Weights:** elimination with level-dependent weights away from M above the fibre levels.
5. **Tree non-derivative terms** on level one (V00 analogue, shift of the massless root) in a curved rather than frozen setting; gauge invariance should constrain them.
6. **Replica:** with c^TT = T/2 and fixed-state mixed part T/4 at V = T, the mixed gap becomes -T/4, against -(7/20)T at level one. Not closed; not in the insert. Whether a fibre-resolved cone supplies it is the scout's R4.
7. **D1, A, E, G-derived:** untouched.

## Special instructions for the gatekeeper

Please re-check by independent means:
- **The pointwise forms and the equal-weight step.** The claim that all-harmonic elimination is pointwise rests on the trace being a fibre average for all external harmonics: this is stated as an assumption, and no external harmonic above J = 1 was computed from the proper-time vertices.
- **Dust identity and the comparison constant:** X.X - (tr_3 X)^2 = rho0^2/2 and the calibration -64 pi^2 m^6 (...)/(c q^2). The whole statement "one coefficient" depends on this calibration on the three-space, where hbar is transverse.
- **S1 against S2:** whether "(S1) is the source of the same action with M^2 proportional to rho/sqrt|g|" is correct. My derivation is in s5 (D) as hand algebra.
- **The "attractive sign" wording,** which relies on the sign in Eq. (3.9) and the formal continuation.
- **Whether the mirage-sign sentence in the insert is scoped tightly enough,** or should be shortened.

Must not be asserted:
- that a ghost exists in NAMCG or in the published model;
- that 1/x is removed off shell (it is replaced by h(x));
- that G_stat = G_TT holds without V = T, S1 and equal weights;
- that the published theory is contradicted;
- any Cassini bound (the number in `s4` is an arithmetic illustration and is not in the insert).

Insert length: 15.6 kB, 9 blocks, comparable to 047. If you prefer a split, the natural cut is before "Equal weights and all fibre harmonics".

Result 5 is the claim of highest risk.
