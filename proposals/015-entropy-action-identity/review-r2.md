VERDICT: ACCEPT | MILESTONE: M2 | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
Every r1 finding F1–F6 is applied as required, and nothing else in the LaTeX changed apart from a few connective phrases. The anchors, labels and BibTeX records check out, and no label is touched.

## Source reading
Digest + targeted reads. The r1 full scan stands, and `git status` shows no chapter or bib changes since then. Only `proposals/016-mirage-stress/` is untracked.

`python scripts/make_digest.py --check` printed `DIGEST STALE` just now. I do not rely on the digest for any claim here. Every passage was checked directly against `chapters/` and `proposal-r1.md`. Because no chapter files differ, no new full scan is triggered. The orchestrator may want to regenerate the digest.

I read `proposal-r2.md` in full and diffed it by eye against the r1 Item 1–4 text. I also re-read `review-r1.md`. I did not re-run the five scripts. They are unchanged and no new script was added. The r2 F2 note is plain arithmetic, which I re-checked by hand.

## Claim under review
Problem B (B2 area coefficient, and the normalisation half of B1), via the entropy-action identity route. The current ledger text is quoted from r1 and not re-edited: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived."

Problem F reads: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion."

The Chapter 17 critical-path set A, B, C, D1, E, F, G-derived, N is unchanged. The package proposes no label change.

## Checks performed (direct verification)
- **F1.** The appG snippet is character-identical to my r1 snippet, including both delta prescriptions.
- **F2.** The appH no-go sentence now reads "for the replica of the first paragraph". The sentence "In this class (Poisson limit, Euclidean section, background Feynman gauge, one loop, \(\LUV^2\) term, the two modes with \(\delta\rho=0\)) and for the replica of the first paragraph, …" supplies both the replica clause and the class clause. The c_A line also says "for the replica of the first paragraph".
- **F3.** The ch07 sentence is verbatim my snippet.
- **F4.** The appG Status sentence is verbatim my snippet.
- **F5.**
  - The first paragraph says "the coefficient \(\mathcal A\) of Equation~\eqref{eq:Geff-structure}", which fixes the area/coefficient symbol clash.
  - The variables are named: "in the variables \((G,\rho,\partial\Theta)\) of the contact-term paragraph below".
  - The paragraph closes with a scope pointer to the second paragraph: "the scope of the whole block is given at the end of the second paragraph below".
  - The single closing status sentence stays only on the second paragraph, so there are no repeated status lines.
- **F6.** The singular-ρ result reads "a statement conditional on that branch and not used below". "Checked by direct summation" is gone, and the support cited is the local a_1 ratio.
- **Prior-claim framing.** None remains in the proposed LaTeX. In the proposal body it is only withdrawn explicitly, in the changelog and in the milestone and gatekeeper-instruction sections. Items 2a, 3 and 6 are framed as clarifications.
- **Other LaTeX.** Compared with r1, the Replica, Contact term, Dependence-on-variables (including the table) and TT paragraphs are textually unchanged. The only changes are the F5/F6 edits and the F2 clauses above.
- **Anchors, each occurring once.**
  - The appH "Those inputs are not supplied by the displayed microscopic" anchor is in `appH-microscopic-proofs.tex`.
  - The appG "with the prefactor identified from the Seeley" anchor is in `appG-sector-entropy.tex`.
  - The appG Status anchor, searched as a fixed string (appG l. 53), is also in `appG-sector-entropy.tex`.
  - The ch07 "borrows a geometric identity used in Jacobson" anchor is in `ch07-massless-tensor.tex`.
- **Labels.** `eq:Geff-structure` exists at ch08 l. 223. The other labels were verified in r1 and no chapter has changed since.
- **No label change.** There is no status, priority or completion edit anywhere.
- **BibTeX.** The two entries are identical to the r1 entries.
  - Solodukhin2011: BibTeX record: VERIFIED.
  - SusskindUglum1994: BibTeX record: VERIFIED.
  - Neither key exists in `bib/` or `chapters/` yet, so the integrator adds both.
- **F2 arithmetic.** Under replica (II), c_A = −N_tot/12, which is negative. Equality with c_T = N_tot/6 − 4 needs N_tot = 16, where 1/G_T = (16−24)Λ²/(12π) < 0. So the no-go is not an artefact of replica (I) for positive G_T. This is stated in the proposal as a check, not a manuscript claim.

