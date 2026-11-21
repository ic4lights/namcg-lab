# Proposal local-gpu 072-080 (Problem G edge-sector block), round 2

## Result

This round revises the gpu block 072-080 as one package. It is a bounded, conditional sharpening inside the
existing Problem G edge-entropy paragraph. It closes nothing.

1. **072 RESEARCHER-DECISION: option (b), the direct-sum background.**
   - The two-component block is now defined as X = X1 (+) X2 (two deformed fuzzy spheres, one cap each), with
     Θ = Θ1 (+) Θ2 of rank M1+M2 and subsystem group U(M1+M2) x U(2N-M1-M2).
   - For this block the following are exact:
     - the edge datum is a sum of two rank-one pieces;
     - E has nonzero spectrum {s1², s2²}, so Tr E^p = s1^{2p} + s2^{2p} with no corner term;
     - for momenta without entries between the summands, the charge spectrum is exactly the union of the two
       single-cap pairs.
   - The two band-separated caps of one axis (option (a), which needs M1+M2 < N) are kept as a second instance.
   - The U(M1+M2) two-row reading is now applied only where it is valid. The product block Θ1 ⊗ Θ2 (rank M1M2,
     connected edge) is handed to the accepted local 067 and explicitly excluded from the reading.
   - Every closed form and number of 072-075 depends only on (M_f, ℓ_f) and on the per-summand formula
     s_f² = k_f M_f (N - M_f), so all of them survive unchanged. The only casualties are the product-specific
     corner sentences, which become exact additivity.
2. **The decision propagates through 073-080.**
   - 075: the two cap axes are now the axes of the two summands, so independent averaging is natural. The corner
     sentence is deleted.
   - 076: the product-testbed comparison is replaced by an exact direct-sum statement. With q_f coincident copies
     of summand f and momenta copy-invariant within each group, the per-summand stacked diagram (ℓ1^{q1}, ℓ2^{q2})
     is the one read. This is the positive counterpart of the old negative statement about the product.
   - 077, 078, 080: the pencil now applies to any block with one cap per summand.
   - The coincident copies are the direct sum of equal summands. This is exactly the U(q) background J ⊗ 1_q of
     the cited selection rule.
