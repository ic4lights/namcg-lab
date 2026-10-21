# Proposal 037-comparator-first-law, round 2

## Result
Bounded, conditional result; Problem B and A stay open.
1. The comparator $12\kappa_C^T$ (=$-4\kappa_X$ for $\operatorname{tr}\Omega^2$) is not selected by any first law available for the composite connection. It is the entropy of a metric functional that agrees with $\operatorname{tr}\Omega^2$ on every sampled mode. The two functionals have different polarisations (e_extension.py), so the 12-mode quadratic form does not fix the cross term with the replica direction, which lies outside the modes. The value $12\kappa_C^T$ is **not shown to be** the entropy of $\operatorname{tr}\Omega^2$.
2. The composite constraint $b=F[\Theta]$ is covariant only under the rotation acting on the chart and the matrix indices together (c_equivariance.py: fails for chart-only, index-only, non-orthogonal linear and non-linear chart maps). The only flow vanishing on $\Sigma$ is the normal-plane rotation, which acts on the fibre by $\mathcal{J}_{12}$, so the Lorentz-Lie Noether pairing is $\kappa_X\operatorname{tr}(\mathcal{J}_{12}\Omega_{12})$, coefficient $-2\kappa_X$ of $W$. $\mathcal{J}_{34}$ cannot enter. The multiplier route fixes $\lambda$ in terms of $D(\partial L/\partial\Omega)$ and reproduces the Euler--Lagrange expression of the composite Lagrangian (a check of the field equations in a one-dimensional toy, not of a charge).
3. Exact dictionary (b_dictionary.py): the $W$-coefficient of the Noether entropy with fibre holonomies $(\alpha_v,\alpha_f)$ is $N_{\mathrm{tot}}/10-2\alpha_v+n_D\alpha_f$. The Noether value corresponds to $(1,1)$. The periodic, fixed-state and completed replicas equal it at $(0,0)$, $(0,1)$, $(1,1)$ for all $(N_s,n_D)$ (exact arithmetic on six modes of each chirality), so their agreement with $E$ at their own holonomy is an identity. The comparator $12\kappa_C^T$ equals $E(2,2)$; this is a statement about the coefficient of $W$ and not about a holonomy of the bundle. Relative to $E(1,1)$ the residuals of the periodic, fixed-state and completed replicas are $2-n_D$, $2$, $0$.
4. So the completed Weyl gap $2\kappa_X$ is a comparator artefact. The physical residual is the vector holonomy omitted by integer-$n$ gluing (fixed-state: $2$, independent of $N_s$, $n_D$), a contact of the type $S_{\mathrm{BH}}=S_{\mathrm{ent}}-Q$, by analogy with the Noether-charge term for non-minimally coupled scalars of Frolov--Fursaev.
5. Caveat: for matched holonomy the agreement is an identity between two cross terms of the same $a_2$ with the same deltas. The independent check is the Dirac entry (index weight $-1/2$ versus the Landau--Aharonov--Bohm spin term). Which holonomy the matrix state selects is not derived. The $\Lambda^2$ analogue ($G_T$ vs $G_A$, $\rho^2X$) is not resolved.

## Target and status
Problem B (replica Ward identity) and A. Appendix H: B "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL"; A "OPEN, CRITICAL PATH for the matrix-derived label". Chapter 17 requires A, B, C, D1, E, F, G-derived, N; no discrepancy found. Original target of B: derive stationarity and the area term from the microscopic dynamics. This package is PROGRAMME-CONDITIONAL and closes nothing (rule 3).

## Source reading
Full scan. `scripts/make_digest.py --check` printed `DIGEST CURRENT`. I read every current `chapters/*.tex` in full (30 files), including ch01--ch18 (including ch17-agenda), appA--appL (all 2737 lines of appH-microscopic-proofs.tex), and the 037 insert. I also read in full: `proposal-r1.md`, `review-r1.md`, `appH_insert.tex`, all six 037 scripts and their libraries, and `reports/ledger.md` (tail).

## Research and reasoning
Setting: the 033 modes ($\delta\rho=0$ plane waves about constant (A)SD $\bar\Theta$), totally geodesic $\Sigma$, first order in $1-n$, Euclidean section.

