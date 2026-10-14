# Recommendations r1: author questions Q1-Q6 (advisory; proposals 002 and 003)

Scope: advisory only. No chapter, bib, report or label edits. All LaTeX is DRAFT, not for integration until a normal proposal round gets a gatekeeper ACCEPT. Sources read: `reports/ledger.md`, `reports/run-20261014-1216.md`, `reports/run-20261014-1314.md`, `proposals/002-auto-target/proposal-r2.md` (author items), `proposals/003-auto-target/proposal-r1.md` and `review-r1.md`, and the manuscript passages cited per question. Digest: `make_digest.py --check` printed STALE (HEAD moved; chapters were not edited, so I treat the recorded chapter hash as controlling). This is "digest + targeted reads", not a full scan.

Critical-path set (Ch.17 `sec:ch17-done` against Appendix H): A, B, C, D1, E, F, G-derived, N; all OPEN / PROGRAMME-CONDITIONAL; H, I, J optional. No discrepancy found in the passages I read.

---

## Q1. appK sign of a_1 (002, finding 9)

**Facts.** `appA-seeley-dewitt.tex` defines `O = -g^{mu nu} D_mu D_nu + E` (`eq:appA-O`) and `a_1 = tr_V(R/6 - E)` (`eq:appA-a1`); `ch08` `eq:a0a1` agrees; appH L1209 agrees. `appK-endomorphism.tex:17` writes `a_1 = tr(E) - (1/6) R dim` for `Delta = -D^2 + E`. This is exactly the negative of the standard value (established identity comparison).

**Options.** (a) Correct to `a_1 = tr(R/6 - E)` (equivalently `(1/6)R dim - tr E`). (b) Leave and add a convention remark (rejected: there is no convention in which the stated operator has this sign). (c) Replace by `\eqref{eq:appA-a1}` cross-reference only.

**Recommendation: (a), with a `\eqref{eq:appA-a1}` reference.** It is a routine sign correction, not a milestone item.

**Downstream.** Nothing changes: `delta a_1 = xi F_{ab} tr(S^{ab}) = 0` depends only on tr S = 0, so the overall sign is irrelevant (established). `sec:a2` and the `Status` section use no sign of `a_1`. Appendix K carries no `\ref` from other files (grep of `app:heat_kernel_mixing`, `sec:a1-null`, `sec:a2`, `sec:not-shown`, `sec:appK-status`: only own labels). Side note, not part of the correction: `sec:a2` says "correction linear in the laboratory field ... proportional to F F"; F F is quadratic. Suggest "first non-vanishing correction, quadratic in the laboratory field". Author may ignore.

**Effect on infrared / full GR:** none (non-load-bearing). **Cost:** one equation line.

DRAFT:
```latex
  a_1=\operatorname{tr}\Bigl(\tfrac16 R-E\Bigr)
     =\tfrac16 R\,\dim-\operatorname{tr}(E),
```
(preceded by "with the sign convention of~\eqref{eq:appA-a1}").

---

## Q2. Overloaded alpha; N target wording; `ass:EFT-a2`

**Facts.** alpha appears as: the Weyl coefficient of `eq:stelle` (`-(alpha/2) C^2`, so `alpha = -2 c_W` against `eq:W4`, conditional on the continuation convention recorded in proposal 002); the a_2 prefactor (`eq:W-again-9`/`eq:W-through-2`); the ECG coupling; the Fierz-Pauli parameter (ch07); `nu_exp` (appE); the per-galaxy fit parameter (ch17 L572, L626). N's target is phrased with "the values of alpha and G_eff computed in Problem F" at appH L1850, ch17 L506, L655, L727 and implicitly ch09 L121.

**Options.**
1. Replace alpha by Upsilon in the target. **Rejected, scope-altering:** Upsilon is defined only inside the truncated identity of `thm:Geff` (flat background, vacuum term removed, curvature continuation convention) and, with the a_1-only G, a specific number. The original target is about the derived two-point function, not that truncation. Using Upsilon would narrow the target to a model.
2. Add a clarifying gloss: alpha means the coefficient of `C^2` in `eq:stelle`, equivalently `c_W = -alpha/2` of `eq:W4`, as obtained from Problem F. Notation only; same target.
3. Restate in terms of both `c_W` and `c_R`. **Scope-widening:** it adds the spin-0 pole (a tachyon if `c_R < 0`), which "no propagating Ostrogradsky ghost" does not mention. Not recommended unless the author wants that enlargement.
4. Leave as is.

