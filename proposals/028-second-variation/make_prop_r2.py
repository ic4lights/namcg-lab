import os
here = os.path.dirname(os.path.abspath(__file__))
blk = open(os.path.join(here, 'block-r2.tex'), encoding='utf8', newline='').read().replace('\r\n', '\n').strip()
r1 = open(os.path.join(here, 'proposal-r1.md'), encoding='utf8').read()


def sect(name, nxt):
    a = r1.index('## ' + name)
    b = r1.index('## ' + nxt)
    return r1[a:b]


def sub(s, a, b):
    assert s.count(a) == 1, a[:50]
    return s.replace(a, b)


res = sect('Result', 'Target and status')
res = sub(res, "The coefficient of any Einstein-Hilbert-form term at the order of the 025-027 weight-two coefficient is exactly zero for every A: the count term, the spin term (quadratic in the Zeeman operator) and the cubic term vanish identically. What remains at that order is -M_str Tr[chi H_X^{-1}], M_str = 4 mu^2 + n_ex mu_i^2.",
         "Exactly zero for every A are only the count term, the spin term (quadratic in the Zeeman operator) and the cubic term. What remains without Z insertions is +M_str Tr[chi Phi'(H_X)] (for Phi = exp(-.): -M_str Tr[chi e^{-H_X}]), M_str = 4 mu^2 + n_ex mu_i^2; at the leading symbol it is proportional to M_str times the moment of 1/(sigma_X - i0). Nothing is claimed about the next-to-leading symbol of that term.")
res = sub(res, "Its second variation therefore has no term with more than one derivative of A, i.e. no derivative term in the fluctuation of K^{mu nu}, hence none of EH form. For the Gaussian window of Delta_{3/4} its Hessian along alpha is indefinite (40 of 59 draws; 5 positive, 14 negative definite) and not gauge invariant (`mass_moment_hessian.py`, `mass_moment_stats.py`).",
         "This leading-symbol term depends on A only through its first derivatives, so its second variation has no second-derivative term and no EH-form term; the next-to-leading symbol (second jet of X) is not computed, and no K^{mu nu} or metric-fluctuation reading is used. The Hessian of the real (PV) part for the Gaussian window of Delta_{3/4} is numerical, at frozen coefficients and phi = pi/2: indefinite in 40 of 59 draws (5 positive, 14 negative definite), numerically nonzero along alpha ~ q in all draws with non-null q (`mass_moment_hessian.py`, `mass_moment_stats.py`).")
res = sub(res, "The A-dependence of the flux at leading q is exactly F_ab -> F^0_ab + eps c (xi.Y_q)(q_a alpha_b - q_b alpha_a). The Gaussian averages of the order-F^4 block depend on q.y at fixed q.q (factor > 2 over rapidity 1.2), and the non-invariant part (|phi|^2 = E^2+B^2 type) is 2 to 180 times the invariant part at eight orbit points (`lorentz_diag.py`, integrand level at one proper time).",
         "At the phase phi = 0 (first-jet terms vanish) and leading q, the flux shift is F_ab -> F^0_ab + eps c (xi.Y_q)(q_a alpha_b - q_b alpha_a); at general phase the sin(phi) term is also present. At fixed proper time and kappa = 3/4 the Gaussian averages in the order-F^4 integrand depend on q.y at fixed q.q (factor > 2 over rapidity 1.2), through y^mu and the window (not separated by the diagnostic). Proposal only: the non-invariant part (|phi|^2 = E^2+B^2 type) is 2 to 180 times the invariant part at eight orbit points (`lorentz_diag.py`; norms of different tensors, one proper time).")
res = sub(res, "This is the same structural type as the Lorentz-violating K-free term of Steinacker (a time-like vector field); no equation-level match is claimed.",
          "Proposal only: this resembles the time-like-vector-field Lorentz violation noted by Steinacker; no equation-level match is claimed and it is not in the LaTeX.")
