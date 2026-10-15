# Proposal 009-matrix-coords-N8, round 1

## Result

Target: develop the "more than four matrix coordinates" extension of `def:matrix-coords` that proposal 008 ranked first, and find out what it buys for the full-GR (matrix-derived) derivation. It derives nothing on the critical path. The package contains one conditional definition and one bounded conditional appH paragraph. Findings (D = number of Hermitian matrices; a 4-dimensional symplectic leaf, Poisson limit, constant Lorentzian target form `eta_IJ`; hypothesis class H_D):

1. **(Correction to 008's "Decisions Taken", not to manuscript text.) More matrices do not make the operator metric conformal to the embedding metric.** For every D >= 4 and every real Lorentzian induced metric `g`, the operator metric `G = (theta^T g theta)^{-1}` is not `c g`. Proof: `G = -g M^2`, `M = g^{-1} omega` is g-antisymmetric; `G = c g` needs `M^2 = -c`, so (real M) `det M = c^2 > 0`, but `det M = Pf(omega)^2/det g < 0`. Exact-rational check plus random embeddings D = 4..11. The hypothesis that carries this no-go is "the symplectic leaf is 4-dimensional": for Euclidean or (2,2) `g` an orthogonal complex structure removes it (checked). So 008's claim that N >= 8 "removes both obstructions" is true only for the field-content obstruction and then only on curved backgrounds (item 2); the second obstruction is D-independent in H_D.
2. **The 3-versus-6 linear-response obstruction does not change on the 008 background; it changes on curved branes.** About a flat brane with constant `theta`, the D-4 normal fluctuations enter the induced metric only at second order, so the rank of the Einstein operator on the linear image is 3 for every D (checked D = 4..11). About a brane with generic second fundamental forms the rank is `min(6, D-1)` (checked D = 4..11, exact rational, also with the normal part of the tree-level equation of motion imposed): all six conserved sources are reachable from D = 7 (D - 1 >= 6). Including the density scalar the gauge-invariant function count is `D-1 >= 7`, i.e. D >= 8, which is 008's count. All of this is kinematic. No field equation is shown to be Einstein's.
3. Extra content that comes with the extension: `D-4` additional scalar moduli (brane position). They are not covered by `ass:locked-block` (that is about internal directions of `Phi`). If they carry the gravitational response they are light, so they are additional infrared fields to be gapped or constrained; if they are gapped they decouple and the flat-brane result of item 2 returns.
4. Relation to the one-loop IKKT literature (abstracts only): the extra conserved stress that 008 says is needed has candidate counterparts in the one-loop terms of Kumar-Steinacker and Steinacker (anharmonicity tensor, dilaton/axion, "mirage matter"); and the fuzzy-extra-dimension mechanism of arXiv:2303.08012 corresponds to relaxing exactly the hypothesis that carries item 1 (leaf dimension > 4). Neither is derived or checked here.

Not established: that the matrix action induces any Einstein-type equation for `G`; that the extra scalars are gapped; the dictionary `Phi <-> tangent-plane frame`; any `G_eff`.

## Target and status

Problems A, D1, E (by dependency), F (primary: `ass:emergent-op`); B, C by dependency. Appendix H (re-read, current text after the 008 integration, commit 3ab80c9): A "OPEN; CRITICAL PATH for the matrix-derived label; PROGRAMME-CONDITIONAL"; D, F "OPEN; CRITICAL PATH; PROGRAMME-CONDITIONAL"; E "OPEN; CRITICAL PATH for the matrix-derived label; PROGRAMME-CONDITIONAL". Chapter 17 (`sec:ch17-done`) lists A, B, C, D1, E, F, G-derived, N; no discrepancy with Appendix H or `CLAUDE.md`. Original target (F): discharge `ass:emergent-op` or replace it by a derived ingredient. Not met. PROGRAMME-CONDITIONAL. A bounded conditional extension plus bounded no-go and rank results.

## Source reading

**Full scan.** I read, in this session, all 30 files of the chapters manifest: ch01-ch18, appA, appB, appC, appD, appE, appF, appG, appI, appJ, appK, appL in full, and appH in full for the Problem A-F, G, H, N sections and the 005/008 paragraphs (Problems I and J: ledger label and keyword scan only, no matrix content). The digest was STALE after the concurrent integration of 008 (I could not refresh it; it lives in `scratch/`); I therefore read the working-tree appH directly, including the integrated 008 paragraph (appH lines 1815-1824, followed by `\section{Problem G: HBEV}` at 1826). Previous proposals read: 008 r2 and review r2, ledger entries for 002-008, 003 Lemma 2 text.

## Research and reasoning

**Setting (conditional; standard semiclassical reading).** `D` Hermitian operators `X^I`, `eta_IJ = diag(-1,1,...,1)` as in `eq:Smatrix` (so `ass:lorentzian` is retained, not derived). Semiclassical configuration: `x^I(y)` on a 4-manifold with nondegenerate Poisson bivector `theta`; `Theta^{IJ} = theta^{ab} d_a x^I d_b x^J` (rank 4); `Tr -> int rho d^4y`. Induced metric `g = dx^T eta dx`. A scalar fluctuation `[X^I, phi]` has Poisson-limit kinetic term `K^{mu nu} d phi d phi` with `K = theta^T g theta` (this is 008's `K = theta^T g theta`), so the metric seen by commutator operators is `G = K^{-1} = omega g^{-1} omega^T`, `omega = theta^{-1}`. For D = 4, `x^I = y^I` gives 005/008's `G`. Equivalent frame form: `K^{mu nu} = eta_IJ V^{I mu} V^{J nu}`, `V^{I b} = theta^{ab} d_a x^I`, an over-complete set of D vector fields spanning a 4-dimensional space (the Hamiltonian vector fields of the `x^I`).

**(1) No-go, D-independent** (script `check_conformal_nogo.py`). `G + g M^2 = 0` and `det M = Pf^2/det g` verified in exact rationals for 30 random Lorentzian `g`; random embeddings D = 4..11 give minimum relative residual `|G - c g|/|G|` between 0.22 and 0.42 (closed-form optimal c); Euclidean and (2,2) contrasts have `G` proportional to `g`. This extends `rem:ch3-moyal-check` and the 008 paragraph. It bounds the hypothesis class: real symplectic leaf of dimension 4, Poisson limit, real Lorentzian induced metric. Relaxations inside the core: leaf dimension > 4 (the fuzzy-K / covariant-quantum-space structure, in which `K^{mu nu}` of the 4D base includes fibre directions), complex or (2,2) induced metrics (these would change E), Moyal corrections. None is pursued here.

**(2) Linear response** (script `check_brane_rank.py`, exact rational). Chart `y` with constant `theta` (so `rho_y` is constant: in this chart the density scalar of 008 is not a separate variable; the 7 = 10 - 3 count of (G,rho) modulo diffeos corresponds to Sym^2 modulo volume-preserving diffeos). Perturbation `delta x^I = A^I e^{ip.y}`, `A = xi^mu d_mu x + phi_i n_i`. Then `delta g = p (.) (g xi) - 2 phi_i II^i`, `delta G = -G (theta^T delta g theta) G`. Checks: the Hamiltonian choice `xi = theta^T p` gives `delta G = p (.) (G xi)`, a linearised G-diffeo (matrix gauge), True in all runs. Table (rank of Einstein operator of `G` on the image; maximum 6 = conserved sources):

| D | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|----|----|
| flat brane (II = 0) | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| generic II | 3 | 4 | 5 | 6 | 6 | 6 | 6 | 6 |
| K-traceless II | 3 | 4 | 5 | 6 | 6 | 6 | 6 | 6 |

The D = 4 entry reproduces 008's rank 3. Caveats: WKB-type local analysis (background `g`, `theta`, `II` frozen at a point, normal modes enter at order `p^0`, tangent modes at order `p^1`); the Gauss-Codazzi relations between `II` and curvature are not imposed; K-traceless II is only the normal part of `K^{mu nu}(d_mu d_nu x)^perp = 0`; rank samples are one random draw per entry (checks, not proofs). A generic-rank statement needs only one successful draw for the lower bound; the upper bounds are the trivial `min(6, D-1)` counts.

**(3) Scalar content and tree level.** In the Poisson limit the normal fluctuation `phi^i` has a kinetic operator of the same form as the scalar sector of the 005 paragraph (`-rho^{-1} d(rho K d .)`); sign and healthiness are not established (cf. `rem:ch3-trace-quadratic`, which makes no energy claim). So at tree level about a flat brane there are `D-4` such scalars next to the gauge sector; none is a graviton. This is conditional on the Poisson limit. `ass:locked-block` does not cover them.

**(4) Bookkeeping with 005.** In 005, `N_tot = N_s + 2` where `N_s` counts real components with operator `O_s`. Under 005's hypotheses and on its flat constant-`Theta` background the D-4 normal components are such components, so `N_tot = (D-4) + N_other + 2`, and for the pure bosonic matrix sector `N_tot = D-2`. Then the net coefficient on the two TT-type modes is `1 - N_tot/24 = (26-D)/24`, positive for D < 26 (D = 4: 11/12; D = 10: 2/3), so the 005 criterion `N_tot > 24` is not met by the matrix sector alone for any D that is physically considered. Conditional bookkeeping only: it uses 005's formula, ignores curvature couplings of `phi^i` through `II`, fermions, mixing, and says nothing about `G_eff`.

**(5) Local Lorentz and frames (D1; bounded remark, nothing derived).** The orthonormal frames `eps^I{}_A` of the brane tangent plane satisfy `eps^T eta eps = eta_AB`; their redundancy is `SO(3,1)` acting on `A`, and the tangent-plane stabiliser in the target group `SO(1,D-1)` is `SO(1,3) x SO(D-4)`. This is a geometric origin of the structure used in Chapter 10 (`G_int` containing `SO(3,1)` acting on the internal index, locked to the tangent index): the global symmetry is that of the matrix action itself (`eta_IJ` contraction). It is a global symmetry and a frame redundancy, not a derivation of a local gauge symmetry, a connection or its dynamics. The Gauss-Weingarten connection is the Levi-Civita connection of the *induced* `g`, torsion-free by construction, whereas the operators see `G`; the `G`-coframe is `e_{A mu} = e_A{}^alpha omega_{alpha mu}` (as in 005 for D = 4). I make no claim that it carries independent dynamics. Whether `Phi^I{}_A` can be identified with `eps^I{}_A` (and so with `<Phi>/v`) is a conjecture; on D = 4 it was shown in 008 to fail to be tangent to the vacuum manifold of `eq:V` for most directions, and that analysis is not redone for D > 4.

**(6) Lemma 2 (003).** Its hypotheses H1-H4 fail here (kinetic metric built from `Theta` and the embedding; the metric perturbation is a background-dependent, not fixed, linear image of the fluctuations). No claim.

**(7) Literature** (checked 2026-10-14 by fetching the arXiv abstract pages; full texts not read; content below is from the abstract summaries only).
- arXiv:2303.08012, H. C. Steinacker, "One-loop effective action and emergent gravity on quantum spaces in the IKKT matrix model" (v1, 14 Mar 2023; same record as bib key `Steinacker2023`, JHEP 05 (2023) 129: journal data in the bib entry not independently verified). Reported: Einstein-Hilbert action at one loop on a brane with compact fuzzy extra dimensions, Newton constant set by the Kaluza-Klein scale.
- arXiv:2312.01317, K. Kumar and H. C. Steinacker, "Modified Einstein equations from the 1-loop effective action of the IKKT model" (v1, 3 Dec 2023). Reported: generalised Einstein equations with dilaton and axion contributions and an "anharmonicity tensor" `C_{mu nu}`.
- arXiv:2601.08031, H. C. Steinacker, "Modified gravity at large scales on quantum spacetime in the IKKT model" (12 Jan 2026). Reported: modified Einstein equations with an extra geometric tensor ("mirage matter") and extra non-Ricci-flat modes.
- Already in the repository: IKKT1997, Steinacker2010, Steinacker2016Gravity (arXiv:1606.00769, abstract re-checked: linearised Einstein equations under conditions and with an IR cutoff, internal twisted bundle over S^4).
Comparison with this package (conditional, not verified beyond abstracts): (a) 008's "additional conserved stress that would have to be derived" has candidate analogues in the one-loop extra tensors of the Kumar-Steinacker and 2026 papers; whether they absorb the codimension in H_D is not examined. (b) In those papers the quantum space is higher-dimensional (4D brane times fuzzy K), which is the relaxation of "leaf dimension 4" that removes item 1; my construction keeps the leaf 4-dimensional and uses the transverse embedding functions, so it is the simpler member of the family and shares its counting but not its covariance mechanism. (c) Their Newton constant comes from the KK scale of K, i.e. from a sector that the present extension does not contain; so this package is no step towards `G_eff`.

## Claim classification

- Established (exact algebra): `G = -g M^2`, `det M = Pf^2/det g`, no-go `G != c g` for every D >= 4 and real Lorentzian `g` (4D leaf); Euclidean and (2,2) contrasts.
- Established (exact rational checks, one draw per entry): rank table of item (2), gauge direction is a G-diffeo.
- Conditional: the semiclassical reading of the extended definition; scalar content statement (3); `N_tot = D-2` bookkeeping (4); WKB-level linear response.
- Counting argument: `D-1 >= 7` (D >= 8), necessary only.
- Conjecture: `Phi <-> eps` identification; correspondence with one-loop extra tensors; leaf dimension > 4 removes item 1.
- Unresolved: any field equation for `G`; gap of the normal scalars; E; D1 dynamics; `G_eff`.

## Proposed changes

Everything below is conditional and scoped; no label, priority, completion classification or Chapter 17 text is touched. Spacetime and metric stay emergent: `eta_IJ` is a fixed contraction of matrix indices as in `eq:Smatrix`, and no metric appears in the action.

**File 1: `chapters/ch03-matrix-action.tex`.** Insert after the end of `def:matrix-coords`. Anchor (occurs once; verified by `verify_anchors_labels.py`): the last lines of the definition, "  analysis with a \(c\)-number \(\Theta^{\mu\nu}\).\n\end{definition}". Nothing is replaced; `def:matrix-coords`, `eq:NC` and `eq:Smatrix` are unchanged. New label `def:matrix-coords-ext` (absent; verified). Labels used (each verified once): `def:matrix-coords`, `eq:NC`, `eq:Smatrix`, `ass:lorentzian`, `ass:locked-block`, `rem:ch3-moyal-check`, `eq:g-from-e`, `ass:emergent-op`.

```latex
\begin{definition}[Extended matrix coordinates (conditional extension)]
  \label{def:matrix-coords-ext}
  Let \(D\ge4\) and let \(\hat X^I\), \(I=0,\dots,D-1\), be Hermitian
  operators on \(\mathcal{H}\) with
  \([\hat X^I,\hat X^J]=i\Theta^{IJ}\), \(\Theta^{IJ}=-\Theta^{JI}\).
  Matrix indices are contracted with the fixed constant form
  \(\eta_{IJ}=\mathrm{diag}(-1,1,\dots,1)\), exactly as \(\eta_{\mu\nu}\)
  is used in~\eqref{eq:Smatrix}, which is then read with \(I,J\) in place
  of \(\mu,\nu\). The case \(D=4\) is Definition~\ref{def:matrix-coords}.
  In the semiclassical regime a configuration is a map \(y\mapsto x^I(y)\)
  from a four-dimensional manifold carrying a nondegenerate Poisson
  bivector \(\theta^{\alpha\beta}\), with
  \(\Theta^{IJ}=\theta^{\alpha\beta}\partial_\alpha x^I\partial_\beta x^J\)
  and \(\operatorname{Tr}\to\int\mathrm{d}^4y\,\rho\). Two tensors are
  then defined from the configuration, not from the action: the induced
  tensor \(g_{\alpha\beta}=\eta_{IJ}\partial_\alpha x^I\partial_\beta x^J\)
  and the operator tensor
  \(K^{\mu\nu}=\theta^{\alpha\mu}g_{\alpha\beta}\theta^{\beta\nu}\), which
  is the kinetic tensor of a fluctuation \([\hat X^I,\cdot\,]\) in the
  Poisson limit. This definition adds no fundamental metric: the form
  \(\eta_{IJ}\) contracts matrix indices only, and its Lorentzian
  signature is retained as Assumption~\ref{ass:lorentzian}. The index
  \(I\) of this definition is not the internal index of \(\Phi^I{}_A\)
  in Presentation~B, and the \(D-4\) transverse coordinates are not
  covered by Assumption~\ref{ass:locked-block}. By
  Remark~\ref{rem:ch3-moyal-check} and Appendix~\ref{app:status}, the
  inverse of \(K\) is in general not proportional to \(g\); neither
  \(g\) nor \(K^{-1}\) is asserted here to be the emergent metric of
  Equation~\eqref{eq:g-from-e} or the metric of
  Assumption~\ref{ass:emergent-op}.
\end{definition}
```

**File 2: `chapters/appH-microscopic-proofs.tex`.** Insert after the 008 paragraph, immediately before `\section{Problem G: HBEV}`. Anchor (occurs once, verified): "Problem~F, and Problems~A, B, C and~D, remain open." followed by a blank line and `\section{Problem G: HBEV}`. Nothing replaced. Labels verified once: `def:matrix-coords-ext` (new, from File 1), `ass:locked-block`, `ass:emergent-op`, `ass:lorentzian`, `rem:ch3-moyal-check`, `eq:Geff-structure`. Citation keys: `Steinacker2023` (exists), `KumarSteinacker2023` and `Steinacker2026` (new; BibTeX below).

```latex
\paragraph{More than four matrix coordinates in the Poisson limit: what the transverse coordinates supply (conditional; not closure).}
Keep Definition~\ref{def:matrix-coords-ext}, the Poisson limit, a four-dimensional symplectic leaf, a real Lorentzian induced tensor \(g\), \(\omega=\theta^{-1}\), \(K=\theta^{T}g\,\theta\) and \(G=K^{-1}=\omega g^{-1}\omega^{T}\). Put \(M=g^{-1}\omega\), which is \(g\)-antisymmetric, so that \(G=-gM^{2}\) and \(\det M=\operatorname{Pf}(\omega)^{2}/\det g\).

\emph{Operator metric versus induced metric.} A relation \(G=c\,g\) would give \(M^{2}=-c\) with \(c>0\) by signature. A real \(M\) with \(M^{2}=-c\) has eigenvalues \(\pm i\sqrt c\) in conjugate pairs, so \(\det M=c^{2}>0\), whereas \(\det M<0\) for Lorentzian \(g\). Hence for every \(D\ge4\) and every real Lorentzian \(g\), \(G\) is not proportional to \(g\) pointwise; the transverse coordinates do not remove the obstruction of Remark~\ref{rem:ch3-moyal-check} for this relation. The statement uses that the symplectic leaf has dimension four; for a Euclidean or \((2,2)\) tensor \(g\) an orthogonal complex structure gives \(G\propto g\).

\emph{Linear response.} In a chart with constant \(\theta\), let \(\delta x^{I}=A^{I}e^{ip\cdot y}\), \(A=\xi^{\mu}\partial_\mu x+\phi_i n^{i}\) with \(n^{i}\) a normal frame and \(\mathrm{II}^{i}_{\mu\nu}=n^{i}\cdot\partial_\mu\partial_\nu x\). To first order \(\delta g=p\circ(g\xi)-2\phi_i\mathrm{II}^{i}\) with \(a\circ b=ab^{T}+ba^{T}\), and \(\delta G=-G\,\theta^{T}\delta g\,\theta\,G\); the Hamiltonian choice \(\xi=\theta^{T}p\) gives a linearised diffeomorphism of \(G\). About a flat brane the transverse amplitudes do not enter at first order, and the rank of the linearised Einstein operator of \(G\) on the image is three for every \(D\) tested (\(4\le D\le11\)), against six conserved sources \(p^{\mu}T_{\mu\nu}=0\). About a background with generic \(\mathrm{II}^{i}\) the rank is \(\min(6,D-1)\) in exact-rational samples for \(4\le D\le11\), also when \(K^{\mu\nu}\mathrm{II}^{i}_{\mu\nu}=0\); all six sources are then reachable from \(D=7\). The analysis freezes \(g\), \(\theta\) and \(\mathrm{II}\) at a point and does not impose the Gauss--Codazzi relations. Counting the density scalar as well, the number \(D-1\) of gauge-invariant functions must be at least \(7\), that is \(D\ge8\); this is a necessary count. No field equation of Einstein type for \(G\) is derived.

\emph{Content.} The \(D-4\) transverse coordinates are additional infrared fields unless they are gapped; they are not covered by Assumption~\ref{ass:locked-block}, and if they are gapped and decouple the flat-brane statement above applies. Under the hypotheses of the \(N_{\mathrm{tot}}\) bookkeeping of the Poisson-limit paragraph above and on its constant background, each transverse component has the operator \(\mathcal O_s\), so \(N_{\mathrm{tot}}=(D-4)+N_{\mathrm{other}}+2\), and \(N_{\mathrm{tot}}=D-2\) for the bosonic matrix sector alone; this ignores the coupling through \(\mathrm{II}\), fermions and mixing. One-loop IKKT calculations on branes with fuzzy extra dimensions report an induced Einstein--Hilbert term with the Newton constant set by the extra-dimension scale~\cite{Steinacker2023}, and modified Einstein equations with extra tensors~\cite{KumarSteinacker2023,Steinacker2026}; their quantum spaces have a higher-dimensional leaf, which is the hypothesis relaxed relative to the first statement above. We have not checked these results against the present operators.

This is a statement for \(D\) matrix coordinates, the Poisson limit, a four-dimensional symplectic leaf, a constant \(\eta_{IJ}\), locally frozen background data and generic \(p\). It does not identify \(G\) or \(g\) with the emergent metric of Chapter~\ref{ch:vierbein-emergence}, does not identify \(\Phi^{I}{}_{A}\) with a tangent-plane frame, does not derive a local Lorentz symmetry, a signature or an extra conserved stress, and gives no value or sign of \(G_{\mathrm{eff}}\) in Equation~\eqref{eq:Geff-structure}. Problem~F, and Problems~A, B, C, D and~E, remain open.
```

**File 3: `bib/namcg.bib` (integrator, after `ACCEPT`).** Records fetched and checked as arXiv abstract pages; journal data not claimed.

```bibtex
@misc{KumarSteinacker2023,
  author  = {Kumar, Kaushlendra and Steinacker, Harold C.},
  title   = {Modified Einstein Equations from the 1-loop Effective Action
             of the {IKKT} Model},
  year    = {2023},
  eprint  = {2312.01317},
  archivePrefix = {arXiv}
}

@misc{Steinacker2026,
  author  = {Steinacker, Harold C.},
  title   = {Modified Gravity at Large Scales on Quantum Spacetime
             in the {IKKT} Model},
  year    = {2026},
  eprint  = {2601.08031},
  archivePrefix = {arXiv}
}
```

**Stale passages elsewhere.** (i) appH 008 paragraph, sentence "Suppose, as an assumed dictionary not contained in the four-matrix class, that there are \(D\ge4\) coordinate matrices \(X^I\) ..." remains true as written; it is now realised by the extended definition but not in need of an edit. (ii) The 008 final sentence "to the embedding statement above beyond four coordinates" is addressed, not contradicted, by the new paragraph. (iii) ch03 lines about `N>4` (L224-227) and ch05 exercise 7 concern the internal index of `Phi` and are unchanged. (iv) Chapter 17 and the ch16 inventory: unchanged (no assumption added or removed). The 008 *proposal* "Decisions Taken" sentence that N >= 8 "removes both obstructions" is superseded by item 1 above; it is not manuscript text.

## Verification scripts

In `proposals/009-matrix-coords-N8/`:
- `check_conformal_nogo.py` / `.out.txt`: exact rational identities (`det omega = Pf^2`, `det M = Pf^2/det g`, `G = -g M^2`); random Lorentzian embeddings D = 4..11, optimal-c residuals; Euclidean and (2,2) contrasts.
- `check_brane_rank.py` / `.out.txt`: exact rational linear-response and Einstein-rank table (flat / generic II / K-traceless II, D = 4..11), Hamiltonian-gauge direction equals G-diffeo.
- `verify_anchors_labels.py` / `.out.txt`: anchors (ch03 count 1, appH count 1), labels (each existing label count 1, `def:matrix-coords-ext` 0), bib keys (`KumarSteinacker2023`, `Steinacker2026` absent, others present).
Rank samples are checks, not proofs; the sympy runs of `check_brane_rank.py` use one random draw per entry.

## Decisions Taken

- The structural change (definition extension) is pre-approved (emergent, positive for the derivation, no label change). I implemented it as an *additional* labelled definition rather than rewriting `def:matrix-coords`, so that D = 4 results (005, 008) and all references stay valid. Rejected: editing `def:matrix-coords` and `eq:Smatrix` in place (invalidates the 005/008 hypotheses and many cross-references with no gain).
- Which metric is the operative one: the operator metric `G` (the metric seen by commutator operators and used in 005), not the induced `g`. Reason: item 1 shows they cannot be conformal for a 4D leaf, and `ass:emergent-op` is about the operators. Rejected: declaring `g` emergent (the fluctuation operators do not see it).
- Not claimed: N >= 8 as a threshold. The rank computation gives D = 7 (tensor sources) and the density-scalar count gives D = 8; both are necessary-only. Recorded as such.
- Fuzzy-K / leaf dimension > 4: not pursued in this package (the covariance mechanism would need the full covariant-quantum-space machinery and a separate derivation); recorded as the specific hypothesis to relax next.
- Bound the claim about 008: 008's integrated manuscript text is correct (it says the embedding reading is not discharged); only its proposal-level ranking sentence was too optimistic.

## Milestone assessment

Candidate M2 (bounded no-go): D-independent non-proportionality of `G` and `g` for a 4D leaf, and D-independence of the flat-brane rank. Candidate M5 (structural extension of `def:matrix-coords`, pre-approved under the author's 2026-10-14 authorization, emergence preserved, no label change). Not M1, not M3 (no merged claim is wrong), not a breakthrough. The gatekeeper decides.

## Status-label recommendation

None. A, B, C, D1, E, F, G-derived and N remain OPEN / CRITICAL PATH (A, E, N "for the matrix-derived label") / PROGRAMME-CONDITIONAL.

## Author decision needed

None.

## Remaining open step

To discharge `ass:emergent-op` and advance D1/E/F: (a) a derived field equation for `G` from the matrix action in the extended setting (tree-level equation of motion `Delta_G x^I = 0` and the one-loop terms), including whether the one-loop extra tensors of the IKKT literature supply the codimension; (b) a mechanism gapping or constraining the `D-4` transverse scalars; (c) relaxing the 4D-leaf hypothesis (fuzzy extra dimensions) to remove the `G`-versus-`g` no-go and to obtain a matrix-derived Newton constant; (d) the identification of `Phi` with a tangent-plane or `G`-coframe and its vacuum manifold; (e) Moyal corrections and non-constant backgrounds; (f) a derived signature (E) and local Lorentz dynamics (D1).

## Special instructions for the gatekeeper

- Verify the determinant argument independently; check that the no-go is scoped to a 4D real symplectic leaf and a real Lorentzian `g`.
- Re-run `check_brane_rank.py` (about 100 s); check the claim `rank = min(6, D-1)` is described as a sampled generic rank, and the WKB/frozen-background caveat is preserved. In particular check the definition of the image in the chart with constant `theta` and the correctness of the Hamiltonian gauge direction.
- The `N_tot = D-2` sentence depends on 005's formula and on the 005 constant background; check that it is not read as a derived induced-EH sign. Decide whether it should be dropped.
- Citations: only abstract pages were read; the text must not attribute results beyond "reported". `Steinacker2023` is an existing bib key whose journal data were not independently verified.
- Must not be asserted: that the extension solves F, A, D1 or E; that `G = c g` is attainable; that the transverse scalars are gapped; that the one-loop literature supplies the 008 extra stress; any label change.
