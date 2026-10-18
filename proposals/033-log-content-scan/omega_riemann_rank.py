import pickle, sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy import QQ
ro, rr = pickle.load(open('omega_riemann_full.pkl', 'rb'))
def dm(rows): return DomainMatrix([[QQ.from_sympy(sp.Rational(x)) for x in r] for r in rows], (len(rows), len(rows[0])), QQ)
A, B = dm(rr), dm(ro)
J = DomainMatrix([ra + rb for ra, rb in zip(A.to_Matrix().tolist(), B.to_Matrix().tolist())], (len(rr), 96 * 2), QQ) if False else dm([list(a) + list(b) for a, b in zip(rr, ro)])
s = 'K=45 samples, first jet fixed: rank dR = %d, rank dOmega = %d, rank joint = %d, dOmega a fixed linear image of dR: %s' % (A.rank(), B.rank(), J.rank(), J.rank() == A.rank())
print(s); open('omega_riemann_full.out.txt', 'w').write(s + '\n')
