# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
N = 400
q = 200
Ndot = 3*N
kB = 1.381e-23
h = 6.626e-34
f = 1420.4e6
eps = h*f
def S(q,Ndot):
    return ((q+Ndot)*np.log(q+Ndot) - Ndot*np.log(Ndot) - q*np.log(q))*kB
T = np.linspace(0.1,400,5000)
def CV(N,T):
    return 3*N*kB*(eps/(kB*T))**2 * (np.exp(eps/(kB*T))/((np.exp(eps/(kB*T))-1)**2))
plt.plot(T[650:],CV(N,T)[650:])
plt.xlabel('Temperature [K]')
plt.ylabel('Heat Capacity [J/K]')
plt.title('Heat capacity per temperature', y=1.08)
plt.plot(T[650:], S)
plt.show()