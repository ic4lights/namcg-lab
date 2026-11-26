VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M2 | FLAGS: none | PROGRESS: first | OPEN: 0/2

## Verdict
The cone calculation, the contact-term sign, the torsion-basis identity and the TT arithmetic all check out, and Problem B is not touched or closed. Two required corrections remain before integration. The appG replacement sentence is ambiguous about the conical-delta convention. The no-go sentence in appH must name the replica it depends on. I do not find any of the three flagged "prior-claim" items to be an error in merged text, so there is no PRIOR-CLAIM-ERROR and no M3.

## Source reading
- **Full scan: done.** I read every file under `chapters/`.
  - ch01 to ch18 in full: ch06, ch07 and ch08 in contiguous ranges, ch17 and ch18 in full.
  - appA to appL in full.
  - appH, all 2410 lines, in ranges 1-36, 36-150, 141-841, 840-1670, 1660-1900 and 1896-2410.
- `python scripts/make_digest.py --check` printed `DIGEST CURRENT` at the start of this review. The researcher's "STALE" remark is superseded.
- Also read: `CLAUDE.md`, `MILESTONE.md`, `reports/ledger.md` (tail), and `proposal-r1.md` with its five scripts.
- Not read: other proposals' review files.

## Claim under review
Problem B, sub-items B2 (area coefficient) and the normalisation half of B1.

The current ledger text, quoted from appH `sec:status-B`: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived."

Problem F, also touched, reads: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion."

The Chapter 17 critical-path set at `sec:ch17-done` is A, B, C, D1, E, F, G-derived, N. It is unchanged, and the package proposes no label change.

The package asserts four things.
- **Cone coefficient.** With the pulled-back replica, S = (A_G/48π) Σ w tr1 Λ², with Q = 0 in all sectors.
- **Choice of cone.** A cone carried by a singular Poisson structure gives −1/2 times that result.
- **Basis dependence.** The "coefficient of R" is basis-dependent.
- **No-go.** A bounded no-go for G_T = G_A (the tensor-block action coefficient against the area coefficient) in the Poisson/Feynman/one-loop/Λ² class.

## Checks performed
- **Scripts.** I re-ran all five scripts; all outputs match the researcher's.
  - `cone_checks.py`: (1/12)(1/n − n) = −0.125 and −0.2222 at n = 2, 3; (1 − n∂n) gives 1/6.
  - `operator_identities.py`, `verify_E_torsion.py`: residuals about 1e-16.
  - `tt_quadratic_forms.py`: eigenvalues −1/4, −1/4, −3/4 for ρR[g_ρ] and 1, 1, 1 for ρ²X.
  - `sector_table.py`.
  - I wrote no new script. These are checks, not proofs.
- **Cone coefficient, by hand.** I re-derived (1 − n∂n)[(1/12)(1/n − n)] = 1/(6n), giving 1/6 at n = 1. With ln Z = ½∫ds/s Tr K this yields S = A/(48πε²) per real component. Together with 1/G_ind = 1/(12πε²) this is the standard Sakharov/Solodukhin balance.
- **Contact-term sign and size.** I fetched arXiv:1104.3712 and extracted the text; eq. (322) reads S_BH = S_ent − Q and eq. (323) gives Q = 2π ξ ⟨φ²⟩ summed over fields (the extracted text drops the symbols).
  - Eq. (321) has the induced G with the factor (1−6ξ). That is consistent with the proposal's ΔS = −ξA/(8πε²) = −2πξA⟨φ²⟩ when the delta of R is continued into E.
  - So "S" without the delta equals S_ent = S_BH + Q, and the proposal's convention is consistent with Solodukhin's.
