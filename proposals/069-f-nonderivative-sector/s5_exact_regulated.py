"""s5 (round 2): the regulated U with the cubic Hessian evaluated EXACTLY (no truncation of the
small-s_Lambda expansion), as required by review-r1 F1, and the parts of F3 that do not depend on
the regulator.

Exact identity (units chi = 1, eps = s_Lambda chi^2):
    U(eps) = int_eps^inf ds s^-3 sum_n w_n e^{-s lam_n} = eps^-2 sum_n w_n E_3(eps lam_n),
with E_3 the generalised exponential integral (E_3(0) = 1/2), valid for lam_n >= 0.
Since sum w = sum w lam = 0 exactly, E_3(z) may be replaced by g3(z) = E_3(z) - 1/2 + z, which is
evaluated without cancellation.  s2's closed form is the expansion of g3 to order z^2 with the
remainder dropped; that remainder is O(eps lam_max) = O(eps N^2), i.e. O(1) at eps N^2 ~ 1.
"""
import os, io, contextlib, importlib.util
import numpy as np, mpmath as mp
from scipy.special import expn

here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("s2", os.path.join(here, "s2_traces.py"))
s2 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(s2)

EG = 0.5772156649015329
FACT = [1.0]
for k_ in range(1, 40):
    FACT.append(FACT[-1] * k_)

def g3(z):
    z = np.asarray(z, float); out = np.empty_like(z)
    sm = z < 0.5; zs = z[sm]; ser = np.zeros_like(zs); m = zs > 0
    ser[m] = zs[m]**2 / 2 * (-np.log(zs[m]) + 1.5 - EG)
    for k in range(3, 36):
        ser += -((-zs)**k) / ((k - 2) * FACT[k])
    out[sm] = ser; out[~sm] = expn(3, z[~sm]) - 0.5 + z[~sm]
    return out

def Uex(N, kap, eps):
    w, x = s2.wl(N, kap, "v-tau")
    assert x.min() >= 0
    assert abs(np.sum(w)) < 1e-6 and abs(np.sum(w * x)) < 1e-6 * N**2
    return float(np.sum(w * g3(eps * x)) / eps**2)

print("A. exact form against direct quadrature (N=3, mpmath, 40 digits)")
mp.mp.dps = 40
for kap in (2.0, -0.3365, 1.0):
    w, x = s2.wl(3, kap, "v-tau")
    f = lambda s: sum(mp.mpf(float(a)) * mp.e ** (-s * mp.mpf(float(b))) for a, b in zip(w, x))
    for eps in (mp.mpf("0.5"), mp.mpf("0.05")):
        q = mp.quad(lambda s: f(s) / s**3, [eps, 1, 10, mp.inf])
        print(f"  kappa={kap:+.4f} eps={float(eps):5.2f}  quad={float(q):+.12f}  E_3 form={Uex(3, kap, float(eps)):+.12f}  truncated={s2.Ureg(3, kap, float(eps)):+.6f}")

print("\nB. per N^4 at kappa=-0.3365, N=512: exact vs truncated (review-r1 F1 table)")
for e in (0.9, 0.5, 0.1):
    eps = e / 512**2
    print(f"  eps*N^2={e:4.2f}  exact={Uex(512, -0.3365, eps)/512**4:+.4f}  truncated={s2.Ureg(512, -0.3365, eps)/512**4:+.4f}")

print("\nC. sign of the exact U: max of U/N^4 over eps*N^2 in [1e-4, 30] (99 points), per kappa and N")
grid_e = np.concatenate([np.logspace(-4, 0, 41), np.linspace(1.5, 30, 58)])
allneg = True
for k in (-0.99, -0.5, -0.3365, 0.0, 0.5, 1.0, 1.5, 1.8, 1.9, 1.95, 1.99):
    row = []
    for N in (16, 64, 512):
        mx = max(Uex(N, k, e / N**2) / N**4 for e in grid_e)
        row.append(f"N={N}: {mx:+.2e}")
        if k <= 1.9:
            allneg = allneg and mx < 0
    print(f"  kappa={k:+.4f}  " + "  ".join(row))
