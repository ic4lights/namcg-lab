VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/3

## Verdict
The exact algebra is verified and reproduced, and the two readings are correctly separated in substance. The insert needs six verbatim scope and wording edits before it can be accepted. Without them the averaged-frame c_A − c_T = 0 reads as a result before the sentence that says it is not the fibre trace. The index-density transfer, the restriction to inert = 0, and the notion of "covariant" are also stated too weakly.

## Source reading
Digest plus targeted reads. This is not a full scan, and I did not claim one.
- `make_digest --check` printed `DIGEST STALE (head changed)`. The only HEAD change is the 045 proposal commit. Chapters are dirty with the accepted 043/044 integrations, so CLAUDE.md 3(d) applies and I read the affected passages directly.
- Read in full from `chapters/appH-microscopic-proofs.tex`:
  - the 044 paragraph (L2370–2391) and the Casimir paragraph (L2365–2368);
  - the CP^{1,2} level-one passages (L2116–2164), including the fibre-integrated response, Q = Σ s_i s_i, and the six polarisations at null q;
  - the Problem B ledger label and normalisation paragraph (L44–50, L174–179);
  - the gauge, fermionic-content and cone paragraphs (L181–192);
  - the Problem C entry (L400–420);
  - the Problem F ledger label (L1365–1384).
- Read in full from `chapters/ch17-agenda.tex`: the Problem C passage (L139–157), the order of work, and `sec:ch17-done` (L691 onward).
- The labels `sec:status-B`, `ch:vierbein-emergence` and `ass:lorentzian` each occur once.
- `proposals/044-rank6-class-transfer/review-r2.md` was read. `review-r1.md` was not re-read in full.
- The Steinacker PDF was fetched and extracted with pdftotext. I read §7 through §7.2.2.
- `compile_check` was not re-run. I relied on the saved output (321 → 323 pages, 0 undefined refs/cites, 0 multiply defined labels).

## Claim under review
CP^{1,2} × K at IKKT content: frozen-fibre leading symbol, hybrid fibre treatment, Poisson limit, one loop, formal Lorentzian η.
- Rank-one frame perturbation δE^{aμ} = α^a v^μ, δT = −m v(q∧α), X = m⁻⁴ v²(q²α² − (q·α)²).
- Averaged-frame reading: X = −2EH + k(tr h̄)² and a₁ = EH/6 + k′(tr h̄)². This gives c_T = W_R/6 − 2W_X on the five traceless polarisations and c_A − c_T = 0 (fixed-state, finite parts).
- Fibre-trace reading: a bounded no-go for a single G_T.

Target statuses, quoted verbatim:
- Problem F (appH): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion."
- Problem B (appH L44–47): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived."
- Problem C (appH L403–407): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. A scalar-tensor result is a reduced-scope outcome only when its operator, coupling and phenomenological test are supplied; it does not by itself meet the matrix-derived criterion."
- The Chapter 17 `sec:ch17-done` set is A, B, C, D1, E, F, G-derived and N, and Appendix H agrees. No discrepancy.

## Checks performed
**Re-runs**
- I re-ran s1 (1 m 07 s), s2 (1 m 25 s) and s3 (3 m 12 s) in the proposal folder. Each output is byte-identical to the saved `.out.txt`.
- s1 covers the bracket sign, the exact background {T,y}, the invariant quadric (4e-14), the fibre basis, and δE, δF, δT against the closed forms at 12 random points, relative residual ≤ 3e-14. It finds no higher powers of λ.
- s2 covers EH2 against a direct curvature computation (both signatures), the −4 and 1/6 calibration in four coordinates, and the seven CP^{1,2} cases.
- s3 checks the fibre average by Monte Carlo and by an exact design. It checks the realisation basis and the eigenvalues. It is not independent of the pointwise closed forms used in s2.
- I read s4 and its output. I checked the arithmetic of every gap entry in the insert by hand. Fixed, periodic and smooth gaps on the five traceless polarisations and on the trace polarisation are all correct.

