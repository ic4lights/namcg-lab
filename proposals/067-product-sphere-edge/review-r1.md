VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/3

## Verdict
The exact lemmas and the reproduction pack check out, but three sentences of the insert need correcting before integration: one numerical range statement is false as worded, one conclusion is extrapolated beyond what was tested, and the paragraph does not say that the block is still a region of a compact internal factor.

## Source reading
Digest + targeted reads; no full scan was done or claimed.
- `python scripts/make_digest.py --check` printed `DIGEST CURRENT`; `chapters/` and `bib/` are clean at HEAD 54a2dcb.
- A full scan is not required: the proposed ordinal is 64 (next 5th-item scan at 65), there is no milestone, and the insert changes no definition, assumption, scope or status passage.
- Read in full:
  - `proposal-r1.md`, `appH_insert.tex`, all five scripts and their saved outputs, `build_r1.txt`;
  - appH `sec:status-G` L2850-2896, including the whole 065 paragraph;
  - ch17 L474-495 (Problem G and G completion levels);
  - ch03 `def:matrix-coords-ext`; ch12 `def:HBEV` and `ass:Sent-density`;
  - ledger entries 064-066; 065 `review-r2.md`; the G-derived block of `reports/graph/frontier.yaml`.
- Not read: ch04 `eq:g-from-e` (only its label uniqueness was checked; the insert makes a negative statement about it). No file was unreadable.

## Claim under review
- **Claim.** On the product of two deformed fuzzy spheres with positive contraction, for toric blocks at a fixed frame:
  - exact edge-operator lemma (E diagonal, rank = number of edge sites, closed forms);
  - pointwise identity making P_K the 3-volume in γ̃ = (√g/ρ)^{2/3} K^{-1};
  - √2 T ≥ P_K, scaling exponents, and a crystalline T-density for oblique half-planes;
  - exact 2r × 2r reduction of the charge Q and diagonal ⟨YY†⟩ for Gaussian momenta;
  - numerical statements on rows (Monte Carlo) and on the Weyl dimension;
  - bearing: the 065 "single row" cause is removed, while rank dependence, frame, state and compactness persist.
- **Original target.** G-derived: matrix-derived S_ent(h_ij, φ) on ∂M (`ass:Sent-density`), boundary stationarity (`ass:bdy-EE`), and Λ_eff from `eq:Leff`.
- **Appendix H, verbatim.** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope results: G-model and G-external support at most a scope-limited model; G remains OPEN and neither satisfies the matrix-derived criterion."
- **ch17, verbatim.** "CRITICAL PATH; mechanism CLOSED CONDITIONALLY, derivation OPEN."
- **Labels.** No status, priority or completion label is changed. The closing sentence restates the existing label and is scoped; "PROGRAMME-CONDITIONAL" occurs once in the insert.

## Checks performed
**Reproduction pack (directly verified).**
- e1, e2, e3, e4 re-run: all exit 0, stdout identical to the saved `*_output.txt` files.
- `apply_check.py` re-run in report mode: APPLY CHECK PASS.
  - Baseline appH 624232 B, sha256 c2dac013...; anchor occurs once at L2894, inside `sec:status-G`.
  - Result 634866 B, sha256 e098f981..., 3405 CRLF, 0 bare LF.
  - Six refs each resolve once; no new label; the cite key exists once; delimiters balanced; no process language.
- The repository was unchanged after the runs.

**Independent re-derivation (by hand).**
- Edge operator.
  - A¹J¹ + A²J² = ½(A¹ − iA²)J⁺ + ½(A¹ + iA²)J⁻; the J³ part drops because Θ is diagonal.
  - Same-I hops stay in one factor. The J⁺Θ̄J⁻ terms are diagonal with coefficient k_f and entries i(N−i) and (i+1)(N−i−1).
  - The J⁺Θ̄J⁺ terms connect i and i∓2 through an outside site, which is exactly the excluded pattern; their coefficient ¼Σ(A¹ ∓ iA²)² vanishes iff AᵀA is a multiple of the identity on the plane.
  - rank 𝓔 = rank E and T is the trace norm. The cap × sphere and product-block closed forms are correct.
- Pointwise identity.
  - K(df,df) = Σ_I {f,x^I}²; det K^{-1} = ρ⁴/det g; cofactor step det₃(K^{-1}|_ij) = K⁰⁰ det K^{-1}.
  - Hence (√g/ρ)√det₃K^{-1} = ρ√K⁰⁰ = √det₃γ̃. Correct.
- Cap × sphere measure.
  - P_K = N√(M₁(N−M₁)) · mean|A₁e_φ| and k₁ = ½·mean|A₁e_φ|², so √2T/P_K = rms/mean ≥ 1, with equality iff σ₁ = σ₂. Correct.
  - Scaling exponents re-derived from the block-diagonal g and K^{-1}. Correct.
- Half-plane counting (a ≥ b ≥ 0).
  - The last site of each fixed-i₂ line is the only edge site, and it has a second outside neighbour exactly at a step.
  - Densities n₁ (rank), n₁e₁+n₂e₂ (s²), (n₁−n₂)√e₁ + n₂√(e₁+e₂) (T). The Minkowski step and its equality cases are correct, as is the P_K/√2 density √(n₁²e₁+n₂²e₂).
  - The "only" in bearing (ii) also holds for deformed A_f, by combining Minkowski with Jensen on the L¹ versus L² averages; both inequalities point the same way.
- Charge reduction.
  - QU = U(−2i)(α−α†) + 2iVR and QV = −2iUR†; for α = 0 the spectrum is ±2 sv(C_⊥). Correct.
  - D is diagonal by torus weight conservation; ⟨YY†⟩ is diagonal because two links into one outside site are either the excluded pattern or carry different a. Correct.
  - Uniform W for cap × sphere follows from the Schur row sum (2l₂+1)/N. Correct.
- Numbers in the insert against the outputs: 1.113, 1.096, 10⁻⁴; 0.85/0.94/0.93/0.95, sixteen positive eigenvalues, cv 0.3 in the last three; 3.38 → 4.60 against 3.91. All match.

**My own checks** (scripts in `C:\Users\redgi\AppData\Local\Temp\claude\3ba14ee056ac155d\8445fbac-1820-4671-b227-7d272a39e1df\scratchpad\gk067\`: `gk_rows.py`, `gk_dim.py`).
- N-scaling, cap × sphere (N = 8, 12, 16; l_c1 = N−1, l_c2 = 3): ⟨Σ pos Q⟩/(2√W T) = 0.89, 0.92, 0.94, while the ratio to 2√W s is 2.5, 3.2, 3.8. This supports "follows T, not s".
- Non-uniform edges (N = 12, ν₂/ν₁ = 3):

  | Block | M | r | ratio to 2Σ_u√Et_u | ratio to 2√(rΣEt_u) |
  |---|---|---|---|---|
  | product 6×3 | 18 | 8 | 0.82 | 0.79 |
  | product 3×7 | 21 | 9 | 0.83 | 0.72 |
  | half-plane b/a = 0.41 | 55 | 12 | 0.92 | 0.81 |

  The local-sum form is closer and more stable, but the separation (4-13%) is of the order of the stated accuracy. This case is not in the pack (see F2).
- Weyl dimension at unsampled points of the range stated in the insert (see F1): the stated bounds fail.

**Not independently verified.**
- The scratch build (`build_r1.txt`: 384 pages, 0 undefined) was not rebuilt by me.
- arXiv:2408.05274 was not re-fetched; I rely on its verification in the 065 reviews. No new citation is added.

## Findings

**F1. Major. Insert, "Dimension" paragraph.**
- Finding: the sentence "log d = 2rℓ[log(M/(r+ℓ))+c] with 0.80<c<0.97 for 1≤r≤160, 4≤ℓ≤400, M=4000 and 16000 … by a factor between 0.69 and 0.98 in that range" is false as a range statement.
- Reason: e4 evaluates seven (r,ℓ) pairs only. Inside the stated range I find:
  - c = 1.041 and 1.005 at (r,ℓ) = (1,400), M = 4000 and 16000;
  - c = 0.796 at (2,4);
  - factor 0.55 and 0.62 at (160,4).
  The slope claim "for M≥4000, r≤160, ℓ≤40" likewise rests on six sampled pairs.
- Qualitative conclusions (c of order one, rank entering through M/(r+ℓ), sub-additivity) are unaffected.
- Required action: state the sampled pairs instead of a range (snippet S1), or extend e4 over a grid and quote the bounds actually found.

**F2. Major. Insert, Bearing (i) and (ii).**
- Finding: "the number of boxes … is, within the accuracy of the numerical comparison above, a sum over the sites of a three-dimensional edge of a quantity fixed by the links at that site" and "The measure of that sum is T weighted by the state" are stated for the factor in general.
- Reason: the Monte Carlo covers only cap × whole sphere, where all N edge sites are equivalent. There Σ_u√Et_u = √(r ΣEt_u), so the comparison cannot distinguish a local sum of square roots from a non-local combination.
- Consequence: the crystalline-anisotropy conclusions in the Measure paragraph are exact statements about T, but they bear on the entropy only through this untested identification.
- Evidence: my check above is mildly favourable but not decisive at these sizes.
- Required action: either restrict (i)/(ii) to the tested block and mark the non-uniform case untested (snippet S2), or add a non-uniform-edge Monte Carlo (product and oblique blocks, larger M/r) to e3 and quote it.

**F3. Major (scope wording; the named test target). Insert, Bearing (iv) and the first paragraph.**
- Answer to the test: 067 does **not** leave the 065 class clause "a compact internal factor with positive contraction". S²_N × S²_N with δ_IJ is a compact factor with positive contraction, and the block is a region of that factor. It is not a "4D region × fibre" spacetime block.
- What 067 relaxes: the dimension of the factor (2 → 4) and the clause "single projector or coaxial cap pair" (→ toric blocks). It keeps: fixed frame, leading order with one dominant irrep, Gaussian proxy states, and the FFHS block algebra.
- Accuracy of the texts:
  - The proposal md is accurate on this (section 1, Result (c), H6).
  - The insert says "compact four-dimensional fuzzy factor" and, in (iv), "the factor is compact with a positive contraction". That is correct but incomplete: it compares the edge with "the dimension of ∂M in Definition def:HBEV" and never says the block is still not a region of the emergent spacetime and its edge is not ∂M.
  - The proposal's own stale-passage note restricts 065's bearing (i) "to the single cap it treats", which leaves the point unstated for the new block.
- Required action: add one clause to (iv) (snippet S3).

**F4. Minor. Insert, Bearing (iii).**
- Finding: "the value for r rows is not r times the value for one row" is a comparison at the same M.
- Reason: for the cap × sphere, M = M₁N and r = N, and for ℓ ≪ N the value is extensive in N with a per-site factor log M₁ + c. The non-locality there is carried by the depth, not by r.
- Required action: insert "at the same M" (snippet S4).

**F5. Minor. Proposal md only (Result, first paragraph).**
- Finding: 065's avenue 1 is glossed as "a block with a three-dimensional edge". The ledger records avenue 1 as "A spacetime-block subsystem (4D region x fibre)".
- Required action: correct the wording in r2. The ledger and frontier should record 067 as a compact proxy, with `G.spacetime-block` still untried.

**F6. Minor, optional. Insert, "Rows".**
- "it follows T … and not s" rests on a single N in the pack. My N = 8, 12, 16 check supports it; adding that scan to e3 would put the evidence in the pack.

**Observation, no action.** The closing sentence duplicates the 065 closing sentence nearly verbatim in the adjacent paragraph block. Each block needs its own scoped status sentence under CLAUDE.md, so I do not object.

## Scope of what is established
- **Proved (exact, finite N).** Edge-operator lemma, rank and closed forms; charge reduction; diagonal ⟨YY†⟩ and uniform W for the stated Gaussian class.
- **Proved (exact, Poisson kinematics).** Pointwise identity for γ̃; √2T/P_K = rms/mean; scaling exponents; half-plane densities and the Minkowski inequality.
- **Numerical.**
  - Box count ≈ 2√W T for cap × sphere only (N = 16; 5-15%).
  - Weyl-dimension values at the sampled pairs only.
- **Conditional** (imported leading-order FFHS entropy, fixed frame, equal rows): log d_μ is not an integral of an edge-local density, because of the depth dependence.
- **Supplied inputs.** State, cut-offs, frame.
- **No-go class, stated exactly.** Compact internal factor S²_N × S²_N with positive contraction; toric blocks at one fixed frame without the excluded pattern; Gaussian proxy momenta; FFHS block algebra at leading order with one dominant irrep. It closes nothing outside that class, and the replica route of `ass:Sent-density` is untouched.
- **Status.** PROGRAMME-CONDITIONAL; G remains OPEN / CRITICAL PATH. Not a breakthrough, no milestone, no label change.

**Relaxations that could still favour G-derived, ranked.**
1. A genuine spacetime-block subsystem (region of the non-compact / Lorentzian leaf × fibre). This is 065's avenue 1 and is still untried; it relaxes "compact, positive contraction" and needs a state where the weight is not positive.
2. Combinations that cancel the depth dependence (mutual-information type for adjacent toric blocks), which relax the single-block functional.
3. The frame average and its minimisation, and non-toric projectors, which relax "fixed frame"; this tests whether the crystalline anisotropy survives.
4. A within-core state (e^{-S/2} or OS reconstruction on fibre modes), which relaxes the Gaussian proxy and could change the site-counting of the fibre.
5. A fixed-volume partition-function route, independent of the factorisation map.
6. Subleading orders or an alternative subsystem algebra; the vacuum term of 2303.08012.

## Recommended disposition
Revise. Apply S1-S4 (or the evidence alternatives in F1/F2), correct the md wording of F5, and return as r2. No other change is needed; the anchor, references, CRLF plan and build record are in order.

## Corrected snippet
No new physics or assumptions; these only narrow wording.

**S1** (Dimension; replaces from "the Weyl dimension formula gives" through "in that range (numerical)"):
```latex
the Weyl dimension formula, evaluated at \((r,\ell)=(1,40),(4,40),(16,40),(40,40),(160,40),(40,4)\) and \((40,400)\) with \(M=4000\) and \(16000\), gives \(\mathrm d\log d/\mathrm d\log M=2r\ell\) to within \(2\%\) in the six cases with \(\ell\le40\), and \(\log d=2r\ell\,[\log(M/(r+\ell))+c]\) with \(0.80<c<0.97\) in all of them; for \(r>1\) this is below \(r\) times the value for one row on each side at the same \(M\), by a factor between \(0.69\) and \(0.98\) in these cases (numerical; sampled values, not bounds over a range)
```

**S2** (Bearing (i) and the first sentence of (ii)):
```latex
(i) For the cap times the whole second sphere, whose edge sites are all equivalent, the number of boxes, the coefficient of the logarithm in \(\log d_\mu\), is, within the accuracy of the numerical comparison above, a sum over the sites of a three-dimensional edge of a quantity fixed by the links at that site and by the row sums \(D_v\) of the state; the single row of the preceding paragraph was special to a one-dimensional edge. For edges whose sites are not equivalent, the sum of the square roots of the entries of \(\langle YY^\dagger\rangle\) is the corresponding estimate, and its agreement with the number of boxes is not tested here. (ii) With that proviso the measure of that sum is \(T\) weighted by the state.
```

**S3** (end of Bearing (iv); replace the final full stop):
```latex
, and the factor is compact with a positive contraction: as in (i) of the preceding paragraph, the block is a region of this factor and not of the emergent spacetime, and its edge, though three-dimensional, is not the boundary \(\partial M\) of Definition~\ref{def:HBEV}.
```

**S4** (Bearing (iii)): replace "the value for \(r\) rows is not \(r\) times the value for one row" with "the value for \(r\) rows is not \(r\) times the value for one row at the same \(M\)".

Relevant paths:
- `C:\Users\redgi\Projects\namcg-lab\proposals\067-product-sphere-edge\proposal-r1.md`
- `C:\Users\redgi\Projects\namcg-lab\proposals\067-product-sphere-edge\appH_insert.tex`
- `C:\Users\redgi\Projects\namcg-lab\proposals\067-product-sphere-edge\e3_charge_rows.py`
- `C:\Users\redgi\Projects\namcg-lab\proposals\067-product-sphere-edge\e4_dimension.py`
- `C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex` (L2850-2896)
- `C:\Users\redgi\Projects\namcg-lab\reports\graph\frontier.yaml` (L347-362)
