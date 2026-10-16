# Proposal 020-flux-locus-cp12, round 2

## Changelog (r1 -> r2)
- Finding 1a: item (i) now begins "Conditional on the self-duality statement above, the closed forms give ...".
- Finding 1b: "a union of at most two lines" replaced by "a linear subspace of the zeta-plane (a line, or the whole plane only if F is (anti-)self-dual)".
- Finding 1c: final scope paragraph gains the sentence that self-duality of Q^{-1/2}FQ^{-1/2} is verified numerically at sampled points, is not proved, and that the classification of f1 = f2 is conditional on it.
- Finding 2: Troost phrased as "the Landau levels of the same form"; \cite{Troost2000} added with a BibTeX entry. DOI 10.1016/S0550-3213(99)00721-X verified via Crossref (title "Constant field strengths on T2n", author Jan Troost, Nuclear Physics B 568, pages 180-194, 2000-02). Verified by me this round: Crossref record only; the paper's content was verified by the gatekeeper in review-r1.
- Finding 3: left as is, per instruction.
- "Remaining open step" replaced by the review's ranked avenues (H2 first).
- Anchor re-verified: `\section{Problem G: HBEV}` occurs once (appH line 1982); the 018 paragraph ending "Problem~F remains open." immediately precedes it (checked by compile_check_r2.py). block-r2.tex equals the r2 block below (asserted in compile_check_r2.py).
- Unchanged from r1: Result, claims, scripts, no label change. Items 2 and 3 of the r1 Result list that say "exactly"/"holds exactly" refer to the closed forms and are to be read as conditional on the self-duality identification (see the block).

## Result
Within the 018 class (H1-H5) the question "is f1 = f2 ever reached" is answered in closed form. The outcome is a bounded no-go for a stable region, with exact structure that locates the missing ingredient. It is not a derivation of w.

1. (Closed form; structural argument plus numerical verification at sampled points.) With y^a = M^{a5}, y^4 = M^{45}, y.y = -l^2 and Q^{ab} = (y^4)^2 eta^{ab} + y^a y^b (Gram matrix of the D^a in the ambient metric, det Q = l^2 |y^4|^6), the vertical field of the symbol is F(zeta) = Q^{1/2} omega Q^{1/2} with omega delta-self-dual (chirality = sign y^4). Then f_{1,2} = |p| +- |r| (delta-SD and ASD parts of F). With Q = diag(a,b,m,m) in an adapted frame (ab = l^2 m, m = (y^4)^2): f2/f1 = min/max(l,|y^4|) along the axis, sqrt(b/a) orthogonal to it, monotone in between.
2. (Classification.) f1 = f2 for every zeta (the only case with no vector negative mode at any zeta) holds exactly on |y^4| = l, y_i = 0: the S^2 fibres over y^0 = -sqrt2 l, y^4 = +-l. Codimension 4 in the 6D leaf. f1 = f2 for some zeta only: from the closed form, codimension 2 (|y^4| = l and the fibre point orthogonal to the axis); not separately scanned. Near the set |r|/|p| grows linearly. The 018 sampled range [0.006, 0.84] is part of an interval whose supremum 1 is attained only on this set.
3. (Corrects an 018 avenue.) For the compact form so(6) with delta throughout, f2/f1 = |y^4|/l exactly for all zeta and fibre points (200 points x 45 directions, error 4e-16): f1 = f2 only over the poles. So 018 avenue 5 (a compact twistor section replacing the instability by zero modes) is not realised with the constant contraction delta_ab. Self-duality holds identically only for the position-dependent contraction by the ambient metric Q^{-1}.
4. (Troost.) A zeta-independent transverse flux cannot cure the instability in the Poisson limit, because f1 - f2 = 2|r| grows linearly in |zeta|. Stability on a finite fibre needs a transverse flux above a bound set by |r|/|p|.
5. (At f1 = f2.) The vector density tends to f^2/(2 pi^2) for sf >> 1, independent of s, so the zeta integral still diverges. With N=1-type Landau content (vector, ghosts, Majorana) the supertrace equals the prefactor times 6 sinh^2(sf), i.e. is s-independent (index density 3f^2/(8 pi^2)): all s-dependence, hence any s^-3 coefficient, cancels there.
6. The sign and size of w are not defined by this package. No closure.

