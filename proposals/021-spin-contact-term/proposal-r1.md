# Proposal 021-spin-contact-term, round 1

## Result
Bounded no-go plus localisation of the missing ingredient. Problem B stays open; nothing is closed.

1. **Direction of the spin term (established algebra).** The spin term is not missing from the area side; it is what creates the gap. The antiperiodic Dirac cone value +1/3 equals the unrotated / (G,rho,dTheta)-reading value -2/3 plus +1 per Dirac field, and that +1 is exactly the Lichnerowicz contact of the R_G/4 term. `dirac_lichnerowicz.py` gives tr E_f/4 = R_G/4 - T^2/16 + T T'/8 (residual 3e-13, 7 random closed omega), i.e. Q_f = 1/4 per component in the torsion reading (scalar: +T^2/16). `cone_contact_bookkeeping.py` gives (AP - P)'(1) = 1/2 = 2 Q_f per two-component block. The Larsen-Wilczek / xi R-type term is therefore already inside c_A = ... + n_D/3 and cannot be added again. Double counting with the 015 Q=0 statement is avoided as follows: Q=0 refers to the endomorphism E in (G,rho,dTheta) variables on the pulled-back cover, whereas the spin excess is the holonomy/gluing of the connection; they are the same number at n=1, not two terms. It raises c_A; closing needs c_A to fall by 2.
2. **First-order Weitzenboeck identity (established, exact symbolic).** For omega = omega_bar + eps dA (any constant omega_bar, any A): R_G^(1) = -2 Box delta ln rho and rho R[g_rho]^(1) = -(1/2) rho^2 R_G^(1) (`firstorder_poisson.py`). Hence a first-order smooth conical deficit of a Poisson structure forces ln rho to carry flux through Sigma (rho singular); the 015/017/019 replica (pull-back, rho regular, cone on G) is not a limit of smooth Poisson structures. For the smooth first-order replica Q = 1/4 in every sector (the -1/2 factor of 015, now branch-free) and c_A^sm = -N_tot/12. For Dirac fields this reproduces +1/3 with no gluing assumption, an independent support for the 019 fermion value. Identity: c_A^sm = c_A(AP) - (1/4)(N_s+2). The two readings differ by the total derivative 3c Box delta ln rho, i.e. by the flux of grad ln rho through Sigma.
3. **Outcome at (n_D, N_s) = (2, 6) (c_T = 0, N_tot = 0).** Fixed-state AP: c_A = 2. AP plus a Kabat/Donnelly-Wall vector contact (-1): 1. Smooth first-order: 0. The 0 is 0 = 0 for every sector-uniform Q because N_tot = 0 (same character as the 019 periodic coincidence); it is not a derivation. Standard contacts have weight +1 per Dirac (included), -1 vector, 0 scalars/ghosts, so at most c_A = 1. No known contact/edge term closes the gap non-vacuously at Lambda^2.
4. **Edge modes.** Donnelly-Wall edge modes reproduce the Kabat vector contact for Maxwell (abstract level). Kabat: for spin 1/2 the BH and entanglement entropies are identical (abstract verified), so no fermion contact beyond the Lichnerowicz term already counted. I found no source on fermion edge modes (searched; not found, so not examined). Whether the symplectic-diffeomorphism sector of a^mu has a Maxwell-like edge term is not shown; even granted, c_A = 1.
5. **Where the ingredient sits.** Which of {2, 0} is the Lambda^2 area coefficient is decided by one boundary datum: the flux of grad ln rho through Sigma in the regularised replica (zero for the fixed-state cover, nonzero for the smooth replica). This is a tip-regularisation (Problem A) datum, not a bulk-operator datum. If it selects the smooth value, the Lambda^2 comparison is 0 = 0 at the D=10 content and the burden moves to the next order (019 avenue 2).

