# Proposal 050-frame-bundle-local-lorentz, round 2

## Result

Round 2 applies the review's corrections and corrects my r1 record. It contains no new research and no new claim.

D1 stays OPEN. Nothing here is DERIVED in the Chapter 17 sense. What the package establishes, as ruled in `review-r1.md`:

1. **A bounded obstruction (O-orbit).** No six-parameter local rotation of the frame index exists in the conjugate-coordinate class, under the hypotheses listed in "Rulings adopted".
2. **A conditional class with local SO(3,1) inside U(H).** The class is supplied, and its central statements are prior work of Hanada-Kawai-Kimura (2005) and Furuta et al. (2007).
3. **A few additions recorded and not found stated in the sources read.** These are short consequences, and no novelty is claimed for them.

**Withdrawn from r1:** the whole "New relative to the cited source" list, Milestone "Candidate M2", and "Partial M1 candidate".

**Mechanics:** R1-R27 and the four bib entries are applied exactly once. Bytes match the expected hashes:

| File | Bytes | Line endings | sha256 |
|---|---|---|---|
| `appH_insert.tex` (r2) | 18152 | LF, ASCII | `819f40a624e4f7a87c177253be13f23dc97d0861921230bf1835c421ec2987f9` |
| `appH_insert.r1.tex` (r1 kept) | 14623 | LF, ASCII | `408a9d28fff6308559036268e399c018c0eb98cf383b48171ef449012c024c7c` |
| `new_bib_entries.bib` (r2) | 2035 | LF | `7f05cb9d40570ffc1f57f753476538a280cea26e2924aad3070c67e0ddebb42e` |

Both r2 files are byte-identical to the review's reference copies in its scratchpad (`cmp`).

**I found no R text wrong, so there is no discrepancy to report in the sense of the brief.** Four remarks that change no text are under "Special instructions".

## Target and status

Verbatim from Appendix H, as quoted in `review-r1.md`. I re-grepped the status lines, and they are unchanged at L569 (D), L2551 (F) and L2915 (N).

- **D:** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: D2, imposed local Lorentz symmetry, supports only a scope-limited Presentation-B model; D remains OPEN and the matrix-derived criterion is unmet."
- **F:** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion."
- **N:** "Status: OPEN. Priority: CRITICAL PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL."

**Original target (ch17, item D1):** "an SO(3,1) gauge symmetry is derived from the matrix algebra and condensate, with the omega, A_mu, B and ghost operators specified and the field content stated. The locked frame and its non-degeneracy on the claimed domain are derived, not assumed".

**Classification:** PROGRAMME-CONDITIONAL. No label change.

**Dependencies:** as in r1, plus the cited literature below.

## Source reading

**Digest + targeted reads. No full scan.** The package changes no definition, assumption, scope or status passage.

**Digest.** `make_digest.py --check` prints `DIGEST STALE (head changed)`, not `DIGEST CURRENT`.
- The digest head is 2fd707d and HEAD is d2ee344. `git diff 2fd707d d2ee344 -- chapters bib` is empty, so those commits touch neither chapters nor bib.
- `dirty-chapters: yes`, because of the accepted 049 integration awaiting the author's commit, so I read working-tree files.
- I did not regenerate the digest, since I write only in this folder. The orchestrator may want to.

**Read this round:**
- `review-r1.md` in full, `sme-consult-r1.md` in full, `proposal-r1.md` in full.
- The r1 insert in full, and the r2 insert L18-26.
- Scripts `bundlelib`, `s2`, `s3`, `s6` and `compile_check`.

**Literature read by me from arXiv LaTeX sources** (the review's and SME's downloads, read-only):

