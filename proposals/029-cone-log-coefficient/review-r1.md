VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/2

## Verdict
The central derivation and the assembly check out as a conditional result for the fixed-state replica. The LaTeX needs revisions before integration:
- the spin-term sign convention contradicts the proposal's own channel assignment;
- the mismatch sentence is not scoped against the smooth replica and the state-selection question;
- edge modes and contacts are not named as the place where a cancellation could occur;
- the notation clashes with the 024 and 026 blocks, and some symbols are undefined.

## Source reading
Digest and targeted reads. `make_digest --check` printed DIGEST STALE, which is expected with a dirty `appH`. I read in full:
- the whole of `sec:status-B` text in `appH` (lines 36-236, with 181-237 in full, covering the 019, 021, 024 and 026 paragraphs);
- the Problem B ledger label and the Chapter 17 Problem B paragraph (lines 121-135);
- `proposal-r1.md`, `appH_insert.tex`, and all of `flat_landau_ab.py`, `assemble_check.py` and `a_side_sd.py`;
- the SME scout R-B2 text and the ledger tail.

I did not perform a full scan: ordinal 26 or 27 is not a 5th-integration item, and the proposal changes no definition, scope or status passage. I read the affected passages directly, as `CLAUDE.md` 3(d) requires.

Literature:
- I extracted Solodukhin 1104.3712 locally with `pdftotext`. Eq. (70) is legible with the Greek letters lost.
- Eq. (275) of the same text, quoting Duff, gives A = (n0 + 11 n_{1/2} + 62 n1)/360 and B = (n0 + 6 n_{1/2} + 12 n1 ...)/120.
- Eq. (276) gives `a_A ∝ R_Σ` and `a_B ∝ −W`.
- Solodukhin2011 exists in the bib with the correct DOI and arXiv ID. No new bib entries.
- I did not open Fursaev-Miele or Bianchi et al. The proposal uses neither quantitatively.

## Claim under review
Conditional structural result for Problem B (with A and F): the A-side logarithmic coefficient at (N_s, n_D) = (6, 2) for the fixed-state replica. On the rotation-invariant self-dual example, S = R_Σ/(12π), against the T-side 0 of 026.

Current Appendix H ledger label for B, verbatim: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived." Chapter 17: "CRITICAL PATH; OPEN." Critical set A, B, C, D1, E, F, G-derived, N. A and F are touched only through dependencies. No label change is proposed.

## Checks performed
1. **Fixed-state replica as a Z_n sum (point 1).**
   - The replica operator is the lift of one operator from M to the n-fold branched cover M_n.
   - Deck-group characters give single-sheet problems with twist e^{2πik/n}. This is the standard orbifold decomposition and is exact for integer n.
   - The sums are polynomial in k/n, so they continue analytically in n (Bernoulli power sums; Σ a_k² = (n²−1)/(12n)). The continuation is the polynomial one, and uniqueness is not proved. The LaTeX does not claim it.
   - This does not conflict with 024. The |n−1|/(2n) non-analytic index belongs to the singular-ρ cone, where ln ρ = (n−1) ln|z| carries flux through Σ. The fixed-state replica has ρ regular, as 021 and 024 define it (line 200: "ρ regular, cone on G"). These are different replicas, and the 024 text already says so.
   - Compatible with merged 019 and 024. The 019 statement (less singular extension gives analytic Σa_k²) is reproduced.
