VERDICT: ACCEPT | MILESTONE: M3, M2 | FLAGS: PRIOR-CLAIM-ERROR | PROGRESS: improving | OPEN: 0/0

## Verdict
Items 1–5 of r3 apply all four r2 findings correctly, Item 7 is fully removed, and every anchor and label checks out. The mathematics is unchanged from r2, where I re-derived it in full. Accepted for integration is Items 1–5, with Item 6 merged into Items 2–4.

## Source reading
Digest + targeted reads. `make_digest.py --check` printed `DIGEST CURRENT` at chapters-hash 41a9a98585142521, and the git tree is clean.
- My r2 full scan covers the same text. The diff touches no passage beyond the ch03 line, so no new full scan was needed.
- I read `proposal-r3.md` in full, `review-r2.md` in full, the r2→r3 diff, and the ch03 passage (L72–80).
- This is not the 5th-item full-scan case.
- No unreadable files.

## Claim under review
The claim is unchanged from r2. It has four parts:
- a scaffold no-go (Lemma 1) at fixed A_μ, with the scaffold operator;
- the finite ΔZ;
- Lemma 2, a no-go scoped to H1–H4;
- the correction of `prop:scaffold`/ch05, with `ass:emergent-op` recorded as a named assumption.

Original target (Problem F), unchanged: "evaluate the weighted a_1 and the curvature-linear part of a_2 on the locked block, including diffeomorphism and local-Lorentz ghosts and the radial-mode threshold, with a scheme stated".

Appendix H, quoted verbatim:
- F: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion."
- C, B and D keep the same OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL statuses with their qualifiers, quoted in review-r2. The proposal does not touch them.

The Chapter 17 critical-path set is A, B, C, D1, E, F, G-derived and N. This is unchanged and matches Appendix H.

## Checks performed
**Diff of r3 against r2.** I diffed Items 1–5 directly. The only changes are the four r2 findings and the ch03 edit; Items 2(a)–(d) and 5 are unchanged.

**r2 findings.**
1. **Closed.**
   - The appH sentence now reads "No Λ⁴, Λ² or ln Λ term contains a derivative of Φ̄ … terms with derivatives of Φ̄ have coefficients independent of Λ or vanishing as Λ→∞". This is my snippet verbatim.
   - The ch08 remark now reads "no term … that grows with Λ_UV (Λ⁴, Λ², ln Λ) contains a derivative of the condensate". Also verbatim.
   - Residual wording: the "Result" section of the proposal restates the claim with the same restriction, and the claim table says "no Λ⁴, Λ² or ln Λ term". No unrestricted "Λ-dependent" statement remains in the integration text. I searched for it.
2. **Closed.** The appB text is my snippet verbatim: "requires a specified map from the auxiliary metric to the emergent metric, which the displayed action does not supply (see Assumption~\ref{ass:emergent-op})". The remaining sentences are unchanged.
3. **Closed.**
   - The ch03 edit is now Item 4(c). It replaces "Chapter~8 uses this scaffold." with "Chapter~8 writes its heat kernel on the emergent metric under Assumption~\ref{ass:emergent-op}."
   - I checked the anchor in the source. Lines 77–78 read "…The auxiliary metric is a scaffold for writing derivatives and heat kernels. Chapter~8 uses this scaffold." The phrase "Chapter~8 uses this scaffold." occurs exactly once (grep). It does not break across lines inside the phrase itself.
   - The text depends on the label defined in Item 2(b), so it must be integrated with Item 2. The proposal states this.
   - This is wording only, and it removes a direct contradiction with the new ch08 text.
4. **Closed.** E_1 is defined at first use in appH paragraph 1: "with E_1(x)=∫_x^∞ e^{-t}t^{-1}dt, the exponential integral". The preceding display now ends with a comma. LaTeX is syntactically fine: `\mathrm dt` matches the manuscript's later use.

**Item 7.** In the integration text (Items 1–6) I grepped for ch16, `ch:falsifiers` and "inventory" and found nothing. Item 7 reads "Removed in r3". The queued ch16 edits and the optional ch17 sentence appear only in "Stale passages" and "Author decision needed", and the proposal says neither is needed by Items 1–5. The only label that Items 1–5 depend on from the ch16 context is `ass:emergent-op`, which Item 2 defines. Nothing else from Item 7 is used.
- Two sentences remain that mention F discharging `ass:emergent-op`: the appH sentence and the ch08 remark's last sentence. They are consistent with ch04 L221–222 and with the Chapter 17 F missing step. They edit neither Chapter 17 nor F's target. I judged this in r2 and still hold that view.

**Scripts.**
- I re-ran `verify_anchors_labels_r3.py` with `C:\Python312\python`. The output is byte-identical to the saved `verify_anchors_labels_r3.out.txt` and ends `PROBLEMS 0`.
- Every anchor occurs exactly once. Every existing label used is defined exactly once (printed 1 for each, including `rem:ch3-varying-theta`).
- `ass:emergent-op` and `rem:ch8-scaffold-vs-emergent` occur 0 times now, so they will be defined once on integration (Item 2(b)).
- `prop:scaffold` has exactly three occurrences: ch08 L288, appB L112 and ch08 L364. The package replaces all three: Item 2(b) replaces the definition, Item 3 the appB sentence, and Item 2(d) the exercise at ch08 L364.
- I did not re-run the physics scripts (hessian, bubble, finite-μ, invariance). They are unchanged and I checked them in r2. The central equations were re-derived by hand in r2.

**Not verified.** I did not compile the LaTeX; the integrator's `build_check` does. No external citations are used in the LaTeX.

## Findings
None. Blocking: 0. Major: 0. Minor: 0.

Advisory, no action required (RESEARCHER-DECISION is not triggered):
- The proposal's own source-reading paragraph says the r1 full scan stands. My r2 full scan is the operative one and covers the same text.
- The text relies on `ass:emergent-op` being absent from the ch16 inventory until the author rules. That is a bookkeeping gap, not an error.

## Scope of what is established
**Proved under stated conditions.**
- Lemma 1 holds at fixed A_μ with the scaffold proper-time regulator. The Λ⁴, Λ² and ln Λ terms contain no derivative of Φ̄.
- The conformal-mode counterexample shows the scaffold Λ²(∂σ)² coefficient is 0, while the operator on g gives the induced term of `eq:Z-sigma`.
- The finite ΔZ holds at one loop, with A_μ = 0 held fixed and p² ≪ μ² ≪ λv².
- Lemma 2 holds under H1–H4: flat scaffold, rotation-preserving regulator and gauge fixing, rotation-invariant vacuum, and h a fixed linear image of the Φ components. Within that class, at any loop order, no linearized diffeomorphism invariance, EH form or massless FP form is generated. It is explicitly not a no-go for a composite-metric EH term in general.
- The ψ–T orthogonality at tree level, and the false merged claims in `prop:scaffold` (load-bearing for reading `thm:Geff` as a statement about the emergent metric) and in ch05 (ψ∂∂T clause, non-load-bearing).

**Input, not derived.** `ass:emergent-op` is an assumption that F must discharge.

**Hypotheses a within-core route could relax**, which are not excluded and not shown to work:
- a regulator or kinetic metric built from Θ^{μν} (Presentation A);
- a vacuum or background not invariant under scaffold rotations;
- a curved scaffold;
- a composite metric that is not a fixed linear image of Φ.

**Status.** No problem is closed, no label changes, so there is no `LABEL-CHANGE-PROPOSED` flag. F, C, B and D remain OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

**Emergence.** Spacetime stays emergent. g^(0) remains a non-dynamical scaffold, and the metric is still the composite of Chapter 4.

**BREAKTHROUGH:** not warranted. This is a bounded no-go plus a correction, with no critical-path step derived.

**Milestones.**
- M3 holds: a false implication in merged text.
- M2 holds: a bounded no-go.
- M1, M4 and M5 do not hold. The ch16 and ch17 items that could have affected scope are removed from the package.

## Recommended disposition
Integrate as written. The integrator should apply Items 1–5 together:
- **Item 1:** the three appH paragraphs before `\section{Problem G: HBEV}`.
- **Item 2:** (a)–(d) in ch08.
- **Item 3:** appB.
- **Item 4:** (a) ch04 Exercise 7, (b) appG, and (c) ch03.
- **Item 5:** ch05, verbatim.
- **Item 6:** merged into Items 2–4.

Item 4(c) must not be applied without Item 2, because it uses `ass:emergent-op`. After integration, `build_check` should confirm no undefined references. PRIOR-CLAIM-ERROR stops the loop for the author at integration, per `MILESTONE.md`.

**Excluded and returned to the author.**
- Item 7: the ch16 inventory row, the premise sentence and the chain-item-6 edit.
- The optional ch17 F "Missing step" sentence.

## Corrected snippet
None needed.

Files: `C:\Users\redgi\Projects\namcg-lab\proposals\003-auto-target\proposal-r3.md`, `C:\Users\redgi\Projects\namcg-lab\proposals\003-auto-target\review-r2.md`, `C:\Users\redgi\Projects\namcg-lab\proposals\003-auto-target\verify_anchors_labels_r3.py`, `C:\Users\redgi\Projects\namcg-lab\chapters\ch03-matrix-action.tex`.
