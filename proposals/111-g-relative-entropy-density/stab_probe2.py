import numpy as np, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as cm
def ratio(L,mu,N):
    sites = np.arange(6,6+N)
    C,Pi = cm.restrict(L,mu,sites); G0 = cm.G_block(C,Pi)
    A = cm.A_of_G(G0)  # returns real sym; use nus margin instead
    nu = cm.nus(G0)
    # recompute imag ratio via raw route
    n=N; O=cm.omega(n)
    wG,U=np.linalg.eigh(0.5*(G0+G0.T))
    sq=U@np.diag(np.sqrt(wG))@U.T; isq=U@np.diag(1/np.sqrt(wG))@U.T
    Kh=-1j*(sq@O@sq); hw,HV=np.linalg.eigh(Kh)
    Kf=HV@np.diag(np.sign(hw)*cm.hvec(np.abs(hw)))@HV.conj().T
    Ar=-1j*((isq@Kf@sq)@O)
    r=np.max(np.abs(Ar.imag))/(1+np.max(np.abs(Ar.real)))
    print("L=%d mu=%.2f N=%d nu_min-0.5=%.3e ratio=%.3e minEigA=%.3e" % (L,mu,N,nu.min()-0.5,r,np.linalg.eigvalsh(A).min()))
for (L,mu,N) in [(49,0.05,12),(41,0.05,12),(31,0.05,8),(49,0.10,16),(61,0.05,20)]:
    try: ratio(L,mu,N)
    except Exception as e: print("L=%d mu=%.2f N=%d ERR %s %s" % (L,mu,N,type(e).__name__,str(e)[:80]))
