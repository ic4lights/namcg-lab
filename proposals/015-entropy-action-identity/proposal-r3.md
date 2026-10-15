# Proposal 015-entropy-action-identity, round 3

## Changelog against r2

- Build fix: every `\LUV_s`, `\LUV_v` (10 occurrences, Item 1 appH block) replaced by `\Lambda_{\mathrm{UV},s}`, `\Lambda_{\mathrm{UV},v}` (exponents follow, e.g. `\Lambda_{\mathrm{UV},s}^{2}`), because `\LUV` already contains a subscript (namcg-book7.tex l.54). No other subscripted macro is subscripted again (no `\Geff_x` use).
- Content change (only one): "(for the branch stated)" added to "The two choices differ by the factor -1/2 in every sector."
- Everything else identical to r2.

## Changelog against r1

Response to `review-r1.md` (ACCEPT WITH REQUIRED REVISIONS, M2, OPEN 0/2, no PRIOR-CLAIM-ERROR). The mathematics, scripts and claim set of r1 are unchanged; only the wording and scope of the proposed text change. The "prior-claim" framing of r1 (Result item 6, Decision 3, gatekeeper instructions) is withdrawn: the review found no error in merged text, and the three points are clarifications.

| Finding | Addressed how |
|---|---|
| F1 (major) appG sentence | Replaced by the review's snippet (Item 2a): the entropy differs from `Area/(4 G_eff)` by a contact term proportional to `tr Q` if the conical delta of `R` is not continued into `E`; the difference vanishes if it is. This agrees with the appH contact-term paragraph (delta continued: `Delta S = -2 pi A tr Q <phi^2>`, i.e. `S_BH = S_ent - Q`; without the delta the entropy is `S_ent`). |
| F2 (major) no-go scope | The appH no-go sentences now read "for the replica of the first paragraph" and name the class "(Poisson limit, Euclidean section, background Feynman gauge, one loop, `LUV^2` term, the two modes with `delta rho = 0`)". |
| F3 ch07 | The review's sentence is used verbatim (Item 3): the coefficient equality is part of the content of Hypotheses 5 and 6 as written, not an extra input, and is not supplied by Hypothesis 4 or by the `Geff` identification. |
| F4 appG Status | The review's sentence is used (Item 2b). |
| F5 appH first paragraph | Notation: "the coefficient `A` of Equation~\eqref{eq:Geff-structure}" (label verified, ch08 l. 223). The variables `(G, rho, dTheta)` are stated at "with that G". A scoped closing clause points to the closing sentence of the second paragraph. |
| F6 (II) | The singular-rho result is marked "a statement conditional on that branch and not used below"; "checked by direct summation" is removed; the only support cited is the branch-independent local `a_1` ratio `-1/2`. |
| F7 | No action (the reviewer agrees: ch08 left unedited, follow-up recorded). |

Other changes: Result item 6 and Decision 3 reworded without "prior claim"; "Remaining open step" carries a ranked avenue list for the `G_T != G_A` gap (listed only, not explored in this round); anchors and labels re-verified.

## Result

Target: Problem B, sub-items B2 (area coefficient) and the normalisation half of B1, route "entropy-action identity" (`reports/sme-route-B-DorauMuch-20261015-1052.md`). Operators of the integrated Poisson-limit paragraph (scalar `O_s`, internal-index connection `O_v`, ghost of weight -2; Euclidean, background gauge, `ass:emergent-op`). No `S = A/4` and no external `G` is used. Derivations and scripts are those of `proposal-r1.md` ("Research and reasoning", sections 1-10), which stay in force.

