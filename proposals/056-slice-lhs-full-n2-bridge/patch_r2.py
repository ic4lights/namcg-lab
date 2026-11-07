# r2 script patches: link_r1.py (m1 label, m2 quad column marked truncation-check,
# exact |1-J/I| column, m3 crossing epsilon*, F2 tube comment) and bridge_r1.py
# (m5 deterministic off-slice contrast with |O_k| > 2). Run: python -I patch_r2.py
import io

link = io.open('link_r1.py', encoding='ascii').read()

oldB = ('print("eps      |I|        |J(lam=2)|   |I-J|/|I| (mp.quad)")\n'
        'for e in (mp.mpf(\'0.05\'), mp.mpf(\'0.02\'), mp.mpf(\'0.01\')):\n'
        '    Iv = abs(2*mp.sqrt(mp.pi/e)*mp.exp(-gcm**2/(4*e)))\n'
        '    Qv = e*(1 + 2*mp.cos(3*mp.pi/8))\n'
        '    Jv = abs(2*mp.sqrt(mp.pi/Qv)*mp.exp(-gcm**2/(4*Qv)))\n'
        '    dif = abs(mp.quad(lambda x: mp.exp(-e*x*x)*(1 - mp.exp(-2*e*mp.cos(3*mp.pi/8)*x*x))*2*mp.cos(gcm*x), [-30, 0, 30]))\n'
        '    print("%6.3f  %s  %s  %s" % (e, mp.nstr(Iv, 8), mp.nstr(Jv, 8), mp.nstr(dif/Iv, 6)))\n'
        'print("model: |I| = sqrt(pi/eps)-scale * exp(cos(pi/8)/(8*eps)) ; cos(pi/8)/8 =", mp.nstr(mp.cos(mp.pi/8)/8, 6))\n')
newB = ('print("eps      |I|        |J(lam=2)|   |1-J/I| exact    |I-J|/|I| quad (TRUNCATION CHECK ONLY, mp.quad unreliable on growing oscillatory tails)")\n'
        'for e in (mp.mpf(\'0.05\'), mp.mpf(\'0.02\'), mp.mpf(\'0.01\')):\n'
        '    Icm = 2*mp.sqrt(mp.pi/e)*mp.exp(-gcm**2/(4*e))\n'
        '    Qv = e*(1 + 2*mp.cos(3*mp.pi/8))\n'
        '    Jcm = 2*mp.sqrt(mp.pi/Qv)*mp.exp(-gcm**2/(4*Qv))\n'
        '    dif = abs(mp.quad(lambda x: mp.exp(-e*x*x)*(1 - mp.exp(-2*e*mp.cos(3*mp.pi/8)*x*x))*2*mp.cos(gcm*x), [-30, 0, 30]))\n'
        '    print("%6.3f  %s  %s  %s  %s (sandwich: |1-J/I| <= %.5f)" % (e, mp.nstr(abs(Icm), 8), mp.nstr(abs(Jcm), 8),\n'
        '          mp.nstr(abs(1 - Jcm/Icm), 6), mp.nstr(dif/abs(Icm), 6), 1 + abs(Jcm/Icm)))\n'
        'print("model: |I| = 2*sqrt(pi/eps)*exp(-Re(gc^2)/(4*eps)), -Re(gc^2)/4 = sqrt(2)/32 =", mp.nstr(mp.sqrt(2)/32, 8))\n')
assert oldB in link
link = link.replace(oldB, newB)

oldC = ('# rank-one corner: A0tilde = rho*H (Tr H^2=1), transverse |Atilde_i| ~ c1*sqrt(eps) so\n'
        '# quartic S_E part and all other exponent pieces are O(1); regulator damping in rho:\n')
newC = ('# rank-one corner: A0tilde = rho*H (Tr H^2=1), transverse |Atilde_i| ~ c1*eps (tube of\n'
        '# scale O(eps): quartic cross penalty kappa*tau^2*rho^2 is O(1) at rho* = O(1/eps); a tube\n'
        '# O(sqrt(eps)) would give penalty Theta(1/eps) and only c0(u)/(1+kappa*sin(pi u/2)/K) (F2).\n'
        '# Regulator damping in rho:\n')
assert oldC in link
link = link.replace(oldC, newC)

oldD = ('print("%6.3f  %s  %s  %s" % (e, mp.nstr(lo, 6), mp.nstr(hi, 6), "NO" if lo > hi else "yes (finite eps only)")\n)')
newD = ('    print("%6.3f  %s  %s  %s" % (e, mp.nstr(lo, 6), mp.nstr(hi, 6), "NO" if lo > hi else "yes (finite eps only)"))\n'
        '# m3: exact asymptotic statement: incompatibility for all sufficiently small eps;\n'
        '# finite-eps crossing (poly=1) solved numerically:\n'
        'g = lambda ee: mp.log(Lstar*ee) + c03/ee\n'
        'loE, hiE = mp.mpf(\'0.001\'), mp.mpf(\'0.05\')\n'
        'for _ in range(80):\n'
        '    mid = (loE + hiE)/2\n'
        '    if g(mid) > 0: hiE = mid\n'
        '    else: loE = mid\n'
        'print("crossing epsilon* (u=0.3, poly=1): lambda_*eps = exp(-c0/eps) at eps* =", mp.nstr((loE+hiE)/2, 6))')
assert oldD in link
link = link.replace(oldD, newD)
io.open('link_r1.py', 'w', encoding='ascii', newline='\n').write(link)

br = io.open('bridge_r1.py', encoding='ascii').read()
old2 = ('# off-slice complex k for contrast: rho_X^2 complex generically, |O_k| can exceed 2 at R_1\n'
        'rnd = random.Random(11)\nk = [mp.mpc(rnd.uniform(-1, 1), rnd.uniform(-1, 1)) for _ in range(4)]\n'
        'w = [sum(k[mu]*a[aa][mu] for mu in range(4)) for aa in range(3)]\n'
        'rho2m = rho2_matrix(w)\n'
        'Om = abs(2*mp.cos(mp.sqrt(rho2m)/2))\n'
        'print("non-slice complex k: im(rho_X^2) =", mp.nstr(mp.im(rho2m), 6), " |O_k| =", mp.nstr(Om, 8), "> 2:", Om > 2)\n')
new2 = ('# m5: deterministic off-slice contrast exhibiting |O_k| > 2 at u=0 fields: k=(0,2i,0,0),\n'
        '# A^1_1 = 2 only: w^1 = 4i, rho_X^2 = -16, rho_X = 4i, |O_k| = 2 cosh(2) = 7.524 > 2.\n'
        'kk = [mp.mpc(0), mp.mpc(0, 2), mp.mpc(0), mp.mpc(0)]\n'
        'aa2 = [[mp.mpc(0)]*4 for _ in range(3)]\n'
        'aa2[0][1] = mp.mpf(2)\n'
        'w2 = [sum(kk[mu]*aa2[aa][mu] for mu in range(4)) for aa in range(3)]\n'
        'rho2b = rho2_matrix(w2)\n'
        'Omb = abs(2*mp.cos(mp.sqrt(rho2b)/2))\n'
        'print("off-slice k=(0,2i,0,0), A^1_1=2: rho_X^2 =", mp.nstr(rho2b, 6), " |O_k| =", mp.nstr(Omb, 8), "> 2:", Omb > 2)\n')
assert old2 in br
br = br.replace(old2, new2)
io.open('bridge_r1.py', 'w', encoding='ascii', newline='\n').write(br)
print("patched link_r1.py and bridge_r1.py OK")
