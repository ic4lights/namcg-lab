# Proposal 081-088-r2 (Problem G moments block, gpu 081-088), round 3

## Result

This round answers review-r2 (verdict AWRR, 1 BLOCKING, 1 MAJOR PRIOR-CLAIM-ERROR, 2 minors with action). The
mathematical content of the two paragraphs is unchanged from r2. Three things change.

1. **The numbers are corrected.** The r2 slot-profile numbers came from `v3_row_length_profile.py`. That script
   builds T_lm by repeated commutators in floating point, and at N=400 the tensors are not orthogonal: the new
   script reproduces |<T_{40,3},T_{38,3}>| = 0.973. So its outputs were wrong.
   - The replacement `v3_row_length_profile_r3.py` diagonalises the Casimir superoperator on each fixed-offset
     subspace (symmetric tridiagonal, `scipy.linalg.eigh_tridiagonal`).
   - It cross-checks against exact Clebsch-Gordan coefficients and a dense superoperator at N=12.
   - It asserts the full-row sum N^-1 Σ(2l+1)f(l) at N=400.
   - It reproduces every entry of the gatekeeper's table exactly. The corrected value is D_eff = 37.96 (text:
     38.0) at N=400, M=N/2, l_c=40, f=νl/2.
2. **Snippets (a)-(c) of review-r2 are applied verbatim** to the inserted paragraph.
3. **Snippet (d) is applied verbatim** as a third anchored replacement (S3) in the integrated Row length
   paragraph. It repairs the PRIOR-CLAIM-ERROR there: the paragraph's 1.021, 1.041 and 1.07 are 4s²(W−g_u)
   ratios, not 4s²·(full block-row sum) ratios.
   - I re-checked the other two numbers of that paragraph against the redefined W, i.e. the local exponents
     3.93 and 2.98. They match W−g_u under symmetric differences (3.934-3.936 and 2.980-2.981), not the full
     block sum (3.914 and 2.956). So no further edit is needed.

The qualitative conclusion of r2 stands: D_eff ≤ l_c−1, ρ_2−1 ≥ 1/(l_c−1), and beyond the second moment the
match holds only as l_c → ∞. The corrected D_eff = 37.96 lies close to the bound l_c−1 = 39; the wrong 29.5 did
not. Nothing here advances G-derived. Problem G stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## Target and status

Unchanged from r2, re-read in the current tree (appH sha256 `779bfcac…`, live):
- **Problem G** (appH `\section{Problem G: HBEV}`): Status OPEN, Priority CRITICAL PATH, Completion
  PROGRAMME-CONDITIONAL. G-model and G-external are reduced-scope only.
- **ch17 completion item, Problem G-derived:** the infrared boundary entropy density and the stationarity
  relation are derived from the matrix theory, and Λ_eff follows from them.
- **Dependencies:** `ass:Sent-density`, `ass:bdy-EE`, the leading-order entropy of
  FlissFrenkelHartnollSoni2025, the transplanted selection rule, and the supplied state of the State and
  coarse-graining paragraph.

This package is PROGRAMME-CONDITIONAL (model-internal). The discrepancy flagged in r2, the absent "Missing step
paragraph", stands; the reference stays dropped.

## Source reading

Digest + targeted reads. `make_digest.py --check`: DIGEST CURRENT (`dirty-chapters: yes`, because the working
tree carries uncommitted integrated changes). No full scan is claimed. Review-r2 records the full scan as pending
(3(c)), to be done by the gatekeeper in passes. S3 edits a sentence of an integrated paragraph, so 3(c) applies
again.

Read in full:
- review-r2.md;
- proposal-r2.md, insert_r2.tex, closing_r2.tex, clause_r2.txt, apply_build_r2.py/.out and
  v3_row_length_profile.py/.out;
- appH Problem G, L2918-2926: the Row length, State and coarse-graining and Bearing paragraphs, including the
  whole L2922 line.

The pre-hash was re-confirmed as live: 779bfcac09504722912302eb74299f4ba045dca64c65c166799b7bc3f70f723f.

## Research and reasoning

### R1. Stable construction of the T_lm (finding 1)

Notation:
- Basis |k), k = 0..N−1, with J³|k) = (j−k)|k), j = (N−1)/2.
- (J₊)_{k−1,k} = c_k = [j(j+1) − (j−k)(j−k+1)]^{1/2}, with c_0 = c_N = 0.
- E_{a,b} is a matrix unit with b = a+m. These units span the offset-m subspace, which holds the operators that
  raise J³ by m.

