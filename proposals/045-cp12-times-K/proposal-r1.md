# Proposal 045-cp12-times-K, round 1

## Result

The computation that 044 left open is done, at the frozen-fibre leading symbol. 044's top-ranked avenue was: on CP^{1,2} (finite fibre) × K at IKKT content, find the Dirac/vector index density of the mixed term on the six level-one modes, and whether those modes source axial torsion.

Inputs to the computation:
- 044's exact factorisation. The mixed term is −(1/4)σ^M τ^K. At order (2,2) it equals −(1/8)v₂ᴹv₂ᴷ. The vector index part never enters it.
- The hybrid evaluation of Steinacker 2303.08012 §7 (finite fibre, K scale above the fibre fluxes).

All the M-data reduce to the Poisson-algebraic frame E^{aμ} = {X^a, y^μ} and torsion T^{abμ} = {F^{ab}, y^μ} of the level-one amplitudes, evaluated per fibre point and then traced over the fibre.

**Established (exact identities at the leading symbol; Lie–Poisson verified on an explicit orbit realisation):**

1. **Background frame and torsion.** E^{aμ} = s m η^{aμ} and T̄^{abμ} = η^{aμ}y^b − η^{bμ}y^a. Both are fibre-independent; this is an exact Poisson-algebra identity.
2. **Rank-one lemma.** For any amplitude α^a(t)e^{iq·y} (any fibre dependence), the frame perturbation at a fibre point is δE^{aμ} = α^a v^μ (up to phase), with v = M(t)q = Σ_j n^j s_j. So the pointwise frame perturbation is rank one. The torsion is δT^{abμ} = −m v^μ(q^aα^b − q^bα^a), and the pointwise index density is X(t) = m⁻⁴(v·v)(q²α·α − (q·α)²).
   - For level-one modes α = Σ_i n^i c_i. s1 verifies δE, δF and δT against a direct Lie–Poisson computation at 12 random orbit points, relative residual ≤ 3e-14.
3. **Torsion content (answer to (a)).** Write c_i = D_ij s_j + γ_i q. The γ are gauge, sym D gives the six physical polarisations, and antisym D the three inert amplitudes.
   - Averaged frame: the six source **no axial torsion**. They source vector torsion V^a ∝ q^a tr(DG), i.e. only through the trace of h̄. The inert three source axial torsion.
   - Fibre-resolved: the six **do** source axial torsion, ∝ [D, nnᵀ]. It sits in the second fibre harmonic, averages to zero, and vanishes identically only for D ∝ 1.
   - Exact rational arithmetic in 7 cases (4 base points, 5 wave vectors incl. one time-like, both fibre orientations).
4. **Averaged-frame reading (densities of the fibre-averaged frame).** Exactly, at every sampled point:
   - X = −2·EH(h̄) + k(tr h̄)²;
   - a₁,scalar = (1/6)EH(h̄) + k′(tr h̄)²;
   - the inert amplitudes decouple from h̄.

   Hence on the **five traceless polarisations** there is a single coefficient c_T = W_R/6 − 2W_X. On the trace polarisation c_T = −(5/24)W_R + W_X. With the ledger cone values, the fixed-state replica gives c_A = W_R/6 − 2W_X, so **c_A − c_T = 0 on the five traceless polarisations (finite parts), with no Stueckelberg input**. This is the 044 criterion realised. The other gaps:

   | replica | five traceless | trace polarisation |
   |---|---|---|
   | periodic | 2W_X | 3W_R/8 − W_X |
   | smooth | −W_R/4 + 2W_X | W_R/8 − W_X |
   | fixed-state | 0 | 3W_R/8 − 3W_X |

5. **Trace reading — the actual one-loop fibre trace (bounded no-go).** The fibre trace of a multiplication operator is its fibre average, so the index and scalar densities are ⟨X(t)⟩ and ⟨a₁(t)⟩. These are not the densities of ⟨E⟩. On the six polarisations, at all 7 cases:
   - neither form lies in the covariant span {q²h̄·h̄, q²(tr h̄)²}; the best-fit residual is 0.03–0.36;
   - both couple the inert amplitudes to the six;
   - the generalised eigenvalues vs EH(h̄) on the five traceless polarisations are distinct and of both signs (index form −4.36 ×2, −0.73 ×2, +0.47 at case 1);
   - exact linear algebra finds no W_R:W_X that makes the sum proportional to EH or covariant;
   - −2 is never a generalised eigenvalue of the index form, so the mixed-term part of the fixed-state gap vanishes on no traceless polarisation.

   So there is **no single G_T, for any K**, in this reading. An independent Monte Carlo/Lie–Poisson computation on the explicit realisation agrees (s3).
