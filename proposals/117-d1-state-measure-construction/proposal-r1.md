# Proposal 117-d1-state-measure-construction, round 1

## Result

Under stated Presentation-B hypotheses, the single consumable estimate left open
by the integrated item 116 is realized: a Euclidean Gibbs history measure on a
finite-dimensional truncation of the condensate-field space is **constructed**
with normalizing integral \(0<\mathcal Z<\infty\), and its first moment of the
spacetime-integrated potential is finite **automatically** - it is a theorem of
the construction, not a hypothesis on it:
\(\mathbb E_\mu[S_E]\le(2/e)\,\mathcal Z(1/2)/\mathcal Z(1)<\infty\) (from
\(\sup_{s\ge0}se^{-s/2}=2/e\)) and
\(\mathbb E_\mu[\mathcal V(x)]\le(8C^4/\mathrm{Vol})\,\mathbb E_\mu[S_E]+\lambda v^4(16C^4+1)\).
Typed to one-point distributions \(\omega_x\), the 116 bound becomes
\(\omega_x\{\det e(x)=0\}\le\min\{1,4\,\mathbb E_{\omega_x}[\mathcal V(x)]/(\lambda v^4)\}\),
and it **saturates to zero identically**, \(\omega_x\{\det e(x)=0\}=0\), because
the singular set is a proper real-algebraic cone while the truncation contains
the constant identity field (pushforward of an \(e^{-S_E}\)-density: absolute
continuity). By Fubini, \(\mu\)-almost every configuration has
spacetime-Lebesgue-**null** defect set \(\{x:\det\Phi(x)=0\}\) - null, not
empty. For the \(\beta\)-family \(\mu_\beta\propto e^{-\beta S_E}\), convexity
of \(\ln\mathcal Z(\beta)\) (Holder) makes \(\mathbb E_{\mu_\beta}[S_E]\)
nonincreasing, giving the volume-averaged soft-event bound
\(\mathrm{Vol}^{-1}\!\int\omega_x\{\mathcal V(x)\ge\lambda v^4/4\}\,\mathrm{dvol}
\le 4\,\mathbb E_{\mu_{\beta_0}}[S_E]/(\lambda v^4)\) for all \(\beta\ge\beta_0\).
The tracking factor \(f\) of the 116 reduction equals
\(f=4\,\mathbb E_\mu[S_E]/(\lambda v^4)\cdot\)Vol-normalization, explicitly
bounded above. Nothing is closed: the measure is a Presentation-B probe
measure, **not** a matrix-theory state; the Presentation-A selection of
Equation (eq:V) remains the upstream gating input; the truncation is not
removed; and the vacuum-expectation reading of the frame would additionally
require mean-field control that is not provided (mixtures of non-singular
fields can average to a singular one). Problem D remains OPEN, CRITICAL PATH,
PROGRAMME-CONDITIONAL.

## Target and status

- **Problem**: D (local Lorentz / locked frame), specifically the D1
  frame-non-degeneracy **state/measure route**: 116 reduced frame
  non-degeneracy to one consumable estimate - existence/characterization of a
  state or integration measure \(\mu\) with
  \(E_\mu[\mathcal V]\le f\cdot\lambda v^4/4\), typed via one-point
  distributions \(\omega_x[\mathbf1_{\det e(x)=0}]\le4\omega_x[\mathcal V(x)]/(\lambda v^4)\).
  The gatekeeper's 116 review-r2 ranked avenue (1): build a Gibbs/Euclidean
  measure in which \(\mathcal V\) enters positively with weight \(e^{-S_E}\) so
  first-moment finiteness is automatic.
- **Current status (appH, "Ledger label" paragraph of `\section{Problem D: local Lorentz}`, verbatim)**:
  "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL.
  Reduced-scope result: D2, imposed local Lorentz symmetry, supports only a
  scope-limited Presentation-B model; D remains OPEN and the matrix-derived
  criterion is unmet."
- **Missing step (appH, verbatim)**: "The locked frame and its non-degeneracy
  must also be derived rather than assumed (Assumptions~\ref{ass:frame-lock}
  and~\ref{ass:nondeg})."
- **Chapter 17 criterion (ch17 L327-345, verbatim excerpt)**: "D1 closure also
  requires that the locked frame exist and be non-degenerate on the claimed
  domain, derived from the same microscopic data rather than taken from
  Assumptions~\ref{ass:frame-lock} and~\ref{ass:nondeg}." Completion words per
  ch17 L58-61: "Derived means that the problem's target has no remaining
  assumed premise in the claimed chain."
