VERDICT: ACCEPT | MILESTONE: none | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
The r2 block differs from r1 only by my six substitutions (F5, F2, F4, F6, F3, F1), applied verbatim, and all six findings are closed.

## Source reading
Targeted reads only, not a full scan. I re-used my r1 reading of the affected Appendix H passages (B ledger, 037/038 blocks, D head, torsion-invariant paragraph) and Chapter 10. I did not re-read `proposal-r2.md`, `apply_r2.py` or `compile_check_r2.out.txt`; the accepted text is `appH_insert.tex` itself, which I checked directly.

## Checks performed
- **Diff of r1 vs r2.**
  - Method: word-level diff of `appH_insert_r1.tex` (CR-stripped) against `appH_insert.tex`.
  - Result: exactly six edit clusters, each matching the replacement text I gave in review-r1. Nothing else changed.
  - F5: the setting sentence now defines V_μ = G^{λν}T_{λμν}, equal to ∂_μ lnρ on the Poisson class.
  - F2: "whole" is removed, "with V_μV^μ replaced by its class value |∂lnρ|²" is added, and the parenthetical stating that 2(V_μV^μ − |∂lnρ|²) vanishes on the class but is not invariant is added.
  - F4: the Dressed density opening now states the input, the density κ_Xρ²X[Λe], the pair invariance, Λ as a stationary field, and that the unitary gauge Λ = 𝕀 gives the undressed density with r undetermined.
  - F6: the Hessian is now stated over the twelve real rotation amplitudes.
  - F3: "At the stationary points above, where S = 0 and V_μ = ∂_μ lnρ, …".
  - F1: "smaller by 2κ_X than the value 4 − n_D before the dressing, that is half of it at n_D = 0 and unchanged at n_D = 2".
- **Labels and anchor.**
  - `\label{ass:local-lorentz}` is unique in `chapters/` (`ch10-lorentz-locking.tex:56`).
  - `\label{eq:dressed-omega}` is unique (`ch10-lorentz-locking.tex:133`).
  - The anchor `\section{Problem C: conformal mode and Cassini}` occurs exactly once in `chapters/appH-microscopic-proofs.tex`.
- **Bytes and balance (Python).**
  - 6406 bytes in `appH_insert.tex`.
  - 0 TAB, 0 CR, 0 non-ASCII, and 0 control characters other than LF.
  - Braces balance (net 0) and `\(` / `\)` balance (net 0).
- **Bibliography and wording.**
  - The block has no `\cite`, so there are no new bib entries. The uncommitted `bib/namcg.bib` change is the 038 one (3 entries).
  - No process language.
  - It closes with one scoped status sentence.

## Findings
none.

## Scope of what is established
Unchanged from review-r1.
- **Proved or numerically verified.** The invariant span {𝒯, |∂lnρ|²}; X = 2𝒯 + (3/2)S² + 2V²; the Euclidean Hessian is positive definite; S = 0 and the 1/2 ratio at the plane-wave stationary point; the cone family lies on the stationary set.
- **Conditional (PROGRAMME-CONDITIONAL).** The dressing e → Λe with the density ρ²X[Λe] as an input of Assumption local-lorentz, and tree-level stationarity of Λ. Together they give r = −2, c_W = c_T^ext, and the residue c_A − c_T^ext = 2 (1 on n < 1, 3 on n > 1 with the vector holonomy contact).
- **Not derived.** The matrix origin of Λ or the local rotation symmetry; a contact of modulus 2; the loop-level treatment of Λ; the nonlinear stationary set; the entropy of the rigid compensating rotation.
- **Status.** Problems B, D and A remain OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. No label change.
- **Open avenues** ranked as in review-r1: the covariant bundle connection for the fluctuation operator; a contact or holonomy of modulus 2; the loop-level Λ; the nonlinear stationary set; the fermion X-term; the Lorentzian ghost-sign Goldstones.
- **Breakthrough.** None.

## Recommended disposition
Integrate as-is.

**Accepted text:** the entire contents of `proposals/039-lorentz-locking-noether/appH_insert.tex` (r2, 6406 bytes, LF; convert to CRLF on insertion).

**Insertion point:** immediately before the line `\section{Problem C: conformal mode and Cassini}` in `chapters/appH-microscopic-proofs.tex`. That is after the Order Λ² contacts / Noether-coefficient paragraph from proposal 038, which ends "Problem~B stays open and PROGRAMME-CONDITIONAL.", with one blank line between the two paragraphs.

## Corrected snippet
Not needed.
