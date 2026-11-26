VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: RESEARCHER-DECISION | PROGRESS: first | OPEN: 1/3

## Verdict
The tree statement, scaling identity, exponent algebra, static response, rank-one vacuum term and literature all re-derive. The headline does not hold as scoped: the potential of chi omits the chi-dependent first term of the merged factorisation. That term is not small on the class's own solutions, and it falsifies "S1 and V = T are incompatible at a local minimum for Uhat >= 0", the weak-coupling statements on S^2_N, the window, and "S1 is not the coupling computed". Another round is required. This is a review verdict, not merge approval.

## Source reading
**Method: digest + targeted reads. No full scan.**

Ruling on the scan:
- Ordinal 47 is not a 5th item.
- There is no milestone verdict.
- The package changes no definition, assumption, scope or status passage. It adds one conditional paragraph and one bib entry.
- `make_digest.py --check` printed DIGEST CURRENT.
- `dirty-chapters: yes` matches the only modified file, appH. Per the 2026-10-15 directive it does not by itself trigger a scan, so I read the working-tree files directly.

Read in full:
- proposal-r1.md, appH_insert.tex, new_bib_entry.bib;
- 048 review-r2.md;
- MILESTONE.md;
- appH L2370-2488, i.e. the working-tree 044-048 blocks;
- ch17 L139-157 and L690-749;
- the appH C and F labels, and the N label at L2858.

Read in part:
- digest (header, and manifest lines by grep);
- the ledger tail, lines cut to about 400 characters;
- ch03 L137-175;
- the bib entries used;
- the paper passages named below.

reports/sme-scout-20261101-after45.md: I did not read it, and I do not rely on it. Unreadable files: none. Process slip: my first read rounds used parallel calls, against the serial rule; nothing in the repo changed. `git status` is still only appH.

## Claim under review
Original targets:
- **Problem C:** scalar operator, coupling, Cassini comparison, Assumption gap-psi discharged.
- **Problem F:** A, B, C and the sign/scheme of G_eff from specified operators.
- **Problem N:** no propagating Ostrogradsky ghost for p < L_UV.

Verbatim labels:
- **C:** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. A scalar-tensor result is a reduced-scope outcome only when its operator, coupling and phenomenological test are supplied; it does not by itself meet the matrix-derived criterion."
- **F:** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating \(G_{\mathrm{eff}}\) as an input leaves F OPEN and does not satisfy the matrix-derived criterion."
- **N:** "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL."

The Ch.17 critical path is A, B, C, D1, E, F, G-derived, N, with no discrepancy against CLAUDE.md. The package claims: the K mass is rigid in gamma at tree level; chi responds with beta_K < 0 at any local minimum with U_4 <= 0, U_2 < 0; so S1 is not the computed coupling.

## Checks performed
**Hand derivations (agree unless a finding says otherwise).**

- **Background values.**
  - G = eta/m^2, m^2 = -y^2 - l^2, rho = 1/m. This gives R = 18 vartheta - 24, phi = (3/2) ln m, box phi = 6 vartheta - 6, |dphi|^2 = -(9/4) vartheta, E_0 = 6 - (15/4) vartheta.
  - Hence R/6 + E_0 = 2 - (3/4) vartheta. This derives the merged value, and E_0 = -box phi - |dphi|^2 follows from conjugating the operator.
  - Xbar = 6 y^2/m^2 = -6 vartheta, by direct contraction and also from merged L2438 (-R + 4 box phi + 4|dphi|^2 = -3 vartheta). It agrees with the expansion 4(1-xi)e^{-xi/2} = 4 - 3 s vartheta + ...
  - The U_4 and U_2 prefactors follow from Gamma = -(1/2) int ds/s str, with W_X = -T/8. U_2 at V = T is correct.
- **First variation.**
  - delta ln sqrt|g| = -t/2m^2.
  - delta ln X at fixed Tbar = -t_perp/3m^2 with t_perp = t - y.h.y/y^2.
  - Omega = (1/2) hbar^00 - (5/3) hbar^11.
  - Tbar.deltaT = -(2/m)[(q.v)(y.alpha) - (alpha.v)(q.y)] = 0 at q.y = 0, since q.v = 0 identically.
