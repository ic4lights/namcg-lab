# Proposal local-gpu/062-064-r2, round 2

Joint revision of three gpu-line items (gpu numbering, not this branch's): gpu 062 block 2, gpu 064 and gpu 062
block 1. This is item 4 of `reports/pathfinder/plan-2026-11-21.md`. It replaces, for integration on this branch,
`proposals/local-gpu/062-c-scalar-tadpole-nonderivative-obstruction/insert-r2.tex` (both blocks) and
`proposals/local-gpu/064-f-fibre-level-response-q0-trace/insert-r1.tex`. Those texts are VOID for integration.
The texts to apply are `block_C_r2.tex` and `block_F_r2.tex` in this folder.

## Result

1. **062 block 2 and 064 are merged into one new Problem F paragraph, built in the channel of the recorded reduced
   form.** Re-derivation shows that the gpu texts used a channel the recorded forms do not use. The recorded static
   channel at large tau runs along `y^mu y^nu`, with `hbar^{11} ∝ ½β_K(1-g) → 0`. It is not the pure-trace direction
   `hbar ∝ gammabar`. In the recorded channel the rigidity of appH holds as recorded (`Tbar^{abmu} y_mu = 0`). So the
   group4 M3 objection, that the rigidity fails, is met by using the right channel. No caveat is needed.
2. **Established identity (exact for the recorded forms, at operators with c_3 = mu = 0 and V = T).** At a
   background that is stationary in this channel at q = 0 (`Σ T_i = 0`), the first-pole denominator of the
   vacuum-term display is
   `q^2 - q_b^2 + q_*^2 = q^2 + (L/2m^4) Σ_i (C_i - T_i) + q_*^2|_chi`.
   Here every term that carries sqrt|g| alone drops out. This includes U_4 and any term of the cosmological type,
   and hence the term -q_b^2. The right-hand side does not depend on the parametrisation at `Σ T = 0`, while each
   C_i alone does. This corrects the gpu 062 statement "the pole sits at q^2 = q_b^2". Cancelling the tadpole with
   sqrt|g|-alone terms also cancels -q_b^2.
3. **Bounded obstruction.** The recorded identities give `q_*^2|_chi = -L U'_loop^2/(4m^4 U_chichi) < 0` at a local
   minimum. A Yukawa first pole at a stationary background therefore needs a positive profile deviation
   `Σ(C_i - T_i)` from terms that do not carry sqrt|g| alone. Within the recorded content these are:
   - the second-order parts of U_2 and of the fibre-constant part of the first term;
   - the fibre-flux part of the first term.

   None of these is computed. If they are set to zero, the first pole has the tachyonic sign.
4. **vartheta, resolved consistently for both blocks.** In the recorded channel, vartheta does not respond at
   first order (recorded rigidity). The 064 reading "vartheta = -y.y/m^2 in the fluctuated metric" would move
   vartheta along `y^mu y^nu`, by `δ ln vartheta = -ε y.y`. That contradicts the rigidity, so this reading is
   excluded there. Along the pure-trace direction the response is a hypothesis, `δ ln vartheta = p sigma_1`:
   - p = 0 extends the rigidity;
   - p = ½ is the excluded reading.
5. **064 has been shrunk.** It cannot be rescued as derivation-grade input to q_*^2, because its channel is not the
   reduced one. What survives, with derivation-grade status:
   - the regulated density of the first term, `-(sqrt|g|/32π^2) Σ(2J+1)[(15/4)vartheta^2 E_1(s_Λ D) - vartheta c_J/D + c_J^2/D^2]`, whose ln chi derivative is the recorded Y;
   - under the hypothesis, its extra first-order part `-p(...)[(15/2)vartheta^2 E_1 - vartheta c_J/D]`. Its sign depends on the regulator (numerical sign change at s_Λ D ≈ 3 for the sampled level);
   - the finite t-response of Y.

   I have removed the sign claim, the ds/s sentence and the gpu quadratic coefficients, which were computed on the
   Y bracket.
6. **062 block 1** (Problem C "Missing step"): M1, m1 and m2 of group2 are applied verbatim in substance. The final
   clause now points to the new F paragraph ("static scalar channel", `Section~\ref{sec:status-F}`).

Nothing is closed. Problems C, F and N remain OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL. No label change.

## Target and status

Re-read in the current tree (appH sha a7f1492a…):
- **Problem C** (appH L551-554): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. A
  scalar-tensor result is a reduced-scope outcome only when its operator, coupling and phenomenological test are
  supplied; it does not by itself meet the matrix-derived criterion." ch17 L139-157 (target) and L708-711
  (criterion: "computed scalar operator, coupling, and phenomenological comparison defining and testing either a
  sufficiently heavy m_psi or the scalar-tensor outcome; Assumption gap-psi discharged").
- **Problem F** (appH L1824-1828): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL.
  Reduced-scope result: treating G_eff as an input leaves F OPEN …". ch17 L403-412 (target: the weighted a_1 and the
  curvature-linear a_2 on the locked block, with ghosts, thresholds and scheme) and L717-719.
- **Dependencies** (ch17 L267-268, appH C entry): C and F are tied through G_eff. D1 gates both (plan file; ch17
  L650-653). F gates N.
- **Discrepancies.** None in the labels. One ordering point: ch17's order list places "Problem C: compute the
  tree-level scalar operator" before F. This package bears on the static scalar channel of the F class, and both
  C and F record it. That is consistent.
- Classification of this package: **PROGRAMME-CONDITIONAL** (conditional identities in a supplied class). Not
  DERIVED.

## Source reading

Digest + targeted reads. `make_digest.py --check` printed DIGEST CURRENT. The digest has `dirty-chapters: yes`,
which is expected for the uncommitted working tree. I reviewed against the working-tree bytes, sha a7f1492a….

Read in full:
- appH:
  - Problem C entry L548-712;
  - Problem F ledger and Missing step L1821-1842;
  - the F paragraphs L2918-2948 (fibre-point forms), L2949-3005 (response of the scale of K, as qualified by
    local 069) and L3006-3046 (Hessian of a tree stabiliser, local 069).
- ch17: L135-160 (C), L260-272, L403-430 (F), L640-735 (order and criterion).
- Other chapters: ch04 Definition def:vierbein and the following remark; ch03 L255-300 (ass:frame-lock,
  eq:Phi-transform, "not derived from Presentation A alone"); ch07 L30-40 (h = T + ¼ηψ) and L110-126 (the ψ
  dependency of C).
- Packages and reviews: group4 sections "062 block 2" and "064"; group2 section "062 block 1"; gpu 062
  proposal-r2/review-r2 (heads); gpu 064 review-r1; both gpu insert texts; the reference copy
  `scratch/integrator-backup/gpu-import-full/chapters/appH-microscopic-proofs.tex` L3018/L3020 and L685
  (placement).

No full scan. Protocol 3(c) may apply to block C, because a "Missing step" paragraph restates the problem's
target. The text does not change the target, status or scope. It restates ch17's target and criterion, and I
checked it against ch17 L139-157 and L708-711. I flag this for the gatekeeper (see special instructions).

## Research and reasoning

### R1. Which channel the recorded reduced form uses
Recorded (scale-of-K paragraph, "Scalar channel"): at ϱ = 1,
- `hbar^{00}`, `hbar^{11}` and t are proportional to `(2-β_K)g`, `½β_K(1-g)` and `β_K - 2g`;
- `1-g ≃ 2/sinh^2 τ`.

At `y^i = 0`, y is along e_0. So at large τ the wave is `hbar^{00}`, which is along `y^mu y^nu`. The relation
`t = -hbar^{00} + 2 hbar^{11}` reproduces `β_K - 2g` exactly. The recorded rigidity ("Since `Tbar^{abμ} y_μ = 0`, a
perturbation along `y^μ y^ν` leaves the Gaussian average over the loop momentum unchanged") therefore applies to
the channel in which `q_*^2 = 2ML` is defined.

The gpu texts instead took `h_{μν} = (t/4) gbar_{μν}`. That is the pure-trace direction, a different direction
from the recorded one, and the group4 M3 objection is correct for it. Choosing the right channel removes the
objection at its source. The verify script (S5) checks the rigidity algebra: for `Tbar y = 0`,
`Tbar(γ + ε y y^T)Tbar^T = Tbar γ Tbar^T` exactly, to all orders in ε.

### R2. Parametrisation and recorded conventions
The recorded forms satisfy three relations:
- `sqrt|g_n| = m^{-4}(1+x_n)^{-1}`, with x_n linear in the frame amplitude;
- the reduced form `S_E = (q^2/4L)t^2 + ½ M t^2` with `q_*^2 = 2ML` is a phase average, so a local term `c t^2`
  gives M = c;
- the Hessian paragraph uses "U_4 σ_1^2", with `σ_1 = -t/2m^2`.

I checked these against each other (S2):
- `U_4 σ_1^2` gives `2ML = U_4 L/(2m^4) = -q_b^2`, with the recorded `q_b^2 = 12Ûχ^2/(m^2(V̂+2T̂))`,
  `L = 32π^2 m^6/A` and `A = F(V̂+2T̂)χ^2/24`;
- the χ exchange gives `-β_K U' L/(8m^4)`, as recorded;
- the recorded relation `q_*^2|χ = β_K U'/(4U_4) q_b^2` holds.

So in the recorded parametrisation `sqrt|g| = sqrt|gbar|(1 + σ_1 + σ_1^2 + …)` and a local `C σ_1^2` shifts the
pole by `(L/2m^4)C`.

**Correction to gpu 062.** The gpu magnitudes ("M = F sqrt|g| Û χ^4/256π^2", "q_*^2 = 6 sqrt|g| Ûχ^2 m^6/(V̂+2T̂)",
"ratio sqrt|g| m^8/2", "|T| = FÛχ^4/(32π^2 m^8)") used two things at once:
- the metric-trace variable t_062, which is `-t/m^2` at first order;
- the coefficient of t^2 as ½M rather than M, together with the recorded L.

They are therefore not in the recorded convention. They also depend on the parametrisation when the tadpole is
not cancelled (S1): for the same first-order channel, C/T is 1/4 (metric), 3/4 (inverse metric), 1 (frame rank
one, as recorded) or 1/2 (conformal φ). Under `σ → σ + aσ^2`, `C → C + aT`. These magnitudes are dropped.

### R3. Identity at a stationary background (derivation)
Write the q = 0 non-derivative density at fixed χ as `Σ_i (T_i σ_1 + C_i σ_1^2)`.
- Stationarity in the channel is `Σ T_i = 0`. The tree term carries ρ_M, and `δρ_M = 0` because the wave changes
  sqrt|g| at fixed ρ_M (φ = ½ ln(ρ_M/sqrt|g|), δφ = t/4m^2, as recorded). Stationarity in χ is separate.
- The first-pole denominator is `q^2 + (L/2m^4)ΣC_i + q_*^2|χ` (R2). Using `ΣT = 0`, `ΣC_i = Σ(C_i - T_i)`.
- In the recorded parametrisation a term `w sqrt|g|` with w not responding to the wave has `C = T = w sqrt|gbar|`,
  so it drops out.
- Under `σ → σ + aσ^2` the sum shifts by `aΣT = 0`. It is invariant (S3).
- With U_4 and a term `Λ sqrt|g|` alone, `Λ = -U_4` and the pole shift vanishes: -q_b^2 is cancelled (S3).

A χ-independent Λ does not change `U'_loop` or `U_χχ`, so β_K and q_*^2|χ are unchanged. From
`β_K = 2U'/U_χχ`, `q_*^2|χ = -L U'^2/(4m^4 U_χχ)` (S4), which is negative at a local minimum with U' ≠ 0. At a
χ-stationary point `U'_loop = -∂(ρ_M V_t/g^2)/∂ln χ`, which is nonzero for the recorded tree quartic.

**What is and is not covered.** Exactly, U_4 and cosmological-type terms carry sqrt|g| alone. At first order,
U_2 and the fibre-constant part of the first term do so too, by the recorded rigidity; their T_i are therefore
w_i sqrt|gbar|. Their C_i are second-order parts and are not computed (the Hessian paragraph records "plus the
second-order parts of U_2 and of the first term … not computed"). The rigidity argument (S5) is exact in ε for the
averaged `hbar` along yy. But the recorded forms are fibre averages of fibre-point expressions, and the
perturbation at a fibre point is along v, not y. So I do not claim C_i = T_i for U_2 and the first term. The
fibre-flux part of the first term (c_J, μ_J) is not covered by the recorded rigidity, which names "the
fibre-constant part of Y".

### R4. vartheta
appH L2899 records `vartheta = -y·y/m^2` off `y^i = 0`, which is a background function of the base point. It
enters U_2 (`R/6 + E_0 = 2 - ¾ϑ`, index density -6ϑ) and the first term through background torsion and
curvature contractions. Those enter through the loop Gaussian average, which the rigidity leaves fixed along yy.

Reading `y·y` in the fluctuated metric gives `δ(y·y) = -ε (y·y)^2` for `δγ^{μν} = ε y^μ y^ν` (S5). This is
nonzero, so that reading contradicts the recorded rigidity in the recorded channel and is not the response of
these densities. It is therefore excluded there. 064's implicit position (vartheta moves) and 062's implicit
position (vartheta held) are reconciled as follows:
- in the recorded channel, vartheta is held by the rigidity; this is established, given the recorded rigidity;
- along the pure-trace direction it is the hypothesis `δ ln ϑ = p σ_1`. The contraction reading gives p = ½ for
  both metric and inverse-metric pure trace (S8); p = 0 extends the rigidity.

### R5. 064 re-derived
The level form recorded in appH (fibre flux in the first term) is the average integrand `s^2[15/4 ϑ^2 - sϑc_J + s^2 c_J^2]`.
The Y display has the bracket `15ϑ^2/(4D) - ϑc_J/D^2 + 2c_J^2/D^3` with `D = M_A^2 + μ_J`, and
`dD/dln χ = 2M_A^2`.

The density whose ln χ derivative is Y comes from `∫_{s_Λ}^∞ ds/s e^{-sD}[…]`, which equals
`(15/4)ϑ^2 E_1(s_Λ D) - ϑc e^{-s_Λ D}/D + c^2 e^{-s_Λ D}(1+s_Λ D)/D^2` exactly (S6). Then:
- `d/dD → -(Y bracket)` as `s_Λ → 0`;
- the prefactor is `-(sqrt|g|/32π^2) Σ(2J+1)`, fixed by Y's display and its sign;
- the fibre-constant limit reproduces `Y = 15F ϑ^2 sqrt|g| N_K/64π^2`.

This agrees with the group4 statement. Under the hypothesis, with sqrt|g| responding as `e^{σ_1}` at first order
(S7):
- the extra first-order part is `-p(sqrt|g|/32π^2)Σ(2J+1)[(15/2)ϑ^2 E_1 - ϑc_J/D]`;
- at ϑ = 1, D = 10, c = 2 the bracket is 47.3, 13.5, 1.45, 0.167 and -0.102 at `s_Λ D` = 0.001, 0.1, 1, 2 and 3,
  so its sign depends on s_Λ;
- U_2 at V = T is ϑ-linear (as recorded, `-(3F/128π^2)ϑT̂ sqrt|g|χ^2`), so its extra part is `p U_2`;
- the t-response of Y is `(sqrt|g|/32π^2)(2J+1)2M_A^2[(1+2p)15ϑ^2/(4D) - (1+p)ϑc/D^2 + 2c^2/D^3]` (S8), which is
  finite.

Group4's numbers are reproduced at p = ½ in t_064 = 2σ (S9): `ϑ(15ϑDE - 2c)/(8D)` and `ϑ(75ϑDE - 8c)/(64D)`. I do
not put the quadratic coefficient into the text. It is parametrisation-dependent at an uncancelled tadpole (R2),
and it needs a second-order response hypothesis.

**Why 064 cannot be rescued as derivation-grade input to q_*^2.** Its channel is not the reduced one (R1), and in
the reduced channel its ϑ-response is zero (R4). It also holds μ_J, which is exactly the "response of the fibre
levels to hbar" that is recorded as not computed. It does not compute that item and must not be described as
retiring it; the gpu closer "retire the recorded item … for this channel component" is dropped.

### R6. 062 block 1
I checked every claim in it against the source:
- eq:Phi-transform is "a choice of field content … not derived from Presentation A alone" (ch03);
- the remark after def:vierbein ("A corrected Repair I would need additional background tensors or an
  independent coframe, which is part of Problem C") is present;
- the ψ dependency is in ch07 L123-124;
- ch07 L36 has `h = T + ¼ηψ`, so ψ is the trace of the metric fluctuation (m2).

Changes applied:
- M1: the ch17 phenomenological clause, verbatim in substance;
- m1: "are not derived";
- m2: "the trace of the metric fluctuation h_{μν}".

I also replaced "mode labels of K" by "the amplitude ψ of the modes ψΛ_A of K", which is the recorded usage in the
scale-of-K paragraph. The last clause now refers to the "static scalar channel" and `Section~\ref{sec:status-F}`.

**Literature.** None is cited or needed. The package adds no citation.

## Claim classification

| # | Claim | Class |
|---|---|---|
| 1 | Recorded channel at large τ is along `y^μ y^ν` (`hbar^{11} ∝ 1-g`) | established (from recorded forms) |
| 2 | Rigidity algebra `Tbar(γ+εyy)Tbar^T = Tbar γ Tbar^T` for `Tbar y = 0` | established (identity; S5) |
| 3 | Recorded conventions: `U_4σ_1^2 ↔ -q_b^2`, `C σ_1^2 ↔ (L/2m^4)C` | established (consistency of recorded forms; S2) |
| 4 | Identity `q^2 - q_b^2 + q_*^2 = q^2 + (L/2m^4)Σ(C_i - T_i) + q_*^2|χ` at `ΣT = 0`; parametrisation invariance | conditional (exact within the recorded class at c_3 = μ = 0, V = T, one loop, frozen symbol) |
| 5 | sqrt|g|-alone terms (U_4, cosmological type) drop out; cancellation removes -q_b^2 | conditional (as 4) |
| 6 | `q_*^2|χ = -LU'^2/(4m^4U_χχ) < 0` at a local min | conditional (from recorded β_K and exchange) |
| 7 | A Yukawa first pole needs positive profile deviations from the uncomputed terms; with them zero it is tachyonic | conditional / bounded obstruction |
| 8 | ϑ held at first order in the recorded channel; the fluctuated-metric reading is excluded there | conditional (on the recorded rigidity) |
| 9 | `δ ln ϑ = p σ_1` along the pure-trace direction | input (response hypothesis) |
| 10 | Regulated first-term density with `E_1(s_Λ D)` | established for the recorded level form (exact integral; S6), conditional on that level form |
| 11 | Extra first-order part under 9; its regulator-dependent sign | conditional (on 9); the sign change is numerical |
| 12 | t-response of Y (finite) | conditional (on 9) |
| 13 | gpu 062 magnitudes and "pole at q_b^2" | corrected: dropped (convention mix; wrong at stationarity) |
| 14 | Block 1 restated target (ch17-consistent) | established (restatement of the source) |
| — | second-order parts of U_2 and the first term; level response; W_R term; p | unresolved |

## Proposed changes

Only `chapters/appH-microscopic-proofs.tex`. There are two pure insertions, nothing is deleted, and no label is
added.

### Change 1: Problem C, new `\paragraph{Missing step.}`
- **Anchor**, unique in the current appH, checked by count in `apply_and_build_r2.py`: the bytes
  `tensor operator or the remaining scalar couplings.\r\nProblems~B, C, D, F and~G remain open.\r\n\r\n\section{Problem D: local Lorentz}`.
- **Insertion**: `\r\n\r\n` + `block_C_r2.tex`, placed directly after "the remaining scalar couplings."
- **What stays**:
  - the existing closer "Problems~B, C, D, F and~G remain open." now follows the new paragraph on the next line,
    so it is the single status sentence of the block;
  - the mixing block above is kept unchanged.
- **Labels used** (each defined exactly once, checked by the script): `ch:agenda`, `ass:gap-psi`,
  `eq:Phi-transform`, `def:vierbein`, `ass:nondeg`, `ass:frame-lock`, `eq:Z-sigma`, `ch:massless-tensor`,
  `lem:msigma`, `sec:status-F`.

```latex
\paragraph{Missing step.} The full target of Problem~C is the gauge-fixed quadratic scalar operator on the locked vacuum in a constructed frame: the canonically normalised kinetic coefficient of the pure-trace scalar, including the induced Einstein--Hilbert term, its mixing with \(T_{\mu\nu}\), its non-minimal curvature coupling, its matter coupling, and its pole mass as a derived output, and the phenomenological comparison of Chapter~\ref{ch:agenda}, defining and testing either a sufficiently heavy \(m_\psi\) or the scalar-tensor outcome, with Assumption~\ref{ass:gap-psi} discharged. On the bare data of Presentation~A this operator is not yet definable: three of the inputs it needs are not derived. (i)~A frame. [...] (iii)~The constraint structure of the massless sector. [...] the \(\psi\) of Chapter~\ref{ch:massless-tensor} is the trace of the metric fluctuation \(h_{\mu\nu}\), distinct from the amplitude \(\psi\) of the modes \(\psi\Lambda_A\) of \(K\) in the Problem~F entry. [...] and in the conjugate-coordinate class the \(q=0\) non-derivative sector of the static scalar channel carries a bounded obstruction recorded in Section~\ref{sec:status-F}.
```
The full text is in `block_C_r2.tex` (2594 B, sha256 `cb0aeb6c…faacb8`). The elisions `[...]` above are
byte-identical to gpu 062 block 1, apart from m1, m2 and the K wording.

### Change 2: Problem F, new paragraph before `\section{Problem G: HBEV}`
- **Anchor**, unique: `Problems~C, F and~N remain open and PROGRAMME-CONDITIONAL.\r\n\r\n\section{Problem G: HBEV}`.
  This is the closer of the local-069 Hessian paragraph.
- **Insertion**: `\r\n\r\n` + `block_F_r2.tex`, after that closer.
- **What stays**: all of the existing text, and the 069 paragraphs are untouched.
- **Consistency with 069**:
  - the setting states "the operators at c_3 = μ = 0", the qualifier 069 introduced;
  - the exchange term q_*^2|χ and the `U_4σ_1^2` form are taken from 069's "Exchange of the scale of K";
  - the scope line lists "the term of U_2 proportional to W_R", which 069 records as not computed.
- **Labels used**: `ch:vierbein-emergence` (one definition).

The full text is in `block_F_r2.tex` (7046 B, sha256 `d2f0a7dc…393d0b`). It has one `\paragraph`, two `\emph`
sub-blocks, a scope line and one closer: "Problems~C, F and~N remain open and PROGRAMME-CONDITIONAL." Its
displayed equations are:

```latex
\[
q^2-q_b^2+q_*^2=q^2+\frac{L}{2m^4}\sum_i\bigl(C_i-T_i\bigr)+q_*^2\big|_\chi ,
\]
...
\[
-\frac{\sqrt{|g|}}{32\pi^2}\sum_A\sum_{J\le n}(2J+1)\Bigl[\tfrac{15}{4}\vartheta^2E_1(s_\Lambda\mathcal D)-\frac{\vartheta c_J}{\mathcal D}+\frac{c_J^2}{\mathcal D^2}\Bigr],
\]
```

**Stale passages elsewhere.** None in the current tree. The gpu 062 and 064 texts are not in the tree. The
recorded sentence in the scale-of-K paragraph, "The tree non-derivative terms, the terms that cancel the tadpole
of U_4 at q = 0, and any term with the same fibre dependence are not computed, and a long-range form needs them
or Û→0", remains true. The new paragraph refines it for the first pole only, and I propose no edit to it.

**Post-state** (simulated on bytes): appH 743323 B, sha256
`112b485c75518bd63eb7495a5ade2bced80028b6bbe05fab6ce7c6cebaeee07f`, CRLF 3647, bare LF 0. The pre-state is
733675 B, `a7f1492a…`, CRLF 3628.

## Verification scripts

All are in `proposals/local-gpu/062-064-r2/`:
- `verify_r2.py`: sympy and mpmath checks S1-S9 (listed in its docstring). Output is in `verify_r2_output.txt`.
- `make_snippets_r2.py`: writes the CRLF snippets and prints their sizes and hashes. Output is in
  `make_snippets_r2_output.txt`.
- `apply_and_build_r2.py <repo> <scratch>`:
  - asserts the pre-hash, the uniqueness of both anchors, CRLF-only snippets and the post-size, and that every
    `\ref` resolves to one label;
  - copies the repo (excluding .git, proposals, scratch, reports and the book PDF) outside the repository, applies
    the change, runs pdflatex twice, scans the log, and deletes the copy.

  Output is in `apply_and_build_r2_output.txt`.

**Reproduction pack** (from the folder):
```
python -I verify_r2.py            -> last line "ALL CHECKS PASS: True"; S7 bracket list ends (3.0, -0.1021...)
python -I make_snippets_r2.py     -> block_C_r2.tex 2594 cb0aeb6c...; block_F_r2.tex 7046 d2f0a7dc...
python -I apply_and_build_r2.py C:/Users/redgi/Projects/namcg-lab <dir outside repo>
                                  -> pre sha a7f1492a...; post 743323 B sha 112b485c...; CRLF 3647 bareLF 0;
                                     pdflatex passes rc 0; undefined refs/cites 0; multiply defined 0; copy removed
```
Expected invariants: `S2 U4 sigma^2 gives -q_b^2: True`; `S3 sum C = sum (C-T) on sum T = 0: True`;
`S5 covariance … unchanged, all orders in eps: True`; `S6 dG/dD -> -(Y bracket): True`;
`S8 contraction reading gives p = 1/2: True`; S9 reproduces both group4 coefficients.

## Decisions Taken

- **D1: channel.** I rebuilt 062 block 2 and 064 in the recorded y^μy^ν channel rather than patching them with the
  group4 caveat in the pure-trace direction. The reason: q_*^2 = 2ML belongs to the recorded channel, and a
  caveat-only fix would leave a statement about a pole in a channel the pole does not belong to.
  Rejected: (a) applying the group4 replacement sentences verbatim, which keeps the channel mismatch and the
  convention-mixed magnitudes; (b) keeping both blocks separately, which keeps two positions on ϑ.
- **D2: ϑ.** Held in the recorded channel (from the recorded rigidity); a parametrised hypothesis along pure
  trace. This favours the derivation: it states which channel carries the open item, so a later package can
  target the response of the fibre levels and the second-order parts in the right channel.
- **D3: 064.** Kept as the density and the first-order and Y responses only, as the review's options allow
  ("density coefficients with s_Λ stated" and "t-response of Y"). I did not put the quadratic coefficients into
  the text.
- **D4: gpu 062 magnitudes and "pole at q_b^2".** Dropped as convention-mixed or incorrect (R2, R3). The
  convention-free identity replaces them.
- **D5: placement.** One new `\paragraph` after the 069 Hessian paragraph, rather than `\emph` blocks inside the
  scale-of-K paragraph, so that it can rely on 069's exchange term and c_3 = μ = 0 qualifier without
  rewriting 069 text.
- **D6: block 1 placement.** Same as the gpu import: it is closed by the existing C-entry status line.

## Milestone assessment

Routine. This is a conditional identity and a bounded obstruction in a supplied class. No critical-path step is
derived.

## Status-label recommendation

The critical-path set (ch17 L700-735 and Appendix H ledger labels) is A, B, C, D1, E, F, G-derived and N. Affected
labels are C, F and N, all unchanged: OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## Author decision needed

None.

## Remaining open step

To decide the sign of the static scalar pole in this class, a later package must compute in the recorded
y^μy^ν channel:
- (i) the second-order parts of U_2 and of the fibre-constant part of the first term, as profile deviations
  C_i - T_i;
- (ii) the response of the fibre levels μ_J and of the flux insertions to `hbar` in the fibre-flux part of the
  first term, at first and second order;
- (iii) on the cubic branch (V ≠ T), the response of the W_R term.

The ranked avenues, derivation-first:
1. (ii), because the identity shows it is the only term that can shift both the tadpole and the pole away from
   the sqrt|g| profile at leading order;
2. (i);
3. (iii), which depends on 069's regulator issue;
4. pure-trace-direction stationarity (fixing p). This is bottom-ranked: it does not enter the reduced-form pole.

None of these closes F. F also needs the a_1/a_2 target of ch17 L403-412 and is gated by D1 (plan file; ch17
L650-653). Findings that transfer to C: the C-side clause pointing to this obstruction.

## Special instructions for the gatekeeper

- Re-derive R1, the channel: from the recorded `hbar^{00}, hbar^{11}, t ∝ (2-β_K)g, ½β_K(1-g), β_K - 2g`. Check
  that t = -hbar^{00} + 2hbar^{11} fits, and that at large τ the wave is along y y.
- Re-derive R2, the convention chain (S2): `U_4σ_1^2 → -q_b^2`, and the 069 relation for q_*^2|χ. If this chain
  failed, the identity's normalisation (L/2m^4) would need restating. The structural statement (sqrt|g|-alone
  terms drop out at ΣT = 0) does not depend on the normalisation.
- Must not be asserted:
  - that U_2's or the first term's second-order parts are those of sqrt|g| alone;
  - that 064 computes the response of the fibre levels;
  - any value or sign of p;
  - a Cassini or Newtonian statement;
  - any label change.
- Block C restates the target (protocol 3(c) question). Check it against ch17 L139-157 and L708-711.
- The gpu 062 review r2 accepted magnitudes that this package drops. Please confirm R2's argument that they mixed
  t_062 = -t/m^2 and ½M vs M with the recorded L.
- OPEN counts:
  - 062 block 2 M3: addressed by D1/D2; OPEN 0/1 → 0/0 claimed;
  - 064 M3: all four required items addressed (density with s_Λ and Y response; sign claim removed; ds/s deleted;
    "Take as response hypothesis that …"); 0/1 → 0/0 claimed;
  - 062 block 1 M1, m1, m2: applied; 0/1 → 0/0 claimed;
  - new self-findings recorded and acted on: N1 (wrong channel), N2 (gpu 062 magnitudes in mixed conventions;
    "pole at q_b^2" wrong at stationarity) and N3 (the contraction reading contradicts the recorded rigidity).
