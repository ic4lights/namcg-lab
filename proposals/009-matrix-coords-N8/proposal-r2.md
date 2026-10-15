# Proposal 009-matrix-coords-N8, round 2

## Changelog against r1 (review-r1: ACCEPT WITH REQUIRED REVISIONS, M5, OPEN 0/3)

| Finding | Action in r2 |
|---|---|
| F1 (major) duplicate no-go | The "Operator metric versus induced metric" proof paragraph is deleted and replaced by the review's one-sentence cross-reference (D-independence; Euclidean contrast with G Euclidean). Result item 1 no longer claims a new no-go (M2 withdrawn). |
| F2 (major) N_tot | The N_tot = D-2 sentence and r1 Result item 4 are dropped. Kept: the D-4 transverse scalars are not covered by `ass:locked-block` and are extra infrared fields unless gapped. |
| F3 (major) literature | Extra-dimension and Newton-constant statements attributed only to `Steinacker2023`; "extra tensors" only to `KumarSteinacker2023`, `Steinacker2026`. Leaf dimension > 4 is phrased as a relaxation available in this package's class, not as a property of those papers. BibTeX unchanged (verified in review-r1). |
| F4 (minor) definition | (i) `\rho=1/|\operatorname{Pf}\theta|` defined; (ii) the "K^{-1} not proportional to g" sentence now states the exact hypothesis class and points to the merged 008 paragraph of Appendix `app:status`, no longer to `rem:ch3-moyal-check`; (iii) "read with I,J" restricted to the quartic and matter terms (cubic term excluded); "reduces, for D = 4, to". |
| F5 (minor) ch03 anchor | Moved to the end of the paragraph ending "The existence of such a map is enough for now.", before `\section{Presentation B...}`. `verify_anchors_labels.py` updated and re-run: count 1; `eq:Smatrix` precedes the anchor. |
| F6 (minor) contrast | The (2,2) contrast is dropped (a pull-back of a form with one negative eigenvalue has at most one). Hypotheses of the no-go stated; the within-core route is to relax the leaf dimension. |
| F7 (minor) linear response | Factor i absorbed in xi; `xi ∝ theta^T p`; "exactly three for every D"; generic-rank logic stated (exact upper bound; lower bound one exact-rational draw, generic by lower semicontinuity). |
| F8 (minor) closing | Closing sentence replaced by "This changes no ledger label; Problem~F remains open." |

Unchanged from r1: `check_conformal_nogo.py` and `check_brane_rank.py` and their outputs (no input changed; the gatekeeper re-ran the rank script and reproduced the table). Only `verify_anchors_labels.py` changed and was re-run.

## Result

Target: give the "more than four matrix coordinates" setting of proposal 008 a labelled conditional home (`def:matrix-coords-ext`) and record in one appH paragraph its kinematic linear-response content. It derives nothing on the critical path. Hypothesis class H_D: D Hermitian matrices, Poisson limit, 4-dimensional real symplectic leaf, constant Lorentzian `eta_IJ`, real induced `g`, frozen background at a point (WKB), generic momentum.

