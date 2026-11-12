# Proposal 060-semiclassical-signature-domains, round 2

## r1 → r2 change list

The review-r1 verdict was ACCEPT WITH REQUIRED REVISIONS, with two major and seven minor findings. The r1 bytes are kept as `appH_insert.r1.tex` (10284 B, f2a08fbc…94ee) and `bib_entries.r1.bib` (877 B, e142c5c0…daf7). `apply_r2_edits.py` performs every edit. It checks both r1 hashes, and asserts that each old string occurs exactly once before replacement and each new string exactly once after; its output is in `apply_r2_edits.out.txt`. All strings are Python raw strings.

| Finding | Change in `appH_insert.tex` (verbatim from review-r1 "Corrected snippet" unless noted) |
|---|---|
| **M1 (R1)** | The kinetic tensor is now written \(\mathsf K\): its definition ("…that of Definition~\ref{def:matrix-coords-ext} with \(h_0\) in place of \(\eta_{IJ}\)"), the Gram sentence, the Sylvester sentence, \(\mathsf K=m^2\eta^{-1}H\eta^{-1}\), \(\mathsf K=0\) where \(m=0\), and the dilaton "\(\rho^2=\rho_M|\det\mathsf K^{\mu\nu}|^{1/2}\), with \(\mathsf K\) the tensor written \(\gamma^{\mu\nu}\) there,". **Deviation (string only):** the review's old string "four, \(\gamma\) has, by Sylvester's" does not occur in r1; the r1 text is "…does not depend on the fibre point, \(\gamma\) has, by Sylvester's". I applied the same substitution γ → \(\mathsf K\) to the actual string "point, \(\gamma\) has, by Sylvester's". Every remaining γ is the mass parameter, apart from the explicit pointer to the notation of 2605 (the script lists all nine). |
| **M2 (R2)** | The two so(4,2) sentences are replaced by the subalgebra argument: the T^a span so(4,1) on the five indices; a non-compact simple Lie algebra has no non-trivial Hermitian N×N representation; so(5)⊂so(6) has such representations; so a non-zero finite-N solution has η definite on the five indices. |
| m1 (R3) | "\(\ell^2=-y_ay^a\)" → "\(y_\mu y^\mu=-\ell^2-m^2\)". |
| m2 (R4) | The criterion now fails as "The Euclidean criterion …"; for η, the window |t′−t|<Δ_T = 0 contains no t′≠t, and the ratio grows like σ⁻². The Gaussian state's "uncertainty σ" stands in place of Δ_T, since no quasi-coherent state exists. |
| m3 (R5) | w is "likewise a supplied momentum scale, and no width is derived". |
| m4 (R6) | The quoted constant is now "of order \(g_{\mathrm{YM}}\)". The factor-2 error in 2605 Eq. (64) changes the printed g_YM/√2 of Eq. (100). |
| m5 (R7) | Base coordinates: "with \(c>0\) for \(h_0\) of signature \((9,1)\) as above". |
| m6 (R8) | "do not apply to the conjugate-coordinate backgrounds". |
| m7 (R9) | Steinacker2026Weak gains `note = {Version 2; the equation numbers cited refer to it}`. |
| Optional item 10 | **Adopted:** "The same mechanism, averaging over the fibre, gives the signature change of~\cite{Steinacker2018BB}, where,". This avoids implying that the four-matrix computation appears in that paper. I did not adopt the second optional idea, relating the identity to the h-form equation of Liao2026, because I have not read that paper beyond the abstract. |

### New check and re-runs

**New script.** `s5_subalgebra_span.py` (output `.out.txt`) supports M2. It computes the closure of the four T^a under commutators: dimension 10, equal to the complex span of the M^{AB} on the five indices. It then gives the trace-form inertia, which is proportional to the Killing form, on the real elements:

| Case | Span | Inertia | Type |
|---|---|---|---|
| so(4,2), c₀=4 (the class) | so(4,1) | (4,6) | non-compact |
| so(4,2), c₀=5 (base coordinates) | so(3,2) | (6,4) | non-compact |
| so(6) twin | so(5) | (0,10) | compact |
| so(5,1) with spacelike S = {1,2,3,4}, c₀ = 5 | so(5) | (0,10) | compact |

