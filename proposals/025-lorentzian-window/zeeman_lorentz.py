"""025 script 6: Lorentzian nilpotent flux F_ab(zeta) = zeta_k S^{ab}_k of [D^a, D^b] (centre part) for the four-matrix class with eta=diag(-1,1,1,1).
Eigenvalues of F^a_b = eta^{ac} F_cb: pairs (+-i b) magnetic-type and (+-a) electric-type (a real).  The vector Zeeman block of H_V has eigenvalues +-2b (real) and +-2 i a (imaginary):
the factor exp(-i s (H - i eps)) is a phase for +-2b and grows like exp(2 s a) for the imaginary pair, while log det(sigma + Z) = ln(sigma^2 - 4b^2) + ln(sigma^2 + 4a^2) is finite."""
import sys, numpy as np
sys.path.insert(0, r'../023-casimir-regulator')
from symbol_tools import *
rng = np.random.default_rng(3)
eta = np.diag([-1., 1, 1, 1])
print(" y4^2   theta  |  eig(eta F)  (a: real pair, b: imaginary pair)  | I1=F_ab F^ab/2=b^2-a^2  I2=F.Fdual   | (b>a?)")
stat = {'mixed': 0, 'purely_mag': 0, 'purely_el': 0}
rows = 0
for t in range(8):
    z = rand_z_pos(rng, rng.uniform(0.5, 4)); M0 = Mfun(z); y = M0[:5, 5]
    sym = symbol(M0, [(a, 4) for a in range(4)], [-1., 1, 1, 1])
    c, Fh = sym['c'], sym['F']
    S = np.einsum('Ii,ijk,Jj->IJk', c, Fh, c)                 # F_{IJ,k}, raw antisymmetric in I,J (index = matrix label a)
    for th in np.linspace(0, np.pi, 4, endpoint=False):
        zeta = np.array([np.cos(th), np.sin(th)])
        F = np.einsum('abk,k->ab', S, zeta)
        Fm = eta @ F                                           # F^a_b
        ev = np.linalg.eigvals(Fm)
        I1 = 0.25*np.sum(F * (eta @ F @ eta)) * 2 / 2           # F_ab F^ab / 2 up to factor conv
        Iab = 0.5*np.sum(F * (eta @ F @ eta))
        tr2 = np.trace(Fm @ Fm)                                # = -F_ab F^ab
        eps = np.zeros((4,4,4,4))
        import itertools
        for p in itertools.permutations(range(4)): eps[p] = np.linalg.det(np.eye(4)[list(p)])
        Fd = 0.5*np.einsum('abcd,cd->ab', eps, F)
        I2 = np.sum(F*Fd)
        ev_s = np.sort_complex(np.round(ev, 5))
        print("%7.3f %5.2f | %s | %9.4f  %9.4f | tr(F^2)=%9.4f = -F_abF^ab: %s" % (y[4]**2, th, np.round(ev_s, 4), Iab, I2, tr2, np.isclose(tr2, -2*Iab, rtol=1e-6) or np.isclose(tr2, -Iab, rtol=1e-6)))
