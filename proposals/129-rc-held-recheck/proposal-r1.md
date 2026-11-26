# Proposal 129-rc-held-recheck, round 1

## Result

Independent re-derivation of the eight held blocks from `reports/rc-parallel-apph-blocks-2026-11-25.md`
(items 068-076) against our live appH (pin dee9a4174b81, 883,075 B, 4,146 lines). One block (48) survives as a
conditional-manuscript addition, recorded in a single payload: two new paragraphs inserted in the Problem F
"Explicit \(K\)." region. Headline results, all re-derived here (not imported):

1. **Gauge-free shift identity (established).** At \(X^i=\chi J^i\) on \(S^2_N\), the difference of the quadratic
   forms of the matrix-model action with and without the cubic term is exactly \(\tfrac12(c_3/\chi)\chi^2\mathsf{SO}\),
   \((\mathsf{SO}A)^i=-\epsilon_{kij}\mathrm i[J^k,A^j]\), residual \(<1.5\times10^{-13}\) for \(N=2..5\),
   \((\chi,c)\in\{(1,\pm),(2,2),(1,\tfrac23),(1,-\tfrac12),(1,1.5)\}\). The cubic term changes only the spin-orbit
   coefficient \(2\mathsf{S\cdot L}\to\kappa_3\mathsf{S\cdot L}\), independently of any gauge fixing; combined with
   OUR integrated L3194 \(c_3=0\) anchor, the held operator statement \(H_V^K=\chi^2(L^2-\kappa_3\mathsf{S\cdot L})\)
   becomes conditional only on that anchor.
2. **Branch spectrum bookkeeping (established).** Spectrum \(\chi^2(l(l+1)-\kappa_3l)^{(2l+3)}\),
   \(\chi^2(l(l+1)+\kappa_3)^{(2l+1)}\), \(\chi^2(l(l+1)+\kappa_3(l+1))^{(2l-1)}\), \(l=1..N-1\), total \(3(N^2-1)\);
   no negative mode iff \(-1\le\kappa_3\le2\); \(\kappa_3=-2\) carries mode \(-2\chi^2\) at \((l,j)=(1,0)\);
   \(\kappa_3=2\) reproduces our integrated vector spectrum \(l(l-1),\ l(l+1)+2,\ (l+1)(l+2)\).
3. **Tree-curve algebra (established) + bounded no-go (conditional on one supplied weight input).**
   \(\beta_K=2(r_3-1)/(4-3r_3+\delta)\); \(\beta_K=1\Leftrightarrow r_3=(6+\delta)/5\); \(\beta_K|_{\kappa_3=-2}=2/(\delta-2)\).
   WITH the supplied large-\(N\) weight input \(\hat V/\hat T\to\kappa_3^2/4\): no stationary point of the cubic branch
   has \(\hat V=\hat T\) and no negative mode (\(\hat V=\hat T\Leftrightarrow r_3\in\{0,2\}\); \(r_3=0\) is \(c_3=0\),
   \(r_3=2\) leaves the window).
4. **The live L3194 example lies on the cubic branch** with \(r_3\simeq1.168\), \(\kappa_3\simeq-0.336\) (inside the
   window), \(\delta\simeq-0.159\), and its quoted \(\beta_K=1\) is exactly \(2\cdot5.34/10.68\) (all values recomputed
   from the live supplied numbers \(7.935\), \(-12.36\), \(10.68\)).

A second-moment arithmetic error in my own session-1 notes was corrected: \(\sum_{l}\!(2l+3)l^2+(2l+1)+(2l-1)(l+1)^2
= N^2(N^2-1)\) exactly (the held factor IS reproduced); the per-\(l\) cross term vanishes identically.

## Target and status

- Problem F (appH ledger section "Problem F", F-area paragraphs on \(K\), explicit-\(K\) spectrum and scale
  dependence). Current status as read live: OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL (ch17 full-GR criterion
  includes F). Original target: the \(q=0\)/static scalar-channel data of the fluctuation operator on \(K\) feeding
  the \(\beta_K\)/rigidity derivation. Dependencies of this package: the integrated L3194 explicit-\(K\) paragraph
  (anchor), L3152-3173 \(\beta_K\) recording, eq:Smatrix, def:matrix-coords-ext.
- Classification: **PROGRAMME-CONDITIONAL evidence package.** Closes nothing. Adds derived branch data to an OPEN
  critical-path problem; no status/priority/completion label is touched.
