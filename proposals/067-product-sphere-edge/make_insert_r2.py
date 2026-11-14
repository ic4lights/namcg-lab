"""
067 round 2: builds appH_insert_r2.tex from the round-1 appH_insert.tex by exact, single-occurrence replacements,
one per gatekeeper finding (F1, F2+F6, F2, F3, F4), and prints a unified diff. Writes only appH_insert_r2.tex in
this folder.
"""
import difflib, hashlib, os

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, 'appH_insert.tex'), 'rb').read().decode('ascii')
assert hashlib.sha256(src.encode()).hexdigest() == '4ee4d8920f7bd8c5e4cbb9516036cf175cf8fdee9c6bb2d96e82cbe8a5b6bb52'

EDITS = []

# F1 (Dimension): sampled values instead of a range; grid extrema from e5
EDITS.append(('F1',
r"""the Weyl dimension formula gives \(\mathrm d\log d/\mathrm d\log M=2r\ell\) to within \(2\%\) for \(M\ge4000\), \(r\le160\), \(\ell\le40\), and \(\log d=2r\ell\,[\log(M/(r+\ell))+c]\) with \(0.80<c<0.97\) for \(1\le r\le160\), \(4\le\ell\le400\), \(M=4000\) and \(16000\); for \(r>1\) this is below \(r\) times the value for one row on each side, by a factor between \(0.69\) and \(0.98\) in that range (numerical)""",
r"""the Weyl dimension formula, evaluated at \((r,\ell)=(1,40)\), \((4,40)\), \((16,40)\), \((40,40)\), \((160,40)\), \((40,4)\) and \((40,400)\) with \(M=4000\) and \(16000\), gives \(\mathrm d\log d/\mathrm d\log M=2r\ell\) to within \(2\%\) in the six cases with \(\ell\le40\), and \(\log d=2r\ell\,[\log(M/(r+\ell))+c]\) with \(0.80<c<0.97\) in all of them; for \(r>1\) this is below \(r\) times the value for one row on each side at the same \(M\), by a factor between \(0.69\) and \(0.99\) in these cases. At the points with \(r\) equal to \(1\), \(2\), \(4\), \(8\), \(16\), \(40\), \(80\) or \(160\) and \(\ell\) equal to \(4\), \(8\), \(16\), \(40\), \(100\), \(200\) or \(400\), with the same two values of \(M\), \(c\) lies between \(0.79\) and \(1.05\) and the factor, for \(r>1\), between \(0.55\) and \(1\) (numerical; values at the points evaluated, not bounds over a range)"""))

# F6 + F2 (Rows): N scan; blocks with inequivalent edge sites
EDITS.append(('F6/F2 rows',
r"""In this regime the number of boxes of the diagram on each side is therefore close to \(2W^{1/2}T\): it follows \(T\), which here is \(N^{1/2}s\), and not \(s\).""",
r"""With \(M_1=N/2\), \(l_{c1}=N-1\) and \(l_{c2}=3\) the same ratio is \(0.90\), \(0.93\), \(0.94\) at \(N=8,12,16\), and the ratio to \(2W^{1/2}s\) is \(2.6\), \(3.2\), \(3.8\) (numerical). For this block the number of boxes of the diagram on each side is therefore close to \(2W^{1/2}T\): it follows \(T\), which here is \(N^{1/2}s\), and not \(s\). When the edge sites are not equivalent, the corresponding estimate is \(L\equiv2\sum_u\langle YY^\dagger\rangle_{uu}^{1/2}\), the sum being over the \(r\) edge sites; it is at most \(G\equiv2\,(r\operatorname{Tr}\langle YY^\dagger\rangle)^{1/2}\), which is not a sum over the edge sites, with equality only for equal entries. Take \(N=12\) and \(16\), \(A_f=\nu_f1\) with \(\nu_2/\nu_1=1\) and \(3\), and the variance \(f\) above with \(l_{c1}=N-1\), \(l_{c2}=3\), or the sum of this \(f\) and the same with \(l_1\) and \(l_2\) exchanged. For the half-plane blocks with \(b/a=0.41\) and \(3^{-1/2}\) that contain half of the sites, \(M=N^2/2\) and \(r=N\), the ratio \(L/G\) lies between \(0.86\) and \(0.99\) in the sixteen cases, and the sum of the positive eigenvalues of \(Q\) is between \(0.92\) and \(0.96\) of \(L\) and between \(0.81\) and \(0.94\) of \(G\); the change of \(\nu_2/\nu_1\) from \(1\) to \(3\) changes its ratio to \(L\) by at most \(0.02\) and its ratio to \(G\) by \(0.07\) to \(0.11\). For the product blocks with \((M_1,M_2)\) equal to \((6,3)\) and \((3,7)\) at \(N=12\), and to \((8,4)\) and \((4,9)\) at \(N=16\), where \(M/r\) is between \(2\) and \(3\), \(L/G\) lies between \(0.80\) and \(0.99\), and the sum is between \(0.78\) and \(0.91\) of \(L\) and between \(0.67\) and \(0.85\) of \(G\) (numerical, \(60\) samples, statistical errors at most \(0.02\), momenta not constrained to \(\operatorname{Tr}Q=0\))."""))

