VERDICT: ACCEPT WITH REQUIRED REVISIONS | MILESTONE: none | FLAGS: none | PROGRESS: first | OPEN: 0/5

## Verdict
The core mathematics is correct: the commuting form, the on-shell signature, the exact redefinition and E3 identity, the labels, the reading of the double zeros, the group case and the cutoff block. Seventeen printed sentences or clauses are literally false, over-read or under-scoped, so bytes must change and another round is needed. This is a review verdict, not merge approval. Only the author merges.

## Source reading
**Method: digest + targeted reads. No full scan.**

- **Ruling on the scan:** none is required at ordinal 49 (the ledger gives "Next integration is 49; the 5th-item full scan is due at 50"). I agree the package changes no definition, assumption, scope or status passage: it is a pure insertion with no label and one closing status sentence. No milestone verdict is issued.
- **Digest:** `make_digest.py --check` printed DIGEST CURRENT. `dirty-chapters: yes` comes from the 049 and 050 integrations, so I read working-tree files, per the author directive. **The next integrated item (ordinal 50) requires my full scan.**
- **Read in full:** proposal-r1.md, appH_insert.tex, MILESTONE.md, 050 review-r2.md.
- **Read in part, manuscript:**
  - appH L1340-1409, the whole 050 block
  - appH L566-572 (D label), L1405-1408 (F label), L2950-2975 (N label and missing step)
  - ch17 L700-735
  - eq:Smatrix in ch03
- **Grepped across chapters:** "negative norm", "double zero", "Jordan". The only other hits are appH L1088 and L1108, which concern other sectors and are not made stale.
- **Not read by me:** the rest of appH L2975-3084 and ch03 beyond eq:Smatrix. The 050 sme-consult-r1.md was only grepped for two arXiv numbers. Unreadable files: none.
- **Process slip:** my first tool round issued three reads, and a later round issued two, against the serial rule. Later calls were serial. Two heredocs failed in the shell wrapper and wrote nothing. All my files are in the scratchpad and `git status` is unchanged. No background job was started.

## Claim under review
**Targets (ch17):**
- D1: "an \(SO(3,1)\) gauge symmetry is derived from the matrix algebra and condensate ... The locked frame and its non-degeneracy on the claimed domain are derived, not assumed".
- N: "Assumption~\ref{ass:EFT-a2} is discharged; there is no propagating Ostrogradsky ghost for \(p<\LUV\) in the derived graviton two-point function, for the values of \(\alpha\) and \(G_{\mathrm{eff}}\) computed in Problem~F".

**Verbatim Appendix H labels:**
- D: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: D2, imposed local Lorentz symmetry, supports only a scope-limited Presentation-B model; D remains OPEN and the matrix-derived criterion is unmet."
- F: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating \(G_{\mathrm{eff}}\) as an input leaves F OPEN and does not satisfy the matrix-derived criterion."
- N: "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL."

**Claim:** at quadratic order about the flat point of the first-order class, with a bounded extension to the de Sitter group case:
- the signature of the action's pairing;
- the exact map of 40 linear equations onto ten Maxwell equations with right-invariant labels;
- the double zeros read as the nilpotent translation action on labels;
- the sign on truncations, reported as a tension;
- the cutoff 2 x 2 block;
- the unfavourable result that torsion modes stay massless and are not removed.

No label change. No closure.

## Checks performed
**Priority 1, sign (by hand; correct as mathematics).**
- X_a = -u_a^b p_b, and (p,u) -> (up,u) is unitary, so X_a is unitarily -p~_a tensor 1.
- With eq:Smatrix (prefactor -1/(4g^2), confirmed) and F = 0: Tr D^{ab}D_ab = -2 eta^{ab} Tr(A_a (EA)_b), so S_2 = +(1/2g^2) eta^{ab} Tr(A_a(EA)_b).
- On kernels, EA = Q.Q A - Q(Q.A) with Q real.
- Non-null Q gives A proportional to Q. Null Q != 0 gives Q.A = 0, and eta is positive definite on Q-perp/Q for complex A.
- In background gauge the operator is multiplication by Q.Q. Level sets are null, since Q.Q is a nonconstant polynomial at fixed u,u', so there is no eigenvector on Hilbert-Schmidt kernels.
- Finite N is diagonal. s4 parts b and f are consistent.
- **Literal error (F4):** on shell at non-null Q the gauge directions have form value Q.Q|Lambda|^2 of either sign, so "indefinite ... only off shell and at Q=0" is false without "modulo gauge".

