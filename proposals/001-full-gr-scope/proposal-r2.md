# Proposal 001-full-gr-scope, round 2

**Review stage:** gatekeeper review only
**Milestone context:** The author selected the broader full-GR scope after the M5 decision request. This proposal does not claim that the M5 criterion or any research target has been achieved.
**Prior-round record:** No prior proposal/review file or exact prior-round diff was present in `proposals/` (only `.gitkeep`); this revision therefore does not claim or reconstruct an exact earlier diff.
**Integration boundary:** Proposal text only. No manuscript files, agenda statuses, or source files are edited here.

## Proposed source-integrated LaTeX changes

### 1. `chapters/ch01-geometrogenesis.tex`, after `\label{sec:ch1-checklist}`

Keep checklist items 1–7 unchanged. Remove the current numbered `\item` titled `Phenomenology as corollary` from the `enumerate` and place the following after `\end{enumerate}`. This keeps the seven derivation obligations separate from their phenomenological consequence.

```latex
\paragraph{Phenomenology as corollary.}
Rotation curves, regular cores, inspiral drag, and tidal disruption
are consequences to assess only after the seven derivation obligations
above and, for a full-GR claim, the additional criterion in
Section~\ref{sec:full-gr-criterion}. They are not evidence that those
requirements have been proved.

The seven-item list above is the existing infrared-sector
requirement. It is not by itself the broader full-GR criterion stated
in Chapter~\ref{ch:agenda}.
```

### 2. `chapters/ch17-agenda.tex`, after the Problem J text and before `\section{Problems that look like work and are not}`

```latex
\section{Broader full-GR criterion and additional open targets}
\label{sec:full-gr-criterion}

The seven derivation obligations in Section~\ref{sec:ch1-checklist}
remain distinct and necessary. Its phenomenology paragraph is a
corollary, not an eighth derivation obligation. The five problems
listed in Section~\ref{sec:ch17-done} are the existing criterion for
the infrared sector; they do not by themselves state the broader
full-GR criterion here, and no completion of that criterion is
claimed.

For a full-GR claim, the matrix-derived theory must meet all seven
obligations in Section~\ref{sec:ch1-checklist} and derive, rather
than assume, each of the following:
\begin{enumerate}
  \item \textbf{Nonlinear Einstein dynamics.} On the low-energy
        domain of the composite metric, derive the full nonlinear
        Einstein equation
        \[
          G_{\mu\nu}[g]+\Lambda_{\mathrm{eff}}g_{\mu\nu}
          =8\pi G_{\mathrm{eff}}T_{\mu\nu}^{\mathrm{total}},
        \]
        not only a linearized massless-TT equation. This equation is
        a target, not an input to a conservation argument.
  \item \textbf{Universal matter coupling and equivalence-principle
        recovery.} Derive a common low-energy matter action
        \(S_{\mathrm{matter}}[\psi,g]\) for all species, with no
        direct coupling to condensate or other long-range fields
        that survives in the claimed regime. Non-gravitational
        local physics must have no species-dependent metric, and
        test bodies must follow \(g_{\mu\nu}\)-geodesics in the
        appropriate low-energy limit.
  \item \textbf{Lorentzian signature.} Derive
        \(\operatorname{sig}(g)=(-,+,+,+)\) from the microscopic
        theory, rather than retaining Assumption~\ref{ass:lorentzian}.
\end{enumerate}

The additional tracked targets are OPEN:
\begin{itemize}
  \item \textbf{Problem K: frame and composite-metric construction.}
        Derive the locked frame and its non-degeneracy from the
        microscopic dynamics, thereby constructing the composite
        metric without assuming Assumptions~\ref{ass:frame-lock}
        and~\ref{ass:nondeg}.
  \item \textbf{Problem L: nonlinear Einstein dynamics.} Derive the
        nonlinear metric field equation and its domain of validity
        from the microscopic theory; the linearized result of
        Theorem~\ref{thm:mT} and the equation assumed in
        Theorem~\ref{thm:conservation} do not meet this target.
  \item \textbf{Problem M: universal matter coupling.} Derive a
        common low-energy action \(S_{\mathrm{matter}}[\psi,g]\) for
        all matter sectors and the corresponding
        equivalence-principle limit, excluding surviving direct
        couplings to extra long-range fields. Problem~C's
        unresolved scalar coupling is adjacent evidence, not
        ownership of this general target.
  \item \textbf{Problem N: diffeomorphism and Bianchi consistency.}
        Derive the required diffeomorphism identity and conservation
        of the total stress from the microscopic theory, rather than
        assuming a diffeomorphism-scalar infrared action and the
        Einstein equation as in Theorem~\ref{thm:conservation}.
  \item \textbf{Problem O: effective-field-theory control.} Derive
        the regime in which higher-derivative terms are controlled
        EFT vertices and establish that no additional physical pole
        occurs below its cutoff, rather than retaining
        Assumption~\ref{ass:EFT-a2}.
\end{itemize}
Problems K--O are OPEN and CRITICAL PATH for the full-GR scope;
their targets are not reported as derived. Problem E is likewise
required and OPEN for this scope, as specified below. Problems B, C,
D, F, and G retain their existing OPEN, CRITICAL PATH,
PROGRAMME-CONDITIONAL statuses.
```

