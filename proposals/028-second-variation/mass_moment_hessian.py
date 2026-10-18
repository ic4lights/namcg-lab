"""028 script 3: A-dependence of the degree-one (mass-insertion) term.  For X^a = T^a + eps*alpha^a cos(q.y) (alpha^a constant) the Hamiltonian fields are
 W_a(eps) = W_a - eps sin(phi) alpha_a Y_q ,  Y_q = q_mu Ham(y^mu)  (exact for this ansatz; verified below by the Poisson algebra).
At phase phi=pi/2 (maximal 1-jet) the symbol is sigma_eps(xi) = eta^{ab} v_a v_b with v_a = xi.(W_a - eps alpha_a Y_q), i.e. W_hat_eps = W_hat - eps alpha Y^T (4x6).
Gaussian window  exp(-xi^T P xi), P = -sigma(Delta_{3/4}); the mass moment is N(eps) = (4pi)^-3 det(P)^(-1/2) M(lam),  lam = eig(eta B_eps), B_eps = W_hat_eps P^-1 W_hat_eps^T
 (Sylvester; M = i int ds prod (1+i s lam_k)^(-1/2), Re M, Im M from the 027 Gaussian lemma).
Reported: Re N and Im N at eps=0, first and second eps-derivative (central differences, step 1e-3 and 2e-3), quadratic form Q(alpha)=d^2 Re N/d eps^2 as a 4x4 matrix, its eigenvalues,
and positivity of Re N(eps) over a scan (lemma: B_eps > 0 so (3,1) pencil)."""
import numpy as np
from scipy.integrate import quad
from geom28 import *
rng = np.random.default_rng(7)
def Mlemma(lam):
    lam = np.array(lam); neg = lam[lam < 0]; pos = lam[lam > 0]
    assert len(neg) == 1
    c = -neg[0]
    re = (2/c)*quad(lambda v: np.prod([(1 + a*(1 - v*v)/c)**-0.5 for a in pos]), 0, 1, epsabs=1e-12, epsrel=1e-12)[0]
    im = (2/c)*quad(lambda v: np.prod([(1 + a*(1 + v*v)/c)**-0.5 for a in pos]), 0, np.inf, epsabs=1e-12, epsrel=1e-12)[0]
    return re + 1j*im
def Nmoment(What, P):
    Pinv = np.linalg.inv(P)
    B = What @ Pinv @ What.T
    lam = np.real(np.linalg.eigvals(eta4 @ B))
    return (4*np.pi)**-3*np.linalg.det(P)**-0.5*Mlemma(lam)
def setup(M0, q):
    Pi, W, Yb, c, E = fields(M0)
    wf = window_forms(M0)
    Yq = sum(q[m]*Yb[m] for m in range(4))
    return W, Yq, wf['P'], wf
def Neps(W, Yq, P, alpha, eps):
    What = W - eps*np.outer(alpha, Yq)
    return Nmoment(What, P)
def derivs(W, Yq, P, alpha, h=2e-3):
    f = lambda e: Neps(W, Yq, P, alpha, e)
    n0 = f(0.0); p1 = f(h); m1 = f(-h); p2 = f(2*h); m2 = f(-2*h)
    d1 = (8*(p1 - m1) - (p2 - m2))/(12*h)
    d2 = (-(p2 + m2) + 16*(p1 + m1) - 30*n0)/(12*h*h)
    return n0, d1, d2
