# Round-2 check (finding 7): exact unit-circle crossing values Upsilon_*(delta).
# Zero of F(x)=1-(x/U)(ln(1/x)+d) on |x|=1, x=e^{i th}, th in [0,pi]:
#   U = (d - i th) e^{i th}  =>  d sin th - th cos th = 0,  U = d cos th + th sin th.
# For d>=1 only th=0 (U=d). Cross-check: zero count in slit unit disc just above/below U_*
# via principal-sheet Lambert zeros x = -U / W_j(-U e^{-d}), j in {0,-1}.
import mpmath as mp
mp.mp.dps = 30

def ustar(d):
    d = mp.mpf(d)
    if d >= 1:
        return d, mp.mpf(0)
    if d == 0:
        return mp.pi/2, mp.pi/2
    g = lambda t: d*mp.sin(t) - t*mp.cos(t)
    lo, hi = (mp.mpf('1e-12'), mp.pi/2) if d > 0 else (mp.pi/2, mp.pi - mp.mpf('1e-12'))
    th = mp.findroot(g, (lo, hi), solver='bisect')
    return d*mp.cos(th) + th*mp.sin(th), th

def zeros_in_disc(U, d):
    n = 0
    for j in (0, -1):
        w = mp.lambertw(-U*mp.e**(-d), j)
        x = -U/w
        if abs(mp.im(mp.log(x)) ) <= mp.pi and abs(1 - (x/U)*(mp.log(1/x)+d)) < mp.mpf('1e-15'):
            if abs(x) < 1:
                n += 1
    return n

for d in ['-10', '-9.58458', '-6', '-4', '-2', '-1', '0', '0.5', '0.9', '1', '2', '5']:
    U, th = ustar(d)
    eps = mp.mpf('1e-3')
    print(f"delta={d:>9}  U*={mp.nstr(U,8):>12}  theta={mp.nstr(th,6):>9}  "
          f"zeros(U*-eps)={zeros_in_disc(U-eps, mp.mpf(d))}  zeros(U*+eps)={zeros_in_disc(U+eps, mp.mpf(d))}")

# Upsilon=10 lower window edge: U_*(d)=10 for d<0
d10 = mp.findroot(lambda d: ustar(d)[0]-10, -9.5)
print("Upsilon=10 lower edge delta =", mp.nstr(d10, 8))