- **Exponents.**
  - beta_K = -U_chi,phi/U_chichi. Static (8U_4 + 4U_2)/U_chichi and homogeneous (8U_4 + 2U_2)/U_chichi both correct for the forms stated. V_t = 0 gives 1/2.
  - Cases -1/(1+eps), cubic and mass all correct at Y = 0 (Y is defined under F1).
- **Scaling.** H = lambda H_M + chi^2 H_K, s -> s/lambda. Flat direction and exponent 1/2 correct. phi = ln lambda.
- **"Local minimum".** S_E carries +U and the tree kinetic is +Z_chi(d ln chi)^2/2, with Z_chi = rho_M chi^2 nbar m^2/g^2 from (1/2g^2) Tr F_ai F^ai. So "local minimum" means a stationary point of the formal Euclidean-sign density with U_chichi > 0 in the frozen continuation. This agrees with S = T - V stated immediately before (7.48) of 2303.08012. It carries no statement about the Lorentzian path integral; the insert's "formal continuation" scope is adequate.
- **Integrating out chi.** beta_K(q) and the contact term correct, with J = 2 rho0 m^2.
- **Source.** X_beta on the mass shell and h_beta = delta(e^{-2 beta phi} gamma) correct.
- **Static response.**
  - The I decomposition expands exactly to (1-beta)g + beta^2/4 + (varrho-1)(g2 - beta g + beta^2/4).
  - g2 closed form from the parameter derivative of the principal value.
  - g - g2 = 2/S - (16/3)/S^2 and g2 - g^2 = -(4/3)/S^2, with S = sinh^2 tau.
  - Potentials (2-beta)g, beta(1-g)/2, beta - 2g. Ratio beta(1+g-beta)/(4g(1-beta)+beta^2) -> beta/(2-beta).
  - Heavy t: g(1-g) with ratio 1/2.
  - Interval (1, 4/3] from monotonicity of 2(1-beta)/(2-beta).
- **Vacuum term.**
  - det(1 + alpha v^T/m) = 1 + x. Delta(B/A) = -q_b^2/q^2, with q_b^2 = 12 Uhat chi^2/m^2(Vhat + 2 That). The factor 1/2 from the phase average is in place. The three poles follow from the Legendre form.
  - Moments 1/3 and 1/15 match (4.27).
- **Flat stacks.** The identity v - tau = 16 s0 prod sinh checked at order s^4, with sign chart f1 - f2 - f3.
- **Window algebra.** Correct as algebra, but see F1.

**Own computation (scratchpad).**
- Closed sums at 60 digits, up to N = 4096: V-T-4lnN -> 1.016184; T/N^2 -> 4; U/N^2 -> 1. The printed fit stands and is labelled numerical. No V-T claim goes beyond N = 512.
- The 0.9994 ratio at N = 1024 is a ratio of V0 and T0 separately, not of the difference V-T, and it is printed by the re-run s5. I recomputed the same quantities independently at (N, n) = (64, 4) and (256, 10), which agree: 0.98006, 0.98058, 0.99314, 0.99318.
- First-term derivative: see F1.

**Scripts on copies outside the repo.** s1-s5 outputs are byte-identical to the saved files. I read the saved s6 and compile_check outputs and did not re-run them: anchor count 1, labels 1 each, one status sentence; [0,0,0,0], 333 -> 337 pages, 0 undefined. My `sha256sum` of the insert matches the proposal. The anchor line is unique (appH L2490). Rendered pages not inspected. The "round " hit in s6 is the "background" false positive, as stated.

**Literature (e-prints and PDFs fetched; e-print sha of 2303 and 2509 match the proposal).**
- **2303.08012:** (7.47)-(7.48), S = T - V, -6 coth^2 eta, "This is indeed possible in Minkowski signature". The "not evident a priori" sentence is commented text, as said. "Could a priori have either sign" is present.
- **2509.24753:** title and authors match the bib entry. (3.35), (3.36), (3.37) with A = alpha^2, so chi ~ lambda^{-1/6} at fixed l and tau. Footnote 11 and the rescaling sentence are present (the latter for alpha-proportional chi, i.e. epsilon = -3/4).
- **2601.08031:** (3.12), (3.14), (4.27), (4.46), L351, L832, "should cancel up to curvature", V01 > 0.