| Source | Lines | What I confirmed |
|---|---|---|
| hep-th/0611093 Furuta et al. | L1-1029, L1430-1499, L1700-1856 | Abstract, intro, ansatz, gauge variations, the two-bracket equation, linear equations, negative-norm footnote, weak-field expansion, `j` at L868-879, mass term, discussion, physical components |
| hep-th/0602210 | L455-470, L518-530 | "contains a set of matrices which are unitary equivalent"; "we do not fix M" |
| hep-th/0606163 Hanada | title block, L505-535, L583-612; grep for Spin(n) | Regulated action, three remarks |
| 1205.1468 | L105-122 | Principal Spin(D-1,1) bundle over an "arbitrary" manifold |
| 1910.00839 | L1254-1260 | "excessive dof and the associated ghost issues" |
| 2112.08204 | L3170 | "the absence of ghosts has not been established" |
| 2509.06646v2 | L148-156, L720-726, L1221, L1327-1338 | The sentences used in R27 |
| 1709.02588 Sakai | L725-730, L1000-1005, L1096-1107 | Triangular linear equations; "still unclear"; metricity remark |
| hep-th/0508211 | grep with context lines | L1303 maximally symmetric; L1572-1676 diffeomorphism and local Lorentz; L1724-1725 rank-three; L1740 divergent trace; L642 fixed manifold |

**Bib records.** Fetched from the INSPIRE API this round for all four new entries. Authors, title, journal, volume, pages, DOI and eprint match.

**Not read or not verified by me:**
- Sakai 2017 one-loop section beyond those lines.
- Matsuo et al., Isono-Tomino, the Bender-Mannheim abstracts, the Plancherel remarks. None is relied on in the text.
- The journal reference for 2509.06646. The `@misc` entry is kept.
- The Cartan reconstruction has no citation. It is standard mathematics, and the insert now assumes the manifold structure it needs.

**Unreadable files:** none.

**Process slips:**
- Against the serial rule, I batched read-only calls in one early round and one Write plus its Bash run in another. Nothing else was affected.
- The run was interrupted by a usage limit before anything was written. On resuming I confirmed that the insert and bib still had their r1 hashes and that no `.r1` copy existed, so nothing was double-applied.

## Research and reasoning

### 1. Verification of R1-R27, before applying

| R | Finding | How I verified it |
|---|---|---|
| R1-R3, R5, R8, R17, R20, R22 | F8 notation | Pure renames. Each collision confirmed in the r1 text (`\sigma` as both orientation and index in one formula; vector `\eta`; `\Phi` against the condensate). `\Phi`, `\sigma\ell`, `\eta\cdot` occur 0 times after application |
| R4, R6, R7 | F9 | R6: an equivariant base is a union of orbits G/H. A vertical so(3,1) lies in h, and h != g in positive dimension. so(3,1) is maximal in so(4,1) because its isotropy representation on R^{3,1} is irreducible. So h = so(3,1). U(2) has rank 2 and compact subgroups of SO(3,1) have rank 1. Correct |
| R9, R10 | F3 | The spectrum of a commutative algebra is not automatically a manifold, and "pointwise independent" gives no basis. Correct |
| R11 | F2 | Section 3 below and `s8` |
| R12 | F7 | 1205.1468 L109-112 |
| R13 | attribution | hep-th/0508211 L334, L1633-1676 |
| R14 | F2 | Hermitian in the reference measure, since (xi d)^dagger = -d xi. Closure of `xi + (1/2) div xi` on the class is in `s8` part C. HKK L1572 onward |
| R15 | F10 | rho(u) is double-valued on SO(3,1), so the cover is needed |
| R16 | F6 | Hanada L505-535, L590-601, Spin(n) at L211 and L489; HKK L1740 |
| R18 | F11 | s2 frames are unipotent by construction (`s2_torsion_eom.py` L47-48) |
| R19 | F1 | Furuta L554-575. With T^F = -T: first bracket `-R + D T^F + T^F T^F`, second `D R + T^F R`, equal to my first two brackets term by term. My third bracket is not in Furuta, since it has no A term in its ansatz. Correct as written ("the first two") |
| R21 | F1, F8 | By hand and `s9`. HKK L1303 and Furuta L1441-1446, L1472-1496 for the massive case |
| R23 | F12, F1 | HKK L1724-1725; Furuta L162-167, L700-718, L777-781, L1712-1714 |
| R24 | F1, F6 | Furuta L676-685, L1712-1727, L1737-1757, L1820-1827, L1852-1856; 1910.00839 L1256. `s7` for the count |
| R25, R26 | F4 | Furuta L720-725: R_ab = (3-d) d_a d_b phi. The first bracket contains D T and T T |
| R27 | F5 | 2509.06646 L153 ("So far, this does not appear to have been very successful \cite{HKK}"), L723-724, L1221, L1329-1335. The fibre-less scope is as the text says, and I checked that the text does not assert those objections are its reasons at L153 |

