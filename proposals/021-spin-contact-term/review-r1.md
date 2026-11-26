VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M2 | FLAGS: none | PROGRESS: first | OPEN: 0/3

## Verdict
The mathematics holds as a bounded, conditional no-go with no PRIOR-CLAIM-ERROR. Three wording points need fixing before integration: the sign and weight of the Dirac contact, the Kabat attribution, and the "which of 2 and 0" localisation.

## Source reading
- **Full scan, per CLAUDE.md 3(c) and 3(d).** `python scripts/make_digest.py --check` reported `DIGEST STALE`. I read every file in the manifest in full, 30 files under `C:\Users\redgi\Projects\namcg-lab\chapters`:
  - `ch01`–`ch18`.
  - `appA`–`appL`.
  - `appH` (2499 lines) and `ch17` read in full.
- I read the working tree, which holds the uncommitted 017–020 integrations.
- I also read the proposal, `appH_insert.tex`, `bib_entries.bib` and the three scripts with their outputs. I read `reports/ledger.md`, `MILESTONE.md` and `bib/namcg.bib`.
- Proposal 022 was not examined.
- There are no earlier rounds for 021.

## Claim under review
Problem B, `sec:status-B`. Quoted verbatim from `chapters/appH-microscopic-proofs.tex`:
- B: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived."
- A: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL."
- F: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN…"
- Chapter 17 criterion: A, B, C, D1, E, F, G-derived and N are DERIVED. H, I and J are optional. No discrepancy found.

The claims are:
1. The "spin term" is already inside c_A = +1/3 per Dirac field, so a further contact would double count.
2. The pulled-back replica (ρ regular, cone on G) is not a limit of smooth Poisson structures. A smooth first-order replica gives c_A = −N_tot/12.
3. At (n_D, N_s) = (2, 6): fixed-state antiperiodic c_A = 2; with a Kabat/Donnelly–Wall vector contact c_A = 1; smooth c_A = 0, which is a 0 = 0 equality.
4. The ambiguity is localised to the flux of ∇lnρ through Σ.

No label is changed.

## Checks performed
- **Reruns.** I re-ran all three scripts with `python -I`.
  - `dirac_lichnerowicz.py` (98 s), `firstorder_poisson.py` and `cone_contact_bookkeeping.py` reproduce the stored outputs.
  - The E_f fit residual is 3.4e-13. The fit has 7 samples and 4 unknowns, so it is overdetermined.
- **Lichnerowicz identification, checked independently of the fit.**
  - The script finds tr E_f/4 = R_G/4 − T²/16 + TT′/8.
  - The merged Weitzenböck relation R_G = −¼T² − ½TT′ + V² − 2□lnρ turns this into tr E_f/4 = E_s − T²/8, equivalently tr E_f = 4E_s − X/2.
  - That agrees with the merged β-trace tr β_σβ^σ = −½X and with the merged table entry (4/6)ρR + ½ρ²X.
  - The merged scalar line E_s = ¼R_G + T²/16 + TT′/8 reproduces E_s = −½□lnρ + ¼V².
  - R_G, T², TT′, V² and □lnρ are linearly dependent through that relation. So Q_f = ¼ is a statement about the choice of independent variables, exactly as in the merged scalar case, and "no further term" is the representation with V² and □lnρ coefficients zero.
- **Cone constants.**
  - From AP = (n²−1)/(12n) and P = −2AP: AP′(1) = 1/6, P′(1) = −1/3, so (AP−P)′(1) = 1/2.
  - The Q-contact −(1−n)trQ gives trQ = 4·¼·½ = ½ for a two-component block, i.e. 2Q_f = ½. This matches.
  - The match is a derivative-at-n=1 statement only. The full n-dependences differ.
- **Sign of the excess.**
  - Q = 0 variables, weight −1: −2/3.
  - Q = ¼ variables: −4(1/6−1/4) = +1/3.
  - So the excess is +1 per Dirac field, and the contact in c-units is −w trQ = +1.
  - This confirms the direction: the spin term raises c_A.
- **First-order identity, derived by hand.**
  - From R_G = ρ⁻¹[R[g_ρ] − 3□lnρ − (3/2)|∇lnρ|²] and R_G^(1) = −2□_Gδlnρ (the first-order form of the merged Weitzenböck relation), I get R[g_ρ]^(1) = □_{g_ρ}δlnρ.
  - Hence ρ̄R[g_ρ]^(1) = ρ̄²□_Gδlnρ = −½ρ̄²R_G^(1). Both identities hold.
  - I also checked the example Θ¹² = 1/f(x¹,x²), Θ³⁴ = 1: R_G = −2□_G ln ρ exactly.
  - A deficit 2π(1−n) with R_G^(1) = −2□δlnρ forces δlnρ = (n−1)ln r, i.e. flux 2π(n−1) equal to the deficit.
  - The script `firstorder_poisson.py` uses one fixed rational ω̄, not an arbitrary one. The general case follows from the identities above.
