# Proposal 124-n-mqm-pos, round 1

## Result

The hypotheses of the integrated spectral-positivity sublemma of Problem N
(appH, paragraph "Spectral positivity of the exact correlator.",
L3985-4021) are realized **as theorems in a named, explicitly defined
finite-N truncation class**: the homogeneous (spatially constant)
truncation of the Presentation-B microscopic action \eqref{eq:Smicro}
at \(A_\mu=0\), fixed flat background \(g^{(0)}=\eta\), finite internal
dimension \(N\), canonically quantized as matrix quantum mechanics on
\(L^2(\mathbb C^{N^2})\). In that class, for every finite \(N\): the
canonical Hamiltonian exists, is essentially self-adjoint, is bounded
below with \(H_{\rm F}\ge0\), has compact resolvent, pure point spectrum
and an \(L^2\)-normalizable ground-state eigenvector (no gap claimed);
the Kallen-Lehmann residue statement holds for **every** self-adjoint
observable of the model with any real-constant-coefficient projection
(residues at isolated simple real poles are sums of squared matrix
elements, hence \(\ge0\)); and the Euclidean measure realized as the
kernel of \(e^{-\tau H}\) is reflection-positive for time reflection
(pairing \(=\|e^{-(T/2)H}\widetilde{\mathcal F}\|^2\ge0\)). This is
strictly more than the signature-only content of Assumption
\ref{ass:lorentzian}. A companion bounded no-go shows the hypothesis
class is not vacuous and the sign convention is decisive: the canonical
classical-mechanics lift of the Presentation-A action \eqref{eq:Smatrix}
with kinetic metric \(\eta_{\mu\nu}\) has kinetic Hamiltonian polynomial
negative on an open set and a quartic form equal to
\(\tfrac14\sum_{ij}\|[\hat X^i,\hat X^j]\|^2-\tfrac12\sum_i\|[\hat X^0,\hat X^i]\|^2\)
that tends to \(-\infty\) on an explicit ray (\(-t^4/(4g_{\rm YM}^2)\)).
The package also **bounds the recorded E and D no-go statements from
above**: their failed measures are of the \(\eta_{\mu\nu}\)-contracted
Presentation-A family, so that failure is family-specific at finite N
and not a property of finite-N matrix measures at large. Nothing is
closed: the realization transfers to the manuscript's actual hypotheses
only through the unproved kinetic-sign direction of Assumption
\ref{ass:dictionary}, the undelivered composite \(T_{\mu\nu}\)
(Problem D), and removal of the homogeneous truncation. No status label
is touched.

## Target and status

- **Problem**: N ("Control of the effective expansion",
  `appH-microscopic-proofs.tex`, `\label{sec:status-N}`, L3870).
- **Current status, re-derived from the manuscript** (L3873-3875):
  "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label.
  Completion: PROGRAMME-CONDITIONAL." Section status line (L4130-4131):
  "Remains Assumption~\ref{ass:EFT-a2}." Problem N is in the current
  full-GR completion set (ch17-agenda, criterion includes N). Re-derived
  critical-path list from the ledger snapshot in the manuscript and
  `reports/ledger.md`: A, B, C, D1, E, F, G-derived, N; H, I, J optional.
  No discrepancy flagged.
- **Original target of the targeted gap** (verbatim, L4001-4012):
  "These hypotheses are not established in the present hypothesis class:
  a self-adjoint Hamiltonian bounded below with a normalizable ground
  state lies beyond the content of Assumption~\ref{ass:lorentzian},
  which fixes only the Lorentzian signature of the locked vacuum; the
  Euclidean measures of Section~\ref{sec:status-E} fail the positivity
  of [Osterwalder-Schrader] on the invariant polynomial algebra at
  finite \(N\), and the tree-level reflected form at the Euclidean flat
  point of Section~\ref{sec:status-D} is negative on the gauge-invariant
  translation probes; neither the fluctuation class nor \(T_{\mu\nu}\)
  is derived (Problem~D)."
- **Frontier edge**: N.mqm-pos (rank 18, untried), ledger 067 avenue (b):
  "finite-N matrix-quantum-mechanics Hamiltonian positivity beyond
  ass:lorentzian's signature-only content (untouched by E's OS-specific
  no-go) - most promising route to the R1 hypothesis class".
