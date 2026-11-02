SME-SCOUT: 7 routes | TOP: E:which regulated integral, finite-N limit-order lemma for the Lorentzian integral against the Euclidean model; D1/selection:semi-classical self-consistency test of the commuting-fibre and CP^{1,2} classes using the 2605.13294 criterion; A:matrix-built subregion projector and edge charge (Frenkel, Fliss et al.) on a NAMCG background | EMERGENCE-RISK: low

Date: 2026-11-02. Branch remote/claude. Scout after integration 50 (ledger through 052). Advice only. No label change is proposed.

## 0. Bottom line

1. **New and most consequential: 052's sentence on the Lorentzian integral needs a scope it does not have.**
   - The 052 insert, citing 2609.08955, says a regulated Lorentzian integral "is then no longer related to the Euclidean model by Wick rotation" and that the reflection statement "does not bear on that integral".
   - 2604.19836 Eqs. 2.8-2.11 says the opposite for its own definition. At gamma = 0, Lorentzian moments equal Euclidean moments times phases, by Cauchy, Pfaffian included. It concludes the emergent spacetime "should be interpreted as Euclidean, and moreover it is complex".
   - 2501.17798 finds inequivalence for a third definition, with Faddeev-Popov fixing of the boosts, at N = 2, d = 4, without fermions. 2604.19836 argues, without demonstrating it, that this equivalence "recovers" at large N.
   - So three published definitions disagree, and the manuscript cites none of the Nishimura-line numerics. My grep of `chapters/` finds no Nishimura, Anagnostopoulos, Tripathi, Hartnoll or Frenkel.
   - 052 is not false as attributed, but it presents one side of an open dispute as settled. This is a major concern for the author, and 052 is still uncommitted.
2. **The flat point is out of favour in the field.**
   - 2605.13294 (Steinacker): "commutative backgrounds should not be considered as classical, because off-diagonal quantum fluctuations are never small".
   - 2501.17798 (N = 2, bosonic): "the commuting saddles appear in the Euclidean model, whereas they do not show up in the Lorentzian model".
   - 050-052 mostly live at that point. Stop extending the class until route R2 has tested it.
3. **Problem A now has a first computable step, which the previous scout missed.** See R3. The published setting is matrix quantum mechanics, not a time-free integral, so this does not close A.
4. **G-derived:** none found, scoped (section 5).
5. **No published result selects a background class.** Section 4 gives what exists.

## 1. What I read, and limits

- **Repo, in full:** ledger 048-052; sme-scout-20261101-after45; 052 review-r3; 052 appH_insert; ch17 L690-749; appH Problems A, E, G (status passages).
- **Repo, not used:** no digest and no `make_digest --check`. Targeted reads only, no full scan.
- **Literature method:** WebFetch, which returns a small model's reading of the page, except where stated. Quotes and equation numbers are second-hand and must be confirmed from source before use. I did not download TeX, because my Bash is read-only by role.
- **Directly read:** only 2606.24577 pp. 1-14 (PDF images).
- **Page access by source:**
  - HTML up to the tool's window: 2609.40183 (first 100k characters; appendices not read), 2608.29688 (first 100k), 2604.19836 (first 100k; three focused passes), 2605.13294 (first 100k), 2609.08955 (characters 0-170k), 2501.17798, 2509.06646, 2411.10880, 2311.10131 (first 100k), 2408.05274v2 (first 100k; the derivation in its Sec. 5 not seen), 2609.13163 (first 100k), 1905.10067.
  - 2512.03163: characters 0-220k. Its Sec. 7 on minimal areas was not reached.
  - Abstract record only: 2002.07410, 2504.06481, hep-th/0005147, hep-th/0103159, 1106.6153, PRL 135, 221601.
- **Process slips:**
  - Two early tool rounds batched read-only calls, against the serial rule. Later calls were serial. Nothing changed.
  - Two guessed arXiv IDs returned unrelated papers (1709.07659, hep-th/0004076). Neither is used.
  - Hartnoll's Kyoto talk PDF did not parse.