Tensions are stated with no conclusion on those works. rho^2 = sqrt G/rho_M equals e^{2 phi}, which I checked. The V_0 sign convention matches through S = T - V.

**Not verified:**
- the external-harmonic hypothesis above J = 1;
- the fibre-flux first-term coefficient;
- the rotating-K fluctuation operator;
- the "hand estimate" in proposal section G.

## Findings

**F1. Severity: blocking. Location: "Potential of chi" and every statement built on it (sign statement, S^2_N values, m_chi, V = T paragraph, window, Consequence; proposal items 4, 5, 8, 9).**
- *Finding.* "The terms ... that depend on chi are rho_M V_t/g^2 + U_4 + U_2" is false. The first term s_0^K(v^M - 2 sigma^M) of merged L2375 depends on chi through s_0^K.
- *Reason (independent derivation).*
  - For Z = rotation in the (y, k) plane, v - 2 sigma = 2(cosh 2sw - 1) - 8(cosh sw - 1) = s^4 w^4 + ..., and <w^4> = (1/4s^2)(y^4/m^4)(9 + 6).
  - So v^M - 2 sigma^M = (F sqrt|g|/16 pi^2)(15/4) vartheta^2 at order s^0. This is the merged closed forms (15 xi^2), and Q^V - 2Q^D = (15/4) vartheta^2 is consistent with merged 3125/648.
  - Then dU/d ln chi gains Y = (15F/64 pi^2) vartheta^2 sqrt|g| N_K >= 0, with N_K the modes having chi^2 mu_A^2 >> vartheta. Merged L2413 already says this weight is "not suppressed by the flux of K".
  - Numerics, full frozen integrals, N = 64 and 256, confirm Y -> (15/2) vartheta^2 (N^2 - 1) in units F sqrt|g|/32 pi^2, for example 30685 against 30712 at chi^2 = vartheta. The mixed term matches 2U_2 to 0.9994 and 0.9999.
  - On S^2_N at large N, Y/2|U_2| = (5/4) vartheta/chi^2.
  - The researcher's weak-coupling minimum sits at chi^2 = (3/2)|eps| vartheta << vartheta, where Y dominates.
- *Consequences within the class (frozen, V = T, late static).*
  - In the static channel the loop terms depend on h only through sqrt|g|. Late-time h lies along y, and A = y^2 eta - y y annihilates y, so <J^n> is unchanged. Therefore U = U_t(chi) + e^{-2 phi} L(chi), and exactly
    beta_K = 2 L'/U_chichi = -2 U_t'/U_chichi.
  - So beta_K has the sign opposite to the slope of the tree term. "For every V_t" fails.
  - With x = chi^2/vartheta, L' is proportional to -4x^2 - 6x + 15/2, positive for x < (sqrt 39 - 3)/4 = 0.811.
  - Counterexample in units a N^2 vartheta^2, a = F sqrt|g|/32 pi^2: Uhat > 0, V = T, x = 0.3, tree quartic 7.935 plus tree cubic -12.36 (or quartic 3.3 plus mass -9.27). Then |eps| = 0.011 (0.027), U_chichi = 10.68, beta_K = 1 exactly.
  - For V_t = abar chi^4 alone, P = A x^2 - 6x + 15/2 with A = 4(1/|eps| - 1), so a stationary point needs |eps| >= 10/13, with minimum at x >= 5/2 and beta_K < -1. There is no minimum at weak coupling. So "beta_K -> -1 at weak coupling", m_chi^2 = 4(1+eps) chi^2 and the window are vacuous as printed.
