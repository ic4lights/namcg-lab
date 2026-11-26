# Proposal 018-induced-coefficient-cp12, round 2

## Changelog against r1
Review r1: ACCEPT WITH REQUIRED REVISIONS, M2 (narrow), all findings wording. No calculation changed; the r1 scripts and outputs remain valid.
- R1: first sentence of "Hypoelliptic structure" now states the sub-Laplacian / step-2 / Q = 8 claim for the Euclidean contraction Box_E = sum_a (D^a)^2, not the Casimir difference; ranks, step and Q = 8 depend only on D^a, J^{ab}; ghost and vector operators are then built from Box_E.
- R2: "no sign-definite heat trace" replaced by "e^{-sH_V} is unbounded for every s>0 at the leading symbol, so the proper-time trace of this sector diverges".
- R3: fibre-constant density marked "a formal evaluation for eta = diag(-1,1,1,1); no Euclidean heat-kernel statement is made for this sector".
- R4: closing scope list now contains "the proper-time cutoff of Box_X as the regulator, one loop,".
- R5: sampling stated (12 sampled points, 9 directions of zeta each; no claim over the whole leaf); "no heat kernel exists" replaced by "the Euclidean heat-kernel construction does not apply".
- R6: w and varrho pointed to "the induced and tree-level coefficients of the preceding paragraph" (the 016 crossover paragraph).
- Optional: O(s^(1/2)) -> O(s). "Scheme-dependent" is not in the block and is removed from the proposal text.
- Proposal text: Result items 2, 3 aligned with R1, R2, R3, R5; "Remaining open step" replaced by the review's ranked avenues; compile check re-run on block-r2.tex.
- block-r2.tex is identical to the LaTeX block below.

## Result
The induced Einstein-Hilbert coefficient w, and hence the sign and size of varrho = Lambda/w, is **not determined** in this package. What is established is a bounded no-go together with exact structure that fixes where the missing computation sits.

1. (Established, exact algebra.) The Theta-built regulator in the CP^{1,2} class is the proper-time cutoff of Box_X = eta_ab {X^a,{X^b,.}}. At the background, Box = C_{so(4,1)} - C_{so(3,1)}, [Box,J^{ab}] = 0, the ghost operator is -Box, and the gauge-fixed vector operator is H_V = -Box - 2s J_ab Sigma^{ab} + mu^2. Fibre-constant functions are an invariant subspace and equal functions on the hyperboloid y.y = -ell^2 with D^a = s(y^4 d^a - y^a d_4). On it Box is the 4D operator with K = m^2 eta, rho = 1/m, whose Seeley-DeWitt density is (5m^2 - 3 ell^2)/(4 m^6), not sign-definite (formal evaluation for eta = diag(-1,1,1,1)).
2. (Established numerically at sampled points; theory cited.) The horizontal fields D^a have rank 4 and, with J^{ab}, rank 6 (rank drop only on y^4 = 0). The Euclidean contraction Box_E = sum_a (D^a)^2 (not the Casimir difference; the ranks, step and Q = 8 depend only on the D^a, J^{ab}) is therefore a step-two sub-Laplacian of homogeneous dimension 8. Its heat-kernel diagonal is c_0 s^{-4}, not the s^{-3} of a 4D operator times a fibre mode count. The leading symbol is a 4D Landau problem in a self-dual-or-not field F(zeta) with an exactly known diagonal.
3. (Bounded no-go.) The 011 statement "1/G_eff ~ Lambda^2 x weighted mode count" is the limit s f_j << 1 of the Landau diagonal. It does not hold in the Poisson limit, where the fibre momentum |zeta| is unbounded. In the Euclidean continuation eta -> delta the vector operator has lowest eigenvalue -|f1 - f2| at fixed zeta. At the 12 sampled points x 9 zeta-directions f1/f2 lies in [0.006, 0.84] (no claim over the whole leaf); e^{-sH_V} is unbounded for every s>0 at the leading symbol and the proper-time trace of the sector diverges. For f1 = f2 there would be an unbounded family of zero modes. For the Lorentzian contraction (electric-type) the Euclidean heat-kernel construction does not apply. The sign of w therefore cannot be read from a Euclidean heat kernel in this class without a change of content or of regulator (see Remaining open step).
4. (Established, conditional on sf << 1.) The F^2-structure of the bosonic loop is (22 - n_ex)/6 times (f1^2 + f2^2) s^2. This renormalises the coefficient of the quartic term logarithmically. It is not the EH coefficient.

