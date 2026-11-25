# Proposal 119-d1-selection-underdetermination, round 1

## Result
Within a stated hypothesis class, Equation `eq:Smatrix` (ch03) does **not** fix the Presentation-A
selection of the couplings `(c3,c2,c1,c0)` of Equation `eq:V`: (i) at tree level the selection is
undefined or zero (`S_matter` is a symbolic placeholder; the minimal kinetic lift carries the shift
symmetry `Phi -> Phi + kappa I`, which forbids potentials, while `eq:V` is not shift-invariant);
(ii) at one loop the scalar sector generates `(Tr X)^2` (tensor `(256,96)`, ratio `3/8` at `n=4`)
so the slice `c2=0` is not preserved, and no one-loop fixed ray of `r = c2/c3` exists for
`0 <= w <= 64+16*sqrt(42) ~ 167.7 > 16*pi^2` at `B_G=v4=0` (exact criterion
`(w-v4-64)^2 > 10752 + 112 B_G w`; off-window `w=200` gives the exact rays `r = 3/14, 1`);
(iii) the generated `c2/c3` ratio is group data (`0` for orthonormal `u(4)` vs `1/56` for
orthonormal `su(4)`, with orthonormality asserted and a non-orthonormal-basis control showing the
earlier `1/35` was an artifact); (iv) the sign of the generated `c1` is unfixed in every scheme
(sharp cutoff `(Lambda^2/64pi^2)(64c3+136c2+...)`, content-dependent sign; Pauli-Villars
regulator-spectrum datum; mass-independent `beta_{c1}=c1*gamma`, so `c1=0` is an exact surface);
(v) the constant-Theta Moyal route collapses (star potential = ordinary potential at zero gradient
to all orders; `O(Theta)` total derivative, `O(Theta^2)` pure derivative operator). This redirects
the D/D1 gate from further Presentation-B computation to an explicit datum decision. The package
closes nothing: Problems D, D1, A remain OPEN as recorded.

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
- Dependencies: `eq:Smatrix` (ch03 L143), `eq:Smicro` (L221), `eq:V` (L241), `ass:dictionary`
  (L346), `sec:ch3-relate` (L335), `eq:LUV-def` (L119) - all verified defined exactly once.

## Source reading
digest + targeted reads. `make_digest --check` is vacuous while `chapters/` is dirty (author
reflow 2026-11-23 08:50); baseline re-hashed directly:
`chapters/appH-microscopic-proofs.tex` working bytes sha1[:12] `2ed53c7778c1`, size 843649 B;
anchor `\section{Problem E: signature}` count 1 at byte offset 290106 (matches dispatch pins).
Read in full: appH Problem D ledger paragraph (L765 ff.), the four tail paragraphs before the
anchor (116-era composite, vacuum-non-degeneracy, state-route, 117 Gibbs, 118 constraint
paragraph ending "... and nothing in this paragraph closes Problem~D, Problem~D1, or Problem~A."),
ch17 Problem D paragraph (L329-360), ch03
`eq:Smatrix`/`eq:Smicro`/`eq:V`/`ass:dictionary` passages, `scratch/119/notes.md` and all
`scratch/119/out-*.txt` stage artifacts. All payload numbers trace to `out-r119.txt` (this
folder) and the quoted stage artifacts (see notes.md "Payload numbers -> sources").

## Research and reasoning
1. **Tree-level audit.** `eq:Smatrix` is IKKT + cubic C-term + symbolic `S_matter` with no `Phi`
   field; any `Phi`-potential must come from `S_matter` (never specified) or from a lift of
   `eq:Smatrix`. The minimal kinetic lift (`|D Phi|^2`-type terms and commutator interactions) is
   invariant under constant shifts `Phi -> Phi + kappa I`; `eq:V` (slice
   `c1 = -lambda v^2/2 != 0`) breaks it. So any local `W(X)` is an added datum. (Established for
   the stated lift; the lift itself is not specified in the manuscript - hypothesis class.)
2. **One-loop machine.** `V1_div = +(1/64 pi^2 eps) STr M4` with `STrM4[W] = Tr(H_W H_W)` on the
   real-component Hessian; MSbar, `beta = -2*(1/eps CT coefficient)`. Calibrated on the textbook
   `lambda phi^4/4!` (`beta = 3 lambda^2/16 pi^2`) and O(2) anchors (verifier H1-H3).
