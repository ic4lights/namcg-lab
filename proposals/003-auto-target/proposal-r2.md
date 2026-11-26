# Proposal 003-auto-target, round 2

Working title: *Which metric the condensate heat kernel is built on: a scaffold no-go for the induced Einstein-Hilbert and Fierz-Pauli structures of the composite metric (Problem F; consequences for C, B, D1), with the emergent-background operator recorded as a named assumption.*

## Changelog: findings of review-r1.md and 004 Q4/Q6 -> changes

| Finding | Severity | Resolution in r2 |
|---|---|---|
| 1 (ch05 A-dT clause) | major | Reviewer's corrected snippet adopted verbatim (Item 5). The PRIOR-CLAIM-ERROR for ch05 is restricted to the psi-ddT clause. New check: psi-T orthogonality of the kinetic and potential forms (script `check_finite_mu_and_mixing.py`, part B). |
| 2 (ch08 text unqualified; "multiplies no derivative") | major | Every ch08 / appH statement now carries "internal connection held at a background value" and says "no cutoff-dependent term contains a derivative of the condensate". The general "no composite-metric EH term" claim is attributed to Lemma 2 (which covers eliminated connections), not Lemma 1. |
| 3 (finite-term IR limit) | major | Finite mu kept (matches `eq:s-limits`). Both blocks now stated for p^2 << mu^2 << lambda v^2, including Delta Z_K = (lambda^2 v^2/12 pi^2)(mu^-2 - Lambda^-2); script extended and re-run (Item 1, R3). |
| 4 ("enters only through ...") | minor | Reworded as the reviewer asked: "is not produced in this calculation; in the manuscript it arises from the induced Einstein-Hilbert term, that is, from the operator built on the emergent metric." |
| 5 (restricted vs reduced form) | minor | Physical criterion stated as the reduced (Schur-complement) form; lemma statement unchanged. |
| 6 (appB wording) | minor | appB sentence rewritten along appH L72-75 and now points to `ass:emergent-op` for the missing map, not to a proposition. |
| 7 (stale passages) | minor | ch04 Ex. 7, ch08 L56-58 and L363-367, appG L19-29 and appB L110-112 are now proposed rewordings (Items 2-6, from 004 Q6); ch16 is Item 7 (separable, flagged). Remaining optional stale passages are listed, not edited. |
| 8 (Proposition with premise as conclusion) | minor / AUTHOR-DECISION | Decided (autonomy directive, 004 Q4 option 3): `prop:scaffold` is replaced by `ass:emergent-op` plus a remark keeping the counterexample. Recorded in Decisions Taken. |
| 004 Q4, Q6 | - | Integrated. Label `ch:vierbein-emergence` used; `ch:vierbein` and `ch:ultraviolet-placeholder` are not used anywhere. |

## Result

For the displayed Presentation-B action `eq:Smicro` + `eq:V` on the fixed scaffold `g^(0)` (Assumption `ass:aux-metric`) the package establishes the following, and records one merged claim as false.

1. **Lemma 1 (established; conditional on the regularization of `eq:W-again` with the operator built from `g^(0)` and the internal connection `A_mu` held at a background value, not integrated).** The kinetic term is bilinear in Phi, so the fluctuation operator is `-g^(0)mu nu Dbar_mu Dbar_nu + E(Phibar)`, `E` = (1/2) Hess V, with no derivative of Phibar. The Lambda-dependence of `W_E^(1)` is fixed by `a_0,a_1,a_2` up to terms vanishing as Lambda -> infinity, so **no Lambda-dependent term contains a derivative of Phibar** (outside total derivatives). The Lambda^2 curvature term is `eq:universal-R` (with `N_0` = 32) for the **scaffold** metric. For the conformal mode `Phibar = (v+sigma) I` the scaffold Lambda^2 term is `(Lambda^2/32 pi^2) int tr E(sigma)` with `tr E = 16 lambda (v^2 + 4 v sigma + 2 sigma^2)` and has no `(d sigma)^2`, while the operator built on `g = (1+sigma/v)^2 eta` gives `-N_0 Lambda^2 (d sigma)^2/(32 pi^2 v^2)`, the induced term of `eq:Z-sigma`. Replacing `g^(0)` by `g` therefore **supplies** this coefficient; it does not correct a scaffold value.
2. **Finite conformal-mode coefficient (established at one loop; `A_mu = 0` held fixed; limits `eq:s-limits`; p^2 << mu^2 << lambda v^2).** `Delta Z = (3 lambda/4 pi^2)(e^{-lambda v^2/Lambda^2} - e^{-lambda v^2/mu^2}) + (lambda^2 v^2/12 pi^2)(mu^-2 - Lambda^-2)`. The first term (Hermitian block) tends to `3 lambda/4 pi^2` and carries no Lambda^2 or ln Lambda; the second (massless anti-Hermitian block) is an infrared-limit effect, positive, with no Lambda^2 or ln Lambda. Both are positive for mu < Lambda. They do not contain the opposite-sign term of `eq:Z-sigma`.
3. **Lemma 2 (no-go, scoped to its hypothesis class; NOT a no-go for a composite-metric EH term in general).** Hypotheses: (H1) flat scaffold; (H2) regulator and gauge fixing preserving scaffold rotations; (H3) vacuum and background invariant under scaffold rotations; (H4) `h` a fixed linear image of the components of Phi, with the physical criterion the reduced form on `h` (all other components eliminated). Under H1-H4, at any loop order, the quadratic effective action in Phi is a function of p^2 only; a form on `h` invariant under `h -> h + p (x) xi + xi (x) p` vanishes, so no linearized diffeomorphism invariance, no linearized Einstein-Hilbert form and no massless Fierz-Pauli form is generated for the composite metric. A p^2-only form can equal a gauge-fixed EH operator (Feynman-de Donder) but without the gauge symmetry and ghosts all its directions propagate. Each hypothesis is a place where a within-core route can differ: a regulator or kinetic metric built from `Theta^{mu nu}` (Presentation A), a vacuum or background that is not invariant under scaffold rotations, a curved scaffold, or a composite metric that is not a fixed linear image of Phi. None of these is excluded by Lemma 2, and none is shown to work (pointer only; see Remaining open step).
4. **Correction of merged text (PRIOR-CLAIM-ERROR).** (a) The last sentence of `prop:scaffold` ("Self-consistently substituting the emergent metric is therefore valid through the order of this conditional truncated identity") does not follow: by Lemma 1 and the counterexample the replacement produces the entire Lambda^2 emergent-metric coefficient, while the scaffold value is zero. (b) ch05 L249-251 says the surviving mixings after gauge fixing are psi-ddT and A-dT; the quadratic expansion of `eq:Smicro` has no psi-T mixing (ch05 clause restricted to this; the A-dT clause is **not** claimed false, see Finding 1). Corrections take the form of a named assumption `ass:emergent-op` (Decisions Taken).

