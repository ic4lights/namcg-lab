import os, re
here = os.path.dirname(os.path.abspath(__file__))
fence = '`' * 3
m = open(os.path.join(here, 'proposal-r1.md'), encoding='utf8').read()
blk = open(os.path.join(here, 'block-r2.tex'), encoding='utf8').read()
m = re.sub(fence + r'latex\n.*?' + fence, lambda _: fence + 'latex\n' + blk + fence, m, count=1, flags=re.S)
def rep(a, b):
    global m
    assert m.count(a) == 1, a[:60]
    m = m.replace(a, b)
rep('# Proposal 025-lorentzian-window, round 1', '# Proposal 025-lorentzian-window, round 2')
rep("(a) The Poisson-limit fibre is a compact S^2 with unbounded harmonic number (this is what 018-023 call \"unbounded fibre\").",
    "(a) The Poisson-limit fibre is a compact S^2; |zeta| is unbounded in the Poisson limit and expected to be bounded by the fibre harmonic number.")
rep("Admissibility (1910.00839 eq (3.44), footnote 8) has the symbol-level content -sigma(C42)>=0 (a cone), conditional on the footnote-8 identification. With the cone and any fibre bound, a function of the central C42 is a compact window and kappa is not needed (kappa only rescales Lambda^2 by 2kappa-1 at fixed fibre bound).",
    "Admissibility (1910.00839 eq (3.44), footnote 8) has the symbol-level content -sigma(C42)>=0 (a cone), conditional on the footnote-8 identification. The cone only restricts to the admissible sector; it is not what bounds the window. The fibre bound beta q_f <= Q is a cutoff of S^2 = 2C41 - C42, so it relaxes the hypothesis of 023 and does not contradict 023 (i), which stands for functions of C42 alone. At fixed fibre bound kappa only rescales Lambda^2 by 2kappa-1 and the divergence at kappa->1 is absent. The Lorentzian moments, flux and exact-sector results are for the Gaussian Delta_kappa window, not for the fibre-bounded window.")
rep("reproduces the appendix density (5m^2-3 ell^2)/(4m^2) by an independent route, and gives the windowed Lorentzian weight-two function Q(a): Re Q changes sign at a=sinh(tau)~0.62 (not at a^2=3/5) and Im Q->pi; it carries a scale-dependent term -2 ln(mu^2 t) proportional to the mode count (cancels only if N_b=N_f at this order).",
    "reproduces the Seeley-DeWitt coefficient (5m^2-3 ell^2)/(4m^2), whose product with sqrt|G| = m^-4 is the density (5m^2-3 ell^2)/(4m^6) of the preceding paragraphs, by an independent route, and gives the windowed Lorentzian weight-two function Q(a): Re Q is indefinite; with the subtraction at x=1 it changes sign at a=sinh(tau)~0.62 (not at a^2=3/5), a location that moves with the subtraction point and has no invariant meaning; Im Q->pi. It carries a scale-dependent term -2 ln(mu^2 t) proportional to the mode count (the R/6 curvature of the auxiliary H^4 window geometry; cancels only if N_b=N_f at this order).")
rep("c_s = 5/4-3/(4a^2) = (5m^2-3 ell^2)/(4m^2), identical to the independent computation of a_1 for the appendix operator (a1_invariant_sector.py: R/6 - omega^2 - div omega) and to the appendix density.",
    "c_s = 5/4-3/(4a^2) = (5m^2-3 ell^2)/(4m^2), the Seeley-DeWitt coefficient, identical to the independent computation of a_1 for the appendix operator (a1_invariant_sector.py: R/6 - omega^2 - div omega); times sqrt|G| = m^-4 it is the appendix density (5m^2-3 ell^2)/(4m^6).")
rep("the invariant-sector a_1 is indefinite", "the invariant-sector a_1 is indefinite")
rep("sign change of Re Q at a~0.62.", "Re Q indefinite (root a~0.62 only with the subtraction at x=1; it moves with the subtraction point).")
rep("c_s = (5a^2-3)/(4a^2) from two independent computations", "c_s = (5a^2-3)/(4a^2) from two independent computations (review-r1 re-derived it)")
rep("the log det is finite;", "the log det has integrable logarithmic singularities at sigma=+-2b;")
rep("kappa-rescaling lemma.", "kappa-rescaling lemma (for the fibre-bounded window; not used in the Gaussian-window moments).")
rep("Re-check: the Gaussian moments", "Re-check: that the flux and exactness statements are scoped to the Delta_kappa Gaussian window; the Gaussian moments")
# sections
i = m.index('## Remaining open step'); j = m.index('## Special instructions')
m = m[:i] + """## Remaining open step
To close the weight-two coefficient: the second variation of the windowed Lorentzian trace under A for the vector, ghost and scalar sectors including fibre harmonics; the supertrace or fermionic content that removes the mode-count term; a regulator built from the dynamical matrices; and the sign of the result, which cannot be read from this package.

Ranked open avenues (review-r1):
1. Lorentzian moments in the fibre-bounded cone window (q_f <= Q), not computed here.
2. Exact SO(4,1) spin-1 (Plancherel or finite-N) trace, extending the exact sector to vector and ghost.
3. Weyl second variation under A in the Gaussian window.
4. Supertrace/fermionic content to remove the mode-count term.
5. A window built from dynamical matrices only (exact finite-N trace).
6. Reconcile s <= n with s <= x^0/r (T^i diagonal sphere versus SU(2)_L radius).
7. The eight-matrix (5,1) Hessian.
8. Moyal terms.

""" + m[j:]
m = m.replace("## Source reading", """## Changelog from round 1 (review-r1: ACCEPT WITH REQUIRED REVISIONS, OPEN 0/3, no PRIOR-CLAIM-ERROR)
- F1: block now says 023 (i) stands for functions of C42 alone; the cone only restricts to the admissible sector; beta q_f <= Q is a cutoff of S^2 = 2C41 - C42 and relaxes 023's hypothesis; the Lorentzian moments, flux and exact-sector results are for the Gaussian Delta_kappa window; "divergence at kappa->1 is absent" replaces "at the ends of the interval"; "Delta_kappa is not needed" removed.
- F2: density wording fixed in block and body: Seeley-DeWitt coefficient (5m^2-3 ell^2)/(4m^2), times sqrt|G| = m^-4 gives (5m^2-3 ell^2)/(4m^6).
- F3: Re Q indefinite; root 0.62 tied to the subtraction at x=1 and moving with it; mode-count term identified as R/6 of the auxiliary H^4 window geometry.
- F4: "unbounded fibre" quotation and attribution removed.
- F5: "equivalent, by (2.7) and (3.43), to -C42 > 9/2 in that convention"; footnote 8 printing noted.
- F6: integrable logarithmic singularities at sigma=+-2b; "at the leading symbol and at the sampled points" added.
- Remaining open step replaced by the review's ranked avenues. No label change. Calculations unchanged (scripts of r1 unchanged); block-r2.tex built by make_r2.py and equals the block below.

## Source reading""",1)
m = m.replace("`compile_check_r1.py` / `.out.txt`: scratch copy", "`make_r2.py`, `make_md_r2.py`: build block-r2.tex from block-r1.tex by the review substitutions (each asserted once) and this file.\n- `compile_check_r2.py` / `.out.txt`: (r1 script adapted to r2) scratch copy")
open(os.path.join(here, 'proposal-r2.md'), 'w', encoding='utf8', newline='\n').write(m)
