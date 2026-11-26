import numpy as np, sys
sys.dont_write_bytecode = True
from engine_d import second_order_gen
from toy2d_direct import local_density
B, kappa, t = 1e-4, 0.5, 0.35
alpha = np.array([0.0, 1.0])
eta=np.eye(2); F=np.array([[0,B],[-B,0.]]); Theta=B/(4*np.pi*np.sinh(t*B))
T=second_order_gen(F,eta,np.array([kappa,0.]),alpha,np.array([0.,0.]),1.0,-1j*t,nquad=40)
print("engine", (Theta*T).real, "Maxwell a2 expectation", -t*alpha[1]**2*kappa**2/(48*np.pi))
ks=np.linspace(-6,6,25); dk=ks[1]-ks[0]; tot=0
for phi0 in 2*np.pi*(np.arange(3)+.5)/3:
  for k2 in ks:
    f=lambda e: local_density(1e-9,kappa,alpha,0.0,1.0,t,e,phi0,k2,N=240,L=6.0)
    d=0.05
    tot+=(f(d)-2*f(0)+f(-d))/(2*d*d)/(2*np.pi)*dk/3
print("direct", tot)