## Findings
- **Minor (optional, not required).** appH "Which geometry carries the cone", sentence "The two choices differ by the factor −1/2 in every sector."
  - Finding: it now reads unconditionally, although the (II) result is flagged conditional earlier in the same paragraph.
  - Suggested edit: add "(for the branch stated)". The caveat is already adjacent, so I do not block on this.
- No blocking or major findings remain.

## Scope of what is established

**Established identities and derivations**
- The flat-cone coefficient and S = A/(48πε²) per component.
- The contact term ΔS = −2π tr Q⟨φ²⟩A, which is consistent with Solodukhin eqs. (321)–(323).
- E_s = R_G/4 + torsion terms, and the TT arithmetic.

**Conditional**
- Replica (I): the pulled-back replica with bounded endomorphism and connection, in the variables (G, ρ, ∂Θ).
- Replica (II): conditional on the m = 0 branch, and unused.
- The Jacobson reduction to m_T = 0 and G_T = G_A.
- The bounded no-go. Its class is: Poisson limit; Euclidean section; background Feynman gauge; one loop; Λ² term; the two δρ = 0 modes; bosonic content N_tot = N_s + 2; replica (I); constant Θ̄; Fierz–Pauli reading of T^op. Nothing is claimed outside this class.

**Open**
- ass:EE, stationarity, the map Θ → G, and any value or sign of G_eff.
- Whether the ghost-weighted cone sum is a physical entropy, and whether the matrix algebra has an area law.

**Classification and status**
- PROGRAMME-CONDITIONAL. Problem B stays OPEN, CRITICAL PATH. Problem F stays OPEN.
- Spacetime stays emergent, since the cone sits on the composite G built from Θ.
- No BREAKTHROUGH: no critical-path step is derived.

**Ranked open avenues for the G_T ≠ G_A gap**

The proposal's list is correct and correctly scoped. My ranking of which relaxations are most promising, most favourable first:
1. **Content.** Fermions or extra fields whose T² endomorphism terms shift 1/G_T − 1/G_A by +2Λ_v²/π. This is algebraic and decisive. It relaxes the "bosonic content N_tot = N_s + 2" hypothesis.
2. **Tensor-block identification, Φ–a mixing and the Presentation-B frame coupling.** These could change the quadratic form on the TT modes. They relax the "δρ = 0 modes of a^μ" and Fierz–Pauli-reading hypotheses.
3. **Tree-level term and the 014 class.** A derived tree-level Einstein structure could supply G_T. This relaxes the "Λ² term only" hypothesis.
4. **Gauge fixing.** Non-minimal gauges, and a gauge-invariant (on-shell propagator) coefficient. This relaxes the "Feynman background gauge" hypothesis. It is plausible but the off-shell form is expected to remain gauge dependent, so it is less likely to yield a clean closure.
5. **Moyal and finite-cutoff corrections.** These relax "Poisson limit" and "Λ² term". They are the hardest, but the only avenue that tests the exact matrix model.
6. **Curved or non-constant backgrounds, and a_2 partners.** These relax "constant Θ̄". They are unlikely to repair a Λ² mismatch.
7. **Replica choice.** (II) or an edge-mode-corrected ghost-weighted entropy changes c_A. For (II) the sign structure already prevents equality at positive G, so this is least promising.

## Recommended disposition
Integrate as-is at ordinal 15. The optional minor wording item may be taken or left.

**Accepted items, by file:**
- `chapters/appH-microscopic-proofs.tex`: Item 1, the two new paragraphs in `sec:status-B`.
- `chapters/appG-sector-entropy.tex`: Item 2a (replacement of the two sentences) and Item 2b (the Status sentence).
- `chapters/ch07-massless-tensor.tex`: Item 3, the sentence inserted after "argument."
- Bibliography (`bib/namcg.bib`): the Solodukhin2011 and SusskindUglum1994 entries. BibTeX record: VERIFIED for each.
- Not accepted or touched: ch08 (left unedited, follow-up recorded), ch06, ch17, and any label or status text.

The integrator should normalise CRLF line endings and run `python scripts/build_check.py`.

## Corrected snippet
None needed.
