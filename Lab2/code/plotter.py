# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sc

"""
EXPERIMENTAL PART
Data from semester-page (not very good)
"""
plt.figure()
T = [1/(87.07+273.15), 1/(91.2+273.15)]
P = [np.log(62.07), np.log(73.0)]
lin = sc.linregress(T,P)
x = np.linspace(20,100, 1000)
def fit(x):
    return lin[0]*x + lin[1]
test = np.array(T)
cons = test*-lin[0]
plt.plot(x, fit(x))
plt.xlabel(r'$\frac{1}{T}$', size=16)
plt.ylabel(r'$\ln{P}$')
plt.title('Plot using real data')
plt.show()
"""
Alternative data found on engineeringtoolbox
"""
plt.figure()
T = [1/(60+273.15), 1/(70+273.15), 1/(80+273.15), 1/(90+273.15), 1/(96+273.15)]
P = [np.log(19.95), np.log(31.2), np.log(47.41), np.log(70.18), np.log(87.77)]
lin = sc.linregress(T,P)
x = np.linspace(20,100, 1000)
def fit(x):
    return lin[0]*x + lin[1]
test = np.array(T)
cons2 = test*-lin[0]
plt.plot(x, fit(x))
plt.xlabel(r'$\frac{1}{T}$', size=16)
plt.ylabel(r'$\ln{P}$')
plt.title('Plot using data provided by Engineering Toolbox')
plt.show()


"""
ANALYTICAL PART
"""
V = np.linspace(0.5,3,  2000)
T = [0.9, 0.95, 1, 1.05, 1.1]
def P(V,T):
    return 8/3*T/(V-1/3)-3/(V**2)
def G(V,T):
    return -(8/3)*T*np.log(3*V-1) -3/V + P(V,T)*V
plt.figure()
lst = []
for i in T:
    lst.append(P(V,i))
j = 0
for i in lst:
    plt.plot(V, i[:], label='T = %g' %(T[j]))
    j += 1
plt.xlabel(r'$\frac{V}{V_C}$')
plt.ylabel(r'$\frac{P}{P_C}$')
plt.title(r'$P_R(V_R)$')
plt.legend()
plt.show()

plt.figure()
lst2 = []
for i in T:
    lst2.append(G(V,i))   
j = 0
for i in lst2:
    plt.plot(V, i[:], label='T = %g' %(T[j]))
    j += 1
plt.xlabel(r'$\frac{V}{V_C}$')
plt.ylabel(r'$\frac{G}{G_C}$')
plt.title(r'$G_R(V_R)$')
plt.legend()
plt.show()

plt.figure()

for i in range(len(T)):
    plt.plot(lst[i], lst2[i], label='T = %g' %(T[i]))
    
plt.xlabel(r'$\frac{P}{P_C}$')
plt.ylabel(r'$\frac{G}{G_C}$')
plt.title(r'$G_R(P_R)$')
plt.legend()
plt.show()

plt.figure()

T2 = np.linspace(0.9,0.95,5)
    
for i in T2:
    plt.plot(P(V, i), G(V,i), label='T = %g' %(i))
plt.xlabel(r'$\frac{P}{P_C}$')
plt.ylabel(r'$\frac{G}{G_C}$')
plt.title('Plot used to best fit a line through the points where the plot intersects itself')
plt.legend()
plt.show()


plt.figure()
Pco = [0.647, 0.686, 0.727, 0.769, 0.812]
Gco = [-4.077, -4.046, -0.417, -3.988, -3.959]

lin = sc.linregress(Pco, Gco)
def fit2(x):
    return lin[0]*x + lin[1]
    
x = np.linspace(0.3,1,10)
plt.plot(x, fit2(x))
plt.xlabel(r'$Temperature [T_B]$')
plt.ylabel('Pressure')
plt.title('A linear fit for the liquid-gas coexistence line')
plt.legend(['a = %.3f \nb = %.3f' %(lin[0],lin[1])])
plt.grid()
plt.show()
Hv = lin[0]


V = np.linspace(0.5,3,  2000)
T = [0.9, 0.95, 1, 1.05, 1.1]
Pc = 22.064e6
Tc = 647.096
Pr = P(V,Tc)/Pc
plt.figure()
plt.plot(V, Pr)
plt.xlabel('Volume [V]')
plt.ylabel(r'$P_R$')
plt.title('A van der Fluid mapped onto water')
plt.show()