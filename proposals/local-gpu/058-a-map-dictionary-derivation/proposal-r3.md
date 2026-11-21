# Proposal 058-a-map-dictionary-derivation, round 3

Round 3 on branch remote/claude. It answers the local re-review `review-local-r1.md` (AWRR: one MAJOR, two
required minors, one optional minor). The package text is not in the current tree, so the insertion is re-anchored
against the current `chapters/appH-microscopic-proofs.tex` (sha256 `fc0884aa8c24e414020520f979a356b07374e2d58e8cdedf55910344a16510c6`).
The deliverable is one insertion, given in full below and as `insert-r3.tex` (CRLF). No labels are added or changed, no bib entries are needed, and no status labels change.

## Result

Within the flat Abelian constant-Θ Moyal class, the A.map data of Problem A are pinned exactly and the
per-order-in-Θ error is explicit. Items 1-4 are unchanged in content from r2. Item 5 is corrected by this round.

1. Plane Weyl data: the pairing Tr W_Θ(f)W_Θ(g) = (2π)^{-2}|Pf Θ|^{-1}∫fg is exact.
2. Finite-N 't Hooft data for one symplectic plane:
   - the product law [Ŵ_v,Ŵ_w] = 2i sin((ϑ/2)σ(v,w))Ŵ_{v+w} is exact for all modes;
   - for mode-limited symbols with 2M<N, Tr Ŵ(f)Ŵ(g) = N Σ f̂_v ĝ_{−v} is exact, and the remainder bound
     ‖R‖ ≤ Σ|f̂_v||ĝ_w|(ϑ|σ|)³/24 holds uniformly in N. Without the mode limit, aliasing terms appear (new check).
3. The Moyal bracket contains only odd powers of Θ, with coefficient −i/24 at order Θ³.
4. The order-Θ symbol of the fluctuating coordinates contains a connection-inducing term. The first correction is
   at order Θ³.
5. **Corrected (MAJOR).** Write the product as f⋆g = fg + B₁ + B₂ + O(Θ³), with B₁ = (i/2)Θ^{ab}∂_a⊗∂_b.
   - The order-Θ² associator is A₂ = B₁(B₁(f,g),h) − B₁(f,B₁(g,h)) − δB₂(f,g,h).
   - The plain signed sum over the six orderings, Alt, kills δB₂ identically for **every** bilinear B₂. The proof
     below is algebraic and uses only commutativity of the pointwise product.
   - Hence Alt(A₂) = [Θ,Θ]^{abc}∂_af∂_bg∂_ch with factor one, whatever order-Θ² correction is chosen.
   - The leading-order freedom B₁ → B₁+δC (C a differential operator) also leaves Alt(A₂) unchanged.
   - Conclusion: Schouten closure of the leading bivector is **necessary** for associativity at order Θ².
     Order-Θ² corrections are not an alternative to it. They are an additional requirement in general, because the
     2D Poisson counterexample shows that the naive truncation fails even when [Θ,Θ]=0.

Assumption `ass:dictionary` is not derived. Problem A stays OPEN. Nothing here closes a critical-path item.

## Response to review-local-r1

