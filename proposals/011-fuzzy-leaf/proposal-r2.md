# Proposal 011-fuzzy-leaf, round 2

## Changelog against r1 (every finding of review-r1 addressed)

| Finding | Action in r2 |
|---|---|
| F1 (major) leaf-level det argument wrong for c<0, false at 2m=2 | Replaced by the c>0 / c<0 split (review snippet, re-derived below); restricted to `2m>=4`; `check_zero_mode_nogo.py` item (d) rewritten (exact 2m=2 counterexample `K=-4 g^{-1}` printed, c>0 determinant sign for 2m=2,4,6, Witt-index statement), re-run, output saved. |
| F2 (major) "(N_tot-12)/6" sentence | Deleted; replaced by the linear-dependence sentence (restricted to the Poisson-class perturbations about constant `Theta-bar`); net coefficient `1-N_tot/24` stays. The "(N_tot-12)/6" remark is removed also from this file. |
| F3 torsion identity wording / stronger claim | Outcome: **the identity is now proved** (chain (i)-(v) below, all steps by hand except the classical teleparallel identity, which is textbook and whose signs/coefficients are verified exactly). New script `check_torsion_exact.py`: exact rational arithmetic, finite-amplitude generic 2-jets of a closed `omega`, 12 cases (both signatures), every step and the final identity pass with `==`. The "checked numerically through third order" sentence is therefore replaced by the proved statement; the soft wording "a rewriting using the coframe `e=eta^{-1}omega` is the squared axial torsion" is used as required. |
| F4 index conventions; ambiguous "preceding Presentation A paragraph" | Stated: `alpha,beta` (matrix indices) lowered/raised with `eta`, coordinate indices and `S^2` with `G`; explicit description of the Poisson-limit paragraph replaces the vague reference. |
| F5 CP^{1,2} | Invariant form `diag(-,+,+,+,+,-)` stated; `y^mu=M^{mu5}/R` not among the four matrix coordinates; `eta^{mu nu}` is the Cartesian form of the `y^mu`; leaf lies outside the four-dimensional leaf of `def:matrix-coords-ext`; matrix-induced tensor on the leaf has rank 4; dictionary for `y^mu` not derived. |
| F6 | "`c != 0`", K=0 exclusion sentence, "in this class" added. |
| F7 | The closing status sentence stays only on the last paragraph. |

## Result

Target: the leaf-dimension relaxation (4+k-dimensional symplectic leaf) named in 008/009 as the within-core route past `G != c g`. All results are kinematic or conditional; nothing on the critical path is derived.

1. **Bounded no-go (Theorem 1), exact.** Hypotheses: real `Theta`, `eta=diag(-1,1,...,1)`, the four base coordinates `y^mu` are four of the D matrix coordinates (`y^mu=x^mu`), any D, any leaf dimension, any compact fibre, any positive fibre measure. Then the fibre average `K^{mu nu}=<Theta^{I mu}eta_{IJ}Theta^{J nu}>` has `K^{00}>=0` and `tr K>=0`, so `K=c eta^{-1}` forces `c=0`; `K=0` forces `Theta^{I mu}=0` (the `x^mu` Casimirs), contradicting nondegeneracy. Hence in this class `K != c eta^{-1}` for every `c != 0`, and enlarging the leaf by a fibre does not remove the obstruction. Leaf-level companion (corrected, F1): for a real Lorentzian `g_L` on a leaf of dimension `2m>=4`, `K=theta^T g_L theta != c g_L^{-1}` for `c != 0`; at `2m=2` a solution exists (`c=-4`).
2. **Product class.** For `M^4 x C` with block-diagonal data, `K` is that of the `M` factor; first-order response is the 4D one with amplitude `<A^mu>`; rank statements of 009 hold with D the number of coordinates varying over M.
3. **Where the obstruction is absent.** `CP^{1,2}` coadjoint orbit of SO(4,2), `T^a=M^{a4}/R`, base functions `y^mu=M^{mu5}/R` (not matrices): `K^{mu nu}=(M^{45}/R^2)^2 eta^{mu nu}` pointwise. Conformally flat; Einstein rank not computed; the dictionary `y^mu=M^{mu5}` is not derived.
4. **Heat kernel over a fuzzy factor (conditional).** Unchanged from r1.
5. **Connection-sector term X: now a proved identity.** For real nondegenerate `Theta` with `omega=Theta^{-1}` closed (Jacobi), `eta` of either signature,
   `rho^2 X = -2 rho R[g_rho] - rho g_rho^{mu nu} d_mu ln rho d_nu ln rho + (3/2) rho^2 S_{lmn}S^{lmn} + 2 d_mu(g_rho^{mu nu} d_nu rho)`,
   exactly, pointwise (not only perturbatively). Proof in "Research and reasoning". It adds a re-expression of the existing term X; it derives no heat-kernel coefficient, no `G_eff`, no discharge of `ass:emergent-op`.