- *Caveat.* The fibre-flux part of the first term (merged L2415: per level J^2/mu_J) is not computed and could change Y. So the positive result here is also conditional.
- *Required action.* Either carry Y through, or restrict everything to chi^2 >> vartheta and drop the tree-quartic results. See RESEARCHER-DECISION below. Add a script in the folder checking Y and the formula above; do not rely on my check. Change the proposal's headline, claim table and hypothesis class accordingly.

**F2. Severity: major. Location: Consequence, "The route to beta_K = 1 that remains here is ... a tree mass and a loop quartic above the tree quartic".**
- *Finding.* False even at Y = 0.
- *Reason.*
  - In the cubic case beta_K = 2(2U_4 + U_2)/(2Utilde + 2U_4 - U_2) = 1 exactly at U_4 = Utilde - (3/2)U_2, with U_chichi > 0 and negative cubic (example Utilde = 1, U_2 = -1, U_4 = 5/2, C_3 = -4), and it tends to 2 beyond. The researcher's own s4 prints "y2=0: 2".
  - With cubic and mass together any U_4 > -U_2/2 works, so neither a tree mass nor U_4 > Utilde is necessary.
  - In the mass case with U_2 < 0, beta_K < 1 strictly (exact 1 needs U_2 = 2 Utilde > 0).
  - The necessary condition at Y = 0 is only 2U_4 + U_2 > 0, hence Uhat < 0.
- *Required action.* R7, R18.

**F3. Severity: major. Location: Explicit K, flat stacks.**
- *Finding.* "Uhat < 0 and Vhat < That" is stated exactly, but as defined (int_0^infty) these integrals diverge: Uhat ~ -1/s_c, V-T ~ ln s_c, T ~ 1/s_c^2. Only the integrand sign is exact.
- *Reason.* The exponents use U_4 ~ chi^4. A fixed proper-time cutoff gives chi^2/s_c instead. A cutoff scaling as chi^{-2} (mode truncation) preserves scaling, but then the sign is not established, since pointwise negativity is a statement about the untruncated identity.
- *Required action.* R9.

**F4. Severity: major. Location: Tree level, "A positive beta_K can therefore come only from the response of chi".**
- *Finding.* Non sequitur.
- *Reason.* A correction c M^2 e^{-2 l phi} with c < 0 has positive logarithmic derivative. The power counting gives the exponent of the correction, not its sign. It is correctly labelled as power counting; the inference is the problem.
- *Required action.* R1.

**F5. Severity: minor. Location: scalar channel.** "(1/2)(A/4 pi^2) sqrt|g| g d phi d phi" is off by 2 as a density under the 048 convention, since the forms are phase averages. Merged L2438 gives (A/16 pi^2) sqrt|g|(-R + 4|d phi|^2), and sqrt|g| R is a total derivative for a static lapse, so the density is (A/4 pi^2) sqrt|g| |d phi|^2. Its phase average reproduces (q^2/4L) t^2. "t is a physical scalar here" overclaims: only gauge invariance (q.v = 0) and the static sign are shown. R12.

**F6. Severity: minor. Location: notation.**
- "g" denotes the metric, the coupling and the function g(tau), and "g_2 - g^2" sits in the same paragraph as rho_M/g^2.
- V_0 collides with the merged weight V_0.
- U is never defined.
- "Yukawa pole" needs M >= 0.
- R4, R11, R13, R14.

**F7. Severity: minor, for the record.** The proposal's "Stale passages: none" and the "(S1) ... not the computed coupling" reading must be redone. The merged "which is not derived" remains true.

**PRIOR-CLAIM-ERROR: none.** The 048 S1/S2 statements remain true as scoped (S1 = beta 1, S2 = beta 0, X_beta reduces to both; the 048 limits are reproduced). 044-047 give the first term correctly. The omission is in this proposal only. Published (7.48) has the same two-term structure under its weak-coupling condition (7.49); no conclusion on that work is drawn, and agreement of structure does not validate completeness here.

**Literal checks that pass:** the exact string `\section{Problem G: HBEV}` as anchor; no status, priority or completion label changed; one closing status sentence; emergence kept; "not a Cassini bound" stated; compact-K scan not in the insert; "a finite list, no general statement" present; no non-existence claim leaks; the fit is labelled numerical; the window is labelled a scale estimate; no process language.