### 2. The split as a corollary (`s7`)

**Block-triangular form.** On e^{iq.y}, with w = i wt, the linear equations are exactly:

- E2_b^{de} = q^2 wt_b^{de} - q_b q^a wt_a^{de}, with no h;
- E1_b^e = (q^2 h_b^e - q_b q^a h_a^e) + (q^a wt_{ab}^e - 2 q^a wt_{ba}^e + q_b wt_a^{ae}).

Each diagonal block is a Maxwell operator with extra indices. The coupling goes from connection to frame only, and it has the ratios 1/2 : -1 : 1/2 of Furuta's linear `j` (L868-879).

**Rank at null q.**
- For a transverse i (q_i = q^i = 0) the other two coupling terms vanish on the S_i sector, leaving S -> q_c S^{c mu}.
- A 2-form contracted with a null q has image exactly q-perp, of dimension 3, with kernel 3.
- Two transverse i give rank 6.

**Count.** Physical components at d = 4: h_i^mu (2 x 4 = 8) and S_i^{cd} (2 x 6 = 12), total 20. The reduced system is [[q^2, C], [0, q^2]] with rank C = 6 at q^2 = 0, so:

- 6 pairs (q^2, q^2) join into one double zero each;
- the 2 h modes outside the image of C and the 6 S modes in its kernel stay simple.

**8 + 2·6 = 20.** The split is a short corollary of published equations. It claims no novelty.

**Full operator.**
- Blocks alone: (unit, eps, eps, 0) on each extra index, so unit^10, eps^20, 0^10.
- The induced map from ker(wt block) to coker(h block) has rank exactly 6, which joins 6 pairs (eps, eps) into (unit, eps^2).
- That gives unit^16, eps^8, (eps^2)^6, 0^10, as the exact local Smith computation finds.
- The ten zeros are the gauge directions (generic rank 30 of 40).

**Which vector is which.**
- The eigenvector of a chain is the frame-type tail (S = 0, R = 0, T != 0). The generalised vector carries the connection mode. This is the gatekeeper's and SME's reading.
- Heads including gauge have rank 16. Their wt projection is exactly the span of q_a lam^{cd} (rank 6). So 10 have wt = 0: 4 diffeomorphism gauge directions and 6 tails.

**Results of `s7`:**

| Line | Result |
|---|---|
| Four transversal lines, with and without E3 | unit 16, eps 8, eps^2 6, zero 10 |
| Rank at eps = 3/7, each of the four lines | 30 of 40 |
| Reduced 20 x 20 | unit 6, eps 8, eps^2 6 |
| Tangent line q^2 = eps^2 | unit 16, eps^2 8, eps^4 6, zero 10 |

This agrees with r1 (two lines) and with the review (six lines).

**Comparison with the printed `j`.** See Special instructions, item 1.

### 3. Measure and conjugation (`s8`)

**Hand proof of div V_a = T_ac^c for general e.** Work at u = 1 and write omega_a = e_a^mu omega_mu.
- From the frame fields, -T_ab^c = C_ab^c - omega_a^c_b + omega_b^c_a, where [e_a, e_b] = C_ab^c e_c. Hence T_ac^c = -C_ac^c - omega_c^c_a.
- In the measure dual to e, div e_a = -C_ac^c.
- The vertical part is a coefficient times Haar-divergence-free fields, so it contributes only through its action on that coefficient, u_a^b: this gives -omega_b^b_a at u = 1.
- So div V_a = div e_a - omega_b^b_a = T_ac^c.
- General u follows by equivariance.