(a) Decomposition (a_decomposition.py, a2_frame_variants.py). On all sampled modes $\langle\Omega,\Omega\rangle=-4C^2=2\langle R,R\rangle$, and $\ell_{\mathcal{J}_{12}}(\Omega)=\ell_{\mathcal{J}_{12}}(R)=-R_{ijij}$. With the identity identification of matrix and chart index $\langle\Omega,R\rangle=0$. With the coframe identification $e=\bar\omega$, $\langle\Omega,R\rangle=\langle R,R\rangle$, so $\Omega=R+N$ with $\langle N,R\rangle=0$, $\langle N,N\rangle=\langle R,R\rangle$, $\ell_{\mathcal{J}_{12}}(N)=0$. The factor 2 in $\operatorname{tr}\Omega^2=-4C^2$ is half Levi-Civita and half a part the holonomy cannot pair with. Both identifications are reported; the claims used (norm ratio 2, equal $\mathcal{J}_{12}$ pairing) do not depend on the choice.

(b) Extension non-uniqueness (e_extension.py). $Q_1=\operatorname{tr}\Omega^2/12$ and $Q_2=-C^2/3$ agree on each single mode; $B_1-B_2$ is non-zero on pairs of modes with different wave vectors and between a mode and generic closed jets. Equality on single modes is all the earlier gap used.

(c) Composite constraint and first law. Extended Lagrangian $L(G,\omega)+\langle\lambda,\omega-F[\Theta]\rangle$. The $\omega$-equation gives $\lambda=-E_\omega$, and the $\Theta$-equation then equals the chain-rule Euler-Lagrange expression (toy check). A Noether charge needs a local symmetry; $F$ is covariant only under the diagonal SO(4) (Euclidean test), so a diffeomorphism-covariant Iyer-Wald derivation is not available for Presentation A. That is the Problem D content and is not supplied. Jacobson-Mohd (abstract verified): the diffeomorphism-only charge fails because a regular frame is not invariant under the Killing flow at the bifurcation surface; they use the combined Lorentz-diffeomorphism charge. Here the combined action is forced by the equivariance of $F$, and the pairing is with $\mathcal{J}_{12}$ only. The spin-complete modular generator gives $\alpha_f=1$ for Dirac fields (certain) and $\alpha_v=1$ for the vector if $K$ includes the spin of the index; integer-$n$ gluing gives $\alpha_v=0$. The spin-complete continuation is non-analytic at $n=1$ (ledger, fermionic-content paragraph). **With the auxiliary-variable hypothesis** (connection treated as an auxiliary independent field on which the Lagrangian depends through its curvature), the Noether density is $\kappa\operatorname{tr}(H\Omega_{12})$ with $H=\mathcal{J}$. The charge of the constraint term $\langle\lambda,\omega-F[\Theta]\rangle$ is not computed: for the composite $\omega=F[\Theta]$ the multiplier term has its own Noether contribution, and $\delta_\xi\Theta$ involves $\partial\xi$, which is non-zero at $\Sigma$. A covariance under general diffeomorphisms of the chart is not available for $b$.

(d) Dictionary as in Result 3, with $\kappa_v=1$, $\kappa_f=-1/2$ and the $W$-coefficient of $\tau$ ($-2$) fitted from the modes.

Hypotheses of the earlier no-go and relaxations: the comparator is relaxed here; the replica holonomy is now a parameter and its selection is open; the diagonal family is not needed; the cross-term rule is used only for the Levi-Civita part; first order in $1-n$, the $n<1$ branch and totally geodesic $\Sigma$ are unchanged.

