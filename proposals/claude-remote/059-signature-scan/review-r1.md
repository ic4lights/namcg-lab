VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M2 | FLAGS: none | PROGRESS: first | OPEN: 0/1

## Verdict
The mathematics holds: I re-derived the rigidity lemma, Claims A and B, the sharpness at t = 0, 1, the Witten h/h̄ comparison and the MW count, and checked them against the sources. The insert still needs three wording fixes before it can be integrated. One sentence calls the pull-back of h₀ "the composite metric", which in this manuscript means the emergent metric (major). The Kontsevich–Segal analogy omits one real difference (minor). One symbol is undefined (minor).

## Source reading
- **Mode:** digest + targeted reads. No full scan is claimed.
- **Digest:** `make_digest.py --check` printed DIGEST CURRENT, `dirty-chapters: yes`. The appH hash in the digest (9443341b74f9) matches the baseline in the proposal.
- **Read in full:**
  - `proposals/059-signature-scan/proposal-r1.md` and `appH_insert.tex`.
  - appH L1482–1581: all of Problem E. This covers the ledger label, 053, 054, the dirty 055/056/057 blocks and the Status anchor.
  - ch17 L392–400 (Problem E) and L690–752 (completion criterion).
  - ch04 L313–333 (`ass:lorentzian`).
  - ch03 L130–204 (`eq:Smatrix`, `def:matrix-coords-ext`).
  - `MILESTONE.md`.
  - ledger entries for 053–058, via grep.
  - Every repository use of "composite metric": appF L18, L30; appG L34; appH L35, L68, L2099, L2117.
- **Other dirty files** (058: ch13, ch16, appE, appI): checked by `git diff --stat` and by grepping the diff for lorentz/signature/status-E, which returned 0 hits. They were not read in full and are irrelevant to E.
- **Scan ruling.**
  - 3(c) is not triggered. The insert adds a conditional paragraph inside `sec:status-E`. It changes no definition, assumption, status passage or ledger label. Its scope sentence restates that `ass:lorentzian` is not discharged and does not alter that assumption's wording or scope; F1 tightens it further.
  - 3(b) is not triggered. M2 is non-stopping under the directive, and no milestone digest follows.
  - 3(d) is met by reading the dirty E passages in full. The ordinal-55 full scan (ledger L369) plus these deltas is the coverage. The next 5th-item scan is due at 60.
- **Unreadable files:** none.

## Claim under review
Replace η in S_b by a real nondegenerate h₀ of signature (10−t, t) and keep Definition (A). The package claims:
1. **Rigidity lemma.**
2. **Real closure points of 𝔆:** t ∈ {0, 1, 9, 10}.
3. **For 2 ≤ t ≤ 8:**
   - paths with Re iS_b ≤ 0 keep h real;
   - single contours with Re M > 0 and P⁻¹h₀ = ±c have real h;
   - so the ε=0 integrand is non-integrable and the domination used in 053 is unavailable.
4. **MW content (cited):** MW iff s−t ≡ 0 mod 8.
5. **Conditional selection:** under P1 ∧ P2, h₀ = ±TᵀηT.

The original target is Problem E: derive Lorentzian signature rather than retain `ass:lorentzian`. Appendix H L1486–1489, verbatim: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. A scope retaining Assumption~\ref{ass:lorentzian} gives up the claim of emergent or matrix-derived Lorentzian signature." ch17 L395 agrees: "OPEN; CRITICAL PATH for the matrix-derived label." The current critical-path set (ch17 L700–733) is A, B, C, D1, E, F, G-derived and N. I found no discrepancy between the two sources.

