"""030 script 1: next-to-leading (weight-2) symbol of the resolvent of H = eta^{ab} Pi_a Pi_b, Pi_a = omega_a - eps*alpha_a*zeta*sin(phi), omega_a = w0_a.p, zeta = Y.p, [omega_a, phi] = -i kappa_a.
This is the exact reduction of H_X = -Box_X, X^a = T^a + eps*alpha^a*cos(phi), phi = q.y, to the constant-first-jet sector (see the proposal).
Left-quantised symbols; composition (a o b) = sum_n (1/n!) (D_xi^n a)(-i d_phi)^n b with D_xi = kappa_a d/d omega_a (derivative along q in xi-space).
Variables: w_a (= omega'_a = omega_a - eps zeta alpha_a S), zeta, S=sin(phi), C=cos(phi), Ui = 1/(eta w w - z).
Output: r0, r1, r2 as polynomials in (w, zeta, S, C, eps) times powers of Ui; stored as pickles for the later scripts."""
import sympy as sp, pickle, itertools, sys

def build(eta, names=None):
    n = len(eta)
    w = sp.symbols('w1:%d' % (n + 1)); al = sp.symbols('al1:%d' % (n + 1)); ka = sp.symbols('ka1:%d' % (n + 1))
    zeta, S, C, eps, Ui = sp.symbols('zeta S C eps Ui')
    ak = sum(eta[a] * al[a] * ka[a] for a in range(n))            # alpha.kappa
    dw = [-eps * zeta * al[a] * C for a in range(n)]               # d_phi omega'_a at fixed omega
    du = sum(2 * eta[a] * w[a] * dw[a] for a in range(n))          # d_phi u, u = eta w w - z
    def dphi(F):
        out = sp.diff(F, S) * C - sp.diff(F, C) * S
        out += sum(sp.diff(F, w[a]) * dw[a] for a in range(n))
        out += sp.diff(F, Ui) * (-Ui ** 2 * du)
        return out
    def D(F):
        return sum(ka[a] * (sp.diff(F, w[a]) + sp.diff(F, Ui) * (-Ui ** 2) * 2 * eta[a] * w[a]) for a in range(n))
    p2 = None                                                      # symbol p2 = u (u = 1/Ui)
    Dp2 = 2 * sum(eta[a] * ka[a] * w[a] for a in range(n))         # D_xi u
    D2p2 = 2 * sum(eta[a] * ka[a] ** 2 for a in range(n))          # D_xi^2 u
    p1 = sp.I * eps * ak * zeta * C
    r0 = Ui
    r1 = -Ui * (p1 * r0 + Dp2 * (-sp.I * dphi(r0)))
    r2 = -Ui * (p1 * r1 + Dp2 * (-sp.I * dphi(r1)) + sp.Rational(1, 2) * D2p2 * (-dphi(dphi(r0))))
    return dict(w=w, al=al, ka=ka, zeta=zeta, S=S, C=C, eps=eps, Ui=Ui, r0=r0, r1=sp.expand(r1), r2=sp.expand(r2), n=n, eta=eta, dphi=dphi, D=D)

if __name__ == "__main__":
    eta = [-1, 1, 1, 1]
    B = build(eta)
    print("r1: number of terms", len(sp.Add.make_args(B['r1'])), " r2: number of terms", len(sp.Add.make_args(B['r2'])))
    Ui = B['Ui']
    P2 = sp.Poly(B['r2'], Ui)
    print("powers of Ui in r2:", sorted(m[0] for m in P2.monoms()))
    P1 = sp.Poly(B['r1'], Ui)
    print("powers of Ui in r1:", sorted(m[0] for m in P1.monoms()))
    out = {k: B[k] for k in ['r0', 'r1', 'r2']}
    out.update({k: B[k] for k in ['w', 'al', 'ka', 'zeta', 'S', 'C', 'eps', 'Ui']})
    pickle.dump(out, open('nlo_symbol_eta4.pkl', 'wb'))
    print("saved nlo_symbol_eta4.pkl")