1. **Relation to the merged 008 result.** The non-proportionality `G != c g` for every D >= 4 is already in the merged 008 paragraph. It uses only the real 4-dimensional leaf and the real Lorentzian `g`, so it is independent of D. A Euclidean `g` admits `G ∝ g`, but then `G` is Euclidean. The within-core route to remove the obstruction is to relax the leaf dimension. This package adds only the cross-reference. (The 008 proposal-level sentence that N >= 8 "removes both obstructions" is superseded; it is not manuscript text.)
2. **Linear response.** About a flat brane (constant `theta`, `II = 0`) the rank of the linearised Einstein operator of `G` on the image of the embedding fluctuations is exactly 3 for every D (normal modes do not enter `delta g` at first order, so the image is the D = 4 image). About a brane with generic second fundamental forms `II` the rank is `min(6, D-1)`: the upper bound is exact; the lower bound is one exact-rational draw for each D = 4..11, generic by lower semicontinuity; also with the normal part `K^{mu nu} II^i_{mu nu} = 0`. All six conserved sources are reachable from D = 7. Counting the density scalar, D-1 >= 7 (D >= 8) is a necessary count only. All kinematic; no Einstein-type field equation for `G` is derived.
3. **Content.** The D-4 transverse coordinates are not covered by `ass:locked-block`; they are extra infrared fields unless gapped. If gapped and decoupled, the flat-brane rank 3 returns.
4. **Literature (abstract level only).** One-loop IKKT work with compact fuzzy extra dimensions reports an induced Einstein-Hilbert term with the Newton constant set by the KK scale (`Steinacker2023`); modified Einstein equations with extra tensors are reported in `KumarSteinacker2023`, `Steinacker2026`. Not checked against the present operators.

Not established: any field equation for `G`; gap of the transverse scalars; the dictionary `Phi <-> tangent-plane frame`; any extra conserved stress; any `G_eff`.

## Target and status

Problems A, D1, E (by dependency), F (primary: `ass:emergent-op`); B, C by dependency. Appendix H: A "OPEN; CRITICAL PATH for the matrix-derived label; PROGRAMME-CONDITIONAL"; D, F "OPEN; CRITICAL PATH; PROGRAMME-CONDITIONAL"; E "OPEN; CRITICAL PATH for the matrix-derived label; PROGRAMME-CONDITIONAL" (quoted verbatim in review-r1, still current after the 008 and 010 integrations). Chapter 17 `sec:ch17-done` lists A, B, C, D1, E, F, G-derived, N; no discrepancy. Original target (F): discharge `ass:emergent-op` or replace it by a derived ingredient. Not met. PROGRAMME-CONDITIONAL.

## Source reading

Full scan of all 30 chapter files was done in r1 and by the gatekeeper in review-r1 (CLAUDE.md 3(c)); the 010 integration (ch09, appK) was checked by diff in the review and does not touch ch03 or appH. For r2: digest CURRENT (chapters-hash fc4f4857691baf87, per the orchestrator); targeted reads of ch03 lines 143-172 (`eq:Smatrix`, new anchor), the integrated 008 paragraph in appH (line 1822, "Metric seen by the operators") and the paragraph's final sentence. Anchor and label counts re-run by script.

## Research and reasoning

**Setting.** `x^I(y)` on a 4-manifold with nondegenerate Poisson bivector `theta`; `Theta^{IJ} = theta^{ab} d_a x^I d_b x^J`; `g = dx^T eta dx`; `K = theta^T g theta`; `G = K^{-1} = omega g^{-1} omega^T`, `omega = theta^{-1}`. For D = 4, `x^I = y^I`, `g = eta`.

**No-go (cross-reference only).** With `M = g^{-1} omega`: `G = -g M^2`, `det M = Pf(omega)^2/det g < 0`. `G = c g` needs `M^2 = -c` with `c > 0`, and a real 4x4 `M` with `M^2 = -c` has `det M = c^2 > 0`: contradiction. The merged 008 text makes the same point through the characteristic polynomial of `N = theta g`. The manuscript text of this package contains only the cross-reference sentence. `check_conformal_nogo.py` (r1, unchanged) verifies the identities in exact rationals for random Lorentzian `g`, D = 4..11.