1. **Cone coefficient (derived, conditional).** For the pulled-back replica (cone on `G` and `g_rho` together, `rho` regular), every Laplace-type sector with bounded connection and endomorphism has the flat-cone area term, `S = (A_G/48 pi) sum_s w_s tr 1_s Lambda_s^2`. The same limit in the effective action gives `1/(16 pi G) = sum_s w_s tr 1_s Lambda_s^2/(192 pi^2)`. So `S = A_G/(4G)` in the variables `(G, rho, dTheta)`, and the coefficient of `delta A` in `eq:first-law` is the `Lambda^2` coefficient `A = 1/(12 pi)` per unit weighted fibre trace.
2. **Contact term.** With the conical delta of `R_G` continued into `E = E_0 + Q R_G`, `Delta S = -2 pi A_G sum w tr Q <phi^2>`, i.e. `S_BH = S_ent - Q` (Solodukhin eqs. (322)-(323)); without the delta, `S = S_ent`. In `(G, rho, dTheta)` all sectors have `Q = 0`.
3. **Variable dependence.** In `(G, torsion)` the scalar sector has `Q = 1/4` (`E_s = R_G/4 + T^2/16 + TT'/8`) and the `R_G` coefficient flips from `N_tot/6` to `-N_tot/12`. `A_{1,R,s}` of `thm:Geff` is not a function of the operators alone.
4. **Which geometry carries the cone.** Replica (I) (used) against (II) (singular `rho`; conditional on the `m = 0` branch; not used): ratio `-1/2`, equal to the local `a_1` result with `Q = 1/4`.
5. **Bounded no-go.** In the class (Poisson limit, Euclidean section, background Feynman gauge, one loop, `Lambda^2` term, the two modes with `delta rho = 0`) and for the replica (I): the induced form has `c_T = N_tot/6 - 4` against `c_A = N_tot/6`; `1/G_A - 1/G_T = 2 Lambda^2/pi` (common cutoff), `2 Lambda_v^2/pi` (separate), independent of `N_s`; equality only for scalar content alone. Check (review F2 note, not a manuscript claim): under replica (II), `c_A = -N_tot/12 < 0` while `c_T > 0` needs `N_tot > 24`, so the no-go is not an artefact of (I) for positive `G_T`.
6. **Clarifications of existing text (no error found).** (a) appG: the cone-prefactor statement is the `S_BH` statement when the delta is continued, and needs the stated convention otherwise. (b) The coefficient equality `G_T = G_A` sits inside Hypotheses 5 and 6 of `thm:mT`; it is not flagged there as a separate physical condition. (c) `thm:Geff` "specified endomorphism" leaves `A_{1,R,s}` variable-dependent for composite `G`; recorded, ch08 not edited.

Nothing here derives `ass:EE`, stationarity, the map `Theta -> G`, or any value or sign of `G_eff`. Problem B stays OPEN.

## Target and status

Unchanged from r1: Problem B (`sec:status-B`), OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL; appH, ch17 and `reports/ledger.md` agree; ch17 critical-path set A, B, C, D1, E, F, G-derived, N. Original target: `delta S_D = 0` at fixed volume for the non-conformal tensor block, with the area term and the map to the emergent metric. This package addresses B2 and the normalisation half of B1 only. Dependencies: F, A, C, D1. Classification of this package: PROGRAMME-CONDITIONAL.

## Source reading

Digest + targeted reads for this revision: re-read `proposal-r1.md` and `review-r1.md`; re-checked anchors and labels by search in `chapters/`. The r1 full scan and the reviewer's full scan stand; I did not re-scan for r2 and make no new full-scan claim. Literature as in r1 (Solodukhin arXiv:1104.3712 equations read; Jacobson arXiv:1505.04753; Susskind-Uglum abstract and Crossref level). Not read: other proposals' reviews.

## Research and reasoning

Unchanged from r1, sections 1-10. Added in r2 only:
- F1 convention check: with `R_sing = 4 pi (1-n) delta` continued into `E`, `Tr K` gains `-(1-n) Q A/(4 pi s)` and `Delta S = -2 pi Q A <phi^2>` relative to the entropy computed without the delta (`cone_checks.py`, part 2). So the entropy without the delta is `S_ent`, with it `S_BH = S_ent - Q`. The difference between `S_ent` and `A/(4 G_eff)` is `Q`; between `S_BH` and `A/(4 G_eff)` it vanishes.
- F2 note: `c_A^(II) = -N_tot/12`; `c_T = c_A^(II)` would need `N_tot = 16`, where `1/G_T < 0`.

## Claim classification

| Claim | Class |
|---|---|
| Flat-cone coefficient; `S = A/(4G_ind)` for `Q = 0`; `Delta S = -2 pi tr Q <phi^2> A` | established |
| Replica (I) entropy equals the `Lambda^2` coefficient of `thm:Geff` in `(G, rho, dTheta)` | conditional |
| `E_s = R_G/4 + T^2/16 + TT'/8`; `tr B^2 = -X` | established identities |
| (II): `-1/12` per component, ratio `-1/2` | conditional, not used |
| TT eigenvalues; `c_T = N_tot/6 - 4`; `1/G_A - 1/G_T = 2 Lambda_v^2/pi` | established computation, conditional on class and gauge |
| Reduction `m_T = 0` and `G_T = G_A` | conditional (Jacobson tensor step, Fierz-Pauli structure) |
| Item 6 clarifications | established (reading of merged text) |
| Ghost-weighted cone sum as a physical entropy; `ass:EE`; stationarity; map; `G_eff` | unresolved |

