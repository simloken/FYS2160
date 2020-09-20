# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
file = open('termokopper.txt', 'r')
f = file.readlines()
data = []
for i in f:
        data.append(i.split('\t'))

ndata = []
getlen = len(data)
for i in range(len(data)):
    for j in data[i]:
        ndata.append(j.strip())
data = np.zeros((3,getlen))
for i in [0,1,2]:
    data[i] = ndata[i::3]

plt.plot(data[0],data[1])
plt.plot(data[0],data[2])
plt.title('Temperatures in two steel thermo mugs over %g seconds' %(data[0][getlen-1]))
plt.legend(['Mug A','Mug B'])
plt.xlabel('Seconds [s]')
plt.ylabel('Temperature [C]')
plt.show()