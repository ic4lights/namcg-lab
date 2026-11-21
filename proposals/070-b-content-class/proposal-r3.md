# Proposal 070-b-content-class, round 3

**Round 3 is a minimal revision of r2 (review-r2: ACCEPT WITH REQUIRED REVISIONS).** The exact diffs from r2 are:

| # | Where | r2 | r3 |
|---|---|---|---|
| D1 (m-a, required, verbatim) | insert, "Sectors with a scale"; same sentence in the `latex` block below | `For this formal shift the comparison at this content is thus not vacuous only for a split spectrum, where it reduces to the two sums \(\mathsf S_n\) and \(\mathsf S_\kappa\).` | `For this formal shift the comparison at this content is thus, for the periodic gluing, not vacuous only for a split spectrum, where it reduces to the two sums \(\mathsf S_n\) and \(\mathsf S_\kappa\); for the fixed-state replica it keeps the Dirac term for every spectrum.` |
| D2 (m-c, optional, adopted verbatim) | insert, paragraph "At \(N_s=6\), \(n_D=2\)"; same sentence in the `latex` block below | `the family \(L_r\) of the paragraph on covariant variables reduces to \(L_0\)` | `the family \(L_r\) of the paragraph on covariant variables, with \(\kappa_X\) taken over the whole content, reduces to \(L_0\)` |
| D3 (m-b, proposal file only) | Verification scripts, "Earlier S1 failure (m5)", first bullet | "`sp.nsimplify` was applied to exact rationals with large denominators, and returned a surd approximation;" | corrected wording, see that paragraph and Decisions Taken item R3-1 |
| D4 | file names and hashes | `appH_insert_r3.tex`, `apply_build_r2.py`, post `7e9f6760...` (702343 B) | `appH_insert_r4.tex`, `apply_build_r3.py`, post `4ea0ee0f50b0676ee161ff8ebd6620e3bd775ae74ffb1796b07d8a78f9e24b18` (702490 B) |
| D5 | new evidence files | none | `nsimplify_check.py`, `nsimplify_check_output.txt`, `apply_build_r3_output.txt` |

Nothing else changes:
- the anchor is the same;
- the L437 companion edit is the same ("at the end of this section" -> "later in this section");
- the pre hash is the same, `5106f993...`;
- no `\ref`, `\label` or `\cite` is added, and no label changes.

`appH_insert_r3.tex`, `apply_build_r2.py` and their outputs are kept and superseded. D1 and D2 are the only byte differences between `appH_insert_r3.tex` (8612 B) and `appH_insert_r4.tex` (8759 B).

On D1: with a common mass, the fixed-state comparison at (6,2) is `c_A - c_T = 2 f(m^2)`, not 0, so the r2 sentence was too strong for the fixed-state gluing. This matches the massless (6,2) ledger of the same insert (fixed-state gap 2, `s3_content_ledger_output.txt`). D1 restricts the split-spectrum statement to the periodic gluing and records the fixed-state Dirac term.

On D2: `kappa_X` is the content-weighted sum. The clause makes explicit in what sense `kappa_X = 0` holds at (6,2), and hence why `L_r = L_0` there.


## Result

1. **The `n_D = 0` scope of the edge-term question (content identities).** These hold for every content, re-derived and re-checked:
   - `c_A - c_T = 4 kappa_X + n_D`;
   - `c_A^per - c_T = 4 kappa_X`;
   - `(c_A - 1) - c_W(-1) = n_D/2`;
   - `(c_A - 1) - c_T = 3 kappa_X + n_D/2`.

   So "gap = 4 kappa_X", "c_A - 1 = c_W(-1)" and "3 kappa_X remains" hold at `n_D = 0` only. appH already scopes them to `n_D = 0`, so no prior statement is false.

   One addition makes 070 consistent with the integrated 065 text. The difference `c_T - c_W(0) = -4 kappa_X` is the same for every content. For `n_D > 0`, however, the fixed-state `c_A` exceeds `c_W(0)` by the Dirac excess `n_D`, which sits on the area side only. The term that the fixed-state replica needs is therefore `-(4 kappa_X + n_D)`. The "coefficient `-4 kappa_X` required at `n_D = 0`" of the matrix-gauge and nearest-published paragraphs is its value at `n_D = 0`.
2. **At the IKKT content `(N_s, n_D) = (6, 2)`, order Lambda^2.**
   - The tensor side vanishes in every presentation: `c_T = c_T^ext = c_W(r) = 0`, and `L_r = L_0`.
   - The periodic and smooth replicas give `0 = 0`.
   - The only nonzero entry is the fixed-state `c_A = 2`. That is the Dirac excess, so the term needed is `-2`, not a `rho^2 X` term.
   - In this class the comparison is `0 = 0` or `2 != 0`, and it fixes no Newton constant. The `2 != 0` reading is conditional on the gluing hypotheses, which are now named in place.
3. **Sectors with a scale.**
   - For a formal constant-mass shift, both sides are weighted by the same `f(m^2)`. The comparison reduces to `S_n` and `S_kappa`, and periodic equality holds iff `S_kappa = 0`.
   - The integrated product class `M x K` of `sec:status-F` is not of this form. There `W_R` and `W_X` play the roles of `S_n` and `S_kappa`, and the periodic gap `4 W_X` is nonzero. The insert quotes that class with its caveats and adds nothing to it.

This is a bounded, conditional result. Problem B stays OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL.

## Target and status