**Not established:** any value or sign of physical `G_eff`; anything about the A_mu-integrated theory in Lemma 1; anything about Theta-dependent regulators, non-invariant vacua, curved scaffolds, or Presentation A; that the emergent-background operator is wrong as a modelling premise (it is only shown not to be supplied by the displayed action). No problem is closed; no label changes.

## Target and status

Re-derived this round from `chapters/ch17-agenda.tex` (`sec:ch17-done`, L644-720 region; F entry L399-475) and `chapters/appH-microscopic-proofs.tex`; no discrepancy between them found for the rows below.

| Problem | Ch.17 | App H ledger | Role here |
|---|---|---|---|
| F | "CRITICAL PATH; OPEN" | Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL | primary |
| C | CRITICAL PATH; OPEN | OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL | Z_sigma consequence |
| B | CRITICAL PATH; OPEN | OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL | provenance of hyp. 5 of `thm:mT` |
| D (D1) | CRITICAL PATH; OPEN | OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL | structural ingredient |
| A, E, G-derived, N | critical path, OPEN | OPEN, PROGRAMME-CONDITIONAL | not targeted |

- **Original target (F):** "evaluate the weighted a_1 and the curvature-linear part of a_2 on the locked block, including diffeomorphism and local-Lorentz ghosts and the radial-mode threshold, with a scheme stated"; ch17 completion: "A, B, C and the sign/scheme dependence of G_eff computed from the specified operators; G_eff is not an input". G_eff is the coupling of the **emergent** metric.
- **Dependencies:** D1 (operators for omega, A_mu, B, ghosts), A (dictionary), E (signature); C depends on F via `eq:Z-sigma`.
- **Classification of this package:** PROGRAMME-CONDITIONAL; a no-go / dependency resolution and correction of a merged claim; **not** a derivation of F.

## Source reading

Digest + targeted reads. `python scripts/make_digest.py --check` printed `DIGEST STALE` at my run, although `git status` is clean and `chapters/` has not changed since the digest head `eecd202` (hash 41a9a98585142521, as the orchestrator stated); I therefore re-read every range I rely on or edit: appH Problem F ledger and the end of the F section / start of Problem G; ch08 L40-135 (split, `eq:O-eta`, `eq:W-again`, `ass:laplace`, `eq:W-expand`), L135-235 (`eq:universal-R`, `thm:Geff`), L276-305, L355-372; ch04 L410-426; appG L10-35; appB L100-116; ch05 L150-256; ch16 in full (L1-135); ch17 L92-106, L399-475, L655-712; the r1 proposal and review in full; 004 `recommendations-r2.md` and `review-r1.md` in full. A full scan is required for proposals that change a definition, assumption or scope statement; this round introduces a named assumption but I did not re-scan the 30 files: **the r1 full scan (same text for ch01-ch16, appA-appL except the 002 additions in appH Problem N and ch09) and the r1 gatekeeper full scan stand; the gatekeeper should treat this round as "digest + targeted reads" and apply its own 5th-item full-scan rule.** No unreadable files.

## Research and reasoning

### R1. Exact missing step
Unchanged from r1: Problem F's missing step asks for gauge-fixed Hessians for every locked-block field and the weighted a_1. The manuscript's one-block bookkeeping then *assumes* the operator lives on the emergent background (`eq:O-eta`, ch08 L56-58). The question this package answers is whether the displayed action, on its own scaffold, induces an EH term for the composite metric at all. In the class stated in Lemma 1 (Lambda-dependent terms) and Lemma 2 (all orders, class H1-H4) it does not; so the emergent-background operator is not a technical replacement but the source of the induced coupling, and it must be discharged as an assumption of F.

### R2. Lemma 1 (re-verified, unchanged in substance)
Euclidean `S_E = int sqrt(g0) Tr(g0^{mu nu}(D_mu Phi)^dag D_nu Phi + V)`, locked 4x4 complex block, `A_mu = Abar_mu` fixed. With real components `Phi = Phibar + sum_a (h_a + i k_a) T_a`, `Tr T_a T_b = delta_ab`, the kinetic form is `sum (d h)^2 + (d k)^2` (check 1(i)), so `delta^2 S_E = 2(-Dbar^2 + E)`, `E = (1/2) Hess V`. For `I(Lambda) = int_{Lambda^-2}^{mu^-2} ds s^-1 f(s)`, `d_Lambda I = 2 Lambda^-1 f(Lambda^-2)`, so with `f ~ (4 pi s)^-2 sum s^k int a_k`, terms k >= 3 give `d_Lambda I = O(Lambda^{3-2k})` whose integral converges as Lambda -> infinity. The Lambda-dependent part is therefore `-int sqrt(g0)[a_0 Lambda^4/64 pi^2 + a_1 Lambda^2/32 pi^2 + a_2 ln(Lambda^2/mu^2)/32 pi^2]`, with `a_0 = 32`, `a_1 = tr(R0/6 - E)`, `a_2` of `eq:appA-a2`; in `a_2` a derivative of `E` appears only in `D^2 E` (total derivative). The gatekeeper re-derived this (review-r1, "Cutoff dependence"). Scope: fixed `A_mu`, scaffold regulator; no claim for the integrated `A_mu` (that case is covered, for the eliminated-connection class, only by Lemma 2).

Counterexample (flat scaffold, `Abar = 0`, `Phibar = (v+sigma) I`): `g = Omega^2 delta`, `Omega = 1 + sigma/v` (`eq:repairII-trace`); `sqrt(g) R = 6(d Omega)^2 - 6 d(Omega d Omega)` in 4D Euclidean (check 1(iv), sign fixed by R = +12 on unit S^4). The operator on `g` gives `-(32/192 pi^2) Lambda^2 * 6 (d sigma)^2/v^2 = -N_0 Lambda^2 (d sigma)^2/(32 pi^2 v^2)`; with `1/(16 pi G) = N_0 Lambda^2/(192 pi^2)` this is the Euclidean image of the induced term `+3 (d sigma)^2/(8 pi G v^2)` in `eq:Z-sigma` (gatekeeper-verified chain). The scaffold operator gives `(Lambda^2/32 pi^2) int tr E(sigma)`, no `(d sigma)^2`.

