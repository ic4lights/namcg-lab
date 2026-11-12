VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/2

## Verdict
The algebra holds up: the fibre formula, weights, zero set, gap, compact exponent, large-label series and the D² identity all re-derive. The insert is not ready, for two reasons. As worded, the local-integrability hypothesis cannot be met by a normal trace on B(M_{k,p}) whenever C5 has continuous spectrum there. And the closing claims at the level of Pf_rel ("no divergence of log Pf_rel", "does not by itself force Pf_rel = 0") go further than the bounded-set, fermionic-term result that is actually proved.

## Source reading
- **Mode:** digest + targeted reads.
- **Digest status:** `make_digest.py --check` printed DIGEST CURRENT. The digest shows head 4c94521, `dirty-chapters: no`, and a clean tree. The working-tree appH matches the baseline: 606731 B, sha256 4808ae9c…30cf.
- **Scan ruling.** No full scan is due, and none was done.
  - 3(a): this is ordinal 62, not a 5th item; the next scan is at 65.
  - 3(b): no milestone verdict is issued.
  - 3(c): the insert adds a new conditional paragraph with a locally defined quantity. It changes no core definition, assumption, scope statement or status passage.
  - 3(d): the digest is current and clean at review time.
  - The researcher's start-of-run `dirty-chapters: yes` came from the accepted 061–063 integrations. They are now committed in 9680d08 with an identical appH hash. The researcher read the affected 061/062 blocks directly, which the 2026-10-15 directive allows. No action is needed.
- **Read in full:**
  - appH: Problem E header and ledger label (L1482–1493); the 059/060 paragraphs (L1575–1607, line-truncated scan plus the paragraphs relied on); the 061 block (L1609–1620) and 062 block (L1622–1631) in full; the anchor at L1633–1634.
  - ch17: L328–345 (D), L394–399 (E), L698–745 (criterion).
  - ch04: L312–336 (`ass:lorentzian`).
  - The whole proposal, the insert, apply_check.py and its output, and build_r1.txt.
- **Not re-read:** `reports/ledger.md` beyond what the proposal cites. There are no earlier rounds.

## Claim under review
- **Claim.** The package defines log Pf_rel = ¼τ[tr₁₆ log(D²−iε) − 16 log(□−iε)] on the so(4,1)⊂so(4,2) doubleton member, with the iε, branch and τ supplied. It then claims:
  - an exact fibre formula;
  - the zero set equals 062's kernel condition;
  - local integrability and the ε→0 limit under a hypothesis on τ;
  - a gap |λ| ≥ c/4 on C5 ≤ −9/4;
  - |Pf_rel| ∝ ε^{K/4} → 0 on the compact members;
  - a list of what is not established.
- **Original target, Problem E:** Lorentzian signature derived from the matrix theory. Appendix H verbatim: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. A scope retaining Assumption~\ref{ass:lorentzian} gives up the claim of emergent or matrix-derived Lorentzian signature." ch17 L395: "OPEN; CRITICAL PATH for the matrix-derived label."
- **D1:** bearing only (ch17 L328: "CRITICAL PATH; OPEN"). No frame claim is made.
- **Critical-path set** (ch17 L700–735): A, B, C, D1, E, F, G-derived, N. H, I and J are optional. No discrepancy with the agenda.

## Checks performed
Direct verification by hand and with my own script, `C:\Users\redgi\AppData\Local\Temp\claude\3ba14ee056ac155d\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\gk064.py`:

- **D² identity.** Γ^aΓ^b ad_a ad_b = η^{ab}ad_a ad_b + ¼[Γ^a,Γ^b]ad_{[T_a,T_b]}. With [T_a,T_b] = −iF_ab, the second term is −(i/4)[Γ^a,Γ^b]ad_{F_ab} = −Σ^ψ_ab[F^ab,·]. Correct.
- **Weights in (4.16).** From iΓ, the fermion factor is exp(¼ Tr log(D²−iε)). The split weights are −½·10 + ¼·16 + 1 = 0, so the relative split is exact. The γ-independence follows from D², □ ∝ c with c > 0 under the principal branch. Correct.
- **Fibre formula.**
  - (σ·J)² + σ·J = J², and 4J_L² = C4 ± 2iP = (k ± ip)² − 1 using C4 = k² − p² − 1 and P = ±kp. So X² + X = (z² − 1)/4, with roots x₁ = (z−1)/2 and x₂ = −(z+1)/2.
  - Lagrange interpolation with tr_{C²}σ·J = 0 gives 2α = ((z+1)/z)f(x₁) + ((z−1)/z)f(x₂).
  - λ₁,₂ = c(A + 1 ∓ z), with A = C5 − k² + p² + 1, gives c(C5 + 2 − k(k±1) + p² ∓ ip). Symbolic check: zero difference.
  - A and X commute because C5 and C4 commute with so(3,1). Correct.
- **k an integer.** −1 ∈ Spin(3,1) is central in the group acting on the irreducible H_n, so it acts by a scalar and trivially in the adjoint action. The same holds for s in the Spin(4,1) principal series. Correct; the insert states this only for k (minor finding 4).
- **Zero set.** At p = 0, 062's B = k² − (C5 + 2 − k²)² = 0 ⇔ C5 = k(k±1) − 2. At k = 0, p ≠ 0, B = −p² − (A+1)² ≠ 0. This matches the fibre zero set exactly.
- **Gap.**
  - min_p |λ/c|² is −R − ¼ (R ≤ −½) or R² (otherwise), with R = C5 + 2 − k(k±1). For integer k, k(k±1) ≥ 0. So C5 ≤ −9/4 ⇒ R ≤ −¼ ⇒ |λ/c| ≥ ¼. My grid scan gives a minimum of exactly 0.25.
  - For −9/4 < C5 < −2 the bound c|C5+2| is correct.
  - At k = 0 the spherical form λ₁ = c[(p − i/2)² − ν²] is correct.
- **Casimir normalisation.** The infinitesimal character with ρ = (3/2, ½) reproduces 061's m1(m1+3) + m2(m2+1) and gives s(s+1) − 9/4 − ν². s4 confirms the sign on the hyperboloid with the same generators: 4 on the vector, −(9/4 + ν²) on horospherical waves, and C4 = −(1 + p²) at k = 0.
- **Compact exponent.** The top component (m1,m2) coupled to spin j_L + ½ has dimension (m1+m2+2)(m1−m2+1). The (m1,−m2) partner gives the same count on the other chirality, and the cross case does not vanish (difference 2m2). That is 8 per (m1,m2) on the 16 components. Σ = (4/3)n(n+4)(n²+4n+7) for n ≤ 7 (my script). □ = c(C5−C4) ≥ c(m1+m2) ≥ c on traceless matrices. So |Pf_rel| ∝ ε^{K/4}, which is 20 and 76.
- **Large-label series.** The t¹ coefficient is 0 and the t² coefficient is 1 − z². The chirality sum is −2C4. My symbolic series also gives t³ = (4/3)(z²−1).
- **Branch dependence.** Re(w log λ) shifts by −2π Im w, with Im(1/z) = −p/|z|². Correct.
- **Scripts.** I re-ran s1–s4 to the scratchpad; all exit 0 and all outputs are byte-identical to the submitted .out.txt. s4 also rewrote its own git-ignored .out.txt in the proposal folder, with identical content. s2 confirms the full chiral spectra for n = 1, 2 (deviation ≤ 6.2e−14) and the slopes 20 and 76. Symbolic and numerical output is a check, not a proof.
- **apply_check** (re-run, output to the scratchpad only):
  - baseline 606731 B, 4808ae9c…30cf;
  - anchor found once, at L1633;
  - insert 6728 B, 980cb390…e27d;
  - result 613489 B, sha256 a0e4ff965eab20014968022aee823b06e573162a92c225b0345bb2257d60ac98, 3353 CRLF, 0 bare LF;
  - `ass:lorentzian` has 1 label occurrence and Steinacker2023 has 1 bib entry; no new labels; no process language.
  - All match the claim.