if __name__ == "__main__":
    print("A. consistency of the ansatz: Ham fields of X^a = T^a + eps alpha^a cos(q.y), checked through the Poisson bracket {F,.} identity")
    z = rand_z_pos(rng, 2.0); M0 = Mfun(z); Pi, W, Yb, c, E = fields(M0)
    q = rng.normal(size=4); alpha = rng.normal(size=4)
    m = M0[4, 5]
    # {T^a, y^mu} = s m eta^{a mu}  -> {T^a, q.y} = s m q^a ;   F^{ab}[X] first order in eps: eps*(-sin phi)*s m (q^a alpha^b - q^b alpha^a)*(-1)?  verified via Ham fields below
    phi = 0.7; eps = 1e-6
    # first-order change of Ham field of F^{ab}={X^a,X^b} computed from Jacobi on the 15-dim ambient algebra: F^{ab}= s M^{ab} + eps * [ {T^a, A^b} - {T^b, A^a} ]
    # {T^a, A^b} with A^b = alpha^b cos(q.y): = -alpha^b sin(phi) * q_mu {T^a,y^mu}
    qlow = q
    def dF_ham(a, b):
        # Ham field of  g = -sin(phi) m s (alpha^b q^a - alpha^a q^b) * ... ; d(g)= (alpha^b q^a - alpha^a q^b) (-s)(cos(phi) m dphi + sin(phi) dm)
        qup = eta4 @ qlow
        coef = (alpha[b]*qup[a] - alpha[a]*qup[b])
        Yq = sum(qlow[mu]*Yb[mu] for mu in range(4))
        return -s*coef*(np.cos(phi)*m*Yq + np.sin(phi)*c[pidx[(4, 5)]])
    # independent check: finite-difference of {X^a, X^b} Ham fields is not available for non-polynomial functions in M; instead verify the linear-in-A product rule numerically for a POLYNOMIAL A = alpha^b * (q.y)  (cos -> linear)
    # X^b = T^b + eps alpha^b (q.y): F^{ab} = s M^{ab}... Ham(F^{ab}) = s*c[(a,b)] + eps*[Ham({T^a,alpha^b q.y}) - Ham({T^b,alpha^a q.y})] ; {T^a, q.y} = s m q^a -> Ham(s m)(...)
    def dF_ham_lin(a, b):
        qup = eta4 @ qlow
        coef = (alpha[b]*qup[a] - alpha[a]*qup[b])
        return s*coef*c[pidx[(4, 5)]]                    # Ham(m)= Ham(M^{45})
    # direct: {X^a,X^b} bracket of the linear functions via lie algebra: use M-space brackets
    def Fab_linear_coeffs(a, b, eps):
        # X^a = M^{a4} + eps*alpha^a * sum_mu q_mu M^{mu5}  : bracket of two LINEAR functions in M is linear -> compute with lin_coeffs
        La = np.zeros(15); Lb = np.zeros(15)
        # represent X^a as linear combination coefficients on M^p
        def lin(a_):
            L = np.zeros(15); L[pidx[(a_, 4)]] += 1.0
            for mu in range(4): L[pidx[(mu, 5)]] += eps*alpha[a_]*qlow[mu]
            return L
        La, Lb = lin(a), lin(b)
        out = np.zeros(15)
        for i, p in enumerate(pairs):
            for j, r in enumerate(pairs):
                if La[i] != 0 and Lb[j] != 0:
                    out += La[i]*Lb[j]*lin_coeffs(*p, *r)
        return out        # coefficients L_P with {X^a,X^b} = s * sum L_P M^P  (lin_coeffs includes s)
    a, b = 1, 2
    h = 1e-4
    Lp = Fab_linear_coeffs(a, b, h); Lm = Fab_linear_coeffs(a, b, -h); L0 = Fab_linear_coeffs(a, b, 0.0)
    num = (ham_of_lin(M0, Lp) - ham_of_lin(M0, Lm))/(2*h)
    # compare tangent-coordinates: ham_of_lin returns a 15-vector; project with E
    numE = E @ num
    pred = dF_ham_lin(a, b)
    print("   O(eps) change of Ham({X^a,X^b}) (linear A=alpha (q.y)): |numerical - predicted| =", np.abs(numE - pred).max(), " |pred| =", np.abs(pred).max())
    print()
    print("B. Re N, Im N, derivatives along alpha at 6 orbit points (q random), window kappa=3/4")
    for t in range(6):
        z = rand_z_pos(rng, rng.uniform(0.5, 4)); M0 = Mfun(z); y = M0[:5, 5]; a_ = M0[4, 5]/np.sqrt(-(y @ np.diag([-1., 1, 1, 1, 1]) @ y))
        q = rng.normal(size=4); alpha = rng.normal(size=4)
        W, Yq, P, wf = setup(M0, q)
        n0, d1, d2 = derivs(W, Yq, P, alpha)
        neps = [Neps(W, Yq, P, alpha, e) for e in np.linspace(-0.5, 0.5, 21)]
        print("  a=%.3f  N(0)=%.6f%+.6fi  dN=%.5f%+.5fi  d2N=%.5f%+.5fi   min over eps in[-.5,.5] of Re N = %.5f" % (a_, n0.real, n0.imag, d1.real, d1.imag, d2.real, d2.imag, min(np.real(neps))))
    print()
    print("C. quadratic form Q_ab = d^2 Re N/d eps^2 (polarised over alpha in R^4), eigenvalues relative to Re N(0)")
    for t in range(4):
        z = rand_z_pos(rng, rng.uniform(0.5, 4)); M0 = Mfun(z); q = rng.normal(size=4)
        W, Yq, P, wf = setup(M0, q)
        n00 = Nmoment(W, P).real
        Q = np.zeros((4, 4))
        for i in range(4):
            for j in range(i, 4):
                ei = np.eye(4)[i]; ej = np.eye(4)[j]
                Qi = derivs(W, Yq, P, ei)[2].real; Qj = derivs(W, Yq, P, ej)[2].real; Qij = derivs(W, Yq, P, ei + ej)[2].real
                Q[i, j] = Q[j, i] = (Qij - Qi - Qj)/2 if i != j else Qi
        ev = np.linalg.eigvalsh(Q)
        print("  Re N(0) = %.6f ; eigenvalues of Q/ReN(0):" % n00, np.round(ev/n00, 4))
