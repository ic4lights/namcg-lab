# Proposal 024-replica-classification, round 2

## Result

Package 024 classifies the three area coefficients of 021, c_A in {2, 1, 0} at (n_D, N_s) = (2, 6), against the published contact-term treatments, and states what the Lewkowycz-Maldacena replica argument implies for G_A versus G_T in the Poisson-limit class. All of it is conditional and bounded; nothing closes Problem B, and no label changes.

What is established (derived here or checked by script, inside the 021 class: Poisson limit, Euclidean section, alpha = 1, Lambda^2 term, one loop, the two replicas of 021):

1. **Contact versus boundary term, exact bookkeeping.** With the heat-trace bookkeeping of the integrated contact paragraph, a delta of xi R on the cone shifts the entropy by -2 pi xi A <phi^2> = -xi A Lambda^2/(8 pi), and the Herzog-Nishioka counterterm dI_E = -2 pi (1-n) xi int phi^2 (their Eq. (2.19)) shifts it by +2 pi xi A <phi^2>. The sum vanishes (`check_contact_vs_counterterm.py`). The first is the Wald contact of Donnelly-Wall Eq. (4). Herzog-Nishioka do not mention Wald's formula (the word is absent from the v3 text, which I searched); the relation is the bookkeeping above, not a statement in their paper. This answers the point the scout left unverified.
2. **Classification (by the form of the coefficient; analogy, not derivation).**
   - c_A = 2 (fixed-state replica, operators with no delta on the cone): the contact-free value. This is the Herzog-Nishioka/Friedrichs-type entropy for scalar and ghost sectors, Kabat's bulk-mode entanglement value for the vector part, and the Kabat/Casini-Huerta value for Dirac fields.
   - c_A = 0 (first-order smooth replica, Q = 1/4 in the torsion reading): the delta-potential entropy of Solodukhin Eqs. (143)-(144) with xi replaced by Q. Solodukhin does not accept this as an entanglement entropy; Donnelly-Wall assign the scalar version to the generalised entropy as a Wald contact. It satisfies S_BH = S_ent - Q (Solodukhin Eq. (322)) with Q = (N_s+2)/4.
   - c_A = 1: no published prescription of this operator class. It is c_A = 2 plus an imported vector contact. Kabat's contact is the Ricci delta that Herzog-Nishioka's vector term (their Eq. (7.2)) *removes*. So the vector contact is not the gauge analogue of the Herzog-Nishioka term; it is the object that term cancels. Donnelly-Wall give it a statistical meaning (edge modes) for Maxwell with Ricci coupling. In the variables (G, rho, dTheta) the Poisson-limit O_v has Q = 0 and a symplectic gauge group, so applying that contact is an input.