The last row is the reviewer's counterexample to the r1 wording: a non-compact form with a finite-N solution.

**Re-runs.**
- `apply_check.py` was re-run; the output is in `apply_check.txt`, and the r1 output is kept as `apply_check.r1.txt`.
- s1–s4 are unaffected and not re-run; the gatekeeper found them byte-identical on re-run.
- The scratch build was re-run.

**Proposal-level corrections, the same claims as in the insert:**
- the M2 subalgebra point (§2.4, Result 4, Claim classification, Milestone (c));
- the effect of the Eq. (64) factor on the late-τ constant of Eq. (100) (§2.1, §2.6);
- the notation \(\mathsf K\) throughout;
- the Minkowski-window point (§2.2);
- w as a momentum scale (§2.2);
- the definition of ℓ (§2.4).

## Result

This package tests the two supplied background classes against the semi-classical criterion of arXiv:2605.13294 v2, and determines where the kinetic tensor \(\mathsf K\) of each class is Lorentzian, Euclidean or degenerate. There is no label change. Problems D and E remain OPEN, CRITICAL PATH and PROGRAMME-CONDITIONAL.

1. **The criterion, verified from the v2 source and PDF.**
   - Δ_T is the uncertainty of the quasi-coherent states (13).
   - The proposed condition is max|⟨⟨t|𝒜|t′⟩⟨t′|𝒜|t⟩⟩|^{1/2} ≪ Δ_T, with |t′−t| < Δ_T for Minkowski signature (16, 17).
   - The paper evaluates it at tree level in a Lorentz/Feynman gauge, and states that it fails for commutative backgrounds.
   - Equation numbers are those of the v2 PDF: coupling (89), late-time estimate (100). The scouts' (104) and (115) are HTML numbering.
2. **First-order class (050–052), flat point: bounded no-go.**
   - No quasi-coherent state exists, so Δ_T = 0 and the Euclidean criterion (16) fails.
   - At finite N, for η, the window of (17) is empty for t′ ≠ t.
   - A Gaussian state of uncertainty σ (in place of Δ_T) gives a ratio of the two sides of g/2σ² (Euclidean) or 2^{−3/4}g/σ² (η, Definition A). This grows like σ⁻² as σ → 0, so a window needs a supplied σ ≫ g^{1/2}.
   - The weight w of 051/052 is likewise a supplied momentum scale.
3. **Lemmas on \(\mathsf K\).**
   - (i) Gram positivity: there is no Lorentzian \(\mathsf K\) in the Euclidean model, consistent with 2512.03161.
   - (ii) Sylvester: for a fibre-independent rank-4 frame, sig \(\mathsf K\) = sig(h₀|_W).
   - (iii) Fibre averaging can change the signature.
4. **CP^{1,2} class (045–049), conjugate coordinates.**
   - \(\mathsf K\) = m²η⁻¹Hη⁻¹ with H = Lᵀh₀L.
   - The exact Lie identity shows that the EOM holds iff H = cη, with mass γ = 3cη^{c₀c₀}.
   - For h₀ of signature (9,1), which 059 obtains under P1∧P2: c > 0, W is timelike, γ > 0, and \(\mathsf K\) is Lorentzian on m ≠ 0. \(\mathsf K\) = 0 at m = 0.
   - The so(6) twin solves the same equation at the same sign of γ, with a positive definite \(\mathsf K\), so the classical equation selects nothing.
   - The T^a generate the subalgebra so(4,1) on the five indices. A non-compact simple algebra has no non-trivial Hermitian N×N representation, so within this family a non-zero finite-N solution has η definite on the five indices. It therefore has a positive definite \(\mathsf K\), and **the Lorentzian member exists only for N → ∞ first**, at fixed γ > 0.