- **Classification of this package**: conditional construction + derived
  consequences - PROGRAMME-CONDITIONAL. It does not DERIVE anything for the
  full-GR criterion (Wick rotation, compactness, truncation, and the probe-measure
  status vs a matrix-theory state are all retained premises).
- **Dependencies (upstream, unchanged by this package)**: Presentation-A
  selection of Eq. (eq:V) (`sec:ch3-relate`) gates what any Presentation-B
  measure can be cited as (recorded in the integrated 116 text); the operator
  specification of D1 (\(\omega,A_\mu,B\), ghosts) is untouched here;
  `ass:frame-lock` and `ass:nondeg` remain assumed.
- **Non-duplication vs 114/115/116**: 114 is the locked-ghost-sector spec
  (different target); 115 derived the threshold
  \(\inf\{\mathcal V:\det\Phi=0\}=\lambda v^4/4\) (consumed here by reference,
  not re-derived); 116 proved the measure bound for an **arbitrary** measure
  space and explicitly recorded that no state or integration measure is
  constructed. This package supplies exactly that missing object (a specific
  measure) and sharpens 116's bound to the exact nullity
  \(\omega_x\{\det e=0\}=0\) on it; it reuses 116's statement only through the
  integrated paragraph.

## Source reading

digest + targeted reads. `python -I scripts/make_digest.py --check` printed
`DIGEST CURRENT` this run. Read in full: `chapters/appH-microscopic-proofs.tex`
Problem D ledger and the three integrated paragraphs L1690-1714 (ghost-sector,
Elitzur/Elitzur-composite, 115-threshold, 116-state-route) including the exact
anchor line and its 140-byte pre-context; `chapters/ch03-matrix-action.tex`
eq:Smicro/eq:V/sec:ch3-relate regions; `chapters/ch04-vierbein-emergence.tex`
L85-170 (eq:vev-is-frame, ass:nondeg, eq:g-from-e); `chapters/ch17-agenda.tex`
L56-62, L327-346, L650-656; `proposals/116-d1-state-nondeg-realization/review-r2.md`,
`manifest.md`, `cert-r116p.py` (model for the certificate). Label uniqueness
re-verified across `chapters/` (`.tex` sources): `eq:Smicro`, `eq:V`,
`eq:vacuum-manifold`, `eq:vev-is-frame`, `eq:g-from-e`, `ass:nondeg`,
`ass:frame-lock`, `sec:ch3-relate`, `eq:Phi-eom` each defined exactly once
(second grep hits are stale `.aux` artifacts, not manuscript sources).
Baseline: appH sha1 `28f3a0d2401efc1c65b53a99a5968cdcb70fed7d`, 834663 B (the
116-integrated canonical POST). Unreadable files: none. No full-scan trigger
(no definition, assumption, scope-statement or status-passage change; not a
milestone).

## Research and reasoning

All numerals below are derived in-package or traced to recorded manuscript
constants (`lambda v^4/4`, `v`, `lambda`). Units: \(\lambda,v\) are the recorded
coupling and vacuum radius; write \(|\cdot|_F\) for the Frobenius norm.

### 1. Coercivity and pointwise control of V (established identities)

With \(s_i=\sigma_i(\Phi)^2\), \(T=\sum s_i=|\Phi|_F^2\), \(Q=\sum s_i^2\),
Eq. (eq:V) expands exactly as
\(\mathcal V=\frac\lambda4(Q-2v^2T+4v^4)\) (check S1). Since \(Q\ge T^2/4\),
\(\tfrac{32}\lambda\mathcal V-T^2+64v^4=8Q-T^2+64v^4-16v^2T\ge2T^2-T^2+64v^4-16v^2T=(T-8v^2)^2\ge0\),
so
\[ \mathcal V\;\ge\;\frac\lambda{32}|\Phi|_F^4-2\lambda v^4 \qquad\text{(S3)}, \]
and \(Q\le T^2+2v^2T\) gives the upper bound
\(\mathcal V\le\frac\lambda4|\Phi|_F^4+\lambda v^4\) (S3c). Sanity: at
\((0,v,v,v)\): \(\mathcal V=\lambda v^4/4\), the recorded 115 threshold (S4).

### 2. The Gibbs construction and \(0<\mathcal Z<\infty\) (conditional derivation)