## Checks performed
**Re-derived by hand:**
- **2×2 identity.** Im det(r+is) = r₁₁s₂₂ + r₂₂s₁₁ − 2r₁₂s₁₂ = tr(adj r · s). Correct.
- **Closed condition.** At N=2, Re iS_b = −Im S_b = −(1/4g²)Σ Im m_ab, so Re iS_b ≤ 0 for all X is equivalent to Im det(h|_E) ≥ 0 for every E. Setting x³ = 0 gives one direction; summing gives the other. A real basis change multiplies det by (det P)² > 0. For N ≥ 3 the su(2)-block embedding reproduces the N=2 form exactly, so the condition is implied.
- **Rigidity lemma.**
  - In an R-orthonormal basis, a V₊ plane gives tr S_E ≥ 0, so λ₁+λ₂ ≥ 0 (take the eigenvector plane). A V₋ plane gives adj(−𝟙) = −𝟙, so ν_{q−1}+ν_q ≤ 0.
  - A mixed plane gives adj diag(1,−1) = diag(−1,1), so S(f,f) ≥ S(e,e) and λ_p ≤ ν₁.
  - The chain 0 ≤ λ₂ ≤ λ_p ≤ ν₁ ≤ ν_{q−1} ≤ 0 uses p ≥ 2 (λ₂ exists) and q ≥ 2 (ν_{q−1} exists). With the two sums it forces every λ and ν to vanish, so the diagonal blocks of S are zero.
  - Off-diagonal step: R(e,e) = cosh²−sinh² = 1 and R(e,f₂) = 0. Since S(f₂,f₂) = 0, the condition gives S(f₂,f₂) − S(e,e) = −sinh 2a · S(e₁,f₁) ≥ 0 for all a, so S(e₁,f₁) = 0. This needs f₂, i.e. q ≥ 2. The two-vector plane {e, f} with f = sinh a·e₁ + cosh a·f₁ gives 0 identically, so f₂ really is needed.
  - The lemma is correct.
- **Why both bounds are needed.** At t=1, 𝓡_u satisfies the condition with S ≠ 0. At t=0, e^{iθ}𝟙 does too. Since det(−h|_E) = det(h|_E), −𝓡_u and −e^{iθ}𝟙 do the same at t = 9, 10. So the t=0,1 examples show q ≥ 2 is needed and their negatives show p ≥ 2 is needed.
- **Open-and-closed corollary.**
  - The set 𝓡_t of real forms with t negative eigenvalues is closed in 𝔇_inv: it is the set of real points intersected with a locally constant inertia.
  - It is open: nearby points of 𝔇_inv have Re h invertible with the same inertia, so the lemma makes them real.
  - 𝔆 ⊂ 𝔇_inv, because 055 (i) makes Re(e^{−iθ}h) > 0, so h is invertible. 𝔆 contains no real form. Hence 𝓡_t ∩ cl 𝔆 = ∅.
- **Claim A via 055 (ii).** Re h has at least nine positive eigenvalues on 𝔆₀, hence at least nine non-negative ones on cl 𝔆₀. A real invertible h there has t ≤ 1; on cl(−𝔆₀), t ≥ 9.
  - Occurrence at t=0: e^{iθ}TᵀT ∈ 𝔆₀ because the pairwise sum 2θ ∈ (0,π).
  - Occurrence at t=1: η = lim 𝓡_u, and real-congruence invariance carries it to all of t=1.
  - t = 9, 10 follow by negation. Correct.
- **Claim B(a).** The path h(τ) is continuous, lies in 𝔇_inv and starts in 𝓡_t. 𝓡_t is clopen in 𝔇_inv, so the path stays in it.
  - Only continuity and invertibility of Λ are used. The regulator and mass enter neither the hypothesis Re iS_b ≤ 0 nor the argument, so "every regulator, any mass term" is proved for this statement.
- **Claim B(b).**
  - h = c(M − 2Σℓ_jℓ_jᵀ) and hΛ⁻¹e_j = Λᵀh₀e_j = −cΛᵀe_j = −cMΛ⁻¹e_j.
  - For complex v and real symmetric R, S, the quantity v̄ᵀhv = v̄ᵀRv + i·v̄ᵀSv has v̄ᵀRv real, so v̄ᵀ(Re h)v = −c·v̄ᵀ(Re M)v < 0 on a complex t-dimensional subspace. Courant–Fischer then gives at least t negative eigenvalues.
  - On {a_jᵀx = 0} (with a_j = Re ℓ_j, b_j = Im ℓ_j): xᵀ(Re h)x = c[xᵀ(Re M)x + 2Σ(b_jᵀx)²] > 0, so at least 10−t positive eigenvalues.
  - The inertia is exactly (10−t, t), and the lemma applies. Correct.
