VERDICT: ACCEPT | MILESTONE: none | FLAGS: none | PROGRESS: improving | OPEN: 0/0

## Verdict
The r2 insert is r1 plus exactly R1-R27 and the bib file is r1 plus exactly the four entries. I re-derived every changed claim and it holds. None of the four researcher notes needs a byte changed, so no byte changes. This is a review verdict, not merge approval. Only the author merges.

## Source reading
**Method: digest + targeted reads. No full scan.**
- **Why no full scan:** this is ordinal 48 (the ledger gives "Next integration is 48; the 5th-item full scan is due at 50"). There is no milestone verdict. The package changes no definition, assumption, scope or status passage: it is a pure insertion with no label, and its only ledger word is the one closing status sentence.
- **Digest:** `make_digest.py --check` printed DIGEST CURRENT at the start and at the end. `dirty-chapters: yes` comes from the 049 integration, so I read working-tree files.
- **Read in full:**
  - proposal-r2.md, appH_insert.tex (r2), review-r1.md, MILESTONE.md
  - s7, s8, s9, s6b and compile_check, as source and as saved output
- **Read in part, manuscript:**
  - ch03 def:matrix-coords (L98-115)
  - appH ledger labels of D (L568-572), F (L1364-1368), G (L2550-2553), N (L2914-2916)
  - appH L1340-1347 and the L2133 identity
  - ch17 L712-718
- **Read in part, literature, from arXiv sources:**
  - hep-th/0602210 L440-536, plus a grep for Lorentz, Spin(1,1) and signature
  - hep-th/0611093 L520-579, L780-1019, L1700-1856, plus a grep for double, Jordan and degenerate
  - 1205.1468 L105-122
  - 2509.06646 L150-155
- **Read in round 1 and relied on here without re-reading this round:** Problem D L565-1345, appH L2096-2167, the rest of ch17, the other R27 lines of 2509.06646, Hanada 0606163.
- **Unreadable files:** none.
- **Process slips:**
  - One early tool round batched a background Bash with a Grep, against the serial rule. Later calls were serial.
  - My first d = 2 script, `gk_conj_d2.py`, timed out in sympy `simplify` and was left running in the background. I replaced it with `gk_conj_d2b.py`, which finished. I tried to list Python processes through PowerShell in a call that also printed the source lines. The permission classifier denied that call. I did not retry the listing, and I read the source lines with Read instead. I could not confirm that the stray process has exited. It writes nothing to the repository; its task output file was empty at my last read. If it is still running, the orchestrator or author can stop it (task id `b516kqmfz`).
  - All my scripts live in the scratchpad. `git status` is unchanged apart from the pre-existing bib and appH changes, and I left no pycache in the proposal folder.

## Claim under review
**Target (ch17, item D1):** "an \(SO(3,1)\) gauge symmetry is derived from the matrix algebra and condensate, with the \(\omega,A_\mu,B\) and ghost operators specified and the field content stated. The locked frame and its non-degeneracy on the claimed domain are derived, not assumed".

**Verbatim Appendix H labels:**
- **D:** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: D2, imposed local Lorentz symmetry, supports only a scope-limited Presentation-B model; D remains OPEN and the matrix-derived criterion is unmet."
- **F:** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating \(G_{\mathrm{eff}}\) as an input leaves F OPEN and does not satisfy the matrix-derived criterion."
- **N:** "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL."

**Claim:** a bounded obstruction on the single orbit; a conditional first-order equivariant class with local SO(3,1) inside U(H), attributed to prior work; a few recorded additions without a novelty claim; an order-zero no-source lemma; one null Kaluza-Klein solution. No label change. D1 is not closed and is not claimed closed.

## Checks performed