## Target and status
Problem F (coefficients A, B, C; induced G_eff). Appendix H sec:status-F: OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL (reduced-scope result: treating G_eff as an input leaves F OPEN). Original target: the matrix-derived G_eff (sign and size) in a class where the 008/009/011 obstructions are absent. Dependencies: A, B, C, D1, E, N through G_eff. Critical-path set at the full-GR scope per Ch. 17: A, B, C, D1, E, F, G-derived, N. No discrepancy between Ch. 17 and appH found. This package is PROGRAMME-CONDITIONAL.

## Source reading
Digest + targeted reads (dirty-chapters: yes; working tree treated as current). Read in full: 018 proposal r2 and review r2, the 018 scripts check_hormander_weyl.py and cp12_realisation.py, the integrated 018 block (appH lines ~1972-1980), the SME scout (R-f1, R-f2, R-b3). Literature opened with the fetch tool (which returns model-extracted text, so quotations are as extracted): Troost hep-th/9909187 (arXiv abstract page; ar5iv), Steinacker arXiv:2303.08012 (ar5iv, all 295k characters in three chunks). Correction to the task text: Troost eq. (35) is in Section 7 (lambda_k^+- = 2 pi(sum_i (2m_i+1) f_i +- 2 f_k)); the no-tachyon condition f2+...+fn >= f1 is stated inline in Section 9 with no equation number; eq. (43), Section 10, gives the fermion levels; "on T^4 stability implies self-dual and coincides with SUSY" is Section 9. Troost's DOI was not independently verified.

## Research and reasoning
A. Structure. The leaf is a bundle over the base H^4 = {y.y = -l^2} with S^2 fibre. On functions D^a = s(y^4 d^a - y^a d_4) are rotation fields; at fixed y they form a frame of T H^4 with Gram matrix Q. The vertical part of [D^a,D^b] is the curvature of the horizontal distribution acting on the fibre; H^4 has constant curvature (Weyl = 0), so the curvature operator is a multiple of the identity on Lambda^2 and the vertical component is self-dual for the ambient metric. I did not prove that the numerically defined horizontal distribution is the Levi-Civita lift. It is verified at 300 points x 2 centre directions: the opposite-chirality fraction of Q^{-1/2} S_k Q^{-1/2} is at most 7e-10, and the chirality equals sign(y^4). The classification is therefore conditional on that structural identification.
B. With F = Q^{1/2} omega Q^{1/2} and Q = diag(a,b,m,m): the delta-SD/ASD amplitudes per unit |n| are s_par = (sqrt(ab)+m)/2, s_perp = sqrt(m)(sqrt a + sqrt b)/2, l_par = (sqrt(ab)-m)/2, l_perp = sqrt(m)(sqrt a - sqrt b)/2. With ab = l^2 m: l_par = |y^4|(l-|y^4|)/2, zero iff |y^4| = l. l_perp = 0 iff a = b iff y_i = 0 and |y^4| = l (a = b needs y0 y_i = 0 and y0^2 - 2(y^4)^2 = r^2; y0 = 0 is excluded since y0^2 = l^2 + (y^4)^2 + r^2). So L = diag(l_par, l_perp, l_perp) has rank >= 2 off that set, and the centre plane is never inside its kernel except where L = 0. Numerics: the closed-form bracket contains the numerical f2/f1 to 1.5e-13 and its ends are attained at every sampled point; minimisation to y_i = 0, |y^4| = l gave f2/f1 = 1.000000 at six points. On the time axis |r|/|p| = (l-|y^4|)/(l+|y^4|) exactly (checked at y^4 = l(1.2, 1.1, 1.05)).
C. Fork. Hypotheses and what each relaxation gave:
 - H2 (contraction). Constant delta_ab with so(4,2) (hybrid): stable set of codimension 4. Compact so(6) with delta: codimension 4 (the poles), f2/f1 = |y^4|/l. Contraction by Q^{-1}: f1 = f2 identically. Q^{-1} = (eta + eta y y^T eta / l^2)/(y^4)^2 is position dependent: it needs the term (y_a D^a)^2 / l^2 besides eta_ab D^a D^b, i.e. the unit time-like vector of the background. Whether the matrix action supplies it is not shown. Most favourable lead.
 - H4 additional fluxes (task item 2). Transverse matrices with a background (for example a fuzzy S^2) give a zeta-independent flux f3. The lowest level is sum f - 2 f_max, so stability holds iff f1 - f2 <= f3, which holds for |zeta| below a bound only. In the Poisson limit the fibre directions are the centre (Fourier variable zeta), not an extra Landau plane. On a finite fibre the condition becomes f3 >= 2 sup|L n| zeta_max. A flux growing with zeta would need transverse matrices depending on the fibre: a different background whose equations of motion are not examined (Problem A). An emergence-preserving configuration (built from matrix data only) satisfying Troost's inequality for all zeta was not found; one for bounded zeta exists in principle.
 - H4 fermions. Dirac-squared levels sum(2m+1)f_i +- f_1 +- f_2 are non-negative, so fermions cannot cancel a tachyon at f1 != f2 (SME inference confirmed for the Landau levels); at f1 = f2 they cancel all s-dependence (item 5). They help only on the codimension-4 set.
 - R-f2 (Steinacker 2303.08012, as extracted). The one-loop action is a Gaussian integral with Feynman i epsilon (eqs. 4.14-4.15), expanded in powers of (box - i epsilon)^{-1}[F,.] (4.16); leading terms cancel by maximal SUSY and the first non-vanishing term is n = 4 (4.18); V4[dF] = -4 tr dF^4 + (tr dF^2)^2 (4.21); target space Minkowski R^{9,1} with eta. In the text read there is no discussion of tachyons or negative modes. So it formally avoids a Euclidean heat trace, since each term of the flux series is finite. It does not remove the instability: a series in [F,.] has a finite radius set by the lowest box eigenvalue, where a negative mode crosses zero, and the stated validity regime is weak coupling with semiclassical wave packets. Identity (sympy): for a 4D flux with plane strengths f1, f2, V4 = -4(f1^2 - f2^2)^2, zero exactly on (anti-)self-dual flux. In the present class f1^2 - f2^2 is proportional to |p||r|; no identification with Steinacker's dF (a flux difference at two points) is claimed. R-f2 changes regulator (H5) and content (H4) together: a lead, not an application.
 - R-b3. c_K^2 = (pi^2/8) sum C_L^2/mu_L^2 > 0 (eq. 6.30-6.31 as extracted) is a finite sum over a fuzzy extra space with Euclidean target-space metric. Here the fibre belongs to the leaf and the zeta integral is non-compact; a finite positive fibre sum appears only after truncation. Mapping c_K^2 to w is a hypothesis; not computed.