**RESEARCHER-DECISION.** Choose how to resolve F1:
- (a) carry Y through and keep the Uhat > 0 route open; this favours the infrared derivation and is what R1-R20 implement;
- (b) restrict the whole paragraph to chi^2 >> vartheta, deleting the V_t = abar chi^4 results, m_chi formula and window, and record chi^2 <~ vartheta as not treated.

Either way another round is needed. My recommendation is (a), together with computing the fibre-flux part or stating it as open.

**Required replacements (R1-R20; every old string verified to occur once in the r1 insert, sha 13879e6c...; apply in order).** Old strings are in `C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\g49\own\repl_old.txt`, line k = Rk. The researcher must verify each new text and may substitute option (b).

- **R1.** old: `A positive \(\beta_K\) can therefore come only from the response of \(\chi\).`
  new: `So, while the loop expansion is controlled, a value \(\beta_K\) of order one can come only from the response of \(\chi\); a loop correction of negative sign contributes a small positive part.`
- **R2.** old: `the terms of the action density without derivatives of the wave that depend on \(\chi\) are`
  new: `the terms of the action density without derivatives of the wave that depend on \(\chi\), through first order in the background torsion, are`
- **R3.** old: `including the negative sign of the torsion term in the Lorentzian section.`
  new: `including the negative sign of the torsion term in the Lorentzian section. At the next order the first term \(s_0^K(v^M-2\sigma^M)\) of the factorisation enters: at the frozen symbol \(v^M-2\sigma^M\) has the value \(\tfrac{15}{4}\vartheta^2F\sqrt{|g|}/16\pi^2\) at order \(s^0\) on the background, so \(\partial U/\partial\ln\chi\) gains \(Y=\tfrac{15F}{64\pi^2}\vartheta^2\sqrt{|g|}N_K\ge0\), with \(N_K\) the number of modes of \(K\) with \(\chi^2\mu_A^2\gg\vartheta\). It is not suppressed by the flux of \(K\) or at large \(N\); on \(S^2_N\) at large \(N\), \(Y/2|U_2|=\tfrac54\vartheta/\chi^2\). The fibre-flux part of the same order is not computed.`
- **R4.** old: `Write \(U_{\chi\chi}=\partial^2U/\partial(\ln\chi)^2\) at a stationary point.`
  new: `Write \(U\) for this density and \(U_{\chi\chi}=\partial^2U/\partial(\ln\chi)^2\) at a stationary point. In this channel \(Y\) also carries \(\sqrt{|g|}\) alone.`
- **R5.** old: `\beta_K=\frac{4(2U_4+U_2)}{U_{\chi\chi}},`
  new: `\beta_K=\frac{2(4U_4+2U_2+Y)}{U_{\chi\chi}}=-\frac{2\,\partial_{\ln\chi}(\rho_MV_{\mathrm t}/g^2)}{U_{\chi\chi}},`
- **R6.** old: `Hence at a local minimum, \(U_{\chi\chi}>0\), for \(U_4\le0\) and \(U_2<0\) one has \(\beta_K<0\) for every \(V_{\mathrm t}\).`
  new: `Hence at a local minimum, \(U_{\chi\chi}>0\), \(\beta_K\) has the sign opposite to the slope of the tree term; for \(U_4\le0\) and \(U_2<0\) one has \(\beta_K<0\) for every \(V_{\mathrm t}\) exactly where \(Y<4|U_4|+2|U_2|\), in particular for \(\chi^2\gg\vartheta\).`
