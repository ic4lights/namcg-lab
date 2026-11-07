VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M2 | FLAGS: none | PROGRESS: first | OPEN: 0/0

## Verdict
I re-derived statements (i)-(iv) and they hold within their stated hypotheses. Four minor corrections are still required before integration. One is a missing justification in (iv): the u-independence of I^{(u)}[1] for 1<u<2. The other three are wording fixes: the closing sentences repeat the 053 block, the u=1 sentence can be read as a limit, and k^mu is never defined.

## Source reading
- **Mode: digest + targeted reads.** This is not a full scan.
- **Digest.** `make_digest.py --check` printed `DIGEST CURRENT`. The digest has `dirty-chapters: no`, head a31435a, and the appH hash 7a75554ef8cb. `git diff --stat HEAD -- chapters bib` is empty. `sha256sum` of the working appH is 7a75554e…6aaa, 3203 lines, matching the proposal and apply_check.
- **Scan ruling.** No full scan is required now, for four reasons:
  - this would be integration ordinal 52, not a 5th item;
  - the digest is current and the chapters are clean;
  - the insert adds one conditional block and changes no definition, assumption, scope sentence or status passage;
  - no milestone digest is triggered by an AWRR verdict.
- **Next round.** If r2 is a plain ACCEPT carrying M2, CLAUDE.md 3(b) requires the r2 gatekeeper to do a full scan before issuing it.
- **Read in full:**
  - `chapters/appH-microscopic-proofs.tex` L1482-1515: all of Problem E, i.e. the ledger label, the entire 053 block L1495-1510 and the Status paragraph L1512-1513;
  - appH L1478 (the 052 paragraph, as re-scoped by 053);
  - `chapters/ch17-agenda.tex` L390-400 (Problem E) and the grep of criterion L718-719;
  - the label `ass:lorentzian` (ch04 L322, defined once);
  - `MILESTONE.md`;
  - the tail of `reports/ledger.md`, including the 053 entry;
  - the proposal, the insert, and every script output in the folder.
- Unreadable files: none.

## Claim under review
The package extends 053's Definition (A) limit (fixed N, eps→0 first, gamma=0) to Fourier observables, i.e. products of traces of single-index exponentials e^{iκA_μ}. It makes five claims:
- **Step 0:** exact Stokes at fixed eps for u<2/3, any N.
- **(i):** for κ on the rays that make every factor unitary on R_u, lim I_eps[O] equals the eps=0 integral on R_u. Proved at N=2; conditional for N≥3.
- **(ii):** for real κ≠0, the "Euclidean value at phases" integrand for Tr e^{iκA_0} is not integrable at N=2.
- **(iii):** the Gaussian-smeared limit is a line integral of J, for timelike and spacelike axis momenta.
- **(iv), at N=2:**
  - J is holomorphic on 0<arg κ<3π/4, with |J| ≤ 2[sin(4 arg κ/3)]^{-27/2};
  - F_E(t)=J(√t e^{3πi/8}) is holomorphic on |arg t|<3π/4 and equals the Euclidean characteristic function for t>0;
  - the spacelike smeared limit is ∫_R φ F_E(e^{iπ/4}κ²);
  - real timelike κ lies on the edge ray arg t=−3π/4, reached from k·k−i0.

**Original target:** derive Lorentzian signature rather than retain it (Assumption ass:lorentzian).

**Appendix H, verbatim:** "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. A scope retaining Assumption~\ref{ass:lorentzian} gives up the claim of emergent or matrix-derived Lorentzian signature." The Status paragraph reads "Remains Assumption~\ref{ass:lorentzian}."

**Chapter 17, verbatim:** "OPEN; CRITICAL PATH for the matrix-derived label." The criterion item reads "Problem~E: Lorentzian signature is derived rather than retained (Assumption~\ref{ass:lorentzian})." The two sources do not conflict. The current critical-path set is A, B, C, D1, E, F, G-derived, N. No label change is proposed.

## Checks performed
Each check below was verified directly by hand unless stated otherwise.

