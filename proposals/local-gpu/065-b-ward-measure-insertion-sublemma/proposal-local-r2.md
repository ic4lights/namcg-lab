# Proposal 065-b-ward-measure-insertion-sublemma, local round 2

Local revision of the gpu-accepted package 065 (gpu `proposal-r2.md` / `review-r2.md`, verdict ACCEPT), answering the
local re-review `proposals/local-gpu/_local-review/group2-B-C-D1.md`, section 065 (AWRR, minors m1-m5 only). The gpu
numbering is not this branch's numbering. Manuscript-text changes against the gpu `insert-r2.tex` are exactly the five
required minors plus one softening (s1) of the negative survey sentence that the local review flagged as not
independently verified beyond the abstracts.

## Result

Unchanged in substance from the accepted gpu round; all central identities re-derived and re-checked.

1. **Measure identity (established, finite N).** For `Z_n(eps) = ∫ j_eps e^{-S_{E,eps}}`,
   `∂_eps ln Z_n = -<I_n>_n + <∂_eps ln j_eps>_n` with `I_n = ∂_eps S_{E,n}`.
2. **Null directions (established).** Divergence-free (unimodular) field redefinitions leave every `Z_n` invariant,
   so `<I_n>_n = <∂_eps ln j_eps>_n = 0`. The compensating rotation has `tr B = 0` (B is eta-antisymmetric, both
   signatures), so `(det e^{tB})^{N^2} = 1`, and every adjoint flow has `tr ad_Lambda = 0`. Hence the coefficient
   `-4 kappa_X` required at `n_D = 0` in the paragraph on the matrix gauge realisation cannot come from the insertion
   identity along these flows.
3. **Gaussian conical-contact obstruction (conditional on the class).** For `A_n = A_1 + (1/n - n) P + eps B`,
   `∂_eps S_D = Tr(G_1 B G_1 P) - 1/2 Tr(G_1 B)`, `G_1 = A_1^{-1}`. For `P != A_1/2` this is nonzero for generic `B`
   and vanishes only on a codimension-one hyperplane; at `P = A_1/2` it vanishes identically, which is why the m5
   qualifier is needed.
4. **Fork probe (new in this round, proposal text only).** If "fixed volume" is modelled inside the Gaussian class as
   `Tr(G_1 B) = 0`, then stationarity for every such `B` holds if and only if `P = lambda A_1`. A tip contact
   supported at the branch locus cannot satisfy this, so in this class the missing ingredient cannot be a localized
   Gaussian contact. It must sit in a non-Gaussian, state-dependent or measure-dependent contact (see the avenue
   ranking).

Problem B is not closed. No label changes.

## Target and status

- **Problem B.** appH L157-160, verbatim: "Status: OPEN. Priority: CRITICAL PATH. Completion: PROGRAMME-CONDITIONAL.
  The first-law identity is established, but the stationarity condition for the tensor block is not derived."
- **ch17 L121-137.** "*CRITICAL PATH; OPEN.*" Derive `delta S_D = 0` at fixed volume as a Ward identity of
  `eq:Smicro`, or of `eq:Smatrix` after Problem A, for the non-conformal tensor block, with a specified map
  `g^(0) -> g` and no use of an existing metric.
- **ch17 L661 and L704.** These list B in the critical-path sequence and in the finished-derivation criterion.
- **No discrepancy** between appH and ch17.
- **Problem D**, named in the closing sentence: appH ledger status OPEN / CRITICAL PATH, unchanged and not touched.
- **Classification:** PROGRAMME-CONDITIONAL. The sub-lemma is a bounded obstruction, not a derivation of the target.
- **Critical-path set** (ch17 and CLAUDE.md, re-checked): A, B, C, D1, E, F, G-derived and N.

## Source reading

- **Mode:** digest plus targeted reads. `python scripts/make_digest.py --check` gave `DIGEST CURRENT`, with
  `dirty-chapters: yes` (the working tree carries uncommitted, previously accepted integrations).
- **Not a full scan.** The insert adds two conditional paragraphs and changes no definition, assumption, scope or
  status passage, so no full scan is required (3(c) does not apply). The digest condition 3(d)
  (`dirty-chapters: yes`) was handled by reading the whole live Problem B section of the current tree.
