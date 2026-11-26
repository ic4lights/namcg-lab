# Proposal 021-spin-contact-term, round 2

## Changelog (r1 to r2)
Mathematics, scripts, bib entries and anchors unchanged. Wording of the LaTeX block revised; `appH_insert.tex` equals the block below exactly.
- **F1 (major).** Weighted shift stated: "the contact of Q_f R_G, which at the weight -1 shifts c_A by +1 per Dirac field, would count it twice" (review snippet 1).
- **F2 (major).** The binary "which of 2 and 0 is the coefficient ... is the flux" is replaced: 2 and 0 correspond to zero flux and full-deficit flux; intermediate fluxes not computed; the replica is selected by state and tip regularisation, not derived (snippet 3). Result item 5 and Remaining open step rewritten accordingly.
- **F3 (major).** Kabat is cited only for the Levi-Civita statement; the torsion-reading equality (both +1/3 per Dirac field) is stated to be the computation above (snippet 2).
- **F4.** Q_f = Q_s = 1/4 in the torsion reading stated; the match 1/2 = 2Q_f is stated to be an n-derivative equality at n = 1, not an identity in n; the branch-free -1/2 is restricted to the first-order local density of a regularised smooth family, and the branch issue of the unregularised singular-rho cone is stated not to be removed.
- **F5.** "Fixed-state replica" defined (pulled-back replica, rho regular, cone on G, antiperiodic Dirac gluing). Added: the first-order result does not by itself exclude it as the definition of Tr rho^n; the non-limit statement is at first order about constant Theta-bar.
- **F6.** Script scope: "checked symbolically for a generic omega-bar and following from the Weitzenboeck identities of the torsion-invariant paragraph". (The script uses one rational omega-bar with arbitrary A; the general case is by the merged identities, hand-derived in review-r1.)
- **F7.** Paragraphs named: "the paragraphs on fermionic content and on fermion replica gluing"; "the normalisation" now refers to the fermion-gluing paragraph (where the cone constants a^2+1/6 and the less singular extension are given); "the paragraph on the replica cone coefficient"; "the paragraph on the torsion invariant".
- **F8.** Weights "+1 Dirac, -1 vector, 0 scalar/ghost" scoped to fields minimally coupled in (G, rho, dTheta); "at most 1" scoped to that class; the torsion-reading bosonic contacts -(N_s+2)/4 are identified with the smooth reading and outside the class.
- Review "Conditional" note: the net torsion-reading connection-sector contact is -1/2, not -1; the vector -1 remains an input (already classified so). No label change.

## Result
Bounded no-go plus localisation of the missing ingredient. Problem B stays open; nothing is closed.

1. **Direction of the spin term (established algebra).** The spin term is not missing from the area side; it is what creates the gap. The antiperiodic Dirac cone value +1/3 equals the unrotated / (G,rho,dTheta)-reading value -2/3 plus +1 per Dirac field, and that +1 is the contact of the Lichnerowicz term Q_f R_G at weight -1. `dirac_lichnerowicz.py` gives tr E_f/4 = R_G/4 - T^2/16 + T T'/8 (residual 3e-13, 7 random closed omega), i.e. Q_f = Q_s = 1/4 in the torsion reading (scalar: +T^2/16). `cone_contact_bookkeeping.py` gives (AP - P)'(1) = 1/2 = 2 Q_f per two-component block; this is an equality of n-derivatives at n = 1, not an identity in n. The contact is already inside c_A = ... + n_D/3 and cannot be added again; it raises c_A, and closing needs c_A to fall by 2. No double counting with the 015 Q = 0 statement: Q = 0 refers to the endomorphism in (G,rho,dTheta) variables on the pulled-back cover, the spin excess to the holonomy/gluing; they agree at n = 1.
2. **First-order Weitzenboeck identity (established; symbolic and by hand).** For omega = omega_bar + eps dA: R_G^(1) = -2 Box delta ln rho and rho R[g_rho]^(1) = -(1/2) rho^2 R_G^(1). Hence a first-order smooth conical deficit of a Poisson structure about constant Theta-bar forces ln rho to carry flux through Sigma; the fixed-state replica is not a limit of smooth Poisson structures at this order (this does not exclude it as a definition of Tr rho^n). For a regularised smooth family the first-order local density has Q = 1/4 in every sector and c_A^sm = -N_tot/12; for Dirac this reproduces +1/3 with no gluing prescription. c_A^sm = c_A(AP) - (1/4)(N_s+2). The Bessel-branch issue of the unregularised singular-rho cone is not removed.
3. **Outcome at (n_D, N_s) = (2, 6) (c_T = 0, N_tot = 0).** Fixed-state AP: c_A = 2. AP plus a Kabat/Donnelly-Wall vector contact (-1, input): 1. Smooth first-order: 0, which is 0 = 0 for every sector-uniform Q (not a derivation). In the class of fields minimally coupled in (G,rho,dTheta), contact weights are +1 per Dirac (included), -1 vector, 0 scalars/ghosts, so at most c_A = 1.
4. **Edge modes.** Donnelly-Wall edge modes reproduce the Kabat vector contact for Maxwell (abstract level). Kabat: for spin 1/2 with the Levi-Civita connection the BH and entanglement entropies coincide (abstract verified); the torsion-reading equality is this proposal's computation. No source on fermion edge modes found (not examined). Whether the symplectic-diffeomorphism sector of a^mu has a Maxwell-like edge term is not shown; granted, c_A = 1.
5. **Where the ingredient sits.** The values 2 and 0 correspond to zero flux and full-deficit flux of grad ln rho through Sigma. c_A for intermediate flux is not computed. Which replica the matrix state selects depends on the state and the tip regularisation, not derived here (Problem A territory). If the smooth value is selected, the Lambda^2 comparison is 0 = 0 at the D=10 content and the burden moves to the next order.

