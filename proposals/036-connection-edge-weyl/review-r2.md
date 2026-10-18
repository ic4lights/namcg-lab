VERDICT: ACCEPT | MILESTONE: none | FLAGS: PRIOR-CLAIM-ERROR | PROGRESS: improving | OPEN: 0/0

## Verdict
All five r1 findings are closed and nothing else in the LaTeX changed, so r2 is accepted for integration. The PRIOR-CLAIM-ERROR flag stays because the package corrects the merged 035 ASD sentence.

## Source reading
Digest plus targeted reads, not a full scan.
- I read `proposal-r2.md` in full, `review-r1.md` in full, and `appH_insert.tex`.
- I read the working-tree `chapters/appH-microscopic-proofs.tex` around the 035 clause and the anchor.
- No new mathematics was introduced in r2. I rely on my r1 re-runs of the scripts (outputs matched) and the r1 analytic chirality check, which still apply unchanged.
- `appH` is dirty with the accepted 032, 033 and 035 integrations, as expected. I applied `CLAUDE.md` 3(d) by reading the affected passages.
- `proposals/034-*` is ignored, as instructed.

## Claim under review
The claim is a bounded no-go. Edge, endomorphism and holonomy contacts of the vector/connection sector do not supply the missing `-2κ_X W` of the completed Weyl gap `2κ_X`, within the 033 setting. The package also corrects the integrated 035 ASD clause.

Appendix H, verbatim:
- Problem B: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL."
- Problem A: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label."

Chapter 17 (A, B, C, D1, E, F, G-derived, N required; H, I, J optional) is unchanged and consistent with Appendix H. No label is touched.

## Checks performed
A script compared the r2 block, `appH_insert.tex`, the r1 block and the working-tree `appH` text.
- **F1: PASS.**
  - Section (b) records the old string and the new string verbatim.
  - The old string `and \(-N_{\mathrm{tot}}c_b/15+2\kappa_X(1-c_b)\) about an anti-self-dual one` occurs exactly once in the working tree, in the 035 paragraph.
  - After replacement the sentence reads "...the same expression about an anti-self-dual one with \(\Theta^{34}=-r^{-\epsilon c_b}\), for which \(H=c_a\mathcal J_{12}-c_b\mathcal J_{34}\), and equals \(2\kappa_X\) at \(c_b=0\)."
  - "The same expression" refers to the SD expression `-N_tot c_b/15 + 2κ_X(1+c_b)`, which is the `c_a=1` case of the exponent-parametrised gap I confirmed in r1.
  - The trailing clause is grammatical.
- **F2: PASS.** The comparator sentence is present, verbatim as in my r1 snippet, directly after "...without a singular metric on \(\Sigma\)."
- **F3: PASS.** The endomorphism sentence now reads "...which vanishes at first order about constant \(\bar\Theta\)".
- **F4: PASS.** The DW wording is now "does not treat the dependence on the Weyl tensor, and leaves that on the extrinsic geometry open".
- **F5: PASS.** "stated above" is replaced by "of the preceding paragraph".
- **No other changes: PASS.** A line diff of the r1 and r2 blocks shows changes only in four paragraphs (endomorphism, edge, holonomy, closing). In each, the difference is exactly the F2–F5 edit.
- **`appH_insert.tex`: PASS.**
  - It equals the r2 block exactly.
  - It has 0 TAB characters, no bytes above 127 (pure ASCII), and no carriage returns (LF). The integrator converts to CRLF.
  - Escapes are intact.
- **Anchor: PASS.** `\section{Problem C: conformal mode and Cassini}` occurs exactly once. It is immediately preceded by the blank line after the 035 block, which ends "...Problem~B stays open and PROGRAMME-CONDITIONAL."
- **Labels: PASS.** The block has no `\label` and no `\ref`, and one `\cite{DonnellyWall2016}` (key present, per r1). So there are no label changes.
- **Closing line.** There is one scoped status sentence, "Problem~B stays open and PROGRAMME-CONDITIONAL.", with no repeated closing lines.
- **Emergence.** Nothing makes spacetime or the metric fundamental.
- **Builds.** I did not rebuild. The proposal reports a scratch compile with both edits (301 pages, no undefined or multiply-defined references). Run `scripts/build_check.py` after integration.

## Findings
None.

## Scope of what is established
- **Established (conditional, sampled jets and symbolic).**
  - Setting: the 033 test modes, totally geodesic Σ, first order in 1−n on the n<1 branch, the completed replica, Poisson-limit one-loop operators, α=1.
  - In the `(G,ρ,∂Θ)` presentation, endomorphism contacts have no W coefficient.
  - The diagonal-profile holonomy gap is the same for both chiralities in the exponent parametrisation, `N_tot(3c_a−2c_b−3)/30 + 2κ_X(2−c_a+c_b)`.
  - No diagonal-family profile closes the gap for all contents.
  - The merged 035 ASD formula was wrong and is corrected.
- **Conditional on hypotheses.**
  - The edge density is W-free only if the edge operator is the intrinsic abelian one of the DW classes. DW do not treat the Weyl dependence and leave the extrinsic geometry open.
  - The vector/Dirac edge-content premise is hedged in the text ("if it carries...").
- **Not derived.** The extended cross-term rule for `c_b≠0`, the dropping of the Euler W part, and the "holonomy-type missing ingredient" conjecture.
- **Status.** B and A remain OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. This is not a breakthrough.
- **Open avenues, ranked.**
  1. The comparator: the metric-universal `12κ_C^T` (−4κ_X) against the Noether/Wald entropy in `(G,ω)` (−2κ_X, equal to the replica). This is a second-order first-law question with variation of both G and ω, and it could turn the gap into a comparator artefact.
  2. Off-diagonal or equivariant profiles with a J_34 circulation and a regular Σ metric.
  3. The exact heat trace of the cone with holonomy, replacing the cross-term rule.
  4. The non-delta 1/r singular parts of ω and ln ρ.
  5. Edge algebra of the symplectic gauge group (non-abelian).
  6. Non-totally-geodesic Σ.
- **Hypotheses a within-core route could relax.** The comparator choice (rank 1), the diagonal family (rank 2) and the cross-term rule (rank 3).

## Recommended disposition
Integrate as-is, as integration ordinal 33. Exactly two items are accepted.

1. **Replacement of one 035 clause in `chapters/appH-microscopic-proofs.tex`.** The old string occurs exactly once. The rest of the sentence and the paragraph stay unchanged.

   Old string, verbatim:
   ```latex
   and \(-N_{\mathrm{tot}}c_b/15+2\kappa_X(1-c_b)\) about an anti-self-dual one
   ```
   New string, verbatim:
   ```latex
   and the same expression about an anti-self-dual one with \(\Theta^{34}=-r^{-\epsilon c_b}\), for which \(H=c_a\mathcal J_{12}-c_b\mathcal J_{34}\)
   ```

2. **The new block, exactly as in `C:\Users\redgi\Projects\namcg-lab\proposals\036-connection-edge-weyl\appH_insert.tex`.** It starts at `\paragraph{Edge and contact terms of the vector and connection sector at the Weyl coefficient (conditional; not closure).}` and ends "...Problem~B stays open and PROGRAMME-CONDITIONAL." Insert it followed by one blank line, immediately before the unique `\section{Problem C: conformal mode and Cassini}` and after the 035 block. Convert to CRLF and write UTF-8 without BOM.

## Corrected snippet
None needed.