- Held-block dispositions (per dispatch):
  | block | verdict | reason |
  |---|---|---|
  | 22 (Problem C "Missing step." rewording) | SUPERSEDED | our live L762 is newer, has (i)-(iii) + F-obstruction cross-ref; held text is the older variant |
  | 48 ¶1 (cubic Hessian) | ADOPT-MODIFY -> payload-F ¶1 | shift identity + bookkeeping re-derived; conditional only on our own integrated anchor |
  | 48 ¶2 (tadpole/\(\theta\)) | SUPERSEDED / NOT-FOR-MANUSCRIPT | pure-trace channel duplicates our newer integrated L3220/L3222 |
  | 48 ¶3 + 49/50/51 (tree non-derivative, singlet, \(C_{\rm tree}\)) | NOT payloaded (conditional) | localisation identity verified only at \(L=-\Box\) level; \(C_{\rm tree}\) coefficient and explicit 4x4 realisation not reproduced; live L3212 "not computed" sentence stays |
  | 42 (TT dispersion) | NOT-FOR-MANUSCRIPT | \(v^2,\mu^2\) inputs in held text; \(\rho_M\to\) dark energy needs \(G_N\) connection; no derivation-grade input |
  | 27 (E-relaxations + compact toy) | NOT-FOR-MANUSCRIPT | hedged conditionals concluding D,E,F,N open; unverified refs; toy duplicates our reviewed text in diverged form |
  | 28 (Heisenberg cones) | NOT-FOR-MANUSCRIPT (future candidate) | coherent but reproduction pack not reconstructible from our manuscript; same-conclusion extension, ranked BELOW F-area follow-ups |

## Source reading

digest + targeted reads. scratch/digest.md (DIGEST CURRENT per dispatch; appH pin dee9a4174b81). Read in full:
appH L3150-3200 (beta_K paragraph, Explicit K, Scale dependence), appH L755-770 (Problem C),
`reports/rc-parallel-apph-blocks-2026-11-25.md` blocks 22/27/28/42/48/49/50/51,
`reports/rc-import-review-2026-11-25.md`, `proposals/claude-remote-late/README.md`, ch17 F-criterion passages,
MILESTONE.md. Grep-verified: `c_3` only at appH L1720-1738 (U(4) potential, no F-area clash; payload adds a
disambiguation clause); `r_3`/`\kappa_3` absent from appH (no duplication); `\emph{Scale dependence}` count 1;
anchor tail count 1; labels eq:Smatrix, def:matrix-coords-ext exist. Item 128 (paused, ~L3224), E.thimble and
C.operator passages are NOT touched, quoted, or depended on.

## Research and reasoning

Model \(S(X)=-\tfrac14\mathrm{tr}[X^i,X^j]^2+\tfrac{\mathrm i c}{3}\epsilon\,\mathrm{tr}XXX\), \(X=\chi J\), \(J\) spin
\((N-1)/2\). Convention gate: \(a_3/a_4=-2/3\) fixes \(c_3=-\tfrac32(a_3c)/(a_4\chi)\chi\)... precisely
\(V=a_4\chi^4+a_3c\,\chi^3=\bar a(\chi^4-\tfrac23c_3\chi^3)\Rightarrow c_3/\chi=-\tfrac32(a_3c)/(a_4\chi)\),
\(\kappa_3=2-c_3/\chi\).

- Shift identity: extracted the EXACT quadratic part by even-part interpolation
  \((16E(1)-E(2)-15E(0))/24\) (exact for the quartic polynomial), polarised, and compared \(c\) vs \(c=0\) bilinear
  forms; residual 3e-15..1.4e-13. The operator \(\mathsf{SO}\) is real symmetric on the Hermitian ONB (single ad is
  anti-Hermitian-valued, hence the i), spectrum \(\{l^{(2l+3)},(-1)^{(2l+1)},(-(l+1))^{(2l-1)}\}\) + 3 trace zeros
  (verified \(N=2..4\)).
- Why an earlier full-spectrum match attempt failed and is not needed: the live L3194 anchor is the FLUX operator
  (\(\Lambda^i=J^i\)); a flux-free Hessian has kernel \(\{0^{\times8},2^{\times3},6\}\) at \(N=2,\chi=1,c=0\) and cannot
  test the anchored \(c=0\) spectrum. The shift identity is gauge-free, so only the anchor is imported - and it is our
  own integrated text.