## Target and status
Problem B (`sec:status-B`): Status OPEN, Priority CRITICAL PATH, Completion PROGRAMME-CONDITIONAL (appH lines 45-47). Chapter 17 full-GR criterion: A, B, C, D1, E, F, G-derived, N all DERIVED; H, I, J optional. No discrepancy found. Problem F enters only through c_T. Original target: derive fixed-volume stationarity of the tensor block with the area coefficient identified with the emergent-metric Einstein coefficient (G_T = G_A). Dependencies: A (state, modular flow, tip domain), F, C, D. This package: PROGRAMME-CONDITIONAL bounded no-go; no label change.

## Source reading
Digest + targeted reads (digest flagged dirty-chapters: yes; not a full scan). Read in full: appH `sec:status-B` (lines 41-198), 019 review-r2 and insert, 017 gap_table.py and hk_lib header, 015 verify_E_torsion.py, `reports/sme-scout-gluing-fermions-20261015.md`, ch08 `eq:O-eta`. The working tree now also contains the accepted 020 block and Troost2000; neither touches the anchor (anchor strings re-counted: each occurs once).

## Research and reasoning
Setting: Poisson limit, eta = delta, alpha = 1, Lambda^2 term, one loop (H1-H9 of 019 unchanged; H10 relaxed here).

(a) Operators. O_s = -D_mu D_mu (not rho^{-1} D rho D, which is the Laplace-Beltrami operator of G with E = 0); O_f = O_s - (1/2) gamma^{mu nu}{Theta_{mu nu},.}. Gilkey data extracted in exact arithmetic reproduce E_s = -(1/2) Box ln rho + (1/4)|d ln rho|^2, the scalar torsion identity of 015, and the 019 table entry tr(R_G/6 - E_f) = (4/6) R[g_rho]/rho + (1/2) X (independent re-derivation, diff <= 2e-13). New: the E_f identity. Interpretation: D_f = D_LC minus axial torsion minus a trace part absorbed in rho; no V^2 or Box ln rho term survives in the trace.

(b) Sides. T side: quadratic-form eigenvalue c_T = N_tot/6 - 4b, reading independent. A side: cone data of the chosen replica, plus a contact if E carries a delta. Reading (I): pulled-back, rho regular, E bounded, Q = 0 for bosons; the Dirac spin gluing adds +1 (holonomy of the Cartesian-component connection, equal at n=1 to the Q=1/4 delta of the Lichnerowicz reading). Reading (II): smooth first-order, all Q = 1/4. The fermion value is +1/3 in both; bosons are 1 (I) versus -1/2 (II) times the R[g_rho] coefficient.

(c) Bookkeeping (`cone_contact_bookkeeping.py`; W = N_tot, b = 1 - n_D/2): c_T = W/6 - 4b; c_A(unrot) = W/6 (gap 4 - 2n_D); c_A(AP) = W/6 + n_D (gap 4 - n_D); c_A(AP + vector contact) = W/6 + n_D - 1 (gap 3 - n_D); c_A(smooth) = -W/12 (gap 7/2 - N_s/4 - n_D). Smooth equals c_T on the line N_s = 14 - 4 n_D (e.g. non-vacuous at (n_D,N_s) = (5/2,4), (3,2), c_T > 0); supersymmetric D=6 (1,2) and D=4 (1/2,0) are not on it; (2,6) is on it with W = 0. Covariant N=4 SYM benchmark (minimal scalars, Lichnerowicz Dirac, Maxwell with Ricci): induced = cone with Kabat contact = 1, not 0; the matrix c_T = 0 differs because of the non-covariant rho^2 X structure.

(d) Sector cutoffs. With separate cutoffs the gap is 4 Lambda_v^2 - n_D Lambda_f^2 (scalar and ghost sectors 0); it vanishes at Lambda_f^2 = 2 Lambda_v^2 for n_D = 2, which nothing derived forces and which would also spoil c_T = 0. Recorded only.

Literature (fetched): Kabat hep-th/9503016 (NPB 453 (1995) 281-299, DOI 10.1016/0550-3213(95)00443-V): BH = entanglement entropy for spin 0 and 1/2, contact term for spin 1 (abstract). Donnelly-Wall 1506.05792 (PRD 94, 104053): edge modes account for the Kabat contact (abstract level). Larsen-Wilczek hep-th/9506066 (NPB 458 (1996) 249; abstract only; not used in the LaTeX). Solodukhin 1104.3712: abstract only this round; the vector value -1 in these units is taken from the merged statement that the vector with ghosts goes from 1/3 to -2/3. Not verified: any source on fermion edge modes; a Maxwell-like edge structure for the symplectic gauge sector.