Hypotheses (recorded as such, not derived): (H1) the Presentation-B background
\((M,g^{(0)})\) of Eq. (eq:Smicro) is closed (compact without boundary) with
volume element \(\mathrm{dvol}\), \(\mathrm{Vol}<\infty\); (H2) the Euclidean
continuation \(S_E[\Phi]=\int(|D\Phi|_F^2+\mathcal V(\Phi))\,\mathrm{dvol}\)
exists (Wick-rotation input; the background gauge field is fixed); (H3) the
field is restricted to a finite-dimensional real-linear subspace (the
truncation) of matrix fields containing the constant fields, with coordinates
\(\phi\in\mathbb R^K\), and the evaluation maps \(L_x:\phi\mapsto\Phi(x)\) are
nonzero (automatic: \(L_x\phi_{\mathbb I}=\mathbb I\)). On \(\mathbb R^K\) set
\(\mu=\mathcal Z^{-1}e^{-S_E}\prod_k\mathrm d\phi_k\).
Finiteness: \(\mathcal V\ge(\lambda/32)|\Phi|_F^4-2\lambda v^4\) and
\(\int|\Phi|_F^4\mathrm{dvol}=0\Rightarrow\Phi\equiv0\), so on the unit sphere
of the truncation \(q(\phi)=\frac{\lambda}{128}\int|\Phi|_F^4\,\mathrm{dvol}>0\)
continuously, hence uniformly \(q_0>0\); \(S_E(tu)\ge t^4q_0-(\lambda v^2/2)t^2\mathrm{Vol}-2\lambda v^4\mathrm{Vol}\)
uniformly in directions \(u\), so \(e^{-S_E}\) is dominated outside a ball by
\(e^{-q_0\|\phi\|_2^4/2}\) and \(\mathcal Z\le C''+\int e^{-c|\phi|^4}\mathrm d\phi<\infty\);
the dominating super-Gaussian integral has closed form
\(\mathrm{surf}\cdot\Gamma(D/4)/(4c^{D/4})\) (S7: 0.1734998 both by quadrature
and closed form). Positivity: on the tube of constant fields
\(\Phi=v(\mathbb I+E)\), \(\|E\|_F\le\rho\), the upper bound gives
\(S_E\le\mathrm{Vol}\,[(\lambda/4)v^4(2+\rho)^4+\lambda v^4]=:c_0\) (numerically
checked: max tube \(V=0.2953\le10.7656\), N10), so
\(\mathcal Z\ge e^{-c_0}\,\omega_{32}\rho^{32}v^{32}>0\),
\(\omega_{32}=\pi^{16}/16!=4.303070\times10^{-6}\) (S6). Hence \(0<\mathcal Z<\infty\).

### 3. Automatic first moment (conditional derivation; realizes the 116 hint)

The 116 gatekeeper note: for \(V\ge0\) entering with weight \(e^{-\int V}\),
domination makes the first moment automatic since \(\sup_t te^{-t}<\infty\).
Here the measure is constructed, so the finite-first-moment hypothesis of
116-C9 is *discharged by construction*. Chain: (a) interpolation on the
truncation, \(\sup_x|\Phi(x)|_F\le C\|\phi\|_2\), \(C^2=\sup_x\sum_k|E_k(x)|_F^2\)
(N2/N15: max surplus \(\le0\) numerically; identity for an \(L^2\)-orthonormal
matrix-valued basis \(C=4C_L\)); (b) Jensen/Cauchy-Schwarz
\(\mathrm{Vol}^{-1}\!\int|\Phi|_F^4\ge(\mathrm{Vol}^{-1}\!\int|\Phi|_F^2)^2=(\mathrm{Vol}^{-1}\|\phi\|_2^2)^2\);
(c) coercivity \(\mathrm{Vol}^{-1}\!\int|\Phi|_F^4\le(32/\lambda)(\mathrm{Vol}^{-1}\!\int\mathcal V\,\mathrm{dvol}+2\lambda v^4)\);
combining, pointwise in \(x\):
\(\mathcal V(x)\le\frac\lambda4C^4\|\phi\|_2^4+\lambda v^4\le\frac{8C^4}{\mathrm{Vol}}\int\mathcal V\,\mathrm{dvol}+\lambda v^4(16C^4+1)\le\frac{8C^4}{\mathrm{Vol}}S_E+\lambda v^4(16C^4+1)\)
(N15: min slack \(1.608\times10^{10}>0\) over 30 random matrix-valued trig fields).
Taking \(\mathbb E_\mu\) and using
\(\mathbb E_\mu[S_E]=\mathcal Z^{-1}\int S_Ee^{-S_E}\le\mathcal Z(1)^{-1}\sup_{s\ge0}\{se^{-s/2}\}\mathcal Z(1/2)=\frac2e\frac{\mathcal Z(1/2)}{\mathcal Z(1)}\)
(S5: \(2/e\) at \(s=2\); N5-ES-bound: \(6.08164\le366.515\) in the 1-site model)
gives the stated automatic bound. The \(f\)-factor of the 116 reduction is
therefore explicit:
\(f=4\,\mathbb E_\mu[\mathcal V(x)]/(\lambda v^4)\le4[(8C^4/\mathrm{Vol})\,\mathbb E_\mu[S_E]+\lambda v^4(16C^4+1)]/(\lambda v^4)\).

