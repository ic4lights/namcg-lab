# Proposal 027-fibre-window-spin1, round 2

## Result
Same bounded, conditional results as round 1 for Problem F; no sign or size of G_eff, no closure. Round 2 applies review-r1 (ACCEPT WITH REQUIRED REVISIONS, OPEN 0/3, no PRIOR-CLAIM-ERROR); the mathematics is unchanged, the statements are corrected and narrowed.
1. **Gaussian lemma (proved).** For any Gaussian window the Lorentzian principal-value mass moment has Re M = (2/c) int_0^1 dv prod(1+l_k(1-v^2)/c)^(-1/2) > 0 and Im M > 0.
2. **Cone window.** Geometry identities at 60 orbit points (1e-9); apex-inside shell formula (proved); the continuation of the shell formula to spacelike p with |p| >= R up to the tangency distance R coth(tau) is now stated as a **numerical observation only** (the round-1 domain-of-dependence/unique-continuation justification was wrong and is withdrawn). The sign Re N_W > 0 and the finiteness of N_W are explicitly conditional on that observation.
3. **Electric growth.** Closed forms for the Zeeman eigenvalues (f_e, f_m) on three planes at 59 of 60 points; base maximum to 6e-5 over 3000 directions; the electric rate is bounded by a quantity linear in the base cutoff with fibre part independent of it; the log det has integrable logarithmic singularities at sigma = +-2 f_m. Exact kernel-plane threshold |y^4| = ell.
4. **Vector, ghost, invariant sector (exact in s = 0).** tr(E+R/6) = 4 D_1 + 6 s^2 (1+a^2)/(t+i s a^2) - 4 i s mu^2, with D_1 and the E+R/6 convention now defined.
5. **Supertrace.** For the supplied IKKT content the count, index and F^2 terms cancel; the remainder of the weight-two coefficient at A = 0 is -(4 mu^2 + n_ex mu_i^2) j(a), Re j = 2/(1+a^2) > 0 (no sign of the supertrace claimed). The conclusion "is a property of the next order" is replaced by: not by itself the Newton coefficient; higher order or A-dependence not computed.

## Target and status
Problem F (coefficients A,B,C): Status OPEN, Priority CRITICAL PATH, Completion PROGRAMME-CONDITIONAL (Appendix H); Problem E touched only by the caveat on Assumption ass:lorentzian (OPEN, CRITICAL PATH for the matrix-derived label, PROGRAMME-CONDITIONAL). Original target: induced coefficients from the matrix theory including sign and size of w. The Chapter 17 critical-path set (A,B,C,D1,E,F,G-derived,N) is untouched. Classification: PROGRAMME-CONDITIONAL. No label change.

## Source reading
Digest + targeted reads (round 1: appH 018-025 paragraphs, sector-sum/fermion paragraphs, proposal 025 and its scripts, SME scout). Round 2: review-r1 read in full; the 025 block (appH lines ~2040-2077) re-read to define D_1, x, Q(a), and to remove the undefined g. Working tree used as is (025 block uncommitted). No external paper fetched; no new citation.

## Research and reasoning
The mathematics is as in round 1 (scripts unchanged except the repaired det check); only the following changed.