### R3. Finite (d sigma)^2 coefficient with the manuscript's infrared limit (Finding 3)
Hessian at `phi0 I`: `E_H = (lambda/2)(3 phi0^2 - v^2)` (x16), `E_K = (lambda/2)(phi0^2 - v^2)` (x16), no off-diagonal entries. At `phi0 = v + sigma`: `E_H(0) = lambda v^2`, `E_H' = 3 lambda v`, `E_K(0) = 0`, `E_K' = lambda v`. Second order of `(1/2) Tr ln`: `W ⊃ -(1/4) sum_b n_b E_b'^2 int sigma(p) sigma(-p) B_b(p)`, with, for limits `s_min = Lambda^-2`, `s_max = mu^-2`,
`B(p) = (1/16 pi^2) int_0^1 dx [ E_1((m^2 + x(1-x) p^2)/Lambda^2) - E_1((m^2 + x(1-x) p^2)/mu^2) ]`.
- Massive block (`m^2 = lambda v^2`): `d_{p^2} B|_0 = -(e^{-m^2/Lambda^2} - e^{-m^2/mu^2})/(96 pi^2 m^2)` (exact; check A). Contribution to `Delta Z` (= 2 x coefficient of `(d sigma)^2` in W; tree value `Z = 2N`, N = 4): `(3 lambda/4 pi^2)(e^{-lambda v^2/Lambda^2} - e^{-lambda v^2/mu^2})`, i.e. `3 lambda/4 pi^2` up to `O(lambda v^2/Lambda^2)` and `O(e^{-lambda v^2/mu^2})` for `mu^2 << lambda v^2`.
- Massless block (`m = 0`): the difference of the two `E_1` terms is analytic at small p^2, `= ln(mu^2/Lambda^2) + x(1-x) p^2 (Lambda^-2 - mu^-2) + O(p^4)`, so `d_{p^2} B_0|_0 = (Lambda^-2 - mu^-2)/(96 pi^2)` for p^2 << mu^2 (exact small-p expansion; numerically checked at four (Lambda, mu) pairs, check A). Contribution: `Delta Z_K = (lambda^2 v^2/12 pi^2)(mu^-2 - Lambda^-2)`. This is **not** a UV coefficient: it is positive, infrared-regulator dependent, diverges as mu -> 0 (where the coefficient is replaced by a term non-analytic in p^2, as found in r1 for `s_max = infinity`), and has no Lambda^2 or ln Lambda piece. This reproduces the gatekeeper's value.
Healthy sign (`lem:msigma`) is preserved by both terms. The opposite-sign term of `eq:Z-sigma` is not produced; it arises in the manuscript from the induced EH term, that is, from the operator on the emergent metric.

### R4. Lemma 2 (re-verified; scope sharpened)
Premise from the manuscript: appH Problem D (L742-757): "In `eq:Smicro` the field Phi^I_A carries no coordinate index: it is a set of scalar fields on the scaffold"; ch02 keeps coordinate, tangent and internal alphabets separate; the identification A <-> mu (`eq:vev-is-frame`) is not a symmetry. Pure scaffold rotations `x -> Rx`, `Phi_a(x) -> Phi_a(R^-1 x)` with `A_mu`, `omega_mu` rotating in mu only are a symmetry of `eq:Smicro` and `eq:D-both` (the gatekeeper confirmed that the extra diagonal symmetry does not rescue EH).
Under H1-H3, `Gamma^(2)_{ab}(Rp) = Gamma^(2)_{ab}(p)`, so the Phi-Phi kernel depends on p^2 only; mixed kernels `p_mu f(p^2)` and connection kernels `alpha delta + beta p p` have the Schur complement again a function of p^2.
**Reduced form (Finding 5).** If the full effective action is invariant under a linearized gauge transformation that moves components other than `h`, the invariance passes to the form obtained by eliminating those components, the Schur complement. That reduced form `Q_p` on `h` is the physical criterion, and it too depends on p^2 only. The lemma proper is then: if a form `Q_p` that depends on `p` only through `p^2` is invariant under `h -> h + p (x) xi + xi (x) p` for all `xi`, then it annihilates `p' (x) xi + xi (x) p'` for all `p'` with `p'^2 = p^2`, which span `Sym^2` for `p != 0`; hence `Q_p = 0`; likewise on the traceless block with `eq:FP-gauge`. Script `check_invariance_nogo.py` (r1, unchanged, re-run) solves this for Euclidean p^2 = 1 and Lorentzian p^2 = +1, -1, 0.
**Hypothesis class and relaxations.** H1 (flat scaffold), H2 (rotation-preserving regulator and gauge fixing), H3 (rotation-invariant vacuum and background), H4 (h a fixed linear image of Phi components). The result is a no-go for linear-in-Phi composite fluctuations in that class only. Relaxing H2 with a regulator or kinetic metric built from `Theta^{mu nu}` (Presentation A, `rem:ch3-varying-theta`) breaks scaffold rotations; relaxing H3 with a non-invariant vacuum or background does the same; H1 and H4 can also be relaxed. These are pointers: the 004 survey records that such a route is not shown to produce an EH term for a Phi-composite metric, and that Lorentz recovery (D1/E) would be an open cost. The Weinberg-Witten theorem, mentioned in r1, is not used and not claimed.
Relation to existing text: appH D (L765-791) proves the tree-level classification for at most two derivatives and says FP structures "are not excluded" for terms that tie derivative and tangent indices; Lemma 2 shows such mixing is not *generated* by `eq:Smicro` in class H1-H4 at any loop order. It extends, and does not contradict, that text.

### R5. Item 5 (ch05), Finding 1
At `Phibar = v I`: `(D Phi)^dag D Phi ⊃ -i v (d dPhi)^dag A + i v A d dPhi`, trace `= 2 i v Tr(A d K)`, `K` the anti-Hermitian part (the Y-A mixing of the appH U(4) paragraph). Under the manuscript's identification `M = eta h` (appH L1033-1037) the `T_{0i}` components, and for complex `dPhi` the imaginary parts of `T`, lie in `K`; so whenever `G_int` contains those generators there is a tree-level derivative A-T mixing. The A-dT clause is therefore not asserted false. For psi-T: `psi -> (psi/4) I`, `T -> eta T`, `Tr(eta T) = eta^{mu nu} T_{mu nu} = 0` kills the cross term in the kinetic form and in the second variation of `V` (check B, `d^2 V/da db = 0`, kinetic cross term 0). The reviewer's snippet is adopted verbatim.

### R6. Why a named assumption (Finding 8, 004 Q4)
After the correction, the conclusion of `prop:scaffold` is a premise. Options: keep a weakened proposition; a remark only (the premise stays unnamed and can be reused silently); a named assumption plus a remark recording the counterexample, with F as the problem that must discharge it. The third is chosen. It changes no problem label and no scope statement; its ch16 inventory entry has one ch17 cross-reference to be flagged (Item 7).

### R7. Literature
Seeley-DeWitt a_0, a_1, a_2 are used as displayed in `eq:appA-a0`-`eq:appA-a2` (standard; not re-derived). No new citation is added to the LaTeX. Weinberg-Witten (Phys. Lett. B 96 (1980) 59) is not used; its applicability to NAMCG is unchecked and the earlier BibTeX entry is withdrawn from this package. The 004 survey's references (arXiv 2411.02598, `Steinacker2023`) are not used; "not independently verified".

### R8. Comparison with the original target
F is not derived. The package removes an unnamed premise from the heat-kernel route and shows that the displayed action (class H1-H4) cannot supply it.