- **Classification of this package**: DERIVED **within the named class**;
  PROGRAMME-CONDITIONAL for Problem N: it does not discharge
  ass:EFT-a2 or ass:lorentzian, does not deliver \(T_{\mu\nu}\), and
  does not remove the truncation. It is a sub-lemma-grade advance: it
  converts the sublemma's hypothesis clause from "not established in
  the present hypothesis class" into "established in a named subclass,
  with the transfer gaps pinned to three recorded inputs".

## Source reading

digest + targeted reads. `scripts/make_digest.py` state noted; the tree
is permanently dirty so `--check` was not relied on (memory rule). Read
IN FULL: Problem N, appH L3870-4131; the E OS no-go paragraph L1781-1837;
the D reflected-form paragraphs L1677-1700; the anchor surroundings
L4023-4067; ch03 L100-262 (eq:Smatrix, eq:Smicro with the sign note
L233-237, eq:V); ch04 L319-332 (ass:lorentzian); `proposals/067-*`
proposal-r1 R1 section and review-r2 ranked relaxations; `reports/ledger.md`
067 entry; `frontier.yaml` N.mqm-pos. appH pin re-verified at every
script run: sha1 `ba72024aba4d26aff3fd5ad5a1219cdd5a1bd1e1`, 869275 B.
Unreadable files: none.

## Research and reasoning

**Setup.** Presentation B (ch03, eq:Smicro):
\(S_{\mathrm{micro}}=\int\mathrm d^4x\sqrt{-g^{(0)}}\,\mathrm{Tr}(-g^{(0)\mu\nu}(D_\mu\Phi)^\dagger D_\nu\Phi-V(\Phi^\dagger\Phi))\),
with the manuscript's own sign note (L233-237): "In the signature
\((-,+,+,+)\) of Chapter~2 the kinetic term is written with the minus
sign so that time derivatives have positive energy. This is a correction
to the Presentation-B action as stated; that the matrix action of
Presentation~A reproduces this sign is part of the unproved dictionary
(Assumption~\ref{ass:dictionary}) and remains to be derived." The
potential is the Mexican hat eq:V,
\(V=\frac\lambda4\mathrm{Tr}(\Phi^\dagger\Phi-v^2\mathbb I)^2\). The
class takes eq:Smicro as the definition (a named truncation of the
microscopic model), so the sign note is a boundary condition on the
class, not an input imported from Presentation A.

**P1 (established derivation). Canonical Hamiltonian.** Truncate
\(\Phi(\mathbf x,t)=M(t)\) (\(N\times N\) complex), \(A_\mu=0\),
\(g^{(0)}=\eta\), space of volume \(V_3\). The kinetic form is
\(\mathrm{Tr}\,\dot M^\dagger\dot M=\sum_{I,A}|\dot M_{IA}|^2\): the
field-space metric is flat and positive definite, so the Legendre
transform is invertible with no ordering ambiguity. Verified symbolically
(`verify_pos_124.py` A1, residual exactly 0):
\(H=V_3^{-1}\mathrm{Tr}\,\Pi\Pi^\dagger+V_3\frac\lambda4\mathrm{Tr}(M^\dagger M-v^2\mathbb I)^2\).

**P2 (established, standard self-adjoint operator theory). Positivity,
confinement, discreteness, ground state.** Writing \(A=M^\dagger M-v^2\mathbb I\)
(positive Hermitian), \(\mathrm{Tr}\,A^2=\sum_a(\sigma_a^2-v^2)^2\) over
the singular values \(\sigma_a\) of \(M\) (identity checked, A2a
residual 0): the potential is \(\ge0\), vanishes exactly at
\(\sigma_a\equiv v\), i.e. \(M=vU\), \(U\) unitary (compact zero set;
\(V(vU)=2.5\cdot10^{-32}\) numerically, \(V>0\) off the set: 0.144 on a
sample point). Cauchy-Schwarz on eigenvalues gives
\(N\,\mathrm{Tr}\,A^2\ge(\mathrm{Tr}\,A)^2\), i.e.
\(V\ge V_3\frac{\lambda}{4N}(\mathrm{Tr}\,M^\dagger M-Nv^2)^2\) (the
\(N=2\) sum-of-squares form
\(2\mathrm{Tr}A^2-(\mathrm{Tr}A)^2=(a_{11}-a_{22})^2+4|a_{12}|^2\)
checked with residual 0, A2b), so the potential is confining
(\(\to\infty\) as \(\|M\|\to\infty\); quartic ray growth \(t^4\) with
positive leading coefficient, A2c). Then, as a Schrödinger operator
\(-V_3^{-1}\Delta+\widetilde V\) on \(\mathbb R^{2N^2}\) with continuous
\(\widetilde V\ge0\): essential self-adjointness on
\(C_c^\infty(\mathbb R^{2N^2})\) and Friedrichs extension
\(H_{\rm F}\ge0\) (classical criterion: Schrödinger operators with
continuous potentials bounded below, e.g. the Glimm-Jaffe/Reed-Simon
theorem; named here, not re-proved); compact resolvent and pure point
spectrum \(E_n\to\infty\) with \(L^2\)-normalizable eigenfunctions
(Rellich compactness + confining tail). No gap above \(E_0\) is claimed
or needed by the sublemma. Numerical sanity at \(N=1\) (complex scalar,
box \([-8,8]^2\), \(180^2\) grid, A3): lowest eigenvalues
\(1.1516,\,2.6816\ (\times2),\dots>0\), increasing.