### 4. Typed one-point nullity and Fubini (conditional derivation)

The law \(\omega_x\) of \(\Phi(x)\) is the pushforward of the
\(\mathbb R^K\)-Lebesgue-a.c. density \(e^{-S_E}/\mathcal Z\) under the linear
map \(L_x\); it is absolutely continuous w.r.t. Hausdorff measure on
\(\mathrm{ran}\,L_x\). The cone \(\mathcal C=\{\det=0\}\) is real-algebraic, and
\(L_x^{-1}\mathcal C\) is a **proper** algebraic subset of \(\mathbb R^K\)
because \(L_x(\phi_{\mathbb I})=\mathbb I\notin\mathcal C\). A proper real
algebraic subset of \(\mathbb R^K\) has Lebesgue measure zero and its image
under \(L_x\) is Hausdorff-\(0\) in \(\mathrm{ran}\,L_x\), hence
\(\omega_x\{\det\Phi(x)=0\}=0\) **exactly**. The 115 threshold gives the
containment \(\{\det=0\}\subseteq\{\mathcal V\ge\lambda v^4/4\}\) and 116's
measure bound applies verbatim to the *soft event*:
\(\omega_x\{\mathcal V(x)\ge\lambda v^4/4\}\le\min\{1,4\mathbb E_{\omega_x}[\mathcal V(x)]/(\lambda v^4)\}\)
(N8). Joint measurability holds (smooth fields, finite truncation), so Fubini
gives \(\mathbb E_\mu\big[\int\mathbf1_{\{\det\Phi=0\}}\mathrm{dvol}\big]=\int\omega_x\{\det=0\}\mathrm{dvol}=0\):
the defect set is spacetime-Lebesgue-null for \(\mu\)-a.e. configuration -
**null, not empty**; it does not discharge the pointwise `ass:nondeg`.
Probes: N6 (complex-Gaussian small ball: fitted exponent 2.05 over 5 usable
\(\varepsilon\)s, \(P(10^{-2})=0\) in batch tail - codim-2 cone carries no
mass); N7 (explicit smooth field \(\det\Phi(x)=\tfrac12+\cos2\pi x_0+i\sin2\pi x_1\)
with rank-2 zeros: tube fractions collapse with fitted slope 2.07: defect set
null). These probes illustrate the null/tube mechanism; they assert no
genericity of the physical field.

### 5. Beta-family and averaged consumption (established under hypotheses)

Holder (log-convexity of \(L^p\) norms) gives \(\ln\mathcal Z(\theta\beta_1+(1-\theta)\beta_2)\le\theta\ln\mathcal Z(\beta_1)+(1-\theta)\ln\mathcal Z(\beta_2)\):
\(\ln\mathcal Z\) is convex, hence (its derivative is nondecreasing and
\(\mathbb E_{\mu_\beta}[S_E]=-\tfrac{\mathrm d}{\mathrm d\beta}\ln\mathcal Z(\beta)\)
a.e.) \(\beta\mapsto\mathbb E_{\mu_\beta}[S_E]\) is nonincreasing (N13: secant
slopes \(-12.42,-4.41,-1.90,-0.89,-0.44,-0.16\) increasing; N5-mono:
\(\mathbb E_{\mu_\beta}[S_E]\) strictly decreasing over \(b\in[0.5,64]\)).
Markov on the one-point law, then integrating in \(x\), then using
\(\int\mathcal V\le S_E\):
\(\mathrm{Vol}^{-1}\int\omega_x\{\mathcal V(x)\ge\lambda v^4/4\}\,\mathrm{dvol}\le4\,\mathbb E_{\mu_\beta}[S_E]/(\lambda v^4)\le4\,\mathbb E_{\mu_{\beta_0}}[S_E]/(\lambda v^4)\).
In the 1-site truncation the numerics additionally show the rate
\(4\mathbb E_{\mu_\beta}[\mathcal V]=O(1/\beta)\) (b·f in [22.2, 32.3],
f(64) = 0.4770; N5-rate) and the general super-Gaussian event bound
\(P_\beta\{\mathcal V\ge T\}\le e^{-\beta T/2}\mathcal Z(\beta/2)/\mathcal Z(\beta)\)
(N11). The \(O(1/\beta)\) rate is numerical for the 1-site model only, not
claimed in the payload; the rigorous package input used is the Laplace-chart
lower bound \( \mathcal Z(\beta)\ge c\beta^{-q}\) (verified on grid in the
checked form \(\mathcal Z(b)\ge\mathcal Z(1)e^{-1}b^{-9}\), N9).