- **Singular-ρ ratio.** −½□ln ρ = π(1−n)δ = ¼R_sing, so Q = 1/4. The ratio (1/6 − 1/4)/(1/6) = −1/2 is pure arithmetic, and the script's direct summation agrees. This item is conditional and not used in the identification.
- **Torsion-basis identity.** The Weitzenböck identity is already merged in appH, and the script confirms E_s = R_G/4 + T²/16 + TT'/8 on random two-jets.
- **TT reconciliation (claim 4).**
  - 005's merged paragraph gives the form −(Λ²/32π²) ρ̄²p² (1 − N_tot/24) M on the two TT-type modes. That is (N_tot/6)(−1/4) + 1 = 1 − N_tot/24, matching the merged text.
  - Matching to c ρR (eigenvalue −c/4) gives c_T = N_tot/6 − 4.
  - Then 1/G_T = (N_tot − 24)Λ²/(12π) and 1/G_A = N_tot Λ²/(12π), so the difference is 2Λ²/π. I confirmed this by hand.
  - For δρ = 0, G = ρ̄ g_ρ, so ρR[g_ρ] equals √G R_G at quadratic order. The identification is legitimate.
- **Jacobson.** I extracted the PDF of arXiv:1505.04753. Eqs. (22), (24), (27) exist and have the stated roles (δA at fixed volume, tensor equation, G = 1/(4ħη)). The tensor-equation step and its conditions I did not verify further.
- **Cross-check against ch06/ch07.** Prop. `prop:ward` has coefficient κ/(8πG_eff) on δA. Eq. `eq:deltaA-G` has a unit coefficient on E[T], and `eq:Top-improved` has a unit coefficient on E. The "Einstein terms cancel" step therefore equates unit coefficients under the identification h = T. The ch07 bridge says the prefactor of the action is "still a symbol G_eff".
- **Anchors.** Each is a single occurrence and I verified them.
  - appH l. 139-140 ("Those inputs are not supplied by the displayed microscopic action") occurs once.
  - appG l. 24-26 occurs once.
  - ch07 l. 319-320 ("borrows a geometric identity used in Jacobson's argument") occurs once.
- **Labels.** The labels used all exist: `sec:status-F`, `sec:status-B`, `ass:emergent-op`, `thm:Geff`, `eq:universal-R`, `eq:first-law`, `eq:first-law-zero`, `eq:deltaA-G`, `eq:Top-improved`, `eq:mass-identity`, `prop:ward`, `ass:EE`, `thm:mT`, `eq:W-again`, `rem:ch3-trace-quadratic`, `ch:entanglement-equilibrium`, `app:modular`. The macros `\LUV` and `\Geff` are defined. booktabs is loaded. No new labels are added and no label is changed.
- **BibTeX.**
  - Solodukhin2011: BibTeX record: VERIFIED. Crossref confirms title, Living Reviews in Relativity, vol. 14, issue 1, article 8, 2011; the arXiv number is confirmed from the PDF header.
  - SusskindUglum1994: BibTeX record: VERIFIED. Crossref confirms PRD 50(4), pp. 2700-2711, 1994; the arXiv abstract page confirms the title, authors and hep-th/9401070.
  - Both keys are unique in `bib/`; the only match in the repository is Jacobson2016.

## Findings

**F1. Major (required). appG replacement sentence, convention of the conical delta.**
- *Finding.* The new text says that for E = E_0 + QR "the replica entropy differs from Area/(4G_eff) ... by a contact term ∝ tr Q". That is true only if the conical delta of R is not continued into E. If it is continued, the entropy equals the Wald/Bekenstein–Hawking value, i.e. S_BH, and the difference vanishes. The proposal's own appH paragraph says exactly this ("if R_G is continued ... the entropy changes by −Q"). As written, the appG sentence could be read as contradicting the cone literature and the appH paragraph.
- *Adjudication of "false".* The old sentence ("prefactor ... from the Seeley–DeWitt coefficient that multiplies the deficit ... the standard result") is overgeneral and ambiguous, not demonstrably false. Read with the delta included, it is the standard S_BH statement. I do not treat it as a PRIOR-CLAIM-ERROR.
- *Action.* Use the corrected snippet below.