Fork (hypotheses and relaxations of c_A - c_T = 2): H10 conical-only (relaxed: contacts examined, result above); replica geometry (I) vs (II) (relaxed: (II) gives 0 = 0); sectors/cutoffs (d); next order Lambda^0 and log on a curved J = 0 leaf (open); vector/ghost/scalar tip domains (open); non-rotational or non-quasi-free state (open); symplectic-gauge edge modes (open, bounded by c_A = 1 if Maxwell-like).

## Claim classification
- E_f = R_G/4 - T^2/16 + T T'/8 (trace/4); first-order identities; (AP - P)' = 2 Q_f: established (symbolic / exact-arithmetic numerics; the cone constants are the 019 conditional ones).
- Spin excess = Lichnerowicz contact, no double counting: established at n=1, conditional on the 019 constants.
- c_A^sm = -N_tot/12 with gluing-free Dirac +1/3: conditional (first-order smooth replica, alpha = 1, Lambda^2).
- Smooth replica forced by the Poisson class: conditional (smooth family with conical limit).
- Difference of readings = flux of grad ln rho: established algebra; its value in the matrix replica: unresolved.
- Vector contact -1 applying to a^mu: input / conjecture.
- Fermion edge modes: unresolved (no source found).
- Cutoff relation Lambda_f^2 = 2 Lambda_v^2: input, not derived.

## Proposed changes
File `chapters/appH-microscopic-proofs.tex`, `sec:status-B`. Anchor, occurring once and ending the 019 third paragraph: "...and they do not compute the next order of either side. Problems~B, C, D, F and~G remain open." The block goes immediately after that line and before `\section{Problem C: conformal mode and Cassini}` (occurs once). Nothing is replaced. No `\ref` added. New cites Kabat1995 and DonnellyWall2016 (neither is in `bib/namcg.bib`; entries in `bib_entries.bib`, for the integrator). `\LUV` is defined (`namcg-book7.tex:54`). Scratch compile outside the repo (working tree plus block plus entries; pdflatex, bibtex, pdflatex x2): 271 pages, 0 undefined or multiply-defined lines. `appH_insert.tex` is the same text (LF; integrator writes CRLF).