6. **Regime fork.**
   - The equal-weight trace applies when the K scale exceeds the fibre gaps. This is Steinacker's regime (his (7.25): m_s² a small IR scale).
   - The averaged-frame forms are exactly the trace over fibre-constant loop modes with projected coefficients. The full trace approaches them when the fibre gaps exceed the K scale, because intermediate second-harmonic states are then Duhamel-suppressed. This is an argument, not computed.
   - In that regime the first term of the factorisation has a fibre-flux two-derivative part (Steinacker §7.1.2, stated there to be non-Lorentz-invariant a priori). It is not suppressed there and not computed here.

**Breakthrough self-assessment:** a single matrix-derived Einstein coefficient with G_A = G_T is **not** obtained in a rank-6 class.
- What holds in the averaged-frame reading is: G_A = G_T for the finite parts, on five of six polarisations, fixed-state replica. That reading is conditional on a regime whose own non-covariant contribution is uncomputed.
- In the regime of the cited construction, the trace reading excludes it at the leading frozen symbol.

## Target and status

- **Problem F** (`sec:status-F`, appH L1366), verbatim: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. Reduced-scope result: treating G_eff as an input leaves F OPEN and does not satisfy the matrix-derived criterion."
  - Ch17 target (`sec:ch17-done` item 6): A, B, C and the sign/scheme dependence of G_eff computed from the specified operators; G_eff not an input.
- **Problem B** (`sec:status-B`, L45): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived."
  - Ch17 target: Assumption EE as a lemma, including fixed-volume variations of the non-conformal tensor block. The sub-target used here is G_T = G_A (normalisation paragraph, L174).
- **Critical-path set:** Ch17 `sec:ch17-done` = A, B, C, D1, E, F, G-derived, N. Appendix H agrees; no discrepancy.
- **Dependencies:**
  - F on D1, E and the class;
  - B on A (state/replica) and F;
  - the trace polarisation touches C (conformal mode).
- **Completion classification of this package:** PROGRAMME-CONDITIONAL; nothing DERIVED.

## Source reading

**Full scan.** `make_digest --check` printed DIGEST CURRENT with dirty-chapters: yes, so 3(d) applies. I read every file of the 30-file manifest in full:
- ch01–ch18;
- appA–appG, appI–appL;
- appH in ranges covering L1–2896.

The dirty diff (`git diff --stat`, ch07 and bib hunks) is the accepted 043/044 integrations. The 044 paragraph (L2370–2391) and the 043 block (L387–398) were read in full.

Also read:
- `proposals/044-*` (r1, r2, both reviews, s1, s4, compile_check);
- `proposals/013-*` realisation and model scripts;
- `strategy-20261025/assessment.md` (relevant parts);
- `reports/sme-scout-20261025.md` (R2);
- the ledger tail.

No unreadable files.

## Research and reasoning

### 1. Setting and hypotheses

- **H1.** Product M × K, no mixed flux (044).
- **H2.** IKKT content supplied (044).
- **H3.** Poisson limit on M. M is the conjugate-coordinate class: T^a = M^{a4}, base y^μ = M^{μ5}, level-one A^a = c_i^a(y)n^i.
- **H4.** One loop.
- **H5.** Frozen coefficients at a base point with y^i = 0; other points follow by SO(3,1) covariance. Plane wave e^{iqy}, |q|ℓ ≫ 1, leading symbol (highest power of q in each form).
- **H6.** Hybrid fibre treatment, as in Steinacker §7. The fibre momenta and the fibre components of the Hamiltonian fields are dropped; this holds for K scale ≫ fibre fluxes (merged 2185(i): replication is the s·f ≪ 1 limit). The fibre trace of a multiplication operator is the uniform fibre average. This holds for any harmonic weights, since Σ_m⟨Y_sm|f|Y_sm⟩ is SU(2)-invariant and so picks out the l = 0 component of f.
- **H7.** Replicas: the ledger cone values (044), with the cone in the base at every fibre point.
- **H8.** Orientation-even mixed term.
- **H9.** Formal Lorentzian η (as in merged 2181).