### 6. Computation method and recorded dead leads

- **Dead lead (recorded)**: tensor-product Gauss-Legendre quadrature on
  singular values is **unreliable** for this integrand: 72 vs 96 nodes give
  rel-diff 0.772 (identical at \(b=1,16,64\)) because the Vandermonde factor
  \(\prod_{i<j}(\sigma_i^2-\sigma_j^2)^2\) concentrates the measure onto
  hyperplanes; quadrature was abandoned, not tuned.
- **Fix used**: exact-factorization importance sampling. Proposal
  \(q_1(\sigma)\propto\sigma^{13}e^{-\beta(\sigma^2-1)^2/4}\) (per \(\sigma\)),
  weight \(w=\prod_{i<j}(\sigma_i^2-\sigma_j^2)^2/\prod_i\sigma_i^{12}\)
  bounded away from the \(\sigma\to0\) boundary and exact for all \(\beta\);
  \(\ln\)-partition differences by adjacent ratios
  \(\ln\mathcal Z(b_1)-\ln\mathcal Z(b_2)=\ln\mathbb E_{q_{b_2}}[we^{(b_2-b_1)W}]-\ln\mathbb E_{q_{b_2}}[w]\).
  Seed-split convergence N4 (rel-diff \(<8\%\)).
- **Dead lead**: the constant tube lower bound gives
  \(\mathcal Z(\beta)\ge c e^{-\beta c_0}\) - exponentially weak for
  \(\beta\)-ratios of moments; the polynomial Laplace-type bound (Sect. 5) is
  the one that closes.
- **Rejected**: rescaling \(V\to\beta V\) alone (the kinetic term scales too;
  not a free parameter).
- **Recorded gap (positive result boundary)**: the vev reading
  \(e=\langle\Phi\rangle/v\) (Eq. eq:vev-is-frame) is an **averaged** object:
  a mixture of fields with \(\det\Phi(x)\neq0\) everywhere can have
  \(\det\mathbb E_\mu[\Phi(x)]=0\) (e.g. average of \(I\) and \(-I\) is 0), so
  the one-point nullity does NOT imply frame non-degeneracy at vev level; no
  mean-level statement is claimed. This is the honest boundary of the package.
- Kinetic-mode facts used by the truncation picture (N3, exact numerically,
  rel-err \(2.19\times10^{-16}\)): on a lattice-Fourier span
  \(\int|\nabla\Phi|_F^2\mathrm{dvol}=\sum_k(2\pi)^2|k|^2\|\phi_k\|_F^2\) and
  \(k=0\) is the unique constant mode.

### Comparison with the original target

The 116-reduced target asked for a state/measure with
\(E_\mu[\mathcal V]\le f\lambda v^4/4\), \(f\) tracked, connecting the
one-point estimate to a non-vanishing-determinant conclusion. Delivered: a
concrete measure with explicit \(f\), the determinant cone at exact
\(\omega_x\)-measure zero, and an a.s.-null defect set - inside hypothesis
class (H1)-(H3). Not delivered: a matrix-theory state (H1)-(H3 define a
Presentation-B Euclidean probe theory, not the matrix model); truncation
removal; Wick-rotation derivation; vev-level non-degeneracy. The target
remains OPEN, with the state-route gap relocated from "no measure exists"
(this package) to "the physical measure of the matrix theory is not shown to
be of this Gibbs form / truncation-independent / vev-non-degenerate".

## Claim classification

- C1 Coercivity lower bound \(\mathcal V\ge(\lambda/32)|\Phi|_F^4-2\lambda v^4\)
  and upper \(\mathcal V\le(\lambda/4)|\Phi|_F^4+\lambda v^4\): **established
  identities** (S1-S4; one-line algebra above).
- C2 \(0<\mathcal Z<\infty\) on the truncation: **conditional derivation**
  under (H1)-(H3) (S6, S7, N10).
- C3 Automatic finite first moment,
  \(\mathbb E_\mu[\mathcal V(x)]\le(8C^4/\mathrm{Vol})\mathbb E_\mu[S_E]+\lambda v^4(16C^4+1)\),
  \(\mathbb E_\mu[S_E]\le(2/e)\mathcal Z(1/2)/\mathcal Z(1)\): **conditional
  derivation** (N2/N15/N5-ES-bound; 116-gatekeeper hint realized).
- C4 Soft-event typed Markov bound (116 estimate applied to \(\omega_x\)):
  **conditional derivation** (116 integrated result + 115 threshold; N8).