D. Why w is not computed: the stable set has codimension 4 and has a divergent zeta integral even there; the weight-two coefficient and its A-variation need the second-order symbol, which is not available.

## Claim classification
- Q, det Q, Gram structure: established (algebra; sympy det).
- F = Q^{1/2} omega Q^{1/2}, omega self-dual: structural argument + numerical at 300 points (conditional on equiregularity and the Levi-Civita identification).
- Closed-form bracket and the codimension-4 stable set: conditional on the previous line; numerical agreement 1.5e-13. The codimension-2 "some zeta" set follows from the closed form and was not scanned.
- Compact so(6) result: numerical (4e-16), same structural argument.
- Troost levels and condition: literature, as extracted. Constant transverse flux cannot compensate: established within the Landau symbol.
- Fermion remark and SD supertrace: established algebra (sympy) for Landau levels; not a statement on the IKKT content.
- V4 identity: established; relation to the leaf: not claimed.
- w sign and size: unresolved.

## Proposed changes
File chapters/appH-microscopic-proofs.tex. Anchor: the line `\section{Problem G: HBEV}`, which occurs exactly once (asserted in compile_check_r1.py), placed after the integrated 018 paragraph ending "This changes no ledger label; Problem~F remains open." Nothing existing is replaced. The block (identical to block-r2.tex) uses one citation key, Troost2000 (entry below; absent from bib/namcg.bib at present, no duplicate), and no labels.

