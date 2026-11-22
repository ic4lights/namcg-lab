import sys, numpy as np
P='C:/Users/redgi/Projects/namcg-lab/proposals/071-d1-curved-torsion-backgrounds'; sys.path.insert(0,P)
import bg, core068 as K
eta=bg.eta_of([-1,1,1,1])
# null rotation algebra: Y=E0+E3, [Y,E1]=E2, [Y,E2]=-E1, E0-E3 central
C=np.zeros((4,4,4))
for a in (0,3):
    C[a,1,2]+=0.5*2/2; C[1,a,2]-=0.5*2/2
    C[a,2,1]-=0.5*2/2; C[2,a,1]+=0.5*2/2
# check: [E0,E1]+[E3,E1] = E2 requires each 1/2 ; E0=(Y+Z)/2,E3=(Y-Z)/2 -> [E0,E1]=[E3,E1]=E2/2
C=np.zeros((4,4,4))
for a in (0,3):
    C[a,1,2]=0.5; C[1,a,2]=-0.5; C[a,2,1]=-0.5; C[2,a,1]=0.5
_,_,T0,_=bg.brackets(C,np.zeros((4,4,4)),eta)
k=np.array([1.,0,0,1]); J=np.zeros((4,4)); J[1,2]=1; J[2,1]=-1
for th in (-0.5,0.5):
    _,_,T1,_=bg.brackets(np.zeros((4,4,4)),th*np.einsum('a,cd->acd',k,J),eta)
    print('vartheta',th,'max|T(const frame)-T(left-inv)| =',np.abs(T1-T0).max())
