# Proposal 122-d1-bilocal-nondeg, round 1

## Result

For the bilocal composite reading of the frame, \(M(x,y)=\Phi(x)W(x,y)\Phi(y)^\dagger\),
the two-point-kernel non-degeneracy step recorded as an open gap in the Appendix H
D-probe region ("pointwise singular-value bounds do not control the smallest
singular value of a two-point kernel") is discharged as follows. (1) Exact
reduction (established): \(T_M=\mathsf P\,T_W\,\mathsf P^\dagger\) gives
\(\sigma_{\min}(T_M)\ge c^2\,\sigma_{\min}(T_W)\) and
\(\kappa(T_M)\le(C/c)^2\kappa(T_W)\), so the gap is exactly the transport number
\(w:=\sigma_{\min}(T_W)\), and (sharp, proved by examples) no bound on \(w\) can
follow from pointwise \(\Phi\)-data alone. (2) Positive derivation (conditional on
explicit hypotheses): on a finite carrier with unitary transport matrices - the
matrix link-variable / fuzzy Wilson-line class, the finite-\(N\) matrix-theory
regime - \(w=1\) exactly and uniformly in carrier size, so
\(\sigma_{\min}(T_M)\ge c^2\), and with the recorded region bound
\(\sigma_i(\Phi)^2\ge v^2-2\sqrt{\varepsilon/\lambda}\) this is
\(\sigma_{\min}(T_M)\ge v^2-2\sqrt{\varepsilon/\lambda}>0\) for
\(\varepsilon<\lambda v^4/4\). (3) Conditional state version: under the single
one-point moment hypothesis \(\mu_{\mathcal V}:=\mathbb E_\omega[\mathcal V(x)]<\lambda v^4/4\),
the coincidence composite satisfies
\(\lambda_{\min}(\mathbb E_\omega[\Phi\Phi^\dagger])\ge\sup_{\mu_{\mathcal V}<\varepsilon<\lambda v^4/4}(v^2-2\sqrt{\varepsilon/\lambda})(1-\mu_{\mathcal V}/\varepsilon)>0\);
the hypothesis is sharp at the recorded defect threshold. (4) Scoped obstructions
(established counterexamples and computations): the off-diagonal expectation
composite is not boundable from pointwise data (Haar average vanishes identically);
on continuum smooth-kernel carriers \(w=0\) (compact operators are not bounded
below; the exactly computable heat-kernel instance has smallest eigenvalue
\(\exp(-s^2n^2/4)\to0\) while a fixed band keeps \(e^{-s^2K^2}\)) - so the bilocal
non-degeneracy statement must live on a finite carrier or at the coincidence
fibre; and for path-ordered transporters
\(\sigma_{\min}(W)\ge\exp(-\int\sigma_{\max}(\omega))\), with equality on
scalar-gauge paths and \(=1\) for anti-Hermitian integrands. The paragraph lands
in the D-region; it closes none of Problem D, D1, F, N and changes no status.

## Target and status

- Target: frontier chain 7, edge D1.lorentz avenue 2 - the composite/two-point-kernel
  non-degeneracy gap for the bilocal reading of Assumption ass:nondeg, recorded
  verbatim at appH-microscopic-proofs.tex L1713 (D-probe region), the named-uncovered
  head edge of chain 7 (frontier.yaml chain-7 note; proposals/059-d1-lorentz-local-frame
  review-r1 L37 avenue (2): "explicit bilocal composite frame with matrix parallel
  transporters and a computed non-degeneracy criterion for ass:nondeg").
- Current manuscript status (appH Problem D ledger, read live this round): Problem D
  OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL; missing step includes "The locked frame
  and its non-degeneracy must also be derived rather than assumed (Assumptions
  ass:frame-lock and ass:nondeg)". D1 is Chapter 17 full-GR order item 1; F is item 3
  (ch17 L653-656: F consumes D1's ghost operators \(\omega,A_\mu,B\); L659-663: N
  consumes F's \(G_{\rm eff}\)). This package addresses one named substep of D1
  (composite non-degeneracy under explicit hypotheses); it does NOT close D1, and
  reports DERIVED only for the conditional statements above. No label change proposed.
- Dependencies consumed as recorded inputs (not re-derived): eq:V potential, vacuum
  manifold, defect threshold \(\inf\{\mathcal V:\det\Phi=0\}=\lambda v^4/4\) at fibre
  \((0,v,v,v)\), region bound \(r\le r_\varepsilon\) and
  \(\sigma_i^2\ge v^2-2\sqrt{\varepsilon/\lambda}\) (appH L1711-1713), Gibbs one-point
  moment paragraph (L1715). NO-ADVANCE compliance: no re-run of the pointwise state-route
  bound, the Gibbs probe, slice refinements, eq:V selection via shift breaking, or the
  \(A_\mu/\omega\) tensor threshold sums; those enter only as cited recorded inputs.

## Source reading

digest + targeted reads (digest was stale/dirty per dispatch; targeted full-range reads
used). Read in full this or the immediately preceding round: appH L763-812 (Problem D
ledger and missing step), L1704-1719 (all five D-probe paragraphs, the gap sentence,
the Gibbs paragraph, and the 118 paragraph following the insertion point, verified live
bytes: anchor paragraph at L1715, insertion before L1718), L4066-4124 (item-121 style
model and scope-sentence house style), ch04-vierbein-emergence.tex L170-175 (ass:nondeg
statement), ch17-agenda.tex L329-370 (Problem D), L403-471 (Problem F missing step),
L648-686 (dependency order items 1,3,4), proposals/059-d1-lorentz-local-frame
proposal-r3.md L47,L115 and review-r1.md L37 (avenue (2) wording), frontier.yaml chain 7
note and no-gos (extracted to temp file to avoid single-line blowups). Live pin
re-verified at generation time: appH = cf3139fbedb0 / 857887, unchanged; anchor
occurs exactly once and is immediately followed by CRLFCRLF (join count 1). Unreadable
files: none.

## Research and reasoning

Notation: \(\sigma_{\min},\sigma_{\max}\) smallest/largest singular value;
\(\kappa=\sigma_{\max}/\sigma_{\min}\); \(T_K\) the integral operator of kernel \(K\)
on \(L^2(\mathrm d\mu_c)\otimes\mathbb C^4\).

- R0 (established identity, checked 60 trials, d=2..5):
  \(\sigma_{\min}(AB)\ge\sigma_{\min}(A)\sigma_{\min}(B)\) and
  \(\sigma_{\max}(AB)\le\sigma_{\max}(A)\sigma_{\max}(B)\); equality when a factor is
  unitary; strict in general (example diag(1,2)diag(2,1): \(\sigma_{\min}=2>1\)).
- R1 (established): for measurable essentially bounded \(\Phi\),
  \(T_M=\mathsf P T_W\mathsf P^\dagger\) exactly (direct computation of the slice
  kernels, 40 block trials to 1e-9), and \(\sigma_{\min}(\mathsf P)=\sigma_{\min}(\mathsf P^\dagger)=\operatorname{ess\,inf}\sigma_{\min}(\Phi)=c\).
  Applying R0 twice: \(\sigma_{\min}(T_M)\ge c^2 w\);
  \(\sigma_{\max}(T_M)\le C^2\sigma_{\max}(T_W)\); \(\kappa(T_M)\le(C/c)^2\kappa(T_W)\).
  Sharpness (two teeth, proved): \(\Phi\equiv v\mathbb I\) with rank-3 projector
  transport: \(w=0=\sigma_{\min}(T_M)\) with \(\Phi\) invertible; fibre with
  \(\sigma_{\min}=10^{-5}\): \(\sigma_{\min}(T_M)\) tracks \(c^2\), not \(C^2\). Hence
  the recorded gap sentence is exactly the statement that pointwise data bounds only
  \(c\): the missing quantity is \(w\).
- R2 (established): \(\sigma_{\min}(AUB^\dagger)\ge\sigma_{\min}(A)\sigma_{\min}(B)\)
  with equality on radial fibres \(\Phi=\rho U\) (30 trials exact to 1e-9) and strict
  for non-radial fibres (60-trial tooth); \(\det\) multiplicativity exact (60 trials).
  Correction made during development: an assumed equality for general fibres was
  found numerically false (worst abs error 0.92); the package states inequality +
  radial equality only.
- R3 (established): coincidence \(\sigma_{\min}(\Phi\Phi^\dagger)=\sigma_{\min}(\Phi)^2\);
  threshold chain \(r_\varepsilon=v-\sqrt{v^2-2\sqrt{\varepsilon/\lambda}}\),
  \((1-r_\varepsilon/v)^4=(\sigma_{\min}^2/v^2)^2\)-form consistency with the recorded
  \(\lvert\det e\rVert\) bound, checked over the full region
  \(\varepsilon\in[0,\lambda v^4/4)\) (80 trials), threshold fibre \((0,v,v,v)\) at
  \(\mathcal V=\lambda v^4/4\).
- Positive case (ii): finite carrier, transport matrix unitary:
  \(\sigma_{\min}(T_U)=1\) exactly (Kronecker structure, \(N=2..8\), \(d=4\),
  \(v=1.9,\delta=0.6\) over the full admissible fibre range), so
  \(\sigma_{\min}(T_M)\ge(v-\delta)^2\), and on \(\{\mathcal V\le\varepsilon\}\),
  \(\ge v^2-2\sqrt{\varepsilon/\lambda}\). Teeth: \(c\to0\) kills the bound; singular
  (rank-3 projector) transport gives \(\sigma_{\min}(T_M)=0\) with \(\Phi\) invertible.
  The result is a conditional derivation: hypothesis = finite carrier + unitary
  transport class (link variables / exactly unitary fuzzy Wilson lines); the
  conclusion is a strictly positive kernel lower bound derived from the recorded
  pointwise inputs. What is NOT claimed: that the NAMCG transporter is in this class
  (an input scoped in the paragraph), and equality of \(\sigma_{\min}(T_M)\) with the
  bound (inequality only; R2).
- R5 (established): for positive-semidefinite \(A\) with \(\lambda_{\min}(A)\ge s\),
  every compression \(PAP\) satisfies \(\lambda_{\min}(PAP|_{\rm ran P})\ge s\)
  (variational principle; 30 trials, d=6); for non-positive factors this fails
  (analytic example \(A=\begin{pmatrix}1&4\\4&1\end{pmatrix}\):
  \(\sigma_{\min}=3\) but the corner entry is 1; numerically 300-trial search agrees).
  This is why the transported object is the positive composite
  \(Q=\Phi\Phi^\dagger\).
- State bound (iv): \(\lambda_{\min}\) is concave on positive operators, so
  \(\lambda_{\min}(\mathbb E Q)\ge\mathbb E[\lambda_{\min}(Q)]\) (Loewner/Jensen);
  pointwise \(\lambda_{\min}(Q)\ge(v^2-2\sqrt{\varepsilon/\lambda})\mathbf 1_{\{\mathcal V\le\varepsilon\}}\);
  Markov \(\mathbb P(\mathcal V>\varepsilon)\le\mu_{\mathcal V}/\varepsilon\); optimize
  over \(\varepsilon\in(\mu_{\mathcal V},\lambda v^4/4)\). MC check (3 reps, p=0.7
  mixture at the threshold fibre): bound positive and \(\le\mathbb E[\lambda_{\min}]\)
  (best 0.271 vs 1.585). Teeth: \(\mu_{\mathcal V}=\lambda v^4/4\) makes the bound
  nonpositive (best \(-10^{-18}\)); double-collapsed fibre gives
  \(\mathbb E[\lambda_{\min}]=0\). Off-diagonal: \(\mathbb E[M]\) under independent
  Haar rotations of the fibres vanishes identically (expectation of the middle unitary
  is 0; MC 4000 samples: \(\lVert\mathbb E M\rVert=0.032\to0\)); so no off-diagonal
  \(\langle M\rangle\) non-degeneracy follows from pointwise data - the same
  mean-field obstruction recorded at L1717, now proved for the composite. This is why
  (iv) is stated for the coincidence composite and not for \(e=\langle\Phi\rangle/v\).
- Carrier topology (v): a compact operator on an infinite-dimensional space cannot
  be bounded below (else the identity is compact), and every smooth-kernel operator on
  a finite-measure domain is Hilbert-Schmidt, hence compact: continuum smooth-kernel
  carriers have \(w=0\). Explicit exactly-computable instance (T2, exact spectrum,
  not numerics-dependent): periodic \(n\)-point grid, \(T_W=F\,{\rm diag}(e^{-s^2k^2})F^\dagger/n\),
  \(\sigma_{\min}=e^{-s^2n^2/4}\) (3.2e-3, 9.9e-11, 3.1e-18, 2.8e-19 at n=32..256,
  s=0.15) while the \(|k|\le3\) band compression keeps \(e^{-s^2\cdot9}=0.816686\)
  grid-independently. Conclusion (established): the bilocal non-degeneracy claim must
  be carried by a finite carrier (the matrix-theory regime, case (ii)) or the
  coincidence fibre (iii) - a presentation choice forced by the mathematics.
- Transport bound: for \(U'=A(t)U\),
  \(\tfrac{d}{dt}\lVert U^{-1}\rVert\le\sigma_{\max}(A)\lVert U^{-1}\rVert\) gives
  \(\sigma_{\min}(U(t))\ge\exp(-\int\sigma_{\max}(A))\); equality for scalar
  \(A=-g\mathbb I\) (T5, attained to 1e-9); anti-Hermitian \(A\) gives unitary \(U\),
  \(\sigma_{\min}=1\) (30 trials, 150 slices). This connects (ii) to connection
  classes: metric-compatible (anti-Hermitian) class connections sit at the good end.
- Comparison with prior items: 059 avenue (2) asked for exactly this criterion;
  115/116/117 remain single-site (pointwise defect threshold, state non-degeneracy,
  state measure); this package is the two-point extension and consumes their recorded
  outputs without re-running them; the 1717 mean-field gap is shown to bind the
  off-diagonal composite too (Haar vanishing). No result here re-runs a NO-ADVANCE
  route.

## Claim classification

1. R0, R1 (factorization + estimates), R2, R3, R5, heat-kernel spectrum, transport
   bound, Haar vanishing, threshold sharpness: established identities / derivations
   (numerically checked where stated; analytic arguments given).
2. Case (ii) \(w=1\) bound and (iv) moment bound: conditional derivations under the
   explicit hypotheses (finite carrier, unitary transport class; \(\mu_{\mathcal V}<\lambda v^4/4\)).
3. Hypotheses (finite carrier, connection class of \(W\), state \(\omega\), smallness
   of \(\mu_{\mathcal V}\)): inputs, not derived from eq:Smicro; the identification of
   the NAMCG transporter with the unitary class is an input, scoped in text.
4. "Finite-\(N\) matrix-theory regime is the right carrier": mechanism/conjecture
   about the programme's intended reading; the paragraph only states that a continuum
   smooth-kernel reading cannot carry \(w>0\).
5. Unresolved: computation of \(w\) for a specific proposed NAMCG carrier beyond the
   unitary class; derivation of the transporter/connection class from the matrix
   theory; selection of the state; off-diagonal (mean-field) control; anything closing
   D/D1/F/N.

## Proposed changes

File: chapters/appH-microscopic-proofs.tex only. One insertion: a new `\emph{...}`
paragraph between the Gibbs-probe paragraph (ends "...so Problem~D remains OPEN and
PROGRAMME-CONDITIONAL.", live L1715) and the Presentation-A selection paragraph
(starts "\emph{Constraint results on the Presentation-A selection of
Equation~\eqref{eq:V}.}", live L1718). Anchor (verified unique, count 1, join
count 1): the final sentence of the Gibbs paragraph,
`remains the upstream input that gates what any Presentation-B measure can be cited as; Assumptions~\ref{ass:frame-lock} and~\ref{ass:nondeg} remain assumed, so Problem~D remains OPEN and PROGRAMME-CONDITIONAL.`
Kept: everything before and after, both surrounding paragraphs verbatim; no existing
sentence is removed or replaced. No stale passage elsewhere needs changing: the
recorded gap sentence at L1713 stays true (the new paragraph proves pointwise-only
bounds impossible, consistent with it).

Canonical splice (as executed in make_payload_122.py, count=1):
`replace(anchor + CRLFCRLF, anchor + CRLFCRLF + payload + CRLF, 1)`, yielding
POST = PRE + len(payload) + 2 = 857887 + 5783 + 2 = 863672,
POST sha1 = c577442aab35c7d4a736557c32cc17ae91079736; layout verified in
preview-appH-spliced.tex: Gibbs paragraph, blank line, new paragraph, blank line,
Presentation-A paragraph. payload-122.tex sha1 = 33165816b9fd404bf77899ed4eaf8efa84e6368b
(pure ASCII, one CRLF-terminated line, braces 50/50, no `$`, no `\label`, no `\cite`;
refs used and each verified once in live chapters: ass:nondeg, ass:frame-lock, eq:V,
eq:vev-is-frame, eq:vacuum-manifold, eq:Smicro).

Payload text (bytes identical to payload-122.tex):

```latex
\emph{Bilocal composite: exact reduction of the two-point-kernel gap and conditional non-degeneracy bounds.} This paragraph records derivations that discharge the two-point-kernel non-degeneracy step under explicit hypotheses and scope what the bilocal reading of Assumption~\ref{ass:nondeg} can supply. Let \(M(x,y)=\Phi(x)\,W(x,y)\,\Phi(y)^\dagger\) be the bilocal composite with transport coefficients \(W(x,y)\in\mathbb C^{4\times4}\) on a carrier measure \(\mathrm d\mu_{\rm c}\) over the base, and let \(T_M\) be the operator \((T_M f)(x)=\int M(x,y)f(y)\,\mathrm d\mu_{\rm c}(y)\) on \(L^2(\mathrm d\mu_{\rm c})\otimes\mathbb C^4\), with \(T_W\) the operator of \(W\) alone and \(\kappa(T):=\sigma_{\max}(T)/\sigma_{\min}(T)\). (i)~Reduction. The factorization \(T_M=\mathsf P\,T_W\,\mathsf P^\dagger\), with \(\mathsf P\) fibrewise multiplication by \(\Phi\), applied to the identities \(\sigma_{\min}(AB)\ge\sigma_{\min}(A)\,\sigma_{\min}(B)\) and \(\sigma_{\max}(AB)\le\sigma_{\max}(A)\,\sigma_{\max}(B)\), gives: if \(c\le\sigma_{\min}(\Phi)\) and \(\sigma_{\max}(\Phi)\le C\) \(\mathrm d\mu_{\rm c}\)-a.e., then \(\sigma_{\min}(T_M)\ge c^2\sigma_{\min}(T_W)\) and \(\kappa(T_M)\le(C/c)^2\kappa(T_W)\). The gap recorded above therefore reduces exactly to the transport-kernel lower bound \(w:=\sigma_{\min}(T_W)\), and no bound on \(w\) follows from pointwise \(\Phi\)-data: with \(\Phi\equiv v\,\mathbb I\) and \(W\) fibrewise a rank-deficient projector, \(w=0=\sigma_{\min}(T_M)\) with \(\Phi\) invertible, and a fibre of smallest singular value \(c\) drives the bound at rate \(c^2\). (ii)~Unitary-transporter carrier case. If the carrier is finite and the transporter matrix is unitary -- matrix link variables and exactly unitary fuzzy Wilson lines, path-ordered exponentials of anti-Hermitian fibre connections, for which \(\sigma_{\min}=1\) exactly and uniformly in the carrier size -- then \(w=1\) and \(\sigma_{\min}(T_M)\ge c^2\); on a region where \(\mathcal V\le\varepsilon\) for \(\mathcal V\) of Equation~\eqref{eq:V}, the recorded bound \(\sigma_i(\Phi)^2\ge v^2-2\sqrt{\varepsilon/\lambda}\) upgrades this to \(\sigma_{\min}(T_M)\ge v^2-2\sqrt{\varepsilon/\lambda}>0\) for \(\varepsilon<\lambda v^4/4\). The estimate is an inequality in general, with equality on radial fibres \(\Phi=\rho\,U\), so it transfers non-degeneracy and does not determine the spectrum of \(T_M\). (iii)~Coincidence fibre and positivity. At coincidence, \(\sigma_{\min}(\Phi\Phi^\dagger)=\sigma_{\min}(\Phi)^2\) and \(\det(\Phi\Psi^\dagger)=\det\Phi\,\overline{\det\Psi}\) hold exactly, so the diagonal composite inherits pointwise non-degeneracy; every orthogonal compression of a positive-semidefinite fibre bounded below by \(c\) retains lower bound \(c\), while compression of a non-positive factor can drop below \(\sigma_{\min}\) -- positivity of the composite is what transports. (iv)~Diagonal state bound. For any one-point state \(\omega\) with potential moment \(\mu_{\mathcal V}:=\mathbb E_\omega[\mathcal V(x)]<\lambda v^4/4\), the Loewner estimate \(\lambda_{\min}(\mathbb E_\omega[\Phi\Phi^\dagger])\ge\mathbb E_\omega[\lambda_{\min}(\Phi\Phi^\dagger)]\), the fibre identity of (iii), and Markov's inequality give \(\lambda_{\min}(\mathbb E_\omega[\Phi\Phi^\dagger])\ge\sup_{\mu_{\mathcal V}<\varepsilon<\lambda v^4/4}\,(v^2-2\sqrt{\varepsilon/\lambda})(1-\mu_{\mathcal V}/\varepsilon)>0\): under the single moment hypothesis \(\mu_{\mathcal V}<\lambda v^4/4\) -- the one-point moment class made finite by the Gibbs paragraph above, whose smallness remains an input -- the coincidence composite \(\mathbb E_\omega[\Phi\Phi^\dagger]\) is state-nondegenerate; this is a statement about the composite and not about the mean-field frame \(e=\langle\Phi\rangle/v\) of Equation~\eqref{eq:vev-is-frame}, whose control is the mean-field gap recorded above. The hypothesis is sharp, the bound being non-positive at \(\mu_{\mathcal V}=\lambda v^4/4\) on the threshold fibre \((0,v,v,v)\), and no analogous bound holds for the off-diagonal expectation composite, whose fibre-wise Haar average vanishes identically. (v)~Carrier topology. The lower bound \(w\) is a property of the carrier, not of the kernel alone: on a periodic grid of \(n\) points the Fourier-diagonalised heat kernel of diffusion parameter \(s\) has smallest eigenvalue \(\exp(-s^2 n^2/4)\to0\), while its compression to a fixed band \(|k|\le K\) has grid-independent smallest eigenvalue \(\exp(-s^2K^2)\); a continuum smooth-kernel reading of the composite therefore cannot carry a uniform \(w>0\), and the bilocal non-degeneracy of Assumption~\ref{ass:nondeg} must be stated on a finite carrier as in (ii), the finite-\(N\) matrix-theory regime, or through the coincidence fibre (iii). For a path-ordered transporter \(W=P\exp\int\omega\) one has \(\sigma_{\min}(W)\ge\exp(-\int\sigma_{\max}(\omega))\), with equality on scalar-gauge paths and \(\sigma_{\min}=1\) for anti-Hermitian \(\omega\). Scope: (i)-(iii) and (v) are identities and conditional estimates under the stated a.e.\ bounds with explicit sharpness examples, and (iv) is a conditional estimate under the stated moment hypothesis; the carrier measure, the connection class of \(W\), and the state \(\omega\) are inputs and are not derived from Equation~\eqref{eq:Smicro}, no measure or state is constructed here, the off-diagonal expectation composite is not bounded, the vacuum-manifold fibre measure of Equation~\eqref{eq:vacuum-manifold} is untouched, and the computation of \(w\) for the specific carrier of Problem~D1 remains open; Assumptions~\ref{ass:frame-lock} and~\ref{ass:nondeg} remain assumed and this paragraph closes none of Problem~D, Problem~D1, Problem~F or Problem~N, all of which remain OPEN and PROGRAMME-CONDITIONAL.
```

No other file changes. bib: none. Figures/code: none.

## Verification scripts

Folder: proposals/122-d1-bilocal-nondeg/. All scripts fixed-seed, run twice, outputs
byte-identical (see manifest.md).

- bilocal_nondeg_s1.py (df1d198e305b) - fiber/operator algebra R0-R6 with 5 teeth
  (strict-R0 example; rank-3 projector transport; near-degenerate fibre; threshold
  fibre; non-positive compression). Reproduce:
  `python -I proposals/122-d1-bilocal-nondeg/bilocal_nondeg_s1.py`
  expect last line `FAILURES: 0 (none)`; invariant OK lines include
  "R1 kernel factorization exact (40)", "R1 TOOTH sW=0 forces sM=0 (Phi invertible)",
  "R2 equality on radial shells rho*U (30)", "R3 threshold chain vs recorded form",
  "R5 TOOTH non-positive compresses below s". Output out-s1-run{1,2}.txt = 62ea7c6e5b25.
- bilocal_nondeg_s2.py (f57402f6ca0e) - T1 unitary fuzzy transport (N=2..8 full range,
  teeth c->0, singular W); T2 exact-spectrum heat kernel collapse 3.2e-3..2.8e-19 vs
  carrier 0.816686 == e^{-0.2025}; T3 Haar-mean composite ~0 (4000); T4 Loewner+Markov
  bound (3 reps, p=0.7, 4000-point epsilon grid) with threshold and double-collapse
  teeth; T5 transport bound, anti-Hermitian, scalar-path sharpness. Reproduce:
  `python -I proposals/122-d1-bilocal-nondeg/bilocal_nondeg_s2.py`
  expect `FAILURES: 0 (none)`. Output out-s2-run{1,2}.txt = 2ab6fb1050ee.
- make_payload_122.py (8c29318d3995) - regenerates payload-122.tex and
  preview-appH-spliced.tex deterministically; 7 hygiene detectors each proven to fire
  by an injected positive control (non-ASCII byte, missing terminator, lone CR,
  injected `\label`, injected `$`, unresolvable ref, unbalanced `\)`): "controls
  fired: 7/7"; prints PRE 857887 PAY 5783 POST 863672 and both sha1s; asserts
  POST = PRE + PAY + 2. Reproduce:
  `python -I proposals/122-d1-bilocal-nondeg/make_payload_122.py`
  expect `GEN-FAILURES: 0 (none)`. pdflatex was NOT run (dispatch constraint; build
  check belongs to the integrator).

## Decisions Taken

- Stated R2 as inequality + radial-equality after the equality conjecture failed
  numerically (error 0.92); rejected keeping an equality claim.
- Made the finite carrier + unitary transport the primary positive case (w=1 exactly,
  matching the actual finite-N matrix-theory regime) rather than proposing a
  continuum regularization of \(T_W\): continuum operators are provably not bounded
  below, so any such route would smuggle in a non-emergent background structure and
  fail; rejected as unsound and off-mission.
- Kept the state bound at the coincidence composite (positive \(Q=\Phi\Phi^\dagger\))
  rather than claiming control of \(e=\langle\Phi\rangle/v\): the Haar-vanishing
  obstruction makes the off-diagonal/mean-field reading unsupported; rejected.
- Recorded the transport lower bound \(\exp(-\int\sigma_{\max}(\omega))\) as a scoping
  statement connecting (ii) to anti-Hermitian connection classes rather than
  promoting it to a NAMCG result (connection class is an input).
- Chose the payload landing after the Gibbs paragraph (consumes its moment class by
  citation, "the Gibbs paragraph above") instead of after L1713: keeps referents
  "above" correct and avoids touching the 118 paragraph's boundary.

## Milestone assessment

Routine. No milestone trigger: this is a conditional sublemma package (one named
D1 substep under explicit hypotheses plus sharp scoping), no critical-path problem
is closed and no missing link is closed without retained hypotheses (the transport
hypotheses are retained inputs).

## Status-label recommendation

Derived from live Chapter 17 criterion and Appendix H this round: critical path at
the full-GR scope = A, B, C, D1, E, F, G-derived, N; all remain OPEN as recorded.
Affected labels: none. No status, priority, or completion-classification change is
proposed. Label changes: none.

## Author decision needed

None.

## Remaining open step

To close the recorded step fully one still needs: (a) the computation of \(w\) (or a
proof of membership in the unitary/anti-Hermitian transport class) for the specific
carrier and class connection of the NAMCG matrix theory, derived from eq:Smicro;
(b) identification of the carrier (finite fuzzy carrier vs emergent continuum limit -
(v) shows the continuum smooth-kernel limit cannot carry \(w>0\), so the carrier
statement is part of the target); (c) state selection and the mean-field input for
any expectation-value reading; (d) the rest of D1 (frame existence, ghost operators
\(\omega,A_\mu,B\) for F). D, D1, F, N all stay OPEN and PROGRAMME-CONDITIONAL.

## Special instructions for the gatekeeper

Scope limits - the payload must not be read as asserting: construction of a state or
measure; control of \(\langle\Phi\rangle\) or \(e=\langle\Phi\rangle/v\); that the
NAMCG transporter is unitary (hypothesis); any closure or status change; a result for
the emergent metric (all operator statements are for the composite on a stated
carrier). Re-check, in order: (1) R0/R1/R2 (inequality directions; radial equality;
the false-equality correction is reflected in the text); (2) the two-sided estimate
and both sharpness examples in R1; (3) the (iv) Loewner-Markov chain and threshold
sharpness at \(\lambda v^4/4\); (4) the heat-kernel exact spectrum and the
compactness statement; (5) payload hygiene (pure ASCII, one line, ends CRLF, zero new
labels/cites, the six refs resolve), anchor uniqueness and POST bytes/sha1 against
manifest.md (863672, c577442aab35...); (6) re-run both scripts (expect
FAILURES: 0 (none)) and the generator (GEN-FAILURES: 0 (none), PAY 5783). No pdflatex
was run by the researcher; do not infer compile-cleanness from this package - the
integrator runs scripts/build_check.py after integration. Do not require milestone
language: this package closes none of Problem D, D1, F, N.