- **Read in full:**
  - appH L154-514: the whole Problem B section of the live tree, sha256 `4d6d58cf…`, 686,297 B, 3522 CRLF;
  - ch17 L60-80, L119-138, L650-680, L700-710;
  - ch03 L136-150 (`eq:Smatrix`).
- **Reference copy:** `scratch/integrator-backup/gpu-import-full/chapters/appH-microscopic-proofs.tex` L506-519.
  It is byte-identical to the gpu `insert-r2.tex` (LF-normalised comparison, 6666 chars each).
- **Also read:**
  - the gpu `proposal-r2.md` and `review-r2.md`;
  - the local review section 065;
  - local `proposals/070-b-content-class/`: `proposal-r1.md` (anchor section), `review-r1.md`, `appH_insert_r2.tex`,
    `apply_check_r2_output.txt`.
- **No file was unreadable.**

## Research and reasoning

**R1. Measure identity.**
- Differentiate `ln ∫ j_eps e^{-S_eps}` under the integral: `∂ ln Z = <∂ ln j> - <∂ S>`.
- `derive_local_r2.py` checks this two ways:
  - L1a: a non-Gaussian two-variable integral with a nontrivial Jacobian, using quadrature with a 5-point
    derivative; residual about 2e-13;
  - L1b: exactly for a Gaussian.
- Check 1 of `derive_ward_r1.py` (re-run) agrees.

**R2. Null directions.**
- If `x -> phi_eps(x)` is a field redefinition with `det D phi_eps = 1`, change variables: `Z(eps) = Z(0)`. Then the
  identity gives `<I> = <∂ ln j>`, and both vanish when `j = 1`.
- L2a checks this numerically for a quartic action not invariant under the flows. Three traceless flows (diagonal,
  rotation, boost-type) give `d ln Z = 0` to 1e-12. A non-unimodular control `diag(1,0)` gives `-1 = -tr B`.
- L2b: `B = eta^{-1} Omega` with `Omega` antisymmetric gives `tr B = 0` for both signatures.
- L2c: `ad_Lambda = I ⊗ Lambda - Lambda^T ⊗ I` gives `tr = N tr Lambda - N tr Lambda = 0` for random complex
  `Lambda`, N = 2..5, and acts as `[Lambda, ·]`.

**R3. Conical-contact formula.**
- Take `ln Z_n = -1/2 ln det A_n + const`, `W_n = ln Z_n - n ln Z_1`, `S_D = (1 - n∂_n) W_n|_{n=1}`.
- Then `∂_eps W_n = -1/2 Tr(G_n B) + n/2 Tr(G_1 B)`. At `n = 1`, `(1 - n∂_n)` gives
  `1/2 ∂_n Tr(G_n B)|_1 - 1/2 Tr(G_1 B)`.
- `∂_n G_n = -G_n (∂_n A_n) G_n` and `c'(1) = -2` for `c(n) = 1/n - n` give `∂_n Tr(G_n B)|_1 = 2 Tr(G_1 P G_1 B)`.
- Hence `∂_eps S_D = Tr(G_1 P G_1 B) - 1/2 Tr(G_1 B)`. This equals the form `∂_n <I_n>|_1 - <I_1>_1` of appH L234-238
  with `<I_n> = 1/2 Tr(B G_n)`.
- Exact rational checks: L3a and L3b on a random 4×4 block, and Check 4 of `derive_ward_r1.py`.

**R4. The m5 qualifier.**
- `Tr(G_1 B) = Tr(G_1 B G_1 A_1)`, so `∂_eps S_D = 1/2 Tr(B K)` with `K = G_1 (2P - A_1) G_1` (L3f).
- The map `B -> Tr(BK)` on symmetric `B` is the zero functional iff `K = 0`, i.e. iff `P = A_1/2`.
- So the hyperplane statement and the "nonzero for generic B" statement both need `P != A_1/2`. L3d confirms that
  the derivative vanishes for every `B` at `P = A_1/2`.

**R5. The m4 wording and local 070.**
- From appH L302 and L420: `c_R = N_tot/6`, `kappa_X = 1 - n_D/2`, `c_T = c_R - 4 kappa_X`, and the fixed-state
  `c_A = c_R + n_D`.