```latex
\paragraph{Conjugate-coordinate class: where the flux eigenvalues of the Euclidean symbol coincide (conditional; bounded no-go).}
Keep the setting of the preceding paragraph: Poisson limit, leaf \(\mathbb{CP}^{1,2}\), \(D^a=\{T^a,\cdot\}\), the nilpotent (Landau) leading symbol with centre variable \(\zeta\in\mathbb R^2\), the contraction \(\eta\to\delta\) of the four matrix indices with the Lie--Poisson algebra \(\mathfrak{so}(4,2)\) kept, and the sheet realised by the orbit. Write \(y^a=M^{a5}\), \(y^4=M^{45}\), \(y\cdot y=-\ell^2\), and \(Q^{ab}=(y^4)^2\eta^{ab}+y^ay^b\), the Gram matrix of the fields \(D^a\) in the ambient metric of the hyperboloid; \(Q\) is positive definite with \(\det Q=\ell^2|y^4|^6\). At \(300\) random orbit points, with both centre directions, the matrix \(Q^{-1/2}F_{ab}Q^{-1/2}\), \(F_{ab}=\zeta_kS^{ab}{}_k\), is self-dual or anti-self-dual with respect to \(\delta\) to a relative accuracy of \(10^{-9}\), with the sign equal to \(\operatorname{sign}y^4\); this is the expected statement that the vertical curvature of the horizontal distribution over the constant-curvature base is self-dual for the ambient metric. Hence \(F=Q^{1/2}\omega Q^{1/2}\) with \(\omega\) self-dual, and the plane strengths of \(F\) are \(f_{1,2}=|p|\pm|r|\), with \(p\) and \(r\) the \(\delta\)-self-dual and anti-self-dual parts of \(F\). Let \(a\ge b\) be the eigenvalues of \(Q\) on the plane spanned by the time axis and \(\vec y\), so that \(ab=\ell^2(y^4)^2\) and the remaining eigenvalue is \((y^4)^2\) twice. For \(\zeta\) such that \(\omega\) points along the axis of that plane one finds \(f_2/f_1=\min(\ell,|y^4|)/\max(\ell,|y^4|)\); for \(\omega\) orthogonal to it, \(f_2/f_1=\sqrt{b/a}\); for other directions the ratio lies between these values. The numerical range of \(f_2/f_1\) at the sampled points lies inside this bracket to \(10^{-13}\).

\emph{Consequences.} (i) The vector sector has no negative mode at fixed \(\zeta\) only if \(f_1=f_2\), and a stable point must have this for every \(\zeta\), because the set of \(\zeta\) with \(f_1=f_2\) is a linear subspace of the \(\zeta\)-plane (a line, or the whole plane only if \(F\) is (anti-)self-dual). Conditional on the self-duality statement above, the closed forms give \(f_1=f_2\) for all \(\zeta\) exactly on \(\vec y=0\), \(|y^4|=\ell\), that is on the two-sphere fibres over the points \(y^0=-\sqrt2\,\ell\), \(y^4=\pm\ell\): codimension \(4\) in the six-dimensional leaf (the minimisation of the distance to this set found it, with \(f_2/f_1=1\) to six digits at six points). On the rest of the leaf the lowest vector eigenvalue is \(-|f_1-f_2|<0\) for generic \(\zeta\), and \(|f_1-f_2|/(f_1+f_2)=(\ell-|y^4|)/(\ell+|y^4|)\) on the time axis grows linearly with the distance from the set. (ii) The same holds for the compact real form \(\mathfrak{so}(6)\) with \(\delta\) throughout: there \(f_2/f_1=|y^4|/\ell\) for every \(\zeta\) and every fibre point (checked at \(200\) points, error \(4\cdot10^{-16}\)), equal to \(1\) only over the poles \(\vec y=0\). A compact Euclidean section with the contraction \(\delta_{ab}\) therefore does not replace the instability by zero modes; self-duality holds identically only for the contraction by the position-dependent ambient metric \(Q^{-1}\), which is not a constant contraction of the matrix indices. (iii) Constant additional fluxes \(f_3,\dots\) from transverse matrices change the lowest level to \(\sum_kf_k-2\max_kf_k\) (the Landau levels of the same form, \(2\pi(\sum_i(2m_i+1)f_i\pm2f_k)\), of \cite{Troost2000}, eq.~(35), and the no-tachyon condition of its Section~9, \(f_1\le f_2+\dots+f_n\)); because \(f_1-f_2\) grows linearly in \(|\zeta|\), a \(\zeta\)-independent transverse flux restores stability only for \(|\zeta|\) below a bound set by that flux, that is on a finite fuzzy fibre, not in the Poisson limit. (iv) At the self-dual points the vector density \(\prod_j f_j/(4\pi\sinh sf_j)\) times the Zeeman trace tends to \(f^2/(2\pi^2)\) for \(sf\gg1\), independent of \(s\), so the integral over \(\zeta\) diverges there as well; the proper-time cutoff does not regulate it.

This is a statement for the Poisson limit, the leading symbol, equiregular points, the contraction \(\eta\to\delta\) (or \(\delta\) with \(\mathfrak{so}(6)\)), constant additional fluxes and bosonic content. The self-duality of \(Q^{-1/2}FQ^{-1/2}\) is verified numerically at sampled points and is not proved, so the classification of the set \(f_1=f_2\) is conditional on it. It does not treat a contraction by a position-dependent metric, Moyal terms, fermions, a finite fibre, or other backgrounds for the transverse matrices, and it determines neither the sign nor the size of \(w\). This changes no ledger label; Problem~F remains open.
```