- C5 \(\omega_x\{\det e(x)=0\}=0\) exactly: **conditional derivation** under
  (H3) (absolute continuity; proper algebraic cone; N6 probe).
- C6 \(\mu\)-a.s. null defect set: **conditional derivation** (Fubini; N7 probe).
- C7 \(\ln\mathcal Z\) convex, \(\mathbb E_{\mu_\beta}[S_E]\) nonincreasing,
  averaged soft-event bound: **established under (H1)-(H3)** (N13, N5; N9 grid
  check of the Laplace-input form).
- C8 Hypotheses (H1)-(H3): **input** (compactness, Wick rotation, truncation
  choice assumed, not derived).
- C9 Matrix-theory origin of the measure; removal of the truncation;
  Wick-rotation derivation; vev-level mean-field control: **unresolved**.
- C10 \(O(1/\beta)\) decay rate: **numerical** (1-site model; not in payload).

## Proposed changes

### File `chapters/appH-microscopic-proofs.tex` (single chain, two edits)

**Edit A (stale-passage correction, integrated-116 paragraph).** The clause
occurs exactly once in the live tree and becomes false after Edit B:
- replace (verbatim, count 1):
  `no state of the matrix theory and no integration measure is constructed`
- by:
  `no state of the matrix theory is constructed (the Euclidean Gibbs measure of the paragraph below is a Presentation-B probe measure, not a matrix-theory state)`
- byte delta \(+87\). Everything else in the paragraph is kept.

**Edit B (insert).** Payload `insert-d1-state-measure.tex` (4597 B, sha1 `b514e44a19ee627f0aab4ac3d4f69bc052506154`, one leading
blank CRLF line + one paragraph line + CRLF) inserted immediately before the
unique line `\section{Problem E: signature}` via the 115-form join
`data.replace(ANCHOR, PAYLOAD + CRLF + ANCHOR, 1)`; the payload begins with a
CRLF separator so the new paragraph is blank-line separated from the 116
paragraph (which currently ends `...PROGRAMME-CONDITIONAL.\r\n` with NO blank
line before the anchor), and carries no trailing blank line. Expected POST:
amended `a38d4e293806a09f7fc5072a273ae49f62100590` (834750 B), POST `7e0546a425c16b55e30f2513a228efd836c120b8` (839349 B)
= baseline 834663 + 87 (amend) + 4597 (payload) + 2 (join).

Anchor verification: `anchor count 1` at byte 281406; 140-byte pre-context
ends `...h3-relate}; and Assumptions~\ref{ass:frame-lock} and~\ref{ass:nondeg}
remain assumed, so Problem~D remains OPEN and PROGRAMME-CONDITIONAL.\r\n`.

Payload reference targets (verified unique `\label` in `.tex` sources):
`eq:Smicro`, `eq:V`, `eq:vacuum-manifold`, `eq:vev-is-frame`, `ass:nondeg`,
`ass:frame-lock`, `sec:ch3-relate`. Payload contains no `\label`, no `\cite`,
no `eq:Phi-eom` (carry-over (ii): the background-relative optimality witness
is not restated), ASCII only, CRLF-terminated, one scoped closing sentence
keeping Problem D OPEN and PROGRAMME-CONDITIONAL.

**Stale-passage audit elsewhere**: the 116 sentences "these are geometric
statements about configurations..." and "the small-measure exception obtained
when \(E_{\mathcal V}>0\) is a fortiori not the pointwise statement of
Assumption~\ref{ass:nondeg}..." remain true and are kept; ch17 D1 text
(L327-345) and the appH D ledger are untouched; the 115 threshold paragraph is
untouched; no Chapter 17 scope statement or Appendix H status line is altered
by this package. Carry-over (i) honored: the payload hypothesizes/constructs
the history measure with finite first moment explicitly and keeps \(\mu\) and
\(\mathrm{dvol}\) notationally distinct (and its scope sentence upgrades the
116 conditional "whenever the weighted measure exists" to the realized
statement); carry-over (iii): ch17 "Completion words" pointer taken as L58-61.

## Verification scripts

All in this folder; run with `python -I -B <script>` (seed 117; interpreter
`python 3.11`, numpy/sympy/scipy).