tgt = sect('Target and status', 'Source reading')
src = sect('Source reading', 'Research and reasoning')
rr = sect('Research and reasoning', 'Claim classification')
rr = sub(rr, "first mass constant M_str = 4 mu^2 + n_ex mu_i^2 (= -12 + 6 mu_i^2 at mu^2 = -3; zero at mu_i^2 = 2, the Pauli condition str(k_1 m^2) = 0 of Visser eq. 35 with k_1 equal for all components)",
         "first mass constant M_str = 4 mu^2 + n_ex mu_i^2 (= -12 + 6 mu_i^2 at mu^2 = -3; zero at mu_i^2 = 2). Correction (F6): this is the condition str(m^2) = 0, Visser eq. 33; it is not eq. 35, str(k_1 m^2) = 0, because k_1 differs by species (Visser Table 1: 1/6 for a minimal scalar, -1/3 for a Dirac spinor). Neither equation is used in the LaTeX")
rr = rr.replace("with mu_i^2 = 2 the Pauli point and", "with mu_i^2 = 2 the str(m^2) = 0 point and")
rr = sub(rr, "(Gaussian lemma of 027). The Hessian along alpha is indefinite (see above).",
         "(Gaussian lemma of 027). The Hessian of the real (PV) part along alpha is indefinite in the sampled draws (numerical, frozen coefficients, phi = pi/2).")
rr += """**Sign convention (F1).** m_i is a scalar, so the first-order term without Z insertions is +M_str Tr[chi Phi'(H_X)]; Phi = exp(-.) gives -M_str Tr[chi e^{-H_X}] (the `duhamel_toy.py` convention, c_2). With the 027 convention Sigma ln = -int ds/s Tr e^{-is(H - i eps)}, Phi'(H) = 1/(H - i0), so the leading-symbol term is +M_str int chi (sigma_X - i0)^{-1}; the minus sign in 027's "-(4 mu^2 + n_ex mu_i^2) j(a)" belongs to its Q-convention (Sigma ln = -(4 pi)^{-2} Lambda^2 Q). The LaTeX states only proportionality to M_str and the moment, and no sign of G_eff. Terms linear in m with two Z insertions are the separate constant c_12.

**Flux shift (F2).** Ham(F^{ab}) = s c_ab + eps s (alpha^a q^b - alpha^b q^a)[sin(phi) Ham(M^{45}) + m cos(phi) Y_q]. At phi = 0 the sin term and the shift of W vanish and F is exactly linear in eps ({cos phi, cos phi} = 0); `lorentz_diag.py` is an evaluation at that phase, isolating the second-jet (dA)^2 structure. At general phase the first-order sin(phi) term is present.

## Changelog r1 -> r2
- F1 (major): sign fixed: "+M_str Tr[chi Phi'(H_X)] ... without insertions of Z (for Phi = exp(-.): -M_str Tr[chi e^{-H_X}])"; (ii) now "proportional to M_str int chi (sigma_X - i0)^{-1}".
- F2 (major): flux shift stated at phi = 0 where the first-jet terms vanish; "only through" removed.
- F3 (major): K^{mu nu} language dropped; text now "depends on A only through its first derivatives ... next-to-leading symbol, which involves the second jet of X, is not computed"; Result item 2 restricted to count, spin and cubic terms.
- F4 (minor): "its integrand", "through y^mu and the window", "at fixed proper time and kappa = 3/4"; 2-180 ratio and Steinacker comparison kept out of the LaTeX.
- F5 (minor): Hessian of the real (PV) part, numerical, frozen coefficients, phi = pi/2; "numerically nonzero in all draws with non-null q" replaces the gauge-invariance reason.
- F6 (proposal body): Visser eq. 33 (str m^2 = 0) vs eq. 35, k_1 species-dependent, corrected above.
- Remaining open step replaced by the review's ranked avenues. `make_block_r2.py` derives block-r2.tex from block-r1.tex by exact asserted replacements; `compile_check_r2.py` re-verified the anchor and the build.

"""
rest = r1[r1.index('## Claim classification'):r1.index('## Proposed changes')]
rest = sub(rest, "- Vanishing of the EH-form part at the weight-two order for every A: conditional on the class hypotheses and on the leading-symbol reading of the mass term.",
           "- Vanishing of the count, spin and cubic terms for every A: established algebra (formal expansion). Absence of second-derivative (EH-form) terms in the leading-symbol mass term: established within the leading symbol; the next-to-leading symbol is unresolved.")
