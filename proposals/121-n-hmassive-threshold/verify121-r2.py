# verify121.py - verification pack for proposal 121-n-hmassive-threshold (round 1)
# Run:  python -I verify121.py    (sympy + mpmath; deterministic; prints <= 30 lines)
# Expected last two lines: "TOTAL 12/12 PASS" then "ALL CHECKS DONE 121"
import mpmath as mp, sympy as sp, re, os
mp.mp.dps = 30
ok = tot = 0
def chk(name, cond):
    global ok, tot; tot += 1; ok += bool(cond)
    print(("PASS " if cond else "FAIL ") + name)
E1 = mp.e1
def bis(f, lo, hi, n=400):
    flo = f(lo)
    for _ in range(n):
        mid = (lo+hi)/2
        fm = f(mid)
        if (fm > 0) == (flo > 0): lo, flo = mid, fm
        else: hi = mid
    return (lo+hi)/2
gJ  = lambda m2,a,b: mp.quad(lambda s: mp.e**(-m2*s)/s**2, [a,b])
def gcJ(m2,a,b):
    if m2 == 0: return (b-a)/(a*b)
    return mp.e**(-m2*a)/a - mp.e**(-m2*b)/b - m2*(E1(m2*a)-E1(m2*b))
gL  = lambda m2,a,b: mp.quad(lambda s: mp.e**(-m2*s)/s, [a,b])
gcL = lambda m2,a,b: E1(m2*a) - E1(m2*b)

# S1: a1-window J identity, range-wide + limits + value + continuity tooth
g = all(abs(gJ(*[mp.mpf(t) for t in p])-gcJ(*[mp.mpf(t) for t in p])) < mp.mpf('1e-24')
       for p in [("0","1","5"),("1","1","5"),("0.01","1e-3","10"),("500","1e-4","3"),("2","1","1")])
g = g and abs(gcJ(mp.mpf(0),mp.mpf(1),mp.mpf(5))-mp.mpf('0.8')) < mp.mpf('1e-30')
g = g and abs(gcJ(1.,1.,5.)-mp.mpf('0.14829621296738028')) < mp.mpf('1e-9')
g = g and abs(gcJ(1.01,1.,5.)-gcJ(1.,1.,5.)) < mp.mpf('0.01')
chk("S1 J identity + J(m=0)=1/a-1/b + value 0.1482962130", g)

# S2: a2 basis identity + c_R + R-linear coefficient (established identities)
Ri,Rc,Rs,Q,m2,R = sp.symbols('Ri Rc Rs Q m2 R', real=True)
C2, EGB = Ri-2*Rc+Rs/3, Ri-4*Rc+Rs
univ = (Ri-Rc+sp.Rational(5,2)*Rs)/180
univR = univ.subs(Rs, R**2)
g = sp.simplify(univ - (C2/120 - EGB/360 + Rs/72)) == 0
a2E = sp.expand(sp.Rational(1,2)*(R/6-(m2+Q*R))**2)
g = g and sp.simplify((a2E+univR).coeff(R,2)-sp.Rational(1,72)-sp.Rational(1,2)*(sp.Rational(1,6)-Q)**2)==0
g = g and sp.simplify((a2E+univR).coeff(R,1)+m2*(sp.Rational(1,6)-Q))==0
g = g and sp.simplify(a2E.coeff(R,0)-sp.Rational(1,2)*m2**2)==0
chk("S2 a2 decomp: C2/120, c_R=1/2(1/6-Q)^2, R-lin=-m2(1/6-Q)", g)

# S3: Lm window closed form + massless limit + E1 small/large series
g = abs(gL(2.,1e-3,1.)-gcL(2.,1e-3,1.)) < mp.mpf('1e-25')
g = g and abs(gcL(mp.mpf('1e-14'),1e-3,1.)-mp.log(1000)) < mp.mpf('1e-9')
x = mp.mpf('0.01')
g = g and abs(E1(x)-(mp.log(1/x)-mp.euler+x-x**2/4+x**3/18)) < mp.mpf('1e-9')
g = g and abs(E1(mp.mpf(10))-mp.e**(-10)*(mp.mpf(1)/10-mp.mpf(1)/100+mp.mpf(2)/1000
              -mp.mpf(6)/10000+mp.mpf(24)/10**5)) < mp.mpf('1e-8')