### 2. Leading symbols

- δE^{aμ} = {A^a, y^μ} ≈ ∂_νA^a{y^ν, y^μ} = ∓i q_ν M^{νμ}(t)α^a, i.e. rank one.
- δF^{ab} ≈ Ē^{aμ}∂_μA^b − (a↔b) = −i m(q^aα^b − q^bα^a).
- δT^{abμ} = {δF^{ab}, y^μ} ≈ −m v^μ(q^aα^b − q^bα^a). This equals the anholonomy of the frame E(t) at frozen t (Jacobi identity).
- Terms hitting n^i, m or S_i(y) carry no q and are subleading.
- s1 confirms the closed forms with fitted constants −i, −i and −1, relative residual 3e-14, and finds no higher powers of λ.

### 3. Densities (normalisation)

- **Scalar.** Per fibre point the scalar operator is −∂γ∂, with γ = η_ab E^aE^b; the frame is divergence-free because q·v = 0. By the 044 lemma it is −λΔ_ĝ, ĝ = √(detγ)γ⁻¹. Its a₁ density per d⁴y is (1/6)R[ĝ] = (1/6)√G R[G] − √G|∂φ|² mod total derivatives, with G = γ⁻¹ and φ = −¼ln det G (conformal formula).
- **Index.** The index a₁ is √G G_μν η η T T, the merged normalisation of ρ²X.
- **Checks.**
  - The Fierz–Pauli implementation of the second variation of √g R is validated against a direct curvature computation in both signatures (s2 (0)). An initial factor-2 error was caught by this test and fixed.
  - Calibration in the four-coordinate class: index form = −4 EH and scalar form = (1/6) EH on the δρ = 0 modes, both signatures. This reproduces merged L177/L2385 (s2 (1)).

### 4. Fibre averages

The fibre is S², with n uniform on the unit sphere. In s1 the realisation's fibre lies on the invariant quadric to 4e-14, and its W_y basis matches the 013 model S_i = ℓ[e_i∧v̂ + e_j∧e_k] to 2e-14.
- Exact moments: ⟨n_in_j⟩ = δ/3, ⟨n⁴⟩ = (δδ+δδ+δδ)/15.
- The closed form of the index form is ∝ 2tr(GC) + trG·trC, with C = q²DGDᵀ. The tr G·tr(DGD) structure is what breaks covariance: G = SᵀηS is not covariant in q.
- s3 recomputes the trace forms from the Lie–Poisson symbols with Monte Carlo fibre sampling and the realisation's own basis. Its eigenvalues agree with s2 (exact-design column to all printed digits; Monte Carlo within noise).

### 5. Why the trace reading, and the comparison with Steinacker

Steinacker §7.2.1 evaluates the M–K mixed term "as in (6.24)", i.e. T·T·G with T the torsion of a frame on M^{3,1}.
- For fibre-independent torsion (the background) both readings agree.
- For level-one fluctuations, the torsion depends on the fibre point. The rank-one lemma shows no fluctuation content can make it fibre-independent: a single wave gives δE ∝ α(t) ⊗ v(t), with v(t) sweeping q^⊥.
- The trace of 𝔽𝔽 over all loop modes φ(y)Y_sm(t) is N·⟨TT⟩.

The averaged-frame reading corresponds to dropping the second fibre harmonic. It is exact for the s = 0-truncated loop. I do not claim the cited work is wrong. Its fluctuation treatment is not examined, and its graviton is not identified here with the level-one amplitudes.

### 6. Literature

- **Steinacker 2303.08012** (bib `Steinacker2023`). arXiv PDF fetched; §4.1, §6.2 and §7 read. Used: (7.1)–(7.5), with m_s² = 3s/R² as an IR mass; §7.1.2 and its remark that the k̃ contraction is "not Lorentz invariant a priori"; (7.14)/(7.25) (K dominance); (7.21)–(7.24).
- No new citation; no BibTeX.
- **Not independently verified:** Steinacker's normalisation of G_N, and how his hs fluctuations are averaged.

### 7. Hypotheses of the no-go and relaxations (fork)

The trace-reading no-go (no single G_T on the six or the five, any K) depends on H1–H6, H8, H9 and on carrying the six by level-one amplitudes.