**Hermiticity.** V^dagger = -V - div V, so V + t is anti-Hermitian iff t = (1/2) div V, for real t.

**Conjugation.** U = |det e|^{-1/2}, as multiplication, maps L^2(mu) to L^2(reference) isometrically.
- U V U^{-1} = V + (1/2) V ln|det e|. Hence t~_a = t_a + (1/2) V_a ln|det e| = (1/2) div_ref V_a, the symmetrised form in the reference measure.
- Elements of A commute with U. S_cd commutes with U because det e does not depend on u.
- So all the relations are carried to the same relations with the same coefficients, since conjugation by U is an algebra isomorphism fixing A and S_cd.
- The order-zero difference is (1/2)([V_a, V_b] + T_ab^c V_c) ln|det e| = (1/2)((1/2) R_ab^cd S_cd) ln|det e| = 0.

**How far the script goes:**

| Part | What it does | Coverage |
|---|---|---|
| 0 | A real chart on the fibre (Cayley, A in so(p,q)), with dA = (1/2)(1+A) Omega (1-A) from du = u Omega. The Haar density det(1-A)^{-(d-1)} is tested and not assumed: left and right invariant fields, boosts included, are divergence free | d = 2, 3, 4, on every basis element, at one rational point each |
| A | div_mu V_a = T_ac^c involves only the first jet of e and the value of omega, and is linear in them at fixed (e, u). So symbolic first jets at fixed (e, u) cover **every** jet there. Frames neither triangular nor unimodular | d = 2 with (e, u) also symbolic; d = 3, 4 at one rational (e, u) each, 64 + 24 symbols at d = 4 |
| B | Polynomial e (degree 2) and omega (degree 1), non-triangular, non-unimodular, to second order: t_a = (1/2) T_ac^c, and the order-zero part of [D_a, D_b] + T^c D_c is the same in both pictures | d = 3: three pairs, plus the all-pairs difference. d = 4: **one pair, for run time** (the difference at other pairs follows from the hand line above) |
| C | Formal anti-symmetry of L_a = V_a + (1/2) div_ref V_a against test functions; S_cd has no y part and no divergence, with the stated commutator; `xi + (1/2) div xi` closes on the class in the reference measure | d = 3, one point each |

**Limits of this check.** These are pointwise identities in a chart, with formal adjoints. Specifically:
- The chart covers the open set det(1-A) != 0 of the identity component. Extension to the connected component is by real-analyticity, by argument. Other components are not considered.
- U needs det e != 0 on the whole domain, which is the non-degeneracy that the class assumes and does not derive.
- No domains, self-adjointness, boundary terms or integrals over the non-compact fibre are treated. The insert says domains are untreated.
- The conjugation relates different e on a fixed Z. Different manifolds enter only through the separable-Hilbert-space statement attributed to hep-th/0602210, which is formal.

## Correcting the r1 record

### Withdrawn

**The list "New relative to the cited source" in r1 is withdrawn in full.** I missed Furuta et al. (2007) and did not search citers of HKK. Item by item:

| r1 item | Correct status |
|---|---|
| Full formula with torsion | Published (Furuta L554-575). Only the F bracket and the Hermiticity shift are additions |
| Linear spectrum with torsion, the 14 null solutions | The count is Furuta's (d = 4: 20 physical components). The explicit split is a corollary |
| Link to the merged class | The massive case is HKK's and Furuta's, including maximally symmetric solutions. The remark is only that a Lie algebra identity holds in every representation |
| Generators from commutators on rank-six curvature | Withdrawn as a "new" item. Text kept as a labelled observation, unchanged |
| Order-zero no-source lemma | Bounded lemma at T = 0; the classical statement is HKK's |
| Null Kaluza-Klein solution | One example, stays below |

