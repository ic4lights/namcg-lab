VERDICT: ACCEPT | MILESTONE: M5 | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
All eight r1 findings (F1–F8) are closed, and no new finding arises. I accept the r2 package (ch03 definition, appH paragraph, two bib entries) as a pre-approved, emergence-preserving structural extension with no label change.

## Source reading
Digest + targeted reads. The digest is CURRENT (chapters-hash fc4f4857691baf87, per the orchestrator). My r1 full scan of all 30 chapter files stands. The only change since then is proposal 010 (ch09, appK), which I already checked by diff, and it touches neither ch03 nor appH. I did not re-scan the whole manuscript.

For r2 I re-read:
- the full r2 proposal and review-r1;
- a diff of r2 against r1;
- ch03 lines 143–174, the new anchor region;
- the integrated 008 paragraph in appH (line 1822, with its closing sentence at line 1823 and `\section{Problem G: HBEV}` at 1826).

## Claim under review
Give the ">4 matrix coordinates" setting of 008 a labelled conditional home, `def:matrix-coords-ext`. Record in one appH paragraph the kinematic linear-response ranks, the transverse-scalar content remark, and the literature context.

Target: Problem F (`ass:emergent-op`), with A, D1 and E by dependency.

Appendix H statuses, as quoted verbatim in r1 and unchanged:
- F: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion."
- A: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL."
- D: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: D2 ... supports only a scope-limited Presentation-B model; D remains OPEN ..."
- E: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL."

Chapter 17 `sec:ch17-done` lists A, B, C, D1, E, F, G-derived and N, so there is no discrepancy. The original target is not met, and the package does not claim it is.

## Checks performed
**Diff r2 against r1.** The changes match the changelog, and I found no unlisted change to the proposed text.

**Re-verification of the earlier findings.**
- **F1 closed.** The duplicate proof paragraph is replaced by one cross-reference sentence. That sentence matches the 008 argument:
  - It states the same hypotheses: a real four-dimensional leaf and a real Lorentzian g.
  - My r1 re-derivation of the determinant argument covers it: G = −gM², det M = Pf(ω)²/det g < 0, whereas G = cg would force det M = c² > 0.
  - The merged 008 text reaches the same conclusion through the characteristic polynomial of N = θg.
  - "The preceding paragraph" is the 008 "Metric seen by the operators" paragraph, which sits at line 1822 directly before the insertion point. The new paragraph goes after the 008 closing sentence and before `\section{Problem G: HBEV}`.
  - The r1 Euclidean-contrast statement (G ∝ g possible, but G Euclidean) is retained correctly.
- **F2 closed.** The N_tot sentence is gone. Only "not covered by `ass:locked-block`; additional infrared fields unless gapped" remains, and that is supported.
- **F3 closed.**
  - The extra-dimension and Newton-constant statements are attributed to `Steinacker2023` only.
  - The extra tensors are attributed to `KumarSteinacker2023` and `Steinacker2026` only.
  - The leaf-dimension relaxation is framed as a route in this package's class, not as a property of those papers.
  - The sentence ends with "not checked against the present operators".
  - The abstracts were fetched in r1: only 2303.08012 mentions fuzzy extra dimensions.
- **F4 closed.**
  - ρ = 1/|Pf θ| is defined.
  - The definition now states the hypothesis class and cites `app:status`, no longer `rem:ch3-moyal-check`.
  - The "read with I,J" clause is restricted to the quartic and matter terms, and the cubic term is excluded.
  - The wording is "reduces, for D = 4, to".
- **F5 closed.** I re-ran `verify_anchors_labels.py`. The ch03 anchor count is 1 and `eq:Smatrix` precedes it. The anchor is the paragraph ending "The existence of such a map is enough for now." (line 170), followed by a blank line and `\section{Presentation B: the covariant condensate action}`, and that section title occurs once. The appH anchor count is 1. Every cited label counts 1: `def:matrix-coords`, `eq:Smatrix`, `ass:lorentzian`, `ass:locked-block`, `eq:g-from-e`, `ass:emergent-op`, `eq:Geff-structure`. `def:matrix-coords-ext` counts 0, so it is new. A grep confirms `app:status` (appH line 2) and `ch:vierbein-emergence` (ch04 line 2) each occur once. `Steinacker2023` exists in `bib/namcg.bib` (line 121). `KumarSteinacker2023` and `Steinacker2026` are absent, so they are new. The working tree is clean.
- **F6 closed.** The (2,2) contrast is dropped, and the hypotheses are stated.
- **F7 closed.** The text now has all of:
  - the factor i absorbed in ξ;
  - ξ ∝ θᵀp;
  - "exactly three for every D" for the flat brane;
  - the generic-rank logic: the upper bound min(6, D−1) is exact, and the lower bound comes from one exact-rational draw for each 4 ≤ D ≤ 11, generic by lower semicontinuity.
