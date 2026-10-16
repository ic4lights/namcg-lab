# Proposal 018-induced-coefficient-cp12, round 1

## Result
The induced Einstein-Hilbert coefficient w, and hence the sign and size of varrho = Lambda/w, is **not determined** in this package. What is established is a bounded no-go together with exact structure that fixes where the missing computation sits.

1. (Established, exact algebra.) The Theta-built regulator in the CP^{1,2} class is the proper-time cutoff of Box_X = eta_ab {X^a,{X^b,.}}. At the background, Box = C_{so(4,1)} - C_{so(3,1)}, [Box,J^{ab}] = 0, the ghost operator is -Box, and the gauge-fixed vector operator is H_V = -Box - 2s J_ab Sigma^{ab} + mu^2. Fibre-constant functions are an invariant subspace and equal functions on the hyperboloid y.y = -ell^2 with D^a = s(y^4 d^a - y^a d_4). On it Box is the 4D operator with K = m^2 eta, rho = 1/m, whose Seeley-DeWitt density is (5m^2 - 3 ell^2)/(4 m^6), not sign-definite.
2. (Established numerically at sampled points; theory cited.) The horizontal fields D^a have rank 4 and, with J^{ab}, rank 6 (rank drop only on y^4 = 0). Box is therefore a step-two sub-Laplacian of homogeneous dimension 8. Its heat-kernel diagonal is c_0 s^{-4}, not the s^{-3} of a 4D operator times a fibre mode count. The leading symbol is a 4D Landau problem in a self-dual-or-not field F(zeta) with an exactly known diagonal.
3. (Bounded no-go.) The 011 statement "1/G_eff ~ Lambda^2 x weighted mode count" is the limit s f_j << 1 of the Landau diagonal. It does not hold in the Poisson limit, where the fibre momentum |zeta| is unbounded. In the Euclidean continuation eta -> delta the vector operator has lowest eigenvalue -|f1 - f2| at fixed zeta. At all sampled points f1/f2 lies in [0.006, 0.84], so it is unbounded below and not regulated by the cutoff. For f1 = f2 there would be an unbounded family of zero modes. For the Lorentzian contraction there is no heat kernel (electric-type). The sign of w therefore cannot be read from a Euclidean heat kernel in this class without a fibre truncation or fermionic partners.
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
Ranking: (1) weight-two coefficient with A-variation in the nilpotent model (a bounded next package); (2) finite-fibre product regime with derived connection-sector term; (3) character/harmonic-analysis computation; (4) compact Euclidean model as a consistency check; (5) fermions.

G. varrho. varrho = Lambda/w has the sign of Lambda w. If the Euclidean induced TT-channel form is positive like the tree term, varrho > 0 (the crossover branch without a sign flip); a negative net induced form gives varrho < 0. Neither is derived. The sign of w is scheme-dependent in this class for the reasons in item 3.

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
File `chapters/appH-microscopic-proofs.tex`. Anchor: the line `\section{Problem G: HBEV}` (occurs once; verified, line 1961). Insert immediately before it, after the 016 paragraphs, the contents of `block-r1.tex` (one paragraph, closing with the status sentence). Nothing existing is replaced. The labels used are `thm:Geff`, `ch:vierbein-emergence`, `ass:EE`, each defined once (verified). A new bibliography entry is needed (the integrator adds it to `bib/namcg.bib`):

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

The LaTeX block is in `proposals/018-induced-coefficient-cp12/block-r1.tex` (full text; to be inserted verbatim, CRLF normalised by the integrator). No stale passages elsewhere need changing; the sentence in the fuzzy-leaf paragraph on the heat kernel over a fuzzy factor remains correct as stated for a product leaf with a finite fuzzy factor, and the new paragraph states the limit of its validity.

## Verification scripts
- `check_casimir_forms.py` / `.out.txt`: items B and A (exact, both s).
- `check_l0_reduction.py` / `.out.txt`: 4D reduction of the fibre-constant sector and the a_1 density.
- `check_hormander_weyl.py` / `.out.txt`: ranks, nilpotent data, Landau f1/f2, eta-contraction eigenvalues, nu, c_0, 3 zeta(3) check, y^4 -> 0 sequence. Uses `cp12_realisation.py` (copy of the 013 realisation).
- `check_landau_vector.py` / `.out.txt`: Fock-space spectra and the s^2 coefficient (22 - n)/6.
- `compile_check_r1.py` / `.out.txt`: scratch-copy build outside the repository: 264 pages, 0 errors, 0 undefined, 0 double-subscript.
- `verify_anchors_labels.out.txt`.
The exploratory files `explore1.py`-`explore3.py` in the folder are superseded by the scripts above.

## Decisions Taken
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
The sign and size of w: the weight-two term of the diagonal and its second variation under the level-one amplitudes (including the T dkappa Y vertex), in a regularisation that handles the vector sector (fibre truncation, fermions, or another Euclidean section); then Lambda/w.

## Special instructions for the gatekeeper
Do not read the paragraph as a derivation of w or of varrho; it is a no-go on a reading plus structure. Check: (a) the Landau diagonal normalisation (Script 3 self-dual check); (b) that "Euclidean contraction eta -> delta with the Lie-Poisson algebra kept" is stated as a continuation choice, not a derivation; (c) the Ben Arous citation is used only for the form of the leading term under equiregularity (abstract-level verification); (d) the l = 0 density is claimed only as a formula for that sector. The MST arXiv:2411.02598 and arXiv:2609.08955 material is not imported.
