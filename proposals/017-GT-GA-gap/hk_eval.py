"""
Numerical evaluation of the second-order heat-trace coefficients c_2 (a_0 term) and c_4 (a_1 term)
for the operators built in hk_lib.py.  See hk_lib.py for the formulas.

Usage:  python hk_eval.py <sector> [kappa ...]   with sector in {scalar, vector, dirac}
Output: for each kappa, the TT-mode and third-mode eigenvalues of the a_1 quadratic form relative to
        rho_bar^2 p^2 M  (the normalisation of Appendix H / proposal 015), and the a_0 check.
"""
import sys, os, pickle, time
import numpy as np
import sympy as sp
import hk_lib as H

BGID = os.environ.get('NAMCG_BG', 'A')
BASE = dict(A=dict(a0=4, b0=sp.Rational(9, 4), p=[sp.Rational(1, 2), sp.Rational(-3, 5), sp.Rational(2, 3), sp.Rational(1, 3)]),
            B=dict(a0=3, b0=sp.Rational(4, 3), p=[1, sp.Rational(-1, 2), sp.Rational(1, 3), sp.Rational(2, 5)]))[BGID]
kap = sp.Symbol('kap')


def get_mats(sector, tag=''):
    fn = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'cache_{sector}{tag}' + ('' if BGID == 'A' else '_' + BGID) + '.pkl')
    if os.path.exists(fn):
        return pickle.load(open(fn, 'rb'))
    bg = H.Background(BASE['a0'], BASE['b0'], BASE['p'])
    if sector == 'scalar':
        M = H.build_scalar(bg)
    elif sector == 'vector':
        M = H.build_vector(bg, kap)
    elif sector == 'dirac':
        M = H.build_dirac_squared(bg)
    elif sector == 'vectorc':
        M = H.build_vector_c(bg, kap)
    elif sector == 'ghostc':
        M = H.build_ghost_c(bg, kap)
    else:
        raise ValueError
    mm = H.mats_from(M)
    out = {}
    for key, mat in mm.items():
        out[key] = sp.srepr(mat)
    pickle.dump(out, open(fn, 'wb'))
    return out


def lam_funcs(mat):
    d = mat.shape[0]
    args = list(H.kk) + [H.lam, kap]
    return [[sp.lambdify(args, mat[a, b], 'numpy') for b in range(d)] for a in range(d)]


def evalmat(fl, K, lamv, kapv):
    d = len(fl)
    N = K.shape[0]
    out = np.zeros((N, d, d), dtype=complex)
    for a in range(d):
        for b in range(d):
            out[:, a, b] = fl[a][b](K[:, 0], K[:, 1], K[:, 2], K[:, 3], lamv, kapv)
    return out


def prepare(sector):
    raw = get_mats(sector)
    mats = {k: eval(v, dict(sp.__dict__)) for k, v in raw.items()}
    d = mats[(0, 0)].shape[0]
    u = list(H.uu)
    funcs = {}
    funcs['A'] = lam_funcs(sp.Matrix(mats[(0, 0)]))
    funcs['V1'] = {}
    for n in (-1, 1):
        V = sp.Matrix(mats[(n, 1)])
        funcs['V1'][n] = [lam_funcs(V.diff(u[i])) for i in range(4)]
    V2 = sp.Matrix(mats[(0, 2)])
    funcs['V2'] = {}
    for i in range(4):
        for j in range(i, 4):
            # symmetric coefficient: V2(u) = sum_ij u_i u_j V2^{(ij)} with V2^{(ij)}=V2^{(ji)}
            if i == j:
                c = V2.diff(u[i], 2) / 2
            else:
                c = V2.diff(u[i], u[j]) / 2
            funcs['V2'][(i, j)] = lam_funcs(c)
    return d, funcs


def gh_grid(n, c):
    x, w = np.polynomial.hermite.hermgauss(n)
    X = np.array(np.meshgrid(x, x, x, x, indexing='ij')).reshape(4, -1).T
    W = (w[:, None, None, None] * w[None, :, None, None] * w[None, None, :, None] * w[None, None, None, :]).reshape(-1)
    Q = X / np.sqrt(c)
    wt = W * np.exp((X ** 2).sum(1)) / c ** 2
    return Q, wt


def expA(sector, q, x, kapv):
    """exp(-x A(q)) with A = q^2 (1 - kappa qhat qhat^T) (vector) or q^2 * 1."""
    q2 = (q * q).sum(1)
    if sector == 'vector':
        d = 4
        z_ = x * kapv * q2
        small = np.abs(z_) < 1e-6
        g = np.where(small, x * kapv * (1 + z_ / 2 + z_ ** 2 / 6), np.expm1(z_) / np.where(small, 1, q2))
        pref = np.exp(-x * q2)
        E = pref[:, None, None] * (np.eye(4)[None] + g[:, None, None] * q[:, :, None] * q[:, None, :])
        return E
    d = 4 if sector in ('dirac', 'vectorc') else 1
    return np.exp(-x * q2)[:, None, None] * np.eye(d)[None]