Hypotheses of the no-go (fork analysis): see "Research and reasoning", section F.

## Target and status
Problem F (coefficients A, B, C; induced G_eff). Appendix H sec:status-F: Status OPEN, Priority CRITICAL PATH, Completion PROGRAMME-CONDITIONAL; reduced-scope result "treating G_eff as an input leaves F OPEN". Original target: the matrix-derived G_eff (sign and size) in a class where the 008/009/011 obstructions are absent. Dependencies: A, B, C, D1, E, N through G_eff. This package is PROGRAMME-CONDITIONAL (Poisson limit, leading symbol, Euclidean continuation, bosonic content). No discrepancy found between Ch. 17 and Appendix H labels. The 016 paragraphs are now integrated immediately before `\section{Problem G: HBEV}`.

## Source reading
Digest + targeted reads (digest current). Read in full: appH Problem F ledger and the Presentation-A, fuzzy-leaf, conjugate-coordinate, level-one, Noether and crossover paragraphs (lines 1143-1960); ledger entries 003-016; SME scout (R9, R15, R17) and 016 review r2. Literature: arXiv:2411.02598 (Manta-Steinacker-Tran) HTML Sec. 3 as extracted by the fetch tool (first 100k characters only; eq. 3.4 character formula, 3.33 for 1/G_N). I imported no result from it. arXiv:2609.08955 eq. 92: not read, only the SME extraction (1/G_N = (1/4 pi rho^2) Tr_K(dF dF/Box_6)); not used. Steinacker2023: not re-read. Ben Arous, Ann. Inst. Fourier 39 (1989) 73-99, DOI 10.5802/aif.1158: bibliographic record and abstract-level content confirmed by search (Numdam); the theorem's exact hypotheses not read, so the equiregularity requirement is stated as an assumption.

## Research and reasoning
A. Operator content (sector table). Matrix fluctuations: A^a (4 components, operator H_V), ghosts (-Box, weight -2), n_ex extra matrices (-Box + mu_i^2; mu_i^2 an extra input since mu^2 = -3 was fixed only for X^a). Fibre harmonics are not separate fields: they are the spectrum of Box on L^2 of the 6D leaf. Gauge: background Feynman, D_a A^a. Check: delta(D.A) = -Box Lambda for A = {Lambda,T}. (Script 1.) No fermions.

B. Exact structure (Script 1, sympy, both s): Box = C_41 - C_31; [Box,J^{ab}] = 0 (so the MST-type condition [Box,F] = 0 holds exactly for J^{ab} at the background); on functions of y^A, D^a = s(y^4 d^a - y^a d_4). Script 2 verifies the 4D reduction of the l = 0 sector and computes its a_1 density in the Lorentzian formula. The Euclidean line of that script uses an ad hoc continuation of m and is not used.

C. Hypoellipticity (Script 3). Floats at random orbit points of the explicit realisation (013): rank 4 and 6. The nilpotent approximation has four horizontal generators with [D^a,D^b] = s S^{ab}_k Z_k, a 2D centre. After Fourier transform in the centre: constant field F_ab(zeta), Landau levels f1(2n1+1) + f2(2n2+1), diagonal prod f_j/(4 pi sinh s f_j) per d^2 zeta/(2 pi)^2. Liouville normalisation nu from the Pfaffian of omega on (D^0..D^3,Z1,Z2). Self-dual check: numerical integral equals 3 zeta(3)/(64 pi^3) to 16 digits. Verification that the leading coefficient is c_0 s^{-4} rests on the cited nilpotent-approximation theorem (not re-proved).

D. Landau spectra (Script 4). Truncated Fock space: scalar lowest f1 + f2; vector lowest -|f1 - f2| (cases (1,1): 0 doubly; (1,3): -2; (0.3,2): -1.7). Series of the bosonic weight: 2 + n + (22 - n)/6 (f1^2 + f2^2) s^2 (sympy).

