# Proposal 011-fuzzy-leaf, round 1

## Result

Target: the leaf-dimension relaxation (4+k-dimensional symplectic leaf, M^{3,1} x compact fuzzy factor) named in 008/009 as the within-core route past the obstruction `G != c g`. Hypothesis class and findings (all kinematic or conditional; nothing on the critical path is derived):

1. **Bounded no-go (Theorem 1), exact.** Let the base coordinates `y^mu` of the reduced 4D theory be the Lorentzian block `x^mu`, `mu=0..3`, of the D matrix coordinates (real `Theta`, `eta=diag(-1,1,..,1)`, any D, any leaf dimension, any compact fibre, any positive fibre measure). Then the fibre-averaged operator tensor `S^{mu nu}=<Theta^{I mu} eta_{IJ} Theta^{J nu}>` satisfies `S^{00}>=0` and `tr S>=0` (sums of squares, symbolic check D=4..7), so `S = c eta^{-1}` forces `c=0`. Hence in this class the obstruction does not disappear on averaging: raising the leaf dimension by a fibre does nothing. Leaf-level companion: for any real Lorentzian nondegenerate `g_L` on a symplectic leaf of dimension 2m, `G_L=(theta^T g_L theta)^{-1} != c g_L` (`det(g^{-1} omega)<0` vs `c^m>0`).
2. **Product class (Prop. 2).** For `M^4 x C` with block-diagonal `theta` and embedding (Steinacker2023's `M^{3,1} x K`), the zero-mode tensor is exactly `K_M`; first-order response of `K` is the 4D one with amplitude `<A^mu>_C`; transverse and non-constant fibre amplitudes drop (`V^{i mu}=0`). Einstein-operator rank stays 3 about a flat M (script: 3 for 3 transverse fuzzy-sphere coordinates). KK modes enter only quadratically (matter). So a product factor adds no gauge-invariant functions and no conserved stress at linear order.
3. **Where the obstruction is actually absent (Prop. 3, exact algebra + numerics).** Take the SO(4,2) coadjoint orbit `CP^{1,2}` (6-dim leaf), D=4 matrices `T^a=M^{a4}/R`, and **different** base functions `x^mu=M^{mu5}/R`. The Lie-Poisson relation gives `{T^a,x^mu}=s eta^{a mu} M^{45}/R^2` (s=-1 in my convention), so pointwise `K^{mu nu}=(M^{45}/R^2)^2 eta^{mu nu}`: Lorentzian, conformal to the Cartesian `eta_{mu nu}` of the position functions, no fibre average needed; `M^{45}` is a function of `x^mu` (`x_a x^a=-n^2/4`). Verified on explicit orbit (rank of generator Poisson matrix 6; rank of `{x^mu,M^{AB}}` 4; K_L has rank 4 with 4x4 base block conformal to eta). So the escape is: matrices are momentum-like and the base coordinates are conjugate functions, not matrices. Cost: G is conformally flat (single scalar), so no metric waves in the exact class; fluctuations of `T^a` that are fibre-constant do not change `K` at first order in the (numerically checked, Monte-Carlo) fibre-average of `M^{mu nu}`; metric fluctuation needs s>=1 harmonics. Rank/Einstein count for these is NOT done.
4. **Heat kernel over the fuzzy factor (conditional).** For the product class the Poisson-limit scalar operator is `O_s (x) 1 + 1 (x) Box_C`; each 4D sector is replicated over the n^2 modes of Mat(H_C) with proper-time weight `F(m^2/Lambda^2)=e^{-x}-x Gamma(0,x) in (0,1]`. NAMCG's truncated heat kernel therefore gives `1/G_eff ∝ Lambda_UV^2 sum_Lambda d_Lambda F` (UV-dominated, ~n^2 Lambda^2 for light modes), not a KK-scale-set constant; common-threshold limit of the 005 TT coefficient is `Z (1-(D-2)/24)` with `N_s=D-4`, positive (wrong-sign for induced EH in 005's convention) for D<=10. Definite EH sign is not obtained. Steinacker2023's mechanism differs (below).
5. **New exact structure for the connection-sector term X (resolves 005's open item).** `X=eta^{rl}eta eta d_rTheta d_lTheta = G_{mu nu}T^{ab mu}T_{ab}^nu` exactly (`Theta^T G Theta=eta^{-1}`), with `T^{ab mu}=Theta^{mu r}d_r Theta^{ab}` the Weitzenboeck torsion of the coframe `e=eta^{-1}omega`. Chain: `V_mu=d_mu ln rho` (numerical, exact in class), teleparallel identity (numerical to cubic order), `S^2=(I_A-2I_B)/3`; result
   `rho^2 X = -2 rho R[g_rho] - rho|grad ln rho|^2 + (3/2) rho^2 S_{lmn}S^{lmn} + 2 d_mu(g_rho^{mu nu} d_nu rho)`
   (S = totally antisymmetric part of torsion), pointwise through third order in the Poisson-class perturbation, all masks, generic momenta; the extra "eta-using rewriting" of 005 is the axial torsion squared. Matches the ratio `TT = -2R - Ttilde^2` of Steinacker2023 (6.29)->(6.32) as I read it (coefficient -2; T-tilde normalisation from Kumar-Steinacker (2.17)-(2.19) gives `Ttilde^2=-(3/2)S^2` by my computation, not independently verified). Not proved to all orders.

Not established: any field equation for G; Einstein rank in the covariant class; gap of transverse scalars; `Phi`=coframe; any G_eff value or sign.

## Target and status

Problem F (`ass:emergent-op`, primary), A, D1, E by dependency. Appendix H: F "OPEN; CRITICAL PATH; PROGRAMME-CONDITIONAL" (ledger paragraph `sec:status-F`, quoted from file); Chapter 17 criterion lists A,B,C,D1,E,F,G-derived,N; ledger/009 state unchanged; no discrepancy found. Original target (F): discharge `ass:emergent-op` or replace by a derived ingredient: NOT met. PROGRAMME-CONDITIONAL.

## Source reading

Digest CURRENT (`--check`). Targeted reads: ch03 lines 85-205 (`def:matrix-coords`, `eq:Smatrix`, `def:matrix-coords-ext`), all of ch08, appH Problem F ledger + 005 paragraphs (lines 1103-1135, 1630-1836) incl. 008/009 paragraphs, ledger, proposal 009 r2, 005 scripts. Not a full scan: no definition, assumption, scope or status text is changed (only new appH paragraphs). Literature: Steinacker2023 (arXiv:2303.08012) read pp.1-6, 12-30 of the PDF (intro, heat kernel, Sec.4-7.3); Kumar-Steinacker (2312.01317) read pp.1-7 (abstract, Sec.2-3); Steinacker2026 (2601.08031): abstract only, not independently verified beyond that.

## Research and reasoning

**Setting.** Semiclassical leaf with Poisson bracket `{,}`; `V^{I mu}:={x^I,y^mu}`; zero-mode kinetic tensor of functions `phi(y^mu)` is `K^{mu nu}=<eta_{IJ}V^{I mu}V^{J nu}>_fibre`. For a 4D leaf, `V^{I mu}=theta^{alpha mu}d_alpha x^I`, recovering `K=theta^T g theta`.

**Theorem 1.** If `y^mu=x^mu` (mu=0..3), `V^{I mu}=Theta^{I mu}` antisymmetric. `S^{00}=sum_{I>=1}(Theta^{I0})^2>=0`. `tr S=sum_{I>=4}(Theta^{I0})^2+sum_{I>=1,k>=1}(Theta^{Ik})^2>=0` (the `-(Theta^{0k})^2` of the time row cancels `(Theta^{k0})^2`). `c eta^{-1}` has `S^{00}=-c`, `tr=2c`: c<=0 and c>=0. Because the argument is linear in a positive measure, averaging cannot help. Numerical addendum: minimum of `min_c||S-c eta^{-1}||/||S||` over 1-4-point measures found 0.5 (D>=5) and 0.577/0.5 (D=4), consistent with a uniform gap (observation only). Where the proof fails: `y^mu` not among the matrices (Prop. 3), or Euclidean/complexified data.

**Prop. 2.** Product: `V^{i mu}={x^i(y_C),y^mu}=0`; so `K_bar=theta_M^T g_M theta_M`. First order `delta K^{mu nu}=(theta^T p)^mu (theta^T eta <A>)^nu+(mu<->nu)`; no dependence on transverse or non-constant parts. Therefore 008/009 statements apply with D replaced by the number of coordinates actually varying over M. (Honest caveat: bare action does not make a fuzzy sphere a solution; background is off shell, as in 005.)

**Prop. 3.** `{M^{AB},M^{CD}}=s(eta^{AC}M^{BD}-eta^{AD}M^{BC}-eta^{BC}M^{AD}+eta^{BD}M^{AC})` (verified, s=-1, 150 samples in an explicit su(2,2) oscillator realisation). With `eta^{45}=0` only the (a,mu) contraction survives. All numerical checks in `check_covariant_leaf.out.txt`. This reproduces the structure stated as `G_{mu nu}=sinh(eta) eta_{mu nu}` in Kumar-Steinacker (2.25) only in the conformal-flat sense; I did not recompute their dilaton. The coordinates `x^mu` are functions on the leaf, so spacetime stays emergent; `eta_IJ` stays a fixed contraction.

**Heat kernel.** Factorisation `Tr e^{-s(O_s+Box_C)}=Tr e^{-sO_s} Tr_C e^{-s Box_C}` in the product class. Per mode, resummed R-coefficient factor `F(x)=int_1^inf u^-2 e^{-xu}du`. Sector weights of 005 (scalars 1/6, connection 4/6 rho R + rho^2X, ghosts -2/6): `c_TT=sum_Lambda d_Lambda[(11/12)F_Lambda^{(v)} - (1/24) sum_c F^{(c)}]`; ghost and `a^mu` share `m_Lambda^2`; transverse scalars have shifted spectrum (not computed). With item 5, the EH-type coefficient of `rho R[g_rho]` alone is `(N_tot-12)/6` times Z (positive EH-type iff N_tot>12) and the axial term adds to the TT kernel; this refines, and does not contradict, 005's statement "N_tot>24 for the TT Maxwell kernel".

**Comparison (Steinacker2023).** (i) Its background is a product with `[T^alpha,K^i]=0`; effective metric `G^{mu nu}=rho^{-2}eta E E` (4.7) = NAMCG's operator metric; it never needs `G ∝ g_induced`. (ii) Its EH term arises from the n=4 term of the maximally supersymmetric one-loop action after the first three cancel (4.16: weights 1, -1/2, -2 on traces over 10-, 16-, ghost components, i.e. 10-8-2=0 count); NAMCG's bosonic truncated `a_1` has no such cancellation, so `G_N ∝ m_K^2 rho^{-2}` (6.31) is not a NAMCG output. Importing it would require the fermion sector (changes `N_0` to 0, killing the `Lambda^4` and `Lambda^2` terms of `eq:Geff-structure`) - a sector-list decision, not derived here. (iii) Sign `c_K^2>0` rests on Euclidean target metric on K (6.20) and positive KK-mass sums. (iv) Kumar-Steinacker: modified Einstein equations with dilaton, axion and anharmonicity tensor `C_{mu nu}` (the tree-level YM action) because only the matrix embedding is varied: structurally the same as 008's rank deficit; item 5 shows the axion/torsion piece already inside the NAMCG connection sector. Not imported.

## Claim classification

- Established (exact): Theorem 1; 2m-dim leaf no-go; `X=G T T` identity; Prop. 2 (given the stated first-order formula); Lie-Poisson algebra and `K=(M^{45})^2 eta^{-1}/R^4` on the explicit orbit.
- Established numerically (perturbative, exact rationals/float): `V=d ln rho`; teleparallel identity; torsion form of X (through cubic order). Not proved to all orders.
- Conditional: heat-kernel factorisation and thresholds (Poisson limit, off-shell background, truncated diagonal kernel, Euclidean signs, 005 sector weights).
- Input/literature (abstract/section level): Steinacker2023 and Kumar-Steinacker content.
- Conjecture/unresolved: covariant-class fluctuation rank; Phi dictionary; transverse-scalar gap; G_eff.

## Proposed changes

Only `chapters/appH-microscopic-proofs.tex`; no label, priority, classification or Chapter 17 text touched. Anchor (occurs once): final sentence of the 009 paragraph "`This changes no ledger label; Problem~F remains open.`" followed by blank line and `\section{Problem G: HBEV}`. Insert the two paragraphs between them. Labels verified once: `def:matrix-coords-ext`, `app:status`, `ch:vierbein-emergence`, `eq:Geff-structure`, `thm:Geff`, `rem:ch3-trace-quadratic`, `ass:emergent-op`; no new labels, no new citations beyond existing `Steinacker2023`, `KumarSteinacker2023` (bib keys present).

```latex
\paragraph{Leaf dimension above four: fibre averages, a product factor and a conjugate-coordinate class (conditional; not closure).}
Work in the Poisson limit with matrix coordinates \(x^I\), \(I=0,\dots,D-1\), contracted with \(\eta=\mathrm{diag}(-1,1,\dots,1)\), on a symplectic leaf of dimension \(2m\ge4\), and four base functions \(y^\mu\) on the leaf. For a function \(\phi(y^\mu)\) the kinetic tensor is \(K^{\mu\nu}=\langle\eta_{IJ}V^{I\mu}V^{J\nu}\rangle\) with \(V^{I\mu}=\{x^I,y^\mu\}\) and \(\langle\cdot\rangle\) a positive average over the fibre; for a four-dimensional leaf it is \(\theta^{T}g\theta\).

\emph{Matrices as base coordinates.} Let \(y^\mu=x^\mu\), \(\mu=0,\dots,3\), so that \(V^{I\mu}=\Theta^{I\mu}\) is real and antisymmetric. Then \(K^{00}=\langle\sum_{I\ge1}(\Theta^{I0})^2\rangle\ge0\) and \(\sum_\mu K^{\mu\mu}=\langle\sum_{I\ge4}(\Theta^{I0})^2+\sum_{I\ge1,\,k\ge1}(\Theta^{Ik})^2\rangle\ge0\), whereas \(K=c\,\eta^{-1}\) has \(K^{00}=-c\) and \(\sum_\mu K^{\mu\mu}=2c\). Hence \(K\ne c\,\eta^{-1}\) for every \(D\), every compact fibre and every positive average: enlarging the leaf by a fibre does not remove the proportionality obstruction of the preceding paragraphs. For any nondegenerate real Lorentzian \(g_L\) on a leaf of dimension \(2m\), \(G_L=(\theta^{T}g_L\theta)^{-1}\) is not proportional to \(g_L\) (\(\det(g_L^{-1}\omega)<0\), while \(M^2=-c\) needs \(\det M=c^m>0\)). For a product leaf \(M\times\mathcal C\) with block-diagonal \(\theta\) and embedding, \(V^{i\mu}=0\) for the coordinates along \(\mathcal C\), so \(K\) is the tensor of the \(M\) factor, and to first order the response of \(K\) to \(\delta x^I=A^I(t)e^{ip\cdot y}\) is the four-dimensional one with amplitude \(\langle A^\mu\rangle\); transverse amplitudes and non-constant fibre parts do not enter. The rank statements of the preceding paragraph therefore hold with \(D\) the number of coordinates that vary over \(M\), and Kaluza--Klein modes enter only quadratically.

\emph{Conjugate coordinates.} The proportionality is not excluded when the base functions are not matrices. For the \(\mathrm{SO}(4,2)\) coadjoint orbit \(\mathbb{CP}^{1,2}\) with \(T^a=M^{a4}/R\) and \(y^\mu=M^{\mu5}/R\), the Lie--Poisson relation gives \(\{T^a,y^\mu\}=\pm\eta^{a\mu}M^{45}/R^2\), hence \(K^{\mu\nu}=(M^{45}/R^2)^2\eta^{\mu\nu}\) pointwise, with \(M^{45}\) a function of \(y^\mu\) (checked on an explicit realisation). This \(K\) is conformally flat, so the exact class carries one scalar function and no metric waves; whether fluctuations of \(T^a\) that are not fibre-constant supply a sufficient number of gauge-invariant functions is not computed here.

\emph{Heat kernel over a fuzzy factor.} For the product leaf with a finite fuzzy factor, the scalar operator of the Poisson-limit paragraph is \(\mathcal O_s\otimes1+1\otimes\Box_{\mathcal C}\), so each four-dimensional sector is replicated over the \(\dim\mathrm{Mat}(\mathcal H_{\mathcal C})\) modes, the mode of mass \(m\) with the threshold factor \(F(m^2/\Lambda_{\mathrm{UV}}^2)=\int_1^\infty u^{-2}e^{-m^2u/\Lambda_{\mathrm{UV}}^2}\mathrm du\in(0,1]\) multiplying the coefficient of Theorem~\ref{thm:Geff}. In the truncated expansion the curvature coefficient is thus of order \(\Lambda_{\mathrm{UV}}^2\) times the weighted number of light modes; it is not set by the Kaluza--Klein scale. The supersymmetric one-loop mechanism of~\cite{Steinacker2023}, in which the corresponding terms cancel and the Newton constant is set by a finite mixed term, rests on field content that is not part of the present sector list.

This is a statement for the Poisson limit, the stated fibre classes and off-shell backgrounds; it does not identify \(G\) or \(\eta_{\mu\nu}\) with the emergent metric of Chapter~\ref{ch:vierbein-emergence}, gives no field equation, gap of the transverse scalars, \(G_{\mathrm{eff}}\) value or sign, and does not compute the rank of the linearised Einstein operator in the conjugate-coordinate class. This changes no ledger label; Problem~F remains open.

\paragraph{Connection-sector term \(X\) as a torsion invariant (conditional; not closure).}
In the Poisson limit of Presentation~A with four matrices, let \(\omega=\Theta^{-1}\), \(e^A{}_\mu=\eta^{AB}\omega_{\mu B}\) (so \(G_{\mu\nu}=\eta_{AB}e^Ae^B\)), \(T^{A}{}_{\mu\nu}=\partial_\mu e^A{}_\nu-\partial_\nu e^A{}_\mu\), \(T_{\lambda\mu\nu}=\eta_{AB}e^A{}_\lambda T^B{}_{\mu\nu}\), and \(S_{\lambda\mu\nu}=T_{[\lambda\mu\nu]}\). Since \(\Theta^{T}G\Theta=\eta^{-1}\), the term \(X\) of the connection sector equals \(G_{\mu\nu}T^{\alpha\beta\mu}T_{\alpha\beta}{}^{\nu}\) with \(T^{\alpha\beta\mu}=\Theta^{\mu\rho}\partial_\rho\Theta^{\alpha\beta}\), a quadratic invariant of the torsion of \(e\). Using \(\partial_\mu\ln\rho=G^{\lambda\nu}T_{\lambda\mu\nu}\) and the teleparallel identity for \(\sqrt{|G|}R[G]\) one finds
\[
  \rho^2X=-2\rho R[g_\rho]-\rho\,g_\rho^{\mu\nu}\partial_\mu\ln\rho\,\partial_\nu\ln\rho+\tfrac32\rho^2S_{\lambda\mu\nu}S^{\lambda\mu\nu}+2\partial_\mu\bigl(g_\rho^{\mu\nu}\partial_\nu\rho\bigr),
\]
verified pointwise through third order in the Poisson-class perturbation used in the preceding Presentation~A paragraph, for both signatures; it is not proved to all orders. The \(\eta\)-using rewriting of \(X\) left untested above is therefore the squared totally antisymmetric torsion. With \(N_{\mathrm{tot}}\) as above, the coefficient of \(\rho R[g_\rho]\) in the Euclidean \(\Lambda_{\mathrm{UV}}^2\) functional is \((N_{\mathrm{tot}}-12)/6\) times that of a single scalar's \(\tfrac16\), and the torsion term contributes to the transverse-traceless kernel; this does not alter the quadratic statement above.

This is a computation for the Poisson-limit operators of the preceding paragraphs. It does not identify \(G\) with the emergent metric of Chapter~\ref{ch:vierbein-emergence}, does not treat Moyal corrections, fermions or other fields, and gives no value or sign of \(G_{\mathrm{eff}}\). This changes no ledger label; Problem~F remains open.
```

Stale passages elsewhere: none found by grep (009 paragraph's sentence "leaf of dimension greater than four is the hypothesis ... relaxed" stays true; refined by new paragraph). One check needed by gatekeeper: the "(N_tot-12)/6" sentence is awkward; if rejected, drop that last sentence of paragraph 2 (it is derived: scalars `N_s/6`, connection+ghost `2/6`, so coefficient `N_tot/6-2`).

## Verification scripts

In `proposals/011-fuzzy-leaf/` (outputs saved as `.out.txt`): `check_zero_mode_nogo.py` (Thm 1 symbolic + random + optimisation; 2m-dim determinant); `check_product_kk.py` (product response rank 3, F(x), n^2 count); `check_covariant_leaf.py` (explicit su(2,2) orbit: Lie-Poisson constant, `E=s eta M^{45}`, `K`, ranks, `x_a x^a`, Monte-Carlo fibre average; Monte-Carlo residual 0.004 is sampling noise); `check_torsion_decomposition.py` + `base005.py` (verbatim copy of 005 framework): exact `X=GTT`, fits (cubic: `h,r,S` residual 1e-16, `h,r` alone 0.27); `check_torsion_pointwise.py` (ratio Res/TD = 2.000 for all masks); `check_teleparallel_chain.py` (V=dlnrho, teleparallel, conformal relation, S^2 algebra). Anchor/label counts above were run with grep (all 1).

## Decisions Taken

- Chose to treat the leaf-dimension question as "which functions are the base coordinates", because Theorem 1 shows dimension alone is inert; favours the full-GR route by pointing to the conjugate-coordinate (covariant) class as the only one where the obstruction is absent.
- Did not add a new Chapter 3 definition (avoids a definition change and full-scan trigger); all text in appH. Rejected: a new `def:` for fibred leaves (premature before the fluctuation rank is known).
- Did not import Steinacker's G_N formula or sign; recorded the SUSY-cancellation difference instead.
- Included the torsion identity here (shared Poisson-limit derivation chain and Steinacker comparison); rejected splitting it into a separate package.

## Milestone assessment

M2 (bounded no-go: leaf enlargement with matrices as base coordinates cannot remove `G != c g`, kept open by 008/009 text). Also a sub-lemma for F (torsion form of X) and a structural pointer for the next package; no breakthrough claimed.

## Status-label recommendation

None. A, B, C, D1, E, F, G-derived, N remain as in Appendix H / Chapter 17 (OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL).

## Author decision needed

None. (Noted, for the author's information only: adding the IKKT fermion/ghost content to the F sector list would set `N_0=0`; this is a sector-list choice that would change `eq:Geff-structure`'s `Lambda^2` and `Lambda^4` terms and is not proposed.)

## Remaining open step

(a) Linearised response and Einstein-operator rank in the covariant conjugate-coordinate class (s>=1 harmonics) with an explicit fluctuation basis on `CP^{1,2}`; (b) derive the extra conserved stress (anharmonicity/axion sector) from the same action and show whether it closes the 3-vs-6 deficit; (c) prove the torsion identity of item 5 to all orders; (d) transverse-scalar spectrum and gap; (e) Phi-to-coframe dictionary in the conjugate class; (f) derived signature (E), D1 dynamics, G_eff.

## Special instructions for the gatekeeper

- Must not be asserted: that the leaf relaxation closes F; that `G ∝ g_induced` holds for matrix base coordinates; that Prop. 3 gives metric dynamics; Steinacker's G_N as NAMCG output; any label change.
- Re-check: Theorem 1 inequalities (hand proof short); the claim "`tr S` time-row cancellation"; Prop. 3 sign `s` (irrelevant to K); that torsion identity is stated only through third order; the `(N_tot-12)/6` sentence (derived from 005 weights, drop if doubtful); normalisation matches with Steinacker are marked unverified.
- Literature: Steinacker2023 read at page level listed above; 2601.08031 abstract only.