**F2. Major (required). appH no-go sentence, scope clause.**
- *Finding.* The final no-go sentence ("for every N_s and every Λ_v > 0") rests on c_A = N_tot/6, which holds only for the pulled-back replica (I). The paragraph just above shows that the area coefficient depends on the replica choice (−N_tot/12 for the singular-ρ replica). A reader could take the no-go as replica-independent.
- *Action.* Add to the no-go paragraph: "for the replica of the first paragraph". The class should also be named in that sentence: Poisson limit, Euclidean, background Feynman gauge, one loop, Λ² term, δρ = 0 modes.
- *Note, arithmetic from the proposal's own numbers.* Under replica (II) the area coefficient is negative for N_tot > 0, whereas c_T > 0 needs N_tot > 24. The no-go therefore survives (II) for positive G_T. Equality c_T = c_A^(II) would need N_tot = 16, i.e. negative G. This is not a claim for the manuscript, only a check that the no-go is not an artefact of replica (I).

**F3. Minor (required). ch07 inserted sentence.**
- *Finding.* "an input of the theorem in addition to m_T = 0" is illogical: m_T = 0 is the conclusion, not an input. Also, the unit-coefficient equality is literally contained in the displayed forms of `eq:Top-improved` and `eq:deltaA-G` (Hypotheses 5 and 6 as written). It is not hidden in the sense of being false; it is unflagged as a physical condition.
- *Adjudication of (b).* This is a transparency clarification, not an error: thm:mT is a valid conditional statement. No PRIOR-CLAIM-ERROR.
- *Action.* Use the corrected snippet below. The statement that the Ward identity cannot be satisfied if the coefficients differ is not needed and is omitted.

**F4. Minor (required). appG Status sentence.**
- *Finding.* l. 53-54 ("The area term in S_D is the standard heat-kernel result") stays overgeneral directly after the corrected sentence. Restrict it as shown in the corrected snippet below.

**F5. Minor. appH first paragraph.**
- *Notation clash.* "coefficient of δA is the Λ² coefficient ... A = 1/(12π)" uses A for both area and the coefficient of `eq:Geff-structure`. Write "the coefficient A of Equation~\eqref{eq:Geff-structure}" or use \mathcal A.
- *Variables.* The sentence "S = A_G/(4G) with that G" should say "in the variables (G, ρ, ∂Θ) of the contact-term paragraph".
- *Closing sentence.* The first paragraph has no scoped closing sentence. CLAUDE.md asks for one per paragraph; the second paragraph does close, so the paragraph could end with a short scope clause pointing to the closing sentence of the second paragraph.

**F6. Minor. Singular-ρ replica (II) in appH.**
- *Finding.* The statement of the −1/2 result relies on choosing the m = 0 branch, which is regular in the lifted unbranched chart. I did not independently re-derive the Bessel/branch analysis. The local a_1 argument (ratio −1/2 from Q = 1/4) is independent of it.
- *Action.* Add "(not used below)" next to the (II) result, or soften "checked by direct summation".

**F7. Not an error. thm:Geff and ch08 (claim 3).**
- *Finding.* The basis dependence is real. R_G, T²/16 + TT'/8 and V² are linearly dependent modulo total derivatives (merged Weitzenböck identity). The bulk density is basis-independent as a function of Θ. What changes is which terms count as "explicit R" and hence the cone prescription. No merged statement is false, because thm:Geff says "specified endomorphism" and the merged 005 paragraph states its variables.
- *Action.* Leaving ch08 unedited and recording the follow-up is acceptable; I agree with the proposal's own recommendation.

## Scope of what is established
- **Established (identities / derivations).**
  - The flat-cone coefficient and S = A/(48πε²) per component.
  - S = A/(4G_ind) for Q = 0.
  - ΔS = −2π tr Q⟨φ²⟩ A, consistent with Solodukhin (322)-(323) and (321).
  - E_s = R_G/4 + torsion².
  - The TT arithmetic c_T = N_tot/6 − 4, c_A = N_tot/6 and 1/G_A − 1/G_T = 2Λ_v²/π.