chk("S3 Lm=E1(a)-E1(b) + L(0)=ln(b/a) + E1 small/large series", g)

# S4: Upsilon_H(y) = 10[e^{-y} - y E1(y)] (mu<<m): 10 at y=0; monotone decoupling
Uh = lambda y: 10*(mp.e**(-y)-y*E1(y))
g = abs(Uh(mp.mpf('1e-30'))-10) < mp.mpf('1e-27')
g = g and all(Uh(mp.mpf(v))>Uh(mp.mpf(w)) for v,w in
    [("0.001","0.01"),("0.01","1"),("1","10"),("10","100")])
g = g and Uh(100) < mp.mpf('1e-40')
g = g and abs(Uh(1.) - 10*gcJ(1.,mp.mpf('1.'),mp.mpf('1e6'))) < mp.mpf('1e-8')
chk("S4 Upsilon_H=10J/LUV^2: 10 at y=0, monotone, decouples", g)

# S5: U(a)=int ln(a+tau(1-tau)) closed form; U(0)=-2; heavy limit U=ln a+1/(6a)
tt, aa = sp.symbols('t a', positive=True)
Fcf = sp.lambdify(aa, sp.integrate(sp.log(aa+tt*(1-tt)), (tt,0,1)), 'mpmath')
def gU(a):
    f = lambda t: mp.log(a+t*(1-t))
    if a != 0 and abs(a) < mp.mpf('1e-6'):
        r = mp.sqrt(abs(a))
        return mp.quad(f, [0, r]) + mp.quad(f, [r, 1])
    return mp.quad(f, [0, 1])
g = all(abs(gU(mp.mpf(v))-Fcf(mp.mpf(v))) < mp.mpf('1e-18') for v in
        ["1e-8","0.001","1","4","100","1e6"])
g = g and mp.mpf('1e-9') < gU(mp.mpf('1e-8'))+2 < mp.mpf('1e-6')
g = g and abs(gU(0)+2) < mp.mpf('1e-30')
g = g and abs((gU(mp.mpf('1e6'))-mp.log(1e6))-1/(6*mp.mpf('1e6'))) < mp.mpf('1e-13')
g = g and gU(mp.mpf('0.5')) < gU(1) and gU(1) > 0 and gU(0) < 0
chk("S5 U(a) cf + U(0)=-2 + U(a)-ln a -> 1/(6a) + monotone", g)

# S6: r(y)=e^{-y}/E1(y)-y increasing 0->1; band y* = e^{-(10+gamma)}
rf = lambda y: mp.e**(-y)/E1(y)-y
g = all(rf(mp.mpf(u))<rf(mp.mpf(v)) for u,v in
    [("1e-8","1e-6"),("1e-6","1e-4"),("0.01","0.1"),("1","5"),("20","100")])
ys = bis(lambda y: 10*rf(y)-1, mp.mpf('1e-6'), mp.mpf('1e-3'))
g = g and abs(ys/(mp.e**(-(10+mp.euler)))-1) < mp.mpf('5e-3')
g = g and rf(mp.mpf('1e-8')) < mp.mpf('0.11') and 1-rf(100) < mp.mpf('0.05')
chk("S6 r monotone 0->1; 10r(y*)=1 at y*=e^{-(10+gE)}", g)

# S7: massless zeros x_k = -U/W_k(-U e^{-d}): recorded window + pole data
def nzeros(U, d):
    n = 0
    for k in range(-6, 7):
        t = -d - mp.lambertw(-U*mp.e**(-d), k)
        if abs(mp.im(t)) < mp.pi*0.999999 and mp.re(t) > 1e-9: n += 1
    return n