## Target and status
Problem B (`sec:status-B`): Status OPEN, Priority CRITICAL PATH, Completion PROGRAMME-CONDITIONAL. Chapter 17 full-GR criterion: A, B, C, D1, E, F, G-derived, N all DERIVED; H, I, J optional. No discrepancy found. Problem F enters only through c_T. Original target: derive fixed-volume stationarity of the tensor block with the area coefficient identified with the emergent-metric Einstein coefficient (G_T = G_A). Dependencies: A (state, modular flow, tip domain), F, C, D. This package: PROGRAMME-CONDITIONAL bounded no-go; no label change.

## Source reading
Digest + targeted reads; r1 reads plus review-r1 (full scan by the gatekeeper) re-used. Working tree (uncommitted 017-020 integrations) treated as current. Paragraph titles in `chapters/appH-microscopic-proofs.tex` re-listed this round (lines 142, 188, 193, 1907) to name the references. Anchor strings re-counted in the working tree: "...do not compute the next order of either side. Problems~B, C, D, F and~G remain open." occurs once (line 199 region, end of the fermion-gluing block), `\section{Problem C: conformal mode and Cassini}` occurs once; the new paragraph title does not yet occur; Kabat1995 / DonnellyWall2016 are absent from `bib/namcg.bib`. Proposal 022 ignored as instructed.

## Research and reasoning
Unchanged from r1 except for the wording corrections above. Summary.

(a) Operators. O_s = -D_mu D_mu; O_f = O_s - (1/2) gamma^{mu nu}{Theta_{mu nu},.}. E_f identity as in Result 1; in the torsion reading Q_f = Q_s, so the Dirac-specific content is the holonomy gluing; its n-derivative at n = 1 equals the Q_f contact.

(b) Sides. T side: c_T = N_tot/6 - 4b, reading independent. A side: cone data of the chosen replica plus a contact if E carries a delta. Fixed-state (I): rho regular, bosons Q = 0, Dirac gluing +1. Smooth (II): all Q = 1/4. Fermion value +1/3 in both; bosons are 1 (I) versus -1/2 (II) times the R[g_rho] coefficient.

(c) Bookkeeping (`cone_contact_bookkeeping.py`; W = N_tot, b = 1 - n_D/2): c_T = W/6 - 4b; c_A(unrot) = W/6; c_A(AP) = W/6 + n_D (gap 4 - n_D); with vector contact W/6 + n_D - 1 (gap 3 - n_D); smooth -W/12 (gap 7/2 - N_s/4 - n_D). Smooth equals c_T on N_s = 14 - 4 n_D (scratch only; unphysical contents). Covariant N=4 SYM benchmark: induced = cone with Kabat contact = 1, not 0.

(d) Sector cutoffs: gap 4 Lambda_v^2 - n_D Lambda_f^2; vanishes at Lambda_f^2 = 2 Lambda_v^2 for n_D = 2; tuned input, recorded here only.

