import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d
 
X = [2,3,4,6,12,18,22,33,40,45,50,57]

Y = [4.5,10,16,37,120,10,83.9,65,64,66,70,71]


f = interp1d(X,Y, kind='linear')
n = f(3.5) #interponlacion de 3.5

print(n)

y = f(X)

plt.plot(X,y, label = 'interpolacion')
plt.show()