**P3 (established derivation). Kallen-Lehmann residues for every
self-adjoint observable.** With (P2), for any self-adjoint observable
\(\mathcal O\) of the truncated model,
\(\langle\Omega|\mathcal O(t)\mathcal O(0)|\Omega\rangle=\sum_ne^{-\mathrm i(E_n-E_0)t}|\langle\Omega|\mathcal O|n\rangle|^2\):
the spectral measure is a positive sum of point masses, so the residue
at every isolated simple real pole of any projection with real constant
coefficients (the class analogue of the spin-two projection: it
preserves self-adjointness) is a sum of squared matrix elements and so
\(\ge0\). Numerically (A3): \(\mathcal O=q_1\) and \(\mathcal O=q_1q_2\):
minimum residue \(3.7\cdot10^{-28}\ge0\) on 12 states, sum-rule fraction
\(\sum_nr_n/\langle\Omega|\mathcal O^2|\Omega\rangle=0.99998\); the
12-state spectral reconstruction of \(G(t)=\langle\Omega|\mathcal O(t)\mathcal O(0)|\Omega\rangle\)
at \(t=0.37\) agrees with direct \(e^{-itH}\) evolution
(expm_multiply) to \(1.13\cdot10^{-5}\) (independent method check).
This realizes the hypotheses of the sublemma (self-adjoint \(H\) bounded
below + normalizable ground state + self-adjoint rank-two-type
observable) in the class, and more: residue positivity for every
self-adjoint observable, not only for the derived \(T_{\mu\nu}\) the
manuscript does not yet have.

**P4 (derived corollary). Reflection positivity of the realized
Euclidean measure.** The Euclidean path-integral measure of the class
realized as the kernel of \(e^{-\tau H}\) satisfies OS reflection
positivity for \(\theta:\tau\mapsto-\tau\): the \(\theta\)-reflected
pairing of a functional equals
\(\|e^{-(T/2)H}\widetilde{\mathcal F}\|^2\ge0\) (standard; time-zero
representative \(\widetilde{\mathcal F}\), total Euclidean time
\(T>0\); self-adjointness and \(H\ge0\) suffice). Bottom of
\(e^{-TH}\) is \(e^{-TE_0}>0\) (A4: \(e^{-0.5\cdot1.1516}=0.562\)).
Contrast with the integrated E no-go (L1781-1837): its weights
\(\rho=c_{\rm P}(\det\tilde{\mathcal G})^4e^{-S_{\rm E}}\) (N=2, Pfaffian
content) and the bosonic \(e^{-S_{\rm E}}\times\)mass measures at every
finite \(N\) fail OS positivity on the invariant polynomial algebra, and
the D tree-level reflected form at the Euclidean flat point is negative
on the gauge-invariant translation probes (L1696). Both are measures of
the \(\eta_{\mu\nu}\)-contracted Presentation-A family; the P4 measure
is a different family (kernel of \(e^{-\tau H}\) for a
positive-definite-Hamiltonian quantum mechanics), so the recorded
failure is family-specific at finite \(N\).