## Proposed changes

Three files plus two BibTeX entries. No label is touched or added. Labels verified present exactly once (grep over `chapters/`): `sec:status-F`, `sec:status-B`, `sec:replica-cone`, `ass:emergent-op`, `thm:Geff`, `eq:universal-R`, `eq:first-law`, `eq:first-law-zero`, `eq:deltaA-G`, `eq:Top-improved`, `eq:mass-identity`, `prop:ward`, `ass:EE`, `thm:mT`, `rem:ch3-trace-quadratic`, `ch:entanglement-equilibrium`, `app:modular`, `eq:Geff-structure` (newly used here; defined ch08 l. 223). Anchors verified to occur exactly once: appH "Those inputs are not supplied by the displayed microscopic"; appG "with the prefactor identified from the Seeley"; appG "The area term in \(S_D\) is the standard heat-kernel result"; ch07 "borrows a geometric identity used in Jacobson". `\LUV` and `\Geff` are defined. The integrator normalises CRLF.

### Item 1: appH, Section `sec:status-B`
Anchor (once): "...Those inputs are not supplied by the displayed microscopic action. Problems~B, C, D, F and~G remain open." Kept: everything before and after; the block goes between that sentence and `\section{Problem C: conformal mode and Cassini}`.

```latex
\paragraph{Replica cone coefficient of the Poisson-limit operators and the area term of the first law (conditional; not closure).}
Keep the setting of the Presentation~A Poisson-limit paragraphs of Section~\ref{sec:status-F}: four matrix coordinates, the Poisson limit, the Euclidean section \(\eta=\delta\), the scalar operator \(\mathcal O_s\), the connection operator \(\mathcal O_v\) acting on the internal index of \(a^\mu\) in background gauge, the ghost operator of weight \(-2\), \(G=\rho\,g_\rho\) with \(\sqrt{|G|}=\rho^2\), Assumption~\ref{ass:emergent-op}, and one proper-time limit \(s_{\min,s}=\Lambda_{\mathrm{UV},s}^{-2}\) per sector, shared by the effective action and the replica entropy. Only the \(\Lambda_{\mathrm{UV},s}^2\) term is compared, for constant \(\Lambda_{\mathrm{UV},s}\); neither a value of \(G_{\mathrm{eff}}\) nor the relation \(S=A/4G\) is assumed.

\emph{Replica on the matrix chart.} Let \(Z_n\) be the partition function on the \(n\)-sheeted cover of the chart \(x\), branched over a two-surface \(\Sigma\), with every background field (\(\Theta\), hence \(G\), \(g_\rho\), \(\rho\), the connections and the endomorphisms) pulled back. Then \(G\) and \(g_\rho\) are conical with the same angle \(2\pi n\) and \(\rho\) is a regular density of the chart: the cone is on \(G\) and \(g_\rho\) together. For a Laplace-type sector whose connection and endomorphism stay bounded on the cover, the leading surface term of the heat trace is the flat-cone term~\cite{Solodukhin2011},
\[
  \operatorname{Tr}e^{-s\mathcal O}\big|_n-n\operatorname{Tr}e^{-s\mathcal O}\big|_1
  =\operatorname{tr}\mathbb I\;\frac1{12}\Bigl(\frac1n-n\Bigr)\frac{A_G(\Sigma)}{4\pi s}+O(s^0),
\]
independent of the connection and of the endomorphism. The fibre index of \(\mathcal O_v\) is internal, so the fibre is not rotated around \(\Sigma\) by a Levi-Civita holonomy. With \(S=(1-n\partial_n)(\ln Z_n-n\ln Z_1)|_{n=1}\) and \(\ln Z_n=\tfrac12\sum_sw_s\int\mathrm{d}s\,s^{-1}\operatorname{Tr}e^{-s\mathcal O_s}\),
\[
  S=\frac{A_G(\Sigma)}{48\pi}\sum_sw_s\operatorname{tr}\mathbb I_s\,\Lambda_{\mathrm{UV},s}^2
\]
(the \(\mu_s^2\) terms of Theorem~\ref{thm:Geff} subtracted). The same limits in Equation~\eqref{eq:universal-R} give, for the coefficient of \(\int\sqrt{G}\,R_G\) when the endomorphisms carry no explicit curvature, \(1/(16\pi G)=\sum_sw_s\operatorname{tr}\mathbb I_s\,\Lambda_{\mathrm{UV},s}^2/(192\pi^2)\). Hence \(S=A_G(\Sigma)/(4G)\) with that \(G\), in the variables \((G,\rho,\partial\Theta)\) of the contact-term paragraph below: for these operators the coefficient of \(\delta A\) in Equation~\eqref{eq:first-law} is the \(\LUV^2\) coefficient of Theorem~\ref{thm:Geff}, namely the coefficient \(A=1/(12\pi)\) of Equation~\eqref{eq:Geff-structure} per unit weighted fibre trace, as in the sector-sum paragraph of Section~\ref{sec:status-F}, and it is determined by the operators and the cutoff. This holds for the replica and variables just stated; the scope of the whole block is given at the end of the second paragraph below.

\emph{Contact term.} If an endomorphism is \(E_s=E_{0,s}+Q_sR_G\) and \(R_G\) is continued onto the cone with its conical delta, the heat trace gains \(-(1-n)\operatorname{tr}Q_s\,A_G/(4\pi s)\) and the entropy changes by \(-\tfrac{A_G}{8\pi}\sum_sw_s\operatorname{tr}Q_s\Lambda_{\mathrm{UV},s}^2=-2\pi A_G\sum_sw_s\operatorname{tr}Q_s\langle\phi^2\rangle_s\), \(\langle\phi^2\rangle_s=\Lambda_{\mathrm{UV},s}^2/(16\pi^2)\). This is the contact term of Susskind and Uglum~\cite{SusskindUglum1994}, \(S_{\mathrm{BH}}=S_{\mathrm{ent}}-Q\) in Equations~(322)--(323) of~\cite{Solodukhin2011}, with \(S_{\mathrm{BH}}\) built from the coefficient \(\operatorname{tr}(\tfrac16-Q_s)\) of Theorem~\ref{thm:Geff}. With \((G,\rho,\partial\Theta)\) as independent variables, the scalar endomorphism \(E_s=-\tfrac12\Box_G\ln\rho+\tfrac14|\partial\ln\rho|_G^2\), the connection endomorphism with \(\operatorname{tr}E_v=4E_s+\operatorname{tr}(B_\sigma B^\sigma)\), \(\operatorname{tr}B_\sigma=0\), \(\operatorname{tr}(B_\sigma B^\sigma)=-X\), and the ghost operator \(-\mathcal O_s\) all have \(Q=0\) and are bounded on the pulled-back cover, so the contact term vanishes sector by sector.

\emph{Dependence on the independent variables.} The Weitzenb\"ock identity quoted in the paragraph on the torsion invariant gives \(E_s=\tfrac14R_G+\tfrac1{16}T_{\lambda\mu\nu}T^{\lambda\mu\nu}+\tfrac18T_{\lambda\mu\nu}T^{\mu\lambda\nu}\) and \(\operatorname{tr}(B_\sigma B^\sigma)=-T_{\lambda\mu\nu}T^{\lambda\mu\nu}\) (the first checked at random two-jets of a closed \(\omega\), for both signatures). With the coframe torsion in place of \(\partial\Theta\) as independent variable, the scalar operator has \(Q_s=\tfrac14\), and its coefficient \(\mathcal A_{1,R,s}\) is \(\tfrac16-\tfrac14=-\tfrac1{12}\) per component instead of \(\tfrac16\), of opposite sign. The coefficient \(\mathcal A_{1,R,s}\) of Theorem~\ref{thm:Geff} is therefore not a function of these operators alone. With \(N_{\mathrm{tot}}=N_s+2\) as in the Poisson-limit paragraph, the weighted coefficient \(c\) of \(\sqrt G\,R_G\) in \(\operatorname{tr}(R_G/6-E)\) is:
\begin{center}
\begin{tabular}{@{}lcc@{}}
\toprule
sector (weight) & \(c\) in \((G,\rho,\partial\Theta)\) & \(c\) in \((G,\text{torsion})\)\\
\midrule
\(N_s\) scalar components & \(N_s/6\) & \(-N_s/12\)\\
connection, 4 components & \(2/3\) & \(-1/3\)\\
ghost, weight \(-2\) & \(-1/3\) & \(1/6\)\\
total & \(N_{\mathrm{tot}}/6\) & \(-N_{\mathrm{tot}}/12\)\\
\bottomrule
\end{tabular}
\end{center}

\emph{Which geometry carries the cone.} The first column is the replica entropy above, \(S=(\LUV^2A_G/8\pi)\,c\), with \(\rho\) regular. The cone on \(G\) can instead be carried by the Poisson structure: for \(\Theta^{12}=1/f(x^1,x^2)\), \(\Theta^{34}=1\), one has \(G_\perp=f^2\delta\) and \(\rho=f\), and \(f=|z|^{n-1}\) makes \(G\) conical of angle \(2\pi n\) with \(\rho\propto r^{n-1}\) singular, \(g_\rho\) singular, and torsion unbounded, \(|T|^2\propto(n-1)^2/u^2\) at proper distance \(u\) from \(\Sigma\). Then \(E_s\) contains \(-\tfrac12\Box_G\ln\rho=\pi(1-n)\delta_\Sigma\), a contact term with \(Q=\tfrac14\), and \(\mathcal O_s\) reduces to a Bessel problem of index \(\sqrt{m^2+((n-1)/2)^2}/n\). With the branch regular at \(m=0\), the first-order coefficient is that of the second column, for the scalar and ghost and for the components of \(a^\mu\) in this block class (a statement conditional on that branch and not used below; the factor \(-\tfrac12\) is also what the local \(a_1\) coefficient with the delta function, \(Q=\tfrac14\), gives). The two choices differ by the factor \(-\tfrac12\) in every sector (for the branch stated). The first is the replica of the same state, since \(\operatorname{Tr}\rho_D^n\) is built on the cover of the same background; the second changes the background with \(n\) and corresponds to a smooth-coframe reading of the induced action. Only the first is used in the identification above.

\paragraph{Normalisation of the tensor kinetic term against the area coefficient (conditional; not closure).}
Assume Equation~\eqref{eq:first-law-zero} for every small diamond, every unit timelike direction of \(\xi\) and the fixed-volume variations of the tensor block, with the geometry of Equation~\eqref{eq:deltaA-G} in the form of~\cite{Jacobson2016}, in which \(\delta A|_V\) is proportional to \(G^{(1)}_{00}[h]\), and write \(1/(4G_A)\) for the coefficient of \(\delta A\). A symmetric tensor whose contraction with every timelike unit vector vanishes is zero, so the condition is the tensor equation \(G^{(1)}_{\mu\nu}[h]=8\pi G_A\,\delta\langle T^{\mathrm{op}}_{\mu\nu}\rangle[h]\) up to a term proportional to \(\eta_{\mu\nu}\). For a tensor block with the Fierz--Pauli structure of Equation~\eqref{eq:Top-improved} this requires both \(m_T=0\) and \(G_T=G_A\), where \(1/(16\pi G_T)\) is the coefficient with which the quadratic action whose metric response defines \(T^{\mathrm{op}}\) carries the linearised Einstein form. The second condition is not implied by the first, by the identification of the area prefactor with the coefficient of Theorem~\ref{thm:Geff}, or by Proposition~\ref{prop:ward}: it equates the coefficient of the quadratic term of the block with the coefficient of the area term.

In the class of the Poisson-limit paragraphs, about a constant \(\bar\Theta\), the induced \(\LUV^2\) quadratic form on the two modes with \(\delta\rho=0\) is \(-\tfrac{\LUV^2}{32\pi^2}\bar\rho^{2}p_\eta^2\,(1-N_{\mathrm{tot}}/24)\,\mathcal M\), with \(\mathcal M\) the tree-level kernel of Remark~\ref{rem:ch3-trace-quadratic}. A term \(c\,\rho R[g_\rho]\) has eigenvalue \(-c/4\) on these modes, so the form is that of an Einstein term with \(c_T=N_{\mathrm{tot}}/6-4\), whereas the area coefficient above, for the replica of the first paragraph, is \(c_A=N_{\mathrm{tot}}/6\). With a common cutoff \(1/G_T=(N_{\mathrm{tot}}-24)\LUV^2/(12\pi)\) and \(1/G_A=N_{\mathrm{tot}}\LUV^2/(12\pi)\); with the connection sector at its own limit \(\Lambda_{\mathrm{UV},v}\), \(1/G_A-1/G_T=2\Lambda_{\mathrm{UV},v}^2/\pi\), independent of \(N_s\). The difference is the term \(\rho^2X\) of the connection sector, which is bounded on the replica cover and contributes no entropy but contributes to the quadratic form; for scalar content alone \(G_T=G_A\). In this class (Poisson limit, Euclidean section, background Feynman gauge, one loop, \(\LUV^2\) term, the two modes with \(\delta\rho=0\)) and for the replica of the first paragraph, the induced term therefore has the Einstein structure but not the coefficient that \(G_T=G_A\) requires, for every \(N_s\) and every \(\Lambda_{\mathrm{UV},v}>0\).

These statements are for the Poisson-limit operators of the preceding paragraphs at one loop, for the \(\LUV^2\) term, the replica above and the background gauge stated. They do not derive Assumption~\ref{ass:EE}, fixed-volume stationarity of the tensor block, or the identification of \(G\) with the emergent metric (Assumption~\ref{ass:emergent-op}); they do not treat the tree-level term (of lower order in momentum and not of Einstein form), fermions or additional scalars, Moyal corrections at the cutoff, the mixing of \(\Phi\) with \(a^\mu\), edge modes or the interpretation of the ghost-weighted sum as an entropy, or the logarithmic terms; the off-shell quadratic form is gauge dependent; and they give no value or sign of \(G_{\mathrm{eff}}\). Problems~B, C, D, F and~G remain open.
```