Not established: any field equation for G; Einstein rank in the covariant class; gap of transverse scalars; `Phi`=coframe; any `G_eff` value or sign.

## Target and status

Problem F (`ass:emergent-op`, primary); A, D1, E by dependency. Appendix H: F "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL" (as quoted in review-r1, re-read this round at the ledger paragraph); Chapter 17 criterion lists A, B, C, D1, E, F, G-derived, N; no discrepancy found. Original target (F): discharge `ass:emergent-op` or replace it by a derived ingredient: NOT met. PROGRAMME-CONDITIONAL. A, B, C, D1, E, F, G-derived and N all stay OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL.

## Source reading

Digest CURRENT (as stated by the orchestrator). Targeted reads: all of review-r1.md and proposal-r1.md; appH lines 1800-1837 (009 paragraphs and anchor, re-read now); grep of labels/anchor/bib keys; all scripts of the folder. Literature as in r1: Steinacker2023 (arXiv:2303.08012) read at page level in r1; the review verified its (4.13), (4.16)-(4.18) and (7.19)-(7.24) at equation level; Kumar-Steinacker (2312.01317) and Steinacker2026 (2601.08031) not independently verified and not used in the proposed text. Not a full scan; no definition, assumption, scope or status text is changed.

## Research and reasoning

**Theorem 1 and the leaf-level companion (F1, F6).** With `y^mu=x^mu`, `V^{I mu}=Theta^{I mu}` is antisymmetric, `K^{00}=sum_{I>=1}(Theta^{I0})^2>=0`, `tr K=sum_{I>=4}(Theta^{I0})^2+sum_{I>=1,k>=1}(Theta^{Ik})^2>=0` (time-row term `-(Theta^{0k})^2` cancels `(Theta^{k0})^2`). `c eta^{-1}` has `K^{00}=-c`, `tr=2c`: both signs of c excluded, so c=0; then both sums vanish, all `Theta^{I mu}=0` for `mu<=3`, contradicting nondegeneracy.
Leaf-level: `K=theta^T g theta=-theta g theta`, so `K=c g^{-1}` is `N^2=-c I` for `N=theta g`. `c>0`: `det N=c^m>0`, but `det N=Pf(theta)^2 det g<0`. `c<0`: `N^T g=-g N` (since `theta^T=-theta`, `g^T=g`) so for eigenvectors `u,u'` with eigenvalue `+sqrt|c|` one has `2 sqrt|c| g(u,u')=0`: each of the two real eigenspaces (`N^2=|c|` makes N diagonalisable over R) is totally null; a Lorentzian form has Witt index 1, so each has dimension <=1 and `2m<=2`. For `2m=2`, `g=diag(-1,1)`, `theta=2 eps` gives `K=-4g^{-1}`, so the restriction `2m>=4` is necessary (script item (d)). The r1 determinant argument alone fails for `c<0`, m odd.

**Torsion identity: proof (F3).** Setting: four matrix coordinates, `Theta` real nondegenerate Poisson (Jacobi), `omega=Theta^{-1}`, so `d omega=0` where, because there are four matrices and four coordinates, matrix indices and coordinate indices are identified. `eta` lowers/raises matrix indices `A,B,alpha,beta`; `G_{mu nu}=eta_{AB}e^A_mu e^B_nu` with `e^A_mu=eta^{AB}omega_{mu B}`, i.e. `G=omega eta^{-1} omega^T`, `G^{-1}=Theta^T eta Theta=K`; `rho=|Pf omega|` (so `rho^2=sqrt|G|`); `g_rho=G/rho` is unimodular, `g_rho^{mu nu}=rho K^{mu nu}`. `T^A_{mu nu}=d_mu e^A_nu-d_nu e^A_mu`, `T_{lmn}=eta_{AB}e^A_l T^B_{mn}`, `V_mu=G^{ln}T_{lmn}`, `I_A=T_{lmn}T^{lmn}`, `I_B=T_{lmn}T^{mln}`, `S_{lmn}=T_{[lmn]}`, indices on T, S, V raised with G. `X=eta^{rl}eta_{ma}eta_{nb}d_rTheta^{mn}d_lTheta^{ab}`.
(i) `d omega=0` gives `T^A_{mu nu}=-eta^{AB}d_B omega_{mu nu}`. Using `d_rTheta=-Theta(d_r omega)Theta` and `Theta^T eta Theta=G^{-1}`, `X=eta^{EF}d_E omega_{mu nu}d_F omega_{mu'nu'}G^{mu mu'}G^{nu nu'}`. Also `e G^{-1}e^T=eta^{-1}` gives `I_A=eta_{BD}G^{mu mu'}G^{nu nu'}T^B_{mu nu}T^D_{mu'nu'}` = the same. So **`X=I_A`**.
(ii) `G^{ln}omega_{lB}=eta_{BC}Theta^{C n}` gives `V_mu=Theta^{nu C}d_C omega_{mu nu}`. From `d omega=0`: `d_sigma ln Pf omega=½Theta^{nu mu}d_sigma omega_{mu nu}=-Theta^{nu mu}d_mu omega_{nu sigma}`. Then `d_beta Theta^{alpha beta}=-Theta^{alpha a}(d_beta omega_{ab})Theta^{b beta}=-Theta^{alpha a}d_a ln Pf omega`, and `V_mu=-omega_{mu alpha}d_beta Theta^{alpha beta}=d_mu ln Pf omega`. So **`V_mu=d_mu ln rho`**.
(iii) Teleparallel identity (classical; flatness of the Weitzenboeck connection `e_A^l d_m e^A_n`, Levi-Civita plus contortion): `R[G]=-(I_A/4+I_B/2-V^2)-2 nabla_mu V^mu`, valid for any coframe. Checked exactly (below), including the signs and coefficients in my index convention, for closed and for generic non-closed coframes.
(iv) `S^2=(1/3)(I_A-2I_B)` (algebra: `S_{lmn}=(T_{lmn}+T_{mnl}+T_{nlm})/3`, `T_{lmn}T^{mnl}=-I_B`). Then `I_B=(I_A-3S^2)/2` and (iii) gives `I_A=-2R[G]+(3/2)S^2+2V^2-4 nabla_mu V^mu`.
(v) `G=rho g_rho` in 4D: `R[G]=rho^{-1}(R[g_rho]-3 Box_{g_rho}ln rho-(3/2)|grad ln rho|^2_{g_rho})`; `g_rho` unimodular, so `rho Box ln rho=d(g_rho^{mu nu}d_nu rho)-rho|grad ln rho|^2`. Hence `rho^2 R[G]=rho R[g_rho]+(3/2)rho|grad ln rho|^2-3 td`, `td:=d_mu(g_rho^{mu nu}d_nu rho)`; with (ii), `rho^2 V^2=rho|grad ln rho|^2_{g_rho}` and `rho^2 nabla_mu V^mu=td` (since `sqrt|G| G^{mu nu}V_nu=rho^2 rho^{-1}g_rho^{mu nu}d_nu rho/rho=g_rho^{mu nu}d_nu rho`).
Combine: `rho^2 X=rho^2 I_A=-2(h+(3/2)r-3td)+(3/2)rho^2 S^2+2r-4td=-2h-r+(3/2)rho^2S^2+2td`, `h=rho R[g_rho]`, `r=rho|grad ln rho|^2`. QED.
The classical step (iii) is the only imported ingredient; it is textbook (not independently looked up this round: not verified against a source), and the exact script tests it in the form used. Consequently the identity is classified: **derived (given the classical teleparallel identity), exactly checked on finite-amplitude jets**; the r1 "third order only" limitation is lifted. `X=I_A` and `V=d ln rho` are proved above (not assumed).

