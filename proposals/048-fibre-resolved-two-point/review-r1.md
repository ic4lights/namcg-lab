VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/3

## Verdict
The central derivations all re-derive, but three printed statements are literally false or incomplete and must change before integration: the three-space calibration, the variable behind "potential ratio 0", and the sign interval. A further round is required. This is a review verdict, not merge approval.

## Source reading
**Method: digest + targeted reads. No full scan was done, and I rule that none is required.** The package changes no definition, assumption, scope or status passage, and it is integration ordinal 46.

- **Digest:** `make_digest.py --check` printed DIGEST CURRENT, `dirty-chapters: yes`. I opened only the digest header and read the working-tree files directly. Only appH is modified.
- **Read in full:**
  - proposal-r1.md and appH_insert.tex (sha256 6ec4f657..., confirmed);
  - 047 review-r3;
  - appH L2086-2097, L2130-2147, L2380-2392, L2393-2459;
  - ch17 L495-520, L690-749;
  - MILESTONE.md;
  - forms_lib.py.
- **Read in part:**
  - appH L404-407, L1366-1369, L2825-2832;
  - the ledger 047 entry;
  - the scout report (grep of R1, R2 and the sign claims);
  - the opening of s2 and s3.
- **Unreadable files:** none.
- **Process slip:** I issued several batches of read-only calls in one block, against the sequential rule. Nothing changed; all my files are in the scratchpad.

## Claim under review
The conditional 048 paragraph on CP^{1,2} x K covers fibre-point forms, helicity +-2 with the tree form, equal-weight elimination of all harmonics, and static dust under couplings S1 and S2.

Verbatim labels:
- **Problem C (appH L404-407):** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. A scalar-tensor result is a reduced-scope outcome only when its operator, coupling and phenomenological test are supplied; it does not by itself meet the matrix-derived criterion."
- **Problem F (appH L1366-1369):** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating \(G_{\mathrm{eff}}\) as an input leaves F OPEN and does not satisfy the matrix-derived criterion."
- **Problem N (appH L2827-2828):** "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL."

The Ch.17 critical path re-read at L690-749 is A, B, C, D1, E, F, G-derived, N. There is no discrepancy with CLAUDE.md. No label changes and no target is claimed closed.

## Checks performed
All algebra below was done by hand unless marked otherwise; my scripts are listed at the end.

**1. Fibre-point forms (hand, from the definitions).**
- EH2 = -(q^2/8m^6)(h.h - t^2), and the dilaton term is q^2 t^2/32m^6.
- These give X_n and SC_n as printed.
- The fourth moment gives IX2 and SC2 as printed.
- F_2 is proportional to qhGhq, which vanishes at every fibre point, so L_2 = 0 on all nine.
- The decomposition with 5m^2[...] + l^2k^2(4 delta - 2 qhat qhat) is correct.
- The moments are 1/3, 1/5, 3/5.
- My static block, built from these closed forms without forms_lib, equals s3's F_qq, F_qp, F_pp exactly.

**2. Two-point form (hand).**
- Z, v^2, mu^2 and 1 - v^2 are as printed.
- The coefficients at the two roots are +Z(k^2-w^2) and -Z(k^2-w^2).
- The residue is 256 pi^2 m^6/c.
- a at the massless and extra roots is as printed.
- The discriminant and the first-order shift are as printed.
- At the extra root the one-loop term is -1 times the tree term, which is immediate from the root's definition. On the null cone the ratio is (1-v^2)k^2/mu^2.
- **Tree input:** it matches merged L2130-2147 (S^(2) = (1/4g^2) int vol m^2 F F, with kappa-factor delta_ij). The phase average is the same as for the induced forms.
- **Induced normalisation:** -1/32 pi^2 is merged L2381, consistent with 1/G = c/2 pi.
- **Sign convention:** merged L2145 says the overall sign "depends on the convention for the weight". The insert fixes this explicitly with S_L = -S_E. The opposite relative sign of the residues does not depend on that choice.
- **(4.44):** S proportional to (q0^2-k^2)(q0^2-k^2/5+m^2) has the same overall sign as the insert's S_L.

**3. Weights.** A, B, C, varrho, 4A = W_R/6 - 4W_X and kappa are as printed. c_T^TT at equal weights is (2V+T)/5. On the null cone v.v = a sin^2 theta, which gives I = (1+varrho)/4 X.X. c^TT is as printed, and (2V+T)/5 > c^TT, the difference being proportional to 3V^2 - 2VT + 2T^2.