# F2 (Bearing (i), (ii)): restrict to the tested blocks
EDITS.append(('F2 bearing',
r"""(i) On this four-dimensional factor the number of boxes, the coefficient of the logarithm in \(\log d_\mu\), is, within the accuracy of the numerical comparison above, a sum over the sites of a three-dimensional edge of a quantity fixed by the links at that site and by the row sums \(D_v\) of the state; the single row of the preceding paragraph was special to a one-dimensional edge. (ii) The measure of that sum is \(T\) weighted by the state.""",
r"""(i) For the cap times the whole second sphere, whose edge sites are all equivalent, and for the half-plane blocks sampled, the number of boxes, the coefficient of the logarithm in \(\log d_\mu\), is, within the accuracy of the numerical comparisons above, a sum over the sites of a three-dimensional edge of a quantity fixed by the links at that site and by the row sums \(D_v\) of the state; the single row of the preceding paragraph was special to a one-dimensional edge. For the product blocks sampled the same sum is an estimate with a deficit of up to \(22\%\), and blocks of other shapes, larger \(N\) and larger \(M/r\) with inequivalent edge sites are not tested. (ii) With that proviso the measure of that sum is \(T\) weighted by the state."""))

# F4 (Bearing (iii)): at the same M
EDITS.append(('F4',
r"""the value for \(r\) rows is not \(r\) times the value for one row, so at this order""",
r"""the value for \(r\) rows is not \(r\) times the value for one row at the same \(M\), so at this order"""))

# F3 (Bearing (iv)): the block is a region of the compact factor, not of the emergent spacetime
EDITS.append(('F3',
r"""and the factor is compact with a positive contraction.""",
r"""and the factor is compact with a positive contraction: as in (i) of the preceding paragraph, the block is a region of this factor and not of the emergent spacetime, and its edge, though three-dimensional, is not the boundary \(\partial M\) of Definition~\ref{def:HBEV}."""))

out = src
for tag, old, new in EDITS:
    assert out.count(old) == 1, (tag, out.count(old))
    out = out.replace(old, new)
    print('applied', tag)
assert out.isascii() and '\r' not in out and out.endswith('\n')
open(os.path.join(HERE, 'appH_insert_r2.tex'), 'wb').write(out.encode('ascii'))
print('appH_insert_r2.tex:', len(out), hashlib.sha256(out.encode()).hexdigest())
print('paragraphs (r1 -> r2):', src.count('\n\n') + 1, '->', out.count('\n\n') + 1)
for line in difflib.unified_diff(src.splitlines(), out.splitlines(), 'appH_insert.tex', 'appH_insert_r2.tex', lineterm='', n=0):
    print(line[:400] + (' ...' if len(line) > 400 else ''))
