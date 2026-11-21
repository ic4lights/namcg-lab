"""081 s2: charge-to-edge moment identification in the Gaussian rank-one class.

Class (named exactly): rank-one block-cut edge datum of the appH Row length
paragraph - Q = -2i(|u)(w|-|w)(u|), a = Im(u|w), r = |w_perp|^2; Gaussian state
with independent momenta, so a is a real centered Gaussian independent of r, and
r = s^2 * sum_i g_i E_i with E_i iid Exp(1), g the block-row profile, W = sum g,
s^2 the edge datum of the Edge datum paragraph; leading-order convention a = 0
(the convention under which the manuscript states <ell^2> = 4 s^2 W).
Established here:
 (A) pointwise in configuration, at a = 0: Tr Q^{2p} = 2 ell^{2p} and odd
     charge moments vanish, where ell = 2|w_perp| is the row length (exact,
     numerical against full spectra, deviations ~1e-12);
 (B) Gaussian average: <Tr Q^{2p}> = 2 (4 s^2 W)^p rho_p(g), with
     rho_p(g) = p! h_p(g)/W^p exact (rational check) - the edge-data
     single-scale prediction 2(4 s^2 W)^p is exact at p = 1 (rho_1 = 1) and
     multiplied by the exact profile factor rho_p at p >= 2;
 (C) exact lower bound on the obstruction: rho_p - 1 >= C(p,2) D_eff^{-1},
     D_eff = W^2/sum g^2 (from h_p = sum_{lambda |- p} p_lambda/z_lambda;
     verified on random profiles and in the uniform and fuzzy-proxy classes);
 (D) per-factor multiplicity signature identity of the 080 integrated
     paragraph, reproduced from full charge spectra at (q1,q2)=(2,1),
     (n1,n2)=(1/4,2/9): excesses 9/17 and 81/145.

Run: python -I proposals/081-g-edge-moments/s2_eq_moment_identity.py
Expected invariants: PARTA max dev < 1e-9; PARTB exact rational 0; PARTC
bound violations 0; PARTD |ratio-26/17|, |ratio-226/145| < 1e-9; last line
'PASS s2'.
"""
from fractions import Fraction
from math import comb, factorial

import numpy as np


def hcf(m, xs):
    pw = [sum(x ** t for x in xs) for t in range(m + 1)]
    h = [Fraction(1)]
    for m2 in range(1, m + 1):
        h.append(sum(pw[t] * h[m2 - t] for t in range(1, m2 + 1)) / m2)
    return h[m]


def rho(p, xs):
    return factorial(p) * hcf(p, xs) / sum(xs) ** p


def deff(xs):
    return sum(xs) ** 2 / sum(x * x for x in xs)


def partition_terms(p):
    """All lambda |- p as multiplicity vectors (m_1..m_p); z_lambda denominator."""
    out = []

    def rec(rem, maxpart, m):
        if rem == 0:
            out.append(tuple(m))
            return
        for k in range(min(maxpart, rem), 0, -1):
            m[k - 1] += 1
            rec(rem - k, k, m)
            m[k - 1] -= 1
    rec(p, p, [0] * p)
    return out


def z_lambda(m):
    z = 1
    for k, mk in enumerate(m, start=1):
        z *= (k ** mk) * factorial(mk)
    return z


def part_a(rng):
    worst = 0.0
    for _ in range(200):
        N = 8
        u = rng.standard_normal(N) + 1j * rng.standard_normal(N)
        u /= np.linalg.norm(u)
        z = rng.standard_normal(N) + 1j * rng.standard_normal(N)
        w = z - u * np.vdot(u, z)  # (u|w) = 0 exactly, so a = 0
        Q = -2j * (np.outer(u, w.conj()) - np.outer(w, u.conj()))
        Q = (Q + Q.conj().T) / 2
        ell = 2.0 * np.linalg.norm(w)
        ev = np.linalg.eigvalsh(Q)
        for p in (1, 2, 3):
            got = float(np.sum(ev ** (2 * p)))
            want = 2.0 * ell ** (2 * p)
            worst = max(worst, abs(got - want) / max(1.0, want))
        for p in (0, 1, 2):
            got = float(np.sum(ev ** (2 * p + 1)))
            worst = max(worst, abs(got) / max(1.0, ell ** (2 * p + 1)))
    return worst


def part_b():
    g = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)]
    s2v = Fraction(5, 3)
    W = sum(g)
    resid = []
    for p in range(1, 5):
        lhs = 2 * 4 ** p * s2v ** p * factorial(p) * hcf(p, g)
        rhs = 2 * (4 * s2v * W) ** p * rho(p, g)
        resid.append(lhs - rhs)
    return resid, g, s2v, W