**P5 (bounded no-go, companion; established derivation in its class).
Presentation-A lift fails.** Give eq:Smatrix (0-dimensional,
\(\eta_{\mu\nu}\)-contracted quartic, no time in the manuscript) the
canonical classical-mechanics lift to a fresh time \(\tau\) with
Hermitian \(\hat X^\mu(\tau)\) and kinetic metric \(\eta_{\mu\nu}\).
(i) Kinetic: the Hamiltonian kinetic polynomial
\(\sum_{\mu\nu}\eta^{\mu\nu}(-\mathrm{Tr}P^\mu P^\nu)\) evaluates to
\(-\mathrm{Tr}(P^0)^2<0\) at \(P^i=0\) (\(\eta^{00}=-1\)); quantumly its
quadratic form on \(e^{\mathrm i\lambda q_0}\chi\) states in the
\(\hat X^0\) fibre is \(-\lambda^2\|\chi\|^2+O(\lambda)\)
(`verify_nogo_124.py` B3). (ii) Potential: the quartic form equals
\(\tfrac14\sum_{ij}\|[\hat X^i,\hat X^j]\|^2-\tfrac12\sum_i\|[\hat X^0,\hat X^i]\|^2\)
with \(\|[\cdot,\cdot]\|^2=-\mathrm{Tr}[\cdot,\cdot]^2\ge0\) (symbolic
identity on traceless \(2\times2\) Hermitians, residual 0; both summands
\(\ge0\) on 300 random points, B1), which on the ray
\(\hat X^0=t\sigma_1/2,\ \hat X^1=t\sigma_2/2\) equals exactly
\(-t^4/4\) at \(g_{\rm YM}=1\) (\(-4\) at \(t=2\), B2), so it is
unbounded below; along the same ray the quartic dominates the cubic, so
the full Presentation-A potential tends to \(-\infty\). Hypothesis (i)
of the sublemma fails in this class for both kinetic and potential
reasons. This proves the class of the P1-P4 result is the sign-bearing
one and that the sign question the manuscript flags (ch03 L233-237,
ass:dictionary) is decisive, not cosmetic.

**Why this escapes the 067 bounded no-go and E's class (for the
gatekeeper).** The 067 no-go (integrated sublemma) assumes its
hypotheses conditionally and records that they are not established "in
the present hypothesis class"; it does not exclude their realization in
a new named subclass. This package supplies such a subclass with the
hypotheses proved (new mathematical objects: a different Hamiltonian, a
different measure family), which is the relaxation avenue (b) named in
the 067 review-r2 ranked list. E's no-go is a statement about
\(\eta\)-contracted Euclidean Presentation-A-family weights on the
invariant polynomial algebra at finite \(N\); the P4 measure is neither
of that family nor obtained by that reflection analysis, and P5 shows
the two classes really differ (positivity holds in one, fails in the
other for sign reasons). No existing no-go is restated in a wider
class; the deliverable is the positive realization (P1-P4).

**Transfer gaps (kept visible).** (1) The sign convention that makes
the kinetic term positive is the presentation-B convention; whether the
manuscript's fundamental Presentation-A action realizes it is the
unproved content of ass:dictionary quoted above, and P5 shows the
opposite convention is not harmless. (2) The sublemma's observable is
the composite fluctuation \(T_{\mu\nu}\), still undelivered (Problem D);
P3 covers every self-adjoint observable of the truncated model, but a
composite continuum \(T_{\mu\nu}\) needs the fluctuation class.
(3) The homogeneous truncation is an assumption of the class; the full
Position-space dynamics, the gauge coupling (\(A_\mu=0\)) and \(N\to\infty\)
are outside it. These three are exactly what the inserted text records.

## Claim classification

| claim | class |
|---|---|
| P1 canonical H, positive flat kinetic form, Legendre identity | established derivation (symbolic check A1) |
| potential = \((\lambda/4)\sum_a(\sigma_a^2-v^2)^2\ge0\), zero set \(M=vU\) compact, coercive bound | established derivation (A2a/A2b identities, Cauchy-Schwarz) |
| essential self-adjointness, \(H_{\rm F}\ge0\), compact resolvent, pure point spectrum, normalizable ground state, every finite \(N\) | established (standard SA theory applied to the named operator; criteria named, not re-proved) |
| KL residue positivity for every self-adjoint observable + real-constant-coefficient projection | established derivation from the spectral resolution (numeric confirmation A3) |
| OS reflection positivity of the \(e^{-\tau H}\)-kernel measure | established derivation (standard corollary of P2) |
| Presentation-A lift: kinetic polynomial negative on an open set; quartic \(-t^4/4\) ray; unbounded below | established derivation (B1-B3), bounded no-go in the named lift class |
| E/D failures are properties of the Presentation-A-family measures, not of finite-N matrix measures at large | conditional consequence: exact for the recorded weight classes (L1788-1796); "not generic" is a scope statement, not a theorem about all measures |
| transfer to the manuscript's hypotheses via ass:dictionary | unresolved microscopic step (assumption in the target's own terms) |
| \(T_{\mu\nu}\) as a derived composite | unresolved (Problem D) |
| removal of the homogeneous truncation / \(A_\mu\ne0\) / \(N\to\infty\) | unresolved |