- Tree curve: sympy identities I1-I10 (script), including \(\beta_K=-2\partial_{\ln\chi}(\rho_MV_t/g^2)/U_{\chi\chi}\)
  (live L3171 value) rewritten as \(2(r_3-1)/(4-3r_3+\delta)\) with \(\delta\) defined by
  \(U_{\chi\chi}=4\tilde U(4-3r_3+\delta)\). Example: \(c_3/\chi=1.5\cdot12.36/7.935=2.33648\Rightarrow r_3=1.168242\),
  \(\kappa_3=-0.336484\), tree slope \(4\tilde U(1-r_3)=-5.34\Rightarrow\beta_K=2\cdot5.34/10.68=1.0000\);
  \(\delta=5r_3-6\simeq-0.159\) reproduces \(U_{\chi\chi}=10.68\) exactly
  (\(4\tilde U(4-3r_3+\delta)=10.68\)).
- Bounded no-go (conditional on \(\hat V/\hat T\to\kappa_3^2/4\)): \(c_3\ne0\Rightarrow r_3>0\); no-negative-mode
  \(\Rightarrow r_3\le3/2\); \(\hat V=\hat T\Rightarrow r_3\in\{0,2\}\) \(\Rightarrow\) empty intersection. \(\beta_K=1\) and
  \(\hat V=\hat T\) simultaneously needs \(r_3=2\) (negative mode) or \(\delta=-6\) (outside one-loop validity). Stated
  within its hypotheses only.
- Transfers to work order B: item 075's NEEDS-EVIDENCE objection (cubic/Hessian) is resolved by (1)-(2) above; our
  evidence is strictly stronger than the held numerical-Hessian claim because ours pins the anchor as integrated text.

