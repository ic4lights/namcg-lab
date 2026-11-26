VERDICT: ACCEPT | MILESTONE: M2 | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
All six r1 findings (F1–F6) are closed. The manuscript paragraph is a bounded conditional obstruction for H_A, with no label change, and spacetime stays emergent.

## Source reading
Digest plus targeted reads. `make_digest.py --check` printed DIGEST CURRENT. This is not a full scan. In r1 I read in full the following:
- Appendix H, Problem F and the 005 paragraph, and the Problem A label.
- ch08 `ass:emergent-op`.
- ch03 `def:matrix-coords`, `eq:V`, `rem:ch3-moyal-check` and `rem:ch3-trace-quadratic`.
- ch04 `eq:vev-is-frame`.

This round I diffed r2 against r1, re-read the full r2 text, and re-checked the anchor and labels. The proposal changes no definition, assumption or scope text. I did not compile LaTeX.

## Claim under review
The target is to discharge `ass:emergent-op` (Problem F, with A, B, C and D1 by dependency). The proposal does not derive it. It records a conditional obstruction in the class H_A. Quoted verbatim from Appendix H:
- F: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion."
- A: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL."

Chapter 17 still lists A, B, C, D1, E, F, G-derived and N. No label change is proposed.

## Checks performed
- **Scripts.** I re-ran `check_linear_response.py` and `check_embedding_and_vacuum.py`, and both are identical to the saved `r2_*.out.txt`. I ran `verify_anchors_labels.py`.
- **r1 independent checks.** My earlier checks (own finite-difference rank 3 against 6, the sl2+sl2 kernel argument, `K = c g^{-1}` impossibility, gauge counting 4−1=3) cover the unchanged algebra. The r2 changelog says no computation changed, and the diff confirms only wording changed.
- **Anchor.** The sentence "do not apply; no linearized-diffeomorphism invariance is claimed." occurs once (appH L1812). Together with "Problems~B, C, D and~F remain open." (L1813) the anchor is unique. The same closing phrase also appears at L1648 as a different paragraph's ending, so the anchor must include the L1812 clause. The anchor is immediately followed by `\section{Problem G: HBEV}`.
- **Labels.** Each of `thm:Geff`, `eq:O-eta`, `ass:emergent-op`, `rem:ch3-moyal-check`, `rem:ch3-trace-quadratic`, `def:composite-metric`, `eq:g-from-e`, `eq:vev-is-frame`, `eq:V` and `ass:EE` occurs once. No new labels are introduced.
- **LaTeX.** The inserted paragraph has no process language and balanced math. It has no repeated closing-status lines: there is one closing scoped sentence.

## Re-verification of F1–F6
- **F1 (major), closed.** The embedding reading is labelled "an assumed dictionary not contained in the four-matrix class". `K ≠ c g^{-1}` is stated pointwise for any real Lorentzian g. The text now says G has the form `eq:g-from-e` for the Θ-coframe. The conclusion is scoped to the embedding reading. This matches my corrected snippet.
- **F2 (major), closed.** The text now says the tensor equation E[h]=T, "and any linear local relation", holds only on a subspace of dimension at most 3 of the 6-dimensional space of conserved sources. "Conserved" is defined as p^μT_μν=0. Varying a^μ gives only the projection. An extra conserved stress is not excluded and "would have to be derived". The overreaching "whatever the coefficients" phrase is gone.
- **F3, closed.** The text now says "codimension four ... lies in the set cut out by this relation", with no claim of sufficiency.
- **F4, closed.** The N−1+4≥11 parenthetical is absent from the manuscript text. N≥8 appears only under "Decisions Taken", which is not manuscript text.
- **F5, closed.** The notation fixes are in place:
  - ℓ is defined.
  - Orthogonality is stated as n^T K̄ p=0.
  - The circle product a∘b := ab^T+ba^T is defined.
  - e₀ and J are defined.
  - The vacuum statement gives the δ contraction and the real locked block.
  - The 3-versus-7 count is marked "a counting argument (not a derived result)".
- **F6, closed.** The rank-five statement now refers to the differential of Θ→K for Θ≠0, Pf Θ=0.

## Findings
None blocking or major. Minor note, no action required: the paragraph is dense but is the smallest accurate record.

## Scope of what is established
**Exact hypotheses of H_A.**
- Four Hermitian matrix coordinates, in the Poisson limit.
- Matrix indices contracted with constant η.
- Real nondegenerate Θ.
- Linear order about a constant Θ̄, with generic p.

**Established inside H_A** (exact algebra, symbolic and rational checks; checks are not proofs):
- Rank 6 of Θ→G at Pf≠0, and the quadratic image relation (codimension four).
- A 3-dimensional linear response.
- A rank-3 linearised Einstein operator against 6 conserved sources. Any linear local relation is bounded the same way. Hence E[h]=T cannot hold for generic conserved T without an additional conserved stress.
- `K ≠ c g^{-1}` pointwise for real Lorentzian g.
- A tree-level quadratic action that is algebraic in (δG, δρ).

**Conditional:**
- The vacuum-manifold mismatch, which applies only if e is identified with ⟨Φ⟩/v.
- The nonlinear 3-versus-7 count (a counting argument).

**Not established:**
- ⟨Φ⟩/v as the coframe.
- Any value or sign of G_eff.
- Anything for Presentation B with an independent Φ.
- Moyal corrections.
- T_ent.

Hypotheses a within-core route could relax (named only; no research originated): a derived extra conserved stress; Moyal corrections; non-constant backgrounds; fermion and scalar content; Presentation B; more matrix coordinates (pre-approved future structural route, not in this text). F, A, B, C and D stay OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL. There is no label change and no closure by scope. The metric stays emergent: G is built from Θ, and the embedding dictionary is only an assumed reading.

M2 applies (bounded new obstruction). It is not M1, M3, M4 or M5 for this text, and it is not a BREAKTHROUGH. N≥8 is not in the text, so no M5 or AUTHOR-DECISION arises here.

## Recommended disposition
Integrate as-is at ordinal 6.

What is accepted: exactly the LaTeX block in proposal-r2.md under "Proposed changes" (the single `\paragraph{Presentation~A in the Poisson limit: what four matrix coordinates can supply (conditional; not closure).}` with its four paragraphs). Insert it after the 005 paragraph, immediately after the sentence ending "...no linearized-diffeomorphism invariance is claimed. Problems~B, C, D and~F remain open." at appH L1812–1813 and before `\section{Problem G: HBEV}`. Nothing is replaced. The "Decisions Taken", milestone and remaining-step sections are not manuscript text and are not accepted as text. Preserve CRLF line endings. Run `scripts/build_check.py` after integration.

## Corrected snippet
None needed.