Then:
- J₊E_{ab}J₋ = c_a c_b E_{a−1,b−1} and J₋E_{ab}J₊ = c_{a+1}c_{b+1}E_{a+1,b+1}.
- J₊J₋ = diag(c_{a+1}²) and J₋J₊ = diag(c_a²).
- Therefore C(X) = Σ_a[J_a,[J_a,X]] = ½([J₊,[J₋,X]] + [J₋,[J₊,X]]) + [J³,[J³,X]] maps offset m to itself.

On that subspace C is the real symmetric tridiagonal matrix

  diag_a = ½(c_a² + c_{a+1}² + c_b² + c_{b+1}²) + m²,   offdiag_{a,a+1} = −c_{a+1}c_{b+1},

with simple eigenvalues l(l+1), l = m..N−1. Its Frobenius-orthonormal eigenvectors are the trace-normalised T_{l,m}
up to a phase.

The variances do not depend on that phase:
- Each entry (v,j) lies on exactly one offset. With π_{l,−m} = (−1)^m π̄_{lm} and E|π_lm|² = f(l), this gives
  E|Π_vj|² = Σ_l f(l)|T_{l,m}(v,j)|², with m the offset of (v,j).
- Summing over j and using Σ_m T_lm T_lm† = (2l+1)/N reproduces the full row sum N^-1 Σ(2l+1)f(l) (asserted
  numerically at N=400 to 1e-10 relative).

Checks in `v3_row_length_profile_r3.py`:
- **A.** At N=400, offsets m = 0, 1, 3, 17, 40: the eigenvalues equal l(l+1) to relative error 5e-12, and
  orthonormality holds to 7e-15.
- **B.** At N=12:
  - |T_lm(m1,m2)|² = (2l+1)/N·|⟨j m2; l m | j m1⟩|², checked against exact sympy CG, deviation 2e-16. This
    normalisation follows from Σ_{m1,m2}|CG|² = (2j+1)/(2l+1).
  - A dense diagonalisation of the full N²×N² superoperator gives the spectrum l(l+1) with multiplicity 2l+1
    (deviation 3e-13).
- **F.** The old repeated-commutator construction gives |⟨T_{40,3},T_{38,3}⟩| = 0.973 at N=400, which confirms
  the gatekeeper's diagnosis.

### R2. Corrected table (N=400, M=200; block k<M, v=|M), u=|M−1))

W_block is the full block-row sum, including u. "Slots" counts the slots of r with g > 0.

| l_c | f | full-row sum (= N^-1Σ(2l+1)f) | W_block | g_u/W_block | W−g_u | D_eff(r) | slots | ratio |
|---|---|---|---|---|---|---|---|---|
| 20 | l/2 | 7.4375 | 3.6315 | 0.0441 | 3.4714 | 18.68 | 19 | 6N(W−g_u)/l_c³ = 1.0414 |
| 40 | l/2 | 56.375 | 27.8560 | 0.0230 | 27.2166 | 37.96 | 39 | 6N(W−g_u)/l_c³ = 1.0206 |
| 20 | l(l+1)/4 | 60.6375 | 29.6642 | 0.0385 | 28.5224 | 18.70 | 19 | |
| 40 | l(l+1)/4 | 882.525 | 436.5711 | 0.0202 | 427.7367 | 38.07 | 39 | 16N(W−g_u)/l_c⁴ = 1.0693 |

For comparison, the ratios built from W_block are 1.0894 (l_c=20), 1.0446 (l_c=40) and 16N·W_block/l_c⁴ = 1.0914.
They do not match the integrated 1.041, 1.021 and 1.07. This confirms the gatekeeper's finding 2, that the
integrated numbers are W−g_u ratios.

Local exponents at l_c=40 (scratch computation, recorded here; the Row length text gives no definition):

| f | W−g_u, central (39,41) / (38,42) / (36,44) | W_block, same stencils |
|---|---|---|
| l/2 | 2.981 / 2.980 / 2.980 | 2.956 / 2.957 / 2.957 |
| l(l+1)/4 | 3.936 / 3.934 / 3.934 | 3.913 / 3.915 / 3.914 |

One-sided differences oscillate with the parity of l_c at fixed M. For example, (39,40) gives 3.004 and (40,41)
gives 2.957 for W−g_u at f=l/2. The integrated 2.98 and 3.93 therefore agree, at the stated precision, with
W−g_u under symmetric stencils. After (d) they are consistent with the redefined W, so no edit is proposed. The
gatekeeper may still want a stencil statement; see the special instructions.

All gatekeeper values are reproduced to the printed digits; `v3` E asserts nine of them. Nothing differs.

### R3. Snippets (a)-(c) (findings 1, 3, 4)

- **(a)** D_eff 29.5 → 38.0. R2 gives 37.96, which is ≤ l_c−1 = 39, as the exact bound requires.
- **(b)** "the entries carry distinct nonzero charges of one sign". Under U_θ = e^{iθn·J}, Π_{vj} picks up the
  phase e^{iθ(m_v−m_j)}, and m_v − m_j = j − M < 0 for every block index j < M.
  - Invariance kills E w_jw_k^* for j ≠ k, because the charges are distinct.
  - It kills E w_jw_k for all j, k, including j = k, because the total charge (j−M)+(k−M) is nonzero. That
    needs the charges to be of one sign and nonzero.
  - So r2's "distinct" alone was insufficient for the pseudo-covariance. The finding is correct.
- **(c)** "at a=0 exactly at the second moment". The moment identity 2(4s²W)^pρ_p is stated at a=0, and for a≠0
  the second moment carries the extra 16⟨a²⟩ = 8s²g_u. The qualifier is correct.

### R4. Snippet (d) (finding 2)

ℓ = 2|w_⊥| and r = |w_⊥|² = Σ_{j≠u}|w_j|². This uses step 5 of r2: u = |M−1) is a basis vector, so
w_⊥ = (w_j)_{j≠u}. Hence ⟨ℓ²⟩ = 4s²Σ_{j≠u}g_j = 4s²(W_block − g_u), which is exact and holds without neglecting
Im α.

Separately, a = Im α with α = w_u circular and E|α|² = s²g_u, so E a² = s²g_u/2. Then
½⟨Tr Q²⟩ = ½(16⟨a²⟩ + 8⟨r⟩) = 4s²(g_u + Σ_{j≠u}g_j) = 4s²W_block (exact). Snippet (d) states exactly these two
facts.

The anchor `with \(W\) the sum over the boundary row inside the block.` occurs once in the live appH, once in the
`\emph{Row length.} If ` line, and in neither insert_r3.tex nor its replacement. All of this is asserted in
apply_build_r3.py. The insert's own phrase "the full sum over the boundary row inside the block" does not contain
the anchor.

### Avenues

Unchanged from r2 and review-r2's disposition, ranked:
1. a core-produced state, i.e. a within-core state such as OS reconstruction of the matrix weight;
2. typical rather than averaged moments, or the l_c → ∞ limit of the rows-from-moments reading;
3. the non-compact/Lorentzian spacetime-block and split-algebra (U(M1)×U(M2)) routes;
4. two-sided diagrams.

The corrected D_eff ≈ l_c−1 sharpens avenue 2. At fixed l_c the excess ρ_2−1 = 1/D_eff ≈ 1/(l_c−1) is
essentially saturated, so the only within-state route to the averaged-moment reading is l_c → ∞.

## Claim classification

| claim | class |
|---|---|
| tridiagonal form of the Casimir on offset m, simple spectrum l(l+1) | established (exact) |
| E\|Π_vj\|² = Σ_l f(l)\|T_lm(v,j)\|², full row sum N^-1Σ(2l+1)f | established (exact) |
| D_eff = 37.96 (l_c=40), 18.68 (l_c=20), f=l/2; 38.07 (f=l(l+1)/4); g_u/W 0.0230 / 0.0441 | numerical |
| ⟨ℓ²⟩ = 4s²(W_block−g_u), ½⟨TrQ²⟩ = 4s²W_block | established (exact, given the supplied state) |
| integrated 1.021, 1.041, 1.07, 2.98, 3.93 consistent with W = W_block−g_u | numerical (exponents: under symmetric stencils) |
| (b) charge argument for covariance and pseudo-covariance | established |
| everything else in the two paragraphs | as classified in r2, unchanged |
| bearing on `ass:Sent-density` / G-derived | unresolved, unchanged |

## Proposed changes

File `chapters/appH-microscopic-proofs.tex` only. There are three edits. No `\ref`, `\label` or bib change.

**S1: insertion (r2 S1, with (a)-(c) applied).** Insert `insert_r3.tex` (two paragraphs, each followed by one
blank CRLF line) immediately before the unique line starting `\emph{Vacuum term.} The abstract
of~\cite{Steinacker2023}`, which directly follows `\emph{Coincident copies and the multiplicity reading.}` and a
blank line. Its text is:

```latex
\emph{Moments of the edge charge in the Gaussian rank-one class.} With \(a=\operatorname{Im}\alpha\) and \(r=|w_\perp|^{2}\) as in the Row length paragraph, the nonzero eigenvalues of the charge of a single cap are the roots of \(\lambda^{2}+4a\lambda-4r=0\), so that, pointwise, \(\operatorname{Tr}Q^{m}=(-1)^{m}2^{m+1}\sum_{k\le m/2}\binom{m}{2k}\sum_{j=0}^{k}\binom{k}{j}a^{m-2k+2j}r^{k-j}\) for every \(m\ge1\); for the two band-separated caps of one axis, and for the direct sum of the two-component paragraph with momenta without entries between the summands, the moment sequences add (exact). Reversing the sign of the momenta sends \(Q\) to \(-Q\), so the odd moments average to zero in every state invariant under that reversal, and at \(a=0\) the even moments are \(2\ell^{2p}\), with \(\ell=2r^{1/2}\) the row length. If \(r=s^{2}\sum_{i}g_{i}E_{i}\) with independent unit exponentials \(E_{i}\), a profile \(g=(g_{1},\dots,g_{D})\) of \(D\) slots and \(W=\sum_{i}g_{i}\), then \(\langle\ell^{2}\rangle=4s^{2}W\) and, at \(a=0\), the averaged \(2p\)-th moment is its single-row value \(2(4s^{2}W)^{p}\) times \(\rho_{p}(g)=p!\,h_{p}(g)/W^{p}=\sum_{\lambda\vdash p}(p!/z_{\lambda})\prod_{k\ge1}(s_{k}/W^{k})^{m_{k}}\), with \(h_{p}\) the complete homogeneous symmetric polynomial, \(s_{k}=\sum_{i}g_{i}^{k}\) and \(m_{k}\) the multiplicity of the part \(k\) in \(\lambda\); hence \(\rho_{2}-1=1/D_{\mathrm{eff}}\) with \(D_{\mathrm{eff}}=W^{2}/s_{2}\), \(\rho_{p}-1\ge\binom{p}{2}/D_{\mathrm{eff}}\), \(\rho_{p}\le p!\) with equality for \(p\ge2\) only when one slot carries all the weight, and \(\rho_{p}\ge\prod_{k=1}^{p-1}(1+k/D)\) with equality for \(p\ge2\) only at the uniform profile (exact). In the Gaussian state of the Row length paragraph, as in every Gaussian state of the momenta invariant under conjugation by \(e^{\mathrm i\theta\,n\cdot J}\), the entries of the boundary row \(w\) in the eigenbasis of \(n\cdot J\) are independent circular complex Gaussians, since the entries carry distinct nonzero charges of one sign under that rotation; so \(a\) is independent of \(r\), \(r\) has the form above with \(s^{2}g_{i}\) the variances of the entries other than the one at \(u\), and \(\langle\operatorname{Tr}Q^{2}\rangle\) is \(8s^{2}\) times the full sum over the boundary row inside the block (exact). These variances vanish for entries more than \(l_c\) places from \(v\) in that eigenbasis, so at most \(l_c-1\) slots carry \(r\) and \(\rho_{2}-1\ge1/(l_c-1)\) for every \(N\) and \(M\) (exact); \(D_{\mathrm{eff}}=38.0\) at \(N=400\), \(M=N/2\), \(l_c=40\) and \(f=\nu l/2\) (numerical). The reading of the rows from the edge data in the transplanted selection rule therefore matches the averaged charge moments at \(a=0\) exactly at the second moment, and beyond it only as \(D_{\mathrm{eff}}\to\infty\), which in this state requires \(l_c\to\infty\).

\emph{Coupled slots and laws of the edge vector.} For a Gaussian state without that invariance, write the boundary row in a basis of \(D\) slots in which \(\mathbb{E}\,w_{i}w_{j}^{*}=s^{2}g_{i}\delta_{ij}\), assume the slots circular, and set \(q_{i}=|u_{i}|^{2}\), \(W=\sum_{i}g_{i}\), \(\mu=\sum_{i}q_{i}g_{i}\) and \(\Gamma=\sum_{i}q_{i}(g_{i}-\mu)^{2}\). Then \(\mathbb{E}\,a^{2}=s^{2}\mu/2\), \(\mathbb{E}\,ar=0\), \(\mathbb{E}\,a^{2}r-\mathbb{E}\,a^{2}\,\mathbb{E}\,r=s^{4}\Gamma/2\) and \(|(\mathbf 1-uu^{\dagger})Gu|^{2}=\Gamma\), with \(G=\operatorname{diag}(g)\), so \(a\) and \(r\) are independent if and only if \(\Gamma=0\), that is, if and only if \(g\) is constant on the support of \(u\), which holds in the preceding paragraph, where \(u\) is one slot; \(\langle\operatorname{Tr}Q^{2}\rangle=8s^{2}W\) for every \(u\), and \(\langle\operatorname{Tr}Q^{4}\rangle\) exceeds its value for independent \(a\) and \(r\) with the same marginals by \(128s^{4}\Gamma\) (exact). For a law \(\pi\) of \(u\) independent of \(g\), \(\mathbb{E}_{\pi}\Gamma=g^{T}\Sigma_{\pi}g\) with \(\Sigma_{\pi}=\mathbb{E}_{\pi}(\operatorname{diag}(q)-qq^{T})\) positive semidefinite and annihilating the constant profiles. On the hyperplane \(\sum_{i}g_{i}=W\) the zero set, the minimiser set and the stationary set of \(\mathbb{E}_{\pi}\Gamma\) are the profiles constant on the components of the graph in which \(i\) and \(j\) are joined when \(\pi(q_{i}q_{j}>0)>0\); this is the uniform profile alone exactly when the graph is connected, as for the Haar law, for which \(\Sigma_{\pi}\) is \(1/(D+1)\) times the orthogonal projector onto the profiles of mean zero; and \(\mathbb{E}_{\pi}\Gamma\ge\lambda^{+}W^{2}(D_{\mathrm{eff}}^{-1}-D^{-1})\), with \(D_{\mathrm{eff}}=W^{2}/\sum_{i}g_{i}^{2}\) and \(\lambda^{+}\) the least eigenvalue of \(\Sigma_{\pi}\) on profiles of mean zero (exact). The stationary set is unchanged under reparametrisations with nowhere-vanishing derivative and becomes that of the union of the graphs under positive combinations of laws, so no functional built in this way from averaged decoupling data selects a value of the profile within a component; a profile is fixed only by the state, which the State and coarse-graining paragraph leaves as a supplied input. These two paragraphs fix no state, \(s\), \(g\) or edge vector.
```

Relative to insert_r2.tex, the exact replacements are:
- (a) `\(D_{\mathrm{eff}}=29.5\) at …` → `\(D_{\mathrm{eff}}=38.0\) at \(N=400\), \(M=N/2\), \(l_c=40\) and
  \(f=\nu l/2\) (numerical)`;
- (b) `since distinct entries carry distinct charges under that rotation;` → `since the entries carry distinct
  nonzero charges of one sign under that rotation;`;
- (c) `…matches the averaged charge moments exactly at the second moment,` → `…matches the averaged charge
  moments at \(a=0\) exactly at the second moment,`.

`make_snippets_r3.py` applies them to insert_r2.tex with count-1 assertions.

**S2: closing clause (unchanged from r2).** In the unique line starting `These statements are for a compact factor
with positive contraction; for a single projector`, replace
`and for Gaussian states with the stated variances or the stated momentum data.` with
`and for Gaussian states with the stated variances, the stated momentum data or the stated slot laws, with the
stated laws of the edge vector.`

The resulting line is `closing_r2.tex`, which is unchanged, so no closing_r3.tex is written. The status sentence
appears once, in that line.

**S3: Row length paragraph (snippet (d), new).** In the unique line starting `\emph{Row length.} If ` (L2922),
replace the unique text

```latex
with \(W\) the sum over the boundary row inside the block.
```

with

```latex
with \(W\) the sum over the boundary row inside the block without its entry at \(u\), while \(\tfrac12\langle\operatorname{Tr}Q^{2}\rangle\) is \(4s^{2}\) times the full sum (exact).
```

Everything else in the line is kept verbatim, including "with \(\operatorname{Im}\alpha\) neglected", 1.021,
1.041, 3.93, 1.07 and 2.98 (see R2). Old and new are stored in `rowlen_r3.txt`.

**Stale passages elsewhere:** none. `29.5` does not occur in the applied file. The proposal record is corrected
below and in R2.

**Byte contract:**

| item | value |
|---|---|
| pre appH sha256 | `779bfcac09504722912302eb74299f4ba045dca64c65c166799b7bc3f70f723f` (676585 B, CRLF 3463, bare LF 0), live |
| insert_r3.tex | `8dfc3ac0e98f6505fa21220a546a66ce284a43cd918fd05deb5b5d14db9200b6` (5236 B, CRLF) |
| closing_r2.tex | `44f1695d0b403fbc513439d0c55aab2fee4dd345d3c2b2c66772ba73b706ea08` (unchanged) |
| clause_r2.txt | `06b5de4cb36316a02b0343fa39e1e6679643c6d6f97b97c9ad5a9722e33a4e7a` (unchanged) |
| rowlen_r3.txt | `24d15670950d6ae7ac478000afdb6fa21aa01a0db87de732c29d4a02120a6428` |
| post appH sha256 | `b71bb0ac1034f9bc9ce68c72e0c015009c6e5b7cfddada29b8fe1dc185ec6be9` (682008 B, CRLF 3467, bare LF 0) |

The script asserts that the post file, with the insert removed and the S2 and S3 replacements reverted, is
byte-identical to the pre file.

### Corrections to the proposal record (r2 → r3)

| r2 statement | r3 |
|---|---|
| Result: "D_eff = 29.5 at N=400, M=N/2, l_c=40, f=νl/2" | 37.96 (text 38.0) |
| step 5: "D_eff = 15.57 (l_c=20), 29.52 (l_c=40) for f=l/2, 29.01 for f=l(l+1)/4" | 18.68, 37.96, 38.07 |
| claim table: "D_eff = 29.5 …" | 37.96 / 38.0 |
| verification table: "`D_eff(r) = 29.52` … (15.57 …; 29.01 …)" | superseded by v3-r3 (37.96; 18.68; 38.07) |
| special instructions: "g_u/W = 0.0085 at l_c=20 and 0.042 at l_c=40" | 0.0441 at l_c=20 and 0.0230 at l_c=40 |
| v3 output W_block 64.72 / 413.29 / 6412.25 (above the full-row sums 7.44 / 56.38 / 882.5) | 3.6315 / 27.856 / 436.571 |
| step 5 (b): pseudo-covariance from "exponent ≠ 0 when j, k in block" | correct; now worded as nonzero charges of one sign (b) |
| v3 "D proxy 1488 / 23017" | correct arithmetic on the dropped proxy; no longer computed or cited |

v1 and v2 numbers are unaffected: they do not use T_lm.

## Verification scripts

All are in `proposals/local-gpu/081-088-r2/`; run from the repository root.

| script | checks | expected invariant output |
|---|---|---|
| `v1_moment_map.py` (r2) | moment map, ρ_p | `PASS v1` |
| `v2_coupling_locus.py` (r2) | coupled slots, frame-law locus | `PASS v2` |
| `v3_row_length_profile_r3.py` (new) | R1, R2 | A dev < 1e-10; B CG dev ~2e-16, dense dev ~3e-13; full-row sums 7.4375 / 56.375 / 60.6375 / 882.525 at rel < 1e-10; `D_eff(r) 37.96` (l_c=40, f=l/2), 18.68, 38.07; `6N(W-g_u)/lc^3 = 1.0206` / `1.0414`; `16N(W-g_u)/lc^4 = 1.0693`; `E gatekeeper table reproduced: [True]*9`; F overlap 0.973; `PASS v3-r3` |
| `make_snippets_r3.py` | writes insert_r3.tex, rowlen_r3.txt | the hashes above |
| `apply_build_r3.py OUTDIR --build [--keep]` | S1-S3 anchors count 1; S1 adjacency; byte contract; no `29.5` in the insert; no `diagonal-cut` or "Missing step paragraph"; status-sentence count unchanged; out-of-repo build; removes OUTDIR/build unless `--keep` | `POST … b71bb0ac…`, `BUILD PASS pages=394`, `undefined/multiply-defined warnings: 0`, `build directory removed: True` (see apply_build_r3.out) |

Reproduction pack:

```
python -I proposals/local-gpu/081-088-r2/v3_row_length_profile_r3.py   # ... D_eff(r) 37.96 ... PASS v3-r3
python -I proposals/local-gpu/081-088-r2/make_snippets_r3.py           # insert_r3.tex 5236 B sha256 8dfc3ac0...
python -I proposals/local-gpu/081-088-r2/apply_build_r3.py <dir outside repo> --build   # post b71bb0ac..., BUILD PASS pages=394
```

The applied copy (`appH-microscopic-proofs.tex`) was written to the session scratchpad, outside the repository.
The script removed its build directory. The r2 files are kept unchanged. `v3_row_length_profile.py` is superseded
and must not be cited.

## Decisions Taken

- **D6: stable construction.** I chose the Casimir superoperator restricted to each offset (tridiagonal) as the
  production method, with exact CG as the small-N cross-check.
  - Rejected: CG at N=400 through sympy, which is too slow and adds nothing beyond the N=12 check.
  - Rejected: re-orthogonalised commutators, which are ad hoc.
- **D7: (d) as a separate anchored replacement S3 in this package**, per review-r2. It shares the derivation of
  step 5. No closing_r3.tex is written, since S2 is unchanged.
- **D8: no edit to the integrated exponents 3.93 / 2.98.** They agree with the redefined W under symmetric
  stencils (R2). I add no stencil definition, which keeps the change minimal.
- **D9: "with Im α neglected" is kept** in the Row length line. After (d), ⟨ℓ²⟩ = 4s²W holds exactly without it,
  so the qualifier is redundant but not false. Removing it would go beyond the verbatim (d).

## Milestone assessment

Routine. This round corrects numbers and an integrated prior-claim error inside a model. It derives no
critical-path step.

## Status-label recommendation

The critical-path set at the full-GR / matrix-derived scope (ch17) is A, B, C, D1, E, F, G-derived and N, all
OPEN. Only G is touched, and it stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL. No label change.

## Author decision needed

None.

## Remaining open step

As in r2. G-derived needs:
- a matrix-derived IR entropy density on ∂M, with the block-to-∂M identification derived;
- the stationarity of `ass:bdy-EE`;
- the Λ_eff scaling;
- for this sub-line, a state produced by the core, since the profile, l_c and the moment-row reading are fixed
  only by the state;
- resolution of the rank-dependence obstruction (Bearing (ii)).

## Special instructions for the gatekeeper

- **Findings addressed.** OPEN count against review-r2: 0/4 actionable findings open.
  - 1 BLOCKING: v3-r3, (a) and the record corrections.
  - 2 MAJOR: (d), applied as S3.
  - 3: (b).
  - 4: (c).
  - 5: no action, as directed.
  - 6 (procedural): the full scan is still pending, for the gatekeeper.
- **Re-run** v3-r3 and apply_build_r3. Confirm post sha `b71bb0ac…`, 394 pp, 0 undefined.
- **Wording check on (d), applied verbatim.** "the full sum" means the block-row sum including u, by contrast
  with the preceding "without its entry at u". The same paragraph earlier uses "every full row sum" for the sum
  over all N entries of a row (N^-1Σ(2l+1)f). A reader could conflate the two. If you judge this ambiguous,
  "the full sum over the boundary row inside the block" would be unambiguous; I did not deviate from the
  verbatim snippet.
- **Not re-derived here.** The normalisation of the integrated ratio "⟨ℓ²⟩ / (ν³l_c³M(N−M)/3N)" was checked only
  at ν = 1 with σ₁ = σ₂ = 1, i.e. s² = M(N−M)/2, where it equals 6N(W−g_u)/l_c³. Its ν-dependence (W ∝ ν against
  the ν³ in the denominator) was not re-derived in this round.
- **Must not be asserted:** the r2 list stands (no rows-from-moments derivation; no leading-order averaged-moment
  claim; the frame-law no-go stays scoped to Gaussian slot laws and profile-independent edge-vector laws).
