"""086 s1: exact moment-excess values for the 081 fuzzy proxies (L3177 fix).

Profile: g_l = l/2 (exact Fraction) with multiplicity 2l+1, l = 1..l_c
(081 s3_r2 convention; its Fraction(int(f(l)*1000),1000) equals l/2 exactly).
D_eff = (sum g)^2 / sum g^2. Fourth-moment excess = rho_2 - 1 (= 1/D_eff
exactly); eighth-moment excess = rho_4 - 1. Both computed twice: generic
complete-homogeneous recursion (081 hcf) and Newton-identity closed forms.
Run: python -I proposals/086-g-081-momentlabel-correction/s1_moment_values.py
Expected final line: PASS s1_086
"""
from fractions import Fraction


def powersums(lc, kmax):
    s = [Fraction(0)] * (kmax + 1)
    for l in range(1, lc + 1):
        g = Fraction(l, 2)
        for k in range(1, kmax + 1):
            s[k] += (2 * l + 1) * g ** k
    return s


def h_complete(s, m):
    h = [Fraction(1)]
    for m2 in range(1, m + 1):
        h.append(sum(s[t] * h[m2 - t] for t in range(1, m2 + 1)) / m2)
    return h[m]


def analyze(lc):
    s = powersums(lc, 4)
    S1 = s[1]
    deff = S1 * S1 / s[2]
    h2 = h_complete(s, 2)
    h4 = h_complete(s, 4)
    rho2 = 2 * h2 / S1 ** 2
    rho4 = 24 * h4 / S1 ** 4
    # Newton-identity closed forms (independent route)
    rho2c = 1 + s[2] / S1 ** 2
    rho4c = 1 + (6 * S1 ** 2 * s[2] + 3 * s[2] ** 2 + 8 * S1 * s[3] + 6 * s[4]) / S1 ** 4
    assert rho2 == rho2c and rho4 == rho4c, (lc, rho2 - rho2c, rho4 - rho4c)
    assert rho2 - 1 == Fraction(1) / deff, lc  # exact fourth-moment excess = 1/D_eff
    return deff, rho2 - 1, rho4 - 1


d40, x40, y40 = analyze(40)
d160, x160, y160 = analyze(160)
f = lambda v: float(v)
print(f"lc=40:  D_eff = {f(d40):.6f};  1/D_eff = {f(x40):.9e};  6/D_eff = {f(6/d40):.9e};  rho4-1 = {f(y40):.9e}")
print(f"lc=160: D_eff = {f(d160):.6f};  1/D_eff = {f(x160):.9e};  6/D_eff = {f(6/d160):.9e};  rho4-1 = {f(y160):.9e}")
# 2-s.f. rounding targets for the corrected manuscript numerals
assert 0.00067200 < f(x40) < 0.00067210      # -> 6.7e-4
assert 0.000043440 < f(x160) < 0.000043460   # -> 4.3e-5
# the currently quoted numerals are 6/D_eff and rho4-1 (eighth-moment), 2 s.f.
assert 0.0040320 < f(6 / d40) < 0.0040330    # -> 4.0e-3
assert 0.00026060 < f(6 / d160) < 0.00026070 # -> 2.6e-4
assert 0.0040370 < f(y40) < 0.0040380        # -> 4.0e-3
assert 0.00026065 < f(y160) < 0.00026075     # -> 2.6e-4
# D_eff values quoted in the same sentence
assert 1488.002 < f(d40) < 1488.003
assert 23016.89 < f(d160) < 23016.90
print("fourth-moment excesses round to 6.7e-4 (lc=40) and 4.3e-5 (lc=160);")
print("quoted 4.0e-3 / 2.6e-4 match 6/D_eff and the exact eighth-moment excess (mislabel confirmed).")
print("PASS s1_086")
