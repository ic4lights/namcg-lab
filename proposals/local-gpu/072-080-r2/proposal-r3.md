# Proposal local-gpu 072-080 (Problem G edge-sector block), round 3

## Result

This round answers review-r2 (verdict AWRR: one major finding, M1, and minors R2-R6). It applies R1-R6 exactly as
the review words them. It also re-derives the two corrected scale statements and extends the scripts to test them.
The package is still a bounded, conditional sharpening inside the Problem G edge-entropy paragraph, and it closes
nothing.

1. **M1 (R1), the residual depends on whether the row fractions are equal (re-derived, exact mechanism).**
   - The hook ratios of the stacked defect telescope exactly:
     Π_{c=1}^{ℓ2} (a−c)/(a+q2−c) = Π_{j=0}^{q2−1} (a−ℓ2+j)/(a+j), with a = ℓ1+q1−r+1.
   - The hook part of Δ_{q1,q2} is therefore
     Hk = Σ_{r=1}^{q1} Σ_{j=0}^{q2−1} log[(ℓ1−ℓ2+q1−r+1+j)/(ℓ1+q1−r+1+j)].
     - At u1 = u2 it is −q1q2 log N + O(1).
     - At u1 > u2 it tends to q1q2 log((u1−u2)/u1), which is bounded.
   - The content (row-sum) part, minus NΛ, is bounded in both cases. Numerically, its increments per doubling of N
     are ≤ 0.0035 and decrease.
   - So the q1q2 log N growth quoted in r2 holds only at equal fractions, which is the symmetric saddle. At the
     unequal fractions tested, the residual stays bounded.
   - The established bound |Δ − NΛ| ≤ q1q2 log(ℓ1+q1+q2) + C is unaffected. Its logarithm is attained only at
     u1 = u2.
2. **R2, the scale dependence of the union with entries between the summands (re-derived).**
   - At equal scales, the diagonal entries K11 and K22 of the edge-row Gram matrix differ by O(D^{1/2}). This is the
     same order as the coupling K12, so the perturbation is degenerate and the relative distance is O(D^{−1/2}).
   - At unequal scales, K22 − K11 is about 2(σ2² − σ1²)D. The shift is then second order, |K12|²/(K22 − K11) = O(1),
     and the relative distance is O(D^{−1}).
   - d1(g) confirms this numerically:
     - slope −0.463 at scales (1,1);
     - slope −0.989 at (1,1.6) and −1.022 at (1,3);
     - D × median roughly constant at unequal scales (1.6-1.8 and 0.65-0.76).
   - The text now states the quoted numbers only for M1 = M2 and s1 = s2, which is the review's wording.
3. **R3-R5: wording, applied verbatim.**
4. **R6, PRIOR-CLAIM-ERROR (scoping), applied in two places.**
   - The integrated Bearing (ii) sentence (appH L2926) is changed by a separate anchored replacement.
   - The parenthesis in the block is changed as well.
   - Derivation of the ℓ²/M term: see R6 below. The gatekeeper's gk_approx case is reproduced to within 0.07.
5. **Integration order (unchanged):**
   1. local 067 (`proposals/067-product-sphere-edge/appH_insert_r2.tex`, sha256 f0fa634c..., unchanged);
   2. then the block;
   3. then the closing sentence;
   4. then the R6 Bearing replacement.

   The applied-copy build outside the repository passes: 394 pp, 0 undefined or multiply-defined references.

## Target and status

- **Status: unchanged from r2.** I re-read appH L2886-2932 and the ch17 G passages in the current tree.
- **Appendix H, L2890:** "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL". G-model and
  G-external are reduced-scope only.
- **Chapter 17:** G-derived requires the entropy density of `ass:Sent-density` and the stationarity of `ass:bdy-EE`
  to be derived from the matrix theory, and Λ_eff to follow from them.
- **Original target:** S_ent^(IR) and boundary stationarity from the matrix theory, then Λ_eff.
- **This package:** PROGRAMME-CONDITIONAL. It is evidence about the edge-mode functional of a block of a compact
  factor (a region of the factor, not of the emergent spacetime).
- **Dependencies:** as in r2. They are FFHS (`FlissFrenkelHartnollSoni2025`), arXiv:2311.10131 (new key
  `Frenkel2023EdgeModes`), the supplied Gaussian states, and local 067.
- **Critical-path set** (Chapter 17 and the Appendix H status lines at L16, 103, 462, 627, 1513, 1705, 2890 and
  3293): A, B, C, D1, E, F, G-derived and N. All 8 are OPEN.
- **Optional problems:** H, I and J (L2936, 3023, 3168), all OPEN.
- No discrepancy between Chapter 17 and Appendix H.

## Source reading

**Digest + targeted reads. No full scan was performed.**

- `python scripts/make_digest.py --check` printed `DIGEST CURRENT`, with `dirty-chapters: yes`.
- appH SHA-256 fa3e3181..., identical to the r2 pin.
- Read in this round:
  - `scratch/digest.md` (head);
  - `review-r2.md` in full;
  - `proposal-r2.md` in full;
  - appH L2926 (the Bearing paragraph line) in full;
  - the status lines of every Problem section in appH;
  - the 067 insert's Bearing line (L24 of `appH_insert_r2.tex`);
  - the three gk scripts and the r2 scripts d1 and d3.
- **Full scan owed** under 3(c) and 3(d). The review assigns it to the re-review passes.

## Research and reasoning

### R1 (M1). Equal against unequal row fractions

Write exp Δ_{q1,q2} = (content factors) × (hook ratios), as in the block.