- **MAJOR (L128-130): accepted. Re-derived independently, and the R2 replacement is applied verbatim.**
  - *Algebraic proof.* Let A be commutative and φ any bilinear map. Define
    δφ(a,b,c) = aφ(b,c) − φ(ab,c) + φ(a,bc) − φ(a,b)c, and let Alt be the signed sum over S₃.
    - The outer terms cancel. A cyclic relabelling σ → (σ₃,σ₁,σ₂) is even and maps φ(a_{σ1},a_{σ2})a_{σ3} to
      a_{σ'1}φ(a_{σ'2},a_{σ'3}).
    - The inner terms cancel pairwise. For −φ(ab,c), the transpositions σ₁↔σ₂ flip the sign, and ab = ba. The
      same argument applies to φ(a,bc).
    - So Alt(δφ) ≡ 0.
  - Since A₂ = (B₁∘B₁ part) − δB₂, the signed sum of A₂ does not depend on B₂.
  - At leading order, order-1 associativity forces δB₁ = 0. Changing B₁ → B₁+δC alters the B₁∘B₁ part by
    Gerstenhaber brackets [B₁,δC] = ±δ[B₁,C] and [δC,δC] = δ(⋯). These are coboundaries, so Alt kills them.
  - *Mechanical check.* `verify_alt_hochschild_coboundary.py`, run on generic f,g,h rather than only on linear
    functions as in the gatekeeper's `scratch/gk-grpA/alt_coboundary_all.py`:
    - (A) Alt(δB₂)=0 for a generic B₂ with 100 arbitrary coefficient functions: 2D up to order 3 per slot, and
      3D up to order 2 per slot.
    - (B) For a generic 3D bivector (three arbitrary component functions), Alt(B₁∘B₁) = [Θ,Θ]^{abc}∂_af∂_bg∂_ch
      exactly, with [Θ,Θ] totally antisymmetric. The naive-Moyal B₂ instance gives the same result.
    - (C) The B₁ → B₁+δC invariance holds.
  - Hand check of the factor on (x₁,x₂,x₃): Alt(B₁∘B₁) = −¼ · (−2−2)[Θ,Θ]^{123} = [Θ,Θ]^{123}.
  - Avenue 1 of r2 ("without Schouten-closure") is **removed** (see "Remaining open step").
- **MINOR R1 (normalisation): applied verbatim.** The text now says "summed with signs over the six orderings".
  Check (D) confirms that the 1/6-averaged convention gives the same contraction divided by 6, so factor one refers
  to the plain signed sum. This is also the convention of `term_alt` in script 3.
- **MINOR R3 (torus pairing): applied verbatim, with one adjacent repair.**
  - New script `verify_torus_r3.py` (2a)-(2b): Tr Ŵ_vŴ_w = Nδ_{v+w,0} for |m|,|n|≤M with 2M<N. Without a mode limit,
    |Tr Ŵ_{(N/2,0)}Ŵ_{(N/2,0)}| = |Tr Ŵ_{(3,N−2)}Ŵ_{(−3,2)}| = N. These are the aliasing terms.
  - The product law is exact for all modes, so R3's "holds exactly" for the commutator is correct.
  - The adjacent repair concerns the line after R3's last line. That line read "and the operator-norm remainder of
    \(\tfrac1i[\dots]\) … obeys \(\|R\|\le\dots\)" with R undefined. It now reads "and the remainder
    \(R=\tfrac1i[\dots]-\dots\) … obeys the operator-norm bound \(\|R\|\le\dots\)". R3's wording is not wrong; this
    only defines the symbol R it uses.
  - v=(m,n), w=(m',n') and σ(v,w)=mn'−nm' are now defined inline, because R3 uses m,n for v.
  - The symbol bracket is pinned as {e_v,e_w}_Θ = ϑσ(v,w)e_{v+w}, the convention of script 2's `poisson_symbol`.
- **MINOR (optional, θ overloaded; single pair = one plane): adopted.**
  - The torus parameter is now ϑ. The fluctuation field is now a_μ. θ survives only in "|Pf θ|^{-1} density of
    Definition def:matrix-coords-ext", where it is that Definition's own bivector.
  - "At finite N, the analogue of one symplectic plane of these data is the 't Hooft pair".
- **Script defect found while re-running (not in the review).** The scaling table of `verify_nc_torus_bound.py`
  varies ϑ only in the Weyl phase and keeps U at p=1. Its p>1 rows therefore do not realise UV=e^{iϑ}VU. The script
  is left byte-identical, and its output reproduces. `verify_torus_r3.py` (1) redoes the table with U rebuilt for
  each p: the product-law error is ≤2.5e−14 and the bound holds for p=1..4. The bound itself does not depend on the
  table: it follows from the exact product law and |2 sin(x/2) − x| ≤ |x|³/24 (check (3)).
- **Typography ('t Hooft): reversed r2/F6, with evidence.** In LaTeX, ``t produces an opening double quote (“t), which
  is wrong. A straight ' produces ’ (U+2019), the correct elision apostrophe. In the applied-copy build, pdftotext
  shows the bytes `342 200 231 t Hooft`, i.e. U+2019. The snippet uses 't~Hooft.
- **Smallest scoped status close.**
  - The title carries "(conditional; not closure)", the appH convention for paragraphs of this kind.
  - The final sentence closes "so they do not derive Assumption~\ref{ass:dictionary} and Problem~A remains open."
  - The hard-coded "ch03 kinetic term" is replaced by "the kinetic term in~\eqref{eq:Smicro}" (label verified).

## Target and status

- **Problem:** A, matrix-to-modular map, A.map / dictionary sub-target.
- **appH ledger, `sec:status-A` L15-20, re-read in full this round:** "Status: OPEN. Priority: CRITICAL PATH for the
  matrix-derived label. Completion: PROGRAMME-CONDITIONAL."
- **ch17, re-read:**
  - L377-391 (Problem A, the infrared dictionary): OPEN; CRITICAL PATH for the matrix-derived label. A derivation must
    specify the Hilbert space, Weyl map, continuum limit, and error at each order in Θ.
  - L701-703 (completion item): Assumption `ass:dictionary` is derived, or the other chains are re-derived without it.
- **Discrepancies:** none between appH and ch17 for A.
- **Dependencies:** ch03 `eq:NC`, `def:matrix-coords-ext`, `ass:dictionary`/`eq:dictionary`, `rem:ch3-moyal-check`,
  `rem:ch3-trace-quadratic`, `eq:Smicro`; the appH free/Poisson and general-sector paragraphs.
- **Classification:** PROGRAMME-CONDITIONAL. This is a class-restricted derivation of the map data with error
  bookkeeping, plus a necessity obstruction.

## Source reading

Digest + targeted reads. `python scripts/make_digest.py --check` printed `DIGEST CURRENT` (head bc78424,
dirty-chapters: yes). The dirty file is appH, which carries other uncommitted integrations. For that reason appH
was read directly, not from the digest.

Read in full:
- appH L1-99: the whole Problem A section, i.e. ledger label, free/Poisson lemma, general sector and missing step;
- ch17 L372-395 and L660-720;
- ch03 L165-200 (`def:matrix-coords-ext`), L340-450 (`ass:dictionary`, `eq:dictionary`, `rem:ch3-moyal-check`) and
  L450-474 (`rem:ch3-trace-quadratic`);
- `review-local-r1.md`, `proposal-r2.md` and `review-r1.md` (F6);
- the four original scripts and the gatekeeper's `scratch/gk-grpA/alt_coboundary_all.py`.

No unreadable files.

**Current-tree differences from the import.** The r2 anchor sentence "The error bound therefore controls the
difference from an unproven candidate, not from the diamond modular Hamiltonian." no longer occurs. The general-sector
paragraph now ends "…Even if derived, the estimate would therefore control only the difference from an unproven
candidate, not from the diamond modular Hamiltonian." The insertion is therefore re-anchored to that ending.

## Research and reasoning

**Associator algebra.** With f⋆g = fg + B₁(f,g) + B₂(f,g) + O(Θ³), collect the order-Θ² terms of (f⋆g)⋆h − f⋆(g⋆h):
- from B₂(fg,h) + B₂(f,g)h − B₂(f,gh) − fB₂(g,h), which is −δB₂(f,g,h);
- from B₁(B₁(f,g),h) − B₁(f,B₁(g,h)).

Alt(δB₂) ≡ 0 (proof above), so the signed sum is a property of B₁ alone. On linear functions it equals
−¼Σ_σ sgnσ({{x_{σ1},x_{σ2}},x_{σ3}} − {x_{σ1},{x_{σ2},x_{σ3}}}). With {x_a,x_b}=Θ^{ab}:
- {{x_a,x_b},x_c} = −Θ^{cd}∂_dΘ^{ab};
- {x_a,{x_b,x_c}} = Θ^{ad}∂_dΘ^{bc}.

Each signed sum of one of these gives 2[Θ,Θ]^{123}, so the total is [Θ,Θ]^{123}. Script 5 (B) confirms this on
generic f,g,h: the signed sum is exactly the first-derivative trivector contraction, with no higher-derivative
remainder. Therefore:

- **Necessity.** If [Θ,Θ] ≠ 0, then no choice of B₂, and no differential-gauge change of B₁, makes the product
  associative at order Θ². This is the Gerstenhaber obstruction in its Hochschild-Kostant-Rosenberg (HKR) image.
  The HKR statement that every differential Hochschild 2-cocycle is a bivector plus δC is standard and not
  re-derived here. Check (C) covers the δC part for a generic second-order C.
- **Insufficiency of the naive truncation.** Script 4 shows a 2D bivector that is Poisson for dimensional reasons.
  Its naive order-Θ² associator is nonzero (4 terms), while Alt of it vanishes. So correction operators are needed
  in general even when the bivector is Schouten-closed. That they *suffice* for a Poisson bivector is Kontsevich
  formality. It is not used, not cited in the text, and not independently verified here.

The text therefore reads "requires a Schouten-closed leading bivector and, in general, explicit order-Θ² correction
bidifferential operators".

**Consequence for the NAMCG infrared derivation.** A dictionary with a variable expectation-value Θ is possible
only if the condensate selects a Θ whose leading bivector is Poisson. This is a concrete, checkable constraint on
candidate condensates (avenue 2 below). It does not forbid a variable-Θ dictionary.

**Literature.** No citation is added. Kontsevich formality and the Gerstenhaber obstruction are named in this
proposal only as standard context. They are not used in the manuscript text, and no bib entry is needed.

## Claim classification

- **Established identities.**
  - Exact plane pairing with (2π)^{-2}|Pf Θ|^{-1} (scripts 1, 2).
  - Torus product law, exact for all modes (scripts 2, 6).
  - Torus pairing, exact for mode-limited symbols with 2M<N (script 6 (2a)). Aliasing without the limit (6 (2b)).
  - Odd-powers-only Moyal bracket with coefficients i and −i/24 (script 1).
  - Alt(δφ) ≡ 0 for any bilinear φ on a commutative algebra (algebraic proof; script 5 (A)).
  - Alt(A₂) = [Θ,Θ]^{abc}∂f∂g∂h with factor one in the plain signed sum, for any B₂ (script 5 (B), (D)).
- **Conditional results.**
  - Torus remainder bound, uniform in N, under the mode-limit hypotheses (script 6 (1), (3)).
  - Order-Θ fluctuating-coordinate symbol and the Θ³ first correction, within the flat Abelian Weyl calculus.
  - Invariance of Alt(A₂) under B₁ → B₁+δC (script 5 (C)). It is general given HKR for differential cochains,
    which is a standard input and not re-derived.
- **Established counterexample.** The naive truncation fails at order Θ² for a generic Poisson 2D bivector
  (script 4).
- **Not independently verified (context only, unused).** Sufficiency of correction operators for Poisson bivectors
  (Kontsevich formality).
- **Unresolved.**
  - Selection of the data class and of Θ by the matrix condensate.
  - Identification of the induced connection with the kinetic-term connection of `eq:Smicro`, and the constant-Θ
    obstruction of `rem:ch3-moyal-check`.
  - The non-Abelian sector.
  - The unbounded boost/diamond-charge symbol and the sharp cutoff.

## Proposed changes

**File:** `chapters/appH-microscopic-proofs.tex`. This is one insertion, and nothing else in the file changes.

- **Pre-image sha256:** `fc0884aa8c24e414020520f979a356b07374e2d58e8cdedf55910344a16510c6`.
- **Post-image sha256:** `4d6d58cf7947dae9570e917ced6db8b6e40287437162321c4517eb726a568fce`. This is the result of
  applying `insert-r3.tex` (sha256 `c79a07427b6dbdc6016a1cc3fc4c05d409c13cda8c2ed1e43331a6af374015dc`, 55 CRLF lines
  including a trailing blank line).
- **Anchor.** The byte string below occurs exactly once (checked on CRLF bytes). It is the end of the
  general-sector paragraph (current L84-87) followed by the start of the Problem A missing-step paragraph (L90-91):

  ```
  control only the difference from an unproven candidate, not from the⏎diamond modular⏎Hamiltonian.⏎⏎\paragraph{Missing step.}⏎An error-controlled identification of the algebraic inclusion generated
  ```

  The string `\paragraph{Missing step.}` alone occurs 7 times in appH. The second line pins the Problem A instance:
  "An error-controlled identification of the algebraic inclusion generated" occurs once.
- **Placement.** Insert the block after the blank line that follows "Hamiltonian." and before
  `\paragraph{Missing step.}`. All existing sentences are kept unchanged.
- **Encoding.** CRLF line endings, UTF-8 without BOM.

**Labels referenced.** Each occurs exactly once in the `.tex` sources:
- `rem:ch3-trace-quadratic` (ch03:450);
- `def:matrix-coords-ext` (ch03:173);
- `rem:ch3-moyal-check` (ch03:372);
- `eq:dictionary` (ch03:352);
- `ass:dictionary` (ch03:346);
- `eq:Smicro` (ch03:221).

No new labels are defined. The build of the applied copy reports 0 undefined or multiply-defined references.

**Stale passages elsewhere.** None. No chapter mentions Hooft, Schouten or "Weyl data" (grep).

**Full insertion (`insert-r3.tex`, shown here with LF line endings):**

```latex
\paragraph{Explicit Weyl data and per-order error in the flat Abelian class (conditional; not closure).}
Within the constant-\(\Theta\) Abelian Moyal class the map data of Problem~A can be
pinned and the per-order error made explicit. These descriptions are limiting
descriptions of matrix data: \(\Theta\) remains the expectation of the matrix coordinate
commutator, not input geometry. On \(\mathbb R^4\) with constant nondegenerate
\(\Theta\), take \(\mathcal H=L^2(\mathbb R^2)\) and
\(W_\Theta(f)=\int\frac{d^4k}{(2\pi)^4}\tilde f(k)\,e^{\mathrm i k\cdot\hat X}\) with
\([\hat X_\mu,\hat X_\nu]=\mathrm i\Theta_{\mu\nu}\); the pairing
\(\operatorname{Tr}W_\Theta(f)W_\Theta(g)=(2\pi)^{-2}|\operatorname{Pf}\Theta|^{-1}\!\int fg\)
is exact, with the \((2\pi)^{-2}|\operatorname{Pf}\Theta|^{-1}\) trace density of
Remark~\ref{rem:ch3-trace-quadratic} and the \(|\operatorname{Pf}\theta|^{-1}\) density of
Definition~\ref{def:matrix-coords-ext}. At finite \(N\), the analogue of one symplectic
plane of these data is the 't~Hooft pair \(UV=e^{\mathrm i\vartheta}VU\) on
\(\mathbb C^N\), \(\vartheta=2\pi p/N\), with Weyl-ordered symbols
\(\widehat W(e_{m,n})=e^{-\mathrm i(\vartheta/2)mn}U^mV^n\), \(v=(m,n)\),
\(w=(m',n')\) and \(\sigma(v,w)=mn'-nm'\):
\([\widehat W_v,\widehat W_w]=2\mathrm i\sin(\tfrac{\vartheta}{2}\sigma(v,w))\,\widehat W_{v+w}\)
holds exactly; for mode-limited symbols (\(\hat f_v=\hat g_v=0\) unless
\(|m|,|n|\le M\)) with \(2M<N\),
\(\operatorname{Tr}\widehat W(f)\widehat W(g)=N\sum_v\hat f_v\hat g_{-v}\) holds exactly,
and the remainder
\(R=\tfrac1{\mathrm i}[\widehat W(f),\widehat W(g)]-\widehat W(\{f,g\}_\Theta)\), where
\(\{\cdot,\cdot\}_\Theta\) is the symbol-level Poisson bracket,
\(\{e_v,e_w\}_\Theta=\vartheta\,\sigma(v,w)\,e_{v+w}\), obeys the operator-norm bound
\(\|R\|\le\sum_{v,w}|\hat f_v|\,|\hat g_w|\,(\vartheta|\sigma(v,w)|)^3/24\), uniform in
\(N\); the continuum limit is \(N\to\infty\) at fixed modes with \(\vartheta\to0\). Only
odd powers of \(\Theta\) occur in the Moyal bracket; the order-\(\Theta\) term is
\(\mathrm i\{\cdot,\cdot\}_\Theta\) and the first correction is order \(\Theta^3\) with
coefficient \(-\mathrm i/24\), the third-derivative contraction of
Remark~\ref{rem:ch3-moyal-check}. For fluctuating coordinates
\(\hat X_\mu=W(y_\mu+a_\mu)\), the order-\(\Theta\) symbol of
\([\hat X_\mu,\Phi]_\star\) is
\(\mathrm i\Theta_{\mu\nu}\partial^\nu\Phi+\mathrm i\Theta^{\alpha\beta}(\partial_\alpha a_\mu)(\partial_\beta\Phi)\):
the second term is the connection-inducing piece and the first higher-derivative
correction of Equation~\eqref{eq:dictionary} in this class is order \(\Theta^3\) with
third derivatives of \(a_\mu\). For nonconstant \(\Theta\) the naive insertion of
\(\Theta(x)\) into the constant-coefficient Moyal formula generically fails associativity
at order \(\Theta^2\); the order-\(\Theta^2\) part of \((f\star g)\star h-f\star(g\star h)\),
summed with signs over the six orderings of \((f,g,h)\), equals
\([\Theta,\Theta]^{abc}\partial_af\,\partial_bg\,\partial_ch\) with
\([\Theta,\Theta]^{abc}:=\Theta^{ad}\partial_d\Theta^{bc}
+\Theta^{bd}\partial_d\Theta^{ca}+\Theta^{cd}\partial_d\Theta^{ab}\), and
Schouten-closure alone does not remove the full order-\(\Theta^2\) associator of the
naive truncation. No order-\(\Theta^2\) bidifferential correction of the product changes
the first-derivative part of this signed sum, so an associative Moyal-type continuum
description at a variable expectation-value \(\Theta\) requires a Schouten-closed leading
bivector and, in general, explicit order-\(\Theta^2\) correction bidifferential operators.
These statements are for the flat Abelian constant-\(\Theta\) class with mode-limited or
Schwartz symbols; they do not select this class from the matrix condensate, do not
identify the induced connection with the connection of the kinetic term
in~\eqref{eq:Smicro} or resolve the constant-\(\Theta\) kinetic
obstruction of Remark~\ref{rem:ch3-moyal-check}, do not cover the non-Abelian sector, and
do not bound the unbounded boost/diamond-charge symbol or the sharp diamond cutoff, so
they do not derive Assumption~\ref{ass:dictionary} and Problem~A remains open.
```

## Verification scripts

All scripts are in `proposals/local-gpu/058-a-map-dictionary-derivation/`. Run them from that folder with `python -I`.

| # | Script | Output | What it checks |
|---|---|---|---|
| 1 | `verify_moyal_odd_powers.py` | `moyal_out.txt` | Odd-powers-only Moyal bracket, −i/24 at Θ³ |
| 2 | `verify_nc_torus_bound.py` | `torus_out.txt` | Torus product law, bound, pairing, Hermiticity (scaling table defective, see above) |
| 3 | `verify_variable_theta_associator.py` | `assoc_out.txt` | Factor one for the special 3D family; constant and Casimir controls |
| 4 | `verify_poisson_2d_counterexample.py` | `poisson2d_out.txt` | Generic 2D Poisson bivector: c2≠0 (4 terms), Alt=0, constant control |
| 5 | `verify_alt_hochschild_coboundary.py` (new) | `alt_coboundary_out.txt` | (A) Alt(δB₂)=0 for generic B₂; (B) factor-one identity for a generic 3D bivector, B₂-independent; (C) B₁→B₁+δC invariance; (D) the 1/6 convention |
| 6 | `verify_torus_r3.py` (new) | `torus_r3_out.txt` | (1) bound with U rebuilt per ϑ; (2a) pairing under the mode limit; (2b) aliasing without it; (3) the sin inequality |
| — | `apply_and_build_r3.py` (new) | `build_r3_out.txt` | Applies the insertion to a copy outside the repo, checks hashes, anchor and CRLF, runs two pdflatex passes, scans the log, deletes the copy |

**Re-runs this round.** Scripts 1-4 were re-run with `python -I`. Their outputs are byte-identical to the stored
`*_out.txt` files (diff empty for all four).

**Reproduction pack.**
- Scripts 1-4: `python -I verify_moyal_odd_powers.py | diff - moyal_out.txt`, and likewise for `torus_out.txt`,
  `assoc_out.txt` and `poisson2d_out.txt`. Expected: no diff. The "ALL CHECKS" lines are True.
- Script 5: `python -I verify_alt_hochschild_coboundary.py` (about 40 s). Expected:
  - both (A) lines True;
  - "[Theta,Theta]^{abc} (cyclic definition) totally antisymmetric: True";
  - (B) True, and "naive Moyal B2 instance … True";
  - (C) True and (D) True;
  - `ALL CHECKS: True`.
- Script 6: `python -I verify_torus_r3.py`. Expected:
  - p=1..4 with ok=True;
  - (2a) True;
  - (2b) both values 60.0 (= N);
  - (3) True;
  - `ALL CHECKS: True`.
- Apply and build: `python -I apply_and_build_r3.py <repo-root> <empty-dir-outside-repo>`. Expected:
  - `pre-image sha256 : fc0884aa… MATCH`;
  - `post-image sha256: 4d6d58cf7947dae9570e917ced6db8b6e40287437162321c4517eb726a568fce`;
  - `patched file CRLF-pure: True`;
  - pass 2 rc=0, 0 undefined, 0 multiply-defined, 0 errors;
  - `BUILD PASS pages=396`.

## Decisions Taken

- **R1, R2 and R3 are applied verbatim.** Re-derivation confirmed all three. The only adjacent edits:
  - R is now defined, and "operator-norm" moves to "bound". R3's wording is kept; this only defines its symbol.
  - v, w and σ are defined inline.
  - The torus bracket convention is pinned.

  Rejected: leaving R and σ undefined.
- **The optional minor is adopted** (ϑ, a_μ, "one symplectic plane"), because it removes a three-way overload of θ
  in one paragraph at no cost.
- **Typography: 't~Hooft, not ``t Hooft.** The evidence is the rendered glyph U+2019. The r2/F6 recommendation would
  render as an opening double quote.
- **Status close.** "(conditional; not closure)" goes in the title, and "…and Problem~A remains open." ends the final
  sentence. This is one scoped status sentence and no label change.
- **The false avenue is removed.** It is replaced by the route the obstruction actually points to: constrain the
  condensate Θ to be Poisson, then add correction operators.
- **Script 2 is kept byte-identical.** Its scaling defect is recorded, and the fix lives in the new script 6. This
  keeps the earlier gatekeeper reproductions valid. Rejected: editing script 2 in place.

## Milestone assessment

Routine. The round corrects a material overstatement (Schouten closure presented as optional) into a necessity
obstruction. No critical-path step is derived from the matrix theory.

## Status-label recommendation

The current critical-path set, from ch17 L691-720 and the appH ledgers, is A, B, C, D1, E, F, G-derived and N. H, I
and J are optional within their scopes. Problem A remains OPEN / CRITICAL PATH for the matrix-derived label /
PROGRAMME-CONDITIONAL. No label change is proposed.

## Author decision needed

none

## Remaining open step

To close A (derive `ass:dictionary`), the following is still needed:
1. derive that the matrix condensate selects this data class, i.e. which algebra and which expectation-value Θ;
2. identify the connection-inducing term with the kinetic-term connection of `eq:Smicro`, including metric and sign
   matching, and evade the constant-Θ obstruction of `rem:ch3-moyal-check`;
3. extend the map and the per-order bound to the non-Abelian sector;
4. find symbol classes for the unbounded boost/diamond-charge symbol and the sharp diamond cutoff;
5. control the δΘ fluctuation error of the general-sector estimate.

**Ranked open avenues.** The r2 avenue 1 ("without Schouten-closure") is removed as false.
1. **Variable-Θ dictionary with a Poisson leading bivector plus explicit order-Θ² corrections.** Compute B₂ for the
   condensate's Θ and test it against the 2D counterexample. Sufficiency via formality is to be derived, not cited.
2. **Schouten closure as a selection constraint on candidate condensate Θ.** This links A.map to the condensate
   problems.
3. **Extend the per-order calculus to unbounded (boost/diamond-charge) symbol classes.**
4. **Upgrade the δΘ bound via half-sided modular inclusion deformations.** Lead: Lechner-Scotford, arXiv:2111.03172,
   scout Route 6; not independently verified.
5. **Theorem-level continuum-limit language via spectral or covariant propinquity.** Lead: scout Route 1; not
   independently verified.

## Special instructions for the gatekeeper

- Re-run script 5. Confirm that Alt(δB₂)=0 on **generic** f,g,h, not only on linear functions as in
  `alt_coboundary_all.py`. Check the algebraic proof (cyclic relabelling plus pairwise transpositions using
  commutativity).
- Confirm that the R1, R2 and R3 text in `insert-r3.tex` matches your replacements verbatim. The adjacent edits are
  listed in Decisions Taken.
- Check the 't Hooft reversal against your F6.
- Confirm the scope:
  - no sufficiency claim for Schouten closure, no closure language, and the emergence guard sentence intact;
  - one insertion and no label changes;
  - the final sentence is the only status sentence.
- Re-run `apply_and_build_r3.py` against the current tree. If another integration has changed appH, the pre-image
  hash will not match and the anchor must be re-verified.