- **Bookkeeping, re-derived.** From the c-table and weights:
  - c_A^sm = −N_tot/12.
  - c_A^sm = c_A(AP) − ¼(N_s+2). For the connection and ghost sector: 4 components give −1, the weight-(−2) ghost gives +½, net −½ = −¼·2.
  - At (2, 6): 2, 1 and 0 as claimed, with c_T = 0 and N_tot = 0.
  - For any sector-uniform Q, c_A = N_tot(1/6−Q) = 0, so the 0 = 0 character is correct. The LaTeX says this.
  - The equality line N_s = 14−4n_D appears only in the scratch files and not in the LaTeX.
- **Sources (Crossref and arXiv abstract pages).**
  - Kabat, Nucl. Phys. B 453 (1995) 281, DOI 10.1016/0550-3213(95)00443-V, eprint hep-th/9503016. Crossref gives vol 453, issue 1–2, pp 281–299, 1995, single author Kabat. The arXiv journal-ref says 281–302; the Crossref pages are used. BibTeX record: VERIFIED.
  - Donnelly & Wall, Phys. Rev. D 94 (2016) 104053, issue 10, DOI 10.1103/PhysRevD.94.104053, eprint 1506.05792. BibTeX record: VERIFIED.
  - Kabat abstract: "For fields of spin zero and one-half the black hole entropy is identical to the entropy of entanglement." For spin one the two differ by a contact interaction with the horizon.
  - Donnelly–Wall abstract: the contact term amounts to "one negative scalar degree of freedom confined to the entangling surface". I checked that a negative 2D scalar gives ΔS = −Λ²A/(8π), i.e. c = −1 in these units. So "Kabat value −1" is consistent.
  - I could not extract the full text of Kabat (PDF unreadable). Only the abstracts are verified.
- **Anchor.**
  - "…do not compute the next order of either side. Problems~B, C, D, F and~G remain open." occurs exactly once.
  - `\section{Problem C: conformal mode and Cassini}` occurs exactly once.
  - `\LUV` is defined at `namcg-book7.tex:54`.
  - `appH_insert.tex` is identical to the proposal's LaTeX block and has CRLF endings.
  - Braces and `\(`/`\)` are balanced.
  - Kabat1995 and DonnellyWall2016 are not in `bib/namcg.bib`, so the integrator must add them.
  - I did not compile. The proposal reports a clean scratch compile (0 undefined or multiply-defined; not independently verified).
- **Emergence.** G, ρ and g_ρ are all built from Θ. Spacetime stays emergent.

## Findings

**F1 (major). Sign and weight of the Dirac contact.**
- Location: LaTeX paragraph 1, "adding a contact −tr Q_f per Dirac field to it would count it twice".
- Finding: the contact of the Q_f R_G term shifts c_A by −w trQ_f, and at w = −1 that is +1 per Dirac field. As written, "−trQ_f" can be read as a lowering of −1 per Dirac.
- Reason: this is the headline direction claim. The 019 ledger avenue spoke of a "Lichnerowicz −R/4" contact that could lower c_A by n_D. A reader could take the new sentence as saying that route exists but is double counted, when the point is that its sign is the opposite.
- Required action: state the weighted shift explicitly.

**F2 (major). Localisation of the missing datum.**
- Location: LaTeX paragraph 3, "Which of 2 and 0 is the Λ² area coefficient … is the value of the flux of ∇lnρ through Σ".
- Finding: the sentence is binary and says the coefficient "is" the flux value.
- Reason:
  - Within the first-order smooth Poisson class the flux equals the deficit, so there are only two extreme cases.
  - A general regularised replica of the matrix state could carry an intermediate flux. c_A as a function of flux is not computed.
  - The fixed-state value 2 also depends on the gluing and the state, which the paragraph elsewhere says are not derived.
  - The datum belongs with the replica, tip domain and state, which are Problem A territory. The LaTeX correctly avoids saying "Problem A", and the wording should not imply a decisive single datum.
- Required action: state that 2 and 0 correspond to zero flux and full-deficit flux, that intermediate values are not computed, and that the actual replica is not derived.

**F3 (major). Kabat attribution.**
- Location: LaTeX paragraph 1, last sentence, "For spin ½ the conical and the induced coefficients are the same in the torsion reading~\cite{Kabat1995}".
- Finding: Kabat covers spin ½ with the Levi-Civita spin connection. The torsion reading of the NAMCG operator O_f is the proposal's own computation (AP = +1/3 equals the Q_f = ¼ induced coefficient).
- Required action: cite Kabat only for the standard statement, and say the torsion-reading equality follows from the computation above.

**F4 (minor). Q_f = Q_s in the torsion reading.**
- Finding: the scalar has the same R_G/4 in the torsion reading. The Dirac-specific content is therefore the holonomy gluing, and the identification with the Q_f contact is a statement about the n-derivative at n = 1 (1/2 = 2Q_f), not an identity in n. Say this in one sentence.
- Related: the "−1/2 branch-free" claim is the first-order local-density statement for a regularised smooth family. The Bessel-branch issue in the merged text is not removed for the unregularised singular-ρ cone.

