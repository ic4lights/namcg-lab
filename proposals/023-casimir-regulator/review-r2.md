VERDICT: ACCEPT | MILESTONE: none | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
All three r1 findings are fixed. The sign is consistent, the (5,1) claim is restricted to sampled λ, and the A=48 fraction is marked numerical. I found no other changes, the anchor is unique, and no labels change.

## Source reading
Digest + targeted reads. I read proposal-r2.md, block-r2.tex, review-r1.md, the two modified scripts, the committed diff between db56cd7 (r1) and 18e9d73 (r2), and the Appendix H anchor region. This is not a full scan. The block is a conditional paragraph in Appendix H and changes no definition, status or scope line, so 3(c) does not apply. I did not run `make_digest.py --check`, so the digest status is unverified; I read the affected passages directly, as CLAUDE.md 3(d) requires for a dirty tree.

## Claim under review
Bounded no-go plus conditional route in the Poisson, one-loop, leading-symbol, four-matrix class, for Problem F (Casimir regulator). Problem F's status and priority in Appendix H are unchanged by this block, so I quote nothing new. The block states "This changes no ledger label; Problem~F remains open."

## Checks performed
- **Finding 1 (sign).**
  - **Block text.** The r2 block now carries the single convention statement: "the principal symbol is its negative, so that the principal symbol of H_V is σ(Box) and that of Δ_κ below is −σ(Δ_κ)". The displayed formula is −σ(Δ_κ)=α(κ−½)q_b+β(1−κ)q_f, which is the correct linear combination (σ(C_42)=−αq_b+βq_f, σ(C_41)=−½αq_b+βq_f). Positivity is stated via −σ(Δ_κ) for ½<κ<1, and at κ=¾ the block gives −σ(Δ_{3/4})=¼(αq_b+βq_f). Consequences (ii), (iii) and (iv) use χ(−σ(Δ_κ)/Λ²), {−σ(Δ_κ)≤Λ²} and the pair (σ(Box), −σ(Δ_{3/4})). Item (iv) now says "principal symbol σ(Box) of H_V". Result item 4 in proposal-r2.md is also fixed (line 9).
  - **Scripts.** The git diff between r1 and r2 shows one docstring line changed in each of `window_local.py` and `sym_pencil.py`, and no `*.out.txt` file changed. I re-ran `window_local.py`: its output is identical to the committed `window_local.out.txt` (diff reports SAME). That output includes d_* from 1.72 to 5.55 and the det^(-1/2) values. In the script, K_H=σ(Box) is paired with A_κ=K41−κK42=−σ(Δ_κ), which matches the new (σ(Box), −σ(Δ)) statement. I did not re-run `sym_pencil.py`.
- **Finding 2.** The block now reads "A (5,1) induced form with no centre variable thus occurs at the sampled values λ=0.01, 0.1, 10, and requires two independent bilinear coefficients; the Hessian of that set is not examined." The word "Lorentzian" and the claim "for λ>0, λ≠1" are gone.
- **Finding 3.** The block now says the fraction "falls numerically to 2.5·10⁻³ at A=48 (… not proved)".
- **No other changes.** The earlier whole-file diff of block-r1 against block-r2 flagged every line as different, because the line-ending state of the two files differs. Comparing the text, apart from the edits above the block is the r1 block, and r2 only added those edits. The text of the block matches the proposal text (it appears verbatim in proposal-r2.md). The block has LF endings only (26 LF, 0 CRLF), while CLAUDE.md says `.tex` files use CRLF. The integrator must convert it to the target file's line endings and must not paste the LF text over a CRLF file.
- **Anchor.** `\section{Problem G: HBEV}` occurs exactly once, at line 2019 of `chapters/appH-microscopic-proofs.tex`. The preceding paragraph is the 022 block ("This is a statement for the Poisson limit, the leading symbol, equiregular points, …"). The paragraph title "Conjugate-coordinate class: the Casimir of \(\mathfrak{so}(4,2)\)…" does not yet exist in `chapters/`.
- **Labels.** The block has no `\label` and uses only `ch:vierbein-emergence`, `ass:lorentzian` and `\LUV` (the `\LUV` macro I did not look up). I did not check these labels against the chapters myself. I rely on the proposal's `compile_check_r2.out.txt`, which reports pdflatex, bibtex and pdflatex runs with rc 0 and 0 errors, undefined references, multiply-defined references and double subscripts. I did not rebuild.
- **Not re-verified.** I did not re-run `compact_scaling.py`, `eight_stationarity.py` or `sym_eight*.py`. r1 accepted those results, and the changed sentences are only hedges.

## Findings
None. Nothing remains open, and no minor item is left.

## Scope of what is established
**Proved or exact.**
- The algebraic relations in the "Exact relations" paragraph: H_V=C_G−C_41−C_Σ+μ², Box=C_41−C_31, and the commutation properties.

**Numerical, at sampled points.**
- The (2,4) signature of the symbols and the pencil eigenvalues ½ and 1.
- The positive-definite window for ½<κ<1.
- The window-volume scaling.
- The (iv) generalised eigenvalues.
- The Zeeman bound d_*.
- The compact-check spectrum, with its pattern verified for N≤3 and the A=48 fraction numerical.
- The eight-matrix signatures at the sampled λ.

**Conditional or not derived.**
- Δ_κ is an additional regulator, built from the J^{A5} generators outside U(so(4,1)'), and is not derived from the action.
- Neither κ nor the cutoff function χ is fixed by the algebra.

**No-go class (exact hypotheses).**
- Poisson limit, one loop, leading symbol, four-matrix class with the bilinear term μ²=−3, background gauge, and regulators that are functions of C_42 and C_41.
- Within that class, a function of C_42 alone is not elliptic.
- Within that class, the Casimir window bounds the negative direction by a quantity linear in Λ and does not remove it.

**Status.**
- Problem F stays OPEN. Under CLAUDE.md rule 3, a scope-limited outcome leaves F OPEN and PROGRAMME-CONDITIONAL. E also stays open, since a Euclidean coefficient is not a Lorentzian one and Assumption~\ref{ass:lorentzian} stays in place.
- No label change is proposed.

**Open avenues (relaxations that could still favour the derivation), most promising first.**
1. Fix κ and χ by a matrix-intrinsic fibre-admissibility condition. The proposal's fork list calls this SME R-F2.
2. Use a Lorentzian iε Schwinger integral in the window, which removes the Euclidean-contraction obstruction (iv).
3. Examine the Hessian of the eight-matrix set with two independent bilinear coefficients. This is the (5,1), no-centre-variable case, and the block says it has not been examined.
4. Go beyond the leading symbol and the Poisson limit: Moyal terms and fermions.
5. Use regulators outside the class of functions of C_42 and C_41 only (for example, from the exact matrix action).

## Recommended disposition
Integrate as-is (ordinal 21). Insert exactly the text of block-r2.tex (the one paragraph titled "Conjugate-coordinate class: the Casimir of \(\mathfrak{so}(4,2)\) and its combinations as proper-time regulators in the four-matrix class (conditional; bounded no-go and conditional route).") immediately before `\section{Problem G: HBEV}` and after the 022 paragraph. The integrator must give it CRLF line endings and rebuild with `scripts/build_check.py`.

Accepted, exactly:
- The block-r2.tex paragraph with the corrected sign convention.
- The restricted (5,1) wording.
- The "numerically" qualifier on the A=48 fraction.
- The scoped closing sentences "This changes no ledger label; Problem~F remains open."

Nothing else, and no label change, is accepted.

## Corrected snippet
None needed.