**My own derivations**
- Averaged torsion. Averaging δT = −m v(q^aα^b − q^bα^a) gives −m(q^aH^{bμ} − q^bH^{aμ}) with H = ⟨δE⟩. This is linear in the averaged frame.
  - For symmetric transverse H the totally antisymmetric part vanishes.
  - The vector part is ∝ q^b tr H.
  - Antisymmetric H (the inert amplitudes) gives axial torsion.
  - This agrees with s2.
- Index form on TT. For symmetric transverse traceless H, the index form is X = m⁻⁴ q²H·H. Using EH2 = −½ m⁻⁴ q² H·H for TT, X/EH = −2.
  - The calibration is consistent with 044's −4: the missing −2 is exactly the absent axial torsion, which 044 stated in words ("one half and the axial torsion the other").
  - On the trace polarisation (h̄ ∝ P_{q⊥}) the same formulas give X/EH = +1, as s2 reports.
  - On the traceless five, "single c_T" follows from Lorentz covariance of a torsion-squared form in the averaged frame. The non-trivial inputs are the coefficient −2 and the cone values.
- Scalar density. I re-derived the conformal step. With ĝ = |det G|^{-1/2}G, ρR[ĝ] = ρ√G(R[G] − 6□φ − 6|∂φ|²), so (1/6)√G R[G] − √G|∂φ|² mod total derivatives is correct.
- Second-order terms.
  - The second-order metric γ^{(2)} enters only through the first variation of ∫R, which is a total derivative.
  - The T̄·δ²T and T̄·δT·δG terms are of relative order 1/(|q|ℓ).
- Fibre trace. For a multiplication operator on the fibre S², the trace is the SU(2)-invariant average, so the pointwise densities are averaged and ⟨X⟩ ≠ X(⟨E⟩). The second-harmonic origin of the non-covariance is real.
- Preferred vector. The model S_i depends on v̂ = y/ℓ (the cosmic time direction). The fibre therefore breaks Lorentz invariance at O(1), consistent with merged L2366, "no point of the leaf is fixed by the matrix Lorentz group".

**Merged-text consistency**
- Notation matches merged L2121 and L2148–2158: the rank-6 response, h̄ = fibre-integrated δK, s_i^μ = S_i^{μρ}q_ρ, and the 3 + 3 + 6 split of the twelve amplitudes.
- The averaged frame is the same object as the merged "fibre-integrated tensor".
- No merged sentence becomes false. The 044 sentence "its two-derivative density … not computed" describes that paragraph's scope, and the supplement pattern matches L2117.
- The 044 statement "mixed-term part of the gap would vanish for tensor modes that source neither axial nor vector torsion" is what the five traceless polarisations realise in the averaged-frame reading. It rests on the same non-derived equality of values that 044 states.
- No PRIOR-CLAIM-ERROR.

**Steinacker 2303.08012 (fetched, pdftotext)**
- (7.5): m_s² = 3s/R², called "an IR mass in the late-time regime". Verified.
- §7: "hybrid way … finite tower of hs harmonics on S², then semi-classical trace on M". Verified.
- §7.1.2: the mixed S²–M term is "sub-leading compared with those from K". "The contractions of the torsion via k̃ is not Lorentz invariant a priori, reflecting the presence of a time-like vector field." The suppression condition is (7.14), c_K² m_K² ≫ 1/R². Verified.
- (7.21)–(7.22): the weights are (2s+1)C₂ with denominators containing m_s²/m_K². Equal weight on harmonics therefore holds for m_s² ≪ m_K², and (7.25) states exactly this. Verified.
- (7.21) writes T^μT^νG_{μν} for a single frame on M^{3,1}. The proposal's remark that the fibre dependence of fluctuations is not examined there is fair.
- The identification of level-one amplitudes with the graviton is correctly not asserted. Steinacker's G_N normalisation and his fibre averaging of hs fluctuations were not independently verified.