3. **Three errors in the gpu-accepted text, corrected with evidence.**
   - E1, PRIOR-CLAIM-ERROR. "[the rule] is stated for the diagonal cut" (072, repeated in 076-078 as "its
     diagonal-cut convention", and in 081). arXiv:2311.10131 uses the *block* partition. Its §5 and the Fig. 10
     caption state that the diagonal partition belongs to an earlier reference and that the block partition is
     "the choice considered in [44, 45], and this note".
   - E2. 074's "error ... of order q log(ℓ1+1) uniformly in N" is wrong. The residual grows as q1q2 log N: the
     increments per doubling of N approach q² log 2 (d3(d)). This is the 079 bound.
   - E3. 079's "row lengths of valid diagrams never exceed the total rank" is false for polynomial diagrams of
     U(M). Frame-uniformity holds for a different reason: the saddle rows are bounded by ℓ^{(0)} (tr B/2)^{1/2}.
4. **Group-wide cleanup.**
   - The eight "close(s) nothing in Problem G" clauses are removed.
   - The stale closing scope sentence is replaced by one scoped status sentence for the whole paragraph.
   - The block is compressed from 33,133 B (12 paragraphs) to 14,501 B (4 paragraphs), merging results that share
     derivations: 073+074+079, 076+077+078+080.
5. **Fork on the bounded obstruction** (the non-additivity over components). Explored in this package:
   - frame average: survives;
   - o(N) row perturbations: survive;
   - stacked diagrams: survive;
   - O(N) perturbations: remove it;
   - inter-summand momenta: the union holds only at leading order.

   The ranked open avenues are listed under "Remaining open step".

## Target and status

- **Problem G.** Appendix H ledger, live, `chapters/appH-microscopic-proofs.tex` L2889-2892: "Status: OPEN. Priority:
  CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope results: G-model and G-external support at most a
  scope-limited model; G remains OPEN and neither satisfies the matrix-derived criterion."
  - Status paragraph, L2900-2905: the mechanism is CLOSED CONDITIONALLY; the derivation of the infrared entropy
    density and of stationarity from the matrix theory is OPEN.
- **Chapter 17.**
  - L474-480: "CRITICAL PATH; mechanism CLOSED CONDITIONALLY, derivation OPEN".
  - G completion levels, L482-495: G is DERIVED only when the entropy density of `ass:Sent-density` and the
    stationarity of `ass:bdy-EE` are derived from the matrix theory and Λ_eff follows from them.
  - L723-725: G-derived is in the full-GR criterion.
  - No discrepancy between Chapter 17 and Appendix H.
- **Original target:** derive S_ent^(IR) and boundary stationarity from the matrix theory, then Λ_eff.
- **This package:** PROGRAMME-CONDITIONAL. It is conditional evidence about the edge-mode functional of a matrix
  block on a compact factor (a region of the factor, not of the emergent spacetime). It is not a derivation of the
  target.
- **Dependencies:**
  - the FFHS block subsystem (arXiv:2408.05274, `FlissFrenkelHartnollSoni2025`, in bib);
  - the transplanted selection rule (arXiv:2311.10131, new bib entry);
  - the supplied Gaussian states of the Row length paragraph;
  - local 067 (accepted r2, not integrated), cited for the product block.
- **Current critical-path set** (Chapter 17 L700-730 and ledger): A, B, C, D1, E, F, G-derived, N. H, I and J are
  optional.

## Source reading

**Digest + targeted reads. No full scan was performed.**

- `python scripts/make_digest.py --check` printed `DIGEST CURRENT`. The digest reports `dirty-chapters: yes`
  (uncommitted appH, ch14 and bib changes in the working tree).
- Read in full:
  - `scratch/digest.md` (head and Problem G region);
  - appH L2886-2932, the whole Problem G section in the current tree;
  - ch17 L470-495, L650-680 and L700-745;
  - the gpu-import backup L3153-3175 (texts of 072-080) and the references from 081-088 into this block;
  - `_local-review/group5-G1.md` in full;
  - 067 `appH_insert_r2.tex` and `review-r2.md` (tail);
  - 072 `review-r1.md`, 075 `review-r2.md`, 079 `proposal-r1.md` L1-140;
  - the 076, 077 and 079 script headers;
  - ledger L677-730.
- Grep sweeps over all `chapters/*.tex` for: selection rule, direct sum, two caps, edge mode, FlissFrenkel,
  Frenkel2023, dominant representation/diagram. No passage outside the Problem G paragraph depends on the text
  changed here.
- **Full scan owed.** The protocol requires one under 3(c) (this package replaces a paragraph-level scope sentence)
  and 3(d) (`dirty-chapters: yes`). I did not perform it: the manifest is 13,231 lines (1.07 MB). The gatekeeper
  must perform or discharge it.
- No unreadable files.

## Research and reasoning

### R1. The 072 decision

**The mismatch.** The gpu 072 text mixes two different blocks:
- the edge data of Θ1 ⊗ Θ2 on S² x S²: rank M1M2, E spectrum {s1² x (M2-1), s2² x (M1-1), s1²+s2²}, and a
  connected L-shaped edge;
- the selection and defect reading, which is for U(M1+M2) with one row per disconnected component.

**Options.**

- **(a) Two band-separated caps of one axis.**
  - This setting is already in the Row length paragraph, which establishes the exact union property.
  - It needs M1+M2 < N, and more than twice the band width between the edges.
  - Cost:
    - the headline symmetric numbers (m1 = m2 = 1/2, Δ/N = 0.521, the c = 1/2 breakdown of 073, and the
      0.5232 q values of 074 and 075) are unrealizable and would have to be recomputed;
    - both caps share one axis and one deformation, so k1 = k2 and the axis is common, and 075's independent
      two-axis average does not exist;
    - the rows could not be tuned independently through the frame.
- **(b) Direct-sum background X1 (+) X2.**
  - Needs one definition, plus the derivation below.
  - All numbers survive, because the defect depends only on (M_f, ℓ_f).
  - The corner disappears exactly.
  - Independent frames are natural.
  - The coincident copies of 076-080 are its special case of equal summands. This is the U(q) background J ⊗ 1_q
    of arXiv:2311.10131, §3.2, eq. (3.16).
- **(c) Keep Θ1 ⊗ Θ2 with U(M1M2) and 067's multi-row reading.**
  - The diagram then has about M1+M2-1 rows (067: the box count follows the trace norm T, not s).
  - The two-row U(M1+M2) defect and all 072-075 closed forms would be the wrong object, so everything would have
    to be redone.
  - This duplicates 067's line.

**Decision: (b).** (a) is kept as a second instance. (c) is delegated to 067.

**What (b) needs, with derivation.** Let X^a = X_1^a ⊕ X_2^a on C^N ⊕ C^N, with X_f^a = A_f J (N-dim irreps),
Θ = Θ1 ⊕ Θ2, and Θ̄ = Θ̄1 ⊕ Θ̄2.

1. *Edge datum.* X is block-diagonal and Θ, Θ̄ are block-diagonal, so Θ X^a Θ̄ = ⊕_f Θ_f X_f^a Θ̄_f. Each summand
   is rank one, c_f^a |u_f)(v_f|, by the Edge datum paragraph. Hence X_{ΣΣ̄} = Σ_f c_f^a |u_f)(v_f|, with
   u_f, v_f supported in summand f (exact).
2. *Edge operator.* E = Σ_a Θ X Θ̄ X Θ = ⊕_f s_f² |u_f)(u_f|, with s_f² = Σ_a |c_f^a|² = k_f M_f (N - M_f) by the
   Edge datum paragraph. So spec E \ {0} = {s1², s2²} and Tr E^p = s1^{2p} + s2^{2p} exactly. There is no corner
   term. This replaces the product's corner admixture, which was O(1/N).
3. *Charge.*
   - Y = Σ_a X_{ΣΣ̄} Π_{Σ̄Σ} = Σ_f |u_f)(w_f|, with (w_f| = Σ_a c_f^a (v_f| Π^a Θ.
   - If Π^a has no entries between the summands, w_f lies in summand f. Then Q = Q_1 ⊕ Q_2, with Q_f the
     single-cap charge, and the nonzero spectrum is the union of the two pairs −2h_f ± 2(h_f² + n_f)^{1/2}, with
     h_f = Im(u_f|w_f) and n_f = |w_{f,⊥}|² (exact).
   - Derivation of the pair: in the basis (u, w_⊥/|w_⊥|), Q = [[−4h, −2i|w_⊥|], [2i|w_⊥|, 0]], so
     λ² + 4hλ − 4|w_⊥|² = 0.
   - d1(c) and d1(pair) check this at relative error ≤ 6e-16 for N1 ≠ N2 as well.
   - The pair formula needs M_f ≥ 2. For M_f = 1 the block is one-dimensional, w_⊥ = 0, and Q_f has the single
     eigenvalue −4h. This is why the text states M_f ≥ 2.
4. *Subsystem.* By the paragraph's opening definition, the FFHS subsystem for a projector of rank M is made
   invariant under U(M) x U(N_tot − M). Here this is U(M1+M2) x U(2N − M1 − M2). No new assumption enters. The
   direct sum is a matrix configuration of the same compact positive-contraction class; it is reducible, which is
   the multi-brane configuration.
5. *Second instance (a).* For two caps of one axis with M1+M2 = N, the projector is the identity and the edge
   datum vanishes (d1(f)). For M1+M2 < N with band-separated momenta, the union is exact (Row length paragraph;
   076 s2 re-run: deviation 0.000e+00).
6. *Relaxation of the "no entries between summands" hypothesis* (fork).
   - For iid Gaussian momenta on the full 2N space, the w_f are independent isotropic Gaussian vectors on the whole
     (M1+M2)-dim block.
   - The median relative distance of the 4-point spectrum from the union of the diagonal pairs is 0.0861, 0.0538,
     0.0398, 0.0296, 0.0227 at block rank 50-800, slope −0.471 (d2(f)).
   - So the union holds at leading order, which is consistent with Frenkel's "cross terms between topologically
     disconnected pieces ... vanish to leading order in N" (§3.1, near eq. 3.15). But n_f then counts entries in
     the other summand's block, and the row is no longer the single-cap row.
   - At small N the deviation is ≥ 0.224 (d1(d)), so the hypothesis is load-bearing at finite N.

**Why the numbers survive.**
- Δ (two-row), Δ_{q1,q2} (stacked), Λ, the bound, the box minima, the breakdown at c = 1/2, Δ_{q,0}/(qN) and the
  rank ratio are functions of (M1, M2, ℓ1, ℓ2, q1, q2) alone.
- The rows on the saddle class are t·s_f, with the same s_f formula for the product factor, the direct-sum summand
  and the cap of one axis.
- With N the summand dimension, M_f = m_f N and k_f = 1, every quoted value is reproduced (runs/; d3).

### R2. The selection rule: what arXiv:2311.10131 states (verified from the PDF text, 36 pp, v1 16 Nov 2023, no journal ref)

- **§1 summary.** "the dominant irrep in the SU(M) entanglement edge mode density matrix is given by a Young
  diagram ... The Young diagram has one row for each disconnected component of the entanglement cut, and the length
  of each row is given by the boundary length (i.e. 'area') of this component". Shown via Tr Q², then Tr Q^{2p}
  (eq. 1.10): "Q has one eigenvalue for each disconnected component".
- **States.** States "localized to some classical state", with quadratic (Gaussian) fluctuations (eq. 1.7).
- **§3.2.** The background X = J^i ⊗ 1_q (eq. 3.16), with K_{q,ij} = K_ij ⊗ 1_q (eq. 3.18). "each topologically
  disconnected piece of the entanglement cut contributes q rows instead of 1", "To leading order (if q doesn't scale
  with N)".
- **§4.** General noncommutative backgrounds are argued, under quadratic fluctuations and kinetic terms of at most
  second order.
- **Partition.**
  - §5: "our choice of partition of the degrees of freedom is not the same as for previous computations ... in
    [37] ... The choice of a diagonal partition obscures the internal U(M) symmetry of Γ that is manifest in the
    block partition."
  - Fig. 10 caption: "On the left is the choice of partition considered in [37]. On the right is the choice
    considered in [44, 45], and this note."
  - §2.2: the blocks X_{AB} = Γ_A X Γ_B and the symmetry breaking U(N) → U(M) x U(N−M).
- **Consequence (E1).** The rule *is* stated for the block cut. The gpu sentence "it is stated for the diagonal
  cut, and its transposition to the block cut is a transplant" is false. In this block, the transplant consists of:
  - the use with the supplied states of the Row length paragraph (Frenkel's states are the quadratic-fluctuation
    states of the theory);
  - rows set by the edge data s_f (Frenkel's §4 rows are lengths in a deformed metric G̃);
  - direct sums of *distinct* spheres. Only equal summands appear as Frenkel's U(q) background.

  The revised text says exactly this. The gpu 072 reviewer's "diagonal-vs-block cut comparison left open ✓" refers
  to Frenkel's open comparison of the two partitions. That comparison does not make the rule a diagonal-cut
  statement.

### R3. The defect, row perturbations, stacks and the residual bound (072-074, 079)

- **Two-row closed form.**
  - Hook-content: dim_{U(M)}(ℓ1, ℓ2) = Π(M+c−1) Π(M+c−2) / [((ℓ1+1)!/(ℓ1−ℓ2+1)) ℓ2!].
  - Divided by the single-row dimensions, this gives the displayed Δ (derivation in R3 of the gpu 072 proposal;
    re-derived here).
  - Checked from scratch in Fractions on 1620 cases (d3(a)), and by 072 s2 on 1155 cases.
- **Limit.**
  - (1/N)Δ → 2[G(1, ½) − G(½, ½)] = 3 log(3/2) − log 2 = log(27/16) = 0.523248144 (d3(c)).
  - Δ/N = 0.520906 at N = 3200.
  - The ratio to N log 2 is 0.7515 (072 s3).
  - The rank ratio is 0.8111, with limit 2 log(3/2) = 0.810930 (d3(c)).
- **Non-monotone increment.** It equals exactly log(37/72) (d3(b)).
- **Stacked identity.** 074 s1: 17,856 cases, 0 failures; 2268 reduce to the two-row form.
- **Bound** (079, re-run s1: Lemma R 210, Lemma H 77, identity 70, chain 1560 cases, 0 failures):
  - statement: |Δ_q − NΛ| ≤ Σ|log(A/B)| + ℓ-shift terms + q1q2 log(ℓ1+q1+q2);
  - the shift terms are ℓ1 Σ(r−1)/(M−r+1) + ..., which is (ℓ/M) times a function of q, so C depends on m_f, ℓ_f/M
    and q_f;
  - the established bound is written that way.
- **E2: residual growth.** The residual N qΛ − Δ_{q,q} at N = 400-3200 is:
  - 5.42 → 7.50 at q = 1;
  - 19.22 → 27.50 at q = 2;
  - 39.82 → 58.41 at q = 3.

  The increments per doubling are 0.690-0.692, 2.751-2.767 and 6.167-6.220, against q² log 2 = 0.693, 2.773 and
  6.238 (d3(d)). The residual therefore grows as q1q2 log N, so 074's "of order q log(ℓ1+1) uniformly in N" is
  wrong in its q-dependence. The 079 bound has the correct coefficient.
- **Box minima and breakdown** (073 s5, 074 s3 re-run):
  - at c = 0.4975, min/N = 0.001727, 0.002440 and 0.002889 for q = 1, 2, 3;
  - at c = ½, min/N = 0 at (0, 0);
  - the argmin is at the far corner.
- **Single-stack values** (074 s2): Δ_{q,0}/(qN) = 0.188909, 0.188979, 0.189049.

### R4. Frame average (075, 079)

- **Exact identities.**
  - s²(n) = ¼M(N−M)(tr B − n·Bn) (075 s1, worst relative error 1.4e-15).
  - With ρ = ½(tr B − n·Bn): E_n ρ = tr B/3.
  - The profile is strictly increasing and strictly concave in ρ (d3(f), sympy plus samples; 075 s2(2)). This is
    the composition of a concave increasing φ(u) with u ∝ √ρ.
- **Jensen** under tr B = 3. This is the review's "squared edge-length fraction" fix: ρ is that fraction relative to
  B = 1.
- **Uniformity (E3).**
  - The 079 text argued that "the row lengths of valid diagrams never exceed the total rank". Polynomial diagrams of
    U(M) have unbounded row length (for example the symmetric powers), so that argument is invalid.
  - The correct reason: at fixed B_f the saddle rows are ℓ^{(0)} ρ^{1/2} ≤ ℓ^{(0)} (tr B/2)^{1/2}, because
    max_n ρ = ½(tr B − λ_min) ≤ tr B/2.
  - The bound therefore holds uniformly over the axes, with a constant fixed by ℓ^{(0)}/N and tr B.
- **Family B = diag((3−γ)/2, (3−γ)/2, γ).**
  - Averaged limits 0.522655, 0.519217, 0.511350.
  - Minima 0.479485, 0.396700, 0.268892.
  - Reproduced by independent Gauss-Legendre quadrature (d3(e)) and by 075 s2(3).
- **Residuals and rank ratio.**
  - Two-row residuals: maximum 7.70 at γ = 2.6, N = 3200 (075 s2(4)).
  - Depth-three residuals: maximum 59.80 at γ = 2.2 (075 s3).
  - Rank ratio between 0.7858 and 0.9023 (075 s2(7)).
- **079 scan** (re-run s2):
  - two rows: worst residual 7.102, bounds [8.609, 9.006];
  - depth three: worst residual 54.874, bounds [74.830, 80.211];
  - round frame: 8.772 and 77.037;
  - no failures at N = 400, 1600, 3200.
  - The scan samples random trace-3 Gram matrices B, the same for both summands, with axes e1, e2 and t = 1. Its
    round-frame rows are therefore 1131 = (½·1600²)^{1/2}, not N/2. The review's sentence is kept, with
    "(ℓ_f^{(0)} = 1131)" and "with tr B = 3" added so the normalisation is explicit.
- **Corner fractions** (0.9423-2.4484): product-only, deleted.

### R5. Copies, pencil, multiplicities, typicality (076-078, 080)

- **Copies.**
  - Coincident copies = direct sum of q equal summands.
  - Copy-invariant momenta give an exact lift (076 s1).
  - Generic momenta give simple eigenvalues (076 s1, least gap 0.05+).
  - Groups q_f of summand f with copy-invariant momenta within each group: E has s_f² with multiplicity q_f, and Q
    is ⊕ 1_{q_f} ⊗ Q_f (d1(e), deviation 2.7e-15).
- **Band-separated mismatch.** 9/17 and 81/145, and 1 at equal depths. Independent of N and t (076 s3; d2(d)).
- **Pencil identity.**
  - Q = [U R] (−2i)[[0, 1], [−1, 0]] [U R]^†. Its nonzero spectrum is that of
    −2i[[0, 1], [−1, 0]] [[1, C0], [C0^†, Z0]] = −2i[[C0^†, Z0], [−1, −C0]].
  - Since the lower-left block is scalar, det[[A, B], [C, D]] = det(AD − BC). This gives
    det((λ + 2iC0^†)(λ − 2iC0) − 4Z0) = det(λ² + 4λH − 4K).
  - Checked symbolically at q = 2 (d2(a)), at q = 2 and 3 (078 s1, s3), and numerically for q = 3-6.
- **Block-scalar factorization.** Realised data; d2(b), 080 s1 (96 cases).
- **q = 2 criterion.**
  - 64d − (4b − a²)² = −256[(Δh)⁴ + 2Δh²(n1+n2) + (n1−n2)²] (d2(c), 080 s2).
  - This vanishes iff Δh = 0 and n1 = n2, given n_f ≥ 0. The first condition then holds automatically.
  - Example: (λ−2)²(λ+14)(λ+22) (d2(c), 078 s3).
- **Equalized class.**
  - The codimension-three coincidence set is von Neumann-Wigner for Hermitian H.
  - Gap lower bound: by the mean value theorem on λ_±(h) = −2h ± 2(h² + n)^{1/2}, with derivative magnitude
    ≥ 2(1 − h_max/(n + h_max²)^{1/2}), and branch separation ≥ 4n/((n + h_max²)^{1/2} + h_max) (078 s2b, s3).
- **Moment identity** at h = 0: exact rationals (d2(d), 080 s3).
- **Typicality** (my own sampler, d2(e)). For iid Gaussian momenta the edge rows are iid isotropic Gaussian vectors
  on the block (the 077 s2b reduction).
  - Matched scales: medians of D_gap and U2 at N = 50, 100, 200, 400 are 0.2833/0.0986, 0.2049/0.0492,
    0.1535/0.0244 and 0.1111/0.0126. The slopes are −0.447 and −0.992.
  - Scales (1, 1.6): D_gap = 0.4329, 0.4102, 0.3973 at N = 120, 240, 480 (slope −0.062).
  - |h|/n^{1/2} slope: −0.556 (d2(g)).
  - These are statistically consistent with the gpu 077 values (0.2986 → 0.1176, 0.1027 → 0.0143; control
    0.4147-0.3946). The text quotes my d2 values, rounded.
  - Exact non-typicality: 0 of 6000 draws; first-order linear splitting, D/t ≈ 0.79-0.81 (077 s1).
- **Dropped from 077** (not reproduced by a passing run in this round, or not needed):
  - the fixed-q grids to q = 32;
  - the along-q exponent at N = 1024;
  - the lognormal mixture;
  - the q = 4 failure points of U2 < 0.05.

  The 077 addendum records s2/s2b as not run.

### R6. Local 067

- 067 (accepted r2, sha256 f0fa634c..., not integrated) is the product-sphere paragraph. It owns rank, T, the rows
  of the toric block, and the multi-row reading.
- The revised block **cites** 067 ("the toric-block paragraph below") and does **not** duplicate its closed forms:
  the product E-spectrum sentence of gpu 072 is removed.
- **Anchor plan:**
  - 067 is integrated first, unchanged, immediately before `\section{Problem H: modular origin of the interpolating
    function}`, that is after the Edge-entropy paragraph's closing sentence. Its "preceding paragraph" references
    then still point to that paragraph.
  - This block is then inserted inside that paragraph, before `\emph{Vacuum term.}`.
  - The two anchors are disjoint, so the result does not depend on the order. The cross-reference "below" requires
    067 to be present.
- **067 alone on the current tree:** 661,373 B, sha256 069aafc47357a448..., CRLF 3455. The 637,508 B in 067's review
  refer to an older tree.

## Claim classification

| Claim | Class |
|---|---|
| Direct-sum edge datum, E spectrum, Tr E^p additivity, charge union for momenta without inter-summand entries | established (exact) |
| Pair formula −2h ± 2(h²+n)^{1/2}, M_f ≥ 2 | established |
| Union at leading order with iid inter-summand entries, decay ~ rank^{-1/2} | numerical |
| Content of arXiv:2311.10131 (block cut, one row per component, q rows on J ⊗ 1_q, leading order) | literature, verified from the PDF text |
| Transplanted selection rule (supplied states, rows from s_f, distinct summands) | conditional input (transplant) |
| Two-row closed form, stacked identity, log(37/72) increment, log(27/16) limit | established |
| Residual bound with explicit constants | established (079 derivation) |
| Residual growth q1q2 log N; box minima; breakdown at c = ½; Δ_{q,0} values; rank ratios | numerical |
| s²(n), E ρ = tr B/3, concavity, Jensen bound, uniform convergence of the frame average | established |
| γ-family values, residual maxima, 079 scan | numerical |
| Copy lift, group lift, pencil identity, block-scalar factorization, q = 2 criterion, double-root example, codimension, gap bound, moment identity | established |
| Generic-momenta simplicity, non-typicality, leading-order tiling rates, scale-mismatch persistence | numerical |
| "Not an artefact of the probe diagram" | conditional (within the dominant-representation class and the transplant) |
| Entropy density on ∂M, Λ_eff, stationarity | not derived (unresolved) |

## Proposed changes

**File:** `chapters/appH-microscopic-proofs.tex`, Problem G section only. Nothing else in chapters changes.

### C1. New text inside the Edge-entropy paragraph

- Insert `insert_block_r2.tex` (14,501 B, CRLF 7, sha256 a2c59c496170183a84ca9a9b272ce52944b3e5ca6c93fdfe3d41c533831b8c03)
  followed by one blank CRLF line.
- Position: immediately before the unique line that starts with `\emph{Vacuum term.} The abstract
  of~\cite{Steinacker2023}` (current L2928). The line-start count is 1. The bare string "Vacuum term" also occurs
  at L2874, in Problem F, which is why the anchor is the line-start form.
- Kept: the Edge datum, Row length, State and coarse-graining, Bearing and Vacuum term paragraphs are all kept
  verbatim.

```latex
\emph{Two-component blocks and the transplanted selection rule.} Let \(X^a=X^a_1\oplus X^a_2\) on \(\mathbb C^N\oplus\mathbb C^N\) be the direct sum of two deformed spheres \(X^a_f=A_f{}^a{}_bJ^b\) of the edge-datum paragraph, and let \(\Theta=\Theta_1\oplus\Theta_2\), with \(\Theta_f\) the spectral projector of \(n_f\cdot J\) on its \(M_f\ge2\) largest eigenvalues in summand \(f\); the subsystem of~\cite{FlissFrenkelHartnollSoni2025} attached to \(\Theta\) is invariant under \(U(M_1+M_2)\times U(2N-M_1-M_2)\). Then \(X^a_{\Sigma\bar\Sigma}=c^a_1|u_1)(v_1|+c^a_2|u_2)(v_2|\), with \(u_f,v_f\) in summand \(f\); the nonzero spectrum of \(E=\sum_a\Theta X^a\bar\Theta X^a\Theta\) is \(\{s_1^2,s_2^2\}\), with \(s_f^2=k_fM_f(N-M_f)\) and \(k_f=\tfrac14(\sigma_{f,1}^2+\sigma_{f,2}^2)\), so that \(\operatorname{Tr}E^p=s_1^{2p}+s_2^{2p}\) for every \(p\); and for momenta without entries between the summands the nonzero spectrum of \(Q\) is the union of the two single-cap pairs of the Row length paragraph (exact). The two caps of one axis of the Row length paragraph give the same union, with \(k_1=k_2\), when \(M_1+M_2<N\) and the edges are band-separated; at \(M_1+M_2=N\) their projector is the identity and has no edge. For independent identically distributed Gaussian momenta, which have entries between the summands, the union holds only approximately: the median relative distance of the spectrum from it is \(0.086\) at block rank \(50\) and \(0.023\) at rank \(800\), decaying as about the inverse square root of the rank, and the norm of each edge row then also includes its entries in the block of the other summand (numerical). The selection rule of~\cite{Frenkel2023EdgeModes} is derived for the block cut of~\cite{FlissFrenkelHartnollSoni2025} on the fuzzy sphere, in Gaussian states of the quadratic fluctuations about it, and argued for general noncommutative backgrounds: at leading order in \(N\) the moments \(\operatorname{Tr}Q^{2p}\) fix the dominant diagram, with one row for each disconnected component of the cut, of length set by that component, and \(q\) equal rows for each component on the background \(J^a\otimes\mathbf 1_q\). Its use with the supplied states of the Row length paragraph, with rows set by the edge data \(s_f\), and for direct sums of distinct spheres is a transplant (conditional), referred to below as the transplanted selection rule. For a block that is the union of two disconnected components, such as the direct sum above or the two band-separated caps of one axis, whose charge spectrum is exactly the union of the two single-cap pairs, it suggests a two-row diagram of \(U(M_1+M_2)\) with rows fixed by the single-cap edge data; the block \(\Theta_1\otimes\Theta_2\) of the product of two spheres, treated in the toric-block paragraph below, has rank \(M_1M_2\) and a connected edge, so this reading does not apply to it. On the saddle class \(\ell_f=t\,s_f\) with fixed \(t\), the defect \(\Delta=\log\dim_{U(M_1+M_2)}(\ell_1,\ell_2)-\log\dim_{U(M_1)}(\ell_1)-\log\dim_{U(M_2)}(\ell_2)\), \(\ell_1\ge\ell_2\), is \(\sum_{c=1}^{\ell_1}\log\frac{M_1+M_2-1+c}{M_1-1+c}+\sum_{c=1}^{\ell_2}\log\frac{M_1+M_2-2+c}{M_2-1+c}-\log\frac{\ell_1+1}{\ell_1-\ell_2+1}\) (exact, by the hook-content formula; checked in rational arithmetic), the exact form of the excess in item~(ii) of the bearing paragraph (the approximate form holds for \(\ell_f\ll M_f\)). For the direct sum at \(M_1=M_2=N/2\), \(k_1=k_2=1\), \(t=1\) it grows linearly in \(N\): \(\Delta/N=0.521\) at \(N=3200\), against the limit \(\log\frac{27}{16}=0.5232\) and about \(0.75\) of the approximate form, and \(\sum_{(r,c)\in\mu}M/(M+c-r)=0.811\,|\mu|\) at block rank \(M=M_1+M_2\), so the dependence on the rank survives (numerical). The defect is not monotone in \(\ell_2\): \(\Delta(\ell_1,\ell_2+1)-\Delta(\ell_1,\ell_2)=\log\frac{37}{72}\) at \((M_1,M_2,\ell_1,\ell_2)=(2,24,13,12)\) (exact). Within the dominant-representation class (compact factor, positive contraction, leading semiclassical order with the leading-order entropy of~\cite{FlissFrenkelHartnollSoni2025} and one dominant diagram), with the diagram selected by the transplanted selection rule on the saddle class at fixed frame, the non-additivity of item~(ii) is therefore not an artefact of the fixed probe diagram.

\emph{Row perturbations, stacked rows and the residual bound.} For depths \(1\le q_f\le M_f\) let \(\Delta_{q_1,q_2}\) be the same difference for the diagram of \(U(M_1+M_2)\) with \(q_1\) rows \(\ell_1\) and \(q_2\) rows \(\ell_2\), \(\ell_1\ge\ell_2\ge0\), against \((\ell_1^{q_1})\) of \(U(M_1)\) and \((\ell_2^{q_2})\) of \(U(M_2)\). With \(M=M_1+M_2\), \(\exp\Delta_{q_1,q_2}\) is the product of the content factors \((M+c-r)/(M_1+c-r)\) on the first stack and \((M-q_1+c-r)/(M_2+c-r)\) on the second and of the hook ratios \((\ell_1-c+q_1-r+1)/(\ell_1-c+q_1+q_2-r+1)\) on the first \(\ell_2\) columns of the first stack (exact; checked in rational arithmetic, and equal to the two-row form at \(q_1=q_2=1\)), a function of the ranks and rows alone. With \(M_f=m_fN\), \(u_f=\ell_f/N\), \(G(m,u)=(m+u)\log(m+u)-m\log m-u\) and \(\Lambda=\sum_fq_f[G(m_1+m_2,u_f)-G(m_f,u_f)]\), which is positive and strictly increasing in each \(u_f\), the residual obeys \(|\Delta_{q_1,q_2}-N\Lambda|\le q_1q_2\log(\ell_1+q_1+q_2)+C\), with \(C\) depending only on \(m_f\), \(\ell_f/M\) and \(q_f\) (exact: each row sum is bracketed by its integral, the shift of the ranks by the row index is bounded by the mean-value theorem, and the hook ratios telescope); at fixed fractions the residual grows as \(q_1q_2\log N\) (numerical). So \(\Delta_{q_1,q_2}/N\to\Lambda\), linear in the depths and additive over the stacks: at the symmetric saddle \(\Delta_{q,q}/N=0.5209\), \(1.0379\), \(1.5515\) at \(N=3200\), \(q=1,2,3\), against \(0.5232\,q\) (numerical). The minimum of \(\Delta\) over two-row diagrams with \(|\ell'_f-\ell_f|\le b\) is therefore of order \(N\) for every \(b=o(N)\), with a deficit from the saddle value that is linear in \(b\), of slope \(\sum_f\log\frac{m_1+m_2+u_f}{m_f+u_f}\) at leading order (numerical). Perturbations of order \(N\) remove it: at the symmetric saddle the minimum over \(|\ell'_f-\ell_f|\le cN\) is attained at the far diagonal corner, is positive up to \(c=0.4975\) and vanishes at \(c=\tfrac12\), where the box contains the trivial diagram (numerical, exhaustive at \(N=400\) for \(q_1=q_2\le3\)), whereas removing the second stack leaves \(\Delta_{q,0}/(qN)=0.189\) at \(N=1600\), \(m=(\tfrac12,\tfrac13)\), \(q\le3\) (numerical).

\emph{Frame average at the saddle.} For a summand deformed by \(A_f\), with \(B_f=A_f^{\mathsf T}A_f\), the cap of axis \(n\) has \(s_f^2(n)=\tfrac14M_f(N-M_f)(\operatorname{tr}B_f-n\cdot B_fn)\) (exact; the general-axis form of the edge-datum identity). With \(\rho_f(n)=\tfrac12(\operatorname{tr}B_f-n\cdot B_fn)\), the squared edge-length fraction relative to \(B_f=\mathbf 1\), the saddle rows are \(\ell_f(n)=\ell_f^{(0)}\rho_f(n)^{1/2}\), and \(\Lambda\) depends on the frame through a sum of one term for each summand, strictly increasing and strictly concave in \(\rho_f\). The bound of the preceding paragraph involves the frame only through the rows, which are at most \(\ell_f^{(0)}(\operatorname{tr}B_f/2)^{1/2}\), so the average of \(\Delta_{q_1,q_2}/N\) over the two axes, taken independently and uniformly on the sphere, converges to the sphere mean of \(\Lambda\), uniformly over the frames. When the sphere mean of the squared edge-length fraction equals its round-frame value, \(\operatorname{tr}B_f=3\), that mean is bounded above by the round-frame value, \(0.523248144\,q\) at \(m_f=\tfrac12\), \(\ell_f^{(0)}=N/2\), \(q_1=q_2=q\), with equality only for \(B_f\propto\mathbf 1\), and below by the value at the axis of the largest eigenvalue of \(B_f\), which is positive unless the transverse edge data of a summand degenerate. For \(B_f=\operatorname{diag}(\tfrac12(3-\gamma),\tfrac12(3-\gamma),\gamma)\), at these values and \(q=1\), the averaged limit is \(0.522655\), \(0.519217\), \(0.511350\) and the frame minimum \(0.479485\), \(0.396700\), \(0.268892\) at \(\gamma=1.4\), \(2\), \(2.6\); the finite-\(N\) residuals stay below \(7.7\) for two rows and \(59.8\) at depth three for \(N\le3200\), the stacked limits are the depth times the averaged profile, reproducing the isotropic values of the stacked-rows paragraph at the round frame, and the ratio of \(\mathrm d\log\dim/\mathrm d\log M\) to \(|\mu|\) at the saddle stays between \(0.7858\) and \(0.9023\) (numerical). A sampled frame scan checks the inequality: at \(N=3200\) with symmetric block ranks and saddle parameter one (\(\ell_f^{(0)}=1131\)), over \(150\) sampled frames with \(\operatorname{tr}B=3\) the worst residual is \(7.1\) for two rows and \(54.9\) at depth three, against values of the row-dependent form of the bound between \(8.6\) and \(9.0\) and between \(74.8\) and \(80.2\) (\(8.8\) and \(77.0\) at the round frame), with no violation at \(N=400\), \(1600\) and \(3200\) (numerical, sampled frame grids). This is an average over cap frames at fixed saddle parameter, not the frame average or the minimisation over frames of~\cite{FlissFrenkelHartnollSoni2025}.

\emph{Coincident copies and the multiplicity reading.} The direct sum of \(q\) equal summands, \(\widetilde X=\mathbf 1_q\otimes X\) with \(\widetilde\Theta=\mathbf 1_q\otimes\Theta\) for one cap, is, for undeformed summands, the background \(J^a\otimes\mathbf 1_q\) of the transplanted selection rule; the further conditional reading used here is that multiplicity \(q_f\) of a nonzero eigenvalue of the charge is read as \(q_f\) equal rows, at fixed depths. For copy-invariant momenta \(\mathbf 1_q\otimes\Pi\) the charge is \(\mathbf 1_q\otimes Q\) (exact), so every nonzero eigenvalue has multiplicity \(q\) and the stacked diagram of common depth \(q\) is read; for generic momenta on the same background the rank is the same but the eigenvalues are simple (numerical), so the multiplicity is a property of the state, not of the background alone. For \(q_f\) coincident copies of summand \(f\) of the direct sum, with momenta copy-invariant within each group and without entries between the groups, the charge is \(\bigoplus_f\mathbf 1_{q_f}\otimes Q_f\) and the stacked diagram \((\ell_1^{q_1},\ell_2^{q_2})\) is read (exact). For the band-separated caps of the Row length paragraph, whose combined spectrum has multiplicity \(1\), no stacked diagram is selected: with saddle rows and depths \((q_1,q_2)\) the stacked moment signature exceeds the multiplicity-\(1\) signature by the fraction \(\sum_f(q_f-1)w_f^p/\sum_fw_f^p\), with \(w_f=k\,m_f(1-m_f)\) and \(k\) the edge-length coefficient of the factor, independent of \(N\) and \(t\): it is \(9/17\) at \(p=1\) and \(81/145\) at \(p=2\) for \((q_1,q_2)=(2,1)\), \((m_1,m_2)=(\tfrac12,\tfrac13)\), \(k=1\), and \(1\) at equal depths \(2\) (exact), a mismatch of leading order in \(N\). For one cap in each of \(q\) summands, or \(q\) coincident copies, the charge is \(-2\mathrm i(UR^\dagger-RU^\dagger)\), with \(U\) the matrix of the orthonormal edge vectors and \(R\) that of the edge rows; with \(C_0=U^\dagger R\), \(Z_0=R^\dagger R\), \(H=(C_0-C_0^\dagger)/(2\mathrm i)\) and \(K=Z_0-C_0^\dagger C_0=R^\dagger(\mathbf 1-UU^\dagger)R\succeq0\), its nonzero spectrum is that of \(-2\mathrm i\left(\begin{smallmatrix}C_0^\dagger&Z_0\\-\mathbf 1_q&-C_0\end{smallmatrix}\right)\), whose characteristic polynomial is \(\det(\lambda^2\mathbf 1_q+4\lambda H-4K)\), so \(\operatorname{Re}C_0\) never enters (exact). If \(H\) and \(K\) are block-scalar, \(h_f\mathbf 1_{q_f}\) and \(n_f\mathbf 1_{q_f}\) with \(n_f>0\), the polynomial is \(\prod_f(\lambda^2+4\lambda h_f-4n_f)^{q_f}\), and the spectrum is the union of \(q_f\) copies of the Row length pair \(-2h_f\pm2(h_f^2+n_f)^{1/2}\); every such datum is realised by \(R=U(A+\mathrm iH)+VK^{1/2}\), with \(A\) real and block-scalar and \(V\) an isometry onto vectors orthogonal to those of \(U\); for \(K=n\mathbf 1_q\) alone the pairs are those of the eigenvalues \(h_f\) of \(H\) (exact). For two diagonal pairs, as for block-diagonal momenta, the quartic \(\lambda^4+a\lambda^3+b\lambda^2+c\lambda+d\) is the square of a real quadratic if and only if \(h_1=h_2\) and \(n_1=n_2\), that is \(\operatorname{Im}\alpha_1=\operatorname{Im}\alpha_2\) and \(|w_{\perp,1}|=|w_{\perp,2}|\), since \(64d-(4b-a^2)^2=-256[(h_1-h_2)^4+2(h_1-h_2)^2(n_1+n_2)+(n_1-n_2)^2]\); a double root need not be a double pair, the pairs \((h,n)=(3,7)\) and \((5,11)\) giving \((\lambda-2)^2(\lambda+14)(\lambda+22)\) (exact). For \(K=n\mathbf 1_q\) a double eigenvalue occurs exactly when two \(h_f\) coincide, a set of real codimension three among Hermitian \(H\), and otherwise the \(2q\) eigenvalues are distinct, with gaps bounded below linearly in \(\min_{f\ne g}|h_f-h_g|\) (exact). At \(h_f=0\) the ratio of \(\sum_je_j^{2p}\) over the nonzero eigenvalues \(e_j\) to its multiplicity-\(1\) value is \(1+\sum_f(q_f-1)n_f^p/\sum_fn_f^p\), the stacked signature above with \(n_f\) in place of \(w_f\), with excess \(9/17\) at \(p=1\) and \(81/145\) at \(p=2\) for \((q_1,q_2)=(2,1)\), \((n_1,n_2)=(\tfrac14,\tfrac29)\) (exact), so in this class the excess is carried by the charge spectrum itself. Within independent Gaussian momenta exact multiplicity is not typical: none of \(6000\) draws at \(q=2\) and \(3\) has it, and along a generic perturbation of copy-invariant momenta the relative gap \(D_{\mathrm{gap}}=\max_{k=1,2}(e_{kq}-e_{(k-1)q+1})/\max_j|e_j|\) of the ordered nonzero eigenvalues grows linearly (numerical). At leading order in \(N\) it is approximately restored when the copies have equal scales: for independent standard complex Gaussian momenta at \(q=2\), with \(M=N/2\), the medians of \(D_{\mathrm{gap}}\) and of \(U_2=\operatorname{Tr}Q^4/\bigl(2q(\operatorname{Tr}Q^2/(2q))^2\bigr)-1\) fall from \(0.28\) and \(0.099\) at \(N=50\) to \(0.11\) and \(0.013\) at \(N=400\), as about \(N^{-1/2}\) and \(N^{-1}\), because the \(h_f\) stay of order one while the \(n_f\) grow as \(M\); with per-copy scales \((1,1.6)\) the median of \(D_{\mathrm{gap}}\) stays near \(0.4\) from \(N=120\) to \(480\) (numerical, sampled edge rows). This is consistent with the \(q\) equal rows of~\cite{Frenkel2023EdgeModes} for equal copies at leading order, and the scale mismatch shows that equal rows at leading order require equal norms of the edge rows.
```

### C2. Replacement of the stale closing scope sentence

- Replace the whole unique line that starts with `These statements are for a compact factor with positive
  contraction, a single projector at fixed frame for the deformed sphere and the two caps,` (current L2930; count 1).
- Replacement: `closing_r2.tex` (1,072 B, sha256 a24fcb157724c0f709cf505d26c6546b49262b4e1c64ff764a1da66db1fb6272).
- The second and third sentences of the original are kept in substance; the third ("They derive no entropy density
  ... PROGRAMME-CONDITIONAL.") is kept verbatim. This is the single scoped status sentence for the block.

```latex
These statements are for a compact factor with positive contraction; for a single projector on the deformed sphere, for the two band-separated caps of one axis and for direct sums of deformed spheres with one cap in each summand, at fixed frame except for the stated average over cap frames at fixed saddle parameter; for the leading semiclassical order with one dominant representation, read through the transplanted selection rule at fixed depths; and for Gaussian states with the stated variances or the stated momentum data. Items~(i) and~(iii) of the bearing paragraph apply to every block treated; the frame average and the minimisation of~\cite{FlissFrenkelHartnollSoni2025} are used for its state and not re-derived, and the two-sided diagrams are not computed. They derive no entropy density on \(\partial M\), no value or scaling of \(S_{\mathrm{ent}}^{\mathrm{(IR)}}\), no boundary stationarity and no \(\Lambda_{\mathrm{eff}}\); Assumptions~\ref{ass:Sent-density} and~\ref{ass:bdy-EE} are not discharged, and Problem~G remains open and PROGRAMME-CONDITIONAL.
```

### C3. Bibliography (integrator adds to `bib/namcg.bib`)

- Verified: arXiv abstract page (single author Alexander Frenkel, exact title, v1 16 Nov 2023, no journal ref) and
  the PDF text (36 pages).

```bibtex
@misc{Frenkel2023EdgeModes,
  author  = {Frenkel, Alexander},
  title   = {Entanglement Edge Modes of General Noncommutative Matrix
             Backgrounds},
  year    = {2023},
  eprint  = {2311.10131},
  archivePrefix = {arXiv}
}
```

### C4. Dependency, not part of this package

Local 067 `appH_insert_r2.tex` (accepted r2) goes immediately before `\section{Problem H: modular origin of the
interpolating function}`, as in R6.

### Labels

- Labels used, all verified to exist once: `ass:Sent-density` (ch12 L139), `ass:bdy-EE` (ch12 L185).
- Citations: `FlissFrenkelHartnollSoni2025` (bib L994) and `Frenkel2023EdgeModes` (new).
- No new `\label`, no `\ref` to a new label, no `$`, no process language.

### Expected bytes (current tree pins)

| File | State | Bytes | sha256 | CRLF / bare LF |
|---|---|---|---|---|
| appH | PRE | 648,097 | fa3e318109a21b7df1562641d661179f5ba5ca03db97e6cc3e537e5eea000384 | 3428 / 0 |
| appH | POST, 067 then this block | 676,267 | a4dca867b648808ed88177be6322a2c93bc428cd3ce2f7dc8157093e48dd541d | 3463 / 0 |
| appH | POST, this block only | 662,991 | 5fac5620eb478e6330dcc1911709e02d9e709b4f02f9bd90c4b1bb94bc99b3c7 | 3436 / 0 |
| bib | PRE | 31,439 | b727e7d6... | 1050 / 0 |
| bib | POST | 31,682 | a7aec454de0f6591c157ecb4709179f212c876b6f0df5df67713df85bb0493ed | 1059 / 0 |

### Stale passages elsewhere

- None in chapters.
- The pending gpu 081-088 texts contain "its diagonal-cut convention" (081) and references to "the selection-rule
  paragraph". Their r2 must drop the former (E1) and refer to the paragraph titled "Two-component blocks and the
  transplanted selection rule".

### Map of required revisions (group5-G1.md) to this text

| Item | How it is addressed |
|---|---|
| 072 BLOCKING | Decision (b). The review's minimal selection sentence is used with "such as the direct sum above or the two band-separated caps of one axis" (the review's text names only (a); (b) is the chosen instance) and "the block Θ1⊗Θ2 of the product of two spheres, treated in the toric-block paragraph below" in place of "the block Θ1⊗Θ2 above", because the product is no longer defined in this block. |
| 072 minor "M2=N/3, k1=k2" | Moot: the corner sentence is deleted, because in the direct sum Tr E^p is exactly additive. |
| 072 minor "Define Θ and E" | Done: Θ = Θ1 ⊕ Θ2; E defined in the first sentence. The product is cited to 067. |
| 072 minor "(the approximate form holds for ℓ_f ≪ M_f)" | Appended verbatim where the approximate excess is referenced. Bearing (ii) itself is not edited. |
| 073 | "a function of the ranks and rows alone" is in the merged paragraph; the 079 bound is stated there. |
| 074 | "product testbed" is removed; the paragraph is merged. |
| 075 | Two-factor averaging becomes two summands, independent. Corner sentence deleted. "squared edge-length fraction" verbatim. "reproducing the isotropic values of the stacked-rows paragraph at the round frame" verbatim. |
| 076 | Product comparison replaced by the direct-sum group statement. "w_f = k m_f(1−m_f), with k the edge-length coefficient of the factor" and "k = 1" verbatim. |
| 077 | The forward-reference fix is absorbed: in the merged paragraph the general-q form precedes the q = 2 criterion, and the q = 2 criterion is now derived from it. The clause the review would have edited no longer exists. |
| 079 | "this bound is established with explicit constants": the content is kept as "(exact: ...)". The "previously verified" clause is removed. The scan sentence is used verbatim with two normalisation insertions (R4). |
| 080 | "with excess 9/17 at p = 1" verbatim, extended with "and 81/145 at p = 2". |
| Group-wide | All eight "close(s) nothing" clauses removed (the apply script asserts the count is 0); one status sentence; stale scope sentence replaced; compression. |

## Verification scripts

All scripts are run from the repository root with `python -I`. Outputs are saved next to each script.

| Script | What it checks | Expected invariant |
|---|---|---|
| `d1_direct_sum.py` | Direct-sum edge datum (a); E spectrum and moments (b); union and pair formula (c); inter-summand failure at small N (d); groups of copies (e); complementary caps (f) | all deviations < 1e-9; (d) min relative deviation 2.239e-01; `PASS d1` |
| `d2_pencil_typicality.py` | Symbolic and numeric pencil identity (a); block-scalar spectrum (b); q = 2 criterion and example (c); 9/17 and 81/145 (d); typicality medians and slopes (e), (g); inter-summand union decay (f) | D slope −0.447, U2 slope −0.992, mismatched D slope −0.062, (f) slope −0.471, (g) slope −0.556; `PASS d2` |
| `d3_defect_frame.py` | Closed form, 1620 cases (a); 37/72 (b); 0.520906, log(27/16), 0.8111 (c); q² log 2 increments (d); γ-family values (e); concavity (f) | `PASS d3` |
| `runs/run_inherited.sh` (`sh proposals/local-gpu/072-080-r2/runs/run_inherited.sh`) | Re-runs 28 inherited gpu scripts (072 s1-s3, 073 s4-s5, 074 s1-s3, 075 s1-s3, 076 s1-s4, 077 s1/s3/s4b/s5/s6, 078 s1/s2b/s3, 079 s1-s2, 080 s1-s3) | every line rc=0, then `DONE`; outputs in `runs/*.out`, summary `runs/summary.txt` |
| `normalize_crlf_r2.py` | Normalises the snippets to CRLF UTF-8 without BOM | idempotent |
| `apply_build_r2.py OUTDIR --build` (OUTDIR outside the repo) | Applies R1-R4 in memory; writes the applied copies; builds in OUTDIR/build (pdflatex, bibtex, pdflatex x2) | POST hashes as in the table above; `BUILD PASS pages=394`; 0 undefined/multiply-defined; 0 bibtex warnings for the new key |

The applied-copy build of this round ran in a session scratchpad outside the repository and was deleted afterwards.
Its output is in `apply_build_r2.out`.

## Decisions Taken

1. **072 RESEARCHER-DECISION: option (b), the direct-sum background.** The reasons are in R1.
   - It preserves every derived number.
   - It removes the corner exactly.
   - It makes the two-row U(M1+M2) reading valid.
   - It identifies the coincident copies of 076-080 with Frenkel's U(q) background, which strengthens the
     connection to the cited rule.
   - It keeps independent frames.

   Rejected:
   - (a) as the primary instance: m1+m2 < 1 kills the symmetric numbers and the c = ½ breakdown, and forces a
     common axis. (a) is kept as a second instance.
   - (c): the defect object would be wrong, and it duplicates 067.
2. **076 product comparison: replaced, not deleted.** The direct-sum group statement is the exact analogue and
   supplies the realisation of per-summand depths that 080 needs. The product q1q2 statement concerns a block to
   which the reading does not apply, so it is dropped.
3. **E1: corrected in the text** (the transplant is described exactly) rather than only flagged. The gpu
   "diagonal-cut convention" qualifiers are removed throughout.
4. **E2 and E3: corrected** by stating the established 079 bound and the correct uniformity reason.
5. **077 numerics.**
   - Quoted only from passing runs: 077 s1, and my d2 sampler.
   - The unreproduced s2/s2b grids are dropped.
   - The rates quoted are my d2 medians.
6. **067: cite, ordered before this block in integration, placed after it in the text.** Not absorbed: 067 has its
   own accepted scope and its own status sentence.
7. **Compression.** 12 paragraphs become 4, merged by shared derivation. The stable title "Two-component blocks and
   the transplanted selection rule" defines "the transplanted selection rule" for 081-088.

## Milestone assessment

Routine. A bounded, conditional sharpening of a no-go inside a compact-factor proxy. No critical-path step is
derived and no MILESTONE.md trigger applies.

## Status-label recommendation

- The current critical-path list (Chapter 17 and the ledger) is A, B, C, D1, E, F, G-derived, N.
- Affected label: Problem G, unchanged (OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL).
- No label change is proposed.

## Author decision needed

None.

## Remaining open step

**For G-derived (unchanged):**
- a derivation from the matrix theory of the entropy density of `ass:Sent-density` on ∂M of the emergent spacetime;
- boundary stationarity `ass:bdy-EE`;
- then Λ_eff.

**Bounded obstruction recorded here.** At leading order, log d_μ is not additive over disconnected components
(rank dependence, Δ = Θ(N)). Its hypothesis class:
- H1: compact factor with positive contraction;
- H2: leading semiclassical order, one dominant irrep;
- H3: the FFHS block subsystem with U(M1+M2) edge group;
- H4: fixed frame or cap-frame average;
- H5: supplied Gaussian states;
- H6: rows from the transplanted selection rule.

**Explored here:**
- H4: survives the average;
- H6: survives o(N) perturbations and stacked diagrams; fails under O(N) perturbations;
- H5: inter-summand entries keep the union only at leading order.

**Open avenues, ranked:**
1. **Split algebra (relax H3).** Use a subsystem algebra without the cross blocks Θ1 X Θ2 between components (edge
   group U(M1) x U(M2)). Bearing (ii) identifies these blocks as the cause. In the direct-sum picture they are the
   open strings between the two branes. The question is which algebra is the algebra of a region with disconnected
   components, and whether its factorisation map exists.
2. **Two-sided diagrams of FFHS (±ℓ rows)** (relax the polynomial-diagram class in H6); not computed.
3. **Depth-cancelling (mutual-information type) combinations** across separations.
4. **Spacetime-block subsystem** of a non-compact or Lorentzian leaf (relax H1; 065 avenue 1, untried).
5. **Within-core state**, e^{−S/2} or OS reconstruction (relax H5).
6. **A derivation of the rows-from-moments step** for supplied states and distinct summands, which would remove the
   transplant.

## Special instructions for the gatekeeper

- **Full scan owed** (3(c) and 3(d)): not performed by the researcher.
- **E1:** re-verify against the PDF of arXiv:2311.10131 (§5 and the Fig. 10 caption; §3.2 eq. 3.16-3.19).
- **Do not let the text assert:**
  - that the block or its edge is a region or boundary of the emergent spacetime;
  - that the rule is derived for supplied states;
  - any minimised or FFHS-frame-averaged entropy;
  - any statement about ∂M or Λ_eff.
- **Re-check:**
  - the pair-formula sign convention, h = Im(u|w) with (w| = (u|Y (d1);
  - that "connected edge" for Θ1⊗Θ2 is consistent with 067;
  - that the anchor R1 is the line-start form (the bare string occurs twice).
- **Integration order:** 067 (accepted) first, then this block. Re-verify both anchors against the live tree.
- **078:** plain ACCEPT on gpu, but its text is compressed here (all its exact results kept, the spacing bound
  stated qualitatively). It therefore needs re-review as part of this block.