3. **Herzog-Nishioka does not map the singular-rho cone to 2.** On rho ~ |z|^(n-1) the scalar operator is unitarily equivalent to -Box + E_s (checked), with s-wave Bessel index nu_0 = |n-1|/(2n). The regular branch vanishes at the tip, so the delta term does not act on it. Its constant -nu_0/2 (verified numerically against the Bessel heat trace) gives the entropy coefficient 1/6 - 1/4 = -1/12 for n < 1 and 1/6 + 1/4 = 5/12 for n > 1: non-analytic at n = 1. The less singular branch swaps them. So 021's smooth value -1/12 is the n < 1 value of the regular branch. Removing the delta alone does not give the contact-free 1/6. The O((n-1)^2) terms for k != 0 depend logarithmically on the tip scale and drop at first order (numerics: partial sums grow as (lambda^2/2)(ln K + 0.574...)).
4. **Teleparallel structure of the replica ambiguity.** From the manuscript's own Weitzenboeck identity, E_s = -(1/2) nabla V + (1/4) V^2 = (1/4)(R_G + T_tele) + (1/4) V^2, with V = d ln rho and T_tele = T^2/4 + TT'/2 - V^2. Per scalar component R/6 - E_s = -R/12 - T_tele/4 - V^2/4. Using T_tele = -R - 2 nabla V gives R-coefficient 1/6, which is the per-component c_T. So for scalar content c_T = c_A (fixed-state) and the two replicas differ exactly by the boundary term R_G + T_tele = -2 nabla V, the flux of nabla ln rho through the entangling surface.
5. **What Lewkowycz-Maldacena implies if the metric is dynamical.**
   - Their entropy is -d_n of the action of a regularised cone minus that of the cone, localised at the tip. The first-order variation vanishes by the equations of motion of the *full* action (their Eqs. (3.1)-(3.4)). That presupposes stationarity of the background, which is the open step of Problem B, so it cannot supply that step.
   - Their regularised cone has the far field of the n = 1 solution with angle 2 pi n, all other fields regular, and both configurations obey the same boundary conditions. With Theta the only field, R_G^(1) = -2 Box dln rho (021) excludes that configuration at first order, so LM's construction is not available in this class. The only first-order regularisation is the smooth family, whose far field rho ~ r^(n-1) differs from the cone's; the vanishing of LM's first bracket is therefore not established for it. The area coefficient of this replica is c_A^sm = -c_R/2, the coefficient of sqrt(G) R_G at fixed coframe torsion, so S = A/4G_ind holds in those variables as a definition of G_ind for every content.
   - It does **not** give G_A = G_T. c_A^sm - c_T = (14 - N_s - 4 n_D)/4, zero only on N_s + 4 n_D = 14 (already in 021's outputs). The scout's inference that "G_A = G_T holds by construction" is not supported in this class.
   - At (6, 2) the conditions c_R = 0 (N_s = 4 n_D - 2) and c_T = 0 (N_s = 22 - 8 n_D) are independent and intersect only at n_D = 2. The 0 = 0 there is the vanishing of the Lambda^2 term of the induced action (two independent supersymmetric cancellations), not a verified consistency of G. c_A (fixed-state) = 2 stays as the contact-free entanglement coefficient, in the relation S_BH = S_ent - Q with S_BH = 0 at this order.
   - So the remaining physical content at IKKT is not "is the Lambda^2 coefficient nonzero" (it is zero in this class) but the next order (Lambda^0, log) on a curved J = 0 leaf. For non-supersymmetric contents the Lambda^2 coefficient is nonzero and G_A != G_T generically.
6. **R-B2 (interpolation) is only partly meaningful.** The identity R_G^(1) = -2 Box dln rho ties the G-deficit to the flux for every first-order perturbation of constant Theta, so there is no family of such perturbations joining the endpoints. Under an assumed superposition of the two first-order local densities, c_A(f) = c_A - f (N_s+2)/4, which is 2 - 2f at IKKT: affine, with no new content beyond the endpoints. The s-wave indices are nu_k = |k + i (n-1)/2|/n, an imaginary twist; the real-holonomy (Bernoulli, periodic) template of Jing-Niu-Xian is not imported.

What is not established: which replica the matrix state selects; stationarity; covariance of the induced action in Theta; the vector contact; edge modes; the next order.

## Target and status

- Problems B (sec:status-B) and A (state/replica datum). Current Appendix H ledger label for B, quoted: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived." Chapter 17 full-GR criterion: A, B, C, D1, E, F, G-derived and N must be DERIVED; H, I, J are optional. I found no discrepancy between ledger and agenda for B or A in this task (I read the B ledger entry in Appendix H; I did not re-read the Chapter 17 text this round beyond the CLAUDE.md summary of the criterion, so "no discrepancy" is for the B entry only).
- Original target (B): derive delta S_D = 0 for allowed fixed-volume variations, and the area coefficient and its relation to the emergent metric. This package derives neither. It narrows what the replica ambiguity of 021 means and what a dynamical-metric argument could and could not add.
- Classification: PROGRAMME-CONDITIONAL (conditional sharpening of 021; no closure).

## Source reading

Digest + targeted reads. The digest header reads `dirty-chapters: yes` (accepted 021/022 integrations), so I treated the working tree as current and read directly: Appendix H Problem B in full (lines 41-205), including the integrated 015/017/019/021 blocks, and the torsion-invariant paragraph (about line 1913); the scout report in full; 021 review-r2 in full. I did not read other chapters; this proposal changes no definition, assumption, scope or status passage, so the full-scan rule 3(c) does not apply. The 021 script outputs `firstorder_poisson.out.txt` and `cone_contact_bookkeeping.out.txt` were read (not rerun); my own scripts recompute the table.

Sources opened live this round (PDF text via pdftotext, plus page images for equation numbers):

| Source | Opened | Equations / passages used |
|---|---|---|
| Herzog-Nishioka arXiv:1610.02261 v3 (JHEP12(2016)138) | full text; images of pp. 7, 8, 34 | Eq. (1.5); (2.12)-(2.20), counterterm (2.19), Friedrichs statement after (2.20); Sec. 5 (5.4), (5.9), (5.20) and "our prescription ... may be restated as removing the contact term"; Sec. 7 Eqs. (7.1), (7.2). |
| Solodukhin arXiv:1104.3712 | Secs. 3.15-3.16, 8.2 | Eqs. (126), (141)-(148), (322)-(323); the statement after (144) that the delta-potential entropy cannot be interpreted as entanglement entropy. |
| Kabat hep-th/9503016 | abstract, Sec. 1 | spin 0 and 1/2: black-hole entropy equals entanglement entropy; spin 1 differs by a contact term in the black-hole entropy only; list of c_1. Body of the paper not read. |
| Donnelly-Wall arXiv:1506.05792 | abstract, Introduction (page image), Sec. III C, IV | Eq. (4) S_contact = -2 pi xi int <phi^2>; the Maxwell contact is not a Wald entropy and has an edge-mode interpretation. |
| Lewkowycz-Maldacena arXiv:1304.4926 | Secs. 2-3, conclusions | the passage before Eq. (3.1), Eqs. (3.1)-(3.4), the conclusion on allowed singularities. |
| Jing-Niu-Xian arXiv:2511.01366 v3 | Secs. 3.2, 4.1-4.3 | Eqs. (4.23) (C_2(alpha, mu_E)), (4.27) (S(mu_E)); mu = i mu_E purely imaginary chemical potential; heat kernel 2 pi-periodic in mu_E. Scalars only. |
| Frolov-Fursaev-Zelnikov hep-th/9607104; Jacobson gr-qc/9404039 | abstract only (arXiv API) | not used in the manuscript block. |

Not opened beyond abstract or skim: Dong 1601.06788 (holographic Renyi; not used), Dong 1310.5713, Camps, Frenkel 2311.10131 (taken from the scout, not independently verified). Equation numbers in the scout for Herzog-Nishioka ((5), (24), (98)) do not match the v3 numbering ((1.5), (2.19), (5.20)); I use v3. The scout's Jing-Niu-Xian numbers ((61), (67), (127)-(128)) are HTML numbers; in the v3 PDF they are (4.23), (4.27).

## Research and reasoning

**Setting and notation (from 021).** Appendix H operators and variables: Poisson limit, alpha = 1, N_tot = N_s + 2 - 4 n_D, b = 1 - n_D/2. c_R = N_tot/6 (coefficient of rho R[g_rho]); c_T = c_R - 4b; c_A (fixed-state, antiperiodic Dirac) = (N_s+2)/6 + n_D/3; c_A^sm = -N_tot/12; c_A - c_A^sm = (N_s+2)/4. These are 021's; their relations are recomputed in `check_contents_and_teleparallel.py`.

**1. Contact versus counterterm.** The heat trace of -Box + xi R on the cone, with the transverse kernel (4 pi s)^-1 at the tip and on the surface, gains -(1-n) xi A/(4 pi s). Integrating ln Z_n = (1/2) int ds/s Tr from s = Lambda^-2 and applying S = (1 - n d_n)(ln Z_n - n ln Z_1) at n = 1 gives -xi A Lambda^2/(8 pi) = -2 pi xi A <phi^2> with <phi^2> = Lambda^2/(16 pi^2), the 021 value. The Herzog-Nishioka counterterm (2.19) enters ln Z_n as +2 pi (1-n) xi int <phi^2> and gives +2 pi xi A <phi^2>. Wald: 1/(4 G_eff) = 1/(4G) - 2 pi xi phi^2 for L = R/(16 pi G) - xi R phi^2/2, the Donnelly-Wall contact. Hence the Herzog-Nishioka entropy is the Solodukhin delta-potential entropy minus the Wald contact, i.e. the minimal-coupling value. This is for the scalar with explicit xi.

**2. Mapping to 021 (analogy).** In the fixed-state replica E_s, E_v and the ghost operator are bounded (Q = 0 in (G, rho, dTheta)); no delta needs removing; the coefficient equals the contact-free one. In the smooth family E_s carries -(1/2) Box dln rho = pi(1-n) delta (Q = 1/4), the delta-potential of Solodukhin (143). The dictionary is by the form of the coefficient. It does not show that the matrix state's modular flow selects either: Herzog-Nishioka is a scalar, flat-background, explicit-xi analysis; Dirac and gauge cases are not in it; Solodukhin says the treatment of non-minimally coupled fields is not yet available.

**3. s-wave analysis.** With O_s = -Box + grad f . grad on the cone (f = ln rho), psi = e^{f/2} u gives O psi = e^{f/2}(-Box u + E_s u), E_s = -(1/2) Box f + (1/4)|grad f|^2 (sympy check in `check_swave_branches.py`). On f = (n-1) ln|z| the angular channel k has index sqrt(k^2 + lambda^2)/n, lambda = (n-1)/2 (the manuscript's Bessel statement). A Bessel channel of index nu with the regular branch has heat-trace constant -nu/2 (numerically confirmed for nu = 0, 1/4, 1/2, 3/4 to 7 digits). For k != 0 the first-order part reproduces the cone constant 1/(12 n); the k = 0 channel gives -|n-1|/(4n). Then (1 - n d_n)[C(n) - n C(1)] at n = 1 is 1/6 - 1/4 for n < 1 and 1/6 + 1/4 for n > 1 (script). This is the "branch" of the 019/021 text, now identified with the s-wave channel. In Herzog-Nishioka's treatment of n > 0 angular modes the regular solution vanishes at the origin and the delta has no effect; the same holds for the k = 0 channel here because nu_0 > 0. Hence "remove the delta" is not "set the s-wave index to zero" on this cone.

**4. Teleparallel identity.** Algebra from the manuscript's Weitzenboeck identity R[G] = -(T^2/4 + TT'/2 - V^2) - 2 nabla V (checked there on exact two-jets) and the Appendix H expression for E_s (checked there). I verified that the two forms of E_s agree on that identity and the decomposition of the density (`check_contents_and_teleparallel.py`). The interpretation (EH versus torsion-scalar Lagrangian representatives, boundary term -2 nabla V) is mine and is not checked against the teleparallel literature.

**5. Lewkowycz-Maldacena, in detail.**
(a) LM Eq. (3.1): S = -d_n[ln Z(n) - n ln Z(1)]. They add and subtract an off-shell regularised cone that agrees with the cone far away; the first bracket is a first-order variation about the solution of period 2 pi n and vanishes by the equations of motion; the second is local at the tip and gives Area/(4G) through the integral of sqrt(g) R over the regularised cone ((3.3)-(3.4)).
(b) "The cone far away" is the n = 1 solution with theta of period 2 pi n, so every other field is regular there.
(c) In Theta-only field space 021's first-order identity R_G^(1) = -2 Box dln rho means the integral of R_G^(1) over the transverse plane equals -2 times the flux of grad ln rho (for fields independent of the surface coordinates). A regular rho far away has zero flux at large radius, so the enclosed deficit would vanish: LM's regularisation (same far field as the cone) does not exist at first order. The only first-order regularisation has rho ~ r^(n-1) far away (the smooth family), a different far field; LM's first-bracket cancellation (same boundary conditions, no boundary terms) is not shown for it.
(d) Local density: a_1 = R_G/6 - E per component; on the smooth family R_G^(1) = -2 Box dln rho and E = -(1/2) Box dln rho, giving (1/6) Box dln rho; with deficit D = -2 Phi this is -D/12 per component, i.e. c_A^sm. Equivalent to -c_R/2 since rho R[g_rho]^(1) = -(1/2) rho^2 R_G^(1).
(e) c_A^sm equals the coefficient of sqrt(G) R_G in (G, torsion) variables (second column of the manuscript table). With S = (Lambda^2 A/8 pi) c and 1/(16 pi G_ind) = c Lambda^2/(32 pi^2) (from the manuscript's relation at c = N/6), S = A/(4 G_ind) in those variables; this defines G_ind and does not test G_A = G_T.
(f) c_A^sm - c_T = (14 - N_s - 4 n_D)/4 (script; equals 021's gap).
(g) Independent vanishing conditions at IKKT: c_R = 0 iff N_s = 4 n_D - 2; c_T = 0 iff N_s = 22 - 8 n_D; intersection (N_s, n_D) = (6, 2) only.

Consequences, with status: G_A = G_T does not follow (derived within the class). At (6, 2) the induced Lambda^2 density vanishes identically in the class (c_R = 0, b = 0), so the LM first bracket involves only the tree-level equation (J = 0 in the 020/021 language). That makes the LM stationarity condition checkable at the supersymmetric point at this order, but I have not derived it for the full action.

**6. Interpolation.** First-order identity as in 5(c). The affine law c_A(f) = c_A^fx + f(c_A^sm - c_A^fx) is the sum of two first-order local densities and rests on the superposition assumption stated in the block. Compact versus non-compact: Jing-Niu-Xian use phi(theta + 2 pi alpha) = e^{i mu_E} phi, a real compact phase, with area coefficient quadratic in mu_E on [0, 2 pi) (their Eq. (4.23)); its structure is the Bernoulli polynomial B_2 of the 019 twist weights. Here the index is |k + i lambda|/n, an imaginary twist: the non-analytic linear term of B_2 corresponds to nu_0, and the quadratic term is replaced by a logarithmically divergent sum. The template is therefore not applied.

**Fork analysis.** The statement "G_A = G_T fails for the smooth replica" depends on: (i) c_T as the Einstein-structure coefficient on the delta-rho = 0 modes; (ii) alpha = 1 and the 019 gluing constants; (iii) Theta as the only field (no independent metric or dilaton); (iv) the Lambda^2 order; (v) the Lagrangian representative (the grouping of total derivatives, point 4). Relaxations:

| Avenue | Hypothesis relaxed | What it would give | Status |
|---|---|---|---|
| A1 next order (Lambda^0, log) on a curved J = 0 leaf | (iv) | at IKKT the Lambda^2 term vanishes, so the first nonzero comparison of the Wald/LM coefficient with the Hessian is there | highest value; needs a_2 coefficients with torsion; open |
| A2 covariant completion of the induced action | (iii)/(v) | which non-Einstein torsion invariants (axial torsion S^2, rho^2 X) cause c_A^sm != c_T; the line N_s + 4 n_D = 14 would be a statement about that invariant | open; 021 avenue |
| A3 tip domain and edge modes of the symplectic gauge sector | vector contact input | whether a 1/e^2-type edge term bounds c_A at 1 (scout R-B4; Frenkel-Hartnoll) | not examined |
| A4 state-dependent frame kappa | identification of rho with the conformal factor | whether the flux of grad ln rho is grad ln kappa in Frenkel's tilde G = kappa G | from the scout only |
| A5 non-quasi-free state, non-rotational flow | 019 constants | different gluing, different c_A | open |
| A6 contents on N_s + 4 n_D = 14 | content | non-vacuity check (c_A^sm = c_T != 0 for n_D != 2) | cheap; unphysical contents |
| A7 stationarity at the supersymmetric point | LM first bracket | with the induced Lambda^2 density zero, only the tree-level equation enters | open; shares work with A1 |

Ranked: A1 > A2 > A7 > A3 > A4 > A5 > A6.

## Claim classification

| Claim | Class |
|---|---|
| Contact and H-N counterterm shifts are -/+ 2 pi xi A <phi^2>; sum zero | established (script + 021 bookkeeping) |
| The contact is the Wald expectation (Donnelly-Wall Eq. (4)); H-N never mention Wald | established for the quote; "H-N term = removal of the Wald contact" is the derived bookkeeping |
| 2 = contact-free (H-N/Friedrichs-type, Kabat entanglement); 0 = Solodukhin delta-potential; 1 = imported vector contact | classification by analogy (scalar, flat, explicit xi in the sources) |
| The Kabat contact is the Ricci delta that H-N Eq. (7.2) removes | established from the cited statements; applicability to the symplectic sector: input |
| Singular-rho cone s-wave: entropy 1/6 -/+ 1/4 for n < 1 / n > 1 (regular branch) | derived (Bessel zeta value, numerics); the Bessel index statement is the manuscript's |
| Replica ambiguity = boundary term -2 nabla V | derived algebra from the manuscript identity; teleparallel interpretation: conjecture/mechanism |
| LM's regularised cone is unavailable at first order when Theta is the only field; the smooth family is the only first-order regularisation, with a different far field; the LM first bracket is not shown to vanish for it | conditional (021's first-order identity and LM's construction); the first-bracket statement unresolved |
| c_A^sm = -c_R/2 = area coefficient of the smooth replica = coefficient of sqrt(G) R_G at fixed torsion; S = A/4G_ind there defines G_ind | established within the class (algebra) |
| G_A = G_T not implied; c_A^sm - c_T = (14 - N_s - 4 n_D)/4 | established within the class (algebra; same as 021 gap) |
| IKKT 0 = 0 is two independent cancellations, no information on G at Lambda^2 | established within the class |
| Affine c_A(f) | conditional on superposition |
| Holonomy template not applicable | derived structurally (imaginary versus real twist; compact versus non-compact) |
| Which replica the state selects; stationarity; covariance of the induced action | unresolved |

## Proposed changes

File: `chapters/appH-microscopic-proofs.tex`, section `sec:status-B`.

Anchor (unique, verified by search in the current working tree): the last sentence of the integrated 021 block,
"...or the next order of either side, and give no value or sign of \(G_{\mathrm{eff}}\). Problems~B, C, D, F and~G remain open."
(count 1; it ends the paragraph "Spin term, Lichnerowicz contact and the smooth first-order cone ..."). The block is inserted immediately after that line and before `\section{Problem C: conformal mode and Cassini}` (count 1). Nothing existing is removed or replaced. If another package also inserts at this anchor, the integrator should order them.

Labels referenced: none added; the block has no `\ref`. It uses the existing macro `\LUV` (namcg-book7.tex:54) and the `\cite` keys Solodukhin2011, Kabat1995, DonnellyWall2016 (all present in `bib/namcg.bib` in the working tree) and the new HerzogNishioka2016, LewkowyczMaldacena2013 (BibTeX below, verified through Crossref: JHEP12(2016)138 and JHEP08(2013)090, matching the arXiv records).

Scratch compile: a copy of the working tree outside the repository, block inserted after the anchor, the two new entries appended to the bib, pdflatex + bibtex + pdflatex x2: 279 pages, no undefined or multiply-defined references, both new keys resolved in the .bbl, the paragraph present in the PDF. The copy was deleted. The integrator must still run `python scripts/build_check.py`. The chapter file uses CRLF; `appH_insert.tex` is LF and must be written with CRLF.

```latex
\paragraph{Replica prescriptions against published contact-term treatments (conditional; not closure).}
Keep the setting, the fixed-state replica and the first-order smooth replica of the preceding paragraph, and write \(c_A\) and \(c_A^{\mathrm{sm}}\) for their area coefficients and \(c_R=N_{\mathrm{tot}}/6\) for the coefficient of \(\rho R[g_\rho]\); \(c_A=2\) and \(c_A^{\mathrm{sm}}=0\) at \(n_D=2\), \(N_s=6\). Put \(V_\mu=\partial_\mu\ln\rho\).

\emph{Scalar and ghost sectors.} For a scalar with a coupling \(\xi R\phi^2\), Herzog and Nishioka add the codimension-two term \(\delta I_E=-2\pi(1-n)\xi\int\phi^2\) (Eq.~(2.19) of~\cite{HerzogNishioka2016}), which cancels the delta of \(\xi R\) on the cone and gives an entropy independent of \(\xi\). With the heat-trace bookkeeping of the contact-term paragraph above, this term shifts the entropy by \(+2\pi\xi A\langle\phi^2\rangle\), equal and opposite to the contact \(-2\pi\xi A\langle\phi^2\rangle\), which is the expectation value of Wald's formula for \(\xi R\phi^2\)~\cite{DonnellyWall2016}, Eq.~(4); Herzog and Nishioka do not discuss Wald's formula, and their term is related to it only through this bookkeeping. The fixed-state replica, whose scalar and ghost operators carry no delta on the cone, therefore has the contact-free coefficient. The smooth replica, in which \(E_s\) contains \(-\tfrac12\Box_G\ln\rho\) with \(Q=\tfrac14\), has the form of the delta-potential entropy of Eqs.~(143)--(144) of~\cite{Solodukhin2011} with \(\xi\) replaced by \(Q\); that review does not accept this entropy as an entanglement entropy, and Donnelly and Wall assign the corresponding term to the generalised entropy as a Wald contact. Neither value is asserted here to be the entanglement entropy of the matrix state: the identifications are by the form of the coefficient, the cited analysis is for a scalar on a flat background, and the operators here have no independent \(\xi\). On the singular-\(\rho\) cone \(\ln\rho=(n-1)\ln|z|\), the operator \(\mathcal O_s\) is unitarily equivalent to \(-\Box+E_s\), with s-wave Bessel index \(\nu_0=|n-1|/(2n)>0\). The regular branch vanishes at \(\Sigma\), so the delta multiplies a function that vanishes there, and the constant \(-\nu_0/2\) gives the entropy coefficient \(\tfrac16-\tfrac14\) per component for \(n<1\) and \(\tfrac16+\tfrac14\) for \(n>1\), non-analytic at \(n=1\); the less singular branch exchanges the two. The smooth value \(-\tfrac1{12}\) is thus the \(n<1\) value of the regular branch, and removing the delta alone does not carry this cone to the contact-free value \(\tfrac16\). The terms of order \(((n-1)/2)^2\) in the indices \(\nu_k\) with \(k\neq0\) depend logarithmically on the tip scale and drop out at first order in \(n-1\).

\emph{Connection sector.} For the Maxwell field in Feynman gauge, Herzog and Nishioka remove the Ricci delta of the vector operator with \(\delta I=-\pi(1-n)\int\delta^{ij}A_iA_j\) (Eq.~(7.2) of~\cite{HerzogNishioka2016}), and note that this term is not gauge invariant. Kabat's contact is that delta: it is present in the black-hole entropy and absent from the bulk-mode entanglement entropy~\cite{Kabat1995}, and Donnelly and Wall identify it with edge modes~\cite{DonnellyWall2016}. Herzog and Nishioka state that their boundary term contributes oppositely to the contact term (Eq.~(5.20) of~\cite{HerzogNishioka2016}). The vector contact \(-1\) that gives \(c_A=1\) is therefore the term that the Herzog--Nishioka term removes. Its use presupposes a \(U(1)\) structure and a Ricci coupling that the operator \(\mathcal O_v\) does not have in the variables \((G,\rho,\partial\Theta)\), where the gauge group is symplectic and \(Q=0\); it remains an input and is not a prescription of this class.

\emph{Teleparallel form.} The identity for the Weitzenb\"ock connection of the paragraph on the torsion invariant gives \(E_s=-\tfrac12\nabla_\mu V^\mu+\tfrac14V_\mu V^\mu=\tfrac14\bigl(R_G+\mathcal T\bigr)+\tfrac14V_\mu V^\mu\) with \(\mathcal T=\tfrac14T_{\lambda\mu\nu}T^{\lambda\mu\nu}+\tfrac12T_{\lambda\mu\nu}T^{\mu\lambda\nu}-V_\mu V^\mu\), and the scalar density is \(\tfrac16R_G-E_s=-\tfrac1{12}R_G-\tfrac14\mathcal T-\tfrac14V_\mu V^\mu\). With \(\mathcal T=-R_G-2\nabla_\mu V^\mu\) the coefficient of \(R_G\) is \(\tfrac16\), which is the value in the quadratic form on the two modes with \(\delta\rho=0\), where \(V_\mu V^\mu\) is of higher order. For scalar content alone \(c_T=c_A\), as stated above, and the two replicas differ by the integrated boundary term \(R_G+\mathcal T=-2\nabla_\mu V^\mu\), the flux of \(\nabla\ln\rho\) through \(\Sigma\).

\emph{Dynamical metric.} In the replica construction of Lewkowycz and Maldacena the entropy is \(-\partial_n\) of the action of a regularised cone minus that of the cone, localised at the tip; the difference between the action of the true \(n\)-solution and that of the regularised cone is a first-order variation about a solution and vanishes by the equations of motion (Eqs.~(3.1)--(3.4) of~\cite{LewkowyczMaldacena2013}). That step requires the background to solve the equations of motion of the full action, of which the stationarity condition of the tensor block is the part not derived here. The regularised cone has the far field of the \(n=1\) solution with the angle identified modulo \(2\pi n\), so that every field other than the metric is regular there. With \(\Theta\) the only field, \(R_G^{(1)}=-2\Box_{\bar G}\,\delta\ln\rho\) excludes such a configuration at first order, as stated above. The only first-order regularisation in this class is the smooth family, whose far field has \(\rho\propto r^{n-1}\) and so differs from that of the cone; the construction of~\cite{LewkowyczMaldacena2013}, and the vanishing of its first bracket, are therefore not reproduced for it. For the smooth replica the area coefficient is \(c_A^{\mathrm{sm}}=-c_R/2\). This is the coefficient of \(\sqrt G\,R_G\) at fixed coframe torsion, so the smooth replica satisfies \(S=A/4G_{\mathrm{ind}}\) in those variables for every content, whereas \(c_A^{\mathrm{sm}}-c_T=(14-N_s-4n_D)/4\), which vanishes only for \(N_s+4n_D=14\). The generalised-entropy structure therefore does not imply \(G_A=G_T\) in this class. At \(n_D=2\), \(N_s=6\), the conditions \(c_R=0\) (\(N_s=4n_D-2\)) and \(c_T=0\) (\(N_s=22-8n_D\)) are independent and meet only there; \(c_A^{\mathrm{sm}}=0=c_T\) is then the absence of the \(\LUV^2\) term in the induced action and carries no information on \(G\), while \(c_A=2\) is the contact-free entanglement coefficient, in the relation, in form, \(S_{\mathrm{BH}}=S_{\mathrm{ent}}-Q\) of Eq.~(322) of~\cite{Solodukhin2011}, where \(Q\) is here the bosonic contact \((N_s+2)/4\) of the smooth reading and \(S_{\mathrm{BH}}\) is built from the induced action.

\emph{Intermediate flux.} For first-order smooth perturbations of constant \(\bar\Theta\) the integral of \(R_G^{(1)}\) over the transverse plane is \(-2\) times the flux of \(\nabla\ln\rho\), so no family of such perturbations joins the two replicas. If the first-order local densities of the pulled-back cone and of the smooth family are superposed with weight \(f\) on the smooth family, then \(c_A(f)=c_A-f(N_s+2)/4\), which is \(2-2f\) at \(n_D=2\), \(N_s=6\); the superposition is an assumption. The indices \(\nu_k=\sqrt{k^2+((n-1)/2)^2}/n=|k+\mathrm i(n-1)/2|/n\) are those of an imaginary twist, so the periodic quadratic dependence of the area coefficient on a real Abelian holonomy is not used.

These statements are for the Poisson-limit operators, the \(\LUV^2\) term, one loop, \(\alpha=1\), and the two replicas stated; they do not derive the replica or the state selected by the matrix model, the stationarity condition, the covariance of the induced action in \(\Theta\), the vector contact, or the tip domain, they treat neither edge modes of the symplectic gauge sector nor fermion edge modes, and they give no value or sign of \(G_{\mathrm{eff}}\). Problems~B, C, D, F and~G remain open.
```

Stale passages elsewhere: none. The sentence in the integrated 021 block "The values \(2\) and \(0\) correspond to a replica in which \(\ln\rho\) carries no flux ... intermediate fluxes are not computed" stays; the new block adds why intermediate flux is not a first-order family.

BibTeX (Crossref-verified):

```bibtex
@article{HerzogNishioka2016,
  author  = {Herzog, Christopher P. and Nishioka, Tatsuma},
  title   = {The Edge of Entanglement: Getting the Boundary Right for Non-Minimally Coupled Scalar Fields},
  journal = {Journal of High Energy Physics},
  volume  = {2016},
  number  = {12},
  pages   = {138},
  year    = {2016},
  doi     = {10.1007/JHEP12(2016)138},
  eprint  = {1610.02261},
  archivePrefix = {arXiv}
}

@article{LewkowyczMaldacena2013,
  author  = {Lewkowycz, Aitor and Maldacena, Juan},
  title   = {Generalized gravitational entropy},
  journal = {Journal of High Energy Physics},
  volume  = {2013},
  number  = {8},
  pages   = {090},
  year    = {2013},
  doi     = {10.1007/JHEP08(2013)090},
  eprint  = {1304.4926},
  archivePrefix = {arXiv}
}
```

## Verification scripts

All in `proposals/024-replica-classification/`, run as `python -I <script>`; outputs saved next to them.

- `check_contact_vs_counterterm.py` / `.out.txt`: sympy. Entropy shift of the cone delta (-A Lambda^2 xi/(8 pi) = -2 pi xi A <phi^2>), of the Herzog-Nishioka counterterm (+), their sum (0), and A/(4 G_eff) = A/(4G) - 2 pi xi phi^2 A.
- `check_swave_branches.py` / `.out.txt`: mpmath/sympy. (1) Bessel-channel heat-trace constant -nu/2 for nu = 0, 1/4, 1/2, 3/4 by numerical integration with Richardson. (2) Entropy coefficients of the singular-rho cone from C(n) = -(1/2) sum_k nu_k for the regular and less singular branches on each side of n = 1 (-1/12 and 5/12 exchanged between branches). (3) Logarithmic growth of the O(lambda^2) sum. (4) Sympy check of O(e^{f/2} u) = e^{f/2}(-Box u + E_s u).
- `check_contents_and_teleparallel.py` / `.out.txt`: sympy. E_s in torsion and rho variables agree on the Weitzenboeck identity; density R/6 - E_s = -R/12 - T_tele/4 - V^2/4, R-coefficient 1/6 after T_tele = -R - 2 nabla V; contents table; c_A^sm = -c_R/2; c_A^sm - c_T = -(N_s + 4 n_D - 14)/4; c_A - c_T = 4 - n_D; c_A - c_A^sm = (N_s+2)/4; IKKT row; the independent conditions N_s = 4 n_D - 2 and N_s = 22 - 8 n_D with intersection (6, 2); the affine law at IKKT.

These check algebra and numerics; they are not proofs of the physical identifications.

## Decisions Taken

- Used the Herzog-Nishioka v3 numbering and flagged the scout's numbering mismatch rather than carrying it forward.
- Treated the LM/Dong question with Theta as the only field, because the manuscript's own first-order identity forbids a regular-rho cone at first order. Treating G and rho as independent fields would make the fixed-state replica the LM replica and give G_A = G_T for scalar content, but it contradicts the Poisson-limit constraint and imports an independent metric. Rejected.
- Did not cite Jing-Niu-Xian in the manuscript block: the point needed (imaginary versus real twist) follows from the manuscript's own Bessel index, and their formula is scalar-only. Used for comparison here only.
- Imported no published formula into the interpolation; the affine law is stated as conditional on superposition.
- Kept the vector contact -1 as an input and stated that it is the term Herzog-Nishioka's vector term removes.
- Did not cite Dong 1601.06788 in the block (holographic Renyi; only the LM construction is used).

## Changelog (r1 to r2)

- Finding 1 (major): Dynamical-metric paragraph and body (Result 5, Research 5(c),(e), classification) corrected per the review snippet: LM's construction is not available in the Theta-only class at first order; the smooth family is the only first-order regularisation, with far field rho ~ r^(n-1); the LM first bracket is not established for it; c_A^sm = -c_R/2 is the area coefficient of this replica; c_A^sm - c_T != 0 kept.
- Finding 2: "absent from the bulk-mode entanglement entropy" (Kabat); added the H-N Eq. (5.20) sentence (verified by the gatekeeper).
- Finding 3: last sentence now "in the relation, in form, ..." with Q the bosonic contact (N_s+2)/4 of the smooth reading.
- "Remaining open step" replaced by the review's ranked avenues. appH_insert.tex equals the r2 block. bib_entries.bib unchanged. No label changes.
- Anchor re-verified (count 1 at line 204; Problem C section at 206); scratch compile outside the repo re-run: 279 pages, 0 undefined or multiply-defined references, both new keys in the .bbl.

## Milestone assessment

Routine to M2: a bounded sharpening (classification, and a bounded structural no-go that the generalised-entropy structure does not imply G_A = G_T in the Theta-only class, plus the s-wave branch identification). No critical-path step is derived from the matrix theory. No breakthrough claimed.

## Status-label recommendation

Current critical-path list (Chapter 17): A, B, C, D1, E, F, G-derived, N. No label change for any of them. Problems B and A remain OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL as recorded.

## Author decision needed

None.

## Remaining open step

Original target B (stationarity of the tensor block, area coefficient and its relation to the emergent metric) is not closed. Avenues, ranked (bounded no-go: G_A = G_T is not implied in the Theta-only Poisson-limit class at the Lambda^2 order, one loop, alpha = 1; each relaxation below targets one of those hypotheses):

1. Next order (Lambda^0, log) on a curved J = 0 leaf at the SUSY content, where the Lambda^2 term vanishes (relaxes the order). First nonzero comparison of the Wald/LM coefficient with the Hessian; needs a_2 coefficients with torsion.
2. A covariant completion of the induced action, identifying the torsion invariants behind c_A^sm != c_T (relaxes Theta-only/Lagrangian representative).
3. Stationarity at the SUSY point (the LM first bracket for the smooth family; shares work with 1).
4. Tip domains and symplectic/fermion edge modes (Frenkel-Hartnoll 1/e^2 structure) (relaxes the vector-contact input).
5. A state-dependent frame kappa (Frenkel) (relaxes the identification of rho with the conformal factor).
6. Non-quasi-free or non-rotational states (relaxes the 019 gluing constants).
7. Contents on N_s + 4 n_D = 14 (non-vacuity check).

## Special instructions for the gatekeeper

- The block must not be read as choosing between the replicas, as asserting that Herzog-Nishioka or Solodukhin describes the matrix state, or as deriving G_T = G_A. It states a classification by the form of the coefficient and conditional consequences.
- Re-check: (1) H-N v3 Eqs. (2.19) and (7.2) and the absence of any mention of Wald's formula (full text searched; equation page images inspected); (2) Donnelly-Wall Eq. (4) and the text that the Maxwell contact is not a Wald term; (3) the s-wave numbers (1/6 -/+ 1/4) via the script and your own evaluation of -nu/2 and of (1 - n d_n) on C(n) = 1/(12 n) - |n-1|/(4 n); (4) that c_A^sm = -c_R/2 and c_A^sm - c_T = (14 - N_s - 4 n_D)/4 follow from the integrated 021 numbers; (5) the claim that LM's regularised cone is excluded at first order in Theta-only field space, which rests on R_G^(1) = -2 Box dln rho from 021 and on LM's construction as quoted; (6) the anchor (unique) and that the block has a single closing status sentence.
- The sentence "the regular branch vanishes at Sigma, so the delta multiplies a function that vanishes there" is a domain statement in the manner of H-N after their Eq. (2.15), not a full self-adjoint-extension analysis; judge whether the wording is adequately scoped.
- The teleparallel interpretation (boundary term, Lagrangian representative) appears in the block only as an algebraic identity plus the statement that the replicas differ by the flux term; no teleparallel literature is cited or claimed.
- Not independently verified: Kabat's body (abstract and Sec. 1 read only), Frolov-Fursaev-Zelnikov and Jacobson (abstracts), Dong's papers, Frenkel 2311.10131.
