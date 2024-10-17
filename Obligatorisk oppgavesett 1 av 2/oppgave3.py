import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

url = "https://www.uio.no/studier/emner/matnat/math/STK1100/v20/doedelighet.txt"
doed = pd.read_csv(url, sep="\t")
alder = doed["alder"].values
menn = doed["menn"].values

qx = menn[35:]/1000
Sx = np.cumprod(1-qx)
Fx = 1-Sx

tmp = np.zeros(72)
tmp[1:72] = Fx[0:71]
px = Fx - tmp

x = alder[35:]

plt.bar(x, px, width=1, edgecolor="black")
plt.xlabel("Alder")
plt.ylabel("Punktsannsynlighet")
plt.show()

x = np.arange(0, 72)

hx = np.zeros(72)
for i in range(32, 72):
     hx[i] = 100000 * np.sum(1/(1.03 ** np.arange(32, i+1)))

EhX = sum(hx * px)
print("E[h(x)]=", EhX)

gx = (1 - (1/1.03)**(np.minimum(x,31)+1))/(1 - (1/1.03)) 

EgX = sum(gx*px) 
print("E[g(x)]=", EgX)