- So `c_A - c_T = 4 kappa_X + n_D` (L4a). It equals `4 kappa_X` iff `n_D = 0` (L4b).
- The paragraphs on covariant variables (L496) and on the matrix gauge realisation (L501, L507) are stated at
  `n_D = 0`, where `-4 kappa_X = -4` (L4d).
- At the IKKT content (6,2), `-4 kappa_X = 0` and `c_T = 0`. The fixed-state `c_A = 2` remains (L4c), which is the
  070 ledger: 0 = 0 for the periodic and smooth replicas, and `2 != 0` for the fixed-state one.
- The qualifier "required at `n_D = 0`" therefore states the scope of the `-4 kappa_X` requirement correctly. Without
  it, a reader at (6,2) would read a vanishing requirement as the whole gap, whereas the fixed-state gap there is
  the Dirac excess `n_D = 2`. 065's null-direction result is content-independent for the bosonic flat measure, so
  it is consistent with 070 at every content.

**R6. Literature, checked against abstracts.**
- Saved arXiv API capture (`citecheck_arxiv.xml`) and live arXiv abstract pages for 2602.02683 and 2606.27437,
  fetched 2026-11-19.
- **Craps et al. 2602.02683** (title, authors as in the bib). The abstract states that "the nonlocal transformation
  induced by the leg-pole factor that relates the target space tachyon and the matrix model collective excitations
  cannot account for the area-like term", with a comment on non-singlet sectors. This supports the m1 wording; the
  original "no singlet-sector mechanism" over-generalised.
- **Arata, Ismail, Liberati, Martin, Mattingly, Neri 2606.27437.** The abstract states: "In the static, spherically
  symmetric, asymptotically AdS sector with c_14=0 … a previously unidentified symmetry of the reduced action,
  generated by … δu^a = f a^a, where a^a is the aether acceleration and f obeys an elliptic constraint. We derive the
  associated current and charge." This supports the m2 wording. "Genuine local symmetry" and "elliptic gauge-fixed
  action" are not in the abstract, so they are removed.
- **Other entries, checked against abstracts:**
  - TsuchiyaYamashiro2022: qualitative agreement with the area;
  - KawamotoKuroki2021: momentum-space entanglement on fuzzy spheres;
  - AlloucheDou2026: the interaction correction has an extensive bulk contribution and does not obey a pure area
    law;
  - ChoudhuryLaurenzano2024: black 0-brane and its Hawking radiation in BFSS;
  - JacobsonVisser2019 and Svesko2019: causal-diamond first law and entanglement equilibrium in a given metric;
  - JensenSorceSperanza2023: type II algebra and "a version of Jacobson's entanglement equilibrium hypothesis",
    relying on states "whose modular flow is geometric";
  - ArataLiberatiNeri2026: "irreducible entropic AEther contribution" in the horizon charge of stationary black
    holes.
  - EynardOrantin2009: DOI record in `citecheck_eo.json`. It is cited for the loop equations, which is standard.
- **Not independently verified beyond abstracts:** the negative survey claim. The manuscript sentence is softened
  (s1) to "None of these is stated to treat fixed-volume variations of a non-conformal block or the matrix data of
  Equation~\eqref{eq:Smatrix}". The second clause is checkable from the abstracts: BFSS, c=1, a complex matrix model
  and fuzzy-space QFT are not the action `eq:Smatrix`. The conclusion "none supplies the missing step of Problem~B"
  follows because the missing step is stated for `eq:Smatrix` and `eq:Smicro`. The full texts were not read.

**R7. Fork analysis (author directive 2026-10-15).** The obstruction in (ii) depends on these hypotheses:
- H1 the Gaussian class;
- H2 the flat bosonic measure;
- H3 finite N with no factorisation;
- H4 the fixed-geometry, fixed-measure replica;
- H5 a localized contact `P` that is independent of the state;
- H6 Presentation A with no fermions in the measure.

What each avenue gave in this package:
- **H5** was probed (L5). Stationarity on the whole `Tr(G_1 B) = 0` subspace forces `P ∝ A_1`, so a localized
  Gaussian contact is excluded. The contact must be non-local or state-dependent.