**Effect on 005 (F2).** The identity only re-expresses X. At quadratic order about constant `Theta-bar` (the Poisson-class perturbations of the 005 paragraph) 005 already finds `rho^2X` in the span of `h,r` mod td, so `S^2` is in the span there; the decomposition into `h,r,S^2` is basis dependent and does not alter the net coefficient `1-N_tot/24` of the TT kernel. The r1 "(N_tot-12)/6" statement is withdrawn.

**Other items** (Prop. 2, CP^{1,2} algebra, heat kernel, Steinacker comparison): as in r1 and accepted by the review; the CP^{1,2} text is corrected as in F5. `{M^{a4},M^{mu5}}=s eta^{a mu}M^{45}` because `eta^{45}=eta^{a5}=eta^{4mu}=0`; `K^{mu nu}=eta_{ab}eta^{a mu}eta^{b nu}(M^{45})^2/R^4=(M^{45}/R^2)^2eta^{mu nu}`; the matrix-induced tensor on the six-dimensional leaf has rank 4 (script), which is why Theorem 1 (a statement about four matrix coordinates) does not apply.

## Claim classification

- Established (exact): Theorem 1 (hypotheses as stated, `c != 0`, K=0 excluded); leaf-level no-go for `2m>=4` (c>0 determinant, c<0 totally null eigenspaces), 2m=2 counterexample; `X=I_A`; `V=d ln rho`; the torsion identity given the classical teleparallel identity; CP^{1,2} Lie-Poisson algebra and `K=(M^{45}/R^2)^2eta^{-1}`; Prop. 2 given its first-order formula.
- Established (exact rational check, not a proof of the classical step): teleparallel identity in the stated convention; whole chain on 12 finite-amplitude cases.
- Conditional: heat-kernel factorisation and thresholds.
- Input/literature: Steinacker2023 statements (SUSY cancellation, G_N from mixed term; verified by gatekeeper at equation level in r1 review); Kumar-Steinacker not verified.
- Conjecture/unresolved: Einstein rank in the covariant class; why `y^mu=M^{mu5}` are base functions; Phi dictionary; transverse-scalar gap; `G_eff`.

## Proposed changes

Only `chapters/appH-microscopic-proofs.tex`; no label, priority, classification or Chapter 17 text touched; no new labels or citations. Anchor (occurs once, line 1835, followed by a blank line and `\section{Problem G: HBEV}` at line 1837): the final sentence "This changes no ledger label; Problem~F remains open." of the 009 paragraph "More than four matrix coordinates in the Poisson limit: linear response". Insert the two paragraphs after it (before the `\section`). Labels re-verified to occur once in `.tex`: `def:matrix-coords-ext` (ch03:173), `ch:vierbein-emergence`, `eq:Geff-structure`, `thm:Geff`, `ass:emergent-op`; bib keys `Steinacker2023` (bib:121), `KumarSteinacker2023` (bib:393; not used in the text below).

```latex
\paragraph{Leaf dimension above four: fibre averages, a product factor and a conjugate-coordinate class (conditional; not closure).}
Work in the Poisson limit with matrix coordinates \(x^I\), \(I=0,\dots,D-1\), contracted with \(\eta=\mathrm{diag}(-1,1,\dots,1)\), on a symplectic leaf of dimension \(2m\ge4\), and four base functions \(y^\mu\) on the leaf. For a function \(\phi(y^\mu)\) the kinetic tensor is \(K^{\mu\nu}=\langle\eta_{IJ}V^{I\mu}V^{J\nu}\rangle\) with \(V^{I\mu}=\{x^I,y^\mu\}\) and \(\langle\cdot\rangle\) a positive average over the fibre; for a four-dimensional leaf it is \(\theta^{T}g\theta\).

\emph{Matrices as base coordinates.} Let \(y^\mu=x^\mu\), \(\mu=0,\dots,3\), so that \(V^{I\mu}=\Theta^{I\mu}\) is real and antisymmetric. Then \(K^{00}=\langle\sum_{I\ge1}(\Theta^{I0})^2\rangle\ge0\) and \(\sum_\mu K^{\mu\mu}=\langle\sum_{I\ge4}(\Theta^{I0})^2+\sum_{I\ge1,\,k\ge1}(\Theta^{Ik})^2\rangle\ge0\), whereas \(K=c\,\eta^{-1}\) has \(K^{00}=-c\) and \(\sum_\mu K^{\mu\mu}=2c\); hence \(c=0\). The case \(K=0\) forces \(\Theta^{I\mu}=0\) for \(\mu\le3\), so the \(x^\mu\) would be Casimir functions, contradicting nondegeneracy. Therefore \(K\ne c\,\eta^{-1}\) for every \(c\ne0\), for every \(D\), every compact fibre and every positive average: in this class, enlarging the leaf by a fibre does not remove the proportionality obstruction of the preceding paragraphs. For any nondegenerate real Lorentzian \(g_L\) on a leaf of dimension \(2m\ge4\), \(G_L=(\theta^{T}g_L\theta)^{-1}\) is not proportional to \(g_L\). Indeed \(K=c\,g_L^{-1}\) with \(c\neq0\) gives \(N^2=-c\,\mathbb I\) for \(N=\theta g_L\). For \(c>0\), \(\det N=c^m>0\), whereas \(\det N=(\operatorname{Pf}\theta)^2\det g_L<0\). For \(c<0\), \(N\) is \(g_L\)-skew with \(N^2=|c|\,\mathbb I\), so its \(\pm\sqrt{|c|}\) eigenspaces are totally null and have dimension at most one in Lorentzian signature, which forces \(2m\le2\); for \(2m=2\) the relation can hold (\(g_L=\mathrm{diag}(-1,1)\), \(\theta=2\epsilon\) gives \(K=-4g_L^{-1}\)). For a product leaf \(M\times\mathcal C\) with block-diagonal \(\theta\) and embedding, \(V^{i\mu}=0\) for the coordinates along \(\mathcal C\), so \(K\) is the tensor of the \(M\) factor, and to first order the response of \(K\) to \(\delta x^I=A^I(t)e^{ip\cdot y}\) is the four-dimensional one with amplitude \(\langle A^\mu\rangle\); transverse amplitudes and non-constant fibre parts do not enter. The rank statements of the preceding paragraph therefore hold with \(D\) the number of coordinates that vary over \(M\), and Kaluza--Klein modes enter only quadratically.

\emph{Conjugate coordinates.} The proportionality is not excluded when the base functions are not among the matrix coordinates. Let \(M^{AB}\), \(A,B=0,\dots,5\), generate \(\mathfrak{so}(4,2)\) with invariant form \(\mathrm{diag}(-,+,+,+,+,-)\) on the coadjoint orbit \(\mathbb{CP}^{1,2}\) (six-dimensional leaf), take the four matrix coordinates \(T^a=M^{a4}/R\), \(a=0,\dots,3\), and the base functions \(y^\mu=M^{\mu5}/R\). The functions \(y^\mu\) are not among the \(T^a\), and the leaf is not the four-dimensional leaf of Definition~\ref{def:matrix-coords-ext}. The Lie--Poisson relation gives \(\{T^a,y^\mu\}=\pm\eta^{a\mu}M^{45}/R^2\), because the form has \(\eta^{45}=\eta^{a5}=\eta^{4\mu}=0\), hence \(K^{\mu\nu}=(M^{45}/R^2)^2\eta^{\mu\nu}\) pointwise, with \(M^{45}\) a function of \(y^\mu\) on the orbit (checked on an explicit realisation). Here \(\eta^{\mu\nu}\) is the Cartesian form of the functions \(y^\mu\), not the pull-back of the matrix contraction \(\eta_{IJ}\), and the matrix-induced tensor on the six-dimensional leaf has rank four. This \(K\) is conformally flat, so the exact class carries one scalar function and no metric waves; whether fluctuations of \(T^a\) that are not fibre-constant supply a sufficient number of gauge-invariant functions is not computed here, and no argument is given that the \(y^\mu=M^{\mu5}/R\) are the base functions of the reduced theory.

\emph{Heat kernel over a fuzzy factor.} For the product leaf with a finite fuzzy factor, the scalar operator of the Poisson-limit paragraph is \(\mathcal O_s\otimes1+1\otimes\Box_{\mathcal C}\), so each four-dimensional sector is replicated over the \(\dim\mathrm{Mat}(\mathcal H_{\mathcal C})\) modes, the mode of mass \(m\) with the threshold factor \(F(m^2/\Lambda_{\mathrm{UV}}^2)=\int_1^\infty u^{-2}e^{-m^2u/\Lambda_{\mathrm{UV}}^2}\mathrm du\in(0,1]\) multiplying the coefficient of Theorem~\ref{thm:Geff}. In the truncated expansion the curvature coefficient is thus of order \(\Lambda_{\mathrm{UV}}^2\) times the weighted number of light modes; it is not set by the Kaluza--Klein scale. The supersymmetric one-loop mechanism of~\cite{Steinacker2023}, in which the corresponding terms cancel and the Newton constant is set by a finite mixed term, rests on field content that is not part of the present sector list.

This is a statement for the Poisson limit, the stated fibre classes and off-shell backgrounds; it does not identify \(G\) or \(\eta_{\mu\nu}\) with the emergent metric of Chapter~\ref{ch:vierbein-emergence}, gives no field equation, gap of the transverse scalars, \(G_{\mathrm{eff}}\) value or sign, and does not compute the rank of the linearised Einstein operator in the conjugate-coordinate class.

\paragraph{Connection-sector term \(X\) as a torsion invariant (conditional; not closure).}
Take the setting of the Poisson-limit paragraph on Presentation~A above: four matrix coordinates, a real nondegenerate \(\Theta\) with Jacobi identity, \(\eta=\mathrm{diag}(-1,1,1,1)\) or \(\mathrm{diag}(1,1,1,1)\), \(K^{\mu\nu}=\eta_{\alpha\beta}\Theta^{\alpha\mu}\Theta^{\beta\nu}\), \(G=K^{-1}\), \(\rho=1/|\operatorname{Pf}\Theta|\), \(g_\rho^{\mu\nu}=\rho K^{\mu\nu}\). Let \(\omega=\Theta^{-1}\) (closed), \(e^A{}_\mu=\eta^{AB}\omega_{\mu B}\) so that \(G_{\mu\nu}=\eta_{AB}e^Ae^B\), \(T^{A}{}_{\mu\nu}=\partial_\mu e^A{}_\nu-\partial_\nu e^A{}_\mu\), \(T_{\lambda\mu\nu}=\eta_{AB}e^A{}_\lambda T^B{}_{\mu\nu}\) and \(S_{\lambda\mu\nu}=T_{[\lambda\mu\nu]}\). The matrix indices \(\alpha,\beta,A,B\) are lowered and raised with \(\eta\); coordinate indices, and \(S_{\lambda\mu\nu}S^{\lambda\mu\nu}\), with \(G\). The term \(X\) of the connection sector is \(X=\eta^{\rho\lambda}\eta_{\mu\alpha}\eta_{\nu\beta}\partial_\rho\Theta^{\mu\nu}\partial_\lambda\Theta^{\alpha\beta}\). Since \(\Theta^{T}\eta\,\Theta=G^{-1}\) and \(\partial\Theta=-\Theta(\partial\omega)\Theta\), \(X=G_{\mu\nu}T^{\alpha\beta\mu}T_{\alpha\beta}{}^{\nu}\) with \(T^{\alpha\beta\mu}=\Theta^{\mu\rho}\partial_\rho\Theta^{\alpha\beta}\), and \(X=T_{\lambda\mu\nu}T^{\lambda\mu\nu}\) because \(d\omega=0\) gives \(T^A{}_{\mu\nu}=-\eta^{AB}\partial_B\omega_{\mu\nu}\). Moreover \(\partial_\mu\ln\rho=G^{\lambda\nu}T_{\lambda\mu\nu}\), which follows from \(d\omega=0\) through \(\partial_\sigma\ln\operatorname{Pf}\omega=-\Theta^{\nu\mu}\partial_\mu\omega_{\nu\sigma}\). With the classical teleparallel identity \(R[G]=-\bigl(\tfrac14T_{\lambda\mu\nu}T^{\lambda\mu\nu}+\tfrac12T_{\lambda\mu\nu}T^{\mu\lambda\nu}-V_\mu V^\mu\bigr)-2\nabla_\mu V^\mu\), \(V_\mu=G^{\lambda\nu}T_{\lambda\mu\nu}\), the relation \(S_{\lambda\mu\nu}S^{\lambda\mu\nu}=\tfrac13\bigl(T_{\lambda\mu\nu}T^{\lambda\mu\nu}-2T_{\lambda\mu\nu}T^{\mu\lambda\nu}\bigr)\), and the conformal transformation \(G=\rho\,g_\rho\) with \(\det g_\rho=1\), one finds the exact pointwise identity
\[
  \rho^2X=-2\rho R[g_\rho]-\rho\,g_\rho^{\mu\nu}\partial_\mu\ln\rho\,\partial_\nu\ln\rho+\tfrac32\rho^2S_{\lambda\mu\nu}S^{\lambda\mu\nu}+2\partial_\mu\bigl(g_\rho^{\mu\nu}\partial_\nu\rho\bigr).
\]
A rewriting using the coframe \(e=\eta^{-1}\omega\) is therefore the squared axial torsion. The identity was also verified in exact rational arithmetic on finite-amplitude generic two-jets of a closed \(\omega\) for both signatures. At quadratic order about constant \(\bar\Theta\), for the perturbations of the Poisson class, the invariants \(\rho R[g_\rho]\), \(\rho\,g_\rho^{\mu\nu}\partial_\mu\ln\rho\,\partial_\nu\ln\rho\) and \(\rho^2S_{\lambda\mu\nu}S^{\lambda\mu\nu}\) are linearly dependent, so this decomposition does not alter the net coefficient \(1-N_{\mathrm{tot}}/24\) stated above.

This is a statement for the Poisson-limit operators of the preceding paragraphs. It does not identify \(G\) with the emergent metric of Chapter~\ref{ch:vierbein-emergence}, does not treat Moyal corrections, fermions or other fields, and gives no value or sign of \(G_{\mathrm{eff}}\). This changes no ledger label; Problem~F remains open.
```