The level-one extra root at V = T is a Rayleigh quotient of the continuum, with sin^2 theta weights reproducing 1/5 and -(4/5) l^2/m^2.

**4. Dust and calibration (hand plus sympy).** X eta^-1 X = rho0^2 eta/4 holds. See finding 1 for the calibration.

**5. Principal-value and regulator claims.**
- g(tau) was derived by hand as c-integrals and agrees with my closed-form computation.
- Beyond-dust I, h(x) and "1 - g" were derived by hand.
- K was computed by parameter-differentiated finite parts: 0.32952847, 0.92209551, 0.99920021 at s^2 = 9, 100, 1e4, matching s5.
- The potential ratio at varrho = 0.75, 1.25 tends to 1 from below (0.99967, 0.99988 at 1e4). s5's values above 1 are regulator noise; the conclusion stands.
- My independent quadrature reproduces 0.2106676, 0.2372844, 0.2455324, 0.2492261 and continues to 0.2499921 at eps = 2e-7.
- The exact deficit follows sqrt(eps) pi/(2 sqrt 2) for eps >> c0^2 and pi eps/(2 c0 theta) for eps << c0^2. So 0.2492 against 0.25 is fully explained.

**6. S1 against S2 (hand).** The source is (1/2)rho_M[dphi dphi + M^2 phi^2 eta/(2m^2)]. On the mass shell M^2 <phi^2>/m^2 = <phi_dot^2>, so X = rho0(uu + eta/2) for dust, and X = T - (1/2) eta trT for any free massive mode.

The claim is correct but needs "on the mass shell". An independent check: hhat = delta(e^{-2 phi} gamma), so S1 is a rigid mass in the frame with cometric e^{-2 phi} gamma, which is the G of (3.9). S1 is not smuggled in: the insert says "not derived".

**7. Literature.** Source fetched (TeX sha256 233dc123..., PDF equation numbers checked with pdftotext).

Confirmed from source:
- (3.1), (3.9), (3.12), (3.25), (3.37), (4.33), (4.41), (4.43)-(4.46);
- the (4.42) typo (t in place of u);
- the tilde-Box symbol u u k k - k0^2 and its average k^2/3 - k0^2;
- "all hs contributions were ignored";
- the "no issue with ghost-like signatures" sentence;
- the 1/3 vs 1/5 sentence.

V00 and V01 values in the appendix were not derived by me and are not used.

**8. Scripts.**
- s1, s2, s3, s4 on copies: output identical to saved.
- s5 parts A-D identical. Part E exits with an error on my copy because it walks the repo. I checked its anchor, ASCII and bib items separately.
- Label counts rest on the saved s5 output and identical merged uses.
- compile_check was not re-run because the text must change; the saved output is 0 undefined, 329 and 333 pages. Rendered pages not inspected.
- My own Galerkin on the null cone gives c_N/A = 4.8, 4.28571, 4.14815, 4.06154, 4.01061 at N = 1, 3, 5, 9, 25, matching s4. I did not re-implement the varrho = 0.75 truncation; I rely on s4.

**Not verified:**
- any external harmonic above J = 1 from proper-time vertices (none exists; the insert states this as an assumption);
- the static N -> infinity limit at eps = 0. Only N -> infinity at fixed eps, then eps -> 0, is checked, and the insert claims no more;
- the scale estimate varpi >> 1 beyond my own power count, which agrees, and which the insert labels a scale estimate.

## Findings

**1. Severity major. Location: "would give ... X.X - (tr_3 X)^2", "since X.X - (tr_3 X)^2 = 1/2 rho0^2", "ratio to the same source".**
- **Finding:** with X = T - (1/2) eta trT as defined, the four-dimensional contraction is X.X = rho0^2, tr_3 X = rho0/2, and the difference is (3/4) rho0^2, not (1/2) rho0^2.
- **Reason:** the elimination on transverse hbar uses the projection X_3. Then X_3.X_3 - (tr X_3)^2 = T.T - (1/2)(trT)^2 = rho0^2/2 (sympy residual 0). So c = T/2 stands only with the projected X.
- For S2, the printed form with X = T gives 0, so "the same source" cannot be the reference of "four times this" or of 4g. The reference used by s3 is the T.T - (1/2)(trT)^2 value.
- **Required action:** R1-R5.