- **H2 and H6** were probed partially. The null-direction argument is content-independent for bosons. For the
  Grassmann measure the Berezinian of a spin-representation rotation is also 1 (traceless generators), so the
  insertion identity cannot produce the (6,2) Dirac excess either. This is stated only here, as a remark that is not
  checked by script, and is not put in the manuscript.

Ranked open avenues for follow-up packages:
1. Large-N factorisation plus the saddle measure: loop equations at leading order, with the contact `P` fixed by the
   planar resolvent instead of by hand (relaxes H3 and H5).
2. A geometry-varying replica in which the conical-locus data vary with `eps`, Lewkowycz-Maldacena type. This
   requires the background equations of motion and is the route in which stationarity can be an equation of motion
   (relaxes H4).
3. Measure Jacobians beyond the flat measure: Moyal corrections and the measure of the matrix integral, which are
   explicitly not computed in the book (relaxes H2).
4. The hyperplane `Tr(BK) = 0` read as a selection condition on the state that fixes `P` (relaxes H5 with L5).
5. A local symmetry of the matrix data that carries the `n_D = 0` coefficient (Problem D route).
6. Non-Gaussian contacts at quartic order (relaxes H1).
7. Literature analogues (eigenvalue-subregion and fuzzy entanglement) as analogy sources only.

## Claim classification

| Claim | Class |
|---|---|
| Measure identity at finite N | established identity |
| Unimodular flows are null directions; `tr B = 0`, `tr ad = 0` | established |
| `-4 kappa_X` (at `n_D = 0`) not producible along these flows | established within stated hypotheses (flat bosonic measure, Presentation A) |
| `∂_eps S_D = Tr(G_1BG_1P) - 1/2 Tr(G_1B)`; hyperplane for `P != A_1/2` | conditional on the Gaussian conical-contact class |
| Stationarity on all `Tr(G_1B)=0` forces `P ∝ A_1` (L5) | conditional (toy fixed-volume model); proposal text only |
| Grassmann Berezinian = 1 for spin rotations | established standard fact; not script-checked; proposal text only |
| Literature identifications | recorded identifications; abstracts verified; negative survey softened, full texts not independently verified |
| Fixed-volume stationarity of the tensor block | unresolved (Problem B stays OPEN) |

## Response to the local review (065)

| Finding | Action | Status |
|---|---|---|
| m1 Craps2026 wording | applied verbatim (edit `m1`) | closed |
| m2 ArataIsmailLiberati2026 scope | applied verbatim (edit `m2`) | closed |
| m3 disclaimer split | applied verbatim (edit `m3`) | closed |
| m4 "required at `n_D=0`" | applied verbatim at both occurrences (`m4a`, `m4b`) | closed |
| m5 `P != 1/2 A_1` qualifier | applied, with a placement change: "which, for \(P\neq\tfrac12A_1\), is nonzero … and vanishes only on the codimension-one hyperplane" instead of after "hyperplane" | closed |
| Note: negative survey not verified beyond abstracts | softened (`s1`) | closed |

The m5 placement change needs a reason, because the review asked for verbatim text. By R4, at `P = A_1/2` the
derivative vanishes for every `B` (L3d). The clause "nonzero for a generic block deformation B", which comes before
"hyperplane", is then false too. With the qualifier placed only after "hyperplane", that clause would stay
unqualified. Placing it after "which" makes it govern both clauses. The qualifier's text is unchanged.

OPEN after this round: 0/5 required findings (plus the note, also addressed).

## Cross-package: local 070 and its re-anchoring

- **Status of 070.** Round 1 got ACCEPT WITH REQUIRED REVISIONS (OPEN 0/2 majors, plus minors). A round-2 insert
  (`appH_insert_r2.tex`) and its apply check exist. There is no `proposal-r2.md` and no review-r2, so 070 is **not
  accepted**. Its certified baseline (`c2dac013…`) is not the live tree (`4d6d58cf…`), so 070 must re-certify its
  pre-state in any case.
