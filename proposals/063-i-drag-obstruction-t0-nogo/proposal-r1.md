# Proposal 063-i-drag-obstruction-t0-nogo, round 1

## Result

Two bounded results about the drag/dissipation prescription of Problem~I, plus a
conditional benchmark, none of which closes or narrows the ledger status of
Problem~I:

**(P1, definitional obstruction, bounded and exhaustive over the exits currently
in the repository.)** On the bare data of Presentation~A (matrix-valued
coordinates, Definition~`def:matrix-coords-ext`; action Eq.~`eq:Smatrix`) the
Kubo prescription of `sec:status-I` is not a statement about the matrix model:
there is no c-number pair-separation parameter \(r\) with respect to which
\(\delta\hat F_i=-\partial H/\partial r_i\) could be taken, and therefore no
parameter-labelled correlator \(\chi^R_{ij}(\omega;\mathbf r,\ell_A,\ell_B)\)
either. The prescription becomes well posed only through one of three exits —
(i) a fixed-background class with commuting base coordinates (the
conjugate-coordinate class of the Problem~F entry has commuting \(y^\mu\)), which
requires extending the sector list by localized cores and importing the
identification of a \(y\)-difference with \((d,\ell_A,\ell_B)\); (ii) the
Presentation~B dictionary (`ass:dictionary`), whose conditionality the result
inherits and which cannot discharge the matrix-derived label; (iii) an explicitly
reduced model with imported separation, which is an input model. These are
definitional statements, not a no-go for a future route.

**(P2, bounded T=0 / sub-critical vanishing.)** Inside exit~(iii) (supplied
Hamiltonian, stationary passive reference diagonal in the energy eigenbasis,
connected force operators at fixed \(\mathbf r\)), the transform convention of the
section (\(\chi^R(\omega)=\int\mathrm dt\,e^{i\omega t}\chi^R(t)\)) gives the
spectral representation
\(\operatorname{Im}\chi^R_{(ij)}(\omega)=\frac{\pi}{\hbar}\sum_{m,n}(p_n-p_m)\operatorname{Re}(F^i_{mn}F^j_{nm})\delta\!\bigl(\omega-\tfrac{E_m-E_n}{\hbar}\bigr)\)
for \(\omega>0\) (established derivation; verified numerically two ways), so
\(\operatorname{Im}\chi^R_{(ij)}\) is supported on weighted Bohr frequencies.
Consequences within this bounded class: gapped reference (or finite volume)
\(\Rightarrow\Gamma_{ij}=0\) exactly; gapless linear bath with finite-size
Gaussian cores and derivative coupling: \(\operatorname{Im}\chi^R\propto\omega^3e^{-\omega^2\ell^2/c^2}\)
in \(d=3\) (super-Ohmic, \(\Gamma=0\)); gapped bath: support starts at
\(\omega=\Delta\). NOT universal: in \(d=1\) the same integral is Ohmic,
\(\operatorname{Im}\chi^R=\omega e^{-\omega^2\ell^2/c^2}/(2c^3)\) at the stated
normalization, \(\Gamma=1/(2c^3)\neq0\). The on-shell golden-rule absorption rate
\(P(v)\) vanishes for \(v<\min_q\varepsilon_q/|\mathbf q|\) (Landau criterion —
a criterion, not a theorem; on a lattice the threshold is the minimum phase
velocity, e.g. \(2/\pi\) for \(\omega_k=2|\sin(k/2)|\), not the sound speed
\(c=1\)); the BEK mechanism (Berezhiani–Elder–Khoury 2019, verified) reopens
sub-critical friction when the low-momentum phase velocity is medium-modified.
Consequence: a nonzero working law \(\Gamma\propto d^{-4}\) (`ass:drag`) requires
a definable separation AND an open low-frequency channel with nonzero weighted
spectral weight at \(\omega\downarrow0\); its exponent and tensor are fixed by
that channel, not by the static mutual-information tail. This ties the drag
question to \(G_{\mathrm{eff}}\)/modified propagation (Problem~F), and does not
close Problem~I.

**(P3, conditional benchmark, script-level).** Two impurities in a free
Bogoliubov gas with an imported separation: \(\Gamma_{ij}(r;\ell_A,\ell_B)\) =
r-independent self terms + an oscillatory interference term with O(1)-power
envelope (endpoint asymptotics \(r^{-1}\); measured envelope slopes \(-0.2\) to
\(-1.4\) depending on fit window); NO separation exponent \(-4\) arises in this
class for any core sizes; subsonic rates exactly zero; BEK-type dispersion
lowering reopens them. Benchmark only; nothing here computes or constrains the
NAMCG correlator.