- **Problem B**, `sec:status-B`, appH L154-528 at the pre-hash below.
  - Ledger label, verbatim (L157-160): "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL. The first-law identity is established, but the stationarity condition for the tensor block is not derived."
  - ch17 L121-137: "*CRITICAL PATH; OPEN.* ... Closure requires fixed-volume variations of the tensor (non-conformal) block from the microscopic action, a specified map `g^(0) -> g`, and no use of an already-existing metric. A conformal-only derivation is a sub-case and leaves B OPEN."
- **Original target.** Derive `delta S_D = 0` at fixed volume for the tensor block from the microscopic action. The sub-question here is the necessary condition `G_A = G_T` of the normalisation paragraph (L287-292).
- **Dependencies.** A (state, gluing), D (local frame rotations), F (induced coefficient, product class).
- **Classification.** PROGRAMME-CONDITIONAL.
- **Discrepancies.** None between ch17 and appH for B.

## Source reading

Digest + targeted reads. `python scripts/make_digest.py --check` printed `DIGEST CURRENT`. No full scan, because no definition, assumption, scope statement or status passage is changed. The companion edit changes only a positional phrase ("at the end of this section" becomes "later in this section").

- Read in full:
  - appH `sec:status-B` L154-531, including the integrated 065 paragraphs L513-528 (Schwinger-Dyson insertion; Nearest published statements);
  - ch17 L110-137;
  - appH `sec:status-F` L2780-2812 (product backgrounds, and the first conjugate-coordinate-times-fuzzy-factor paragraph).
- Read: `review-r1.md`, `proposal-r1.md`, the r2 draft (`appH_insert_r2.tex`, `make_insert_r2.py`, `apply_check_r2.py`).
- No file was unreadable.
- Pre appH: 693736 bytes, sha256 `5106f9938be746607dd0b5fe6ecbf89a2918d795ffad7ee79d9ed7bf972d7681`. This is the working tree with 065 integrated.

## Research and reasoning

### Re-derivation (by hand, then the scripts)

**Sector densities.** From L287 (table), L302 (Dirac: `(4/6) rho R + (1/2) rho^2 X`) and L467 (connection: `(4/6) rho R + rho^2 X`), with weights 1, 1, -2, -1:
- `c_R = N_tot/6`, where `N_tot = N_s + 2 - 4 n_D`;
- `kappa_X = 1 - n_D/2`.

On the `delta rho = 0` modes a term `c rho R` has eigenvalue `-c/4`, and `rho^2 X` acts as `-4 rho R` (L290, L439, L2797). Hence `c_T = c_R - 4 kappa_X`.

**Area side.**
- Periodic gluing: the Dirac value `-2/3` equals its `rho R` coefficient (L302), so `c_A^per = c_R`.
- Fixed-state replica: the antiperiodic Dirac value `+1/3` is `+1` per field above the periodic value, so `c_A = c_R + n_D`.

**Noether coefficient.** `c_W(r) = c_R + kappa_X r` (L439).

**Identities.**
- `c_A - c_T = 4 kappa_X + n_D`.
- `c_A^per - c_T = 4 kappa_X`.
- `(c_A - 1) - c_W(-1) = c_R + n_D - 1 - c_R + kappa_X = n_D - 1 + 1 - n_D/2 = n_D/2`.
- `(c_A - 1) - c_T = 4 kappa_X + n_D - 1 = 3 - n_D = 3 kappa_X + n_D/2`.
- `c_T - c_W(0) = -4 kappa_X` for every content, while `c_A - c_W(0) = n_D`.

**Consistency with 065.** In the covariant-variables and matrix-gauge paragraphs (L496, L507) and in 065 (L520, L527), the required term relative to the fixed-state coefficient is `c_T - c_A`. At `n_D = 0` that is `-4 kappa_X`, as those paragraphs state; at general `n_D` it is `-(4 kappa_X + n_D)`, and at (6,2) it is `-2`.

065's statement that the insertion identity along a compensating rotation or an adjoint flow cannot produce `-4 kappa_X` is scoped to `n_D = 0`. 070 neither repeats it nor extends it: at (6,2) the `-4 kappa_X` part is zero, and the remaining `-2` is an area-side Dirac term about which 065 says nothing.

The two packages do not duplicate each other:
- 065 treats the matrix-integral insertion identity, measure Jacobians and literature;
- 070 treats the content dependence of the Lambda^2 coefficients.

Their only shared object is the phrase "the coefficient `-4 kappa_X` required at `n_D = 0` in the paragraph on the matrix gauge realisation". 070 cites it by naming those paragraphs and does not restate their argument.

**(6,2).** The weighted `a_1` vanishes pointwise (L345), so `c_T = c_T^ext = c_W(r) = 0` and `L_r = L_0` (since `r kappa_X = 0`).
- Uniform contact: `-N_tot/4 = 0` (L422).
- Smooth replica: `c_A^sm = 0` (L317).
- Vector holonomy contact: shifts `c_A` to 1 on `n < 1` and to 3 on `n > 1` (L435: "4 - n_D - alpha_v sigma"; at `n_D = 2`, `sigma = -1` gives 3).
- Dirac holonomy contact: 0 at first order (L422).
- Newton constants: `1/G = c Lambda^2/(2 pi)` (L420), with `c = 2`, gives `1/G_A = Lambda^2/pi`.
- Log order (L382): the gaps `4 - 2n_D`, `4 - n_D`, `2 - n_D` are 0, 2, 0 at `n_D = 2`, and `kappa_C^T = N_tot/120 - kappa_X/3 = 0`. The log coefficient is `proportional to int rho^2 S_4` (L345), with `b_sigma = O(epsilon)` about constant `Theta-bar`, hence `O(epsilon^4)`.

