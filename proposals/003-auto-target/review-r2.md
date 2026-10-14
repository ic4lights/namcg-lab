VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M3, M2 | FLAGS: PRIOR-CLAIM-ERROR, AUTHOR-DECISION | PROGRESS: improving | OPEN: 0/0

## Verdict
The mathematics of Items 1–6 holds on independent re-derivation, and all eight r1 findings are closed or reduced to wording. Four minor wording and bookkeeping corrections are required before integration. Item 7 (ch16) must be excluded and returned to the author, because it changes the Chapter 17 completion criterion by cross-reference.

## Source reading
**Full scan.** `scripts/make_digest.py --check` printed `DIGEST CURRENT`. The digest header reads chapters-hash 41a9a98585142521, 30 files, dirty-chapters: no. I read all 30 manifest files in full: ch01–ch18 and appA–appL, including appH L1–1972 and ch17 L1–787. No file was unreadable. The full scan was required because the package changes a definition and assumption (`prop:scaffold` becomes `ass:emergent-op`) and edits a scope-adjacent passage.

I also read, in full:
- `proposal-r2.md` and `proposal-r1.md`
- `review-r1.md`
- 004 `recommendations-r2.md` and `review-r1.md`
- `MILESTONE.md` and the tail of `reports/ledger.md`

The researcher's statement that its own run saw "DIGEST STALE" does not apply: `chapters/` is clean at the digest head. Its "digest + targeted reads" stance rested on the r1 scan, so the full scan above is new.

## Claim under review
The package has six parts:
- **Lemma 1.** At fixed A_μ, with the scaffold operator, the fluctuation operator is −D̄²+E with E derivative-free. The Λ⁴, Λ² and ln Λ terms therefore contain no derivative of Φ̄. The conformal-mode Λ²(∂σ)² coefficient is 0 with the scaffold operator and equals the induced term of `eq:Z-sigma` with the operator on g.
- **Finite conformal-mode term.** ΔZ = (3λ/4π²)(e^{−λv²/Λ²}−e^{−λv²/μ²}) + (λ²v²/12π²)(μ⁻²−Λ⁻²), for p² ≪ μ² ≪ λv².
- **Lemma 2.** A scoped no-go under H1–H4: no linearized-diffeomorphism-invariant, EH or massless Fierz–Pauli form is generated for a fixed linear image of the Φ components.
- **PRIOR-CLAIM-ERROR.** The last sentence of `prop:scaffold` does not follow, and ch05's ψ∂∂T clause is false.
- **`ass:emergent-op`.** A named assumption plus a remark, replacing the Proposition, with the five stale passages reworded.
- **Item 7.** A ch16 inventory row, plus a premise sentence and a chain-item-6 edit.

Original target (Problem F, Ch.17): "evaluate the weighted a_1 and the curvature-linear part of a_2 on the locked block, including diffeomorphism and local-Lorentz ghosts and the radial-mode threshold, with a scheme stated". Completion: "A, B, C and the sign/scheme dependence of G_eff computed from the specified operators; G_eff is not an input".

Current statuses, quoted verbatim from Appendix H (Ch.17 gives "CRITICAL PATH; OPEN." for F, C, B and D):
- **F:** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion."
- **C:** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. A scalar-tensor result is a reduced-scope outcome only when its operator, coupling and phenomenological test are supplied; it does not by itself meet the matrix-derived criterion."
- **B:** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived."
- **D:** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: D2, imposed local Lorentz symmetry, supports only a scope-limited Presentation-B model; D remains OPEN and the matrix-derived criterion is unmet."

The critical-path set in `sec:ch17-done` is A, B, C, D1, E, F, G-derived and N. It matches Appendix H, and the proposal's status table matches both.

## Checks performed
**Scripts.** I re-ran `check_finite_mu_and_mixing`, `check_scaffold_hessian`, `check_bubble_lambda`, `check_invariance_nogo` and `verify_anchors_labels` with `C:\Python312\python`, writing output to the scratchpad. Every output is byte-identical to the saved `.out.txt`. These are checks, not proofs.