Literature. Verified (arXiv page and/or Crossref): Jacobson-Mohd 1507.01054, PRD 92, 124010; Frolov-Fursaev hep-th/9703178, PRD 56, 2212 (abstract: $S_{\mathrm{BH}}$ and $S_{\mathrm{R}}$ differ by a Noether-charge surface integral $Q$ for non-minimal constituents); Hung-Myers-Smolkin 1101.5813, JHEP 04 (2011) 025 (Wald's formula does not in general give EE); Iyer-Wald PRD 50, 846; Hollands-Wald CMP 321, 629; Dong JHEP 01 (2014) 044 (the last three by Crossref record only, not used for a claim). Correction to the scout: 2012.14892 is by Elgood, Ortin, Perenniguez, JHEP 05 (2021) 110. The scout's equation numbers were not re-verified and are not used. Dong/Camps $K^2$ terms vanish on totally geodesic $\Sigma$.

## Claim classification
- Decomposition, non-uniqueness, equivariance, multiplier toy, dictionary: established (exact arithmetic or symbolic on sampled jets, within the stated modes and hypotheses).
- Completed Weyl gap is a comparator artefact: conditional on the replica/holonomy identification.
- Matched-holonomy agreement: identity, not an independent confirmation, except the Dirac entry.
- Selection $\alpha_v=1$: conjecture (spin-complete modular flow).
- $\Lambda^2$ analogue: unresolved.

## Addressing gatekeeper findings

**F1 (Major -- Dictionary paragraph):** Reworded. The Noether value of the preceding paragraph is $E(1,1)$. The periodic, fixed-state and completed replicas have the coefficients of $W$ of $E$ at $(\alpha_v,\alpha_f)=(0,0)$, $(0,1)$, $(1,1)$ for all $(N_s,n_D)$ (exact arithmetic on six modes of each chirality), so their agreement with $E$ at their own holonomy is an identity. The comparator $12\kappa_C^T$ equals $E(2,2)$; this is a statement about the coefficient of $W$ and not about a holonomy of the bundle. Relative to $E(1,1)$ the residuals of the periodic, fixed-state and completed replicas are $2-n_D$, $2$, $0$. The vanishing-gap sentence is deleted; the residuals against $(1,1)$ are kept. The $(2,2)$ entry is stated as a statement about the coefficient of $W$ only.

**F2 (Major -- Composite constraint paragraph):** Added the auxiliary-variable hypothesis: "with the auxiliary-variable hypothesis (connection treated as an auxiliary independent field on which the Lagrangian depends through its curvature)". Added that the charge of the constraint term is not computed. Described the 1-D toy as "a check of the field equations in a one-dimensional toy, not of a charge". The charge of the constraint term of the composite connection is added to the closing "do not derive" list.

**F3 (Minor -- Comparator is an extension):** Changed "have the same value on each mode" to "have the same value on every sampled mode" (verified on six modes per chirality, not proved for the family). Changed "is the entropy of $\operatorname{tr}\Omega^2$" to "is not shown to be the entropy of $\operatorname{tr}\Omega^2$".

**F4 (Minor -- Multiplier sign):** Changed "gives $\lambda=-D(\partial L/\partial\Omega)$" to "fixes $\lambda$ in terms of $D(\partial L/\partial\Omega)$", dropping the explicit sign (which depends on a multiplier convention not stated).

**F5 (Minor -- Frolov-Fursaev citation):** Changed "a contact of the type $S_{\mathrm{BH}}=S_{\mathrm{ent}}-Q$ of Frolov--Fursaev" to "a contact of the type $S_{\mathrm{BH}}=S_{\mathrm{ent}}-Q$, by analogy with the Noether-charge term for non-minimally coupled scalars of Frolov--Fursaev", making clear that the surface term $Q$ is a Noether charge for non-minimally coupled scalars and the vector holonomy contact is by analogy.

## Proposed changes
File `chapters/appH-microscopic-proofs.tex`. Insert the block below (identical to the corrected `appH_insert.tex`) immediately before `\section{Problem C: conformal mode and Cassini}` (occurs once), after the 036 block ending "Problem~B stays open and PROGRAMME-CONDITIONAL.", followed by one blank line. Nothing is replaced. No $\label$ or $\ref$ added; new $\cite$ keys JacobsonMohd2015 and FrolovFursaev1997 (absent from `bib/namcg.bib` at time of check). The block has 0 TABs, is ASCII, LF (integrator converts to CRLF).

```latex
\paragraph{Comparator for the entropy of the bundle curvature and the holonomy dictionary (conditional; not closure).}
Keep the setting of the preceding paragraph: the modes with \(\delta\rho=0\) about a constant self-dual or anti-self-dual \(\bar\Theta\), a totally geodesic \(\Sigma\), cross terms at first order in \(1-n\), and the weights \(\kappa_X=1-\tfrac12n_D\) (vector \(1\), each Dirac field \(-\tfrac12\)). Write \(\mathcal J=\mathcal J_{12}\) for the generator of the rotation of the normal plane, \(\alpha_v\mathcal J\) for the holonomy around \(\Sigma\) of the vector bundle connection and \(\alpha_f\mathcal J\) for that of each Dirac fibre (\(\mathcal J\to\tfrac12\gamma^{12}\)).

\emph{The comparator is an extension.} The functionals \(\tfrac1{12}\operatorname{tr}\Omega^2\) and \(-\tfrac13C^2\) have the same value on every sampled mode (exact arithmetic, both chiralities), but their polarisations differ on pairs of modes with different wave vectors and between a mode and a generic closed second jet (exact arithmetic). The entropy at first order in the amplitude is the cross term of the quadratic form with the direction of the replica, which lies outside the modes, so the quadratic form on the modes does not fix it. The value \(12\kappa_C^T\) is the entropy of the metric functional with the same value on every sampled mode, is not shown to be the entropy of \(\operatorname{tr}\Omega^2\). Under the identification of the matrix index with the tangent index through the coframe \(e=\bar\omega\), \(\Omega^v=R\oplus N\) on the modes, with \(R\) the Levi-Civita curvature, \(\langle N,R\rangle=0\), \(\langle N,N\rangle=\langle R,R\rangle\) and \(\operatorname{tr}(\mathcal J N_{12})=0\); the holonomy generator pairs with \(R\) only (without that identification \(\langle\Omega^v,R\rangle=0\), while the values \(\langle\Omega^v,\Omega^v\rangle=2\langle R,R\rangle\) and \(\operatorname{tr}(\mathcal J\Omega_{12})\) are unchanged).

\emph{The composite constraint.} For \(b_\sigma=G_{\sigma\tau}\Theta^{\rho\tau}\partial_\rho\Theta\) the transformation law of a one-form valued in the adjoint holds under the rotation acting on the chart and on the matrix indices together, and fails under a rotation of the chart alone, of the matrix indices alone, under a non-orthogonal diagonal linear map and under a non-linear change of chart (exact check at a point, Euclidean section). The flow generated by the rotation of the normal plane therefore acts on the fibre through \(\mathcal J\), and no generator \(\mathcal J_{34}\) enters the pairing, since the corresponding rotation does not vanish on \(\Sigma\). Introducing a multiplier \(\lambda\) for \(\omega-F[\Theta]\) fixes \(\lambda\) in terms of \(D(\partial L/\partial\Omega)\) and reproduces the Euler--Lagrange expression of the composite Lagrangian (a check of the field equations in a one-dimensional toy, not of a charge). A first law of the form of the Lorentz--diffeomorphism Noether charge~\cite{JacobsonMohd2015} can be formed only with this tie. If the connection is treated as an auxiliary independent field on which the Lagrangian depends through its curvature, it gives the density \(\kappa\,\operatorname{tr}(H\Omega_{12})\) with \(H=\mathcal J\); the charge of the constraint term is not computed. A covariance under general diffeomorphisms of the chart is not available for \(b\).

\emph{Dictionary.} Let \(E(\alpha_v,\alpha_f)\) be the coefficient of \(W\) in the cross term \(\sum_i\kappa_i\operatorname{tr}(H_i\Omega_{12})\) with the holonomy \(H=\alpha_v\mathcal J\) on the vector bundle and \(H=\alpha_f\mathcal J\) on each Dirac fibre. It is \(N_{\mathrm{tot}}/10-2\alpha_v+n_D\alpha_f\), because \(\operatorname{tr}(\mathcal J\Omega_{12})\) has coefficient \(-2\) of \(W\). The Noether value of the preceding paragraph is \(E(1,1)\). The periodic, fixed-state and completed replicas have the coefficients of \(W\) of \(E\) at \((\alpha_v,\alpha_f)=(0,0)\), \((0,1)\), \((1,1)\) for all \((N_s,n_D)\) (exact arithmetic on six modes of each chirality), so their agreement with \(E\) at their own holonomy is an identity. The comparator \(12\kappa_C^T\) equals \(E(2,2)\); this is a statement about the coefficient of \(W\) and not about a holonomy of the bundle. Relative to \(E(1,1)\) the residuals of the periodic, fixed-state and completed replicas are \(2-n_D\), \(2\), \(0\). For the periodic and completed replicas this agreement is the identity between two cross terms of the same \(a_2\) with the same deltas. The Dirac entry is a check: the index weight \(-\tfrac12\) of the heat coefficient and the spin term of the Landau--Aharonov--Bohm spectrum agree. The residual \(2\) of the fixed-state replica is the vector holonomy that integer-\(n\) gluing omits, a contact of the type \(S_{\mathrm{BH}}=S_{\mathrm{ent}}-Q\), by analogy with the Noether-charge term for non-minimally coupled scalars of~\cite{FrolovFursaev1997}.

These statements are for the modes, replica and hypotheses of the preceding paragraphs, the Euclidean section and the coefficient of \(W\) only. They do not derive the holonomy selected by the matrix state, the continuation in \(n\) of the spin-complete replica (not analytic at \(n=1\) in the ledger above), the Euler coefficient, the logarithmic order off these modes, a first law at order \(\Lambda_{\mathrm{UV}}^2\) (where \(\rho^2X\) has no bundle curvature and the gap of the normalisation paragraph is not addressed), the charge of the constraint term of the composite connection, or a value or sign of \(G_{\mathrm{eff}}\). Problem~B stays open and PROGRAMME-CONDITIONAL.
```

BibTeX (Crossref-verified):
```bibtex
@article{JacobsonMohd2015,
  author  = {Jacobson, Ted and Mohd, Arif},
  title   = {Black hole entropy and {Lorentz}--diffeomorphism {Noether} charge},
  journal = {Physical Review D},
  volume   = {92},
  pages   = {124010},
  year   = {2015},
  doi   = {10.1103/PhysRevD.92.124010},
  eprint  = {1507.01054},
  archivePrefix = {arXiv}
}

@article{FrolovFursaev1997,
  author  = {Frolov, Valeri P. and Fursaev, Dmitri V.},
  title   = {Mechanism of the generation of black hole entropy in {Sakharov}'s induced gravity},
  journal = {Physical Review D},
  volume   = {56},
  pages   = {2212--2225},
  year   = {1997},
  doi   = {10.1103/PhysRevD.56.2212},
  eprint  = {hep-th/9703178},
  archivePrefix = {arXiv}
}
```

## Verification scripts
Run from the proposal folder with `python` (not `-I`, local imports). Outputs are saved as *.out.txt.
- a_decomposition.py, a2_frame_variants.py: norms, pairings, $\Omega=R+N$ under both frame identifications.
- b_dictionary.py: replica/holonomy dictionary, gaps, $\alpha=2$ for the comparator.
- c_equivariance.py: equivariance of $b$ under five classes of maps.
- e_extension.py: non-uniqueness of the extension.
- f_multiplier_toy.py: multiplier versus chain rule.
- modes_lib.py, lib.py, lin_lib.py: libraries copied from 033/036.

## Decisions Taken
- The comparator is treated as a property of the functional and of the flow, not a choice: the answer is the Noether value with the holonomy fixed by equivariance. Rejected: fixing it by matching the replica.
- Both frame identifications are reported rather than one chosen.
- The $\Lambda^2$ analogue is left as a fork rather than extending the claim.

## Milestone assessment
Candidate important bounded result, not a breakthrough claim: the Weyl gap $2\kappa_X$ of 033 is removed as a comparator artefact for the spin-complete replica, and the physical residual is relocated to the vector spin contact. It covers one coefficient on 12 modes, the matching is partly an identity, and the holonomy selection and the $\Lambda^2$ gap ($G_T$ vs $G_A$) remain open. The gatekeeper decides.

## Status-label recommendation
None. B and A remain OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL.

## Author decision needed
None.

## Remaining open step
Ranked open avenues:
1. Derive from the matrix state whether the modular flow rotates the vector index ($\alpha_v$): the vector spin contact / edge sector (Kabat, Donnelly-Wall), including the non-analyticity at $n=1$.
2. $\Lambda^2$ analogue: entropy of $\rho^2X$ (no bundle curvature). Sketch only, not verified: a first-derivative frame-dependent Lagrangian has a diffeomorphism-only Noether charge proportional to $\xi$, vanishing on $\Sigma$, and the Iyer-Wald ambiguity proportional to the derivative of $\xi$ is not fixed without local Lorentz covariance (D1). Test via the TEGR identity $R=-(T^2/4+TT/2-V^2)-2\operatorname{div}V$.
3. A diffeomorphism-covariant lift of $F$ (Problem D) so the Iyer-Wald derivation is not conditional.
4. Non-geodesic $\Sigma$ and Dong/Camps $K^2$ terms; the Euler coefficient; the Lorentzian section.
5. Exact heat trace of the cone with holonomy in place of the cross-term rule.

## Special instructions for the gatekeeper
- Do not read the dictionary as an independent confirmation of $A=T$; check its identity status (Result item 5) and the Dirac cross-check.
- Re-run b_dictionary.py and c_equivariance.py; equivariance is tested in the Euclidean section only.
- "$12\kappa_C^T = \text{holonomy } 2\mathcal{J}$" is a $W$-coefficient statement, not a physical holonomy.
- The coframe identification is used only for the orthogonality claim.
- The scratch copy for the compile check is in the session scratchpad, outside the repo.
