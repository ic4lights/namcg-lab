"""040 t6: sign of the log term in 034 l3_fin.integrate.  Test function f(s)=c e^{-s}/s on the ray; by the definition Fin = lim[int_{s0}^inf f ds - c ln(1/s0)] one has Fin = -gamma*c."""
import sys, mpmath as mp
sys.dont_write_bytecode = True
import l3_fin as L
c = mp.mpf(1)
f = lambda s: c * mp.exp(-s) / s
v = L.integrate(f, mp.mpf('0.05'), mp.mpf(40), c, nn=8, nint=6)
print('034 integrate():', mp.nstr(v, 12), ' expected -gamma =', mp.nstr(-mp.euler, 12), ' with +c ln(rho1 PH) instead:', mp.nstr(v + 2 * c * mp.log(mp.mpf('0.05') * L.PH), 12))