**Recommendation: option 2**, applied at the N entry in appH (with the 002 integration) and as a parenthetical in ch17 L506 and L727 (the criterion). Keep "alpha and G_eff computed in Problem F". The ch17 edit touches a completion criterion, so it must be a pure gloss; I flag that the author must approve it as such. It does not change scope or any label.

**`ass:EFT-a2` "(p/Lambda_UV)^2".** Recommend not editing the assumption now. Proposal 002 finds, conditionally, corrections of relative size `(L/Upsilon)(p/Lambda_UV)^2` with `L = ln(Lambda_UV^2/mu^2)` (truncated identity), and `(ln(Lambda_UV^2/p^2)+delta_W)/Upsilon` in model F. "At order (p/Lambda_UV)^2" is accurate up to logarithms and coefficients, and those coefficients are the unresolved content of F. Qualifying an assumption's text on conditional model results would put model output into an assumption. Record the point in the N entry (002 item 1) and revisit once F fixes `W_C`. If the author insists, the qualifier "up to logarithmic factors and the coefficients c_W, c_R" only weakens the assertion and does not alter the N target. Flag it so the author sees it.

**Effect:** infrared derivation: removes an ambiguity in what N must show. Full-GR criterion: unchanged. **Classification:** notation identification alpha = -2 c_W is established algebra conditional on the continuation convention (002); the criterion itself is unchanged.

DRAFT (appH N "Missing step", after "Problem~F"; analogous parenthesis in ch17):
```latex
(here \(\alpha\) is the coefficient of \(C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma}\)
in~\eqref{eq:stelle}, equivalently \(c_W=-\alpha/2\) of~\eqref{eq:W4}, and not
any other coupling denoted \(\alpha\) in this book)
```

---

## Q3. Optional Barvinsky-Vilkovisky citation

**Verified this session (Crossref):** "Covariant perturbation theory (II). Second order in the curvature. General algorithms", A. O. Barvinsky and G. A. Vilkovisky, Nuclear Physics B 333 (1990) 471-511, DOI 10.1016/0550-3213(90)90047-H, March 1990. The title supports the statement "at second order in curvature the one-loop action is nonlocal with form factors". **Not verified:** any claim about large-argument decay of the Weyl form factor; I did not read the paper.

**Options.** (a) Add the entry and cite it only for the nonlocality/form-factor statement. (b) Add nothing; keep the sentence uncited. (c) Add and cite for decay (rejected, unsupported).

**Recommendation: (a).** It is low-cost, and it keeps the nonlocal-form-factor statement sourced in the N text, which matters because model F and the |k| ~ Lambda_UV control open step rest on form factors. Cite narrowly and keep decay as a stated assumption. Requires a `bib/namcg.bib` edit by the integrator; key `Barvinsky1990` is absent (checked in 002; still the only match for "Barvinsky" is none).

DRAFT BibTeX:
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
Effect on derivations: none. Classification: bibliographic record established; supports-statement limited to the title-level claim.

---

## Q4. Form of `prop:scaffold`; ch16 inventory

**Facts.** After the 003 correction the conclusion is a premise. Lemma 1 (fixed A_mu) and the conformal-mode counterexample show the replacement g0 -> g moves the Lambda^2 (d sigma)^2 coefficient from 0 to the full induced value, so "valid through the order of the identity" is false. The proposition's own text uses undefined `h^(0)` and `||.||` (review finding 8). ch04 L217-222 and appH L1194-1199 already call the operator a Presentation-B assumption, but ch16 does not list it, and Ch.17 (Problem D) states that D2/Presentation-B-only results leave D and F open.

**Options.**
1. Keep as a Proposition with a weakened true conclusion. Weak: vague hypotheses, and a proposition label that suggests a derived result.
2. Convert to a Remark recording the counterexample. Honest but leaves the premise unnamed and absent from the inventory, so it can again be used silently (as ch08 L56-58, appG L19-29 do).
3. **Named assumption** ("Emergent-background fluctuation operator"), with a short remark recording the counterexample, listed in ch16 as load-bearing and tied to Problem F (with A, D1) as its target for discharge.