**Linear response.** In a chart with constant `theta`, `delta x^I = A^I e^{i p.y}`, `A = xi^mu d_mu x + phi_i n^i` (factor i absorbed in `xi`). Then `delta g = p (.) (g xi) - 2 phi_i II^i` with `a (.) b = a b^T + b a^T`, and `delta G = -G theta^T delta g theta G`. The Hamiltonian choice `xi ∝ theta^T p` gives `delta G = p (.) (G xi)`, a linearised `G`-diffeomorphism. Rank logic: the image contains the gauge direction, and the Einstein operator annihilates `Diff_G` (4-dim), so rank <= D-1; the image lies in the 6-dimensional space of conserved tensors, so rank <= 6. Both bounds are exact. Flat brane: exactly 3 for every D. Generic `II`: one exact-rational draw at full rank `min(6, D-1)` is sufficient since rank is lower semicontinuous in polynomial data (`check_brane_rank.py`; the gatekeeper reproduced the table, and with independent numpy draws). Caveats: frozen coefficients (WKB, consistent once normal amplitudes are rescaled `phi ~ p xi`), Gauss-Codazzi not imposed, generic `p`.

**Frames.** The tangent-plane frame redundancy is `SO(3,1)` and the stabiliser in `SO(1,D-1)` is `SO(1,3) x SO(D-4)`: a global-symmetry/frame remark, not a derivation of local gauge symmetry. It is not put in the manuscript text of r2. `Phi <-> eps` remains a conjecture.

**Literature checked** (arXiv abstract pages, 2026-10-14, re-fetched by the gatekeeper): arXiv:2303.08012 (key `Steinacker2023`, existing); arXiv:2312.01317 (Kumar, Steinacker); arXiv:2601.08031 (Steinacker). Only abstract-level content is used. Full texts not read; the leaf dimension of the latter two is not verified.

## Claim classification

- Established (exact algebra; already merged via 008): `G != c g`, D-independent, in H_D.
- Established: rank upper bounds and the flat value 3 (exact). Established by exact-rational sample plus semicontinuity: generic lower bound `min(6, D-1)` for D = 4..11 in the frozen-WKB, Gauss-Codazzi-free class.
- Counting (necessary only): D-1 >= 7 with the density scalar.
- Conditional: the semiclassical reading in `def:matrix-coords-ext`; the transverse-scalar content statement.
- Conjecture: leaf dimension > 4 removes the `G`-versus-`g` obstruction; correspondence with one-loop extra tensors; `Phi <-> eps`.
- Unresolved: Einstein-type field equation for `G`; gap of transverse scalars; extra conserved stress; E; D1 dynamics; `G_eff`.

## Proposed changes

No label, priority, completion classification or Chapter 17 text is touched. Spacetime and metric stay emergent: `eta_IJ` contracts matrix indices only.

**File 1: `chapters/ch03-matrix-action.tex`.** Anchor (occurs once, verified): the end of the paragraph "...in Chapter~14. The existence of such a map is enough for now." followed by a blank line and `\section{Presentation B: the covariant condensate action}`. Insert the block between them; nothing replaced; `eq:Smatrix` (line 143) precedes it. Labels verified once: `def:matrix-coords`, `eq:Smatrix`, `ass:lorentzian`, `ass:locked-block`, `eq:g-from-e`, `ass:emergent-op`, `app:status`; `def:matrix-coords-ext` is new (count 0).

