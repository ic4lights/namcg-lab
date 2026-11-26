import sys, numpy as np
P='C:/Users/redgi/Projects/namcg-lab/proposals/071-d1-curved-torsion-backgrounds'; sys.path.insert(0,P)
import bg
PA=bg.PAIRS
def C_of(p):
    C=np.zeros((4,4,4))
    for k,(a,b) in enumerate(PA): C[a,b]=p[4*k:4*k+4]; C[b,a]=-p[4*k:4*k+4]
    return C
X=np.load(P+'/solvable_solutions_seed21.npy'); eta=bg.eta_of([-1,1,1,1])
for x in X:
    C=C_of(x[:24]); W=bg.W_of(x[24:]); B1,B2,T,R=bg.brackets(C,W,eta)
    trad=np.einsum('abb->a',C); trT=np.einsum('acc->a',T); F=-np.einsum('abc,c->ab',C,trT/2)
    print('tr ad_a =',np.round(trad,4),' |T trace| %.3f'%np.abs(trT).max(),' |F=-c t| (unimodular formula) %.3f'%np.abs(F).max())