Literature checked: arXiv hep-th/0101102 (Iso-Kimura-Tanaka-Wakatsuki, "Noncommutative Gauge Theory on Fuzzy Sphere
from Matrix Model", Nucl. Phys. B604 (2001) 121-147, DOI 10.1016/S0550-3213(01)00173-0) - arXiv record fetched and
verified; DOI resolves to PII S0550321301001730 (Elsevier landing page itself not fetched). **NOT cited in the payload**
(no derivation in it depends on it); BibTeX supplied below for an optional author/integrator addition. Held-report
citations (HoKawaiSteinacker2025, Chatzistavrakidis2011, IsonoTomino2010, Liao2026, Bertotti2003): NOT verified and
NOT used (their payloads are not proposed).

## Claim classification

- established (this package, scripts): shift identity (numerically exact, N<=5); SO spectrum + multiplicities;
  branch bookkeeping, no-negative-mode window, \(\kappa_3=-2\) mode, \(\kappa_3=2\) anchor match; tree-curve identities
  I1-I10; example arithmetic (\(r_3,\kappa_3,\delta,\beta_K\)); corrected second moment \(N^2(N^2-1)\) and vanishing
  cross term; algebra \((\kappa_3^2-4)\chi^4=c_3^2\chi^2-4c_3\chi^3\).
- conditional: full operator identity \(H_V^K=\chi^2(L^2-\kappa_3\mathsf{S\cdot L})\) beyond the shift (on our L3194
  anchor + same-reduction statement); \(\hat V/\hat T\to\kappa_3^2/4\) and \(\hat V/\hat T=(1-r_3)^2\) (supplied weight
  input, not recomputed); bounded no-go (on that input); \(\beta_K\) value itself is the recorded (not derived)
  quantity of L3152-3173.
- input (phenomenological/supplied): tree cubic on \(K\) ("supplied there" per live L3173 and def:matrix-coords-ext);
  example tree values 7.935/-12.36/10.68 (live L3194).
- conjecture/mechanism: none originated.
- unresolved: one-loop curvature \(\delta\) as a computed quantity; response of the one-loop density beyond
  \(\sqrt{|g|}\); spinor/ghost supertrace bookkeeping of the full \(\sum w\lambda^2\) identity; regulated
  \(\mathcal U\) signs (NOT payloaded).

## Proposed changes

### chapters/appH-microscopic-proofs.tex (one insertion)

Anchor (occurs exactly once, verified; tail of the "Explicit \(K\)." paragraph, live line 3194):

    On this evidence the sign of \(\hat U\) depends on \(K\).

Boundary: the next paragraph starts (unique in file, live line 3196) `\emph{Scale dependence.}`. Insert the fenced
block between them (after the blank line). Everything in both anchor paragraphs stays untouched. No \ref/\label added
(only the pre-existing `\eqref{eq:Smatrix}`). Payload adds no citation (bib-key issue avoided; see Author decision).

payload-F.tex (full text, also stored at `proposals/129-rc-held-recheck/payload-F.tex`, CRLF+ASCII, 3147 B; text below is the r2-corrected payload, byte-identical to payload-F.tex on disk; r1 as-submitted values are recorded in review-r1.md):

```latex
\emph{Tree stabiliser on \(K\) with a tree cubic term.} Read the cubic term of Equation~\eqref{eq:Smatrix} on the flux directions of \(K\), specialised there to \(C_{ijk}=\mathrm i c_3\epsilon_{ijk}/g^2\) on the flux directions with constant \(c_3\) (a coupling label local to these two paragraphs, not the quartic-potential \(c_3\) of the \(U(4)\) discussion), and write \(V_{\mathrm t}=\bar a(\chi^4-\tfrac23c_3\chi^3)\), \(r_3=c_3/2\chi\), \(\kappa_3=2-c_3/\chi=2(1-r_3)\). The tree part is stationary at \(\chi=c_3/2\) and convex there, \(\partial^2_{\ln\chi}(\rho_MV_{\mathrm t}/g^2)=4\tilde U(4-3r_3)>0\). At \(X^i=\chi J^i\) on \(S^2_N\), with \(J^i\) the spin-\((N-1)/2\) generators, the difference of the quadratic forms of the quartic and cubic terms at \(c_3\) and at \(c_3=0\) is exactly \(\tfrac12(c_3/\chi)\,\chi^2\) times the real symmetric operator \((\mathsf{SO}\,A)^i=-\epsilon_{kij}\mathrm i[J^k,A^j]\); this is an identity between two unfixed quadratic forms, checked at \(N\le5\) with residual below \(1.5\times10^{-13}\). In the same reduction of the fluctuation operator that gives the vector spectrum of the preceding paragraph, the cubic term therefore changes only the spin-orbit coefficient, and the vector spectrum becomes \(\chi^2(l(l+1)-\kappa_3l)\), \(\chi^2(l(l+1)+\kappa_3)\), \(\chi^2(l(l+1)+\kappa_3(l+1))\) with multiplicities \(2l+3\), \(2l+1\), \(2l-1\) over \(l=1,\dots,N-1\), of total \(3(N^2-1)\); at \(\kappa_3=2\) it is the vector spectrum of the preceding paragraph, and the spinor and ghost parts being unchanged, there is no negative mode exactly for \(-1\le\kappa_3\le2\) (at \(\kappa_3=-2\) the mode \(-2\chi^2\) appears). The supplied example of the preceding paragraph lies on this branch with \(c_3/\chi\simeq2.34\) and \(\kappa_3\simeq-0.336\), inside the window.

\emph{The tree curve of the cubic branch.} Write \(U_{\chi\chi}=4\tilde U(4-3r_3+\delta)\) at a stationary point of the branch, which defines \(\delta\). With \(\partial_{\ln\chi}(\rho_MV_{\mathrm t}/g^2)=4\tilde U(1-r_3)\), the value \(\beta_K=-2\partial_{\ln\chi}(\rho_MV_{\mathrm t}/g^2)/U_{\chi\chi}\) recorded above reads \(\beta_K=2(r_3-1)/(4-3r_3+\delta)\) on the branch; \(\beta_K=1\) is equivalent to \(r_3=(6+\delta)/5\), and at \(\kappa_3=-2\) one has \(\beta_K=2/(\delta-2)\). In the units of the example of the preceding paragraph its supplied values give \(r_3\simeq1.168\), \(\kappa_3\simeq-0.336\), \(\delta\simeq-0.159\) and \(\beta_K\simeq2\cdot5.34/10.68\simeq1.000\), a restatement of the value quoted there. If in addition the large-\(N\) weights on this branch give \(\hat V/\hat T\to\kappa_3^2/4\) (supplied, not recomputed here), then at a stationary point \(\hat V/\hat T=(1-r_3)^2\), so \(\hat V=\hat T\) requires \(r_3=0\) or \(r_3=2\): the first is \(c_3=0\), the second leaves the window of no negative modes. On that input no stationary point of the cubic branch has \(\hat V=\hat T\) with no negative mode, and the example has \(\hat V/\hat T\simeq0.028\). The one-loop curvature \(\delta\), the weight ratio, and the response of the one-loop density beyond \(\sqrt{|g|}\) are not computed here.
```

Consistency with `\beta_K=-1/(1+\varepsilon-Y/4\tilde U)` (L3173, pure quartic) and the live example sentence is by
construction (r3-form of the same recorded identity; verified numerically). Stale passages elsewhere: none - no live
text contradicts the payload (it sits between the two anchor paragraphs and repeats no claim with different content).

Deliberately NOT payloaded (with reasons): block 48 ¶2 (duplicates newer integrated text); 48 ¶3/49-51 singlet-sector
items (\(C_{\rm tree}\) coefficient not reproduced; live "not computed" stays); the completed-square exchange
(\(\sigma_1\)-coupling coefficient \(\tfrac12U'_{\rm loop}\) not derived from our live contact structure);
\(\varrho=(V+2T)/3V\) (not a live-text symbol); the full \(\sum w\lambda^2\) identity and \(\mathcal U\)-sign claims
(supertrace bookkeeping not reverified); the held report's "not stationary without counterterms" admission (their
one-loop numerics not reproduced - recorded here, not in manuscript); block 42/22/27/28 dispositions as tabled.

BibTeX (OPTIONAL, not used by the payload; verify+add only if the author wants the citation):

    @article{IsoKimuraTanakaWakatsuki2001,
      author  = "Iso, S. and Kimura, Y. and Tanaka, K. and Wakatsuki, K.",
      title  = {{Noncommutative Gauge Theory on Fuzzy Sphere from Matrix Model}},
      journal = {Nucl. Phys. B},
      volume  = {604},
      pages   = {121--147},
      year    = {2001},
      doi     = {10.1016/S0550-3213(01)00173-0},
      eprint  = {hep-th/0101102}
    }

## Verification scripts

All under `proposals/129-rc-held-recheck/`; run from the repository root. Reproduction pack:

- `python -I proposals/129-rc-held-recheck/verify_hessian_129.py`
  -> last line `HESSIAN_129 PASS`; invariants: `a3/a4 = -0.666667`; all shift residuals < 1e-8 (observed 3e-15..1.4e-13);
  SO spectrum multiset match N=2..4; `kappa3=-2: minimum branch = -2.000`; kappa3=2 anchor values; multiplicities
  \(3(N^2-1)\) N=2..7.
- `python -I proposals/129-rc-held-recheck/verify_treecurve_129.py` -> last line `TREECURVE_129 PASS` (sympy asserts
  I1-I10: slopes \(4\tilde U(1-r_3)\), \(4\tilde U(4-3r_3)\); beta formula; \(r_3=(6+\delta)/5\); \(2/(\delta-2)\);
  \((1-r_3)^2=\kappa_3^2/4\); \(V=T\Leftrightarrow r_3\in\{0,2\}\); limits; eliminated coefficient).
- `python -I proposals/129-rc-held-recheck/verify_example_129.py` -> last line `EXAMPLE_129 PASS`; invariants
  \(r_3=1.168242\), \(\kappa_3=-0.336484\), \(V/T=0.028305\), tree slope 5.3400, slope ratio 0.168242,
  \(\beta_K=2\cdot5.34/10.68=1.0000\), \(4\tilde U(4-3r_3+\delta)=10.68\) at \(\delta=5r_3-6\).
- `python -I proposals/129-rc-held-recheck/verify_weights_129.py` -> last line `WEIGHTS_129 PASS (...)`; invariants
  \(\sum=3(N^2-1)\), \(\sum\mu^2=N^2(N^2-1)\) exactly, per-\(l\) cross term 0, \((\kappa_3^2-4)\chi^4\) algebra.
- `python -I proposals/129-rc-held-recheck/cert_129.py` -> last line `CERT129 PASS (exit 0, undefined refs/citations = 0)`;
  splices payload-F.tex into a temp-dir copy of appH OUTSIDE the repository (anchor/join asserts), runs
  pdflatex-bibtex-pdflatex-pdflatex -halt-on-error on a full copy (chapters, frontmatter, bib, figs, namcg-book7.tex),
  prints `pages = 450, undefined refs/citations = 0, multiply-defined = 0`, then deletes the scratch.

**Compile certificate (executed 2026-11-26): CERT129 PASS** - two+ two-pass builds exit 0, 450 pages, zero undefined
references/citations, zero multiply-defined; splice pre 883,075 B -> post 886,190 B = payload 3,113 B + 2 B join CRLF;
scratch deleted by the script. No scratch build inside the repository.

## Decisions Taken

- Reconstructed the payload around OUR recorded \(\beta_K\) identity (L3171) instead of the held \(U'_{\rm loop}/L\)
  notation: fewer new symbols, no dependence on undefined live objects, keeps every payload quantity live-traceable.
- Dropped from the payload the completed-square exchange and \(\varrho\) ratio (coefficients/couplings not derivable
  from the live text without touching the paused L3224 region's neighbourhood); kept the no-go, which is the
  derivation-grade output.
- No \cite in the payload although IKTW is verified, because the bib key is missing from bib/namcg.bib and I may not
  edit bib/: the payload compiles with zero undefined citations; the citation is optional author/integrator follow-up.
- Work order B recorded as NOT-FOR-MANUSCRIPT (blocks 27/28) rather than forcing marginal text: their only plausible
  manuscript effect would be same-conclusion hedging (deprioritized per derivation-first directive); open avenues
  ranked below F-area follow-ups. Full ranked avenue list: (1) recompute \(\hat V/\hat T\) weights on the cubic branch
  from exact spectra (removes the last conditionality in the no-go) - POSITIVE-aimed; (2) compute the \(\sigma_1\)
  coupling coefficient to restore the exchange paragraph - POSITIVE-aimed; (3) spinor/ghost supertrace for
  \(\sum w\lambda^2\); (4) reproduce IKTW-style \(C_{\rm tree}\) (49-51); (5) Heisenberg cone reproduction (28);
  (6) E-relaxations package (27) - these last are same-conclusion extensions unless gaps appear.
- Block 22 SUPERSEDED verified against live L762 (no payload).

## Milestone assessment

Routine. No MILESTONE.md trigger: no critical-path step is closed; a conditional evidence package is added to the
OPEN Problem F entry area.

## Status-label recommendation

Critical-path set re-derived from ch17/appH: A, B, C, D1, E, F, G-derived, N (OPEN, CRITICAL PATH). All labels
UNCHANGED. This package does not close Problem F (the weight input, \(\delta\), and the non-\(\sqrt{|g|}\) response
stay open).

## Author decision needed

- Bib key `IsoKimuraTanakaWakatsuki2001` is absent from bib/namcg.bib (verified by grep). The payload does not need it;
  add the supplied BibTeX only if a citation is wanted. (No other author decision: no label, scope or core change.)

## Remaining open step

To close the ORIGINAL Problem-F use of these paragraphs: (i) derive \(\hat V/\hat T\to\kappa_3^2/4\) (or a corrected
weight ratio) on the cubic branch from exact spectra (the vector-content factor \(N^2(N^2-1)\) and cross-term
vanishing are already established here; spinor/ghost supertrace bookkeeping remains); (ii) compute \(\delta\) (the
one-loop curvature) and the one-loop density response beyond \(\sqrt{|g|}\), which the live \(\beta_K\) recording
assumes; (iii) verify the same-reduction statement for the \(c_3\ne0\) operator against a flux-anchored gauge-fixed
Hessian at finite N. Until then every payload sentence retains its stated conditions and Problem F stays OPEN.

## Special instructions for the gatekeeper

- Scope: only the two-paragraph insertion between the quoted anchor tail (L3194) and the unique
  `\emph{Scale dependence.}` (L3196); anchors must be re-quoted against the live tree (another chain may have moved
  text). Do NOT let the payload text be asserted unconditionally: the shift identity is established N<=5 numerically,
  the operator extension is conditional on the L3194 anchor/same-reduction clause, and every \(\hat V/\hat T\) and
  no-go statement is conditional on the supplied weight input.
- Re-check: (a) the shift identity's factor \(\tfrac12(c_3/\chi)\chi^2\) against the script's
  `2(G(c)-G(0))=(c3/chi)chi^2 SO`; (b) \(\kappa_3=2\) anchor match with the live L3194 spectrum sentence;
  (c) example values from the live numbers only; (d) the second-moment CORRECTION (held factor N^2(N^2-1) IS
  reproduced; session-1 note said otherwise - check verify_weights_129.py, not the journal); (e) re-run all four
  verify scripts + cert_129.py.
- Never run `proposals/123-f-coeff-locked-block/verify_ghost_op_123.py` (author kill-order). Do not evaluate or cite
  the paused appH regulated/Lorentzian passage near L3224, E.thimble lines, or C.operator HOLD material; this
  package does not touch them. Their gatekeeper verdicts have zero authority (CLAUDE rule 6); the held blocks were
  used as prior art only. Their IKTW-type citations and the 27/28 references were NOT verified here and none entered
  the payload.