**F5 (minor). Replica definition.** Add that the first-order result does not by itself exclude the pulled-back replica as the definition of Tr ρⁿ. It says only that this replica is not a limit of smooth Poisson structures, at first order about constant Θ̄. Define "fixed-state" as the pulled-back replica with antiperiodic Dirac gluing.

**F6 (minor). Script scope.** The LaTeX says "any constant antisymmetric invertible ω̄ … exact symbolic computation". The script checks one rational ω̄ with arbitrary A. The general statement follows from the merged exact identities, as shown above. Say "checked symbolically for a generic ω̄ and following from Weitzenböck identities".

**F7 (minor). Cross-references.** "the normalisation of the preceding paragraph" means the fermion-gluing paragraph, not the paragraph immediately before the new block. "The two preceding paragraphs" are the two `\paragraph` blocks. Name them.

**F8 (minor). Weights qualifier.** "0 for scalars and ghosts" holds only for minimally coupled fields in the variables (G, ρ, ∂Θ). In the torsion reading the same sentence's smooth value uses −¼ per scalar and +½ for the ghost. Add the qualifier, so that "at most the value 1" is clearly scoped to the standard-weight class (Dirac +1 included, vector −1).

**PRIOR-CLAIM-ERROR: none.**
- Merged text, `appH` sec:status-B, 015 block ("Which geometry carries the cone"): "Only the first is used in the identification above." The new paragraph agrees with this and adds the first-order rigidity. The merged "differ by the factor −½" is reproduced for all sectors, including Dirac (+1/3 = −½ × (−2/3)).
- The 019 text calls the +1 an "excess" of the cone value over the ρR[g_ρ] coefficient. The new text identifies it with the contact. This is a scope clarification, not a correction.

## Scope of what is established

**Established (conditional, M2).** The class is: Poisson limit, Euclidean section, α = 1, the Λ² term, one loop, 019 constants (quasi-free state, rotational flow, less singular extension, uniqueness of continuation), the pulled-back antiperiodic replica and the first-order smooth replica as defined.
1. The Dirac spin excess (+1 per Dirac field, AP over unrotated) equals the weighted Q_f contact at n = 1, so no further spin contact exists; the same contact is the −½ factor and AP = +1/3.
2. The smooth replica gives −N_tot/12 = AP + bosonic contacts. It is the 0 = 0 equality at the (2, 6) content and equals c_T on N_s = 14 − 4n_D (scratch only; unphysical contents).
3. Standard contacts (Dirac +1 included, vector −1 as an input, scalar/ghost 0 in the (G,ρ,∂Θ) variables) bring c_A at most to 1 at (2, 6), against the needed 0.

**Conditional or input.**
- The vector contact −1 for a^μ is an import from covariant Maxwell. In the torsion reading the connection sector has trQ = 1 with ghost Q = ¼, so the consistent net contact is −½, not −1.
- Fermion and symplectic-gauge edge modes are not examined.

**Not established.**
- The state, tip domain, gluing and the actual replica flux.
- The next order of either side.
- G_eff.

**Status.** Problem B stays OPEN and PROGRAMME-CONDITIONAL. No label change. No BREAKTHROUGH: no critical-path step is derived.

**Open avenues, ranked.**
1. The replica and flux datum. Compute c_A for intermediate flux, and the replica of the matrix state, as a Problem A sub-lemma.
2. The next order (Λ⁰ and log) on a curved J = 0 leaf, where c_T = c_A = 0 at Λ².
3. Tip domains for the vector, ghost and scalar sectors, and whether a Maxwell-like edge term applies to the symplectic gauge sector (bounded at c_A = 1 if so).
4. A non-quasi-free or non-rotational state.
5. Contents on N_s = 14 − 4n_D, as a check of non-vacuity only.
6. Sector cutoffs (tuned; low).

## Recommended disposition
Revise with F1–F3 (required) and F4–F8 (minor), then integrate. The bib entries are acceptable as submitted.

## Corrected snippet
No new physics or assumptions are needed.

1. Replace "and adding a contact \(-\operatorname{tr}Q_f\) per Dirac field to it would count it twice" with "and adding to it the contact of \(Q_fR_G\), which at the weight \(-1\) shifts \(c_A\) by \(+1\) per Dirac field, would count it twice".
2. Replace "For spin \(\tfrac12\) the conical and the induced coefficients are the same in the torsion reading~\cite{Kabat1995}." with "For a Dirac field with the Levi-Civita spin connection the black-hole and entanglement entropies coincide~\cite{Kabat1995}; for the torsion reading the corresponding equality (both \(+\tfrac13\) per Dirac field) is the computation above."
3. Replace "Which of \(2\) and \(0\) is the \(\LUV^2\) area coefficient of the matrix state is the value of the flux of \(\nabla\ln\rho\) through \(\Sigma\) in the regularised replica." with "The values \(2\) and \(0\) correspond to a replica in which \(\ln\rho\) carries no flux through \(\Sigma\) and one in which it carries the full deficit; intermediate fluxes are not computed, and which replica the matrix state selects depends on the state and the tip regularisation, which are not derived here."
4. Make the sentences carrying F4–F8 edits as described above.
