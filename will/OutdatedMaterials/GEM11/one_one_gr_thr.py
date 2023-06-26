import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('/home/wtf8hu/lammps/likos_collab/will/GEM11/oneone_thr.txt', sep =' ', skiprows = 4, header=None)
r= data.iloc[0:, 1].dropna().to_numpy()
gr = data.iloc[0:, 2].dropna().to_numpy()
c3 = data.iloc[0:, 3].dropna().to_numpy()

print(data)

plt.xlabel("r")
plt.ylabel("g(r)")
plt.ylim([0.85,1.5])
plt.plot(r, gr,color='black')
#plt.savefig('/home/dell/lammps/projects/likoslab/one_one_gr/EquilDamp/images/test.png', dpi = 700)
plt.show()