print("  negative at every sampled limit for every sampled kappa <= 1.9 and N in {16,64,512}:", allneg)
print("  truncated form vanishes at eps*N^2 = 0.9257 (kappa=-0.3365, N=512); exact value there:",
      f"{Uex(512, -0.3365, 0.9257/512**2)/512**4:+.4f}")
print("  kappa = 2 (c=0): exact U/N^2 at eps*N^2 = 1e-6, N=512:", f"{Uex(512, 2.0, 1e-6/512**2)/512**2:.5f} (merged Uhat/N^2 -> 1)")

print("\nD. the example of the merged text (x = chi^2/vartheta = 3/10, vartheta = 1, c/chi = 2.33648 at chi^2 = 0.3)")
print("   units F sqrt|g| N^2 vartheta^2 / 32 pi^2 ; P = -chi^4 U / N^2 replaces U_4 = -x^2 = -0.09 ; s_Lambda fixed in physical units")
r = 1.168241965973535; chis = np.sqrt(0.3); c = 2 * r * chis; h = 1e-5
def P(chi, N, sL):
    return -chi**4 * Uex(N, 2 - c / chi, sL * chi**2) / N**2
def dP(N, e):
    sL = e / (chis**2 * N**2)
    return (P(chis * np.exp(h), N, sL) - P(chis * np.exp(-h), N, sL)) / (2 * h)
for N in (16, 64, 512):
    for e in (0.5, 0.1):
        p0 = P(chis, N, e / (chis**2 * N**2))
        print(f"  N={N:4d} s_L chi^2 N^2={e:3.1f}:  P={p0:10.2f}  P/7.935={p0/7.935:8.2f}  dP/dlnchi={dP(N, e):10.2f}")
def U2(chi):
    k = 2 - c / chi
    return (2 - 1.25 * k**2) * chi**2
dU2 = (U2(chis * np.exp(h)) - U2(chis * np.exp(-h))) / (2 * h)
print(f"  U_2 with the Hessian (large N) = {U2(chis):+.4f} (merged -0.9); dU_2/dlnchi at fixed c = {dU2:+.4f} (merged 2U_2 = -1.8); Y = 7.5 unchanged")
def U2t(chi, th):     # general vartheta: U_2 = -[2(kappa^2-4)/th - (3/4)(kappa^2-8)] chi^2/th, units N^2 th^2
    k = 2 - c / chi; return -(2 * (k**2 - 4) / th - 0.75 * (k**2 - 8)) * chi**2 / th
for th in (1.0, 1.2, 1.5, 2.0):
    ch = np.sqrt(0.3 * th)          # x = chi^2/th = 3/10 held fixed; c/chi = 2r held fixed
    cs = c; c = 2 * r * ch
    d = (U2t(ch * np.exp(h), th) - U2t(ch * np.exp(-h), th)) / (2 * h)
    print(f"  vartheta={th}: U_2={U2t(ch, th):+.4f}  dU_2/dlnchi={d:+.4f}  dU_2+Y={d+7.5:+.4f}  (> 5.34: {d+7.5>5.34})")
    c = cs
grid_s = np.concatenate([np.logspace(-4, 0, 41), np.linspace(1.5, 30, 58)])
for N in (16, 64, 512):
    sl = [dP(N, e) for e in grid_s]; i = int(np.argmin(sl))
    print(f"  N={N:4d}: min over s_L chi^2 N^2 in [1e-4,30] of dP/dlnchi = {sl[i]:+.3f} (at {grid_s[i]:.3g}); "
          f"min one-loop slope dP + dU_2 + Y = {sl[i]+dU2+7.5:+.3f} against 5.34 = -(tree slope); all > 5.34: {min(sl)+dU2+7.5 > 5.34}")

print("\nE. U_2 from the exact spectra (V = Vhat chi^2, T = That chi^2 at kappa = -0.33648)")
k = 2 - 2 * r
for N in (64, 512):
    V = s2.I2(N, k, "v"); T = s2.I2(N, k, "tau")
    print(f"  N={N}: Vhat/N^2={V/N**2:.4f} (kappa^2={k**2:.4f}), That/N^2={T/N**2:.4f};  U_2 = {-(2*(V-T) - 0.75*(V-2*T))/N**2*0.3:+.4f}")
