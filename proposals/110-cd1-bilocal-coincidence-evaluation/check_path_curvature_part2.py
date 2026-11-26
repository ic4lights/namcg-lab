# --- L path: seg1 along x1, seg2 along x2; composition left-multiplies
s = sp.symbols('s')
V_s1 = transport1(a*C1, {1: (a*a) * B11})
seg1 = sp.eye(3) + eps*V_s1[1] + eps**2*V_s1[2] + eps**3*V_s1[3]
P1_seg2 = {0: (a*b) * B21, 1: (b*b) * B22}
V_s2 = transport1(b*C2, P1_seg2)
seg2 = sp.eye(3) + eps*V_s2[1] + eps**2*V_s2[2] + eps**3*V_s2[3]
U_L = sp.simplify(seg2 * seg1)

def eps_coeffs(mat, ks):
    # returns list [coeff(eps,k) matrix for k in ks]; Dc[i] <-> ks[i]
    return [sp.simplify(mat.applyfunc(lambda x, k=k: sp.expand(x).coeff(eps, k)))
            for k in ks]

D = U_L - U_line
Dc = eps_coeffs(D, [1, 2, 3])          # Dc[0]=O(eps), Dc[1]=O(eps^2), Dc[2]=O(eps^3)
ck("P2 no order-eps path difference", Dc[0] == sp.zeros(3))

Farea = (B21 - B12) - (C1*C2 - C2*C1)   # (d1 w2 - d2 w1) - [w1,w2] at 0
ck("P2 eps^2 loop coeff = (ab/2)*((d1 w2 - d2 w1) - [w1,w2])",
   sp.simplify(Dc[1] - sp.Rational(1,2)*a*b*Farea) == sp.zeros(3))

# P2b: parabolic path x = eps a s, y = eps b s^2 must agree at eps^2.
def transport1s(P0_of_s, P1_of_s, nord=4):
    Vs = [{0: sp.eye(3)}]
    V1 = [None] + [sp.zeros(3) for _ in range(nord)]
    for e in range(1, nord):
        rhs = {}
        for sp1, M1 in Vs[e-1].items():
            for sp2, M2 in P0_of_s.items():
                rhs[sp1+sp2] = rhs.get(sp1+sp2, sp.zeros(3)) + M2 * M1
        if e-2 >= 0:
            for sp1, M1 in Vs[e-2].items():
                for sp2, M2 in P1_of_s.items():
                    rhs[sp1+sp2] = rhs.get(sp1+sp2, sp.zeros(3)) + M2 * M1
        Ve_s = {}
        Ve1 = sp.zeros(3)
        for sd, M in rhs.items():
            Ve_s[sd+1] = M / sp.Integer(sd+1)
            Ve1 = Ve1 + M / sp.Integer(sd+1)
        Vs.append(Ve_s)
        V1[e] = Ve1
    return V1

P0_p = {0: a*C1, 1: (2*b)*C2}
P1_p = {1: (a*a)*B11, 2: (a*b)*(B12 + 2*B21), 3: (2*b*b)*B22}
Vp = transport1s(P0_p, P1_p)
U_p = sp.eye(3) + eps*Vp[1] + eps**2*Vp[2]
Dp = U_p - U_line
Dpc = eps_coeffs(Dp, [1, 2])           # Dpc[0]=O(eps), Dpc[1]=O(eps^2)
ck("P2b parabolic path: no eps-order difference", Dpc[0] == sp.zeros(3))
ck("P2b parabolic eps^2 coeff = (ab/6)*loop form (area between parabola and chord)",
   sp.simplify(Dpc[1] - sp.Rational(1,6)*a*b*Farea) == sp.zeros(3))