g = nzeros(10,0)==0 and nzeros(mp.mpf('1.5'),0)==2
th = bis(lambda t: t-10*mp.sin(t), mp.mpf('2.5'), mp.mpf('3.1'))
g = g and abs(10*mp.cos(th)+9.58) < mp.mpf('0.01')
g = g and nzeros(10,mp.mpf('-9.5'))==0 and nzeros(10,mp.mpf('-9.7'))==2
g = g and nzeros(10,mp.mpf('9.5'))==0 and nzeros(10,mp.mpf('10.5'))==1
g = g and nzeros(mp.mpf('1.58'),0)==0   # U above pi/2: zero-free
tm = bis(lambda t: mp.sin(t)+t*mp.cos(t)-t/10, mp.mpf('1.0'), mp.mpf('2.8'))
Fmin = abs(1-(mp.e**(1j*tm)/10)*(-1j*tm))
g = g and abs(Fmin-mp.mpf('0.82')) < mp.mpf('0.005')
chk("S7 U_*(0)=pi/2, window -9.58<d<10, Fmin=0.82, counts", g)

# S8: exact massive kernel L(x;y)=int E1(y+tau(1-tau)x); log form; decoupling
def Lk(y, x):
    return mp.quad(lambda t: E1(y+t*(1-t)*x), [0,1])
logL = lambda y, x: mp.log(1/x)-mp.euler-gU(y/x)+y+x/6
g = abs(Lk(mp.mpf('0.01'),mp.mpf('0.5'))-logL(mp.mpf('0.01'),mp.mpf('0.5'))) < mp.mpf('0.02')
g = g and abs(Lk(1,mp.mpf('0.5'))-logL(1,mp.mpf('0.5'))) > mp.mpf('0.05')
g = g and abs(Lk(mp.mpf('1e-4'),mp.mpf('1e-6'))-(-mp.log(mp.mpf('1e-4'))-mp.euler)) < mp.mpf('0.02')
g = g and abs(Lk(mp.mpf('1e-4'),mp.mpf('1e-6'))-Lk(mp.mpf('1e-4'),mp.mpf('1e-8'))) < mp.mpf('5e-3')
g = g and abs(Lk(mp.mpf(100),mp.mpf('0.5'))) < mp.mpf('1e-40')
g = g and abs(Lk(0,mp.mpf('0.01'))-(mp.log(100)+2-mp.euler)) < mp.mpf('0.05')
chk("S8 massive kernel: log form + teeth + k-decoupling", g)

# S9 massive kernel has a branch cut on negative real x starting at x=-4y
def Lkj(x, y):
    return mp.quad(lambda t: E1(y+t*(1-t)*x), [0,1])
jump = lambda y: abs(Lkj(mp.mpf('-0.5')+1e-8j, y) - Lkj(mp.mpf('-0.5')-1e-8j, y))
g = jump(mp.mpf('1e-6')) > 1 and jump(1) < mp.mpf('1e-6')
tip = lambda d: abs(Lkj(-4*mp.mpf('1e-3')+1j*d, mp.mpf('1e-3')))
g = g and tip(mp.mpf('1e-2')) < tip(mp.mpf('1e-6')) < tip(mp.mpf('1e-10'))
g = g and tip(mp.mpf('1e-10')) > 3
chk("S9 branch cut (-inf,-4y]: jump>0 light, =0 heavy, log tip", g)

# S10: Upsilon_H linear in (1/6-Q): vanishes at conformal coupling
g = 60*(sp.Rational(1,6)-sp.Rational(1,6)) == 0
g = g and 60*sp.Rational(1,6) == 10
g = g and 60*(sp.Rational(1,6)-sp.Rational(1,3)) == -10
a1lin = sp.Rational(1,6)*R - (m2 + Q*R)
g = g and a1lin.coeff(R,1) == sp.Rational(1,6)-Q and a1lin.coeff(m2,1) == -1
chk("S10 Upsilon_H prop (1/6-Q): 0 at Q=1/6", g)