### 3. `chapters/ch17-agenda.tex`, replace the current Problem E paragraph

Replace the current Problem E paragraph under `\subsection{Optional problems A and E}` with:

```latex
\paragraph{Problem E: Lorentzian signature.}
\emph{OPEN; OPTIONAL only within a scope retaining
Assumption~\ref{ass:lorentzian}; CRITICAL PATH for the full-GR
criterion of Section~\ref{sec:full-gr-criterion}.} Retaining
Assumption~\ref{ass:lorentzian} gives up the claim that Lorentzian
signature is emergent or derived. Euclidean positivity and a formal
Wick rotation do not select it. Under the full-GR criterion, derive
\(\operatorname{sig}(g)=(-,+,+,+)\) from the microscopic theory;
Problem~E remains OPEN until that target is met.
```

### 4. `chapters/appH-microscopic-proofs.tex`, status ledger

Update the opening sentence from “precise status of Problems A--J” to “precise status of Problems A--O.” Replace the current Problem E ledger label with:

```latex
\paragraph{Ledger label.}
Status: OPEN. Priority: OPTIONAL only within a scope retaining
Assumption~\ref{ass:lorentzian}; CRITICAL PATH for the full-GR
criterion of Section~\ref{sec:full-gr-criterion}. Completion:
PROGRAMME-CONDITIONAL. The claim of emergent or matrix-derived
Lorentzian signature is given up only in the scope retaining that
assumption.
```

Before `\section{What this appendix does not do}`, append:

```latex
\section{Problem K: frame and composite-metric construction}
\label{sec:status-K}

\paragraph{Ledger label.}
Status: OPEN. Priority: CRITICAL PATH for the full-GR scope.
Completion: PROGRAMME-CONDITIONAL.

The composite-metric definition and Lorentz-locking theorem are
conditional on a non-degenerate frame and the named locking and
local-Lorentz assumptions. Problem~D addresses deriving local
\(\mathrm{SO}(3,1)\) from Presentation~A; it does not derive the
existence and non-degeneracy of the condensate frame.

\paragraph{Missing step.}
Construct the locked frame from the microscopic dynamics, prove its
non-degeneracy on the claimed spacetime domain, and obtain
\(g_{\mu\nu}=\eta_{AB}e^A_\mu e^B_\nu\) without assuming
Assumptions~\ref{ass:frame-lock} and~\ref{ass:nondeg}. Until then
the metric definition is conditional.

\section{Problem L: nonlinear Einstein dynamics}
\label{sec:status-L}

\paragraph{Ledger label.}
Status: OPEN. Priority: CRITICAL PATH for the full-GR scope.
Completion: PROGRAMME-CONDITIONAL.

Theorem~\ref{thm:mT} is a conditional linearized tensor result.
Theorem~\ref{thm:conservation} assumes the Einstein equation; neither
derives nonlinear Einstein dynamics.

\paragraph{Missing step.}
Derive the full nonlinear field equation for the composite metric
from the microscopic theory, including its sourced solutions and
the regime in which the equation applies. Do not take
\(\eqref{eq:EFE-total}\) as an input to this derivation.

\section{Problem M: universal matter coupling}
\label{sec:status-M}

\paragraph{Ledger label.}
Status: OPEN. Priority: CRITICAL PATH for the full-GR scope.
Completion: PROGRAMME-CONDITIONAL.

The matter stress is defined by metric variation in
Chapter~\ref{ch:conservation}, but
separate matter conservation is not assumed. Problem~C leaves the
scalar's matter coupling unresolved; that is not a derivation of
universal coupling for all matter sectors.

\paragraph{Missing step.}
Derive a common low-energy matter action \(S_{\mathrm{matter}}[\psi,g]\)
for all species and establish the test-body geodesic and
equivalence-principle limit for local non-gravitational physics,
while excluding species-dependent metrics and surviving direct
couplings to additional long-range fields.

\section{Problem N: diffeomorphism and Bianchi consistency}
\label{sec:status-N}

\paragraph{Ledger label.}
Status: OPEN. Priority: CRITICAL PATH for the full-GR scope.
Completion: PROGRAMME-CONDITIONAL.

Theorem~\ref{thm:conservation} proves conservation conditionally
under diffeomorphism invariance of \(S_{\mathrm{IR}}\), the Einstein
equation, and on-shell matter and condensate fields. The current
agenda assigns no problem the derivation of these hypotheses from
the microscopic theory.

\paragraph{Missing step.}
Derive the diffeomorphism identity for the emergent effective action
from the microscopic dynamics, including the entropic and matter
sectors, and establish the resulting total-stress conservation
without assuming the target Einstein equation.

\section{Problem O: effective-field-theory control}
\label{sec:status-O}

\paragraph{Ledger label.}
Status: OPEN. Priority: CRITICAL PATH for the full-GR scope.
Completion: PROGRAMME-CONDITIONAL.

Assumption~\ref{ass:EFT-a2} treats the four-derivative terms as EFT
vertices rather than additional poles. Problem~F concerns the
coefficient map and specified fluctuation and ghost operators; it
does not prove the EFT-control assumption.

\paragraph{Missing step.}
Derive the low-energy expansion and its cutoff from the microscopic
theory, show that the higher-derivative operators are used within
that controlled regime, and exclude additional physical poles below
the cutoff. Do not infer EFT control from the composite nature of
the metric alone.
```

## Source-grounded ownership and status map

“Conditional” below means the cited theorem is proved under its listed hypotheses; it does not mean the hypotheses have been derived. K–O are proposed new agenda entries, not existing assignments.

| Target | Existing owner / source status | Ownership gap and proposal |
|---|---|---|
| Composite metric | Ch. 4, Definition `def:composite-metric`: \(g=\eta ee\) is defined from a non-degenerate frame; Ch. 17 `sec:ch17-closed` calls this conditional. | Definition does not construct the frame. Track construction under new K; do not assign it wholesale to D. |
| Frame-locking | Ch. 10, Theorem `thm:locking`, assumes `ass:frame-lock`, `ass:local-lorentz`, and `ass:nondeg`; it proves the gauge/frame statements conditionally. | Problem D owns deriving local Lorentz gauge symmetry from Presentation A and diagonal-connection dynamics, but not deriving existence of the condensate frame or non-degeneracy. New K covers those gaps. |
| Non-degeneracy | Ch. 4, Assumption `ass:nondeg`, explicitly supplies an invertible frame; the text notes that defects with \(\det e=0\) are possible. Ch. 16 `sec:ch16-inventory` calls it load-bearing. | No current agenda problem explicitly owns its derivation. New K. |
| Two massless TT modes | Ch. 7, Theorem `thm:mT`, derives \(m_T^2=0\) and the linearized Einstein action under the microscopic setup, `ass:nondeg`, `ass:lorentzian`, `ass:EE`, Fierz–Pauli, and other stated conditions. | B owns deriving entanglement stationarity; this remains a conditional theorem, not a completed derivation. It does not supply nonlinear dynamics. |
| Coefficient map | Ch. 1 checklist and Ch. 17 Problem F; Theorem `thm:Geff` is a conditional truncated heat-kernel identity. | F explicitly owns evaluation of physical \(G_{\mathrm{eff}}\) and \(A,B,C\); preserve F's frozen status. |
| Bianchi/diffeomorphism consistency | Ch. 11, Theorem `thm:conservation`, assumes a diffeomorphism-scalar infrared action, the Einstein equation, and on-shell matter/condensate fields. Ch. 17 `sec:ch17-closed` lists conservation as conditionally closed. | Proof is conditional; no current problem owns deriving those hypotheses. Do not reassign to D. New N. |
| EFT control | Ch. 9, Assumption `ass:EFT-a2`, prescribes four-derivative terms as vertices and not poles; Ch. 16 lists it as a load-bearing assumption. | The text adopts rather than proves this EFT reading. F is coefficient/operator matching, not proof of EFT control. New O. |
| Vacuum energy | Ch. 12, Theorem `thm:Leff`, is conditional on `ass:Sent-density`, `ass:bdy-EE`, and a boundary subtraction. Ch. 17 Problem G explicitly owns deriving infrared entropy and stationarity from the matrix theory. | G is the existing owner; theorem remains conditional and G's frozen status is unchanged. |
| Nonlinear Einstein dynamics | Ch. 7 `thm:mT` is linearized; Ch. 11 `thm:conservation` takes `eq:EFE-total` as an assumption. Ch. 17's five-item criterion does not list nonlinear dynamics as a separate derived target. | No existing agenda problem owns deriving the full nonlinear equation. D's connection issue and F's coefficients are adjacent, not ownership. New L. |
| Universal matter coupling / equivalence principle | Ch. 11 defines matter stress by metric variation and allows matter/condensate exchange. Ch. 17 Problem C and App. H `sec:status-C` leave scalar matter coupling unresolved. | C covers the scalar-specific branch only, not universal coupling of all matter sectors. New M. |
| Lorentzian signature | Ch. 4 Assumption `ass:lorentzian` supplies \((-,+,+,+)\); Ch. 17 Problem E and App. H `sec:status-E` say E is OPEN and optional only while that assumption is retained. | Under full-GR scope E becomes required and remains OPEN; under a scope retaining the assumption it remains optional. Preserve statuses B, C, D, F, and G. |

## Source coverage and review notes

- `scratch/digest.md` was regenerated and checked: `DIGEST CURRENT`, 30 files, `dirty-chapters: no`. It was used as navigation only.
- A full-text concept scan of `chapters/**/*.tex` covered all 30 files (1,712 matches across frame/metric/Einstein/matter/equivalence/Lorentz/non-degeneracy/Bianchi/conservation/EFT/ghost/coefficient/entropy/vacuum/signature/massless/TT/problem/scope/derivation/assumption terms). The digest also supplied the complete 30-file section/label index. This was not a complete read of all 30 files and must not be reported as a full scan.
- Direct full reads covered the cited checklist, non-degeneracy and Lorentzian assumptions, EFT assumption, locking theorem, conservation theorem, Problem E text, and the full Problems B and C ledger sections. The relevant Problem D ledger/status and missing-step passages, and Problems F and G ledger passages, were read for ownership/status claims. The proposal does not rely on a line-by-line reread of every unrelated calculation in all 30 files.
- The exact Problem E condition was verified in both Chapter 17 and Appendix H: it is OPTIONAL only in a scope retaining Assumption~\ref{ass:lorentzian}; its derivation is explicitly given up in that narrower scope.
- No duplicate labels were reported by the generated digest. The proposal only uses source labels verified in that digest or in the directly read source passages.
- Repository state at proposal creation: `main`, clean worktree; no prior proposal file or collision at `proposals/001-full-gr-scope/`.
- Because the source-reading protocol requires a full 30-file scan for scope or status changes, this proposal's source coverage remains incomplete pending that scan; do not treat the targeted review as satisfying the full-scan requirement.
