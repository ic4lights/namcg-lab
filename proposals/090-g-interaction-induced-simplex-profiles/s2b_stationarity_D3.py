import mpmath as mp
mp.mp.dps = 30
def grads(p, a, b):
    D = len(p)
    return [(a-1)/p[i] + sum(b/(p[i]-p[j]) for j in range(D) if j != i) for i in range(D)]
def solve(a, b, starts):
    for s0 in starts:
        def f(x, y):
            p = [mp.mpf(x), mp.mpf(y), 1-mp.mpf(x)-mp.mpf(y)]
            g = grads(p, a, b)
            return (g[0]-g[2], g[1]-g[2])
        try:
            r = mp.findroot(f, (mp.mpf(s0[0]), mp.mpf(s0[1])), tol=1e-22, maxsteps=400)
        except Exception:
            continue
        p = [mp.mpf(r[0]), mp.mpf(r[1]), 1-mp.mpf(r[0])-mp.mpf(r[1])]
        if p[0] > p[1] > p[2] > 0:
            return p
    return None
S = [['0.52','0.32'],['0.42','0.33'],['0.9','0.08'],['0.75','0.22'],['0.6','0.3']]
for bval in ['0.2','1','5','20']:
    p = solve(2, mp.mpf(bval), S)
    g = grads(p, 2, mp.mpf(bval))
    eul = sum(p[i]*g[i] for i in range(3)) - (3 + 3*mp.mpf(bval))
    print('a=2 beta=%s p*=%s resid=%s euler_mismatch=%s' % (bval, [mp.nstr(x,10) for x in p], mp.nstr(max(abs(g[0]-g[1]),abs(g[1]-g[2])),3), mp.nstr(eul,3)))
prev = None; starts = [['0.42','0.33'],['0.4','0.34'],['0.38','0.35']]
for k in range(2,9):
    bv = mp.mpf(10)**(-k)
    p = solve(2, bv, starts)
    gap = p[1]-p[2]
    if prev:
        print('onset k=%s slope=%s' % (k, mp.nstr(mp.log(gap/prev[0])/mp.log(bv/prev[1]),4)))
    starts = [[mp.nstr(p[0],12), mp.nstr(p[1],12)]]
    prev = (gap, bv)
pv = [mp.mpf('0.4'), mp.mpf('0.35'), mp.mpf('0.25')]
for bval in ['0.0','1']:
    g = grads(pv, 1, mp.mpf(bval))
    print('a=1 beta=%s avg_grad=%s euler_mu=%s mismatch=%s' % (bval, mp.nstr(sum(g)/3,5), mp.nstr(sum(pv[i]*g[i] for i in range(3)),5), mp.nstr(sum(pv[i]*g[i] for i in range(3))-sum(g)/3,5)))
print('S2B OK')