Literature (fetched in r1 and re-confirmed by the gatekeeper at abstract level): Kabat hep-th/9503016 (NPB 453 (1995) 281-299, DOI 10.1016/0550-3213(95)00443-V); Donnelly-Wall 1506.05792 (PRD 94, 104053; abstract: contact term = one negative scalar on the entangling surface, consistent with c = -1 in these units). Larsen-Wilczek and Solodukhin: abstract level only, not cited in the block. Not verified: full text of Kabat; any source on fermion edge modes; Maxwell-like edge structure of the symplectic gauge sector.

Fork (hypotheses and relaxations of c_A - c_T = 2) is recorded in "Remaining open step".

## Claim classification
- E_f = R_G/4 - T^2/16 + T T'/8 (trace/4); first-order identities; (AP - P)'(1) = 2 Q_f: established (symbolic / exact-arithmetic numerics; cone constants are the 019 conditional ones).
- Spin excess = Lichnerowicz contact at n = 1, no double counting: established at n = 1, conditional on the 019 constants.
- c_A^sm = -N_tot/12 with gluing-free Dirac +1/3: conditional (first-order regularised smooth family, alpha = 1, Lambda^2).
- Fixed-state replica not a limit of smooth Poisson structures at first order about constant Theta-bar: conditional (smooth family with conical limit); does not exclude it as a definition.
- Difference of readings = flux of grad ln rho: established algebra; the flux selected by the matrix replica: unresolved.
- Vector contact -1 applying to a^mu: input / conjecture (torsion-reading net connection-sector contact would be -1/2).
- Fermion and symplectic-gauge edge modes: unresolved (not examined).
- Cutoff relation Lambda_f^2 = 2 Lambda_v^2: input, not derived.

## Proposed changes
File `chapters/appH-microscopic-proofs.tex`, `sec:status-B`. Anchor, occurring once and ending the fermion-gluing third paragraph: "...and they do not compute the next order of either side. Problems~B, C, D, F and~G remain open." The block goes immediately after that line and before `\section{Problem C: conformal mode and Cassini}` (occurs once). Nothing is replaced. No `\ref` added (no new labels; paragraphs are named in words). New cites Kabat1995 and DonnellyWall2016 (absent from `bib/namcg.bib`; entries in `bib_entries.bib`, for the integrator). `\LUV` is defined (`namcg-book7.tex:54`). Scratch compile outside the repo (copy of the working tree without .git/proposals/scratch/reports, block inserted with CRLF, entries appended to bib; pdflatex, bibtex, pdflatex x2; script kept outside the repo): 271 pages, 0 undefined or multiply-defined lines. `appH_insert.tex` is byte-identical to the block below (LF; integrator writes CRLF).