## Claim classification

| Claim | Class |
|---|---|
| Fluctuation operator of `eq:Smicro` at fixed Abar is `-Dbar^2 + E`, E derivative-free | established identity |
| Lambda-dependence of `W_E^(1)` fixed by a_0-a_2; no Lambda-dependent term contains d Phibar (Abar fixed) | established, conditional on scaffold regulator and fixed Abar |
| `tr E(sigma) = 16 lambda (v^2 + 4 v sigma + 2 sigma^2)`; `E_H`, `E_K` | established (sympy, check 1) |
| `sqrt(g) R = 6 (d sigma)^2/v^2` + t.d. for `g = (1+sigma/v)^2 eta` | established (sympy) |
| Operator on `g` gives `-N_0 Lambda^2 (d sigma)^2/(32 pi^2 v^2)`, matching `eq:Z-sigma` | established algebra, conditional on the emergent-operator premise |
| Last sentence of `prop:scaffold` does not follow (PRIOR-CLAIM-ERROR) | established (counterexample) |
| `Delta Z` formula above, both blocks, finite mu | established one-loop, conditional on Abar = 0 fixed, scaffold regulator, p^2 << mu^2 << lambda v^2 |
| Lemma 2 (p^2-only form + shift invariance => 0) | established, conditional on H1-H4 |
| Relaxing H1-H4 (Theta regulator etc.) is not excluded | pointer; not shown to work |
| ch05: no psi-T mixing in the tree quadratic action | established (direct expansion; check B) |
| ch05: A-dT mixing present iff `G_int` contains the anti-Hermitian T components | established, conditional on the identification `M = eta h` |
| `ass:emergent-op` | input (assumption); F must discharge it |
| A_mu-integrated Lemma 1; curved scaffolds; Presentation A | unresolved / not covered |

## Proposed changes

All target files are CRLF. New labels: `ass:emergent-op` and `rem:ch8-scaffold-vs-emergent`, each defined once in Item 2; `verify_anchors_labels.py` confirms neither exists now. Verified existing labels used (each defined exactly once): `eq:Smicro`, `eq:V`, `ass:aux-metric`, `eq:W-again`, `eq:s-limits`, `eq:appA-a0`, `eq:appA-a2`, `eq:universal-R`, `eq:repairII-trace`, `eq:Z-sigma`, `lem:msigma`, `eq:D-both`, `eq:g-from-e`, `eq:vev-is-frame`, `eq:FP-gauge`, `eq:FP`, `thm:mT`, `sec:status-D`, `sec:status-F`, `eq:O-eta`, `thm:Geff`, `eq:Geff-structure`, `eq:W-expand`, `app:status`, `ch:vierbein-emergence`, `ch:heat-kernel`, `ch:agenda`, `sec:ch8-which-g`, `ch:falsifiers`, `rem:ch3-varying-theta`. Anchors verified single-occurrence by script. The integrator should apply Items 1-6 together; Item 7 only after the author acknowledges the ch17 cross-reference flagged in Author decision needed.

### Item 1 - `chapters/appH-microscopic-proofs.tex`, Problem F section (three new conditional paragraphs)

Anchor: insert immediately **before** `\section{Problem G: HBEV}` (one occurrence; preceded by the paragraph ending "...sector sum. Problems~B, C, D, F and~G remain open."). Nothing removed; leave one blank line before the section command.