```latex
\begin{definition}[Extended matrix coordinates (conditional extension)]
  \label{def:matrix-coords-ext}
  Let \(D\ge4\) and let \(\hat X^I\), \(I=0,\dots,D-1\), be Hermitian
  operators on \(\mathcal{H}\) with
  \([\hat X^I,\hat X^J]=i\Theta^{IJ}\), \(\Theta^{IJ}=-\Theta^{JI}\).
  Matrix indices are contracted with the fixed constant form
  \(\eta_{IJ}=\mathrm{diag}(-1,1,\dots,1)\), exactly as \(\eta_{\mu\nu}\)
  is used in the first (quartic) term and in the matter term
  of~\eqref{eq:Smatrix}, read with \(I,J\) in place of \(\mu,\nu\); the
  cubic term is not extended here. The definition reduces, for \(D=4\),
  to Definition~\ref{def:matrix-coords}.
  In the semiclassical regime a configuration is a map \(y\mapsto x^I(y)\)
  from a four-dimensional manifold carrying a nondegenerate Poisson
  bivector \(\theta^{\alpha\beta}\), with
  \(\Theta^{IJ}=\theta^{\alpha\beta}\partial_\alpha x^I\partial_\beta x^J\)
  and \(\operatorname{Tr}\to\int\mathrm{d}^4y\,\rho\), where
  \(\rho=1/|\operatorname{Pf}\theta|\). Two tensors are
  then defined from the configuration, not from the action: the induced
  tensor \(g_{\alpha\beta}=\eta_{IJ}\partial_\alpha x^I\partial_\beta x^J\)
  and the operator tensor
  \(K^{\mu\nu}=\theta^{\alpha\mu}g_{\alpha\beta}\theta^{\beta\nu}\), which
  is the kinetic tensor of a fluctuation \([\hat X^I,\cdot\,]\) in the
  Poisson limit. This definition adds no fundamental metric: the form
  \(\eta_{IJ}\) contracts matrix indices only, and its Lorentzian
  signature is retained as Assumption~\ref{ass:lorentzian}. The index
  \(I\) of this definition is not the internal index of \(\Phi^I{}_A\)
  in Presentation~B, and the \(D-4\) transverse coordinates are not
  covered by Assumption~\ref{ass:locked-block}. For a real
  four-dimensional leaf and a real Lorentzian \(g\), \(K^{-1}\) is
  nowhere proportional to \(g\), for every \(D\ge4\)
  (Appendix~\ref{app:status}); neither \(g\) nor \(K^{-1}\) is asserted
  here to be the emergent metric of Equation~\eqref{eq:g-from-e} or the
  metric of Assumption~\ref{ass:emergent-op}.
\end{definition}
```

**File 2: `chapters/appH-microscopic-proofs.tex`.** Anchor (occurs once, verified): "Problem~F, and Problems~A, B, C and~D, remain open." followed by a blank line and `\section{Problem G: HBEV}`. Insert a new paragraph after that sentence's blank line, before `\section{Problem G: HBEV}`; the 008 paragraph is untouched. (Merging as a continuation of the 008 paragraph is an equivalent alternative; I choose the separate paragraph so the merged text stays unchanged.) Labels verified once: `def:matrix-coords-ext` (new), `ass:locked-block`, `ass:emergent-op`, `ass:lorentzian`, `eq:Geff-structure`, `ch:vierbein-emergence`. Citation keys: `Steinacker2023` (exists), `KumarSteinacker2023`, `Steinacker2026` (new). `ass:emergent-op` and `ass:lorentzian` are not cited in the text below and need no check beyond the above.