3. **Scalar tensors.** Exact Hessian computation: `Tr(H_{TrX^2}^2) = (32(n+4), 96)`,
   `Tr(H_{TrX^2} H_{(TrX)^2}) = (96, 32(n+4))`, `Tr(H_{(TrX)^2}^2) = (0, 128(n+1))` (pairs =
   coefficients of `TrX^2`, `(TrX)^2`), verified `n=2..6` with zero fit residuals on five
   diagonal backgrounds plus a generic off-diagonal integer-complex `Phi` check (B1-B3).
   At `n=4`: `(256,96)`, ratio `96/256 = 3/8`.
4. **Gauge one-loop, group dependence.** `S = sum_ab K^ab K^ba`, `K^ab = Tr(T^a Y T^b)`,
   `Y = Phi Phi^dagger`: orthonormal `u(n)` gives exactly `(n, 0)` (c2=0 preserved); orthonormal
   `su(n)` gives `(n - 2/n, 1/n^2)`; `su(2) = (1, 1/4)`; `n=4`: `B/A = 1/56` vs `0` for `U(4)`.
   Orthonormality is asserted numerically-symbolically (C1/C3), generic complex integer `Phi`
   checks at `u(4)/su(4)` (C6/C7), and a positive control shows a doubled basis element breaks
   orthonormality and moves `B/A` off `1/56` (C9), confirming the discarded `1/35` was a
   non-orthonormal-basis artifact.
5. **Beta system and fixed rays.** With `w = g^4/c3^2`, `v4 = sum y_f^4/c3^2`, `B_G` the group
   coefficient (`0` for `u(4)`, `1/16` for `su(4)`): `beta_c3 = c3^2(256+192r+4w-4v4)/32pi^2`,
   `beta_c2 = c3^2(96+512r+640r^2+B_G w)/32pi^2`, `beta_r = c3 P(r)/32pi^2`,
   `P(r) = 448r^2 + (256+4(v4-w))r + 96 + B_G w` (exactly quadratic: `A22 = 0`). Renormalizable
   Yukawas enter only through single cyclic words -> `TrX^2` only (E1/E2), so
   `P(0) = 96 + B_G w > 0` is fermion-independent: the slice `c2=0` is not a fixed ray, not an
   infrared attractor. `disc P = 16[(w-v4-64)^2 - 10752 - 112 B_G w]` (D3/D3b): no real fixed
   rays for `0 <= w <= 64+16 sqrt(42) ~ 167.69 > 16 pi^2 ~ 157.91` at `B_G=v4=0`; window grid,
   threshold double root `r* = sqrt(42)/14`, and the OFF-DEFAULT two-root tooth `w=200 ->
   {r = 3/14, r = 1}` all exact (D4-D7). General `n`: threshold `w*(n) = 8(n+4)+sqrt(3072(n-1/2))`;
   `w*(2) ~ 115.9`, `w*(3) ~ 143.6` fall below `16 pi^2` (this qualifies the stage-2 blanket
   "for any N" claim, see notes.md discrepancy 5; `w*(n) > 16 pi^2` for `n >= 4`).
6. **`c1` scheme analysis.** Sharp cutoff: `V_quad = m2 Lambda^2/(64 pi^2)` per real scalar
   (exact radial integral, F1/F2), `K3 = 64`, `K2 = 136` at `n=4`, `Tr Hess TrX = 64` (F3),
   `C_u(n) = n`, `C_su(n) = (n^2-1)/n` exact (F4/F5), and the content sign can flip (F6 tooth:
   fermion term dominates) -> sign of `delta c1` unfixed. Pauli-Villars: no power divergence,
   `delta c1|PV` = finite regulator-spectrum sum with threshold coefficient
   `A M0 (2 ln(M0/mu^2)+1)` (F7). Mass-independent schemes: `beta_{c1} = c1 gamma` (dimensional
   counting + mass independence), so `c1 = 0` is an exact RG surface (F8).
7. **Moyal collapse.** Constant Theta: every p-th star term carries >= 1 derivative on each
   factor, so at zero gradient `W_star = W_ordinary` exactly to all orders; verified to `p<=3`
   with independent `(Phi, Phi^dagger)`, the `p=3` term kills quadratic polynomials, the
   `O(Theta^2)` zero-gradient part is 0, and the `O(Theta)` term is a total derivative on the
   1x1 warm-up (G1-G3). No Theta-generated `W(X)` exists at constant Theta.