**1. Byte check, by my own script.**
- I parsed the 27 old/new pairs from review-r1.md and applied them in order to appH_insert.r1.tex.
  - r1 has 14623 bytes, sha256 408a9d28...; this also equals the committed 2fd707d blob.
  - Each old string occurs once in r1 and once at its turn.
  - The result equals appH_insert.tex byte for byte: 18152 bytes, sha256 819f40a6..., LF, ASCII, no BOM. It also equals the 4c0313f blob.
- The r1 bib (580 bytes, 2 entries) is a byte prefix of the r2 bib. The remainder is exactly my four entries. r2 bib: 2035 bytes, sha256 7f05cb9d..., LF, ASCII.

**2. Changed claims, re-derived by hand. All correct.**
- **Measure (R11).** For a parallelism {X_i} with [X_i,X_j] = c_ij^k X_k, the Lie derivative of the dual volume gives div X_i = -c_ij^j.
  - The volume dual to {V_c, S_cd} is |det e|^{-1} d^4y dHaar.
  - The coefficient of V_c in [V_a,V_c] is -T_ac^c, and [V_a,S_cd] has no S_cd component. Hence div_mu V_a = T_ac^c for general e. This is a shorter proof than the researcher's Section 3, and it is independent of it.
  - The researcher's hand line also checks out. Tracing -T_ab^c = C_ab^c - omega_a^c_b + omega_b^c_a gives T_ac^c = -C_ac^c - omega_c^c_a. Adding div e_a = -C_ac^c and the vertical contribution -omega_b^b_a gives the same result.
  - V^dagger = -V - div V, so t_a = (1/2) T_ac^c.
- **Conjugation.** U = |det e|^{-1/2} is isometric from L^2(mu) onto L^2(reference), and it is onto because det e != 0.
  - U V U^{-1} = V + (1/2) V ln|det e|, so t~ = (1/2) div_ref V.
  - U commutes with A and with S_cd, so conjugation is an algebra isomorphism fixing them, and T, R and F are unchanged.
  - Order-zero difference: (1/2)([V_a,V_b] + T_ab^c V_c) ln|det e| = (1/2)((1/2) R S) ln|det e| = 0.
- **R14.** (xi d)^dagger = -d xi in d^4y dHaar, so Lambda is Hermitian there. The field [xi,V_a] again has the form of the class.
- **Finite local rotation.** Haar is bi-invariant because SO(3,1) is unimodular, and a vertical automorphism fixes the base. The finite form is therefore unitary in both measures.
- **R21.** [E^{ab},E_a4] = (1-4) E^b4, so [T_a,[T^a,T^b]] = -3 T^b.
  - X_a = i E_a4 gives [X^b,[X_b,X_a]] = 3 X_a, that is mu^2 = -3.
  - Y^A = g^A_4 is annihilated by E_ab. Ric = 3 eta. The E_a4 realise the class relations with S = E_ab.
  - This matches the merged identity at appH L2133. The "under the Lie bracket" qualifier is present.
- **R6.** so(3,1) is maximal in so(4,1) because its isotropy representation is irreducible. U(2) has rank 2 and compact subgroups of SO(3,1) have rank 1.
- **R19, against Furuta L531-575.** First bracket: -R^F_b^c + D^a T^F_ab^c + T^F_ab^d T^{Fa}_d^c. With T^F = -T and the curvature convention absorbed by O_cd (R^F_b^c = Ric_b^c = -R_ab^{ac} of the insert) this is the insert's bracket term by term. The second bracket also matches. The third is not in Furuta, as the text says.
- **Block-triangular corollary.** Directly from Furuta's definitions, E2 has no h and the h part of E1 is a Maxwell operator.
  - The S' part is a three-term source with no h back-reaction.
  - For a transverse i only S -> q_c S^{c mu} survives at null q. It has image q-perp, of rank 3.
  - The reduced system [[q^2,C],[0,q^2]] with rank C = 6 gives 6 double and 8 simple zeros, and 8 + 2·6 = 20.