- `verify_r117.py` -> recorded `out-r117.txt`. 31 checks: S1-S7 symbolic
  (expansion identity; coercivity via the \((T-8v^2)^2\) completion; upper
  bound; recorded threshold; \(\sup te^{-t/2}=2/e\); \(\omega_{32}=\pi^{16}/16!\);
  super-Gaussian integral closed form vs quadrature); N2 interpolation +
  Holder; N3 Fourier orthonormality, kinetic identity (rel-err \(2.19\mathrm{e}{-}16\)),
  unique \(k=0\); N4 importance-sampling positivity/convergence; N5 monotone
  \(\mathbb E_\beta[S]\), rate, ES bound; N13 convexity; N8 Markov; N11 event
  bound; N12 second moment; N9 Laplace lower-bound form; N15 interpolation +
  full linearization chain; N6 codim-2 small ball (slope 2.05); N7 rank-2-zero
  defect-tube (slope 2.07); N10 tube bound. **Invariant output**: last two
  lines `PASS 31 FAIL 0` / `ALL CHECKS DONE 117`, exit 0. Symbolic output is a
  check, not a proof; the proofs are Sects. 1-5 above.
- `gen_payload_117.py` -> `insert-d1-state-measure.tex`, byte-identical on
  re-run (sha1 `b514e44a19ee627f0aab4ac3d4f69bc052506154`, 4597 B). **Invariant output**: `bytes 4597 CR 2 LF 2 CRLF 2 ... endsCRLF True
  BOM False backslash-ws 0` + `PAYLOAD SCAN OK`.
- `cert-r117p.py` -> recorded `out-cert-r117p.txt`: out-of-repo copy (untracked
  `namcg-book7.bbl` included), Edit A + Edit B applied to the copy (anchor and
  amendment string recounted), two pdflatex passes, hard asserts before
  `CERT PASS`. **Invariant output**:
  `rc1=0 rc2=0 errlines=0 outw=True undefrefs_pass2=0`,
  `undefrefs-touching-package-labels=0`, `CERT PASS` (run twice: the first run
  FAILED with `! Undefined control sequence` at `l.1715` of the spliced copy -
  a fragment-boundary macro-absorption bug where `\propto` was immediately
  followed by `e`, rendering `\proptoe`; the generator was fixed by inserting
  the boundary space, correcting three mismatched `\lvert...Vert` delimiter
  pairs to `\lVert...Vert`, and adding a durable fragment-join assertion
  that rejects `\macro`+letter boundaries; the regenerated 4597-byte payload
  then passed two passes cleanly); baseline line
  `baseline sha1 28f3a0d2401efc1c65b53a99a5968cdcb70fed7d size 834663`;
  amended line `a38d4e293806a09f7fc5072a273ae49f62100590 size 834750 (delta +87)`;
  POST line `7e0546a425c16b55e30f2513a228efd836c120b8 size 839349`.

- `_scan_macro_join.py` -> audits the payload for macro tokens outside a
  standard-macro whitelist (catches macro-absorption like `\proptoe`; the
  residual flags `equiv`, `ln`, `mapsto` are legitimate macros whitelisted by
  hand).

Reproduction pack (exact commands, from this folder):
`python -I -B verify_r117.py` (expect `PASS 31 FAIL 0`);
`python -I -B gen_payload_117.py` (expect `PAYLOAD SCAN OK`, `bytes 4597`);
`python -I -B cert-r117p.py` (expect `CERT PASS`, `POST sha1 7e0546a425c16b55e30f2513a228efd836c120b8`).

## Decisions Taken

1. **Construction class**: finite-dimensional Euclidean Gibbs truncation
   (chosen) vs continuum field measure (rejected: no microscopic measure
   theory exists for the target action, and finiteness/positivity become
   unproved) vs matrix eigenvalue ensemble (rejected: would silently import a
   large-N assumption beyond Presentation B). The truncation is the smallest
   hypothesis class where the consumable estimate is derivable grade.
2. **Headline claim**: kept the exact nullity \(\omega_x\{\det e=0\}=0\)
   (positive derivation-grade output) rather than only the Markov-type
   re-typing of 116; soft-event bound retained for the non-nullity-reachable
   soft set. Rejected: claiming pointwise non-degeneracy (invalid: null !=
   empty) and vev-level non-degeneracy (invalid without mean control; mixture
   counterexample recorded in Research).
3. **Stale 116 clause**: corrected by a minimal in-place amendment (Edit A)
   rather than weakening 117's wording; after Edit A the 116 statement remains
   literally true and points to the new paragraph.
4. **Beta-family content in payload**: rigorous monotonicity + averaged bound
   only; the \(O(1/\beta)\) rate and Laplace numerics stay proposal-side
   (rule: payload = derived-grade statements under stated hypotheses).
5. **Probe design**: N7 rewritten from a generic trigonometric field (whose
   |det| never approaches 0 on the grid - no crossings, slope undefined) to an
   explicit rank-2-zero field probing the correct codim-2 tube scaling; N6
   eps grid calibrated to counts >= 30. Both are probes of the null/tube
   mechanism only.