5. **Base coordinates as matrices.**
   - γ = −3c, with c > 0 for (9,1).
   - The fibre average of \(\mathsf K\) is diag(m², (2ℓ²−m²)/3 ×3). It is positive definite for 0 < m² < 2ℓ² and Lorentzian with reversed overall sign for m² > 2ℓ².
   - The same fibre averaging gives the signature change of 1709.10480. There, κ² = 1 is Euclidean everywhere, and κ² > 1 requires two mass parameters.
6. **Coupling.**
   - ρ_M ∝ 1/|m|, so g² ∝ |m|⁻³ in the conjugate presentation, diverging at the only non-Lorentzian locus. In the base presentation g² ∝ |2ℓ²−m²|^{−3/2}.
   - 2605 Eq. (100) estimates the ratio of the two sides as of order g_YM at late τ. The printed g_YM/√2 is changed by the factor 2 in its Eq. (64), so the corrected value is g_YM, an order-one change. On that estimate the semi-classical domain lies inside the Lorentzian one.

**Bottom line.** Together with 059, the signature of \(\mathsf K\) in the manuscript's CP^{1,2} presentation comes from three sources:
- the target contraction, (9,1) under P1∧P2;
- the real form of the supplied background algebra;
- the classical equation, which forces compatibility but does not select.

The Lorentzian member needs N → ∞ first and fixed γ > 0, which is the corner 053–059 leave open. No signature, background or frame is derived.

## Target and status

The target is unchanged from r1.

**Problem E** (appH L1486–1489, verbatim): "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. A scope retaining Assumption~\ref{ass:lorentzian} gives up the claim of emergent or matrix-derived Lorentzian signature."
- Original target (ch17 item 5): "Lorentzian signature is derived rather than retained."

**Problem D** (appH L600–603): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: D2, …".
- D1 target (ch17 item 4): SO(3,1) derived, "the locked frame and its non-degeneracy on the claimed domain are derived, not assumed".

**Dependencies:** ass:lorentzian, ass:frame-lock, ass:nondeg, def:matrix-coords-ext, eq:Smatrix, blocks 045–052, and the P1/P2 of 059.

**Critical-path set** (ch17 L700–733): A, B, C, D1, E, F, G-derived, N. There is no discrepancy with appH. Everything here is PROGRAMME-CONDITIONAL.

## Source reading

Mode: digest + targeted reads, as in r1. For this round I also read review-r1 in full. The baselines were re-verified: appH is 579751 B (b6c505ad…5a8a) and the bib is 26627 B (acbee1ce…738f), both matching. No full scan is claimed and none is due (ordinal 58).

## Research and reasoning

Sections not listed below are unchanged from r1 §2.1–2.9.

### 2.1 Criterion

As in r1. Eq. (64) is low by a factor 2, so Eq. (63), Eq. (99) and the late-time constant of Eq. (100) change by an order-one factor: Δ^Q is larger by √2, so the ratio becomes g_YM rather than g_YM/√2. The insert therefore says "of order g_YM". No "≪" conclusion changes.

### 2.2 Flat point

Derivation as in r1, with two corrections.
- **Δ_T.** No quasi-coherent state exists, so the Gaussian state's uncertainty σ is used in place of Δ_T. With the quasi-coherent definition the infimum is 0, so (16) fails.
- **Finite N.** For (17) at finite N the window |t′−t| < 0 is empty for t′≠t. The eigenvector argument therefore establishes failure of (16) only. For η, failure follows from the σ⁻² growth of the ratio.
- **The weight w.** w (051/052) weights p for label truncation. Δ_T measures the spread of p̃ = up, which under the non-compact fibre is not the width of w. So w is a supplied momentum scale, not "such a width".

### 2.4 Conjugate coordinates