8. **Comparison with the original target.** The missing step (derive the slice of `eq:V` from
   `eq:Smatrix`) is NOT closed. What is established is that it cannot be closed inside the named
   class by any of: tree-level completion with the minimal lift, one-loop running (any group, any
   renormalizable Yukawa content), cutoff scheme choice, or constant-Theta structure. The gate is
   therefore a datum decision: explicit `S_matter`/lift, or group+fermion content plus a UV
   boundary condition on `(c3,c2,c1)` at `LUV` (eq:LUV-def), or a non-renormalizable
   double-trace completion; the strongly-coupled and dynamical-Theta branches are not evaluated.

## Claim classification
- Tree-level shift symmetry of the minimal lift; tensor formulas n=2..6; exact fixed-ray
  discriminants, roots, thresholds; scheme statements (sharp integral, PV threshold, c1=0
  surface); Moyal collapse identity: established derivations (verifier, full ranges).
- One-loop beta system itself (content, `STrM4` heat-kernel form, `Y = Phi Phi^dagger` gauge
  channel, `B_G` normalization; one-loop truncation): conditional result (standard 1-loop
  machinery applied to a stated field content).
- "Group choice and renormalizable content are not fixed by `eq:Smicro`": input (manuscript
  state: `ass:dictionary` is a matching condition).
- No selection beyond the stated class (nonperturbative completion, dynamical Theta, higher
  loops): unresolved / not evaluated - the no-go is bounded by its hypotheses, not a general
  no-go.

