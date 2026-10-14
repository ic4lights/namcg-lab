# Recommendations r2: author questions Q1-Q6 (advisory; proposals 002 and 003)

Scope: advisory only. r1 (`recommendations-r1.md`) is unchanged; this file supersedes it only where stated. No chapter, bib, report or label edits. All LaTeX below is DRAFT: not for integration until it goes through a normal proposal round and receives a gatekeeper ACCEPT. Source reading: digest + targeted reads (not a full scan); the gatekeeper's review `review-r1.md` read in full; label and passage greps redone this round (listed below). Critical-path set (Ch.17 `sec:ch17-done` against Appendix H): A, B, C, D1, E, F, G-derived, N; all OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL (statuses as quoted in the review; not re-read end to end this round); H, I, J optional. No label change is proposed anywhere.

## Changelog (findings of review-r1.md -> changes)

| Finding | Change in r2 |
|---|---|
| F1 (major, R4 wording) | R4 rewritten: "not excluded by Lemma 2's hypotheses; the only route identified here that ties the derivative index to the tangent index (via Theta)". States that the Theta-built metric g_rho, not a Phi-composite metric, acquires curvature; Lorentz recovery (D1/E) is an open cost; R3 and S2 are not shown dead. The phrases "the only within-core route that keeps a genuine path to a matrix-derived G_eff" and "only route with a matrix-derived G_eff" are withdrawn. |
| F2 (major, Q2 gloss) | Corrected gloss adopted (coefficient of C^2 is -alpha/2; c_W = -alpha/2 conditional on the continuation convention). Placeholder resolved: chapter label `ch:ultraviolet` (ch09, one occurrence); the convention itself is located at `app:seeley-dewitt` (S_E=-iS_L, appA L162) plus the added curvature-continuation convention that exists only in 002's proposed N text (not yet in the manuscript; see Q2). |
| F3 (major, Q4 label) | `ch:vierbein-emergence` used. All labels re-verified (list below). |
| F4 (major, Q5 identity and "dead") | Identity stated with scope (constant Lambda; scalar sector; unimodular g_rho; rho a field; every 4D unimodular g_rho); "cancels" replaced; R1 "excluded within Lemma 2's class"; Lambda^4 int rho^2 term and vector sector explicitly not addressed. |
| F5 (minor, next target, ranking) | Next-target computation labelled a preview, meaningful for F only if S1 is adopted; "authorize S1" removed as a default; unsupported "highest impact" for Q5 dropped and ranking redone. |
| F6 (minor, literature) | arXiv 2411.02598 abstract claim and `Steinacker2023` remain "not independently verified" (I did not re-fetch them this round). |
| F7 (minor, Q6) | Q6 states item 6 uses the corrected ch05 snippet in `proposals/003-auto-target/review-r1.md`; all Q6/ch16 text and labels need a normal proposal round. |
| Side note (appK L38-39) | Added to Q1 as separate optional item 1b, verified (see Q1). |

## Labels verified this round (grep over `chapters/`; each exactly one `\label` hit)

`ch:vierbein-emergence` (ch04 L2), `ch:heat-kernel` (ch08 L2), `ch:agenda` (ch17 L2), `ch:ultraviolet` (ch09 L2), `app:seeley-dewitt` (appA L2), `app:status` (appH L2), `sec:status-F` (appH L1104), `sec:status-N` (appH L1837), `sec:ch8-which-g` (ch08 L281), `prop:scaffold` (ch08 L288), `eq:O-eta` (ch08 L63), `eq:W-expand` (ch08 L131), `eq:Smicro` (ch03 L185), `eq:stelle` (ch09 L111), `eq:W4` (ch09 L62), `eq:appA-a1` (appA L69), `eq:appA-O` (appA L18). Not existing (by design, introduced by the DRAFT): `ass:emergent-op`. Nonexistent and withdrawn: `ch:vierbein`, `ch:ultraviolet-placeholder`. Any new label in a proposal round must be re-checked for duplicates then.

---

## Q1. appK sign of a_1 (002, finding 9)

