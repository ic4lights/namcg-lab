VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/2

## Verdict
The package's mathematics is largely correct and reproducible, and the proposed appH insertion is honest about scope, but two major scoping/definition defects must be fixed before integration: (1) the proposal's claim classification asserts Θ²-associator vanishing "for constant/Poisson bivectors," which is false for generic Poisson bivectors (I have an explicit counterexample); (2) the inserted sentence uses the undefined symbol [Θ,Θ] whose verified "factor one" holds only in an explicit cyclic-sum convention.

## Source reading
Digest + targeted full reads + exhaustive concept greps across the manifest. **A literal full scan of all 30 chapters files was NOT performed and is not claimed.** Constraint: `chapters/appH-microscopic-proofs.tex` alone is 542,851 B (~3,212 CRLF-terminated lines); a 900-line read exceeded the 25,000-token tool limit, so a single-context full scan of all 30 files was not feasible. Coverage actually obtained:
- `scratch/digest.md`: read in full (COMPACT mode, DIGEST CURRENT at head a33e52c, dirty-chapters: no, 30 files, "Duplicate labels: none", label index empty). TOC + status-line extracts obtained for all 30 files.
- `chapters/appH-microscopic-proofs.tex`: L1–120 read in full (Problem A section L12–71 in full, including Ledger label, free/Poisson lemma, "General sector" paragraph, anchor, "Missing step."); full section structure map (all `\section`/`\paragraph{Ledger label.}` lines); targeted reads at L2080–2090; exhaustive concept greps (Moyal, odd powers, Weyl, associator, Schouten, torus, 't Hooft, trace density, status lines) over the whole file.
- `chapters/ch03-matrix-action.tex`: L55–215 and L340–520 read in full (eq:NC, def:matrix-coords-ext, ass:dictionary/eq:dictionary, rem:ch3-moyal-check with the −i/24 display, rem:ch3-trace-quadratic).
- `chapters/ch17-agenda.tex`: L355–430 and L690–730 read in full (Problem A entry, completion criterion).
- `chapters/ch02-preliminaries.tex` and the remaining 26 files: digest TOC + targeted concept greps only (star/Moyal/Weyl/Poisson/associator/'t Hooft/torus/density terms); no convention conflicts found by grep.
- `proposals/058-a-map-dictionary-derivation/proposal-r1.md`: read in full (r1; no prior review-r*.md exists).
- `reports/sme-scout-20261107-1758.md`: read in full. `reports/ledger.md`: tail read (54 integrations; appH sha 185bdcee… matches digest; "FULL SCAN DUE AT 55").
- No unreadable files. Note for the orchestrator: this proposal edits a status-passage region (sec:status-A), which the protocol flags for full scan; the coverage above is the maximum the read tooling permits for a 543 KB single file. The greps used are exhaustive over file *content*, so no passage matching the insertion's concepts can have been missed, but I will not certify per-file full reads.

## Claim under review
Problem A / A.map, `sec:status-A`. Appendix H verbatim: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL." Chapter 17 criterion verbatim: "Problem~A: Assumption~\ref{ass:dictionary} is derived, or the chains of the other items are re-derived without invoking it. Renaming the same map does not meet this item." The package claims: (i) pinned Hilbert space/Weyl map/trace pairing for the constant-Θ Abelian Moyal class on R⁴; (ii) exact finite-N 't Hooft torus Weyl data with an exact operator-norm per-order remainder bound uniform in N; (iii) odd-powers-only Moyal bracket with coefficients i and −i/24, degree-≤2 exactness, order-Θ fluctuating-coordinate symbol and Θ³ first correction; (iv) Θ² associativity obstruction for naive variable-Θ star truncation, antisymmetrized part equal to the Schouten contraction with factor one, plus a derived consistency condition. Original target (ass:dictionary derived in the matrix-derived chain) is **not** claimed closed, and the insertion says so explicitly. Status: OPEN. Priority: CRITICAL PATH.

## Checks performed
Direct verification:
1. All three researcher scripts re-run with `python -I` in the proposal folder; stdout byte-compared to saved `moyal_out.txt`, `torus_out.txt`, `assoc_out.txt` — all match (MOYAL_MATCH / TORUS_MATCH / ASSOC_MATCH).
2. Independent re-derivations (scratch, outside the repo in `/tmp/gk058/`, run with `-I`):
   - Weyl product law on the torus re-derived by hand (VⁿU^{m'} = e^{−iθnm'}U^{m'}Vⁿ): with Weyl ordering β = −θ/2, [Ŵ_v,Ŵ_w] = 2i sin((θ/2)σ(v,w))Ŵ_{v+w} exactly; confirmed numerically for (N,p) = (37,3), (80,7), (50,1) (errors ~1e−12). β = +θ/2 fails for either sign of the right-hand side (err ≈ 4.0) — an extra phase e^{−iθ(mn'+m'n)} survives; the proposal's β choice is essential, not conventional.
   - Remainder bound: |2 sin x − 2x| ≤ |x|³/3 at x = θσ/2 plus unitarity of Ŵ_v gives ‖R‖ ≤ Σ|f̂_v||ĝ_w|(θ|σ|)³/24. Verified numerically to hold; "uniform in N" is **substantive, not vacuous**, within the stated class: for fixed mode sets (2M<N) and N-independent symbols the constant is N-free and the remainder is O(θ³) = O(N⁻³) at θ = 2πp/N.
   - Moyal bracket: only odd powers; order-Θ = i{·,·}_Θ; order-Θ³ coefficient −i/24 = 2(i/2)³/3! — matches ch03 L386–390 display; exactness for symbols of degree ≤2 confirmed, consistent with the appH free/Poisson lemma "exact at constant Θ".
   - Pairing: hand re-derivation of Tr W_Θ(f)W_Θ(g) = (2π)⁻²|PfΘ|⁻¹∫fg from the ch03 Fourier convention; factor is byte-identical to rem:ch3-trace-quadratic (ch03 L466–474) and to the inserted display.
   - Variable-Θ associator, my own script `assoc_generic.py`: for a fully generic 3D variable bivector (48 terms, first derivatives only) the antisymmetrized Θ² associator minus (cyclic Schouten)·det(df,dg,dh) is exactly zero — factor one **in the cyclic-sum convention**.
   - **Counterexample `assoc_2d.py`**: for a generic variable 2D bivector π^{12}(x¹,x²) — automatically Schouten-closed (dimension) — the naive-truncation Θ² associator coefficient is **not** identically zero (`c2 == 0 ... False`). Schouten-closure alone does not kill the Θ² associator of the naive truncation; vanishing holds for constant Θ and special Casimir-transverse families (script control Θ^{12}=εa(x³)), not for Poisson bivectors in general.
   - Hermiticity of Ŵ for real symbols, exact torus pairing NΣf̂_v ĝ_{−v}: confirmed (~1e−12).
3. Anchor byte-verified in working-tree bytes: "The error bound therefore controls the difference from an unproven candidate, not from the diamond modular Hamiltonian." occurs exactly **once** (byte offset 3007). Insertion point (before `\paragraph{Missing step.}`) exists. Post-apply appH expected ≈ 546,1xx B (block is 3,223 B LF → +2 CRLF terminators).
4. Labels: `def:matrix-coords-ext` (ch03:173), `ass:dictionary` (ch03:346), `eq:dictionary` (ch03:352), `rem:ch3-moyal-check` (ch03:372), `rem:ch3-trace-quadratic` (ch03:450) — each unique. No new labels. No status/priority/completion text altered; the paragraph ends "so they do not derive Assumption~\ref{ass:dictionary}" — no closure language. No chat/process language. Emergence guard present ("Θ remains the expectation … not input geometry") — consistent with the emergence requirement.
5. Hygiene: appH 3212 CRLF, 0 bare LF; insertion must be written CRLF, UTF-8 no BOM. Manuscript-wide greps found no other 't Hooft/torus/associator/Schouten usage, so the insertion creates no stale statements; other "Moyal terms dropped" passages (e.g., appH L2084) say corrections at cutoff are not handled — the insertion does not contradict them.
6. Numbers: θ=2πp/N, σ, 24, −i/24, (2π)⁻², |PfΘ|⁻¹ all either derived in the proposal/scripts or present in ch03/appH — no unsourced numbers.
Not independently verified: Lechner–Scotford (scout arXiv 2111.03172) and the Latremoliere/Lechner-Scotford book leads — proposal body only; **no citations are imported into the manuscript text**, so the verdict does not depend on them. No SME-CONSULT needed.

## Findings
- **F1, major — Location: proposal-r1.md L154–155 and insertion L207–209.** The classification "Θ² associator … vanishing for constant/Poisson bivectors: **established identity**" is an overgeneralization. My `assoc_2d.py` shows a variable 2D bivector is automatically Schouten-closed yet the naive truncation retains a nonzero Θ² associator; script 3 only tests constant Θ and the Casimir-transverse control. The inserted sentence's *necessity* clause ("requires a Schouten-closed leading bivector or explicit order-Θ² correction bidifferential operators") is valid — if the full associator vanishes its antisymmetric part does, so [Θ,Θ]≠0 forces corrections — but the first clause "the naive insertion … fails associativity at order Θ²" is generically (not universally) true, and "requires X or Y" must not be read as sufficiency. Required action: scope the proposal classification to "constant bivector and Casimir-transverse Poisson controls; generic Poisson bivectors not guaranteed"; in the insertion add "generically" to the failure clause and state that Schouten-closure alone does not remove the full Θ² associator.
- **F2, major — Location: insertion L209–210.** `\([\Theta,\Theta]^{abc}\partial_af\partial_bg\partial_ch\)` — [Θ,Θ] is undefined anywhere in the manuscript. My generic check confirms factor one only for the explicit cyclic-sum definition; common weighted-Nijenhuis-Rijmenbach normalizations shift the factor (e.g., Σ_cyc = (3/2)[π,π]^{123} for some conventions). As written the "factor one" content is convention-ambiguous. Required action: pin the definition inline (see Corrected snippet).
- **F3, minor — insertion L187–188.** "matching the density of Definition~\ref{def:matrix-coords-ext}": the def's density is ρ = 1/|Pf θ| without the (2π)⁻²; the exact displayed factor (2π)⁻²|PfΘ|⁻¹ is in rem:ch3-trace-quadratic. Cite it (or write "the |Pf θ|^{-1} density of Definition … together with the Fourier factor of Remark …"). Not a mathematical error: the (2π)⁻² is the Fourier-convention factor, and the two ch03 conventions coexisting without comment is pre-existing, not created here.
- **F4, minor — insertion L189.** "At finite N the same data are the 't Hooft pair": the torus algebra (UV = e^{iθ}VU) is the finite-N analogue of, not identical to, the R⁴ Heisenberg data. Prefer "the finite-N analogue is".
- **F5, minor — insertion L195.** `\(\{f,g\}_\Theta\)` on the torus is undefined at that point; add "the symbol-level Poisson bracket" once.
- **F6, minor — typography/proposal-internal.** "'t Hooft" with a straight apostrophe renders as a closing quote in LaTeX; use ``t Hooft. The proposal labels Lechner–Scotford "Scout Route 3"; the scout report lists it as Route 6 (process-internal only; no manuscript consequence).

## Scope of what is established
- **Proved (established identities within stated hypotheses):** exact torus Weyl-ordered product law and pairing; the operator-norm bound ‖R‖ ≤ Σ|f̂||ĝ|(θ|σ|)³/24 for 2M<N (substantive, N-uniform in that class, O(θ³) decay); odd-powers-only Moyal bracket with i and −i/24 and degree-≤2 exactness; exact (2π)⁻²|PfΘ|⁻¹ pairing; antisymmetrized Θ² associator = Schouten contraction × det with factor one in the cyclic convention (generic 3D bivector, exact symbolic identity).
- **Conditional (holding only under stated hypotheses):** order-Θ fluctuating-coordinate symbol and connection-inducing term; Θ³-first-correction statement; the consistency condition binds only if the continuum description is Moyal-type.
- **Bounded obstruction, correctly within its hypotheses:** naive constant-form Θ² truncation generically non-associative at variable Θ; not associative at Θ² even for generic Poisson bivectors (F1's sharper fact).
- **Still OPEN:** everything A requires for matrix-derived completion — selection of this data class from the matrix condensate, identification of the induced connection with the ch03 kinetic connection and resolution of the constant-Θ kinetic obstruction, non-Abelian sector, unbounded boost/diamond symbol and sharp cutoff, extension of bounded-symbol results to the diamond modular Hamiltonian. ass:dictionary NOT derived; no ledger label change is warranted or proposed.
- **Open avenues ranked (relaxations that could still favour A):** (1) relaxing the *naive-truncation* hypothesis — Kontsevich-formal / corrected star products can restore associativity at variable Θ without Schouten-closure, so the Θ² obstruction constrains but does not forbid a variable-Θ dictionary; (2) relaxing *Abelian/constant-Θ* toward the condensate's own fluctuating statistics; (3) relaxing *mode-limited symbols* toward symbols growing with N (where the torus bound must be re-proved); (4) relaxing the star-product ansatz entirely (dictionary map not a star product — the proposal itself notes the condition then need not bind, but the map must still be constructed).

## Recommended disposition
Revise, then integrate as a single insertion. Apply rule: in `chapters/appH-microscopic-proofs.tex`, after the sentence ending at byte offset 3007 ("…not from the diamond modular Hamiltonian.") and before `\paragraph{Missing step.}`, insert the corrected block (below) as one `\paragraph{}` separated by blank CRLF lines; CRLF endings, UTF-8 no BOM; expected final size ≈ 546,1xx B. No other file changes; no bib changes. After apply: `python scripts/build_check.py` must be clean (new refs to existing labels only; watch for "undefined references" — none expected since all four labels plus rem:ch3-trace-quadratic exist uniquely). Researcher must also correct the proposal's internal claim classification per F1.

## Corrected snippet
Minimal-diff replacement of the affected passages (no new physics; added/changed text marked; rest of block unchanged):

```latex
is exact, with the \((2\pi)^{-2}|\operatorname{Pf}\Theta|^{-1}\) trace density of
Remark~\ref{rem:ch3-trace-quadratic} and the \(|\operatorname{Pf}\theta|^{-1}\) density
of Definition~\ref{def:matrix-coords-ext}. % F3
At finite \(N\) the finite-\(N\) analogue of these data is the 't Hooft pair % F4
...
the operator-norm remainder of
\(\tfrac1{\mathrm i}[\widehat W(f),\widehat W(g)]-\widehat W(\{f,g\}_\Theta)\), where
\(\{\cdot,\cdot\}_\Theta\) is the symbol-level Poisson bracket, obeys % F5
...
For nonconstant \(\Theta\) the naive insertion of \(\Theta(x)\) into the
constant-coefficient Moyal formula generically fails associativity at order
\(\Theta^2\); the antisymmetrized order-\(\Theta^2\) associator equals
\([\Theta,\Theta]^{abc}\partial_af\,\partial_bg\,\partial_ch\) with
\([\Theta,\Theta]^{abc}:=\Theta^{ad}\partial_d\Theta^{bc}
+\Theta^{bd}\partial_d\Theta^{ca}+\Theta^{cd}\partial_d\Theta^{ab}\), and
Schouten-closure alone does not remove the full order-\(\Theta^2\) associator of the
naive truncation; hence a Moyal-type continuum description at a variable
expectation-value \(\Theta\) requires a Schouten-closed leading bivector or explicit
order-\(\Theta^2\) correction bidifferential operators. % F1, F2
```

(The "requires … or …" clause is kept as a necessity statement only; the added clause blocks the sufficiency misreading. All three scripts reproduce exactly as submitted; no changes to the scripts are required.)