### Item 2: appG, Section `sec:replica-cone`
(a) Anchor (once): "with the prefactor identified from the Seeley--DeWitt coefficient that multiplies the deficit. This is the standard result used in Chapter~6 and Appendix~B." Replaces those two sentences only; the equation before and "The conditional heat-kernel identity of Theorem~\ref{thm:Geff}" onward stay.

```latex
with the prefactor given by the Seeley--DeWitt coefficient that multiplies the
deficit. This is the standard cone computation for operators whose
endomorphism contains no explicit curvature coupling, on a replica geometry on
which the connection and the endomorphism stay bounded. For
\(E=E_0+QR\) with the conical delta of \(R\) not continued into \(E\), the
replica entropy differs from
\(\operatorname{Area}(\Sigma)/(4G_{\mathrm{eff}})\), with
\(G_{\mathrm{eff}}\) the curvature coefficient of Theorem~\ref{thm:Geff}, by
a contact term proportional to \(\operatorname{tr}Q\); if the delta is
continued into \(E\), the difference vanishes. For operators built from a
composite metric the curvature coefficient depends on the independent variables
chosen (Section~\ref{sec:status-B}). Chapter~\ref{ch:entanglement-equilibrium}
and Appendix~\ref{app:modular} use \(1/(4G_{\mathrm{eff}})\) as the name of
the coefficient of \(\delta A\).
```