```latex
\paragraph{Spin term, Lichnerowicz contact and the smooth first-order cone in the comparison of \(G_T\) with \(G_A\) (conditional; not closure).}
Keep the setting of the paragraphs on fermionic content and on fermion replica gluing: Poisson limit, Euclidean section, \(\alpha=1\), the \(\LUV^2\) term, \(N_s\) scalars, the connection with its ghosts and \(n_D\) Dirac fields, \(N_{\mathrm{tot}}=N_s+2-4n_D\), and the coframe \(e^A{}_\mu=\eta^{AB}\omega_{\mu B}\) with torsion \(T\) of the paragraph on the torsion invariant. The \emph{fixed-state replica} is the pulled-back replica of the paragraph on the replica cone coefficient (\(\rho\) regular, cone on \(G\)) with the antiperiodic Dirac gluing of the paragraph on fermion replica gluing. At random two-jets of a closed \(\omega\), the operator \(\mathcal O_f\) of the fermionic-content paragraph satisfies \(\tfrac14\operatorname{tr}E_f=\tfrac14R_G-\tfrac1{16}T_{\lambda\mu\nu}T^{\lambda\mu\nu}+\tfrac18T_{\lambda\mu\nu}T^{\mu\lambda\nu}\), with no further term in the representation by \(R_G\), \(T^2\) and \(TT'\); the scalar identity differs only in the sign of the first torsion term, so that \(Q_f=Q_s=\tfrac14\) in the torsion reading, whereas in the variables \((G,\rho,\partial\Theta)\) one has \(Q_f=0\). The coefficient of \(R_G\) in \(\operatorname{tr}(\tfrac16R_G-E_f)\) is then \(-\tfrac13\) over four components, and with weight \(-1\) it gives \(+\tfrac13\) per Dirac field, the antiperiodic cone value, instead of \(-\tfrac23\). In the normalisation of the paragraph on fermion replica gluing, the \(n\)-derivative at \(n=1\) of the heat-trace constant of a two-component block is \(\tfrac16\) for the antiperiodic gluing with the less singular extension and \(-\tfrac13\) for the unrotated gluing with the componentwise-regular domain; the difference \(\tfrac12=2Q_f\) equals the contact term of \(Q_fR_G\) continued with its conical delta. This is an equality of \(n\)-derivatives at \(n=1\), not an identity in \(n\). The excess \(+1\) per Dirac field of the antiperiodic over the unrotated area coefficient is therefore the Lichnerowicz contact. It is already contained in \(c_A\), it enters the area side only and raises \(c_A\), and adding to it the contact of \(Q_fR_G\), which at the weight \(-1\) shifts \(c_A\) by \(+1\) per Dirac field, would count it twice. For a Dirac field with the Levi-Civita spin connection the black-hole and entanglement entropies coincide~\cite{Kabat1995}; for the torsion reading the corresponding equality (both \(+\tfrac13\) per Dirac field) is the computation above.

\emph{Smooth first-order cone.} For \(\omega=\bar\omega+\epsilon\,\mathrm dA\), with any constant antisymmetric invertible \(\bar\omega\) and any \(A\), one has to first order in \(\epsilon\) \(R_G^{(1)}=-2\Box_{\bar G}\,\delta\ln\rho\) and \(\bar\rho\,R[g_\rho]^{(1)}=-\tfrac12\bar\rho^{\,2}R_G^{(1)}\). These were checked symbolically for a generic \(\bar\omega\) and follow from the Weitzenb\"ock identities of the paragraph on the torsion invariant. A conical deficit \(2\pi(1-n)\) at first order in \(n-1\) of a smooth Poisson structure about constant \(\bar\Theta\) therefore requires \(\ln\rho\) to carry the flux \(\oint\nabla\ln\rho\) through \(\Sigma\), that is a singular \(\rho\); the fixed-state replica is not a limit of smooth Poisson structures at this order. This does not by itself exclude the fixed-state replica as the definition of \(\operatorname{Tr}\rho^n\). For a regularised smooth family the first-order local density of every sector has \(Q=\tfrac14\), the factor \(-\tfrac12\) of the paragraph on the replica cone coefficient then carries no branch dependence, and the area coefficient is \(c_A^{\mathrm{sm}}=-N_{\mathrm{tot}}/12\), the factor \(-\tfrac12\) times the coefficient of \(\rho R[g_\rho]\) in every sector including the Dirac fields, for which it coincides with the antiperiodic value \(+\tfrac13\) without any gluing prescription. The branch issue of the unregularised singular-\(\rho\) cone is not removed. Thus \(c_A^{\mathrm{sm}}\) equals the fixed-state coefficient \(c_A\) plus the bosonic contacts \(-\tfrac14(N_s+2)\), and the two readings differ by the total derivative \(\Box\delta\ln\rho\), that is by the boundary flux of \(\nabla\ln\rho\) through \(\Sigma\).

\emph{Outcome for \(n_D=2\), \(N_s=6\).} Here \(c_T=0\) and \(N_{\mathrm{tot}}=0\). The fixed-state replica gives \(c_A=2\). If the connection sector carries a contact of the Kabat value \(-1\) in these units (the value that takes the vector with its ghosts from \(\tfrac13\) to \(-\tfrac23\)), which for a Maxwell field is the edge-mode term of Donnelly and Wall~\cite{DonnellyWall2016}, then \(c_A=1\). The smooth reading gives \(c_A^{\mathrm{sm}}=0=c_T\), an equality of vanishing coefficients, which holds for every sector-uniform \(Q\) because \(N_{\mathrm{tot}}=0\) and is not a derivation. For fields minimally coupled in the variables \((G,\rho,\partial\Theta)\), the contacts of these types have weight \(+1\) per Dirac field (already contained in \(c_A\)), \(-1\) for the vector and \(0\) for the scalars and ghosts, so within this class they give at most the value \(1\) above; the torsion-reading bosonic contacts \(-\tfrac14(N_s+2)\) are the smooth reading and do not belong to this class. The values \(2\) and \(0\) correspond to a replica in which \(\ln\rho\) carries no flux through \(\Sigma\) and one in which it carries the full deficit; intermediate fluxes are not computed, and which replica the matrix state selects depends on the state and the tip regularisation, which are not derived here. These statements are for the Poisson-limit operators, the \(\LUV^2\) term, one loop, \(\alpha=1\) and the fixed-state and first-order smooth replicas stated; they do not derive the replica, the state, the tip domain or the gluing, do not treat edge modes of the symplectic gauge sector of \(a^\mu\), of the ghosts or of fermions (not examined), the \(\LUV^4\) term for \(N_{\mathrm{tot}}\neq0\), or the next order of either side, and give no value or sign of \(G_{\mathrm{eff}}\). Problems~B, C, D, F and~G remain open.
```

