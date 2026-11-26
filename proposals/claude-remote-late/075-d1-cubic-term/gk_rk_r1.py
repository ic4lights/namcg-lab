import numpy as np, itertools
from sympy.combinatorics import Permutation
eta=np.diag([-1.,1,1,1]); eps=np.zeros((4,)*4)
for p in itertools.permutations(range(4)): eps[p]=Permutation(list(p)).signature()
def M(q,v):
    ql=eta@q; q2=q@ql
    m=np.zeros((4,4),complex)
    for b in range(4):
        for d in range(4):
            m[b,d]=-(q2*(b==d)-ql[b]*q[d])+1j*sum(eps[b,c,d,f]*v[f]*q[c] for c in range(4) for f in range(4))*eta[d,d]
    return m
rng=np.random.default_rng(3)
for v in [np.array([1.,0,0,0]),np.array([0,0,0,1.]),np.array([1.,0,0,1])]:
    k=rng.normal(size=3); q=np.r_[np.linalg.norm(k),k]  # null q
    print(v, 'rank M at q^2=0:', np.linalg.matrix_rank(M(q,v),tol=1e-9), 'sv', np.round(np.linalg.svd(M(q,v),compute_uv=False),4))