No empirical inputs, no fits. All numbers are computed here (verifiers)
or quoted from the manuscript passages read.

## Proposed changes

One file: `chapters/appH-microscopic-proofs.tex`. One insertion, a single
new `\paragraph` between the sublemma paragraph and the completion-class
paragraph.

- Anchor (exact, occurs exactly once in the file, count 1 verified by
  `check_payload_124.py` against the live bytes):
  `\paragraph{The named completion class and the remainder bound.}`
  (L4023).
- Preceding kept text ends: "...located above the scale of the
  truncation." (L4020-4021; the sublemma paragraph, unchanged).
- Insertion point: immediately before the anchor; everything else in the
  file is kept byte-identical.
- Labels referenced by the insertion and verified to exist (exactly once
  as `\label`): `eq:Smicro`, `eq:V`, `eq:Smatrix` (ch03),
  `ass:lorentzian` (ch04), `ass:dictionary`, `ass:EFT-a2`,
  `sec:status-E`, `sec:status-D` (appH). The insertion adds no `\label`
  and no `\cite`, so no bibliography change is needed.
- Stale passages elsewhere: none. The insertion does not alter the
  sublemma's own sentence "These hypotheses are not established in the
  present hypothesis class", which stays true as written (the class of
  the present hypotheses being the full matrix dynamics); the new
  paragraph states explicitly that the realization is in a named
  subclass. If the gatekeeper prefers the two sentences to be read
  together, note that the new paragraph's first sentence says exactly
  which class is realized and its last sentence says what remains.

Payload bytes (`payload-124.txt`, sha1 `8988a8baf171cc510ed109618c25fa729f2fb5d2`,
5797 B, single ASCII line + CRLFCRLF; braces balanced; content verbatim):