```latex
\paragraph{Which metric the scaffold one-loop action induces (conditional; not closure).}
Consider the displayed action~\eqref{eq:Smicro} with
potential~\eqref{eq:V} on the square locked block, on the scaffold
\(g^{(0)}\) of Assumption~\ref{ass:aux-metric}, after Wick rotation,
with the internal connection held at a background value
\(\bar A_\mu\) and not integrated. Expand \(\Phi=\bar\Phi+\varphi\)
about a smooth background \(\bar\Phi\) and write \(\varphi\) in
thirty-two real components normalized so that the kinetic term is
\(\sum_a g^{(0)\mu\nu}\bar D_\mu\varphi_a\bar D_\nu\varphi_a\). The
kinetic term is bilinear in \(\Phi\), so its second variation does not
depend on \(\bar\Phi\), and the fluctuation operator is
\[
  \mathcal O_{\bar\Phi}
  =-g^{(0)\mu\nu}\bar D_\mu\bar D_\nu+E(\bar\Phi),
\]
where \(\bar D\) is built from \(g^{(0)}\) and \(\bar A_\mu\), and
\(E(\bar\Phi)\) is one half of the Hessian of \(V\) at \(\bar\Phi\);
\(E\) contains no derivative of \(\bar\Phi\). Use this operator
in~\eqref{eq:W-again} with the limits~\eqref{eq:s-limits}. For
\(I(\LUV)=\int_{\LUV^{-2}}^{\mu^{-2}}s^{-1}f(s)\,\mathrm{d}s\) one has
\(\partial_{\LUV}I=2\LUV^{-1}f(\LUV^{-2})\), so the
\(\LUV\)-dependence of \(W_E^{(1)}\) is fixed by the small-\(s\)
expansion of the heat trace through \(a_2\), up to terms that vanish as
\(\LUV\to\infty\). By~\eqref{eq:appA-a0}--\eqref{eq:appA-a2},
\[
  W_E^{(1)}\supset
  -\int\mathrm{d}^4x\,\sqrt{g^{(0)}}\left[
    \frac{32\,\LUV^4}{64\pi^2}
    +\frac{\LUV^2}{32\pi^2}
     \operatorname{tr}\Bigl(\tfrac16R[g^{(0)}]-E(\bar\Phi)\Bigr)
    +\frac{1}{32\pi^2}\ln\Bigl(\frac{\LUV^2}{\mu^2}\Bigr)a_2
  \right],
\]
where \(a_2\) contains \(E^2\), \(R[g^{(0)}]E\), curvature-squared
terms of \(g^{(0)}\), \(\bar F_{\mu\nu}\bar F^{\mu\nu}\) and total
derivatives. No \(\LUV\)-dependent term contains a derivative of
\(\bar\Phi\) outside a total derivative. The \(\LUV^2\) curvature term
is the term~\eqref{eq:universal-R}, with \(\mathcal N_0=32\), for the
scaffold metric \(g^{(0)}\), which Assumption~\ref{ass:aux-metric}
holds fixed.

For the composite metric the corresponding coefficient vanishes. On
the flat scaffold take \(\bar A_\mu=0\) and
\(\bar\Phi=(v+\sigma)\mathbb I\), so that
\(g=(1+\sigma/v)^2\eta\) by~\eqref{eq:repairII-trace}; in the
Euclidean section \(\sqrt g\,R[g]=6(\partial\sigma)^2/v^2\) up to a
total derivative. The \(\LUV^2\) term above is
\(\tfrac{\LUV^2}{32\pi^2}\int\mathrm{d}^4x\operatorname{tr}E(\sigma)\),
with \(\operatorname{tr}E(\sigma)=16\lambda(v^2+4v\sigma+2\sigma^2)\),
and contains no \((\partial\sigma)^2\). Building the operator on \(g\)
instead, as in Assumption~\ref{ass:emergent-op}, gives
\(-\mathcal N_0\LUV^2(\partial\sigma)^2/(32\pi^2v^2)\) at the same
order, which is the induced term of~\eqref{eq:Z-sigma} with
\(1/(16\pi G_{\mathrm{eff}})=\mathcal N_0\LUV^2/(192\pi^2)\). The
replacement supplies the whole \(\LUV^2\) coefficient for the composite
metric; it does not correct a scaffold value.

The \((\partial\sigma)^2\) term of the scaffold one-loop action has no
\(\LUV^2\) or \(\ln\LUV\) piece. Take the limits~\eqref{eq:s-limits}
and \(p^2\ll\mu^2\ll\lambda v^2\). At \(\bar A_\mu=0\) the sixteen
Hermitian components have
\(E_H=\tfrac\lambda2\bigl(3(v+\sigma)^2-v^2\bigr)\) and the sixteen
anti-Hermitian components have
\(E_K=\tfrac\lambda2\bigl((v+\sigma)^2-v^2\bigr)\). At second order in
\(\sigma\) a block of \(n\) components with mass \(m\) gives
\[
  W_E^{(1)}\supset
  -\frac n4\,E'(0)^2\int\frac{\mathrm{d}^4p}{(2\pi)^4}\,
   \tilde\sigma(p)\tilde\sigma(-p)\,B(p),
\]
\[
  B(p)=\frac{1}{16\pi^2}\int_0^1\mathrm{d}x\left[
   E_1\!\left(\frac{m^2+x(1-x)p^2}{\LUV^2}\right)
   -E_1\!\left(\frac{m^2+x(1-x)p^2}{\mu^2}\right)\right].
\]
For the Hermitian block, \(n=16\), \(E'(0)=3\lambda v\),
\(m^2=\lambda v^2\) and
\(\partial_{p^2}B|_{p=0}=-\bigl(e^{-\lambda v^2/\LUV^2}
-e^{-\lambda v^2/\mu^2}\bigr)/(96\pi^2\lambda v^2)\). For the
anti-Hermitian block, \(n=16\), \(E'(0)=\lambda v\), \(m=0\) and
\(\partial_{p^2}B|_{p=0}=(\LUV^{-2}-\mu^{-2})/(96\pi^2)\). The local
term \(\tfrac12\Delta Z\int\mathrm{d}^4x\,(\partial\sigma)^2\) therefore
adds to the microscopic value \(2N\) of \(Z\) in~\eqref{eq:Z-sigma}
\[
  \Delta Z=\frac{3\lambda}{4\pi^2}
   \Bigl(e^{-\lambda v^2/\LUV^2}-e^{-\lambda v^2/\mu^2}\Bigr)
   +\frac{\lambda^2v^2}{12\pi^2}\Bigl(\frac1{\mu^2}-\frac1{\LUV^2}\Bigr),
\]
that is, \(3\lambda/4\pi^2\) up to \(O(\lambda v^2/\LUV^2)\) and
\(O(e^{-\lambda v^2/\mu^2})\) from the Hermitian block, plus a positive
term from the anti-Hermitian block that depends on the infrared limit
\(\mu\) and is replaced by a term non-analytic in \(p^2\) as
\(\mu\to0\). Both terms are positive for \(\mu<\LUV\) and carry
no \(\LUV^2\) or \(\ln\LUV\) piece. In this one-loop calculation the
conformal-mode kinetic term keeps the sign of Lemma~\ref{lem:msigma}.
The opposite-sign term of~\eqref{eq:Z-sigma} is not produced in this
calculation; in the manuscript it arises from the induced
Einstein--Hilbert term, that is, from the operator built on the
emergent metric.

\paragraph{Scaffold rotations exclude linearized diffeomorphism invariance in a stated class (conditional; not closure).}
In~\eqref{eq:Smicro} the components of \(\Phi^I{}_A\) are scalars of
the scaffold: a scaffold index appears only on \(\partial_\mu\) and
\(A_\mu\), and on \(\omega_\mu\) in the completion~\eqref{eq:D-both}.
On the flat Euclidean scaffold, rotations \(x\mapsto Rx\),
\(R\in\mathrm{SO}(4)\), acting on scaffold indices alone are a
symmetry, and the background \(\bar\Phi=v\mathbb I\),
\(\bar A_\mu=\bar\omega_\mu=0\) is invariant. Assume that the regulator
and the gauge fixing preserve this symmetry, as the scaffold
proper-time regulator above does, and that the composite-metric
fluctuation \(h_{\mu\nu}\) is a fixed linear function of the components
of \(\Phi\), for example the one obtained from~\eqref{eq:g-from-e}
with the identification~\eqref{eq:vev-is-frame}. Then, at any loop
order, the quadratic part of the effective action in the components of
\(\Phi\), with the connections set to zero or eliminated at quadratic
order, has the form
\(\sum_{a,b}\tilde\varphi_a(-p)F_{ab}(p^2)\tilde\varphi_b(p)\):
invariance gives \(F_{ab}(Rp)=F_{ab}(p)\), an
\(\mathrm{SO}(4)\)-invariant function of one vector depends only on
\(p^2\), and eliminating a connection, whose mixed and diagonal kernels
have the forms \(p_\mu f(p^2)\) and
\(\alpha(p^2)\delta_{\mu\nu}+\beta(p^2)p_\mu p_\nu\) with internal
labels suppressed, preserves this form. Let \(Q_p\) be the reduced form
on \(h\) obtained by eliminating the remaining components; it is the
reduced form that inherits any invariance of the full effective action
under a linearized gauge transformation, and it too depends on \(p\)
only through \(p^2\). If \(Q_p\) is invariant under
\(h\mapsto h+p\otimes\xi+\xi\otimes p\) for all \(\xi\), then \(Q_p\)
annihilates \(p'\otimes\xi+\xi\otimes p'\) for every \(p'\) with
\(p'^2=p^2\); for \(p\neq0\) these tensors span all symmetric tensors,
so \(Q_p=0\). The same holds on the traceless block with the
transformation~\eqref{eq:FP-gauge}. The linearized Einstein--Hilbert
form and the massless Fierz--Pauli form~\eqref{eq:FP} are invariant
and nonzero, hence depend on the direction of \(p\); \(Q_p\) cannot
equal \(c\) times either of them plus a form depending on \(p\) only
through \(p^2\) unless \(c=0\). A form depending only on \(p^2\) can
coincide with a gauge-fixed linearized Einstein--Hilbert operator, for
example the Feynman--de~Donder form
\(p^2\bigl(h_{\mu\nu}h_{\mu\nu}-\tfrac12h^2\bigr)\), but without the
gauge symmetry and its ghosts each nondegenerate direction of such a
form, including directions of opposite sign, is a propagating
component. This statement holds for a flat scaffold, a regulator and
gauge fixing that preserve scaffold rotations, a vacuum and background
invariant under them, and a composite-metric fluctuation that is a
fixed linear function of the components of \(\Phi\). It does not
exclude a composite-metric Einstein--Hilbert term in general: a
regulator or kinetic metric built from \(\Theta^{\mu\nu}\) in
Presentation~A (Remark~\ref{rem:ch3-varying-theta}), a vacuum or
background that is not invariant under scaffold rotations, a curved
scaffold, or a composite metric that is not a fixed linear image of
\(\Phi\) each relaxes one of these hypotheses and is not covered.

\paragraph{What the two preceding results imply for Problem~F (conditional; not closure).}
In the class of the preceding paragraph, neither the displayed action
nor its quantum corrections give the composite-metric fluctuation a
linearized diffeomorphism invariance, an induced Einstein--Hilbert
term, or the Fierz--Pauli block of hypothesis~5 of
Theorem~\ref{thm:mT}; the induced Fierz--Pauli term assumed in the
quadratic tests of Section~\ref{sec:status-D} is likewise not
generated in this way. These structures need an ingredient that ties
derivative indices to tangent indices. The
operator~\eqref{eq:O-eta} on the emergent background, used in
Theorem~\ref{thm:Geff}, is such an ingredient; it enters as
Assumption~\ref{ass:emergent-op}, which is assumed, not derived. The
one-loop \(\Phi\)--\(\Phi\) action of the displayed action on the
scaffold contributes to the \(\LUV^2\) and \(\ln\LUV\) coefficients
\(A\) and \(B\) of~\eqref{eq:Geff-structure} only through the curvature
of \(g^{(0)}\), not through that of the composite metric; the missing
step of Problem~F includes discharging
Assumption~\ref{ass:emergent-op}, or replacing it by another derived
ingredient. Not covered here: integration of the auxiliary \(A_\mu\) in
the first result, the hypotheses relaxed in the second, and
Presentation~A in general. No value or sign of \(G_{\mathrm{eff}}\)
follows. Problems~B, C, D and~F remain open.
```

