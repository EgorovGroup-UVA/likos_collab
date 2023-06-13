# Generating g(r) from MD with LAMMPs' radial distribution function

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data Importing #
d1 = pd.read_csv('/home/wtf8hu/MAIN/plots/case1oneone.txt', sep =' ', skiprows = 4,header=None)
d2 = pd.read_csv('/home/wtf8hu/MAIN/plots/case1onetwo.txt', sep =' ', skiprows = 4,header=None)
d3 = pd.read_csv('/home/wtf8hu/MAIN/plots/case1twotwo.txt', sep =' ', skiprows = 4,header=None)
d4 = pd.read_csv('/home/wtf8hu/MAIN/plots/case2oneone.txt', sep =' ', skiprows = 4,header=None)
d5 = pd.read_csv('/home/wtf8hu/MAIN/plots/case2onetwo.txt', sep =' ', skiprows = 4,header=None)
d6 = pd.read_csv('/home/wtf8hu/MAIN/plots/case2twotwo.txt', sep =' ', skiprows = 4,header=None)
d7 = pd.read_csv('/home/wtf8hu/MAIN/plots/case3oneone.txt', sep =' ', skiprows = 4,header=None)
d8 = pd.read_csv('/home/wtf8hu/MAIN/plots/case3onetwo.txt', sep =' ', skiprows = 4,header=None)
d9 = pd.read_csv('/home/wtf8hu/MAIN/plots/case3twotwo.txt', sep =' ', skiprows = 4,header=None)
# -------- #

fig, axs = plt.subplots(3, sharex=True)

# SUBPLOT 1 #
r= d1.iloc[0:, 1].dropna().to_numpy(); gr = d1.iloc[0:, 2].dropna().to_numpy()
axs[0].plot(r, gr,color="black")

r= d2.iloc[0:, 1].dropna().to_numpy(); gr = d2.iloc[0:, 2].dropna().to_numpy()
axs[0].plot(r, gr,color="red")

r= d3.iloc[0:, 1].dropna().to_numpy(); gr = d3.iloc[0:, 2].dropna().to_numpy()
axs[0].plot(r, gr, color="blue")

# SUBPLOT 2 #
r= d4.iloc[0:, 1].dropna().to_numpy(); gr = d4.iloc[0:, 2].dropna().to_numpy()
axs[1].plot(r, gr,color="black")

r= d5.iloc[0:, 1].dropna().to_numpy(); gr = d5.iloc[0:, 2].dropna().to_numpy()
axs[1].plot(r, gr,color="red")

r= d6.iloc[0:, 1].dropna().to_numpy(); gr = d6.iloc[0:, 2].dropna().to_numpy()
axs[1].plot(r, gr, color="blue")

# SUBPLOT 3 #
r= d7.iloc[0:, 1].dropna().to_numpy(); gr = d7.iloc[0:, 2].dropna().to_numpy()
axs[2].plot(r, gr,color="black")

r= d8.iloc[0:, 1].dropna().to_numpy(); gr = d8.iloc[0:, 2].dropna(4).to_numpy()
axs[2].plot(r, gr,color="red")

r= d9.iloc[0:, 1].dropna().to_numpy(); gr = d9.iloc[0:, 2].dropna().to_numpy()
axs[2].plot(r, gr, color="blue")
# -------- #

axs[2].tick_params(left = True, direction="inout")

axs[0].tick_params(bottom = True, top = True, right = True, direction = "in",length = 4,labelsize=14)
axs[1].tick_params(bottom = True, top = True, right = True, direction = "in",length = 4,labelsize=14)
axs[2].tick_params(bottom = True, top = True, right = True, direction = "in",length = 4,labelsize=14)

plt.xlabel(r"r/$\sigma$",fontsize = 14)

# axs[0].y_label(r"$g_{11}$(r)")

plt.subplots_adjust(wspace =0,hspace =0.0001)

axs[0].margins(x=0)
axs[1].margins(x=0)
axs[2].margins(x=0)

for ax in axs:
    #ax.set(ylabel='y-label')
    axs[0].set_ylabel(r'$g_{11}$(r)',fontsize=14)
    axs[1].set_ylabel(r'$g_{12}$(r)',fontsize=14)
    axs[2].set_ylabel(r'$g_{22}$(r)',fontsize=14)
# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs:
    ax.label_outer()

axs[0].set_ylim([0.80,1.5])
axs[1].set_ylim([0.80,1.7])
axs[2].set_ylim([0.50, 2.6])
axs[0].set_xlim([0,4])

axs[0].set_yticks([0.9, 1.0,1.1,1.2,1.3,1.4,1.5])
axs[1].set_yticks([1.0,1.2,1.4,1.6])
axs[2].set_yticks([0.5,1.0,1.5,2.0,2.5])

plt.xticks([0, 1, 2, 3, 4])

plt.show()