```latex
\paragraph{Realization of the spectral-positivity hypotheses in homogeneous Presentation-B matrix quantum mechanics (derivations in a named truncation class; not closure).} The hypotheses of the sublemma of the paragraph ``Spectral positivity of the exact correlator'' are realized as theorems in the following named class. Class: Equation~\eqref{eq:Smicro} with \(A_\mu=0\), no couplings beyond Equations~\eqref{eq:Smicro} and~\eqref{eq:V}, fixed flat background \(g^{(0)}=\eta\) of Assumption~\ref{ass:lorentzian}, truncated to the spatially homogeneous mode \(\Phi(\mathbf x,t)=M(t)\) at finite internal dimension \(N\), and canonically quantized as matrix quantum mechanics on \(L^2(\mathbb C^{N^2})\) with the flat field-space measure. Derivations in the class. The kinetic form of the truncation is \(\operatorname{Tr}\dot M^\dagger\dot M=\sum_{I,A}|\dot M_{IA}|^2\): the field-space metric is flat, positive and finite-dimensional, so there is no ordering ambiguity, and the Legendre transform gives the canonical Hamiltonian \(H=V_3^{-1}\operatorname{Tr}\Pi\Pi^\dagger+V_3(\lambda/4)\operatorname{Tr}(M^\dagger M-v^2\mathbb I)^2\) with \(V_3\) the volume of space (checked symbolically). The potential equals \((\lambda/4)\sum_a(\sigma_a^2-v^2)^2\) in the singular values \(\sigma_a\) of \(M\) (identity checked symbolically), hence is non-negative, vanishes exactly on the compact set \(M=vU\) with \(U\) unitary, and dominates \(V_3(\lambda/4N)(\operatorname{Tr}M^\dagger M-Nv^2)^2\) by Cauchy--Schwarz on the eigenvalues, \(N\operatorname{Tr}A^2\ge(\operatorname{Tr}A)^2\) for Hermitian \(A\) (the \(N=2\) sum-of-squares form \(2\operatorname{Tr}A^2-(\operatorname{Tr}A)^2=(a_{11}-a_{22})^2+4|a_{12}|^2\) checked symbolically). Then, for every finite \(N\): (i)~\(H\) is the Schr\"odinger operator \(-V_3^{-1}\Delta+V_3(\lambda/4)\operatorname{Tr}(M^\dagger M-v^2\mathbb I)^2\) on \(\mathbb R^{2N^2}\): by the classical essential self-adjointness criterion for Schr\"odinger operators with continuous potentials bounded below it is essentially self-adjoint on \(C_c^\infty(\mathbb R^{2N^2})\), and its Friedrichs extension obeys \(H\ge0\); the potential is confining, so the Rellich compactness criterion gives compact resolvent, pure point spectrum \(E_n\to\infty\) with an orthonormal eigenbasis, and an \(L^2\)-normalizable ground-state eigenvector \(\Omega\); no gap above \(E_0\) is claimed or needed. (ii)~For every self-adjoint observable \(\mathcal O\) of the truncated model and every projection with real constant coefficients (the class analogue of the spin-two projection, which preserves self-adjointness), \(\langle\Omega|\mathcal O(t)\mathcal O(0)|\Omega\rangle=\sum_ne^{-\mathrm i(E_n-E_0)t}|\langle\Omega|\mathcal O|n\rangle|^2\) by the spectral resolution of (i): the spectral measure is a positive sum of point masses and the residue at each isolated simple real pole of the projected two-point function is a sum of squared matrix elements and so non-negative. This realizes the residue-positivity hypotheses of the sublemma above as theorems in the class for every self-adjoint observable, not only for a derived composite \(T_{\mu\nu}\). (iii)~The Euclidean measure of the class realized as the kernel of \(e^{-\tau H}\) is reflection-positive for the reflection \(\theta\) that negates Euclidean time about \(0\): the \(\theta\)-reflected pairing of any bounded measurable functional of the fields at times of one side equals \(\|e^{-(T/2)H}\widetilde{\mathcal F}\|^2\ge0\), in terms of the time-zero representative \(\widetilde{\mathcal F}\) and the time length \(T>0\), by self-adjointness and \(H\ge0\). Contrast, fixing the scope of the recorded no-go statements of Sections~\ref{sec:status-E} and~\ref{sec:status-D}. The weights failing reflection positivity there are of the Presentation-A family with \(\eta_{\mu\nu}\)-contracted field-space metric, so that failure is a property of that family at finite \(N\) and not of finite-\(N\) matrix measures at large; and the sign of the kinetic convention of Equation~\eqref{eq:Smicro} is decisive rather than cosmetic, since the canonical classical-mechanics lift of Equation~\eqref{eq:Smatrix} to a time \(\tau\) with Hermitian \(\hat X^\mu(\tau)\) and kinetic metric \(\eta_{\mu\nu}\) has Hamiltonian kinetic polynomial \(\sum_{\mu,\nu}\eta^{\mu\nu}(-\operatorname{Tr}P^\mu P^\nu)\), which evaluates to \(-\operatorname{Tr}(P^0)^2<0\) at \(P^i=0\) and whose quantum form is \(-\lambda^2\|\chi\|^2+O(\lambda)\) on states \(e^{\mathrm i\lambda q_0}\chi\) in a coordinate \(q_0\) of the \(\hat X^0\) fibre, while its quartic form equals \(\tfrac14\sum_{i,j}\|[\hat X^i,\hat X^j]\|^2-\tfrac12\sum_i\|[\hat X^0,\hat X^i]\|^2\) with \(\|[\,\cdot\,,\cdot\,]\|^2=-\operatorname{Tr}[\,\cdot\,,\cdot\,]^2\ge0\) (identity checked symbolically on traceless \(2\times2\) Hermitian matrices), which tends to \(-\infty\) on the ray \(\hat X^0=t\sigma_1/2\), \(\hat X^1=t\sigma_2/2\), where it equals \(-t^4/(4g_{\mathrm{YM}}^2)\): in that lift the sublemma hypotheses fail. Together the two halves pin the open content of the sublemma hypotheses to recorded inputs: the kinetic-sign content of Assumption~\ref{ass:dictionary} that Presentation~A reproduces the convention of Equation~\eqref{eq:Smicro}, the derivation of the composite fluctuation \(T_{\mu\nu}\) of Problem~D, and the restriction to the matrix-quantum-mechanics truncation class named here. These statements derive nothing about the emergent metric or the full dynamics, they do not discharge Assumption~\ref{ass:lorentzian} or Assumption~\ref{ass:EFT-a2}, they do not constrain the poles of the truncated kernels of this section (the two-oscillator artifact recorded above stands untouched), they change no status label, and Problems~F and~N remain open.
```