- Here ℓ is the orbit constant, y_Ay^A = −ℓ² over A = 0..4, so y_μy^μ = −ℓ² − m² (appH L1378, L2426).
- The identity and the EOM equivalence are as in r1.
- **Finite N (corrected).** The EOM involves only the T^a and their commutators. These span so(η restricted to {a, c₀}): so(4,1) for the class, so(3,2) for the base presentation, so(5) for the twin (s5).
  - A non-trivial Hermitian representation of a simple algebra 𝔤 is injective. Its image lies in 𝔲(N), where −tr(XY) is positive and invariant, so the Killing form of the image is negative definite. Hence 𝔤 is compact.
  - So a non-zero finite-N solution has η definite on the five indices. With c > 0 and (9,1), definite means δ, so \(\mathsf K\) is positive definite.
  - The Lorentzian member (η of signature (4,1) on the five indices) exists only as N → ∞.
  - The r1 wording ("compact forms" of the ambient so(p,q)) was false: so(5,1) with spacelike S ∪ {c₀} gives a finite-N solution through so(5) (s5).

### 2.5 Base presentation

As in r1. c > 0 is now stated explicitly. The 1709.10480 sentence now reads "the same mechanism … gives the signature change of", making no claim that the four-matrix result appears there.

### 2.8 Fork

As in r1, with no-go (c) corrected: no finite-N exact Hermitian solution in the family has a Lorentzian \(\mathsf K\).

Ranked open avenues:
1. One-loop comparison of the so(4,1)/so(4,2) and so(5)/so(6) members at N → ∞ and fixed γ > 0.
2. N → ∞ first in Definition (A) at fixed γ > 0, and whether the conjugate background is a saddle (057 avenue 1).
3. Curved first-order members, with Δ_T from ½𝖱𝒮.
4. Approximate finite-N truncations of so(4,1) that solve the EOM to controlled error.
5. A fluctuation estimate near the bounce, and in the base presentation's Euclidean domain.
6. Anisotropic or non-Lie backgrounds.

### 2.9 Literature

As in r1. The gatekeeper independently confirmed the v2 PDF numbering and the 1709.10480 and 2512.03161 statements.

## Claim classification