No status, priority or completion label is changed anywhere.

## Target and status

- Problem: **I (dynamical drag / dissipation coefficient)**, `sec:status-I`,
  appH lines 3024–3154 of the certified current bytes.
- Current status verbatim (Ledger-label paragraph, L3027ff):
  "Status: OPEN. Priority: OPTIONAL falsifiable phenomenological extension;
  prerequisite only if drag is claimed as derived or predicted. Completion:
  PROGRAMME-CONDITIONAL."
- Original target (Missing step paragraph, L3139–3147): specify microscopic
  dynamics, stationary reference state and force operators for finite cores;
  compute \(\chi^R_{ij}(\omega;\mathbf r,\ell_A,\ell_B)\); justify passivity and
  low-frequency assumptions; derive longitudinal and transverse responses;
  determine whether they reduce to the isotropic \(d^{-4}\) law and calculate
  its coefficient before estimating \(\eta\).
- Classification of this package: **PROGRAMME-CONDITIONAL contribution**; it
  closes nothing. DERIVED parts: the P1 definitional statements (for the stated
  data), the spectral representation, the exact form-factor integrals, the
  threshold kinematics. The ch17 criterion is unaffected (I is OPTIONAL unless
  drag is claimed derived/predicted).
- depends_on (report-only, per the scout verdict): completion of the I.drag
  target plausibly requires F.coeff (\(G_{\mathrm{eff}}\), and any
  medium-modified low-frequency channel), arguably E (definition of emergent
  separation). Reported, not asserted.

## Source reading

digest + targeted reads. `python scripts/make_digest.py --check` printed
`DIGEST CURRENT`. Read IN FULL: `sec:status-I` entire section (L3024–3154);
appH conjugate-coordinate class paragraphs (L2374–2411); 061/062 exit-exhaustion
precedents; `ch14-dissipation.tex` L100–264 (Kubo pair `eq:linear-response`,
`eq:Gamma-kubo`; `ass:drag`; the registered false ratio claim at L243–258, left
untouched); `ch11-conservation.tex` prop:allowed-drag (L225–301);
`ch17-agenda.tex` Problem~I passages (L575–599, L740–751);
`ch03-matrix-action.tex` `eq:Smatrix` (L143), `def:matrix-coords-ext` (L173),
`ass:dictionary` (L346). Bib read-only: 27350 B, sha
40d6ea09915dd4b8220f30c466821118492ee5560f66930b7c5d9a2dd8b95b90, 86 keys, no
Landau/Berezhiani key present. Certified current appH bytes before any edit:
573239, sha256 08a61b890e33dedf9c3122912c8e4ea6c113fe95396fa4220136d3417b49b9eb,
CRLF 3419, bare LF 0. All anchor counts re-verified against these bytes (see
Verification scripts).

## Research and reasoning

### 1. P1: definitional status

