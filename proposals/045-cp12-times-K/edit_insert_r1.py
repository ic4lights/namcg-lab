"""edit_insert_r1.py (proposal 045): wording edits applied to appH_insert.tex; each old string must occur once."""
p = 'appH_insert.tex'
s = open(p, encoding='utf-8').read()
reps = [
(r"At the leading symbol, for any fibre dependence of the amplitude, \(\delta E^{a\mu}=\alpha^a v^\mu\) up to a constant phase, with \(\alpha=\sum_in^ic_i\) and \(v=\sum_jn^js_j\), so the frame perturbation at a fibre point has rank one, and \(\delta T^{ab\mu}=-m\,v^\mu(q^a\alpha^b-q^b\alpha^a)\) (Lie--Poisson computation at points of an explicit realisation of the orbit, relative residual \(3\cdot10^{-14}\)).",
 r"At the leading symbol, for an amplitude \(\alpha^a\) with any dependence on the fibre point, \(\delta E^{a\mu}=\alpha^a v^\mu\) up to a constant phase, with \(v=\sum_jn^js_j\), so the frame perturbation at a fibre point has rank one, and \(\delta T^{ab\mu}=-m\,v^\mu(q^a\alpha^b-q^b\alpha^a)\); for the level-one amplitudes \(\alpha=\sum_in^ic_i\) (verified by a Lie--Poisson computation at points of an explicit realisation of the orbit, relative residual \(3\cdot10^{-14}\))."),
(r"At a fibre point the six polarisations do source axial torsion, in the second fibre harmonic, which averages to zero and vanishes identically only for \(D\propto\mathbb I\) (exact rational arithmetic at seven sampled base points and wave vectors).",
 r"At a fibre point the six polarisations do source axial torsion, proportional to \([D,nn^{T}]\) and so in the second fibre harmonic; it averages to zero and vanishes identically only for \(D\propto\mathbb I\) (exact rational arithmetic in seven sampled cases: four base points, five wave vectors including a time-like one, both orientations of the fibre basis)."),
(r"\emph{Two-derivative forms.} In the normalisation of the preceding paragraph the index density at a fibre point is",
 r"\emph{Two-derivative forms.} In the normalisation of the preceding paragraph, for a real wave averaged over its phase, the index density at a fibre point is"),
(r"The same routine gives, on the two modes with \(\delta\rho=0\) of four coordinates, the index form \(-4\) and the scalar form \(\tfrac16\) times the Einstein--Hilbert form.",
 r"With these densities the two modes with \(\delta\rho=0\) of four coordinates have the index form \(-4\) and the scalar form \(\tfrac16\) times the Einstein--Hilbert form, as in the preceding paragraph."),
(r"on the five traceless polarisations and \(-\tfrac5{24}W_R+W_X\) on the trace polarisation.",
 r"on the five traceless polarisations and \(-\tfrac5{24}W_R+W_X\) on the trace polarisation, their complement in the six."),
(r"For this trace no single \(G_T\) covers the six polarisations or the five traceless ones, and the mixed-term part of the fixed-state gap vanishes on none of the five.",
 r"For this trace no single \(G_T\) covers the six polarisations or the five traceless ones, and \(-2\) is not a generalised eigenvalue of the index form at any sampled point, so the mixed-term part of the fixed-state gap vanishes on no traceless polarisation."),
(r"which that work states is not Lorentz invariant a priori; this part is not suppressed there and is not computed here.",
 r"which that work states is not Lorentz invariant a priori and finds subdominant for a scale of \(K\) above the fibre scale, a condition that fails in that regime; this part is not computed here."),
]
for a, b in reps:
    n = s.count(a)
    assert n == 1, (n, a[:70])
    s = s.replace(a, b)
open(p, 'w', encoding='utf-8', newline='\n').write(s)
print("applied", len(reps), "edits; bytes", len(s.encode('utf-8')))