Bibliography entry required by the block (DOI verified via Crossref):
```bibtex
@article{Troost2000,
  author  = {Troost, Jan},
  title   = {Constant field strengths on {$T^{2n}$}},
  journal = {Nucl. Phys. B},
  volume  = {568},
  pages   = {180--194},
  year    = {2000},
  doi     = {10.1016/S0550-3213(99)00721-X},
  eprint  = {hep-th/9909187}
}
```
Stale passages: none need editing. 018's "Remaining open step" item 5 (compact twistor section as a zero-mode family) is superseded by consequence (ii) of the block; the 018 paragraph's own text does not state it.

## Verification scripts
- check_flux_classification.py / .out.txt: SD structure, closed-form bracket, locus Sigma by minimisation (f2/f1 = 1.000000), Lorentzian eta-contraction (E parallel B; real/imaginary eigenvalue ratio = l/|y^4|). Note: the last "displacement" part of this script used the wrong sheet (y^0 > 0, minimisation residual ~7) and its numbers are invalid; superseded by the next script. The first part also printed "all equal = False" for the chirality because the sign depends on sign(y^4); resolved there.
- check_orientation_displacement.py / .out.txt: chirality = sign(y^4); on the realised sheet |r|/|p| near Sigma = (l-y^4)/(l+y^4) (0.0909, 0.0476, 0.0244).
- check_compact_section.py / .out.txt: PB/lie constant (-1), ranks (4,6), f2/f1 = |y^4|/l to 4e-16.
- check_algebra.py / .out.txt: V4 = -4(f1^2-f2^2)^2; SD supertrace = 6 sinh^2(sf); large-f vector density; Troost lowest level; det Q = l^2 y4^6.
- compile_check_r2.py / .out.txt (supersedes r1): scratch-copy build with bib entry and block-r2.tex; make_r2.py generates block-r2.tex from r1 outside the repo: 268 pages, 0 errors, 0 undefined, 0 multiply defined, 0 double subscripts.
- cp12_realisation.py: copy of the 018 file.

## Decisions Taken
- Treated targets 1, 2 and 4 jointly; no stable locus of positive measure exists, so target 3 (sign of w) is recorded as the missing step.
- Used the Levi-Civita identification as a structural argument checked at 300 points, not as proved.
- One manuscript block only.
- Corrected the Troost citation (eq. 35 is in Section 7).
- Did not run the rank-5 SO(4,1)-covariant presentation (X^A = M^{A5}); recorded as an avenue.

## Milestone assessment
M2 (narrow): closed-form classification and a bounded no-go, with a correction of an 018 avenue. No breakthrough; no critical-path step derived.

## Status-label recommendation
None. F, A, B, C, D1, E, G-derived, N remain OPEN / CRITICAL PATH / PROGRAMME-CONDITIONAL.

## Author decision needed
None.

## Remaining open step
Ranked avenues (from review-r1; each relaxes a hypothesis; none completed here):
1. H2 (most favourable): the position-dependent ambient contraction Q^{-1}, for which f1 = f2 identically. Determine whether the matrix action, gauge fixing or regulator supplies the Q^{-1} contraction, i.e. the term (y_a D^a)^2/l^2 (the unit time-like vector of the background built from matrix data).
2. H4 with a finite fibre: truncation of l with transverse flux f3 >= 2 sup|Ln| zeta_max, giving a finite positive fibre sum (the R-b3 analogue).
3. SO(4,1)-covariant presentation X^A = M^{A5} (five horizontal fields; not computed).
4. R-f2: SUSY flux expansion of the Lorentzian one-loop action; compare its radius of convergence with |r|/|p|. V4 = -4(f1^2-f2^2)^2 vanishes on (anti-)self-dual flux, but no identification with Steinacker's dF is claimed: a lead, not an application.
5. H1: exact so(4,2) character analysis with Moyal terms.
6. Fermions help only on the codimension-4 locus; at f1 != f2 the Dirac-squared Landau levels are non-negative and cannot cancel a tachyon.

## Special instructions for the gatekeeper
Do not accept the closed forms as a proof of the Levi-Civita identification: it is numerical at 300 points plus a structural argument. Re-run check_orientation_displacement.py (the displacement part of the first script is invalid and declared superseded). The block states a no-go inside H1-H5 only and must not be read as excluding other contractions, finite-fibre or fermionic cures. Re-check: chirality = sign(y^4), the codimension counts, the Troost section numbering, that no status label changes, and that the block equals block-r2.tex. The integrator must add the Troost2000 entry to bib/namcg.bib together with the block.
