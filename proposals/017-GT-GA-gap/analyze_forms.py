"""
Reads the quadratic forms saved by hk_eval.py (forms/S_<bg>_<sector>_k<kappa>_n<n>_lam<m>.npy), reduces them on the
three-dimensional quotient u ~ q and prints eigenvalues relative to rho_bar^2 p^2 M (units of proposal 015):
   lam^4 <-> a_1 form (this is what enters the Lambda^2 term),  lam^2 <-> a_0 check.
Then compares with the closed forms
   vector (alpha = 1/(1-kappa)):  e_TT = 5/6 - (alpha-1)/24 ,  e_3 = 1/2 - (alpha-1)/8 + (alpha^2-1)/4 ,  a_0: (3+alpha^2)/4 relative to kappa=0
   scalar: e_TT = -1/24, e_3 = -1/8 ; Dirac (4 comps, weight +1): e_TT = 1/3, e_3 = 0
   ghost with F = D.a + c E.a:  uniform shift -c^2 q^2/(8 p^2)  ;  vector with the same F: uniform shift +c^2 q^2/(4 p^2).
"""
import glob, os, re
import numpy as np

BG = {'A': dict(a0=4.0, b0=9 / 4, p=[1 / 2, -3 / 5, 2 / 3, 1 / 3]),
      'B': dict(a0=3.0, b0=4 / 3, p=[1, -1 / 2, 1 / 3, 2 / 5])}


def reduce(S, bg):
    a0, b0, p = bg['a0'], bg['b0'], np.array(bg['p'])
    Tb = np.zeros((4, 4)); Tb[0, 1], Tb[1, 0], Tb[2, 3], Tb[3, 2] = a0, -a0, b0, -b0
    q = Tb @ p
    rhobar = 1 / (a0 * b0)
    Qm, _ = np.linalg.qr(np.column_stack([q, np.eye(4)]))
    B = Qm[:, 1:4]
    red = B.T @ S @ B / (q @ q) / (rhobar ** 2 * (p @ p))
    return np.sort(np.linalg.eigvalsh(0.5 * (red + red.T))), q @ q / (p @ p)


here = os.path.dirname(os.path.abspath(__file__))
rows = []
for f in sorted(glob.glob(os.path.join(here, 'forms', 'S_*_lam4.npy'))):
    m = re.match(r'S_([AB])_(\w+?)_k([-\d.e]+)_n(\d+)_lam4\.npy', os.path.basename(f))
    if not m:
        continue
    bgid, sector, kv, n = m.group(1), m.group(2), float(m.group(3)), int(m.group(4))
    S4 = np.load(f)
    S2 = np.load(f.replace('lam4', 'lam2'))
    ev, q2p2 = reduce(S4, BG[bgid])
    ev2, _ = reduce(S2, BG[bgid])
    rows.append((bgid, sector, kv, n, ev, ev2[-1], q2p2))

print('bg sector kappa n | lam^4 eigenvalues (sorted)            | prediction (TT, third)            | a0 third mode')
for bgid, sector, kv, n, ev, a0third, q2p2 in rows:
    tt = np.mean(ev[np.argsort(abs(ev - np.median(ev)))[:2]]) if sector != 'scalar' else None
    if sector == 'vector':
        al = 1 / (1 - kv)
        pred = (5 / 6 - (al - 1) / 24, 0.5 - (al - 1) / 8 + (al ** 2 - 1) / 4)
        a0pred = (3 + al ** 2) / 4
    elif sector == 'dirac':
        pred = (1 / 3, 0.0); a0pred = 1.0
    elif sector == 'scalar':
        pred = (-1 / 24, -1 / 8); a0pred = 1.0
    elif sector == 'vectorc':
        pred = (5 / 6 + kv ** 2 * q2p2 / 4, 0.5 + kv ** 2 * q2p2 / 4); a0pred = 1.0
    elif sector == 'ghostc':
        pred = (-1 / 24 - kv ** 2 * q2p2 / 8, -1 / 8 - kv ** 2 * q2p2 / 8); a0pred = 1.0
    else:
        pred = (np.nan, np.nan); a0pred = np.nan
    # TT pair = the two nearly degenerate eigenvalues; third = the remaining one
    d = [abs(ev[0] - ev[1]), abs(ev[1] - ev[2])]
    if d[0] < d[1]:
        TT, third = 0.5 * (ev[0] + ev[1]), ev[2]
    else:
        TT, third = 0.5 * (ev[1] + ev[2]), ev[0]
    print(f'{bgid} {sector:8s} {kv:8.4f} {n:2d} | TT {TT: .6f} third {third: .6f} | pred TT {pred[0]: .6f} third {pred[1]: .6f} | a0 third {a0third:.6f} (x(3+al^2)/4 rel. kappa=0 value if vector)')

print()
print('a_0 check (lam^2 third mode, vector sector): ratio to the kappa=0 value of the same background vs (3+alpha^2)/4')
base = {r[0]: r[5] for r in rows if r[1] == 'vector' and r[2] == 0.0}
for bgid, sector, kv, n, ev, a0third, q2p2 in rows:
    if sector == 'vector' and bgid in base:
        al = 1 / (1 - kv)
        print(f'  {bgid} kappa={kv:8.4f} alpha={al:7.4f}: ratio {a0third / base[bgid]:.5f}   (3+alpha^2)/4 = {(3 + al ** 2) / 4:.5f}')

# least-squares fit of the third-mode offset and of the TT eigenvalue as polynomials in alpha (vector sector, background A, n=20)
al_, tt_, th_ = [], [], []
for bgid, sector, kv, n, ev, a0third, q2p2 in rows:
    if sector == 'vector' and bgid == 'A' and n == 20 and abs(kv - 2 / 3) > 1e-6:
        d = [abs(ev[0] - ev[1]), abs(ev[1] - ev[2])]
        TT, third = (0.5 * (ev[0] + ev[1]), ev[2]) if d[0] < d[1] else (0.5 * (ev[1] + ev[2]), ev[0])
        al_.append(1 / (1 - kv)); tt_.append(TT); th_.append(third)
al_ = np.array(al_)
print()
print('fit e_TT(alpha) = c0 + c1 alpha + c2 alpha^2  :', np.polyfit(al_, tt_, 2)[::-1], ' (closed form: 0.875, -1/24, 0)')
print('fit e_3(alpha)  = c0 + c1 alpha + c2 alpha^2  :', np.polyfit(al_, th_, 2)[::-1], ' (closed form: 1/2+1/8-1/4 = 0.375, -1/8, 1/4)')