**Hand re-derivations.**
- **Hessian blocks.** V₂ = (λ/2)(3φ₀²−v²)Tr h² for Hermitian h, and (λ/2)(φ₀²−v²)Tr κ² for the anti-Hermitian part. At φ₀ = v+σ this gives E_H = λ(v²+3vσ+3σ²/2), E_K = λ(vσ+σ²/2), E_H′ = 3λv, E_K′ = λv, and tr E = 16λ(v²+4vσ+2σ²).
- **Cutoff dependence.** ∂_ΛI = 2Λ⁻¹f(Λ⁻²). In a₂ (`eq:appA-a2`) a derivative of E appears only in D²E, a total derivative. The (∇E)² term first appears in a₃.
- **Counterexample chain.** √gR = 6(∂Ω)² up to a total derivative. With `eq:universal-R` and N₀ = 32 this gives −N₀Λ²(∂σ)²/(32π²v²) = −(1/π²v²)Λ²(∂σ)². With 1/(16πG) = N₀Λ²/(192π²) this is the Euclidean image of +3(∂σ)²/(8πGv²) in `eq:Z-sigma`. ✓
- **ΔZ normalization.** The Duhamel second order of ½Tr ln gives W ⊃ −(n/4)E′²∫σσB with B = (1/16π²)∫dx[E₁(M/Λ²)−E₁(M/μ²)]. Hence ΔZ = 2×coefficient of (∂σ)² = −(n/2)E′²B′(0).
  - **Massive block.** B′(0) = −(e^{−m²/Λ²}−e^{−m²/μ²})/(96π²m²), giving ΔZ_H = (3λ/4π²)(e^{−λv²/Λ²}−e^{−λv²/μ²}). ✓
  - **Massless block.** B′₀(0) = (Λ⁻²−μ⁻²)/(96π²), giving ΔZ_K = (λ²v²/12π²)(μ⁻²−Λ⁻²). ✓
  - This equals my own r1 value (my `gk_ircut.py`), and the numerical cross-checks in the script agree to 8–9 digits.
  - Both terms are positive for μ<Λ, and neither carries a Λ² or ln Λ piece.
- **ψ–T orthogonality.** Tr(ηT) = 0, so the kinetic cross term is 0 and ∂²V/∂a∂b = 0 at Φ̄ = vI. The script agrees. The ch05 snippet in Item 5 is identical to the corrected snippet in my r1 review.
- **Lemma 2.** Pure scaffold rotations leave `eq:Smicro` and `eq:D-both` invariant. The Φ components, being scalars, do not rotate. So F_ab(Rp) = F_ab(p), and the kernel depends on p² only. The mixed and connection kernels have the forms p_μ f(p²) and αδ+βpp (no ε-structure is possible with one vector). Their Schur complement keeps the p²-only form.
  - **Reduced form.** If Γ(h,r) is shift-invariant, Q(h) = ext_r Γ is shift-invariant. This holds provided the r-block is eliminable (see Lemma 2 scope below).
  - **Annihilation argument.** Because Q_{p′} = Q_p for p′² = p², invariance annihilates p′⊗ξ+ξ⊗p′ for every p′ on the sphere. These tensors span Sym² for p ≠ 0, so Q = 0. The traceless block with `eq:FP-gauge` is handled by the script.
  - **Direction dependence.** The linearized EH and FP forms depend on the direction of p, so a nonzero multiple cannot equal a p²-only form. The Feynman–de Donder form p²(h·h−½h²) is p²-only, as stated.

**Anchors and labels (direct).**
- Every ch08, ch04, ch05, appB, appG and ch16 replacement anchor occurs exactly once. The appH insertion anchor `\section{Problem G: HBEV}` occurs once, preceded by "…sector sum. Problems~B, C, D, F and~G remain open."
- Every existing label used is defined exactly once, including `ch:vierbein-emergence`, `ch:heat-kernel`, `ch:agenda`, `sec:ch8-which-g`, `rem:ch3-varying-theta` and `lem:msigma`.
- `ass:emergent-op` and `rem:ch8-scaffold-vs-emergent` occur nowhere now, so they are not duplicates.
- `prop:scaffold` has exactly three occurrences: its definition at ch08 L288, appB L112, and ch08 L364. All three are replaced in this package. Nothing else depends on it.
- `\LUV` is defined at `namcg-book7.tex` L54, and the files are CRLF.

**Not verified.** I did not compile the LaTeX (no build, by role). No external literature is used. Weinberg–Witten, `Steinacker2023` and arXiv 2411.02598 are not used in the LaTeX and are not independently verified.

## Re-verification of r1 findings
1. **Closed.** ch05 uses my snippet verbatim. The A∂T clause is kept as scoped, and the PRIOR-CLAIM-ERROR is restricted to ψ∂∂T.
2. **Closed in substance.** The fixed-A_μ qualifier is present throughout the ch08 and appH text. The general "no composite-metric EH term" claim is attributed to Lemma 2. One residual overstatement is new finding 1 below.
3. **Closed.** Finite μ is kept, and ΔZ_K is added and matches my value.
4. **Closed.** The wording is now "is not produced in this calculation; in the manuscript it arises from the induced Einstein–Hilbert term…".
5. **Closed.** The reduced (Schur-complement) form is stated as the physical criterion.
6. **Partly closed.** appB no longer cites `prop:scaffold`, but the wording is not the one I suggested (new finding 2).
7. **Closed.** Five stale passages are rewritten and ch16 is separated as Item 7. A further stale passage found in the full scan is new finding 3.
8. **Closed.** The decision is a named assumption plus a remark with the counterexample. Its content is the premise already called a "Presentation-B assumption" at ch04 L217–222 and appH L1194–1199. It adds no new physical hypothesis and is not a core-assumption change, but it is a defined-assumption edit. The author will see it at merge.