E. Regime of the 011 formula. Since prod s f_j/sinh s f_j = 1 - s^2(f1^2 + f2^2)/6 + ..., the product replication is the regime where Lambda_UV^2 exceeds the largest populated f_j (finite fuzzy fibre with l <= n). The NC scale of a quantum space is of the order of that largest f_j, so a Poisson-limit cutoff below it is in the Landau regime. This is an order-of-magnitude statement and is labelled conjecture.

F. No-go as a fork. Hypotheses: (H1) Poisson limit and leading (nilpotent) symbol; (H2) Euclidean contraction eta -> delta with the Lie-Poisson algebra kept; (H3) equiregular points; (H4) bosonic content, background gauge; (H5) proper-time cutoff of Box_X. Avenues and outcomes:
 - Finite fuzzy fibre (cutoff on l): removes the unbounded |zeta| and restores the product regime; then the 011/005 machinery applies to sectors, but the connection-sector torsion term of the CP class (analogue of X in 005) is not derived. Open.
 - Fermionic partners (SUSY-type): Zeeman terms cancel the instability by construction; this is what cancels alpha^0 and alpha^2 in MST; content change, not within the bosonic sector.
 - Another Euclidean section (compact twistor-type model CP^3 -> S^4, where the horizontal curvature is self-dual): the unbounded zero-mode family for f1 = f2 replaces the instability. Not computed.
 - Exact so(4,2) harmonic analysis / character technique (as in MST) at the quantum-space level, with the Moyal terms included: the only route that treats Lambda_UV ~ Lambda_NC.
 - Second-order sub-Riemannian symbol calculus (weight-two term s^{-3} and its A-variation): the direct computation of w. Not done.
 - Different gauge: cannot remove the Nielsen-Olesen-type negative modes of the nilpotent operator (physical, not gauge).