**Mass shift.** `Tr e^{-s(O + m^2)} = e^{-s m^2} Tr e^{-s O}` holds exactly, on the chart and on the cone. Both the Lambda^2 term of the effective action (`int ds s^{-2} e^{-s m^2} a_1`) and the cone term (`int ds s^{-2} e^{-s m^2}` times the flat-cone coefficient) are therefore weighted by
`f(m^2) = Lambda^2 E_2(m^2/Lambda^2) = Lambda^2 - m^2 ln(Lambda^2/m^2) - (1 - gamma_E) m^2 + O(m^4/Lambda^2)`.

The tensor-side `-m^2 ln(Lambda^2/m^2) a_1` term is the curvature part of the change of `a_2` given at L347 (`-m_i^2 a_1^(i)`); this is a consistency check with integrated text.

With ghosts at the connection mass:
- `S_n = N_s f_s + 2 f_v - 4 n_D f_D`;
- `S_kappa = f_v - (n_D/2) f_D`.

For one bosonic and one fermionic mass at (6,2): `S_n = 8(f_b - f_f)` and `S_kappa = f_b - f_f`, so `c_T = -(8/3)(f_b - f_f)` and `c_A^per = (4/3)(f_b - f_f)`.

**Product class (M1).** Checked against L2789-2799. The insert says:
- the first term `s_0^K(v^M - 2 sigma^M)` has no two-derivative part;
- `c_T = W_R/6 - 4 W_X`;
- periodic `c_A = W_R/6`, so the periodic gap is `4 W_X`;
- `W_X < 0` for nonzero flux of K;
- the fixed-state `c_A` is "2 per matrix mode of K at order Lambda^2 ... cutoff-dependent terms ... finite remainders are not computed";
- the mixed term corresponds to the term of Section 6.2 of Steinacker2023;
- the scope is the Poisson limit on M, one loop, K not required to solve the EOM and not constructed, no mixed flux, the orientation-even part, and no sign of `W_R`.

Each of these is verbatim in substance from L2781-2801.

I removed the r2-draft clause "which contain no cubic or mass term on K": no such statement appears in the cited paragraph, so it was unsourced.

### Placement (re-anchoring)

The orchestrator's anchor is the closing sentence of the 065 paragraph "Nearest published statements ...", plus the blank line and the `\section{Problem C ...}` header. It occurs once. Placing 070 there, however, makes one existing phrase stale. L437 (paragraph on the order Lambda^2, "Dragging, regularity, covariance") says the later aether treatments "are recorded in the paragraph on the nearest published statements at the end of this section". After the insert, that paragraph is no longer at the end.

Alternatives, rejected:
- Insert before the SD paragraph (after L511). This breaks the SD paragraph's "disclaimed in the preceding paragraph", which refers to the matrix-gauge paragraph.
- Insert between the SD and Nearest paragraphs. This splits 065's contiguous block, leaving the SD paragraph without its status sentence.

Chosen: keep the orchestrator's anchor and add a two-word companion edit at L437, replacing "at the end of this section" with "later in this section". That phrase occurs once in the manuscript (grep over `chapters/*.tex`).

### Duplication audit (m4 and the smallest-text rule)

Compared with r1 and the r2 draft:
- **Table removed.** Every general-content entry is a formula already stated: `c_T` at L290 and L302; `c_T^ext` at L452; `c_W` at L439; `c_A`, `c_A^per` and `c_A^sm` at L302, L317 and L328. The (6,2) column is now carried in one sentence, and the (6,0) column added nothing used.
- **"Sector data" reduced.** It is now a back-reference to the existing densities with the check description; the content is unchanged.
- **The displayed identity `c_W(r) - c_T = kappa_X(r + 4)` dropped**, since it is stated at L439. It is replaced by the new `(c_A - 1) - c_T = 3 kappa_X + n_D/2`, which is the direct generalisation of "3 kappa_X remains".
- **The first two identities kept in the display**, with the sentence "The first two are the gaps `4 - n_D` and `4 - 2 n_D` of the paragraph on the order Lambda^2", so they are tied to existing text and not presented as new.
- **The frame-rotation non-invariance remark dropped from the (6,2) paragraph.** L448 already says "unless `kappa_X = 0`, that is `n_D = 2`".
- **Log-order clause reduced** to a pointer to L382 and L345, with the m2 wording.

Net new content:
- the fourth and third identities and the `n_D` generalisation of the required term, `-(4 kappa_X + n_D)`;
- the statement that at (6,2) the needed term is `-2` from the Dirac excess and not a `rho^2 X` term;
- the area side of the formal mass shift;
- the comparison pointer to the product class.

Size: 8612 bytes CRLF (r1: 8208 LF; r2 draft: 9783 LF).

### No-go fork (corrected per M1)

**Obstruction.** At (6,2), in the four-coordinate massless Poisson class, there is no nontrivial `G_A = G_T` at order Lambda^2.