(b) Status sentence. Anchor (once): "The area term in \(S_D\) is the standard heat-kernel result." Replaced by:

```latex
The area term in \(S_D\) is the standard heat-kernel term for the operators of
Section~\ref{sec:replica-cone}.
```

### Item 3: ch07, remark "What the theorem does not hide"
Anchor (once): "borrows a geometric identity used in Jacobson's argument." Insert after "argument."; the rest stays.

```latex
The cancellation of the Einstein-operator terms
in~\eqref{eq:mass-identity} also uses that the coefficient of
\(\mathcal E_{\mu\nu}\) in the stress response~\eqref{eq:Top-improved}
equals the coefficient of \(\mathcal E_{\mu\nu}\) in the area
term~\eqref{eq:deltaA-G}. This equality is part of the content of
Hypotheses~5 and~6 as written; it is not supplied by Hypothesis~4 or by the
identification of the area prefactor with \(\Geff\)
(Section~\ref{sec:status-B}).
```

### Item 4: bibliography (integrator adds; unchanged from r1, verified by the reviewer)
```bibtex
@article{Solodukhin2011,
  author  = {Solodukhin, Sergey N.},
  title   = {Entanglement Entropy of Black Holes},
  journal = {Living Reviews in Relativity},
  volume  = {14},
  number  = {1},
  pages   = {8},
  year    = {2011},
  doi     = {10.12942/lrr-2011-8},
  eprint  = {1104.3712},
  archivePrefix = {arXiv}
}

@article{SusskindUglum1994,
  author  = {Susskind, Leonard and Uglum, John},
  title   = {Black hole entropy in canonical quantum gravity and superstring theory},
  journal = {Physical Review D},
  volume  = {50},
  pages   = {2700--2711},
  year    = {1994},
  doi     = {10.1103/PhysRevD.50.2700},
  eprint  = {hep-th/9401070},
  archivePrefix = {arXiv}
}
```