## Verification scripts

All in `proposals/124-n-mqm-pos/`; run with `python -I` from this folder;
each run is bounded (< 60 s except the optional cert reproduction).

1. `verify_pos_124.py` -> `verify_pos_124.out` (rc 0). P1-P4 checks.
   Reproduction pack - expected invariant outputs:
   - `A1 Legendre residual (expect 0): 0`
   - `A2a V - invariant form residual (expect 0): 0`
   - `A2b TrA2-SOS residual (expect 0): 0` (identity with coefficient 4)
   - `A2c t^4 coefficient min ... (expect > 0): 0.158...`
   - `A2c quartic-part ray ratios (expect 16, 16): [16. 16.]`
   - `A2c bound ... (expect >= 0): [nonneg, nonneg, nonneg]`
   - `A2d V(vU) (expect ~0): 2.5e-32   V(off zero set) (expect > 0): 0.144`
   - `A3 eigenvalues 0..7 (expect > 0, increasing)` starting 1.1516,
     `A3 KL ...: min r_n (expect >= 0) = 3.7e-28`,
     `sum r_n / <O^2> = 0.99998`,
     `A3 G(t=0.37) ... |diff| = 1.13e-05`
   - `A4 bottom of e^{-T H} ... (expect > 0): 0.562`
2. `verify_nogo_124.py` -> `verify_nogo_124.out` (rc 0). P5 checks:
   - `B1 identity residual (expect 0): 0`;
     `B1 min over 300 random points: A_sum >= 0, B_sum >= 0`
   - `B2 S on ray ... : -t**4/4` exact; `B2 value at t=2 (expect < 0): -4`
   - `B3 eta^{00} = -1`; leading quantum form `-lambda**2`
3. `make_payload_124.py` -> `make_payload_124.out` (rc 0). Regenerates
   `payload-124.txt` and prints PRE/PAY/POST sha1+size; every hygiene
   guard (ASCII, braces, no-label/cite, refs-exist, one-line, anchor
   count, join) has an injected positive control that must fire; the run
   prints "injected control fires" for each. Expected pins:
   PRE `ba72024aba4d26aff3fd5ad5a1219cdd5a1bd1e1`/869275,
   PAY `8988a8baf171cc510ed109618c25fa729f2fb5d2`/5797,
   POST `1d192b89bd2d20c50a4c70dfd108656a529baa4d`/875072.
   NOTE: writes only into the proposal folder and the given outdir; do
   not point outdir into the repository chapters/.
4. `check_payload_124.py` -> `check_payload_124.out` (rc 0, final line
   `ALL CHECKS PASS`). Independent re-verification (does not import the
   generator): payload pin, ASCII, CRLF-only, tail, brace balance, no
   `\label`/`\cite`, all `\ref`/`\eqref` targets exist in `chapters/`,
   anchor count 1, POST size = PRE+PAY and POST pin, join position.
5. Compile certificate: `cert-summary-124.txt` (spliced file built in a
   fresh tree OUTSIDE the repository; five pdflatex passes + bibtex, all
   rc 0; final pass: 0 undefined references, 0 undefined citations, 0
   multiply-defined, 0 LaTeX Warnings, 448 pages). Reproduction: copy
   `namcg-book7.tex`, `chapters/`, `frontmatter/`, `bib/`, `figs/` to an
   external directory, replace `chapters/appH-microscopic-proofs.tex`
   with `spliced_appH_124.bin` (sha1 1d192b89bd2d20c50a4c70dfd108656a529baa4d, reproducible from
   make_payload_124.py), run `pdflatex; bibtex namcg-book7; pdflatex;
   pdflatex` (nonstopmode).

## Decisions Taken

- **Route (within Presentation B vs modifying the core)**: chose the
  homogeneous Presentation-B MQM class - the only sign-convention
  positive presentation already in the manuscript (its sign note makes
  the positivity condition explicit). Rejected: attempting Presentation
  A positivity directly (P5 shows it fails for sign reasons, so the
  package contains that outcome as the companion no-go instead);
  introducing new field content or a regulator (changes no hypothesis
  of the sublemma that matters and would add unsupported inputs).
