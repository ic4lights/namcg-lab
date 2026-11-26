import numpy as np
rng=np.random.default_rng(120)
def fams(z,zb):
    P=np.array([[z[0],z[1]],[z[2],z[3]]],dtype=complex)
    Pd=np.array([[zb[0],zb[2]],[zb[1],zb[3]]],dtype=complex)  # independent zbar, (Pd)ij = zb of z_ji
    X=Pd@P
    trX=np.trace(X); trP=np.trace(P); trPd=np.trace(Pd)
    q=[trX, np.trace(X@X), trP**2, trPd**2, trP*trPd, np.trace(Pd@Pd)]
    return q
def rows(fn, npts=400):
    R=[]
    for _ in range(npts):
        z=rng.integers(-7,8,4).astype(complex)+1j*rng.integers(-7,8,4)
        zb=rng.integers(-7,8,4).astype(complex)+1j*rng.integers(-7,8,4)
        v0=fn(z,zb)
        for s,sb in [(1,0),(0,1),(1,1),(0,1j),(1j,0)]:
            v1=fn(z+s,zb+sb)
            R.extend([[ (x-y).real for x,y in zip(v1,v0)],[(x-y).imag for x,y in zip(v1,v0)]])
    return np.array(R)
def rank(M,tol=1e-7):
    s=np.linalg.svd(M,compute_uv=False); return int((s>tol*s[0]).sum()) if s[0]>0 else 0
Mq=rows(lambda z,zb: fams(z,zb))
rq=rank(Mq); print('quad family dim 6 -> shift-map rank', rq, ' kernel dim', 6-rq)
def qprod(z,zb):
    q=fams(z,zb); return [q[i]*q[j] for i in range(6) for j in range(i,6)]
Mqq=rows(qprod)
r1=rank(Mqq); nf=21
print('quartic products-21 map rank', r1, ' kernel dim', nf-r1)
def W1(z,zb):
    P=np.array([[z[0],z[1]],[z[2],z[3]]],dtype=complex); Pd=np.array([[zb[0],zb[2]],[zb[1],zb[3]]],dtype=complex)
    C=P@Pd-Pd@P
    return np.trace(C.conj().T if False else C@C)  # z,zbar independent: Tr C^2
def qw(z,zb): return qprod(z,zb)+[W1(z,zb)]
Mqw=rows(qw)
r2_=rank(Mqw)
print('quartic21+W1 map rank', r2_, ' kernel dim', 22-r2_)
# W1 independence from products: value-rank
V=[];VW=[]
for _ in range(300):
    z=rng.integers(-7,8,4).astype(complex); zb=rng.integers(-7,8,4).astype(complex)
    V.append(qprod(z,zb)); VW.append(qprod(z,zb)+[W1(z,zb)])
print('W1 in span of 21-products?', rank(np.array(V))==rank(np.array(VW)), rank(np.array(V)), rank(np.array(VW)))
# TrX-only span shift-invariants:
Mx=rows(lambda z,zb: [fams(z,zb)[0],fams(z,zb)[1],fams(z,zb)[2]])
print('X-span(TrX,TrX2,(TrP)^2...) kernel dim (expect 0):', 3-rank(Mx))
# quad kernel vectors explicit:
import numpy.linalg as la
s,U,VT=np.linalg.svd(Mq); ker=VT[s>1e-7*s[0]:].conj()
print('quad kernel rows (conj):', np.round(ker,3))
# quartic kernel basis:
s2,U2,VT2=np.linalg.svd(Mqq); ker2=VT2[s2>1e-7*s2[0]:].conj()
print('quartic kernel dim via SVD:', ker2.shape[0])