| # | Hypothesis | Relaxation | Status |
|---|---|---|---|
| H1 | Four coordinates, no scale | Product `M x K` with a fuzzy factor | **Already begun in `sec:status-F` (L2780ff), not a new edge.** That work gives the periodic gap `4 W_X != 0` and the fixed-state `c_A = 2` per mode plus uncomputed cutoff-dependent parts. The formal mass shift here is a different, simpler class. |
| H2 | One loop, Lambda^2 and log orders | Finite terms; two loops | Not explored. |
| H3 | Poisson limit first | Moyal corrections at the cutoff | Not explored. |
| H4 | Gluing: fixed-state, periodic or smooth | A matrix state selecting the replica or Dirac tip domain | Not explored; belongs to A intersect B. A periodic or smooth replica gives `0 = 0` at Lambda^2 and moves the test to H1. |
| H5 | Yukawa couplings dropped | Keep them off the background | Not explored. |
| H6 | One common proper-time limit | Sector-dependent limits | An input unless derived. |

**Open avenues, ranked** (as in review-r1, which I adopt):
1. The product and conjugate-coordinate classes of `sec:status-F` (L2780ff). The live sub-questions are the first-term cutoff-dependent parts of the fixed-state `c_A`, the scale range, and the construction of K. This must be serialized with the F chain.
2. The replica and Dirac tip domain selected by a matrix state (A intersect B).
3. Moyal corrections at the cutoff.
4. Finite terms and two loops at (6,2).
5. Yukawa couplings off the background.
6. Sector-dependent proper-time limits (an input).

The r1 suggestion of a new edge "B.kk-spectral-sums" is withdrawn.

### Literature

No new source. `DonnellyWall2016` and `Steinacker2023` are existing bib keys (one entry each, checked), used as in L317, L324, L347 and L2789. Their content was not re-fetched and is not independently verified in this package.

## Claim classification

- Sector densities and the eigenvalue `-1/4`: established identity at sampled jets and modes (exact arithmetic; not a general proof). They restate integrated values.
- The four content identities, `c_T - c_W(0) = -4 kappa_X`, and the required term `-(4 kappa_X + n_D)`: established algebra, given the sector values and replica coefficients.
- `c_A` values per replica, and the holonomy and Kabat contacts: conditional (inherited replica prescriptions, tip domain, quasi-free state; the Kabat value is an input).
- `1/G_A = Lambda^2/pi` against `1/G_T = 0`: conditional (gluing hypotheses named in place; regulator dependent).
- The log-order gaps 0, 2, 0 and `S_4` at quadratic order: conditional (sampled-jet identities of L345 and L382).
- Mass-weighted formulas: conditional (formal shift, no gauge-invariant mass term).
- Product-class statements: quoted from `sec:status-F` with its hypotheses; nothing added.
- State, gluing and modular Hamiltonian: unresolved (Problem A).

## Proposed changes

**File:** `chapters/appH-microscopic-proofs.tex` only. There are two edits; nothing else is removed.

**Edit 1 (insert).** Immediately before `\section{Problem C: conformal mode and Cassini}`, at the end of `sec:status-B`.

- Anchor (occurs once; checked by `apply_build_r3.py`): the closing sentences of the paragraph "Nearest published statements and the reduced-action charge mechanism", then CRLF CRLF, then the Problem C header.

> These identifications record what the published mechanisms do and do not supply for Problem~B; no result is imported into the matrix theory. Problems~B and~D remain open and PROGRAMME-CONDITIONAL.
>
> \section{Problem C: conformal mode and Cassini}

- The insert bytes are `proposals/070-b-content-class/appH_insert_r4.tex`: CRLF, UTF-8 without BOM, ending in one blank line. The existing blank line after the anchor sentence is kept.
- The insert adds one `\ref` (`sec:status-F`, label exists once) and no `\label`. It cites `DonnellyWall2016` and `Steinacker2023` and uses `\LUV` (defined in `namcg-book7.tex`).
- It has one status sentence, "Problem~B stays open and PROGRAMME-CONDITIONAL.". The adjacent preceding paragraph ends "Problems~B and~D remain open and PROGRAMME-CONDITIONAL.", so the two do not repeat each other.

