# -*- coding: utf-8 -*-
import lammps_logfile
import matplotlib.pyplot as plt
import numpy as np
log = lammps_logfile.File("log.lammps")
vels = open("lmaotemp.lammpstrj", "r")
v = vels.readlines()
data = []
x = log.get("Temp")
y = log.get("TotEng")
plt.plot(x,y)
CV = x/y
print(np.mean(CV))
print(np.std(CV))
plt.show()
vels.close()
tv = ([[1.49948, -0.114314, 1.39652],
[-1.4974, -0.621795, 0.661926], 
[1.14418, 1.74067, -0.899157], 
[-1.7679, 0.0944875, -0.881728], 
[0.408638, -1.60964, -0.927935], 
[-0.357638, 0.36183, 1.45065], 
[1.36583, -0.213783, -0.917162], 
[1.09349, 1.0172, -0.964581], 
[1.34942, 0.628734, -0.217633], 
[-1.25276, -1.60659, -0.746578], 
[0.945492, 0.84165, 1.62025], 
[1.1565, -2.06983, -0.767166], 
[0.453629, 1.37962, -1.65859],
[1.56037, 1.07708, 0.0222623], 
[0.990732, 0.553375, -0.796413], 
[-0.965454, 0.834479, -0.869487], 
[-1.60677, 0.290256, 0.00830711], 
[-0.450748, 1.40394, 0.776034]])
vs = np.zeros(len(tv))
for i in range(len(tv)):
    vs[i] = np.sqrt(tv[i][0]**2+tv[i][1]**2+tv[i][2])
lol = np.sum(vs)
lol = lol/len(vs)
lol = np.sqrt(lol)
std = np.std(vs)
print(lol, std)