**2. Severity major. Location: "so the second potential vanishes and that ratio is 0".**
- **Finding:** "that ratio" was defined as hhat^11/hhat^00. For S2, hhat = (1/2) hbar^00 (1,1,1,1) in the upper diagonal, so that ratio is literally 1. The value 0 is hbar^11/hbar^00.
- **Reason:** the fork is real only with the reading "potentials in the variable the source couples to". Then gamma-like values are g and 0. The sum hbar^00 + hbar^11 = hhat^00 + hhat^11 is the same in both readings.
- **Required action:** R9-R12.

**3. Severity major. Location: "for V_i=T_i and (S1) ... negative for 4<sinh^2 tau<5+sqrt 21".**
- **Finding (interval):** the roots and poles are right, but the printed list of negative intervals omits 5 - sqrt 21 < s^2 < 2/3. There the ratio is -0.857 at s^2 = 1/2 and -2.436 at 9/16; s3's own output shows the latter.
- **Finding (formula):** the formula holds only for V_i = T_i = T. With T_0 != T_1 = T_2 and V_i = T_i the value differs: 37677/53452 against 2251/3576 at s^2 = 100.
- **Required action:** R6, R7. Proposal Result 4 ("survives only at intermediate tau") must be corrected in r2.

**4. Severity minor. Location: "the value 1/5 at large tau needs these weights".**
- **Finding:** 1/5 means c = 4 kappa, one linear condition on the weights: V_0/6 + T_0/12 + (V_1-T_1)/30 - T_2/4 = 0. So "needs" is false in general. Among equal weights it does force V = T.
- The answer to your item 5 is therefore: 1/5 requires V = T among equal weights, not in general. V_i = T_i alone is also insufficient unless T_0 = T_2.
- **Required action:** R8.

**5. Severity minor. Location: mirage sentence.**
- **Finding:** (3.25) prints (1 - m^2 tilde-Box^-1). The quotient tilde-Box/(tilde-Box - m^2) is its inverse, displayed after it. The identification of that mass with varpi/m^2 is also unstated, and "m" collides with the fibre m.
- **Required action:** R13-R15.

**6. Severity minor. Location: "(S1) is the source of the same action". The on-shell condition is omitted. Required action: R12.**

**7. Severity minor. Location: notation.**
- **Finding:** T is both the weight and the stress ("X=T", "at V=T" in one passage). A is both DG and (V+2T)/24.
- **Required action:** R16-R21.

**8. Severity minor. Location: proposal-r1 caveat "Convergence in eps is slow, as a square root".**
- **Finding:** true only for eps >> c0^2; below that the deficit is linear. Not in the insert.
- **Required action:** correct it in proposal-r2.

**Rulings**
- **Item 1:** equal weights stated as a hypothesis in the opening sentence of the block and again as "an assumption" in the scope paragraph. Nothing reads as a derivation of Newtonian gravity. The scope sentence denies G_eff, Cassini and any emergent-metric identification.
- **Item 4:** the extra root is not claimed as a state. The text is a bounded obstruction bearing on N, and it says whether the root is a state "depends on the control of higher loops". This is not a claim about Problem N beyond what is shown. N's target concerns the emergent graviton two-point function, which the insert disclaims.
- **Item 6:** the mirage sentence does not read as a contradiction once R13-R15 are applied. It is then scoped tightly enough to keep. Algebra verified: factor = 1 + sigma PV int dc/(c^2 - sigma) = 1 - sigma + ..., against 1/(1 - 3 sigma); both tend to -1/(3 sigma) as k -> 0.
- **Item 8:** no merged claim is false, so there is no PRIOR-CLAIM-ERROR.
  - c_T^TT at level one stands.
  - "L_2 vanishes on the five" is sharpened, not contradicted.
  - The inert-elimination sentence at L2448 concerns level-one inert amplitudes, not higher harmonics.
  - The phase-average convention matches L2398, and no Q_i is used.
  - Note for the ledger: the 047 review avenue text "1/x ... comes from restricting to level one" is superseded by the denominator reading. That text is in a review and the ledger, not in the manuscript.
- **L2092:** stays true as scoped ("present operators" are G, K of that D-coordinate paragraph). No edit, no full scan.
- **Item 9:** labels unchanged. The one closing status sentence is scoped. Emergence is kept: hbar, hhat, h_n are composites and are disclaimed against the emergent metric. "Newtonian limit" appears only as something not computed earlier. No process language.