```latex
\paragraph{Content class of the order-\(\LUV^2\) comparison: the gaps at general content, the ledger at \(N_s=6\), \(n_D=2\) and sectors with a scale (conditional; not closure).}
Keep the setting of the paragraphs on the normalisation of the tensor kinetic term, on fermionic content and on the order \(\Lambda^2\): four matrix coordinates, the Poisson limit taken before the one common proper-time limit, the Euclidean section, \(\alpha=1\), one loop, the \(\LUV^2\) term, \(N_s\) scalar components, the connection with its ghosts and \(n_D\) Dirac fields with the Yukawa couplings dropped, and the two modes with \(\delta\rho=0\) about a constant \(\bar\Theta\). No state of the matrix model enters: the replicas are the gluing prescriptions of the preceding paragraphs for the Poisson-limit operators on the cover of the matrix chart, and no limit of finite matrices is taken.

\emph{Gaps at general content.} The sector densities \(\tfrac n6\rho R[g_\rho]+\kappa\,\rho^2X\), with \((n,\kappa)=(1,0)\) for a scalar component and a ghost, \((4,1)\) for the connection and \((4,\tfrac12)\) for a Dirac field, and the eigenvalue \(-\tfrac14\) of \(\rho R[g_\rho]\) relative to \(\rho^2X\) on the modes with \(\delta\rho=0\), are those of the preceding paragraphs (checked from \(\mathcal O_s\), \(\mathcal O_v\), \(\mathcal O_f\) at four random two-jets of a closed \(\omega\) and on four random modes, exact arithmetic). With \(c_R=N_{\mathrm{tot}}/6\), \(c_T=c_R-4\kappa_X\), \(c_W(r)=c_R+\kappa_Xr\) and the area coefficients \(c_A^{\mathrm{per}}=c_R\) of the unrotated periodic gluing and \(c_A=c_R+n_D\) of the fixed-state replica, for every \(N_s\) and \(n_D\)
\[
  c_A-c_T=4\kappa_X+n_D,\qquad c_A^{\mathrm{per}}-c_T=4\kappa_X,\qquad (c_A-1)-c_W(-1)=\tfrac12n_D,\qquad (c_A-1)-c_T=3\kappa_X+\tfrac12n_D .
\]
The first two are the gaps \(4-n_D\) and \(4-2n_D\) of the paragraph on the order \(\Lambda^2\). The identification of the fixed-state gap with \(4\kappa_X\), the relation \(c_A-1=c_W(-1)\) and the remainder \(3\kappa_X\) of the paragraphs on covariant variables and on the matrix gauge realisation hold at \(n_D=0\), as stated there, and at no other \(n_D\). The difference \(c_T-c_W(0)=-4\kappa_X\) does not depend on \(n_D\), but for \(n_D>0\) the fixed-state coefficient exceeds \(c_W(0)\) by the Dirac excess \(n_D\), which lies on the area side only; the term that the fixed-state replica needs is then \(-(4\kappa_X+n_D)\), and the coefficient \(-4\kappa_X\) required at \(n_D=0\) in the paragraphs on the matrix gauge realisation and on the nearest published statements is its value at \(n_D=0\).

\emph{At \(N_s=6\), \(n_D=2\).} Here \(c_R=\kappa_X=0\) and the weighted \(a_1\) density vanishes pointwise (paragraph on the next order), so \(c_T=c_T^{\mathrm{ext}}=c_W(r)=0\) for every \(r\): the family \(L_r\) of the paragraph on covariant variables, with \(\kappa_X\) taken over the whole content, reduces to \(L_0\), and the presentation dependence of the Noether coefficient and the coefficient \(-4\kappa_X\) vanish. The periodic and smooth replicas give \(0=0\), and the uniform contact \(-N_{\mathrm{tot}}/4\) is zero. The one nonvanishing entry is the fixed-state coefficient \(c_A=n_D=2\), the Dirac excess alone, so the term that the fixed-state replica needs is \(-2\) and is not a term in \(\rho^2X\). The Dirac holonomy contact vanishes at first order, and the vector holonomy contact of modulus \(1\) changes \(c_A\) to \(1\) on \(n<1\), the value \(-1\) being that of the edge-mode term of~\cite{DonnellyWall2016} for a Maxwell field if the state carries that sector (an input, not a prescription of this class), and to \(3\) on \(n>1\); no contact of the paragraph on the order \(\Lambda^2\) removes it. At logarithmic order, about a constant self-dual or anti-self-dual \(\bar\Theta\) on the \(n<1\) branch, the gaps of the coefficient of \(W\) of the paragraph on the content dependence of the logarithmic comparison are \(0\), \(2\), \(0\) at \(n_D=2\), with \(\kappa_C^T=0\), and the logarithmic coefficient \(\propto\int\rho^2\mathcal S_4\) of the paragraph on the next order, quartic in \(b_\sigma\), vanishes at quadratic order about a constant \(\bar\Theta\), given the sampled-jet identity of that paragraph. In the units \(1/G=c\,\LUV^2/2\pi\) of the paragraph on the order \(\Lambda^2\), the requirement \(G_A=G_T\) of the paragraph on the normalisation is, at this content and order, the single condition \(c_A=0\) with \(1/G_T=0\): for the fixed-state replica, which is the trace of \(\rho^n\) only under the hypotheses of the paragraph on fermion replica gluing (a quasi-free state of the Poisson-limit fermions with rotational modular flow, the less singular extension and a unique continuation from integer \(n\)), \(1/G_A=\LUV^2/\pi\) while \(1/G_T=0\), and for the periodic and smooth replicas both vanish. In this class the comparison at this content is an equality of vanishing coefficients or the inequality \(2\neq0\), and in neither case does it determine a Newton constant.

\emph{Sectors with a scale.} Let each sector carry a constant mass, \(\mathcal O_i\to\mathcal O_i+m_i^2\), the formal shift of the paragraph on the next order, with the ghosts at the mass of the connection. The heat trace of the sector is multiplied by \(e^{-sm_i^2}\) on the chart and on the cover alike, so both sides are weighted by \(f(m^2)=\int_{\LUV^{-2}}^\infty\mathrm ds\,s^{-2}e^{-sm^2}=\LUV^2-m^2\ln(\LUV^2/m^2)-(1-\gamma_{\mathrm E})m^2+O(m^4/\LUV^2)\), with \(\gamma_{\mathrm E}\) the Euler constant; on the tensor side the term in \(m^2\ln\LUV\) is the curvature part of the change of \(a_2\) stated there. With \(\mathsf S_n=\sum_iw_in_if(m_i^2)\) and \(\mathsf S_\kappa=\sum_iw_i\kappa_if(m_i^2)\), in units in which the massless value of \(f\) is \(1\),
\[
  c_T=\tfrac16\mathsf S_n-4\mathsf S_\kappa,\qquad c_A^{\mathrm{per}}=\tfrac16\mathsf S_n,\qquad c_A=\tfrac16\mathsf S_n+\sum_{\text{Dirac}}f(m_D^2),\qquad c_A^{\mathrm{per}}-c_T=4\mathsf S_\kappa .
\]
At \(N_s=6\), \(n_D=2\) the \(\LUV^2\) parts of \(\mathsf S_n\) and \(\mathsf S_\kappa\) cancel and both sums are of order \(m^2\ln\LUV\). The tensor coefficient is nonzero only if \(\mathsf S_n\neq24\,\mathsf S_\kappa\), and for the periodic gluing it equals the area coefficient if and only if \(\mathsf S_\kappa=0\), a condition on the connection and Dirac spectra alone; the fixed-state replica keeps in addition the Dirac term, of order \(\LUV^2\). For one bosonic mass and one fermionic mass \(c_T=-\tfrac83(f_b-f_f)\) and \(c_A^{\mathrm{per}}=\tfrac43(f_b-f_f)\), of opposite sign. For this formal shift the comparison at this content is thus, for the periodic gluing, not vacuous only for a split spectrum, where it reduces to the two sums \(\mathsf S_n\) and \(\mathsf S_\kappa\); for the fixed-state replica it keeps the Dirac term for every spectrum. The product backgrounds \(M\times K\) of the paragraph on product backgrounds in Section~\ref{sec:status-F} are not of this form: there the scalar operator of \(K\) is common to all species, the term that would carry \(\mathsf S_\kappa\) has no two-derivative part, and the comparison is \(c_T=\tfrac16W_R-4W_X\) against \(c_A^{\mathrm{per}}=\tfrac16W_R\), with \(W_X\) from the mixed term, which that paragraph relates to a term of Section~6.2 of~\cite{Steinacker2023}, so that \(W_R\) and \(W_X\) take the places of \(\mathsf S_n\) and \(\mathsf S_\kappa\) and the periodic gap \(4W_X\) is nonzero for a nonzero flux of \(K\); the fixed-state replica there keeps the value \(c_A=2\) of this content for each matrix mode of \(K\) at order \(\LUV^2\), with cutoff-dependent terms whose finite remainders are not computed there. Those statements are for the Poisson limit on \(M\), one loop, a fuzzy space \(K\) that is not constructed and not required to solve the equations of motion, product backgrounds without mixed flux, the orientation-even part of the mixed term and the replicas of this section, and they fix no sign of \(W_R\).

These statements are for the Poisson limit taken first, four matrix coordinates, the Euclidean section, one loop, \(\alpha=1\), one common proper-time limit, the contents stated with the Yukawa couplings dropped, the replicas and contacts of the preceding paragraphs with their hypotheses, the two modes with \(\delta\rho=0\), and formal constant masses without a gauge-invariant mass term. They supply no state, modular Hamiltonian or gluing of the matrix model, do not derive the content, treat no finite terms, Moyal corrections or Kaluza--Klein tower, add nothing to the statements quoted from Section~\ref{sec:status-F}, and give no value or sign of \(G_{\mathrm{eff}}\). Problem~B stays open and PROGRAMME-CONDITIONAL.
```

