VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/1

## Verdict
The closed forms and the bounded no-go are sound within H1-H5. Two sentences of the block state the codimension-4 classification as exact, although it rests on a numerically verified, unproved self-duality identification. Rewording is required (smallest correction below). I found no PRIOR-CLAIM-ERROR and no status change.

## Source reading
Digest + targeted reads. `make_digest.py --check` printed DIGEST STALE (dirty-chapters: yes). I read the working-tree appH directly, including the integrated 018 paragraphs from "Conjugate-coordinate class: extra stress ..." through "\section{Problem G: HBEV}" (lines ~1960-1982). The block changes no scope, status or definition, so no 3(c) full scan is triggered. The ordinal is 18 or 19, so no 3(a) full scan is due. I did not do a full scan. I did not re-read Ch. 17 or the Problem F entry in full this round. The status quotation below is therefore from the proposal and the 018 block, not independently re-quoted.

## Claim under review
Within the 018 class, the block claims four things.
- It gives closed forms for the vertical flux F = Q^{1/2} ω Q^{1/2} with ω δ-self-dual, and for f1, f2.
- It claims f1 = f2 for all ζ only on |y4| = ℓ, y_i = 0 (codimension 4 in the 6D leaf).
- It claims that the compact so(6) section gives f2/f1 = |y4|/ℓ, so no zero-mode family appears.
- It claims that a ζ-independent transverse flux cannot cure the instability in the Poisson limit, and that the vector density at f1 = f2 tends to f²/(2π²), so the ζ-integral still diverges.

The target is Problem F: the matrix-derived G_eff, sign and size.
- The proposal quotes Appendix H sec:status-F as "OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL" with the qualifier that treating G_eff as an input leaves F OPEN.
- The block does not change this label. It ends "This changes no ledger label; Problem~F remains open."

## Checks performed
Direct verification:
- **Anchor.** `\section{Problem G: HBEV}` occurs exactly once (line 1982). The block sits after the 018 paragraph ending "Problem~F remains open." Both are consistent with the proposal.
- **Block text.** The LaTeX block in proposal-r1.md equals block-r1.tex (string comparison: True). It uses no labels or \cite, and the process-language scan found nothing.
- **Q and det Q.** I re-derived det Q = ℓ²|y4|⁶ by hand: on the (t, y⃗) plane ab = ℓ²m, with the remaining eigenvalue m twice. Q is positive definite.
- **Closed forms.** I re-derived the amplitudes by hand: l_par/s_par = (ℓ-|y4|)/(ℓ+|y4|), hence f2/f1 = |y4|/ℓ along the axis, with min/max for |y4| > ℓ. This agrees with check_orientation_displacement.out.txt (0.0909, 0.0476, 0.0244).
- **Large-f density.** The vector density tends to f²/(2π²) for sf ≫ 1: 4 cosh(2sf) · f²/(16π² sinh²(sf)) → 1/(2π²) · f². This is independent of s, so the ζ-integral diverges. check_algebra.py agrees.
- **V4.** V4 = -4(f1²-f2²)² (sympy, re-run).
- **Compact section.** check_compact_section.py re-run: PB/lie ratio constant (-1), ranks (4,6), error 4e-16.
- **Troost hep-th/9909187.** I opened it (arXiv abstract and ar5iv). It is "Constant field strengths on T^{2n}", Nucl. Phys. B568 (2000) 180-194. Eq. (35) is in Section 7: λ_k^± = 2π(Σ_i(2m_i+1)f_i ± 2f_k). Section 9 states inline "no tachyonic modes when f2+…+fn ≥ f1" and "on T^4 stability implies self-dual (f1=f2)". The block's use matches. The lowest level is Σf - 2f_max, which gives the condition f3 ≥ f1 - f2. The DOI was not checked; the journal data come from the arXiv page.
- **Steinacker 2303.08012.** I did not re-open it. The R-f2 reading and the eq. numbers 4.14-4.21 are not in the LaTeX block, so nothing in the block depends on them. The V4 identity is a pure algebra check.

Not verified:
- The Levi-Civita identification of the numerically defined horizontal distribution. Self-duality is checked only at 300 points × 2 centre directions (worst opposite-part fraction 7e-10).
- The codimension-2 "some ζ" set (not in the block).

## PRIOR-CLAIM-ERROR check (018)
The merged 018 paragraphs in appH state only the 12-point, 9-direction sample range f1/f2 ∈ [0.006, 0.84] ("never at 1; no claim is made over the whole leaf"). They also state the Lorentzian electric-type case and the vector-sector instability.
- They do not mention a compact twistor section or "avenue 5" anywhere (grep of `twistor` and `compact` in appH finds only unrelated hits).
- The 018 avenue therefore appears only in proposal and review text, so there is no manuscript error.
- The 020 claim "sampled range ... supremum 1" is consistent with the merged 018 wording.

