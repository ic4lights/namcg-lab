VERDICT: ACCEPT | MILESTONE: M2 | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
Both r2 required fixes were applied verbatim. Nothing else in the LaTeX changed, the anchor and labels check out, and there is no label change.

## Source reading
Digest and targeted reads. The digest is CURRENT and the chapters are unchanged since my r1 full scan, which was done at ordinal 10 (all 30 chapter files, with appH in full) and covers this integration.
I read proposal-r3 and review-r2 in full and ran `diff proposal-r2.md proposal-r3.md`.
I did not re-derive the central equations this round. The r2 derivation and checks stand, because the displayed identity and all mathematical content are untouched.

## Claim under review
- **Claim:** the same package as r2. It is a bounded leaf-dimension no-go (M2), the CP^{1,2} class, a conditional heat-kernel factorisation, and the torsion identity for X.
- **Original target:** Problem F (`ass:emergent-op`). Appendix H, verbatim: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion."
- **A and E, verbatim:** "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL."
- **Chapter 17:** the criterion lists A, B, C, D1, E, F, G-derived and N.
- **Original F target:** not met.

## Checks performed
**Diff r2 to r3, LaTeX block.** There are exactly two changes, in the torsion paragraph:
- "linearly dependent" became "linearly dependent modulo total derivatives". This is verbatim from my snippet.
- "With the classical teleparallel identity" became "With the identity for the Weitzenb\"ock connection of the coframe \(e\) (in the present index convention, checked by direct computation)". This is verbatim, and the displayed formula is unchanged.
- The other diff hunks are the proposal's changelog and prose: "proved" to "derived", classification wording, and a decisions note. None of them is manuscript text.

**Search for "proved".** The LaTeX block (lines 79–99 of proposal-r3) contains no "proved" or "prove". The only hits in r3 are changelog lines 10 and 21, which are not manuscript text.

**Anchor.** "This changes no ledger label; Problem~F remains open." occurs exactly once, at `chapters/appH-microscopic-proofs.tex` line 1835. `git status` is clean.

**Labels.** `def:matrix-coords-ext` is at ch03 line 173, `thm:Geff` at ch08 line 187, and `ch:vierbein-emergence` at ch04 line 2. Each is defined once in .tex (the other hit for each is its .aux entry). The only citation key used is Steinacker2023, which was verified in r1. No new labels, citations or bib entries.

**Status and emergence.** No label, status, priority or classification is touched. Spacetime stays emergent: the text explicitly declines to identify G or η with the emergent metric.

## Findings
None. Earlier findings F1–F7 and the two r2 minor findings are closed.

## Scope of what is established
- **Exact (within stated hypotheses):**
  - Theorem 1: real Θ, y^μ equal to four of the matrix coordinates, positive fibre average, c≠0, K=0 excluded.
  - The leaf-level no-go for 2m≥4, and the 2m=2 counterexample.
  - X=I_A and V=d ln ρ.
  - The torsion identity for X (four matrix coordinates, real nondegenerate Θ with Jacobi). It is derived given the Weitzenböck identity, which is stated explicitly, uncited, and verified by direct exact computation; it is also checked on 12 finite-amplitude cases.
  - The CP^{1,2} Lie–Poisson algebra and K=(M^{45}/R²)²η^{-1}.
- **Conditional:** the heat-kernel factorisation and thresholds.
- **Open:**
  - the Einstein rank in the conjugate-coordinate class;
  - why y^μ=M^{μ5} are the base functions;
  - the Φ-to-coframe dictionary;
  - the transverse-scalar gap;
  - any G_eff value or sign.
- **Hypotheses a within-core route could relax:** y^μ not matrices (the CP^{1,2} class), non-positive or complex Θ, and dynamical fibre geometry.
- **Critical path:** A, B, C, D1, E, F, G-derived and N all remain OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL.
- This is not a BREAKTHROUGH and no label change is proposed.

## Recommended disposition
Integrate as-is. Accepted text is exactly the two appH paragraphs in the proposal's single ```latex block, inserted before the `\section{Problem G: HBEV}` line, immediately after line 1835 of `chapters/appH-microscopic-proofs.tex`:
1. `\paragraph{Leaf dimension above four: fibre averages, a product factor and a conjugate-coordinate class (conditional; not closure).}` with its sub-blocks (Matrices as base coordinates; Conjugate coordinates; Heat kernel over a fuzzy factor) and its closing scope paragraph.
2. `\paragraph{Connection-sector term \(X\) as a torsion invariant (conditional; not closure).}` with its derivation paragraph, displayed identity, check paragraph, and closing scope paragraph.

The first paragraph carries the same text as r2 and r1-reviewed content. The proposal's own prose, changelog and verification-script sections are not manuscript text.

## Corrected snippet
None needed.
