"""s4 (mechanism, proposal only): eigenvalues of the spin coupling (1/2) F_ab S^ab on a Weyl spinor
for a real antisymmetric F, Euclidean so(4) versus Lorentzian so(3,1).  Euclidean: real, +-(f1+f2)
on one chirality and +-(f1-f2) on the other (skew eigenvalues f1,f2). Lorentzian: +-sqrt((B+iE).(B+iE))
up to normalisation, real only when E.B=0 and |B|>=|E|."""
import numpy as np
rng=np.random.default_rng(3)
s=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]),np.diag([1.,-1]).astype(complex)]
I2=np.eye(2)
gE=[np.kron(s[0],s[0]),np.kron(s[0],s[1]),np.kron(s[0],s[2]),np.kron(s[1],I2)]
chi=gE[0]@gE[1]@gE[2]@gE[3]
gL=[1j*gE[0]]+gE[1:]           # gamma^0 with (gamma^0)^2=-1, signature (-,+,+,+)
eta=np.diag([-1.,1,1,1])
def spin(g,F,metric):
    S=np.zeros((4,4),complex)
    for a in range(4):
        for b in range(4):
            Fab=F[a,b]
            S+=0.5*Fab*(-0.25j)*(g[a]@g[b]-g[b]@g[a])
    return S
w,v=np.linalg.eigh(chi); P=[v[:,w>0],v[:,w<0]]
for trial in range(3):
    A=rng.normal(size=(4,4)); F=A-A.T
    SE=spin(gE,F,np.eye(4))
    evE=[np.round(np.linalg.eigvals(p.conj().T@SE@p),6) for p in P]
    Fl=eta@F@eta*0+F   # components F_{ab} with lower indices; S^{ab} built from gamma^a
    SL=spin(gL,F,eta)
    evL=[np.round(np.linalg.eigvals(p.conj().T@SL@p),6) for p in P]
    E=F[0,1:]; B=np.array([F[2,3],F[3,1],F[1,2]])
    print("Euclidean chiral eigenvalues:",evE,"  Lorentzian:",evL)
    print("   (1/2)sqrt((B+-iE)^2):",np.round(0.5*np.sqrt(np.dot(B+1j*E,B+1j*E)),6),np.round(0.5*np.sqrt(np.dot(B-1j*E,B-1j*E)),6))