- **The researcher's question on whether s7's induced map is the right object: yes.** The ker(wt block) -> coker(h block) map is the first-order connecting map of the triangular system.
  - Exact gauge directions in ker map to zero in coker, because C x_wt = -H x_h. So the rank 6 falls in the eps-eps part.
  - The exact Smith result (unit 16, eps 8, eps^2 6, zero 10) confirms this and matches my six lines from round 1.
- **Furuta sentences used in R23 and R24.**
  - Dilaton and B-field reading: L1708.
  - All torsion components propagate: L1712-1714.
  - Mass or constraint suggested: L1718-1724, L1737-1738.
  - Transverse physical components: L1822-1827; d = 4 gives 8 + 12 = 20.
  - Odd-time-index negative norm: L681.
  - A grep finds no "double", "Jordan" or "degenerate", so "The double zeros are not mentioned" is accurate.

**Independent computation, in my scratchpad: gk_conj_d2b.py.**
- It uses a different fibre chart from s8 (w = e^chi, Haar dw/w), with non-triangular, non-unimodular polynomial e, omega and A, at two exact rational points.
- Results:
  - div_mu V_a = T_ac^c, and the opposite sign fails;
  - t~ = (1/2) div_ref V;
  - F_01 is order zero and identical in both pictures;
  - Re F = V_a t_b - V_b t_a + T^c t_c, which is nonzero at T != 0;
  - Im F = -(V_a A_b - V_b A_a + T^c A_c).
- It is a check, not a proof. The hand argument carries the claim.

**Scripts re-run in the folder with bytecode writing off.**
- s9, s7, s6b: identical to saved output.
- s8: identical except timings (731 s against 576 s). Last line ALL ASSERTIONS PASSED.
- I read s8's logic. Part A's "symbolic first jets cover every jet at fixed (e,u)" is valid, since both sides are linear in the first jet and in omega at fixed (e,u).
- apply_r2.py was not run, as instructed. My own byte check replaces it.
- The r1 scripts were not re-run this round. They were re-run in round 1, and the text they test is unchanged.

**Mechanics, on a copy outside the repository (compile_check.py).**
- Baseline: exit codes [0,0,0,0], 339 pages. With insert and bib: exit codes [0,0,0,0], 344 pages.
- No undefined references, no undefined citations, no multiply defined labels. CRLF preserved. Scratch removed.
- Anchor at byte level: `\section{Problem E: signature}` + CRLF occurs once, and bare LF occurs 0 times. It sits at L1346.
- In-memory insertion with LF->CRLF: prefix and suffix unchanged, 18191 bytes added as expected, 0 bare LF in the result, 0 trailing-whitespace lines.
- Bib keys: all six new keys are absent from bib/namcg.bib. Steinacker2019NoGhost is present once.
- **Integrator note:** bib/namcg.bib is entirely CRLF (641 of 641 lines). Convert the entries to CRLF on appending, as with the insert.

## Rulings on the four researcher notes

**(a) Furuta's printed j. Confirmed; no erratum claimed and no text affected.**
- From the printed T_abc = S_abc - S_bac and the printed form [D_a,D_b] = R O + T D, the linear terms are:
  - [D_a,D_b]|_partial = (f_ab^mu + S'_ab^mu - S'_ba^mu) partial_mu;
  - F_ab^{cd}[partial^a,O_cd] = -F_ab^{a mu} partial_mu.
- Hence the partial_mu coefficient is partial^a f_ab^mu + partial^a S'_ab^mu - 2 partial^a S'_ba^mu + partial_b S'_a^{a mu}. So the linear -j is exactly 2 x the printed -j, with the same ratios.
- Furuta's divergence check at L1001-1014 does not distinguish the scale. A convention I have not seen could account for the factor, so this remains an observation. No sentence of the insert uses the coefficient. "Block-triangular" and rank 6 need only a nonzero coefficient.

**(b) "checked exactly for unipotent frames". True; keep it.** It understates the checks now available (s8) and the hand proof. It claims nothing false, and the sentence also says "by hand". No byte change.