Explored here:
- **Averaged frame / heavy fibre (H6 regime).** This route works on the five traceless polarisations. It is recorded as a conditional route.
- **Other fluctuation content (higher fibre harmonics).** The rank-one lemma excludes a fibre-constant frame for any content at the leading symbol.
- **Replicas (H7).** All three ledger replicas were tabulated.

Ranked open avenues:
1. **Interpolation between the regimes.** Compute the second-order Duhamel term with the loop fibre-harmonic gaps Δ_s (derive m_s² in this class rather than import it). This gives W_X′ = −(1/8)∫ds s⁻²τ^K w(sΔ₂), the weight of the non-covariant second-harmonic part. Also compute the first-term fibre-flux (S²–M) two-derivative part in the same regime. Together these decide whether any regime has covariant leading K-dependent EH.
2. **Effective form for h̄ after eliminating inert and higher-harmonic amplitudes.** In the induced-dominated window above the crossover (merged 2162/2174), take the Schur complement with the tree Maxwell forms. Could this restore an Einstein form?
3. **Trace polarisation.** Couple it with the conformal sector (Problem C): the mismatch is localised in the dilaton direction even in the favourable reading.
4. Λ² and log first-term excess and replica selection (044 avenue 2; Problem A).
5. Subleading symbol, finite fibre beyond the hybrid (hypoelliptic).
6. Non-product backgrounds.
7. Explicit K (sign of W_R).

## Claim classification

| # | Claim | Class |
|---|---|---|
| 1 | Background frame/torsion of CP^{1,2}, fibre-independent | established (exact Poisson algebra) |
| 2 | Rank-one lemma; δT and X(t) closed forms | established at the leading symbol (derivation + Lie–Poisson check 3e-14) |
| 3 | Averaged-frame torsion: no axial on the six, vector ∝ q tr h̄, axial on the inert | established (exact rational, 7 cases; algebraic) |
| 4 | Fibre-resolved axial ∝ [D, nnᵀ], zero only for D ∝ 1 | established (algebraic; exact checks) |
| 5 | Averaged-frame forms: X = −2EH + k(tr h̄)², a₁ = EH/6 + k′(tr h̄)²; c_T = W_R/6 − 2W_X (five), −5W_R/24 + W_X (trace) | established at frozen leading symbol (exact rational, 7 cases) |
| 6 | Fixed-state c_A − c_T = 0 on the five (finite parts) in the averaged-frame reading; other gaps | conditional (ledger cone values; cone in base, fibre spectator) |
| 7 | The one-loop trace is the fibre average of pointwise densities | conditional (hybrid H6; semiclassical fibre) |
| 8 | Trace reading: no single G_T for any W_R:W_X; inert coupling; eigenvalue spread | established at 7 sampled cases (exact linear algebra), numerical values as stated |
| 9 | Regime correspondence (equal weight ↔ K ≫ gaps; averaged ↔ gaps ≫ K) | conjecture/argument (Duhamel suppression, not computed) |
| 10 | First-term fibre-flux two-derivative part in CP^{1,2} | unresolved (cited as non-Lorentz-invariant a priori; not computed) |
| 11 | No G_eff value or sign; no closure | unresolved |

## Proposed changes

### `chapters/appH-microscopic-proofs.tex`

**Placement.** Insert `proposals/045-cp12-times-K/appH_insert.tex` as one paragraph at the end of the Problem F ledger:
- immediately after the 044 paragraph, whose last line is "...Problems~B and~F remain open and PROGRAMME-CONDITIONAL.";
- immediately before the unique line `\section{Problem G: HBEV}`, with one blank line before the anchor.

**Anchor and file checks.**
- The anchor occurs once, and the line before it is the 044 closing sentence (checked by s5).
- The file is 7691 bytes: ASCII, LF, 0 CR, 0 TAB.
- Braces, `\(`/`\)` and `\[`/`\]` are balanced.
- One `\paragraph`, no `\label`.
- The integrator converts it to CRLF.

**References.**
- `\ref`s: `sec:status-B`, `ch:vierbein-emergence` and `ass:lorentzian`, each defined once.
- Cite: `Steinacker2023`, present in the bib.
- No BibTeX added.

Nothing is replaced.