**Recommendation: option 3 (within core).** It makes the load-bearing premise explicit, gives F a precise dependency ("derive this assumption from Presentation A or another specified completion"), and keeps `thm:Geff` and all downstream conditional work (including proposal 002's N analysis, which uses G_eff from that premise) intact, labelled conditional. It does not close F or D, and it does not change any label. Honest cost: new inventory entry; the load-bearing sentence in ch16 L128 ("targets of critical-path Problems A, E and N") must add F; two references to `prop:scaffold` (appB L112, ch08 L364 exercise) must be retargeted. This adds an assumption to the inventory but changes no status, priority or completion label. Check MILESTONE M4: it concerns problems/labels, not the assumption inventory; I flag it for the author anyway.

DRAFT (ch08, replacing the Proposition environment and its lead-in "The justification is the derivative expansion:"):
```latex
\begin{assumption}[Fluctuation operator on the emergent background]
  \label{ass:emergent-op}
  The fluctuation operator \(\mathcal{O}_\eta\) of~\eqref{eq:O-eta} is
  built from the emergent metric \(g_{\mu\nu}\) of
  Chapter~\ref{ch:vierbein}, with the endomorphism and curvature
  coupling stated for each sector, and not from the scaffold
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
(`ch:vierbein` is a placeholder: the integrator must confirm the actual chapter label of ch04 before use; I did not verify it here.) ch16 row DRAFT: `\ref{ass:emergent-op} & load-bearing & fluctuations propagate on the emergent metric \\`.

Classification: Lemma 1/counterexample established (gatekeeper re-derived, conditional on fixed A_mu and scaffold regulator); the assumption is an input.

---

## Q5. Ingredient tying derivative indices to tangent indices

**Target restated.** Lemma 2 (003): flat scaffold, SO(4)-preserving regulator and gauge fixing, invariant vacuum, h a fixed linear image of scalar Phi components, then every linearized-diffeomorphism-invariant quadratic form vanishes. So no composite-metric EH/FP structure arises from `eq:Smicro` at any loop order in that class. Something must make the metric seen by fluctuations non-scalar in the scaffold sense.

### Within-core routes surveyed

**R1. A_mu-integrated theory.** Lemma 1 does not cover it, but Lemma 2 does: connections eliminated by Schur complement preserve the p^2-only structure. A_mu carries a scaffold index but enters `eq:Smicro` only contracted with `g^(0)`, so integrating it yields scaffold-scalar sigma-model terms. **Dead end** for a composite-metric EH term (conditional on the rotation-symmetric regulator; established by Lemma 2 reasoning). It remains useful for completing Lemma 1, not for G_eff.

**R2. Named emergent-background assumption (Q4 option 3).** Consistent and honest. Supplies a Sakharov G_eff from `thm:Geff`, but G_eff is then the output of an inserted premise, not matrix-derived. It is the D2-class route that Ch.17 says cannot close D or F. Keep as the current working model; **no path to a matrix-derived G_eff**.

**R3. Constrained spin connection omega = omega(e[Phi]) (torsion-free Palatini-type completion, App H "D2" completion `eq:D-both`).** Ties derivative index to tangent index through derivatives of Phi. It inserts a new term into the action, i.e. a covariant completion, and the ledger already says covariant completion is necessary but not sufficient and is D2-class. Within the manuscript's vocabulary but not matrix-derived. Candidate model route, no derived G_eff.

**R4. Symmetry-breaking vacuum / Theta-dependent regulator and kinetic metric (Presentation A).** The manuscript already contains the only place where a derivative index contracts with something other than `g^(0)`: the dictionary `eq:dictionary`, `[X_mu, Phi] <-> i Theta_{mu nu} D^nu Phi`, giving the fluctuation kinetic metric `K_Theta^{nu rho} = eta_{alpha beta} Theta^{alpha nu} Theta^{beta rho}` (rem:ch3-moyal-check; rem:ch3-varying-theta). A background `Theta` is not SO(3,1)-invariant, so Lemma 2's invariant-vacuum premise fails, and a regulator built from `Theta` (`Lambda_UV ~ Theta^{-1/2}`) is exactly the "Theta-dependent regulator" that 003 lists as not covered. Constant real Theta cannot give `K_Theta ∝ eta` (rem:ch3-moyal-check), but nothing requires that: `K_Theta` can itself be the metric seen by fluctuations. **This is the only within-core route that keeps a genuine path to a matrix-derived G_eff.** It is Presentation A, which Ch.3 calls the ontological starting point.

### Preview calculation for R4 (new; conditional; script saved)

Take the scalar operator of rem:ch3-varying-theta, `L phi = rho^{-1} d_mu(rho K^{mu nu} d_nu phi)`, with `rho = 1/|Pf Theta|`, `g_rho^{mu nu} = rho K^{mu nu}`, `det g_rho = 1` (all as stated there, as extra assumptions). Let `G = rho g_rho`, so `sqrt(G) = rho^2` and `G^{mu nu} = K^{mu nu}`. Then (script, sympy, all pointwise zero):

- `L = Lap_G - grad ln rho . grad = D^2 - E`, with `D = nabla + omega`, `omega = -(1/2) d ln rho`, and `E = -(1/2) Box_G ln rho + (1/4)(grad ln rho)^2`.
- `omega` is a pure gradient, so `-L` is similar to a Laplace-type operator on `L^2(sqrt G)` and the heat-trace coefficients are those of Laplace type with this `E`.
- `sqrt(G) (R_G/6 - E) = rho R[g_rho]/6`, exactly, for the tested unimodular diagonal family `g_rho = diag(e^u, e^-u, e^v, e^-v)` with `u, v, rho` functions of two coordinates.

Consequence (conditional on the assumed trace map and kinetic term; verified only on that family; the general unimodular case is the standard 4D conformal-transformation identity but is **not** checked in the script): the Lambda^2 term of this sector is `∝ ∫ rho R[g_rho]`, a Brans-Dicke omega = 0 scalar-tensor structure with the Pfaffian density playing the role of 1/G. The conformal-mode (d rho)^2 term of the scaffold-metric computation cancels. This (i) gives a non-trivial G_eff-like object whose value is controlled by `Theta` data rather than by Phi, (ii) connects directly to Problem C's scalar-tensor operator, and (iii) is a warning that the Presentation-A route will not simply reproduce `eq:Z-sigma`. It is not a derivation of G_eff: the trace map, the kinetic term and Theta dynamics are not derived (rem:ch3-varying-theta says so), only the scalar sector is treated, and the relation `g = e^T eta e` (locked Phi) versus `G` from `K_Theta` is unresolved.

### STRUCTURAL - author only

These change the NAMCG core or the operator content of the F target; none is a default.
- **S1. Make `K_Theta`-built metric the fluctuation/emergent metric and treat the locked-Phi frame as derived from it** (reorient F from the locked block to matrix fluctuations; fixes what "the locked block" means in the F target in Ch.17 and App H). It is R4 taken as the definition of the metric. It would affect A, D1, E, F, C and the Ch.4 construction. I recommend the author authorize it for *investigation*, since R4 is the only route with a matrix-derived G_eff; but whether it is a core change depends on how the author reads "locked block" in F. Falsifier: the sectors' a_1 and the dilaton structure above fail to give a healthy tensor EH term, or Lorentz invariance cannot be recovered in the infrared (Problem D1/E).
- **S2. Promote the tangent index of Phi to a scaffold covector index (Phi^I_mu coframe)** (003 route (a)); inherits the indefinite-kinetic issues of App H D and requires checking Weinberg-Witten (not checked; its application to NAMCG is unverified).
- **S3. Drop Presentation A's ontological priority (D2)**: not a route to the matrix-derived label and ruled out as a closure by Ch.17.

### Recommendation and next target

Keep R2 as the labelled working model; pursue R4 as the research direction (S1 for authorization only). **Single most promising next target:** in Problem F, compute the Presentation-A one-loop Lambda^2 term for the *vector* and scalar fluctuation sectors of the Yang-Mills matrix action about varying `Theta` (rem:ch3-trace-quadratic extended to nonconstant Theta), using the Laplace-type reduction above, and decide (a) whether a tensor (TT) Einstein-Hilbert term for `K_Theta` survives with a definite sign, and (b) what the dilaton/Pfaffian structure does to the conformal mode (Problem C). Preconditions to state, not assume: the trace map and kinetic term for nonconstant Theta, and the Theta-dependent regulator. Literature context already in the bibliography (`Steinacker2010`, `MantaSteinackerTran2024`, `Steinacker2023`); I verified only the arXiv abstract of 2411.02598, which reports "explicit expressions for the effective Newton constant" on a covariant quantum spacetime with fuzzy extra dimensions; I did not verify that it yields Einstein-Hilbert or compare operators; `Steinacker2023` was not verified.

---

## Q6. Stale passages after the `prop:scaffold` correction (consistent with Q4/Q5)

All edits are minimal rewordings; all DRAFT. They assume label `ass:emergent-op` (Q4). If the author prefers option 2 (remark), substitute "the emergent-background premise of Section~\ref{sec:ch8-which-g}".

1. **ch04 Exercise 7 (L418-423).** Current: "Write one sentence stating when it is legitimate to replace g^(0) by g inside a heat kernel, and what error term that replacement drops. The full answer is Chapter 8; the sentence is due now."
```latex
    Write one sentence stating what must be assumed in order to
    replace \(g^{(0)}\) by \(g\) inside a heat kernel, and why the
    displayed action does not supply it. The full answer is
    Chapter~\ref{ch:heat-kernel}, Assumption~\ref{ass:emergent-op}.
```
(`ch:heat-kernel` is used in ch08-related text of appH; confirm label before use.)

2. **ch08 L56-58.** Current: "Integrate eta at one loop on a slowly varying emergent background g, using Presentation B."
```latex
Integrate \(\eta\) at one loop on a slowly varying emergent
background \(g_{\mu\nu}\), using Presentation~B and
Assumption~\ref{ass:emergent-op}.
```
Also in the same file the exercise at L363-367 ("Expand Proposition~\ref{prop:scaffold} ... Which of them renormalize G_eff?"):
```latex
  \item \textbf{Scaffold error.}
    For \(\bar\Phi=(v+\sigma)\mathbb{I}\) on a flat scaffold, compare
    the \(\LUV^2(\partial\sigma)^2\) coefficient of the one-loop
    action computed with the scaffold operator and with the operator
    of Assumption~\ref{ass:emergent-op}.
```

3. **appG L19-29.** Current: "For a Laplace-type fluctuation operator the heat-kernel expansion on the cone produces the area term ... This is the standard result used in Chapter 6 and Appendix B."
```latex
For a Laplace-type fluctuation operator on the emergent metric
(Assumption~\ref{ass:emergent-op}) the heat-kernel expansion on the
cone produces the area term
```
and keep the remainder (the final sentence already says A,B,C remain open in F). The "standard result" refers to the conical heat-kernel expansion for a Laplace-type operator, not to its application to NAMCG; the rewording makes this explicit.

4. **appB L110-112.** Current: "later identified with the emergent spacetime by Proposition~\ref{prop:scaffold}."
```latex
In Presentation~B the cover is a branched cover of the auxiliary
manifold. Identifying it with the emergent spacetime requires a
specified map \(g^{(0)}\to g\), which the displayed action does not
supply (Assumption~\ref{ass:emergent-op}). In Presentation~A the same
construction requires Problem~A of Chapter~\ref{ch:agenda}.
```
(Chapter label `ch:agenda` is used elsewhere in appH; confirm.)

5. **ch16 inventory and L125-130.** Add the row in Q4 and extend "targets of critical-path Problems A, E and N" to include F for `ass:emergent-op`.

6. Also affected by 003 (not on the author's list): ch05 L249-251 ψ∂∂T clause. Use the gatekeeper's corrected snippet in `review-r1.md` (it drops the A∂T clause).

Effect: removes the places that currently present the emergent-background identification as controlled. No scope or label change. All refs must be re-verified (`\label` existence, duplicates) in the normal proposal round; I did not verify the placeholder chapter labels.

---

## Verification scripts

- `check_weighted_laplacian_a1.py`, output `check_weighted_laplacian_a1.out.txt` (sympy 1.14.0). Checks (i) `L = Lap_G - grad ln rho . grad`, (ii) `L = D^2 - E` with the stated `omega`, `E`, (iii) pointwise equality `sqrt(G)(R_G/6 - E) = rho R[g_rho]/6` on the family `g_rho = diag(e^u,e^-u,e^v,e^-v)`, `u,v,rho` functions of two coordinates. Output: parts 1, 1b zero; part 2 identically zero. Scope: a 4D family, scalar operator, Euclidean algebra; a check, not a proof; not the full Presentation-A calculation.

## Ranking by impact on the infrared / full-GR derivation

Highest impact is Q5 (R4, the Presentation-A kinetic-metric route, is the only identified path to a matrix-derived G_eff, and the preview shows its Lambda^2 term has Brans-Dicke omega=0 structure, affecting C), then Q4 (naming the emergent-background premise and listing it in ch16 makes F's dependency precise and prevents silent reuse), then Q6 (removes stale statements that currently present the premise as derived), then Q2 (notation gloss that keeps N's target unambiguous without a scope change), then Q3 (a sourced statement of nonlocal form factors for N) and Q1 (sign correction in a non-load-bearing appendix, no downstream change). Proposed label changes: none; F, C, B, D1, N and the other critical-path problems stay OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL. The only items needing author action beyond text edits are S1-S3 in the STRUCTURAL section (M5, author only) and the ch16 inventory addition.
