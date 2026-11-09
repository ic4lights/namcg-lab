# Proposal 061-g-sent-replica-obstruction-and-cut-benchmark, round 1

## Result
Two connected results for Problem G (HBEV), sharing one set of premises (quadratic
fluctuations about a constant-Theta background of the Presentation-A action):

1. **Bounded definitional no-go (G-R4).** The replica construction of the entropy
density of Assumption ass:Sent-density (eq:replica: Tr rho_D^n as a path integral on
an n-sheeted cover branched over the edge of partial M) is **undefined on
Presentation-A data alone**: the matrix data (regularized trace with cutoff
eq:LUV-def, noncommutative coordinates eq:NC) supply no manifold M, no hypersurface
partial M, no tubular neighbourhood, no branched cover and no region factorization of
the trace. The hypothesis class of the no-go is exactly: Presentation-A data without
the dictionary of ass:dictionary and without any supplied background geometry. Two
exits are named: (i) a Presentation-A **spectral cut** (spectral projections of the
coordinate operators; Tr rho_D^n defined by Fock factorization over the restricted
one-particle space for quadratic fluctuations) — the output is a functional of the
quadratic kernel and the cut projector, not a cover path integral and not a
diffeomorphism scalar, and reducing it to eq:Sent-exp requires an undrawn
dictionary-type identification of cut with partial M; (ii) Presentation B with the
dictionary, in which case any G-derived use of eq:Sent-exp in eq:Leff inherits
ass:dictionary and cannot discharge the matrix-derived criterion while that assumption
is retained. Consequence: the matrix-derived route through ass:Sent-density depends
on Problem A; the attack-plan entry "G.ent depends_on: []" is dependency drift
(report-only; nothing changed).

2. **Form mismatch (G-R3, folded in).** A sharp spectral cut of a quadratic kernel
gives a strict area law S = sigma Lambda_UV^2 A_cut (dimension 2); the dim-3 density
form alpha_0 Lambda_UV^3 of eq:Sent-exp is recovered from it only for a tube of width
w = Theta^{1/2} = Lambda_UV^{-1} (eq:LUV-def convention) — the localization scale of
ass:Sent-density is forced by the cut rather than derived — and the thin-tube limit
w -> 0 diverges as sigma Lambda_UV^2 / w (verified symbolically: alpha_0 =
sigma/(Lambda w); continuum_check.py (iv)).

3. **Free benchmark sub-lemma (G-R1, conditional).** In the free constant-Theta
(Moyal) sector of eq:Smatrix (cubic C-term and matter dropped) each transverse mode
p_perp reduces to a 1D half-line problem cut by the spectrum of one coordinate
operator; with restricted symplectic spectrum nu_k >= 1/2 of D^{1/2} C D^{1/2},
S_cut = sum_k[(nu+1/2)ln(nu+1/2)-(nu-1/2)ln(nu-1/2)]. Numerics (halfline_ee.py):
massless half line s_1(N) = (1/6)ln N + 0.2315(3) (slope fit 0.166626 vs 1/6;
ln 2/3 = 0.231049 is the closest closed-form candidate, the converged value is
0.23152(5)); massive mode s_1(mu) <~ (pi/2)e^{-mu} (ratio 0.98 at mu = 2.5); slab
coefficient sigma = (2pi)^{-2} int_BZ^2 d^2p_perp s_1(mu(p_perp)) = 0.0096 +- 0.0003
(fitted-grid 0.009591; direct 64^2 + tail 0.009590). With w = Theta^{1/2},
alpha_0^free = sigma. alpha_1, alpha_2 NOT computed. Decoupled-kernel zero-entropy
identity verified (continuum_check.py (iii)): a kernel not coupling across the cut
contributes nu_k = 1/2 and no entropy.

Nothing is closed. Problem G stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## Target and status
- Problem G, appH-microscopic-proofs.tex L2823-2842 (sec:status-G): "Status: OPEN.
Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL." Status paragraph (L2837-
2842): mechanism CLOSED CONDITIONALLY under the stated boundary entropy; derivation
of the infrared entropy density and stationarity from the matrix theory OPEN. This is
the only critical-path entry without a \paragraph{Missing step.} (scout discrepancy 1;
ledger audit item "G-gap not restated in appH"). No \paragraph{Missing step.} exists
in the current bytes — verified (anchor_check.out).
- ch17-agenda.tex: Problem G passage L474-495 (G completion levels); completion
criterion item 7 L723-726 requires deriving the ass:Sent-density entropy density and
ass:bdy-EE stationarity from the matrix theory, with Lambda_eff then following from
eq:Leff; chains resting on ass:dictionary do not qualify (L696-698).
- Dependencies: Problem A (emergent-smooth-spacetime existence) is a genuine
dependency of the matrix-derived route through ass:Sent-density (this proposal's
no-go); the attack plan's "G.ent depends_on: []" conflicts with eq:Leff containing
\Geff and ch12 L64-69 (Problem F matched G_eff) — report-only.
- Classification of this package: **conditional sub-lemma + bounded no-go + missing-
step record**; DERIVED part: only the free-theory benchmark numbers within their
stated truncation. PROGRAMME-CONDITIONAL overall.

## Source reading
digest + targeted reads (digest CURRENT; dirty-chapters: yes — the uncommitted appH
diff is proposal 060's Problem-E material, unrelated to G). Read IN FULL:
chapters/ch12-hbev.tex (400 lines; ass:Sent-density L138-156/eq:Sent-exp L147,
ass:bdy-EE L184-193/eq:bdy-EE L190, thm:Leff/eq:Leff L202-225, Dimensional-status
remark L243-265, matched-G_eff passage L64-69, boundary-geometry opening L74-104);
appH Problem G L2760-2854 (current bytes, incl. L2815-2860 repr dump in
anchor_check.out); ch17-agenda.tex L474-495 and L690-749; ch06-entanglement-
equilibrium.tex L115-259 (def:rhoD L125-133 incl. Presentation-A region algebra =
"spectral projections of Xhat^mu whose eigenvalues lie in D, after the dictionary",
eq:replica L176-181 with the Presentation-A concession L196-198/202-205);
ch03-matrix-action.tex L100-229 (eq:NC L106, eq:LUV-def L119, eq:Smatrix L143) and
L330-370 (ass:dictionary L346); ch09-ultraviolet.tex L140-183 (Presentation-A
"regularized trace over H with cutoff eq:LUV-def"); reports/sme-scout-20261109-0002.md
IN FULL; reports/ledger.md audit list; proposals/052-060 for deliverable style and the
060 F1 single-pass-splice lesson. No unreadable files.

## Research and reasoning
(P1) Presentation-A data are a 0-dimensional regularized trace over H with cutoff
eq:LUV-def on coordinates obeying eq:NC ([Xhat^mu,Xhat^nu]=i Theta^{mu nu}, c-number;
ch03: "the notion of a sharply localized event is meaningless below LUV^{-1}. This is
the NAMCG replacement for a hard lattice."). Every geometric input of eq:replica (M,
partial M, tube, n-sheeted cover branched over B, Tr over a region algebra) is absent
from these data; ch06 itself concedes the replica construction "requires the
dictionary of Assumption ass:dictionary" in Presentation A (L196-198, L202-205), and
def:rhoD's Presentation-A algebra is defined "after the dictionary of ass:dictionary".
This is the bounded obstruction: it is definitional, holds for ALL states/measures of
the Presentation-A theory, and its only escape hypotheses are (a) an added dictionary-
type identification (which is ass:dictionary, i.e. smuggles geometry — H5), or (b) a
non-geometric partition. Literature cross-check (verified this session): Anous-
Karczmarek-Mintun-van Raamsdonk-Way, arXiv:1911.11145 (SciPost 8, 057 (2020)): BFSS
has no factorized Hilbert space over spatial regions; region entropies must be "more
general than the usual subsystem entanglement entropies". This supports the
non-factorization statement in a neighbouring matrix model; it is NOT imported as a
NAMCG result.
(P2) Exit (i) spectral cut: the single operator Xhat^3 has a PV spectral measure even
without a manifold; for quadratic fluctuations the ground state is a real Gaussian
functional (zero X-P covariance correlations), the one-particle space splits by
transverse momentum into 1D problems, and Tr rho_D^n is defined by the standard
quasi-free formula through the restricted symplectic spectrum nu_k of D^{1/2} C D^{1/2}
(nu_k >= 1/2 by Heisenberg), with the entropy functional
s(nu) = (nu+1/2)ln(nu+1/2)-(nu-1/2)ln(nu-1/2). This defines a number from matrix data
(kernel + cut projector) alone — no cover, no geometry — hence the object is NOT a
diffeomorphism scalar and is NOT equal to eq:Sent-exp's local density without the
identification of the cut with partial M, which is exactly what must be derived.
(P3) Computation (halfline_ee.py): lattice units a=1, Lambda_UV = pi (Theta^{1/2}=a
up to O(1)); per p_perp a 1D chain with omega(p) = sqrt(mu^2 + 4 sin^2(p/2)); C_ij,
D_ij from iDFT of 1/(2 omega) and omega/2 (massless zero-mode: fC(0)=0; the 1/omega
divergence is r-independent, the matrix piece is proportional to 11^T, and
1^T D 1 = Dhat(0) = 0, so it cannot enter nu — standard massless treatment).
Checks: (1) massless s1(N)-(1/6)lnN = 0.236180, 0.232219, 0.231679, 0.231555,
0.231524 at N=256..8192; fitted slope (s1(8192)-s1(4096))/ln2 = 0.166626 vs 1/6 =
0.166667; ln2/3 = 0.231049 is NOT the observed limit (0.23152(5)). The 1/6 slope is
the established c=1 half-line value (CFT) — used only as a check that the numerics
reproduce a known result, not as an input. (2) s1(mu)/(pi/2 e^{-mu}) = 0.8779,
0.9334, 0.9614, 0.9775 at mu=1,1.5,2,2.5. (3) s1 = (1/(6pi))ln(1/mu) + b with b
drifting slowly: 0.2383 (mu=.3) ... 0.1896 (mu=.001); fitted b = 0.1979 at mu=.01.
NOTE: the script also prints a hand-derived continuum reference
c0_ref = ln2/3 - 9/(16pi) + ln(4/pi)/(6pi) = 0.144345 which does NOT match the
numerics; it is kept in the output for transparency but is NOT quoted and is
suspected erroneous (derivation not re-checked). (4) sigma: fitted-asymptotics 512^2
grid: 0.009591; direct s1 on 64^2 offset grid for mu >= 0.05 (0.009240) + analytic
tail (0.000350) = 0.009590; naive continuum reference 1/(48pi^2)+(ln2-9/16)/(2pi) =
0.008398 is an order-of-magnitude comparison only (misses the lattice b constant).
Quoted: sigma = 0.0096 +- 0.0003.
(P4) Continuum cross-checks (continuum_check.py): (i) the continuum x-x correlator is
C(r) = int dp/(2pi) e^{ipr}/(2 sqrt(p^2+mu^2)) = K0(mu r)/(2pi) (verified numerically
via the once-integrated-by-parts, absolutely convergent form; agreement 1e-3; short-
distance log C(r) + (1/2pi)(ln(mu r/2)+gamma) -> 0 to 1.6e-7). (Note: an earlier draft
of this script misstated the identity with K1/(4pi); the shipped version has the
correct K0/(2pi) — corrected before delivery.) (ii) D(r) = -C'' + mu^2 C =
-mu K1(mu r)/(2 pi r) < 0 for r>0 (symbolic, sympy). (iii) decoupled two-mode kernel
=> CD = (1/4)I => nu={1/2,1/2} => zero cut entropy (established finite-dimensional
identity). (iv) alpha_0 = sigma/(Lambda w); alpha_0 = sigma iff w = 1/Lambda.
(Hazards respected) H1: no heat-kernel/cone/Solodukhin/LM apparatus anywhere; the
half-line correlator method is used. H2: no assumed area law, no 1/(4G_eff) prefactor
imported; sigma is computed. H3: no G_eff on the entropy side. H4: no HDE/CKN use.
H5: the free benchmark is explicitly a quadratic (conditional) truncation of
eq:Smatrix; the no-go covers Presentation-A data without a dictionary.

## Claim classification
- Bounded obstruction (undefinedness of eq:replica on Presentation-A data without
dictionary): **established (definitional analysis of the manuscript's own data and
concessions)**; the two-exit trichotomy is a conditional structural statement.
- Non-factorization of region algebras in matrix models (BFSS): **established in the
literature** (Anous2020, verified); transfer to NAMCG: not imported, only "same
structural situation".
- Spectral-cut definition of Tr rho_D^n for quadratic fluctuations: **established
identity (quasi-free Fock theory) conditional on** the quadratic truncation and the
choice of cut projector.
- Area law S = sigma Lambda^2 A_cut for the sharp cut: **conditional** (quadratic
free theory, lattice-regularized).
- s_1(N) = (1/6)lnN + 0.2315(3): **numerical** (high precision; slope agrees with the
established c=1 value).
- s_1(mu) <~ (pi/2)e^{-mu}; sigma = 0.0096 +- 0.0003; alpha_0^free = sigma at
w = Theta^{1/2}: **numerical/conditional** (quadratic truncation, convention
Lambda_UV = Theta^{-1/2}).
- alpha_1, alpha_2 coefficients: **unresolved** (not computed).
- G-R3 form mismatch and forced tube width w = Theta^{1/2}: **established
dimensional bookkeeping** + **conditional** identification with the cut.
- Dependency of G-derived-via-ass:Sent-density on Problem A: **conditional** (follows
from the no-go plus the two exits).
- c0_ref = 0.144345: **unresolved/suspected erroneous** — not used.
- Anous2020 record: **verified** (arXiv:1911.11145; SciPost Phys. 8, 057 (2020)).
HHL 2012.15683/2105.13726, Han-Hartnoll 1906.08781: **not independently verified by
me this session** (scout-verified only) — NOT cited in manuscript text.

## Proposed changes
Single file: `chapters/appH-microscopic-proofs.tex`. One insertion: the three-paragraph
block below, placed after the Status paragraph of Problem G (ends
"scope-limited model.") and before `\section{Problem H: ...}`. Nothing is removed or
replaced; all existing G text is kept. A second proposed insert is folded in: the
\paragraph{Missing step.} (third paragraph of the block) closes the scout/ledger audit
item that Problem G is the only critical-path entry without a Missing-step paragraph
(verified: no such paragraph exists in the current bytes).

Verified labels used: ass:Sent-density (ch12:139), eq:Sent-exp (ch12:147),
ass:bdy-EE (ch12:185), eq:bdy-EE (ch12:190), eq:Leff (ch12:215), ch:hbev (ch12:2),
ass:dictionary (ch03:346), eq:LUV-def (ch03:119), eq:Smatrix (ch03:143), eq:NC
(ch03:106), sec:ch6-replica (ch06:176), eq:replica (ch06:181), def:rhoD (ch06:133).
No new labels are introduced; no duplicate-label risk. \Tr is defined
(namcg-book7.tex:104). New citation key: Anous2020 (NOT in bib/namcg.bib today —
verified by grep; full BibTeX below; the integrator adds it only if the gatekeeper
accepts; until then the build_check will flag an undefined citation — expected).

BibTeX (record verified this session at arXiv:1911.11145 and the SciPost DOI):
```bibtex
@article{Anous2020,
  author  = {Anous, Tatsuma and Karczmarek, Katherine and Mintun, James and
             van Raamsdonk, Mark and Way, Christopher},
  title   = {{Areas and entropies in BFSS/gravity duality}},
  journal = {SciPost Phys.},
  volume  = {8},
  pages   = {057},
  year    = {2020},
  doi     = {10.21468/SciPostPhys.8.4.057},
  eprint  = {1911.11145},
  archivePrefix = {arXiv},
  primaryClass  = {hep-th}
}
```

Insert file: `proposals/061-g-sent-replica-obstruction-and-cut-benchmark/insert-r1.tex`
(LF-stored; converted to CRLF by the apply rule). Fenced block (verbatim, LF):

```latex
\paragraph{Bounded obstruction: the replica density on Presentation-A data.}
The entropy density of Assumption~\ref{ass:Sent-density} is evaluated in
Section~\ref{sec:ch6-replica} through the replica formula~\eqref{eq:replica}:
\(\Tr\rho_D^n\) as a path integral on an \(n\)-sheeted cover of \(M\) branched
over the edge \(B\) of \(\partial M\). Restricted to Presentation~A, the
regularized trace over \(\mathcal H\) with cutoff~\eqref{eq:LUV-def} and matrix
coordinates~\eqref{eq:NC}, this object is undefined: the data supply neither a
manifold \(M\), nor a hypersurface \(\partial M\), nor a tubular neighbourhood,
nor a branched cover, nor a factorization of the trace over a region. The
boundary \(\partial M\) of the emergent spacetime is available only through the
infrared dictionary of Assumption~\ref{ass:dictionary}; the non-factorization
of region algebras in matrix models is established independently in the BFSS
setting in~\cite{Anous2020}. Two exits remain. (i) A Presentation-A cut:
spectral projections of the coordinate operators (Definition~\ref{def:rhoD})
define a one-particle cut, and for quadratic fluctuations \(\Tr\rho_D^n\) is
defined by Fock factorization over the restricted one-particle space; the
output is a functional of the quadratic kernel of the action and of the cut
projector, not a cover path integral and not a diffeomorphism scalar, and
reducing it to the local form~\eqref{eq:Sent-exp} requires a dictionary-type
identification of the cut with \(\partial M\), which is not derived.
(ii) Presentation~B with the dictionary, in which case any use of
\eqref{eq:Sent-exp} in \eqref{eq:Leff} inherits Assumption~\ref{ass:dictionary}
and cannot discharge the matrix-derived completion criterion while that
assumption is retained. The matrix-derived route through
Assumption~\ref{ass:Sent-density} therefore depends on Problem~A, and a
derivation chain recorded without this dependency is incomplete. A sharp
spectral cut of a quadratic kernel gives a strict area law
\(S=\sigma\Lambda_{\mathrm{UV}}^2 A_{\mathrm{cut}}\) of mass dimension two;
the density form \(\alpha_0\Lambda_{\mathrm{UV}}^3\) of \eqref{eq:Sent-exp} is
recovered from it only for a tube of width \(w=\Theta^{1/2}=\Lambda_{\mathrm{UV}}^{-1}\)
in the convention of \eqref{eq:LUV-def}, so the localization scale of
Assumption~\ref{ass:Sent-density} is forced by the cut rather than derived, and
in the thin-tube limit \(w\to0\) the density diverges as
\(\sigma\Lambda_{\mathrm{UV}}^2/w\).

\paragraph{Free benchmark in the constant-\(\Theta\) sector.}
For quadratic fluctuations about a constant \(\Theta\) background, with the
cubic term and the matter action in \eqref{eq:Smatrix} dropped, each transverse
Fourier mode \(p_\perp\) gives a one-dimensional half-line problem cut by the
spectrum of one coordinate operator. The ground-state covariance \((C,D)\) of
each one-dimensional problem, restricted to the half-line, has a restricted
symplectic spectrum \(\nu_k\ge\tfrac12\) (a kernel that does not couple across
the cut contributes only \(\nu_k=\tfrac12\) and no entropy), and
\(S_{\mathrm{cut}}=\sum_k[(\nu_k+\tfrac12)\ln(\nu_k+\tfrac12)-(\nu_k-\tfrac12)\ln(\nu_k-\tfrac12)]\).
Numerically, in lattice units with \(\Lambda_{\mathrm{UV}}=\pi\): the massless
half-line entropy obeys \(s_1(N)=\tfrac16\ln N+0.2315(3)\), the coefficient
\(\tfrac16\) agreeing with the central-charge value for one free massless
field; a mode of mass \(\mu\) contributes \(s_1(\mu)\lesssim\tfrac\pi2 e^{-\mu}\);
and the slab coefficient
\(\sigma=(2\pi)^{-2}\int_{\mathrm{BZ}^2}d^2p_\perp\,s_1(\mu(p_\perp))\)
evaluates to \(\sigma=0.0096\pm0.0003\). With \(w=\Theta^{1/2}\) this fixes
\(\alpha_0\) in \eqref{eq:Sent-exp} to \(\sigma\) at the free level;
\(\alpha_1\) and \(\alpha_2\) are not computed. These are conditional
benchmark values in a quadratic truncation of \eqref{eq:Smatrix}; they do not
derive Assumption~\ref{ass:Sent-density}, and Problem~G remains open.

\paragraph{Missing step.}
Closing the matrix-derived criterion for Problem~G requires, beyond the
present note: (i) a derivation, not a retained dictionary, of the
identification between a Presentation-A boundary cut and \(\partial M\) under
which the cut entropy becomes the local density \eqref{eq:Sent-exp}; (ii) the
interacting condensate sector of \eqref{eq:Smatrix}, the cubic term, matter
and non-Gaussian ground-state correlations, which carry the \(\alpha_1\) and
\(\alpha_2\) structures; (iii) a derivation of the stationarity
condition~\eqref{eq:bdy-EE} of Assumption~\ref{ass:bdy-EE}; and (iv) the
mass-dimension-one boundary-to-bulk conversion recorded in the dimensional
status remark of Chapter~\ref{ch:hbev}, without which \eqref{eq:Leff} stays
schematic.
```

**APPLY RULE (byte-exact, single-pass, ascending, exactly one splice)** — against
the CURRENT working-tree bytes of `chapters/appH-microscopic-proofs.tex`
(size 560743, sha256 fe02de8970b7dee8b0df8cad9a84ca557b1ecf41bc9d2b4984135a50b8faab8d,
CRLF 3326, bare LF 0 — re-verified in anchor_check.out):
- anchor A1 = `b'scope-limited model.'` must occur exactly once, at offset 540076
  (verified);
- bytes [540096:540100] must equal `b'\r\n\r\n'`;
- at offset 540100 the line `b'\section{Problem H: modular origin of the interpolating function}'`
  must begin and occur exactly once (verified: the shorter string
  `b'\section{Problem H}'` occurs 0 times — the full header is required);
- insertion offset X = 540100;
- insert = bytes of `insert-r1.tex`, which must contain no carriage return;
  right-strip trailing LF, convert every LF to CRLF, re-terminate with `b'\r\n\r\n'`;
  resulting insert: 4804 bytes, sha256 c0157f9184e3789c3599797f89ee7b9fbbbe27a84c947b478b8ff4fb19665f2d;
- result = appH[:X] + insert + appH[X:];
- predicted post-state: size 565547, CRLF 3395, bare LF 0,
  sha256 610963e24a0d0ca72297320313d3ebfa8433519143e432a1b33b693da3d1b7a8.

Stale passages / report-only items (nothing changed by me):
1. Attack plan `reports/graph/attack-plan.yaml` "G.ent depends_on: []": contradicts
the P1/P4 dependency finding and eq:Leff's \Geff content + ch12 L64-69; F.coeff
should precede G.2. Reports-only (I cannot edit reports/).
2. appH L2832 hard-codes "Chapter~12" — pre-existing text, convention violation
flagged for the integrator's awareness; NOT touched here.
3. ch17 L474-495 and the ledger correctly keep G OPEN; no inconsistency with this
insert. No stale G passage asserts a matrix derivation of ass:Sent-density.

## Verification scripts
All under `proposals/061-g-sent-replica-obstruction-and-cut-benchmark/`, run with
`python -I`; outputs saved:
- `halfline_ee.py` / `halfline_ee.out` — checks (1)-(4) above; symplectic-spectrum
entropy of the half-line restriction (FFT Toeplitz correlators, eigh/eigvalsh),
massless slope and constant, large-mu decay, small-mu log, sigma by two independent
quadrature routes.
- `continuum_check.py` / `continuum_check.out` — continuum correlator identity
C(r)=K0(mu r)/(2pi) (numerical, IBP form), short-distance log, D(r)=-C''+mu^2 C =
-mu K1(mu r)/(2 pi r) (symbolic), decoupled zero-entropy identity, tube-width
dimensional solve alpha_0 = sigma/(Lambda w).
- `anchor_check.out` — appH byte size/sha256/CRLF/bare-LF, anchor counts and offsets,
repr dump of lines 2815-2860.
- `simulate_apply.py` / `simulate_apply.out` — byte-exact splice simulation and
predicted post-state (does not write outside the folder).

## Decisions Taken
- Package G-R4 + G-R3 (folded) + G-R1 in ONE proposal (shared premises: quadratic
constant-Theta truncation and the spectral-cut definition), per the scout
recommendation and the batching rule; G-R2 rejected (relative-entropy route: premise
smuggling, H5 — its hypothesis does the work).
- Route for G-R1: direct 1D half-line correlator/symplectic-spectrum computation on
the Moyal sector (avoids H1 apparatus entirely); rejected alternatives: link-variable
factorization (HHL) — not computed, would need gauge-invariant edge-mode bookkeeping
beyond one cycle; eigenvalue-cut of the full fuzzy background — harder, same status.
- Citation policy: cite ONLY Anous2020 (verified by me). CLPW 2206.10780 NOT cited
(scout did not fetch it); the scout's not-verified list kept out of text.
- Missing-step paragraph included as the third paragraph of the same block (report-
style audit item closed inside the same insert; keeps one contiguous block, one
closing scoped status sentence lives at the end of paragraph 2; the Missing-step
paragraph is a ledger list, matching the style of other problems' Missing-step
paragraphs).
- Convention for alpha_0 = sigma: state w = Theta^{1/2}, Lambda_UV = Theta^{-1/2}
(eq:LUV-def); lattice units Lambda = pi for the numerics. The mismatched hand-derived
constant c0_ref is quarantined (printed, not quoted).
- No status-label change; no scope change; nothing asserted beyond the classification.

## Milestone assessment
Routine. No MILESTONE.md trigger: no critical-path step is derived or closed. The
value is a bounded obstruction (which constrains every future G route to a non-
geometric partition or an explicit derivation of the cut-partialM identification),
the first Missing-step record for G, and a computed free-theory benchmark coefficient
alpha_0^free = sigma ~= 0.0096 for the leading density term.

## Status-label recommendation
Re-derived from ch17 (criterion items incl. item 7 for G) and appH: critical-path set
A, B, C, D1, E, F, G-derived, N. Affected labels: NONE. Problem G stays
OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL. No change proposed anywhere.

## Author decision needed
None. (Report-only: attack-plan depends_on drift; pre-existing hard-coded
"Chapter~12" at appH:2832.)

## Remaining open step
To close G-matrix-derived: (i) a derived (not assumed) identification of a
Presentation-A cut (spectral projection of the coordinate operators, or a link/edge
partition) with partial M under which the cut entropy equals the eq:Sent-exp local
density — this is the content of the G-R4 obstruction's missing hypothesis and the
next critical target; (ii) the interacting sector (alpha_1 curvature and alpha_2
matter coefficients from the cubic C-term and matter of eq:Smatrix); (iii) a
derivation of eq:bdy-EE stationarity; (iv) the dim-1 boundary-to-bulk conversion for
eq:Leff. Ranked open avenues: (1) spectral-cut identification with fuzzy/curved
background (alpha_1); (2) link-variable/edge-mode partition à la HHL as the non-
geometric factorization (leads 2012.15683/2105.13726, not verified by me); (3)
interacting correction to alpha_0 via Gaussian-fixing around the constant-Theta
background; (4) G-R3 dim-1 conversion as a standalone consistency package.

## Special instructions for the gatekeeper
- Verify the bounded obstruction against the actual ch06/ch03 text (the concessions at
ch06:196-198 and 202-205 and the def:rhoD phrase), not against the attack plan.
- The no-go is definitional on Presentation-A data without a dictionary: do not read
it as a no-go for Presentation-B/conditional derivations, and do not read it as
closing G beyond its hypothesis class.
- Re-run halfline_ee.py and continuum_check.out expectations: quoted numbers are only
sigma = 0.0096 +- 0.0003, s1 massless constant 0.2315(3), slope 1/6 (fit 0.166626),
large-mu bound style s1 <~ (pi/2)e^{-mu}. c0_ref is NOT a claim.
- The text must not be read as deriving ass:Sent-density; paragraph 2 closes with the
scoped status sentence and G stays OPEN.
- Anous2020 is the only citation; verify it exists before bib insertion; until the
entry is added, an undefined-citation flag in build_check for Anous2020 is expected,
not a defect.
- Check the CRLF conversion (insert file is LF; post-state bare LF must be 0) and the
single-splice rule (060 F1 lesson).