- **MY CHECK** items are by hand and unreviewed. They are pointers, not results.

## 2. Routes by your gaps

### Gap 3 (E): R1, regulated Lorentzian integral. Rank 1.

**Literature**
- **Definition A, 2609.08955 Eqs. 40-41:** S_eps = S + tr(i eps sum_a (T^a)^2). This breaks SO(9,1) to SO(9). The rationale (search snippet of the same paper) is that a full rotation breaks Hermiticity and misses the Lorentzian saddles.
- **Definition B, 2604.19836 Eqs. 2.8-2.11:** A_0 = e^{-3 pi i u/8} Atilde_0, A_i = e^{i pi u/8} Atilde_i, with u -> +0. Also breaks Lorentz symmetry. Equivalent to Euclidean at gamma = 0.
  - gamma < 0 still rotates to the Euclidean model.
  - gamma > 0 does not.
  - The proposed definition is large N, then gamma -> 0. Simulations are at N <= 128, gamma = 4, xi = 12, d-tilde = 5, m_f = 6, with no extrapolation.
  - Singular drift is avoided only by the fermion mass.
  - "the CLM is not capable of finding the most dominant saddle points."
- **Definition C, 2501.17798:** delta(tr A_0 A_i) plus an FP determinant. Inequivalent at N = 2.
- **2609.40183 (Liao), classical only:** p(G) <= p(h) <= p(eta), so a Lorentzian effective metric needs timelike directions already in the contraction eta. Stability and selection are stated as open. Still one preprint, not independently confirmed.
- **Convergence:** hep-th/0103159: D = 10 partition function converges, and correlators converge for degree k < 2(D-3) = 14.

**MY CHECK**
- Eq. 2.9 follows from 2.7-2.8; I re-derived it.
- Applying the same rotation to Definition A, the regulator's real part is eps[cos(3 pi u/4) Tr T0^2 + cos(pi u/4) Tr Ti^2], positive for u < 2/3.
- So at finite N, Cauchy moves the regulated integral to some u_0 in (0, 2/3), where the quartic has a positive real part. If domination holds, eps -> 0 then gives the Euclidean value times phases.
- This suggests the "no longer related" claim holds at fixed eps or with N -> infinity first, and not at finite N with eps -> 0.
- The weak point is the bound on the rotated Pfaffian along flat directions. I did not prove it, and Austing-Wheater was read at abstract level only.

**Sub-lemma**
- Hypotheses: SU(N) finite, IKKT content, observables of degree < 14.
- Claim: lim_{eps->0} <O>_eps(Definition A) = phases x <O>_E.
- Consequence: Lorentzian signature cannot come from that limit. It requires one of N -> infinity first, gamma > 0, or a different definition. Then re-scope the 052 relaxation.
- Add an exact N = 2 comparison across A, B and C if cheap.

**Assessment**
- Constraints:
  - Do not treat gamma > 0, m_f or xi as derived. They are deformations, so a result relying on them is a scoped one (CLAUDE.md rule 3).
  - The eps -> 0 lemma says nothing about the large-N order.
- Feasibility: high, roughly 60-70% for a clean conditional statement, in my judgement.
- Value: conditional sharpening, not a breakthrough. It is the first package in this run about the integral itself and not a supplied class.
- Emergence: preserved.

**Author-level question (advice)**
- In all published work I read, Lorentzian signature enters through eta in the action, or a Euclidean model with complex phases results. I found no derivation of eta.
- Chapter 17 says "derived rather than retained". Does a real time emerging from an action with eta count? If not, 052's bound plus R1 leave no visible route, and the author should know that.
- Evidence needed before any decision: R1's outcome.

### Gap 4 (selection, frame and non-degeneracy for D1): R2, self-consistency in place of dominance. Rank 2.

**What exists (full list in section 4).** Nothing selects a class. A dominance calculation is out of reach. A self-consistency test is not.