**Also corrected in r1:**
- "Algebraic definition (no manifold assumed)" is not established. The insert now assumes smoothness and a basis (R9, R10).
- r1 Section E's reading that 2509.06646 concerns "a vacuum without this fibre" was false for its first statement (F5). I had said I did not determine the reasons. The same paper states objections to differential-operator expansions, shown there without an O_cd sector.
- r1 "the hypothesis this rests on is the representation" overstated (R7).
- r1 "These are outputs of the operators" overstated (R10).
- r1's unstated measure (R11, R14).
- "So Ric = 0 stands" is true only at T = 0 (R25, R26).
- "With no action defined on the class" is false as a statement about the literature (R16, R24). The correct statement is that no action is used here.

### Reclassification, adopted from the review

**Conditional (class supplied; identities exact within it). Known, with attribution:**
- local Lorentz and diffeomorphisms inside U(H), and Ric = 0 plus Maxwell (HKK, hep-th/0508211);
- the torsion equation, massive case and physical count (Furuta et al., hep-th/0611093);
- large-N unitary equivalence with M not fixed (hep-th/0602210);
- the formal Lorentzian fibre (Asano-Kawai-Tsuchiya, 1205.1468, and others);
- the triangular linear form (Furuta et al.; Sakai 1709.02588 has the same structure at L725-730).

**Conditional, recorded here and not found stated in the sources read:**
- the F bracket and the Hermiticity shift;
- the explicit |det e|^{-1/2} conjugation;
- the explicit 8 simple / 6 double split, a short corollary;
- the null KK solution, one example.

**No novelty is claimed.** The SME reports no published statement of double zeros, with scoped searches and incomplete full-text indexing. That is not evidence of absence.

**Unresolved or not claimed:**
- selection of the class or A by the matrix integral;
- derivation of the frame and non-degeneracy;
- Assumptions frame-lock, nondeg, lorentzian, local-lorentz;
- the B operator and any identification with Presentation B or the emergent metric;
- a norm or masses; any Ostrogradsky statement;
- sources beyond KK fields; loops; G_eff.

The ghost operator is specified only as a formula. Double zeros carry no norm in this text.

### Emergence ruling, adopted

**The route is not non-emergent as written and is not rejected. A form of it survives, and only that form is allowed.** This replaces r1 Decision 3.

- **Excluded reading.** Taking the manifold and bundle as given input would make the base fundamental. HKK as published starts this way, and Asano-Kawai-Tsuchiya frames it this way. This reading is not used.
- **Surviving form.**
  - Operators on one fixed separable Hilbert space, with e, omega and A as components of the dynamical X_a.
  - The action contains only the constant eta on matrix indices, as in Definition def:matrix-coords-ext.
  - K = eta^{ab} D_a y D_b y is a function of the configuration.
  - eta enters the relation [S,D] as the so(4,2) form enters the orbit. Its signature stays Assumption ass:lorentzian.
  - The published formal statement is hep-th/0602210 (unitary equivalence, "we do not fix M"). It is formal and selects nothing.
- **Standard.** Emergence is at the same standard as CP^{1,2}, not a stronger one.
  - **Weaker:** the orbit comes from one Lie-algebra representation with no free function, while here Z, its smooth structure and A are data of the class, and the six-parameter local rotations hold because S_cd is postulated.
  - **Stronger:** all metrics are configurations of the matrices, and the identities are exact in the operators with no Poisson limit.
- **Neither class derives spacetime from the matrix integral.**

### Rulings adopted

- **O-orbit.** Hypotheses: Poisson limit; one orbit CP^{1,2}; base functions y^mu; gauge parameters functions on the leaf; linear order about T^a. Result: no six-parameter local rotation of the frame index. Fibre orders do not mix, only J = 1 acts, three functions xi, W_y is not a subalgebra for m != 0, the boost part equals the displacement of y, no nonconstant parameter fixes y, and there is no positive-dimensional equivariant base with a vertical so(3,1).
- **O-source.** Hypotheses: tree level; T = 0; matter in A tensor a fixed factor. Result: Ric = 0 stands.
- **Trade-off.** The S^2 fibre has no timelike modes (2509.06646, "no ghosts arise") and no local rotation. The SO(3,1) fibre has local rotation, and timelike-index torsion components expected to be negative norm.
- **No published no-go** for this interpretation was found (SME, scoped). The published concerns are stated difficulties, not theorems.