- **Literature.** I fetched 2303.08012v1 and read printed pp. 14–15 from the page images.
  - Eq. (4.15), S → S + iε Tr Σ(T^a)², regulates the bosonic matrices only.
  - Eq. (4.16) has the logs with coefficients 1, −½ and −2, each with −iε.
  - Eq. (4.17) gives F^{ab} = i[T^a,T^b] and Σ^(ψ)_ab = (i/4)[Γ_a,Γ_b].
  - The text below (4.17) states that the leading terms cancel by maximal supersymmetry.
  - So the insert's attribution, and its statement that the fermion iε is a prescription, are supported.
  - Fioresi–Yuncken Thm 7.1 and Martin-Dussaud Eq. (297) are relied on via 062 and were not re-fetched. The SL(2,C) Plancherel density ∝ k² + p² is standard.
- **Build.** I did not re-run it; I relied on build_r1.txt (PASS, 378 pp, 0 undefined). The revised text will need a rebuild.
- **Checked by eye:** LaTeX syntax; distinctness of the closing sentence from 054–062; no label change; no non-zero-density, selection or one-loop-separation claim.

## Findings

**1. Severity: major.**
- **Location:** insert ¶1, "with \(\omega_{k,p}\) a normal semifinite trace on the operators on \(\mathcal M_{k,p}\)", together with the hypothesis in ¶3, "Suppose \(\omega_{k,p}\) gives finite weight to the spectral projections of \(C_5\) for bounded intervals".
- **Finding:** As written, the hypothesis can only hold in a special case. A normal semifinite trace on B(M_{k,p}) is a multiple of Tr. Tr(E_{C5}(I)) is the rank of the projection. That rank is finite only if C5 has finitely many eigenvalues of finite multiplicity in I. If HS(H_n)|Spin(4,1) contains principal series continuously in ν, C5 has continuous spectrum on M_{k,p}, and the hypothesis fails for every non-zero such ω. The proposal's own remark (HS(H₀) ⊂ ∞λ_{Spin(4,1)}) points to exactly that case, and so do the gap paragraph's continuous principal series. The conditional local-integrability result would then be vacuous.
- **Reason:** A conditional result must be stated with a hypothesis that is not secretly inconsistent with the object it describes.
- **Required action:** Define ω_{k,p} as a weight (measure) on the spectrum of C5. Only this restriction enters, because the spinor-traced integrand is a function of (C5, k, p). Also state when the canonical trace qualifies. Replacement text is given below.

**2. Severity: major.**
- **Location:** insert ¶3 ("By dominated convergence … and the zeros produce no divergence of \(\log\operatorname{Pf}_{\mathrm{rel}}\)") and ¶8 ("does not by itself force \(\operatorname{Pf}_{\mathrm{rel}}=0\)").
- **Finding:** Both statements are overstated at the level of Pf_rel.
- **Reason, part (a):** What is proved concerns the fermionic term on bounded label sets. The zero set {p = 0, C5 = k(k±1) − 2} has infinitely many components in k. Whether their contributions are summable is exactly the open condition in ¶5. If it fails, the zero set could still force Pf_rel = 0. So "does not by itself force Pf_rel = 0" is not established globally.
- **Reason, part (b):** The reference term is not controlled by the stated hypothesis. log(□ − iε) is singular on A = C5 − k² + p² + 1 = 0. Finite weight on bounded C5 windows allows ω_{k,p} to charge that curve, for instance an atom at C5 = k² − 1 − p² for p in an interval. log ε then appears on a set of positive measure, and the reference term diverges as ε → 0. The fermionic term escapes this only because Im λ = ∓cp does not depend on C5.
- **Reason, part (c), the proof step:** The stated bound |λ − iε| ≥ |cp ± ε| is not an ε-independent dominator: sup_ε |log|cp+ε|| = ∞ for p < 0. The bound does give uniform L¹ and L² control, so the limit holds by Vitali's theorem, not by dominated convergence.
- **Required action:** Restrict the claims to the fermionic term on bounded label sets. Add the extra condition under which the reference term converges. Name the right convergence theorem. Replacement text is given below.

