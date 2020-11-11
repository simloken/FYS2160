# -*- coding: utf-8 -*-
import numpy as np
import scipy.stats as sp
import matplotlib.pyplot as plt
k2 = np.array([285.5, 417.8, 561.4, 682.7, 836.9, 975.6, 1114.8, 1254, 1393.3, 1532.2, 1671.5, 1810.4, 1949.9])
k4 = np.array([314.1, 451.3, 594.0, 738.6, 883.3, 1028.5, 1174.1, 1320.7, 1466.7, 1612.9, 1759.2, 1905.7, 2051.8])
k3 = np.array([311.2, 465.8, 616.9, 769.4, 921.9, 1074.9, 1229.1, 1382.8, 1536.5, 1690.0, 1843.6, 1998.3])
k1Ar = np.array([269.8, 389.2, 524.6, 650.0, 777.8, 904.7, 1033.1, 1161.1, 1292.0, 1420.3, 1548.4, 1667.8, 1806.9, 1935.8])
k1CO2 = np.array([233.8, 336.9, 442.3, 561.1, 670.2, 780.9, 891.7, 1002.4, 1113.4, 1225.4, 1336.4, 1447.6, 1559.0, 1670.7, 1782.3, 1894.7, 2006.2])
k2_mp = np.zeros(len(k2))
k4_mp = np.zeros(len(k4))
k3_mp = np.zeros(len(k3))
k1Ar_mp = np.zeros(len(k1Ar))
k1CO2_mp = np.zeros(len(k1CO2))
L = np.array([1.243,1.244])
for i in range(1,len(k2)+1):
    k2_mp[i-1] = i
for i in range(1,len(k4)+1):
    k4_mp[i-1] = i
for i in range(1,len(k3)+1):
    k3_mp[i-1] = i
for i in range(1,len(k1Ar)+1):
    k1Ar_mp[i-1] = i
for i in range(1,len(k1CO2)+1):
    k1CO2_mp[i-1] = i
s2 = sp.linregress(k2_mp,k2)
s4 = sp.linregress(k4_mp,k4)
s3 = sp.linregress(k3_mp,k3)
s1Ar = sp.linregress(k1Ar_mp,k1Ar)
s1CO2 = sp.linregress(k1CO2_mp,k1CO2)
s = np.array([s2,s4,s3,s1Ar,s1CO2])
c = np.zeros(5)
cError = np.zeros(5)
c[0] = s2[0]*L[0]*2
c[1] = s4[0]*L[1]*2
c[2] = s3[0]*L[1]*2
c[3] = s1Ar[0]*L[0]*2
c[4] = s1CO2[0]*L[0]*2
for i in range(5):
    if i == 1 or i == 2:
        j = 1
        cError[i] = c[i]*np.sqrt((s[i][4]/s[i][0])**2 + (1.5e-3/L[j])**2)
    else:
        j = 0
        cError[i] = c[i]*np.sqrt((s[i][4]/s[i][0])**2 + (1.5e-3/L[j])**2)
print(c)
print(cError)
T = np.linspace(293.15,353.15,200)
def v_s(T, M):
    return np.sqrt((gamma*R*T)/M)
gamma = 5/3
R = 1.380e-23 * 6.022e23
plt.plot(T, v_s(T,4.002602e-3))
plt.plot(T,v_s(T,20.17e-3))
plt.plot(T,v_s(T,39.948e-3))
plt.plot(T,v_s(T,83.8e-3))
new = sp.linregress([25,50,70],[c[0],c[1],c[2]])
plt.plot(T,new[0]*(T-272.15)+new[1])
plt.legend(['Helium','Neon','Argon','Krypton','Oxygen'])
plt.xlabel('Temperature [K]')
plt.ylabel('Speed of Sound [m/s]')
plt.show()