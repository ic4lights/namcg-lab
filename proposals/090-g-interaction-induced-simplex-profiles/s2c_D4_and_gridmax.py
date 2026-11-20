import mpmath as mp
mp.mp.dps = 30
def grads(p, a, b):
    D = len(p)
    return [(a-1)/p[i] + sum(b/(p[i]-p[j]) for j in range(D) if j != i) for i in range(D)]
def f3(x, y, z):
    p = [mp.mpf(x), mp.mpf(y), mp.mpf(z), 1-mp.mpf(x)-mp.mpf(y)-mp.mpf(z)]
    g = grads(p, 2, mp.mpf('1'))
    return (g[0]-g[3], g[1]-g[3], g[2]-g[3])
r = mp.findroot(f3, (mp.mpf('0.45'), mp.mpf('0.3'), mp.mpf('0.2')), tol=1e-24, maxsteps=400)
p = [mp.mpf(r[0]), mp.mpf(r[1]), mp.mpf(r[2]), 1-mp.mpf(r[0])-mp.mpf(r[1])-mp.mpf(r[2])]
g = grads(p, 2, mp.mpf('1'))
eul = sum(p[i]*g[i] for i in range(4)) - (4 + 6)
print('D4 a=2 beta=1 p*=', [mp.nstr(x, 12) for x in p])
print('D4 resid=', mp.nstr(max(abs(g[0]-g[1]), abs(g[1]-g[2]), abs(g[2]-g[3])), 3), 'euler_mismatch=', mp.nstr(eul, 3))
def kern3(p, a, b):
    v = mp.mpf('1')
    for x in p:
        v *= x**(a-1)
    for i in range(3):
        for j in range(i+1, 3):
            v *= abs(p[i]-p[j])**b
    return v
N = 241
best = (mp.mpf('0'), None)
for ii in range(1, N):
    x1 = mp.mpf(ii)/N
    for jj in range(1, N-ii):
        x2 = mp.mpf(jj)/N
        x3 = 1-x1-x2
        if not (x1 > x2 > x3 > 0):
            continue
        v = kern3([x1, x2, x3], 2, 1)
        if v > best[0]:
            best = (v, (x1, x2, x3))
ps = solve = None
def f2(x, y):
    p = [mp.mpf(x), mp.mpf(y), 1-mp.mpf(x)-mp.mpf(y)]
    g = grads(p, 2, mp.mpf('1'))
    return (g[0]-g[2], g[1]-g[2])
rr = mp.findroot(f2, (mp.mpf('0.65'), mp.mpf('0.27')), tol=1e-24)
qs = [mp.mpf(rr[0]), mp.mpf(rr[1]), 1-mp.mpf(rr[0])-mp.mpf(rr[1])]
d = max(abs(best[1][0]-qs[0]), abs(best[1][1]-qs[1]), abs(best[1][2]-qs[2]))
print('D3_grid_argmax=', [mp.nstr(x, 6) for x in best[1]], 'dist_to_stationary=', mp.nstr(d, 3), 'grid_h=', mp.nstr(1/mp.mpf(N), 3))
print('S2C OK')
