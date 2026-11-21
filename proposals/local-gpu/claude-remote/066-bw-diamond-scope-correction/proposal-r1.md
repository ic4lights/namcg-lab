# Proposal 066-bw-diamond-scope-correction, round 1

## Result

The merged sentence in the Problem A free/Poisson lemma (appH L30-31) is overbroad and misattributed. It reads
"By the Bisognano–Wichmann theorem this charge is the modular Hamiltonian of the causal diamond of the free theory".
This is a correction of a materially false claim (PRIOR-CLAIM-ERROR).

1. The Bisognano–Wichmann theorem concerns wedge regions. Their modular operator is a complexified boost, from
   Theorem 1(d) of the primary source, read from the LBL-4283 preprint of the 1976 J. Math. Phys. paper. The paper
   treats double cones only as algebras built from wedge algebras (its Sec. VI duality results). It gives no
   geometric modular flow for double cones.
2. The double-cone (causal diamond) geometric modular flow is Hislop–Longo, CMP 84 (1982) 71–85. It is proved
   for the free massless scalar field through conformal covariance.
3. "The free theory" of this lemma is not restricted to massless conformal fields. The manuscript's own quadratic
   sector of the Mexican-hat potential contains a radial Higgs mode of mass m_σ ∼ √λ v (ch03, Section
   `sec:ch3-scales`). So the sentence cannot be saved by reading "free theory" as "massless conformal field". The
   negative-result branch (sentence correct as stated) does not apply.

The bound O(R√‖δΘ‖), and its companion O(R√‖δΘ‖ + ‖H_int‖) at L52–55, appears nowhere else in the repository.
It has no derivation and no citation. It entered in author commit 6aa4490 together with the BW sentence. `R` is
not defined in the passage. I mark it as an unproved estimate and leave it in place.