```latex
\paragraph{Spin term, Lichnerowicz contact and the smooth first-order cone in the comparison of \(G_T\) with \(G_A\) (conditional; not closure).}
Keep the setting of the two preceding paragraphs: Poisson limit, Euclidean section, \(\alpha=1\), the \(\LUV^2\) term, \(N_s\) scalars, the connection with its ghosts and \(n_D\) Dirac fields, \(N_{\mathrm{tot}}=N_s+2-4n_D\), and the coframe \(e^A{}_\mu=\eta^{AB}\omega_{\mu B}\) with torsion \(T\) of the torsion-invariant paragraph. At random two-jets of a closed \(\omega\), the operator \(\mathcal O_f\) of the fermionic-content paragraph satisfies \(\tfrac14\operatorname{tr}E_f=\tfrac14R_G-\tfrac1{16}T_{\lambda\mu\nu}T^{\lambda\mu\nu}+\tfrac18T_{\lambda\mu\nu}T^{\mu\lambda\nu}\), with no further term; the scalar identity differs only in the sign of the first torsion term. With the torsion as independent variable the Dirac operator therefore has the Lichnerowicz coefficient \(Q_f=\tfrac14\) per component, whereas in the variables \((G,\rho,\partial\Theta)\) it has \(Q_f=0\). The coefficient of \(R_G\) in \(\operatorname{tr}(\tfrac16R_G-E_f)\) is then \(-\tfrac13\) over four components, and with weight \(-1\) it gives \(+\tfrac13\) per Dirac field, the antiperiodic cone value, instead of \(-\tfrac23\). In the normalisation of the preceding paragraph the \(n\)-derivative at \(n=1\) of the heat-trace constant of a two-component block is \(\tfrac16\) for the antiperiodic gluing with the less singular extension and \(-\tfrac13\) for the unrotated gluing with the componentwise-regular domain; the difference \(\tfrac12=2Q_f\) is the contact term of \(Q_fR_G\) continued with its conical delta. The excess \(+1\) per Dirac field of the antiperiodic over the unrotated area coefficient is therefore the Lichnerowicz contact, it is already contained in \(c_A\), it enters the area side only and raises \(c_A\), and adding a contact \(-\operatorname{tr}Q_f\) per Dirac field to it would count it twice. For spin \(\tfrac12\) the conical and the induced coefficients are the same in the torsion reading~\cite{Kabat1995}.

\emph{Smooth first-order cone.} For \(\omega=\bar\omega+\epsilon\,\mathrm dA\), with any constant antisymmetric invertible \(\bar\omega\) and any \(A\), one has to first order in \(\epsilon\) (exact symbolic computation) \(R_G^{(1)}=-2\Box_{\bar G}\,\delta\ln\rho\) and \(\bar\rho\,R[g_\rho]^{(1)}=-\tfrac12\bar\rho^{\,2}R_G^{(1)}\). A conical deficit \(2\pi(1-n)\) at first order in \(n-1\) of a smooth Poisson structure therefore requires \(\ln\rho\) to carry the flux \(\oint\nabla\ln\rho\) through \(\Sigma\), that is a singular \(\rho\); the replica of the preceding paragraphs, with \(\rho\) regular and the cone on \(G\), is not a limit of smooth Poisson structures. For the smooth deformation every sector has \(Q=\tfrac14\) at first order and the area coefficient is \(c_A^{\mathrm{sm}}=-N_{\mathrm{tot}}/12\), the factor \(-\tfrac12\) times the coefficient of \(\rho R[g_\rho]\) in every sector including the Dirac fields, for which it coincides with the antiperiodic value \(+\tfrac13\) without any gluing prescription. Thus \(c_A^{\mathrm{sm}}\) equals the fixed-state antiperiodic coefficient \(c_A\) plus the bosonic contacts \(-\tfrac14(N_s+2)\), and the two readings differ by the total derivative \(\Box\delta\ln\rho\), that is by the boundary flux of \(\nabla\ln\rho\) through \(\Sigma\).

\emph{Outcome for \(n_D=2\), \(N_s=6\).} Here \(c_T=0\) and \(N_{\mathrm{tot}}=0\). The fixed-state replica gives \(c_A=2\). If the connection sector carries a contact of the Kabat value \(-1\) in these units (the value that takes the vector with its ghosts from \(\tfrac13\) to \(-\tfrac23\)), which for a Maxwell field is the edge-mode term of Donnelly and Wall~\cite{DonnellyWall2016}, then \(c_A=1\). The smooth reading gives \(c_A^{\mathrm{sm}}=0=c_T\), an equality of vanishing coefficients, which holds for every sector-uniform \(Q\) because \(N_{\mathrm{tot}}=0\) and is not a derivation. The contacts of these three types have weight \(+1\) per Dirac field (already contained in \(c_A\)), \(-1\) for the vector and \(0\) for the scalars and ghosts, so they give at most the value \(1\) above. Which of \(2\) and \(0\) is the \(\LUV^2\) area coefficient of the matrix state is the value of the flux of \(\nabla\ln\rho\) through \(\Sigma\) in the regularised replica. These statements are for the Poisson-limit operators, the \(\LUV^2\) term, one loop, \(\alpha=1\) and the fixed-state and first-order smooth replicas stated; they do not derive that flux, the state, the tip domain, or the gluing, do not treat edge modes of the symplectic gauge sector of \(a^\mu\), of the ghosts or of fermions (not examined), the \(\LUV^4\) term for \(N_{\mathrm{tot}}\neq0\), or the next order of either side, and give no value or sign of \(G_{\mathrm{eff}}\). Problems~B, C, D, F and~G remain open.
```

