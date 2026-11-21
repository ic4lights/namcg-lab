# Local re-review r1 (remote/claude, 2026-11-18): 058-a-map-dictionary-derivation

VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/1

Source reading: digest + targeted reads + pattern scans of all 30 chapter files. This is not a literal full scan.
The text in the tree (appH L90-136) is byte-identical to proposal-r2.md L152-198. All four scripts re-run with matching output.

Verified:
- Moyal bracket: only odd powers of Theta occur, with coefficient -i/24 at order Theta^3.
- 't Hooft-pair commutator law, and the uniform-in-N remainder bound via |2 sin(x/2) - x| <= x^3/24.
- Plane pairing.
- Order-Theta symbol of the fluctuating coordinates.
- The associator, as a signed sum over the six orderings, equals [Theta,Theta] with factor 1.
- The 2D Schouten-closed counterexample.

Findings:
- MAJOR (L128-130). The text calls "explicit order-Theta^2 correction bidifferential operators" an alternative to Schouten closure; it is not.
  - The signed sum of delta B_2 vanishes for a generic bidifferential B_2 (checked in scratch/gk-grpA/alt_coboundary*.py), so no order-Theta^2 correction can cancel [Theta,Theta] != 0. Schouten closure is therefore necessary.
  - Avenue 1 of the package ("without Schouten-closure") is false.
- MINOR, required (L123). The normalisation of "antisymmetrized" is unstated: factor 1 for the plain signed sum, factor 6 off for the 1/6-averaged Alt.
- MINOR, required (L106-107). The torus pairing is stated as exact with no mode limit, and M is undefined. Without a mode limit, aliasing terms appear.
- MINOR, optional. theta carries three meanings in one paragraph. A single 't Hooft pair is the finite-N analogue of one symplectic plane only.

Required replacements (chapters/appH-microscopic-proofs.tex, CRLF):

R1 (L122-123) replace
    at order \(\Theta^2\); the antisymmetrized order-\(\Theta^2\) associator equals
with
    at order \(\Theta^2\); the order-\(\Theta^2\) part of \((f\star g)\star h-f\star(g\star h)\),
    summed with signs over the six orderings of \((f,g,h)\), equals

R2 (L128-130) replace
    naive truncation; hence a Moyal-type continuum description at a variable
    expectation-value \(\Theta\) requires a Schouten-closed leading bivector or explicit
    order-\(\Theta^2\) correction bidifferential operators. These statements are for the
with
    naive truncation. No order-\(\Theta^2\) bidifferential correction of the product changes
    the first-derivative part of this signed sum, so an associative Moyal-type continuum
    description at a variable expectation-value \(\Theta\) requires a Schouten-closed leading
    bivector and, in general, explicit order-\(\Theta^2\) correction bidifferential operators.
    These statements are for the

R3 (L106-107) replace
    and \(\operatorname{Tr}\widehat W(f)\widehat W(g)=N\sum_v\hat f_v\hat g_{-v}\) hold
    exactly, and for mode-limited symbols with \(2M<N\) the operator-norm remainder of
with
    holds exactly; for mode-limited symbols (\(\hat f_v=\hat g_v=0\) unless
    \(|m|,|n|\le M\)) with \(2M<N\),
    \(\operatorname{Tr}\widehat W(f)\widehat W(g)=N\sum_v\hat f_v\hat g_{-v}\) holds exactly,
    and the operator-norm remainder of

Disposition: researcher r3 with R1-R3, then re-review (integrate only on plain ACCEPT). The imported text remains in the tree as is.
Status: Problem A OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL; no label change.
