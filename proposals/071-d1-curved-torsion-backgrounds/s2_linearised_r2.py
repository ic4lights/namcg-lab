"""S2. Linearised frame and connection equations on the R != 0, T != 0 backgrounds of S1.
Numerical (double precision) unless stated.  Uses core068.M_op (the 068 linearisation of the
closed bracket formulas, which takes arbitrary constant cbar, wbar) and lin.py.
Checks:
 (a) kernel at generic q = the ten gauge directions, which need the curvature term
     omega_a^{de} = xi^c R_ca^{de} in the diffeomorphism directions;
 (b) (R1) fails: the connection equations contain h at R != 0;
 (c) translation labels (generalised R2): for each I, the fluctuation
     h_a^c = -f_a delta^c_I, omega_a^{cd} = -f_a w_I^{cd} is mapped by the forty equations to
     B1_b^e = (Qf)_b delta^e_I, B2_b^{de} = -(Qf)_b w_I^{de}, with Q the order-zero operator
     (F_ab = nabla_a A_b - nabla_b A_a + T_ab^c A_c, Q_b = nabla^a F_ab - T_ab^c F^a_c);
 (d) characteristic roots along lines q = (t, kvec): every root satisfies q^2 = 2 alpha (k.q)
     for alpha in a finite set, i.e. lies on a shifted null cone (q - alpha k)^2 = 0, k^a = (-1,0,1,0);
     and conversely M(q) drops rank on each such cone at random complex points;
 (e) the boost-dilation symmetry of F: boost in the 0-2 plane composed with a dilation maps w to w.
Round 2: (d) no longer rounds alpha.  The unrounded alpha of all roots are clustered, each
cluster is identified with a closed form a + i b (a^2 and 2b integers, accepted only if the
cluster median lies within 1e-4 of it), and the converse rank test is run at the closed form;
the median itself is also tested.  (g) sign map: the alpha set of the background -w is minus
that of w (the dilation D -> -D), so the sign of alpha depends on the normalisation of w.
Run: python -I s2_linearised_r2.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import lin, core068 as K, tools068 as Tl, bg

np.set_printoptions(precision=4, suppress=True)
rng = np.random.default_rng(11)
KUP = np.array([-1.0, 0, 1.0, 0])
ETA = K.ETA


def vec(f, I, W, sh, sw):
    h = np.zeros((4, 4, 1), complex); w = np.zeros((4, 4, 4, 1), complex)
    for a in range(4):
        h[a, I, 0] = sh * f[a]; w[a, :, :, 0] = sw * f[a] * W[I]
    return K.pack_hw(h, w)


def qsq(q):
    return -q[0] ** 2 + q[1] ** 2 + q[2] ** 2 + q[3] ** 2




def cluster(vals, tol=5e-3):
    vals = sorted(vals, key=lambda z: (z.real, z.imag))
    groups = []
    for z in vals:
        for g in groups:
            if abs(z - np.median(np.real(g)) - 1j * np.median(np.imag(g))) < tol:
                g.append(z); break
        else:
            groups.append([z])
    out = []
    for g in groups:
        med = np.median(np.real(g)) + 1j * np.median(np.imag(g))
        out.append((med, max(abs(z - med) for z in g)))
    return sorted(out, key=lambda p: (round(p[0].real, 3), round(p[0].imag, 3)))


def closed_form(z, tol=1e-4):
    """a + i b with a^2 integer (a = +-sqrt(n)) and 2b integer, if within tol of z."""
    n = int(round(z.real ** 2)); a = np.sign(z.real) * np.sqrt(n) if n else 0.0
    b2 = int(round(2 * z.imag)); b = b2 / 2
    cf = a + 1j * b
    if abs(cf - z) > tol:
        return None
    ra = ('0' if n == 0 else ('%s%s' % ('-' if a < 0 else '', 'sqrt%d' % n if n not in (1, 4, 9) else '%d' % int(abs(a)))))
    return cf, '%s%+gi' % (ra, b)


BGS = [('F (s=1, tau=-2+sqrt3, trace-free)', lin.bg_F(), [1, 1, 1, 1]),
       ('F (s=1, tau=1)', lin.bg_F(tau=1.0), [1, 1, 1, 1]),
       ('H (kappa=1, zeta=1, x=0), characters q_2 = 0', lin.bg_H(), [1, 1, 0, 1])]
for name, (c, w), mask in BGS:
    print('==', name)
    B1, B2, T, R = bg.brackets(c, w, ETA)
    print('  background |B1|, |B2| = %.1e %.1e ; |T| = %.3f ; |R| = %.3f' % (np.abs(B1).max(), np.abs(B2).max(),
                                                                            np.abs(T).max(), np.abs(R).max()))
    for t in range(3):
        q = rng.normal(size=4) * np.array(mask)
        E = K.chars(q); M = K.M_op(c, w, E)
        G = lin.gauge_vectors_R(c, w, E); G0 = lin.gauge_vectors_R(c, w, E, with_R=False)
        ns = 40 - K.rank(M)
        Gk = np.linalg.matrix_rank(np.hstack([G, np.linalg.svd(M)[2][-ns:].conj().T]), 1e-8)
        print('  (a) q=%s rank M = %d, |M G| = %.1e, kernel = span G: %s ; without the xi R term |M G0| = %.2f'
              % (np.round(q, 3), K.rank(M), np.abs(M @ G).max(), Gk == 10, np.abs(M @ G0).max()))
        if t == 0:
            print('  (b) |dB2/dh| (connection equations on pure frame fluctuations) = %.3f' % np.abs(M[16:, :16]).max())
        if mask[2] == 1:
            Q = lin.Qop(c, w, E); err = 0.0
            for I in range(4):
                for b in range(4):
                    f = np.eye(4)[b]
                    err = max(err, np.abs(M @ vec(f, I, w, -1, -1) - vec(Q[:, b], I, w, +1, -1)).max())
            print('  (c) translation labels: max |M v_I(f) - u_I(Qf)| = %.1e ; rank Q = %d' % (err, K.rank(Q)))
    if mask[2] == 1:
        raw = []
        for kv in ([0.3, -0.5, 0.7], [1.1, 0.2, -0.4], [-0.6, 0.9, 0.25], [0.0, 0.0, 0.0]):
            a = np.array([0, *kv]); b = np.array([1.0, 0, 0, 0])
            for lab, fun, r in [('M', lambda t: K.M_op(c, w, K.chars(a + t * b)), 30),
                                ('Q', lambda t: lin.Qop(c, w, K.chars(a + t * b)), 3)]:
                roots = Tl.char_roots(fun, r)
                al = []; nkq = 0
                for z in roots:
                    q = a + z * b; kq = KUP @ q
                    if abs(kq) > 1e-3 * np.linalg.norm(q):
                        al.append(qsq(q) / (2 * kq))
                    else:
                        nkq += 1
                al = [z for z in al if abs(z) > 1e-3]
                if lab == 'M':
                    raw += al
                cl = cluster(al)
                print('  (d) kvec=%s %s: %d roots; alpha clusters (median, spread) %s%s' % (kv, lab, len(roots),
                      ['%.6f%+.6fj (%.0e)' % (m.real, m.imag, sp_) for m, sp_ in cl],
                      ' (+ %d roots with |k.q| < 1e-3 |q|)' % nkq if nkq else ''))
        cl = cluster(raw)
        print('  (d) converse: sigma_30/sigma_1 of M(q) at random complex q on (q - alpha k)^2 = 0'
              ' (generic rank 30; a value ~1e-12 or below is a rank drop), alpha unrounded:')
        def s30(q):
            sv = np.linalg.svd(K.M_op(c, w, K.chars(q)), compute_uv=False)
            return sv[29] / sv[0]
        def test(al0):
            vals = []
            for t in range(3):
                v = 0.5 * (rng.normal(size=3) + 1j * rng.normal(size=3))
                qt = np.array([np.sqrt(v @ v), *v])            # complex null covector
                vals.append(s30(qt + al0 * np.array([1.0, 0, 1.0, 0])))   # k_a = (1,0,1,0)
            return vals
        allon = []
        for med, spread in cl:
            cf = closed_form(med)
            v_med = test(med)
            if cf is None:
                print('      median %.8f%+.8fj: no closed form; at median %s' % (med.real, med.imag, ['%.1e' % x for x in v_med]))
                continue
            v_cf = test(cf[0])
            allon += v_cf
            print('      alpha = %s (|median - closed form| = %.1e): at closed form %s ; at median %s'
                  % (cf[1], abs(med - cf[0]), ['%.1e' % x for x in v_cf], ['%.1e' % x for x in v_med]))
        ctrl = [s30(0.5 * (rng.normal(size=4) + 1j * rng.normal(size=4))) for t in range(6)]
        print('      control (random complex q):', ['%.1e' % x for x in ctrl])
        print('      SUMMARY %s: max over cones at closed forms %.1e ; min over controls %.1e'
              % (name, max(allon), min(ctrl)))
# (e) boost-dilation symmetry of F
from scipy.linalg import expm
c, w = lin.bg_F()
for th in (0.3, -0.7):
    X = np.zeros((4, 4)); X[0, 2] = X[2, 0] = th            # boost generator acting on lower indices
    L = expm(X)
    assert np.abs(L.T @ ETA @ L - ETA).max() < 1e-12
    Li = np.linalg.inv(L)
    # w_a^{cd}: lower a, upper c,d
    wt = np.einsum('aA,cC,dD,ACD->acd', L, Li.T, Li.T, w)
    best = min((np.abs(wt * lam - w).max(), lam) for lam in (np.exp(th), np.exp(-th)))
    print('== (e) boost theta=%.1f: min over dilation factor e^{+-theta} of |w_boosted * factor - w| = %.1e' % (th, best[0]))
# (f) block-triangular form: labels f^I = -h_a^I, connection remainder w' = w - h_a^I w_I;
#     outputs g^I = B1_b^I, B2' = B2 + B1_b^I w_I.  Then B2' depends on w' only, and the
#     roots of the 24 x 24 block Y: w' -> B2' are the alpha with nonzero imaginary part.
print('== (f) block-triangular form on F')
for name, (c, w) in [('F trace-free', lin.bg_F()), ('F tau=1', lin.bg_F(tau=1.0))]:
    # change of variables matrices (40x40): x = P x', with x' = (f, w')
    P = np.zeros((40, 40)); Pout = np.zeros((40, 40))
    for a in range(4):
        for I in range(4):
            P[4 * a + I, 4 * a + I] = -1.0                  # h_a^I = -f_a^I
            for n, (cc, d) in enumerate(K.PAIRS):
                P[16 + 6 * a + n, 4 * a + I] = -w[I, cc, d]  # w = w' + h_a^I w_I = w' - f_a^I w_I
    for n in range(24):
        P[16 + n, 16 + n] = 1.0
    for b in range(4):
        for I in range(4):
            Pout[4 * b + I, 4 * b + I] = 1.0                # g_b^I = B1_b^I
            for n, (cc, d) in enumerate(K.PAIRS):
                Pout[16 + 6 * b + n, 4 * b + I] = w[I, cc, d]   # B2' = B2 + B1_b^I w_I
    for n in range(24):
        Pout[16 + n, 16 + n] = 1.0
    worst = 0.0
    for t in range(3):
        q = rng.normal(size=4)
        Mp = Pout @ K.M_op(c, w, K.chars(q)) @ P
        worst = max(worst, np.abs(Mp[16:, :16]).max())
    print('  %s: max |dB2\'/df| = %.1e (zero: block-triangular, w\' sources f)' % (name, worst))

    def Yop(t, a, b):
        return (Pout @ K.M_op(c, w, K.chars(a + t * b)) @ P)[16:, 16:]
    a = np.array([0, 0.3, -0.5, 0.7]); b = np.array([1.0, 0, 0, 0])
    q = rng.normal(size=4)
    rY = K.rank((Pout @ K.M_op(c, w, K.chars(q)) @ P)[16:, 16:])
    roots = Tl.char_roots(lambda t: Yop(t, a, b), rY)
    al = sorted(set(complex(np.round(qsq(a + z * b) / (2 * (KUP @ (a + z * b))), 2)) for z in roots),
                key=lambda z: (z.real, z.imag))
    print('  %s: generic rank of Y = %d; roots of Y on the line kvec=(0.3,-0.5,0.7): alpha in %s' % (name, rY, al))

# (g) sign map: alpha set of -w is minus that of w (D -> -D maps solutions to solutions, E -> -E, w -> -w, q -> -q)
print('== (g) sign map w -> -w on F (s = 1 -> s = -1)')
for name, (c, w) in [('F trace-free', lin.bg_F()), ('F tau=1', lin.bg_F(tau=1.0))]:
    sets = []
    for sg in (1, -1):
        a = np.array([0, 0.3, -0.5, 0.7]); b = np.array([1.0, 0, 0, 0])
        roots = Tl.char_roots(lambda t: K.M_op(c, sg * w, K.chars(a + t * b)), 30)
        al = [qsq(a + z * b) / (2 * (KUP @ (a + z * b))) for z in roots]
        sets.append(sorted(set(cf[1] for cf in (closed_form(m) for m, _ in cluster(al)) if cf), key=str))
    print('  %s: alpha(w) = %s ; alpha(-w) = %s' % (name, sets[0], sets[1]))