- **R7.** old: line 7 of repl_old.txt, from `\(\beta_K=-1/(1+\varepsilon)\); adding a tree cubic term` through `and a tree mass of negative sign for the minimum.`
  new: `\(\beta_K=-1/(1+\varepsilon-Y/4\tilde U)\); adding a tree cubic term, of the form of the cubic term of Equation~\eqref{eq:Smatrix} read on \(K\) and supplied there, gives \(\beta_K=2(4U_4+2U_2+Y)/(4\tilde U+4U_4-2U_2-3Y)\); adding a tree mass term gives \(\beta_K=(4U_4+2U_2+Y)/(4\tilde U+4U_4-Y)\). Where the tree stabiliser dominates, \(\beta_K\to0\), from below where the tree slope is positive. For \(Y\) negligible, \(\beta_K>0\) needs \(U_4>0\), so \(\hat U<0\); then \(\beta_K=1\) is attained in the cubic case at \(U_4=\tilde U-\tfrac32U_2\) and approached from below in the mass case as \(U_4\) comes to dominate \(\tilde U\) and \(U_2\), each with a tree term of negative slope.`
- **R8.** old: `so \(U_4<0\), \(U_2<0\) and \(\beta_K\le-1\) at the minimum for \(V_{\mathrm t}=\bar a\chi^4\), with \(\beta_K\to-1\) at weak coupling \(|\varepsilon|\ll1\).`
  new: `so \(U_4<0\), \(U_2<0\) and, at large \(N\) with \(x=\chi^2/\vartheta\) and \(N^2\chi^2\gg\vartheta\), \(4U_4+2U_2+Y\) is proportional to \(-4x^2-6x+\tfrac{15}2\), positive for \(x<(\sqrt{39}-3)/4\simeq0.81\). For \(V_{\mathrm t}=\bar a\chi^4\) a stationary point then exists only for \(|\varepsilon|\ge\tfrac{10}{13}\), the minimum having \(x\ge\tfrac52\) and \(\beta_K<-1\), so there is none at weak coupling.`
- **R9.** old: `so for \(f_1<f_2+f_3\), the range without a negative mode, \(\hat U<0\) and \(\hat V<\hat T\), and for \(f_1=f_2+f_3\), \(v\equiv\tau\). So the sign of \(\hat U\) depends on \(K\).`
  new: `so for \(f_1<f_2+f_3\), the range without a negative mode, the integrands of \(\hat U\) and \(\hat V-\hat T\) are negative for every \(s\), and for \(f_1=f_2+f_3\), \(v\equiv\tau\). These integrals diverge at small \(s\) for such non-compact stacks, so \(\hat U<0\) and \(\hat V<\hat T\) are signs with a lower limit on \(s\); the scaling \(U_4\propto\chi^4\) then needs a limit that scales as \(\chi^{-2}\), such as a fixed truncation of the modes, for which the sign is not established. On this evidence the sign of \(\hat U\) depends on \(K\).`
- **R10.** old: `For \(V_{\mathrm t}=\bar a\chi^4\), \(m^2m_\chi^2=8(1+\varepsilon)\bar a\chi^2/\bar n\), which is \(4(1+\varepsilon)\chi^2\) on \(S^2_N\). So (S1) is not the coupling computed in this class, and (S2) holds above \(m_\chi\) and approximately where a tree stabiliser dominates.`
  new: `For \(V_{\mathrm t}=\bar a\chi^4\), \(m^2m_\chi^2=8(1+\varepsilon-Y/4\tilde U)\bar a\chi^2/\bar n\), which is \(4(1+\varepsilon-Y/4\tilde U)\chi^2\) on \(S^2_N\). So (S2) holds above \(m_\chi\) and approximately where a tree stabiliser dominates, and below \(m_\chi\) the value (S1) is a condition on the tree stabiliser and on \(\chi^2/\vartheta\), not an output of this class.`
- **R11.** old: `in addition to \(g\) of the preceding paragraph,`
  new: `in addition to the function \(g=g(\tau)\) of the preceding paragraph (in the next display \(g^2\) is its square, not the coupling),`
- **R12.** old: `that is \(\tfrac12(A/4\pi^2)\sqrt{|g|}g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi\) in this static channel, with the positive sign in \(S_E\), so that \(t\) is a physical scalar here and the matter charge is \(1-\tfrac12\beta_K\).`
  new: `the phase average of the density \((A/4\pi^2)\sqrt{|g|}g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi\) in this static channel, with the positive sign in \(S_E\); \(t\) is gauge invariant here, since \(q\cdot v=0\), and the matter charge is \(1-\tfrac12\beta_K\).`