- **Conditional, and the class is restricted.**
  - (I): the pulled-back replica with bounded E and ω on the cover. No uniform remainder estimate is given; that is flagged.
  - (II): block class, regular branch at m = 0.
  - The Jacobson reduction (m_T = 0 and G_T = G_A), which depends on the Fierz–Pauli structure and on reading T^op as the metric response of the quadratic action.
  - The no-go for G_T = G_A. Its hypothesis class is: Poisson limit; Euclidean section; four matrix coordinates; bosonic content N_tot = N_s + 2; Feynman background gauge; one loop; Λ² term only; replica (I); constant Θ̄ and the δρ = 0 modes. The researcher lists the within-core relaxations; I agree with that list. Content, non-minimal gauges, Moyal corrections at the cutoff, Φ–a mixing and curved backgrounds are not excluded. The off-shell form is gauge dependent.
- **Open.**
  - Ass:EE, off-shell stationarity, the map Θ → G, and any G_eff value or sign.
  - Whether the ghost-weighted cone sum is a physical entropy (edge modes).
  - Whether the matrix algebra has an area law.
- **Classification.** PROGRAMME-CONDITIONAL. Problem B remains OPEN and CRITICAL PATH. Problem F remains OPEN. Spacetime stays emergent: the cone sits on G, which is built from Θ, and nothing fundamental is added.
- **Breakthrough.** Not warranted. No critical-path step is derived.
- **Emergence.** No REJECT trigger: the metric stays composite and the work is on emergent G.

## Recommended disposition
Revise, then integrate with the researcher's 3-package structure unchanged (appH sec:status-B, appG, ch07, two BibTeX records). Apply F1 to F4 as required; F5 and F6 are minor edits. The package is coherent: all parts depend on the same computation, and the touched appG and ch07 passages are exactly the two statements the result affects. Proposed ordinal 15.

## Corrected snippet
No new physics beyond the proposal's own appH paragraph (the two prescriptions for the delta).

**appG, replacement for the two sentences:**

```latex
with the prefactor given by the Seeley--DeWitt coefficient that multiplies the
deficit. This is the standard cone computation for operators whose
endomorphism contains no explicit curvature coupling, on a replica geometry on
which the connection and the endomorphism stay bounded. For
\(E=E_0+QR\) with the conical delta of \(R\) not continued into \(E\), the
replica entropy differs from
\(\operatorname{Area}(\Sigma)/(4G_{\mathrm{eff}})\), with
\(G_{\mathrm{eff}}\) the curvature coefficient of Theorem~\ref{thm:Geff}, by
a contact term proportional to \(\operatorname{tr}Q\); if the delta is
continued into \(E\), the difference vanishes. For operators built from a
composite metric the curvature coefficient depends on the independent variables
chosen (Section~\ref{sec:status-B}). Chapter~\ref{ch:entanglement-equilibrium}
and Appendix~\ref{app:modular} use \(1/(4G_{\mathrm{eff}})\) as the name of
the coefficient of \(\delta A\).
```

**appG Status sentence:**

```latex
The area term in \(S_D\) is the standard heat-kernel term for the operators of
Section~\ref{sec:replica-cone}.
```

**ch07, inserted after "argument.":**

```latex
The cancellation of the Einstein-operator terms
in~\eqref{eq:mass-identity} also uses that the coefficient of
\(\mathcal E_{\mu\nu}\) in the stress response~\eqref{eq:Top-improved}
equals the coefficient of \(\mathcal E_{\mu\nu}\) in the area
term~\eqref{eq:deltaA-G}. This equality is part of the content of
Hypotheses~5 and~6 as written; it is not supplied by Hypothesis~4 or by the
identification of the area prefactor with \(\Geff\)
(Section~\ref{sec:status-B}).
```

**appH, no-go paragraph.** Insert after "whereas the area coefficient above is \(c_A=N_{\mathrm{tot}}/6\)":

```latex
for the replica of the first paragraph
```

Add also, in the same paragraph: "in this class (Poisson limit, Euclidean section, background Feynman gauge, one loop, \(\LUV^2\) term, the two modes with \(\delta\rho=0\))".

**Extra assumptions.** None beyond the proposal's own appH paragraph.

Files:
- C:\Users\redgi\Projects\namcg-lab\proposals\015-entropy-action-identity\proposal-r1.md
- C:\Users\redgi\Projects\namcg-lab\chapters\appG-sector-entropy.tex
- C:\Users\redgi\Projects\namcg-lab\chapters\ch07-massless-tensor.tex
- C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex
