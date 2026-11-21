# Proposal 081-088-r2 (Problem G moments block, gpu 081-088), round 2

## Result

This round replaces the seven gpu 081-088 paragraphs, with 086's correction riding along, by two paragraphs,
as the group6-G2 major finding M1 asks. Every kept claim was re-derived and re-checked in fresh scripts
(`v1`-`v3`). The text is anchored to the current tree, which has the integrated direct-sum edge block of
072-080 r3 and local 067. Nothing here advances G-derived.

Re-derivation forced one material correction to the group6 text, which had inherited it from 081, 085 and 087.
The "fuzzy variance proxies" (g = νl/2 with multiplicity 2l+1, D = l_c(l_c+2), D_eff = 1488 at l_c = 40) are
not the slot law of the Gaussian state of the Row length paragraph. The proxy counts modes, but the slots of r
are the matrix entries of the boundary row. In that state:
- the law is invariant under conjugation by e^{iθ n·J};
- so the boundary-row entries in the n·J eigenbasis are independent and circular;
- so the edge vector u is one slot, a = Im α is independent of r, and the induced coupling Γ is identically 0;
- the spin-l matrices are banded at offset m with |m| ≤ l ≤ l_c, so at most l_c−1 slots carry r.

Hence D_eff ≤ l_c−1 and ρ_2−1 ≥ 1/(l_c−1) for every N and M (exact). Numerically D_eff = 29.5 at N=400, M=N/2,
l_c=40, f=νl/2, against the proxy's 1488. The identification of moments with edge data is exact at the second
moment. Beyond it, it is recovered only as l_c → ∞ in that state, not "as the cutoff grows through
D_eff ≈ l_c²".

The proxy numbers, the 8/9 limit and the W²/(8D²) Haar rate are therefore dropped, not refined. The coupled-slot
and frame-law content (the bounded no-go of 087/088: no frame-averaged decoupling functional selects a profile
value within a component) is kept in the second paragraph. It is explicitly scoped to Gaussian states without
the axial invariance.

Problem G stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## Target and status

- Problem G, appH `\section{Problem G: HBEV}` (L2886), ledger label verbatim: "Status: OPEN. Priority: CRITICAL
  PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope results: G-model and G-external support at most a
  scope-limited model; G remains OPEN and neither satisfies the matrix-derived criterion."
- ch17 L663-665, order of work: "Problem~G: derive \(S_{\mathrm{ent}}^{\mathrm{(IR)}}\) and boundary
  stationarity from the matrix theory, then derive the \(\Lambda_{\mathrm{eff}}\) scaling or value."
- ch17 L723-726, completion item: "Problem~G-derived: the infrared boundary entropy density and stationarity
  relation are derived from the matrix theory, and the \(\Lambda_{\mathrm{eff}}\) scaling or value follows from
  them. G-model and G-external do not meet this item."
- Dependencies, as recorded in the current tree: Assumptions `ass:Sent-density` and `ass:bdy-EE` (ch12 L139,
  L185); the leading-order entropy of FlissFrenkelHartnollSoni2025; the transplanted selection rule (appH L2928);
  the supplied state (State and coarse-graining paragraph, L2924).
- Classification of this package: PROGRAMME-CONDITIONAL (model-internal). It derives no G-derived item.
- Discrepancy flagged: the group6 text and all seven gpu paragraphs cite "the missing steps (i)-(iv) of the
  Missing step paragraph". The current Problem G section has no Missing step paragraph. The gpu import's
  `\paragraph{Missing step.}`, "Bounded obstruction" and "Free benchmark" paragraphs (backup L3043-3130) are not
  in the tree. The reference is therefore dropped. The closing scope sentence (L2938) already states what stays
  underived. I do not propose to restore those paragraphs; that belongs to a separate package.

## Source reading

Digest + targeted reads. `make_digest.py --check`: DIGEST CURRENT. No full scan is claimed. The package changes
no definition, assumption, scope statement or status label. It extends one clause of a scope sentence, so the
gatekeeper may judge that 3(c) applies.

Read in full:
- appH L2886-2967, the whole current Problem G section, including 067 to `\section{Problem H}`;
- ch17 L640-760;
- group6-G2.md;
- 072-080-r2 review-r2.md (E1) and apply_build_r3.py with its .out;
- gpu backup L3022-3195, the seven 081-088 paragraphs verbatim;
- 086 proposal-r1;
- 081 s3_r2 header.

I also re-ran 19 inherited scripts of 081-088 under `python -I`; all pass (see Verification).

## Research and reasoning

### Group6 M1 and the paragraph references

The group6 two-paragraph text is the starting point. Its internal references were checked against the current
tree:

| reference | current tree | action |
|---|---|---|
| "the Row length paragraph" | L2922 `\emph{Row length.}` | kept |
| "the State and coarse-graining paragraph" | L2924 | kept |
| "the transplanted selection rule" | defined at L2928 ("referred to below as the transplanted selection rule"); the inserts sit below it | kept |
| "the preceding paragraph" (in the second paragraph) | the first inserted paragraph | kept |
| "the Missing step paragraph", items (i)-(iv) | **absent** from Problem G | removed; the closing sentence L2938 carries the status |
| "diagonal-cut convention" (081) | E1: Frenkel's rule uses the block partition (the current L2928 already says so) | absent from the new text; the script asserts `diagonal-cut` is not in the applied file |
| 072-077 product testbed | the current tree treats the product block only in 067 (connected edge) | no dependence; the additivity clause is rewritten against the direct sum of L2928 |

### Re-derivations

The first paragraph (moments) rests on these steps.

1. **Single-cap pair.** The Row length eigenvalues are −2a ± 2(a²+r)^{1/2}, with sum −4a and product −4r. They
   are therefore the roots of λ²+4aλ−4r. The power sums are
   (−2)^m[(a−√(a²+r))^m + (a+√(a²+r))^m] = (−1)^m 2^{m+1} Σ_k C(m,2k) a^{m−2k}(a²+r)^k.
   Expanding (a²+r)^k binomially gives the stated double sum. `v1` A, B check this symbolically for m ≤ 12.
2. **Additivity.** The union of spectra gives the sum of power sums. The two cases are the band-separated caps
   (Row length paragraph) and the direct sum with momenta without inter-summand entries (L2928, exact). This
   replaces the old product-testbed framing.
3. **Sign reversal.** Π → −Π gives w → −w, so α → −α, a → −a and r → r. By step 1 the spectrum maps to its
   negative, so Q → −Q. Odd moments are odd and average to zero under any reversal-invariant state. At a = 0
   the eigenvalues are ±2√r, so Tr Q^{2p} = 2(4r)^p = 2ℓ^{2p} and the odd moments vanish (`v1` C, D).
4. **Exponential slots.** The MGF of Σ g_i E_i is Π(1−g_i t)^{-1} = Σ h_p t^p. So E r^p = p! s^{2p} h_p(g) and
   ⟨Tr Q^{2p}⟩|_{a=0} = 2·4^p s^{2p} p! h_p = 2(4s²W)^p ρ_p (`v1` E).
   - Partition form: h_p = Σ_λ p_λ/z_λ (`v1` F).
   - ρ_2 − 1 = s_2/W² (`v1` G).
   - ρ_p − 1 ≥ C(p,2)/D_eff: every partition term is ≥ 0; λ = 1^p gives 1, and λ = (2,1^{p−2}) gives
     p!/(2(p−2)!)·s_2/W².
   - ρ_p ≤ p!: every monomial of h_p has coefficient 1 ≤ its multinomial coefficient in W^p, with equality for
     p ≥ 2 only if one g_i ≠ 0 (`v1` H).
   - Sharp fixed-D bound: the 082 pair identity, re-checked symbolically for p = 2..7, shows that averaging an
     unequal pair strictly lowers h_p. The uniform value is Π_{k<p}(D+k)/D^p (`v1` I, 2000 exact-rational
     profiles, 0 violations, 0 equality off uniform).
5. **New check: the slot law of the Row length state.** Under conjugation by U_θ = e^{iθ n·J}, the entry Π_{vj}
   picks up the phase e^{iθ(m_v−m_j)}.
   - Invariance of the law forces E w_j w_k^* = 0 for j ≠ k.
   - It also forces E w_j w_k = 0, because the exponent 2m_v − m_j − m_k ≠ 0 when j and k both lie in the block,
     m_j, m_k > m_v.
   - Gaussian + uncorrelated + circular gives independent entries.
   - u = |M−1) is a basis vector, so α = w_u is independent of w_⊥ and r = Σ_{j≠u}|w_j|².
   - Normalisation: E|w_j|² = Σ_a|c^a|²⟨|Π_vj|²⟩ = s²g_j, since s² = Σ_a‖X^a_{ΣΣ̄}‖² = Σ_a|c^a|².
   - ⟨Tr Q²⟩ = 16⟨a²⟩ + 8⟨r⟩ = 8s²g_u + 8s²Σ_{j≠u}g_j, which is 8s² times the full row sum.
   - Band structure: T_{lm} has entries only on the diagonal at offset m (`v3` A), and |m| ≤ l ≤ l_c. So
     g_j = 0 for |j−v| > l_c. Removing u (distance 1) leaves at most l_c−1 slots with g > 0.
   - Cauchy-Schwarz gives D_eff ≤ #support ≤ l_c−1.
   - `v3` B/C builds the covariance and pseudo-covariance explicitly from the T_{lm} at N = 60, 400. Off-diagonal
     and pseudo parts are exactly 0, at most l_c−1 slots are nonzero, and D_eff = 15.57 (l_c=20), 29.52 (l_c=40)
     for f = l/2, and 29.01 for f = l(l+1)/4 at l_c=40. The proxy gives 1488.0 / 23016.9 (`v3` D), the 081/086
     numbers.
   - The argument holds for every deformation A, since Θ and the momentum law depend on n·J only.

The second paragraph (coupled slots) is checked in `v2` with exact symbolic Gaussian (Isserlis) moments at D = 3
and Σq = 1 imposed.

6. **Pair moments.** E a² = s²μ/2, E ar = 0, E r = s²(W−μ), and E a²r − E a² E r = s⁴Γ/2.
   - From p_2 = 16a² + 8r: ⟨Tr Q²⟩ = 8s²W.
   - From p_4 = 256a⁴ + 256a²r + 32r², the excess over the product law is 256·s⁴Γ/2 = 128s⁴Γ.
   - Independence: cov(w_⊥, α) = s²(1−uu†)Gu, and |(1−uu†)Gu|² = u†G²u − (u†Gu)² = Γ (`v2` C). If Γ = 0, then
     w_⊥ and α are uncorrelated and jointly circular, hence independent. Conversely, independence forces the
     covariance term, i.e. Γ, to vanish.
   - The eigenvalue clause of group6 ("the D−1 nonzero eigenvalues ...") is dropped: it needs all g_i > 0 and is
     not used.
7. **Frame-law locus.**
   - Γ = g^T(diag q − qq^T)g, which is PSD (it is the variance of g under q) and annihilates the constant
     profiles (`v2` D).
   - Kernel = profiles constant on the components of the coincidence graph. Constancy on components follows
     transitively from the a.e. constancy on supports. Conversely, frames meeting two components form a finite
     union of null sets. `v2` F checks 300 random finite laws, comparing the kernel dimension with the number of
     components.
   - The minimiser set at fixed W is that kernel, with minimum 0. The stationary set on the hyperplane satisfies
     2Σg = λ1; pairing with 1 gives λ = 0. The stated stationary set is on the hyperplane, without sign
     constraints.
   - Lower bound: write g = (W/D)1 + g_0 with g_0 of mean zero. Σ preserves 1^⊥ and |g_0|² = W²(D_eff^{-1}−D^{-1}).
   - Haar: q is uniform on the simplex, so E q_i² = 2/(D(D+1)) and E q_iq_j = 1/(D(D+1)), which gives
     Σ = (1−ee^T/D)/(D+1). This is 1/(D+1) times the projector onto mean zero (exact; Monte Carlo max error
     ≤ 4e-4).
   - A reparametrisation φ with φ' ≠ 0 multiplies the gradient by φ'. Positive combinations add PSD matrices,
     whose kernel is the intersection of the kernels, i.e. the union graph.

### Avenues (directive: a no-go is a fork)

The bounded no-go kept here: within Gaussian slot laws and profile-independent edge-vector laws, no
averaged-decoupling functional selects a profile value. It rests on these hypotheses:
- (H1) Gaussian slot law;
- (H2) laws of u independent of g;
- (H3) the functional is built from Σ_π only;
- (H4) the leading-order transplanted rule.

The correction in item 5 shows that in the actual Row length state (H2) is degenerate (u is a slot and Γ ≡ 0).
The profile there is fixed by the variance f(l) and the banded T_{lm}, i.e. by the state. So the missing
ingredient is the state, which is exactly the supplied input of the State and coarse-graining paragraph.
Group6 and this round agree: further refinement of the Gaussian profile does not move G-derived.

Ranked open avenues, unchanged from 072-080 r2:
1. a spacetime-block subsystem of a non-compact or Lorentzian leaf;
2. a split algebra with edge group U(M1)×U(M2);
3. derive rows-from-moments, where item 5 sharpens the target: at fixed l_c the fourth-moment mismatch is
   O(1) in N, so a rows-from-moments derivation must either take l_c → ∞ or use typical rather than averaged
   moments;
4. a within-core state, via OS reconstruction;
5. two-sided diagrams.

No new avenue is opened here.

### Literature

No new citation. The text uses only keys already present, `FlissFrenkelHartnollSoni2025` and
`Frenkel2023EdgeModes`, both cited by the existing paragraphs it relies on. The E1 confirmation (the block
partition in arXiv:2311.10131) comes from the 072-080 r2 gatekeeper review. I did not re-fetch it; not
independently verified in this round.

## Claim classification

| claim | class |
|---|---|
| quadratic λ²+4aλ−4r, the Tr Q^m formula, additivity for band-separated caps and the direct sum | established (exact) |
| Q → −Q under momentum reversal; odd averages vanish; a=0 moments 2ℓ^{2p} | established |
| E r^p = p! s^{2p}h_p, the ρ_p partition form, ρ_2−1 = 1/D_eff, ρ_p−1 ≥ C(p,2)/D_eff, ρ_p ≤ p!, sharp fixed-D bound | established (exact, for the stated exponential slot law) |
| Row length state: independent circular entries, u a slot, a ⟂ r, ⟨Tr Q²⟩ = 8s²·(row sum), at most l_c−1 slots, ρ_2−1 ≥ 1/(l_c−1) | established (exact, given the supplied state) |
| D_eff = 29.5 at N=400, M=N/2, l_c=40, f=νl/2 | numerical |
| "the reading of rows ... matches only at second moment, beyond only as D_eff→∞ (l_c→∞)" | conditional (on the transplanted rule, on averaged moments) |
| coupled-slot identities, independence iff Γ=0, 128s⁴Γ | established (exact, for the stated circular Gaussian slots) |
| frame-law locus, Haar Σ, λ⁺ bound, reparametrisation and union rigidity | established (exact) |
| "a profile is fixed only by the state" | conditional (within the stated functional class); the state stays a supplied input |
| bearing on Assumption `ass:Sent-density` / G-derived | unresolved, unchanged |

## Proposed changes

File `chapters/appH-microscopic-proofs.tex` only. There are two edits. No `\ref` or `\label` is added, and no
bib change is needed.

**S1: insertion.**
- Insert the two paragraphs below, each followed by one blank CRLF line, immediately before the line that starts
  `\emph{Vacuum term.} The abstract of~\cite{Steinacker2023}`.
- That anchor prefix occurs once (the other `\emph{Vacuum term.}`, in Problem F, has different text). It is
  current L2936 and directly follows `\emph{Coincident copies and the multiplicity reading.}` (L2934) and a blank
  line; the script asserts this adjacency.
- Placement: after the integrated edge block and before the closing scope sentence. It is not after 067, because
  067 has its own factor (the product of two spheres), its own Bearing paragraph and its own closing sentence,
  and the new paragraphs use the cap and direct-sum data of the edge block and its transplanted rule.
- Everything else is kept.

```latex
\emph{Moments of the edge charge in the Gaussian rank-one class.} With \(a=\operatorname{Im}\alpha\) and \(r=|w_\perp|^{2}\) as in the Row length paragraph, the nonzero eigenvalues of the charge of a single cap are the roots of \(\lambda^{2}+4a\lambda-4r=0\), so that, pointwise, \(\operatorname{Tr}Q^{m}=(-1)^{m}2^{m+1}\sum_{k\le m/2}\binom{m}{2k}\sum_{j=0}^{k}\binom{k}{j}a^{m-2k+2j}r^{k-j}\) for every \(m\ge1\); for the two band-separated caps of one axis, and for the direct sum of the two-component paragraph with momenta without entries between the summands, the moment sequences add (exact). Reversing the sign of the momenta sends \(Q\) to \(-Q\), so the odd moments average to zero in every state invariant under that reversal, and at \(a=0\) the even moments are \(2\ell^{2p}\), with \(\ell=2r^{1/2}\) the row length. If \(r=s^{2}\sum_{i}g_{i}E_{i}\) with independent unit exponentials \(E_{i}\), a profile \(g=(g_{1},\dots,g_{D})\) of \(D\) slots and \(W=\sum_{i}g_{i}\), then \(\langle\ell^{2}\rangle=4s^{2}W\) and, at \(a=0\), the averaged \(2p\)-th moment is its single-row value \(2(4s^{2}W)^{p}\) times \(\rho_{p}(g)=p!\,h_{p}(g)/W^{p}=\sum_{\lambda\vdash p}(p!/z_{\lambda})\prod_{k\ge1}(s_{k}/W^{k})^{m_{k}}\), with \(h_{p}\) the complete homogeneous symmetric polynomial, \(s_{k}=\sum_{i}g_{i}^{k}\) and \(m_{k}\) the multiplicity of the part \(k\) in \(\lambda\); hence \(\rho_{2}-1=1/D_{\mathrm{eff}}\) with \(D_{\mathrm{eff}}=W^{2}/s_{2}\), \(\rho_{p}-1\ge\binom{p}{2}/D_{\mathrm{eff}}\), \(\rho_{p}\le p!\) with equality for \(p\ge2\) only when one slot carries all the weight, and \(\rho_{p}\ge\prod_{k=1}^{p-1}(1+k/D)\) with equality for \(p\ge2\) only at the uniform profile (exact). In the Gaussian state of the Row length paragraph, as in every Gaussian state of the momenta invariant under conjugation by \(e^{\mathrm i\theta\,n\cdot J}\), the entries of the boundary row \(w\) in the eigenbasis of \(n\cdot J\) are independent circular complex Gaussians, since distinct entries carry distinct charges under that rotation; so \(a\) is independent of \(r\), \(r\) has the form above with \(s^{2}g_{i}\) the variances of the entries other than the one at \(u\), and \(\langle\operatorname{Tr}Q^{2}\rangle\) is \(8s^{2}\) times the full sum over the boundary row inside the block (exact). These variances vanish for entries more than \(l_c\) places from \(v\) in that eigenbasis, so at most \(l_c-1\) slots carry \(r\) and \(\rho_{2}-1\ge1/(l_c-1)\) for every \(N\) and \(M\) (exact); \(D_{\mathrm{eff}}=29.5\) at \(N=400\), \(M=N/2\), \(l_c=40\) and \(f=\nu l/2\) (numerical). The reading of the rows from the edge data in the transplanted selection rule therefore matches the averaged charge moments exactly at the second moment, and beyond it only as \(D_{\mathrm{eff}}\to\infty\), which in this state requires \(l_c\to\infty\).

\emph{Coupled slots and laws of the edge vector.} For a Gaussian state without that invariance, write the boundary row in a basis of \(D\) slots in which \(\mathbb{E}\,w_{i}w_{j}^{*}=s^{2}g_{i}\delta_{ij}\), assume the slots circular, and set \(q_{i}=|u_{i}|^{2}\), \(W=\sum_{i}g_{i}\), \(\mu=\sum_{i}q_{i}g_{i}\) and \(\Gamma=\sum_{i}q_{i}(g_{i}-\mu)^{2}\). Then \(\mathbb{E}\,a^{2}=s^{2}\mu/2\), \(\mathbb{E}\,ar=0\), \(\mathbb{E}\,a^{2}r-\mathbb{E}\,a^{2}\,\mathbb{E}\,r=s^{4}\Gamma/2\) and \(|(\mathbf 1-uu^{\dagger})Gu|^{2}=\Gamma\), with \(G=\operatorname{diag}(g)\), so \(a\) and \(r\) are independent if and only if \(\Gamma=0\), that is, if and only if \(g\) is constant on the support of \(u\), which holds in the preceding paragraph, where \(u\) is one slot; \(\langle\operatorname{Tr}Q^{2}\rangle=8s^{2}W\) for every \(u\), and \(\langle\operatorname{Tr}Q^{4}\rangle\) exceeds its value for independent \(a\) and \(r\) with the same marginals by \(128s^{4}\Gamma\) (exact). For a law \(\pi\) of \(u\) independent of \(g\), \(\mathbb{E}_{\pi}\Gamma=g^{T}\Sigma_{\pi}g\) with \(\Sigma_{\pi}=\mathbb{E}_{\pi}(\operatorname{diag}(q)-qq^{T})\) positive semidefinite and annihilating the constant profiles. On the hyperplane \(\sum_{i}g_{i}=W\) the zero set, the minimiser set and the stationary set of \(\mathbb{E}_{\pi}\Gamma\) are the profiles constant on the components of the graph in which \(i\) and \(j\) are joined when \(\pi(q_{i}q_{j}>0)>0\); this is the uniform profile alone exactly when the graph is connected, as for the Haar law, for which \(\Sigma_{\pi}\) is \(1/(D+1)\) times the orthogonal projector onto the profiles of mean zero; and \(\mathbb{E}_{\pi}\Gamma\ge\lambda^{+}W^{2}(D_{\mathrm{eff}}^{-1}-D^{-1})\), with \(D_{\mathrm{eff}}=W^{2}/\sum_{i}g_{i}^{2}\) and \(\lambda^{+}\) the least eigenvalue of \(\Sigma_{\pi}\) on profiles of mean zero (exact). The stationary set is unchanged under reparametrisations with nowhere-vanishing derivative and becomes that of the union of the graphs under positive combinations of laws, so no functional built in this way from averaged decoupling data selects a value of the profile within a component; a profile is fixed only by the state, which the State and coarse-graining paragraph leaves as a supplied input. These two paragraphs fix no state, \(s\), \(g\) or edge vector.
```

**S2: extend the closing scope sentence.** It must be extended. As it stands it covers Gaussian states only
"with the stated variances or the stated momentum data", which does not cover the exponential slot laws or the
laws of the edge vector π.
- In the line that starts `These statements are for a compact factor with positive contraction; for a single
  projector` (L2938, unique), replace the clause (unique in the file):

```latex
and for Gaussian states with the stated variances or the stated momentum data.
```
- with:

```latex
and for Gaussian states with the stated variances, the stated momentum data or the stated slot laws, with the stated laws of the edge vector.
```
- The rest of the line is kept verbatim, including the status sentence "Problem~G remains open and
  PROGRAMME-CONDITIONAL". The whole replaced line is in `closing_r2.tex`.

The status sentence is not repeated in the inserts. The block keeps one closing status sentence.

**Stale passages elsewhere:** none in the current tree. The gpu backup's 081-088 paragraphs were never
integrated here, and `grep diagonal-cut` finds nothing in appH.

**Byte contract:**

| item | value |
|---|---|
| pre appH sha256 | `779bfcac09504722912302eb74299f4ba045dca64c65c166799b7bc3f70f723f` (676585 B, CRLF 3463, bare LF 0); equals the recorded POST of 072-080 r3 |
| `insert_r2.tex` | `9d6f2b033fb022d82cd2aa73e077e5643379074fabbae2ef4b0feab044514ee3` (5210 B, CRLF) |
| `closing_r2.tex` | `44f1695d0b403fbc513439d0c55aab2fee4dd345d3c2b2c66772ba73b706ea08` |
| `clause_r2.txt` | `06b5de4cb36316a02b0343fa39e1e6679643c6d6f97b97c9ad5a9722e33a4e7a` |
| post appH sha256 | `c541fb20694cb723cf08be52593466ec2f0e267d28d7118690c6bded43fa559a` (681858 B, CRLF 3467, bare LF 0) |

The script asserts that the post file minus the insert, with the clause reverted, is byte-identical to the pre
file.

## Verification scripts

All are in `proposals/local-gpu/081-088-r2/`, run from the repository root with `python -I`. Outputs are saved
as `*.out`.

| script | checks | expected last line / invariants |
|---|---|---|
| `v1_moment_map.py` | steps 1, 3, 4 | A-I all `True`, violations 0, `equality off uniform: 0`, MC rel < 1e-2; `PASS v1` |
| `v2_coupling_locus.py` | steps 6, 7 | A `[True]*4`, B `[True, True]`, C True, Haar exact True with MC err < 2e-3, F failures 0; `PASS v2` |
| `v3_row_length_profile.py` | step 5 | offdiag 0 and pseudo 0; slots ≤ l_c−1; `D_eff(r) = 29.52` at N=400, M=200, l_c=40, f=l/2 (15.57 at l_c=20; 29.01 for f=l(l+1)/4); proxy 1488.002 / 23016.894; `PASS v3` |
| `make_snippets_r2.py` | writes `insert_r2.tex`, `clause_r2.txt`, `closing_r2.tex` (reads appH read-only) | hashes above |
| `apply_build_r2.py OUTDIR --build` | anchors S1/S2 count 1; S1 follows Coincident copies; byte contract; no `diagonal-cut`, no "Missing step paragraph"; status-sentence count unchanged; out-of-repo build | `BUILD PASS pages=394`, `undefined/multiply-defined warnings: 0` (see `apply_build_r2.out`) |

Reproduction pack:

```
python -I proposals/local-gpu/081-088-r2/v1_moment_map.py          # PASS v1
python -I proposals/local-gpu/081-088-r2/v2_coupling_locus.py      # PASS v2
python -I proposals/local-gpu/081-088-r2/v3_row_length_profile.py  # D_eff(r) = 29.52 ... PASS v3
python -I proposals/local-gpu/081-088-r2/apply_build_r2.py <dir outside repo> --build   # post sha c541fb20..., BUILD PASS pages=394
```

All 19 inherited scripts pass under `python -I` as of this round:
- 081 s1_r2, s2, s3_r2;
- 082 s1_v2;
- 083 s1, s2d, s3b;
- 084 s1, s2, s4;
- 085 s1, s2, s5;
- 086 s1;
- 087 s1, s2, s3;
- 088 s1, s2.

Their proxy outputs (1488, 23017, the 8/9 limit, the W²/(8D²) rate) are correct arithmetic on the mode-count
proxy. They are no longer cited.

The applied-copy build was in the session scratchpad. Deleting its build directory was refused by the
permission system, so it remains there. It is outside the repository.

## Decisions Taken

- **D1 (M1): accept the two-paragraph consolidation** rather than the fallback minors m1-m4.
  - m1 and m3 are absorbed: the ν-factors no longer appear, since the proxies are dropped, and the
    G^{1/2}(1−uu†)G^{1/2} clause is dropped, as unused and needing g > 0.
  - m2 is absorbed: no Kuriki-Numata attribution.
  - m4 is moot: no "named coupled gaussian slot law" wording.
- **D2: drop the mode-count proxy** instead of keeping it as a labelled proxy. Re-derivation shows it is not the
  slot law of the only state the manuscript supplies (step 5). Keeping its D_eff ≈ 0.89 l_c² next to the
  transplanted rule would suggest the averaged-moment identification is recovered at leading order, when in the
  Row length state D_eff ≤ l_c − 1. Replacing it with the exact bound is shorter and correct.
  - Rejected: keeping the proxy with a caveat (longer, and misleading about rates).
  - Rejected: computing the true profile in closed form (a refinement, against the group6 advice).
- **D3: keep the frame-law no-go**, scoped to Gaussian states without axial invariance, because it bounds a
  selection route (averaged decoupling) and points to the state as the missing ingredient. That favours the
  G-derived route by excluding a dead end. The per-frame range bound, the two-block example and the
  degenerate-reparametrisation continuum of 087/088 are dropped as non-load-bearing.
- **D4: placement** before `\emph{Vacuum term.}`, after the integrated edge block, with the closing clause
  extended (S2). The reasons are given under Proposed changes.
- **D5: the "Missing step paragraph" reference is removed**, not repaired by restoring the gpu-import Missing
  step paragraph. Restoring it would be a separate status-passage package needing a full scan. The closing
  sentence already records what is not derived.

## Milestone assessment

Routine. No MILESTONE trigger applies. The correction in step 5 is a scope correction inside a model, not a
critical-path derivation.

## Status-label recommendation

From ch17 L700-735, the critical-path set at the full-GR / matrix-derived scope is A, B, C, D1, E, F, G-derived
and N, all OPEN; this package touches only G. Problem G stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.
There is no label change.

## Author decision needed

None.

## Remaining open step

G-derived still needs:
- an infrared entropy density on ∂M derived from the matrix theory, with the block-to-∂M identification derived
  rather than supplied (Bearing (i), (iii));
- the boundary stationarity relation of `ass:bdy-EE`;
- the Λ_eff scaling that follows from them;
- for this sub-line specifically, a state produced by the core (State and coarse-graining paragraph), since the
  profile, l_c and the moment-row reading are fixed only by it.

The edge-entropy route also still needs the rank-dependence obstruction resolved (Bearing (ii)).

## Special instructions for the gatekeeper

- Re-derive step 5, which is the new load-bearing claim:
  - the U(1) phase argument for the covariance and the pseudo-covariance;
  - the T_{lm} offset structure;
  - D_eff ≤ l_c − 1.
- Confirm that the Row length state is invariant under conjugation by e^{iθ n·J}: the variance is f(l) per spin-l
  sector, and the Π^a are independent with the same law.
- Possible prior-claim imprecision, not edited here: the Row length paragraph states ⟨ℓ²⟩ = 4s²W, with W the full
  row sum, "with Im α neglected". Exactly, ⟨Tr Q²⟩/2 = 4s²W and ⟨(2|w_⊥|)²⟩ = 4s²(W − g_u). The share
  g_u/W = 0.0085 at l_c = 20 and 0.042 at l_c = 40 (N = 400, M = 200, f = l/2; computed ad hoc from `v3`'s
  `row_cov`). Decide whether this needs a later minor note; I made no change, to keep this package minimal.
- Must not be asserted:
  - that the moments paragraph derives rows from moments;
  - that averaged moments are what the transplanted rule uses at leading order (the closing sentence and
    "conditional" scoping apply);
  - that the frame-law no-go extends beyond Gaussian slot laws and profile-independent laws.
- The stationary set in the second paragraph is on the hyperplane Σg = W without sign constraints. Check that the
  wording "On the hyperplane" suffices.
- OPEN count against group6-G2: M1 addressed (0/1 open). The fallback m1-m4 are absorbed or moot (D1). 072-080
  E1 is addressed: no "diagonal-cut" in the new text.