**Edit 2 (companion; position wording only).** At appH L437, in the paragraph "Order \(\Lambda^2\): contacts, vector holonomy ...", sub-paragraph "Dragging, regularity, covariance". The phrase occurs once.

- Replace: `in the paragraph on the nearest published statements at the end of this section)`
- by: `in the paragraph on the nearest published statements later in this section)`

All other text of that sentence stays.

**Stale passages elsewhere.** None in the manuscript; the `n_D = 0` statements of L481-511 are correctly scoped to `n_D = 0`. Outside the manuscript (not mine to edit), the frontier edge `B.matrix-state-edge-sector` should carry "(n_D = 0 only; at the IKKT content the required term is the Dirac excess -2, the -4 kappa_X part is 0)". It should point at `sec:status-F` L2780ff for classes with a scale.

## Verification scripts

All in `C:\Users\redgi\Projects\namcg-lab\proposals\070-b-content-class\`. Run from the repository root.

| Command | Checks | Expected invariant output |
|---|---|---|
| `python -I proposals/070-b-content-class/s1_weighted_a1.py` (about 2 min) | `E_s = e`, `tr E_v = 4e - X`, `tr E_f = 4e - X/2` at four random two-jets (exact); weighted sum | all residuals `0`; `weighted a_1 at (6,2): 0`; `S1 PASS`. r2 output `s1_weighted_a1_output_r2.txt` is byte-identical to `s1_weighted_a1_output.txt` (timing lines stripped) |
| `python -I proposals/070-b-content-class/s2_mode_ratio.py` | second-order averages on `delta rho = 0` modes | `ratio = -1/4` four times; generic modes differ; `S2 PASS`. r2 output identical |
| `python -I proposals/070-b-content-class/s3_content_ledger.py` | cone constants, the four identities, (6,0)/(6,2) values, mass sums, `f(m^2)` expansion | `(c_A^fs - 1) - c_W(-1) = n_D/2`; `(c_A^fs - 1) - c_T - 3 kappa_X = n_D/2`; (6,2) gaps periodic 0, fixed-state 2, holonomy 1/3, smooth 0; `ratio c_A^per/c_T = -1/2`; `f` residuals `-5.0e-7`, `-4.5e-8`. r2 output identical |
| `python -I proposals/070-b-content-class/apply_build_r3.py` | pre hash, unique anchor, unique companion phrase, CRLF, no BOM, refs/labels/cites, balance, process words, one status sentence differing from the adjacent one, no duplicate labels, post hash | `pre appH: 693736 5106f993...7681`; `post appH: 702490 4ea0ee0f50b0676ee161ff8ebd6620e3bd775ae74ffb1796b07d8a78f9e24b18`; `APPLY/BUILD R3 PASS` |
| `python -I proposals/070-b-content-class/nsimplify_check.py` | m-b: `nsimplify` on exact `Rational`s in sympy 1.14.0 | `4093/72 ... identity: False`; `81811/27648 ... identity: False`; `1/3`, `-26/81` identity True; integer short-circuit True (saved: `nsimplify_check_output.txt`) |
| `python -I proposals/070-b-content-class/apply_build_r3.py <dir outside repo>` | as above, plus a copy of the build inputs with the applied appH and two `pdflatex` passes | `pdflatex pass 1/2` PASS; `no undefined/multiply-defined references or citations (0)`; `pages: 401`; `APPLY/BUILD R3 PASS` (saved: `apply_build_r3_output.txt`) |

The build copy is left in the given directory and nothing is deleted. In this round it was the session scratchpad, `C:\Users\redgi\AppData\Local\Temp\claude\...\scratchpad\070-r3-build-1795102124`. The repository PDF and working tree were not touched by the build.

**Earlier S1 failure (m5).** The first committed `s1_weighted_a1_output.txt` (commit 20741cb) ended in `S1 FAIL`: trial 0, residual (c). There were two causes:
- `sp.nsimplify` was applied to exact `Rational` values at the base point (in `at0`, and entrywise in `endo`; the Dirac entries are also non-`Rational` `Add` expressions containing `I`). In the installed sympy 1.14.0, `nsimplify` short-circuits only integers. An exact `Rational` goes through the floating-point identification step and can come back as a different closed form. For example, `nsimplify(Rational(81811, 27648))` returns `7*2**(557/607)*3**(556/607)*5**(357/607)*7**(201/607)/60`, which differs by about 1.2e-17. `nsimplify(Rational(4093, 72))` returns a similar product of fractional prime powers. The denominators are not large. This is what broke the exact residuals (`nsimplify_check.py`);
- the monomial list came from an unordered set, so the random jets were not reproducible.

The script was changed (commit 7efe824) to sort the monomials with `default_sort_key` and to use `simplify`/`expand` instead of `nsimplify`. It now passes, and the r2 re-run under `python -I` reproduces the PASS output byte-for-byte.

The integrator must re-run `apply_build_r3.py` on the tree it integrates into. If appH has moved, the pre-hash check fails by design, and the anchor and companion-phrase checks show whether the text is still applicable.

`make_insert_r2.py`, `appH_insert_r2.tex` and `apply_check_r2.py` were an intermediate draft against the pre-065 tree (old anchor, pre hash `c2dac013...`). They are superseded by `appH_insert_r4.tex` and `apply_build_r3.py` (r2's `appH_insert_r3.tex` and `apply_build_r2.py` are likewise superseded) and are not for integration.

## Decisions Taken

1. **Placement at the orchestrator's anchor plus a two-word companion edit.** The reasons and the rejected placements are given under "Placement" above. Moving the insert to avoid the companion edit would break either 065's "preceding paragraph" reference or its one-status-sentence block.
2. **Consolidated table dropped** (smallest text; m4). Every general entry restates integrated formulas, and the (6,2) values fit in one sentence.
3. **The `n_D` generalisation of the required term is stated as `-(4 kappa_X + n_D)`, with `-4 kappa_X` as its value at `n_D = 0`.** This keeps 065's wording ("required at `n_D = 0`") correct and visible, and it shows that at (6,2) the missing ingredient is an area-side Dirac term of `-2`, not a `rho^2 X` edge term. This points the B search at the Dirac tip domain and gluing (A intersect B) rather than at the `r`-family. Rejected: rewording 065's text, which is integrated and correct as scoped.
4. **The 065 SD result is cited by naming its paragraphs, not restated.** 070 does not claim that the SD obstruction extends to the Dirac term.
5. **The unsourced clause "no cubic or mass term on K" was removed** from the product-class sentence.
6. **The L382/L384 tension** ("not the trace of the n-th power of one state" against the L307 hypotheses) is pre-existing wording, as the reviewer noted. The insert quotes the hypotheses and does not sharpen the tension. It is recorded under "Remaining open step" for a later package.
7. **"B.kk-spectral-sums" is withdrawn** as a new edge (M1). The route is the existing F-chain material at L2780ff.

**R3-1 (m-b).** I checked the gatekeeper's proposed mechanism, and it does not hold for the installed sympy. In sympy 1.14.0, `nsimplify(Rational)` is not the identity: the function returns early only for integers (`as_int`). I verified this in three ways:
- I read `inspect.getsource(sympy.nsimplify)`.
- `nsimplify_check.py` shows the behaviour directly.
- I re-ran the `s1_weighted_a1.py` of commit 20741cb (trial 0 only; scratch copy outside the repository) with `nsimplify` instrumented, under `PYTHONHASHSEED` = 1..6.

In the instrumented run the arguments were of three types: `Zero` (65), `Rational` (19) and `Add` (8, the complex Dirac entries). Under seeds 5 and 6, a `Rational` argument (4093/72 and 81811/27648) was returned as a surd. Under seed 6 this produced nonzero residuals (b) and (c). Every `Add` argument came back unchanged in all six runs.

So in the failures I reproduced, `nsimplify` was applied to an exact `Rational`, not to a non-`Rational` intermediate. I did not adopt the wording "applied to a non-Rational intermediate", because my check contradicts it. D3 instead removes the actual error in r2, the claim "large denominators", and names the mechanism: this sympy version does not short-circuit non-integer `Rational`s. The seed dependence matches the second cause already listed, the unordered monomial set. The original FAIL in 20741cb was not re-run bit-for-bit, because its hash seed is unknown. This is a correction to the proposal file only and has no manuscript effect.

**R3-2 (m-c).** Adopted verbatim. It claims nothing beyond r2 and makes explicit which `kappa_X` vanishes.

## Milestone assessment

Routine. No critical-path step is derived. The package records a scope statement and a bounded obstruction at the IKKT content, and it redirects the B edge-term question: at (6,2) the missing term is the Dirac excess on the area side.

## Status-label recommendation

At the full-GR / matrix-derived scope, ch17 and appH give the critical-path set A, B, C, D1, E, F, G-derived and N. No label is affected. B stays OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL.

## Author decision needed

None.

## Remaining open step

For the original target of B:
- `delta S_D = 0` at fixed volume for the tensor block from the microscopic action;
- a state, modular Hamiltonian and gluing (Problem A), which at (6,2) decides between `0 = 0` and the Dirac term `-2`;
- the map from scaffold to emergent metric;
- a nonzero induced `G_T` at the actual content, in a class with a scale (`sec:status-F` product and conjugate-coordinate classes; Problem F);
- in that class, the equality of `c_A` with the induced coefficient, including the uncomputed first-term cutoff-dependent parts of the fixed-state `c_A`.

Separately, the wording tension between L307 (fixed-state Dirac gluing as `Tr rho^n` under hypotheses) and L384 ("hybrid ... not the trace of the n-th power of one state") should be resolved in a later package.

## Special instructions for the gatekeeper

**r1 findings and how each was addressed.** All seven are addressed.

| Finding | Action in r2 |
|---|---|
| **M1** (major): "is not examined" contradicted `sec:status-F` | Both closing sentences replaced by a quotation of the product-class comparison (L2780-2801) with its caveats; one `\ref{sec:status-F}`. Fork row H1 and the avenue ranking corrected; "B.kk-spectral-sums" withdrawn. The unsourced "no cubic or mass term on K" clause from the r2 draft removed. |
| **M2** (major): `Tr rho^n` without its hypotheses | The gatekeeper's snippet adopted verbatim: quasi-free state, rotational modular flow, less singular extension, unique continuation. |
| **m1**: Donnelly-Wall apposition | Attached to the `n < 1` value only, as "the value -1 ... (an input, not a prescription of this class)"; `n > 1` gives 3 as the holonomy branch. |
| **m2**: log-order wording | "vanishes at quadratic order about a constant `Theta-bar`, given the sampled-jet identity of that paragraph". The W-gap statement is scoped to "a constant self-dual or anti-self-dual `Theta-bar` on the `n < 1` branch". "Same pattern" was removed; the clause now points to L382, where the remark that the completed gap has no Lambda^2 counterpart already appears. |
| **m3**: negative half attributed to Steinacker2023 | Removed. The citation now says only that the product-class paragraph relates the mixed term to a term of Section 6.2 of Steinacker2023. |
| **m4**: duplication | Decomposition sentence, table, `c_W - c_T` identity and frame-rotation remark removed or turned into back-references (see the duplication audit). |
| **m5**: S1 FAIL disclosure, stale hash | Disclosed above. New pre and post hashes are for the 065-integrated tree, and the integrator re-runs the script. |

Orchestrator items:
- **Re-anchor:** done.
- **065 consistency:** stated (`-(4 kappa_X + n_D)`, with `-4 kappa_X` its value at `n_D = 0`).
- **No duplication with 065:** checked.
- **Adjacent status sentences:** they differ. The script checks this.

**review-r2 findings.**
- m-a: applied verbatim (D1).
- m-c: applied verbatim (D2).
- m-b: the wording is corrected (D3), but by a different mechanism than the one in the review; R3-1 gives the evidence. Please re-run `nsimplify_check.py`.

Post hash: `4ea0ee0f50b0676ee161ff8ebd6620e3bd775ae74ffb1796b07d8a78f9e24b18` (702490 B); 401 pp; 0 undefined. The ordinal-65 full scan is still owed.

**Open count (r1 to r2).** r1 had 0 blocking and 2 major (M1, M2) open, plus 5 minor. After r2 all are addressed, and the researcher-side count is 0 blocking, 0 major and 0 minor open. The ordinal-65 full scan is still owed by the gatekeeper before a plain ACCEPT.

**Please re-check:**
- `(c_A - 1) - c_T = 3 kappa_X + n_D/2` and the required term `-(4 kappa_X + n_D)` against L496, L507 and L520;
- the claim that the companion phrase is the only positional reference made stale by the insert (grep `end of this section`);
- that every product-class quotation matches L2780-2801;
- the build output (401 pages, 0 undefined).

**Must not be asserted:**
- that (6,2) closes or excludes B beyond the stated class;
- that the SD obstruction of 065 covers the Dirac term;
- any value or sign of `G_eff`;
- that the formal mass shift describes the K tower.