```latex
\paragraph{Conjugate-coordinate class times a fuzzy factor: torsion of the level-one amplitudes and the induced Einstein coefficient (conditional; bounded no-go and conditional route).}
This paragraph supplements the preceding one, in which the two-derivative density of the mixed term on the six level-one amplitudes, its cone values and the torsion those amplitudes source were not computed. Take for \(M\) the conjugate-coordinate class (Poisson limit, leaf \(\mathbb{CP}^{1,2}\), \(X^a=T^a+A^a\), \(T^a=M^{a4}\), base functions \(y^\mu=M^{\mu5}\), \(m=M^{45}\)), the split \(d=4\) and \(K\) of the preceding paragraph, the level-one amplitudes \(A^a=c_i^a(y)\,n^i\) with \(M^{\mu\rho}=\sum_in^iS_i^{\mu\rho}\) on the fibre, \(n\) a unit vector of the fibre two-sphere, a plane wave \(e^{\mathrm iq\cdot y}\) with frozen coefficients at a base point, \(|q|\ell\gg1\), \(s_i^\mu=S_i^{\mu\nu}q_\nu\), \(G_{ij}=s_i\cdot s_j\), and the leading symbol in which the fibre momenta and the fibre components of the Hamiltonian fields are dropped and the trace over the fibre harmonics of a multiplication operator is its fibre average. This is the hybrid evaluation of Section~7 of~\cite{Steinacker2023}, for a finite fibre and a scale of \(K\) above the fibre fluxes.

\emph{Frame and torsion.} With \(E^{a\mu}=\{X^a,y^\mu\}\), \(F^{ab}=\{X^a,X^b\}\) and \(T^{ab\mu}=\{F^{ab},y^\mu\}\), the background has \(E^{a\mu}=\pm m\,\eta^{a\mu}\) and \(T^{ab\mu}=\eta^{a\mu}y^b-\eta^{b\mu}y^a\), independent of the fibre point (exact in the Lie--Poisson algebra). At the leading symbol, for an amplitude \(\alpha^a\) with any dependence on the fibre point, \(\delta E^{a\mu}=\alpha^a v^\mu\) up to a constant phase, with \(v=\sum_jn^js_j\), so the frame perturbation at a fibre point has rank one, and \(\delta T^{ab\mu}=-m\,v^\mu(q^a\alpha^b-q^b\alpha^a)\); for the level-one amplitudes \(\alpha=\sum_in^ic_i\) (verified by a Lie--Poisson computation at points of an explicit realisation of the orbit, relative residual \(3\cdot10^{-14}\)). Write \(c_i=D_{ij}s_j+\gamma_iq\). The \(\gamma_i\) are gauge directions, the fibre-averaged metric depends only on the symmetric part of \(D\), which gives the six polarisations, and the antisymmetric part gives the three inert amplitudes. The torsion of the fibre-averaged frame has no axial part on the six polarisations and a vector part proportional to \(q^a\operatorname{tr}(DG)\), that is to the trace of the averaged metric perturbation; the inert amplitudes carry axial torsion. At a fibre point the six polarisations do source axial torsion, proportional to \([D,nn^{T}]\) and so in the second fibre harmonic; it averages to zero and vanishes identically only for \(D\propto\mathbb I\) (exact rational arithmetic in seven sampled cases: four base points, five wave vectors including a time-like one, both orientations of the fibre basis).

\emph{Two-derivative forms.} In the normalisation of the preceding paragraph, for a real wave averaged over its phase, the index density at a fibre point is \(X=m^{-4}(v\cdot v)\,(q^2\alpha\cdot\alpha-(q\cdot\alpha)^2)\), and the scalar density is \(\tfrac16\sqrt{|G|}R[G]-\sqrt{|G|}\,G^{\mu\nu}\partial_\mu\phi\,\partial_\nu\phi\), with \(G\) the inverse of \(\eta_{ab}E^aE^b\) and \(\phi=-\tfrac14\ln|\det G|\). With these densities the two modes with \(\delta\rho=0\) of four coordinates have the index form \(-4\) and the scalar form \(\tfrac16\) times the Einstein--Hilbert form, as in the preceding paragraph. For the fibre-averaged frame, exactly at every sampled point, the index form is \(-2\) times the Einstein--Hilbert form \(\mathrm{EH}(\bar h)\) of the averaged metric plus a multiple of \(q^2(\operatorname{tr}\bar h)^2\), and the scalar form is \(\tfrac16\,\mathrm{EH}(\bar h)\) plus such a multiple. The inert amplitudes do not couple to \(\bar h\) and enter only through the axial term. Hence, in the units \(c\) of the preceding paragraph, \(c_T=\tfrac16W_R-2W_X\) on the five traceless polarisations and \(-\tfrac5{24}W_R+W_X\) on the trace polarisation, their complement in the six. With the cone values of the preceding paragraph and the cone in the base at every fibre point, the fixed-state replica has \(c_A=\tfrac16W_R-2W_X\), equal to \(c_T\) on the five traceless polarisations for the finite parts, without the dressed density of the paragraph on local frame rotations. The periodic and smooth gaps there are \(2W_X\) and \(-\tfrac14W_R+2W_X\). On the trace polarisation the fixed-state, periodic and smooth gaps are \(\tfrac38W_R-3W_X\), \(\tfrac38W_R-W_X\) and \(\tfrac18W_R-W_X\).

\emph{Fibre trace.} The fibre averages of the pointwise densities differ from these by the second fibre harmonic. On the six polarisations neither form lies in the span of \(q^2\bar h_{\mu\nu}\bar h^{\mu\nu}\) and \(q^2(\operatorname{tr}\bar h)^2\) (relative residual of the best fit between \(0.03\) and \(0.36\)), both couple the inert amplitudes to the six, and their generalised eigenvalues relative to \(\mathrm{EH}(\bar h)\) on the five traceless polarisations are distinct and of both signs (for the index form \(-4.36\), \(-0.73\), each twice, and \(0.47\) at one point). No ratio \(W_R:W_X\) makes their sum proportional to \(\mathrm{EH}(\bar h)\) or covariant (exact linear algebra at the seven sampled points; a Monte Carlo fibre average on the explicit realisation agrees). For this trace no single \(G_T\) covers the six polarisations or the five traceless ones, and \(-2\) is not a generalised eigenvalue of the index form at any sampled point, so the mixed-term part of the fixed-state gap vanishes on no traceless polarisation. The trace with equal weight on all fibre harmonics applies when the scale of \(K\) exceeds the fibre gaps, which is the regime of the cited construction. The averaged-frame forms are the trace over the fibre-constant loop modes with projected coefficients. The full trace approaches them when the fibre gaps exceed the scale of \(K\), since intermediate states in the second harmonic are then suppressed in the proper-time integral; this is an argument and is not computed. In that regime the first term of the factorisation has a part with two base derivatives from the fibre flux, the mixed \(S^2\)--\(M\) term of Section~7.1.2 of~\cite{Steinacker2023}, which that work states is not Lorentz invariant a priori and finds subdominant for a scale of \(K\) above the fibre scale, a condition that fails in that regime; this part is not computed here. In the cited construction the mixed term is written with the torsion of a frame on \(M^{3,1}\). Replacing the frame of the level-one amplitudes by its fibre average gives the averaged-frame forms above, and for a fibre-independent torsion, such as that of the background, the two evaluations agree.

These statements are for the Poisson limit, one loop, the content and product backgrounds of the preceding paragraph, the orientation-even mixed term, the level-one amplitudes, the leading symbol at a frozen base point with \(y^i=0\) (other points follow by Lorentz covariance), a formal evaluation with the Lorentzian \(\eta\), and the replicas of Section~\ref{sec:status-B} with the cone in the base. They do not compute the first-term contributions of order \(\LUV^2\), the logarithmic and fibre-flux contributions, the subleading symbol, the interpolation between the two regimes, or the fibre spectrum. They do not construct \(K\) or fix the sign of \(W_R\), derive the replica or the regime from the matrix state, identify \(\bar h\) with the emergent metric of Chapter~\ref{ch:vierbein-emergence}, or bear on Assumption~\ref{ass:lorentzian}. Problems~B and~F remain open and PROGRAMME-CONDITIONAL.
```
(Identical to appH_insert.tex, the authoritative byte-exact copy.)

