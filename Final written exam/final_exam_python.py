import numpy as np
import scipy.stats as stats

x = [1, 3.4, 5, 14.4, 11.5, 8.2, 0.6, 2.7, 26.8, 3.0,
1.3, 20.2, 4, 14, 3.3, 1.8, 1.7, 4.6, 7.4, 7.1,
5.2, 23.6, 1.6, 1.1, 15.5, 3, 1.9, 4.2, 27.4, 1.5]

m = np.median(x) #estimat for medianen
n = np.mean(x) #estimat for gjennomsnitt

l=np.size(x) #størrelse
s=np.std(x) #sigma

h = stats.norm.interval(0.95, loc=n, scale=s/l) #intervallet for gjennomsnitt
f = stats.norm.interval(0.95, loc=m, scale=s/l) #intervallet for median

print("Estimat for median er %g"%(m))
print("Estimat for gjennomsnitt er %g"%(n))
print("Tilnærmet 95% konfidensintervall for medianen er")
print(f)
print(" tilnærmet 95% konfidensintervall for gjennomsnitt")
print(h)

B = 10000
meanvec = []
medianvec = []
for i in range(B):
  xstar = stats.norm.rvs(n, s, size=l)
  meanvec.append(np.mean(xstar))
  medianvec.append(np.median(xstar))

print("Standardfeilen til estimat for gjennomsnitt er %g" %(np.std(meanvec)))
print("Standardfeilen til estimat for median er %g" %(np.std(medianvec)))