2. **Ω term (point 2).** Re-run: `flat_landau_ab.py` reproduces C₁ = a(a−1)/2 and linear coefficient −B₃(a)/3. I also re-derived `Dreg` by hand from the tower sums.
   - My sum over m differs from the script's `Dreg` by exactly +a e^{−ε}/(1−e^{−2ε}). This is the extra-flux state count, and it cancels the spurious 1/ε pole (a/2ε against −a/2ε). The shift is therefore forced, not ad hoc.
   - Σ_k B₃(k/n) = 0 follows from the multiplication theorem at x = 0.
   - Dirac sign: the script's `tot` line only checks arithmetic (Σ_k σ(−a|a|) = −S₂ for N = 2..5). It does not derive which σ is attractive. I derived the pairing independently.
     - For the pair (a, −a), the regular terms ∓B₃/3·B_σ cancel because the same B_σ appears for every twist.
     - The flagged terms give −a²(γ¹²Ω₁₂) per flagged component, expressed convention-free through the Pauli term γ¹²Ω₁₂ of (γD)². The total is −(S₂/2) tr(γ¹²Ω₁₂), with dS₂/dn = 1/6.
   - Check against the E-weight. The per-component tip is S₂/2 against the scalar ΣC = −S₂, a ratio of −½, so with Dirac weight −1 the E contribution is −E/(48π). This matches `ΔS_D`, and the Ω term enters with the same prefactor. The Levi-Civita subtraction is consistent: tr E_LC = R and T_LC = −2R₁₂₁₂ = −R_ijij, so ΔS_D vanishes for Levi-Civita.
   - **Sign-convention defect.** The text says "(γD)² = D² − σ₃F₁₂" and "spin term −σ₃·2πa δ of (γD)²", but also "attractive channel σ₃a > 0". With the l = m − a convention (D = ∂ − iA), σ₃ = −iγ¹², and Ω = [D₁,D₂] = −iF, one gets (γD)² ∋ +σ₃F, so the delta is +σ₃·2πa δ in (γD)². The final formula −½S₂ tr(γ¹²Ω₁₂) is convention-free once tied to the Pauli term γ¹²Ω₁₂. The stated intermediate sign is wrong or unspecified. See Finding 2.
3. **Eq. (70) and the Dirac input (point 3).**
   - Eq. (70) in the extracted text has the structure a₂^Σ = (π/3)(1−α)(1+α)/α ∫(R/6 + X) − (π/180)(1−α)(1+α)(1+α²)/α³ ∫(R_ii − 2R_ijij), where X is Solodukhin's E (his operator is −(∇² + X)). This matches c_B and d_B. The normalisation of the c_B term is not independently tested by the sphere check, which only tests d_B (the sphere gives −1/90 = −4a). It rests on Eq. (70) itself.
   - The Dirac value a = 11/360 appears in Solodukhin Eq. (275) (Duff) as the coefficient 11 against 1 for a scalar. The identification of n_{1/2} with a Dirac field is not stated in the review text. I checked it by N = 4 SYM: (6 + 4·11/2 + 62)/360 = 1/4 = (6 + 12 + 12)/120. This is a standard value, not re-derived, and it must be labelled an input and cited.
   - From Eq. (276), S_log = −(a/2π)R_Σ + (c/2π)W for totally geodesic Σ. With R_ii − 2R_ijij = R_Σ − 3W, the scalar Q term matches a : c = 1 : 3.
   - I rederived the assembly by hand. 8 scalar-type components (6 scalars, 4 vector, −2 ghost) give 8R/6 − (8e − X′) − (4/15)(R_Σ − 3W). Two Dirac fields give −(11/15)R_Σ + (6/5)W for the Levi-Civita part and R − tr E_f − T − R_ijij for the torsion correction. The sum is 24πS = (4/3)R + 2R_ii − 2R_ijij + 2W − 12e + (3/2)X′ − T, as stated. `assemble_check.py` reproduces this symbolically.
4. **Self-dual example (point 4).**
   - I re-ran `a_side_sd.py`. At all three points e = R/6, W = 0, X′ = −2R, T = −(5/3)R, R_ii = (4/3)R, and R_ijij = R. Hence (3/2)X′ − T = −(4/3)R = 2R_Σ with R_Σ = −(2/3)R.
   - I checked R_Σ independently without the script's Gauss relation. On Σ the metric is b₃²δ with b₃ = 1 + x₃² − x₄², giving R_Σ = 8(x₃² + x₄²)/b₃⁴. At (1/3, 1/5) this is 3098250000/3373402561, matching `Rsig` exactly.
   - The ratios are pointwise constants, so the identity is plausibly provable, but only three points of one example are tested. The proposal says "observed, not proved". The LaTeX says "not proved". That is adequate.