## Proposed changes
**File: `chapters/appH-microscopic-proofs.tex` (one insertion, purely additive).**
Anchor (quote, occurs exactly once, byte offset 290106 at the working baseline):
`\section{Problem E: signature}`. The insertion lands immediately after the 118 paragraph whose
final sentence (kept, quoted as boundary) is: "... and nothing in this paragraph closes
Problem~D, Problem~D1, or Problem~A." and immediately before the anchor. Canonical splice:
`text.replace(anchor, payload + CRLF + anchor, 1)`; POST = 843649 + 4704 + 2 = 848355
(full sha1 `eaea0964e7f50c27c24540b9ac523c443af873d7`).
Everything else in the file is kept; no sentences are replaced. No stale passages identified:
the surviving 116/117/118 statements ("the locking is not derived from Presentation A", "the
selection ... remains the missing input of Section~\ref{sec:ch3-relate}") are consistent with,
and are cited as context by, the new paragraph (which adds the one-loop/scheme depth and states
what is NOT excluded). Payload file: `insert-overdetermination-r1.tex` (10 sentence lines, one
`\emph{...}` paragraph, 118 register; zero `\label`, zero `\cite`, ASCII, CRLF-terminated,
4704 bytes, sha1[:12] `3b4c2d0794a9`). The payload text (each line CRLF-terminated in the file,
reproduced line by line; canonical bytes are `insert-overdetermination-r1.tex`):

```latex
\emph{One-loop and scheme-level constraints on the selection datum.} Write \(X=\Phi^\dagger\Phi\) and \(r=c_2/c_3\) for the four couplings \((c_3,c_2,c_1,c_0)\) of the general \(U(4)\)-invariant potential \(c_3\operatorname{Tr}X^2+c_2(\operatorname{Tr}X)^2+c_1\operatorname{Tr}X+c_0\), so that Equation~\eqref{eq:V} is the slice \((\lambda/4,\,0,\,-\lambda v^2/2,\,\lambda v^4)\).
At tree level nothing fixes this slice: the matter term \(S_{\mathrm{matter}}\) of Equation~\eqref{eq:Smatrix} is a symbolic placeholder that has never been specified, and the minimal kinetic lift of Equation~\eqref{eq:Smatrix} to the bifundamental of Equation~\eqref{eq:Smicro} is invariant under \(\Phi\mapsto\Phi+\kappa\,\mathbb I\), a symmetry that forbids any potential, whereas Equation~\eqref{eq:V} is not shift-invariant; every local \(W(X)\) assigned in Presentation~B is therefore an added datum rather than an output of Equation~\eqref{eq:Smatrix}.
At one loop the scalar sector generates \((\operatorname{Tr}X)^2\): for the counterterm kernel \(\operatorname{Tr}(H_WH_W)\), with \(H_W\) the Hessian in the real components of \(\Phi\), one has \(\operatorname{Tr}(H_{\operatorname{Tr}X^2}^2)=256\operatorname{Tr}X^2+96(\operatorname{Tr}X)^2\) at \(n=4\) (ratio \(3/8\)), so \(\beta_{c_2}>0\) on the slice \(c_2=0\).
The gauge contribution is group data: over an orthonormal Hermitian \(u(N)\) basis the gauge loop gives exactly \(+N\operatorname{Tr}X^2\) with vanishing \((\operatorname{Tr}X)^2\) coefficient, while over an orthonormal \(su(N)\) basis it gives \((N-2/N)\operatorname{Tr}X^2+(1/N^2)(\operatorname{Tr}X)^2\), so the generated ratio of \((\operatorname{Tr}X)^2\) to \(\operatorname{Tr}X^2\) at \(N=4\) is \(1/56\) against \(0\) for \(U(4)\), and the group choice itself is not fixed by Equation~\eqref{eq:Smicro}.
With \(w=g^4/c_3^2\), \(v_4=\sum_f y_f^4/c_3^2\), and \(B_G\) the coefficient of the gauge contribution to \(\beta_{c_2}\) in units of \(w\) (\(B_G=0\) for \(u(4)\), \(1/16\) for \(su(4)\)), \(\beta_{c_3}=c_3^2(256+192r+4w-4v_4)/(32\pi^2)\), \(\beta_{c_2}=c_3^2(96+512r+640r^2+B_Gw)/(32\pi^2)\), and \(\beta_r=c_3P(r)/(32\pi^2)\) with \(P(r)=448r^2+(256+4(v_4-w))r+96+B_Gw\).
Renormalizable Yukawa couplings enter through \(\operatorname{Tr}X^2\) only (single cyclic-word identity), so \(P(0)=96+B_Gw>0\) is fermion-independent, the slice \(c_2=0\) is not a fixed ray and not an infrared attractor, and real fixed rays exist if and only if \((w-v_4-64)^2>10752+112B_Gw\): at \(B_G=v_4=0\) none occur for \(0\le w\le 64+16\sqrt{42}\approx167.7>16\pi^2\), and off-window at \(w=200\) the two exact rays are \(r=3/14\) and \(r=1\).
The \(c_1\) direction is scheme- and content-dependent: a sharp cutoff generates \(\delta c_1=(\Lambda^2/64\pi^2)(64c_3+136c_2+\ldots)\operatorname{Tr}X\) with the omitted gauge-ghost and Yukawa terms of content-dependent sign (bosonic loops positive, fermionic negative), Pauli--Villars replaces the quadratic sensitivity by a finite regulator-spectrum datum, and in a mass-independent minimal-subtraction scheme \(\beta_{c_1}=c_1\gamma\) carries no additive term, so \(c_1=0\) is an exact renormalization surface rather than a derived value.
The constant-\(\Theta\) Moyal structure generates no potential either: every \(p\)-th star term carries at least one derivative on each factor, so at zero gradient the star potential collapses to the ordinary potential to all orders, the \(O(\Theta)\) correction being a total derivative and the \(O(\Theta^2)\) correction a pure derivative operator.
Scope: within this hypothesis class (tree-level Presentation~A with unspecified matter term or minimal shift-symmetric lift, a local Presentation-B potential \(W(X)\) for \(n=4\) bifundamental scalars, renormalizable gauge and Yukawa couplings, group choice as input, fixed-\(\Theta\) deformation, one-loop accuracy) these computations constrain but do not select the slice of Equation~\eqref{eq:V}; closing the selection would require an explicit \(S_{\mathrm{matter}}\) or lift, or a specified group, fermion content and ultraviolet boundary condition on \((c_3,c_2,c_1)\) at the cutoff \(\LUV\) of Equation~\eqref{eq:LUV-def}, or a non-renormalizable double-trace completion, none of which Equation~\eqref{eq:Smatrix} supplies; a dynamical-\(\Theta\) or strongly coupled branch is not evaluated here, and none of the listed data, if specified, is excluded from realizing the slice.
The selection of Equation~\eqref{eq:V} by Presentation~A therefore remains an input of the matching discussed in Section~\ref{sec:ch3-relate}: it is constrained but underdetermined as datum, and nothing in this paragraph closes Problem~D, Problem~D1, or Problem~A.
```

**No other manuscript file changes. No bib entries. No code changes.**

## Verification scripts
All in this folder (reproduction pack - re-run commands and expected invariants):
1. `python -I -B verify_r119.py` -> expect sections A,H,B,C,D,E,F,G with all-PASS, the
   informational `D9 general-n strong-coupling threshold w*(n)` line (n=2:115.88, n=3:143.64,
   n=4:167.69, n=5:189.58, n=6:209.98; 16 pi^2 = 157.91), `TOTAL 62/62 PASS` and
   `ALL CHECKS DONE 119`; byte-identical to `out-r119.txt` (raw capture). History: an earlier
   raw run recorded 59/61 with two CHECK-SIDE bugs (D4 grid point (0,60) not interior to its own
   antecedent; G3 comparing a scalar to `sp.zeros(2,2)`); both fixed in the script, the failed
   raw capture is kept unedited as `out-r119-run1-fail.txt`, and the fresh run above is 62/62
   (61 original checks + new companion check G3b). No payload text changed. Key invariants:
   `A1` slice identity (generic 4x4 X); `B1` tensors n=2..6 residual 0; `B2` `(256,96)`, `3/8`;
   `C2/C4` `(n,0)`, `(n-2/n,1/n^2)`; `C5` `(1,1/4)`; `C8` `0` vs `1/56`; `C9` control fires;
   `D2` `P(0)=96+B_G w`; `D3/D3b` discriminants (BG=0 and general BG); `D5` `r*=sqrt(42)/14`;
   `D6` `64+16 sqrt42 > 16 pi^2`; `D7` `{3/14, 1}` at `w=200` (OFF-DEFAULT two-root regime tooth);
   `D10a/D10b` payload beta-function channels reproduced exactly from the n=4 tensors;
   `F3` `K3=64,K2=136`; `F4/F5` `C_u(n)=n`, `C_su=(n^2-1)/n`; `G1` collapse 0;
   `G2` p=3 term kills quadratic Phi; `G3/G3b` zero-gradient parts of the theta^2 and theta
   coefficients of W_star exactly 0 (scalar-zero comparisons).
2. `python -I -B gen_payload_119.py` (twice; second run asserts byte-identity) ->
   `payload bytes: 4704  sha1[:12]: 3b4c2d0794a9`,
   `POST: 848355 (= 843649 + 4704 + 2)  full sha1: eaea0964e7f50c27c24540b9ac523c443af873d7`,
   `GEN OK 119`. Includes join guard `r'\\[A-Za-z]+$'` with positive control (injected
   `\secti` fragment FIRES) and negative control, hygiene asserts (CR=LF, ends CRLF, ASCII,
   no tab/BOM/`$`, no `\label`/`\cite`, brace and `\(...\)` balance), live baseline pins and
   independent POST reconstruction.
3. `python -I -B cert-r119p.py` -> `PRE-COMPILE PINS OK ...`, `PASS 1: rc=0`, `PASS 2: rc=0`,
   zero `!` error lines, zero undefined/multiply-defined references in pass 2, `CERT PASS`,
   `temp tree removed`; raw capture `out-cert-r119p.txt` (`CERT-EXIT=0`). Compile tree: fresh
   out-of-repo temp dir from tracked working bytes minus `namcg-book7.pdf` and `reports/`,
   plus the working `namcg-book7.bbl` (2945 files; root PDF excluded); tree deleted after.

## Decisions Taken
- Restricted all "no fixed ray" statements to exact derived criteria (discriminant condition;
  n=4 window `64+16 sqrt42 > 16 pi^2`) and recorded the general-n thresholds including
  `w*(2), w*(3) < 16 pi^2`, rejecting the stage-2 blanket "for any N" as not exact; the
  within-payload claim is therefore unconditional inside its hypotheses. Rejected alternatives:
  dropping general-n (loses transfer data for other n), keeping the blanket (overstatement).
- Kept "not an infrared attractor" with the exact witness `P(0) = 96+B_G w > 0` (r=0 not
  stationary) rather than the stronger flow picture (which needs UV-completion assumptions).
- Spelled "mass-independent minimal-subtraction scheme" in words (book uses no `\overline`
  anywhere; grep count 0), avoiding an unproven macro dependency.
- Single additive `\emph{}` paragraph before `\section{Problem E: signature}` (118 register)
  rather than a new subsection or status passage edit (rule: smallest accurate text; no label
  changes).
- Added verifier checks D3b, D10a, D10b after drafting the payload so that EVERY numeric claim
  in the payload traces to a green check (payload-beta formulas <-> tensor identity bridge).
- Verifier run-1 FAILs diagnosed as check-side, not math: D4 asserted for a grid point outside
  its own interior antecedent ((0-60-64)^2 = 15376 > 10752; replaced by (0,30), interior); G3
  compared the scalar trace to a matrix (always False; the theta^2 and theta zero-gradient parts
  are exactly 0, confirmed standalone and by patched checks G3/G3b). Fixing the checks rather
  than weakening them: D4 now states all 8 grid points satisfy the antecedent, and G3b was added.
- 118 record fixes executed in the 118 folder per dispatch: superseded copy preserved
  byte-for-byte (`proposal-r1-superseded-F1F2.md`, sha1[:12] 4a6fa455daa2, 48887 B = pin),
  then F1 `x = (1/(2eps),0,0,0)` -> `x = (1/sqrt(2 eps),0,0,0)` and F2
  `y^2 = -c1/(2(c3+k c2))` -> `sigma^2 = w^2 = -c1/(2(c3 + k c2))` (counts 1 each; D7 and D5
  locations per review-r1 findings 1-2); `proposal-r1.md` now sha1[:12] b6c55d51a73f, 48902 B;
  old/new pins recorded in the 118 `manifest.md` section 10 (the manifest's section-1 table row
  keeps the old pin and is superseded by section 10, left unedited).

## Milestone assessment
Routine. Bounded negative result + datum list; no milestone trigger (no critical-path step
derived, no missing link closed without new inputs).

## Status-label recommendation
None. Re-derived current critical-path list (ch17 full-GR criterion + appH ledger): A, B, C, D1,
E, F, G-derived, N; Problem D remains OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL; D1, A
unchanged. This package proposes no label edits and closes nothing.

## Author decision needed
None. (The missing-datum decision is recorded as research content under "Remaining open step";
it changes no definition, scope statement or label, and spacetime remains emergent throughout.)

## Remaining open step
Exactly one datum (or a derivation replacing it) is still needed to close the selection target:
(1) an explicit `S_matter` (or a specified non-minimal lift of `eq:Smatrix`) whose tree level
produces `W(X)`; or (2) specified group choice + fermion content + a UV boundary condition on
`(c3,c2,c1)` at the cutoff `LUV` (eq:LUV-def) shown to survive to the infrared; or (3) a
non-renormalizable (double-trace) completion whose induced flow fixes the slice; or (4) a
strongly-coupled / dynamical-Theta branch (not evaluated here, outside the tested class). None
of (1)-(4) is supplied by `eq:Smatrix` as recorded, and none is excluded by this package.
The no-go is bounded by its hypotheses: tree level with the minimal lift, one-loop accuracy,
`n=4` bifundamental scalars, renormalizable gauge+Yukawa content, fixed Theta, and the four
schemes computed.

## Special instructions for the gatekeeper
- The payload closes NOTHING and must not be summarized as "eq:V is not selected by the matrix
  theory" beyond the stated hypothesis class; the correct reading is "underdetermined as datum
  within the class; gate moved to datum decision".
- Must NOT be asserted: any closure or label change for D/D1/A; that higher loops or
  nonperturbative dynamics cannot select the slice; that the group choice is wrong/right - the
  payload uses the ratio difference `0` vs `1/56` only as evidence of datum-hood.
- Re-check first: D7 exact roots at `w=200` (off-default two-root tooth), C9 control semantics,
  D5 threshold double root, F6 sign tooth, the generator positive control actually firing
  (temporarily flip the control to a clean string to see the assert fail), and the cert PRE-COMPILE
  pins against the live baseline (anchor may move if another chain integrates first - the cert
  recomputes pins itself and will fail loudly if the tree moved).
- Report, not fix (dispatch): repo-root `out-q4.txt` is a stray failed-run traceback (left
  untouched); `scratch/119/out-s7-m1.txt` is stale w.r.t. its script (fast-path output is
  `out-s7-m1b.txt`); stage-2 note "no fixed ray ... for any N" needed the n=2,3 qualification
  handled above.
- Verifier history: run 1 = 59/61 (raw, kept as out-r119-run1-fail.txt) with the two check-side
  bugs in Decisions Taken; run 2 = 62/62 (raw out-r119.txt). Verify the run-2 FAIL-absence and
  that the D4/G3/G3b messages match the patched script; the payload bytes never changed between
  runs (payload pin 3b4c2d0794a9 in both generator and cert).
- 118 folder changes in this round were record-only (two literal replacements + supersession
  copy + manifest section 10); verify the supersession copy hashes to the pinned pre-edit
  record and that no other byte of `proposal-r1.md` changed.