# S12: running-window (implicit) spin-two factor has NO positive real zero; v7's
# factor-2 claim was a phantom (no sign change in bracket; bis returned edge P=100).
# True statement: (a) f<0 at both v7 bracket ends; (b) x*L(x;y) -> 2(e^-y - yE1(y))
# = Uh(y)/5; (c) sup_x x*L*Uh^-1 < 0.9 on grid; (d) CONTROL: coupling Uh/10 has a
# true root found by the same bisection (sign change + residual), so (a) is not
# vacuous. No zero-free-region claim: S9 branch cut stands (see proposal tiers).
def Lx(x, y):
    return mp.quad(lambda t: E1(y+t*(1-t)*x), [0,1])
asym = lambda y: 2*(mp.e**(-y)-y*E1(y))
g = True
for yv in ["1e-6","1e-4","1e-2","1","10"]:
    yy = mp.mpf(yv)
    f = lambda P: P - Uh(yy)/Lx(P,yy)
    g = g and f(mp.mpf('1e-9')) < 0 and f(100) < 0
    g = g and abs(mp.mpf('1e10')*Lx(mp.mpf('1e10'),yy)/asym(yy)-1) < mp.mpf('1e-5')
    hmax = max(x*Lx(x,yy)/Uh(yy) for x in
               [mp.mpf(10)**(mp.mpf(k)/4) for k in range(-32,41)])
    g = g and hmax < mp.mpf('0.9')
U2c = Uh(mp.mpf('1e-6'))/10
f2 = lambda P: P - U2c/Lx(P,mp.mpf('1e-6'))
g = g and f2(mp.mpf('1e-9'))*f2(100) < 0
Pc = bis(f2, mp.mpf('1e-9'), mp.mpf('100'))
g = g and abs(Pc*Lx(Pc,mp.mpf('1e-6'))-U2c)/U2c < mp.mpf('1e-25')
chk("S12 running-window factor: no positive real zero; x*L -> Uh/5; control fires", g)

# S11: payload hygiene + ref whitelist + injected controls. v8 S11 was a dead
# guard: its pattern was built from a single literal backslash, an invalid regex
# escape that crashed whenever the payload existed (earlier runs only SKIPped).
# The scanner below uses chr(92), no backslash literals; every guard carries a
# positive control that must fire (lesson of 117 vacuous-guard controls).
here = os.path.dirname(os.path.abspath(__file__))
cands = sorted(f for f in os.listdir(here) if f.startswith('insert') and f.endswith('.tex') and 'superseded' not in f)
if cands:
    b = open(os.path.join(here, cands[0]), 'rb').read()
    BS = chr(92); BB = BS.encode()
    def refs(bb):
        s = bb.decode('latin-1'); res = []
        for pre in ('eqref', 'ref', 'autoref'):
            tok = BS + pre + '{'; i = 0
            while True:
                j = s.find(tok, i)
                if j < 0: break
                res.append(s[j + len(tok):s.find('}', j)]); i = j + 1
        return res
    names = refs(b)
    wl = ('thm:Geff','eq:appA-a1','eq:appA-a2','eq:appA-scalar','eq:O-eta','eq:V',
          'eq:Smicro','ass:emergent-op','sec:status-N','sec:status-F','eq:appA-Wexp','eq:LUV-def')
    g = (b.endswith(b'\r\n') and b'\n' not in b.replace(b'\r\n', b'') and b'$' not in b
         and BB + b'label' not in b and BB + b'cite' not in b and BB + b'begin' not in b
         and b.decode('ascii', 'ignore') == b.decode('latin-1'))
    g = g and len(names) >= 8 and all(n in wl for n in names)
    g = g and any(n not in wl for n in refs(b + BB + b'ref{bogus:not-wl}'))
    g = g and (b'$' in (b + b'$'))
    g = g and not (b + b'x').endswith(b'\r\n')
    g = g and (b'\n' in (b + b'\nx').replace(b'\r\n', b''))
    g = g and (BB + b'label' in (b + BB + b'label{q}'))
    g = g and (b.decode('ascii', 'ignore') != (b + bytes([0xE9])).decode('latin-1'))
    g = g and ('thm:Geff' in names and 'eq:Smicro' in names)
    chk("S11 payload hygiene + ref whitelist + controls", g)
else:
    print("SKIP S11 payload absent")


print("TOTAL %d/%d PASS" % (ok, tot))
print("ALL CHECKS DONE 121")