**Telescoping.** For row r of the first stack, put a = ℓ1+q1−r+1. The hook ratios over the first ℓ2 columns are
Π_{c=1}^{ℓ2} (a−c)/(a+q2−c).
- The numerator is (a−1)!/(a−ℓ2−1)!.
- The denominator is (a+q2−1)!/(a+q2−ℓ2−1)!.
- Their ratio is [(a+q2−ℓ2−1)!/(a−ℓ2−1)!] / [(a+q2−1)!/(a−1)!] = Π_{j=0}^{q2−1} (a−ℓ2+j)/(a+j).
- So the hook part is Hk = Σ_{r=1}^{q1} Σ_{j=0}^{q2−1} log[(ℓ1−ℓ2+q1−r+1+j)/(ℓ1+q1−r+1+j)]. It has exactly q1q2
  factors.
- Status: established. d3(g1) checks it in Fractions on 810 cases with 0 failures.

**Equal fractions** (u1 = u2, so ℓ1 = ℓ2 = ℓ). Every numerator is O(1) (between 1 and q1+q2−1) and every
denominator is ℓ + O(1). So Hk = −q1q2 log ℓ + O(1) = −q1q2 log N + O(1).

**Unequal fractions** (u1 > u2 fixed). Every factor is (ℓ1−ℓ2+O(q))/(ℓ1+O(q)), which tends to (u1−u2)/u1. So
Hk = q1q2 log((u1−u2)/u1) + O(q³/(N(u1−u2))). This is bounded in N, but it diverges as u2 → u1. The crossover to the
log N regime is at ℓ1 − ℓ2 = O(q).

**Content part.**
- The rows give Σ_r Σ_c log[(M+c−r)/(M1+c−r)] and Σ_r Σ_c log[(M−q1+c−r)/(M2+c−r)]. The summands are smooth
  functions of c/N on [0, u_f], and the row shifts are O(q/N).
- By the Euler-Maclaurin bracket used in the 079 bound, each sum equals N times its integral plus O(1). The O(1) part
  depends on m_f, ℓ_f/M and q_f. The integrals reproduce NΛ.
- So NΛ − (Δ − Hk) = O(1) in both regimes.
- Numerically, d3(g2) and (g3) find content-part increments per doubling of at most 0.0035 in absolute value,
  decreasing in N, at every fraction tested, including the equal one.

**Conclusion.**
- The residual is NΛ − Δ_{q,q} = −Hk + O(1).
- It grows as q1q2 log N at equal fractions. This reproduces the r2 increments 0.692, 2.767 and 6.220 against q² log 2.
- It is bounded at unequal fractions. At N = 3840, −Hk = 0.916, 3.659 and 8.226 at (½,½; ½,3/10), for q = 1, 2, 3,
  against q² log(u1/(u1−u2)) = 0.916, 3.665 and 8.247.
- d3(g2) checks four fraction sets (one equal, three unequal), q = 1, 2, 3 and N = 480-3840. Every unequal residual
  is < 10.1, and the last increments are 0.001-0.031.
- This agrees with gk_hc_r2, which I re-ran: residuals 0.924-0.930 at q = 1 and 8.185-8.354 at q = 3 for
  (½,½,½,0.3). The (½,⅓,0.4,0.25) residuals oscillate by ±0.06 because the gk script rounds M2 = N/3. d3(g) avoids
  this by choosing N divisible by 30 and evaluating Λ at the exact integer fractions.

**Consequences.**
1. The r2 statement "at fixed fractions the residual grows as q1q2 log N" was too broad. It is replaced by the review's
   wording, which is now derived.
2. The established bound |Δ_{q1,q2} − NΛ| ≤ q1q2 log(ℓ1+q1+q2) + C needs no change. It is sharp in its logarithm only
   at u1 = u2.