```latex
\paragraph{More than four matrix coordinates in the Poisson limit: linear response (conditional; not closure).}
Keep Definition~\ref{def:matrix-coords-ext}, the Poisson limit, a four-dimensional symplectic leaf, a real Lorentzian induced tensor \(g\), \(\omega=\theta^{-1}\), \(K=\theta^{T}g\,\theta\) and \(G=K^{-1}\).

\emph{Operator metric versus induced metric.} The relation \(G=c\,g\) is excluded for every \(D\ge4\) by the argument of the preceding paragraph, because only the real four-dimensional leaf and the real Lorentzian \(g\) enter it; for a Euclidean induced \(g\) an orthogonal complex structure gives \(G\propto g\), but then \(G\) is Euclidean.

\emph{Linear response.} In a chart with constant \(\theta\), let \(\delta x^{I}=A^{I}e^{ip\cdot y}\), \(A=\xi^{\mu}\partial_\mu x+\phi_i n^{i}\) with \(n^{i}\) a normal frame and \(\mathrm{II}^{i}_{\mu\nu}=n^{i}\cdot\partial_\mu\partial_\nu x\); a factor \(i\) is absorbed in \(\xi\). To first order \(\delta g=p\circ(g\xi)-2\phi_i\mathrm{II}^{i}\) with \(a\circ b=ab^{T}+ba^{T}\), and \(\delta G=-G\,\theta^{T}\delta g\,\theta\,G\); the Hamiltonian choice \(\xi\propto\theta^{T}p\) gives \(\delta G=p\circ(G\xi)\), a linearised diffeomorphism of \(G\). About a flat brane the transverse amplitudes do not enter at first order, so the rank of the linearised Einstein operator of \(G\) on the image is exactly three for every \(D\), against six conserved sources \(p^{\mu}T_{\mu\nu}=0\). About a background with generic \(\mathrm{II}^{i}\) the rank is at most \(\min(6,D-1)\), because the image contains a gauge direction and lies in the space of conserved tensors; one exact-rational draw for each \(4\le D\le11\) attains this bound, so it is the generic rank by lower semicontinuity, and the same holds when \(K^{\mu\nu}\mathrm{II}^{i}_{\mu\nu}=0\). All six sources are then reachable from \(D=7\). The analysis freezes \(g\), \(\theta\) and \(\mathrm{II}\) at a point and does not impose the Gauss--Codazzi relations. Counting the density scalar as well, the number \(D-1\) of gauge-invariant functions must be at least \(7\), that is \(D\ge8\); this is a necessary count. No field equation of Einstein type for \(G\) is derived.

\emph{Content.} The \(D-4\) transverse coordinates are not covered by Assumption~\ref{ass:locked-block}; they are additional infrared fields unless they are gapped, and if they are gapped and decouple the flat-brane statement above applies. One-loop IKKT calculations on a brane with compact fuzzy extra dimensions report an induced Einstein--Hilbert term with the Newton constant set by the Kaluza--Klein scale~\cite{Steinacker2023}, and modified Einstein equations with extra tensors are reported in~\cite{KumarSteinacker2023,Steinacker2026}. A leaf of dimension greater than four is the hypothesis of the first statement above that such a construction would relax. These results have not been checked against the present operators.

This is a statement for \(D\) matrix coordinates, the Poisson limit, a four-dimensional symplectic leaf, a constant \(\eta_{IJ}\), locally frozen background data and generic \(p\). It does not identify \(G\) or \(g\) with the emergent metric of Chapter~\ref{ch:vierbein-emergence}, does not identify \(\Phi^{I}{}_{A}\) with a tangent-plane frame, does not derive a local Lorentz symmetry, a signature or an extra conserved stress, and gives no value or sign of \(G_{\mathrm{eff}}\) in Equation~\eqref{eq:Geff-structure}. This changes no ledger label; Problem~F remains open.
```

"The preceding paragraph" is the integrated 008 paragraph (appH line 1822, "Metric seen by the operators"), which directly precedes the insertion.

**File 3: `bib/namcg.bib` (integrator, after `ACCEPT`).** Records verified in review-r1 (abstract pages; no journal data claimed).

```bibtex
@misc{KumarSteinacker2023,
  author  = {Kumar, Kaushlendra and Steinacker, Harold C.},
  title   = {Modified Einstein Equations from the 1-loop Effective Action
             of the {IKKT} Model},
  year    = {2023},
  eprint  = {2312.01317},
  archivePrefix = {arXiv}
}

@misc{Steinacker2026,
  author  = {Steinacker, Harold C.},
  title   = {Modified Gravity at Large Scales on Quantum Spacetime
             in the {IKKT} Model},
  year    = {2026},
  eprint  = {2601.08031},
  archivePrefix = {arXiv}
}
```

**Stale passages elsewhere.** None. The 008 sentence "Suppose, as an assumed dictionary not contained in the four-matrix class..." stays true and is now realised by the definition; its closing phrase "to the embedding statement above beyond four coordinates" is addressed, not contradicted. ch03 `N>4` lines and ch05 exercise 7 concern the internal index of `Phi` and are unchanged. Chapter 17 and the ch16 inventory are unchanged (no assumption added or removed).

## Verification scripts