**Stale passages.** None. The 044 sentence "Its two-derivative density, its values on the six level-one amplitudes and on the cone, and whether those amplitudes source the axial torsion, are not computed; ..." describes that paragraph's scope. The new paragraph opens with "This paragraph supplements the preceding one, in which ... were not computed", the pattern used at merged L2117.

The 044 statement "The first term has no two-derivative part" is in the four-coordinate subsection and remains true. The insert notes that in CP^{1,2} the first term has a fibre-flux part.

**No PRIOR-CLAIM-ERROR.**

## Verification scripts

All are in `proposals/045-cp12-times-K/`, each with a saved `.out.txt`.

- **`cp12_realisation.py`** — copied from 013 (explicit orbit).
- **`s1_lie_poisson_torsion.py`** (~1 min):
  - bracket sign;
  - exact {T, y} and background torsion;
  - realisation fibre basis via the exact invariant quadric;
  - leading symbols δE, δF, δT vs closed forms (12 random points/q/c);
  - Monte Carlo fibre moments.
- **`forms_lib.py`** — exact routines: EH2, scalar/index forms, model S_i, exact fibre moments, CP^{1,2} forms, span tests.
- **`s2_forms_exact.py`** (~40 s):
  - (0) EH2 vs direct curvature;
  - (1) four-coordinate calibration;
  - (2) seven CP^{1,2} cases: gauge invariance, hbar structure, torsion content, pointwise X formula, block structure, averaged-frame exact identities, trace-reading span tests, eigenvalues, (W_R, W_X) solves.
