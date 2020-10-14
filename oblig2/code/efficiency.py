# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

Cp = np.array([1.003,1.005,1.008,1.013,1.020,1.029,1.040,1.051,1.063,1.075,
               1.087,1.099,1.121,1.142,1.155,1.173,1.190,1.204,1.216])
Cv = np.array([0.716,0.718,0.721,0.726,0.733,0.742,0.753,0.764,0.776,0.788,
               0.8,0.812,0.834,0.855,0.868,0.886,0.903,0.917,0.929])
vol1 = [6,9,12]; vol2 = []
for k in vol1:
    vol2.append(k/3)
T = np.array([250,300,350,400,450,500,550,600,650,700,750,800,900,
              1000,1100,1200,1300,1400,1500])
def eff(T1, vol1, vol2, Cv,Cp):
    g = Cp/Cv
    T2 = T1*vol1**(g-1)
    T3 = T2*vol2
    T4 = T3*(vol2/vol1)**(g-1)
    Q1 = Cp*(T3-T2)
    Q2 = Cv*(T4-T1)
    netW = Q1-Q2
    eff = netW/Q1
    return eff
def eff2(T1, vol1, vol2, Cv,Cp):
    g = Cp/Cv
    eff = 1- 1/vol1**(g-1) * ((vol2)**g - 1)/(g*(vol2)-1)
    return eff
p = str(input("General Efficiency or Diesel Efficiency? [G/D] \n"))
p = p.lower()
if p == 'g':
    mode = eff; s = 'General'
elif p == 'd':
    mode = eff2; s = 'Diesel'
else:
    raise ValueError('Not recognized input. Please enter G or D only')
plt.figure(figsize=(8,8))
for i in range(len(vol1)):
    for j in range(len(vol2)):
        plt.plot(T, mode(T,vol1[i],vol2[j],Cv,Cp),
                 label='Factor 1->2: = %i, Factor 2->3: = %i' %(vol1[i],vol2[j]))
plt.title("""Efficiency given initial temperature from 250K through 1500K 
          using the %s efficiency equation""" %(s))
plt.xlabel('Temperature [K]'); plt.ylabel('Efficiency [%]')
plt.legend(fontsize=8)
plt.show()