rest = sub(rest, "- Indefinite mass-moment Hessian: numerical, sampled.",
           "- Indefinite Hessian of the real (PV) part of the mass moment: numerical, sampled, frozen coefficients, phi = pi/2.")
pc = "## Proposed changes\nFile `chapters/appH-microscopic-proofs.tex`. Anchor: `\\section{Problem G: HBEV}`, occurring exactly once (re-verified by `compile_check_r2.py` on the current working tree); insert immediately before it, after the 027 block whose last sentence is \"This changes no ledger label; Problem~F remains open.\" Nothing existing is removed or replaced. Label used: `ch:vierbein-emergence` (exists). No `\\cite`, no bib entry. The block is identical to `block-r2.tex`:\n\n```latex\n" + blk + "\n```\n\nStale passages elsewhere: none found; the 027 sentence \"whether it arises at higher order of the expansion or through the dependence on \\(A\\) is not computed\" stays true.\n\n"
tail = """## Verification scripts
As in r1 (outputs `*.out.txt`), plus: `make_block_r2.py` (exact replacements r1 -> r2, each asserted unique), `compile_check_r2.py` / `compile_check_r2.out.txt` (scratch copy outside the repo, deleted afterwards: anchor unique, 0 errors, 0 undefined, 0 multiply defined, 0 double subscripts, 289 pages). `mass_moment_stats.out.txt` supports "nonzero in all draws with non-null q" (finite cases with |q|^2 > 1e-3).

## Decisions Taken
- Sign: state the Phi'-form with explicit exp specialisation, and no sign of G_eff (F1).
- Drop the K^{mu nu} language rather than state a hypothesis, keeping the block independent of an unestablished map from A to a metric fluctuation (F3).
- Evaluation phase phi = 0 stated explicitly (F2).
- Earlier decisions of r1 unchanged (no ad hoc cutoff; formal expansion; no bib change; spacetime emergent).

## Milestone assessment
Routine/conditional sharpening; no trigger. Not a breakthrough.

## Status-label recommendation
None. F, E and all critical-path labels unchanged.

## Author decision needed
None.

## Remaining open step (ranked avenues)
No-go hypothesis class: Poisson limit, one loop, leading symbol, CP^{1,2} four-matrix class with mu^2 = -3, vanishing transverse matrices, supplied 16-component fermions without bilinear mass, species-independent window from fixed T, formal Duhamel expansion.
1. Nilpotent (Landau) resummation of the non-expanded logarithm: finite, hypoelliptic, the direct route to an F^4 constant; relaxes the Schwinger expansion.
2. Next-to-leading symbol of the M_str term on the six-dimensional leaf (R/6 + E structure): the only place an EH-form piece can enter in this class; relaxes "leading symbol".
3. Fermion mass patterns (scalar m_F or matrix bilinears): break T_2 = 0; relax "no bilinear mass".
4. Transverse flux / fuzzy K with the mixed invariant: relaxes "transverse matrices vanishing".
5. Species- or A-dependent windows: relaxes the common window and breaks the lemma.
6. Eight-matrix sets and Moyal terms.
Afterwards still needed for F/E: the map from the fibre-integrated quadratic form to the linearised Einstein form of the emergent metric, and a derivation of the matrix content. None is done here.

## Special instructions for the gatekeeper
- The block says the count, spin and cubic terms vanish for all A, that the leading-symbol mass term depends only on the first jet, and that the next-to-leading symbol and the F^4 constant are not computed. It does not say an EH term is absent in general.
- The n = 3 cancellation depends on Z_D = -Sigma_D with Z_V = -Sigma_V (re-run `tensors_lemma.py`); the lemma is a formal expansion.
- Lorentz and Hessian numbers are integrand-level or sampled, at fixed proper time, kappa = 3/4, frozen coefficients: diagnostics, not coefficients.
- Visser and Steinacker are not cited in the LaTeX.
"""
open(os.path.join(here, 'proposal-r2.md'), 'w', encoding='utf8').write("# Proposal 028-second-variation, round 2\n\n" + res + tgt + src + rr + rest + pc + tail)