**Anchor:** `\section{Problem G: HBEV}` occurs once (appH L2459). Citations `Steinacker2026` (eprint 2601.08031) and `KumarSteinacker2023` exist.

**Significance:** consequential and coherent. No split is needed. Results 1-6 share the pointwise form and the same source updates.

## Scope of what is established
**Exact for these forms:**
- X_n, SC_n, IX2, SC2, L_2 = 0;
- the EH form of hhat_n at V = T;
- the factorised S_L and residue signs (frozen symbol, leading-symbol tree, formal continuation);
- level-one static ratios, by exact symbolic closed forms;
- the moments dictionary as algebra.

**Conditional on equal weights, V = T and S1:**
- I = rho0^2/4 for every q with q.u = 0;
- c = T/2 = c^TT with attractive sign;
- the ratio g(tau) -> 1 in hhat.

**Conditional, wider:**
- the V != T large-tau statements (finite part; numerics at two varrho);
- S2 values.

**Inputs, not derived:** V = T, equal weights above J = 1, S1 or S2, rho_M and g, formal continuation.

**Open:** C, F, N remain OPEN and PROGRAMME-CONDITIONAL. Nothing is DERIVED.

**Bounded obstruction classes:**
- **O1, opposite sign at the extra root.** Frozen symbol; leading-symbol tree dropping non-derivative terms and the fibre Laplacian; one-loop truncation; formal continuation; helicity +-2 or alpha.alpha > 0 pointwise; w^2 >= 0 for the hbar reading.
- **O2, ratio 0 in hbar.** Rigid K mass; V = T; equal weights; q.y = 0.
- **O3, no single coefficient off shell or beyond dust.** Equal weights at V = T.

None of these closes a direction outside its class.

**Open avenues, ranked (each keeps spacetime emergent; none is the only route):**
1. K-scale response to the dilaton: is the K mass rigid in the e^{-2 phi} gamma frame? This decides S1 against S2 and is the sharpest computable step for C.
2. Control of the extra root: higher loops or a large number of K modes, with the fibre Laplacian and cross term kept near the resonance, for N.
3. Fibre Laplacian retained in the static channel; decides whether the mirage sign difference and the principal value survive.
4. Level-dependent weights, including the external-harmonic vertices above J = 1, away from M above the levels. The singular eliminator needs high J, so this tests the equal-weight hypothesis directly.
5. V = T: existence of K with W_R = 0, or the V != T static and TT forms.
6. Tree non-derivative terms and V00, V01 on level one.
7. A fibre-resolved cone for the replica gap at c^TT = T/2.

## Recommended disposition
Revise, then re-review. Apply R1-R21 to appH_insert.tex. Each old string was verified to occur exactly once in the current file, by script; applying all of them in sequence leaves the text ASCII at 16390 characters. Re-run s5(E) and compile_check. In proposal-r2 correct Result 4, the "as a square root" caveat, and the classification row for level-one sign. Milestone: none. Conditional result, not a breakthrough, by the same standard as 044-047. No SME consultation needed.

## Corrected snippet
No new physics; no extra assumption. Old => New:

- **R1.** `would give \(-64\pi^2m^6(X\cdot X-(\operatorname{tr}_3X)^2)/cq^2\), with \(\operatorname{tr}_3\) the trace on the three-space orthogonal to \(q\).` => `would give \(-64\pi^2m^6(X_3\cdot X_3-(\operatorname{tr}X_3)^2)/cq^2\), with \(X_3\) the projection of \(X\) on the three-space orthogonal to \(q\).`
- **R2.** `since \(X\cdot X-(\operatorname{tr}_3X)^2=\tfrac12\varrho_0^2\).` => `since \(X_3\cdot X_3-(\operatorname{tr}X_3)^2=T^{\mathrm m}\cdot T^{\mathrm m}-\tfrac12(\operatorname{tr}T^{\mathrm m})^2=\tfrac12\varrho_0^2\).`
- **R3.** `a ratio to the same source with the coefficient \(c_T^{\mathrm{TT}}\) of` => `a ratio to the one-coefficient value \(-64\pi^2m^6(T^{\mathrm m}\cdot T^{\mathrm m}-\tfrac12(\operatorname{tr}T^{\mathrm m})^2)/cq^2\) at \(c=c_T^{\mathrm{TT}}\) of`
- **R4.** `the response is \((V+2T)/(2V+T)\) times that of \(c^{\mathrm{TT}}\)` => `the response is \((V+2T)/(2V+T)\) times the one-coefficient value at \(c=c^{\mathrm{TT}}\)`
- **R5.** `the response is \(4g(\tau)\) times that of the coefficient \(c^{\mathrm{TT}}\)` => `the response is \(4g(\tau)\) times the one-coefficient value at \(c=c^{\mathrm{TT}}\)`
- **R6.** `for \(V_i=T_i\) and (S1) the ratio is` => `for \(V_i=T_i=T\) and (S1) the ratio is`
- **R7.** `negative for \(4<\sinh^2\tau<5+\sqrt{21}\), tending to \(\tfrac23\)` => `negative for \(5-\sqrt{21}<\sinh^2\tau<\tfrac23\) and \(4<\sinh^2\tau<5+\sqrt{21}\), tending to \(\tfrac23\)`
- **R8.** `the value \(\tfrac15\) at large \(\tau\) needs these weights, and in general the limit is` => `the value \(\tfrac15\) at large \(\tau\) holds at these weights and, among equal weights \(V_i=V\), \(T_i=T\), only there, and in general the limit is`
- **R9.** `which is the ratio of the two potentials once the part along` => `which is the ratio of the two potentials, read in \(\hat h\), the variable to which this source couples, once the part along`
- **R10.** `so the second potential vanishes and that ratio is \(0\).` => `so, read in \(\bar h\), the variable to which this source couples, the second potential vanishes and the ratio is \(0\) (in \(\hat h\) the same solution has ratio \(1\); the sum of the two potentials is the same in both readings).`
- **R11.** `the value \(1\) of that ratio depends on` => `the value \(1\) of the ratio so read depends on`
- **R12.** `(S1) is the source of the same action with` => `(S1) is, on the mass shell, the source of the same action with`
- **R13.** `which is the fibre-resolved form of \(\tilde\Box/(\tilde\Box-m^2)\) of Equation~(3.25) of~\cite{Steinacker2026}; for` => `which has the structure of \(\tilde\Box/(\tilde\Box-\varpi/m^2)\) resolved on the fibre, the mass in the inverse of the factor in Equation~(3.25) of~\cite{Steinacker2026} being read as \(\varpi/m^2\), a normalisation not compared; for`
- **R14.** `This difference of sign is conditional on these hypotheses and on dropping the fibre Laplacian` => `This difference of sign is conditional on these hypotheses, on the principal value and on dropping the fibre Laplacian`
- **R15.** `were ignored in that derivation.` => `were ignored in that derivation, so no conclusion on that work is drawn.`
- **R16.** `for dust \(T_{\mu\nu}=\varrho_0u_\mu u_\nu\)` => `for dust \(T^{\mathrm m}_{\mu\nu}=\varrho_0u_\mu u_\nu\)`
- **R17.** `as \(T_{\mu\nu}\hat h^{\mu\nu}\)` => `as \(T^{\mathrm m}_{\mu\nu}\hat h^{\mu\nu}\)`
- **R18.** `so that \(X=T-\tfrac12\eta\operatorname{tr}T\)` => `so that \(X=T^{\mathrm m}-\tfrac12\eta\operatorname{tr}T^{\mathrm m}\)`
- **R19.** `with \(X=T\),` => `with \(X=T^{\mathrm m}\),`
- **R20.** `for \(T=\varrho_0uu+p(e_1e_1+e_2e_2)\)` => `for \(T^{\mathrm m}=\varrho_0uu+p(e_1e_1+e_2e_2)\)`
- **R21.** `2(\operatorname{tr}A)^2+2\operatorname{tr}AA^{T}+2\operatorname{tr}A^2]\), with \(P=DGD^{T}\) and \(A=DG\)` => `2(\operatorname{tr}DG)^2+2\operatorname{tr}DG^2D^{T}+2\operatorname{tr}DGDG]\), with \(P=DGD^{T}\)`

## Files
- Proposal: `C:\Users\redgi\Projects\namcg-lab\proposals\048-fibre-resolved-two-point\proposal-r1.md`
- Insert: `C:\Users\redgi\Projects\namcg-lab\proposals\048-fibre-resolved-two-point\appH_insert.tex`
- Static block, calibration, potentials check: `C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\g48\own\a.py`
- Regulator check: `C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\g48\own\e.py`
- Galerkin check: `C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\g48\own\g.py`
- Replacement once-only check: `C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\g48\own\r.py`
- Paper source: `C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\g48\paper\GravityfromIIB-NC-V2.tex`