Proposed change: six minimal OLD→NEW edits inside the two evidence paragraphs of Problem A ("Free/Poisson sector
(lemma)" and "General sector"), plus one new verified bib entry (`HislopLongo1982`). The changes:
- restrict BW to wedges;
- attribute the diamond statement to Hislop–Longo for the free massless scalar;
- scope the lemma's H_D claim to that part;
- mark the √δΘ bounds as not derived.

The "Ledger label" paragraph, the "Missing step" paragraph, the section title and every status, priority and
completion label are untouched. Problem A stays OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

Separately, report only: there is a definitional mismatch between ch17 (Problem A = infrared dictionary with error
control) and appH (Problem A = matrix-to-modular map). The texts are quoted below for the author.

## Target and status

- Problem A, `sec:status-A` (appH L12). Ledger label (appH L15–20), verbatim: "Status: OPEN. Priority: CRITICAL
  PATH for the matrix-derived label. Completion: PROGRAMME-CONDITIONAL. The general matrix-to-modular map remains
  unproved. A scope-limited Presentation-B model may retain Assumption~\ref{ass:dictionary} and claims no
  derivation from the matrix model."
- ch17 (L377–392): "OPEN; CRITICAL PATH for the matrix-derived label." The status and priority agree with appH.
  The definitions of the target differ; see the separate item below.
- Original target (ch17): derive Assumption `ass:dictionary`, [X̂_μ,Φ] ↔ iΘ_{μν}D^νΦ plus higher-derivative
  corrections, with "Hilbert space, Weyl map, continuum limit, and error at each order in Θ".
- Dependencies: Chapter 8 heat kernel (Presentation-B unless A is derived), and the modular/diamond working formula
  `eq:HD-boost` (ch06), via the appH framing.
- This package: a correction of a materially false attribution plus a scope marking. It is neither DERIVED nor
  PROGRAMME-CONDITIONAL as an advance on A. It changes no label.

## Source reading

Digest + targeted reads. `python scripts/make_digest.py --check` printed `DIGEST CURRENT`. The digest reports
`dirty-chapters: yes`, and appH is CHANGED (the 064/065 integrations, uncommitted).

Baseline was verified by the apply-check:
- appH: 624232 bytes, sha256 c2dac013…558b5c, all 3378 line endings CRLF, no BOM;
- bib: 29781 bytes, sha256 28fdd7f8…a64d, CRLF.

Read in full:
- appH L1–70: Problem A (section, ledger label, lemma, general sector, missing step).
- ch17 L372–399: Problem A and E agenda entries.
- appB L110–150: `sec:appB-BW`, `eq:appB-BW`, and the "exact for free fields in Rindler space" passage.
- ch02 L436–456: the H_D definition context and the BW sentence.
- ch06 L144–160: `eq:HD-boost` context.
- ch03 L219–245 (`eq:Smicro`, `eq:V`), L345–361 (`ass:dictionary`) and L785–830 (`sec:ch3-scales`, `eq:scales`,
  the radial Higgs mass row, `eq:scale-ineq`).
- bib/namcg.bib, the BisognanoWichmann1976 entry and its surroundings.

Searches:
- `delta.Theta` across chapters/*.tex: only appH L36, L43 and L54.
- `Bisognano|Hislop|Longo` across chapters and bib.
- `git log -S` on both strings: both entered in author commit 6aa4490, commit message "1".

No full scan. This is not needed because no definition, assumption, scope statement or status passage changes; see
"Special instructions". The edits are inside the Problem A ledger section of appH, but not in its "Ledger label"
status paragraph.

## Research and reasoning

### 1. What the sentence claims

K_0 has a Weyl symbol equal to "the classical boost/diamond Noether charge" of the constant-Θ quadratic sector. The
sentence then asserts, via BW, that this charge is the modular Hamiltonian H_D of a causal diamond for "the free
theory". Everything after it relies on that identification:
- the half-sided inclusion "whose modular operator is exactly H_D";
- "the map (X̂,Φ)↦H_D is a lemma in this sector";
- MI via Araki.

### 2. Primary sources (verified)

**Bisognano–Wichmann 1976.** I read the LBL-4283 preprint, "On the duality condition for quantum fields",
J. J. Bisognano and E. H. Wichmann, August 1975, "Submitted to Journal of Mathematical Physics". Its eScholarship
permalink is https://escholarship.org/uc/item/0sf4t33q. I read the page images of preprint pp. (1)–(7) and
(33)–(36). What it says:
- The abstract covers a general QFT with operator-valued tempered distributions, boson and fermion fields. It
  relates complex Lorentz transformations to TCP and gives duality conditions.
- The Introduction calls the 1975 paper "BW I" (the Hermitian scalar field) and extends it to general fields.
  Section V is "The duality condition for the wedge regions W_R and W_L". Section VI builds algebras for "other
  regions than wedge regions in terms of algebras associated with W_R and W_L", and "for reasons of simplicity …
  double cones and their causal complements". Its results there are duality statements.
- Eq. (2) defines the right wedge as W_R = {x | x³ > |x⁴|}.
- Theorem 1 (pp. 33–34), parts (c) and (d), states the following. Let V(t) be the velocity transformation in the
  3-direction. Then V(t)𝒫(W_R)V(t)⁻¹ = 𝒫(W_R). Also V(iπ)XΩ = J X*Ω for X ∈ 𝒫(W_R) (eq. 45d), and (46c)
  identifies the closure of the Tomita operator as JV(iπ). This is the modular statement Δ^{1/2} = V(iπ) for the
  wedge. In modular language: Δ^{it} = V(−2πt), so the modular Hamiltonian is 2π times the boost generator.

The journal record (J. Math. Phys. 17 (1976) 303–321) matches the bib entry `BisognanoWichmann1976`. The DOI
10.1063/1.522898 comes only from a secondary listing (Bohrium); I could not open the AIP page. Only the preprint
content is verified, and it is the source of the statements above. The 1975 paper, J. Math. Phys. 16 (1975)
985–1007, "On the duality condition for a Hermitian scalar field", is confirmed bibliographically by the nLab entry
and a Scilit search snippet. I did not read its content, so it is not cited.

**Hislop–Longo 1982.** P. D. Hislop and R. Longo, "Modular structure of the local algebras associated with the
free massless scalar field theory", Commun. Math. Phys. 84(1) (1982) 71–85, DOI 10.1007/BF01208372. This was
verified through the University of Kentucky Scholars record
(https://scholars.uky.edu/en/publications/modular-structure-of-the-local-algebras-associated-with-the-free-/). The
abstract, as the record presents it:
- it treats the modular structure of the double-cone algebra in the vacuum representation of the free massless
  scalar field in any dimension;
- the modular automorphism group is implemented by generalized fractional linear (conformal) transformations
  preserving the double cone;
- lightcone, double-cone and wedge algebras are unitarily equivalent.

I did not read the full text (the Springer page redirects to a login). The claim used is the abstract-level one.

**Not used in the manuscript text:** Longo–Morsella, "The massless modular Hamiltonian", arXiv:2012.00565. I
verified the abstract. Its arXiv comment records that "results on the massive modular hamiltonian of a ball
contained a gap, and have been removed". This supports the cautious wording "no such geometric identification is
used here for massive free fields". It does not prove non-geometricity for massive fields, and I make no such claim.

### 3. Is the sentence correct under some reading of "free theory"?

- **(a) BW attribution.** False for diamonds under any reading. BW yields the wedge result. The diamond result for
  the massless scalar follows from BW combined with conformal covariance, and that is Hislop–Longo's contribution.
  Attributing it to BW is a misattribution. The wedge statement holds with or without mass: BW assumes only
  Wightman fields, so it covers free massive fields.
- **(b) Diamond for "the free theory".** The surrounding manuscript's quadratic sector includes the radial Higgs σ
  with m_σ ∼ √λ v (ch03 table in `sec:ch3-scales`; `eq:scale-ineq` keeps m_σ ≪ Λ_UV, nonzero). Expanding
  `eq:V` about Φ†Φ = v²I, with Φ = (v+ρ)U, gives V ≈ λ v² Tr ρ² ≠ 0. So the quadratic sector has massive
  modes. Goldstones are eaten by the gauge connection (same table), so massive vectors also appear.
  - For a massive free field the diamond's conformal Killing vector is not a symmetry. The associated "diamond
    Noether charge" is not conserved, and no theorem identifies it with the diamond modular Hamiltonian.
  - Hence even a charitable reading ("free = massless conformal") is not what the lemma's sector contains. The
    statement is overbroad, not merely misattributed.
- **(c) Lattice illustration.** This is not a proof and is not used in the manuscript. In
  `lattice_modular_profile_066.py`, the interval entanglement Hamiltonian of a free-fermion chain (Peschel's
  formula) has a nearest-neighbour profile within 6% of the conformal parabola β(x) = 2πx(ℓ−x)/ℓ at m = 0. That
  6% is the known lattice correction. The profile deviates by 27% at m = 0.2 and by 44% at m = 0.5, and the
  longer-range weight grows (1.7% → 6–7%). This is consistent with the diamond-geometric form being a massless
  feature. It is a fermion lattice model at ℓ = 12, not the continuum scalar.

**Verdict.** The sentence is false as written: it misattributes the result and extends the diamond identification
to massive free fields. The minimal correction keeps BW for wedges (any mass), cites Hislop–Longo for the massless
scalar diamond, and scopes the lemma's H_D claim to the free massless scalar part.

### 4. The √δΘ bounds

- They appear only at appH L36 and L54, with no derivation in any chapter, appendix or bib entry, and no citation.
  `R` is undefined in Problem A; elsewhere the manuscript uses ℓ for the diamond radius.
- Standard reasoning available, not imported into the manuscript. For bounded generators, Duhamel gives
  ‖e^{iKt}Ae^{−iKt} − e^{iK't}Ae^{−iK't}‖ ≤ 2|t|‖K−K'‖‖A‖. This is linear in the generator change at fixed t. A
  √‖δΘ‖ law would need a separate mechanism, e.g. Pinsker-type trace-norm bounds from relative entropy.
  Neither exists in the manuscript. In QFT the modular Hamiltonians are unbounded, so ‖K−K'‖ can be infinite. The
  missing ingredient is therefore a bound of the relative modular generator (e.g. a Connes cocycle estimate) in
  terms of δΘ on the relevant algebra.
- I cannot source or derive the estimate within this package. I scope it: "not derived here … an unproved
  estimate", and "Even if derived, the estimate would …". This keeps the author's estimate visible as a target,
  with `R` named as the diamond radius. The General-sector conclusion, that the bound controls at most the
  difference from an unproven candidate, is kept and strengthened.

### 5. No-go fork (author directive 2026-10-15)

This is a correction, not a no-go. It does narrow the free/Poisson lemma, so I record the avenues that could restore
a diamond-level statement for the full quadratic sector:
1. **Small-diamond limit ℓ ≪ 1/m_σ.** Massive modes should look conformal at leading order. This is the
   ch06/appB working formula `eq:HD-boost` ("to leading order in ℓ"). It needs an error-controlled estimate of the
   massive diamond modular flow, which is not available. Longo–Morsella removed their massive-ball result
   because of a gap.
2. **Work with wedges.** BW holds for massive free fields. If the Problem A modular map can be formulated for
   wedge (Rindler-horizon) algebras, the mass restriction disappears. The cost is a non-compact region and the
   need to connect to the diamond-based first law.
3. **Integrate out σ.** Under `eq:scale-ineq` (m_σ ≪ Λ_UV is assumed, but the infrared regime is below m_σ), the
   IR theory could be the massless sector only. The Goldstone/gauge content then decides whether the remaining
   free part is conformal. Free Maxwell is conformal in 4D, but Hislop–Longo covers only the scalar.
4. **Free massless Maxwell/fermion diamond results** would extend avenue 3. They are not checked here.

Ranking for follow-up: 2 (cheapest, sound for massive fields), then 3, then 1, then 4.

## Claim classification

- BW gives wedge modular flow = boosts for general Wightman fields, including massive free fields. **Established**
  (verified from the preprint, Theorem 1).
- The double-cone modular flow is conformal-geometric for the free massless scalar. **Established** (Hislop–Longo,
  verified at the abstract level).
- The appH sentence attributing the diamond statement to BW for "the free theory" is false and overbroad.
  **Established** (correction).
- The NAMCG quadratic sector contains a massive radial mode. **Established** within the manuscript (ch03 table,
  `eq:V` expansion).
- The massive diamond modular flow is not geometric. **Not claimed.** It is only stated as not used and not
  established here.
- The √δΘ bounds. **Unresolved step** (unsourced estimate, now marked as such).
- The positive spectral subspace generates a half-sided inclusion "whose modular operator is exactly H_D".
  **Unresolved, not addressed.** It is unsourced and is now conditional on the scoped identification. It is
  flagged under "Remaining open step", with no edit.
- The lattice profile. **Illustration only.**

## Proposed changes

### File `chapters/appH-microscopic-proofs.tex`

All six edits are inside `\section{Problem A: matrix-to-modular map}`, in the paragraphs "Free/Poisson sector
(lemma)" and "General sector". Each OLD string occurs exactly once (checked by `apply_check_066.py`). Line breaks
are CRLF. All other text in both paragraphs is kept verbatim. The "Ledger label." and "Missing step." paragraphs are
untouched.

**E1** replaces the two lines L30–31. This is the sentence "By the Bisognano–Wichmann theorem … free theory." The
L30 prefix "degree \(\le 2\)). " and the trailing "The" (start of the next sentence) are kept.

OLD (the en-dash is U+2013 in the source):
```latex
degree \(\le 2\)). By the Bisognano–Wichmann theorem this charge is the
modular Hamiltonian of the causal diamond of the free theory. The
```
NEW:
```latex
degree \(\le 2\)). For a Rindler wedge, the Bisognano--Wichmann
theorem~\cite{BisognanoWichmann1976} identifies the vacuum modular
Hamiltonian with \(2\pi\) times the boost generator that fixes the
wedge (Section~\ref{sec:appB-BW}), for free fields with or without
mass. For a causal diamond (double cone), the identification of the
vacuum modular flow with the conformal Killing flow of the diamond is
established for the free massless scalar field~\cite{HislopLongo1982},
through conformal covariance. No such geometric identification is
used here for massive free fields, such as the radial mode with the
mass \(m_\sigma\) of Section~\ref{sec:ch3-scales}. Hence the charge
is the modular Hamiltonian of the wedge for the free theory, and
of the causal diamond only for its free massless scalar part. The
```

**E6** scopes the lemma claim (L34) to match E1.

OLD:
```latex
\((\hat X,\Phi)\mapsto H_D\) is a lemma in this sector, defined from
```
NEW:
```latex
\((\hat X,\Phi)\mapsto H_D\) is a lemma for that massless scalar part
of this sector, defined from
```

**E2** marks the bound (L36).

OLD:
```latex
\(\Theta\), with error \(O(R\sqrt{\|\delta\Theta\|})\) under fluctuations.
```
NEW:
```latex
\(\Theta\). Its error under fluctuations of \(\Theta\) is not derived
here; the scaling \(O(R\sqrt{\|\delta\Theta\|})\), with \(R\) the
diamond radius, is an unproved estimate.
```

**E3** (L50–52). The displayed equation itself is kept unchanged.

OLD:
```latex
terms and is not a routine specialisation of the free-field result. The
bound
\[
```
NEW:
```latex
terms and is not a routine specialisation of the free-field result. The
estimate, which is not derived here,
\[
```

**E4** (L56–58).

OLD:
```latex
controls the difference from the free modular flow (itself identified
with the diamond only in the constant-\(\Theta\) quadratic sector); it
does not control
```
NEW:
```latex
would control the difference from the free modular flow (itself
identified with the diamond only in the constant-\(\Theta\) quadratic
sector, and there only for its free massless scalar part); it would
not control
```

**E5** (L59–60). The final line "Hamiltonian." is kept.

OLD:
```latex
of the general theory. The error bound therefore controls the
difference from an unproven candidate, not from the diamond modular
```
NEW:
```latex
of the general theory. Even if derived, the estimate would therefore
control only the difference from an unproven candidate, not from the
diamond modular
```

The result has 625157 bytes and sha256 `173ab97bc1ffeb14a089f2db2fbefb6f6570727e5d8f5ec885d09083f497e945`.
CRLF = LF = 3393, no bare LF, no BOM.

Labels verified to exist exactly once:
- `sec:appB-BW` (appB L118);
- `sec:ch3-scales` (ch03 L790).

Citation keys:
- `BisognanoWichmann1976` already exists in the bib. It was cited by no chapter; it was included only via
  `\nocite{*}`.
- `HislopLongo1982` is new (below).

### File `bib/namcg.bib`

**B1** inserts after the existing `BisognanoWichmann1976` entry, which is kept unchanged. OLD is the full existing
entry plus its CRLF. NEW is the same entry, a blank line, and the following:

```bibtex
@article{HislopLongo1982,
  author  = {Hislop, Peter D. and Longo, Roberto},
  title   = {Modular Structure of the Local Algebras Associated with
             the Free Massless Scalar Field Theory},
  journal = {Communications in Mathematical Physics},
  volume  = {84},
  number  = {1},
  pages   = {71--85},
  year    = {1982},
  doi     = {10.1007/BF01208372}
}
```

The result has 30159 bytes and sha256 `4315a89553cb97405af89604f1e43c9e5e0237fa5b7be0439431d042677a6060`.
CRLF = LF = 1006, no BOM. I propose no DOI for `BisognanoWichmann1976`: its DOI was not verified on the
publisher page.

### Stale passages elsewhere: none requiring change

- ch02 L443–444, ch06 L149–151 and appB L119–124, L144: these state BW for "a free field in Rindler space", which
  is the wedge statement and is correct.
- The ch06 / appB small-diamond "to leading order in ℓ" statement is a working approximation already labelled as
  such. It is not touched; see avenue 1.

## Verification scripts

- `apply_check_066.py <repo_root> <out_dir>`, with output in `apply_check_066_output.txt`.
  - Report-only. Backslashes are built with `chr(92)`, and it writes only to an out_dir outside the repo (it
    asserts this).
  - It checks the baseline sizes and hashes, single occurrence of each OLD, zero prior occurrences of each NEW,
    CRLF and no BOM, and prints the result hashes. Status: ALL CHECKS PASS.
- `lattice_modular_profile_066.py`, with output in `lattice_modular_profile_066_output.txt`. This is the
  illustration in §3(c), not a proof.
- Scratch build (see the end of this file): pdflatex, bibtex, pdflatex, pdflatex on a copy outside the repo with
  both patched files.

## Decisions Taken

- **Wording: scope, not delete.** The lemma keeps the wedge statement, valid for all free fields, and the diamond
  statement for the massless scalar part. Deleting the lemma would discard a correct wedge result usable by avenue
  2. Restricting only to "massless conformal" without mentioning wedges would lose the mass-independent statement.
- **Bound: mark, not delete.** The author's estimate is kept as a named, unproved target, with R defined as the
  diamond radius (the meaning implied by context). Deleting it would remove the author's stated target. Sourcing
  it is impossible: there is no derivation or citation.
- **Cite the 1976 BW paper only.** That is the one whose content I read. The 1975 paper is bibliographically
  confirmed but its content was not read.
- **Half-sided-inclusion sentence: report, not edit.** Editing its content would go beyond the minimal correction
  and would need a separate argument.

## Milestone assessment

M3, correction of a materially false prior claim (PRIOR-CLAIM-ERROR) in author-edited Problem A text. The claim
is a misattributed and overbroad theorem citation. It is not a breakthrough. No critical-path step is derived.

## Status-label recommendation

The current critical-path set at full-GR / matrix-derived scope, per ch17 and appH, is A, B, C, D1, E, F,
G-derived and N. Affected labels: none. Problem A remains OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL. The
correction narrows the evidence paragraph; it does not change the label.

### Separate item (report only, no edit): ch17/appH definitional mismatch for Problem A

ch17 L377–392, verbatim:
> \paragraph{Problem A: the infrared dictionary.} \emph{OPEN; CRITICAL PATH for the matrix-derived label.} A
> scope-limited Presentation-B model may retain Assumption~\ref{ass:dictionary}; it then claims no derivation from
> the matrix model, and Chapter~8 remains a Presentation-B calculation. Assumption~\ref{ass:dictionary} is the map
> [\hat X_\mu,\Phi] ⟷ i\Theta_{\mu\nu}D^\nu\Phi (eq:dict-again) plus higher-derivative corrections. A derivation
> must specify the Hilbert space, Weyl map, continuum limit, and error at each order in \(\Theta\).

appH L12 and L17–18:
> \section{Problem A: matrix-to-modular map}
> … The general matrix-to-modular map remains unproved.

appH L63–69 ("Missing step"):
> An error-controlled identification of the algebraic inclusion generated by \(K_0\) (or of \([\hat X,\Phi]\))
> with the modular Hamiltonian \(H_D\) of a causal diamond, or with the mutual-information functional
> \(U_{\mathrm{ent}}[I(A:B)]\), that holds for the general (non-quadratic) matrix model before the composite metric
> is defined.

**Discrepancy.**
- ch17's completion target is a kinematic operator dictionary: commutator ↔ Θ-twisted covariant derivative, with
  a specified Hilbert space, Weyl map, continuum limit and order-by-order error.
- appH's target, as titled and stated in the missing step, is a dynamical/state-dependent identification of a
  matrix-built inclusion with the diamond modular Hamiltonian, or with the MI functional.
- The two are logically distinct. Deriving the dictionary does not give the modular identification. That would
  need the state, the subsystem algebra and the modular theory, consistent with the gatekeeper's rule that "a
  commutator-to-derivative identity does not determine the state, subsystem algebra, modular Hamiltonian or MI".
  Conversely, a modular identification need not supply the Weyl map with order-by-order error.
- appH's "Missing step" mentions [X̂,Φ] only parenthetically. It ends by saying that until the identification is
  a lemma, Chapter 8's relation to Chapter 3 "is still Assumption~\ref{ass:dictionary}". This treats the modular
  map as the route to the dictionary without saying so explicitly.

**Options for the author** (scope change, author only):
- (i) align the appH title and missing step with ch17 (dictionary as target, modular map as one route);
- (ii) state in ch17 that A comprises both;
- (iii) split A into A-dictionary and A-modular, with the critical-path label on whichever ch17 requires.

I recommend (i), because ch17 controls completion and its target is the narrower, better-specified one. I make no
edit.

## Author decision needed

Only the separate ch17/appH Problem A definitional mismatch above. That is a scope/definition question, and no edit
is proposed. Nothing else.

## Remaining open step

- Problem A, original ch17 target: unchanged and OPEN.
- In the free/Poisson lemma:
  - (a) the half-sided-inclusion sentence ("positive spectral subspace … whose modular operator is exactly H_D")
    is unsourced. Its relation to Wiesbrock-type half-sided modular inclusions is not derived. This is a candidate
    follow-up correction or derivation.
  - (b) A derivation of the δΘ error estimate needs a bound on the relative modular generator, e.g. a
    Connes-cocycle estimate on the double-cone or wedge algebra, in terms of δΘ.
  - (c) The diamond identification for the massive modes: follow avenues 2, 3, 1, 4 above.

## Special instructions for the gatekeeper

- Re-check the BW content against the preprint (eScholarship 0sf4t33q). The key items are Theorem 1(c)–(d), eqs.
  (45b)–(45d) and (46c), on preprint pp. (33)–(34); Section V (wedges) and Section VI (double cones via wedge
  algebras, duality only).
- Hislop–Longo is verified at the record/abstract level only.
- Must not be asserted:
  - that massive diamond modular flow is non-geometric (only "not used here / not established");
  - that the δΘ estimate is false (it is unproved);
  - any status change.
- Full-scan question: the edits change neither a definition, an assumption, a scope statement nor a status
  passage. They correct a cited-theorem range inside an evidence paragraph of the Problem A ledger section. E1/E6
  narrow what the lemma claims. If you classify that narrowing as a scope statement, a full scan is required
  before ACCEPT.
- Integration ordinal: 64.
- Re-run: `python -I proposals/066-bw-diamond-scope-correction/apply_check_066.py <repo> <outdir-outside-repo>`.

## Build result

Scratch build (copy outside the repo with both patched files; pdflatex, bibtex, pdflatex, pdflatex): all exit codes 0, 0 bibtex warnings, no undefined or multiply-defined references or citations in the final log, `HislopLongo1982` present in the .bbl, 380 pages. Output in `scratch_build_066_output.txt`. The scratch build copy is left in the session scratchpad (no rm -rf was run).