In `proposals/009-matrix-coords-N8/`:
- `check_conformal_nogo.py` / `.out.txt` (unchanged): identities `det omega = Pf^2`, `det M = Pf^2/det g`, `G = -g M^2`; random Lorentzian embeddings D = 4..11.
- `check_brane_rank.py` / `.out.txt` (unchanged; reproduced by the gatekeeper): rank table flat / generic / K-traceless `II`, D = 4..11; Hamiltonian direction is a `G`-diffeo.
- `verify_anchors_labels.py` / `verify_anchors_labels.out.txt` (updated, re-run in r2): new ch03 anchor count 1 and `eq:Smatrix` precedes it; appH anchor count 1; all cited labels count 1; `def:matrix-coords-ext` 0; bib keys `KumarSteinacker2023`, `Steinacker2026` absent, others present. `app:status` (appH) and `ch:vierbein-emergence` (ch04) were counted once by a separate grep.

## Decisions Taken

- Keep the definition as an additional labelled definition; `def:matrix-coords` and `eq:Smatrix` untouched. Rejected: dropping it (the D > 4 class would remain an unlabelled sentence in 008, and a leaf-dimension relaxation needs a home); editing `def:matrix-coords` in place (breaks 005/008 hypotheses).
- Separate appH paragraph with the review's closing sentence. Rejected: merging into the 008 paragraph (more invasive, no gain).
- M2 and the "correction to 008" framing withdrawn; the no-go is cited, not re-proved.
- Operative metric remains the operator metric `G`, not the induced `g`; neither is asserted emergent.
- Next package (pointer only, not begun): ranked first, **relax the leaf-dimension hypothesis** (4-dimensional brane times a compact fuzzy extra-dimension factor): it is exactly the hypothesis carrying the D-independent `G`-versus-`g` obstruction, it stays inside the matrix core with emergent spacetime, and it is the only route among the checked literature that comes with a matrix-derived Newton constant (`Steinacker2023`, abstract level). Ranked second: deriving the extra conserved stress (one-loop tensors), which requires full-text reading of the cited papers first.

## Milestone assessment

M5 only (pre-approved structural extension, emergence preserved, no label change), if the definition is integrated. No M2 (no-go already merged), no M1/M3, no breakthrough.

## Status-label recommendation

None. A, B, C, D1, E, F, G-derived and N remain OPEN / CRITICAL PATH (A, E, N "for the matrix-derived label") / PROGRAMME-CONDITIONAL.

## Author decision needed

None.

## Remaining open step

To discharge `ass:emergent-op` and advance D1/E/F: (a) a derived field equation for `G` from the matrix action in the extended setting (tree level `Delta_G x^I = 0` and one-loop terms), including whether extra tensors supply the missing conserved stress; (b) a mechanism gapping or constraining the `D-4` transverse scalars; (c) relaxing the 4-dimensional-leaf hypothesis (fuzzy extra dimensions) for the `G`-versus-`g` obstruction and a matrix-derived Newton constant (next package, pointer only); (d) identification of `Phi` with a tangent-plane or `G`-coframe and its vacuum manifold; (e) Moyal corrections and non-constant backgrounds; (f) a derived signature (E) and local Lorentz dynamics (D1).

## Special instructions for the gatekeeper

- The no-go is cited, not proved, in the new text. Check that the one cross-reference sentence matches the merged 008 argument and that "the preceding paragraph" is correct at the insertion point.
- Check the new ch03 anchor (once) and that `eq:Smatrix` precedes the insertion.
- Check the generic-rank wording: exact upper bound, one-draw lower bound by semicontinuity, frozen WKB, Gauss-Codazzi not imposed.
- Must not be asserted: that the extension solves F, A, D1 or E; that `G = c g` is attainable for Lorentzian `g`; that transverse scalars are gapped; that the literature supplies the 008 extra stress or that the leaf dimension of 2312.01317 and 2601.08031 exceeds four; any label change.