- **`s3_realisation_crosscheck.py`** (~3 min) — independent Lie–Poisson + Monte Carlo (6000 samples) + icosahedral-design exact evaluation on the realisation; basis-invariant eigenvalues compared with s2.
- **`s4_replica_bookkeeping.py`** — c_T, c_A and gaps for both readings.
- **`s5_insert_mechanics.py`** — bytes, balance, refs/labels/cites, anchor, title collision, process language.
- **`edit_insert_r1.py`** — record of the wording edits applied to the insert.
- **`compile_check.py`** — scratch build of the CURRENT working tree outside the repo (pdflatex, bibtex, pdflatex ×2):
  - baseline 321 pages, with insert 323 pages;
  - exit codes 0; 0 undefined references, 0 undefined citations, 0 multiply defined labels;
  - CRLF preserved; scratch removed.

## Decisions Taken

1. **Which reading is "the" one-loop result.** I take the fibre trace (reading II) as the result in the cited construction's regime. The averaged-frame forms are recorded as an exact but conditional route.
   - Reason: the trace of a multiplication operator over fibre harmonics is the fibre average of the symbol.
   - Rejected: presenting the averaged-frame G_A = G_T result as the one-loop outcome. That would overstate.
2. **Einstein reference.** I compare with EH of the fibre-averaged metric (the metric with the rank-6 linear response, merged 2121). I also test the covariant span (any conformal frame), so that conformal-frame choices cannot fake a mismatch.
3. **Trace polarisation.** It is reported separately, as a conformal-sector datum (Problem C), rather than folded into "no single G_T".
4. **Insert wording.** Supplement pattern; no edit to the merged 044 text.

## Milestone assessment

**Routine / bounded result; no milestone claimed.**
- No M1.
- M2 is a weak candidate only. The trace-reading no-go excludes the CP^{1,2}×K level-one route to a single G_T at the leading frozen symbol in the K-dominant regime. But the averaged/heavy-fibre regime and the other avenues remain open, so by the 044 review's standard M2 does not fire.
- No M3, M4 or M5.

## Status-label recommendation

None. B and F remain OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL. The critical-path set is A, B, C, D1, E, F, G-derived, N (Ch17 `sec:ch17-done`; Appendix H agrees).

## Author decision needed

None.

## Remaining open step

For a single matrix-derived Einstein coefficient with G_A = G_T in this rank-6 class:
1. derive the loop fibre spectrum and compute the regime interpolation (avenue 1), including the first-term fibre-flux part;
2. find a regime or mechanism in which the second-harmonic contributions vanish or become covariant;
3. fix the trace polarisation (Problem C);
4. remove the Λ²/log first-term excess (replica selected by the state, Problem A);
5. construct K and fix the sign of W_R;
6. do all of this without Assumption dictionary and with derived signature (Problem E).

## Special instructions for the gatekeeper

- **Must not be asserted:**
  - that G_A = G_T is obtained (it holds only in the averaged-frame reading, on five polarisations, finite parts);
  - that Steinacker's construction is wrong;
  - that the regime correspondence is computed;
  - any G_eff sign;
  - any closure.
- **Re-check:**
  - the trace-of-multiplication-operator argument (SU(2) invariance ⇒ l = 0 component);
  - the EH2 factor (s2 (0));
  - the calibration −4 (s2 (1));
  - the cone values carried from 044;
  - that the trace-reading residuals are not a basis artefact (s3 exact-design column agrees with the model).
- Runtimes: s1 ~1 min, s2 ~40 s, s3 ~3 min.
