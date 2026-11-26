import numpy as np
rng=np.random.default_rng(119)
def tr(M): return M[0,0]+M[1,1]
def fam(z,zb):
    ZZ=np.array([[z[0],z[1]],[z[2],z[3]]],dtype=complex)
    ZZd=np.array([[zb[0],zb[1]],[zb[2],zb[3]]],dtype=complex)
    ZT=ZZ.T; ZdT=ZZd.T
    w1=tr(ZZ@ZZ@ZZ@ZZ);            w1c=tr(ZZd@ZZd@ZZd@ZZd)
    w2=tr(ZZ@ZZ@ZZ@ZdT);           w2c=tr(ZZd@ZZd@ZZd@ZT)
    w3=tr(ZZ@ZZ@ZdT@ZdT)
    w4=tr(ZZ@ZdT@ZZ@ZdT)
    trP=tr(ZZ); trPd=tr(ZZd); trP2=tr(ZZ@ZZ); trPd2=tr(ZZd@ZdT)*0+tr(ZZdT2:=ZdT@ZdT)
    trPd2=tr(ZdT@ZdT); trX=tr(ZdT@ZZ)
    out=[(w1+w1c)/2,(w1-w1c)/2j,(w2+w2c)/2,(w2-w2c)/2j,w3,w4,w2*w2c]
    out+=[trX*(trP2+trPd2)/2, trX*(trP2-trPd2)/2j, trX*trP*trPd, trP*trPd*trP*trPd]
    out+=[(trP**4+w1c)/2,(trP**4-w1c)/2j]
    out+=[(trP2*trPd2+tr(ZZd@ZZd)*tr(ZZ@ZZ))/2]
    out+=[(trP**2*trP2+tr(ZZd)**2*tr(ZZd@ZZd))/2,(trP**2*trP2-tr(ZZd)**2*tr(ZZd@ZZd))/2j]
    return out
def rank(M,tol=1e-6):
    s=np.linalg.svd(M,compute_uv=False); return int((s>tol*max(s[0],1)).sum())
R=[]
for _ in range(150):
    z=rng.integers(-6,7,4).astype(complex)+1j*rng.integers(-6,7,4)
    zb=rng.integers(-6,7,4).astype(complex)+1j*rng.integers(-6,7,4)
    I2=np.array([1,0,0,1],dtype=complex)
    v0=np.array(fam(z,zb),dtype=complex)
    for s_,sb_ in [(1,0),(0,1),(1,1),(1j,0),(0,1j),(2,-3j),(3,2)]:
        v1=np.array(fam(z+s_*I2,zb+sb_*I2),dtype=complex)
        R.append((v1-v0).real); R.append((v1-v0).imag)
M=np.array(R); r=rank(M); print('QUAR-16 map rank', r, 'kernel dim', 16-r)
# W1 direction check: W1 = 2w4-2w3 (elements indices 4,5 = w3,w4)
s,U,VT=np.linalg.svd(M)
ker=VT[s>1e-6*max(s[0],1),:]
WDIR=np.zeros(16); WDIR[4]=-1; WDIR[5]=1
print('WDIR in kernel? max residual:', np.abs(ker@(ker.T@WDIR)).max() if ker.size else None, '| proj norm', np.linalg.norm(np.dot(WDIR,ker.T)))
# also linear relations among family VALUES (CH dependencies):
V=[np.array(fam(*[rng.integers(-6,7,4).astype(complex)+1j*rng.integers(-6,7,4) for _ in range(2)]),dtype=complex) for _ in range(100)]
print('value-rank of family:', rank(np.array(V)))