**Attribution to Ho-Kawai-Steinacker: verified.** 2509.06646 L667-689 and L1327-1328 state positivity for quenched diagonal elements in the planar sector. L723-724 gives a_i^0, L943 c_i^+ in the minimal model, L1329-1332 "very different" and "no clear correspondence". L1334-1335 gives bilocal finiteness against tensor divergence.

**Priority 2, redefinition and labels (by hand and my own script; correct).**
- From [S,D] and the fluctuation, T_ab^c = d_a h_b^c - d_b h_a^c + w_b^c_a - w_a^c_b, and T = F + yF, R = F.
- E1 + y_g E2^{ge} = -Mx[f^e], E2 = Mx[f^{de}].
- 2E3_b = d_c E1_b^c - eta_bg E2_c^{gc}, including the Bianchi step 2 d_g F_bc^{gc} = d_b F_gc^{gc}.
- [V,D_a] = 0; the fibre part acts as -u_a^c lam_c^b; [P_g,J_lam] = -lam_g^c P_c; unit Jacobian and Haar invariance make exp(tJ) unitary.
- Count: 16 + 24 = 40 = 10 x 4; labels 1 + 4 + 6 = 11; 22 = 20 + 2.
- My `gk_id.py` uses random polynomial fields in d = 4 with its own index code and gives 0 failures, with a wrong-sign control failing. A first failure was my own contraction error, fixed and re-run.
- u-dressed pairing: eta^{ab} u_a^r u_b^s eps_r eps_s = 1 pointwise. For A + A-dagger the cross term is eta^{ab}Tr(A_aA_b), which vanishes at nonzero translation charge, so the Hermitian part has half the value. The insert does not state this (R7).

**Priority 3, double zeros (correct, and consistent with merged 050 L1379).**
- At fixed q the 14 solutions are 8 h plus 6 w with q.lam = 0. The six y-linear partners have q.lam != 0, rank 3 per polarisation (my rank check gives 3).
- e^{ik.y}exp(tJ) solves the linear equation for all t, since exp(tJ) is in the commutant.
- **Note:** u_a^r is unbounded on the non-compact fibre, so "bounded family" in proposal Section 3 applies to exp(tJ) only. The insert says "unitary", which is accurate.

**Priority 4, sign on truncations.**
- The computation is correct, with four corrections: G > 0 needs a hyperplane through the origin; h_i^0 and h_i^mu propto q^mu are positive only off such a hyperplane; omega's O was never defined; and a fibre-local O has an infinite delta(u,u')-squared factor.
- The scoping does not meet the bar. See F2 and F3.

**Priority 5, cutoff (hand re-derivation; correct as a compression).**
- Q2 = t v.p + O(t^2); int t phi phi' = -1/2; H12 = -(sigma/sqrt2) sqrt(vGv)(1 + O(sigma^2)); parity gives diagonals O(sigma^2).
- Raw-basis matrix: M_12 -> -(1/2) sqrt(vGv), M_21 = O(sigma^2), the Jordan form. Norm^2 of phi' = 1/(2 sigma^2).
- Examples: v has Euclidean norm 2 and kappa = -sqrt2 sigma P, matching s3.
- **The operator is only compressed; the probes do not span an invariant space (F1).**
- R must be the right translation of u alone: with exp(tJ) the multiplier would be k^2 = 0.
- k.lam != 0 is needed, otherwise the first probe vanishes.

**Priority 6, unfavourable results (present and correct).**
- Non-derivative cancellation on dS by hand: E_b - 3A_b with [D_a,D_b]f^a = 3f_b gives -nabla^a F_ab, and gauge invariance gives the same sign.
- Theta: only the order-zero bracket changes, even though Theta breaks the [S,D] relation (it enters only with order-zero coefficients). Singlets: unchanged.
- J-symmetry, HS symmetry when ad F_0i = 0, and neutrality all hold by hand.
- Random matrices, my script in a different stacking convention: same draw, onset root tau_c = 0.00890 ("about 0.009" is accurate). Twenty other seeds on a grid range from about 0.0035 to 0.27, so "at the seed used" is right. These are not solutions.
- dS is hand argument plus one exact point. I re-derived it by hand and the wording is accurate after R5.