| Claim | Class |
|---|---|
| Criterion (13), (16), (17) of 2605.13294 v2; proposed there | input (verified from source) |
| Flat point: no quasi-coherent state; (16) fails; for η the ratio grows like σ⁻² | established (tree level, background Feynman gauge) |
| Gaussian values and ratios g/2σ², 2^{−3/4}g/σ² | established (max over t′ numerical for η) |
| A supplied σ ≫ g^{1/2} is needed; w is a supplied momentum scale | established / input |
| Lemmas (i)–(iii) for \(\mathsf K\) | established |
| E = ±mη, \(\mathsf K\) = m²η⁻¹Hη⁻¹, \(\mathsf K\) = 0 at m = 0 | established (Poisson limit) |
| Lie identity; EOM ⇔ H = cη, γ = 3cη^{c₀c₀} | established |
| (9,1) ⇒ c > 0, W timelike, Lorentzian on m ≠ 0 | conditional (on h₀ under P1∧P2 and on the supplied class) |
| so(6) twin at the same sign γ > 0, Euclidean | established |
| T^a generate so(4,1); a non-compact simple algebra has no non-trivial Hermitian rep; finite-N solutions in the family have positive definite \(\mathsf K\); Lorentzian only for N → ∞ | established |
| Base-presentation average and signature table (c > 0) | established |
| 1709.10480 κ statements; 2512.03161 Euclidean metric | input (verified from source) |
| ρ_M ∝ 1/|m|; exponents of g² | established (uses 2605's definition of g) |
| Semi-classical domain inside the Lorentzian domain (2605 Eq. (100), corrected constant of order g_YM) | conditional |
| Criterion near m → 0, for K and transverse modes, for curved members, at one loop | unresolved |
| Selection of the real form, W or the background; any derived signature or frame | unresolved |

## Proposed changes

### chapters/appH-microscopic-proofs.tex

There is one insertion and nothing is replaced. The anchor and placement are as in r1. The anchor is unique, count 1, at line 1588: `\paragraph{Status.}` CRLF `Remains Assumption~\ref{ass:lorentzian}.`. The block goes immediately before it, followed by one CRLF blank line.

The exact text is `appH_insert.tex` (r2):
- LF: 11102 B, d4d35ace6f76aa370ace725a54bbb23f0e6deb028888dd0c6f694af0198b089b; ASCII, no CR, no tab.
- CRLF: 11122 B, fdff5088e8b01bb03ac91bcb37563b35eb99a594b24a35daed5f5c49dbef3aa2.
- Result appH: 590875 B, sha256 94befe3b6d9f6c01c6a30d88010eebce6cac986938e6e882f5bd06b4397485c6, CRLF 3300, bare LF 0.

The file is authoritative and is not duplicated here. Refs, each to a unique label: sec:status-D, sec:status-F, def:matrix-coords-ext (new in r2, via R1), eq:Smatrix, ass:lorentzian, ass:frame-lock, ass:nondeg, ch:vierbein-emergence. There are no new labels.

### bib/namcg.bib

Append `bib_entries.bib` (r2) after a CRLF blank line. It is 942 B LF, 1fa7f24b…1e6f; 972 B CRLF, 38196621…6eda. The result is 27601 B, sha256 645c93c9bab8486142651b2d8ec0a784431bc248acb815a530bd1747a47d0f67, CRLF 923, with no duplicate keys. The entries are as in r1, except that Steinacker2026Weak now carries:

```bibtex
  note    = {Version 2; the equation numbers cited refer to it},
```

### Stale passages elsewhere

None.

## Verification scripts

- **s1–s4:** unchanged from r1, and their outputs are unchanged.
- **s5_subalgebra_span.py → .out.txt (new):** subalgebra spans and their compactness, for M2.
- **apply_r2_edits.py → .out.txt:** the r1→r2 edits, with hash and uniqueness asserts.
- **apply_check.py → apply_check.txt:** r2 report mode. The baselines match, and refs, labels and cites resolve. The r1 output is kept as apply_check.r1.txt.
- **Scratch build** in scratchpad `build060r2`, outside the repository: pdflatex, bibtex, pdflatex, pdflatex. Result: PASS, **371 pages**, 0 undefined and 0 multiply defined references or citations, bibtex clean, and no overfull boxes in the inserted lines.
- **Earlier scratch directories:** removal of build060 and build2605 was denied in r1. They are left in place, and the new build directory is left as well.

## Decisions Taken

1. R1–R9 are applied verbatim. The single deviation is the R1 old string, corrected to the actual r1 text with the identical substitution.
2. Optional item 10 is adopted, for the reason given above. The Liao2026 suggestion is not adopted, because I have read only its abstract.
3. s5 was added so that M2's factual basis, the subalgebra span and its compactness, can be re-run.
4. The other choices from r1 stand: placement in Problem E, the v2 PDF numbering, and the three verified bib entries.

## Milestone assessment

M2 (bounded no-go, non-stopping). This round rules out three things within the classes of r1 §2.8:
- (a) a semi-classical reading of the flat point without a supplied scale;
- (b) classical selection of the signature of \(\mathsf K\) within the four-generator Lie family with an isotropic mass;
- (c) any finite-N exact Hermitian solution of that family with a Lorentzian \(\mathsf K\). This is the corrected wording: the T^a generate so(4,1), and only compact subalgebras admit finite-N representations.

It is not M1, M3, M4 or M5, and not a breakthrough.

## Status-label recommendation

D and E are unchanged: OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. I recommend no label change.

## Author decision needed

None.

## Remaining open step

As in r1. E needs (a) the target contraction fixed without P1/P2, (b) selection of the real form so(4,1)/so(4,2) over its compact twin, and (c) control of N → ∞ first at fixed γ > 0 and then γ → 0. D1 additionally needs the frame and its non-degeneracy derived, with the bounce m = 0 treated, and a semi-classical regime that does not rest on a supplied scale.

The next step is avenue 1.

## Special instructions for the gatekeeper

- Verify that the r2 insert equals r1 plus exactly the listed replacements: run `apply_r2_edits.py` against the r1 files, or diff them. Check the R1 Sylvester deviation in particular.
- Check that no γ in the insert still denotes the kinetic tensor.
- Re-run s5 to confirm the so(4,1) span, compactness of the so(6) and so(5,1) cases, and the R2 wording.
- bibtex must be run once at integration, because `build_check.py` does not run it.
