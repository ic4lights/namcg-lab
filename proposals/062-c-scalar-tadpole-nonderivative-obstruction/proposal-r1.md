# Proposal 062-c-scalar-tadpole-nonderivative-obstruction, round 1

Target: attack-plan item **C.scalar** (Problem C: conformal mode and Cassini — OPEN / CRITICAL PATH /
PROGRAMME-CONDITIONAL), scout routes **C-R1** (top) + **C-R2** (2nd) of `reports/sme-scout-20261109-0354.md`,
bundled because both are statements about the same trace channel of the same 048/049 computation and the
Problem-C operator that consumes it. C-R3 not used: C-R1 did not stall.

## Result

**(C-R1, computation.)** The `q=0` non-derivative sector deferred at appH L2815 ("The tree non-derivative
terms, the terms that cancel the tadpole of \(U_4\) at \(q=0\), and any term with the same fibre dependence
are not computed") is computed *for the sub-class of terms that carry \(\sqrt{|g|}\) alone*, in the recorded
048/049 hypothesis class (equal weights, \(V=T\), frozen symbol, product background, static channel
\(q\cdot v=0\), one loop, pure-trace channel \(h_{\mu\nu}=(t/4)\bar g_{\mu\nu}\)). What is established:

1. **Profile identity (established derivation).** For every density term \(W_i\sqrt{|g|}\) the whole
   \(q=0\) \(t\)-dependence is fixed by \(\sqrt{|g+h|}=\sqrt{|g|}\,(1+t/2+t^{2}/16+O(t^{3}))\) (pure-trace
   channel; the sign of the quadratic part is direction-dependent — rank-one gives \(-\lambda^2/8\) — which
   is stated in the text).
2. **Exact tadpole/mass relation (established, conditional on the class data).** With the formal
   continuation \(S_E=-S_L\) used by the reduced form: \(T_i=-\sqrt{|g|}W_i/2\), \(\mathcal M_i=-\sqrt{|g|}W_i/8\),
   so \(\mathcal M_i=T_i/4\) (ratio continuation-invariant) and, with the recorded \(q_*^2=2\mathcal M L\),
   \(q_*^2=\tfrac12 L\sum_i T_i\).
3. **Bounded no-go (conditional result within the class).** No supplied set of \(\sqrt{|g|}\)-alone terms —
   including a cosmological-type counterterm — cancels the \(q=0\) tadpole and leaves a nonzero
   \(\mathcal M\): the cancellation condition \(\sum_i W_i=0\) cancels the quadratic part identically
   (verified: at \(\Lambda_{\rm ct}^*=(U_4+U_2)/\sqrt{|g|}\) the total \(\mathcal M=0\), hence \(q_*^2=0\)).
   A background flat at \(q=0\) therefore has the vacuum-display pole at \(q^2=q_b^2\), tachyonic-signed for
   \(\hat U>0\). Conversely the Yukawa threshold \(q_*^2=q_b^2\) requires an uncancelled tadpole
   \(|T|=\hat U\chi^2/(32\pi^2m^8)\).
4. **Uncancelled-\(U_4\) magnitudes (conditional, convention-bound).** Taken alone,
   \(\mathcal M_E[U_4]=+F\sqrt{|g|}\hat U\chi^4/256\pi^2\) (sign pulls \(q_*^2\) positive for \(\hat U>0\)
   in the stated continuation), \(q_*^2[U_4]=6F\sqrt{|g|}\hat U\chi^4m^6/(\hat V+2\hat T)\), ratio to
   \(q_b^2\) equal to \(F\sqrt{|g|}\chi^2m^8/2\); the comparison of magnitudes turns on the conventions for
   \(m,\vartheta,\sqrt{|g|}\) and is not settled.
5. **Localization of the missing ingredient (conditional within the class).** The \(\chi\)-derivative that
   sets \(\beta_K\) survives the cancellations (the tree density carries \(\rho_M\), not \(\sqrt{|g|}\), as
   recorded), so it is *not* the missing \(\mathcal M\); within the recorded class the missing non-derivative
   terms cannot be supplied by further vacuum-energy terms carrying \(\sqrt{|g|}\) alone. The candidate that
   could supply \(\mathcal M\) without cancelling its own tadpole is the response of the fibre levels to
   \(\bar h\) in \(v^M-2\sigma^M\), recorded at appH L2795 as not computed.

**(C-R2, definability obstruction + missing-step record.)** The full Problem-C target (gauge-fixed quadratic
scalar operator on the locked vacuum in a constructed frame) is not definable on bare Presentation-A data:
three of its inputs are themselves among the unresolved outputs — (i) a constructed frame (Repair~I
obstructed; the route used posits the frame via Assumptions `ass:nondeg`, `ass:frame-lock`),
(ii) \(G_{\mathrm{eff}}\) (the \(Z\) of `eq:Z-sigma` is written in terms of \(G_{\mathrm{eff}}\), whose
derivation is Problem F), (iii) the constraint structure of the massless sector (whether the \(\psi\) sector
of Chapter `ch:massless-tensor` supplies the Fierz–Pauli constraint structure is unresolved). A
`\paragraph{Missing step.}` block is added to Problem C's ledger section — the last critical-path ledger
entry lacking one (precedent: 061 supplied the one for G). The \(\psi\) notation collision (tensor-fluctuation
trace vs the \(K\)-mode labels of the Problem F entry) is disambiguated in the inserted text.

**Nothing is closed.** Problem C stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL. The no-go (3) is
bounded by its hypothesis class (see "Remaining open step"); it is a fork, not a stop: it relocates the
missing \(q=0\) ingredient to the fibre-level response to \(\bar h\), which is the queued follow-up
computation.

## Target and status

Appendix H ledger entry, `chapters/appH-microscopic-proofs.tex` L482-486, quoted verbatim:

    \paragraph{Ledger label.}
    Status: OPEN. Priority: CRITICAL PATH. Completion:
    PROGRAMME-CONDITIONAL. A scalar-tensor result is a reduced-scope
    outcome only when its operator, coupling and phenomenological test
    are supplied; it does not by itself meet the matrix-derived criterion.

Original target, `chapters/ch17-agenda.tex` L142-150 (verbatim extract):

    Compute the full quadratic scalar operator on the locked vacuum in a
    constructed frame: the canonically normalised kinetic coefficient of the
    pure-trace scalar (including the induced Einstein--Hilbert contribution),
    its mixing with \(T_{\mu\nu}\), its non-minimal curvature coupling, and its
    matter coupling. ... From the operator, produce the pole mass, or a ratio
    \(m_\psi/v\), together with the coupling that can be compared with Cassini
    bounds.

Dependencies: Problem F (derivation of \(G_{\mathrm{eff}}\), used by `eq:Z-sigma` and by the 048/049
reduced form); frame construction (part of Problem C itself, `sec:status-C` Repair~I obstruction
L498-551); Assumption `ass:gap-psi`; the 048/049 trace-channel sector of the Problem F entry
(appH L2773-2821). Consistency: Chapter 17 and Appendix H agree (C in the critical-path set, OPEN,
PROGRAMME-CONDITIONAL). No discrepancy found. DERIVED or PROGRAMME-CONDITIONAL: this proposal is
PROGRAMME-CONDITIONAL evidence inside the Problem F entry's class; it neither is nor claims the
Problem-C operator.

## Source reading

digest + targeted reads. Digest CURRENT (built at aa93aae). Files read IN FULL for the passages relied on:
`chapters/appH-microscopic-proofs.tex` L479-641 (whole Problem C ledger section, including the anchor
paragraph at L631-641), L2773-2821 (the 048/049 "Potential of \(\chi\)" set of paragraphs and the
scope/status paragraph), the Problem G section header location; `chapters/ch17-agenda.tex` L142-181
(Problem C closure criterion and Lemma `lem:msigma`), `eq:Z-sigma` context L246; `chapters/ch04-vierbein-emergence.tex`
L108-150 (Repair~I, `def:vierbein`, the remark whose closing sentence L148-149 is quoted in the C block)
and L171 (`ass:nondeg`); `chapters/ch03-matrix-action.tex` L265 (`ass:frame-lock`), L274-290
(`eq:Phi-transform` and the Presentation~A/B statement at L288 "Presentation~A alone; it is the additional
structure that Presentation~B..."); `chapters/ch07-massless-tensor.tex` L2, L411 (`ch:massless-tensor`,
`ass:gap-psi`); `reports/sme-scout-20261109-0354.md` routes C-R1/C-R2/C-R3 and hazards H1-H7;
`reports/ledger.md` Problem C entry. Byte state of `chapters/appH-microscopic-proofs.tex` re-verified
this round: 566953 B, sha256 21737625769589a64090c8b7f93842b1eaa5d12cff3e4877f70f2db8e5947999, CRLF 3415,
bare LF 0. `bib/namcg.bib` unchanged: 27350 B, sha256 40d6ea09915dd4b8220f30c466821118492ee5560f66930b7c5d9a2dd8b95b90,
CRLF 908, bare LF 0. Nothing unreadable.

## Research and reasoning

### 1. Determinant profile (established identity)

With \(\epsilon=\bar g^{-1}\bar h\), \(\sqrt{|\det(\mathbf 1+\epsilon)|}=1+\tfrac12\mathrm{tr}\,\epsilon
+\tfrac18(\mathrm{tr}\,\epsilon)^2-\tfrac14\mathrm{tr}(\epsilon^2)+O(\epsilon^3)\). For the pure-trace
channel \(\bar h=(t/4)\bar g\) (so \(t=\bar h^\mu{}_\mu\), \(\epsilon=(t/4)\mathbf 1\)) this is exact:
\(\sqrt{\det(\mathbf 1+(t/4)\mathbf 1)}=(1+t/4)^2=1+t/2+t^2/16\) (all orders below cubic in 4d). Verified
symbolically two ways in `tadpole_minderivative.py` (exact pure-trace determinant: remainder 0; random
symmetric 4x4 at \(\epsilon=10^{-3}\): remainder \(-9.29\cdot10^{-11}\), consistent with \(O(\epsilon^3)\)).
Direction dependence: along a rank-one direction \(\epsilon=\lambda vv^{\mathsf T}\) the second-order part
is \(-\lambda^2/8\), so the sign of the quadratic determinant term is channel-dependent; the inserted text
states the pure-trace channel as part of the claim.

### 2. Class data taken from the manuscript (inputs, quoted)

appH L2773-2777: density terms without derivatives of the wave that depend on \(\chi\), equal weights:
\(\rho_M V_t/g^2+U_4+U_2\), \(U_4=-\frac{F}{32\pi^2}\sqrt{|g|}\hat U\chi^4\),
\(U_2=-\frac{F}{32\pi^2}\sqrt{|g|}[2(\hat V-\hat T)-\tfrac34\vartheta(\hat V-2\hat T)]\chi^2\); at
\(V=T\): \(U_2=-\frac{3F}{128\pi^2}\sqrt{|g|}\vartheta\hat T\chi^2\) (re-derived: match `True`).
L2779: where \(\bar h^{11}\) is negligible, \(U_4,U_2\) and the fibre-constant part of \(Y\) carry
\(\sqrt{|g|}\) alone. The tree density carries \(\rho_M\), not \(\sqrt{|g|}\) (L2775, as recorded).
Reduced form (L2807): \(S_E=(q^2/4L)t^2-(1-\tfrac12\beta_K)\varrho_0 t\), \(L=32\pi^2m^6/A\),
\(A=(\hat V+2\hat T)/24\). L2809: "With a term \(\tfrac12\mathcal Mt^2\), \(q_*^2=2\mathcal ML\)".
L2811: \(q_b^2=12\hat U\chi^2/m^2(\hat V+2\hat T)\) — **parse fixed to
\(q_b^2=12\hat U\chi^2/[\,m^2(\hat V+2\hat T)\,]\)**, because with this parse the recorded large-\(N\)
\(S^2_N\) limit of the same section reproduces exactly \(q_b^2\to\chi^2/m^2\) (script section 4:
\(\hat U/N^2=1\), \((\hat V+2\hat T)/N^2=12\)); the alternative parse \(12\hat U\chi^2(\hat V+2\hat T)/m^2\)
reproduces no recorded limit. L2813 display denominator \(q^2-q_b^2+q_*^2\); L2815 sign sentence and the
not-computed sentence; L2819 consequence ("the vacuum term must be cancelled at the minimum without
cancelling its derivative in \(\chi\)").

### 3. Tadpole/mass relation and continuation convention

A term \(W\sqrt{|g|}\) in the density contributes \(W\sqrt{|g|}(1+t/2+t^2/16)\) to the Euclidean action
density; with the formal continuation \(S_E=-S_L\) used by the reduced form (L2807 displays \(S_E\)), the
\(t\)-sector data are \(T=-\sqrt{|g|}W/2\) (coefficient of \(t\)) and \(\mathcal M=-\sqrt{|g|}W/8\) (in
\(\tfrac12\mathcal Mt^2\)), hence \(\mathcal M=T/4\) and \(q_*^2=2\mathcal ML=\tfrac12 LT\) (remainder 0,
script section 3). The *ratio* \(\mathcal M/T=1/4\) and the relation \(q_*^2=\tfrac12 LT\) are invariant
under the continuation choice; only the common sign follows the convention. This is why the inserted text
states the convention explicitly. (Earlier draft reasoning that read \(\mathcal M\) off the Lorentzian
coefficient directly gave the opposite sign for \(q_*^2[U_4]\); corrected before writing. The manuscript's
own recorded sentence at L2815 is about the *display* (its denominator) and is unaffected.)

Saddle completion re-derived (script section 5): eliminating \(t\) from
\((q^2/4L+\mathcal M/2)t^2-Jt\) gives \(-LJ^2/(q^2+2\mathcal ML)\); with the recorded vacuum shift the
denominator becomes \(q^2-q_b^2+q_*^2\), so the pole is at \(q^2=q_b^2-q_*^2\): tachyonic-signed for
\(\hat U>0\) unless \(q_*^2>q_b^2\), exactly as recorded at L2815.

### 4. Flatness no-go and the Yukawa threshold

Tadpole cancellation for the recorded terms plus a constant counterterm \(-\Lambda_{\rm ct}\) (a
\(\sqrt{|g|}\)-alone term) gives \(\Lambda_{\rm ct}^*=F\chi^2(-3\hat T\vartheta-4\hat U\chi^2)/(128\pi^2)
=(U_4+U_2)/\sqrt{|g|}\) (verified equal), and at it the total \(\mathcal M=0\Rightarrow q_*^2=0\). So within
this sub-class, "flat at \(q=0\)" forces the tachyonic-signed pole — the *only* \(\sqrt{|g|}\)-alone escape
is to leave an uncancelled tadpole of size \(|T|=2q_b^2/L=\hat U\chi^2/(32\pi^2m^8)\) (the Yukawa
threshold). Uncancelled \(U_4\) alone: \(\mathcal M_E=+F\sqrt{|g|}\hat U\chi^4/256\pi^2\),
\(q_*^2[U_4]=6F\sqrt{|g|}\hat U\chi^4m^6/(\hat V+2\hat T)\), ratio \(q_*^2[U_4]/q_b^2=F\sqrt{|g|}\chi^2m^8/2\)
(positive for \(\hat U>0\)); whether this exceeds 1 is a convention question about \(m,\vartheta,\sqrt{|g|}\)
(the ratio \(|T_{\rm need}/T[U_4]|=2/(F\chi^2m^8\sqrt{|g|})\) is the same statement).

### 5. Why the surviving \(\chi\)-derivative is not the missing \(\mathcal M\)

The tree density \(\rho_M V_t/g^2\) carries no \(\sqrt{|g|}\) (as recorded; no identification of \(\rho_M\)
with a determinant of the fluctuating frame is made in this class), so it is invisible to the profile
identity and supplies no \(t\)-channel \(\mathcal M\); but its \(\chi\)-derivative (the \(\beta_K\)
machinery, and the L2819 requirement) is untouched by \(\sqrt{|g|}\)-tadpole cancellations. Hence L2819's
requirement is *compatible* with the flatness no-go, and the two recorded gaps (uncancelled
\(\chi\)-derivative; uncomputed non-derivative terms) are genuinely distinct. The candidate class that
could carry \(\mathcal M\) with an uncancelled tadpole is the fibre-level response of \(v^M-2\sigma^M\) to
\(\bar h\) (L2795: "The response of the fibre levels to \(\bar h\) ... are not computed"). This is where
the missing ingredient sits, as a hypothesis-localized target for the next package.

### 6. Worked-example audit of the 049 entry (no PRIOR-CLAIM-ERROR)

`example_recheck.py` reproduces every recorded number of the L2797 example in units
\(F\sqrt{|g|}N^2\vartheta^2/32\pi^2\), \(\vartheta=1\), \(x=\chi^2/\vartheta=3/10\): reading "a tree quartic
7.935 and a tree cubic \(-12.36\)" as the **values of the tree terms at \(\chi\)** (not coefficients) gives
\(U_4=-0.09\), \(U_2(V=T)=-0.9\), \(|\varepsilon|=|U_4/\tilde U|=0.0113\) (recorded 0.011),
\(U_{\chi\chi}=16(7.935)+9(-12.36)+4(-0.9)+16(-0.09)=10.680000\) (recorded 10.68), and \(\beta_K=1\)
conditioned on \(Y=7.5\) reproduces \(\beta_K=1.000000\) with denominator \(10.6800=U_{\chi\chi}\) and
\(N_K/N^2=1.0000\) (consistent with "the tree quartic is of the order of \(Y\)"). All recorded values
reproduced: `True`. **No correction to L2797 is proposed.** (The coefficient reading fails to reproduce
10.68 and was rejected.)

### 7. C-R2 definability analysis

The three premises the C operator needs that are not bare Presentation-A data:
(i) **Frame.** `eq:Phi-transform` (ch03 L280) is the Presentation-B transformation law; ch03 L288 states it
is extra structure not available "Presentation~A alone". Repair~I is obstructed in `sec:status-C`
(no equivariant linear map; rank \(\le3\) contraction), and the remark after `def:vierbein` (ch04 L139-150)
records that a corrected Repair~I "would need additional background tensors or an independent coframe,
which is part of Problem~C". The route in use posits the frame (`ass:nondeg`, `ass:frame-lock`).
(ii) **\(G_{\mathrm{eff}}\).** `eq:Z-sigma` (ch17 L246) writes \(Z=2N-3/(4\pi G_{\rm eff}v^2)\); appH L582-583
records "This result also assumes \(G_{\mathrm{eff}}>0\), which is not derived (Problem~F)".
(iii) **Massless-sector constraint structure.** The trace-constrained Fierz–Pauli structure of the
quadratic tensor block is not shown to follow from the NAMCG quadratic block; the \(\psi\) sector of
Chapter `ch:massless-tensor` is the unresolved supplier, and the notation collision with the \(K\)-mode
\(\psi\) labels of the Problem F entry is disambiguated in the inserted text.
With these supplied, the recorded C-section results (`lem:msigma` tree radial mass; \(Z\) at the stated
truncation; off-shell trace–tensor mixing) are computations within posited frame data — the inserted
Missing-step block says exactly this.

### 8. Hazard compliance (H1-H7)

No literature result is imported anywhere in this package; every claim is internal derivation or a quotation
of recorded manuscript data. H1: no continuum conformal-factor literature used. H2: no lattice spectra used.
H3: no upgrade of any \(\beta\) to a Cassini bound — the F block explicitly disclaims any Cassini or
Newtonian comparison. H4: rotating class not treated (disclaimed). H5: no fakeon import; the \(Z<0\) branch
is not "discharged". H6: no heat-kernel/background-metric generation of kinetic terms — the emergence
rule respected (nothing in the insert makes the metric fundamental; the F block states \(t\) is not
identified with an emergent-metric quantity). H7: no soft-scalar/scalon arguments.

### 9. Comparison with the original target

The original C target is the full operator; this package supplies (a) a computed \(q=0\) sub-sector with a
bounded obstruction in the 048/049 class, and (b) a definability statement sharpening what the target
requires. It does not compute the loop kinetic coefficient, mixing, non-minimal or matter couplings, the
pole mass, or any Cassini comparison. No premise is being retired; nothing is marked closed.

## Claim classification

- Determinant expansion and pure-trace identity; rank-one sign: **established identity** (script-verified).
- \(U_2(V=T)\) form; \(L\); \(q_b^2\) parse (large-\(N\) consistency); saddle completion reproducing the
  recorded display denominator; reproduction of the L2797 example: **established derivation /
  established identity against recorded data**.
- \(\mathcal M=T/4\), \(q_*^2=\tfrac12LT\) for \(\sqrt{|g|}\)-alone terms: **established identity within
  the class hypotheses** (inputs conditional on L2773-2815 as recorded).
- Flatness \(\Rightarrow q_*^2=0\), pole at \(q^2=q_b^2\) tachyonic for \(\hat U>0\); Yukawa-threshold
  tadpole \(|T|=\hat U\chi^2/(32\pi^2m^8)\); \(U_4\)-alone magnitudes and ratio:
  **conditional result** (hypothesis class stated in the text).
- Density data, \(\rho_M\)-not-\(\sqrt{|g|}\), "fibre response not computed", L2819 requirement:
  **input** (recorded manuscript data).
- "The missing \(\mathcal M\) is localized in the fibre-level response to \(\bar h\)":
  **conditional within the recorded class / unresolved step** (it is an elimination argument: no
  \(\sqrt{|g|}\)-alone candidate works; the named candidate is uncomputed).
- Magnitude comparison \(q_*^2[U_4]\) vs \(q_b^2\): **conjecture-level until conventions fixed** — the text
  explicitly declines to settle it.
- C-R2 (i)-(iii) premises: **established readings of recorded text** (obstructions/assumptions quoted);
  "whether \(\psi\) supplies the FP constraint structure": **unresolved step**.

## Proposed changes

One file: `chapters/appH-microscopic-proofs.tex`. Two insertions, zero deletions, zero edits of existing
text. No bib changes. No new labels (the insert defines none; every `\ref`/`\eqref` is to an existing
label, verified unique: `eq:Phi-transform` ch03 L280; `def:vierbein` ch04 L117; `ass:nondeg` ch04 L171;
`ass:frame-lock` ch03 L265; `eq:Z-sigma` ch17 L246; `ass:gap-psi` ch07 L411; `ch:massless-tensor` ch07 L2;
`lem:msigma` ch17 L160 — first use of `ch:massless-tensor` inside appH, valid).

**Insertion C** (end of Problem C ledger section, before the existing status sentence). Anchor (unique,
count 1): the sentence-ending bytes `tensor operator or the remaining scalar couplings.` (ends L641:
"The displayed microscopic action on the fixed scaffold does not specify the full coupled, gauge-fixed
tensor operator or the remaining scalar couplings."). Insert after them. The following bytes must be
`\r\nProblems~B, C, D, F and~G remain open.\r\n\r\n\section{Problem D: local Lorentz}` (asserted; the
existing status sentence is kept, the block adds **no** own status sentence — exactly one scoped status
sentence closes the section). Anchor offset in the current pre-state: X_C = 144554.

**Insertion F** (end of the 048/049 "Potential of \(\chi\)" set of paragraphs in the Problem F ledger
section, immediately after its closing status paragraph and before the Problem G section header). Anchor
(unique, count 1): the bytes `\r\n\r\n\section{Problem G: HBEV}` at X_F = 539217; preceding bytes asserted
to end with `PROGRAMME-CONDITIONAL.` (the L2821 paragraph end). The F block closes with its own scoped
status sentence `Problems~C, F and~N remain open and PROGRAMME-CONDITIONAL.` — matching the convention of
every ledger paragraph in that block (061 precedent for a G status line).

`proposals/062-c-scalar-tadpole-nonderivative-obstruction/insert-r1.tex` is the exact byte content to
insert (LF line endings in the file; convert LF→CRLF on apply; it contains two blocks separated by the
line `%---SPLIT---%`: block 1 = manuscript text for insertion C, block 2 = for insertion F; strip the
trailing newline of block 2 before conversion, per `simulate_apply.py`). Verbatim content (the two fenced
blocks below equal the file's two blocks):

```latex
\paragraph{Missing step.} The full target of Problem~C is the gauge-fixed quadratic scalar operator on the locked vacuum in a constructed frame: the canonically normalised kinetic coefficient of the pure-trace scalar, including the induced Einstein--Hilbert term, its mixing with \(T_{\mu\nu}\), its non-minimal curvature coupling, its matter coupling, and its pole mass as a derived output, with Assumption~\ref{ass:gap-psi} discharged. On the bare data of Presentation~A this operator is not yet definable: three of the inputs it needs are among the things the target is meant to establish. (i)~A frame. The transformation law of Equation~\eqref{eq:Phi-transform} is a field-content choice of Presentation~B and is not derived from Presentation~A alone; the stated Repair~I map to an orthonormal frame is obstructed above; the remark following Definition~\ref{def:vierbein} records that a corrected Repair~I would need additional background tensors or an independent coframe, which is part of Problem~C; and the route actually used posits the frame through Assumptions~\ref{ass:nondeg} and~\ref{ass:frame-lock}. (ii)~\(G_{\mathrm{eff}}\). The coefficient \(Z\) of Equation~\eqref{eq:Z-sigma} is written in terms of \(G_{\mathrm{eff}}\), whose derivation is Problem~F, so the scalar wave-function renormalisation ties Problem~C to Problem~F. (iii)~The constraint structure of the massless sector. The trace-constrained Fierz--Pauli structure of the quadratic tensor block is not shown to follow from the NAMCG quadratic block, and whether the \(\psi\) sector of Chapter~\ref{ch:massless-tensor} supplies it is unresolved and is a dependency of Problem~C; the \(\psi\) of Chapter~\ref{ch:massless-tensor} is the trace of the tensor fluctuation, distinct from the mode labels of \(K\) used in the Problem~F entry. With these three inputs supplied, the recorded results of this section (the tree radial mass of Lemma~\ref{lem:msigma}, the wave-function factor \(Z\) of Equation~\eqref{eq:Z-sigma} at the stated truncation, and the off-shell trace--tensor mixing term) are computations within posited frame data; the loop-level kinetic coefficient, the mixing, the non-minimal coupling, the matter coupling and the pole mass are not outputs of the matrix theory, and in the conjugate-coordinate class the \(q=0\) non-derivative sector of the trace channel carries a bounded obstruction recorded in the Problem~F entry.
```

```latex
\emph{Trace-channel tadpole and the non-derivative sector at \(q=0\).} Under the hypotheses of the preceding set of paragraphs (equal weights, \(V=T\), frozen symbol, product background, static channel \(q\cdot v=0\), one loop), the \(q=0\) part of every density term that enters the trace channel carrying \(\sqrt{|g|}\) alone is fixed by the determinant. Write such a term as \(W_i\sqrt{|g|}\) at the background and take the channel along the pure-trace direction \(h_{\mu\nu}=(t/4)\bar g_{\mu\nu}\), \(t=h^\mu{}_\mu\): then \(\sqrt{|g+h|}=\sqrt{|g|}\,(1+t/2+t^2/16+O(t^3))\), by the expansion of \(\sqrt{\det(1+\epsilon)}\) to second order, so the whole \(q=0\) contribution of the term to the reduced \(t\)-form runs along one profile common to all such terms. Its tadpole \(T_i\) (the coefficient of \(t\) at \(q=0\)) and its contribution \(\mathcal M_i\) to the term \(\tfrac12\mathcal Mt^2\) are then proportional with a fixed ratio, invariant under the choice of continuation, while their common sign follows it: with the formal continuation \(S_E=-S_L\), \(T_i=-\sqrt{|g|}W_i/2\) and \(\mathcal M_i=-\sqrt{|g|}W_i/8\), and with \(q_*^2=2\mathcal ML\) as above, \(q_*^2=\tfrac12L\sum_iT_i\). Two consequences. First, no supplied set of terms carrying \(\sqrt{|g|}\) alone, including a cosmological-type counterterm, cancels the \(q=0\) tadpole and leaves a nonzero \(\mathcal M\): the cancellation condition \(\sum_iW_i=0\) cancels the quadratic part with it, so with the recorded terms a background flat at \(q=0\) has \(q_*^2=0\) and the pole of the vacuum-term display sits at \(q^2=q_b^2\), which for \(\hat U>0\) has the tachyonic sign recorded above. Conversely the Yukawa threshold \(q_*^2=q_b^2\) at \(\hat U>0\) requires an uncancelled tadpole of size \(|T|=\hat U\chi^2/(32\pi^2m^8)\) in the same convention. Second, taken alone and not cancelled, \(U_4\) contributes \(\mathcal M=F\sqrt{|g|}\hat U\chi^4/256\pi^2\), of the sign that pulls \(q_*^2\) positive for \(\hat U>0\), and \(q_*^2=6F\sqrt{|g|}\hat U\chi^4m^6/(\hat V+2\hat T)\); its ratio to \(q_b^2\) is \(F\sqrt{|g|}\chi^2m^8/2\), and the comparison of magnitudes turns on the conventions for \(m\), \(\vartheta\) and \(\sqrt{|g|}\) and is not settled here. The sign of the quadratic part of the determinant profile is direction-dependent (along a rank-one direction the second-order part is \(-\lambda^2/8\)), so the pure-trace channel used by the reduced form is part of the statement. The derivative in \(\chi\) that sets \(\beta_K\) survives these cancellations, because the tree density carries \(\rho_M\) and not \(\sqrt{|g|}\) as recorded (and no identification of \(\rho_M\) with a determinant of the fluctuating frame is made in this class), so it supplies no \(t\)-channel mass: the requirement recorded above, that the vacuum term cancel at the minimum without cancelling its derivative in \(\chi\), is compatible with these identities, and the surviving \(\chi\) derivative is not the missing \(\mathcal M\). Within the recorded class, then, the \(q=0\) terms flagged above as not computed cannot be cancelled by adding further vacuum-energy terms carrying \(\sqrt{|g|}\) alone; the candidate that could supply the required \(\mathcal M\) without cancelling its own tadpole is the response of the fibre levels to \(\bar h\) in \(v^M-2\sigma^M\), which is recorded as not computed. These statements are for the hypotheses of the preceding set of paragraphs and the channel convention stated here; they do not compute the fibre-level response, the loop kinetic term of \(\chi\), the second-order non-derivative terms at \(\chi^2\lesssim\vartheta\), the rotating class or higher loops, do not settle the convention-bound magnitudes, do not identify \(t\) with a quantity of the emergent metric, and give no Cassini or Newtonian comparison. Problems~C, F and~N remain open and PROGRAMME-CONDITIONAL.
```

Stale passages elsewhere: none identified. The new F text is consistent with (and explicitly references)
L2815/L2819/L2795; no existing sentence is contradicted or superseded; L2821 and the C-section status
sentence are kept verbatim.

Apply rule (as simulated): assert pre-state (appH 566953 B, sha256 21737625769589a64090c8b7f93842b1eaa5d12cff3e4877f70f2db8e5947999,
CRLF 3415, bare LF 0); single ascending pass
`out = app[:144554] + b"\r\n\r\n" + pc + app[144554:539217] + b"\r\n\r\n" + pf + app[539217:]` where
`pc, pf` are the CRLF-converted blocks (`pf` first stripped of its trailing LF). Predicted post-state:
**size 573261, sha256 4ad691c1888ca5806e37b716654e3fc282f9cecea766f3b34902e128797c5531, CRLF 3419,
bare LF 0**; block hashes: C raw 2415 B sha256-prefix c8985520d679dcf1 (single line, conversion a no-op);
F raw 3886 B prefix 55d18e40e5431354, rstripped 3885 B prefix 62340ebc66a9c398. If any earlier item
changes appH before this one integrates, re-anchor by the same assert-once anchors and re-run
`simulate_apply.py`; the byte offsets above are for the recorded pre-state only.

## Verification scripts

All under `proposals/062-c-scalar-tadpole-nonderivative-obstruction/` (run with `python -I` from that
folder):

- `tadpole_minderivative.py` / `tadpole_minderivative.out` — (1) determinant expansion (random-matrix
  check, remainder \(-9.29\cdot10^{-11}\); pure-trace exact, remainder 0; rank-one \(-\lambda^2/8\));
  (2) \(U_2(V=T)\) match `True`; (3) \(T=-\sqrt{|g|}W/2\), \(\mathcal M=-\sqrt{|g|}W/8\),
  \(q_*^2-LT/2=0\); (4) \(L=768\pi^2m^6/(2\hat T+\hat V)\), \(q_b^2\) parse + large-\(N\) limit
  \(\chi^2/m^2\), \(\mathcal M_E[U_4]=F\hat U\chi^4\sqrt g/256\pi^2\),
  \(q_*^2[U_4]=6F\hat U\chi^4m^6\sqrt g/(2\hat T+\hat V)\), ratio \(F\chi^2m^8\sqrt g/2\);
  (5) saddle completions (both denominators, remainder 0); (6) \(\Lambda_{\rm ct}^*=(U_4+U_2)/\sqrt{|g|}\)
  (`True`), \(\mathcal M|_{\rm flat}=0\Rightarrow q_*^2=0\), threshold \(|T|=\hat U\chi^2/(32\pi^2m^8)\),
  \(|T_{\rm need}/T[U_4]|=2/(F\chi^2m^8\sqrt g)\).
- `example_recheck.py` / `example_recheck.out` — reproduction of all recorded values of the L2797 worked
  example (`all recorded values reproduced: True`); no manuscript correction.
- `simulate_apply.py` / `simulate_apply.out` — byte-level apply simulation: pre-state asserts (appH and
  bib), anchor uniqueness and offsets X_C=144554, X_F=539217, following/preceding-byte asserts, block
  hashes, predicted post-state (size 573261, sha256 4ad691c1…, CRLF 3419, bare LF 0), junction spot checks
  (`F end junction found: True at 545467`), bib echoed unchanged.

Numbers-traceability (every formula/number in the inserted manuscript text → script line in
`tadpole_minderivative.out`, except where quoted from the manuscript):

| manuscript-text value | .out line |
|---|---|
| \(1+t/2+t^2/16\) | 3-4 |
| rank-one \(-\lambda^2/8\) | 5 |
| \(T_i=-\sqrt{|g|}W_i/2\), \(\mathcal M_i=-\sqrt{|g|}W_i/8\) | 9 |
| \(q_*^2=\tfrac12L\sum_iT_i\) | 11 |
| \(|T|=\hat U\chi^2/(32\pi^2m^8)\) | 26 |
| \(\mathcal M=F\sqrt{|g|}\hat U\chi^4/256\pi^2\) | 14 |
| \(q_*^2=6F\sqrt{|g|}\hat U\chi^4m^6/(\hat V+2\hat T)\) | 15 |
| ratio \(F\sqrt{|g|}\chi^2m^8/2\) | 16 |
| \(q_*^2=0\) at flatness; \(\Lambda_{\rm ct}^*=(U_4+U_2)/\sqrt{|g|}\) | 24-25 |
| \(q_*^2=2\mathcal ML\), display denominator, \(q_b^2\) formula | quoted from appH L2809/L2813/L2811 (parse cross-checked at .out 13, 17) |

## Decisions Taken

1. **Continuation convention (RESEARCHER-DECISION class).** Sign-bearing quantities are stated in the
   Euclidean convention of the reduced form (\(S_E=-S_L\)), with the invariant content (\(\mathcal M/T=1/4\),
   \(q_*^2=\tfrac12LT\)) stated first. Rejected alternative: quoting Lorentzian density coefficients as
   \(\mathcal M\) — it mislabels the sign relative to the display the section actually uses (and produced
   the earlier sign error caught during verification).
2. **L2797 example reading.** "tree quartic 7.935 / tree cubic −12.36" read as term **values** at \(\chi\):
   reproduces 10.68 and 0.011 exactly. Rejected: coefficient reading (fails 10.68). Consequence: no
   PRIOR-CLAIM-ERROR flag, no correction text.
3. **q_b² parse** = \(12\hat U\chi^2/[m^2(\hat V+2\hat T)]\), fixed by the recorded \(S^2_N\) limit
   \(\chi^2/m^2\). Rejected: \(12\hat U\chi^2(\hat V+2\hat T)/m^2\) (inconsistent with the recorded limit).
4. **C-block placement / status line.** Insert before the existing `Problems~B, C, D, F and~G remain
   open.` and add no own status sentence (one scoped status sentence per contiguous block). Rejected:
   appending after the status sentence (would separate it from the section it scopes).
5. **F-block status line.** Keep the closing `Problems~C, F and~N remain open and PROGRAMME-CONDITIONAL.`
   (matches every ledger paragraph's convention in that block; 061 precedent).
6. **Scope.** C-R1 + C-R2 bundled; C-R3 (operator-class/basis-invariance analysis) dropped because C-R1
   completed; the fibre-response computation is queued as the follow-up package (it is the localized
   missing ingredient, not a fallback).
7. **Apply mechanics.** Trailing LF of block F stripped before CRLF conversion (avoids a triple blank line
   before `\section{Problem G: HBEV}`); cosmetic only.

## Milestone assessment

**Routine.** No MILESTONE.md trigger applies: no critical-path step is closed or newly derived for the
programme (the no-go is bounded inside the 048/049 class; the definability block records premises).
Precedent: 060 and 061 were likewise judged routine. The value is a reproducible obstruction that
relocates the missing ingredient to a computable target (fibre-level response to \(\bar h\)).

## Status-label recommendation

Derived from the current agenda/ledger: critical-path set {A, B, C, D1, E, F, G-derived, N}. **No label
changes** are recommended or made by this proposal; Problem C remains OPEN / CRITICAL PATH /
PROGRAMME-CONDITIONAL; F and N unchanged.

## Author decision needed

None.

## Remaining open step

To close Problem C's original target: the full quadratic scalar operator — loop kinetic coefficient of the
pure-trace scalar including the induced EH term, mixing with \(T_{\mu\nu}\), non-minimal curvature
coupling, matter coupling, pole mass and a comparison-grade coupling — on a *constructed* frame with
`ass:gap-psi` discharged and \(G_{\mathrm{eff}}\) derived (Problem F). Within the 048/049 trace-channel
thread, the exact next computation identified by this package: the response of the fibre levels to
\(\bar h\) in \(v^M-2\sigma^M\) (the only candidate class left by the profile identity for an uncancelled
tadpole carrying \(\mathcal M\)), then the loop kinetic term of \(\chi\), the second-order non-derivative
terms at \(\chi^2\lesssim\vartheta\), the rotating class, and higher loops — all recorded as not computed.

## Special instructions for the gatekeeper

- This will be integration item 60 → your run carries the MANDATORY full `chapters/**/*.tex` scan. Audit
  items this insert **touches**: (a) the ψ notation collision (carried from earlier audits) — **resolved**
  by the explicit distinction sentence in the C block; (b) `eq:Z-sigma`/\(Z\)-family — touched by
  reference only, no new \(Z\) symbol; (c) \(G_{\rm eff}\) usage unchanged in meaning (identical to
  `eq:Z-sigma` context). Items it does **not** touch: β-family (only the pre-existing \(\beta_K\) of the
  same section is mentioned), \(\alpha=-16\pi G_{\rm eff}\) sites, \(\zeta\), \(\sigma\)-family, \(\nu\),
  \(G\) vs \(G_{\rm eff}\) mapping doubt (unresolved elsewhere, untouched here), F2 θ-closure.
- No new labels, no bib entries. Please confirm no duplicate `\label` arises (insert defines none) and
  that `ch:massless-tensor` resolves from appH (it is a chapter-level label; appH never referenced it
  before this insert).
- Must re-derive, not just re-run: the profile identity (pure-trace \((1+t/4)^2\) is one line), the ratio
  \(\mathcal M/T=1/4\), the flatness no-go at \(\Lambda_{\rm ct}^*\), and the threshold identity
  \(2q_b^2/L=\hat U\chi^2/(32\pi^2m^8)\) with \(L=768\pi^2m^6/(\hat V+2\hat T)\). Check the sign-convention
  sentence is right for the section's own \(S_E\) usage.
- Must NOT be asserted: closure or narrowing of Problem C; that the no-go extends beyond the stated
  hypothesis class (in particular not to \(\bar h^{11}\)-response terms, the rotating class, \(\rho_M\)
  frame-identifications, or higher loops); that any magnitude comparison was settled; that \(t\) is a
  quantity of the emergent metric.
- Re-run `simulate_apply.py` against the then-current appH: if the pre-hash matches, the predicted
  post-hash is 4ad691c1888ca5806e37b716654e3fc282f9cecea766f3b34902e128797c5531 (573261 B, CRLF 3419,
  bare LF 0); if not, re-anchor via the assert-once anchors and re-simulate before applying.