**(c) R11's attribution. The sentence is accurate; keep it.**
- The printed source reads "For any manifold \(M\), this space contains a set of matrices which are unitary equivalent to the covariant derivatives" and "{\it we do not fix} \(M\)". The insert's paraphrase follows these words.
- The source context is Riemannian (L457, L524), which the insert's sentence does not repeat. But the insert says "as in" and marks the difference in the next sentence: "there on \(\mathrm{Spin}(10)\) with the Euclidean form, read here with the Lorentzian contraction of the matrix index, as for the principal \(\mathrm{Spin}(D-1,1)\) bundle of~\cite{AsanoKawaiTsuchiya2012}".
- 1205.1468 L109-112 says the same for "an arbitrary \(D\)-dimensional manifold" with the Lorentzian fibre. hep-th/0602210 itself has a Lorentzian Spin(1,1) example at L940-941.
- The transferred statement is also true at the same formal level, since L^2(Z) is a separable infinite-dimensional Hilbert space.
- "this selects none of them" stands.

**(d) F_ab at T != 0. Confirmed; no text affected.**
- Since D_a is anti-Hermitian and T_ab^c D_c is not, F_ab has a real part forced by Hermiticity. Its value is Re F_ab = V_a t_b - V_b t_a + T_ab^c t_c, and my check finds it nonzero at T != 0.
- The insert says "free Maxwell" only under "For \(\mathsf T=0\)", where t = 0 and F = -i dA. It introduces F only as a coefficient of the relation.
- The future-work caution stands: the third bracket is not Maxwell at T != 0.

## Item 4: the s8 limits and the "one Hilbert space" sentence
**The limits are honest.** proposal-r2.md Section 3 states all of them: pointwise identities in a chart; formal adjoints; the chart covers det(1-A) != 0 of the identity component, with extension by analyticity by argument only; det e != 0 is needed; domains, self-adjointness, boundary terms and non-compact integrals are untreated; different e on a fixed Z only. Its coverage table matches the output, including "d = 4: one pair, for run time".

**The insert's sentence does not claim more.**
- **Non-compact fibre.** L^2(R^4 x SO(3,1), d^4y dHaar) is a well-defined separable Hilbert space. Infinite Haar volume does not obstruct it. It obstructs the trace, which the insert lists as untreated.
- **The map itself.** U is a genuine unitary between the two L^2 spaces, given det e != 0. The insert's own R9 hypothesis (a basis of vector fields at each point) already implies det e != 0, so no extra assumption enters. U preserves compactly supported smooth functions, and the formal antisymmetry is honest on those functions. Essential self-adjointness is not claimed, and it could genuinely fail, for example through incomplete flows of V_a on a geodesically incomplete base. The closing paragraph says "Domains of the unbounded operators ... are not treated".
- **Different manifolds.** The derived part is fixed Z with fixed coordinates. "with the manifold not fixed" sits inside the attributed formal statement.
- **Finite-dimensional fibre representations.** rho(u) and similar finite-dimensional functions are not in L^2(Z) for the non-compact fibre. This does not affect the text, because Psi and elements of A are operators (matrices), not vectors of H. It does matter for any later norm or mode expansion (avenue 5).

## Item 2: F1-F12 and the record
Each finding is closed, because the replacements are in place byte for byte and I re-checked their content above or in round 1:
- F1: R19, R21, R23, R24, plus the bib entries.
- F2: R11, R14.
- F3: R9, R10.
- F4: R25, R26.
- F5: R27.
- F6: R16, R24.
- F7: R12.
- F8: R1-R3, R5, R8, R17, R20-R22, R25.
- F9: R4, R6, R7.
- F10: R15.
- F11: R18 and the R11 wording.
- F12: R23.