- **R13.** old: `\(V_0=-F\hat U\chi^4/32\pi^2\).`
  new: `\(V_0=-F\hat U\chi^4/32\pi^2\), not the weight \(V_0\) of the preceding paragraphs.`
- **R14.** old: `and for \(\hat U<0\) it is a Yukawa pole.`
  new: `and for \(\hat U<0\) and \(\mathcal M\ge0\) it is a Yukawa pole.`
- **R15.** old: `so (S1) and \(V=T\) are incompatible at a local minimum for \(\hat U\ge0\): the sign of the torsion term that supplies the minimum is the one that makes \(\beta_K\) negative.`
  new: `so for \(\hat U\ge0\) and \(\chi^2\gg\vartheta\), where \(Y\) is negligible, (S1) and \(V=T\) are incompatible at a local minimum: the sign of the torsion term that supplies the minimum is the one that makes \(\beta_K\) negative. This does not extend to \(Y>4|U_4|+2|U_2|\).`
- **R16.** old (with its leading space): ` For \(V_{\mathrm t}=\bar a\chi^4\) and \(\vartheta\) near \(1\) this condition and \(|\varepsilon|\ll1\) leave the window \(F/4\pi^2N\ll\rho_M/g^2\sqrt{|g|}\ll3NF/8\pi^2n^2\), as a scale estimate.`
  new: empty.
- **R17.** old: `and the computed exponent is negative for \(\hat U\ge0\).`
  new: `and the computed exponent is negative for \(\hat U\ge0\) where \(\chi^2\gg\vartheta\).`
- **R18.** old: `The route to \(\beta_K=1\) that remains here is \(\hat U<0\), a tree mass and a loop quartic above the tree quartic, for which \(q_b^2<0\) and the vacuum term must then be cancelled at the minimum without cancelling its derivative in \(\chi\).`
  new: `The value \(\beta_K=1\) needs a tree term of negative slope at the minimum, together with either \(\hat U<0\), for which \(q_b^2<0\), or \(Y>4|U_4|+2|U_2|\), which at large \(N\) on \(S^2_N\) is \(\chi^2<0.81\vartheta\) and is subject to the fibre-flux part not computed; the vacuum term must then be cancelled at the minimum without cancelling its derivative in \(\chi\).`
- **R19.** old: `the fibre-constant background for \(U_2\);`
  new: `the fibre-constant background for \(U_2\) and \(Y\), with higher orders in \(\vartheta/\chi^2\) not treated;`
- **R20.** old: `The sign statement and the exponents are exact for these forms, the values on explicit \(K\) are exact spectra with numerical fits, and the window is a scale estimate.`
  new: `The sign statement and the exponents are exact for these forms, and the values on explicit \(K\) are exact spectra with numerical fits.`

Check for r2: R17 leaves "exceeds 1 ... for beta_K in [-1,0)", which stays true. I verified only the old strings by script; the new texts were checked by algebra (R7 cubic and mass forms at Y = 0, and the numeric counterexample through the R7 cubic formula). I did not compile the result.

## Scope of what is established
**Exact for these forms (stands):**
- tree form and rigidity in gamma at fixed chi;
- l-loop exponent -l, power counting only and labelled so;
- Gamma_1 as a function of chi^2/lambda where the proper-time form converges;
- homogeneous exponent 1/2 and flat direction;
- Tbar.deltaT = 0, Omega;
- beta_K = -2 U_t'/U_chichi (late static, V = T), which after F1 is the sharper form;
- beta_K(q), contact term (tree kinetic only);
- X_beta, h_beta;
- I[X_beta], g2, potentials, ratios, heavy-t residual, Legendre form, rank-one determinant, q_b^2, three poles (given U_4 alone among second-order vacuum terms).

**Numerical:** S^2_N limits, fit, equal-weight ratios.

**Conditional, valid only after F1:**
- for Uhat >= 0, beta_K < 0 and S1 incompatible with V = T for chi^2 >> vartheta;
- at chi^2 <~ vartheta, the sign is that of -U_t'.