**Sub-lemma**
- Apply the 2605.13294 criterion (Eq. 16; Eq. 17 in Minkowski, restricted to |t'-t| < Delta_T, with a warning about light-like long strings): Delta^(Q) A << Delta_T, measured in quasi-coherent states.
- Use 052's two-point formula (singular V, 1/|y-y'|^2) for the commuting fibre class, and the 045-049 propagator on CP^{1,2} x K.
- Expected outcome:
  - The fibre class fails or needs a stated smearing, giving a bounded no-go for its semi-classical reading.
  - CP^{1,2} passes at late tau, as 2605 Eq. 115 claims. Note 2605's own unexplained logarithm.
- Include the fibre-class coupling definition: the g_YM^2 analogue of 2605 Eqs. 34 and 104.

**Assessment**
- Conflicts: 2509.06646 Sec. 10 assumes the diagonal distribution is "almost uniquely determined" and four-dimensional, whereas Euclidean numerics report SO(3).
- Feasibility: medium-high.
- Value: high decision value. It tells the loop whether to keep working on 050-052. It does not discharge frame-lock or nondeg.
- Emergence: preserved.

### Gap 5 (A): R3, matrix-built subregions. Rank 3.

**Literature**
- **2311.10131 (Frenkel):**
  - Theta_Sigma = chi_Sigma(X), a projector built from the matrices.
  - Edge charge Q_Sigma from the Sigma-Sigma-bar blocks (Eqs. 38, 75). Gauss law on blocks.
  - Tr Q^2 scales as boundary length squared on the fuzzy sphere (Eq. 61).
  - O_Q = K_ij[X^i,[X^j,.]] becomes a second-order operator with a metric G-tilde generally different from the kinematic G (Eqs. 74, 76).
  - Heuristic for general backgrounds (ETH, Berry-type conjecture).
  - No modular Hamiltonian in the part read.
- **2408.05274 (Fliss, Frenkel, Hartnoll, Soni; SciPost Phys. 18, 171):**
  - Relational subsystem, S = min over regions (Eq. 1.1, Eq. 2.47), with coefficient ~ 1/g_M and a logarithm.
  - States peaked on X_cl; replica symmetry assumed; coarse-graining required to suppress non-geometric frames.
  - No first law or Euclidean integral seen.
- **Scoped search result:** no paper on target-space entanglement or a modular Hamiltonian in IKKT (one search, plus 2512.03163 in the part read).

**Sub-lemma**
- On CP^{1,2} x K, define Theta_Sigma = chi(f(X)).
- Compute the second cumulant of the block charge from the Gaussian form, using block correlators of the matrix integral.
- Test whether it is a boundary functional, and with which metric, G-tilde or the composite G. A G-tilde mismatch would bear directly on the frame issue in Problem B.

**Conflicts and what it does not do**
- No Hamiltonian or time slice exists in IKKT, so a "state" must come from a reflection or a chosen slice. This is the crux and may fail.
- It gives at most a block-entropy functional, not the causal-diamond H_D or U_ent of Assumption dictionary.
- 1/g_M with a logarithm is not 1/(4G).
- It does not close A.

**Assessment**
- Feasibility: low-medium for the charge cumulant; low for an entropy statement.
- Value: if it works, this is the first matrix-side step on A in the run, and A stays open.
- Emergence: low risk, since Theta is matrix-built before any metric. Watch that f(X) does not smuggle in a geometry.

### Gap 1 (non-commutant modes at T != 0): R4. Rank 4.

**Scoped search result:** I found no published quadratic form on torsionful Lie-algebraic backgrounds of IIB. Liao states stability is unanalysed. Closest neighbours:
- **2608.29688 (Muramatsu), N = 5, Lorentzian, iepsilon on a local Gaussian:** the constrained Hessian has inertia (95, 74, 1) on 170 directions, so it is strongly indefinite. The global cycle is left open and no dimensional selection is claimed.
- **1905.10067 (Sakai):** flat background, torsion-free conditions imposed. Its introduction records no mass at one loop.

