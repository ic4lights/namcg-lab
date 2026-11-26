"""s3: the bosonic mass-insertion density int d^4k (K(k) - i eps)^{-1}, K = k.k with a Lorentzian
quadratic form of signature (-,+,+,+), over an ellipsoidal momentum region {(k0/a)^2+|k|^2 <= L^2}
(a positive definite cutoff form; a=1 the ball), compared with the Euclidean form K=k_E^2 on the
same region, and with the Wick-rotated (Lorentz-invariant analytic) value, whose real part is 0.
Closed forms derived in the proposal:
  Re (Lorentzian) = 2 pi^2 L^2 a/(1+a^2),  Im = 2 pi^2 L^2 a^2/(1+a^2),  Euclidean = 2 pi^2 L^2 a/(1+a).
Numerics: angular integrals by quadrature, PV by symmetric excision around the light cone, and
Im via -i eps at finite eps extrapolated."""
import numpy as np
from scipy.integrate import quad
L=1.0
def lor_re(a,delta=1e-7):
    f=lambda x: np.sin(x)**2/(np.sin(x)**2-a*a*np.cos(x)**2)
    x1=np.arctan(a); x2=np.pi-x1
    pts=[0,x1-delta,x1+delta,x2-delta,x2+delta,np.pi]
    s=0
    for lo,hi in zip(pts[0::2],pts[1::2]): s+=quad(f,lo,hi,limit=400)[0]
    return (L**2/2)*4*np.pi*a*s
def lor_im(a,eps=1e-4):
    f=lambda x: np.sin(x)**2*eps/((np.sin(x)**2-a*a*np.cos(x)**2)**2+eps**2)
    x1=np.arctan(a); x2=np.pi-x1
    s=quad(f,0,np.pi,points=[x1,x2],limit=2000)[0]
    return (L**2/2)*4*np.pi*a*s
def euc(a):
    f=lambda x: np.sin(x)**2/(np.sin(x)**2+a*a*np.cos(x)**2)
    return (L**2/2)*4*np.pi*a*quad(f,0,np.pi)[0]
print(" a     Re_L(num)   Re_L(closed)  Im_L(num)  Im_L(closed)  Eucl(num)  Eucl(closed)  Re_L/Eucl  (1+a)/(1+a^2)")
for a in (0.25,np.sqrt(2)-1,0.7,1.0,1.5,3.0):
    rl=lor_re(a); il=lor_im(a); e=euc(a)
    print(f"{a:5.3f} {rl:11.6f} {2*np.pi**2*a/(1+a*a):11.6f} {il:11.6f} {2*np.pi**2*a*a/(1+a*a):11.6f} {e:11.6f} {2*np.pi**2*a/(1+a):11.6f} {rl/e:9.6f} {(1+a)/(1+a*a):9.6f}")
print("max of (1+a)/(1+a^2) at a=sqrt2-1:",(1+np.sqrt(2)-1)/(1+(np.sqrt(2)-1)**2),"=(1+sqrt2)/2 =",(1+np.sqrt(2))/2)
print("Wick-rotated value: i * pi^2 L^2 (ball in the rotated variable), real part 0")