**Not established:**
- S1 or S2 for the K selected by the theory;
- the fibre-flux part of Y;
- mass of t;
- G_eff;
- any ghost statement;
- any Cassini bound on the emergent metric.

**Open:** C, F, N remain OPEN and PROGRAMME-CONDITIONAL. Nothing is DERIVED. No label change.

**Obstruction classes (none closes a direction outside its hypotheses).**

Common hypotheses: Poisson limit; one loop; IKKT content supplied; product background without mixed flux; K single-scale with fixed Lambda; matter mass from chi alone; frozen symbol; formal continuation; first-order response; q.y = 0; V = T; late time; q below m_chi; local minimum of chi with tree kinetic; equal weights.

- **O4a, beta_K < 0.** The common hypotheses plus U_4 <= 0, U_2 < 0, chi^2 >> vartheta (precisely Y < 4|U_4| + 2|U_2|). Not a no-go for S1 outside this range.
- **O4b, no minimum at weak coupling.** For the undeformed quartic on S^2_N at large N, |eps| < 10/13; frozen first term, fibre-flux part excluded.
- **O5, ratio 1 at large tau.** Needs light t and beta_K = 1, at V = T, equal weights, late static, first order.

**Milestone ruling.**
- M2 is not met. The claimed no-go does not hold as stated. The corrected class is a bounded restriction on a coupling that 048 kept only as a non-derived input, which is the same standard as 044-048.
- M3 is not met: nothing merged is false.
- M4, M5: none. BREAKTHROUGH: no; this is conditional, and the S1-compatible point is tuned and rests on an uncomputed part.
- No SME consultation needed.

**Open avenues, ranked (each keeps spacetime emergent).**
1. Complete the chi potential at order vartheta^2: fibre-flux part of the first term and its response. This decides whether the chi^2 <~ vartheta branch with beta_K > 0 and Uhat > 0 survives. It is directly favourable to C.
2. Fluctuation operator about the rotating K (2509.24753), static channel with uniform omega. Note the hand estimate in proposal section G is not verified.
3. Tree stabilisers with negative slope: the cubic form and its actual coefficient for a K selected by the theory. Exact beta_K = 1 needs a relation among tree data and chi^2/vartheta; test whether anything fixes it.
4. Non-derivative sector of t: q_*^2 (including -U_chi,phi^2/2U_chichi), tadpole, V_00, V_01, and cancelling U_4 at the minimum while keeping d/d chi.
5. Compact K with Uhat < 0 and no negative mode, or a proof of absence. The scan so far is uninformative, and no non-existence is claimed.
6. Level-dependent and external-harmonic weights; fibre Laplacian.
7. Loop kinetic and W_R mixing of chi; non-singlet moduli; composition dependence.
8. D1, overdue and independent; a reasonable next package if avenue 1 stalls.

## Recommended disposition
Revise. Do not integrate r1. Round 2 must resolve F1 by option (a) or (b), close F2-F7, add a first-term verification script, and restate the headline and hypothesis class. Bib entry `MantaSteinacker2025b` is verified and may stay unchanged.

## Corrected snippet
R1-R20 above. No new physics beyond the merged factorisation and closed forms. Extra caveat: the fibre-flux part stays not computed.

## Files
- Proposal: `C:\Users\redgi\Projects\namcg-lab\proposals\049-k-scale-dilaton-response\proposal-r1.md`
- Insert: `C:\Users\redgi\Projects\namcg-lab\proposals\049-k-scale-dilaton-response\appH_insert.tex`
- First-term check: `C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\g49\own\firstterm.py` and `C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\g49\own\firstterm2.py` (the mixed column of firstterm.py is nan; use firstterm2.py)
- Equal-weight check: `C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\g49\own\d.py`
- Old strings and uniqueness check: `C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\g49\own\repl_old.txt` and `C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\g49\own\chk.py`
- Script copies and outputs: `C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\g49\copy`
- Fetched sources: `C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\g49\lit`