Notes for Item 1: the inline `h_{\mu\nu}h_{\mu\nu}` is the Euclidean contraction stated in the paragraph ("flat Euclidean scaffold"). The scaffold regulator "above" refers to the proper-time limits of the first paragraph. Spelling "linearized" follows the manuscript's dominant usage.

### Item 2 - `chapters/ch08-heat-kernel.tex`, Section `sec:ch8-which-g` (correction of `prop:scaffold`; named assumption)

(a) Replace exactly the sentence `The justification is the derivative expansion:` (appears once) by
```latex
This is an assumption of the chapter, not a consequence of the action:
```
The two preceding sentences ("Assumption~\ref{ass:aux-metric} declared \(g^{(0)}\) non-dynamical. The heat kernel of this chapter is nevertheless written on \(g_{\mu\nu}\).") stay.

(b) Replace the whole environment from `\begin{proposition}[Scaffold replacement]` through its `\end{proposition}` (the first and last lines are `\begin{proposition}[Scaffold replacement]` and `\end{proposition}`, the latter preceded by "Self-consistently substituting the emergent metric is therefore valid through the order of this conditional truncated identity.") by
```latex
\begin{assumption}[Fluctuation operator on the emergent background]
  \label{ass:emergent-op}
  The fluctuation operator \(\mathcal{O}_\eta\) of~\eqref{eq:O-eta} is
  built from the emergent metric \(g_{\mu\nu}\) of
  Chapter~\ref{ch:vierbein-emergence}, with the endomorphism and
  curvature coupling stated for each sector, and not from the scaffold
  \(g^{(0)}_{\mu\nu}\).
\end{assumption}

\begin{remark}[Operator on the scaffold and on the emergent metric]
  \label{rem:ch8-scaffold-vs-emergent}
  The displayed action~\eqref{eq:Smicro} does not supply the operator
  of Assumption~\ref{ass:emergent-op}. With the operator built from
  \(g^{(0)}\) and the internal connection held at a background value,
  no \(\LUV\)-dependent term of the one-loop action contains a
  derivative of the condensate, so the \(\LUV^2\) curvature term
  of~\eqref{eq:W-expand} multiplies the curvature of \(g^{(0)}\). For
  \(\bar\Phi=(v+\sigma)\mathbb I\) on a flat scaffold, where
  \(g=(1+\sigma/v)^2\eta\), the \(\LUV^2(\partial\sigma)^2\) coefficient
  is zero with the scaffold operator and is the induced term
  of~\eqref{eq:Z-sigma} with the operator built on \(g\)
  (Appendix~\ref{app:status}, Section~\ref{sec:status-F}). Replacing
  \(g^{(0)}\) by \(g\) therefore supplies this coefficient; it does not
  correct a scaffold value. The expansion~\eqref{eq:W-expand} and
  Theorem~\ref{thm:Geff} are stated for operators built on \(g\), that
  is, under this assumption. Discharging
  Assumption~\ref{ass:emergent-op} is part of Problem~F.
\end{remark}
```
The paragraph that follows ("At higher order the replacement produces the backreaction tensor \(\mathcal{G}_{\mu\nu}\) of~\eqref{eq:SW}. ...") is kept.

(c) Replace exactly (L56-58) `Integrate \(\eta\) at one loop on a slowly varying emergent background \(g_{\mu\nu}\), using Presentation~B.` (the line break after "Integrate" is whitespace) by
```latex
Integrate \(\eta\) at one loop on a slowly varying emergent
background \(g_{\mu\nu}\), using Presentation~B and
Assumption~\ref{ass:emergent-op}.
```
(d) Replace exactly the exercise item beginning `\item \textbf{Scaffold error.}` (ending "...and which renormalize higher-curvature couplings?") by
```latex
  \item \textbf{Scaffold error.}
    For \(\bar\Phi=(v+\sigma)\mathbb{I}\) on a flat scaffold, compare
    the \(\LUV^2(\partial\sigma)^2\) coefficient of the one-loop
    action computed with the scaffold operator and with the operator
    of Assumption~\ref{ass:emergent-op}.
```

### Item 3 - `chapters/appB-modular.tex`, Section `sec:appB-replica`

Replace the two sentences "In Presentation~B the cover is a branched cover of the auxiliary manifold, later identified with the emergent spacetime by Proposition~\ref{prop:scaffold}. In Presentation~A the same construction requires Problem~A of Chapter~17." (L110-113) by
```latex
In Presentation~B the cover is a branched cover of the auxiliary
manifold. Identifying it with the emergent spacetime requires that the
fluctuation operator be built from the emergent metric
(Assumption~\ref{ass:emergent-op}), which the displayed action does
not supply. In Presentation~A the same construction requires
Problem~A of Chapter~\ref{ch:agenda}.
```