## Findings
1. Severity: major (wording; it affects the accuracy of the status claim).
   - Location: Consequences (i), "The closed forms give f1=f2 for all ζ exactly on y⃗=0, |y4|=ℓ ... codimension 4", together with the final scope paragraph.
   - Finding: "exactly" and "the closed forms give" present the locus as a theorem. The closed forms exist only through F = Q^{1/2}ωQ^{1/2} with ω self-dual. That statement is a numerical check at 300 points plus a structural (constant-curvature) argument. The Levi-Civita identification is not proved, and the proposal says so. The leading paragraph hedges ("expected statement"), but the final scope paragraph does not list it as unproved.
   - Required action: add "conditional on the self-duality statement above" to (i), and add to the final scope sentence that self-duality of Q^{-1/2}FQ^{-1/2} is verified numerically at sampled points and is not proved, so the locus classification is conditional on it. Also replace "a union of at most two lines" by "a linear subspace of the ζ-plane (a line, or the plane if F is (anti-)self-dual)". The set {ζ : Lζ = 0} for a linear map L: R²→R³ is a point, a line or the plane, so "two lines" is loose.
2. Severity: minor.
   - Location: Consequences (iii).
   - Finding: the Troost levels are for constant diagonal flux on T^{2n}. They are applied here as the local Landau symbol, a Euclidean analogue.
   - Required action: say "as the Landau levels of the same form" and add the \cite with the bib entry. The journal data now verified: NPB 568 (2000) 180-194. If the integrator does not add the bib entry, keep the bare "hep-th/9909187" and do not use \cite.
3. Severity: minor.
   - Location: the Q = Gram/ambient-metric remark and the "(ii) ... self-duality holds identically only for the contraction by Q^{-1}" sentence.
   - Finding: the sentence is correct as a statement about the closed form. The block does not say that Q^{-1} contraction is not shown to be supplied by the matrix action. It does say it is "not a constant contraction of the matrix indices", which is adequate. Keep as is.
4. Everything else holds.
   - The "(ii) compact so(6)" statement is correctly limited to the constant δ contraction.
   - The scope paragraph names the hypotheses (Poisson limit, leading symbol, equiregular points, the η→δ contraction, constant additional fluxes, bosonic content).
   - The block does not claim a position-dependent contraction is excluded.
   - The block does not claim to determine w.

## Scope of what is established
Established (conditional on the numerically verified self-duality identification):
- the closed forms for f1, f2;
- the codimension-4 locus where f1 = f2 for every ζ, including the compact result f2/f1 = |y4|/ℓ (a numerical identity, 4e-16);
- the vector-sector instability off the locus, with relative depth growing linearly with the distance from it;
- the failure of a ζ-independent transverse flux to stabilise on an unbounded fibre;
- the s-independent f²/(2π²) density at f1 = f2, so the ζ-integral diverges and the proper-time cutoff does not regulate it.

Not established: the Levi-Civita/self-duality identification as a proof; the sign and size of w; any contraction other than η→δ or so(6) with δ. The classification is PROGRAMME-CONDITIONAL. Problem F, and the critical-path set, remain OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. There is no label change and no emergence issue: the background direction ŷ is built from matrix data, and the anisotropy is SO(3,1)-covariant when y^μ is treated as a vector.

The loop should follow up on these avenues, ranked by promise (they relax stated hypotheses, and none is excluded here):
1. H2: the position-dependent ambient contraction Q^{-1} (f1 = f2 identically). Determine whether the matrix action, gauge fixing or regulator supplies the (y_a D^a)²/ℓ² term. Most favourable.
2. H4 with a finite fibre: truncation of ℓ with transverse flux f3 ≥ 2 sup|Ln| ζ_max, giving a finite positive fibre sum (the R-b3 analogue).
3. The SO(4,1)-covariant presentation X^A = M^{A5} (five horizontal fields; not computed).
4. R-f2: the SUSY flux expansion of the Lorentzian one-loop action; compare its radius of convergence with |r|/|p|. V4 = -4(f1²-f2²)² vanishes exactly on (anti-)self-dual flux, but no identification with Steinacker's ΔF is claimed or available, so this is a lead and not an application.
5. H1: exact so(4,2) character analysis with Moyal terms.
6. Fermions help only on the codimension-4 locus; at f1 ≠ f2 the Dirac-squared Landau levels are non-negative and cannot cancel a tachyon.

## Recommended disposition
Revise, then integrate. Apply Findings 1 and 2 only; the block is otherwise suitable. It is a coherent bounded no-go, a locus classification with a correction of an unmerged avenue. It is not a breakthrough and not a derivation of w. The package is single-purpose and correctly sized.

## Corrected snippet
The following replacements need no new physics.
- In (i), replace "The closed forms give \(f_1=f_2\) for all \(\zeta\) exactly on" by "Conditional on the self-duality statement above, the closed forms give \(f_1=f_2\) for all \(\zeta\) exactly on".
- Replace "is a union of at most two lines unless \(F\) is (anti-)self-dual identically" by "is a linear subspace of the \(\zeta\)-plane (a line, or the whole plane only if \(F\) is (anti-)self-dual)".
- In the final scope paragraph, insert after "bosonic content" the sentence "The self-duality of \(Q^{-1/2}FQ^{-1/2}\) is verified numerically at sampled points and is not proved, so the classification of the set \(f_1=f_2\) is conditional on it."
- Optional: add \cite{Troost2000} and the bib entry from the proposal (journal data verified via the arXiv page; the DOI was not verified).
