import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

doed = pd.read_csv("https://www.uio.no/studier/emner/matnat/math/STK1100/v20/doedelighet.txt", sep="\t")
alder = doed["alder"].values
menn = doed["menn"].values

qx = menn[35:]/1000
Sx = np.cumprod(1-qx)
Fx = 1-Sx

tmp = np.zeros(72)
tmp[1:72] = Fx[0:71]
px = Fx-tmp

x = alder[35:]

width = 1
plt.bar(x, px, width, edgecolor="black")
plt.xlabel("Alder")
plt.ylabel("Punktsannsynlighet")
plt.show()

x=np.arange(0,72)

hx=(100000/1.03**x)*(x>=32)
EhX=sum(hx*px)
print("E[h(x)]=", EhX)

gx=(1-(1/1.03)**(np.minimum(x,34)+1))/(1-(1/1.03))
EgX=sum(gx*px)
print("E[g(x)]=", EgX)