Stale passages elsewhere: none found. The 005 sentence that the eta-using rewritings of X are untested (appH, 005 paragraph) remains true as a statement about 005's own scope and is now supplemented; the gatekeeper may judge whether one clause there should be cross-referenced (no edit proposed).

## Verification scripts

In `proposals/011-fuzzy-leaf/`:
- `check_torsion_exact.py` -> `check_torsion_exact.out.txt` (new): exact rational jets, 12 cases (6 seeds x sig=+-1), checks `|det G|=rho^4`, (i) `X=I_A`, (ii) `V=d ln rho`, (iii) teleparallel identity (also for generic non-closed coframes), (iv) conformal relation, (v) `S^2` algebra, (vi) final identity; all `True`, lhs=rhs printed.
- `check_zero_mode_nogo.py` -> `check_zero_mode_nogo.out.txt` (item (d) rewritten and re-run): Theorem 1 (a)-(c) unchanged; (d) 2m=2 counterexample, c>0 determinant sign for 2m=2,4,6, null-eigenvector check, Witt index.
- Unchanged from r1 (outputs saved): `check_product_kk.py`, `check_covariant_leaf.py`, `check_torsion_decomposition.py` + `base005.py`, `check_torsion_pointwise.py`, `check_teleparallel_chain.py`. The perturbative third-order checks are superseded by the exact script; they remain as cross-checks. The reviewer's `allorders.py` (float, finite amplitude) is consistent with the exact script.
- Anchor and labels: grep counts re-run this round (anchor sentence 1 occurrence, line 1835; `\section{Problem G: HBEV}` line 1837; each label once in `.tex`).