- **Gap vs closure framing**: recorded as a class-restricted realization
  with the three transfer gaps pinned, rather than claiming the
  sublemma's hypotheses are "established"; the manuscript sentence at
  L4001 is left untouched to avoid a scope-closure reading.
- **Insertion point**: after the sublemma paragraph (immediately before
  the named-completion-class paragraph) rather than inside E or D,
  because the hypotheses quoted are N's and the contrast references
  point back to E/D.
- **Non-ASCII payload characters**: none (Schroedinger written
  `Schr\\\"odinger`); the ascii guard control corrupts with `chr(233)`
  at runtime instead of embedding a non-ASCII byte in the generator.
- **bibtex base name**: first cert attempt passed the wrong base
  (`namcg` instead of `namcg-book7`), a no-op; reran as
  `bibtex namcg-book7` with rc 0; both recorded in the cert summary.

## Milestone assessment

Routine package (no milestone trigger). Candidate description: an
important sub-lemma-level advance for Problem N - the R1 hypothesis
clause gains a positive realization in a named class plus a bounded
companion no-go - but no critical-path step of Problem N (no-ghost for
\(p<\LUV\) from the matrix path integral) is closed and no missing link
is closed without inputs (ass:dictionary sign, \(T_{\mu\nu}\), and the
truncation all remain).

## Status-label recommendation

Re-derived current critical-path list (appH L3873-3875 + ch17 full-GR
criterion + ledger): A, B, C, D1, E, F, G-derived, N - all OPEN /
CRITICAL PATH, PROGRAMME-CONDITIONAL as recorded. This package changes
no label and proposes no label change: Problem N remains OPEN /
CRITICAL PATH / PROGRAMME-CONDITIONAL; E and D unchanged (the scope
note about their measure families is not a status change and the
payload changes no status text).

## Author decision needed

None. (All choices taken were route/presentation choices that change no
status, priority, completion label, Chapter 17 scope, critical-path set
or core assumption.)

## Remaining open step

To close the original target (residue positivity for the actual
hypothesis class of Problem N, beyond the named truncation):
1. derive, from Presentation A itself, the kinetic-sign content of
   ass:dictionary (or extend the class definition so the microscopic
   dynamics is Presentation B - a core change, out of scope here);
   P5 shows why this sign is load-bearing;
2. deliver the composite fluctuation \(T_{\mu\nu}\) and its rank-two
   projection as an operator of the class (Problem D input);
3. remove the homogeneous truncation: inhomogeneous modes, \(A_\mu\ne0\),
   and control of the \(N\to\infty\) limit; and
4. connect the class ground state \(\Omega\) to the locked vacuum whose
   signature ass:lorentzian postulates.
Each is stated in the inserted text as an open item; none is claimed.

## Special instructions for the gatekeeper

- Scope limits: verify (a) the Legendre/self-adjointness/confinement
  claims for the named operator at general finite \(N\) (the criteria
  are standard; the derivation obligation is that the operator fits the
  criteria - nonnegative continuous confining potential - which A2
  checks), (b) the KL identity and the OS pairing identity, (c) the P5
  identities B1-B3, (d) anchor uniqueness and that nothing else in the
  file changes, (e) the payload compiles (cert-summary-124.txt; rerun
  the external-tree build if in doubt).
- What must NOT be asserted about this text: that the sublemma's
  hypotheses are established for the manuscript's actual matrix
  dynamics; that the E/D no-gos are wrong (only their scope is
  bounded); that any status changes; that the two-oscillator artifact
  or the completion-class paragraph is affected; that \(T_{\mu\nu}\),
  ass:lorentzian, ass:EFT-a2 or ass:dictionary are discharged.
- Re-check especially: the phrase "the Presentation-A family with
  \(\eta_{\mu\nu}\)-contracted field-space metric" as a description of
  the E weights at L1788-1796 and the D reflected-form setup at
  L1688-1696 (the claim is membership of those recorded classes, plus
  non-membership of the P4 class); the ray value \(-t^4/(4g_{\rm YM}^2)\)
  (verifier used \(g_{\rm YM}=1\), restoring \(g_{\rm YM}\) is by the
  overall \(1/g_{\rm YM}^2\) prefactor of eq:Smatrix - confirm against
  ch03 L142-157); and that "real constant coefficients" suffices for
  the projection to preserve self-adjointness in the class.
- The 067 review-r2 ranked relaxation list, avenue (b), is the dispatched
  route; confirm the package answers avenue (b) and not a restatement
  of the merged 067 conditional text.