- **Claim B(c).**
  - Tr(CD) is real for anti-Hermitian C, D, so S_b is real when h is real. The mass term with real γ is a pure phase as well.
  - ∫|w∘Λ| = ∫r^{d+n−1}dr · ∫_S|w∘Λ| = ∞, since w∘Λ is a nonzero polynomial.
  - For contour limits, the integrands converge pointwise in X, so a dominating g would dominate the limit integrand, which is non-integrable. Correct.
- **Damped paths at t = 0 and t = 1.**
  - t = 0: h = e^{iπτ/4}𝟙 and S_b = e^{iπτ/2}S_E, using Tr CC = −‖C‖². So Re iS_b = −sin(πτ/2)S_E and Re M = cos(πτ/4) > 0. Correct.
  - t = 1: 𝓡_u per 053.
  - The P1 conclusion is immediate: for 2 ≤ t ≤ 8 the end contour has real h, so it is not damped.
- **Witten comparison.** Im det(h̄|_E) = −Im det(h|_E), so h̄ damps e^{−iS_b}. Also −h ∈ 𝔆 whenever h ∈ 𝔆, while 𝔆̄₀ ∩ 𝔆 = ∅, so −𝔆₀ is not the conjugate pair. Correct.
- **Claim C arithmetic.** s = 10−t gives 10−2t ≡ 0 mod 8, so t ≡ 1 mod 4, so t ∈ {1, 5, 9}.

**Scripts:**
- Re-ran `apply_check.py`: output identical to `apply_check.txt`. The baseline matches, the anchor is unique (count 1, L1575), the insert is ASCII, LF, with no trailing whitespace, and the result is 579472 B, daad5415…2e29, CRLF 3279 and bare LF 0.
- Re-ran `rigidity_checks.py` (ALL PASS, same output) and `colour_first_order_checks.py` (ALL PASS, identical).
- Own check, `C:\Users\redgi\AppData\Local\Temp\claude\3ba14ee056ac155d\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\gk059.py`:
  - Random-plane search with no constructive planes, over 42 random (h₀, S) with t = 2..8: a violating plane was found in every case.
  - Sharpness: 𝓡_{0.3} and −𝓡_{0.3} have minimum sampled Im det 0.454 > 0; e^{0.2i}𝟙 has 0.389.
  - N=2 S_b from explicit commutators against (1/4)Σ minors, at t=3 with complex Λ: relative error 1.6e-16.
  - B(b) inertia: 300/300 contours with Re M > 0 over t = 0..10.
  - Witten pair: h damped, h̄ minimum −0.145, −h damped.
  - These are numerical checks, not proofs.
- **Bib.** `bib/namcg.bib` is 25976 B, a651fe60…c42b, CRLF. The three keys are absent. Baseline + CRLF + CRLF-converted entries gives 26627 B, acbee1ce…738f, matching the proposal.

**Literature, fetched and read this session:**
- **Van Proeyen hep-th/9910030:** arXiv record checked (title, author, KUL-TF-99/37, no journal-ref). PDF pp. 21–22 read: (3.25) "s − t = 0, 1, 7 mod 8 …", (3.28) "MW spinor: s − t = 0 mod 4", and Table 2, whose d=10 row has MW at t ≡ 1 mod 4. The insert's attribution is verified.
- **IKKT hep-th/9612115:** PDF pp. 2–3. (2.1): "θ¹ and θ² are Majorana-Weyl spinors in ten dimensions having the same chiralities". (2.6): κ-fixing θ¹ = θ² = ψ. Verified.
- **Witten 2111.06514:** arXiv record checked (no journal-ref). PDF pp. 8–10: (3.5) Σ|Arg λ_i| < π, "Theorem 2.2 in [6]", (3.6) −(1∓iε), "two different ways", Feynman and complex-conjugate Feynman. Verified.
- **Kontsevich–Segal 2105.10161:** arXiv abstract only, no journal-ref. It contains "Ordinary Riemannian metrics are contained in the allowable domain, while Lorentzian metrics lie on its boundary." This verifies the insert's use, which is only the proposal and the abstract statement.
- All three new bib entries are accurate, and none invents a journal reference.

