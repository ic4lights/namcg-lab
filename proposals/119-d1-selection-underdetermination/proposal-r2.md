# Proposal 119-d1-selection-underdetermination, round 2

Round 2 applies EXACTLY the three required actions of review-r1.md (verdict ACCEPT WITH REQUIRED
REVISIONS, confirmed unchanged by review-r1-addendum.md). No new claims, no new targets; all other
payload lines are byte-identical to the r1 payload.

## Result
Within the same stated hypothesis class, Equation `eq:Smatrix` (ch03) does **not** fix the
Presentation-A selection of the couplings `(c3,c2,c1,c0)` of Equation `eq:V`: (i) at tree level the
selection is undefined or zero (`S_matter` is a symbolic placeholder; commutator-type lifts carry the
shift symmetry `Phi -> Phi + kappa I`, which forbids potentials, while the eq:Smicro lift with
`D_mu Phi = partial_mu Phi - i A_mu Phi` and the eq:dictionary bridge are NOT shift-covariant and
`eq:V` is not shift-invariant); (ii) at one loop the scalar sector generates `(Tr X)^2` (tensor
`(256,96)`, ratio `3/8` at `n=4`) so the slice `c2=0` is not preserved, and no one-loop fixed ray of
`r = c2/c3` exists for `0 <= w < 64+16*sqrt(42) ~ 167.7 > 16*pi^2` at `B_G=v4=0` (exact criterion
`(w-v4-64)^2 >= 10752 + 112 B_G w`, equality the single marginal double ray `r* = sqrt(42)/14`;
off-window `w=200` gives the exact rays `r = 3/14, 1`); (iii) the generated `c2/c3` ratio is group
data (`0` for orthonormal `u(4)` vs `1/56` for orthonormal `su(4)`, with orthonormality asserted and
a non-orthonormal-basis control showing the earlier `1/35` was an artifact), the displayed beta
system is the `u(4)` instance `(A_G,B_G)=(4,0)`, and for `su(4)` the `Tr X^2` channel carries
`A_G = N-2/N = 7/2` in addition to `B_G = 1/16`, both group choices giving thresholds above
`16*pi^2`; (iv) the sign of the generated `c1` is unfixed in every scheme (sharp cutoff
`(Lambda^2/64pi^2)(64c3+136c2+...)`, content-dependent sign; Pauli-Villars regulator-spectrum datum;
mass-independent `beta_{c1}=c1*gamma`, so `c1=0` is an exact surface); (v) the constant-Theta Moyal
route collapses (star potential = ordinary potential at zero gradient to all orders; `O(Theta)` total
derivative, `O(Theta^2)` pure derivative operator). The package closes nothing: Problems D, D1, A
remain OPEN as recorded.

## Target and status
- Problem D "local Lorentz" ledger block (`chapters/appH-microscopic-proofs.tex`, section
  `Problem D: local Lorentz`): verbatim current status "Status: OPEN. Priority: CRITICAL PATH.
  Completion: PROGRAMME-CONDITIONAL."; D1 is the matrix-derived-submatrix agenda item
  (`ch17-agenda.tex`), no separate appH section exists, and the payload refers to "Problem~D1"
  as text exactly as the 118 paragraph does.
- Original target of the gate this package addresses: derive the selection of the Presentation-B
  potential `eq:V` from the matrix theory `eq:Smatrix` (Section `sec:ch3-relate`;
  `ass:dictionary` is "a matching condition, not an established result").
- Classification: bounded negative result (underdetermination) + explicit missing-datum list.
  DERIVED status: none; nothing is marked solved; no label changes proposed.
- Dependencies: `eq:Smatrix`, `eq:Smicro`, `eq:V`, `ass:dictionary`, `sec:ch3-relate`, `eq:LUV-def`
  - all re-verified defined exactly once book-wide this round (plus `eq:dictionary`, defined but NOT
  referenced by this payload; see Decisions).