proposal-r2.md matches on every listed point:
- the "new" list is withdrawn in full, item by item;
- the reclassification is adopted;
- the emergence ruling is adopted, with the excluded reading and the surviving form, in place of r1 Decision 3;
- O-orbit and O-source are as ruled;
- the milestone ruling is adopted, with "Candidate M2" and "Partial M1 candidate" withdrawn;
- the avenues are in my ranking;
- no novelty is claimed.

**Record errata. They change no insert byte and do not block; they are for the ledger.**
- "L2551 (F)" in proposal-r2.md "Target and status" is wrong. L2551 is G's label; F's label is at L1365. The quoted F text itself is correct.
- "Digest STALE" was true when written and has since been superseded: the digest is now CURRENT.

## Item 6
- No status, priority or completion label changes. No labels are added.
- D, F and N stay open. One scoped closing status sentence: "Problems~D, F and~N remain open and PROGRAMME-CONDITIONAL."
- Emergence is kept in the surviving form only: operators on one fixed separable Hilbert space, Z and A declared as data of the class, Assumption ass:lorentzian retained.
- No novelty claim, no process language, no closure by scope.
- ACCEPT here does not close D1. The class is supplied.

## Findings
**Blocking: none. Major: none.**

**Minor, no action required on the text:**
- **M1. Location:** insert, R19 sentence. The Furuta comparison mentions the sign of T only, and the curvature and generator normalisation also differ (R^F O = (1/2) R S with R^F of opposite sign). The brackets agree as whole expressions, and the insert separately states R_ab^{ae} = -Ric_b^e, so the sentence is true. No change.
- **M2. Location:** proposal-r2.md, line references (see Record errata). Correct in the ledger only.

**Prior claims:** no PRIOR-CLAIM-ERROR. The round 1 rulings on L651-655, L671-675, L713-718, L873-887, L2121, L2123 and L2148-2164 stand, and nothing this round bears against them.

## Scope of what is established
**Proved within stated hypotheses (bounded).**
- **O-orbit.** Hypotheses: Poisson limit; one orbit CP^{1,2}; base functions y^mu; gauge parameters functions on the leaf; linear order about T^a. Result: no six-parameter local rotation of the frame index. Fibre orders do not mix, only J = 1 acts, three functions xi, W_y is not a subalgebra for m != 0, the boost part equals the displacement of y, no nonconstant parameter fixes y, and there is no positive-dimensional equivariant base with a vertical so(3,1).
- **O-source.** Hypotheses: tree level; T = 0; matter in A tensor a fixed factor. Result: Ric = 0 stands.

**Conditional (class supplied; identities exact within it). Known, with attribution:**
- local Lorentz and diffeomorphisms inside U(H), Ric = 0 plus Maxwell at T = 0 (hep-th/0508211);
- torsion equation, massive case and physical count (hep-th/0611093);
- large-N unitary equivalence with the manifold not fixed (hep-th/0602210; formal; selects nothing);
- the formal Lorentzian fibre (1205.1468);
- the triangular linear form (hep-th/0611093).

**Conditional, recorded here and not found stated in the sources read. No novelty is claimed.**
- the F bracket and the Hermiticity shift;
- the explicit |det e|^{-1/2} conjugation;
- the explicit 8 simple / 6 double split, a short corollary;
- the null KK solution, one example.

**Unresolved or not claimed:**
- selection of the class or A by the matrix integral;
- derivation of the frame and non-degeneracy;
- Assumptions frame-lock, nondeg, lorentzian, local-lorentz;
- the B operator and any identification with Presentation B or the emergent metric;
- a norm or masses, and any Ostrogradsky statement;
- domains and the regulated trace;
- sources beyond KK fields, loops, G_eff.

**Classification:** PROGRAMME-CONDITIONAL. D1 is not DERIVED. D, F and N remain OPEN and CRITICAL PATH. No published no-go for this interpretation was found (SME, scoped); the published concerns are stated difficulties.