**F1 (tangency).** Withdrawn: the claim that a causal line through p meets the ball iff P < r sqrt(1+v_c^2) is false (a timelike line through p at spatial distance P > R never meets the ball; the formula is the distance of the nearest null line), and Holmgren-John continuation from the ball reaches only the domain of dependence of a spacelike slab inside the ball. The observed validity range ends at the touching of the sphere with the characteristic cone of the apex, a Landau-type singularity of P(p), consistent with the sharp numerical threshold (review P-scan: <= 4e-3 up to P = 1.30, then -0.062, -0.233, -0.645, -1.79 at P = 1.32, 1.35, 1.40, 1.50; threshold 1.2991 at r = 1; I did not re-run that scan, it is the reviewer's). It is reported as a numerical observation; no mechanism is claimed. Saved outputs: shell_apex_lemma.out.txt (apex-inside |p| = 0.45: 14.19139 vs 14.18981; trace identity 34.198648 = 34.198648), cone_window_moment.out.txt.

**F2 (definitions).** D_1: the diagonal of exp(z Delta_H4 + w Delta_H3) is D = D_0 (1 + D_1 + ...), D_1 of degree one in (z,w) = (t - i s, i s), depending on a; verified against the SD coefficient (sd_scalar_vs_exact.out.txt, difference 1e-124 to 1e-126 at three points). tr(E+R/6) is the first Seeley-DeWitt density for exponent Delta + E. x = s/t is defined where used (subtraction at x = 1 of 025). The reference to g is removed.

**F3.** flux_closed_forms.out.txt: 59 points; the singular point has a vanishing fibre Gram eigenvalue in double precision (divide-by-zero at wf**-0.5 in cone_window_geometry.py, visible in the warnings of flux_closed_forms.out.txt). The block states 59 of 60, 1e-9 except the base maximum (3000 directions, 6e-5). I did not identify which sampled point it is; the cause given is the numerical one visible in the warning.

**F4, F5.** Statement on the rate and the log det per review snippet 3 and the 025 wording; finiteness rests on the conditional shell formula (the window function has a jump at the cone edge when chi(0) != 0, so it is not Lipschitz).

**F6 (symbols).** Zeeman eigenvalues A,B -> f_e, f_m (A is reserved for the matrix fluctuation). sigma(Box) form S -> K (blocks K_uu, K_uzeta, K_zetazeta), freeing S^2 = 2C41 - C42. The three uses of calligraphic J: J_ab (generators, kept), J_a -> j(a), Jacobian J_c -> varrho; second-moment matrix J -> N. The window integral <.>_W -> N_W = int_W varrho d^4u d^2zeta chi (sigma - i0)^(-1). The cone variable x -> bold x to keep x = s/t.

**F7.** Added: on the kernel plane F_ab F^ab/2 is negative for |y^4| < ell, positive above, exact threshold |y^4| = ell, replacing the sample-dependent value of 025 on that plane; opposite signs on the vertical plane (f_e^2 - f_m^2 = |zeta|^2 (a^2-1)/2 there). The 025 sentence is a sampled-points statement and is not materially false.

**F8.** Supertrace closing clause per review snippet 5; sign stated: remainder -(4 mu^2 + n_ex mu_i^2) j(a), Re j = 2/(1+a^2) > 0, no sign of the supertrace claimed.

**F9.** Optional; not taken. The 025 closing sentence "the positivity of the moment is numerical" stays untouched; the new block supersedes it for Gaussian windows only, and its own scope paragraph says what is conditional.

## Claim classification
- Established (proved): Gaussian lemma (Sylvester inertia of K plus contour rotation); apex-inside shell formula; spin-term sum rules and Dirac/vector trace relation by algebra; Zeeman character identity.
- Established numerically (high precision, sampled): geometry identities (60 points, 1e-9); Zeeman closed forms (59 points; base max 6e-5); SD vs exact scalar kernel (125 digits); matrix SD vector/Dirac (120 digits); closed-form Q_mu, Q_sp.
- Conditional / numerical observation: shell formula for spacelike |p| >= R up to the tangency distance, hence Re N_W > 0 and finiteness of N_W; formal SD coefficient as the weight-two term on the full leaf; fermion content (input); varrho not computed.
- Unresolved: second variation under A; vector kernel; Plancherel/finite N; next order; real/imaginary identification; Moyal terms; window from dynamical matrices.

## Proposed changes
File chapters/appH-microscopic-proofs.tex. Insert the block below (identical to block-r2.tex) immediately before `\section{Problem G: HBEV}`. Anchor re-verified: that string occurs exactly once (line 2078 in the current working tree) and is immediately preceded by the 025 block whose last sentence is "This changes no ledger label; Problem~F remains open." (line 2076). Labels used: `ch:vierbein-emergence`, `ass:lorentzian` (exist, unchanged from round 1); no new labels, bib entries or `\cite`. Compile check in a scratch copy outside the repo (compile_check_r2.py/.out.txt): anchor unique; pdflatex-bibtex-pdflatex-pdflatex all rc 0; 0 errors, 0 undefined, 0 multiply defined, 0 double subscripts; 285 pages (round 1 recorded 283; I changed no chapter file, so the difference comes from the tree state, not from this block alone).

```latex
\paragraph{Conjugate-coordinate class: Lorentzian moments in the fibre-bounded cone window, and the vector, ghost and spin terms of the invariant sector (conditional; bounded no-go).}
Keep the setting and notation of the two preceding paragraphs (Poisson limit, leaf \(\mathbb{CP}^{1,2}\), \(T^a=M^{a4}\), \(\Box\), \(H_V\) with \(\mu^2=-3\), \(C_{42}\), \(C_{41}\), \(C_{31}\), \(\sigma(\cdot)\), \(S^2=2C_{41}-C_{42}\) with symbol \(\beta q_f\), the base symbol \(\alpha q_b\), \(a=\sinh\tau=y^4/\ell\), and the function \(Q(a)\) of the exact invariant sector). At a point of the leaf take coordinates \((u,\zeta)\in\mathbb R^4\times\mathbb R^2\) on the cotangent space with \(|u|^2=\alpha q_b\) and \(|\zeta|^2=\beta q_f\), so that \(-\sigma(C_{42})=|u|^2-|\zeta|^2\), and write \(\mathsf K\) for the form \(\sigma(\Box)\) (rank four, signature \((3,1)\)) in these coordinates, with blocks \(\mathsf K_{uu}\), \(\mathsf K_{u\zeta}\), \(\mathsf K_{\zeta\zeta}\).

\emph{Gaussian windows.} Let \(\lambda_0=-c\) and \(\lambda_1,\lambda_2,\lambda_3\) be positive and \(\mathcal M=\mathrm i\int_0^\infty\mathrm ds\prod_{k=0}^3(1+\mathrm is\lambda_k)^{-1/2}\), the Gaussian average of \((\sigma-\mathrm i0)^{-1}\). Rotating \(s=-\mathrm iu\) (the fourth quadrant contains no singularity) gives \(\mathcal M=\int_0^\infty\mathrm du\,(1-cu-\mathrm i0)^{-1/2}\prod_{k\ge1}(1+\lambda_ku)^{-1/2}\), whose first factor is real for \(u<1/c\) and equals \(\mathrm i(cu-1)^{-1/2}\) for \(u>1/c\). With \(u=(1\mp v^2)/c\),
\[
  \operatorname{Re}\mathcal M=\frac2c\int_0^1\!\mathrm dv\prod_{k\ge1}\Bigl(1+\frac{\lambda_k(1-v^2)}c\Bigr)^{-1/2}>0,\qquad
  \operatorname{Im}\mathcal M=\frac2c\int_0^\infty\!\mathrm dv\prod_{k\ge1}\Bigl(1+\frac{\lambda_k(1+v^2)}c\Bigr)^{-1/2}>0 ,
\]
and \(\operatorname{Re}\mathcal M=2/(\lambda+c)\) for \(\lambda_k=\lambda\). The pencil of \(\sigma(\Box)\) with any positive definite window form has one negative, three positive and two zero generalised eigenvalues, so the principal-value mass moment of every Gaussian window of the class is positive; this proves, for Gaussian windows, the positivity that the preceding paragraph found by sampling.

\emph{Geometry of the cone window.} At \(60\) random orbit points (agreement \(10^{-9}\) or better, not proved): the eigenvalues of \(\mathsf K_{uu}\) are \(-\tfrac12\) and \(\tfrac12\sinh^2\tau\) (three times); the Schur complement of \(\mathsf K_{uu}\) in \(\mathsf K\) vanishes, so \(\sigma=Q_L(u+w\zeta)\) with \(Q_L=\mathsf K_{uu}\) and \(w=\mathsf K_{uu}^{-1}\mathsf K_{u\zeta}\); \(w\) is conformal, \(|w\zeta|=\coth\tau\,|\zeta|\), and its image is orthogonal to the time eigenvector of \(Q_L\). In the variable \(\boldsymbol x=u+w\zeta\) the removed region \(|u|<|\zeta|\) is therefore the ball of radius \(r=|\zeta|\) about the spacelike point \(p=w\zeta\), at distance \(r\coth\tau=r\sqrt{1+c/\lambda}\) from the apex \(\boldsymbol x=0\) with \(c=\tfrac12\), \(\lambda=\tfrac12\sinh^2\tau\): the cone \(|u|=|\zeta|\) touches the null cone of \(Q_L\).

\emph{Mass moment in the fibre-bounded cone window.} Let \(\chi\ge0\) be bounded and integrable on \([0,\infty)\) and take the window function \(\chi(|u|^2-|\zeta|^2)\) on \(|\zeta|^2\le Q_f\) and \(|u|\ge|\zeta|\). For a ball of radius \(R\) about \(p\) with \(|p|<R\), polar coordinates about the apex give \(\operatorname{PV}\!\int_{|\boldsymbol x-p|<R}\mathrm d^4\boldsymbol x\,Q_L^{-1}=\tfrac12(R^2-|p|^2)I_0+p^{\mathsf T}\mathsf Np\), where \(I_0=\operatorname{PV}\oint\mathrm d\Omega\,Q_L^{-1}=8\pi^2/\cosh^2\tau\) and \(\mathsf N=\operatorname{PV}\oint\mathrm d\Omega\,nn^{\mathsf T}Q_L^{-1}\), because the remaining term of the exit radius is odd in the direction \(n\) and \(Q_L\) is even (checked against a direct quadrature to \(10^{-4}\)). For spacelike \(p\) with \(|p|\ge R\), quadrature indicates that the same expression continues to hold up to the tangency distance \(R\coth\tau\) (agreement to \(10^{-3}\) in the sampled cases) and departs from it beyond; this is a numerical observation and is not proved here. Under this observation every shell \(r\le|u|\le\sqrt{r^2+\Lambda^2}\) has principal-value moment \(\tfrac12\Lambda^2I_0\), independent of \(p\), and so
\[
  \operatorname{Re}\,\mathcal N_W=\tfrac12\,\varrho\,\pi Q_f\,I_0\int_0^\infty\chi(\lambda)\,\mathrm d\lambda>0 ,\qquad
  \mathcal N_W=\int_W\varrho\,\mathrm d^4u\,\mathrm d^2\zeta\;\chi\,(\sigma-\mathrm i0)^{-1},
\]
with \(\varrho>0\) the Jacobian of the coordinates \((u,\zeta)\); the sign of the real part is conditional on the numerical observation, and the real part depends on the cutoff function only through \(\int\chi\) and on the fibre bound only through the area \(\pi Q_f\). The imaginary part is \(\pi\int_W\varrho\,\chi\,\delta(\sigma)\ge0\). Finiteness of \(\mathcal N_W\) is likewise rested on the shell formula: the apex singularity is of order \(|\boldsymbol x|^{-2}\) in four dimensions and integrable, but the window function has a jump at the cone edge when \(\chi(0)\ne0\), and the edge touches the null cone of \(Q_L\) at one point, so finiteness there is not shown independently.

\emph{Zeeman field and electric growth.} The first-order term of \(H_V\) is exactly the Zeeman matrix of the field \(F_{ab}(\xi)=\xi(\mathcal J_{ab})\), linear in the covector \(\xi\); let \(\eta F\) have eigenvalues \(\pm f_e\) (electric pair, factor \(\mathrm e^{\pm2sf_e}\) in \(\mathrm e^{-\mathrm isH_V}\)) and \(\pm\mathrm if_m\) (magnetic pair, phases), so \(f_e^2-f_m^2=-F_{ab}F^{ab}/2=-\sigma(C_{31})(\xi)\). At \(59\) of the \(60\) points (one point is numerically singular in the whitening, a fibre Gram eigenvalue vanishing in double precision), to \(10^{-9}\) except for the maximum over the base plane, which is obtained from \(3000\) sampled directions to \(6\cdot10^{-5}\): on the base plane \(f_m=0\) and \(\max f_e=|u|\cosh\tau/\sqrt2\); on the vertical plane of the pencil \(f_e=|\zeta|\sinh\tau/\sqrt2\), \(f_m=|\zeta|/\sqrt2\) in every direction; on the kernel plane of \(\mathsf K\) (the centre variable of the nilpotent model) \(f_e^2=|\zeta|^2/(2(1+2\sinh^2\tau))\) and \(f_m^2=|\zeta|^2\sinh^2\tau/(2(1+2\sinh^2\tau))\), so that on this plane \(F_{ab}F^{ab}/2\) is negative for \(|y^4|<\ell\), positive for \(|y^4|>\ell\) and changes sign exactly at \(|y^4|=\ell\); this exact threshold replaces the sample-dependent value of the preceding paragraph on that plane (on the vertical plane the signs are opposite). The fibre-driven electric rate \(2f_e\) is \(2s_f\sinh\tau\) with \(\beta q_f=2s_f^2\le2s_{\max}^2\), whereas the base-driven rate grows linearly with \(|u|\); the electric rate is thus bounded by a quantity linear in the base cutoff, whose fibre part is bounded independently of the base cutoff. The logarithm of the determinant of the Zeeman block, \(\ln(\sigma^2-4f_m^2)+\ln(\sigma^2+4f_e^2)\), has only integrable logarithmic singularities, at \(\sigma=\pm2f_m\), at the leading symbol; the growth is a property of the Schwinger representation and is not removed by the fibre bound.

\emph{Vector and ghost sectors of the invariant sector.} The ghost operator is \(-\Box\), the same as the scalar of the preceding paragraph. On fibre-constant vector fields \(A_c(y)\) the cross term \(\eta_{ac}\eta_{bd}\mathcal J^{ab}\Sigma^{cd}\) of \(C_G\) equals \(-2s\mathcal J_{ab}A^b\) exactly (symbolic check), so \(H_V=-\Box-2s\mathcal J_{ab}A^b+\mu^2\) is \(C_G-C_{41}-C_\Sigma+\mu^2\) there. Write the diagonal of \(\mathrm e^{z\Delta_{H^4}+w\Delta_{H^3}}\) as \(D=D_0(1+D_1+\dots)\), with \(D_1\) depending on \(a\) and homogeneous of degree one in \((z,w)=(t-\mathrm is,\mathrm is)\); \(\operatorname{tr}(E+R/6)\) is the first Seeley--DeWitt density of \(\mathrm e^{t\Delta_{H^4}-\mathrm isH_V}\) in the convention that the exponent is \(\Delta+E\), and for one scalar component it equals \(D_1\). For the four components, with the \(4\times4\) matrix connection,
\[
  \operatorname{tr}\bigl(E+\tfrac16R\bigr)=4D_1+\frac{6s^2(1+a^2)}{t+\mathrm isa^2}-4\mathrm is\mu^2 ,
\]
the spin term being \(2s^2\operatorname{tr}[G\,\sigma(\Delta_{H^3})]=-2s^2\operatorname{tr}[G\,\sigma(C_{31})]\), with \(G\) the inverse of the symbol of the exponent, that is the Zeeman square \(f_e^2-f_m^2\) traced against \(G\). The route reproduces the exact scalar coefficient \(D_1\) to \(120\) digits at three points, and the vector and Dirac traces were verified to the same accuracy; the vector kernel itself was not computed. With \(x=s/t\) and the subtraction at \(x=1\) of the preceding paragraph, the weight-two functions are \(Q_\mu=-\mu^2j(a)\) with \(j(a)=2(1+\mathrm i/a)/(1+a^2)\), and \(Q_{\mathrm{sp}}=-8/(1+a^2)-\mathrm i\,4(3a^2+1)/(a^3(1+a^2))\) for the spin term, so \(\operatorname{Re}[Q_{\mathrm{sp}}+4Q_{\mu}]=16/(1+a^2)\) for \(\mu^2=-3\). For \(n_{\mathrm{ex}}\) further scalars of mass \(\mu_i^2\) the bosonic content has
\[
  \operatorname{Re}Q_{\mathrm{bos}}=(2+n_{\mathrm{ex}})\operatorname{Re}Q+\frac{16-2n_{\mathrm{ex}}\mu_i^2}{1+a^2},
\]
plus the scale-dependent term proportional to \(2+n_{\mathrm{ex}}\) of the preceding paragraph. The first term is indefinite and the second has the sign of \(8-n_{\mathrm{ex}}\mu_i^2\); the scale-dependent term has the sign of a logarithm. On the full leaf the spin term in a Gaussian window has a large-\(s\) tail \(C\,\mathrm ds/s\) with \(C\) purely imaginary and proportional to \(\sigma(C_{31})\) on the kernel plane, that is to \((1-a^2)/(1+2a^2)\), so its logarithmic coefficient is of indefinite sign on the leaf, and its real part depends on the contour angle.

\emph{Supertrace.} The matrix part of the coefficient is traceless, so it enters only through \(\operatorname{tr}\Sigma^{ab}\Sigma^{cd}\), and the species-independent part \(R/6+E\) is multiplied by the number of components. For the Dirac representation \(\operatorname{tr}\Sigma_D\Sigma_D=\tfrac12\operatorname{tr}\Sigma_V\Sigma_V\) for all index pairs. Supply, as an input not contained in the class, the sixteen real fermion components of the ten-dimensional supersymmetric matrix model with the square of the Dirac operator equal to \(\Box+s\Sigma^{ab}\mathcal J_{ab}\) on each component, no bilinear mass, and \(n_{\mathrm{ex}}=6\), and weight \(-\tfrac12\) per real fermion component. Then the component count \(4+6-2-8\) vanishes, the weighted index \(1-\tfrac12\cdot4\cdot\tfrac12\) vanishes, the Zeeman character is \(4(\cos sf_m-\cosh sf_e)^2=s^4(f_e^2+f_m^2)^2+\dots\) (the order \(s^4\) is a sum of the squares of the two invariants and does not vanish for any non-zero flux in Lorentzian signature), and what remains of the weight-two coefficient in the invariant sector is \(-\bigl(4\mu^2+n_{\mathrm{ex}}\mu_i^2\bigr)j(a)\), the mass supertrace times the mass moment \(j(a)\), with \(\operatorname{Re}j=2/(1+a^2)>0\); no sign of the mass supertrace itself is claimed. The mode-count term and the spin term of the order \(F^2\) both cancel identically; the curvature and connection part of the weight-two term therefore does not by itself carry the Newton coefficient for this content; whether it arises at higher order of the expansion or through the dependence on \(A\) is not computed.

This is a statement for the Poisson limit, one loop, the leading symbol and the invariant sector, the four-matrix class with \(\mu^2=-3\), Gaussian windows and the cone window of the stated form, the sampled points and the supplied fermion content with no bilinear fermion mass and the same window for bosons and fermions. The continuation of the shell identity to spacelike \(p\) with \(|p|\ge R\) is a numerical observation, and the sign of the cone-window moment is conditional on it; the vector kernel and the second variation under \(A\) are not computed; fermions are not part of the class; the Jacobian \(\varrho\) and the Liouville normalisation are not computed as functions of position. It does not treat Moyal terms or a window built from dynamical matrices, it identifies no induced metric with the emergent metric of Chapter~\ref{ch:vierbein-emergence} and, since a Euclidean coefficient is not a Lorentzian one, leaves Assumption~\ref{ass:lorentzian} in place (Problem~E). This changes no ledger label; Problem~F remains open.
```

Stale passages: none replaced. The 025 sentence "the Lorentzian moments are not computed in the fibre-bounded window, and the positivity of the moment is numerical" is superseded for Gaussian windows (proved) and, conditionally, for the cone window; the old sentence is left untouched.

## Changelog r1 -> r2
- F1: tangency sentence replaced by review snippet 1 (numerical observation; no unique-continuation or domain-of-dependence claim); sign and finiteness explicitly conditional on it; scope paragraph updated.
- F2: opening reference to g removed; D_1 defined (review snippet 4 plus "depending on a"; "for one scalar component it equals D_1"); E+R/6 convention stated; x = s/t defined at use.
- F3: 59 of 60 points, reason for the singular point, 1e-9 except base maximum 6e-5 (3000 directions).
- F4: review snippet 3 wording; log det with integrable logarithmic singularities at sigma = +-2 f_m at the leading symbol.
- F5: finiteness rests on the conditional shell formula; jump at the cone edge noted.
- F6: symbols renamed as above (f_e, f_m; K; j(a); varrho; N; N_W; bold x).
- F7: kernel-plane threshold |y^4| = ell named with the plane.
- F8: review snippet 5; sign -(4 mu^2 + n_ex mu_i^2) j(a) explicit.
- F9: not taken (optional).
- Five early script outputs saved as .out.txt; sd_scalar_vs_exact.py det check repaired (it now compares the determinant of the inverse metric with ell^2/m^2 and prints True).
- Remaining open step replaced by the review's ranked avenues.

## Verification scripts
In proposals/027-fibre-window-spin1/ (re-runnable; the sympy ones take minutes): sd_core.py; sd_scalar_vs_exact.py/.out.txt (new output, det check repaired); tangency_identity.py/.out.txt; shell_apex_lemma.py/.out.txt; cone_window_geometry.py/.out.txt; cone_window_moment.py/.out.txt (the four further new outputs); sd_vector_spin, sd_dirac_spin, gaussian_pv_lemma, invariant_sector_Q, closed_forms_Q, flux_window_growth, centre_flux_kernel, flux_closed_forms, spin_term_6d, spin_tail_6d, susy_sum_rules (.py/.out.txt as in r1); compile_check_r2.py/.out.txt (this round); helpers cp12_realisation.py, symbol_tools.py, sym_signatures.py. cone_window_geometry.out.txt and flux_closed_forms.out.txt contain numpy divide-by-zero warnings from the singular sample point.

## Decisions Taken
- Withdrew the domain-of-dependence mechanism rather than seeking a replacement proof; kept the numerical observation and tied the sign and finiteness to it (a proof of the continuation, or a window with |p| < r, is ranked third below).
- Renamed symbols myself (routine notation choice): f_e, f_m, K, j(a), varrho, N, N_W, bold x.
- Stated the singular-point cause as the visible numerical one and did not re-sample; the accuracy statement is the honest one.
- F9 not taken.

## Milestone assessment
Routine. One proved lemma, a conditional cone-window moment, a bounded supertrace remainder; no critical-path step derived.

## Status-label recommendation
None. Problem F remains OPEN, CRITICAL PATH, PROGRAMME-CONDITIONAL; Problem E remains open.

## Author decision needed
none

## Remaining open step
Hypothesis class of the no-go: Poisson limit, one loop, leading symbol; invariant (s = 0, fibre-constant) sector; four-matrix class with mu^2 = -3; Gaussian windows or the cone window of the stated form; supplied fermion content with no bilinear mass and equal bosonic and fermionic window; weight-two term at A = 0, species-independent part. Ranked open avenues (review-r1):
1. The A-dependence (second variation under the matrix fluctuation) of the mass-supertrace term, and the order-s^4 term with the Zeeman character, i.e. (f_e^2+f_m^2)^2. The count and index cancellations remove only the species-independent part.
2. Fermion content or mass pattern beyond "no bilinear mass" (supersymmetric bilinears, fermion masses, the eight-matrix (5,1) set), where the mass supertrace need not vanish or have indefinite sign; relaxes the supplied-input hypothesis.
3. A window with |p| < r, or a proof of the continuation of the shell formula, to turn the conditional sign into a theorem.
4. Exact vector kernel and Plancherel in the five-matrix presentation (tests the SD-coefficient-as-weight-two-term assumption).
5. The real/imaginary identification of the action; non-Gaussian windows built from dynamical matrices.
6. Moyal terms and the SO(4,1) to SO(3,1) branching for the non-central C31.

## Special instructions for the gatekeeper
- Do not read the block as giving a sign of G_eff or w; the positive moment multiplies a mass input.
- The sign of Re N_W and the finiteness of N_W are conditional on a numerical observation; the block asserts no mechanism. Check that no sentence still says "unique continuation" or "domain of dependence" (the only remaining "Lipschitz" is in the explicit statement that the window function is not Lipschitz at the cone edge; in the block it appears as "jump").
- Check that D_1, x, j(a), varrho, N, N_W, K, f_e, f_m are each defined at first use, and that no g remains.
- The changed sentences are wording of review snippets 1, 3, 4, 5; no recalculation was required, and the scripts are unchanged except the det check.
- block-r2.tex has LF endings; the integrator converts to CRLF.