**Insert mechanics**
- Python byte check on `appH_insert.tex`: 7691 bytes, 0 CR, 0 TAB, 0 non-ASCII, 0 controls other than LF.
- Braces net 0. `\(` `\)` balanced, `\[` `\]` balanced.
- One `\paragraph`, no `\label`.
- Refs `sec:status-B`, `ch:vierbein-emergence` and `ass:lorentzian` exist once each. Cite key `Steinacker2023` exists once in the bib. `\LUV` is defined in `namcg-book7.tex` L54.
- `\section{Problem G: HBEV}` occurs once (L2393). The line before it ends "…Problems~B and~F remain open and PROGRAMME-CONDITIONAL.", and L2391 is the 044 paragraph, so the anchor is correct.
- No process language. The title fragment is not duplicated.
- The closing status sentence repeats the 044 closing. Consecutive repeated closings are the convention in this ledger (L2114, L2123, L2128, L2146, L2164), so I do not require a change.

## Findings

**1. Major (scope). Location: "Two-derivative forms", the "Hence …" sentence.**
- Finding: c_T = W_R/6 − 2W_X and "c_A equal to c_T on the five traceless polarisations" are stated before the text says they hold only for the fibre-averaged frame. They are not the fibre trace. The text also does not say that the equality inherits the cone-value equality that 044 explicitly says is "an equality of the two values, not derived".
- Required action: apply replacements R1 and R2 below.

**2. Major (scope). Location: "Frame and torsion" / "Two-derivative forms".**
- Finding: the index density at a fibre point is taken as √G G_{μν}ηηTT, the 4-coordinate-class normalisation of ρ²X. This is carried over to the leaf CP^{1,2}. It is calibrated only in the four-coordinate class (s2 (1)), not recomputed for CP^{1,2}. 044 says the CP^{1,2} density is "not computed". The coefficient −2 depends on this identification.
- Reason: the transfer is plausible, because the first-order term of the Dirac square is the frame anholonomy, which is the torsion. It is not an established identity.
- Required action: apply R3.

**3. Major (scope). Location: "Fibre trace".**
- Finding (a): the no-go and the eigenvalues are for the quadratic form restricted to the six polarisations with the inert amplitudes set to zero. The text says only that the inert amplitudes are coupled to the six. s2 shows the sym–antisym cross blocks are non-zero for IX2 and SC2. A Schur-complement elimination of the inert amplitudes, which the proposal itself lists as avenue 2, is not performed. "No single G_T" therefore needs the restriction stated.
- Finding (b): "covariant" is tested only against the span of q²h̄·h̄ and q²(tr h̄)². A form that also depends on the background vector y/ℓ is not tested. That vector is a physical preferred direction of the leaf, and the fibre breaks Lorentz invariance at O(1). Proportionality to EH(h̄) is excluded in any case.
- Finding (c): "vanishes on no traceless polarisation" is imprecise. For spacelike q, EH is indefinite on the traceless transverse polarisations, so a Rayleigh quotient equal to −2 exists for some non-eigen polarisations. The correct statement is that −2 is not a generalised eigenvalue.
- Required action: apply R4, R5, R6.

**4. Minor. Location: first paragraph.**
- Finding: m = M^{45}, T^a = M^{a4} and y^μ = M^{μ5} are written without R. The merged text uses /R in places and "in units R = 1" in others. The text says "five wave vectors including a time-like one", but two of the five have q² < 0 (cases 3 and 4).
- Required action: apply R7, R8. R7 and R8 are not among the six numbered replacements in the summary line above: R1–R6 are the scope edits, and R7 and R8 are the two cosmetic ones. The total number of replacements is therefore eight. The six scope and wording edits named in the verdict are R1–R6.

**5. Minor (proposal and ledger wording only; the insert does not make the claim). Location: proposal avenue 3 and Decisions Taken 3.**
- Finding: "the mismatch is localised in the dilaton direction" and "touches C (conformal mode)" attribute the trace-polarisation mismatch to Problem C.
- The merged Problem C is the radial and pure-trace scalar of the composite metric on the locked vacuum, with its kinetic coefficient, mixing and coupling.
- The trace polarisation here is the sixth transverse polarisation of the rank-6 response. Merged L2151 notes that its trace is not removed by gauge.
- Its relation to the Problem C scalar is not established. The computation shows only that, with the cone values, the gap is non-zero there (3W_R/8 − 3W_X for fixed-state).
- Required action: any report or ledger text should say "the trace polarisation of h̄ (the sixth polarisation); its relation to the Problem C scalar is not established". The insert stays as is, since it does not attribute.