The section takes "\(\mathbf r\) … and \(H(\mathbf r)\) a microscopic Hamiltonian"
as data (L3039–3040). On Presentation~A: coordinates are matrices
(`def:matrix-coords-ext`), the action `eq:Smatrix` is a single-trace matrix
potential with no pair-separation parameter; nothing in the bare data supports
\(\partial H/\partial r_i\) or a tensor index \(i\). This is a definitional gap,
not a computational one: the obstruction is that separation is itself one of the
emergent quantities (consistent with Anous2020-type non-factorization of
subsystems already cited in appH — that citation is used only for the general
point that a tensor-factor subsystem algebra with a separation parameter is not
given in a matrix model). Exhaustion of exits available in the repository:
(i) conjugate-coordinate class (appH L2374–2406): base functions
\(y^\mu=M^{\mu5}/R\) are commuting functions on the leaf, so a difference of base
points is definable; but the class's sector list has no localized matter/impurity
sector, and identifying a \(y\)-difference with the \((d,\ell_A,\ell_B)\) of the
entanglement cores is extra input — any resulting \(\Gamma_{ij}\) is a coefficient
of the extended fixed-background system; (ii) Presentation~B: available but
inherits `ass:dictionary` (the manuscript already says "Every later heat-kernel
formula is a calculation within Presentation~B, contingent on the dictionary");
(iii) reduced model with imported separation: well posed, input-based.
No exit makes \(\Gamma_{ij}\) a bare Presentation~A output; that is the bounded
obstruction. This mirrors the exit-exhaustion pattern accepted in 061/062.

### 2. Spectral representation (established derivation)

With \(\chi^R_{ij}(t)=\frac{i}{\hbar}\theta(t)\langle[\delta\hat F_i(t),\delta\hat F_j(0)]\rangle\)
and \(\chi^R(\omega)=\int\mathrm dt\,e^{i\omega t}\chi^R(t)\) (the convention
actually printed at appH L3057–3060), insert a energy-eigenbasis resolution. The
commutator gives \((p_n-p_m)\)-weighted exponentials
\(e^{\pm i(E_m-E_n)t/\hbar}\); \(\int_0^\infty e^{iat}\mathrm dt=\pi\delta(a)+i\,\mathrm{PV}(1/a)\)
then yields a principal-value real part and, for \(\omega>0\),
\[
\operatorname{Im}\chi^R_{(ij)}(\omega)=\frac{\pi}{\hbar}\sum_{m,n}(p_n-p_m)\operatorname{Re}\!\bigl(F^i_{mn}F^j_{nm}\bigr)\delta\!\Bigl(\omega-\frac{E_m-E_n}{\hbar}\Bigr).
\]
Symmetrization in \((ij)\) is needed for the off-diagonal product structure; the
\(\Gamma\) definition of the section already symmetrizes
(\(\chi^R_{(ij)}\), L3071). Sign check: with this convention
\(\operatorname{Im}\chi^R(\omega>0)\ge0\) for a passive state, consistent with
"Passivity requires this dissipative tensor to be positive semidefinite"
(L3073–3074). Numerically verified in `p2_drag_toy.py` Part A two ways (direct
Heisenberg evolution + damped DFT vs eigenbasis sum, matched Lorentzian
broadening): agreement in sign and in magnitude to within 2–3% broadening
accuracy, 3 random 24-level systems.

Consequences: support = weighted Bohr spectrum. Ground-state reference: support
\(\subset\{E_m-E_0\}\); gapped \(\Rightarrow\) \(\operatorname{Im}\chi^R\equiv0\)
on a neighbourhood of \(\omega=0\) \(\Rightarrow\Gamma_{ij}=0\) exactly (no
assumption about limits needed beyond the displayed identity). Gapless
thermodynamic limit: \(\Gamma_{ij}=0\) whenever the weighted density of states
\(J(\omega)=o(\omega)\) (super-Ohmic); \(\Gamma_{ij}\neq0\) needs
\(J(\omega)\sim c\,\omega\) or heavier at low \(\omega\).

### 3. Exact form-factor integrals (established computation at stated conventions)

Field \(u(x)=\int\frac{\mathrm d^dq}{(2\pi)^d}\frac{b_qe^{iqx}+\mathrm{h.c.}}{\sqrt{2\varepsilon_q}}\);
\(H_{\mathrm{int}}=\int\mathrm d^dx\,W(\mathbf x-\mathbf r)\,\partial_i u\)
(derivative coupling, so \(F_i=-\partial H/\partial r_i\) carries one power of
the core gradient); Gaussian core \(|\widetilde W(\mathbf q)|^2=e^{-q^2\ell^2}\).
Then \(\operatorname{Im}\chi^R(\omega)=\pi\!\int\!\frac{\mathrm d^dq}{(2\pi)^d}
\frac{q^2|\widetilde W|^2}{2\varepsilon_q}\delta(\omega-\varepsilon_q)\) times
the angular factor \(S_d\). Sympy (Part C of `p2_drag_toy.py`) gives exactly:
- \(d=1,\ \varepsilon_q=cq\): \(\operatorname{Im}\chi^R(\omega)=\dfrac{\omega\,e^{-\omega^2\ell^2/c^2}}{2c^3}\),
  \(\Gamma=\dfrac1{2c^3}\neq0\) (Ohmic — the \(1/\sqrt{2\varepsilon_q}\) zero-point
  factor cancels one power of \(\omega\); the naive "derivative coupling ⇒
  super-Ohmic in every d" expectation is wrong in d=1).
- \(d=3,\ \varepsilon_q=cq\): \(\operatorname{Im}\chi^R(\omega)=\dfrac{\omega^3e^{-\omega^2\ell^2/c^2}}{4\pi c^5}\),
  \(\Gamma=0\).
- \(\varepsilon_q=\sqrt{\Delta^2+c^2q^2}\): support only for \(\omega\ge\Delta\)
  (sympy Piecewise/Heaviside form; \(d=1\): \(\sqrt{\omega^2-\Delta^2}e^{-(\omega^2-\Delta^2)\ell^2/c^2}/(2c^3)\);
  \(d=3\): \((\omega^2-\Delta^2)^{3/2}e^{-(\omega^2-\Delta^2)\ell^2/c^2}/(4\pi c^5)\)),
  hence \(\Gamma=0\).

### 4. Landau threshold vs the \(\omega\downarrow0\) coefficient (two distinct statements)

The prescription coefficient \(\Gamma=\lim_{\omega\downarrow0}\operatorname{Im}\chi/\omega\)
and the on-shell absorption rate \(P(v)\propto\sum_k|\langle k|F|0\rangle|^2\delta(\varepsilon_k-\mathbf v\cdot\mathbf k)\)
answer different questions. \(P(v)\) requires a resonant \(\mathbf k\) with
\(\varepsilon_k=\mathbf v\cdot\mathbf k\), hence \(v\ge\min_q\varepsilon_q/|\mathbf q|\):
Landau's criterion (Landau 1941). It is kinematics, not a theorem about
\(\Gamma\): the finite chain example (Part B) shows both coexisting — for
\(\omega_k=\sqrt{\Delta^2+4\sin^2(k/2)}\) the threshold is \(\sqrt5/\pi\approx0.712\)
(gapped) and \(2/\pi\approx0.637\) (gapless, set by \(k=\pi\), NOT the sound
speed 1); below threshold the exact resonance count is 0 and the broadened
\(P_\epsilon(v)\) shrinks proportional to \(\epsilon\) (tail of an exact zero),
while above threshold \(P_\epsilon\) is \(\epsilon\)-independent; yet in the
1D gapless derivative case \(\Gamma\neq0\) even though \(P(v<2/\pi)=0\). The
BEK paper (verified today at arXiv:1905.09297 / JCAP 10 (2019) 074) states in
its abstract that a gravity-tachyonic modification of the sound dispersion
reopens subsonic dynamical friction: the loophole ingredient for the Landau
factor, and the mechanism family of modified propagation in the Problem~F
entry. Hence "sub-critical \(\Rightarrow\) no drag" is false as a general
statement and true only inside the stated bounded class; \(\Gamma=0\) is never
presented as universal.

### 5. P3 benchmark (conditional; script only, no manuscript text)

`p3_two_impurity.py`: two impurities, \(\varepsilon_q=\sqrt{c^2q^2+q^4/4}\),
Gaussian cores \(\ell_A,\ell_B\), separation imported as a parameter,
on-shell rate with self + interference \(\cos(qr\mu^*(q))\) structure.
Subsonic: exactly zero (empty resonance set); supersonic: nonzero; interference
term sign-oscillates with envelope of O(1) negative power (\(\sim r^{-1}\) by
endpoint asymptotics; measured fit slopes \(-1.44\) windowed, tail pointwise
\(-2.4\) to \(-0.2\)); self terms r-independent; no \(-4\) exponent for any
core sizes. BEK-type lowering (\(c_{\rm eff}=\sqrt{c^2-\kappa^2}=0.954\),
\(v=0.97<c=1\)): bare rate 0, modified rate \(3.4\) — reopening demonstrated.
Kept OUT of the manuscript text: it is an input model with imported separation
(exit (iii)) and adds no status-bearing claim; it exists to show what a nonzero
\(\Gamma_{ij}(r;\ell_A,\ell_B)\) looks like structurally, so the "exponent"
question can be posed sharply.

### Literature checked

- Berezhiani, Elder, Khoury, "Dynamical Friction in Superfluids", JCAP 10 (2019)
  074, DOI 10.1088/1475-7516/2019/10/074, arXiv:1905.09297 — record AND the
  specific loophole statement re-verified from the arXiv abstract page during
  this round.
- Landau, "The Theory of the Superfluidity of Helium II", Phys. Rev. 60, 356
  (1941), DOI 10.1103/PhysRev.60.356 — bibliographic record verified in an
  earlier round via the DOI landing page; the criterion's physical content is
  standard and matches the derivation given above; full text NOT independently
  verified.
- Anous2020 (already in bib and appH) is invoked in this proposal only for the
  general point that matrix models do not factorize subsystems; no new claim
  imported.
- The garbled scout key "Bulanikov-Sukhbaeva" is NOT used anywhere.

## Claim classification

| claim | class |
|---|---|
| P1: no separation parameter in bare Presentation-A data; three-exit exhaustion | established (definitional, for the stated data) |
| spectral representation of \(\operatorname{Im}\chi^R_{(ij)}\), sign with the section's convention | established identity/derivation (+ numerical check) |
| gapped/passive \(\Rightarrow\Gamma_{ij}=0\) in exit-(iii) class | conditional result (bounded class) |
| exact \(\omega e^{-\omega^2\ell^2/c^2}/(2c^3)\), \(\omega^3e/(4\pi c^5)\), gapped support \(\omega\ge\Delta\) | established computation at stated conventions |
| Landau threshold \(P(v)=0\) below \(\min\varepsilon_q/q\); lattice threshold \(2/\pi\) | established kinematics (bounded model); criterion not theorem |
| BEK reopening of subsonic friction | literature result (record + abstract verified); mechanism, not applied to NAMCG |
| P3 structure (self + \(r^{-1}\)-type interference, no \(-4\); BEK reopening numerics) | conditional benchmark (input model) |
| "the \(-\eta\mu v/d^4\) law requires an open low-frequency channel + definable separation" | conditional consequence (within stated class) |
| anything about NAMCG \(\eta\), \(\Gamma_{ij}\), the emergent metric, or observations | NOT claimed |

## Proposed changes

File: `chapters/appH-microscopic-proofs.tex` ONLY. One insertion, inside
`sec:status-I`, immediately after the last sentence of the paragraph
"\paragraph{Static tail, distinct from the response.}" (which ends
"...determines the retarded force response, its tensor structure, or its
coefficient.") and immediately before "\paragraph{Missing step.}". Everything
in the Ledger-label paragraph (L3027) and the Status paragraph (L3149–3153) is
kept unchanged; the "Static tail" paragraph itself is kept unchanged; the
"Conditional Kubo formulation" paragraph is kept unchanged. No text in
`ch14-dissipation.tex` is touched (the ch14 Kubo pair and the registered
L243–258 ratio-claim issue are out of scope for this package; the new material
makes no claim that would desynchronize them, because it speaks only about the
bounded exit-(iii) class).

Anchor (verified unique in current bytes, count 1 for the sentence and count 1
for sentence+CRLFs+paragraph):
`response, its tensor structure, or its coefficient.` followed by
`\r\n\r\n\paragraph{Missing step.}` (the bare `\paragraph{Missing step.}`
occurs 9 times in appH, so the uniqueness comes from the prefixed sentence).

Insert file `insert-r1.tex` (LF-only, single block, no `%---SPLIT---%`; CRLF
conversion on apply; content):

```latex
\paragraph{Definitional status of the prescription.} The formulation above takes \(\mathbf r\) and \(H(\mathbf r)\) as data: at fixed \(\mathbf r\) it presupposes a microscopic Hamiltonian depending on separation as an external parameter, so that \(\delta\hat F_i=-\partial H/\partial r_i\) and the correlator are defined. On the bare data of Presentation~A this is not available. The coordinates of Definition~\ref{def:matrix-coords-ext} are matrix-valued and the action Equation~\eqref{eq:Smatrix} contains no pair-separation parameter with respect to which a derivative could be taken, and separation is among the infrared quantities the programme takes to be emergent, so the prescription is not a statement about the matrix model until one of three exits is taken. (i)~A fixed-background class with commuting base coordinates: in the conjugate-coordinate class of the Problem~F entry the base functions \(y^\mu\) commute, so a separation between two localized configurations can be written as a difference in \(y\)-space; but that class must then be extended by a sector supplying localized cores (its sector list contains none), and the identification of a \(y\)-difference with the separation \(d\) and sizes \(\ell_A,\ell_B\) used above is an additional input, so the resulting \(\Gamma_{ij}\) is a coefficient of the extended fixed-background system, not of the bare matrix model. (ii)~The Presentation~B dictionary (Assumption~\ref{ass:dictionary}): geometric separations are available there, but every calculation inherits the dictionary, and a \(\Gamma_{ij}\) obtained this way carries the dictionary's conditionality and cannot discharge the matrix-derived label. (iii)~An explicitly reduced model with imported separation: a bath Hamiltonian, coupling and the parameter \(\mathbf r\) are supplied as inputs; the prescription is then well posed, but the model is an assumption and its \(\Gamma_{ij}\) constrains the NAMCG correlator only if the dictionary route of (ii) is also taken. These statements are for the bare Presentation-A data and the three exits as characterized here; they compute no response, do not exclude the existence of a further route, and change no ledger label; Problem~I remains open.

\paragraph{Low-frequency support and sub-critical vanishing (conditional; not closure).} Within exit~(iii), where the data are supplied, the prescription itself restricts the answer. Let the reference state be stationary and passive, diagonal in the eigenbasis of \(H\) with weights \(p_n\), and let \(F^i_{mn}=\langle m|\delta\hat F_i|n\rangle\) at fixed \(\mathbf r\). With the transform convention of the display above, \(\chi^R_{ij}(\omega)=\int\mathrm dt\,e^{i\omega t}\chi^R_{ij}(t)\), the transform of the commutator has a principal-value real part and, for \(\omega>0\), an imaginary part
\[
\operatorname{Im}\chi^R_{(ij)}(\omega;\mathbf r)
=
\frac{\pi}{\hbar}
\sum_{m,n}
(p_n-p_m)\,
\operatorname{Re}\!\bigl(F^i_{mn}F^j_{nm}\bigr)\,
\delta\!\left(\omega-\frac{E_m-E_n}{\hbar}\right),
\]
so \(\operatorname{Im}\chi^R_{(ij)}\) is supported on the weighted Bohr frequencies of the connected force operators. Consequently, whenever that support stays a positive distance from \(\omega=0\) -- a gapped reference, or finite volume -- \(\Gamma_{ij}=0\) exactly; and for a gapless bath in the thermodynamic limit the tensor vanishes when the weighted density of states vanishes faster than \(\omega\) at low frequency, e.g.\ for finite-size Gaussian cores of size \(\ell\) with derivative coupling to a linear bath \(\varepsilon_q=cq\) in three spatial dimensions, where the form-factor integral gives \(\operatorname{Im}\chi^R(\omega)\propto\omega^3 e^{-\omega^2\ell^2/c^2}\), and for gapped baths \(\varepsilon_q=\sqrt{\Delta^2+c^2q^2}\), where the support starts at \(\omega=\Delta\). The vanishing is not universal: with derivative coupling in one spatial dimension the same integral gives \(\operatorname{Im}\chi^R(\omega)\propto\omega e^{-\omega^2\ell^2/c^2}\) and \(\Gamma\neq0\), so the question is exactly the low-frequency weighted spectral weight. Distinct from this \(\omega\downarrow0\) coefficient is the on-shell absorption rate at velocity \(v\), supported on \(\omega=v\,\mathbf q\cdot\hat{\mathbf v}\): it vanishes for \(v<\min_q\varepsilon_q/|\mathbf q|\) -- on a lattice the minimum phase velocity, not the long-wavelength sound speed, sets the threshold -- which is the Landau criterion \cite{Landau1941}, a kinematic criterion and not a theorem; a medium-modified dispersion with lowered low-momentum phase velocity reopens sub-critical Cherenkov friction \cite{BerezhianiElderKhoury2019}, the same mechanism family as modified propagation in the Problem~F entry. A drag law of the working form \(\Gamma\propto d^{-4}\) with nonzero coefficient (Assumption~\ref{ass:drag}) therefore requires, beyond a definable separation, an open low-frequency channel with nonzero weighted spectral weight at \(\omega\downarrow0\) at every separation in the regime, and its exponent and tensor structure are fixed by that channel, not by any static tail. These statements are for the exit-(iii) class of supplied Hamiltonians, stationary passive reference states and finite-size Gaussian cores at the stated truncations; they do not compute the NAMCG correlator, do not constrain the dictionary or the emergent metric, do not establish or exclude the \(d^{-4}\) law, and give no value or sign of any coefficient; Problem~I remains open.
```

Labels referenced (verified present, unique): `def:matrix-coords-ext`
(ch03:173), `eq:Smatrix` (ch03:143), `ass:dictionary` (ch03:346),
`ass:drag` (ch14:184). No new `\label` is introduced; the displayed equation is
unnumbered, matching the section's existing style. New citation keys (not in
`bib/namcg.bib`, no collision anywhere in the repository):

```bibtex
@article{Landau1941,
  author  = {Landau, L.},
  title   = {The Theory of the Superfluidity of Helium {II}},
  journal = {Phys. Rev.},
  volume  = {60},
  pages   = {356},
  year    = {1941},
  doi     = {10.1103/PhysRev.60.356}
}

@article{BerezhianiElderKhoury2019,
  author        = {Berezhiani, Lasha and Elder, Benjamin and Khoury, Justin},
  title         = {Dynamical Friction in Superfluids},
  journal       = {J. Cosmolog. Astropart. Phys.},
  volume        = {2019},
  number        = {10},
  pages         = {074},
  year          = {2019},
  doi           = {10.1088/1475-7516/2019/10/074},
  eprint        = {1905.09297},
  archivePrefix = {arXiv}
}
```

The integrator must add both entries (gatekeeper-accepted text only); until
then the two `\cite`s would be undefined. Stale passages elsewhere: none
introduced; the sentence the block is anchored after is kept verbatim.

Predicted post-state of appH (from `simulate_apply.py` run this round):
size **578723**, sha256
**5b5fc2650f05d95dce7fb7a4ed96ca282b946dbf7a3b3d2e368331b65638a631**,
CRLF **3433**, bare LF 0; bib unchanged (27350, 40d6ea09…).

## Verification scripts

All in this folder; run with `python -I <script>` (authoritative `.out` files
committed alongside):

- `p2_drag_toy.py` / `p2_drag_toy.out` — Part A: spectral representation,
  eigenbasis formula vs direct Heisenberg evolution + damped DFT, same
  broadening \(\epsilon=0.05\), sign and magnitude agreement (3 systems);
  ground-state weighted-Bohr gap ⇒ \(\Gamma=0\). Part B: finite chain +
  external-parameter heavy site (exit-(iii) benchmark): discrete support gap;
  Landau threshold table (gapped 0.712, gapless 0.637) with exact resonance
  counts and \(\epsilon\)-scaling of the broadened rate. Part C: sympy exact
  form-factor integrals quoted above.
- `p3_two_impurity.py` / `p3_two_impurity.out` — P3 benchmark: Cherenkov
  threshold zeros, self + interference structure, envelope-slope diagnostics,
  asymmetric cores \((\ell_A,\ell_B)\) amplitude dependence, BEK reopening
  (\(v=0.97\): bare 0, modified 3.41).
- `simulate_apply.py` / `simulate_apply.out` — byte-level splice rehearsal:
  pre-state asserts (573239 / 08a61b89… / CRLF 3419 / bare LF 0; bib echo),
  anchor uniqueness, LF→CRLF conversion, post-state prediction, junction
  checks, Ledger-label untouched check.

## Decisions Taken

1. **P3 kept script-level only, no manuscript sentence.** It is an exit-(iii)
   input model; a manuscript sentence about it would need its own scoping text
   for marginal value and risks the H1 hazard (reified dragged-medium reading).
   Rejected alternative: one benchmark sentence in appH.
2. **Single insert block, no split marker.** The two paragraphs share anchor,
   section and status consequence; one block is the minimal verifiable unit.
3. **No new `\label` for the displayed spectral formula** — nothing references
   it; the section's existing displays are unnumbered. Rejected: adding
   `eq:I-spectral` (unused label).
4. **`\Gamma\propto(\omega^{3},\omega)e^{-\omega^2\ell^2/c^2}` written with
   `\propto` in the manuscript; exact coefficients kept in this proposal and
   the scripts** (normalization of the core coupling is convention-dependent).
5. **Landau content attribution phrased as criterion** because the full 1941
   text was not re-read this round; record verified.
6. **"or its coefficient." chosen as anchor** (with the prefixed sentence)
   because bare `\paragraph{Missing step.}` is not unique in appH (9 occurrences)
   — recorded so the integrator does not "simplify" the anchor.
7. **Citations restricted to the scout allow-list** plus already-in-bib Anous2020;
   Bulanikov-Sukhbaeva never cited.

## Milestone assessment

Routine. No milestone trigger: Problem~I is OPTIONAL and remains OPEN and
PROGRAMME-CONDITIONAL; nothing is closed. The package follows the accepted
061/062 pattern (bounded obstruction + bounded conditional results recorded
next to the ledger entry).

## Status-label recommendation

Current critical-path set re-derived from ch17 (L575–599 region and the
criterion passage) and appH ledger: A, B, C, D1, E, F, G-derived, N
(OPEN, CRITICAL PATH); H, I, J optional within their scopes; I: OPEN / OPTIONAL
falsifiable / PROGRAMME-CONDITIONAL. **Affected labels: none.** This proposal
requests no change to any status, priority or completion classification.

## Author decision needed

None. (The bounded results preserve emergence; nothing here is STRUCTURAL.)

## Remaining open step

To close the ORIGINAL I target one still needs, for the stated programme:
(1) a definable route to \((\mathbf r,\ell_A,\ell_B)\) as parameters of a
NAMCG Hamiltonian (none of exits (i)–(iii) does this without inputs);
(2) a microscopic dynamics + stationary passive reference for finite cores;
(3) a computed \(\chi^R_{ij}(\omega;\mathbf r,\ell_A,\ell_B)\) with an open
low-frequency channel (weighted spectral weight \(\sim\omega\) at
\(\omega\downarrow0\)) at every separation in the regime — per P2 this is the
exact place the missing ingredient sits;
(4) derivation of the longitudinal/transverse structure and the \(d^{-4}\)
exponent and coefficient as outputs.

Ranked open avenues after the bounded no-go (hypothesis → relaxation):
1. **Sector/field content:** the no-go's super-Ohmic branch is about a
   derivative-coupled scalar bath; other field content (the \(\psi\) sector,
   gauge sectors, fermions) can carry different low-\(\omega\) weighted
   spectral weight — revisit after F/E progress.
2. **Medium-modified dispersion / regulator:** BEK-type lowering of the
   low-momentum phase velocity reopens the channel (ties to F.coeff,
   \(G_{\mathrm{eff}}\)); verified numerically in the benchmark; the NAMCG
   analogue is unexamined.
3. **Background:** the bounded class used a stationary passive reference about
   one background; a reference with soft modes (gapless weighted support
   accumulating at 0 with weight \(\sim\omega\)) evades the \(\Gamma=0\) branch
   by assumption — the question becomes whether the NAMCG reference state is of
   that kind, which needs E/entanglement input.
4. **Truncation:** tree/quadratic spectral weight can vanish while loop or
   contact-term weight does not; the P2 vanishing statements are single-particle
   form-factor statements and say nothing about many-body continuum channels.
5. **Presentation:** exit (i)+(ii) hybrid (commuting base coordinates plus
   dictionary identification) is not excluded by P1; it is a definitional
   programme, not a computation, and would still not carry the matrix-derived
   label without more.

## Special instructions for the gatekeeper

- Re-derive the spectral representation yourself with the section's printed
  convention \(\chi^R(\omega)=\int e^{i\omega t}\chi^R(t)\); check the
  \((p_n-p_m)\operatorname{Re}(F^i_{mn}F^j_{nm})\) structure against the
  symmetrized \(\chi^R_{(ij)}\) definition at appH L3071, and re-run
  `p2_drag_toy.py` (Part A sign agreement depends on this convention; a sign
  error here would not affect the vanishing claims but would corrupt the
  displayed formula).
- Re-run the Part C sympy integrals and check the d=1 Ohmic claim against the
  \(1/\sqrt{2\varepsilon_q}\) factor (this is the one place where naive
  power counting fails).
- Must NOT be asserted anywhere: that \(\eta\) or \(\Gamma_{ij}\) is derived;
  that the NAMCG correlator was computed; that the \(d^{-4}\) law is excluded
  or confirmed; any observational content. The insert says "do not establish or
  exclude" — preserve exactly.
- Verify the two `\cite` keys resolve only after the bib entries above are
  added; flag as undefined-reference risk, do not integrate insert text without
  the gatekeeper-accepted BibTeX.
- Do not treat the P2 no-go as extending beyond: stationary passive reference,
  supplied exit-(iii) Hamiltonians, Gaussian finite-size cores, derivative
  coupling, single-particle spectral representation (no loops, no other
  sectors, no dynamical background). Its BEK sentence is a cited mechanism, not
  our derivation.
- The anchor sentence "response, its tensor structure, or its coefficient."
  must remain verbatim; the uniqueness of the splice anchor depends on it.
- ch14 L243–258 (registered false ratio claim) is deliberately untouched; this
  package does not repair or reference it. Do not import its exponent language.
