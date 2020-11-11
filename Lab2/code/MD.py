import lammps_logfile
import matplotlib.pyplot as plt
import numpy as np

log = lammps_logfile.File("log.lammps")
data = []
x = log.get("Temp")
y = log.get("TotEng")
plt.plot(x,y)
plt.xlabel('Temperature [K]')
plt.ylabel('Total Energy of system')
plt.title('Total energy of our system as we increase temperature')
plt.show()