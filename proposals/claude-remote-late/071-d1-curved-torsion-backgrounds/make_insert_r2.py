"""Build appH_insert_r2.tex from appH_insert_r1.tex by the exact replacements of round 2
(each asserted to occur once).  Output CRLF, UTF-8 without BOM.  Run: python -I make_insert_r2.py"""
import hashlib
from pathlib import Path
here = Path(__file__).resolve().parent
s = (here / 'appH_insert_r1.tex').read_bytes().decode('utf-8').replace('\r\n', '\n')
R = [
 ('A', r"but give the connection constant components \(\omega_a{}^{cd}=w_a{}^{cd}\) in this frame.",
  r"but give the connection constant components \(w_a{}^{cd}\) in this frame, normalised so that the first-order part of \(\mathbb D_a\) at \(u=1\) is \(E_a+\tfrac12w_a{}^{cd}\mathcal S_{cd}\), the sign of the fluctuation \(\tfrac12\omega_a{}^{cd}\mathcal S_{cd}\) below; in the coordinate form of the paragraph on local \(\mathrm{SO}(3,1)\) inside the unitary group this is \(e_a{}^\mu\omega_\mu{}^{cd}=-w_a{}^{cd}\)."),
 ('S', r"\(\mathsf R_{abcd}\mathsf R^{abcd}=0\), \(\mathsf T_{abc}\mathsf T^{abc}=0\), \(\mathsf R_{ab}{}^{ab}=-2sm_1\), and",
  r"\(\mathsf R_{abcd}\mathsf R^{abcd}=\mathsf R_{ab}{}^{ab}=0\), \(\mathsf T_{abc}\mathsf T^{abc}=0\), and"),
 ('D', r"with \(w_a{}^{cd}=k_a(\zeta N^{cd}+xN'^{cd})\). The torsion is trace-free,",
  r"with \(w_a{}^{cd}=k_a(\zeta N^{cd}+xN'^{cd})\) and \((\zeta,x)\neq(0,0)\). The torsion is trace-free, so \(\mathsf t=0\) and the third bracket holds,"),
 ('H', r"is cancelled in the first bracket by the torsion terms. ",
  r"is cancelled in the first bracket by the torsion terms. On the algebra of (ii) the wider ansatz \(w_a{}^{cd}=k_a(aB^{cd}+\zeta N^{cd}+xN'^{cd})\) solves all three brackets for all real \(\kappa,a,\zeta,x\): \(\mathsf T_{ac}{}^c=a\,k_a\), the only nonzero pair of \(\mathsf F\) is \(\mathsf F_{13}=\tfrac12a\kappa\), the only nonzero pair of \(\mathsf R\) is \(\mathsf R_{13}{}^{cd}=\kappa(aB^{cd}+\zeta N^{cd}+xN'^{cd})\), and \(\mathsf R_{abcd}\mathsf R^{abcd}=-4a^2\kappa^2\), \(\mathsf R_{ab}{}^{ab}=0\), \(\mathsf T_{abc}\mathsf T^{abc}=2\kappa^2\) (exact for the section values; for the operators on the bundle at random Lorentz \(u\), including the order-zero part, residual below \(10^{-15}\)). For \(a\neq0\) it is an exact solution with \(\mathsf R_{abcd}\mathsf R^{abcd}\neq0\) on a unimodular algebra. "),
 ('C', r"with \(\mathsf c\) free, solutions with \(\mathsf R_{abcd}\mathsf R^{abcd}\neq0\) were found on algebras with a two-dimensional abelian derived algebra (numerical, not a classification)",
  r"with \(\mathsf c\) free, solutions of the first two brackets with \(\mathsf R_{abcd}\mathsf R^{abcd}\neq0\) were found on algebras with a two-dimensional abelian derived algebra, not all unimodular, for which the order-zero field and the third bracket are not examined (numerical, not a classification)"),
 ('B', r"Conversely the forty equations drop rank at random complex points of these cones (numerical; the relative smallest singular value is \(10^{-16}\) for \(m=(0,2,0,0)\), and between \(3\cdot10^{-10}\) and \(5\cdot10^{-5}\) at the trace-free point, against \(10^{-4}\) to \(3\cdot10^{-3}\) at random points off the cones, so that the converse is clean only for \(m=(0,2,0,0)\)).",
  r"Conversely the forty equations drop rank at random complex points of each of these cones (numerical; the relative smallest singular value is about \(10^{-16}\) at both points, against \(3\cdot10^{-5}\) to \(3\cdot10^{-2}\) at random points off the cones)."),
 ('SC1', r"left-invariant backgrounds with constant connection, the two families named,",
  r"left-invariant backgrounds with constant connection, the families named,"),
 ('SC2', r"Family (ii) and the survey solutions with \(\mathsf R_{abcd}\mathsf R^{abcd}\neq0\), for which no scaling symmetry is shown, are not linearised here,",
  r"Family (ii), its extension with \(a\neq0\) and the survey solutions with \(\mathsf R_{abcd}\mathsf R^{abcd}\neq0\), for which no scaling symmetry is shown, are not linearised here,"),
]
for tag, old, new in R:
    assert s.count(old) == 1, (tag, s.count(old))
    s = s.replace(old, new)
    print('replacement', tag, 'applied once')
b = s.replace('\n', '\r\n').encode('utf-8')
(here / 'appH_insert_r2.tex').write_bytes(b)
print('appH_insert_r2.tex bytes', len(b), 'sha256', hashlib.sha256(b).hexdigest(), 'bare LF', b.count(b'\n') - b.count(b'\r\n'))
