import numpy as np
rng=np.random.default_rng(120)
def fams(z,zb):
    P=np.array([[z[0],z[1]],[z[2],z[3]]],dtype=complex)
    Pd=np.array([[zb[0],zb[2]],[zb[1],zb[3]]],dtype=complex)
    X=Pd@P; trX=np.trace(X); trP=np.trace(P); trPd=np.trace(Pd)
    return [trX, np.trace(X@X), trP**2, trPd**2, trP*trPd, np.trace(Pd@Pd), np.trace(P@P)]
def rows(fn,nf,npts=60):
    R=[]
    for _ in range(npts):
        z=rng.integers(-7,8,4).astype(complex)+1j*rng.integers(-7,8,4)
        zb=rng.integers(-7,8,4).astype(complex)+1j*rng.integers(-7,8,4)
        I2=np.array([1,0,0,1],dtype=complex)
        v0=np.array(fn(z,zb),dtype=complex)
        for s,sb in [(1,0),(0,1),(1,1),(1j,0),(0,1j),(2,3)]:
            v1=np.array(fn(z+s*I2,zb+sb*I2),dtype=complex)
            R.append((v1-v0).real); R.append((v1-v0).imag)
    return np.array(R)
def rank(M,tol=1e-6):
    s=np.linalg.svd(M,compute_uv=False); return int((s>tol*max(s[0],1)).sum())
F6=lambda z,zb: fams(z,zb)[:6]
Mq=rows(F6,6); print('6-fam kernel dim (my family A):', 6-rank(Mq))
FV=lambda z,zb: [f for f in fams(z,zb)]
Mv=rows(FV,7); print('7-fam kernel dim:', 7-rank(Mv))
# check the 3 claimed generators in family-A span (need (TrP)^2 which is in family): g1,g2,g3:
def genvals(z,zb):
    f=fams(z,zb)
    trX,TrX2,trP2,trPd2,trPtrPd,trPd2w,trP2w = f
    g1=2*trX-trPtrPd
    g2=2*np.real(trP2w)-np.real(trP2)   # needs Re: real-polynomial ring: treat real/imag as separate elements
    return [g1]
# verify symbolic invariance of the three generators directly with diagonal shift numerics:
def three(z,zb):
    P=np.array([[z[0],z[1]],[z[2],z[3]]],dtype=complex); Pd=np.array([[zb[0],zb[2]],[zb[1],zb[3]]],dtype=complex)
    trP=np.trace(P); trPd=np.trace(Pd); X=Pd@P; trX=np.trace(X)
    g1=2*trX-trP*trPd
    g2=2*trP*trP-... 
    return [g1]
