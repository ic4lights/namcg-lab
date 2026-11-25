import numpy as np
rng=np.random.default_rng(7)
def fams(z,zb):
    P=np.array([[z[0],z[1]],[z[2],z[3]]],dtype=complex)
    Pd=np.array([[zb[0],zb[2]],[zb[1],zb[3]]],dtype=complex)
    X=Pd@P
    trX=np.trace(X); trP=np.trace(P); trPd=np.trace(Pd)
    return np.array([trX, np.trace(X@X), trP**2, trPd**2, trP*trPd, np.trace(Pd@Pd)],dtype=complex)
z=rng.integers(-7,8,4).astype(complex)+1j*rng.integers(-7,8,4); zb=rng.integers(-7,8,4).astype(complex)+1j*rng.integers(-7,8,4)
v0=fams(z,zb); v1=fams(z+1,zb); v2=fams(z,zb+1j)
d1=v1-v0; d2=v2-v0
print('d(s=1):',np.round(d1,3))
print('d(sb=i):',np.round(d2,3))
print('2d0-d4 (s=1):', 2*d1[0]-d1[4], '| 2d0-d4 (sb=i):', 2*d2[0]-d2[4])
P=np.array([[z[0],z[1]],[z[2],z[3]]],dtype=complex); Pd=np.array([[zb[0],zb[2]],[zb[1],zb[3]]],dtype=complex)
trP=np.trace(P); trPd=np.trace(Pd)
print('trP,trPd:',trP,trPd)
q4_0=trP*trPd; q4_1=(trP+2)*trPd
print('manual d q4:', q4_1-q4_0, '2*trPd:',2*trPd)
print('manual d q0:', np.trace(Pd@P+Pd- Pd@P))
print('v0[4],v1[4]:', v0[4], v1[4], 'diff', v1[4]-v0[4])
