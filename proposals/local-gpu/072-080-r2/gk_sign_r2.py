import numpy as np
rng=np.random.default_rng(1)
worst=0
for _ in range(50):
    D=7
    u=rng.normal(size=D)+1j*rng.normal(size=D); u/=np.linalg.norm(u)
    w=rng.normal(size=D)+1j*rng.normal(size=D)   # column |w)
    Y=np.outer(u,w.conj())                         # |u)(w|
    Q=-2j*(Y-Y.conj().T)
    ev=np.linalg.eigvalsh(Q); ev=np.sort(ev[np.abs(ev)>1e-9])
    a=np.vdot(u,w); h=a.imag; n=np.vdot(w,w).real-abs(a)**2
    pr=np.sort([-2*h+2*np.sqrt(h*h+n),-2*h-2*np.sqrt(h*h+n)])
    worst=max(worst,np.abs(ev-pr).max())
print('sign convention -2h, h=Im(u|w): max dev',worst)
# direct sum with inter-summand Gaussian momenta, unequal scales: distance from union of full-row pairs
for sc in [(1,1),(1,1.6),(1,3)]:
  for N in (50,200,800):
    devs=[]
    for _ in range(300):
        R=(rng.normal(size=(N,2))+1j*rng.normal(size=(N,2)))*np.array(sc)
        U=np.zeros((N,2),complex);U[0,0]=1;U[N//2,1]=1
        Q=-2j*(U@R.conj().T-R@U.conj().T)
        e=np.linalg.eigvalsh(Q); e=np.sort(e[np.abs(e)>1e-9*np.abs(e).max()])
        C=U.conj().T@R;H=(C-C.conj().T)/2j;K=R.conj().T@R-C.conj().T@C
        un=[]
        for f in range(2):
            h,n=H[f,f].real,K[f,f].real
            un+=[-2*h+2*np.sqrt(h*h+n),-2*h-2*np.sqrt(h*h+n)]
        devs.append(np.abs(e-np.sort(un)).max()/np.abs(e).max())
    print(sc,N,'%.4f'%np.median(devs))