def part_c(rng):
    """Full-spectrum reproduction of the 080 per-factor signature excesses."""
    q1, q2 = 2, 1
    n = [Fraction(1, 4), Fraction(2, 9)]
    nfv = [float(n[0]), float(n[1])]
    q = q1 + q2
    mult = [q1, q2]
    R = np.zeros((2 * q, q))
    U = np.zeros((2 * q, q))
    for i in range(q):
        U[i, i] = 1.0
        f = 0 if i < q1 else 1
        # R = V K^(1/2), V the isometry onto the complement of U's columns:
        # C0 = U^dagger R = 0, Z0 = R^dagger R = K (the 080 construction at A=0)
        R[q + i, i] = np.sqrt(nfv[f])
    Q = -2j * (U @ R.conj().T - R @ U.conj().T)
    Q = (Q + Q.conj().T) / 2
    ev = np.linalg.eigvalsh(Q)
    nz = ev[np.abs(ev) > 1e-10]
    want = []
    for f in range(2):
        for _ in range(mult[f]):
            want.append(2.0 * np.sqrt(nfv[f]))
            want.append(-2.0 * np.sqrt(nfv[f]))
    dev = np.max(np.abs(np.sort(nz) - np.sort(np.array(want))))
    ratios = []
    for p in (1, 2):
        mixed = float(np.sum(nz ** (2 * p)))
        unit1 = float(sum(2.0 * (4.0 * nfv[f]) ** p for f in range(2)))
        ratios.append(mixed / unit1)
    exact = [sum(mult[f] * n[f] ** p for f in range(2)) / sum(n[f] ** p for f in range(2))
             for p in (1, 2)]
    return dev, ratios, exact


def part_d():
    rows = []
    for D in (8, 64, 512, 4096):
        g = [Fraction(1, D)] * D
        rows.append((f'uniform D={D}', float(rho(4, g) - 1),
                     float(6 / D), float(deff(g))))
    for lc in (10, 40, 160):
        g = []
        for l in range(1, lc + 1):
            g += [Fraction(int(l / 2 * 1000), 1000)] * (2 * l + 1)
        rows.append((f'fuzzy nu_l2 lc={lc}', float(rho(4, g) - 1),
                     float(6 / deff(g)), float(deff(g))))
    return rows


def main():
    rng = np.random.default_rng(81002)
    worst = part_a(rng)
    assert worst < 1e-9, worst
    print(f"PARTA pointwise at a=0: max rel dev of Tr Q^{{2p}} from 2*ell^{{2p}} and "
          f"of odd moments from 0, 200 configs: {worst:.3e}")
    resid, g, s2v, W = part_b()
    assert all(x == 0 for x in resid), resid
    print(f"PARTB <Tr Q^{{2p}}> = 2(4 s^2 W)^p rho_p(g), g=(1/2,1/3,1/6) s^2=5/3, "
          f"p=1..4: exact rational 0; rho_1..rho_4 = "
          f"{[str(rho(p, g)) for p in (1, 2, 3, 4)]}, D_eff = {deff(g)}")
    viol = 0
    for _ in range(400):
        D = int(rng.integers(2, 9))
        x = rng.random(D) ** rng.choice([1.0, 1.0, 3.0, 0.3])
        xs = [Fraction(int(v * 10 ** 5), 10 ** 5) for v in x / x.sum()]
        for p in range(2, 7):
            if rho(p, xs) - 1 < comb(p, 2) / deff(xs):
                viol += 1
    for name, got, want, de in part_d():
        if got + 1e-12 < want:
            viol += 1
        print(f"PARTC/D {name}: rho_4-1 = {got:.6f} vs 6/D_eff = {want:.6f}, "
              f"D_eff = {de:.1f}")
    assert viol == 0, viol
    print(f"PARTC obstruction bound rho_p-1 >= C(p,2)/D_eff, 400 random profiles "
          f"p=2..6 plus uniform and fuzzy-proxy classes: violations {viol}")
    dev, ratios, exact = part_c(rng)
    assert dev < 1e-9, dev
    assert abs(ratios[0] - float(exact[0])) < 1e-9 and abs(ratios[1] - float(exact[1])) < 1e-9
    print(f"PARTD full 6x6 charge spectrum at (q1,q2)=(2,1), (n1,n2)=(1/4,2/9): "
          f"spectrum max dev {dev:.3e}; moment ratios {ratios[0]:.12f} vs 26/17 "
          f"= {float(Fraction(26,17)):.12f} and {ratios[1]:.12f} vs 226/145 = "
          f"{float(Fraction(226,145)):.12f} (excesses 9/17, 81/145)")
    print("PASS s2")


if __name__ == '__main__':
    main()