### Findings addressed

| F | Severity | Addressed by |
|---|---|---|
| F1 | Blocking | R19, R21, R23, R24; bib entries; "new" list withdrawn above |
| F2 | Major | R11, R14; `s8` |
| F3 | Major | R9, R10 |
| F4 | Major | R25, R26 |
| F5 | Major | R27 |
| F6 | Major | R16, R24 |
| F7 | Minor | R12 |
| F8 | Minor | R1-R3, R5, R8, R17, R20, R21, R22, R25 |
| F9 | Minor | R4, R6, R7 |
| F10 | Minor | R15 |
| F11 | Minor | R18, R11 wording |
| F12 | Minor | R23 |

I disagree with no finding.

## Claim classification

| Claim | Class |
|---|---|
| Bracket formulas, y_nu lambda^{nu sigma} = -s m xi^sigma, W_y not a subalgebra, selection rule, no vertical parameter | Established within O-orbit |
| No six-parameter local rotation in the class | Bounded obstruction, O-orbit |
| Relations imply the three-part formula | Established algebra. First two brackets published (Furuta et al.) |
| Local rotations and diffeomorphisms in U(H), Ric = 0 plus Maxwell at T = 0 | Conditional on the supplied class; prior result (HKK). Lorentzian form formal (Asano-Kawai-Tsuchiya), domains untreated |
| div_mu V_a = T_ac^c; t_a = (1/2) T_ac^c | Established within the class (hand; exact checks in `s2`, `s8`) |
| |det e|^{-1/2} conjugation, relations unchanged | Established formally within the class on fixed Z; needs det e != 0 (hand; `s8`) |
| One Hilbert space with the manifold not fixed | Formal statement of hep-th/0602210; selects nothing |
| Massive case, maximally symmetric solutions | Prior result (HKK; Furuta et al.) |
| Lie algebra identity common to both classes | Established (`s9`); regular versus minimal representation not examined |
| 8 + 2·6 split | Established corollary of published equations (hand; `s7`); no norm attached |
| Order-zero no-source | Bounded lemma, O-source |
| Null KK solution | Established, one example |
| Negative norm of odd-time-index modes | Published expectation without an action (Furuta et al.); not derived or asserted here |
| Class selected by the matrix integral; frame and non-degeneracy derived | Unresolved |
| Cartan reconstruction | Standard input, not re-proved |

## Proposed changes

**File:** `chapters/appH-microscopic-proofs.tex`. Insert the bytes of `appH_insert.tex` immediately before the unique line `\section{Problem E: signature}`, at L1346 of the current working tree. Nothing is replaced, and the preceding text "...and leaves Problems~B, C, D, F and~G open." stays.

**Anchor at byte level:** `\section{Problem E: signature}` + CRLF occurs once, bare LF form 0 times (`s6b`). Convert the insert from LF to CRLF on integration. In the Bash tool a double backslash collapses, so match at byte level.

**Bib:** add all six entries of `new_bib_entries.bib` to `bib/namcg.bib`. All six keys are absent now. `Steinacker2019NoGhost`, also cited, is already there once (arXiv 1910.00839).

**The LaTeX** is the file itself, so that one copy is authoritative. It is r1 plus exactly R1-R27 in order, and nothing else. The application log is `apply_r2.r2.out.txt`.

**Stale passages elsewhere:** none are false. The review's check of L651-655, L671-675, L713-718, L873-887, L2121, L2123, L2148-2164 and ch09 L333 stands, and no replacement is proposed.

## Verification scripts