- **Consistency with 065.** The 070 r2 text says that at (6,2) "the term \(-4\kappa_X\) required there of the
  modular Hamiltonian [is] absent". It also says that the identification of the fixed-state gap with `4 kappa_X`
  holds "at \(n_D=0\) … and at no other \(n_D\)". With m4, 065 states the `-4 kappa_X` requirement as an `n_D = 0`
  requirement, which agrees with this exactly (R5, L4a-L4d). 065 makes no statement at (6,2). Nothing in 070 has to
  change for consistency with 065.
- **Ordering.** 065 must sit immediately after the paragraph on the matrix gauge realisation, because its first
  paragraph says "disclaimed in the preceding paragraph", meaning that paragraph's scope sentence (L511). The apply
  check asserts this adjacency. 070 names the paragraphs it relies on ("on covariant variables and on the matrix
  gauge realisation") and so does not need adjacency.
- **Re-anchoring 070.**
  - After 065 is integrated, put 070 between the 065 block and `\section{Problem C: conformal mode and Cassini}`.
  - New anchor: the 065 closing sentence "These identifications record what the published mechanisms do and do not
    supply for Problem~B; no result is imported into the matrix theory. Problems~B and~D remain open and
    PROGRAMME-CONDITIONAL.", followed by a blank line and the Problem C header. In the post-state this combination
    occurs exactly once (asserted by `apply_build_local_r2.py`).
  - If 070 is integrated first, 065's anchor must instead be the matrix-gauge closing sentence followed by a blank
    line and `\paragraph{Content class of the order-…`. That breaks nothing textually, but it would put 070 before
    065. The preferred order is 065 then 070.
  - 070 itself is not rewritten here.

## Proposed changes

**File `chapters/appH-microscopic-proofs.tex`** (live pre-state: 686,297 B, 3522 CRLF, 0 bare LF, sha256
`4d6d58cf7947dae9570e917ced6db8b6e40287437162321c4517eb726a568fce`).

- **Insertion point.** Inside `sec:status-B`, at its end. Insert the block immediately before the unique line
  `\section{Problem C: conformal mode and Cassini}` (L513), so that it follows the existing blank line after L511.
- **Anchor**, which occurs exactly once:
  > …the Dirac sector or the measure of the matrix integral, and derive no local Lorentz symmetry. Problems~B and~D
  > remain open and PROGRAMME-CONDITIONAL.
  > (blank line)
  > \section{Problem C: conformal mode and Cassini}
- **Splice.** `pre[:i] + insert + CRLF + pre[i:]`, with `i` the offset of the header. The insert ends in CRLF, and
  the extra CRLF gives the blank line before the header.
- **Kept.** Nothing is removed or replaced. Every existing line is kept, and the Problem B ledger is untouched.
- **Expected post-state:** 693,327 B, 3538 CRLF, 0 bare LF, sha256
  `e6a3df38334ebf2bddc84cae2186288a8a3dfa331872f9779750418e684a5ada`.
- **Labels and keys.** The insert adds no `\label`. It uses `\eqref{eq:Smatrix}` (ch03 L143, unique) and
  `\ref{ass:EE}` (ch06 L71, unique), and 11 cite keys, all new.
- **Status sentence.** There is exactly one, at the end of the block: "Problems~B and~D remain open and
  PROGRAMME-CONDITIONAL."
- **Exact bytes.** The insert, with CRLF line endings, is
  `proposals/local-gpu/065-b-ward-measure-insertion-sublemma/insert-local-r2.tex` (7,028 B, sha256
  `c8a2422bed86cb74a983ced0e3f64db25d9c68b578fee24a0a9c8dec8f5c312e`).

```latex
\paragraph{Schwinger--Dyson insertion, measure Jacobians and null directions of the replica functional (conditional; not closure).}
Let \(Z_n(\varepsilon)\) be the replica functional of the paragraph on the replica insertion identity, built from the matrix data of Equation~\eqref{eq:Smatrix} at finite \(N\) and Presentation~A: \(\varepsilon\) deforms a datum of the block or of the induced density and the insertion is \(\mathcal I_n=\partial_\varepsilon S_{E,n}\). Writing the integrand as \(j_\varepsilon\,e^{-S_{E,\varepsilon}}\), with \(j_\varepsilon\) the ratio of the integration measure to the reference matrix measure, differentiation under the integral sign gives, at finite \(N\), the exact identity
\[
  \partial_\varepsilon\ln Z_n=-\langle\mathcal I_n\rangle_n+\langle\partial_\varepsilon\ln j_\varepsilon\rangle_n\,,
\]
and the Schwinger--Dyson (loop) equations of the matrix integral~\cite{EynardOrantin2009}, \(\langle\mathcal V(S_{E,n})\rangle_n=\langle\operatorname{Div}\mathcal V\rangle_n\) for compactly supported vector fields \(\mathcal V\) on the matrix entries, give zero expectation to every equation-of-motion insertion and reduce insertions to contact terms. For the flat Lebesgue matrix measure of Equation~\eqref{eq:Smatrix} the Jacobian term vanishes identically; for Moyal corrections and the measure of the matrix integral, disclaimed in the preceding paragraph, and for field redefinitions it must be retained, and it is not computed anywhere in this book.

Two consequences bound what the loop equations can supply for Problem~B. (i)~Unimodular deformations are null directions: if the \(\varepsilon\)-dependence is generated by a divergence-free field redefinition, then every \(Z_n(\varepsilon)\) is \(\varepsilon\)-independent and \(\langle\mathcal I_n\rangle_n=\langle\partial_\varepsilon\ln j_\varepsilon\rangle_n=0\) for every \(n\). The compensating rotation acts as \(X^a\mapsto e^{tB}X^a\) with \(B^a{}_b=\partial_b\xi^a\) antisymmetric in \(\eta\), hence \(\operatorname{tr}B=0\) and \((\det e^{tB})^{N^2}=1\) over the \(N^2\) matrix entries, and the adjoint flows \(X\mapsto e^{t\Lambda}Xe^{-t\Lambda}\) have \(\operatorname{tr}\operatorname{ad}_\Lambda=0\) (exact checks). The coefficient \(-4\kappa_X\) required at \(n_D=0\) in the paragraph on the matrix gauge realisation cannot therefore be produced by the insertion identity along a compensating rotation or an adjoint flow, which sharpens the recorded conclusion that this coefficient is a property of the modular Hamiltonian of the state at \(\Sigma\), or of a local symmetry under which the compensating rotation would be a gauge transformation, and not of the induced density. (ii)~The loop equations do not imply stationarity even at Gaussian order: for the conical-contact family \(A_n=A_1+(\tfrac1n-n)P+\varepsilon B\) of the block quadratic form, with \(P\) supported at the branch locus (the same \(n\)-dependence as the flat-cone coefficient of the paragraph on the replica cone coefficient), the identity above gives exactly
\[
  \partial_\varepsilon S_D=\operatorname{Tr}(G_1BG_1P)-\tfrac12\operatorname{Tr}(G_1B),\qquad G_1=A_1^{-1},
\]
which, for \(P\neq\tfrac12A_1\), is nonzero for a generic block deformation \(B\) and vanishes only on the codimension-one hyperplane \(2\operatorname{Tr}(G_1BG_1P)=\operatorname{Tr}(G_1B)\). In this class \(\delta S_D=0\) is a linear condition on the deformation, a linearised block equation together with a contact term at the tip, and not a consequence of any Schwinger--Dyson identity. These statements are for finite \(N\), the Gaussian conical-contact class, the flat matrix measure of Equation~\eqref{eq:Smatrix}, Presentation~A and the fixed-geometry, fixed-measure replica prescription of the paragraph on the replica insertion identity, into which the conical-locus contribution enters through \(S_{E,n}\); they do not give the locality or large-\(N\) factorisation that would turn contact identities into a Ward identity of the block, do not establish fixed-volume stationarity of the tensor block, and do not select the edge term.

\paragraph{Nearest published statements and the reduced-action charge mechanism (conditional; not closure).}
The nearest published analogues compute entanglement of matrix degrees of freedom rather than the response of a block to fixed-volume deformations: target-space entanglement of eigenvalue subregions with qualitative area agreement in the bubbling-geometry matrix model~\cite{TsuchiyaYamashiro2022}; momentum-space entanglement on fuzzy spheres~\cite{KawamotoKuroki2021}; perturbative interaction corrections to entanglement on fuzzy spaces, which are bulk-extensive and do not obey a pure area law~\cite{AlloucheDou2026}; the entanglement of the black 0-brane with its Hawking radiation in the BFSS model~\cite{ChoudhuryLaurenzano2024}; and the \(c=1\) string, where a dilaton-dependent area-like term is expected in the generalised entropy of bulk subregions but the leg-pole transformation relating the target-space tachyon to the singlet-sector collective field does not account for it~\cite{Craps2026}. None of these is stated to treat fixed-volume variations of a non-conformal block or the matrix data of Equation~\eqref{eq:Smatrix}, and none supplies the missing step of Problem~B. On the continuum side, the first law and equilibrium statements for causal diamonds~\cite{JacobsonVisser2019,Svesko2019} and the type-II-algebra realisation of a variant of the entanglement equilibrium hypothesis~\cite{JensenSorceSperanza2023} presuppose an existing metric or a geometric modular flow, an input that a derivation of Assumption~\ref{ass:EE} from Equation~\eqref{eq:Smatrix} must not use. For the edge-term bookkeeping, the published mechanism nearest to the \(r\)-family argument is the charge mechanism of Einstein--aether thermodynamics: the first law of stationary black holes carries an irreducible entropic aether contribution~\cite{ArataLiberatiNeri2026}, and the additional first-law term of misaligned universal horizons is, in the static, spherically symmetric, asymptotically AdS sector with \(c_{14}=0\), the charge of a symmetry \(\delta u^a=f\,a^a\) of the reduced action, with \(f\) obeying an elliptic constraint~\cite{ArataIsmailLiberati2026}. The NAMCG situation is the mirror obstruction, not an application of this mechanism: the compensating rotation is an isotropy of the background and not a local rotation of the matrix index, the densities \(L_r\) agree with \(L_0\) only on the stated background class, the term \(Y(\phi,\mathcal L_\xi X)\) does not drop out of the charge, and no local symmetry of the matrix data carries the coefficient \(-4\kappa_X\) required at \(n_D=0\) in the paragraph on the matrix gauge realisation; the existence of such a symmetry belongs to Problem~D. These identifications record what the published mechanisms do and do not supply for Problem~B; no result is imported into the matrix theory. Problems~B and~D remain open and PROGRAMME-CONDITIONAL.
```

**File `bib/namcg.bib`** (live pre-state: 31,682 B, 1059 CRLF, sha256
`a7aec454de0f6591c157ecb4709179f212c876b6f0df5df67713df85bb0493ed`).
- Append `bib_additions.bib` unchanged from gpu r1/r2 (LF-normalised sha256 `d9f83e00…`, as recorded by the gpu
  gatekeeper), converted to CRLF, with one CRLF separator.
- There are 11 entries; none of the keys and none of the arXiv IDs or DOIs is already in the bib (checked by grep).
- Expected post-state: 35,433 B, 1178 CRLF, 0 bare LF, sha256
  `a0b2319a3d1cce3c616f188b6859b7a508d582c0f547786794662a73a80e2962`, 111 entries.

**Stale passages elsewhere.** None. ch17 and the ledger are unchanged.

## Verification scripts

All scripts live in `proposals/local-gpu/065-b-ward-measure-insertion-sublemma/`. Run them with `python -I` from any
directory.

| Command | What it checks | Expected invariant output |
|---|---|---|
| `python -I derive_ward_r1.py` | gpu checks C1-C4 (re-run) | output byte-identical to the gpu record, sha256 `6655d85b…` (saved as `derive_ward_r1.out`); `C4 … True` |
| `python -I derive_local_r2.py` | independent L1-L5 (measure identity non-Gaussian/Gaussian; null directions; conical formula and its replica form; `P=A_1/2` degeneracy; content arithmetic for m4/070; fork probe) | 26 `PASS` lines, last line `ALL PASS`; `d_eps S_D = 259954600/2708890209` equal to the closed form; `c_A - c_T = 4 - n_D`; at (6,2) `kappa_X=0, -4kappa_X=0, c_T=0, c_A=2` |
| `python -I make_insert_local_r2.py` | builds `insert-local-r2.tex` from `insert-r2.tex` (LF sha `7db417b6…`) by seven count-asserted edits | `m3 m4a m5 m1 s1 m2 m4b applied (1 occurrence)`; `dst bytes=7028 CRLF=15 bareLF=0 sha256=c8a2422b…`; `\label` 0; one closing status sentence; `MAKE INSERT PASS` |
| `python -I apply_build_local_r2.py` | live pre-state hashes; anchor uniqueness; splice; adjacency to the matrix-gauge paragraph; 070 re-anchor point unique; labels; bib keys | `appH post: bytes=693327 … sha256=e6a3df38…`; `bib post: bytes=35433 … sha256=a0b2319a…`; `APPLY CHECK PASS` |
| `python -I apply_build_local_r2.py --build <dir outside repo, not existing>` | copies the sources, applies, runs pdflatex, bibtex, pdflatex, pdflatex | `pages=399`, `undefined/multiply-defined warnings: 0`, `bibtex warnings/errors: 0`, `new keys in bbl: 11 / 11`, `BUILD PASS` |

- **Build result.** The build was run in
  `C:/Users/redgi/AppData/Local/Temp/claude/3ba14ee056ac155d/8095df06-9555-40ba-b1c2-719eb5f35f33/scratchpad/build065`.
  The copy is left there, nothing was deleted, and the log is saved as `build_local_r2.out`. Nothing was built inside
  the repository.
- **Superseded scripts.** `simulate_apply.py` and `simulate_apply_r2.py` are the gpu-era scripts. They assert the gpu
  pre-state (`dd0bea77…`) and a different folder depth, so they fail by design on this tree.
  `apply_build_local_r2.py` replaces them.

## Decisions Taken

1. **m5 placement.** I put the qualifier after "which" so that it governs both clauses (R4, L3d). I rejected the
   literal placement, because it would leave "nonzero for a generic B" false at `P = A_1/2`.
2. **Survey softening (s1).** I chose "is stated to treat …" and added the checkable clause about the matrix data of
   `eq:Smatrix`. I rejected deleting the sentence, because the bounded negative is useful for routing. I also
   rejected an in-text "not independently verified", which is process language.
3. **m4 at the second occurrence.** I used the full phrase "required at \(n_D=0\) in the paragraph on the matrix
   gauge realisation" at both places, for verbatim compliance and unambiguous scope at (6,2).
4. **Ordering with 070.** 065 goes first, adjacent to the matrix-gauge paragraph, and 070 follows it. The reason is
   that "preceding paragraph" in 065 must resolve, and 070 uses only named references.
5. **Fork probe L5.** It is kept in the proposal text only, as routing evidence that the missing contact is
   non-local or state-dependent. Adding it to the manuscript would enlarge the insert beyond the accepted result.
   It can be a follow-up package with avenue 4.

## Milestone assessment

Routine. A bounded obstruction and a sub-lemma; no critical-path step derived.

## Status-label recommendation

- Critical-path list from ch17 and the ledger: A, B, C, D1, E, F, G-derived, N.
- Affected labels: B and D (named in the closing sentence). Both stay OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.
  No change is recommended.

## Author decision needed

None.

## Remaining open step

Derive `delta S_D = 0` at fixed volume for the non-conformal tensor block from `eq:Smatrix` (after A), with a
specified map `g^(0) -> g`. This needs one of the following, in the ranked order of R7:
- a contact or measure term fixed by the large-N state, not by hand;
- a geometry-varying replica whose stationarity is an equation of motion;
- a local symmetry carrying the `n_D = 0` coefficient.

At (6,2) the remaining fixed-state gap is the Dirac excess `c_A = 2`, which is 070's subject.

## Special instructions for the gatekeeper

- Verify that `insert-local-r2.tex` differs from the accepted gpu text only by the seven listed edits. Re-run
  `make_insert_local_r2.py`: every edit is count-asserted against the LF sha `7db417b6…`.
- Re-check that the m5 relocation is justified by `P = A_1/2 ⇒ ∂_eps S_D ≡ 0`.
- Do not let the insert be read as a statement at (6,2). The `-4 kappa_X` requirement is an `n_D = 0` statement.
- The fork probe L5 and the Berezinian remark are proposal-only and must not migrate into the manuscript without a
  package.
- The negative survey claim rests on abstracts only. The full texts were not read.
- Integrate 065 before local 070 and re-anchor 070 as described. 070 is not accepted.
