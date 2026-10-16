VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: M2 | FLAGS: none | PROGRESS: first | OPEN: 0/3

## Verdict
The core algebra is sound and the scope is mostly well hedged. Three wording fixes are required before the insert is accurate. One misstates what the "preceding paragraphs" do. One calls a chosen self-adjoint extension "the domain of the first-order operator". One omits the continuation-uniqueness hypothesis from the stated conditions.

## Source reading
- This was not a full scan of every file, and I do not claim one.
- Read in full: `chapters/appH-microscopic-proofs.tex` (all 2485 lines, including the integrated 017 and 018 blocks and the `sec:status-B` header) and `chapters/ch17-agenda.tex` (all 790 lines).
- For every other `chapters/*.tex`, I grepped for fermion, Dirac, antiperiodic, gluing, polar frame, `Tr rho`, `n_D` and `Q_10`. The only hits were `ch02:499-501` (spinor bundles deferred) and `ch16:180` (fermions in a falsifier). Neither interacts with the insert.
- Round 2 should complete the remaining files to satisfy CLAUDE.md 3(c)/(d).
- Digest: `--check` prints DIGEST CURRENT. The working tree is dirty (017, 018, BenArous1989), as announced.
- I read the proposal and `appH_insert.tex` in full and re-ran all five scripts.
- Anchors: the replace sentence "The gluing selected by the matrix state is not determined here." occurs once. The insert anchor "…or the Kaluza--Klein sector. Problems~B, C, D, F and~G remain open." occurs once, directly before `\section{Problem C…}`. `\LUV` is defined at `namcg-book7.tex:54`.
- Not verified: Steinacker 2303.08012 (`V_4`; only numerically matched), Nishioka-Yaakov, Solodukhin beyond the equations 017 already verified.

## Claim under review
Problem B, sub-gap `G_T` vs `G_A` of the integrated 017 block. Problem A supplies the replica gluing from the modular flow. Current Appendix H labels, quoted verbatim:
- Problem B: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived."
- Problem A: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL."
- Chapter 17 `sec:ch17-done` requires A, B, C, D1, E, F, G-derived and N. H, I and J are optional.

Claims in the package:
1. Under a quasi-free state with rotational modular flow, `Tr rho^n` gives polar-frame antiperiodicity and Cartesian monodromy `-e^{2 pi i n sigma}`. The k-sum is `(n^2-1)/(12n)`, and `c_A(Dirac)=1/3`, so `c_A-c_T=4-n_D`.
2. 017's "periodic" branch is not `Tr rho^n`.
3. The rotated-vector branches are not continuations of `Tr rho^n`.
4. `N_tot` and `b` are the orders `alpha^0` and `alpha^2` of the `Q_10` character, and the first surviving order is `alpha^4`.

## Checks performed
Direct verification:
- **Casini-Huerta (arXiv:0905.2562).** The text states the last entry `(-1)^{n+1}`, twists `e^{i2πk/n}`, `k=-(n-1)/2..(n-1)/2`, "roots of `(-1)^{n+1}`", and `rho^n` as a rotation by `2πn`.
- **Fursaev-Miele (hep-th/9605153).** Eq. 4.4 gives antiperiodic in the polar tetrad, and eq. 4.6 gives `-e^{iσ3β/2}`. After 4.11 the text says the phase choice is possible for `β≤2π` and larger `β` goes "by analytical continuation". This supports the Dirac-domain analytic branch.
- **Manta-Steinacker-Tran (arXiv:2411.02598), opened.**
  - Eq. 3.7 defines `Q_10` as the trace over R of `e^{iΣ^V F} − (1/2)e^{iΣ^Ψ F} − 2`.
  - Eq. 3.8 gives the 4+6 split `Ψ = (2_-⊗4_-) ⊕ (2_+⊗4_+)`.
  - Eq. 3.9 is the factorised form.
  - Eq. 3.10 gives `χ^(4)=4−2α²F²+…` and `χ^(2)=2−(α²/2)F²+…`.
  - The paper states "the expansion of Q10 starts at O(α⁴) as a result of maximal supersymmetry". The identification is verified.
