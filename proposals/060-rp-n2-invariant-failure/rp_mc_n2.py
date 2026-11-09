"""Monte Carlo confirmation for proposal 060.

Model: N=2, three traceless Hermitian matrices A_mu = sum_a A^a_mu sigma^a/2,
mu in {0,1,2} (one time, two space), real Pauli coefficients (9 variables).
Weights (all theta-invariant under theta: A^a_0 -> -A^a_0):
  p=0 :  w = exp(-S_E - (m^2/2) sum_mu Tr A_mu^2),  S_E = (1/4) sum_{mu,nu} ||[A_mu,A_nu]||^2
  p=4 :  w = (det G)^4 * w_p0 , G_ab = sum_mu A^a_mu A^b_mu
(the positive mass is needed for normalizability along the commuting flat
directions; it is theta-invariant, as are all masses with positive-definite
coefficient matrix M_{mu nu} used in the manuscript limit identity).

Measured (normalized reflected pairings of the theta-odd invariant probes):
  f1 = Tr A_0 A_1        ->  <f1^theta, f1>_theta = -<f1^2>
  f2 = Tr([A_0,A_1] A_2) ->  <f2^theta, f2>_theta = -<|f2|^2>
Cross-checks: <f1> ~ 0 (theta-symmetry of the measure);
for g = 1 + f1: <g^theta g> = 1 - <f1^2>.
Signs, not exact values, are the point. Fixed seed; no external deps beyond numpy.
"""
import numpy as np

sig1 = np.array([[0, 1], [1, 0]], dtype=complex)
sig2 = np.array([[0, -1j], [1j, 0]])
sig3 = np.array([[1, 0], [0, -1]])
SIG = [sig1, sig2, sig3]

def mats(coef):
    # coef shape (3 mu, 3 a)
    return [sum(coef[mu, a] * SIG[a] for a in range(3)) / 2 for mu in range(3)]

def action(coef, m2):
    As = mats(coef)
    s = 0.0
    for mu in range(3):
        for nu in range(mu + 1, 3):
            C = As[mu] @ As[nu] - As[nu] @ As[mu]
            s += float(np.real(np.trace(C.conj().T @ C)))
    s *= 0.25
    tr2 = sum(float(np.real(np.trace(A @ A))) for A in As)
    return s + 0.5 * m2 * tr2

def weight(coef, m2, p4):
    w = np.exp(-action(coef, m2))
    if p4:
        G = coef.T @ coef          # G_ab = sum_mu A^a_mu A^b_mu  (3x3 PSD)
        d = np.linalg.det(G)
        w *= d ** 4
    return w

def probes(coef):
    As = mats(coef)
    f1 = float(np.real(np.trace(As[0] @ As[1])))
    C = As[0] @ As[1] - As[1] @ As[0]
    t2 = np.trace(C @ As[2])
    return f1, t2, abs(t2) ** 2

def run(seed, m2, p4, nsteps=400000, burn=40000, step=0.45, thin=20):
    rng = np.random.default_rng(seed)
    coef = rng.normal(size=(3, 3))
    w = weight(coef, m2, p4)
    acc = 0
    s_f1 = s_f1sq = s_f2abs2 = s_f1_meancheck = 0.0
    n = 0
    for it in range(nsteps):
        prop = coef + step * rng.normal(size=(3, 3))
        wp = weight(prop, m2, p4)
        if wp > 0 and np.log(wp) - np.log(w) > np.log(rng.random() + 1e-300):
            coef, w = prop, wp
            acc += 1
        if it >= burn and (it - burn) % thin == 0:
            f1, t2, f2abs2 = probes(coef)
            s_f1 += f1
            s_f1sq += f1 * f1
            s_f2abs2 += f2abs2
            n += 1
    return acc / nsteps, s_f1 / n, s_f1sq / n, s_f2abs2 / n, n

print("Metropolis, N=2 truncated model (mu=0,1,2), seed 20261108, m^2=1")
for p4 in (False, True):
    tag = "p=4 (Pfaffian weight (det G)^4)" if p4 else "p=0 (bosonic)"
    acc, m_f1, m_f1sq, m_f2abs2, n = run(20261108, 1.0, p4)
    print(f"[{tag}] acceptance={acc:.3f}, nsamp={n}")
    print(f"  <f1>                = {m_f1:+.5f}   (theta-symmetry cross-check: ~0)")
    print(f"  <f1^2>              = {m_f1sq:.5f}")
    print(f"  reflected <f1^theta,f1> = {-m_f1sq:+.5f}   (must be negative)")
    print(f"  <|f2|^2>            = {m_f2abs2:.5f}")
    print(f"  reflected <f2^theta,f2> = {-m_f2abs2:+.5f}   (must be negative)")
    print(f"  for g=1+f1: <g^theta g> = {1.0 - m_f1sq:+.5f}")
# second seed for stability
print("seed check (different seed):")
for p4 in (False, True):
    acc, m_f1, m_f1sq, m_f2abs2, n = run(777, 1.0, p4)
    tag = "p=4" if p4 else "p=0"
    print(f"  [{tag}] -<f1^2>={-m_f1sq:+.5f}  -<|f2|^2>={-m_f2abs2:+.5f}")