## Scope of what is established

**Established at the leading frozen symbol (algebra, verified):**
- The rank-one frame perturbation and the torsion/index closed forms (Lie–Poisson to 3e-14).
- The torsion content. The averaged frame gives no axial torsion on the six, a vector part ∝ q^a tr h̄, and axial torsion on the inert three. The fibre-resolved axial part ∝ [D, nnᵀ] sits in the second harmonic and averages to zero.
- The averaged-frame forms X = −2EH + k(tr h̄)² and a₁ = EH/6 + k′(tr h̄)² (exact rational at 7 cases, and analytically for TT).
- The pointwise fibre-averaged forms are not proportional to EH and not in the covariant span (7 sampled cases; the exact-design column of s3 agrees with s2).

**Conditional:**
- The identification of the index density with the torsion invariant for CP^{1,2}.
- The hybrid H6 evaluation.
- The cone values carried from 044, with the cone in the base at every fibre point. These include the non-derived equality −1 ↔ the coefficient in ½ρ²X.
- The formal Lorentzian η, and the IKKT content supplied by hand.

**Not computed or argued only:**
- The regime correspondence (equal-weight trace for K scale above fibre gaps; averaged forms when fibre gaps exceed the K scale). It is plausible, since for s ≫ 1/Δ the intermediate states are suppressed in the proper-time integral, but it is not computed. Nor is the claim that the averaged-frame forms are exactly the trace over fibre-constant loop modes.
- The first-term fibre-flux (S²–M) two-derivative part, the Λ² and log first-term excess, the trace polarisation, and the subleading symbol.
- K, the sign of W_R, and the replica selected by the state.

**Classification:** PROGRAMME-CONDITIONAL; nothing DERIVED; B and F remain OPEN, CRITICAL PATH. No label change.

**Bounded no-go (hypotheses H1–H9):**
- Product background without mixed flux.
- IKKT content supplied.
- Poisson limit on M.
- One loop.
- Frozen leading symbol at |q|ℓ ≫ 1.
- Hybrid fibre treatment with the fibre trace equal to the fibre average.
- The 044 cone values.
- The orientation-even mixed term.
- Formal η.
- The six carried by level-one amplitudes with the inert amplitudes set to zero (not eliminated).
- Covariance meaning invariance under the frozen-point Lorentz group without the background vector.

Under these hypotheses there is no single G_T on the six or the five. It does not close the CP^{1,2} × K route beyond them.

**Open avenues that could still favour the infrared or full-GR derivation, ranked by promise:**
1. Regime interpolation. Derive the loop fibre spectrum in this class and compute the second-order Duhamel weights. Compute the first-term fibre-flux part in the same regime. This relaxes H6 and the regime argument, and is the one route that could turn the averaged-frame result from an argument into a computation.
2. Eliminate the inert and higher-harmonic amplitudes with the tree Maxwell forms in the induced-dominated window (merged L2162). This relaxes "inert = 0".
3. Test forms that depend on the background vector y/ℓ. An Einstein term plus preferred-frame terms is not excluded by the span test. This relaxes the covariance hypothesis, but the target requires the Einstein form.
4. Replica selection and the Λ²/log first-term excess (Problem A, 044 avenue 2).
5. The sixth (trace) polarisation, with its relation to the Problem C scalar left as a question rather than an attribution.
6. The subleading symbol and the finite-fibre hypoelliptic trace beyond the hybrid scheme.
7. Non-product backgrounds, explicit K, and the sign of W_R.

**Significance:**
- This is a consequential bounded package, for three reasons.
  - It answers 044's top-ranked avenue.
  - It gives an exact torsion and index analysis of the CP^{1,2} level-one amplitudes.
  - It shows that the 044 criterion is realisable on five of the six polarisations only in a reading that the cited regime does not supply.