**Priority 7, S_2's sign: sound as treated, after R1.**
- For (-,+,+,+) with weight e^{iS}, the usual sign is S_2 = -(1/2)A Q^2 A, so eq:Smatrix is opposite, as the researcher says. The passages of ch03 and appH read state no weight, and appH refers to Euclidean positivity.
- Without matter, S -> -S is complex conjugation and cannot change the relative sign of modes. "Positive" here therefore means sign in the form eta^{ab}Tr(A^dagger A), a signature statement.
- Relative to matter and G_eff the common sign is physical and unaddressed, so the text must say so, including the weight.

**Priority 8, literature.**
- **Steinacker2019NoGhost:** L293-297 (no physical mode of negative norm; "the quadratic action is defined by the same inner product"), L634-638 (Tr phi-dagger phi', SO(4,2)-invariant), L1957-1962 (eta-contracted matrix). "Same kind of inner product" is accurate. Footnote L1257 confirms the ghost-issue pointer, with "cf. Sakai:2019cmj".
- **Hanada:** L875-884 (right action, only for a Lie group) and L1636-1672 (ISO(n), uniform p, quenched reduced model) support both attributions.
- **Hehl:** L1242-1244 (translational field strength (torsion), Lorentz field strength (curvature)); L324-325 (Kibble first to gauge).
- **Kibble: drop.** The record exists (Crossref matches) but it was read by neither of us. Hehl's record matches Crossref and INSPIRE.
- **Prior statement not attributed:** Sakai 1905.10067 L245, "all massless at the tree level or in the presence of the supersymmetry", with L102. Attribute it (R6). I checked the record at INSPIRE: Nucl. Phys. B 949 (2019) 114801.
- **Abstracts I read:** 2604.25052, 2605.13294, 2605.10720, 2605.13972. None concerns this question from the abstract.
- **Citers searched at INSPIRE:** HKS (17), Furuta (27), Hanada (6), Sakai 2017 (4), Sakai 2019 (9).
- **Two relevant citers absent from the proposal's reading list:** 2606.24577 and 2410.13414 (Hattori et al., finite-size covariant derivatives). They use a Frobenius inner product on Euclidean, Kahler or S^2, T^2 settings. Grep plus L1328-1352 and L858-912 found no negative-norm, torsion or Lorentzian-fibre statement. Partially read, not exhaustive.
- **Worth reading next, not read by me:** 0911.1769 (torsion gravity solutions, for avenue 1), 2609.40183 and 2608.09598 (for selection), Sakai's thesis.
- Keyword searches returned 0 hits, which is not evidence of absence.
- No SME consultation is needed: no novelty is claimed and each statement cited in the revised insert is verified at its source, except the HKS and Furuta tensor-field and field-theory readings, which are reported as theirs.

**Scripts re-run in the folder with bytecode off:** s1, s2, s3, s4, s5 are all identical to saved output. Researcher's compile_check was not re-run. My own build (below) covers the revised text.

**Mechanics, on a copy outside the repository, with R1-R17 and the revised bib.**
- All 17 old strings occur once in r1 and once at their turn.
- r1 sha256 is 13c124fa..., as stated, 12560 bytes.
- Revised insert: 14148 bytes LF, ASCII, sha256 b6ccbf5f8cbd2848413c3c1fddb7a6c112e52c103262c307d593c5cb45ef86dd. It adds 14187 bytes after CRLF conversion.
- Anchor: `\section{Problem E: signature}` + CRLF occurs once, bare LF 0 times. Bare LF after insertion: 0.
- Exit codes [0,0,0,0], 348 pages, 0 undefined references or citations, 0 multiply defined labels, no bibtex warnings.
- New keys are absent from bib/namcg.bib, which ends in CRLF.

## Findings
**Blocking: none.**

**F1. Major.** Location: cutoff paragraph. "on this two-dimensional space the two-point function has two simple poles".
- *Reason:* the probes do not span an invariant subspace. The matrix is a compression of a multiplication operator. The true two-point function of these probes has a positive continuous spectral measure and no poles (s3's own Monte Carlo quantiles, about +-0.2 at sigma = 0.05, against compressed eigenvalues +-0.07). Item 5 of the proposal summary repeats the error.
- *Action:* R12 to R15.

**F2. Major.** Location: sign paragraph and end of the curved paragraph. Scoping of "tension", and "the absence of negative norm ... holds at flat space".
- *Reason:* HKS itself separates bilocal positivity from tensor-field negativity, so the pairing here is on its bilocal side. "gives one explicit correspondence" reads as answering their "no clear correspondence", but the map depends on w and the frame, and diverges. Furuta's expectation is conditional on a field theory action (L679-685). "absence of negative norm" says the opposite of the required scoping, and "absence of Jordan blocks" conflicts with the double zeros that stand at fixed q.
- *Action:* R11 and R17. Tension is kept only as a tension between readings. The text must say negative norm is not shown absent for effective fields.

**F3. Major.** Location: "The flat measure ... is not a choice of regulator."
- *Reason, ruling:* the reason is false. Lebesgue measure on Hermitian matrices does not determine eta^{ab}Tr: it equally accompanies delta^{ab}Tr. The true statement is that at finite N the form is the trace form in the action. The truncations of first-order operators (w, fibre) are a choice, and the flat class is infinite-dimensional.
- *Action:* R2.

**F4. Major.** Location: "indefinite ... only off shell and at Q=0". False on on-shell gauge directions. *Action:* R1, which also fixes item 7.

**F5. Major.** Location: pairing paragraph.
- *Reason:* "positive norm on every such truncation" fails for h_i^0 when w lies on p_0 = 0. "unless w lies on a hyperplane" is false for an affine hyperplane off the origin. omega's O is undefined. "int f^2 G_gh" leaves g,h and the fibre factor unstated, and "infrared volumes" misses delta(u,u')^2. A is not Hermitian and the condition is unstated.
- *Action:* R7 to R10.

**Minor, all required because a byte must change:**
- **F6, R5:** "every first-order fluctuation" must be equivariant. Non-equivariant fluctuations are outside the class (merged L1383) and f_a need not be a dressed one-form.
- **F7, R3:** "They" includes functions of u, which are not right-invariant fields.
- **F8, R4:** Kibble unread and "have the form" is unsupported. Also delete the Kibble entry from new_bib_entries.bib.
- **F9, R6:** unattributed prior statement. Add the Sakai2019 entry (below).
- **F10, R12:** k.lam != 0 was missing.
- **F11, R13:** R ambiguous against exp(tJ), and the operator is unnamed.
- **F12, R16:** "labels are absent" is too strong. Functions commuting with D_a can survive reduced holonomy, and "automorphisms" is not the right condition for commuting with D_a only.

**Record errata (ledger, no insert byte):**
- "bounded family" (see Priority 3);
- proposal item 5 and classification row on poles (F1);
- proposal item 4 "positive pairing" needs the hyperplane condition;
- the summary "excess massless positive modes" holds only in this pairing.

**Prior claims:** no PRIOR-CLAIM-ERROR. Merged L1379 on double zeros, heads and the 14 + 6 count, and L1383 on "the norm and masses ... are not treated", stay true as scoped.

## Scope of what is established
**Proved within hypotheses (formal adjoints, domains untreated):**
- Equation eq:Smatrix with C = 0, no matter, quadratic order about commuting matrices: on-shell signature on Q-perp/Q at null Q != 0.
- No HS eigenvector or Jordan block in background gauge at flat space.
- Fibre-less content is HKS's. Spectrum and right action are Hanada's in the Euclidean form.

**Established identities:** T = F + yF, E1 + yE2 = -Mx, E2 = Mx, 2E3 = dE1 - eta E2; commutant ad-compatibility; dS labels and Maxwell (no pairing and no spectrum there).

**Conditional or unresolved:**
- which form governs effective fields, and the sign of h_i^0 for them;
- full fibre smearing;
- selection of the class, frame, non-degeneracy, Assumptions frame-lock, nondeg, lorentzian, local-lorentz;
- the B operator, masses, loops, diagonal dynamics, G_eff, the graviton two-point function, EFT-a2.

**Classification:** PROGRAMME-CONDITIONAL. Nothing is DERIVED for a critical-path target. D, F, N remain OPEN. Emergence is respected: the 050 surviving form only, with A as data and ass:lorentzian retained. The one closing status sentence is correct. No process language. No closure by scope.

**Obstruction class (bounded, not a no-go on the route):** quadratic order; T = 0 background; first-order operators; commutant labels; Theta, order-zero and K-singlet additions; the bilinear term on dS. Within this class torsion labels remain massless. Each hypothesis below can still be relaxed.

**Milestone ruling.** M1: no, the class is supplied and this is quadratic order. M2: no, the statement is bounded and lists its relaxations. M3: none. M4, M5: none. No BREAKTHROUGH.

**Open avenues, ranked:**
1. **T != 0 backgrounds** (Lie-algebra or left-invariant with torsion): the first place a label can get a non-derivative term, because F is first order there. Relaxes "background torsion zero". Read 0911.1769 first.
2. **Diagonal-element dynamics and which labels are Nambu-Goldstone** (HKS mass gap): relaxes the commuting vacuum and connects to selection.
3. **One-loop induced form on labels with IKKT content:** decides the tension. Sakai reports no mass induced at one loop, which lowers expectations for the mass branch unless independent torsion modes change it; test that. A renormalised form may have a different sign from any positive truncation.
4. **Constraint branch for the fibre class:** an HKS-type or supermatrix constraint (Furuta L1741-1757, HKS Section "Constraint for unitarity") removing excess labels. It must be derived, not imposed.
5. **Curved backgrounds with few automorphisms:** complex pairs on actual solutions, neutral chains.
6. **Full fibre smearing and Plancherel treatment;** full Hilbert-space construction per label, with domains.

## Recommended disposition
Revise. The researcher applies exactly R1-R17 to appH_insert.tex and replaces the Kibble entry with the Sakai2019 entry. Then another review round, in which the integrator stays idle. Update the proposal record per the errata.

## Corrected snippet (no new physics or assumptions)
Each old string occurs once, verified. The exact strings are also at the scratchpad file below, with `@@` for backslash and `@@QQ` for backslash-apostrophe.

**R1.** Old: `The form is indefinite on these kernels only off shell and at \(Q=0\), the moduli of the commuting set. This statement concerns the signature; the overall sign relative to matter is not addressed.`
New: `Modulo the gauge directions \(A_a=Q_a\Lambda\), on which the form has the value \(Q\cdot Q\,|\Lambda|^2\) of either sign, the form is indefinite on these kernels only off shell and at \(Q=0\), the moduli of the commuting set. This statement concerns the signature, that is the relative sign of modes; the overall sign, relative to matter and to the weight of the integral, is not addressed.`

**R2.** Old: `The flat measure of the matrix integral is the one of this pairing, so at finite \(N\) the pairing is not a choice of regulator.`
New: `At finite \(N\) this pairing is the trace form in which the action is written, so no regulator enters there; the truncations of first-order operators below are a choice.`

**R3.** Old: `They are the right-invariant fields on \(Z=\mathrm{ISO}(3,1)\);`
New: `The last two are the right-invariant fields on \(Z=\mathrm{ISO}(3,1)\);`

**R4.** Old: `Here \(\mathsf T\) and \(\mathsf R\) have the form of the translational and Lorentz field strengths of a gauge theory of the Poincar\'e group~\cite{Kibble1961,Hehl2017}.`
New: `Here \(\mathsf T\) and \(\mathsf R\) are the linearised torsion and curvature, which in the gauge theory of the Poincar\'e group are read as the translational and Lorentz field strengths~\cite{Hehl2017}.`

**R5.** Old: `and every first-order fluctuation is a sum of terms`
New: `and every equivariant first-order fluctuation is a sum of terms`

**R6.** Old: `Each label retains its gauge parameter, so these modes stay massless at this order.`
New: `Each label retains its gauge parameter, so these modes stay massless at this order; that the fields of the expansion in differential operators are massless at tree level is stated in~\cite{Sakai2019}.`

**R7.** Old: `has pairing \(\int|\mathcal O|^2\), whatever \(\mathcal O\) is.`
New: `has pairing \(\eta^{ab}\mathrm{Tr}(A_a^\dagger A_b)=\int|\mathcal O|^2\), whatever \(\mathcal O\) is, and if \(\mathcal O\) carries nonzero translation charge then \(\eta^{ab}\mathrm{Tr}(A_aA_b)=0\), so the Hermitian part of \(A_a\) has half of that value.`

**R8.** Old: `this is \(\int f^2\,\mathsf G_{gh}\) with \(\mathsf G_{gh}=\int w\,p_gp_h\), up to infrared volumes.`
New: `the pairing of the truncations for \(g\) and \(h\) is \(\int|f|^2\,\mathsf G_{gh}\) with \(\mathsf G_{gh}=\int w\,p_gp_h\), up to a positive fibre factor common to all \(g,h\) and infrared volumes.`

**R9.** Old: `positive definite unless \(w\) lies on a hyperplane, and`
New: `positive definite unless \(w\) lies on a hyperplane through the origin, and`

**R10.** Old: `So \(h_i{}^0\) and \(\omega_i{}^{0j}\), with \(i\) transverse in this sense, have positive norm on every such truncation, the boost part of \(\omega_i\) included, and the direction \(h_i{}^\mu\propto q^\mu\) has positive and not zero norm.`
New: `So in this pairing \(\omega_i{}^{0j}\), with \(i\) transverse in this sense and \(\mathcal O\) a truncation of \(f\mathcal J_\lambda\), has a positive value, the boost part of \(\omega_i\) included, and for \(w\) not on such a hyperplane so do \(h_i{}^0\) and the direction \(h_i{}^\mu\propto q^\mu\), whose value is not zero.`

**R11.** Old: `This is in tension with the reading in~\cite{FurutaHanadaKawaiKimura2007}, where those components are expected to be negative, and with the statements in~\cite{HoKawaiSteinacker2025} on tensor fields, that the time component of each tensor field has negative norm, that the transverse zero-norm components decouple, and that there is no clear correspondence between the bilocal and the tensor inner products. The truncation gives one explicit correspondence. It does not settle the question: the form diverges`
New: `This differs from the reading in~\cite{FurutaHanadaKawaiKimura2007}, where those components are expected to be negative were the equation derived from a field theory action, and from the statements in~\cite{HoKawaiSteinacker2025} on tensor fields, that the time component of each tensor field has negative norm and that, in a minimal model without a fibre, the transverse zero-norm components decouple; that reference records that this is very different from the positivity of bilocal fields and that there is no clear correspondence between the bilocal and the tensor inner products. The pairing here is of the bilocal kind, so this is a tension between readings and not a contradiction, and the truncation is one regulator-dependent map from that pairing to a form on the label coefficients, not a derivation of the tensor inner product. It does not settle the question and does not show that negative norm is absent for effective fields: the form diverges`

**R12.** Old: `Fix a null \(k\), a one-parameter subgroup \(\Lambda_t=\exp(t\lambda)\) and`
New: `Fix a null \(k\), a one-parameter subgroup \(\Lambda_t=\exp(t\lambda)\) with \(k\cdot\lambda\neq0\) and`

**R13.** Old: `with \(R\) the right translation, on which the operator is multiplication by`
New: `with \(R\) the right translation of \(u\) alone, not \(\exp(t\mathcal J_\lambda)\), on which the background-gauge operator is multiplication by`

**R14.** Old: `and they are cutoffs of the frame and fibre parts. On them the operator is`
New: `and they are cutoffs of the frame and fibre parts. The compression of the operator to their span is`

**R15.** Old: `so its eigenvalues are real, with orthonormal eigenvectors: on this two-dimensional space the two-point function has two simple poles with residues of one sign, which merge as \(\sigma\to0\).`
New: `so its eigenvalues are real, with orthonormal eigenvectors: the resolvent of this compression has two simple poles with residues of one sign, which merge as \(\sigma\to0\). These are not poles of the two-point function of the probes, whose spectral measure under the full multiplication operator is positive and continuous.`

**R16.** Old: `and without automorphisms of the parallelism the labels are absent.`
New: `and without vector fields commuting with all \(\mathbb D_a\) the first-order labels are absent.`

**R17.** Old: `So the absence of negative norm and of Jordan blocks found above holds at flat space and is not claimed for curved backgrounds.`
New: `So the positivity of the pairing on shell and the absence of Jordan blocks on Hilbert--Schmidt kernels found above hold about commuting backgrounds and are not claimed for curved ones.`

**Bib:** delete the Kibble1961 entry from new_bib_entries.bib. Keep Hehl2017. Add (records checked at INSPIRE):
```
@article{Sakai2019,
  author  = {Sakai, Katsuta},
  title   = {A Note on Higher Spin Symmetry in the {IIB} Matrix Model with the Operator Interpretation},
  journal = {Nuclear Physics B},
  volume  = {949},
  pages   = {114801},
  year    = {2019},
  doi     = {10.1016/j.nuclphysb.2019.114801},
  eprint  = {1905.10067},
  archivePrefix = {arXiv}
}
```
No extra assumptions.

**Files:**
- C:\Users\redgi\Projects\namcg-lab\proposals\051-finite-rank-pairing-torsion-modes\proposal-r1.md
- C:\Users\redgi\Projects\namcg-lab\proposals\051-finite-rank-pairing-torsion-modes\appH_insert.tex
- C:\Users\redgi\Projects\namcg-lab\proposals\051-finite-rank-pairing-torsion-modes\new_bib_entries.bib
- C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\g51\reps_raw.txt
- C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\g51\revised_insert.tex
- C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\g51\bib_new.txt
- C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\g51\gk_id.py
- C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\g51\gk_krein.py
- C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\g51\gk_build.py