6. **Notation**: \(\mathcal Z\) for normalizers, \(\mu\) (history measure) vs
   \(\mathrm{dvol}\) (volume element) kept separate per carry-over (ii); no
   restatement of the \((0,v,v,v)\) witness or `eq:Phi-eom` (carry-over (ii)
   made vacuous by avoidance).
7. **Splice**: 115-form `replace(anchor, payload + CRLF + anchor)` with
   leading CRLF separator in the payload (no trailing blank line) - per the
   post-116 author rule.

## Milestone assessment

Routine. No MILESTONE.md trigger: the package is a conditional construction
inside named hypotheses (H1)-(H3) for a Presentation-B probe measure; it does
not derive a critical-path step from the matrix theory. Candidate note (not a
claim): the 116 state-route consumable estimate is now *inhabited* (a measure
with the required property exists), which converts the D1 state route from
"no known object" to "object exists; its physical selection, truncation
removal and vev-level control are open" - a dependency relocation, not a
milestone.

## Status-label recommendation

Derived from the current agenda (ch17 L327-345, L650-656) and ledger (appH
Problem D): critical path A, B, C, D1, E, F, G-derived, N. Affected labels:
Problem D - OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL: **unchanged**; D1
**unchanged** OPEN; no priority or completion-label changes proposed anywhere
(no label edit in the payload beyond the two scoped status-preserving
sentences).

## Author decision needed

None.

## Remaining open step

To close the original target (frame non-degeneracy derived from the same
microscopic data, ch17 L339-342):
1. **Presentation-A selection of Eq. (eq:V)** (`sec:ch3-relate`) - upstream,
   gates any citation of this construction (unchanged).
2. **Physical measure**: show the matrix-theory state/measure (e.g. a
   large-N/eigenvalue ensemble or the real-time state after rotation) is, or
   is dominated by, a measure of the Gibbs class used here; the present
   measure is a probe construction.
3. **Truncation removal**: uniformity of \(C\), \(C_1=8C^4/\mathrm{Vol}\) and
   \(\mathcal Z\) bounds in \(K\) (or a projective/continuum limit).
4. **Wick rotation** (H2) and **background compactness** (H1) derived from
   Presentation-B data or replaced by hypotheses stated at the level of the
   matrix model.
5. **From null to pointwise**: `ass:nondeg` is pointwise; mean-field (vev)
   control \(\det\mathbb E_\mu[\Phi(x)]\neq0\) or an equivalent strengthened
   non-degeneracy statement is open (mixture obstruction recorded).
The transfer note to the upstream gating problem: the coercivity and
threshold chain of Sects. 1 and 4 use only Eq. (eq:V), so they transfer
verbatim if Presentation-A selects a different representative with the same
level-set geometry.

## Special instructions for the gatekeeper

- Scope limits: the payload must NOT be read as constructing a matrix-theory
  state or as discharging `ass:nondeg` or `ass:frame-lock`; the single closing
  sentence keeps D OPEN and PROGRAMME-CONDITIONAL. The null defect set is
  null, not empty, and is a configuration-level statement; do not let it be
  upgraded to a vev statement.
- Re-check by re-derivation (not by rerunning the pack alone): the coercivity
  constants 32 and 2 (completion to \((T-8v^2)^2\)); the upper bound
  \(\mathcal V\le(\lambda/4)|\Phi|_F^4+\lambda v^4\); the linearization
  constants \(8C^4/\mathrm{Vol}\) and \(16C^4\lambda v^4+\lambda v^4\);
  \(\sup_{s\ge0}se^{-s/2}=2/e\); the tube bound
  \(S_E\le\mathrm{Vol}[(\lambda/4)v^4(2+\rho)^4+\lambda v^4]\); the convexity
  (Holder) argument for \(\ln\mathcal Z\); and the absolute-continuity step
  (proper algebraic cone + identity direction; check explicitly that this is
  where (H3) is used, and that \(\omega_x\) may be supported on a proper
  subspace of matrix space - which is irrelevant to the cone nullity).
- Verify the Fubini step needs only smoothness of truncated fields.
- Payload hygiene: regenerate (`gen_payload_117.py`), rerun the byte scan, and
  re-run `cert-r117p.py` out of repo. Re-verify anchor and amendment-string
  uniqueness against the CURRENT tree before any integration; recompute POST
  if the tree moved.
- Rule audit points: payload numerals are (lambda/32, 2 lambda v^4, 8 C^4/Vol,
  16 C^4+1, 2/e, lambda v^4/4, 4) - all derived in-package or recorded 115/116
  constants; no citations anywhere; N6/N7 are probes, not genericity claims.
