"""
R-b1 Step 1.  Check of the Manta-Steinacker-Tran character (arXiv:2411.02598 eq. (3.7), (3.9), (3.10)):
   Q10 = Tr_V e^{i a Sigma^V dF} - 1/2 Tr_Psi e^{i a Sigma^Psi dF} - 2,   dim V=10, Psi = 16 (Weyl, chirality sum (2-x4-)+(2+x4+)).
Euclidean SO(10) stand-in for SO(1,9) (only the Lie-algebra invariants enter).  Generator of the vector rep: antisymmetric M (the
bracket coupling dF); spinor lift S(M) = (1/4) M_ab g_a g_b.  Weighted traces:  weights (+1 vector, -1/2 spinor, -2 ghosts).
Outputs: orders a^0, a^1, a^2 vanish; a^4 coefficient and its relation to V4 = -4 tr M^4 + (tr M^2)^2 (Steinacker 2303.08012 eq. (4.21),
quoted by the SME scout; not opened by me).
"""
import numpy as np, itertools, sympy as sp
rng = np.random.default_rng(1)
# gamma matrices for SO(10) (32x32)
s0=np.eye(2); sx=np.array([[0,1],[1,0]]); sy=np.array([[0,-1j],[1j,0]]); sz=np.diag([1,-1])
def kron(*ms):
    out=np.array([[1]])
    for m in ms: out=np.kron(out,m)
    return out
g=[]
for j in range(5):
    g.append(kron(*([sz]*j+[sx]+[s0]*(4-j))))
    g.append(kron(*([sz]*j+[sy]+[s0]*(4-j))))
for a in range(10):
    for b in range(10):
        assert np.allclose(g[a]@g[b]+g[b]@g[a], 2*(a==b)*np.eye(32))
G11 = np.eye(32, dtype=complex)
for x in g: G11 = G11 @ x
G11 = G11 * (1j)**(-5) if not np.allclose(G11@G11, np.eye(32)) else G11
if not np.allclose(G11@G11,np.eye(32)):
    G11 = G11/np.sqrt((G11@G11)[0,0])
assert np.allclose(G11@G11,np.eye(32))
P = (np.eye(32)+G11)/2          # Weyl projector: rank 16
assert round(np.trace(P).real)==16

def S(M):
    out = np.zeros((32,32),dtype=complex)
    for a in range(10):
        for b in range(10):
            out += 0.25*M[a,b]*g[a]@g[b]
    return out
def randM(dim, k=10):
    A = rng.normal(size=(dim,dim)); A = A-A.T
    M = np.zeros((10,10)); M[:dim,:dim]=A
    return M
# homomorphism check
M1, M2 = randM(10), randM(10)
assert np.allclose(S(M1)@S(M2)-S(M2)@S(M1), S(M1@M2-M2@M1))

def moments(M, kmax=4):
    Sm = S(M)
    out = {}
    for k in range(kmax+1):
        tv = np.trace(np.linalg.matrix_power(M,k)).real
        ts = np.trace(P@np.linalg.matrix_power(Sm,k))
        out[k] = (tv, ts, tv - 0.5*ts - (2 if k==0 else 0))
    return out
for dim in (10, 4):
    M = randM(dim)
    mo = moments(M)
    print('F supported on %d dims:' % dim)
    for k in range(5):
        print('  order %d : tr_V M^k = %+.6f ; tr_16 S^k = %+.6f%+.6fj ; Q10 coefficient (x k!) = %+.6e' % (k, mo[k][0], mo[k][1].real, mo[k][1].imag, mo[k][2]))
    trF2 = np.trace(M@M); trF4=np.trace(np.linalg.matrix_power(M,4))
    V4 = -4*trF4 + trF2**2
    print('  V4 = -4 trM^4 + (trM^2)^2 = %.6f ;  Q10 order-4 numerator / V4 = %.6f' % (V4, mo[4][2]/V4))
print('(ratio constant over random F => alpha^4 term is proportional to V4 for any F)')
for t in range(3):
    M = randM(10); mo = moments(M); trF2 = np.trace(M@M); trF4=np.trace(np.linalg.matrix_power(M,4))
    print('  ratio (10D, random %d): %.8f' % (t, mo[4][2]/(-4*trF4+trF2**2)))

print('--- 4D-supported F, closed form (x=a phi1, y=a phi2; eigenvalues +-i phi) ---')
x,y=sp.symbols('x y')
Q = 2*sp.cos(x)+2*sp.cos(y) + 6 - 2*(4*sp.cos(x/2)*sp.cos(y/2)) - 2
# vector: 4D block + 6 inert scalars (contribute 6); Dirac: tr_D e^{aS} = 4 cos(x/2)cos(y/2); weight -1/2 on 16 = 2 Dirac*... -> n_D=2 : -2 * tr_D ... -2 (ghosts)
ser = sp.series(Q.subs({x:x*sp.Symbol('t'),y:y*sp.Symbol('t')}),sp.Symbol('t'),0,6).removeO()
print(sp.simplify(sp.expand(ser)))
print('order-4 coefficient factorised:', sp.factor(sp.expand(ser).coeff(sp.Symbol('t'),4)))
nD = sp.Symbol('n_D')
Qn = 2*sp.cos(x)+2*sp.cos(y) + 6 - 2 - nD*(4*sp.cos(x/2)*sp.cos(y/2))
t=sp.Symbol('t'); sern=sp.expand(sp.series(Qn.subs({x:x*t,y:y*t}),t,0,5).removeO())
print('general n_D: order 0:', sp.simplify(sern.coeff(t,0)), ' order 2:', sp.factor(sern.coeff(t,2)), ' order 4:', sp.factor(sern.coeff(t,4)))