5. **Anchor.** The substring "no logarithmic coefficient of the cone (area) side" occurs exactly once (the end of the 026 paragraph, line 236). `\section{Problem C: conformal mode and Cassini}` follows at line 238. The anchor is unique and correct.
6. **Other checks.** Spacetime stays emergent: G, ρ and b are built from Θ and no metric is made fundamental. No label touched. Cited bib keys exist.

## Findings

**1. Major. Location: LaTeX paragraph 1, last four sentences ("The two sides therefore differ…").**
- Finding: the mismatch is stated without the context that the first-order smooth replica gives 0 = 0, and that 024 records which replica the matrix state selects as undetermined. The reader could take this as a mismatch for the matrix model. The block also never names edge modes, contacts and finite terms as the place where a cancellation could occur (the proposal itself ranks this as avenue 3). Paragraph 2 lists edge modes only among things "not treated".
- Required action: add one sentence at the end of paragraph 1, for example: "The first-order smooth replica of the preceding paragraphs gives zero on both sides, and which replica the matrix state selects is not derived here; contact and edge-mode terms of the connection and Dirac sectors, not included, shift the coefficient of R_Σ and could cancel the difference." Say explicitly that the statement is about the fixed-state replica only, and make clear that "differ at logarithmic order" is a statement about coefficients, not about G_eff.

**2. Major. Location: LaTeX, "spin term −σ₃ 2πa δ_Σ of (γ^μD_μ)²" and "Ω₁₂ the bundle curvature".**
- Finding: the sign and convention are inconsistent with the attractive-channel assignment (see Check 2). The load-bearing sign of the Ω term depends on this.
- Required action: state the convention, or use the convention-free form: "the spin term γ¹²Ω₁₂ of (γ^μD_μ)², with Ω₁₂ = [D₁,D₂], whose part supported on Σ is attractive in the component where it is positive". Replace "−σ₃ 2πa δ" accordingly (extra assumption: D = ∂ − iA, σ₃ = −iγ¹²). Define T with the same Ω.

**3. Minor. Location: the symbols 𝒯 and 𝒮.**
- Finding: 𝒯 is already used in the 024 block (line 213) for the teleparallel torsion scalar, and 𝒮_4 exists in the 026 block. The new 𝒯 = tr(γ¹²Ω^f₁₂) and 𝒮 clash with these.
- Required action: rename both, for example τ for the first and σ_log for the second, and use the new names in the displayed formula and the text.

**4. Minor. Location: LaTeX.**
- Finding: R_ii, R_ijij and R_Σ are undefined in the manuscript before this block (R_ijij appears only inside the new block). W = W_ijij and X′ are defined inline, which is fine.
- Required action: define R_ii = R_{μν}n^μ_i n^ν_i summed over i, R_ijij = R_{μνρσ}n^μ_i n^ν_j n^ρ_i n^σ_j summed over i and j, and R_Σ as the intrinsic scalar curvature of Σ. For totally geodesic Σ, R_Σ = R − 2R_ii + R_ijij.

**5. Minor. Location: LaTeX paragraph 2.**
- Finding: the Dirac input a = 11/360 is stated without a source. It must be labelled an input, not taken from tool summaries.
- Required action: cite "the value a = 11/360 of the Dirac field (Eq. (275) of Solodukhin2011, after Duff), not re-derived here". Do the same for Eq. (70) (already cited).

**6. Minor. Location: closing sentence.**
- Finding: "Problems B, C, D, F and G remain open" is repeated verbatim after the immediately preceding paragraph's identical closer. `CLAUDE.md` asks that the fixed list not be repeated and that the current criterion be used.
- Required action: end with a single scoped status sentence, for example "Problem B remains open and PROGRAMME-CONDITIONAL."

**7. Minor. Location: `flat_landau_ab.py`, last print line.**
- Finding: the third tuple entry prints −S₂/2, which is mislabelled against the printed `tot` = −S₂. Also, the script does not derive the attractive-channel assignment (see Check 2).
- Required action: correct the label, or note that this assignment is an input checked by hand.

## Scope of what is established
- **Established.**
  - The Z_n flavour-vortex decomposition for the fixed-state replica (exact for integer n).
  - The flat-model constants C₁ and −B₃/3, the flagged-channel shifts, and Σa_k².
  - The Ω-term weight −½S₂ tr(γ¹²Ω₁₂), via a convention-free argument.
  - The symbolic assembly of 24πS given Eq. (70) and a = 11/360.