**LaTeX:**
- `def:matrix-coords-ext` (ch03 L173), `eq:Smatrix` (L143) and `ass:lorentzian` (ch04 L322) are each unique.
- `IKKT1997` exists. No new labels.
- No process language.
- The closing sentence is distinct from the 053–057 closings.
- The colour-mixing probe and the first-order proof are kept out of the insert, which says "no statement about linear maps that also mix the colour components".
- P1 and P2 are stated as premises.
- Nothing claims that Lorentzian signature is derived. No label change.
- I did not re-run the scratch build. The researcher reports 367 pages and 0 undefined references; the integrator's `build_check.py` remains required.

## Findings

**F1 — Severity: major.**
- **Location:** final paragraph of the insert, the sentence ending "…so the signature of the composite metric is a property of the background and is not derived here."
- **Finding:** The pull-back argument concerns the induced tensor g_{αβ} = h₀(∂x, ∂x) of `def:matrix-coords-ext`. Throughout the manuscript, "composite metric" means g = η_AB e^A e^B (appF L30; appH L35, L68, L2099), and `def:matrix-coords-ext` L202–204 explicitly says that g is not asserted to be the emergent metric. The sentence therefore asserts a property ("is a property of the background") of an object the argument does not touch. This is the one place where the scope sentence could be read as a statement about the emergent metric.
- **Required action:** replace the sentence "The induced tensor of Definition~\ref{def:matrix-coords-ext} is its pull-back by a configuration, and for \(h_0\) of signature \((9,1)\) the restriction to a four-dimensional tangent space is positive definite, Lorentzian or degenerate according to the configuration, so the signature of the composite metric is a property of the background and is not derived here." with exactly:
  `With \(h_0\) in place of \(\eta_{IJ}\), the induced tensor of Definition~\ref{def:matrix-coords-ext} is its pull-back by a configuration, and for \(h_0\) of signature \((9,1)\) it is positive definite, Lorentzian or degenerate according to the configuration. Neither its signature nor that of the composite metric is derived here.`

**F2 — Severity: minor (required, since the item returns anyway).**
- **Location:** insert (i), "Two differences matter. \(\mathfrak C\) is invariant under \(h\mapsto-h\), whence the two classes and the values \(t=9,10\), whereas the allowable domain contains no negative definite metric."
- **Finding:** The insert presents the KS domain as containing the Riemannian metrics with the Lorentzian ones on its boundary, and then lists only two differences. 𝔆 contains no real form, so positive-definite h is a boundary point of 𝔆, not an interior one. (i) itself shows this: TᵀT = lim e^{iθ}TᵀT. The matrix counterparts of the Euclidean metrics are h = e^{iπ/4}TᵀT (056 (i)). Leaving this out overstates the analogy.
- **Required action:** replace that passage with exactly:
  `Three differences matter. \(\mathfrak C\) contains no real form, so the positive definite forms also lie only on its boundary, whereas the Riemannian metrics lie inside the allowable domain; the Euclidean contours of the matrix weight are \(h=\mathrm e^{\mathrm i\pi/4}T^{\mathrm T}T\). \(\mathfrak C\) is invariant under \(h\mapsto-h\), whence the two classes and the values \(t=9,10\), whereas the allowable domain contains no negative definite metric.`
  The following sentence, "And~\cite{Witten2021ComplexMetrics} reaches …", stays as it is and is the third difference. No new assumption is introduced: both facts are already established in 055 and 056.