BibTeX (records verified through Crossref; DOIs resolve):

```bibtex
@article{Kabat1995,
  author  = {Kabat, Daniel},
  title   = {Black hole entropy and entropy of entanglement},
  journal = {Nuclear Physics B},
  volume  = {453},
  number  = {1--2},
  pages   = {281--299},
  year    = {1995},
  doi     = {10.1016/0550-3213(95)00443-V},
  eprint  = {hep-th/9503016},
  archivePrefix = {arXiv}
}

@article{DonnellyWall2016,
  author  = {Donnelly, William and Wall, Aron C.},
  title   = {Geometric entropy and edge modes of the electromagnetic field},
  journal = {Physical Review D},
  volume  = {94},
  number  = {10},
  pages   = {104053},
  year    = {2016},
  doi     = {10.1103/PhysRevD.94.104053},
  eprint  = {1506.05792},
  archivePrefix = {arXiv}
}
```

## Verification scripts
- `dirac_lichnerowicz.py` / `.out.txt`: Gilkey extraction of E_s, E_f for random closed omega; scalar formula, Dirac torsion identity (fit), manuscript table entry. About 2.5 min.
- `firstorder_poisson.py` / `.out.txt`: symbolic R_G^(1) = -2 Box delta ln rho, rho R[g_rho]^(1) = -(1/2) rho^2 R_G^(1), E_s^(1) = R^(1)/4.
- `cone_contact_bookkeeping.py` / `.out.txt`: cone constants AP/P (odd n up to 15), contact derivative, all c_A scenarios, IKKT values, equality line, sector-cutoff gap.
Run with `python -I`. These are checks, not proofs.

## Decisions Taken
- Treated the proposed "missing +1" as a sign question and answered it directly: it is an excess to be removed, not a deficit to be supplied.
- Put the first-order smooth reading in the LaTeX because it removes the branch dependence of the factor -1/2 and independently supports the 019 fermion value. Rejected a stronger statement that the smooth reading is the physical one (not derivable here).
- Rejected: writing the sector-cutoff relation into the manuscript (tuned input); writing the equality line N_s = 14 - 4 n_D into the manuscript (unphysical contents; kept here only).
- Spacetime remains emergent: G is built from Theta throughout.

## Milestone assessment
Candidate M2 (new bounded no-go: Lichnerowicz, Kabat and Donnelly-Wall contacts do not close the Lambda^2 gap non-vacuously; the ambiguity is localised to a boundary-flux datum). Not a breakthrough: no critical-path step is derived.

## Status-label recommendation
None. Problem B and the Chapter 17 set (A, B, C, D1, E, F, G-derived, N) unchanged.

## Author decision needed
None.

## Remaining open step
Derive from the matrix replica (Problem A: state, tip domain) the flux of grad ln rho through Sigma, i.e. choose between c_A = 2 and c_A = 0. Then compare the next order (Lambda^0 / log on a curved J = 0 leaf), where c_T = c_A = 0 at order Lambda^2. Also settle the vector/ghost/scalar tip domains, and establish or exclude a Maxwell-like edge term for the symplectic gauge sector. Ranked open avenues: (1) flux datum / replica choice; (2) next-order A side on a curved J = 0 leaf; (3) vector, ghost, scalar tip domains; (4) non-rotational or non-quasi-free state; (5) symplectic-sector edge modes (bounded at c_A = 1); (6) sector cutoffs (low).

## Special instructions for the gatekeeper
- Do not read the smooth-reading equality at IKKT as a derivation of G_T = G_A; it is 0 = 0 and holds for any sector-uniform Q.
- Re-check the E_f identity (script 1), the -1/2 relation (script 2), and that the block says "conditional; not closure" and changes no label.
- The vector contact -1 and its applicability to a^mu are inputs; fermion edge modes are explicitly not examined.
- "The Poisson class forces rho singular" is for smooth families with a conical limit at first order; it does not exclude the fixed-state replica as a definition of Tr rho^n.