- **Scripts.**
  - `twist_ksum.py`: phases `(-1)^{n+1}`; periodic = antiperiodic set for odd n and = graded set for even n; graded `a=1/2` at n=1; `sum a²=(n²−1)/(12n)`; `(1−n∂n)F|₁=−1/6`; ratio −2 at odd n; rotated vs unrotated vector `13/24` vs `1/24` at n=2.
  - `q10_check.py`: orders 0–3 vanish; order 4 is −3/8 `V_4`; the closed form gives `8−4n_D`, `(n_D−2)(x²+y²)/2`, and `(x²−y²)²/16` at `n_D=2`.
  - `gap_fixed.py`: `4−n_D`, with `(c_T,c_A)=(0,2)`.
  - `holonomy_check.py` and `w4_check.py`.
  - These are checks, not proofs.
- **Independent re-derivation of the tip-domain step.**
  - The componentwise-regular value per two components is `a²−a`. The 2D scalar check gives `(1−n²)/(12n)`, as expected.
  - Reversing the one lower Bessel order from `+a` to `−a` shifts the Cheeger term by `+a`. This gives `a²`.
  - The k-sum matches the CH 2D `c=1` result.
  - `c_A(Dirac)=(−1)(2)(−1/6)=+1/3`, matching Solodukhin.
  - `c_A=8/6+2/3=2`, and `c_T=4n_D/3−8/3=0`. Both are correct.
- **New observation, not stated by the researcher.** I computed `Σ|a_k|` for the antiperiodic set. It is `n/4` for even n and `(n²−1)/(4n)` for odd n. So the componentwise-regular domain gives a parity-dependent, non-analytic `Tr rho^n`. This independently supports the Dirac-domain analytic branch, but the selection is a choice of extension and must be worded as one.

BibTeX records:
- `CasiniHuerta2009`: Crossref gives Casini and Huerta, "Entanglement entropy in free quantum field theory", J. Phys. A 42 (2009), no. 50, article 504007, DOI 10.1088/1751-8113/42/50/504007. arXiv 0905.2562 fetched. BibTeX record: VERIFIED. Optional: add `number={50}` and the article number.
- `FursaevMiele1997`: Crossref gives "Cones, spins and heat kernels", Nucl. Phys. B 484 (1997) 697–723, DOI 10.1016/S0550-3213(96)00631-1. hep-th/9605153 fetched. BibTeX record: VERIFIED.
- Both keys are currently absent from `bib/namcg.bib` (count 0). The integrator adds them; `MantaSteinackerTran2024` exists.

## Findings
**F1 (major). Location: insert para 1, first sentence.**
- Finding: "acting on every field through its representation of the rotation group, as in the replica of the preceding paragraphs" is inaccurate. The merged 017 text says the Dirac gluing "is not the unrotated pull-back gluing used above for a^μ". The preceding paragraphs use the unrotated gluing for a^μ and give the rotated one only as an alternative.
- Required action: delete "as in the replica of the preceding paragraphs". Add "(for integer spin this is the identity at integer n)".

**F2 (major). Location: insert para 1, "the domain of the first-order operator γ^μ D_μ".**
- Finding: the first-order operator on the cone is not essentially self-adjoint for `0<|a|<1`. The "less singular" extension is a choice, which the proposal itself calls conditional (§1d). The LaTeX presents it as "the" domain.
- Required action: write "the less singular self-adjoint extension of the first-order operator". Add that the componentwise-regular domain gives a parity-dependent, non-analytic `Tr rho^n` (`Σ|a_k| = n/4` or `(n²−1)/(4n)`). Keep the extension choice in the final conditional list.

**F3 (major). Location: insert, final conditional sentence and the "do not apply" / "not continuations" sentences.**
- Finding:
  - The list of conditions omits uniqueness of the continuation from integer n (a Carlson-type uniqueness, assumed, not proved). The exclusion of the rotated branches rests on it.
  - "Its values −2/3 and 4−2n_D do not apply to Tr ρ^n" is domain-conditional. At odd n the periodic set is the `Tr rho^n` set with the regular domain.
- Required action: add "uniqueness of the continuation from integer n" and "the tip-domain choice" to the list of conditions. Phrase the exclusion as "do not apply for the stated extension".

**F4 (minor). Location: replacement sentence.**
- Finding: "stated below" is followed by two paragraphs, one of which is the rotated-index paragraph.
- Required action: no change needed. Optionally split the long first insert paragraph in two.

**F5 (minor). Location: `bib/namcg.bib`.**
- Finding: the CH record lacks `number`.
- Required action: optionally add `number = {50}`.