BibTeX (unchanged from r1; records verified through Crossref, re-confirmed by the gatekeeper):

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
Unchanged from r1; outputs stored.
- `dirac_lichnerowicz.py` / `.out.txt`: Gilkey extraction of E_s, E_f for random closed omega; scalar formula, Dirac torsion identity (fit), manuscript table entry. About 2.5 min.
- `firstorder_poisson.py` / `.out.txt`: symbolic R_G^(1) = -2 Box delta ln rho, rho R[g_rho]^(1) = -(1/2) rho^2 R_G^(1), E_s^(1) = R^(1)/4, for one rational omega-bar and arbitrary A; the general omega-bar follows from the merged Weitzenboeck identities (hand-derived in review-r1).
- `cone_contact_bookkeeping.py` / `.out.txt`: cone constants AP/P, contact derivative, all c_A scenarios, IKKT values, equality line, sector-cutoff gap.
Run with `python -I`. These are checks, not proofs.

## Decisions Taken
- The "missing +1" is an excess to be removed, not a deficit to be supplied; the weighted shift is stated as +1 per Dirac field to rule out the opposite reading.
- Kept the first-order smooth reading in the LaTeX, scoped to a regularised smooth family; rejected a statement that it is the physical replica.
- Localisation sentence made non-binary (F2) rather than dropped, since the flux datum is still the identified controlling variable.
- Rejected: sector-cutoff relation and the N_s = 14 - 4 n_D line in the manuscript (tuned / unphysical).
- Spacetime remains emergent: G is built from Theta throughout.

## Milestone assessment
Candidate M2 (new bounded no-go: Lichnerowicz, Kabat and Donnelly-Wall contacts do not close the Lambda^2 gap non-vacuously; the ambiguity is localised to a replica/flux datum). Not a breakthrough.

## Status-label recommendation
None. Problem B and the Chapter 17 set (A, B, C, D1, E, F, G-derived, N) unchanged.

## Author decision needed
None.

## Remaining open step
Ranked open avenues (from review-r1):
1. The replica and flux datum: compute c_A for intermediate flux of grad ln rho through Sigma, and the replica of the matrix state (state and tip regularisation), as a Problem A sub-lemma. Decides between c_A = 2, 1 and 0 at the D = 10 content.
2. The next order (Lambda^0 and log) on a curved J = 0 leaf, where c_T = c_A = 0 at Lambda^2.
3. Tip domains for the vector, ghost and scalar sectors, and whether a Maxwell-like edge term applies to the symplectic gauge sector (bounded at c_A = 1 if so); fermion edge modes.
4. A non-quasi-free or non-rotational state.
5. Contents on N_s = 14 - 4 n_D, as a check of non-vacuity only (unphysical contents).
6. Sector cutoffs (tuned; low).

## Special instructions for the gatekeeper
- Do not read the smooth-reading equality at IKKT as a derivation of G_T = G_A; it is 0 = 0 and holds for any sector-uniform Q.
- Re-check that the block says "conditional; not closure", changes no label, states the +1 per Dirac weighted shift, cites Kabat only for the Levi-Civita statement, and does not call the flux decisive or binary.
- The vector contact -1 and its applicability to a^mu are inputs; fermion edge modes are explicitly not examined.
- "The Poisson class forces rho singular" is scoped to smooth families with a conical limit at first order about constant Theta-bar and does not exclude the fixed-state replica as a definition of Tr rho^n.