## Decisions Taken

- Attempted the all-orders proof (F3, "strongly recommended"): it succeeded modulo the classical teleparallel identity, so the identity is stated as derived rather than numerically checked; the classical step is explicitly flagged. Alternative rejected: keeping "checked numerically" (would understate a verifiable derivation).
- Kept the torsion paragraph in this package (shared Poisson-limit chain), as the review allowed.
- Used "c != 0" and the explicit K=0 exclusion rather than weakening the theorem.
- Removed the "(N_tot-12)/6" content completely rather than rephrasing.
- No new definition, no label change, no new bib entry.

## Milestone assessment

M2 (bounded no-go: leaf enlargement with matrices as base coordinates cannot remove `G != c g`; hypothesis class stated: real Theta, `y^mu` four of the matrix coordinates, positive fibre average, `c != 0`; relaxation routes: y^mu not matrices (CP^{1,2}), non-positive/complex data, fibre dynamics). The torsion identity is a proved sub-lemma re-expressing X; not claimed as a breakthrough.

## Status-label recommendation

None. A, B, C, D1, E, F, G-derived and N remain OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL as in Appendix H / Chapter 17.

## Author decision needed

None.

## Remaining open step

Pointer only; ranked by impact on the infrared / full-GR derivation:
1. **Einstein-operator rank in the CP^{1,2} conjugate-coordinate class** (explicit s>=1 fluctuation basis, linearised `K` or `G`, gauge-invariant function count versus the conserved-stress count). This is the only route in which the 008/009 obstruction is absent, and it is concrete and computable; its outcome (rank deficit or not) decides whether step 2 is worth pursuing. Rank 1.
2. **Derive why `y^mu=M^{mu5}` are the base functions** (a dictionary from the matrix theory, with `T^a` momentum-like and `y^mu` conjugate). Required for the class to count as derived rather than chosen, but without step 1 it risks being a derivation of a class that fails the rank test. Rank 2.
3. Subsequent: extra conserved stress from the same action (anharmonicity/axion sector), transverse-scalar spectrum and gap, `Phi`-to-coframe dictionary, derived signature (E), D1 dynamics, `G_eff`.

## Special instructions for the gatekeeper

- Must not be asserted: that the leaf relaxation closes F; that `G proportional to g_induced` holds for matrix base coordinates; that the CP^{1,2} class gives metric dynamics or that `y^mu=M^{mu5}` is derived; Steinacker's G_N as NAMCG output; any label change.
- Re-check: (1) the c>0/c<0 argument (note `N=theta g` real with `N^2=|c|>0` is diagonalisable over R; eigenspace dimensions need not be equal; Witt index of Lorentzian form is 1); (2) steps (i), (ii), (v) of the torsion proof by hand, and `check_torsion_exact.py`; (3) the one imported classical identity (iii), its sign convention `V_mu=G^{ln}T_{lmn}` and `-2 nabla V`; (4) the sentence on linear dependence at quadratic order (relies on 005's quadratic-order statement that `rho^2 X` lies in the span of `h,r` mod td, plus the identity); (5) anchor/label counts; (6) the new text uses `\ref` only for existing labels and `\cite{Steinacker2023}` only.
- Literature: Kumar-Steinacker and Steinacker2026 not independently verified and not cited in the proposed text.