### Stale passages elsewhere
ch08 `thm:Geff` "includes the specified endomorphism": not edited (Problem-F follow-up). ch06 `eq:first-law` and ch17: unchanged.

## Verification scripts

Unchanged from r1, all in this folder with `.out.txt`: `cone_checks.py`, `operator_identities.py`, `verify_E_torsion.py`, `tt_quadratic_forms.py`, `sector_table.py` (contents as listed in r1). No new script in r2; the F2 note is arithmetic (`-N_tot/12` against `N_tot/6 - 4`). These are checks, not proofs.

## Decisions Taken

1. Replica (I) is used for B2; (II) is reported as conditional and unused (same state replicated; (II) changes the background with `n`).
2. New appH text stays in `sec:status-B` after the replica paragraph.
3. The appG and ch07 edits are clarifications of convention and of what the hypotheses already contain, in the reviewer's wording; no claim that merged text is false.
4. `G_T` is defined on the `delta rho = 0` modes.
5. No Kabat citation (the index is internal).
6. The hypothesis class is stated in the no-go sentence itself; relaxations are listed, not computed here.
7. Only the Feynman background gauge is treated.
8. The `A` clash is resolved by citing `eq:Geff-structure` explicitly.

## Milestone assessment

M2: bounded no-go, as in r1, now stated with its replica and class. M3 withdrawn (no error in merged text). Not M1: no critical-path step is derived.

