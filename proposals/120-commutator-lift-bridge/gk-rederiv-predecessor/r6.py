import numpy as np
rng=np.random.default_rng(7)
def fams(z,zb):
    P=np.array([[z[0],z[1]],[z[2],z[3]]],dtype=complex)
    Pd=np.array([[zb[0],zb[2]],[zb[1],zb[3]]],dtype=complex)
    X=Pd@P
    trX=np.trace(X); trP=np.trace(P); trPd=np.trace(Pd)
    return [trX, np.trace(X@X), trP**2, trPd**2, trP*trPd, np.trace(Pd@Pd)]
z=rng.integers(-7,8,4).astype(complex)+1j*rng.integers(-7,8,4); zb=rng.integers(-7,8,4).astype(complex)+1j*rng.integers(-7,8,4)
v0=fams(z,zb); v1=fams(z+1,zb); v2=fams(z,zb+1j)
import numpy as np
c=np.array([2,0,0,0,-1,0])
print('combo shift s=1:', np.dot(c,(np.array(v1)-np.array(v0))))
print('combo shift sb=i:', np.dot(c,(np.array(v2)-np.array(v0))))
print('q diffs s=1:', np.array(v1-v0))