- **F8 closed.** The closing sentence is "This changes no ledger label; Problem~F remains open." It lists no fixed problem set and does not repeat the 008 closing line.

**Scripts.** `check_conformal_nogo.py` and `check_brane_rank.py` and their outputs are unchanged since r1. I reproduced them and wrote independent numpy checks in r1. Only the anchors script changed, and I re-ran it (results above). These are checks, not proofs. The exact algebra is supported by my hand re-derivation, and the rank upper bounds are exact by the counting argument.

**BibTeX record: VERIFIED.** The entries for `KumarSteinacker2023` (arXiv:2312.01317) and `Steinacker2026` (arXiv:2601.08031) are text-identical to those I verified in r1 against the arXiv abstract pages. They are @misc entries with authors, title, year and eprint, and they claim no journal data. The existing `Steinacker2023` entry was matched to Crossref in r1. This verification covers abstract level only. The content of the three papers is not independently verified, and the leaf dimension of 2312.01317 and 2601.08031 is not verified. The new text does not claim either.

## Findings
None.

Two optional style notes, neither required:
- "the hypothesis of the first statement above" refers to the "Operator metric versus induced metric" sentence. This is acceptable as it stands.
- Optionally add `primaryClass` to the bib entries.

## Scope of what is established
- **Established, and already merged via 008.** G ≠ c·g pointwise for every D ≥ 4. The hypothesis class is: real four-dimensional symplectic leaf, Poisson limit, real Lorentzian g. This result is now only cross-referenced, not re-proved. The within-core route to relax it is the leaf dimension, which is the hypothesis that carries the obstruction.
- **Established (kinematic).**
  - The linearised Einstein rank about a flat brane is exactly 3 for every D.
  - The rank is min(6, D−1) for generic frozen II, for 4 ≤ D ≤ 11. The lower bound is a sample result plus semicontinuity, and the upper bound is exact.
  - The class is: Poisson limit, frozen coefficients at a point (WKB), Gauss–Codazzi not imposed, generic p.
  - D ≥ 8 including the density scalar is a necessary count only.
- **Conditional.** The semiclassical reading in `def:matrix-coords-ext`; the transverse-scalar content statement.
- **Not established.** Any Einstein-type field equation for G; a gap for the transverse scalars; the identification of Φ with a tangent-plane frame; local Lorentz symmetry; a signature; any extra conserved stress; any G_eff.
- **Completion and labels.** The package is PROGRAMME-CONDITIONAL. F, A, D1 and E remain OPEN with their labels unchanged. No label change is proposed. I checked the proposal text, the appH closing sentence and the definition, and none changes a label.
- **Emergence.** Spacetime stays emergent. η_IJ contracts matrix indices only, as in `eq:Smatrix`. The definition adds no fundamental metric. The Lorentzian signature stays an assumption, `ass:lorentzian`. Neither g nor G is asserted to be the emergent metric.
- **Milestone.** M5 only, a pre-approved structural extension. No M1–M4 and no BREAKTHROUGH.

## Recommended disposition
Integrate as-is at ordinal 9. The accepted items are exactly the following, with no other change:
1. **ch03 definition.** The `definition` environment `def:matrix-coords-ext` as given in File 1 of proposal-r2.md. It goes at the end of the paragraph ending "The existence of such a map is enough for now." and before `\section{Presentation B: the covariant condensate action}`.
2. **appH paragraph.** The paragraph headed "More than four matrix coordinates in the Poisson limit: linear response (conditional; not closure)", as given in File 2. It goes after the 008 paragraph's closing sentence and its blank line, and before `\section{Problem G: HBEV}`. The 008 paragraph is left untouched.
3. **Bib entries.** `KumarSteinacker2023` and `Steinacker2026` appended to `bib/namcg.bib`, as in File 3.

Preserve CRLF line endings. After the integration, run `python scripts/build_check.py` and check for undefined citations (`KumarSteinacker2023`, `Steinacker2026`) and for the new label.

Relevant files:
- C:\Users\redgi\Projects\namcg-lab\proposals\009-matrix-coords-N8\proposal-r2.md
- C:\Users\redgi\Projects\namcg-lab\proposals\009-matrix-coords-N8\review-r1.md
- C:\Users\redgi\Projects\namcg-lab\proposals\009-matrix-coords-N8\verify_anchors_labels.py