## Status-label recommendation

None. B and F remain OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL; the ch17 set A, B, C, D1, E, F, G-derived, N is unchanged. No label edit appears above.

## Author decision needed

None. Spacetime stays emergent: the cone is on the composite `G` built from `Theta`.

## Remaining open step

Not derived: stationarity for the tensor block (B1), the map to the emergent metric (B3, A), `ass:EE`. Not examined: the tree-level term, Moyal corrections, edge modes and the ghost-weighted entropy, the `a_2` terms, positivity (Fisher information, N), an area-law test for the matrix regularisation.

The no-go depends on: Poisson limit; Euclidean section; bosonic content `N_tot = N_s + 2`; Feynman background gauge; one loop; `Lambda^2` term; replica (I); constant `Theta_bar` and the `delta rho = 0` modes; the Fierz-Pauli reading of `T^op`. Ranked avenues that could close the `G_T != G_A` gap (listed only; none explored here; a separate follow-up package takes them):
1. **Content.** Fermions and extra scalars or gauge fields whose endomorphism terms in `T^2` cancel `rho^2 X` on the TT modes, i.e. shift `1/G_T - 1/G_A` by `+2 Lambda_v^2/pi`. Most direct and algebraic.
2. **Gauge fixing.** Non-minimal or non-Laplace gauges; the gauge dependence of the off-shell form; whether a gauge-invariant (graviton-propagator, on-shell) coefficient differs.
3. **Tensor-block identification.** A tensor block other than the `delta rho = 0` modes of `a^mu`; `Phi`-`a` mixing and the Presentation-B frame coupling.
4. **Tree-level term and the 014 class.** A derived extra stress or tree-level Einstein structure (CP^{1,2}) supplying `G_T`.
5. **Moyal and finite-cutoff corrections** to the `Lambda^2` coefficients.
6. **Curved or non-constant backgrounds**, and the `a_2` partners.
7. **Replica choice.** A (II)-type or edge-mode-corrected ghost-weighted entropy changes `c_A`; for (II) the sign structure already prevents equality at positive `G`.

## Special instructions for the gatekeeper

- Do not read this as closing B or B2. The match is the Sakharov-type identity for operators with `Q = 0` in `(G, rho, dTheta)`; the TT result is a bounded obstruction in the stated class and replica.
- Check that each of F1-F6 is implemented as in the changelog. The five scripts are unchanged and may be re-run.
- Do not assert that the merged appG or ch07 text was erroneous; the insertions are clarifications.
- Check that the appH first paragraph now ends with a scope pointer and that the second paragraph carries the single closing status sentence.