**3. Severity: minor.**
- **Location:** insert ¶5, "so the trace at fixed \(C_5\) diverges linearly in a cut-off on \(p\)".
- **Finding:** This holds only if ω_{k,p} gives that value of C5 a weight bounded below at large p. That depends on τ, which is supplied. The asymptotic constant also follows analytically from the second-order term (−2C4/A² times k² + p² → 2), not only numerically.
- **Required action:** Add the condition (replacement text below).

**4. Severity: minor.**
- **Location:** insert ¶4, "On the principal series \((s,\nu)\) … zeros therefore need \(s\ge1\)".
- **Finding:** This needs s to be an integer. If s = ½ were present, s(s+1) = ¾ ≥ ¼ + ν² would be possible. s is an integer for the same reason as k, but the insert does not say so.
- **Required action:** Add the clause (replacement text below).

**5. Severity: minor; proposal text only, not in the insert.**
- **Location:** proposal Result 2, "yes, 0 is in the spectrum (for C5 ≥ −2)".
- **Finding:** Unsupported. It needs the C5 spectrum on M_{k,p} near p = 0 to reach k(k±1) − 2, and the Spin(4,1) decomposition is not computed. The insert correctly does not assert it.
- **Required action:** None for the insert. Do not carry this sentence into later packages as established.

**Optional, not required.** In ¶1, "since the centre acts trivially in the adjoint action" could read "since \(-1\in\mathrm{Spin}(3,1)\) is central in the group acting on the irreducible \(\mathcal H_n\), acts there by a scalar and hence trivially in the adjoint action".

