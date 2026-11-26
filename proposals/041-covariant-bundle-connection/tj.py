"""Truncated Taylor jets in D variables (order ORD) with numpy; fields are arrays [..., M] of Taylor coefficients."""
import itertools, numpy as np

class Jets:
    def __init__(self, D=4, ORD=3):
        self.D, self.ORD = D, ORD
        mons = [m for m in itertools.product(range(ORD+1), repeat=D) if sum(m) <= ORD]
        mons.sort(key=lambda m: (sum(m), m))
        self.mons = mons; self.M = len(mons)
        self.idx = {m: i for i, m in enumerate(mons)}
        M = self.M
        P = np.zeros((M, M, M))
        for a, ma in enumerate(mons):
            for b, mb in enumerate(mons):
                mc = tuple(i+j for i, j in zip(ma, mb))
                if sum(mc) <= ORD:
                    P[a, b, self.idx[mc]] = 1.0
        self.P = P
        # derivative operators: d_k : coefficients
        self.Dk = []
        for k in range(D):
            Dm = np.zeros((M, M))
            for a, ma in enumerate(mons):
                if ma[k] > 0:
                    mb = list(ma); mb[k] -= 1
                    Dm[self.idx[tuple(mb)], a] = ma[k]     # new coeff of x^{ma-e_k} gets ma[k]*c
            self.Dk.append(Dm)
        # which degree
        self.deg = np.array([sum(m) for m in mons])
    def const(self, c):
        a = np.zeros(self.M); a[0] = c; return a
    def mul(self, a, b):
        return np.einsum('...a,...b,abc->...c', a, b, self.P, optimize=True)
    def matmul(self, A, B):
        # A [i,j,M], B [j,k,M]
        return np.einsum('ija,jkb,abc->ikc', A, B, self.P, optimize=True)
    def d(self, f, k):
        return np.einsum('ca,...a->...c', self.Dk[k], f)
    def inv_series(self, A):
        """inverse of matrix jets A [n,n,M] with invertible constant part."""
        n = A.shape[0]
        A0 = A[:, :, 0]
        A0i = np.linalg.inv(A0)
        Ai = np.zeros_like(A); Ai[:, :, 0] = A0i
        dA = A.copy(); dA[:, :, 0] = 0
        Id0 = np.zeros_like(A); Id0[:, :, 0] = A0i
        term = Id0.copy(); res = Id0.copy()
        for _ in range(self.ORD):
            term = -self.matmul(self.matmul(term, dA), Id0)
            res = res + term
        return res
    def at0(self, f):
        return f[..., 0]
    def point_series(self, coeffs_by_mon):
        a = np.zeros(self.M)
        for m, c in coeffs_by_mon.items():
            a[self.idx[m]] = c
        return a

def random_class(J, seed, eta_diag=(1, 1, 1, 1), amp=0.4):
    rng = np.random.default_rng(seed)
    D = J.D
    eta = np.diag(np.array(eta_diag, float))
    while True:
        w0 = rng.uniform(-1, 1, (D, D)); w0 = w0 - w0.T
        if abs(np.linalg.det(w0)) > 0.1: break
    A = np.zeros((D, J.M))
    for mu in range(D):
        for i, m in enumerate(J.mons):
            if 2 <= sum(m) <= 3:
                A[mu, i] = amp*rng.uniform(-1, 1)
    om = np.zeros((D, D, J.M)); om[:, :, 0] = w0
    for m in range(D):
        for n in range(D):
            om[m, n] += J.d(A[n], m) - J.d(A[m], n)
    Th = J.inv_series(om)
    return dict(eta=eta, om=om, Th=Th)