def run(sector, kapv, n=16, c=None, Nl=10, r0=0.3, nt=8, chunk=30000):
    d, F = prepare(sector)
    Tb = np.array(H.Background(BASE['a0'], BASE['b0'], BASE['p']).Tb.tolist(), dtype=float)
    p = np.array([float(x) for x in BASE['p']])
    w = Tb @ p
    if c is None:
        c = 1.0
    Qall, wtall = gh_grid(n, c)
    Kall = (np.linalg.inv(Tb) @ Qall.T).T
    tn, tw = np.polynomial.legendre.leggauss(nt)
    tn = 0.5 * (tn + 1)
    tw = 0.5 * tw
    jac = 1 / abs(np.linalg.det(Tb)) / (2 * np.pi) ** 4
    lams = r0 * np.exp(2j * np.pi * np.arange(Nl) / Nl)
    Fval = np.zeros((Nl, 4, 4), dtype=complex)
    idx = np.array_split(np.arange(Qall.shape[0]), max(1, Qall.shape[0] // chunk))
    for ix in idx:
        Q, wt, K = Qall[ix], wtall[ix], Kall[ix]
        for il, lv in enumerate(lams):
            E0 = expA(sector, Q, 1.0, kapv)
            for i in range(4):
                for j in range(i, 4):
                    V2 = evalmat(F['V2'][(i, j)], K, lv, kapv)
                    val = (wt * (-np.einsum('nab,nba->n', E0, V2))).sum() * jac
                    Fval[il, i, j] += val
                    if i != j:
                        Fval[il, j, i] += val
            for nn in (1, -1):
                Kp = K + nn * lv * p[None, :]
                Qp = Q + nn * lv * w[None, :]
                Vn = [evalmat(F['V1'][nn][i], K, lv, kapv) for i in range(4)]
                Vm = [evalmat(F['V1'][-nn][i], Kp, lv, kapv) for i in range(4)]
                for t, tw_ in zip(tn, tw):
                    E1 = expA(sector, Qp, t, kapv)
                    E2 = expA(sector, Q, 1 - t, kapv)
                    X = [np.einsum('nab,nbc->nac', Vn[j], E2) for j in range(4)]
                    Y = [np.einsum('nab,nbc->nac', Vm[i], E1) for i in range(4)]
                    for i in range(4):
                        for j in range(4):
                            Fval[il, i, j] += 0.5 * tw_ * (wt * np.einsum('nab,nba->n', Y[i], X[j])).sum() * jac
    res = {}
    for m in (2, 4, 6):
        cm = np.array([(Fval[:, i, j] * lams ** (-m)).mean() for i in range(4) for j in range(4)]).reshape(4, 4)
        res[m] = cm * (4 * np.pi) ** 2
    return res


def forms_to_modes(Mat):
    """Mat[i,j] for i<=j holds the symmetric coefficient of u_i u_j  (off-diagonal: coefficient of u_i u_j, i<j, i.e. 2*Qij)."""
    S = np.zeros((4, 4), dtype=complex)
    for i in range(4):
        for j in range(i, 4):
            if i == j:
                S[i, i] = Mat[i, i]
            else:
                S[i, j] = S[j, i] = Mat[i, j] / 2
    return S


def mode_eigs(S):
    Tb = np.array(H.Background(BASE['a0'], BASE['b0'], BASE['p']).Tb.tolist(), dtype=float)
    p = np.array([float(x) for x in BASE['p']])
    q = Tb @ p
    pf0 = float(BASE['a0'] * BASE['b0'])
    rhobar = 1 / pf0
    Qm, _ = np.linalg.qr(np.column_stack([q, np.eye(4)]))
    B = Qm[:, 1:4]
    q2 = q @ q
    p2 = p @ p
    Sred = B.T @ S @ B / q2 / (rhobar ** 2 * p2)
    return np.linalg.eigvals(Sred), np.linalg.norm(S @ q) / np.linalg.norm(S), Sred


if __name__ == '__main__':
    sector = sys.argv[1]
    n_ = 16
    kaps = []
    for a in sys.argv[2:]:
        if a.startswith('n='):
            n_ = int(a[2:])
        else:
            kaps.append(float(a))
    kaps = kaps or [0.0]
    for kv in kaps:
        t0 = time.time()
        res = run(sector, kv, n=n_, c=max(0.3, min(1.0, 1 - kv)) if sector == 'vector' else None)
        for m in (2, 4):
            S = 0.5 * (res[m] + res[m].T).real
            os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'forms'), exist_ok=True)
            np.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'forms', f'S_{BGID}_{sector}_k{kv}_n{n_}_lam{m}.npy'), S)
            ev, gres, _ = mode_eigs(S)
            ev = np.sort(ev.real)
            print(f'{sector} kappa={kv} n={n_}: lam^{m}: eig(rel to rho^2 p^2 M) = {ev}  gauge residual {gres:.2e}')
        print('time', round(time.time() - t0))