**Checked, no finding.**
- **Emergence.** The wedge, rotation and cone are built on the emergent `G` of the preceding paragraphs. No background metric is made fundamental. REJECT is not triggered.
- **PRIOR-CLAIM-ERROR / M3.** No merged 017 sentence becomes materially false.
  - 017 presents periodic gluing only as an alternative and states that the gluing "is not determined here".
  - 019 conditionally resolves that statement and relabels the alternative.
  - 017's final "2 for antiperiodic and 0 for periodic" stays as a report of alternatives.
- **Overreach.**
  - The LaTeX makes no `a_2` or `W_4` claim; `W_4` stays in the proposal only, as the proposal itself asks.
  - The LaTeX does not assert the identification of the α⁴ vanishing locus with 018's `f1=f2`; keep it out.
  - The self-dual statement itself is correct: eigenvalues `±ix, ±iy` with `|x|=|y|` are (anti-)self-dual.

## Scope of what is established
- **Established (algebra, verified).**
  - The frame/phase relation. Polar antiperiodic under `2πn` is Cartesian `−e^{2πinσ}`.
  - The twist sets and the k-sum.
  - Periodic = `Tr rho^n` at odd n and graded at even n.
  - The graded trace is not normalised at n=1.
  - `c_A−c_T=4−n_D`, giving `(0,2)` at `(2,6,1)`.
  - `N_tot` and `b` are the orders `α⁰` and `α²` of `Q_10` (MST eq. 3.7, verified). The first survivor is `(x²−y²)²/16` at `n_D=2`. This is a character statement only.
- **Conditional.**
  - Quasi-free state and rotational modular flow (Problem A).
  - The less-singular extension (the mode-by-mode derivation is consistent with CH and FM; it is not operator-theoretic).
  - Carlson-type uniqueness.
  - The `Lambda²` order, the content `n_D=2`, `N_s=6`, and the Poisson/Euclid/one-loop class.
- **Not established.** The state, the flow, the vector and ghost tip domains, `ass:EE`, a value or sign of `G_eff`, and the A-side next order.
- **Classification.** Problem B stays OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. No label change is proposed. This is a bounded sharpening of a bounded no-go within hypotheses H1–H10 of the proposal. It is not a breakthrough.

Open avenues after this no-go, ranked:
1. **Contact/edge terms of weight `n_D=2` at order `Lambda²`.** The whole remaining gap is the spin term, +1 per Dirac (a Lichnerowicz-type `−R/4` endomorphism or edge modes). This relaxes H10 (conical-only area coefficient).
2. **A-side next order on a curved `J=0` leaf**, compared with the T-side structural survivor. The `W_4` claim is conjectural; E and Ω were not re-derived. This relaxes H4 and H8.
3. **Vector, ghost and scalar tip domains.** These fix the `α`-dependence and the R-holonomy kink. They relax H6.
4. **Non-rotational modular flow or a non-quasi-free state, and Moyal corrections.** This relaxes H7 (Problem A).
5. **Non-flat `J=0` backgrounds** to test the lemma and the tip conditions.

## Recommended disposition
Revise F1–F3 (a wording-only change), then integrate the insert and the one-sentence replacement. Complete the unread chapters in the next round. Treat the `bib/namcg.bib` additions as an integrator step.

## Corrected snippet (wording only; no new physics)
- Sentence 1: "…acting on every field through its representation of the rotation group (for integer spin, the identity at integer \(n\))."
- Replace "and the domain of the first-order operator \(\gamma^\mu D_\mu\), whose square is \(\mathcal O_f\)" with "and the less singular self-adjoint extension of the first-order operator \(\gamma^\mu D_\mu\), whose square is \(\mathcal O_f\), which is the one giving an analytic continuation (the componentwise-regular domain gives \(\sum_k|a_k|\) equal to \(n/4\) or \((n^2-1)/(4n)\) by parity of \(n\))".
- Replace "its values \(-\tfrac23\) and \(4-2n_D\) do not apply to \(\operatorname{Tr}\rho^n\)" with "for the stated extension its values \(-\tfrac23\) and \(4-2n_D\) do not apply to \(\operatorname{Tr}\rho^n\)".
- Final conditional list: after "the domain of the first-order operator" insert "the choice of self-adjoint extension, the uniqueness of the continuation from integer \(n\),".

Relevant files:
- `C:\Users\redgi\Projects\namcg-lab\proposals\019-fermion-replica-gluing\proposal-r1.md`
- `C:\Users\redgi\Projects\namcg-lab\proposals\019-fermion-replica-gluing\appH_insert.tex`
- `C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex` (lines 188–191, 193)
- `C:\Users\redgi\Projects\namcg-lab\bib\namcg.bib`
