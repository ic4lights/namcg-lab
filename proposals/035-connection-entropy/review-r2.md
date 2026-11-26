VERDICT: ACCEPT | MILESTONE: none | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
All three required wording fixes from review-r1 are applied by substitution. Nothing else in the LaTeX changed, and the insert and anchor check out. The mathematics was verified in r1 and is unchanged.

## Source reading
Digest plus targeted reads.
- The digest is stale (`dirty-chapters`), as expected from the accepted but uncommitted 032/033 integrations.
- I did not do a full scan. Ordinal 32 is not a 5th item, the block changes no scope statement, and there is no PRIOR-CLAIM-ERROR.
- I read in full: `proposal-r2.md`, the diff r1 to r2, `appH_insert.tex`, the git diff of the insert between r1 (747c4b0) and r2 (550faea), and `review-r1.md`.
- I read the appH tail around the anchor (lines 268–275).
- The scripts and outputs are unchanged. They were re-run and confirmed in r1, and I did not re-run them.

## Claim under review
Problem B (sec:status-B), whose status is "Status OPEN, Priority CRITICAL PATH, Completion PROGRAMME-CONDITIONAL". The original target is tensor-block stationarity and the area/G relation.

The proposal gives a bounded conditional record:
- the Lorentz-Lie Noether charge assigns `-2 kappa_X` to the W coefficient;
- the diagonal-family holonomy and delta analysis shows no content-independent profile closes the gap;
- the tau_Omega decomposition in the fit basis is sampled, not proved.

It changes no label.

## Checks performed
- **The three fixes, verified in the insert diff r1 to r2.**
  1. Paragraph 1 now reads "the charge vanishes at the bifurcation surface for a regular connection with vanishing momentum map, and the term is absent". It also gains "(a bookkeeping variable, not a metric)", which was optional in r1 and is acceptable.
  2. Paragraph 2 now reads "(an extension of the cross-term rule beyond the cone, not derived)". The Sigma-singularity remark reads "(read off the delta structure; not separately checked)".
  3. Paragraph 3 now reads "in the basis \((W,R_\Sigma,R,e,X')\) of the fit". It also reads "in that basis; no statement is made about their topological character beyond it". This replaces "not Euler densities" and "Euler density R_Sigma".
- **Nothing else changed.** The git diff of `appH_insert.tex` shows only these substitutions. The setting, formulas, gap expressions, closing scope sentence and status sentence are identical to r1.
- **Block versus file.** `appH_insert.tex` matches the "Insert text (r2)" block in `proposal-r2.md` exactly. I compared them in Python after normalising line endings.
- **Encoding.** The insert has 0 TAB characters, no CR (it is LF only, so the integrator converts to CRLF), and is pure ASCII (3488 bytes). I found no corrupted escapes.
- **Labels.**
  - The insert has 0 `\label`, `\ref{` and `\cite`.
  - It has a single `\paragraph{...}`.
  - "Problem~B stays open and PROGRAMME-CONDITIONAL." appears once, at the end.
  - The insert text does not yet occur in appH.
- **Anchor.** `\section{Problem C: conformal mode and Cassini}` occurs exactly once, at line 275 of `chapters/appH-microscopic-proofs.tex`.
  - It is preceded by a blank line and the end of the 033 paragraph ("These statements are for the Poisson-limit operators…").
  - Inserting the block plus one blank line immediately before that section line is correct.
- **Body versus insert.** The r2 body changes (the "thinner evidence" note and the ranked avenues) are not in the insert. The Chern–Weil conjecture remains body-only.
- **Not independently verified:** the Jacobson–Mohd and Elgood et al. equation numbers. The insert does not cite them.

## Findings
None (0 blocking, 0 major, 0 minor).

## Scope of what is established
What is accepted, as exactly the text of `appH_insert.tex`: one `\paragraph` of three blocks.
- **Established algebra and symbolic results** (re-run in r1):
  - the cross-term rule as the Lorentz-Noether charge for a tied frame (H = J_12);
  - the exact diagonal-family holonomy and Riemann deltas;
  - the pairing table on SD/ASD modes.
- **Conditional:**
  - the gap formulas, which extend the cross-term rule beyond the cone and are flagged as not derived;
  - the statement that no content-independent profile removes the gap, which holds in the diagonal family only (Θ^{12} = r^{-εc_a}, Θ^{34} = r^{-εc_b}), for plane-wave modes with δρ = 0 about a constant SD or ASD Θ̄, in the completed replica, with a totally geodesic Σ and first order in 1−n.
- **Sampled, not proved:** the τ_Ω decomposition at the 17 totally geodesic points, in the basis (W, R_Σ, R, e, X′).
- **Not derived:**
  - which holonomy the matrix state selects;
  - the replica;
  - the sign or value of G_eff;
  - the topological character of the leftover densities.
- Problem B stays OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. There is no label change, and spacetime remains emergent: the connection is explicitly a bookkeeping variable and not a metric.

Open avenues, ranked:
1. Edge or contact terms of the connection sector (Donnelly–Wall type) supplying −2κ_X W. This is the most promising.
2. Non-chiral Θ̄ and δρ ≠ 0 modes.
3. Off-diagonal equivariant Θ with Burgers/vortex-type deltas.
4. A smooth-cone replica in place of the cross-term rule.
5. O(h²) Dong K² terms with contortion.
6. Finite-n/fixed-state versions of the gap.

## Recommended disposition
Integrate as-is, as ordinal 32. Insert `appH_insert.tex` with CRLF endings and one blank line before it, immediately before `\section{Problem C: conformal mode and Cassini}` (line 275, after the 033 block). Replace nothing, and run `build_check.py` afterwards.

## Corrected snippet
None needed.