**MY CHECK:** for k = d = 4, Liao Corollary 2 forces g_ss = 0 (dim so(1,3) = 6 > 4), so every nondegenerate Lorentzian 4-dimensional case is solvable, as 052's null-rotation algebra is.

**Sub-lemma:** exact tree Hessian on the non-commutant Lorentz modes for 052's null-rotation algebra and its non-commutant modes, at Q = 0 and at small Q; inertia, zero modes, gauge directions. Expected form: an order-zero term bilinear in structure constants, of indefinite sign under eta.

**Assessment**
- Feasibility: high.
- Value: conditional. New relative to what I found, but it stays in a supplied class. Only worth doing if R2 does not retire the class.

### Gap 2 (one-loop second order at T != 0, diagonal sector): R5 and R6.

**R5, second variation of V4. Rank 5.**
- 2609.08955 Eqs. 87-88: V4[dF] = -4 tr dF^4 + (tr dF^2)^2, with dF = F(x) - F(y).
  - The first three terms cancel for any background.
  - The one-loop action vanishes for commuting and central F.
  - So 052's O(A^4) extends at once to central F. The second-order term measures non-centrality of F, matching 052's exponent 2.0 example.
- 2609 also claims a Tr(AA) mass for hs modes and that C^1 deformations from SO(3,1) generators "are flat directions of the quantum effective potential". Both are directly testable.
- **MY CHECK:** for d = 4 with blocks lambda_1, lambda_2, V4 = -4(lambda_1^2 - lambda_2^2)^2 <= 0, zero exactly on (anti-)self-dual dF. With three or more blocks the sign is indefinite (three equal blocks give a positive value). So the sign of the form is not universal once K indices enter. Prefactor sign not checked.
- **Sub-lemma:** second variation about dF_0 != 0 on labels for the product background.
- Feasibility: medium. Value: conditional; overlaps 045-049.

**R6, diagonal fermion zero modes and eigenvalue dynamics. Rank 6. Here I disagree with the gatekeeper's "sharpest" description, on cost rather than on correctness.**
- Literature is old: Aoki et al. hep-th/9802085 and the review hep-th/9908038 (search snippets). hep-th/0005147: branched-polymer scaling, and isotropy once the phase is dropped by hand.
- A dynamical mass term in hep-th/0604211 appears as a search snippet only, not verified.
- 2509.06646 calls the diagonal effective action "complicated" and does not treat fermion zero modes.
- 2411.10880 integrates out off-diagonals for two-matrix QM: non-local in time, truncatable only with a symmetry-breaking mass, fermions dropped. Not transferable as it stands.
- Scoped: nothing from 2025-26 found on this exact sector.
- Sub-lemma: at N = 2 or 3, integrate the xi zero modes exactly and read the off-diagonal quadratic term on labels.
- Feasibility: low-medium. Value: connects loops to selection, but through a phase that the literature says is crucial and hard.

### Gap 5 (G-derived): R7. Rank 7, nothing actionable.

Section 5 records the result.

## 3. Concerns for the researcher

- Do not cite gamma > 0 numerics as signature selection. They are deformed, not extrapolated, and the CLM admits it misses dominant saddles.
- Chou-Nishimura-Wang is N = 2 only.
- The Hattori-Seko-Tsuchiya finite regularisation is Euclidean, on Kahler M, with vanishing torsion assumed in the Einstein step. It presupposes M, so it inherits the HKK emergence caveat from 050. Useful for 050's "regulated trace" avenue, not for selection.
- Weinberg-Witten not re-checked this session.

## 4. What the literature says about selection (scoped)

| Source | Scope | Statement |
|---|---|---|
| 2002.07410 (JHEP 06 (2020) 069 per DOI) | Euclidean, CLM + GEM, deformed | SO(3)-symmetric vacuum. 2604 fn 5: "physical meaning" is "not clear" |
| 2604.19836 | Lorentzian, deformed | (3+1)D expanding phase; SO(5) -> SO(3) |
| 2501.17798 | N = 2, d = 4, bosonic | Commuting saddles Euclidean only |
| 2504.06481 (SciPost 19, 099) | Polarised model | First-order transition at Omega^2 N ~ 1 to separated D-instantons |
| 2507.18472 (PRL 135, 221601) | N = 2 | IKKT saddle smoothly connected to fuzzy sphere; diverging commuting matrices dominate at small Omega; Omega -> 0 does not reduce to IKKT |
| 2609.08955 | Review | "not clear whether one saddle point will dominate" |
| 2605.13294 | Weak coupling | "Stability must be checked for each candidate background"; no dominance claim |