- The bundle is coherent: one calculation, one insert.

**Milestone and breakthrough:**
- MILESTONE: none.
  - M1 does not fire. No important remaining step of F or B is derived, because the cone values, the regime argument, the first-term parts, K and W_R are all open.
  - M2 does not fire. The no-go is within H1–H9 and in one reading. The manuscript does not keep this route open as a claimed derivation; it was only listed as an avenue in 044.
  - M3 does not fire. M4 and M5 are not claimed.
- BREAKTHROUGH: no. The traceless-sector G_A = G_T result:
  - is conditional on the averaged-frame reading, which is not the fibre trace in the cited regime;
  - is conditional on an uncomputed regime argument, on the uncomputed first-term fibre-flux and Λ²/log parts, and on cone values that are not derived;
  - does not cover the sixth polarisation, K or the sign of W_R;
  - and amounts largely to the 044 criterion with the −2 coefficient that follows from the absence of axial torsion.

  It does not derive a critical-path step. The researcher's "no milestone" self-assessment is right.

## Recommended disposition
Revise, then integrate. The edits are verbatim and add no physics.
- Apply R1–R8 to `appH_insert.tex` (r1, 7691 bytes) exactly.
- If the researcher resubmits with only these edits, only a diff check against this review is needed.
- Preserve CRLF when integrating.
- Leave the 044 paragraph unchanged.

**What is accepted:** exactly `appH_insert.tex` with R1–R8 applied, inserted as one paragraph immediately before `\section{Problem G: HBEV}` (after L2391, with one blank line). Nothing else.

## Corrected snippet
No new physics is needed. R3 adds one explicit assumption: the identification of the index density with the torsion invariant is carried over from the four-coordinate class. Each old string occurs exactly once in the insert.

**R1**
Old: `Hence, in the units \(c\) of the preceding paragraph, \(c_T=`
New: `Hence, in this averaged-frame reading, which is not the fibre trace treated below, and in the units \(c\) of the preceding paragraph, \(c_T=`

**R2**
Old: `for the finite parts, without the dressed density of the paragraph on local frame rotations.`
New: `for the finite parts, without the dressed density of the paragraph on local frame rotations; this inherits the equality of the Dirac cone value with the coefficient of the Einstein term in the index density, which the preceding paragraph does not derive.`

**R3**
Old: `for a real wave averaged over its phase, the index density at a fibre point is`
New: `for a real wave averaged over its phase, and taking the index density to be the torsion invariant of the four-coordinate class evaluated on the frame at the fibre point (an identification carried over from that class and not recomputed for the leaf \(\mathbb{CP}^{1,2}\)), the index density at a fibre point is`

**R4**
Old: `On the six polarisations neither form lies in the span of`
New: `On the six polarisations, with the inert amplitudes set to zero, neither form lies in the span of`

**R5**
Old: `makes their sum proportional to \(\mathrm{EH}(\bar h)\) or covariant (exact linear algebra`
New: `makes their sum proportional to \(\mathrm{EH}(\bar h)\) or covariant under the Lorentz group of the frozen point (a form that also depends on the background vector \(y^\mu/\ell\) is not tested; exact linear algebra`

**R6** (three edits in the same sentence)
Old (a): `For this trace no single \(G_T\) covers the six polarisations or the five traceless ones,`
New (a): `For this trace, with the inert amplitudes set to zero rather than eliminated, no single \(G_T\) covers the six polarisations or the five traceless ones,`
Old (b): `so the mixed-term part of the fixed-state gap vanishes on no traceless polarisation.`
New (b): `so the mixed-term part of the fixed-state gap vanishes on no generalised eigendirection of the traceless polarisations.`
Old (c): `the interpolation between the two regimes, or the fibre spectrum.`
New (c): `the interpolation between the two regimes, the elimination of the inert amplitudes or the fibre spectrum.`

**R7**
Old: `\(m=M^{45}\))`
New: `\(m=M^{45}\), units \(R=1\))`

**R8**
Old: `five wave vectors including a time-like one`
New: `five wave vectors including two time-like ones`