## Source reading
digest + targeted reads (round-2 baseline re-verified live: appH sha1[:12] `2ed53c7778c1`, 843649 B;
anchor `\section{Problem E: signature}` count 1 at byte offset 290106 - matches dispatch-r2 pins;
the tree is actively re-typeset, so anchoring is byte-based only). Read in full this round:
`proposals/119-d1-selection-underdetermination/{dispatch-r2.md, review-r1.md, review-r1-addendum.md,
proposal-r1.md, manifest.md, notes.md, insert-overdetermination-r1.tex}`, targeted live reads:
`chapters/ch03-matrix-action.tex` L213-230 (eq:Smicro: `D_mu Phi = partial_mu Phi - i A_mu Phi`
"acting on the \(I\) index", `S_micro` with `-g^{(0)mu nu}(D_mu Phi)^dagger D_nu Phi - V(Phi^dagger Phi)`),
L344-363 (ass:dictionary, `eq:dictionary`: `[Xhat_mu, Phi] <-> i Theta_{mu nu} D^nu Phi` "plus
higher-derivative corrections"); the `namcg-book7.tex` preamble trace macro (L104:
`\newcommand{\Tr}{\operatorname{Tr}}`); the trace-macro census in appH (`\operatorname{Tr}` 88x,
`\mathrm{Tr}` 22x incl. the adjacent 118 paragraph, `\Tr` 2x); all four tail paragraphs before the
anchor re-read at byte level (118 paragraph ending unchanged: "... and nothing in this paragraph
closes Problem~D, Problem~D1, or Problem~A."). All payload numbers trace to `out-r119.txt` /
`out-r119-r2.txt` (this folder) and the quoted stage artifacts (notes.md "Payload numbers -> sources"
plus the Round 2 section).

## Research and reasoning
1. **Tree-level audit (F-3 revised).** `eq:Smatrix` is IKKT + cubic C-term + symbolic `S_matter` with
   no `Phi` field; any `Phi`-potential must come from `S_matter` (never specified) or from a lift of
   `eq:Smatrix`. Lifts in which `Phi` enters only through commutators are invariant under constant
   shifts `Phi -> Phi + kappa I` (exact: `[A, Phi + kappa I] = [A, Phi]`), which forbids any potential,
   while `eq:V` (slice `c1 = -lambda v^2/2 != 0`) breaks the symmetry. The lift actually chosen in
   the manuscript is NOT of that type: with `D_mu Phi = partial_mu Phi - i A_mu Phi` acting by LEFT
   multiplication on the `I` index (ch03 L214-218), `D_mu(Phi + kappa I) = D_mu Phi - i kappa A_mu`
   (defect `- i kappa A_mu` re-derived symbolically this round), so the eq:Smicro lift is not
   shift-covariant; the eq:dictionary bridge is not either: its LHS `[Xhat_mu, Phi]` is shift-
   invariant while the RHS `i Theta_{mu nu} D^nu Phi` picks up `+ kappa Theta_{mu nu} A^nu`. Also
   `X = Phi^dagger Phi` itself shifts (`X -> X + kappa(Phi + Phi^dagger) + kappa^2 I` for the scalar
   warm-up), so `V(Phi^dagger Phi)` in eq:Smicro is not shift-invariant. So any local `W(X)` is an
   added datum, and the shift-symmetry obstruction is lift-specific: it applies to the commutator-type
   subclass only. (Established derivations for the stated lifts; the lift choice itself is
   manuscript input - hypothesis class.)
2. **One-loop machine.** `V1_div = +(1/64 pi^2 eps) STr M4` with `STrM4[W] = Tr(H_W H_W)` on the
   real-component Hessian; MSbar, `beta = -2*(1/eps CT coefficient)`. Calibrated on the textbook
   `lambda phi^4/4!` (`beta = 3 lambda^2/16 pi^2`) and O(2) anchors (verifier H1-H3). Unchanged r1.
3. **Scalar tensors.** `Tr(H_{TrX^2}^2) = (32(n+4), 96)`, `Tr(H_{TrX^2} H_{(TrX)^2}) = (96, 32(n+4))`,
   `Tr(H_{(TrX)^2}^2) = (0, 128(n+1))`, verified `n=2..6` (B1-B3). At `n=4`: `(256,96)`, ratio `3/8`.
   Unchanged r1.
4. **Gauge one-loop, group dependence (F-2 revised wording).** `S = sum_ab K^ab K^ba`,
   `K^ab = Tr(T^a Y T^b)`, `Y = Phi Phi^dagger`: orthonormal `u(n)` gives exactly `(n, 0)`; orthonormal
   `su(n)` gives `(n - 2/n, 1/n^2)`; `n=4`: `B/A = 1/56` vs `0` for `u(4)` (C1-C9 unchanged). The
   displayed beta system's `beta_c3` carries `+4w`, i.e. the `Tr X^2` channel coefficient `A_G = 4`
   of `u(4)`; `su(4)` instead carries `A_G = 7/2` in that channel AND `B_G = 1/16` in `beta_c2`
   (gatekeeper C4/C7/C8 teeth; independently re-verified by review-r1). Round 2 therefore labels the
   displayed system the `u(4)` instance `(A_G,B_G)=(4,0)` and states the `su(4)` channel data
   OUTSIDE the displayed pairing.
5. **Beta system and fixed rays (F-1 revised endpoint).** With `w = g^4/c3^2`, `v4 = sum y_f^4/c3^2`,
   `B_G` the gauge double-trace coefficient in units of `w` (`0` for the displayed `u(4)` instance):
   `beta_c3 = c3^2(256+192r+4w-4v_4)/32pi^2`, `beta_c2 = c3^2(96+512r+640r^2+B_G w)/32pi^2`,
   `beta_r = c3 P(r)/32pi^2`, `P(r) = 448r^2 + (256+4(v4-w))r + 96 + B_G w` (exactly quadratic,
   `A22 = 0`). `disc P = 16[(w-v4-64)^2 - 10752 - 112 B_G w]` (D3/D3b): real fixed rays exist iff
   `(w-v4-64)^2 >= 10752 + 112 B_G w`, with a single marginal double ray at equality (`r* = sqrt(42)/14`
   at `B_G=v4=0`, `w* = 64+16 sqrt(42)`: re-derived this round as `P(r*)=P'(r*)=0` with exactly one
   distinct root) and two distinct rays above it; hence at `B_G=v4=0` none occur for the STRICT window
   `0 <= w < w* ~ 167.69 > 16 pi^2 ~ 157.91`; off-window `w=200 -> {r=3/14, r=1}` (D4-D7).
   General `n`: `w*(n) = 8(n+4)+sqrt(3072(n-1/2))`; `w*(2), w*(3) < 16 pi^2` (qualifies the stage-2
   blanket "any N" claim; notes.md discrepancy 5).
   **Group-threshold robustness (new payload sentence, grounded here):** with the displayed system's
   `+A_G w` channel general, `P = 448r^2+(256+4v4-A_G w)r+96+B_G w` and
   `disc = 16[(64+v4-(A_G/4)w)^2 - 10752 - 112 B_G w]` (re-derived symbolically this round; matches
   review-r1's independent identity). For `su(4)` (`A_G=7/2`, `B_G=1/16`, `v4=0`) the exact threshold
   is `w* = 544/7 + 32 sqrt(705)/7 ~ 199.09`; rigorously, for all `0 <= w <= 158`,
   `|(7/8)w - 64| <= 297/4` and `(297/4)^2 = 88209/16 < 10752`, while `112 B_G w = 7w >= 0`, so no
   rays exist on `[0,158]` and `16 pi^2 < 158` - hence "both give thresholds above 16 pi^2" with no
   floating-point step. The `u(4)` value `64+16 sqrt(42) > 16 pi^2` is exact (D6). The printed-form
   `(A_G=4, B_G=1/16)` one-parameter instance sits in the D3b-checked family (threshold ~173.39).
   Renormalizable Yukawas enter only through single cyclic words -> `TrX^2` only (E1/E2), so
   `P(0) = 96 + B_G w > 0` is fermion-independent: `c2=0` is not a fixed ray and not an IR attractor.
6. **`c1` scheme analysis.** Sharp cutoff `V_quad = m2 Lambda^2/(64 pi^2)` per real scalar,
   `K3 = 64`, `K2 = 136` at `n=4`, content sign can flip (F6 tooth); Pauli-Villars finite
   regulator-spectrum datum with threshold coefficient `A M0 (2 ln(M0/mu^2)+1)` (F7); mass-independent
   schemes `beta_{c1} = c1 gamma`, `c1 = 0` exact surface (F8). Unchanged r1.
7. **Moyal collapse.** Constant Theta: every p-th star term carries >= 1 derivative on each factor, so
   at zero gradient `W_star = W_ordinary` exactly to all orders; `O(Theta)` term total derivative,
   `O(Theta^2)` zero-gradient part 0 (G1-G3b). Unchanged r1.
8. **Comparison with the original target.** Unchanged: the missing step (derive the slice of `eq:V`
   from `eq:Smatrix`) is NOT closed; what is established is that it cannot be closed inside the named
   class by tree-level completion with a commutator-type lift, one-loop running (any group, any
   renormalizable Yukawa content), cutoff scheme choice, or constant-Theta structure. The F-3 revision
   additionally makes explicit that the shift obstruction does NOT apply to the manuscript's eq:Smicro
   lift (it is lift-specific to the commutator subclass), which NARROWS the class in which the
   tree-level argument runs and is recorded as such in the payload and Scope sentence.
9. **Review-r1 conflicts noticed in round 2 (report only, none fixed):** none between review-r1 and
   the live sources beyond its own findings; one internal looseness noted in review-r1 itself: the
   F-2 option-(a) snippet keeps the symbolic `112 B_G w` in the rays condition of a system it labels
   "the u(4) instance `(A_G,B_G)=(4,0)`" - coherent only because `B_G` remains the symbolic
   coefficient of the displayed `beta_c2` (u(4) value 0); the payload retains the snippet's wording
   verbatim (spec) with this sentence recorded as the reading. The addendum's determinism note (its
   "6-byte diff" was its own appended `rc2=0` line) confirms `out-r119.txt` is the stable verifier
   capture.

## Claim classification
- Tree-level shift invariance of commutator-type lifts; non-shift-covariance of the eq:Smicro lift and
  the eq:dictionary bridge; tensor formulas n=2..6; exact fixed-ray discriminant, endpoint structure
  (double ray at equality), thresholds incl. `w*(su4) > 16 pi^2` by the `(297/4)^2 < 10752` bound and
  `16 pi^2 < 158`; generalized-discriminant identity in `A_G`; scheme statements (sharp integral, PV
  threshold, c1=0 surface); Moyal collapse identity: established derivations (verifier and/or this
  round's independent sympy checks; full ranges).
- One-loop beta system itself (content, `STrM4` heat-kernel form, `Y = Phi Phi^dagger` gauge channel,
  `B_G`/`A_G` normalization; one-loop truncation): conditional result (standard 1-loop machinery
  applied to a stated field content).
- "Group choice and renormalizable content are not fixed by `eq:Smicro`": input (manuscript state:
  `ass:dictionary` is a matching condition).
- No selection beyond the stated class (nonperturbative completion, dynamical Theta, higher loops):
  unresolved / not evaluated - the no-go is bounded by its hypotheses, not a general no-go.

## Proposed changes
**File: `chapters/appH-microscopic-proofs.tex` (one insertion, purely additive).**
Anchor (quote, occurs exactly once, byte offset 290106 at the working baseline `2ed53c7778c1`/843649):
`\section{Problem E: signature}`. The insertion lands immediately after the 118 paragraph whose final
sentence (kept, quoted as boundary) is: "... and nothing in this paragraph closes Problem~D,
Problem~D1, or Problem~A." and immediately before the anchor. Canonical splice:
`text.replace(anchor, payload + CRLF + anchor, 1)`; POST = 843649 + 5191 + 2 = **848842**
(full sha1 `9e0b198af2c3c7f11454980ec6df2e875fbb80ef`).
Everything else in the file is kept; no sentences are replaced. No stale passages identified: the
surviving 116/117/118 statements are consistent with, and are cited as context by, the new paragraph.
Payload file: `insert-overdetermination-r1.tex` (10 sentence lines, one `\emph{...}` paragraph,
118 register; zero `\label`, zero `\cite`, ASCII, CRLF-terminated, **5191 bytes, sha1[:12]
`c085c19cba68`**). Diff vs the r1 payload (superseded copy `insert-overdetermination-r1-superseded-r1.tex`,
`3b4c2d0794a9`/4704): exactly the F-1/F-2/F-3 passages on lines 2, 5, 6, 9; lines 1, 3, 4, 7, 8, 10
byte-identical, including the final rule-3 scope sentence. Payload text (canonical bytes are the file;
changed lines below in full):

```latex
\emph{One-loop and scheme-level constraints on the selection datum.} Write \(X=\Phi^\dagger\Phi\) and \(r=c_2/c_3\) for the four couplings \((c_3,c_2,c_1,c_0)\) of the general \(U(4)\)-invariant potential \(c_3\operatorname{Tr}X^2+c_2(\operatorname{Tr}X)^2+c_1\operatorname{Tr}X+c_0\), so that Equation~\eqref{eq:V} is the slice \((\lambda/4,\,0,\,-\lambda v^2/2,\,\lambda v^4)\).
At tree level nothing fixes this slice: the matter term \(S_{\mathrm{matter}}\) of Equation~\eqref{eq:Smatrix} is a symbolic placeholder that has never been specified, and lifts of Equation~\eqref{eq:Smatrix} to the bifundamental of Equation~\eqref{eq:Smicro} in which \(\Phi\) enters only through commutators are invariant under \(\Phi\mapsto\Phi+\kappa\,\mathbb I\), a symmetry that forbids any potential, whereas the lift of Equation~\eqref{eq:Smicro} with \(D_\mu\Phi=\partial_\mu\Phi-iA_\mu\Phi\) acting on the \(I\) index, and the bridge of Assumption~\ref{ass:dictionary}, are not shift-covariant, and Equation~\eqref{eq:V} is not shift-invariant; every local \(W(X)\) assigned in Presentation~B is therefore an added datum rather than an output of Equation~\eqref{eq:Smatrix}.
At one loop the scalar sector generates \((\operatorname{Tr}X)^2\): for the counterterm kernel \(\operatorname{Tr}(H_WH_W)\), with \(H_W\) the Hessian in the real components of \(\Phi\), one has \(\operatorname{Tr}(H_{\operatorname{Tr}X^2}^2)=256\operatorname{Tr}X^2+96(\operatorname{Tr}X)^2\) at \(n=4\) (ratio \(3/8\)), so \(\beta_{c_2}>0\) on the slice \(c_2=0\).
The gauge contribution is group data: over an orthonormal Hermitian \(u(N)\) basis the gauge loop gives exactly \(+N\operatorname{Tr}X^2\) with vanishing \((\operatorname{Tr}X)^2\) coefficient, while over an orthonormal \(su(N)\) basis it gives \((N-2/N)\operatorname{Tr}X^2+(1/N^2)(\operatorname{Tr}X)^2\), so the generated ratio of \((\operatorname{Tr}X)^2\) to \(\operatorname{Tr}X^2\) at \(N=4\) is \(1/56\) against \(0\) for \(U(4)\), and the group choice itself is not fixed by Equation~\eqref{eq:Smicro}.
With \(w=g^4/c_3^2\), \(v_4=\sum_f y_f^4/c_3^2\), and \(B_G\) the coefficient of the gauge contribution to \(\beta_{c_2}\) in units of \(w\) (\(B_G=0\) for \(u(4)\)), \(\beta_{c_3}=c_3^2(256+192r+4w-4v_4)/(32\pi^2)\)... [lines 5-6 in canonical bytes: beta clause now reads \(B_G=0\) for \(u(4)\) only; rays clause reads "\(\ge\) ... with a single marginal double ray at equality and two distinct rays above it: at \(B_G=v_4=0\) none occur for \(0\le w<64+16\sqrt{42}\approx167.7>16\pi^2\), and off-window at \(w=200\) the two exact rays are \(r=3/14\) and \(r=1\). The displayed system is the \(u(4)\) instance \((A_G,B_G)=(4,0)\); for \(su(4)\) the \(\operatorname{Tr}X^2\) channel carries \(A_G=N-2/N=7/2\) in addition to \(B_G=1/16\), and both give thresholds above \(16\pi^2\)."]
The \(c_1\) direction is scheme- and content-dependent: [unchanged r1 line 7]
The constant-\(\Theta\) Moyal structure generates no potential either: [unchanged r1 line 8]
Scope: within this hypothesis class (tree-level Presentation~A with unspecified matter term or commutator-type lift, [rest of unchanged r1 line 9]
The selection of Equation~\eqref{eq:V} by Presentation~A therefore remains an input of the matching discussed in Section~\ref{sec:ch3-relate}: it is constrained but underdetermined as datum, and nothing in this paragraph closes Problem~D, Problem~D1, or Problem~A.
```

(The bracketed markers in lines 5-9 above are proposal prose, NOT payload bytes; the canonical payload
is `insert-overdetermination-r1.tex`, pinned `c085c19cba68`/5191, whose complete text the gatekeeper
reads from that file. Payload references: `eq:Smatrix`, `eq:Smicro`, `eq:V`, `eq:LUV-def`,
`sec:ch3-relate`, `ass:dictionary` - all labels verified unique this round; `\eqref{eq:V}` etc. all
pre-existing; `Assumption~\ref{ass:dictionary}` is a new reference to an existing unique label, kept
inside the dispatch-enumerated set; zero new `\cite`, zero `\label`.)

**No other manuscript file changes. No bib entries. No code changes.**

## Verification scripts
All in this folder (reproduction pack - re-run commands and expected invariants):
1. `python -I -B verify_r119.py` -> sections A,H,B,C,D,E,F,G all-PASS, `TOTAL 62/62 PASS` and
   `ALL CHECKS DONE 119`; script UNCHANGED in round 2 (option (a) chosen; per dispatch the check-side
   strict-iff wording of D3/D3b is left as is per F-5 "no action required"). Round-2 raw capture
   `out-r119-r2.txt` (new file; old captures untouched), confirmed byte-identical to `out-r119.txt` (`009de59d50ac`/6476, `cmp` exit 0) since the
   script and interpreter are unchanged (three independent rerun confirmations in review-r1 + addendum).
   Capture procedure (auditable): the run's shell wrapper had appended its own 14-byte `VERIFY-EXIT=0`
   status line (file 6490 B); after `cmp -n 6476` proved the verifier prefix byte-identical to
   `out-r119.txt`, the appended status line was removed by `head -c 6476` truncation - no verifier byte
   was added, changed, or deleted, and the file ends `TOTAL 62/62 PASS` / `ALL CHECKS DONE 119` as
   required; raw stdout redirect, never hand-edited. Key invariants unchanged (see proposal-r1 section; D5
   already records the threshold double root `r*=sqrt(42)/14`, consistent with the F-1 endpoint).
2. `python -I -B gen_payload_119.py` (twice; second run asserts byte-identity) ->
   `payload bytes: 5191  sha1[:12]: c085c19cba68`,
   `POST: 848842 (= 843649 + 5191 + 2)  full sha1: 9e0b198af2c3c7f11454980ec6df2e875fbb80ef`,
   `GEN OK 119`. Join guard `r'\\[A-Za-z]+$'` unchanged; positive control (injected dangling `\secti`)
   fires and negative control passes INSIDE both generator runs; additionally re-demonsembled
   standalone this round by extracting the regex literal from the patched generator source:
   positive control prints `JOIN GUARD FIRED (injected): '\\secti'`, real payload passes.
   Hygiene asserts unchanged and passing (CR=LF, ends CRLF, ASCII, no tab/BOM/`$`, no `\label`/`\cite`,
   brace and `\(...\)` balance), live baseline pins and independent POST reconstruction unchanged.
3. `python -I -B cert-r119p.py` -> `PRE-COMPILE PINS OK: baseline 2ed53c7778c1/843649, anchor 1,
   payload c085c19cba68/5191, POST 848842 9e0b198af2c3c7f11454980ec6df2e875fbb80ef`, `PASS 1: rc=0`,
   `PASS 2: rc=0`, zero `!` error lines, zero undefined/multiply-defined references in pass 2,
   `CERT PASS`, `temp tree removed`; raw capture `out-cert-r119p-r2.txt` (`CERT-EXIT=0`). Compile
   tree: fresh out-of-repo temp dir from tracked working bytes minus `namcg-book7.pdf` and `reports/`,
   plus the working `namcg-book7.bbl` (2945 files); tree deleted after.
4. Round-2 independent re-derivations (scratch, outside the repo; content summarized in notes.md
   Round 2 section): generalized discriminant identity; endpoint double-ray (`P(r*)=P'(r*)=0`, one
   distinct root); `w*(su4) = 544/7 + 32 sqrt(705)/7 ~ 199.09` and the rigorous `(297/4)^2 < 10752`
   bound; lift non-covariance defects (`-kappa A`, `kappa Theta A`) with explicit 2x2 matrix
   witnesses; `w=200 -> {3/14, 1}` re-check.

## Decisions Taken
- **F-2 option (a) chosen** (gatekeeper's minimal snippet: displayed system labeled `u(4)` instance
  `(A_G,B_G)=(4,0)`; `su(4)` channel data `A_G=7/2`, `B_G=1/16` stated outside the displayed pairing).
  Rationale: the payload's own argument never needs the general system inside the displayed equations
  - its only group-dependent input (line 4, `0` vs `1/56`) is already stated group-general with both
  channel coefficients, and the displayed system's sole job is the fixed-ray threshold, for which the
  window conclusion is now recorded as robust to the group choice with an exact bound. Option (b)
  would widen the displayed formulas, force the verifier extension, and enlarge the diff for no gain
  in the argument; the dispatch marks (a) the default. Recorded the reading under which (a) is exact:
  `B_G` in the symbolic beta/rays clauses is the coefficient kept general in the `beta_c2` channel of
  the A_G=4 family (D3b family), and `su(4)` needs the separate statement because it also moves
  `A_G`.
- **Trace macro**: use `\operatorname{Tr}` (as in the rest of the payload), not the gatekeeper
  snippet's `\Tr`. Verified live: the preamble defines `\Tr = \operatorname{Tr}` (compiles either
  way), but appH uses `\operatorname{Tr}` 88x vs `\Tr` 2x and the adjacent paragraphs use
  `\mathrm{Tr}`/`\operatorname{Tr}` - the payload stays internally consistent with its own r1 lines
  and with the dominant manuscript macro (dispatch: "match the manuscript, not the snippet").
- **Bridge named via `Assumption~\ref{ass:dictionary}`** instead of a new `\eqref{eq:dictionary}`:
  keeps the payload reference set inside the dispatch-enumerated list (`eq:Smatrix, eq:Smicro, eq:V,
  sec:ch3-relate, ass:dictionary, eq:LUV-def`); the bridge equation `eq:dictionary` is the displayed
  equation INSIDE Assumption ass:dictionary (ch03 L352-356, verified), so the reference names the
  same object; both labels verified unique book-wide.
- **`review-r1-addendum.md`** read and confirmed spec-neutral (it restates F-1/F-2/F-3 verbatim and
  retracts a self-flagged determinism artifact); incorporated as a pinned input.
- **Stale OUT handling**: the r1 payload bytes were preserved byte-for-byte as
  `insert-overdetermination-r1-superseded-r1.tex` (re-hashed to the old pin before deletion), the old
  file then removed so the generator's byte-identity assert compares the two round-2 runs.
- **Verify capture procedure**: first round-2 capture attempt appended a `VERIFY-EXIT` status line,
  which would have broken the required `... ALL CHECKS DONE 119` ending; discarded and recaptured
  with a plain redirect (script determinism established by the addendum's three reruns); the capture
  is a raw stdout redirect, never hand-edited.
- **F-5 wording**: verifier D3/D3b check messages left strict (not manuscript-bound; review-r1 and
  addendum both waive action; dispatch requires the verify pack unchanged under option (a)).
- Rejected alternatives: option (b) (above); `\Tr` (above); `\eqref{eq:dictionary}` (above); keeping
  the r1 closed-interval window clause (false at endpoint, F-1); attributing shift invariance to the
  eq:Smicro lift (false as printed, F-3).

## Milestone assessment
Routine. Required-revision round on a bounded negative result + datum list; no milestone trigger (no
critical-path step derived, no missing link closed without new inputs).

## Status-label recommendation
None. Re-derived current critical-path list (ch17 full-GR criterion + appH ledger): A, B, C, D1, E,
F, G-derived, N; Problem D remains OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL; D1, A unchanged.
This package proposes no label edits and closes nothing.

## Author decision needed
None. (The missing-datum decision is recorded as research content under "Remaining open step"; it
changes no definition, scope statement or label, and spacetime remains emergent throughout.)

## Remaining open step
Unchanged from r1: exactly one datum (or a derivation replacing it) is still needed to close the
selection target: (1) an explicit `S_matter` (or a specified non-minimal lift of `eq:Smatrix`) whose
tree level produces `W(X)`; or (2) specified group choice + fermion content + a UV boundary condition
on `(c3,c2,c1)` at the cutoff `LUV` (eq:LUV-def) shown to survive to the infrared; or (3) a
non-renormalizable (double-trace) completion whose induced flow fixes the slice; or (4) a
strongly-coupled / dynamical-Theta branch (not evaluated here, outside the tested class). None of
(1)-(4) is supplied by `eq:Smatrix` as recorded, and none is excluded by this package. The no-go is
bounded by its hypotheses: tree level with a commutator-type lift (the eq:Smicro lift is NOT
shift-covariant - F-3), one-loop accuracy, `n=4` bifundamental scalars, renormalizable
gauge+Yukawa content, fixed Theta, and the four schemes computed.

## Special instructions for the gatekeeper
- Scope limits and must-not-assert items are UNCHANGED from proposal-r1 (read it jointly with this
  file for everything outside the three revised passages): the payload closes NOTHING; do not
  summarize as "eq:V is not selected by the matrix theory" beyond the stated hypothesis class.
- This round's diff is exactly review-r1's F-1/F-2/F-3 (plus the forced proposal wording syncs);
  re-check FIRST: (i) the payload file `insert-overdetermination-r1.tex` lines 2/5/6/9 vs the
  Corrected snippet block (only intentional deviation: `\operatorname{Tr}` for the snippet's `\Tr` -
  decision recorded, both are the same macro by preamble L104 - and "the bridge of
  Assumption~\ref{ass:dictionary}" for "the eq:dictionary bridge", inside the dispatch-enumerated
  reference set); (ii) `>=`/equality-case/strict-`<` endpoint wording against your D5/GK14/GK17;
  (iii) the su(4)-threshold sentence against the exact `544/7 + 32 sqrt(705)/7` and the `(297/4)^2 <
  10752` bound (elementary, re-derive in one line); (iv) POST 848842 /
  `9e0b198af2c3c7f11454980ec6df2e875fbb80ef` reconstructed from the LIVE tree (anchor may move - the
  cert recomputes and fails loudly); (v) generator run twice byte-identical and the join-guard
  positive control firing (extract the literal from the source; injecting a clean string makes the
  self-test assert fail by construction).
- Verifier `verify_r119.py` and `out-r119.txt` are UNCHANGED this round; `out-r119-r2.txt` must be
  byte-identical to `out-r119.txt` (same interpreter, same script). Do not "fix" the D3/D3b strict-iff
  message wording (F-5 waived; pack must stay pin-stable).
- Report, not fix: the review-r1 option-(a) snippet's retained symbolic `B_G` in a clause labeled
  `(A_G,B_G)=(4,0)` is internally coherent only under the recorded reading (proposal reasoning item
  9); if the gatekeeper reads it differently, that is a round-3 wording finding, not math.
- 118-folder and repo-root items unchanged from r1 (stray `out-q4.txt`, stale `out-s7-m1.txt`).