**Facts (established, re-checked).** appA `eq:appA-O` is `O = -g^{mu nu} D_mu D_nu + E`; `eq:appA-a1` is `a_1 = tr_V(R/6 - E)`. `appK-endomorphism.tex` L17 reads `a_1 = tr(E) - (1/6) R dim` for `Delta = -D^2 + E`, the exact negative. `delta a_1 = 0` uses only `tr S = 0` and is sign-independent. No other file references appK labels (r1 grep).

**Options.** (a) correct to `tr(R/6 - E)` and cite `\eqref{eq:appA-a1}`; (b) convention remark (rejected: no convention gives this sign for this operator); (c) cross-reference only.

**Recommendation: (a).** Routine, non-load-bearing, no milestone. Effect on infrared / full GR: none. Cost: one equation line.

DRAFT:
```latex
  a_1=\operatorname{tr}\Bigl(\tfrac16 R-E\Bigr)
     =\tfrac16 R\,\dim-\operatorname{tr}(E),
```
preceded by "with the sign convention of~\eqref{eq:appA-a1}".

**1b (optional, separate; verified).** appK L38-39 reads "The first non-vanishing correction linear in the laboratory field appears in \(a_2\) and is proportional to \(F_{\mu\nu}F^{\mu\nu}\)". `F F` is quadratic in the field, and the section title (L35) already says "Quadratic appearance". Check: `a_2` contains `tr(E^2)`; with `E = E_0 + xi F S`, the first non-vanishing field-dependent term is `xi^2 F_{ab}F_{cd} tr(S^{ab}S^{cd})`, since the linear term vanishes by `tr S = 0` (this is the `delta a_1 = 0` argument; for `a_2` I checked only that structure, not the full coefficient). DRAFT replacement of the one sentence:
```latex
The first non-vanishing correction appears in \(a_2\), is quadratic in
the laboratory field, and is proportional to
\(F_{\mu\nu}F^{\mu\nu}\).
```
The remaining sentences of the section are kept. Classification: established comparison (Q1a, 1b wording); the `a_2` statement itself remains the manuscript's (not recomputed here).

---

## Q2. Overloaded alpha; N target wording; `ass:EFT-a2`

**Facts.** alpha appears as the Weyl coefficient of `eq:stelle` (`-(alpha/2) C^2`), the `a_2` prefactor, the ECG coupling, the Fierz-Pauli parameter, `nu_exp`, and a per-galaxy fit parameter. N's target uses "the values of alpha and G_eff computed in Problem F" (appH L1850, ch17 L506, L655, L727). `eq:W4` has `+c_W C^2`, so `c_W = -alpha/2`: established algebra, **conditional on the continuation convention** of 002 (item 4: `S_E=-iS_L` as in `app:seeley-dewitt`, curvature invariants continued without change of sign, an added convention). The latter half of that convention exists only in 002's proposed N text, not yet in the manuscript; `app:seeley-dewitt` L162 contains the `S_E=-iS_L` part.

**Options.** (1) Replace alpha by Upsilon: rejected, narrows the target to a truncated model. (2) Notation gloss: alpha is the Weyl-squared coupling of `eq:stelle` (its `C^2` coefficient is `-alpha/2`), `c_W = -alpha/2` of `eq:W4` under the stated convention. (3) State in `c_W, c_R`: rejected, scope-widening (adds the spin-0 pole). (4) Leave.