All are in `proposals/050-frame-bundle-local-lorentz/`. No r1 output was overwritten or refreshed. The r1 scripts `s1`-`s5` were not re-run, since nothing they test changed. The review re-ran `s1`, `s2`, `s2b`, `s4`, `s5` and checked `s3` by its own code.

| Script | Output | Checks | Result |
|---|---|---|---|
| `apply_r2.py` | `apply_r2.r2.out.txt` | One-shot, reads strings raw from `review-r1.md`, requires each old string once at its turn, refuses to write on a mismatch or a second run | Each of R1-R27: 1 in r1 bytes, 1 at its turn. Second run refused, exit 1 |
| `s7_split_corollary.py` | `s7_split_corollary.r2.out.txt` | Section 2 | All as stated |
| `s8_measure_conjugation.py` | `s8_measure_conjugation.r2.out.txt` | Section 3; asserts stop it on failure | Last line ALL ASSERTIONS PASSED, 576 s; the opposite sign in part A is False at d = 2, 3, 4 |
| `s9_r21_lie.py` | `s9_r21_lie.r2.out.txt` | The formulas of R21 as written: [E_a4, E_b4] = -E_ab; [S,D] relation; -3 T^b; mu^2 = -3; Y annihilated; K = eta - YY; Y.Y = 1 | All true |
| `s6b_insert_mechanics_r2.py` | `s6b_insert_mechanics.r2.out.txt` | Byte-level anchor, labels, keys | See below |
| `compile_check.py` (unchanged) | `compile_check.r2.out.txt` | Copy outside the repository, new bytes and bib | See below |

**Mechanics (`s6b`):**
- ASCII, no CR, no BOM; 8 blocks; no new labels; one status sentence.
- Residual `\Phi`, `\sigma\ell`, `\eta\cdot`: 0 each.
- Every `\ref` label exists once: ass:frame-lock, ass:local-lorentz, ass:lorentzian, ass:nondeg, ch:vierbein-emergence, def:matrix-coords, eq:LUV-def, eq:NC, eq:Smatrix, eq:Smicro, eq:dressed-omega, sec:status-F, sec:status-N.
- The two "round " hits are "background".

**Compile:**

| Build | Exit codes | Pages | Undefined refs | Undefined citations | Multiply defined |
|---|---|---|---|---|---|
| Baseline | [0,0,0,0] | 339 | none | none | none |
| With insert and bib | [0,0,0,0] | 344 | none | none | none |

CRLF preserved; scratch removed. `git status` outside this folder shows only the pre-existing bib and appH changes.

## Decisions Taken