### Item 4 - ch04 Exercise 7, appG, in one item (`chapters/ch04-vierbein-emergence.tex` L418-423; `chapters/appG-sector-entropy.tex` L19-29)

ch04: replace exactly `Write one sentence stating when it is legitimate to replace \(g^{(0)}\) by \(g\) inside a heat kernel, and what error term that replacement drops. The full answer is Chapter~8; the sentence is due now.` by
```latex
Write one sentence stating what must be assumed in order to
replace \(g^{(0)}\) by \(g\) inside a heat kernel, and why the
displayed action does not supply it. The full answer is
Chapter~\ref{ch:heat-kernel}, Assumption~\ref{ass:emergent-op}.
```
appG: replace exactly the clause `For a Laplace-type fluctuation operator the heat-kernel expansion on the cone produces the area term` by
```latex
For a Laplace-type fluctuation operator on the emergent metric
(Assumption~\ref{ass:emergent-op}) the heat-kernel expansion on the
cone produces the area term
```
The rest of the appG paragraph (including "the coefficients \(A,B,C\) and physical matching remain open in Problem~F") is kept.

### Item 5 - `chapters/ch05-lorentz-decomposition.tex`, Section `sec:ch5-kinetic` (psi-ddT clause; PRIOR-CLAIM-ERROR, non-load-bearing)

Replace exactly (L249-251) `On a Minkowski condensate the mixing terms that survive after gauge fixing are of the form \(\psi\,\partial\partial T\) and \(A\,\partial T\). They are the usual linearized scalar--tensor and vector--tensor mixings.` by the reviewer's snippet:
```latex
Mixing terms of the form \(\psi\,\partial\partial T\) and
\(A\,\partial T\) would be the usual linearized scalar--tensor and
vector--tensor mixings. The quadratic expansion of
\(S_{\mathrm{micro}}\) on the flat scaffold contains no
\(\psi\)--\(T\) mixing: its kinetic term contracts derivatives only
through \(g^{(0)\mu\nu}\), and the trace and \(\eta\)-traceless parts
are orthogonal in its kinetic and potential forms. The internal
connection \(A_\mu\) mixes only with the anti-Hermitian part of
\(\delta\Phi\), with the derivative index contracted with that of
\(A_\mu\); which components of \(T_{\mu\nu}\) lie in that part depends
on the identification of \(T_{\mu\nu}\) in \(\delta\Phi\) and on the
internal gauge group. A \(\psi\,\partial\partial T\) structure requires
an additional ingredient (Appendix~\ref{app:status},
Section~\ref{sec:status-F}).
```
"Two structural facts will be used later." and the enumerate are kept.

### Item 6 - (merged into Items 2-4)
No separate item. The ch08 L56-58 and L363-367 and ch04/appG/appB rewordings are Items 2(c), 2(d), 4 and 3.

### Item 7 - `chapters/ch16-falsifiers.tex` (separable; apply only after the author acknowledges the ch17 cross-reference in "Author decision needed")