## Findings
1. **Minor, required.**
   - **Location:** appH Item 1 paragraph 1 ("No Λ-dependent term contains a derivative of Φ̄") and the ch08 remark ("no Λ_UV-dependent term of the one-loop action contains a derivative of the condensate").
   - **Finding:** Read literally, the statement is false by the package's own results. ΔZ_H carries e^{−λv²/Λ²}, and a₃ and higher terms give (∂E)²Λ⁻² corrections. In appH the qualifier "up to terms that vanish as Λ→∞" sits a sentence earlier. The ch08 remark has no such qualifier.
   - **Required action:** Restrict the statement to the terms that grow with Λ, as in the snippet below.
2. **Minor, required.**
   - **Location:** Item 3 (appB).
   - **Finding:** The new text says identification "requires that the fluctuation operator be built from the emergent metric". That is a necessity claim the package does not prove. It is not the closer wording of appH L72–75 that r1 suggested, "requires a specified map between them".
   - **Required action:** Use the snippet below.
3. **Minor, required to list; editing optional.**
   - **Location:** ch03 L77–78, "The auxiliary metric is a scaffold for writing derivatives and heat kernels. Chapter~8 uses this scaffold."
   - **Finding:** After `ass:emergent-op` this directly contradicts ch08, which now says its operator is built on g, not on the scaffold. It is not in the researcher's stale list.
   - **Required action:** Add it to the "Stale passages elsewhere" list, or edit it as in the snippet below. The edit is wording only.
4. **Minor, required.**
   - **Location:** Item 1 paragraph 3, `E_1`.
   - **Finding:** `E_1` is the exponential integral. It is defined only later in appH (L1267) and sits near `E`, `E_H` and `E_K`. A reader of the inserted paragraph cannot tell what it is.
   - **Required action:** Add "with \(E_1(x)=\int_x^\infty e^{-t}t^{-1}\,\mathrm dt\)" at first use.
5. **Scope classification for Item 7 (AUTHOR-DECISION).**
   - **Chapter 17 definitions.** Ch.17 L80–84 says "each load-bearing assumption must be discharged by one of them" (the critical-path problems). Ch.17 L91–96 defines the Completed-derivation label as one where "no load-bearing assumption of Chapter~ch:falsifiers remains assumed in their chains". The Ch.17 text at L693–695 lists the specific assumptions that disqualify a chain.
   - **Effect of Item 7.** A new `load-bearing` row, together with the sentence "Problem~F must discharge" it, adds `ass:emergent-op` to that class by cross-reference. It tightens what F must show without editing Ch.17. That is a change to the completion criterion's scope, hence AUTHOR-DECISION under the directive. It is not a pure bookkeeping edit.
   - **Consequence.** The Ch.17 F target ("computed from the specified operators") plausibly already implies it, but that is for the author to rule on. This agrees with 004 review-r1, which marked the ch16 inventory entry an author-approval item.
   - **Separability.** Items 1–6 do not depend on Item 7. The ch08 remark's "Discharging … is part of Problem~F" and the appH sentence "the missing step of Problem~F includes discharging…" are consistent with ch04 L221–222 ("remains part of Problem~F") and Ch.17's F Missing step ("Specify the gauge-fixed quadratic Hessian…"). They edit neither Ch.17 nor the F target.
   - **Interim gap.** Until the author rules on Item 7, `ass:emergent-op` is a named assumption absent from the ch16 inventory. That is a bookkeeping gap, not an error.

**Lemma 2 scope.** Lemma 2 is scoped to H1–H4 and does not overclaim.
- The text lists the hypotheses.
- It states that the reduced form is the criterion.
- It names the relaxations (a Θ-built regulator, a non-invariant vacuum, a curved scaffold, a non-linear composite map) as pointers, and does not claim they work.
- The Weinberg–Witten theorem is not invoked.
- It says it extends, and does not contradict, appH L765–791 and L926–966 on FP structures being "not excluded".
- One unstated condition is implicit: the eliminated r-block must be non-degenerate, or gauge-fixed in a rotation-preserving way. That is covered by H2 and need not be spelled out.

## Scope of what is established
**Established (proof or sympy check).**
- Lemma 1 at fixed A_μ with the scaffold proper-time regulator.
- The conformal-mode counterexample.
- The finite ΔZ at one loop with A_μ = 0 fixed, p² ≪ μ² ≪ λv².
- Lemma 2 under flat scaffold, rotation-preserving regulator and gauge fixing, rotation-invariant vacuum, and h a fixed linear image of the Φ components.
- The ψ–T orthogonality at tree level.
- The merged-text errors: `prop:scaffold`'s final sentence (load-bearing for reading `thm:Geff` as a statement about the emergent metric) and ch05's ψ∂∂T clause (non-load-bearing).

**Input.** `ass:emergent-op` is a premise, not a result, and F must discharge it.

**Not covered.**
- The A_μ-integrated Lemma 1.
- Θ-dependent regulators and Presentation A.
- Curved scaffolds.
- Any value or sign of G_eff.
- Weinberg–Witten applicability.

**Status.** No problem is closed. F, C, B, D and the rest of the critical-path set stay OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL. No label changes, so no `LABEL-CHANGE-PROPOSED` flag.

**Emergence.** Preserved. g^(0) stays a non-dynamical scaffold. The metric remains the composite of Chapter 4. The package shows that the displayed action on the scaffold does not supply the emergent-metric operator. It does not make any metric fundamental.

**Milestones.**
- **M3** holds: the final inference of `prop:scaffold` is a false implication in a merged paragraph. I judge it load-bearing for `thm:Geff`.
- **M2** holds as a bounded no-go within H1–H4.
- **M1:** no. Nothing on the critical path is derived.
- **M4:** no.
- **M5:** not triggered by Items 1–6. Item 7 is the author-decision item.

**BREAKTHROUGH:** not warranted. This is a bounded no-go plus a correction, with no critical-path step derived.

## Recommended disposition
Integrate Items 1–6 after the four minor corrections. Do not integrate Item 7 (the three ch16 edits).

**Accepted for integration:**
- **Item 1:** the three appH paragraphs before `\section{Problem G: HBEV}`, with findings 1 and 4 applied.
- **Item 2:** (a)–(d) in ch08, with finding 1 applied to the remark.
- **Item 3:** appB, with finding 2.
- **Item 4:** ch04 Exercise 7 and appG.
- **Item 5:** ch05, verbatim.
- **Item 6:** merged into Items 2–4.

**Excluded and deferred:**
- **Item 7:** the ch16 inventory row, the "premise of Theorem thm:Geff that Problem F must discharge" sentence, and the chain-item-6 rewrite. Return to the author with the Ch.17 cross-reference. The optional ch17 sentence in F's Missing step is also an author call.

PRIOR-CLAIM-ERROR stops the loop for the author at integration, per `MILESTONE.md`.

## Corrected snippet
No new physics is needed. The only assumption is the scope already stated.

**Finding 1, appH Item 1 (replaces "No \(\LUV\)-dependent term contains a derivative of \(\bar\Phi\) outside a total derivative."):**
```latex
No \(\LUV^4\), \(\LUV^2\) or \(\ln\LUV\) term contains a derivative of
\(\bar\Phi\) outside a total derivative; terms with derivatives of
\(\bar\Phi\) have coefficients that are independent of \(\LUV\) or vanish
as \(\LUV\to\infty\).
```

**Finding 1, ch08 remark (replaces the clause "no \(\LUV\)-dependent term of the one-loop action contains a derivative of the condensate"):**
```latex
no term of the one-loop action that grows with \(\LUV\)
(\(\LUV^4\), \(\LUV^2\), \(\ln\LUV\)) contains a derivative of the
condensate
```

**Finding 2, appB (replaces the second and third sentences of the Item 3 text):**
```latex
Identifying it with the emergent spacetime requires a specified map
from the auxiliary metric to the emergent metric, which the displayed
action does not supply (see Assumption~\ref{ass:emergent-op}). In
Presentation~A the same construction requires Problem~A of
Chapter~\ref{ch:agenda}.
```

**Finding 3, ch03 L77–78 (optional edit; replaces "Chapter~8 uses this scaffold."):**
```latex
Chapter~8 writes its heat kernel on the emergent metric under
Assumption~\ref{ass:emergent-op}.
```
This uses a label defined by the package, so it takes effect only with Item 2.

Files reviewed and relevant:
- `C:\Users\redgi\Projects\namcg-lab\proposals\003-auto-target\proposal-r2.md`
- `C:\Users\redgi\Projects\namcg-lab\proposals\003-auto-target\review-r1.md`
- `C:\Users\redgi\Projects\namcg-lab\proposals\003-auto-target\check_finite_mu_and_mixing.py`
- `C:\Users\redgi\Projects\namcg-lab\chapters\ch08-heat-kernel.tex`
- `C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex`
- `C:\Users\redgi\Projects\namcg-lab\chapters\ch16-falsifiers.tex`
- `C:\Users\redgi\Projects\namcg-lab\chapters\ch17-agenda.tex`