1. **Emergence:** adopt the review's ruling with its excluded reading and surviving form, in place of r1 Decision 3. Rejected alternative: keeping "no manifold assumed", which was not established.
2. **Text:** verbatim only. Where a stronger wording is now available (R11's "for unipotent frames", while `s8` checks general frames), I did not change it. It stays true and the brief forbids silent changes. See Special instructions, item 2.
3. **Order of work:** the checks ran before the writes for R21, and for R24's count; the `s8` part A run and the hand proof ran before R11 and R14 were applied.
4. **d = 4 scope of `s8` part B:** one pair for run time. A hand line carries the rest, and the limit is stated.

## Milestone assessment

**Routine; my r1 "Candidate M2" and "Partial M1 candidate" are withdrawn.** Adopting the review's ruling:
- M1 not met: the class is supplied, the symmetry is postulated with it, and the central statement is a 2005 result.
- M2 not met on the 044-049 standard: O-orbit answers only the Poisson, linear-order half of the ledger's 043 avenue 4, with its own relaxation in the same package. It is a bounded sharpening of L2121.
- M3, M4, M5: none.
- No BREAKTHROUGH. Nothing is derived from the matrix theory that selects this route, and the published authors' caution stands.

## Status-label recommendation

Critical-path list from Chapter 17 and Appendix H: A, B, C, D1, E, F, G-derived, N. Affected labels: none. No change recommended.

## Author decision needed

None. The route keeps spacetime emergent in the surviving form, and changes no label.

## Remaining open step

To close D1, the frame and its non-degeneracy, together with the symmetry, must be derived from the matrix theory and not supplied with the class. Avenues, ranked as in the review:

1. **Torsion sector, the gate for N.** What removes the negative-norm components and double zeros.
   - Constraint branch: imposed by hand in hep-th/0602210 and in the fibre-less constraint of 2509.06646. Neither is derived.
   - Mass branch: Furuta's suggestion. The SME reports a Sakai 2017 one-loop result that, at T = 0 with g-independent fields, leaves IIB massless (not fully checked), so it must be tested with independent torsion modes.
   - Needs a norm from a regulated action or finite-rank pairing.
   - Relaxes: flat, no norm, first-order truncation.
2. **Sources at T != 0.** Torsion in the first bracket, then KK on the K of Problems C and F, then one-loop. Sakai 1709.02588 calls the gravitational mediation "still unclear". Relaxes O-source's T = 0.
3. **Selection.** Whether the matrix integral prefers this class against CP^{1,2} and commutative distributions; what fixes A; regular versus minimal representation. This is where frame and non-degeneracy would have to come from.
4. **Intermediate fibres.** Classes between S^2 and SO(3,1) that trade local rotations against timelike modes.
5. **Regulated trace for the Lorentzian fibre.** Hanada's kernel is built for Spin(n), and its non-compact use is unjustified in what was read. Cyclicity under regulation (2509.06646), non-compact Haar volume, bilocal modes.
6. **Relaxations of O-orbit.** Moyal or finite-N inner automorphisms; field-dependent parameters at second order; direct sums of orbits; extra matrices acting on y.
7. **Map to Presentation B** (Phi, Xi, B and the F operators) and non-equivariant fluctuations.
8. **Supersymmetry.** HKK states the restriction destroys global supersymmetry.

## Special instructions for the gatekeeper

None of these four items changes a byte. Items 2 and 3 are wording you may want to judge.

1. **Printed `j` in Furuta (L868-879).** From Furuta's own definitions of T and R (L531-551), I obtain the linear term of the first equation as exactly **2 x** the printed `-j`, with the same three-term ratios (`s7` A2). Its L1001-1014 divergence check is consistent for either overall scale. Possibly a convention I have missed; I claim no erratum. No text depends on it: R24 says only "block-triangular", and rank 6 needs only a nonzero coefficient.
2. **R11 wording.** "checked exactly for unipotent frames" is true, and now weaker than the checks (`s8` part A covers general frames). Applied verbatim. Changing it would need your text.
3. **R11 attribution.** The hep-th/0602210 sentence (L461-465) follows a statement about "any d-dimensional Riemannian manifold with a fixed spin structure", and the insert applies "as in the statement of" to Lorentzian covariant derivatives. That is the formal transfer R12 attributes to Asano-Kawai-Tsuchiya, and that paper also has a Spin(1,1) example (SME; I did not read that passage). I read it as acceptable. Also, the conjugation relates different e on a fixed Z only, and different manifolds rest on the formal statement alone.
4. **Order-zero part at T != 0.** `s8` part B prints a nonzero order-zero coefficient at T != 0 with A = 0. So F_ab is not only the A field strength there: it contains a real part forced by Hermiticity, whose linear part is the E3 term of s3. The insert says only "free Maxwell" at T = 0, so nothing is wrong. Do not read the third bracket as Maxwell at T != 0.

**Please re-check:**
- the `apply_r2.py` log and hashes;
- that `s7`'s induced-map rank is the right object;
- the hand line in Section 3;
- that I have not claimed novelty anywhere.

**Digest:** `--check` is STALE by head only (see Source reading).

**What the insert must not assert:** closure of D1; a norm or ghost statement of its own; selection; identification with the emergent metric; a value or sign of G_eff.

**Do not integrate before a new verdict.** The review says no byte may be integrated without another round.