**Reading:**
- No published result says the integral prefers a four-dimensional non-degenerate frame, CP^{1,2} x K or a fibre bundle.
- The Euclidean numerics point to three extended directions, not four, which sits badly with any Euclidean four-frame.
- Frame and non-degeneracy have no published derivation I could find.

## 5. A and G-derived, as scoped search results

- **A:** a computable step exists in matrix quantum mechanics (R3). None was found in IKKT or for a causal-diamond modular Hamiltonian. This came from two searches and partial reads, and is not evidence of absence.
- **G-derived:** one extended search found no derivation of an infrared boundary entropy density or stationarity relation from a matrix theory.
  - 2609.13163 (single-author assessment, Euclidean finite temperature) finds no intrinsic Hawking temperature and O(N^3) entropy at fixed kappa. It does not help.
  - Search snippets say vacuum energy gives no effective four-dimensional cosmological constant, because it depends on the symplectic volume form. Not independently verified this session. A future G-derived claim must address it.
  - **I name no computable step.**

## 6. Programme-level assessment

**Plainly:** the conditional results cannot add up to the Chapter 17 label as things stand.
- DERIVED requires no assumed premise. D1 requires the frame and non-degeneracy derived. F and N need values for the vacuum actually chosen.
- Every class studied (CP^{1,2} x K, commuting fibre, left-invariant) is supplied by hand. Sharper statements inside a supplied class leave that premise in place.
- The 048 to 052 items added 22 pages (333 to 355). 052's stated progress is flat by the literal definition.
- This is careful work and the obstructions are real, but the rate of return on the current pattern is falling.

**Highest expected value next package: R1.** It is cheap, can correct a live sentence, concerns the integral itself, and frames R2.

**What the loop is avoiding:**
1. **Selection and the integral itself.** It has been listed as an avenue (049 rank 3, 050 rank 3) and then passed over for computable class work. The manuscript does not engage the Lorentzian numerics.
2. **Problem A.** Across the package headings, A is never the lead problem. It appears only as a secondary tag. Packages 015-043 work the replica and B side with A attached. A matrix-to-subregion map has not been attempted, and the literature for it was not in the manuscript.
3. **G-derived.** No package heading names it after G's mechanism. This one seems reasonable, since no route exists.

**Redundancy with published work:**
- **052 Part 1 (O(A^4)):** largely redundant. It is a corollary of IKKT's cancellation, as the text says, and 2609.08955 states vanishing for commuting and central F outright. What is added: all Q including Q = 0, the sigma scaling, and non-commuting limits. Modest value.
- **051 masslessness:** partly recorded in the Sakai 1905.10067 introduction, attributed there to earlier work. The positive pairing and compression are additional.
- **050 core:** known and attributed, as the ledger says. Its value lies in the emergence ruling and the bounded O-orbit.
- **052 reflection form:** one search found nothing in the literature on reflection positivity for IKKT. This looks like the least redundant piece, scoped to that single search. No novelty claim is warranted from it.
- **048-049:** no redundancy identified, but 2509.24753 overlap was not rechecked.

**Target to retire (advice):** further flat-point packages, including 052 avenues 5 and 6, until R2 reports.

**Emergence:** every route above can keep the metric composite. Lowest-margin points: HKK-type constructions presupposing M, and f(X) in R3.

## 7. Literature checked

