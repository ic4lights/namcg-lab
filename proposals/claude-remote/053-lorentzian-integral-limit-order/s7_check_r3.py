#!/usr/bin/env python3
"""S7 check: with A_mu = e^{i pi/8} At_mu for mu = 1..d+1 and A_0 = -i A_{d+1}, one gets A_0 = e^{-3 i pi/8} At_{d+1},
which is R_1 with At_{d+1} the At_0 of the insert; read at mu = 0 the unrestricted display would instead give A_0 = e^{i pi/8} At_0,
off from R_1 by a factor i.  Also R_1 spatial phase e^{i pi u/8} at u = 1 equals e^{i pi/8}."""
import sympy as sp
u = sp.Integer(1)
r1_time = sp.exp(-3*sp.pi*sp.I*u/8); r1_space = sp.exp(sp.pi*sp.I*u/8)
cnt_time = -sp.I*sp.exp(sp.pi*sp.I/8)
print("A_0 = -i A_{d+1}, A_{d+1}=e^{i pi/8} At:  -i e^{i pi/8} - e^{-3 i pi/8} =", sp.simplify(sp.expand_complex(cnt_time - r1_time)))
print("spatial: e^{i pi/8} - R_1 phase =", sp.simplify(r1_space - sp.exp(sp.pi*sp.I/8)))
print("unrestricted mu=0 reading / R_1 time phase =", sp.simplify(sp.expand_complex(sp.exp(sp.pi*sp.I/8)/r1_time)))
