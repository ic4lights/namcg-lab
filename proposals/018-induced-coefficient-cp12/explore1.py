import numpy as np, sys
from cp12_realisation import *
np.set_printoptions(precision=5, suppress=True, linewidth=160)
rng=np.random.default_rng(1)
s=-1.0
pairs=[(A,B) for A in range(6) for B in range(A+1,6)]
idx={p:i for i,p in enumerate(pairs)}
def vec(M0,C,D):
    # Hamiltonian vector field of M^{CD} acting on the 15 coords M^{AB}
    v=np.zeros(15)
    for (A,B) in pairs:
        v[idx[(A,B)]]=s*lie(C,D,A,B,M0)
    return v
def pbM(M0,C,D,E,F): return s*lie(C,D,E,F,M0)
z=rand_z_pos(rng,3.0); M0=Mfun(z)
print("y^a:",M0[:5,5])
D=[vec(M0,a,4) for a in range(4)]
J={(a,b):vec(M0,a,b) for a in range(4) for b in range(a+1,4)}
Hm=np.array(D)
print("rank horiz",np.linalg.matrix_rank(Hm,tol=1e-9))
allv=np.array(D+list(J.values()))
print("rank all",np.linalg.matrix_rank(allv,tol=1e-9))
# all hamiltonian fields
allg=np.array([vec(M0,A,B) for (A,B) in pairs]); print("tangent dim",np.linalg.matrix_rank(allg,tol=1e-9))