**Verified records (arXiv or journal page fetched):**
- [2609.40183](https://arxiv.org/abs/2609.40183) Liao
- [2606.24577](https://arxiv.org/abs/2606.24577) Hattori, Seko, Tsuchiya
- [2608.29688](https://arxiv.org/abs/2608.29688) Muramatsu
- [2604.19836](https://arxiv.org/abs/2604.19836) Anagnostopoulos et al.
- [2605.13294](https://arxiv.org/abs/2605.13294) Steinacker
- [2609.08955](https://arxiv.org/abs/2609.08955) Steinacker
- [2501.17798](https://arxiv.org/abs/2501.17798) Chou, Nishimura, Tripathi (journal citation not listed; the page says accepted by PRL)
- [2509.06646](https://arxiv.org/abs/2509.06646) Ho, Kawai, Steinacker
- [2504.06481](https://arxiv.org/abs/2504.06481) Hartnoll, Liu
- [PRL 135, 221601](https://journals.aps.org/prl/abstract/10.1103/y1rm-n85b) Chou, Nishimura, Wang
- [2002.07410](https://arxiv.org/abs/2002.07410) Anagnostopoulos et al.
- [hep-th/0005147](https://arxiv.org/abs/hep-th/0005147) Ambjorn et al.
- [hep-th/0103159](https://arxiv.org/abs/hep-th/0103159) Austing, Wheater
- [2311.10131](https://arxiv.org/abs/2311.10131) Frenkel
- [2408.05274](https://arxiv.org/abs/2408.05274) Fliss, Frenkel, Hartnoll, Soni
- [2512.03163](https://arxiv.org/abs/2512.03163) Fliss, Frenkel
- [2411.10880](https://arxiv.org/abs/2411.10880) Brahma et al.
- [2609.13163](https://arxiv.org/abs/2609.13163) Matsumoto
- [1905.10067](https://arxiv.org/abs/1905.10067) Sakai
- [1106.6153](https://arxiv.org/abs/1106.6153) abstract only; fetched but not relied on

**Search snippets only, not independently verified:**
- [2507.18472](https://arxiv.org/abs/2507.18472) as the arXiv ID of the PRL paper, and its Omega -> 0 sentences
- Hartnoll's [Kyoto talk](https://indico.yukawa.kyoto-u.ac.jp/event/54/contributions/1315/attachments/839/1122/Kyoto%2025.pdf)
- [hep-th/9908038](https://arxiv.org/abs/hep-th/9908038)
- [hep-th/0604211](https://arxiv.org/abs/hep-th/0604211)
- [2301.01325](https://arxiv.org/abs/2301.01325)
- PTEP references for 2604.19836 and 2606.24577
- the 2609.08955 Hermiticity rationale for its regulator, seen as a snippet
- the vacuum-energy sentence

**Carried from earlier records, not re-fetched:** hep-th/9802085, 2601.08031, 2509.24753, 1108.1107.

**Searches that found nothing relevant (scoped):**
- quadratic form on torsionful Lie-algebraic IIB backgrounds
- IKKT entanglement or modular Hamiltonian
- IR boundary entropy from a matrix theory
- 2025-26 work on diagonal fermion zero modes
- reflection positivity for IKKT (one search)
- a dynamical derivation of eta

## 8. Suggested next targets

1. **R1:** finite-N limit-order lemma; map definitions A, B and C; propose re-scoping the 052 sentence through the normal gatekeeper route.
2. **R2:** semi-classical self-consistency test of both classes against 2605.13294.
3. **R3:** Theta_Sigma and the block-charge cumulant on CP^{1,2} x K; which metric appears.
4. **Author question:** what "Lorentzian signature derived" means when eta sits in the action.

**Files:**
- C:\Users\redgi\Projects\namcg-lab\proposals\052-reflection-form-one-loop-labels\appH_insert.tex
- C:\Users\redgi\Projects\namcg-lab\proposals\052-reflection-form-one-loop-labels\review-r3.md
- C:\Users\redgi\Projects\namcg-lab\reports\ledger.md
- C:\Users\redgi\Projects\namcg-lab\chapters\appH-microscopic-proofs.tex
- C:\Users\redgi\Projects\namcg-lab\chapters\ch17-agenda.tex