**Recommendation: option 2**, at the appH N entry (with 002's integration, so that the convention it points to exists) and as a parenthesis at ch17 L506 and L727. The ch17 edit is in a completion criterion and must be approved by the author as a pure notation gloss; it does not change scope or label.

**`ass:EFT-a2`:** unchanged recommendation: do not edit now; the (p/Lambda_UV)^2 corrections carry logarithms and the F-dependent coefficients, which belong in the N entry (002 item 1), not in an assumption.

Effect: removes an ambiguity in what N must show; no change to the full-GR criterion.

DRAFT (the gatekeeper's corrected gloss, label resolved):
```latex
(here \(\alpha\) is the Weyl-squared coupling of~\eqref{eq:stelle},
whose \(C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma}\) coefficient is
\(-\alpha/2\); with the continuation convention stated in
Section~\ref{sec:status-N} and Appendix~\ref{app:seeley-dewitt},
\(c_W=-\alpha/2\) in~\eqref{eq:W4} of
Chapter~\ref{ch:ultraviolet}; it is not any other coupling denoted
\(\alpha\) in this book)
```
Caveat for the round: the reference to `sec:status-N` for the convention is valid only after 002's N text (which records the convention) is integrated. If the ch17 gloss is applied before that, drop the clause "with the continuation convention ..." and say only "conditional on the continuation convention of Appendix~\ref{app:seeley-dewitt}" or defer the ch17 edit.

---

## Q3. Optional Barvinsky-Vilkovisky citation

Verified in r1 session via Crossref: A. O. Barvinsky and G. A. Vilkovisky, "Covariant perturbation theory (II). Second order in the curvature. General algorithms", Nucl. Phys. B 333 (1990) 471-511, DOI 10.1016/0550-3213(90)90047-H. The review re-confirmed the Crossref record and that no `Barvinsky*` entry exists in `bib/` or `chapters/`. Not verified: the paper's content, and any large-argument decay claim. **Recommendation (a):** add the entry; cite only for "second-order one-loop action is nonlocal with form factors"; keep decay an explicit assumption. Requires a `bib/` edit by the integrator. Effect on derivations: none. Classification: bibliographic record established; support limited to the title-level claim.

```bibtex
@article{Barvinsky1990,
  author  = {Barvinsky, A. O. and Vilkovisky, G. A.},
  title   = {Covariant Perturbation Theory ({II}). Second Order in the
             Curvature. General Algorithms},
  journal = {Nuclear Physics B},
  volume  = {333},
  pages   = {471--511},
  year    = {1990}
}
```

---

## Q4. Form of `prop:scaffold`; ch16 inventory

**Facts.** After the 003 correction the "conclusion" of `prop:scaffold` is a premise: Lemma 1 (fixed A_mu) plus the conformal-mode counterexample show replacing g^(0) by g moves the Lambda^2 (d sigma)^2 coefficient from 0 to the full induced value (established; gatekeeper re-derived, conditional on fixed A_mu and a scaffold regulator). ch16 L128 reads "targets of critical-path Problems A, E and N", so adding F is a real edit.

**Options.** (1) keep a weakened Proposition; (2) Remark only (premise stays unnamed, can be used silently again); (3) named assumption plus a remark recording the counterexample, listed in ch16 and tied to F.

**Recommendation: option 3 (within the present formulation).** It makes the load-bearing premise explicit and gives F a precise dependency, keeps `thm:Geff` and 002's conditional N analysis intact, and changes no label. It does not close F or D. Costs: a new inventory entry; ch16 L128 must add F; the two references to `prop:scaffold` (appB L112, ch08 L364) must be retargeted. M4 concerns problem labels, not the assumption inventory; flagged to the author anyway. The ch16 inventory entry is an author-approval item.

DRAFT (ch08; replaces the Proposition environment and its lead-in "The justification is the derivative expansion:"):
```latex
\begin{assumption}[Fluctuation operator on the emergent background]
  \label{ass:emergent-op}
  The fluctuation operator \(\mathcal{O}_\eta\) of~\eqref{eq:O-eta} is
  built from the emergent metric \(g_{\mu\nu}\) of
  Chapter~\ref{ch:vierbein-emergence}, with the endomorphism and
  curvature coupling stated for each sector, and not from the scaffold
  \(g^{(0)}_{\mu\nu}\).
\end{assumption}

The displayed action~\eqref{eq:Smicro} does not supply this
operator. With the operator built from \(g^{(0)}\) and the internal
connection held at a background value, no \(\LUV\)-dependent term
contains a derivative of the condensate, so the \(\LUV^2\)
curvature term of~\eqref{eq:W-expand} multiplies the scaffold
curvature; the emergent-metric coefficient arises only on replacing
\(g^{(0)}\) by \(g\)
(Appendix~\ref{app:status}, Section~\ref{sec:status-F}). Discharging
Assumption~\ref{ass:emergent-op} is part of Problem~F.
```
ch16 row DRAFT: `\ref{ass:emergent-op} & load-bearing & fluctuations propagate on the emergent metric \\`. Labels used and verified: `ch:vierbein-emergence`, `eq:O-eta`, `eq:Smicro`, `eq:W-expand`, `app:status`, `sec:status-F`. `\LUV` is an existing macro in the snippet's source file (the same macro appears in the text being replaced); not re-verified as a definition this round. The fixed-A_mu qualifier required by 003 finding 2 is retained.

Classification: Lemma 1/counterexample established (conditional on fixed A_mu and scaffold regulator); the assumption is an input.

---

## Q5. Ingredient tying derivative indices to tangent indices

**Target restated.** Lemma 2 (003): for a flat scaffold, an SO(4)-preserving regulator and gauge fixing, an invariant vacuum, and h a fixed linear image of scalar Phi components, every linearized-diffeomorphism-invariant quadratic form vanishes. So no composite-metric EH/FP structure arises from `eq:Smicro` in that class. Something must make the metric seen by fluctuations non-scalar in the scaffold sense.

### Routes surveyed

**R1. A_mu-integrated theory.** Lemma 1 does not cover it, but Lemma 2's class does: connections eliminated by Schur complement keep the p^2-only structure and enter only contracted with g^(0). **Excluded within Lemma 2's class** (flat scaffold, rotation-preserving regulator and gauge fixing, invariant vacuum, fixed linear image of the Phi components); not excluded outside it. Useful for completing Lemma 1, not as a source of G_eff in that class.

**R2. Named emergent-background assumption (Q4 option 3).** Consistent. Supplies a Sakharov G_eff from `thm:Geff`, but as the output of an inserted premise; D2-class, cannot close D or F (Ch.17). Current working model.

**R3. Constrained spin connection omega = omega(e[Phi]) (App H "D2" completion `eq:D-both`).** Inserts a new term (covariant completion; necessary, not sufficient per the ledger). Not shown to be dead; not matrix-derived as formulated.

**R4. Theta-dependent kinetic metric / regulator (Presentation A).** `eq:dictionary` gives `[X_mu, Phi] <-> i Theta_{mu nu} D^nu Phi`, hence the fluctuation kinetic metric `K_Theta^{nu rho} = eta_{alpha beta} Theta^{alpha nu} Theta^{beta rho}` (rem:ch3-moyal-check, rem:ch3-varying-theta). R4 is **not excluded by Lemma 2's hypotheses** (a background Theta is not SO(3,1)-invariant; a regulator built from Theta is the "Theta-dependent regulator" 003 lists as not covered). It is the only route identified in the documents I read that ties the derivative index to the tangent index (via Theta). Limits, stated plainly:
- Not excluded is not evidence for an Einstein-Hilbert term. For constant Theta, K_Theta is a fixed constant metric (rem:ch3-varying-theta's example has only an SO(1,1)xSO(2) isometry); a K_Theta-built regulator then reproduces the flat-scaffold situation with g^(0) replaced by K_Theta, with no linearized diffeomorphism invariance of a composite h.
- The metric that acquires curvature in the preview below is the **Theta-built** g_rho, not a Phi-composite metric. Whether the metric seen by Phi fluctuations is K_Theta-built or `e[Phi]` (the locked-block target of F) is unresolved; this is what S1 concerns.
- Recovery of Lorentz invariance in the infrared (D1/E) is an open cost of R4, not merely a falsifier.
R3 and S2 are not shown dead; R4 is "the only one identified here".

### Preview calculation (conditional; script saved; scope stated)

Assumptions: the scalar operator of rem:ch3-varying-theta, `L phi = rho^{-1} d_mu(rho K^{mu nu} d_nu phi)`, with `rho = 1/|Pf Theta|`, `g_rho^{mu nu} = rho K^{mu nu}`, `det g_rho = 1`; **constant Lambda** (a position-dependent Lambda_UV ~ Theta^{-1/2} would multiply the Lambda^2 term by a further function of rho and is not treated); **scalar sector only**; rho treated as a field. Let `G = rho g_rho`, `sqrt(G) = rho^2`, `G^{mu nu} = K^{mu nu}`. Then:
- `L = Lap_G - grad ln rho . grad = D^2 - E`, `omega = -(1/2) d ln rho`, `E = -(1/2) Box_G ln rho + (1/4)(grad ln rho)^2` (script, tested family).
- Established identity (script on the diagonal family `g_rho = diag(e^u, e^-u, e^v, e^-v)`; the gatekeeper's hand derivation for **every 4D unimodular g_rho**): `R_G = rho^{-1}[R - 3 Box ln rho - (3/2)|grad ln rho|^2]`, `E = rho^{-1}(-(1/2) Box ln rho - (1/4)|grad ln rho|^2)`, hence `sqrt(G)(R_G/6 - E) = rho R[g_rho]/6` pointwise. Sign conventions as appA (`-L = -D^2 + E`, `a_1 = R/6 - E`). The (d rho)^2 and Box ln rho terms drop out of this particular combination of the scalar-sector integrand; this is an algebraic identity, not a physical cancellation: with det g_rho = 1 there is no conformal mode, rho is a separate dilaton, and the identity says that the scalar-sector Lambda^2 integrand has the form rho R[g_rho]/6 with no rho kinetic term (Brans-Dicke omega = 0 form in this sector only).
- **Not addressed:** the Lambda^4 int rho^2 term (it is the a_0 term, sqrt(G) = rho^2, and it contributes to the dilaton potential), vector-sector contributions, the trace map and kinetic term for nonconstant Theta (not derived; rem:ch3-varying-theta says so), Theta dynamics, and the relation between G (from K_Theta) and `g = e^T eta e` (locked Phi).

Consequence: conditional; it shows the Theta-built scalar-sector Lambda^2 integrand has Einstein-Hilbert-like form for g_rho with Pfaffian weight. It gives no EH term for any Phi-composite metric, no sign of G_eff, and no Lorentz recovery.

### STRUCTURAL - author only

None of these is a default; each changes the NAMCG core or the operator content of the F target (M5 would fire on adoption).
- **S1. Make the K_Theta-built metric the fluctuation/emergent metric and treat the locked-Phi frame as derived from it** (reorients F from the locked block to matrix fluctuations; changes what "the locked block" means in F, ch17 and appH). It would affect A, D1, E, F, C and ch04. Falsifiers: no healthy tensor EH term with definite sign from the sectors' a_1 and dilaton structure; Lorentz invariance not recoverable in the infrared (D1/E). I do not recommend authorizing S1 on the present evidence beyond permitting the preview computation below; the decision on "locked block" is the author's.
- **S2. Promote the tangent index of Phi to a scaffold covector index (Phi^I_mu coframe)** (003 route (a)); inherits the indefinite-kinetic issues of App H D; Weinberg-Witten applicability unchecked.
- **S3. Drop Presentation A's ontological priority (D2)**: not a route to the matrix-derived label; Ch.17 rules it out as a closure.

### Next target (preview; F-relevance conditional on S1)

A preview computation within F: the Presentation-A one-loop Lambda^2 term for the scalar and vector fluctuation sectors about varying Theta (rem:ch3-trace-quadratic extended to nonconstant Theta), using the Laplace-type reduction above, to decide (a) whether a TT Einstein-Hilbert term for K_Theta survives with definite sign and (b) what the dilaton/Pfaffian structure does to the conformal mode (Problem C). Its output bears on F **only if S1 is adopted**; otherwise it is a model calculation about a Theta-built metric and does not touch the F locked-block target. Preconditions to state, not assume: trace map and kinetic term for nonconstant Theta; the Theta-dependent regulator; constant versus position-dependent Lambda.

Literature: `Steinacker2010`, `MantaSteinackerTran2024`, `Steinacker2023` are in the bibliography. arXiv 2411.02598: only its abstract was read in an earlier session (reporting "explicit expressions for the effective Newton constant" on a covariant quantum spacetime with fuzzy extra dimensions); **not independently verified** here or by the gatekeeper, and I did not compare its operators. `Steinacker2023`: **not independently verified**.

---

## Q6. Stale passages after the `prop:scaffold` correction

Status of this section: all text is DRAFT and, together with the ch16 additions and every label, requires a normal proposal round and a gatekeeper ACCEPT; nothing here is integrable now. Assumes the label `ass:emergent-op` (Q4). If the author prefers a remark instead, use "the emergent-background premise of Section~\ref{sec:ch8-which-g}".

1. **ch04 Exercise 7 (L418-423).** Current "Write one sentence stating when it is legitimate to replace g^(0) by g inside a heat kernel, and what error term that replacement drops. The full answer is Chapter 8; the sentence is due now."
```latex
    Write one sentence stating what must be assumed in order to
    replace \(g^{(0)}\) by \(g\) inside a heat kernel, and why the
    displayed action does not supply it. The full answer is
    Chapter~\ref{ch:heat-kernel}, Assumption~\ref{ass:emergent-op}.
```
2. **ch08 L56-58** "Integrate eta at one loop on a slowly varying emergent background g, using Presentation B."
```latex
Integrate \(\eta\) at one loop on a slowly varying emergent
background \(g_{\mu\nu}\), using Presentation~B and
Assumption~\ref{ass:emergent-op}.
```
and the exercise at ch08 L363-367:
```latex
  \item \textbf{Scaffold error.}
    For \(\bar\Phi=(v+\sigma)\mathbb{I}\) on a flat scaffold, compare
    the \(\LUV^2(\partial\sigma)^2\) coefficient of the one-loop
    action computed with the scaffold operator and with the operator
    of Assumption~\ref{ass:emergent-op}.
```
3. **appG L19-29** "...the heat-kernel expansion on the cone produces the area term ... standard result used in Chapter 6 and Appendix B."
```latex
For a Laplace-type fluctuation operator on the emergent metric
(Assumption~\ref{ass:emergent-op}) the heat-kernel expansion on the
cone produces the area term
```
keeping the remainder (the final sentence already says A, B, C remain open in F).
4. **appB L110-112** "later identified with the emergent spacetime by Proposition~\ref{prop:scaffold}."
```latex
In Presentation~B the cover is a branched cover of the auxiliary
manifold. Identifying it with the emergent spacetime requires a
specified map \(g^{(0)}\to g\), which the displayed action does not
supply (Assumption~\ref{ass:emergent-op}). In Presentation~A the same
construction requires Problem~A of Chapter~\ref{ch:agenda}.
```
5. **ch16 inventory and L125-130.** Add the row of Q4 and extend "targets of critical-path Problems A, E and N" to include F for `ass:emergent-op`. Author-approval item.
6. **ch05 L249-251 (psi-d-d-T clause).** Use the **corrected snippet in `proposals/003-auto-target/review-r1.md`** (it drops the A-dT clause), not any earlier draft; it is not reproduced here to avoid divergence. It too needs a normal proposal round.

Anchor existence for items 1-4 was confirmed by the gatekeeper (ch04 L418-423, ch08 L56-58, L363-367, appG L19-29, appB L110-112). Labels used: `ass:emergent-op` (new), `ch:heat-kernel`, `ch:agenda` (both verified above), `sec:ch8-which-g` (verified). Effect: removes places presenting the emergent-background identification as controlled; no scope or label change.

---

## Verification scripts

`check_weighted_laplacian_a1.py` with output `check_weighted_laplacian_a1.out.txt` (sympy 1.14.0; unchanged; re-run by the gatekeeper). Checks `L = Lap_G - grad ln rho . grad`, `L = D^2 - E`, and pointwise `sqrt(G)(R_G/6 - E) = rho R[g_rho]/6` on a diagonal unimodular family. The general unimodular case rests on the gatekeeper's hand derivation (reproduced above), not on the script. Checks, not proofs. This round's new checks were grep-based (labels, appK line contents); nothing new computed.

## Ranking by impact on the infrared / full-GR derivation (redone)

No item here derives anything for a critical-path target; ranking is by how much each reduces the risk of misstating what F and N must show, not by progress on derivations.
1. Q4 (named premise `ass:emergent-op` and ch16 inventory): makes F's load-bearing dependency explicit and stops silent reuse.
2. Q6 (stale passages): removes places that present the premise as derived; depends on Q4.
3. Q5 (survey and preview): informative about which routes survive, but R4's relevance to F depends on S1 and on unresolved Lorentz recovery; no ranking above Q4/Q6 is supported. The preview is a conditional scalar-sector identity.
4. Q2 (notation gloss): keeps N's target unambiguous; touches a completion criterion, author approval needed.
5. Q3 (citation) and Q1 (sign correction, plus optional 1b): non-load-bearing.

Proposed label changes: none; F, C, B, D1, N and the other critical-path problems stay OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL. Author actions beyond text edits: the S1-S3 decision (M5, author only), the ch16 inventory addition, and approval of the ch17 gloss as notation only.