**Step 0 (Stokes at fixed eps).**
- On every R_{u'} with u'≤u, ||e^{iκA_μ}|| ≤ e^{|κ| ||Ã_μ||}.
- The ball-boundary term is poly(R)·e^{cR}·e^{−eps cos(3πu/4)R²} → 0 for u<2/3, and Re iS_b ≤ 0 along the homotopy.
- Holds for any N, since Pf is polynomial.

**(i) Unitary phases and the limit.**
- κA_0 = K e^{3πiu/8}e^{−3πiu/8}Ã_0 = KÃ_0, and κA_j = KÃ_j, so every factor is unitary and |O| ≤ N^{n_tr}.
- The regulator modulus is ≤ 1 for u<2/3. Domination by 053's bound with k=0, then dominated convergence.
- The denominator follows from 053's lim I_eps[1].

**(ii) Real momenta.**
- At N=2, Tr e^{izÃ_0} = 2cos(z|ã|/2), and |cos(p+iq)| ≥ |sinh q|. For z=κe^{−3πi/8}, |Im z| = |κ| sin(3π/8).
- On R_1, G = e^{iπ/4}(B̃ᵀB̃ − e^{−iπ}ããᵀ) = e^{iπ/4}G̃. So |Pf| = |c_P|(det G̃)⁴ exactly, and the Euclidean modulus equals the bound integrand at u=1 with c=1.
- **Reading of "converges exactly for k<14": confirmed as "if and only if".**
  - I re-derived the power counting along the flat direction myself, using singular values s1=R ≫ s2, s3 ~ t/R of the 10×3 matrix.
  - The measure is ∏s_i^7 ∏|s_i²−s_j²|; (det G̃)⁴ = ∏s_i^8; S_E ≈ R²(s2²+s3²).
  - Collecting powers gives R^{k−15} dR: convergent iff k<14, logarithmically divergent at k=14.
  - This matches 053's numerics (log growth at 2n=14) and the 053 ledger entry "k < 14 sharp for the modulus".
- Since sinh x ≥ x^14/14! for x ≥ 0, and by the SO(10) argument, the integral of sinh(c|ã_0|) against the weight diverges. Statement (ii) is correct as worded (absolute non-integrability, N=2).

**(iii) Smearing.**
- The Fourier identity is correct, and exact_checks (1) re-run gives the same output.
- The eigenvalue bound: Re(iκ0e^{−iα}λ − ℓ²e^{−2iα}λ²/4) = κ0 λ sin α − ℓ² cos 2α λ²/4, with maximum κ0² sin²α/(ℓ² cos 2α).
- Turning the κ-line: |φ| decays with cos 2α' ≥ cos 2α > 0 for α<π/4, against trace growth N e^{|κ|·||Ã_0||}.
- Fubini on R_u × line. θ = 3πu/8 ∈ (0, π/4).
- Spacelike case: β = πu/8 ∈ (0, π/12) and cos 2β > 0.

**(iv) Holomorphy at N=2.**
- *Damping region.* I re-derived Re iS_b for independent phases A_0 = e^{−iα}Ã_0, A_i = e^{iβ}Ã_i: Re iS_b = −(1/4g²)[sin 4β X + 2 sin(2α−2β) Y]. This matches exact_checks (7). Damping holds iff 0<β<π/4 and 0<α−β<π/2, and R_u satisfies both for 0<u<2.
- *Cauchy-Binet.* det G = Σ c_μc_νc_ρ det[a_μ a_ν a_ρ]² with |c|=1, so |det G| ≤ det G̃ for any phases.
- *Scaling exponent.* 30 real dimensions plus degree 24 of (det G̃)⁴ give s^{−54/4} = s^{−27/2}, and πu/2 = 4 arg κ/3.
- *Evenness.* G and aᵀ(trW−W)a depend on a only through aaᵀ.
  - In polar coordinates with z = e^{−iφ}r, the measure d³a becomes z² dz dn.
  - The substitution (r,n) → (−r,−n) converts 2cos into a single exponential along full lines.
- *The two half-lines.*
  - r>0 at phase α*−δ, r<0 at phase α*+δ. For |arg κ − α*| < δ/2, Im(κz) ≥ |κ||r| sin(δ/2) on both halves.
  - With β* = α*/3: φ± − β* = 2α*/3 ∓ δ ∈ (0, π/2) and β* ∈ (0, π/4), so c = min(sin 4β*, sin(2φ±−2β*)) > 0.
  - Domination is uniform near κ*, and Morera with Fubini gives holomorphy.
- *Equality with the R_{u(κ)} integral.* Rotating each half to arg κ keeps |e^{iκz/2}| ≤ 1 and stays in the damping region. Moving β* to arg κ/3 also stays in the region.
- *Boundary terms.* The bound on the dominating function is phase-independent. If ∫R²M(R)dR < ∞, then liminf R³M(R) = 0, so the arc terms vanish along a sequence of radii. Correct.
- *Spacelike case.* I checked the per-row phase conditions with b_j at β*±δ: 0 < β_i+β_j < π/2 and 0 < α−β_j < π/2 both hold.
  - The identity theorem on the ray arg κ = −π/8 (where e^{iπ/4}κ² = K² > 0) gives J_s = F_E(e^{iπ/4}κ²).
  - For arg κ ∈ [−θ, 0], arg t ∈ [π/4−2θ, π/4], inside the sector. The bound stays finite there, since arg κ_t ∈ [π/2−θ, π/2]. Turning the line back to R is therefore legitimate.
- *Timelike case.* √t = e^{−3πi/8}κ is the principal root for arg κ ∈ (0, 3π/4). Real κ gives arg t = −3π/4.
- *Sign of k·k.* With k^μ = κδ^μ_0, k·k = −κ², and e^{iπ/4}(−κ²) = e^{−3πi/4}κ². For small arg κ > 0, k·k = |κ|²e^{i(2 arg κ − π)}, which is k·k − i0. The same holds for κ<0 by evenness. Correct.

**Gap found in (iv).** J is a ratio, so it needs I^{(u)}[1] to be independent of u on the whole range 0<u<2. 053 gives this only for u ≤ 1. The proposal's "|I^{(u)}[1]| = |Z_E| (053)" cites 053 beyond its range. 053's specific auxiliary factor e^{3πi/8}Tr A_0² keeps a positive real part on R_u only for u < 7/6. With the phase on Tr A_0² re-chosen for [1, u1], the angles span 3π(u1−1)/4 < π, so the same Stokes argument works. The fact is true and easy to justify, but it has to be stated (F1).

**Scripts.**
- Re-run with output to the scratchpad; identical to the saved outputs:
  - `apply_check.py` (report mode): baseline 7a75554e…, anchor count 1 at L1512 (61 bytes, a7c77412…), insert LF 7677 / CRLF 7693 bytes, result 540271 bytes 28e8d36d…, CRLF 3220, bare LF 0;
  - `exact_checks.py`;
  - `check_a_integral.py` (maximum relative difference 6.9e-7).
- `n2_runs.py` was **not** re-run (about 3 h). Instead I checked every numerical sentence of the insert against `n2_runs.txt`:
  - moments within 4.4e-7 relative, against the claimed 5e-7;
  - β agreement 4.80e-11, against the claimed 5e-11;
  - slope changes 1.4-1.9% for (i) and 1.5-1.8% for smeared, against the claimed ≤ 2%;
  - R_0.5 versus R_0.6 about 2e-6, against the claimed 3e-6;
  - the Taylor difference at K=1 equals the first omitted term, 3.6e-6.
- The numerics are supporting evidence, not proof. `grid_tests.txt` is not relied on, and the insert makes no conditioning claim.

**LaTeX.**
- Braces and `\(`/`\)` are balanced. The only reference is `\ref{ass:lorentzian}`, which exists. No new labels or citations.
- No process language. The anchor is unique.
- `\mathcal J` is also used in Problem B (L279-288) for a rotation. It is defined locally here, so this is acceptable.
- Two problems found: the closing two sentences repeat the 053 block verbatim on consecutive paragraphs (F2), and k^μ is never defined (F4).
- No build was run (read-only). The researcher's scratch build is not independently verified.

**Literature.** No new citations. 2112.15368 is not cited and was not independently verified. No SME consultation is needed for the insert as worded, because it makes no novelty claim.

## Findings
**F1. Severity: minor.**
- *Location:* insert (iv), first sentence.
- *Finding:* J is the ratio of the R_u integral to I^{(u)}[1]. Its holomorphy and the bound on 3π/8 ≤ arg κ < 3π/4 use the fact that I^{(u)}[1] is independent of u (and nonzero) for 1<u<2. 053 proves this only for u ≤ 1. The cited auxiliary factor fails for u ≥ 7/6 unless its phase on Tr A_0² is re-chosen.
- *Required action:* replace "so the integral of (i) on \(\mathcal R_u\) defines \(\mathcal J(\kappa)\) for \(0<\arg\kappa<3\pi/4\)," with:
  "so the integral of (i) on \(\mathcal R_u\), divided by \(I^{(u)}[1]\), defines \(\mathcal J(\kappa)\) for \(0<\arg\kappa<3\pi/4\), where \(I^{(u)}[1]\) is independent of \(u\in(0,2)\) by the Stokes argument of the preceding paragraph with the phase of the auxiliary factor on \(\operatorname{Tr}A_0^2\) chosen for each interval of \(u\),"
- Also correct the proposal's "(053)" citation for |I^{(u)}[1]| = |Z_E|.

**F2. Severity: minor.**
- *Location:* the closing two sentences of the insert.
- *Finding:* "It does not derive a signature, a background, a frame or the fermion content, and Assumption~\ref{ass:lorentzian} is not discharged. Problem~E remains open and PROGRAMME-CONDITIONAL." repeats the 053 block's last two sentences verbatim on the consecutive paragraph. Precedent: 009 r1 and 011 r1 flagged the same thing.
- *Required action:* replace both sentences with the single scoped sentence:
  "Assumption~\ref{ass:lorentzian} is not discharged by this either, and Problem~E keeps its ledger label."

**F3. Severity: minor.**
- *Location:* insert (i), last sentence.
- *Finding:* "The same construction at \(u=1\) gives the Euclidean expectation value …" comes right after a limit statement and can be read as a limit of I_eps. At u=1 no limit is established, at any N, because (i) needs u<2/3. The statement is an identity of integrands.
- *Required action:* replace it with:
  "At \(u=1\) the same choice of \(\kappa\) makes the integral on \(\mathcal R_1\) at \(\epsilon=0\) the Euclidean expectation value of \(O\) with every factor replaced by \(\mathrm e^{\mathrm iK\tilde A_\mu}\); this is an identity of integrands, not a limit of \(I_\epsilon\)."

**F4. Severity: minor.**
- *Location:* insert (iv), "With \(k^\mu k_\mu=\mp\kappa^2\) for the two cases,".
- *Finding:* k^μ is undefined, and in (ii) the letter k is 053's polynomial degree.
- *Required action:* replace it with:
  "With \(k^\mu=\kappa\delta^\mu_0\) and \(k^\mu=\kappa\delta^\mu_j\), so that \(k^\mu k_\mu=\mp\kappa^2\),"

**Note (not a finding).** After these edits, re-run `apply_check.py` and the scratch build, and update the hashes and byte counts.

No blocking or major findings. No prior-claim error: the 053 text is consistent with this package, and its closing caveat remains a correct scope statement of that paragraph.

## Scope of what is established
**Established identities:**
- Step 0, any N.
- The unitary-phase identity.
- The smearing identity and its bound.
- The u=1 integrand identity.

**Proved at N=2; conditional for N≥3** (053's flat-direction bound at k=0, and Z_E ≠ 0):
- (i), the limits at complex axis momenta on the rays e^{3πiu/8}R (timelike) and e^{−πiu/8}R (spacelike), for 0<u<2/3;
- (iii), the smeared limits as line integrals.

**Proved at N=2 only:**
- (ii), non-integrability for real κ ≠ 0, using the verified sharpness of k<14;
- (iv), the holomorphy of J and F_E on the stated sectors and the bound (once F1 is in);
- the spacelike smeared limit ∫_R φ F_E(e^{iπ/4}κ²);
- the timelike real κ on the edge arg t = −3π/4, reached from k·k − i0.

**Class of the bounded result:**
- IKKT content supplied, C=0, gamma=0;
- Definition (A) with a δ_{μν} Gaussian regulator;
- fixed N, eps→0 first;
- axis momenta, products of single-index exponentials;
- complex momenta on the unitary rays, or Gaussian smearing in κ.

Within this class, the regulated Lorentzian integral yields only continuations of Euclidean data. At N=2 these are values and line integrals of F_E, which F_E on t>0 determines. That is the "real-time reading by continuation" that 053 left unexcluded. It is now realised for this class, not ruled out.

**Not established:**
- the pointwise limit at real timelike κ;
- continuation of F_E across arg t = −3π/4;
- boosted momenta;
- holomorphy for N≥3;
- N→∞ first;
- gamma ≠ 0;
- Definitions (B) and (C);
- any signature, background, frame or fermion content.

**Classification:** PROGRAMME-CONDITIONAL. Problem E remains OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL.

**Relaxations that could still favour the infrared / full-GR derivation (ranked):**
1. **Edge behaviour at N=2.** Find a one-variable representation of F_E (for example the radial marginal of Ã_0) that decides whether F_E continues across arg t = −3π/4, and whether the pointwise eps→0 limit at real timelike κ exists and equals the boundary value. This is the one place a non-Euclidean, singular, light-cone datum could still enter in this class.
2. **Contours beyond per-index phases.** The 3π/4 cap belongs to the phase-per-index contour family. In shifted variables the conditions are |ψ_μ+ψ_ν| < π/4, which I checked are equivalent to my damping conditions. Complex rotations that mix indices are not excluded and could enlarge the sector, or reach boosted momenta.
3. **N→∞ taken first** (053 rank 2). The constants here are not uniform in N.
4. **A positive real-time reading of the continuation.** Reflection positivity (Osterwalder-Schrader type) of the N=2 Euclidean characteristic functions would turn the continuation into a real-time Hilbert-space statement. Spacetime stays emergent.
5. **Holomorphy for N≥3**, via a spectral version of the radial argument, and an independent proof of 053's bound.
6. **gamma>0, and Definitions (B) and (C).**

**Milestone.** This is a bounded no-go extension. It answers, for a stated class, the open exception that 053 named explicitly ("non-polynomial observables such as Tr e^{ik^μA_μ}"). I judge it M2, effective on acceptance. It is not M3 (no merged claim is wrong), not M4/M5, and not a breakthrough: no step of signature derivation is made.

## Recommended disposition
Revise. Apply F1-F4 verbatim, refresh the apply_check hashes and the scratch build, and return as r2. If r2 is a plain ACCEPT with M2, the r2 gatekeeper must do the full scan required by CLAUDE.md 3(b).

## Corrected snippet
The four replacements in F1-F4 are the snippet. They add no new physics. F1 adds no new assumption: I checked that the re-phased auxiliary factor exists for every [1, u1] ⊂ [1, 2), because the A_0 angle span is 3π(u1−1)/4 < π and the spatial span is π(u1−1)/4.

Files:
- C:\Users\redgi\Projects\namcg-lab\proposals\054-lorentzian-fourier-observables\proposal-r1.md
- C:\Users\redgi\Projects\namcg-lab\proposals\054-lorentzian-fourier-observables\appH_insert.tex
- C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex (L1482-1515)

VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M2 | FLAGS: none | PROGRESS: first | OPEN: 0/0