**Trade-off now visible:** the S^2 fibre has no timelike modes (2509.06646) and no local rotation. The SO(3,1) fibre has local rotation, and timelike-index torsion components expected to be negative norm.

**Obstruction classes (a no-go holds only within its own hypotheses):**
- O-orbit, as above. It does not cover Moyal or finite-N, higher orders, direct sums or extra matrices.
- O-source, as above. It does not cover T != 0, further first-order matrices, or loops.
- Neither is a statement against the first-order class, nor against D1 in general.

**Milestone ruling.**
- M1 not met: the class is supplied, the symmetry is postulated with it, and the central statement is a 2005 result.
- M2 not met on the 044-049 standard: O-orbit answers only the Poisson, linear-order half of the ledger's 043 avenue 4, with its own relaxation in the same package.
- M3, M4, M5: none.
- No BREAKTHROUGH. Nothing is derived from the matrix theory that selects this route.

**Open avenues, ranked:**
1. **Torsion sector, the gate for N.** What removes the negative-norm components and double zeros.
   - Constraint branch: imposed by hand in hep-th/0602210 and in the fibre-less constraint of 2509.06646. Neither is derived.
   - Mass branch: Furuta's suggestion. The SME reports a Sakai 2017 one-loop result at T = 0 with g-independent fields, not fully checked by me, which must be tested with independent torsion modes.
   - Needs a norm from a regulated action or finite-rank pairing.
   - Relaxes: flat, no norm, first-order truncation.
2. **Sources at T != 0.** Torsion in the first bracket, including the Hermiticity-forced real part of F in the third bracket; then KK on the K of Problems C and F; then one loop. Relaxes O-source's T = 0.
3. **Selection.** Whether the matrix integral prefers this class against CP^{1,2} and commutative distributions; what fixes A; regular versus minimal representation. The frame and non-degeneracy would have to come from here.
4. **Intermediate fibres.** Classes between S^2 and SO(3,1) that trade local rotations against timelike modes.
5. **Regulated trace for the Lorentzian fibre.** Hanada's kernel is built for Spin(n). Issues: cyclicity under regulation, infinite Haar volume, bilocal modes, and the fact that finite-dimensional fibre functions are not in L^2(Z), so any mode expansion needs a Plancherel treatment. The essential self-adjointness of V_a on incomplete bases also belongs here.
6. **Relaxations of O-orbit.** Moyal or finite-N inner automorphisms; field-dependent parameters at second order; direct sums of orbits; extra matrices acting on y.
7. **Map to Presentation B** (Phi, Xi, B and the F operators) and non-equivariant fluctuations.
8. **Supersymmetry.** HKK states the restriction destroys global supersymmetry. Furuta also points to supermatrices and a torsion constraint (L1741-1757) as a way to remove the unwanted components, which links to avenue 1.

## Recommended disposition
Integrate as-is.
- Insert the bytes of appH_insert.tex, converted LF to CRLF, immediately before `\section{Problem E: signature}` + CRLF, found at byte level.
- Append the six entries of new_bib_entries.bib to bib/namcg.bib, converted to CRLF.
- Do not run apply_r2.py.
- Ledger: record the L2551/L1365 line erratum and that the integration is ordinal 48. Only the author merges or commits.

## Corrected snippet
None. No byte changes.

**Files:**
- C:\Users\redgi\Projects\namcg-lab\proposals\050-frame-bundle-local-lorentz\proposal-r2.md
- C:\Users\redgi\Projects\namcg-lab\proposals\050-frame-bundle-local-lorentz\appH_insert.tex
- C:\Users\redgi\Projects\namcg-lab\proposals\050-frame-bundle-local-lorentz\new_bib_entries.bib
- C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\r2\bytecheck.py
- C:\Users\redgi\AppData\Local\Temp\claude\C--Users-redgi-Projects-namcg-lab\15e6827c-2d5a-4852-be36-98ee14883700\scratchpad\r2\gk_conj_d2b.py