## Scope of what is established
- **Established (exact algebra, given 062's class and decomposition; n > 0 conditional on the ladder identification):**
  - D² = □ − Σ^ψ F;
  - the exact relative split and its γ-independence;
  - the fibre eigenvalues and weights;
  - the zero set equals 062's kernel condition;
  - the gap |λ| ≥ c/4 on C5 ≤ −9/4, and c|C5+2| on (−9/4, −2);
  - C5 = s(s+1) − 9/4 − ν² on the principal series;
  - |Pf_rel| ∝ ε^{K/4} on the compact members;
  - the large-label second-order coefficient −2C4/A²;
  - branch dependence of the modulus.
- **Conditional** (on a supplied τ, the iε prescription and the principal branch, with τ corrected as in finding 1): local integrability of the fermionic term and its ε → 0 limit on bounded label sets.
- **Open:**
  - the reference term under the bare hypothesis;
  - summability over k;
  - UV / large labels;
  - a per-unit-volume trace at given time;
  - a non-zero value;
  - combination with bosons and ghosts at O(γ);
  - signature.
- **Classification:** PROGRAMME-CONDITIONAL. Problem E stays OPEN, CRITICAL PATH for the matrix-derived label, PROGRAMME-CONDITIONAL. D1 is untouched and OPEN. No label change.
- **Open avenues, ranked** (all within scope; spacetime stays emergent):
  1. Compute HS(H_n)|Spin(4,1) at least for n = 0, i.e. whether C5 has continuous spectrum on M_{k,p}. This decides which τ is natural (finding 1) and whether 0 is in the spectrum.
  2. Build a per-unit-volume trace at given time, using the branching kernel for the spherical sector via the H⁴ radial ODE.
  3. Summability over k near the zeros, i.e. the higher-spin content.
  4. Add the bosons and ghosts at O(γ) with a stated cut-off. 061 shows this is regulator-dependent, so the cut-off must be derived, not chosen.
  5. A branch-independent determinant (Fuglede–Kadison) and its comparison with (4.16).

  The researcher's advisory that the E thread is at diminishing returns against ch17 L718–719 is reasonable. Avenue 1 is the one item likely to change a conclusion rather than refine it.
- **Milestone:** none. These are routine conditional sharpenings, not a breakthrough, a no-go or a prior-claim error.

## Recommended disposition
Revise. Apply the replacement texts below, rebuild, and resubmit as r2 with a fresh apply_check (new size and hash).

## Corrected snippet
No new physics is needed. The only extra assumption, marked as such in 2(b), is the bounded-density condition on ω for the reference term.

1. In ¶1, replace
`with \(\omega_{k,p}\) a normal semifinite trace on the operators on \(\mathcal M_{k,p}\), where \(C_5\) acts.`
with
`with \(\omega_{k,p}\) a normal semifinite weight on the von Neumann algebra generated by \(C_5\), which acts on \(\mathcal M_{k,p}\), that is, a measure on the spectrum of \(C_5\) there; only this restriction enters below. The trace of the operators on \(\mathcal M_{k,p}\) gives a spectral projection of \(C_5\) its rank, which is finite on an interval only if \(C_5\) has there finitely many eigenvalues of finite multiplicity.`

2. In ¶3, make two replacements.

   (a) Replace
   `Then \(\log|\lambda_i-\mathrm i\epsilon|\) is integrable on every bounded set of labels, uniformly in \(\epsilon\). By dominated convergence the fermionic term then has its limit \(\epsilon\to0\) there, and the zeros produce no divergence of \(\log\operatorname{Pf}_{\mathrm{rel}}\).`
   with
   `Then \(\log|\lambda_i-\mathrm i\epsilon|\) and its square are integrable on every bounded set of labels, uniformly in \(\epsilon\), and the arguments are bounded. By uniform integrability (Vitali's theorem) the fermionic term then has its limit \(\epsilon\to0\) there, and its zeros produce no divergence on such a set.`

   (b) Then add, as the next sentences:
   `The reference term has its limit there by dominated convergence if, in addition, \(\omega_{k,p}\) has a density in \(C_5\) bounded locally uniformly, since \(|\Box-\mathrm i\epsilon|\ge|\Box|\); under the first condition alone it is not controlled, since \(\Box=c(C_5-k^2+p^2+1)\) vanishes on a set that the weights may charge.`
   (Extra assumption: the bounded density in C5, stated explicitly.)

3. In ¶4, replace
`On the principal series \((s,\nu)\), where`
with
`On the principal series \((s,\nu)\), with \(s\) an integer for the same reason as \(k\), where`

4. In ¶5, replace
`its density times the Plancherel density tends to a constant as \(p\to\infty\) (numerical), so the trace at fixed \(C_5\) diverges linearly in a cut-off on \(p\).`
with
`its density times the Plancherel density tends to a constant as \(p\to\infty\), by the second order above, so the trace at fixed \(C_5\) diverges linearly in a cut-off on \(p\) wherever \(\omega_{k,p}\) gives that value of \(C_5\) a weight bounded below at large \(p\).`

5. In ¶8, replace
`What is shown is that the zero set of the doubleton member, unlike the zero modes of the compact members, does not by itself force \(\operatorname{Pf}_{\mathrm{rel}}=0\).`
with
`What is shown is that, under the conditions above and on every bounded set of labels, the zeros of the doubleton member, unlike the zero modes of the compact members, give a finite contribution to the fermionic term; whether these contributions are summable over \(k\) is the open condition stated above.`

Relevant files:
- C:\Users\redgi\Projects\namcg-lab\proposals\064-relative-pfaffian-density\appH_insert.tex
- C:\Users\redgi\Projects\namcg-lab\proposals\064-relative-pfaffian-density\proposal-r1.md
- C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex (L1609–1634)
- C:\Users\redgi\AppData\Local\Temp\claude\3ba14ee056ac155d\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\gk064.py

VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/2