(a) Inventory row. After the row `\ref{ass:laplace} & setup & infrared operator is Laplace type \\` insert
```latex
\ref{ass:emergent-op} & load-bearing & fluctuations propagate on the
  emergent metric \\
```
(b) Sentence. After "...and frame existence is part of Problem~D1." insert
```latex
Assumption~\ref{ass:emergent-op} is a premise of
Theorem~\ref{thm:Geff} that Problem~F must discharge.
```
(c) Chain item 6. Replace `The Euclidean curvature coefficient obeys the conditional, truncated heat-kernel identity of Theorem~\ref{thm:Geff}; physical matching requires specified operators, weights, thresholds, continuation, and scheme (Problem~F).` by
```latex
The Euclidean curvature coefficient obeys the conditional,
        truncated heat-kernel identity of Theorem~\ref{thm:Geff} for
        operators built on the emergent metric
        (Assumption~\ref{ass:emergent-op}); physical matching requires
        specified operators, weights, thresholds, continuation, and
        scheme (Problem~F).
```
(The enumerate indentation is the integrator's to match.)

### Stale passages elsewhere (not edited; for the author)
- ch08 "What has been computed" row "truncated R-coefficient identity | conditional on specified sectors and scheme | Thm. thm:Geff": could add "and on Assumption ass:emergent-op" (a status-table cell; left to the author).
- ch04 L270-272 ("Chapters 8 and 11 compute pieces of it: the Einstein-Hilbert term from the heat kernel") and ch01 L59-60 ("a heat-kernel expansion supplies an explicit formula for G_eff"): optional qualifiers.
- ch17 F "Missing step": optional sentence, author's call: "On the flat scaffold, in the class stated in Appendix H, Problem F, the quadratic Hessian and its symmetric quantum corrections induce no Einstein-Hilbert term for the composite metric; Assumption~\ref{ass:emergent-op} must itself be discharged." Not drafted into an item because ch17 defines the target.
- Pre-existing, unrelated: ch01 `eq:composite-metric`/`eq:spine`, ch02 `eq:composite-vierbein`, ch03 `eq:vierbein-next` still display the Repair-I form that ch04 abandons.

## Verification scripts

All in `proposals/003-auto-target/`, run with `C:\Python312\python` (sympy, mpmath); outputs saved alongside.
- `check_scaffold_hessian.py` -> `.out.txt` (r1, unchanged, re-run): kinetic form `sum h^2 + k^2`; Hessian blocks `E_H`, `E_K`; `tr E(sigma)`; `sqrt(g)R + 6 Omega Box Omega = 0`, R = +12 on S^4.
- `check_bubble_lambda.py` -> `.out.txt` (r1, `s_max = infinity` case, unchanged): `d_{p^2}B|_0 = -e^{-m^2/Lambda^2}/(96 pi^2 m^2)`; massless block analytic p^2 coefficient `1/(96 pi^2 Lambda^2)`; numerical cross-checks.
- `check_finite_mu_and_mixing.py` -> `check_finite_mu_and_mixing.out.txt` (new): (A) finite `s_max = mu^-2`: massive `d_{p^2}B|_0` exact, massless `(Lambda^-2 - mu^-2)/(96 pi^2)` symbolic and numerical at four (Lambda, mu) pairs and two massive cases; totals `Delta Z_H`, `Delta Z_K`; mu -> 0 limit of `Delta Z_H`. (B) psi-T orthogonality: `Tr(eta T) = 0`, kinetic cross term 0, `d^2 V/da db = 0` at `Phibar = v I`.
- `check_invariance_nogo.py` -> `.out.txt` (r1, unchanged, re-run): the invariant symmetric form on `h` is forced to zero for Euclidean and Lorentzian p, also on the traceless block; `Q_FP` invariant and direction dependent; `Q_FP + de Donder = p^2(h.h - h^2/2)`.
- `verify_anchors_labels.py` -> `verify_anchors_labels.out.txt` (new): every anchor of Items 1-7 occurs exactly once (whitespace and CRLF normalised); every existing label used is defined exactly once; the two new labels are defined zero times at present. (The label `rem:ch3-varying-theta` is not in this list; it was checked separately by grep: one definition in ch03.)

Tool output is a check; the reasoning is in R2-R5.

## Decisions Taken

1. **Finding 3: keep finite mu.** Reason: `eq:s-limits` is the manuscript's regulator and the K-block term is a genuine, if infrared-dependent, correction to Z; dropping it would hide an infrared-regulator dependence that bears on the conformal-mode sign discussion in C. Rejected: restricting to `s_max -> infinity` (discards the stated limits and introduces a non-analytic term that has no local coefficient).
2. **Finding 8 / 004 Q4: option 3.** `prop:scaffold` becomes `ass:emergent-op` plus a remark that keeps the conformal-mode counterexample; the premise is recorded as load-bearing in ch16 (Item 7), with F as the problem that must discharge it. Reason: it makes F's dependency explicit, prevents silent reuse, keeps `thm:Geff` and 002's conditional N analysis intact, changes no label and does not touch the matrix-derived criterion. Rejected: keeping a weakened proposition (vague hypothesis `h`, undefined norm); a remark only (premise stays unnamed).
3. **Q6: all five stale passages rewritten** (ch04 Ex. 7, ch08 L56-58, ch08 L363-367, appG, appB) using label `ch:vierbein-emergence` where a ch04 reference is needed. Reason: they present the emergent-background identification as controlled; the minimal rewordings remove that without scope change.
4. **ch16 / ch17 cross-effect.** The Q6 note asks whether adding F to the ch16 inventory sentence alters a Ch.17 scope statement. I decided to propose the ch16 edits as a separable Item 7 and to flag the ch17 effect (below), not to edit ch17. Reason: Ch.17 L93-96 defines the completed label by "no load-bearing assumption of Chapter~\ref{ch:falsifiers} remains assumed", so a new load-bearing row enlarges that class by one assumption by cross-reference, although `sec:ch17-done`'s explicit list (L693-695) and F's own target ("computed from the specified operators; G_eff is not an input") already require the operator to be specified. Rejected: classifying the row "setup" (understates the role) or applying the row silently.
5. **Lemma 2 presentation.** Written as a scoped no-go (H1-H4), explicit that it does not close the composite-metric EH route; relaxations named only as pointers. Reason: no-go results are bounded by their hypotheses. Rejected: the r1 sketch of an explicit structural ingredient (promoting the tangent index to a scaffold covector index) and the Weinberg-Witten remark; neither is needed, and the former belongs to the 004 survey.
6. **Claims about A and B.** The statement "contributes nothing to A, B or C" is narrowed to the Lambda^2 and ln Lambda coefficients A and B (C multiplies mu^2 and is not addressed).

## Milestone assessment

**M3** applies: the final inference of `prop:scaffold` is a false implication in merged text, load-bearing for reading `thm:Geff` as a statement about the emergent metric (counterexample in R2; gatekeeper confirmed). The ch05 psi-ddT clause is also false but non-load-bearing. **M2** applies: Lemma 2 is a new no-go, now explicitly scoped to H1-H4, ruling out the route in which the displayed action and its symmetric quantum corrections generate linearized-diffeomorphism-invariant composite-metric EH/FP structures on a flat scaffold. No M1 (nothing on the critical path is derived). No M4 (no label change). **M5 is not claimed**: adding a named assumption records an existing premise and changes no definition, but the ch16 inventory entry and its ch17 cross-reference are flagged for the author.

## Status-label recommendation

Critical-path set from ch17 `sec:ch17-done` and App H: A, B, C, D1, E, F, G-derived, N (H, I, J optional). **No label change recommended.** F, C, B, D remain OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL. The proposed text adds no status word and edits no "Ledger label" paragraph.

## Author decision needed

1. **ch16 inventory and the ch17 cross-reference (Item 7).** Ch.17 L93-96 defines DERIVED by reference to "load-bearing assumption of Chapter ch:falsifiers"; a new load-bearing row therefore adds `ass:emergent-op` to the premises that must not remain assumed, by cross-reference. The explicit assumption list of `sec:ch17-done` (L693-695) and F's target are not edited. Please acknowledge or reject; Items 1-6 do not depend on it. If rejected, drop Item 7 and keep the remark's "Discharging ... is part of Problem~F".
2. **Optional ch17 sentence** in F's "Missing step" (see "Stale passages"). Optional.

No structural change to the NAMCG core is proposed in this round.

## Remaining open step

To close F as targeted: derive from the matrix theory (or a stated completion) the fluctuation operator that Assumption `ass:emergent-op` supplies, or an equivalent composite-metric structure tying derivative and tangent indices; then specify gauge-fixed operators, ghosts (diffeomorphism and local-Lorentz), weights, thresholds, continuation and counterterm scheme, and compute A, B, C and the sign of G_eff. Still open in this direction: the A_mu-integrated version of Lemma 1 (the integrated `A_mu` is not of Laplace type); the hypotheses of Lemma 2 that a within-core route can relax (a Theta-built regulator or kinetic metric in Presentation A, a non-invariant vacuum, curved scaffolds, nonlinear composite maps), each to be examined with its Lorentz-recovery cost (D1/E); for C, mixing with T, matter couplings and the physical status of Z once a metric-producing ingredient is chosen; for B, the Fierz-Pauli block and stationarity.

## Special instructions for the gatekeeper

- Must not be asserted: that physical G_eff vanishes; that the emergent-background premise is wrong as a model; that Lemma 2 excludes a composite-metric EH term in general; that F, B, C or D is closed or advanced to DERIVED; that Weinberg-Witten applies.
- Re-check: (1) `Delta Z_K` and the finite-mu `Delta Z_H` (script part A; compare with your own `gk_ircut.py`); (2) that every appH/ch08 statement now carries the fixed-A_mu qualifier or is attributed to Lemma 2; (3) that Lemma 2's text lists H1-H4 and calls the reduced form the criterion; (4) that the ch05 snippet is verbatim yours and that the psi-T check (script B) supports "orthogonal in kinetic and potential forms"; (5) Items 2(a)/(b): the Proposition is replaced as a whole, so check that nothing else in the manuscript depends on its first sentences (grep: only appB L112 and ch08 L364 referred to `prop:scaffold`, both replaced here); (6) the ch17 cross-reference claim in Decision 4 against ch17 L93-96 and L693-695.
- Source-reading scope: digest + targeted reads this round (see above); full-scan status rests on r1.
- Items 2 and 5 edit merged text (PRIOR-CLAIM-ERROR): please classify severity (I assess Item 2 load-bearing, Item 5 non-load-bearing).