Ranking of avenues: see Remaining open step (the gatekeeper's ranking replaces the r1 ranking).

## Claim classification
- Casimir forms, ghost operator, l = 0 invariance and 4D reduction: established (exact in the polynomial Poisson algebra / sympy).
- l = 0 density (5m^2 - 3 ell^2)/(4 m^6): established as a formula; its relevance to w: not claimed.
- Rank 4 / 6: numerical at sampled points (floats), generic.
- s^{-4} diagonal and Landau form: conditional (cited theorem, equiregularity, nilpotent approximation); c_0 numerics and the 3 zeta(3) check: established as computation.
- Euclidean-continuation instability: established within H1-H5 (numerically at sampled points; the formula -|f1 - f2| is standard Landau + Zeeman).
- (22 - n_ex)/6 coefficient: established (conditional on sf << 1).
- Regime-of-validity statement about the NC scale: conjecture.
- w sign and size, varrho: unresolved.

## Proposed changes
File `chapters/appH-microscopic-proofs.tex`. Anchor: the line `\section{Problem G: HBEV}` (occurs exactly once; re-verified in r2, asserted in compile_check_r2.py). Insert immediately before it, after the 016 paragraphs, the block below (identical to `block-r2.tex`). Nothing existing is replaced. Labels used: `thm:Geff`, `ch:vierbein-emergence`, `ass:EE`, each defined once (re-verified). The integrator adds the entry below to `bib/namcg.bib` (unchanged from r1, verified by the gatekeeper against Crossref; the existing bib file has no accented names, so the `{\'e}` form is retained and the integrator should confirm it).

```bibtex
@article{BenArous1989,
  author  = {Ben Arous, G{\'e}rard},
  title   = {D{\'e}veloppement asymptotique du noyau de la chaleur hypoelliptique sur la diagonale},
  journal = {Annales de l'Institut Fourier},
  volume  = {39},
  number  = {1},
  pages   = {73--99},
  year    = {1989},
  doi     = {10.5802/aif.1158}
}
```

```latex
\paragraph{Conjugate-coordinate class: the \(\Theta\)-built heat kernel and the induced coefficient (conditional; bounded no-go).}
Keep the Poisson limit, the leaf \(\mathbb{CP}^{1,2}\), \(X^a=T^a+A^a\), the bilinear term with \(\mu^2=-3\) and the notation of the preceding paragraphs; \(D^a=\{T^a,\cdot\}\), \(J^{AB}=\{M^{AB},\cdot\}\), \(\Box=\eta_{ab}D^aD^b\). The regulator is the proper-time cutoff \(s\ge\LUV^{-2}\) of the operator \(\Box_X\) itself, applied to every sector; it is built from Poisson brackets and the matrix contraction only. Background gauge fixing \(D_aA^a\) gives the ghost operator \(-\Box\) (weight \(-2\)), the vector operator \(H_V=-\Box-2sJ_{ab}\Sigma^{ab}\) (the same \(J_{ab}A^b\) as in the quadratic form above, with \(\mu^2\) added), and, for \(n_{\mathrm{ex}}\) further matrices with trivial background, \(-\Box+\mu_i^2\) with \(\mu_i^2\) an additional input. Fermions are absent. In exact arithmetic in the polynomial Poisson algebra, for both signs \(s\): \(\Box=C_{\mathfrak{so}(4,1)}-C_{\mathfrak{so}(3,1)}\) with the generators \(J^{AB}\), \(A,B\le4\), and \(J^{ab}\), \(a,b\le3\); \([\Box,J^{ab}]=0\) while \([\Box,D^a]\ne0\); and on functions of \(y^A=M^{A5}\), \(A\le4\), one has \(D^a=s\,(y^4\partial^a-y^a\partial_4)\), a rotation field of the hyperboloid \(y\cdot y=-\ell^2\). Fibre-constant functions therefore form an invariant subspace of \(\Box\), on which \(\Box=\rho^{-1}\partial_\mu(\rho\,m^2\eta^{\mu\nu}\partial_\nu\,\cdot)\) with \(m=y^4\), \(\rho=1/m\); for \(G^{\mu\nu}=m^2\eta^{\mu\nu}\) the Seeley--DeWitt density of this sector is \(\sqrt{|G|}\,(R_G/6-E)=(5m^2-3\ell^2)/(4m^6)\), which is not of definite sign (a formal evaluation for \(\eta=\mathrm{diag}(-1,1,1,1)\); no Euclidean heat-kernel statement is made for this sector). Fibre harmonics of order \(\ge1\) are not an invariant subspace of the perturbed operators, so this sector does not by itself give the response to the level-one amplitudes.

\emph{Hypoelliptic structure.} At every sampled point of the orbit (random points, and the sequence \(y^4\to0\)) the fields \(D^a\) have rank four and \(D^a\), \(J^{ab}\) together span the six-dimensional tangent space; the horizontal rank drops on \(y^4=0\) (one singular value proportional to \(y^4\)), which is excluded. Hence, for the Euclidean contraction \(\eta\to\delta\) (the operator \(\Box_E=\sum_a(D^a)^2\), which is not the Casimir difference above), the operator is a sub-Laplacian of step two with homogeneous dimension \(4+2\cdot2=8\), not an elliptic operator on a product; the ranks, the step and the dimension \(8\) depend only on the fields \(D^a\), \(J^{ab}\). The ghost and vector operators below are then built from \(\Box_E\). Under equiregularity the diagonal of its heat kernel is \(K(s)=c_0s^{-4}(1+O(s))\) with \(c_0\) given by the nilpotent approximation~\cite{BenArous1989}, here a group with four horizontal generators and a two-dimensional centre. After Fourier transform along the centre (variable \(\zeta\in\mathbb R^2\)) the nilpotent operator is a four-dimensional charged Laplacian in a constant field \(F_{ab}(\zeta)=\zeta_kS^{ab}{}_k\) of the two-plane strengths \(f_1,f_2\propto|\zeta|\), with Landau levels \(f_1(2n_1+1)+f_2(2n_2+1)\) and the diagonal \(\prod_j f_j/(4\pi\sinh sf_j)\) per unit horizontal volume and per \(\mathrm d^2\zeta/(2\pi)^2\). With \(\nu\) the Liouville volume of the frame \((D^0,\dots,D^3,Z_1,Z_2)\) of the nilpotent algebra, \(c_0=\nu^{-1}(64\pi^4)^{-1}\!\int_0^{2\pi}\!\mathrm d\varphi\,\phi_1\phi_2\!\int_0^\infty\!\mathrm du\,u^3/(\sinh u\phi_1\sinh u\phi_2)\), \(f_j=|\zeta|\phi_j\); for \(f_1=f_2\) this is \(3\zeta(3)/(64\pi^3\nu)\). With the Euclidean contraction \(\eta\to\delta\) of the four matrix indices (the Poisson algebra kept) the ratio \(f_1/f_2\) at \(12\) sampled points and \(9\) directions of \(\zeta\) each lies between \(0.006\) and \(0.84\), never at \(1\); no claim is made over the whole leaf. For the Lorentzian contraction \(F\eta\) has one real and one imaginary eigenvalue pair, the electric-type case, to which the Euclidean heat-kernel construction does not apply.

\emph{Consequences.} (i) The statement that a fuzzy factor replicates the four-dimensional coefficient of Theorem~\ref{thm:Geff} over its modes, with threshold weights, is the limit \(sf_j\ll1\) of the diagonal above, \(\prod_j sf_j/\sinh sf_j=1-s^2(f_1^2+f_2^2)/6+\dots\), valid when \(\LUV^2\) exceeds the largest populated \(f_j\). In the Poisson limit \(|\zeta|\) is unbounded and the regime is the hypoelliptic one; the replication formula does not apply there, and the weighted mode count is replaced by \(\nu^{-1}\int\mathrm d^2\zeta\,(2\pi)^{-2}\prod_j sf_j/\sinh sf_j\). (ii) In the same nilpotent limit \(H_V\) acquires the Zeeman term \(\pm2f_1,\pm2f_2\), so its lowest eigenvalue at fixed \(\zeta\) is \(-|f_1-f_2|\) (checked by diagonalisation in a truncated Fock space): zero modes of unbounded number for \(f_1=f_2\), and eigenvalues unbounded below for \(f_1\ne f_2\), neither regulated by the proper-time cutoff. The vector sector therefore needs a fibre truncation (a finite fuzzy fibre) or fermionic partners, and in the Euclidean continuation used here \(e^{-sH_V}\) is unbounded for every \(s>0\) at the leading symbol, so the proper-time trace of this sector diverges. (iii) For \(sf_j\ll1\), the vector, ghost and \(n_{\mathrm{ex}}\) scalar sectors together give \(2+n_{\mathrm{ex}}+\tfrac{22-n_{\mathrm{ex}}}{6}s^2(f_1^2+f_2^2)\); the \(s^2\) term has the structure of the quartic term \(\{X^a,X^b\}^2\) and renormalises its coefficient logarithmically, not the Einstein--Hilbert coefficient. (iv) An Einstein--Hilbert coefficient would be the weight-two term \(\propto s^{-3}\) of the diagonal and its second variation under \(A\); no such computation is made here, and neither the sign nor the size of \(w\), hence of \(\varrho=\Lambda/w\), follows, with \(w\) and \(\varrho\) the induced and tree-level coefficients of the preceding paragraph.

This is a statement for the Poisson limit, the proper-time cutoff of \(\Box_X\) as the regulator, one loop, the leading (nilpotent) symbol, equiregular points, the Euclidean contraction \(\eta\to\delta\) with the Lie--Poisson algebra kept, background gauge and the bosonic content listed. It does not treat Moyal terms, fermions, the subleading symbol, the dependence on \(A\), or the identification of \(G\) with the emergent metric of Chapter~\ref{ch:vierbein-emergence}, and it does not bear on Assumption~\ref{ass:EE}. This changes no ledger label; Problem~F remains open.
```

No stale passages elsewhere need changing; the 011 sentence on the heat kernel over a fuzzy factor remains correct as stated for a product leaf with a finite fuzzy factor.

## Verification scripts
- `check_casimir_forms.py` / `.out.txt`: items B and A (exact, both s).
- `check_l0_reduction.py` / `.out.txt`: 4D reduction of the fibre-constant sector and the a_1 density.
- `check_hormander_weyl.py` / `.out.txt`: ranks, nilpotent data, Landau f1/f2, eta-contraction eigenvalues, nu, c_0, 3 zeta(3) check, y^4 -> 0 sequence. Uses `cp12_realisation.py` (copy of the 013 realisation).
- `check_landau_vector.py` / `.out.txt`: Fock-space spectra and the s^2 coefficient (22 - n)/6.
- `compile_check_r1.py` / `.out.txt` (superseded) and `compile_check_r2.py` / `compile_check_r2.out.txt`: scratch-copy build of block-r2.tex outside the repository: 264 pages, 0 errors, 0 undefined, 0 multiply defined, 0 double-subscript.
- `verify_anchors_labels.out.txt`, `verify_anchors_labels_r2.out.txt` (thm:Geff, ch:vierbein-emergence, ass:EE: one definition each; the anchor occurs exactly once, asserted in compile_check_r2.py).
The exploratory files `explore1.py`-`explore3.py` in the folder are superseded by the scripts above.

## Decisions Taken
- r2: applied R1-R6 and the optional O(s) replacement with the review's wording; kept 'scheme-dependent' out of the manuscript text and removed it from the proposal text. The bib entry is unchanged; the bib file contains no accented entries, so the `{\'e}` form is retained and the integrator should confirm it.
- r2: the r1 ranking in section F is replaced by the gatekeeper's ranking in Remaining open step, adopted unchanged; none of the avenues is explored here.
- Chose the Poisson-limit hypoelliptic reading of the Theta-built regulator over the 011 product reading, because the CP leaf has rank-4 horizontal fields on a 6D leaf (not a product).
- Did not present a "reduced-model" value of w from the fibre-averaged 4D operator: its premise is shown to fail in the Poisson limit, and a number from it would be misleading.
- Stopped at this package because w needs a second-order symbol calculus with the A-variation (next package); no label or scope change.

## Milestone assessment
M2 narrow (bounded no-go: product/replication reading of the induced coefficient excluded in the Poisson-limit CP class, with the instability of the Euclidean vector sector). No breakthrough.

## Status-label recommendation
None. F, A, B, C, D1, E, G-derived, N remain OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## Author decision needed
None.

## Remaining open step
The sign and size of w (hence of varrho = Lambda/w) are not determined. Each avenue below relaxes one hypothesis of the no-go (H1 Poisson limit and leading nilpotent symbol; H2 Euclidean contraction eta -> delta with the Lie-Poisson algebra kept; H3 equiregular points; H4 bosonic content, background gauge, one loop; H5 regulator = proper-time cutoff of Box_X). Ranked by the gatekeeper's judgement of how much each favours the infrared or full-GR derivation; none is explored in this package:
1. Relax H4, bosonic content: fermionic or supersymmetric partners, or a fibre truncation. The Zeeman instability is the obstruction to a definite sign of w in the bosonic class, and a fermionic content change is how the published IKKT one-loop mechanism avoids it. Such a content change would need the usual structural review.
2. Relax H1, Poisson limit and leading symbol together: exact so(4,2) harmonic analysis and character technique at the quantum-space level, Moyal terms included. This treats Lambda_UV ~ Lambda_NC directly and is the only route that does not presuppose the sf << 1 or Landau regime.
3. Relax H1, leading symbol: the second-order sub-Riemannian symbol, i.e. the weight-two s^-3 term of the diagonal and its A-variation in the nilpotent model. This is the direct computation of w, meaningful once avenue 1 or 4 fixes the vector-sector problem; the cited expansion has integer powers, so the weight-two coefficient is a well-defined target.
4. Relax H5 and H3: a different regulator, for example a cutoff on fibre harmonic number l, which restores the product regime. The connection-sector torsion term X for the CP class is still not derived.
5. Relax H2: a compact Euclidean section (twistor CP^3 -> S^4), where self-dual horizontal curvature replaces the instability by a zero-mode family. A consistency check only, since signature remains Problem E.

## Special instructions for the gatekeeper
Unchanged from r1: the paragraph is a no-go on a reading plus structure, not a derivation of w or varrho. Re-check only the R1-R6 wording against the review's corrected snippets (diff block-r1.tex block-r2.tex), the compile record, and the single occurrence of the anchor.