- **Conditional.** The formula holds only under these hypotheses:
  - the fixed-state replica with ρ regular;
  - the less singular Dirac extension;
  - antiperiodic polar-frame gluing;
  - totally geodesic Σ;
  - one loop, α = 1, Yukawas dropped;
  - one common proper-time limit;
  - the two literature inputs;
  - first order in n−1 for the Dirac geometric part.

  The result S = R_Σ/(12π) rests on a numerical identity checked at three points of one example. The "smooth replica = 0" statement rests on S₄ ≥ 0, from 026.
- **Not established.**
  - The matrix state, the tip domain and the extension.
  - Edge modes, contacts and finite terms.
  - Any statement about G_eff, or about the full G_T versus G_A comparison.
  - Problem B stays OPEN, CRITICAL PATH and PROGRAMME-CONDITIONAL. No label change is proposed.

**Effect on merged scope statements (015-026).** None is falsified; no PRIOR-CLAIM-ERROR.
- 026's closing sentence ("compute no logarithmic coefficient of the cone side… no comparison of G_T with G_A at logarithmic order follows") stays true of that block.
- 024's "which replica the state selects is undetermined" is unchanged and should be cross-referenced by the new hedge in Finding 1.

**Open avenues after this conditional mismatch, ranked by promise for the infrared or full-GR derivation:**
1. Edge-mode and contact terms (H4): the Kabat vector contact (−1 in the 024 units), the Dirac edge modes, and the Herzog-Nishioka-type terms. Compute whether they shift the R_Σ coefficient enough to cancel 2R_Σ. This is the most likely site for G_A = G_T.
2. Prove (3/2)X′ − T = 2R_Σ on self-dual backgrounds (Weitzenböck identity), and evaluate on the non-BPS d(hΛ³) family (needs c = 1/20 and W ≠ 0).
3. The log analogue of the intermediate-flux replica (c_A(f)), and the smooth replica's own log coefficient beyond the S₄ ≥ 0 argument.
4. An independent spindle-spectra check of the Dirac geometric part and of the sign of the Ω term (S²_n × R², branched S⁴).
5. Relax H1: non-totally-geodesic Σ, with extrinsic-curvature terms.
6. The rotated-gluing vector branch of 024 (non-analytic at n = 1).
7. The a₃ Kaluza-Klein route of 026.

## Recommended disposition
Revise and re-submit. The paragraph is a coherent single package (reduction, Ω term, assembly, example). Fixing Findings 1-2 is the substance. Findings 3-7 are cosmetic, and I would accept them in the revised LaTeX without another derivation round. I flag no SME-CONSULT; the two inputs are checked as far as I can without originating research.

## Corrected snippet
Only Finding 1 and the Finding 6 closer need new wording. Neither adds physics.

Append to paragraph 1, after "…on these backgrounds.":

> The first-order smooth replica of the preceding paragraphs gives zero on both sides, and which replica the matrix state selects is not derived here. Contact and edge-mode terms of the connection and Dirac sectors, which are not included, shift the coefficient of \(R_\Sigma\) and could cancel the difference.

Replace the closing "Problems~B, C, D, F and~G remain open." with:

> Problem~B remains open and PROGRAMME-CONDITIONAL.

Finding 2 replacement (extra assumption: \(D=\partial-\mathrm iA\), \(\sigma_3=-\mathrm i\gamma^{12}\), \(\Omega_{12}=[D_1,D_2]\)):

> For a Dirac field the common phase is accompanied by the spin term \(\gamma^{12}\Omega_{12}\) of \((\gamma^\mu D_\mu)^2\), whose part supported on \(\Sigma\) is attractive in the component where it is positive; …

File paths:
- `C:\Users\redgi\Projects\namcg-lab\proposals\029-cone-log-coefficient\proposal-r1.md`
- `C:\Users\redgi\Projects\namcg-lab\proposals\029-cone-log-coefficient\appH_insert.tex`
- `C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex` (anchor line 236)