**F3 — Severity: minor.**
- **Location:** insert (iii)(b), "\(hv=-cMv\) on the span of the \(\Lambda^{-1}e_j\)".
- **Finding:** e_j is not defined in the insert.
- **Required action:** replace it with "\(hv=-cMv\) on the span of the \(\Lambda^{-1}e_j\), \(e_j\) the basis vectors of the negative entries".

**F4 — Severity: minor; no insert change.**
- **Location:** proposal §1, "Sharpness".
- **Finding:** The t = 0, 1 examples show only that q ≥ 2 is needed. That p ≥ 2 is needed follows from their negatives (t = 9, 10), since det(−h|_E) = det(h|_E). The insert makes no sharpness claim, so this is a record correction only.

**F5 — Severity: none (record only).**
- The first-order colour-mixing proof in proposal §6 was not reviewed as an accepted result. I re-ran its numerical checks only. It is correctly excluded from the insert.

## Scope of what is established

**Proved (exact, every N):**
- **Rigidity lemma** (p, q ≥ 2 ⇒ h real), and its clopen corollary.
- **Real closure points of 𝔆** are exactly t ∈ {0, 1, 9, 10}.
- **Path rigidity.** For 2 ≤ t ≤ 8, every continuous path of invertible linear colour-blind contours from a real contour with Re iS_b ≤ 0 keeps h real. This holds for any regulator and any mass term.
- **Single contours.** Single contours with Re M > 0, under P⁻¹h₀ = ±c (which includes Definition (A) with h₀ = diag(±1)), have real h.
- **Consequences.** On these contours S_b is real, nothing is damped, the ε=0 integrand is not absolutely integrable, and the domination of 053 is unavailable, including on invertible limits.

**Cited and verified:** MW iff s−t ≡ 0 mod 8, so t ∈ {1, 5, 9} at d = 10; the IKKT content is one MW spinor.

**Conditional (PROGRAMME-CONDITIONAL):** h₀ = ±TᵀηT under P1 (an imposed representation premise) and P2 (supplied fermion content; eq:Smatrix is bosonic). This concerns the target contraction only, not the emergent or composite metric.

**Not established:** Lorentzian signature of the emergent metric, and discharge of `ass:lorentzian`. Problem E remains "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL." No label change.

**Hypothesis class of the no-go:**
- linear contours that do not mix colour;
- Re iS_b ≤ 0 along the path (for (a)), or Re M > 0 with P⁻¹h₀ = ±c (for (b));
- a damped-contour representation of the limit;
- ε → 0 at fixed N.

**Open relaxations, ranked by promise for the IR / full-GR derivation:**
1. **Signature of the induced or composite metric on a selected background** (the scout's R2, a D1/E coupling). This is the step that actually bears on `ass:lorentzian`; this package shows the target-contraction step cannot discharge it by itself.
2. **H9/H3: whether lim_{ε→0} I_ε exists for 2 ≤ t ≤ 8** at N=2 (bosonic first) by a non-dominated or oscillatory route. This decides whether P1 is a real restriction or only one of representation.
3. **H2: colour-mixing linear maps, non-perturbatively.** Only first order is done, and that only in the proposal.
4. **H1: non-linear contours or Lefschetz thimbles** for 2 ≤ t ≤ 8.
5. **P2 alternatives, and N → ∞ taken first** (low feasibility).

**Milestone:**
- **M2 (non-stopping):** a bounded no-go on the damped-linear-contour route for target signatures 2 ≤ t ≤ 8. This is consistent with how 053–057 were classified.
- Not M1, M3, M4 or M5. Not a breakthrough.

## Recommended disposition
Revise. Apply F1–F3 verbatim in r2. The bib entries and the anchor are unchanged, but the insert hashes in `apply_check` must be regenerated. If the r2 diff is limited to these replacements, it should be acceptable without further mathematical review.

## Corrected snippet
The F1, F2 and F3 replacement texts are given verbatim above. No new physics or assumptions are involved.

VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M2 | FLAGS: none | PROGRESS: first | OPEN: 0/1
