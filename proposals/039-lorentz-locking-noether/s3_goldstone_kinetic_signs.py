"""s3: signature of the Goldstone (local-rotation) quadratic form induced by rho^2 X about constant Theta-bar.
The 12 real parameters are Re/Im amplitudes of the six lambda_{AB}.  Hessian of X over the orbit at fixed class amplitude.
Reports, per random (Theta-bar, p), the diagonal Hessian entries on boost pairs (0i) and rotation pairs (ij) in the eta-frame labels
and the (+,-) eigenvalue counts."""
import numpy as np, sys
sys.path.insert(0, '.')
import importlib.util
spec = importlib.util.spec_from_file_location("s2", "s2_goldstone_extremum.py")
src = open("s2_goldstone_extremum.py", encoding="utf-8").read().split('print("signature')[0]
ns = {}
exec(src, ns)
np_ = np
rng = np.random.default_rng(5)
for eta_d in [(1, 1, 1, 1), (-1, 1, 1, 1)]:
    for t in range(4):
        w0 = ns['rand_w0'](); p = rng.normal(size=4)
        eta, etai, E, G, Gi = ns['sym_setup'](eta_d, w0)
        Eh = ns['class_amp'](etai, w0, p, rng.normal(size=4))
        c0, sol, ev = ns['quad_ext'](eta, etai, E, Gi, p, Eh)
        f = lambda v: ns['invariants'](ns['torsion_amp'](eta, E, p, ns['shifted'](etai, E, Eh, v)), Gi)[0]
        diag = []
        for k, (a, b) in enumerate(ns['pairs']):
            e = np.zeros(12); e[k] = 1.0
            diag.append(f(e) + f(-e) - 2*f(np.zeros(12)))
        boost = [round(d, 3) for d, (a, b) in zip(diag, ns['pairs']) if a == 0]
        rot = [round(d, 3) for d, (a, b) in zip(diag, ns['pairs']) if a != 0]
        print(eta_d, "boost-pair Hessian diag:", boost, "rotation-pair:", rot, "eig (+,-):", (int((ev > 1e-9).sum()), int((ev < -1e-9).sum())), "min|eig|:", round(float(np.abs(ev).min()), 4))
