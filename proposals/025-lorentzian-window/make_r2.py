"""Builds block-r2.tex from block-r1.tex by the review-r1 substitutions; asserts each applies once."""
import os
here = os.path.dirname(os.path.abspath(__file__))
t = open(os.path.join(here, 'block-r1.tex'), encoding='utf8').read()
subs = [
(r"its harmonic number, equivalently the centre variable \(\zeta\), is unbounded; this is the sense of ``unbounded fibre'' in the preceding paragraphs. Two bounds",
 r"\(|\zeta|\) is unbounded; it is expected to be bounded by the fibre harmonic number of the quantum space. Two bounds"),
(r"equivalent to \(-C_{42}>9/2\) in that convention (stated there as plausible, not proved, for the \(SO(4,2)\) content of \(\operatorname{End}(\mathcal H_n)\))",
 r"equivalent, by (2.7) and (3.43) of that reference, to \(-C_{42}>9/2\) in that convention (its footnote~8 prints \(C_2[\mathfrak{so}(4,2)]>9/2\) and states the identification with the \(SO(4,2)\) content of \(\operatorname{End}(\mathcal H_n)\) as plausible, not investigated)"),
(r"so a function of the central operator \(C_{42}\) regularises once the fibre is bounded. In that case \(\Delta_\kappa\) is not needed: for fixed \(Q\)",
 r"so a function of the central operator \(C_{42}\) regularises once the fibre is bounded. The cone restricts to the admissible sector and is not what bounds the window: the bound \(\beta q_f\le Q\) is a cutoff of \(S^2=2C_{41}-C_{42}\), so this relaxes the hypothesis of the preceding paragraph and does not contradict it, whose consequence~(i) for functions of \(C_{42}\) alone stands. The Lorentzian moments, the flux and the exact-sector results below are for the Gaussian window of \(\Delta_\kappa\), not for this fibre-bounded window. For fixed \(Q\)"),
(r"the divergence of the window volume at the ends of the interval is absent.", r"the divergence at \(\kappa\to1\) is absent."),
(r"is finite. The exponential growth", r"has integrable logarithmic singularities at \(\sigma=\pm2b\). The exponential growth"),
(r"is absent order by order in the flux (each order is a polynomial in \(s\) times \(e^{-is\sigma}\)) and for the magnetic pair, and is present",
 r"is absent order by order in the flux (each order is a polynomial in \(s\) times \(e^{-is\sigma}\)) and for the magnetic pair, at the leading symbol and at the sampled points, and is present"),
(r"the Seeley--DeWitt coefficient \((5m^2-3\ell^2)/(4m^2)\), \(m=y^4\), the formal density of the preceding paragraphs obtained by an independent route.",
 r"the Seeley--DeWitt coefficient \((5m^2-3\ell^2)/(4m^2)\), \(m=y^4\), whose product with \(\sqrt{|G|}=m^{-4}\) is the density \((5m^2-3\ell^2)/(4m^6)\) of the preceding paragraphs, obtained by an independent route."),
(r"plus \(-2\) times a scale-dependent logarithm proportional to the number of modes; \(\operatorname{Re}Q\) changes sign at \(a\simeq0.62\) (not at \(a^2=\tfrac35\), the zero of the coefficient above) and is positive above, and \(\operatorname{Im}Q\to\pi\).",
 r"plus \(-2\) times a scale-dependent logarithm proportional to the number of modes, which is the \(R/6\) curvature term of the auxiliary \(H^4\) window geometry; \(\operatorname{Re}Q\) is indefinite, and with the subtraction at \(x=1\) it changes sign at \(a\simeq0.62\) (not at \(a^2=\tfrac35\), the zero of the coefficient above), a location that moves with the subtraction point and has no invariant meaning; \(\operatorname{Im}Q\to\pi\)."),
(r"the admissible cone is conditional on the identification stated, and the positivity of the moment is numerical.",
 r"the admissible cone is conditional on the identification stated, the Lorentzian moments are not computed in the fibre-bounded window, and the positivity of the moment is numerical."),
]
for a, b in subs:
    assert t.count(a) == 1, a[:50]
    t = t.replace(a, b)
open(os.path.join(here, 'block-r2.tex'), 'w', encoding='utf8', newline='\n').write(t)
print('ok')