3. The r2 Result item E2 (on 074's "of order q log(ℓ1+1) uniformly in N") still holds at the symmetric saddle, where
   the coefficient is q1q2, not q. At unequal fractions neither form describes the residual, which is O(1). The
   manuscript text never quotes 074's form, so nothing else changes.

### R2. Scale dependence of the union with entries between the summands

**Setting** (d2(f), now d1(g)).
- The edge rows are r_f = σ_f g_f, with g_f iid standard complex Gaussian on C^D, where D is the block rank.
- The edge vectors are e_0 and e_{D/2}.
- The nonzero spectrum of Q is that of the 2q × 2q pencil, with characteristic polynomial det(λ² + 4λH − 4K)
  (established in the block). At D = 50 and 100 it agrees with the full D × D charge to within 2.1e-15.
- The "union" is formed from the diagonal entries H_ff and K_ff, that is, from the full edge rows.

**Orders.**
- H = O(1), because its entries are imaginary parts of single Gaussian entries.
- K_ff = σ_f² (2D + O(D^{1/2})).
- K_12 = σ1σ2 O(D^{1/2}).
- The eigenvalues are ±2 κ_i^{1/2} + O(1), where κ_i are the eigenvalues of K.

**Equal scales.**
- K11 − K22 = O(D^{1/2}) is of the order of K12, so the perturbation is degenerate.
- κ_i − K_ii = O(D^{1/2}), the eigenvalues move by O(1), and the relative distance is O(D^{−1/2}).
- The H12 coupling also enters at first order, again as an O(1) absolute shift.

**Unequal scales.**
- K22 − K11 = 2(σ2² − σ1²)D + O(D^{1/2}).
- κ_i − K_ii = |K12|²/(K22 − K11) = O(1) at second order, so the eigenvalue shift is O(D^{−1/2}).
- The relative distance is O(D^{−1}). The H12 effects are also second order.

**Numbers** (d1(g), 400 draws, D = 50-1600):

| Scales | Medians | Slope |
|---|---|---|
| (1,1) | 0.0797 → 0.0155 | −0.463 |
| (1,1.6) | 0.0357 → 0.0011 | −0.989 |
| (1,3) | 0.0142 → 0.0004 | −1.022 |

- At unequal scales, D × median is about 1.6-1.8 and 0.65-0.76.
- At every D, the unequal-scale medians are below the equal-scale median.
- This agrees with gk_sign_r2 as re-run: (1,1.6) gives 0.0298, 0.0079, 0.0023 and (1,3) gives 0.0134, 0.0037, 0.0008
  at 50, 200, 800.

**The quoted numbers.** The values 0.086 at 50 and 0.023 at 800 in the text are the d2(f) medians (seed 72081),
taken at equal scales. The d1(g) values with an independent seed (0.0797 at 50, 0.0219 at 800) agree with them.

**Decision on the wording.** The text is scoped to M1 = M2, s1 = s2, using the review's wording. The unequal-scale
O(D^{−1}) behaviour is recorded here and is not added to the text. The equal-scale case is the conservative (largest)
deviation, and the review asked for exactly this sentence.

### R3-R5

Wording only. Each replaced string occurs exactly once in `insert_block_r2.tex`; the counts were asserted when
`insert_block_r3.tex` was generated.
- **R4.** `2\le M_f<N` makes the cap proper. At M_f = N the projector is the identity of the summand and has no edge,
  which is the same mechanism as d1(f).

### R6. Correction order in Bearing (ii)

For one row:
log[(M−1+c)/(M1−1+c)] = log(M/M1) + log(1+(c−1)/M) − log(1+(c−1)/M1).

Summing over c = 1..ℓ1 gives
ℓ1 log(M/M1) − (ℓ1²/2)(1/M1 − 1/M) + (ℓ1³/6)(1/M1² − 1/M²) + O(ℓ1/M1).

- 1/M1 − 1/M = M2/(M1 M) ≤ 1/M1, so the leading correction is of order ℓ1²/M1. Likewise the second row gives
  ℓ2²/M2.
- The hook factor adds −log((ℓ1+1)/(ℓ1−ℓ2+1)), which is of the order of a logarithm.
- **Check against gk_approx_r2** at M1 = M2 = 10⁴, ℓ1 = 1000, ℓ2 = 500:
  - predicted: −25 − 6.25 + 1.25 + 0.16 − 0.69 = −30.53;
  - observed: −30.60.
- The correction is small relative to the leading term when ℓ_f ≪ M_f, but it is unbounded unless ℓ_f² = O(M_f).
  This is why "of the order of a logarithm" was wrong as stated.
- The block's parenthesis becomes "holds at leading order for ℓ_f ≪ M_f", consistent with this.

## Claim classification

**Changed or added this round:**

| Claim | Class |
|---|---|
| Hook-ratio telescoping, Hk with q1q2 factors | established (exact) |
| Residual −Hk + O(1); q1q2 log N at u1 = u2; bounded at u1 > u2 | derived asymptotics, with the O(1) content part from the 079 bracket; the text says "numerical" (review wording) |
| Equal-scale O(D^{−1/2}) against unequal-scale O(D^{−1}) distance from the union | perturbative derivation plus numerics; the text quotes equal-scale numerics only |
| ℓ1²/M1 + ℓ2²/M2 and log correction in Bearing (ii) | derived expansion plus numerics |

All other claims keep their r2 classes. Entropy density on ∂M, Λ_eff and stationarity are not derived.

## Proposed changes

**File:** `chapters/appH-microscopic-proofs.tex`, Problem G section only.

### C0. Dependency, first (unchanged)

- Insert local 067 `proposals/067-product-sphere-edge/appH_insert_r2.tex` (sha256
  f0fa634cbae16d6c41366f72a8c4e3f834b26fbe31d37532204eb513b6c014ee, normalised to CRLF), followed by one blank CRLF
  line.
- Position: immediately before the unique line `\section{Problem H: modular origin of the interpolating function}`
  (line-start count 1).

### C1. Block

- Insert `insert_block_r3.tex` (14,782 B, CRLF 7, sha256
  13f2de4b0ff55fa4fefae94b232b122367a6b045571014b2e049a5397185e80e), followed by one blank CRLF line.
- Position: immediately before the unique line that starts with `\emph{Vacuum term.} The abstract
  of~\cite{Steinacker2023}` (line-start count 1, live tree and after C0).
- It differs from `insert_block_r2.tex` only by the six replacements R1-R6(b) of review-r2, each of whose old strings
  occurred exactly once.

```latex
\emph{Two-component blocks and the transplanted selection rule.} Let \(X^a=X^a_1\oplus X^a_2\) on \(\mathbb C^N\oplus\mathbb C^N\) be the direct sum of two deformed spheres \(X^a_f=A_f{}^a{}_bJ^b\) of the edge-datum paragraph, and let \(\Theta=\Theta_1\oplus\Theta_2\), with \(\Theta_f\) the spectral projector of \(n_f\cdot J\) on its \(M_f\) largest eigenvalues in summand \(f\), \(2\le M_f<N\); the subsystem of~\cite{FlissFrenkelHartnollSoni2025} attached to \(\Theta\) is invariant under \(U(M_1+M_2)\times U(2N-M_1-M_2)\). Then \(X^a_{\Sigma\bar\Sigma}=c^a_1|u_1)(v_1|+c^a_2|u_2)(v_2|\), with \(u_f,v_f\) in summand \(f\); the nonzero spectrum of \(E=\sum_a\Theta X^a\bar\Theta X^a\Theta\) is \(\{s_1^2,s_2^2\}\), with \(s_f^2=k_fM_f(N-M_f)\) and \(k_f=\tfrac14(\sigma_{f,1}^2+\sigma_{f,2}^2)\), so that \(\operatorname{Tr}E^p=s_1^{2p}+s_2^{2p}\) for every \(p\); and for momenta without entries between the summands the nonzero spectrum of \(Q\) is the union of the two single-cap pairs of the Row length paragraph (exact). The two caps of one axis of the Row length paragraph give the same union, with \(k_1=k_2\), when \(M_1+M_2<N\) and the edges are band-separated; at \(M_1+M_2=N\) their projector is the identity and has no edge. For independent identically distributed Gaussian momenta, which have entries between the summands, the union holds only approximately: at \(M_1=M_2\) and \(s_1=s_2\) the median relative distance of the spectrum from the union of the two pairs formed with the full edge rows, whose norms then also include their entries in the block of the other summand, is \(0.086\) at block rank \(50\) and \(0.023\) at rank \(800\), decaying as about the inverse square root of the rank (numerical). The selection rule of~\cite{Frenkel2023EdgeModes} is derived for the block partition of the matrix degrees of freedom, the cut of the subsystem of~\cite{FlissFrenkelHartnollSoni2025} above, on the fuzzy sphere, in Gaussian states of the quadratic fluctuations about it, and argued for general noncommutative backgrounds: at leading order in \(N\) the moments \(\operatorname{Tr}Q^{2p}\) fix the dominant diagram, with one row for each disconnected component of the cut, of length set by that component, and \(q\) equal rows for each component on the background \(J^a\otimes\mathbf 1_q\). Its use with the supplied states of the Row length paragraph, with rows set by the edge data \(s_f\), and for direct sums of distinct spheres is a transplant (conditional), referred to below as the transplanted selection rule. For a block that is the union of two disconnected components, such as the direct sum above or the two band-separated caps of one axis, whose charge spectrum is exactly the union of the two single-cap pairs, it suggests a two-row diagram of \(U(M_1+M_2)\) with rows fixed by the single-cap edge data; the block \(\Theta_1\otimes\Theta_2\) of the product of two spheres, treated in the toric-block paragraph below, has rank \(M_1M_2\) and a connected edge, so this reading does not apply to it. On the saddle class \(\ell_f=t\,s_f\) with fixed \(t\), the defect \(\Delta=\log\dim_{U(M_1+M_2)}(\ell_1,\ell_2)-\log\dim_{U(M_1)}(\ell_1)-\log\dim_{U(M_2)}(\ell_2)\), \(\ell_1\ge\ell_2\), is \(\sum_{c=1}^{\ell_1}\log\frac{M_1+M_2-1+c}{M_1-1+c}+\sum_{c=1}^{\ell_2}\log\frac{M_1+M_2-2+c}{M_2-1+c}-\log\frac{\ell_1+1}{\ell_1-\ell_2+1}\) (exact, by the hook-content formula; checked in rational arithmetic), the exact form of the excess in item~(ii) of the bearing paragraph (the approximate form holds at leading order for \(\ell_f\ll M_f\)). For the direct sum at \(M_1=M_2=N/2\), \(k_1=k_2=1\), \(t=1\) it grows linearly in \(N\): \(\Delta/N=0.521\) at \(N=3200\), against the limit \(\log\frac{27}{16}=0.5232\) and about \(0.75\) of the approximate form, and \(\sum_{(r,c)\in\mu}M/(M+c-r)=0.811\,|\mu|\) at block rank \(M=M_1+M_2\), so the dependence on the rank survives (numerical). The defect is not monotone in \(\ell_2\): \(\Delta(\ell_1,\ell_2+1)-\Delta(\ell_1,\ell_2)=\log\frac{37}{72}\) at \((M_1,M_2,\ell_1,\ell_2)=(2,24,13,12)\) (exact). Within the dominant-representation class (compact factor, positive contraction, leading semiclassical order with the leading-order entropy of~\cite{FlissFrenkelHartnollSoni2025} and one dominant diagram), with the diagram selected by the transplanted selection rule on the saddle class at fixed frame, the non-additivity of item~(ii) is therefore not an artefact of the fixed probe diagram.

\emph{Row perturbations, stacked rows and the residual bound.} For depths \(1\le q_f\le M_f\) let \(\Delta_{q_1,q_2}\) be the same difference for the diagram of \(U(M_1+M_2)\) with \(q_1\) rows \(\ell_1\) and \(q_2\) rows \(\ell_2\), \(\ell_1\ge\ell_2\ge0\), against \((\ell_1^{q_1})\) of \(U(M_1)\) and \((\ell_2^{q_2})\) of \(U(M_2)\). With \(M=M_1+M_2\), \(\exp\Delta_{q_1,q_2}\) is the product of the content factors \((M+c-r)/(M_1+c-r)\) on the first stack and \((M-q_1+c-r)/(M_2+c-r)\) on the second and of the hook ratios \((\ell_1-c+q_1-r+1)/(\ell_1-c+q_1+q_2-r+1)\) on the first \(\ell_2\) columns of the first stack (exact; checked in rational arithmetic, and equal to the two-row form at \(q_1=q_2=1\)), a function of the ranks and rows alone. With \(M_f=m_fN\), \(u_f=\ell_f/N\), \(G(m,u)=(m+u)\log(m+u)-m\log m-u\) and \(\Lambda=\sum_fq_f[G(m_1+m_2,u_f)-G(m_f,u_f)]\), which is positive and strictly increasing in each \(u_f\), the residual obeys \(|\Delta_{q_1,q_2}-N\Lambda|\le q_1q_2\log(\ell_1+q_1+q_2)+C\), with \(C\) depending only on \(m_f\), \(\ell_f/M\) and \(q_f\) (exact: each row sum is bracketed by its integral, the shift of the ranks by the row index is bounded by the mean-value theorem, and the hook ratios telescope); at equal row fractions \(u_1=u_2\), as at the symmetric saddle, the residual grows as \(q_1q_2\log N\), while at the unequal fractions tested it stays bounded in \(N\) (numerical). So \(\Delta_{q_1,q_2}/N\to\Lambda\), linear in the depths and additive over the stacks: at the symmetric saddle \(\Delta_{q,q}/N=0.5209\), \(1.0379\), \(1.5515\) at \(N=3200\), \(q=1,2,3\), against \(0.5232\,q\) (numerical). The minimum of \(\Delta\) over two-row diagrams with \(|\ell'_f-\ell_f|\le b\) is therefore of order \(N\) for every \(b=o(N)\), with a deficit from the saddle value that is linear in \(b\), of slope \(\sum_f\log\frac{m_1+m_2+u_f}{m_f+u_f}\) at leading order (numerical). Perturbations of order \(N\) remove it: at the symmetric saddle the minimum over \(|\ell'_f-\ell_f|\le cN\) is attained at the far diagonal corner, is positive up to \(c=0.4975\) and vanishes at \(c=\tfrac12\), where the box contains the trivial diagram (numerical, exhaustive at \(N=400\) for \(q_1=q_2\le3\)), whereas removing the second stack leaves \(\Delta_{q,0}/(qN)=0.189\) at \(N=1600\), \(m=(\tfrac12,\tfrac13)\), \(q\le3\) (numerical).

\emph{Frame average at the saddle.} For a summand deformed by \(A_f\), with \(B_f=A_f^{\mathsf T}A_f\), the cap of axis \(n\) has \(s_f^2(n)=\tfrac14M_f(N-M_f)(\operatorname{tr}B_f-n\cdot B_fn)\) (exact; the general-axis form of the edge-datum identity). With \(\rho_f(n)=\tfrac12(\operatorname{tr}B_f-n\cdot B_fn)\), the squared edge-length fraction relative to \(B_f=\mathbf 1\), the saddle rows are \(\ell_f(n)=\ell_f^{(0)}\rho_f(n)^{1/2}\), and \(\Lambda\) depends on the frame through a sum of one term for each summand, strictly increasing and strictly concave in \(\rho_f\). The bound of the preceding paragraph involves the frame only through the rows, which are at most \(\ell_f^{(0)}(\operatorname{tr}B_f/2)^{1/2}\), so the average of \(\Delta_{q_1,q_2}/N\) over the two axes, taken independently and uniformly on the sphere, converges to the sphere mean of \(\Lambda\), uniformly over the frames. When the sphere mean of the squared edge-length fraction equals its round-frame value, \(\operatorname{tr}B_f=3\), that mean is bounded above by the round-frame value, \(0.523248144\,q\) at \(m_f=\tfrac12\), \(\ell_f^{(0)}=N/2\), \(q_1=q_2=q\), with equality only for \(B_f\propto\mathbf 1\), and below by the value at the axis of the largest eigenvalue of \(B_f\), which is positive unless the transverse edge data of a summand degenerate. For \(B_f=\operatorname{diag}(\tfrac12(3-\gamma),\tfrac12(3-\gamma),\gamma)\), at these values and \(q=1\), the averaged limit is \(0.522655\), \(0.519217\), \(0.511350\) and the frame minimum \(0.479485\), \(0.396700\), \(0.268892\) at \(\gamma=1.4\), \(2\), \(2.6\); the finite-\(N\) residuals stay below \(7.7\) for two rows and \(59.8\) at depth three for \(N\le3200\), the stacked limits are the depth times the averaged profile, reproducing the isotropic values of the stacked-rows paragraph at the round frame, and the ratio of \(\mathrm d\log\dim/\mathrm d\log M\) to \(|\mu|\) at the saddle stays between \(0.7858\) and \(0.9023\) (numerical). A sampled frame scan checks the inequality: at \(N=3200\) with symmetric block ranks and saddle parameter one (\(\ell_f^{(0)}=1131\)), over \(150\) sampled frames with \(\operatorname{tr}B=3\) the worst residual is \(7.1\) for two rows and \(54.9\) at depth three, against values of the row-dependent form of the bound between \(8.6\) and \(9.0\) and between \(74.8\) and \(80.2\) (\(8.8\) and \(77.0\) at the round frame), with no violation at \(N=400\), \(1600\) and \(3200\) (numerical, sampled frame grids). This is an average over cap frames at fixed saddle parameter, not the frame average or the minimisation over frames of~\cite{FlissFrenkelHartnollSoni2025}.

\emph{Coincident copies and the multiplicity reading.} The direct sum of \(q\) equal summands, \(\widetilde X=\mathbf 1_q\otimes X\) with \(\widetilde\Theta=\mathbf 1_q\otimes\Theta\) for one cap, is, for undeformed summands, the background \(J^a\otimes\mathbf 1_q\) of the transplanted selection rule; the further conditional reading used here is that multiplicity \(q_f\) of a nonzero eigenvalue of the charge is read as \(q_f\) equal rows, at fixed depths. For copy-invariant momenta \(\mathbf 1_q\otimes\Pi\) the charge is \(\mathbf 1_q\otimes Q\) (exact), so every nonzero eigenvalue has multiplicity \(q\) and the stacked diagram of common depth \(q\) is read; for generic momenta on the same background the rank is the same but the eigenvalues are simple (numerical), so the multiplicity is a property of the state, not of the background alone. For \(q_f\) coincident copies of summand \(f\) of the direct sum, with momenta copy-invariant within each group and without entries between the groups, the charge is \(\bigoplus_f\mathbf 1_{q_f}\otimes Q_f\) (exact), so the stacked diagram \((\ell_1^{q_1},\ell_2^{q_2})\) is read. For the band-separated caps of the Row length paragraph, whose combined spectrum has multiplicity \(1\), no stacked diagram is selected: with saddle rows and depths \((q_1,q_2)\) the stacked moment signature exceeds the multiplicity-\(1\) signature by the fraction \(\sum_f(q_f-1)w_f^p/\sum_fw_f^p\), with \(w_f=k\,m_f(1-m_f)\) and \(k\) the edge-length coefficient of the factor, independent of \(N\) and \(t\): it is \(9/17\) at \(p=1\) and \(81/145\) at \(p=2\) for \((q_1,q_2)=(2,1)\), \((m_1,m_2)=(\tfrac12,\tfrac13)\), \(k=1\), and \(1\) at equal depths \(2\) (exact), a mismatch of leading order in \(N\). For one cap in each of \(q\) summands, or \(q\) coincident copies, the charge is \(-2\mathrm i(UR^\dagger-RU^\dagger)\), with \(U\) the matrix of the orthonormal edge vectors and \(R\) that of the edge rows; with \(C_0=U^\dagger R\), \(Z_0=R^\dagger R\), \(H=(C_0-C_0^\dagger)/(2\mathrm i)\) and \(K=Z_0-C_0^\dagger C_0=R^\dagger(\mathbf 1-UU^\dagger)R\succeq0\), its nonzero spectrum is that of \(-2\mathrm i\left(\begin{smallmatrix}C_0^\dagger&Z_0\\-\mathbf 1_q&-C_0\end{smallmatrix}\right)\), whose characteristic polynomial is \(\det(\lambda^2\mathbf 1_q+4\lambda H-4K)\), so \(\operatorname{Re}C_0\) never enters (exact). If \(H\) and \(K\) are block-scalar, \(h_f\mathbf 1_{q_f}\) and \(n_f\mathbf 1_{q_f}\) with \(n_f>0\), the polynomial is \(\prod_f(\lambda^2+4\lambda h_f-4n_f)^{q_f}\), and the spectrum is the union of \(q_f\) copies of the Row length pair \(-2h_f\pm2(h_f^2+n_f)^{1/2}\); every such datum is realised by \(R=U(A+\mathrm iH)+VK^{1/2}\), with \(A\) real and block-scalar and \(V\) an isometry onto vectors orthogonal to those of \(U\); for \(K=n\mathbf 1_q\) alone the pairs are those of the eigenvalues \(h_f\) of \(H\) (exact). For two diagonal pairs, as for block-diagonal momenta, the quartic \(\lambda^4+a\lambda^3+b\lambda^2+c\lambda+d\) is the square of a real quadratic if and only if \(h_1=h_2\) and \(n_1=n_2\), that is \(\operatorname{Im}\alpha_1=\operatorname{Im}\alpha_2\) and \(|w_{\perp,1}|=|w_{\perp,2}|\), since \(64d-(4b-a^2)^2=-256[(h_1-h_2)^4+2(h_1-h_2)^2(n_1+n_2)+(n_1-n_2)^2]\); a double root need not be a double pair, the pairs \((h,n)=(3,7)\) and \((5,11)\) giving \((\lambda-2)^2(\lambda+14)(\lambda+22)\) (exact). For \(K=n\mathbf 1_q\) a double eigenvalue occurs exactly when two \(h_f\) coincide, a set of real codimension three among Hermitian \(H\), and otherwise the \(2q\) eigenvalues are distinct, with gaps bounded below linearly in \(\min_{f\ne g}|h_f-h_g|\) (exact). At \(h_f=0\) the ratio of \(\sum_je_j^{2p}\) over the nonzero eigenvalues \(e_j\) to its multiplicity-\(1\) value is \(1+\sum_f(q_f-1)n_f^p/\sum_fn_f^p\), the stacked signature above with \(n_f\) in place of \(w_f\), with excess \(9/17\) at \(p=1\) and \(81/145\) at \(p=2\) for \((q_1,q_2)=(2,1)\), \((n_1,n_2)=(\tfrac14,\tfrac29)\) (exact), so in this class the excess is carried by the charge spectrum itself. Within independent Gaussian momenta exact multiplicity is not typical: none of \(6000\) draws at \(q=2\) and \(3\) has it, and along a generic perturbation of copy-invariant momenta the relative gap \(D_{\mathrm{gap}}=\max_{k=1,2}(e_{kq}-e_{(k-1)q+1})/\max_j|e_j|\) of the ordered nonzero eigenvalues grows linearly (numerical). At leading order in \(N\) it is approximately restored when the copies have equal scales: for independent standard complex Gaussian momenta at \(q=2\), with \(M=N/2\), the medians of \(D_{\mathrm{gap}}\) and of \(U_2=\operatorname{Tr}Q^4/\bigl(2q(\operatorname{Tr}Q^2/(2q))^2\bigr)-1\) fall from \(0.28\) and \(0.099\) at \(N=50\) to \(0.11\) and \(0.013\) at \(N=400\), as about \(N^{-1/2}\) and \(N^{-1}\), because the \(h_f\) stay of order one while the \(n_f\) grow as \(M\); with per-copy scales \((1,1.6)\) the median of \(D_{\mathrm{gap}}\) stays near \(0.4\) from \(N=120\) to \(480\) (numerical, sampled edge rows). This is consistent with the \(q\) equal rows of~\cite{Frenkel2023EdgeModes} for equal copies at leading order, and the scale mismatch shows that equal rows at leading order require equal norms of the edge rows.
```

### C2. Closing sentence

- Replace the whole unique line that starts with `These statements are for a compact factor with positive
  contraction, a single projector at fixed frame for the deformed sphere and the two caps,` (count 1).
- Replacement: `closing_r3.tex`, byte-identical to `closing_r2.tex` (1,072 B, sha256 a24fcb15...).

```latex
These statements are for a compact factor with positive contraction; for a single projector on the deformed sphere, for the two band-separated caps of one axis and for direct sums of deformed spheres with one cap in each summand, at fixed frame except for the stated average over cap frames at fixed saddle parameter; for the leading semiclassical order with one dominant representation, read through the transplanted selection rule at fixed depths; and for Gaussian states with the stated variances or the stated momentum data. Items~(i) and~(iii) of the bearing paragraph apply to every block treated; the frame average and the minimisation of~\cite{FlissFrenkelHartnollSoni2025} are used for its state and not re-derived, and the two-sided diagrams are not computed. They derive no entropy density on \(\partial M\), no value or scaling of \(S_{\mathrm{ent}}^{\mathrm{(IR)}}\), no boundary stationarity and no \(\Lambda_{\mathrm{eff}}\); Assumptions~\ref{ass:Sent-density} and~\ref{ass:bdy-EE} are not discharged, and Problem~G remains open and PROGRAMME-CONDITIONAL.
```

### C3. R6(a): Bearing (ii), separate anchored replacement, last

- **Line anchor:** the unique line that starts with `\emph{Bearing on Assumption~\ref{ass:Sent-density}.} (i) The
  block is a region of the factor`.
  - Its line-start count is 1, both in the live tree (L2926) and after C0-C2.
  - The shorter prefix `\emph{Bearing on Assumption~\ref{ass:Sent-density}.}` is *not* unique after C0. The 067
    insert has its own Bearing paragraph (its L24, "(i) For the cap times the whole second sphere ..."). The
    longer prefix is therefore used.
- **String anchor:** `up to a correction of the order of a logarithm (numerical)`. Its count is 1 in the live file
  and 0 in the 067 insert, the block and the closing.
- **Replacement**, inside that line only:

```latex
up to a correction of the order of \(\ell_1^2/M_1+\ell_2^2/M_2\) and of a logarithm (numerical)
```

- Everything else in the Bearing line is kept verbatim.

### C4. Bibliography

`bib_additions_r2.bib`, unchanged: `@misc{Frenkel2023EdgeModes}`, arXiv:2311.10131, verified in r2 and confirmed by
the gatekeeper against the PDF.

### Labels and style

- `\ref` targets: `ass:Sent-density` and `ass:bdy-EE` (unchanged; both verified to exist once in ch12).
- No new `\label`. No process language. No `$`.
- The snippets are CRLF UTF-8 without BOM.
- No status-label text is touched.

### Byte contract

| File | State | Bytes | sha256 | CRLF / bare LF |
|---|---|---|---|---|
| appH | PRE | 648,097 | fa3e318109a21b7df1562641d661179f5ba5ca03db97e6cc3e537e5eea000384 | 3428 / 0 |
| appH | POST, 067 then C1-C3 | 676,585 | 779bfcac09504722912302eb74299f4ba045dca64c65c166799b7bc3f70f723f | 3463 / 0 |
| appH | POST, C1-C3 without 067 | 663,309 | 01612a75f3aec5fe0d7ec3b660596cc399384d6b9d0d7c67b5653e1d2baf46b2 | 3436 / 0 |
| bib | PRE | 31,439 | b727e7d68635f832ade32d1272dd0a45e8f5794ca9ef0a4bcf16b92a4317dff3 | 1050 / 0 |
| bib | POST | 31,682 | a7aec454de0f6591c157ecb4709179f212c876b6f0df5df67713df85bb0493ed | 1059 / 0 |

Consistency with r2: 676,267 + 281 (block growth) + 37 (C3 growth) = 676,585.

Order of the passages in the applied file: Bearing (offset 618,721) < block (621,033) < 067 (637,182) < `\section{Problem
H` (650,458). The script asserts this order.

### Stale passages elsewhere

- None in chapters.
- The note for 081 r2 (drop "diagonal-cut convention") stands.

## Verification scripts

All are run from the repository root with `python -I`. Outputs are saved next to each script.

| Script | What it checks | Expected invariant |
|---|---|---|
| `d1_direct_sum_r3.py` | r2 checks (a)-(f), unchanged and byte-identical in output, plus (g): pencil against full charge; scale dependence of the union at (1,1), (1,1.6), (1,3), D = 50-1600 | (g) pencil deviation 2.113e-15; slopes −0.463, −0.989, −1.022; `PASS d1` |
| `d3_defect_frame_r3.py` | r2 checks (a)-(f), unchanged (the first 12 output lines are identical to `d3_defect_frame.out`), plus (g1) hook telescoping, 810 cases; (g2) residuals at one equal and three unequal fraction sets, q ≤ 3, N = 480-3840; (g3) content-part increments and the −Hk limit | (g1) 0 failures; equal increments 0.691-0.693, 2.755-2.768, 6.179-6.223; unequal last increments ≤ 0.031; content-part \|increments\| ≤ 0.0035; `PASS d3` |
| `apply_build_r3.py OUTDIR --build` | Applies, in order, C0 (if 067 is absent), C1, C2, C3 and the bib append in memory; asserts every anchor count and the passage order; builds a copy in OUTDIR/build | hashes as in the byte contract; `BUILD PASS pages=394`; 0 undefined/multiply-defined; 0 bibtex warnings for the new key |
| `gk_hc_r2.py`, `gk_approx_r2.py`, `gk_sign_r2.py` | The gatekeeper's scripts, re-run unchanged | output in `gk_r2_rerun_r3.out`: closed-form failures 0, stacked 0 of 504, 37/72, sign max dev 7.1e-15 |
| `d1_direct_sum.py`, `d2_pencil_typicality.py`, `d3_defect_frame.py` | The r2 scripts, re-run | outputs byte-identical to the saved r2 `.out` files |

**Reproduction pack:**

```
python -I proposals/local-gpu/072-080-r2/d1_direct_sum_r3.py
python -I proposals/local-gpu/072-080-r2/d3_defect_frame_r3.py
python -I proposals/local-gpu/072-080-r2/gk_hc_r2.py
python -I proposals/local-gpu/072-080-r2/gk_approx_r2.py
python -I proposals/local-gpu/072-080-r2/gk_sign_r2.py      # slow (several minutes)
python -I proposals/local-gpu/072-080-r2/apply_build_r3.py <dir outside repo> --build
```

- The applied-copy build of this round ran in the session scratchpad outside the repository. Its directory was
  deleted afterwards.
- `chapters/appH-microscopic-proofs.tex` and `bib/namcg.bib` had the same SHA-256 before and after: fa3e3181... and
  b727e7d6....
- Script SHA-256:
  - d1_direct_sum_r3.py: 489d9ef3...
  - d3_defect_frame_r3.py: 9a211337...
  - apply_build_r3.py: fc7ed7c7...

## Decisions Taken

1. **R2 wording: scoped to the equal-scale case only, as in the review.**
   - The unequal-scale O(D^{−1}) behaviour is derived and recorded here, but not added to the manuscript.
   - Adding it would be a new claim beyond the reviewed text. The equal-scale sentence already gives the largest
     deviation, so it is the conservative statement.
   - Rejected: adding a second clause on unequal scales.
2. **R6(a) anchor: the longer line-start prefix.**
   - The short Bearing prefix is duplicated by the 067 insert's own Bearing paragraph once C0 is applied.
   - Rejected: applying C3 before C0. That would also work, but it would change the integration order the
     orchestrator fixed.
3. **M1 consequence for E2 (r2 reasoning).** E2 is kept, scoped to the symmetric saddle. No manuscript text depends
   on it.
4. **d3(g) uses N divisible by 30, with Λ at the exact integer fractions.** This removes the rounding oscillation
   seen in gk_hc_r2 for m2 = 1/3. The gk script is left unchanged.

## Milestone assessment

Routine. These are corrections and a sharpening of numerical statements inside a bounded, conditional
compact-factor result. No critical-path step is derived.

## Status-label recommendation

- Critical path: A, B, C, D1, E, F, G-derived and N, all OPEN. Optional: H, I and J, all OPEN.
- Affected label: Problem G, unchanged (OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL).
- No label change is proposed.

## Author decision needed

None.

## Remaining open step

**G-derived (unchanged):**
- the entropy density of `ass:Sent-density` on ∂M of the emergent spacetime, derived from the matrix theory;
- boundary stationarity `ass:bdy-EE`;
- then Λ_eff.

**Bounded obstruction (non-additivity of log d_μ over disconnected components at leading order).** Its hypotheses
H1-H6 and the explored avenues are as in r2. Open avenues, in the order given by review-r2:
1. a spacetime-block subsystem of a non-compact or Lorentzian leaf (relax H1);
2. a split algebra with edge group U(M1) × U(M2) (relax H3);
3. a derivation of the rows-from-moments step (removes the transplant);
4. a within-core state, or OS reconstruction (relax H5);
5. the two-sided diagrams of FFHS;
6. depth-cancelling combinations.

**Item from this round.** The equal-fraction q1q2 log N term is a pure hook (column-collision) effect. It is absent
at u1 ≠ u2. Any depth-cancelling combination (avenue 6) must therefore treat equal and unequal rows separately.

## Special instructions for the gatekeeper

- **Full scan owed** under 3(c) and 3(d), in passes as the review disposes.
- **Re-check:**
  - the telescoping identity and the two asymptotic regimes of Hk (d3(g1)-(g3));
  - the equal against unequal scale orders (d1(g));
  - the R6 expansion against gk_approx_r2.
- **Anchors:**
  - C3 uses the long Bearing prefix, because the short one has count 2 after C0;
  - the string anchor of C3 has count 1 overall.
- **Do not let the text assert:**
  - an unequal-scale rate;
  - that the residual is bounded in general (only "at the unequal fractions tested");
  - anything about ∂M, Λ_eff, or the FFHS-minimised entropy.
